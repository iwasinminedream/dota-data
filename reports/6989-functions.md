# Dota 6989: изменения кода по функциям и строки библиотек

Снимки `6988-11263542` → `6989-11264029`; funcdiff.py. В диффе: [S:…] — строка, [K:…] — константа из данных, F — вызов другой функции, L — переход внутри функции, [D]/[T] — прочие адреса. Регистры и смещения стека меняются и от перекомпиляции. Здесь всё, в том числе игровые функции и изменения от пересборки.

## libclient.so: функций 281893 → 281893; без изменений 281891, изменено 2, добавлено 0, удалено 0

### изменена: 0x7309800 (3732 байт) | строки: "Update"; "../../game/client/dota/panorama/hud/dota_hud_plus_timed_stats.cpp"; "kills"; "deaths"; "assists"; "last_hits"; "denies"; "PlusStatsValid"
было: 0x7309800 (3732 байт)
- числа в инструкциях: +0x546fd39b −0x371fcc24
- инструкций: 770 → 770
```diff
@@ -491,11 +491,11 @@
 test eax, eax
 je L
-lea rsi, [S:"target_denies"]
-lea rdi, [D]
-call F
-mov rdi, r12
-call F
-jmp L
-nop word ptr [rax + rax]
+lea rax, [S:"target_denies"]
+mov rdi, r12
+mov dword ptr [D], 0x546fd39b
+mov qword ptr [D], rax
+call F
+jmp L
+nop dword ptr [rax]
 lea r12, [D]
 mov rdi, r12
@@ -515,11 +515,11 @@
 test eax, eax
 je L
-lea rax, [S:"target_deaths"]
-mov rdi, r12
-mov dword ptr [D], 0x371fcc24
-mov qword ptr [D], rax
-call F
-jmp L
-nop dword ptr [rax]
+lea rsi, [S:"target_deaths"]
+lea rdi, [D]
+call F
+mov rdi, r12
+call F
+jmp L
+nop word ptr [rax + rax]
 lea r12, [D]
 mov rdi, r12
```

