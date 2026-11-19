# Dota 6984: изменения кода по функциям

Снимки `6983-11256873` → `6984-11257680`; funcdiff.py. В диффе: [S:…] — строка, [K:…] — константа из данных, F — вызов другой функции, L — переход внутри функции, [D]/[T] — прочие адреса. Регистры и смещения стека меняются и от перекомпиляции.

## libclient.so: функций 281790 → 281883; без изменений 281716, изменено 61, добавлено 93, удалено 4

### изменена: 0x4751cd0 (2009 байт) | строки: "ScriptFile"; "ExtendInstance"; "Init"
было: 0x4751360 (2061 байт)
- числа в инструкциях: −1 −1
- виртуальные вызовы: −0x20 (слот 4)
- прямых вызовов: 39 → 37
- инструкций: 437 → 423
```diff
@@ -329,35 +329,8 @@
 jmp L
 nop dword ptr [rax]
-xor esi, esi
-mov rdi, rbx
-call F
-mov rax, qword ptr [rbx + 0x10]
-test byte ptr [rbp - 0x46], 1
-mov r15, qword ptr [rax + 0x28]
-je L
-mov rax, qword ptr [D]
-mov rsi, qword ptr [rbp - 0x50]
-mov rdi, qword ptr [rax]
-mov rax, qword ptr [rdi]
-call qword ptr [rax + 0x20]
-and word ptr [rbp - 0x46], 0xfffe
-jmp L
-nop word ptr [rax + rax]
 mov qword ptr [D], 0
 lock sub dword ptr [D], 3
 je L
 lea rdi, [D]
-call F
-jmp L
-nop word ptr [rax + rax]
-lea r12, [D]
-mov esi, 3
-mov r13, qword ptr [rbx + 0x828]
-mov edi, dword ptr [r12]
-call F
-test al, al
-jne L
-sub word ptr [D], 1
-jne L
 call F
 lea rsp, [rbp - 0x28]
@@ -369,28 +342,27 @@
 pop rbp
 ret
-nop word ptr cs:[rax + rax]
-xor esi, esi
-mov rdi, rbx
-call F
-mov rdi, qword ptr [rbx + 0x770]
-test rdi, rdi
-jne L
-jmp L
-nop
-lea r12, [D]
-mov esi, 3
-mov edi, dword ptr [r12]
-call F
-test al, al
-jne L
-test byte ptr [rbp - 0x56], 1
+nop dword ptr [rax]
+xor esi, esi
+mov rdi, rbx
+call F
+mov rax, qword ptr [rbx + 0x10]
+test byte ptr [rbp - 0x46], 1
+mov r15, qword ptr [rax + 0x28]
 je L
 mov rax, qword ptr [D]
-mov rsi, qword ptr [rbp - 0x60]
+mov rsi, qword ptr [rbp - 0x50]
 mov rdi, qword ptr [rax]
 mov rax, qword ptr [rdi]
 call qword ptr [rax + 0x20]
-jmp L
-nop dword ptr [rax + rax]
+and word ptr [rbp - 0x46], 0xfffe
+jmp L
+nop word ptr [rax + rax]
+lea r12, [D]
+mov esi, 3
+mov r13, qword ptr [rbx + 0x828]
+mov edi, dword ptr [r12]
+call F
+test al, al
+je L
 mov rax, qword ptr [rbx + 0x770]
 test rax, rax
@@ -406,5 +378,19 @@
 call F
 jmp L
-nop dword ptr [rax + rax]
+nop word ptr [rax + rax]
+xor esi, esi
+mov rdi, rbx
+call F
+mov rdi, qword ptr [rbx + 0x770]
+test rdi, rdi
+jne L
+jmp L
+nop
+lea r12, [D]
+mov esi, 3
+mov edi, dword ptr [r12]
+call F
+test al, al
+je L
 mov rax, qword ptr [rbx + 0x770]
 test rax, rax
```

### изменена: 0x4754430 (4762 байт) вызывается из: CDOTA_Modifier_Lua::vfunc#88
было: 0x4753af0 (3694 байт)
- числа в инструкциях: +0x1a0 −0x191
- инструкций: 627 → 805
```diff
@@ -1,3 +1,3 @@
-cmp esi, 0x191
+cmp esi, 0x1a0
 ja L
 lea rdx, [D]
@@ -626,2 +626,180 @@
 lea rax, [T]
 jmp L
+lea rax, [T]
+jmp L
+lea rax, [T]
+jmp L
+lea rax, [T]
+jmp L
+lea rax, [T]
+jmp L
+lea rax, [T]
+jmp L
+lea rax, [T]
+jmp L
+lea rax, [T]
+jmp L
+lea rax, [T]
+jmp L
+lea rax, [T]
+jmp L
+lea rax, [T]
+jmp L
+lea rax, [T]
+jmp L
+lea rax, [T]
+jmp L
+lea rax, [T]
+jmp L
+lea rax, [T]
+jmp L
+lea rax, [T]
+jmp L
+lea rax, [T]
+jmp L
+lea rax, [T]
+jmp L
+lea rax, [T]
+jmp L
+lea rax, [T]
+jmp L
+lea rax, [T]
+jmp L
+lea rax, [T]
+jmp L
+lea rax, [T]
+jmp L
+lea rax, [T]
+jmp L
+lea rax, [T]
+jmp L
+lea rax, [T]
+jmp L
+lea rax, [T]
+jmp L
+lea rax, [T]
+jmp L
+lea rax, [T]
+jmp L
+lea rax, [T]
+jmp L
+lea rax, [T]
+jmp L
+lea rax, [T]
+jmp L
+lea rax, [T]
+jmp L
+lea rax, [T]
+jmp L
+lea rax, [T]
+jmp L
+lea rax, [T]
+jmp L
+lea rax, [T]
+jmp L
+lea rax, [T]
+jmp L
+lea rax, [T]
+jmp L
+lea rax, [T]
+jmp L
+lea rax, [T]
+jmp L
+lea rax, [T]
+jmp L
+lea rax, [T]
+jmp L
+lea rax, [T]
+jmp L
+lea rax, [T]
+jmp L
+lea rax, [T]
+jmp L
+lea rax, [T]
+jmp L
+lea rax, [T]
+jmp L
+lea rax, [T]
+jmp L
+lea rax, [T]
+jmp L
+lea rax, [T]
+jmp L
+lea rax, [T]
+jmp L
+lea rax, [T]
+jmp L
+lea rax, [T]
+jmp L
+lea rax, [T]
+jmp L
+lea rax, [T]
+jmp L
+lea rax, [T]
+jmp L
```
(ещё 66 строк диффа: so-query.py fdiff libclient.so 0x4754430)

### изменена: 0x4751830 (535 байт) C_DOTA_Ability_Lua::GetCustomCastErrorTarget | строки: "GetCustomCastErrorTarget"; "CUSTOM ERROR"
было: 0x47549d0 (551 байт)
- прямых вызовов: 11 → 10
- инструкций: 129 → 126
```diff
@@ -105,11 +105,8 @@
 jmp L
 nop word ptr [rax + rax]
-mov rax, qword ptr [rbp - 0x50]
-cmp byte ptr [rax], 0
+mov rsi, qword ptr [rbp - 0x50]
+cmp byte ptr [rsi], 0
 je L
-lea rdi, [rbp - 0x50]
-call F
 lea rdi, [r12 + 0x858]
-mov rsi, rax
 call F
 mov rbx, qword ptr [r12 + 0x858]
```

### изменена: 0x4751490 (429 байт) C_DOTA_Ability_Lua::GetCustomCastError | строки: "GetCustomCastError"; "CUSTOM ERROR"
было: 0x4754c00 (441 байт)
- прямых вызовов: 9 → 8
- инструкций: 103 → 100
```diff
@@ -89,11 +89,8 @@
 jmp L
 nop word ptr [rax + rax]
-mov rax, qword ptr [rbp - 0x40]
-cmp byte ptr [rax], 0
+mov rsi, qword ptr [rbp - 0x40]
+cmp byte ptr [rsi], 0
 je L
-lea rdi, [rbp - 0x40]
-call F
 lea rdi, [r12 + 0x850]
-mov rsi, rax
 call F
 mov rbx, qword ptr [r12 + 0x850]
```

### изменена: 0x4751640 (493 байт) C_DOTA_Ability_Lua::GetCustomCastErrorLocation | строки: "GetCustomCastErrorLocation"; "CUSTOM ERROR"
было: 0x4754dc0 (505 байт)
- прямых вызовов: 10 → 9
- инструкций: 118 → 115
```diff
@@ -104,11 +104,8 @@
 jmp L
 nop word ptr [rax + rax]
-mov rax, qword ptr [rbp - 0x50]
-cmp byte ptr [rax], 0
+mov rsi, qword ptr [rbp - 0x50]
+cmp byte ptr [rsi], 0
 je L
-lea rdi, [rbp - 0x50]
-call F
 lea rdi, [r12 + 0x860]
-mov rsi, rax
 call F
 mov rbx, qword ptr [r12 + 0x860]
```

### изменена: 0x474ee90 (329 байт) C_DOTA_Ability_DataDriven::GetChannelTime | строки: "AbilityChannelTime"
было: 0x4754fc0 (277 байт)
- числа в инструкциях: +1
- виртуальные вызовы: +0x20 (слот 4) +0x20 (слот 4)
- инструкций: 78 → 90
```diff
@@ -36,19 +36,25 @@
 mov rax, qword ptr [rbx]
 mov rsi, rbx
-lea r12, [rbp - 0x30]
-mov rdi, r12
+lea rdi, [rbp - 0x30]
 call qword ptr [rax + 0xb78]
-movzx eax, byte ptr [rbp - 0x28]
-cmp al, 0x3a
+movzx edx, byte ptr [rbp - 0x28]
+movzx eax, word ptr [rbp - 0x26]
+and eax, 1
+cmp dl, 0x3a
 ja L
-movabs rdx, 0x6000026040000a2
-bt rdx, rax
+movabs rcx, 0x6000026040000a2
+bt rcx, rdx
 jae L
-cmp al, 0x22
+cmp dl, 0x22
 movss xmm0, dword ptr [rbp - 0x30]
 je L
-mov rdi, r12
+test ax, ax
+je L
+mov rax, qword ptr [D]
 movss dword ptr [rbp - 0x34], xmm0
-call F
+mov rsi, qword ptr [rbp - 0x30]
+mov rdi, qword ptr [rax]
+mov rax, qword ptr [rdi]
+call qword ptr [rax + 0x20]
 movss xmm0, dword ptr [rbp - 0x34]
 add rsp, 0x28
@@ -58,4 +64,5 @@
 pop rbp
 ret
+nop
 xor esi, esi
 call F
@@ -71,6 +78,11 @@
 jmp F
 nop dword ptr [rax]
-mov rdi, r12
-call F
+test ax, ax
+je L
+mov rax, qword ptr [D]
+mov rsi, qword ptr [rbp - 0x30]
+mov rdi, qword ptr [rax]
+mov rax, qword ptr [rdi]
+call qword ptr [rax + 0x20]
 jmp L
 pxor xmm0, xmm0
```

### изменена: 0x474efe0 (329 байт) C_DOTA_Item_DataDriven::GetChannelTime | строки: "AbilityChannelTime"
было: 0x47550e0 (277 байт)
- числа в инструкциях: +1
- виртуальные вызовы: +0x20 (слот 4) +0x20 (слот 4)
- инструкций: 78 → 90
```diff
@@ -36,19 +36,25 @@
 mov rax, qword ptr [rbx]
 mov rsi, rbx
-lea r12, [rbp - 0x30]
-mov rdi, r12
+lea rdi, [rbp - 0x30]
 call qword ptr [rax + 0xcc0]
-movzx eax, byte ptr [rbp - 0x28]
-cmp al, 0x3a
+movzx edx, byte ptr [rbp - 0x28]
+movzx eax, word ptr [rbp - 0x26]
+and eax, 1
+cmp dl, 0x3a
 ja L
-movabs rdx, 0x6000026040000a2
-bt rdx, rax
+movabs rcx, 0x6000026040000a2
+bt rcx, rdx
 jae L
-cmp al, 0x22
+cmp dl, 0x22
 movss xmm0, dword ptr [rbp - 0x30]
 je L
-mov rdi, r12
+test ax, ax
+je L
+mov rax, qword ptr [D]
 movss dword ptr [rbp - 0x34], xmm0
-call F
+mov rsi, qword ptr [rbp - 0x30]
+mov rdi, qword ptr [rax]
+mov rax, qword ptr [rdi]
+call qword ptr [rax + 0x20]
 movss xmm0, dword ptr [rbp - 0x34]
 add rsp, 0x28
@@ -58,4 +64,5 @@
 pop rbp
 ret
+nop
 xor esi, esi
 call F
@@ -71,6 +78,11 @@
 jmp F
 nop dword ptr [rax]
-mov rdi, r12
-call F
+test ax, ax
+je L
+mov rax, qword ptr [D]
+mov rsi, qword ptr [rbp - 0x30]
+mov rdi, qword ptr [rax]
+mov rax, qword ptr [rdi]
+call qword ptr [rax + 0x20]
 jmp L
 pxor xmm0, xmm0
```

### изменена: 0x4756300 (1396 байт)
было: 0x4755a60 (1364 байт)
- числа в инструкциях: +0x1e
- прямых вызовов: 25 → 24
- инструкций: 305 → 309
```diff
@@ -119,5 +119,5 @@
 cmp al, 0x4f
 je L
-nop dword ptr [rax]
+nop dword ptr [rax + rax]
 pxor xmm0, xmm0
 mov qword ptr [r12], 1
@@ -150,9 +150,35 @@
 jmp L
 nop dword ptr [rax]
-lea rdi, [rbp - 0x70]
-call F
+cmp al, 0x22
+movss xmm0, dword ptr [rbp - 0x70]
+je L
+movss dword ptr [r12 + 4], xmm0
+pxor xmm0, xmm0
+mov dword ptr [r12], 1
+movups xmmword ptr [r12 + 8], xmm0
+jmp L
+nop dword ptr [rax + rax]
+cmp rax, r14
+jne L
+jmp L
+nop word ptr cs:[rax + rax]
+add word ptr [D], 1
+lea rax, [D]
+mov qword ptr [rbp - 0x88], rax
+jmp L
+nop dword ptr [rax + rax]
+mov qword ptr [D], 0
+lock sub dword ptr [D], 3
+je L
+mov rdi, qword ptr [rbp - 0x88]
+call F
+jmp L
+nop word ptr [rax + rax]
+mov rsi, qword ptr [rbp - 0x70]
+lea rax, [D]
+test rsi, rsi
+cmove rsi, rax
+mov qword ptr [rbp - 0x50], 0
 lea r14, [rbp - 0x50]
-mov qword ptr [rbp - 0x50], 0
-mov rsi, rax
 mov rdi, r14
 call F
@@ -185,5 +211,4 @@
 nop word ptr cs:[rax + rax]
 nop word ptr cs:[rax + rax]
-nop dword ptr [rax + rax]
 mov rdx, qword ptr [rbx + 0x1b38]
 mov qword ptr [rdx + rax], 0
@@ -230,38 +255,17 @@
 mov qword ptr [r12 + 8], rax
 jmp L
-nop dword ptr [rax]
-cmp al, 0x22
-movss xmm0, dword ptr [rbp - 0x70]
-je L
-movss dword ptr [r12 + 4], xmm0
-pxor xmm0, xmm0
-mov dword ptr [r12], 1
-movups xmmword ptr [r12 + 8], xmm0
-jmp L
-nop dword ptr [rax + rax]
-cmp rax, r14
-jne L
-jmp L
-nop word ptr cs:[rax + rax]
-add word ptr [D], 1
-lea rax, [D]
-mov qword ptr [rbp - 0x88], rax
-jmp L
-nop dword ptr [rax + rax]
-mov qword ptr [D], 0
-lock sub dword ptr [D], 3
-je L
-mov rdi, qword ptr [rbp - 0x88]
-call F
-jmp L
-nop word ptr [rax + rax]
+pxor xmm0, xmm0
+cvtsd2ss xmm0, qword ptr [rbp - 0x70]
+jmp L
+nop
 lea r15, [D]
 xor edx, edx
 jmp L
-nop
-pxor xmm0, xmm0
-cvtsd2ss xmm0, qword ptr [rbp - 0x70]
-jmp L
-nop
+nop dword ptr [rax + rax]
+cmp al, 0x1e
+mov rsi, qword ptr [rbp - 0x70]
+jne L
+jmp L
+nop dword ptr [rax]
 cmp r8d, ecx
 mov eax, r8d
@@ -278,5 +282,5 @@
 call F
 jmp L
-nop
+nop word ptr [rax + rax]
 lea rdi, [rbx + 0x1b38]
 mov esi, edx
```

### изменена: 0x4762360 (19037 байт) вызывается из: CDOTA_Modifier_Lua::vfunc#111, CDOTA_Modifier_Lua_Horizontal_Motion::vfunc#111, CDOTA_Modifier_Lua_Vertical_Motion::vfunc#111 | строки: "CDOTA_Modifier_Lua"; "A lua-based modifier."; "Runs when the think interval occurs."; "Script_OnIntervalThink"; "Runs when the modifier is created."; "Script_OnCreated"; "table"; "Runs when the modifier is refreshed."
было: 0x4760a40 (18013 байт)
- числа в инструкциях: +0 +0 +0 +0 +0 +0 +0 +0 (и ещё 44)
- поля объектов: +0x18 +0x18 +0x18 +0x18 +0x18 +0x18 +0x18 +0x18 +0x18 +0x18 +0x18 +0x18 (и ещё 92)
- инструкций: 4498 → 4706
```diff
@@ -40,119 +40,139 @@
 je L
 mov qword ptr [rbx + 0x48], rdx
-lea r13, [rbx + 0x20]
-mov rdi, r13
-call F
-xor esi, esi
+movsxd r12, dword ptr [rbx + 0x20]
+cmp r12d, dword ptr [rbx + 0x30]
+mov eax, r12d
+je L
+mov rdx, qword ptr [rbx + 0x28]
+add eax, 1
+pxor xmm0, xmm0
+xor r13d, r13d
+mov dword ptr [rbx + 0x20], eax
+lea rax, [r12 + r12*4]
+lea rdi, [S:"Runs when the think interval occurs."]
+shl rax, 4
+add rdx, rax
+movups xmmword ptr [rdx], xmm0
+movups xmmword ptr [rdx + 0x28], xmm0
 movq xmm0, qword ptr [D]
-cdqe
-lea rdx, [rax + rax*4]
-lea rax, [S:"Runs when the think interval occurs."]
-shl rdx, 4
-add rdx, qword ptr [rbx + 0x28]
-mov qword ptr [rdx + 0x10], rax
-lea rax, [S:"Script_OnIntervalThink"]
-movq xmm1, rax
-movsx eax, byte ptr [rdx + 0x1a]
-mov qword ptr [rdx + 0x30], rbx
+mov qword ptr [rdx + 0x10], 0
+mov qword ptr [rdx + 0x18], 0xff1d
+add rax, qword ptr [rbx + 0x28]
+lea rdx, [S:"Script_OnIntervalThink"]
+movq xmm1, rdx
 punpcklqdq xmm0, xmm1
-mov word ptr [rdx + 0x18], si
-movups xmmword ptr [rdx], xmm0
-mov ecx, eax
+movsx edx, byte ptr [rax + 0x1a]
+mov qword ptr [rax + 0x30], rbx
+mov qword ptr [rax + 0x10], rdi
+movups xmmword ptr [rax], xmm0
+mov word ptr [rax + 0x18], r13w
+mov ecx, edx
 sub ecx, 1
 js L
 movsxd rcx, ecx
-cmp byte ptr [rdx + rcx + 0x1b], 0x20
-jne L
-mov byte ptr [rdx + 0x19], 1
-lea ecx, [rax - 2]
-cmp eax, 1
-je L
-movsxd rcx, ecx
-cmp byte ptr [rdx + rcx + 0x1b], 0x20
-jne L
-mov byte ptr [rdx + 0x19], 2
-lea ecx, [rax - 3]
-cmp eax, 2
-je L
-movsxd rcx, ecx
-cmp byte ptr [rdx + rcx + 0x1b], 0x20
-jne L
-mov byte ptr [rdx + 0x19], 3
-lea ecx, [rax - 4]
-cmp eax, 3
-je L
-movsxd rcx, ecx
-cmp byte ptr [rdx + rcx + 0x1b], 0x20
-jne L
-mov byte ptr [rdx + 0x19], 4
-lea ecx, [rax - 5]
-cmp eax, 4
-je L
-movsxd rcx, ecx
-cmp byte ptr [rdx + rcx + 0x1b], 0x20
-jne L
-mov byte ptr [rdx + 0x19], 5
-lea ecx, [rax - 6]
-cmp eax, 5
-je L
-movsxd rcx, ecx
-cmp byte ptr [rdx + rcx + 0x1b], 0x20
-jne L
-mov byte ptr [rdx + 0x19], 6
-lea ecx, [rax - 7]
-cmp eax, 6
-je L
-movsxd rcx, ecx
-cmp byte ptr [rdx + rcx + 0x1b], 0x20
-jne L
-mov byte ptr [rdx + 0x19], 7
-lea ecx, [rax - 8]
-cmp eax, 7
-je L
-movsxd rcx, ecx
-cmp byte ptr [rdx + rcx + 0x1b], 0x20
-jne L
-mov byte ptr [rdx + 0x19], 8
-lea ecx, [rax - 9]
-cmp eax, 8
-je L
-movsxd rcx, ecx
-cmp byte ptr [rdx + rcx + 0x1b], 0x20
-jne L
-mov byte ptr [rdx + 0x19], 9
-lea ecx, [rax - 0xa]
-cmp eax, 9
-je L
-movsxd rcx, ecx
-cmp byte ptr [rdx + rcx + 0x1b], 0x20
-jne L
-mov byte ptr [rdx + 0x19], 0xa
-lea ecx, [rax - 0xb]
-cmp eax, 0xa
-je L
```
(ещё 1446 строк диффа: so-query.py fdiff libclient.so 0x4762360)

### изменена: 0x4768980 (4411 байт) | строки: "scripts/height_levels.txt"; "modifier_datadriven"; "modifier_lua"; "modifier_lua_horizontal_motion"; "modifier_lua_vertical_motion"; "modifier_lua_motion_both"
было: 0x4766c80 (3847 байт)
- константы из данных (числа логики): +0x00000000000000090000000000000000 +0x00000000000000090000000000000000
- числа в инструкциях: +0xffffffff +0xffffffff +0x20 +0x20
- прямых вызовов: 69 → 67
- инструкций: 742 → 834
```diff
@@ -40,8 +40,8 @@
 cmp byte ptr [D], 0
 jne L
-xor r8d, r8d
-mov byte ptr [D], 1
-mov qword ptr [D], r8
-mov qword ptr [D], r8
+xor esi, esi
+mov byte ptr [D], 1
+mov qword ptr [D], rsi
+mov qword ptr [D], rsi
 mov byte ptr [D], 0
 cmp byte ptr [D], 0
@@ -63,5 +63,5 @@
 xor r8d, r8d
 jmp L
-nop
+nop dword ptr [rax]
 je L
 mov dword ptr [r15], 0
@@ -154,9 +154,9 @@
 mov dword ptr [r14 - 0xc], r12d
 mov qword ptr [r14 - 8], 0
-cmp rbx, r14
-jne L
-lea rax, [D]
-mov r9, rbx
-cmp rbx, rax
+cmp r14, rbx
+jne L
+lea rax, [D]
+mov r9, r14
+cmp r14, rax
 jne L
 lea r14, [D]
@@ -191,11 +191,11 @@
 jne L
 lea rax, [D]
-xor ecx, ecx
 mov byte ptr [D], 1
 movss xmm2, dword ptr [K:1]
-mov qword ptr [D], rcx
 mov dword ptr [D], 0x1000100
 movaps xmm0, xmmword ptr [rax]
 movaps xmm1, xmmword ptr [rax + 0x10]
+xor eax, eax
+mov qword ptr [D], rax
 movaps xmmword ptr [D], xmm1
 movaps xmm1, xmm0
@@ -481,9 +481,9 @@
 ret
 lea rax, [T]
-xor edi, edi
-mov rsi, rbx
-mov qword ptr [rbp - 0x48], r12
-mov qword ptr [rbp - 0x40], rdi
-lea rdi, [D]
+xor ecx, ecx
+mov rsi, rbx
+mov qword ptr [rbp - 0x48], r12
+lea rdi, [D]
+mov qword ptr [rbp - 0x40], rcx
 mov qword ptr [rbp - 0x50], rax
 mov byte ptr [D], 1
@@ -495,10 +495,56 @@
 test eax, eax
 je L
+movdqa xmm1, xmmword ptr [K:0x00000000000000090000000000000000]
+xor ecx, ecx
+xor r8d, r8d
+xor edi, edi
+xor edx, edx
+xor r9d, r9d
+mov eax, 0xffffffff
+pxor xmm0, xmm0
+movups xmmword ptr [D], xmm1
 lea rsi, [D]
-mov rdi, rsi
-call F
+movups xmmword ptr [D], xmm0
+movups xmmword ptr [D], xmm0
+movups xmmword ptr [D], xmm0
+movups xmmword ptr [D], xmm0
+movups xmmword ptr [D], xmm0
+movups xmmword ptr [D], xmm0
+mov qword ptr [D], r8
+mov qword ptr [D], r8
+mov qword ptr [D], r8
+mov qword ptr [D], r8
+mov qword ptr [D], r8
+mov qword ptr [D], r9
+mov qword ptr [D], rdx
+mov qword ptr [D], rdx
+mov qword ptr [D], rcx
+mov qword ptr [D], rcx
+mov qword ptr [D], rcx
+mov qword ptr [D], rcx
+mov qword ptr [D], rcx
+mov qword ptr [D], rcx
+mov qword ptr [D], rcx
+mov qword ptr [D], rcx
+mov qword ptr [D], rcx
+mov qword ptr [D], rcx
+mov qword ptr [D], rdi
+mov qword ptr [D], rdi
+mov qword ptr [D], rdi
+mov qword ptr [D], rdi
+mov qword ptr [D], rax
+mov qword ptr [D], 0x20
+mov qword ptr [D], r9
+lea rax, [D]
 lea rdi, [T]
+mov rdx, qword ptr [rax]
+mov qword ptr [rax], rsi
+mov qword ptr [D], rdx
+lea rdx, [D]
+mov eax, dword ptr [rdx]
+lea ecx, [rax + 1]
+mov dword ptr [D], eax
+mov dword ptr [rdx], ecx
```
(ещё 108 строк диффа: so-query.py fdiff libclient.so 0x4768980)

