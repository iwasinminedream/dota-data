// schema-dump: dumps the SchemaSystem of the installed Dota 2 build without starting the game.
//
// Every Source 2 module exports InstallSchemaBindings(interface, ISchemaSystem*), which registers
// the module's classes and enums through ISchemaSystem::RegisterClasses / RegisterEnums. This
// program loads libschemasystem.so, puts its own functions into those two vtable slots (they record
// the arrays and call the originals), loads each module and calls its InstallSchemaBindings. Then
// it writes, per module, every class (size, alignment, base classes with offsets, fields with type,
// offset and metadata, class metadata) and every enum (size, enumerators with values, metadata) as
// JSON. Nothing of the game runs except the modules' static initialisers.
//
//   schema-dump GAME_DIR OUT_DIR [module.so ...]   (default: every module exporting InstallSchemaBindings)
//
// Layouts follow hl2sdk-dota public/schemasystem/schematypes.h. The register calls of current builds
// differ from the SDK: (self, module, project, types, schemaVersion, infos, ...) with `infos` a
// null-terminated array (observed: version 118). The hooks check the module name and every entry.
#include <dlfcn.h>
#include <sys/mman.h>
#include <unistd.h>

#include <algorithm>
#include <cinttypes>
#include <cstdint>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <map>
#include <string>
#include <vector>

struct CSchemaType { void *vtable; const char *name; };
struct Metadata { const char *name; void *data; };
struct Field { const char *name; CSchemaType *type; int offset; int metaCount; Metadata *meta; };
struct ClassInfo;
struct BaseClass { unsigned offset; ClassInfo *cls; };
struct ClassInfo {
    ClassInfo *binding; const char *name; const char *project; const char *cppName;
    int size; uint16_t fieldCount; uint16_t metaCount; uint8_t align; uint8_t baseCount;
    uint16_t miDepth; uint16_t siDepth;
    Field *fields; BaseClass *bases; void *datamap; Metadata *meta;
    void *scope; void *declared; uint32_t flags1; uint32_t flags2; void *manip;
};
struct Enumerator { const char *name; int64_t value; int metaCount; Metadata *meta; };
struct EnumInfo {
    EnumInfo *binding; const char *name; const char *project;
    uint8_t size; uint8_t align; uint8_t flags; uint16_t count; uint16_t metaCount;
    Enumerator *enumerators; Metadata *meta; void *scope; int64_t minValue, maxValue;
};
static_assert(sizeof(ClassInfo) == 112 && sizeof(Field) == 32 && sizeof(EnumInfo) == 72 && sizeof(Enumerator) == 32,
              "layout differs from hl2sdk-dota");

// ISchemaSystem vtable slots (hl2sdk-dota: RegisterAtomics 32, RegisterEnums 33, RegisterClasses 34).
static int SLOT_ENUMS = 33, SLOT_CLASSES = 34;

typedef void *(*RegisterFn)(void *, const char *, const char *, void *, intptr_t, void **, void *, void *);
static RegisterFn g_origEnums, g_origClasses;
static intptr_t g_schemaVersion = -1;

struct Module { std::vector<ClassInfo *> classes; std::vector<EnumInfo *> enums; std::string project; };
static std::map<std::string, Module> g_modules;
static int g_badCalls, g_skipped;

// Readable memory ranges, so metadata values of unknown type can be probed without crashing.
static std::vector<std::pair<uintptr_t, uintptr_t>> g_readable;
static void load_maps() {
    g_readable.clear();
    FILE *f = fopen("/proc/self/maps", "r");
    char line[512];
    while (f && fgets(line, sizeof line, f)) {
        uintptr_t a, b; char perm[5];
        if (sscanf(line, "%" SCNxPTR "-%" SCNxPTR " %4s", &a, &b, perm) == 3 && perm[0] == 'r') g_readable.push_back({a, b});
    }
    if (f) fclose(f);
}
static bool readable(const void *p, size_t n) {
    uintptr_t a = (uintptr_t)p;
    for (auto &r : g_readable) if (a >= r.first && a + n <= r.second) return true;
    return false;
}
static bool plausible_name(const char *s) {
    if (!s || !readable(s, 1)) return false;
    for (int i = 0; i < 512; i++) {
        if (!readable(s + i, 1)) return false;
        unsigned char c = s[i];
        if (!c) return i > 0;
        if (c < 0x20 || c > 0x7e) return false;
    }
    return false;
}

