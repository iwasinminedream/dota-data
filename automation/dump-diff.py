#!/usr/bin/env python3
"""
Compares two raw dumps (dumper/dump) section by section. Two dumps of the same Dota build should
be identical; whatever differs is the dumper being unreliable ("glitches"), not the game.

    dump-diff.py A B [--out REPORT.md] [--title TEXT]

Exit code 0: identical (the steam.inf header is ignored), 1: they differ, 2: usage/IO error.
"""
import argparse
import difflib
import re
import sys

SHOW_LINES = 60
# Lines that legitimately differ between runs (timings).
VOLATILE = re.compile(r'^Time: [0-9.]+$')


def sections(path):
    text = open(path, encoding='utf-8', errors='replace').read()
    parts = re.split(r'^\$> (.+)\n', text, flags=re.M)
    return {parts[i]: [l for l in parts[i + 1].splitlines() if not VOLATILE.match(l)]
            for i in range(1, len(parts), 2)}


def main():
    p = argparse.ArgumentParser()
    p.add_argument('a')
    p.add_argument('b')
    p.add_argument('--out')
    p.add_argument('--title', default='Control dump')
    args = p.parse_args()
    try:
        a, b = sections(args.a), sections(args.b)
    except OSError as e:
        print(e, file=sys.stderr)
        return 2

    rows, details = [], []
    for name in list(a) + [n for n in b if n not in a]:
        la, lb = a.get(name), b.get(name)
        if la == lb:
            continue
        if la is None or lb is None:
            rows.append((name, 'only in ' + ('second' if la is None else 'first'), len(la or lb)))
            continue
        diff = [d for d in difflib.unified_diff(la, lb, lineterm='', n=0) if not d.startswith(('---', '+++'))]
        added = sum(1 for d in diff if d.startswith('+'))
        removed = sum(1 for d in diff if d.startswith('-'))
        rows.append((name, f'+{added} / -{removed}', len(la)))
        # With two lines of context, e.g. the "name" of a JSON constant whose "value" changed.
        context = [d for d in difflib.unified_diff(la, lb, lineterm='', n=2) if not d.startswith(('---', '+++'))]
        shown = [d[:200] for d in context if not d.startswith('@@')][:SHOW_LINES * 2]
        details.append((name, shown, len(context)))

    if not rows:
        print('identical')
        return 0

    out = [f'# {args.title}', '',
           'Two dumps of the same Dota build differ in the sections below. The game did not change '
           'between them, so these lines are unreliable output of the dumper, not API changes.', '',
           '| section | difference | lines |', '|---|---|---|']
    out += [f'| `{n}` | {d} | {c} |' for n, d, c in rows]
    for name, shown, total in details:
        out += ['', f'## `{name}`', '', '```diff', *shown]
        if total > len(shown):
            out.append(f'… {total - len(shown)} more')
        out.append('```')
    report = '\n'.join(out) + '\n'
    if args.out:
        with open(args.out, 'w') as f:
            f.write(report)
    print('differ: ' + ', '.join(f'{n} ({d})' for n, d, _ in rows))
    return 1


if __name__ == '__main__':
    sys.exit(main())
