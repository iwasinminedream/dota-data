# Dota 6987: изменения кода по функциям и строки библиотек

Снимки `6986-11259680` → `6987-11262367`; funcdiff.py. В диффе: [S:…] — строка, [K:…] — константа из данных, F — вызов другой функции, L — переход внутри функции, [D]/[T] — прочие адреса. Регистры и смещения стека меняются и от перекомпиляции. Здесь всё, в том числе игровые функции и изменения от пересборки.

## libclient.so: функций 281886 → 281894; без изменений 281880, изменено 5, добавлено 1, удалено 0

### изменена: 0x48dde70 (3842 байт)
было: 0x48dde50 (3600 байт)
- числа в инструкциях: +-1 +-1 +-1 +0x7fff +3
- поля объектов: +0x28 +0x1a +0x20 +0x20 +0x18 +0x18 +0x10
- прямых вызовов: 35 → 37
- цели вызовов: +0x74696a0
- инструкций: 560 → 635
```diff
@@ -559,2 +559,77 @@
 call F
 jmp L
+test rdi, rdi
+je L
+push rbp
+mov rbp, rsp
+push rbx
+sub rsp, 8
+call F
+mov rbx, rax
+call F
+movzx ecx, word ptr [rbx + 0x28]
+cmp cx, -1
+je L
+test word ptr [rbx + 0x1a], 0x7fff
+cwde
+je L
+mov r8, qword ptr [rbx + 0x20]
+movzx edx, cx
+lea rdx, [rdx + rdx*2]
+shl rdx, 3
+lea rdi, [r8 + rdx]
+mov esi, dword ptr [rdi + 8]
+cmp eax, esi
+jb L
+cmp esi, eax
+jb L
+cmp cx, word ptr [rbx + 0x18]
+jae L
+add rdx, qword ptr [rbx + 0x20]
+cmp cx, word ptr [rdx]
+je L
+mov rax, qword ptr [rdx + 0x10]
+test rax, rax
+je L
+mov edx, dword ptr [rax]
+test edx, edx
+jle L
+mov rax, qword ptr [rax + 8]
+mov rbx, qword ptr [rbp - 8]
+mov rax, qword ptr [rax]
+leave
+ret
+nop
+movzx ecx, word ptr [rsi*8]
+cmp cx, -1
+je L
+movzx edx, cx
+lea rsi, [rdx + rdx*2]
+mov edi, dword ptr [rsi*8 + 8]
+lea rdx, [rsi*8]
+cmp eax, edi
+jb L
+cmp edi, eax
+jb L
+cmp cx, word ptr [rbx + 0x18]
+jae L
+cmp word ptr [rdx], cx
+jne L
+mov rbx, qword ptr [rbp - 8]
+xor eax, eax
+leave
+ret
+nop
+movzx ecx, word ptr [rdi]
+cmp cx, -1
+jne L
+jmp L
+nop
+movzx ecx, word ptr [rdi + 2]
+jmp L
+nop word ptr cs:[rax + rax]
+xor eax, eax
+ret
+nop dword ptr [rax + rax]
+movzx ecx, word ptr [rsi*8 + 2]
+jmp L
```

### изменена: 0x4f8b920 (8443 байт) | строки: "float"; "int"; "bool"; "CUtlString"; "HeroID_t"; "HeroFacetID_t"; "CHandle<CDOTA_BaseNPC>"; "uint32"
было: 0x4f8b8e0 (8731 байт)
- числа в инструкциях: −0x10 −1 −1 −1 −0x3fffffff −0x3fffffff −0x3fffffff −0x3fffffff (и ещё 8)
- поля объектов: −0x158 −0x158 −0x158 −0x168 −0x168 −0x168 −0x168 −0x160 −0x160 −0x160 −0x16c −0x16c (и ещё 3)
- прямых вызовов: 141 → 138
- инструкций: 1724 → 1664
```diff
@@ -159,100 +159,112 @@
 movq xmm4, qword ptr [D]
 punpcklqdq xmm6, xmm3
-movaps xmmword ptr [rbp - 0x2d0], xmm6
+movaps xmmword ptr [rbp - 0x2e0], xmm6
 movq xmm5, qword ptr [D]
 punpcklqdq xmm7, xmm0
-movaps xmmword ptr [rbp - 0x2b0], xmm7
+movaps xmmword ptr [rbp - 0x2d0], xmm7
 movq xmm6, qword ptr [D]
 punpcklqdq xmm4, xmm0
-movaps xmmword ptr [rbp - 0x290], xmm4
+movaps xmmword ptr [rbp - 0x2c0], xmm4
 movq xmm7, qword ptr [D]
 punpcklqdq xmm5, xmm0
-movaps xmmword ptr [rbp - 0x280], xmm5
+movaps xmmword ptr [rbp - 0x2b0], xmm5
 movq xmm4, qword ptr [D]
 punpcklqdq xmm6, xmm0
-movaps xmmword ptr [rbp - 0x260], xmm6
+movaps xmmword ptr [rbp - 0x290], xmm6
 movq xmm5, qword ptr [D]
 punpcklqdq xmm7, xmm0
-movaps xmmword ptr [rbp - 0x240], xmm7
+movaps xmmword ptr [rbp - 0x270], xmm7
 movq xmm6, qword ptr [D]
 punpcklqdq xmm4, xmm1
-movaps xmmword ptr [rbp - 0x220], xmm4
+movaps xmmword ptr [rbp - 0x260], xmm4
 movq xmm7, qword ptr [D]
 punpcklqdq xmm5, xmm0
-movaps xmmword ptr [rbp - 0x200], xmm5
+movaps xmmword ptr [rbp - 0x240], xmm5
 movq xmm4, qword ptr [D]
 punpcklqdq xmm6, xmm1
-movaps xmmword ptr [rbp - 0x1e0], xmm6
+movaps xmmword ptr [rbp - 0x230], xmm6
 punpcklqdq xmm7, xmm1
-movaps xmmword ptr [rbp - 0x1c0], xmm7
+movaps xmmword ptr [rbp - 0x210], xmm7
 punpcklqdq xmm4, xmm0
-movaps xmmword ptr [rbp - 0x190], xmm4
+movaps xmmword ptr [rbp - 0x1e0], xmm4
 movq xmm5, qword ptr [D]
 movq xmm6, qword ptr [D]
 movq xmm7, qword ptr [D]
 punpcklqdq xmm5, xmm0
-movaps xmmword ptr [rbp - 0x170], xmm5
+movaps xmmword ptr [rbp - 0x1c0], xmm5
 movq xmm4, qword ptr [D]
 punpcklqdq xmm6, xmm1
-movaps xmmword ptr [rbp - 0x50], xmm6
+movaps xmmword ptr [rbp - 0x1a0], xmm6
 movq xmm5, qword ptr [D]
 punpcklqdq xmm7, xmm1
-movaps xmmword ptr [rbp - 0x60], xmm7
+movaps xmmword ptr [rbp - 0x180], xmm7
 movq xmm6, qword ptr [D]
 punpcklqdq xmm4, xmm1
-movaps xmmword ptr [rbp - 0x70], xmm4
+movaps xmmword ptr [rbp - 0x160], xmm4
 movq xmm7, qword ptr [D]
 punpcklqdq xmm5, xmm0
-movaps xmmword ptr [rbp - 0x80], xmm5
+movaps xmmword ptr [rbp - 0x50], xmm5
 movq xmm4, qword ptr [D]
 punpcklqdq xmm6, xmm0
-movaps xmmword ptr [rbp - 0x90], xmm6
+movaps xmmword ptr [rbp - 0x60], xmm6
 movq xmm5, qword ptr [D]
 punpcklqdq xmm7, xmm0
-movaps xmmword ptr [rbp - 0xa0], xmm7
+movaps xmmword ptr [rbp - 0x70], xmm7
 movq xmm6, qword ptr [D]
 punpcklqdq xmm4, xmm0
-movaps xmmword ptr [rbp - 0xb0], xmm4
+movaps xmmword ptr [rbp - 0x80], xmm4
 movq xmm7, qword ptr [D]
 punpcklqdq xmm5, xmm0
-movaps xmmword ptr [rbp - 0xc0], xmm5
+movaps xmmword ptr [rbp - 0x90], xmm5
 movq xmm4, qword ptr [D]
 punpcklqdq xmm6, xmm0
-movaps xmmword ptr [rbp - 0xd0], xmm6
+movaps xmmword ptr [rbp - 0xa0], xmm6
 movq xmm5, qword ptr [D]
 punpcklqdq xmm7, xmm0
-movaps xmmword ptr [rbp - 0xe0], xmm7
+movaps xmmword ptr [rbp - 0xb0], xmm7
 movq xmm6, qword ptr [D]
 punpcklqdq xmm4, xmm2
-movaps xmmword ptr [rbp - 0xf0], xmm4
+movaps xmmword ptr [rbp - 0xc0], xmm4
 movq xmm7, qword ptr [D]
 punpcklqdq xmm5, xmm0
-movaps xmmword ptr [rbp - 0x100], xmm5
+movaps xmmword ptr [rbp - 0xd0], xmm5
 movq xmm4, qword ptr [D]
 punpcklqdq xmm6, xmm0
-movaps xmmword ptr [rbp - 0x110], xmm6
+movaps xmmword ptr [rbp - 0xe0], xmm6
 punpcklqdq xmm7, xmm2
-movaps xmmword ptr [rbp - 0x120], xmm7
+movaps xmmword ptr [rbp - 0xf0], xmm7
 punpcklqdq xmm4, xmm2
-movaps xmmword ptr [rbp - 0x130], xmm4
+movaps xmmword ptr [rbp - 0x100], xmm4
 movq xmm5, qword ptr [D]
 movq xmm7, qword ptr [D]
 movq xmm6, qword ptr [D]
 punpcklqdq xmm5, xmm0
-movaps xmmword ptr [rbp - 0x140], xmm5
+movaps xmmword ptr [rbp - 0x110], xmm5
 punpcklqdq xmm7, xmm2
-movaps xmmword ptr [rbp - 0x160], xmm7
+movaps xmmword ptr [rbp - 0x130], xmm7
 movq xmm2, qword ptr [D]
 punpcklqdq xmm6, xmm0
-movaps xmmword ptr [rbp - 0x150], xmm6
+movaps xmmword ptr [rbp - 0x120], xmm6
```
(ещё 492 строк диффа: so-query.py fdiff libclient.so 0x4f8b920)

### изменена: 0x4fcd860 (6476 байт) | строки: "m_pArcanaData_CDOTA_ArcanaDataEntity_DrowRanger"; "CDOTA_ArcanaDataEntity_DrowRanger *"; "CDOTA_ArcanaDataEntity_DrowRanger"; "%s*"; "m_pArcanaData_CDOTA_ArcanaDataEntity_FacelessVoid"; "CDOTA_ArcanaDataEntity_FacelessVoid *"; "CDOTA_ArcanaDataEntity_FacelessVoid"; "m_pArcanaData_CDOTA_ArcanaDataEntity_Razor"
было: 0x4fcd960 (6476 байт)
- числа в инструкциях: +0x5bd1e995 +0xb6700ed2 −0x726574
- прямых вызовов: 174 → 173
- инструкций: 1281 → 1279
```diff
@@ -637,10 +637,8 @@
 mov esi, eax
 call F
-lea rdi, [D]
-mov esi, eax
-call F
 mov edi, 0x158
-xor eax, 0x726574
 imul r13d, eax, 0x5bd1e995
+xor r13d, 0xb6700ed2
+imul r13d, r13d, 0x5bd1e995
 mov eax, r13d
 shr eax, 0xd
@@ -908,5 +906,5 @@
 call F
 jmp L
-nop
+nop word ptr [rax + rax]
 lea r14, [D]
 mov rdi, r14
```

### изменена: 0x4fd4ee0 (20268 байт) | строки: "m_ForcedHUDSkin"; "CUtlString"; "m_nCustomGameForceHeroSelectionId"; "HeroID_t"; "int32"; "m_nCustomGameForceHeroVariant"; "HeroFacetID_t"; "uint32"
было: 0x4fd4fe0 (20220 байт)
- числа в инструкциях: +1 +1
- инструкций: 4627 → 4637
```diff
@@ -87,7 +87,6 @@
 mov eax, dword ptr [D]
 mov rdi, rbx
-mov qword ptr [rbp - 0x58], r12
+mov qword ptr [rbp - 0x40], 0
 lea rsi, [S:"CUtlString"]
-mov qword ptr [rbp - 0x40], 0
 mov dword ptr [r12 + 0x28], eax
 mov rax, qword ptr [D]
@@ -112,6 +111,7 @@
 mov rdi, rbx
 call F
-lea rdi, [r12 + 0x18]
+lea r14, [r12 + 0x18]
 lea rsi, [S:"CUtlString"]
+mov rdi, r14
 call F
 mov rax, qword ptr [K:0x0000077000000008]
@@ -123,12 +123,12 @@
 lea rax, [D]
 mov qword ptr [rbp - 0x78], rax
-mov r12, qword ptr [D]
-test r12, r12
-je L
-mov rdi, r12
+mov r13, qword ptr [D]
+test r13, r13
+je L
+mov rdi, r13
 call F
 test eax, eax
 jg L
-xor r14d, r14d
+xor r15d, r15d
 mov rsi, qword ptr [rbp - 0x78]
 lea rax, [rbp - 0x50]
@@ -138,17 +138,15 @@
 mov rdi, rax
 call F
-mov r12, qword ptr [rbp - 0x58]
+mov rsi, qword ptr [r12 + 0x10]
 mov qword ptr [rbp - 0x48], 0
-mov r15, qword ptr [rbp - 0x68]
-mov rsi, qword ptr [r12 + 0x10]
-mov rdi, r15
+mov rdi, qword ptr [rbp - 0x68]
 test rsi, rsi
 cmove rsi, r13
 call F
+mov rdi, qword ptr [rbp - 0x68]
 lea rsi, [S:"CUtlString"]
-mov rdi, r15
 call F
 mov rsi, qword ptr [rbp - 0x48]
-lea rdi, [r12 + 0x18]
+mov rdi, r14
 call F
 lea rdi, [r12 + 0x128]
@@ -162,15 +160,19 @@
 lea rdi, [r12 + 0x110]
 call F
-test r14b, r14b
+test r15b, r15b
 jne L
-lea rax, [rbp - 0x58]
-lea rdi, [D]
-mov rsi, rax
-mov qword ptr [rbp - 0x80], rax
-call F
+mov r13d, dword ptr [D]
+cmp r13d, dword ptr [D]
+mov eax, r13d
+je L
 lea rsi, [S:"m_ForcedHUDSkin"]
-mov rdx, rbx
-lea rdi, [D]
-mov dword ptr [rbp - 0x40], eax
+add eax, 1
+movsxd rdx, r13d
+mov dword ptr [D], eax
+mov rax, qword ptr [D]
+lea rdi, [D]
+mov qword ptr [rax + rdx*8], r12
+mov rdx, rbx
+mov dword ptr [rbp - 0x40], r13d
 call F
 cmp qword ptr [rbp - 0x48], 0
@@ -250,5 +252,5 @@
 xor eax, eax
 mov rsi, qword ptr [rbp - 0x78]
-mov byte ptr [rbp - 0x8a], al
+mov byte ptr [rbp - 0x80], al
 lea r13, [D]
 mov rdi, qword ptr [rbp - 0x70]
@@ -291,9 +293,11 @@
 lea rdi, [r12 + 0x110]
 call F
-movzx eax, byte ptr [rbp - 0x8a]
+movzx eax, byte ptr [rbp - 0x80]
 test al, al
 jne L
-mov rsi, qword ptr [rbp - 0x80]
-lea rdi, [D]
+lea rax, [rbp - 0x58]
+lea rdi, [D]
+mov rsi, rax
+mov qword ptr [rbp - 0x80], rax
 call F
 mov rdx, rbx
@@ -3647,4 +3651,27 @@
 jmp L
 nop dword ptr [rax + rax]
+mov rsi, r12
+mov rdi, rbx
+call F
+mov rdx, qword ptr [rbp - 0x40]
+lea rdi, [D]
+mov r8, qword ptr [r12 + 0x10]
+mov rcx, qword ptr [r12 + 0x18]
+mov rsi, qword ptr [r12 + 0x20]
```
(ещё 843 строк диффа: so-query.py fdiff libclient.so 0x4fd4ee0)

