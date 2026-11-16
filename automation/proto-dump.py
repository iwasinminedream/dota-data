#!/usr/bin/env python3
"""
Rebuilds the .proto files compiled into the game's libraries: every serialized FileDescriptorProto
embedded by protoc's generated code (usermessages, netmessages, GC messages, modifiers, demo, ...)
is found, parsed with google.protobuf's descriptor_pb2 and printed back as .proto source.

    proto-dump.py OUT_DIR LIB.so [LIB.so ...]

OUT_DIR/<name>.proto for each file (the path inside the name kept); a file whose content differs
between libraries is written once per variant as <name>@<lib>.proto. OUT_DIR/index.json maps every
.proto to the libraries that carry it. Custom options (Valve's extensions) are kept as
`option (<field number>) = …` from the unknown fields, since their definitions are only known by number
when the extension file is not among the dumped ones. Needs `pip install protobuf`.
"""
import hashlib
import json
import os
import re
import sys

from google.protobuf import descriptor_pb2, descriptor_pool, message_factory
from google.protobuf.message import DecodeError


def legacy_descriptor_class():
    """FileDescriptorProto without the editions fields (features, edition_defaults, feature_support):
    Valve's own options reuse those numbers (e.g. FieldOptions 20 = a string), which the current
    descriptor.proto would parse as messages and reject. Here they stay unknown fields."""
    fdp = descriptor_pb2.FileDescriptorProto()
    descriptor_pb2.DESCRIPTOR.CopyToProto(fdp)
    fdp.name, fdp.package = 'legacy/descriptor.proto', 'legacy_descriptor'

    def fix(msg):
        if msg.name.endswith('Options'):
            keep = [f for f in msg.field if f.name not in ('features', 'edition_defaults', 'feature_support')]
            del msg.field[:]
            msg.field.extend(keep)
        for f in msg.field:
            if f.HasField('type_name'):
                f.type_name = f.type_name.replace('.google.protobuf.', '.legacy_descriptor.')
            if f.HasField('extendee'):
                f.extendee = f.extendee.replace('.google.protobuf.', '.legacy_descriptor.')
        for n in msg.nested_type:
            fix(n)
    for m in fdp.message_type:
        fix(m)
    pool = descriptor_pool.DescriptorPool()
    pool.Add(fdp)
    return message_factory.GetMessageClass(pool.FindMessageTypeByName('legacy_descriptor.FileDescriptorProto'))


FileDescriptorProto = legacy_descriptor_class()

NAME_RE = re.compile(rb'\x0a([\x01-\x7f])([A-Za-z0-9_./-]{1,126}\.proto)')
TYPE_NAMES = {1: 'double', 2: 'float', 3: 'int64', 4: 'uint64', 5: 'int32', 6: 'fixed64', 7: 'fixed32',
              8: 'bool', 9: 'string', 10: 'group', 11: 'message', 12: 'bytes', 13: 'uint32', 14: 'enum',
              15: 'sfixed32', 16: 'sfixed64', 17: 'sint32', 18: 'sint64'}
LABELS = {1: 'optional', 2: 'required', 3: 'repeated'}


def varint(buf, pos):
    result = shift = 0
    while pos < len(buf):
        b = buf[pos]
        pos += 1
        result |= (b & 0x7f) << shift
        if not b & 0x80:
            return result, pos
        shift += 7
        if shift > 63:
            break
    raise ValueError


def field_ends(buf, start, max_field=14):
    """Field boundaries of a FileDescriptorProto starting at start, read until a field cannot belong to
    it; data right after the descriptor can look like fields, so the caller backs off from the end."""
    ends = []
    pos = start
    while pos < len(buf):
        try:
            tag, p = varint(buf, pos)
        except ValueError:
            break
        field, wire = tag >> 3, tag & 7
        if not 1 <= field <= max_field:
            break
        if wire == 2:
            try:
                n, p = varint(buf, p)
            except ValueError:
                break
            if p + n > len(buf):
                break
            p += n
        elif wire == 0:
            try:
                _, p = varint(buf, p)
            except ValueError:
                break
        else:
            break  # FileDescriptorProto has only varint and length-delimited fields
        pos = p
        ends.append(pos)
    return ends


def find_descriptors(data):
    found = {}
    for m in NAME_RE.finditer(data):
        if m.group(1)[0] != len(m.group(2)):
            continue
        start = m.start()
        fd = None
        for end in reversed(field_ends(data, start)[-8:]):
            try:
                fd = FileDescriptorProto.FromString(data[start:end])
                break
            except DecodeError:
                continue
        if fd is None or not fd.name.endswith('.proto') or not (fd.message_type or fd.enum_type or fd.service or fd.extension):
            continue
        blob = data[start:end]
        if fd.name not in found or len(blob) > len(found[fd.name][1]):
            found[fd.name] = (fd, blob)
    return found


