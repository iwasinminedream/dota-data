# Dota 6980: изменения кода по функциям

Снимки `6979-11254438` → `6980-11256062`; funcdiff.py. В диффе: [S:…] — строка, [K:…] — константа из данных, F — вызов другой функции, L — переход внутри функции, [D]/[T] — прочие адреса. Регистры и смещения стека меняются и от перекомпиляции.

## libclient.so: функций 281790 → 281790; без изменений 281772, изменено 11, добавлено 1, удалено 1

### изменена: 0x4772e30 (39 байт) CDOTA_Modifier_Juggernaut_BladeFury::vfunc#112
было: 0x4772e30 (31 байт)
- константы из данных (числа логики): +100
- инструкций: 7 → 8
```diff
@@ -2,4 +2,5 @@
 mov rax, rdi
 mov dword ptr [rdi], 1
+subss xmm0, dword ptr [K:100]
 movss dword ptr [rdi + 4], xmm0
 pxor xmm0, xmm0
```

### изменена: 0x56537c0 (1147 байт) CDOTA_Ability_DarkCarnival_Balloon::vfunc#116, CDOTA_Ability_DarkCarnival_Firework::vfunc#116, CDOTA_Ability_DarkCarnival_Pie::vfunc#116 | строки: "dota_player_update_selected_unit"; "dota_ability_changed"; "entityIndex"; "dota_spectator_talent_changed"; "abilityname"; "playerid"; "dota_portrait_ability_layout_changed"
было: 0x5653700 (1262 байт)
- числа в инструкциях: −3 −1
- поля объектов: −0x750 −0xa60 −0xe74 −0xe48
- прямых вызовов: 36 → 35
- инструкций: 301 → 278
```diff
@@ -174,36 +174,18 @@
 mov rdi, rbx
 call F
+mov rdi, rax
+call F
 test rax, rax
 mov r14, rax
 je L
-cmp byte ptr [rax + 0x750], 3
-jne L
-mov rdx, qword ptr [rax]
+mov rax, qword ptr [rax]
 lea rcx, [T]
-mov rax, qword ptr [rdx + 0xa60]
-cmp rax, rcx
-jne L
-mov eax, dword ptr [r14 + 0xe74]
-and eax, 1
-test al, al
-jne L
-mov rax, qword ptr [rdx + 0xe48]
-lea rdx, [T]
-cmp rax, rdx
-je L
-mov rdi, r14
-call rax
-test al, al
-je L
-mov rdx, qword ptr [r14]
-nop word ptr cs:[rax + rax]
-mov rax, qword ptr [rdx + 0xa68]
-lea rcx, [T]
-cmp rax, rcx
+mov rdx, qword ptr [rax + 0xa68]
+cmp rdx, rcx
 jne L
 test byte ptr [r14 + 0xe74], 1
 je L
 mov rdi, r14
-call qword ptr [rdx + 0xe30]
+call qword ptr [rax + 0xe30]
 test al, al
 jne L
@@ -246,5 +228,5 @@
 call qword ptr [rax + 0x48]
 jmp L
-nop dword ptr [rax]
+nop
 mov rax, qword ptr [rbx]
 mov rdi, rbx
@@ -277,12 +259,7 @@
 nop
 mov rdi, r14
-call rax
-test al, al
-jne L
-jmp L
-nop word ptr [rax + rax]
-mov rdi, r14
-call rax
-mov rdx, qword ptr [r14]
+call rdx
+test al, al
+jne L
 jmp L
 mov rdi, rbx
```

### изменена: 0x5655d00 (10267 байт) | строки: "bool"; "EHANDLE"; "float"; "int"; "GameTime_t"; "AbilityBarType_t"; "HeroFacetKey_t"
было: 0x5655cc0 (10587 байт)
- числа в инструкциях: −0x10 −1 −1 −1 −0x3fffffff −0x3fffffff −0x3fffffff −0x3fffffff (и ещё 8)
- поля объектов: −0x158 −0x158 −0x158 −0x168 −0x168 −0x168 −0x168 −0x160 −0x160 −0x160 −0x16c −0x16c (и ещё 3)
- прямых вызовов: 123 → 120
- инструкций: 2115 → 2052
```diff
@@ -513,25 +513,16 @@
 mov edx, r12d
 add edx, 1
-mov edi, 0x10
-mov dword ptr [rbx + 0x158], edx
-mov qword ptr [rax + r12*8], r13
-call F
-movsxd r12, dword ptr [rbx + 0x158]
-mov edi, dword ptr [rbx + 0x168]
-mov r13, rax
 movdqa xmm4, xmmword ptr [rbp - 0xb0]
-movups xmmword ptr [rax], xmm4
-cmp r12d, edi
-je L
-mov rax, qword ptr [rbx + 0x160]
-mov edx, r12d
-movq xmm0, qword ptr [D]
-add edx, 1
 mov rdi, rbx
 mov dword ptr [rbx + 0x158], edx
 mov qword ptr [rax + r12*8], r13
 lea r12, [rbp - 0x40]
+mov rsi, r12
+movaps xmmword ptr [rbp - 0x40], xmm4
+call F
 lea rax, [S:"HeroFacetKey_t"]
 mov rsi, r12
+mov rdi, rbx
+movq xmm0, qword ptr [D]
 movq xmm5, rax
 punpcklqdq xmm0, xmm5
@@ -576,37 +567,5 @@
 pop rbp
 ret
-nop dword ptr [rax + rax]
-mov esi, dword ptr [rbx + 0x16c]
-cmp esi, 0x3fffffff
-ja L
-cmp edi, 0x7fffffff
-je L
-lea r15d, [rdi + 1]
-and esi, 0x3fffffff
-mov ecx, 8
-mov edx, r15d
-call F
-cmp r15d, eax
-mov r14d, eax
-jg L
-movsxd rcx, dword ptr [rbx + 0x168]
-movsxd rdx, r14d
-xor esi, esi
-shl rdx, 3
-mov rdi, qword ptr [rbx + 0x160]
-shl rcx, 3
-cmp dword ptr [rbx + 0x16c], 0x3fffffff
-setbe sil
-call F
-mov edx, dword ptr [rbx + 0x16c]
-mov qword ptr [rbx + 0x160], rax
-cmp edx, 0x3fffffff
-jbe L
-and edx, 0x3fffffff
-mov dword ptr [rbx + 0x16c], edx
-mov edx, dword ptr [rbx + 0x158]
-mov dword ptr [rbx + 0x168], r14d
-jmp L
-nop word ptr [rax + rax]
+nop dword ptr [rax]
 mov esi, dword ptr [rbx + 0x16c]
 cmp esi, 0x3fffffff
@@ -1505,611 +1464,589 @@
 jmp L
 nop word ptr cs:[rax + rax]
-nop dword ptr [rax]
-lea eax, [r14 + r15]
-mov r14d, eax
-shr r14d, 0x1f
-add r14d, eax
-sar r14d, 1
-cmp r15d, r14d
-jg L
-jmp L
-nop dword ptr [rax + rax]
-lea eax, [r14 + r15]
-mov r14d, eax
-shr r14d, 0x1f
-add r14d, eax
-sar r14d, 1
-cmp r15d, r14d
-jg L
-jmp L
-nop dword ptr [rax + rax]
-lea eax, [r14 + r15]
-mov r14d, eax
-shr r14d, 0x1f
-add r14d, eax
-sar r14d, 1
-cmp r15d, r14d
-jg L
-jmp L
-nop dword ptr [rax + rax]
-lea eax, [r14 + r15]
-mov r14d, eax
-shr r14d, 0x1f
-add r14d, eax
-sar r14d, 1
-cmp r15d, r14d
-jg L
-jmp L
-nop dword ptr [rax + rax]
-lea eax, [r14 + r15]
-mov r14d, eax
-shr r14d, 0x1f
-add r14d, eax
-sar r14d, 1
-cmp r15d, r14d
-jg L
-jmp L
-nop dword ptr [rax + rax]
-lea eax, [r14 + r15]
```
(ещё 1149 строк диффа: so-query.py fdiff libclient.so 0x5655d00)

### изменена: 0x5677270 (1266 байт) вызывается из: C_DOTA_BaseNPC::vfunc#155, CAdditionalWearable::vfunc#155, C_DOTAWearableItem::vfunc#155 | строки: "occlusion_glow"
было: 0x5673e20 (869 байт)
- числа в инструкциях: +0 +3 +3 +3 +1
- виртуальные вызовы: +0x50 (слот 10) +0x150 (слот 42) +0x48 (слот 9)
- поля объектов: +0x58 +0xfb8 +0x557 +0x557 +0x557 +0x557 +0x557
- прямых вызовов: 18 → 39
- инструкций: 206 → 299
```diff
@@ -59,6 +59,10 @@
 mov rdi, rbx
 call qword ptr [rax + 0xbd0]
-test al, al
-je L
+mov r13d, eax
+call F
+test al, al
+jne L
+test r13b, r13b
+jne L
 call F
 mov dword ptr [rbp - 0x4c], eax
@@ -113,5 +117,5 @@
 pop rbp
 ret
-nop dword ptr [rax]
+nop word ptr [rax + rax]
 mov rdi, rbx
 call rax
@@ -142,5 +146,74 @@
 nop
 call F
+test al, al
+jne L
+mov rax, qword ptr [rbx]
+lea rdx, [T]
+mov rax, qword ptr [rax + 0xfb8]
+cmp rax, rdx
+jne L
+movzx eax, byte ptr [rbx + 0x557]
+cmp eax, 3
+sete r13b
+call F
+test rax, rax
+je L
+call F
+test rax, rax
+je L
+call F
+test rax, rax
+je F
+call F
+mov rdi, rax
+mov rax, qword ptr [rax]
+call qword ptr [rax + 0x50]
+test rax, rax
+je L
+movzx ebx, byte ptr [rbx + 0x557]
+call F
+test rax, rax
+je L
+call F
+mov rdi, rax
+call F
+cmp eax, ebx
+je L
+call F
 mov dword ptr [rbp - 0x4c], eax
+jmp L
+nop dword ptr [rax]
+xor edi, edi
+call F
+test rax, rax
+mov r15, rax
+je L
+call F
+test al, al
+jne L
+lea rax, [D]
+cmp byte ptr [rax], 0
+jne L
+lea rax, [D]
+mov rdi, qword ptr [rax]
+mov rax, qword ptr [rdi]
+call qword ptr [rax + 0x150]
+test al, al
+je L
+cmp byte ptr [r15 + 0x557], 1
+je L
+call F
+test al, al
+je L
+lea rax, [D]
+mov rax, qword ptr [rax + 8]
+cmp dword ptr [rax + 0x58], 3
+jne L
+call F
+test rax, rax
+je L
+movzx ecx, byte ptr [rbx + 0x557]
+cmp byte ptr [rax + 0x557], cl
+jne L
 jmp L
 nop dword ptr [rax]
@@ -205,2 +278,22 @@
 mov dword ptr [rax + 0x120], 3
 jmp L
+call F
+test rax, rax
+je L
+call F
+test rax, rax
+je L
+call F
+test rax, rax
+je F
+call F
+mov rdi, rax
+mov rax, qword ptr [rax]
+call qword ptr [rax + 0x48]
+cmp eax, 3
+je L
+jmp L
+nop dword ptr [rax + rax]
+mov rdi, rbx
+call rax
+jmp L
```

