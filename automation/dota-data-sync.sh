#!/usr/bin/env bash
#
# Keeps this repo in step with the Dota 2 build installed on the server:
#   1. snapshot the installed build's .so files (automation/so-report.py snapshot);
#   2. if the installed build (ClientVersion, or Steam buildid for a rebuild of the same version) is
#      not the dumped one: npm run auto-dump — the Windows client with Workshop Tools under Wine
#      (its depots refreshed with steamcmd first), or the Linux client when that is not configured or
#      fails (see dumper/linux); repeated once when the dumper asks for it;
#   3. a control dump of the same build: whatever differs between the two is dumper noise, reported
#      in dump-checks/<version>.md and in the commit message;
#   4. npm run build and the files-match-dump test (the schema tests need network fixtures that are
#      gone upstream); a rebuild that changes nothing in files/ is not committed;
#   5. commit "<version>";
#   6. the update report reports/<version>.md: API changes from the dump and .so changes (strings,
#      exports and function by function, reports/<version>-functions.md), drafted and then checked
#      with read-only tools by Claude Sonnet 5.5 (update-report.py), and its English version
#      reports/<version>.en.md (translate-report.py); then push. Commits that could not be pushed are
#      pushed by the next run. Reports missing for recent versions (e.g. the claude login had expired)
#      are written later from those versions' commits (API part only once their .so snapshots are gone);
#   7. new reports go to Telegram (telegram-notify.py, queued until the bot is configured), and so do
#      failures (a dump, a report, an expired claude login), once each.
# Started by dota-data-sync.path when steam.inf changes (any Dota update: the panel button or a manual
# steamcmd) and by dota-data-sync.timer as a fallback; see automation/README.md.
#
#   dota-data-sync.sh [--force]   --force: dump even if the installed build is already dumped, and
#                                 ignore a recent failure of this version
#   dota-data-sync.sh --check     dump the installed build once and compare with the committed dump
#                                 (no commit): a report of dumper noise in $STATE/checks/
#
# Environment: DOTA_DATA_REPO (default: the repo this script is in), DOTA_DATA_ENV (dumper
# environment, /root/dota-data-runtime/dumper.env), DOTA_DATA_BRANCH (master), DOTA_DATA_STATE
# (/var/lib/dota-data). Exit codes: 0 done or nothing to do, 1 failed, 3 committed but not pushed.
set -Eeuo pipefail

HERE=$(cd "$(dirname "$(readlink -f "$0")")" && pwd)
REPO=${DOTA_DATA_REPO:-$(dirname "$HERE")}
ENV_FILE=${DOTA_DATA_ENV:-/root/dota-data-runtime/dumper.env}
BRANCH=${DOTA_DATA_BRANCH:-master}
STATE=${DOTA_DATA_STATE:-/var/lib/dota-data}
LOCK=/run/dota-data-sync.lock
UPDATE_ACTIVE=/run/dota-update.active
RETRY_AFTER=$((6 * 3600)) # a failed version is retried after this long (or with --force)

ARGS=("$@")
FORCE=0
CHECK=0
[[ ${1:-} == --force ]] && FORCE=1
[[ ${1:-} == --check ]] && CHECK=1
CONTROL=${DOTA_DATA_CONTROL_DUMP:-1} # 0: no control dump

say() { echo "dota-data-sync: $*"; }
# A Telegram message about a problem: to DOTA_DATA_TG_ADMIN_CHATS only (telegram-notify.py text).
notify() { python3 "$HERE/telegram-notify.py" text "dota-data: $*" >/dev/null 2>&1 || true; }

exec 9>"$LOCK"
flock -n 9 || { say "already running"; exit 0; }

# shellcheck source=/dev/null
source "$ENV_FILE"
: "${DOTA2_DIR:?DOTA2_DIR missing in $ENV_FILE}"
APP_MANIFEST=$DOTA2_DIR/steamapps/appmanifest_570.acf
STEAMCMD=${DOTA_DATA_STEAMCMD:-/home/steam/steamcmd/steamcmd.sh}

