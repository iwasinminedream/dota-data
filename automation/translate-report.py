#!/usr/bin/env python3
"""
The English version of an update report: reports/<version>.md (written in Russian by
update-report.py) translated into reports/<version>.en.md, which the site shows when its reader
picks English.

One model through the `claude` CLI (the same login as update-report.py), no tools. Code blocks and
inline code never reach the model: they are swapped for placeholders (⟦B12⟧, ⟦I345⟧) and put back
verbatim afterwards, so the model only sees the prose. That prose is translated in chunks cut at
headings (at most CHUNK characters each, a few in parallel): after a big patch a report can be close
to a megabyte, almost all of it code, and one answer cannot hold its translation. Every chunk is
checked against its original (the same placeholders, headings, table rows, <details> blocks and link
targets, a similar length, no Russian prose left) and asked again when it does not match; the whole
translation is checked once more at the end. When anything does not match, nothing is written.

    translate-report.py reports/VERSION.md [--out reports/VERSION.en.md]

Exit code 0: written; 2: the model failed or the translation did not match (the sync retries later).
Environment: REPORT_TRANSLATE_MODEL, REPORT_TRANSLATE_TIMEOUT (seconds per chunk),
REPORT_TRANSLATE_CHUNK (characters), REPORT_TRANSLATE_WORKERS.
"""
import argparse
import concurrent.futures
import os
import re
import subprocess
import sys
import tempfile

MODEL = os.environ.get('REPORT_TRANSLATE_MODEL', 'claude-sonnet-5-5')
TIMEOUT = int(os.environ.get('REPORT_TRANSLATE_TIMEOUT', '1800'))
CHUNK = int(os.environ.get('REPORT_TRANSLATE_CHUNK', '14000'))
WORKERS = int(os.environ.get('REPORT_TRANSLATE_WORKERS', '3'))
ATTEMPTS = 3

PROMPT = """You translate an automatically written report about a Dota 2 update from Russian into \
English. Its readers are developers of Dota 2 custom games.

Translate all Russian text: prose, headings, list items, table headers and cells, the text of \
<summary> tags, quoted game texts (keep the quotes). Use the usual English Dota 2 names of heroes, \
abilities and items. Keep everything else exactly as it is: the Markdown structure (the same headings, \
lists, tables with the same rows, blank lines), HTML tags such as <details> and <summary>, link \
targets, code spans and code blocks (identifiers, file names, addresses, commands and their output). \
Do not add, drop, shorten, merge or comment on anything: every sentence of the original has its \
translation. Write headings in sentence case (capitalise only the first word and proper names). The \
answer is only the translated document.

The text you get is one part of the report, and its code has been replaced by placeholders such as \
⟦B12⟧ (a code block) and ⟦I345⟧ (inline code). Copy every placeholder exactly as it is, once, in the \
matching place of the translation; never translate, change, drop, merge or add placeholders. A \
placeholder that stands alone on a line stays alone on its line."""

FENCE = re.compile(r'```.*?```', re.S)
INLINE = re.compile(r'`[^`\n]*`')
CODE = re.compile(r'```.*?```|`[^`\n]*`', re.S)
PLACEHOLDER = re.compile(r'⟦[BI]\d+⟧')
CYRILLIC = re.compile(r'[А-Яа-яЁё]')


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


def structure(text):
    lines = text.splitlines()
    return {
        'heading levels': [len(line) - len(line.lstrip('#')) for line in lines if re.match(r'#{1,6} ', line)],
        'table rows': sum(1 for line in lines if line.lstrip().startswith('|')),
        '<details> blocks': text.count('<details>'),
        'link targets': sorted(re.findall(r'\]\(([^)\s]+)\)', text)),
    }


def russian_left(prose):
    cyrillic = len(CYRILLIC.findall(prose))
    letters = len(re.findall(r'[A-Za-zА-Яа-яЁё]', prose))
    return cyrillic if cyrillic > 0.01 * max(letters, 1) else 0


def problems(original, translation):
    """What makes the translation unusable: a different structure, a cut or padded text, Russian left."""
    found = [f'{key} differ' for key, value in structure(original).items() if structure(translation)[key] != value]
    ratio = len(translation) / max(len(original), 1)
    if not 0.6 <= ratio <= 1.6:
        found.append(f'length ratio {ratio:.2f}')
    cyrillic = russian_left(CODE.sub('', translation))
    if cyrillic:
        found.append(f'{cyrillic} Cyrillic letters outside code')
    return found