### изменена: 0x56784a0 (709 байт) C_DOTA_Item_Rune::vfunc#262
было: 0x5678410 (715 байт)
- прямых вызовов: 31 → 30
- инструкций: 204 → 200
```diff
@@ -179,5 +179,5 @@
 call F
 jmp L
-nop word ptr [rax + rax]
+nop word ptr cs:[rax + rax]
 lea rdi, [D]
 lea rsi, [rbp - 0x34]
@@ -197,8 +197,4 @@
 jne L
 jmp L
-call F
-test al, al
-jne L
-jmp L
 or r15d, 0xffffffff
 jmp L
```

### изменена: 0x5678766 (810 байт)
было: 0x56786f0 (800 байт)
- инструкций: 213 → 215
```diff
@@ -1,2 +1,4 @@
+mov rax, qword ptr [0]
+ud2
 movzx eax, byte ptr [rdi + 0x557]
 cmp eax, esi
@@ -126,5 +128,5 @@
 call F
 test rax, rax
-je F
+je L
 call F
 mov rdi, rax
```

### изменена: 0x56947c0 (6130 байт) CDOTA_Ability_DarkCarnival_Balloon::vfunc#277, CDOTA_Ability_DarkCarnival_Firework::vfunc#277, CDOTA_Ability_DarkCarnival_Pie::vfunc#277 | строки: "modifier_vengefulspirit_hybrid_special"; "ClickBehaviorKeys"; "quickcast_preview"; "item_recipe_"; "dota_link_clicked"; "dota.item.item_%s"; "link"; "item_ultimate_scepter"
было: 0x5694740 (6188 байт)
- виртуальные вызовы: +0x748 (слот 233)
- поля объектов: −0x770 −0x770 −0x58 −0x748
- прямых вызовов: 154 → 153
- инструкций: 1326 → 1313
```diff
@@ -484,6 +484,6 @@
 jne L
 nop dword ptr [rax]
-mov r13d, dword ptr [rbp - 0xb8]
-mov edi, r13d
+mov r14d, dword ptr [rbp - 0xb8]
+mov edi, r14d
 call F
 test al, al
@@ -496,5 +496,5 @@
 test al, al
 jne L
-cmp r13d, 2
+cmp r14d, 2
 jne L
 mov edi, 2
@@ -507,11 +507,6 @@
 jne L
 mov rax, qword ptr [r12]
-mov rax, qword ptr [rax + 0x748]
-cmp rax, r14
-jne L
-mov rax, qword ptr [r12 + 0x770]
-test rax, rax
-je L
-mov rax, qword ptr [rax + 0x58]
+mov rdi, r12
+call qword ptr [rax + 0x748]
 test al, 8
 je L
@@ -592,10 +587,10 @@
 mov rdi, r14
 call F
-nop dword ptr [rax]
+nop dword ptr [rax + rax]
 mov eax, 1
 jmp L
 test al, al
 jne L
-nop word ptr cs:[rax + rax]
+nop
 xor r8d, r8d
 xor r13d, r13d
@@ -1194,12 +1189,4 @@
 call F
 jmp L
-mov rdi, r12
-call rax
-jmp L
-xor esi, esi
-mov rdi, r12
-call F
-mov rax, qword ptr [r12 + 0x770]
-jmp L
 xor r13d, r13d
 xor edi, edi
@@ -1208,4 +1195,9 @@
 mov rdi, rax
 call F
+jmp L
+mov edi, dword ptr [rbp - 0xb8]
+call F
+test al, al
+jne L
 jmp L
 call F
@@ -1231,8 +1223,17 @@
 mov rsi, qword ptr [rax + 0x58]
 jmp L
-mov edi, dword ptr [rbp - 0xb8]
-call F
-test al, al
-jne L
+mov rdi, r12
+call rax
+test eax, eax
+mov r13d, eax
+je L
+mov rax, qword ptr [r12]
+lea rdx, [T]
+lea rsi, [S:"CUSTOM ERROR"]
+mov rax, qword ptr [rax + 0x800]
+cmp rax, rdx
+jne L
+mov edi, 0x50
+call F
 jmp L
 cmp r12, r14
@@ -1292,24 +1293,10 @@
 mov rdi, r12
 call rax
-test eax, eax
-mov r13d, eax
-je L
-mov rax, qword ptr [r12]
-lea rdx, [T]
-lea rsi, [S:"CUSTOM ERROR"]
-mov rax, qword ptr [rax + 0x800]
-cmp rax, rdx
-jne L
-mov edi, 0x50
-call F
-jmp L
-xor esi, esi
-mov rdi, r12
-call F
-mov rax, qword ptr [r12 + 0x770]
-jmp L
-mov rdi, r12
-call rax
 mov rsi, rax
+jmp L
+xor esi, esi
+mov rdi, r12
+call F
+mov rax, qword ptr [r12 + 0x770]
 jmp L
 call F
```

### изменена: 0x56ab600 (1231 байт) C_DOTACapture_Killcam::vfunc#14 | строки: "default"
было: 0x56ab5c0 (1167 байт)
- числа в инструкциях: +-1 +-2 +9 +0x3f +0x1ff +0x70
- поля объектов: +0x10
- прямых вызовов: 15 → 14
- инструкций: 263 → 280
```diff
@@ -101,8 +101,25 @@
 test eax, eax
 jle L
-mov rdi, qword ptr [r13 + 0x2080]
-call F
-test rax, rax
-je L
+mov rax, qword ptr [r13 + 0x2080]
+mov ecx, dword ptr [rax]
+cmp ecx, -1
+je L
+mov rsi, qword ptr [D]
+test rsi, rsi
+je L
+cmp ecx, -2
+je L
+movzx eax, word ptr [rax]
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
 mov rdx, qword ptr [rax]
 test rdx, rdx
@@ -175,5 +192,5 @@
 add rdx, rcx
 jmp L
-nop word ptr cs:[rax + rax]
+nop word ptr [rax + rax]
 add rax, 0x2c
 cmp rax, rdx
```

### изменена: 0x57160f0 (11212 байт) | строки: "m_hPowerupRune_1"; "CHandle< C_BaseEntity >"; "CHandle< T >"; "uint32"; "C_BaseEntity"; "CHandle< %s >"; "ehandle"; "m_hPowerupRune_2"
было: 0x5716070 (11228 байт)
- числа в инструкциях: +0x4d09f4ae −0xa4f85ebc
- прямых вызовов: 314 → 313
- инструкций: 2300 → 2297
```diff
@@ -492,8 +492,5 @@
 call F
 lea rdi, [D]
-mov esi, 0xa4f85ebc
-call F
-lea rdi, [D]
-mov esi, eax
+mov esi, 0x4d09f4ae
 call F
 mov edi, 0x158
@@ -1572,5 +1569,5 @@
 call F
 jmp L
-nop dword ptr [rax + rax]
+nop word ptr [rax + rax]
 mov rsi, qword ptr [r15 + 0x10]
 lea rax, [D]
```

### изменена: 0x5e2b880 (976 байт) вызывается из: C_DOTA_Unit_Hero_Rubick::vfunc#538, CDOTA_ParticleManager::vfunc#9, C_DOTAWearableItem::vfunc#304
было: 0x5e2b710 (1088 байт)
- прямых вызовов: 14 → 10
- инструкций: 272 → 239
```diff
@@ -1,35 +1,2 @@
-push rbp
-mov rbp, rsp
-push r12
-push rbx
-movzx eax, byte ptr [D]
-lea rbx, [D]
-test al, al
-je L
-mov rax, rbx
-pop rbx
-pop r12
-pop rbp
-ret
-nop dword ptr [rax]
-lea r12, [D]
-lea rbx, [D]
-mov rdi, r12
-call F
-test eax, eax
-je L
-mov rdi, rbx
-call F
-lea rdx, [D]
-mov rsi, rbx
-lea rdi, [T]
-call F
-mov rdi, r12
-call F
-mov rax, rbx
-pop rbx
-pop r12
-pop rbp
-ret
 test rsi, rsi
 je L
```

### изменена: 0x5f826c0 (4800 байт) | строки: "m_nID"; "Double-save to Member '%s'"; "m_bObtainable"; "m_bShowProgressBar"; "m_bShowInitialEarn"; "m_nBadgePointsPerUnit"; "m_nUnitsPerBadgePoint"; "m_nMaxUnitsForBadgePoints"
было: 0x5f82590 (3520 байт)
- строки: +"Stack depth limit hit (%d)"
- константы из данных (числа логики): +0x00000000000000000000000100000000
- числа в инструкциях: +0 +0 +0 +0 +0 +0 +0 +0 (и ещё 28)
- виртуальные вызовы: +0x20 (слот 4) +0x20 (слот 4) +0x20 (слот 4) +0x20 (слот 4) +0x20 (слот 4)
- прямых вызовов: 80 → 115
- инструкций: 735 → 1001
```diff
@@ -734,2 +734,268 @@
 mov r14, rax
 jmp L
+push rbp
+mov rbp, rsp
+push r13
+push r12
+lea r12, [D]
+push rbx
+sub rsp, 0x2d8
+movdqa xmm0, xmmword ptr [K:0x00000000000000000000000100000000]
+mov qword ptr [rbp - 0x2f0], 0
+mov dword ptr [rbp - 0x2e8], 0x10000
+movups xmmword ptr [rbp - 0x2d4], xmm0
+pxor xmm0, xmm0
+mov byte ptr [rbp - 0x2e4], 1
+mov qword ptr [rbp - 0x2e0], 0
+movaps xmmword ptr [rbp - 0x2c0], xmm0
+movaps xmmword ptr [rbp - 0x2b0], xmm0
+mov qword ptr [rbp - 0x2a0], 0
+mov qword ptr [rbp - 0x298], 0
+mov qword ptr [rbp - 0x290], 0
+movzx eax, byte ptr [D]
+test al, al
+je L
+lea rbx, [rbp - 0x170]
+xor esi, esi
+mov rdi, rbx
+call F
+mov rdi, r12
+call F
+lea rcx, [rbp - 0x278]
+mov edx, 1
+mov rdi, rbx
+mov qword ptr [rbp - 0x278], 0
+mov r13, rax
+movabs rax, 0xc000010000000000
+mov rsi, r13
+mov qword ptr [rbp - 0x280], rax
+call F
+test al, al
+je L
+mov rsi, r13
+mov rdi, rbx
+call F
+mov edx, dword ptr [rbp - 0x48]
+cmp edx, 0x3f
+jle L
+lea rsi, [S:"Stack depth limit hit (%d)"]
+mov rdi, rbx
+xor eax, eax
+call F
+mov rdi, rbx
+call F
+mov r8d, dword ptr [rbp - 0x168]
+test r8d, r8d
+jne L
+sub rsp, 8
+mov esi, 1
+mov rdi, r13
+push 0
+xor r9d, r9d
+xor r8d, r8d
+xor ecx, ecx
+mov edx, 0xa
+call F
+pop rsi
+pop rdi
+xor esi, esi
+lea rdi, [rbp - 0x280]
+call F
+movsxd rax, dword ptr [rbp - 0x2a0]
+mov edx, eax
+sub edx, 1
+js L
+movsxd rcx, edx
+mov edx, edx
+lea rbx, [rcx + rcx*2]
+sub rax, rdx
+lea rax, [rax + rax*2]
+shl rbx, 3
+lea r13, [rax*8 - 0x30]
+nop dword ptr [rax + rax]
+mov rdi, qword ptr [rbp - 0x298]
+xor esi, esi
+add rdi, rbx
+sub rbx, 0x18
+add rdi, 8
+call F
+cmp rbx, r13
+jne L
+cmp dword ptr [rbp - 0x28c], 0x3fffffff
+mov dword ptr [rbp - 0x2a0], 0
+ja L
+mov rsi, qword ptr [rbp - 0x298]
+test rsi, rsi
+je L
+mov rax, qword ptr [D]
+mov rdi, qword ptr [rax]
+mov rax, qword ptr [rdi]
+call qword ptr [rax + 0x20]
+cmp qword ptr [rbp - 0x2a8], 0
+je L
+lea rdi, [rbp - 0x2a8]
+call F
+cmp qword ptr [rbp - 0x2b0], 0
+je L
+lea rdi, [rbp - 0x2b0]
+call F
+cmp qword ptr [rbp - 0x2b8], 0
+je L
+lea rdi, [rbp - 0x2b8]
+call F
+cmp qword ptr [rbp - 0x2c0], 0
+je L
+lea rdi, [rbp - 0x2c0]
+call F
+cmp qword ptr [rbp - 0x2e0], 0
+je L
+lea rdi, [rbp - 0x2e0]
```
(ещё 149 строк диффа: so-query.py fdiff libclient.so 0x5f826c0)

