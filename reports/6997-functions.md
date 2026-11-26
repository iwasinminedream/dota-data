# Dota 6997: изменения кода по функциям и строки библиотек

Снимки `6996-11274611` → `6997-11278692`; funcdiff.py. В диффе: [S:…] — строка, [K:…] — константа из данных, F — вызов другой функции, L — переход внутри функции, [D]/[T] — прочие адреса. Регистры и смещения стека меняются и от перекомпиляции. Здесь всё, в том числе игровые функции и изменения от пересборки.

## libclient.so: функций 281894 → 281894; без изменений 281894, изменено 0, добавлено 0, удалено 0

## libserver.so: функций 221948 → 221947; без изменений 221931, изменено 14, добавлено 1, удалено 0

### изменена: 0x44e68c0 (749 байт) CDOTA_Modifier_Nevermore_FeastOfSouls_Collection::OnDestroy | строки: "modifier_nevermore_necromastery"; "particles/units/heroes/hero_nevermore/nevermore_necro_souls.vpcf"; "attach_hitloc"; "linger_duration"; "modifier_nevermore_feast_of_souls_linger"
было: 0x44e68c0 (725 байт)
- числа в инструкциях: −0 −0
- инструкций: 188 → 191
```diff
@@ -7,5 +7,5 @@
 push rbx
 mov rbx, rdi
-sub rsp, 0x28
+sub rsp, 0x38
 call F
 test rax, rax
@@ -18,14 +18,14 @@
 call F
 test rax, rax
-mov r14, rax
+mov qword ptr [rbp - 0x50], rax
 je L
 mov esi, dword ptr [rbx + 0x1b20]
 test esi, esi
 jle L
+xor r12d, r12d
 xor r15d, r15d
-mov byte ptr [rbp - 0x45], 0
 nop dword ptr [rax]
 mov rax, qword ptr [rbx + 0x1b28]
-lea rax, [rax + r15*4]
+lea rax, [rax + r12*4]
 mov ecx, dword ptr [rax]
 cmp ecx, -1
@@ -48,22 +48,23 @@
 cmp ecx, dword ptr [rax + 0x10]
 jne L
-mov r12, qword ptr [rax]
-test r12, r12
+mov r14, qword ptr [rax]
+test r14, r14
 je L
-cmp byte ptr [r12 + 0x5d1], 3
+cmp byte ptr [r14 + 0x5d1], 3
 jne L
-mov rax, qword ptr [r12]
-mov rdi, r12
+mov rax, qword ptr [r14]
+mov rdi, r14
 call qword ptr [rax + 0x538]
 test al, al
 je L
-mov rax, qword ptr [r14]
-test byte ptr [r12 + 0xd3c], 1
+mov rax, qword ptr [rbp - 0x50]
+test byte ptr [r14 + 0xd3c], 1
+mov rax, qword ptr [rax]
 mov rax, qword ptr [rax + 0x1b0]
 je L
-cmp byte ptr [r12 + 0x175a], 0
+cmp byte ptr [r14 + 0x175a], 0
 je L
 mov esi, dword ptr [rbx + 0x1b0c]
-mov rdi, r14
+mov rdi, qword ptr [rbp - 0x50]
 call rax
 mov rdi, rbx
@@ -78,5 +79,5 @@
 call F
 mov rdi, rbx
-mov qword ptr [rbp - 0x50], rax
+mov qword ptr [rbp - 0x58], rax
 call F
 mov rdi, rax
@@ -94,11 +95,11 @@
 mov esi, dword ptr [rbp - 0x44]
 lea r9, [S:"attach_hitloc"]
-mov rdi, qword ptr [rbp - 0x50]
+mov rdi, qword ptr [rbp - 0x58]
 call F
 call F
-mov rdi, r12
+mov rdi, r14
 mov r13, rax
 call F
-mov rcx, r12
+mov rcx, r14
 mov edx, 1
 mov rdi, r13
@@ -109,10 +110,10 @@
 push 0
 push 1
-mov r12d, dword ptr [rbp - 0x44]
-mov esi, r12d
+mov r14d, dword ptr [rbp - 0x44]
+mov esi, r14d
 call F
 add rsp, 0x18
 xor edx, edx
-mov esi, r12d
+mov esi, r14d
 push 0
 xor r9d, r9d
@@ -124,8 +125,8 @@
 mov esi, dword ptr [rbx + 0x1b20]
 pop rdx
-add r15, 1
-cmp esi, r15d
+add r12, 1
+cmp esi, r12d
 jg L
-cmp byte ptr [rbp - 0x45], 0
+test r15b, r15b
 jne L
 lea rsp, [rbp - 0x28]
@@ -139,11 +140,13 @@
 nop dword ptr [rax]
 mov esi, dword ptr [rbx + 0x1b20]
-mov byte ptr [rbp - 0x45], 1
+nop word ptr cs:[rax + rax]
+mov r15d, 1
+jmp L
+nop dword ptr [rax + rax]
+mov esi, dword ptr [rbx + 0x1b08]
+mov rdi, qword ptr [rbp - 0x50]
+call rax
 jmp L
 nop dword ptr [rax]
-mov esi, dword ptr [rbx + 0x1b08]
```
(ещё 5 строк диффа: so-query.py fdiff libserver.so 0x44e68c0)

