"""Build the Costa Rica law repository from the SINALEVI cache (fetch.py).

    python scripts/costa-rica-law/build.py C:/Users/alany/Documents/costa-rica-law --today 2026-10-28 [--limit N]

SINALEVI keeps, for every norm, numbered versions ("Version de la Norma: k de N del <date>"), the full text of each,
and for each version the list of norms that had affected the norm up to that version. So:

1. Each version of the Constitution or a Ley is a set of files: one per article (`articulo-1.md`, in the order of the
   text, Title and Chapter headings on top of the first article under them), one paragraph per line, plus `index.txt`.
2. The norms that first appear in version k's affecting list are the causes of version k. With one cause, the commit is
   authored by that norm (`Kind: amendment`) and dated by its in-force date ("Fecha de vigencia desde" on its SINALEVI
   card). With several, SINALEVI's text cannot be split between them: the publisher is the author, every cause is a
   `Candidate:` line, and the date is the latest of their in-force dates (`Kind: combined`). With none, the publisher
   is the author and the date is the version date (`Kind: unexplained`, `Evidence: version-date`).
3. Version 1 is the norm as enacted, authored by the norm itself and dated by its own in-force date (`Kind: enacted`),
   unless its affecting list already names amending norms: then SINALEVI's first version is already a consolidation and
   it is labelled `Kind: consolidated`, authored by the publisher, with one `Consolidates:` line per amending norm.
4. A norm whose whole text was repealed or annulled by a named norm loses its files on that norm's in-force date
   (`Kind: repeal`).
5. Commits run in in-force order. A version whose cause took effect before the norm's previous version is dated with the
   previous one and keeps its own date in `Cause-in-force:`. Changes by one norm on one day are one commit.
   Changes in force after --today go on the `future` branch, which starts at main's head and is never merged.
"""
import argparse
import csv
import io
import json
import os
import re
import shutil
import stat
import subprocess
import sys
from datetime import datetime, timezone
from html import unescape
from pathlib import Path

import textparse

HERE = Path(__file__).parent
CACHE = HERE / '.cache'
SITE = 'https://sinalevi.go.cr'
COMMITTER = 'Lexifina <costa-rica-law@lexifina.com>'
PUBLISHER = ('SINALEVI (Procuraduria General de la Republica)', 'sinalevi@pgr-go-cr.invalid')
REPEAL = re.compile(r'derog|anula', re.I)
DMY = re.compile(r'(\d{2})/(\d{2})/(\d{4})')


# ---------------------------------------------------------------------------------------------------- dates

# Costa Rica: UTC-6, with daylight time (UTC-5) only in these spans (IANA tzdata America/Costa_Rica).
CR_DST = [('1979-02-25', '1979-06-03'), ('1980-02-24', '1980-06-01'), ('1991-01-19', '1991-07-01'),
          ('1992-01-18', '1992-03-15')]


def offset(day: str) -> int:
    return -5 if any(a <= day < b for a, b in CR_DST) else -6


def git_date(day: str, seq: int) -> str:
    """Noon in Costa Rica. Before 1970: 1970-01-01 plus seq seconds (the real date is in the In-force trailer)."""
    if day < '1970-01-01':
        return f'{21600 + seq} -0600'  # 1970-01-01 00:00 in Costa Rica, plus seq seconds
    off = offset(day)
    y, m, d = map(int, day.split('-'))
    ts = int(datetime(y, m, d, 12 - off, 0, tzinfo=timezone.utc).timestamp())
    return f'{ts} {"-" if off < 0 else "+"}{abs(off):02d}00'


def iso(dmy: str | None) -> str | None:
    m = DMY.search(dmy or '')
    if not m:
        return None
    d = f'{m.group(3)}-{m.group(2)}-{m.group(1)}'
    return d if d > '1700' else None


# ---------------------------------------------------------------------------------------------------- cache

def load_json(p: Path):
    try:
        return json.loads(p.read_text('utf-8'))
    except (OSError, json.JSONDecodeError):
        return None


def norm_rows() -> list[dict]:
    seen = {}
    for f in sorted((CACHE / 'lists').glob('*.json')):
        rows = load_json(f)
        if isinstance(rows, list):
            for r in rows:
                seen[r['IdFichaNorma']] = r
    return [seen[k] for k in sorted(seen)]