### добавлена: 0x4da9800 (136 байт) CDOTA_Modifier_Item_MeteorHammer_Burn::GetEffectName | строки: "item_starforge"; "particles/items5_fx/starforge_burn.vpcf"; "particles/items4_fx/meteor_hammer_spell_debuff.vpcf"

### удалена: 0x5f83380 (1280 байт) | строки: "Stack depth limit hit (%d)"

### копии существующего кода (6): шаблонные / склеенные компоновщиком функции, такой же код есть и в другой сборке — не новый код
- ещё одна копия существующего кода: 0x4db69a0 (117 байт) CDOTA_Item_Medallion_Of_Courage::vfunc#50
- ещё одна копия существующего кода: 0x5676bc0 (10 байт) вызывается из: C_DOTA_BaseNPC::vfunc#378
- ещё одна копия существующего кода: 0x5e2b7f0 (112 байт) вызывается из: C_DOTA_Unit_Hero_Rubick::vfunc#538, CDOTA_ParticleManager::vfunc#9, CDOTAGCClientSystem::vfunc#1
- одной копией существующего кода меньше: 0x4da4f00 (8 байт) CDOTA_Modifier_Item_MeteorHammer_Burn::GetEffectName | строки: "particles/items4_fx/meteor_hammer_spell_debuff.vpcf"
- одной копией существующего кода меньше: 0x4db5d20 (92 байт) C_DOTA_Item_OrchidMalevolence::vfunc#50
- одной копией существующего кода меньше: 0x56786dc (10 байт)

## libserver.so: функций 221832 → 221833; без изменений 221753, изменено 72, добавлено 6, удалено 4

### изменена: 0x3be2ec0 (507 байт) | строки: "\\\tQ"
было: 0x3be2fc0 (507 байт)
- строки: +"\\\tQ"
- инструкций: 133 → 133
```diff
@@ -12,5 +12,5 @@
 cmp al, 0x24
 ja L
-lea rcx, [D]
+lea rcx, [S:"\\\tQ"]
 movzx eax, al
 movsxd rax, dword ptr [rcx + rax*4]
```

### изменена: 0x3bf7440 (808 байт) вызывается из: CDOTA_NPCSpawnerGoodTop::vfunc#22, CDOTA_Ability_Lua::vfunc#355, CDOTA_Ability_Lua::vfunc#381 | строки: "Y:R"; "%g %g %g"; "%g %g %g %g"; "(null)"; "false"; "true"; "%llu"; "%lld"
было: 0x3bf7540 (808 байт)
- строки: +"Y:R" −"Y;R"
- инструкций: 203 → 203
```diff
@@ -36,5 +36,5 @@
 cmp al, 0x4f
 ja L
-lea rcx, [S:"Y;R"]
+lea rcx, [S:"Y:R"]
 movzx edx, al
 movsxd rdx, dword ptr [rcx + rdx*4]
```

### изменена: 0x3c0cf20 (263 байт) | строки: "G~S"
было: 0x3c0d020 (263 байт)
- строки: +"G~S"
- инструкций: 64 → 64
```diff
@@ -2,5 +2,5 @@
 ja L
 push rbp
-lea rdx, [D]
+lea rdx, [S:"G~S"]
 mov edi, edi
 mov rbp, rsp
```

### изменена: 0x3c27520 (1047 байт) | строки: "7\"U"; "Unsupported KV3 basic type '%s' (%d)!"; "Pointers cannot be used as numeric values"
было: 0x3c27620 (1047 байт)
- строки: +"7\"U" −"7#U"
- инструкций: 245 → 245
```diff
@@ -47,5 +47,5 @@
 cmp r8b, 6
 ja L
-lea rcx, [S:"7#U"]
+lea rcx, [S:"7\"U"]
 movzx edx, r8b
 movsxd rdx, dword ptr [rcx + rdx*4]
```

### изменена: 0x3c27940 (1047 байт) | строки: ";&U"; "Unsupported KV3 basic type '%s' (%d)!"; "Pointers cannot be used as numeric values"
было: 0x3c27a40 (1047 байт)
- строки: +";&U" −";'U"
- инструкций: 245 → 245
```diff
@@ -47,5 +47,5 @@
 cmp r8b, 6
 ja L
-lea rcx, [S:";'U"]
+lea rcx, [S:";&U"]
 movzx edx, r8b
 movsxd rdx, dword ptr [rcx + rdx*4]
```

### изменена: 0x3c27d60 (1047 байт) | строки: "?*U"; "Unsupported KV3 basic type '%s' (%d)!"; "Pointers cannot be used as numeric values"
было: 0x3c27e60 (1047 байт)
- строки: +"?*U" −"?+U"
- инструкций: 245 → 245
```diff
@@ -47,5 +47,5 @@
 cmp r8b, 6
 ja L
-lea rcx, [S:"?+U"]
+lea rcx, [S:"?*U"]
 movzx edx, r8b
 movsxd rdx, dword ptr [rcx + rdx*4]
```

### изменена: 0x3c28180 (1047 байт) | строки: "C.U"; "Unsupported KV3 basic type '%s' (%d)!"; "Pointers cannot be used as numeric values"
было: 0x3c28280 (1047 байт)
- строки: +"C.U" −"C/U"
- инструкций: 245 → 245
```diff
@@ -47,5 +47,5 @@
 cmp r8b, 6
 ja L
-lea rcx, [S:"C/U"]
+lea rcx, [S:"C.U"]
 movzx edx, r8b
 movsxd rdx, dword ptr [rcx + rdx*4]
```

### изменена: 0x3c285a0 (1047 байт) | строки: "G2U"; "Unsupported KV3 basic type '%s' (%d)!"; "Pointers cannot be used as numeric values"
было: 0x3c286a0 (1047 байт)
- строки: +"G2U" −"G3U"
- инструкций: 245 → 245
```diff
@@ -47,5 +47,5 @@
 cmp r8b, 6
 ja L
-lea rcx, [S:"G3U"]
+lea rcx, [S:"G2U"]
 movzx edx, r8b
 movsxd rdx, dword ptr [rcx + rdx*4]
```

### изменена: 0x3c289c0 (1047 байт) | строки: "K6U"; "Unsupported KV3 basic type '%s' (%d)!"; "Pointers cannot be used as numeric values"
было: 0x3c28ac0 (1047 байт)
- строки: +"K6U" −"K7U"
- инструкций: 245 → 245
```diff
@@ -47,5 +47,5 @@
 cmp r8b, 6
 ja L
-lea rcx, [S:"K7U"]
+lea rcx, [S:"K6U"]
 movzx edx, r8b
 movsxd rdx, dword ptr [rcx + rdx*4]
```

### изменена: 0x3c6a320 (715 байт) CDOTA_NPCSpawnerGoodTop::vfunc#51, CDOTA_NPCSpawnerGoodMid::vfunc#51, CDOTA_NPCSpawnerGoodBot::vfunc#51 | строки: "disableshadows"; "7,Y"; "disablereceiveshadows"; "ownername"; "O,Y"
было: 0x3c6a420 (715 байт)
- строки: +"7,Y" +"O,Y" −"7-Y" −"O-Y"
- инструкций: 189 → 189
```diff
@@ -25,5 +25,5 @@
 cmp dl, 6
 ja L
-lea rcx, [S:"7-Y"]
+lea rcx, [S:"7,Y"]
 movzx edx, dl
 movsxd rdx, dword ptr [rcx + rdx*4]
@@ -126,5 +126,5 @@
 cmp dl, 6
 ja L
-lea rcx, [S:"O-Y"]
+lea rcx, [S:"O,Y"]
 movzx edx, dl
 movsxd rdx, dword ptr [rcx + rdx*4]
```

### изменена: 0x3c8a650 (478 байт) | строки: ".,["
было: 0x3c8a750 (478 байт)
- строки: +".,[" −".-["
- инструкций: 116 → 116
```diff
@@ -8,5 +8,5 @@
 cmp dil, 0x4f
 ja L
-lea rdx, [S:".-["]
+lea rdx, [S:".,["]
 movzx eax, dil
 movsxd rax, dword ptr [rdx + rax*4]
```

### изменена: 0x3cbffd0 (2479 байт) CBaseLightProbeVolume::vfunc#2 | строки: "box_mins"; "box_maxs"; "moveable"; "handshake"; "@m^"; "indoor_outdoor_level"; "StartDisabled"; "is_selected_in_hammer"
было: 0x3cc00d0 (2479 байт)
- строки: +"@m^" +"nl^" −"@n^" −"nm^"
- инструкций: 618 → 618
```diff
@@ -71,5 +71,5 @@
 cmp dl, 6
 ja L
-lea rcx, [S:"@n^"]
+lea rcx, [S:"@m^"]
 movzx edx, dl
 movsxd rdx, dword ptr [rcx + rdx*4]
@@ -344,5 +344,5 @@
 cmp dl, 6
 ja L
-lea rcx, [S:"nm^"]
+lea rcx, [S:"nl^"]
 movzx edx, dl
 movsxd rdx, dword ptr [rcx + rdx*4]
```

### изменена: 0x3d22be0 (1712 байт) CEntityOutputTemplate<SndOpEventGuid_t>::vfunc#2 | строки: "m_Value"; "Stack depth limit hit (%d)"; "qOd"; "public.aabb_min"; "public.aabb_max"
было: 0x3d22ce0 (1712 байт)
- строки: +"qOd" −"qPd"
- инструкций: 409 → 409
```diff
@@ -90,5 +90,5 @@
 cmp al, 6
 ja L
-lea rdx, [S:"qPd"]
+lea rdx, [S:"qOd"]
 movzx eax, al
 movsxd rax, dword ptr [rdx + rax*4]
```

