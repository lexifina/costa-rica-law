"""Fetch the Constitution and every Ley from SINALEVI (https://sinalevi.go.cr), with every version it keeps.

    python scripts/costa-rica-law/fetch.py lists            # the list of norms, by decade
    python scripts/costa-rica-law/fetch.py norms [--workers 4]  # cards, texts and affecting-norm lists per version
    python scripts/costa-rica-law/fetch.py causes           # the card of every affecting norm outside the corpus

SINALEVI (Sistema Nacional de Legislacion Vigente, Procuraduria General de la Republica) has no robots.txt (404 on
sinalevi.go.cr, www.sinalevi.go.cr and pgrweb.go.cr on 2026-10-28) and no terms of use beyond "Todos los derechos
reservados". At most 5 requests run at once, each with a User-Agent naming this project.

Endpoints (the site's own AJAX calls, all POST form data, answers JSON with an `html` member):
  /ResultadosNormativa/Resultados (GET, the search result page; its listView data is embedded JSON)
  /ResultadosNormativa/_BuscarVersionNorma   idFichaNorma, numeroVersion     -> version card + idVersionNorma
  /ResultadosNormativa/_CargarTextoCompleto  idFichaNorma, version, busqueda -> full text of that version
  /ViewAfectacion/_CargarVistaNormaQueLaAfecto idFichaNorma, version         -> norms that affected it, up to that version
Everything is cached under .cache/ (negative answers too, as {"error": ...}), so reruns only fetch what is missing.
"""
import argparse
import json
import re
import sys
import threading
import time
import urllib.error
import urllib.parse
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

HERE = Path(__file__).parent
CACHE = HERE / '.cache'
BASE = 'https://sinalevi.go.cr'
UA = 'Mozilla/5.0 (compatible; lexifina-git-for-law/1.0; +https://lexifina.com; legislation history research)'
TYPES = {1: 'Constitucion Politica', 8: 'Ley', 15: 'Tratados Internacionales'}
LOCK = threading.Lock()
COUNT = {'requests': 0}


_LOCAL = threading.local()


def _conn(fresh: bool = False):
    """One persistent HTTPS connection per thread (keep-alive): the TLS handshake was 0.5 s of a 0.7 s request."""
    import http.client
    if fresh or getattr(_LOCAL, 'c', None) is None:
        if getattr(_LOCAL, 'c', None) is not None:
            try:
                _LOCAL.c.close()
            except Exception:  # noqa: BLE001
                pass
        _LOCAL.c = http.client.HTTPSConnection('sinalevi.go.cr', timeout=900)
    return _LOCAL.c


class Stop(Exception):
    pass


STOP_FILE = HERE / '.stop'


def request(path: str, data: dict | None = None, get: dict | None = None, timeout: int = 300, tries: int = 4) -> bytes:
    url = path + ('?' + urllib.parse.urlencode(get) if get else '')
    body = urllib.parse.urlencode(data).encode() if data is not None else None
    headers = {'User-Agent': UA, 'Accept-Encoding': 'gzip', 'Connection': 'keep-alive'}
    if body is not None:
        headers['Content-Type'] = 'application/x-www-form-urlencoded'
    last = None
    for i in range(tries):
        if STOP_FILE.exists():
            raise Stop(STOP_FILE.read_text('utf-8'))
        try:
            c = _conn(fresh=i > 0)
            c.request('POST' if body is not None else 'GET', url, body=body, headers=headers)
            r = c.getresponse()
            raw = r.read()
            with LOCK:
                COUNT['requests'] += 1
            if r.getheader('Content-Encoding') == 'gzip':
                import gzip
                raw = gzip.decompress(raw)
            if r.status == 200:
                return raw
            last = RuntimeError(f'HTTP {r.status}')
            if r.status in (403, 429):
                # never get round a refusal: back off once, then stop the whole run
                if i >= 1:
                    STOP_FILE.write_text(f'HTTP {r.status} on {url}\n', 'utf-8')
                    raise Stop(f'HTTP {r.status}')
                time.sleep(120)
                continue
            if r.status in (400, 404) and i >= 1:
                raise last
            if r.status >= 500:
                time.sleep(20 * (i + 1))
        except Stop:
            raise
        except Exception as e:  # noqa: BLE001  timeouts, resets
            last = e
            _conn(fresh=True)
        time.sleep(5 * (i + 1))
    raise RuntimeError(f'{path} {data or get}: {last}')


_LOGGED = {'n': 0}