### изменена: 0x730ef00 (6881 байт) CDOTA_Hud_PlusGuide::vfunc#57 | строки: "#DOTA_Item_Build_DislikedItemsEmpty"; "#DOTA_Item_Build_PreferredItemsEmpty"
было: 0x730ef00 (6846 байт)
- инструкций: 1542 → 1545
```diff
@@ -1346,35 +1346,32 @@
 comiss xmm0, dword ptr [K:0.01]
 jb L
-mov edi, 0x80
-call F
-mov rsi, qword ptr [r15 + 0x30]
-xor edx, edx
-mov rdi, rax
-mov qword ptr [rbp - 0xb0], rax
-call F
 call F
 cmp byte ptr [rax + 0x1638], 0
-jne L
-cmp byte ptr [rax + 0x1639], 0
-jne L
-cmp byte ptr [rax + 0x163b], 0
-lea rdi, [rax + 0x70]
 je L
 lea rdi, [rax + 0x1740]
 mov esi, dword ptr [r13]
 call F
+test rax, rax
+je L
+mov edi, 0x80
+mov qword ptr [rbp - 0xb8], rax
+call F
+mov rsi, qword ptr [r15 + 0x30]
+xor edx, edx
+mov rdi, rax
+mov qword ptr [rbp - 0xb0], rax
+call F
+xor edx, edx
 xor r9d, r9d
 xor r8d, r8d
+mov rsi, qword ptr [rbp - 0xb8]
 mov ecx, 1
 mov rdi, qword ptr [rbp - 0xb0]
-xor edx, edx
-mov rsi, rax
-mov qword ptr [rbp - 0xb8], rax
 call F
 mov rax, qword ptr [rbp - 0xb0]
 mov esi, 1
 mov rdi, qword ptr [rax + 8]
-mov rdx, qword ptr [rdi]
-call qword ptr [rdx + 0x688]
+mov rax, qword ptr [rdi]
+call qword ptr [rax + 0x688]
 mov rdi, qword ptr [rbp - 0xb0]
 call F
@@ -1388,26 +1385,26 @@
 sete sil
 call F
-movsxd rcx, dword ptr [rbp - 0xa0]
-test ecx, ecx
-jle L
-mov rdx, qword ptr [rbp - 0x98]
-mov r8d, dword ptr [r13]
-mov rax, qword ptr [rbp - 0xb8]
-lea r9, [rdx + rcx*4]
-mov esi, dword ptr [rdx]
-cmp esi, r8d
-je L
-movsxd rdi, dword ptr [rax + 0xc0]
-test edi, edi
-jle L
-mov rcx, qword ptr [rax + 0xc8]
-lea rdi, [rcx + rdi*4]
-cmp esi, dword ptr [rcx]
-je L
-add rcx, 4
-cmp rcx, rdi
-jne L
+movsxd rdx, dword ptr [rbp - 0xa0]
+test edx, edx
+jle L
+mov rax, qword ptr [rbp - 0x98]
+mov edi, dword ptr [r13]
+mov r11, qword ptr [rbp - 0xb8]
+lea r8, [rax + rdx*4]
+mov ecx, dword ptr [rax]
+cmp ecx, edi
+je L
+movsxd rsi, dword ptr [r11 + 0xc0]
+test esi, esi
+jle L
+mov rdx, qword ptr [r11 + 0xc8]
+lea rsi, [rdx + rsi*4]
+cmp ecx, dword ptr [rdx]
+je L
 add rdx, 4
-cmp rdx, r9
+cmp rdx, rsi
+jne L
+add rax, 4
+cmp rax, r8
 jne L
 mov esi, 1
@@ -1415,5 +1412,5 @@
 call F
 jmp L
-nop dword ptr [rax + rax]
+nop dword ptr [rax]
 mov rdi, rax
 call F
@@ -1511,5 +1508,5 @@
 jl L
 jmp L
-nop
+nop word ptr cs:[rax + rax]
 sub eax, 1
 add r13d, 1
@@ -1518,4 +1515,10 @@
 jl L
 jmp L
+cmp byte ptr [rax + 0x1639], 0
+jne L
+cmp byte ptr [rax + 0x163b], 0
+lea rdi, [rax + 0x70]
+je L
```
(ещё 21 строк диффа: so-query.py fdiff libclient.so 0x730ef00)

## libserver.so: функций 221951 → 221950; без изменений 221947, изменено 3, добавлено 0, удалено 0

