# Dota 6966: изменения кода по функциям

Снимки `6965-11152239` → `6966-11159903`; funcdiff.py. В диффе: [S:…] — строка, [K:…] — константа из данных, F — вызов другой функции, L — переход внутри функции, [D]/[T] — прочие адреса. Регистры и смещения стека меняются и от перекомпиляции.

## libclient.so: функций 280912 → 280912; без изменений 280912, изменено 0, добавлено 0, удалено 0

## libserver.so: функций 220000 → 220000; без изменений 219994, изменено 6, добавлено 0, удалено 0

### изменена: 0x499e9a0 (90 байт) CDOTA_Ability_Meepo_MegaMeepo::vfunc#365 | строки: "modifier_meepo_megameepo_self"
было: 0x499e9a0 (80 байт)
- числа в инструкциях: +0
- поля объектов: +0x868
- инструкций: 22 → 23
```diff
@@ -17,4 +17,5 @@
 mov rsi, rbx
 call F
+mov dword ptr [rbx + 0x868], 0
 mov dword ptr [rbx + 0x880], 0
 mov rbx, qword ptr [rbp - 8]
```

### изменена: 0x4a4b130 (2106 байт) | строки: "stun_duration"; "backstab_angle"; "modifier_kez_katana_shard_debuff"; "duration"; "backstab"; "modifier_kez_katana_shard_active"; "target"; "particles/units/heroes/hero_kez/kez_katana_impale.vpcf"
было: 0x4a4b130 (2023 байт)
- числа в инструкциях: +1 +0xffffffff +0xf +0xf +-1 +0x7fff +0x7fff
- поля объектов: +0x10 +0x10 +0x10 +0x10 +0x30
- прямых вызовов: 55 → 54
- инструкций: 409 → 429
```diff
@@ -298,14 +298,12 @@
 movabs rax, 0xffff00000000
 mov qword ptr [rbp - 0xf0], rax
-lea r15, [rbp - 0x130]
 movabs rax, 0x1ffffffff
-mov qword ptr [rbp - 0x130], rcx
-mov qword ptr [rbp - 0x100], rcx
 movups xmmword ptr [rbp - 0xa8], xmm0
 pcmpeqd xmm0, xmm0
+mov qword ptr [rbp - 0x130], rcx
 mov qword ptr [rbp - 0x120], 0
-movups xmmword ptr [rbp - 0x68], xmm0
 mov qword ptr [rbp - 0x118], 0
 mov qword ptr [rbp - 0x110], 0
+mov qword ptr [rbp - 0x100], rcx
 mov qword ptr [rbp - 0xf8], 0
 mov qword ptr [rbp - 0xe8], 0
@@ -321,16 +319,32 @@
 mov qword ptr [rbp - 0x78], rax
 mov qword ptr [rbp - 0x70], 0
+movups xmmword ptr [rbp - 0x68], xmm0
 mov qword ptr [rbp - 0x58], 0xffffffffffffffff
 mov qword ptr [rbp - 0x50], 0
 call F
-lea rdi, [rbp - 0x5c]
+test rax, rax
+je L
+mov rdx, qword ptr [rax + 0x10]
+test rdx, rdx
+je L
+mov eax, dword ptr [rdx + 0x10]
+mov ecx, dword ptr [rdx + 0x30]
+shr eax, 0xf
+and ecx, 1
+sub eax, ecx
+cmp dword ptr [rdx + 0x10], -1
+je L
+movzx edx, word ptr [rdx + 0x10]
+and dx, 0x7fff
+shl eax, 0xf
+movzx edx, dx
+or eax, edx
+mov dword ptr [rbp - 0x5c], eax
+mov rdi, rbx
+call F
+lea rdi, [rbp - 0x130]
 mov rsi, rax
 call F
-mov rdi, rbx
-call F
-mov rdi, r15
-mov rsi, rax
-call F
-mov rsi, r15
+mov rsi, rdi
 mov edi, 0xd1
 call F
@@ -400,4 +414,7 @@
 jmp L
 nop dword ptr [rax + rax]
+mov dword ptr [rbp - 0x5c], 0xffffffff
+jmp L
+nop dword ptr [rax]
 pxor xmm0, xmm0
 movaps xmm3, xmm0
@@ -408,2 +425,5 @@
 lea r13, [rbp - 0x150]
 jmp L
+nop word ptr [rax + rax]
+mov edx, 0x7fff
+jmp L
```

