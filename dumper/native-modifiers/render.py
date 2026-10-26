"""From executor paths to formulas: field substitution, names, simplification and text.

Text syntax (Lua-like pseudo-code):
    %name%                  special value `name` of the modifier's ability (GetSpecialValueFor)
    kv.name                 creation parameter `name` of the modifier (the table passed to AddNewModifier)
    self / caster / parent / ability
                            the modifier, its caster, its parent, its ability
    obj:Method(args)        a call of a script method (named after the Lua binding with the same code)
    state(obj, NAME)        obj currently has the modifier state MODIFIER_STATE_NAME
    params.name             a field of the params table the engine passes to the modifier function
    self.field_XXXX         a field of the modifier that the game changes over time (see "fields")
    cond ? a : b, and, or, not, comparisons, + - * /
    ?                       a part the analysis could not follow (status "partial")
"""
import math
import re

from expr import C, F, FALSE, TRUE, ZERO, addr, base_off, bits_to_f32, fval, ite, lnot, signed, substitute, walk
from knowledge import GLOBAL_CLASSES, strip_script_handle
from modifiers import OUT, PARAMS, THIS

STATIC_WRITERS = ("OnCreated", "OnRefresh")
KV_GET = re.compile(r"^import:\?(?:Internal_)?Get(Int|Float|Bool|String|Uint64|Ptr)@")
KV_FIND = "import:?FindKey@KeyValues@@"


def fmt_num(v):
    if isinstance(v, int):
        return str(v)
    if math.isnan(v) or math.isinf(v):
        return "inf" if v > 0 else "-inf" if v < 0 else "nan"
    if v == int(v) and abs(v) < 1e15:
        return str(int(v))
    s = "%.6g" % v
    return s


