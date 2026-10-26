# Dota 6968: изменения кода по функциям

Снимки `6967-11168076` → `6968-11170778`; funcdiff.py. В диффе: [S:…] — строка, [K:…] — константа из данных, F — вызов другой функции, L — переход внутри функции, [D]/[T] — прочие адреса. Регистры и смещения стека меняются и от перекомпиляции.

## libclient.so: функций 280912 → 280912; без изменений 280912, изменено 0, добавлено 0, удалено 0

## libserver.so: функций 220000 → 220000; без изменений 219997, изменено 3, добавлено 0, удалено 0

### изменена: 0x49e56a0 (743 байт) CDOTA_Modifier_Meepo_MegaMeepo::OnDestroy | строки: "modifier_knockback"; "center_x"; "center_y"; "center_z"; "end_knockback_duration"; "duration"; "should_stun"; "end_knockback_distance"
было: 0x49e5640 (703 байт)
- числа в инструкциях: +0xffffffdf
- виртуальные вызовы: +0x6b8 (слот 215)
- поля объектов: +0x6c0
- прямых вызовов: 39 → 42
- инструкций: 179 → 189
```diff
@@ -71,4 +71,14 @@
 xor esi, esi
 mov rdi, rax
+call F
+mov rdi, rbx
+call F
+mov esi, dword ptr [rax + 0x6c0]
+mov r12, rax
+mov rax, qword ptr [rax]
+mov rdi, r12
+and esi, 0xffffffdf
+call qword ptr [rax + 0x6b8]
+mov rdi, r12
 call F
 mov rdi, rbx
```

### изменена: 0x4a6daf0 (1501 байт) CDOTA_Ability_Legion_Commander_PressTheAttack::OnSpellStart | строки: "radius"; "Hero_LegionCommander.PressTheAttack"; "particles/units/heroes/hero_legion_commander/legion_commander_press_the_attack_a"
было: 0x4a7bdb0 (1618 байт)
- числа в инструкциях: −1 −1 −1 −1
- инструкций: 338 → 319
```diff
@@ -48,9 +48,10 @@
 mov rdi, rbx
 mov qword ptr [rbp - 0xe8], 0
+lea r14, [rbp - 0xf0]
+mov qword ptr [rbp - 0xe0], 0
 lea r13, [rbp - 0xd0]
-mov qword ptr [rbp - 0xe0], 0
-call F
-mov rdi, rbx
-mov r14, rax
+call F
+mov rdi, rbx
+mov r15, rax
 call F
 mov rdi, rbx
@@ -59,52 +60,51 @@
 call F
 mov rdi, rbx
-movzx r15d, byte ptr [rax + 0x624]
-call F
-mov rdi, rax
-call F
-push 0
-mov rcx, r14
+movzx esi, byte ptr [rax + 0x624]
+mov dword ptr [rbp - 0x128], esi
+call F
+mov rdi, rax
+call F
+push 0
+mov rcx, r15
 mov rdx, r13
 push 0
 mov rdi, rax
-mov esi, r15d
 mov r9d, 1
-push 0
-lea r8, [rbp - 0xf0]
+mov r8, r14
+push 0
 push 0x13
+mov esi, dword ptr [rbp - 0x128]
 movss xmm0, dword ptr [rbp - 0x124]
 call F
 add rsp, 0x20
 mov rsi, r12
-mov dword ptr [rbp - 0x100], 0xffffffff
-lea rdi, [rbp - 0x100]
-call F
-mov r8d, dword ptr [rbp - 0xf0]
-mov edx, dword ptr [rbp - 0x100]
-test r8d, r8d
-movsxd r14, r8d
-jle L
-mov rcx, qword ptr [rbp - 0xe8]
-movsxd r14, r8d
-xor eax, eax
-jmp L
-nop word ptr [rax + rax]
-add rax, 1
-cmp r14, rax
-je L
-cmp dword ptr [rcx + rax*4], edx
-jne L
-mov rdi, rbx
-call F
-test rax, rax
-je L
-mov rdi, rbx
-call F
+mov dword ptr [rbp - 0xf8], 0xffffffff
 lea rdi, [rbp - 0xf8]
-mov dword ptr [rbp - 0xf8], 0xffffffff
-mov rsi, rax
 call F
 movsxd rdx, dword ptr [rbp - 0xf0]
 mov ecx, dword ptr [rbp - 0xf8]
+test edx, edx
+jle L
+mov rsi, qword ptr [rbp - 0xe8]
+xor eax, eax
+jmp L
+nop
+add rax, 1
+cmp rdx, rax
+je L
+cmp dword ptr [rsi + rax*4], ecx
+jne L
+mov rdi, rbx
+call F
+test rax, rax
+je L
+mov rdi, rbx
+call F
+lea rdi, [rbp - 0xf4]
+mov dword ptr [rbp - 0xf4], 0xffffffff
+mov rsi, rax
+call F
+movsxd rdx, dword ptr [rbp - 0xf0]
+mov ecx, dword ptr [rbp - 0xf4]
 test edx, edx
 jle L
@@ -268,6 +268,7 @@
 mov rdi, rbx
 mov qword ptr [rbp - 0xe8], 0
+lea r14, [rbp - 0xf0]
+mov qword ptr [rbp - 0xe0], 0
 lea r13, [rbp - 0xd0]
-mov qword ptr [rbp - 0xe0], 0
 call F
 mov rdi, rbx
@@ -279,5 +280,5 @@
 call F
 mov rdi, rbx
-movzx r14d, byte ptr [rax + 0x624]
+movzx r15d, byte ptr [rax + 0x624]
 call F
 mov rdi, rax
@@ -285,11 +286,11 @@
 push 0
```
(ещё 71 строк диффа: so-query.py fdiff libserver.so 0x4a6daf0)

### изменена: 0x4aa79f0 (3322 байт) | строки: "m_hDoubleShotTarget"; "EHANDLE"; "CHandle< T >"; "uint32"; "CBaseEntity"; "CHandle< %s >"; "ehandle"; "CDOTA_Unit_Hero_Muerta"
было: 0x4aa7a30 (3290 байт)
- числа в инструкциях: +0x5bd1e995 +0x5bd1e995 +0xd +0xf +0x6174
- прямых вызовов: 69 → 68
- инструкций: 658 → 665
```diff
@@ -450,13 +450,19 @@
 mov esi, eax
 call F
-lea rdi, [r13 + 0x14]
-mov esi, eax
-call F
-mov rdx, r13
+lea rcx, [rbp - 0xc0]
 mov rsi, rbx
 mov rdi, r15
-lea rcx, [rbp - 0xc0]
+xor eax, 0x6174
 mov r9d, 2
 mov r8d, 0x2300
+imul eax, eax, 0x5bd1e995
+mov edx, eax
+shr edx, 0xd
+xor eax, edx
+imul eax, eax, 0x5bd1e995
+mov edx, eax
+shr edx, 0xf
+xor eax, edx
+mov rdx, r13
 mov dword ptr [rbp - 0xc0], eax
 call F
@@ -468,5 +474,5 @@
 call F
 jmp L
-nop dword ptr [rax + rax]
+nop
 mov eax, r13d
 xor edx, edx
@@ -614,5 +620,6 @@
 jle L
 nop word ptr cs:[rax + rax]
-nop
+nop word ptr cs:[rax + rax]
+nop word ptr [rax + rax]
 add ebx, r14d
 mov eax, ebx
```