def n_versions(row: dict) -> int:
    m = re.search(r'(\d+)\s+de\s+(\d+)', row.get('VersionNorma') or '')
    return int(m.group(2)) if m else 1


def complete(row: dict) -> bool:
    f = row['IdFichaNorma']
    for k in range(1, n_versions(row) + 1):
        d = load_json(CACHE / 'cards' / f'{f}_{k}.json')
        vid = (d or {}).get('idVersionNorma')
        if not vid or not (CACHE / 'text' / f'{f}_{vid}.json').exists() or not (CACHE / 'aff' / f'{f}_{vid}.json').exists():
            return False
    return True


def card_info(ficha: int, k: int) -> dict | None:
    d = load_json(CACHE / 'cards' / f'{ficha}_{k}.json')
    if not d or 'error' in d or not d.get('idVersionNorma'):
        return None
    t = textparse.norm(unescape(re.sub(r'<[^>]+>', ' ', d.get('html') or '')))
    info = {'vid': d['idVersionNorma'], 'text': t}
    m = re.search(r'Ficha de la Norma\s+(.+?):\s*(\S+)\s+del\s+(\d{2}/\d{2}/\d{4})\s+(.*?)\s+Datos Generales', t)
    if m:
        info.update(tipo=m.group(1).strip(), numero=m.group(2), fecha=iso(m.group(3)), nombre=m.group(4).strip())
    m = re.search(r'Versi\u00f3n de la Norma:\s*(\d+)\s+de\s+(\d+)\s+del\s+(\d{2}/\d{2}/\d{4})', t)
    if m:
        info.update(k=int(m.group(1)), n=int(m.group(2)), version_date=iso(m.group(3)))
    m = re.search(r'Fecha de vigencia desde:\s*(\d{2}/\d{2}/\d{4})', t)
    info['vigencia'] = iso(m.group(1)) if m else None
    m = re.search(r'N\u00b0 Gaceta:\s*(\S+)\s+del\s+(\d{2}/\d{2}/\d{4})', t)
    if m:
        info.update(gaceta=m.group(1), gaceta_date=iso(m.group(2)))
    m = re.search(r'Ente Emisor:\s*(.+?)\s+(?:Fecha de vigencia|Versi\u00f3n de la Norma)', t)
    if m:
        info['ente'] = m.group(1).strip()
    return info


def affecting(ficha: int, vid: int) -> dict[int, dict] | None:
    """{cause ficha: {tipo, numero, fecha, nombre, effects: [(article, tipo de afectacion)]}}; None if not fetched."""
    d = load_json(CACHE / 'aff' / f'{ficha}_{vid}.json')
    if d is None or 'error' in d:
        return None
    out: dict[int, dict] = {}
    for top in d.get('rows') or []:
        art = top.get('ArticuloAfectado') or 0
        for a in top.get('lstViewAfectacion') or []:
            f = a.get('IdFichaNorma')
            if not f:
                continue
            c = out.setdefault(f, {'tipo': (a.get('DescTipoNorma') or '').strip(), 'numero': a.get('NumeroNormativa'),
                                   'fecha': (a.get('FechaNormativa') or '')[:10], 'nombre': textparse.norm(a.get('NombreNormativa') or ''),
                                   'effects': set()})
            for b in a.get('lstViewAfectacion') or [{}]:
                c['effects'].add((art, textparse.norm(b.get('DescTipoAfectacion') or '')))
    return out


def text_units(ficha: int, vid: int) -> list[tuple[str, str, list[str]]] | None:
    d = load_json(CACHE / 'text' / f'{ficha}_{vid}.json')
    if not d or 'error' in d or 'html' not in d:
        return None
    return textparse.parse(d['html'])


# ---------------------------------------------------------------------------------------------------- names

def ascii_slug(s: str) -> str:
    return textparse.label_slug('x ' + (s or ''))[2:] or 'x'


def law_dir(row: dict) -> str:
    if row['IdTipoNorma'] == 1:
        return f"constitucion/{(row.get('FechaNormativa') or '0000')[:4]}"
    sub = (row.get('IdSubNumeroNormativa') or '0').strip()
    num = row.get('NumeroNormativa')
    return f"ley/{num}" + (f'-{ascii_slug(sub)}' if sub not in ('', '0') else '')