### изменена: 0x51f14c0 (5403 байт) | строки: "FreeConstAligned"
было: 0x51f1540 (5545 байт)
- числа в инструкциях: +1 +1 +0x48 +0x38 −0 −0 −0 −0 −0 −2
- виртуальные вызовы: −0x20 (слот 4)
- поля объектов: +0x40 +0x10 +0x10 +0x18 +0x2c −0x28 −0x38 −0x24 −0x24 −0x14 −0x20 −0x30 −0x3c
- прямых вызовов: 50 → 49
- инструкций: 1172 → 1145
```diff
@@ -84,5 +84,5 @@
 mov qword ptr [rbp - 0x320], rax
 mov qword ptr [rbp - 0x310], rax
-mov qword ptr [rbp - 0x300], rdx
+mov qword ptr [rbp - 0x2f8], rdx
 xor edx, edx
 xor esi, esi
@@ -90,5 +90,5 @@
 call F
 add rbx, 0x58
-cmp qword ptr [rbp - 0x300], rbx
+cmp qword ptr [rbp - 0x2f8], rbx
 jne L
 mov rbx, qword ptr [rbp - 0x2e0]
@@ -121,5 +121,5 @@
 mov qword ptr [rbp - 0x218], 0
 mov r13, qword ptr [rbp - 0x2e0]
-mov qword ptr [rbp - 0x338], rax
+mov qword ptr [rbp - 0x330], rax
 lea r12, [rbp - 0x268]
 mov rcx, qword ptr [rbp - 0x320]
@@ -129,8 +129,8 @@
 mov qword ptr [rbp - 0x328], rbx
 mov rbx, r12
-mov qword ptr [rbp - 0x2f8], rax
+mov qword ptr [rbp - 0x308], rax
 mov byte ptr [rbp - 0x2e0], 0
-mov byte ptr [rbp - 0x308], r15b
-mov qword ptr [rbp - 0x330], r13
+mov byte ptr [rbp - 0x300], r15b
+mov qword ptr [rbp - 0x338], r13
 mov dword ptr [rbp - 0x220], 0
 test byte ptr [rcx + 0x11], 1
@@ -195,11 +195,11 @@
 add rcx, 0x58
 add rbx, 0x18
-cmp qword ptr [rbp - 0x2f8], rbx
+cmp qword ptr [rbp - 0x308], rbx
 jne L
 cmp byte ptr [rbp - 0x2e0], 0
 mov dword ptr [rbp - 0x220], 0
-movzx r15d, byte ptr [rbp - 0x308]
+movzx r15d, byte ptr [rbp - 0x300]
 mov rbx, qword ptr [rbp - 0x328]
-mov r13, qword ptr [rbp - 0x330]
+mov r13, qword ptr [rbp - 0x338]
 mov eax, dword ptr [rbp - 0x20c]
 jne L
@@ -213,8 +213,7 @@
 mov rax, qword ptr [rdi]
 call qword ptr [rax + 0x20]
-mov rax, qword ptr [rbp - 0x2f8]
-lea r12, [rbp - 0x148]
+mov rax, qword ptr [rbp - 0x308]
+lea rdx, [rbp - 0x148]
 movdqa xmm0, xmmword ptr [K:0xffffffffffffffff00000000ffffffff]
-mov r14, rax
 mov dword ptr [rax], 0
 add rax, 0x48
@@ -227,19 +226,19 @@
 mov qword ptr [rax - 0x20], 0
 movups xmmword ptr [rax - 0x18], xmm0
-cmp r12, rax
-jne L
-mov qword ptr [rbp - 0x360], rbx
+cmp rdx, rax
+jne L
+mov r15, qword ptr [rbp - 0x330]
+mov r8, rbx
+mov qword ptr [rbp - 0x358], rbx
+mov r14, qword ptr [rbp - 0x308]
+lea rax, [rbp - 0x288]
+mov qword ptr [rbp - 0x300], r13
+mov rbx, qword ptr [rbp - 0x320]
+mov qword ptr [rbp - 0x2e0], rax
+lea r12, [r15 + 0x48]
+mov qword ptr [rbp - 0x338], r12
 mov rcx, r14
+mov r12, r8
 mov r8, r13
-mov r15, qword ptr [rbp - 0x338]
-lea rdx, [rbp - 0x288]
-mov qword ptr [rbp - 0x350], r12
-mov r12, rbx
-mov qword ptr [rbp - 0x308], r13
-mov qword ptr [rbp - 0x2e0], rdx
-lea rax, [r15 + 0x48]
-mov qword ptr [rbp - 0x340], rax
-mov rax, qword ptr [rbp - 0x320]
-mov rbx, rax
 mov r14d, dword ptr [r15]
 test r14d, r14d
@@ -251,17 +250,15 @@
 add rcx, 0x48
 add rbx, 0x58
-cmp qword ptr [rbp - 0x340], r15
+cmp qword ptr [rbp - 0x338], r15
 jne L
 cmp dword ptr [rbp + 0x10], 0x13
 lea rax, [rbp - 0x208]
 mov qword ptr [rbp - 0x2d8], rax
-mov r12, qword ptr [rbp - 0x350]
 lea rax, [rbp - 0x288]
 mov qword ptr [rbp - 0x2e8], rax
 je L
-mov qword ptr [rbp - 0x340], r12
-mov r15, qword ptr [rbp - 0x360]
+mov r15, qword ptr [rbp - 0x358]
 mov r12, qword ptr [rbp - 0x348]
-mov rax, qword ptr [rbp - 0x308]
+mov rax, qword ptr [rbp - 0x300]
 mov r9d, dword ptr [rax]
 test r9d, r9d
@@ -270,23 +267,23 @@
 add r15, 4
 add r12, 0x18
-add qword ptr [rbp - 0x308], 4
+add qword ptr [rbp - 0x300], 4
 mov rax, qword ptr [rbp - 0x310]
 add qword ptr [rbp - 0x2d8], 0x48
```
(ещё 367 строк диффа: so-query.py fdiff libclient.so 0x51f14c0)

### добавлена: 0x4739d60 (22 байт) CDOTA_Modifier_PathMoveSpeed::vfunc#18

### копии существующего кода (9): шаблонные / склеенные компоновщиком функции, такой же код есть и в другой сборке — не новый код
- ещё одна копия существующего кода: 0x4739a10 (3 байт) CDOTA_Modifier_PathInLane::vfunc#18
- ещё одна копия существующего кода: 0x4f4a100 (3 байт) CDOTA_Modifier_Creep_Slow::vfunc#18
- ещё одна копия существующего кода: 0x4f4a1a0 (3 байт) CDOTA_Modifier_Lane_Creep_OutOfLane_Slow::vfunc#18
- ещё одна копия существующего кода: 0x4f4a210 (3 байт) CDOTA_Modifier_Creep_Haste::vfunc#18
- ещё одна копия существующего кода: 0x517ccc0 (3 байт) CDOTA_Modifier_Neutral_Sleep_AI::vfunc#18
- ещё одна копия существующего кода: 0x5181d80 (3 байт) CDOTA_Modifier_Creep_Siege::vfunc#18
- ещё одна копия существующего кода: 0x5181e50 (3 байт) CDOTA_Modifier_Creep_Piercing::vfunc#18
- ещё одна копия существующего кода: 0x5181f00 (3 байт) CDOTA_Modifier_Creep_Irresolute::vfunc#18
- одной копией существующего кода меньше: 0x48dec80 (242 байт)

## libserver.so: функций 221943 → 221951; без изменений 221832, изменено 100, добавлено 8, удалено 9

### изменена: 0x3bb3ce0 (258 байт)
было: 0x3bb3ca0 (258 байт)
- строки: −"@!N"
- инструкций: 86 → 86
```diff
@@ -7,5 +7,5 @@
 mov rbx, rsi
 movsxd rsi, edx
-lea rdx, [S:"@!N"]
+lea rdx, [D]
 sub rsp, 0x18
 movsxd rax, dword ptr [rdx + rdi*4]
```

### изменена: 0x3bd9200 (323 байт) | строки: "CUtlString"; "CUtlVector"
было: 0x3bd91c0 (323 байт)
- строки: −"xiP"
- инструкций: 99 → 99
```diff
@@ -2,5 +2,5 @@
 ja L
 push rbp
-lea rdx, [S:"xiP"]
+lea rdx, [D]
 mov edi, edi
 mov rbp, rsp
```

### изменена: 0x3bf9220 (238 байт) | строки: "_UR"
было: 0x3bf91e0 (238 байт)
- строки: +"_UR"
- инструкций: 65 → 65
```diff
@@ -2,5 +2,5 @@
 ja L
 push rbp
-lea rdx, [D]
+lea rdx, [S:"_UR"]
 mov edi, edi
 mov rbp, rsp
```

### изменена: 0x3bfaec0 (323 байт) | строки: "LqR"; "CUtlSymbolLarge"; "CNetworkUtlVectorBase"
было: 0x3bfae80 (323 байт)
- строки: +"LqR"
- инструкций: 99 → 99
```diff
@@ -2,5 +2,5 @@
 ja L
 push rbp
-lea rdx, [D]
+lea rdx, [S:"LqR"]
 mov edi, edi
 mov rbp, rsp
```

### изменена: 0x3bfb070 (317 байт) | строки: "hsR"
было: 0x3bfb030 (317 байт)
- строки: +"hsR" −"(sR"
- инструкций: 98 → 98
```diff
@@ -7,5 +7,5 @@
 push rbx
 ja L
-lea rdx, [S:"(sR"]
+lea rdx, [S:"hsR"]
 mov edi, edi
 mov rbx, rsi
```

### изменена: 0x3c19b60 (602 байт) | строки: "CGlobalSymbol"; "CAnimGraph2ParamOptionalRef"; "CTransform"
было: 0x3c19b20 (602 байт)
- строки: −"dGT"
- инструкций: 169 → 169
```diff
@@ -9,5 +9,5 @@
 cmp edi, 6
 ja F
-lea rdx, [S:"dGT"]
+lea rdx, [D]
 mov edi, edi
 mov rbx, rsi
```

### изменена: 0x3c29ac0 (1047 байт) | строки: "oEU"; "Unsupported KV3 basic type '%s' (%d)!"; "Pointers cannot be used as numeric values"
было: 0x3c29a80 (1047 байт)
- строки: +"oEU" −"/EU"
- инструкций: 245 → 245
```diff
@@ -47,5 +47,5 @@
 cmp r8b, 6
 ja L
-lea rcx, [S:"/EU"]
+lea rcx, [S:"oEU"]
 movzx edx, r8b
 movsxd rdx, dword ptr [rcx + rdx*4]
```

### изменена: 0x3c29ee0 (1047 байт) | строки: "sIU"; "Unsupported KV3 basic type '%s' (%d)!"; "Pointers cannot be used as numeric values"
было: 0x3c29ea0 (1047 байт)
- строки: +"sIU" −"3IU"
- инструкций: 245 → 245
```diff
@@ -47,5 +47,5 @@
 cmp r8b, 6
 ja L
-lea rcx, [S:"3IU"]
+lea rcx, [S:"sIU"]
 movzx edx, r8b
 movsxd rdx, dword ptr [rcx + rdx*4]
```

### изменена: 0x3c2b7f0 (951 байт) | строки: "IKV3TransferInterface_GameTime_Load"; "NeU"
было: 0x3c2b7b0 (951 байт)
- строки: +"NeU"
- инструкций: 235 → 235
```diff
@@ -63,5 +63,5 @@
 cmp al, 6
 ja L
-lea rdx, [D]
+lea rdx, [S:"NeU"]
 movzx eax, al
 movsxd rax, dword ptr [rdx + rax*4]
```

### изменена: 0x3c6d480 (1027 байт) | строки: "l[Y"; "CEntityIOOutput"; "CBaseFilter"; "CHandle"
было: 0x3c6d440 (1027 байт)
- строки: +"l[Y" −",[Y"
- инструкций: 172 → 172
```diff
@@ -2,5 +2,5 @@
 ja L
 push rbp
-lea rdx, [S:",[Y"]
+lea rdx, [S:"l[Y"]
 mov edi, edi
 mov rbp, rsp
```

### изменена: 0x3c6e7a0 (653 байт) | строки: "AoY"; "%g %g %g"; "(null)"; "%g %g %g %g"; "%lld"; "%llu"; "%d %d %d %d"; "false"
было: 0x3c6e760 (653 байт)
- строки: +"AoY"
- инструкций: 159 → 159
```diff
@@ -7,5 +7,5 @@
 cmp al, 0x4f
 ja L
-lea rcx, [D]
+lea rcx, [S:"AoY"]
 movzx edx, al
 movsxd rdx, dword ptr [rcx + rdx*4]
```

### изменена: 0x3c7c6d0 (1801 байт) вызывается из: CPulseInputParameterAdapterWithCPPSignature::vfunc#1, CPulseInputParameterAdapterWithCPPSignature::vfunc#2 | строки: "CPulseInstanceLoadAPI"; "IKV3TransferInterface_GameTime_Load"; "IKV3TransferInterface_EHandle_Load"; "IKV3TransferInterface_Worldspace_Load"; "CKV3TransferInterface_PulseEnum_Load"
было: 0x3c7c690 (1801 байт)
- строки: −"xNZ"
- инструкций: 406 → 406
```diff
@@ -53,5 +53,5 @@
 cmp edx, 0x14
 ja L
-lea rcx, [S:"xNZ"]
+lea rcx, [D]
 movsxd rdx, dword ptr [rcx + rdx*4]
 add rdx, rcx
```

### изменена: 0x3cbc4a0 (989 байт) | строки: "_Target"; "param"; "%g %g %g"; "(null)"; "%g %g %g %g"; "%lld"; "%llu"; "%d %d %d %d"
было: 0x3cbc460 (989 байт)
- строки: −"M*^"
- инструкций: 228 → 228
```diff
@@ -76,5 +76,5 @@
 cmp al, 0x4f
 ja L
-lea rcx, [S:"M*^"]
+lea rcx, [D]
 movzx edx, al
 movsxd rdx, dword ptr [rcx + rdx*4]
```

