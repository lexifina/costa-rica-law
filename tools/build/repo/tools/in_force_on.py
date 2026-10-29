"""Print a Costa Rican norm, or one article of it, as this repository has it in force on a date.

    python tools/in_force_on.py 2016-01-01 constitucion/1949                 # the whole Constitution
    python tools/in_force_on.py 2016-01-01 constitucion/1949 articulo-1      # one article
    python tools/in_force_on.py 2026-10-28 ley/7472 articulo-2               # a Ley

Picks the last commit on `main` whose `In-force:` trailer is on or before the date (commit dates before 1970 are
clamped, so the trailer is the real date). Changes after the build date are on the `future` branch: pass --future to
include them. Standard library only.
"""
import subprocess
import sys


def git(*args: str) -> str:
    return subprocess.run(['git', *args], capture_output=True, text=True, encoding='utf-8', check=True).stdout


def commit_on(day: str, path: str, ref: str) -> tuple[str | None, str | None]:
    fmt = '%H%x1f%(trailers:key=In-force,valueonly,separator=)'
    earliest = None
    for line in git('log', '--no-merges', '--first-parent', f'--format={fmt}', ref, '--', path).splitlines():
        h, d = (line.split('\x1f') + [''])[:2]
        d = d.strip()
        if not d:
            continue
        earliest = d
        if d <= day:
            return h, d
    return None, earliest


def main() -> None:
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8')
    args = [x for x in sys.argv[1:] if x != '--future']
    ref = 'future' if '--future' in sys.argv else 'main'
    if len(args) < 2:
        sys.exit(__doc__)
    day, law = args[0], args[1].strip('/')
    unit = args[2] if len(args) > 2 else None
    if unit and unit.endswith('.md'):
        unit = unit[:-3]
    path = f'{law}/{unit}.md' if unit else law
    h, when = commit_on(day, path, ref)
    if not h:
        sys.exit(f'{path}: no version in force on {day}' + (f' (the record starts on {when})' if when else ' (not found)'))
    if not unit and law.count('/') == 0:
        # a whole folder of norms (`ley`, `constitucion`): list each norm's files with their blob ids as of the date
        sys.stdout.write(git('ls-tree', '-r', h, f'{law}/'))
        return
    try:
        if unit:
            sys.stdout.write(git('show', f'{h}:{path}'))
            return
        names = [n for n in git('show', f'{h}:{law}/index.txt').splitlines() if n]
    except subprocess.CalledProcessError:
        sys.exit(f'{path}: not in force on {day} (removed by the commit in force on {when})')
    for n in names:
        sys.stdout.write(git('show', f'{h}:{law}/{n}') + '\n')


if __name__ == '__main__':
    main()
