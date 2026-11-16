#!/usr/bin/env python3
"""
What changed in tracking/ (game-tracking.py) between two builds, as text blocks for the update
report and its model: the SchemaSystem structurally (classes and enums added/removed, size and base
changes, fields added/removed/retyped, offset shifts summarised as runs: "fields from m_x on +8"),
the .proto files (unified diff), the VPK index (files added/removed/changed per folder) and the text
files from the VPKs and the game folder (unified diff).

    tracking-diff.py OLD_TRACKING_DIR NEW_TRACKING_DIR      prints the blocks
    (in update-report.py: blocks(old_dir, new_dir) -> [(title, lines)], table(...) -> counts)
"""
import collections
import difflib
import glob
import json
import os
import sys

MAX_DIFF_LINES = int(os.environ.get('TRACKING_MAX_DIFF_LINES', '600'))  # per file
MAX_LIST = int(os.environ.get('TRACKING_MAX_LIST', '400'))  # paths per folder and kind


def load_json(path):
    try:
        with open(path) as f:
            return json.load(f)
    except (OSError, ValueError):
        return None


def files_under(root):
    out = {}
    for path in glob.glob(os.path.join(root, '**', '*'), recursive=True):
        if os.path.isfile(path):
            out[os.path.relpath(path, root)] = path
    return out


def read_lines(path):
    with open(path, encoding='utf-8', errors='replace') as f:
        return f.read().splitlines()


def udiff(old, new, name):
    lines = list(difflib.unified_diff(read_lines(old), read_lines(new), f'old/{name}', f'new/{name}', n=2, lineterm=''))
    if len(lines) > MAX_DIFF_LINES:
        extra = len(lines) - MAX_DIFF_LINES
        lines = lines[:MAX_DIFF_LINES] + [f'... ещё {extra} строк диффа']
    return lines


# --- schema --------------------------------------------------------------------------------------
def shift_runs(old_fields, new_fields):
    """Offset changes of the fields present in both, as runs of equal shift in field order."""
    old = {f['name']: f for f in old_fields}
    runs, cur = [], None
    for f in new_fields:
        o = old.get(f['name'])
        if not o:
            continue
        delta = f['offset'] - o['offset']
        if cur and cur[0] == delta:
            cur[2] = f['name']
            cur[3] += 1
        else:
            if cur:
                runs.append(cur)
            cur = [delta, f['name'], f['name'], 1]
    if cur:
        runs.append(cur)
    return [r for r in runs if r[0] != 0]


