#!/usr/bin/env python3
"""
The report of a Dota update, reports/<version>.md: what changed in the API (the dump's changelog,
files/changelogs/<version>.json) and in the Linux .so files (two snapshots of so-report.py): strings
and exports, and function by function (funcdiff.py: every changed, added and removed function of
the game's libraries with its class/callback name, strings, changed constants and code diff;
written in full to reports/<version>-functions.md).

The report is technical, for developers of custom games and server plugins: APIs, engine, client
and server as a platform, protocols and schema, and first of all whatever limits or changes what a
custom game, a client or a server may do (game-mode checks, the browser and URLs, allow/deny lists of
commands, convars and addresses, command flags such as clientcmd_can_execute, new refusals and
limits), put first in «Главное» and in «⚠ Ограничения и странное». Left out of the model's input and
of the report: game content and balance (Abilities, Units, Localization, Modifiers and their native
formulas; functions of single heroes, abilities, items and modifiers, and helpers only they call;
assets and the game's KV files) and what a recompilation alone explains (field offsets and vtable
slots that move across the library, register and inlining changes, address bytes funcdiff reads as
strings). funcdiff's call targets (which functions a changed function now calls and no longer
calls) keep a new call plus a branch from being taken for a recompilation; a function with signs of
a restriction is never left out. The workspace keeps the full inputs (*-all.txt) and the list of
what was left out and why (func-dropped.txt); reports/<version>-functions.md has every function and
every string of the libraries.

Two passes, both by Claude Sonnet 5.5 by default (REPORT_DRAFT_MODEL / REPORT_FINAL_MODEL), through
the `claude` CLI (the server's Claude Code subscription login, or ANTHROPIC_API_KEY when set), no
spending cap:

1. The draft pass goes through everything, uncapped: the changelog, the .so diff and the changed
   functions are cut into chunks (by category / library and string group / function) and each chunk
   gets a detailed digest with the exact names (a few chunks in parallel, no tools: the chunk is the
   whole input).
2. The final pass reads the digests, checks every claim that goes into the report against the raw
   data, fixes and completes them, and writes the report, listing what it corrected. It works as a
   read-only agent: Read/Grep/Glob inside the analysis workspace, this repo and the two snapshots
   (the server's Metamod plugins are not part of this public report), and one shell command,
   automation/so-query.py (strings, symbols, string references, disassembly, functions: changed
   list, whole diffs, callers, vtables); `--permission-mode dontAsk` refuses everything else,
   nothing can be written.

    update-report.py VERSION --out reports/VERSION.md [--no-ai] [--data-rev REV]

--data-rev: the dump data (files/, dumper/dump, dump-checks/) is taken from commit REV instead of
the worktree — a report written later for a version that is no longer the newest one.

Exit code 0: written (or --no-ai); 2: a model failed, nothing written (the sync retries later).
"""
import argparse
import collections
import concurrent.futures
import datetime
import glob
import importlib.util
import json
import os
import re
import shutil
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
spec = importlib.util.spec_from_file_location('so_report', os.path.join(HERE, 'so-report.py'))
so_report = importlib.util.module_from_spec(spec)
spec.loader.exec_module(so_report)
spec = importlib.util.spec_from_file_location('funcdiff', os.path.join(HERE, 'funcdiff.py'))
funcdiff = importlib.util.module_from_spec(spec)
spec.loader.exec_module(funcdiff)
spec = importlib.util.spec_from_file_location('tracking_diff', os.path.join(HERE, 'tracking-diff.py'))
tracking_diff = importlib.util.module_from_spec(spec)
spec.loader.exec_module(tracking_diff)

STATE = os.environ.get('DOTA_DATA_STATE', '/var/lib/dota-data')
DRAFT_MODEL = os.environ.get('REPORT_DRAFT_MODEL', 'claude-sonnet-5-5')
FINAL_MODEL = os.environ.get('REPORT_FINAL_MODEL', 'claude-sonnet-5-5')
FINAL_EFFORT = os.environ.get('REPORT_FINAL_EFFORT', 'high')
CHUNK_CHARS = int(os.environ.get('REPORT_CHUNK_CHARS', '60000'))
DRAFT_WORKERS = int(os.environ.get('REPORT_DRAFT_WORKERS', '3'))
DATA = REPO  # where files/, dumper/dump and dump-checks/ are read from (--data-rev: an extracted commit)
DATA_REV = 'HEAD'
KEEP_ANALYSIS = 10  # versions whose analysis workspace is kept


def model_name(model):
    m = re.match(r'claude-([a-z]+)-(\d+)-(\d+)', model)
    return f'Claude {m.group(1).capitalize()} {m.group(2)}.{m.group(3)}' if m else model


def item_text(item):
    name = item.get('name', '?')
    if item.get('class'):
        name = f"{item['class']}.{name}"
    extra = item.get('signature') or item.get('value') or item.get('description') or ''
    if isinstance(extra, (dict, list)):
        extra = json.dumps(extra, ensure_ascii=False)
    kind = item.get('type', '')
    return f"{kind} {name}{' — ' + str(extra)[:300] if extra and extra != name else ''}".strip()


def changed_text(item):
    parts = []
    for field, change in (item.get('changes') or {}).items():
        if isinstance(change, dict) and 'old' in change:
            parts.append(f"{field}: {str(change['old'])[:300]} -> {str(change['new'])[:300]}")
    return f"{item_text(item)} [{'; '.join(parts)}]"


def activity_noise(category, item):
    return category in ('Lua Enums', 'Panorama Enums') and isinstance(item, dict) and item.get('enum') == 'GameActivity_t'


def api_blocks(version):
    """The changelog as (title, lines) blocks, one per category (game content and balance left out,
    see GAMEPLAY_CATEGORIES), and the count table of all categories."""
    with open(os.path.join(DATA, 'files', 'changelogs', f'{version}.json')) as f:
        log = json.load(f)
    blocks, table = [], []
    for category, change in log['changes'].items():
        # GameActivity_t members (ACT_*) are registered at run time: they come and go between dumps
        added, removed, changed = ([i for i in change.get(k) or [] if not activity_noise(category, i)]
                                   for k in ('added', 'removed', 'changed'))
        table.append((category, len(added), len(removed), len(changed)))
        lines = [f'+ {item_text(i)}' for i in added] + [f'- {item_text(i)}' for i in removed] + \
            [f'~ {changed_text(i)}' for i in changed]
        if lines and category not in GAMEPLAY_CATEGORIES:
            blocks.append((f'API {category}: +{len(added)} -{len(removed)} ~{len(changed)}', lines))
    return blocks, table


def chunk(blocks):
    """Packs blocks into chunks of at most CHUNK_CHARS; a bigger block is split into parts."""
    pieces = []
    for title, lines in blocks:
        part, size, n = [], 0, 1
        for line in lines:
            if part and size + len(line) > CHUNK_CHARS:
                pieces.append((f'{title} (часть {n})', part))
                part, size, n = [], 0, n + 1
            part.append(line)
            size += len(line) + 1
        pieces.append((f'{title} (часть {n})' if n > 1 else title, part))
    chunks, current, size = [], [], 0
    for title, lines in pieces:
        text = f'### {title}\n' + '\n'.join(lines) + '\n'
        if current and size + len(text) > CHUNK_CHARS:
            chunks.append(current)
            current, size = [], 0
        current.append((title, text))
        size += len(text)
    if current:
        chunks.append(current)
    return chunks


