/*
 * LD_PRELOAD helper for running the dumper with the Linux Dota 2 client.
 *
 * 1. The Windows dumper runs Dota with -tools. Workshop Tools do not exist on Linux, and outside of
 *    tools mode libvscript.so never creates the FDesc / CDesc / EDesc documentation tables that
 *    addon_init.lua reads. Every place that asks "is the application in tools mode?" before touching
 *    those tables is a virtual call `call [rax+0xd0]` on the VApplication001 interface.
 *    dumper/linux/vscript-patch.mts finds those call sites in the on-disk libvscript.so and passes
 *    their virtual addresses in DUMPER_VSCRIPT_PATCH ("0x6623f,0x6872e,..."). When the engine
 *    dlopen()s libvscript.so, each call is replaced in memory with `mov al, 1` (the files on disk
 *    are never modified, and only the documentation checks are touched, not the engine-wide mode).
 *
 * 2. panorama_generate_layout_xsd puts ~22 MB of XSD on the clipboard. On X11 the bundled SDL3
 *    answers a selection request for that much data in one request, which fails with BadLength and
 *    kills the client. With DUMPER_CLIPBOARD_FILE set, SDL_SetClipboardText writes the text to that
 *    file instead and never takes the X selection.
 *
 * The client runs inside the Steam Linux Runtime container (glibc 2.31), so the library must not
 * depend on symbol versions newer than the container's: dlsym is bound to its GLIBC_2.2.5 version.
 *
 * Build: gcc -shared -fPIC -O2 -o dumper_hook.so dumper_hook.c -Wl,--no-as-needed -l:libdl.so.2
 */
#define _GNU_SOURCE
#include <link.h>
#include <stdbool.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/mman.h>
#include <errno.h>
#include <unistd.h>

__asm__(".symver dlsym,dlsym@GLIBC_2.2.5");
extern void *dlsym(void *handle, const char *symbol);

static const unsigned char CALL_VFUNC_D0[6] = {0xff, 0x90, 0xd0, 0x00, 0x00, 0x00};
static const unsigned char MOV_AL_1[6] = {0xb0, 0x01, 0x90, 0x90, 0x90, 0x90};

static int vscript_patched = 0;

/* strtoul is redirected to __isoc23_strtoul (GLIBC_2.38) by newer headers, so parse by hand. */
static unsigned long parse_address(const char *s) {
  unsigned long value = 0;
  if (s[0] == '0' && (s[1] == 'x' || s[1] == 'X')) s += 2;
  for (; *s; s++) {
    int digit;
    if (*s >= '0' && *s <= '9') digit = *s - '0';
    else if (*s >= 'a' && *s <= 'f') digit = *s - 'a' + 10;
    else if (*s >= 'A' && *s <= 'F') digit = *s - 'A' + 10;
    else break;
    value = value * 16 + (unsigned long)digit;
  }
  return value;
}

static void log_line(const char *fmt, const char *a, unsigned long b) {
  fprintf(stderr, "[dumper_hook] ");
  fprintf(stderr, fmt, a, b);
  fprintf(stderr, "\n");
}

static void patch_vscript(void *handle) {
  const char *list = getenv("DUMPER_VSCRIPT_PATCH");
  if (!list || !*list || vscript_patched) return;
  struct link_map *map = (struct link_map *)handle;
  long page = sysconf(_SC_PAGESIZE);
  int applied = 0, skipped = 0;

  char *copy = strdup(list);
  for (char *item = strtok(copy, ","); item; item = strtok(NULL, ",")) {
    unsigned long vaddr = parse_address(item);
    unsigned char *site = (unsigned char *)(map->l_addr + vaddr);
    if (memcmp(site, CALL_VFUNC_D0, sizeof CALL_VFUNC_D0) != 0) {
      log_line("%s 0x%lx: unexpected bytes, not patched", "libvscript.so", vaddr);
      skipped++;
      continue;
    }
    uintptr_t start = (uintptr_t)site & ~(uintptr_t)(page - 1);
    size_t len = ((uintptr_t)site + sizeof MOV_AL_1) - start;
    if (mprotect((void *)start, len, PROT_READ | PROT_WRITE | PROT_EXEC) != 0) {
      log_line("%s 0x%lx: mprotect failed", "libvscript.so", vaddr);
      skipped++;
      continue;
    }
    memcpy(site, MOV_AL_1, sizeof MOV_AL_1);
    mprotect((void *)start, len, PROT_READ | PROT_EXEC);
    applied++;
  }
  free(copy);
  vscript_patched = 1;
  log_line("%s: script documentation enabled at %lu sites", "libvscript.so", (unsigned long)applied);
  if (skipped) log_line("%s: %lu sites skipped", "libvscript.so", (unsigned long)skipped);
}

void *dlopen(const char *filename, int flags) {
  static void *(*real_dlopen)(const char *, int) = NULL;
  if (!real_dlopen) real_dlopen = (void *(*)(const char *, int))dlsym(RTLD_NEXT, "dlopen");
  void *handle = real_dlopen(filename, flags);
  if (handle && filename) {
    const char *base = strrchr(filename, '/');
    base = base ? base + 1 : filename;
    if (strcmp(base, "libvscript.so") == 0) patch_vscript(handle);
  }
  return handle;
}

bool SDL_SetClipboardText(const char *text) {
  const char *path = getenv("DUMPER_CLIPBOARD_FILE");
  if (path && *path) {
    size_t tmp_len = strlen(path) + 5;
    char *tmp = malloc(tmp_len);
    snprintf(tmp, tmp_len, "%s.tmp", path);
    FILE *f = fopen(tmp, "wb");
    if (f) {
      if (text) fwrite(text, 1, strlen(text), f);
      fclose(f);
      rename(tmp, path);
      log_line("clipboard: %s (%lu bytes)", path, (unsigned long)(text ? strlen(text) : 0));
    } else {
      log_line("clipboard: cannot write %s (errno %lu)", path, (unsigned long)errno);
    }
    free(tmp);
    return true;
  }
  static bool (*real_set)(const char *) = NULL;
  if (!real_set) real_set = (bool (*)(const char *))dlsym(RTLD_NEXT, "SDL_SetClipboardText");
  return real_set ? real_set(text) : false;
}