# Started when steam.inf changes, i.e. possibly in the middle of an update: wait until the panel's
# update/plugin check (marker with a live pid) and any steamcmd are done and the app is installed.
settled() {
    if [[ -e $UPDATE_ACTIVE ]] && kill -0 "$(cut -d' ' -f1 "$UPDATE_ACTIVE" 2>/dev/null)" 2>/dev/null; then
        return 1
    fi
    pgrep -x steamcmd >/dev/null && return 1
    grep -q '"StateFlags"[[:space:]]*"4"' "$APP_MANIFEST" 2>/dev/null
}
for _ in $(seq 360); do settled && break; sleep 10; done
settled || { say "Dota is still being updated or checked — later"; exit 0; }
export GIT_TERMINAL_PROMPT=0
# Commit identity from the env file (DOTA_DATA_GIT_NAME / DOTA_DATA_GIT_EMAIL) unless git has one.
if [[ -n ${DOTA_DATA_GIT_NAME:-} ]]; then
    export GIT_AUTHOR_NAME=$DOTA_DATA_GIT_NAME GIT_COMMITTER_NAME=$DOTA_DATA_GIT_NAME
    export GIT_AUTHOR_EMAIL=${DOTA_DATA_GIT_EMAIL:-} GIT_COMMITTER_EMAIL=${DOTA_DATA_GIT_EMAIL:-}
fi
mkdir -p "$STATE"
cd "$REPO"

inf() { grep -m1 "^$1=" "$2" | cut -d= -f2- | tr -d '\r'; }
INSTALLED=$(inf ClientVersion "$DOTA2_DIR/game/dota/steam.inf")
[[ -n $INSTALLED ]] || { say "cannot read the installed version"; exit 1; }

if [[ -n $(git status --porcelain) ]]; then
    say "worktree has local changes, not touching it:"
    git status --short | head -20
    exit 1
fi

# Bring in what was pushed from elsewhere (fast-forward only).
if git fetch -q origin "$BRANCH"; then
    if git merge-base --is-ancestor HEAD "origin/$BRANCH"; then
        git merge -q --ff-only "origin/$BRANCH"
    elif ! git merge-base --is-ancestor "origin/$BRANCH" HEAD; then
        say "local $BRANCH and origin/$BRANCH have diverged — resolve by hand"
        exit 1
    fi
else
    say "git fetch failed, continuing with the local branch"
fi

python3 automation/so-report.py snapshot || say "snapshot of the .so files failed"

# When the modifier function list changed, the dumper updates itself and asks for a second run.
dump_with_repeat() {
    local log=$STATE/auto-dump.log
    timeout 3h npm run auto-dump 2>&1 | tee "$log"
    (( PIPESTATUS[0] == 0 )) || return 1
    if grep -q 'REPEAT THE DUMP' "$log"; then
        say "the dumper changed (modifier functions) — dumping again"
        timeout 3h npm run auto-dump 2>&1 | tee "$log"
        (( PIPESTATUS[0] == 0 )) || return 1
    fi
}

# Refreshes the Windows depots of the Wine mode (dumper/linux/wine-launch.sh). Succeeds only when
# Steam's public build is the installed one: newer Windows binaries over older content would not do.
windows_depots() {
    [[ -n ${DUMPER_WINE_LAUNCH:-} ]] || return 1
    local out=$STATE/steamcmd-windows-depots.txt installed public
    installed=$(grep -m1 -oP '"buildid"\s+"\K[0-9]+' "$APP_MANIFEST")
    say "steamcmd: Windows depots for build $installed"
    if ! timeout 1h flock -n /run/dota-update.lock sudo -u steam -H "$STEAMCMD" \
        +@sSteamCmdForcePlatformType windows +login "$DOTA_DATA_STEAM_LOGIN" \
        +app_info_update 1 +app_info_print 570 \
        +download_depot 570 373302 +download_depot 570 373303 +download_depot 570 381450 \
        +download_depot 1007 1004 +quit >"$out" 2>&1; then
        say "steamcmd failed, see $out"
        return 1
    fi
    sed -i 's/\x1b\[[0-9;]*m//g' "$out"
    if (( $(grep -c 'Depot download complete' "$out") != 4 )); then
        say "steamcmd did not download all four Windows depots, see $out"
        return 1
    fi
    public=$(awk '/"branches"/{b=1} b&&/"public"/{p=1} p&&/"buildid"/{gsub(/[^0-9]/,"",$2); print $2; exit}' "$out")
    if [[ $public != "$installed" ]]; then
        say "Steam's public build is $public, installed is $installed — no Windows dump"
        return 1
    fi
}

