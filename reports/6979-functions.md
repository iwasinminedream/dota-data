# Dota 6979: изменения кода по функциям

Снимки `6978-11253575` → `6979-11254438`; funcdiff.py. В диффе: [S:…] — строка, [K:…] — константа из данных, F — вызов другой функции, L — переход внутри функции, [D]/[T] — прочие адреса. Регистры и смещения стека меняются и от перекомпиляции.

## libclient.so: функций 281789 → 281790; без изменений 281755, изменено 24, добавлено 2, удалено 1

### изменена: 0x4de0120 (108 байт) вызывается из: CDOTA_Modifier_Item_Skadi_Slow::vfunc#88
было: 0x4de0120 (106 байт)
- инструкций: 29 → 27
```diff
@@ -13,11 +13,9 @@
 test byte ptr [rax + 0x15bc], 2
 jne L
-mov eax, dword ptr [r12 + 0x1b00]
+movss xmm0, dword ptr [r12 + 0x1b00]
+movss dword ptr [rbx + 4], xmm0
+mov rax, rbx
 pxor xmm0, xmm0
-cvtsi2ss xmm0, eax
 mov dword ptr [rbx], 1
-mov rax, rbx
-movss dword ptr [rbx + 4], xmm0
-pxor xmm0, xmm0
 movups xmmword ptr [rbx + 8], xmm0
 pop rbx
@@ -25,5 +23,5 @@
 pop rbp
 ret
-nop
-mov eax, dword ptr [r12 + 0x1b04]
+nop dword ptr [rax + rax]
+movss xmm0, dword ptr [r12 + 0x1b04]
 jmp L
```

### изменена: 0x4de0190 (116 байт) вызывается из: CDOTA_Modifier_Item_Skadi_Slow::vfunc#88
было: 0x4de0190 (122 байт)
- инструкций: 33 → 31
```diff
@@ -17,11 +17,9 @@
 test byte ptr [rax + 0x15bc], 2
 jne L
-mov eax, dword ptr [r12 + 0x1af8]
+movss xmm0, dword ptr [r12 + 0x1af8]
+movss dword ptr [rbx + 4], xmm0
+mov rax, rbx
 pxor xmm0, xmm0
-cvtsi2ss xmm0, eax
 mov dword ptr [rbx], 1
-mov rax, rbx
-movss dword ptr [rbx + 4], xmm0
-pxor xmm0, xmm0
 movups xmmword ptr [rbx + 8], xmm0
 pop rbx
@@ -29,5 +27,5 @@
 pop rbp
 ret
-nop dword ptr [rax + rax]
-mov eax, dword ptr [r12 + 0x1afc]
+nop dword ptr [rax]
+movss xmm0, dword ptr [r12 + 0x1afc]
 jmp L
```

### изменена: 0x4df1880 (367 байт) CDOTA_Modifier_Item_Skadi_Slow::vfunc#79 | строки: "cold_attack_slow_melee"; "cold_attack_slow_ranged"; "cold_slow_melee"; "cold_slow_ranged"; "restoration_reduction"
было: 0x4df18c0 (367 байт)
- числа в инструкциях: +0xffffffff +0xffffffff +0xffffffff +0xffffffff −0 −0 −0 −0
- инструкций: 86 → 98
```diff
@@ -10,9 +10,15 @@
 call qword ptr [rax + 0x1a8]
 test r12, r12
+pxor xmm1, xmm1
 je L
-lea rsi, [rbx + 0x1b00]
+xor r9d, r9d
+xor r8d, r8d
+xor ecx, ecx
+lea rsi, [S:"cold_attack_slow_melee"]
+mov edx, 0xffffffff
 mov rdi, r12
-lea rdx, [S:"cold_attack_slow_melee"]
 call F
+movaps xmm1, xmm0
+movss dword ptr [rbx + 0x1b00], xmm1
 mov rdi, rbx
 call F
@@ -22,9 +28,15 @@
 call qword ptr [rax + 0x1a8]
 test r12, r12
+pxor xmm1, xmm1
 je L
-lea rsi, [rbx + 0x1b04]
+xor r9d, r9d
+xor r8d, r8d
+xor ecx, ecx
+lea rsi, [S:"cold_attack_slow_ranged"]
+mov edx, 0xffffffff
 mov rdi, r12
-lea rdx, [S:"cold_attack_slow_ranged"]
 call F
+movaps xmm1, xmm0
+movss dword ptr [rbx + 0x1b04], xmm1
 mov rdi, rbx
 call F
@@ -34,9 +46,15 @@
 call qword ptr [rax + 0x1a8]
 test r12, r12
+pxor xmm1, xmm1
 je L
-lea rsi, [rbx + 0x1af8]
+xor r9d, r9d
+xor r8d, r8d
+xor ecx, ecx
+lea rsi, [S:"cold_slow_melee"]
+mov edx, 0xffffffff
 mov rdi, r12
-lea rdx, [S:"cold_slow_melee"]
 call F
+movaps xmm1, xmm0
+movss dword ptr [rbx + 0x1af8], xmm1
 mov rdi, rbx
 call F
@@ -46,9 +64,15 @@
 call qword ptr [rax + 0x1a8]
 test r12, r12
+pxor xmm1, xmm1
 je L
-lea rsi, [rbx + 0x1afc]
+xor r9d, r9d
+xor r8d, r8d
+xor ecx, ecx
+lea rsi, [S:"cold_slow_ranged"]
+mov edx, 0xffffffff
 mov rdi, r12
-lea rdx, [S:"cold_slow_ranged"]
 call F
+movaps xmm1, xmm0
+movss dword ptr [rbx + 0x1afc], xmm1
 mov rdi, rbx
 call F
@@ -73,14 +97,2 @@
 pop rbp
 ret
-nop word ptr [rax + rax]
-mov dword ptr [rbx + 0x1b00], 0
-jmp L
-nop
-mov dword ptr [rbx + 0x1afc], 0
-jmp L
-nop dword ptr [rax]
-mov dword ptr [rbx + 0x1af8], 0
-jmp L
-nop
-mov dword ptr [rbx + 0x1b04], 0
-jmp L
```

### изменена: 0x4ecb1f0 (172 байт) вызывается из: CDOTA_Modifier_Orb_Of_Corrosion_Debuff::vfunc#88 | строки: "modifier_item_skadi_slow"
было: 0x4ecb190 (186 байт)
- инструкций: 50 → 47
```diff
@@ -34,11 +34,9 @@
 test byte ptr [rax + 0x15bc], 2
 jne L
-mov eax, dword ptr [r12 + 0x1b00]
+movss xmm0, dword ptr [r12 + 0x1b00]
+movss dword ptr [rbx + 4], xmm0
+mov rax, rbx
 pxor xmm0, xmm0
-cvtsi2ss xmm0, eax
 mov dword ptr [rbx], 1
-mov rax, rbx
-movss dword ptr [rbx + 4], xmm0
-pxor xmm0, xmm0
 movups xmmword ptr [rbx + 8], xmm0
 pop rbx
@@ -46,5 +44,4 @@
 pop rbp
 ret
-nop word ptr cs:[rax + rax]
-mov eax, dword ptr [r12 + 0x1b04]
+movss xmm0, dword ptr [r12 + 0x1b04]
 jmp L
```

### изменена: 0x4ecd300 (116 байт) вызывается из: CDOTA_Modifier_Orb_Of_Corrosion_Debuff::vfunc#88 | строки: "modifier_item_skadi_slow"
было: 0x4ecd2b0 (117 байт)
- константы из данных (числа логики): +-0,0,0,0
- числа в инструкциях: +0 +0
- инструкций: 36 → 34
```diff
@@ -22,10 +22,8 @@
 ret
 nop word ptr [rax + rax]
-mov eax, dword ptr [r12 + 0x1afc]
-pxor xmm0, xmm0
+movss xmm0, dword ptr [r12 + 0x1afc]
 mov dword ptr [rbx], 1
-neg eax
-cvtsi2ss xmm0, eax
 mov rax, rbx
+xorps xmm0, xmmword ptr [K:-0,0,0,0]
 movss dword ptr [rbx + 4], xmm0
 pxor xmm0, xmm0
```

### изменена: 0x4ecb150 (151 байт) вызывается из: CDOTA_Modifier_Orb_Of_Corrosion_Debuff::vfunc#88 | строки: "modifier_desolator_buff"; "modifier_stygian_desolator_buff"
было: 0x4ecd330 (155 байт)
- инструкций: 42 → 41
```diff
@@ -34,7 +34,6 @@
 test rax, rax
 jne L
-pxor xmm0, xmm0
+movss xmm0, dword ptr [r12 + 0x1af8]
 mov dword ptr [rbx], 1
-cvtsi2ss xmm0, dword ptr [r12 + 0x1af8]
 movss dword ptr [rbx + 4], xmm0
 pxor xmm0, xmm0
```

### изменена: 0x4ed6e40 (1027 байт) CDOTA_Modifier_Orb_Of_Corrosion_Debuff::vfunc#79 | строки: "corruption_armor"; "heal_reduction"; "slow_melee"; "slow_ranged"; "AbilityManaCost"; "AbilityHealthCost"
было: 0x4ed3150 (287 байт)
- строки: +"AbilityManaCost" +"AbilityHealthCost"
- константы из данных (числа логики): +0.5 +100
- числа в инструкциях: +-1 +0 +1 +1 +2 +2 +0x3f800000
- виртуальные вызовы: +0x10c8 (слот 537)
- поля объектов: +0x18 +0x18 +0x814 +0xa60 +0xe74 +0xe74 +0x770 +0x770 +0x116
- прямых вызовов: 11 → 28
- инструкций: 70 → 251
```diff
@@ -1,18 +1,49 @@
 push rbp
 mov rbp, rsp
+push r15
+push r14
+push r13
 push r12
 push rbx
 mov rbx, rdi
-call F
-mov rdi, rbx
-mov r12, rax
-mov rax, qword ptr [rbx]
-call qword ptr [rax + 0x1a8]
-test r12, r12
-je L
-lea rsi, [rbx + 0x1af8]
-mov rdi, r12
-lea rdx, [S:"corruption_armor"]
-call F
+sub rsp, 0x28
+call F
+mov rdi, rbx
+mov r12, rax
+mov rax, qword ptr [rbx]
+call qword ptr [rax + 0x1a8]
+test r12, r12
+movss dword ptr [rbp - 0x44], xmm0
+pxor xmm0, xmm0
+je L
+mov rdi, r12
+call F
+cmp eax, -1
+mov r13d, eax
+je L
+lea r15, [S:"corruption_armor"]
+mov rdi, r12
+mov rsi, r15
+call F
+test rax, rax
+mov r14, rax
+je L
+mov rdi, r12
+call F
+test rax, rax
+je L
+mov rdi, r12
+call F
+lea r8, [rbp - 0x34]
+mov ecx, r13d
+mov rdx, r15
+mov rdi, rax
+mov rsi, r12
+call F
+test al, al
+je L
+movss xmm0, dword ptr [rbp - 0x34]
+nop dword ptr [rax + rax]
+movss dword ptr [rbx + 0x1af8], xmm0
 mov rdi, rbx
 call F
@@ -47,24 +78,174 @@
 test r12, r12
 je L
+lea rsp, [rbp - 0x28]
+mov rdi, r12
 lea rsi, [rbx + 0x1b04]
-mov rdi, r12
 pop rbx
 pop r12
+pop r13
+pop r14
+pop r15
 pop rbp
 lea rdx, [S:"slow_ranged"]
 jmp F
-nop dword ptr [rax + rax]
-mov dword ptr [rbx + 0x1af8], 0
+nop dword ptr [rax]
+pxor xmm0, xmm0
+jmp L
+nop dword ptr [rax]
+mov dword ptr [rbx + 0x1afc], 0
 jmp L
 nop
 mov dword ptr [rbx + 0x1b04], 0
+lea rsp, [rbp - 0x28]
 pop rbx
 pop r12
+pop r13
+pop r14
+pop r15
 pop rbp
 ret
+nop dword ptr [rax]
+mov dword ptr [rbx + 0x1b00], 0
+jmp L
 nop
-mov dword ptr [rbx + 0x1b00], 0
-jmp L
-nop dword ptr [rax]
-mov dword ptr [rbx + 0x1afc], 0
-jmp L
+mov eax, dword ptr [r14 + 0x18]
+pxor xmm0, xmm0
+lea edx, [rax - 1]
+cmp r13d, edx
+mov ecx, edx
+cmovle ecx, r13d
+test ecx, ecx
+js L
+movsxd rsi, ecx
+movss xmm0, dword ptr [r14 + rsi*4 + 0x1c]
+cmp eax, 1
+movss dword ptr [rbp - 0x3c], xmm0
+setg al
+and al, byte ptr [r12 + 0x814]
+je L
+cmp r13d, edx
+jg L
```
(ещё 124 строк диффа: so-query.py fdiff libclient.so 0x4ed6e40)

### изменена: 0x4ed3220 (495 байт) CDOTA_Modifier_Item_Naginata::OnCreated | строки: "bonus_intellect"; "bonus_attack_speed"; "bonus_damage"; "bonus_health"; "bonus_mana_regen"; "cooldown_reduction_percent"; "bonus_chance"
было: 0x4ed4e10 (1251 байт)
- строки: −"AbilityManaCost" −"AbilityHealthCost"
- константы из данных (числа логики): −0.5 −100
- числа в инструкциях: −-1 −0 −1 −1 −2 −2 −0x3f800000
- виртуальные вызовы: −0x10c8 (слот 537)
- поля объектов: −0x18 −0x18 −0x814 −0xa60 −0xe74 −0xe74 −0x770 −0x770 −0x116
- прямых вызовов: 37 → 20
- инструкций: 296 → 115
```diff
@@ -1,11 +1,7 @@
 push rbp
 mov rbp, rsp
-push r15
-push r14
-push r13
 push r12
 push rbx
 mov rbx, rdi
-sub rsp, 0x28
 call F
 mov rdi, rbx
@@ -62,36 +58,9 @@
 call qword ptr [rax + 0x1a8]
 test r12, r12
-movss dword ptr [rbp - 0x44], xmm0
-pxor xmm0, xmm0
 je L
+lea rsi, [rbx + 0x1b08]
 mov rdi, r12
+lea rdx, [S:"bonus_mana_regen"]
 call F
-cmp eax, -1
-mov r13d, eax
-je L
-lea r15, [S:"bonus_mana_regen"]
-mov rdi, r12
-mov rsi, r15
-call F
-test rax, rax
-mov r14, rax
-je L
-mov rdi, r12
-call F
-test rax, rax
-je L
-mov rdi, r12
-call F
-lea r8, [rbp - 0x34]
-mov ecx, r13d
-mov rdx, r15
-mov rdi, rax
-mov rsi, r12
-call F
-test al, al
-je L
-movss xmm0, dword ptr [rbp - 0x34]
-nop dword ptr [rax + rax]
-movss dword ptr [rbx + 0x1b08], xmm0
 mov rdi, rbx
 call F
@@ -114,23 +83,25 @@
 test r12, r12
 je L
-lea rsp, [rbp - 0x28]
+lea rsi, [rbx + 0x1b10]
 mov rdi, r12
-lea rsi, [rbx + 0x1b10]
 pop rbx
 pop r12
-pop r13
-pop r14
-pop r15
 pop rbp
 lea rdx, [S:"bonus_chance"]
 jmp F
-nop word ptr [rax + rax]
-pxor xmm0, xmm0
+nop dword ptr [rax]
+mov dword ptr [rbx + 0x1af8], 0
+jmp L
+nop
+mov dword ptr [rbx + 0x1b10], 0
+pop rbx
+pop r12
+pop rbp
+ret
+nop
+mov dword ptr [rbx + 0x1b0c], 0
 jmp L
 nop dword ptr [rax]
-mov dword ptr [rbx + 0x1b00], 0
-jmp L
-nop word ptr [rax + rax]
-mov dword ptr [rbx + 0x1afc], 0
+mov dword ptr [rbx + 0x1b08], 0
 jmp L
 nop
@@ -138,159 +109,7 @@
 jmp L
 nop
-mov dword ptr [rbx + 0x1b0c], 0
+mov dword ptr [rbx + 0x1b00], 0
 jmp L
 nop
-mov dword ptr [rbx + 0x1af8], 0
+mov dword ptr [rbx + 0x1afc], 0
 jmp L
-nop
-mov dword ptr [rbx + 0x1b10], 0
-lea rsp, [rbp - 0x28]
-pop rbx
-pop r12
-pop r13
-pop r14
-pop r15
-pop rbp
-ret
-nop dword ptr [rax]
-mov eax, dword ptr [r14 + 0x18]
-pxor xmm0, xmm0
-lea edx, [rax - 1]
-cmp r13d, edx
-mov ecx, edx
-cmovle ecx, r13d
-test ecx, ecx
-js L
-movsxd rsi, ecx
-movss xmm0, dword ptr [r14 + rsi*4 + 0x1c]
-cmp eax, 1
```
(ещё 130 строк диффа: so-query.py fdiff libclient.so 0x4ed3220)

