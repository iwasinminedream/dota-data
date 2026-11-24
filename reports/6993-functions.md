# Dota 6993: изменения кода по функциям и строки библиотек

Снимки `6992-11267656` → `6993-11269454`; funcdiff.py. В диффе: [S:…] — строка, [K:…] — константа из данных, F — вызов другой функции, L — переход внутри функции, [D]/[T] — прочие адреса. Регистры и смещения стека меняются и от перекомпиляции. Здесь всё, в том числе игровые функции и изменения от пересборки.

## libclient.so: функций 281876 → 281876; без изменений 281874, изменено 1, добавлено 0, удалено 0

### изменена: 0x4a1cee0 (1429 байт) C_DOTA_Ability_Furion_ForceOfNature::vfunc#306 | строки: "area_of_effect"; "particles/ui_mouseactions/range_finder_aoe.vpcf"
было: 0x4a1cee0 (1368 байт)
- константы из данных (числа логики): +3.402823e+38 +3.402823e+38 +3.402823e+38
- числа в инструкциях: +0
- поля объектов: +0x3c8 +0x3c4
- инструкций: 323 → 345
```diff
@@ -30,10 +30,26 @@
 movss dword ptr [rbp - 0x64], xmm0
 call F
-mov rdi, qword ptr [r12 + 0x10]
+mov ecx, 0
+movss xmm2, dword ptr [rax + 0x3c8]
+ucomiss xmm2, dword ptr [K:3.402823e+38]
+movss xmm1, dword ptr [rax + 0x3c4]
 movss xmm0, dword ptr [rax + 0x3cc]
+setnp dl
 mov rax, qword ptr [rax + 0x3c4]
+cmovne edx, ecx
+ucomiss xmm1, dword ptr [K:3.402823e+38]
 movss dword ptr [rbp - 0x58], xmm0
+mov qword ptr [rbp - 0x60], rax
+setnp al
+cmovne eax, ecx
+test dl, al
+je L
+ucomiss xmm0, dword ptr [K:3.402823e+38]
+setnp al
+cmovne eax, ecx
+test al, al
+jne L
+mov rdi, qword ptr [r12 + 0x10]
 test rdi, rdi
-mov qword ptr [rbp - 0x60], rax
 je L
 lea rdx, [r13 + 8]
@@ -121,11 +137,11 @@
 jge L
 call F
-pxor xmm3, xmm3
+pxor xmm4, xmm4
 pxor xmm1, xmm1
 xor ecx, ecx
-movd xmm2, eax
+movd xmm3, eax
 mov edi, 0x70
-pshufd xmm0, xmm2, 0
-punpcklbw xmm0, xmm3
+pshufd xmm0, xmm3, 0
+punpcklbw xmm0, xmm4
 punpcklwd xmm0, xmm1
 cvtdq2ps xmm0, xmm0
@@ -159,5 +175,5 @@
 cmovs edx, esi
 mov esi, 0xffff
-movd xmm4, ecx
+movd xmm5, ecx
 cmp edx, esi
 cmovg edx, esi
@@ -171,5 +187,5 @@
 or edx, eax
 movd xmm0, edx
-punpckldq xmm0, xmm4
+punpckldq xmm0, xmm5
 punpcklqdq xmm0, xmm0
 packuswb xmm0, xmm0
@@ -205,4 +221,13 @@
 mov r9d, eax
 cmp edx, eax
+jle L
+nop word ptr cs:[rax + rax]
+nop dword ptr [rax]
+lea eax, [r9 + rdx]
+mov r9d, eax
+shr r9d, 0x1f
+add r9d, eax
+sar r9d, 1
+cmp edx, r9d
 jg L
 movsxd rcx, dword ptr [rbx + 0x838]
@@ -226,15 +251,5 @@
 mov dword ptr [rbx + 0x838], r9d
 jmp L
-nop word ptr cs:[rax + rax]
-nop dword ptr [rax]
-lea eax, [rdx + r9]
-mov r9d, eax
-shr r9d, 0x1f
-add r9d, eax
-sar r9d, 1
-cmp edx, r9d
-jg L
-jmp L
-nop dword ptr [rax + rax]
+nop
 movsxd r15, r12d
 xor r14d, r14d
@@ -242,5 +257,5 @@
 test r12d, r12d
 jle L
-nop dword ptr [rax + rax]
+nop
 mov rdx, qword ptr [rbx + 0x830]
 mov rsi, qword ptr [r13 + r14]
@@ -251,5 +266,18 @@
 jne L
 cmp dword ptr [rbp - 0x70], 0x3fffffff
+jbe L
+add rsp, 0x48
+pop rbx
+pop r12
+pop r13
+pop r14
+pop r15
+pop rbp
+ret
+nop word ptr cs:[rax + rax]
+cmp dword ptr [rbp - 0x70], 0x3fffffff
 ja L
+test r13, r13
+je L
 mov rax, qword ptr [D]
 mov rsi, r13
@@ -265,5 +293,4 @@
 pop rbp
 ret
-nop dword ptr [rax]
```
(ещё 12 строк диффа: so-query.py fdiff libclient.so 0x4a1cee0)

