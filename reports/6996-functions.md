# Dota 6996: изменения кода по функциям и строки библиотек

Снимки `6995-11273798` → `6996-11274611`; funcdiff.py. В диффе: [S:…] — строка, [K:…] — константа из данных, F — вызов другой функции, L — переход внутри функции, [D]/[T] — прочие адреса. Регистры и смещения стека меняются и от перекомпиляции. Здесь всё, в том числе игровые функции и изменения от пересборки.

## libclient.so: функций 281894 → 281894; без изменений 281894, изменено 0, добавлено 0, удалено 0

## libserver.so: функций 221948 → 221948; без изменений 221942, изменено 6, добавлено 0, удалено 0

### изменена: 0x5163ee0 (1236 байт) | строки: "modifier_vengefulspirit_hybrid_special"
было: 0x5163ee0 (1201 байт)
- числа в инструкциях: −0x1378
- инструкций: 294 → 301
```diff
@@ -166,13 +166,15 @@
 mov rdi, r15
 call F
+test rax, rax
+je L
 mov qword ptr [rbp - 0x48], rax
 call F
-test al, al
-jne L
-mov rax, qword ptr [rbp - 0x48]
-cmp byte ptr [rax + 0x175a], 0
+mov r8, qword ptr [rbp - 0x48]
+test al, al
+jne L
+cmp byte ptr [r8 + 0x175a], 0
 je L
 lea rdx, [D]
-add rax, 0x1378
+lea rax, [r8 + 0x1378]
 xor ecx, ecx
 mov esi, 0xad
@@ -214,5 +216,5 @@
 jne L
 jmp L
-nop dword ptr [rax + rax]
+nop word ptr cs:[rax + rax]
 movzx edx, byte ptr [r15 + 0x624]
 jmp L
@@ -221,11 +223,11 @@
 jne L
 jmp L
-mov rax, qword ptr [rbp - 0x48]
+lea rdx, [D]
+lea rdi, [r8 + 0x1378]
 xor ecx, ecx
 mov esi, 0xad
-lea rdx, [D]
-lea rdi, [rax + 0x1378]
 call F
 ucomiss xmm0, dword ptr [K:1]
+mov r8, qword ptr [rbp - 0x48]
 jp L
 jne L
@@ -242,8 +244,10 @@
 test al, al
 je L
-mov rdi, qword ptr [rbp - 0x48]
 lea rsi, [S:"modifier_vengefulspirit_hybrid_special"]
 xor edx, edx
-call F
+mov rdi, r8
+mov qword ptr [rbp - 0x48], r8
+call F
+mov r8, qword ptr [rbp - 0x48]
 test rax, rax
 setne r12b
@@ -260,6 +264,8 @@
 pop rbp
 jmp F
+mov qword ptr [rbp - 0x48], r8
 mov rdi, r15
 call rax
+mov r8, qword ptr [rbp - 0x48]
 jmp L
 mov rdi, r15
@@ -292,3 +298,4 @@
 call F
 mov rax, qword ptr [r15 + 0x840]
-jmp L
+mov r8, qword ptr [rbp - 0x48]
+jmp L
```

### изменена: 0x518a290 (228 байт)
было: 0x518a290 (243 байт)
- инструкций: 67 → 65
```diff
@@ -23,21 +23,13 @@
 mov rdi, qword ptr [rax]
 call F
-mov rdi, rbx
-mov r12, rax
-lea rax, [rax + 0x1130]
-test r12, r12
-cmovne r12, rax
-call F
-mov r13, rax
+test rax, rax
+jne L
 add rsp, 8
-mov rsi, r13
-mov rdi, r12
 pop rbx
-mov edx, 1
 pop r12
 pop r13
 pop rbp
-jmp F
-nop dword ptr [rax + rax]
+ret
+nop dword ptr [rax]
 mov esi, dword ptr [r12 + 0x4c]
 cmp esi, -1
@@ -54,14 +46,20 @@
 mov rdi, qword ptr [rax]
 call F
-mov r12, rax
-lea rax, [rax + 0x1130]
-test r12, r12
-cmovne r12, rax
-jmp L
-nop dword ptr [rax]
+test rax, rax
+je L
+lea r12, [rax + 0x1130]
 add rsp, 8
+mov rsi, r13
+mov rdi, r12
 pop rbx
+mov edx, 1
 pop r12
 pop r13
 pop rbp
-ret
+jmp F
+nop word ptr [rax + rax]
+lea r12, [rax + 0x1130]
+mov rdi, rbx
+call F
+mov r13, rax
+jmp L
```