def literal(value, field=None):
    if isinstance(value, bool):
        return 'true' if value else 'false'
    if isinstance(value, str):
        return json.dumps(value, ensure_ascii=False)
    if isinstance(value, bytes):
        return json.dumps(value.decode('latin-1'))
    if field is not None and field.enum_type is not None:
        return field.enum_type.values_by_number[value].name if value in field.enum_type.values_by_number else str(value)
    return str(value)


def unknown_options(options):
    """Custom options (extensions unknown to descriptor_pb2) as (number, value) from the raw bytes."""
    raw = options.SerializeToString()
    out = []
    pos = 0
    try:
        while pos < len(raw):
            tag, p = varint(raw, pos)
            field, wire = tag >> 3, tag & 7
            if wire == 0:
                value, p = varint(raw, p)
            elif wire == 2:
                n, p = varint(raw, p)
                value = raw[p:p + n]
                p += n
                try:
                    value = value.decode('utf-8')
                except UnicodeDecodeError:
                    value = value.hex()
            elif wire == 5:
                value, p = int.from_bytes(raw[p:p + 4], 'little'), p + 4
            elif wire == 1:
                value, p = int.from_bytes(raw[p:p + 8], 'little'), p + 8
            else:
                break
            if field not in options.DESCRIPTOR.fields_by_number:
                out.append((field, value))
            pos = p
    except ValueError:
        pass
    return out


def option_items(options):
    items = [(f.name, literal(v, f)) for f, v in options.ListFields() if not getattr(f, 'is_repeated', False)]
    items += [(f'({n})', json.dumps(v, ensure_ascii=False) if isinstance(v, str) else str(v)) for n, v in unknown_options(options)]
    return items


def field_options(field):
    items = []
    if field.HasField('default_value'):
        d = field.default_value
        items.append(('default', json.dumps(d, ensure_ascii=False) if field.type in (9, 12) else d))
    if field.HasField('json_name') and field.json_name != camel(field.name):
        items.append(('json_name', json.dumps(field.json_name)))
    if field.HasField('options'):
        items += option_items(field.options)
    return f" [{', '.join(f'{k} = {v}' for k, v in items)}]" if items else ''


def camel(name):
    parts = name.split('_')
    return parts[0] + ''.join(p[:1].upper() + p[1:] for p in parts[1:])


def type_of(field):
    return field.type_name if field.type in (10, 11, 14) else TYPE_NAMES.get(field.type, f'type{field.type}')


def write_enum(out, enum, ind):
    out.append(f'{ind}enum {enum.name} {{')
    if enum.HasField('options'):
        out += [f'{ind}\toption {k} = {v};' for k, v in option_items(enum.options)]
    for v in enum.value:
        opts = option_items(v.options) if v.HasField('options') else []
        out.append(f"{ind}\t{v.name} = {v.number}{' [' + ', '.join(f'{k} = {x}' for k, x in opts) + ']' if opts else ''};")
    out.append(f'{ind}}}')


def write_field(out, field, ind, proto3, maps):
    if field.type == 11 and field.type_name in maps:
        k, v = maps[field.type_name]
        out.append(f'{ind}map<{type_of(k)}, {type_of(v)}> {field.name} = {field.number}{field_options(field)};')
        return
    label = LABELS.get(field.label, '')
    if proto3 and field.label == 1 and not field.proto3_optional:
        label = ''
    out.append(f"{ind}{label + ' ' if label else ''}{type_of(field)} {field.name} = {field.number}{field_options(field)};")


