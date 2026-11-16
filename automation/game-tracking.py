#!/usr/bin/env python3
"""
Game-file tracking of the installed Dota 2 build, written to tracking/ (committed with the dump,
outside files/ so it is neither in the npm package nor a deploy trigger):

  tracking/schema/<module>.json    SchemaSystem of every module: classes (size, bases, fields with
                                   type and offset, metadata) and enums (schema-dump, built on demand)
  tracking/protobuf/*.proto        the .proto files compiled into the libraries (proto-dump.py)
  tracking/vpk/<pak>/<group>.txt   the VPK index: `path crc size` per file, sorted, split by folder
  tracking/vpk-files/<pak>/...     text files from the VPKs: scripts/** (txt, res, lst, eventdef, ...),
                                   items_game.txt split into its top-level sections (it is >50 MB)
  tracking/game/                   gameinfo.gi, gameinfo_branchspecific.gi, steam.inf
  tracking/manifest.json           counts, and which steps failed

    game-tracking.py [--repo DIR] [--game DIR] [--only schema,protobuf,vpk,files,game]

A step that fails keeps what is committed for it (restored from git by the caller) and is listed
in manifest.json "failed"; the exit code is 0 unless every step failed. Compiled resources (*_c:
soundevents, vdata) are only listed, not decompiled.
"""
import argparse
import collections
import glob
import json
import os
import re
import shutil
import subprocess
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
STATE = os.environ.get('DOTA_DATA_STATE', '/var/lib/dota-data')
THIRD_PARTY = re.compile(r'^lib(av|sw|v8|SDL|vorbis|ogg|mpg123|vpx|cairo|pango|fontconfig|freetype|steam_api|steamaudio|phonon)')
TEXT_EXT = {'txt', 'res', 'lst', 'eventdef', 'caverndef', 'eventactions', 'vdata', 'kv3', 'json', 'cfg', 'gi'}
PAKS = {'dota': 'dota/pak01_dir.vpk', 'core': 'core/pak01_dir.vpk'}
GROUP_LINES = 20000   # a VPK folder with more files is split by its subfolders
SECTION_BYTES = 4 << 20  # an items_game section bigger than this is split into parts


def log(msg):
    print(f'game-tracking: {msg}', file=sys.stderr, flush=True)


def fresh(path):
    shutil.rmtree(path, ignore_errors=True)
    os.makedirs(path)


def text(data):
    """Bytes of a game text file → LF-only UTF-8 (UTF-16 with BOM converted), None if binary."""
    if data.startswith((b'\xff\xfe', b'\xfe\xff')):
        try:
            data = data.decode('utf-16').encode('utf-8')
        except UnicodeDecodeError:
            return None
    if data.startswith(b'\xef\xbb\xbf'):
        data = data[3:]
    if b'\0' in data:
        return None
    return data.replace(b'\r\n', b'\n').replace(b'\r', b'\n')


# --- schema --------------------------------------------------------------------------------------
def schema_binary():
    src = os.path.join(HERE, 'schema-dump', 'schema-dump.cpp')
    out = os.path.join(STATE, 'bin', 'schema-dump')
    if not os.path.exists(out) or os.path.getmtime(out) < os.path.getmtime(src):
        os.makedirs(os.path.dirname(out), exist_ok=True)
        subprocess.run(['g++', '-O2', '-std=c++17', '-o', out + '.tmp', src, '-ldl'], check=True)
        os.replace(out + '.tmp', out)
    return out


def step_schema(game, out):
    dest = os.path.join(out, 'schema')
    tmp = dest + '.tmp'
    fresh(tmp)
    env = dict(os.environ, LD_LIBRARY_PATH=f'{game}/bin/linuxsteamrt64:{game}/dota/bin/linuxsteamrt64')
    res = subprocess.run([schema_binary(), game, tmp], env=env, capture_output=True, text=True, timeout=600)
    if res.returncode != 0 or not glob.glob(os.path.join(tmp, '*.json')):
        raise RuntimeError(f'schema-dump exit {res.returncode}: {res.stderr[-800:]}')
    classes = enums = 0
    for f in glob.glob(os.path.join(tmp, '*.json')):
        with open(f) as fh:
            d = json.load(fh)  # also checks that it is complete
        classes += len(d['classes'])
        enums += len(d['enums'])
    shutil.rmtree(dest, ignore_errors=True)
    os.rename(tmp, dest)
    return {'modules': len(os.listdir(dest)), 'classes': classes, 'enums': enums}