### изменена: 0x4769ac0 (380 байт) | строки: "C_DOTA_Ability_DataDriven"
было: 0x4767b90 (428 байт)
- числа в инструкциях: +0x8bc636b2 −0x2f17c763 −0x5bd1e995 −0x5bd1e995 −0x5bd1e995 −0x21bf90b7 −0xd −0xf
- прямых вызовов: 8 → 7
- инструкций: 98 → 85
```diff
@@ -57,24 +57,11 @@
 test eax, eax
 je L
-lea rdi, [D]
-mov esi, 0x2f17c763
-call F
 lea rcx, [rbp - 0x24]
 mov rsi, rbx
 mov rdi, r12
-imul eax, eax, 0x5bd1e995
+mov dword ptr [rbp - 0x24], 0x8bc636b2
 mov r9d, 2
 mov r8d, 0x8c0
-xor eax, 0x21bf90b7
-imul eax, eax, 0x5bd1e995
-mov edx, eax
-shr edx, 0xd
-xor eax, edx
-imul eax, eax, 0x5bd1e995
-mov edx, eax
-shr edx, 0xf
-xor eax, edx
 lea rdx, [S:"C_DOTA_Ability_DataDriven"]
-mov dword ptr [rbp - 0x24], eax
 call F
 lea rdx, [D]
@@ -85,5 +72,5 @@
 call F
 jmp L
-nop dword ptr [rax]
+nop word ptr [rax + rax]
 lea rdi, [D]
 mov esi, 1
```

### изменена: 0x4769f90 (396 байт) | строки: "C_DOTA_Item_DataDriven"
было: 0x4768090 (460 байт)
- числа в инструкциях: +0x6b3607ab −0x54d48e79 −0x5bd1e995 −0x5bd1e995 −0x5bd1e995 −0x5bd1e995 −0x199bf980 −0x90fcb405 −0xd (и ещё 1)
- прямых вызовов: 9 → 8
- инструкций: 99 → 84
```diff
@@ -56,26 +56,11 @@
 test eax, eax
 je L
-lea rdi, [D]
-mov esi, 0x54d48e79
-call F
 lea rcx, [rbp - 0x24]
 mov rsi, rbx
 mov rdi, r12
-imul eax, eax, 0x5bd1e995
+mov dword ptr [rbp - 0x24], 0x6b3607ab
 mov r9d, 2
 mov r8d, 0x970
-xor eax, 0x199bf980
-imul eax, eax, 0x5bd1e995
-xor eax, 0x90fcb405
-imul eax, eax, 0x5bd1e995
-mov edx, eax
-shr edx, 0xd
-xor eax, edx
-imul eax, eax, 0x5bd1e995
-mov edx, eax
-shr edx, 0xf
-xor eax, edx
 lea rdx, [S:"C_DOTA_Item_DataDriven"]
-mov dword ptr [rbp - 0x24], eax
 call F
 lea rdx, [D]
```

### изменена: 0x476a500 (2092 байт) CDOTA_Modifier_Lua::DeclareFunctions, CDOTA_Modifier_Lua_Horizontal_Motion::DeclareFunctions, CDOTA_Modifier_Lua_Vertical_Motion::DeclareFunctions | строки: "ExtendInstance"; "DeclareFunctions"
было: 0x4768640 (2028 байт)
- числа в инструкциях: +1 +0x10
- виртуальные вызовы: +0x20 (слот 4) +0x20 (слот 4)
- поля объектов: +0xa
- прямых вызовов: 52 → 50
- инструкций: 432 → 445
```diff
@@ -71,20 +71,20 @@
 mov r14, rax
 je L
-mov r15, qword ptr [rbx + 0x1af8]
+mov r8, qword ptr [rbx + 0x1af8]
+lea r15, [rbp - 0xa0]
 mov rdi, rbx
 mov qword ptr [rbp - 0xa0], 0
 mov dword ptr [rbp - 0x98], 0
-mov rax, qword ptr [r15]
-mov r8, qword ptr [rax + 0x158]
+mov rax, qword ptr [r8]
 mov qword ptr [rbp - 0xb0], r8
-call F
-mov r8, qword ptr [rbp - 0xb0]
+mov r9, qword ptr [rax + 0x158]
+mov qword ptr [rbp - 0xa8], r9
+call F
+mov rdi, qword ptr [rbp - 0xb0]
+mov rcx, r15
 mov rsi, r14
-mov rdi, r15
+mov r9, qword ptr [rbp - 0xa8]
 mov rdx, rax
-lea rax, [rbp - 0xa0]
-mov qword ptr [rbp - 0xa8], rax
-mov rcx, rax
-call r8
+call r9
 cmp byte ptr [rbp - 0x98], 0
 je L
@@ -105,10 +105,8 @@
 call F
 test byte ptr [rbp - 0x56], 1
-mov r15, rax
-jne L
-mov rdi, qword ptr [rbp - 0xa8]
-mov qword ptr [rbp - 0x60], r15
-lea r15, [rbp - 0x50]
-mov rsi, r15
+jne L
+lea rsi, [rbp - 0x50]
+mov rdi, r15
+mov qword ptr [rbp - 0x60], rax
 mov byte ptr [rbp - 0x58], 0x1f
 call F
@@ -120,15 +118,22 @@
 xor r8d, r8d
 mov rdx, r13
+lea r14, [rbp - 0x40]
 mov rax, qword ptr [rdi]
 push 1
 call qword ptr [rax + 0xc0]
-mov rdi, r15
-call F
-mov rdi, r13
-call F
 pop rcx
 pop rsi
-mov rdi, qword ptr [rbx + 0x1af8]
-mov rsi, qword ptr [rbp - 0xa8]
+sub r14, 0x10
+test byte ptr [r14 + 0xa], 1
+je L
+mov rax, qword ptr [D]
+mov rsi, qword ptr [r14]
+mov rdi, qword ptr [rax]
+mov rax, qword ptr [rdi]
+call qword ptr [rax + 0x20]
+cmp r14, r13
+jne L
+mov rdi, qword ptr [rbx + 0x1af8]
+mov rsi, r15
 mov rax, qword ptr [rdi]
 call qword ptr [rax + 0x178]
@@ -144,5 +149,5 @@
 test rax, rax
 mov rsi, rax
-mov qword ptr [rbp - 0xb8], rax
+mov qword ptr [rbp - 0xb0], rax
 je L
 mov qword ptr [rbp - 0x90], r14
@@ -157,7 +162,7 @@
 mov dword ptr [rbp - 0x88], 0x1f
 mov rdx, rax
-mov qword ptr [rbp - 0xc0], rax
-mov rax, qword ptr [rdi]
-mov qword ptr [rbp - 0xc8], r8
+mov qword ptr [rbp - 0xb8], rax
+mov rax, qword ptr [rdi]
+mov qword ptr [rbp - 0xc0], r8
 push 1
 call qword ptr [rax + 0xc0]
@@ -166,10 +171,10 @@
 pop rdx
 je L
-mov rdi, qword ptr [rbp - 0xc8]
-call F
 mov rdi, qword ptr [rbp - 0xc0]
 call F
-mov rdi, qword ptr [rbx + 0x1af8]
-mov rsi, qword ptr [rbp - 0xb8]
+mov rdi, qword ptr [rbp - 0xb8]
+call F
+mov rdi, qword ptr [rbx + 0x1af8]
+mov rsi, qword ptr [rbp - 0xb0]
 mov rax, qword ptr [rdi]
 call qword ptr [rax + 0xb8]
@@ -177,11 +182,13 @@
 mov rdi, rbx
 call F
-mov rdi, qword ptr [rbp - 0xa8]
-call F
-sub word ptr [D], 1
-jne L
-call F
-jmp L
-nop dword ptr [rax]
+test byte ptr [rbp - 0x96], 1
+je L
```
(ещё 134 строк диффа: so-query.py fdiff libclient.so 0x476a500)

### изменена: 0x48ddd50 (3600 байт)
было: 0x48dbe30 (3842 байт)
- числа в инструкциях: −-1 −-1 −-1 −0x7fff −3
- поля объектов: −0x28 −0x1a −0x20 −0x20 −0x18 −0x18 −0x10
- прямых вызовов: 37 → 35
- инструкций: 635 → 560
```diff
@@ -559,77 +559,2 @@
 call F
 jmp L
-test rdi, rdi
-je L
-push rbp
-mov rbp, rsp
-push rbx
-sub rsp, 8
-call F
-mov rbx, rax
-call F
-movzx ecx, word ptr [rbx + 0x28]
-cmp cx, -1
-je L
-test word ptr [rbx + 0x1a], 0x7fff
-cwde
-je L
-mov r8, qword ptr [rbx + 0x20]
-movzx edx, cx
-lea rdx, [rdx + rdx*2]
-shl rdx, 3
-lea rdi, [r8 + rdx]
-mov esi, dword ptr [rdi + 8]
-cmp eax, esi
-jb L
-cmp esi, eax
-jb L
-cmp cx, word ptr [rbx + 0x18]
-jae L
-add rdx, qword ptr [rbx + 0x20]
-cmp cx, word ptr [rdx]
-je L
-mov rax, qword ptr [rdx + 0x10]
-test rax, rax
-je L
-mov edx, dword ptr [rax]
-test edx, edx
-jle L
-mov rax, qword ptr [rax + 8]
-mov rbx, qword ptr [rbp - 8]
-mov rax, qword ptr [rax]
-leave
-ret
-nop
-movzx ecx, word ptr [rsi*8]
-cmp cx, -1
-je L
-movzx edx, cx
-lea rsi, [rdx + rdx*2]
-mov edi, dword ptr [rsi*8 + 8]
-lea rdx, [rsi*8]
-cmp eax, edi
-jb L
-cmp edi, eax
-jb L
-cmp cx, word ptr [rbx + 0x18]
-jae L
-cmp word ptr [rdx], cx
-jne L
-mov rbx, qword ptr [rbp - 8]
-xor eax, eax
-leave
-ret
-nop
-movzx ecx, word ptr [rdi]
-cmp cx, -1
-jne L
-jmp L
-nop
-movzx ecx, word ptr [rdi + 2]
-jmp L
-nop word ptr cs:[rax + rax]
-xor eax, eax
-ret
-nop dword ptr [rax + rax]
-movzx ecx, word ptr [rsi*8 + 2]
-jmp L
```

### изменена: 0x4900410 (101 байт) CDOTA_Modifier_Sniper_Headshot::vfunc#88
было: 0x48fe4d0 (67 байт)
- числа в инструкциях: +0 −0x389 −0x381 −0x391
- поля объектов: +0x1250 +0x1258
- инструкций: 7 → 13
```diff
@@ -1,7 +1,13 @@
-mov qword ptr [rdi + 0xe0], 0x389
+lea rax, [T]
 mov qword ptr [rdi + 0xe8], 0
-mov qword ptr [rdi + 0x130], 0x381
+mov qword ptr [rdi + 0xe0], rax
+lea rax, [T]
+mov qword ptr [rdi + 0x130], rax
+lea rax, [T]
+mov qword ptr [rdi + 0x1ab0], rax
+lea rax, [T]
 mov qword ptr [rdi + 0x138], 0
-mov qword ptr [rdi + 0x1ab0], 0x391
 mov qword ptr [rdi + 0x1ab8], 0
+mov qword ptr [rdi + 0x1250], rax
+mov qword ptr [rdi + 0x1258], 0
 ret
```

### изменена: 0x4934870 (95 байт) CDOTA_Modifier_Sniper_Headshot::vfunc#1
было: 0x4919c70 (25 байт)
- числа в инструкциях: +0x390 +0x3fffffff +0 −0x3a8
- виртуальные вызовы: +0x20 (слот 4)
- поля объектов: +0x1b2c +0x1b18 +0x1b20
- прямых вызовов: 0 → 1
- инструкций: 5 → 23
```diff
@@ -1,5 +1,23 @@
+push rbp
 lea rax, [D]
+mov rbp, rsp
+push rbx
+mov rbx, rdi
+sub rsp, 8
 mov qword ptr [rdi], rax
-add rax, 0x3a8
+add rax, 0x390
+cmp dword ptr [rdi + 0x1b2c], 0x3fffffff
 mov qword ptr [rdi + 0x10], rax
+mov dword ptr [rdi + 0x1b18], 0
+ja L
+mov rsi, qword ptr [rdi + 0x1b20]
+test rsi, rsi
+je L
+mov rax, qword ptr [D]
+mov rdi, qword ptr [rax]
+mov rax, qword ptr [rdi]
+call qword ptr [rax + 0x20]
+mov rdi, rbx
+mov rbx, qword ptr [rbp - 8]
+leave
 jmp F
```

### изменена: 0x4934a80 (103 байт) CDOTA_Modifier_Sniper_Headshot::vfunc#2
было: 0x491c1d0 (50 байт)
- числа в инструкциях: +0x390 +0x3fffffff +0 −0x3a8
- виртуальные вызовы: +0x20 (слот 4)
- поля объектов: +0x1b2c +0x1b18 +0x1b20
- прямых вызовов: 1 → 2
- инструкций: 14 → 25
```diff
@@ -6,6 +6,17 @@
 sub rsp, 8
 mov qword ptr [rdi], rax
-add rax, 0x3a8
+add rax, 0x390
+cmp dword ptr [rdi + 0x1b2c], 0x3fffffff
 mov qword ptr [rdi + 0x10], rax
+mov dword ptr [rdi + 0x1b18], 0
+ja L
+mov rsi, qword ptr [rdi + 0x1b20]
+test rsi, rsi
+je L
+mov rax, qword ptr [D]
+mov rdi, qword ptr [rax]
+mov rax, qword ptr [rdi]
+call qword ptr [rax + 0x20]
+mov rdi, rbx
 call F
 mov rdi, rbx
```

### изменена: 0x4937f70 (123 байт) CModifierFactory<CDOTA_Modifier_Sniper_Headshot>::vfunc#0
было: 0x4936140 (97 байт)
- числа в инструкциях: +0x1b30 +0x1b30 +0 +0 +0x390 −0x1b18 −0x1b18 −0x3a8
- поля объектов: +0x1b18 +0x1b20 +0x1b28 −0x1b12
- инструкций: 25 → 27
```diff
@@ -1,9 +1,9 @@
 push rbp
-mov edi, 0x1b18
+mov edi, 0x1b30
 mov rbp, rsp
 push rbx
 sub rsp, 0x18
 call F
-mov edx, 0x1b18
+mov edx, 0x1b30
 xor esi, esi
 mov rdi, rax
@@ -14,11 +14,13 @@
 call F
 lea rax, [D]
-mov byte ptr [rbx + 0x1b12], 0
+mov qword ptr [rbx + 0x1b18], 0
 mov qword ptr [rbx], rax
-add rax, 0x3a8
+add rax, 0x390
 mov qword ptr [rbx + 0x10], rax
 mov eax, 0xffffffff
 mov word ptr [rbx + 0x1b10], ax
 mov rax, rbx
+mov qword ptr [rbx + 0x1b20], 0
+mov qword ptr [rbx + 0x1b28], 0
 mov rbx, qword ptr [rbp - 8]
 leave
```

### изменена: 0x4981cb0 (460 байт) | строки: "CDOTA_Ability_Ursa_Bear_Down"
было: 0x497fbb0 (452 байт)
- числа в инструкциях: +0x3141593a −0xbb07933e
- прямых вызовов: 10 → 11
- инструкций: 99 → 103
```diff
@@ -56,8 +56,12 @@
 test eax, eax
 je L
-lea rdi, [D]
-mov esi, 0xbb07933e
+lea r14, [S:"CDOTA_Ability_Ursa_Bear_Down"]
+mov esi, 0x3141593a
+mov rdi, r14
 call F
-lea rdi, [D]
+lea rdi, [r14 + 8]
+mov esi, eax
+call F
+lea rdi, [r14 + 0x10]
 mov esi, eax
 call F
@@ -76,5 +80,5 @@
 shr edx, 0xf
 xor eax, edx
-lea rdx, [S:"CDOTA_Ability_Ursa_Bear_Down"]
+mov rdx, r14
 mov dword ptr [rbp - 0x24], eax
 call F
```

### изменена: 0x49d62b0 (519 байт) CDOTA_Modifier_Enchantress_Impetus::vfunc#112 | строки: "modifier_phantom_assassin_stiflingdagger_caster"; "impetus"
было: 0x498c120 (86 байт)
- строки: +"modifier_phantom_assassin_stiflingdagger_caster"
- константы из данных (числа логики): +0.1 +nan +8388608 +1
- числа в инструкциях: +8 +0 +0xffffffff
- виртуальные вызовы: +0x780 (слот 240) +0x880 (слот 272)
- поля объектов: +0xc40 +0x14c8 +0x14c0 +0x7c4 +0xab0 +0x799 +0x9a8 +0xef0
- прямых вызовов: 0 → 14
- инструкций: 20 → 126
```diff
@@ -1,20 +1,126 @@
-mov edx, dword ptr [rdx + 0xc]
-mov rax, rdi
-cmp edx, 0x6a9
+push rbp
+mov rbp, rsp
+push r14
+push r12
+mov r12, rsi
+push rbx
+mov rbx, rdi
+sub rsp, 8
+mov eax, dword ptr [rdx + 0xc]
+cmp eax, 0x6a9
 je L
-jle L
-cmp edx, 0x6de
+jg L
+sub eax, 0x5df
+cmp eax, 2
+jbe L
+mov qword ptr [rbx], 2
+pxor xmm0, xmm0
+movups xmmword ptr [rbx + 8], xmm0
+add rsp, 8
+mov rax, rbx
+pop rbx
+pop r12
+pop r14
+pop rbp
+ret
+nop word ptr cs:[rax + rax]
+cmp eax, 0x6de
+jne L
+mov rdi, r12
+call F
+lea rsi, [S:"modifier_phantom_assassin_stiflingdagger_caster"]
+xor edx, edx
+mov rdi, rax
+call F
+test rax, rax
+jne L
+mov rdi, r12
+call F
+test rax, rax
 je L
-pxor xmm0, xmm0
-mov qword ptr [rax], 2
-movups xmmword ptr [rax + 8], xmm0
-ret
-nop dword ptr [rax + rax]
-sub edx, 0x5df
-cmp edx, 2
+mov rdi, r12
+call F
+lea rdx, [T]
+mov rdi, rax
+mov rax, qword ptr [rax]
+mov rax, qword ptr [rax + 0xc40]
+cmp rax, rdx
+jne L
+mov rax, qword ptr [rdi + 0x14c8]
+or rax, qword ptr [rdi + 0x14c0]
+test al, 8
+jne L
+mov rdi, r12
+call F
+cmp byte ptr [rax + 0x7c4], 0
+jne L
+mov rdi, r12
+call F
+lea rcx, [T]
+mov rdx, qword ptr [rax]
+mov rdx, qword ptr [rdx + 0xab0]
+cmp rdx, rcx
+jne L
+movzx eax, byte ptr [rax + 0x799]
+test al, al
+je L
+mov rdi, r12
+call F
+mov esi, 0xffffffff
+mov rdi, rax
+mov rax, qword ptr [rax]
+call qword ptr [rax + 0x780]
+pxor xmm5, xmm5
+mov rdi, r12
+cvtsi2ss xmm5, eax
+movd r14d, xmm5
+call F
+lea rdx, [T]
+mov rdi, rax
+mov rax, qword ptr [rax]
+mov rax, qword ptr [rax + 0x9a8]
+cmp rax, rdx
+jne L
+movss xmm0, dword ptr [K:0.1]
+addss xmm0, dword ptr [rdi + 0xef0]
+movss xmm2, dword ptr [K:nan]
+movss xmm3, dword ptr [K:8388608]
+movaps xmm1, xmm0
+andps xmm1, xmm2
+ucomiss xmm3, xmm1
+jbe L
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
+movd xmm6, r14d
+comiss xmm6, xmm0
 ja L
-lea rcx, [S:"impetus"]
-mov qword ptr [rax], 2
```
(ещё 24 строк диффа: so-query.py fdiff libclient.so 0x49d62b0)

### изменена: 0x4a14b50 (680 байт) вызывается из: CDOTA_Modifier_Huskar_Berserkers_Blood::vfunc#88 | строки: "modifier_huskar_berserkers_blood_transfusion_debuff"
было: 0x49f2440 (803 байт)
- константы из данных (числа логики): −100 −100 −100 −1 −1.85 −1.85
- прямых вызовов: 22 → 21
- инструкций: 187 → 163
```diff
@@ -66,9 +66,10 @@
 imul eax, dword ptr [r12 + 0x1b04]
 mov rdi, r12
-pxor xmm0, xmm0
-cvtsi2ss xmm0, eax
-divss xmm0, dword ptr [K:100]
-movss dword ptr [rbp - 0x24], xmm0
+pxor xmm2, xmm2
+cvtsi2ss xmm2, eax
+divss xmm2, dword ptr [K:100]
+movss dword ptr [rbp - 0x24], xmm2
 call F
+movss xmm2, dword ptr [rbp - 0x24]
 mov rdi, rax
 mov rax, qword ptr [rax]
@@ -77,39 +78,18 @@
 jne L
 mov eax, dword ptr [rdi + 0x4b8]
-pxor xmm2, xmm2
-cvtsi2ss xmm2, eax
+pxor xmm1, xmm1
+cvtsi2ss xmm1, eax
 mov rdi, r12
 movss dword ptr [rbp - 0x28], xmm2
+movss dword ptr [rbp - 0x24], xmm1
 call F
-movss xmm4, dword ptr [rbp - 0x24]
-pxor xmm1, xmm1
+pxor xmm0, xmm0
 movss xmm2, dword ptr [rbp - 0x28]
-cvtsi2ss xmm1, dword ptr [rax + 0x4bc]
-ucomiss xmm4, xmm2
-jp L
-je L
-movss xmm0, dword ptr [rbp - 0x24]
-subss xmm1, xmm2
-subss xmm0, xmm2
-movss xmm2, dword ptr [K:1]
-divss xmm1, xmm0
-pxor xmm0, xmm0
-cmpltss xmm0, xmm1
-andps xmm1, xmm0
-minss xmm1, xmm2
-movss xmm0, dword ptr [K:100]
-mulss xmm0, xmm1
-pxor xmm1, xmm1
-addss xmm0, xmm1
-movss xmm1, dword ptr [K:1.85]
+mov rdi, r12
+cvtsi2ss xmm0, dword ptr [rax + 0x4bc]
+movss xmm1, dword ptr [rbp - 0x24]
 call F
-movss xmm1, dword ptr [K:1.85]
-movd r13d, xmm0
-movss xmm0, dword ptr [K:100]
-call F
-movd xmm3, r13d
 mov rdi, r12
-divss xmm3, xmm0
-movss dword ptr [rbp - 0x24], xmm3
+movss dword ptr [rbp - 0x24], xmm0
 call F
 test rax, rax
@@ -155,5 +135,5 @@
 movups xmmword ptr [rbx + 8], xmm0
 jmp L
-nop dword ptr [rax]
+nop
 call rax
 test al, al
@@ -167,17 +147,13 @@
 call F
 jmp L
-subss xmm1, xmm4
-pxor xmm0, xmm0
-movss xmm7, dword ptr [K:100]
-cmpless xmm0, xmm1
-andps xmm0, xmm7
-jmp L
-movss xmm7, dword ptr [rbp - 0x24]
+movss xmm5, dword ptr [rbp - 0x24]
 pxor xmm0, xmm0
 mov dword ptr [rbx], 1
 movups xmmword ptr [rbx + 8], xmm0
-movss dword ptr [rbx + 4], xmm7
+movss dword ptr [rbx + 4], xmm5
 jmp L
+movss dword ptr [rbp - 0x24], xmm2
 call rax
+movss xmm2, dword ptr [rbp - 0x24]
 jmp L
 call rax
```

### изменена: 0x4b8df80 (45 байт) CDOTA_Modifier_Meepo_Fling_Held::CheckState
было: 0x4b8bcc0 (37 байт)
- числа в инструкциях: +0x2000804022 +0xffffffdfff7fbfdd −0x800022 −0xffffffffff7fffdd
- инструкций: 9 → 9
```diff
@@ -1,8 +1,8 @@
-mov rax, qword ptr [rsi]
-or rax, 0x800022
+movabs rax, 0x2000804022
+or rax, qword ptr [rsi]
+movabs rdx, 0xffffffdfff7fbfdd
+and rdx, qword ptr [rsi + 8]
 movq xmm0, rax
-mov rax, qword ptr [rsi + 8]
-and rax, 0xffffffffff7fffdd
-movq xmm1, rax
+movq xmm1, rdx
 punpcklqdq xmm0, xmm1
 movups xmmword ptr [rsi], xmm0
```

### изменена: 0x5e2da90 (1088 байт) вызывается из: C_DOTA_Unit_Hero_Rubick::vfunc#538, CDOTA_ParticleManager::vfunc#9, CDOTAGCClientSystem::vfunc#1
было: 0x5e2b880 (976 байт)
- прямых вызовов: 10 → 14
- инструкций: 239 → 272
```diff
@@ -1,2 +1,35 @@
+push rbp
+mov rbp, rsp
+push r12
+push rbx
+movzx eax, byte ptr [D]
+lea rbx, [D]
+test al, al
+je L
+mov rax, rbx
+pop rbx
+pop r12
+pop rbp
+ret
+nop dword ptr [rax]
+lea r12, [D]
+lea rbx, [D]
+mov rdi, r12
+call F
+test eax, eax
+je L
+mov rdi, rbx
+call F
+lea rdx, [D]
+mov rsi, rbx
+lea rdi, [T]
+call F
+mov rdi, r12
+call F
+mov rax, rbx
+pop rbx
+pop r12
+pop rbp
+ret
 test rsi, rsi
 je L
```

### изменена: 0x4900e80 (76 байт) CDOTA_Modifier_TemplarAssassin_Meld_Animation::vfunc#88
- код тот же, но вызывает другую функцию: было 0x4923c60, стало 0x4925be0

### изменена: 0x4900ff0 (176 байт) CDOTA_Modifier_TemplarAssassin_Meld::vfunc#88
- код тот же, но вызывает другую функцию: было 0x4923ca0, стало 0x4925c20

### изменена: 0x4901380 (169 байт) CDOTA_Modifier_TemplarAssassin_Trap::vfunc#88
- код тот же, но вызывает другую функцию: было 0x4923d40, стало 0x4925cc0

### изменена: 0x49018e0 (219 байт) CDOTA_Modifier_TemplarAssassin_Meditation_Illusion::vfunc#88
- код тот же, но вызывает другую функцию: было 0x4923d60, стало 0x4925ce0

### изменена: 0x4901a30 (126 байт) CDOTA_Modifier_TemplarAssassin_InnerPeace_Passive::vfunc#88
- код тот же, но вызывает другую функцию: было 0x4923da0, стало 0x4925d20

### изменена: 0x4902530 (101 байт) CDOTA_Modifier_Ursa_Overpower::vfunc#88
- код тот же, но вызывает другую функцию: было 0x4923dc0, стало 0x4925d40

### изменена: 0x4902670 (26 байт) CDOTA_Modifier_Ursa_Fury_Swipes::vfunc#88
- код тот же, но вызывает другую функцию: было 0x4923de0, стало 0x4925d60

### изменена: 0x4902c60 (126 байт) CDOTA_Modifier_Venomancer_Plague_Carrier::vfunc#88
- код тот же, но вызывает другую функцию: было 0x4923e20, стало 0x4925da0

### изменена: 0x4902da0 (70 байт) CDOTA_Modifier_Venomancer_VenomousGale::vfunc#88
- код тот же, но вызывает другую функцию: было 0x4923e60, стало 0x4925de0

### изменена: 0x4903450 (51 байт) CDOTA_Modifier_Venomancer_NoxiousPlagueContagious::vfunc#88
- код тот же, но вызывает другую функцию: было 0x4923e80, стало 0x4925e00