def current_snapshot(version):
    snaps = [s for s in so_report.list_snapshots() if s.split('-')[0] == str(version)]
    return snaps[-1] if snaps else None


def snapshot_pair(version):
    snaps = so_report.list_snapshots()
    new = [s for s in snaps if s.split('-')[0] == str(version)]
    if not new:
        return None
    newest = new[-1]
    older = snaps[:snaps.index(newest)]
    return (older[-1], newest) if older else None


def function_diffs(old, new, files, workspace):
    """Function-level comparison of every changed game library (not the third-party ones):
    func-diff/<lib>.json in the workspace (for so-query) and the results."""
    results = []
    os.makedirs(os.path.join(workspace, 'func-diff'), exist_ok=True)
    for f in files:
        if f['status'] != 'changed' or 'text' not in f:
            continue
        try:
            result = funcdiff.compare(os.path.join(so_report.STORE, old, f['rel']),
                                      os.path.join(so_report.STORE, new, f['rel']))
        except Exception as e:  # a library the sweep cannot read: the string diff still covers it
            print(f"funcdiff {f['rel']}: {e!r}", file=sys.stderr)
            continue
        result['rel'] = f['rel']
        with open(os.path.join(workspace, 'func-diff', f"{result['lib']}.json"), 'w') as out:
            json.dump(result, out, ensure_ascii=False)
        results.append(result)
    return results


MANY_FUNCTIONS = int(os.environ.get('REPORT_MANY_FUNCTIONS', '1500'))


# ---------- what the report is about ----------
# The report is for developers of custom games and of server plugins: the technical side of an
# update (APIs, engine, client and server framework, protocols, and above all anything that limits
# what a custom game, a client or a server may do), not the patch itself. Game content and balance
# (abilities, items, units, their values and texts, the code of single heroes, items and
# modifiers) and what a recompilation alone changes (registers, field offsets, vtable slots,
# inlining) are left out of the model's input and of the report; the complete lists stay in
# reports/<version>-functions.md and in the changelog.
GAMEPLAY_CATEGORIES = {'Abilities', 'Units', 'Localization', 'Modifiers', 'Native Modifier Functions'}
# Signs of a restriction or of something unusual in a function's strings or names (never filtered out,
# put first): the browser and web requests, allow/deny lists, custom-game and game-mode checks,
# console and client commands, cheat and trust checks.
_W = r'(?<![A-Za-z0-9_])(?:{})(?![A-Za-z0-9_])'
RESTRICTION = re.compile(
    r'(?i)browser|html|https?://|steam://|openurl|weburl|webpage|web ?request|sv_cheats|clientcmd|can_execute|'
    r'sendtoconsole|sendtoserverconsole|executeclientcmd|clientcommand|servercommand|' + _W.format(
        r'custom ?games?|customgames?|game ?mode|game_mode|gamemode|urls?|white.?list\w*|black.?list\w*|'
        r'allow.?list\w*|deny.?list\w*|block.?list\w*|not allowed|disallow\w*|denied|forbid\w*|restrict\w*|'
        r'permissions?|insecure|untrusted|tamper\w*|vac|exec'))
MANGLED = re.compile(r'^\*?(_Z|St\d|N\d|\d+[A-Za-z_])')   # C++ type names from RTTI, not messages
# a class name is a sign only when it is about the browser or web content
RESTRICTION_CLASS = re.compile(r'(?i)html|browser|webpage|\burl')
# A class of one hero, ability, item or modifier (the framework classes stay: *_Lua, DataDriven, ...).
GAMEPLAY_CLASS = re.compile(r'^C_?DOTA_(Ability|Item|Modifi?er)_(?!Lua$|DataDriven$|Base$)\w+$|^C_?DOTA_Unit_Hero_\w+$|'
                            r'^C_?DOTA_(Neutral\w*|BaseNPC_Creep_Neutral|Roshan\w*|Unit_Roshan\w*)$|'
                            r'^C_?DOTA_\w+_Modifi?er_\w+$|^EventGrant\w*$|'
                            # seasonal events and their game modes, the battle pass and other store content
                            r'^C_?DOTA\w*(Seasonal|Aghs[Ff]ort|DarkCarnival|Overworld|Labyrinth|CandyShop|Trophy|RoadToTI|'
                            r'Frostivus|Crownfall|Bingo|BattlePass|Fantasy|Craftworks|Diretide|Banner|Tarot|FortuneTeller|'
                            r'ArenaOfBlood|Prediction|Match3|Minesweeper|Lockpicking|FightingGame|Survivors|WhackAMole)\w*$')
# Strings that only the code of one hero/ability/item uses.
GAMEPLAY_STRONG = re.compile(r'^(particles|models|sounds|soundevents|materials)/|\.(vpcf|vmdl|vsndevts)$|'
                             r'^(modifier|item|ability|special_bonus|npc_dota_hero)_|^(Hero|Item|Ability)_?[A-Z]\w*\.')
GAMEPLAY_SPECIAL = re.compile(r'^[a-z][a-z0-9_]*$')   # ability special value names: duration, radius, ...
LAYOUT_REPEAT = int(os.environ.get('REPORT_LAYOUT_REPEAT', '5'))
REBUILD_PARTS = ('поля объектов', 'инструкций', 'прямых вызовов')
SUMMARY_STRING = re.compile(r'[+−]("(?:[^"\\]|\\.)*")')


def junk_string(text):
    """Three bytes of an address that funcdiff read as a string ("0nj", "D1m", "{Yu"): they move by
    one with every build. Real three-letter strings (nil, int, off, 100, %d) are not junk."""
    return len(text) == 3 and not re.fullmatch(r'[a-z]+|[A-Z]+|\d+|%.+|\s%\w', text)


def summary_strings(line, signed=False):
    out = []
    for m in SUMMARY_STRING.finditer(line):
        try:
            text = json.loads(m.group(1))
        except ValueError:
            text = m.group(1)
        out.append((line[m.start()], text) if signed else text)
    return out


def junk_strings_line(line):
    """A 'строки: …' summary line that only shows address bytes: junk strings, or three-character
    strings whose old and new form differ in one character (the address moved: "3dj" -> "sdj")."""
    items = summary_strings(line, signed=True)
    if not items:
        return False
    plus = [t for sign, t in items if sign == '+']
    minus = [t for sign, t in items if sign == '−']
    def moved(t, others):
        return len(t) == 3 and any(len(o) == 3 and sum(a != b for a, b in zip(t, o)) == 1 for o in others)
    return all(junk_string(t) or moved(t, minus if sign == '+' else plus) for sign, t in items)


def class_names(entry):
    return [n.split('::')[0] for n in entry.get('names') or []]


def entry_strings(entry):
    strings = entry.get('strings') or re.findall(r'"([^"]*)"', entry.get('title', '').partition('строки:')[2])
    return [x for x in strings if not junk_string(x)]


def _signs(strings):
    return [x for x in strings if not junk_string(x) and not MANGLED.match(x) and RESTRICTION.search(x)]


def restriction_signs(entry, changed_only=False):
    """Strings / names of the function that look like a restriction. changed_only: only those among
    the strings the change added or removed (the strong sign: new or dropped messages, URLs, names)."""
    found = [x for s in entry.get('summary', []) if s.startswith('строки') for x in _signs(summary_strings(s))]
    if entry['kind'] in ('added', 'removed'):
        found += _signs(entry_strings(entry))   # a whole new / dropped function: all its strings are changed
    if not changed_only:
        found += _signs(entry_strings(entry))
        found += [n for n in entry.get('names') or [] if RESTRICTION_CLASS.search(n.split('::')[0])]
    return list(dict.fromkeys(found))[:6]


