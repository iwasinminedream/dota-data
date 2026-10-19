# Dota 6963: изменения кода по функциям

Снимки `6962-11135205` → `6963-11145455`; funcdiff.py. В диффе: [S:…] — строка, [K:…] — константа из данных, F — вызов другой функции, L — переход внутри функции, [D]/[T] — прочие адреса. Регистры и смещения стека меняются и от перекомпиляции.

## libclient.so: функций 280912 → 280912; без изменений 280906, изменено 2, добавлено 0, удалено 0

### изменена: 0x47e0990 (422 байт) C_DOTA_Ability_Tinker_Keen_Teleport::CastFilterResultTarget
было: 0x47e0990 (402 байт)
- виртуальные вызовы: +0xb10 (слот 354)
- прямых вызовов: 12 → 13
- инструкций: 106 → 112
```diff
@@ -25,4 +25,9 @@
 test al, al
 jne L
+mov rax, qword ptr [r12]
+mov rdi, r12
+call qword ptr [rax + 0xb10]
+test al, al
+je L
 mov rdi, rbx
 call F
@@ -69,11 +74,8 @@
 ret
 nop dword ptr [rax]
-mov r13d, 7
-mov r14d, 6
-jmp L
-nop dword ptr [rax]
 call rax
 test al, al
 je L
+nop word ptr [rax + rax]
 mov r13d, 0x17
 pop rbx
@@ -84,4 +86,8 @@
 pop rbp
 ret
+nop word ptr [rax + rax]
+mov r13d, 7
+mov r14d, 6
+jmp L
 nop dword ptr [rax]
 mov rdi, rbx
```

### изменена: 0x4811a20 (1484 байт) C_DOTA_Ability_Tinker_Keen_Teleport::vfunc#261 | строки: "creep_teleport_level"; "hero_teleport_level"
было: 0x48112d0 (1277 байт)
- константы из данных (числа логики): +810000 −inf
- числа в инструкциях: +0 +0 +0x10
- виртуальные вызовы: +0xb10 (слот 354) +0xb10 (слот 354)
- поля объектов: +0x557 +0xe0c
- прямых вызовов: 24 → 26
- инструкций: 319 → 361
```diff
@@ -12,6 +12,6 @@
 push rbx
 mov rbx, rdi
-sub rsp, 0x48
-mov qword ptr [rbp - 0x60], rsi
+sub rsp, 0x58
+mov qword ptr [rbp - 0x68], rsi
 movzx r13d, byte ptr [rdi + 0x557]
 lea rsi, [S:"creep_teleport_level"]
@@ -29,10 +29,10 @@
 call F
 mov rdi, rbx
-mov r15d, dword ptr [rbx + 0x824]
+mov r14d, dword ptr [rbx + 0x824]
 mov dword ptr [rbp - 0x58], eax
 call F
 mov edx, dword ptr [rbx + 0x828]
-mov dword ptr [rbp - 0x64], eax
-mov dword ptr [rbp - 0x68], edx
+mov dword ptr [rbp - 0x6c], eax
+mov dword ptr [rbp - 0x70], edx
 call F
 mov rdi, r12
@@ -47,100 +47,116 @@
 call F
 mov rdi, r12
-mov edx, dword ptr [rax + 0x450]
-mov dword ptr [rbp - 0x54], edx
-call F
-test rax, rax
-je L
-cmp dword ptr [rbp - 0x58], r15d
-mov r14, rax
+mov ecx, dword ptr [rax + 0x450]
+mov dword ptr [rbp - 0x60], ecx
+call F
+test rax, rax
+je L
+cmp dword ptr [rbp - 0x58], r14d
+mov r15, rax
+mov r14d, 0
+mov qword ptr [rbp - 0x58], 0
+movss xmm2, dword ptr [K:inf]
+movss dword ptr [rbp - 0x5c], xmm2
+movss dword ptr [rbp - 0x74], xmm2
 jge L
-movss xmm2, dword ptr [K:inf]
-xor r15d, r15d
-movss dword ptr [rbp - 0x58], xmm2
-jmp L
-nop dword ptr [rax]
-mov rdi, r12
-call F
-test rax, rax
-mov r14, rax
-je L
-cmp byte ptr [r14 + 0x557], r13b
-jne L
-mov rdi, rbx
-call F
-cmp r14, rax
-je L
-mov rax, qword ptr [r14]
-mov rdi, r14
+cmp r13b, byte ptr [r15 + 0x557]
+je L
+nop dword ptr [rax + rax]
+mov rdi, r12
+call F
+test rax, rax
+mov r15, rax
+je L
+cmp r13b, byte ptr [r15 + 0x557]
+jne L
+mov rdi, rbx
+call F
+cmp r15, rax
+je L
+mov rax, qword ptr [r15]
+mov rdi, r15
 call qword ptr [rax + 0xac0]
 test al, al
 jne L
-mov rax, qword ptr [r14]
-lea rdx, [T]
+mov rax, qword ptr [r15]
+mov rdi, r15
+call qword ptr [rax + 0xb10]
+test al, al
+je L
+mov rax, qword ptr [r15]
+lea rcx, [T]
 mov rax, qword ptr [rax + 0x4f8]
-cmp rax, rdx
-jne L
-cmp byte ptr [r14 + 0x4c4], 0
-jne L
-mov eax, dword ptr [r14 + 0xe0c]
+cmp rax, rcx
+jne L
+cmp byte ptr [r15 + 0x4c4], 0
+jne L
+mov eax, dword ptr [r15 + 0xe0c]
 test al, 0x10
-jne L
-mov edx, dword ptr [rbp - 0x68]
-cmp dword ptr [rbp - 0x64], edx
-jl L
-mov rcx, qword ptr [r14]
-lea rsi, [T]
-mov rcx, qword ptr [rcx + 0xa50]
-cmp rcx, rsi
-jne L
-test al, 1
-je L
-nop
-mov rdi, r14
-call F
-cmp dword ptr [rbp - 0x54], -1
-je L
```
(ещё 433 строк диффа: so-query.py fdiff libclient.so 0x4811a20)

