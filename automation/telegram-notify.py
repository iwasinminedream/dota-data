#!/usr/bin/env python3
"""
Telegram notifications of the automatic dumps: every new update report (its «Главное» section, a
link to the full report on GitHub and the report file itself) and failures of the sync.

    telegram-notify.py report reports/6975.md [--functions reports/6975-functions.md]
    telegram-notify.py text "message"      a plain message (failures of the sync)
    telegram-notify.py chats               the bot and who gets what
    telegram-notify.py test                a test message to every report chat
    telegram-notify.py poll                the bot service (dota-data-telegram.service): /start
                                           subscribes a chat to the reports, /stop unsubscribes,
                                           /last sends the newest report; a group or channel the
                                           bot is added to is subscribed, one it leaves is not

Environment (from the dumper env file): DOTA_DATA_TG_TOKEN — the bot token from @BotFather;
DOTA_DATA_TG_CHATS — comma-separated chat ids that get the reports (a user, a group or a channel the
bot is in, e.g. -1001234567890); DOTA_DATA_TG_ADMIN_CHATS — the chats that also get failures and
other technical messages (`text`); they get the reports too, and hear about new subscribers.
Subscribers from /start live in $DOTA_DATA_STATE/telegram-subscribers.json (reports only; a chat
that blocked the bot or removed it is dropped when a send fails that way). DOTA_DATA_REPORT_URL — where reports are viewed (default: the reports/ folder on
GitHub). Without a token or a chat nothing is sent and the exit code is 4, so the sync can keep the
report queued until the bot is set up. Exit code 1: Telegram refused or could not be reached.
Only the standard library is used.
"""
import fcntl
import glob
import html
import json
import os
import re
import sys
import time
import urllib.error
import urllib.request
import uuid

TOKEN = os.environ.get('DOTA_DATA_TG_TOKEN', '').strip()
def chat_list(name):
    return [c.strip() for c in os.environ.get(name, '').split(',') if c.strip()]


ADMIN_CHATS = chat_list('DOTA_DATA_TG_ADMIN_CHATS')
STATE = os.environ.get('DOTA_DATA_STATE', '/var/lib/dota-data')
SUBSCRIBERS = os.path.join(STATE, 'telegram-subscribers.json')
OFFSET = os.path.join(STATE, 'telegram-offset')
REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GONE = re.compile(r'blocked by the user|user is deactivated|chat not found|kicked|not a member|'
                  r'have no rights to send|need administrator rights', re.I)


class Subscribers:
    """telegram-subscribers.json under a lock: {chat_id: {"name": ..., "since": ...}}."""

    def __enter__(self):
        os.makedirs(STATE, exist_ok=True)
        self.lock = open(SUBSCRIBERS + '.lock', 'w')
        fcntl.flock(self.lock, fcntl.LOCK_EX)
        try:
            with open(SUBSCRIBERS) as f:
                self.data = json.load(f)
        except (OSError, ValueError):
            self.data = {}
        self.changed = False
        return self

    def add(self, chat_id, name):
        if str(chat_id) in self.data:
            return False
        self.data[str(chat_id)] = {'name': name, 'since': time.strftime('%Y-%m-%d %H:%M')}
        self.changed = True
        return True

    def remove(self, chat_id):
        removed = self.data.pop(str(chat_id), None) is not None
        self.changed = self.changed or removed
        return removed

    def __exit__(self, *exc):
        if self.changed:
            tmp = SUBSCRIBERS + '.tmp'
            with open(tmp, 'w') as f:
                json.dump(self.data, f, ensure_ascii=False, indent=1)
            os.replace(tmp, SUBSCRIBERS)
        self.lock.close()


def report_chats():
    """Everyone who gets the reports: admins, DOTA_DATA_TG_CHATS and the /start subscribers."""
    with Subscribers() as subs:
        subscribed = list(subs.data)
    return list(dict.fromkeys(ADMIN_CHATS + chat_list('DOTA_DATA_TG_CHATS') + subscribed))


def drop_if_gone(chat, description):
    """A subscriber that blocked or removed the bot is unsubscribed (never an admin or env chat)."""
    if description and GONE.search(description) and str(chat) not in ADMIN_CHATS:
        with Subscribers() as subs:
            if subs.remove(chat):
                print(f'telegram: chat {chat} unsubscribed ({description})', file=sys.stderr)
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