### копии существующего кода (2): шаблонные / склеенные компоновщиком функции, такой же код есть и в другой сборке — не новый код
- ещё одна копия существующего кода: 0x49f2970 (117 байт) C_DOTA_Ability_Alchemist_Corrosive_Weaponry::vfunc#50
- одной копией существующего кода меньше: 0x49f1eb0 (92 байт) C_DOTA_Ability_Invoker_Innate_Mastermind::vfunc#50

## libserver.so: функций 221932 → 221931; без изменений 221924, изменено 7, добавлено 0, удалено 1

### изменена: 0x5aedfa0 (1339 байт) CDOTA_Creature_BehaviorController::vfunc#3
было: 0x5aedfa0 (1330 байт)
- числа в инструкциях: +0 +0 +0
- поля объектов: +0x1952
- инструкций: 301 → 299
```diff
@@ -85,7 +85,5 @@
 call F
 jmp L
-mov rdi, qword ptr [rbx + 0x10]
-call F
-test al, al
+cmp byte ptr [r15 + 0x1952], 0
 jne L
 mov rax, qword ptr [r15]
@@ -113,12 +111,19 @@
 mov qword ptr [rbp - 0xb0], rax
 call F
-mov rsi, qword ptr [rbp - 0xb0]
+mov rcx, qword ptr [rbp - 0xb0]
 lea rdi, [rbp - 0x90]
-movq xmm1, qword ptr [rax]
-movq xmm0, qword ptr [rsi]
+movq xmm0, qword ptr [rax]
+movq xmm1, qword ptr [rcx]
 mov dword ptr [rbp - 0x88], 0
-subps xmm1, xmm0
-movaps xmmword ptr [rbp - 0xc0], xmm1
-movlps qword ptr [rbp - 0x90], xmm1
+subps xmm0, xmm1
+movshdup xmm1, xmm0
+movlps qword ptr [rbp - 0x90], xmm0
+mulss xmm0, xmm0
+mulss xmm1, xmm1
+addss xmm0, xmm1
+movd ecx, xmm0
+movd xmm0, ecx
+sqrtss xmm0, xmm0
+movss dword ptr [rbp - 0xb4], xmm0
 call F
 mov rdi, r12
@@ -127,29 +132,28 @@
 mov qword ptr [rbp - 0xb0], rax
 call F
-mov rsi, qword ptr [rbp - 0xb0]
+mov rcx, qword ptr [rbp - 0xb0]
 lea rdi, [rbp - 0x80]
 movq xmm0, qword ptr [rax]
-movq xmm2, qword ptr [rsi]
+movq xmm1, qword ptr [rcx]
 mov dword ptr [rbp - 0x78], 0
-subps xmm0, xmm2
+subps xmm0, xmm1
 movlps qword ptr [rbp - 0x80], xmm0
 call F
 cmp byte ptr [r15 + 0x17a0], 0
-mov rcx, qword ptr [rbp - 0xa8]
-movaps xmm1, xmmword ptr [rbp - 0xc0]
 jne L
 movss xmm0, dword ptr [rbp - 0x78]
-movss xmm2, dword ptr [rbp - 0x7c]
+movss xmm1, dword ptr [rbp - 0x7c]
 mulss xmm0, dword ptr [rbp - 0x88]
-mulss xmm2, dword ptr [rbp - 0x8c]
-addss xmm0, xmm2
-movss xmm2, dword ptr [rbp - 0x80]
-mulss xmm2, dword ptr [rbp - 0x90]
-addss xmm0, xmm2
-movss xmm2, dword ptr [K:-0.7071]
-comiss xmm2, xmm0
+mulss xmm1, dword ptr [rbp - 0x8c]
+addss xmm0, xmm1
+movss xmm1, dword ptr [rbp - 0x80]
+mulss xmm1, dword ptr [rbp - 0x90]
+addss xmm0, xmm1
+movss xmm1, dword ptr [K:-0.7071]
+comiss xmm1, xmm0
 jb L
-mov rax, qword ptr [rcx + 0x10]
+mov rax, qword ptr [rbp - 0xa8]
 mov edx, 0xffffffff
+mov rax, qword ptr [rax + 0x10]
 test rax, rax
 je L
@@ -161,13 +165,11 @@
 mov esi, dword ptr [rax + 0x10]
 mov rdi, r15
-mov qword ptr [rbp - 0xa8], rcx
-call F
-mov rdi, r13
-call F
-mov rcx, qword ptr [rbp - 0xa8]
+call F
+mov rdi, r13
+call F
 test rax, rax
 je L
 mov r12, qword ptr [rax]
-cmp rcx, r12
+cmp qword ptr [rbp - 0xa8], r12
 jne L
 cmp byte ptr [rbx + 0x20], 0
@@ -207,13 +209,17 @@
 call F
 jmp L
+mov rdi, qword ptr [rbx + 0x10]
+call F
+test al, al
+je L
+xor esi, esi
 xor edx, edx
-xor esi, esi
-mov rdi, r15
-call F
-test rax, rax
+mov rdi, r15
+call F
+test rax, rax
+mov rsi, rax
 je L
 mov rdi, qword ptr [rbx + 0x10]
 xor edx, edx
-mov rsi, rax
 call F
 jmp L
@@ -237,13 +243,6 @@
```
(ещё 54 строк диффа: so-query.py fdiff libserver.so 0x5aedfa0)