def norm_label(tipo: str, numero, fecha: str | None) -> str:
    tipo = (tipo or 'Norma').strip()
    if tipo.lower().startswith('constituci'):
        return f'Constituci\u00f3n Pol\u00edtica ({(fecha or "")[:4]})'
    return f'{tipo} {numero}' + (f' ({fecha})' if fecha and not tipo.lower().startswith('ley') else '')


def author_of(cause: dict) -> tuple[str, str]:
    tipo = cause.get('tipo') or 'Norma'
    num = cause.get('numero')
    if tipo.lower().startswith('ley'):
        email = f'ley-{num}@sinalevi.invalid'
        name = f'Ley {num} ({cause.get("fecha") or "?"})'
    elif tipo.lower().startswith('constituci'):
        email = f'constitucion-{(cause.get("fecha") or "")[:4]}@sinalevi.invalid'
        name = f'Constituci\u00f3n Pol\u00edtica ({(cause.get("fecha") or "")[:4]})'
    else:
        email = f'{ascii_slug(tipo)}-{num}-{cause.get("fecha") or "x"}-f{cause["ficha"]}@sinalevi.invalid'
        name = f'{tipo} {num} ({cause.get("fecha") or "?"})'
    return name, email


# ---------------------------------------------------------------------------------------------------- events

def cause_info(f: int, base: dict, cards: dict) -> dict:
    """Merge an affecting-list entry with the cause's own SINALEVI card (in-force date, Gazette)."""
    c = dict(base)
    c['ficha'] = f
    card = cards.get(f)
    if card is None:
        card = card_info(f, 1)
        cards[f] = card
    if card:
        c['vigencia'] = card.get('vigencia')
        c['gaceta'] = card.get('gaceta')
        c['gaceta_date'] = card.get('gaceta_date')
        c['ente'] = card.get('ente')
        c['fecha'] = c.get('fecha') or card.get('fecha')
    when, src = c.get('vigencia'), 'vigencia'
    if not when:
        when, src = c.get('gaceta_date'), 'gazette-date'
    if not when:
        when, src = c.get('fecha'), 'norm-date'
    c['in_force'], c['date_source'] = when, src
    return c


def law_events(row: dict, cards: dict, issues: list) -> tuple[list[dict], dict]:
    """The versions of one norm as events, in version order, plus the law's record for laws.csv."""
    ficha = row['IdFichaNorma']
    path = law_dir(row)
    n = n_versions(row)
    law = {'ficha': ficha, 'path': path, 'tipo': row.get('NombreTipoNorma') or '', 'numero': row.get('NumeroNormativa'),
           'nombre': textparse.norm(row.get('NombreNormativa') or ''), 'fecha': (row.get('FechaNormativa') or '')[:10],
           'estado': (row.get('EstadoNorma') or '').strip(), 'versions': n, 'built_versions': 0}
    events: list[dict] = []
    prev_causes: set[int] = set()
    prev_date = ''
    last_aff: dict | None = None
    for k in range(1, n + 1):
        also: list[dict] = []
        card = card_info(ficha, k)
        if not card:
            issues.append([path, k, 'version card not fetched'])
            continue
        tp = CACHE / 'text' / f"{ficha}_{card['vid']}.json"
        try:
            with open(tp, 'rb') as fh:
                head = fh.read(12)
        except OSError:
            head = b''
        if not head.startswith(b'{"html"'):
            issues.append([path, k, 'text not fetched' if not head else 'text: error answer'])
            continue
        units = None  # parsed when the commit is written, to keep memory flat
        aff = affecting(ficha, card['vid'])
        if aff is None:
            issues.append([path, k, 'affecting list not fetched'])
            aff = {}
        last_aff = aff
        new = sorted(set(aff) - prev_causes)
        prev_causes |= set(aff)
        if k == 1:
            law.update(vigencia=card.get('vigencia'), gaceta=card.get('gaceta'), gaceta_date=card.get('gaceta_date'),
                       ente=card.get('ente'))
            own = cause_info(ficha, {'tipo': law['tipo'], 'numero': law['numero'], 'fecha': law['fecha'],
                                     'nombre': law['nombre'], 'effects': set()}, cards)
            if new:
                causes = [cause_info(f, aff[f], cards) for f in new]
                kind = 'consolidated'
                when = max([own['in_force'] or ''] + [c['in_force'] or '' for c in causes]) or card.get('version_date')
                src = 'latest in-force date of the norm and the amendments it includes'
            else:
                causes = [own]
                kind = 'enacted'
                when, src = own['in_force'], own['date_source']
        else:
            causes = [cause_info(f, aff[f], cards) for f in new]
            dated = [c for c in causes if c.get('fecha') and c['fecha'] == card.get('version_date')]
            if len(causes) > 1 and len(dated) == 1:
                # SINALEVI dates a version by the norm that made it: credit that one, list the others it newly names
                also = [c for c in causes if c is not dated[0]]
                causes = [dated[0]]
            if len(causes) == 1:
                kind = 'amendment'
                when, src = causes[0]['in_force'], causes[0]['date_source']
            elif causes:
                years = {(c.get('fecha') or '')[:4] for c in causes}
                kind = 'combined' if len(years) <= 2 and len(causes) <= 3 else 'consolidated'
                when = max(c['in_force'] or '' for c in causes)
                src = 'latest in-force date of the causes'
            else:
                kind = 'unexplained'
                when, src = card.get('version_date'), 'version-date'
        if not when:
            when, src = card.get('version_date') or law['fecha'] or '1900-01-01', 'version-date'
        cause_when = when
        if when < prev_date:
            when = prev_date
        prev_date = when
        events.append({'law': law, 'k': k, 'n': n, 'vid': card['vid'], 'units': units, 'kind': kind, 'causes': causes,
                       'also': also,
                       'in_force': when, 'cause_in_force': cause_when, 'date_source': src,
                       'version_date': card.get('version_date')})
        law['built_versions'] += 1
    # whole-norm repeal or annulment by a named norm
    if events and REPEAL.search(law['estado']) and last_aff:
        whole = [f for f, c in last_aff.items() if any(a == 0 and REPEAL.search(t) for a, t in c['effects'])]
        if whole:
            causes = [cause_info(f, last_aff[f], cards) for f in sorted(whole)]
            best = max(causes, key=lambda c: (c['in_force'] or '', c['ficha']))
            when = best['in_force'] or prev_date
            events.append({'law': law, 'k': n + 1, 'n': n, 'vid': None, 'units': None, 'kind': 'repeal',
                           'causes': [best] if len(causes) == 1 else causes, 'in_force': max(when, prev_date),
                           'cause_in_force': when, 'date_source': best['date_source'], 'version_date': None})
            law['repealed'] = when
    return events, law


