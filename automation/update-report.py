#!/usr/bin/env python3
"""
The report of a Dota update, reports/<version>.md: what changed in the API (the dump's changelog,
files/changelogs/<version>.json) and in the Linux .so files (two snapshots of so-report.py),
summarised by Claude Haiku 4.5.

The model runs through the `claude` CLI (the Claude Code login of the server, or
ANTHROPIC_API_KEY when set) as a small read-only agent: Read/Grep/Glob inside the analysis
workspace, this repo, the two snapshots and the Metamod plugin sources, and one shell command,
automation/so-query.py (strings, symbols, string references, disassembly of the snapshots).
`--permission-mode dontAsk` refuses everything else, nothing can be written.

    update-report.py VERSION --out reports/VERSION.md [--no-ai]

Exit code 0: written with a summary (or --no-ai); 2: the model failed, nothing written.
"""
import argparse
import datetime
import glob
import importlib.util
import json
import os
import shutil
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
spec = importlib.util.spec_from_file_location('so_report', os.path.join(HERE, 'so-report.py'))
so_report = importlib.util.module_from_spec(spec)
spec.loader.exec_module(so_report)

STATE = os.environ.get('DOTA_DATA_STATE', '/var/lib/dota-data')
MODEL = os.environ.get('REPORT_MODEL', 'claude-haiku-4-5')
BUDGET_USD = os.environ.get('REPORT_BUDGET_USD', '2')
PER_CATEGORY = 150


def item_text(item):
    name = item.get('name', '?')
    if item.get('class'):
        name = f"{item['class']}.{name}"
    extra = item.get('signature') or item.get('value') or item.get('description') or ''
    if isinstance(extra, (dict, list)):
        extra = json.dumps(extra, ensure_ascii=False)
    kind = item.get('type', '')
    return f"{kind} {name}{' — ' + str(extra)[:160] if extra and extra != name else ''}".strip()


def changed_text(item):
    parts = []
    for field, change in (item.get('changes') or {}).items():
        if isinstance(change, dict) and 'old' in change:
            parts.append(f"{field}: {str(change['old'])[:120]} -> {str(change['new'])[:120]}")
    return f"{item_text(item)} [{'; '.join(parts)}]"


def api_changes(version):
    path = os.path.join(REPO, 'files', 'changelogs', f'{version}.json')
    with open(path) as f:
        log = json.load(f)
    lines, table = [f"Изменения API по дампу Dota {version} (changelog {log.get('date')})", ''], []
    for category, change in log['changes'].items():
        added, removed, changed = (change.get(k) or [] for k in ('added', 'removed', 'changed'))
        table.append((category, len(added), len(removed), len(changed)))
        if not (added or removed or changed):
            continue
        lines.append(f'## {category}: +{len(added)} -{len(removed)} ~{len(changed)}')
        for label, items, fmt in (('+', added, item_text), ('-', removed, item_text), ('~', changed, changed_text)):
            for item in items[:PER_CATEGORY]:
                lines.append(f'{label} {fmt(item)}')
            if len(items) > PER_CATEGORY:
                lines.append(f'{label} ... ещё {len(items) - PER_CATEGORY}')
        lines.append('')
    return '\n'.join(lines), table


def snapshot_pair(version):
    snaps = so_report.list_snapshots()
    new = [s for s in snaps if s.split('-')[0] == str(version)]
    if not new:
        return None
    newest = new[-1]
    older = snaps[:snaps.index(newest)]
    return (older[-1], newest) if older else None


SYSTEM_PROMPT = """Ты разбираешь обновление Dota 2 для владельца сервера с кастомными играми и Metamod-\
плагинами и пишешь по-русски отчёт в Markdown.

Данные в рабочем каталоге (читай их инструментом Read):
- api-changes.txt — изменения API по дампу (Lua API и константы, Panorama API/события/панели, \
модификаторы, консольные переменные, способности, юниты, локализация);
- dump-noise.md, если есть, — то, чем различаются два дампа одной и той же сборки. Это шум \
дампера (например, номера динамически регистрируемых активностей), а не изменения игры: не выдавай \
его за изменения;
- so-diff.txt, если есть, — дифф строк и экспортов .so-библиотек Linux между сборками и строки, по \
которым наши плагины ищут код, если они пропали.
Глубже копать можно: Grep/Read по репозиторию dota-data (files/*.json — текущее API, dumper/dump — \
сырой дамп, previous-dump.txt в рабочем каталоге — дамп прошлой версии), по исходникам плагинов, и \
команда `python3 /root/dota-data/automation/so-query.py` (без аргументов печатает справку: строки, \
символы, места использования строки в коде, дизассемблер обоих снимков). Других команд нет. \
Копай только если это меняет вывод: например, чтобы понять, что делает новая функция, или проверить, \
используется ли ещё строка-якорь плагина.

Разделы отчёта (заголовки третьего уровня, ###):
1. «Главное» — 3–8 пунктов: что по сути поменялось (контент, механики, системы).
2. «Для разработчиков кастомок» — новое, удалённое и изменённое в Lua API, Panorama, событиях, \
модификаторах, консольных переменных; конкретные имена; что может сломать существующие аддоны.
3. «Бинарники и плагины» — только если есть so-diff.txt: что видно по .so, риски для плагинов \
(конкретные плагины и что проверить).
Опирайся только на данные; если смысл неясен — так и скажи. Без вступления и заключения. Ответ — \
только сам отчёт."""