### изменена: 0x4ed6250 (963 байт) CDOTA_Modifier_Item_Ocean_Heart::OnCreated | строки: "water_hp_regen"; "water_mp_regen"; "all_stats"; "AbilityManaCost"; "AbilityHealthCost"
было: 0x4ed5300 (1709 байт)
- строки: −"AbilityManaCost" −"AbilityHealthCost"
- константы из данных (числа логики): −0.5 −100
- числа в инструкциях: −-1 −0 −1 −1 −2 −2 −0x3f800000
- виртуальные вызовы: −0x10c8 (слот 537)
- поля объектов: −0x18 −0x18 −0x814 −0xa60 −0xe74 −0xe74 −0x770 −0x770 −0x116
- прямых вызовов: 43 → 26
- инструкций: 402 → 232
```diff
@@ -53,36 +53,9 @@
 call qword ptr [rax + 0x1a8]
 test r12, r12
-movss dword ptr [rbp - 0x44], xmm0
-pxor xmm0, xmm0
-je L
-mov rdi, r12
-call F
-cmp eax, -1
-mov r13d, eax
-je L
-lea r15, [S:"water_mp_regen"]
-mov rdi, r12
-mov rsi, r15
-call F
-test rax, rax
-mov r14, rax
-je L
-mov rdi, r12
-call F
-test rax, rax
-je L
-mov rdi, r12
-call F
-lea r8, [rbp - 0x34]
-mov ecx, r13d
-mov rdx, r15
-mov rdi, rax
-mov rsi, r12
-call F
-test al, al
-je L
-movss xmm0, dword ptr [rbp - 0x34]
-nop word ptr [rax + rax]
-movss dword ptr [rbx + 0x1afc], xmm0
+je L
+lea rsi, [rbx + 0x1afc]
+mov rdi, r12
+lea rdx, [S:"water_mp_regen"]
+call F
 mov rdi, rbx
 call F
@@ -107,13 +80,14 @@
 pop rbp
 jmp F
+nop word ptr cs:[rax + rax]
 pxor xmm0, xmm0
 jmp L
 nop dword ptr [rax]
-pxor xmm0, xmm0
-jmp L
-nop word ptr cs:[rax + rax]
 mov dword ptr [rbx + 0x1b00], 0
 jmp L
 nop dword ptr [rax]
+mov dword ptr [rbx + 0x1afc], 0
+jmp L
+nop
 mov eax, dword ptr [r14 + 0x18]
 pxor xmm0, xmm0
@@ -186,76 +160,4 @@
 movss xmm0, dword ptr [rbp - 0x3c]
 jmp L
-nop dword ptr [rax]
-mov eax, dword ptr [r14 + 0x18]
-pxor xmm0, xmm0
-lea edx, [rax - 1]
-cmp r13d, edx
-mov ecx, edx
-cmovle ecx, r13d
-test ecx, ecx
-js L
-movsxd rsi, ecx
-movss xmm0, dword ptr [r14 + rsi*4 + 0x1c]
-cmp eax, 1
-movss dword ptr [rbp - 0x3c], xmm0
-setg al
-and al, byte ptr [r12 + 0x814]
-je L
-cmp r13d, edx
-jg L
-mov rdi, r12
-call F
-test rax, rax
-je L
-mov rdi, r12
-call F
-lea rcx, [T]
-mov rdx, rax
-mov rax, qword ptr [rax]
-mov rax, qword ptr [rax + 0xa60]
-cmp rax, rcx
-jne L
-mov eax, dword ptr [rdx + 0xe74]
-and eax, 1
-test al, al
-jne L
-test byte ptr [rdx + 0xe74], 2
-jne L
-nop dword ptr [rax + rax]
-mov rdi, r12
-call F
-test rax, rax
-mov rdi, rax
-je L
-lea rcx, [rbp - 0x38]
-mov rdx, r15
-mov rsi, r12
-mov dword ptr [rbp - 0x38], 0x3f800000
-lea r8, [rbp - 0x34]
-mov dword ptr [rbp - 0x34], 0
-call F
-movss xmm0, dword ptr [rbp - 0x3c]
-mulss xmm0, dword ptr [rbp - 0x38]
-addss xmm0, dword ptr [rbp - 0x34]
-movss dword ptr [rbp - 0x3c], xmm0
-pxor xmm0, xmm0
-comiss xmm0, dword ptr [rbp - 0x44]
-ja L
-mov rdi, qword ptr [r12 + 0x770]
```
(ещё 119 строк диффа: so-query.py fdiff libclient.so 0x4ed6250)

### изменена: 0x4ed6620 (1027 байт) CDOTA_Modifier_MetamorphicMandible_Active::OnCreated | строки: "bonus_magic_resistance"; "bonus_movespeed"; "size_decrease"; "armor_decrease"; "AbilityManaCost"; "AbilityHealthCost"
было: 0x4ed59b0 (1789 байт)
- строки: −"AbilityManaCost" −"AbilityHealthCost"
- константы из данных (числа логики): −0.5 −100
- числа в инструкциях: −-1 −0 −1 −1 −2 −2 −0x3f800000
- виртуальные вызовы: −0x10c8 (слот 537)
- поля объектов: −0x18 −0x18 −0x814 −0xa60 −0xe74 −0xe74 −0x770 −0x770 −0x116
- прямых вызовов: 45 → 28
- инструкций: 422 → 251
```diff
@@ -53,36 +53,9 @@
 call qword ptr [rax + 0x1a8]
 test r12, r12
-movss dword ptr [rbp - 0x44], xmm0
-pxor xmm0, xmm0
-je L
-mov rdi, r12
-call F
-cmp eax, -1
-mov r13d, eax
-je L
-lea r15, [S:"bonus_movespeed"]
-mov rdi, r12
-mov rsi, r15
-call F
-test rax, rax
-mov r14, rax
-je L
-mov rdi, r12
-call F
-test rax, rax
-je L
-mov rdi, r12
-call F
-lea r8, [rbp - 0x34]
-mov ecx, r13d
-mov rdx, r15
-mov rdi, rax
-mov rsi, r12
-call F
-test al, al
-je L
-movss xmm0, dword ptr [rbp - 0x34]
-nop word ptr [rax + rax]
-movss dword ptr [rbx + 0x1afc], xmm0
+je L
+lea rsi, [rbx + 0x1afc]
+mov rdi, r12
+lea rdx, [S:"bonus_movespeed"]
+call F
 mov rdi, rbx
 call F
@@ -116,11 +89,11 @@
 lea rdx, [S:"armor_decrease"]
 jmp F
-nop word ptr cs:[rax + rax]
-pxor xmm0, xmm0
-jmp L
-nop dword ptr [rax]
-pxor xmm0, xmm0
-jmp L
-nop dword ptr [rax]
+nop dword ptr [rax]
+pxor xmm0, xmm0
+jmp L
+nop dword ptr [rax]
+mov dword ptr [rbx + 0x1afc], 0
+jmp L
+nop
 mov dword ptr [rbx + 0x1b04], 0
 lea rsp, [rbp - 0x28]
@@ -206,76 +179,4 @@
 movss xmm0, dword ptr [rbp - 0x3c]
 jmp L
-nop dword ptr [rax]
-mov eax, dword ptr [r14 + 0x18]
-pxor xmm0, xmm0
-lea edx, [rax - 1]
-cmp r13d, edx
-mov ecx, edx
-cmovle ecx, r13d
-test ecx, ecx
-js L
-movsxd rsi, ecx
-movss xmm0, dword ptr [r14 + rsi*4 + 0x1c]
-cmp eax, 1
-movss dword ptr [rbp - 0x3c], xmm0
-setg al
-and al, byte ptr [r12 + 0x814]
-je L
-cmp r13d, edx
-jg L
-mov rdi, r12
-call F
-test rax, rax
-je L
-mov rdi, r12
-call F
-lea rcx, [T]
-mov rdx, rax
-mov rax, qword ptr [rax]
-mov rax, qword ptr [rax + 0xa60]
-cmp rax, rcx
-jne L
-mov eax, dword ptr [rdx + 0xe74]
-and eax, 1
-test al, al
-jne L
-test byte ptr [rdx + 0xe74], 2
-jne L
-nop dword ptr [rax + rax]
-mov rdi, r12
-call F
-test rax, rax
-mov rdi, rax
-je L
-lea rcx, [rbp - 0x38]
-mov rdx, r15
-mov rsi, r12
-mov dword ptr [rbp - 0x38], 0x3f800000
-lea r8, [rbp - 0x34]
-mov dword ptr [rbp - 0x34], 0
-call F
-movss xmm0, dword ptr [rbp - 0x3c]
-mulss xmm0, dword ptr [rbp - 0x38]
-addss xmm0, dword ptr [rbp - 0x34]
-movss dword ptr [rbp - 0x3c], xmm0
-pxor xmm0, xmm0
-comiss xmm0, dword ptr [rbp - 0x44]
-ja L
```
(ещё 129 строк диффа: so-query.py fdiff libclient.so 0x4ed6620)

### изменена: 0x4ed6a30 (1027 байт) CDOTA_Modifier_Item_Misericorde::OnCreated | строки: "bonus_damage"; "missing_hp"; "damage"; "aspd"; "AbilityManaCost"; "AbilityHealthCost"
было: 0x4ed60b0 (1789 байт)
- строки: −"AbilityManaCost" −"AbilityHealthCost"
- константы из данных (числа логики): −0.5 −100
- числа в инструкциях: −-1 −0 −1 −1 −2 −2 −0x3f800000
- виртуальные вызовы: −0x10c8 (слот 537)
- поля объектов: −0x18 −0x18 −0x814 −0xa60 −0xe74 −0xe74 −0x770 −0x770 −0x116
- прямых вызовов: 45 → 28
- инструкций: 422 → 251
```diff
@@ -65,36 +65,9 @@
 call qword ptr [rax + 0x1a8]
 test r12, r12
-movss dword ptr [rbp - 0x44], xmm0
-pxor xmm0, xmm0
-je L
-mov rdi, r12
-call F
-cmp eax, -1
-mov r13d, eax
-je L
-lea r15, [S:"damage"]
-mov rdi, r12
-mov rsi, r15
-call F
-test rax, rax
-mov r14, rax
-je L
-mov rdi, r12
-call F
-test rax, rax
-je L
-mov rdi, r12
-call F
-lea r8, [rbp - 0x34]
-mov ecx, r13d
-mov rdx, r15
-mov rdi, rax
-mov rsi, r12
-call F
-test al, al
-je L
-movss xmm0, dword ptr [rbp - 0x34]
-nop dword ptr [rax + rax]
-movss dword ptr [rbx + 0x1b00], xmm0
+je L
+lea rsi, [rbx + 0x1b00]
+mov rdi, r12
+lea rdx, [S:"damage"]
+call F
 mov rdi, rbx
 call F
@@ -116,11 +89,8 @@
 lea rdx, [S:"aspd"]
 jmp F
-nop dword ptr [rax + rax]
-pxor xmm0, xmm0
-jmp L
-nop dword ptr [rax]
-pxor xmm0, xmm0
-jmp L
-nop word ptr cs:[rax + rax]
+nop dword ptr [rax]
+pxor xmm0, xmm0
+jmp L
+nop dword ptr [rax]
 mov dword ptr [rbx + 0x1afc], 0
 jmp L
@@ -136,4 +106,7 @@
 ret
 nop dword ptr [rax]
+mov dword ptr [rbx + 0x1b00], 0
+jmp L
+nop
 mov eax, dword ptr [r14 + 0x18]
 pxor xmm0, xmm0
@@ -206,76 +179,4 @@
 movss xmm0, dword ptr [rbp - 0x3c]
 jmp L
-nop dword ptr [rax]
-mov eax, dword ptr [r14 + 0x18]
-pxor xmm0, xmm0
-lea edx, [rax - 1]
-cmp r13d, edx
-mov ecx, edx
-cmovle ecx, r13d
-test ecx, ecx
-js L
-movsxd rsi, ecx
-movss xmm0, dword ptr [r14 + rsi*4 + 0x1c]
-cmp eax, 1
-movss dword ptr [rbp - 0x3c], xmm0
-setg al
-and al, byte ptr [r12 + 0x814]
-je L
-cmp r13d, edx
-jg L
-mov rdi, r12
-call F
-test rax, rax
-je L
-mov rdi, r12
-call F
-lea rcx, [T]
-mov rdx, rax
-mov rax, qword ptr [rax]
-mov rax, qword ptr [rax + 0xa60]
-cmp rax, rcx
-jne L
-mov eax, dword ptr [rdx + 0xe74]
-and eax, 1
-test al, al
-jne L
-test byte ptr [rdx + 0xe74], 2
-jne L
-nop dword ptr [rax + rax]
-mov rdi, r12
-call F
-test rax, rax
-mov rdi, rax
-je L
-lea rcx, [rbp - 0x38]
-mov rdx, r15
-mov rsi, r12
-mov dword ptr [rbp - 0x38], 0x3f800000
-lea r8, [rbp - 0x34]
-mov dword ptr [rbp - 0x34], 0
-call F
-movss xmm0, dword ptr [rbp - 0x3c]
-mulss xmm0, dword ptr [rbp - 0x38]
```
(ещё 134 строк диффа: so-query.py fdiff libclient.so 0x4ed6a30)

### изменена: 0x4ed7670 (1171 байт) CDOTA_Modifier_OgreSealTotem_Active::OnCreated | строки: "leap_distance"; "leap_speed"; "leap_acceleration"; "leap_radius"; "leap_bonus_duration"; "movement_turn_rate"; "AbilityManaCost"; "AbilityHealthCost"
было: 0x4ed67b0 (1917 байт)
- строки: −"AbilityManaCost" −"AbilityHealthCost"
- константы из данных (числа логики): −0.5 −100
- числа в инструкциях: −-1 −0 −1 −1 −2 −2 −0x3f800000
- виртуальные вызовы: −0x10c8 (слот 537)
- поля объектов: −0x18 −0x18 −0x814 −0xa60 −0xe74 −0xe74 −0x770 −0x770 −0x116
- прямых вызовов: 52 → 35
- инструкций: 447 → 276
```diff
@@ -65,36 +65,9 @@
 call qword ptr [rax + 0x1a8]
 test r12, r12
-movss dword ptr [rbp - 0x44], xmm0
-pxor xmm0, xmm0
-je L
-mov rdi, r12
-call F
-cmp eax, -1
-mov r13d, eax
-je L
-lea r15, [S:"leap_acceleration"]
-mov rdi, r12
-mov rsi, r15
-call F
-test rax, rax
-mov r14, rax
-je L
-mov rdi, r12
-call F
-test rax, rax
-je L
-mov rdi, r12
-call F
-lea r8, [rbp - 0x34]
-mov ecx, r13d
-mov rdx, r15
-mov rdi, rax
-mov rsi, r12
-call F
-test al, al
-je L
-movss xmm0, dword ptr [rbp - 0x34]
-nop word ptr [rax + rax]
-movss dword ptr [rbx + 0x1b04], xmm0
+je L
+lea rsi, [rbx + 0x1b04]
+mov rdi, r12
+lea rdx, [S:"leap_acceleration"]
+call F
 mov rdi, rbx
 call F
@@ -142,21 +115,21 @@
 pop rbp
 ret
-nop dword ptr [rax]
-pxor xmm0, xmm0
-jmp L
-nop dword ptr [rax]
-pxor xmm0, xmm0
-jmp L
-nop dword ptr [rax]
+nop word ptr [rax + rax]
+pxor xmm0, xmm0
+jmp L
+nop dword ptr [rax]
+mov dword ptr [rbx + 0x1b04], 0
+jmp L
+nop word ptr [rax + rax]
 mov dword ptr [rbx + 0x1afc], 0
 jmp L
 nop
+mov dword ptr [rbx + 0x1b18], 0
+jmp L
+nop dword ptr [rax]
+mov dword ptr [rbx + 0x1b0c], 0
+jmp L
+nop
 mov dword ptr [rbx + 0x1b08], 0
-jmp L
-nop
-mov dword ptr [rbx + 0x1b18], 0
-jmp L
-nop dword ptr [rax]
-mov dword ptr [rbx + 0x1b0c], 0
 jmp L
 nop
@@ -231,76 +204,4 @@
 movss xmm0, dword ptr [rbp - 0x3c]
 jmp L
-nop dword ptr [rax]
-mov eax, dword ptr [r14 + 0x18]
-pxor xmm0, xmm0
-lea edx, [rax - 1]
-cmp r13d, edx
-mov ecx, edx
-cmovle ecx, r13d
-test ecx, ecx
-js L
-movsxd rsi, ecx
-movss xmm0, dword ptr [r14 + rsi*4 + 0x1c]
-cmp eax, 1
-movss dword ptr [rbp - 0x3c], xmm0
-setg al
-and al, byte ptr [r12 + 0x814]
-je L
-cmp r13d, edx
-jg L
-mov rdi, r12
-call F
-test rax, rax
-je L
-mov rdi, r12
-call F
-lea rcx, [T]
-mov rdx, rax
-mov rax, qword ptr [rax]
-mov rax, qword ptr [rax + 0xa60]
-cmp rax, rcx
-jne L
-mov eax, dword ptr [rdx + 0xe74]
-and eax, 1
-test al, al
-jne L
-test byte ptr [rdx + 0xe74], 2
-jne L
-nop dword ptr [rax + rax]
-mov rdi, r12
-call F
-test rax, rax
```
(ещё 145 строк диффа: so-query.py fdiff libclient.so 0x4ed7670)

### изменена: 0x4edd0f0 (851 байт) CDOTA_Modifier_Item_Nothl_Sigil::OnCreated | строки: "mana_cost_reduction_pct"; "health_cost_pct"; "AbilityManaCost"; "AbilityHealthCost"
было: 0x4edc7b0 (154 байт)
- строки: +"AbilityManaCost" +"AbilityHealthCost"
- константы из данных (числа логики): +0.5 +100
- числа в инструкциях: +-1 +1 +1 +2 +2 +0x3f800000 +0 +0 −0xffffffff
- виртуальные вызовы: +0x10c8 (слот 537)
- поля объектов: +0x18 +0x18 +0x814 +0xa60 +0xe74 +0xe74 +0x770 +0x770 +0x116
- прямых вызовов: 6 → 23
- инструкций: 44 → 217
```diff
@@ -1,7 +1,11 @@
 push rbp
 mov rbp, rsp
+push r15
+push r14
+push r13
 push r12
 push rbx
 mov rbx, rdi
+sub rsp, 0x28
 call F
 mov rdi, rbx
@@ -28,17 +32,186 @@
 call qword ptr [rax + 0x1a8]
 test r12, r12
-pxor xmm1, xmm1
-je L
-xor r9d, r9d
-xor r8d, r8d
-xor ecx, ecx
-lea rsi, [S:"health_cost_pct"]
-mov edx, 0xffffffff
-mov rdi, r12
-call F
-movaps xmm1, xmm0
-movss dword ptr [rbx + 0x1afc], xmm1
+movss dword ptr [rbp - 0x44], xmm0
+pxor xmm0, xmm0
+je L
+mov rdi, r12
+call F
+cmp eax, -1
+mov r13d, eax
+je L
+lea r15, [S:"health_cost_pct"]
+mov rdi, r12
+mov rsi, r15
+call F
+test rax, rax
+mov r14, rax
+je L
+mov rdi, r12
+call F
+test rax, rax
+je L
+mov rdi, r12
+call F
+lea r8, [rbp - 0x34]
+mov ecx, r13d
+mov rdx, r15
+mov rdi, rax
+mov rsi, r12
+call F
+test al, al
+je L
+movss xmm0, dword ptr [rbp - 0x34]
+movss dword ptr [rbx + 0x1afc], xmm0
+lea rsp, [rbp - 0x28]
 pop rbx
 pop r12
+pop r13
+pop r14
+pop r15
 pop rbp
 ret
+nop dword ptr [rax]
+pxor xmm0, xmm0
+jmp L
+nop
+mov eax, dword ptr [r14 + 0x18]
+pxor xmm0, xmm0
+lea edx, [rax - 1]
+cmp r13d, edx
+mov ecx, edx
+cmovle ecx, r13d
+test ecx, ecx
+js L
+movsxd rsi, ecx
+movss xmm0, dword ptr [r14 + rsi*4 + 0x1c]
+cmp eax, 1
+movss dword ptr [rbp - 0x3c], xmm0
+setg al
+and al, byte ptr [r12 + 0x814]
+je L
+cmp r13d, edx
+jg L
+mov rdi, r12
+call F
+test rax, rax
+je L
+mov rdi, r12
+call F
+lea rcx, [T]
+mov rdx, rax
+mov rax, qword ptr [rax]
+mov rax, qword ptr [rax + 0xa60]
+cmp rax, rcx
+jne L
+mov eax, dword ptr [rdx + 0xe74]
+and eax, 1
+test al, al
+jne L
+test byte ptr [rdx + 0xe74], 2
+jne L
+mov rdi, r12
+call F
+test rax, rax
+mov rdi, rax
+je L
+lea rcx, [rbp - 0x38]
+mov rdx, r15
+mov rsi, r12
+mov dword ptr [rbp - 0x38], 0x3f800000
+lea r8, [rbp - 0x34]
+mov dword ptr [rbp - 0x34], 0
+call F
+movss xmm0, dword ptr [rbp - 0x3c]
+mulss xmm0, dword ptr [rbp - 0x38]
+addss xmm0, dword ptr [rbp - 0x34]
+movss dword ptr [rbp - 0x3c], xmm0
```
(ещё 90 строк диффа: so-query.py fdiff libclient.so 0x4edd0f0)

