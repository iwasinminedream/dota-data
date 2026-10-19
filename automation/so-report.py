#!/usr/bin/env python3
"""
Snapshots the Linux .so files of the installed Dota 2 build and reports what changed between two
snapshots: per-library size / export / string differences, which strings the Metamod plugins rely
on disappeared, and a Russian summary written by Claude Haiku 4.5 (through the `claude` CLI, i.e.
the Claude Code login of this machine).

    so-report.py snapshot                 copy the installed build's .so files into the store
    so-report.py report OLD NEW [--out F] report between two stored snapshots (ids from `list`)
    so-report.py latest --out-dir DIR     report between the two newest snapshots into DIR/<new>.md
    so-report.py list

Snapshots live in $SO_STORE (default /var/lib/dota-data/so), one directory per build:
<ClientVersion>-<SourceRevision>/{bin,dota-bin}/*.so + steam.inf + SHA256SUMS. Only strings from
the read-only data sections are compared (NUL-terminated C strings), so code bytes never show up.
"""
import argparse
import datetime
import glob
import hashlib
import os
import re
import shutil
import struct
import subprocess
import sys

DOTA2_DIR = os.environ.get('DOTA2_DIR', '/home/steam/dota2')
STORE = os.environ.get('SO_STORE', '/var/lib/dota-data/so')
KEEP_SNAPSHOTS = int(os.environ.get('SO_KEEP', '3'))
# Metamod plugins installed for Dota (one dir per plugin in the staged addons tree); their sources
# are /opt/<name>/src.
PLUGIN_STAGE = os.environ.get('SO_PLUGIN_STAGE', '/root/dota-custom/metamod/addons')
PLUGIN_SOURCE = os.environ.get('SO_PLUGIN_SOURCE', '/opt/{}/src')
HAIKU_MODEL = os.environ.get('SO_MODEL', 'claude-haiku-4-5')
BIN_DIRS = {'bin': 'game/bin/linuxsteamrt64', 'dota-bin': 'game/dota/bin/linuxsteamrt64'}

# Third-party libraries: listed in the file table, never diffed string by string.
THIRD_PARTY = re.compile(r'^lib(av|sw|v8|SDL|vorbis|ogg|mpg123|vpx|cairo|pango|fontconfig|freetype|steam_api|steamaudio|phonon)')
PER_BUCKET_FOR_MODEL = 150
PER_BUCKET_IN_REPORT = 40


def steam_inf(path):
    info = {}
    with open(path, encoding='utf-8', errors='replace') as f:
        for line in f:
            if '=' in line:
                k, v = line.strip().split('=', 1)
                info[k] = v
    return info


def snapshot_id(info):
    return f"{info.get('ClientVersion', '0')}-{info.get('SourceRevision', '0')}"


def sha256(path):
    h = hashlib.sha256()
    with open(path, 'rb') as f:
        for chunk in iter(lambda: f.read(1 << 20), b''):
            h.update(chunk)
    return h.hexdigest()


def list_snapshots():
    snaps = []
    for d in glob.glob(os.path.join(STORE, '*')):
        inf = os.path.join(d, 'steam.inf')
        if os.path.isfile(os.path.join(d, 'SHA256SUMS')) and os.path.isfile(inf):
            info = steam_inf(inf)
            snaps.append((int(info.get('ClientVersion', 0)), int(info.get('SourceRevision', 0)), os.path.basename(d)))
    return [s[2] for s in sorted(snaps)]


def cmd_snapshot(_args):
    info = steam_inf(os.path.join(DOTA2_DIR, 'game/dota/steam.inf'))
    sid = snapshot_id(info)
    target = os.path.join(STORE, sid)
    if os.path.isfile(os.path.join(target, 'SHA256SUMS')):
        print(f'snapshot {sid} already exists')
        return
    tmp = target + '.partial'
    shutil.rmtree(tmp, ignore_errors=True)
    sums = []
    for key, rel in BIN_DIRS.items():
        os.makedirs(os.path.join(tmp, key))
        for so in sorted(glob.glob(os.path.join(DOTA2_DIR, rel, '*.so*'))):
            dst = os.path.join(tmp, key, os.path.basename(so))
            shutil.copy2(so, dst)
            sums.append(f'{sha256(dst)}  {key}/{os.path.basename(so)}')
    if not any(rel.endswith('libserver.so') for rel in sums):
        shutil.rmtree(tmp, ignore_errors=True)
        print(f'no libserver.so under {DOTA2_DIR}, not a Linux Dota install — no snapshot')
        return 1
    shutil.copy2(os.path.join(DOTA2_DIR, 'game/dota/steam.inf'), os.path.join(tmp, 'steam.inf'))
    with open(os.path.join(tmp, 'SHA256SUMS'), 'w') as f:
        f.write('\n'.join(sums) + '\n')
    os.rename(tmp, target)
    print(f'snapshot {sid}: {len(sums)} files')
    for old in list_snapshots()[:-KEEP_SNAPSHOTS]:
        shutil.rmtree(os.path.join(STORE, old), ignore_errors=True)
        print(f'removed old snapshot {old}')