class Renderer:
    def __init__(self, kb, functions, states, fields_from, enums=None):
        """fields_from: where the fields of derived classes start (after the handler table);
        enums: files/vscripts/enums.json (optional): names for flags and values of known enums."""
        self.fields_from = fields_from
        self.enum_members = {}
        for en in enums or []:
            if isinstance(en, dict) and en.get("members"):
                self.enum_members[en["name"]] = {m["value"]: m["name"] for m in en["members"]
                                                 if isinstance(m.get("value"), int)}
        self.kb = kb
        self.functions = functions
        self.states = states
        self.counts = {}
        self.expanding = set()
        self.unknown = {}
        self.examples = {}
        self.cur = None
        self.static, self.dynamic = {}, {}
        # handle fields of CDOTA_Buff: GetCaster / GetParent / GetAbility / GetAuraOwner
        self.handles = {}
        for k, lst in kb.templates.items():
            for size, cname, mname, t, nargs in lst:
                if cname == "CDOTA_Buff" and t[0] == 'ent' and t[1][0] == 'ld':
                    b, o = base_off(t[1][1])
                    if b == ('sym', 'obj'):
                        self.handles[o] = {"GetCaster": "caster", "GetParent": "parent", "GetAbility": "ability",
                                           "GetAuraOwner": "aura_owner"}.get(mname, mname)
        # the modifier-state bits of an NPC: the field IsRooted (state 0) tests. client.dll keeps two masks
        # (the server's and the states it predicts) and tests a state in their union:
        #     (ld(npc + A, 1) | ld(npc + B, 1)) & 1
        self.state_field = None
        self.state_other = None
        for k, lst in kb.templates.items():
            for size, cname, mname, t, nargs in lst:
                if cname != "CDOTA_BaseNPC" or mname != "IsRooted":
                    continue
                if t[0] == 'bit' and t[2] == 0:
                    self.state_field = base_off(t[1][1])[1]
                x = t[2][2] if t[0] == 'op' and t[1] == 'and' and t[3] == C(1) and t[2][0] == 'un' else None
                if x is not None and x[0] == 'op' and x[1] == 'or' and x[2][0] == 'ld' and x[3][0] == 'ld':
                    (b1, o1), (b2, o2) = base_off(x[2][1]), base_off(x[3][1])
                    if b1 == b2 == ('sym', 'obj') and abs(o1 - o2) >= 8:
                        self.state_field, self.state_other = min(o1, o2), max(o1, o2)

    def summary(self):
        return ", ".join("%s %d" % kv for kv in sorted(self.counts.items()))

    # --- one modifier
    def modifier(self, name, cname, bases, declared, handlers, writers, lua_names):
        self.cur = name
        fields = self.field_values(writers)
        static = {}
        dynamic = {}
        for off, by in fields.items():
            vals = set()
            for v in by.values():
                vals |= set(v[1]) if v[0] == 'any' else {v}
            # zero is the initial value of a field that is set to something else elsewhere
            nonzero = {v for v in vals if v not in (ZERO, ('f', 0.0))}
            cands = nonzero or vals
            if len(cands) == 1 and not refs_fields(next(iter(cands)), self.fields_from):
                static[off] = next(iter(cands))
            else:
                dynamic[off] = by
        self.static, self.dynamic = static, dynamic
        out = {
            "class": cname[4:-2] if cname.startswith(".?AV") else cname,
            "bases": [b[4:-2] for b in bases[1:] if b.startswith(".?AV")
                      and b not in (".?AVCDOTA_Buff@@", ".?AVCMemZeroOnNew@@")
                      and "MotionController" not in b],
            "functions": [],
        }
        used_fields = set()
        for P, (h, done, aborted) in sorted(handlers.items()):
            fname = self.functions.get(P, "MODIFIER_FUNCTION_%d" % P)
            item = {"function": fname}
            if lua_names.get(P):
                item["handler"] = lua_names[P]
            if fname.startswith("MODIFIER_EVENT_"):
                item["status"] = "event"
                out["functions"].append(item)
                self.counts["event"] = self.counts.get("event", 0) + 1
                continue
            value = self.handler_value(done)
            if value is None:
                item["status"] = "unresolved"
                item["reason"] = sorted(set(a.split(" at ")[0] for a in aborted))[:3] or ["no path"]
            else:
                e = self.finish(value)
                text = self.text(e)
                item["formula"] = text
                item["status"] = self.status(e, aborted)
                specials = sorted({x[1] for x in walk(e) if x[0] == 'special'})
                if specials:
                    item["specials"] = specials
                kv = sorted({x[1] for x in walk(e) if x[0] == 'kv'})
                if kv:
                    item["kv"] = kv
                used_fields |= {x[1] for x in walk(e) if x[0] == 'field'}
            self.counts[item["status"]] = self.counts.get(item["status"], 0) + 1
            out["functions"].append(item)
        # the fields formulas still name (changed over time, or never set by the modifier itself): who sets them
        writes = {}
        for off in sorted(used_fields):
            by = fields.get(off, {})
            if by:
                writes["field_%x" % off] = [{"in": label, "value": self.text(self.finish(v))}
                                            for label, v in sorted(by.items())]
        if writes:
            out["fields"] = writes
        return out

    def field_values(self, writers):
        """{field offset: {writer label: value expression}} (('keep',) = the field stays unchanged)."""
        out = {}
        for label, paths in writers:
            offs = set()
            for conds, fields in paths:
                offs |= set(fields)
            for off in offs:
                vals = [(conds, fields[off][1] if off in fields else ('keep',)) for conds, fields in paths]
                from modifiers import decision
                v = decision(vals)
                v = drop_keep(v)
                if v is None:
                    continue
                if label in out.get(off, {}) and out[off][label] != v:
                    v = ('any', (out[off][label], v))
                out.setdefault(off, {})[label] = v
        return out

    # --- CheckState
    def check_states(self, done):
        """[{"state", "value", "when"?}] from the paths of a CheckState override: per modifier state, whether
        the modifier sets it true or false, and under which condition when that depends on something."""
        from modifiers import decision, STATES, STATES_ON, STATES_OFF
        out = []
        masks = []
        for s in done:
            on = load(s, STATES, 0, 8)
            off = load(s, STATES, 8, 8)
            masks.append((s.conds, on if on != ('unset',) else STATES_ON, off if off != ('unset',) else STATES_OFF))
        for k, name in sorted(self.states.items()):
            if not 0 <= k < 64 or name.endswith("_LAST"):
                continue
            paths = []
            for conds, on, off in masks:
                paths.append((conds, state_value(bit_of(on, k, STATES_ON), bit_of(off, k, STATES_OFF))))
            tree = decision(paths)
            if tree is None or tree == ST_UNSET:
                continue
            for target, value in ((ST_ON, True), (ST_OFF, False)):
                when = when_of(tree, target)
                if when == FALSE:
                    continue
                item = {"state": name, "value": value}
                if when != TRUE:
                    item["when"] = self.text(self.finish(when))
                out.append(item)
            if when_of(tree, ST_UNKNOWN) != FALSE:
                out.append({"state": name, "value": None, "when": "?"})
        known = [x for x in out if x["value"] is not None]
        if not known and out:
            return None         # the masks come from data the analysis cannot read (e.g. a KV table)
        return out

    def handler_value(self, done):
        paths = []
        for s in done:
            kind = load(s, OUT, 0, 4)
            if kind == C(1):
                v = load(s, OUT, 4, 4)
            elif kind == C(2):
                p = load(s, OUT, 8, 8)
                v = ('str', p)
            elif kind == ZERO:
                v = ('none',)
            else:
                v = ('kind', kind, load(s, OUT, 4, 4))
            paths.append((s.conds, v))
        # a path that left the result unwritten (it went through a call the analysis did not follow)
        written = [p for p in paths if not (p[1][0] == 'kind' and p[1][1] == ('unset',))]
        paths = written or paths
        if not paths:
            return None
        from modifiers import decision
        return decision(paths)

    # --- naming and simplification
    def finish(self, e):
        e = self.as_float(e)
        if self.state_other is not None:
            e = substitute(e, self.merge_state_masks)
        for _ in range(3):
            e2 = substitute(e, self.rename)
            e2 = substitute(e2, self.simplify)
            if e2 == e:
                break
            e = e2
        return e

    def merge_state_masks(self, e):
        """(the same read of both state masks) | ... -> the read of the first one (client.dll)."""
        if e[0] == 'op' and e[1] == 'or':
            a, b = e[2], e[3]
            for p, q in ((a, b), (b, a)):
                if q != p and self.shift_masks(q) == p:
                    return substitute(p, self.merge_state_masks)
        return None

    def shift_masks(self, e):
        def fn(x):
            if x[0] == 'ld':
                b, o = base_off(x[1])
                if b is not None and self.state_other <= o < self.state_other + 8:
                    return ('ld', addr(b, o - self.state_other + self.state_field), x[2])
            return None
        return substitute(e, fn)

    def as_float(self, e):
        """A value in float context (the result, operands of float arithmetic): integer constants there
        are float bits."""
        if e[0] == 'c':
            return ('num', bits_to_f32(e[1]))
        if e[0] == 'ite':
            return ('ite', e[1], self.as_float(e[2]), self.as_float(e[3]))
        if e[0] == 'any':
            return ('any', tuple(self.as_float(x) for x in e[1]))
        if e[0] == 'kv' and len(e) == 3:
            return ('kv', e[1], self.as_float(e[2]))
        return e

    def string(self, e):
        """The string an expression points at (a constant address in the image), else None."""
        if e[0] == 'c':
            return self.kb.im.text(e[1] - self.kb.im.base, 200)
        if e[0] == 's':
            return e[1]
        return None

    def kind_of(self, obj):
        if obj == THIS or (obj[0] == 'op' and obj[2] == THIS):
            return 'modifier'
        if obj[0] == 'var':
            return {'caster': 'npc', 'parent': 'npc', 'ability': 'ability', 'aura_owner': 'npc',
                    'self': 'modifier'}.get(obj[1], 'any')
        if obj[0] == 'param':
            return self.kb.param_kinds.get(obj[1], 'any')
        if obj[0] == 'ent':
            h = obj[1]
            if h[0] == 'ld':
                b, o = base_off(h[1])
                if b == THIS and o in self.handles:
                    return {'caster': 'npc', 'parent': 'npc', 'ability': 'ability'}.get(self.handles[o], 'any')
                if b == PARAMS and ('ent', o) in self.kb.params:
                    return self.kb.param_kinds.get(self.kb.params[('ent', o)], 'any')
        if obj[0] == 'call' and obj[1] == 'FindModifierByName':
            return 'modifier'
        if obj[0] == 'm':
            return {'GetCaster': 'npc', 'GetParent': 'npc', 'GetAbility': 'ability', 'GetOwner': 'npc',
                    'FindModifierByName': 'modifier', 'FindAbilityByName': 'ability',
                    'GetOwnerEntity': 'npc', 'GetAttackTarget': 'npc', 'GetCursorCastTarget': 'npc'}.get(obj[1], 'any')
        return 'any'

    def rename(self, e):
        t = e[0]
        if t in ('num', 'special', 'kv', 'kvhas', 'var', 'm', 'field', 'param', 'state', 's', 'str'):
            return e
        if t == 'ent':
            h = e[1]
            if h[0] == 'ld':
                b, o = base_off(h[1])
                if b == THIS and o in self.handles:
                    return ('var', self.handles[o])
                if b == PARAMS and ('ent', o) in self.kb.params:
                    return ('param', self.kb.params[('ent', o)])
        if t == 'call' and isinstance(e[1], tuple) and e[1][0] == 'vcall':
            obj, slot = e[1][1], e[1][2]
            if obj == THIS:
                return None
            name = self.kb.vslot_name(self.kind_of(obj), slot)
            if name is not None:
                args = tuple(a for a in e[2][1:] if a[0] not in ('sym',))
                return ('m', name, substitute(obj, self.rename), ())
        if e == THIS:
            return ('var', 'self')
        if t == 'call' and e[1] == 'special':
            ability, name, level = e[2]
            ability = substitute(ability, self.rename)
            nm = name[1] if name[0] == 's' else None
            if nm is not None:
                if ability == ('var', 'ability') and (level == C(0xFFFFFFFF) or level == C(-1)):
                    return ('special', nm)
                return ('special', nm, ability, substitute(level, self.rename))
        if t == 'call' and isinstance(e[1], str) and KV_GET.match(e[1]):
            # KeyValues: Internal_GetX(FindKey(kv, name)) or GetX(kv, name, default)
            inner = e[2][0]
            key = None
            if inner[0] == 'call' and isinstance(inner[1], str) and inner[1].startswith(KV_FIND):
                key = self.string(inner[2][1])
            elif "@KeyValues@@" in e[1]:
                key = self.string(e[2][1])
            if key:
                return ('kv', key)
        if t == 'call' and isinstance(e[1], str) and e[1].startswith(KV_FIND):
            key = self.string(e[2][1])
            if key:
                return ('kvhas', key)
        if t == 'call' and e[1] == 'FindModifierByName':
            s = self.string(e[2][1])
            if s:
                return ('m', 'FindModifierByName', substitute(e[2][0], self.rename), (('s', s),))
        if t == 'call' and isinstance(e[1], str) and e[2] and self.kb.modifier_manager is not None:
            # a lookup in an NPC's modifier manager by a modifier name: FindModifierByName
            b, o = base_off(e[2][0])
            if b is not None and o == self.kb.modifier_manager:
                for a in e[2][1:]:
                    s = self.string(a)
                    if s and s.startswith("modifier_"):
                        return ('m', 'FindModifierByName', substitute(b, self.rename), (('s', s),))
        if t == 'ld':
            b, o = base_off(e[1])
            if b == THIS:
                if o >= self.fields_from:
                    if o in self.static and o not in self.expanding:
                        v = self.static[o]
                        if size_ok(v):
                            self.expanding.add(o)
                            try:
                                return substitute(v, self.rename)
                            finally:
                                self.expanding.discard(o)
                    return ('field', o)
            if b == PARAMS:
                key = self.kb.params.get((o, e[2]))
                if key is None:
                    key = next((k for (po, ps), k in self.kb.params.items() if po == o), None)
                return ('param', key) if key else ('param', o, e[2])
        if t == 'bit' and self.state_field is not None:
            x = e[1]
            if x[0] == 'ld':
                b, o = base_off(x[1])
                k = (o - self.state_field) * 8 + e[2]
                if b is not None and 0 <= k < 64 and self.kind_of(b) in ('npc', 'any') and k in self.states:
                    if o - self.state_field < 8:
                        return ('state', substitute(b, self.rename), self.states[k])
        if t in ('ld', 'bit', 'cmp', 'call', 'op', 'un', 'ent'):
            m = self.kb.match(e, 'any')
            if m is not None:
                cname, mname, obj, args = m
                kind = self.kind_of(obj) if obj is not None else 'any'
                m2 = self.kb.match(e, kind) if kind != 'any' else m
                if m2 is not None:
                    cname, mname, obj, args = m2
                    target = ('var', GLOBAL_CLASSES[cname]) if obj is None else substitute(obj, self.rename)
                    return ('m', mname, target, tuple(substitute(a, self.rename) for a in args))
        return None

    def simplify(self, e):
        t = e[0]
        if t in ('op', 'cmp') and e[1][:1] == 'f' and e[1] not in ('false',):
            # integer constants in float arithmetic are float bits
            a, b = [substitute(self.as_float(x), self.simplify) for x in (e[2], e[3])]
            return (t, e[1], a, b)
        if t == 'un':
            if e[1] in ('i2f', 'f2i', 'i2f64', 'lo32', 'lo16', 'lo8', 'sx32', 'sx16', 'sx8', 'zx32', 'b2i'):
                return substitute(e[2], self.simplify)
            if e[1] in ('neg', 'fneg'):
                a = e[2]
                if a[0] == 'num':
                    return ('num', -a[1])
                if a[0] == 'f' or a[0] == 'c':
                    return ('num', -float(fval(a) if a[0] == 'f' else signed(a[1])))
                return None
        if t == 'f':
            return ('num', e[1])
        if t == 'c':
            s = self.string(e) if self.kb.im.base <= e[1] < self.kb.im.base + self.kb.im.size else None
            if s is not None and len(s) >= 2:
                return ('s', s)
            v = signed(e[1])
            if 0xFFF00000 <= v <= 0xFFFFFFFF:
                v -= 1 << 32           # a negative 32-bit integer
            return ('num', v)
        if t == 'cmp' and e[1] in ('eq', 'ne') and e[2][0] == 'kvhas' and e[3][0] in ('c', 'num') and not e[3][1]:
            return e[2] if e[1] == 'ne' else ('lnot', e[2])
        if t == 'ite':
            c, a, b = substitute(e[1], self.simplify), e[2], e[3]
            if a == b:
                return substitute(a, self.simplify)
            # kv.name with a default when the key is missing: "kv.name or default"
            if c[0] == 'kvhas' and a[0] == 'kv' and a[1] == c[1] and len(a) == 2:
                return ('kv', a[1], substitute(b, self.simplify))
            if c[0] == 'lnot' and c[1][0] == 'kvhas' and b[0] == 'kv' and b[1] == c[1][1] and len(b) == 2:
                return ('kv', b[1], substitute(a, self.simplify))
            if a == ('num', 1.0) and b == ('num', 0.0) or a == ('num', 1) and b == ('num', 0):
                return None
        return None

    # --- output
    def status(self, e, aborted):
        for x in walk(e):
            if x[0] in ('call', 'ld', 'sym', 'g', 'kind', 'any', 'ent', 'serial', 'slot', 'abs', 'icall'):
                k = unknown_key(x)
                self.unknown[k] = self.unknown.get(k, 0) + 1
                ex = self.examples.setdefault(k, [])
                if len(ex) < 3:
                    ex.append((self.cur, str(x)[:300]))
                return "partial"
        if aborted:
            return "partial"
        if e[0] == 'num':
            return "constant"
        return "formula"

    def flag_text(self, x, mask):
        """A mask of flags of x's enum by member names (A | B), else the number."""
        members = self.enum_members.get(enum_of(x) or '', {})
        names = []
        rest = mask
        for v, n in sorted(members.items()):
            if v and v & (v - 1) == 0 and rest & v:
                names.append(n)
                rest &= ~v
        if names and not rest:
            return names[0] if len(names) == 1 else "(%s)" % " | ".join(names)
        return str(mask)

    def text(self, e, prec=0):
        t = e[0]
        if t == 'num':
            s = fmt_num(e[1])
            return "(%s)" % s if e[1] < 0 and prec > 0 else s
        if t == 'special':
            if len(e) == 2:
                return "%%%s%%" % e[1]
            lvl = e[3]
            s = '%s:GetSpecialValueFor("%s")' % (self.text(e[2], 9), e[1])
            if lvl not in (('num', -1), ('num', 4294967295)):
                s = '%s:GetLevelSpecialValueFor("%s", %s)' % (self.text(e[2], 9), e[1], self.text(lvl))
            return s
        if t == 'kv':
            if len(e) == 3 and e[2] not in (('num', 0), ('num', 0.0)):
                s = "kv.%s or %s" % (e[1], self.text(e[2], 3))
                return "(%s)" % s if prec > 2 else s
            return "kv.%s" % e[1]
        if t == 'kvhas':
            return "kv.%s ~= nil" % e[1]
        if t == 'var':
            return e[1]
        if t == 'm':
            args = ", ".join(self.text(a) for a in e[3])
            if e[2] == ('var', None):
                return "%s(%s)" % (e[1], args)          # a global function
            return "%s:%s(%s)" % (self.text(e[2], 9), e[1], args)
        if t == 'state':
            return "state(%s, %s)" % (self.text(e[1]), e[2])
        if t == 'field':
            return "self.field_%x" % e[1]
        if t == 'param':
            return "params.%s" % e[1] if len(e) == 2 else "params[0x%x]" % e[1]
        if t == 'str':
            p = e[1]
            if p[0] == 'c':
                s = self.kb.im.text(p[1] - self.kb.im.base, 200)
                if s is not None:
                    return '"%s"' % s
            return "?"
        if t == 's':
            return '"%s"' % e[1]
        if t == 'enum':
            return e[1]
        if t == 'none':
            return "nil"
        if t == 'ite':
            s = "%s ? %s : %s" % (self.text(e[1], 2), self.text(e[2], 2), self.text(e[3], 1))
            return "(%s)" % s if prec > 1 else s
        if t == 'cmp':
            ops = {'eq': '==', 'ne': '~=', 'slt': '<', 'sle': '<=', 'sgt': '>', 'sge': '>=', 'ult': '<',
                   'ule': '<=', 'ugt': '>', 'uge': '>=', 'flt': '<', 'fle': '<=', 'fgt': '>', 'fge': '>=',
                   'feq': '==', 'fne': '~='}
            if e[1] in ('true', 'false'):
                return e[1]
            a, b = e[2], e[3]
            en = enum_of(a)
            if en and e[1] in ('eq', 'ne') and b[0] == 'num' and isinstance(b[1], int) and \
                    b[1] in self.enum_members.get(en, {}):
                b = ('enum', self.enum_members[en][b[1]])
            if e[1] in ('ne', 'fne') and b in (('num', 0), ('num', 0.0)) and is_boolish(a):
                return self.text(a, prec)
            if e[1] in ('eq', 'feq') and b in (('num', 0), ('num', 0.0)) and is_boolish(a):
                return "not " + self.text(a, 8)
            s = "%s %s %s" % (self.text(a, 5), ops.get(e[1], e[1]), self.text(b, 5))
            return "(%s)" % s if prec > 4 else s
        if t == 'lnot':
            return "not " + self.text(e[1], 8)
        if t in ('band', 'bor'):
            word, p = ("and", 3) if t == 'band' else ("or", 2)
            s = "%s %s %s" % (self.text(e[1], p), word, self.text(e[2], p))
            return "(%s)" % s if prec > p else s
        if t == 'bit':
            s = "%s & %s ~= 0" % (self.text(e[1], 8), self.flag_text(e[1], 1 << e[2]))
            return "(%s)" % s if prec > 4 else s
        if t == 'op':
            name = e[1]
            sym = {'add': '+', 'fadd': '+', 'sub': '-', 'fsub': '-', 'mul': '*', 'fmul': '*', 'fdiv': '/',
                   'sdiv': '/', 'udiv': '/', 'and': '&', 'or': '|', 'xor': '~', 'shl': '<<', 'shr': '>>',
                   'sar': '>>', 'srem': '%', 'urem': '%'}.get(name)
            if name in ('fmin', 'fmax'):
                return "math.%s(%s, %s)" % (name[1:], self.text(e[2]), self.text(e[3]))
            a, b = e[2], e[3]
            if name in ('fmul', 'mul') and b[0] == 'num' and 0 < abs(b[1]) < 1:
                inv = 1 / b[1]
                if abs(inv - round(inv)) < 1e-3 * abs(inv):
                    name, sym, b = 'fdiv', '/', ('num', float(round(inv)))
            if name in ('add', 'fadd') and b[0] == 'num' and b[1] < 0:
                sym, b = '-', ('num', -b[1])
            if name == 'and' and b[0] == 'num' and isinstance(b[1], int) and enum_of(a):
                b = ('enum', self.flag_text(a, b[1]))
            p = {'+': 6, '-': 6, '*': 7, '/': 7, '%': 7}.get(sym, 5)
            s = "%s %s %s" % (self.text(a, p), sym or name, self.text(b, p + 1))
            return "(%s)" % s if prec > p else s
        if t == 'un':
            if e[1] in ('neg', 'fneg'):
                return "-" + self.text(e[2], 8)
            if e[1] == 'fabs':
                return "math.abs(%s)" % self.text(e[2])
            if e[1] == 'fsqrt':
                return "math.sqrt(%s)" % self.text(e[2])
            if e[1] == 'not':
                return "~" + self.text(e[2], 8)
            return self.text(e[2], prec)
        if t == 'any':
            return " | ".join(self.text(x, 2) for x in e[1])
        return "?"


