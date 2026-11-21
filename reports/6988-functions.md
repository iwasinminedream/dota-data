# Dota 6988: изменения кода по функциям и строки библиотек

Снимки `6987-11262367` → `6988-11263542`; funcdiff.py. В диффе: [S:…] — строка, [K:…] — константа из данных, F — вызов другой функции, L — переход внутри функции, [D]/[T] — прочие адреса. Регистры и смещения стека меняются и от перекомпиляции. Здесь всё, в том числе игровые функции и изменения от пересборки.

## libclient.so: функций 281894 → 281893; без изменений 281886, изменено 5, добавлено 0, удалено 0

### изменена: 0x48a9cb0 (158 байт) C_DOTA_Ability_Pugna_LifeDrain::GetBehavior
было: 0x48a9cb0 (273 байт)
- поля объектов: −0x900 −0x10 −0x38
- прямых вызовов: 5 → 2
- цели вызовов: −C_DOTA_Ability_Pugna_LifeDrain::GetChannelTime −0x567f990 "AbilityDuration"
- инструкций: 69 → 45
```diff
@@ -2,68 +2,44 @@
 lea rdx, [T]
 mov rbp, rsp
+push r12
 push rbx
+mov rax, qword ptr [rdi]
 mov rbx, rdi
-sub rsp, 0x18
-mov rax, qword ptr [rdi]
 mov rax, qword ptr [rax + 0x8f8]
 cmp rax, rdx
 jne L
-movss xmm1, dword ptr [rdi + 0x7cc]
-pxor xmm0, xmm0
-ucomiss xmm1, xmm0
+movss xmm0, dword ptr [rdi + 0x7cc]
+pxor xmm1, xmm1
+ucomiss xmm0, xmm1
 jp L
+mov r12d, 0x20000000
 jne L
-mov rdx, qword ptr [rbx + 0x770]
-mov eax, 0x20000000
-test rdx, rdx
+mov rax, qword ptr [rbx + 0x770]
+test rax, rax
 je L
-or rax, qword ptr [rdx + 0x58]
-mov rbx, qword ptr [rbp - 8]
-leave
+or r12, qword ptr [rax + 0x58]
+pop rbx
+mov rax, r12
+pop r12
+pop rbp
 ret
 nop dword ptr [rax]
-mov rax, qword ptr [rbx]
-lea rdx, [T]
-movss dword ptr [rbp - 0x1c], xmm1
-mov rdi, rbx
-mov rax, qword ptr [rax + 0x900]
-cmp rax, rdx
-jne L
-call F
-movss xmm1, dword ptr [rbp - 0x1c]
-movss dword ptr [rbp - 0x18], xmm0
-mov rax, qword ptr [rbx + 0x10]
-movss dword ptr [rbp - 0x1c], xmm1
-mov edi, dword ptr [rax + 0x38]
-call F
-movss xmm1, dword ptr [rbp - 0x1c]
-movaps xmm2, xmm0
-movss xmm0, dword ptr [rbp - 0x18]
-addss xmm0, xmm1
-comiss xmm2, xmm0
-jp L
-je L
-ja L
-mov rdx, qword ptr [rbx + 0x770]
-mov eax, 0x20400000
-test rdx, rdx
+mov rax, qword ptr [rbx + 0x770]
+mov r12d, 0x20400000
+test rax, rax
 jne L
 mov rdi, rbx
 xor esi, esi
-mov qword ptr [rbp - 0x18], rax
 call F
-mov rdx, qword ptr [rbx + 0x770]
-mov rax, qword ptr [rbp - 0x18]
-mov rbx, qword ptr [rbp - 8]
-or rax, qword ptr [rdx + 0x58]
-leave
+mov rax, qword ptr [rbx + 0x770]
+pop rbx
+or r12, qword ptr [rax + 0x58]
+mov rax, r12
+pop r12
+pop rbp
 ret
-nop dword ptr [rax + rax]
-call rax
-movaps xmm1, xmm0
-jmp L
 nop word ptr [rax + rax]
 call rax
-movss xmm1, dword ptr [rbp - 0x1c]
-movss dword ptr [rbp - 0x18], xmm0
 jmp L
+mov rax, qword ptr [0]
+ud2
```

