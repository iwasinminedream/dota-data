# Dota 6974: изменения кода по функциям

Снимки `6973-11220405` → `6974-11230346`; funcdiff.py. В диффе: [S:…] — строка, [K:…] — константа из данных, F — вызов другой функции, L — переход внутри функции, [D]/[T] — прочие адреса. Регистры и смещения стека меняются и от перекомпиляции.

## libclient.so: функций 280912 → 280912; без изменений 280912, изменено 0, добавлено 0, удалено 0

## libserver.so: функций 220000 → 220000; без изменений 219990, изменено 6, добавлено 1, удалено 1

### изменена: 0x4d42940 (426 байт) вызывается из: CDOTA_Modifier_Item_Chipped_Vest::vfunc#95
было: 0x4d428c0 (346 байт)
- числа в инструкциях: +-1 +-2 +9 +0x3f +0x1ff +0x70
- поля объектов: +0xcc +0xcc +0x10
- прямых вызовов: 8 → 7
- инструкций: 86 → 102
```diff
@@ -39,8 +39,24 @@
 cmp dword ptr [r14 + 0x3c], 1
 jne L
-lea rdi, [r14 + 0xcc]
-call F
-test rax, rax
+mov ecx, dword ptr [r14 + 0xcc]
+cmp ecx, -1
 je L
+mov rsi, qword ptr [D]
+test rsi, rsi
+je L
+cmp ecx, -2
+je L
+movzx eax, word ptr [r14 + 0xcc]
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
 mov rbx, qword ptr [rax]
 test rbx, rbx
```

### изменена: 0x4d425e0 (122 байт) CDOTA_Modifier_Aghanims_Shard::OnIntervalThink
было: 0x4d42a20 (68 байт)
- числа в инструкциях: +-1 +-2 +9 +0x3f +0x1ff +0x70
- поля объектов: +0x1aa8 +0x1aa8 +0x10
- прямых вызовов: 3 → 2
- инструкций: 19 → 35
```diff
@@ -6,8 +6,24 @@
 movss xmm0, dword ptr [K:-1]
 call F
-lea rdi, [rbx + 0x1aa8]
-call F
-test rax, rax
+mov ecx, dword ptr [rbx + 0x1aa8]
+cmp ecx, -1
 je L
+mov rsi, qword ptr [D]
+test rsi, rsi
+je L
+cmp ecx, -2
+je L
+movzx eax, word ptr [rbx + 0x1aa8]
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
 mov rdi, qword ptr [rax]
 test rdi, rdi
```

### изменена: 0x4d435d0 (544 байт) вызывается из: CDOTA_Modifier_Item_Caster_Rapier::vfunc#95 | строки: "modifier_silver_edge_debuff"; "duration"; "DOTA_Item.SilverEdge.Target"
было: 0x4d43550 (458 байт)
- числа в инструкциях: +-1 +-2 +9 +0x3f +0x7fff +0x1ff +0x70
- поля объектов: +0xd0 +0xd0 +0x10
- прямых вызовов: 11 → 10
- инструкций: 117 → 136
```diff
@@ -42,8 +42,26 @@
 cmp dword ptr [r13 + 0x3c], 1
 jne L
-lea rdi, [r13 + 0xd0]
-call F
+mov ecx, dword ptr [r13 + 0xd0]
+cmp ecx, -1
+je L
+mov rsi, qword ptr [D]
+test rsi, rsi
+je L
+cmp ecx, -2
+je L
+movzx eax, word ptr [r13 + 0xd0]
+mov edx, eax
+shr rax, 9
+and eax, 0x3f
+and dx, 0x7fff
+mov rax, qword ptr [rsi + rax*8]
 test rax, rax
 je L
+and edx, 0x1ff
+xor r14d, r14d
+imul rdx, rdx, 0x70
+add rax, rdx
+cmp ecx, dword ptr [rax + 0x10]
+jne L
 mov r14, qword ptr [rax]
 test r14, r14
@@ -111,7 +129,8 @@
 nop
 add rax, 1
-cmp rax, rdi
+cmp rdi, rax
 jne L
 jmp L
+nop word ptr [rax + rax]
 xor r14d, r14d
 jmp L
```

