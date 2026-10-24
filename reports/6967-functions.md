# Dota 6967: изменения кода по функциям

Снимки `6966-11159903` → `6967-11168076`; funcdiff.py. В диффе: [S:…] — строка, [K:…] — константа из данных, F — вызов другой функции, L — переход внутри функции, [D]/[T] — прочие адреса. Регистры и смещения стека меняются и от перекомпиляции.

## libclient.so: функций 280912 → 280912; без изменений 280912, изменено 0, добавлено 0, удалено 0

## libserver.so: функций 220000 → 220000; без изменений 219992, изменено 7, добавлено 1, удалено 0

### изменена: 0x4a133a0 (62 байт) CDOTA_Ability_Meepo_MegaMeepo::vfunc#365 | строки: "modifier_meepo_megameepo_self"
было: 0x499e9a0 (90 байт)
- числа в инструкциях: −0 −0
- поля объектов: −0x868 −0x880
- прямых вызовов: 4 → 3
- инструкций: 23 → 19
```diff
@@ -14,10 +14,6 @@
 mov rdi, rax
 call F
-lea rdi, [D]
-mov rsi, rbx
-call F
-mov dword ptr [rbx + 0x868], 0
-mov dword ptr [rbx + 0x880], 0
+mov rdi, rbx
 mov rbx, qword ptr [rbp - 8]
 leave
-ret
+jmp F
```

### изменена: 0x4a4b270 (2023 байт) | строки: "stun_duration"; "backstab_angle"; "modifier_kez_katana_shard_debuff"; "duration"; "backstab"; "modifier_kez_katana_shard_active"; "target"; "particles/units/heroes/hero_kez/kez_katana_impale.vpcf"
было: 0x4a4b130 (2106 байт)
- числа в инструкциях: −1 −0xffffffff −0xf −0xf −-1 −0x7fff −0x7fff
- поля объектов: −0x10 −0x10 −0x10 −0x10 −0x30
- прямых вызовов: 54 → 55
- инструкций: 429 → 409
```diff
@@ -298,12 +298,14 @@
 movabs rax, 0xffff00000000
 mov qword ptr [rbp - 0xf0], rax
+lea r15, [rbp - 0x130]
 movabs rax, 0x1ffffffff
+mov qword ptr [rbp - 0x130], rcx
+mov qword ptr [rbp - 0x100], rcx
 movups xmmword ptr [rbp - 0xa8], xmm0
 pcmpeqd xmm0, xmm0
-mov qword ptr [rbp - 0x130], rcx
 mov qword ptr [rbp - 0x120], 0
+movups xmmword ptr [rbp - 0x68], xmm0
 mov qword ptr [rbp - 0x118], 0
 mov qword ptr [rbp - 0x110], 0
-mov qword ptr [rbp - 0x100], rcx
 mov qword ptr [rbp - 0xf8], 0
 mov qword ptr [rbp - 0xe8], 0
@@ -319,32 +321,16 @@
 mov qword ptr [rbp - 0x78], rax
 mov qword ptr [rbp - 0x70], 0
-movups xmmword ptr [rbp - 0x68], xmm0
 mov qword ptr [rbp - 0x58], 0xffffffffffffffff
 mov qword ptr [rbp - 0x50], 0
 call F
-test rax, rax
-je L
-mov rdx, qword ptr [rax + 0x10]
-test rdx, rdx
-je L
-mov eax, dword ptr [rdx + 0x10]
-mov ecx, dword ptr [rdx + 0x30]
-shr eax, 0xf
-and ecx, 1
-sub eax, ecx
-cmp dword ptr [rdx + 0x10], -1
-je L
-movzx edx, word ptr [rdx + 0x10]
-and dx, 0x7fff
-shl eax, 0xf
-movzx edx, dx
-or eax, edx
-mov dword ptr [rbp - 0x5c], eax
-mov rdi, rbx
-call F
-lea rdi, [rbp - 0x130]
+lea rdi, [rbp - 0x5c]
 mov rsi, rax
 call F
-mov rsi, rdi
+mov rdi, rbx
+call F
+mov rdi, r15
+mov rsi, rax
+call F
+mov rsi, r15
 mov edi, 0xd1
 call F
@@ -414,7 +400,4 @@
 jmp L
 nop dword ptr [rax + rax]
-mov dword ptr [rbp - 0x5c], 0xffffffff
-jmp L
-nop dword ptr [rax]
 pxor xmm0, xmm0
 movaps xmm3, xmm0
@@ -425,5 +408,2 @@
 lea r13, [rbp - 0x150]
 jmp L
-nop word ptr [rax + rax]
-mov edx, 0x7fff
-jmp L
```