### изменена: 0x48dddd0 (3600 байт)
было: 0x48dde70 (3842 байт)
- числа в инструкциях: −-1 −-1 −-1 −0x7fff −3
- поля объектов: −0x28 −0x1a −0x20 −0x20 −0x18 −0x18 −0x10
- прямых вызовов: 37 → 35
- цели вызовов: −0x7469620
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

### изменена: 0x579c220 (838 байт)
было: 0x579c2a0 (927 байт)
- виртуальные вызовы: −0x900 (слот 288)
- поля объектов: −0x10 −0x38
- прямых вызовов: 20 → 18
- инструкций: 241 → 221
```diff
@@ -23,7 +23,7 @@
 cmp byte ptr [rax + 0x58], 0
 jne L
+test r13d, r13d
+je L
 test rdx, rdx
-je L
-test r13d, r13d
 je L
 call F
@@ -133,31 +133,30 @@
 je L
 movzx eax, byte ptr [rbp - 0x38]
+lea r15, [T]
 xor r12d, r12d
 mov dword ptr [rbp - 0x38], eax
 jmp L
-nop dword ptr [rax]
-mov rax, qword ptr [r14 + 0x770]
-test rax, rax
-je L
-mov rcx, qword ptr [rax + 0x58]
-test ecx, 0x400000
-mov rax, rdx
-jne L
-mov rdx, qword ptr [rdx + 0x8f8]
+mov rax, qword ptr [rdi + 0x770]
+test rax, rax
+je L
+mov rax, qword ptr [rax + 0x58]
+test eax, 0x400000
+jne L
+mov rax, qword ptr [r11 + 0x8f8]
 lea rcx, [T]
-cmp rdx, rcx
-jne L
-movss xmm1, dword ptr [r14 + 0x7cc]
-pxor xmm3, xmm3
-ucomiss xmm1, xmm3
+cmp rax, rcx
+jne L
+movss xmm0, dword ptr [rdi + 0x7cc]
+pxor xmm1, xmm1
+ucomiss xmm0, xmm1
 jp L
 jne L
+mov r11, qword ptr [rdi]
 xor r8d, r8d
 mov edx, dword ptr [rbp - 0x38]
 mov r9d, 1
 mov ecx, r13d
-mov rsi, r15
-mov rdi, r14
-call qword ptr [rax + 0x8a8]
+mov rsi, r14
+call qword ptr [r11 + 0x8a8]
 test al, al
 jne L
@@ -171,5 +170,5 @@
 call F
 test rax, rax
-mov r15, rax
+mov r14, rax
 je L
 mov rsi, qword ptr [rbp - 0x40]
@@ -177,48 +176,30 @@
 call F
 test rax, rax
-mov r14, rax
-je L
-mov rdx, qword ptr [rax]
-lea rcx, [T]
-mov rax, qword ptr [rdx + 0x748]
-cmp rax, rcx
-je L
+mov rdi, rax
+je L
+mov r11, qword ptr [rax]
+mov rax, qword ptr [r11 + 0x748]
+cmp rax, r15
+je L
+mov qword ptr [rbp - 0x48], rdi
+call rax
+mov rdi, qword ptr [rbp - 0x48]
+mov r11, qword ptr [rdi]
+jmp L
+nop word ptr [rax + rax]
+mov ecx, r13d
+mov esi, r15d
 mov rdi, r14
-call rax
-mov rdx, qword ptr [r14]
-mov rcx, rax
+call F
 jmp L
 nop dword ptr [rax + rax]
-mov ecx, r13d
-mov esi, r15d
-mov rdi, r14
-call F
-jmp L
-nop dword ptr [rax + rax]
-movss dword ptr [rbp - 0x48], xmm1
-mov rdi, r14
-call qword ptr [rax + 0x900]
-mov rax, qword ptr [rbx + 0x10]
-movss dword ptr [rbp - 0x44], xmm0
-mov edi, dword ptr [rax + 0x38]
-call F
-movss xmm1, dword ptr [rbp - 0x48]
-movaps xmm2, xmm0
-movss xmm0, dword ptr [rbp - 0x44]
-addss xmm0, xmm1
-comiss xmm2, xmm0
-jp L
-je L
-jbe L
-mov rax, qword ptr [r14]
-jmp L
-nop dword ptr [rax]
```
(ещё 28 строк диффа: so-query.py fdiff libclient.so 0x579c220)