def callers(entry):
    m = re.search(r'вызывается из: ([^|]+)', entry.get('title', ''))
    return [c.strip().split('::')[0] for c in m.group(1).split(',') if c.strip() and 'ещё' not in c] if m else []


def is_gameplay(entry):
    names = class_names(entry)
    if names:
        return all(GAMEPLAY_CLASS.match(n) for n in names)
    if callers(entry) and all(GAMEPLAY_CLASS.match(c) for c in callers(entry)):
        return True   # a helper only heroes / abilities / items call
    strings = entry_strings(entry)
    return bool(strings) and any(GAMEPLAY_STRONG.search(s) for s in strings) and \
        all(GAMEPLAY_STRONG.search(s) or GAMEPLAY_SPECIAL.match(s) for s in strings)


def layout_signatures(result):
    """Summary lines ('числа в инструкциях: …', 'виртуальные вызовы: …') that repeat across many
    functions of a library: the same change everywhere is a moved field or slot, not logic."""
    seen = {}
    for e in result['entries']:
        for s in e.get('summary', []):
            if s.startswith(('числа в инструкциях', 'виртуальные вызовы')):
                seen[s] = seen.get(s, 0) + 1
    return {s for s, n in seen.items() if n >= LAYOUT_REPEAT}


# Calls a recompilation adds or removes on its own: allocation helpers, static-init guards, memory and
# string primitives (inlined in one build, called in the next).
BORING_CALL = re.compile(r'^(UtlVectorMemory_\w+|MemAlloc_\w+|__cxa_\w+|__stack_chk_fail|_Unwind_\w+|'
                         r'mem(cpy|move|set|cmp)|str(len|cmp|ncmp|cpy|ncpy)|V_\w+|free|malloc|realloc|calloc|'
                         r'_Zn[wa]m|_Zd[la]Pv\w*|operator (new|delete)\w*|std::\w.*)\(\)$')


def rebuild_only(entry, layout):
    """A changed function whose diff is what a recompilation or a moved field/slot gives: no new or
    removed string, data constant or call target, numbers and virtual calls only as part of a
    library-wide shift."""
    if entry['kind'] == 'callee':
        return True   # the same code calling another address: a relink, an identical-code fold
    if entry['kind'] != 'changed':
        return False
    calls = (entry.get('calls_added') or []) + (entry.get('calls_removed') or [])
    if any(not BORING_CALL.match(c) for c in calls):
        return False
    for s in entry.get('summary', []):
        if '(и ещё' in s:
            return False   # cut summary: cannot be shown to be only a shift
        head = s.split(':', 1)[0]
        if head == 'прямых вызовов' and 'calls_added' not in entry:
            return False   # an older func-diff without call targets: a changed call count may be logic
        if head in REBUILD_PARTS or (head in ('числа в инструкциях', 'виртуальные вызовы') and s in layout):
            continue
        if head == 'строки' and junk_strings_line(s):
            continue   # only address bytes read as strings
        return False
    return True


def classify(result):
    """{id(entry): 'restriction' | 'gameplay' | 'rebuild' | 'copy' | 'technical'} for one library."""
    layout = layout_signatures(result)
    out = {}
    for e in result['entries']:
        if e['kind'].startswith('copy_'):
            out[id(e)] = 'copy'
        elif restriction_signs(e, changed_only=True):
            out[id(e)] = 'restriction'   # added or removed strings that look like a restriction: always kept
        elif is_gameplay(e):
            out[id(e)] = 'gameplay'
        elif rebuild_only(e, layout):
            out[id(e)] = 'rebuild'
        elif restriction_signs(e):
            out[id(e)] = 'restriction'   # a real change in a function whose strings look like a restriction
        else:
            out[id(e)] = 'technical'
    return out


def filter_lines(lines, keep):
    """Lines of a block where a '+/-/~ …' item line and its indented detail lines go together."""
    out, take = [], True
    for line in lines:
        if not line.startswith(' '):
            take = keep(line)
        if take:
            out.append(line)
    return out


def technical_so_blocks(blocks):
    """so-report blocks without the strings only game content uses (particle and model paths,
    modifier/ability/item names) in libserver/libclient."""
    out = []
    for title, lines in blocks:
        if ('libserver' in title or 'libclient' in title) and 'размеры и экспорт' not in title:
            lines = [s for s in lines if RESTRICTION.search(s) or not GAMEPLAY_STRONG.search(s)]
        if lines:
            out.append((title, lines))
    return out


GAMEPLAY_FILES = re.compile(r'scripts/(npc|items|shops|heroes|regions|tutorial|bots?)/|items_game|neutral_items|'
                            r'npc_\w+\.txt|herolist|/localization/|patchnotes|'
                            # event and store content, sound mixing
                            r'scripts/(tournaments|events|stickers)/|scripts/(shops|change_log|chat_wheel)\.txt|\.eventdef|'
                            r'novels/|pulse/battle_pass|battle_report|bingo|candy_shop|craftworks|comics|fantasy|trophies|roadtoti|'
                            r'frostivus|_vdata_sentinel|sound(mixers|_operator_stacks)|soundstacks/')
BUILD_STAMP = re.compile(r'^[+-](ClientVersion|ServerVersion|PatchVersion|SourceRevision|VersionDate|VersionTime)=')
CONTENT_FOLDERS = re.compile(r' в (models|particles|sounds|soundevents|materials|maps|videos|media|'
                             r'panorama/images|panorama/videos|resource/localization|resource/flash3)\b')


def technical_tracking_blocks(blocks):
    """tracking-diff blocks without game content: the schema of single heroes/abilities/items, the
    game's KV and localization files, and assets (models, particles, sounds, images)."""
    out = []
    for title, lines in blocks:
        if title.startswith('SchemaSystem'):
            lines = filter_lines(lines, lambda l: not re.match(r'^[+~-] класс (\S+)', l) or
                                 not GAMEPLAY_CLASS.match(re.match(r'^[+~-] класс (\S+?):?(\s|$)', l).group(1)))
            n = {k: sum(1 for l in lines if l.startswith(f'{k} класс ')) for k in '+-~'}
            e = {k: sum(1 for l in lines if l.startswith(f'{k} enum ')) for k in '+-~'}
            if not any(n.values()) and not any(e.values()):
                continue
            title = (f"SchemaSystem (без классов отдельных героев, способностей и предметов): классов +{n['+']} "
                     f"−{n['-']} ~{n['~']}, enum +{e['+']} −{e['-']} ~{e['~']}")
        elif title.startswith('Текстовые файлы'):
            # a file's unified diff follows its '~ файл …' line unindented ('---', '@@', '-\t"Key"'),
            # so the file line decides for everything up to the next one
            kept, take = [], True
            for line in lines:
                if re.match(r'^[+~-] файл ', line):
                    take = not GAMEPLAY_FILES.search(line)
                if take:
                    kept.append(line)
            lines = kept
        elif title.startswith('Файлы игры'):
            # steam.inf changes every build (version, source revision, build time): only other edits count
            files, cur = [], None
            for line in lines:
                if re.match(r'^[+~-] файл ', line) or cur is None:
                    cur = [line]
                    files.append(cur)
                else:
                    cur.append(line)
            lines = [l for f in files if [x for x in f[1:] if re.match(r'^[+-](?![+-]{2} )', x) and not BUILD_STAMP.match(x)]
                     or not re.match(r'^[+~-] файл ', f[0]) for l in f]
        elif title.startswith('Индекс VPK'):
            kept, take = [], True
            for line in lines:
                if line.startswith('VPK '):
                    take = not CONTENT_FOLDERS.search(line) and not GAMEPLAY_FILES.search(line)
                if take:
                    kept.append(line)
            lines = kept
        # the title's counts are of the unfiltered block: count again what is left
        if title.startswith(('Текстовые файлы', 'Файлы игры')):
            n = {k: sum(1 for l in lines if l.startswith(f'{k} файл ')) for k in '+-~'}
            title = f"{title.split(':')[0]}: +{n['+']} −{n['-']} ~{n['~']}"
        elif title.startswith('Индекс VPK'):
            n = collections.Counter()
            for line in lines:
                m = re.match(r'^VPK (\S+): (\S+) в .*: (\d+)$', line)
                if m:
                    n[f'{m.group(1)}_{m.group(2)}'] += int(m.group(3))
            title = 'Индекс VPK (без ассетов и игровых файлов): ' + ', '.join(f'{k} {v}' for k, v in n.items())
        if [l for l in lines if l.strip()]:
            out.append((title, lines))
    return out