### изменена: 0x4d488e0 (1233 байт) CDOTA_Modifier_Aghanims_Shard::OnCreated | строки: "source_item"; "tormentor"; "particles/items_fx/aghanims_shard.vpcf"; "shard_acquired"
было: 0x4d43890 (897 байт)
- числа в инструкциях: +1 +1 +1 +0 +0 +0 +0 +0 (и ещё 10)
- виртуальные вызовы: +0xe8 (слот 29) +0xe8 (слот 29)
- поля объектов: +0x878 +0x878 +0x8f1 +0x8f1
- прямых вызовов: 32 → 40
- инструкций: 232 → 294
```diff
@@ -10,7 +10,8 @@
 mov rbx, rsi
 lea rsi, [S:"source_item"]
-sub rsp, 0x18
-mov rdi, rbx
-call F
+sub rsp, 0x68
+mov rdi, rbx
+call F
+lea rdi, [r13 + 0x1aa8]
 test rax, rax
 je L
@@ -31,7 +32,8 @@
 or eax, edx
 mov dword ptr [r13 + 0x1aa8], eax
-jmp L
+call F
+test rax, rax
+jne L
 nop dword ptr [rax + rax]
-mov dword ptr [r13 + 0x1aa8], 0xffffffff
 lea rsi, [S:"tormentor"]
 xor edx, edx
@@ -40,5 +42,5 @@
 mov rdi, r13
 xor ebx, ebx
-mov dword ptr [rbp - 0x34], eax
+mov dword ptr [rbp - 0x84], eax
 lea r14, [T]
 call F
@@ -104,7 +106,66 @@
 jmp L
 nop
+mov dword ptr [r13 + 0x1aa8], 0xffffffff
+call F
+test rax, rax
+je L
+mov r12, qword ptr [rax]
+test r12, r12
+je L
+cmp byte ptr [r12 + 0x878], 0
+jne L
+lea r14, [rbp - 0x68]
+xor r9d, r9d
+pxor xmm0, xmm0
+mov dword ptr [rbp - 0x74], 0x878
+lea rsi, [rbp - 0x74]
+mov rdi, r14
+movaps xmmword ptr [rbp - 0x50], xmm0
+mov word ptr [rbp - 0x34], r9w
+lea r15, [rbp - 0x70]
+mov qword ptr [rbp - 0x70], 1
+mov qword ptr [rbp - 0x68], 0
+mov qword ptr [rbp - 0x60], 0
+mov qword ptr [rbp - 0x58], 0
+mov qword ptr [rbp - 0x40], 0xffffffffffffffff
+mov dword ptr [rbp - 0x38], 0xffffffff
+call F
+mov rax, qword ptr [r12]
+mov rsi, r15
+mov rdi, r12
+call qword ptr [rax + 0xe8]
+mov rdi, r14
+call F
+mov byte ptr [r12 + 0x878], 1
+cmp byte ptr [r12 + 0x8f1], 0
+je L
+lea r14, [rbp - 0x68]
+xor r8d, r8d
+pxor xmm0, xmm0
+mov dword ptr [rbp - 0x74], 0x8f1
+lea rsi, [rbp - 0x74]
+mov rdi, r14
+movaps xmmword ptr [rbp - 0x50], xmm0
+mov word ptr [rbp - 0x34], r8w
+lea r15, [rbp - 0x70]
+mov qword ptr [rbp - 0x70], 1
+mov qword ptr [rbp - 0x68], 0
+mov qword ptr [rbp - 0x60], 0
+mov qword ptr [rbp - 0x58], 0
+mov qword ptr [rbp - 0x40], 0xffffffffffffffff
+mov dword ptr [rbp - 0x38], 0xffffffff
+call F
+mov rax, qword ptr [r12]
+mov rsi, r15
+mov rdi, r12
+call qword ptr [rax + 0xe8]
+mov rdi, r14
+call F
+mov byte ptr [r12 + 0x8f1], 0
+jmp L
+nop word ptr [rax + rax]
 test byte ptr [r12 + 0xcd4], 1
 jne L
-mov ecx, dword ptr [rbp - 0x34]
+mov ecx, dword ptr [rbp - 0x84]
 test ecx, ecx
 jne L
@@ -119,4 +180,5 @@
 pop rbp
 jmp F
+nop dword ptr [rax + rax]
 mov rdi, r15
 call rax
@@ -128,5 +190,5 @@
 mov rax, qword ptr [r15 + 0x840]
 jmp L
-nop word ptr cs:[rax + rax]
+nop
 cmp byte ptr [r12 + 0x16d2], 0
 jne L
```

### изменена: 0x4d48780 (153 байт) CDOTA_Modifier_Item_Arcane_Blink_Buff::OnCreated | строки: "cast_pct_improvement"; "manacost_reduction"; "debuff_amp"; "cast_range_bonus"
было: 0x4d47b30 (134 байт)
- числа в инструкциях: +0xffffffff
- поля объектов: +0x1aa8
- инструкций: 30 → 37
```diff
@@ -5,9 +5,16 @@
 sub rsp, 8
 call F
-lea rsi, [rbx + 0x1aa8]
-lea rdx, [S:"cast_pct_improvement"]
 mov rdi, rax
+xor eax, eax
+test rdi, rdi
+je L
+xor r9d, r9d
+xor r8d, r8d
+xor ecx, ecx
+lea rsi, [S:"cast_pct_improvement"]
+mov edx, 0xffffffff
 call F
 mov rdi, rbx
+mov dword ptr [rbx + 0x1aa8], eax
 call F
 lea rsi, [rbx + 0x1aac]
```

### изменена: 0x4d4dfe0 (3179 байт) | строки: "m_iStoredRuneType"; "int"; "int32"; "OnChaliceStoredRuneChanged"; "CDOTA_Item_Bottomless_Chalice"; "15CNetworkVarBaseIiN29CDOTA_Item_Bottomless_Chalice28NetworkVar_m_iStoredRuneTyp"
было: 0x4d4df20 (3179 байт)
- прямых вызовов: 69 → 68
- инструкций: 642 → 640
```diff
@@ -58,7 +58,4 @@
 mov esi, 0x31415937
 mov rdi, rbx
-call F
-lea rdi, [rbx + 4]
-mov esi, eax
 call F
 lea rdi, [rbx + 8]
@@ -457,4 +454,5 @@
 call F
 jmp L
+nop dword ptr [rax + rax]
 mov eax, r12d
 xor edx, edx
```

### добавлена: 0x4d496d0 (225 байт)

### удалена: 0x4d48dc0 (570 байт) | строки: "CNetworkTransmitComponent::StateChanged(%s) @%s:%d"

### копии существующего кода (2): шаблонные / склеенные компоновщиком функции, такой же код есть и в другой сборке — не новый код
- ещё одна копия существующего кода: 0x4d49910 (118 байт)
- одной копией существующего кода меньше: 0x4d49150 (118 байт)