### изменена: 0x579ef90 (1234 байт) вызывается из: C_DOTAPlayerController::vfunc#114 | строки: "model"; "skin"; "ItemData"
было: 0x579f050 (1186 байт)
- числа в инструкциях: +0 +0 +0
- прямых вызовов: 27 → 28
- цели вызовов: +0x57ceee0 +0x532eca0
- инструкций: 249 → 259
```diff
@@ -179,13 +179,23 @@
 pop rax
 pop rdx
-mov rdx, qword ptr [rbp - 0x118]
-mov rsi, r14
+mov esi, dword ptr [rbp - 0x94]
+mov rdx, r14
 mov qword ptr [rbp - 0xf0], r14
-mov rdi, qword ptr [rbp - 0x128]
 lea rax, [T]
+mov r13, qword ptr [rbp - 0x118]
 mov qword ptr [rbp - 0x100], 0
 mov qword ptr [rbp - 0x108], rax
+lea rax, [D]
 movdqu xmm1, xmmword ptr [rbp - 0x108]
+mov rcx, r13
 movups xmmword ptr [rbp - 0xe8], xmm1
+mov rdi, qword ptr [rax]
+call F
+mov rdi, qword ptr [rbp - 0x128]
+mov rdx, r13
+xor esi, esi
+mov qword ptr [rbp - 0xe8], 0
+mov qword ptr [rbp - 0xe0], 0
+mov qword ptr [rbp - 0xf0], 0
 call F
 mov r13, qword ptr [rbp - 0xb8]
@@ -205,5 +215,5 @@
 lea rdi, [rbp - 0xa0]
 call F
-nop word ptr cs:[rax + rax]
+nop dword ptr [rax]
 add ebx, 1
 add r15, 0x50
@@ -225,5 +235,5 @@
 pop rbp
 ret
-nop word ptr [rax + rax]
+nop
 mov r12, qword ptr [D]
 mov esi, 2
```

### изменена: 0x57ceee0 (558 байт)
было: 0x57cef60 (398 байт)
- числа в инструкциях: +-1 +-2 +9 +0x3f +0x1ff +0x70 +4
- поля объектов: +0x10
- прямых вызовов: 4 → 6
- цели вызовов: +__dynamic_cast() +0x57cee20
- инструкций: 128 → 181
```diff
@@ -1,2 +1,55 @@
+push rbp
+mov rbp, rsp
+push r13
+push r12
+push rbx
+sub rsp, 8
+mov rbx, qword ptr [rdx + 8]
+movsxd rax, dword ptr [rdx]
+lea r12, [rbx + rax*4]
+cmp r12, rbx
+je L
+mov r13, rdi
+mov eax, dword ptr [rbx]
+cmp eax, -1
+je L
+mov rcx, qword ptr [D]
+test rcx, rcx
+je L
+cmp eax, -2
+je L
+mov rdx, rax
+shr rdx, 9
+and edx, 0x3f
+mov rdx, qword ptr [rcx + rdx*8]
+test rdx, rdx
+je L
+mov ecx, eax
+and ecx, 0x1ff
+imul rcx, rcx, 0x70
+add rdx, rcx
+cmp eax, dword ptr [rdx + 0x10]
+jne L
+mov rdi, qword ptr [rdx]
+test rdi, rdi
+je L
+lea rsi, [D]
+xor ecx, ecx
+lea rdx, [D]
+call F
+test rax, rax
+mov rsi, rax
+je L
+mov rdi, r13
+call F
+add rbx, 4
+cmp r12, rbx
+jne L
+add rsp, 8
+pop rbx
+pop r12
+pop r13
+pop rbp
+ret
 cmp edi, 6
 ja L
```

### копии существующего кода (5): шаблонные / склеенные компоновщиком функции, такой же код есть и в другой сборке — не новый код
- ещё одна копия существующего кода: 0x48c61b0 (92 байт) C_DOTA_Ability_Slardar_Amplify_Damage::vfunc#50
- ещё одна копия существующего кода: 0x48dec00 (242 байт)
- одной копией существующего кода меньше: 0x48a9dc2 (10 байт) вызывается из: CDOTA_Unit_CustomGameAnnouncer::vfunc#174
- одной копией существующего кода меньше: 0x48c6690 (117 байт) CDOTA_Unit_Announcer_Killing_Spree::vfunc#50
- одной копией существующего кода меньше: 0x57cf0f0 (187 байт)