### изменена: 0x3d306a0 (547 байт) | строки: "x&e"; "CHandle"; "CBasePlayerController"; "CNetworkUtlVectorBase"; "CBasePlayerPawn"
было: 0x3d307a0 (547 байт)
- строки: +"x&e" −"x'e"
- инструкций: 158 → 158
```diff
@@ -2,5 +2,5 @@
 ja L
 push rbp
-lea rdx, [S:"x'e"]
+lea rdx, [S:"x&e"]
 mov edi, edi
 mov rbp, rsp
```

### изменена: 0x3d51940 (117 байт)
было: 0x3d51a40 (117 байт)
- строки: −"y g"
- инструкций: 39 → 39
```diff
@@ -2,5 +2,5 @@
 cmp edx, 6
 ja L
-lea rcx, [S:"y g"]
+lea rcx, [D]
 push rbp
 mov rdi, rsi
```

### изменена: 0x3d527e0 (339 байт) | строки: "D-g"; "VPhysicsCollisionAttribute_t"; "SolidType_t"; "SurroundingBoundsType_t"
было: 0x3d528e0 (339 байт)
- строки: +"D-g" −"D.g"
- инструкций: 99 → 99
```diff
@@ -2,5 +2,5 @@
 ja L
 push rbp
-lea rdx, [S:"D.g"]
+lea rdx, [S:"D-g"]
 mov edi, edi
 mov rbp, rsp
```

### изменена: 0x3d52a00 (499 байт) | строки: "P/g"; "GameTime_t"; "BeamType_t"; "CBaseEntity"; "CHandle"; "AttachmentHandle_t"; "VectorWS"
было: 0x3d52b00 (499 байт)
- строки: +"P/g" −"P0g"
- инструкций: 135 → 135
```diff
@@ -2,5 +2,5 @@
 ja L
 push rbp
-lea rdx, [S:"P0g"]
+lea rdx, [S:"P/g"]
 mov edi, edi
 mov rbp, rsp
```

### изменена: 0x3d61fc0 (785 байт) | строки: "Z$h"; "Unsupported KV3 basic type '%s' (%d)!"; "Pointers cannot be used as numeric values"
было: 0x3d620c0 (785 байт)
- строки: +"Z$h" −"Z%h"
- инструкций: 219 → 219
```diff
@@ -20,5 +20,5 @@
 cmp bl, 6
 ja L
-lea rdx, [S:"Z%h"]
+lea rdx, [S:"Z$h"]
 movzx eax, bl
 movsxd rax, dword ptr [rdx + rax*4]
```

### изменена: 0x3d85050 (243 байт) | строки: "h0j"; "VectorWS"
было: 0x3d85150 (243 байт)
- строки: +"h0j" −"h1j"
- инструкций: 67 → 67
```diff
@@ -1,5 +1,5 @@
 cmp edi, 6
 ja L
-lea rdx, [S:"h1j"]
+lea rdx, [S:"h0j"]
 mov edi, edi
 push rbp
```

### изменена: 0x3d85150 (227 байт) | строки: "T1j"; "VectorWS"
было: 0x3d85250 (227 байт)
- строки: +"T1j" −"T2j"
- инструкций: 74 → 74
```diff
@@ -1,5 +1,5 @@
 cmp edi, 6
 ja L
-lea rcx, [S:"T2j"]
+lea rcx, [S:"T1j"]
 mov edi, edi
 push rbp
```

### изменена: 0x3d85240 (339 байт) | строки: "(2j"; "BASEPTR"; "GameTick_t"
было: 0x3d85340 (339 байт)
- строки: +"(2j" −"(3j"
- инструкций: 90 → 90
```diff
@@ -1,5 +1,5 @@
 cmp edi, 6
 ja L
-lea rdx, [S:"(3j"]
+lea rdx, [S:"(2j"]
 mov edi, edi
 push rbp
```

### изменена: 0x3d85bb0 (243 байт) | строки: "|;j"; "VectorWS"
было: 0x3d85cb0 (243 байт)
- строки: +"|;j" −"|<j"
- инструкций: 76 → 76
```diff
@@ -2,5 +2,5 @@
 ja L
 push rbp
-lea rdx, [S:"|<j"]
+lea rdx, [S:"|;j"]
 mov edi, edi
 mov rbp, rsp
```

### изменена: 0x3d85fc0 (371 байт) | строки: "\\?j"; "GameTime_t"; "CBaseEntity"; "CHandle"
было: 0x3d860c0 (371 байт)
- строки: +"\\?j" −"\\@j"
- инструкций: 112 → 112
```diff
@@ -2,5 +2,5 @@
 ja L
 push rbp
-lea rdx, [S:"\\@j"]
+lea rdx, [S:"\\?j"]
 mov edi, edi
 mov rbp, rsp
```

### изменена: 0x3d866f0 (98 байт) | строки: "bFj"
было: 0x3d867f0 (98 байт)
- строки: +"bFj" −"bGj"
- инструкций: 36 → 36
```diff
@@ -2,5 +2,5 @@
 cmp edx, 6
 ja L
-lea rcx, [S:"bGj"]
+lea rcx, [S:"bFj"]
 push rbp
 mov rdi, rsi
```

### изменена: 0x3d86940 (117 байт) | строки: "qHj"
было: 0x3d86a40 (117 байт)
- строки: +"qHj" −"qIj"
- инструкций: 39 → 39
```diff
@@ -2,5 +2,5 @@
 cmp edx, 6
 ja L
-lea rcx, [S:"qIj"]
+lea rcx, [S:"qHj"]
 push rbp
 mov rdi, rsi
```

### изменена: 0x3d87bf0 (206 байт) | строки: "?[j"
было: 0x3d87cf0 (206 байт)
- строки: +"?[j" −"?\\j"
- инструкций: 62 → 62
```diff
@@ -2,5 +2,5 @@
 ja L
 push rbp
-lea rdx, [S:"?\\j"]
+lea rdx, [S:"?[j"]
 mov edi, edi
 mov rbp, rsp
```

### изменена: 0x3d88000 (222 байт) | строки: "'_j"
было: 0x3d88100 (222 байт)
- строки: +"'_j" −"'`j"
- инструкций: 64 → 64
```diff
@@ -2,5 +2,5 @@
 ja L
 push rbp
-lea rdx, [S:"'`j"]
+lea rdx, [S:"'_j"]
 mov edi, edi
 mov rbp, rsp
```

### изменена: 0x3d881e0 (435 байт) | строки: "X`j"; "CTransform"; "CNetworkUtlVectorBase"
было: 0x3d882e0 (435 байт)
- строки: +"X`j" −"Xaj"
- инструкций: 118 → 118
```diff
@@ -1,5 +1,5 @@
 cmp edi, 6
 ja L
-lea rdx, [S:"Xaj"]
+lea rdx, [S:"X`j"]
 mov edi, edi
 push rbp
```

### изменена: 0x3d88450 (302 байт) | строки: "scj"
было: 0x3d88550 (302 байт)
- строки: +"scj" −"sdj"
- инструкций: 71 → 71
```diff
@@ -2,5 +2,5 @@
 ja L
 push rbp
-lea rdx, [S:"sdj"]
+lea rdx, [S:"scj"]
 mov edi, edi
 mov rbp, rsp
```

### изменена: 0x3d88920 (811 байт) | строки: "Xgj"
было: 0x3d88a20 (811 байт)
- строки: +"Xgj" −"Xhj"
- инструкций: 232 → 232
```diff
@@ -9,5 +9,5 @@
 movsxd r13, edx
 push r12
-lea rdx, [S:"Xhj"]
+lea rdx, [S:"Xgj"]
 mov r12d, ecx
 push rbx
```

### изменена: 0x3d956d0 (659 байт) | строки: "83k"; "CTakeDamageInfo"; "CTakeDamageResult"
было: 0x3d957d0 (659 байт)
- строки: +"83k" −"84k"
- инструкций: 126 → 126
```diff
@@ -2,5 +2,5 @@
 ja L
 push rbp
-lea rdx, [S:"84k"]
+lea rdx, [S:"83k"]
 mov edi, edi
 mov rbp, rsp
```

### изменена: 0x3d95d00 (563 байт) | строки: "H9k"; "CUtlVector"; "VectorWS"; "GameTime_t"
было: 0x3d95e00 (563 байт)
- строки: +"H9k" −"H:k"
- инструкций: 157 → 157
```diff
@@ -2,5 +2,5 @@
 ja L
 push rbp
-lea rdx, [S:"H:k"]
+lea rdx, [S:"H9k"]
 mov edi, edi
 mov rbp, rsp
```

### изменена: 0x3d98c50 (4083 байт) вызывается из: CTakeDamageInfo::vfunc#2 | строки: "m_vecDamageForce"; "m_bitsDamageType"; "+lk"; "m_vecDamagePosition"; "m_vecReportedPosition"; "m_vecDamageDirection"; "m_hInflictor"; "m_hAttacker"
было: 0x3d98d50 (4083 байт)
- строки: +"+lk" +"6vk" −"+mk" −"6wk"
- инструкций: 886 → 886
```diff
@@ -113,5 +113,5 @@
 cmp r8b, 6
 ja L
-lea rdx, [S:"+mk"]
+lea rdx, [S:"+lk"]
 movzx eax, r8b
 movsxd rax, dword ptr [rdx + rax*4]
@@ -362,5 +362,5 @@
 cmp r8b, 6
 ja L
-lea rdx, [S:"6wk"]
+lea rdx, [S:"6vk"]
 movzx eax, r8b
 movsxd rax, dword ptr [rdx + rax*4]
```

### изменена: 0x3da4900 (414 байт) | строки: "P$l"
было: 0x3da4a00 (414 байт)
- строки: +"P$l" −"P%l"
- инструкций: 136 → 136
```diff
@@ -8,5 +8,5 @@
 movsxd r12, edx
 push rbx
-lea rdx, [S:"P%l"]
+lea rdx, [S:"P$l"]
 mov rbx, rsi
 sub rsp, 0x18
```

### изменена: 0x3da5520 (542 байт) | строки: "00l"
было: 0x3da5620 (542 байт)
- строки: +"00l" −"01l"
- инструкций: 159 → 159
```diff
@@ -9,5 +9,5 @@
 movsxd r12, edx
 push rbx
-lea rdx, [S:"01l"]
+lea rdx, [S:"00l"]
 mov rbx, rsi
 sub rsp, 0x10
```

### изменена: 0x3daa770 (961 байт) | строки: "Bxl"; "%g %g %g"; "(null)"; "%g %g %g %g"; "unknown_variant_type"; "qxl"; "%lld"; "%llu"
было: 0x3daa870 (961 байт)
- строки: +"Bxl" +"qxl" −"Byl" −"qyl"
- инструкций: 213 → 213
```diff
@@ -7,5 +7,5 @@
 cmp al, 0x4f
 ja L
-lea rcx, [S:"Byl"]
+lea rcx, [S:"Bxl"]
 movzx edx, al
 movsxd rdx, dword ptr [rcx + rdx*4]
@@ -91,5 +91,5 @@
 cmp al, 0x47
 ja L
-lea rdx, [S:"qyl"]
+lea rdx, [S:"qxl"]
 movzx eax, al
 movsxd rax, dword ptr [rdx + rax*4]
