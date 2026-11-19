# Dota 6983: изменения кода по функциям

Снимки `6980-11256062` → `6983-11256873`; funcdiff.py. В диффе: [S:…] — строка, [K:…] — константа из данных, F — вызов другой функции, L — переход внутри функции, [D]/[T] — прочие адреса. Регистры и смещения стека меняются и от перекомпиляции.

## libserver.so: функций 221833 → 221833; без изменений 221831, изменено 2, добавлено 0, удалено 0

### изменена: 0x5c19ae0 (2330 байт)
было: 0x5c19ae0 (2314 байт)
- инструкций: 529 → 532
```diff
@@ -222,14 +222,17 @@
 mov rdi, r12
 call F
-test al, al
-je L
-movss xmm1, dword ptr [r15 + 0x54]
-pxor xmm0, xmm0
+movaps xmm1, xmm0
+movss xmm0, dword ptr [r15 + 0x54]
 comiss xmm1, xmm0
 jp L
 je L
 jbe L
-movss xmm1, dword ptr [r15 + 0x50]
-comiss xmm1, xmm0
+pxor xmm1, xmm1
+comiss xmm0, xmm1
+jp L
+je L
+jbe L
+movss xmm0, dword ptr [r15 + 0x50]
+comiss xmm0, xmm1
 ja L
 pxor xmm0, xmm0
```

### изменена: 0x5c1a400 (727 байт) вызывается из: CDOTA_BaseNPC::vfunc#512 | строки: "<NoAbilityName>"
было: 0x5c1a3f0 (753 байт)
- числа в инструкциях: +3 −1
- поля объектов: +0xc −0x10 −0x18 −0x20
- прямых вызовов: 15 → 12
- инструкций: 153 → 151
```diff
@@ -104,7 +104,10 @@
 je L
 jmp L
+nop dword ptr [rax]
 mov rdi, rbx
 call F
 mov rdi, qword ptr [rbx + 0x10]
+cmp dword ptr [rdi + 8], 3
+je L
 call F
 mov rdi, qword ptr [rbx + 0x18]
@@ -113,5 +116,7 @@
 mov rdi, r13
 call F
+test r12, r12
 mov dword ptr [r13 + 8], 1
+je L
 mov rax, qword ptr [r12 + 0x10]
 test rax, rax
@@ -138,16 +143,9 @@
 pop rbp
 ret
-nop word ptr cs:[rax + rax]
-call F
-mov rdi, qword ptr [rbx + 0x10]
-call F
-mov rdi, qword ptr [rbx + 0x18]
-call F
-mov r13, qword ptr [rbx + 0x20]
-mov rdi, r13
-call F
-test r12, r12
-mov dword ptr [r13 + 8], 1
-jne L
+nop dword ptr [rax]
 mov dword ptr [r13 + 0x58], 0xffffffff
 jmp L
+nop word ptr [rax + rax]
+movq xmm0, qword ptr [rdi + 0xc]
+call F
+jmp L
```