### изменена: 0x47919a0 (4687 байт) вызывается из: CDOTA_Modifier_Warlock_Rain_Of_Chaos_Thinker::OnIntervalThink | строки: "stun_duration"; "golem_duration"; "leash_radius"; "modifier_stunned"; "duration"; "npc_dota_warlock_golem"; "golem_hp"; "golem_dmg"
было: 0x47919a0 (4674 байт)
- поля объектов: +0xd78
- инструкций: 870 → 874
```diff
@@ -218,13 +218,13 @@
 xor edx, edx
 mov rdi, r13
-lea rbx, [S:"golem_dmg"]
-call F
-mov rsi, rbx
-xor edx, edx
-mov rdi, r13
-movss xmm0, dword ptr [K:-1]
-mov dword ptr [rbp - 0x1b8], eax
-call F
-mov rsi, rbx
+lea r14, [S:"golem_dmg"]
+call F
+mov rsi, r14
+xor edx, edx
+mov rdi, r13
+movss xmm0, dword ptr [K:-1]
+mov ebx, eax
+call F
+mov rsi, r14
 xor edx, edx
 mov rdi, r13
@@ -237,32 +237,35 @@
 lea rsi, [S:"golem_gold_bounty"]
 add eax, 0xa
+mov dword ptr [rbp - 0x1cc], eax
+call F
+mov r14d, eax
+movss xmm0, dword ptr [K:-1]
+lea rsi, [S:"golem_movement_speed"]
+xor edx, edx
+mov rdi, r13
+call F
+movss xmm0, dword ptr [K:-1]
+xor edx, edx
+mov rdi, r13
+lea rsi, [S:"golem_armor"]
 mov dword ptr [rbp - 0x1d8], eax
 call F
-mov ebx, eax
-movss xmm0, dword ptr [K:-1]
-lea rsi, [S:"golem_movement_speed"]
-xor edx, edx
-mov rdi, r13
-call F
-movss xmm0, dword ptr [K:-1]
-xor edx, edx
-mov rdi, r13
-lea rsi, [S:"golem_armor"]
-mov r14d, eax
-call F
-xor edx, edx
-mov rdi, r13
+xor edx, edx
+mov rdi, r13
+movss dword ptr [rbp - 0x1b8], xmm0
+movss xmm0, dword ptr [K:-1]
+lea rsi, [S:"golem_health_regen"]
+call F
+mov esi, ebx
+mov rdi, r12
 movss dword ptr [rbp - 0x1c8], xmm0
-movss xmm0, dword ptr [K:-1]
-lea rsi, [S:"golem_health_regen"]
-call F
-mov esi, dword ptr [rbp - 0x1b8]
-mov rdi, r12
-movss dword ptr [rbp - 0x1cc], xmm0
-call F
-mov esi, dword ptr [rbp - 0x1b8]
+pxor xmm0, xmm0
+cvtsi2ss xmm0, ebx
+movss dword ptr [r12 + 0xd78], xmm0
+call F
 xor r8d, r8d
 xor ecx, ecx
 xor edx, edx
+mov esi, ebx
 mov rdi, r12
 call F
@@ -292,6 +295,6 @@
 call F
 mov dword ptr [r12 + 0xfbc], r15d
-mov r15d, dword ptr [rbp - 0x1d8]
-cmp r15d, dword ptr [r12 + 0xfc0]
+mov ebx, dword ptr [rbp - 0x1cc]
+cmp ebx, dword ptr [r12 + 0xfc0]
 je L
 xor eax, eax
@@ -317,6 +320,7 @@
 lea rdi, [rbp - 0x138]
 call F
-mov dword ptr [r12 + 0xfc0], r15d
-cmp r14d, dword ptr [r12 + 0xfcc]
+mov dword ptr [r12 + 0xfc0], ebx
+mov ebx, dword ptr [rbp - 0x1d8]
+cmp ebx, dword ptr [r12 + 0xfcc]
 je L
 lea rdi, [rbp - 0x130]
@@ -342,10 +346,10 @@
 lea rdi, [rbp - 0x138]
 call F
-mov dword ptr [r12 + 0xfcc], r14d
-cmp ebx, dword ptr [r12 + 0x1078]
+mov dword ptr [r12 + 0xfcc], ebx
+cmp r14d, dword ptr [r12 + 0x1078]
 je L
 lea rdi, [rbp - 0x130]
 mov esi, 1
-xor r14d, r14d
+xor ebx, ebx
 pxor xmm0, xmm0
 mov qword ptr [rbp - 0x140], 1
@@ -356,5 +360,5 @@
 mov qword ptr [rbp - 0x110], 0xffffffffffffffff
 mov dword ptr [rbp - 0x108], 0xffffffff
-mov word ptr [rbp - 0x104], r14w
+mov word ptr [rbp - 0x104], bx
 call F
```
(ещё 102 строк диффа: so-query.py fdiff libserver.so 0x47919a0)

