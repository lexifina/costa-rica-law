# Costa Rica: law history in git

[Español](README.md)

The law of Costa Rica as a git history: one file per article, one commit per version dated the day it took effect (12:00 Costa Rica time), and the norm that made each change as the commit's author. `git blame` names the law behind every line; `git log` lists every change to an article; a date gives the text in force that day.

Part of [lexifina/global-law](https://github.com/lexifina/global-law), which reads this repository as `cr/national/acts`.

**What is in it now:** the Constitución Política of 1949 and the codes in force (Civil, Penal, Trabajo, Comercio, Procesal Civil, Procesal Penal, Familia, Normas y Procedimientos Tributarios, Municipal, Electoral, Niñez y Adolescencia and others), with every version SINALEVI keeps. The Leyes and the international treaties are added as they are downloaded. See the [PLAN.md](PLAN.md).

The texts are in Spanish, as SINALEVI publishes them.

## Layout

| Folder | Holds | Example |
| --- | --- | --- |
| `constitucion/` | the Constitución Política of 1949, every version; the historic constitutions, each in its own folder | `constitucion/1949/articulo-48.md` |
| `codigos/` | the codes in force, every version | `codigos/codigo-penal/articulo-111.md` (Ley N° 4573) |
| `leyes/` | every other Ley; numbers before 1922 repeat, and then carry the year | `leyes/8968/articulo-5.md`, `leyes/63-1887/` |
| `tratados/` | international treaties, by year | `tratados/1970/<name>/` |

Each norm has a `README.md` with its SINALEVI record and version table, and `index.txt` with the order of its articles.

## Commits

- Date: 12:00 America/Costa_Rica on the day the version took effect (dates before 1970: 1970-01-01, the real date in the `In-force:` trailer).
- Author: the norm that made the change (`ley-<n>@sinalevi.invalid`); where SINALEVI folds several norms into one version, the author is SINALEVI and the norms are in `Candidate:` or `Consolidates:` trailers.
- Trailers: `In-force:`, `In-force-evidence:`, `Enacted:`, `Published:`, `Gazette:`, `Affecting:`, `Version:`, `Source:`.
- Changes in force in the future are on the `future` branch.

## Source

| Source | What | Versions |
| --- | --- | --- |
| [SINALEVI](https://sinalevi.go.cr) (Sistema Nacional de Legislación Vigente, Procuraduría General de la República) | the full text of every norm | yes: numbered versions of each norm, each with its text and the norms that affected it |

## Licence

See [`LICENSE`](LICENSE). Lexifina's work (structure, documentation, tools, commit text) is CC0 1.0. No AI wrote legal text.