### изменена: 0x5c02fb0 (842 байт) | строки: "m_eCategory"; "Double-save to Member '%s'"; "m_unActionID"; "m_strLocName"
было: 0x5c02fb0 (857 байт)
- числа в инструкциях: −0 −0 −0
- поля объектов: −0x140 −0x148
- цели вызовов: +0x5bf0720
- инструкций: 209 → 201
```diff
@@ -4,6 +4,6 @@
 push r14
 push r13
-mov r13, rdi
 push r12
+mov r12, rdi
 push rbx
 mov rbx, rsi
@@ -28,5 +28,5 @@
 call F
 test rax, rax
-mov r12, rax
+mov r13, rax
 je L
 lea rdx, [S:"m_eCategory"]
@@ -35,5 +35,5 @@
 lea rsi, [S:"Double-save to Member '%s'"]
 call F
-mov esi, dword ptr [r13]
+mov esi, dword ptr [r12]
 lea rdi, [D]
 movabs rax, 0xc000000800000000
@@ -64,5 +64,5 @@
 jne L
 mov edx, 0x1b
-mov rdi, r12
+mov rdi, r13
 call F
 xor esi, esi
@@ -88,5 +88,5 @@
 call F
 test rax, rax
-mov r12, rax
+mov r13, rax
 je L
 lea rdx, [S:"m_unActionID"]
@@ -95,31 +95,22 @@
 lea rsi, [S:"Double-save to Member '%s'"]
 call F
-mov r14d, dword ptr [r13 + 4]
+mov r14d, dword ptr [r12 + 4]
 sub rsp, 8
 mov edx, 0x16
+xor ecx, ecx
+push 0
 xor r9d, r9d
-push 0
 xor r8d, r8d
-xor ecx, ecx
 mov esi, 4
-mov rdi, r12
+mov rdi, r13
 call F
 mov eax, r14d
-mov qword ptr [r12 + 8], rax
+mov qword ptr [r13 + 8], rax
 pop rax
 pop rdx
-cmp qword ptr [rbx + 0x140], 0
-je L
-xor esi, esi
-mov rdi, rbx
+mov rdi, rbx
+lea rsi, [r12 + 8]
 call F
 test al, al
-je L
-cmp byte ptr [rbx + 0x148], 0
-jne L
-mov rax, qword ptr [r13 + 8]
-test rax, rax
-je L
-cmp byte ptr [rax], 0
 jne L
 lea rsp, [rbp - 0x28]
@@ -131,5 +122,23 @@
 pop rbp
 ret
+nop dword ptr [rax]
+mov rdi, qword ptr [rbx + 0x120]
+lea rax, [S:"m_eCategory"]
+mov rsi, r14
+mov qword ptr [rbp - 0x40], r15
+mov qword ptr [rbp - 0x38], rax
+call F
+mov r13, rax
+jmp L
 nop
+mov rdi, qword ptr [rbx + 0x120]
+lea rax, [S:"m_unActionID"]
+mov rsi, r14
+mov qword ptr [rbp - 0x40], r15
+mov qword ptr [rbp - 0x38], rax
+call F
+mov r13, rax
+jmp L
+nop word ptr cs:[rax + rax]
 mov rdi, qword ptr [rbx + 0x120]
 lea r14, [rbp - 0x40]
@@ -143,5 +152,5 @@
 call F
 test rax, rax
-mov r12, rax
+mov r13, rax
 je L
 lea rdx, [S:"m_strLocName"]
@@ -150,7 +159,7 @@
 lea rsi, [S:"Double-save to Member '%s'"]
 call F
-mov rsi, qword ptr [r13 + 8]
+mov rsi, qword ptr [r12 + 8]
 lea rax, [D]
-mov rdi, r12
+mov rdi, r13
 mov edx, 0x1b
 test rsi, rsi
@@ -165,23 +174,5 @@
 jmp F
 nop dword ptr [rax]
-mov rdi, qword ptr [rbx + 0x120]
```
(ещё 53 строк диффа: so-query.py fdiff libserver.so 0x5c02fb0)

### изменена: 0x5c05a20 (116 байт)
было: 0x5c05a30 (91 байт)
- числа в инструкциях: +-1
- поля объектов: +0x1818
- инструкций: 26 → 34
```diff
@@ -2,7 +2,13 @@
 mov rbp, rsp
 push rbx
-mov rbx, rdi
 sub rsp, 8
-mov rdi, qword ptr [rdi + 8]
+mov rbx, qword ptr [rdi + 8]
+cmp dword ptr [rbx + 0x1818], -1
+je L
+mov rbx, qword ptr [rbp - 8]
+leave
+ret
+nop dword ptr [rax]
+mov rdi, rbx
 call F
 test rax, rax
@@ -13,14 +19,16 @@
 mov rdi, rax
 call F
-mov rdi, qword ptr [rbx + 8]
+movq xmm0, qword ptr [K:0x0000000000000000]
+mov rdi, rbx
 xor edx, edx
 xor esi, esi
 mov rbx, qword ptr [rbp - 8]
-movq xmm0, qword ptr [K:0x0000000000000000]
 movss xmm1, dword ptr [K:0]
 leave
 jmp F
-nop word ptr [rax + rax]
-mov rdi, qword ptr [rbx + 8]
+nop dword ptr [rax]
+mov rdi, rbx
 call F
 jmp L
+mov rax, qword ptr [0x10]
+ud2
```

