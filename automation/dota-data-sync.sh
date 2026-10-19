#!/usr/bin/env bash
#
# Keeps this repo in step with the Dota 2 build installed on the server:
#   1. snapshot the installed build's .so files (automation/so-report.py snapshot);
#   2. if dumper/dump is from an older build: npm run auto-dump (Linux headless client, see
#      dumper/linux; repeated once when the dumper asks for it), npm run build, and the
#      files-match-dump test (the schema tests need network fixtures that are gone upstream);
#   3. .so change report for the new build, summarised by Claude Haiku 4.5 -> so-changes/<version>.md;
#   4. commit "<version>" and push. Commits that could not be pushed are pushed by the next run.
# Started by dota-data-sync.path when steam.inf changes (any Dota update: the panel button or a manual
# steamcmd) and by dota-data-sync.timer as a fallback; see automation/README.md.
#
#   dota-data-sync.sh [--force]   --force: dump even if dumper/dump already is this version, and
#                                 ignore a recent failure of this version
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

FORCE=0
[[ ${1:-} == --force ]] && FORCE=1

say() { echo "dota-data-sync: $*"; }

exec 9>"$LOCK"
flock -n 9 || { say "already running"; exit 0; }

# shellcheck source=/dev/null
source "$ENV_FILE"
: "${DOTA2_DIR:?DOTA2_DIR missing in $ENV_FILE}"
APP_MANIFEST=$DOTA2_DIR/steamapps/appmanifest_570.acf

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
auto_dump() {
    local log=$STATE/auto-dump.log
    timeout 3h npm run auto-dump 2>&1 | tee "$log"
    (( PIPESTATUS[0] == 0 )) || return 1
    if grep -q 'REPEAT THE DUMP' "$log"; then
        say "the dumper changed (modifier functions) — dumping again"
        timeout 3h npm run auto-dump 2>&1 | tee "$log"
        (( PIPESTATUS[0] == 0 )) || return 1
    fi
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
    git checkout -q -- . && git clean -q -fd -- files dumper so-changes
}

DUMPED=$(inf ClientVersion dumper/dump)
FAILED_MARK=$STATE/failed-$INSTALLED
if [[ $DUMPED != "$INSTALLED" || $FORCE == 1 ]]; then
    if (( !FORCE )) && [[ -e $FAILED_MARK ]] && (( $(date +%s) - $(stat -c %Y "$FAILED_MARK") < RETRY_AFTER )); then
        say "dump of $INSTALLED failed recently ($(cat "$FAILED_MARK")) — waiting, or use --force"
    else
        say "dumping Dota $INSTALLED (repo has ${DUMPED:-nothing})"
        if [[ ! -d node_modules || package-lock.json -nt node_modules/.package-lock.json ]]; then
            npm ci --no-audit --no-fund
        fi
        step=""
        if ! { step=auto-dump && auto_dump &&
               step=version && [[ $(inf ClientVersion dumper/dump) == "$INSTALLED" ]] &&
               step=build && npm run build &&
               step=test && npx jest test/files_match_dump.spec.ts --testTimeout=600000 &&
               step=json && json_ok; }; then
            say "failed at: $step — restoring the worktree"
            echo "$(date '+%F %T') $step" >"$FAILED_MARK"
            restore
            exit 1
        fi
        rm -f "$FAILED_MARK"
        git add -A
        git commit -q -m "$INSTALLED"
        say "committed $INSTALLED: $(git show --stat --format= HEAD | tail -1)"
    fi
fi

# .so report for the installed build (needs a snapshot of the build before it).
REPORT=so-changes/$INSTALLED.md
if [[ ! -e $REPORT ]] && (( $(python3 automation/so-report.py list | wc -l) >= 2 )); then
    rc=0
    python3 automation/so-report.py latest --out-dir so-changes || rc=$?
    if (( rc == 0 )) && [[ -e $REPORT ]]; then
        git add "$REPORT"
        git commit -q -m "so-changes: $INSTALLED"
        say "committed $REPORT"
    else
        rm -f "$REPORT"
        say ".so report not committed (so-report.py exit $rc), retried next run"
    fi
fi

AHEAD=$(git rev-list --count "origin/$BRANCH..HEAD" 2>/dev/null || echo 0)
if (( AHEAD > 0 )); then
    if git push -q origin "HEAD:$BRANCH"; then
        say "pushed $AHEAD commit(s) to origin/$BRANCH"
    else
        say "push failed — $AHEAD commit(s) wait locally (deploy key with write access on GitHub?)"
        exit 3
    fi
else
    say "up to date: Dota $INSTALLED"
fi