def collapse_same_day(events: list[dict]) -> list[dict]:
    """Consecutive versions of one norm on one day with the same author become one event (the last text).
    Versions by different authors on one day stay separate commits, in SINALEVI's order."""
    out: list[dict] = []
    for e in events:
        if (out and out[-1]['in_force'] == e['in_force'] and out[-1]['kind'] != 'repeal' and e['kind'] != 'repeal'
                and author_key(out[-1]) == author_key(e)):
            p = out[-1]
            seen = {c['ficha'] for c in p['causes']}
            causes = p['causes'] + [c for c in e['causes'] if c['ficha'] not in seen]
            kinds = {p['kind'], e['kind']}
            if 'consolidated' in kinds:
                kind = 'consolidated'
            elif len(causes) == 1:
                kind = 'enacted' if causes[0]['ficha'] == e['law']['ficha'] else 'amendment'
            elif not causes:
                kind = 'unexplained'
            else:
                kind = 'combined'
            also = (p.get('also') or []) + (e.get('also') or [])
            out[-1] = {**e, 'kind': kind, 'causes': causes, 'also': also, 'k_from': p.get('k_from', p['k'])}
        else:
            out.append(e)
    return out


def author_key(e: dict) -> tuple:
    if e['kind'] in ('enacted', 'amendment', 'repeal') and len(e['causes']) == 1:
        return ('norm', e['causes'][0]['ficha'])
    return ('publisher', e['law']['path'], e['kind'])


