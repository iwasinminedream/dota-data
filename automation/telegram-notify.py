#!/usr/bin/env python3
"""
Telegram notifications of the automatic dumps: every new update report (its «Главное» section, a
link to the full report on GitHub and the report file itself) and failures of the sync.

    telegram-notify.py report reports/6975.md [--functions reports/6975-functions.md]
    telegram-notify.py text "message"      a plain message (failures of the sync)
    telegram-notify.py chats               who has written to the bot (to find the chat id)
    telegram-notify.py test                a test message to every chat

Environment (from the dumper env file): DOTA_DATA_TG_TOKEN — the bot token from @BotFather;
DOTA_DATA_TG_CHATS — comma-separated chat ids (a user, a group or a channel the bot is in, e.g.
-1001234567890); DOTA_DATA_REPORT_URL — where reports are viewed (default: the reports/ folder on
GitHub). Without a token or a chat nothing is sent and the exit code is 4, so the sync can keep the
report queued until the bot is set up. Exit code 1: Telegram refused or could not be reached.
Only the standard library is used.
"""
import html
import json
import os
import re
import sys
import urllib.error
import urllib.request
import uuid

TOKEN = os.environ.get('DOTA_DATA_TG_TOKEN', '').strip()
CHATS = [c.strip() for c in os.environ.get('DOTA_DATA_TG_CHATS', '').split(',') if c.strip()]
REPORT_URL = os.environ.get('DOTA_DATA_REPORT_URL',
                            'https://github.com/iwasinminedream/dota-data/blob/master/reports/')
LIMIT = 4096  # Telegram's message length limit (after entity parsing)
NOT_CONFIGURED = 4


def api(method, fields=None, files=None, timeout=60):
    url = f'https://api.telegram.org/bot{TOKEN}/{method}'
    if files:
        boundary = uuid.uuid4().hex
        body = b''
        for k, v in (fields or {}).items():
            body += (f'--{boundary}\r\nContent-Disposition: form-data; name="{k}"\r\n\r\n{v}\r\n').encode()
        for k, (name, data) in files.items():
            body += (f'--{boundary}\r\nContent-Disposition: form-data; name="{k}"; filename="{name}"\r\n'
                     'Content-Type: text/markdown; charset=utf-8\r\n\r\n').encode() + data + b'\r\n'
        body += f'--{boundary}--\r\n'.encode()
        req = urllib.request.Request(url, data=body,
                                     headers={'Content-Type': f'multipart/form-data; boundary={boundary}'})
    else:
        req = urllib.request.Request(url, data=json.dumps(fields or {}).encode(),
                                     headers={'Content-Type': 'application/json'})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as res:
            return json.load(res)
    except urllib.error.HTTPError as e:
        try:
            return json.load(e)
        except ValueError:
            return {'ok': False, 'description': f'HTTP {e.code}'}
    except (urllib.error.URLError, OSError) as e:
        return {'ok': False, 'description': str(e)}


def inline(text):
    """One line of Markdown → Telegram HTML: `code`, **bold**, *italic*, [links](url)."""
    out, pos = [], 0
    for m in re.finditer(r'`([^`]+)`|\*\*(.+?)\*\*|\[([^\]]+)\]\(([^)\s]+)\)|(?<![\w*])\*([^*\n]+)\*(?!\w)', text):
        out.append(html.escape(text[pos:m.start()], quote=False))
        if m.group(1) is not None:
            out.append(f'<code>{html.escape(m.group(1), quote=False)}</code>')
        elif m.group(2) is not None:
            out.append(f'<b>{inline(m.group(2))}</b>')
        elif m.group(3) is not None:
            href = m.group(4)
            if not re.match(r'https?://', href):  # a link inside the repo: drop it, keep the text
                out.append(html.escape(m.group(3), quote=False))
            else:
                out.append(f'<a href="{html.escape(href)}">{html.escape(m.group(3), quote=False)}</a>')
        else:
            out.append(f'<i>{html.escape(m.group(5), quote=False)}</i>')
        pos = m.end()
    out.append(html.escape(text[pos:], quote=False))
    return ''.join(out)


