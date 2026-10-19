# Automatic dumps on a Linux server

Everything here runs on the Linux server that hosts the Dota 2 dedicated servers (a steamcmd install,
no GPU, no Steam client). When the installed Dota build changes it:

1. snapshots the build's `.so` files (`so-report.py snapshot`, store: `/var/lib/dota-data/so/<ClientVersion>-<SourceRevision>/`, last 3 kept);
2. runs `npm run auto-dump` (once more when the dumper reports that the modifier function list
   changed): with the Windows client and Workshop Tools under Wine after refreshing its depots with
   steamcmd — only when Steam's public build is the installed one — and with the Linux client if
   that is not possible or fails (see "Capturing on Linux" in `CLAUDE.md`). A new build is the
   ClientVersion, or the Steam buildid (`/var/lib/dota-data/dumped-build`) for a rebuild of the same
   version; such a rebuild is committed only if it changes something in `files/`;
3. dumps the same build a second time and compares the raw dumps (`dump-diff.py`): the game did not
   change in between, so any difference is dumper noise. It is written to
   `dump-checks/<version>.md` and noted in the commit message; the first dump is the one committed;
4. `npm run build` and `test/files_match_dump.spec.ts` (the schema tests download fixtures that
   no longer exist upstream and fail regardless);
5. writes `so-changes/<version>.md`: what changed in the `.so` files compared to the previous
   snapshot (sizes, code size, exports, strings from the read-only data sections and protobuf
   descriptors, strings the Metamod plugins look for that disappeared), with a summary by Claude
   Haiku 4.5 through the `claude` CLI (the Claude Code login of the server);
6. commits `<version>` (and `so-changes: <version>`) and pushes to `origin/master`; the commit body
   says which client dumped and how the control dump went.

`dota-data-sync.sh --check` dumps the installed build once more and compares it with the committed
dump without committing anything (report in `/var/lib/dota-data/checks/`): a quick way to see how
reliable the dumper is right now. `DOTA_DATA_CONTROL_DUMP=0` turns the control dump off.

## Pieces

| file | what |
| --- | --- |
| `dota-data-sync.sh` | the whole run; idempotent, safe to start any time (`--force` re-dumps, `--check` compares) |
| `dump-diff.py` | section-by-section comparison of two raw dumps |
| `so-report.py` | `snapshot`, `list`, `report OLD NEW`, `latest --out-dir so-changes` |
| `systemd/dota-data-sync.service` | runs `dota-data-sync.sh` (nice, idle IO, CPU 400 %, memory 12 G) |
| `systemd/dota-data-sync.path` | starts it when `game/dota/steam.inf` changes (panel «Обновить доту» or a manual steamcmd) |
| `systemd/dota-data-sync.timer` | hourly fallback: snapshots the installed build, retries a failed push |

`dota-data-sync.sh` waits until the update has settled (no live `/run/dota-update.active` marker, no
`steamcmd` process, `StateFlags 4` in `appmanifest_570.acf`). A version whose dump failed is retried
after 6 hours (`/var/lib/dota-data/failed-<version>`), or at once with `--force`. A dirty worktree or a
branch that diverged from `origin/master` stops it without touching anything.

## Server setup

- `/root/dota-data-runtime/dumper.env` — environment for the dumper and the commit author (`DOTA2_DIR`, `DUMPER_LAUNCH`
  pointing at `dumper/linux/headless-launch.sh`, overlay dir, Xvfb display, Steam Runtime entry point,
  the lavapipe `fakegpu` Vulkan layer in `/root/dota-data-runtime/fakegpu`, `DOTA_DATA_GIT_NAME/EMAIL`,
  and for the Wine mode `DOTA_DATA_STEAM_LOGIN`, `DUMPER_WINE_LAUNCH`, `DUMPER_WINE_GAME_DIR`,
  `DUMPER_WIN_DEPOTS`, `DUMPER_STEAMWORKS`, `DUMPER_WIN_SERVER_DLL`, `WINEPREFIX`, `DUMPER_LANGUAGE`).
  Packages: wine (64-bit), gcc-mingw-w64-x86-64, xvfb, mesa-vulkan-drivers.
- Push: a deploy key with write access, `/root/.ssh/dota-data-deploy`, used by this clone through
  `core.sshCommand`, push URL `git@github.com:iwasinminedream/dota-data.git`.
- Units: `cp automation/systemd/* /etc/systemd/system/ && systemctl daemon-reload &&
  systemctl enable --now dota-data-sync.path dota-data-sync.timer`.

Logs: `journalctl -u dota-data-sync`; the client output of the last dump is `dumper/linux/client.log`
and its console log `/var/lib/dota-data/dumper/upper/dota/console.log`.