template <class T> static void record(const char *module, const char *project, intptr_t version, void **infos,
                                      std::vector<T *> Module::*list) {
    load_maps();
    if (!plausible_name(module) || !infos) { g_badCalls++; return; }
    Module &m = g_modules[module];
    if (project && plausible_name(project) && m.project.empty()) m.project = project;
    g_schemaVersion = version;
    for (int i = 0; i < 200000 && readable(infos + i, 8) && infos[i]; i++) {
        T *info = (T *)infos[i];
        if (readable(info, sizeof(T)) && plausible_name(info->name)) (m.*list).push_back(info);
        else g_skipped++;
    }
}
static void *hookEnums(void *self, const char *module, const char *project, void *types, intptr_t version, void **infos, void *a, void *b) {
    record<EnumInfo>(module, project, version, infos, &Module::enums);
    return g_origEnums(self, module, project, types, version, infos, a, b);
}
static void *hookClasses(void *self, const char *module, const char *project, void *types, intptr_t version, void **infos, void *a, void *b) {
    record<ClassInfo>(module, project, version, infos, &Module::classes);
    return g_origClasses(self, module, project, types, version, infos, a, b);
}

// --- JSON ----------------------------------------------------------------------------------------
static void jstr(std::string &o, const char *s) {
    o += '"';
    for (; s && *s; s++) {
        unsigned char c = *s;
        if (c == '"' || c == '\\') { o += '\\'; o += c; }
        else if (c < 0x20) { char b[8]; snprintf(b, sizeof b, "\\u%04x", c); o += b; }
        else o += c;
    }
    o += '"';
}

// A metadata value: a string when the data is a pointer to a C string (MNetworkVarNames,
// MPropertyFriendlyName, ...), else nothing — its type is not described anywhere.
static void jmeta(std::string &o, int n, Metadata *meta) {
    o += '[';
    std::vector<std::pair<std::string, std::string>> items;
    for (int i = 0; meta && i < n; i++) {
        if (!plausible_name(meta[i].name)) continue;
        std::string value;
        void *d = meta[i].data;
        if (d && readable(d, sizeof(char *))) {
            const char *s = *(const char **)d;
            if (plausible_name(s)) value = s;
        }
        items.push_back({meta[i].name, value});
    }
    bool first = true;
    for (auto &it : items) {
        if (!first) o += ',';
        first = false;
        o += "{\"name\":"; jstr(o, it.first.c_str());
        if (!it.second.empty()) { o += ",\"value\":"; jstr(o, it.second.c_str()); }
        o += '}';
    }
    o += ']';
}

static const char *type_name(CSchemaType *t) {
    return (t && readable(t, sizeof *t) && plausible_name(t->name)) ? t->name : "?";
}