### изменена: 0x3cc0350 (2479 байт) CBaseLightProbeVolume::vfunc#2 | строки: "box_mins"; "box_maxs"; "moveable"; "handshake"; "indoor_outdoor_level"; "StartDisabled"; "is_selected_in_hammer"; "voxel_size"
было: 0x3cc0310 (2479 байт)
- строки: +"rn^" +"{n^" +"mn^" +"Xn^" +".n^" −"\\n^" −"2n^" −";n^" −"-n^"
- инструкций: 618 → 618
```diff
@@ -202,5 +202,5 @@
 cmp dl, 6
 ja L
-lea rcx, [S:"\\n^"]
+lea rcx, [D]
 movzx edx, dl
 movsxd rdx, dword ptr [rcx + rdx*4]
@@ -231,5 +231,5 @@
 cmp dl, 6
 ja L
-lea rcx, [S:"2n^"]
+lea rcx, [S:"rn^"]
 movzx edx, dl
 movsxd rdx, dword ptr [rcx + rdx*4]
@@ -259,5 +259,5 @@
 cmp dl, 6
 ja L
-lea rcx, [S:";n^"]
+lea rcx, [S:"{n^"]
 movzx edx, dl
 movsxd rdx, dword ptr [rcx + rdx*4]
@@ -287,5 +287,5 @@
 cmp dl, 6
 ja L
-lea rcx, [S:"-n^"]
+lea rcx, [S:"mn^"]
 movzx edx, dl
 movsxd rdx, dword ptr [rcx + rdx*4]
@@ -315,5 +315,5 @@
 cmp dl, 6
 ja L
-lea rcx, [D]
+lea rcx, [S:"Xn^"]
 movzx edx, dl
 movsxd rdx, dword ptr [rcx + rdx*4]
@@ -344,5 +344,5 @@
 cmp dl, 6
 ja L
-lea rcx, [D]
+lea rcx, [S:".n^"]
 movzx edx, dl
 movsxd rdx, dword ptr [rcx + rdx*4]
```

### изменена: 0x3d009a0 (651 байт) | строки: "CUtlVector"; "PointTemplateClientOnlyEntityBehavior_t"; "PointTemplateOwnerSpawnGroupType_t"; "CEntityHandle"; "CEntityOutputTemplate"
было: 0x3d00960 (651 байт)
- строки: −"h7b"
- инструкций: 181 → 181
```diff
@@ -2,5 +2,5 @@
 ja L
 push rbp
-lea rdx, [S:"h7b"]
+lea rdx, [D]
 mov edi, edi
 mov rbp, rsp
```

### изменена: 0x3d22f60 (1712 байт) CEntityOutputTemplate<SndOpEventGuid_t>::vfunc#2 | строки: "m_Value"; "Stack depth limit hit (%d)"; "pQd"; "1Qd"; "public.aabb_min"; "public.aabb_max"
было: 0x3d22f20 (1712 байт)
- строки: +"pQd" +"1Qd" −"0Qd"
- инструкций: 409 → 409
```diff
@@ -65,5 +65,5 @@
 cmp al, 6
 ja L
-lea rdx, [S:"0Qd"]
+lea rdx, [S:"pQd"]
 movzx eax, al
 movsxd rax, dword ptr [rdx + rax*4]
@@ -90,5 +90,5 @@
 cmp al, 6
 ja L
-lea rdx, [D]
+lea rdx, [S:"1Qd"]
 movzx eax, al
 movsxd rax, dword ptr [rdx + rax*4]
```

### изменена: 0x3d305a0 (637 байт) | строки: "\\%e"; "CInfoFan"; "CHandle"; "VectorWS"
было: 0x3d30560 (637 байт)
- строки: +"\\%e"
- инструкций: 147 → 147
```diff
@@ -7,5 +7,5 @@
 cmp edi, 6
 ja L
-lea rdx, [D]
+lea rdx, [S:"\\%e"]
 mov edi, edi
 mov rbx, rsi
```

### изменена: 0x3d30a20 (547 байт) | строки: "8(e"; "CHandle"; "CBasePlayerController"; "CNetworkUtlVectorBase"; "CBasePlayerPawn"
было: 0x3d309e0 (547 байт)
- строки: +"8(e"
- инструкций: 158 → 158
```diff
@@ -2,5 +2,5 @@
 ja L
 push rbp
-lea rdx, [D]
+lea rdx, [S:"8(e"]
 mov edi, edi
 mov rbp, rsp
```

### изменена: 0x3d33c10 (270 байт)
было: 0x3d33bd0 (270 байт)
- строки: −"nZe"
- инструкций: 69 → 69
```diff
@@ -5,5 +5,5 @@
 cmp edi, 6
 ja L
-lea rdx, [S:"nZe"]
+lea rdx, [D]
 mov edi, edi
 mov rbx, rsi
```

### изменена: 0x3d51b90 (183 байт) | строки: "g g"
было: 0x3d51b50 (183 байт)
- строки: +"g g" −"' g"
- инструкций: 55 → 55
```diff
@@ -2,5 +2,5 @@
 ja L
 push rbp
-lea rdx, [S:"' g"]
+lea rdx, [S:"g g"]
 mov edi, edi
 mov rbp, rsp
```

### изменена: 0x3d51cc0 (117 байт) | строки: "9!g"
было: 0x3d51c80 (117 байт)
- строки: +"9!g"
- инструкций: 39 → 39
```diff
@@ -2,5 +2,5 @@
 cmp edx, 6
 ja L
-lea rcx, [D]
+lea rcx, [S:"9!g"]
 push rbp
 mov rdi, rsi
```

### изменена: 0x3d51d40 (561 байт) | строки: "c!g"; "Unsupported KV3 basic type '%s' (%d)!"; "Pointers cannot be used as numeric values"
было: 0x3d51d00 (561 байт)
- строки: +"c!g" −"#!g"
- инструкций: 151 → 151
```diff
@@ -11,5 +11,5 @@
 cmp r8b, 6
 ja L
-lea rdx, [S:"#!g"]
+lea rdx, [S:"c!g"]
 movzx eax, r8b
 movsxd rax, dword ptr [rdx + rax*4]
```

### изменена: 0x3d52040 (227 байт) | строки: "X$g"; "IPhysicsJoint"
было: 0x3d52000 (227 байт)
- строки: +"X$g"
- инструкций: 73 → 73
```diff
@@ -1,5 +1,5 @@
 cmp edi, 6
 ja L
-lea rcx, [D]
+lea rcx, [S:"X$g"]
 mov edi, edi
 push rbp
```

### изменена: 0x3d52740 (190 байт)
было: 0x3d52700 (190 байт)
- строки: −"O+g"
- инструкций: 59 → 59
```diff
@@ -3,5 +3,5 @@
 ja L
 push rbp
-lea rcx, [S:"O+g"]
+lea rcx, [D]
 mov rbp, rsp
 sub rsp, 0x10
```

### изменена: 0x3d52940 (206 байт)
было: 0x3d52900 (206 байт)
- строки: −"C-g"
- инструкций: 55 → 55
```diff
@@ -1,5 +1,5 @@
 cmp edi, 6
 ja L
-lea rcx, [S:"C-g"]
+lea rcx, [D]
 mov edi, edi
 push rbp
```

### изменена: 0x3d53170 (285 байт) | строки: "L5g"; "VectorWS"
было: 0x3d53130 (285 байт)
- строки: +"L5g"
- инструкций: 81 → 81
```diff
@@ -5,5 +5,5 @@
 push rbx
 ja L
-lea rdx, [D]
+lea rdx, [S:"L5g"]
 mov edi, edi
 mov rbx, rsi
```

### изменена: 0x3d533d0 (893 байт) | строки: "@7g"; "InfoForResourceTypeIParticleSystemDefinition"; "CWeakHandle"; "CResourceNameTyped"; "ParticleAttachment_t"; "PrecipitationFilter_t"
было: 0x3d53390 (893 байт)
- строки: +"@7g"
- инструкций: 188 → 188
```diff
@@ -9,5 +9,5 @@
 cmp edi, 6
 ja F
-lea rdx, [D]
+lea rdx, [S:"@7g"]
 mov edi, edi
 mov rbx, rsi
```

### изменена: 0x3d62340 (785 байт) | строки: "Unsupported KV3 basic type '%s' (%d)!"; "Pointers cannot be used as numeric values"
было: 0x3d62300 (785 байт)
- строки: −"R(h"
- инструкций: 219 → 219
```diff
@@ -31,5 +31,5 @@
 cmp bl, 6
 ja L
-lea rdx, [S:"R(h"]
+lea rdx, [D]
 movzx eax, bl
 movsxd rax, dword ptr [rdx + rax*4]
```

### изменена: 0x3d853d0 (243 байт) | строки: "(2j"; "VectorWS"
было: 0x3d85390 (243 байт)
- строки: +"(2j"
- инструкций: 67 → 67
```diff
@@ -1,5 +1,5 @@
 cmp edi, 6
 ja L
-lea rdx, [D]
+lea rdx, [S:"(2j"]
 mov edi, edi
 push rbp
```

### изменена: 0x3d85f30 (243 байт) | строки: "<=j"; "VectorWS"
было: 0x3d85ef0 (243 байт)
- строки: +"<=j"
- инструкций: 76 → 76
```diff
@@ -2,5 +2,5 @@
 ja L
 push rbp
-lea rdx, [D]
+lea rdx, [S:"<=j"]
 mov edi, edi
 mov rbp, rsp
```

### изменена: 0x3d861c0 (307 байт) | строки: "VectorWS"
было: 0x3d86180 (307 байт)
- строки: −"x?j"
- инструкций: 94 → 94
```diff
@@ -2,5 +2,5 @@
 ja L
 push rbp
-lea rdx, [S:"x?j"]
+lea rdx, [D]
 mov edi, edi
 mov rbp, rsp
```

### изменена: 0x3d86940 (183 байт) | строки: "cGj"
было: 0x3d86900 (183 байт)
- строки: +"cGj" −"#Gj"
- инструкций: 55 → 55
```diff
@@ -2,5 +2,5 @@
 ja L
 push rbp
-lea rdx, [S:"#Gj"]
+lea rdx, [S:"cGj"]
 mov edi, edi
 mov rbp, rsp
```

### изменена: 0x3d86a70 (98 байт) | строки: "\"Hj"
было: 0x3d86a30 (98 байт)
- строки: +"\"Hj"
- инструкций: 36 → 36
```diff
@@ -2,5 +2,5 @@
 cmp edx, 6
 ja L
-lea rcx, [D]
+lea rcx, [S:"\"Hj"]
 push rbp
 mov rdi, rsi
```

### изменена: 0x3d86ae0 (98 байт) | строки: "vHj"
было: 0x3d86aa0 (98 байт)
- строки: +"vHj" −"6Hj"
- инструкций: 36 → 36
```diff
@@ -2,5 +2,5 @@
 cmp edx, 6
 ja L
-lea rcx, [S:"6Hj"]
+lea rcx, [S:"vHj"]
 push rbp
 mov rdi, rsi
```

### изменена: 0x3d86be0 (176 байт)
было: 0x3d86ba0 (176 байт)
- строки: −"hIj"
- инструкций: 45 → 45
```diff
@@ -1,5 +1,5 @@
 cmp edi, 6
 ja L
-lea rcx, [S:"hIj"]
+lea rcx, [D]
 mov edi, edi
 push rbp
```

### изменена: 0x3d86cc0 (117 байт) | строки: "1Jj"
было: 0x3d86c80 (117 байт)
- строки: +"1Jj"
- инструкций: 39 → 39
```diff
@@ -2,5 +2,5 @@
 cmp edx, 6
 ja L
-lea rcx, [D]
+lea rcx, [S:"1Jj"]
 push rbp
 mov rdi, rsi
```

### изменена: 0x3d86f10 (136 байт) | строки: "xLj"
было: 0x3d86ed0 (136 байт)
- строки: +"xLj" −"8Lj"
- инструкций: 43 → 43
```diff
@@ -2,5 +2,5 @@
 cmp edx, 6
 ja L
-lea rcx, [S:"8Lj"]
+lea rcx, [S:"xLj"]
 push rbp
 mov rax, rsi
```

### изменена: 0x3d88040 (206 байт)
было: 0x3d88000 (206 байт)
- строки: −"s]j"
- инструкций: 62 → 62
```diff
@@ -2,5 +2,5 @@
 ja L
 push rbp
-lea rdx, [S:"s]j"]
+lea rdx, [D]
 mov edi, edi
 mov rbp, rsp
```

### изменена: 0x3d887d0 (302 байт) | строки: "3ej"
было: 0x3d88790 (302 байт)
- строки: +"3ej"
- инструкций: 71 → 71
```diff
@@ -2,5 +2,5 @@
 ja L
 push rbp
-lea rdx, [D]
+lea rdx, [S:"3ej"]
 mov edi, edi
 mov rbp, rsp
```

### изменена: 0x3d88fe0 (907 байт) | строки: "Dlj"
было: 0x3d88fa0 (907 байт)
- строки: +"Dlj"
- инструкций: 252 → 252
```diff
@@ -9,5 +9,5 @@
 movsxd r13, edx
 push r12
-lea rdx, [D]
+lea rdx, [S:"Dlj"]
 mov r12d, ecx
 push rbx
```

### изменена: 0x3d89e50 (435 байт) | строки: "`zj"; "CPlayerSlot"; "CUtlVector"
было: 0x3d89e10 (435 байт)
- строки: +"`zj" −" zj"
- инструкций: 115 → 115
```diff
@@ -1,5 +1,5 @@
 cmp edi, 6
 ja L
-lea rdx, [S:" zj"]
+lea rdx, [S:"`zj"]
 mov edi, edi
 push rbp
```

### изменена: 0x3d957b0 (659 байт) | строки: "t2k"; "CTakeDamageInfo"; "DestructiblePartDamageRequest_t"; "CUtlLeanVector"; "VectorWS"; "TakeDamageFlags_t"; "HitGroup_t"
было: 0x3d95770 (659 байт)
- строки: +"t2k" −"42k"
- инструкций: 151 → 151
```diff
@@ -1,5 +1,5 @@
 cmp edi, 6
 ja L
-lea rdx, [S:"42k"]
+lea rdx, [S:"t2k"]
 mov edi, edi
 push rbp
```

### изменена: 0x3da4f40 (766 байт)
было: 0x3da4f00 (766 байт)
- строки: −"t(l"
- инструкций: 201 → 201
```diff
@@ -9,5 +9,5 @@
 movsxd r12, edx
 push rbx
-lea rdx, [S:"t(l"]
+lea rdx, [D]
 mov rbx, rsi
 sub rsp, 0x10
```

### изменена: 0x3daaaf0 (961 байт) | строки: "%g %g %g"; "(null)"; "%g %g %g %g"; "unknown_variant_type"; "1zl"; "%lld"; "%llu"; "%d %d %d %d"
было: 0x3daaab0 (961 байт)
- строки: +"1zl"
- инструкций: 213 → 213
```diff
@@ -91,5 +91,5 @@
 cmp al, 0x47
 ja L
-lea rdx, [D]
+lea rdx, [S:"1zl"]
 movzx eax, al
 movsxd rax, dword ptr [rdx + rax*4]
```

### изменена: 0x3db8730 (851 байт) | строки: "<Um"; "%llu"
было: 0x3db86f0 (851 байт)
- строки: +"<Um"
- инструкций: 190 → 190
```diff
@@ -21,5 +21,5 @@
 mov rbx, rax
 je L
-lea r13, [D]
+lea r13, [S:"<Um"]
 nop dword ptr [rax + rax]
 mov qword ptr [rbp - 0xc0], 0
```

### изменена: 0x3df7d00 (407 байт) вызывается из: CVScriptGameSystem::vfunc#85 | строки: "D/q"
было: 0x3df7cc0 (407 байт)
- строки: +"D/q"
- инструкций: 104 → 104
```diff
@@ -31,5 +31,5 @@
 ja L
 movzx eax, word ptr [rax + 0x28]
-lea rdx, [D]
+lea rdx, [S:"D/q"]
 movsxd rax, dword ptr [rdx + rax*4]
 add rax, rdx
