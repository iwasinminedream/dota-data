# Dota 6969: изменения кода по функциям

Снимки `6968-11170778` → `6969-11175759`; funcdiff.py. В диффе: [S:…] — строка, [K:…] — константа из данных, F — вызов другой функции, L — переход внутри функции, [D]/[T] — прочие адреса. Регистры и смещения стека меняются и от перекомпиляции.

## libclient.so: функций 280912 → 280912; без изменений 280908, изменено 4, добавлено 0, удалено 0

### изменена: 0x474b7e0 (39 байт) CDOTA_Modifier_Special_Bonus_Unique_Beastmaster_5_Aura::GetAuraRadius
было: 0x473d960 (9 байт)
- виртуальные вызовы: +0xe18 (слот 451)
- прямых вызовов: 0 → 2
- инструкций: 2 → 12
```diff
@@ -1,2 +1,12 @@
+push rbp
+mov rbp, rsp
+call F
+mov rdi, rax
+mov rax, qword ptr [rax]
+call qword ptr [rax + 0xe18]
 movss xmm0, dword ptr [K:-1]
+test al, al
+je L
+pxor xmm0, xmm0
+pop rbp
 ret
```

### изменена: 0x474b7b0 (39 байт) CDOTA_Modifier_Special_Bonus_Unique_Beastmaster_6_Aura::GetAuraRadius
было: 0x473db10 (9 байт)
- виртуальные вызовы: +0xe18 (слот 451)
- прямых вызовов: 0 → 2
- инструкций: 2 → 12
```diff
@@ -1,2 +1,12 @@
+push rbp
+mov rbp, rsp
+call F
+mov rdi, rax
+mov rax, qword ptr [rax]
+call qword ptr [rax + 0xe18]
 movss xmm0, dword ptr [K:-1]
+test al, al
+je L
+pxor xmm0, xmm0
+pop rbp
 ret
```

### изменена: 0x47b30a0 (460 байт) | строки: "C_DOTA_Ability_Riki_Backstab"
было: 0x47b3060 (452 байт)
- числа в инструкциях: +0x5bd1e995 +0x5bd1e995 +0x3c798d9f +0xde45aed5
- прямых вызовов: 10 → 9
- инструкций: 99 → 100
```diff
@@ -59,16 +59,17 @@
 mov esi, 0x6eb2c47b
 call F
-lea rdi, [D]
-mov esi, eax
-call F
 lea rcx, [rbp - 0x24]
 mov rsi, rbx
 mov rdi, r12
-imul edx, eax, 0x5bd1e995
+imul eax, eax, 0x5bd1e995
 mov r9d, 2
 mov r8d, 0x828
-xor edx, 0xe3502813
-mov eax, edx
-shr eax, 0xd
+xor eax, 0x3c798d9f
+imul eax, eax, 0x5bd1e995
+xor eax, 0xde45aed5
+imul eax, eax, 0x5bd1e995
+xor eax, 0xe3502813
+mov edx, eax
+shr edx, 0xd
 xor eax, edx
 imul eax, eax, 0x5bd1e995
```

### изменена: 0x59f9e80 (12440 байт) вызывается из: CHudDOTABase::vfunc#66, CDOTA_Hud_Minimap::vfunc#16 | строки: "DOTA_Chat_Ping_Msg_AttackMiniboss"; "General.PingAttack"; "General.PingRune"; "panorama/images/heroes/icons/npc_dota_hero_axe_png.vtex"; "#DOTA_Chat_Ping_Msg_Empty"; "General.PingDefense"; "npc_dota_unit_twin_gate"; "dota_item_spotted"
было: 0x59f9e40 (12468 байт)
- инструкций: 2477 → 2472
```diff
@@ -697,51 +697,16 @@
 mov r13, rax
 je L
-lea rax, [D]
 cmp byte ptr [rbp - 0x3c5], 0
+je L
+lea rax, [D]
 mov rax, qword ptr [rax]
 movss xmm0, dword ptr [rax + 0x30]
 movaps xmm1, xmm0
 subss xmm1, dword ptr [D]
-jne L
+comiss xmm1, dword ptr [K:2]
+ja L
 pxor xmm2, xmm2
 comiss xmm2, xmm1
-jbe L
-lea r12, [D]
-xor ecx, ecx
-xor edx, edx
-movss dword ptr [D], xmm0
-lea rsi, [S:"dota_rune_spotted"]
-mov rdi, qword ptr [r12]
-mov rax, qword ptr [rdi]
-call qword ptr [rax + 0x38]
-test rax, rax
-mov rbx, rax
-je L
-mov edx, dword ptr [rbp - 0x398]
-lea rsi, [S:"userid"]
-mov rdi, rax
-call F
-mov edx, dword ptr [r13 + 0xd48]
-lea rsi, [S:"rune"]
-mov rdi, rbx
-call F
-mov edx, dword ptr [r13 + 0xd50]
-lea rsi, [S:"rune_team"]
-mov rdi, rbx
-call F
-mov rax, qword ptr [rbx]
-mov rdi, rbx
-movabs rsi, 0xffffffff035ec176
-lea rdx, [r13 + 0xd54]
-mov rax, qword ptr [rax + 0xc8]
-mov qword ptr [rbp - 0x130], rsi
-lea rsi, [S:"map_location"]
-mov qword ptr [rbp - 0x128], rsi
-mov rsi, qword ptr [rbp - 0x3b8]
-call rax
-mov rdi, qword ptr [r12]
-mov rsi, rbx
-mov rax, qword ptr [rdi]
-call qword ptr [rax + 0x48]
+ja L
 lea r12, [S:"General.PingRune"]
 jmp L
@@ -797,5 +762,5 @@
 call F
 jmp L
-nop word ptr [rax + rax]
+nop dword ptr [rax]
 cmp dword ptr [rbp - 0x398], -1
 sete dl
@@ -897,7 +862,5 @@
 mov dword ptr [rbp - 0x444], eax
 nop word ptr cs:[rax + rax]
-nop word ptr cs:[rax + rax]
-nop word ptr cs:[rax + rax]
-nop dword ptr [rax]
+nop word ptr [rax + rax]
 test edx, edx
 je L
@@ -1983,7 +1946,7 @@
 jne L
 jmp L
+mov rdi, qword ptr [rbx + 0x40]
+jmp L
 mov rdi, qword ptr [rbx + 0x120]
-jmp L
-mov rdi, qword ptr [rbx + 0x40]
 jmp L
 mov byte ptr [rbp - 0x3f0], 0
@@ -2045,19 +2008,10 @@
 mov eax, dword ptr [rbx + 0x9b8]
 jmp L
-lea r12, [S:"General.PingAttack"]
+mov edi, 0x18d
+call F
+jmp L
 mov rdi, r15
 call F
-test al, al
-jne L
-mov rax, qword ptr [r15]
-mov rdi, r15
-call qword ptr [rax + 0xaa8]
-test al, al
-je L
-cmp byte ptr [rbp - 0x3ac], 0
-jne L
-lea r12, [S:"General.PingDefense"]
-jmp L
-nop word ptr cs:[rax + rax]
+jmp L
 cmp byte ptr [rbp - 0x3c5], 0
 je L
@@ -2070,10 +2024,19 @@
 movss dword ptr [rbp - 0x454], xmm0
 jmp L
-mov edi, 0x18d
-call F
-jmp L
+lea r12, [S:"General.PingAttack"]
 mov rdi, r15
 call F
-jmp L
+test al, al
+jne L
+mov rax, qword ptr [r15]
```
(ещё 160 строк диффа: so-query.py fdiff libclient.so 0x59f9e80)