static std::string dump_module(const std::string &name, Module &m) {
    auto byName = [](auto *a, auto *b) { return strcmp(a->name ? a->name : "", b->name ? b->name : "") < 0; };
    std::sort(m.classes.begin(), m.classes.end(), byName);
    std::sort(m.enums.begin(), m.enums.end(), byName);
    m.classes.erase(std::unique(m.classes.begin(), m.classes.end()), m.classes.end());
    m.enums.erase(std::unique(m.enums.begin(), m.enums.end()), m.enums.end());
    std::string o = "{\"module\":";
    jstr(o, name.c_str());
    o += ",\"project\":"; jstr(o, m.project.c_str());
    { char b[48]; snprintf(b, sizeof b, ",\"schema_version\":%ld", (long)g_schemaVersion); o += b; }
    o += ",\"classes\":[\n";
    bool firstc = true;
    for (ClassInfo *c : m.classes) {
        if (!readable(c, sizeof *c) || !plausible_name(c->name)) continue;
        if (!firstc) o += ",\n";
        firstc = false;
        o += "{\"name\":"; jstr(o, c->name);
        char b[160];
        snprintf(b, sizeof b, ",\"size\":%d,\"align\":%u,\"flags\":[%u,%u]", c->size, c->align, c->flags1, c->flags2);
        o += b;
        o += ",\"bases\":[";
        for (int i = 0; i < c->baseCount && c->bases && readable(c->bases + i, sizeof(BaseClass)); i++) {
            if (i) o += ',';
            ClassInfo *bc = c->bases[i].cls;
            o += "{\"name\":"; jstr(o, bc && readable(bc, sizeof *bc) && plausible_name(bc->name) ? bc->name : "?");
            snprintf(b, sizeof b, ",\"offset\":%u}", c->bases[i].offset);
            o += b;
        }
        o += "],\"metadata\":"; jmeta(o, c->metaCount, c->meta);
        o += ",\"fields\":[";
        for (int i = 0; i < c->fieldCount && c->fields && readable(c->fields + i, sizeof(Field)); i++) {
            Field &f = c->fields[i];
            if (i) o += ',';
            o += "\n {\"name\":"; jstr(o, plausible_name(f.name) ? f.name : "?");
            o += ",\"type\":"; jstr(o, type_name(f.type));
            snprintf(b, sizeof b, ",\"offset\":%d,\"metadata\":", f.offset);
            o += b;
            jmeta(o, f.metaCount, f.meta);
            o += '}';
        }
        o += "]}";
    }
    o += "\n],\"enums\":[\n";
    bool firste = true;
    for (EnumInfo *e : m.enums) {
        if (!readable(e, sizeof *e) || !plausible_name(e->name)) continue;
        if (!firste) o += ",\n";
        firste = false;
        o += "{\"name\":"; jstr(o, e->name);
        char b[96];
        snprintf(b, sizeof b, ",\"size\":%u,\"metadata\":", e->size);
        o += b;
        jmeta(o, e->metaCount, e->meta);
        o += ",\"enumerators\":[";
        for (int i = 0; i < e->count && e->enumerators && readable(e->enumerators + i, sizeof(Enumerator)); i++) {
            Enumerator &v = e->enumerators[i];
            if (i) o += ',';
            o += "{\"name\":"; jstr(o, plausible_name(v.name) ? v.name : "?");
            snprintf(b, sizeof b, ",\"value\":%" PRId64 ",\"metadata\":", v.value);
            o += b;
            jmeta(o, v.metaCount, v.meta);
            o += '}';
        }
        o += "]}";
    }
    o += "\n]}\n";
    return o;
}

static bool patch_slot(void **vtable, int slot, void *fn, void **orig) {
    void **p = vtable + slot;
    long page = sysconf(_SC_PAGESIZE);
    uintptr_t start = (uintptr_t)p & ~(uintptr_t)(page - 1);
    if (mprotect((void *)start, page * 2, PROT_READ | PROT_WRITE)) return false;
    *orig = *p;
    *p = fn;
    return true;
}