### изменена: 0x5b634e0 (19300 байт)
было: 0x5b634e0 (19260 байт)
- числа в инструкциях: +0
- поля объектов: +0x2c
- прямых вызовов: 331 → 332
- инструкций: 3739 → 3750
```diff
@@ -2761,18 +2761,21 @@
 lea rsi, [rbp - 0x74]
 mov rdi, r12
-movaps xmmword ptr [rbp - 0x50], xmm0
 mov word ptr [rbp - 0x34], ax
-lea r14, [rbp - 0x70]
-mov qword ptr [rbp - 0x70], 1
-mov qword ptr [rbp - 0x68], 0
-mov qword ptr [rbp - 0x60], 0
-mov qword ptr [rbp - 0x58], 0
-mov qword ptr [rbp - 0x40], 0xffffffffffffffff
-mov dword ptr [rbp - 0x38], 0xffffffff
-call F
-mov rax, qword ptr [rbx]
-mov rsi, r14
-mov rdi, rbx
-call qword ptr [rax + 8]
+mov qword ptr [rbp - 0x70], 1
+lea r14, [rbp - 0x70]
+mov qword ptr [rbp - 0x68], 0
+mov qword ptr [rbp - 0x60], 0
+mov qword ptr [rbp - 0x58], 0
+movaps xmmword ptr [rbp - 0x50], xmm0
+mov qword ptr [rbp - 0x40], 0xffffffffffffffff
+mov dword ptr [rbp - 0x38], 0xffffffff
+call F
+mov rax, qword ptr [rbx]
+lea rdx, [T]
+mov rax, qword ptr [rax + 8]
+cmp rax, rdx
+jne L
+cmp byte ptr [rbx + 0x2c], 0
+jne L
 mov rdi, r12
 call F
@@ -3016,7 +3019,5 @@
 nop word ptr [rax + rax]
 mov eax, 0x1a8
-nop word ptr cs:[rax + rax]
-nop word ptr cs:[rax + rax]
-nop dword ptr [rax + rax]
+nop dword ptr [rax]
 movzx edx, byte ptr [r13 + rax]
 mov byte ptr [rbx + rax], dl
@@ -3056,9 +3057,4 @@
 jmp L
 nop dword ptr [rax + rax]
-mov rsi, r14
-mov rdi, rbx
-call rax
-jmp L
-nop dword ptr [rax]
 mov rsi, r12
 mov rdi, rbx
@@ -3076,4 +3072,9 @@
 jmp L
 nop dword ptr [rax]
+mov rsi, r14
+mov rdi, rbx
+call rax
+jmp L
+nop dword ptr [rax]
 lea rdi, [rbx + 8]
 mov rsi, r14
@@ -3092,4 +3093,9 @@
 nop dword ptr [rax]
 lea rdi, [rbx + 8]
+mov rsi, r14
+call F
+jmp L
+nop dword ptr [rax]
+lea rdi, [rbx + 8]
 mov rsi, r12
 call F
@@ -3576,4 +3582,94 @@
 jmp L
 nop dword ptr [rax]
+mov rsi, r14
+mov rdi, rbx
+call rax
+jmp L
+nop dword ptr [rax]
+mov rsi, r14
+mov rdi, rbx
+call rax
+jmp L
+nop dword ptr [rax]
+mov rsi, r14
+mov rdi, rbx
+call rax
+jmp L
+nop dword ptr [rax]
+mov rsi, r14
+mov rdi, rbx
+call rax
+jmp L
+nop dword ptr [rax]
+mov rsi, r14
+mov rdi, rbx
+call rax
+jmp L
+nop dword ptr [rax]
+mov rsi, r14
+mov rdi, rbx
+call rax
+jmp L
+nop dword ptr [rax]
+mov rsi, r14
+mov rdi, rbx
+call rax
+jmp L
+nop dword ptr [rax]
+mov rsi, r14
+mov rdi, rbx
+call rax
+jmp L
+nop dword ptr [rax]
+mov rsi, r14
+mov rdi, rbx
+call rax
```
(ещё 160 строк диффа: so-query.py fdiff libserver.so 0x5b634e0)