def tracking_counts(blocks):
    """Rows (label, +, −, ~) of the tracking/ table, counted over the filtered blocks."""
    rows = {'классы схемы': [0, 0, 0], 'enum схемы': [0, 0, 0], '.proto': [0, 0, 0],
            'файлы scripts/': [0, 0, 0], 'gameinfo / steam.inf': [0, 0, 0]}
    col = {'+': 0, '-': 1, '~': 2}
    for title, lines in blocks:
        if title.startswith('SchemaSystem'):
            for line in lines:
                m = re.match(r'^([+~-]) (класс|enum) ', line)
                if m:
                    rows['классы схемы' if m.group(2) == 'класс' else 'enum схемы'][col[m.group(1)]] += 1
        elif title.startswith('Protobuf'):
            m = re.search(r'\+(\d+) −(\d+) ~(\d+)', title)
            if m:
                rows['.proto'] = [int(x) for x in m.groups()]
        elif title.startswith(('Текстовые файлы', 'Файлы игры')):
            row = rows['файлы scripts/' if title.startswith('Текстовые') else 'gameinfo / steam.inf']
            for line in lines:
                m = re.match(r'^([+~-]) файл ', line)
                if m:
                    row[col[m.group(1)]] += 1
    return [(k, *v) for k, v in rows.items()]


CONVAR_ATTENTION = {'cheat', 'clientcmd_can_execute', 'server_can_execute', 'sv', 'rep', 'protected',
                    'devonly', 'hidden', 'release', 'per_user', 'user', 'norecord'}


def convar_blocks(version):
    """Flag / default / help changes of the console variables and commands that both versions have
    (the changelog only lists added and removed names). A command's flags decide who may run it:
    clientcmd_can_execute / server_can_execute are the allow lists of client and server commands."""
    cur_path = os.path.join(DATA, 'files', 'convars.json')
    if not os.path.exists(cur_path):
        return []
    revs = subprocess.run(['git', '-C', REPO, 'rev-list', DATA_REV, '--', 'files/convars.json'],
                          capture_output=True, text=True).stdout.split()
    prev = None
    for rev in revs:
        dump = subprocess.run(['git', '-C', REPO, 'show', f'{rev}:dumper/dump'], capture_output=True, text=True).stdout
        m = re.search(r'^ClientVersion=(\d+)', dump, re.M)
        if m and m.group(1) != str(version):
            prev = json.loads(subprocess.run(['git', '-C', REPO, 'show', f'{rev}:files/convars.json'],
                                             capture_output=True, text=True).stdout or '{}')
            break
    if not prev:
        return []
    cur = json.load(open(cur_path))
    lines = []
    for name in sorted(set(prev) & set(cur)):
        a, b = prev[name], cur[name]
        parts = []
        fa, fb = set(a.get('flags') or []), set(b.get('flags') or [])
        if fa != fb:
            parts.append('флаги ' + ' '.join([f'+{x}' for x in sorted(fb - fa)] + [f'−{x}' for x in sorted(fa - fb)]))
        if a.get('default') != b.get('default'):
            parts.append(f"по умолчанию {a.get('default')!r} -> {b.get('default')!r}")
        if (a.get('description') or '') != (b.get('description') or ''):
            parts.append(f"описание: {(a.get('description') or '')[:150]!r} -> {(b.get('description') or '')[:150]!r}")
        if parts:
            mark = '⚠ ' if (fa ^ fb) & CONVAR_ATTENTION else ''
            lines.append(f'{mark}~ {name}: ' + '; '.join(parts))
    return [(f'Консольные переменные и команды: флаги, значения по умолчанию и описания ({len(lines)})', lines)] if lines else []



def significant(entry):
    """A change with meaning beyond recompilation: strings, data constants or virtual calls."""
    return any(s.startswith(('строки', 'константы из данных', 'виртуальные вызовы', 'код тот же'))
               for s in entry['summary'])


REASONS = {'restriction': 'признаки ограничений (⚠)', 'technical': 'технические', 'gameplay': 'игровые (не разбираются)',
           'rebuild': 'от пересборки (не разбираются)', 'copy': 'копии существующего кода'}


def function_blocks(results, workspace=None):
    """Draft-model input: one block per technical changed function, those with signs of a restriction
    first (marked ⚠), added/removed ones in lists. Functions of single heroes/abilities/items and those
    a recompilation alone explains are only counted; what was left out, and why, goes to
    func-dropped.txt in the workspace. In a library with more than MANY_FUNCTIONS technical changed
    functions only the significant ones get a block, the others are listed by name."""
    blocks, dropped = [], []
    for r in results:
        cls = classify(r)
        counts = {k: 0 for k in REASONS}
        for e in r['entries']:
            if e['kind'] in ('changed', 'callee') or cls[id(e)] == 'copy':
                counts[cls[id(e)]] += 1
        c = r['counts']
        head = (f"функций {c['functions_old']} -> {c['functions_new']}, изменено {c['changed']} (из них "
                + ', '.join(f'{REASONS[k]} {n}' for k, n in counts.items() if n) +
                f"), добавлено {c['added']}, удалено {c['removed']}")
        blocks.append((f"Функции {r['lib']}: {head}", ['(дальше — каждая техническая изменённая функция отдельно; '
                                                      'игровые и изменения от пересборки только посчитаны)']))
        lists = {'added': [], 'removed': [], 'minor': []}
        technical = [e for e in r['entries'] if e['kind'] in ('changed', 'callee') and cls[id(e)] == 'technical']
        many = len(technical) > MANY_FUNCTIONS
        ordered = sorted(r['entries'], key=lambda e: cls[id(e)] != 'restriction')
        for e in ordered:
            kind = 'copy' if e['kind'].startswith('copy_') else e['kind']
            why = cls[id(e)]
            if why in ('gameplay', 'rebuild', 'copy'):
                dropped.append(f"{r['lib']}\t{why}\t{kind}\t{e['title'][:200]}")
                continue
            mark = '⚠ ' if why == 'restriction' else ''
            if why == 'restriction':
                signs = '; '.join(f'"{x[:60]}"' for x in restriction_signs(e))
            if kind in ('added', 'removed'):
                lists[kind].append(f"{mark}{e['title']}" + (f' [признаки: {signs}]' if mark else ''))
                continue
            if many and not mark and not significant(e) and not (e.get('calls_added') or e.get('calls_removed')):
                lists['minor'].append(f"{e['title'][:200]} ({'; '.join(e['summary'])})")
                continue
            lines = ([f'признаки ограничения: {signs}'] if mark else []) + [f"было: {e.get('was', '')}"] + \
                [f'- {x}' for x in e['summary']]
            if e['diff']:
                lines += ['дифф нормализованного кода (строки и константы подставлены, регистры как есть):']
                lines += e['diff']
                if e['diff_total'] > len(e['diff']):
                    lines.append(f"... ещё {e['diff_total'] - len(e['diff'])} строк")
            blocks.append((f"{mark}Функция {r['lib']} изменена: {e['title'][:300]}", lines))
        for kind, label in (('minor', 'изменены без новых строк, констант, вызовов и виртуальных вызовов (списком)'),
                            ('added', 'добавлены (технические)'), ('removed', 'удалены (технические)')):
            if lists[kind]:
                blocks.append((f"Функции {r['lib']} {label} ({len(lists[kind])})", lists[kind]))
    if workspace:
        with open(os.path.join(workspace, 'func-dropped.txt'), 'w') as f:
            f.write('библиотека\tпричина\tвид\tфункция\n' + '\n'.join(dropped) + '\n')
    return blocks