# --- ELF -----------------------------------------------------------------------------------------

def elf_sections(data):
    if data[:4] != b'\x7fELF' or data[4] != 2:
        return {}
    shoff, = struct.unpack_from('<Q', data, 0x28)
    shentsize, shnum, shstrndx = struct.unpack_from('<HHH', data, 0x3a)
    headers = []
    for i in range(shnum):
        name, typ, _flags, _addr, off, size = struct.unpack_from('<IIQQQQ', data, shoff + i * shentsize)
        headers.append((name, typ, off, size))
    strtab = headers[shstrndx]
    names = data[strtab[2]:strtab[2] + strtab[3]]
    out = {}
    for name, typ, off, size in headers:
        end = names.index(b'\0', name)
        out[names[name:end].decode('latin1')] = (typ, off, size)
    return out


PRINTABLE = re.compile(rb'^[\x20-\x7e\t]{4,}$')


def rodata_strings(path):
    with open(path, 'rb') as f:
        data = f.read()
    found = set()
    for name, (typ, off, size) in elf_sections(data).items():
        if typ == 8:  # SHT_NOBITS
            continue
        if name.startswith('.rodata'):
            chunks = data[off:off + size].split(b'\0')
        elif name == 'protodesc_cold':
            # serialized protobuf descriptors: length-prefixed, so take printable runs
            chunks = re.findall(rb'[\x20-\x7e]{6,}', data[off:off + size])
        else:
            continue
        for chunk in chunks:
            chunk = chunk.strip(b'\n')
            if PRINTABLE.match(chunk) and len(re.findall(rb'[A-Za-z]', chunk)) >= 3:
                found.add(chunk.decode('ascii'))
    return found


def text_size(path):
    with open(path, 'rb') as f:
        data = f.read()
    return elf_sections(data).get('.text', (0, 0, 0))[2]


def exports(path):
    try:
        out = subprocess.run(['nm', '-D', '--defined-only', path], capture_output=True, text=True, check=True).stdout
    except (OSError, subprocess.CalledProcessError):
        return set()
    return {line.split()[-1] for line in out.splitlines() if line.strip()}


def demangle(names):
    if not names:
        return {}
    try:
        out = subprocess.run(['c++filt'], input='\n'.join(names), capture_output=True, text=True).stdout.splitlines()
        return dict(zip(names, out))
    except OSError:
        return {n: n for n in names}


# --- classification ------------------------------------------------------------------------------

BUCKETS = [
    ('game', 'Имена из игры (модификаторы, способности, предметы, юниты, события)',
     re.compile(r'^(modifier_|item_|npc_dota_|ability_|special_bonus_|dota_hero_|DOTA_[A-Z]|particles/|soundevents?/|[a-z]+_[a-z_]+_(hero|ability|item)\b)')),
    ('rtti', 'C++ классы (RTTI)', re.compile(r'^\d+[A-Z]\w*$|^N\d+')),
    ('convar', 'Консольные переменные и команды (похоже)', re.compile(r'^[+-]?(sv|cl|dota|r|mp|net|engine|snd|panorama|ui|host|tv|gc|vscript|script|fow|nav|phys|sc|mat|tools?|game|bot)_[a-z0-9_]+$')),
    ('ident', 'Прочие идентификаторы', re.compile(r'^[A-Za-z_][\w:.$<>~-]*$')),
    ('path', 'Пути и ресурсы', re.compile(r'[/\\]')),
    ('text', 'Сообщения и описания', re.compile(r' ')),
]


def classify(strings):
    buckets = {key: [] for key, _, _ in BUCKETS}
    buckets['other'] = []
    for s in sorted(strings):
        for key, _, rx in BUCKETS:
            if rx.search(s):
                buckets[key].append(s)
                break
        else:
            buckets['other'].append(s)
    return buckets