### изменена: 0x542c5d0 (1402 байт) вызывается из: CDOTA_Modifier_BigThunderLizard_Slam_Thinker::OnCreated, CDOTA_Modifier_BigThunderLizard_Slam_Thinker::OnIntervalThink | строки: "particles/neutral_fx/ursa_thunderclap.vpcf"; "n_creep_Thunderlizard_Big.Stomp"; "modifier_beastmaster_thunderhide_bonus_damage"; "duration"; "thunderhide_slam_duration"; "modifier_big_thunder_lizard_slam"; "modifier_beastmaster_thunderhide_drum"; "max_stacks"
было: 0x542c5d0 (1398 байт)
- строки: +"duration" −"non_hero_duration" −"hero_duration"
- инструкций: 303 → 298
```diff
@@ -13,6 +13,6 @@
 addss xmm0, dword ptr [rdi + 0x1af8]
 movsldup xmm4, xmm0
-movss dword ptr [rbp - 0x118], xmm0
-movlps qword ptr [rbp - 0x120], xmm4
+movss dword ptr [rbp - 0x120], xmm0
+movlps qword ptr [rbp - 0x128], xmm4
 call F
 mov rdi, rbx
@@ -27,19 +27,18 @@
 movzx r14d, byte ptr [rax + 0x624]
 call F
+mov rdx, r12
+mov r9d, 2
 mov rcx, r13
-mov rdx, r12
 mov qword ptr [rbp - 0xf0], 0
+lea r8, [rbp - 0xf0]
+mov rdi, rax
 mov qword ptr [rbp - 0xe8], 0
-mov rdi, rax
-mov r9d, 2
 mov qword ptr [rbp - 0xe0], 0
-lea r8, [rbp - 0xf0]
-push 0
-lea r13, [rbp - 0xd0]
 mov esi, r14d
 push 0
 push 0
+push 0
 push 3
-movss xmm0, dword ptr [rbp - 0x118]
+movss xmm0, dword ptr [rbp - 0x120]
 call F
 mov eax, dword ptr [rbp - 0xdc]
@@ -47,5 +46,5 @@
 movsxd r15, dword ptr [rbp - 0xf0]
 mov r12, qword ptr [rbp - 0xe8]
-mov dword ptr [rbp - 0x130], eax
+mov dword ptr [rbp - 0x134], eax
 call F
 mov rdi, rbx
@@ -54,5 +53,5 @@
 movaps xmm0, xmmword ptr [K:-1,-1,3.402823e+38,3.402823e+38]
 mov rdi, r14
-mov rsi, r13
+mov dword ptr [rbp - 0xc8], 0
 mov qword ptr [rbp - 0xc0], rax
 xor eax, eax
@@ -61,15 +60,16 @@
 lea rcx, [S:"particles/neutral_fx/ursa_thunderclap.vpcf"]
 mov qword ptr [rbp - 0xd0], rcx
-mov dword ptr [rbp - 0xc8], 0
 mov qword ptr [rbp - 0xb8], 0
 mov qword ptr [rbp - 0xb0], 0
+mov qword ptr [rbp - 0x70], rax
+lea rax, [rbp - 0xd0]
+mov rsi, rax
+mov byte ptr [rbp - 0x96], 0
 mov dword ptr [rbp - 0xa8], 0
 mov qword ptr [rbp - 0xa0], 0
-mov byte ptr [rbp - 0x96], 0
 movlps qword ptr [rbp - 0x94], xmm0
 movhps qword ptr [rbp - 0x8c], xmm0
 mov qword ptr [rbp - 0x84], 0x7f7fffff
 mov qword ptr [rbp - 0x78], 0
-mov qword ptr [rbp - 0x70], rax
 mov qword ptr [rbp - 0x68], 0
 mov qword ptr [rbp - 0x60], 0
@@ -78,4 +78,5 @@
 movhps qword ptr [rbp - 0x48], xmm0
 mov dword ptr [rbp - 0x40], 0x7f7fffff
+mov qword ptr [rbp - 0x118], rax
 call F
 mov r14d, eax
@@ -88,11 +89,11 @@
 call rax
 call F
-mov rcx, r13
+mov rcx, qword ptr [rbp - 0x118]
 mov edx, 1
 mov esi, r14d
 mov rdi, rax
-mov rax, qword ptr [rbp - 0x120]
+mov rax, qword ptr [rbp - 0x128]
 pxor xmm0, xmm0
-movss xmm5, dword ptr [rbp - 0x118]
+movss xmm5, dword ptr [rbp - 0x120]
 movss dword ptr [rbp - 0xc8], xmm5
 mov qword ptr [rbp - 0xd0], rax
@@ -123,12 +124,11 @@
 test r15d, r15d
 jle L
+mov r13, r12
+xor r14d, r14d
+mov qword ptr [rbp - 0x130], rdi
 lea r15, [r12 + r15*4]
-xor ecx, ecx
-mov r14, r12
-mov qword ptr [rbp - 0x128], rdi
-mov byte ptr [rbp - 0x129], cl
-mov qword ptr [rbp - 0x138], r12
-nop dword ptr [rax]
-mov ecx, dword ptr [r14]
+mov qword ptr [rbp - 0x140], r12
+nop word ptr [rax + rax]
+mov ecx, dword ptr [r13]
 cmp ecx, -1
 je L
@@ -138,5 +138,5 @@
 cmp ecx, -2
 je L
-movzx eax, word ptr [r14]
+movzx eax, word ptr [r13]
 mov rdx, rax
 shr rdx, 9
@@ -156,17 +156,13 @@
 jne L
 mov eax, dword ptr [r12 + 0xd3c]
-lea rsi, [S:"non_hero_duration"]
```
(ещё 116 строк диффа: so-query.py fdiff libserver.so 0x542c5d0)

### изменена: 0x5cb2bc0 (1220 байт) вызывается из: CDOTAPlayerController::vfunc#255 | строки: "none"
было: 0x5cb2c20 (1204 байт)
- строки: +"none"
- инструкций: 271 → 274
```diff
@@ -180,8 +180,11 @@
 test al, al
 je L
-mov rcx, qword ptr [rbp - 0x90]
 mov rax, qword ptr [rbp - 0x88]
+lea r15, [S:"none"]
+mov rcx, qword ptr [rbp - 0x90]
+test rax, rax
+je L
+mov r15, qword ptr [rax + 0x28]
 mov r14, qword ptr [rcx + 0x10]
-mov r15, qword ptr [rax + 0x28]
 lea rax, [D]
 test r14, r14
@@ -230,5 +233,5 @@
 je L
 jmp L
-nop
+nop word ptr cs:[rax + rax]
 call F
 test al, al
```