def log_requests(step: str) -> None:
    """Append the requests made since the last entry, so an interrupted run still counts (REPRODUCE.md sums them)."""
    with LOCK:
        n = COUNT['requests'] - _LOGGED['n']
        _LOGGED['n'] = COUNT['requests']
    with open(CACHE / 'requests.log', 'a', encoding='utf-8') as fh:
        fh.write(time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()) + chr(9) + step + chr(9) + str(n) + chr(10))


def save(p: Path, obj) -> None:
    p.parent.mkdir(parents=True, exist_ok=True)
    tmp = p.with_suffix('.part')
    tmp.write_text(json.dumps(obj, ensure_ascii=False), 'utf-8')
    tmp.replace(p)


def embedded_data(page: str) -> list[dict]:
    i = page.find('"data":{"Data":')
    if i < 0:
        return []
    obj, _ = json.JSONDecoder().raw_decode(page[i + 7:])
    return obj['Data']


# ------------------------------------------------------------------------------------------------ lists

def _list(tipo: int, y0: int, y1: int) -> None:
    p = CACHE / 'lists' / f'{tipo}_{y0}_{y1}.json'
    if p.exists():
        return
    try:
        page = request('/ResultadosNormativa/Resultados', get={
            'TipoBusqueda': 2, 'Pagina': 1, 'ListaTipoNorma': tipo, 'radioFechas': 'annios',
            'AnnioDesde': y0, 'AnnioHasta': y1, 'NormasHistoricas': 'false', 'CantidadResultados': -1},
            timeout=900, tries=2).decode('utf-8')
    except Stop:
        raise
    except Exception:  # noqa: BLE001  big windows drop the connection: split
        if y1 > y0:
            m = (y0 + y1) // 2
            _list(tipo, y0, m)
            _list(tipo, m + 1, y1)
            return
        raise
    rows = embedded_data(page)
    if not rows and 'listView' not in page:
        rows = {'error': 'no result list on the page'}
    save(p, rows)
    print(f'list {TYPES[tipo]} {y0}-{y1}: {len(rows) if isinstance(rows, list) else rows}', flush=True)


def fetch_lists(types=None) -> None:
    ranges = [(1800, 1899)] + [(y, y + 9) for y in range(1900, 1970, 10)] + [(y, y + 4) for y in range(1970, 2030, 5)]
    jobs = [(t, a, b) for t in (types or TYPES) for a, b in ranges]
    with ThreadPoolExecutor(5) as pool:
        for f in [pool.submit(_list, *j) for j in jobs]:
            f.result()
    fo = CACHE / 'fetched_on.txt'
    if not fo.exists():
        fo.write_text(time.strftime('%Y-%m-%d', time.gmtime()) + '\n', 'utf-8')


def norms() -> list[dict]:
    seen = {}
    for f in sorted((CACHE / 'lists').glob('*.json')):
        rows = json.loads(f.read_text('utf-8'))
        if isinstance(rows, dict):
            continue
        for r in rows:
            seen[r['IdFichaNorma']] = r
    return [seen[k] for k in sorted(seen)]


def n_versions(row: dict) -> int:
    m = re.search(r'(\d+)\s+de\s+(\d+)', row.get('VersionNorma') or '')
    return int(m.group(2)) if m else 1


# ------------------------------------------------------------------------------------------------ per norm

def card(ficha: int, n: int) -> dict:
    p = CACHE / 'cards' / f'{ficha}_{n}.json'
    if p.exists():
        return json.loads(p.read_text('utf-8'))
    try:
        d = json.loads(request('/ResultadosNormativa/_BuscarVersionNorma', {'idFichaNorma': ficha, 'numeroVersion': n}))
    except Exception as e:  # noqa: BLE001
        d = {'error': str(e)[:300]}
    save(p, d)
    return d


def text(ficha: int, vid: int) -> None:
    p = CACHE / 'text' / f'{ficha}_{vid}.json'
    if p.exists():
        return
    try:
        d = json.loads(request('/ResultadosNormativa/_CargarTextoCompleto',
                               {'idFichaNorma': ficha, 'version': vid, 'busqueda': ''}, timeout=900))
    except Exception as e:  # noqa: BLE001
        d = {'error': str(e)[:300]}
    save(p, d)


def affecting(ficha: int, vid: int) -> None:
    p = CACHE / 'aff' / f'{ficha}_{vid}.json'
    if p.exists():
        return
    try:
        d = json.loads(request('/ViewAfectacion/_CargarVistaNormaQueLaAfecto', {'idFichaNorma': ficha, 'version': vid},
                               timeout=900))
        page = d.get('html') or ''
        d = {'rows': embedded_data(page)}
    except Exception as e:  # noqa: BLE001
        d = {'error': str(e)[:300]}
    save(p, d)


