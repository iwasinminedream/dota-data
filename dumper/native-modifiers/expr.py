"""Symbolic expressions of the executor: plain tuples, so they hash and compare structurally.

    ('c', int)                 integer constant (masked to 64 bits)
    ('f', float)               float constant
    ('sym', name)              an input: 'this', 'out', 'params', 'rsp0', 'undef', ...
    ('g', rva)                 address of a writable global of the image
    ('ld', addr, size)         a read of memory nothing was stored to
    ('op', name, a, b)         binary operation (add sub mul and or xor shl shr sar sdiv fadd fsub fmul fdiv fmin fmax)
    ('un', name, a)            unary operation (neg not lo8 lo16 lo32 sx8 sx16 sx32 i2f f2i fneg fabs fsqrt b2i)
    ('cmp', name, a, b)        comparison, a boolean (eq ne slt sle sgt sge ult ule ugt uge flt fle fgt fge feq fne)
    ('bit', a, k)              bit k of a, a boolean
    ('lnot', a)                logical not of a boolean
    ('call', name, args)       result of a call the executor did not follow
    ('slot', handle)           entity list slot of a handle (internal)
    ('ent', handle)            the entity a handle points at
    ('ite', cond, a, b)        cond ? a : b
"""
import math
import struct

M64 = (1 << 64) - 1
MASK = {1: 0xFF, 2: 0xFFFF, 4: 0xFFFFFFFF, 8: M64}


def C(v):
    return ('c', v & M64)


def F(v):
    return ('f', float(v))


ZERO = ('c', 0)
ONE = ('c', 1)
TRUE = ('cmp', 'true', ZERO, ZERO)
FALSE = ('cmp', 'false', ZERO, ZERO)


def is_c(e):
    return e[0] == 'c'


def signed(v, size=8):
    v &= MASK[size]
    return v - (1 << (8 * size)) if v >> (8 * size - 1) else v


def bits_to_f32(v):
    return struct.unpack("<f", struct.pack("<I", v & 0xFFFFFFFF))[0]


def f32_to_bits(f):
    try:
        return struct.unpack("<I", struct.pack("<f", f))[0]
    except (OverflowError, struct.error):
        return 0


def is_bool(e):
    return e[0] in ('cmp', 'bit', 'lnot')


def base_off(e):
    """Split an address into (base expression, constant offset)."""
    if e[0] == 'c':
        return None, signed(e[1])
    if e[0] == 'op' and e[1] == 'add' and e[3][0] == 'c':
        b, o = base_off(e[2])
        return b, o + signed(e[3][1])
    if e[0] == 'op' and e[1] == 'sub' and e[3][0] == 'c':
        b, o = base_off(e[2])
        return b, o - signed(e[3][1])
    return e, 0


def addr(base, off):
    if base is None:
        return C(off)
    if off == 0:
        return base
    return ('op', 'add', base, C(off))


# --- constructors with folding

def strip_lo(e):
    while e[0] == 'un' and e[1] in ('lo8', 'lo16', 'lo32'):
        e = e[2]
    return e


def op(name, a, b):
    if name in ('add', 'sub', 'mul', 'and', 'or', 'xor', 'shl', 'shr', 'sar'):
        return iop(name, a, b)
    if name in ('fadd', 'fsub', 'fmul', 'fdiv', 'fmin', 'fmax'):
        return fop(name, a, b)
    return ('op', name, a, b)