### копии существующего кода (8): шаблонные / склеенные компоновщиком функции, такой же код есть и в другой сборке — не новый код
- ещё одна копия существующего кода: 0x47f3300 (117 байт) C_DOTA_Unit_Hero_Sniper::vfunc#49
- ещё одна копия существующего кода: 0x47f3380 (117 байт) C_DOTA_Ability_Sniper_Shrapnel::vfunc#49
- ещё одна копия существующего кода: 0x47f3400 (117 байт) C_DOTA_Ability_Sniper_Headshot::vfunc#49
- ещё одна копия существующего кода: 0x47f3480 (117 байт) C_DOTA_Ability_Sniper_TakeAim::vfunc#49
- одной копией существующего кода меньше: 0x47f3020 (92 байт) C_DOTA_Ability_Roshan_RevengeRoar::vfunc#49
- одной копией существующего кода меньше: 0x47f3080 (92 байт) C_DOTA_Unit_Roshan::vfunc#49
- одной копией существующего кода меньше: 0x47f30e0 (92 байт) C_DOTA_Unit_Scout::vfunc#49
- одной копией существующего кода меньше: 0x47f3140 (92 байт) C_DOTA_Unit_TargetDummy::vfunc#49

## libserver.so: функций 219999 → 220000; без изменений 219981, изменено 11, добавлено 0, удалено 0

### изменена: 0x4593b30 (294 байт) CDOTA_Ability_Tinker_Keen_Teleport::CastFilterResultTarget
было: 0x4593b30 (278 байт)
- виртуальные вызовы: +0xad8 (слот 347)
- прямых вызовов: 7 → 8
- инструкций: 75 → 75
```diff
@@ -17,4 +17,9 @@
 test al, al
 jne L
+mov rax, qword ptr [r12]
+mov rdi, r12
+call qword ptr [rax + 0xad8]
+test al, al
+je L
 mov eax, dword ptr [rbx + 0x7b0]
 cmp dword ptr [rbx + 0x85c], eax
@@ -54,13 +59,8 @@
 je L
 xor edx, edx
-pop rbx
 test byte ptr [r12 + 0xcd4], 2
-pop r12
-pop r13
-pop r14
 cmovne eax, edx
-pop rbp
-ret
-nop dword ptr [rax + rax]
+jmp L
+nop dword ptr [rax]
 mov r13d, 7
 mov r14d, 6
```

### изменена: 0x45f41c0 (1885 байт) CDOTA_Ability_Tinker_Rearm::OnChannelFinish | строки: "modifier_tinker_rearm"; "launch_missiles"; "item_blink"; "item_black_king_bar"; "doom_bringer_devour"; "tinker_heat_seeking_missile"; "<NoAbilityName>"; "item_phoenix_ash"
было: 0x45f4140 (1932 байт)
- строки: −"item_black_king_bar" −"item_black_king_bar"
- прямых вызовов: 77 → 75
- инструкций: 454 → 447
```diff
@@ -124,144 +124,10 @@
 je L
 lea rsi, [S:"item_black_king_bar"]
-mov rdi, r14
-call F
-test al, al
-jne L
-lea rsi, [S:"item_phoenix_ash"]
-mov rdi, r14
-call F
-test al, al
-jne L
-lea rsi, [S:"item_meteor_hammer"]
-mov rdi, r14
-call F
-test al, al
-jne L
-lea rsi, [S:"item_aeon_disk"]
-mov rdi, r14
-call F
-test al, al
-jne L
-lea rsi, [S:"item_arcane_boots"]
-mov rdi, r14
-call F
-test al, al
-jne L
-lea rsi, [S:"item_sphere"]
-mov rdi, r14
-call F
-test al, al
-jne L
-lea rsi, [S:"item_helm_of_the_dominator"]
-mov rdi, r14
-mov r15, r14
-call F
-test al, al
-jne L
-lea rsi, [S:"item_helm_of_the_overlord"]
-mov rdi, r15
-call F
-test al, al
-jne L
-lea rsi, [S:"item_hand_of_midas"]
-mov rdi, r15
-call F
-test al, al
-jne L
-lea rsi, [S:"item_refresher"]
-mov rdi, r15
-call F
-test al, al
-jne L
-lea rsi, [S:"item_refresher_shard"]
-mov rdi, r15
-call F
-test al, al
-jne L
-lea rsi, [S:"item_renewal_orb"]
-mov rdi, r15
-call F
-test al, al
-jne L
-lea rsi, [S:"item_pipe"]
-mov rdi, r15
-call F
-test al, al
-jne L
-lea rsi, [S:"item_necronomicon"]
-mov rdi, r15
-call F
-test al, al
-jne L
-lea rsi, [S:"item_necronomicon_2"]
-mov rdi, r15
-call F
-test al, al
-jne L
-lea rsi, [S:"item_necronomicon_3"]
-mov rdi, r15
-call F
-test al, al
-jne L
-test r14, r14
-jne L
-lea r14, [D]
-jmp L
-nop word ptr [rax + rax]
-mov rdi, qword ptr [rax]
-test rdi, rdi
-je L
-lea rsi, [S:"doom_bringer_devour"]
-cmp rdi, rsi
-je L
+cmp r14, rsi
+je L
+mov rdi, r14
 call F
 test eax, eax
-je L
-nop dword ptr [rax]
-mov rax, qword ptr [r12]
-lea rcx, [T]
-mov rdx, qword ptr [rax + 0x7e0]
-cmp rdx, rcx
-jne L
-mov rdi, r12
-call qword ptr [rax + 0x940]
-test al, al
-jne L
-mov rax, qword ptr [r12]
-mov rdi, r12
-call qword ptr [rax + 0x920]
-mov rdi, r12
-call F
-test al, al
-jne L
-nop dword ptr [rax]
-add r13d, 1
-mov rdi, rbx
```
(ещё 292 строк диффа: so-query.py fdiff libserver.so 0x45f41c0)