## libserver.so: функций 221951 → 221951; без изменений 221945, изменено 6, добавлено 0, удалено 0

### изменена: 0x476bb90 (668 байт) вызывается из: CDOTA_Modifier_Miniboss_Alleviation::vfunc#97 | строки: "hp_restoration_pct"; "radius"; "aura_duration"; "modifier_miniboss_alleviation_active_aura"; "duration"
было: 0x476bb90 (680 байт)
- прямых вызовов: 22 → 21
- инструкций: 177 → 173
```diff
@@ -52,5 +52,4 @@
 je L
 and eax, 0x1ff
-xor r14d, r14d
 imul rax, rax, 0x70
 add rax, rdx
@@ -62,8 +61,11 @@
 cmp byte ptr [r14 + 0x5d1], 3
 jne L
+test r13, r13
+je L
 mov rdi, r12
 call F
 cmp r13, rax
 je L
+nop word ptr cs:[rax + rax]
 pxor xmm0, xmm0
 mov qword ptr [rbx], 1
@@ -79,9 +81,6 @@
 ret
 nop dword ptr [rax]
-mov rdi, r12
-xor r14d, r14d
-call F
-cmp r13, rax
-jne L
+xor r13d, r13d
+jmp L
 movzx eax, byte ptr [r13 + 0x624]
 cmp byte ptr [r14 + 0x624], al
@@ -173,5 +172,2 @@
 call F
 jmp L
-nop dword ptr [rax]
-xor r13d, r13d
-jmp L
```

### изменена: 0x4770480 (7099 байт) CDOTA_Ability_Tinker_Keen_Teleport::OnAbilityPhaseStart | строки: "maximum_distance"; "good_healer_6"; "npc_dota_watch_tower_bottom"; "npc_dota_watch_tower_top"; "tower1"; "minimum_distance"; "particles/items2_fx/teleport_start.vpcf"; "particles/items2_fx/teleport_end.vpcf"
было: 0x4770490 (7035 байт)
- числа в инструкциях: +-1 +-2 +9 +0x3f +0x1ff +0x70
- поля объектов: +0x10
- прямых вызовов: 168 → 167
- цели вызовов: −0x3ba8c40
- инструкций: 1386 → 1401
```diff
@@ -149,8 +149,8 @@
 cmp eax, -1
 je L
+mov rcx, qword ptr [D]
+test rcx, rcx
+je L
 cmp eax, -2
-mov rcx, qword ptr [D]
-je L
-test rcx, rcx
 je L
 mov rdx, rax
@@ -196,11 +196,26 @@
 cmp r14, r13
 je L
+nop dword ptr [rax]
 mov eax, dword ptr [r13]
-mov rdi, qword ptr [rbp - 0x2f0]
-mov dword ptr [rbp - 0x220], eax
-call F
-test rax, rax
-je L
-mov r15, qword ptr [rax]
+cmp eax, -1
+je L
+cmp eax, -2
+mov rcx, qword ptr [D]
+je L
+test rcx, rcx
+je L
+mov rdx, rax
+shr rdx, 9
+and edx, 0x3f
+mov rdx, qword ptr [rcx + rdx*8]
+test rdx, rdx
+je L
+mov ecx, eax
+and ecx, 0x1ff
+imul rcx, rcx, 0x70
+add rdx, rcx
+cmp eax, dword ptr [rdx + 0x10]
+jne L
+mov r15, qword ptr [rdx]
 test r15, r15
 je L
@@ -225,4 +240,5 @@
 mov dword ptr [rbp - 0x150], 0
 jbe L
+nop dword ptr [rax]
 mov rax, qword ptr [r10 + 0x10]
 test rax, rax
@@ -336,8 +352,8 @@
 cmp ecx, -1
 je L
+cmp ecx, -2
 mov rsi, qword ptr [D]
+je L
 test rsi, rsi
-je L
-cmp ecx, -2
 je L
 movzx eax, word ptr [rax]
@@ -1123,5 +1139,4 @@
 jne L
 jmp L
-nop
 mov qword ptr [rbp - 0x318], r10
 mov rdi, r15
@@ -1130,5 +1145,5 @@
 test al, al
 je L
-nop dword ptr [rax + rax]
+nop word ptr [rax + rax]
 lea rax, [D]
 mov qword ptr [rbp - 0x318], r10
@@ -1357,4 +1372,6 @@
 movsxd rax, dword ptr [rbp - 0x150]
 jmp L
+movss xmm0, dword ptr [r12 + 0x864]
+jmp L
 mov rsi, qword ptr [rbp - 0x148]
 test rsi, rsi
@@ -1371,6 +1388,4 @@
 jne L
 jmp L
-movss xmm0, dword ptr [r12 + 0x864]
-jmp L
 mov qword ptr [rbp - 0x2f0], r10
 mov rdi, r15
```