### изменена: 0x4a652a0 (1761 байт) CDOTA_Ability_Meepo_MegaMeepo::OnSpellStart | строки: "modifier_megameepo_frame_invulnerable"; "radius"; "npc_dota_meepo_megameepo_frame"; "modifier_faceless_void_chronosphere_freeze"; "modifier_enigma_black_hole_pull"; "modifier_legion_commander_duel"; "particles/units/heroes/hero_meepo/meepo_divide_we_stand.vpcf"; "modifier_meepo_flung"
было: 0x4a65240 (1745 байт)
- прямых вызовов: 49 → 50
- инструкций: 374 → 377
```diff
@@ -27,12 +27,15 @@
 ret
 nop dword ptr [rax]
+lea rdi, [D]
+mov rsi, r12
+lea r14, [rbp - 0x110]
+lea r15, [S:"modifier_megameepo_frame_invulnerable"]
+call F
+xor edx, edx
+mov rdi, r12
+mov dword ptr [r12 + 0x868], 0
 lea rsi, [S:"radius"]
-xor edx, edx
-mov rdi, r12
-mov dword ptr [r12 + 0x868], 0
 mov dword ptr [r12 + 0x880], 0
-lea r14, [rbp - 0x110]
-call F
-lea r15, [S:"modifier_megameepo_frame_invulnerable"]
+call F
 xor ecx, ecx
 xor edx, edx
```

### изменена: 0x4a75450 (759 байт) CDOTA_Modifier_Meepo_MegaMeepo_Self::OnDestroy | строки: "meepo_megameepo_fling"; "meepo_megameepo"
было: 0x4a74810 (730 байт)
- числа в инструкциях: +0 +0
- поля объектов: +0x868 +0x880
- прямых вызовов: 14 → 15
- инструкций: 182 → 188
```diff
@@ -44,4 +44,10 @@
 test r13d, r13d
 jg L
+lea rdi, [D]
+mov rsi, r12
+call F
+mov dword ptr [r12 + 0x868], 0
+mov dword ptr [r12 + 0x880], 0
+nop dword ptr [rax]
 mov ecx, dword ptr [rbx + 0x1ab8]
 cmp ecx, -1
@@ -77,5 +83,5 @@
 pop rbp
 jmp F
-nop dword ptr [rax]
+nop dword ptr [rax + rax]
 lea rdi, [rbp - 0x38]
 mov esi, r13d
```