### изменена: 0x4ed4bf0 (899 байт) CDOTA_Modifier_Item_Occult_Bracelet::OnRefresh | строки: "stack_limit"; "stack_duration"; "AbilityManaCost"; "AbilityHealthCost"
было: 0x4edc850 (207 байт)
- строки: +"AbilityManaCost" +"AbilityHealthCost"
- константы из данных (числа логики): +0.5 +100
- числа в инструкциях: +-1 +0 +0 +1 +1 +2 +2 +0x3f800000 −0xffffffff
- виртуальные вызовы: +0x10c8 (слот 537)
- поля объектов: +0x18 +0x18 +0x814 +0xa60 +0xe74 +0xe74 +0x770 +0x770 +0x116
- прямых вызовов: 8 → 25
- инструкций: 51 → 222
```diff
@@ -1,8 +1,11 @@
 push rbp
 mov rbp, rsp
+push r15
+push r14
+push r13
 push r12
 push rbx
 mov rbx, rdi
-sub rsp, 0x10
+sub rsp, 0x28
 call F
 mov rdi, rbx
@@ -24,28 +27,196 @@
 test r12, r12
 pxor xmm1, xmm1
-je L
-xor r9d, r9d
-xor r8d, r8d
-xor ecx, ecx
-lea rsi, [S:"stack_duration"]
-mov edx, 0xffffffff
-mov rdi, r12
-call F
-movaps xmm1, xmm0
+movss dword ptr [rbp - 0x44], xmm0
+je L
+mov rdi, r12
+call F
+cmp eax, -1
+mov r13d, eax
+je L
+lea r15, [S:"stack_duration"]
+mov rdi, r12
+mov rsi, r15
+call F
+test rax, rax
+mov r14, rax
+je L
+mov rdi, r12
+call F
+test rax, rax
+je L
+mov rdi, r12
+call F
+lea r8, [rbp - 0x34]
+mov ecx, r13d
+mov rdx, r15
+mov rdi, rax
+mov rsi, r12
+call F
+test al, al
+je L
+movss xmm1, dword ptr [rbp - 0x34]
 movss dword ptr [rbx + 0x1b00], xmm1
 mov rdi, rbx
-movss dword ptr [rbp - 0x14], xmm1
+movss dword ptr [rbp - 0x44], xmm1
 call F
 mov edi, eax
 call F
-movss xmm1, dword ptr [rbp - 0x14]
+movss xmm1, dword ptr [rbp - 0x44]
 addss xmm0, xmm1
 movss dword ptr [rbx + 0x1b04], xmm0
-add rsp, 0x10
+lea rsp, [rbp - 0x28]
 pop rbx
 pop r12
+pop r13
+pop r14
+pop r15
 pop rbp
 ret
+nop dword ptr [rax]
+pxor xmm1, xmm1
+jmp L
 nop word ptr cs:[rax + rax]
 mov dword ptr [rbx + 0x1afc], 0
 jmp L
+nop
+mov eax, dword ptr [r14 + 0x18]
+pxor xmm0, xmm0
+lea edx, [rax - 1]
+cmp r13d, edx
+mov ecx, edx
+cmovle ecx, r13d
+test ecx, ecx
+js L
+movsxd rsi, ecx
+movss xmm0, dword ptr [r14 + rsi*4 + 0x1c]
+cmp eax, 1
+movss dword ptr [rbp - 0x3c], xmm0
+setg al
+and al, byte ptr [r12 + 0x814]
+je L
+cmp r13d, edx
+jg L
+mov rdi, r12
+call F
+test rax, rax
+je L
+mov rdi, r12
+call F
+lea rcx, [T]
+mov rdx, rax
+mov rax, qword ptr [rax]
+mov rax, qword ptr [rax + 0xa60]
+cmp rax, rcx
+jne L
+mov eax, dword ptr [rdx + 0xe74]
+and eax, 1
+test al, al
+jne L
+test byte ptr [rdx + 0xe74], 2
+jne L
+mov rdi, r12
+call F
+test rax, rax
+mov rdi, rax
```
(ещё 102 строк диффа: so-query.py fdiff libclient.so 0x4ed4bf0)

### изменена: 0x4ed4f80 (963 байт) CDOTA_Modifier_Item_MaskOfDispair::OnCreated | строки: "bonus_strength"; "bonus_armor"; "spell_lifesteal"; "AbilityManaCost"; "AbilityHealthCost"
было: 0x4edc920 (223 байт)
- строки: +"AbilityManaCost" +"AbilityHealthCost"
- константы из данных (числа логики): +0.5 +100
- числа в инструкциях: +-1 +0 +0 +1 +1 +2 +2 +0x3f800000 −0xffffffff
- виртуальные вызовы: +0x10c8 (слот 537)
- поля объектов: +0x18 +0x18 +0x814 +0xa60 +0xe74 +0xe74 +0x770 +0x770 +0x116
- прямых вызовов: 8 → 25
- инструкций: 58 → 236
```diff
@@ -1,7 +1,11 @@
 push rbp
 mov rbp, rsp
+push r15
+push r14
+push r13
 push r12
 push rbx
 mov rbx, rdi
+sub rsp, 0x28
 call F
 mov rdi, rbx
@@ -22,15 +26,36 @@
 call qword ptr [rax + 0x1a8]
 test r12, r12
-pxor xmm1, xmm1
-je L
-xor r9d, r9d
-xor r8d, r8d
-xor ecx, ecx
-lea rsi, [S:"bonus_armor"]
-mov edx, 0xffffffff
-mov rdi, r12
-call F
-movaps xmm1, xmm0
-movss dword ptr [rbx + 0x1afc], xmm1
+movss dword ptr [rbp - 0x44], xmm0
+pxor xmm0, xmm0
+je L
+mov rdi, r12
+call F
+cmp eax, -1
+mov r13d, eax
+je L
+lea r15, [S:"bonus_armor"]
+mov rdi, r12
+mov rsi, r15
+call F
+test rax, rax
+mov r14, rax
+je L
+mov rdi, r12
+call F
+test rax, rax
+je L
+mov rdi, r12
+call F
+lea r8, [rbp - 0x34]
+mov ecx, r13d
+mov rdx, r15
+mov rdi, rax
+mov rsi, r12
+call F
+test al, al
+je L
+movss xmm0, dword ptr [rbp - 0x34]
+nop dword ptr [rax]
+movss dword ptr [rbx + 0x1afc], xmm0
 mov rdi, rbx
 call F
@@ -41,18 +66,171 @@
 test r12, r12
 je L
+lea rsp, [rbp - 0x28]
+mov rdi, r12
 lea rsi, [rbx + 0x1b00]
-mov rdi, r12
 pop rbx
 pop r12
+pop r13
+pop r14
+pop r15
 pop rbp
 lea rdx, [S:"spell_lifesteal"]
 jmp F
-nop word ptr [rax + rax]
+nop dword ptr [rax + rax]
+pxor xmm0, xmm0
+jmp L
+nop word ptr cs:[rax + rax]
 mov dword ptr [rbx + 0x1af8], 0
 jmp L
 nop
 mov dword ptr [rbx + 0x1b00], 0
+lea rsp, [rbp - 0x28]
 pop rbx
 pop r12
+pop r13
+pop r14
+pop r15
 pop rbp
 ret
+nop dword ptr [rax]
+mov eax, dword ptr [r14 + 0x18]
+pxor xmm0, xmm0
+lea edx, [rax - 1]
+cmp r13d, edx
+mov ecx, edx
+cmovle ecx, r13d
+test ecx, ecx
+js L
+movsxd rsi, ecx
+movss xmm0, dword ptr [r14 + rsi*4 + 0x1c]
+cmp eax, 1
+movss dword ptr [rbp - 0x3c], xmm0
+setg al
+and al, byte ptr [r12 + 0x814]
+je L
+cmp r13d, edx
+jg L
+mov rdi, r12
+call F
+test rax, rax
+je L
+mov rdi, r12
+call F
+lea rcx, [T]
+mov rdx, rax
+mov rax, qword ptr [rax]
+mov rax, qword ptr [rax + 0xa60]
```
(ещё 114 строк диффа: so-query.py fdiff libclient.so 0x4ed4f80)

### изменена: 0x4ed5350 (963 байт) CDOTA_Modifier_Item_Mechanical_Arm::OnCreated | строки: "bat"; "stun_duration"; "stun_chance"; "AbilityManaCost"; "AbilityHealthCost"
было: 0x4edca00 (963 байт)
- числа в инструкциях: +0 −0xffffffff
- инструкций: 239 → 236
```diff
@@ -14,15 +14,36 @@
 call qword ptr [rax + 0x1a8]
 test r12, r12
-pxor xmm1, xmm1
-je L
-xor r9d, r9d
-xor r8d, r8d
-xor ecx, ecx
-lea rsi, [S:"bat"]
-mov edx, 0xffffffff
-mov rdi, r12
-call F
-movaps xmm1, xmm0
-movss dword ptr [rbx + 0x1afc], xmm1
+movss dword ptr [rbp - 0x44], xmm0
+pxor xmm0, xmm0
+je L
+mov rdi, r12
+call F
+cmp eax, -1
+mov r13d, eax
+je L
+lea r15, [S:"bat"]
+mov rdi, r12
+mov rsi, r15
+call F
+test rax, rax
+mov r14, rax
+je L
+mov rdi, r12
+call F
+test rax, rax
+je L
+mov rdi, r12
+call F
+lea r8, [rbp - 0x34]
+mov ecx, r13d
+mov rdx, r15
+mov rdi, rax
+mov rsi, r12
+call F
+test al, al
+je L
+movss xmm0, dword ptr [rbp - 0x34]
+nop dword ptr [rax + rax]
+movss dword ptr [rbx + 0x1afc], xmm0
 mov rdi, rbx
 call F
@@ -32,36 +53,9 @@
 call qword ptr [rax + 0x1a8]
 test r12, r12
-movss dword ptr [rbp - 0x44], xmm0
-pxor xmm0, xmm0
-je L
-mov rdi, r12
-call F
-cmp eax, -1
-mov r13d, eax
-je L
-lea r15, [S:"stun_duration"]
-mov rdi, r12
-mov rsi, r15
-call F
-test rax, rax
-mov r14, rax
-je L
-mov rdi, r12
-call F
-test rax, rax
-je L
-mov rdi, r12
-call F
-lea r8, [rbp - 0x34]
-mov ecx, r13d
-mov rdx, r15
-mov rdi, rax
-mov rsi, r12
-call F
-test al, al
-je L
-movss xmm0, dword ptr [rbp - 0x34]
-nop word ptr [rax + rax]
-movss dword ptr [rbx + 0x1b00], xmm0
+je L
+lea rsi, [rbx + 0x1b00]
+mov rdi, r12
+lea rdx, [S:"stun_duration"]
+call F
 mov rdi, rbx
 call F
@@ -83,8 +77,8 @@
 lea rdx, [S:"stun_chance"]
 jmp F
-nop dword ptr [rax + rax]
-pxor xmm0, xmm0
-jmp L
 nop word ptr cs:[rax + rax]
+pxor xmm0, xmm0
+jmp L
+nop dword ptr [rax]
 mov dword ptr [rbx + 0x1b04], 0
 lea rsp, [rbp - 0x28]
@@ -97,4 +91,7 @@
 ret
 nop dword ptr [rax]
+mov dword ptr [rbx + 0x1b00], 0
+jmp L
+nop
 mov eax, dword ptr [r14 + 0x18]
 pxor xmm0, xmm0
```

### изменена: 0x4ed5720 (931 байт) CDOTA_Modifier_Item_Mind_Breaker::OnCreated | строки: "magic_damage"; "attack_speed"; "duration"; "AbilityManaCost"; "AbilityHealthCost"
было: 0x4edcdd0 (220 байт)
- строки: +"AbilityManaCost" +"AbilityHealthCost"
- константы из данных (числа логики): +0.5 +100
- числа в инструкциях: +-1 +0 +0 +1 +1 +2 +2 +0x3f800000 −0xffffffff
- виртуальные вызовы: +0x10c8 (слот 537)
- поля объектов: +0x18 +0x18 +0x814 +0xa60 +0xe74 +0xe74 +0x770 +0x770 +0x116
- прямых вызовов: 9 → 26
- инструкций: 56 → 229
```diff
@@ -1,7 +1,11 @@
 push rbp
 mov rbp, rsp
+push r15
+push r14
+push r13
 push r12
 push rbx
 mov rbx, rdi
+sub rsp, 0x28
 call F
 mov rdi, rbx
@@ -34,23 +38,192 @@
 call qword ptr [rax + 0x1a8]
 test r12, r12
-pxor xmm1, xmm1
-je L
-xor r9d, r9d
-xor r8d, r8d
-xor ecx, ecx
-lea rsi, [S:"duration"]
-mov edx, 0xffffffff
-mov rdi, r12
-call F
-movaps xmm1, xmm0
-movss dword ptr [rbx + 0x1b00], xmm1
+movss dword ptr [rbp - 0x44], xmm0
+pxor xmm0, xmm0
+je L
+mov rdi, r12
+call F
+cmp eax, -1
+mov r13d, eax
+je L
+lea r15, [S:"duration"]
+mov rdi, r12
+mov rsi, r15
+call F
+test rax, rax
+mov r14, rax
+je L
+mov rdi, r12
+call F
+test rax, rax
+je L
+mov rdi, r12
+call F
+lea r8, [rbp - 0x34]
+mov ecx, r13d
+mov rdx, r15
+mov rdi, rax
+mov rsi, r12
+call F
+test al, al
+je L
+movss xmm0, dword ptr [rbp - 0x34]
+movss dword ptr [rbx + 0x1b00], xmm0
+lea rsp, [rbp - 0x28]
 pop rbx
 pop r12
+pop r13
+pop r14
+pop r15
 pop rbp
 ret
-nop dword ptr [rax + rax]
+nop word ptr cs:[rax + rax]
+pxor xmm0, xmm0
+jmp L
+nop word ptr cs:[rax + rax]
+mov dword ptr [rbx + 0x1afc], 0
+jmp L
+nop
 mov dword ptr [rbx + 0x1af8], 0
 jmp L
 nop
-mov dword ptr [rbx + 0x1afc], 0
-jmp L
+mov eax, dword ptr [r14 + 0x18]
+pxor xmm0, xmm0
+lea edx, [rax - 1]
+cmp r13d, edx
+mov ecx, edx
+cmovle ecx, r13d
+test ecx, ecx
+js L
+movsxd rsi, ecx
+movss xmm0, dword ptr [r14 + rsi*4 + 0x1c]
+cmp eax, 1
+movss dword ptr [rbp - 0x3c], xmm0
+setg al
+and al, byte ptr [r12 + 0x814]
+je L
+cmp r13d, edx
+jg L
+mov rdi, r12
+call F
+test rax, rax
+je L
+mov rdi, r12
+call F
+lea rcx, [T]
+mov rdx, rax
+mov rax, qword ptr [rax]
+mov rax, qword ptr [rax + 0xa60]
+cmp rax, rcx
+jne L
+mov eax, dword ptr [rdx + 0xe74]
+and eax, 1
+test al, al
+jne L
+test byte ptr [rdx + 0xe74], 2
+jne L
+mov rdi, r12
+call F
+test rax, rax
+mov rdi, rax
+je L
+lea rcx, [rbp - 0x38]
+mov rdx, r15
```
(ещё 99 строк диффа: so-query.py fdiff libclient.so 0x4ed5720)

### изменена: 0x4ed5ad0 (931 байт) CDOTA_Modifier_Item_Orb_Of_Frost::OnCreated | строки: "armor"; "attack_speed"; "duration"; "AbilityManaCost"; "AbilityHealthCost"
было: 0x4edceb0 (220 байт)
- строки: +"AbilityManaCost" +"AbilityHealthCost"
- константы из данных (числа логики): +0.5 +100
- числа в инструкциях: +-1 +0 +0 +1 +1 +2 +2 +0x3f800000 −0xffffffff
- виртуальные вызовы: +0x10c8 (слот 537)
- поля объектов: +0x18 +0x18 +0x814 +0xa60 +0xe74 +0xe74 +0x770 +0x770 +0x116
- прямых вызовов: 9 → 26
- инструкций: 56 → 229
```diff
@@ -1,7 +1,11 @@
 push rbp
 mov rbp, rsp
+push r15
+push r14
+push r13
 push r12
 push rbx
 mov rbx, rdi
+sub rsp, 0x28
 call F
 mov rdi, rbx
@@ -34,23 +38,192 @@
 call qword ptr [rax + 0x1a8]
 test r12, r12
-pxor xmm1, xmm1
-je L
-xor r9d, r9d
-xor r8d, r8d
-xor ecx, ecx
-lea rsi, [S:"duration"]
-mov edx, 0xffffffff
-mov rdi, r12
-call F
-movaps xmm1, xmm0
-movss dword ptr [rbx + 0x1b00], xmm1
+movss dword ptr [rbp - 0x44], xmm0
+pxor xmm0, xmm0
+je L
+mov rdi, r12
+call F
+cmp eax, -1
+mov r13d, eax
+je L
+lea r15, [S:"duration"]
+mov rdi, r12
+mov rsi, r15
+call F
+test rax, rax
+mov r14, rax
+je L
+mov rdi, r12
+call F
+test rax, rax
+je L
+mov rdi, r12
+call F
+lea r8, [rbp - 0x34]
+mov ecx, r13d
+mov rdx, r15
+mov rdi, rax
+mov rsi, r12
+call F
+test al, al
+je L
+movss xmm0, dword ptr [rbp - 0x34]
+movss dword ptr [rbx + 0x1b00], xmm0
+lea rsp, [rbp - 0x28]
 pop rbx
 pop r12
+pop r13
+pop r14
+pop r15
 pop rbp
 ret
-nop dword ptr [rax + rax]
+nop word ptr cs:[rax + rax]
+pxor xmm0, xmm0
+jmp L
+nop word ptr cs:[rax + rax]
+mov dword ptr [rbx + 0x1afc], 0
+jmp L
+nop
 mov dword ptr [rbx + 0x1af8], 0
 jmp L
 nop
-mov dword ptr [rbx + 0x1afc], 0
-jmp L
+mov eax, dword ptr [r14 + 0x18]
+pxor xmm0, xmm0
+lea edx, [rax - 1]
+cmp r13d, edx
+mov ecx, edx
+cmovle ecx, r13d
+test ecx, ecx
+js L
+movsxd rsi, ecx
+movss xmm0, dword ptr [r14 + rsi*4 + 0x1c]
+cmp eax, 1
+movss dword ptr [rbp - 0x3c], xmm0
+setg al
+and al, byte ptr [r12 + 0x814]
+je L
+cmp r13d, edx
+jg L
+mov rdi, r12
+call F
+test rax, rax
+je L
+mov rdi, r12
+call F
+lea rcx, [T]
+mov rdx, rax
+mov rax, qword ptr [rax]
+mov rax, qword ptr [rax + 0xa60]
+cmp rax, rcx
+jne L
+mov eax, dword ptr [rdx + 0xe74]
+and eax, 1
+test al, al
+jne L
+test byte ptr [rdx + 0xe74], 2
+jne L
+mov rdi, r12
+call F
+test rax, rax
+mov rdi, rax
+je L
+lea rcx, [rbp - 0x38]
+mov rdx, r15
```
(ещё 99 строк диффа: so-query.py fdiff libclient.so 0x4ed5ad0)