### изменена: 0x5c02fb0 (857 байт) | строки: "m_eCategory"; "Double-save to Member '%s'"; "m_unActionID"; "m_strLocName"
было: 0x5c02f70 (842 байт)
- числа в инструкциях: +0 +0 +0
- поля объектов: +0x140 +0x148
- цели вызовов: −0x5bf0720
- инструкций: 201 → 209
```diff
@@ -4,6 +4,6 @@
 push r14
 push r13
+mov r13, rdi
 push r12
-mov r12, rdi
 push rbx
 mov rbx, rsi
@@ -28,5 +28,5 @@
 call F
 test rax, rax
-mov r13, rax
+mov r12, rax
 je L
 lea rdx, [S:"m_eCategory"]
@@ -35,5 +35,5 @@
 lea rsi, [S:"Double-save to Member '%s'"]
 call F
-mov esi, dword ptr [r12]
+mov esi, dword ptr [r13]
 lea rdi, [D]
 movabs rax, 0xc000000800000000
@@ -64,5 +64,5 @@
 jne L
 mov edx, 0x1b
-mov rdi, r13
+mov rdi, r12
 call F
 xor esi, esi
@@ -88,5 +88,5 @@
 call F
 test rax, rax
-mov r13, rax
+mov r12, rax
 je L
 lea rdx, [S:"m_unActionID"]
@@ -95,22 +95,31 @@
 lea rsi, [S:"Double-save to Member '%s'"]
 call F
-mov r14d, dword ptr [r12 + 4]
+mov r14d, dword ptr [r13 + 4]
 sub rsp, 8
 mov edx, 0x16
-xor ecx, ecx
+xor r9d, r9d
 push 0
-xor r9d, r9d
 xor r8d, r8d
+xor ecx, ecx
 mov esi, 4
-mov rdi, r13
+mov rdi, r12
 call F
 mov eax, r14d
-mov qword ptr [r13 + 8], rax
+mov qword ptr [r12 + 8], rax
 pop rax
 pop rdx
-mov rdi, rbx
-lea rsi, [r12 + 8]
+cmp qword ptr [rbx + 0x140], 0
+je L
+xor esi, esi
+mov rdi, rbx
 call F
 test al, al
+je L
+cmp byte ptr [rbx + 0x148], 0
+jne L
+mov rax, qword ptr [r13 + 8]
+test rax, rax
+je L
+cmp byte ptr [rax], 0
 jne L
 lea rsp, [rbp - 0x28]
@@ -122,23 +131,5 @@
 pop rbp
 ret
-nop dword ptr [rax]
-mov rdi, qword ptr [rbx + 0x120]
-lea rax, [S:"m_eCategory"]
-mov rsi, r14
-mov qword ptr [rbp - 0x40], r15
-mov qword ptr [rbp - 0x38], rax
-call F
-mov r13, rax
-jmp L
 nop
-mov rdi, qword ptr [rbx + 0x120]
-lea rax, [S:"m_unActionID"]
-mov rsi, r14
-mov qword ptr [rbp - 0x40], r15
-mov qword ptr [rbp - 0x38], rax
-call F
-mov r13, rax
-jmp L
-nop word ptr cs:[rax + rax]
 mov rdi, qword ptr [rbx + 0x120]
 lea r14, [rbp - 0x40]
@@ -152,5 +143,5 @@
 call F
 test rax, rax
-mov r13, rax
+mov r12, rax
 je L
 lea rdx, [S:"m_strLocName"]
@@ -159,7 +150,7 @@
 lea rsi, [S:"Double-save to Member '%s'"]
 call F
-mov rsi, qword ptr [r12 + 8]
+mov rsi, qword ptr [r13 + 8]
 lea rax, [D]
-mov rdi, r13
+mov rdi, r12
 mov edx, 0x1b
 test rsi, rsi
@@ -174,5 +165,23 @@
 jmp F
 nop dword ptr [rax]
-movsxd r15, dword ptr [r12]
```
(ещё 53 строк диффа: so-query.py fdiff libserver.so 0x5c02fb0)