## libserver.so: функций 220000 → 220000; без изменений 219986, изменено 14, добавлено 0, удалено 0

### изменена: 0x44c8df0 (32 байт) CDOTA_Modifier_Special_Bonus_Unique_Beastmaster_5_Aura::GetAuraRadius
было: 0x44ba340 (9 байт)
- числа в инструкциях: +0
- поля объектов: +0x16d2
- прямых вызовов: 0 → 1
- инструкций: 2 → 9
```diff
@@ -1,2 +1,9 @@
+push rbp
+mov rbp, rsp
+call F
 movss xmm0, dword ptr [K:-1]
+cmp byte ptr [rax + 0x16d2], 0
+je L
+pxor xmm0, xmm0
+pop rbp
 ret
```

### изменена: 0x44c8dd0 (32 байт) CDOTA_Modifier_Special_Bonus_Unique_Beastmaster_6_Aura::GetAuraRadius
было: 0x44ba4e0 (9 байт)
- числа в инструкциях: +0
- поля объектов: +0x16d2
- прямых вызовов: 0 → 1
- инструкций: 2 → 9
```diff
@@ -1,2 +1,9 @@
+push rbp
+mov rbp, rsp
+call F
 movss xmm0, dword ptr [K:-1]
+cmp byte ptr [rax + 0x16d2], 0
+je L
+pxor xmm0, xmm0
+pop rbp
 ret
```

### изменена: 0x44c95d0 (90 байт) CDOTA_Modifier_Special_Bonus_Unique_Beastmaster_6_Aura::GetAuraEntityReject
было: 0x44c95b0 (78 байт)
- виртуальные вызовы: +0xc60 (слот 396) +0xc60 (слот 396) −0xc58 (слот 395) −0xc58 (слот 395)
- инструкций: 26 → 32
```diff
@@ -6,21 +6,27 @@
 mov rbx, rdi
 call F
-mov rdx, rax
-mov eax, 1
-test rdx, rdx
+test rax, rax
 je L
-mov rax, qword ptr [r12]
-mov rdi, r12
-call qword ptr [rax + 0xc58]
 mov rdi, rbx
-mov r12, rax
 call F
 mov rdi, rax
 mov rax, qword ptr [rax]
-call qword ptr [rax + 0xc58]
-cmp r12, rax
-setne al
+call qword ptr [rax + 0xc60]
+mov rdi, r12
+mov ebx, eax
+mov rax, qword ptr [r12]
+call qword ptr [rax + 0xc60]
+mov edx, eax
+xor eax, eax
+cmp edx, ebx
+jne L
 pop rbx
 pop r12
 pop rbp
 ret
+nop word ptr [rax + rax]
+pop rbx
+mov eax, 1
+pop r12
+pop rbp
+ret
```