### изменена: 0x45f4aa0 (6175 байт) CDOTA_Ability_Tinker_Keen_Teleport::OnAbilityPhaseStart | строки: "maximum_distance"; "good_healer_6"; "npc_dota_watch_tower_bottom"; "npc_dota_watch_tower_top"; "tower1"; "minimum_distance"; "particles/items2_fx/teleport_start.vpcf"; "particles/items2_fx/teleport_end.vpcf"
было: 0x45f4a60 (5752 байт)
- константы из данных (числа логики): +0.1 +100 −0xffffffffffffffff
- числа в инструкциях: +4 +3 +3 +0x10 +5 −0xffffffff
- виртуальные вызовы: +0xbc0 (слот 376) +0xad8 (слот 347) +0xad8 (слот 347) +0xad8 (слот 347)
- поля объектов: +0x5d1 +0x5d1 +0xcd4 −0x878 −0x870
- прямых вызовов: 164 → 172
- инструкций: 1159 → 1256
```diff
@@ -2,14 +2,14 @@
 mov rbp, rsp
 push r15
+mov r15, rdi
 push r14
-mov r14d, 4
 push r13
-mov r13, rdi
 push r12
 push rbx
-sub rsp, 0x308
+sub rsp, 0x318
+mov qword ptr [rbp - 0x2d8], rdi
 call F
 lea rax, [D]
-mov rdi, r13
+mov rdi, r15
 movq qword ptr [rbp - 0x2b8], xmm0
 movss dword ptr [rbp - 0x2b0], xmm1
@@ -25,10 +25,10 @@
 movaps xmm1, xmm3
 subss xmm1, dword ptr [rbp - 0x278]
-movss dword ptr [rbp - 0x2e8], xmm3
+movss dword ptr [rbp - 0x2f8], xmm3
 movq xmm5, rax
-mov qword ptr [rbp - 0x2e0], rax
+mov qword ptr [rbp - 0x2e8], rax
 movaps xmm4, xmm5
 subss xmm4, dword ptr [rbp - 0x27c]
-mov dword ptr [rbp - 0x2f0], eax
+mov dword ptr [rbp - 0x310], eax
 mulss xmm1, xmm1
 movaps xmm0, xmm4
@@ -37,6 +37,6 @@
 movd eax, xmm0
 movd xmm0, eax
-mov eax, dword ptr [r13 + 0x7b0]
-cmp dword ptr [r13 + 0x85c], eax
+mov eax, dword ptr [r15 + 0x7b0]
+cmp dword ptr [r15 + 0x85c], eax
 sqrtss xmm0, xmm0
 jg L
@@ -44,13 +44,15 @@
 comiss xmm1, xmm0
 jbe L
+mov r12d, 4
+xor ebx, ebx
+mov r13, qword ptr [rbp - 0x2d8]
 movabs rax, 0x8000000000000040
-mov rdi, r13
 mov qword ptr [rbp - 0x150], 0
-lea r15, [rbp - 0x150]
+lea r14, [rbp - 0x150]
 mov qword ptr [rbp - 0x140], rax
 lea rax, [rbp - 0x138]
-mov qword ptr [rbp - 0x2d8], r15
-mov qword ptr [rbp - 0x300], rax
-lea rbx, [rbp - 0x210]
+mov qword ptr [rbp - 0x2e0], r14
+mov qword ptr [rbp - 0x320], rax
+mov rdi, r13
 mov qword ptr [rbp - 0x148], rax
 call F
@@ -60,17 +62,20 @@
 call F
 mov rdi, r13
-movzx r12d, byte ptr [rax + 0x624]
-call F
-push 0
+movzx r15d, byte ptr [rax + 0x624]
+call F
 xor ecx, ecx
 mov r9d, 1
+mov r8, r14
 movss xmm0, dword ptr [K:-1]
 mov rdi, rax
+lea rax, [rbp - 0x210]
+mov qword ptr [rbp - 0x2f0], rax
+mov rdx, rax
+mov esi, r15d
 push 0
-mov r8, r15
+push 0
 push 0x50
-mov rdx, rbx
-mov esi, r12d
-push r14
+push r12
+mov r12, rax
 call F
 add rsp, 0x20
@@ -78,6 +83,6 @@
 call F
 xor edx, edx
-mov rsi, rbx
-mov rdi, r15
+mov rsi, r12
+mov rdi, r14
 movq qword ptr [rbp - 0x210], xmm0
 movss dword ptr [rbp - 0x208], xmm1
@@ -86,14 +91,10 @@
 test eax, eax
 jle L
-mov r14, qword ptr [rbp - 0x148]
-lea r12, [r14 + rax*4]
-jmp L
-nop word ptr cs:[rax + rax]
-nop word ptr cs:[rax + rax]
-nop dword ptr [rax]
-add r14, 4
-cmp r12, r14
-je L
-mov eax, dword ptr [r14]
+test rbx, rbx
+je L
+mov r15, qword ptr [rbp - 0x148]
+lea r12, [r15 + rax*4]
+nop word ptr [rax + rax]
+mov eax, dword ptr [r15]
 cmp eax, -1
```
(ещё 1438 строк диффа: so-query.py fdiff libserver.so 0x45f4aa0)