### изменена: 0x4903740 (126 байт) CDOTA_Modifier_Viper_PoisonAttack::vfunc#88
- код тот же, но вызывает другую функцию: было 0x4923ee0, стало 0x4925e60

### изменена: 0x4903d50 (76 байт) CDOTA_Modifier_Viper_ViperStrike_Slow::vfunc#88
- код тот же, но вызывает другую функцию: было 0x4923f60, стало 0x4925ee0

### изменена: 0x4904020 (51 байт) CDOTA_Modifier_Viper_Predator::vfunc#88
- код тот же, но вызывает другую функцию: было 0x4923f80, стало 0x4925f00

### изменена: 0x4904150 (76 байт) CDOTA_Modifier_Warlock_FatalBonds::vfunc#88
- код тот же, но вызывает другую функцию: было 0x4923fa0, стало 0x4925f20

### изменена: 0x4904520 (101 байт) CDOTA_Modifier_Warlock_Rain_Of_Chaos_Golem::vfunc#88
- код тот же, но вызывает другую функцию: было 0x4923fe0, стало 0x4925f60

### изменена: 0x4904770 (76 байт) CDOTA_Modifier_Warlock_Golem_Permanent_Immolation::vfunc#88
- код тот же, но вызывает другую функцию: было 0x4924020, стало 0x4925fa0

### изменена: 0x4904d10 (226 байт) CDOTA_Modifier_WitchDoctor_DeathWard::vfunc#88
- код тот же, но вызывает другую функцию: было 0x49240a0, стало 0x4926020

### изменена: 0x4905160 (26 байт) CDOTA_Modifier_Item_GrisGris::vfunc#88
- код тот же, но вызывает другую функцию: было 0x4924160, стало 0x49260e0

### изменена: 0x49052d0 (44 байт) CDOTA_Modifier_Miniboss_InherentBuffs::vfunc#88
- код тот же, но вызывает другую функцию: было 0x4924180, стало 0x4926100

### изменена: 0x49054b0 (126 байт) CDOTA_Modifier_Miniboss_UnyieldingShield::vfunc#88
- код тот же, но вызывает другую функцию: было 0x49241c0, стало 0x4926140

### изменена: 0x49059b0 (26 байт) CDOTA_Modifier_Miniboss_Minion_Deflecting_Shield_Aura::vfunc#88
- код тот же, но вызывает другую функцию: было 0x4924220, стало 0x49261a0

### изменена: 0x4905ba0 (51 байт) CDOTA_Modifier_Miniboss_Team_Unreliable_Gold_Tracker_Thinker::vfunc#88
- код тот же, но вызывает другую функцию: было 0x4924260, стало 0x49261e0

### изменена: 0x4907870 (157 байт) CDOTA_Modifier_Roshan_InherentBuffs::vfunc#88
- код тот же, но вызывает другую функцию: было 0x4924340, стало 0x49262c0

### изменена: 0x4900910 (26 байт) CDOTA_Modifier_Sniper_Assassinate_Trigger::vfunc#88
- код тот же, но вызывает другую функцию: было 0x48fe520, стало 0x4925bc0

### изменена: 0x49034e0 (26 байт) CDOTA_Modifier_Venomancer_Snakebite::vfunc#88
- код тот же, но вызывает другую функцию: было 0x4923ec0, стало 0x4925e40

### изменена: 0x49035d0 (26 байт) CDOTA_Modifier_Venomancer_WardCounter::vfunc#88
- код тот же, но вызывает другую функцию: было 0x4923e00, стало 0x4925d80

### изменена: 0x4904470 (26 байт) CDOTA_Modifier_Warlock_Rain_Of_Chaos_Death_Trigger::vfunc#88
- код тот же, но вызывает другую функцию: было 0x4923fc0, стало 0x4925f40

### изменена: 0x4904690 (26 байт) CDOTA_Modifier_Warlock_Golem_Flaming_Fists::vfunc#88
- код тот же, но вызывает другую функцию: было 0x4924000, стало 0x4925f80

### изменена: 0x49048c0 (26 байт) CDOTA_Modifier_Warlock_Imp_AutoAttack::vfunc#88
- код тот же, но вызывает другую функцию: было 0x4924040, стало 0x4925fc0

### изменена: 0x49049a0 (26 байт) CDOTA_Modifier_Warlock_EldritchSummoning::vfunc#88
- код тот же, но вызывает другую функцию: было 0x4924060, стало 0x4925fe0

### изменена: 0x49053d0 (51 байт) CDOTA_Modifier_Miniboss_Reflect::vfunc#88
- код тот же, но вызывает другую функцию: было 0x49241a0, стало 0x4926120

### изменена: 0x49055e0 (26 байт) CDOTA_Modifier_Miniboss_Radiance::vfunc#88
- код тот же, но вызывает другую функцию: было 0x49241e0, стало 0x4926160

### изменена: 0x49056d0 (26 байт) CDOTA_Modifier_Miniboss_Alleviation::vfunc#88
- код тот же, но вызывает другую функцию: было 0x4924200, стало 0x4926180

### изменена: 0x4905a10 (51 байт) CDOTA_Modifier_Miniboss_Minion_Deflecting_Shield_Buff::vfunc#88
- код тот же, но вызывает другую функцию: было 0x4924240, стало 0x49261c0

### изменена: 0x4905f00 (26 байт) CDOTA_Modifier_Nian_Frenzy::vfunc#88
- код тот же, но вызывает другую функцию: было 0x49242a0, стало 0x4926220

### изменена: 0x49065e0 (26 байт) CDOTA_Modifier_Nian_GreaterBash::vfunc#88
- код тот же, но вызывает другую функцию: было 0x49242c0, стало 0x4926240

### изменена: 0x4906700 (51 байт) CDOTA_Modifier_NianCharge::vfunc#88
- код тот же, но вызывает другую функцию: было 0x49242e0, стало 0x4926260

### изменена: 0x4907330 (76 байт) CDOTA_Modifier_Roshan_Grab::vfunc#88
- код тот же, но вызывает другую функцию: было 0x4924320, стало 0x49262a0

### добавлена: 0x4755730 (749 байт)

### добавлена: 0x4755a20 (36 байт) | строки: "GetModifierAttackWhileMovingTarget"

### добавлена: 0x4755a50 (36 байт) | строки: "GetModifierSpellRedirectTarget"

### добавлена: 0x475a240 (36 байт) | строки: "GetModifierPreAttack_BonusDamage_Proc"

### добавлена: 0x475a270 (36 байт) | строки: "GetModifierProcAttack_ConvertPhysicalToMagical"

### добавлена: 0x475a2a0 (36 байт) | строки: "GetModifierProcAttack_BonusDamage_Magical_Target"

### добавлена: 0x475a2d0 (36 байт) | строки: "GetModifierHealthcostReduction_Constant"

### добавлена: 0x475a300 (36 байт) | строки: "GetModifierBaseAttackTimeConstant_Adjust"

### добавлена: 0x475a330 (36 байт) | строки: "GetModifierBaseAttackTimePercentage"

### добавлена: 0x475a360 (36 байт) | строки: "GetModifierBonusDamageOutgoing_Percentage"

### добавлена: 0x475a390 (36 байт) | строки: "GetModifierDamageOutgoing_Percentage_Illusion_Amplify"

### добавлена: 0x475a3c0 (36 байт) | строки: "GetModifierSpellAmplify_PercentageTarget"

### добавлена: 0x475a3f0 (36 байт) | строки: "GetModifierManaDrainAmplify_Percentage"

### добавлена: 0x475a420 (36 байт) | строки: "GetModifierPhysicalArmorTotal_Percentage"

### добавлена: 0x475a450 (36 байт) | строки: "GetModifierPhysicalArmorBonusPost"

### добавлена: 0x475a480 (36 байт) | строки: "GetModifierMinPhysicalArmor"

### добавлена: 0x475a4b0 (36 байт) | строки: "GetModifierMagicalResistanceBaseReduction"

### добавлена: 0x475a4e0 (36 байт) | строки: "GetModifierMagicalResistanceBonusIllusions"

### добавлена: 0x475a510 (36 байт) | строки: "GetModifierMagicalResistanceBonusUnique"

### добавлена: 0x475a540 (36 байт) | строки: "GetModifierExtraManaBonusPercentage"

### добавлена: 0x475a570 (36 байт) | строки: "GetModifierBonusStats_Strength_Percentage"

### добавлена: 0x475a5a0 (36 байт) | строки: "GetModifierBonusStats_Agility_Percentage"

### добавлена: 0x475a5d0 (36 байт) | строки: "GetModifierBonusStats_Intellect_Percentage"

### добавлена: 0x475a600 (36 байт) | строки: "GetModifierIntellectNone"

### добавлена: 0x475a630 (36 байт) | строки: "GetModifierCastRangeBonusPercentage"

### добавлена: 0x475a660 (36 байт) | строки: "GetModifierProjectileSpeedBonusPercentage"

### добавлена: 0x475a690 (36 байт) | строки: "GetModifierPercentageCooldownOngoing"

### добавлена: 0x475a6c0 (36 байт) | строки: "GetModifierConstantCasttime"

### добавлена: 0x475a6f0 (36 байт) | строки: "GetModifierPercentageAttackAnimTime"

### добавлена: 0x475a720 (36 байт) | строки: "GetModifierPercentageConvertExpToGold"

### добавлена: 0x475a750 (36 байт) | строки: "GetModifierPhysical_ConstantBlockBonus"

### добавлена: 0x475a780 (36 байт) | строки: "GetModifierInnateDamageBlockPctOverride"

### добавлена: 0x475a7b0 (36 байт) | строки: "GetModifierStrongIllusion"

### добавлена: 0x475a7e0 (36 байт) | строки: "GetModifierSuperIllusion"

### добавлена: 0x475a810 (36 байт) | строки: "GetModifierXPDuringDeath"

### добавлена: 0x475a840 (36 байт) | строки: "GetDisableManaGain"

### добавлена: 0x475a870 (36 байт) | строки: "GetAllowEtherealAttack"

### добавлена: 0x475a8a0 (36 байт) | строки: "GetTriggerCosmeticAndEndAttack"

### добавлена: 0x475a8d0 (36 байт) | строки: "GetAlwaysAutoAttackWhileHoldPosition"

### добавлена: 0x475a900 (36 байт) | строки: "GetPhysicalArmorPiercingPercentageTarget"

### добавлена: 0x475a930 (36 байт) | строки: "GetMagicalArmorPiercingPercentageTarget"

### добавлена: 0x475a960 (36 байт) | строки: "GetCriticalStrikeBonus"

### добавлена: 0x475a990 (36 байт) | строки: "GetConvertAttackPhysicalToPure"

### добавлена: 0x475a9c0 (36 байт) | строки: "GetBuffAmplification"

### добавлена: 0x475a9f0 (36 байт) | строки: "OnOrderReceived"

### добавлена: 0x475aa20 (36 байт) | строки: "OnSpentItemCharge"

### добавлена: 0x475aa50 (36 байт) | строки: "OnRedirectHealthGain"

### добавлена: 0x475aa80 (36 байт) | строки: "OnModifierRemoved"

### добавлена: 0x475aab0 (36 байт) | строки: "OnScepterUpgradeSelected"

### добавлена: 0x475aae0 (36 байт) | строки: "OnShardUpgradeSelected"

### добавлена: 0x475ab10 (36 байт) | строки: "GetModifierShard"

### добавлена: 0x475ab40 (36 байт) | строки: "GetModifierRadarCooldownReduction"

### добавлена: 0x475ab70 (36 байт) | строки: "GetModifierIgnoreCooldown"

### добавлена: 0x475aba0 (36 байт) | строки: "GetModifierIncomingDamageIllusion"

### добавлена: 0x475abd0 (36 байт) | строки: "GetSuppressCleave"

### добавлена: 0x475ac00 (36 байт) | строки: "GetModifierTurnRateConstant"

### добавлена: 0x475ac30 (36 байт) | строки: "GetModifierPhysicalDamageOutgoing_Percentage"

### добавлена: 0x475ac60 (36 байт) | строки: "GetModifierKnockbackAmplification_Percentage"

### добавлена: 0x475ac90 (36 байт) | строки: "GetModifierPropertyFailAttack"

### добавлена: 0x475acc0 (36 байт) | строки: "GetModifierPrereduceIncomingDamage_Mult"

### добавлена: 0x475acf0 (36 байт) | строки: "GetModifierIncomingDamageConstantPost"

### добавлена: 0x475ad20 (36 байт) | строки: "GetModifierDamageOutgoing_PercentageMultiplicative"

### добавлена: 0x475ad50 (36 байт) | строки: "GetModifierTickGold_Multiplier"

### добавлена: 0x475ad80 (36 байт) | строки: "GetModifierSlowResistance_Unique"

### добавлена: 0x475adb0 (36 байт) | строки: "GetModifierSlowResistanceAppliesToAttacks"

### добавлена: 0x475ade0 (36 байт) | строки: "GetModifierAoEBonusPercentage"

### добавлена: 0x475ae10 (36 байт) | строки: "GetModifierProjectileSpeed"

### добавлена: 0x475ae40 (36 байт) | строки: "GetModifierProjectileSpeedTarget"

### добавлена: 0x475ae70 (36 байт) | строки: "GetModifierBecomeStrength"

### добавлена: 0x475aea0 (36 байт) | строки: "GetModifierBecomeAgility"

### добавлена: 0x475aed0 (36 байт) | строки: "GetModifierBecomeIntelligence"

### добавлена: 0x475af00 (36 байт) | строки: "GetModifierBecomeUniversal"

### добавлена: 0x475af30 (36 байт) | строки: "OnForceProcMagicStick"

### добавлена: 0x475af60 (36 байт) | строки: "GetModifierForceMaxHealth"

### добавлена: 0x475af90 (36 байт) | строки: "GetModifierForceMaxMana"

### добавлена: 0x475afc0 (36 байт) | строки: "GetModifierAoEBonusConstant"

### добавлена: 0x475aff0 (36 байт) | строки: "OnTakeDamagePostUnavoidableBlock"

### добавлена: 0x475b020 (36 байт) | строки: "OnMuteDamageAbilities"

### добавлена: 0x475b050 (36 байт) | строки: "GetSuppressCrit"

### добавлена: 0x475b080 (36 байт) | строки: "GetModifierAbilityPoints"

### добавлена: 0x475b0b0 (36 байт) | строки: "GetModifierBuybackPenaltyPercent"

### добавлена: 0x475b0e0 (36 байт) | строки: "GetModifierReplaceAttack"

### добавлена: 0x475b110 (36 байт) | строки: "GetModifierPropertyIgnoreForceTarget"

### добавлена: 0x475b140 (36 байт) | строки: "OnTreePlanted"

### добавлена: 0x475b170 (36 байт) | строки: "OnDamageHPLossSelf"

### добавлена: 0x475b1a0 (36 байт) | строки: "GetModifierHeroKillBountyBonus"

### добавлена: 0x475b1d0 (36 байт) | строки: "GetModifierPropertyAttackPotency"

### добавлена: 0x475b200 (36 байт) | строки: "GetModifierHealthDrainConstant"

### добавлена: 0x475b230 (36 байт) | строки: "GetModifierHealthDrainPercentage"

### добавлена: 0x475b260 (36 байт) | строки: "GetModifierHealthBarPipsFragile"

### добавлена: 0x4939020 (218 байт) | строки: "AttackRecord_t"; "CUtlVector"

### добавлена: 0x4a13c80 (3782 байт)

### добавлена: 0x4aaa8d0 (74880 байт)

### удалена: 0x473f310 (44 байт) вызывается из: CDOTA_Modifier_Lua::DeclareFunctions

### удалена: 0x49302b0 (111 байт) | строки: "AttackRecord_t"

### удалена: 0x4aa85d0 (23760 байт)

### удалена: 0x4aae2c0 (51120 байт)

### копии существующего кода (12): шаблонные / склеенные компоновщиком функции, такой же код есть и в другой сборке — не новый код
- ещё одна копия существующего кода: 0x4745120 (83 байт)
- ещё одна копия существующего кода: 0x474f130 (961 байт) | строки: "%g %g %g"; "(null)"; "%g %g %g %g"; "unknown_variant_type"; "%lld"; "%llu"; "%d %d %d %d"; "false"
- ещё одна копия существующего кода: 0x48deb80 (242 байт)
- ещё одна копия существующего кода: 0x4926260 (19 байт) вызывается из: CDOTA_Modifier_NianCharge::vfunc#88
- ещё одна копия существующего кода: 0x4926280 (19 байт) вызывается из: CDOTA_Modifier_NianCharge::vfunc#88
- ещё одна копия существующего кода: 0x49262a0 (19 байт) вызывается из: CDOTA_Modifier_Roshan_Grab::vfunc#88
- ещё одна копия существующего кода: 0x49262c0 (19 байт) вызывается из: CDOTA_Modifier_Roshan_InherentBuffs::vfunc#88
- ещё одна копия существующего кода: 0x4a14e00 (2420 байт)
- одной копией существующего кода меньше: 0x47450c0 (83 байт)
- одной копией существующего кода меньше: 0x474eec0 (653 байт) | строки: "%g %g %g"; "(null)"; "%g %g %g %g"; "%lld"; "%llu"; "%d %d %d %d"; "false"; "true"
- одной копией существующего кода меньше: 0x4a11d00 (6020 байт)
- одной копией существующего кода меньше: 0x5e2b7f0 (112 байт) вызывается из: C_DOTA_Unit_Hero_Rubick::vfunc#538, CDOTA_ParticleManager::vfunc#9, CDOTAGCClientSystem::vfunc#1

## libserver.so: функций 221833 → 221929; без изменений 221506, изменено 147, добавлено 102, удалено 6

### изменена: 0x3be2f40 (507 байт)
было: 0x3be2ec0 (507 байт)
- строки: −"\\\tQ"
- инструкций: 133 → 133
```diff
@@ -12,5 +12,5 @@
 cmp al, 0x24
 ja L
-lea rcx, [S:"\\\tQ"]
+lea rcx, [D]
 movzx eax, al
 movsxd rax, dword ptr [rcx + rax*4]
```

### изменена: 0x3bf74c0 (808 байт) вызывается из: CDOTA_NPCSpawnerGoodTop::vfunc#22, CDOTA_Ability_Lua::GetIntrinsicModifierName, CDOTA_Ability_Lua::GetAssociatedPrimaryAbilities | строки: "%g %g %g"; "%g %g %g %g"; "(null)"; "false"; "true"; "%llu"; "%lld"; "%g %g"
было: 0x3bf7440 (808 байт)
- строки: −"Y:R"
- инструкций: 203 → 203
```diff
@@ -36,5 +36,5 @@
 cmp al, 0x4f
 ja L
-lea rcx, [S:"Y:R"]
+lea rcx, [D]
 movzx edx, al
 movsxd rdx, dword ptr [rcx + rdx*4]
```

### изменена: 0x3bf8f20 (238 байт) | строки: "_TR"
было: 0x3bf8ea0 (238 байт)
- строки: +"_TR"
- инструкций: 65 → 65
```diff
@@ -2,5 +2,5 @@
 ja L
 push rbp
-lea rdx, [D]
+lea rdx, [S:"_TR"]
 mov edi, edi
 mov rbp, rsp
```

### изменена: 0x3bfabc0 (323 байт) | строки: "LpR"; "CUtlSymbolLarge"; "CNetworkUtlVectorBase"
было: 0x3bfab40 (323 байт)
- строки: +"LpR"
- инструкций: 99 → 99
```diff
@@ -2,5 +2,5 @@
 ja L
 push rbp
-lea rdx, [D]
+lea rdx, [S:"LpR"]
 mov edi, edi
 mov rbp, rsp
```

### изменена: 0x3bfad70 (317 байт) | строки: "hrR"
было: 0x3bfacf0 (317 байт)
- строки: +"hrR"
- инструкций: 98 → 98
```diff
@@ -7,5 +7,5 @@
 push rbx
 ja L
-lea rdx, [D]
+lea rdx, [S:"hrR"]
 mov edi, edi
 mov rbx, rsi
```

### изменена: 0x3c0cfa0 (263 байт)
было: 0x3c0cf20 (263 байт)
- строки: −"G~S"
- инструкций: 64 → 64
```diff
@@ -2,5 +2,5 @@
 ja L
 push rbp
-lea rdx, [S:"G~S"]
+lea rdx, [D]
 mov edi, edi
 mov rbp, rsp
```

### изменена: 0x3c275a0 (1047 байт) | строки: "Unsupported KV3 basic type '%s' (%d)!"; "Pointers cannot be used as numeric values"
было: 0x3c27520 (1047 байт)
- строки: −"7\"U"
- инструкций: 245 → 245
```diff
@@ -47,5 +47,5 @@
 cmp r8b, 6
 ja L
-lea rcx, [S:"7\"U"]
+lea rcx, [D]
 movzx edx, r8b
 movsxd rdx, dword ptr [rcx + rdx*4]
```

### изменена: 0x3c279c0 (1047 байт) | строки: "Unsupported KV3 basic type '%s' (%d)!"; "Pointers cannot be used as numeric values"
было: 0x3c27940 (1047 байт)
- строки: −";&U"
- инструкций: 245 → 245
```diff
@@ -47,5 +47,5 @@
 cmp r8b, 6
 ja L
-lea rcx, [S:";&U"]
+lea rcx, [D]
 movzx edx, r8b
 movsxd rdx, dword ptr [rcx + rdx*4]
```

### изменена: 0x3c27de0 (1047 байт) | строки: "Unsupported KV3 basic type '%s' (%d)!"; "Pointers cannot be used as numeric values"
было: 0x3c27d60 (1047 байт)
- строки: −"?*U"
- инструкций: 245 → 245
```diff
@@ -47,5 +47,5 @@
 cmp r8b, 6
 ja L
-lea rcx, [S:"?*U"]
+lea rcx, [D]
 movzx edx, r8b
 movsxd rdx, dword ptr [rcx + rdx*4]
```

### изменена: 0x3c28200 (1047 байт) | строки: "Unsupported KV3 basic type '%s' (%d)!"; "Pointers cannot be used as numeric values"
было: 0x3c28180 (1047 байт)
- строки: −"C.U"
- инструкций: 245 → 245
```diff
@@ -47,5 +47,5 @@
 cmp r8b, 6
 ja L
-lea rcx, [S:"C.U"]
+lea rcx, [D]
 movzx edx, r8b
 movsxd rdx, dword ptr [rcx + rdx*4]
```

### изменена: 0x3c28620 (1047 байт) | строки: "Unsupported KV3 basic type '%s' (%d)!"; "Pointers cannot be used as numeric values"
было: 0x3c285a0 (1047 байт)
- строки: −"G2U"
- инструкций: 245 → 245
```diff
@@ -47,5 +47,5 @@
 cmp r8b, 6
 ja L
-lea rcx, [S:"G2U"]
+lea rcx, [D]
 movzx edx, r8b
 movsxd rdx, dword ptr [rcx + rdx*4]
```

### изменена: 0x3c28a40 (1047 байт) | строки: "Unsupported KV3 basic type '%s' (%d)!"; "Pointers cannot be used as numeric values"
было: 0x3c289c0 (1047 байт)
- строки: −"K6U"
- инструкций: 245 → 245
```diff
@@ -47,5 +47,5 @@
 cmp r8b, 6
 ja L
-lea rcx, [S:"K6U"]
+lea rcx, [D]
 movzx edx, r8b
 movsxd rdx, dword ptr [rcx + rdx*4]
```

### изменена: 0x3c297c0 (1047 байт) | строки: "oDU"; "Unsupported KV3 basic type '%s' (%d)!"; "Pointers cannot be used as numeric values"
было: 0x3c29740 (1047 байт)
- строки: +"oDU"
- инструкций: 245 → 245
```diff
@@ -47,5 +47,5 @@
 cmp r8b, 6
 ja L
-lea rcx, [D]
+lea rcx, [S:"oDU"]
 movzx edx, r8b
 movsxd rdx, dword ptr [rcx + rdx*4]
```

### изменена: 0x3c29be0 (1047 байт) | строки: "sHU"; "Unsupported KV3 basic type '%s' (%d)!"; "Pointers cannot be used as numeric values"
было: 0x3c29b60 (1047 байт)
- строки: +"sHU"
- инструкций: 245 → 245
```diff
@@ -47,5 +47,5 @@
 cmp r8b, 6
 ja L
-lea rcx, [D]
+lea rcx, [S:"sHU"]
 movzx edx, r8b
 movsxd rdx, dword ptr [rcx + rdx*4]
```

### изменена: 0x3c2b4f0 (951 байт) | строки: "IKV3TransferInterface_GameTime_Load"; "NdU"
было: 0x3c2b470 (951 байт)
- строки: +"NdU"
- инструкций: 235 → 235
```diff
@@ -63,5 +63,5 @@
 cmp al, 6
 ja L
-lea rdx, [D]
+lea rdx, [S:"NdU"]
 movzx eax, al
 movsxd rax, dword ptr [rdx + rax*4]
```

### изменена: 0x3c6a3a0 (715 байт) CDOTA_NPCSpawnerGoodTop::vfunc#51, CDOTA_NPCSpawnerGoodMid::vfunc#51, CDOTA_NPCSpawnerGoodBot::vfunc#51 | строки: "disableshadows"; "disablereceiveshadows"; "ownername"
было: 0x3c6a320 (715 байт)
- строки: −"7,Y" −"O,Y"
- инструкций: 189 → 189
```diff
@@ -25,5 +25,5 @@
 cmp dl, 6
 ja L
-lea rcx, [S:"7,Y"]
+lea rcx, [D]
 movzx edx, dl
 movsxd rdx, dword ptr [rcx + rdx*4]
@@ -126,5 +126,5 @@
 cmp dl, 6
 ja L
-lea rcx, [S:"O,Y"]
+lea rcx, [D]
 movzx edx, dl
 movsxd rdx, dword ptr [rcx + rdx*4]
```

### изменена: 0x3c6d180 (1027 байт) | строки: "lZY"; "CEntityIOOutput"; "CBaseFilter"; "CHandle"
было: 0x3c6d100 (1027 байт)
- строки: +"lZY"
- инструкций: 172 → 172
```diff
@@ -2,5 +2,5 @@
 ja L
 push rbp
-lea rdx, [D]
+lea rdx, [S:"lZY"]
 mov edi, edi
 mov rbp, rsp
```

### изменена: 0x3c6e4a0 (653 байт) | строки: "AnY"; "%g %g %g"; "(null)"; "%g %g %g %g"; "%lld"; "%llu"; "%d %d %d %d"; "false"
было: 0x3c6e420 (653 байт)
- строки: +"AnY"
- инструкций: 159 → 159
```diff
@@ -7,5 +7,5 @@
 cmp al, 0x4f
 ja L
-lea rcx, [D]
+lea rcx, [S:"AnY"]
 movzx edx, al
 movsxd rdx, dword ptr [rcx + rdx*4]
```

### изменена: 0x3c8a6d0 (478 байт)
было: 0x3c8a650 (478 байт)
- строки: −".,["
- инструкций: 116 → 116
```diff
@@ -8,5 +8,5 @@
 cmp dil, 0x4f
 ja L
-lea rdx, [S:".,["]
+lea rdx, [D]
 movzx eax, dil
 movsxd rax, dword ptr [rdx + rax*4]
```

