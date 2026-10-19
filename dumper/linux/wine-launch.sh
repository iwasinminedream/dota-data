#!/usr/bin/env bash
#
# Launcher for the dumper with the *Windows* client and Workshop Tools under Wine (set
# DUMPER_WINE_LAUNCH to this file). Unlike the Linux client this gives a real -tools dump: every
# convar, the native documentation tables, vConsole on port 29000. The dumper passes the Dota
# arguments; everything else comes from the environment:
#
#   DOTA2_DIR             Linux Dota 2 install: the shared content (VPKs) comes from here
#   DUMPER_WIN_DEPOTS     ':'-separated depot dirs, topmost first (steamcmd `download_depot 570`
#                         381450 tools, 373303 binaries, 373302 DX11 shaders), laid over DOTA2_DIR
#   DUMPER_GAME_DIR       <upper>/game: the overlay upper dir receives every write
#   DUMPER_STEAMWORKS     dir with the Windows steamclient64.dll (steamcmd `download_depot 1007
#                         1004`): the listen server's Steamworks init needs it
#   WINEPREFIX            Wine prefix, prepared here on first use
#   DUMPER_XVFB_DISPLAY   start Xvfb on this display when set
#   DUMPER_LANGUAGE       -language for the client (cl_language is part of cvarlist)
#
# Rendering goes through `-vulkan` to the host Vulkan driver (winevulkan), so software Vulkan
# (lavapipe) works the same as for the Linux client; its VK_* variables are passed through.
# Needs root (overlay mount), wine, and x86_64-w64-mingw32-gcc for the two helper DLL/EXEs.
set -euo pipefail

HERE=$(cd "$(dirname "$(readlink -f "$0")")" && pwd)
: "${DOTA2_DIR:?}" "${DUMPER_WIN_DEPOTS:?}" "${DUMPER_GAME_DIR:?}" "${DUMPER_STEAMWORKS:?}" "${WINEPREFIX:?}"
export WINEPREFIX WINEDEBUG=${WINEDEBUG:--all} WINEDLLOVERRIDES=${WINEDLLOVERRIDES:-mscoree,mshtml=}
UPPER=$(dirname "$DUMPER_GAME_DIR")
WORK=$(dirname "$UPPER")/work
MERGED=$(dirname "$UPPER")/dota2
BUILD=$HERE/.build

# --- one-time prefix setup ------------------------------------------------------------------
system32=$WINEPREFIX/drive_c/windows/system32
steam_dir=$WINEPREFIX/drive_c/Program\ Files\ \(x86\)/Steam
[[ -d $system32 ]] || wineboot -u
mkdir -p "$BUILD"
# Wine has no winsqlite3.dll (Windows 10 system DLL) and the tools' assetpreview.dll imports it.
if [[ ! -f $system32/winsqlite3.dll || $HERE/winsqlite3.c -nt $system32/winsqlite3.dll ]]; then
    x86_64-w64-mingw32-gcc -shared -O2 -o "$BUILD/winsqlite3.dll" "$HERE/winsqlite3.c"
    cp "$BUILD/winsqlite3.dll" "$system32/"
fi
if [[ ! -f $steam_dir/steamclient64.dll || $DUMPER_STEAMWORKS/steamclient64.dll -nt $steam_dir/steamclient64.dll ]]; then
    mkdir -p "$steam_dir"
    cp "$DUMPER_STEAMWORKS"/*.dll "$steam_dir/"
    wine reg add 'HKCU\Software\Valve\Steam' /v SteamPath /t REG_SZ /d 'C:\Program Files (x86)\Steam' /f >/dev/null
    wine reg add 'HKCU\Software\Valve\Steam\ActiveProcess' /v SteamClientDll64 /t REG_SZ \
        /d 'C:\Program Files (x86)\Steam\steamclient64.dll' /f >/dev/null
    wineserver -w
fi

# --- overlay: depots over the Linux install ---------------------------------------------------
mkdir -p "$UPPER/game/dota" "$UPPER/game/bin/win64" "$WORK" "$MERGED"
grep -v 'addons/metamod' "$DOTA2_DIR/game/dota/gameinfo.gi" >"$UPPER/game/dota/gameinfo.gi"
echo 570 >"$UPPER/game/bin/win64/steam_appid.txt"

xvfb_pid=
cleanup() {
    wineserver -k 2>/dev/null || true
    if [[ -n $xvfb_pid ]]; then kill "$xvfb_pid" 2>/dev/null || true; fi
}
trap cleanup EXIT
if [[ -n ${DUMPER_XVFB_DISPLAY:-} ]]; then
    n=${DUMPER_XVFB_DISPLAY#:}
    if ! { [[ -f /tmp/.X$n-lock ]] && kill -0 "$(tr -d ' ' </tmp/.X$n-lock)" 2>/dev/null; }; then
        rm -f "/tmp/.X$n-lock" "/tmp/.X11-unix/X$n"
        Xvfb "$DUMPER_XVFB_DISPLAY" -screen 0 1600x900x24 -nolisten tcp >/dev/null 2>&1 &
        xvfb_pid=$!
        for _ in $(seq 50); do [[ -e /tmp/.X11-unix/X$n ]] && break; sleep 0.1; done
    fi
    export DISPLAY=$DUMPER_XVFB_DISPLAY
fi

# shellcheck disable=SC2016
unshare -m --propagation private bash -c '
    mount -t overlay overlay -o "lowerdir=$1,upperdir=$2,workdir=$3" "$4" || exit 1
    cd "$4/game/bin/win64"; shift 4
    wine ./dota2.exe -vulkan "$@"' \
    launch "$DUMPER_WIN_DEPOTS:$DOTA2_DIR" "$UPPER" "$WORK" "$MERGED" \
    ${DUMPER_LANGUAGE:+-language "$DUMPER_LANGUAGE"} "$@"