def iop(name, a, b):
    if a[0] == 'c' and b[0] == 'c':
        x, y = a[1], b[1]
        if name == 'add':
            return C(x + y)
        if name == 'sub':
            return C(x - y)
        if name == 'mul':
            return C(x * y)
        if name == 'and':
            return C(x & y)
        if name == 'or':
            return C(x | y)
        if name == 'xor':
            return C(x ^ y)
        if name == 'shl':
            return C(x << (y & 63))
        if name == 'shr':
            return C(x >> (y & 63))
        if name == 'sar':
            return C(signed(x) >> (y & 63))
    # constants to the right
    if name in ('add', 'mul', 'and', 'or', 'xor') and a[0] == 'c':
        a, b = b, a
    if b[0] == 'c':
        k = b[1]
        if name in ('add', 'sub', 'or', 'xor', 'shl', 'shr', 'sar') and k == 0:
            return a
        if name == 'mul' and k == 1:
            return a
        if name in ('mul', 'and') and k == 0:
            return ZERO
        if name == 'add' and a[0] == 'op' and a[1] in ('add', 'sub') and a[3][0] == 'c':
            inner = a[3][1] if a[1] == 'add' else -a[3][1]
            return iop('add', a[2], C(inner + k))
        if name == 'sub':
            return iop('add', a, C(-k))
        if name == 'and' and k == 1:
            s = strip_lo(a)
            if s[0] == 'op' and s[1] == 'shr' and s[3][0] == 'c':
                return ('un', 'b2i', ('bit', s[2], s[3][1]))
            if s[0] == 'un' and s[1] == 'not':
                inner = iop('and', s[2], ONE)
                if inner[0] == 'un' and inner[1] == 'b2i':
                    return ('un', 'b2i', lnot(inner[2]))
            if s[0] == 'un' and s[1] == 'b2i':
                return s
            if s[0] == 'ld':
                return ('un', 'b2i', ('bit', s, 0))
    if name == 'sub' and a == b:
        return ZERO
    if name == 'xor' and a == b:
        return ZERO
    return ('op', name, a, b)


def fval(e):
    """Float value of a constant expression (float constants, or integer bits of a float)."""
    if e[0] == 'f':
        return e[1]
    if e[0] == 'c':
        return bits_to_f32(e[1])
    return None


def fop(name, a, b):
    x, y = fval(a), fval(b)
    if x is not None and y is not None:
        try:
            if name == 'fadd':
                return F(x + y)
            if name == 'fsub':
                return F(x - y)
            if name == 'fmul':
                return F(x * y)
            if name == 'fdiv':
                return F(x / y) if y else ('op', name, a, b)
            if name == 'fmin':
                return F(min(x, y))
            if name == 'fmax':
                return F(max(x, y))
        except (OverflowError, ValueError):
            pass
    if name == 'fmul':
        if y == 1.0:
            return a
        if x == 1.0:
            return b
        if y == 0.0 or x == 0.0:
            return F(0.0)
        if y == -1.0:
            return un('fneg', a)
        if x == -1.0:
            return un('fneg', b)
    if name in ('fadd', 'fsub') and y == 0.0:
        return a
    if name == 'fadd' and x == 0.0:
        return b
    if name == 'fsub' and x == 0.0:
        return un('fneg', b)
    if name == 'fdiv' and y == 1.0:
        return a
    return ('op', name, a, b)