```

### изменена: 0x3db83b0 (851 байт) | строки: "|Sm"; "%llu"
было: 0x3db84b0 (851 байт)
- строки: +"|Sm" −"|Tm"
- инструкций: 190 → 190
```diff
@@ -21,5 +21,5 @@
 mov rbx, rax
 je L
-lea r13, [S:"|Tm"]
+lea r13, [S:"|Sm"]
 nop dword ptr [rax + rax]
 mov qword ptr [rbp - 0xc0], 0
```

### изменена: 0x3db8bc0 (819 байт) | строки: "$Ym"; "DecalFlags_t"; "GameTime_t"
было: 0x3db8cc0 (819 байт)
- строки: +"$Ym" −"$Zm"
- инструкций: 143 → 143
```diff
@@ -2,5 +2,5 @@
 ja L
 push rbp
-lea rdx, [S:"$Zm"]
+lea rdx, [S:"$Ym"]
 mov edi, edi
 mov rbp, rsp
```

### изменена: 0x3df77a0 (350 байт) | строки: "_,q"
было: 0x3df78a0 (350 байт)
- строки: +"_,q" −"_-q"
- инструкций: 92 → 92
```diff
@@ -2,5 +2,5 @@
 ja L
 push rbp
-lea rdx, [S:"_-q"]
+lea rdx, [S:"_,q"]
 mov edi, edi
 mov rbp, rsp
```

### изменена: 0x3dfc0d0 (502 байт) | строки: "4tq"
было: 0x3dfc1d0 (502 байт)
- строки: +"4tq" −"4uq"
- инструкций: 139 → 139
```diff
@@ -21,5 +21,5 @@
 cmp al, 0x24
 ja L
-lea rcx, [S:"4uq"]
+lea rcx, [S:"4tq"]
 movzx eax, al
 movsxd rax, dword ptr [rcx + rax*4]
```

### изменена: 0x3e1a900 (4702 байт) | строки: "classname"; "connections"; "attributes"; "X[s"
было: 0x3e1aa00 (4702 байт)
- строки: +"X[s" −"X\\s"
- инструкций: 1086 → 1086
```diff
@@ -747,5 +747,5 @@
 cmp al, 0x4f
 ja L
-lea rsi, [S:"X\\s"]
+lea rsi, [S:"X[s"]
 movzx edx, al
 movsxd rdx, dword ptr [rsi + rdx*4]
```

### изменена: 0x3e2b8e0 (542 байт) | строки: "DZt"
было: 0x3e2b9e0 (542 байт)
- строки: +"DZt" −"D[t"
- инструкций: 159 → 159
```diff
@@ -9,5 +9,5 @@
 movsxd r12, edx
 push rbx
-lea rdx, [S:"D[t"]
+lea rdx, [S:"DZt"]
 mov rbx, rsi
 sub rsp, 0x10
```

### изменена: 0x3e6cef0 (243 байт) | строки: " \\x"; "VectorWS"
было: 0x3e6cff0 (243 байт)
- строки: +" \\x" −" ]x"
- инструкций: 70 → 70
```diff
@@ -1,5 +1,5 @@
 cmp edi, 6
 ja L
-lea rdx, [S:" ]x"]
+lea rdx, [S:" \\x"]
 mov edi, edi
 push rbp
```

### изменена: 0x3e6d940 (451 байт) | строки: "dfx"; "CEconWearable"; "CHandle"; "CNetworkUtlVectorBase"; "RelationshipOverride_t"; "CUtlVector"; "Hull_t"; "CMovementStatsProperty"
было: 0x3e6da40 (451 байт)
- строки: +"dfx" −"dgx"
- инструкций: 129 → 129
```diff
@@ -2,5 +2,5 @@
 ja L
 push rbp
-lea rdx, [S:"dgx"]
+lea rdx, [S:"dfx"]
 mov edi, edi
 mov rbp, rsp
```

### изменена: 0x3e6ed90 (98 байт) | строки: "Rzx"
было: 0x3e6ee90 (98 байт)
- строки: +"Rzx" −"R{x"
- инструкций: 36 → 36
```diff
@@ -2,5 +2,5 @@
 cmp edx, 6
 ja L
-lea rcx, [S:"R{x"]
+lea rcx, [S:"Rzx"]
 push rbp
 mov rdi, rsi
```

### изменена: 0x3e6ef70 (187 байт) | строки: "S|x"
было: 0x3e6f070 (187 байт)
- строки: +"S|x" −"S}x"
- инструкций: 52 → 52
```diff
@@ -3,5 +3,5 @@
 ja L
 push rbp
-lea rcx, [S:"S}x"]
+lea rcx, [S:"S|x"]
 mov rdi, rsi
 mov rbp, rsp
```

### изменена: 0x3e6f0e0 (133 байт) | строки: "U}x"
было: 0x3e6f1e0 (133 байт)
- строки: +"U}x" −"U~x"
- инструкций: 41 → 41
```diff
@@ -2,5 +2,5 @@
 cmp edx, 6
 ja L
-lea rcx, [S:"U~x"]
+lea rcx, [S:"U}x"]
 push rbp
 mov rdi, rsi
```

### изменена: 0x3e6f230 (133 байт) | строки: "m~x"
было: 0x3e6f330 (133 байт)
- строки: +"m~x"
- инструкций: 40 → 40
```diff
@@ -1,5 +1,5 @@
 cmp edi, 6
 ja L
-lea rcx, [D]
+lea rcx, [S:"m~x"]
 mov edi, edi
 push rbp
```

### изменена: 0x3eaa420 (769 байт) вызывается из: CAnimGraphControllerBase::vfunc#2, CEmptyGraphController::vfunc#2, EventGrantDefinition_Emoticon_t::vfunc#2 | строки: "b,|"; "Unsupported KV3 basic type '%s' (%d)!"; "Pointers cannot be used as numeric values"
было: 0x3eaa520 (769 байт)
- строки: +"b,|" −"b-|"
- инструкций: 220 → 220
```diff
@@ -31,5 +31,5 @@
 cmp bl, 6
 ja L
-lea rdx, [S:"b-|"]
+lea rdx, [S:"b,|"]
 movzx eax, bl
 movsxd rax, dword ptr [rdx + rax*4]
```

### изменена: 0x3eaea40 (904 байт) | строки: "xo|"
было: 0x3eaeb40 (904 байт)
- строки: +"xo|" −"xp|"
- инструкций: 237 → 237
```diff
@@ -7,5 +7,5 @@
 mov r15d, edx
 push r14
-lea rdx, [S:"xp|"]
+lea rdx, [S:"xo|"]
 push r13
 push r12
```

### изменена: 0x3eaf920 (891 байт) | строки: "$~|"; "CPhysicsBodyGameMarkup"; "CUtlDict"
было: 0x3eafa20 (891 байт)
- строки: +"$~|"
- инструкций: 230 → 230
```diff
@@ -1,5 +1,5 @@
 cmp edi, 6
 ja L
-lea rdx, [D]
+lea rdx, [S:"$~|"]
 mov edi, edi
 push rbp
```

### изменена: 0x3eca360 (904 байт) | строки: "((~"
было: 0x3eca460 (904 байт)
- строки: +"((~" −"()~"
- инструкций: 238 → 238
```diff
@@ -7,5 +7,5 @@
 mov r15d, edx
 push r14
-lea rdx, [S:"()~"]
+lea rdx, [S:"((~"]
 push r13
 push r12
```

### изменена: 0x4453760 (39 байт) CDOTA_Modifier_Juggernaut_BladeFury::vfunc#128
было: 0x4453860 (31 байт)
- константы из данных (числа логики): +100
- инструкций: 7 → 8
```diff
@@ -2,4 +2,5 @@
 mov rax, rdi
 mov dword ptr [rdi], 1
+subss xmm0, dword ptr [K:100]
 movss dword ptr [rdi + 4], xmm0
 pxor xmm0, xmm0
```

### изменена: 0x44bbf50 (461 байт) вызывается из: CDOTA_Modifier_Morphling_Syntropy::vfunc#97 | строки: "modifier_morphling_syntropy_slow"
было: 0x44b5fa0 (573 байт)
- числа в инструкциях: −-1 −-2 −9 −0x3f −0x1ff −0x70 −3
- поля объектов: −0xcc −0xcc −0x10 −0x5d1
- прямых вызовов: 6 → 7
- инструкций: 143 → 118
```diff
@@ -60,30 +60,4 @@
 cmp ecx, -1
 je L
-mov rsi, qword ptr [D]
-test rsi, rsi
-je L
-cmp ecx, -2
-je L
-movzx eax, word ptr [r13 + 0xd0]
-mov rdx, rax
-shr rdx, 9
-and edx, 0x3f
-mov rdx, qword ptr [rsi + rdx*8]
-test rdx, rdx
-je L
-and eax, 0x1ff
-xor r14d, r14d
-imul rax, rax, 0x70
-add rax, rdx
-cmp ecx, dword ptr [rax + 0x10]
-jne L
-mov r14, qword ptr [rax]
-test r14, r14
-je L
-cmp byte ptr [r14 + 0x5d1], 3
-jne L
-mov ecx, dword ptr [r13 + 0xcc]
-cmp ecx, -1
-je L
 cmp ecx, -2
 mov rsi, qword ptr [D]
@@ -91,5 +65,5 @@
 test rsi, rsi
 je L
-movzx eax, word ptr [r13 + 0xcc]
+movzx eax, word ptr [r13 + 0xd0]
 mov rdx, rax
 shr rdx, 9
@@ -103,12 +77,15 @@
 cmp ecx, dword ptr [rax + 0x10]
 jne L
-mov r13, qword ptr [rax]
+mov r14, qword ptr [rax]
+test r14, r14
+je L
+cmp byte ptr [r14 + 0x5d1], 3
+jne L
+mov rdi, r13
+call F
+mov rdi, rbx
+mov r13, rax
+call F
 test r13, r13
-je L
-cmp byte ptr [r13 + 0x5d1], 3
-jne L
-mov rdi, rbx
-call F
-test r14, r14
 mov r15, rax
 je L
@@ -136,7 +113,5 @@
 call F
 jmp L
-nop dword ptr [rax]
-xor r14d, r14d
-jmp L
+nop
 mov rdi, rbx
```
(ещё 1 строк диффа: so-query.py fdiff libserver.so 0x44bbf50)

### изменена: 0x450a810 (1272 байт) CDOTA_Ability_Lich_Sinister_Gaze::vfunc#334 | строки: "channel_duration"; "aoe_scepter"; "duration"; "modifier_lich_sinister_gaze"; "Hero_Lich.SinisterGaze.Cast"; "modifier_lich_sinister_gaze_self"
было: 0x450ee40 (1324 байт)
- числа в инструкциях: −1 −1
- поля объектов: −0x860 −0x860 −0x860 −0x870 −0x868
- инструкций: 316 → 307
```diff
@@ -254,5 +254,4 @@
 call F
 movzx esi, byte ptr [r13 + 0x624]
-mov r14d, 0xffffffff
 movss xmm0, dword ptr [rbp - 0x94]
 mov rdi, rax
@@ -267,18 +266,15 @@
 mov rdi, r12
 call F