```

### изменена: 0x3df99a0 (547 байт) | строки: "hKq"; "CHandle"; "CEnvSoundscapeTriggerable"; "CBasePlayerPawn"; "CUtlVector"
было: 0x3df9960 (547 байт)
- строки: +"hKq" −"(Kq"
- инструкций: 144 → 144
```diff
@@ -2,5 +2,5 @@
 ja L
 push rbp
-lea rdx, [S:"(Kq"]
+lea rdx, [S:"hKq"]
 mov edi, edi
 mov rbp, rsp
```

### изменена: 0x3e1ac80 (4702 байт) | строки: "classname"; "PXs"; "connections"; "attributes"; "X^s"
было: 0x3e1ac40 (4702 байт)
- строки: +"PXs" +"X^s"
- инструкций: 1086 → 1086
```diff
@@ -208,5 +208,5 @@
 cmp r14b, 0x4f
 ja L
-lea rsi, [D]
+lea rsi, [S:"PXs"]
 movsxd rax, dword ptr [rsi + r14*4]
 add rax, rsi
@@ -617,5 +617,5 @@
 cmp al, 0x4f
 ja L
-lea rsi, [D]
+lea rsi, [S:"X^s"]
 movzx edx, al
 movsxd rdx, dword ptr [rsi + rdx*4]
```

### изменена: 0x3e4b3f0 (2071 байт) вызывается из: CWorldGameSystem::vfunc#15 | строки: "_dotatilegrid_minheight"; "_dotatilegrid_maxheight"; "_dotatilegrid_stepheight"
было: 0x3e4b3b0 (2071 байт)
- строки: −"rZv" −"nZv"
- инструкций: 485 → 485
```diff
@@ -62,5 +62,5 @@
 cmp al, 6
 ja L
-lea rdx, [S:"rZv"]
+lea rdx, [D]
 movzx eax, al
 movsxd rax, dword ptr [rdx + rax*4]
@@ -96,5 +96,5 @@
 cmp al, 6
 ja L
-lea rdx, [S:"nZv"]
+lea rdx, [D]
 movzx eax, al
 movsxd rax, dword ptr [rdx + rax*4]
```

### изменена: 0x3e4c240 (2322 байт) CWorldGameSystem::vfunc#15 | строки: "maxpropscreenwidth"; "minpropscreenwidth"; "newunit"; "startdark"; "startcolor"; "update_nav_obstacle_splits_only_on_final_tick"; "_dotatilegrid_heightshift"; "_dotatilegrid_fogbounds_min"
было: 0x3e4c200 (2322 байт)
- строки: −"\\iv"
- инструкций: 567 → 567
```diff
@@ -187,5 +187,5 @@
 cmp al, 6
 ja L
-lea rdx, [S:"\\iv"]
+lea rdx, [D]
 movzx eax, al
 movsxd rax, dword ptr [rdx + rax*4]
```

### изменена: 0x3e6cde0 (211 байт) | строки: "GameTime_t"
было: 0x3e6cda0 (211 байт)
- строки: −"dYx"
- инструкций: 63 → 63
```diff
@@ -1,5 +1,5 @@
 cmp edi, 6
 ja L
-lea rdx, [S:"dYx"]
+lea rdx, [D]
 mov edi, edi
 push rbp
```

### изменена: 0x3e6cec0 (187 байт) | строки: "hZx"; "Disposition_t"
было: 0x3e6ce80 (187 байт)
- строки: +"hZx" −"(Zx"
- инструкций: 59 → 59
```diff
@@ -1,5 +1,5 @@
 cmp edi, 6
 ja L
-lea rdx, [S:"(Zx"]
+lea rdx, [S:"hZx"]
 mov edi, edi
 push rbp
```

### изменена: 0x3e6d0b0 (275 байт) | строки: "D\\x"; "VectorWS"
было: 0x3e6d070 (275 байт)
- строки: +"D\\x"
- инструкций: 84 → 84
```diff
@@ -1,5 +1,5 @@
 cmp edi, 6
 ja L
-lea rcx, [D]
+lea rcx, [S:"D\\x"]
 mov edi, edi
 push rbp
```

### изменена: 0x3e6dcc0 (451 байт) | строки: "$hx"; "CEconWearable"; "CHandle"; "CNetworkUtlVectorBase"; "RelationshipOverride_t"; "CUtlVector"; "Hull_t"; "CMovementStatsProperty"
было: 0x3e6dc80 (451 байт)
- строки: +"$hx"
- инструкций: 129 → 129
```diff
@@ -2,5 +2,5 @@
 ja L
 push rbp
-lea rdx, [D]
+lea rdx, [S:"$hx"]
 mov edi, edi
 mov rbp, rsp
```

### изменена: 0x3e6eeb0 (183 байт) | строки: "?zx"
было: 0x3e6ee70 (183 байт)
- строки: +"?zx"
- инструкций: 55 → 55
```diff
@@ -2,5 +2,5 @@
 ja L
 push rbp
-lea rdx, [D]
+lea rdx, [S:"?zx"]
 mov edi, edi
 mov rbp, rsp
```

### изменена: 0x3e6efe0 (183 байт) | строки: "S{x"
было: 0x3e6efa0 (183 байт)
- строки: +"S{x"
- инструкций: 55 → 55
```diff
@@ -2,5 +2,5 @@
 ja L
 push rbp
-lea rdx, [D]
+lea rdx, [S:"S{x"]
 mov edi, edi
 mov rbp, rsp
```

### изменена: 0x3e6f180 (98 байт) | строки: "f|x"
было: 0x3e6f140 (98 байт)
- строки: +"f|x" −"&|x"
- инструкций: 36 → 36
```diff
@@ -2,5 +2,5 @@
 cmp edx, 6
 ja L
-lea rcx, [S:"&|x"]
+lea rcx, [S:"f|x"]
 push rbp
 mov rdi, rsi
```

### изменена: 0x3e6f3b0 (171 байт) | строки: "@~x"; "HitGroup_t"
было: 0x3e6f370 (171 байт)
- строки: +"@~x"
- инструкций: 54 → 54
```diff
@@ -1,5 +1,5 @@
 cmp edi, 6
 ja L
-lea rdx, [D]
+lea rdx, [S:"@~x"]
 mov edi, edi
 push rbp
```

### изменена: 0x3e7ba30 (436 байт)
было: 0x3e7b9f0 (436 байт)
- строки: −"y?y"
- инструкций: 100 → 100
```diff
@@ -5,5 +5,5 @@
 cmp edi, 6
 ja L
-lea rdx, [S:"y?y"]
+lea rdx, [D]
 mov edi, edi
 mov rbx, rsi
```

### изменена: 0x3eaa7a0 (769 байт) вызывается из: CAnimGraphControllerBase::vfunc#2, CEmptyGraphController::vfunc#2, EventGrantDefinition_Emoticon_t::vfunc#2 | строки: "\".|"; "Unsupported KV3 basic type '%s' (%d)!"; "Pointers cannot be used as numeric values"
было: 0x3eaa760 (769 байт)
- строки: +"\".|" −"z+|"
- инструкций: 220 → 220
```diff
@@ -20,5 +20,5 @@
 cmp bl, 6
 ja L
-lea rdx, [S:"z+|"]
+lea rdx, [D]
 movzx eax, bl
 movsxd rax, dword ptr [rdx + rax*4]
@@ -31,5 +31,5 @@
 cmp bl, 6
 ja L
-lea rdx, [D]
+lea rdx, [S:"\".|"]
 movzx eax, bl
 movsxd rax, dword ptr [rdx + rax*4]
```

### изменена: 0x3eacdb0 (856 байт) | строки: "|Q|"
было: 0x3eacd70 (856 байт)
- строки: +"|Q|" −"<Q|"
- инструкций: 221 → 221
```diff
@@ -10,5 +10,5 @@
 movsxd r12, edx
 push rbx
-lea rdx, [S:"<Q|"]
+lea rdx, [S:"|Q|"]
 mov rbx, rsi
 sub rsp, 0x58
```

### изменена: 0x48551b0 (1111 байт) CDOTA_Modifier_Batrider_FlamingLasso::vfunc#2 | строки: "modifier_faceless_void_chronosphere_freeze"; "modifier_enigma_black_hole_pull"
было: 0x4855150 (1199 байт)
- числа в инструкциях: −-1 −-2 −9 −0x3f −0x1ff −0x70
- поля объектов: −0x1b14 −0x1b14 −0x10
- прямых вызовов: 19 → 20
- инструкций: 287 → 267
```diff
@@ -48,26 +48,11 @@
 call F
 movss dword ptr [rbp - 0x64], xmm0
-mov ecx, dword ptr [rbx + 0x1b14]
-cmp ecx, -1
-je L
-mov rsi, qword ptr [D]
-test rsi, rsi
-je L
-cmp ecx, -2
-je L
-movzx eax, word ptr [rbx + 0x1b14]
-mov rdx, rax
-shr rdx, 9
-and edx, 0x3f
-mov rdx, qword ptr [rsi + rdx*8]
-test rdx, rdx
-je L
-and eax, 0x1ff
-imul rax, rax, 0x70
-add rax, rdx
-cmp ecx, dword ptr [rax + 0x10]
-jne L
-mov r13, qword ptr [rax]
+lea r13, [rbx + 0x1b14]
 mov rdi, r13
+call F
+test rax, rax
+mov rdi, rax
+je L
+mov rdi, qword ptr [rax]
 call F
 pxor xmm0, xmm0
@@ -97,5 +82,4 @@
 pop rbp
 ret
-nop word ptr [rax + rax]
 mov rdi, rbx
 call F
@@ -154,27 +138,27 @@
 mov rdi, r12
 call F
-mov edx, dword ptr [rbx + 0x1b14]
+mov ecx, dword ptr [rbx + 0x1b14]
 mov r14, rax
-cmp edx, -1
+cmp ecx, -1
 je L
 mov rsi, qword ptr [D]
 test rsi, rsi
 je L
```
(ещё 64 строк диффа: so-query.py fdiff libserver.so 0x48551b0)

### изменена: 0x48592c0 (8816 байт) | строки: "Hero_Batrider.Firefly.Loop"
было: 0x4858ee0 (9536 байт)
- константы из данных (числа логики): −0x00000000000000090000000000000000
- числа в инструкциях: −0xffffffff −0 −0 −0 −0 −0 −0 −0 (и ещё 19)
- прямых вызовов: 97 → 90
- цели вызовов: −0x47ef7e0 −0x480ec20
- инструкций: 1498 → 1386
```diff
@@ -1,114 +1,2 @@
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
-mov qword ptr [D], 0
-mov qword ptr [D], 0
```
(ещё 64 строк диффа: so-query.py fdiff libserver.so 0x48592c0)

### изменена: 0x485e340 (3963 байт) | строки: "PlayerID_t"
было: 0x485ed80 (1083 байт)
- константы из данных (числа логики): +0x00000000000000090000000000000000 +0x00000000000000090000000000000000 +0x00000000000000090000000000000000 +0x00000000000000090000000000000000
- числа в инструкциях: +0xffffffff +0xffffffff +0xffffffff +0xffffffff +0 +0 +0 +0 (и ещё 100)
- прямых вызовов: 12 → 40
- цели вызовов: +__cxa_guard_acquire() +0x6a429b0 +__cxa_atexit() +__cxa_guard_release() +0x59dbe20 +0x4811360 +0x480efa0 +0x3bbc200 +0x4811370 +0x480efc0 +0x4811380 +0x480efe0 +0x4811390 +0x480f000
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
+mov qword ptr [D], 0
+mov qword ptr [D], 0
+mov qword ptr [D], 0
+mov qword ptr [D], 0
+mov qword ptr [D], 0
+mov qword ptr [D], 0
+mov qword ptr [D], 0
+mov qword ptr [D], 0
+mov qword ptr [D], 0
+mov qword ptr [D], 0
+mov qword ptr [D], 0
+mov qword ptr [D], 0
+mov qword ptr [D], 0
+mov qword ptr [D], 0
+mov qword ptr [D], 0x20
+mov qword ptr [D], 0
+mov qword ptr [D], 0
```
(ещё 400 строк диффа: so-query.py fdiff libserver.so 0x485e340)

### изменена: 0x48afc30 (2372 байт) вызывается из: CDOTA_Ability_Primal_Companion::OnSpellStart, CDOTA_Modifier_Brewmaster_PrimalSplitDelay::OnDestroy | строки: "brewmaster_drunken_brawler"; "give_brawler_passive"; "duration"; "primal_split_cancel"; "brewmaster_primal_split_cancel"; "brewmaster_storm_dispel_magic"; "brewmaster_storm_cyclone"; "brewmaster_storm_wind_walk"
было: 0x48afb30 (2180 байт)
- строки: +"duration" +"scepter_brewling_items" +"modifier_brewmaster_drunken_brawler_brewed_up" +"brewed_up_duration"
- константы из данных (числа логики): +-1 +-1
- числа в инструкциях: +1
- прямых вызовов: 96 → 106
- инструкций: 562 → 608
```diff
@@ -495,5 +495,51 @@
 mov esi, dword ptr [rbp - 0x88]
 call F
-jmp L
+mov rdi, qword ptr [rbp - 0x68]
+call F
+mov rdi, rax
+call F
+test al, al
+je L
+mov rdi, qword ptr [rbp - 0x68]
+xor r9d, r9d
+xor r8d, r8d
+xor ecx, ecx
+movss xmm0, dword ptr [K:-1]
+mov edx, 1
+lea rsi, [S:"scepter_brewling_items"]
+call F
+test eax, eax
+jg L
+lea r12, [rbp - 0x50]
+xor ecx, ecx
+xor edx, edx
+lea rsi, [S:"modifier_brewmaster_drunken_brawler_brewed_up"]
+mov rdi, r12
+call F
+xor ecx, ecx
+xor edx, edx
+mov rdi, r13
+movss xmm0, dword ptr [K:-1]
+lea rsi, [S:"brewed_up_duration"]
+call F
+lea rsi, [S:"duration"]
+mov rdi, r12
+call F
+mov rdi, r12
+call F
+mov rdi, qword ptr [rbp - 0x68]
+mov qword ptr [rbp - 0x80], rax
+call F
+mov rcx, qword ptr [rbp - 0x80]
+mov rdi, rbx
+xor r9d, r9d
+mov rsi, rax
+mov r8, r12
+mov rdx, r13
+call F
+mov rdi, r12
+call F
+jmp L
+nop dword ptr [rax]
```
(ещё 2 строк диффа: so-query.py fdiff libserver.so 0x48afc30)

### изменена: 0x48d8d60 (2336 байт) CDOTA_Modifier_Batrider_Firefly::OnIntervalThink | строки: "particles/units/heroes/hero_batrider/batrider_firefly_debuff.vpcf"
было: 0x48d8ba0 (2356 байт)
- числа в инструкциях: +0 −0x3fffffff
- виртуальные вызовы: −0x20 (слот 4)
- поля объектов: −0x1b38
- цели вызовов: +0x44e3070
- инструкций: 477 → 473
```diff
@@ -7,5 +7,5 @@
 mov r12, rdi
 push rbx
-sub rsp, 0x128
+sub rsp, 0x118
 call F
 mov rdi, r12
@@ -36,5 +36,4 @@
 mov edi, eax
 call F
-mov edx, dword ptr [r12 + 0x1b38]
 movaps xmm1, xmm0
 movss xmm0, dword ptr [r12 + 0x1b20]
@@ -43,4 +42,5 @@
 je L
 jbe L
+mov edx, dword ptr [r12 + 0x1b38]
 test edx, edx
 jle L
@@ -147,7 +147,9 @@
 pop rbp
 jmp F
+mov ecx, dword ptr [r12 + 0x1b38]
+mov dword ptr [rbp - 0xfc], 0
 addss xmm0, dword ptr [r12 + 0x1b14]
-test edx, edx
 movss dword ptr [r12 + 0x1b20], xmm0
+test ecx, ecx
 jle L
 xor r13d, r13d
@@ -155,11 +157,10 @@
 xor ebx, ebx
 mov qword ptr [rbp - 0x120], 0
-mov dword ptr [rbp - 0x118], 0
+mov dword ptr [rbp - 0x114], 0
 mov r14, r13
-mov dword ptr [rbp - 0x114], 0
-mov byte ptr [rbp - 0x13d], 0
-movss dword ptr [rbp - 0x13c], xmm2
-movss dword ptr [rbp - 0x144], xmm1
-nop word ptr [rax + rax]
+mov byte ptr [rbp - 0x139], 0
+movss dword ptr [rbp - 0x118], xmm2
+movss dword ptr [rbp - 0x140], xmm1
+nop
 mov qword ptr [rbp - 0xf0], 0
 mov rdi, r12
@@ -364,22 +365,18 @@
 cmp dword ptr [r12 + 0x1b38], eax
 jg L
-movss xmm2, dword ptr [rbp - 0x13c]
```
(ещё 123 строк диффа: so-query.py fdiff libserver.so 0x48d8d60)