### изменена: 0x4614130 (2108 байт) CDOTA_Unit_Roshan::Spawn | строки: "particles/neutral_fx/roshan_spawn.vpcf"; "attach_hitloc"; "modifier_phased"; "roshan_location_1"; "roshan_location_2"; "roshan_midpoint"; "CNetworkTransmitComponent::StateChanged(%s) @%s:%d"
было: 0x4611650 (2092 байт)
- числа в инструкциях: +1 +1
- инструкций: 436 → 437
```diff
@@ -297,13 +297,10 @@
 cmp byte ptr [rbx + 0x1ca8], 0
 jne L
+lea rdi, [rbp - 0x130]
+mov esi, 1
 xor r14d, r14d
-mov rsi, r12
 pxor xmm0, xmm0
-mov dword ptr [rbp - 0x180], 0x1ca8
-mov word ptr [rbp - 0x104], r14w
-lea r14, [rbp - 0x138]
-mov rdi, r14
+mov qword ptr [rbp - 0x140], 1
 movaps xmmword ptr [rbp - 0x120], xmm0
-mov qword ptr [rbp - 0x140], 1
 mov qword ptr [rbp - 0x138], 0
 mov qword ptr [rbp - 0x130], 0
@@ -311,14 +308,18 @@
 mov qword ptr [rbp - 0x110], 0xffffffffffffffff
 mov dword ptr [rbp - 0x108], 0xffffffff
-call F
+mov word ptr [rbp - 0x104], r14w
+call F
+mov rax, qword ptr [rbp - 0x130]
+mov rsi, r13
+mov rdi, rbx
+add dword ptr [rbp - 0x138], 1
+mov dword ptr [rax], 0x1ca8
 mov rax, qword ptr [rbx]
-mov rsi, r13
-mov rdi, rbx
 call qword ptr [rax + 0xe8]
-mov rdi, r14
+lea rdi, [rbp - 0x138]
 call F
 mov byte ptr [rbx + 0x1ca8], 1
 jmp L
-nop dword ptr [rax]
+nop word ptr cs:[rax + rax]
 xor eax, eax
 mov esi, 1
```

### изменена: 0x461bcb0 (1092 байт) CDOTA_Unit_Roshan::vfunc#262 | строки: "Spectator.RoshanFightToggle"
было: 0x461bab0 (1086 байт)
- числа в инструкциях: +1 +1 +1 +1
- инструкций: 263 → 262
```diff
@@ -1,5 +1,4 @@
 push rbp
 mov rbp, rsp
-push r15
 push r14
 push r13
@@ -8,5 +7,5 @@
 mov r12, rdi
 push rbx
-sub rsp, 0x68
+sub rsp, 0x60
 call F
 mov eax, dword ptr [r12 + 0x1c7c]
@@ -70,8 +69,8 @@
 cmp ecx, -1
 je L
+mov rdx, qword ptr [D]
+test rdx, rdx
+je L
 cmp ecx, -2
-mov rdx, qword ptr [D]
-je L
-test rdx, rdx
 je L
 movzx eax, word ptr [rax + 0x3c]
@@ -99,13 +98,11 @@
 cmp rax, rdx
 jne L
-add rsp, 0x68
+add rsp, 0x60
 pop rbx
 pop r12
 pop r13
 pop r14
-pop r15
 pop rbp
 ret
-nop dword ptr [rax]
 mov rdi, rbx
 call rax
@@ -137,5 +134,5 @@
 xor eax, eax
 jmp L
-nop
+nop word ptr [rax + rax]
 add rax, 1
 cmp rax, rcx
@@ -145,5 +142,5 @@
 jmp L
 nop dword ptr [rax + rax]
-lea rbx, [rbp - 0x70]
+lea rbx, [rbp - 0x60]
 mov rdi, rbx
 call F
@@ -164,11 +161,11 @@
 test rax, rax
 je L
-lea rdi, [rbp - 0x78]
+lea rdi, [rbp - 0x64]
 mov rsi, rbx
-mov dword ptr [rbp - 0x78], 0xffffffff
+mov dword ptr [rbp - 0x64], 0xffffffff
 call F
 movsxd r13, dword ptr [r12 + 0x1c90]
 cmp r13d, dword ptr [r12 + 0x1ca0]
-mov r14d, dword ptr [rbp - 0x78]
+mov r14d, dword ptr [rbp - 0x64]
 mov eax, r13d
 je L
@@ -204,54 +201,56 @@
 je L
 mov rdx, qword ptr [K:0x00000003ffffffff]
-lea rbx, [rbp - 0x68]
-mov qword ptr [rbp - 0x88], rax
+mov qword ptr [rbp - 0x78], rax
+lea rdi, [rbp - 0x50]
 xor eax, eax
-lea rsi, [rbp - 0x74]
-mov rdi, rbx
-mov word ptr [rbp - 0x34], ax
+mov esi, 1
+mov word ptr [rbp - 0x24], ax
 pxor xmm0, xmm0
-mov dword ptr [rbp - 0x74], 0xb3c
-lea r12, [rbp - 0x70]
-movaps xmmword ptr [rbp - 0x50], xmm0
-mov qword ptr [rbp - 0x40], rdx
-mov qword ptr [rbp - 0x70], 1
-mov qword ptr [rbp - 0x68], 0
-mov qword ptr [rbp - 0x60], 0
+mov qword ptr [rbp - 0x60], 1
+lea rbx, [rbp - 0x60]
+movaps xmmword ptr [rbp - 0x40], xmm0
+mov qword ptr [rbp - 0x30], rdx
 mov qword ptr [rbp - 0x58], 0
-mov dword ptr [rbp - 0x38], 0xffffffff
-call F
+mov qword ptr [rbp - 0x50], 0
+mov qword ptr [rbp - 0x48], 0
+mov dword ptr [rbp - 0x28], 0xffffffff
+call F
+mov rdx, qword ptr [rbp - 0x50]
+mov rsi, rbx
+mov rdi, r13
+add dword ptr [rbp - 0x58], 1
+mov dword ptr [rdx], 0xb3c
 mov rdx, qword ptr [r13]
-mov rsi, r12
+call qword ptr [rdx + 0xe8]
+lea rdi, [rbp - 0x58]
+call F
+mov rax, qword ptr [rbp - 0x78]
+mov dword ptr [r13 + 0xb48], eax
+jmp L
+mov eax, 0x7fff
+jmp L
+lea rdi, [rbp - 0x50]
+xor edx, edx
+mov rax, qword ptr [K:0x00000002ffffffff]
+mov esi, 1
```
(ещё 49 строк диффа: so-query.py fdiff libserver.so 0x461bcb0)