+mov dword ptr [rbp - 0x50], 0xffffffff
 mov rax, qword ptr [r13 + 0x10]
+lea rdi, [rbx + 0x860]
 test rax, rax
 je L
-mov r14d, dword ptr [rax + 0x10]
-movsxd r13, dword ptr [rbx + 0x860]
-cmp r13d, dword ptr [rbx + 0x870]
-mov eax, r13d
-je L
-add eax, 1
-mov dword ptr [rbx + 0x860], eax
-mov rax, qword ptr [rbx + 0x868]
-mov dword ptr [rax + r13*4], r14d
-jmp L
-nop dword ptr [rax]
+mov eax, dword ptr [rax + 0x10]
+mov dword ptr [rbp - 0x50], eax
+mov rsi, r12
+call F
+jmp L
+nop dword ptr [rax + rax]
 mov rdi, rbx
 call F
@@ -310,7 +306,2 @@
 pop rbp
 jmp rax
-lea rdi, [rbx + 0x868]
-mov esi, 1
-call F
-mov eax, dword ptr [rbx + 0x860]
-jmp L
```

### изменена: 0x4537a40 (452 байт) | строки: "CDOTA_Ability_Kunkka_Return"
было: 0x4537b40 (460 байт)
- числа в инструкциях: +0x6b0e43b1 −0x3141593d
- прямых вызовов: 11 → 10
- инструкций: 103 → 99
```diff
@@ -56,12 +56,8 @@
 test eax, eax
 je L
-lea r14, [S:"CDOTA_Ability_Kunkka_Return"]
-mov esi, 0x3141593d
-mov rdi, r14
+lea rdi, [D]
+mov esi, 0x6b0e43b1
 call F
-lea rdi, [r14 + 8]
-mov esi, eax
-call F
-lea rdi, [r14 + 0x10]
+lea rdi, [D]
 mov esi, eax
 call F
@@ -80,5 +76,5 @@
 shr edx, 0xf
 xor eax, edx
-mov rdx, r14
+lea rdx, [S:"CDOTA_Ability_Kunkka_Return"]
 mov dword ptr [rbp - 0x24], eax
 call F
@@ -90,5 +86,5 @@
 call F
 jmp L
-nop dword ptr [rax + rax]
+nop dword ptr [rax]
 lea rdi, [D]
 mov esi, 1
```

### изменена: 0x4563260 (296 байт) CDOTA_Modifier_Puck_Coiled::OnIntervalThink
было: 0x4563360 (299 байт)
- инструкций: 79 → 81
```diff
@@ -10,4 +10,26 @@
 test rax, rax
 je L
+mov rdi, rbx
+call F
+test rax, rax
+je L
+mov rdi, rbx
+call F
+mov rdi, rbx
+mov r12, rax
+call F
+mov rdi, r12
+mov rsi, rax
+call F
+test al, al
+je L
+add rsp, 0x20
+pop rbx
+pop r12
+pop r13
+pop r14
+pop rbp
+ret
+nop dword ptr [rax + rax]
 mov rdi, rbx
 call F
@@ -27,18 +49,4 @@
 mov r12, rax
 je L
-mov rdi, rbx
-call F
-test rax, rax
-je L
-mov rdi, rbx
-call F
-mov rdi, rbx
-mov r13, rax
-call F
-mov rdi, r13
-mov rsi, rax
-call F
-test al, al
-jne L
 mov rax, qword ptr [rbx + 0x1af8]
 pxor xmm0, xmm0
@@ -71,9 +79,3 @@
 mov rdi, r13
 call F
-add rsp, 0x20
-pop rbx
-pop r12
-pop r13
-pop r14
-pop rbp
-ret
+jmp L
```

### изменена: 0x48c1fc0 (4055 байт) CDOTA_Ability_Enchantress_Enchant::vfunc#334 | строки: "dominate_duration"; "slow_duration"; "modifier_enchantress_enchant_controlled"; "modifier_dominated"; "enchanted_creep"; "xp_gain_pct"; "modifier_kill"; "duration"
было: 0x48b6130 (4111 байт)
- числа в инструкциях: +1 +1
- поля объектов: +0x860 +0x860 +0x860 +0x868 +0x870
- инструкций: 890 → 887
```diff
@@ -7,5 +7,5 @@
 push rbx
 mov rbx, rdi
-sub rsp, 0x1b8
+sub rsp, 0x1a8
 call F
 test rax, rax
@@ -46,5 +46,5 @@
 call F
 test al, al
-mov r14d, eax
+mov r15d, eax
 jne L
 mov eax, dword ptr [r12 + 0xd3c]
@@ -69,5 +69,5 @@
 mov rdi, r12
 mov rsi, rax
-mov qword ptr [rbp - 0x1d0], rax
+mov qword ptr [rbp - 0x1c0], rax
 call F
 test rax, rax
@@ -84,12 +84,12 @@
 mov rdx, qword ptr [rbx + 0x868]
 movsxd rax, r13d
-lea r15, [rdx + rax*4]
+lea r14, [rdx + rax*4]
 jmp L
 nop dword ptr [rax]
 sub r13d, 1
-sub r15, 4
+sub r14, 4
 cmp r13d, -1
 je L
-mov rdi, r15
+mov rdi, r14
 call F
 test rax, rax
@@ -102,8 +102,6 @@
 cmp r12, rax
 jne L
-lea rax, [rbx + 0x860]
+lea rdi, [rbx + 0x860]
 mov esi, r13d
-mov rdi, rax
-mov qword ptr [rbp - 0x1c0], rax
 call F
 sub dword ptr [rbx + 0x860], 1
@@ -111,10 +109,11 @@
 call F
 test rax, rax
-mov r13, rax
-je L
-mov r13, qword ptr [rax]
-mov rdi, rbx
-call F
-cmp r13, rax
+mov r14, rax
+je L
+mov r14, qword ptr [rax]
+lea r13, [rbp - 0x140]
+mov rdi, rbx
+call F
+cmp r14, rax
 je L
 mov edx, 6
@@ -127,10 +126,10 @@
 mov rax, qword ptr [r12]
 mov rdi, rbx
-mov r13, qword ptr [rax + 0x348]
```
(ещё 517 строк диффа: so-query.py fdiff libserver.so 0x48c1fc0)

### изменена: 0x48d1bd0 (6232 байт) вызывается из: CDOTA_Ability_Dazzle_NothlProjection::vfunc#334 | строки: "shadow_wave_cdr"; "healing_amp"; "leash_start"; "base_leash_pull"; "leash_increase"; "modifier_dazzle_nothl_projection_soul_clone"; "<NoAbilityName>"; "dazzle_nothl_projection_end"
было: 0x48d1d80 (6470 байт)
- строки: −"CreateSoul" −"<NoAbilityName>" −"<NoAbilityName>" −"false"
- числа в инструкциях: −4 −0xac8 −0xffffff80 −0x14
- поля объектов: −0x840 −0x840 −0xe30
- прямых вызовов: 150 → 147
- инструкций: 1293 → 1237
```diff
@@ -1,41 +1,36 @@
 push rbp
-lea rax, [S:"CreateSoul"]
 mov rbp, rsp
 push r15
-movq xmm4, rax
 push r14
 push r13
 push r12
 push rbx
-sub rsp, 0x1e8
+sub rsp, 0x1d8
 test rsi, rsi
-movq xmm3, qword ptr [D]
 mov qword ptr [rbp - 0x1e0], rdi
-punpcklqdq xmm3, xmm4
-movaps xmmword ptr [rbp - 0x210], xmm3
-je L
-lea rbx, [D]
-mov r14, rsi
-mov rdi, qword ptr [rbx]
-call F
-mov r12, rax
+je L
+lea r12, [D]
+mov r15, rsi
+mov rdi, qword ptr [r12]
+call F
+mov rbx, rax
 lea rax, [rbp - 0x140]
-test r12, r12
+test rbx, rbx
 mov qword ptr [rbp - 0x1d0], rax
 je L
-mov rax, qword ptr [r12]
-mov rdi, r12
-mov esi, dword ptr [r12 + 0x6c0]
-lea r15, [S:"shadow_wave_cdr"]
+mov esi, dword ptr [rbx + 0x6c0]
+mov rdi, rbx
+mov rax, qword ptr [rbx]
+lea r14, [S:"shadow_wave_cdr"]
 lea r13, [S:"healing_amp"]
 and esi, 0xffffffdf
 call qword ptr [rax + 0x6b8]
-mov rdi, r12
+mov rdi, rbx
 call F
 xor edx, edx
 xor esi, esi
-mov rdi, r12
-call F
-mov rbx, qword ptr [rbp - 0x1e0]
+mov rdi, rbx
+call F
+mov r12, qword ptr [rbp - 0x1e0]
 xor ecx, ecx
 xor edx, edx
@@ -43,16 +38,16 @@
 movss xmm0, dword ptr [K:-1]
 mov rsi, r9
-mov rdi, rbx
-call F
-xor ecx, ecx
-xor edx, edx
-mov rsi, r15
+mov rdi, r12
+call F
+xor ecx, ecx
```
(ещё 1721 строк диффа: so-query.py fdiff libserver.so 0x48d1bd0)

### изменена: 0x4ac4380 (2664 байт) CDOTA_Ability_EarthSpirit_RollingBoulder::vfunc#371 | строки: "modifier_earthspirit_petrify"; "npc_dota_earth_spirit_stone"; "earth_spirit_stone_caller"; "particles/units/heroes/hero_earth_spirit/espirit_rollingboulder_stone.vpcf"; "Hero_EarthSpirit.RollingBoulder.Stone"; "Hero_EarthSpirit.RollingBoulder.Target"; "Hero_EarthSpirit.RollingBoulder.Damage"; "stun_duration"
было: 0x4ac4640 (2680 байт)
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

### изменена: 0x4ad26e0 (887 байт) вызывается из: CDOTA_Modifier_ChaosKnight_Armageddon_Formation::vfunc#2, CDOTA_Modifier_ChaosKnight_Armageddon_Charge::vfunc#2
было: 0x4ad29c0 (823 байт)
- числа в инструкциях: +0x20 +0x40 +0x2f +0x21
- поля объектов: +0x1248
- инструкций: 212 → 222
```diff
@@ -7,16 +7,25 @@
 push rbx
 sub rsp, 0x48
+test rsi, rsi
+movss dword ptr [rbp - 0x54], xmm0
+je L
 test rdi, rdi
-movss dword ptr [rbp - 0x54], xmm0
-je L
-test rsi, rsi
+mov rbx, rdi
+je L
+mov rax, qword ptr [rdi]
 mov r13, rsi
-je L
-mov rax, qword ptr [rdi]
-mov rbx, rdi
 mov r12, rdx
 call qword ptr [rax + 0x538]
 test al, al
 je L
+mov rax, qword ptr [rbx + 0x1248]
+test al, 0x20
+jne L
+test al, 0x40
+jne L
+bt rax, 0x2f
+jb L
+bt rax, 0x21
+jb L
 lea r14, [D]
 xor esi, esi
@@ -63,5 +72,6 @@
 jg L
 jmp L
-nop
+nop word ptr cs:[rax + rax]
+nop word ptr [rax + rax]
 add r15, 1
 cmp esi, r15d