### изменена: 0x44c9630 (90 байт) CDOTA_Modifier_Special_Bonus_Unique_Beastmaster_5_Aura::GetAuraEntityReject
было: 0x44c9600 (78 байт)
- виртуальные вызовы: +0xc60 (слот 396) +0xc60 (слот 396) −0xc58 (слот 395) −0xc58 (слот 395)
- инструкций: 26 → 32
```diff
@@ -6,21 +6,27 @@
 mov rbx, rdi
 call F
-mov rdx, rax
-mov eax, 1
-test rdx, rdx
+test rax, rax
 je L
-mov rax, qword ptr [r12]
-mov rdi, r12
-call qword ptr [rax + 0xc58]
 mov rdi, rbx
-mov r12, rax
 call F
 mov rdi, rax
 mov rax, qword ptr [rax]
-call qword ptr [rax + 0xc58]
-cmp r12, rax
-setne al
+call qword ptr [rax + 0xc60]
+mov rdi, r12
+mov ebx, eax
+mov rax, qword ptr [r12]
+call qword ptr [rax + 0xc60]
+mov edx, eax
+xor eax, eax
+cmp edx, ebx
+jne L
 pop rbx
 pop r12
 pop rbp
 ret
+nop word ptr [rax + rax]
+pop rbx
+mov eax, 1
+pop r12
+pop rbp
+ret
```

### изменена: 0x44c9690 (90 байт) CDOTA_Modifier_Beastmaster_DrumsOfSlom::GetAuraEntityReject
было: 0x44c9650 (78 байт)
- виртуальные вызовы: +0xc60 (слот 396) +0xc60 (слот 396) −0xc58 (слот 395) −0xc58 (слот 395)
- инструкций: 26 → 32
```diff
@@ -6,21 +6,27 @@
 mov rbx, rdi
 call F
-mov rdx, rax
-mov eax, 1
-test rdx, rdx
+test rax, rax
 je L
-mov rax, qword ptr [r12]
-mov rdi, r12
-call qword ptr [rax + 0xc58]
 mov rdi, rbx
-mov r12, rax
 call F
 mov rdi, rax
 mov rax, qword ptr [rax]
-call qword ptr [rax + 0xc58]
-cmp r12, rax
-setne al
+call qword ptr [rax + 0xc60]
+mov rdi, r12
+mov ebx, eax
+mov rax, qword ptr [r12]
+call qword ptr [rax + 0xc60]
+mov edx, eax
+xor eax, eax
+cmp edx, ebx
+jne L
 pop rbx
 pop r12
 pop rbp
 ret
+nop word ptr [rax + rax]
+pop rbx
+mov eax, 1
+pop r12
+pop rbp
+ret
```

### изменена: 0x44c96f0 (90 байт) CDOTA_Modifier_Beastmaster_InnerBeast_Aura::GetAuraEntityReject
было: 0x44c96a0 (78 байт)
- виртуальные вызовы: +0xc60 (слот 396) +0xc60 (слот 396) −0xc58 (слот 395) −0xc58 (слот 395)
- инструкций: 26 → 32
```diff
@@ -6,21 +6,27 @@
 mov rbx, rdi
 call F
-mov rdx, rax
-mov eax, 1
-test rdx, rdx
+test rax, rax
 je L
-mov rax, qword ptr [r12]
-mov rdi, r12
-call qword ptr [rax + 0xc58]
 mov rdi, rbx
-mov r12, rax
 call F
 mov rdi, rax
 mov rax, qword ptr [rax]
-call qword ptr [rax + 0xc58]
-cmp r12, rax
-setne al
+call qword ptr [rax + 0xc60]
+mov rdi, r12
+mov ebx, eax
+mov rax, qword ptr [r12]
+call qword ptr [rax + 0xc60]
+mov edx, eax
+xor eax, eax
+cmp edx, ebx
+jne L
 pop rbx
 pop r12
 pop rbp
 ret
+nop word ptr [rax + rax]
+pop rbx
+mov eax, 1
+pop r12
+pop rbp
+ret
```

