# How this repository is made

1. `python tools/build/fetch.py lists` downloads SINALEVI's list of every Constitución, Ley and Tratado
   Internacional (`/ResultadosNormativa/Resultados`, by year windows).
2. `python tools/build/fetch.py norms` downloads, for each norm, every version's card
   (`_BuscarVersionNorma`; the number of versions N is read from the version-1 card), full text
   (`_CargarTextoCompleto`) and the norms that affected it (`ViewAfectacion/_CargarVistaNormaQueLaAfecto`), plus the
   version-1 card of each affecting norm (for its in-force date). At most 5 requests in flight; the run stops at the
   first 403 or 429.
3. `python tools/build/build.py <repo> --mode first|append --fichas <list> --today <day>` writes one commit per
   version with `git fast-import`: one file per article (`textparse.py`), dated 12:00 America/Costa_Rica on the day
   the version took effect, authored by the norm that made it. `core.json` maps the Constitution and the codes to
   their folders.

No AI model runs when these files are built. The build code was written by Claude Code (Claude Opus 5.5).
