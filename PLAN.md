# Plan: costa-rica-law

Layout approved 2026-11-26. Source: SINALEVI (sinalevi.go.cr).

## 2. Principles

1. **Folders follow the kind of Costa Rican norm**, Spanish names as SINALEVI and searchers write them, ASCII-folded
   (`constitucion`, `leyes`, `decretos-ejecutivos`, `reglamentos`), as argentina-law / brazil-law do. Machine folders
   `data/`, `tools/`, `visualisations/`, `vulnerabilities/` as in every lexifina repo.
2. **Act trees** (one folder per norm, one file per article, one commit per SINALEVI version, repeal = commit deleting
   the files) and **document trees** (one file per record as issued, never changed: Gaceta issues, pronunciamientos,
   judgments).
3. **Dating: one commit per version at 12:00 America/Costa_Rica (-0600, no DST) on the in-force day** of that
   version (SINALEVI "Fecha de vigencia desde" / the version's own date, else the Gaceta publication date). Trailers:
   `In-force:`, `In-force-evidence:` (`SINALEVI ficha <id> versión k de N` or `La Gaceta <n> del <fecha>`),
   `Published:`, `Gazette:`, `Affecting:`. Real dates before 1970 kept (as the wip-build did, back to 1821). Future
   versions wait on a `future` branch. Late finds are appended as `Kind: correction`; no rewrite after launch.
4. Author = the norm that made the change (SINALEVI's affecting list; Sala Constitucional "anulado por" notes credit
   the voto), `<tipo>-<numero>@sinalevi.invalid`; committer `Lexifina <costa-rica-law@lexifina.com>`. No personal
   names in paths.
5. ≤1,000 entries per folder: year folders under every bulk kind.

## 3. Top level

| Folder | Holds | Path | Example |
| --- | --- | --- | --- |
| `constitucion/` | Constitución Política 1949, every version; historic constitutions 1821-1917 as their own folders | `constitucion/1949/articulo-<n>.md`, `transitorio-<n>.md` | `constitucion/1949/articulo-48.md` |
| `codigos/` | the codes in force (Civil, Penal, Procesal Civil, Procesal Penal, Trabajo, Comercio, Familia, Normas y Procedimientos Tributarios, Municipal, Niñez, Electoral, Procesal Contencioso-Administrativo, Minería, Aduanero, ...), every version | `codigos/<slug>/articulo-<n>.md`; folder README gives "Ley N° ..." | `codigos/codigo-penal/articulo-111.md` (Ley 4573) |
| `leyes/` | every other Ley | `leyes/<numero>/articulo-<n>.md`; pre-1922 numbers repeat each year, so duplicates are `leyes/<numero>-<año>/` | `leyes/8968/articulo-5.md`, `leyes/63-1887/` |
| `tratados/` | Tratados Internacionales (with their approving Ley in the README) | `tratados/<año>/<slug-o-ley>/` | `tratados/1970/convencion-americana-ddhh/` |
| `decretos-ejecutivos/` | Decretos Ejecutivos, every version | `decretos-ejecutivos/<año>/<numero>-<siglas>/articulo-<n>.md` | `decretos-ejecutivos/2024/44871-mp/` |
| `reglamentos/` | Reglamentos of autonomous bodies, by issuer | `reglamentos/<ente>/<año>/<slug>/` | `reglamentos/ccss/2023/reglamento-salud/` |
| `municipal/` | reglamentos and acuerdos municipales | `municipal/<municipalidad>/<año>/<slug>/` | `municipal/san-jose/2019/...` |
| `tse/` | Decretos del Tribunal Supremo de Elecciones | `tse/<año>/<numero>/` | |
| `acuerdos/`, `directrices/`, `circulares/`, `resoluciones/` | the remaining SINALEVI types, by year | `<tipo>/<año>/<numero-o-slug>/` | |
| `la-gaceta/` | issues as published, text layer only (document tree) | `la-gaceta/<año>/<mm>/<dd>.md` (+ `alcance-<n>.md`) | `la-gaceta/2005/01/03.md` |
| `procuraduria/` | PGR dictámenes and opiniones jurídicas (document tree) | `procuraduria/dictamenes/<año>/c-<nnn>-<año>.md`, `opiniones-juridicas/<año>/oj-<nnn>-<año>.md` | `procuraduria/dictamenes/2024/c-012-2024.md` |
| `sala-constitucional/`, `salas/` | slots for judgments (Nexus unreachable; see Needs Alan) | `sala-constitucional/<año>/<mm>/<dd>/voto-<nnnnn>-<año>.md` (never party names) | |
| `data/` | `normas.csv` (ficha -> path, tipo, número, versions), `hosts.json` (terms, date read), `issues.csv` | | |
| `tools/` | `in_force_on.py`, `check.py`, `test_repo.py` (from the wip-build) | | |
| root | `README.md` (Spanish) + `README.en.md`, same commit always; `LICENSE` (Lexifina's work CC0; each source's terms); `REPRODUCE.md`, `PLAN.md`, `corpus.json`, `jurisdiction.json` | | |

Article files: `articulo-<n>.md` (`articulo-12-bis.md`, `articulo-transitorio-i.md`), `anexo-<n>.md`,
`preambulo.md`; headings (Título, Capítulo, Sección) stay as heading lines in the next article. Each norm folder has
a `README.md` with its version table (version, in force, made by, Gaceta).

## 4. Lanes (after approval)

| Lane | Host | Writes | Requests | Time at 5 in flight |
| --- | --- | --- | --- | --- |
| cr-core | SINALEVI | Constitución 1949 + the ~15 codes in force, every version (card 1 first to get the real N) | ~1.5k | < 30 min, first commits day 1 |
| cr-leyes | SINALEVI | all 21,273 Leyes + constituciones, versions from cards (fixes the "* de *" gap) | ~100k | ~6-8 h |
| cr-decretos | SINALEVI | Decretos Ejecutivos, then Reglamentos, Tratados, the other types | ~300k (all non-Ley types) | ~15-20 h |
| cr-gaceta | imprentanacional.go.cr `/pub/` | la-gaceta 2003- (text layer; stop at first 403/429/challenge) | ~8.5k days probed, ~5.7k PDFs | ~1 day at 2 in flight (Cloudflare host) |
| cr-pgr | SINALEVI | procuraduria/ (count first) | ~2 × records | ~1 day |
| cr-sala | Nexus | only if Alan gets access | | |

Pacing: 5 in flight on SINALEVI (no stated limit), no daily cap; stop at the first 403/429/challenge; back off on
5xx/disconnects; one ~15 MB text (Ley 8764) needs a long timeout.

**ETA to max completion of the reachable record: ~1.5-2 days elapsed** (SINALEVI decrees/reglamentos are the long
pole; Gaceta runs in parallel). Core codes with full history within the first hour; all Leyes within the first day.