### изменена: 0x462dde0 (2512 байт) CDOTA_Unit_Miniboss::vfunc#128 | строки: "particles/neutral_fx/miniboss_death_dire.vpcf"; "particles/neutral_fx/miniboss_death.vpcf"; "attach_core_fx"; "Miniboss.Tormenter.Death"; "dota_ancient_decoration_event"; "entindex"; "teamnumber"; "eventname"
было: 0x462dbe0 (3289 байт)
- числа в инструкциях: −1 −1 −1 −3 −3 −3 −0 −0 (и ещё 21)
- поля объектов: −0x10 −0x1a −0x1c −0x20 −0x20
- прямых вызовов: 52 → 45
- инструкций: 742 → 552
```diff
@@ -515,15 +515,12 @@
 jmp L
 nop dword ptr [rax + rax]
-lea rax, [rbp - 0x68]
+lea rdi, [rbp - 0x60]
 xor r12d, r12d
-movss dword ptr [rbp - 0xf8], xmm0
 pxor xmm1, xmm1
+mov esi, 1
+movss dword ptr [rbp - 0xe8], xmm0
+movaps xmmword ptr [rbp - 0x50], xmm1
 mov word ptr [rbp - 0x34], r12w
 lea r12, [rbp - 0x70]
-mov rdi, rax
-lea rsi, [rbp - 0xc0]
-movaps xmmword ptr [rbp - 0x50], xmm1
-mov qword ptr [rbp - 0xe8], rax
-mov dword ptr [rbp - 0xc0], 0x38
 mov qword ptr [rbp - 0x70], 1
 mov qword ptr [rbp - 0x68], 0
@@ -533,10 +530,13 @@
 mov dword ptr [rbp - 0x38], 0xffffffff
 call F
+mov rax, qword ptr [rbp - 0x60]
 mov rsi, r12
 mov rdi, r13
-call F
-mov rdi, qword ptr [rbp - 0xe8]
-call F
-movss xmm0, dword ptr [rbp - 0xf8]
+add dword ptr [rbp - 0x68], 1
+mov dword ptr [rax], 0x38
+call F
+lea rdi, [rbp - 0x68]
+call F
+movss xmm0, dword ptr [rbp - 0xe8]
 movss dword ptr [rbp - 0x78], xmm0
 jmp L
@@ -545,5 +545,5 @@
 jns L
 jmp L
-nop word ptr [rax + rax]
+nop dword ptr [rax]
 mov dword ptr [rbp - 0xe8], 0
 xor ebx, ebx
@@ -551,192 +551,2 @@
 jmp L
 jmp F
-push rbp
-mov rbp, rsp
-push r15
-push r14
-push r13
-push r12
-mov r12, rdx
-push rbx
-sub rsp, 0xb8
-mov qword ptr [rbp - 0xc8], rdi
-mov rdi, rsi
-call F
-mov rbx, rax
-mov eax, dword ptr [r12]
-test rbx, rbx
-mov dword ptr [rbp - 0xd0], eax
-je L
-mov rdi, rbx
-call F
-mov r13, rax
-mov r14d, eax
-xor r13d, 0x3501a674
-lea r12, [rbp - 0xc0]
-xor r8d, r8d
-xor esi, esi
-mov qword ptr [rbp - 0xb8], 0
-movabs rax, 0xc000008000000000
-mov ecx, r14d
-mov rdx, rbx
-mov rdi, r12
-mov qword ptr [rbp - 0xc0], rax
-call F
-xor esi, esi
-mov rdi, r12
-call F
-test byte ptr [rbp - 0xb9], 0x40
-lea rax, [rbp - 0xb8]
-jne L
-test dword ptr [rbp - 0xbc], 0x3fffffff
-lea rax, [D]
-jne L
-cmp r14d, 3
-jle L
-lea edi, [r14 - 4]
-shr r14d, 2
-lea esi, [r14*4]
-lea r8d, [r14 - 1]
-add rsi, rax
-nop word ptr cs:[rax + rax]
-nop word ptr cs:[rax + rax]
-nop word ptr cs:[rax + rax]
-nop word ptr cs:[rax + rax]
-imul edx, dword ptr [rax], 0x5bd1e995
-add rax, 4
-imul r13d, r13d, 0x5bd1e995
-mov ecx, edx
-shr ecx, 0x18
-xor edx, ecx
-imul edx, edx, 0x5bd1e995
-xor r13d, edx
-cmp rax, rsi
-jne L
-shl r8d, 2
-sub edi, r8d
-mov r14d, edi
-cmp r14d, 2
-je L
-cmp r14d, 3
-je L
-cmp r14d, 1
-je L
-jmp L
```
(ещё 118 строк диффа: so-query.py fdiff libserver.so 0x462dde0)

### изменена: 0x4642be0 (444 байт) | строки: "CDOTA_Ability_Sniper_Concussive_Grenade"
было: 0x46429e0 (444 байт)
- числа в инструкциях: +0x5bd1e995 +0x2af99bb2
- прямых вызовов: 12 → 11
- инструкций: 97 → 95
```diff
@@ -63,9 +63,7 @@
 mov esi, eax
 call F
-lea rdi, [r14 + 0x20]
-mov esi, eax
-call F
 lea rdi, [r14 + 0x24]
-mov esi, eax
+imul esi, eax, 0x5bd1e995
+xor esi, 0x2af99bb2
 call F
 lea rcx, [rbp - 0x24]
@@ -84,5 +82,5 @@
 call F
 jmp L
-nop word ptr [rax + rax]
+nop word ptr cs:[rax + rax]
 lea rdi, [D]
 mov esi, 1
```