### изменена: 0x5c20980 (3649 байт) | строки: "npc_dota_hero_razor"; "modifier_disable_taunt_animation_cancel"
было: 0x5c20940 (3633 байт)
- числа в инструкциях: +0x5df
- виртуальные вызовы: −0xdc0 (слот 440)
- поля объектов: +0xdc0
- прямых вызовов: 80 → 81
- цели вызовов: +0x44209b0
- инструкций: 779 → 782
```diff
@@ -448,16 +448,14 @@
 call qword ptr [rax + 0xe30]
 lea rsi, [S:"npc_dota_hero_razor"]
-cmp rax, rsi
-je L
-test rax, rax
-je L
 mov rdi, rax
 call F
-test eax, eax
-jne L
-mov rax, qword ptr [r12]
+mov edx, eax
+mov rax, qword ptr [r12]
+test dl, dl
+mov rax, qword ptr [rax + 0xdc0]
+je L
 mov esi, 0x5df
 mov rdi, r12
-call qword ptr [rax + 0xdc0]
+call rax
 mov esi, 0x5df
 mov rdi, r12
@@ -530,5 +528,5 @@
 pop rbp
 jmp F
-nop dword ptr [rax]
+nop dword ptr [rax + rax]
 mov rdi, r13
 call F
@@ -540,4 +538,5 @@
 movss dword ptr [rbx + 0x10], xmm0
 jmp L
+nop dword ptr [rax + rax]
 mov rbx, qword ptr [rbp - 0x140]
 mov rdi, rbx
@@ -567,5 +566,10 @@
 mov esi, 0x5dc
 call F
-jmp L
+mov rax, qword ptr [r12]
+mov esi, 0x5df
+mov rdi, r12
+call qword ptr [rax + 0xdc0]
+jmp L
+nop word ptr [rax + rax]
 mov rdi, qword ptr [rbp - 0x148]
 mov rax, qword ptr [rdi]
@@ -735,8 +739,7 @@
 mov qword ptr [rsi + 8], rdx
 jmp L
-mov rax, qword ptr [r12]
 mov esi, 0x5de
 mov rdi, r12
-call qword ptr [rax + 0xdc0]
+call rax
 mov esi, 0x5de
 mov rdi, r12
```