### изменена: 0x3cc0050 (2479 байт) CBaseLightProbeVolume::vfunc#2 | строки: "box_mins"; "box_maxs"; "moveable"; "handshake"; "indoor_outdoor_level"; "StartDisabled"; "is_selected_in_hammer"; "voxel_size"
было: 0x3cbffd0 (2479 байт)
- строки: +"rm^" +"{m^" +"mm^" +"Xm^" +".m^" −"@m^" −"nl^"
- инструкций: 618 → 618
```diff
@@ -71,5 +71,5 @@
 cmp dl, 6
 ja L
-lea rcx, [S:"@m^"]
+lea rcx, [D]
 movzx edx, dl
 movsxd rdx, dword ptr [rcx + rdx*4]
@@ -231,5 +231,5 @@
 cmp dl, 6
 ja L
-lea rcx, [D]
+lea rcx, [S:"rm^"]
 movzx edx, dl
 movsxd rdx, dword ptr [rcx + rdx*4]
@@ -259,5 +259,5 @@
 cmp dl, 6
 ja L
-lea rcx, [D]
+lea rcx, [S:"{m^"]
 movzx edx, dl
 movsxd rdx, dword ptr [rcx + rdx*4]
@@ -287,5 +287,5 @@
 cmp dl, 6
 ja L
-lea rcx, [D]
+lea rcx, [S:"mm^"]
 movzx edx, dl
 movsxd rdx, dword ptr [rcx + rdx*4]
@@ -315,5 +315,5 @@
 cmp dl, 6
 ja L
-lea rcx, [D]
+lea rcx, [S:"Xm^"]
 movzx edx, dl
```
(ещё 8 строк диффа: so-query.py fdiff libserver.so 0x3cc0050)

### изменена: 0x3d22c60 (1712 байт) CEntityOutputTemplate<SndOpEventGuid_t>::vfunc#2 | строки: "m_Value"; "Stack depth limit hit (%d)"; "pPd"; "1Pd"; "public.aabb_min"; "public.aabb_max"
было: 0x3d22be0 (1712 байт)
- строки: +"pPd" +"1Pd" −"qOd"
- инструкций: 409 → 409
```diff
@@ -65,5 +65,5 @@
 cmp al, 6
 ja L
-lea rdx, [D]
+lea rdx, [S:"pPd"]
 movzx eax, al
 movsxd rax, dword ptr [rdx + rax*4]
@@ -90,5 +90,5 @@
 cmp al, 6
 ja L
-lea rdx, [S:"qOd"]
+lea rdx, [S:"1Pd"]
 movzx eax, al
 movsxd rax, dword ptr [rdx + rax*4]
```

### изменена: 0x3d302a0 (637 байт) | строки: "\\$e"; "CInfoFan"; "CHandle"; "VectorWS"
было: 0x3d30220 (637 байт)
- строки: +"\\$e"
- инструкций: 147 → 147
```diff
@@ -7,5 +7,5 @@
 cmp edi, 6
 ja L
-lea rdx, [D]
+lea rdx, [S:"\\$e"]
 mov edi, edi
 mov rbx, rsi
```

### изменена: 0x3d30720 (547 байт) | строки: "8'e"; "CHandle"; "CBasePlayerController"; "CNetworkUtlVectorBase"; "CBasePlayerPawn"
было: 0x3d306a0 (547 байт)
- строки: +"8'e" −"x&e"
- инструкций: 158 → 158
```diff
@@ -2,5 +2,5 @@
 ja L
 push rbp
-lea rdx, [S:"x&e"]
+lea rdx, [S:"8'e"]
 mov edi, edi
 mov rbp, rsp
```

### изменена: 0x3d519c0 (117 байт) | строки: "9 g"
было: 0x3d51940 (117 байт)
- строки: +"9 g"
- инструкций: 39 → 39
```diff
@@ -2,5 +2,5 @@
 cmp edx, 6
 ja L
-lea rcx, [D]
+lea rcx, [S:"9 g"]
 push rbp
 mov rdi, rsi
```

### изменена: 0x3d51a40 (561 байт) | строки: "c g"; "Unsupported KV3 basic type '%s' (%d)!"; "Pointers cannot be used as numeric values"
было: 0x3d519c0 (561 байт)
- строки: +"c g"
- инструкций: 151 → 151
```diff
@@ -11,5 +11,5 @@
 cmp r8b, 6
 ja L
-lea rdx, [D]
+lea rdx, [S:"c g"]
 movzx eax, r8b
 movsxd rax, dword ptr [rdx + rax*4]
```

### изменена: 0x3d51d40 (227 байт) | строки: "X#g"; "IPhysicsJoint"
было: 0x3d51cc0 (227 байт)
- строки: +"X#g"
- инструкций: 73 → 73
```diff
@@ -1,5 +1,5 @@
 cmp edi, 6
 ja L
-lea rcx, [D]
+lea rcx, [S:"X#g"]
 mov edi, edi
 push rbp
```

### изменена: 0x3d52860 (339 байт) | строки: "VPhysicsCollisionAttribute_t"; "SolidType_t"; "SurroundingBoundsType_t"
было: 0x3d527e0 (339 байт)
- строки: −"D-g"
- инструкций: 99 → 99
```diff
@@ -2,5 +2,5 @@
 ja L
 push rbp
-lea rdx, [S:"D-g"]
+lea rdx, [D]
 mov edi, edi
 mov rbp, rsp
```

### изменена: 0x3d52a80 (499 байт) | строки: "GameTime_t"; "BeamType_t"; "CBaseEntity"; "CHandle"; "AttachmentHandle_t"; "VectorWS"
было: 0x3d52a00 (499 байт)
- строки: −"P/g"
- инструкций: 135 → 135
```diff
@@ -2,5 +2,5 @@
 ja L
 push rbp
-lea rdx, [S:"P/g"]
+lea rdx, [D]
 mov edi, edi
 mov rbp, rsp
```

### изменена: 0x3d52e70 (285 байт) | строки: "L4g"; "VectorWS"
было: 0x3d52df0 (285 байт)
- строки: +"L4g"
- инструкций: 81 → 81
```diff
@@ -5,5 +5,5 @@
 push rbx
 ja L
-lea rdx, [D]
+lea rdx, [S:"L4g"]
 mov edi, edi
 mov rbx, rsi
```

### изменена: 0x3d530d0 (893 байт) | строки: "@6g"; "InfoForResourceTypeIParticleSystemDefinition"; "CWeakHandle"; "CResourceNameTyped"; "ParticleAttachment_t"; "PrecipitationFilter_t"
было: 0x3d53050 (893 байт)
- строки: +"@6g"
- инструкций: 188 → 188
```diff
@@ -9,5 +9,5 @@
 cmp edi, 6
 ja F
-lea rdx, [D]
+lea rdx, [S:"@6g"]
 mov edi, edi
 mov rbx, rsi
```

### изменена: 0x3d62040 (785 байт) | строки: "Unsupported KV3 basic type '%s' (%d)!"; "Pointers cannot be used as numeric values"
было: 0x3d61fc0 (785 байт)
- строки: −"Z$h"
- инструкций: 219 → 219
```diff
@@ -20,5 +20,5 @@
 cmp bl, 6
 ja L
-lea rdx, [S:"Z$h"]
+lea rdx, [D]
 movzx eax, bl
 movsxd rax, dword ptr [rdx + rax*4]
```

### изменена: 0x3d850d0 (243 байт) | строки: "(1j"; "VectorWS"
было: 0x3d85050 (243 байт)
- строки: +"(1j" −"h0j"
- инструкций: 67 → 67
```diff
@@ -1,5 +1,5 @@
 cmp edi, 6
 ja L
-lea rdx, [S:"h0j"]
+lea rdx, [S:"(1j"]
 mov edi, edi
 push rbp
```

### изменена: 0x3d851d0 (227 байт) | строки: "VectorWS"
было: 0x3d85150 (227 байт)
- строки: −"T1j"
- инструкций: 74 → 74
```diff
@@ -1,5 +1,5 @@
 cmp edi, 6
 ja L
-lea rcx, [S:"T1j"]
+lea rcx, [D]
 mov edi, edi
 push rbp
```

### изменена: 0x3d852c0 (339 байт) | строки: "BASEPTR"; "GameTick_t"
было: 0x3d85240 (339 байт)
- строки: −"(2j"
- инструкций: 90 → 90
```diff
@@ -1,5 +1,5 @@
 cmp edi, 6
 ja L
-lea rdx, [S:"(2j"]
+lea rdx, [D]
 mov edi, edi
 push rbp
```

### изменена: 0x3d85c30 (243 байт) | строки: "<<j"; "VectorWS"
было: 0x3d85bb0 (243 байт)
- строки: +"<<j" −"|;j"
- инструкций: 76 → 76
```diff
@@ -2,5 +2,5 @@
 ja L
 push rbp
-lea rdx, [S:"|;j"]
+lea rdx, [S:"<<j"]
 mov edi, edi
 mov rbp, rsp
```

### изменена: 0x3d86040 (371 байт) | строки: "GameTime_t"; "CBaseEntity"; "CHandle"
было: 0x3d85fc0 (371 байт)
- строки: −"\\?j"
- инструкций: 112 → 112
```diff
@@ -2,5 +2,5 @@
 ja L
 push rbp
-lea rdx, [S:"\\?j"]
+lea rdx, [D]
 mov edi, edi
 mov rbp, rsp
```

### изменена: 0x3d86640 (183 байт) | строки: "cFj"
было: 0x3d865c0 (183 байт)
- строки: +"cFj"
- инструкций: 55 → 55
```diff
@@ -2,5 +2,5 @@
 ja L
 push rbp
-lea rdx, [D]
+lea rdx, [S:"cFj"]
 mov edi, edi
 mov rbp, rsp
```

### изменена: 0x3d86770 (98 байт) | строки: "\"Gj"
было: 0x3d866f0 (98 байт)
- строки: +"\"Gj" −"bFj"
- инструкций: 36 → 36
```diff
@@ -2,5 +2,5 @@
 cmp edx, 6
 ja L
-lea rcx, [S:"bFj"]
+lea rcx, [S:"\"Gj"]
 push rbp
 mov rdi, rsi
```

### изменена: 0x3d867e0 (98 байт) | строки: "vGj"
было: 0x3d86760 (98 байт)
- строки: +"vGj"
- инструкций: 36 → 36
```diff
@@ -2,5 +2,5 @@
 cmp edx, 6
 ja L
-lea rcx, [D]
+lea rcx, [S:"vGj"]
 push rbp
 mov rdi, rsi
```

### изменена: 0x3d869c0 (117 байт) | строки: "1Ij"
было: 0x3d86940 (117 байт)
- строки: +"1Ij" −"qHj"
- инструкций: 39 → 39
```diff
@@ -2,5 +2,5 @@
 cmp edx, 6
 ja L
-lea rcx, [S:"qHj"]
+lea rcx, [S:"1Ij"]
 push rbp
 mov rdi, rsi
```

### изменена: 0x3d86c10 (136 байт) | строки: "xKj"
было: 0x3d86b90 (136 байт)
- строки: +"xKj"
- инструкций: 43 → 43
```diff
@@ -2,5 +2,5 @@
 cmp edx, 6
 ja L
-lea rcx, [D]
+lea rcx, [S:"xKj"]
 push rbp
 mov rax, rsi
```

### изменена: 0x3d87c70 (206 байт)
было: 0x3d87bf0 (206 байт)
- строки: −"?[j"
- инструкций: 62 → 62
```diff
@@ -2,5 +2,5 @@
 ja L
 push rbp
-lea rdx, [S:"?[j"]
+lea rdx, [D]
 mov edi, edi
 mov rbp, rsp
```

### изменена: 0x3d88080 (222 байт)
было: 0x3d88000 (222 байт)
- строки: −"'_j"
- инструкций: 64 → 64
```diff
@@ -2,5 +2,5 @@
 ja L
 push rbp
-lea rdx, [S:"'_j"]
+lea rdx, [D]
 mov edi, edi
 mov rbp, rsp
```

### изменена: 0x3d88260 (435 байт) | строки: "CTransform"; "CNetworkUtlVectorBase"
было: 0x3d881e0 (435 байт)
- строки: −"X`j"
- инструкций: 118 → 118
```diff
@@ -1,5 +1,5 @@
 cmp edi, 6
 ja L
-lea rdx, [S:"X`j"]
+lea rdx, [D]
 mov edi, edi
 push rbp
```

### изменена: 0x3d884d0 (302 байт) | строки: "3dj"
было: 0x3d88450 (302 байт)
- строки: +"3dj" −"scj"
- инструкций: 71 → 71
```diff
@@ -2,5 +2,5 @@
 ja L
 push rbp
-lea rdx, [S:"scj"]
+lea rdx, [S:"3dj"]
 mov edi, edi
 mov rbp, rsp
```

### изменена: 0x3d889a0 (811 байт)
было: 0x3d88920 (811 байт)
- строки: −"Xgj"
- инструкций: 232 → 232
```diff
@@ -9,5 +9,5 @@
 movsxd r13, edx
 push r12
-lea rdx, [S:"Xgj"]
+lea rdx, [D]
 mov r12d, ecx
 push rbx
```

### изменена: 0x3d88ce0 (907 байт) | строки: "Dkj"
было: 0x3d88c60 (907 байт)
- строки: +"Dkj"
- инструкций: 252 → 252
```diff
@@ -9,5 +9,5 @@
 movsxd r13, edx
 push r12
-lea rdx, [D]
+lea rdx, [S:"Dkj"]
 mov r12d, ecx
 push rbx
```

### изменена: 0x3d89b50 (435 байт) | строки: "`yj"; "CPlayerSlot"; "CUtlVector"
было: 0x3d89ad0 (435 байт)
- строки: +"`yj"
- инструкций: 115 → 115
```diff
@@ -1,5 +1,5 @@
 cmp edi, 6
 ja L
-lea rdx, [D]
+lea rdx, [S:"`yj"]
 mov edi, edi
 push rbp
```

### изменена: 0x3d954b0 (659 байт) | строки: "t1k"; "CTakeDamageInfo"; "DestructiblePartDamageRequest_t"; "CUtlLeanVector"; "VectorWS"; "TakeDamageFlags_t"; "HitGroup_t"
было: 0x3d95430 (659 байт)
- строки: +"t1k"
- инструкций: 151 → 151
```diff
@@ -1,5 +1,5 @@
 cmp edi, 6
 ja L
-lea rdx, [D]
+lea rdx, [S:"t1k"]
 mov edi, edi
 push rbp
```

### изменена: 0x3d95750 (659 байт) | строки: "CTakeDamageInfo"; "CTakeDamageResult"
было: 0x3d956d0 (659 байт)
- строки: −"83k"
- инструкций: 126 → 126
```diff
@@ -2,5 +2,5 @@
 ja L
 push rbp
-lea rdx, [S:"83k"]
+lea rdx, [D]
 mov edi, edi
 mov rbp, rsp
```

### изменена: 0x3d95d80 (563 байт) | строки: "CUtlVector"; "VectorWS"; "GameTime_t"
было: 0x3d95d00 (563 байт)
- строки: −"H9k"
- инструкций: 157 → 157
```diff
@@ -2,5 +2,5 @@
 ja L
 push rbp
-lea rdx, [S:"H9k"]
+lea rdx, [D]
 mov edi, edi
 mov rbp, rsp
```

### изменена: 0x3d98cd0 (4083 байт) вызывается из: CTakeDamageInfo::vfunc#2 | строки: "m_vecDamageForce"; "m_bitsDamageType"; "m_vecDamagePosition"; "m_vecReportedPosition"; "m_vecDamageDirection"; "m_hInflictor"; "m_hAttacker"; "m_hAbility"
было: 0x3d98c50 (4083 байт)
- строки: −"+lk" −"6vk"
- инструкций: 886 → 886
```diff
@@ -113,5 +113,5 @@
 cmp r8b, 6
 ja L
-lea rdx, [S:"+lk"]
+lea rdx, [D]
 movzx eax, r8b
 movsxd rax, dword ptr [rdx + rax*4]
@@ -362,5 +362,5 @@
 cmp r8b, 6
 ja L
-lea rdx, [S:"6vk"]
+lea rdx, [D]
 movzx eax, r8b
 movsxd rax, dword ptr [rdx + rax*4]
```

### изменена: 0x3da4980 (414 байт)
было: 0x3da4900 (414 байт)
- строки: −"P$l"
- инструкций: 136 → 136
```diff
@@ -8,5 +8,5 @@
 movsxd r12, edx
 push rbx
-lea rdx, [S:"P$l"]
+lea rdx, [D]
 mov rbx, rsi
 sub rsp, 0x18
```

### изменена: 0x3da55a0 (542 байт)
было: 0x3da5520 (542 байт)
- строки: −"00l"
- инструкций: 159 → 159
```diff
@@ -9,5 +9,5 @@
 movsxd r12, edx
 push rbx
-lea rdx, [S:"00l"]
+lea rdx, [D]
 mov rbx, rsi
 sub rsp, 0x10
```

### изменена: 0x3daa7f0 (961 байт) | строки: "%g %g %g"; "(null)"; "%g %g %g %g"; "unknown_variant_type"; "1yl"; "%lld"; "%llu"; "%d %d %d %d"
было: 0x3daa770 (961 байт)
- строки: +"1yl" −"Bxl" −"qxl"
- инструкций: 213 → 213
```diff
@@ -7,5 +7,5 @@
 cmp al, 0x4f
 ja L
-lea rcx, [S:"Bxl"]
+lea rcx, [D]
 movzx edx, al
 movsxd rdx, dword ptr [rcx + rdx*4]
@@ -91,5 +91,5 @@
 cmp al, 0x47
 ja L
-lea rdx, [S:"qxl"]
+lea rdx, [S:"1yl"]
 movzx eax, al
 movsxd rax, dword ptr [rdx + rax*4]
```

### изменена: 0x3db8430 (851 байт) | строки: "<Tm"; "%llu"
было: 0x3db83b0 (851 байт)
- строки: +"<Tm" −"|Sm"
- инструкций: 190 → 190
```diff
@@ -21,5 +21,5 @@
 mov rbx, rax
 je L
-lea r13, [S:"|Sm"]
+lea r13, [S:"<Tm"]
 nop dword ptr [rax + rax]
 mov qword ptr [rbp - 0xc0], 0
```

### изменена: 0x3db8c40 (819 байт) | строки: "DecalFlags_t"; "GameTime_t"
было: 0x3db8bc0 (819 байт)
- строки: −"$Ym"
- инструкций: 143 → 143
```diff
@@ -2,5 +2,5 @@
 ja L
 push rbp
-lea rdx, [S:"$Ym"]
+lea rdx, [D]
 mov edi, edi
 mov rbp, rsp
```

### изменена: 0x3df7820 (350 байт)
было: 0x3df77a0 (350 байт)
- строки: −"_,q"
- инструкций: 92 → 92
```diff
@@ -2,5 +2,5 @@
 ja L
 push rbp
-lea rdx, [S:"_,q"]
+lea rdx, [D]
 mov edi, edi
 mov rbp, rsp
```

### изменена: 0x3df7a00 (407 байт) вызывается из: CVScriptGameSystem::vfunc#85 | строки: "D.q"
было: 0x3df7980 (407 байт)
- строки: +"D.q"
- инструкций: 104 → 104
```diff
@@ -31,5 +31,5 @@
 ja L
 movzx eax, word ptr [rax + 0x28]
-lea rdx, [D]
+lea rdx, [S:"D.q"]
 movsxd rax, dword ptr [rdx + rax*4]
 add rax, rdx
```

### изменена: 0x3df96a0 (547 байт) | строки: "hJq"; "CHandle"; "CEnvSoundscapeTriggerable"; "CBasePlayerPawn"; "CUtlVector"
было: 0x3df9620 (547 байт)
- строки: +"hJq"
- инструкций: 144 → 144
```diff
@@ -2,5 +2,5 @@
 ja L
 push rbp
-lea rdx, [D]
+lea rdx, [S:"hJq"]
 mov edi, edi
 mov rbp, rsp
```

### изменена: 0x3dfc150 (502 байт)
было: 0x3dfc0d0 (502 байт)
- строки: −"4tq"
- инструкций: 139 → 139
```diff
@@ -21,5 +21,5 @@
 cmp al, 0x24
 ja L
-lea rcx, [S:"4tq"]
+lea rcx, [D]
 movzx eax, al
 movsxd rax, dword ptr [rcx + rax*4]
```

### изменена: 0x3e1a980 (4702 байт) | строки: "classname"; "PWs"; "connections"; "attributes"; "X]s"
было: 0x3e1a900 (4702 байт)
- строки: +"PWs" +"X]s" −"X[s"
- инструкций: 1086 → 1086
```diff
@@ -208,5 +208,5 @@
 cmp r14b, 0x4f
 ja L
-lea rsi, [D]
+lea rsi, [S:"PWs"]
 movsxd rax, dword ptr [rsi + r14*4]
 add rax, rsi
@@ -617,5 +617,5 @@
 cmp al, 0x4f
 ja L
-lea rsi, [D]
+lea rsi, [S:"X]s"]
 movzx edx, al
 movsxd rdx, dword ptr [rsi + rdx*4]
@@ -747,5 +747,5 @@
 cmp al, 0x4f
 ja L
-lea rsi, [S:"X[s"]
+lea rsi, [D]
 movzx edx, al
 movsxd rdx, dword ptr [rsi + rdx*4]
```

### изменена: 0x3e2b960 (542 байт)
было: 0x3e2b8e0 (542 байт)
- строки: −"DZt"
- инструкций: 159 → 159
```diff
@@ -9,5 +9,5 @@
 movsxd r12, edx
 push rbx
-lea rdx, [S:"DZt"]
+lea rdx, [D]
 mov rbx, rsi
 sub rsp, 0x10
```

### изменена: 0x3e6cbc0 (187 байт) | строки: "hYx"; "Disposition_t"
было: 0x3e6cb40 (187 байт)
- строки: +"hYx"
- инструкций: 59 → 59
```diff
@@ -1,5 +1,5 @@
 cmp edi, 6
 ja L
-lea rdx, [D]
+lea rdx, [S:"hYx"]
 mov edi, edi
 push rbp
```

### изменена: 0x3e6cdb0 (275 байт) | строки: "D[x"; "VectorWS"
было: 0x3e6cd30 (275 байт)
- строки: +"D[x"
- инструкций: 84 → 84
```diff
@@ -1,5 +1,5 @@
 cmp edi, 6
 ja L
-lea rcx, [D]
+lea rcx, [S:"D[x"]
 mov edi, edi
 push rbp
```

### изменена: 0x3e6cf70 (243 байт) | строки: "VectorWS"
было: 0x3e6cef0 (243 байт)
- строки: −" \\x"
- инструкций: 70 → 70
```diff
@@ -1,5 +1,5 @@
 cmp edi, 6
 ja L
-lea rdx, [S:" \\x"]
+lea rdx, [D]
 mov edi, edi
 push rbp
```

### изменена: 0x3e6d9c0 (451 байт) | строки: "$gx"; "CEconWearable"; "CHandle"; "CNetworkUtlVectorBase"; "RelationshipOverride_t"; "CUtlVector"; "Hull_t"; "CMovementStatsProperty"
было: 0x3e6d940 (451 байт)
- строки: +"$gx" −"dfx"
- инструкций: 129 → 129
```diff
@@ -2,5 +2,5 @@
 ja L
 push rbp
-lea rdx, [S:"dfx"]
+lea rdx, [S:"$gx"]
 mov edi, edi
 mov rbp, rsp
```

### изменена: 0x3e6eff0 (187 байт)
было: 0x3e6ef70 (187 байт)
- строки: −"S|x"
- инструкций: 52 → 52
```diff
@@ -3,5 +3,5 @@
 ja L
 push rbp
-lea rcx, [S:"S|x"]
+lea rcx, [D]
 mov rdi, rsi
 mov rbp, rsp
```

### изменена: 0x3e6f0b0 (171 байт) | строки: "@}x"; "HitGroup_t"
было: 0x3e6f030 (171 байт)
- строки: +"@}x"
- инструкций: 54 → 54
```diff
@@ -1,5 +1,5 @@
 cmp edi, 6
 ja L
-lea rdx, [D]
+lea rdx, [S:"@}x"]
 mov edi, edi
 push rbp
```

### изменена: 0x3e6f160 (133 байт)
было: 0x3e6f0e0 (133 байт)
- строки: −"U}x"
- инструкций: 41 → 41
```diff
@@ -2,5 +2,5 @@
 cmp edx, 6
 ja L
-lea rcx, [S:"U}x"]
+lea rcx, [D]
 push rbp
 mov rdi, rsi
```

### изменена: 0x3e6f2b0 (133 байт)
было: 0x3e6f230 (133 байт)
- строки: −"m~x"
- инструкций: 40 → 40
```diff
@@ -1,5 +1,5 @@
 cmp edi, 6
 ja L
-lea rcx, [S:"m~x"]
+lea rcx, [D]
 mov edi, edi
 push rbp
```

### изменена: 0x3eaa4a0 (769 байт) вызывается из: CAnimGraphControllerBase::vfunc#2, CEmptyGraphController::vfunc#2, EventGrantDefinition_Emoticon_t::vfunc#2 | строки: "\"-|"; "Unsupported KV3 basic type '%s' (%d)!"; "Pointers cannot be used as numeric values"
было: 0x3eaa420 (769 байт)
- строки: +"\"-|" −"b,|"
- инструкций: 220 → 220
```diff
@@ -31,5 +31,5 @@
 cmp bl, 6
 ja L
-lea rdx, [S:"b,|"]
+lea rdx, [S:"\"-|"]
 movzx eax, bl
 movsxd rax, dword ptr [rdx + rax*4]
```

### изменена: 0x3eacab0 (856 байт) | строки: "|P|"
было: 0x3eacd90 (856 байт)
- строки: +"|P|"
- инструкций: 221 → 221
```diff
@@ -10,5 +10,5 @@
 movsxd r12, edx
 push rbx
-lea rdx, [D]
+lea rdx, [S:"|P|"]
 mov rbx, rsi
 sub rsp, 0x58
```

### изменена: 0x3eaeac0 (904 байт) | строки: "8p|"
было: 0x3eaea40 (904 байт)
- строки: +"8p|" −"xo|"
- инструкций: 237 → 237
```diff
@@ -7,5 +7,5 @@
 mov r15d, edx
 push r14
-lea rdx, [S:"xo|"]
+lea rdx, [S:"8p|"]
 push r13
 push r12
```

### изменена: 0x3eaf9a0 (891 байт) | строки: "CPhysicsBodyGameMarkup"; "CUtlDict"
было: 0x3eaf920 (891 байт)
- строки: −"$~|"
- инструкций: 230 → 230
```diff
@@ -1,5 +1,5 @@
 cmp edi, 6
 ja L
-lea rdx, [S:"$~|"]
+lea rdx, [D]
 mov edi, edi
 push rbp
```

### изменена: 0x3eca3e0 (904 байт)
было: 0x3eca360 (904 байт)
- строки: −"((~"
- инструкций: 238 → 238
```diff
@@ -7,5 +7,5 @@
 mov r15d, edx
 push r14
-lea rdx, [S:"((~"]
+lea rdx, [D]
 push r13
 push r12