### изменена: 0x5cba9a0 (5084 байт) вызывается из: CDOTA_PlayerResource::vfunc#237
было: 0x5cba9e0 (5180 байт)
- числа в инструкциях: −0
- поля объектов: −0x2c
- прямых вызовов: 74 → 73
- инструкций: 1068 → 1051
```diff
@@ -454,4 +454,5 @@
 mov dword ptr [rbp - 0x3c], esi
 mov esi, 1
+movaps xmmword ptr [rbp - 0x50], xmm6
 mov word ptr [rbp - 0x34], r8w
 mov qword ptr [rbp - 0x70], 1
@@ -459,20 +460,14 @@
 mov qword ptr [rbp - 0x60], 0
 mov qword ptr [rbp - 0x58], 0
-movaps xmmword ptr [rbp - 0x50], xmm6
 mov dword ptr [rbp - 0x38], 0xffffffff
 call F
 mov rsi, qword ptr [rbp - 0x60]
-lea rax, [T]
-add dword ptr [rbp - 0x68], 1
-mov rcx, qword ptr [rbp - 0x148]
+mov rdi, r13
+add dword ptr [rbp - 0x68], 1
 mov dword ptr [rsi], 0x3a4
-mov rsi, qword ptr [r13]
-mov r8, qword ptr [rsi + 8]
-cmp r8, rax
-jne L
-cmp byte ptr [r13 + 0x2c], 0
-jne L
+mov r8, qword ptr [r13]
+mov rsi, qword ptr [rbp - 0x140]
+call qword ptr [r8 + 8]
 lea rdi, [rbp - 0x68]
-mov qword ptr [rbp - 0x148], rcx
 call F
 mov rcx, qword ptr [rbp - 0x148]
@@ -554,10 +549,4 @@
 jmp L
 nop dword ptr [rax]
-mov rsi, qword ptr [rbp - 0x140]
-lea rdi, [r13 + 8]
-call F
-mov rcx, qword ptr [rbp - 0x148]
-jmp L
-nop dword ptr [rax]
 lea rdi, [r13 + 8]
 mov rsi, rbx
@@ -565,10 +554,4 @@
 jmp L
 nop word ptr cs:[rax + rax]
-mov qword ptr [rbp - 0x148], rcx
-mov rsi, qword ptr [rbp - 0x140]
-mov rdi, r13
-call r8
-mov rcx, qword ptr [rbp - 0x148]
-jmp L
 mov r10, qword ptr [rbp - 0x138]
 mov ebx, dword ptr [rbp - 0x130]
```

### изменена: 0x5cdf9c0 (1378 байт) | строки: "item_tpscroll"; "ItemPurchasable"; "item_enchanted_mango"; "item_faerie_fire"
было: 0x5cdfa80 (1362 байт)
- числа в инструкциях: +1 +1 +1 +1
- инструкций: 304 → 306
```diff
@@ -7,5 +7,5 @@
 push rbx
 mov ebx, edi
-sub rsp, 0x58
+sub rsp, 0x48
 mov rdi, qword ptr [D]
 test rdi, rdi
@@ -116,13 +116,11 @@
 cmp byte ptr [r13 + 0x8f0], 0
 jne L
-lea r14, [rbp - 0x68]
+lea rdi, [rbp - 0x60]
 xor edx, edx
 pxor xmm0, xmm0
-mov dword ptr [rbp - 0x74], 0x8f0
-lea rsi, [rbp - 0x74]
-mov rdi, r14
+mov esi, 1
 movaps xmmword ptr [rbp - 0x50], xmm0
+lea r14, [rbp - 0x70]
 mov word ptr [rbp - 0x34], dx
-lea r15, [rbp - 0x70]
 mov qword ptr [rbp - 0x70], 1
 mov qword ptr [rbp - 0x68], 0
@@ -132,9 +130,12 @@
 mov dword ptr [rbp - 0x38], 0xffffffff
 call F
+mov rax, qword ptr [rbp - 0x60]
+mov rsi, r14
+mov rdi, r13
+add dword ptr [rbp - 0x68], 1
+mov dword ptr [rax], 0x8f0
 mov rax, qword ptr [r13]
-mov rsi, r15
-mov rdi, r13
 call qword ptr [rax + 0xf0]
-mov rdi, r14
+lea rdi, [rbp - 0x68]
 call F
 mov byte ptr [r13 + 0x8f0], 1
@@ -165,13 +166,11 @@
 cmp byte ptr [rbx + 0x8f0], 0
 jne L
-lea r12, [rbp - 0x68]
+lea rdi, [rbp - 0x60]
 xor eax, eax
 pxor xmm0, xmm0
-mov dword ptr [rbp - 0x74], 0x8f0
-lea rsi, [rbp - 0x74]
-mov rdi, r12
+mov esi, 1
 movaps xmmword ptr [rbp - 0x50], xmm0
+lea r12, [rbp - 0x70]
 mov word ptr [rbp - 0x34], ax
-lea r13, [rbp - 0x70]
 mov qword ptr [rbp - 0x70], 1
 mov qword ptr [rbp - 0x68], 0
@@ -181,9 +180,12 @@
 mov dword ptr [rbp - 0x38], 0xffffffff
 call F
+mov rax, qword ptr [rbp - 0x60]
+mov rsi, r12
+mov rdi, rbx
+add dword ptr [rbp - 0x68], 1
+mov dword ptr [rax], 0x8f0
 mov rax, qword ptr [rbx]
-mov rsi, r13
-mov rdi, rbx
 call qword ptr [rax + 0xf0]
-mov rdi, r12
+lea rdi, [rbp - 0x68]
 call F
 mov byte ptr [rbx + 0x8f0], 1
```

