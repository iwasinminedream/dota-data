#!/usr/bin/env python3
"""
When did something change: searches every version's API changelog (files/changelogs/*.json), the
update reports (reports/*.md, *-functions.md) and, with --schema, the SchemaSystem of every
committed version (tracking/schema in git history) for a name.

    history.py NAME [--schema] [--exact]

NAME is a case-insensitive substring (--exact: the whole name). Prints one line per version and hit,
oldest first: `6969  API vscripts  ~ CDOTA_BaseNPC.GetHealth [...]`, `6975  report  …line…`,
`6970  schema libserver.so  CDOTA_BaseNPC.m_iHealth int32 @1212 -> @1220`.
"""
import argparse
import glob
import json
import os
import re
import subprocess
import sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def matcher(name, exact):
    if exact:
        rx = re.compile(rf'(?<![\w]){re.escape(name)}(?![\w])', re.I)
    else:
        rx = re.compile(re.escape(name), re.I)
    return rx.search


def changelog_hits(match):
    for path in sorted(glob.glob(os.path.join(REPO, 'files', 'changelogs', '*.json')),
                       key=lambda p: int(re.sub(r'\D', '', os.path.basename(p)) or 0)):
        version = os.path.basename(path)[:-5]
        try:
            log = json.load(open(path))
        except ValueError:
            continue
        for category, change in (log.get('changes') or {}).items():
            for kind, sign in (('added', '+'), ('removed', '-'), ('changed', '~')):
                for item in change.get(kind) or []:
                    text = json.dumps(item, ensure_ascii=False)
                    if match(text):
                        name = item.get('name', '?')
                        if item.get('class'):
                            name = f"{item['class']}.{name}"
                        detail = ''
                        if kind == 'changed':
                            detail = ' [' + '; '.join(
                                f"{k}: {str(v.get('old'))[:80]} -> {str(v.get('new'))[:80]}"
                                for k, v in (item.get('changes') or {}).items() if isinstance(v, dict)) + ']'
                        yield version, f'API {category}', f'{sign} {name}{detail}'


def report_hits(match):
    for path in sorted(glob.glob(os.path.join(REPO, 'reports', '*.md'))):
        base = os.path.basename(path)
        if base.endswith('.en.md'):
            continue
        version = base.split('.')[0].split('-functions')[0]
        kind = 'functions' if '-functions' in base else 'report'
        with open(path, encoding='utf-8', errors='replace') as f:
            for line in f:
                if match(line):
                    yield version, kind, line.strip()[:240]


def schema_hits(match):
    revs = subprocess.run(['git', '-C', REPO, 'log', '--reverse', '--format=%H', '--', 'tracking/schema'],
                          capture_output=True, text=True).stdout.split()
    last = {}
    for rev in revs:
        manifest = subprocess.run(['git', '-C', REPO, 'show', f'{rev}:tracking/manifest.json'],
                                  capture_output=True, text=True).stdout
        try:
            version = json.loads(manifest)['build']['ClientVersion']
        except (ValueError, KeyError, TypeError):
            version = rev[:7]
        files = subprocess.run(['git', '-C', REPO, 'ls-tree', '--name-only', rev, 'tracking/schema/'],
                               capture_output=True, text=True).stdout.split()
        for file in files:
            mod = os.path.basename(file)[:-5]
            try:
                data = json.loads(subprocess.run(['git', '-C', REPO, 'show', f'{rev}:{file}'],
                                                 capture_output=True, text=True).stdout)
            except ValueError:
                continue
            now = {}
            for c in data['classes']:
                if match(c['name']):
                    now[c['name']] = f"size {c['size']}"
                for f in c['fields']:
                    if match(f['name']) or match(c['name']):
                        now[f"{c['name']}.{f['name']}"] = f"{f['type']} @{f['offset']}"
            for e in data['enums']:
                for v in e['enumerators']:
                    if match(e['name']) or match(v['name']):
                        now[f"{e['name']}.{v['name']}"] = f"= {v['value']}"
            prev = last.get(mod, {})
            for key in sorted(set(now) | set(prev)):
                if prev.get(key) != now.get(key):
                    if key not in prev:
                        what = f'+ {now[key]}' if prev or mod in last else now[key]
                    elif key not in now:
                        what = '- (removed)'
                    else:
                        what = f'{prev[key]} -> {now[key]}'
                    yield version, f'schema {mod}', f'{key} {what}'
            last[mod] = now


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument('name')
    p.add_argument('--schema', action='store_true', help='also walk the SchemaSystem history (slower)')
    p.add_argument('--exact', action='store_true')
    args = p.parse_args()
    match = matcher(args.name, args.exact)
    hits = list(changelog_hits(match)) + list(report_hits(match))
    if args.schema:
        hits += list(schema_hits(match))
    key = lambda h: (int(re.sub(r'\D', '', h[0].split('-')[0]) or 0), h[1])
    for version, where, text in sorted(hits, key=key):
        print(f'{version:>6}  {where:<22}  {text}')
    if not hits:
        print(f'nothing found for {args.name!r}', file=sys.stderr)
        return 1
    return 0


if __name__ == '__main__':
    sys.exit(main())