ST_ON, ST_OFF, ST_UNSET, ST_UNKNOWN = ('stv', 'on'), ('stv', 'off'), ('stv', 'unset'), ('stv', '?')


def bit_of(e, k, initial):
    """Bit k of a state mask after CheckState: 1, 0, 'same' (as before), ('ite', c, a, b), or None."""
    t = e[0]
    if e == initial:
        return 'same'
    if t == 'c':
        return (e[1] >> k) & 1
    if t == 'op' and e[1] in ('or', 'and', 'xor'):
        a, b = bit_of(e[2], k, initial), bit_of(e[3], k, initial)
        if e[1] == 'or':
            if a == 1 or b == 1:
                return 1
            if a == 0:
                return b
            if b == 0:
                return a
        elif e[1] == 'and':
            if a == 0 or b == 0:
                return 0
            if a == 1:
                return b
            if b == 1:
                return a
        else:
            if b == 0:
                return a
            if a == 0:
                return b
        return None
    if t == 'ite':
        return ('ite', e[1], bit_of(e[2], k, initial), bit_of(e[3], k, initial))
    return None


def state_value(on, off):
    """The modifier's verdict on one state from its bits in the two masks."""
    if isinstance(on, tuple) and on[0] == 'ite':
        return ite(on[1], state_value(on[2], off), state_value(on[3], off))
    if isinstance(off, tuple) and off[0] == 'ite':
        return ite(off[1], state_value(on, off[2]), state_value(on, off[3]))
    if on == 1:
        return ST_ON
    if off == 1:
        return ST_OFF
    if on in (0, 'same') and off in (0, 'same'):
        return ST_UNSET
    return ST_UNKNOWN