def to_html(markdown):
    lines = []
    for line in markdown.splitlines():
        s = line.rstrip()
        if not s or s.startswith(('<details', '</details', '<summary')):
            if lines and lines[-1] != '':
                lines.append('')
            continue
        heading = re.match(r'#{1,6}\s+(.*)', s)
        if heading:
            lines.append(f'<b>{inline(heading.group(1))}</b>')
            continue
        bullet = re.match(r'(\s*)[-*+]\s+(.*)', s) or re.match(r'(\s*)\d+[.)]\s+(.*)', s)
        if bullet:
            lines.append(('  ' * (len(bullet.group(1)) // 2)) + '• ' + inline(bullet.group(2)))
        else:
            lines.append(inline(s))
    return '\n'.join(lines).strip()


def section(markdown, title):
    """The text of the ### section whose heading starts with title."""
    m = re.search(rf'^###\s+{re.escape(title)}[^\n]*\n(.*?)(?=^#{{2,3}}\s|\Z)', markdown, re.M | re.S)
    return m.group(1).strip() if m else ''


def cut(html_text, limit):
    """Shortens at a line boundary below limit (no tag is left open: tags never span lines)."""
    if len(html_text) <= limit:
        return html_text
    keep = html_text[:limit].rsplit('\n', 1)[0]
    return keep + '\n…'


def send_text(text_html, disable_preview=True):
    if not TOKEN or not CHATS:
        print('telegram: DOTA_DATA_TG_TOKEN / DOTA_DATA_TG_CHATS are not set — nothing sent', file=sys.stderr)
        return NOT_CONFIGURED
    delivered = 0
    for chat in CHATS:
        res = api('sendMessage', {'chat_id': chat, 'text': text_html, 'parse_mode': 'HTML',
                                  'link_preview_options': {'is_disabled': disable_preview}})
        if not res.get('ok'):
            # Bad markup is the likely cause: send it as plain text instead.
            plain = re.sub(r'<[^>]+>', '', text_html)
            res = api('sendMessage', {'chat_id': chat, 'text': html.unescape(plain)[:LIMIT]})
        if res.get('ok'):
            delivered += 1
        else:
            print(f"telegram: chat {chat}: {res.get('description')}", file=sys.stderr)
    # Success once any chat has it: a retry would send it again to the chats that did get it.
    return 0 if delivered else 1


def send_document(path, caption_html=''):
    rc = 0
    with open(path, 'rb') as f:
        data = f.read()
    for chat in CHATS:
        res = api('sendDocument', {'chat_id': chat, 'caption': caption_html, 'parse_mode': 'HTML'},
                  {'document': (os.path.basename(path), data)}, timeout=300)
        if not res.get('ok'):
            print(f"telegram: chat {chat}, {os.path.basename(path)}: {res.get('description')}", file=sys.stderr)
            rc = 1
    return rc


def cmd_report(path, functions=None):
    with open(path, encoding='utf-8') as f:
        markdown = f.read()
    title = (re.search(r'^#\s+(.*)', markdown, re.M) or [None, os.path.basename(path)])[1]
    url = REPORT_URL + os.path.basename(path)
    main = section(markdown, 'Главное') or section(markdown, 'Сводка')
    head = f'<b>{inline(title)}</b>\n\n'
    tail = f'\n\n<a href="{html.escape(url)}">Полный отчёт</a>'
    body = cut(to_html(main), LIMIT - len(head) - len(tail) - 50) if main else 'Раздела «Главное» в отчёте нет.'
    rc = send_text(head + body + tail)
    if rc:
        return rc
    # The message (with its link) is what counts; a file that does not go through is only logged,
    # so the report is not sent again on every run.
    send_document(path, 'Отчёт целиком')
    if functions and os.path.exists(functions) and os.path.getsize(functions) < 45 << 20:
        send_document(functions, 'Изменения кода по функциям')
    return 0


def cmd_chats():
    if not TOKEN:
        print('DOTA_DATA_TG_TOKEN is not set')
        return NOT_CONFIGURED
    me = api('getMe')
    if not me.get('ok'):
        print(f"getMe: {me.get('description')}")
        return 1
    print(f"bot: @{me['result'].get('username')}")
    res = api('getUpdates', {'allowed_updates': ['message', 'channel_post', 'my_chat_member']})
    seen = {}
    for u in res.get('result', []):
        for key in ('message', 'channel_post', 'my_chat_member'):
            chat = (u.get(key) or {}).get('chat')
            if chat:
                name = chat.get('title') or ' '.join(filter(None, (chat.get('first_name'), chat.get('last_name'))))
                seen[chat['id']] = f"{chat.get('type')}: {name} {('@' + chat['username']) if chat.get('username') else ''}"
    if not seen:
        print('nobody has written to the bot yet: send it /start (or add it to the group/channel) and run again')
    for cid, desc in seen.items():
        print(f'{cid}\t{desc}')
    return 0


def main(argv):
    if not argv:
        print(__doc__)
        return 2
    cmd = argv[0]
    if cmd == 'report' and len(argv) >= 2:
        functions = argv[argv.index('--functions') + 1] if '--functions' in argv else None
        return cmd_report(argv[1], functions)
    if cmd == 'text' and len(argv) >= 2:
        return send_text(html.escape(' '.join(argv[1:]), quote=False))
    if cmd == 'chats':
        return cmd_chats()
    if cmd == 'test':
        return send_text('<b>dota-data</b>: тестовое сообщение, бот настроен.')
    print(__doc__)
    return 2


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