def write_message(out, msg, ind, scope, proto3):
    out.append(f'{ind}message {msg.name} {{')
    inner = ind + '\t'
    full = f'{scope}.{msg.name}'
    if msg.HasField('options'):
        out += [f'{inner}option {k} = {v};' for k, v in option_items(msg.options)]
    maps = {}
    for nested in msg.nested_type:
        if nested.options.map_entry:
            maps[f'{full}.{nested.name}'] = (nested.field[0], nested.field[1])
    for e in msg.enum_type:
        write_enum(out, e, inner)
    for nested in msg.nested_type:
        if not nested.options.map_entry:
            write_message(out, nested, inner, full, proto3)
    oneofs = {i: [] for i in range(len(msg.oneof_decl))}
    for field in msg.field:
        if field.HasField('oneof_index') and not field.proto3_optional:
            oneofs[field.oneof_index].append(field)
        else:
            write_field(out, field, inner, proto3, maps)
    for i, fields in oneofs.items():
        if fields:
            out.append(f'{inner}oneof {msg.oneof_decl[i].name} {{')
            for field in fields:
                out.append(f'{inner}\t{type_of(field)} {field.name} = {field.number}{field_options(field)};')
            out.append(f'{inner}}}')
    for r in msg.extension_range:
        out.append(f"{inner}extensions {r.start} to {'max' if r.end >= 536870912 else r.end - 1};")
    for r in msg.reserved_range:
        out.append(f"{inner}reserved {r.start}{'' if r.end - 1 == r.start else f' to {r.end - 1}'};")
    if msg.reserved_name:
        out.append(f"{inner}reserved {', '.join(json.dumps(n) for n in msg.reserved_name)};")
    write_extensions(out, msg.extension, inner, proto3)
    out.append(f'{ind}}}')


def write_extensions(out, extensions, ind, proto3):
    by_extendee = {}
    for ext in extensions:
        by_extendee.setdefault(ext.extendee, []).append(ext)
    for extendee, fields in by_extendee.items():
        out.append(f'{ind}extend {extendee} {{')
        for f in fields:
            write_field(out, f, ind + '\t', proto3, {})
        out.append(f'{ind}}}')


def render(fd):
    proto3 = fd.syntax == 'proto3'
    out = [f'syntax = "{fd.syntax or "proto2"}";', '']
    if fd.package:
        out += [f'package {fd.package};', '']
    for i, dep in enumerate(fd.dependency):
        kind = 'public ' if i in fd.public_dependency else 'weak ' if i in fd.weak_dependency else ''
        out.append(f'import {kind}"{dep}";')
    if fd.dependency:
        out.append('')
    if fd.HasField('options'):
        out += [f'option {k} = {v};' for k, v in option_items(fd.options)] + ['']
    scope = f'.{fd.package}' if fd.package else ''
    for e in fd.enum_type:
        write_enum(out, e, '')
        out.append('')
    for m in fd.message_type:
        write_message(out, m, '', scope, proto3)
        out.append('')
    write_extensions(out, fd.extension, '', proto3)
    for s in fd.service:
        out.append(f'service {s.name} {{')
        for m in s.method:
            cs = 'stream ' if m.client_streaming else ''
            ss = 'stream ' if m.server_streaming else ''
            opts = option_items(m.options) if m.HasField('options') else []
            body = ' {\n' + ''.join(f'\t\toption {k} = {v};\n' for k, v in opts) + '\t}' if opts else ';'
            out.append(f'\trpc {m.name} ({cs}{m.input_type}) returns ({ss}{m.output_type}){body}')
        out.append('}')
        out.append('')
    return '\n'.join(out).rstrip() + '\n'


def main(argv):
    if len(argv) < 2:
        print(__doc__)
        return 2
    out_dir, libs = argv[0], argv[1:]
    variants = {}  # name -> {sha: (text, [libs])}
    for lib in libs:
        with open(lib, 'rb') as f:
            data = f.read()
        found = find_descriptors(data)
        print(f'{os.path.basename(lib)}: {len(found)} .proto', file=sys.stderr)
        for name, (fd, _blob) in found.items():
            text = render(fd)
            sha = hashlib.sha1(text.encode()).hexdigest()
            variants.setdefault(name, {}).setdefault(sha, [text, []])[1].append(os.path.basename(lib))
    os.makedirs(out_dir, exist_ok=True)
    for old in os.listdir(out_dir):
        path = os.path.join(out_dir, old)
        if old.endswith('.proto') or old == 'index.json':
            os.remove(path)
    index = {}
    for name in sorted(variants):
        vs = sorted(variants[name].values(), key=lambda v: -len(v[1]))
        index[name] = [{'libs': sorted(v[1]), 'file': None} for v in vs]
        for i, (text, owners) in enumerate(vs):
            safe = name.replace('/', '__')
            file = safe if i == 0 else f'{safe[:-6]}@{sorted(owners)[0]}.proto'
            with open(os.path.join(out_dir, file), 'w') as f:
                f.write(text)
            index[name][i]['file'] = file
    with open(os.path.join(out_dir, 'index.json'), 'w') as f:
        json.dump(index, f, indent=1, sort_keys=True)
        f.write('\n')
    print(f'{len(variants)} .proto files', file=sys.stderr)
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