def schema_lines(old_dir, new_dir):
    lines, counts = [], collections.Counter()
    old_mods = {os.path.basename(p)[:-5]: p for p in glob.glob(os.path.join(old_dir, '*.json'))}
    new_mods = {os.path.basename(p)[:-5]: p for p in glob.glob(os.path.join(new_dir, '*.json'))}
    for mod in sorted(set(old_mods) | set(new_mods)):
        if mod not in old_mods or mod not in new_mods:
            lines.append(f"{'+' if mod in new_mods else '-'} модуль {mod}")
            continue
        o, n = load_json(old_mods[mod]), load_json(new_mods[mod])
        if not o or not n:
            continue
        oc, nc = {c['name']: c for c in o['classes']}, {c['name']: c for c in n['classes']}
        oe, ne = {e['name']: e for e in o['enums']}, {e['name']: e for e in n['enums']}
        mod_lines = []
        for name in sorted(set(nc) - set(oc)):
            c = nc[name]
            bases = ', '.join(b['name'] for b in c['bases'])
            mod_lines.append(f"+ класс {name} (размер {c['size']}{', база ' + bases if bases else ''}, полей {len(c['fields'])}): "
                             + ', '.join(f"{f['type']} {f['name']}@{f['offset']}" for f in c['fields'][:40])
                             + (' …' if len(c['fields']) > 40 else ''))
            counts['classes_added'] += 1
        for name in sorted(set(oc) - set(nc)):
            mod_lines.append(f'- класс {name}')
            counts['classes_removed'] += 1
        for name in sorted(set(oc) & set(nc)):
            a, b = oc[name], nc[name]
            parts = []
            if a['size'] != b['size']:
                parts.append(f"размер {a['size']} -> {b['size']} ({b['size'] - a['size']:+d})")
            ab, bb = [x['name'] for x in a['bases']], [x['name'] for x in b['bases']]
            if ab != bb:
                parts.append(f"базы {ab} -> {bb}")
            af, bf = {f['name']: f for f in a['fields']}, {f['name']: f for f in b['fields']}
            added = [f"{bf[k]['type']} {k}@{bf[k]['offset']}" for k in bf if k not in af]
            removed = [f"{af[k]['type']} {k}" for k in af if k not in bf]
            retyped = [f"{k}: {af[k]['type']} -> {bf[k]['type']}" for k in bf if k in af and af[k]['type'] != bf[k]['type']]
            if added:
                parts.append('поля + ' + ', '.join(added))
            if removed:
                parts.append('поля − ' + ', '.join(removed))
            if retyped:
                parts.append('тип ' + '; '.join(retyped))
            runs = shift_runs(a['fields'], b['fields'])
            if runs:
                parts.append('смещения ' + '; '.join(
                    f"{r[1]}{'…' + r[2] if r[3] > 1 else ''} ({r[3]} пол.) {r[0]:+d}" for r in runs))
            am = [m['name'] + ('=' + m['value'] if m.get('value') else '') for m in a['metadata']]
            bm = [m['name'] + ('=' + m['value'] if m.get('value') else '') for m in b['metadata']]
            if am != bm:
                parts.append(f"метаданные + {sorted(set(bm) - set(am))} − {sorted(set(am) - set(bm))}")
            if parts:
                mod_lines.append(f"~ класс {name}: " + ' | '.join(parts))
                counts['classes_changed'] += 1
                counts['fields_added'] += len(added)
                counts['fields_removed'] += len(removed)
                if runs:
                    counts['classes_shifted'] += 1
        for name in sorted(set(ne) - set(oe)):
            mod_lines.append(f"+ enum {name}: " + ', '.join(f"{v['name']}={v['value']}" for v in ne[name]['enumerators'][:60]))
            counts['enums_added'] += 1
        for name in sorted(set(oe) - set(ne)):
            mod_lines.append(f'- enum {name}')
            counts['enums_removed'] += 1
        for name in sorted(set(oe) & set(ne)):
            a = {v['name']: v['value'] for v in oe[name]['enumerators']}
            b = {v['name']: v['value'] for v in ne[name]['enumerators']}
            if a != b:
                ch = [f'+{k}={b[k]}' for k in b if k not in a] + [f'-{k}' for k in a if k not in b] + \
                     [f'{k}: {a[k]} -> {b[k]}' for k in b if k in a and a[k] != b[k]]
                mod_lines.append(f"~ enum {name}: " + ', '.join(ch))
                counts['enums_changed'] += 1
        if mod_lines:
            lines.append(f'## {mod}')
            lines += mod_lines
    return lines, counts


# --- protobuf, files -----------------------------------------------------------------------------
def tree_diff(old_dir, new_dir, label):
    """Added / removed / changed files under the two roots, with unified diffs of the changed ones."""
    old, new = files_under(old_dir), files_under(new_dir)
    lines, counts = [], collections.Counter()
    for rel in sorted(set(new) - set(old)):
        n = read_lines(new[rel])
        lines.append(f'+ {label} {rel} ({len(n)} строк)')
        lines += [f'  {line}' for line in n[:80]] + (['  …'] if len(n) > 80 else [])
        counts['added'] += 1
    for rel in sorted(set(old) - set(new)):
        lines.append(f'- {label} {rel}')
        counts['removed'] += 1
    for rel in sorted(set(old) & set(new)):
        with open(old[rel], 'rb') as a, open(new[rel], 'rb') as b:
            if a.read() == b.read():
                continue
        lines.append(f'~ {label} {rel}')
        lines += udiff(old[rel], new[rel], rel)
        counts['changed'] += 1
    return lines, counts


