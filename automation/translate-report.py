#!/usr/bin/env python3
"""
The English version of an update report: reports/<version>.md (written in Russian by
update-report.py) translated into reports/<version>.en.md, which the site shows when its reader
picks English.

One model through the `claude` CLI (the same login as update-report.py), no tools: the report is
the whole input. The translation is checked against the original: the same headings, table rows,
<details> blocks and link targets, a similar length and no Russian prose left. When it does not
match, nothing is written.

    translate-report.py reports/VERSION.md [--out reports/VERSION.en.md]

Exit code 0: written; 2: the model failed or the translation did not match (the sync retries later).
"""
import argparse
import os
import re
import subprocess
import sys
import tempfile

MODEL = os.environ.get('REPORT_TRANSLATE_MODEL', 'claude-sonnet-5-5')
TIMEOUT = int(os.environ.get('REPORT_TRANSLATE_TIMEOUT', '3600'))

PROMPT = """You translate an automatically written report about a Dota 2 update from Russian into \
English. Its readers are developers of Dota 2 custom games.

Translate all Russian text: prose, headings, list items, table headers and cells, the text of \
<summary> tags, quoted game texts (keep the quotes). Use the usual English Dota 2 names of heroes, \
abilities and items. Keep everything else exactly as it is: the Markdown structure (the same headings, \
lists, tables with the same rows, blank lines), HTML tags such as <details> and <summary>, link \
targets, code spans and code blocks (identifiers, file names, addresses, commands and their output). \
Do not add, drop, shorten, merge or comment on anything: every sentence of the original has its \
translation. The answer is only the translated document."""


def claude(args, prompt, cwd, timeout):
    env = {k: v for k, v in os.environ.items() if k not in ('CLAUDECODE', 'CLAUDE_CODE_ENTRYPOINT')}
    cmd = ['claude', '-p', '--no-session-persistence', '--strict-mcp-config', '--setting-sources', 'local',
           '--output-format', 'text'] + args
    try:
        res = subprocess.run(cmd, input=prompt, capture_output=True, text=True, encoding='utf-8',
                             timeout=timeout, cwd=cwd, env=env)
    except (OSError, subprocess.TimeoutExpired) as e:
        return None, str(e)
    if res.returncode != 0 or not res.stdout.strip():
        return None, (res.stderr or res.stdout).strip()[:500]
    return res.stdout.strip(), None


CODE = re.compile(r'```.*?```|`[^`\n]*`', re.S)


def structure(text):
    lines = text.splitlines()
    return {
        'heading levels': [len(line) - len(line.lstrip('#')) for line in lines if re.match(r'#{1,6} ', line)],
        'table rows': sum(1 for line in lines if line.lstrip().startswith('|')),
        '<details> blocks': text.count('<details>'),
        'link targets': sorted(re.findall(r'\]\(([^)\s]+)\)', text)),
    }


def problems(original, translation):
    """What makes the translation unusable: a different structure, a cut or padded text, Russian left."""
    found = [f'{key} differ' for key, value in structure(original).items() if structure(translation)[key] != value]
    ratio = len(translation) / max(len(original), 1)
    if not 0.6 <= ratio <= 1.6:
        found.append(f'length ratio {ratio:.2f}')
    prose = CODE.sub('', translation)
    cyrillic = len(re.findall(r'[А-Яа-яЁё]', prose))
    letters = len(re.findall(r'[A-Za-zА-Яа-яЁё]', prose))
    if cyrillic > 0.01 * max(letters, 1):
        found.append(f'{cyrillic} Cyrillic letters outside code')
    return found


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument('report')
    p.add_argument('--out', help='default: the report with .en.md')
    args = p.parse_args()
    out = args.out or os.path.splitext(args.report)[0] + '.en.md'

    with open(args.report, encoding='utf-8') as f:
        original = f.read()
    with tempfile.TemporaryDirectory() as cwd:  # no project files for the model to pick up
        text, error = claude(['--model', MODEL, '--tools', '', '--system-prompt', PROMPT], original, cwd, TIMEOUT)
    if text is None:
        print(f'translation failed: {error}', file=sys.stderr)
        return 2
    text = text[text.find('#'):] if text.find('#') > 0 else text  # drop any preamble
    found = problems(original, text)
    if found:
        print(f"translation rejected: {'; '.join(found)}", file=sys.stderr)
        return 2
    with open(out, 'w', encoding='utf-8', newline='\n') as f:
        f.write(text.rstrip() + '\n')
    print(f'translation: {out}')
    return 0


if __name__ == '__main__':
    sys.exit(main())