### изменена: 0x4a65380 (1729 байт) CDOTA_Ability_Meepo_MegaMeepo::OnSpellStart | строки: "modifier_megameepo_frame_invulnerable"; "radius"; "npc_dota_meepo_megameepo_frame"; "modifier_faceless_void_chronosphere_freeze"; "modifier_enigma_black_hole_pull"; "modifier_legion_commander_duel"; "particles/units/heroes/hero_meepo/meepo_divide_we_stand.vpcf"; "modifier_meepo_flung"
было: 0x4a652a0 (1761 байт)
- числа в инструкциях: −0 −0
- поля объектов: −0x868 −0x880
- инструкций: 377 → 374
```diff
@@ -27,14 +27,11 @@
 ret
 nop dword ptr [rax]
-lea rdi, [D]
-mov rsi, r12
 lea r14, [rbp - 0x110]
+mov rdi, r12
+call F
 lea r15, [S:"modifier_megameepo_frame_invulnerable"]
-call F
-xor edx, edx
-mov rdi, r12
-mov dword ptr [r12 + 0x868], 0
+xor edx, edx
+mov rdi, r12
 lea rsi, [S:"radius"]
-mov dword ptr [r12 + 0x880], 0
 call F
 xor ecx, ecx
```

### изменена: 0x4a7bdb0 (1618 байт) CDOTA_Ability_Legion_Commander_PressTheAttack::OnSpellStart | строки: "radius"; "Hero_LegionCommander.PressTheAttack"; "particles/units/heroes/hero_legion_commander/legion_commander_press_the_attack_a"
было: 0x4a6d9f0 (1501 байт)
- числа в инструкциях: +1 +1 +1 +1
- инструкций: 319 → 338
```diff
@@ -48,10 +48,9 @@
 mov rdi, rbx
 mov qword ptr [rbp - 0xe8], 0
-lea r14, [rbp - 0xf0]
+lea r13, [rbp - 0xd0]
 mov qword ptr [rbp - 0xe0], 0
-lea r13, [rbp - 0xd0]
-call F
-mov rdi, rbx
-mov r15, rax
+call F
+mov rdi, rbx
+mov r14, rax
 call F
 mov rdi, rbx
@@ -60,51 +59,52 @@
 call F
 mov rdi, rbx
-movzx esi, byte ptr [rax + 0x624]
-mov dword ptr [rbp - 0x128], esi
-call F
-mov rdi, rax
-call F
-push 0
-mov rcx, r15
+movzx r15d, byte ptr [rax + 0x624]
+call F
+mov rdi, rax
+call F
+push 0
+mov rcx, r14
 mov rdx, r13
 push 0
 mov rdi, rax
+mov esi, r15d
 mov r9d, 1
-mov r8, r14
-push 0
+push 0
+lea r8, [rbp - 0xf0]
 push 0x13
-mov esi, dword ptr [rbp - 0x128]
 movss xmm0, dword ptr [rbp - 0x124]
 call F
 add rsp, 0x20
 mov rsi, r12
+mov dword ptr [rbp - 0x100], 0xffffffff
+lea rdi, [rbp - 0x100]
+call F
+mov r8d, dword ptr [rbp - 0xf0]
+mov edx, dword ptr [rbp - 0x100]
+test r8d, r8d
+movsxd r14, r8d
+jle L
+mov rcx, qword ptr [rbp - 0xe8]
+movsxd r14, r8d
+xor eax, eax
+jmp L
+nop word ptr [rax + rax]
+add rax, 1
+cmp r14, rax
+je L
+cmp dword ptr [rcx + rax*4], edx
+jne L
+mov rdi, rbx
+call F
+test rax, rax
+je L
+mov rdi, rbx
+call F
+lea rdi, [rbp - 0xf8]
 mov dword ptr [rbp - 0xf8], 0xffffffff
-lea rdi, [rbp - 0xf8]
+mov rsi, rax
 call F
 movsxd rdx, dword ptr [rbp - 0xf0]
 mov ecx, dword ptr [rbp - 0xf8]
-test edx, edx
-jle L
-mov rsi, qword ptr [rbp - 0xe8]
-xor eax, eax
-jmp L
-nop
-add rax, 1
-cmp rdx, rax
-je L
-cmp dword ptr [rsi + rax*4], ecx
-jne L
-mov rdi, rbx
-call F
-test rax, rax
-je L
-mov rdi, rbx
-call F
-lea rdi, [rbp - 0xf4]
-mov dword ptr [rbp - 0xf4], 0xffffffff
-mov rsi, rax
-call F
-movsxd rdx, dword ptr [rbp - 0xf0]
-mov ecx, dword ptr [rbp - 0xf4]
 test edx, edx
 jle L
@@ -268,7 +268,6 @@
 mov rdi, rbx
 mov qword ptr [rbp - 0xe8], 0
-lea r14, [rbp - 0xf0]
+lea r13, [rbp - 0xd0]
 mov qword ptr [rbp - 0xe0], 0
-lea r13, [rbp - 0xd0]
 call F
 mov rdi, rbx
@@ -280,5 +279,5 @@
 call F
 mov rdi, rbx
-movzx r15d, byte ptr [rax + 0x624]
+movzx r14d, byte ptr [rax + 0x624]
 call F
 mov rdi, rax
@@ -286,11 +285,11 @@
 push 0
```
(ещё 71 строк диффа: so-query.py fdiff libserver.so 0x4a7bdb0)