def render_functions(results, report_name):
    """Model-free part of the report: counts by kind, and the functions the report is about; every
    function with its code diff is in the -functions.md file."""
    out = ['### Функции', '',
           'Сравнение по функциям (funcdiff.py). Игровые функции (отдельные герои, способности, предметы, '
           'модификаторы) и изменения, которые объясняются одной пересборкой (регистры, сдвиги полей и слотов, '
           f'встраивание), в отчёт не входят: все функции с диффом кода — в [`{report_name}`]({report_name}).', '',
           '| библиотека | изменено | ⚠ признаки ограничений | технические | игровые | от пересборки | добавлено | удалено |',
           '|---|---|---|---|---|---|---|---|']
    shown = []
    for r in results:
        cls = classify(r)
        n = {k: sum(1 for e in r['entries'] if e['kind'] in ('changed', 'callee') and cls[id(e)] == k) for k in REASONS}
        c = r['counts']
        out.append(f"| {r['rel']} | {c['changed']} | {n['restriction']} | {n['technical']} | {n['gameplay']} | "
                   f"{n['rebuild']} | {c['added']} | {c['removed']} |")
        shown.append((r, [e for e in r['entries'] if e['kind'] in ('changed', 'callee', 'added', 'removed')
                          and cls[id(e)] in ('restriction', 'technical')], cls))
    out.append('')
    for r, entries, cls in shown:
        if not entries:
            continue
        out += [f"<details><summary>{r['lib']}: технические изменения ({len(entries)})</summary>", '']
        for e in sorted(entries, key=lambda e: cls[id(e)] != 'restriction')[:300]:
            mark = '⚠ ' if cls[id(e)] == 'restriction' else ''
            out.append(f"- {mark}{funcdiff.KIND[e['kind']]}: `{e['title'][:240]}`")
        if len(entries) > 300:
            out.append(f'- … ещё {len(entries) - 300}')
        out += ['', '</details>', '']
    return out


def previous_dump(version):
    """The raw dump of the version before (from git), for the final model to compare against."""
    revs = subprocess.run(['git', '-C', REPO, 'rev-list', DATA_REV, '--', 'dumper/dump'],
                          capture_output=True, text=True).stdout.split()
    for rev in revs:
        text = subprocess.run(['git', '-C', REPO, 'show', f'{rev}:dumper/dump'],
                              capture_output=True, text=True).stdout
        for line in text.splitlines()[:3]:
            if line.startswith('ClientVersion=') and line.split('=', 1)[1].strip() != str(version):
                return text
    return None


def previous_tracking(version, workspace):
    """tracking/ of the version before (game-tracking.py output committed with it), extracted into the
    workspace; None when no earlier commit has one."""
    revs = subprocess.run(['git', '-C', REPO, 'rev-list', DATA_REV, '--', 'tracking/manifest.json'],
                          capture_output=True, text=True).stdout.split()
    for rev in revs:
        manifest = subprocess.run(['git', '-C', REPO, 'show', f'{rev}:tracking/manifest.json'],
                                  capture_output=True, text=True).stdout
        try:
            built = json.loads(manifest).get('build', {}).get('ClientVersion')
        except ValueError:
            continue
        if built and built != str(version):
            dest = os.path.join(workspace, 'tracking-old')
            os.makedirs(dest, exist_ok=True)
            archive = subprocess.run(['git', '-C', REPO, 'archive', rev, 'tracking'], capture_output=True, check=True)
            subprocess.run(['tar', '-x', '-C', dest], input=archive.stdout, check=True)
            return os.path.join(dest, 'tracking'), built
    return None, None


def claude(args, prompt, cwd, timeout):
    env = {k: v for k, v in os.environ.items() if k not in ('CLAUDECODE', 'CLAUDE_CODE_ENTRYPOINT')}
    cmd = ['claude', '-p', '--no-session-persistence', '--strict-mcp-config', '--setting-sources', 'local',
           '--output-format', 'text'] + args
    try:
        res = subprocess.run(cmd, input=prompt, capture_output=True, text=True, timeout=timeout,
                             cwd=cwd, env=env)
    except (OSError, subprocess.TimeoutExpired) as e:
        return None, str(e)
    if res.returncode != 0 or not res.stdout.strip():
        return None, (res.stderr or res.stdout).strip()[:500]
    return res.stdout.strip(), None


DRAFT_PROMPT = """Ты делаешь первый, черновой проход по обновлению Dota 2 для разработчиков кастомных игр \
и серверных плагинов. Их интересует техника, а не сам патч: API (Lua, Panorama, события, перечисления, \
консольные переменные и команды), движок, клиентская и серверная части как платформа (интерфейс, ввод, \
консоль, сеть, VScript, Panorama, браузер, звук, система модификаторов и способностей в целом), протоколы \
и схема — и прежде всего всё, что ограничивает или меняет, что можно кастомке, клиенту или серверу.

Тебе дают одну часть данных: изменения API из дампа игры (строки «+» добавлено, «-» удалено, «~» \
изменено; изменения флагов, значений по умолчанию и описаний консольных переменных и команд), и/или дифф \
Linux-библиотек .so (строки из секций данных, экспортируемые символы), и/или изменённые функции кода, и/или \
изменения файлов игры (SchemaSystem, .proto, скрипты и Panorama из VPK). У функции: имя «Класс::Колбэк» или \
«Класс::vfunc#N», строки, сводка (строки/константы +/−, «цели вызовов» — какие функции она теперь вызывает \
и какие перестала, виртуальные вызовы, поля объектов) и дифф нормализованного кода: [S:"…"] строка, [K:…] \
константа из данных, F вызов другой функции, L переход внутри функции, [D]/[T] прочие адреса. Функции \
отдельных героев, способностей, предметов и модификаторов и изменения, которые объясняются одной пересборкой, \
уже убраны.

Что писать (по-русски, сгруппировав по смыслу, с точными именами, старым и новым значением):
- Сначала, с пометкой «⚠», — всё странное и всё, что похоже на ограничение: что-то выключается или \
ведёт себя иначе в кастомных играх (проверки режима игры: game mode 15 = DOTA_GAMEMODE_CUSTOM, «custom \
game», аддон), браузер, HTML-панели и URL (что открывается, куда разрешены запросы), белые и чёрные списки \
(консольных и клиентских команд, конваров, событий, адресов), новые флаги команд (cheat, \
clientcmd_can_execute, server_can_execute и т. п.), новые проверки прав, доверия и античита, лимиты и \
отказы («not allowed», «denied», «disabled»). Функции с признаками ограничения в данных уже помечены «⚠» — \
разбери каждую: что именно проверяется и что запрещается. Пиши даже о мелочи.
- Затем остальные технические изменения: что поменялось в логике функции (новая или убранная проверка, \
другой вызов, строки, константы), в API, в протоколах и схеме — и что это может значить для кастомок и \
плагинов (с пометкой «возможно», если это вывод).
- Отдельным списком в конце — все новые свойства, события и методы (модификаторов, Lua API, Panorama) с \
точными именами и сигнатурами.

Чего не писать совсем — ни подробно, ни одной строкой, ни чтобы сказать, что это оно: сам патч и его \
содержание (герои, способности, предметы, нейтралы, их модификаторы и классы схемы, баланс, тексты, \
ассеты); то, что объясняется пересборкой (другие регистры и смещения стека, сдвиги полей и слотов vtable, \
встраивание и вынос кода в другую функцию, перенос static-инициализации, вызов помощника вместо \
встроенного кода и наоборот, другие адреса вызовов и таблиц при том же коде, номера строк __LINE__ в \
сообщениях); шум дампера (значения, перечисленные во вводных как нестабильные). Без вступления и \
заключения."""