### изменена: 0x5c79c20 (7256 байт) | строки: "m_vecMaterials"; "m_vecEconItems"; "m_vecCraftableRewards"; "m_vecHeroes"; "m_vecTradeRecipes"; "m_mapCodexEntriesLocalized"; "m_strTokenLocStringPrefix"; "m_vecSmallRewards"
было: 0x5c79c20 (7160 байт)
- строки: +"m_vecMaterials"
- числа в инструкциях: +2 +0xf +1 +9 +0xffffffff9ce441ba −0 −0xffffffff −0x9ce441ba
- поля объектов: +0x140 +0x128
- прямых вызовов: 168 → 170
- цели вызовов: +0x6513d20 "<unknown>"
- инструкций: 1502 → 1523
```diff
@@ -16,21 +16,31 @@
 test rax, rax
 jne L
-lea r12, [S:"m_vecMaterials"]
-mov edx, 0xffffffff
-mov esi, 0x9ce441ba
-lea r8, [rbp - 0xbc]
-mov rcx, r12
-mov rdi, r14
+mov rax, qword ptr [r14 + 0x128]
+movzx edi, word ptr [rax]
+shr di, 2
+and edi, 0xf
+cmp dil, 1
+je L
+cmp dil, 9
+jne L
+lea r12, [rbp - 0xb0]
+xor ecx, ecx
+mov rdi, rax
+mov qword ptr [rbp - 0xb0], 0xffffffff9ce441ba
+lea r13, [S:"m_vecMaterials"]
+mov rsi, r12
+lea rdx, [rbp - 0xbc]
+mov qword ptr [rbp - 0xa8], r13
 call F
 test rax, rax
 mov rbx, rax
 je L
-lea rsi, [rbp - 0xb0]
-mov rdi, r14
-mov qword ptr [rbp - 0xa8], r12
+mov rsi, r12
+mov rdi, r14
 mov r12, rbx
 mov qword ptr [rbp - 0xb0], 0xffffffff9ce441ba
-call F
-movzx eax, word ptr [r12]
+mov qword ptr [rbp - 0xa8], r13
+call F
+movzx eax, word ptr [rbx]
 xor edx, edx
 xor r15d, r15d
@@ -90,5 +100,5 @@
 test r15d, r15d
 jg L
-test rbx, rbx
+test r12, r12
 je L
 mov rdi, r14
@@ -660,6 +670,26 @@
 test al, al
 jne L
+mov rax, qword ptr [r14 + 0x140]
+test rax, rax
+je L
 jmp L
 nop word ptr [rax + rax]
+movzx edi, dil
+call F
+lea rsi, [D]
+mov rdi, r14
+mov rdx, rax
+xor eax, eax
+call F
+mov r12, qword ptr [r14 + 0x140]
+test r12, r12
+je L
+xor esi, esi
+mov rdi, r14
+call F
+test al, al
+jne L
+jmp L
+nop dword ptr [rax]
 cmp qword ptr [r14 + 0x140], 0
 je L
@@ -716,16 +746,7 @@
 jmp L
 nop dword ptr [rax]
-cmp qword ptr [r14 + 0x140], 0
-je L
-xor esi, esi
-mov rdi, r14
-call F
-test al, al
-jne L
-jmp L
-nop dword ptr [rax]
-mov rax, qword ptr [rbp - 0xc8]
-mov rdi, r15
-mov r13, qword ptr [rax + 0xd8]
+mov rax, qword ptr [rbp - 0xc8]
+mov rdi, r15
+mov r13, qword ptr [rax + 0x38]
 call F
 mov rdi, r15
@@ -765,10 +786,10 @@
 cmp r12, rax
 je L
-add r13, 0x10
-jmp L
-nop dword ptr [rax + rax]
-mov rax, qword ptr [rbp - 0xc8]
-mov rdi, r15
-mov r13, qword ptr [rax + 0x68]
+add r13, 0x70
+jmp L
+nop dword ptr [rax]
+mov rax, qword ptr [rbp - 0xc8]
+mov rdi, r15
+mov r13, qword ptr [rax + 0x20]
 call F
 mov rdi, r15
@@ -799,7 +820,7 @@
 mov rsi, r14
 mov rdi, r13
-call F
-mov rdi, r14
 add r12, 1
```
(ещё 462 строк диффа: so-query.py fdiff libserver.so 0x5c79c20)

### копии существующего кода (1): шаблонные / склеенные компоновщиком функции, такой же код есть и в другой сборке — не новый код
- одной копией существующего кода меньше: 0x5c05a8c (10 байт)


## Строки библиотек