### изменена: 0x4a6d9f0 (1501 байт) CDOTA_Ability_Legion_Commander_PressTheAttack::OnSpellStart | строки: "radius"; "Hero_LegionCommander.PressTheAttack"; "particles/units/heroes/hero_legion_commander/legion_commander_press_the_attack_a"
было: 0x4a7b670 (1618 байт)
- числа в инструкциях: −1 −1 −1 −1
- инструкций: 338 → 319
```diff
@@ -48,9 +48,10 @@
 mov rdi, rbx
 mov qword ptr [rbp - 0xe8], 0
+lea r14, [rbp - 0xf0]
+mov qword ptr [rbp - 0xe0], 0
 lea r13, [rbp - 0xd0]
-mov qword ptr [rbp - 0xe0], 0
-call F
-mov rdi, rbx
-mov r14, rax
+call F
+mov rdi, rbx
+mov r15, rax
 call F
 mov rdi, rbx
@@ -59,52 +60,51 @@
 call F
 mov rdi, rbx
-movzx r15d, byte ptr [rax + 0x624]
-call F
-mov rdi, rax
-call F
-push 0
-mov rcx, r14
+movzx esi, byte ptr [rax + 0x624]
+mov dword ptr [rbp - 0x128], esi
+call F
+mov rdi, rax
+call F
+push 0
+mov rcx, r15
 mov rdx, r13
 push 0
 mov rdi, rax
-mov esi, r15d
 mov r9d, 1
-push 0
-lea r8, [rbp - 0xf0]
+mov r8, r14
+push 0
 push 0x13
+mov esi, dword ptr [rbp - 0x128]
 movss xmm0, dword ptr [rbp - 0x124]
 call F
 add rsp, 0x20
 mov rsi, r12
-mov dword ptr [rbp - 0x100], 0xffffffff
-lea rdi, [rbp - 0x100]
-call F
-mov r8d, dword ptr [rbp - 0xf0]
-mov edx, dword ptr [rbp - 0x100]
-test r8d, r8d
-movsxd r14, r8d
-jle L
-mov rcx, qword ptr [rbp - 0xe8]
-movsxd r14, r8d
-xor eax, eax
-jmp L
-nop word ptr [rax + rax]
-add rax, 1
-cmp r14, rax
-je L
-cmp dword ptr [rcx + rax*4], edx
-jne L
-mov rdi, rbx
-call F
-test rax, rax
-je L
-mov rdi, rbx
-call F
+mov dword ptr [rbp - 0xf8], 0xffffffff
 lea rdi, [rbp - 0xf8]
-mov dword ptr [rbp - 0xf8], 0xffffffff
-mov rsi, rax
 call F
 movsxd rdx, dword ptr [rbp - 0xf0]
 mov ecx, dword ptr [rbp - 0xf8]
+test edx, edx
+jle L
+mov rsi, qword ptr [rbp - 0xe8]
+xor eax, eax
+jmp L
+nop
+add rax, 1
+cmp rdx, rax
+je L
+cmp dword ptr [rsi + rax*4], ecx
+jne L
+mov rdi, rbx
+call F
+test rax, rax
+je L
+mov rdi, rbx
+call F
+lea rdi, [rbp - 0xf4]
+mov dword ptr [rbp - 0xf4], 0xffffffff
+mov rsi, rax
+call F
+movsxd rdx, dword ptr [rbp - 0xf0]
+mov ecx, dword ptr [rbp - 0xf4]
 test edx, edx
 jle L
@@ -268,6 +268,7 @@
 mov rdi, rbx
 mov qword ptr [rbp - 0xe8], 0
+lea r14, [rbp - 0xf0]
+mov qword ptr [rbp - 0xe0], 0
 lea r13, [rbp - 0xd0]
-mov qword ptr [rbp - 0xe0], 0
 call F
 mov rdi, rbx
@@ -279,5 +280,5 @@
 call F
 mov rdi, rbx
-movzx r14d, byte ptr [rax + 0x624]
+movzx r15d, byte ptr [rax + 0x624]
 call F
 mov rdi, rax
@@ -285,11 +286,11 @@
 push 0
```
(ещё 71 строк диффа: so-query.py fdiff libserver.so 0x4a6d9f0)