### изменена: 0x4ed5e80 (963 байт) CDOTA_Modifier_Orb_Of_Frost_Debuff::vfunc#79 | строки: "slow_melee"; "slow_ranged"; "heal_reduction"; "AbilityManaCost"; "AbilityHealthCost"
было: 0x4edcf90 (1677 байт)
- строки: −"AbilityManaCost" −"AbilityHealthCost"
- константы из данных (числа логики): −0.5 −100
- числа в инструкциях: −0xffffffff −-1 −1 −1 −2 −2 −0x3f800000
- виртуальные вызовы: −0x10c8 (слот 537)
- поля объектов: −0x18 −0x18 −0x814 −0xa60 −0xe74 −0xe74 −0x770 −0x770 −0x116
- прямых вызовов: 43 → 25
- инструкций: 403 → 236
```diff
@@ -14,15 +14,36 @@
 call qword ptr [rax + 0x1a8]
 test r12, r12
-pxor xmm1, xmm1
-je L
-xor r9d, r9d
-xor r8d, r8d
-xor ecx, ecx
-lea rsi, [S:"slow_melee"]
-mov edx, 0xffffffff
-mov rdi, r12
-call F
-movaps xmm1, xmm0
-movss dword ptr [rbx + 0x1af8], xmm1
+movss dword ptr [rbp - 0x44], xmm0
+pxor xmm0, xmm0
+je L
+mov rdi, r12
+call F
+cmp eax, -1
+mov r13d, eax
+je L
+lea r15, [S:"slow_melee"]
+mov rdi, r12
+mov rsi, r15
+call F
+test rax, rax
+mov r14, rax
+je L
+mov rdi, r12
+call F
+test rax, rax
+je L
+mov rdi, r12
+call F
+lea r8, [rbp - 0x34]
+mov ecx, r13d
+mov rdx, r15
+mov rdi, rax
+mov rsi, r12
+call F
+test al, al
+je L
+movss xmm0, dword ptr [rbp - 0x34]
+nop dword ptr [rax + rax]
+movss dword ptr [rbx + 0x1af8], xmm0
 mov rdi, rbx
 call F
@@ -32,36 +53,9 @@
 call qword ptr [rax + 0x1a8]
 test r12, r12
-movss dword ptr [rbp - 0x44], xmm0
-pxor xmm0, xmm0
-je L
-mov rdi, r12
-call F
-cmp eax, -1
-mov r13d, eax
-je L
-lea r15, [S:"slow_ranged"]
-mov rdi, r12
-mov rsi, r15
-call F
-test rax, rax
-mov r14, rax
-je L
-mov rdi, r12
-call F
-test rax, rax
-je L
-mov rdi, r12
-call F
-lea r8, [rbp - 0x34]
-mov ecx, r13d
-mov rdx, r15
-mov rdi, rax
-mov rsi, r12
-call F
-test al, al
-je L
-movss xmm0, dword ptr [rbp - 0x34]
-nop word ptr [rax + rax]
-movss dword ptr [rbx + 0x1afc], xmm0
+je L
+lea rsi, [rbx + 0x1afc]
+mov rdi, r12
+lea rdx, [S:"slow_ranged"]
+call F
 mov rdi, rbx
 call F
@@ -71,35 +65,21 @@
 call qword ptr [rax + 0x1a8]
 test r12, r12
-movss dword ptr [rbp - 0x44], xmm0
-pxor xmm0, xmm0
-je L
-mov rdi, r12
-call F
-cmp eax, -1
-mov r13d, eax
-je L
-lea r15, [S:"heal_reduction"]
-mov rdi, r12
-mov rsi, r15
-call F
-test rax, rax
-mov r14, rax
-je L
-mov rdi, r12
-call F
-test rax, rax
-je L
-mov rdi, r12
-call F
-lea r8, [rbp - 0x34]
-mov ecx, r13d
-mov rdx, r15
-mov rdi, rax
-mov rsi, r12
-call F
```
(ещё 212 строк диффа: so-query.py fdiff libclient.so 0x4ed5e80)

### изменена: 0x4f0ebe0 (225 байт) CDOTA_Modifier_Item_SerratedShiv::OnCreated | строки: "proc_chance"; "hp_dmg"; "hp_dmg_rosh"
было: 0x4f0f2b0 (218 байт)
- инструкций: 61 → 62
```diff
@@ -9,6 +9,6 @@
 mov rax, qword ptr [rbx]
 call qword ptr [rax + 0x1a8]
-xor eax, eax
 test r12, r12
+pxor xmm1, xmm1
 je L
 xor r9d, r9d
@@ -19,6 +19,7 @@
 mov rdi, r12
 call F
+movaps xmm1, xmm0
+movss dword ptr [rbx + 0x1af8], xmm1
 mov rdi, rbx
-mov dword ptr [rbx + 0x1af8], eax
 call F
 mov rdi, rbx
```

### изменена: 0x4f0f190 (233 байт) CDOTA_Modifier_Safety_Bubble::OnCreated, CDOTA_Modifier_Safety_Bubble::OnRefresh | строки: "bonus_hp_regen"; "shield"; "restore_time"
было: 0x4f0f390 (226 байт)
- инструкций: 62 → 63
```diff
@@ -26,6 +26,6 @@
 mov rax, qword ptr [rbx]
 call qword ptr [rax + 0x1a8]
-xor eax, eax
 test r12, r12
+pxor xmm1, xmm1
 je L
 xor r9d, r9d
@@ -36,6 +36,7 @@
 mov rdi, r12
 call F
+movaps xmm1, xmm0
+movss dword ptr [rbx + 0x1b04], xmm1
 mov rdi, rbx
-mov dword ptr [rbx + 0x1b04], eax
 call F
 mov rdi, rbx
```

### изменена: 0x4f26d50 (450 байт) CDOTA_Modifier_Item_Stormcrafter::OnCreated | строки: "range"; "damage"; "slow_duration"; "bonus_mana_regen"; "max_targets"; "passive_movement_bonus"
было: 0x4f26e90 (443 байт)
- инструкций: 117 → 118
```diff
@@ -31,6 +31,6 @@
 mov rax, qword ptr [rbx]
 call qword ptr [rax + 0x1a8]
-xor eax, eax
 test r12, r12
+pxor xmm1, xmm1
 je L
 xor r9d, r9d
@@ -41,6 +41,7 @@
 mov rdi, r12
 call F
+movaps xmm1, xmm0
+movss dword ptr [rbx + 0x1b04], xmm1
 mov rdi, rbx
-mov dword ptr [rbx + 0x1b04], eax
 call F
 mov rdi, rbx
```

### изменена: 0x4f2e340 (38 байт) вызывается из: CDOTA_Modifier_Item_Witch_Blade_Slow::vfunc#88
было: 0x4f2e480 (39 байт)
- константы из данных (числа логики): +-0,0,0,0
- числа в инструкциях: +0 +0
- инструкций: 10 → 8
```diff
@@ -1,8 +1,6 @@
-mov edx, dword ptr [rsi + 0x1af8]
-pxor xmm0, xmm0
+movss xmm0, dword ptr [rsi + 0x1af8]
 mov rax, rdi
+xorps xmm0, xmmword ptr [K:-0,0,0,0]
 mov dword ptr [rdi], 1
-neg edx
-cvtsi2ss xmm0, edx
 movss dword ptr [rdi + 4], xmm0
 pxor xmm0, xmm0
```

### изменена: 0x4f3ef40 (240 байт) CDOTA_Modifier_Item_Witch_Blade_Slow::OnCreated | строки: "slow"; "int_damage_multiplier"; "building_effectiveness_pct"
было: 0x4f3f080 (239 байт)
- числа в инструкциях: +0xffffffff −0
- инструкций: 61 → 64
```diff
@@ -10,9 +10,15 @@
 call qword ptr [rax + 0x1a8]
 test r12, r12
+pxor xmm1, xmm1
 je L
-lea rsi, [rbx + 0x1af8]
+xor r9d, r9d
+xor r8d, r8d
+xor ecx, ecx
+lea rsi, [S:"slow"]
+mov edx, 0xffffffff
 mov rdi, r12
-lea rdx, [S:"slow"]
 call F
+movaps xmm1, xmm0
+movss dword ptr [rbx + 0x1af8], xmm1
 mov rdi, rbx
 call F
@@ -57,5 +63,2 @@
 movss xmm0, dword ptr [K:1]
 jmp F
-nop
-mov dword ptr [rbx + 0x1af8], 0
-jmp L
```

### добавлена: 0x4f023a0 (136 байт) вызывается из: CDOTA_Modifier_Safety_Bubble::vfunc#88

### добавлена: 0x4f02430 (107 байт) вызывается из: CDOTA_Modifier_Item_SerratedShiv::vfunc#88

### удалена: 0x4f024e0 (251 байт) вызывается из: CDOTA_Modifier_Safety_Bubble::vfunc#88

### копии существующего кода (12): шаблонные / склеенные компоновщиком функции, такой же код есть и в другой сборке — не новый код
- ещё одна копия существующего кода: 0x4de9c50 (92 байт) C_DOTA_Item_Skypiercer::vfunc#50
- ещё одна копия существующего кода: 0x4de9cb0 (92 байт) C_DOTA_Item_Slippers::vfunc#50
- ещё одна копия существующего кода: 0x4ed4a70 (92 байт) C_DOTA_Item_Orb_Of_Corrosion::vfunc#50
- ещё одна копия существующего кода: 0x4ed4ad0 (92 байт) C_DOTA_Item_Orb_Of_Frost::vfunc#50
- ещё одна копия существующего кода: 0x4ed4b30 (92 байт) CDOTA_Item_Recipe_Orb_Of_Destruction::vfunc#50
- ещё одна копия существующего кода: 0x4ed4b90 (92 байт) CDOTA_Item_Orb_Of_Destruction::vfunc#50
- одной копией существующего кода меньше: 0x4dea7d0 (117 байт) C_DOTA_Item_RingOfTarrasque::vfunc#50
- одной копией существующего кода меньше: 0x4dea850 (117 байт) C_DOTA_Item_RiverPainter::vfunc#50, C_DOTA_Item_RiverPainter2::vfunc#50, CDOTA_Item_RiverPainter3::vfunc#50
- одной копией существующего кода меньше: 0x4ed6f30 (117 байт) C_DOTA_Item_MartyrsPlate::vfunc#50
- одной копией существующего кода меньше: 0x4ed6fb0 (117 байт) C_DOTA_Item_Recipe_MaskOfDispair::vfunc#50
- одной копией существующего кода меньше: 0x4ed7030 (117 байт) C_DOTA_Item_MaskOfDispair::vfunc#50
- одной копией существующего кода меньше: 0x4ed70b0 (117 байт) C_DOTA_Item_Mechanical_Arm::vfunc#50

## libserver.so: функций 221832 → 221832; без изменений 221719, изменено 103, добавлено 2, удалено 4

### изменена: 0x3bf7540 (808 байт) вызывается из: CDOTA_NPCSpawnerGoodTop::vfunc#22, CDOTA_Ability_Lua::GetIntrinsicModifierName, CDOTA_Ability_Lua::GetAssociatedPrimaryAbilities | строки: "Y;R"; "%g %g %g"; "%g %g %g %g"; "(null)"; "false"; "true"; "%llu"; "%lld"
было: 0x3bf7500 (808 байт)
- строки: +"Y;R"
- инструкций: 203 → 203
```diff
@@ -36,5 +36,5 @@
 cmp al, 0x4f
 ja L
-lea rcx, [D]
+lea rcx, [S:"Y;R"]
 movzx edx, al
 movsxd rdx, dword ptr [rcx + rdx*4]
```

### изменена: 0x3bf8fa0 (238 байт)
было: 0x3bf8f60 (238 байт)
- строки: −"_TR"
- инструкций: 65 → 65
```diff
@@ -2,5 +2,5 @@
 ja L
 push rbp
-lea rdx, [S:"_TR"]
+lea rdx, [D]
 mov edi, edi
 mov rbp, rsp
```

### изменена: 0x3bfac40 (323 байт) | строки: "CUtlSymbolLarge"; "CNetworkUtlVectorBase"
было: 0x3bfac00 (323 байт)
- строки: −"LpR"
- инструкций: 99 → 99
```diff
@@ -2,5 +2,5 @@
 ja L
 push rbp
-lea rdx, [S:"LpR"]
+lea rdx, [D]
 mov edi, edi
 mov rbp, rsp
```

### изменена: 0x3bfadf0 (317 байт)
было: 0x3bfadb0 (317 байт)
- строки: −"hrR"
- инструкций: 98 → 98
```diff
@@ -7,5 +7,5 @@
 push rbx
 ja L
-lea rdx, [S:"hrR"]
+lea rdx, [D]
 mov edi, edi
 mov rbx, rsi
```

### изменена: 0x3c27620 (1047 байт) | строки: "7#U"; "Unsupported KV3 basic type '%s' (%d)!"; "Pointers cannot be used as numeric values"
было: 0x3c275e0 (1047 байт)
- строки: +"7#U"
- инструкций: 245 → 245
```diff
@@ -47,5 +47,5 @@
 cmp r8b, 6
 ja L
-lea rcx, [D]
+lea rcx, [S:"7#U"]
 movzx edx, r8b
 movsxd rdx, dword ptr [rcx + rdx*4]
```

### изменена: 0x3c27a40 (1047 байт) | строки: ";'U"; "Unsupported KV3 basic type '%s' (%d)!"; "Pointers cannot be used as numeric values"
было: 0x3c27a00 (1047 байт)
- строки: +";'U"
- инструкций: 245 → 245
```diff
@@ -47,5 +47,5 @@
 cmp r8b, 6
 ja L
-lea rcx, [D]
+lea rcx, [S:";'U"]
 movzx edx, r8b
 movsxd rdx, dword ptr [rcx + rdx*4]
```

### изменена: 0x3c27e60 (1047 байт) | строки: "?+U"; "Unsupported KV3 basic type '%s' (%d)!"; "Pointers cannot be used as numeric values"
было: 0x3c27e20 (1047 байт)
- строки: +"?+U"
- инструкций: 245 → 245
```diff
@@ -47,5 +47,5 @@
 cmp r8b, 6
 ja L
-lea rcx, [D]
+lea rcx, [S:"?+U"]
 movzx edx, r8b
 movsxd rdx, dword ptr [rcx + rdx*4]
```

### изменена: 0x3c28280 (1047 байт) | строки: "C/U"; "Unsupported KV3 basic type '%s' (%d)!"; "Pointers cannot be used as numeric values"
было: 0x3c28240 (1047 байт)
- строки: +"C/U"
- инструкций: 245 → 245
```diff
@@ -47,5 +47,5 @@
 cmp r8b, 6
 ja L
-lea rcx, [D]
+lea rcx, [S:"C/U"]
 movzx edx, r8b
 movsxd rdx, dword ptr [rcx + rdx*4]
```

### изменена: 0x3c286a0 (1047 байт) | строки: "G3U"; "Unsupported KV3 basic type '%s' (%d)!"; "Pointers cannot be used as numeric values"
было: 0x3c28660 (1047 байт)
- строки: +"G3U"
- инструкций: 245 → 245
```diff
@@ -47,5 +47,5 @@
 cmp r8b, 6
 ja L
-lea rcx, [D]
+lea rcx, [S:"G3U"]
 movzx edx, r8b
 movsxd rdx, dword ptr [rcx + rdx*4]
```

### изменена: 0x3c28ac0 (1047 байт) | строки: "K7U"; "Unsupported KV3 basic type '%s' (%d)!"; "Pointers cannot be used as numeric values"
было: 0x3c28a80 (1047 байт)
- строки: +"K7U"
- инструкций: 245 → 245
```diff
@@ -47,5 +47,5 @@
 cmp r8b, 6
 ja L
-lea rcx, [D]
+lea rcx, [S:"K7U"]
 movzx edx, r8b
 movsxd rdx, dword ptr [rcx + rdx*4]
```

### изменена: 0x3c29840 (1047 байт) | строки: "Unsupported KV3 basic type '%s' (%d)!"; "Pointers cannot be used as numeric values"
было: 0x3c29800 (1047 байт)
- строки: −"oDU"
- инструкций: 245 → 245
```diff
@@ -47,5 +47,5 @@
 cmp r8b, 6
 ja L
-lea rcx, [S:"oDU"]
+lea rcx, [D]
 movzx edx, r8b
 movsxd rdx, dword ptr [rcx + rdx*4]
```

### изменена: 0x3c29c60 (1047 байт) | строки: "Unsupported KV3 basic type '%s' (%d)!"; "Pointers cannot be used as numeric values"
было: 0x3c29c20 (1047 байт)
- строки: −"sHU"
- инструкций: 245 → 245
```diff
@@ -47,5 +47,5 @@
 cmp r8b, 6
 ja L
-lea rcx, [S:"sHU"]
+lea rcx, [D]
 movzx edx, r8b
 movsxd rdx, dword ptr [rcx + rdx*4]
```

### изменена: 0x3c2b570 (951 байт) | строки: "IKV3TransferInterface_GameTime_Load"
было: 0x3c2b530 (951 байт)
- строки: −"NdU"
- инструкций: 235 → 235
```diff
@@ -63,5 +63,5 @@
 cmp al, 6
 ja L
-lea rdx, [S:"NdU"]
+lea rdx, [D]
 movzx eax, al
 movsxd rax, dword ptr [rdx + rax*4]
```