def protect(text):
    """The text with every code block and inline code replaced by a placeholder, and the code by key."""
    codes = {}

    def keep(kind):
        def swap(m):
            key = f'⟦{kind}{len(codes)}⟧'
            codes[key] = m.group(0)
            return key
        return swap
    text = FENCE.sub(keep('B'), text)
    text = INLINE.sub(keep('I'), text)
    return text, codes


def split(text):
    """Chunks of about CHUNK characters, cut before a heading (inside a long section before a blank
    line); joined with newlines they give the text back."""
    chunks, current, size = [], [], 0
    for line in text.split('\n'):
        heading = bool(re.match(r'#{1,6} ', line))
        if current and ((heading and size + len(line) > CHUNK / 2) or (size > CHUNK and not line.strip())):
            chunks.append('\n'.join(current))
            current, size = [], 0
        current.append(line)
        size += len(line) + 1
    chunks.append('\n'.join(current))
    return chunks


def chunk_problems(original, translation):
    found = []
    if sorted(PLACEHOLDER.findall(original)) != sorted(PLACEHOLDER.findall(translation)):
        found.append('placeholders differ')
    found += [f'{key} differ' for key, value in structure(original).items() if structure(translation)[key] != value]
    ratio = len(translation) / max(len(original), 1)
    if not 0.5 <= ratio <= 1.8:
        found.append(f'length ratio {ratio:.2f}')
    cyrillic = russian_left(PLACEHOLDER.sub('', translation))
    if cyrillic:
        found.append(f'{cyrillic} Cyrillic letters left')
    return found


def translate_chunk(chunk):
    """(translation, None) or (None, why it failed)."""
    if not CYRILLIC.search(PLACEHOLDER.sub('', chunk)):
        return chunk, None   # nothing Russian in it
    lead = chunk[:len(chunk) - len(chunk.lstrip('\n'))]
    trail = chunk[len(chunk.rstrip('\n')):]
    why = None
    for _attempt in range(ATTEMPTS):
        with tempfile.TemporaryDirectory() as cwd:  # no project files for the model to pick up
            text, error = claude(['--model', MODEL, '--tools', '', '--system-prompt', PROMPT], chunk, cwd, TIMEOUT)
        if text is None:
            why = f'the model failed: {error}'
            continue
        if chunk.lstrip().startswith('#') and text.find('#') > 0:
            text = text[text.find('#'):]  # drop any preamble
        text = lead + text.strip('\n') + trail
        found = chunk_problems(chunk, text)
        if not found:
            return text, None
        why = '; '.join(found)
    return None, why


def translate(original):
    """(translation, None) or (None, why it failed)."""
    skeleton, codes = protect(original)
    chunks = split(skeleton)
    with concurrent.futures.ThreadPoolExecutor(max(1, WORKERS)) as pool:
        results = list(pool.map(translate_chunk, chunks))
    failed = [f'part {n}/{len(chunks)}: {why}' for n, (text, why) in enumerate(results, 1) if text is None]
    if failed:
        return None, '; '.join(failed)
    text = PLACEHOLDER.sub(lambda m: codes[m.group(0)], '\n'.join(text for text, _ in results))
    if sorted(CODE.findall(text)) != sorted(CODE.findall(original)):
        return None, 'code differs after the placeholders were put back'
    found = problems(original, text)
    return (None, '; '.join(found)) if found else (text, None)


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument('report')
    p.add_argument('--out', help='default: the report with .en.md')
    args = p.parse_args()
    out = args.out or os.path.splitext(args.report)[0] + '.en.md'

    with open(args.report, encoding='utf-8') as f:
        original = f.read()
    text, why = translate(original)
    if text is None:
        print(f'translation rejected: {why}', file=sys.stderr)
        return 2
    with open(out, 'w', encoding='utf-8', newline='\n') as f:
        f.write(text.rstrip() + '\n')
    print(f'translation: {out}')
    return 0


if __name__ == '__main__':
    sys.exit(main())