### изменена: 0x492c920 (1862 байт) CDOTA_Ability_EmberSpirit_Activate_FireRemnant::vfunc#371 | строки: "damage"; "radius"; "modifier_ember_spirit_fire_remnant_remnant_tracker"; "Hero_EmberSpirit.FireRemnant.Explode"; "modifier_ember_spirit_fire_remnant"; "modifier_ember_spirit_fire_remnant_timer"
было: 0x492c720 (1809 байт)
- числа в инструкциях: +0xffffffff +1 +-1 +0xf +0xf +0x7fff +0x7fff
- поля объектов: +0x10 +0x10 +0x10 +0x10 +0x894 +0x894 +0x30
- прямых вызовов: 56 → 55
- инструкций: 440 → 457
```diff
@@ -8,5 +8,5 @@
 push rbx
 mov rbx, rdi
-sub rsp, 0x88
+sub rsp, 0x78
 call F
 test rax, rax
@@ -28,5 +28,5 @@
 pop rbp
 ret
-nop dword ptr [rax]
+nop word ptr [rax + rax]
 lea rsi, [S:"damage"]
 xor edx, edx
@@ -36,14 +36,12 @@
 mov rdi, rbx
 lea rsi, [S:"radius"]
-movss dword ptr [rbp - 0xac], xmm0
+movss dword ptr [rbp - 0xa0], xmm0
 call F
 mov rax, qword ptr [r12 + 0xc]
+lea rdi, [rbx + 0x894]
 movss dword ptr [rbp - 0x98], xmm0
 mov qword ptr [rbp - 0x5c], rax
 mov eax, dword ptr [r12 + 0x14]
 mov dword ptr [rbp - 0x54], eax
-lea rax, [rbx + 0x894]
-mov rdi, rax
-mov qword ptr [rbp - 0xa0], rax
 call F
 test rax, rax
@@ -85,5 +83,5 @@
 xor eax, eax
 jmp L
-nop word ptr cs:[rax + rax]
+nop dword ptr [rax]
 add rax, 1
 cmp rax, rsi
@@ -124,8 +122,9 @@
 call F
 mov rdi, rbx
-mov qword ptr [rbp - 0xa8], rax
-call F
-mov rdi, rbx
-movzx r15d, byte ptr [rax + 0x624]
+mov r15, rax
+call F
+mov rdi, rbx
+movzx esi, byte ptr [rax + 0x624]
+mov dword ptr [rbp - 0x9c], esi
 call F
 mov rdi, rax
@@ -137,8 +136,8 @@
 mov rdi, rax
 mov r9d, 2
-mov esi, r15d
+mov rcx, r15
 push 0
 push 3
-mov rcx, qword ptr [rbp - 0xa8]
+mov esi, dword ptr [rbp - 0x9c]
 movss xmm0, dword ptr [rbp - 0x98]
 call F
@@ -204,17 +203,16 @@
 mov dword ptr [rbx + 0x894], 0xffffffff
 je L
-mov edx, dword ptr [r13 + 0x1aa8]
-test edx, edx
-je L
-sub edx, 1
-mov r15d, edx
+mov r15d, dword ptr [r13 + 0x1aa8]
+test r15d, r15d
+je L
+sub r15d, 1
 js L
-movsxd r8, edx
+movsxd rcx, r15d
 mov rdi, qword ptr [r13 + 0x1ab0]
 lea rax, [r13 + 0x1aa8]
-lea r12, [r8*4]
+lea r12, [rcx*4]
 mov qword ptr [rbp - 0x98], rax
 jmp L
-nop
+nop dword ptr [rax]
 sub r15d, 1
 sub r12, 4
@@ -222,11 +220,11 @@
 je L
 lea rax, [rdi + r12]
-mov ecx, dword ptr [rax]
-cmp ecx, -1
-je L
-mov r9, qword ptr [D]
-test r9, r9
-je L
-cmp ecx, -2
+mov edx, dword ptr [rax]
+cmp edx, -1
+je L
+mov r8, qword ptr [D]
+test r8, r8
+je L
+cmp edx, -2
 je L
 movzx eax, word ptr [rax]
@@ -234,10 +232,10 @@
 shr rsi, 9
 and esi, 0x3f
-mov rsi, qword ptr [r9 + rsi*8]
+mov rsi, qword ptr [r8 + rsi*8]
 test rsi, rsi
 je L
 and eax, 0x1ff
 imul rax, rax, 0x70
-cmp ecx, dword ptr [rsi + rax + 0x10]
+cmp edx, dword ptr [rsi + rax + 0x10]
 je L
 mov rdi, qword ptr [rbp - 0x98]
```
(ещё 70 строк диффа: so-query.py fdiff libserver.so 0x492c920)