### изменена: 0x5bf33e0 (628 байт) вызывается из: CDOTA_ItemSpawner::vfunc#237 | строки: "Spawn"; "../../game/shared/entityspawner.h"; "classname"; "CALLBACKS"
было: 0x5bf3420 (553 байт)
- числа в инструкциях: +0 +1
- поля объектов: +0x58 +0x50 +0x50 +0x38 +0x48
- инструкций: 136 → 157
```diff
@@ -10,17 +10,17 @@
 cmp qword ptr [rdi + 8], 0
 je L
-lea r12, [rbp - 0x50]
+lea r13, [rbp - 0x50]
 mov r15, rdi
 mov dword ptr [rbp - 0x48], 0x4bb
-lea r13, [S:"Spawn"]
-mov rdx, r12
+lea r14, [S:"Spawn"]
+mov rdx, r13
 lea rax, [S:"../../game/shared/entityspawner.h"]
-mov rdi, r13
-mov qword ptr [rbp - 0x40], r13
+mov rdi, r14
+mov qword ptr [rbp - 0x40], r14
 lea rsi, [D]
 mov qword ptr [rbp - 0x50], rax
 call F
 mov rdi, qword ptr [r15 + 8]
-mov rsi, r12
+mov rsi, r13
 mov qword ptr [rbp - 0x50], 0xffffffffc61b1c62
 mov qword ptr [rbp - 0x78], rax
@@ -49,14 +49,14 @@
 mov r8d, dword ptr [r15 + 0x28]
 call F
-mov r14, rax
+mov rbx, rax
 pop rax
-test r14, r14
+test rbx, rbx
 pop rdx
 je L
-mov rax, qword ptr [r14 + 0x10]
-mov ebx, 0xffffffff
+mov rax, qword ptr [rbx + 0x10]
+mov r12d, 0xffffffff
 test rax, rax
 je L
-mov ebx, dword ptr [rax + 0x10]
+mov r12d, dword ptr [rax + 0x10]
 mov esi, dword ptr [r15 + 0x2c]
 lea r8, [r15 + 0x30]
@@ -65,5 +65,5 @@
 mov qword ptr [rbp - 0x60], rax
 lea rax, [D]
-movq xmm0, qword ptr [r14 + 0x10]
+movq xmm0, qword ptr [rbx + 0x10]
 mov rcx, qword ptr [rbp - 0x80]
 movhps xmm0, qword ptr [r15 + 8]
@@ -72,10 +72,9 @@
 mov rax, qword ptr [rdi]
 call qword ptr [rax + 0x118]
-mov rax, qword ptr [r14 + 0x10]
+mov rax, qword ptr [rbx + 0x10]
 test byte ptr [rax + 0x31], 2
 je L
-mov ebx, 0xffffffff
+mov r12d, 0xffffffff
 mov rax, qword ptr [rbp - 0x78]
-mov r12d, ebx
 call rax
 lea rsp, [rbp - 0x28]
@@ -90,9 +89,9 @@
 nop dword ptr [rax]
 mov rax, qword ptr [rdx + 0x58]
-mov r14, qword ptr [rax]
-test r14, r14
+mov r12, qword ptr [rax]
+test r12, r12
 je L
 mov rdi, qword ptr [r15 + 8]
-mov rsi, r12
+mov rsi, r13
 mov qword ptr [rbp - 0x50], 0xffffffffc61b1c62
 mov qword ptr [rbp - 0x48], rbx
@@ -103,5 +102,5 @@
 je L
 mov rdi, qword ptr [rbp - 0x88]
-mov rdx, r14
+mov rdx, r12
 call F
 mov rdx, qword ptr [r15 + 0x18]
@@ -109,5 +108,5 @@
 nop
 lea rax, [D]
-mov rsi, r14
+mov rsi, rbx
 mov rdx, qword ptr [r15 + 8]
 mov rdi, qword ptr [rax]
@@ -116,6 +115,6 @@
 je L
 lea rax, [S:"../../game/shared/entityspawner.h"]
-mov rdx, r12
-mov qword ptr [rbp - 0x40], r13
+mov rdx, r13
+mov qword ptr [rbp - 0x40], r14
 lea rsi, [D]
 mov qword ptr [rbp - 0x50], rax
@@ -123,12 +122,34 @@
 mov dword ptr [rbp - 0x48], 0x4e2
 call F
-mov rdx, qword ptr [r15 + 8]
-mov rsi, r14
-mov rdi, qword ptr [r15 + 0x68]
-mov r12, rax
-call F
-call r12
+mov r13, qword ptr [r15 + 8]
+mov r15, qword ptr [r15 + 0x68]
+mov r14, rax
+test r15, r15
+jne L
 jmp L
-nop dword ptr [rax]
+nop
+mov rdx, qword ptr [r15 + 0x50]
+add rdi, qword ptr [r15 + 0x58]
+test dl, 1
```
(ещё 22 строк диффа: so-query.py fdiff libserver.so 0x5bf33e0)

