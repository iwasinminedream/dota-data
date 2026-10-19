# Automatic dumps on a Linux server

Everything here runs on the Linux server that hosts the Dota 2 dedicated servers (a steamcmd install,
no GPU, no Steam client). When the installed Dota build changes it:

1. snapshots the build's `.so` files (`so-report.py snapshot`, store: `/var/lib/dota-data/so/<ClientVersion>-<SourceRevision>/`, last 3 kept);
2. runs `npm run auto-dump` with the Linux client (see `dumper/linux/` and the Linux section of
   `CLAUDE.md`; once more when the dumper reports that the modifier function list changed), then
   `npm run build` and `test/files_match_dump.spec.ts` (the schema tests download fixtures that
   no longer exist upstream and fail regardless);
3. writes `so-changes/<version>.md`: what changed in the `.so` files compared to the previous
   snapshot (sizes, code size, exports, strings from the read-only data sections and protobuf
   descriptors, strings the Metamod plugins look for that disappeared), with a summary by Claude
   Haiku 4.5 through the `claude` CLI (the Claude Code login of the server);
4. commits `<version>` (and `so-changes: <version>`) and pushes to `origin/master`.

## Pieces

| file | what |
| --- | --- |
| `dota-data-sync.sh` | the whole run; idempotent, safe to start any time (`--force` re-dumps) |
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
  the lavapipe `fakegpu` Vulkan layer in `/root/dota-data-runtime/fakegpu`, `DOTA_DATA_GIT_NAME/EMAIL`).
- Push: a deploy key with write access, `/root/.ssh/dota-data-deploy`, used by this clone through
  `core.sshCommand`, push URL `git@github.com:iwasinminedream/dota-data.git`.
- Units: `cp automation/systemd/* /etc/systemd/system/ && systemctl daemon-reload &&
  systemctl enable --now dota-data-sync.path dota-data-sync.timer`.

Logs: `journalctl -u dota-data-sync`; the client output of the last dump is `dumper/linux/client.log`
and its console log `/var/lib/dota-data/dumper/upper/dota/console.log`.