### изменена: 0x4a74f50 (727 байт) CDOTA_Modifier_Meepo_MegaMeepo_Self::OnDestroy | строки: "meepo_megameepo_fling"; "meepo_megameepo"
было: 0x4a75450 (759 байт)
- числа в инструкциях: −0 −0
- поля объектов: −0x868 −0x880
- инструкций: 188 → 185
```diff
@@ -44,10 +44,7 @@
 test r13d, r13d
 jg L
-lea rdi, [D]
-mov rsi, r12
+mov rdi, r12
 call F
-mov dword ptr [r12 + 0x868], 0
-mov dword ptr [r12 + 0x880], 0
-nop dword ptr [rax]
+nop
 mov ecx, dword ptr [rbx + 0x1ab8]
 cmp ecx, -1
```

### изменена: 0x4aa7a30 (3290 байт) | строки: "m_hDoubleShotTarget"; "EHANDLE"; "CHandle< T >"; "uint32"; "CBaseEntity"; "CHandle< %s >"; "ehandle"; "CDOTA_Unit_Hero_Muerta"
было: 0x4aa78f0 (3322 байт)
- числа в инструкциях: −0x5bd1e995 −0x5bd1e995 −0xd −0xf −0x6174
- прямых вызовов: 68 → 69
- инструкций: 665 → 658
```diff
@@ -450,19 +450,13 @@
 mov esi, eax
 call F
+lea rdi, [r13 + 0x14]
+mov esi, eax
+call F
+mov rdx, r13
+mov rsi, rbx
+mov rdi, r15
 lea rcx, [rbp - 0xc0]
-mov rsi, rbx
-mov rdi, r15
-xor eax, 0x6174
 mov r9d, 2
 mov r8d, 0x2300
-imul eax, eax, 0x5bd1e995
-mov edx, eax
-shr edx, 0xd
-xor eax, edx
-imul eax, eax, 0x5bd1e995
-mov edx, eax
-shr edx, 0xf
-xor eax, edx
-mov rdx, r13
 mov dword ptr [rbp - 0xc0], eax
 call F
@@ -474,5 +468,5 @@
 call F
 jmp L
-nop
+nop dword ptr [rax + rax]
 mov eax, r13d
 xor edx, edx
@@ -620,6 +614,5 @@
 jle L
 nop word ptr cs:[rax + rax]
-nop word ptr cs:[rax + rax]
-nop word ptr [rax + rax]
+nop
 add ebx, r14d
 mov eax, ebx
```

### изменена: 0x5c25d70 (1027 байт)
было: 0x5c25d00 (947 байт)
- числа в инструкциях: +2 +1 +0x38 +3 +0xffffffffffffffff
- поля объектов: +0x61
- прямых вызовов: 11 → 12
- инструкций: 208 → 232
```diff
@@ -1,2 +1,26 @@
+push rbp
+mov rbp, rsp
+push rbx
+mov ebx, esi
+sub rsp, 0x28
+movzx eax, byte ptr [rdi + 0x61]
+test al, 2
+je L
+test al, 1
+je L
+movsxd rax, ebx
+mov rbx, qword ptr [rbp - 8]
+imul rax, rax, 0x38
+add rax, qword ptr [rdi + 8]
+leave
+ret
+nop dword ptr [rax + rax]
+lea rdx, [rbp - 0x18]
+mov esi, 3
+mov qword ptr [rbp - 0x28], rdi
+mov qword ptr [rbp - 0x18], 0xffffffffffffffff
+call F
+mov rdi, qword ptr [rbp - 0x28]
+jmp L
 test edx, edx
 jle L
```

### добавлена: 0x4a13270 (295 байт) вызывается из: CDOTA_Ability_Meepo_MegaMeepo::vfunc#365, CDOTA_Ability_Meepo_MegaMeepo::OnSpellStart, CDOTA_Modifier_Meepo_MegaMeepo_Self::OnDestroy | строки: "modifier_meepo_megameepo"

### копии существующего кода (1): шаблонные / склеенные компоновщиком функции, такой же код есть и в другой сборке — не новый код
- одной копией существующего кода меньше: 0x5c25c90 (80 байт)