### изменена: 0x5d0e910 (3198 байт)
было: 0x5d0e9d0 (3157 байт)
- числа в инструкциях: +1 +1
- поля объектов: +0xf048 +0xf048 +0xf050 +0xf058
- инструкций: 669 → 679
```diff
@@ -120,10 +120,10 @@
 cmp qword ptr [r12 + 0x58], 1
 je L
-xor esi, esi
+xor edi, edi
+mov esi, 1
 pxor xmm0, xmm0
 mov qword ptr [rbp - 0x70], 1
-mov word ptr [rbp - 0x34], si
+mov word ptr [rbp - 0x34], di
 lea rdi, [rbp - 0x60]
-mov esi, 1
 mov qword ptr [rbp - 0x68], 0
 lea r15, [rbp - 0x70]
@@ -156,7 +156,5 @@
 test al, al
 jne L
-mov r15d, dword ptr [rbp - 0x78]
 test r14b, r14b
-mov dword ptr [rbp - 0x70], r15d
 jne L
 lea rax, [D]
@@ -166,7 +164,8 @@
 cmp al, 1
 je L
-test r15d, r15d
-jne L
-nop dword ptr [rax]
+mov eax, dword ptr [rbp - 0x78]
+test eax, eax
+jne L
+nop word ptr [rax + rax]
 call F
 mov esi, dword ptr [rbp - 0x74]
@@ -215,33 +214,4 @@
 nop word ptr [rax + rax]
 lea rdi, [rbp - 0x60]
-xor r8d, r8d
-pxor xmm0, xmm0
-mov esi, 1
-mov qword ptr [rbp - 0x70], 1
-lea r15, [rbp - 0x70]
-mov qword ptr [rbp - 0x68], 0
-mov qword ptr [rbp - 0x60], 0
-mov qword ptr [rbp - 0x58], 0
-movaps xmmword ptr [rbp - 0x50], xmm0
-mov qword ptr [rbp - 0x40], 0xffffffffffffffff
-mov dword ptr [rbp - 0x38], 0xffffffff
-mov word ptr [rbp - 0x34], r8w
-call F
-mov rax, qword ptr [rbp - 0x60]
-lea rdx, [T]
-add dword ptr [rbp - 0x68], 1
-mov dword ptr [rax], 0x58
-mov rax, qword ptr [r12]
-mov rax, qword ptr [rax + 8]
-cmp rax, rdx
-jne L
-cmp byte ptr [r12 + 0x2c], 0
-jne L
-lea rdi, [rbp - 0x68]
-call F
-mov qword ptr [r12 + 0x58], r13
-jmp L
-nop word ptr cs:[rax + rax]
-lea rdi, [rbp - 0x60]
 xor r9d, r9d
 pxor xmm0, xmm0
@@ -260,5 +230,5 @@
 lea rdx, [T]
 add dword ptr [rbp - 0x68], 1
-mov dword ptr [rax], 0x30
+mov dword ptr [rax], 0x58
 mov rax, qword ptr [r12]
 mov rax, qword ptr [rax + 8]
@@ -269,11 +239,9 @@
 lea rdi, [rbp - 0x68]
 call F
-cmp qword ptr [r12 + 0x58], r13
-mov byte ptr [r12 + 0x30], 1
-je L
-jmp L
-nop word ptr [rax + rax]
+mov qword ptr [r12 + 0x58], r13
+jmp L
+nop word ptr cs:[rax + rax]
 lea rdi, [rbp - 0x60]
-xor ecx, ecx
+xor r10d, r10d
 pxor xmm0, xmm0
 mov esi, 1
@@ -286,5 +254,36 @@
 mov qword ptr [rbp - 0x40], 0xffffffffffffffff
 mov dword ptr [rbp - 0x38], 0xffffffff
-mov word ptr [rbp - 0x34], cx
+mov word ptr [rbp - 0x34], r10w
+call F
+mov rax, qword ptr [rbp - 0x60]
+lea rdx, [T]
+add dword ptr [rbp - 0x68], 1
+mov dword ptr [rax], 0x30
+mov rax, qword ptr [r12]
+mov rax, qword ptr [rax + 8]
+cmp rax, rdx
+jne L
+cmp byte ptr [r12 + 0x2c], 0
+jne L
+lea rdi, [rbp - 0x68]
+call F
+cmp qword ptr [r12 + 0x58], r13
+mov byte ptr [r12 + 0x30], 1
+je L
+jmp L
+nop word ptr [rax + rax]
+xor esi, esi
+pxor xmm0, xmm0
+mov qword ptr [rbp - 0x70], 1
+mov word ptr [rbp - 0x34], si
+lea rdi, [rbp - 0x60]
+mov esi, 1
```
(ещё 106 строк диффа: so-query.py fdiff libserver.so 0x5d0e910)

### изменена: 0x61bc340 (198 байт) CDOTA_BaseNPC::vfunc#156, CDOTA_Unit_Announcer::vfunc#156, CDOTA_Unit_CustomGameAnnouncer::vfunc#156
было: 0x61bb440 (67 байт)
- числа в инструкциях: +0 +0xffffffff +0xffffffff
- поля объектов: +0x540 +0x540 +0x548 +0x548
- прямых вызовов: 2 → 4
- цели вызовов: +0x64df680 "./dota/nextbot_s1/nextbot.cpp"; "NextBotCombatCharacter::DoThink" +0x3c72d60 +0x3c97800
- инструкций: 20 → 56
```diff
@@ -1,7 +1,9 @@
 push rbp
 mov rbp, rsp
+push r13
+push r12
 push rbx
 mov rbx, rdi
-sub rsp, 8
+sub rsp, 0x18
 mov rax, qword ptr [rdi + 0x10]
 mov edi, dword ptr [rax + 0x38]
@@ -12,9 +14,43 @@
 jne L
 mov rdi, qword ptr [rbx + 0x1ac8]
+mov r12, qword ptr [rbx + 0x540]
+mov r13, qword ptr [rbx + 0x548]
 test rdi, rdi
+mov rdx, r12
 je L
 call F
+mov rdx, qword ptr [rbx + 0x540]
+lea rax, [T]
+cmp rdx, rax
+je L
+cmp r12, rax
+jne L
+test r13, r13
+je L
+add rsp, 0x18
 mov rdi, rbx
-mov rbx, qword ptr [rbp - 8]
-leave
+pop rbx
+pop r12
+pop r13
+pop rbp
 jmp F
+nop word ptr [rax + rax]
+cmp qword ptr [rbx + 0x548], 0
+je L
+jmp L
+nop dword ptr [rax]
+mov esi, 0xffffffff
+mov rdi, rbx
+call F
+mov rdi, rbx
+movss dword ptr [rbp - 0x24], xmm0
+call F
+movss xmm0, dword ptr [rbp - 0x24]
+add rsp, 0x18
+mov rdi, rbx
+pop rbx
+mov esi, 0xffffffff
+pop r12
+pop r13
+pop rbp
+jmp F
```