### изменена: 0x492dcc0 (3273 байт) CDOTA_Modifier_Dawnbreaker_Solar_Guardian_Thinker::OnIntervalThink | строки: "particles/units/heroes/hero_dawnbreaker/dawnbreaker_solar_guardian_damage.vpcf"; "attach_hitloc"; "miss_rate"; "particles/units/heroes/hero_dawnbreaker/dawnbreaker_solar_guardian_healing_buff."; "modifier_dawnbreaker_solar_guardian_evasion"; "duration"; "particles/units/heroes/hero_dawnbreaker/dawnbreaker_solar_guardian_damage_hit.vp"; "Hero_Dawnbreaker.Solar_Guardian.Damage"
было: 0x492da80 (3145 байт)
- числа в инструкциях: +1 +0 +3 +3
- поля объектов: +0x5d1 +0x5d1 +0xcd4 +0x16d2 +0xd48
- прямых вызовов: 82 → 81
- инструкций: 653 → 676
```diff
@@ -200,7 +200,8 @@
 test eax, eax
 jle L
-lea r15, [r12 + rax*4]
+lea r14, [r12 + rax*4]
 mov qword ptr [rbp - 0x1b0], r12
-nop dword ptr [rax]
+mov r15, r14
+nop
 mov ecx, dword ptr [r12]
 cmp ecx, -1
@@ -343,12 +344,12 @@
 mov qword ptr [rbp - 0x170], r12
 movsxd rax, dword ptr [rbp - 0x174]
-mov r14, rcx
+mov r15, rcx
 lea r13, [rcx + rax*4]
 jmp L
 nop dword ptr [rax + rax]
-add r14, 4
-cmp r14, r13
-je L
-mov ecx, dword ptr [r14]
+add r15, 4
+cmp r15, r13
+je L
+mov ecx, dword ptr [r15]
 cmp ecx, -1
 je L
@@ -358,5 +359,5 @@
 cmp ecx, -2
 je L
-movzx eax, word ptr [r14]
+movzx eax, word ptr [r15]
 mov rdx, rax
 shr rdx, 9
@@ -380,5 +381,5 @@
 call F
 mov rdi, rbx
-mov r15, rax
+mov r14, rax
 call F
 movss xmm3, dword ptr [K:1]
@@ -387,5 +388,5 @@
 movq xmm1, qword ptr [K:0x0000000000000000]
 mov rdi, rax
-mov rdx, r15
+mov rdx, r14
 mov rsi, r12
 movss xmm2, dword ptr [K:0]
@@ -417,27 +418,37 @@
 test ecx, ecx
 jle L
-mov rdi, r12
+cmp byte ptr [r12 + 0x5d1], 3
+mov r14, r12
+jne L
+mov rdi, rbx
 mov dword ptr [rbp - 0x1a8], ecx
 call F
-mov rdi, rbx
-mov r15, rax
-call F
-mov rdi, rax
-call F
+mov ecx, dword ptr [rbp - 0x1a8]
+test rax, rax
+mov rdi, rax
+je L
+cmp byte ptr [rax + 0x5d1], 3
+jne L
+test byte ptr [rax + 0xcd4], 1
+jne L
+mov rax, qword ptr [rax]
+lea rdx, [T]
+mov rax, qword ptr [rax + 0xd48]
+cmp rax, rdx
+jne L
+xor edi, edi
 xor r9d, r9d
 xor r8d, r8d
 mov edx, 0x33e
-mov ecx, dword ptr [rbp - 0x1a8]
-mov rdi, rax
-mov rsi, r15
-call F
-nop dword ptr [rax]
-call F
-mov rdi, rbx
-mov r15, rax
+mov rsi, r14
+call F
+nop word ptr [rax + rax]
+call F
+mov rdi, rbx
+mov r14, rax
 call F
 mov rsi, qword ptr [rbp - 0x168]
 lea rcx, [S:"particles/units/heroes/hero_dawnbreaker/dawnbreaker_solar_guardian_damage_hit.vpcf"]
-mov rdi, r15
+mov rdi, r14
 mov qword ptr [rbp - 0xb0], rax
 mov rax, qword ptr [K:0x00000000ffffffff]
@@ -466,5 +477,5 @@
 mov dword ptr [rbp - 0x40], 0x7f7fffff
 call F
-mov r15d, eax
+mov r14d, eax
 mov rax, qword ptr [rbp - 0x58]
 test rax, rax
@@ -481,12 +492,12 @@
 push 1
 mov rdi, rax
-mov esi, r15d
+mov esi, r14d
 lea r9, [S:"attach_hitloc"]
 mov edx, 1
-add r14, 4
+add r15, 4
 movq xmm0, qword ptr [K:0x7f7fffff7f7fffff]
```
(ещё 49 строк диффа: so-query.py fdiff libserver.so 0x492dcc0)

### изменена: 0x4940140 (1441 байт) CDOTA_Ability_Hoodwink_Decoy::OnSpellStart | строки: "Hero_Hoodwink.Scurry.Cast"; "duration"; "decoy_stun_duration"; "decoy_detonate_radius"; "projectile_speed"; "modifier_illusion"; "images_do_damage_percent"; "outgoing_damage"
было: 0x493fe80 (1425 байт)
- виртуальные вызовы: +0x920 (слот 292)
- прямых вызовов: 43 → 44
- инструкций: 323 → 327
```diff
@@ -171,4 +171,7 @@
 mov rdi, r15
 call qword ptr [rax + 0x7a8]
+mov rax, qword ptr [r15]
+mov rdi, r15
+call qword ptr [rax + 0x920]
 mov rax, qword ptr [r15]
 mov esi, 0xffffffff
@@ -313,4 +316,5 @@
 pop rbp
 ret
+nop dword ptr [rax]
 lea rdi, [rbp - 0x68]
 mov esi, 1
```

