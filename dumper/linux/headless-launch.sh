#!/usr/bin/env bash
#
# Launcher for the dumper on a Linux server (set DUMPER_LAUNCH to this file). The dumper passes the
# Dota arguments; everything here is configured through the environment:
#
#   DOTA2_DIR             Dota 2 install (contains game/)                                  required
#   DUMPER_GAME_DIR       overlay upper dir over $DOTA2_DIR/game (root only): the client writes
#                         there (console.log, cfg, the dumper addon) and the install stays
#                         untouched; gameinfo.gi is copied without Metamod, which crashes a client
#   DUMPER_XVFB_DISPLAY   start Xvfb on this display (e.g. :97) and run the client windowed on it
#   STEAM_RUNTIME_ENTRY   SteamLinuxRuntime_sniper/_v2-entry-point to run the game in
#
# Software Vulkan (lavapipe) needs whatever layer/driver variables your setup uses (VK_*,
# LP_NUM_THREADS, ...); they are passed through unchanged.
set -euo pipefail

: "${DOTA2_DIR:?DOTA2_DIR is not set}"
GAME=$DOTA2_DIR/game
UPPER=${DUMPER_GAME_DIR:-}
XVFB_DISPLAY=${DUMPER_XVFB_DISPLAY:-}
RUNTIME=${STEAM_RUNTIME_ENTRY:-}

xvfb_pid=
cleanup() { if [[ -n $xvfb_pid ]]; then kill "$xvfb_pid" 2>/dev/null || true; fi; }
trap cleanup EXIT

run=("$GAME/dota.sh")
if [[ -n $XVFB_DISPLAY ]]; then
    n=${XVFB_DISPLAY#:}
    # A killed Xvfb leaves its lock and socket behind: only a live lock owner counts.
    if ! { [[ -f /tmp/.X$n-lock ]] && kill -0 "$(tr -d ' ' </tmp/.X$n-lock)" 2>/dev/null; }; then
        rm -f "/tmp/.X$n-lock" "/tmp/.X11-unix/X$n"
        Xvfb "$XVFB_DISPLAY" -screen 0 1280x720x24 -nolisten tcp >/dev/null 2>&1 &
        xvfb_pid=$!
        for _ in $(seq 50); do [[ -e /tmp/.X11-unix/X$n ]] && break; sleep 0.1; done
    fi
    export DISPLAY=$XVFB_DISPLAY
    run+=(-windowed -w 1280 -h 720)
fi
run+=("$@")
if [[ -n $RUNTIME ]]; then run=("$RUNTIME" --verb=waitforexitandrun -- "${run[@]}"); fi

if [[ -n $UPPER && $(realpath -m "$UPPER") != $(realpath -m "$GAME") ]]; then
    work=$(dirname "$UPPER")/work
    mkdir -p "$UPPER/dota" "$work"
    grep -v 'addons/metamod' "$GAME/dota/gameinfo.gi" >"$UPPER/dota/gameinfo.gi"
    # shellcheck disable=SC2016
    unshare -m --propagation private bash -c \
        'mount -t overlay overlay -o "lowerdir=$1,upperdir=$2,workdir=$3" "$1" && shift 3 && exec "$@"' \
        launch "$GAME" "$UPPER" "$work" "${run[@]}"
else
    "${run[@]}"
fi