### изменена: 0x5283b50 (6181 байт) | строки: "Bot"; "HeroType"; "DOTA_BOT_TANK"; "DOTA_BOT_STUN_SUPPORT"; "DOTA_BOT_PURE_SUPPORT"; "DOTA_BOT_PUSH_SUPPORT"; "DOTA_BOT_HARD_CARRY"; "DOTA_BOT_SEMI_CARRY"
было: 0x5283b50 (5731 байт)
- числа в инструкциях: +0 +0 +0 +0 +0 +0 +1 +1 (и ещё 1)
- прямых вызовов: 121 → 120
- инструкций: 1208 → 1264
```diff
@@ -2,54 +2,55 @@
 mov rbp, rsp
 push r15
-mov r15, r8
 push r14
 push r13
+mov r13, r8
 push r12
 push rbx
 mov ebx, r9d
 sub rsp, 0xc8
-lea rax, [D]
+lea r15, [D]
 mov dword ptr [rbp - 0x7c], esi
-mov qword ptr [rbp - 0xc8], rdi
-mov dword ptr [rbp - 0x80], edx
-mov qword ptr [rbp - 0x98], rcx
-mov rdi, qword ptr [rax]
+mov qword ptr [rbp - 0xd0], rdi
+mov dword ptr [rbp - 0xc4], edx
+mov qword ptr [rbp - 0xa0], rcx
+mov rdi, qword ptr [r15]
 call F
 cmp byte ptr [D], 0
 lea rdi, [D]
-mov dword ptr [rbp - 0x90], eax
-jne L
-cmp byte ptr [D], 0
-je L
-call F
-xor r13d, r13d
+mov dword ptr [rbp - 0x80], eax
+jne L
+cmp byte ptr [D], 0
+je L
+call F
+xor r12d, r12d
+mov byte ptr [rbp - 0xe5], 0
+test eax, eax
+mov ecx, eax
+mov byte ptr [rbp - 0xb8], 0
 mov byte ptr [rbp - 0xdd], 0
-test eax, eax
-mov r12d, eax
-mov byte ptr [rbp - 0xb0], 0
-mov byte ptr [rbp - 0xd5], 0
-mov byte ptr [rbp - 0xd6], 0
-mov byte ptr [rbp - 0xd7], 0
-mov byte ptr [rbp - 0xb8], 0
-mov byte ptr [rbp - 0xd8], 0
-je L
-lea rax, [r15 + 0x60]
+mov byte ptr [rbp - 0xde], 0
+mov byte ptr [rbp - 0xdf], 0
+mov byte ptr [rbp - 0xc0], 0
+mov byte ptr [rbp - 0xe0], 0
+je L
+lea rax, [r13 + 0x60]
 mov r14d, 1
-mov qword ptr [rbp - 0x78], rax
-mov rax, r15
-mov r15d, r14d
-mov r14, rax
-test r14, r14
-je L
-mov rdx, qword ptr [rbp - 0x78]
-mov rax, r14
-cmp dword ptr [rax], r15d
-jne L
-lea eax, [r15 + 1]
-cmp r12d, r15d
-je L
-mov r15d, eax
-mov rax, r14
-cmp dword ptr [rax], r15d
+mov dword ptr [rbp - 0x78], ebx
+mov rbx, r13
+mov qword ptr [rbp - 0x88], rax
+mov r13d, r14d
+mov r14d, ecx
+test rbx, rbx
+je L
+mov rdx, qword ptr [rbp - 0x88]
+mov rax, rbx
+cmp dword ptr [rax], r13d
+jne L
+lea eax, [r13 + 1]
+cmp r14d, r13d
+je L
+mov r13d, eax
+mov rax, rbx
+cmp dword ptr [rax], r13d
 je L
 add rax, 4
@@ -58,5 +59,5 @@
 cmp byte ptr [D], 0
 lea rax, [D]
-mov qword ptr [rbp - 0xa0], rax
+mov qword ptr [rbp - 0x98], rax
 lea rdi, [rax + 0x1958]
 jne L
@@ -66,5 +67,5 @@
 lea rax, [D]
 cmove rdi, rax
-mov esi, r15d
+mov esi, r13d
 call F
 test rax, rax
@@ -79,85 +80,77 @@
 mov rdi, rax
 call F
-lea rsi, [D]
-test rax, rax
-mov qword ptr [rbp - 0x88], rsi
-je L
-xor ecx, ecx
-xor edx, edx
-mov rdi, rax
-call F
-mov qword ptr [rbp - 0x88], rax
```
(ещё 1575 строк диффа: so-query.py fdiff libserver.so 0x5283b50)

### изменена: 0x52925a0 (2392 байт) | строки: "!bCanIncrementStats"; "BaseKillEaterFound without stat tracking item."
было: 0x52923e0 (2392 байт)
- числа в инструкциях: +0x7629 −0x7624
- инструкций: 506 → 506
```diff
@@ -493,5 +493,5 @@
 movdqa xmm4, xmmword ptr [rbp - 0x2c0]
 mov rdi, r13
-mov dword ptr [rbp - 0x258], 0x7624
+mov dword ptr [rbp - 0x258], 0x7629
 mov qword ptr [rbp - 0x260], rax
 movzx eax, byte ptr [rbp - 0x254]
```