BUCKET_TITLES = {key: title for key, title, _ in BUCKETS} | {'other': 'Прочее'}


def plugin_anchor_strings():
    """String literals of the installed Dota plugins that look like something code is found by."""
    literal = re.compile(r'"((?:[^"\\\n]|\\.){6,200})"')
    specific = re.compile(r'[_:%./]|[a-z][A-Z]| ')
    anchors = {}
    plugins = [d for d in sorted(os.listdir(PLUGIN_STAGE)) if d != 'metamod'] if os.path.isdir(PLUGIN_STAGE) else []
    for plugin in plugins:
        src = PLUGIN_SOURCE.format(plugin)
        for path in glob.glob(os.path.join(src, '**', '*'), recursive=True):
            if not re.search(r'\.(c|cc|cpp|h|hpp|inc)$', path):
                continue
            try:
                text = open(path, encoding='utf-8', errors='replace').read()
            except OSError:
                continue
            for m in literal.finditer(text):
                if specific.search(m.group(1)):
                    anchors.setdefault(m.group(1), set()).add(plugin)
    return anchors


# --- report --------------------------------------------------------------------------------------

def read_sums(snapshot):
    sums = {}
    with open(os.path.join(STORE, snapshot, 'SHA256SUMS')) as f:
        for line in f:
            digest, rel = line.split()
            sums[rel] = digest
    return sums


def fmt_size(n):
    return f'{n / 1048576:.1f} МБ' if n >= 1048576 else f'{n / 1024:.0f} КБ'


def build_diff(old, new):
    old_sums, new_sums = read_sums(old), read_sums(new)
    files = []
    anchors = plugin_anchor_strings()
    anchor_hits = []
    for rel in sorted(set(old_sums) | set(new_sums)):
        o, n = os.path.join(STORE, old, rel), os.path.join(STORE, new, rel)
        entry = {'rel': rel, 'old_size': os.path.getsize(o) if rel in old_sums else None,
                 'new_size': os.path.getsize(n) if rel in new_sums else None}
        if rel not in old_sums or rel not in new_sums:
            entry['status'] = 'added' if rel not in old_sums else 'removed'
        elif old_sums[rel] == new_sums[rel]:
            entry['status'] = 'same'
        else:
            entry['status'] = 'changed'
            name = os.path.basename(rel)
            if not THIRD_PARTY.match(name):
                so, sn = rodata_strings(o), rodata_strings(n)
                eo, en = exports(o), exports(n)
                entry['strings_added'], entry['strings_removed'] = sn - so, so - sn
                entry['exports_added'], entry['exports_removed'] = en - eo, eo - en
                entry['text'] = (text_size(o), text_size(n))
                for s in entry['strings_removed']:
                    if s in anchors:
                        anchor_hits.append((s, sorted(anchors[s]), name))
        files.append(entry)
    return files, sorted(anchor_hits)


def model_input(old, new, files, anchor_hits):
    lines = [f'Сборка Dota 2 для Linux: {old} -> {new}.', '']
    for f in files:
        if f['status'] != 'changed' or 'strings_added' not in f:
            continue
        lines.append(f"### {f['rel']} ({fmt_size(f['old_size'])} -> {fmt_size(f['new_size'])}, "
                     f"код {f['text'][1] - f['text'][0]:+} байт)")
        dem = demangle(sorted(f['exports_added'] | f['exports_removed']))
        for label, items in (('экспорт добавлен', f['exports_added']), ('экспорт удалён', f['exports_removed'])):
            for e in sorted(items)[:60]:
                lines.append(f'{label}: {dem.get(e, e)}')
        for label, items in (('ДОБАВЛЕНО', f['strings_added']), ('УДАЛЕНО', f['strings_removed'])):
            for key, bucket in classify(items).items():
                if not bucket:
                    continue
                lines.append(f'{label} / {BUCKET_TITLES[key]} ({len(bucket)}):')
                lines.extend('  ' + s[:200] for s in bucket[:PER_BUCKET_FOR_MODEL])
                if len(bucket) > PER_BUCKET_FOR_MODEL:
                    lines.append(f'  ... ещё {len(bucket) - PER_BUCKET_FOR_MODEL}')
        lines.append('')
    if anchor_hits:
        lines.append('### Строки, по которым наши Metamod-плагины ищут код, и которых больше нет:')
        lines.extend(f'  "{s}" (плагины: {", ".join(p)}; было в {lib})' for s, p, lib in anchor_hits)
    return '\n'.join(lines)