def order_groups(events: list[dict]) -> list[list[dict]]:
    """Commits in in-force order; on one day, one commit per author, each norm's versions kept in order."""
    by_day: dict[str, list[dict]] = {}
    for e in events:
        by_day.setdefault(e['in_force'], []).append(e)
    groups: list[list[dict]] = []
    for day in sorted(by_day):
        evs = sorted(by_day[day], key=lambda e: (e['law']['path'], e['k']))
        queue: dict[str, list[dict]] = {}
        for e in evs:
            queue.setdefault(e['law']['path'], []).append(e)
        pending = {}
        for e in evs:
            pending.setdefault(author_key(e), []).append(e)
        while pending:
            pick = None
            for key in sorted(pending):
                if all(queue[e['law']['path']][0] is e for e in pending[key]):
                    pick = key
                    break
            if pick is None:  # a cycle between authors: write the first author's ready events alone
                key = sorted(pending)[0]
                ready = [e for e in pending[key] if queue[e['law']['path']][0] is e]
                if not ready:
                    key = next(k for k in sorted(pending) if any(queue[e['law']['path']][0] is e for e in pending[k]))
                    ready = [e for e in pending[key] if queue[e['law']['path']][0] is e]
                g = ready
                pending[key] = [e for e in pending[key] if not any(e is r for r in ready)]
                if not pending[key]:
                    del pending[key]
            else:
                g = pending.pop(pick)
            for e in g:
                queue[e['law']['path']].pop(0)
            groups.append(g)
    return groups


# ---------------------------------------------------------------------------------------------------- writing

def unit_text(label: str, lines: list[str]) -> str:
    return '\n'.join(lines) + '\n' if lines else ''


def law_files(e: dict) -> dict[str, str]:
    path = e['law']['path']
    files = {}
    order = []
    units = text_units(e['law']['ficha'], e['vid']) or []
    for slug, label, lines in units:
        t = unit_text(label, lines)
        if not t:
            continue
        files[f'{path}/{slug}.md'] = t
        order.append(f'{slug}.md')
    if order:
        files[f'{path}/index.txt'] = '\n'.join(order) + '\n'
    return files


def message(group: list[dict], when: str) -> tuple[str, str, str]:
    e0 = group[0]
    key = author_key(e0)
    laws = [e['law'] for e in group]
    if key[0] == 'norm':
        c = e0['causes'][0]
        name, email = author_of(c)
        own = all(e['kind'] == 'enacted' for e in group)
        who = norm_label(c.get('tipo'), c.get('numero'), c.get('fecha'))
        if e0['kind'] == 'repeal':
            what = 'repeals ' + ', '.join(norm_label(l['tipo'], l['numero'], l['fecha']) for l in laws)
        elif own:
            what = 'enacted, in force'
        else:
            what = 'amends ' + ', '.join(norm_label(l['tipo'], l['numero'], l['fecha']) for l in laws)
        subject = f'{who}: {what}'
    else:
        name, email = PUBLISHER
        l = laws[0]
        lab = norm_label(l['tipo'], l['numero'], l['fecha'])
        subject = {'combined': f'{lab}: SINALEVI version combining {len(e0["causes"])} amending norms',
                   'consolidated': f'{lab}: SINALEVI version folding in {len(e0["causes"])} earlier changes',
                   'unexplained': f'{lab}: SINALEVI version with no amending norm named'}[e0['kind']]
    if len(subject) > 72:
        subject = subject[:71].rstrip(' ,;') + '\u2026'
    body = []
    for e in group:
        l = e['law']
        lab = norm_label(l['tipo'], l['numero'], l['fecha'])
        ver = (f"versions {e['k_from']}-{e['k']}" if e.get('k_from') else f"version {e['k']}") + f" of {e['n']}"
        if e['kind'] == 'repeal':
            body.append(f"{lab} ({l['nombre']}): repealed or annulled as a whole; its files are removed.")
        else:
            body.append(f"{lab} ({l['nombre']}): SINALEVI {ver}, dated {e['version_date'] or '?'}.")
        if e['cause_in_force'] != e['in_force']:
            body.append(f"  Its cause took effect on {e['cause_in_force']}, before the previous version of this norm; "
                        f"it is placed on {e['in_force']} to keep the norm's versions in order.")
        if e['kind'] == 'consolidated':
            body.append('  SINALEVI did not keep a version for each of the amending norms this text already includes '
                        '(it began keeping versions about 2001), so it is credited to none of them; they are listed '
                        'in Consolidates trailers.')
        if e['kind'] == 'combined':
            body.append('  This version adds several amending norms at once; the text cannot be split between them.')
        if e['kind'] == 'unexplained':
            body.append('  No amending norm is newly named for this version (a correction, or a change SINALEVI does not attribute).')
    tr = [f"Kind: {e0['kind']}", f'In-force: {when}']
    srcs = sorted({e['date_source'] for e in group})
    for s in srcs:
        if s != 'vigencia':
            tr.append(f'Evidence: {s}')
    for e in group:
        if e['cause_in_force'] != e['in_force']:
            tr.append(f"Cause-in-force: {e['cause_in_force']}")
    if key[0] == 'norm':
        c = e0['causes'][0]
        if c.get('fecha'):
            tr.append(f"Enacted: {c['fecha']}")
        if c.get('gaceta_date'):
            tr.append(f"Published: {c['gaceta_date']}")
        if c.get('gaceta'):
            tr.append(f"Gazette: La Gaceta {c['gaceta']}")
        tr.append(f"Norm: {norm_label(c.get('tipo'), c.get('numero'), c.get('fecha'))}")
    else:
        lines = 'Candidate' if e0['kind'] == 'combined' else 'Consolidates'
        for c in sorted(e0['causes'], key=lambda c: (c.get('in_force') or '', c['ficha'])):
            if c['ficha'] == e0['law']['ficha']:
                continue
            tr.append(f"{lines}: {norm_label(c.get('tipo'), c.get('numero'), c.get('fecha'))}, in force {c.get('in_force') or '?'}")
    for e in group:
        for c in sorted(e.get('also') or [], key=lambda c: c['ficha']):
            tr.append(f"Also-named: {norm_label(c.get('tipo'), c.get('numero'), c.get('fecha'))}")
    for e in group:
        tr.append(f"Affecting: {e['law']['path']}")
    for e in group:
        if e['vid']:
            tr.append(f"Version: {e['law']['path']} {e['k']}/{e['n']}")
    for e in group:
        if e['vid']:
            tr.append(f"Source: {SITE}/ResultadosNormativa/Informacion?param1={e['law']['ficha']}&param2={e['vid']}&param3=1")
    msg = '\n'.join([subject, '', *body, '', *tr]) + '\n'
    return f'{name} <{email}>', subject, msg