### изменена: 0x5c22a60 (776 байт) вызывается из: CDOTA_BaseNPC::vfunc#519, CDOTA_BaseNPC::vfunc#458
было: 0x5c22a10 (698 байт)
- числа в инструкциях: +1 +0x5dc −0
- поля объектов: +0xa98 +0x1788 +0xb4 +0xb4 +0xaa0 +0x1790 −0x268 −0xb1
- прямых вызовов: 14 → 16
- цели вызовов: +0x5cb4f40 +CDOTA_BaseNPC::vfunc#340 +0x604d850 −0x5cb84b0 −CDOTALocomotor::vfunc#77
- инструкций: 142 → 159
```diff
@@ -1,8 +1,9 @@
 push rbp
 mov rbp, rsp
+push r14
 push r12
 push rbx
 mov rbx, rdi
-sub rsp, 0x130
+sub rsp, 0x138
 cmp byte ptr [rdi + 0xa0], 0
 jne L
@@ -21,4 +22,5 @@
 mov rdi, r12
 call F
+lea r12, [T]
 mov rdi, rbx
 call F
@@ -26,12 +28,23 @@
 xor edx, edx
 xor esi, esi
+movq xmm0, qword ptr [K:0x0000000000000000]
 movss xmm1, dword ptr [K:0]
-movq xmm0, qword ptr [K:0x0000000000000000]
 call F
-mov rdi, qword ptr [rbx + 0x10]
+mov rdi, qword ptr [rbx + 8]
 mov eax, 1
 movd xmm0, eax
 pshufd xmm0, xmm0, 0
 movups xmmword ptr [rbx + 0x30], xmm0
+mov rax, qword ptr [rdi]
+mov rax, qword ptr [rax + 0xa98]
+cmp rax, r12
+jne L
+mov rdi, qword ptr [rdi + 0x1788]
+movss xmm2, dword ptr [rdi + 0xb4]
+movd r14d, xmm2
+xor esi, esi
+call F
+mov rdi, qword ptr [rbx + 0x10]
+movd xmm0, r14d
 call F
 mov rdi, qword ptr [rbx + 0x18]
@@ -40,87 +53,83 @@
 call F
 mov rax, qword ptr [rbx + 0x28]
+mov edx, 0xffffffff
+movabs rcx, 0xffffffff00000000
+mov qword ptr [rax + 0x18], rdx
 lea rdx, [T]
-movabs rcx, 0xffffffff00000000
+mov qword ptr [rax + 8], 0
 mov qword ptr [rax + 0x10], rcx
-mov ecx, 0xffffffff
-mov qword ptr [rax + 8], 0
-mov qword ptr [rax + 0x18], rcx
 mov qword ptr [rax + 0x20], 0
 mov rdi, qword ptr [rbx + 8]
 mov rax, qword ptr [rdi]
-mov rax, qword ptr [rax + 0xa98]
+mov rax, qword ptr [rax + 0xaa0]
 cmp rax, rdx
 jne L
-mov rbx, qword ptr [rdi + 0x1788]
-mov rax, qword ptr [rbx]
-lea rdx, [T]
-mov rax, qword ptr [rax + 0x268]
-cmp rax, rdx
-jne L
-xor esi, esi
-mov rdi, rbx
-call F
-mov byte ptr [rbx + 0xb1], 0
-add rsp, 0x130
+mov rdi, qword ptr [rdi + 0x1790]
+add rsp, 0x138
+xor ecx, ecx
+mov edx, 1
 pop rbx
+mov esi, 0x5dc
 pop r12
+pop r14
 pop rbp
-ret
-nop dword ptr [rax + rax]
+jmp F
+nop
 movq xmm0, qword ptr [D]
 lea rax, [T]
-mov qword ptr [rbp - 0x138], 0
-movq xmm2, rax
-mov qword ptr [rbp - 0x140], rbx
+mov qword ptr [rbp - 0x148], 0
+movq xmm3, rax
+mov qword ptr [rbp - 0x150], rbx
 lea rdi, [rbx + 0xa8]
-punpcklqdq xmm0, xmm2
+punpcklqdq xmm0, xmm3
+movaps xmmword ptr [rbp - 0x140], xmm0
+call F
+mov rcx, qword ptr [rbp - 0x140]
+mov qword ptr [rbp - 0x130], 0
+mov rdx, qword ptr [rbp - 0x138]
+mov qword ptr [rbp - 0x128], 0
+mov qword ptr [rbp - 0x120], 0
+test rcx, rcx
+mov qword ptr [rbp - 0x118], rdx
+je L
+movdqa xmm0, xmmword ptr [rbp - 0x150]
+mov qword ptr [rbp - 0x120], rcx
 movaps xmmword ptr [rbp - 0x130], xmm0
-call F
+pxor xmm0, xmm0
+movaps xmmword ptr [rbp - 0x140], xmm0
 mov rcx, qword ptr [rbp - 0x130]
-mov qword ptr [rbp - 0x120], 0
-mov rdx, qword ptr [rbp - 0x128]
-mov qword ptr [rbp - 0x118], 0
-mov qword ptr [rbp - 0x110], 0
-test rcx, rcx
```
(ещё 84 строк диффа: so-query.py fdiff libserver.so 0x5c22a60)