### изменена: 0x5c002b0 (659 байт) | строки: "CVDataLocalizedToken"; "EMonsterHunterCodexAuthor"
было: 0x5bf5340 (723 байт)
- числа в инструкциях: −0 −0
- поля объектов: −0x48 −0x40
- прямых вызовов: 21 → 16
- инструкций: 183 → 164
```diff
@@ -103,29 +103,16 @@
 test rsi, rsi
 je L
-cmp qword ptr [rsi + 0x48], 0
-je L
-lea rdi, [rsi + 0x48]
-call F
-cmp qword ptr [rbx + 0x40], 0
-je L
-lea rdi, [rbx + 0x40]
-call F
-lea rdi, [rbx + 0x30]
-xor esi, esi
-call F
-lea rdi, [rbx + 0x20]
-xor esi, esi
-call F
-lea rdi, [rbx + 0x10]
-xor esi, esi
-call F
-xor esi, esi
-mov rdi, rbx
+mov rdi, rsi
 call F
 mov esi, 0x78
 mov rdi, rbx
 call F
-jmp L
-nop
+pop rbx
+mov eax, 1
+pop r12
+pop r13
+pop r14
+pop rbp
+ret
 movabs rax, 0xc000000800000000
 pxor xmm0, xmm0
@@ -169,15 +156,9 @@
 mov rdi, rbx
 call F
-pop rbx
-mov eax, 1
-pop r12
-pop r13
-pop r14
-pop rbp
-ret
-nop dword ptr [rax]
+jmp L
+nop dword ptr [rax + rax]
 xor eax, eax
 jmp L
-nop
+nop word ptr [rax + rax]
 xor eax, eax
 ret
```