### изменена: 0x49fdbe0 (2342 байт) вызывается из: CDOTA_Modifier_Legion_Commander_Duel::vfunc#95 | строки: "modifier_legion_commander_duel"; "modifier_legion_commander_duel_damage_boost"; "particles/units/heroes/hero_legion_commander/legion_commander_duel_victory.vpcf"; "particles/units/heroes/hero_legion_commander/legion_commander_duel_body.vpcf"; "attach_hitloc"; "particles/econ/items/legion/legion_weapon_voth_domosh/legion_commander_duel_arca"; "Hero_LegionCommander.Duel.Victory"; "legion_commander_press_the_attack"
было: 0x49fd920 (2314 байт)
- строки: +"modifier_legion_commander_duel_damage_boost" +"modifier_legion_commander_duel_damage_boost"
- инструкций: 505 → 507
```diff
@@ -40,39 +40,35 @@
 call F
 test rax, rax
-mov r15, rax
-je L
-test byte ptr [rax + 0xcd4], 1
-je L
-cmp byte ptr [rax + 0x16d2], 0
-jne L
+mov r13, rax
+je L
 lea rdi, [r12 + 0x1acc]
 call F
 test rax, rax
 je L
-mov r13, qword ptr [rax]
-test r13, r13
-je L
-cmp byte ptr [r13 + 0x5d1], 3
-jne L
-mov rdi, r12
-call F
-cmp r15, rax
-je L
-cmp r15, r13
-jne L
+mov r14, qword ptr [rax]
+test r14, r14
+je L
+cmp byte ptr [r14 + 0x5d1], 3
+jne L
+mov rdi, r12
+call F
+cmp r13, rax
+je L
+cmp r13, r14
+jne L
+pxor xmm0, xmm0
 mov ecx, 0xffffffff
-pxor xmm0, xmm0
+movabs rax, 0xffffffff00000000
+movabs rsi, 0x10000000000
+mov qword ptr [rbp - 0x348], rax
+lea rdx, [rbp - 0x350]
+mov qword ptr [rbp - 0x328], rax
+lea rdi, [r13 + 0x1300]
+movabs rax, 0xffff00000000
 movups xmmword ptr [rbp - 0x2d8], xmm0
-movabs rax, 0xffffffff00000000
 movdqa xmm0, xmmword ptr [K:0x00000000000000000000000100000000]
-mov qword ptr [rbp - 0x348], rax
-movabs rdx, 0x10000000000
+mov qword ptr [rbp - 0x350], rcx
+mov qword ptr [rbp - 0x338], rsi
 mov esi, 0x7c
-mov qword ptr [rbp - 0x328], rax
-lea rdi, [r15 + 0x1300]
-movabs rax, 0xffff00000000
-mov qword ptr [rbp - 0x350], rcx
-mov qword ptr [rbp - 0x338], rdx
-lea rdx, [rbp - 0x350]
 mov qword ptr [rbp - 0x320], rcx
 xor ecx, ecx
@@ -104,75 +100,66 @@
 comiss xmm1, xmm0
 ja L
+mov rax, qword ptr [r13]
+mov rdi, r13
+call qword ptr [rax + 0xd50]
+test al, al
+jne L
+test byte ptr [r13 + 0xcd4], 1
+je L
+cmp byte ptr [r13 + 0x16d2], 0
+jne L
+mov rdi, r12
+call F
+cmp r13, rax
+je L
+mov rdi, r12
+call F
+test rax, rax
+mov r14, rax
+je L
+test byte ptr [r14 + 0xcd4], 1
+je L
+cmp byte ptr [r14 + 0x16d2], 0
+jne L
+xor ecx, ecx
+xor edx, edx
+mov rdi, r14
+mov byte ptr [r12 + 0x1ac5], 1
+lea rsi, [S:"modifier_legion_commander_duel"]
+call F
+lea rax, [rbp - 0x370]
+xor ecx, ecx
+xor edx, edx
+mov rdi, rax
+mov qword ptr [rbp - 0x3a0], rax
+lea rsi, [S:"modifier_legion_commander_duel_damage_boost"]
+call F
+xor edx, edx
+mov rdi, r14
+lea rsi, [S:"modifier_legion_commander_duel_damage_boost"]
+call F
+test rax, rax
+mov r15, rax
+je L
 mov rax, qword ptr [r15]
 mov rdi, r15
-call qword ptr [rax + 0xd50]
-test al, al
-je L
-lea r14, [S:"modifier_legion_commander_duel"]
-xor ecx, ecx
-xor edx, edx
-mov rsi, r14
-mov rdi, r13
-call F
-mov rdi, r12
```
(ещё 394 строк диффа: so-query.py fdiff libserver.so 0x49fdbe0)

### копии существующего кода (15): шаблонные / склеенные компоновщиком функции, такой же код есть и в другой сборке — не новый код
- ещё одна копия существующего кода: 0x45c7620 (92 байт) CDOTA_Ability_WitchDoctor_DeathWard::vfunc#49
- ещё одна копия существующего кода: 0x45c7680 (92 байт) CDOTA_Ability_WitchDoctor_Voodoo_Switcheroo::vfunc#49
- ещё одна копия существующего кода: 0x45c76e0 (92 байт) CDOTA_Ability_Witch_Doctor_Innate_Voodoo_Jinx::vfunc#49
- ещё одна копия существующего кода: 0x45c7740 (92 байт) CDOTA_Ability_Witch_Doctor_Innate_Maledict_Heal_Reduction::vfunc#49
- ещё одна копия существующего кода: 0x45c77a0 (92 байт) CDOTA_Ability_Witch_Doctor_GrisGris::vfunc#49
- ещё одна копия существующего кода: 0x45c7800 (92 байт) CDOTA_Item_GrisGris::vfunc#49
- ещё одна копия существующего кода: 0x45c7860 (92 байт) CDOTA_Unit_LoopingSound::vfunc#49
- ещё одна копия существующего кода: 0x462e7c0 (761 байт)
- одной копией существующего кода меньше: 0x45b9c90 (67 байт) CDOTA_Ability_Roshan_Slam::vfunc#49
- одной копией существующего кода меньше: 0x45b9ce0 (67 байт) CDOTA_Ability_Roshan_InherentBuffs::vfunc#49
- одной копией существующего кода меньше: 0x45b9d30 (67 байт) CDOTA_Ability_Roshan_Devotion::vfunc#49
- одной копией существующего кода меньше: 0x45b9d80 (67 байт) CDOTA_Ability_Roshan_RevengeRoar::vfunc#49
- одной копией существующего кода меньше: 0x45b9dd0 (67 байт) CDOTA_Unit_Roshan::vfunc#49
- одной копией существующего кода меньше: 0x45b9e20 (67 байт) CDOTA_Unit_Scout::vfunc#49
- одной копией существующего кода меньше: 0x45b9e70 (67 байт) CDOTA_Unit_TargetDummy::vfunc#49