DELIVERED = []  # chats the last send_text reached


def send_text(text_html, disable_preview=True, chats=None):
    chats = report_chats() if chats is None else chats
    del DELIVERED[:]
    if not TOKEN or not chats:
        print('telegram: DOTA_DATA_TG_TOKEN / chats are not set — nothing sent', file=sys.stderr)
        return NOT_CONFIGURED
    delivered = 0
    for chat in chats:
        res = api('sendMessage', {'chat_id': chat, 'text': text_html, 'parse_mode': 'HTML',
                                  'link_preview_options': {'is_disabled': disable_preview}})
        if not res.get('ok'):
            # Bad markup is the likely cause: send it as plain text instead.
            plain = re.sub(r'<[^>]+>', '', text_html)
            res = api('sendMessage', {'chat_id': chat, 'text': html.unescape(plain)[:LIMIT]})
        if res.get('ok'):
            delivered += 1
            DELIVERED.append(chat)
        else:
            print(f"telegram: chat {chat}: {res.get('description')}", file=sys.stderr)
            drop_if_gone(chat, res.get('description'))
    # Success once any chat has it: a retry would send it again to the chats that did get it.
    return 0 if delivered else 1


def send_document(path, caption_html='', chats=()):
    rc = 0
    with open(path, 'rb') as f:
        data = f.read()
    for chat in chats:
        res = api('sendDocument', {'chat_id': chat, 'caption': caption_html, 'parse_mode': 'HTML'},
                  {'document': (os.path.basename(path), data)}, timeout=300)
        if not res.get('ok'):
            print(f"telegram: chat {chat}, {os.path.basename(path)}: {res.get('description')}", file=sys.stderr)
            rc = 1
    return rc


def cmd_report(path, functions=None, chats=None):
    with open(path, encoding='utf-8') as f:
        markdown = f.read()
    title = (re.search(r'^#\s+(.*)', markdown, re.M) or [None, os.path.basename(path)])[1]
    url = REPORT_URL + os.path.basename(path)
    main = section(markdown, 'Главное') or section(markdown, 'Сводка')
    head = f'<b>{inline(title)}</b>\n\n'
    tail = f'\n\n<a href="{html.escape(url)}">Полный отчёт</a>'
    body = cut(to_html(main), LIMIT - len(head) - len(tail) - 50) if main else 'Раздела «Главное» в отчёте нет.'
    rc = send_text(head + body + tail, chats=chats)
    if rc:
        return rc
    reached = list(DELIVERED)
    # The message (with its link) is what counts; a file that does not go through is only logged,
    # so the report is not sent again on every run.
    send_document(path, 'Отчёт целиком', reached)
    if functions and os.path.exists(functions) and os.path.getsize(functions) < 45 << 20:
        send_document(functions, 'Изменения кода по функциям', reached)
    return 0


def chat_name(chat):
    name = chat.get('title') or ' '.join(filter(None, (chat.get('first_name'), chat.get('last_name'))))
    return f"{name}{' @' + chat['username'] if chat.get('username') else ''}".strip() or str(chat.get('id'))


def cmd_chats():
    if not TOKEN:
        print('DOTA_DATA_TG_TOKEN is not set')
        return NOT_CONFIGURED
    me = api('getMe')
    print(f"bot: @{me['result'].get('username')}" if me.get('ok') else f"getMe: {me.get('description')}")
    print(f"admins (reports + failures): {', '.join(ADMIN_CHATS) or '-'}")
    print(f"DOTA_DATA_TG_CHATS (reports): {', '.join(chat_list('DOTA_DATA_TG_CHATS')) or '-'}")
    with Subscribers() as subs:
        print(f'subscribers via /start (reports): {len(subs.data)}')
        for cid, info in subs.data.items():
            print(f"  {cid}\t{info.get('name')}\tsince {info.get('since')}")
    return 0


def latest_report():
    reports = [p for p in glob.glob(os.path.join(REPO, 'reports', '*.md'))
               if re.fullmatch(r'\d+(-\d+)?\.md', os.path.basename(p))]
    key = lambda p: tuple(int(x) for x in os.path.basename(p)[:-3].split('-'))
    return max(reports, key=key) if reports else None


WELCOME = ('Подписка оформлена: сюда будут приходить отчёты об обновлениях Dota 2 — что изменилось в API, '
           'коде игры и файлах (для разработчиков кастомок).\n\n/last — последний отчёт\n/stop — отписаться')