VN = re.compile(r'Versi(?:\u00f3|&#xF3;|o)n de la Norma:\s*(\d+)\s+de\s+(\d+)', re.I)


def card_n(c: dict) -> int | None:
    m = VN.search(re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', ' ', c.get('html') or '')))
    return int(m.group(2)) if m else None


def done_marker(ficha: int) -> Path:
    return CACHE / 'done' / f'{ficha}.json'


def do_norm(row: dict) -> str:
    """Every version of one norm (N read from the version-1 card, not the list), plus version-1 cards of its causes."""
    ficha = row['IdFichaNorma']
    if done_marker(ficha).exists():
        return f'{ficha} (cached)'
    c1 = card(ficha, 1)
    n = card_n(c1) or n_versions(row)
    causes = set()
    for k in range(1, n + 1):
        c = c1 if k == 1 else card(ficha, k)
        vid = c.get('idVersionNorma')
        if not vid:
            continue
        text(ficha, vid)
        affecting(ficha, vid)
        d = json.loads((CACHE / 'aff' / f'{ficha}_{vid}.json').read_text('utf-8'))
        for top in d.get('rows') or []:
            for a in top.get('lstViewAfectacion') or []:
                if a.get('IdFichaNorma'):
                    causes.add(a['IdFichaNorma'])
    for f in sorted(causes):
        card(f, 1)
    bad = [k for k in range(1, n + 1) if 'error' in json.loads((CACHE / 'cards' / f'{ficha}_{k}.json').read_text('utf-8'))]
    if not bad:
        save(done_marker(ficha), {'n': n})
    return f'{ficha} ({n})'


def fetch_norms(workers: int, only: list[int] | None) -> None:
    rows = norms()
    if only:
        rows = [r for r in rows if r['IdFichaNorma'] in only]
    # Constitution and codes first, then treaties, then by list version count (largest first)
    pri = {int(k) for k in json.loads((HERE / 'core.json').read_text('utf-8'))}
    rows.sort(key=lambda r: (r['IdFichaNorma'] not in pri, r.get('IdTipoNorma') != 15, -n_versions(r), r['IdFichaNorma']))
    print(f'{len(rows)} norms, {sum(n_versions(r) for r in rows)} versions', flush=True)
    t0 = time.time()
    done = 0
    with ThreadPoolExecutor(workers) as pool:
        futs = [pool.submit(do_norm, r) for r in rows]
        for fut in as_completed(futs):
            try:
                fut.result()
            except Stop as e:
                print(f'STOP {e}', flush=True)
                pool.shutdown(wait=False, cancel_futures=True)
                return
            except Exception as e:  # noqa: BLE001
                print(f'FAIL {e}', file=sys.stderr, flush=True)
            done += 1
            if done % 100 == 0 or done == len(rows):
                el = time.time() - t0
                line = (f'{time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())} {done}/{len(rows)} norms, '
                        f'{COUNT["requests"]} requests, {el:.0f}s, {COUNT["requests"] / max(el, 1):.1f} req/s')
                print(line, flush=True)
                with open(HERE / 'progress.log', 'a', encoding='utf-8') as fh:
                    fh.write(line + chr(10))
                log_requests('norms')
    print(f'norms done: {COUNT["requests"]} requests in {time.time() - t0:.0f}s', flush=True)


def fetch_causes(workers: int) -> None:
    """Cards (version 1) of every norm named in an affecting list, so each cause has its in-force date."""
    want = set()
    for f in (CACHE / 'aff').glob('*.json'):
        d = json.loads(f.read_text('utf-8'))
        for top in d.get('rows') or []:
            for a in top.get('lstViewAfectacion') or []:
                if a.get('IdFichaNorma'):
                    want.add(a['IdFichaNorma'])
    todo = sorted(f for f in want if not (CACHE / 'cards' / f'{f}_1.json').exists())
    print(f'{len(want)} affecting norms, {len(todo)} cards to fetch', flush=True)
    with ThreadPoolExecutor(workers) as pool:
        list(pool.map(lambda f: card(f, 1), todo))
    print(f'causes done: {COUNT["requests"]} requests', flush=True)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument('step', choices=['lists', 'norms', 'causes'])
    ap.add_argument('--workers', type=int, default=5)
    ap.add_argument('--only', type=int, nargs='*')
    a = ap.parse_args()
    a.workers = min(a.workers, 5)
    if a.step == 'lists':
        fetch_lists(a.only)
    elif a.step == 'norms':
        fetch_norms(a.workers, a.only)
    else:
        fetch_causes(a.workers)
    log_requests(a.step)  # only the requests not yet logged (norms logs every 100 norms as it goes)


if __name__ == '__main__':
    main()