### изменена: 0x3c6a420 (715 байт) CDOTA_NPCSpawnerGoodTop::vfunc#51, CDOTA_NPCSpawnerGoodMid::vfunc#51, CDOTA_NPCSpawnerGoodBot::vfunc#51 | строки: "disableshadows"; "7-Y"; "disablereceiveshadows"; "ownername"; "O-Y"
было: 0x3c6a3e0 (715 байт)
- строки: +"7-Y" +"O-Y"
- инструкций: 189 → 189
```diff
@@ -25,5 +25,5 @@
 cmp dl, 6
 ja L
-lea rcx, [D]
+lea rcx, [S:"7-Y"]
 movzx edx, dl
 movsxd rdx, dword ptr [rcx + rdx*4]
@@ -126,5 +126,5 @@
 cmp dl, 6
 ja L
-lea rcx, [D]
+lea rcx, [S:"O-Y"]
 movzx edx, dl
 movsxd rdx, dword ptr [rcx + rdx*4]
```

### изменена: 0x3c6d200 (1027 байт) | строки: "CEntityIOOutput"; "CBaseFilter"; "CHandle"
было: 0x3c6d1c0 (1027 байт)
- строки: −"lZY"
- инструкций: 172 → 172
```diff
@@ -2,5 +2,5 @@
 ja L
 push rbp
-lea rdx, [S:"lZY"]
+lea rdx, [D]
 mov edi, edi
 mov rbp, rsp
```

### изменена: 0x3c6e520 (653 байт) | строки: "%g %g %g"; "(null)"; "%g %g %g %g"; "%lld"; "%llu"; "%d %d %d %d"; "false"; "true"
было: 0x3c6e4e0 (653 байт)
- строки: −"AnY"
- инструкций: 159 → 159
```diff
@@ -7,5 +7,5 @@
 cmp al, 0x4f
 ja L
-lea rcx, [S:"AnY"]
+lea rcx, [D]
 movzx edx, al
 movsxd rdx, dword ptr [rcx + rdx*4]
```

### изменена: 0x3c8a750 (478 байт) | строки: ".-["
было: 0x3c8a710 (478 байт)
- строки: +".-["
- инструкций: 116 → 116
```diff
@@ -8,5 +8,5 @@
 cmp dil, 0x4f
 ja L
-lea rdx, [D]
+lea rdx, [S:".-["]
 movzx eax, dil
 movsxd rax, dword ptr [rdx + rax*4]
```

### изменена: 0x3cc00d0 (2479 байт) CBaseLightProbeVolume::vfunc#2 | строки: "box_mins"; "box_maxs"; "moveable"; "handshake"; "@n^"; "indoor_outdoor_level"; "StartDisabled"; "is_selected_in_hammer"
было: 0x3cc0090 (2479 байт)
- строки: +"@n^" +"nm^" −"rm^" −"{m^" −"mm^" −"Xm^" −".m^"
- инструкций: 618 → 618
```diff
@@ -71,5 +71,5 @@
 cmp dl, 6
 ja L
-lea rcx, [D]
+lea rcx, [S:"@n^"]
 movzx edx, dl
 movsxd rdx, dword ptr [rcx + rdx*4]
@@ -231,5 +231,5 @@
 cmp dl, 6
 ja L
-lea rcx, [S:"rm^"]
+lea rcx, [D]
 movzx edx, dl
 movsxd rdx, dword ptr [rcx + rdx*4]
@@ -259,5 +259,5 @@
 cmp dl, 6
 ja L
-lea rcx, [S:"{m^"]
+lea rcx, [D]
 movzx edx, dl
 movsxd rdx, dword ptr [rcx + rdx*4]
@@ -287,5 +287,5 @@
 cmp dl, 6
 ja L
-lea rcx, [S:"mm^"]
+lea rcx, [D]
 movzx edx, dl
 movsxd rdx, dword ptr [rcx + rdx*4]
@@ -315,5 +315,5 @@
 cmp dl, 6
 ja L
-lea rcx, [S:"Xm^"]
+lea rcx, [D]
 movzx edx, dl
 movsxd rdx, dword ptr [rcx + rdx*4]
@@ -344,5 +344,5 @@
 cmp dl, 6
 ja L
-lea rcx, [S:".m^"]
+lea rcx, [S:"nm^"]
 movzx edx, dl
 movsxd rdx, dword ptr [rcx + rdx*4]
```

### изменена: 0x3d22ce0 (1712 байт) CEntityOutputTemplate<SndOpEventGuid_t>::vfunc#2 | строки: "m_Value"; "Stack depth limit hit (%d)"; "qPd"; "public.aabb_min"; "public.aabb_max"
было: 0x3d22ca0 (1712 байт)
- строки: +"qPd" −"pPd" −"1Pd"
- инструкций: 409 → 409
```diff
@@ -65,5 +65,5 @@
 cmp al, 6
 ja L
-lea rdx, [S:"pPd"]
+lea rdx, [D]
 movzx eax, al
 movsxd rax, dword ptr [rdx + rax*4]
@@ -90,5 +90,5 @@
 cmp al, 6
 ja L
-lea rdx, [S:"1Pd"]
+lea rdx, [S:"qPd"]
 movzx eax, al
 movsxd rax, dword ptr [rdx + rax*4]
```

### изменена: 0x3d30320 (637 байт) | строки: "CInfoFan"; "CHandle"; "VectorWS"
было: 0x3d302e0 (637 байт)
- строки: −"\\$e"
- инструкций: 147 → 147
```diff
@@ -7,5 +7,5 @@
 cmp edi, 6
 ja L
-lea rdx, [S:"\\$e"]
+lea rdx, [D]
 mov edi, edi
 mov rbx, rsi
```

### изменена: 0x3d307a0 (547 байт) | строки: "x'e"; "CHandle"; "CBasePlayerController"; "CNetworkUtlVectorBase"; "CBasePlayerPawn"
было: 0x3d30760 (547 байт)
- строки: +"x'e" −"8'e"
- инструкций: 158 → 158
```diff
@@ -2,5 +2,5 @@
 ja L
 push rbp
-lea rdx, [S:"8'e"]
+lea rdx, [S:"x'e"]
 mov edi, edi
 mov rbp, rsp
```

### изменена: 0x3d51a40 (117 байт) | строки: "y g"
было: 0x3d51a00 (117 байт)
- строки: +"y g" −"9 g"
- инструкций: 39 → 39
```diff
@@ -2,5 +2,5 @@
 cmp edx, 6
 ja L
-lea rcx, [S:"9 g"]
+lea rcx, [S:"y g"]
 push rbp
 mov rdi, rsi
```

### изменена: 0x3d51ac0 (561 байт) | строки: "Unsupported KV3 basic type '%s' (%d)!"; "Pointers cannot be used as numeric values"
было: 0x3d51a80 (561 байт)
- строки: −"c g"
- инструкций: 151 → 151
```diff
@@ -11,5 +11,5 @@
 cmp r8b, 6
 ja L
-lea rdx, [S:"c g"]
+lea rdx, [D]
 movzx eax, r8b
 movsxd rax, dword ptr [rdx + rax*4]
```

### изменена: 0x3d51dc0 (227 байт) | строки: "IPhysicsJoint"
было: 0x3d51d80 (227 байт)
- строки: −"X#g"
- инструкций: 73 → 73
```diff
@@ -1,5 +1,5 @@
 cmp edi, 6
 ja L
-lea rcx, [S:"X#g"]
+lea rcx, [D]
 mov edi, edi
 push rbp
```

### изменена: 0x3d528e0 (339 байт) | строки: "D.g"; "VPhysicsCollisionAttribute_t"; "SolidType_t"; "SurroundingBoundsType_t"
было: 0x3d528a0 (339 байт)
- строки: +"D.g"
- инструкций: 99 → 99
```diff
@@ -2,5 +2,5 @@
 ja L
 push rbp
-lea rdx, [D]
+lea rdx, [S:"D.g"]
 mov edi, edi
 mov rbp, rsp
```

### изменена: 0x3d52b00 (499 байт) | строки: "P0g"; "GameTime_t"; "BeamType_t"; "CBaseEntity"; "CHandle"; "AttachmentHandle_t"; "VectorWS"
было: 0x3d52ac0 (499 байт)
- строки: +"P0g"
- инструкций: 135 → 135
```diff
@@ -2,5 +2,5 @@
 ja L
 push rbp
-lea rdx, [D]
+lea rdx, [S:"P0g"]
 mov edi, edi
 mov rbp, rsp
```

### изменена: 0x3d52ef0 (285 байт) | строки: "VectorWS"
было: 0x3d52eb0 (285 байт)
- строки: −"L4g"
- инструкций: 81 → 81
```diff
@@ -5,5 +5,5 @@
 push rbx
 ja L
-lea rdx, [S:"L4g"]
+lea rdx, [D]
 mov edi, edi
 mov rbx, rsi
```

### изменена: 0x3d53150 (893 байт) | строки: "InfoForResourceTypeIParticleSystemDefinition"; "CWeakHandle"; "CResourceNameTyped"; "ParticleAttachment_t"; "PrecipitationFilter_t"
было: 0x3d53110 (893 байт)
- строки: −"@6g"
- инструкций: 188 → 188
```diff
@@ -9,5 +9,5 @@
 cmp edi, 6
 ja F
-lea rdx, [S:"@6g"]
+lea rdx, [D]
 mov edi, edi
 mov rbx, rsi
```

### изменена: 0x3d620c0 (785 байт) | строки: "Z%h"; "Unsupported KV3 basic type '%s' (%d)!"; "Pointers cannot be used as numeric values"
было: 0x3d62080 (785 байт)
- строки: +"Z%h"
- инструкций: 219 → 219
```diff
@@ -20,5 +20,5 @@
 cmp bl, 6
 ja L
-lea rdx, [D]
+lea rdx, [S:"Z%h"]
 movzx eax, bl
 movsxd rax, dword ptr [rdx + rax*4]
```

### изменена: 0x3d85150 (243 байт) | строки: "h1j"; "VectorWS"
было: 0x3d85110 (243 байт)
- строки: +"h1j" −"(1j"
- инструкций: 67 → 67
```diff
@@ -1,5 +1,5 @@
 cmp edi, 6
 ja L
-lea rdx, [S:"(1j"]
+lea rdx, [S:"h1j"]
 mov edi, edi
 push rbp
```

### изменена: 0x3d85250 (227 байт) | строки: "T2j"; "VectorWS"
было: 0x3d85210 (227 байт)
- строки: +"T2j"
- инструкций: 74 → 74
```diff
@@ -1,5 +1,5 @@
 cmp edi, 6
 ja L
-lea rcx, [D]
+lea rcx, [S:"T2j"]
 mov edi, edi
 push rbp
```

### изменена: 0x3d85340 (339 байт) | строки: "(3j"; "BASEPTR"; "GameTick_t"
было: 0x3d85300 (339 байт)
- строки: +"(3j"
- инструкций: 90 → 90
```diff
@@ -1,5 +1,5 @@
 cmp edi, 6
 ja L
-lea rdx, [D]
+lea rdx, [S:"(3j"]
 mov edi, edi
 push rbp
```

### изменена: 0x3d85cb0 (243 байт) | строки: "|<j"; "VectorWS"
было: 0x3d85c70 (243 байт)
- строки: +"|<j" −"<<j"
- инструкций: 76 → 76
```diff
@@ -2,5 +2,5 @@
 ja L
 push rbp
-lea rdx, [S:"<<j"]
+lea rdx, [S:"|<j"]
 mov edi, edi
 mov rbp, rsp
```

### изменена: 0x3d860c0 (371 байт) | строки: "\\@j"; "GameTime_t"; "CBaseEntity"; "CHandle"
было: 0x3d86080 (371 байт)
- строки: +"\\@j"
- инструкций: 112 → 112
```diff
@@ -2,5 +2,5 @@
 ja L
 push rbp
-lea rdx, [D]
+lea rdx, [S:"\\@j"]
 mov edi, edi
 mov rbp, rsp
```

### изменена: 0x3d866c0 (183 байт)
было: 0x3d86680 (183 байт)
- строки: −"cFj"
- инструкций: 55 → 55
```diff
@@ -2,5 +2,5 @@
 ja L
 push rbp
-lea rdx, [S:"cFj"]
+lea rdx, [D]
 mov edi, edi
 mov rbp, rsp
```

### изменена: 0x3d867f0 (98 байт) | строки: "bGj"
было: 0x3d867b0 (98 байт)
- строки: +"bGj" −"\"Gj"
- инструкций: 36 → 36
```diff
@@ -2,5 +2,5 @@
 cmp edx, 6
 ja L
-lea rcx, [S:"\"Gj"]
+lea rcx, [S:"bGj"]
 push rbp
 mov rdi, rsi
```

### изменена: 0x3d86860 (98 байт)
было: 0x3d86820 (98 байт)
- строки: −"vGj"
- инструкций: 36 → 36
```diff
@@ -2,5 +2,5 @@
 cmp edx, 6
 ja L
-lea rcx, [S:"vGj"]
+lea rcx, [D]
 push rbp
 mov rdi, rsi
```

### изменена: 0x3d86a40 (117 байт) | строки: "qIj"
было: 0x3d86a00 (117 байт)
- строки: +"qIj" −"1Ij"
- инструкций: 39 → 39
```diff
@@ -2,5 +2,5 @@
 cmp edx, 6
 ja L
-lea rcx, [S:"1Ij"]
+lea rcx, [S:"qIj"]
 push rbp
 mov rdi, rsi
```

### изменена: 0x3d86c90 (136 байт)
было: 0x3d86c50 (136 байт)
- строки: −"xKj"
- инструкций: 43 → 43
```diff
@@ -2,5 +2,5 @@
 cmp edx, 6
 ja L
-lea rcx, [S:"xKj"]
+lea rcx, [D]
 push rbp
 mov rax, rsi
```

### изменена: 0x3d87cf0 (206 байт) | строки: "?\\j"
было: 0x3d87cb0 (206 байт)
- строки: +"?\\j"
- инструкций: 62 → 62
```diff
@@ -2,5 +2,5 @@
 ja L
 push rbp
-lea rdx, [D]
+lea rdx, [S:"?\\j"]
 mov edi, edi
 mov rbp, rsp
```

### изменена: 0x3d88100 (222 байт) | строки: "'`j"
было: 0x3d880c0 (222 байт)
- строки: +"'`j"
- инструкций: 64 → 64
```diff
@@ -2,5 +2,5 @@
 ja L
 push rbp
-lea rdx, [D]
+lea rdx, [S:"'`j"]
 mov edi, edi
 mov rbp, rsp
```

### изменена: 0x3d882e0 (435 байт) | строки: "Xaj"; "CTransform"; "CNetworkUtlVectorBase"
было: 0x3d882a0 (435 байт)
- строки: +"Xaj"
- инструкций: 118 → 118
```diff
@@ -1,5 +1,5 @@
 cmp edi, 6
 ja L
-lea rdx, [D]
+lea rdx, [S:"Xaj"]
 mov edi, edi
 push rbp
```

### изменена: 0x3d88550 (302 байт) | строки: "sdj"
было: 0x3d88510 (302 байт)
- строки: +"sdj" −"3dj"
- инструкций: 71 → 71
```diff
@@ -2,5 +2,5 @@
 ja L
 push rbp
-lea rdx, [S:"3dj"]
+lea rdx, [S:"sdj"]
 mov edi, edi
 mov rbp, rsp
```

### изменена: 0x3d88a20 (811 байт) | строки: "Xhj"
было: 0x3d889e0 (811 байт)
- строки: +"Xhj"
- инструкций: 232 → 232
```diff
@@ -9,5 +9,5 @@
 movsxd r13, edx
 push r12
-lea rdx, [D]
+lea rdx, [S:"Xhj"]
 mov r12d, ecx
 push rbx
```

### изменена: 0x3d88d60 (907 байт)
было: 0x3d88d20 (907 байт)
- строки: −"Dkj"
- инструкций: 252 → 252
```diff
@@ -9,5 +9,5 @@
 movsxd r13, edx
 push r12
-lea rdx, [S:"Dkj"]
+lea rdx, [D]
 mov r12d, ecx
 push rbx
```

### изменена: 0x3d89bd0 (435 байт) | строки: "CPlayerSlot"; "CUtlVector"
было: 0x3d89b90 (435 байт)
- строки: −"`yj"
- инструкций: 115 → 115
```diff
@@ -1,5 +1,5 @@
 cmp edi, 6
 ja L
-lea rdx, [S:"`yj"]
+lea rdx, [D]
 mov edi, edi
 push rbp
```

### изменена: 0x3d95530 (659 байт) | строки: "CTakeDamageInfo"; "DestructiblePartDamageRequest_t"; "CUtlLeanVector"; "VectorWS"; "TakeDamageFlags_t"; "HitGroup_t"
было: 0x3d954f0 (659 байт)
- строки: −"t1k"
- инструкций: 151 → 151
```diff
@@ -1,5 +1,5 @@
 cmp edi, 6
 ja L
-lea rdx, [S:"t1k"]
+lea rdx, [D]
 mov edi, edi
 push rbp
```

### изменена: 0x3d957d0 (659 байт) | строки: "84k"; "CTakeDamageInfo"; "CTakeDamageResult"
было: 0x3d95790 (659 байт)
- строки: +"84k"
- инструкций: 126 → 126
```diff
@@ -2,5 +2,5 @@
 ja L
 push rbp
-lea rdx, [D]
+lea rdx, [S:"84k"]
 mov edi, edi
 mov rbp, rsp
```

### изменена: 0x3d95e00 (563 байт) | строки: "H:k"; "CUtlVector"; "VectorWS"; "GameTime_t"
было: 0x3d95dc0 (563 байт)
- строки: +"H:k"
- инструкций: 157 → 157
```diff
@@ -2,5 +2,5 @@
 ja L
 push rbp
-lea rdx, [D]
+lea rdx, [S:"H:k"]
 mov edi, edi
 mov rbp, rsp
```

### изменена: 0x3d98d50 (4083 байт) вызывается из: CTakeDamageInfo::vfunc#2 | строки: "m_vecDamageForce"; "m_bitsDamageType"; "+mk"; "m_vecDamagePosition"; "m_vecReportedPosition"; "m_vecDamageDirection"; "m_hInflictor"; "m_hAttacker"
было: 0x3d98d10 (4083 байт)
- строки: +"+mk" +"6wk"
- инструкций: 886 → 886
```diff
@@ -113,5 +113,5 @@
 cmp r8b, 6
 ja L
-lea rdx, [D]
+lea rdx, [S:"+mk"]
 movzx eax, r8b
 movsxd rax, dword ptr [rdx + rax*4]
@@ -362,5 +362,5 @@
 cmp r8b, 6
 ja L
-lea rdx, [D]
+lea rdx, [S:"6wk"]
 movzx eax, r8b
 movsxd rax, dword ptr [rdx + rax*4]
```

### изменена: 0x3da4a00 (414 байт) | строки: "P%l"
было: 0x3da49c0 (414 байт)
- строки: +"P%l"
- инструкций: 136 → 136
```diff
@@ -8,5 +8,5 @@
 movsxd r12, edx
 push rbx
-lea rdx, [D]
+lea rdx, [S:"P%l"]
 mov rbx, rsi
 sub rsp, 0x18
```

### изменена: 0x3da5620 (542 байт) | строки: "01l"
было: 0x3da55e0 (542 байт)
- строки: +"01l"
- инструкций: 159 → 159
```diff
@@ -9,5 +9,5 @@
 movsxd r12, edx
 push rbx