@@ -203,10 +213,10 @@
 mov esi, 1
 mov qword ptr [rbp - 0x70], r8
-mov qword ptr [rbp - 0x68], rcx
-mov qword ptr [rbp - 0x60], r11
+mov qword ptr [rbp - 0x68], r11
+mov qword ptr [rbp - 0x60], rcx
 call F
 mov r9d, dword ptr [r12]
 mov r8, qword ptr [rbp - 0x70]
-mov rcx, qword ptr [rbp - 0x68]
-mov r11, qword ptr [rbp - 0x60]
+mov r11, qword ptr [rbp - 0x68]
+mov rcx, qword ptr [rbp - 0x60]
 jmp L
```

### изменена: 0x4ad2a60 (810 байт) CDOTA_Modifier_ChaosKnight_Armageddon_Formation::vfunc#2 | строки: "modifier_chaos_knight_armageddon_charge"
было: 0x4ad2d00 (741 байт)
- числа в инструкциях: +0x20 +0x40 +0x2f +0x21 +0x21 +0
- виртуальные вызовы: +0x538 (слот 167)
- поля объектов: +0x1248
- прямых вызовов: 14 → 15
- инструкций: 186 → 205
```diff
@@ -1,4 +1,5 @@
 push rbp
 mov rbp, rsp
+push r14
 push r13
 mov r13, rsi
@@ -6,5 +7,5 @@
 mov r12, rdi
 push rbx
-sub rsp, 0x78
+sub rsp, 0x70
 call F
 test rax, rax
@@ -16,5 +17,5 @@
 test al, al
 jne L
-add rsp, 0x78
+add rsp, 0x70
 mov rdi, r12
 xor r8d, r8d
@@ -25,7 +26,8 @@
 pop r12
 pop r13
+pop r14
 pop rbp
 jmp F
-nop dword ptr [rax + rax]
+nop
 lea rsi, [S:"modifier_chaos_knight_armageddon_charge"]
 xor edx, edx
@@ -45,4 +47,6 @@
 test al, 1
 jne L
+bt rax, 0x21
+jb L
 mov rdi, rbx
 call F
@@ -54,5 +58,5 @@
 call F
 pxor xmm2, xmm2
-movss dword ptr [rbp - 0x50], xmm2
+mov dword ptr [rbp - 0x50], 0
 movshdup xmm1, xmm0
 movaps xmm3, xmm0
@@ -131,8 +135,8 @@
 jne L
 mov rdi, qword ptr [r13 + 0x1788]
-lea rbx, [rbp - 0x48]
+lea r14, [rbp - 0x48]
 xor ecx, ecx
 mov rsi, r13
-mov rdx, rbx
+mov rdx, r14
 call F
 test al, al
@@ -140,18 +144,10 @@
 mov eax, dword ptr [r12 + 0x1afc]
 test eax, eax
-jle L
-movss xmm0, dword ptr [r12 + 0x1af8]
-mov rdi, r12
-movss dword ptr [rbp - 0x64], xmm0
-call F
-movss xmm0, dword ptr [rbp - 0x64]
-lea rdx, [r12 + 0x1b10]
-mov rdi, r13
-mov rsi, rax
-call F
-add rsp, 0x78
```
(ещё 53 строк диффа: so-query.py fdiff libserver.so 0x4ad2a60)

### изменена: 0x4adf120 (1696 байт) CDOTA_Modifier_ChaosKnight_Armageddon_Charge::vfunc#2
было: 0x4adf380 (1680 байт)
- числа в инструкциях: +1 +0x21
- инструкций: 350 → 353
```diff
@@ -213,23 +213,11 @@
 ret
 nop dword ptr [rax]
-mulss xmm1, dword ptr [rbx + 0x1b24]
-subss xmm0, xmm1
-pxor xmm1, xmm1
-comiss xmm1, xmm0
-movss dword ptr [rbx + 0x1b1c], xmm0
-jb L
-movss dword ptr [rbx + 0x1b1c], xmm1
-xor r8d, r8d
-xor ecx, ecx
-xor edx, edx
-xor esi, esi
-mov rdi, rbx
-call F
-jmp L
-nop dword ptr [rax]
 bt rax, 0x2f
 jb L
 bt rax, 0x30
 jb L
+test al, 1
+jne L
+shr rax, 0x21
 mov r13d, eax
 and r13d, 1
@@ -268,4 +256,19 @@
 jmp L
 nop
+mulss xmm1, dword ptr [rbx + 0x1b24]
+subss xmm0, xmm1
+pxor xmm1, xmm1
+comiss xmm1, xmm0
+movss dword ptr [rbx + 0x1b1c], xmm0
+jb L
+movss dword ptr [rbx + 0x1b1c], xmm1
+xor r8d, r8d
+xor ecx, ecx
+xor edx, edx
+xor esi, esi
+mov rdi, rbx
+call F
+jmp L
+nop
 ucomiss xmm0, xmm3
 jp L
@@ -320,9 +323,4 @@
 jmp L
 nop dword ptr [rax + rax]
-mov rdi, r12
-call rax
-mov rdi, rax
-jmp L
-nop dword ptr [rax]
 movss dword ptr [rbp - 0x214], xmm1
 mov rdi, r12
@@ -330,4 +328,9 @@
 movss xmm1, dword ptr [rbp - 0x214]
 mov ecx, eax
+jmp L
+nop dword ptr [rax]
+mov rdi, r12
+call rax
+mov rdi, rax
 jmp L
 nop dword ptr [rax]
```

### изменена: 0x4af81f0 (3218 байт) CDOTA_Ability_Hoodwink_AcornShot::vfunc#371 | строки: "source_projectile_handle"; "debuff_duration"; "modifier_hoodwink_acorn_shot_slow"; "duration"; "special_bonus_unique_hoodwink_acorn_shot_armor_corruption"; "modifier_hoodwink_acorn_shot_armor_corruption"; "modifier_hoodwink_acorn_shot_damage"; "Hero_Hoodwink.AcornShot.Target"
было: 0x4af8470 (3290 байт)
- числа в инструкциях: −0 −0 −0 −0 −0 −0
- прямых вызовов: 67 → 66
- инструкций: 760 → 748
```diff
@@ -135,8 +135,5 @@
 cmp r10d, -1
 jne L
-mov dword ptr [rbp - 0x50], r12d
-mov qword ptr [rbp - 0x48], 0
-mov qword ptr [rbp - 0x40], 0
-mov qword ptr [rbp - 0x38], 0
+nop word ptr cs:[rax + rax]
 movsxd rax, ecx
 lea r13, [rax + rax*2]
@@ -162,16 +159,11 @@
 mov rax, qword ptr [rbx + 0x870]
 add rax, r13
-mov r10d, ecx
+movsxd r10, ecx
 mov dword ptr [rax + 0x10], r12d
 mov qword ptr [rax + 0x18], 0
 mov qword ptr [rax + 0x20], 0
 mov qword ptr [rax + 0x28], 0
-lea rdi, [rbp - 0x48]
-mov dword ptr [rbp - 0x78], r10d
-call F
-movsxd r10, dword ptr [rbp - 0x78]
 mov esi, 1
 jmp L
-nop dword ptr [rax + rax]
 xor eax, eax
 test dword ptr [rbx + 0x86c], 0x7fffffff
@@ -192,5 +184,5 @@
 pop rbp
 ret
-nop word ptr cs:[rax + rax]
+nop
 movsxd r10, dword ptr [rax]
 jmp L
@@ -406,4 +398,11 @@
 jmp L
 nop dword ptr [rax]
+mov eax, dword ptr [rax + 4]
+xor r8d, r8d
+cmp eax, -1
+je L
+movsxd rcx, eax
+jmp L
+nop word ptr [rax + rax]
 xor eax, eax
 nop word ptr [rax + rax]
@@ -462,7 +461,4 @@
 mov eax, dword ptr [rax]
 mov r8d, 1
-cmp eax, -1
-je L
-movsxd rcx, eax
 jmp L
 nop dword ptr [rax]
@@ -477,9 +473,5 @@
 jmp L
 nop dword ptr [rax]
-mov dword ptr [rbp - 0x50], eax
 mov r8d, 1
-mov qword ptr [rbp - 0x48], 0
-mov qword ptr [rbp - 0x40], 0
-mov qword ptr [rbp - 0x38], 0
 mov r10d, dword ptr [rbx + 0x880]
 cmp r10d, -1
@@ -523,10 +515,6 @@
 mov dword ptr [rbp - 0x78], r10d
 call F
-mov r10d, dword ptr [rbp - 0x78]
```
(ещё 86 строк диффа: so-query.py fdiff libserver.so 0x4af81f0)

### изменена: 0x4d282e0 (295 байт) вызывается из: CDOTA_Modifier_Techies_StickyBomb_Chase::OnDestroy, CDOTA_Modifier_Techies_StickyBomb_Chase::vfunc#2 | строки: "countdown"; "modifier_techies_sticky_bomb_countdown"; "duration"
было: 0x4d5a8d0 (279 байт)
- инструкций: 82 → 83
```diff
@@ -4,9 +4,8 @@
 push r14
 push r13
-xor r13d, r13d
 push r12
 push rbx
 mov rbx, rdi
-sub rsp, 0x28
+sub rsp, 0x38
 call F
 mov rdi, rbx
@@ -20,16 +19,15 @@
 mov rdi, r12
 call F
-mov r13d, eax
 lea r12, [rbp - 0x50]
 xor ecx, ecx
 xor edx, edx
+movss dword ptr [rbp - 0x54], xmm0
 lea r15, [S:"modifier_techies_sticky_bomb_countdown"]
 mov rdi, r12
 mov rsi, r15
 call F
-pxor xmm0, xmm0
-cvtsi2ss xmm0, r13d
+movss xmm0, dword ptr [rbp - 0x54]
+lea rsi, [S:"duration"]
 mov rdi, r12
-lea rsi, [S:"duration"]
 call F
 mov rdi, rbx
@@ -69,5 +67,5 @@
 mov rdi, r12
 call F
-add rsp, 0x28
+add rsp, 0x38
 pop rbx
 pop r12
@@ -77,4 +75,7 @@
 pop rbp
 ret
+nop dword ptr [rax + rax]
+pxor xmm0, xmm0
+jmp L
 nop dword ptr [rax]
 call rax
```

### изменена: 0x4d46fa0 (1110 байт) CDOTA_Modifier_Techies_StickyBomb_Chase::vfunc#2 | строки: "modifier_techies_sticky_bomb_countdown"; "countdown"; "duration"; "target"
было: 0x4d5aa50 (1118 байт)
- инструкций: 257 → 255
```diff
@@ -213,7 +213,6 @@
 mov rdi, r12
 call F
-pxor xmm0, xmm0
-mov rdi, r12
-cvtsi2ss xmm0, dword ptr [rbp - 0x8c]
+movss xmm0, dword ptr [rbp - 0x8c]
+mov rdi, r12
 lea rsi, [S:"duration"]
 call F
@@ -246,5 +245,4 @@
 call F
 jmp L
-nop dword ptr [rax]
 mov rdi, r13
 call rax