def un(name, a):
    if a[0] == 'c':
        v = a[1]
        if name == 'neg':
            return C(-v)
        if name == 'not':
            return C(~v)
        if name == 'lo8':
            return C(v & 0xFF)
        if name == 'lo16':
            return C(v & 0xFFFF)
        if name == 'lo32':
            return C(v & 0xFFFFFFFF)
        if name == 'sx8':
            return C(signed(v, 1))
        if name == 'sx16':
            return C(signed(v, 2))
        if name == 'sx32':
            return C(signed(v, 4))
        if name == 'i2f':
            return F(signed(v, 4))
        if name == 'i2f64':
            return F(signed(v, 8))
        if name == 'fneg':
            return F(-bits_to_f32(v))
    if a[0] == 'f':
        v = a[1]
        if name == 'fneg':
            return F(-v)
        if name == 'fabs':
            return F(abs(v))
        if name == 'fsqrt' and v >= 0:
            return F(math.sqrt(v))
        if name == 'f2i' and math.isfinite(v):
            return C(int(v))
        if name in ('lo32', 'lo8', 'lo16'):
            return a
    if name in ('lo8', 'lo16', 'lo32'):
        size = {'lo8': 1, 'lo16': 2, 'lo32': 4}[name]
        if a[0] == 'ld' and a[2] <= size:
            return a
        if a[0] == 'op' and a[1] == 'and' and a[3][0] == 'c' and a[3][1] <= MASK[size]:
            return a
        if a[0] == 'op' and a[1] == 'shr' and a[3][0] == 'c' and a[2][0] == 'ld' and a[2][2] <= size:
            return a
        if a[0] == 'un' and a[1] in ('lo8', 'lo16', 'lo32'):
            inner = {'lo8': 1, 'lo16': 2, 'lo32': 4}[a[1]]
            return a if inner <= size else un(name, a[2])
        if a[0] == 'un' and a[1] in ('zx8', 'zx16', 'zx32', 'b2i', 'i2f', 'f2i', 'fneg', 'fabs', 'fsqrt'):
            if a[1] in ('b2i', 'i2f', 'f2i', 'fneg', 'fabs', 'fsqrt'):
                return a
            inner = {'zx8': 1, 'zx16': 2, 'zx32': 4}[a[1]]
            if inner <= size:
                return a[2] if inner == size else a
        if a[0] == 'un' and a[1] in ('sx8', 'sx16', 'sx32'):
            inner = {'sx8': 1, 'sx16': 2, 'sx32': 4}[a[1]]
            if inner >= size:
                return un(name, a[2]) if inner > size else a[2]
        if a[0] in ('f', 'call', 'ite') or is_bool(a):
            return a
        if a[0] == 'op' and a[1].startswith('f'):
            return a
    if name in ('sx32', 'sx16', 'sx8'):
        size = {'sx8': 1, 'sx16': 2, 'sx32': 4}[name]
        if a[0] == 'un' and a[1] == 'b2i':
            return a
    if name == 'neg' and a[0] == 'un' and a[1] == 'neg':
        return a[2]
    if name == 'fneg' and a[0] == 'un' and a[1] == 'fneg':
        return a[2]
    if name == 'i2f' and a[0] == 'un' and a[1] == 'neg':
        return un('fneg', un('i2f', a[2]))
    return ('un', name, a)


def lnot(c):
    if c == TRUE:
        return FALSE
    if c == FALSE:
        return TRUE
    if c[0] == 'lnot':
        return c[1]
    if c[0] == 'cmp':
        inv = {'eq': 'ne', 'ne': 'eq', 'slt': 'sge', 'sge': 'slt', 'sle': 'sgt', 'sgt': 'sle',
               'ult': 'uge', 'uge': 'ult', 'ule': 'ugt', 'ugt': 'ule', 'feq': 'fne', 'fne': 'feq'}
        if c[1] in inv:
            return ('cmp', inv[c[1]], c[2], c[3])
    return ('lnot', c)


def cmp(name, a, b, size=8):
    """A comparison, folded to TRUE/FALSE when decidable."""
    if name.startswith('f'):
        x, y = fval(a), fval(b)
        if x is not None and y is not None and a[0] == 'f' and b[0] == 'f':
            r = {'flt': x < y, 'fle': x <= y, 'fgt': x > y, 'fge': x >= y, 'feq': x == y, 'fne': x != y}[name]
            return TRUE if r else FALSE
        return ('cmp', name, a, b)
    if a[0] == 'c' and b[0] == 'c':
        m = MASK[size]
        x, y = a[1] & m, b[1] & m
        sx, sy = signed(x, size), signed(y, size)
        r = {'eq': x == y, 'ne': x != y, 'ult': x < y, 'ule': x <= y, 'ugt': x > y, 'uge': x >= y,
             'slt': sx < sy, 'sle': sx <= sy, 'sgt': sx > sy, 'sge': sx >= sy}[name]
        return TRUE if r else FALSE
    # booleans compared with 0/1
    if b[0] == 'c' and a[0] == 'un' and a[1] == 'b2i' and name in ('eq', 'ne'):
        k = b[1] & MASK[size]
        if k == 0:
            return a[2] if name == 'ne' else lnot(a[2])
        if k == 1:
            return a[2] if name == 'eq' else lnot(a[2])
    if a == b and name in ('eq', 'ule', 'uge', 'sle', 'sge'):
        return TRUE
    if a == b and name in ('ne', 'ult', 'ugt', 'slt', 'sgt'):
        return FALSE
    if b[0] == 'c':
        b = C(signed(b[1], size)) if name.startswith('s') else C(b[1] & MASK[size])
    return ('cmp', name, a, b)