### изменена: 0x44f9a50 (453 байт) CDOTA_Modifier_Beastmaster_InnerBeast::OnIntervalThink | строки: "modifier_beastmaster_inner_beast_aura"
было: 0x44f98f0 (453 байт)
- виртуальные вызовы: +0xc60 (слот 396) +0xc60 (слот 396) −0xc58 (слот 395) −0xc58 (слот 395)
- инструкций: 123 → 126
```diff
@@ -6,8 +6,8 @@
 push r12
 push rbx
-mov rbx, rdi
-sub rsp, 0x18
-mov eax, dword ptr [rdi + 0x1aac]
-test eax, eax
+sub rsp, 0x28
+mov edx, dword ptr [rdi + 0x1aac]
+mov qword ptr [rbp - 0x48], rdi
+test edx, edx
 jle L
 call F
@@ -31,26 +31,26 @@
 cmp eax, dword ptr [rdx + 0x10]
 jne L
-mov r12, qword ptr [rdx]
-test r12, r12
+mov r15, qword ptr [rdx]
+test r15, r15
 je L
-cmp byte ptr [r12 + 0x5d1], 3
+cmp byte ptr [r15 + 0x5d1], 3
 jne L
 lea rsi, [S:"modifier_beastmaster_inner_beast_aura"]
 xor edx, edx
-mov rdi, r12
+mov rdi, r15
 call F
 test rax, rax
-mov r15, rax
+mov rbx, rax
 je L
-movsxd r13, dword ptr [rax + 0xc8]
-test r13d, r13d
+movsxd r12, dword ptr [rax + 0xc8]
+test r12d, r12d
 jle L
-lea rax, [r13*4]
+lea rax, [r12*4]
 xor r14d, r14d
 xor r13d, r13d
 mov qword ptr [rbp - 0x38], rax
 nop word ptr [rax + rax]
-mov rax, qword ptr [r15 + 0xd0]
-mov eax, dword ptr [rax + r13]
+mov rax, qword ptr [rbx + 0xd0]
+mov eax, dword ptr [rax + r14]
 cmp eax, -1
 je L
@@ -72,25 +72,47 @@
 cmp eax, dword ptr [rdx + 0x10]
 jne L
-mov rdi, qword ptr [rdx]
-test rdi, rdi
+mov r12, qword ptr [rdx]
+test r12, r12
 je L
-cmp byte ptr [rdi + 0x5d1], 3
+cmp byte ptr [r12 + 0x5d1], 3
 jne L
-mov rax, qword ptr [rdi]
-call qword ptr [rax + 0xc58]
+mov rax, qword ptr [r15]
+mov rdi, r15
+call qword ptr [rax + 0xc60]
 mov rdi, r12
-mov qword ptr [rbp - 0x40], rax
+mov dword ptr [rbp - 0x3c], eax
 mov rax, qword ptr [r12]
-call qword ptr [rax + 0xc58]
-cmp qword ptr [rbp - 0x40], rax
+call qword ptr [rax + 0xc60]
+mov esi, dword ptr [rbp - 0x3c]
+cmp eax, esi
 sete al
 movzx eax, al
-add r14d, eax
-add r13, 4
-cmp qword ptr [rbp - 0x38], r13
+add r13d, eax
+add r14, 4
+cmp qword ptr [rbp - 0x38], r14
 jne L
-mov dword ptr [rbx + 0x1ab4], r14d
-add rsp, 0x18
-mov rdi, rbx
+mov rax, qword ptr [rbp - 0x48]
+mov dword ptr [rax + 0x1ab4], r13d
+add rsp, 0x28
+mov rdi, rax
+pop rbx
+pop r12
+pop r13
+pop r14
+pop r15
+pop rbp
+jmp F
+nop dword ptr [rax]
+add rsp, 0x28
+pop rbx
+pop r12
+pop r13
+pop r14
+pop r15
+pop rbp
+ret
+nop
+movss xmm0, dword ptr [K:-1]
+add rsp, 0x28
 pop rbx
 pop r12
@@ -101,23 +123,4 @@
 jmp F
 nop dword ptr [rax + rax]
-add rsp, 0x18
-pop rbx
-pop r12
-pop r13
-pop r14
```
(ещё 17 строк диффа: so-query.py fdiff libserver.so 0x44f9a50)

### изменена: 0x452ac80 (2697 байт) CDOTA_Modifier_Beastmaster_DrumsOfSlom::OnIntervalThink | строки: "particles/units/heroes/hero_beastmaster/beastmaster_drums_of_slom_stop.vpcf"; "attach_hitloc"; "Hero_Beastmaster.DrumsOfSlom.Strike"; "particles/units/heroes/hero_beastmaster/beastmaster_drums_of_slom_hit.vpcf"; "particles/units/heroes/hero_phoenix/phoenix_sunray_beam_friend.vpcf"
было: 0x452ac40 (2697 байт)
- виртуальные вызовы: +0xc60 (слот 396) +0xc60 (слот 396) −0xc58 (слот 395) −0xc58 (слот 395)
- инструкций: 557 → 555
```diff
@@ -318,4 +318,139 @@
 jmp L
 nop word ptr [rax + rax]
+movss xmm6, dword ptr [rbp - 0x18c]
+pxor xmm0, xmm0
+mov r13, qword ptr [rbp - 0x188]
+comiss xmm6, xmm0
+mov r14, qword ptr [rbp - 0x1b0]
+jbe L
+movss xmm0, dword ptr [rbx + 0x1aa8]
+mov rdi, rbx
+mov qword ptr [rbp - 0x130], 0
+mov qword ptr [rbp - 0x128], 0
+movss dword ptr [rbp - 0x188], xmm0
+mov qword ptr [rbp - 0x120], 0
+call F
+mov rdi, rax
+call F
+mov rdi, rbx
+mov r12, rax
+call F
+mov rdi, rbx
+movzx r15d, byte ptr [rax + 0x624]
+call F
+mov rdi, rax
+call F
+push 0
+xor ecx, ecx
+mov rdx, r12
+push 0
+mov rdi, rax
+mov r9d, 1
+mov esi, r15d
+push 0
+push 0x13
+mov r8, qword ptr [rbp - 0x1a8]
+movss xmm0, dword ptr [rbp - 0x188]
+call F
+mov r10, qword ptr [rbp - 0x128]
+add rsp, 0x20
+movsxd rax, dword ptr [rbp - 0x130]
+lea rdx, [r10 + rax*4]
+cmp rdx, r10
+je L
+mov qword ptr [rbp - 0x198], r13
+mov r13, r10
+mov qword ptr [rbp - 0x188], rdx
+mov qword ptr [rbp - 0x1a0], r14
+nop dword ptr [rax + rax]
+mov eax, dword ptr [r13]
+mov rdi, qword ptr [rbp - 0x198]
+mov dword ptr [rbp - 0x154], eax
+call F
+test rax, rax
+je L
+mov r12, qword ptr [rax]
+test r12, r12
+je L
+cmp byte ptr [r12 + 0x5d1], 3
+jne L
+mov rdi, rbx
+call F
+mov rdi, rax
+mov rax, qword ptr [rax]
+call qword ptr [rax + 0xc60]
+mov rdi, r12
+mov r14d, eax
+mov rax, qword ptr [r12]
+call qword ptr [rax + 0xc60]
+cmp eax, r14d
+jne L
+mov rdi, rbx
+call F
+mov rdi, rbx
+mov r14, rax
+call F
+mov rdx, r14
+xor ecx, ecx
+mov rdi, r12
+movss xmm0, dword ptr [rbp - 0x18c]
+mov rsi, rax
+call F
+call F
+mov rdi, rbx
+mov r14, rax
+call F
+mov rdi, rbx
+mov r15, rax
+call F
+sub rsp, 8
+mov r9, r15
+xor r8d, r8d
+push 0
+mov rcx, rax
+mov edx, 1
+mov rdi, r14
+lea rsi, [S:"particles/units/heroes/hero_phoenix/phoenix_sunray_beam_friend.vpcf"]
+call F
+mov r14d, eax
+call F
+mov rdi, rbx
+mov r15, rax
+call F
+mov r8d, 5
+mov esi, r14d
+push 0
+movss xmm1, dword ptr [K:3.402823e+38]
+mov rcx, rax
+mov rdi, r15
+push 1
+movq xmm0, qword ptr [K:0x7f7fffff7f7fffff]
+lea r9, [S:"attach_hitloc"]
+mov edx, 1
+call F
+add rsp, 0x20
+call F
+mov esi, r14d
+mov rdi, rax
+mov rax, qword ptr [rax]
+call qword ptr [rax + 0x18]
```
(ещё 169 строк диффа: so-query.py fdiff libserver.so 0x452ac80)