### изменена: 0x4a6b820 (1492 байт) CDOTA_Ability_Ogre_Magi_Smash::OnSpellStart | строки: "damage"; "duration"; "modifier_ogre_magi_smash_buff"; "Hero_OgreMagi.FireShield.Cast"; "Hero_OgreMagi.FireShield.Target"; "ogre_magi_multicast"; "modifier_ogre_magi_arcana"; "multicast_fireshield_aoe"
было: 0x4a7bce0 (1524 байт)
- числа в инструкциях: −1 −1
- инструкций: 327 → 319
```diff
@@ -82,5 +82,5 @@
 cmp byte ptr [rax + 0x7e1], 0
 jne L
-lea rsi, [rbp - 0xdc]
+lea rsi, [rbp - 0xd8]
 mov rdi, rax
 call F
@@ -96,5 +96,5 @@
 mov esi, dword ptr [rbp - 0x110]
 mov rdi, rax
-movss xmm0, dword ptr [rbp - 0xdc]
+movss xmm0, dword ptr [rbp - 0xd8]
 call F
 mov esi, dword ptr [rbp - 0x110]
@@ -137,5 +137,5 @@
 cvtsi2ss xmm0, eax
 lea rcx, [rbp - 0x70]
-mov qword ptr [rbp - 0x128], rcx
+mov qword ptr [rbp - 0x130], rcx
 movss dword ptr [rbp - 0x70], xmm0
 pxor xmm0, xmm0
@@ -164,5 +164,5 @@
 lea rax, [rbp - 0xb0]
 mov rsi, rax
-mov qword ptr [rbp - 0x130], rax
+mov qword ptr [rbp - 0x128], rax
 call F
 mov rdi, rbx
@@ -180,8 +180,8 @@
 mov rdi, rbx
 call F
+xor ecx, ecx
+mov edx, 2
 xor r8d, r8d
-xor ecx, ecx
-mov edx, 2
-mov rsi, qword ptr [rbp - 0x128]
+mov rsi, qword ptr [rbp - 0x130]
 mov rdi, rax
 movss xmm0, dword ptr [rbp - 0x118]
@@ -189,52 +189,42 @@
 mov rdi, rbx
 call F
-lea rdi, [rbp - 0xd8]
-mov dword ptr [rbp - 0xd8], 0xffffffff
-mov rsi, rax
-call F
-mov ecx, dword ptr [rbp - 0xd8]
+lea rdi, [rbp - 0xd4]
+mov dword ptr [rbp - 0xd4], 0xffffffff
+mov rsi, rax
+call F
 lea rax, [rbp - 0xd0]
-mov esi, 1
-lea rdi, [rbp - 0xc8]
-mov qword ptr [rbp - 0x120], rax
+mov rsi, rdi
+mov qword ptr [rbp - 0x120], rdi
+mov rdi, rax
+mov qword ptr [rbp - 0x118], rax
 mov qword ptr [rbp - 0xd0], 0
 mov qword ptr [rbp - 0xc8], 0
-mov dword ptr [rbp - 0x118], ecx
 mov qword ptr [rbp - 0xc0], 0
 call F
-mov ecx, dword ptr [rbp - 0x118]
-mov rdi, rbx
-mov edx, dword ptr [rbp - 0xd0]
-mov rax, qword ptr [rbp - 0xc8]
-add edx, 1
-mov dword ptr [rax], ecx
-mov dword ptr [rbp - 0x140], edx
-call F
-lea rdx, [rbp - 0xd4]
+mov rdi, rbx
+call F
+mov rdi, qword ptr [rbp - 0x120]
 mov dword ptr [rbp - 0xd4], 0xffffffff
 mov rsi, rax
-mov rdi, rdx
 call F
 mov rsi, rdi
-mov qword ptr [rbp - 0x118], rdi
-mov rdi, qword ptr [rbp - 0x130]
-call F
-mov edx, dword ptr [rbp - 0x140]
+mov qword ptr [rbp - 0x120], rdi
+mov rdi, qword ptr [rbp - 0x128]
+call F
+mov rsi, qword ptr [rbp - 0x128]
+mov rdi, qword ptr [rbp - 0x118]
+call F
+mov rsi, qword ptr [rbp - 0x138]
+mov rdi, qword ptr [rbp - 0x118]
+call F
 mov rsi, qword ptr [rbp - 0x130]
-mov rdi, qword ptr [rbp - 0x120]
-mov dword ptr [rbp - 0xd0], edx
-call F
-mov rsi, qword ptr [rbp - 0x138]
-mov rdi, qword ptr [rbp - 0x120]
-call F
-mov rsi, qword ptr [rbp - 0x128]
-mov rdi, qword ptr [rbp - 0x120]
-call F
-mov r11, qword ptr [rbp - 0x118]
+mov rdi, qword ptr [rbp - 0x118]
+call F
+mov r11, qword ptr [rbp - 0x120]
 mov rsi, r12
 mov dword ptr [rbp - 0xd4], 0xffffffff
 mov rdi, r11
 call F
-mov rdi, qword ptr [rbp - 0x120]
+mov rdi, qword ptr [rbp - 0x118]
 mov rsi, r11
 call F
@@ -246,5 +236,5 @@
 jle L
 lea rax, [r10 + rax*4]
```
(ещё 43 строк диффа: so-query.py fdiff libserver.so 0x4a6b820)