-lea rdx, [D]
+lea rdx, [S:"01l"]
 mov rbx, rsi
 sub rsp, 0x10
```

### изменена: 0x3daa870 (961 байт) | строки: "Byl"; "%g %g %g"; "(null)"; "%g %g %g %g"; "unknown_variant_type"; "qyl"; "%lld"; "%llu"
было: 0x3daa830 (961 байт)
- строки: +"Byl" +"qyl" −"1yl"
- инструкций: 213 → 213
```diff
@@ -7,5 +7,5 @@
 cmp al, 0x4f
 ja L
-lea rcx, [D]
+lea rcx, [S:"Byl"]
 movzx edx, al
 movsxd rdx, dword ptr [rcx + rdx*4]
@@ -91,5 +91,5 @@
 cmp al, 0x47
 ja L
-lea rdx, [S:"1yl"]
+lea rdx, [S:"qyl"]
 movzx eax, al
 movsxd rax, dword ptr [rdx + rax*4]
```

### изменена: 0x3db84b0 (851 байт) | строки: "|Tm"; "%llu"
было: 0x3db8470 (851 байт)
- строки: +"|Tm" −"<Tm"
- инструкций: 190 → 190
```diff
@@ -21,5 +21,5 @@
 mov rbx, rax
 je L
-lea r13, [S:"<Tm"]
+lea r13, [S:"|Tm"]
 nop dword ptr [rax + rax]
 mov qword ptr [rbp - 0xc0], 0
```

### изменена: 0x3db8cc0 (819 байт) | строки: "$Zm"; "DecalFlags_t"; "GameTime_t"
было: 0x3db8c80 (819 байт)
- строки: +"$Zm"
- инструкций: 143 → 143
```diff
@@ -2,5 +2,5 @@
 ja L
 push rbp
-lea rdx, [D]
+lea rdx, [S:"$Zm"]
 mov edi, edi
 mov rbp, rsp
```

### изменена: 0x3df78a0 (350 байт) | строки: "_-q"
было: 0x3df7860 (350 байт)
- строки: +"_-q"
- инструкций: 92 → 92
```diff
@@ -2,5 +2,5 @@
 ja L
 push rbp
-lea rdx, [D]
+lea rdx, [S:"_-q"]
 mov edi, edi
 mov rbp, rsp
```

### изменена: 0x3df7a80 (407 байт) вызывается из: CVScriptGameSystem::vfunc#85
было: 0x3df7a40 (407 байт)
- строки: −"D.q"
- инструкций: 104 → 104
```diff
@@ -31,5 +31,5 @@
 ja L
 movzx eax, word ptr [rax + 0x28]
-lea rdx, [S:"D.q"]
+lea rdx, [D]
 movsxd rax, dword ptr [rdx + rax*4]
 add rax, rdx
```

### изменена: 0x3df9720 (547 байт) | строки: "CHandle"; "CEnvSoundscapeTriggerable"; "CBasePlayerPawn"; "CUtlVector"
было: 0x3df96e0 (547 байт)
- строки: −"hJq"
- инструкций: 144 → 144
```diff
@@ -2,5 +2,5 @@
 ja L
 push rbp
-lea rdx, [S:"hJq"]
+lea rdx, [D]
 mov edi, edi
 mov rbp, rsp
```

### изменена: 0x3dfc1d0 (502 байт) | строки: "4uq"
было: 0x3dfc190 (502 байт)
- строки: +"4uq"
- инструкций: 139 → 139
```diff
@@ -21,5 +21,5 @@
 cmp al, 0x24
 ja L
-lea rcx, [D]
+lea rcx, [S:"4uq"]
 movzx eax, al
 movsxd rax, dword ptr [rcx + rax*4]
```

### изменена: 0x3e1aa00 (4702 байт) | строки: "classname"; "connections"; "attributes"; "X\\s"
было: 0x3e1a9c0 (4702 байт)
- строки: +"X\\s" −"PWs" −"X]s"
- инструкций: 1086 → 1086
```diff
@@ -208,5 +208,5 @@
 cmp r14b, 0x4f
 ja L
-lea rsi, [S:"PWs"]
+lea rsi, [D]
 movsxd rax, dword ptr [rsi + r14*4]
 add rax, rsi
@@ -617,5 +617,5 @@
 cmp al, 0x4f
 ja L
-lea rsi, [S:"X]s"]
+lea rsi, [D]
 movzx edx, al
 movsxd rdx, dword ptr [rsi + rdx*4]
@@ -747,5 +747,5 @@
 cmp al, 0x4f
 ja L
-lea rsi, [D]
+lea rsi, [S:"X\\s"]
 movzx edx, al
 movsxd rdx, dword ptr [rsi + rdx*4]
```

### изменена: 0x3e2b9e0 (542 байт) | строки: "D[t"
было: 0x3e2b9a0 (542 байт)
- строки: +"D[t"
- инструкций: 159 → 159
```diff
@@ -9,5 +9,5 @@
 movsxd r12, edx
 push rbx
-lea rdx, [D]
+lea rdx, [S:"D[t"]
 mov rbx, rsi
 sub rsp, 0x10
```

### изменена: 0x3e6cc40 (187 байт) | строки: "Disposition_t"
было: 0x3e6cc00 (187 байт)
- строки: −"hYx"
- инструкций: 59 → 59
```diff
@@ -1,5 +1,5 @@
 cmp edi, 6
 ja L
-lea rdx, [S:"hYx"]
+lea rdx, [D]
 mov edi, edi
 push rbp
```

### изменена: 0x3e6ce30 (275 байт) | строки: "VectorWS"
было: 0x3e6cdf0 (275 байт)
- строки: −"D[x"
- инструкций: 84 → 84
```diff
@@ -1,5 +1,5 @@
 cmp edi, 6
 ja L
-lea rcx, [S:"D[x"]
+lea rcx, [D]
 mov edi, edi
 push rbp
```

### изменена: 0x3e6cff0 (243 байт) | строки: " ]x"; "VectorWS"
было: 0x3e6cfb0 (243 байт)
- строки: +" ]x"
- инструкций: 70 → 70
```diff
@@ -1,5 +1,5 @@
 cmp edi, 6
 ja L
-lea rdx, [D]
+lea rdx, [S:" ]x"]
 mov edi, edi
 push rbp
```

### изменена: 0x3e6da40 (451 байт) | строки: "dgx"; "CEconWearable"; "CHandle"; "CNetworkUtlVectorBase"; "RelationshipOverride_t"; "CUtlVector"; "Hull_t"; "CMovementStatsProperty"
было: 0x3e6da00 (451 байт)
- строки: +"dgx" −"$gx"
- инструкций: 129 → 129
```diff
@@ -2,5 +2,5 @@
 ja L
 push rbp
-lea rdx, [S:"$gx"]
+lea rdx, [S:"dgx"]
 mov edi, edi
 mov rbp, rsp
```

### изменена: 0x3e6f070 (187 байт) | строки: "S}x"
было: 0x3e6f030 (187 байт)
- строки: +"S}x"
- инструкций: 52 → 52
```diff
@@ -3,5 +3,5 @@
 ja L
 push rbp
-lea rcx, [D]
+lea rcx, [S:"S}x"]
 mov rdi, rsi
 mov rbp, rsp
```

### изменена: 0x3e6f130 (171 байт) | строки: "HitGroup_t"
было: 0x3e6f0f0 (171 байт)
- строки: −"@}x"
- инструкций: 54 → 54
```diff
@@ -1,5 +1,5 @@
 cmp edi, 6
 ja L
-lea rdx, [S:"@}x"]
+lea rdx, [D]
 mov edi, edi
 push rbp
```

### изменена: 0x3e6f1e0 (133 байт) | строки: "U~x"
было: 0x3e6f1a0 (133 байт)
- строки: +"U~x"
- инструкций: 41 → 41
```diff
@@ -2,5 +2,5 @@
 cmp edx, 6
 ja L
-lea rcx, [D]
+lea rcx, [S:"U~x"]
 push rbp
 mov rdi, rsi
```

### изменена: 0x3eaa520 (769 байт) вызывается из: CAnimGraphControllerBase::vfunc#2, CEmptyGraphController::vfunc#2, EventGrantDefinition_Emoticon_t::vfunc#2 | строки: "b-|"; "Unsupported KV3 basic type '%s' (%d)!"; "Pointers cannot be used as numeric values"
было: 0x3eaa4e0 (769 байт)
- строки: +"b-|" −"\"-|"
- инструкций: 220 → 220
```diff
@@ -31,5 +31,5 @@
 cmp bl, 6
 ja L
-lea rdx, [S:"\"-|"]
+lea rdx, [S:"b-|"]
 movzx eax, bl
 movsxd rax, dword ptr [rdx + rax*4]
```

### изменена: 0x3eace90 (856 байт)
было: 0x3eacaf0 (856 байт)
- строки: −"|P|"
- инструкций: 221 → 221
```diff
@@ -10,5 +10,5 @@
 movsxd r12, edx
 push rbx
-lea rdx, [S:"|P|"]
+lea rdx, [D]
 mov rbx, rsi
 sub rsp, 0x58
```

### изменена: 0x3eaeb40 (904 байт) | строки: "xp|"
было: 0x3eaeb00 (904 байт)
- строки: +"xp|" −"8p|"
- инструкций: 237 → 237
```diff
@@ -7,5 +7,5 @@
 mov r15d, edx
 push r14
-lea rdx, [S:"8p|"]
+lea rdx, [S:"xp|"]
 push r13
 push r12
```

### изменена: 0x3eca460 (904 байт) | строки: "()~"
было: 0x3eca420 (904 байт)
- строки: +"()~"
- инструкций: 238 → 238
```diff
@@ -7,5 +7,5 @@
 mov r15d, edx
 push r14
-lea rdx, [D]
+lea rdx, [S:"()~"]
 push r13
 push r12
```

### изменена: 0x44b5fa0 (573 байт) вызывается из: CDOTA_Modifier_Morphling_Syntropy::vfunc#97 | строки: "modifier_morphling_syntropy_slow"
было: 0x44bbf80 (461 байт)
- числа в инструкциях: +-1 +-2 +9 +0x3f +0x1ff +0x70 +3
- поля объектов: +0xcc +0xcc +0x10 +0x5d1
- прямых вызовов: 7 → 6
- инструкций: 118 → 143
```diff
@@ -60,4 +60,30 @@
 cmp ecx, -1
 je L
+mov rsi, qword ptr [D]
+test rsi, rsi
+je L
+cmp ecx, -2
+je L
+movzx eax, word ptr [r13 + 0xd0]
+mov rdx, rax
+shr rdx, 9
+and edx, 0x3f
+mov rdx, qword ptr [rsi + rdx*8]
+test rdx, rdx
+je L
+and eax, 0x1ff
+xor r14d, r14d
+imul rax, rax, 0x70
+add rax, rdx
+cmp ecx, dword ptr [rax + 0x10]
+jne L
+mov r14, qword ptr [rax]
+test r14, r14
+je L
+cmp byte ptr [r14 + 0x5d1], 3
+jne L
+mov ecx, dword ptr [r13 + 0xcc]
+cmp ecx, -1
+je L
 cmp ecx, -2
 mov rsi, qword ptr [D]
@@ -65,5 +91,5 @@
 test rsi, rsi
 je L
-movzx eax, word ptr [r13 + 0xd0]
+movzx eax, word ptr [r13 + 0xcc]
 mov rdx, rax
 shr rdx, 9
@@ -77,15 +103,12 @@
 cmp ecx, dword ptr [rax + 0x10]
 jne L
-mov r14, qword ptr [rax]
+mov r13, qword ptr [rax]
+test r13, r13
+je L
+cmp byte ptr [r13 + 0x5d1], 3
+jne L
+mov rdi, rbx
+call F
```
(ещё 21 строк диффа: so-query.py fdiff libserver.so 0x44b5fa0)

### изменена: 0x44d4700 (385 байт) | строки: "AddActiveCannonball"; "false"
было: 0x44d4660 (385 байт)
- числа в инструкциях: +0x78b −0x786
- инструкций: 96 → 96
```diff
@@ -29,5 +29,5 @@
 mov rdi, rbx
 movq xmm0, qword ptr [D]
-mov dword ptr [rbp - 0x28], 0x786
+mov dword ptr [rbp - 0x28], 0x78b
 movq xmm1, rax
 lea rax, [S:"false"]
```

### изменена: 0x44e3f60 (2073 байт) вызывается из: CDOTA_Modifier_Kunkka_Tidebringer::vfunc#97 | строки: "cleave_starting_width"; "cleave_ending_width"; "cleave_distance"; "particles/units/heroes/hero_kunkka/kunkka_spell_tidebringer.vpcf"; "particles/units/heroes/hero_kunkka/kunkka_spell_tidebringer_aoe.vpcf"; "particles/units/heroes/hero_kunkka/kunkka_tidebringer_aoe.vpcf"; "movespeed_slow_duration"; "pierces_armor"
было: 0x44e3ec0 (1929 байт)
- строки: +"particles/units/heroes/hero_kunkka/kunkka_tidebringer_aoe.vpcf"
- числа в инструкциях: +1
- виртуальные вызовы: +0x18 (слот 3)
- поля объектов: +0x1b04 +0x1afc
- прямых вызовов: 64 → 73
- инструкций: 412 → 446
```diff
@@ -9,5 +9,5 @@
 push rbx
 mov rbx, rsi
-sub rsp, 0x2d8
+sub rsp, 0x2e8
 mov ecx, dword ptr [rdx + 0xcc]
 cmp ecx, -1
@@ -43,5 +43,5 @@
 mov qword ptr [r12], 1
 movups xmmword ptr [r12 + 8], xmm0
-add rsp, 0x2d8
+add rsp, 0x2e8
 mov rax, r12
 pop rbx
@@ -121,10 +121,10 @@
 mov qword ptr [rbp - 0x270], rax
 lea rax, [rbp - 0x280]
-mov qword ptr [rbp - 0x2e0], rax
+mov qword ptr [rbp - 0x2e8], rax
 lea rax, [rbp - 0x268]
 mulss xmm2, xmm3
 mov qword ptr [rbp - 0x278], rax
 divss xmm2, dword ptr [K:100]
-movss dword ptr [rbp - 0x2e8], xmm2
+movss dword ptr [rbp - 0x2e0], xmm2
 call F
 mov rdi, rbx
@@ -161,12 +161,12 @@
 movss xmm1, dword ptr [rbx + 0x1b00]
 mov word ptr [rbp - 0x284], dx
-movss xmm2, dword ptr [rbp - 0x2e8]
+movss xmm2, dword ptr [rbp - 0x2e0]
 mov qword ptr [rbp - 0x290], 0
 mov dword ptr [rbp - 0x288], 0
 unpcklps xmm1, xmm0
 movss xmm0, dword ptr [rbx + 0x1afc]
-movlps qword ptr [rbp - 0x300], xmm1
+movlps qword ptr [rbp - 0x2f0], xmm1
 unpcklps xmm2, xmm0
-movlps qword ptr [rbp - 0x2e8], xmm2
+movlps qword ptr [rbp - 0x2e0], xmm2
 call F
 mov rdi, rbx
@@ -175,6 +175,6 @@
 lea rcx, [S:"particles/units/heroes/hero_kunkka/kunkka_spell_tidebringer.vpcf"]
 mov rsi, r15
-movq xmm2, qword ptr [rbp - 0x2e8]
-movq xmm1, qword ptr [rbp - 0x300]
+movq xmm2, qword ptr [rbp - 0x2e0]
```
(ещё 147 строк диффа: so-query.py fdiff libserver.so 0x44e3f60)

### изменена: 0x45100e0 (1677 байт) вызывается из: CDOTA_Modifier_Morphling_Replicate_Echo_Source::vfunc#97 | строки: "replicate_echo"; "nodraw"; "no_effect_on_original"; "invulnerability_on_creation"; "duration"; "permit_illusion_recycling"; "illusion_"; "modifier_morphling_replicate_echo"
было: 0x450ffc0 (1661 байт)
- строки: +"permit_illusion_recycling"
- прямых вызовов: 37 → 38
- инструкций: 352 → 356
```diff
@@ -113,4 +113,8 @@
 lea rsi, [S:"duration"]
 mov rdi, r13
+call F
+xor edx, edx
+mov rdi, r13
+lea rsi, [S:"permit_illusion_recycling"]
 call F
 mov rax, qword ptr [rbp - 0xe0]
```

### изменена: 0x451b160 (2026 байт) CDOTA_Ability_AntiMage_Mana_Overload::OnSpellStart | строки: "duration"; "outgoing_damage"; "incoming_damage"; "modifier_illusion"; "illusion_"; "particles/units/heroes/hero_antimage/antimage_blink_start.vpcf"; "Hero_Antimage.Blink_out"; "modifier_antimage_blink_illusion"
было: 0x451b040 (2066 байт)
- числа в инструкциях: −9 −0x3f −0x1ff −0x70 −-3
- поля объектов: −0x10
- прямых вызовов: 59 → 60
- инструкций: 465 → 453
```diff
@@ -207,8 +207,8 @@
 cmp ecx, -1
 je L
+cmp ecx, -2
 mov rsi, qword ptr [D]
+je L
 test rsi, rsi
-je L
-cmp ecx, -2
 je L
 movzx eax, word ptr [rax]
@@ -421,24 +421,11 @@
 test eax, eax
 jle L
-mov rcx, qword ptr [rbp - 0x68]
-mov rsi, qword ptr [D]
-lea rdi, [rcx + rax*4]
-mov r8d, dword ptr [rcx]
-cmp r8d, -3
-ja L
-test rsi, rsi
-je L
-movzx eax, word ptr [rcx]
-mov rdx, rax
-shr rdx, 9
-and edx, 0x3f
-mov rdx, qword ptr [rsi + rdx*8]
-test rdx, rdx
-je L
-and eax, 0x1ff
-imul rax, rax, 0x70
-add rax, rdx
-cmp r8d, dword ptr [rax + 0x10]
-jne L
+mov rbx, qword ptr [rbp - 0x68]
+lea rax, [rbx + rax*4]
+mov qword ptr [rbp - 0x148], rax
+mov rdi, rbx
+call F
+test rax, rax
+je L
 mov r12, qword ptr [rax]
 test r12, r12
@@ -450,11 +437,12 @@
 jmp L
 nop dword ptr [rax]
-add rcx, 4
-cmp rcx, rdi
+mov rax, qword ptr [rbp - 0x148]
```
(ещё 10 строк диффа: so-query.py fdiff libserver.so 0x451b160)

### изменена: 0x451dec0 (498 байт) | строки: "CreateHitListForCannonballVolley"; "false"; "<NULL>"
было: 0x451dde0 (498 байт)
- числа в инструкциях: +0x775 −0x770
- инструкций: 113 → 113
```diff
@@ -75,5 +75,5 @@
 movq xmm0, qword ptr [D]
 movq xmm1, rax