### изменена: 0x454af60 (3692 байт) CDOTA_Unit_Courier::Spawn | строки: "modifier_magic_immune"; "modifier_phased"; "modifier_track_order_issuer"; "team_first_courier"; "DOTA_COURIER_MODE_THINK_CONTEXT"; "modifier_courier_passive_bonus"; "initiallevel"; "solecontrollingplayerid"
было: 0x454af20 (3692 байт)
- числа в инструкциях: −1 −1
- инструкций: 729 → 728
```diff
@@ -507,11 +507,13 @@
 jmp L
 nop dword ptr [rax + rax]
+lea r15, [rbp - 0x138]
 xor eax, eax
-mov esi, 1
-pxor xmm0, xmm0
-mov qword ptr [rbp - 0x140], 1
-lea rdi, [rbp - 0x130]
+pxor xmm0, xmm0
+mov dword ptr [rbp - 0x180], 0x1c7c
+lea rsi, [rbp - 0x180]
+mov rdi, r15
 movaps xmmword ptr [rbp - 0x120], xmm0
 mov word ptr [rbp - 0x104], ax
+mov qword ptr [rbp - 0x140], 1
 mov qword ptr [rbp - 0x138], 0
 mov qword ptr [rbp - 0x130], 0
@@ -520,12 +522,9 @@
 mov dword ptr [rbp - 0x108], 0xffffffff
 call F
-mov rax, qword ptr [rbp - 0x130]
+mov rax, qword ptr [rbx]
 mov rsi, r12
 mov rdi, rbx
-add dword ptr [rbp - 0x138], 1
-mov dword ptr [rax], 0x1c7c
-mov rax, qword ptr [rbx]
 call qword ptr [rax + 0xe8]
-lea rdi, [rbp - 0x138]
+mov rdi, r15
 call F
 cmp dword ptr [rbx + 0x1014], r14d
@@ -533,5 +532,5 @@
 je L
 jmp L
-nop
+nop dword ptr [rax]
 test eax, eax
 je L
@@ -570,5 +569,5 @@
 je L
 mov byte ptr [rbx + 0x315], 1
-nop
+nop word ptr cs:[rax + rax]
 lea rax, [D]
 mov rax, qword ptr [rax]
```