int main(int argc, char **argv) {
    if (argc < 3) {
        fprintf(stderr, "usage: %s GAME_DIR OUT_DIR [module.so ...]\n", argv[0]);
        return 2;
    }
    std::string game = argv[1], out = argv[2];
    std::string bin = game + "/bin/linuxsteamrt64/", dotaBin = game + "/dota/bin/linuxsteamrt64/";
    if (!dlopen((bin + "libtier0.so").c_str(), RTLD_NOW | RTLD_GLOBAL)) { fprintf(stderr, "%s\n", dlerror()); return 1; }
    void *ss = dlopen((bin + "libschemasystem.so").c_str(), RTLD_NOW | RTLD_GLOBAL);
    if (!ss) { fprintf(stderr, "%s\n", dlerror()); return 1; }
    auto create = (void *(*)(const char *, int *))dlsym(ss, "CreateInterface");
    void *schema = create ? create("SchemaSystem_001", nullptr) : nullptr;
    if (!schema) { fprintf(stderr, "no SchemaSystem_001\n"); return 1; }
    if (getenv("SCHEMA_SLOT_ENUMS")) SLOT_ENUMS = atoi(getenv("SCHEMA_SLOT_ENUMS"));
    if (getenv("SCHEMA_SLOT_CLASSES")) SLOT_CLASSES = atoi(getenv("SCHEMA_SLOT_CLASSES"));
    void **vtable = *(void ***)schema;
    if (!patch_slot(vtable, SLOT_ENUMS, (void *)hookEnums, (void **)&g_origEnums) ||
        !patch_slot(vtable, SLOT_CLASSES, (void *)hookClasses, (void **)&g_origClasses)) {
        perror("mprotect");
        return 1;
    }

    std::vector<std::string> modules;
    for (int i = 3; i < argc; i++) modules.push_back(argv[i]);
    if (modules.empty()) {
        // Engine modules first (others' schemas refer to their types), the game's two last.
        const char *defaults[] = {"libschemasystem.so", "libtier0.so", "libengine2.so", "libanimationsystem.so",
                                  "libmaterialsystem2.so", "libmeshsystem.so", "libnetworksystem.so", "libparticles.so",
                                  "libpulse_system.so", "libresourcesystem.so", "libscenefilecache.so", "libscenesystem.so",
                                  "libsoundsystem.so", "libvphysics2.so", "libworldrenderer.so", "librendersystemvulkan.so",
                                  "libpanorama.so", "libinputsystem.so", "libv8system.so", "libvscript.so",
                                  "dota:libserver.so", "dota:libclient.so"};
        modules.assign(std::begin(defaults), std::end(defaults));
    }
    int installed = 0;
    for (auto &spec : modules) {
        bool dota = spec.rfind("dota:", 0) == 0;
        std::string file = dota ? spec.substr(5) : spec;
        std::string path = (dota ? dotaBin : bin) + file;
        if (access(path.c_str(), R_OK)) { fprintf(stderr, "%s: missing\n", file.c_str()); continue; }
        void *h = dlopen(path.c_str(), RTLD_NOW | RTLD_GLOBAL);
        if (!h) { fprintf(stderr, "%s: %s\n", file.c_str(), dlerror()); continue; }
        auto install = (bool (*)(const char *, void *))dlsym(h, "InstallSchemaBindings");
        if (!install) { fprintf(stderr, "%s: no InstallSchemaBindings\n", file.c_str()); continue; }
        size_t before = g_modules.size();
        bool ok = install("SchemaSystem_001", schema);
        fprintf(stderr, "%s: InstallSchemaBindings -> %d (%zu module scope(s) so far)\n", file.c_str(), ok, g_modules.size());
        installed += ok;
        (void)before;
    }
    if (g_skipped) fprintf(stderr, "note: %d registered entries without a readable name skipped\n", g_skipped);
    if (g_badCalls) fprintf(stderr, "warning: %d register calls with implausible arguments (vtable slots wrong?)\n", g_badCalls);
    size_t classes = 0, enums = 0;
    for (auto &kv : g_modules) {
        std::string json = dump_module(kv.first, kv.second);
        std::string file = out + "/" + kv.first + ".json";
        FILE *f = fopen(file.c_str(), "w");
        if (!f) { perror(file.c_str()); return 1; }
        fwrite(json.data(), 1, json.size(), f);
        fclose(f);
        classes += kv.second.classes.size();
        enums += kv.second.enums.size();
        fprintf(stderr, "%s: %zu classes, %zu enums\n", kv.first.c_str(), kv.second.classes.size(), kv.second.enums.size());
    }
    if (classes == 0) { fprintf(stderr, "no classes recorded — the vtable slots are probably wrong\n"); return 1; }
    fprintf(stderr, "total: %zu classes, %zu enums in %zu modules\n", classes, enums, g_modules.size());
    fflush(stderr);
    _exit(0);  // the modules' static destructors expect an engine that never ran
}