### изменена: 0x4ac8100 (2664 байт) CDOTA_Ability_EarthSpirit_RollingBoulder::vfunc#371 | строки: "modifier_earthspirit_petrify"; "npc_dota_earth_spirit_stone"; "earth_spirit_stone_caller"; "particles/units/heroes/hero_earth_spirit/espirit_rollingboulder_stone.vpcf"; "Hero_EarthSpirit.RollingBoulder.Stone"; "Hero_EarthSpirit.RollingBoulder.Target"; "Hero_EarthSpirit.RollingBoulder.Damage"; "stun_duration"
было: 0x4ac7f40 (2680 байт)
- цели вызовов: +0x44209b0
- инструкций: 577 → 573
```diff
@@ -74,12 +74,8 @@
 call qword ptr [rax + 0xe30]
 lea rsi, [S:"npc_dota_earth_spirit_stone"]
-cmp rax, rsi
-je L
-test rax, rax
-je L
-mov rdi, rax
-call F
-test eax, eax
-jne L
+mov rdi, rax
+call F
+test al, al
+je L
 movss xmm1, dword ptr [rbx + 0x8ac]
 mov rdi, rbx
@@ -214,5 +210,5 @@
 xor esi, esi
 call F
-nop word ptr [rax + rax]
+nop dword ptr [rax]
 xor eax, eax
 lea rsp, [rbp - 0x28]
```

### изменена: 0x4aced30 (10020 байт) вызывается из: CDOTA_Modifier_AbyssalUnderlord_Underling_Spawn_Thinker::OnIntervalThink | строки: "abyssal_underlord_dark_portal"; "DOTA_Item.Necronomicon.Activate"; "modifier_underlord_underling_autoattack"; "target"; "duration"; "npc_dota_necronomicon_archer_%d"; "particles/items_fx/necronomicon_spawn.vpcf"; "necronomicon_archer_aoe"
было: 0x4aceb80 (10004 байт)
- строки: +"<NoAbilityName>"
- цели вызовов: +0x44209b0
- инструкций: 1980 → 1981
```diff
@@ -1751,15 +1751,15 @@
 jne L
 mov rax, qword ptr [rbx + 0x840]
+lea rdi, [S:"<NoAbilityName>"]
 test rax, rax
 je L
 mov rdi, qword ptr [rax]
+lea rax, [D]
 test rdi, rdi
-je L
+cmove rdi, rax
 lea rsi, [S:"grimstroke_ink_creature"]
-cmp rdi, rsi
-je L
-call F
-test eax, eax
-jne L
+call F
+test al, al
+je L
 mov rdi, qword ptr [rbp - 0x78]
 call F
@@ -1788,5 +1788,5 @@
 pop rbp
 jmp F
-nop
+nop dword ptr [rax]
 lea r12, [D]
 jmp L
@@ -1798,4 +1798,5 @@
 mov dword ptr [r14 + 0x1368], 0xffffffff
 jmp L
+nop dword ptr [rax + rax]
 mov rax, qword ptr [K:0x7f7fffff7f7fffff]
 movss xmm1, dword ptr [K:3.402823e+38]
```

### изменена: 0x4addff0 (3408 байт) CDOTA_Modifier_EarthSpirit_Magnetize::OnIntervalThink | строки: "Hero_EarthSpirit.Magnetize.Target.Tick"; "particles/units/heroes/hero_earth_spirit/espirit_magnetize_target.vpcf"; "attach_hitloc"; "modifier_earthspirit_petrify"; "npc_dota_earth_spirit_stone"; "modifier_earth_spirit_stone_thinker"; "modifier_earth_spirit_magnetize"; "duration"
было: 0x4adde30 (3136 байт)
- константы из данных (числа логики): +-1,-1,3.402823e+38,3.402823e+38 +0x00000000ffffffff
- числа в инструкциях: +0 +0 +0 +0 +0 +0 +0 +0 (и ещё 5)
- прямых вызовов: 117 → 118
- цели вызовов: +0x552c270 −0x3bc4370
- инструкций: 722 → 744
```diff
@@ -7,10 +7,10 @@
 push r12
 push rbx
-sub rsp, 0x98
+sub rsp, 0x118
 call F
 test rax, rax
 je L
 movzx eax, byte ptr [r15 + 0x1b3c]
-lea rbx, [rbp - 0x70]
+lea rbx, [rbp - 0xf0]
 test al, al
 jne L
@@ -27,5 +27,5 @@
 mov rdi, r15
 mulss xmm0, dword ptr [r15 + 0x1afc]
-movss dword ptr [rbp - 0xa8], xmm0
+movss dword ptr [rbp - 0x128], xmm0
 call F
 mov rdi, r15
@@ -43,5 +43,5 @@
 movq xmm1, qword ptr [K:0x0000000000000000]
 movss xmm2, dword ptr [K:0]
-movss xmm0, dword ptr [rbp - 0xa8]
+movss xmm0, dword ptr [rbp - 0x128]
 call F
 mov rdi, r15
@@ -57,5 +57,5 @@
 lea rdx, [S:"Hero_EarthSpirit.Magnetize.Target.Tick"]
 xor ecx, ecx
-lea rdi, [rbp - 0xa0]
+lea rdi, [rbp - 0x120]
 mov rsi, rax
 call F
@@ -101,5 +101,5 @@
 add rsp, 0x20
 call F
-lea rcx, [rbp - 0x50]
+lea rcx, [rbp - 0xd0]
 mov edx, 2
 mov esi, r12d
@@ -107,7 +107,7 @@
 mov rdi, rax
 movsldup xmm1, xmm0
-movss dword ptr [rbp - 0x48], xmm0
+movss dword ptr [rbp - 0xc8], xmm0
 pxor xmm0, xmm0
-movlps qword ptr [rbp - 0x50], xmm1
+movlps qword ptr [rbp - 0xd0], xmm1
 call F
 sub rsp, 8
```
(ещё 415 строк диффа: so-query.py fdiff libserver.so 0x4addff0)

### изменена: 0x4ae1670 (3571 байт) CDOTA_Modifier_Disruptor_Thunder_Strike::OnIntervalThink | строки: "particles/units/heroes/hero_disruptor/disruptor_thunder_strike_bolt.vpcf"; "attach_hitloc"; "slow_duration"; "modifier_disruptor_thunderstrike_slow"; "duration"; "particles/units/heroes/hero_disruptor/disruptor_thunder_strike_aoe.vpcf"; "Hero_Disruptor.ThunderStrike.Target"; "modifier_disruptor_kinetic_field"
было: 0x4ae13b0 (3659 байт)
- числа в инструкциях: −0 −3 −1
- поля объектов: −0x5d1 −0xd3c −0x175a −0xd58
- цели вызовов: +0x44c0900
- инструкций: 786 → 764
```diff
@@ -401,5 +401,16 @@
 cmp dword ptr [rbp - 0x164], 1
 movzx r14d, byte ptr [rbp - 0x166]
-jg L
+jle L
+mov rdi, r12
+call F
+mov rdi, rax
+call F
+xor r9d, r9d
+mov ecx, 1
+xor esi, esi
+movzx r8d, byte ptr [rbp - 0x165]
+mov rdi, rax
+mov edx, 0x227
+call F
 mov rdi, r12
 call F
@@ -433,5 +444,5 @@
 pop rbp
 ret
-nop dword ptr [rax]
+nop dword ptr [rax + rax]
 xor r14d, r14d
 cmp byte ptr [rbx + 0x5d1], 3
@@ -651,42 +662,9 @@
 jmp L
 nop dword ptr [rax + rax]
-mov rdi, r12
-movzx ebx, byte ptr [rbp - 0x165]
-call F
-test rax, rax
-mov rdi, rax
-je L
-cmp byte ptr [rax + 0x5d1], 3
-jne L
-test byte ptr [rax + 0xd3c], 1
-jne L
-mov rax, qword ptr [rax]
-lea rdx, [T]
-mov rax, qword ptr [rax + 0xd58]
-cmp rax, rdx
-jne L
-xor edi, edi
-xor r9d, r9d
-mov r8d, ebx
-mov ecx, 1
-mov edx, 0x227
-xor esi, esi
-call F
-jmp L
```
(ещё 18 строк диффа: so-query.py fdiff libserver.so 0x4ae1670)

### изменена: 0x4afc070 (3300 байт) CDOTA_Ability_Hoodwink_AcornShot::vfunc#371 | строки: "source_projectile_handle"; "debuff_duration"; "modifier_hoodwink_acorn_shot_slow"; "duration"; "special_bonus_unique_hoodwink_acorn_shot_armor_corruption"; "modifier_hoodwink_acorn_shot_armor_corruption"; "modifier_hoodwink_acorn_shot_damage"; "Hero_Hoodwink.AcornShot.Target"
было: 0x4afbe30 (3218 байт)
- прямых вызовов: 66 → 68
- цели вызовов: +0x50775e0 +0x5077fe0
- инструкций: 748 → 766
```diff
@@ -6,6 +6,6 @@
 mov r15, rsi
 push r14
-lea r14, [rbp - 0x50]
 push r13
+lea r13, [rbp - 0x50]
 push r12
 push rbx
@@ -13,5 +13,5 @@
 sub rsp, 0x68
 mov rdi, qword ptr [rsi + 0x20]
-mov rsi, r14
+mov rsi, r13
 mov qword ptr [rbp - 0x48], rax
 mov qword ptr [rbp - 0x50], 0xffffffffee749ffe
@@ -27,6 +27,6 @@
 je L
 mov rdx, qword ptr [rbx + 0x870]
-movsxd r10, ecx
-movsxd rax, r10d
+mov r14d, ecx
+movsxd rax, r14d
 lea rax, [rax + rax*2]
 shl rax, 4
@@ -56,17 +56,18 @@
 cmp ecx, dword ptr [rax + 0x10]
 jne L
-mov r13, qword ptr [rax]
-test r13, r13
-je L
-cmp byte ptr [r13 + 0x5d1], 3
+mov r10, qword ptr [rax]
+test r10, r10
+je L
+cmp byte ptr [r10 + 0x5d1], 3
 jne L
 test sil, sil
 jne L
-movzx eax, byte ptr [r13 + 0x174c]
-mov rdx, qword ptr [r13 + 0x1248]
+movzx eax, byte ptr [r10 + 0x174c]
+mov rdx, qword ptr [r10 + 0x1248]
 test al, al
 je L
-lea r10, [r10 + r10*2]
-shl r10, 4
+movsxd r11, r14d
+lea r11, [r11 + r11*2]
+shl r11, 4
 and dh, 2
 jne L
```
(ещё 1087 строк диффа: so-query.py fdiff libserver.so 0x4afc070)

### изменена: 0x4eb5680 (586 байт) вызывается из: CDOTA_Modifier_Item_Silver_Edge::vfunc#97 | строки: "modifier_silver_edge_debuff"; "backstab_duration"; "duration"; "DOTA_Item.SilverEdge.Target"; "modifier_item_silver_edge_windwalk"
было: 0x4eb1a00 (488 байт)
- строки: +"backstab_duration"
- виртуальные вызовы: +0xf78 (слот 495) +0x1f0 (слот 62)
- прямых вызовов: 13 → 19
- цели вызовов: +0x3bbd2f0
- инструкций: 123 → 144
```diff
@@ -81,10 +81,27 @@
 test eax, 0x193
 je L
+mov rdi, r12
+call F
+mov rdi, r12
+mov r13, rax
+call F
+test rax, rax
+je L
+mov rdi, r12
+call F
+mov rsi, r13
+mov rdi, rax
+mov rax, qword ptr [rax]
+call qword ptr [rax + 0xf78]
+lea rsi, [r12 + 0x1b10]
+mov rdi, r13
+lea r15, [S:"modifier_silver_edge_debuff"]
 lea r13, [rbp - 0x50]
+lea rdx, [S:"backstab_duration"]
+call F
 xor ecx, ecx
 xor edx, edx
-lea r15, [S:"modifier_silver_edge_debuff"]
+mov rsi, r15
 mov rdi, r13
-mov rsi, r15
 call F
 lea rsi, [S:"duration"]
@@ -119,5 +136,9 @@
 call F
 jmp L
-nop dword ptr [rax]
+nop word ptr cs:[rax + rax]
 xor r14d, r14d
 jmp L
+mov rax, qword ptr [r12]
+mov rdi, r12
+call qword ptr [rax + 0x1f0]
+jmp L
```

### изменена: 0x4eb6d50 (237 байт) CDOTA_Modifier_Item_Skadi::OnCreated | строки: "bonus_all_stats"; "bonus_health"; "bonus_mana"; "cold_duration"
было: 0x4eb5da0 (218 байт)
- числа в инструкциях: +0xffffffff
- поля объектов: +0x1af8
- цели вызовов: +0x3bbdb70 "AbilityManaCost"; "AbilityHealthCost"
- инструкций: 56 → 63
```diff
@@ -9,9 +9,16 @@
 mov rax, qword ptr [rbx]
 call qword ptr [rax + 0x1f0]
-lea rsi, [rbx + 0x1af8]
+xor eax, eax
+test r12, r12
+je L
+xor r9d, r9d
+xor r8d, r8d
+xor ecx, ecx
+lea rsi, [S:"bonus_all_stats"]
+mov edx, 0xffffffff
 mov rdi, r12
-lea rdx, [S:"bonus_all_stats"]
 call F
 mov rdi, rbx
+mov dword ptr [rbx + 0x1af8], eax
 call F
 mov rdi, rbx
```

### изменена: 0x4eb6040 (461 байт) CDOTA_Modifier_Item_Skypiercer::OnCreated | строки: "bonus_strength"; "bonus_armor"; "bonus_health_regen"; "hp_regen_amp"; "slow_resistance"; "bonus_evasion"; "buff_cooldown_acceleration_pct"; "close_radius"
было: 0x4eb5e80 (485 байт)
- числа в инструкциях: −0xffffffff
- поля объектов: −0x1b00
- инструкций: 121 → 113
```diff
@@ -37,16 +37,8 @@
 mov rax, qword ptr [rbx]
 call qword ptr [rax + 0x1f0]
-test r12, r12
-pxor xmm1, xmm1
-je L
-xor r9d, r9d
-xor r8d, r8d
-xor ecx, ecx
-lea rsi, [S:"bonus_health_regen"]
-mov edx, 0xffffffff
+lea rsi, [rbx + 0x1b00]
 mov rdi, r12
+lea rdx, [S:"bonus_health_regen"]
 call F
-movaps xmm1, xmm0
-movss dword ptr [rbx + 0x1b00], xmm1
 mov rdi, rbx
 call F
@@ -115,5 +107,5 @@
 pop rbp
 jmp F
-nop
+nop dword ptr [rax]
 pop rbx
 pop r12
```