-mov dword ptr [rbp - 0x28], 0x770
+mov dword ptr [rbp - 0x28], 0x775
 lea rax, [S:"false"]
 punpcklqdq xmm0, xmm1
```

### изменена: 0x451e0c0 (1282 байт) вызывается из: CDOTA_Modifier_Kunkka_Ghost_Ship_Fire_Cannons::OnIntervalThink | строки: "base_cannon_rotation"; "rotation_per_cannon"; "distance_between_cannons"; "initial_cannon_offset"; "forward_cannon_count"; "Ability.Ghostship.Cannon.Fire"; "FireCannonsFromLocation"; "false"
было: 0x451dfe0 (1282 байт)
- числа в инструкциях: +0x8ee −0x8e9
- инструкций: 279 → 279
```diff
@@ -245,5 +245,5 @@
 mov dword ptr [rbp - 0xb8], edx
 movq xmm5, rax
-mov dword ptr [rbp - 0x48], 0x8e9
+mov dword ptr [rbp - 0x48], 0x8ee
 lea rax, [S:"false"]
 punpcklqdq xmm0, xmm5
```

### изменена: 0x4525900 (568 байт) вызывается из: CDOTA_Ability_Kunkka_GhostShip::vfunc#371 | строки: "RemoveActiveCannonball"; "false"; "<NULL>"
было: 0x4525840 (568 байт)
- числа в инструкциях: +0x7a3 −0x79e
- инструкций: 146 → 146
```diff
@@ -29,5 +29,5 @@
 mov rdi, rbx
 movq xmm0, qword ptr [D]
-mov dword ptr [rbp - 0x28], 0x79e
+mov dword ptr [rbp - 0x28], 0x7a3
 movq xmm1, rax
 lea rax, [S:"false"]
```

### изменена: 0x4525b40 (3526 байт) CDOTA_Ability_Kunkka_GhostShip::vfunc#371 | строки: "ghostship"; "kunkka_admirals_rum"; "buff_duration"; "rum_factor"; "ghostship_projectile_id"; "cannonball_volley"; "dragenemies"; "modifier_kunkka_ghost_ship_damage_absorb"
было: 0x4525a80 (3526 байт)
- числа в инструкциях: +0x86b −0x866
- инструкций: 760 → 760
```diff
@@ -677,5 +677,5 @@
 mov rdi, r15
 movq xmm0, qword ptr [D]
-mov dword ptr [rbp - 0x58], 0x866
+mov dword ptr [rbp - 0x58], 0x86b
 movq xmm3, rax
 lea rax, [S:"false"]
```

### изменена: 0x4d28540 (2795 байт) | строки: "modifier_techies_stasis_trap_stunned"; "duration"; "particles/units/heroes/hero_techies/techies_stasis_trap_beams.vpcf"; "attach_fx"; "attach_hitloc"; "particles/units/heroes/hero_techies/techies_stasis_trap_explode.vpcf"; "Hero_Techies.StasisTrap.Stun"
было: 0x4d26590 (9275 байт)
- константы из данных (числа логики): −0x00000000000000090000000000000000 −0x00000000000000090000000000000000 −0x00000000000000090000000000000000 −0x00000000000000090000000000000000 −0x00000000000000090000000000000000 −0x00000000000000090000000000000000 −0x00000000000000090000000000000000 −0x00000000000000090000000000000000 −0x00000000000000090000000000000000
- числа в инструкциях: −0xffffffff −0xffffffff −0xffffffff −0xffffffff −0xffffffff −0xffffffff −0xffffffff −0xffffffff (и ещё 235)
- прямых вызовов: 131 → 68
- инструкций: 1559 → 551
```diff
@@ -1,1010 +1,2 @@
-push rbp
-mov rbp, rsp
-push rbx
-sub rsp, 8
-movzx eax, byte ptr [D]
-test al, al
-je L
-mov rax, qword ptr [D]
-test rax, rax
-je L
-mov rbx, qword ptr [rbp - 8]
-leave
-ret
-nop word ptr [rax + rax]
-lea rbx, [D]
-mov rdi, rbx
-call F
-test eax, eax
-je L
-pxor xmm0, xmm0
-mov eax, 0xffffffff
-movdqa xmm1, xmmword ptr [K:0x00000000000000090000000000000000]
-movups xmmword ptr [D], xmm0
-movups xmmword ptr [D], xmm0
-lea rsi, [D]
-movups xmmword ptr [D], xmm0
-movups xmmword ptr [D], xmm0
-movups xmmword ptr [D], xmm0
-movups xmmword ptr [D], xmm1
-movups xmmword ptr [D], xmm0
-mov qword ptr [D], rax
-mov qword ptr [D], 0
-mov qword ptr [D], 0
-mov qword ptr [D], 0
-mov qword ptr [D], 0
-mov qword ptr [D], 0
-mov qword ptr [D], 0
-mov qword ptr [D], 0
-mov qword ptr [D], 0
-mov qword ptr [D], 0
-mov qword ptr [D], 0
-mov qword ptr [D], 0
-mov qword ptr [D], 0
-mov qword ptr [D], 0
-mov qword ptr [D], 0
-mov qword ptr [D], 0
-mov qword ptr [D], 0
-mov qword ptr [D], 0x20
```
(ещё 962 строк диффа: so-query.py fdiff libserver.so 0x4d28540)

### изменена: 0x4ea5be0 (92 байт) вызывается из: CDOTA_Modifier_Item_Skadi_Slow::vfunc#97
было: 0x4ea5b60 (98 байт)
- инструкций: 27 → 25
```diff
@@ -11,11 +11,9 @@
 test byte ptr [rax + 0x1060], 2
 jne L
-mov eax, dword ptr [r12 + 0x1b00]
+movss xmm0, dword ptr [r12 + 0x1b00]
+movss dword ptr [rbx + 4], xmm0
+mov rax, rbx
 pxor xmm0, xmm0
-cvtsi2ss xmm0, eax
 mov dword ptr [rbx], 1
-mov rax, rbx
-movss dword ptr [rbx + 4], xmm0
-pxor xmm0, xmm0
 movups xmmword ptr [rbx + 8], xmm0
 pop rbx
@@ -23,5 +21,5 @@
 pop rbp
 ret
-nop word ptr [rax + rax]
-mov eax, dword ptr [r12 + 0x1b04]
+nop dword ptr [rax]
+movss xmm0, dword ptr [r12 + 0x1b04]
 jmp L
```

### изменена: 0x4ea5c40 (108 байт) вызывается из: CDOTA_Modifier_Item_Skadi_Slow::vfunc#97
было: 0x4ea5bd0 (106 байт)
- инструкций: 31 → 29
```diff
@@ -15,11 +15,9 @@
 test byte ptr [rax + 0x1060], 2
 jne L
-mov eax, dword ptr [r12 + 0x1af8]
+movss xmm0, dword ptr [r12 + 0x1af8]
+movss dword ptr [rbx + 4], xmm0
+mov rax, rbx
 pxor xmm0, xmm0
-cvtsi2ss xmm0, eax
 mov dword ptr [rbx], 1
-mov rax, rbx
-movss dword ptr [rbx + 4], xmm0
-pxor xmm0, xmm0
 movups xmmword ptr [rbx + 8], xmm0
 pop rbx
@@ -27,5 +25,5 @@
 pop rbp
 ret
-nop
-mov eax, dword ptr [r12 + 0x1afc]
+nop dword ptr [rax]
+movss xmm0, dword ptr [r12 + 0x1afc]
 jmp L
```

### изменена: 0x4eb1bc0 (340 байт) CDOTA_Modifier_Item_Skadi_Slow::vfunc#88 | строки: "cold_attack_slow_melee"; "cold_attack_slow_ranged"; "cold_slow_melee"; "cold_slow_ranged"; "restoration_reduction"
было: 0x4eb2070 (263 байт)
- числа в инструкциях: +0xffffffff +0xffffffff +0xffffffff
- поля объектов: +0x1b00 +0x1b04 +0x1af8 +0x1afc −0x1b08
- прямых вызовов: 15 → 14
- инструкций: 66 → 89
```diff
@@ -9,38 +9,16 @@
 mov rax, qword ptr [rbx]
 call qword ptr [rax + 0x1f0]
-lea rsi, [rbx + 0x1b00]
+test r12, r12
+pxor xmm1, xmm1
+je L
+xor r9d, r9d
+xor r8d, r8d
+xor ecx, ecx
+lea rsi, [S:"cold_attack_slow_melee"]
+mov edx, 0xffffffff
 mov rdi, r12
-lea rdx, [S:"cold_attack_slow_melee"]
 call F
-mov rdi, rbx
-call F
-mov rdi, rbx
-mov r12, rax
-mov rax, qword ptr [rbx]
-call qword ptr [rax + 0x1f0]
-lea rsi, [rbx + 0x1b04]
-mov rdi, r12
-lea rdx, [S:"cold_attack_slow_ranged"]
-call F
-mov rdi, rbx
-call F
-mov rdi, rbx
-mov r12, rax
-mov rax, qword ptr [rbx]
-call qword ptr [rax + 0x1f0]
-lea rsi, [rbx + 0x1af8]
-mov rdi, r12
-lea rdx, [S:"cold_slow_melee"]
-call F
-mov rdi, rbx
-call F
-mov rdi, rbx
-mov r12, rax
-mov rax, qword ptr [rbx]
-call qword ptr [rax + 0x1f0]
-lea rsi, [rbx + 0x1afc]
-mov rdi, r12
-lea rdx, [S:"cold_slow_ranged"]
-call F
+movaps xmm1, xmm0
+movss dword ptr [rbx + 0x1b00], xmm1
 mov rdi, rbx
 call F
```
(ещё 61 строк диффа: so-query.py fdiff libserver.so 0x4eb1bc0)

### изменена: 0x4eb2240 (485 байт) CDOTA_Modifier_Item_Skypiercer::OnCreated | строки: "bonus_strength"; "bonus_armor"; "bonus_health_regen"; "hp_regen_amp"; "slow_resistance"; "bonus_evasion"; "buff_cooldown_acceleration_pct"; "close_radius"
было: 0x4eb2180 (565 байт)
- числа в инструкциях: −0xffffffff −0xffffffff −0xffffffff
- поля объектов: −0x1b0c −0x1b10 −0x1b14
- инструкций: 145 → 121
```diff
@@ -75,16 +75,8 @@
 mov rax, qword ptr [rbx]
 call qword ptr [rax + 0x1f0]
-test r12, r12
-pxor xmm1, xmm1
-je L
-xor r9d, r9d
-xor r8d, r8d
-xor ecx, ecx
-lea rsi, [S:"bonus_evasion"]
-mov edx, 0xffffffff
+lea rsi, [rbx + 0x1b0c]
 mov rdi, r12
+lea rdx, [S:"bonus_evasion"]
 call F
-movaps xmm1, xmm0
-movss dword ptr [rbx + 0x1b0c], xmm1
 mov rdi, rbx
 call F
@@ -93,16 +85,8 @@
 mov rax, qword ptr [rbx]
 call qword ptr [rax + 0x1f0]
-test r12, r12
-pxor xmm1, xmm1
-je L
-xor r9d, r9d
-xor r8d, r8d
-xor ecx, ecx
-lea rsi, [S:"buff_cooldown_acceleration_pct"]
-mov edx, 0xffffffff
+lea rsi, [rbx + 0x1b10]
 mov rdi, r12
+lea rdx, [S:"buff_cooldown_acceleration_pct"]
 call F
-movaps xmm1, xmm0
-movss dword ptr [rbx + 0x1b10], xmm1
 mov rdi, rbx
 call F
@@ -111,16 +95,8 @@
 mov rax, qword ptr [rbx]
 call qword ptr [rax + 0x1f0]
-test r12, r12
-pxor xmm1, xmm1
-je L
-xor r9d, r9d
-xor r8d, r8d
-xor ecx, ecx
-lea rsi, [S:"close_radius"]
-mov edx, 0xffffffff
```
(ещё 15 строк диффа: so-query.py fdiff libserver.so 0x4eb2240)

### изменена: 0x4eb30e0 (1082 байт) CDOTA_Modifier_Item_Shivas_Guard_Thinker::OnCreated | строки: "blast_speed"; "blast_radius"; "blast_damage"; "blast_debuff_duration"; "particles/items2_fx/shivas_guard_active.vpcf"
было: 0x4eb2f60 (1211 байт)
- строки: +"blast_speed" +"blast_radius" +"blast_damage" +"blast_debuff_duration" +"particles/items2_fx/shivas_guard_active.vpcf" −"paint_duration" −"RiverPaint.Cast"
- константы из данных (числа логики): +0.2 +-1,-1,3.402823e+38,3.402823e+38 +0x00000000ffffffff −-1
- числа в инструкциях: +0 +0 +0 +0 +0 +-1 +0x7f7fffff +0x7f7fffff −0xffffffff −0xffffffff −0x427e −0x427e −0xffffffffffffffff −0x3fffffff −8 −0xc78 (и ещё 8)
- виртуальные вызовы: +0x1f0 (слот 62) +0x1f0 (слот 62) +0x1f0 (слот 62) +0x1f0 (слот 62) −0x20 (слот 4) −0xc70 (слот 398)
- поля объектов: +0x1af8 +0x1b20 +0x1b20 +0x1b28 +0x1afc +0x1b24 +0x1b24 +0x1b30 +0x1b3c +0x1b34 +0x18 −0x1efc −0x1efc −0x1efc −0x1ef8 −0x1ef8 −0x1f00 −0x840 −0x840 −0x840 −0x80 −0x80 −0x1ef0 (и ещё 5)
- прямых вызовов: 17 → 27
- инструкций: 256 → 194
```diff
@@ -1,256 +1,194 @@
 push rbp
-xor r9d, r9d
-xor r8d, r8d
-xor ecx, ecx
-lea rsi, [S:"paint_duration"]
 mov rbp, rsp
-push r15
-mov edx, 0xffffffff
-push r14
 push r13
 push r12
 push rbx
 mov rbx, rdi
-sub rsp, 0x68
-movss xmm0, dword ptr [K:-1]
+sub rsp, 0xc8
 call F
-lea r13, [D]
-movss dword ptr [rbp - 0x84], xmm0
-mov r12, qword ptr [r13]
-test r12, r12
-je L
-lea r14, [r12 + 0x1ef0]
-mov rdi, r14
+mov rdi, rbx
+mov r12, rax
+mov rax, qword ptr [rbx]
+call qword ptr [rax + 0x1f0]
+lea rsi, [rbx + 0x1b30]
+mov rdi, r12
+lea rdx, [S:"blast_speed"]
 call F
-movss xmm1, dword ptr [rbp - 0x84]
-movss xmm2, dword ptr [r12 + 0x1efc]
-subss xmm2, xmm0
-maxss xmm2, xmm1
-movss xmm1, dword ptr [r12 + 0x1ef8]
-movaps xmm0, xmm2
-divss xmm0, dword ptr [r12 + 0x1f00]
-ucomiss xmm0, xmm1
+mov rdi, rbx
+call F
+mov rdi, rbx
+mov r12, rax
+mov rax, qword ptr [rbx]
+call qword ptr [rax + 0x1f0]
+lea rsi, [rbx + 0x1b34]
+mov rdi, r12
```
(ещё 372 строк диффа: so-query.py fdiff libserver.so 0x4eb30e0)

### изменена: 0x4eb3520 (1227 байт) CDOTA_Item_RiverPainter::OnSpellStart, CDOTA_Item_RiverPainter2::OnSpellStart, CDOTA_Item_RiverPainter3::OnSpellStart | строки: "paint_duration"; "RiverPaint.Cast"
было: 0x4eb3420 (1146 байт)
- строки: +"paint_duration" +"RiverPaint.Cast" −"blast_speed" −"blast_radius" −"blast_damage" −"blast_debuff_duration" −"particles/items2_fx/shivas_guard_active.vpcf"
- константы из данных (числа логики): +-1 −0.2 −-1,-1,3.402823e+38,3.402823e+38 −0x00000000ffffffff
- числа в инструкциях: +0x427e +0x427e +1 +1 +1 +0xffffffffffffffff +0x3fffffff +8 −0 −0 −0 −0 −0 −-1 −0x7f7fffff −0x7f7fffff (и ещё 9)
- виртуальные вызовы: +0x20 (слот 4) +0xc70 (слот 398) −0x1f0 (слот 62) −0x1f0 (слот 62) −0x1f0 (слот 62) −0x1f0 (слот 62)
- поля объектов: +0x1efc +0x1efc +0x1efc +0x1ef8 +0x1ef8 +0x1f00 +0x840 +0x840 +0x840 +0x80 +0x80 +0x1ef0 −0x1b34 −0x1b34 −0x1b3c −0x1b3c −0x1af8 −0x1b20 −0x1b20 −0x1b28 −0x1afc −0x1b24 −0x1b24 −0x1b30 (и ещё 6)
- прямых вызовов: 27 → 17
- инструкций: 212 → 259
```diff
@@ -1,212 +1,259 @@
 push rbp
+xor r9d, r9d
+xor r8d, r8d
+xor ecx, ecx
+lea rsi, [S:"paint_duration"]
 mov rbp, rsp
+push r15
+mov edx, 0xffffffff
+push r14
 push r13
 push r12
 push rbx
 mov rbx, rdi
-sub rsp, 0xc8
-call F
-mov rdi, rbx
-mov r12, rax
-mov rax, qword ptr [rbx]
-call qword ptr [rax + 0x1f0]
-lea rsi, [rbx + 0x1b30]
-mov rdi, r12
-lea rdx, [S:"blast_speed"]
-call F
-mov rdi, rbx
-call F
-mov rdi, rbx
-mov r12, rax
-mov rax, qword ptr [rbx]
-call qword ptr [rax + 0x1f0]
+sub rsp, 0x68
+movss xmm0, dword ptr [K:-1]
+call F
+lea r13, [D]
+movss dword ptr [rbp - 0x84], xmm0
+mov r12, qword ptr [r13]
 test r12, r12
-pxor xmm1, xmm1
-je L
-xor r9d, r9d
-xor r8d, r8d
-xor ecx, ecx
-lea rsi, [S:"blast_radius"]
-mov edx, 0xffffffff
-mov rdi, r12
-call F
-movaps xmm1, xmm0
-movss dword ptr [rbx + 0x1b34], xmm1
-mov rdi, rbx
```
(ещё 389 строк диффа: so-query.py fdiff libserver.so 0x4eb3520)

### изменена: 0x4fa54c0 (164 байт) вызывается из: CDOTA_Modifier_Orb_Of_Corrosion_Debuff::vfunc#97 | строки: "modifier_item_skadi_slow"
было: 0x4fa5480 (170 байт)
- инструкций: 48 → 46
```diff
@@ -32,11 +32,9 @@
 test byte ptr [rax + 0x1060], 2
 jne L
-mov eax, dword ptr [r12 + 0x1b00]
+movss xmm0, dword ptr [r12 + 0x1b00]
+movss dword ptr [rbx + 4], xmm0
+mov rax, rbx
 pxor xmm0, xmm0