```

### изменена: 0x441f460 (410 байт) CDOTA_Ability_Lua::OnChannelFinish | строки: "OnChannelFinish"
было: 0x44124c0 (360 байт)
- числа в инструкциях: +0 +3
- инструкций: 90 → 100
```diff
@@ -1,4 +1,5 @@
 push rbp
 mov rbp, rsp
+push r14
 push r13
 push r12
@@ -6,5 +7,5 @@
 push rbx
 mov ebx, esi
-sub rsp, 0x28
+sub rsp, 0x20
 call F
 cmp rax, qword ptr [D]
@@ -14,7 +15,8 @@
 test eax, eax
 je L
-lea rdi, [D]
+lea r13, [D]
+mov rdi, r13
 call F
-mov r13, qword ptr [r12 + 0x10]
+mov r14, qword ptr [r12 + 0x10]
 mov dword ptr [rbp - 0x38], 0
 xor ecx, ecx
@@ -25,5 +27,5 @@
 mov qword ptr [rbp - 0x40], 0
 mov dword ptr [rbp - 0x28], 6
-mov rdx, qword ptr [r13 + 0x28]
+mov rdx, qword ptr [r14 + 0x28]
 mov rdi, qword ptr [r12]
 mov rax, qword ptr [rdi]
@@ -36,5 +38,5 @@
 mov ecx, 1
 mov rsi, rbx
```
(ещё 43 строк диффа: so-query.py fdiff libserver.so 0x441f460)

### изменена: 0x441f600 (410 байт) CDOTA_Item_Lua::OnChannelFinish | строки: "OnChannelFinish"
было: 0x4412630 (360 байт)
- числа в инструкциях: +0 +3
- инструкций: 90 → 100
```diff
@@ -1,4 +1,5 @@
 push rbp
 mov rbp, rsp
+push r14
 push r13
 push r12
@@ -6,5 +7,5 @@
 push rbx
 mov ebx, esi
-sub rsp, 0x28
+sub rsp, 0x20
 call F
 cmp rax, qword ptr [D]
@@ -14,7 +15,8 @@
 test eax, eax
 je L
-lea rdi, [D]
+lea r13, [D]
+mov rdi, r13
 call F
-mov r13, qword ptr [r12 + 0x10]
+mov r14, qword ptr [r12 + 0x10]
 mov dword ptr [rbp - 0x38], 0
 xor ecx, ecx
@@ -25,5 +27,5 @@
 mov qword ptr [rbp - 0x40], 0
 mov dword ptr [rbp - 0x28], 6
-mov rdx, qword ptr [r13 + 0x28]
+mov rdx, qword ptr [r14 + 0x28]
 mov rdi, qword ptr [r12]
 mov rax, qword ptr [rdi]
@@ -36,5 +38,5 @@
 mov ecx, 1
 mov rsi, rbx
```
(ещё 43 строк диффа: so-query.py fdiff libserver.so 0x441f600)

### изменена: 0x441f7a0 (431 байт) CDOTA_Modifier_Lua::OnRemoved, CDOTA_Modifier_Lua_Horizontal_Motion::OnRemoved, CDOTA_Modifier_Lua_Vertical_Motion::OnRemoved | строки: "OnRemoved"
было: 0x4412c40 (377 байт)
- числа в инструкциях: +0 +3
- инструкций: 96 → 105
```diff
@@ -1,11 +1,12 @@
 push rbp
 mov rbp, rsp
+push r15
+mov r15d, esi
 push r14
-mov r14d, esi
 push r13
 push r12
 mov r12, rdi
 push rbx
-sub rsp, 0x20
+sub rsp, 0x28
 call F
 cmp rax, qword ptr [D]
@@ -15,5 +16,6 @@
 test eax, eax
 je L
-lea rdi, [D]
+lea r14, [D]
+mov rdi, r14
 call F
 mov rdi, r12
@@ -29,19 +31,19 @@
 mov r13, rax
 je L
-mov dword ptr [rbp - 0x28], 0
+mov dword ptr [rbp - 0x38], 0
 xor r9d, r9d
 xor r8d, r8d
 mov rsi, r13
 mov rdi, qword ptr [r12 + 0x1af8]
-mov qword ptr [rbp - 0x40], rbx
+mov qword ptr [rbp - 0x50], rbx
```
(ещё 69 строк диффа: so-query.py fdiff libserver.so 0x441f7a0)

### изменена: 0x441f950 (528 байт) CDOTA_Modifier_Lua::OnCreated, CDOTA_Modifier_Lua_Horizontal_Motion::OnCreated, CDOTA_Modifier_Lua_Vertical_Motion::OnCreated | строки: "OnCreated"
было: 0x44149b0 (451 байт)
- числа в инструкциях: +0 +3
- инструкций: 115 → 125
```diff
@@ -2,11 +2,11 @@
 mov rbp, rsp
 push r15
+mov r15, rsi
 push r14
-mov r14, rsi
 push r13
 push r12
 push rbx
 mov rbx, rdi
-sub rsp, 0x28
+sub rsp, 0x38
 call F
 cmp rax, qword ptr [D]
@@ -16,5 +16,7 @@
 test eax, eax
 je L
-lea rdi, [D]
+lea rax, [D]
+mov rdi, rax
+mov qword ptr [rbp - 0x58], rax
 call F
 mov rdi, rbx
@@ -30,5 +32,5 @@
 mov r13, rax
 je L
-mov r15, qword ptr [rbx + 0x1af8]
+mov r14, qword ptr [rbx + 0x1af8]
 mov qword ptr [rbp - 0x50], r12
 lea r12, [rbp - 0x40]
@@ -37,14 +39,14 @@
 mov dword ptr [rbp - 0x38], 0
 mov dword ptr [rbp - 0x48], 0x1f
-mov rax, qword ptr [r15]
```
(ещё 72 строк диффа: so-query.py fdiff libserver.so 0x441f950)

### изменена: 0x441fb60 (528 байт) CDOTA_Modifier_Lua::OnRefresh, CDOTA_Modifier_Lua_Horizontal_Motion::OnRefresh, CDOTA_Modifier_Lua_Vertical_Motion::OnRefresh | строки: "OnRefresh"
было: 0x4414b80 (451 байт)
- числа в инструкциях: +0 +3
- инструкций: 115 → 125
```diff
@@ -2,11 +2,11 @@
 mov rbp, rsp
 push r15
+mov r15, rsi
 push r14
-mov r14, rsi
 push r13
 push r12
 push rbx
 mov rbx, rdi
-sub rsp, 0x28
+sub rsp, 0x38
 call F
 cmp rax, qword ptr [D]
@@ -16,5 +16,7 @@
 test eax, eax
 je L
-lea rdi, [D]
+lea rax, [D]
+mov rdi, rax
+mov qword ptr [rbp - 0x58], rax
 call F
 mov rdi, rbx
@@ -30,5 +32,5 @@
 mov r13, rax
 je L
-mov r15, qword ptr [rbx + 0x1af8]
+mov r14, qword ptr [rbx + 0x1af8]
 mov qword ptr [rbp - 0x50], r12
 lea r12, [rbp - 0x40]
@@ -37,14 +39,14 @@
 mov dword ptr [rbp - 0x38], 0
 mov dword ptr [rbp - 0x48], 0x1f
-mov rax, qword ptr [r15]
```
(ещё 72 строк диффа: so-query.py fdiff libserver.so 0x441fb60)

### изменена: 0x4420970 (1143 байт) | строки: "ability_lua"
было: 0x441fea0 (1039 байт)
- числа в инструкциях: +1 +1 +3
- прямых вызовов: 21 → 22
- инструкций: 226 → 246
```diff
@@ -9,4 +9,12 @@
 sub rsp, 0x88
 call F
+cmp rax, qword ptr [D]
+je L
+mov rsi, rax
+mov eax, dword ptr [D]
+test eax, eax
+je L
+lea rdi, [D]
+call F
 lea rax, [rbp - 0x50]
 xor ecx, ecx
@@ -26,15 +34,16 @@
 call qword ptr [rax + 0x138]
 test eax, eax
+mov r8d, eax
 jle L
-mov r8d, eax
+lea r15, [rbp - 0x80]
 mov qword ptr [rbp - 0x90], r14
 xor r12d, r12d
 xor ebx, ebx
-lea r15, [rbp - 0x80]
-mov r14d, r8d
 lea rax, [rbp - 0x70]
 mov qword ptr [rbp - 0x88], r15
+mov r14d, r8d
 mov r15, rax
 jmp L
+nop word ptr [rax + rax]
 cmp al, 2
 je L
@@ -133,4 +142,12 @@
```
(ещё 43 строк диффа: so-query.py fdiff libserver.so 0x4420970)

### изменена: 0x44217e0 (119 байт) CDOTA_Ability_DataDriven::vfunc#50
было: 0x44203e0 (94 байт)
- поля объектов: +0x138 +0x60 +0x18
- инструкций: 27 → 34
```diff
@@ -23,4 +23,11 @@
 test rax, rax
 je L
+mov rdx, qword ptr [rax + 0x18]
+mov rax, qword ptr [rdx + 0x138]
+test rax, rax
+jne L
+mov rax, qword ptr [rdx + 0x60]
+test rax, rax
+je L
 mov rdi, qword ptr [rax + 0x18]
 xor esi, esi
```

### изменена: 0x4421860 (119 байт) CDOTA_Ability_Lua::vfunc#50
было: 0x4420440 (94 байт)
- поля объектов: +0x138 +0x60 +0x18
- инструкций: 27 → 34
```diff
@@ -23,4 +23,11 @@
 test rax, rax
 je L
+mov rdx, qword ptr [rax + 0x18]
+mov rax, qword ptr [rdx + 0x138]
+test rax, rax
+jne L
+mov rax, qword ptr [rdx + 0x60]
+test rax, rax
+je L
 mov rdi, qword ptr [rax + 0x18]
 xor esi, esi
```

### изменена: 0x44218e0 (119 байт) CDOTA_Item_DataDriven::vfunc#50
было: 0x44204a0 (94 байт)
- поля объектов: +0x138 +0x60 +0x18
- инструкций: 27 → 34
```diff
@@ -23,4 +23,11 @@
 test rax, rax
 je L
+mov rdx, qword ptr [rax + 0x18]
+mov rax, qword ptr [rdx + 0x138]
+test rax, rax
+jne L
+mov rax, qword ptr [rdx + 0x60]
+test rax, rax
+je L
 mov rdi, qword ptr [rax + 0x18]
 xor esi, esi
```

### изменена: 0x4421960 (119 байт) CDOTA_Item_Lua::vfunc#50
было: 0x4420500 (94 байт)
- поля объектов: +0x138 +0x60 +0x18
- инструкций: 27 → 34
```diff
@@ -23,4 +23,11 @@
 test rax, rax
 je L
+mov rdx, qword ptr [rax + 0x18]
+mov rax, qword ptr [rdx + 0x138]
+test rax, rax
+jne L
+mov rax, qword ptr [rdx + 0x60]
+test rax, rax
+je L
 mov rdi, qword ptr [rax + 0x18]
 xor esi, esi
```

### изменена: 0x44219e0 (119 байт) CDOTA_NPC_DataDriven::vfunc#50
было: 0x4420560 (94 байт)
- поля объектов: +0x138 +0x60 +0x18
- инструкций: 27 → 34
```diff
@@ -23,4 +23,11 @@
 test rax, rax
 je L
+mov rdx, qword ptr [rax + 0x18]
+mov rax, qword ptr [rdx + 0x138]
+test rax, rax
+jne L
+mov rax, qword ptr [rdx + 0x60]
+test rax, rax
+je L
 mov rdi, qword ptr [rax + 0x18]
 xor esi, esi
```

### изменена: 0x4423370 (4762 байт) вызывается из: CDOTA_Modifier_Lua::vfunc#97
было: 0x4421ed0 (3694 байт)
- числа в инструкциях: +0x1a0 −0x191
- инструкций: 627 → 805
```diff
@@ -1,3 +1,3 @@
-cmp esi, 0x191
+cmp esi, 0x1a0
 ja L
 lea rdx, [D]
@@ -626,2 +626,180 @@
 lea rax, [T]
 jmp L
+lea rax, [T]
+jmp L
+lea rax, [T]
+jmp L
+lea rax, [T]
+jmp L
+lea rax, [T]
+jmp L
+lea rax, [T]
+jmp L
+lea rax, [T]
+jmp L
+lea rax, [T]
+jmp L
+lea rax, [T]
+jmp L
+lea rax, [T]
+jmp L
+lea rax, [T]
+jmp L
+lea rax, [T]
+jmp L
+lea rax, [T]
+jmp L
+lea rax, [T]
+jmp L
```
(ещё 152 строк диффа: so-query.py fdiff libserver.so 0x4423370)

### изменена: 0x44262d0 (365 байт) CDOTA_Item_Lua::GetCustomHudErrorMessage | строки: "GetCustomHudErrorMessage"
было: 0x44246f0 (373 байт)
- прямых вызовов: 8 → 7
- инструкций: 90 → 87
```diff
@@ -24,4 +24,5 @@
 mov rdx, r14
 mov dword ptr [rbp - 0x28], 0
+xor r12d, r12d
 lea rsi, [S:"GetCustomHudErrorMessage"]
 lea rdi, [rax + 0x28]
@@ -29,6 +30,5 @@
 cmp byte ptr [rbp - 0x28], 0x1e
 jne L
-mov rdi, r14
-call F
+mov rax, qword ptr [rbp - 0x30]
 cmp byte ptr [rax], 0
 je L
@@ -38,8 +38,8 @@
 mov rsi, rax
 call F
-mov rbx, qword ptr [rbx + 0x978]
+mov r12, qword ptr [rbx + 0x978]
 lea rax, [D]
-test rbx, rbx
-cmove rbx, rax
+test r12, r12
+cmove r12, rax
 test byte ptr [rbp - 0x26], 1
 je L
@@ -52,5 +52,5 @@
 je L
 add rsp, 0x10
-mov rax, rbx
+mov rax, r12
 pop rbx
 pop r12
@@ -59,5 +59,5 @@
```
(ещё 21 строк диффа: so-query.py fdiff libserver.so 0x44262d0)

### изменена: 0x4420f20 (1106 байт) | строки: "modifier_lua"
было: 0x4424870 (954 байт)
- числа в инструкциях: +0 +0x4f +0x1e +2 +0x200 +0xc000000800000000
- прямых вызовов: 19 → 21
- инструкций: 207 → 240
```diff
@@ -8,5 +8,5 @@
 push rbx
 sub rsp, 0x88
-mov qword ptr [rbp - 0x98], rsi
+mov qword ptr [rbp - 0x90], rsi
 call F
 cmp rax, qword ptr [D]
@@ -22,5 +22,5 @@
 xor ecx, ecx
 mov rdi, rax
-mov qword ptr [rbp - 0x90], rax
+mov qword ptr [rbp - 0x88], rax
 lea rsi, [S:"modifier_lua"]
 call F
@@ -28,5 +28,5 @@
 mov qword ptr [rbp - 0x80], 0
 mov dword ptr [rbp - 0x78], 0
-mov rsi, qword ptr [rbp - 0x98]
+mov rsi, qword ptr [rbp - 0x90]
 mov qword ptr [rbp - 0x70], 0
 mov dword ptr [rbp - 0x68], 0
@@ -39,12 +39,11 @@
 xor r12d, r12d
 xor ebx, ebx
+mov qword ptr [rbp - 0x98], rax
+lea rax, [rbp - 0x60]
+mov r15d, edx
 lea r14, [rbp - 0x80]
 mov qword ptr [rbp - 0xa0], rax
-lea rax, [rbp - 0x60]
-mov qword ptr [rbp - 0x88], r14
-mov r14d, edx
-mov qword ptr [rbp - 0xa8], rax
-jmp L
```
(ещё 214 строк диффа: so-query.py fdiff libserver.so 0x4420f20)

### изменена: 0x4421380 (1106 байт) | строки: "modifier_lua"
было: 0x4424c30 (954 байт)
- числа в инструкциях: +0 +0x4f +0x1e +2 +0x200 +0xc000000800000000
- прямых вызовов: 19 → 21
- инструкций: 207 → 240
```diff
@@ -8,5 +8,5 @@
 push rbx
 sub rsp, 0x88
-mov qword ptr [rbp - 0x98], rsi
+mov qword ptr [rbp - 0x90], rsi
 call F
 cmp rax, qword ptr [D]
@@ -22,5 +22,5 @@
 xor ecx, ecx
 mov rdi, rax
-mov qword ptr [rbp - 0x90], rax
+mov qword ptr [rbp - 0x88], rax
 lea rsi, [S:"modifier_lua"]
 call F
@@ -28,5 +28,5 @@
 mov qword ptr [rbp - 0x80], 0
 mov dword ptr [rbp - 0x78], 0
-mov rsi, qword ptr [rbp - 0x98]
+mov rsi, qword ptr [rbp - 0x90]
 mov qword ptr [rbp - 0x70], 0
 mov dword ptr [rbp - 0x68], 0
@@ -39,12 +39,11 @@
 xor r12d, r12d
 xor ebx, ebx
+mov qword ptr [rbp - 0x98], rax
+lea rax, [rbp - 0x60]
+mov r15d, edx
 lea r14, [rbp - 0x80]
 mov qword ptr [rbp - 0xa0], rax
-lea rax, [rbp - 0x60]
-mov qword ptr [rbp - 0x88], r14
-mov r14d, edx
-mov qword ptr [rbp - 0xa8], rax
-jmp L
```
(ещё 214 строк диффа: so-query.py fdiff libserver.so 0x4421380)

### изменена: 0x4426f80 (365 байт) CDOTA_Item_Lua::GetCustomCastErrorLocation | строки: "GetCustomCastErrorLocation"
было: 0x4425b30 (393 байт)
- прямых вызовов: 8 → 7
- инструкций: 91 → 88
```diff
@@ -26,10 +26,10 @@
 movss xmm1, dword ptr [rbx + 8]
 lea rsi, [S:"GetCustomCastErrorLocation"]
+xor ebx, ebx
 lea rdi, [rax + 0x28]
 call F
 cmp byte ptr [rbp - 0x28], 0x1e
 jne L
-mov rdi, r14
-call F
+mov rax, qword ptr [rbp - 0x30]
 cmp byte ptr [rax], 0
 je L
@@ -60,5 +60,5 @@
 pop rbp
 ret
-nop dword ptr [rax + rax]
+nop
 mov edx, 3
 lock cmpxchg dword ptr [D], edx
@@ -70,7 +70,4 @@
 jmp L
 nop word ptr [rax + rax]
-xor ebx, ebx
-jmp L
-nop dword ptr [rax]
 add word ptr [D], 1
 lea r13, [D]
```

### изменена: 0x4428620 (1132 байт) CDOTA_Ability_Lua::vfunc#372 | строки: "OnProjectileThink"; "OnProjectileThinkHandle"; "OnProjectileThink_ExtraData"
было: 0x44271e0 (1033 байт)
- числа в инструкциях: +1 +1 +3
- прямых вызовов: 22 → 23
- инструкций: 239 → 256
```diff
@@ -2,5 +2,4 @@
 mov rbp, rsp
 push r15
-mov r15, rdi
 push r14
 push r13
@@ -9,7 +8,18 @@
 push rbx
 sub rsp, 0x98
-mov qword ptr [rbp - 0xb0], rdi
-call F
-mov rdi, qword ptr [r15 + 0x10]
+mov qword ptr [rbp - 0x98], rdi
+call F
+cmp rax, qword ptr [D]
+je L
+mov rsi, rax
+mov eax, dword ptr [D]
+test eax, eax
+je L
+lea rdi, [D]
+call F
+mov rax, qword ptr [rbp - 0x98]
+mov ebx, 0xffffffff
+mov r12d, 0xffffffff
+mov rdi, qword ptr [rax + 0x10]
 test rdi, rdi
 je L
@@ -23,5 +33,5 @@
 lea rsi, [S:"OnProjectileThink"]
 mov dword ptr [rbp - 0x48], 0
-mov qword ptr [rbp - 0x98], rdx
+mov qword ptr [rbp - 0xa0], rdx
 call F
```
(ещё 115 строк диффа: so-query.py fdiff libserver.so 0x4428620)

### изменена: 0x441fd70 (1181 байт) CDOTA_Ability_Lua::OnHeroDiedNearby | строки: "OnHeroDiedNearby"; "unit"; "attacker"
было: 0x44275f0 (1129 байт)
- числа в инструкциях: +1 +1 +1
- виртуальные вызовы: +0x20 (слот 4) +0x20 (слот 4) +0x20 (слот 4)
- инструкций: 241 → 254
```diff
@@ -61,9 +61,9 @@
 mov rdx, qword ptr [rax]
 mov rdi, rax
-mov qword ptr [rbp - 0xd8], rax
-mov qword ptr [rbp - 0xe0], rcx
+mov qword ptr [rbp - 0xe0], rax
+mov qword ptr [rbp - 0xd8], rcx
 call qword ptr [rdx + 0x128]
 mov rdx, qword ptr [rbp - 0xb0]
-mov rax, qword ptr [rbp - 0xd8]
+mov rax, qword ptr [rbp - 0xe0]
 test rdx, rdx
 jne L
@@ -71,24 +71,26 @@
 mov r14, qword ptr [r13 + 0x10]
 mov qword ptr [rbp - 0xa0], 0
-mov rdi, qword ptr [rbp - 0xe0]
+mov rdi, qword ptr [rbp - 0xd8]
 mov rsi, rax
-mov qword ptr [rbp - 0xd8], rax
+mov qword ptr [rbp - 0x100], rax
 mov dword ptr [rbp - 0x98], 0
 lea r13, [rbp - 0x60]
 mov dword ptr [rbp - 0x68], 0
 call F
-lea rax, [rbp - 0x80]
+movzx eax, word ptr [rbp - 0x66]
+lea rdx, [rbp - 0x80]
 mov dword ptr [rbp - 0x78], 0
-mov rsi, rax
-mov qword ptr [rbp - 0xf8], rax
+mov rsi, rdx
+mov qword ptr [rbp - 0xf8], rdx
 lea rdi, [rbp - 0xc0]
```
(ещё 145 строк диффа: so-query.py fdiff libserver.so 0x441fd70)

### изменена: 0x4420210 (1181 байт) CDOTA_Item_Lua::OnHeroDiedNearby | строки: "OnHeroDiedNearby"; "unit"; "attacker"
было: 0x4427a60 (1129 байт)
- числа в инструкциях: +1 +1 +1
- виртуальные вызовы: +0x20 (слот 4) +0x20 (слот 4) +0x20 (слот 4)
- инструкций: 241 → 254
```diff
@@ -61,9 +61,9 @@
 mov rdx, qword ptr [rax]
 mov rdi, rax
-mov qword ptr [rbp - 0xd8], rax
-mov qword ptr [rbp - 0xe0], rcx
+mov qword ptr [rbp - 0xe0], rax
+mov qword ptr [rbp - 0xd8], rcx
 call qword ptr [rdx + 0x128]
 mov rdx, qword ptr [rbp - 0xb0]
-mov rax, qword ptr [rbp - 0xd8]
+mov rax, qword ptr [rbp - 0xe0]
 test rdx, rdx
 jne L
@@ -71,24 +71,26 @@
 mov r14, qword ptr [r13 + 0x10]
 mov qword ptr [rbp - 0xa0], 0
-mov rdi, qword ptr [rbp - 0xe0]
+mov rdi, qword ptr [rbp - 0xd8]
 mov rsi, rax
-mov qword ptr [rbp - 0xd8], rax
+mov qword ptr [rbp - 0x100], rax
 mov dword ptr [rbp - 0x98], 0
 lea r13, [rbp - 0x60]
 mov dword ptr [rbp - 0x68], 0
 call F
-lea rax, [rbp - 0x80]
+movzx eax, word ptr [rbp - 0x66]
+lea rdx, [rbp - 0x80]
 mov dword ptr [rbp - 0x78], 0
-mov rsi, rax
-mov qword ptr [rbp - 0xf8], rax
+mov rsi, rdx
+mov qword ptr [rbp - 0xf8], rdx
 lea rdi, [rbp - 0xc0]
```
(ещё 145 строк диффа: so-query.py fdiff libserver.so 0x4420210)

### изменена: 0x4429aa0 (1353 байт) | строки: "ApplyModifier"; "%f %f %f"
было: 0x4428f40 (1321 байт)
- числа в инструкциях: −0 −0
- поля объектов: +0xf0
- прямых вызовов: 30 → 31
- инструкций: 273 → 283
```diff
@@ -9,6 +9,6 @@
 sub rsp, 0xe8
 test rsi, rsi
-mov qword ptr [rbp - 0xf8], rdi
-mov qword ptr [rbp - 0xf0], rcx
+mov qword ptr [rbp - 0xf0], rdi
+mov qword ptr [rbp - 0xe8], rcx
 mov qword ptr [rbp - 0xd0], r8
 je L
@@ -25,18 +25,28 @@
 call r14
 test rax, rax
-mov qword ptr [rbp - 0xe8], rax
+mov r15, rax
 je L
 cmp byte ptr [rax + 0x5d1], 3
 jne L
-mov rdi, rbx
-call F
-test rax, rax
-mov r15, rax
+test rbx, rbx
+je L
+lea r12, [D]
+xor edi, edi
+mov r13, qword ptr [r12]
+mov rax, qword ptr [r13]
+mov r14, qword ptr [rax + 0xf0]
+call F
+mov rsi, rbx
+mov rdi, r13
+mov rdx, rax
+call r14
+test rax, rax
```
(ещё 259 строк диффа: so-query.py fdiff libserver.so 0x4429aa0)

### изменена: 0x4429ff0 (1333 байт) | строки: "ApplyModifier"; "%f %f %f"
было: 0x4429470 (1317 байт)
- числа в инструкциях: +1
- виртуальные вызовы: +0x20 (слот 4)
- инструкций: 280 → 283
```diff
@@ -161,6 +161,11 @@
 test r12, r12
 je L
-mov rdi, qword ptr [rbp - 0xd8]
-call F
+test byte ptr [rbp - 0xa6], 1
+je L
+mov rax, qword ptr [D]
+mov rsi, qword ptr [rbp - 0xb0]
+mov rdi, qword ptr [rax]
+mov rax, qword ptr [rdi]
+call qword ptr [rax + 0x20]
 mov rdi, r14
 call F
@@ -168,5 +173,5 @@
 call F
 jmp L
-nop word ptr [rax + rax]
+nop word ptr cs:[rax + rax]
 cmp dil, 0x22
 movss xmm0, dword ptr [rbp - 0xb0]
@@ -176,5 +181,5 @@
 call F
 jmp L
-nop
+nop word ptr cs:[rax + rax]
 mov rax, qword ptr [rbp - 0xb0]
 test rax, rax
@@ -251,9 +256,7 @@
 jmp L
 nop word ptr [rax + rax]
-lea rax, [rbp - 0xb0]
-mov qword ptr [rbp - 0xd8], rax
 lea r14, [rbp - 0xc0]
```
(ещё 16 строк диффа: so-query.py fdiff libserver.so 0x4429ff0)

### изменена: 0x442a530 (1362 байт) | строки: "ApplyModifier"; "%f %f %f"
было: 0x44299a0 (1330 байт)
- поля объектов: +0xf0
- прямых вызовов: 30 → 31
- инструкций: 274 → 283
```diff
@@ -29,6 +29,16 @@
 cmp byte ptr [rax + 0x5d1], 3
 jne L