### изменена: 0x4eb6f50 (1071 байт) CDOTA_Modifier_Item_Shivas_Guard_Thinker::OnCreated | строки: "blast_speed"; "blast_radius"; "blast_damage"; "blast_debuff_duration"; "particles/items2_fx/shivas_guard_active.vpcf"
было: 0x4eb6d20 (1082 байт)
- числа в инструкциях: +1
- инструкций: 194 → 192
```diff
@@ -5,5 +5,5 @@
 push rbx
 mov rbx, rdi
-sub rsp, 0xc8
+sub rsp, 0xb8
 call F
 mov rdi, rbx
@@ -62,7 +62,7 @@
 jne L
 mov rdi, r12
-movss dword ptr [rbp - 0xd4], xmm2
+movss dword ptr [rbp - 0xc4], xmm2
 call F
-movss xmm2, dword ptr [rbp - 0xd4]
+movss xmm2, dword ptr [rbp - 0xc4]
 addss xmm0, xmm2
 ucomiss xmm0, dword ptr [rbx + 0x1b24]
@@ -128,5 +128,5 @@
 mov rax, qword ptr [rax]
 mov rax, qword ptr [rax + 0x18]
-add rsp, 0xc8
+add rsp, 0xb8
 pop rbx
 pop r12
@@ -138,5 +138,5 @@
 mov esi, 1
 pxor xmm1, xmm1
-movss dword ptr [rbp - 0xd4], xmm0
+movss dword ptr [rbp - 0xc4], xmm0
 lea rdi, [rbp - 0xb0]
 mov qword ptr [rbp - 0xc0], 1
@@ -150,23 +150,22 @@
 call F
 mov rsi, qword ptr [rbp - 0xb0]
-movss xmm0, dword ptr [rbp - 0xd4]
+movss xmm0, dword ptr [rbp - 0xc4]
 mov dword ptr [rsi], 0xc
 cmp dword ptr [rbp - 0xa4], 0x3fffffff
 ja L
 mov rax, qword ptr [D]
-movss dword ptr [rbp - 0xd4], xmm0
+movss dword ptr [rbp - 0xc4], xmm0
 mov rdi, qword ptr [rax]
 mov rax, qword ptr [rdi]
 call qword ptr [rax + 0x20]
-movss xmm0, dword ptr [rbp - 0xd4]
+movss xmm0, dword ptr [rbp - 0xc4]
 movss dword ptr [rbx + 0x1b24], xmm0
 jmp L
 nop dword ptr [rax]
 xor ecx, ecx
```
(ещё 32 строк диффа: so-query.py fdiff libserver.so 0x4eb6f50)

### изменена: 0x4eb7380 (1211 байт) CDOTA_Item_RiverPainter::OnSpellStart, CDOTA_Item_RiverPainter2::OnSpellStart, CDOTA_Item_RiverPainter3::OnSpellStart | строки: "paint_duration"; "RiverPaint.Cast"
было: 0x4eb7160 (1227 байт)
- числа в инструкциях: +1 +1 +1 +1
- инструкций: 259 → 262
```diff
@@ -12,9 +12,9 @@
 push rbx
 mov rbx, rdi
-sub rsp, 0x68
+sub rsp, 0x58
 movss xmm0, dword ptr [K:-1]
 call F
 lea r13, [D]
-movss dword ptr [rbp - 0x84], xmm0
+movss dword ptr [rbp - 0x74], xmm0
 mov r12, qword ptr [r13]
 test r12, r12
@@ -23,5 +23,5 @@
 mov rdi, r14
 call F
-movss xmm1, dword ptr [rbp - 0x84]
+movss xmm1, dword ptr [rbp - 0x74]
 movss xmm2, dword ptr [r12 + 0x1efc]
 subss xmm2, xmm0
@@ -34,7 +34,7 @@
 jne L
 mov rdi, r14
-movss dword ptr [rbp - 0x84], xmm1
-call F
-movss xmm1, dword ptr [rbp - 0x84]
+movss dword ptr [rbp - 0x74], xmm1
+call F
+movss xmm1, dword ptr [rbp - 0x74]
 addss xmm0, xmm1
 ucomiss xmm0, dword ptr [r12 + 0x1efc]
@@ -51,6 +51,6 @@
 mov r12d, 1
 jmp L
-nop
-add rsp, 0x68
+nop word ptr [rax + rax]
+add rsp, 0x58
 pop rbx
 pop r12
@@ -60,12 +60,11 @@
 pop rbp
 ret
-nop
+nop word ptr [rax + rax]
 xor edx, edx
-movss dword ptr [rbp - 0x84], xmm0
+mov esi, 1
+movss dword ptr [rbp - 0x74], xmm0
 pxor xmm1, xmm1
-lea rsi, [rbp - 0x74]
+lea rdi, [rbp - 0x60]
```
(ещё 106 строк диффа: so-query.py fdiff libserver.so 0x4eb7380)

### изменена: 0x4eb7840 (1028 байт) CDOTA_Item_SheepStick::OnSpellStart | строки: "upgrade_radius"; "CDOTA_Item_SheepStick::OnSpellStart"; "sheep_duration"; "duration"; "modifier_sheepstick_debuff"; "DOTA_Item.Sheepstick.Activate"
было: 0x4eb7630 (1026 байт)
- числа в инструкциях: +1 +1
- цели вызовов: +0x3bbffc0
- инструкций: 232 → 234
```diff
@@ -13,5 +13,5 @@
 push rbx
 mov ebx, 0xffffffff
-sub rsp, 0xd8
+sub rsp, 0xc8
 movss xmm0, dword ptr [K:-1]
 call F
@@ -37,5 +37,5 @@
 test eax, eax
 mov dword ptr [r15], ebx
-mov dword ptr [rbp - 0xe4], edi
+mov dword ptr [rbp - 0xd4], edi
 js L
 lea r14, [r15 + rax*4 + 4]
@@ -78,5 +78,5 @@
 cmp r14, rbx
 jne L
-cmp dword ptr [rbp - 0xe4], 0x3fffffff
+cmp dword ptr [rbp - 0xd4], 0x3fffffff
 ja L
 mov rax, qword ptr [D]
@@ -85,5 +85,5 @@
 mov rax, qword ptr [rdi]
 mov rax, qword ptr [rax + 0x20]
-add rsp, 0xd8
+add rsp, 0xc8
 pop rbx
 pop r12
@@ -93,5 +93,5 @@
 pop rbp
 jmp rax
-add rsp, 0xd8
+add rsp, 0xc8
 pop rbx
 pop r12
@@ -142,5 +142,5 @@
 xor edx, edx
 mov rdi, rax
-mov qword ptr [rbp - 0xf0], rax
+mov qword ptr [rbp - 0xe0], rax
 lea rsi, [S:"CDOTA_Item_SheepStick::OnSpellStart"]
 call F
@@ -153,5 +153,5 @@
 lea rsi, [S:"sheep_duration"]
 call F
-mov rdi, qword ptr [rbp - 0xf0]
+mov rdi, qword ptr [rbp - 0xe0]
 lea rsi, [S:"duration"]
 call F
@@ -161,5 +161,5 @@
 mov rdx, r13
```
(ещё 72 строк диффа: so-query.py fdiff libserver.so 0x4eb7840)

### изменена: 0x4eb7c50 (1700 байт) CDOTA_Modifier_Item_Shivas_Guard_Thinker::OnIntervalThink | строки: "modifier_item_shivas_guard_blast"; "particles/items2_fx/shivas_guard_impact.vpcf"
было: 0x4eb7a40 (1711 байт)
- числа в инструкциях: +1
- цели вызовов: +0x3bbffc0
- инструкций: 347 → 345
```diff
@@ -171,8 +171,8 @@
 cmp edx, -1
 je L
+cmp edx, -2
 mov rsi, qword ptr [D]
+je L
 test rsi, rsi
-je L
-cmp edx, -2
 je L
 movzx eax, word ptr [r8]
@@ -289,5 +289,5 @@
 pop rdx
 add r8, r13
-cmp dword ptr [rbx + 0x1b10], r15d
+cmp r15d, dword ptr [rbx + 0x1b10]
 mov eax, r15d
 je L
@@ -321,7 +321,6 @@
 pxor xmm1, xmm1
 mov word ptr [rbp - 0x94], si
-lea rdi, [rbp - 0xc8]
-lea rsi, [rbp - 0xf0]
-mov dword ptr [rbp - 0xf0], 0xc
+mov esi, 1
+lea rdi, [rbp - 0xc0]
 mov qword ptr [rbp - 0xd0], 1
 mov qword ptr [rbp - 0xc8], 0
@@ -332,10 +331,9 @@
 mov dword ptr [rbp - 0x98], 0xffffffff
 call F
+mov rsi, qword ptr [rbp - 0xc0]
 movss xmm0, dword ptr [rbp - 0xf8]
+mov dword ptr [rsi], 0xc
 cmp dword ptr [rbp - 0xb4], 0x3fffffff
 ja L
-mov rsi, qword ptr [rbp - 0xc0]
-test rsi, rsi
-je L
 mov rax, qword ptr [D]
 movss dword ptr [rbp - 0xf8], xmm0
```

### изменена: 0x4f4e1a0 (14971 байт) вызывается из: CDOTA_Item_Enchanters_Bauble::OnInventoryContentsChanged, CDOTA_Modifier_Item_Enchanters_Bauble::OnCreated
было: 0x4f4d4e0 (17659 байт)
- числа в инструкциях: −0 −0 −0 −0 −0 −0 −0 −0 (и ещё 8)
- прямых вызовов: 404 → 340
- цели вызовов: +0x4f475e0 +0x4f47590 +0x4f47540 +0x4f474f0 +0x4f474a0 +0x4f47450 +0x4f47400 +0x4f473b0 +0x4f47360 +0x4f47310 +0x4f472c0 +0x4f47270 +0x4f47220 +0x4f471d0 +0x4f47180 +0x4f47130 +0x4f470e0 +0x4f47090 +0x4f47040 +0x4f46ff0 −__cxa_guard_acquire() −0x3bbba40 −0x6a429b0 −__cxa_atexit() −__cxa_guard_release() −0x5c30200 −0x4f43eb0 −0x4f49660 −0x4de0e60 −0x4f49a50 −0x4f49680 −0x4f49a60 −0x4f496a0 −0x4f49a70 −0x4f496c0 −0x4f49a80 −0x4f496e0 −0x4f49a90 −0x4f49700 −0x4f49aa0
- инструкций: 3347 → 2771
```diff
@@ -1,578 +1,2 @@
-push rbp
-mov rbp, rsp
-push r12
-push rbx
-movzx eax, byte ptr [D]
-test al, al
-je L
-mov rax, qword ptr [D]
-test rax, rax
-je L
-pop rbx
-pop r12
-pop rbp
-ret
-nop dword ptr [rax + rax]
-lea rbx, [D]
-mov rdi, rbx
-call F
-test eax, eax
-je L
-lea r12, [D]
-mov rdi, r12
-call F
-lea rdi, [T]
-lea rdx, [D]
-mov rsi, r12
-call F
-mov rdi, rbx
-call F
-mov rax, qword ptr [D]
-test rax, rax
-jne L
-nop dword ptr [rax]
-movzx eax, byte ptr [D]
-test al, al
-je L
-lea rax, [D]
-mov qword ptr [D], rax
-mov rax, qword ptr [D]
-lea rbx, [D]
-mov qword ptr [D], rbx
-mov qword ptr [D], rbx
-mov qword ptr [D], rax
-call F
-movq xmm0, qword ptr [D]
-mov qword ptr [D], 0
-mov qword ptr [D], rax
-lea rax, [T]
-mov qword ptr [D], 0
-movq xmm1, rax
```
(ещё 528 строк диффа: so-query.py fdiff libserver.so 0x4f4e1a0)

### изменена: 0x4fb1ae0 (1475 байт) вызывается из: CDOTA_Modifier_Item_Mechanical_Arm::vfunc#97 | строки: "modifier_mechanical_arm_counter"; "duration"; "modifier_item_occult_bracelet_mana_stack"; "particles/items_fx/occult_bracelet_hit.vpcf"
было: 0x4fb18a0 (1555 байт)
- числа в инструкциях: −-1 −-2 −9 −0x3f −0x1ff −0x70
- поля объектов: −0xd0 −0xd0 −0x10
- прямых вызовов: 51 → 52
- инструкций: 403 → 386
```diff
@@ -19,24 +19,8 @@
 cmp byte ptr [r14 + 0x5d1], 3
 jne L
-mov ecx, dword ptr [r12 + 0xd0]
-cmp ecx, -1
-je L
-mov rsi, qword ptr [D]
-test rsi, rsi
-je L
-cmp ecx, -2
-je L
-movzx eax, word ptr [r12 + 0xd0]
-mov rdx, rax
-shr rdx, 9
-and edx, 0x3f
-mov rdx, qword ptr [rsi + rdx*8]
-test rdx, rdx
-je L
-and eax, 0x1ff
-imul rax, rax, 0x70
-add rax, rdx
-cmp ecx, dword ptr [rax + 0x10]
-jne L
+lea rdi, [r12 + 0xd0]
+call F
+test rax, rax
+je L
 mov r15, qword ptr [rax]
 test r15, r15
@@ -67,5 +51,5 @@
 pop rbp
 ret
-nop dword ptr [rax]
+nop
 mov rdi, r13
 call F
@@ -77,5 +61,4 @@
 xor r14d, r14d
 jmp L
-nop dword ptr [rax + rax]
 mov rdi, r13
 call F
```

### изменена: 0x4fb56f0 (1018 байт) CDOTA_Item_Minotaur_Horn::OnSpellStart | строки: "duration"; "modifier_magic_immune"; "DOTA_Item.MinotaurHorn.Cast"; "modifier_minotaur_horn_immune"; "modifier_slark_pounce_leash"; "modifier_invoker_deafening_blast_disarm"; "modifier_silence"
было: 0x4fb5770 (2236 байт)
- строки: +"duration" +"duration" +"modifier_silence" −"Item.LotusOrb.Activate" −"particles/items3_fx/lotus_orb_reflect.vpcf" −"attach_hitloc" −"block_cooldown" −"modifier_lotus_orb_delay" −"modifier_mirror_shield_delay"
- константы из данных (числа логики): +-1 +1 −1.5 −3.402823e+38 −0x7f7fffff7f7fffff
- числа в инструкциях: +-1 +-1 +-2 +9 +0x3f +0x1ff +0x70 +1 −0 −0 −0 −0xa −5 −0x3f80000000000001 (и ещё 4)
- виртуальные вызовы: +0xf78 (слот 495) −0x78 (слот 15) −0x18 (слот 3)
- поля объектов: +0xcc +0x15da +0x13b0 +0xd3c +0x1248 +0x174c −0x1bf8 −0x1bf8 −0x780 −0x1af8 −0x1afc −0xc −0x1b04 −0x1b08 −0x14 −0x1b0c −0x18 −0x1b10 (и ещё 151)
- прямых вызовов: 52 → 37
- цели вызовов: +0x505aeb0 +0x44bed50 +0x44be5b0 +0x5040d30 −0x3ba8c40 −0x5044a30 −CDOTA_Ability_DarkCarnival_Balloon::vfunc#240 −0x5405e90 −0x3c787c0 −0x552c170 −0x3bc4370 −0x5550a50 −0x552ce40
- инструкций: 443 → 257
```diff
@@ -89,157 +89,37 @@
 mov rdi, rsi
 push r12
-mov r12, rdx
+mov r12, rsi
 push rbx
-mov rbx, rsi
-sub rsp, 0x78
-call F
-test rax, rax
-je L
-cmp byte ptr [rax + 0x175a], 0
-jne L
-mov rdi, r12
-call F
-test rax, rax
-mov r14, rax
-je L
-mov r14, qword ptr [rax]
-mov rdi, r14
-call F
-test rax, rax
-je L
-mov rdi, r14
-call F
-mov rdi, rbx
-movzx r15d, byte ptr [rax + 0x624]
-call F
-cmp byte ptr [rax + 0x624], r15b
-je L
-mov rdi, rbx
-mov byte ptr [rbx + 0x1bf8], 0
-call F
-mov rdi, rax
-mov rax, qword ptr [rax]
-call qword ptr [rax + 0x940]
-test al, al
-je L
-mov byte ptr [rbx + 0x1bf8], 1
-mov rax, qword ptr [r14]
-lea rdx, [T]
-mov rax, qword ptr [rax + 0x780]
-cmp rax, rdx
-jne L
-lea r14, [rbp - 0x50]
-mov rsi, r12
-mov rdi, rbx
-call F
-mov rdi, rbx
-call F
-lea rdx, [S:"Item.LotusOrb.Activate"]
```
(ещё 453 строк диффа: so-query.py fdiff libserver.so 0x4fb56f0)

