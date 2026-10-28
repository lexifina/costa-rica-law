# The laws of Costa Rica, as a git repository

The Constitución Política and every Ley of Costa Rica as a git history: 31 norms (30 Leyes and 1 constitutions), with the 1439 versions that SINALEVI, the Sistema Nacional de Legislación Vigente of the Procuraduría General de la República, keeps for them. Each version is a commit, dated by the day the change took effect. There is one file per article, with one paragraph per line, so `git blame` and `git log -p` work article by article and line by line. The text is in Spanish, as published.

The record runs from 1949-11-08 to 2026-09-02, in 1221 commits on `main`. 0 changes that take effect after 2026-10-28 are on the `future` branch.

## A lawyer's questions as git commands

| Question | Command |
| --- | --- |
| What did article 1 of the Constitution say on 1 January 2015? | `python tools/in_force_on.py 2015-01-01 constitucion/1949 articulo-1` |
| The whole Constitution as in force on a date | `python tools/in_force_on.py 2015-01-01 constitucion/1949` |
| Which norms changed an article, and when? | `git log --format="%(trailers:key=In-force,valueonly,separator=) %an" -- constitucion/1949/articulo-50.md` |
| Which norm wrote each line of an article? | `git blame constitucion/1949/articulo-50.md` |
| What exactly did a change do, word by word? | `git log -p --word-diff -- constitucion/1949/articulo-50.md` |
| Everything one amending law changed | `git log --author="^Ley 9849 " --stat` |
| Every law that took effect in 2020 | `git log --since=2020-01-01T00:00:00-06:00 --until=2020-12-31T23:59:59-06:00 --format="%ad %an" --date=short` |
| The list of norms, with their dates and states | [`laws.csv`](laws.csv) |
| Each version, its causes and their dates | [`data/versions.csv`](data/versions.csv) |

Use the tool rather than `git rev-list --before=DATE`. A bare date in `--before` takes the time of day you run it, and every commit sits at noon in Costa Rica, so the answer on the day a law took effect would depend on the clock. Dates before 1970 are also clamped (see below), and the tool reads the real date from the `In-force:` trailer. In PowerShell, `git show $(...):path` splits into two arguments, so use `$r = git rev-list ...; git show "$($r):path"`. After a rebuild, run `git fetch --force --tags`.

Folders: `constitucion/1949/` (and the historic constitutions SINALEVI lists, by year), and `ley/<number>/` for each Ley. A number shared by two SINALEVI records gets the record's ficha number appended (`ley/12-f4567`). Each file is one article as SINALEVI splits the text (`articulo-1.md`, `articulo-12-bis.md`, `transitorio-i.md`). The Title and Chapter headings printed above an article are the first lines of its file, and the notes SINALEVI prints under an article are kept as they are: `(Así reformado por el artículo único de la Ley N° 9305 del 24 de agosto del 2015)`. `index.txt` lists a norm's files in the order of the text. Text after a norm's last article is in `final.md`, and a norm that SINALEVI does not split into articles is one file, `texto.md`.

## The dates, and which one we use

Each SINALEVI version is dated by the norm that made it (`Versión de la Norma: 18 de 28 del 24/08/2015`), and each norm's card gives the day it took effect (`Fecha de vigencia desde: 01/10/2015`) and its publication in La Gaceta. **Each commit is dated by the in-force date of the norm that caused the version**, at noon in Costa Rica (UTC−6; UTC−5 during the daylight-time spans of 1979, 1980, 1991 and 1992). That date is also in the `In-force:` trailer. `Enacted:` is the date of the norm, `Published:` and `Gazette:` give its La Gaceta issue. When a norm's card has no in-force date, the Gazette date is used, then the norm's own date, and the commit says so in an `Evidence:` trailer.

Some versions have a cause that took effect before the norm's previous version. They are dated with the previous version, so that a norm's versions stay in their order, and the cause's own date is kept in `Cause-in-force:` (94 versions). Git cannot store dates before 1970. Commits in force before then are dated 1970-01-01 at midnight in Costa Rica, a second apart and in order, and the real date is in `In-force:`.