-mov rdi, rbx
-call F
+test rbx, rbx
+je L
+lea r12, [D]
+xor edi, edi
+mov r13, qword ptr [r12]
+mov rax, qword ptr [r13]
+mov r14, qword ptr [rax + 0xf0]
+call F
+mov rsi, rbx
+mov rdi, r13
+mov rdx, rax
+call r14
 test rax, rax
 je L
@@ -56,8 +66,7 @@
 test al, al
 je L
-lea r12, [D]
+mov rdi, qword ptr [r12]
 mov qword ptr [rbp - 0xc8], r10
 mov rsi, qword ptr [rbp - 0xd0]
-mov rdi, qword ptr [r12]
 mov rax, qword ptr [rdi]
 call qword ptr [rax + 0x138]
@@ -76,6 +85,6 @@
 mov qword ptr [rbp - 0xc8], rax
 lea r14, [rbp - 0xc0]
-mov qword ptr [rbp - 0x100], r10
-mov qword ptr [rbp - 0x108], r15
```
(ещё 13 строк диффа: so-query.py fdiff libserver.so 0x442a530)

### изменена: 0x4437b60 (877 байт)
было: 0x4435f80 (493 байт)
- константы из данных (числа логики): +0x00000000000000090000000000000000
- числа в инструкциях: +0xffffffff +0 +0 +0 +0 +0 +0 +0 (и ещё 17)
- прямых вызовов: 12 → 11
- инструкций: 111 → 152
```diff
@@ -17,5 +17,5 @@
 pop rbp
 ret
-nop
+nop dword ptr [rax + rax]
 lea rbx, [D]
 mov rdi, rbx
@@ -23,10 +23,51 @@
 test eax, eax
 je L
-lea r12, [D]
-mov rdi, r12
-call F
+pxor xmm0, xmm0
+mov eax, 0xffffffff
+movdqa xmm1, xmmword ptr [K:0x00000000000000090000000000000000]
+movups xmmword ptr [D], xmm0
+movups xmmword ptr [D], xmm0
+lea rsi, [D]
+movups xmmword ptr [D], xmm0
+movups xmmword ptr [D], xmm0
+movups xmmword ptr [D], xmm0
+movups xmmword ptr [D], xmm1
+movups xmmword ptr [D], xmm0
+mov qword ptr [D], rax
+mov qword ptr [D], 0
+mov qword ptr [D], 0
+mov qword ptr [D], 0
+mov qword ptr [D], 0
+mov qword ptr [D], 0
+mov qword ptr [D], 0
+mov qword ptr [D], 0
+mov qword ptr [D], 0
+mov qword ptr [D], 0
```
(ещё 53 строк диффа: so-query.py fdiff libserver.so 0x4437b60)

### изменена: 0x44417e0 (3650 байт) вызывается из: CDOTA_Modifier_Lua_Motion_Both::vfunc#127 | строки: "CDOTA_Modifier_Lua_Motion_Both"; "A lua-based motion controller controlling both vertical and horizontal."; "Script_SetPriority"; "Set the priority"; "nMotionPriority"; "Script_GetPriority"; "Get the priority"; "Script_ApplyHorizontalMotionController"
было: 0x443fa80 (3650 байт)
- строки: −"Called when the motion gets interrupted."
- инструкций: 925 → 925
```diff
@@ -579,14 +579,15 @@
 lea rdi, [T]
 mov dword ptr [rax + 0x48], 1
-lea rdx, [D]
-mov qword ptr [rax + 0x40], rdi
+mov qword ptr [rax + 0x38], rdi
+lea rdx, [T]
+lea rdi, [D]
+mov qword ptr [rax + 0x40], rdx
+mov qword ptr [rax + 0x28], rdi
+lea r14, [S:"Called when the motion gets interrupted."]
 mov rdi, rbx
-lea r14, [T]
-mov qword ptr [rax + 0x28], rdx
-mov qword ptr [rax + 0x38], r14
 call F
 lea rcx, [S:"Script_OnHorizontalMotionInterrupted"]
+xor edi, edi
 movq xmm0, qword ptr [D]
-lea rdi, [S:"Called when the motion gets interrupted."]
 cdqe
 movq xmm6, rcx
@@ -596,7 +597,6 @@
 add rax, qword ptr [r13 + 0x28]
 movsx ecx, byte ptr [rax + 0x1a]
-mov qword ptr [rax + 0x10], rdi
-xor edi, edi
 mov qword ptr [rax + 0x30], r13
+mov qword ptr [rax + 0x10], r14
 movups xmmword ptr [rax], xmm0
 mov word ptr [rax + 0x18], di
@@ -798,12 +798,12 @@
 jne L
 mov byte ptr [rax + 0x19], 0xc
```
(ещё 23 строк диффа: so-query.py fdiff libserver.so 0x44417e0)

### изменена: 0x4442ba0 (877 байт)
было: 0x4440e40 (493 байт)
- константы из данных (числа логики): +0x00000000000000090000000000000000
- числа в инструкциях: +0xffffffff +0 +0 +0 +0 +0 +0 +0 (и ещё 17)
- прямых вызовов: 12 → 11
- инструкций: 111 → 152
```diff
@@ -17,5 +17,5 @@
 pop rbp
 ret
-nop
+nop dword ptr [rax + rax]
 lea rbx, [D]
 mov rdi, rbx
@@ -23,10 +23,51 @@
 test eax, eax
 je L
-lea r12, [D]
-mov rdi, r12
-call F
+pxor xmm0, xmm0
+mov eax, 0xffffffff
+movdqa xmm1, xmmword ptr [K:0x00000000000000090000000000000000]
+movups xmmword ptr [D], xmm0
+movups xmmword ptr [D], xmm0
+lea rsi, [D]
+movups xmmword ptr [D], xmm0
+movups xmmword ptr [D], xmm0
+movups xmmword ptr [D], xmm0
+movups xmmword ptr [D], xmm1
+movups xmmword ptr [D], xmm0
+mov qword ptr [D], rax
+mov qword ptr [D], 0
+mov qword ptr [D], 0
+mov qword ptr [D], 0
+mov qword ptr [D], 0
+mov qword ptr [D], 0
+mov qword ptr [D], 0
+mov qword ptr [D], 0
+mov qword ptr [D], 0
+mov qword ptr [D], 0
```
(ещё 53 строк диффа: so-query.py fdiff libserver.so 0x4442ba0)

### изменена: 0x4443680 (2730 байт) вызывается из: CDOTA_Modifier_Lua_Horizontal_Motion::vfunc#127 | строки: "CDOTA_Modifier_Lua_Horizontal_Motion"; "A lua-based horizontal motion controller."; "Set the priority"; "Script_SetPriority"; "nMotionPriority"; "Get the priority"; "Script_GetPriority"; "Starts the horizontal motion controller effects for this buff.  Returns true if "
было: 0x44417a0 (2570 байт)
- числа в инструкциях: +0 +0 +1 +1 +1 +1 +0xff1d +0xff1d
- поля объектов: +0x18 +0x18 +0x20 +0x20 +0x20 +0x20 +0x20 +0x20 +0x20 +0x28 +0x28 +0x28 (и ещё 6)
- инструкций: 639 → 672
```diff
@@ -31,17 +31,26 @@
 test rax, rax
 jne L
-lea r12, [rbx + 0x20]
-mov rdi, r12
-call F
+movsxd r12, dword ptr [rbx + 0x20]
+cmp r12d, dword ptr [rbx + 0x30]
+mov eax, r12d
+je L
+mov rdx, qword ptr [rbx + 0x28]
+add eax, 1
+pxor xmm0, xmm0
+xor r8d, r8d
+mov dword ptr [rbx + 0x20], eax
+lea rax, [r12 + r12*4]
+lea rsi, [S:"Set the priority"]
+shl rax, 4
+add rdx, rax
+movups xmmword ptr [rdx], xmm0
+movups xmmword ptr [rdx + 0x28], xmm0
+movq xmm0, qword ptr [D]
+mov qword ptr [rdx + 0x10], 0
+mov qword ptr [rdx + 0x18], 0xff1d
+add rax, qword ptr [rbx + 0x28]
 lea rdx, [S:"Script_SetPriority"]
-xor r8d, r8d
-movq xmm0, qword ptr [D]
-lea rsi, [S:"Set the priority"]
-cdqe
 movq xmm1, rdx
-lea rax, [rax + rax*4]
 punpcklqdq xmm0, xmm1
-shl rax, 4
```
(ещё 193 строк диффа: so-query.py fdiff libserver.so 0x4443680)

### изменена: 0x4444180 (2730 байт) вызывается из: CDOTA_Modifier_Lua_Vertical_Motion::vfunc#127 | строки: "CDOTA_Modifier_Lua_Vertical_Motion"; "A lua-based vertical motion controller."; "Set the priority"; "Script_SetPriority"; "nMotionPriority"; "Get the priority"; "Script_GetPriority"; "Starts the vertical motion controller effects for this buff.  Returns true if su"
было: 0x4442200 (2570 байт)
- числа в инструкциях: +0 +0 +1 +1 +1 +1 +0xff1d +0xff1d
- поля объектов: +0x18 +0x18 +0x20 +0x20 +0x20 +0x20 +0x20 +0x20 +0x20 +0x28 +0x28 +0x28 (и ещё 6)
- инструкций: 639 → 672
```diff
@@ -31,17 +31,26 @@
 test rax, rax
 jne L
-lea r12, [rbx + 0x20]
-mov rdi, r12
-call F
+movsxd r12, dword ptr [rbx + 0x20]
+cmp r12d, dword ptr [rbx + 0x30]
+mov eax, r12d
+je L
+mov rdx, qword ptr [rbx + 0x28]
+add eax, 1
+pxor xmm0, xmm0
+xor r8d, r8d
+mov dword ptr [rbx + 0x20], eax
+lea rax, [r12 + r12*4]
+lea rsi, [S:"Set the priority"]
+shl rax, 4
+add rdx, rax
+movups xmmword ptr [rdx], xmm0
+movups xmmword ptr [rdx + 0x28], xmm0
+movq xmm0, qword ptr [D]
+mov qword ptr [rdx + 0x10], 0
+mov qword ptr [rdx + 0x18], 0xff1d
+add rax, qword ptr [rbx + 0x28]
 lea rdx, [S:"Script_SetPriority"]
-xor r8d, r8d
-movq xmm0, qword ptr [D]
-lea rsi, [S:"Set the priority"]
-cdqe
 movq xmm1, rdx
-lea rax, [rax + rax*4]
 punpcklqdq xmm0, xmm1
-shl rax, 4
```
(ещё 193 строк диффа: so-query.py fdiff libserver.so 0x4444180)

### изменена: 0x4448300 (460 байт) | строки: "CDOTA_Item_Lua"
было: 0x4445f10 (500 байт)
- прямых вызовов: 12 → 11
- инструкций: 121 → 103
```diff
@@ -1,16 +1,2 @@
-push rbp
-mov rbp, rsp
-push rbx
-sub rsp, 8
-call F
-mov rdi, rax
-mov rbx, rax
-call F
-mov rdi, rbx
-mov rbx, qword ptr [rbp - 8]
-mov qword ptr [D], rax
-mov rsi, rax
-leave
-jmp F
 push rbp
 mov rbp, rsp
@@ -20,6 +6,7 @@
 lea r12, [D]
 push rbx
-mov rbx, rdi
 sub rsp, 0x10
+call F
+mov rbx, rax
 movzx eax, byte ptr [D]
 test al, al
@@ -27,6 +14,8 @@
 cmp byte ptr [D], 0
 je L
+mov qword ptr [D], r12
 add rsp, 0x10
-mov rax, r12
+mov rsi, r12
+mov rdi, rbx
```
(ещё 54 строк диффа: so-query.py fdiff libserver.so 0x4448300)

### изменена: 0x46ef570 (101 байт) CDOTA_Modifier_Sniper_Headshot::vfunc#97
было: 0x46ed570 (67 байт)
- числа в инструкциях: +0 −0x409 −0x401 −0x411
- поля объектов: +0x1250 +0x1258
- инструкций: 7 → 13
```diff
@@ -1,7 +1,13 @@
-mov qword ptr [rdi + 0xe0], 0x409
+lea rax, [T]
 mov qword ptr [rdi + 0xe8], 0
-mov qword ptr [rdi + 0x130], 0x401
+mov qword ptr [rdi + 0xe0], rax
+lea rax, [T]
+mov qword ptr [rdi + 0x130], rax
+lea rax, [T]
+mov qword ptr [rdi + 0x1ab0], rax
+lea rax, [T]
 mov qword ptr [rdi + 0x138], 0
-mov qword ptr [rdi + 0x1ab0], 0x411
 mov qword ptr [rdi + 0x1ab8], 0
+mov qword ptr [rdi + 0x1250], rax
+mov qword ptr [rdi + 0x1258], 0
 ret
```

### изменена: 0x4713460 (128 байт)
было: 0x47114c0 (52 байт)
- числа в инструкциях: +1 +1 +1
- инструкций: 19 → 45
```diff
@@ -1,2 +1,28 @@
+mov edx, dword ptr [rdi]
+test edx, edx
+jle L
+mov rcx, qword ptr [rdi + 8]
+movsxd r8, edx
+xor eax, eax
+cmp word ptr [rcx + rax*2], si
+jne L
+lea rsi, [rcx + rax*2]
+sub edx, 1
+cmp edx, eax
+je L
+movsxd rdx, edx
+movzx eax, word ptr [rcx + rdx*2]
+mov word ptr [rsi], ax
+mov eax, dword ptr [rdi]
+lea edx, [rax - 1]
+mov dword ptr [rdi], edx
+mov eax, 1
+ret
+nop word ptr [rax + rax]
+add rax, 1
+cmp r8, rax
+jne L
+xor eax, eax
+ret
 push rbp
 xor edx, edx
```

### изменена: 0x472cf30 (123 байт) CModifierFactory<CDOTA_Modifier_Sniper_Headshot>::vfunc#0
было: 0x472b140 (97 байт)
- числа в инструкциях: +0x1b30 +0x1b30 +0 +0 +0x410 −0x1b18 −0x1b18 −0x428
- поля объектов: +0x1b18 +0x1b20 +0x1b28 −0x1b12
- инструкций: 25 → 27
```diff
@@ -1,9 +1,9 @@
 push rbp
-mov edi, 0x1b18
+mov edi, 0x1b30
 mov rbp, rsp
 push rbx
 sub rsp, 0x18
 call F
-mov edx, 0x1b18
+mov edx, 0x1b30
 xor esi, esi
 mov rdi, rax
@@ -14,11 +14,13 @@
 call F
 lea rax, [D]
-mov byte ptr [rbx + 0x1b12], 0
+mov qword ptr [rbx + 0x1b18], 0
 mov qword ptr [rbx], rax
-add rax, 0x428
+add rax, 0x410
 mov qword ptr [rbx + 0x10], rax
 mov eax, 0xffffffff
 mov word ptr [rbx + 0x1b10], ax
 mov rax, rbx
+mov qword ptr [rbx + 0x1b20], 0
+mov qword ptr [rbx + 0x1b28], 0
 mov rbx, qword ptr [rbp - 8]
 leave
```

### изменена: 0x47462c0 (448 байт) CDOTA_Modifier_TemplarAssassin_RefractionDamage::vfunc#130 | строки: "Hero_TemplarAssassin.Refraction.Damage"
было: 0x4743e60 (1138 байт)
- строки: −"first_hit" −"attack_index" −"original_damage"
- числа в инструкциях: −1 −1 −1 −1 −1 −-1 −-2 −9 (и ещё 16)
- виртуальные вызовы: −0xb98 (слот 371)
- поля объектов: −0x44 −0xcc −0xcc −0x10 −0x10 −0x10 −0x5d1 −0x3c −0x1b10 −0x1b18 −0x38 −0x38 (и ещё 1)
- прямых вызовов: 26 → 9
- инструкций: 291 → 124
```diff
@@ -123,169 +123,2 @@
 call rax
 jmp L
-push rbp
-mov rbp, rsp
-push r15
-push r14
-push r13
-mov r13, rsi
-push r12
-mov r12, rdx
-push rbx
-mov rbx, rdi
-sub rsp, 0x78
-call F
-movzx esi, word ptr [r12 + 0x44]
-mov rdi, rax
-call F
-test rax, rax
-je L
-mov rdi, r13
-mov r15, rax
-call F
-test rax, rax
-je L
-mov esi, dword ptr [r12 + 0xcc]
-cmp esi, -1
-je L
-mov rdi, qword ptr [D]
-test rdi, rdi
-je L
-cmp esi, -2
-je L
-movzx eax, word ptr [r12 + 0xcc]
```
(ещё 136 строк диффа: so-query.py fdiff libserver.so 0x47462c0)

### изменена: 0x4747820 (1156 байт) вызывается из: CDOTA_Modifier_Sniper_Headshot::vfunc#97 | строки: "modifier_sniper_headshot_slow"; "duration"; "modifier_absolute_no_cc"; "modifier_sniper_headshot_knockback"; "center_x"; "center_y"; "knockback_duration"; "should_stun"
было: 0x4744950 (1155 байт)
- числа в инструкциях: −0
- поля объектов: −0x1b10 −0x1b12
- прямых вызовов: 39 → 40
- инструкций: 279 → 281
```diff
@@ -78,8 +78,8 @@
 test al, al
 jne L
-movzx eax, word ptr [rbx + 0x1b10]
-cmp word ptr [r13 + 0x44], ax
-jne L
-cmp byte ptr [rbx + 0x1b12], 0
+movzx esi, word ptr [r13 + 0x44]
+lea rdi, [rbx + 0x1b18]
+call F
+test al, al
 je L
 lea rax, [rbp - 0x70]
@@ -203,10 +203,10 @@
 mov rdi, r12
 movss xmm0, dword ptr [rax + 4]
-movaps xmm4, xmm0
+movaps xmm3, xmm0
 movss xmm0, dword ptr [rax]
-subss xmm4, dword ptr [r13 + 4]
+subss xmm3, dword ptr [r13 + 4]
 subss xmm0, dword ptr [r13]
 lea r13, [rbp - 0x50]
-movd r15d, xmm4
+movd r15d, xmm3
 movss dword ptr [rbp - 0x80], xmm0
 call F
@@ -215,11 +215,11 @@
 xor edx, edx
 addss xmm0, dword ptr [rax]
-movd xmm5, r15d
-mov rdi, r12
-addss xmm5, dword ptr [rax + 4]
+movd xmm4, r15d
```
(ещё 27 строк диффа: so-query.py fdiff libserver.so 0x4747820)

### изменена: 0x476c160 (682 байт) вызывается из: CDOTA_Modifier_Viper_PoisonAttack::vfunc#97 | строки: "max_stacks"; "modifier_viper_poison_attack_slow"; "duration"; "hero_viper.PoisonAttack.Target"
было: 0x4769fe0 (771 байт)
- числа в инструкциях: −1 −1
- поля объектов: −0x1b00 −0x1b00 −0x1b00 −0x1b08
- прямых вызовов: 21 → 22
- инструкций: 189 → 170
```diff
@@ -52,23 +52,9 @@
 cmp rax, rcx
 jne L
-mov edx, dword ptr [rbx + 0x1b00]
 movzx esi, word ptr [r13 + 0x44]
-test edx, edx
-jle L
-mov rcx, qword ptr [rbx + 0x1b08]
-movsxd rdi, edx
-xor eax, eax
-cmp si, word ptr [rcx + rax*2]
-jne L
-lea rsi, [rcx + rax*2]
-sub edx, 1
-cmp edx, eax
+lea rdi, [rbx + 0x1b00]
+call F
+test al, al
 je L
-movsxd rdx, edx
-movzx eax, word ptr [rcx + rdx*2]
-mov word ptr [rsi], ax
-mov eax, dword ptr [rbx + 0x1b00]
-lea edx, [rax - 1]
-mov dword ptr [rbx + 0x1b00], edx
 mov rdi, r13
 call F
@@ -169,9 +155,4 @@
 call F
 jmp L
-nop dword ptr [rax]
-add rax, 1
-cmp rdi, rax
-jne L
```
(ещё 3 строк диффа: so-query.py fdiff libserver.so 0x476c160)

### изменена: 0x479a700 (750 байт) вызывается из: CDOTA_Modifier_Sniper_Headshot::vfunc#97 | строки: "modifier_sniper_take_aim_bonus"; "sniper_take_aim"; "headshot_chance"
было: 0x476a2f0 (713 байт)
- числа в инструкциях: −0 −0
- поля объектов: +0x1b18 +0x1b20 −0x1b12 −0x1b12 −0x1b12
- прямых вызовов: 14 → 15
- инструкций: 175 → 186
```diff
@@ -58,7 +58,13 @@
 ret
 nop
-cmp byte ptr [rsi + 0x1b12], 0
-pxor xmm0, xmm0
+mov edx, dword ptr [rsi + 0x1b18]
+test edx, edx
+jle L
+mov rsi, qword ptr [rsi + 0x1b20]
+movsxd rcx, edx
+xor edx, edx
+cmp ax, word ptr [rsi + rdx*2]
 jne L
+movss xmm0, dword ptr [r13 + 0x1b0c]
 movss dword ptr [rbx + 4], xmm0
 pxor xmm0, xmm0
@@ -66,5 +72,5 @@
 movups xmmword ptr [rbx + 8], xmm0
 jmp L
-nop word ptr cs:[rax + rax]
+nop word ptr [rax + rax]
 xor edx, edx
 cmp rax, rdx
@@ -135,13 +141,11 @@
 je L
 movzx eax, word ptr [r12 + 0x44]
-mov byte ptr [r13 + 0x1b12], 0
 mov word ptr [r13 + 0x1b10], ax
 jmp L
-cmp ax, -1
-je L
-mov word ptr [r13 + 0x1b10], ax
-mov byte ptr [r13 + 0x1b12], 1
-nop word ptr cs:[rax + rax]
```
(ещё 20 строк диффа: so-query.py fdiff libserver.so 0x479a700)

### изменена: 0x476ef90 (7035 байт) CDOTA_Ability_Tinker_Keen_Teleport::OnAbilityPhaseStart | строки: "maximum_distance"; "good_healer_6"; "npc_dota_watch_tower_bottom"; "npc_dota_watch_tower_top"; "tower1"; "minimum_distance"; "particles/items2_fx/teleport_start.vpcf"; "particles/items2_fx/teleport_end.vpcf"
было: 0x476d140 (7099 байт)
- числа в инструкциях: −-1 −-2 −9 −0x3f −0x1ff −0x70
- поля объектов: −0x10
- прямых вызовов: 167 → 168
- инструкций: 1401 → 1386
```diff
@@ -149,8 +149,8 @@
 cmp eax, -1
 je L
+cmp eax, -2
 mov rcx, qword ptr [D]
+je L
 test rcx, rcx
-je L
-cmp eax, -2
 je L
 mov rdx, rax
@@ -196,26 +196,11 @@
 cmp r14, r13
 je L
-nop dword ptr [rax]
 mov eax, dword ptr [r13]
-cmp eax, -1
-je L
-cmp eax, -2
-mov rcx, qword ptr [D]
-je L
-test rcx, rcx
-je L
-mov rdx, rax
-shr rdx, 9
-and edx, 0x3f
-mov rdx, qword ptr [rcx + rdx*8]
-test rdx, rdx
-je L
-mov ecx, eax
-and ecx, 0x1ff
-imul rcx, rcx, 0x70
-add rdx, rcx
-cmp eax, dword ptr [rdx + 0x10]
```
(ещё 55 строк диффа: so-query.py fdiff libserver.so 0x476ef90)

### изменена: 0x4790440 (965 байт) CDOTA_Unit_TargetDummy::vfunc#263
было: 0x4785ed0 (997 байт)
- числа в инструкциях: +1 +1 −0 −0x3fffffff
- виртуальные вызовы: −0x20 (слот 4)
- инструкций: 213 → 202
```diff
@@ -4,5 +4,4 @@
 mov edx, 8
 mov rbp, rsp
-push r14
 push r13
 push r12
@@ -11,5 +10,5 @@
 push rbx
 mov rbx, rdi
-sub rsp, 0x60
+sub rsp, 0x58
 mov rax, qword ptr [rdi]
 movss xmm1, dword ptr [K:-999]
@@ -53,5 +52,5 @@
 mov rdi, rbx
 call F
-add rsp, 0x60
+add rsp, 0x58
 mov rsi, r12
 mov rdi, rbx
@@ -59,5 +58,4 @@
 pop r12
 pop r13
-pop r14
 pop rbp
 jmp F
@@ -69,34 +67,35 @@
 jp L
 je L
-lea r13, [rbp - 0x58]
 xor edx, edx
+mov esi, 1
+movss dword ptr [rbp - 0x64], xmm0
 pxor xmm1, xmm1
```
(ещё 164 строк диффа: so-query.py fdiff libserver.so 0x4790440)

### изменена: 0x4795df0 (1806 байт) CDOTA_Modifier_Animation_TailSpin::OnIntervalThink | строки: "attach_tail1"; "attach_tail2"; "attach_tail3"; "attach_tail4"; "attach_tail5"; "knockback_duration"; "knockback_distance"; "modifier_knockback"
было: 0x4793ff0 (1826 байт)
- инструкций: 412 → 406
```diff
@@ -94,6 +94,6 @@
 call F
 push 0
-mov r8, r12
 mov r9d, 2
+mov r8, r12
 push 0
 mov rdi, rax
@@ -121,8 +121,8 @@
 call F
 push 0
-mov r8, r12
 mov rdx, r15
-push 0
 mov r9d, 2
+push 0
+mov r8, r12
 mov rdi, rax
 push 0x10
@@ -147,9 +147,9 @@
 call F
 push 0
-mov r8, r12
 mov rdx, r14
+mov r9d, 2
 push 0
 mov esi, r15d
-mov r9d, 2
+mov r8, r12
 mov rdi, rax
 push 0x10
@@ -173,9 +173,9 @@
 call F
 push 0
```
(ещё 255 строк диффа: so-query.py fdiff libserver.so 0x4795df0)

### изменена: 0x479a9f0 (670 байт) вызывается из: CDOTA_Modifier_Viper_PoisonAttack::vfunc#97 | строки: "particles/units/heroes/hero_viper/viper_poison_attack.vpcf"; "hero_viper.poisonAttack.Cast"
было: 0x47988c0 (717 байт)
- числа в инструкциях: −1 −1
- поля объектов: −0x1b00 −0x1b00 −0x1b10 −0x1b08 −0x38
- инструкций: 180 → 172
```diff
@@ -15,8 +15,8 @@
 cmp esi, -1
 je L
+cmp esi, -2
 mov rdi, qword ptr [D]
+je L
 test rdi, rdi
-je L
-cmp esi, -2
 je L
 movzx edx, word ptr [rbx + 0xcc]
@@ -167,14 +167,6 @@
 mov esi, 1
 call qword ptr [rax + 0x978]
-movsxd r13, dword ptr [r12 + 0x1b00]
-cmp r13d, dword ptr [r12 + 0x1b10]
-je L
-add dword ptr [r12 + 0x1b00], 1
-mov rax, qword ptr [r12 + 0x1b08]
-movzx edx, word ptr [rbx + 0x38]
-mov word ptr [rax + r13*2], dx
-jmp L
-lea rdi, [r12 + 0x1b08]
-mov esi, 1
+lea rsi, [rbx + 0x38]
+lea rdi, [r12 + 0x1b00]
 call F
 jmp L