# DOTA_SERVER_BINARY inside the dump too: the dumper ends with the native-modifier analysis of server.dll
dump_wine() { (export DUMPER_GAME_DIR=$DUMPER_WINE_GAME_DIR DOTA_SERVER_BINARY=$DUMPER_WIN_SERVER_DLL; dump_with_repeat); }
dump_linux() { (unset DUMPER_WINE_LAUNCH; dump_with_repeat); }

# Windows client with Workshop Tools under Wine (a complete -tools dump) when possible, the Linux
# client otherwise; DUMP_MODE says which. DOTA_SERVER_BINARY tells the build which server binary
# the engine enums come from.
auto_dump() {
    unset DOTA_SERVER_BINARY
    DUMP_MODE=
    if windows_depots; then
        say "dumping with the Windows client under Wine (-tools)"
        if dump_wine; then
            DUMP_MODE=wine
            export DOTA_SERVER_BINARY=$DUMPER_WIN_SERVER_DLL
            return 0
        fi
        say "the Wine dump failed — falling back to the Linux client"
    fi
    dump_linux && DUMP_MODE=linux
}

# A second dump of the same build in the same mode, compared with the first (kept in dumper/).
# Sets CONTROL_NOTE; writes the report to $1 when they differ.
control_dump() {
    local report=$1 first=$STATE/dump-first modfirst=$STATE/modifier-first
    cp dumper/dump "$first"
    cp dumper/modifier_test_output.txt "$modfirst"
    say "control dump ($DUMP_MODE)"
    if { if [[ $DUMP_MODE == wine ]]; then dump_wine; else dump_linux; fi; }; then
        cp dumper/dump "$STATE/dump-control"
        if python3 automation/dump-diff.py "$first" dumper/dump --out "$report" \
            --title "Dota $INSTALLED (build $BUILD): control dump"; then
            CONTROL_NOTE="Control dump ($DUMP_MODE): identical."
            rm -f "$report"
        else
            CONTROL_NOTE="Control dump ($DUMP_MODE) differs — dumper noise, see ${report#"$REPO"/}."
        fi
    else
        CONTROL_NOTE="Control dump ($DUMP_MODE) failed."
    fi
    cp "$first" dumper/dump
    cp "$modfirst" dumper/modifier_test_output.txt
    say "$CONTROL_NOTE"
}

# The test rewrites every files/*.json; a killed run leaves them truncated. Never commit that.
json_ok() {
    node -e '
const fs = require("fs"), path = require("path");
let bad = 0;
(function walk(d) {
  for (const e of fs.readdirSync(d, { withFileTypes: true })) {
    const p = path.join(d, e.name);
    if (e.isDirectory()) walk(p);
    else if (p.endsWith(".json")) try { JSON.parse(fs.readFileSync(p, "utf8")); } catch { bad++; console.log("invalid JSON:", p); }
  }
})("files");
process.exit(bad ? 1 : 0);'
}

restore() {
    git checkout -q -- . && git clean -q -fd -- files dumper reports dump-checks tracking
}

