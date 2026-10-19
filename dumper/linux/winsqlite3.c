/*
 * Stand-in for Windows 10's winsqlite3.dll, which Wine does not ship and the Dota 2 Workshop Tools
 * (assetpreview.dll) import. Only the 14 functions the tools use, behaving like an always-empty
 * database: opening, preparing and binding succeed, every query returns no rows, writes are
 * dropped. Enough for an asset preview cache; nothing is persisted.
 *
 * x86_64-w64-mingw32-gcc -shared -O2 -o winsqlite3.dll winsqlite3.c
 */
#include <stdlib.h>

#define SQLITE_OK 0
#define SQLITE_MISUSE 21
#define SQLITE_DONE 101

typedef struct { int unused; } sqlite3;
typedef struct { int unused; } sqlite3_stmt;

static sqlite3 the_db;
static sqlite3_stmt the_stmt;

__declspec(dllexport) int sqlite3_open_v2(const char *name, sqlite3 **db, int flags, const char *vfs) {
  (void)name; (void)flags; (void)vfs;
  if (!db) return SQLITE_MISUSE;
  *db = &the_db;
  return SQLITE_OK;
}
__declspec(dllexport) int sqlite3_close_v2(sqlite3 *db) { (void)db; return SQLITE_OK; }
__declspec(dllexport) int sqlite3_exec(sqlite3 *db, const char *sql, void *cb, void *arg, char **err) {
  (void)db; (void)sql; (void)cb; (void)arg;
  if (err) *err = NULL;
  return SQLITE_OK;
}
__declspec(dllexport) void sqlite3_free(void *p) { (void)p; }
__declspec(dllexport) int sqlite3_prepare_v2(sqlite3 *db, const char *sql, int n, sqlite3_stmt **stmt, const char **tail) {
  (void)db; (void)n;
  if (stmt) *stmt = &the_stmt;
  if (tail) { const char *end = sql; if (end) while (*end) end++; *tail = end; }
  return SQLITE_OK;
}
__declspec(dllexport) int sqlite3_bind_blob(sqlite3_stmt *s, int i, const void *v, int n, void (*d)(void *)) {
  (void)s; (void)i; (void)v; (void)n; (void)d; return SQLITE_OK;
}
__declspec(dllexport) int sqlite3_bind_int(sqlite3_stmt *s, int i, int v) { (void)s; (void)i; (void)v; return SQLITE_OK; }
__declspec(dllexport) int sqlite3_bind_text(sqlite3_stmt *s, int i, const char *v, int n, void (*d)(void *)) {
  (void)s; (void)i; (void)v; (void)n; (void)d; return SQLITE_OK;
}
__declspec(dllexport) int sqlite3_step(sqlite3_stmt *s) { (void)s; return SQLITE_DONE; }
__declspec(dllexport) const void *sqlite3_column_blob(sqlite3_stmt *s, int i) { (void)s; (void)i; return NULL; }
__declspec(dllexport) int sqlite3_column_int(sqlite3_stmt *s, int i) { (void)s; (void)i; return 0; }
__declspec(dllexport) int sqlite3_column_bytes(sqlite3_stmt *s, int i) { (void)s; (void)i; return 0; }
__declspec(dllexport) int sqlite3_finalize(sqlite3_stmt *s) { (void)s; return SQLITE_OK; }
__declspec(dllexport) int sqlite3_reset(sqlite3_stmt *s) { (void)s; return SQLITE_OK; }