```

### изменена: 0x47a4d20 (3310 байт) CDOTA_RoshanSpawner::vfunc#237 | строки: "Unit"; "UseNeutralCreepBehavior"; "npc_dota_roshan"; "particles/neutral_fx/roshan_timer.vpcf"
было: 0x47a2c20 (3374 байт)
- числа в инструкциях: −-1 −-2 −9 −0x3f −0x1ff −0x70
- поля объектов: −0x10 −0x794 −0x794
- прямых вызовов: 75 → 76
- инструкций: 665 → 648
```diff
@@ -9,6 +9,6 @@
 push rbx
 sub rsp, 0xd8
-lea r15, [D]
-mov rdx, qword ptr [r15]
+lea r14, [D]
+mov rdx, qword ptr [r14]
 movsxd rax, dword ptr [rdx + 0x418]
 cmp eax, 0xc
@@ -35,5 +35,5 @@
 mov rdi, rbx
 call F
-lea r14, [rbp - 0x90]
+lea r15, [rbp - 0x90]
 mov edx, 1
 mov rdi, rbx
@@ -42,5 +42,5 @@
 mov edx, 2
 xor esi, esi
-mov rdi, r14
+mov rdi, r15
 lea rax, [T]
 mov qword ptr [rbp - 0xc0], 0
@@ -54,5 +54,5 @@
 mov qword ptr [rbp - 0x48], r12
 call F
-mov r8, r14
+mov r8, r15
 mov rcx, rbx
 xor edx, edx
@@ -62,5 +62,5 @@
 movss xmm1, dword ptr [rax + 8]
 call F
-mov rdi, r14
```
(ещё 252 строк диффа: so-query.py fdiff libserver.so 0x47a4d20)

### изменена: 0x47b6410 (4205 байт) | строки: "m_pszNetworkedSoundLoop"; "char[256]"; "char"; "%s%s[%d]"; "m_nLoopingSoundParity"; "int"; "int32"; "CDOTA_Unit_LoopingSound"
было: 0x47b4350 (4205 байт)
- числа в инструкциях: +0x706f6f −0x5bd1e995 −0x27039e0d
- прямых вызовов: 100 → 101
- инструкций: 863 → 864
```diff
@@ -66,7 +66,9 @@
 mov esi, eax
 call F
+lea rdi, [D]
+mov esi, eax
+call F
 mov edi, 0x158
-imul eax, eax, 0x5bd1e995
-xor eax, 0x27039e0d
+xor eax, 0x706f6f
 imul eax, eax, 0x5bd1e995
 mov edx, eax
@@ -194,5 +196,4 @@
 jns L
 jmp L
-nop dword ptr [rax + rax]
 sub r14d, 1
 jb L
```

### изменена: 0x47d7180 (123 байт) CDOTA_Modifier_Enchantress_Impetus::vfunc#97
было: 0x47d50c0 (98 байт)
- числа в инструкциях: +0
- поля объектов: +0x11d0 +0x11d8
- инструкций: 12 → 15
```diff
@@ -5,8 +5,11 @@
 mov qword ptr [rdi + 0xd70], rax
 lea rax, [T]
+mov qword ptr [rdi + 0x1250], rax
+lea rax, [T]
 mov qword ptr [rdi + 0xd78], 0
-mov qword ptr [rdi + 0x1250], rax
 mov qword ptr [rdi + 0x1258], 0
 mov qword ptr [rdi + 0x10b0], 0x401
 mov qword ptr [rdi + 0x10b8], 0
+mov qword ptr [rdi + 0x11d0], rax
+mov qword ptr [rdi + 0x11d8], 0
 ret
```

### изменена: 0x47f80d0 (323 байт) CDOTA_Modifier_Enchantress_Impetus::vfunc#128 | строки: "modifier_phantom_assassin_stiflingdagger_caster"; "impetus"
было: 0x47d5130 (86 байт)
- строки: +"modifier_phantom_assassin_stiflingdagger_caster"
- числа в инструкциях: +8 +0 +0xffffffff
- виртуальные вызовы: +0xad0 (слот 346) +0x940 (слот 296)
- поля объектов: +0x1248 +0x7c8 +0xd68
- прямых вызовов: 0 → 13
- инструкций: 20 → 83
```diff
@@ -1,20 +1,83 @@
-mov edx, dword ptr [rdx + 0xc]
-mov rax, rdi
-cmp edx, 0x6a9
+push rbp
+mov rbp, rsp
+push r13
+push r12
+mov r12, rsi
+push rbx
+mov rbx, rdi
+sub rsp, 8
+mov eax, dword ptr [rdx + 0xc]
+cmp eax, 0x6a9
 je L
-jle L
-cmp edx, 0x6de
+jg L
+sub eax, 0x5df
+cmp eax, 2
+jbe L
+mov qword ptr [rbx], 2
+pxor xmm0, xmm0
+movups xmmword ptr [rbx + 8], xmm0
+add rsp, 8
+mov rax, rbx
+pop rbx
+pop r12
+pop r13
+pop rbp
+ret
+nop word ptr cs:[rax + rax]
+cmp eax, 0x6de
+jne L
```
(ещё 67 строк диффа: so-query.py fdiff libserver.so 0x47f80d0)

### изменена: 0x47dcb80 (240 байт) CDOTA_Modifier_Chen_Zealot_Aura::GetAuraEntityReject | строки: "modifier_chen_zealot_buff"
было: 0x47dab10 (155 байт)
- строки: +"modifier_chen_zealot_buff"
- числа в инструкциях: +0 +1 +1 +0x1f
- поля объектов: +0x175a +0xd8d +0x1248
- прямых вызовов: 5 → 7
- инструкций: 51 → 72
```diff
@@ -1,4 +1,5 @@
 push rbp
 mov rbp, rsp
+push r14
 push r13
 mov r13, rdi
@@ -6,5 +7,4 @@
 push rbx
 mov rbx, rsi
-sub rsp, 8
 call F
 mov r12, rax
@@ -28,14 +28,21 @@
 test al, 1
 jne L
+cmp byte ptr [rbx + 0x175a], 0
+jne L
+movzx r13d, byte ptr [rbx + 0xd8d]
+test r13b, r13b
+jne L
 test eax, 0x110
 je L
-nop
-mov eax, 1
-add rsp, 8
+nop dword ptr [rax + rax]
+mov r13d, 1
 pop rbx
+mov eax, r13d
 pop r12
 pop r13
+pop r14
 pop rbp
 ret
```
(ещё 29 строк диффа: so-query.py fdiff libserver.so 0x47dcb80)

### изменена: 0x4853b30 (1199 байт) CDOTA_Modifier_Batrider_FlamingLasso::vfunc#2 | строки: "modifier_faceless_void_chronosphere_freeze"; "modifier_enigma_black_hole_pull"
было: 0x48518b0 (1111 байт)
- числа в инструкциях: +-1 +-2 +9 +0x3f +0x1ff +0x70
- поля объектов: +0x1b14 +0x1b14 +0x10
- прямых вызовов: 20 → 19
- инструкций: 267 → 287
```diff
@@ -48,11 +48,26 @@
 call F
 movss dword ptr [rbp - 0x64], xmm0
-lea r13, [rbx + 0x1b14]
+mov ecx, dword ptr [rbx + 0x1b14]
+cmp ecx, -1
+je L
+mov rsi, qword ptr [D]
+test rsi, rsi
+je L
+cmp ecx, -2
+je L
+movzx eax, word ptr [rbx + 0x1b14]
+mov rdx, rax
+shr rdx, 9
+and edx, 0x3f
+mov rdx, qword ptr [rsi + rdx*8]
+test rdx, rdx
+je L
+and eax, 0x1ff
+imul rax, rax, 0x70
+add rax, rdx
+cmp ecx, dword ptr [rax + 0x10]
+jne L
+mov r13, qword ptr [rax]
 mov rdi, r13
-call F
-test rax, rax
-mov rdi, rax
-je L
-mov rdi, qword ptr [rax]
 call F
 pxor xmm0, xmm0
@@ -82,4 +97,5 @@
```
(ещё 88 строк диффа: so-query.py fdiff libserver.so 0x4853b30)

### изменена: 0x4854fa0 (392 байт) вызывается из: CDOTA_Modifier_Broodmother_Spider_HP::vfunc#97
было: 0x4852cc0 (475 байт)
- числа в инструкциях: −1 −3
- поля объектов: −0x5d1 −0xd3c −0xd58
- прямых вызовов: 6 → 4
- инструкций: 125 → 103
```diff
@@ -64,17 +64,4 @@
 cmp ecx, dword ptr [rax + 0x10]
 jne L
-mov rax, qword ptr [rax]
-test rax, rax
-je L
-cmp byte ptr [rax + 0x5d1], 3
-jne L
-test byte ptr [rax + 0xd3c], 1
-je L
-cmp byte ptr [rax + 0x175a], 0
-jne L
-lea rdi, [r12 + 0xd0]
-call F
-test rax, rax
-je L
 mov r13, qword ptr [rax]
 test r13, r13
@@ -83,11 +70,7 @@
 jne L
 test byte ptr [r13 + 0xd3c], 1
+je L
+cmp byte ptr [r13 + 0x175a], 0
 jne L
-mov rax, qword ptr [r13]
-lea rdx, [T]
-mov rax, qword ptr [rax + 0xd58]
-cmp rax, rdx
-jne L
-xor r13d, r13d
 mov rdi, r12
 call F
@@ -110,4 +93,5 @@
 call F
```
(ещё 13 строк диффа: so-query.py fdiff libserver.so 0x4854fa0)

### изменена: 0x485cbc0 (3963 байт) | строки: "PlayerID_t"
было: 0x485b420 (1083 байт)
- константы из данных (числа логики): +0x00000000000000090000000000000000 +0x00000000000000090000000000000000 +0x00000000000000090000000000000000 +0x00000000000000090000000000000000
- числа в инструкциях: +0xffffffff +0xffffffff +0xffffffff +0xffffffff +0 +0 +0 +0 (и ещё 100)
- прямых вызовов: 12 → 40
- инструкций: 229 → 677
```diff
@@ -1,2 +1,450 @@
+push rbp
+mov rbp, rsp
+push rbx
+sub rsp, 8
+movzx eax, byte ptr [D]
+test al, al
+je L
+mov rax, qword ptr [D]
+test rax, rax
+je L
+mov rbx, qword ptr [rbp - 8]
+leave
+ret
+nop word ptr [rax + rax]
+lea rbx, [D]
+mov rdi, rbx
+call F
+test eax, eax
+je L
+pxor xmm0, xmm0
+mov eax, 0xffffffff
+movdqa xmm1, xmmword ptr [K:0x00000000000000090000000000000000]
+movups xmmword ptr [D], xmm0
+movups xmmword ptr [D], xmm0
+lea rsi, [D]
+movups xmmword ptr [D], xmm0
+movups xmmword ptr [D], xmm0
+movups xmmword ptr [D], xmm0
+movups xmmword ptr [D], xmm1
+movups xmmword ptr [D], xmm0
+mov qword ptr [D], rax
+mov qword ptr [D], 0
+mov qword ptr [D], 0
```
(ещё 417 строк диффа: so-query.py fdiff libserver.so 0x485cbc0)

### изменена: 0x4868c70 (477 байт) вызывается из: CDOTA_Ability_Chen_Zealot::OnHeroLevelUp, CDOTA_Ability_Chen_Zealot::OnAbilityUpgrade | строки: "modifier_chen_zealot_creep"; "modifier_chen_zealot_buff"
было: 0x4866990 (477 байт)
- инструкций: 128 → 128
```diff
@@ -40,5 +40,5 @@
 mov rcx, r13
 xor ebx, ebx
-push 0x12
+push 0x13
 lea r14, [S:"modifier_chen_zealot_creep"]
 call F
```

### изменена: 0x48aad90 (899 байт) | строки: "scepter_brewling_items"; "<NoAbilityName>"; "modifier_brewmaster_primal_split_scepter_item"; "original_item"; "brewling_item"
было: 0x48b3800 (860 байт)
- числа в инструкциях: −1 −1 −1 −1
- инструкций: 216 → 216
```diff
@@ -9,5 +9,5 @@
 mov r12, rdi
 push rbx
-sub rsp, 0x58
+sub rsp, 0x68
 call F
 test rax, rax
@@ -55,5 +55,5 @@
 call F
 cmp eax, 5
-mov dword ptr [rbp - 0x78], eax
+mov dword ptr [rbp - 0x88], eax
 jbe L
 lea rsp, [rbp - 0x28]
@@ -65,5 +65,5 @@
 pop rbp
 ret
-nop dword ptr [rax + rax]
+nop
 mov rdi, r13
 call F
@@ -95,5 +95,5 @@
 push 0
 push 0
-mov ecx, dword ptr [rbp - 0x78]
+mov ecx, dword ptr [rbp - 0x88]
 call F
 add rsp, 0x20
@@ -116,10 +116,10 @@
 mov rdi, rax
 call F
-mov ecx, dword ptr [rbp - 0x78]
+mov ecx, dword ptr [rbp - 0x88]
 cmp eax, ecx
```
(ещё 94 строк диффа: so-query.py fdiff libserver.so 0x48aad90)

### изменена: 0x48aed40 (1040 байт) CDOTA_Ability_Primal_Companion::OnSpellStart | строки: "brewmaster_primal_split"; "brewmaster_drunken_brawler"; "npc_dota_brewmaster_fire_%1d"; "npc_dota_brewmaster_earth_%1d"; "modifier_brewmaster_primal_companion"; "npc_dota_brewmaster_storm_%1d"
было: 0x48b43f0 (1136 байт)
- числа в инструкциях: −1
- поля объектов: −0x1afc
- прямых вызовов: 33 → 29
- инструкций: 259 → 239
```diff
@@ -238,22 +238,2 @@
 movss xmm1, dword ptr [rbp - 0x148]
 jmp L
-mov rbx, qword ptr [rbp - 0x200]
-mov rdi, rbx
-call F
-pxor xmm0, xmm0
-mov edx, 1
-xor edi, edi
-cvtsi2ss xmm0, dword ptr [rbx + 0x1afc]
-mov rsi, rax
-call F
-mov rdi, rbx
-movss dword ptr [rbp - 0x1d8], xmm0
-call F
-movss xmm0, dword ptr [rbp - 0x1d8]
-xor edx, edx
-lea rdi, [D]
-mov rsi, rax
-cvttss2si ecx, xmm0
-call F
-mov eax, dword ptr [0xd3c]
-ud2
```

### изменена: 0x48b8350 (4111 байт) CDOTA_Ability_Enchantress_Enchant::OnSpellStart | строки: "dominate_duration"; "slow_duration"; "modifier_enchantress_enchant_controlled"; "modifier_dominated"; "enchanted_creep"; "xp_gain_pct"; "modifier_kill"; "duration"
было: 0x48c1fc0 (4055 байт)
- числа в инструкциях: −1 −1 −1 −1
- поля объектов: −0x860 −0x860 −0x860 −0x868 −0x870
- инструкций: 887 → 889
```diff
@@ -7,5 +7,5 @@
 push rbx
 mov rbx, rdi
-sub rsp, 0x1a8
+sub rsp, 0x1c8
 call F
 test rax, rax
@@ -23,10 +23,10 @@
 xor edx, edx
 mov rdi, rbx
-movss dword ptr [rbp - 0x1b0], xmm0
+movss dword ptr [rbp - 0x1c0], xmm0
 movss xmm0, dword ptr [K:-1]
 lea rsi, [S:"slow_duration"]
 call F
 test byte ptr [r12 + 0x1249], 2
-movss dword ptr [rbp - 0x1a4], xmm0
+movss dword ptr [rbp - 0x1b4], xmm0
 je L
 lea rsp, [rbp - 0x28]
@@ -46,5 +46,5 @@
 call F
 test al, al
-mov r15d, eax
+mov r14d, eax
 jne L
 mov eax, dword ptr [r12 + 0xd3c]
@@ -69,5 +69,5 @@
 mov rdi, r12
 mov rsi, rax
-mov qword ptr [rbp - 0x1c0], rax
+mov qword ptr [rbp - 0x1e0], rax
 call F
 test rax, rax
```
(ещё 774 строк диффа: so-query.py fdiff libserver.so 0x48b8350)

### изменена: 0x48cb530 (1205 байт) вызывается из: CDOTA_Modifier_Enchantress_Impetus::vfunc#97 | строки: "modifier_phantom_assassin_stiflingdagger_caster"; "particles/units/heroes/hero_enchantress/enchantress_impetus.vpcf"; "Hero_Enchantress.Impetus"
было: 0x48c9000 (1109 байт)
- числа в инструкциях: +1 +1
- поля объектов: +0xd3c +0xd58
- прямых вызовов: 22 → 25
- инструкций: 260 → 282
```diff
@@ -158,4 +158,16 @@
 mov rdi, r14
 call F
+test rax, rax
+mov rdi, rax
+je L
+test byte ptr [rax + 0xd3c], 1
+jne L
+mov rax, qword ptr [rax]
+lea rdx, [T]
+mov rax, qword ptr [rax + 0xd58]
+cmp rax, rdx
+jne L
+mov rdi, r14
+call F
 lea rdi, [rbp - 0x60]
 mov esi, 0xa
@@ -164,14 +176,14 @@
 call F
 jmp L
-nop
-test rax, rax
-jne L
-mov r9d, dword ptr [r13 + 0xd0]
-cmp r9d, -1
-je L
+nop dword ptr [rax]
+test rax, rax
+jne L
+mov r9d, dword ptr [r13 + 0xd0]
+cmp r9d, -1
+je L
+cmp r9d, -2
 mov r8, qword ptr [D]
```
(ещё 28 строк диффа: so-query.py fdiff libserver.so 0x48cb530)

### изменена: 0x48d3fd0 (6248 байт) вызывается из: CDOTA_Ability_Dazzle_NothlProjection::OnSpellStart | строки: "shadow_wave_cdr"; "healing_amp"; "leash_start"; "base_leash_pull"; "leash_increase"; "modifier_dazzle_nothl_projection_soul_clone"; "<NoAbilityName>"; "dazzle_nothl_projection_end"
было: 0x48d1bd0 (6232 байт)
- числа в инструкциях: −1 −1
- поля объектов: +0x7b0 +0x7b0
- инструкций: 1237 → 1239
```diff
@@ -158,6 +158,8 @@
 je L
 cmp byte ptr [r12 + 0x818], 0
-je L
-jmp L
+jne L
+mov eax, dword ptr [r12 + 0x7b0]
+cmp dword ptr [r14 + 0x7b0], eax
+jge L
 nop dword ptr [rax]
 xor esi, esi
@@ -1107,11 +1109,14 @@
 mov dword ptr [r12 + 0x85c], eax
 jmp L
+lea rdx, [rbp - 0x138]
 xor eax, eax
-mov esi, 1
 pxor xmm1, xmm1
-movss dword ptr [rbp - 0x1c8], xmm0
-lea rdi, [rbp - 0x130]
+movss dword ptr [rbp - 0x1d8], xmm0
+mov rdi, rdx
 movaps xmmword ptr [rbp - 0x120], xmm1
+lea rsi, [rbp - 0x180]
+mov qword ptr [rbp - 0x1c8], rdx
 mov word ptr [rbp - 0x104], ax
+mov dword ptr [rbp - 0x180], 0x7dc
 mov qword ptr [rbp - 0x140], 1
 mov qword ptr [rbp - 0x138], 0
@@ -1121,14 +1126,11 @@
 mov dword ptr [rbp - 0x108], 0xffffffff
 call F
-mov rax, qword ptr [rbp - 0x130]
-mov rdi, r14
```
(ещё 22 строк диффа: so-query.py fdiff libserver.so 0x48d3fd0)

### изменена: 0x48d7520 (2356 байт) CDOTA_Modifier_Batrider_Firefly::OnIntervalThink | строки: "particles/units/heroes/hero_batrider/batrider_firefly_debuff.vpcf"
было: 0x48d5100 (2336 байт)
- числа в инструкциях: +0x3fffffff −0
- виртуальные вызовы: +0x20 (слот 4)
- поля объектов: +0x1b38
- инструкций: 473 → 477
```diff
@@ -7,5 +7,5 @@
 mov r12, rdi
 push rbx
-sub rsp, 0x118
+sub rsp, 0x128
 call F
 mov rdi, r12
@@ -36,4 +36,5 @@
 mov edi, eax
 call F
+mov edx, dword ptr [r12 + 0x1b38]
 movaps xmm1, xmm0
 movss xmm0, dword ptr [r12 + 0x1b20]
@@ -42,5 +43,4 @@
 je L
 jbe L
-mov edx, dword ptr [r12 + 0x1b38]
 test edx, edx
 jle L
@@ -147,9 +147,7 @@
 pop rbp
 jmp F
-mov ecx, dword ptr [r12 + 0x1b38]
-mov dword ptr [rbp - 0xfc], 0
 addss xmm0, dword ptr [r12 + 0x1b14]
+test edx, edx
 movss dword ptr [r12 + 0x1b20], xmm0
-test ecx, ecx
 jle L
 xor r13d, r13d
@@ -157,10 +155,11 @@
 xor ebx, ebx
 mov qword ptr [rbp - 0x120], 0
+mov dword ptr [rbp - 0x118], 0
```
(ещё 140 строк диффа: so-query.py fdiff libserver.so 0x48d7520)

### изменена: 0x4a6ede0 (1847 байт) вызывается из: CDOTA_Modifier_ArcWarden_TempestDouble::vfunc#97 | строки: "particles/units/heroes/hero_chaos_knight/chaos_knight_crit_tgt.vpcf"; "attach_hitloc"; "Hero_ChaosKnight.ChaosStrike"
было: 0x4a6c9a0 (1847 байт)
- строки: +"Hero_ChaosKnight.ChaosStrike" −"Hero_ChaosKnisght.ChaosStrike"
- инструкций: 426 → 426
```diff
@@ -412,5 +412,5 @@
 lea rdi, [rbp - 0xf0]
 xor ecx, ecx
-lea rdx, [S:"Hero_ChaosKnisght.ChaosStrike"]
+lea rdx, [S:"Hero_ChaosKnight.ChaosStrike"]
 mov rsi, rax
 call F
```

### изменена: 0x4b207f0 (45 байт) CDOTA_Modifier_Meepo_Fling_Held::CheckState
было: 0x4b1e3b0 (37 байт)
- числа в инструкциях: +0x2000804022 +0xffffffdfff7fbfdd −0x800022 −0xffffffffff7fffdd
- инструкций: 9 → 9
```diff
@@ -1,8 +1,8 @@
-mov rax, qword ptr [rsi]
-or rax, 0x800022
+movabs rax, 0x2000804022
+or rax, qword ptr [rsi]
+movabs rdx, 0xffffffdfff7fbfdd
+and rdx, qword ptr [rsi + 8]
 movq xmm0, rax
-mov rax, qword ptr [rsi + 8]
-and rax, 0xffffffffff7fffdd
-movq xmm1, rax
+movq xmm1, rdx
 punpcklqdq xmm0, xmm1
 movups xmmword ptr [rsi], xmm0
```

### изменена: 0x4b92000 (1025 байт) CDOTA_Modifier_Meepo_Geomancy::OnIntervalThink | строки: "modifier_meepo_geomancy"; "modifier_slardar_puddle"; "meepo_divided_we_stand"
было: 0x4b8d810 (818 байт)
- строки: +"meepo_divided_we_stand"
- числа в инструкциях: +0 +-1 +-2 +9 +0x3f +0x1ff +0x70 +0xffffffff
- поля объектов: +0x1b18 +0x1b18 +0x1b18 +0x10 +0x10 +0x10
- прямых вызовов: 16 → 18
- инструкций: 178 → 218
```diff
@@ -48,25 +48,39 @@
 jmp F
 nop dword ptr [rax]
-mov ecx, dword ptr [r12 + 0x1b18]
+mov edx, dword ptr [r12 + 0x1b18]
 mov qword ptr [r12 + 0x1b0c], 0
 mov dword ptr [r12 + 0x1b14], 0
-cmp ecx, -1
+cmp edx, -1
 je L
 mov rsi, qword ptr [D]
 test rsi, rsi
 je L
-cmp ecx, -2
+cmp edx, -2
 je L
 movzx eax, word ptr [r12 + 0x1b18]
-mov rdx, rax
-shr rdx, 9
-and edx, 0x3f
-mov rdx, qword ptr [rsi + rdx*8]
-test rdx, rdx
+mov rcx, rax
+shr rcx, 9
+and ecx, 0x3f
+mov rcx, qword ptr [rsi + rcx*8]
+test rcx, rcx
+je L
+mov rdi, rax
+and edi, 0x1ff
+imul rdi, rdi, 0x70
+add rcx, rdi
+cmp edx, dword ptr [rcx + 0x10]
+jne L
```
(ещё 64 строк диффа: so-query.py fdiff libserver.so 0x4b92000)

### изменена: 0x4bab8d0 (555 байт) вызывается из: CDOTA_Modifier_Marci_Unleash::vfunc#97 | строки: "extend_duration"; "modifier_marci_unleash_flurry_pulse_debuff"
было: 0x4ba9490 (629 байт)
- числа в инструкциях: −3 −1 −0
- поля объектов: −0x5d1 −0xd3c −0x175a −0xd58
- инструкций: 150 → 137
```diff
@@ -92,15 +92,8 @@
 movss dword ptr [rbp - 0x24], xmm1
 ja L
-cmp byte ptr [r12 + 0x5d1], 3
-jne L
-test byte ptr [r12 + 0xd3c], 1
-jne L
-mov rax, qword ptr [r12]
-lea rdx, [T]
-mov rax, qword ptr [rax + 0xd58]
-cmp rax, rdx
-jne L
-xor r12d, r12d
+mov rdi, r12
+call F
 mov rdi, r13
+mov r12, rax
 call F
 mov rdi, rax
@@ -124,12 +117,6 @@
 pop rbp
 ret
+nop dword ptr [rax + rax]
 xor r14d, r14d
-jmp L
-mov rdi, r12
-call rax
-test al, al
-je L
-cmp byte ptr [r12 + 0x175a], 0
-je L
 jmp L
 lea rsi, [S:"modifier_marci_unleash_flurry_pulse_debuff"]