### изменена: 0x61c3820 (1363 байт) CDOTA_BaseNPC::vfunc#430, CDOTA_Unit_Announcer::vfunc#430, CDOTA_Unit_CustomGameAnnouncer::vfunc#430
было: 0x61c3880 (288 байт)
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
+mov dword ptr [r12 + 4], edx
+mov dword ptr [r12], eax
+mov rdi, rsi
+nop word ptr [rax + rax]
+mov ecx, dword ptr [r12]
+cmp ecx, edx
+jle L
+mov edx, dword ptr [rbx + 4]
+add rbx, 4
+cmp ecx, edx
+jg L
+cmp ecx, dword ptr [rdi - 4]
+lea rax, [rdi - 4]
+jge L
+nop dword ptr [rax]
+nop dword ptr [rax + rax]
+sub rax, 4
+cmp ecx, dword ptr [rax]
+jl L
+cmp rbx, rax
+jae L
+mov ecx, dword ptr [rax]
+mov rdi, rax
+add rbx, 4
+mov dword ptr [rbx - 4], ecx
+mov dword ptr [rax], edx
+mov edx, dword ptr [rbx]
+jmp L
+cmp ecx, edi
+jl L
+cmp eax, edi
+jge L
+mov dword ptr [r12], edi
+mov dword ptr [rsi - 4], edx
+mov edx, dword ptr [r12 + 4]
+jmp L
+nop dword ptr [rax]
+mov rdx, r13
+mov rdi, rbx
+call L
+mov rax, rbx
+sub rax, r12
+cmp rax, 0x40
+jle L
+mov rdx, rax
+sar rax, 3
+mov rsi, rbx
+sar rdx, 2
+test r13, r13
+jne L
+lea r8, [rdx - 1]
+not rdx
+lea r11, [rax - 1]
+sar r8, 1
+mov r10d, edx
+lea r9, [r12 + rax*4 - 4]
+mov rcx, r11
+and r10d, 1
+cmp r8, rcx
+mov edi, dword ptr [r9]
+mov r13, r9
+jle L
+mov rbx, rcx
+jmp L
+nop word ptr cs:[rax + rax]
+nop word ptr cs:[rax + rax]
+nop word ptr cs:[rax + rax]
+nop word ptr cs:[rax + rax]
+nop word ptr cs:[rax + rax]
+nop word ptr [rax + rax]
+sub rax, 1
+lea r13, [r12 + rax*4]
+cmp r8, rax
+mov edx, dword ptr [r13]
+mov dword ptr [r12 + rbx*4], edx
+jle L
+mov rbx, rax
+lea rdx, [rbx + 1]
+lea rax, [rdx + rdx]
+shl rdx, 3
+lea r13, [r12 + rdx]
+mov r14d, dword ptr [r13]
+cmp dword ptr [r12 + rdx - 4], r14d
+jg L
+mov edx, dword ptr [r13]
+cmp r8, rax
```
(ещё 168 строк диффа: so-query.py fdiff libserver.so 0x61c3820)

### изменена: 0x61ed890 (2044 байт) | строки: "CannotDropNeutralItems"; "item_madstone_bundle"
было: 0x61ed910 (2075 байт)
- виртуальные вызовы: +0x538 (слот 167)
- поля объектов: −0x538
- прямых вызовов: 57 → 56
- инструкций: 505 → 497
```diff
@@ -362,12 +362,8 @@
 je L
 mov rax, qword ptr [r13]
-lea rdx, [T]
-mov rdi, r13
-mov rax, qword ptr [rax + 0x538]
-cmp rax, rdx
-jne L
-call F
-test eax, eax
-jle L
+mov rdi, r13
+call qword ptr [rax + 0x538]
+test al, al
+je L
 mov rax, qword ptr [r13]
 mov rdi, r13
@@ -405,5 +401,5 @@
 lea r15, [T]
 jmp L
-nop
+nop dword ptr [rax]
 cmp byte ptr [r12 + 0x175a], 0
 jne L
@@ -476,8 +472,4 @@
 test rax, rax
 mov r13, rax
-jne L
-jmp L
-call rax
-test al, al
 jne L
 jmp L
```

### изменена: 0x6232670 (2341 байт) CDOTA_BaseNPC_Hero::vfunc#156, CDOTA_Unit_Hero_AncientApparition::vfunc#156, CDOTA_Unit_Hero_AntiMage::vfunc#156 | строки: "valve_dota_001.stinger.respawn"; "DOTAMusic_Hero.Reincarnate"
было: 0x6232730 (2405 байт)
- числа в инструкциях: −0x20
- поля объектов: −0x10 −0x38 −0x668 −0x1ac8
- прямых вызовов: 48 → 46
- цели вызовов: +CDOTA_BaseNPC::vfunc#156 −0x5135780 −CBaseEntity::vfunc#156 −0x5c26e50
- инструкций: 538 → 525
```diff
@@ -77,7 +77,7 @@
 mov edi, dword ptr [rax + 0x38]
 call F
-mov rax, qword ptr [rbx + 0x10]
+movss xmm1, dword ptr [rbx + 0x1e58]
 pxor xmm2, xmm2
-movss xmm1, dword ptr [rbx + 0x1e58]
+mov rdi, rbx
 subss xmm1, xmm0
 movaps xmm0, xmm1
@@ -88,11 +88,4 @@
 orps xmm0, xmm1
 movss dword ptr [rbx + 0x1e60], xmm0
