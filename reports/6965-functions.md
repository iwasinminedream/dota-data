# Dota 6965: изменения кода по функциям

Снимки `6964-11146732` → `6965-11152239`; funcdiff.py. В диффе: [S:…] — строка, [K:…] — константа из данных, F — вызов другой функции, L — переход внутри функции, [D]/[T] — прочие адреса. Регистры и смещения стека меняются и от перекомпиляции.

## libserver.so: функций 220000 → 220000; без изменений 219999, изменено 1, добавлено 0, удалено 0

### изменена: 0x5f3dd30 (2107 байт) CDOTA_Bot_AbilityUsage_SandKing_BurrowStrike::vfunc#5 | строки: "burrow_width"
было: 0x5f45910 (2099 байт)
- инструкций: 469 → 471
```diff
@@ -5,8 +5,8 @@
 push r15
 push r14
-lea r14, [D]
 push r13
-mov rsi, r14
+lea r13, [D]
 push r12
+mov rsi, r13
 push rbx
 mov rbx, rdi
@@ -25,5 +25,5 @@
 mov rdi, qword ptr [rbx + 8]
 mov qword ptr [rbp - 0x58], 0
-mov r13d, eax
+movd r15d, xmm0
 mov dword ptr [rbp - 0x60], 0
 call F
@@ -35,5 +35,5 @@
 lea rsi, [rbp - 0x58]
 addss xmm0, xmm3
-movd r15d, xmm3
+movd r14d, xmm3
 call F
 test al, al
@@ -82,5 +82,5 @@
 comiss xmm0, dword ptr [K:0.75]
 jae L
-nop word ptr [rax + rax]
+nop dword ptr [rax]
 xor eax, eax
 lea rsp, [rbp - 0x28]
@@ -96,5 +96,5 @@
 xor edx, edx
 mov ecx, 0xffffffff
-mov rsi, r14
+mov rsi, r13
 mov rax, qword ptr [rdi]
 call qword ptr [rax + 0x868]
@@ -137,5 +137,5 @@
 xor edx, edx
 mov ecx, 0xffffffff
-mov rsi, r14
+mov rsi, r13
 mov rax, qword ptr [rdi]
 call qword ptr [rax + 0x868]
@@ -255,5 +255,5 @@
 call qword ptr [rax + 0xac8]
 mov rdi, qword ptr [rbx + 8]
-mov r15d, eax
+mov r14d, eax
 call F
 mov esi, 0xffffffff
@@ -263,6 +263,6 @@
 call qword ptr [rax + 0xac8]
 pxor xmm0, xmm0
-add r15d, eax
-cvtsi2ss xmm0, r15d
+add r14d, eax
+cvtsi2ss xmm0, r14d
 addss xmm0, dword ptr [K:100]
 comiss xmm0, dword ptr [rbp - 0x70]
@@ -273,5 +273,5 @@
 call F
 mov rdi, qword ptr [rbx + 8]
-mov r15, rax
+mov r14, rax
 call F
 mov rdi, rax
@@ -279,15 +279,17 @@
 sub rsp, 8
 mov r9d, r12d
-mov r8, r15
+mov r8, r14
 mov esi, eax
+movd xmm6, r15d
+mov rdi, rbx
+pxor xmm0, xmm0
+lea rax, [rbp - 0x5c]
 mov ecx, 1
 mov edx, 3
-pxor xmm0, xmm0
-lea rax, [rbp - 0x5c]
-mov rdi, rbx
 push rax
 lea rax, [rbp - 0x50]
 push rax
-push r13
+cvttss2si eax, xmm6
+push rax
 call F
 add rsp, 0x20
@@ -309,5 +311,5 @@
 xor edx, edx
 mov dword ptr [rbx + 0x14], 0xffffffff
-mov rsi, r14
+mov rsi, r13
 mov rax, qword ptr [rdi]
 call qword ptr [rax + 0x868]
@@ -347,5 +349,5 @@
 xor edx, edx
 mov ecx, 0xffffffff
-mov rsi, r14
+mov rsi, r13
 mov rax, qword ptr [rdi]
 call qword ptr [rax + 0x868]
@@ -418,5 +420,5 @@
 comiss xmm1, xmm0
 ja L
-movd xmm5, r15d
+movd xmm5, r14d
 movq xmm1, qword ptr [rbp - 0x50]
 mov dword ptr [rbx + 0x14], 0xffffffff
```