def is_type_check(c, e):
    """c compares a byte field of entity e with a constant: an inlined dynamic cast of e."""
    if c[0] != 'cmp' or c[1] not in ('eq', 'ne') or c[3][0] != 'c':
        return None
    x = c[2]
    if x[0] == 'ld' and x[2] == 1:
        b, o = base_off(x[1])
        if b == e and 0 < o < 0x1000:
            return c[1]
    return None


def ite(c, a, b):
    if c == TRUE:
        return a
    if c == FALSE:
        return b
    if a == b:
        return a
    if c[0] == 'lnot':
        return ite(c[1], b, a)
    # cast(e) = e when its type field matches, else nil: assume the cast succeeds (like valid handles)
    if a == ZERO and b[0] == 'ent' and is_type_check(c, b) == 'ne':
        return b
    if b == ZERO and a[0] == 'ent' and is_type_check(c, a) == 'eq':
        return a
    return ('ite', c, a, b)


def walk(e):
    """Every sub-expression of e (pre-order)."""
    stack = [e]
    while stack:
        x = stack.pop()
        yield x
        if not isinstance(x, tuple):
            continue
        for y in x[1:]:
            if isinstance(y, tuple) and y and isinstance(y[0], str):
                stack.append(y)
            elif isinstance(y, tuple):
                for z in y:
                    if isinstance(z, tuple) and z and isinstance(z[0], str):
                        stack.append(z)


def substitute(e, fn):
    """Rebuild e bottom-up, replacing every sub-expression x for which fn(x) is not None."""
    r = fn(e)
    if r is not None:
        return r
    if not isinstance(e, tuple) or not e:
        return e
    t = e[0]
    if t in ('c', 'f', 'sym', 'g'):
        return e
    if t == 'ld':
        return ('ld', substitute(e[1], fn), e[2])
    if t == 'op':
        return op(e[1], substitute(e[2], fn), substitute(e[3], fn))
    if t == 'un':
        return un(e[1], substitute(e[2], fn))
    if t == 'cmp':
        return cmp(e[1], substitute(e[2], fn), substitute(e[3], fn))
    if t == 'bit':
        return ('bit', substitute(e[1], fn), e[2])
    if t == 'lnot':
        return lnot(substitute(e[1], fn))
    if t == 'call':
        return ('call', e[1], tuple(substitute(a, fn) for a in e[2]))
    if t in ('slot', 'ent'):
        return (t, substitute(e[1], fn))
    if t == 'ite':
        return ite(substitute(e[1], fn), substitute(e[2], fn), substitute(e[3], fn))
    # other nodes: rebuild their expression children
    out = [t]
    changed = False
    for x in e[1:]:
        if isinstance(x, tuple) and x and isinstance(x[0], str):
            y = substitute(x, fn)
        elif isinstance(x, tuple) and x and all(isinstance(z, tuple) and z and isinstance(z[0], str) for z in x):
            y = tuple(substitute(z, fn) for z in x)
        else:
            y = x
        changed |= y is not x
        out.append(y)
    return tuple(out) if changed else e