```

### изменена: 0x4ebf890 (388 байт) CDOTA_Item_Starforge::vfunc#335 | строки: "DOTA_Item.MeteorHammer.Channel"; "modifier_item_meteor_hammer_land"
было: 0x4ebfa90 (391 байт)
- числа в инструкциях: −1
- инструкций: 98 → 98
```diff
@@ -92,5 +92,5 @@
 mov esi, dword ptr [rbx + 0x938]
 mov ecx, 1
-mov edx, 1
+xor edx, edx
 mov rdi, rax
 call F
```

### изменена: 0x4f4a120 (14971 байт) вызывается из: CDOTA_Item_Enchanters_Bauble::vfunc#358, CDOTA_Modifier_Item_Enchanters_Bauble::OnCreated
было: 0x4f498a0 (17659 байт)
- числа в инструкциях: −0 −0 −0 −0 −0 −0 −0 −0 (и ещё 8)
- прямых вызовов: 404 → 340
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
-punpcklqdq xmm0, xmm1
-lea rax, [T]
-movups xmmword ptr [D], xmm0
-movq xmm0, qword ptr [D]
-movq xmm2, rax
-mov rax, rbx
-pop rbx
-pop r12
-punpcklqdq xmm0, xmm2
-movups xmmword ptr [D], xmm0
-pop rbp
-ret
-lea rbx, [D]
-mov rdi, rbx
-call F
-test eax, eax
-je L
-call F
```
(ещё 510 строк диффа: so-query.py fdiff libserver.so 0x4f4a120)

### изменена: 0x56afb90 (336 байт)
было: 0x56afdb0 (439 байт)
- числа в инструкциях: −0 −0 −-1 −-1 −0x7fff −4
- поля объектов: −0x7c −0x84 −0xa
- инструкций: 90 → 72
```diff
@@ -71,20 +71,2 @@
 call F
 jmp L
-movzx eax, word ptr [D]
-cmp ax, -1
-je L
-xor ecx, ecx
-test word ptr [D], 0x7fff
-cmovne rcx, qword ptr [D]
-nop word ptr cs:[rax + rax]
-nop word ptr cs:[rax + rax]
-nop word ptr cs:[rax + rax]
-shl rax, 4
-add rax, rcx
-mov rdx, qword ptr [rax]
-mov qword ptr [rdx + 0x7c], 0
-mov dword ptr [rdx + 0x84], 0
-movzx eax, word ptr [rax + 0xa]
-cmp ax, -1
-jne L
-ret
```

### изменена: 0x5c01b70 (476 байт) CDOTA_NPC_Controller::vfunc#0
было: 0x5c01b40 (554 байт)
- числа в инструкциях: −0
- поля объектов: −0x28 −0x28 −0x20 −0x20 −0x30
- прямых вызовов: 11 → 12
- инструкций: 133 → 114
```diff
@@ -63,20 +63,11 @@
 mov esi, 0x78
 call F
-mov rdi, qword ptr [r12 + 0x18]
-test rdi, rdi
+mov rbx, qword ptr [r12 + 0x18]
+test rbx, rbx
 je L
-mov rax, qword ptr [rdi + 0x30]
-test rax, rax
-je L
-mov rdx, qword ptr [rdi + 0x28]
-test rdx, rdx
-je L
-mov rax, qword ptr [rdi + 0x20]
-test rax, rax
-mov qword ptr [rdx], rax
-je L
-mov rdx, qword ptr [rdi + 0x28]
-mov qword ptr [rax + 8], rdx
+mov rdi, rbx
+call F
 mov esi, 0x88
+mov rdi, rbx
 call F
 mov rbx, qword ptr [r12 + 0x10]
@@ -94,5 +85,5 @@
 jmp F
 mov dword ptr [r12 + 0xa8], 0
-nop word ptr [rax + rax]
+nop dword ptr [rax + rax]
 test eax, eax
 js L
@@ -122,12 +113,2 @@
 jne L
 jmp L
-nop dword ptr [rax]
-lea rdx, [rdi + 0x20]
-cmp qword ptr [rax], rdx
-jne L
-mov rdx, qword ptr [rdi + 0x20]
-test rdx, rdx
-mov qword ptr [rax], rdx
-je L
-mov qword ptr [rdx + 8], 0
-jmp L
```

### изменена: 0x5c12410 (837 байт)
было: 0x5c12450 (781 байт)
- числа в инструкциях: +-1 +-2 +9 +0x3f +0x1ff +0x70
- поля объектов: +0x10 +0x198c +0x198c
- прямых вызовов: 17 → 16
- инструкций: 181 → 197
```diff
@@ -18,14 +18,14 @@
 test al, al
 jne L
-mov r14d, dword ptr [rbx + 0xd3c]
-test r14d, 0x10000
+mov esi, dword ptr [rbx + 0xd3c]
+test esi, 0x10000
 jne L
 mov ecx, dword ptr [rbx + 0x179c]
 cmp ecx, -1
 je L
+mov rdi, qword ptr [D]
+test rdi, rdi
+je L
 cmp ecx, -2
-mov rsi, qword ptr [D]
-je L
-test rsi, rsi
 je L
 movzx eax, word ptr [rbx + 0x179c]
@@ -33,5 +33,5 @@
 shr rdx, 9
 and edx, 0x3f
-mov rdx, qword ptr [rsi + rdx*8]
+mov rdx, qword ptr [rdi + rdx*8]
 test rdx, rdx
 je L
@@ -51,5 +51,5 @@
 call F
 jmp L
-nop dword ptr [rax + rax]
+nop dword ptr [rax]
 mov edi, 0x48
 call F
@@ -137,8 +137,24 @@
 jmp L
 nop dword ptr [rax]
-lea rdi, [rbx + 0x198c]
-call F
-test rax, rax
+mov ecx, dword ptr [rbx + 0x198c]
+cmp ecx, -1
 je L
+cmp ecx, -2
+mov rdi, qword ptr [D]
+je L
+test rdi, rdi
+je L
+movzx eax, word ptr [rbx + 0x198c]
+mov rdx, rax
+shr rdx, 9
+and edx, 0x3f
+mov rdx, qword ptr [rdi + rdx*8]
+test rdx, rdx
+je L
+and eax, 0x1ff
+imul rax, rax, 0x70
+add rax, rdx
+cmp ecx, dword ptr [rax + 0x10]
+jne L
 cmp qword ptr [rax], 0
 je L
@@ -151,7 +167,7 @@
 call F
 jmp L
-nop
+nop dword ptr [rax]
 xor r12d, r12d
-and r14d, 0x10
```
(ещё 3 строк диффа: so-query.py fdiff libserver.so 0x5c12410)

### изменена: 0x5c1f720 (781 байт) вызывается из: CDOTA_BaseNPC::vfunc#15
было: 0x5c1f720 (858 байт)
- числа в инструкциях: −0
- поля объектов: −0x30 −0x28 −0x28 −0x20 −0x20
- прямых вызовов: 18 → 19
- инструкций: 181 → 162
```diff
@@ -47,21 +47,12 @@
 mov r13, rax
 call F
-mov rdi, qword ptr [rbx + 0x18]
+mov r14, qword ptr [rbx + 0x18]
 mov qword ptr [rbx + 0x18], r13
-test rdi, rdi
+test r14, r14
 je L
-mov rax, qword ptr [rdi + 0x30]
-test rax, rax
-je L
-mov rdx, qword ptr [rdi + 0x28]
-test rdx, rdx
-je L
-mov rax, qword ptr [rdi + 0x20]
-test rax, rax
-mov qword ptr [rdx], rax
-je L
-mov rdx, qword ptr [rdi + 0x28]
-mov qword ptr [rax + 8], rdx
+mov rdi, r14
+call F
 mov esi, 0x88
+mov rdi, r14
 call F
 mov edi, 0x78
@@ -80,11 +71,11 @@
 call F
 mov rdi, qword ptr [rbx + 0x28]
-mov edx, 0xffffffff
-movabs rcx, 0xffffffff00000000
+mov ecx, 0xffffffff
+movabs rdx, 0xffffffff00000000
 mov qword ptr [rax], rbx
 mov qword ptr [rax + 8], 0
-mov qword ptr [rax + 0x10], rcx
+mov qword ptr [rax + 0x10], rdx
 test rdi, rdi
-mov qword ptr [rax + 0x18], rdx
+mov qword ptr [rax + 0x18], rcx
 mov qword ptr [rax + 0x20], 0
 mov qword ptr [rbx + 0x28], rax
@@ -158,5 +149,5 @@
 pop rbp
 ret
-nop word ptr cs:[rax + rax]
+nop word ptr [rax + rax]
 mov rax, qword ptr [D]
 mov rdi, qword ptr [rax]
@@ -170,12 +161,2 @@
 call qword ptr [rax + 0x20]
 jmp L
-nop dword ptr [rax]
-lea rdx, [rdi + 0x20]
-cmp qword ptr [rax], rdx
-jne L
-mov rdx, qword ptr [rdi + 0x20]
-test rdx, rdx
-mov qword ptr [rax], rdx
-je L
-mov qword ptr [rdx + 8], 0
-jmp L
```

### добавлена: 0x44b5ba0 (949 байт) вызывается из: CDOTA_Modifier_Juggernaut_BladeFury::vfunc#97 | строки: "particles/units/heroes/hero_juggernaut/juggernaut_blade_fury_attacks.vpcf"; "attach_hitloc"; "npc_dota_hero_juggernaut"; "npc_dota_hero_rubick"; "npc_dota_hero_morphling"

### добавлена: 0x44bb540 (500 байт) вызывается из: CDOTA_Modifier_Bloodseeker_Bloodrage::vfunc#97

### добавлена: 0x48547b0 (360 байт) вызывается из: CDOTA_Modifier_DarkSeer_Normal_Punch::vfunc#97

### добавлена: 0x4e766f0 (96 байт) CDOTA_Modifier_Item_MeteorHammer_Burn::GetEffectName | строки: "item_starforge"; "particles/items5_fx/starforge_burn.vpcf"; "particles/items4_fx/meteor_hammer_spell_debuff.vpcf"

### добавлена: 0x56afd00 (103 байт) вызывается из: CSource1GameConfiguration::vfunc#22

### добавлена: 0x5bffc70 (551 байт) вызывается из: CDOTA_NPC_Controller::vfunc#0

### удалена: 0x44b5af0 (790 байт) вызывается из: CDOTA_Modifier_Juggernaut_BladeFury::vfunc#97 | строки: "particles/units/heroes/hero_juggernaut/juggernaut_blade_fury_attacks.vpcf"; "attach_hitloc"

### удалена: 0x44b61e0 (556 байт) вызывается из: CDOTA_Modifier_Bloodseeker_Bloodrage::vfunc#97

### удалена: 0x48534c0 (447 байт) вызывается из: CDOTA_Modifier_DarkSeer_Normal_Punch::vfunc#97

### удалена: 0x48d1d4d (38 байт)

### копии существующего кода (3): шаблонные / склеенные компоновщиком функции, такой же код есть и в другой сборке — не новый код
- ещё одна копия существующего кода: 0x4f49690 (2688 байт)
- одной копией существующего кода меньше: 0x4854a6a (10 байт)
- одной копией существующего кода меньше: 0x4e6a710 (8 байт) CDOTA_Modifier_Item_MeteorHammer_Burn::GetEffectName | строки: "particles/items4_fx/meteor_hammer_spell_debuff.vpcf"
