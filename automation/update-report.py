#!/usr/bin/env python3
"""
The report of a Dota update, reports/<version>.md: what changed in the API (the dump's changelog,
files/changelogs/<version>.json) and in the Linux .so files (two snapshots of so-report.py).

Two models, both through the `claude` CLI (the server's Claude Code subscription login, or
ANTHROPIC_API_KEY when set), no spending cap:

1. Claude Haiku 4.5 goes through everything, uncapped: the changelog and the .so diff are cut into
   chunks (by category / library and string group) and each chunk gets a detailed digest with the
   exact names (a few chunks in parallel, no tools: the chunk is the whole input).
2. Claude Opus 5.5 reads the digests, checks every claim that goes into the report against the raw
   data, fixes and completes them, and writes the report, listing what it corrected. It works as a
   read-only agent: Read/Grep/Glob inside the analysis workspace, this repo, the two snapshots and
   the Metamod plugin sources, and one shell command, automation/so-query.py (strings, symbols,
   string references, disassembly of the snapshots); `--permission-mode dontAsk` refuses
   everything else, nothing can be written.

    update-report.py VERSION --out reports/VERSION.md [--no-ai]

Exit code 0: written (or --no-ai); 2: a model failed, nothing written (the sync retries later).
"""
import argparse
import concurrent.futures
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
DRAFT_MODEL = os.environ.get('REPORT_DRAFT_MODEL', 'claude-haiku-4-5')
FINAL_MODEL = os.environ.get('REPORT_FINAL_MODEL', 'claude-opus-5-5')
FINAL_EFFORT = os.environ.get('REPORT_FINAL_EFFORT', 'high')
CHUNK_CHARS = int(os.environ.get('REPORT_CHUNK_CHARS', '60000'))
DRAFT_WORKERS = int(os.environ.get('REPORT_DRAFT_WORKERS', '3'))


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


def api_blocks(version):
    """The whole changelog as (title, lines) blocks, one per category, and the count table."""
    with open(os.path.join(REPO, 'files', 'changelogs', f'{version}.json')) as f:
        log = json.load(f)
    blocks, table = [], []
    for category, change in log['changes'].items():
        added, removed, changed = (change.get(k) or [] for k in ('added', 'removed', 'changed'))
        table.append((category, len(added), len(removed), len(changed)))
        lines = [f'+ {item_text(i)}' for i in added] + [f'- {item_text(i)}' for i in removed] + \
            [f'~ {changed_text(i)}' for i in changed]
        if lines:
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


def snapshot_pair(version):
    snaps = so_report.list_snapshots()
    new = [s for s in snaps if s.split('-')[0] == str(version)]
    if not new:
        return None
    newest = new[-1]
    older = snaps[:snaps.index(newest)]
    return (older[-1], newest) if older else None


def previous_dump(version):
    """The raw dump of the version before (from git), for the final model to compare against."""
    revs = subprocess.run(['git', '-C', REPO, 'rev-list', 'HEAD', '--', 'dumper/dump'],
                          capture_output=True, text=True).stdout.split()
    for rev in revs:
        text = subprocess.run(['git', '-C', REPO, 'show', f'{rev}:dumper/dump'],
                              capture_output=True, text=True).stdout
        for line in text.splitlines()[:3]:
            if line.startswith('ClientVersion=') and line.split('=', 1)[1].strip() != str(version):
                return text
    return None


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


DRAFT_PROMPT = """Ты делаешь первый, черновой проход по обновлению Dota 2. Тебе дают одну часть данных: \
изменения API из дампа игры (Lua API и константы, Panorama API/события/панели, модификаторы, консольные \
переменные, способности, юниты, локализация; строки «+» добавлено, «-» удалено, «~» изменено) и/или \
дифф Linux-библиотек .so (строки из секций данных, экспортируемые символы).

Перечисли по-русски ВСЕ значимые изменения этой части, сгруппировав по смыслу: точные имена (функции, \
классы, константы, переменные, модификаторы, способности, предметы, юниты), что добавилось, удалилось \
или изменилось (со старым и новым значением, если оно есть), и короткую трактовку, только если она \
прямо следует из данных. Догадки помечай словом «возможно». Однотипную массу (например, сотни строк \
локализации или похожих строк) своди в группу с подсчётом и примерами. Шум дампера — значения, \
перечисленные во вводных как нестабильные, — изменениями не считай. Без вступления и заключения."""