FINAL_PROMPT = """Ты проверяешь и доводишь технический отчёт об обновлении Dota 2 для разработчиков \
кастомных игр и серверных плагинов. Пиши по-русски, Markdown.

Отчёт — о технике, а не о патче. В нём: API, движок, клиент и сервер как платформа, протоколы и схема — \
и в первую очередь всё странное и всё, что ограничивает кастомки, клиент или сервер. Не упоминай вообще — \
ни подробно, ни одной строкой, ни чтобы сказать, что это игровое или пересборка: героев, способности, \
предметы, нейтралов, их модификаторы, их функции и классы схемы, баланс, тексты, ассеты, «это патч 7.xx»; \
то, что объясняется пересборкой (другие регистры, сдвиги полей и слотов vtable, встраивание и вынос кода \
в другую функцию, перенос static-инициализации, вызов помощника вместо встроенного кода и наоборот, другие \
адреса вызовов и таблиц при том же коде, номера строк __LINE__); шум дампера. Не пиши и о том, что \
что-то отфильтровано, «не разбирается» или «игровое» — просто не упоминай, и в «Что исправлено в черновике» \
тоже. Если раздел после этого пуст — одна строка.

В рабочем каталоге:
- digests/ — черновые конспекты всех частей данных (первый проход, без инструментов). Черновик ошибается: \
путает классы, выдаёт догадки за факты, пропускает важное, принимает шум или пересборку за изменения;
- chunks/ — исходные части, по которым писались конспекты (тот же номер);
- api-changes.txt — технические изменения API по дампу (игровые разделы убраны заранее) и изменения \
флагов, значений по умолчанию и описаний консольных переменных и команд; so-diff.txt — дифф строк и \
экспорта .so без строк игрового контента; func-diff.txt — технические изменённые, добавленные и удалённые \
функции (игровые и изменения от пересборки убраны заранее) с именами, строками, сводкой («цели вызовов» — \
какие функции она теперь вызывает и какие перестала) и диффом нормализованного кода ([S:…] строка, [K:…] \
константа из данных, F вызов, L переход внутри функции); dump-noise.md (если есть) — шум дампера; \
tracking-diff.txt (если есть) — технические изменения файлов игры: SchemaSystem без классов отдельных \
героев/способностей/предметов, .proto, скрипты и Panorama из VPK (файлы прошлой версии — tracking-old/, \
этой — tracking/ репозитория);
- previous-dump.txt — сырой дамп прошлой версии; в репозитории dota-data — files/*.json (текущее API, \
convars.json — флаги и значения конваров), dumper/dump (текущий сырой дамп);
- команда `python3 /root/dota-data/automation/so-query.py` (без аргументов печатает справку) — строки, \
символы, места использования строки в коде (xref), строки вокруг этих мест (context), дизассемблер \
Linux-библиотек установленной сборки («new»: libclient.so — клиент, интерфейс, Panorama-панели, браузер; \
libserver.so — сервер; libengine2.so — движок, сеть, консоль) и прошлой («old»), если её снимок есть; по \
функциям: funcs, fdiff (весь дифф функции), func (код с подставленными строками и константами, кто её \
вызывает и кого она), callers, vtable. Запускай её только так, одной командой: \
`python3 /root/dota-data/automation/so-query.py <аргументы>` — без cd, &&, ;, конвейеров (|) и \
перенаправлений, иначе вызов отклонят.

Работа: прочитай все конспекты. Каждое утверждение, которое попадёт в отчёт, проверь по исходным данным \
(Grep/Read по chunks, api-changes.txt, so-diff.txt, func-diff.txt, дампам; so-query для .so). Исправь \
неверное, убери неподтверждённое, игровое и объяснимое пересборкой, дополни пропущенное. Особенно ищи \
ограничения: функции, помеченные «⚠»; новые и изменённые проверки режима игры (сравнение с 15 = \
DOTA_GAMEMODE_CUSTOM, «custom game»); всё про браузер, HTML-панели и URL (по строкам browser/HTML/URL — \
xref и func: что проверяется перед открытием); белые и чёрные списки команд, конваров, событий и адресов \
(массивы имён в коде, новые флаги clientcmd_can_execute / server_can_execute / cheat в api-changes.txt); \
новые отказы и лимиты. Для каждого — что именно проверяется, что запрещается или меняется, для кого \
(кастомки, все игры, клиент, сервер), доказательства и надёжность. Если смысл неясен — так и скажи.

Новые свойства, события и методы проверяй не только по дампу, но и по коду (so-query: есть ли имя в \
libserver.so/libclient.so, где оно используется, что делает код) и объясняй, что каждое делает; учти тест \
HasFunction (modifier_properties.json: false — движок эту Lua-функцию не вызывает). Если код не нашёл — \
так и скажи.

Отчёт (заголовки третьего уровня, ###):
1. «Главное» — до 8 пунктов о технике обновления; первыми — пункты «⚠» про ограничения и странное, если \
они есть (этот раздел уходит в уведомления, поэтому важное — в его начале). Если ограничений нет, не пиши \
об этом здесь. Если технических изменений нет совсем — одна строка: «Технических изменений нет.»
2. «⚠ Ограничения и странное» — каждое ограничение и каждая странность подробно: что, где в коде \
(функция, строки, сравнение), для кого, что это ломает или меняет для кастомок и плагинов, надёжность \
вывода. Если ничего такого нет — одна строка: «Не найдено.» (без разбора ложных срабатываний).
3. «Новые свойства и методы: что делают» — по каждому: что делает, как пользоваться, доказательства и \
надёжность. Если новых нет — одна строка.
4. «Для разработчиков кастомок» — остальное новое, удалённое и изменённое в Lua API, Panorama, событиях, \
перечислениях, консольных переменных и командах (в том числе флаги и значения по умолчанию), KV-ключах; \
конкретные имена; что может сломать существующие аддоны.
5. «Клиент (libclient.so)» — подробный разбор технических изменений клиента: по системам (Panorama и \
интерфейс, HUD, браузер и HTML, ввод и клавиши, камера, консоль и команды, сеть и обработка сообщений, \
VScript на клиенте, звук, настройки): что именно поменялось в коде (новые или убранные проверки и условия, \
другие вызовы, строки, константы), что это значит, доказательства; разбирай код через so-query (fdiff, \
func, func old). Если технических изменений клиента нет — одна строка.
6. «Сервер и движок» — технические изменения libserver.so как платформы (сущности, модификаторы и \
способности в целом, Lua-биндинги, режимы игры, сеть) и библиотек движка (libengine2, libtier0, \
libnetworksystem, libvscript, libpanorama и др.): что и где.
7. «Схема и протоколы» — только техническое: классы схемы (новые и удалённые поля и классы платформы; \
сдвиги смещений — одной строкой на класс, какое поле их вызвало), .proto (новые сообщения и поля — что \
передают), скрипты и Panorama из VPK.
8. «Что исправлено в черновике» — коротко, только о выводах самого черновика: какой вывод был неверен или \
не подтвердился и что вместо него. Не перечисляй, чего нет в данных и что в отчёт не вошло. Если черновик \
верен — одна строка «Черновик подтверждён».
Только подтверждённое данными. Серверные Metamod-плагины сервера и их проверку не упоминай. Без вступления \
и заключения. Ответ — только сам отчёт."""


