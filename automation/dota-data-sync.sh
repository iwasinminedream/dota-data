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
#   6. the update report reports/<version>.md: API changes from the dump and .so changes, summarised
#      by Claude Haiku 4.5 with read-only tools (update-report.py); then push. Commits that could
#      not be pushed are pushed by the next run.
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

dump_wine() { (export DUMPER_GAME_DIR=$DUMPER_WINE_GAME_DIR; dump_with_repeat); }
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
    git checkout -q -- . && git clean -q -fd -- files dumper reports dump-checks
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
               step=json && json_ok; }; then
            say "failed at: $step — restoring the worktree"
            restore
            rerun_if_updated
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

# The update report: API (the dump's changelog) and .so changes, summarised by Claude Haiku 4.5
# with read-only tools (automation/update-report.py). Retried by the next run if it fails.
REPORT_ID=${REPORT_ID:-$INSTALLED}
REPORT=reports/$REPORT_ID.md
if [[ ! -e $REPORT && -e files/changelogs/$INSTALLED.json && $(inf ClientVersion dumper/dump) == "$INSTALLED" ]]; then
    rc=0
    python3 automation/update-report.py "$REPORT_ID" --out "$REPORT" || rc=$?
    if (( rc == 0 )) && [[ -e $REPORT ]]; then
        git add "$REPORT"
        git commit -q -m "report: $REPORT_ID"
        say "committed $REPORT"
    else
        rm -f "$REPORT"
        say "update report not committed (update-report.py exit $rc), retried next run"
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

# An update that came in while this run worked (its .path trigger is lost while we are active).
rerun_if_updated