-mov edi, dword ptr [rax + 0x38]
-call F
-test al, al
-jne L
-test byte ptr [rbx + 0x668], 0x20
-je L
-mov rdi, rbx
 call F
 mov rdi, rbx
@@ -123,5 +116,5 @@
 mov edx, dword ptr [rbx + 0x12e4]
 mov ecx, esi
-nop word ptr cs:[rax + rax]
+nop dword ptr [rax]
 cmp edx, ecx
 jae L
@@ -168,5 +161,5 @@
 lea edi, [rsi - 1]
 lea esi, [r13 + 1]
-cmp r14d, edi
+cmp edi, r14d
 jne L
 xor r13d, r13d
@@ -340,10 +333,4 @@
 jmp L
 nop dword ptr [rax]
-mov rdi, qword ptr [rbx + 0x1ac8]
-test rdi, rdi
-je L
-call F
-jmp L
-nop word ptr [rax + rax]
 lea rax, [D]
 xor esi, esi
```

### изменена: 0x62d3560 (460 байт) | строки: "CInfoPlayerStartBadGuys"
было: 0x62d3660 (460 байт)
- числа в инструкциях: +0x5bd1e995 +0x8410b2b2 −0x737975
- прямых вызовов: 11 → 10
- цели вызовов: −0x3bbce40
- инструкций: 103 → 101
```diff
@@ -63,13 +63,11 @@
 mov esi, eax
 call F
-lea rdi, [r14 + 0x10]
-mov esi, eax
-call F
 lea rcx, [rbp - 0x24]
 mov rsi, rbx
 mov rdi, r12
-xor eax, 0x737975
+imul eax, eax, 0x5bd1e995
 mov r9d, 2
 mov r8d, 0x7b0
+xor eax, 0x8410b2b2
 imul eax, eax, 0x5bd1e995
 mov edx, eax
@@ -90,5 +88,5 @@
 call F
 jmp L
-nop dword ptr [rax + rax]
+nop word ptr cs:[rax + rax]
 lea rdi, [D]
 mov esi, 1
```

### изменена: 0x62e0000 (11697 байт) вызывается из: CDOTA_BaseNPC::vfunc#129 | строки: "<NoAbilityName>"; "item_hand_of_midas"; "last_hit"; "PlayerID"; "EntKilled"; "FirstBlood"; "HeroKill"; "TowerKill"
было: 0x62e0100 (11869 байт)
- числа в инструкциях: +1 +1
- цели вызовов: −0x6213ae0
- инструкций: 2367 → 2360
```diff
@@ -3,11 +3,11 @@
 push r15
 push r14
+mov r14, rdx
 push r13
-mov r13, rdx
 push r12
 mov r12, rdi
 push rbx
 mov rbx, rsi
-sub rsp, 0x1f8
+sub rsp, 0x1e8
 test rcx, rcx
 mov qword ptr [rbp - 0x1c8], rcx
@@ -27,6 +27,6 @@
 lea rax, [T]
 xor r15d, r15d
-xor r14d, r14d
-mov qword ptr [rbp - 0x1f0], rax
+mov dword ptr [rbp - 0x1d8], 0
+mov qword ptr [rbp - 0x1e8], rax
 lea rax, [D]
 mov qword ptr [rbp - 0x1d0], rax
@@ -38,20 +38,19 @@
 mov dword ptr [rbp - 0x200], eax
 lea rax, [D]
-mov rdx, r13
+mov rdx, r14
 mov rsi, rbx
 mov rdi, r12
+mov ecx, 0xffffffff
+pxor xmm0, xmm0
+mov qword ptr [rbp - 0x1a8], 0
+movaps xmmword ptr [rbp - 0x1c0], xmm0
 lea r8, [rbp - 0x1c0]
-mov ecx, 0xffffffff
-mov qword ptr [rbp - 0x1a8], 0
-pxor xmm0, xmm0
 mov qword ptr [rbp - 0x1b0], rcx
-mov ecx, r14d
-movaps xmmword ptr [rbp - 0x1c0], xmm0
+mov ecx, r15d
+mov qword ptr [rbp - 0x1a0], 0
 mov rax, qword ptr [rax]
-mov qword ptr [rbp - 0x210], r8
-mov qword ptr [rbp - 0x1a0], 0
 mov qword ptr [rbp - 0x198], 0
 movzx eax, byte ptr [rax + 0x1f0a]
-mov byte ptr [rbp - 0x1d8], al
+mov byte ptr [rbp - 0x1e0], al
 lea rax, [rbp - 0x1a8]
 push rax
@@ -60,13 +59,13 @@
 mov r9, qword ptr [rbp - 0x1c8]
 call F
-mov rdx, r13
+mov rdx, r14
 mov rsi, rbx
 mov rdi, r12
 lea rcx, [rbp - 0x1bc]
-mov dword ptr [rbp - 0x1e0], eax
+mov r13d, eax
 lea r9, [rbp - 0x1b4]
 lea r8, [rbp - 0x1b8]
 call F
-cmp byte ptr [rbp - 0x1d8], 0
+cmp byte ptr [rbp - 0x1e0], 0
 pop r11
 pop rax
@@ -76,21 +75,21 @@
 movzx eax, byte ptr [rax + 0x1f0a]
 xor eax, 1
-mov byte ptr [rbp - 0x1d8], al
-mov ecx, dword ptr [rbp - 0x1e0]
-mov rdx, r13
+mov byte ptr [rbp - 0x1e0], al
+mov ecx, r13d
+mov rdx, r14
 mov rsi, rbx
 mov rdi, r12
 call F
-mov ecx, r15d
-mov rdx, r13
+mov rdx, r14
 mov rsi, rbx
 mov rdi, r12