EMPTY_SUMMARY = """### Главное

Технических изменений нет.

### ⚠ Ограничения и странное

Не найдено."""


def run_drafts(workspace, chunks, noise_text):
    os.makedirs(os.path.join(workspace, 'chunks'))
    os.makedirs(os.path.join(workspace, 'digests'))
    jobs = []
    for n, parts in enumerate(chunks, 1):
        body = ''.join(text for _title, text in parts)
        with open(os.path.join(workspace, 'chunks', f'chunk-{n:02}.txt'), 'w') as f:
            f.write(body)
        intro = f'Часть {n} из {len(chunks)}.\n'
        if noise_text:
            intro += f'Нестабильные между дампами одной сборки значения (шум дампера):\n{noise_text}\n'
        jobs.append((n, [t for t, _ in parts], intro + '\n' + body))

    def draft(job):
        n, titles, prompt = job
        for _attempt in range(2):
            text, error = claude(['--model', DRAFT_MODEL, '--tools', '', '--system-prompt', DRAFT_PROMPT],
                                 prompt, workspace, 1200)
            if text:
                break
        header = f"# Конспект части {n:02}: {'; '.join(titles)}\n\n"
        with open(os.path.join(workspace, 'digests', f'digest-{n:02}.md'), 'w') as f:
            f.write(header + (text or f'_Черновая модель не справилась с этой частью ({error}); читай chunks/chunk-{n:02}.txt._'))
        return text is not None

    with concurrent.futures.ThreadPoolExecutor(DRAFT_WORKERS) as pool:
        done = list(pool.map(draft, jobs))
    return sum(done)