```

### изменена: 0x4bb3040 (4315 байт) | строки: "int"; "bool"; "float"
было: 0x4bb17a0 (1435 байт)
- константы из данных (числа логики): +0x00000000000000090000000000000000 +0x00000000000000090000000000000000 +0x00000000000000090000000000000000 +0x00000000000000090000000000000000
- числа в инструкциях: +0xffffffff +0xffffffff +0xffffffff +0xffffffff +0 +0 +0 +0 (и ещё 100)
- прямых вызовов: 16 → 44
- инструкций: 299 → 747
```diff
@@ -1,2 +1,450 @@
+push rbp
+mov rbp, rsp
+push rbx
+sub rsp, 8
+movzx eax, byte ptr [D]
+test al, al
+je L
+mov rax, qword ptr [D]
+test rax, rax
+je L
+mov rbx, qword ptr [rbp - 8]
+leave
+ret
+nop word ptr [rax + rax]
+lea rbx, [D]
+mov rdi, rbx
+call F
+test eax, eax
+je L
+pxor xmm0, xmm0
+mov eax, 0xffffffff
+movdqa xmm1, xmmword ptr [K:0x00000000000000090000000000000000]
+movups xmmword ptr [D], xmm0
+movups xmmword ptr [D], xmm0
+lea rsi, [D]
+movups xmmword ptr [D], xmm0
+movups xmmword ptr [D], xmm0
+movups xmmword ptr [D], xmm0
+movups xmmword ptr [D], xmm1
+movups xmmword ptr [D], xmm0
+mov qword ptr [D], rax
+mov qword ptr [D], 0
+mov qword ptr [D], 0
```
(ещё 417 строк диффа: so-query.py fdiff libserver.so 0x4bb3040)

### изменена: 0x4c31da0 (1820 байт) CDOTA_Ability_Ogre_Magi_Smash::OnSpellStart | строки: "damage"; "duration"; "modifier_ogre_magi_smash_buff"; "Hero_OgreMagi.FireShield.Cast"; "Hero_OgreMagi.FireShield.Target"; "ogre_magi_multicast"; "modifier_ogre_magi_arcana"; "multicast_fireshield_aoe"
было: 0x4c1dde0 (1788 байт)
- числа в инструкциях: +1 +1
- инструкций: 399 → 407
```diff
@@ -84,5 +84,5 @@
 cmp byte ptr [rax + 0x7e1], 0
 jne L
-lea rsi, [rbp - 0xd8]
+lea rsi, [rbp - 0xd4]
 mov rdi, rax
 call F
@@ -98,5 +98,5 @@
 mov esi, dword ptr [rbp - 0x110]
 mov rdi, rax
-movss xmm0, dword ptr [rbp - 0xd8]
+movss xmm0, dword ptr [rbp - 0xd4]
 call F
 mov esi, dword ptr [rbp - 0x110]
@@ -140,5 +140,5 @@
 mov rdi, qword ptr [rbp - 0x120]
 call F
-mov dword ptr [rbp - 0x120], eax
+mov dword ptr [rbp - 0x128], eax
 call F
 mov ecx, dword ptr [rbp - 0x110]
@@ -146,15 +146,15 @@
 mov edx, 1
 mov rdi, rax
-mov esi, dword ptr [rbp - 0x120]
+mov esi, dword ptr [rbp - 0x128]
 mov qword ptr [rbp - 0x6c], 0x3f800000
 lea eax, [rcx + 1]
 cvtsi2ss xmm0, eax
 lea rcx, [rbp - 0x70]
-mov qword ptr [rbp - 0x128], rcx
+mov qword ptr [rbp - 0x120], rcx
 movss dword ptr [rbp - 0x70], xmm0
 pxor xmm0, xmm0
```
(ещё 107 строк диффа: so-query.py fdiff libserver.so 0x4c31da0)

### изменена: 0x4e02b80 (728 байт) вызывается из: CDOTA_Modifier_Item_Caduceus::vfunc#97 | строки: "<NoAbilityName>"; "alchemist_unstable_concoction_throw"; "modifier_item_caduceus_enemy_cooldown"
было: 0x4e007c0 (728 байт)
- числа в инструкциях: +1
- инструкций: 176 → 176
```diff
@@ -145,9 +145,9 @@
 call F
 mov rdx, qword ptr [rbp - 0x38]
-xor r8d, r8d
 mov rcx, r15
+mov rdi, r13
 movss xmm0, dword ptr [rbp - 0x3c]
 mov rsi, rax
-mov rdi, r13
+mov r8d, 1
 call F
 mov rdi, r14
```

### изменена: 0x4e02e60 (632 байт) вызывается из: CDOTA_Modifier_Item_Caduceus::vfunc#97 | строки: "modifier_item_caduceus_ally_cooldown"
было: 0x4e00aa0 (632 байт)
- числа в инструкциях: +1
- инструкций: 152 → 152
```diff
@@ -115,9 +115,9 @@
 call F
 mov rdx, qword ptr [rbp - 0x38]
-xor r8d, r8d
 mov rcx, r15
+mov rdi, r14
 movss xmm0, dword ptr [rbp - 0x3c]
 mov rsi, rax
-mov rdi, r14
+mov r8d, 1
 call F
 mov rdi, r13
```

### изменена: 0x4e30a00 (3546 байт) | строки: "m_iStoredRuneType"; "int"; "int32"; "OnStoredRuneChanged"; "CDOTA_Item_EmptyBottle"; "15CNetworkVarBaseIiN22CDOTA_Item_EmptyBottle28NetworkVar_m_iStoredRuneTypeEE"
было: 0x4e2e5d0 (3594 байт)
- прямых вызовов: 65 → 63
- инструкций: 739 → 725
```diff
@@ -1,16 +1,2 @@
-push rbp
-mov rbp, rsp
-push rbx
-sub rsp, 8
-call F
-mov rdi, rax
-mov rbx, rax
-call F
-mov rdi, rbx
-mov rbx, qword ptr [rbp - 8]
-mov qword ptr [D], rax
-mov rsi, rax
-leave
-jmp F
 push rbp
 mov rbp, rsp
```

### изменена: 0x4fafe20 (1555 байт) вызывается из: CDOTA_Modifier_Item_Mechanical_Arm::vfunc#97 | строки: "modifier_mechanical_arm_counter"; "duration"; "modifier_item_occult_bracelet_mana_stack"; "particles/items_fx/occult_bracelet_hit.vpcf"
было: 0x4fada60 (1475 байт)
- числа в инструкциях: +-1 +-2 +9 +0x3f +0x1ff +0x70
- поля объектов: +0xd0 +0xd0 +0x10
- прямых вызовов: 52 → 51
- инструкций: 386 → 403
```diff
@@ -19,8 +19,24 @@
 cmp byte ptr [r14 + 0x5d1], 3
 jne L
-lea rdi, [r12 + 0xd0]
-call F
-test rax, rax
-je L
+mov ecx, dword ptr [r12 + 0xd0]
+cmp ecx, -1
+je L
+mov rsi, qword ptr [D]
+test rsi, rsi
+je L
+cmp ecx, -2
+je L
+movzx eax, word ptr [r12 + 0xd0]
+mov rdx, rax
+shr rdx, 9
+and edx, 0x3f
+mov rdx, qword ptr [rsi + rdx*8]
+test rdx, rdx
+je L
+and eax, 0x1ff
+imul rax, rax, 0x70
+add rax, rdx
+cmp ecx, dword ptr [rax + 0x10]
+jne L
 mov r15, qword ptr [rax]
 test r15, r15
@@ -51,5 +67,5 @@
 pop rbp
 ret
-nop
+nop dword ptr [rax]
```
(ещё 8 строк диффа: so-query.py fdiff libserver.so 0x4fafe20)

### изменена: 0x4fb0440 (616 байт) вызывается из: CDOTA_Modifier_Item_Mind_Breaker::vfunc#97 | строки: "modifier_silence"; "duration"
было: 0x4fae030 (1042 байт)
- строки: −"duration" −"modifier_orb_of_corrosion_debuff" −"modifier_orb_of_corrosion_debuff"
- числа в инструкциях: −-1 −-2 −9 −0x3f −0x1ff −0x70 −1 −1 (и ещё 2)
- виртуальные вызовы: −0xb20 (слот 356)
- поля объектов: −0xcc −0xcc −0x10 −0x44 −0x44 −0x1249 −0x1afc
- прямых вызовов: 27 → 15
- инструкций: 267 → 152
```diff
@@ -94,5 +94,4 @@
 call F
 test rax, rax
-mov rbx, rax
 je L
 test r14, r14
@@ -100,11 +99,6 @@
 cmp byte ptr [rax + 0x175a], 0
 jne L
-mov rax, qword ptr [rax]
-mov rdi, rbx
-call qword ptr [rax + 0xb20]
-test rax, rax
-jne L
-movzx eax, byte ptr [r14 + 0x624]
-cmp byte ptr [rbx + 0x624], al
+movzx ebx, byte ptr [r14 + 0x624]
+cmp byte ptr [rax + 0x624], bl
 je L
 mov eax, dword ptr [r14 + 0xd3c]
@@ -157,111 +151,2 @@
 call F
 jmp L
-push rbp
-mov rbp, rsp
-push r15
-push r14
-push r13
-mov r13, rdi
-mov rdi, rsi
-push r12
-mov r12, rsi
-push rbx
-mov rbx, rdx
```
(ещё 98 строк диффа: so-query.py fdiff libserver.so 0x4fb0440)

### изменена: 0x4fb5cc0 (184 байт) CDOTA_Modifier_MaskOfDispair_Berserk::OnCreated | строки: "berserk_spell_amp"; "berserk_manacost_reduction"; "berserk_magic_resistance"
было: 0x4fb3f50 (204 байт)
- числа в инструкциях: −0xffffffff
- поля объектов: −0x1b00
- прямых вызовов: 9 → 8
- инструкций: 59 → 51
```diff
@@ -43,17 +43,9 @@
 mov rax, qword ptr [rbx]
 call qword ptr [rax + 0x1f0]
-xor eax, eax
-test r12, r12
-je L
-xor r9d, r9d
-xor r8d, r8d
-xor ecx, ecx
-lea rsi, [S:"berserk_magic_resistance"]
-mov edx, 0xffffffff
+lea rsi, [rbx + 0x1b00]
 mov rdi, r12
-call F
-mov dword ptr [rbx + 0x1b00], eax
 pop rbx
 pop r12
 pop rbp
-ret
+lea rdx, [S:"berserk_magic_resistance"]
+jmp F
```

### изменена: 0x50483f0 (258 байт) CDOTA_Modifier_BackdoorProtectionInBase::vfunc#9
было: 0x5045ff0 (268 байт)
- инструкций: 65 → 63
```diff
@@ -62,4 +62,2 @@
 jbe L
 jmp L
-mov rax, qword ptr [0]
-ud2
```

### изменена: 0x5c1c800 (751 байт) вызывается из: CDOTA_BaseNPC::vfunc#512 | строки: "<NoAbilityName>"
было: 0x5c1a400 (727 байт)
- числа в инструкциях: −3
- поля объектов: +0xa98 +0x1788 +0xb4 −0xc
- инструкций: 151 → 156
```diff
@@ -107,7 +107,13 @@
 mov rdi, rbx
 call F
+mov rdi, qword ptr [rbx + 8]
+lea rdx, [T]
+mov rax, qword ptr [rdi]
+mov rax, qword ptr [rax + 0xa98]
+cmp rax, rdx
+jne L
+mov rax, qword ptr [rdi + 0x1788]
 mov rdi, qword ptr [rbx + 0x10]
-cmp dword ptr [rdi + 8], 3
-je L
+movss xmm0, dword ptr [rax + 0xb4]
 call F
 mov rdi, qword ptr [rbx + 0x18]
@@ -130,9 +136,9 @@
 call F
 mov rax, qword ptr [rbx + 0x28]
-mov edx, 0xffffffff
 movabs rcx, 0xffffffff00000000
+mov qword ptr [rax + 0x10], rcx
+mov ecx, 0xffffffff
 mov qword ptr [rax + 8], 0
-mov qword ptr [rax + 0x10], rcx
-mov qword ptr [rax + 0x18], rdx
+mov qword ptr [rax + 0x18], rcx
 mov qword ptr [rax + 0x20], 0
 add rsp, 0x130
@@ -147,5 +153,4 @@
 jmp L
 nop word ptr [rax + rax]
-movq xmm0, qword ptr [rdi + 0xc]
-call F
```
(ещё 2 строк диффа: so-query.py fdiff libserver.so 0x5c1c800)

### изменена: 0x61bed60 (1363 байт) CDOTA_BaseNPC::vfunc#430, CDOTA_Unit_Announcer::vfunc#430, CDOTA_Unit_CustomGameAnnouncer::vfunc#430
было: 0x61bc900 (288 байт)
- числа в инструкциях: +1 +1 +1 +1 +1 +1 +1 +1 (и ещё 32)
- прямых вызовов: 3 → 4
- инструкций: 91 → 376
```diff
@@ -90,2 +90,287 @@
 pop rbp
 ret
+mov rax, rsi
+sub rax, rdi
+cmp rax, 0x40
+jle L
+push rbp
+mov rbp, rsp
+push r14
+push r13
+mov r13, rdx
+mov rdx, rax
+sar rax, 3
+sar rdx, 2
+test r13, r13
+push r12
+mov r12, rdi
+push rbx
+je L
+lea r8, [r12 + rax*4]
+mov ecx, dword ptr [r12 + 4]
+sub r13, 1
+mov eax, dword ptr [r8]
+lea rbx, [r12 + 4]
+mov edi, dword ptr [rsi - 4]
+mov edx, dword ptr [r12]
+cmp ecx, eax
+jge L
+cmp eax, edi
+jl L
+cmp ecx, edi
+jl L
+mov eax, dword ptr [r12 + 4]
```
(ещё 254 строк диффа: so-query.py fdiff libserver.so 0x61bed60)

### изменена: 0x3ec3c40 (1578 байт) | строки: "uint8"; "CUtlVector"; "CNetworkUtlVectorBase"; "%s< %s%s >"; "21CNetworkUtlVectorBaseIhN24CBaseAnimGraphController42NetworkVar_m_SerializePose"; "10CUtlVectorIhi28CNetworkUtlVector_MemoryTypeIhLin1EEE"
- код тот же, но вызывает другую функцию: было 0x3eaca30, стало 0x3eacab0

### изменена: 0x4446d40 (3211 байт) | строки: "scripts/height_levels.txt"; "modifier_datadriven"; "modifier_lua"; "modifier_lua_horizontal_motion"; "modifier_lua_vertical_motion"; "modifier_lua_motion_both"; "Creates a testing npc"; "dota_test_npc"
- код тот же, но вызывает другую функцию: было 0x4446110, стало 0x4448300

### добавлена: 0x3e6ebb0 (183 байт) | строки: "?yx"

### добавлена: 0x3e6ece0 (183 байт) | строки: "Szx"

### добавлена: 0x3e6ee80 (98 байт) | строки: "f{x"

### добавлена: 0x4424670 (677 байт)

### добавлена: 0x4424920 (36 байт) | строки: "GetModifierAttackWhileMovingTarget"

### добавлена: 0x4424950 (36 байт) | строки: "GetModifierSpellRedirectTarget"

### добавлена: 0x442f0b0 (36 байт) | строки: "GetModifierPreAttack_BonusDamage_Proc"

### добавлена: 0x442f0e0 (36 байт) | строки: "GetModifierProcAttack_ConvertPhysicalToMagical"

### добавлена: 0x442f110 (36 байт) | строки: "GetModifierProcAttack_BonusDamage_Magical_Target"

### добавлена: 0x442f140 (36 байт) | строки: "GetModifierHealthcostReduction_Constant"

### добавлена: 0x442f170 (36 байт) | строки: "GetModifierBaseAttackTimeConstant_Adjust"

### добавлена: 0x442f1a0 (36 байт) | строки: "GetModifierBaseAttackTimePercentage"

### добавлена: 0x442f1d0 (36 байт) | строки: "GetModifierBonusDamageOutgoing_Percentage"

### добавлена: 0x442f200 (36 байт) | строки: "GetModifierDamageOutgoing_Percentage_Illusion_Amplify"

### добавлена: 0x442f230 (36 байт) | строки: "GetModifierSpellAmplify_PercentageTarget"

### добавлена: 0x442f260 (36 байт) | строки: "GetModifierManaDrainAmplify_Percentage"

### добавлена: 0x442f290 (36 байт) | строки: "GetModifierPhysicalArmorTotal_Percentage"

### добавлена: 0x442f2c0 (36 байт) | строки: "GetModifierPhysicalArmorBonusPost"

### добавлена: 0x442f2f0 (36 байт) | строки: "GetModifierMinPhysicalArmor"

### добавлена: 0x442f320 (36 байт) | строки: "GetModifierMagicalResistanceBaseReduction"

### добавлена: 0x442f350 (36 байт) | строки: "GetModifierMagicalResistanceBonusIllusions"

### добавлена: 0x442f380 (36 байт) | строки: "GetModifierMagicalResistanceBonusUnique"

### добавлена: 0x442f3b0 (36 байт) | строки: "GetModifierExtraManaBonusPercentage"

### добавлена: 0x442f3e0 (36 байт) | строки: "GetModifierBonusStats_Strength_Percentage"

### добавлена: 0x442f410 (36 байт) | строки: "GetModifierBonusStats_Agility_Percentage"

### добавлена: 0x442f440 (36 байт) | строки: "GetModifierBonusStats_Intellect_Percentage"

### добавлена: 0x442f470 (36 байт) | строки: "GetModifierIntellectNone"

### добавлена: 0x442f4a0 (36 байт) | строки: "GetModifierCastRangeBonusPercentage"

### добавлена: 0x442f4d0 (36 байт) | строки: "GetModifierProjectileSpeedBonusPercentage"

### добавлена: 0x442f500 (36 байт) | строки: "GetModifierPercentageCooldownOngoing"

### добавлена: 0x442f530 (36 байт) | строки: "GetModifierConstantCasttime"

### добавлена: 0x442f560 (36 байт) | строки: "GetModifierPercentageAttackAnimTime"

### добавлена: 0x442f590 (36 байт) | строки: "GetModifierPercentageConvertExpToGold"

### добавлена: 0x442f5c0 (36 байт) | строки: "GetModifierPhysical_ConstantBlockBonus"

### добавлена: 0x442f5f0 (36 байт) | строки: "GetModifierInnateDamageBlockPctOverride"

### добавлена: 0x442f620 (36 байт) | строки: "GetModifierStrongIllusion"

### добавлена: 0x442f650 (36 байт) | строки: "GetModifierSuperIllusion"

### добавлена: 0x442f680 (36 байт) | строки: "GetModifierXPDuringDeath"

### добавлена: 0x442f6b0 (36 байт) | строки: "GetDisableManaGain"

### добавлена: 0x442f6e0 (36 байт) | строки: "GetAllowEtherealAttack"

### добавлена: 0x442f710 (36 байт) | строки: "GetTriggerCosmeticAndEndAttack"

### добавлена: 0x442f740 (36 байт) | строки: "GetAlwaysAutoAttackWhileHoldPosition"

### добавлена: 0x442f770 (36 байт) | строки: "GetPhysicalArmorPiercingPercentageTarget"

### добавлена: 0x442f7a0 (36 байт) | строки: "GetMagicalArmorPiercingPercentageTarget"

### добавлена: 0x442f7d0 (36 байт) | строки: "GetCriticalStrikeBonus"

### добавлена: 0x442f800 (36 байт) | строки: "GetConvertAttackPhysicalToPure"

### добавлена: 0x442f830 (36 байт) | строки: "GetBuffAmplification"

### добавлена: 0x442f860 (36 байт) | строки: "OnOrderReceived"

### добавлена: 0x442f890 (36 байт) | строки: "OnSpentItemCharge"

### добавлена: 0x442f8c0 (36 байт) | строки: "OnRedirectHealthGain"

### добавлена: 0x442f8f0 (36 байт) | строки: "OnModifierRemoved"

### добавлена: 0x442f920 (36 байт) | строки: "OnScepterUpgradeSelected"

### добавлена: 0x442f950 (36 байт) | строки: "OnShardUpgradeSelected"

### добавлена: 0x442f980 (36 байт) | строки: "GetModifierShard"

### добавлена: 0x442f9b0 (36 байт) | строки: "GetModifierRadarCooldownReduction"

### добавлена: 0x442f9e0 (36 байт) | строки: "GetModifierIgnoreCooldown"

### добавлена: 0x442fa10 (36 байт) | строки: "GetModifierIncomingDamageIllusion"

### добавлена: 0x442fa40 (36 байт) | строки: "GetSuppressCleave"

### добавлена: 0x442fa70 (36 байт) | строки: "GetModifierTurnRateConstant"

### добавлена: 0x442faa0 (36 байт) | строки: "GetModifierPhysicalDamageOutgoing_Percentage"

### добавлена: 0x442fad0 (36 байт) | строки: "GetModifierKnockbackAmplification_Percentage"

### добавлена: 0x442fb00 (36 байт) | строки: "GetModifierPropertyFailAttack"

### добавлена: 0x442fb30 (36 байт) | строки: "GetModifierPrereduceIncomingDamage_Mult"

### добавлена: 0x442fb60 (36 байт) | строки: "GetModifierIncomingDamageConstantPost"

### добавлена: 0x442fb90 (36 байт) | строки: "GetModifierDamageOutgoing_PercentageMultiplicative"

### добавлена: 0x442fbc0 (36 байт) | строки: "GetModifierTickGold_Multiplier"

### добавлена: 0x442fbf0 (36 байт) | строки: "GetModifierSlowResistance_Unique"

### добавлена: 0x442fc20 (36 байт) | строки: "GetModifierSlowResistanceAppliesToAttacks"

### добавлена: 0x442fc50 (36 байт) | строки: "GetModifierAoEBonusPercentage"

### добавлена: 0x442fc80 (36 байт) | строки: "GetModifierProjectileSpeed"

### добавлена: 0x442fcb0 (36 байт) | строки: "GetModifierProjectileSpeedTarget"

### добавлена: 0x442fce0 (36 байт) | строки: "GetModifierBecomeStrength"

### добавлена: 0x442fd10 (36 байт) | строки: "GetModifierBecomeAgility"

### добавлена: 0x442fd40 (36 байт) | строки: "GetModifierBecomeIntelligence"

### добавлена: 0x442fd70 (36 байт) | строки: "GetModifierBecomeUniversal"

### добавлена: 0x442fda0 (36 байт) | строки: "OnForceProcMagicStick"

### добавлена: 0x442fdd0 (36 байт) | строки: "GetModifierForceMaxHealth"

### добавлена: 0x442fe00 (36 байт) | строки: "GetModifierForceMaxMana"

### добавлена: 0x442fe30 (36 байт) | строки: "GetModifierAoEBonusConstant"

### добавлена: 0x442fe60 (36 байт) | строки: "OnTakeDamagePostUnavoidableBlock"

### добавлена: 0x442fe90 (36 байт) | строки: "OnMuteDamageAbilities"

### добавлена: 0x442fec0 (36 байт) | строки: "GetSuppressCrit"

### добавлена: 0x442fef0 (36 байт) | строки: "GetModifierAbilityPoints"

### добавлена: 0x442ff20 (36 байт) | строки: "GetModifierBuybackPenaltyPercent"

### добавлена: 0x442ff50 (36 байт) | строки: "GetModifierReplaceAttack"

### добавлена: 0x442ff80 (36 байт) | строки: "GetModifierPropertyIgnoreForceTarget"

### добавлена: 0x442ffb0 (36 байт) | строки: "OnTreePlanted"

### добавлена: 0x442ffe0 (36 байт) | строки: "OnDamageHPLossSelf"

### добавлена: 0x4430010 (36 байт) | строки: "GetModifierHeroKillBountyBonus"

### добавлена: 0x4430040 (36 байт) | строки: "GetModifierPropertyAttackPotency"

### добавлена: 0x4430070 (36 байт) | строки: "GetModifierHealthDrainConstant"

### добавлена: 0x44300a0 (36 байт) | строки: "GetModifierHealthDrainPercentage"

### добавлена: 0x44300d0 (36 байт) | строки: "GetModifierHealthBarPipsFragile"

### добавлена: 0x472e940 (218 байт) | строки: "AttackRecord_t"; "CUtlVector"

### добавлена: 0x4731710 (107 байт) вызывается из: CDOTA_Modifier_Sniper_Headshot::vfunc#97

### добавлена: 0x4746000 (690 байт) вызывается из: CDOTA_Modifier_WitchDoctor_DeathWard::vfunc#97 | строки: "first_hit"; "attack_index"; "original_damage"

### добавлена: 0x4805f50 (118 байт) вызывается из: CDOTA_Modifier_Enchantress_Impetus::vfunc#97

### добавлена: 0x4855650 (447 байт) вызывается из: CDOTA_Modifier_DarkSeer_Normal_Punch::vfunc#97

### добавлена: 0x48b6b70 (96 байт) вызывается из: CDOTA_Modifier_Invoker_EMP::OnDestroy

### добавлена: 0x4b35270 (42 байт) CDOTA_Modifier_Meepo_Geomancy::OnCreated

### добавлена: 0x4ba9350 (680 байт) вызывается из: CDOTA_Modifier_Nyx_Assassin_ManaBurn::vfunc#97

### добавлена: 0x4fb06b0 (402 байт) вызывается из: CDOTA_Modifier_Item_Orb_Of_Corrosion::vfunc#97 | строки: "modifier_orb_of_corrosion_debuff"; "duration"

### удалена: 0x3e6ed90 (98 байт) | строки: "Rzx"

### удалена: 0x4428930 (83 байт)

### удалена: 0x4721ac0 (111 байт) | строки: "AttackRecord_t"

### удалена: 0x48547b0 (360 байт) вызывается из: CDOTA_Modifier_DarkSeer_Normal_Punch::vfunc#97

### удалена: 0x4b33060 (140 байт) CDOTA_Modifier_Meepo_Geomancy::OnCreated | строки: "meepo_divided_we_stand"

### удалена: 0x4ba0190 (752 байт) вызывается из: CDOTA_Modifier_Nyx_Assassin_ManaBurn::vfunc#97

### копии существующего кода (18): шаблонные / склеенные компоновщиком функции, такой же код есть и в другой сборке — не новый код
- ещё одна копия существующего кода: 0x4729610 (192 байт)
- ещё одна копия существующего кода: 0x4729a40 (95 байт) CDOTA_Modifier_Sniper_Headshot::vfunc#7
- ещё одна копия существующего кода: 0x4729c50 (103 байт) CDOTA_Modifier_Sniper_Headshot::vfunc#8
- ещё одна копия существующего кода: 0x473aa10 (254 байт) вызывается из: CDOTA_Modifier_Viper_PoisonAttack::vfunc#97
- ещё одна копия существующего кода: 0x479a6a0 (82 байт)
- ещё одна копия существующего кода: 0x4856bfa (10 байт)
- ещё одна копия существующего кода: 0x48a5b30 (82 байт) вызывается из: CDOTA_Ability_Enchantress_Enchant::OnSpellStart
- ещё одна копия существующего кода: 0x4e309c0 (48 байт)
- ещё одна копия существующего кода: 0x5048500 (10 байт) вызывается из: CDOTA_Modifier_Gold_Bag_Launch::OnDestroy
- одной копией существующего кода меньше: 0x3e6eb30 (183 байт)
- одной копией существующего кода меньше: 0x3e6ec60 (183 байт)
- одной копией существующего кода меньше: 0x470bf10 (25 байт) CDOTA_Modifier_Venomancer_PoisonSting::vfunc#7
- одной копией существующего кода меньше: 0x470e4d0 (50 байт) CDOTA_Modifier_Venomancer_PoisonSting::vfunc#8
- одной копией существующего кода меньше: 0x4727960 (192 байт)
- одной копией существующего кода меньше: 0x47354e0 (254 байт) вызывается из: CDOTA_Modifier_Viper_PoisonAttack::vfunc#97
- одной копией существующего кода меньше: 0x485a8d0 (2880 байт)
- одной копией существующего кода меньше: 0x4bb0c50 (2880 байт)
- одной копией существующего кода меньше: 0x61bca40 (1075 байт)