## What "author" means

The author of a commit is the norm that made the change, at an address that cannot exist, so `git blame` names the law:
- `Ley 9305 (2015-08-24) <ley-9305@sinalevi.invalid>`: an amending law (1237 versions, `Kind: amendment`). Changes made by one law on one day are one commit, across all the norms it changed.
- The norm itself, for its first version (21, `Kind: enacted`).
- The repealing norm, when a whole norm is repealed or annulled and its files are removed (3, `Kind: repeal`).
- Resolutions of the Sala Constitucional and the Tribunal Supremo de Elecciones, which SINALEVI records as changing a text, are authors in the same way.

The publisher, `SINALEVI (Procuraduria General de la Republica) <sinalevi@pgr-go-cr.invalid>`, is the author when the text cannot be credited to one norm. That happens in three cases:
- `Kind: combined` (4): a version that adds several amending norms at once. Each is named in a `Candidate:` trailer.
- `Kind: consolidated` (20): SINALEVI began keeping versions about 2001. For most older norms, the first version it kept, or the first after the original text, already includes amendments made before then, and they are listed in `Consolidates:` trailers.
- `Kind: unexplained` (131): a version for which SINALEVI names no new amending norm, such as a correction.

When a version newly names several norms and exactly one has the version's own date, that one is credited, and the others are listed as `Also-named:`. 1092 distinct norms are credited with at least one change.

Blame credits whole lines (paragraphs), so a paragraph changed by two laws shows only the later one; use `--word-diff`.

## What it does not show

- **Changes before about 2001, one by one.** For most norms older than that, SINALEVI's first version, or its second, folds earlier amendments into one text, and those commits are labelled `consolidated`. So the history of the Constitution between 1949 and 2000 is the 1949 text, then a single commit in force on 2000-07-26 with its 47 amendments listed.
- **Text that SINALEVI does not record as a change.** The applicability of a change, or its transitional rules, is not extracted (`scope.when_absent` in corpus.json).
- **Executive decrees, regulations and treaties.** Only Leyes and constitutions are included.
- **Problems in the source.** Some norms could not be read (0 versions, listed in [`data/issues.csv`](data/issues.csv)). 59 versions have the same text as the version before them; they are listed in [`data/unchanged.csv`](data/unchanged.csv) and make no commit.
- **Pictures in the text** (marked `[imagen]`).

This is a research aid. SINALEVI is the Procuraduría's database, not the official Gazette. The official text is the one published in La Gaceta.

## How it is checked

- `tools/in_force_on.py` was compared with SINALEVI's own version pages for sample articles on several dates.
- Every commit carries an `In-force:` trailer, and every trailer block parses with `git interpret-trailers --parse`.
- `main` has no merges and no date that goes backwards, and nothing in force after the build date.
- `scripts/global-law/check_corpus.py` passes.
- Two builds from the same cache give the same commit hashes.

See [`REPRODUCE.md`](REPRODUCE.md).

## How it is built

`fetch.py` reads the lists of norms from SINALEVI's search, then, for every version of every norm, its card, its full text and the list of norms that had affected it up to that version. `build.py` splits each text into articles (`textparse.py`), works out each version's cause from the norms that first appear in its affecting list, and writes the history with one streamed `git fast-import`. No AI model takes part in building or checking it, and no AI wrote or changed any legal text.

## Licence

Source: SINALEVI, Sistema Costarricense de Información Jurídica, Procuraduría General de la República de Costa Rica (https://sinalevi.go.cr). The site states "© Procuraduría de la República. Todos los derechos reservados" and publishes no reuse terms. Ley 6683 (Ley de Derechos de Autor y Derechos Conexos), artículo 75, permits anyone to reproduce laws and other official acts freely, on condition that they follow the official edition strictly. The wording here was not changed; it was only split into files and lines. **This repository is private.** Lexifina's own contributions (the tools, the arrangement and the commit messages) are CC0. See [`LICENSE`](LICENSE).