### изменена: 0x5cb2c20 (1204 байт) вызывается из: CDOTAPlayerController::vfunc#255
было: 0x5cb2a60 (1204 байт)
- инструкций: 271 → 271
```diff
@@ -124,6 +124,6 @@
 mov rcx, rax
 je L
-cmp r15d, dword ptr [rax + 0x100]
-jg L
+cmp dword ptr [rax + 0x100], r15d
+jb L
 test r15d, r15d
 je L
```

### изменена: 0x5cc57c0 (1820 байт) | строки: "CNetworkTransmitComponent::StateChanged(%s) @%s:%d"
было: 0x5cc5600 (1692 байт)
- числа в инструкциях: +0xff −0
- поля объектов: +0xbf6 +0xbf6
- инструкций: 370 → 395
```diff
@@ -2,10 +2,10 @@
 mov rbp, rsp
 push r15
-mov r15, rsi
 push r14
 push r13
-mov r13, rdi
 push r12
+mov r12, rsi
 push rbx
+mov rbx, rdi
 sub rsp, 0x188
 test byte ptr [rsi + 0x10], 1
@@ -13,31 +13,60 @@
 mov eax, dword ptr [rsi + 0x30]
 mov dword ptr [rdi + 0xbd0], eax
-mov eax, dword ptr [r15 + 0x20]
+mov eax, dword ptr [r12 + 0x20]
 test eax, eax
 je L
-mov rcx, qword ptr [r15 + 0x28]
+mov rdx, qword ptr [r12 + 0x28]
 sub eax, 1
 cdqe
-mov rax, qword ptr [rcx + rax*8 + 8]
+mov rax, qword ptr [rdx + rax*8 + 8]
 mov eax, dword ptr [rax + 0x38]
-cmp dword ptr [r13 + 0xbc4], eax
+cmp dword ptr [rbx + 0xbc4], eax
 jge L
-cmp dword ptr [r13 + 0xbfc], -1
-je L
-mov esi, dword ptr [r13 + 0xc58]
+cmp dword ptr [rbx + 0xbfc], -1
+je L
+mov ecx, dword ptr [rbx + 0xc58]
 lea rax, [D]
-test esi, esi
-mov rcx, qword ptr [rax]
+test ecx, ecx
+mov rdx, qword ptr [rax]
 js L
-mov edi, dword ptr [rcx + 0x44]
-cmp edi, esi
-je L
-lea eax, [rsi + 1]
-mov esi, edi
-sub esi, eax
-cmp esi, 9
+mov esi, dword ptr [rdx + 0x44]
+cmp esi, ecx
+je L
+lea eax, [rcx + 1]
+mov ecx, esi
+sub ecx, eax
+cmp ecx, 9
 jg L
-movsxd rsi, eax
-mov r8d, eax
+movsxd rcx, eax
+mov edi, eax
+imul rcx, rcx, 0x66666667
+sar edi, 0x1f
+sar rcx, 0x22
+sub ecx, edi
+lea edi, [rcx + rcx*4]
+add edi, edi
+sub eax, edi
+mov edi, esi
+mov ecx, eax
+movsxd rax, esi
+sar edi, 0x1f
+imul rax, rax, 0x66666667
+sar rax, 0x22
+sub eax, edi
+lea edi, [rax + rax*4]
+mov eax, esi
+add edi, edi
+sub eax, edi
+cmp ecx, eax
+jle L
+lea edi, [rax + 0xa]
+cmp ecx, edi
+jg L
+mov eax, edi
+movzx edi, word ptr [rbx + 0xc56]
+add eax, 1
+nop dword ptr [rax + rax]
+movsxd rsi, ecx
+mov r8d, ecx
 imul rsi, rsi, 0x66666667
 sar r8d, 0x1f
@@ -45,131 +74,93 @@
 sub esi, r8d
 lea r8d, [rsi + rsi*4]
+mov esi, ecx
 add r8d, r8d
-sub eax, r8d
-mov r8d, edi
-mov esi, eax
-movsxd rax, edi
-sar r8d, 0x1f
+sub esi, r8d
+movsxd rsi, esi
+movzx r8d, byte ptr [rbx + rsi + 0xc4c]
+mov byte ptr [rbx + rsi + 0xc4c], 0
+cmp r8w, di
+cmova r8d, edi
+add ecx, 1
+sub edi, r8d
+cmp ecx, eax
+jne L
+mov word ptr [rbx + 0xc56], di
+movsxd rax, dword ptr [rdx + 0x44]
+mov rsi, rax
 imul rax, rax, 0x66666667
+mov edx, esi
+sar edx, 0x1f
 sar rax, 0x22
-sub eax, r8d
```
(ещё 489 строк диффа: so-query.py fdiff libserver.so 0x5cc57c0)


## Строки библиотек