### изменена: 0x5bfb4c0 (1872 байт) | строки: "classname"; "dota_item_drop"; "ContainedItem"; "origin"; "angles"; "Spawn"; "../../game/shared/entityspawner.h"; "CALLBACKS"
было: 0x5bfb780 (1792 байт)
- числа в инструкциях: +0 +1
- поля объектов: +0x38 +0x58 +0x50 +0x50 +0x48
- инструкций: 377 → 398
```diff
@@ -171,10 +171,10 @@
 test r12, r12
 je L
-lea r12, [S:"Spawn"]
+lea r15, [S:"Spawn"]
 mov rdx, rbx
 mov dword ptr [rbp - 0xd8], 0x4bb
 lea rax, [S:"../../game/shared/entityspawner.h"]
-mov rdi, r12
-mov qword ptr [rbp - 0xd0], r12
+mov rdi, r15
+mov qword ptr [rbp - 0xd0], r15
 lea rsi, [D]
 mov qword ptr [rbp - 0xe0], rax
@@ -206,10 +206,10 @@
 mov esi, dword ptr [rbp - 0x94]
 call F
-mov r15, rax
+mov r12, rax
 pop rax
-test r15, r15
+test r12, r12
 pop rdx
 je L
-mov rax, qword ptr [r15 + 0x10]
+mov rax, qword ptr [r12 + 0x10]
 mov r14d, 0xffffffff
 test rax, rax
@@ -222,5 +222,5 @@
 lea rax, [D]
 lea r8, [rbp - 0x90]
-movq xmm0, qword ptr [r15 + 0x10]
+movq xmm0, qword ptr [r12 + 0x10]
 mov esi, dword ptr [rbp - 0x94]
 movhps xmm0, qword ptr [rbp - 0xb8]
@@ -229,5 +229,5 @@
 mov rax, qword ptr [rdi]
 call qword ptr [rax + 0x118]
-mov rax, qword ptr [r15 + 0x10]
+mov rax, qword ptr [r12 + 0x10]
 test byte ptr [rax + 0x31], 2
 je L
@@ -260,8 +260,8 @@
 pop rbp
 ret
-nop
+nop word ptr [rax + rax]
 mov rax, qword ptr [rdx + 0x58]
-mov r15, qword ptr [rax]
-test r15, r15
+mov r12, qword ptr [rax]
+test r12, r12
 je L
 mov rdi, qword ptr [rbp - 0xb8]
@@ -275,5 +275,5 @@
 je L
 mov rdi, qword ptr [rbp - 0x130]
-mov rdx, r15
+mov rdx, r12
 call F
 mov rdx, qword ptr [rbp - 0xa8]
@@ -292,5 +292,5 @@
 mov r15, qword ptr [rbp - 0xb8]
 jmp L
-nop
+nop word ptr [rax + rax]
 mov r13, qword ptr [D]
 mov esi, 2
@@ -317,23 +317,44 @@
 nop word ptr [rax + rax]
 mov rdi, qword ptr [r13]
-mov rsi, r15
+mov rsi, r12
 mov rdx, qword ptr [rbp - 0xb8]
 call F
 cmp qword ptr [rbp - 0x48], 0
 je L
+lea rax, [S:"../../game/shared/entityspawner.h"]
 mov rdx, rbx
-mov qword ptr [rbp - 0xd0], r12
-lea rax, [S:"../../game/shared/entityspawner.h"]
-mov dword ptr [rbp - 0xd8], 0x4e2
+mov qword ptr [rbp - 0xd0], r15
 lea rsi, [D]
 mov qword ptr [rbp - 0xe0], rax
 lea rdi, [S:"CALLBACKS"]
-call F
-mov rdx, qword ptr [rbp - 0xb8]
-mov rsi, r15
-mov rdi, qword ptr [rbp - 0x58]
-mov rbx, rax
-call F
-call rbx
+mov dword ptr [rbp - 0xd8], 0x4e2
+call F
+mov r15, qword ptr [rbp - 0x58]
+mov rbx, qword ptr [rbp - 0xb8]
+mov r13, rax
+test r15, r15
+jne L
+jmp L
+mov rdx, qword ptr [r15 + 0x50]
+add rdi, qword ptr [r15 + 0x58]
+test dl, 1
+mov rax, rdx
+je L
+mov rax, qword ptr [rdi]
+mov rax, qword ptr [rax + rdx - 1]
+mov rdx, rbx
+mov rsi, r12
+call rax
+mov r15, qword ptr [r15 + 0x38]
+test r15, r15
+je L
+mov rdi, qword ptr [r15 + 0x48]
+test rdi, rdi
+jne L
+cmp qword ptr [r15 + 0x50], 0
+jne L
+jmp L
```
(ещё 4 строк диффа: so-query.py fdiff libserver.so 0x5bfb4c0)