# Game-file tracking (tracking/: SchemaSystem, .proto, VPK index and text files; game-tracking.py) of
# the installed build, committed with the dump. Never fatal: a step that fails leaves its committed
# files as they are (each step writes to a .tmp folder first), manifest.json lists it, and we notify.
track_game() {
    local rc=0 failed
    timeout 1h python3 automation/game-tracking.py --repo "$REPO" --game "$DOTA2_DIR/game" || rc=$?
    git clean -q -fd -- tracking/*.tmp 2>/dev/null || true
    failed=$(python3 -c 'import json,sys; print(" ".join(json.load(open(sys.argv[1])).get("failed", {})))' \
        tracking/manifest.json 2>/dev/null || echo all)
    if (( rc != 0 )) || [[ -n $failed ]]; then
        say "game tracking: failed steps: ${failed:-all} (exit $rc) — their committed files are kept"
        notify "tracking/ для Dota $INSTALLED: не удались шаги ${failed:-все} (exit $rc), в коммите их прошлые файлы"
    fi
    return 0
}

BUILD=$(grep -m1 -oP '"buildid"\s+"\K[0-9]+' "$APP_MANIFEST")
BUILD_MARK=$STATE/dumped-build
DUMPED=$(inf ClientVersion dumper/dump)
[[ -s $BUILD_MARK || $DUMPED != "$INSTALLED" ]] || echo "$BUILD" >"$BUILD_MARK"
DUMPED_BUILD=$(cat "$BUILD_MARK" 2>/dev/null || true)

# Dota can be updated in the middle of a run (dota-auto-update.timer): what was dumped then is neither
# build. Start over for the new one (the new instance waits until the update has settled).
current_build() { grep -m1 -oP '"buildid"\s+"\K[0-9]+' "$APP_MANIFEST"; }
rerun_if_updated() {
    if [[ $(current_build) != "$BUILD" ]] || ! settled; then
        say "Dota changed during this run (build $BUILD -> $(current_build)) — starting over"
        exec "$0" "${ARGS[@]}"
    fi
}

if (( CHECK )); then
    mkdir -p "$STATE/checks"
    report=$STATE/checks/$INSTALLED-$(date +%Y%m%d-%H%M%S).md
    say "check: dumping build $BUILD once more and comparing with the committed dump"
    committed=$STATE/dump-committed
    git show HEAD:dumper/dump >"$committed"
    rc=0
    if auto_dump; then
        python3 automation/dump-diff.py "$committed" dumper/dump --out "$report" \
            --title "Dota $INSTALLED (build $BUILD): check ($DUMP_MODE) against the committed dump" || rc=$?
        (( rc == 0 )) && say "check: identical to the committed dump" || say "check: differs — $report"
    else
        say "check: the dump failed"
        rc=1
    fi
    restore
    exit "$rc"
fi

FAILED_MARK=$STATE/failed-$INSTALLED-$BUILD
if [[ $DUMPED != "$INSTALLED" || $DUMPED_BUILD != "$BUILD" || $FORCE == 1 ]]; then
    if (( !FORCE )) && [[ -e $FAILED_MARK ]] && (( $(date +%s) - $(stat -c %Y "$FAILED_MARK") < RETRY_AFTER )); then
        say "dump of $INSTALLED (build $BUILD) failed recently ($(cat "$FAILED_MARK")) — waiting, or use --force"
    else
        say "dumping Dota $INSTALLED build $BUILD (repo has ${DUMPED:-nothing} build ${DUMPED_BUILD:-?})"
        if [[ ! -d node_modules || package-lock.json -nt node_modules/.package-lock.json ]]; then
            npm ci --no-audit --no-fund
        fi
        CONTROL_NOTE=""
        CHECK_REPORT=$REPO/dump-checks/$INSTALLED.md
        [[ $DUMPED == "$INSTALLED" ]] && CHECK_REPORT=$REPO/dump-checks/$INSTALLED-$BUILD.md
        mkdir -p dump-checks
        step=""
        if ! { step=auto-dump && auto_dump &&
               step=install && [[ $(current_build) == "$BUILD" ]] &&
               step=version && [[ $(inf ClientVersion dumper/dump) == "$INSTALLED" ]] &&
               { (( !CONTROL )) || control_dump "$CHECK_REPORT"; } &&
               step=build && npm run build &&
               step=test && npx jest test/files_match_dump.spec.ts --testTimeout=600000 &&
               step=json && json_ok &&
               step=tracking && track_game; }; then
            say "failed at: $step — restoring the worktree"
            restore
            rerun_if_updated
            [[ -e $FAILED_MARK ]] || notify "дамп Dota $INSTALLED (build $BUILD) не удался на шаге $step; повтор через $((RETRY_AFTER / 3600)) ч"
            echo "$(date '+%F %T') $step" >"$FAILED_MARK"
            exit 1
        fi
        rm -f "$FAILED_MARK"
        rmdir dump-checks 2>/dev/null || true
        # The build reads the game's VPKs too: an update since the dump started spoils the result.
        if [[ $(current_build) != "$BUILD" ]] || ! settled; then
            restore
            rerun_if_updated
        fi
        if [[ $DUMPED == "$INSTALLED" ]] && git diff --quiet -- files && [[ -z $(git ls-files --others --exclude-standard files) ]]; then
            # Same version, new Steam build, same API: nothing worth a commit.
            say "build $BUILD changes nothing in files/ — not committed"
            restore
        else
            message=$INSTALLED
            if [[ $DUMPED == "$INSTALLED" ]]; then
                message="$INSTALLED (build $BUILD)"
                REPORT_ID=$INSTALLED-$BUILD
            fi
            how="Linux client (tools-only convars and int64 types carried over from the previous dump)"
            [[ $DUMP_MODE == wine ]] && how="Windows client with Workshop Tools under Wine"
            git add -A
            git commit -q -m "$message" -m "Dumped with: $how." ${CONTROL_NOTE:+-m "$CONTROL_NOTE"}
            say "committed $message: $(git show --stat --format= HEAD | tail -1)"
        fi
        echo "$BUILD" >"$BUILD_MARK"
    fi
fi

# The update reports (automation/update-report.py) and their English versions (translate-report.py).
# A failed one is retried after RETRY_AFTER (report-failed-<id> in $STATE) or at once with --force.
TG_QUEUE=$STATE/telegram-queue # reports waiting to be sent to Telegram (after the push)
CLAUDE_STATE=unknown
claude_ok() {
    [[ $CLAUDE_STATE == unknown ]] || { [[ $CLAUDE_STATE == ok ]]; return; }
    local out alert=$STATE/claude-login-alert
    if out=$(cd /tmp && echo 'Ответь одним словом: ok' | timeout 300 env -u CLAUDECODE -u CLAUDE_CODE_ENTRYPOINT \
        claude -p --no-session-persistence --strict-mcp-config --setting-sources local \
        --model "${REPORT_FINAL_MODEL:-claude-sonnet-5-5}" --tools '' 2>&1); then
        CLAUDE_STATE=ok
        rm -f "$alert"
        return 0
    fi
    CLAUDE_STATE=bad
    say "claude does not answer (${out:0:300}) — reports wait"
    if [[ ! -e $alert ]] || (( $(date +%s) - $(stat -c %Y "$alert") >= 86400 )); then
        notify "claude на сервере не отвечает, отчёты ждут (нужен claude /login от root?): ${out:0:300}"
        touch "$alert"
    fi
    return 1
}
retry_due() { (( FORCE )) || [[ ! -e $1 ]] || (( $(date +%s) - $(stat -c %Y "$1") >= RETRY_AFTER )); }

# make_report ID [REV]: reports/ID.md (+ -functions.md) and reports/ID.en.md, each its own commit;
# REV: the commit whose dump the report is about when it is not the worktree's.
make_report() {
    local id=$1 rev=${2:-} report=reports/$1.md functions=reports/$1-functions.md en=reports/$1.en.md
    local failed=$STATE/report-failed-$1 en_failed=$STATE/report-en-failed-$1 rc
    if [[ ! -e $report ]] && retry_due "$failed"; then
        claude_ok || return 0
        rc=0
        rm -f "$functions"
        say "writing the update report $report${rev:+ (dump of ${rev:0:7})}"
        python3 automation/update-report.py "$id" --out "$report" ${rev:+--data-rev "$rev"} || rc=$?
        if (( rc == 0 )) && [[ -e $report ]]; then
            git add "$report"
            [[ -e $functions ]] && git add "$functions"
            # The commit body: the report's «Главное», so `git log` shows what the update was about.
            git commit -q -m "report: $id" -m "$(python3 - "$report" <<'PY'
import re, sys
md = open(sys.argv[1], encoding='utf-8').read()
m = re.search(r'^###\s+Главное[^\n]*\n(.*?)(?=^#{2,3}\s|\Z)', md, re.M | re.S)
lines = [re.sub(r'[*`]', '', l).strip() for l in (m.group(1) if m else '').splitlines() if l.strip()]
print('\n'.join(l[:300] for l in lines[:12]))
PY
)"
            rm -f "$failed"
            echo "$id" >>"$TG_QUEUE"
            say "committed $report"
        else
            rm -f "$report" "$functions"
            [[ -e $failed ]] || notify "отчёт $id не написан (update-report.py exit $rc), повтор через $((RETRY_AFTER / 3600)) ч"
            date '+%F %T' >"$failed"
            say "update report not committed (update-report.py exit $rc), retried in $((RETRY_AFTER / 3600)) h or with --force"
            return 0
        fi
    fi
    if [[ -e $report && ! -e $en ]] && retry_due "$en_failed"; then
        claude_ok || return 0
        rc=0
        python3 automation/translate-report.py "$report" --out "$en" || rc=$?
        if (( rc == 0 )) && [[ -e $en ]]; then
            git add "$en"
            git commit -q -m "report: $id (English)"
            rm -f "$en_failed"
            say "committed $en"
        else
            rm -f "$en"
            date '+%F %T' >"$en_failed"
            say "English report not committed (translate-report.py exit $rc), retried in $((RETRY_AFTER / 3600)) h or with --force"
        fi
    fi
}

REPORT_ID=${REPORT_ID:-$INSTALLED}
if [[ -e files/changelogs/$INSTALLED.json && $(inf ClientVersion dumper/dump) == "$INSTALLED" ]]; then
    make_report "$REPORT_ID"
fi

# Catch-up: recent versions (bare "<version>" commits) that have a changelog but no report.
CATCH_UP=${DOTA_DATA_CATCH_UP:-10}
while read -r rev version; do
    [[ $version == "$INSTALLED" || -e reports/$version.md || ! -e files/changelogs/$version.json ]] && continue
    make_report "$version" "$rev"
done < <(git log -n 300 --format='%H %s' | awk '$2 ~ /^[0-9]+$/ && NF == 2' | head -n "$CATCH_UP" | tac)

AHEAD=$(git rev-list --count "origin/$BRANCH..HEAD" 2>/dev/null || echo 0)
if (( AHEAD > 0 )); then
    if git push -q origin "HEAD:$BRANCH"; then
        say "pushed $AHEAD commit(s) to origin/$BRANCH"
        PUSHED=1
    else
        say "push failed — $AHEAD commit(s) wait locally (deploy key with write access on GitHub?)"
        exit 3
    fi
else
    say "up to date: Dota $INSTALLED"
    PUSHED=1
fi

# New reports to Telegram once they are on GitHub (the message links there). Kept in the queue while
# the bot is not configured (exit 4) or Telegram fails.
if [[ ${PUSHED:-0} == 1 && -s $TG_QUEUE ]]; then
    left=()
    while read -r id; do
        [[ -n $id && -e reports/$id.md ]] || continue
        rc=0
        python3 "$HERE/telegram-notify.py" report "reports/$id.md" --functions "reports/$id-functions.md" || rc=$?
        if (( rc == 0 )); then say "report $id sent to Telegram"; else left+=("$id"); fi
    done < <(awk '!seen[$0]++' "$TG_QUEUE")
    printf '%s\n' "${left[@]}" | sed '/^$/d' >"$TG_QUEUE"
fi

# An update that came in while this run worked (its .path trigger is lost while we are active).
rerun_if_updated