### изменена: 0x4fb66b0 (198 байт) CDOTA_Modifier_Orb_Of_Frost_Debuff::vfunc#88 | строки: "slow_melee"; "slow_ranged"; "heal_reduction"
было: 0x4fb6660 (225 байт)
- числа в инструкциях: −0xffffffff
- поля объектов: −0x1b00
- прямых вызовов: 9 → 8
- цели вызовов: +0x3bbd2f0
- инструкций: 62 → 53
```diff
@@ -45,18 +45,9 @@
 mov rax, qword ptr [rbx]
 call qword ptr [rax + 0x1f0]
-test r12, r12
-pxor xmm1, xmm1
-je L
-xor r9d, r9d
-xor r8d, r8d
-xor ecx, ecx
-lea rsi, [S:"heal_reduction"]
-mov edx, 0xffffffff
+lea rsi, [rbx + 0x1b00]
 mov rdi, r12
-call F
-movaps xmm1, xmm0
-movss dword ptr [rbx + 0x1b00], xmm1
 pop rbx
 pop r12
 pop rbp
-ret
+lea rdx, [S:"heal_reduction"]
+jmp F
```

### изменена: 0x4fb7970 (191 байт) CDOTA_Modifier_Item_MaskOfDispair::OnCreated | строки: "bonus_strength"; "bonus_armor"; "spell_lifesteal"
было: 0x4fb7db0 (211 байт)
- числа в инструкциях: −0xffffffff
- поля объектов: −0x1b00
- прямых вызовов: 9 → 8
- цели вызовов: +0x44e6000
- инструкций: 60 → 52
```diff
@@ -44,17 +44,9 @@
 mov rax, qword ptr [rbx]
 call qword ptr [rax + 0x1f0]
-xor eax, eax
-test r12, r12
-je L
-xor r9d, r9d
-xor r8d, r8d
-xor ecx, ecx
-lea rsi, [S:"spell_lifesteal"]
-mov edx, 0xffffffff
+lea rsi, [rbx + 0x1b00]
 mov rdi, r12
-call F
-mov dword ptr [rbx + 0x1b00], eax
 pop rbx
 pop r12
 pop rbp
-ret
+lea rdx, [S:"spell_lifesteal"]
+jmp F
```

### изменена: 0x4fbe880 (476 байт) | строки: "CDOTA_Item_Recipe_Orb_Of_Corrosion"
было: 0x4fbc460 (508 байт)
- прямых вызовов: 13 → 12
- инструкций: 124 → 106
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
 pop rbx
 pop r12
@@ -34,38 +23,31 @@
 pop r14
 pop rbp
-ret
+jmp F
 nop dword ptr [rax]
 mov rdi, rbx
 mov byte ptr [D], 1
 call F
-movsxd rbx, dword ptr [D]
-cmp ebx, dword ptr [D]
-mov r13, rax
-mov edx, ebx
+movsxd r13, dword ptr [D]
+cmp r13d, dword ptr [D]
```
(ещё 44 строк диффа: so-query.py fdiff libserver.so 0x4fbe880)

### изменена: 0x5040610 (1289 байт) | строки: "aura_is_heal"; "aura_apply_modifier"; "aura"; "aura_radius"; "aura_search_flags"; "aura_search_type"; "aura_search_team"
было: 0x50407e0 (1273 байт)
- числа в инструкциях: +1 +0xffffff
- виртуальные вызовы: +0x20 (слот 4)
- прямых вызовов: 50 → 51
- инструкций: 296 → 301
```diff
@@ -198,11 +198,16 @@
 test eax, eax
 je L
+mov dword ptr [D], 0xffffff
+call F
+mov edx, 1
 lea rsi, [S:"aura_apply_modifier"]
-lea rdi, [D]
-call F
-mov rdi, r13
-call F
-jmp L
-nop word ptr [rax + rax]
+mov rdi, rax
+mov rax, qword ptr [rax]
+call qword ptr [rax + 0x20]
+mov rdi, r13
+mov dword ptr [D], eax
+call F
+jmp L
+nop
 lea r13, [D]
 mov rdi, r13
```

### изменена: 0x507384a (10 байт) вызывается из: CDOTA_Ability_DarkCarnival_Balloon::vfunc#349
было: 0x507368a (20 байт)
- инструкций: 4 → 2
```diff
@@ -1,4 +1,2 @@
 mov rax, qword ptr [0]
 ud2
-movzx eax, word ptr [0x140a]
-ud2
```

### изменена: 0x5073860 (1112 байт) CDOTA_Ability_DarkCarnival_Balloon::vfunc#349, CDOTA_Ability_DarkCarnival_Firework::vfunc#349, CDOTA_Ability_DarkCarnival_Pie::vfunc#349
было: 0x50736a0 (954 байт)
- числа в инструкциях: +-1 +-2 +9 +0x3f +0x1ff +0x70
- поля объектов: +0x6bc +0x6bc +0x10
- прямых вызовов: 9 → 8
- инструкций: 187 → 216
```diff
@@ -1,10 +1,9 @@
 push rbp
 mov rbp, rsp
-push r13
 push r12
 mov r12d, esi
 push rbx
 mov rbx, rdi
-sub rsp, 0x118
+sub rsp, 0x110
 mov rax, qword ptr [rdi]
 call qword ptr [rax + 0xae0]
@@ -13,5 +12,4 @@
 cvtsi2ss xmm2, eax
 cmp ecx, -1
-movss dword ptr [rbp - 0x124], xmm2
 je L
 mov rsi, qword ptr [D]
@@ -35,17 +33,19 @@
 test rdi, rdi
 je L
-lea r13, [rbx + 0x6bc]
 mov rsi, rbx
-call F
+movss dword ptr [rbp - 0x114], xmm2
+call F
+movss xmm2, dword ptr [rbp - 0x114]
 test al, al
 je L
 mov rax, qword ptr [rbx]
+movss dword ptr [rbp - 0x118], xmm2
 mov esi, r12d
 mov rdi, rbx
 call qword ptr [rax + 0xac8]
 pxor xmm4, xmm4
-mov rdi, r13
+lea rdi, [rbx + 0x6bc]
 cvtsi2ss xmm4, eax
-movss dword ptr [rbp - 0x128], xmm4
+movss dword ptr [rbp - 0x114], xmm4
 call F
 test rax, rax
@@ -53,4 +53,5 @@
 mov rdi, qword ptr [rax]
 lea rcx, [T]
+movss xmm2, dword ptr [rbp - 0x118]
 mov rax, qword ptr [rdi]
 mov rdx, qword ptr [rax + 0xcb0]
@@ -60,57 +61,57 @@
 xor esi, esi
 call qword ptr [rax + 0xcb8]
```
(ещё 207 строк диффа: so-query.py fdiff libserver.so 0x5073860)

### изменена: 0x5077fe0 (769 байт) вызывается из: CDOTA_Ability_Hoodwink_AcornShot::vfunc#371, CDOTABehaviorAttackPhase::vfunc#67
было: 0x5077be0 (745 байт)
- числа в инструкциях: +0
- поля объектов: +0x4801c
- инструкций: 160 → 169
```diff
@@ -7,15 +7,15 @@
 push r13
 push r12
-mov r12, rdi
 push rbx
+mov rbx, rdi
 sub rsp, 0x100
 movzx ecx, word ptr [rsi + 0x38]
-mov r13, rcx
-mov ebx, ecx
+mov r12, rcx
+mov r13d, ecx
 mov esi, ecx
-and r13d, 0x3ff
-and bx, 0x3ff
+and r12d, 0x3ff
+and r13w, 0x3ff
 and esi, 0x3ff
-lea rdx, [r13 + r13*2]
+lea rdx, [r12 + r12*2]
 lea rdx, [rdi + rdx*2]
 cmp byte ptr [rdx + 0x4801c], 0
@@ -34,5 +34,5 @@
 pop rbp
 jmp F
-nop dword ptr [rax + rax]
+nop dword ptr [rax]
 mov edi, 0xffffffff
 pxor xmm0, xmm0
@@ -128,8 +128,17 @@
 mov word ptr [rbp - 0xdc], cx
 call F
-lea rax, [r13 + r13*2]
-lea r14, [r12 + rax*2]
+lea rax, [r12 + r12*2]
+lea r14, [rbx + rax*2]
+cmp byte ptr [r14 + 0x4801c], 0
+jne L
+add rsp, 0x100
+pop rbx
+pop r12
+pop r13
+pop r14
+pop rbp
+ret
 mov byte ptr [r14 + 0x4801c], 0
-movzx eax, word ptr [r12 + 0x49818]
+movzx eax, word ptr [rbx + 0x49818]
 mov word ptr [r14 + 0x4801a], ax
 movzx eax, byte ptr [r14 + 0x48019]
@@ -140,14 +149,14 @@
```
(ещё 25 строк диффа: so-query.py fdiff libserver.so 0x5077fe0)

### изменена: 0x507cfd0 (372 байт)
было: 0x507cc90 (308 байт)
- прямых вызовов: 6 → 9
- цели вызовов: +_ZN9KeyValues18GetFirstTrueSubKeyEv() +0x507ce80 "AbilityTalentStart"; "Ability%d" +_ZN9KeyValues17GetNextTrueSubKeyEv()
- инструкций: 80 → 102
```diff
@@ -1,2 +1,24 @@
+push rbp
+mov rbp, rsp
+push r12
+mov r12, rsi
+push rbx
+call F
+test rax, rax
+je L
+mov rbx, rax
+nop word ptr [rax + rax]
+mov rdi, rbx
+mov rsi, r12
+call F
+mov rdi, rbx
+call F
+test rax, rax
+mov rbx, rax
+jne L
+pop rbx
+pop r12
+pop rbp
+ret
 push rbp
 mov rbp, rsp
```

### изменена: 0x5087500 (226 байт) вызывается из: CDOTABaseGameMode::vfunc#317
было: 0x5087180 (421 байт)
- числа в инструкциях: −1 −0 −0 −0
- виртуальные вызовы: +0xf0 (слот 30)
- поля объектов: −0xf0 −0x318 −0x48 −0x18 −0x315 −0x30 −0x538 −0x538 −0x530
- прямых вызовов: 5 → 3
- цели вызовов: −CDOTA_NPCSpawnerGoodTop::vfunc#30 −0x3c41be0 " ignored"; "%u,"
- инструкций: 98 → 56
```diff
@@ -14,48 +14,29 @@
 ret
 nop word ptr [rax + rax]
-xor edx, edx
+xor eax, eax
 mov esi, 1
 movss dword ptr [rbp - 0x54], xmm0
 pxor xmm1, xmm1
 lea rdi, [rbp - 0x40]
-mov word ptr [rbp - 0x14], dx
+movaps xmmword ptr [rbp - 0x30], xmm1
+mov word ptr [rbp - 0x14], ax
+lea r12, [rbp - 0x50]
 mov qword ptr [rbp - 0x50], 1
-lea r12, [rbp - 0x50]
 mov qword ptr [rbp - 0x48], 0
 mov qword ptr [rbp - 0x40], 0
 mov qword ptr [rbp - 0x38], 0
-movaps xmmword ptr [rbp - 0x30], xmm1
 mov qword ptr [rbp - 0x20], 0xffffffffffffffff
 mov dword ptr [rbp - 0x18], 0xffffffff
 call F
 mov rax, qword ptr [rbp - 0x40]
-lea rdx, [T]
+mov rsi, r12
+mov rdi, rbx
 add dword ptr [rbp - 0x48], 1
-movss xmm0, dword ptr [rbp - 0x54]
 mov dword ptr [rax], 0x7f0
 mov rax, qword ptr [rbx]
-mov rax, qword ptr [rax + 0xf0]
-cmp rax, rdx
-jne L
-mov eax, dword ptr [rbp - 0x50]
-lea rdi, [rbx + 0x38]
-test eax, eax
-jne L
-cmp byte ptr [rbx + 0x318], 0
-jne L
-mov rax, qword ptr [rbx + 0x48]
-test rax, rax
-je L
-cmp byte ptr [rax + 0x18], 0
-je L
-mov byte ptr [rbx + 0x315], 1
-nop
-lea rax, [D]
-mov rax, qword ptr [rax]
-movss xmm1, dword ptr [rax + 0x30]
-comiss xmm1, dword ptr [rbx + 0x538]
-ja L
```
(ещё 32 строк диффа: so-query.py fdiff libserver.so 0x5087500)

### изменена: 0x5097e70 (68231 байт) CDOTABaseGameMode::vfunc#317, CDOTAMutationGameMode::vfunc#317, CDOTANewPlayerPoolGameMode::vfunc#317 | строки: "ExecuteOrderData"; "issuer_player_id_const"; "sequence_number_const"; "units"; "order_type"; "entindex_target"; "entindex_ability"; "shop_item_name"
было: 0x5097bb0 (68231 байт)
- строки: +"position_y" −"entindex_target"
- цели вызовов: −0x507cfd0
- инструкций: 17572 → 17572
```diff
@@ -64,7 +64,8 @@
 lea rsi, [S:"order_type"]
 mov rdi, r12
+lea r14, [S:"entindex_target"]
 call F
 mov edx, dword ptr [r15 + 0x30]
-lea rsi, [S:"entindex_target"]
+mov rsi, r14
 mov rdi, r12
 call F
@@ -82,5 +83,4 @@
 mov rdi, r12
 lea rsi, [S:"queue"]
-lea r14, [S:"position_y"]
 and edx, 1
 call F
@@ -91,5 +91,5 @@
 movss xmm0, dword ptr [r15 + 0x1c]
 mov rdi, r12
-mov rsi, r14
+lea rsi, [S:"position_y"]
 call F
 movss xmm0, dword ptr [r15 + 0x20]
@@ -122,5 +122,5 @@
 call F
 mov edx, dword ptr [r15 + 0x30]
-lea rsi, [S:"entindex_target"]
+mov rsi, r14
 mov rdi, r12
 mov dword ptr [r15 + 0x2c], eax
@@ -149,5 +149,5 @@
 mov dword ptr [r15 + 0x38], eax
 call F