### изменена: 0x4554d00 (9341 байт) CDOTA_Modifier_DeathProphet_Exorcism::OnIntervalThink | строки: "UntargetableByExorcismSpirits"; "Hero_DeathProphet.Exorcism.Heal"; "exorcismend"; "particles/units/heroes/hero_death_prophet/death_prophet_exorcism_attack.vpcf"; "attach_hitloc"; "Hero_DeathProphet.Exorcism.Damage"; "particles/units/heroes/hero_death_prophet/death_prophet_exorcism_attack_building"; "Damage_Melee.Building"
было: 0x4554cc0 (8406 байт)
- числа в инструкциях: +0xf +0xf +-1 +0x7fff +0x7fff +8 +1 +0xffffffff
- поля объектов: +0x10 +0x10 +0x10 +0x10 +0x10 +0x10 +0x30
- прямых вызовов: 181 → 180
- инструкций: 1877 → 2017
```diff
@@ -10,5 +10,5 @@
 call F
 test rax, rax
-mov qword ptr [rbp - 0x150], rax
+mov qword ptr [rbp - 0x148], rax
 je L
 lea rax, [D]
@@ -21,12 +21,12 @@
 mov r12, qword ptr [r11 + 0x1b00]
 movsxd rax, dword ptr [r11 + 0x1af8]
-lea r13, [r12 + rax*8]
-cmp r13, r12
+lea r14, [r12 + rax*8]
+cmp r14, r12
 je L
 lea rbx, [rbp - 0x70]
 mov qword ptr [rbp - 0x110], r11
 nop dword ptr [rax]
-mov r14, qword ptr [r12]
-mov esi, dword ptr [r14]
+mov r13, qword ptr [r12]
+mov esi, dword ptr [r13]
 cmp esi, -1
 je L
@@ -36,5 +36,5 @@
 cmp esi, -2
 je L
-movzx eax, word ptr [r14]
+movzx eax, word ptr [r13]
 mov rdx, rax
 shr rdx, 9
@@ -60,5 +60,5 @@
 call F
 movq xmm3, qword ptr [rbp - 0x100]
-mov esi, dword ptr [r14]
+mov esi, dword ptr [r13]
 movss dword ptr [rbp - 0x88], xmm1
 movq qword ptr [rbp - 0x90], xmm0
@@ -75,5 +75,5 @@
 cmp esi, -2
 je L
-movzx edx, word ptr [r14]
+movzx edx, word ptr [r13]
 mov eax, edx
 shr rdx, 9
@@ -103,5 +103,5 @@
 call F
 add r12, 8
-cmp r13, r12
+cmp r14, r12
 jne L
 mov r11, qword ptr [rbp - 0x110]
@@ -146,20 +146,21 @@
 cmp r10, rdx
 je L
+mov r15, rdx
+xor r14d, r14d
+mov qword ptr [rbp - 0x108], r10
+mov rbx, r11
 mov dword ptr [rbp - 0x120], 0
-xor r15d, r15d
-mov rbx, r11
 mov dword ptr [rbp - 0x114], 0
 mov qword ptr [rbp - 0x110], 0
 mov dword ptr [rbp - 0x118], 0
-mov qword ptr [rbp - 0x108], r10
-mov qword ptr [rbp - 0x100], rdx
-jmp L
-nop
-mov rdi, rbx
-call F
-mov rdi, rax
-call F
-movss xmm1, dword ptr [r14 + 8]
-movss xmm0, dword ptr [r14 + 4]
+jmp L
+nop word ptr [rax + rax]
+mov rdi, rbx
+call F
+mov rdi, rax
+call F
+mov r10, qword ptr [rbp - 0x100]
+movss xmm1, dword ptr [r10 + 8]
+movss xmm0, dword ptr [r10 + 4]
 subss xmm1, dword ptr [rax + 4]
 subss xmm0, dword ptr [rax]
@@ -174,15 +175,18 @@
 comiss xmm0, xmm1
 jbe L
-cmp dword ptr [r14 + 0x24], -1
-je L
-call F
-mov esi, dword ptr [r14 + 0x24]
+cmp dword ptr [r10 + 0x24], -1
+je L
+mov qword ptr [rbp - 0x100], r10
+call F
+mov r10, qword ptr [rbp - 0x100]
 mov ecx, 1
 xor edx, edx
 mov rdi, rax
-call F
-mov dword ptr [r14 + 0x24], 0xffffffff
-mov dword ptr [r14 + 0x10], 0xffffffff
-mov edx, dword ptr [r14]
+mov esi, dword ptr [r10 + 0x24]
+call F
+mov r10, qword ptr [rbp - 0x100]
+mov dword ptr [r10 + 0x24], 0xffffffff
+mov dword ptr [r10 + 0x10], 0xffffffff
+mov edx, dword ptr [r10]
 cmp edx, -1
 je L
@@ -192,5 +196,5 @@
 cmp edx, -2
 je L
-movzx eax, word ptr [r14]
+movzx eax, word ptr [r10]
 mov rcx, rax
 shr rcx, 9
```
(ещё 1446 строк диффа: so-query.py fdiff libserver.so 0x4554d00)