FINAL_PROMPT = """Ты проверяешь и доводишь отчёт об обновлении Dota 2 для владельца сервера с \
кастомными играми и Metamod-плагинами. Пиши по-русски, Markdown.

В рабочем каталоге:
- digests/ — черновые конспекты всех частей данных от Claude Haiku. Haiku быстрый, но ошибается: \
путает героев и предметы, делает опечатки, выдаёт догадки за факты, пропускает важное, принимает \
шум за изменения;
- chunks/ — исходные части, по которым писались конспекты (тот же номер);
- api-changes.txt — все изменения API по дампу; so-diff.txt (если есть) — весь дифф .so; \
dump-noise.md (если есть) — шум дампера: чем различаются два дампа одной сборки, это не изменения игры;
- previous-dump.txt — сырой дамп прошлой версии; в репозитории dota-data — files/*.json (текущее API) \
и dumper/dump (текущий сырой дамп); исходники Metamod-плагинов;
- команда `python3 /root/dota-data/automation/so-query.py` (без аргументов печатает справку) — строки, \
символы, места использования строки в коде и дизассемблер обоих снимков .so. Других команд нет.

Работа: прочитай все конспекты. Каждое утверждение, которое попадёт в отчёт, проверь по исходным \
данным (Grep/Read по chunks, api-changes.txt, so-diff.txt, дампам; so-query для .so). Исправь \
неверное, убери неподтверждённое, дополни важное, что Haiku пропустил (пробегись по крупным разделам \
исходных частей). Если есть so-diff.txt и в нём есть строки-якоря плагинов, выясни, что с ними стало \
(so-query xref по старому и новому снимку).

Отчёт (заголовки третьего уровня, ###):
1. «Главное» — 3–8 пунктов: что по сути поменялось (контент, механики, системы).
2. «Для разработчиков кастомок» — новое, удалённое и изменённое в Lua API, Panorama, событиях, \
модификаторах, консольных переменных; конкретные имена; что может сломать существующие аддоны.
3. «Бинарники и плагины» — только если есть so-diff.txt: что видно по .so, риски для плагинов \
(конкретные плагины и что проверить).
4. «Что исправлено в черновике» — коротко: что у Haiku было неверно, неподтверждено или пропущено.
Только подтверждённое данными; если смысл неясен — так и скажи. Без вступления и заключения. \
Ответ — только сам отчёт."""


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
            f.write(header + (text or f'_Haiku не справился с этой частью ({error}); читай chunks/chunk-{n:02}.txt._'))
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
    text, error = claude(args, 'Прочитай конспекты в digests/, проверь их по исходным данным и напиши отчёт.',
                         workspace, 5400)
    if text:
        first = text.find('###')  # drop any preamble before the first section
        text = text[first:] if first > 0 else text
        marker = '### Что исправлено в черновике'
        if marker in text:
            before, after = text.split(marker, 1)
            text = (before.rstrip() + '\n\n<details><summary>Что Opus исправил в черновике Haiku</summary>\n\n'
                    + after.strip() + '\n\n</details>')
    return text, error


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

    blocks, api_table = api_blocks(version)
    with open(os.path.join(workspace, 'api-changes.txt'), 'w') as f:
        f.write(''.join(f'### {t}\n' + '\n'.join(lines) + '\n\n' for t, lines in blocks))

    noise = args.noise or (sorted(glob.glob(os.path.join(REPO, 'dump-checks', f'{version}*.md')),
                                  key=os.path.getmtime) or [None])[-1]
    noise_text = ''
    if noise and os.path.exists(noise):
        shutil.copy(noise, os.path.join(workspace, 'dump-noise.md'))
        noise_text = open(noise).read()
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
        so_blocks = so_report.diff_blocks(old, new, files, anchor_hits)
        blocks += so_blocks
        with open(os.path.join(workspace, 'so-diff.txt'), 'w') as f:
            f.write(f'Снимки .so: {old} -> {new}\n\n' +
                    ''.join(f'### {t}\n' + '\n'.join(lines) + '\n\n' for t, lines in so_blocks))
        with open(os.path.join(workspace, 'so-query.json'), 'w') as f:
            json.dump({'old': os.path.join(so_report.STORE, old), 'new': os.path.join(so_report.STORE, new)}, f)
        add_dirs += [os.path.join(so_report.STORE, old), os.path.join(so_report.STORE, new)]

    chunks = chunk(blocks)
    if args.no_ai:
        summary, error, drafted = None, 'отключено (--no-ai)', 0
    else:
        drafted = run_drafts(workspace, chunks, noise_text)
        print(f'drafts: {drafted}/{len(chunks)} chunks by {DRAFT_MODEL}', file=sys.stderr)
        summary, error = run_final(workspace, add_dirs)
        if summary is None:
            print(f'final model failed: {error}', file=sys.stderr)
            return 2

    out = [f'# Dota {version}: что изменилось', '',
           f'Отчёт создан автоматически {datetime.date.today().isoformat()}. Черновик по всем изменениям '
           f'({len(chunks)} частей) — Claude Haiku 4.5, проверка по исходным данным и итог — Claude Opus 5.5 '
           '(оба только с правом чтения); таблицы ниже посчитаны без модели.', '', '## Сводка', '',
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