### изменена: 0x5c1e0f0 (2132 байт) CDOTA_Lane_Creep_BehaviorController::vfunc#3
было: 0x5c1afb0 (2189 байт)
- числа в инструкциях: +1
- поля объектов: +0x8c
- прямых вызовов: 44 → 41
- цели вызовов: +0x5c1ddf0 −0x5c04750 −0x61b1d10 −0x62140f0 −0x5c1ae80
- инструкций: 488 → 478
```diff
@@ -3,42 +3,42 @@
 mov rbp, rsp
 push r15
-mov r15, rdi
 push r14
 push r13
 push r12
 push rbx
+mov rbx, rdi
 sub rsp, 0x78
-mov rbx, qword ptr [rdi + 8]
-mov rax, qword ptr [rbx]
+mov r15, qword ptr [rdi + 8]
+mov rax, qword ptr [r15]
 mov rax, qword ptr [rax + 0xa98]
 cmp rax, rdx
 jne L
-mov r12, qword ptr [rbx + 0x1788]
-cmp byte ptr [rbx + 0x174c], 0
-jne L
-mov rax, qword ptr [rbx + 0x1248]
+mov r12, qword ptr [r15 + 0x1788]
+cmp byte ptr [r15 + 0x174c], 0
+jne L
+mov rax, qword ptr [r15 + 0x1248]
 test eax, 0x80000000
 jne L
-cmp qword ptr [rbx + 0x1308], 0
+cmp qword ptr [r15 + 0x1308], 0
 jne L
 test al, 2
 jne L
-mov byte ptr [r15 + 0x18], 0
-test byte ptr [rbx + 0xd3d], 4
-je L
-cmp byte ptr [rbx + 0x1758], 0
-je L
-mov rdi, rbx
+mov byte ptr [rbx + 0x18], 0
+test byte ptr [r15 + 0xd3d], 4
+je L
+cmp byte ptr [r15 + 0x1758], 0
+je L
+mov rdi, r15
 mov qword ptr [rbp - 0x70], 0
 mov qword ptr [rbp - 0x68], 0
 mov qword ptr [rbp - 0x60], 0
 call F
-movzx r14d, byte ptr [rbx + 0x624]
-mov rdi, rbx
+movzx r14d, byte ptr [r15 + 0x624]
+mov rdi, r15
 mov r13, rax
 call F
 push 0
 mov r9d, 1
-mov rcx, rbx
+mov rcx, r15
 movss xmm0, dword ptr [K:1550]
 push 0
@@ -56,5 +56,5 @@
 mov r14, qword ptr [rbp - 0x68]
 lea r13, [r14 + rax*4]
-nop
+nop dword ptr [rax]
 mov rdi, r14
 call F
@@ -70,8 +70,7 @@
 cmp dword ptr [rax + 0xd64], 1
 jne L
-mov byte ptr [rbx + 0x1758], 0
-nop word ptr [rax + rax]
+mov byte ptr [r15 + 0x1758], 0
 add r14, 4
-cmp r13, r14
+cmp r14, r13
 jne L
 cmp dword ptr [rbp - 0x5c], 0x3fffffff
@@ -79,17 +78,17 @@
 jbe L
 nop dword ptr [rax]
-mov ecx, dword ptr [rbx + 0x12b8]
-cmp ecx, -1
-je L
-mov rsi, qword ptr [D]
-test rsi, rsi
-je L
-cmp ecx, -2
-je L
-movzx eax, word ptr [rbx + 0x12b8]
+mov esi, dword ptr [r15 + 0x12b8]
+cmp esi, -1
+je L
+mov rdi, qword ptr [D]
+test rdi, rdi
+je L
+cmp esi, -2
+je L
+movzx eax, word ptr [r15 + 0x12b8]
 mov rdx, rax
 shr rdx, 9
 and edx, 0x3f
-mov rdx, qword ptr [rsi + rdx*8]
+mov rdx, qword ptr [rdi + rdx*8]
 test rdx, rdx
 je L
@@ -97,5 +96,5 @@
 imul rax, rax, 0x70
 add rax, rdx
-cmp ecx, dword ptr [rax + 0x10]
+cmp esi, dword ptr [rax + 0x10]
 jne L
 mov rax, qword ptr [rax]
@@ -105,7 +104,7 @@
 jne L
 test byte ptr [rax + 0xd3d], 4
-jne L
-cmp byte ptr [rax + 0x624], 4
-je L
+je L
```
(ещё 431 строк диффа: so-query.py fdiff libserver.so 0x5c1e0f0)