-cvtsi2ss xmm0, eax
 mov dword ptr [rbx], 1
-mov rax, rbx
-movss dword ptr [rbx + 4], xmm0
-pxor xmm0, xmm0
 movups xmmword ptr [rbx + 8], xmm0
 pop rbx
@@ -44,5 +42,5 @@
 pop rbp
 ret
-nop word ptr [rax + rax]
-mov eax, dword ptr [r12 + 0x1b04]
+nop dword ptr [rax]
+movss xmm0, dword ptr [r12 + 0x1b04]
 jmp L
```

### изменена: 0x4fa7cf0 (116 байт) вызывается из: CDOTA_Modifier_Orb_Of_Corrosion_Debuff::vfunc#97 | строки: "modifier_item_skadi_slow"
было: 0x4fa7c10 (117 байт)
- константы из данных (числа логики): +-0,0,0,0
- числа в инструкциях: +0 +0
- инструкций: 36 → 34
```diff
@@ -22,10 +22,8 @@
 ret
 nop word ptr [rax + rax]
-mov eax, dword ptr [r12 + 0x1afc]
-pxor xmm0, xmm0
+movss xmm0, dword ptr [r12 + 0x1afc]
 mov dword ptr [rbx], 1
-neg eax
-cvtsi2ss xmm0, eax
 mov rax, rbx
+xorps xmm0, xmmword ptr [K:-0,0,0,0]
 movss dword ptr [rbx + 4], xmm0
 pxor xmm0, xmm0
```

### изменена: 0x4fa6270 (151 байт) вызывается из: CDOTA_Modifier_Orb_Of_Corrosion_Debuff::vfunc#97 | строки: "modifier_desolator_buff"; "modifier_stygian_desolator_buff"
было: 0x4fa7c90 (155 байт)
- инструкций: 42 → 41
```diff
@@ -34,7 +34,6 @@
 test rax, rax
 jne L
-pxor xmm0, xmm0
+movss xmm0, dword ptr [r12 + 0x1af8]
 mov dword ptr [rbx], 1
-cvtsi2ss xmm0, dword ptr [r12 + 0x1af8]
 movss dword ptr [rbx + 4], xmm0
 pxor xmm0, xmm0
```

### изменена: 0x4fb28e0 (243 байт) CDOTA_Modifier_Orb_Of_Corrosion_Debuff::vfunc#88 | строки: "corruption_armor"; "heal_reduction"; "slow_melee"; "slow_ranged"
было: 0x4fb3d40 (229 байт)
- инструкций: 61 → 63
```diff
@@ -9,6 +9,6 @@
 mov rax, qword ptr [rbx]
 call qword ptr [rax + 0x1f0]
-xor eax, eax
 test r12, r12
+pxor xmm1, xmm1
 je L
 xor r9d, r9d
@@ -19,6 +19,7 @@
 mov rdi, r12
 call F
+movaps xmm1, xmm0
+movss dword ptr [rbx + 0x1af8], xmm1
 mov rdi, rbx
-mov dword ptr [rbx + 0x1af8], eax
 call F
 mov rdi, rbx
@@ -26,6 +27,6 @@
 mov rax, qword ptr [rbx]
 call qword ptr [rax + 0x1f0]
-xor eax, eax
 test r12, r12
+pxor xmm1, xmm1
 je L
 xor r9d, r9d
@@ -36,6 +37,7 @@
 mov rdi, r12
 call F
+movaps xmm1, xmm0
+movss dword ptr [rbx + 0x1afc], xmm1
 mov rdi, rbx
-mov dword ptr [rbx + 0x1afc], eax
 call F
 mov rdi, rbx
```

### изменена: 0x4fe0240 (504 байт) вызывается из: CDOTA_Modifier_Safety_Bubble::vfunc#97
было: 0x4fe0340 (496 байт)
- инструкций: 131 → 130
```diff
@@ -10,6 +10,5 @@
 cmp byte ptr [rdx + 0x1e], 0
 je L
-pxor xmm0, xmm0
-cvtsi2ss xmm0, dword ptr [rsi + 0x1b04]
+movss xmm0, dword ptr [rsi + 0x1b04]
 mov dword ptr [rdi], 1
 movss dword ptr [rdi + 4], xmm0
@@ -24,15 +23,14 @@
 pop rbp
 ret
-nop word ptr [rax + rax]
+nop word ptr cs:[rax + rax]
 cmp byte ptr [rdx + 0x1d], 0
 mov r12, rdx
 je L
-pxor xmm1, xmm1
 pxor xmm0, xmm0
 pxor xmm2, xmm2
+mov rax, rbx
 cvtsi2ss xmm0, dword ptr [rsi + 0x1af8]
-cvtsi2ss xmm1, dword ptr [rsi + 0x1b04]
+movss xmm1, dword ptr [rsi + 0x1b04]
 mov dword ptr [rdi], 1
-mov rax, rbx
 subss xmm1, xmm0
 movaps xmm0, xmm1
@@ -99,13 +97,13 @@
 je L
 movss xmm0, dword ptr [r12 + 4]
-mov ecx, dword ptr [r13 + 0x1af8]
+pxor xmm1, xmm1
+mov edx, dword ptr [r13 + 0x1af8]
+movss xmm2, dword ptr [r13 + 0x1b04]
 cvttss2si eax, xmm0
-mov edx, dword ptr [r13 + 0x1b04]
-add eax, ecx
-cmp eax, edx
-jle L
-sub eax, edx
-pxor xmm1, xmm1
+add eax, edx
 cvtsi2ss xmm1, eax
+comiss xmm1, xmm2
+jbe L
+subss xmm1, xmm2
 subss xmm0, xmm1
 pxor xmm1, xmm1
@@ -115,5 +113,6 @@
```
(ещё 14 строк диффа: so-query.py fdiff libserver.so 0x4fe0240)

### изменена: 0x4fe5b60 (225 байт) CDOTA_Modifier_Item_SerratedShiv::OnCreated | строки: "proc_chance"; "hp_dmg"; "hp_dmg_rosh"
было: 0x4fe6b50 (218 байт)
- инструкций: 61 → 62
```diff
@@ -9,6 +9,6 @@
 mov rax, qword ptr [rbx]
 call qword ptr [rax + 0x1f0]
-xor eax, eax
 test r12, r12
+pxor xmm1, xmm1
 je L
 xor r9d, r9d
@@ -19,6 +19,7 @@
 mov rdi, r12
 call F
+movaps xmm1, xmm0
+movss dword ptr [rbx + 0x1af8], xmm1
 mov rdi, rbx
-mov dword ptr [rbx + 0x1af8], eax
 call F
 mov rdi, rbx
```

### изменена: 0x4fe6df0 (405 байт) CDOTA_Modifier_Safety_Bubble::OnCreated, CDOTA_Modifier_Safety_Bubble::OnRefresh | строки: "bonus_hp_regen"; "shield"; "restore_time"
было: 0x4fe6f60 (311 байт)
- константы из данных (числа логики): +nan +8388608 +1
- инструкций: 81 → 102
```diff
@@ -26,6 +26,6 @@
 mov rax, qword ptr [rbx]
 call qword ptr [rax + 0x1f0]
-xor eax, eax
 test r12, r12
+pxor xmm1, xmm1
 je L
 xor r9d, r9d
@@ -36,6 +36,7 @@
 mov rdi, r12
 call F
+movaps xmm1, xmm0
+movss dword ptr [rbx + 0x1b04], xmm1
 mov rdi, rbx
-mov dword ptr [rbx + 0x1b04], eax
 call F
 mov rdi, rbx
@@ -72,10 +73,30 @@
 pop rbp
 jmp F
-nop word ptr [rax + rax]
+nop dword ptr [rax]
 mov rdi, rbx
 call F
 mov edi, eax
 call F
-mov eax, dword ptr [rbx + 0x1b04]
+movss xmm2, dword ptr [K:nan]
 movss dword ptr [rbx + 0x1afc], xmm0
+movss xmm0, dword ptr [rbx + 0x1b04]
+movss xmm3, dword ptr [K:8388608]
+movaps xmm1, xmm0
+andps xmm1, xmm2
+ucomiss xmm3, xmm1
+ja L
+cvttss2si eax, xmm0
 jmp L
+cvttss2si eax, xmm0
+pxor xmm1, xmm1
+movss xmm4, dword ptr [K:1]
+andnps xmm2, xmm0
+cvtsi2ss xmm1, eax
+movaps xmm3, xmm1
+cmpnless xmm3, xmm0
+andps xmm3, xmm4
+subss xmm1, xmm3
+orps xmm1, xmm2
+movaps xmm0, xmm1
+cvttss2si eax, xmm0
```
(ещё 1 строк диффа: so-query.py fdiff libserver.so 0x4fe6df0)

### изменена: 0x4feb180 (486 байт) вызывается из: CDOTA_Modifier_Item_SerratedShiv::vfunc#97 | строки: "proc_chance"
было: 0x4feb080 (470 байт)
- прямых вызовов: 17 → 18
- инструкций: 115 → 118
```diff
@@ -72,8 +72,10 @@
 lea rdx, [S:"proc_chance"]
 call F
+movss xmm0, dword ptr [r12 + 0x1af8]
+call F
 mov rcx, r15
 mov rdx, r14
 mov esi, 0x47
-mov edi, dword ptr [r12 + 0x1af8]
+cvttss2si edi, xmm0
 call F
 test al, al
@@ -103,4 +105,5 @@
 or byte ptr [r13 + 0x50], 0x20
 jmp L
+nop dword ptr [rax + rax]
 xor r14d, r14d
 jmp L
```

### изменена: 0x4ffd5b0 (1110 байт) CDOTA_Modifier_Item_Stormcrafter::OnIntervalThink | строки: "particles/items_fx/chain_lightning.vpcf"; "attach_hitloc"; "modifier_item_stormcrafter_slow"; "duration"; "Item.Stormcrafter.Lightning"
было: 0x4ffd4b0 (1118 байт)
- инструкций: 260 → 259
```diff
@@ -217,7 +217,6 @@
 mov rcx, r10
 call F
-pxor xmm0, xmm0
-mov rdi, rbx
-cvtsi2ss xmm0, dword ptr [rbx + 0x1b04]
+movss xmm0, dword ptr [rbx + 0x1b04]
+mov rdi, rbx
 movss dword ptr [rbp - 0xa0], xmm0
 call F
```

### изменена: 0x5001210 (411 байт) CDOTA_Modifier_Item_Stormcrafter::OnCreated | строки: "range"; "damage"; "slow_duration"; "bonus_mana_regen"; "max_targets"; "passive_movement_bonus"
было: 0x5001110 (385 байт)
- числа в инструкциях: +0xffffffff
- поля объектов: +0x1b04
- инструкций: 95 → 103
```diff
@@ -31,8 +31,16 @@
 mov rax, qword ptr [rbx]
 call qword ptr [rax + 0x1f0]
-lea rsi, [rbx + 0x1b04]
+test r12, r12
+pxor xmm1, xmm1
+je L
+xor r9d, r9d
+xor r8d, r8d
+xor ecx, ecx
+lea rsi, [S:"damage"]
+mov edx, 0xffffffff
 mov rdi, r12
-lea rdx, [S:"damage"]
 call F
+movaps xmm1, xmm0
+movss dword ptr [rbx + 0x1b04], xmm1
 mov rdi, rbx
 call F
```

### изменена: 0x500b320 (38 байт) вызывается из: CDOTA_Modifier_Item_Witch_Blade_Slow::vfunc#97
было: 0x500b1e0 (39 байт)
- константы из данных (числа логики): +-0,0,0,0
- числа в инструкциях: +0 +0
- инструкций: 10 → 8
```diff
@@ -1,8 +1,6 @@
-mov edx, dword ptr [rsi + 0x1af8]
-pxor xmm0, xmm0
+movss xmm0, dword ptr [rsi + 0x1af8]
 mov rax, rdi
+xorps xmm0, xmmword ptr [K:-0,0,0,0]
 mov dword ptr [rdi], 1
-neg edx
-cvtsi2ss xmm0, edx
 movss dword ptr [rdi + 4], xmm0
 pxor xmm0, xmm0
```

### изменена: 0x5018920 (240 байт) CDOTA_Modifier_Item_Witch_Blade_Slow::OnCreated | строки: "slow"; "int_damage_multiplier"; "building_effectiveness_pct"
было: 0x5019940 (214 байт)
- числа в инструкциях: +0xffffffff
- поля объектов: +0x1af8
- инструкций: 56 → 64
```diff
@@ -9,8 +9,16 @@
 mov rax, qword ptr [rbx]
 call qword ptr [rax + 0x1f0]
-lea rsi, [rbx + 0x1af8]
+test r12, r12
+pxor xmm1, xmm1
+je L
+xor r9d, r9d
+xor r8d, r8d
+xor ecx, ecx
+lea rsi, [S:"slow"]
+mov edx, 0xffffffff
 mov rdi, r12
-lea rdx, [S:"slow"]
 call F
+movaps xmm1, xmm0
+movss dword ptr [rbx + 0x1af8], xmm1
 mov rdi, rbx
 call F
```

### изменена: 0x501a040 (236 байт) CDOTA_Modifier_Item_VindicatorsAxe::OnCreated | строки: "bonus_attack_speed"; "bonus_damage"; "bonus_armor"; "bonus_slow_resist"
было: 0x501a260 (255 байт)
- числа в инструкциях: −0xffffffff
- поля объектов: −0x1afc
- инструкций: 65 → 58
```diff
@@ -26,16 +26,9 @@
 mov rax, qword ptr [rbx]
 call qword ptr [rax + 0x1f0]
-xor eax, eax
-test r12, r12
-je L
-xor r9d, r9d
-xor r8d, r8d
-xor ecx, ecx
-lea rsi, [S:"bonus_damage"]
-mov edx, 0xffffffff
+lea rsi, [rbx + 0x1afc]
 mov rdi, r12
+lea rdx, [S:"bonus_damage"]
 call F
 mov rdi, rbx
-mov dword ptr [rbx + 0x1afc], eax
 call F
 mov rdi, rbx
```

### изменена: 0x5c15010 (2695 байт)
было: 0x5c14ed0 (2679 байт)
- инструкций: 570 → 575
```diff
@@ -63,7 +63,4 @@
 mov r15d, eax
 je L
-mov rax, qword ptr [rbx]
-mov rdi, qword ptr [rax + 0x10]
-call F
 cmp dword ptr [rbx + 0xc], 2
 jne L
@@ -113,4 +110,7 @@
 jne L
 mov rax, qword ptr [rbx]
+mov rdi, qword ptr [rax + 0x10]
+call F
+mov rax, qword ptr [rbx]
 mov rsi, qword ptr [rbp - 0x138]
 mov rdi, qword ptr [rax + 0x10]
@@ -123,10 +123,10 @@
 mov rdi, qword ptr [rbp - 0x148]
 mov rsi, r12
-mov byte ptr [rbp - 0x15a], al
+mov byte ptr [rbp - 0x152], al
 call F
 lea rsi, [T]
-mov byte ptr [rbp - 0x159], al
-mov rax, qword ptr [r13]
-mov qword ptr [rbp - 0x158], rsi
+mov byte ptr [rbp - 0x151], al
+mov rax, qword ptr [r13]
+mov qword ptr [rbp - 0x160], rsi
 mov rax, qword ptr [rax + 0x820]
 cmp rax, rsi
@@ -135,5 +135,5 @@
 mov rsi, r12
 call F
-mov byte ptr [rbp - 0x15b], al
+mov byte ptr [rbp - 0x153], al
 mov rsi, qword ptr [rbp - 0x138]
 mov rdx, r13
@@ -142,10 +142,10 @@
 cmp al, 1
 jne L
-cmp byte ptr [rbp - 0x159], 0
-jne L
-cmp byte ptr [rbp - 0x15a], 0
-jne L
-mov rsi, qword ptr [rbp - 0x138]
-mov byte ptr [rbp - 0x159], 0
+cmp byte ptr [rbp - 0x151], 0
+jne L
```
(ещё 171 строк диффа: so-query.py fdiff libserver.so 0x5c15010)

### изменена: 0x3e72fc0 (1059 байт) | строки: "CNetworkUtlVectorBase"; "AnimationAlgorithm_t"; "ExternalAnimGraphHandle_t"; "CGlobalSymbol"; "CBaseAnimGraph"; "CHandle"; "GameTime_t"; "CUtlVectorEmbeddedNetworkVar"
- код тот же, но вызывает другую функцию: было 0x3eace50, стало 0x3eace90

### добавлена: 0x3e6ee90 (98 байт) | строки: "R{x"

### добавлена: 0x4d26650 (7338 байт) | строки: "modifier_techies_sticky_bomb_chase"; "max_chase_time"; "target"; "duration"; "Hero_Techies.StickyBomb.Priming"; "countdown"; "modifier_techies_sticky_bomb_countdown"

### удалена: 0x3e6ebf0 (183 байт) | строки: "?yx"

### удалена: 0x3e6ed20 (183 байт) | строки: "Szx"

### удалена: 0x3e6eec0 (98 байт) | строки: "f{x"

### удалена: 0x4d69620 (882 байт) вызывается из: CDOTA_Modifier_Techies_StickyBombThrow::vfunc#117 | строки: "modifier_techies_sticky_bomb_chase"; "max_chase_time"; "target"; "duration"; "Hero_Techies.StickyBomb.Priming"; "countdown"; "modifier_techies_sticky_bomb_countdown"

### копии существующего кода (12): шаблонные / склеенные компоновщиком функции, такой же код есть и в другой сборке — не новый код
- ещё одна копия существующего кода: 0x3e6ec30 (183 байт)
- ещё одна копия существующего кода: 0x3e6ed60 (183 байт)
- ещё одна копия существующего кода: 0x4d28530 (9 байт)
- ещё одна копия существующего кода: 0x4fe06d0 (92 байт)
- ещё одна копия существующего кода: 0x4fe0730 (92 байт) CDOTA_Item_Pupils_gift::vfunc#50
- ещё одна копия существующего кода: 0x4fe0790 (92 байт) CDOTA_Item_PyrrhicCloak::vfunc#50
- ещё одна копия существующего кода: 0x4fe07f0 (92 байт) CDOTA_Item_Recipe_Quickening_Charm::vfunc#50
- одной копией существующего кода меньше: 0x4d69bd0 (9 байт)
- одной копией существующего кода меньше: 0x4fdf7d0 (67 байт) CDOTA_Item_Seer_Stone::vfunc#50
- одной копией существующего кода меньше: 0x4fdf820 (67 байт) CDOTA_Item_SerratedShiv::vfunc#50
- одной копией существующего кода меньше: 0x4fdf870 (67 байт) CDOTA_Item_Recipe_Angels_Demise::vfunc#50
- одной копией существующего кода меньше: 0x4fdf8c0 (67 байт) CDOTA_Item_Angels_Demise::vfunc#50