-call F
-mov ecx, r15d
-mov rdx, r13
+mov ecx, dword ptr [rbp - 0x1d8]
+call F
+mov rdx, r14
 mov rsi, rbx
 mov rdi, r12
-call F
-test r13, r13
+mov ecx, dword ptr [rbp - 0x1d8]
+call F
+test r14, r14
 je L
 cmp byte ptr [rbx + 0xd89], 0
@@ -104,21 +103,21 @@
 jne L
 mov rdi, r12
-mov rdx, r13
+mov rdx, r14
 mov rsi, rbx
 call F
-mov ecx, r14d
-mov rdi, r12
-mov rdx, r13
+mov ecx, r15d
+mov rdi, r12
+mov rdx, r14
 mov rsi, rbx
 call F
 mov rdi, r12
-mov rdx, r13
+mov rdx, r14
 mov rsi, rbx
```
(ещё 2094 строк диффа: so-query.py fdiff libserver.so 0x62e0000)

### изменена: 0x69fd580 (2645 байт)
было: 0x69fd500 (3221 байт)
- числа в инструкциях: −0x7fffffff −0x7fffffff −0x7fffffff −0x7fffffff −0x7fffffff −0x7fffffff −0x7fffffff −0x7fffffff (и ещё 27)
- поля объектов: −0x10 −0x10 −0x10 −0x10 −0x10 −0x10 −0x10
- цели вызовов: +0x69fd330
- инструкций: 787 → 649
```diff
@@ -1,140 +1,2 @@
-mov ecx, esi
-mov esi, dword ptr [rdi + 4]
-mov rdx, rdi
-and esi, 0x7fffffff
-cmp ecx, -1
-je L
-movsxd rax, ecx
-lea r10, [rax + rax*2]
-shl r10, 4
-test esi, esi
-mov r9, r10
-je L
-mov rax, qword ptr [rdi + 8]
-lea r11, [rax + r10]
-mov r8d, dword ptr [r11 + 4]
-cmp r8d, -1
-je L
-movsxd rsi, r8d
-lea rdi, [rsi + rsi*2]
-shl rdi, 4
-mov eax, dword ptr [rax + rdi]
-mov dword ptr [r11 + 4], eax
-test dword ptr [rdx + 4], 0x7fffffff
-je L
-mov rax, qword ptr [rdx + 8]
-movsxd rsi, dword ptr [rax + rdi]
-mov r11, rax
-cmp esi, -1
-je L
-lea rax, [rsi + rsi*2]
-shl rax, 4
-mov dword ptr [r11 + rax + 8], ecx
-test dword ptr [rdx + 4], 0x7fffffff
-je L
-mov rax, qword ptr [rdx + 8]
-mov esi, dword ptr [rax + r10 + 8]
-mov dword ptr [rax + rdi + 8], esi
-mov esi, dword ptr [rdx + 4]
-and esi, 0x7fffffff
-cmp ecx, dword ptr [rdx + 0x10]
-je L
-xor eax, eax
-test esi, esi
-je L
-mov rax, qword ptr [rdx + 8]
-movsxd r10, dword ptr [rax + r10 + 8]
-mov r11, r10
-lea r10, [r10 + r10*2]
-shl r10, 4
-add rax, r10
-cmp r11d, -1
-je L
-cmp ecx, dword ptr [rax]
-je L
-mov dword ptr [rax + 4], r8d
-test dword ptr [rdx + 4], 0x7fffffff
-je L
-mov rax, qword ptr [rdx + 8]
-mov dword ptr [rax + rdi], ecx
-xor eax, eax
-test dword ptr [rdx + 4], 0x7fffffff
-je L
-mov rax, qword ptr [rdx + 8]
-mov dword ptr [rax + r9 + 8], r8d
-ret
-nop
-test esi, esi
-je L
-mov rax, qword ptr [rdi + 8]
-mov dword ptr [rax - 0x2c], 0xffffffff
-mov r8d, dword ptr [rdx + 0x10]
-cmp r8d, -1
-je L
-mov esi, dword ptr [rdx + 4]
-mov r8d, 0xffffffff
-mov rdi, 0xffffffffffffffd0
-mov r10, 0xffffffffffffffd0
-mov r9, 0xffffffffffffffd0
-and esi, 0x7fffffff
-nop dword ptr [rax]
-xor eax, eax
-test esi, esi
-je L
-mov rax, qword ptr [rdx + 8]
-mov dword ptr [rax + r10], r8d
-xor eax, eax
-test dword ptr [rdx + 4], 0x7fffffff
-je L
-mov rax, qword ptr [rdx + 8]
-cmp ecx, -1
-mov dword ptr [rax + rdi], ecx
-jne L
-ret
-nop word ptr [rax + rax]
-movsxd rsi, dword ptr [rdi]
-xor r11d, r11d
-cmp esi, -1
-jne L
-xor eax, eax
-jmp L
-nop
-mov r8d, dword ptr [r10 + 4]
-cmp r8d, -1
-je L
-movsxd rax, r8d
-lea rdi, [rax + rax*2]
-shl rdi, 4
-mov eax, dword ptr [rdi]
-mov dword ptr [r10 + 4], eax
-jmp L
-test esi, esi
-mov dword ptr [rdx + 0x10], r8d
-jne L
-nop dword ptr [rax + rax]
-mov dword ptr [rdi], ecx
-jmp L
-cmp ecx, dword ptr [rdx + 0x10]
-mov rdi, 0xffffffffffffffd0
-jne L
```
(ещё 35 строк диффа: so-query.py fdiff libserver.so 0x69fd580)

### добавлена: 0x69fd330 (576 байт)

### копии существующего кода (2): шаблонные / склеенные компоновщиком функции, такой же код есть и в другой сборке — не новый код
- одной копией существующего кода меньше: 0x5ca6000 (82 байт)
- одной копией существующего кода меньше: 0x61c39c0 (1075 байт)


## Строки библиотек