HELP = 'Отчёты об обновлениях Dota 2.\n\n/start — подписаться\n/last — последний отчёт\n/stop — отписаться'


def tell_admins(text):
    if ADMIN_CHATS:
        send_text(html.escape(text, quote=False), chats=ADMIN_CHATS)


def subscribe(chat, quiet=False):
    with Subscribers() as subs:
        new = str(chat['id']) not in ADMIN_CHATS and subs.add(chat['id'], chat_name(chat))
    if new:
        tell_admins(f"Новый подписчик на отчёты: {chat_name(chat)} ({chat.get('type')}, {chat['id']})")
    if not quiet:
        send_text(html.escape(WELCOME, quote=False), chats=[chat['id']])


def unsubscribe(chat, reply=True):
    with Subscribers() as subs:
        gone = subs.remove(chat['id'])
    if gone:
        tell_admins(f"Отписался от отчётов: {chat_name(chat)} ({chat.get('type')}, {chat['id']})")
    if reply:
        send_text('Подписка отменена. /start — подписаться снова.', chats=[chat['id']])


def handle(update):
    member = update.get('my_chat_member')
    if member:
        chat, status = member['chat'], member['new_chat_member']['status']
        if chat['type'] in ('group', 'supergroup', 'channel'):
            if status in ('member', 'administrator'):
                subscribe(chat, quiet=chat['type'] == 'channel')
            elif status in ('left', 'kicked'):
                unsubscribe(chat, reply=False)
        elif status == 'kicked':  # a user blocked the bot
            unsubscribe(chat, reply=False)
        return
    msg = update.get('message') or update.get('channel_post')
    if not msg or not msg.get('text'):
        return
    chat = msg['chat']
    command = msg['text'].split()[0].split('@')[0].lower() if msg['text'].startswith('/') else ''
    if command == '/start':
        subscribe(chat)
    elif command == '/stop':
        unsubscribe(chat)
    elif command == '/last':
        report = latest_report()
        if report:
            functions = report[:-3] + '-functions.md'
            cmd_report(report, functions if os.path.exists(functions) else None, chats=[chat['id']])
        else:
            send_text('Отчётов пока нет.', chats=[chat['id']])
    elif chat['type'] == 'private':
        send_text(html.escape(HELP, quote=False), chats=[chat['id']])


def cmd_poll():
    if not TOKEN:
        print('DOTA_DATA_TG_TOKEN is not set', file=sys.stderr)
        return NOT_CONFIGURED
    api('setMyCommands', {'commands': [{'command': 'start', 'description': 'подписаться на отчёты'},
                                       {'command': 'last', 'description': 'последний отчёт'},
                                       {'command': 'stop', 'description': 'отписаться'}]})
    try:
        offset = int(open(OFFSET).read().strip())
    except (OSError, ValueError):
        offset = 0
    print('telegram: polling', file=sys.stderr, flush=True)
    while True:
        res = api('getUpdates', {'offset': offset, 'timeout': 50,
                                 'allowed_updates': ['message', 'channel_post', 'my_chat_member']}, timeout=70)
        if not res.get('ok'):
            print(f"telegram: getUpdates: {res.get('description')}", file=sys.stderr, flush=True)
            time.sleep(15)
            continue
        for update in res['result']:
            offset = update['update_id'] + 1
            try:
                handle(update)
            except Exception as e:  # one bad update must not stop the bot
                print(f'telegram: update {update.get("update_id")}: {e!r}', file=sys.stderr, flush=True)
            with open(OFFSET, 'w') as f:
                f.write(str(offset))


def main(argv):
    if not argv:
        print(__doc__)
        return 2
    cmd = argv[0]
    if cmd == 'report' and len(argv) >= 2:
        functions = argv[argv.index('--functions') + 1] if '--functions' in argv else None
        return cmd_report(argv[1], functions)
    if cmd == 'text' and len(argv) >= 2:
        # failures and technical messages: admin chats only, never the report subscribers
        return send_text(html.escape(' '.join(argv[1:]), quote=False), chats=ADMIN_CHATS)
    if cmd == 'chats':
        return cmd_chats()
    if cmd == 'poll':
        return cmd_poll()
    if cmd == 'test':
        return send_text('<b>dota-data</b>: тестовое сообщение, бот настроен.')
    print(__doc__)
    return 2


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