### изменена: 0x5c7d340 (11035 байт) CDOTA_Item_BotChallenge_MeteorStaff::Spawn, CDOTA_Item_Mask_Spin_Crit::Spawn, CDOTA_Item_Mask_Crit_Lifesteal::Spawn | строки: "<NoAbilityName>"; "ItemBaseLevel"; "ItemCombinable"; "ItemPermanent"; "ItemStackable"; "ItemStackableMax"; "ItemRecipe"; "ItemRecipeConsumesCharges"
было: 0x5c7d280 (11030 байт)
- цели вызовов: +0x44209b0
- инструкций: 1917 → 1918
```diff
@@ -374,4 +374,10 @@
 test rax, rax
 jne L
+lea rsi, [S:"ITEM_FULLY_SHAREABLE_STACKING"]
+mov rdi, r15
+call F
+test al, al
+jne L
+nop dword ptr [rax]
 mov dword ptr [rbx + 0x8d4], 0
 lea rsi, [S:"ItemDeclarations"]
@@ -421,5 +427,5 @@
 pop rbp
 ret
-nop dword ptr [rax]
+nop word ptr [rax + rax]
 xor edi, edi
 mov esi, 1
@@ -1264,14 +1270,7 @@
 call F
 test eax, eax
-je L
-lea rsi, [S:"ITEM_FULLY_SHAREABLE_STACKING"]
-cmp r15, rsi
-je L
-mov rdi, r15
-call F
-test eax, eax
-jne L
-mov r8d, dword ptr [rbx + 0x870]
-test r8d, r8d
+jne L
+mov r9d, dword ptr [rbx + 0x870]
+test r9d, r9d
 je L
 mov edx, 0xffffffff
@@ -1280,5 +1279,4 @@
 call F
 mov dword ptr [rbx + 0x870], 0
-mov byte ptr [rbx + 0x8d0], 1
 jmp L
 nop
@@ -1311,29 +1309,29 @@
 jmp L
 nop dword ptr [rax + rax]
-xor ecx, ecx
-mov esi, 1
+lea rdi, [rbp - 0x170]
+xor esi, esi
 pxor xmm0, xmm0
 mov qword ptr [rbp - 0x180], 1
-lea rdi, [rbp - 0x170]
+mov word ptr [rbp - 0x144], si
+mov esi, 1
+movaps xmmword ptr [rbp - 0x160], xmm0
+lea r14, [rbp - 0x180]
 mov qword ptr [rbp - 0x178], 0
-movaps xmmword ptr [rbp - 0x160], xmm0
-lea r12, [rbp - 0x180]
 mov qword ptr [rbp - 0x170], 0
 mov qword ptr [rbp - 0x168], 0
 mov qword ptr [rbp - 0x150], 0xffffffffffffffff
 mov dword ptr [rbp - 0x148], 0xffffffff
-mov word ptr [rbp - 0x144], cx
 call F
 mov rax, qword ptr [rbp - 0x170]
 lea rdx, [T]
 add dword ptr [rbp - 0x178], 1
-mov dword ptr [rax], 0x87a
+mov dword ptr [rax], 0x87c
 mov rax, qword ptr [rbx]
 mov rax, qword ptr [rax + 0xf0]
 cmp rax, rdx
 jne L
-mov edx, dword ptr [rbp - 0x180]
-lea r15, [rbx + 0x38]
-test edx, edx
+mov ecx, dword ptr [rbp - 0x180]
+lea r9, [rbx + 0x38]
+test ecx, ecx
 jne L
 cmp byte ptr [rbx + 0x318], 0
@@ -1361,32 +1359,34 @@
 mov rax, qword ptr [rdi]
 call qword ptr [rax + 0x20]
-mov byte ptr [rbx + 0x87a], 0
-jmp L
-nop word ptr [rax + rax]
+cmp byte ptr [rbx + 0x87d], 0
+mov byte ptr [rbx + 0x87c], 1
+je L
+jmp L
+nop
+xor ecx, ecx
+mov esi, 1
+pxor xmm0, xmm0
+mov qword ptr [rbp - 0x180], 1
 lea rdi, [rbp - 0x170]
-xor esi, esi
-pxor xmm0, xmm0
-mov qword ptr [rbp - 0x180], 1
-mov word ptr [rbp - 0x144], si
-mov esi, 1
+mov qword ptr [rbp - 0x178], 0
 movaps xmmword ptr [rbp - 0x160], xmm0
-lea r14, [rbp - 0x180]
-mov qword ptr [rbp - 0x178], 0
+lea r12, [rbp - 0x180]
 mov qword ptr [rbp - 0x170], 0
 mov qword ptr [rbp - 0x168], 0
 mov qword ptr [rbp - 0x150], 0xffffffffffffffff
 mov dword ptr [rbp - 0x148], 0xffffffff
+mov word ptr [rbp - 0x144], cx
 call F
 mov rax, qword ptr [rbp - 0x170]
 lea rdx, [T]
 add dword ptr [rbp - 0x178], 1
-mov dword ptr [rax], 0x87c
+mov dword ptr [rax], 0x87a
 mov rax, qword ptr [rbx]
```
(ещё 296 строк диффа: so-query.py fdiff libserver.so 0x5c7d340)


## Строки библиотек