def diff_blocks(old, new, files, anchor_hits):
    """The whole diff, uncapped, as (title, lines) blocks: per library a header with sizes and
    exports, then one block per direction and string group."""
    blocks = []
    for f in files:
        if f['status'] != 'changed' or 'strings_added' not in f:
            continue
        head = [f"{f['rel']}: {fmt_size(f['old_size'])} -> {fmt_size(f['new_size'])}, "
                f"код {f['text'][1] - f['text'][0]:+} байт, строки +{len(f['strings_added'])} "
                f"-{len(f['strings_removed'])}, экспорт +{len(f['exports_added'])} -{len(f['exports_removed'])}"]
        dem = demangle(sorted(f['exports_added'] | f['exports_removed']))
        for label, items in (('экспорт добавлен', f['exports_added']), ('экспорт удалён', f['exports_removed'])):
            head += [f'{label}: {dem.get(e, e)}' for e in sorted(items)]
        blocks.append((f"{f['rel']}: размеры и экспорт", head))
        for label, items in (('добавлено', f['strings_added']), ('удалено', f['strings_removed'])):
            for key, bucket in classify(items).items():
                if bucket:
                    blocks.append((f"{f['rel']}: {label} — {BUCKET_TITLES[key]} ({len(bucket)})", bucket))
    if anchor_hits:
        blocks.append(('Строки, по которым наши Metamod-плагины ищут код, и которых больше нет',
                       [f'"{s}" (плагины: {", ".join(p)}; было в {lib})' for s, p, lib in anchor_hits]))
    return blocks


SYSTEM_PROMPT = """Ты анализируешь обновление Dota 2 по диффу бинарников Linux (.so): какие строки из \
секций данных и какие экспортируемые символы появились или исчезли в каждой библиотеке. По строкам видно \
новые и удалённые консольные переменные, модификаторы, способности, предметы, сообщения, классы C++, \
пути к ресурсам. libserver.so — серверная логика игры, libclient.so — клиент и интерфейс, libengine2.so и \
libtier0.so — движок Source 2, libvscript.so — Lua VScript, libpanorama.so — UI Panorama.

Напиши по-русски короткий отчёт в Markdown для владельца сервера с кастомными играми и Metamod-плагинами:
1. «Главное» — 3–8 пунктов: что по сути поменялось в этом обновлении (новый контент, механики, системы).
2. «Для разработчиков кастомок» — изменения консольных переменных, Lua/Panorama API, событий, модификаторов.
3. «Риски для плагинов» — если в данных есть исчезнувшие строки-якоря плагинов, назови плагины и что \
проверить; иначе одной строкой, что якоря на месте.
Опирайся только на данные, не выдумывай; если смысл строки неясен, так и скажи. Заголовки разделов — \
третьего уровня (###). Без вступления и заключения."""


def ask_haiku(text):
    cmd = ['claude', '-p', '--model', HAIKU_MODEL, '--tools', '', '--system-prompt', SYSTEM_PROMPT,
           '--no-session-persistence', '--strict-mcp-config', '--output-format', 'text']
    env = {k: v for k, v in os.environ.items() if k not in ('CLAUDECODE', 'CLAUDE_CODE_ENTRYPOINT')}
    try:
        res = subprocess.run(cmd, input=text, capture_output=True, text=True, timeout=600, env=env)
    except (OSError, subprocess.TimeoutExpired) as e:
        return None, str(e)
    if res.returncode != 0 or not res.stdout.strip():
        return None, (res.stderr or res.stdout).strip()[:500]
    return res.stdout.strip(), None