def when_of(tree, target):
    """The condition under which a decision tree of state values gives target."""
    if tree is None:
        return FALSE
    if tree[0] == 'stv':
        return TRUE if tree == target else FALSE
    if tree[0] == 'any':
        return TRUE if all(x == target for x in tree[1]) else FALSE
    if tree[0] == 'ite':
        c, a, b = tree[1], when_of(tree[2], target), when_of(tree[3], target)
        if a == b:
            return a
        if a == TRUE and b == FALSE:
            return c
        if a == FALSE and b == TRUE:
            return lnot(c)
        if b == FALSE:
            return ('band', c, a)
        if a == FALSE:
            return ('band', lnot(c), b)
        if a == TRUE:
            return ('bor', c, b)
        return ('bor', lnot(c), a)
    return FALSE


def unknown_key(x):
    """A short description of an unresolved node (statistics for development)."""
    t = x[0]
    if t == 'call':
        n = x[1]
        if isinstance(n, tuple):
            return "vcall %s" % (n[2] if n[0] == 'vcall' else n[0])
        return "call " + str(n)[:60]
    if t == 'ld':
        b, o = base_off(x[1])
        return "ld %s+0x%x" % (b[0] if b else 'abs', o)
    if t == 'sym':
        return "sym " + x[1]
    return t


