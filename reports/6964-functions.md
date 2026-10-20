# Dota 6964: изменения кода по функциям

Снимки `6963-11145455` → `6964-11146732`; funcdiff.py. В диффе: [S:…] — строка, [K:…] — константа из данных, F — вызов другой функции, L — переход внутри функции, [D]/[T] — прочие адреса. Регистры и смещения стека меняются и от перекомпиляции.

## libclient.so: функций 280912 → 280912; без изменений 280911, изменено 1, добавлено 0, удалено 0

### изменена: 0x5642140 (41233 байт) | строки: "EventGrantDefinition_Item_t"; "EventGrantDefinition_LootList_t"; "EventGrantDefinition_Action_t"; "EventGrantDefinition_Points_t"; "scripts/height_levels.txt"; "EventGrantDefinition_ActionList_t"; "EventGrantDefinition_Trophy_t"; "EventGrantDefinition_PeriodicPoints_t"
было: 0x5642140 (41227 байт)
- числа в инструкциях: +0x280 +0x280
- инструкций: 6641 → 6641
```diff
@@ -2295,44 +2295,44 @@
 lea r14, [D]
 xor eax, eax
-xor ecx, ecx
-xor r8d, r8d
-mov r9, rbx
 xor edx, edx
+xor r8d, r8d
+mov r9, rbx
+mov ecx, 0x280
+mov byte ptr [rbp - 0x40], 0
+mov rdi, r14
 mov word ptr [rbp - 0xac], ax
-mov rdi, r14
 mov eax, 3
-mov dword ptr [rbp - 0xb0], 0
 lea rsi, [S:"dota_audio_language_storage"]
 mov word ptr [rbp - 0x50], ax
-mov byte ptr [rbp - 0xaa], 0
-mov qword ptr [rbp - 0xa9], 0
-mov qword ptr [rbp - 0xa1], 0
-mov qword ptr [rbp - 0x99], 0
-mov qword ptr [rbp - 0x91], 0
-mov qword ptr [rbp - 0x89], 0
-mov qword ptr [rbp - 0x81], 0
-mov qword ptr [rbp - 0x78], 0
-mov qword ptr [rbp - 0x70], 0
-mov qword ptr [rbp - 0x68], 0
-mov qword ptr [rbp - 0x60], 0
-mov qword ptr [rbp - 0x58], 0
-mov byte ptr [rbp - 0x40], 0
-mov qword ptr [rbp - 0x48], 0
-call F
-mov rsi, r14
-mov rdx, r12
-lea rdi, [T]
-call F
-lea r14, [D]
-xor eax, eax
-xor ecx, ecx
+mov dword ptr [rbp - 0xb0], 0
+mov byte ptr [rbp - 0xaa], 0
+mov qword ptr [rbp - 0xa9], 0
+mov qword ptr [rbp - 0xa1], 0
+mov qword ptr [rbp - 0x99], 0
+mov qword ptr [rbp - 0x91], 0
+mov qword ptr [rbp - 0x89], 0
+mov qword ptr [rbp - 0x81], 0
+mov qword ptr [rbp - 0x78], 0
+mov qword ptr [rbp - 0x70], 0
+mov qword ptr [rbp - 0x68], 0
+mov qword ptr [rbp - 0x60], 0
+mov qword ptr [rbp - 0x58], 0
+mov qword ptr [rbp - 0x48], 0
+call F
+mov rsi, r14
+mov rdx, r12
+lea rdi, [T]
+call F
 mov edx, 3
 mov r9, rbx
-xor r8d, r8d
-mov byte ptr [rbp - 0x40], 0
+xor eax, eax
+lea r14, [D]
+xor r8d, r8d
+mov ecx, 0x280
 mov word ptr [rbp - 0x50], dx
-mov rdi, r14
+lea rsi, [S:"dota_ui_language_storage"]
 xor edx, edx
-lea rsi, [S:"dota_ui_language_storage"]
+mov rdi, r14
+mov byte ptr [rbp - 0x40], 0
 mov word ptr [rbp - 0xac], ax
 mov dword ptr [rbp - 0xb0], 0
@@ -2423,39 +2423,39 @@
 mov ecx, 0x8080
 xor edx, edx
+mov word ptr [rbp - 0xac], r9w
+mov rdi, r14
+mov r9, rbx
 mov word ptr [rbp - 0x50], r10w
 lea rsi, [S:"dota_player_selection_cycle_ignores_groups"]
-mov rdi, r14
-mov word ptr [rbp - 0xac], r9w
-mov r9, rbx
-mov dword ptr [rbp - 0xb0], 0
-mov byte ptr [rbp - 0xaa], 0
-mov qword ptr [rbp - 0xa9], 0
-mov qword ptr [rbp - 0xa1], 0
-mov qword ptr [rbp - 0x99], 0
-mov qword ptr [rbp - 0x91], 0
-mov qword ptr [rbp - 0x89], 0
-mov qword ptr [rbp - 0x81], 0
-mov qword ptr [rbp - 0x78], 0
-mov qword ptr [rbp - 0x70], 0
-mov qword ptr [rbp - 0x68], 0
-mov qword ptr [rbp - 0x60], 0
-mov qword ptr [rbp - 0x58], 0
-mov byte ptr [rbp - 0x40], 0
-mov qword ptr [rbp - 0x48], 0
-call F
-mov rsi, r14
-mov rdx, r12
+mov byte ptr [rbp - 0x40], 0
+mov dword ptr [rbp - 0xb0], 0
+mov byte ptr [rbp - 0xaa], 0
+mov qword ptr [rbp - 0xa9], 0
+mov qword ptr [rbp - 0xa1], 0
+mov qword ptr [rbp - 0x99], 0
+mov qword ptr [rbp - 0x91], 0
+mov qword ptr [rbp - 0x89], 0
+mov qword ptr [rbp - 0x81], 0
+mov qword ptr [rbp - 0x78], 0
+mov qword ptr [rbp - 0x70], 0
+mov qword ptr [rbp - 0x68], 0
+mov qword ptr [rbp - 0x60], 0
+mov qword ptr [rbp - 0x58], 0
+mov qword ptr [rbp - 0x48], 0
```
(ещё 594 строк диффа: so-query.py fdiff libclient.so 0x5642140)

## libserver.so: функций 220000 → 220000; без изменений 219999, изменено 1, добавлено 0, удалено 0

### изменена: 0x5086d00 (2392 байт) | строки: "!bCanIncrementStats"; "BaseKillEaterFound without stat tracking item."
было: 0x5086d00 (2392 байт)
- числа в инструкциях: +0x74eb −0x74e7
- инструкций: 506 → 506
```diff
@@ -493,5 +493,5 @@
 movdqa xmm4, xmmword ptr [rbp - 0x2c0]
 mov rdi, r13
-mov dword ptr [rbp - 0x258], 0x74e7
+mov dword ptr [rbp - 0x258], 0x74eb
 mov qword ptr [rbp - 0x260], rax
 movzx eax, byte ptr [rbp - 0x254]
```