def run_final(workspace, add_dirs):
    args = ['--model', FINAL_MODEL, '--effort', FINAL_EFFORT, '--tools', 'Read Grep Glob Bash',
            '--allowedTools', 'Bash(python3 /root/dota-data/automation/so-query.py *)',
            '--permission-mode', 'dontAsk', '--system-prompt', FINAL_PROMPT]
    for d in add_dirs:
        args += ['--add-dir', d]
    task = 'Прочитай конспекты в digests/, проверь их по исходным данным и напиши отчёт.'
    if DATA != REPO:
        task += (f' Это отчёт о прошлой версии: её данные (files/, dumper/dump) лежат в {DATA} — читай их там, '
                 f'а не в {REPO} (там уже более новая версия).')
    text, error = claude(args, task,
                         workspace, 4 * 3600)
    if text:
        first = text.find('###')  # drop any preamble before the first section
        text = text[first:] if first > 0 else text
        marker = '### Что исправлено в черновике'
        if marker in text:
            before, after = text.split(marker, 1)
            text = (before.rstrip() + '\n\n<details><summary>Что исправлено в черновике при проверке</summary>\n\n'
                    + after.strip() + '\n\n</details>')
    return text, error


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument('version')
    p.add_argument('--out', required=True)
    p.add_argument('--noise', help='dump-checks report of this build (default: the newest for VERSION)')
    p.add_argument('--no-ai', action='store_true')
    p.add_argument('--data-rev', help='take the dump data from this commit (a report for an older version)')
    args = p.parse_args()
    version = args.version.split('-')[0]

    workspace = os.path.join(STATE, 'analysis', args.version)
    shutil.rmtree(workspace, ignore_errors=True)
    os.makedirs(workspace)
    # The unfiltered inputs and the list of what was left out, for people checking the filters; outside
    # the workspace, so that the model writes only about what it was given.
    full = workspace + '-full'
    shutil.rmtree(full, ignore_errors=True)
    os.makedirs(full)
    # Workspaces of the KEEP_ANALYSIS newest versions stay (for so-query and for checking a report);
    # older ones go, a big patch leaves a couple of hundred MB.
    analysis = os.path.join(STATE, 'analysis')
    by_version = {}
    for name in os.listdir(analysis):
        m = re.match(r'(\d+)', name)
        if m:
            by_version.setdefault(int(m.group(1)), []).append(name)
    for v in sorted(by_version)[:-KEEP_ANALYSIS]:
        if v != int(version):
            for name in by_version[v]:
                shutil.rmtree(os.path.join(analysis, name), ignore_errors=True)
    global DATA, DATA_REV
    if args.data_rev:
        DATA_REV = args.data_rev
        DATA = os.path.join(workspace, 'data')
        os.makedirs(DATA)
        paths = [p for p in ('files', 'dumper/dump', 'dump-checks', 'tracking') if subprocess.run(
            ['git', '-C', REPO, 'cat-file', '-e', f'{DATA_REV}:{p}'], capture_output=True).returncode == 0]
        archive = subprocess.run(['git', '-C', REPO, 'archive', DATA_REV] + paths, capture_output=True, check=True)
        subprocess.run(['tar', '-x', '-C', DATA], input=archive.stdout, check=True)

    blocks, api_table = api_blocks(version)
    blocks += convar_blocks(version)
    with open(os.path.join(workspace, 'api-changes.txt'), 'w') as f:
        f.write(''.join(f'### {t}\n' + '\n'.join(lines) + '\n\n' for t, lines in blocks))

    noise = args.noise or (sorted(glob.glob(os.path.join(DATA, 'dump-checks', f'{version}*.md')),
                                  key=os.path.getmtime) or [None])[-1]
    noise_text = ''
    if noise and os.path.exists(noise):
        shutil.copy(noise, os.path.join(workspace, 'dump-noise.md'))
        noise_text = open(noise).read()
    prev = previous_dump(version)
    if prev:
        with open(os.path.join(workspace, 'previous-dump.txt'), 'w') as f:
            f.write(prev)

    add_dirs = [REPO] + ([DATA] if DATA != REPO else [])
    current = current_snapshot(version)
    pair = snapshot_pair(version)
    if current:
        # so-query on the installed build's libraries (and the build before, when there is a snapshot)
        with open(os.path.join(workspace, 'so-query.json'), 'w') as f:
            json.dump({'old': os.path.join(so_report.STORE, pair[0]) if pair else None,
                       'new': os.path.join(so_report.STORE, current)}, f)
        add_dirs.append(os.path.join(so_report.STORE, current))
    files, func_results = [], []
    if pair:
        old, new = pair
        files, _anchors = so_report.build_diff(old, new)  # plugin anchors: not in this report
        so_all = so_report.diff_blocks(old, new, files, [])
        so_blocks = technical_so_blocks(so_all)
        blocks += so_blocks
        for path, bl in ((os.path.join(workspace, 'so-diff.txt'), so_blocks), (os.path.join(full, 'so-diff-all.txt'), so_all)):
            with open(path, 'w') as f:
                f.write(f'Снимки .so: {old} -> {new}\n\n' +
                        ''.join(f'### {t}\n' + '\n'.join(lines) + '\n\n' for t, lines in bl))
        add_dirs.append(os.path.join(so_report.STORE, old))
        func_results = function_diffs(old, new, files, workspace)
        if func_results:
            technical = []
            for r in func_results:
                cls = classify(r)
                technical.append(dict(r, entries=[e for e in r['entries'] if cls[id(e)] in ('restriction', 'technical')]))
            with open(os.path.join(workspace, 'func-diff.txt'), 'w') as f:
                f.write(f'Снимки .so: {old} -> {new}. Только технические функции\n\n' +
                        '\n'.join(funcdiff.render(r) for r in technical))
            with open(os.path.join(full, 'func-diff-all.txt'), 'w') as f:
                f.write(f'Снимки .so: {old} -> {new}\n\n' + '\n'.join(funcdiff.render(r) for r in func_results))
            blocks += function_blocks(func_results, full)

    tracking_table, tracking_old, t_blocks = None, None, []
    new_tracking = os.path.join(DATA, 'tracking')
    if os.path.exists(os.path.join(new_tracking, 'manifest.json')):
        old_tracking, tracking_old = previous_tracking(version, workspace)
        if old_tracking:
            t_all, tracking_table = tracking_diff.blocks(old_tracking, new_tracking)
            t_blocks = technical_tracking_blocks(t_all)
            for path, bl in ((os.path.join(workspace, 'tracking-diff.txt'), t_blocks),
                             (os.path.join(full, 'tracking-diff-all.txt'), t_all)):
                with open(path, 'w') as f:
                    f.write(f'tracking/: {tracking_old} -> {version}\n\n' +
                            ''.join(f'### {t}\n' + '\n'.join(lines) + '\n\n' for t, lines in bl))
            blocks += t_blocks

    chunks = chunk(blocks)
    if args.no_ai:
        summary, error, drafted = None, 'отключено (--no-ai)', 0
    elif not chunks:
        # nothing technical left after the filters: no model, a fixed summary (the commit body and
        # the Telegram message take «Главное»)
        summary, error, drafted = EMPTY_SUMMARY, None, 0
    else:
        drafted = run_drafts(workspace, chunks, noise_text)
        print(f'drafts: {drafted}/{len(chunks)} chunks by {DRAFT_MODEL}', file=sys.stderr)
        summary, error = run_final(workspace, add_dirs)
        if summary is None:
            print(f'final model failed: {error}', file=sys.stderr)
            return 2

    credit = (f'Черновик по всем изменениям (частей: {len(chunks)}) — {model_name(DRAFT_MODEL)}, проверка по исходным '
              f'данным и итог — {model_name(FINAL_MODEL)} (только с правом чтения); таблицы ниже посчитаны без модели.'
              if chunks else 'Технических изменений для разбора нет, модель не запускалась.')
    out = [f'# Dota {version}: что изменилось', '',
           f'Отчёт создан автоматически {datetime.date.today().isoformat()}. {credit}', '', '## Сводка', '',
           summary or f'_Без сводки: {error}_', '',
           '## Изменения API (дамп)', '',
           f'Полный список: [`files/changelogs/{version}.json`](../files/changelogs/{version}.json).', '']
    tech = [f'| {c} | {a} | {r} | {ch} |' for c, a, r, ch in api_table if (a or r or ch) and c not in GAMEPLAY_CATEGORIES]
    out += ['| раздел | + | − | ~ |', '|---|---|---|---|'] + tech if tech else ['Технических изменений нет.']
    game = [(c, a, r, ch) for c, a, r, ch in api_table if (a or r or ch) and c in GAMEPLAY_CATEGORIES]
    if game:
        out += ['', 'Игровые разделы (способности, юниты, модификаторы, их формулы, тексты) в отчёте не разбираются: ' +
                ', '.join(f'{c} +{a} −{r} ~{ch}' for c, a, r, ch in game) + '.']
    out.append('')
    if noise and os.path.exists(noise):
        rel = os.path.relpath(noise, os.path.dirname(os.path.abspath(args.out)))
        out += ['## Шум дампера', '',
                f'Контрольный дамп той же сборки разошёлся с основным: [`{os.path.basename(noise)}`]({rel}). '
                'Эти строки не считаются изменениями игры.', '']
    if tracking_table is not None:
        out += ['## Файлы игры (tracking/)', '',
                f'Сравнение с {tracking_old}: SchemaSystem, .proto, текстовые файлы из VPK и индекс VPK '
                '([`tracking/`](../tracking/)).', '']
        rows = [f'| {label} | {a} | {r} | {c} |' for label, a, r, c in tracking_counts(t_blocks) if a or r or c]
        out += ['| что | + | − | ~ |', '|---|---|---|---|'] + rows if rows else ['Технических изменений нет.']
        out += ['', 'Ассеты (модели, частицы, звуки, изображения) и игровые файлы scripts/ в отчёте не разбираются.', '']
    out += ['## Бинарники (.so)', '']
    if pair:
        out += [f'Снимки `{pair[0]}` → `{pair[1]}`.', '']
        binaries = so_report.render_binaries(files, [], h='###', anchors=False)
        cut = next((i for i, line in enumerate(binaries) if line.startswith('<details>')), len(binaries))
        functions = os.path.splitext(args.out)[0] + '-functions.md'
        os.makedirs(os.path.dirname(os.path.abspath(functions)), exist_ok=True)
        out += binaries[:cut] + [f'Добавленные и удалённые строки каждой библиотеки — в [`{os.path.basename(functions)}`]'
                                 f'({os.path.basename(functions)}).', '']
        if func_results:
            out += render_functions(func_results, os.path.basename(functions))
        with open(functions, 'w') as f:
            f.write(f'# Dota {version}: изменения кода по функциям и строки библиотек\n\n'
                    f'Снимки `{pair[0]}` → `{pair[1]}`; funcdiff.py. В диффе: [S:…] — строка, [K:…] — '
                    'константа из данных, F — вызов другой функции, L — переход внутри функции, [D]/[T] — '
                    'прочие адреса. Регистры и смещения стека меняются и от перекомпиляции. Здесь всё, в том числе '
                    'игровые функции и изменения от пересборки.\n\n'
                    + '\n'.join(funcdiff.render(r) for r in func_results) + '\n\n## Строки библиотек\n\n'
                    + '\n'.join(binaries[cut:]))
    else:
        out += ['Нет снимка .so этой или предыдущей сборки — сравнивать не с чем.']
    os.makedirs(os.path.dirname(os.path.abspath(args.out)), exist_ok=True)
    with open(args.out, 'w') as f:
        f.write('\n'.join(out).rstrip() + '\n')
    print(f'report: {args.out}')
    # The extracted copies (data/, tracking-old/) are big; chunks, digests and diffs stay for so-query.
    for big in ('data', 'tracking-old'):
        shutil.rmtree(os.path.join(workspace, big), ignore_errors=True)
    return 0


if __name__ == '__main__':
    sys.exit(main())