### изменена: 0x5c20600 (1098 байт)
было: 0x5c205f0 (1090 байт)
- прямых вызовов: 19 → 20
- цели вызовов: +0x61cd3c0
- инструкций: 234 → 233
```diff
@@ -60,5 +60,23 @@
 cmp byte ptr [rbx + 0x14], 0
 mov rax, qword ptr [rbx]
-jne L
+je L
+mov rdi, qword ptr [rax + 0x10]
+call F
+mov rdi, rbx
+call F
+xor eax, eax
+add rsp, 0x118
+pop rbx
+pop r12
+pop r13
+pop rbp
+ret
+nop dword ptr [rax]
+mov rdi, qword ptr [rdi + 0x10]
+call F
+mov rdi, rbx
+call F
+jmp L
+nop dword ptr [rax + rax]
 mov ecx, 0xffffffff
 pxor xmm0, xmm0
@@ -149,29 +167,14 @@
 pop rbp
 jmp F
-nop dword ptr [rax + rax]
-mov rdi, qword ptr [rdi + 0x10]
-call F
-mov rdi, rbx
-call F
-add rsp, 0x118
-xor eax, eax
-pop rbx
-pop r12
-pop r13
-pop rbp
-ret
-nop dword ptr [rax]
-add rsp, 0x118
+nop
+mov rdi, r13
+call F
+test al, al
+jne L
 mov eax, 1
-pop rbx
-pop r12
-pop r13
-pop rbp
-ret
-nop dword ptr [rax + rax]
-mov rdi, qword ptr [rax + 0x10]
-call F
-mov rdi, rbx
-call F
+jmp L
+nop word ptr [rax + rax]
+movzx eax, word ptr [K:0xffff]
+mov word ptr [rbp - 0xdc], ax
 jmp L
 nop dword ptr [rax + rax]
@@ -202,5 +205,5 @@
 call qword ptr [rax + 0x100]
 jmp L
-nop
+nop word ptr [rax + rax]
 mov rax, qword ptr [rbx]
 mov rdi, qword ptr [rax + 0x10]
@@ -220,8 +223,4 @@
 jmp L
 nop dword ptr [rax]
-movzx eax, word ptr [K:0xffff]
-mov word ptr [rbp - 0xdc], ax
-jmp L
-nop dword ptr [rax + rax]
 lea rdx, [rbx + 0x20]
 cmp qword ptr [rax], rdx
```

### удалена: 0x5bf0340 (113 байт)


## Строки библиотек