def vpk_index(path):
    out = {}
    with open(path, encoding='utf-8', errors='replace') as f:
        for line in f:
            parts = line.rstrip('\n').rsplit(' ', 2)
            if len(parts) == 3:
                out[parts[0]] = (parts[1], parts[2])
    return out


def vpk_lines(old_dir, new_dir):
    lines, counts = [], collections.Counter()
    for pak in sorted(set(os.listdir(new_dir)) if os.path.isdir(new_dir) else []):
        old_idx, new_idx = {}, {}
        for p in glob.glob(os.path.join(old_dir, pak, '**', '*.txt'), recursive=True):
            if not p.endswith('_counts.txt'):
                old_idx.update(vpk_index(p))
        for p in glob.glob(os.path.join(new_dir, pak, '**', '*.txt'), recursive=True):
            if not p.endswith('_counts.txt'):
                new_idx.update(vpk_index(p))
        if not old_idx:
            continue
        kinds = {'добавлены': sorted(set(new_idx) - set(old_idx)), 'удалены': sorted(set(old_idx) - set(new_idx)),
                 'изменены': sorted(k for k in set(old_idx) & set(new_idx) if old_idx[k][0] != new_idx[k][0])}
        for kind, paths in kinds.items():
            counts[f'{pak}_{kind}'] = len(paths)
            by_folder = collections.defaultdict(list)
            for p in paths:
                by_folder['/'.join(p.split('/')[:2]) if '/' in p else '.'].append(p)
            for folder in sorted(by_folder, key=lambda f: -len(by_folder[f])):
                items = by_folder[folder]
                lines.append(f'VPK {pak}: {kind} в {folder}/: {len(items)}')
                shown = items[:MAX_LIST]
                lines += [f'  {p} ({new_idx.get(p, old_idx.get(p))[1]})' for p in shown]
                if len(items) > len(shown):
                    lines.append(f'  … ещё {len(items) - len(shown)}')
    return lines, counts


def blocks(old, new):
    """[(title, lines)] for the report and a {area: Counter} table; old/new are tracking/ dirs."""
    out, table = [], {}
    sl, sc = schema_lines(os.path.join(old, 'schema'), os.path.join(new, 'schema'))
    if sl:
        out.append((f'SchemaSystem: классов +{sc["classes_added"]} −{sc["classes_removed"]} ~{sc["classes_changed"]}, '
                    f'enum +{sc["enums_added"]} −{sc["enums_removed"]} ~{sc["enums_changed"]}', sl))
    table['schema'] = sc
    for area, label, title in (('protobuf', 'proto', 'Protobuf (.proto из библиотек)'),
                               ('vpk-files', 'файл', 'Текстовые файлы из VPK (scripts/, items_game)'),
                               ('game', 'файл', 'Файлы игры (gameinfo.gi, steam.inf)')):
        if not os.path.isdir(os.path.join(old, area)):
            continue
        lines, counts = tree_diff(os.path.join(old, area), os.path.join(new, area), label)
        if area == 'game':  # steam.inf changes every build
            keep = [i for i, line in enumerate(lines) if line.startswith(('+', '-', '~')) and 'steam.inf' not in line]
            if not keep:
                lines = []
        if lines:
            out.append((f"{title}: +{counts['added']} −{counts['removed']} ~{counts['changed']}", lines))
        table[area] = counts
    vl, vc = vpk_lines(os.path.join(old, 'vpk'), os.path.join(new, 'vpk'))
    if vl:
        out.append(('Индекс VPK: ' + ', '.join(f'{k} {v}' for k, v in vc.items() if v), vl))
    table['vpk'] = vc
    return out, table


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print(__doc__)
        sys.exit(2)
    result, counts = blocks(sys.argv[1], sys.argv[2])
    for title, lines in result:
        print(f'### {title}')
        print('\n'.join(lines))
        print()
    print(json.dumps(counts, ensure_ascii=False, default=dict), file=sys.stderr)