### изменена: 0x492cd20 (1809 байт) CDOTA_Ability_EmberSpirit_Activate_FireRemnant::vfunc#371 | строки: "damage"; "radius"; "modifier_ember_spirit_fire_remnant_remnant_tracker"; "Hero_EmberSpirit.FireRemnant.Explode"; "modifier_ember_spirit_fire_remnant"; "modifier_ember_spirit_fire_remnant_timer"
было: 0x492c920 (1862 байт)
- числа в инструкциях: −0xffffffff −1 −-1 −0xf −0xf −0x7fff −0x7fff
- поля объектов: −0x10 −0x10 −0x10 −0x10 −0x894 −0x894 −0x30
- прямых вызовов: 55 → 56
- инструкций: 457 → 440
```diff
@@ -8,5 +8,5 @@
 push rbx
 mov rbx, rdi
-sub rsp, 0x78
+sub rsp, 0x88
 call F
 test rax, rax
@@ -28,5 +28,5 @@
 pop rbp
 ret
-nop word ptr [rax + rax]
+nop dword ptr [rax]
 lea rsi, [S:"damage"]
 xor edx, edx
@@ -36,12 +36,14 @@
 mov rdi, rbx
 lea rsi, [S:"radius"]
-movss dword ptr [rbp - 0xa0], xmm0
+movss dword ptr [rbp - 0xac], xmm0
 call F
 mov rax, qword ptr [r12 + 0xc]
-lea rdi, [rbx + 0x894]
 movss dword ptr [rbp - 0x98], xmm0
 mov qword ptr [rbp - 0x5c], rax
 mov eax, dword ptr [r12 + 0x14]
 mov dword ptr [rbp - 0x54], eax
+lea rax, [rbx + 0x894]
+mov rdi, rax
+mov qword ptr [rbp - 0xa0], rax
 call F
 test rax, rax
@@ -83,5 +85,5 @@
 xor eax, eax
 jmp L
-nop dword ptr [rax]
+nop word ptr cs:[rax + rax]
 add rax, 1
 cmp rax, rsi
@@ -122,9 +124,8 @@
 call F
 mov rdi, rbx
-mov r15, rax
-call F
-mov rdi, rbx
-movzx esi, byte ptr [rax + 0x624]
-mov dword ptr [rbp - 0x9c], esi
+mov qword ptr [rbp - 0xa8], rax
+call F
+mov rdi, rbx
+movzx r15d, byte ptr [rax + 0x624]
 call F
 mov rdi, rax
@@ -136,8 +137,8 @@
 mov rdi, rax
 mov r9d, 2
-mov rcx, r15
+mov esi, r15d
 push 0
 push 3
-mov esi, dword ptr [rbp - 0x9c]
+mov rcx, qword ptr [rbp - 0xa8]
 movss xmm0, dword ptr [rbp - 0x98]
 call F
@@ -203,16 +204,17 @@
 mov dword ptr [rbx + 0x894], 0xffffffff
 je L
-mov r15d, dword ptr [r13 + 0x1aa8]
-test r15d, r15d
-je L
-sub r15d, 1
+mov edx, dword ptr [r13 + 0x1aa8]
+test edx, edx
+je L
+sub edx, 1
+mov r15d, edx
 js L
-movsxd rcx, r15d
+movsxd r8, edx
 mov rdi, qword ptr [r13 + 0x1ab0]
 lea rax, [r13 + 0x1aa8]
-lea r12, [rcx*4]
+lea r12, [r8*4]
 mov qword ptr [rbp - 0x98], rax
 jmp L
-nop dword ptr [rax]
+nop
 sub r15d, 1
 sub r12, 4
@@ -220,11 +222,11 @@
 je L
 lea rax, [rdi + r12]
-mov edx, dword ptr [rax]
-cmp edx, -1
-je L
-mov r8, qword ptr [D]
-test r8, r8
-je L
-cmp edx, -2
+mov ecx, dword ptr [rax]
+cmp ecx, -1
+je L
+mov r9, qword ptr [D]
+test r9, r9
+je L
+cmp ecx, -2
 je L
 movzx eax, word ptr [rax]
@@ -232,10 +234,10 @@
 shr rsi, 9
 and esi, 0x3f
-mov rsi, qword ptr [r8 + rsi*8]
+mov rsi, qword ptr [r9 + rsi*8]
 test rsi, rsi
 je L
 and eax, 0x1ff
 imul rax, rax, 0x70
-cmp edx, dword ptr [rsi + rax + 0x10]
+cmp ecx, dword ptr [rsi + rax + 0x10]
 je L
 mov rdi, qword ptr [rbp - 0x98]
```
(ещё 70 строк диффа: so-query.py fdiff libserver.so 0x492cd20)