class Writer:
    def __init__(self, repo: Path):
        self.p = subprocess.Popen(['git', '-C', str(repo), 'fast-import', '--quiet', '--done', '--force'],
                                  stdin=subprocess.PIPE)
        self.mark = 0
        self.w = self.p.stdin.write

    def commit(self, ref: str, author: str, when: str, msg: str, changes: list[tuple[str, str | None]],
               parent: int | None) -> int:
        self.mark += 1
        w = self.w
        w(f'commit {ref}\nmark :{self.mark}\n'.encode())
        w(f'author {author} {when}\ncommitter {COMMITTER} {when}\n'.encode())
        m = msg.encode('utf-8')
        w(f'data {len(m)}\n'.encode() + m + b'\n')
        if parent:
            w(f'from :{parent}\n'.encode())
        for path, text in changes:
            if text is None:
                w(f'D {path}\n'.encode('utf-8'))
            else:
                t = text.encode('utf-8')
                w(f'M 100644 inline {path}\ndata {len(t)}\n'.encode('utf-8') + t + b'\n')
        w(b'\n')
        return self.mark

    def finish(self) -> None:
        self.w(b'done\n')
        self.p.stdin.close()
        if self.p.wait():
            sys.exit('git fast-import failed')


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument('repo', type=Path)
    ap.add_argument('--today', required=True)
    ap.add_argument('--limit', type=int)
    ap.add_argument('--only', type=int, nargs='*', help='IdFichaNorma values (for tests)')
    ap.add_argument('--complete-only', action='store_true', help='only norms with every version cached (WIP builds)')
    a = ap.parse_args()
    if not re.fullmatch(r'\d{4}-\d{2}-\d{2}', a.today):
        sys.exit('--today must be YYYY-MM-DD')
    fo = CACHE / 'fetched_on.txt'
    fetched_on = fo.read_text('utf-8').strip() if fo.exists() else a.today
    if fetched_on > a.today:
        sys.exit(f'retrieval date {fetched_on} is after --today {a.today}')

    rows = norm_rows()
    if a.only:
        rows = [r for r in rows if r['IdFichaNorma'] in a.only]
    if a.complete_only:
        rows = [r for r in rows if complete(r)]
    if a.limit:
        rows = rows[:a.limit]
    # folder names: duplicates of number (and sub-number) get the SINALEVI ficha appended
    dirs: dict[str, list[dict]] = {}
    for r in rows:
        dirs.setdefault(law_dir(r), []).append(r)
    cards: dict = {}
    issues: list[list] = []
    events: list[dict] = []
    laws: list[dict] = []
    for d, rs in sorted(dirs.items()):
        for r in rs:
            ev, law = law_events(r, cards, issues)
            if len(rs) > 1:
                law['path'] = f"{d}-f{r['IdFichaNorma']}"
            laws.append(law)
            events += collapse_same_day(ev)
    groups = order_groups(events)
    print(f'{len(laws)} norms, {len(events)} events, {len(groups)} commits, {len(issues)} issues', flush=True)

    repo = a.repo
    remote = None
    if repo.exists() and any(repo.iterdir()):
        if not (repo / '.git').exists():
            sys.exit(f'{repo} is not empty and not an earlier build')
        r = subprocess.run(['git', '-C', str(repo), 'remote', 'get-url', 'origin'], capture_output=True, text=True)
        remote = r.stdout.strip() or None

        def onerr(func, path, _):
            os.chmod(path, stat.S_IWRITE)
            func(path)
        for child in repo.iterdir():
            shutil.rmtree(child, onerror=onerr) if child.is_dir() else child.unlink()
    repo.mkdir(parents=True, exist_ok=True)
    subprocess.run(['git', 'init', '-q', '-b', 'main', str(repo)], check=True)
    for k, v in (('core.autocrlf', 'false'), ('core.longpaths', 'true'), ('core.quotepath', 'false')):
        subprocess.run(['git', '-C', str(repo), 'config', k, v], check=True)
    if remote:
        subprocess.run(['git', '-C', str(repo), 'remote', 'add', 'origin', remote], check=True)

    wr = Writer(repo)
    state: dict[str, dict[str, str]] = {}  # law path -> {file: text}
    parent = None
    seq = 0
    stats = {'commits': 0, 'empty': 0, 'kinds': {}, 'future': 0}
    unchanged: list[list] = []
    main_head = None
    future_groups = [g for g in groups if g[0]['in_force'] > a.today]
    main_groups = [g for g in groups if g[0]['in_force'] <= a.today]
    log_rows: list[list] = []
    for ref, gs in (('refs/heads/main', main_groups), ('refs/heads/future', future_groups)):
        if ref.endswith('future'):
            if not gs:
                break
            parent = main_head
        for g in gs:
            changes: list[tuple[str, str | None]] = []
            for e in g:
                path = e['law']['path']
                old = state.get(path, {})
                new = {} if e['kind'] == 'repeal' else law_files(e)
                for f in sorted(set(old) | set(new)):
                    if old.get(f) != new.get(f):
                        changes.append((f, new.get(f)))
                if not any(c[0].startswith(path + '/') for c in changes):
                    unchanged.append([path, e['k'], e['kind'], e['in_force'], 'text identical to the previous version'])
                state[path] = new
            if not changes:
                stats['empty'] += 1
                continue
            seq += 1
            when = g[0]['in_force']
            author, subject, msg = message(g, when)
            parent = wr.commit(ref, author, git_date(when, seq), msg, changes, parent)
            stats['commits'] += 1
            stats['kinds'][g[0]['kind']] = stats['kinds'].get(g[0]['kind'], 0) + 1
            if ref.endswith('future'):
                stats['future'] += 1
            log_rows.append([when, g[0]['kind'], author.split(' <')[0], ';'.join(e['law']['path'] for e in g)])
        if ref.endswith('main'):
            # documentation commit, dated by the data's retrieval day
            import docs as docmod
            files = docmod.render(laws, events, issues, unchanged, stats, a.today, fetched_on)
            seq += 1
            dmsg = (f'Documentation: README, REPRODUCE, corpus.json, tools and data\n\n'
                    f'Built from the SINALEVI cache retrieved on {fetched_on}.\n\n'
                    f'Kind: documentation\nIn-force: {fetched_on}\n')
            parent = wr.commit(ref, COMMITTER, git_date(fetched_on, seq), dmsg,
                               [(p, t) for p, t in sorted(files.items())], parent)
            main_head = parent
    wr.finish()
    subprocess.run(['git', '-C', str(repo), 'checkout', '-q', '-f', 'main'], check=True)
    head = subprocess.run(['git', '-C', str(repo), 'rev-parse', 'HEAD'], capture_output=True, text=True).stdout.strip()
    print(f"built {repo}: {stats['commits'] + 1} commits on main+future ({stats['future']} future), kinds {stats['kinds']}, "
          f"{stats['empty']} groups with no text change, head {head}", flush=True)


if __name__ == '__main__':
    main()