def render_binaries(files, anchor_hits, h='##'):
    """The plugin anchor and file sections of a report (Markdown lines)."""
    out = []
    out.append(f'{h} Якоря Metamod-плагинов')
    out.append('')
    if anchor_hits:
        out.append('Исчезли строки, которые встречаются в исходниках плагинов (по ним ищется код):')
        out.append('')
        out.extend(f'- `{s}`: {", ".join(p)} (было в {lib})' for s, p, lib in anchor_hits)
    else:
        out.append('Все строки из исходников плагинов, которые были в старых библиотеках, на месте.')
    out.append('')
    changed = [f for f in files if f['status'] != 'same']
    out.append(f"{h} Файлы ({len(changed)} из {len(files)} изменились)")
    out.append('')
    out.append('| файл | размер | код (.text) | строки + / − | экспорт + / − |')
    out.append('|---|---|---|---|---|')
    for f in changed:
        size = (f"{fmt_size(f['old_size'])} → {fmt_size(f['new_size'])}" if f['status'] == 'changed'
                else f"{f['status']}")
        strs = f"{len(f['strings_added'])} / {len(f['strings_removed'])}" if 'strings_added' in f else '—'
        exps = f"{len(f['exports_added'])} / {len(f['exports_removed'])}" if 'exports_added' in f else '—'
        code = f"{f['text'][1] - f['text'][0]:+,} байт".replace(',', ' ') if 'text' in f else '—'
        out.append(f"| {f['rel']} | {size} | {code} | {strs} | {exps} |")
    out.append('')
    for f in changed:
        if 'strings_added' not in f or not (f['strings_added'] or f['strings_removed']):
            continue
        out.append(f"<details><summary>{f['rel']}: строки</summary>")
        out.append('')
        for label, items in (('Добавлено', f['strings_added']), ('Удалено', f['strings_removed'])):
            for key, bucket in classify(items).items():
                if not bucket:
                    continue
                out.append(f'**{label} — {BUCKET_TITLES[key]} ({len(bucket)})**')
                out.append('')
                out.append('```')
                out.extend(s[:160] for s in bucket[:PER_BUCKET_IN_REPORT])
                if len(bucket) > PER_BUCKET_IN_REPORT:
                    out.append(f'… ещё {len(bucket) - PER_BUCKET_IN_REPORT}')
                out.append('```')
                out.append('')
        out.append('</details>')
        out.append('')
    return out


def render(old, new, files, anchor_hits, summary, error):
    oi, ni = steam_inf(os.path.join(STORE, old, 'steam.inf')), steam_inf(os.path.join(STORE, new, 'steam.inf'))
    out = [f"# Dota 2 {oi.get('ClientVersion')} → {ni.get('ClientVersion')}: что изменилось в .so", '',
           f"Сборки `{old}` ({oi.get('VersionDate')}) → `{new}` ({ni.get('VersionDate')}). "
           f"Отчёт создан автоматически {datetime.date.today().isoformat()}; сводку написал Claude Haiku 4.5 "
           'по диффу строк и экспортов, таблицы ниже посчитаны без модели.', '']
    out.append('## Сводка')
    out.append('')
    out.append(summary if summary else f'_Сводку получить не удалось: {error}_')
    out.append('')
    out += render_binaries(files, anchor_hits)
    return '\n'.join(out).rstrip() + '\n'


def cmd_report(args):
    files, anchor_hits = build_diff(args.old, args.new)
    text = model_input(args.old, args.new, files, anchor_hits)
    if args.input_out:
        with open(args.input_out, 'w') as f:
            f.write(text)
    summary, error = (None, 'отключено (--no-ai)') if args.no_ai else ask_haiku(text)
    report = render(args.old, args.new, files, anchor_hits, summary, error)
    if args.out:
        os.makedirs(os.path.dirname(os.path.abspath(args.out)), exist_ok=True)
        with open(args.out, 'w') as f:
            f.write(report)
        print(f'report: {args.out}' + ('' if summary else f' (без сводки: {error})'))
    else:
        sys.stdout.write(report)
    return 0 if summary or args.no_ai else 2


def cmd_latest(args):
    snaps = list_snapshots()
    if len(snaps) < 2:
        print(f'need two snapshots in {STORE}, have {len(snaps)}')
        return 1
    args.old, args.new = snaps[-2], snaps[-1]
    version = steam_inf(os.path.join(STORE, args.new, 'steam.inf')).get('ClientVersion')
    args.out = os.path.join(args.out_dir, f'{version}.md')
    return cmd_report(args)


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest='cmd', required=True)
    sub.add_parser('snapshot')
    sub.add_parser('list')
    r = sub.add_parser('report')
    r.add_argument('old')
    r.add_argument('new')
    l = sub.add_parser('latest')
    l.add_argument('--out-dir', required=True)
    for sp in (r, l):
        if sp is r:
            sp.add_argument('--out')
        sp.add_argument('--no-ai', action='store_true')
        sp.add_argument('--input-out', help='also save the text sent to the model')
    args = p.parse_args()
    if args.cmd == 'snapshot':
        return cmd_snapshot(args)
    if args.cmd == 'list':
        print('\n'.join(list_snapshots()))
        return 0
    if args.cmd == 'report':
        return cmd_report(args)
    return cmd_latest(args)


if __name__ == '__main__':
    sys.exit(main() or 0)