def refs_fields(v, fields_from):
    """Whether a value depends on fields of the modifier (a counter, an accumulated value)."""
    for x in walk(v):
        if x[0] == 'ld':
            b, o = base_off(x[1])
            if b == THIS and o >= fields_from:
                return True
    return False


# which enum the value of a method / params field is
ENUM_OF = {
    ('m', 'GetBehavior'): 'DOTA_ABILITY_BEHAVIOR',
    ('m', 'GetAbilityTargetFlags'): 'DOTA_UNIT_TARGET_FLAGS',
    ('m', 'GetAbilityTargetType'): 'DOTA_UNIT_TARGET_TYPE',
    ('m', 'GetAbilityTargetTeam'): 'DOTA_UNIT_TARGET_TEAM',
    ('m', 'GetAbilityDamageType'): 'DAMAGE_TYPES',
    ('param', 'damage_flags'): 'DOTADamageFlag_t',
    ('param', 'damage_type'): 'DAMAGE_TYPES',
    ('param', 'damage_category'): 'DamageCategory_t',
}


def enum_of(e):
    if e[0] == 'm':
        return ENUM_OF.get(('m', e[1]))
    if e[0] == 'param' and len(e) == 2:
        return ENUM_OF.get(('param', e[1]))
    return None


def is_boolish(e):
    return e[0] in ('m', 'state', 'cmp', 'lnot', 'bit')


def size_ok(v):
    return sum(1 for _ in walk(v)) <= 40 and not any(x[0] == 'keep' for x in walk(v))


def load(s, base, off, size):
    for o, sz, v in s.mem.get(base, ()):
        if o == off and sz == size:
            return v
        if o <= off and off + size <= o + sz and v[0] == 'c':
            return C((v[1] >> (8 * (off - o))) & ((1 << (8 * size)) - 1))
        if v[0] == 'cat' and o <= off < o + sz:
            for co, cs, cv in v[1]:
                if o + co == off and cs == size:
                    return cv
    return ('unset',)


def drop_keep(v):
    """A value with 'keep' branches (the field is set only on some paths): the value that is set."""
    if v is None:
        return None
    if v == ('keep',):
        return None
    if v[0] == 'ite':
        a, b = drop_keep(v[2]), drop_keep(v[3])
        if a is None:
            return b
        if b is None:
            return a
        return ite(v[1], a, b)
    if v[0] == 'any':
        vals = tuple(x for x in (drop_keep(y) for y in v[1]) if x is not None)
        if not vals:
            return None
        return vals[0] if len(vals) == 1 else ('any', vals)
    return v