-mov rsi, r14
+lea rsi, [S:"position_y"]
 mov rdi, r12
 movss dword ptr [r15 + 0x18], xmm0
```

### изменена: 0x50ac860 (8911 байт) | строки: "BaseClass"; "AbilityTextureName"; "AbilitySharedCooldown"; "AbilityCastAnimation"; "AbilityCastGestureSlot"; "NONE"; "LinkedAbility"; "LinkedScepterAbility"
было: 0x50ac5a0 (8959 байт)
- строки: +"item_"
- прямых вызовов: 267 → 266
- инструкций: 2045 → 2037
```diff
@@ -29,6 +29,6 @@
 mov r13, rax
 call F
+mov rdi, r14
 mov rsi, r12
-mov rdi, r14
 call F
 mov edx, 1
@@ -39,19 +39,19 @@
 mov rdi, rbx
 call F
-mov r13, qword ptr [rbx]
-lea rax, [D]
+mov r14, qword ptr [rbx]
+lea r13, [D]
 mov rdi, r15
 lea rsi, [S:"BaseClass"]
-test r13, r13
-cmove r13, rax
-call F
-test rax, rax
-je L
-mov rsi, r13
-xor ecx, ecx
-xor edx, edx
-mov rdi, rax
-call F
-mov r13, rax
+test r14, r14
+cmove r14, r13
+call F
+test rax, rax
+je L
+mov rsi, r14
+xor ecx, ecx
+xor edx, edx
+mov rdi, rax
+call F
+mov r14, rax
 mov rdi, qword ptr [rbp - 0x1b0]
 lea rsi, [S:"AbilityTextureName"]
@@ -59,43 +59,43 @@
 test rax, rax
 je L
+mov rsi, r14
+xor ecx, ecx
+xor edx, edx
+mov rdi, rax
+call F
+mov r14, rax
+lea rdi, [rbx + 0x10]
```
(ещё 675 строк диффа: so-query.py fdiff libserver.so 0x50ac860)

### изменена: 0x54178c0 (3170 байт) вызывается из: CDOTA_Modifier_MudGolem_RockDestroy::vfunc#97 | строки: "shard_amount"; "shard_health"; "shard_damage"; "shard_duration"; "npc_dota_neutral_mud_golem"; "npc_dota_neutral_mud_golem_split"; "modifier_kill"; "duration"
было: 0x5417600 (3172 байт)
- числа в инструкциях: +1 +1
- цели вызовов: −0x5411c20
- инструкций: 696 → 696
```diff
@@ -121,5 +121,5 @@
 mov rax, qword ptr [r15]
 call qword ptr [rax + 0x1f0]
-lea rsi, [rbp - 0x128]
+lea rsi, [rbp - 0x124]
 mov rdi, rbx
 lea rdx, [S:"shard_amount"]
@@ -165,5 +165,5 @@
 test al, al
 je L
-mov r8d, dword ptr [rbp - 0x128]
+mov r8d, dword ptr [rbp - 0x124]
 xor eax, eax
 test r8d, r8d
@@ -651,14 +651,11 @@
 mov r13, qword ptr [rbp - 0x168]
 jmp L
-lea rax, [rbp - 0xa8]
-xor ecx, ecx
+xor ecx, ecx
+mov esi, 1
 pxor xmm0, xmm0
-mov dword ptr [rbp - 0x124], 0x1768
-lea rsi, [rbp - 0x124]
-mov rdi, rax
+mov qword ptr [rbp - 0xb0], 1
+lea rdi, [rbp - 0xa0]
 mov word ptr [rbp - 0x74], cx
 movaps xmmword ptr [rbp - 0x90], xmm0
-mov qword ptr [rbp - 0x138], rax
-mov qword ptr [rbp - 0xb0], 1
 mov qword ptr [rbp - 0xa8], 0
 mov qword ptr [rbp - 0xa0], 0
@@ -667,9 +664,12 @@
 mov dword ptr [rbp - 0x78], 0xffffffff
 call F
-mov rdx, qword ptr [rbx]
+mov rax, qword ptr [rbp - 0xa0]
 mov rsi, r12
 mov rdi, rbx
-call qword ptr [rdx + 0xf0]
-mov rdi, qword ptr [rbp - 0x138]
+add dword ptr [rbp - 0xa8], 1
+mov dword ptr [rax], 0x1768
+mov rax, qword ptr [rbx]
+call qword ptr [rax + 0xf0]
+lea rdi, [rbp - 0xa8]
 call F
 mov rsi, qword ptr [rbp - 0x120]
```

### изменена: 0x5c02f70 (842 байт) | строки: "m_eCategory"; "Double-save to Member '%s'"; "m_unActionID"; "m_strLocName"
было: 0x5c02c70 (857 байт)
- числа в инструкциях: −0 −0 −0
- поля объектов: −0x140 −0x148
- цели вызовов: +0x5bf06e0
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
```
(ещё 122 строк диффа: so-query.py fdiff libserver.so 0x5c02f70)

### изменена: 0x5c194b0 (75 байт)
было: 0x5c191b0 (87 байт)
- поля объектов: −0x10
- прямых вызовов: 4 → 3
- цели вызовов: −0x5cb83f0
- инструкций: 30 → 27
```diff
@@ -22,7 +22,4 @@
 ret
 nop
-mov rax, qword ptr [rbx]
-mov rdi, qword ptr [rax + 0x10]
-call F
 mov rbx, qword ptr [rbp - 8]
 mov eax, 1
```

### изменена: 0x5c1b200 (339 байт)
было: 0x5c1af10 (355 байт)
- поля объектов: −0x10
- прямых вызовов: 7 → 6
- инструкций: 101 → 98
```diff
@@ -76,10 +76,7 @@
 je L
 ja L
-mov rax, qword ptr [rbx]
-mov rdi, qword ptr [rax + 0x10]
-call F
 mov eax, 1
 jmp L
-nop dword ptr [rax]
+nop word ptr [rax + rax]
 mov rdi, rbx
 mov rbx, qword ptr [rbp - 8]
```

### изменена: 0x5c20940 (3633 байт) | строки: "npc_dota_hero_razor"; "modifier_disable_taunt_animation_cancel"
было: 0x5c20660 (3649 байт)
- числа в инструкциях: −0x5df
- виртуальные вызовы: +0xdc0 (слот 440)
- поля объектов: −0xdc0
- прямых вызовов: 81 → 80
- цели вызовов: −0x44209b0
- инструкций: 782 → 779
```diff
@@ -448,14 +448,16 @@
 call qword ptr [rax + 0xe30]
 lea rsi, [S:"npc_dota_hero_razor"]
+cmp rax, rsi
+je L
+test rax, rax
+je L
 mov rdi, rax
 call F
-mov edx, eax
-mov rax, qword ptr [r12]
-test dl, dl
-mov rax, qword ptr [rax + 0xdc0]
-je L
+test eax, eax
+jne L
+mov rax, qword ptr [r12]
 mov esi, 0x5df
 mov rdi, r12
-call rax
+call qword ptr [rax + 0xdc0]
 mov esi, 0x5df
 mov rdi, r12
@@ -528,5 +530,5 @@
 pop rbp
 jmp F
-nop dword ptr [rax + rax]
+nop dword ptr [rax]
 mov rdi, r13
 call F
@@ -538,5 +540,4 @@
 movss dword ptr [rbx + 0x10], xmm0
 jmp L
-nop dword ptr [rax + rax]
 mov rbx, qword ptr [rbp - 0x140]
 mov rdi, rbx
@@ -566,10 +567,5 @@
 mov esi, 0x5dc
 call F
-mov rax, qword ptr [r12]
-mov esi, 0x5df
-mov rdi, r12
-call qword ptr [rax + 0xdc0]
-jmp L
-nop word ptr [rax + rax]
+jmp L
 mov rdi, qword ptr [rbp - 0x148]
 mov rax, qword ptr [rdi]
@@ -739,7 +735,8 @@
 mov qword ptr [rsi + 8], rdx
 jmp L
```
(ещё 7 строк диффа: so-query.py fdiff libserver.so 0x5c20940)

### изменена: 0x5c7d280 (11030 байт) CDOTA_Item_BotChallenge_MeteorStaff::Spawn, CDOTA_Item_Mask_Spin_Crit::Spawn, CDOTA_Item_Mask_Crit_Lifesteal::Spawn | строки: "<NoAbilityName>"; "ItemBaseLevel"; "ItemCombinable"; "ItemPermanent"; "ItemStackable"; "ItemStackableMax"; "ItemRecipe"; "ItemRecipeConsumesCharges"
было: 0x5c7cfc0 (11035 байт)
- цели вызовов: −0x44209b0
- инструкций: 1918 → 1917
```diff
@@ -374,10 +374,4 @@
 test rax, rax
 jne L
-lea rsi, [S:"ITEM_FULLY_SHAREABLE_STACKING"]
-mov rdi, r15
-call F
-test al, al
-jne L
-nop dword ptr [rax]
 mov dword ptr [rbx + 0x8d4], 0
 lea rsi, [S:"ItemDeclarations"]
@@ -427,5 +421,5 @@
 pop rbp
 ret
-nop word ptr [rax + rax]
+nop dword ptr [rax]
 xor edi, edi
 mov esi, 1
@@ -1270,7 +1264,14 @@
 call F
 test eax, eax
-jne L
-mov r9d, dword ptr [rbx + 0x870]
-test r9d, r9d
+je L
+lea rsi, [S:"ITEM_FULLY_SHAREABLE_STACKING"]
+cmp r15, rsi
+je L
+mov rdi, r15
+call F
+test eax, eax
+jne L
+mov r8d, dword ptr [rbx + 0x870]
+test r8d, r8d
 je L
 mov edx, 0xffffffff
@@ -1279,4 +1280,5 @@
 call F
 mov dword ptr [rbx + 0x870], 0
+mov byte ptr [rbx + 0x8d0], 1
 jmp L
 nop
@@ -1309,29 +1311,29 @@
 jmp L
 nop dword ptr [rax + rax]
+xor ecx, ecx
+mov esi, 1
+pxor xmm0, xmm0
+mov qword ptr [rbp - 0x180], 1
 lea rdi, [rbp - 0x170]
-xor esi, esi
```
(ещё 291 строк диффа: so-query.py fdiff libserver.so 0x5c7d280)

### изменена: 0x3e81e10 (1101 байт) | строки: "CNetworkUtlVectorBase"; "ModelConfigHandle_t"; "CBaseModelEntity"; "CHandle"; "CUtlSymbolLarge"; "CUtlLeanVector"
- код тот же, но вызывает другую функцию: было 0x3eaed80, стало 0x3eaedc0

### изменена: 0x4fb9640 (7237 байт) | строки: "scripts/height_levels.txt"; "modifier_item_martyrs_plate"; "modifier_item_martyrs_plate_aura"; "modifier_item_martyrs_plate_effect"; "modifier_item_mask_of_dispair"; "modifier_item_mask_of_dispair_berserk"; "modifier_item_mechanical_arm"; "modifier_mechanical_arm_counter"
- код тот же, но вызывает другую функцию: было 0x4fbc660, стало 0x4fbe880

### добавлена: 0x3eaedc0 (904 байт) | строки: "8q|"

### добавлена: 0x43ffd30 (22 байт) CDOTA_Modifier_PathMoveSpeed::vfunc#24

### добавлена: 0x4fb5af0 (1932 байт) вызывается из: CDOTA_Modifier_Item_Mirror_Shield::vfunc#97 | строки: "Item.LotusOrb.Activate"; "particles/items3_fx/lotus_orb_reflect.vpcf"; "attach_hitloc"; "block_cooldown"; "modifier_lotus_orb_delay"; "modifier_mirror_shield_delay"

### добавлена: 0x5043f50 (207 байт) вызывается из: CDOTA_Ability_Nevermore_Requiem::OnSpellStart, CDOTA_Ability_Nevermore_Requiem::OnStolen, CDOTA_Modifier_Nevermore_Requiem_Thinker::OnDestroy

### добавлена: 0x5044020 (9 байт)

### добавлена: 0x50446d0 (795 байт)

### добавлена: 0x5077b7c (539 байт) | строки: "AddNewAttackRecord"; "m_unNextFreeIndex < DOTA_PROJECTILES_ATTACK_RECORD_MAX"; "<null>"; "valid"; "invalid"

### добавлена: 0x69fb200 (1237 байт)

### удалена: 0x3eae9e0 (904 байт) | строки: "tm|"

### удалена: 0x4fb1ec0 (616 байт) вызывается из: CDOTA_Modifier_Item_Mind_Breaker::vfunc#97 | строки: "modifier_silence"; "duration"

### удалена: 0x502f860 (149 байт)

### удалена: 0x503d710 (846 байт)

### удалена: 0x5044110 (79 байт) вызывается из: CDOTA_Ability_Nevermore_Requiem::OnSpellStart, CDOTA_Ability_Nevermore_Requiem::OnStolen, CDOTA_Modifier_Nevermore_Requiem_Thinker::OnDestroy

### удалена: 0x50778fc (76 байт) | строки: "AddNewAttackRecord"; "m_unNextFreeIndex < DOTA_PROJECTILES_ATTACK_RECORD_MAX"

### удалена: 0x5077950 (75 байт) вызывается из: CDOTA_Ability_Windrunner_Shackleshot::vfunc#371, CDOTA_Ability_StormSpirit_Overload::vfunc#371, CDOTA_Ability_WitchDoctor_DeathWard::vfunc#371

### удалена: 0x507cb90 (246 байт) | строки: "CNetworkTransmitComponent::StateChanged(%s) @%s:%d"

### удалена: 0x69fa7b0 (3221 байт)

### копии существующего кода (13): шаблонные / склеенные компоновщиком функции, такой же код есть и в другой сборке — не новый код
- ещё одна копия существующего кода: 0x43ff950 (3 байт) CDOTA_Modifier_PathInLane::vfunc#24
- ещё одна копия существующего кода: 0x4858ee0 (980 байт)
- ещё одна копия существующего кода: 0x4f4d710 (2688 байт)
- ещё одна копия существующего кода: 0x5028970 (3 байт) CDOTA_Modifier_Creep_Slow::vfunc#24
- ещё одна копия существующего кода: 0x5028a10 (3 байт) CDOTA_Modifier_Lane_Creep_OutOfLane_Slow::vfunc#24
- ещё одна копия существующего кода: 0x5028a80 (3 байт) CDOTA_Modifier_Creep_Haste::vfunc#24
- ещё одна копия существующего кода: 0x53a6760 (3 байт) CDOTA_Modifier_Neutral_Sleep_AI::vfunc#24
- ещё одна копия существующего кода: 0x53ab6c0 (3 байт) CDOTA_Modifier_Creep_Siege::vfunc#24
- ещё одна копия существующего кода: 0x53ab790 (3 байт) CDOTA_Modifier_Creep_Piercing::vfunc#24
- ещё одна копия существующего кода: 0x53ab840 (3 байт) CDOTA_Modifier_Creep_Irresolute::vfunc#24
- ещё одна копия существующего кода: 0x69faa30 (1984 байт)
- одной копией существующего кода меньше: 0x485e230 (2880 байт)
- одной копией существующего кода меньше: 0x4eb6bb0 (82 байт) вызывается из: CDOTA_Modifier_Item_Shivas_Guard_Thinker::OnCreated, CDOTA_Item_RiverPainter::OnSpellStart, CDOTA_Item_SheepStick::OnSpellStart


## Строки библиотек

<details><summary>dota-bin/libserver.so: строки</summary>

**Добавлено — Сообщения и описания (2)**

```
%d: %s src:%s target:%s
Ran out of free attack record indices.
```

</details>