# --- protobuf ------------------------------------------------------------------------------------
def step_protobuf(game, out):
    libs = []
    for d in ('bin/linuxsteamrt64', 'dota/bin/linuxsteamrt64'):
        libs += [p for p in sorted(glob.glob(os.path.join(game, d, '*.so*')))
                 if not THIRD_PARTY.match(os.path.basename(p))]
    dest = os.path.join(out, 'protobuf')
    tmp = dest + '.tmp'
    shutil.rmtree(tmp, ignore_errors=True)
    res = subprocess.run([sys.executable, '-I', os.path.join(HERE, 'proto-dump.py'), tmp] + libs,
                         capture_output=True, text=True, timeout=1800)
    if res.returncode != 0 or not os.path.exists(os.path.join(tmp, 'index.json')):
        raise RuntimeError(f'proto-dump exit {res.returncode}: {res.stderr[-800:]}')
    shutil.rmtree(dest, ignore_errors=True)
    os.rename(tmp, dest)
    return {'protos': len(json.load(open(os.path.join(dest, 'index.json'))))}


# --- VPK -----------------------------------------------------------------------------------------
def vpk_open(path):
    import vpk  # pip package "vpk"
    return vpk.open(path)


def step_vpk(game, out):
    dest = os.path.join(out, 'vpk')
    tmp = dest + '.tmp'
    fresh(tmp)
    stats = {}
    for name, rel in PAKS.items():
        pak = vpk_open(os.path.join(game, rel))
        rows = []
        for path, meta in pak.read_index_iter():
            # meta: (preload, crc32, preload_length, archive_index, archive_offset, file_length);
            # archive index and offset change with every repack, so they are left out.
            rows.append((path, meta[1], meta[2] + meta[5]))
        rows.sort()
        groups = collections.defaultdict(list)
        for row in rows:
            parts = row[0].split('/')
            groups[parts[0] if len(parts) > 1 else '_root'].append(row)
        for top in list(groups):
            if len(groups[top]) > GROUP_LINES:
                for row in groups.pop(top):
                    parts = row[0].split('/')
                    groups[f'{top}/{parts[1]}' if len(parts) > 2 else f'{top}/_files'].append(row)
        for group, items in groups.items():
            file = os.path.join(tmp, name, group + '.txt')
            os.makedirs(os.path.dirname(file), exist_ok=True)
            with open(file, 'w') as f:
                f.writelines(f'{p} crc={c:08x} size={s}\n' for p, c, s in items)
        exts = collections.Counter(p.rsplit('.', 1)[-1] if '.' in p else '' for p, _c, _s in rows)
        with open(os.path.join(tmp, name, '_counts.txt'), 'w') as f:
            f.write(f'files {len(rows)}\n' + ''.join(f'{e or "(none)"} {n}\n' for e, n in sorted(exts.items())))
        stats[name] = len(rows)
    shutil.rmtree(dest, ignore_errors=True)
    os.rename(tmp, dest)
    return stats


def split_items_game(data):
    """items_game.txt → [(file name, bytes)]: one file per top-level section, a big section in parts
    of whole child blocks. Brace depth is counted outside quoted strings."""
    sections, depth, start, name, quote, i, last_key = [], 0, None, None, False, 0, None
    n = len(data)
    key_start = None
    while i < n:
        c = data[i]
        if quote:
            if c == 0x5c:  # backslash escape inside a string
                i += 2
                continue
            if c == 0x22:
                quote = False
                if key_start is not None:
                    last_key = data[key_start:i].decode('utf-8', 'replace')
                    key_start = None
        elif c == 0x22:
            quote = True
            key_start = i + 1
        elif c == 0x2f and data[i:i + 2] == b'//':
            j = data.find(b'\n', i)
            i = n if j < 0 else j
            continue
        elif c == 0x7b:
            depth += 1
            if depth == 2:
                name, start = last_key, data.rfind(b'\n', 0, i) + 1
                # back up to the line with the section's key
                k = data.rfind(b'"', 0, i)
                k = data.rfind(b'"', 0, k)
                start = data.rfind(b'\n', 0, k) + 1
        elif c == 0x7d:
            if depth == 2 and start is not None:
                end = data.find(b'\n', i)
                end = n if end < 0 else end + 1
                sections.append((name, data[start:end]))
                start = None
            depth -= 1
        i += 1
    files = []
    for idx, (sec, body) in enumerate(sections):
        safe = re.sub(r'[^A-Za-z0-9_.-]', '_', sec or f'section{idx}')
        if len(body) <= SECTION_BYTES:
            files.append((f'{idx:02}-{safe}.txt', body))
            continue
        # split at child blocks: lines that close a depth-3 block, found by scanning lines
        part, size, n_part, d = [], 0, 1, 0
        for line in body.splitlines(keepends=True):
            part.append(line)
            size += len(line)
            stripped = re.sub(rb'"(?:\\.|[^"\\])*"', b'', line.split(b'//')[0])
            d += stripped.count(b'{') - stripped.count(b'}')
            if d == 1 and stripped.strip() == b'}' and size > SECTION_BYTES:
                files.append((f'{idx:02}-{safe}-{n_part:02}.txt', b''.join(part)))
                part, size, n_part = [], 0, n_part + 1
        if part:
            files.append((f'{idx:02}-{safe}-{n_part:02}.txt', b''.join(part)))
    return files