def run_model(workspace, add_dirs):
    allowed = 'Bash(python3 /root/dota-data/automation/so-query.py *)'
    cmd = ['claude', '-p', '--model', MODEL,
           '--tools', 'Read Grep Glob Bash', '--allowedTools', allowed,
           '--permission-mode', 'dontAsk', '--setting-sources', 'local',
           '--no-session-persistence', '--strict-mcp-config', '--max-budget-usd', BUDGET_USD,
           '--system-prompt', SYSTEM_PROMPT, '--output-format', 'text']
    for d in add_dirs:
        cmd += ['--add-dir', d]
    env = {k: v for k, v in os.environ.items() if k not in ('CLAUDECODE', 'CLAUDE_CODE_ENTRYPOINT')}
    prompt = ('Разбери обновление по файлам рабочего каталога и напиши отчёт. '
              'Начни с api-changes.txt, затем dump-noise.md и so-diff.txt, если они есть.')
    try:
        res = subprocess.run(cmd, input=prompt, capture_output=True, text=True, timeout=1800,
                             cwd=workspace, env=env)
    except (OSError, subprocess.TimeoutExpired) as e:
        return None, str(e)
    if res.returncode != 0 or not res.stdout.strip():
        return None, (res.stderr or res.stdout).strip()[:500]
    text = res.stdout.strip()
    # Drop any preamble before the first section ("Анализирую файлы...").
    first = text.find('###')
    return (text[first:] if first > 0 else text), None


def previous_dump(version):
    """The raw dump of the version before (from git), for the model to compare against."""
    revs = subprocess.run(['git', '-C', REPO, 'rev-list', 'HEAD', '--', 'dumper/dump'],
                          capture_output=True, text=True).stdout.split()
    for rev in revs:
        text = subprocess.run(['git', '-C', REPO, 'show', f'{rev}:dumper/dump'],
                              capture_output=True, text=True).stdout
        for line in text.splitlines()[:3]:
            if line.startswith('ClientVersion=') and line.split('=', 1)[1].strip() != str(version):
                return text
    return None


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument('version')
    p.add_argument('--out', required=True)
    p.add_argument('--noise', help='dump-checks report of this build (default: the newest for VERSION)')
    p.add_argument('--no-ai', action='store_true')
    args = p.parse_args()
    version = args.version.split('-')[0]

    workspace = os.path.join(STATE, 'analysis', args.version)
    shutil.rmtree(workspace, ignore_errors=True)
    os.makedirs(workspace)
    api_text, api_table = api_changes(version)
    with open(os.path.join(workspace, 'api-changes.txt'), 'w') as f:
        f.write(api_text)

    noise = args.noise or (sorted(glob.glob(os.path.join(REPO, 'dump-checks', f'{version}*.md')),
                                  key=os.path.getmtime) or [None])[-1]
    if noise and os.path.exists(noise):
        shutil.copy(noise, os.path.join(workspace, 'dump-noise.md'))
    prev = previous_dump(version)
    if prev:
        with open(os.path.join(workspace, 'previous-dump.txt'), 'w') as f:
            f.write(prev)

    add_dirs = [REPO] + sorted(glob.glob(so_report.PLUGIN_SOURCE.format('*')))
    pair = snapshot_pair(version)
    files, anchor_hits = [], []
    if pair:
        old, new = pair
        files, anchor_hits = so_report.build_diff(old, new)
        with open(os.path.join(workspace, 'so-diff.txt'), 'w') as f:
            f.write(so_report.model_input(old, new, files, anchor_hits))
        with open(os.path.join(workspace, 'so-query.json'), 'w') as f:
            json.dump({'old': os.path.join(so_report.STORE, old), 'new': os.path.join(so_report.STORE, new)}, f)
        add_dirs += [os.path.join(so_report.STORE, old), os.path.join(so_report.STORE, new)]

    if args.no_ai:
        summary, error = None, 'отключено (--no-ai)'
    else:
        summary, error = run_model(workspace, add_dirs)
        if summary is None:
            print(f'model failed: {error}', file=sys.stderr)
            return 2

    out = [f'# Dota {version}: что изменилось', '',
           f'Отчёт создан автоматически {datetime.date.today().isoformat()}. Сводку написал Claude Haiku 4.5 '
           'по изменениям API из дампа и по .so-библиотекам (с доступом только на чтение); таблицы ниже '
           'посчитаны без модели.', '', '## Сводка', '',
           summary or f'_Без сводки: {error}_', '',
           '## Изменения API (дамп)', '',
           f'Полный список: [`files/changelogs/{version}.json`](../files/changelogs/{version}.json).', '',
           '| раздел | + | − | ~ |', '|---|---|---|---|']
    out += [f'| {c} | {a} | {r} | {ch} |' for c, a, r, ch in api_table if a or r or ch]
    out.append('')
    if noise and os.path.exists(noise):
        rel = os.path.relpath(noise, os.path.dirname(os.path.abspath(args.out)))
        out += ['## Шум дампера', '',
                f'Контрольный дамп той же сборки разошёлся с основным: [`{os.path.basename(noise)}`]({rel}). '
                'Эти строки не считаются изменениями игры.', '']
    out += ['## Бинарники (.so)', '']
    if pair:
        out += [f'Снимки `{pair[0]}` → `{pair[1]}`.', '']
        out += so_report.render_binaries(files, anchor_hits, h='###')
    else:
        out += ['Нет снимка .so предыдущей сборки — сравнивать не с чем.']
    os.makedirs(os.path.dirname(os.path.abspath(args.out)), exist_ok=True)
    with open(args.out, 'w') as f:
        f.write('\n'.join(out).rstrip() + '\n')
    print(f'report: {args.out}')
    return 0


if __name__ == '__main__':
    sys.exit(main())