### изменена: 0x4939200 (3230 байт) CDOTA_Modifier_Dawnbreaker_Solar_Guardian_Thinker::OnIntervalThink | строки: "particles/units/heroes/hero_dawnbreaker/dawnbreaker_solar_guardian_damage.vpcf"; "attach_hitloc"; "miss_rate"; "particles/units/heroes/hero_dawnbreaker/dawnbreaker_solar_guardian_healing_buff."; "modifier_dawnbreaker_solar_guardian_evasion"; "duration"; "particles/units/heroes/hero_dawnbreaker/dawnbreaker_solar_guardian_damage_hit.vp"; "Hero_Dawnbreaker.Solar_Guardian.Damage"
было: 0x492dcc0 (3273 байт)
- числа в инструкциях: +1 +0 −3 −3
- поля объектов: −0x5d1 −0x5d1 −0xcd4 −0x16d2 −0xd48
- прямых вызовов: 81 → 82
- инструкций: 676 → 667
```diff
@@ -94,5 +94,5 @@
 mov rdi, rbx
 mov qword ptr [rbp - 0x120], 0
-mov qword ptr [rbp - 0x100], 0
+mov dword ptr [rbp - 0xfc], 0
 movss dword ptr [rbp - 0x170], xmm0
 mov qword ptr [rbp - 0xf0], 0
@@ -116,5 +116,5 @@
 mov esi, r13d
 lea rax, [rbp - 0xf0]
-mov qword ptr [rbp - 0x1a0], rax
+mov qword ptr [rbp - 0x198], rax
 mov r8, rax
 push 0
@@ -128,14 +128,13 @@
 test esi, esi
 jle L
-lea rax, [rbp - 0x110]
+lea rax, [rbp - 0x130]
 xor r13d, r13d
 xor r12d, r12d
+mov dword ptr [rbp - 0x188], 0
 mov dword ptr [rbp - 0x178], 0
-mov qword ptr [rbp - 0x190], rax
-lea rax, [rbp - 0x130]
 mov qword ptr [rbp - 0x180], 0
 mov dword ptr [rbp - 0x174], 0
-mov qword ptr [rbp - 0x198], rax
-nop
+mov qword ptr [rbp - 0x190], rax
+nop dword ptr [rax]
 mov rax, qword ptr [rbp - 0xe8]
 lea rax, [rax + r13*4]
@@ -201,5 +200,5 @@
 jle L
 lea r14, [r12 + rax*4]
-mov qword ptr [rbp - 0x1b0], r12
+mov qword ptr [rbp - 0x1a8], r12
 mov r15, r14
 nop
@@ -322,5 +321,5 @@
 call F
 mov rdi, rbx
-mov qword ptr [rbp - 0x1a8], rax
+mov qword ptr [rbp - 0x1a0], rax
 call F
 mov rdi, r13
@@ -329,5 +328,5 @@
 mov r8, qword ptr [rbp - 0x168]
 mov rsi, rax
-mov rdx, qword ptr [rbp - 0x1a8]
+mov rdx, qword ptr [rbp - 0x1a0]
 call F
 mov rdi, qword ptr [rbp - 0x168]
@@ -335,7 +334,7 @@
 nop word ptr [rax + rax]
 add r12, 4
-cmp r15, r12
-jne L
-mov r12, qword ptr [rbp - 0x1b0]
+cmp r12, r15
+jne L
+mov r12, qword ptr [rbp - 0x1a8]
 mov esi, dword ptr [rbp - 0x174]
 test esi, esi
@@ -354,8 +353,8 @@
 cmp ecx, -1
 je L
+cmp ecx, -2
 mov rsi, qword ptr [D]
+je L
 test rsi, rsi
-je L
-cmp ecx, -2
 je L
 movzx eax, word ptr [r15]
@@ -418,30 +417,20 @@
 test ecx, ecx
 jle L
-cmp byte ptr [r12 + 0x5d1], 3
-mov r14, r12
-jne L
-mov rdi, rbx
-mov dword ptr [rbp - 0x1a8], ecx
-call F
-mov ecx, dword ptr [rbp - 0x1a8]
-test rax, rax
-mov rdi, rax
-je L
-cmp byte ptr [rax + 0x5d1], 3
-jne L
-test byte ptr [rax + 0xcd4], 1
-jne L
-mov rax, qword ptr [rax]
-lea rdx, [T]
-mov rax, qword ptr [rax + 0xd48]
-cmp rax, rdx
-jne L
-xor edi, edi
+mov rdi, r12
+mov dword ptr [rbp - 0x1a0], ecx
+call F
+mov rdi, rbx
+mov r14, rax
+call F
+mov rdi, rax
+call F
 xor r9d, r9d
 xor r8d, r8d
 mov edx, 0x33e
+mov ecx, dword ptr [rbp - 0x1a0]
+mov rdi, rax
 mov rsi, r14
 call F
-nop word ptr [rax + rax]
+nop dword ptr [rax]
 call F
 mov rdi, rbx
@@ -512,5 +501,5 @@
 pop rdx
```
(ещё 139 строк диффа: so-query.py fdiff libserver.so 0x4939200)

### изменена: 0x49404e0 (1457 байт) CDOTA_Ability_Hoodwink_Decoy::OnSpellStart | строки: "Hero_Hoodwink.Scurry.Cast"; "duration"; "decoy_stun_duration"; "decoy_detonate_radius"; "projectile_speed"; "modifier_illusion"; "images_do_damage_percent"; "outgoing_damage"
было: 0x4940140 (1441 байт)
- строки: +"permit_illusion_recycling"
- прямых вызовов: 44 → 45
- инструкций: 327 → 331
```diff
@@ -80,4 +80,8 @@
 lea rsi, [S:"no_effect_on_original"]
 call F
+xor edx, edx
+mov rdi, rbx
+lea rsi, [S:"permit_illusion_recycling"]
+call F
 mov rdi, r12
 call F
@@ -102,5 +106,5 @@
 mov qword ptr [rbp - 0xd8], r15
 mov dword ptr [rbp - 0xc0], r14d
-nop dword ptr [rax + rax]
+nop dword ptr [rax]
 mov rax, qword ptr [r12 + 0x868]
 lea rax, [rax + r13*4]
```

### изменена: 0x5dfe860 (2664 байт) CDOTA_BotMode_Farm::vfunc#10 | строки: "../../game/server/dota/bot/dota_bot_mode_farm.cpp"; "CDOTA_BotMode_Farm::GetDesire"; "GetDesire"; "modifier_persistent_invisibility"
было: 0x5dfe4a0 (2664 байт)
- инструкций: 563 → 564
```diff
@@ -400,16 +400,17 @@
 je L
 mov rax, qword ptr [r12 + 0xd8]
+mov rdi, qword ptr [rax + 0xa0]
 add ebx, 1
-mov rdi, qword ptr [rax + 0xa0]
 cmp ebx, dword ptr [rdi + 0x370]
 jge L
 mov esi, ebx
 call F
-test rax, rax
 mov r15, rax
-je L
-cmp rax, qword ptr [r12 + 0xd8]
-je L
-mov rdi, rax
+mov rax, qword ptr [r12 + 0xd8]
+test r15, r15
+je L
+cmp r15, rax
+je L
+mov rdi, r15
 call F
 mov rdi, rax
@@ -428,5 +429,5 @@
 jb L
 jmp L
-nop dword ptr [rax]
+nop
 movss xmm6, dword ptr [r12 + r13*4 + 0xf8]
 movss dword ptr [rbp - 0x74], xmm6
```