def step_files(game, out):
    dest = os.path.join(out, 'vpk-files')
    tmp = dest + '.tmp'
    fresh(tmp)
    stats = {}
    for name, rel in PAKS.items():
        pak = vpk_open(os.path.join(game, rel))
        count = 0
        for path, _meta in pak.read_index_iter():
            ext = path.rsplit('.', 1)[-1].lower() if '.' in path else ''
            if not path.startswith('scripts/') or ext not in TEXT_EXT:
                continue
            data = text(pak.get_file(path).read())
            if data is None:
                continue
            if path == 'scripts/items/items_game.txt':
                parts = split_items_game(data)
                if sum(len(b) for _n, b in parts) < len(data) * 0.9:
                    raise RuntimeError('items_game.txt: the split lost data')
                for fname, body in parts:
                    file = os.path.join(tmp, name, 'scripts/items/items_game', fname)
                    os.makedirs(os.path.dirname(file), exist_ok=True)
                    with open(file, 'wb') as f:
                        f.write(body)
                count += 1
                continue
            file = os.path.join(tmp, name, path)
            os.makedirs(os.path.dirname(file), exist_ok=True)
            with open(file, 'wb') as f:
                f.write(data)
            count += 1
        stats[name] = count
    shutil.rmtree(dest, ignore_errors=True)
    os.rename(tmp, dest)
    return stats


def step_game(game, out):
    dest = os.path.join(out, 'game')
    fresh(dest)
    copied = 0
    for rel in ('dota/gameinfo.gi', 'dota/gameinfo_branchspecific.gi', 'dota/steam.inf', 'core/gameinfo.gi'):
        src = os.path.join(game, rel)
        if os.path.exists(src):
            with open(src, 'rb') as f:
                data = text(f.read())
            target = os.path.join(dest, rel.replace('/', '__'))
            with open(target, 'wb') as f:
                f.write(data or b'')
            copied += 1
    return {'files': copied}


STEPS = {'schema': step_schema, 'protobuf': step_protobuf, 'vpk': step_vpk, 'files': step_files, 'game': step_game}


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument('--repo', default=os.path.dirname(HERE))
    p.add_argument('--game', default=os.path.join(os.environ.get('DOTA2_DIR', '/home/steam/dota2'), 'game'))
    p.add_argument('--only', default=','.join(STEPS))
    args = p.parse_args()
    out = os.path.join(args.repo, 'tracking')
    os.makedirs(out, exist_ok=True)
    manifest_path = os.path.join(out, 'manifest.json')
    try:
        manifest = json.load(open(manifest_path))
    except (OSError, ValueError):
        manifest = {}
    manifest['failed'] = {}
    with open(os.path.join(args.game, 'dota/steam.inf')) as f:
        inf = dict(line.strip().split('=', 1) for line in f if '=' in line)
    manifest['build'] = {k: inf.get(k) for k in ('ClientVersion', 'SourceRevision', 'VersionDate')}
    ok = 0
    names = [s for s in args.only.split(',') if s]
    for name in names:
        t = time.time()
        try:
            manifest[name] = STEPS[name](args.game, out)
            ok += 1
            log(f'{name}: {manifest[name]} ({time.time() - t:.0f} s)')
        except Exception as e:  # keep going: each step is independent
            manifest['failed'][name] = str(e)[:1000]
            shutil.rmtree(os.path.join(out, name if name != 'files' else 'vpk-files') + '.tmp', ignore_errors=True)
            log(f'{name} FAILED: {e}')
    with open(manifest_path, 'w') as f:
        json.dump(manifest, f, indent=1, sort_keys=True)
        f.write('\n')
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
