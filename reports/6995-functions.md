# Dota 6995: изменения кода по функциям и строки библиотек

Снимки `6993-11269454` → `6995-11273798`; funcdiff.py. В диффе: [S:…] — строка, [K:…] — константа из данных, F — вызов другой функции, L — переход внутри функции, [D]/[T] — прочие адреса. Регистры и смещения стека меняются и от перекомпиляции. Здесь всё, в том числе игровые функции и изменения от пересборки.

## libclient.so: функций 281876 → 281894; без изменений 280341, изменено 1532, добавлено 4, удалено 2

### изменена: 0x3bc0de0 (164 байт) | строки: "0nj"; "Release"; "client"
было: 0x3bbdce0 (164 байт)
- строки: +"0nj" −"0]j"
- инструкций: 34 → 34
```diff
@@ -1,5 +1,5 @@
 cmp edi, 6
 ja F
-lea rdx, [S:"0]j"]
+lea rdx, [S:"0nj"]
 mov edi, edi
 movsxd rax, dword ptr [rdx + rdi*4]
```

### изменена: 0x3bee760 (398 байт) | строки: "D1m"
было: 0x3beb660 (398 байт)
- строки: +"D1m" −"D m"
- инструкций: 128 → 128
```diff
@@ -8,5 +8,5 @@
 movsxd r12, edx
 push rbx
-lea rdx, [S:"D m"]
+lea rdx, [S:"D1m"]
 mov rbx, rsi
 sub rsp, 0x18
```

### изменена: 0x3bf1740 (13077 байт) | строки: "m_nId"; "m_Name"; "m_strNameToken"; "m_CoverImage"; "m_nNumberOfImages"; "m_URLForImages"; "m_nNumDigitsInFilename"; "m_ImageFileExtension"
было: 0x3bee640 (13077 байт)
- строки: −"Tym"
- инструкций: 2855 → 2855
```diff
@@ -1719,5 +1719,5 @@
 cmp al, 6
 ja L
-lea rcx, [S:"Tym"]
+lea rcx, [D]
 movzx edx, al
 movsxd rdx, dword ptr [rcx + rdx*4]
```

### изменена: 0x3c0f400 (753 байт) C_PlayerCosmeticPropClientside::vfunc#11 | строки: "playernumber"; "cosmetic_type"; "j7o"
было: 0x3c0c300 (753 байт)
- строки: +"j7o" −"j&o"
- инструкций: 197 → 197
```diff
@@ -103,5 +103,5 @@
 cmp al, 6
 ja L
-lea rdx, [S:"j&o"]
+lea rdx, [S:"j7o"]
 movzx eax, al
 movsxd rax, dword ptr [rdx + rax*4]
```

### изменена: 0x3c74550 (765 байт) CPointClientUIWorldTextPanelPreviewer::vfunc#2 | строки: "horizontal_align"; "(Wu"; "vertical_align"; "\\Vu"; "orientation"
было: 0x3c71450 (765 байт)
- строки: +"(Wu" +"\\Vu" −"(Fu" −"\\Eu"
- инструкций: 185 → 185
```diff
@@ -23,5 +23,5 @@
 cmp dl, 6
 ja L
-lea rcx, [S:"(Fu"]
+lea rcx, [S:"(Wu"]
 movzx edx, dl
 movsxd rdx, dword ptr [rcx + rdx*4]
@@ -53,5 +53,5 @@
 cmp dl, 6
 ja L
-lea rcx, [S:"\\Eu"]
+lea rcx, [S:"\\Vu"]
 movzx edx, dl
 movsxd rdx, dword ptr [rcx + rdx*4]
```

### изменена: 0x3c74870 (334 байт) | строки: "{Yu"
было: 0x3c71770 (334 байт)
- строки: +"{Yu" −"{Hu"
- инструкций: 82 → 82
```diff
@@ -6,5 +6,5 @@
 ja L
 push rbp
-lea rdx, [S:"{Hu"]
+lea rdx, [S:"{Yu"]
 mov edi, edi
 mov rbp, rsp
```

### изменена: 0x3c85e60 (397 байт) | строки: "<nv"
было: 0x3c82d60 (397 байт)
- строки: +"<nv" −"<]v"
- инструкций: 114 → 114
```diff
@@ -12,5 +12,5 @@
 punpcklqdq xmm0, xmm1
 ja L
-lea rdx, [S:"<]v"]
+lea rdx, [S:"<nv"]
 mov edi, edi
 mov rbx, rsi
```

### изменена: 0x3c86280 (1171 байт) | строки: " rv"; "C_BaseModelEntity"; "CHandle"; "C_NetworkUtlVectorBase"; "CUtlSymbolLarge"; "CUtlVector"
было: 0x3c83180 (1171 байт)
- строки: +" rv" −" av"
- инструкций: 235 → 235
```diff
@@ -2,5 +2,5 @@
 ja L
 push rbp
-lea rdx, [S:" av"]
+lea rdx, [S:" rv"]
 mov edi, edi
 mov rbp, rsp
```

### изменена: 0x3c87e40 (568 байт)
было: 0x3c84b00 (568 байт)
- строки: −",zv"
- инструкций: 160 → 160
```diff
@@ -9,5 +9,5 @@
 movsxd r12, edx
 push rbx
-lea rdx, [S:",zv"]
+lea rdx, [D]
 mov rbx, rsi
 sub rsp, 0x10
```

### изменена: 0x3c88080 (568 байт)
было: 0x3c84d40 (568 байт)
- строки: −"P|v"
- инструкций: 160 → 160
```diff
@@ -9,5 +9,5 @@
 movsxd r12, edx
 push rbx
-lea rdx, [S:"P|v"]
+lea rdx, [D]
 mov rbx, rsi
 sub rsp, 0x10
```

### изменена: 0x3c882c0 (568 байт)
было: 0x3c84f80 (568 байт)
- строки: −"t~v"
- инструкций: 160 → 160
```diff
@@ -9,5 +9,5 @@
 movsxd r12, edx
 push rbx
-lea rdx, [S:"t~v"]
+lea rdx, [D]
 mov rbx, rsi
 sub rsp, 0x10
```

### изменена: 0x3c91ac0 (542 байт) | строки: "|)w"
было: 0x3c8e9c0 (542 байт)
- строки: +"|)w"
- инструкций: 159 → 159
```diff
@@ -9,5 +9,5 @@
 movsxd r12, edx
 push rbx
-lea rdx, [D]
+lea rdx, [S:"|)w"]
 mov rbx, rsi
 sub rsp, 0x10
```

### изменена: 0x3cb5920 (2029 байт) | строки: "hGy"; "CGlobalSymbol"; "CAnimGraph2ParamOptionalRef"; "CTransform"; "e_choreo_outro_type"; "e_choreo_entry_type"; "t_choreo_exit_warp"; "t_choreo_target_warp"
было: 0x3cb2820 (2029 байт)
- строки: +"hGy" −"h6y"
- инструкций: 393 → 393
```diff
@@ -9,5 +9,5 @@
 cmp edi, 6
 ja F
-lea rdx, [S:"h6y"]
+lea rdx, [S:"hGy"]
 mov edi, edi
 mov rbx, rsi
```

### изменена: 0x3cc66d0 (1113 байт) CNetworkTransmitComponent::vfunc#3 | строки: "m_nTransmitStateOwnedCounter"; "|Wz"; "Unsupported KV3 basic type '%s' (%d)!"; "Pointers cannot be used as numeric values"
было: 0x3cc35d0 (1113 байт)
- строки: +"|Wz" −"|Fz"
- инструкций: 259 → 259
```diff
@@ -108,5 +108,5 @@
 cmp r8b, 6
 ja L
-lea rdx, [S:"|Fz"]
+lea rdx, [S:"|Wz"]
 movzx eax, r8b
 movsxd rax, dword ptr [rdx + rax*4]
```

### изменена: 0x3cc9c30 (625 байт) вызывается из: CChoreo_GraphController::vfunc#6 | строки: "unknown"; "false"; "true"; "transform"; "vector"; "float"; "globalSymbol"; "bool"
было: 0x3cc6b30 (625 байт)
- строки: −"Ryz"
- инструкций: 165 → 165
```diff
@@ -18,5 +18,5 @@
 cmp al, 5
 ja L
-lea rdx, [S:"Ryz"]
+lea rdx, [D]
 movzx eax, al
 movsxd rax, dword ptr [rdx + rax*4]
```

### изменена: 0x3cd3fe0 (1127 байт) CHitboxComponent::vfunc#4 | строки: "m_flBoundsExpandRadius"; "X-{"; "<-{"; "Unsupported KV3 basic type '%s' (%d)!"; "Pointers cannot be used as numeric values"
было: 0x3cd0ee0 (1127 байт)
- строки: +"X-{" +"<-{"
- инструкций: 258 → 258
```diff
@@ -51,5 +51,5 @@
 cmp r8b, 6
 ja L
-lea rdx, [D]
+lea rdx, [S:"X-{"]
 movzx eax, r8b
 movsxd rax, dword ptr [rdx + rax*4]
@@ -108,5 +108,5 @@
 cmp r8b, 6
 ja L
-lea rdx, [D]
+lea rdx, [S:"<-{"]
 movzx eax, r8b
 movsxd rax, dword ptr [rdx + rax*4]
```

### изменена: 0x3d040c0 (183 байт) | строки: "+\t~"
было: 0x3d00fc0 (183 байт)
- строки: +"+\t~"
- инструкций: 55 → 55
```diff
@@ -2,5 +2,5 @@
 ja L
 push rbp
-lea rdx, [D]
+lea rdx, [S:"+\t~"]
 mov edi, edi
 mov rbp, rsp
```

### изменена: 0x4a49240 (6 байт) CDOTA_Modifier_Lycan_Pack_Hunter_Marked::IsPurgable
было: 0x4a46140 (3 байт)
- числа в инструкциях: +1
- инструкций: 2 → 2
```diff
@@ -1,2 +1,2 @@
-xor eax, eax
+mov eax, 1
 ret
```

### изменена: 0x4a943f0 (136 байт) CDOTA_Modifier_Lycan_Pack_Hunter::vfunc#79 | строки: "mark_duration"; "mark_range"
было: 0x4a8f600 (74 байт)
- строки: +"mark_range"
- виртуальные вызовы: +0x1a8 (слот 53)
- поля объектов: +0x1afc
- прямых вызовов: 3 → 6
- инструкций: 24 → 40
```diff
@@ -19,4 +19,20 @@
 movaps xmm1, xmm0
 movss dword ptr [rbx + 0x1af8], xmm1
+mov rdi, rbx
+call F
+mov rdi, rbx
+mov r12, rax
+mov rax, qword ptr [rbx]
+call qword ptr [rax + 0x1a8]
+test r12, r12
+pxor xmm1, xmm1
+je L
+xor ecx, ecx
+xor edx, edx
+mov rdi, r12
+lea rsi, [S:"mark_range"]
+call F
+movaps xmm1, xmm0
+movss dword ptr [rbx + 0x1afc], xmm1
 pop rbx
 pop r12
```

### изменена: 0x4c4ed50 (76 байт) CDOTA_Modifier_Shredder_Reactive_Armor::vfunc#88
было: 0x4c4bc10 (51 байт)
- числа в инструкциях: +0
- поля объектов: +0xd80 +0xd88
- цели вызовов: +0x4c8cf30
- инструкций: 7 → 10
```diff
@@ -3,4 +3,7 @@
 mov qword ptr [rdi + 0xd70], rax
 lea rax, [T]
+mov qword ptr [rdi + 0xd80], rax
+lea rax, [T]
+mov qword ptr [rdi + 0xd88], 0
 mov qword ptr [rdi + 0xed0], rax
 mov qword ptr [rdi + 0xed8], 0
```

### изменена: 0x4cbb4c0 (405 байт) CDOTA_Modifier_Primal_Beast_Colossal::OnRefresh | строки: "model_scale_per_stack"; "base_slow_resist"; "base_aoe"; "hp_per_threshold"; "slow_resistance_per_threshold"; "aoe_per_threshold"; "trample_bonus"
было: 0x4cb8360 (396 байт)
- инструкций: 105 → 107
```diff
@@ -63,12 +63,14 @@
 mov rax, qword ptr [rbx]
 call qword ptr [rax + 0x1a8]
-xor eax, eax
 test r12, r12
+pxor xmm1, xmm1
 je L
 lea rsi, [S:"slow_resistance_per_threshold"]
+xor edx, edx
 mov rdi, r12
 call F
+movaps xmm1, xmm0
+movss dword ptr [rbx + 0x1b08], xmm1
 mov rdi, rbx
-mov dword ptr [rbx + 0x1b08], eax
 call F
 mov rdi, rbx
```

### изменена: 0x4cbde70 (351 байт) вызывается из: CDOTA_Modifier_Primal_Beast_Colossal::vfunc#88 | строки: "modifier_primal_beast_trample"
было: 0x4cbaf70 (359 байт)
- инструкций: 85 → 83
```diff
@@ -60,9 +60,7 @@
 pxor xmm0, xmm0
 movss xmm2, dword ptr [rbx + 0x1b10]
-cvtsi2ss xmm1, dword ptr [rbx + 0x1b08]
+cvtsi2ss xmm1, dword ptr [rbx + 0x1afc]
 cvtsi2ss xmm0, eax
-mulss xmm0, xmm1
-pxor xmm1, xmm1
-cvtsi2ss xmm1, dword ptr [rbx + 0x1afc]
+mulss xmm0, dword ptr [rbx + 0x1b08]
 addss xmm0, xmm1
 pxor xmm1, xmm1
```

### изменена: 0x4cc92c0 (7511 байт) | строки: "modifier_primal_beast_trample"
было: 0x4cc6160 (7519 байт)
- инструкций: 1197 → 1195
```diff
@@ -1170,9 +1170,7 @@
 pxor xmm0, xmm0
 movss xmm2, dword ptr [rbx + 0x1b10]
-cvtsi2ss xmm1, dword ptr [rbx + 0x1b08]
+cvtsi2ss xmm1, dword ptr [rbx + 0x1afc]
 cvtsi2ss xmm0, eax
-mulss xmm0, xmm1
-pxor xmm1, xmm1
-cvtsi2ss xmm1, dword ptr [rbx + 0x1afc]
+mulss xmm0, dword ptr [rbx + 0x1b08]
 addss xmm0, xmm1
 pxor xmm1, xmm1
```

### изменена: 0x4cfac50 (7274 байт) | строки: "m_stolenAbilityColorHSV1"; "Vector"; "m_stolenAbilityColorHSV2"; "m_stolenAbilityFXColorHSV"; "OnAbilityColorChanged"; "C_DOTA_Unit_Hero_Rubick"; "5Vec3DIfE"; "18CNetworkVectorBaseI5Vec3DIfEN23C_DOTA_Unit_Hero_Rubick36NetworkVar_m_stolenAbi"
было: 0x4cf7ad0 (7290 байт)
- числа в инструкциях: −0xd −0x5bd1e995 −0x5bd1e995 −0x5bd1e995 −0xf −0x54f49d66
- прямых вызовов: 150 → 152
- цели вызовов: +0x3c18240 +0x3c181b0
- инструкций: 1445 → 1441
```diff
@@ -1031,20 +1031,16 @@
 mov esi, eax
 call F
+lea rdi, [r13 + 0x10]
+mov esi, eax
+call F
+lea rdi, [r13 + 0x14]
+mov esi, eax
+call F
+mov rdx, r13
+mov rsi, rbx
+mov rdi, r15
 lea rcx, [rbp - 0xc0]
-mov rsi, rbx
-mov rdi, r15
-imul eax, eax, 0x5bd1e995
 mov r9d, 2
 mov r8d, 0x2110
-xor eax, 0x54f49d66
-imul eax, eax, 0x5bd1e995
-mov edx, eax
-shr edx, 0xd
-xor eax, edx
-imul eax, eax, 0x5bd1e995
-mov edx, eax
-shr edx, 0xf
-xor eax, edx
-mov rdx, r13
 mov dword ptr [rbp - 0xc0], eax
 call F
@@ -1056,5 +1052,5 @@
 call F
 jmp L
-nop word ptr [rax + rax]
+nop dword ptr [rax + rax]
 mov eax, ebx
 xor edx, edx
```

### изменена: 0x4cfc900 (2187 байт) | строки: "VectorWS"; "m_vStartLocation"; "C_DOTA_Ability_Rubick_Telekinesis"; "8VectorWS"; "15CNetworkVarBaseI8VectorWSN33C_DOTA_Ability_Rubick_Telekinesis27NetworkVar_m_vS"
было: 0x4cf9750 (2235 байт)
- прямых вызовов: 51 → 49
- цели вызовов: −0x7dfcaa0 −0x7e02100
- инструкций: 448 → 434
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
```

### изменена: 0x4cffa40 (5519 байт) | строки: "m_flStartTime"; "GameTime_t"; "float32"; "m_vStartLocation"; "VectorWS"; "OnSetStartLocation"; "C_DOTA_Ability_Ringmaster_TameTheBeasts"; "10GameTime_t"
было: 0x4cfc8c0 (5519 байт)
- числа в инструкциях: −0x5bd1e995 −0x5bd1e995 −0x5bd1e995 −0xd −0xf −0xde1dfe64
- прямых вызовов: 108 → 110
- цели вызовов: +0x3c18240 +0x3c181b0
- инструкций: 1043 → 1043
```diff
@@ -526,34 +526,36 @@
 mov qword ptr [D], rax
 call F
-movsxd r12, dword ptr [D]
+mov r13d, dword ptr [D]
 mov edi, dword ptr [D]
 mov r14, rax
 movq xmm0, qword ptr [D]
 movhps xmm0, qword ptr [D]
+cmp r13d, edi
+movups xmmword ptr [rax], xmm0
+je L
+mov rax, qword ptr [D]
+mov edx, r13d
+add edx, 1
+mov edi, 0x10
+mov dword ptr [D], edx
+movsxd rdx, r13d
+mov qword ptr [rax + rdx*8], r14
+call F
+mov edi, dword ptr [D]
+movq xmm0, rbx
+mov r12d, dword ptr [D]
+movhps xmm0, qword ptr [D]
+mov r13, rax
+movups xmmword ptr [rax], xmm0
 cmp r12d, edi
-movups xmmword ptr [rax], xmm0
 je L
 mov rax, qword ptr [D]
 mov edx, r12d
 add edx, 1
-mov edi, 0x10
 mov dword ptr [D], edx
-mov qword ptr [rax + r12*8], r14
-call F
-movq xmm0, rbx
-mov edi, dword ptr [D]
-movsxd rbx, dword ptr [D]
-movhps xmm0, qword ptr [D]
-mov r12, rax
-movups xmmword ptr [rax], xmm0
-cmp ebx, edi
-je L
-mov rax, qword ptr [D]
-mov edx, ebx
-add edx, 1
-mov dword ptr [D], edx
-mov qword ptr [rax + rbx*8], r12
-jmp L
-nop word ptr [rax + rax]
+movsxd rdx, r12d
+mov qword ptr [rax + rdx*8], r13
+jmp L
+nop
 lea r12, [D]
 mov rdi, r12
@@ -571,20 +573,16 @@
 mov esi, eax
 call F
+lea rdi, [r13 + 0x20]
+mov esi, eax
+call F
+lea rdi, [r13 + 0x24]
+mov esi, eax
+call F
+mov rdx, r13
+mov rsi, rbx
+mov rdi, r14
 lea rcx, [rbp - 0xc0]
-mov rsi, rbx
-mov rdi, r14
-imul eax, eax, 0x5bd1e995
 mov r9d, 2
 mov r8d, 0x868
-xor eax, 0xde1dfe64
-imul eax, eax, 0x5bd1e995
-mov edx, eax
-shr edx, 0xd
-xor eax, edx
-imul eax, eax, 0x5bd1e995
-mov edx, eax
-shr edx, 0xf
-xor eax, edx
-mov rdx, r13
 mov dword ptr [rbp - 0xc0], eax
 call F
@@ -596,5 +594,5 @@
 call F
 jmp L
-nop word ptr [rax + rax]
+nop dword ptr [rax + rax]
 mov eax, r13d
 xor edx, edx
@@ -891,16 +889,17 @@
 call F
 cmp r15d, eax
-mov r13d, eax
+mov r12d, eax
 jle L
-nop dword ptr [rax]
-add r13d, r15d
-mov eax, r13d
+nop word ptr cs:[rax + rax]
+nop dword ptr [rax + rax]
+add r12d, r15d
+mov eax, r12d
 shr eax, 0x1f
-add r13d, eax
-sar r13d, 1
-cmp r15d, r13d
+add r12d, eax
+sar r12d, 1
+cmp r15d, r12d
 jg L
 movsxd rcx, dword ptr [D]
-movsxd rdx, r13d
+movsxd rdx, r12d
 xor esi, esi
 shl rdx, 3
```
(ещё 39 строк диффа: so-query.py fdiff libclient.so 0x4cffa40)

### изменена: 0x5d89f20 (31 байт) вызывается из: CDOTA_Modifier_Special_Bonus_HP_Regen::vfunc#88
было: 0x5d86da0 (35 байт)
- инструкций: 8 → 7
```diff
@@ -1,4 +1,3 @@
-pxor xmm0, xmm0
-cvtsi2ss xmm0, dword ptr [rsi + 0x1af8]
+movss xmm0, dword ptr [rsi + 0x1af8]
 mov rax, rdi
 mov dword ptr [rdi], 1
```

### изменена: 0x5e403b0 (555178 байт)
было: 0x5e3cf30 (554458 байт)
- константы из данных (числа логики): +0x00000000000000090000000000000000
- числа в инструкциях: +0xffffffff +0 +0 +0 +0 +0 +0 +0 (и ещё 19)
- прямых вызовов: 5392 → 5399
- цели вызовов: +0x5de6f60 −0x5de6ce0
- инструкций: 86256 → 86368
```diff
@@ -86129,4 +86129,116 @@
 push rbp
 mov rbp, rsp
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
+mov qword ptr [D], 0
+mov qword ptr [D], 0
+mov qword ptr [D], 0
+mov qword ptr [D], 0
+mov qword ptr [D], 0
+lea rax, [D]
+lea rdi, [T]
+mov rdx, qword ptr [rax]
+mov qword ptr [rax], rsi
+mov qword ptr [D], rdx
+lea rdx, [D]
+mov eax, dword ptr [rdx]
+lea ecx, [rax + 1]
+mov dword ptr [D], eax
+mov dword ptr [rdx], ecx
+lea rdx, [D]
+call F
+mov rdi, rbx
+call F
+mov rax, qword ptr [D]
+test rax, rax
+jne L
+nop
+movzx eax, byte ptr [D]
+test al, al
+je L
+lea rax, [D]
+mov qword ptr [D], rax
+mov rax, qword ptr [D]
+lea rbx, [D]
+mov qword ptr [D], rbx
+mov qword ptr [D], rbx
+mov qword ptr [D], rax
+call F
+movq xmm0, qword ptr [D]
+mov qword ptr [D], 0
+mov qword ptr [D], rax
+lea rax, [T]
+mov qword ptr [D], 0
+movq xmm2, rax
+punpcklqdq xmm0, xmm2
+lea rax, [T]
+movups xmmword ptr [D], xmm0
+movq xmm0, qword ptr [D]
+movq xmm3, rax
+mov rax, rbx
+mov rbx, qword ptr [rbp - 8]
+punpcklqdq xmm0, xmm3
+movups xmmword ptr [D], xmm0
+leave
+ret
+nop dword ptr [rax]
+lea rbx, [D]
+mov rdi, rbx
+call F
+test eax, eax
+je L
+call F
+mov rdi, rbx
+mov qword ptr [D], rax
+call F
+jmp L
+push rbp
+mov rbp, rsp
 push r12
 push rbx
```

### изменена: 0x5ecea00 (1152 байт) | строки: "Stack depth limit hit (%d)"
было: 0x5ecb240 (1120 байт)
- виртуальные вызовы: +0x20 (слот 4)
- прямых вызовов: 26 → 27
- инструкций: 225 → 232
```diff
@@ -99,12 +99,9 @@
 cmp rsi, rdx
 je L
-cmp eax, 0x3fffffff
-ja L
 test rsi, rsi
 je L
-mov rax, qword ptr [D]
-mov rdi, qword ptr [rax]
-mov rax, qword ptr [rdi]
-call qword ptr [rax + 0x20]
+cmp eax, 0x3fffffff
+jbe L
+nop dword ptr [rax]
 mov dword ptr [rbp - 0x148], 0
 mov edx, dword ptr [rbp - 0x138]
@@ -135,5 +132,5 @@
 pop rbp
 ret
-nop dword ptr [rax]
+nop word ptr [rax + rax]
 lea r13, [rbp - 0x320]
 mov rsi, rbx
@@ -144,11 +141,17 @@
 cmp eax, 0x3fffffff
 ja L
+mov rsi, qword ptr [rbp - 0xe8]
+test rsi, rsi
+je L
+mov rax, qword ptr [D]
+mov rdi, qword ptr [rax]
+mov rax, qword ptr [rdi]
+call qword ptr [rax + 0x20]
+jmp L
+cmp eax, 0x3fffffff
+ja L
 mov rsi, qword ptr [rbp - 0x140]
 jmp L
-cmp eax, 0x3fffffff
-ja L
-mov rsi, qword ptr [rbp - 0xe8]
-jmp L
-nop word ptr [rax + rax]
+nop dword ptr [rax + rax]
 lea r13, [rbp - 0x320]
 jmp L
@@ -217,9 +220,13 @@
 pop rdi
 jmp L
-nop word ptr [rax + rax]
+nop
 cmp eax, 0x3fffffff
 jbe L
 jmp L
 cmp eax, 0x3fffffff
-jbe L
-jmp L
+ja L
+mov rax, qword ptr [D]
+mov rdi, qword ptr [rax]
+mov rax, qword ptr [rdi]
+call qword ptr [rax + 0x20]
+jmp L
```

### изменена: 0x5ecd520 (83 байт) CDOTA_Modifier_Special_Bonus_Corruption_Debuff::OnCreated | строки: "value"
было: 0x5ecdca0 (76 байт)
- цели вызовов: +0x3bfbd70 "AbilityManaCost"; "AbilityHealthCost" −0x3bfc220 "AbilityManaCost"; "AbilityHealthCost"
- инструкций: 25 → 26
```diff
@@ -9,6 +9,6 @@
 mov rax, qword ptr [rbx]
 call qword ptr [rax + 0x1a8]
-xor eax, eax
 test r12, r12
+pxor xmm1, xmm1
 je L
 xor r9d, r9d
@@ -19,5 +19,6 @@
 mov rdi, r12
 call F
-mov dword ptr [rbx + 0x1af8], eax
+movaps xmm1, xmm0
+movss dword ptr [rbx + 0x1af8], xmm1
 pop rbx
 pop r12
```

### изменена: 0x5ee8a00 (122595 байт) | строки: "scripts/height_levels.txt"; "Use SQL data from playtests to populate quests. Otherwise will use vdata from pr"; "dota_road_to_ti_use_playtest_data"; "dota_rubick_arcana_override_score"; "Reload the rubick arcana descriptor file"; "cl_dota_rubick_arcana_reload"; "dota_scenario_autosave"; "Enable autosaves while spectating a match from lobby"
было: 0x5ee5280 (122455 байт)
- числа в инструкциях: +0 +0
- прямых вызовов: 2568 → 2571
- инструкций: 19191 → 19213
```diff
@@ -18798,4 +18798,26 @@
 mov qword ptr [rbp - 0xb0], rax
 call F
+mov rsi, rbx
+mov qword ptr [rbp - 0xa8], r12
+lea rax, [T]
+mov qword ptr [rbp - 0xa0], 0
+lea rdi, [D]
+mov qword ptr [rbp - 0xb0], rax
+call F
+call F
+mov rsi, rbx
+mov qword ptr [rbp - 0xa8], r12
+mov qword ptr [D], rax
+mov rax, qword ptr [r14]
+lea rdi, [D]
+mov qword ptr [rbp - 0xa0], 0
+mov qword ptr [D], rax
+lea rax, [D]
+mov qword ptr [r14], rax
+lea rax, [T]
+mov qword ptr [D], rax
+lea rax, [T]
+mov qword ptr [rbp - 0xb0], rax
+call F
 lea rax, [T]
 mov rsi, rbx
@@ -18935,18 +18957,18 @@
 mov rsi, r13
 call F
-lea rax, [D]
+xor edx, edx
 mov r9, rbx
+mov ecx, 0x6000
+lea rax, [D]
 mov qword ptr [D], r13
 lea r13, [D]
-mov ecx, 0x6000
-mov byte ptr [rbp - 0x40], 0
-mov qword ptr [D], rax
-xor eax, eax
-xor edx, edx
-mov rdi, r13
-lea r8, [S:"Certain speech concepts will not be said more than once per (n) seconds. Set to 0 to disable."]
 mov word ptr [rbp - 0x50], dx
 mov edx, 1
+lea r8, [S:"Certain speech concepts will not be said more than once per (n) seconds. Set to 0 to disable."]
+mov rdi, r13
+mov qword ptr [D], rax
+xor eax, eax
 lea rsi, [S:"dota_speech_hardcoded_respeak_delay"]
+mov byte ptr [rbp - 0x40], 0
 mov word ptr [rbp - 0xac], ax
 mov qword ptr [D], r15
```

### изменена: 0x601d0c0 (1613 байт) CDotaAddWaterReflectionViews::vfunc#1
было: 0x600bec0 (1613 байт)
- цели вызовов: +0x601a020 "Water Reflection Stencil View"; "DotaReflectionDepth"
- инструкций: 407 → 405
```diff
@@ -8,7 +8,6 @@
 sub rsp, 0x68
 movsxd rax, dword ptr [r8]
-mov qword ptr [rbp - 0x70], rdi
+mov qword ptr [rbp - 0x70], rcx
 mov rdx, qword ptr [D]
-mov qword ptr [rbp - 0x78], rcx
 mov rbx, qword ptr [r8 + 8]
 shl rax, 5
@@ -46,9 +45,9 @@
 test rax, rax
 je L
-mov dword ptr [rbp - 0x7c], 0
+mov dword ptr [rbp - 0x74], 0
 xor r14d, r14d
 xor r12d, r12d
-mov qword ptr [rbp - 0x88], rsi
-nop dword ptr [rax]
+mov qword ptr [rbp - 0x80], rsi
+nop word ptr cs:[rax + rax]
 mov rax, qword ptr [rbx]
 mov r13, qword ptr [rax + 0x28]
@@ -84,5 +83,5 @@
 lea rax, [rax + rax*2]
 comiss xmm1, dword ptr [r14 + rax*8]
-lea r9, [rax*8]
+lea r10, [rax*8]
 jp L
 je L
@@ -173,12 +172,11 @@
 test eax, eax
 setne dl
-mov rdi, qword ptr [rbp - 0x70]
+mov rdi, qword ptr [rbp - 0x68]
 mov byte ptr [rbp - 0x47], dl
-mov r9d, r12d
-mov r8d, 1
+mov r8d, r12d
+mov ecx, 1
 mov byte ptr [rbp - 0x48], dl
-mov rcx, qword ptr [rbp - 0x78]
-mov rdx, qword ptr [rbp - 0x88]
-mov rsi, qword ptr [rbp - 0x68]
+mov rsi, qword ptr [rbp - 0x80]
+mov rdx, qword ptr [rbp - 0x70]
 call F
 mov rdi, qword ptr [rbp - 0x40]
@@ -212,5 +210,5 @@
 cmp edx, -1
 je L
-mov rdi, qword ptr [r14 + r9 + 0x10]
+mov rdi, qword ptr [r14 + r10 + 0x10]
 test rdi, rdi
 je L
@@ -227,5 +225,4 @@
 cmp r12, r14
 je L
-nop dword ptr [rax + rax]
 mov rsi, qword ptr [rbx + 0x10]
 test rsi, rsi
@@ -278,5 +275,5 @@
 sub r10d, r13d
 sub r10d, 1
-mov eax, dword ptr [rbp - 0x7c]
+mov eax, dword ptr [rbp - 0x74]
 add r12d, 1
 cmp r12d, eax
@@ -316,9 +313,9 @@
 cmp rax, 0x7fffffff
 jg L
-mov edi, dword ptr [rbp - 0x7c]
+mov edi, dword ptr [rbp - 0x74]
 xor esi, esi
 mov ecx, 0x18
 mov edx, r12d
-mov qword ptr [rbp - 0x90], r11
+mov qword ptr [rbp - 0x88], r11
 mov dword ptr [rbp - 0x68], r9d
 mov dword ptr [rbp - 0x58], r10d
@@ -328,5 +325,5 @@
 mov r9d, dword ptr [rbp - 0x68]
 mov r8d, eax
-mov r11, qword ptr [rbp - 0x90]
+mov r11, qword ptr [rbp - 0x88]
 jl L
 movsxd rax, r8d
@@ -335,5 +332,5 @@
 mov dword ptr [rbp - 0x68], r10d
 lea rcx, [r11 + r11*2]
-mov dword ptr [rbp - 0x90], r9d
+mov dword ptr [rbp - 0x88], r9d
 lea rdx, [rax + rax*2]
 shl rcx, 3
@@ -342,8 +339,8 @@
 call F
 mov r8d, dword ptr [rbp - 0x58]
-mov r9d, dword ptr [rbp - 0x90]
+mov r9d, dword ptr [rbp - 0x88]
 mov r14, rax
 mov r10d, dword ptr [rbp - 0x68]
-mov dword ptr [rbp - 0x7c], r8d
+mov dword ptr [rbp - 0x74], r8d
 jmp L
 nop dword ptr [rax]
@@ -353,5 +350,6 @@
 mov edx, 8
 jmp L
-nop word ptr [rax + rax]
+nop word ptr cs:[rax + rax]
+nop word ptr cs:[rax + rax]
 add r8d, r12d
 mov eax, r8d
@@ -383,6 +381,6 @@
 mov edx, 4
 jmp L
-mov edi, dword ptr [rbp - 0x7c]
-mov qword ptr [rbp - 0x90], r11
+mov edi, dword ptr [rbp - 0x74]
+mov qword ptr [rbp - 0x88], r11
 mov dword ptr [rbp - 0x68], r9d
```
(ещё 19 строк диффа: so-query.py fdiff libclient.so 0x601d0c0)

### изменена: 0x6014b00 (4897 байт) вызывается из: CRenderingPipelineDota::vfunc#0 | строки: "Deferred Global Light"
было: 0x6012f70 (5585 байт)
- числа в инструкциях: −0 −0 −1 −1 −4 −4 −2 −2 (и ещё 13)
- поля объектов: −0x1f0 −0x1f0 −0x200 −0x200 −0x248 −0x248 −0x248 −0x248 −0x20 −0x20 −0x20 −0x30 (и ещё 5)
- инструкций: 1240 → 1080
```diff
@@ -356,18 +356,16 @@
 lea r14, [r13 + 0xd0]
 jne L
-movdqa xmm2, xmmword ptr [r13 + 0x1e0]
 mov eax, 0x38156425
-movd xmm0, eax
 movzx r15d, byte ptr [rbx + 0x81]
-movdqa xmm1, xmm2
-pshufd xmm0, xmm0, 0
-pcmpeqd xmm1, xmm0
-movmskps ecx, xmm1
-test ecx, ecx
-jne L
-movdqa xmm1, xmmword ptr [r13 + 0x1f0]
-movdqa xmm3, xmm1
-pcmpeqd xmm3, xmm0
-movmskps eax, xmm3
+movd xmm0, eax
+pshufd xmm0, xmm0, 0
+movdqa xmm1, xmm0
+pcmpeqd xmm1, xmmword ptr [r13 + 0x1e0]
+movmskps eax, xmm1
+test eax, eax
+jne L
+movdqa xmm1, xmm0
+pcmpeqd xmm1, xmmword ptr [r13 + 0x1f0]
+movmskps eax, xmm1
 test eax, eax
 jne L
@@ -378,11 +376,11 @@
 jne L
 mov rdx, qword ptr [r13 + 0x248]
-test rdx, rdx
-je L
 mov eax, 0x38156425
 movd xmm0, eax
 pshufd xmm0, xmm0, 0
-jmp L
-nop dword ptr [rax + rax]
+test rdx, rdx
+jne L
+jmp L
+nop word ptr [rax + rax]
 movdqa xmm1, xmm0
 pcmpeqd xmm1, xmmword ptr [rdx + 0x20]
@@ -403,8 +401,8 @@
 test eax, eax
 je L
-xor esi, esi
-lea rdi, [D]
-add esi, dword ptr [rdi + rax*4]
-movsxd rax, esi
+xor ecx, ecx
+lea rsi, [D]
+add ecx, dword ptr [rsi + rax*4]
+movsxd rax, ecx
 cmp rax, 0xb
 ja L
@@ -427,57 +425,10 @@
 xor rax, rdx
 mov qword ptr [r13 + 0x458], rax
-test ecx, ecx
-movzx esi, r15b
-jne L
-movdqa xmm1, xmmword ptr [r13 + 0x1f0]
-mov eax, 0x38156425
-movd xmm0, eax
-pshufd xmm0, xmm0, 0
-pcmpeqd xmm1, xmm0
-movmskps ecx, xmm1
-test ecx, ecx
-jne L
-pcmpeqd xmm0, xmmword ptr [r13 + 0x200]
-mov eax, 2
-movmskps ecx, xmm0
-test ecx, ecx
-jne L
-mov rcx, qword ptr [r13 + 0x248]
-mov eax, 0x38156425
-movd xmm0, eax
-pshufd xmm0, xmm0, 0
-test rcx, rcx
-mov rdx, rcx
-jne L
-jmp L
-nop dword ptr [rax]
-movdqa xmm1, xmm0
-pcmpeqd xmm1, xmmword ptr [rdx + 0x20]
-movmskps eax, xmm1
-test eax, eax
-jne L
-movdqa xmm1, xmm0
-pcmpeqd xmm1, xmmword ptr [rdx + 0x30]
-movmskps eax, xmm1
-test eax, eax
-jne L
-mov rdx, qword ptr [rdx]
-test rdx, rdx
-je L
-movdqa xmm1, xmm0
-pcmpeqd xmm1, xmmword ptr [rdx + 0x10]
-movmskps eax, xmm1
-test eax, eax
-je L
-xor edi, edi
-lea r9, [D]
-add edi, dword ptr [r9 + rax*4]
-movsxd rax, edi
-cmp rax, 0xb
-ja L
-lea rax, [rdx + rax*4 + 0x40]
+movzx edx, r15b
+mov esi, 0x38156425
+mov rdi, r12
+call F
+movabs rax, 0x38156425e0559094
 movabs rdx, 0x94d049bb133111eb
-mov dword ptr [rax], esi
-movabs rax, 0x38156425e0559094
 movdqa xmm1, xmmword ptr [r13 + 0xd0]
```
(ещё 491 строк диффа: so-query.py fdiff libclient.so 0x6014b00)

### изменена: 0x60234d0 (9839 байт) вызывается из: CRenderingPipelineDota3DSkybox::vfunc#0 | строки: "Post Process"; "Translucent Forward"
было: 0x601f810 (10113 байт)
- числа в инструкциях: −0 −0 −4 −8 −0xb −0xb −1 −2 (и ещё 1)
- поля объектов: −0x10 −0x20 −0x30 −0x1e0 −0x1f0 −0x200 −0x248
- прямых вызовов: 55 → 56
- инструкций: 2223 → 2165
```diff
@@ -6,5 +6,4 @@
 movd xmm0, edi
 push r14
-mov r14, rsi
 pshufd xmm0, xmm0, 0
 push r13
@@ -14,4 +13,5 @@
 mov rcx, rax
 sub rsp, 0xa8
+mov qword ptr [rbp - 0x48], rsi
 mov qword ptr [rbp - 0x70], rdx
 movdqa xmm1, xmm0
@@ -146,5 +146,5 @@
 mov qword ptr [rbp - 0x60], rax
 mov eax, 0xc290cc2e
-mov r13, r8
+mov r14, r8
 mov rsi, r8
 movd xmm0, eax
@@ -207,4 +207,5 @@
 jne L
 jmp L
+nop dword ptr [rax]
 movdqa xmm1, xmm0
 pcmpeqd xmm1, xmmword ptr [rdx + 0x20]
@@ -313,5 +314,5 @@
 jne L
 jmp L
-nop word ptr [rax + rax]
+nop
 movdqa xmm1, xmm0
 pcmpeqd xmm1, xmmword ptr [rdx + 0x20]
@@ -450,26 +451,26 @@
 test r8, r8
 je L
-mov rax, qword ptr [r14]
-mov qword ptr [rbp - 0x48], r8
-mov rdi, r14
+mov rdi, qword ptr [rbp - 0x48]
+mov qword ptr [rbp - 0xa8], r8
+mov rax, qword ptr [rdi]
 call qword ptr [rax + 0xd0]
-mov r8, qword ptr [rbp - 0x48]
+mov r8, qword ptr [rbp - 0xa8]
 test al, 2
 jne L
+mov rdi, qword ptr [rbp - 0x48]
+lea r13, [rbp - 0x34]
+sub rsp, 8
 mov edx, dword ptr [rbx + 4]
-lea rcx, [rbp - 0x34]
-sub rsp, 8
-mov rdi, qword ptr [rbp - 0x70]
-mov qword ptr [rbp - 0x48], rcx
-lea rsi, [S:"Post Process"]
-mov rax, qword ptr [r14]
+mov rcx, r13
+mov rsi, qword ptr [rbp - 0x70]
+mov rax, qword ptr [rdi]
 mov rax, qword ptr [rax + 0x68]
 mov dword ptr [rbp - 0x34], 0
-push rdi
-push rdi
+push rsi
+push rsi
 push rdx
-mov rdx, rdi
+mov rdx, rsi
 mov r9d, dword ptr [rbx]
-mov rdi, r14
+lea rsi, [S:"Post Process"]
 call rax
 mov rdi, qword ptr [rbp - 0x60]
@@ -501,7 +502,7 @@
 mov qword ptr [rbp - 0xa8], rax
 je L
-mov rsi, qword ptr [rbp - 0x48]
 lea r12, [rbx + 0x1e0]
 mov edx, 0x38156425
+mov rsi, r13
 mov rdi, r12
 call F
@@ -531,5 +532,5 @@
 call F
 movzx edx, r15b
-mov rsi, qword ptr [rbp - 0x48]
+mov rsi, r13
 mov rdi, r12
 movabs rax, 0x38156425e0559094
@@ -578,5 +579,5 @@
 pshufd xmm0, xmm0, 0
 movdqa xmm1, xmm0
-pcmpeqd xmm1, xmmword ptr [r13]
+pcmpeqd xmm1, xmmword ptr [r14]
 movmskps eax, xmm1
 test eax, eax
@@ -584,9 +585,9 @@
 movdqa xmm1, xmm0
 mov edx, 4
-pcmpeqd xmm1, xmmword ptr [r13 + 0x10]
-movmskps eax, xmm1
-test eax, eax
-jne L
-mov rax, qword ptr [r13 + 0xa8]
+pcmpeqd xmm1, xmmword ptr [r14 + 0x10]
+movmskps eax, xmm1
+test eax, eax
+jne L
+mov rax, qword ptr [r14 + 0xa8]
 test rax, rax
 je L
@@ -614,12 +615,12 @@
 movq xmm1, qword ptr [rbp - 0x98]
 call F
+mov edx, 0x99048fd2
+mov rsi, r13
+mov rdi, r12
 mov rax, qword ptr [D]
-mov edx, 0x99048fd2
-mov rdi, r12
```
(ещё 655 строк диффа: so-query.py fdiff libclient.so 0x60234d0)

### изменена: 0x60307a0 (47961 байт) CRenderingPipelineDota::vfunc#0 | строки: "rtOutputColorFP16"; "setting.shaderquality"; "rtPreDistortionDepth"; "rtLocalOutputDepth"; "rtDotaFowBuffer"; "_rt_minimap_rt.vtex"; "rtDotaMiniMapFowBuffer"; "Fow: Draw MiniMap"
было: 0x602cc20 (48025 байт)
- числа в инструкциях: +0x1038 −1 −1 −4 −0x103b
- поля объектов: −0x708 −0x708 −0x708 −0x718 −0x710
- инструкций: 9217 → 9203
```diff
@@ -1164,5 +1164,5 @@
 sub rsp, 8
 lea rax, [S:"AddLayersToView"]
-mov dword ptr [rbp - 0x1638], 0x103b
+mov dword ptr [rbp - 0x1638], 0x1038
 mov qword ptr [rbp - 0x1630], rax
 movzx eax, word ptr [rbp - 0x1594]
@@ -1588,9 +1588,9 @@
 mov qword ptr [rbp - 0x17d8], rax
 lea rax, [S:"DotaCrystal"]
-mov qword ptr [rbp - 0x1898], rax
-add rax, 4
 mov qword ptr [rbp - 0x1790], rax
 add rax, 4
 mov qword ptr [rbp - 0x17f0], rax
+add rax, 4
+mov qword ptr [rbp - 0x1898], rax
 mov rax, qword ptr [r15]
 lea rsi, [S:"Crystal Frontfaces"]
@@ -1647,5 +1647,5 @@
 mov rdi, r14
 call F
-mov rdi, qword ptr [rbp - 0x1898]
+mov rdi, qword ptr [rbp - 0x1790]
 mov esi, 0x3141592d
 movabs rcx, 0xea1931c3790c336e
@@ -1654,8 +1654,8 @@
 mov qword ptr [rbp - 0x1870], rcx
 call F
-mov rdi, qword ptr [rbp - 0x1790]
+mov rdi, qword ptr [rbp - 0x17f0]
 mov esi, eax
 call F
-mov rdi, qword ptr [rbp - 0x17f0]
+mov rdi, qword ptr [rbp - 0x1898]
 mov esi, eax
 call F
@@ -2247,17 +2247,17 @@
 mov rsi, qword ptr [rax]
 call F
+mov rdx, qword ptr [rbp - 0x1768]
 mov rcx, rbx
-mov rdi, r15
-mov rdx, qword ptr [rbp - 0x1768]
+mov r8d, 1
 lea rsi, [S:"Background Image"]
-mov r8d, 1
+mov rdi, r15
 call r12
+mov ecx, dword ptr [rbp - 0x17f0]
 mov rdx, qword ptr [rbp - 0x1728]
-mov ecx, dword ptr [rbp - 0x17f0]
 mov byte ptr [rax + 0x98], 1
-mov rbx, qword ptr [rbp - 0x1790]
+mov dword ptr [rax + 0x50], ecx
+mov rcx, qword ptr [rbp - 0x1790]
 mov qword ptr [rax + 0xa0], rdx
-mov dword ptr [rax + 0x50], ecx
-mov qword ptr [rax + 0x58], rbx
+mov qword ptr [rax + 0x58], rcx
 mov rax, qword ptr [r15]
 lea rsi, [S:"Decals"]
@@ -4276,9 +4276,9 @@
 xor r13d, r13d
 lea rax, [S:"DotaCrystal"]
-mov qword ptr [rbp - 0x1898], rax
-add rax, 4
 mov qword ptr [rbp - 0x1790], rax
 add rax, 4
 mov qword ptr [rbp - 0x17f0], rax
+add rax, 4
+mov qword ptr [rbp - 0x1898], rax
 mov eax, dword ptr [rbp - 0x18c8]
 test eax, eax
@@ -4344,12 +4344,7 @@
 xor rcx, qword ptr [rbx + 0x458]
 mov rdi, rax
-mov qword ptr [rbp - 0x1898], rax
+mov qword ptr [rbp - 0x1790], rax
 mov qword ptr [rbx + 0x458], rcx
 mov qword ptr [rbp - 0x18c8], rcx
-call F
-mov esi, eax
-lea rax, [D]
-mov rdi, rax
-mov qword ptr [rbp - 0x1790], rax
 call F
 mov esi, eax
@@ -4357,4 +4352,9 @@
 mov rdi, rax
 mov qword ptr [rbp - 0x17f0], rax
+call F
+mov esi, eax
+lea rax, [D]
+mov rdi, rax
+mov qword ptr [rbp - 0x1898], rax
 call F
 mov rsi, qword ptr [rbp - 0x1760]
@@ -4493,10 +4493,10 @@
 test eax, eax
 cmovg r12d, eax
+mov ebx, ecx
 test ecx, ecx
+mov rcx, qword ptr [rbp - 0x17d0]
 mov eax, 1
-cmovle ecx, eax
+cmovle ebx, eax
 test r14, r14
-mov ebx, ecx
-mov rcx, qword ptr [rbp - 0x17d0]
 mov eax, dword ptr [rcx + 0x50]
 mov edx, dword ptr [rcx + 0x54]
@@ -4869,11 +4869,11 @@
 mov rax, qword ptr [rdi]
 call qword ptr [rax + 0x1a8]
-mov byte ptr [rbp - 0x1660], 0
-mov rcx, qword ptr [rbp - 0x17d8]
-mov dword ptr [rbp - 0x1550], 0xffffffff
+mov byte ptr [rbp - 0x16a0], 0
+mov rdx, qword ptr [rbp - 0x17d8]
```
(ещё 466 строк диффа: so-query.py fdiff libclient.so 0x60307a0)

### изменена: 0x6041040 (2805 байт) | строки: "_popup"; "_comic"; "_externalcomic"; "_video"; "_popupimage"; "_if"; "_else"; "_actionswipe"
было: 0x603d500 (2781 байт)
- прямых вызовов: 71 → 72
- инструкций: 586 → 593
```diff
@@ -410,5 +410,4 @@
 jmp L
 mov rdi, r13
-mov r15d, 9
 call F
 mov rsi, rbx
@@ -434,6 +433,14 @@
 mov rdi, r12
 call F
+lea rsi, [D]
+test rax, rax
+je L
+xor ecx, ecx
+xor edx, edx
+mov rdi, rax
+call F
+mov rsi, rax
 lea rdi, [r13 + 0x28]
-mov rsi, rax
+mov r15d, 9
 call F
 mov rdi, qword ptr [rbp - 0x78]
```

### изменена: 0x3c855f0 (355 байт) | строки: "CUtlSymbolLarge"; "C_NetworkUtlVectorBase"
- код тот же, но вызывает другую функцию: было 0x3c851c0, стало 0x3c882c0

### изменена: 0x4c4f3c0 (26 байт) CDOTA_Modifier_Shredder_Exposure_Therapy::vfunc#88
- код тот же, но вызывает другую функцию: было 0x4c89df0, стало 0x4c8cf50

### изменена: 0x4c4fee0 (76 байт) CDOTA_Modifier_Slark_Pounce_Leash::vfunc#88
- код тот же, но вызывает другую функцию: было 0x4c89eb0, стало 0x4c8d010

### изменена: 0x4c4ff60 (76 байт) CDOTA_Modifier_Slark_EssenceShift::vfunc#88
- код тот же, но вызывает другую функцию: было 0x4c89e70, стало 0x4c8cfd0

### изменена: 0x4c50250 (51 байт) CDOTA_Modifier_Slark_EssenceShift_Permanent_Debuff::vfunc#88
- код тот же, но вызывает другую функцию: было 0x4c89ed0, стало 0x4c8d030

### изменена: 0x4c504d0 (126 байт) CDOTA_Modifier_Slark_ShadowDance_PassiveRegen::vfunc#88
- код тот же, но вызывает другую функцию: было 0x4c89f10, стало 0x4c8d070

### изменена: 0x4c50ed0 (220 байт) CDOTA_Modifier_Snapfire_MortimerKisses::vfunc#88
- код тот же, но вызывает другую функцию: было 0x4c89fb0, стало 0x4c8d110

### изменена: 0x4c51600 (151 байт) CDOTA_Modifier_Snapfire_LilShredder_Buff::vfunc#88
- код тот же, но вызывает другую функцию: было 0x4c89fd0, стало 0x4c8d130

### изменена: 0x4c51730 (51 байт) CDOTA_Modifier_Snapfire_LilShredder_Attack::vfunc#88
- код тот же, но вызывает другую функцию: было 0x4c8a030, стало 0x4c8d190

### изменена: 0x4c518c0 (51 байт) CDOTA_Modifier_Snapfire_GobbleUp_BellyHasUnit::vfunc#88
- код тот же, но вызывает другую функцию: было 0x4c8a050, стало 0x4c8d1b0

### изменена: 0x4c51ac0 (101 байт) CDOTA_Modifier_Snapfire_Buckshot::vfunc#88
- код тот же, но вызывает другую функцию: было 0x4c8a090, стало 0x4c8d1f0

### изменена: 0x4c51c50 (51 байт) CDOTA_Modifier_Techies_Suicide_RespawnTime::vfunc#88
- код тот же, но вызывает другую функцию: было 0x4c8a110, стало 0x4c8d270

### изменена: 0x4c51d20 (51 байт) CDOTA_Modifier_Techies_ReactiveTazer::vfunc#88
- код тот же, но вызывает другую функцию: было 0x4c8a130, стало 0x4c8d290

### изменена: 0x4c52250 (151 байт) CDOTA_Modifier_Techies_LandMine::vfunc#88
- код тот же, но вызывает другую функцию: было 0x4c8a150, стало 0x4c8d2b0

### изменена: 0x4c52790 (98 байт) CDOTA_Modifier_Techies_RemoteMine::vfunc#88
- код тот же, но вызывает другую функцию: было 0x4c8a1b0, стало 0x4c8d310

### изменена: 0x4c53010 (76 байт) CDOTA_Modifier_Techies_MutuallyAssuredDestruction::vfunc#88
- код тот же, но вызывает другую функцию: было 0x4c8a1f0, стало 0x4c8d350

### изменена: 0x4c53d60 (76 байт) CDOTA_Modifier_Terrorblade_Dark_Unity::vfunc#88
- код тот же, но вызывает другую функцию: было 0x4c8a210, стало 0x4c8d370

### изменена: 0x4c53e10 (162 байт) CDOTA_Modifier_Treant_EyesInTheForest_Thinker::vfunc#88
- код тот же, но вызывает другую функцию: было 0x4c8a250, стало 0x4c8d3b0

### изменена: 0x4c54520 (76 байт) CDOTA_Modifier_Treant_LeechSeedPassive::vfunc#88
- код тот же, но вызывает другую функцию: было 0x4c8a2b0, стало 0x4c8d410

### изменена: 0x4c545b0 (51 байт) CDOTA_Modifier_Treant_LeechSeed::vfunc#88
- код тот же, но вызывает другую функцию: было 0x4c8a310, стало 0x4c8d470

### изменена: 0x4c549b0 (175 байт) CDOTA_Modifier_Treant_SuperBloom::vfunc#88
- код тот же, но вызывает другую функцию: было 0x4c8a350, стало 0x4c8d4b0

### изменена: 0x4c54c00 (126 байт) CDOTA_Modifier_TrollWarlord_BerserkersRage::vfunc#88
- код тот же, но вызывает другую функцию: было 0x4c8a370, стало 0x4c8d4d0

### изменена: 0x4c55150 (48 байт) CDOTA_Modifier_TrollWarlord_WhirlingAxes_Blind::vfunc#88
- код тот же, но вызывает другую функцию: было 0x4c8a3b0, стало 0x4c8d510

### изменена: 0x4c55220 (101 байт) CDOTA_Modifier_TrollWarlord_Fervor::vfunc#88
- код тот же, но вызывает другую функцию: было 0x4c8a3d0, стало 0x4c8d530

### изменена: 0x4c55320 (173 байт) CDOTA_Modifier_TrollWarlord_BattleTrance::vfunc#88
- код тот же, но вызывает другую функцию: было 0x4c8a410, стало 0x4c8d570

### изменена: 0x4c559f0 (51 байт) CDOTA_Modifier_Tusk_Snowball_Movement::vfunc#88
- код тот же, но вызывает другую функцию: было 0x4c8a450, стало 0x4c8d5b0

### изменена: 0x4c55c10 (126 байт) CDOTA_Modifier_Tusk_FrozenSigil_Aura::vfunc#88
- код тот же, но вызывает другую функцию: было 0x4c8a490, стало 0x4c8d5f0

### изменена: 0x4c55e50 (251 байт) CDOTA_Modifier_Tusk_WalrusPunch::vfunc#88
- код тот же, но вызывает другую функцию: было 0x4c8a590, стало 0x4c8d6f0

### изменена: 0x4c56490 (51 байт) CDOTA_Modifier_Tusk_Tag_Team::vfunc#88
- код тот же, но вызывает другую функцию: было 0x4c8a5b0, стало 0x4c8d710

### изменена: 0x4c56db0 (76 байт) CDOTA_Modifier_Undying_Tombstone_Zombie_Deathstrike::vfunc#88
- код тот же, но вызывает другую функцию: было 0x4c8a5f0, стало 0x4c8d750

### изменена: 0x4c56f20 (176 байт) CDOTA_Modifier_Undying_Tombstone_Zombie_Modifier::vfunc#88
- код тот же, но вызывает другую функцию: было 0x4c8a670, стало 0x4c8d7d0

### изменена: 0x4c57370 (51 байт) CDOTA_Modifier_Undying_FleshGolem_Intrinsic::vfunc#88
- код тот же, но вызывает другую функцию: было 0x4c8a6d0, стало 0x4c8d830

### изменена: 0x4c57420 (151 байт) CDOTA_Modifier_Undying_FleshGolem::vfunc#88
- код тот же, но вызывает другую функцию: было 0x4c8a710, стало 0x4c8d870

### изменена: 0x4c57880 (151 байт) CDOTA_Modifier_Undying_Bite::vfunc#88
- код тот же, но вызывает другую функцию: было 0x4c8a750, стало 0x4c8d8b0

### изменена: 0x4c581b0 (51 байт) CDOTA_Modifier_Visage_GravekeepersCloak::vfunc#88
- код тот же, но вызывает другую функцию: было 0x4c8a7d0, стало 0x4c8d930

### изменена: 0x4c58400 (73 байт) CDOTA_Modifier_Visage_SummonFamiliars_Talents::vfunc#88
- код тот же, но вызывает другую функцию: было 0x4c8a7f0, стало 0x4c8d950

### изменена: 0x4c58500 (48 байт) CDOTA_Modifier_Visage_SummonFamiliars_DamageCharge::vfunc#88
- код тот же, но вызывает другую функцию: было 0x4c8a810, стало 0x4c8d970

### изменена: 0x4c58a50 (101 байт) CDOTA_Modifier_Visage_Silent_As_The_GravePassive::vfunc#88
- код тот же, но вызывает другую функцию: было 0x4c8a850, стало 0x4c8d9b0

### изменена: 0x4c58b20 (117 байт) CDOTA_Modifier_Visage_Silent_As_The_Grave::vfunc#88
- код тот же, но вызывает другую функцию: было 0x4c8a8b0, стало 0x4c8da10

### изменена: 0x4c58cd0 (76 байт) CDOTA_Modifier_Visage_Lurker::vfunc#88
- код тот же, но вызывает другую функцию: было 0x4c8a8d0, стало 0x4c8da30

### изменена: 0x4c59230 (51 байт) CDOTA_Modifier_VoidSpirit_AstralStep_Caster::vfunc#88
- код тот же, но вызывает другую функцию: было 0x4c8a910, стало 0x4c8da70

### изменена: 0x4c59790 (207 байт) CDOTA_Modifier_Winter_Wyvern_Arctic_Burn_Flight::vfunc#88
- код тот же, но вызывает другую функцию: было 0x4c8a950, стало 0x4c8dab0

### изменена: 0x4c59ae0 (51 байт) CDOTA_Modifier_Winter_Wyvern_Cold_Embrace::vfunc#88
- код тот же, но вызывает другую функцию: было 0x4c8a970, стало 0x4c8dad0

### изменена: 0x4c59cf0 (51 байт) CDOTA_Modifier_Winter_Wyvern_Winters_Curse_Aura::vfunc#88
- код тот же, но вызывает другую функцию: было 0x4c8a990, стало 0x4c8daf0

### изменена: 0x4c59f90 (51 байт) CDOTA_Modifier_Winter_Wyvern_Essence_Of_The_Blueheart::vfunc#88
- код тот же, но вызывает другую функцию: было 0x4c8aa10, стало 0x4c8db70

### изменена: 0x4c5a120 (51 байт) CDOTA_Modifier_Winter_Wyvern_Eldwurm_Scholar::vfunc#88
- код тот же, но вызывает другую функцию: было 0x4c8aa30, стало 0x4c8db90

### изменена: 0x4c5a3b0 (176 байт) CDOTA_Modifier_Wisp_Tether::vfunc#88
- код тот же, но вызывает другую функцию: было 0x4c8aa50, стало 0x4c8dbb0

### изменена: 0x4c5ac90 (51 байт) CDOTA_Modifier_Wisp_Relocate_Thinker::vfunc#88
- код тот же, но вызывает другую функцию: было 0x4c8aaf0, стало 0x4c8dc50

### изменена: 0x5e11a10 (151 байт) | строки: "TrackedStatID_t"; "TrackedStatValue_t"
- код тот же, но вызывает другую функцию: было 0x5d8f0b0, стало 0x5d92230

### изменена: 0x5e11ab0 (634 байт) | строки: "GameTime_t"; "sPlayerSnapshot"; "CUtlVector"
- код тот же, но вызывает другую функцию: было 0x5d8f080, стало 0x5d92200

### изменена: 0x5e13b60 (350 байт)
- код тот же, но вызывает другую функцию: было 0x5d8f0a0, стало 0x5d92220

### изменена: 0x5e17790 (385 байт)
- код тот же, но вызывает другую функцию: было 0x5d8f0c0, стало 0x5d92240

### изменена: 0x5e18240 (429 байт) | строки: "PlayerID_t"
- код тот же, но вызывает другую функцию: было 0x5d8f0e0, стало 0x5d92260

### изменена: 0x5e183f0 (429 байт) | строки: "DOTATeam_t"
- код тот же, но вызывает другую функцию: было 0x5d8f0d0, стало 0x5d92250

### изменена: 0x5ec8090 (419 байт) | строки: "C_DOTASpectatorGraphManager"
- код тот же, но вызывает другую функцию: было 0x5d8f090, стало 0x5d92210

### изменена: 0x5ecb1f0 (2999 байт) | строки: "scripts/tracked_stats_player.vdata"; "scripts/tracked_stats_player_staging.vdata"; "scripts/tracked_stats_team.vdata"; "scripts/tracked_stats_team_staging.vdata"; "scripts/tracked_stats_match.vdata"; "scripts/tracked_stats_match_staging.vdata"
- код тот же, но вызывает другую функцию: было 0x5de0840, стало 0x5de3b60

### изменена: 0x5f15620 (476 байт) | строки: "C_DOTA_Ability_Special_Bonus_HP_100"
- код тот же, но вызывает другую функцию: было 0x5dd9f40, стало 0x5ddd240

### изменена: 0x5f15800 (428 байт) | строки: "C_DOTA_Ability_Special_Bonus_HP_125"
- код тот же, но вызывает другую функцию: было 0x5dd9ec0, стало 0x5ddd1c0

### изменена: 0x5f159b0 (428 байт) | строки: "C_DOTA_Ability_Special_Bonus_HP_150"
- код тот же, но вызывает другую функцию: было 0x5dd9e40, стало 0x5ddd140

### изменена: 0x5f15b60 (428 байт) | строки: "C_DOTA_Ability_Special_Bonus_HP_175"
- код тот же, но вызывает другую функцию: было 0x5dd9dc0, стало 0x5ddd0c0

### изменена: 0x5f15d10 (428 байт) | строки: "C_DOTA_Ability_Special_Bonus_HP_200"
- код тот же, но вызывает другую функцию: было 0x5dd9d40, стало 0x5ddd040

### изменена: 0x5f15ec0 (428 байт) | строки: "C_DOTA_Ability_Special_Bonus_HP_225"
- код тот же, но вызывает другую функцию: было 0x5dd9cc0, стало 0x5ddcfc0

### изменена: 0x5f16070 (428 байт) | строки: "C_DOTA_Ability_Special_Bonus_HP_250"
- код тот же, но вызывает другую функцию: было 0x5dd9c40, стало 0x5ddcf40

### изменена: 0x5f16220 (428 байт) | строки: "C_DOTA_Ability_Special_Bonus_HP_275"
- код тот же, но вызывает другую функцию: было 0x5dd9bc0, стало 0x5ddcec0

### изменена: 0x5f163d0 (428 байт) | строки: "C_DOTA_Ability_Special_Bonus_HP_300"
- код тот же, но вызывает другую функцию: было 0x5dd9b40, стало 0x5ddce40

### изменена: 0x5f16580 (428 байт) | строки: "C_DOTA_Ability_Special_Bonus_HP_325"
- код тот же, но вызывает другую функцию: было 0x5dd9ac0, стало 0x5ddcdc0

### изменена: 0x5f16730 (428 байт) | строки: "C_DOTA_Ability_Special_Bonus_HP_350"
- код тот же, но вызывает другую функцию: было 0x5dd9a40, стало 0x5ddcd40

### изменена: 0x5f168e0 (428 байт) | строки: "C_DOTA_Ability_Special_Bonus_HP_375"
- код тот же, но вызывает другую функцию: было 0x5dd99c0, стало 0x5ddccc0

### изменена: 0x5f16a90 (428 байт) | строки: "C_DOTA_Ability_Special_Bonus_HP_400"
- код тот же, но вызывает другую функцию: было 0x5dd9940, стало 0x5ddcc40

### изменена: 0x5f16c40 (428 байт) | строки: "C_DOTA_Ability_Special_Bonus_HP_450"
- код тот же, но вызывает другую функцию: было 0x5dd98c0, стало 0x5ddcbc0

### изменена: 0x5f16df0 (428 байт) | строки: "C_DOTA_Ability_Special_Bonus_HP_475"
- код тот же, но вызывает другую функцию: было 0x5dd9840, стало 0x5ddcb40

### изменена: 0x5f16fa0 (428 байт) | строки: "C_DOTA_Ability_Special_Bonus_HP_500"
- код тот же, но вызывает другую функцию: было 0x5dd97c0, стало 0x5ddcac0

### изменена: 0x5f17150 (428 байт) | строки: "C_DOTA_Ability_Special_Bonus_HP_600"
- код тот же, но вызывает другую функцию: было 0x5dd9740, стало 0x5ddca40

### изменена: 0x5f17300 (428 байт) | строки: "C_DOTA_Ability_Special_Bonus_HP_650"
- код тот же, но вызывает другую функцию: было 0x5dd96c0, стало 0x5ddc9c0

### изменена: 0x5f174b0 (428 байт) | строки: "C_DOTA_Ability_Special_Bonus_HP_700"
- код тот же, но вызывает другую функцию: было 0x5dd9640, стало 0x5ddc940

### изменена: 0x5f17660 (428 байт) | строки: "C_DOTA_Ability_Special_Bonus_HP_800"
- код тот же, но вызывает другую функцию: было 0x5dd95c0, стало 0x5ddc8c0

### изменена: 0x5f17810 (428 байт) | строки: "C_DOTA_Ability_Special_Bonus_HP_900"
- код тот же, но вызывает другую функцию: было 0x5dd9540, стало 0x5ddc840

### изменена: 0x5f179c0 (428 байт) | строки: "C_DOTA_Ability_Special_Bonus_MP_100"
- код тот же, но вызывает другую функцию: было 0x5dd9440, стало 0x5ddc740

### изменена: 0x5f17b70 (428 байт) | строки: "C_DOTA_Ability_Special_Bonus_MP_125"
- код тот же, но вызывает другую функцию: было 0x5dd93c0, стало 0x5ddc6c0

### изменена: 0x5f17d20 (428 байт) | строки: "C_DOTA_Ability_Special_Bonus_MP_150"
- код тот же, но вызывает другую функцию: было 0x5dd9340, стало 0x5ddc640

### изменена: 0x5f17ed0 (428 байт) | строки: "C_DOTA_Ability_Special_Bonus_MP_175"
- код тот же, но вызывает другую функцию: было 0x5dd92c0, стало 0x5ddc5c0

### изменена: 0x5f18080 (428 байт) | строки: "C_DOTA_Ability_Special_Bonus_MP_200"
- код тот же, но вызывает другую функцию: было 0x5dd9240, стало 0x5ddc540

### изменена: 0x5f18230 (428 байт) | строки: "C_DOTA_Ability_Special_Bonus_MP_225"
- код тот же, но вызывает другую функцию: было 0x5dd91c0, стало 0x5ddc4c0

### изменена: 0x5f183e0 (428 байт) | строки: "C_DOTA_Ability_Special_Bonus_MP_250"
- код тот же, но вызывает другую функцию: было 0x5dd9140, стало 0x5ddc440

### изменена: 0x5f18590 (428 байт) | строки: "C_DOTA_Ability_Special_Bonus_MP_275"
- код тот же, но вызывает другую функцию: было 0x5dd90c0, стало 0x5ddc3c0

### изменена: 0x5f18740 (428 байт) | строки: "C_DOTA_Ability_Special_Bonus_MP_300"
- код тот же, но вызывает другую функцию: было 0x5dd9040, стало 0x5ddc340

### изменена: 0x5f188f0 (428 байт) | строки: "C_DOTA_Ability_Special_Bonus_MP_350"
- код тот же, но вызывает другую функцию: было 0x5dd8fc0, стало 0x5ddc2c0

### изменена: 0x5f18aa0 (428 байт) | строки: "C_DOTA_Ability_Special_Bonus_MP_400"
- код тот же, но вызывает другую функцию: было 0x5dd8f40, стало 0x5ddc240

### изменена: 0x5f18c50 (428 байт) | строки: "C_DOTA_Ability_Special_Bonus_MP_500"
- код тот же, но вызывает другую функцию: было 0x5dd8ec0, стало 0x5ddc1c0

### изменена: 0x5f18e00 (428 байт) | строки: "C_DOTA_Ability_Special_Bonus_MP_600"
- код тот же, но вызывает другую функцию: было 0x5dd8e40, стало 0x5ddc140

### изменена: 0x5f18fb0 (428 байт) | строки: "C_DOTA_Ability_Special_Bonus_MP_700"
- код тот же, но вызывает другую функцию: было 0x5dd8dc0, стало 0x5ddc0c0

### изменена: 0x5f19160 (428 байт) | строки: "C_DOTA_Ability_Special_Bonus_MP_800"
- код тот же, но вызывает другую функцию: было 0x5dd8d40, стало 0x5ddc040

### изменена: 0x5f19310 (428 байт) | строки: "C_DOTA_Ability_Special_Bonus_Haste"
- код тот же, но вызывает другую функцию: было 0x5dd7840, стало 0x5ddab40

### изменена: 0x5f1bb90 (428 байт) | строки: "C_DOTA_Ability_Special_Bonus_Base"
- код тот же, но вызывает другую функцию: было 0x5dda3c0, стало 0x5ddd6c0

### изменена: 0x5f1c760 (444 байт) | строки: "C_DOTA_Ability_Special_Bonus_Undefined"
- код тот же, но вызывает другую функцию: было 0x5dda340, стало 0x5ddd640

### изменена: 0x5f1c920 (444 байт) | строки: "C_DOTA_Ability_Special_Bonus_Cleave_15"
- код тот же, но вызывает другую функцию: было 0x5dd7e40, стало 0x5ddb140

### изменена: 0x5f1cae0 (444 байт) | строки: "C_DOTA_Ability_Special_Bonus_Cleave_20"
- код тот же, но вызывает другую функцию: было 0x5dd7dc0, стало 0x5ddb0c0

### изменена: 0x5f1cca0 (444 байт) | строки: "C_DOTA_Ability_Special_Bonus_Cleave_25"
- код тот же, но вызывает другую функцию: было 0x5dd7d40, стало 0x5ddb040

### изменена: 0x5f1ce60 (444 байт) | строки: "C_DOTA_Ability_Special_Bonus_Cleave_30"
- код тот же, но вызывает другую функцию: было 0x5dd7cc0, стало 0x5ddafc0

### изменена: 0x5f1d020 (444 байт) | строки: "C_DOTA_Ability_Special_Bonus_Cleave_35"
- код тот же, но вызывает другую функцию: было 0x5dd7c40, стало 0x5ddaf40

### изменена: 0x5f1d1e0 (444 байт) | строки: "C_DOTA_Ability_Special_Bonus_Cleave_40"
- код тот же, но вызывает другую функцию: было 0x5dd7bc0, стало 0x5ddaec0

### изменена: 0x5f1d3a0 (444 байт) | строки: "C_DOTA_Ability_Special_Bonus_Cleave_60"
- код тот же, но вызывает другую функцию: было 0x5dd7b40, стало 0x5ddae40

### изменена: 0x5f1d560 (444 байт) | строки: "C_DOTA_Ability_Special_Bonus_Cleave_100"
- код тот же, но вызывает другую функцию: было 0x5dd7ac0, стало 0x5ddadc0

### изменена: 0x5f1d720 (444 байт) | строки: "C_DOTA_Ability_Special_Bonus_Cleave_130"
- код тот же, но вызывает другую функцию: было 0x5dd7a40, стало 0x5ddad40

### изменена: 0x5f1d8e0 (444 байт) | строки: "C_DOTA_Ability_Special_Bonus_Cleave_140"
- код тот же, но вызывает другую функцию: было 0x5dd79c0, стало 0x5ddacc0

### изменена: 0x5f1daa0 (444 байт) | строки: "C_DOTA_Ability_Special_Bonus_Cleave_150"
- код тот же, но вызывает другую функцию: было 0x5dd7940, стало 0x5ddac40

### изменена: 0x5f1dc60 (444 байт) | строки: "C_DOTA_Ability_Special_Bonus_Cleave_175"
- код тот же, но вызывает другую функцию: было 0x5dd78c0, стало 0x5ddabc0

### изменена: 0x5f1de20 (444 байт) | строки: "C_DOTA_Ability_Special_Bonus_TrueStrike"
- код тот же, но вызывает другую функцию: было 0x5dd77c0, стало 0x5ddaac0

### изменена: 0x5f1dfe0 (444 байт) | строки: "C_DOTA_Ability_Special_Bonus_Spell_Block_15"
- код тот же, но вызывает другую функцию: было 0x5dd75c0, стало 0x5dda8c0

### изменена: 0x5f1e1a0 (444 байт) | строки: "C_DOTA_Ability_Special_Bonus_Spell_Block_18"
- код тот же, но вызывает другую функцию: было 0x5dd7540, стало 0x5dda840

### изменена: 0x5f1e360 (444 байт) | строки: "C_DOTA_Ability_Special_Bonus_Spell_Block_20"
- код тот же, но вызывает другую функцию: было 0x5dd74c0, стало 0x5dda7c0

### изменена: 0x5f1e520 (444 байт) | строки: "C_DOTA_Ability_Special_Bonus_Mana_Break_15"
- код тот же, но вызывает другую функцию: было 0x5dd7440, стало 0x5dda740

### изменена: 0x5f1e6e0 (444 байт) | строки: "C_DOTA_Ability_Special_Bonus_Mana_Break_20"
- код тот же, но вызывает другую функцию: было 0x5dd73c0, стало 0x5dda6c0

### изменена: 0x5f1e8a0 (444 байт) | строки: "C_DOTA_Ability_Special_Bonus_Mana_Break_25"
- код тот же, но вызывает другую функцию: было 0x5dd7340, стало 0x5dda640

### изменена: 0x5f1ea60 (444 байт) | строки: "C_DOTA_Ability_Special_Bonus_Mana_Break_35"
- код тот же, но вызывает другую функцию: было 0x5dd72c0, стало 0x5dda5c0

### изменена: 0x5f1ec20 (444 байт) | строки: "C_DOTA_Ability_Special_Bonus_Mana_Break_40"
- код тот же, но вызывает другую функцию: было 0x5dd7240, стало 0x5dda540

### изменена: 0x5f1ede0 (444 байт) | строки: "C_DOTA_Ability_Special_Bonus_Spell_Immunity"
- код тот же, но вызывает другую функцию: было 0x5dd71c0, стало 0x5dda4c0

### изменена: 0x5f1efa0 (444 байт) | строки: "C_DOTA_Ability_Special_Bonus_HP_Regen_3"
- код тот же, но вызывает другую функцию: было 0x5dd7140, стало 0x5dda440

### изменена: 0x5f1f160 (444 байт) | строки: "C_DOTA_Ability_Special_Bonus_HP_Regen_4"
- код тот же, но вызывает другую функцию: было 0x5dd70c0, стало 0x5dda3c0

### изменена: 0x5f2c520 (428 байт) | строки: "C_DOTA_Ability_Special_Bonus_HP_1000"
- код тот же, но вызывает другую функцию: было 0x5dd94c0, стало 0x5ddc7c0

### изменена: 0x5f2c6d0 (428 байт) | строки: "C_DOTA_Ability_Special_Bonus_MP_1000"
- код тот же, но вызывает другую функцию: было 0x5dd8cc0, стало 0x5ddbfc0

### изменена: 0x5f348c0 (444 байт) | строки: "C_DOTA_Ability_Special_Bonus_Gold_lvl15_r"
- код тот же, но вызывает другую функцию: было 0x5dda2c0, стало 0x5ddd5c0

### изменена: 0x5f34a80 (444 байт) | строки: "C_DOTA_Ability_Special_Bonus_Gold_lvl20_r"
- код тот же, но вызывает другую функцию: было 0x5dda240, стало 0x5ddd540

### изменена: 0x5f34c40 (444 байт) | строки: "C_DOTA_Ability_Special_Bonus_Gold_lvl25_r"
- код тот же, но вызывает другую функцию: было 0x5dda1c0, стало 0x5ddd4c0

### изменена: 0x5f34e00 (444 байт) | строки: "C_DOTA_Ability_Special_Bonus_Gold_lvl10_l"
- код тот же, но вызывает другую функцию: было 0x5dda140, стало 0x5ddd440

### изменена: 0x5f34fc0 (444 байт) | строки: "C_DOTA_Ability_Special_Bonus_Gold_lvl15_l"
- код тот же, но вызывает другую функцию: было 0x5dda0c0, стало 0x5ddd3c0

### изменена: 0x5f35180 (444 байт) | строки: "C_DOTA_Ability_Special_Bonus_Gold_lvl20_l"
- код тот же, но вызывает другую функцию: было 0x5dda040, стало 0x5ddd340

### изменена: 0x5f35340 (444 байт) | строки: "C_DOTA_Ability_Special_Bonus_Gold_lvl25_l"
- код тот же, но вызывает другую функцию: было 0x5dd9fc0, стало 0x5ddd2c0

### изменена: 0x5f35500 (444 байт) | строки: "CDOTA_Ability_Special_Bonus_Corruption_25"
- код тот же, но вызывает другую функцию: было 0x5dd8040, стало 0x5ddb340

### изменена: 0x5f356c0 (444 байт) | строки: "C_DOTA_Ability_Special_Bonus_Corruption_3"
- код тот же, но вызывает другую функцию: было 0x5dd7fc0, стало 0x5ddb2c0

### изменена: 0x5f35880 (444 байт) | строки: "C_DOTA_Ability_Special_Bonus_Corruption_4"
- код тот же, но вызывает другую функцию: было 0x5dd7f40, стало 0x5ddb240

### изменена: 0x5f35a40 (444 байт) | строки: "C_DOTA_Ability_Special_Bonus_Corruption_5"
- код тот же, но вызывает другую функцию: было 0x5dd7ec0, стало 0x5ddb1c0

### изменена: 0x5f3d300 (452 байт) | строки: "C_DOTA_Ability_Special_Bonus_Base_Attack_Rate_1"
- код тот же, но вызывает другую функцию: было 0x5dd8c40, стало 0x5ddbf40

### изменена: 0x5f3d4d0 (452 байт) | строки: "C_DOTA_Ability_Special_Bonus_Reincarnation_200"
- код тот же, но вызывает другую функцию: было 0x5dd7740, стало 0x5ddaa40

### изменена: 0x5f3d6a0 (452 байт) | строки: "C_DOTA_Ability_Special_Bonus_Reincarnation_250"
- код тот же, но вызывает другую функцию: было 0x5dd76c0, стало 0x5dda9c0

### изменена: 0x5f3d870 (452 байт) | строки: "C_DOTA_Ability_Special_Bonus_Reincarnation_300"
- код тот же, но вызывает другую функцию: было 0x5dd7640, стало 0x5dda940

### изменена: 0x5f49a60 (444 байт) | строки: "C_DOTA_Ability_Special_Bonus_Attack_Speed_10"
- код тот же, но вызывает другую функцию: было 0x5dd8bc0, стало 0x5ddbec0

### изменена: 0x5f49c20 (444 байт) | строки: "C_DOTA_Ability_Special_Bonus_Attack_Speed_15"
- код тот же, но вызывает другую функцию: было 0x5dd8b40, стало 0x5ddbe40

### изменена: 0x5f49de0 (444 байт) | строки: "C_DOTA_Ability_Special_Bonus_Attack_Speed_20"
- код тот же, но вызывает другую функцию: было 0x5dd8ac0, стало 0x5ddbdc0

### изменена: 0x5f49fa0 (444 байт) | строки: "C_DOTA_Ability_Special_Bonus_Attack_Speed_25"
- код тот же, но вызывает другую функцию: было 0x5dd8a40, стало 0x5ddbd40

### изменена: 0x5f4a160 (444 байт) | строки: "C_DOTA_Ability_Special_Bonus_Attack_Speed_30"
- код тот же, но вызывает другую функцию: было 0x5dd89c0, стало 0x5ddbcc0

### изменена: 0x5f4a320 (444 байт) | строки: "C_DOTA_Ability_Special_Bonus_Attack_Speed_35"
- код тот же, но вызывает другую функцию: было 0x5dd8940, стало 0x5ddbc40

### изменена: 0x5f4a4e0 (444 байт) | строки: "C_DOTA_Ability_Special_Bonus_Attack_Speed_40"
- код тот же, но вызывает другую функцию: было 0x5dd88c0, стало 0x5ddbbc0

### изменена: 0x5f4a6a0 (444 байт) | строки: "C_DOTA_Ability_Special_Bonus_Attack_Speed_45"
- код тот же, но вызывает другую функцию: было 0x5dd8840, стало 0x5ddbb40

### изменена: 0x5f4a860 (444 байт) | строки: "C_DOTA_Ability_Special_Bonus_Attack_Speed_50"
- код тот же, но вызывает другую функцию: было 0x5dd87c0, стало 0x5ddbac0

### изменена: 0x5f4aa20 (444 байт) | строки: "C_DOTA_Ability_Special_Bonus_Attack_Speed_55"
- код тот же, но вызывает другую функцию: было 0x5dd8740, стало 0x5ddba40

### изменена: 0x5f4abe0 (444 байт) | строки: "C_DOTA_Ability_Special_Bonus_Attack_Speed_60"
- код тот же, но вызывает другую функцию: было 0x5dd86c0, стало 0x5ddb9c0

### изменена: 0x5f4ada0 (444 байт) | строки: "C_DOTA_Ability_Special_Bonus_Attack_Speed_70"
- код тот же, но вызывает другую функцию: было 0x5dd8640, стало 0x5ddb940

### изменена: 0x5f4af60 (444 байт) | строки: "C_DOTA_Ability_Special_Bonus_Attack_Speed_80"
- код тот же, но вызывает другую функцию: было 0x5dd85c0, стало 0x5ddb8c0

### изменена: 0x5f4b120 (444 байт) | строки: "C_DOTA_Ability_Special_Bonus_Attack_Speed_90"
- код тот же, но вызывает другую функцию: было 0x5dd8540, стало 0x5ddb840

### изменена: 0x5f586a0 (452 байт) | строки: "C_DOTA_Ability_Special_Bonus_Attack_Speed_100"
- код тот же, но вызывает другую функцию: было 0x5dd84c0, стало 0x5ddb7c0

### изменена: 0x5f58870 (452 байт) | строки: "C_DOTA_Ability_Special_Bonus_Attack_Speed_110"
- код тот же, но вызывает другую функцию: было 0x5dd8440, стало 0x5ddb740

### изменена: 0x5f58a40 (452 байт) | строки: "C_DOTA_Ability_Special_Bonus_Attack_Speed_120"
- код тот же, но вызывает другую функцию: было 0x5dd83c0, стало 0x5ddb6c0

### изменена: 0x5f58c10 (452 байт) | строки: "C_DOTA_Ability_Special_Bonus_Attack_Speed_140"
- код тот же, но вызывает другую функцию: было 0x5dd8340, стало 0x5ddb640

### изменена: 0x5f58de0 (452 байт) | строки: "C_DOTA_Ability_Special_Bonus_Attack_Speed_160"
- код тот же, но вызывает другую функцию: было 0x5dd82c0, стало 0x5ddb5c0

### изменена: 0x5f58fb0 (452 байт) | строки: "C_DOTA_Ability_Special_Bonus_Attack_Speed_175"
- код тот же, но вызывает другую функцию: было 0x5dd8240, стало 0x5ddb540

### изменена: 0x5f59180 (452 байт) | строки: "C_DOTA_Ability_Special_Bonus_Attack_Speed_200"
- код тот же, но вызывает другую функцию: было 0x5dd81c0, стало 0x5ddb4c0

### изменена: 0x5f59350 (452 байт) | строки: "C_DOTA_Ability_Special_Bonus_Attack_Speed_225"
- код тот же, но вызывает другую функцию: было 0x5dd8140, стало 0x5ddb440

### изменена: 0x5f59520 (452 байт) | строки: "C_DOTA_Ability_Special_Bonus_Attack_Speed_250"
- код тот же, но вызывает другую функцию: было 0x5dd80c0, стало 0x5ddb3c0

### изменена: 0x4c4f4e0 (26 байт) CDOTA_Modifier_Skywrath_Mage_Staff_Of_The_Scion::vfunc#88
- код тот же, но вызывает другую функцию: было 0x4c89e10, стало 0x4c8cf70

### изменена: 0x4c4f590 (26 байт) CDOTA_Modifier_Skywrath_Mage_Shard::vfunc#88
- код тот же, но вызывает другую функцию: было 0x4c89e30, стало 0x4c8cf90

### изменена: 0x4c4f7c0 (26 байт) CDOTA_Modifier_Skywrath_Mage_Arcane_Bolt_Lifesteal::vfunc#88
- код тот же, но вызывает другую функцию: было 0x4c89e50, стало 0x4c8cfb0

### изменена: 0x4c503e0 (26 байт) CDOTA_Modifier_Slark_ShadowDance_Passive::vfunc#88
- код тот же, но вызывает другую функцию: было 0x4c89ef0, стало 0x4c8d050

### изменена: 0x4c50b70 (76 байт) CDOTA_Modifier_Slark_SaltwaterShiv::vfunc#88
- код тот же, но вызывает другую функцию: было 0x4c89f90, стало 0x4c8d0f0

### изменена: 0x4c52410 (26 байт) CDOTA_Modifier_Techies_StasisTrap::vfunc#88
- код тот же, но вызывает другую функцию: было 0x4c8a190, стало 0x4c8d2f0

### изменена: 0x4c52cd0 (26 байт) CDOTA_Modifier_Techies_SnareTrap::vfunc#88
- код тот же, но вызывает другую функцию: было 0x4c8a1d0, стало 0x4c8d330

### изменена: 0x4c541e0 (51 байт) CDOTA_Modifier_Treant_NaturesGuise::vfunc#88
- код тот же, но вызывает другую функцию: было 0x4c8a270, стало 0x4c8d3d0

### изменена: 0x4c54700 (26 байт) CDOTA_Modifier_Treant_LivingArmor::vfunc#88, CDOTA_Modifier_Treant_LivingArmorPermanent::vfunc#88
- код тот же, но вызывает другую функцию: было 0x4c8a330, стало 0x4c8d490

### изменена: 0x4c55ac0 (26 байт) CDOTA_Modifier_Tusk_Snowball_Movement_Friendly::vfunc#88
- код тот же, но вызывает другую функцию: было 0x4c8a470, стало 0x4c8d5d0

### изменена: 0x4c56930 (26 байт) CDOTA_Modifier_Undying_Decay_Debuff::vfunc#88
- код тот же, но вызывает другую функцию: было 0x4c8a650, стало 0x4c8d7b0

### изменена: 0x4c570f0 (26 байт) CDOTA_Modifier_Undying_Tombstone_Bunker::vfunc#88
- код тот же, но вызывает другую функцию: было 0x4c8a690, стало 0x4c8d7f0

### изменена: 0x4c57190 (151 байт) CDOTA_Modifier_Undying_Tombstone_HP::vfunc#88
- код тот же, но вызывает другую функцию: было 0x4c8a6b0, стало 0x4c8d810

### изменена: 0x4c57760 (26 байт) CDOTA_Modifier_Undying_Tombstone_Death_Trigger::vfunc#88
- код тот же, но вызывает другую функцию: было 0x4c8a730, стало 0x4c8d890

### изменена: 0x4c57cd0 (26 байт) CDOTA_Modifier_Undying_CeaselessDirge::vfunc#88
- код тот же, но вызывает другую функцию: было 0x4c8a7b0, стало 0x4c8d910

### изменена: 0x4c58940 (26 байт) CDOTA_Modifier_Visage_Familiar_Innate::vfunc#88
- код тот же, но вызывает другую функцию: было 0x4c8a830, стало 0x4c8d990

### изменена: 0x4c58f80 (26 байт) CDOTA_Modifier_VoidSpirit_AetherRemnant_Pull::vfunc#88
- код тот же, но вызывает другую функцию: было 0x4c8a8f0, стало 0x4c8da50

### изменена: 0x4c59640 (26 байт) CDOTA_Modifier_VoidSpirit_Variant_Equilibrium::vfunc#88
- код тот же, но вызывает другую функцию: было 0x4c8a930, стало 0x4c8da90

### изменена: 0x4c59ec0 (76 байт) CDOTA_Modifier_Winter_Wyvern_Winters_Curse_Kill_Credit::vfunc#88
- код тот же, но вызывает другую функцию: было 0x4c8a9b0, стало 0x4c8db10

### изменена: 0x4c5a980 (26 байт) CDOTA_Modifier_Wisp_Spirits::vfunc#88
- код тот же, но вызывает другую функцию: было 0x4c8aad0, стало 0x4c8dc30

### изменена: 0x5dce640 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d86630, стало 0x5d897b0

### изменена: 0x5dce6c0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d86600, стало 0x5d89780

### изменена: 0x5dce740 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d865d0, стало 0x5d89750

### изменена: 0x5dce7c0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d865a0, стало 0x5d89720

### изменена: 0x5dce840 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d86570, стало 0x5d896f0

### изменена: 0x5dce8c0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d86540, стало 0x5d896c0

### изменена: 0x5dce940 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d86510, стало 0x5d89690

### изменена: 0x5dce9c0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d864e0, стало 0x5d89660

### изменена: 0x5dcea40 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d864b0, стало 0x5d89630

### изменена: 0x5dceac0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d86480, стало 0x5d89600

### изменена: 0x5dceb40 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d86450, стало 0x5d895d0

### изменена: 0x5dcebc0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d86420, стало 0x5d895a0

### изменена: 0x5dcec40 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d863f0, стало 0x5d89570

### изменена: 0x5dcecc0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d863c0, стало 0x5d89540

### изменена: 0x5dced40 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d86390, стало 0x5d89510

### изменена: 0x5dcedc0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d86360, стало 0x5d894e0

### изменена: 0x5dcee40 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d86330, стало 0x5d894b0

### изменена: 0x5dceec0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d86300, стало 0x5d89480

### изменена: 0x5dcef40 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d862d0, стало 0x5d89450

### изменена: 0x5dcefc0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d862a0, стало 0x5d89420

### изменена: 0x5dcf040 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d86270, стало 0x5d893f0

### изменена: 0x5dcf0c0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d86240, стало 0x5d893c0

### изменена: 0x5dcf140 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d86210, стало 0x5d89390

### изменена: 0x5dcf1c0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d861e0, стало 0x5d89360

### изменена: 0x5dcf240 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d861b0, стало 0x5d89330

### изменена: 0x5dcf2c0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d86180, стало 0x5d89300

### изменена: 0x5dcf340 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d86150, стало 0x5d892d0

### изменена: 0x5dcf3c0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d86120, стало 0x5d892a0

### изменена: 0x5dcf440 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d860f0, стало 0x5d89270

### изменена: 0x5dcf4c0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d860c0, стало 0x5d89240

### изменена: 0x5dcf540 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d86080, стало 0x5d89200

### изменена: 0x5dcf5c0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d86050, стало 0x5d891d0

### изменена: 0x5dcf640 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d86020, стало 0x5d891a0

### изменена: 0x5dcf6c0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d85ff0, стало 0x5d89170

### изменена: 0x5dcf740 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d85fc0, стало 0x5d89140

### изменена: 0x5dcf7c0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d85f90, стало 0x5d89110

### изменена: 0x5dcf840 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d85f60, стало 0x5d890e0

### изменена: 0x5dcf8c0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d85f30, стало 0x5d890b0

### изменена: 0x5dcf940 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d85f00, стало 0x5d89080

### изменена: 0x5dcf9c0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d85ed0, стало 0x5d89050

### изменена: 0x5dcfa40 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d85ea0, стало 0x5d89020

### изменена: 0x5dcfac0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d85e70, стало 0x5d88ff0

### изменена: 0x5dcfb40 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d85e30, стало 0x5d88fb0

### изменена: 0x5dcfbc0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d85e00, стало 0x5d88f80

### изменена: 0x5dcfc40 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d85dd0, стало 0x5d88f50

### изменена: 0x5dcfcc0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d85da0, стало 0x5d88f20

### изменена: 0x5dcfd40 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d85d70, стало 0x5d88ef0

### изменена: 0x5dcfdc0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d85d40, стало 0x5d88ec0

### изменена: 0x5dcfe40 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d85d10, стало 0x5d88e90

### изменена: 0x5dcfec0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d85ce0, стало 0x5d88e60

### изменена: 0x5dcff40 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d85cb0, стало 0x5d88e30

### изменена: 0x5dcffc0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d85c70, стало 0x5d88df0

### изменена: 0x5dd0040 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d85c30, стало 0x5d88db0

### изменена: 0x5dd00c0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d85bf0, стало 0x5d88d70

### изменена: 0x5dd0140 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d85bb0, стало 0x5d88d30

### изменена: 0x5dd01c0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d85b70, стало 0x5d88cf0

### изменена: 0x5dd0240 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d85b30, стало 0x5d88cb0

### изменена: 0x5dd02c0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d85af0, стало 0x5d88c70

### изменена: 0x5dd0340 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d85ab0, стало 0x5d88c30

### изменена: 0x5dd03c0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d85a70, стало 0x5d88bf0

### изменена: 0x5dd0440 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d85a30, стало 0x5d88bb0

### изменена: 0x5dd04c0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d859f0, стало 0x5d88b70

### изменена: 0x5dd0540 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d859b0, стало 0x5d88b30

### изменена: 0x5dd05c0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d85970, стало 0x5d88af0

### изменена: 0x5dd0640 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d85930, стало 0x5d88ab0

### изменена: 0x5dd06c0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d858f0, стало 0x5d88a70

### изменена: 0x5dd0740 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d858b0, стало 0x5d88a30

### изменена: 0x5dd07c0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d85870, стало 0x5d889f0

### изменена: 0x5dd0840 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d85830, стало 0x5d889b0

### изменена: 0x5dd08c0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d857f0, стало 0x5d88970

### изменена: 0x5dd0940 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d857b0, стало 0x5d88930

### изменена: 0x5dd09c0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d85770, стало 0x5d888f0

### изменена: 0x5dd0a40 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d85730, стало 0x5d888b0

### изменена: 0x5dd0ac0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d856f0, стало 0x5d88870

### изменена: 0x5dd0b40 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d856b0, стало 0x5d88830

### изменена: 0x5dd0bc0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d85670, стало 0x5d887f0

### изменена: 0x5dd0c40 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d85630, стало 0x5d887b0

### изменена: 0x5dd0cc0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d855f0, стало 0x5d88770

### изменена: 0x5dd0d40 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d855b0, стало 0x5d88730

### изменена: 0x5dd0dc0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d85570, стало 0x5d886f0

### изменена: 0x5dd0e40 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d85530, стало 0x5d886b0

### изменена: 0x5dd0ec0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d854f0, стало 0x5d88670

### изменена: 0x5dd0f40 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d854b0, стало 0x5d88630

### изменена: 0x5dd0fc0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d85470, стало 0x5d885f0

### изменена: 0x5dd1040 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d85430, стало 0x5d885b0

### изменена: 0x5dd10c0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d853f0, стало 0x5d88570

### изменена: 0x5dd1140 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d853b0, стало 0x5d88530

### изменена: 0x5dd11c0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d85370, стало 0x5d884f0

### изменена: 0x5dd1240 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d85330, стало 0x5d884b0

### изменена: 0x5dd12c0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d852f0, стало 0x5d88470

### изменена: 0x5dd1340 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d852b0, стало 0x5d88430

### изменена: 0x5dd13c0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d85270, стало 0x5d883f0

### изменена: 0x5dd1440 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d85230, стало 0x5d883b0

### изменена: 0x5dd14c0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d851f0, стало 0x5d88370

### изменена: 0x5dd1540 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d851b0, стало 0x5d88330

### изменена: 0x5dd15c0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d85170, стало 0x5d882f0

### изменена: 0x5dd1640 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d85130, стало 0x5d882b0

### изменена: 0x5dd16c0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d850f0, стало 0x5d88270

### изменена: 0x5dd1740 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d850b0, стало 0x5d88230

### изменена: 0x5dd17c0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d85070, стало 0x5d881f0

### изменена: 0x5dd1840 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d85030, стало 0x5d881b0

### изменена: 0x5dd18c0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d84ff0, стало 0x5d88170

### изменена: 0x5dd1940 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d84fb0, стало 0x5d88130

### изменена: 0x5dd19c0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d84f70, стало 0x5d880f0

### изменена: 0x5dd1a40 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d84f30, стало 0x5d880b0

### изменена: 0x5dd1ac0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d84ef0, стало 0x5d88070

### изменена: 0x5dd1b40 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d84eb0, стало 0x5d88030

### изменена: 0x5dd1bc0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d84e70, стало 0x5d87ff0

### изменена: 0x5dd1c40 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d84e30, стало 0x5d87fb0

### изменена: 0x5dd1cc0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d84df0, стало 0x5d87f70

### изменена: 0x5dd1d40 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d84db0, стало 0x5d87f30

### изменена: 0x5dd1dc0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d84d70, стало 0x5d87ef0

### изменена: 0x5dd1e40 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d84d30, стало 0x5d87eb0

### изменена: 0x5dd1ec0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d84cf0, стало 0x5d87e70

### изменена: 0x5dd1f40 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d84cb0, стало 0x5d87e30

### изменена: 0x5dd1fc0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d84c70, стало 0x5d87df0

### изменена: 0x5dd2040 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d84c30, стало 0x5d87db0

### изменена: 0x5dd20c0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d84bf0, стало 0x5d87d70

### изменена: 0x5dd2140 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d84bb0, стало 0x5d87d30

### изменена: 0x5dd21c0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d84b70, стало 0x5d87cf0

### изменена: 0x5dd2240 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d84b30, стало 0x5d87cb0

### изменена: 0x5dd22c0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d84af0, стало 0x5d87c70

### изменена: 0x5dd2340 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d84ab0, стало 0x5d87c30

### изменена: 0x5dd23c0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d84a70, стало 0x5d87bf0

### изменена: 0x5dd2440 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d84a30, стало 0x5d87bb0

### изменена: 0x5dd24c0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d849f0, стало 0x5d87b70

### изменена: 0x5dd2540 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d849b0, стало 0x5d87b30

### изменена: 0x5dd25c0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d84970, стало 0x5d87af0

### изменена: 0x5dd2640 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d84930, стало 0x5d87ab0

### изменена: 0x5dd26c0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d848f0, стало 0x5d87a70

### изменена: 0x5dd2740 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d848b0, стало 0x5d87a30

### изменена: 0x5dd27c0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d84870, стало 0x5d879f0

### изменена: 0x5dd2840 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d84830, стало 0x5d879b0

### изменена: 0x5dd28c0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d847f0, стало 0x5d87970

### изменена: 0x5dd2940 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d847b0, стало 0x5d87930

### изменена: 0x5dd29c0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d84770, стало 0x5d878f0

### изменена: 0x5dd2a40 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d84730, стало 0x5d878b0

### изменена: 0x5dd2ac0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d846f0, стало 0x5d87870

### изменена: 0x5dd2b40 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d846b0, стало 0x5d87830

### изменена: 0x5dd2bc0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d84670, стало 0x5d877f0

### изменена: 0x5dd2c40 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d84630, стало 0x5d877b0

### изменена: 0x5dd2cc0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d845f0, стало 0x5d87770

### изменена: 0x5dd2d40 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d845b0, стало 0x5d87730

### изменена: 0x5dd2dc0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d84570, стало 0x5d876f0

### изменена: 0x5dd2e40 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d84530, стало 0x5d876b0

### изменена: 0x5dd2ec0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d844f0, стало 0x5d87670

### изменена: 0x5dd2f40 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d844b0, стало 0x5d87630

### изменена: 0x5dd2fc0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d84470, стало 0x5d875f0

### изменена: 0x5dd3040 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d84430, стало 0x5d875b0

### изменена: 0x5dd30c0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d843f0, стало 0x5d87570

### изменена: 0x5dd3140 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d843b0, стало 0x5d87530

### изменена: 0x5dd31c0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d84370, стало 0x5d874f0

### изменена: 0x5dd3240 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d84330, стало 0x5d874b0

### изменена: 0x5dd32c0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d842f0, стало 0x5d87470

### изменена: 0x5dd3340 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d842b0, стало 0x5d87430

### изменена: 0x5dd33c0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d84270, стало 0x5d873f0

### изменена: 0x5dd3440 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d84230, стало 0x5d873b0

### изменена: 0x5dd34c0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d841f0, стало 0x5d87370

### изменена: 0x5dd3540 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d841b0, стало 0x5d87330

### изменена: 0x5dd35c0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d84170, стало 0x5d872f0

### изменена: 0x5dd3640 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d84130, стало 0x5d872b0

### изменена: 0x5dd36c0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d840f0, стало 0x5d87270

### изменена: 0x5dd3740 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d840b0, стало 0x5d87230

### изменена: 0x5dd37c0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d84070, стало 0x5d871f0

### изменена: 0x5dd3840 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d84030, стало 0x5d871b0

### изменена: 0x5dd38c0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d83ff0, стало 0x5d87170

### изменена: 0x5dd3940 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d83fb0, стало 0x5d87130

### изменена: 0x5dd39c0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d83f70, стало 0x5d870f0

### изменена: 0x5dd3a40 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d83f30, стало 0x5d870b0

### изменена: 0x5dd3ac0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d83ef0, стало 0x5d87070

### изменена: 0x5dd3b40 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d83eb0, стало 0x5d87030

### изменена: 0x5dd3bc0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d83e70, стало 0x5d86ff0

### изменена: 0x5dd3c40 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d83e30, стало 0x5d86fb0

### изменена: 0x5dd3cc0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d83df0, стало 0x5d86f70

### изменена: 0x5dd3d40 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d83db0, стало 0x5d86f30

### изменена: 0x5dd3dc0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d83d70, стало 0x5d86ef0

### изменена: 0x5dd3e40 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d83d30, стало 0x5d86eb0

### изменена: 0x5dd3ec0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d83cf0, стало 0x5d86e70

### изменена: 0x5dd3f40 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d83cb0, стало 0x5d86e30

### изменена: 0x5dd3fc0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d83c70, стало 0x5d86df0

### изменена: 0x5dd4040 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d83c30, стало 0x5d86db0

### изменена: 0x5dd40c0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d83bf0, стало 0x5d86d70

### изменена: 0x5dd4140 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d83bb0, стало 0x5d86d30

### изменена: 0x5dd41c0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d83b70, стало 0x5d86cf0

### изменена: 0x5dd4240 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d83b30, стало 0x5d86cb0

### изменена: 0x5dd42c0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d83af0, стало 0x5d86c70

### изменена: 0x5dd4340 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d83ab0, стало 0x5d86c30

### изменена: 0x5dd43c0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d83a70, стало 0x5d86bf0

### изменена: 0x5dd4440 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d83a30, стало 0x5d86bb0

### изменена: 0x5dd44c0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d839f0, стало 0x5d86b70

### изменена: 0x5dd4540 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d839b0, стало 0x5d86b30

### изменена: 0x5dd45c0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d83970, стало 0x5d86af0

### изменена: 0x5dd4640 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d83930, стало 0x5d86ab0

### изменена: 0x5dd46c0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d838f0, стало 0x5d86a70

### изменена: 0x5dd4740 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d838b0, стало 0x5d86a30

### изменена: 0x5dd47c0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d83870, стало 0x5d869f0

### изменена: 0x5dd4840 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d83830, стало 0x5d869b0

### изменена: 0x5dd48c0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d837f0, стало 0x5d86970

### изменена: 0x5dd4940 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d837b0, стало 0x5d86930

### изменена: 0x5dd49c0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d83770, стало 0x5d868f0

### изменена: 0x5dd4a40 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d83730, стало 0x5d868b0

### изменена: 0x5dd4ac0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d836f0, стало 0x5d86870

### изменена: 0x5dd4b40 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d836b0, стало 0x5d86830

### изменена: 0x5dd4bc0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d83670, стало 0x5d867f0

### изменена: 0x5dd4c40 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d83630, стало 0x5d867b0

### изменена: 0x5dd4cc0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d835f0, стало 0x5d86770

### изменена: 0x5dd4d40 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d835b0, стало 0x5d86730

### изменена: 0x5dd4dc0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d83570, стало 0x5d866f0

### изменена: 0x5dd4e40 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d83530, стало 0x5d866b0

### изменена: 0x5dd4ec0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d834f0, стало 0x5d86670

### изменена: 0x5dd4f40 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d834b0, стало 0x5d86630

### изменена: 0x5dd4fc0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d83470, стало 0x5d865f0

### изменена: 0x5dd5040 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d83430, стало 0x5d865b0

### изменена: 0x5dd50c0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d833f0, стало 0x5d86570

### изменена: 0x5dd5140 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d833b0, стало 0x5d86530

### изменена: 0x5dd51c0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d83370, стало 0x5d864f0

### изменена: 0x5dd5240 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d83330, стало 0x5d864b0

### изменена: 0x5dd52c0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d832f0, стало 0x5d86470

### изменена: 0x5dd5340 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d832b0, стало 0x5d86430

### изменена: 0x5dd53c0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d83270, стало 0x5d863f0

### изменена: 0x5dd5440 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d83230, стало 0x5d863b0

### изменена: 0x5dd54c0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d831f0, стало 0x5d86370

### изменена: 0x5dd5540 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d831b0, стало 0x5d86330

### изменена: 0x5dd55c0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d83170, стало 0x5d862f0

### изменена: 0x5dd5640 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d83130, стало 0x5d862b0

### изменена: 0x5dd56c0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d830f0, стало 0x5d86270

### изменена: 0x5dd5740 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d830b0, стало 0x5d86230

### изменена: 0x5dd57c0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d83070, стало 0x5d861f0

### изменена: 0x5dd5840 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d83030, стало 0x5d861b0

### изменена: 0x5dd58c0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d82ff0, стало 0x5d86170

### изменена: 0x5dd5940 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d82fb0, стало 0x5d86130

### изменена: 0x5dd59c0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d82f70, стало 0x5d860f0

### изменена: 0x5dd5a40 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d82f30, стало 0x5d860b0

### изменена: 0x5dd5ac0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d82ef0, стало 0x5d86070

### изменена: 0x5dd5b40 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d82eb0, стало 0x5d86030

### изменена: 0x5dd5bc0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d82e70, стало 0x5d85ff0

### изменена: 0x5dd5c40 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d82e30, стало 0x5d85fb0

### изменена: 0x5dd5cc0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d82df0, стало 0x5d85f70

### изменена: 0x5dd5d40 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d82db0, стало 0x5d85f30

### изменена: 0x5dd5dc0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d82d70, стало 0x5d85ef0

### изменена: 0x5dd5e40 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d82d30, стало 0x5d85eb0

### изменена: 0x5dd5ec0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d82cf0, стало 0x5d85e70

### изменена: 0x5dd5f40 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d82cb0, стало 0x5d85e30

### изменена: 0x5dd5fc0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d82c70, стало 0x5d85df0

### изменена: 0x5dd6040 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d82c30, стало 0x5d85db0

### изменена: 0x5dd60c0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d82bf0, стало 0x5d85d70

### изменена: 0x5dd6140 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d82bb0, стало 0x5d85d30

### изменена: 0x5dd61c0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d82b70, стало 0x5d85cf0

### изменена: 0x5dd6240 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d82b30, стало 0x5d85cb0

### изменена: 0x5dd62c0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d82af0, стало 0x5d85c70

### изменена: 0x5dd6340 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d82ab0, стало 0x5d85c30

### изменена: 0x5dd63c0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d82a70, стало 0x5d85bf0

### изменена: 0x5dd6440 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d82a30, стало 0x5d85bb0

### изменена: 0x5dd64c0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d829f0, стало 0x5d85b70

### изменена: 0x5dd6540 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d829b0, стало 0x5d85b30

### изменена: 0x5dd65c0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d82970, стало 0x5d85af0

### изменена: 0x5dd6640 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d82930, стало 0x5d85ab0

### изменена: 0x5dd66c0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d828f0, стало 0x5d85a70

### изменена: 0x5dd6740 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d828b0, стало 0x5d85a30

### изменена: 0x5dd67c0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d82890, стало 0x5d85a10

### изменена: 0x5dd6840 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d82870, стало 0x5d859f0

### изменена: 0x5dd68c0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d82850, стало 0x5d859d0

### изменена: 0x5dd6940 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d82830, стало 0x5d859b0

### изменена: 0x5dd69c0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d82810, стало 0x5d85990

### изменена: 0x5dd6a40 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d827f0, стало 0x5d85970

### изменена: 0x5dd6ac0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d827d0, стало 0x5d85950

### изменена: 0x5dd6b40 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d827b0, стало 0x5d85930

### изменена: 0x5dd6bc0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d82790, стало 0x5d85910

### изменена: 0x5dd6c40 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d82770, стало 0x5d858f0

### изменена: 0x5dd6cc0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d82750, стало 0x5d858d0

### изменена: 0x5dd6d40 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d82730, стало 0x5d858b0

### изменена: 0x5dd6dc0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d82710, стало 0x5d85890

### изменена: 0x5dd6e40 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d826f0, стало 0x5d85870

### изменена: 0x5dd6ec0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d826d0, стало 0x5d85850

### изменена: 0x5dd6f40 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d826b0, стало 0x5d85830

### изменена: 0x5dd6fc0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d82690, стало 0x5d85810

### изменена: 0x5dd7040 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d82670, стало 0x5d857f0

### изменена: 0x5dd70c0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d82650, стало 0x5d857d0

### изменена: 0x5dd7140 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d82630, стало 0x5d857b0

### изменена: 0x5dd71c0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d82610, стало 0x5d85790

### изменена: 0x5dd7240 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d825f0, стало 0x5d85770

### изменена: 0x5dd72c0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d825d0, стало 0x5d85750

### изменена: 0x5dd7340 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d825b0, стало 0x5d85730

### изменена: 0x5dd73c0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d82590, стало 0x5d85710

### изменена: 0x5dd7440 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d82570, стало 0x5d856f0

### изменена: 0x5dd74c0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d82550, стало 0x5d856d0

### изменена: 0x5dd7540 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d82530, стало 0x5d856b0

### изменена: 0x5dd75c0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d82510, стало 0x5d85690

### изменена: 0x5dd7640 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d824f0, стало 0x5d85670

### изменена: 0x5dd76c0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d824d0, стало 0x5d85650

### изменена: 0x5dd7740 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d824b0, стало 0x5d85630

### изменена: 0x5dd77c0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d82490, стало 0x5d85610

### изменена: 0x5dd7840 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d82470, стало 0x5d855f0

### изменена: 0x5dd78c0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d82450, стало 0x5d855d0

### изменена: 0x5dd7940 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d82430, стало 0x5d855b0

### изменена: 0x5dd79c0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d82410, стало 0x5d85590

### изменена: 0x5dd7a40 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d823f0, стало 0x5d85570

### изменена: 0x5dd7ac0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d823d0, стало 0x5d85550

### изменена: 0x5dd7b40 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d823b0, стало 0x5d85530

### изменена: 0x5dd7bc0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d82390, стало 0x5d85510

### изменена: 0x5dd7c40 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d82370, стало 0x5d854f0

### изменена: 0x5dd7cc0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d82350, стало 0x5d854d0

### изменена: 0x5dd7d40 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d82330, стало 0x5d854b0

### изменена: 0x5dd7dc0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d82310, стало 0x5d85490

### изменена: 0x5dd7e40 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d822f0, стало 0x5d85470

### изменена: 0x5dd7ec0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d822d0, стало 0x5d85450

### изменена: 0x5dd7f40 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d822b0, стало 0x5d85430

### изменена: 0x5dd7fc0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d82290, стало 0x5d85410

### изменена: 0x5dd8040 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d82270, стало 0x5d853f0

### изменена: 0x5dd80c0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d82250, стало 0x5d853d0

### изменена: 0x5dd8140 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d82210, стало 0x5d85390

### изменена: 0x5dd81c0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d821d0, стало 0x5d85350

### изменена: 0x5dd8240 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d82190, стало 0x5d85310

### изменена: 0x5dd82c0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d82150, стало 0x5d852d0

### изменена: 0x5dd8340 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d82110, стало 0x5d85290

### изменена: 0x5dd83c0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d820d0, стало 0x5d85250

### изменена: 0x5dd8440 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d82090, стало 0x5d85210

### изменена: 0x5dd84c0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d82050, стало 0x5d851d0

### изменена: 0x5dd8540 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d82010, стало 0x5d85190

### изменена: 0x5dd85c0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d81fd0, стало 0x5d85150

### изменена: 0x5dd8640 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d81f90, стало 0x5d85110

### изменена: 0x5dd86c0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d81f50, стало 0x5d850d0

### изменена: 0x5dd8740 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d81f10, стало 0x5d85090

### изменена: 0x5dd87c0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d81ed0, стало 0x5d85050

### изменена: 0x5dd8840 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d81e90, стало 0x5d85010

### изменена: 0x5dd88c0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d81e50, стало 0x5d84fd0

### изменена: 0x5dd8940 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d81e10, стало 0x5d84f90

### изменена: 0x5dd89c0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d81dd0, стало 0x5d84f50

### изменена: 0x5dd8a40 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d81d90, стало 0x5d84f10

### изменена: 0x5dd8ac0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d81d50, стало 0x5d84ed0

### изменена: 0x5dd8b40 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d81d10, стало 0x5d84e90

### изменена: 0x5dd8bc0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d81cd0, стало 0x5d84e50

### изменена: 0x5dd8c40 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d81c90, стало 0x5d84e10

### изменена: 0x5dd8cc0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d81c50, стало 0x5d84dd0

### изменена: 0x5dd8d40 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d81c10, стало 0x5d84d90

### изменена: 0x5dd8dc0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d81bd0, стало 0x5d84d50

### изменена: 0x5dd8e40 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d81b90, стало 0x5d84d10

### изменена: 0x5dd8ec0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d81b50, стало 0x5d84cd0

### изменена: 0x5dd8f40 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d81b10, стало 0x5d84c90

### изменена: 0x5dd8fc0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d81ad0, стало 0x5d84c50

### изменена: 0x5dd9040 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d81a90, стало 0x5d84c10

### изменена: 0x5dd90c0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d81a50, стало 0x5d84bd0

### изменена: 0x5dd9140 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d81a10, стало 0x5d84b90

### изменена: 0x5dd91c0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d819d0, стало 0x5d84b50

### изменена: 0x5dd9240 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d81990, стало 0x5d84b10

### изменена: 0x5dd92c0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d81950, стало 0x5d84ad0

### изменена: 0x5dd9340 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d81910, стало 0x5d84a90

### изменена: 0x5dd93c0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d818d0, стало 0x5d84a50

### изменена: 0x5dd9440 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d81890, стало 0x5d84a10

### изменена: 0x5dd94c0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d81850, стало 0x5d849d0

### изменена: 0x5dd9540 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d81810, стало 0x5d84990

### изменена: 0x5dd95c0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d817d0, стало 0x5d84950

### изменена: 0x5dd9640 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d81790, стало 0x5d84910

### изменена: 0x5dd96c0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d81750, стало 0x5d848d0

### изменена: 0x5dd9740 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d81710, стало 0x5d84890

### изменена: 0x5dd97c0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d816d0, стало 0x5d84850

### изменена: 0x5dd9840 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d81690, стало 0x5d84810

### изменена: 0x5dd98c0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d81650, стало 0x5d847d0

### изменена: 0x5dd9940 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d81610, стало 0x5d84790

### изменена: 0x5dd99c0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d815d0, стало 0x5d84750

### изменена: 0x5dd9a40 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d81590, стало 0x5d84710

### изменена: 0x5dd9ac0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d81550, стало 0x5d846d0

### изменена: 0x5dd9b40 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d81510, стало 0x5d84690

### изменена: 0x5dd9bc0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d814d0, стало 0x5d84650

### изменена: 0x5dd9c40 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d81490, стало 0x5d84610

### изменена: 0x5dd9cc0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d81450, стало 0x5d845d0

### изменена: 0x5dd9d40 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d81410, стало 0x5d84590

### изменена: 0x5dd9dc0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d813d0, стало 0x5d84550

### изменена: 0x5dd9e40 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d81390, стало 0x5d84510

### изменена: 0x5dd9ec0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d81350, стало 0x5d844d0

### изменена: 0x5dd9f40 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d81310, стало 0x5d84490

### изменена: 0x5dd9fc0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d812d0, стало 0x5d84450

### изменена: 0x5dda040 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d81290, стало 0x5d84410

### изменена: 0x5dda0c0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d81250, стало 0x5d843d0

### изменена: 0x5dda140 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d81210, стало 0x5d84390

### изменена: 0x5dda1c0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d811d0, стало 0x5d84350

### изменена: 0x5dda240 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d81190, стало 0x5d84310

### изменена: 0x5dda2c0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d81150, стало 0x5d842d0

### изменена: 0x5dda340 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d81110, стало 0x5d84290

### изменена: 0x5dda3c0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d810d0, стало 0x5d84250

### изменена: 0x5dda440 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d81090, стало 0x5d84210

### изменена: 0x5dda4c0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d81050, стало 0x5d841d0

### изменена: 0x5dda540 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d81010, стало 0x5d84190

### изменена: 0x5dda5c0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d80fd0, стало 0x5d84150

### изменена: 0x5dda640 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d80f90, стало 0x5d84110

### изменена: 0x5dda6c0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d80f50, стало 0x5d840d0

### изменена: 0x5dda740 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d80f10, стало 0x5d84090

### изменена: 0x5dda7c0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d80ed0, стало 0x5d84050

### изменена: 0x5dda840 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d80e90, стало 0x5d84010

### изменена: 0x5dda8c0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d80e50, стало 0x5d83fd0

### изменена: 0x5dda940 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d80e10, стало 0x5d83f90

### изменена: 0x5dda9c0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d80dd0, стало 0x5d83f50

### изменена: 0x5ddaa40 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d80d90, стало 0x5d83f10

### изменена: 0x5ddaac0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d80d50, стало 0x5d83ed0

### изменена: 0x5ddab40 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d80d10, стало 0x5d83e90

### изменена: 0x5ddabc0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d80cd0, стало 0x5d83e50

### изменена: 0x5ddac40 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d80c90, стало 0x5d83e10

### изменена: 0x5ddacc0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d80c50, стало 0x5d83dd0

### изменена: 0x5ddad40 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d80c10, стало 0x5d83d90

### изменена: 0x5ddadc0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d80bd0, стало 0x5d83d50

### изменена: 0x5ddae40 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d80b90, стало 0x5d83d10

### изменена: 0x5ddaec0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d80b50, стало 0x5d83cd0

### изменена: 0x5ddaf40 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d80b10, стало 0x5d83c90

### изменена: 0x5ddafc0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d80ad0, стало 0x5d83c50

### изменена: 0x5ddb040 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d80a90, стало 0x5d83c10

### изменена: 0x5ddb0c0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d80a50, стало 0x5d83bd0

### изменена: 0x5ddb140 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d80a10, стало 0x5d83b90

### изменена: 0x5ddb1c0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d809d0, стало 0x5d83b50

### изменена: 0x5ddb240 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d80990, стало 0x5d83b10

### изменена: 0x5ddb2c0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d80950, стало 0x5d83ad0

### изменена: 0x5ddb340 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d80910, стало 0x5d83a90

### изменена: 0x5ddb3c0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d808d0, стало 0x5d83a50

### изменена: 0x5ddb440 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d80890, стало 0x5d83a10

### изменена: 0x5ddb4c0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d80850, стало 0x5d839d0

### изменена: 0x5ddb540 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d80810, стало 0x5d83990

### изменена: 0x5ddb5c0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d807d0, стало 0x5d83950

### изменена: 0x5ddb640 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d80790, стало 0x5d83910

### изменена: 0x5ddb6c0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d80750, стало 0x5d838d0

### изменена: 0x5ddb740 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d80710, стало 0x5d83890

### изменена: 0x5ddb7c0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d806d0, стало 0x5d83850

### изменена: 0x5ddb840 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d80690, стало 0x5d83810

### изменена: 0x5ddb8c0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d80650, стало 0x5d837d0

### изменена: 0x5ddb940 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d80610, стало 0x5d83790

### изменена: 0x5ddb9c0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d805d0, стало 0x5d83750

### изменена: 0x5ddba40 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d80590, стало 0x5d83710

### изменена: 0x5ddbac0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d80550, стало 0x5d836d0

### изменена: 0x5ddbb40 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d80510, стало 0x5d83690

### изменена: 0x5ddbbc0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d804d0, стало 0x5d83650

### изменена: 0x5ddbc40 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d80490, стало 0x5d83610

### изменена: 0x5ddbcc0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d80450, стало 0x5d835d0

### изменена: 0x5ddbd40 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d80410, стало 0x5d83590

### изменена: 0x5ddbdc0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d803d0, стало 0x5d83550

### изменена: 0x5ddbe40 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d80390, стало 0x5d83510

### изменена: 0x5ddbec0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d80350, стало 0x5d834d0

### изменена: 0x5ddbf40 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d80310, стало 0x5d83490

### изменена: 0x5ddbfc0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d802d0, стало 0x5d83450

### изменена: 0x5ddc040 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d80290, стало 0x5d83410

### изменена: 0x5ddc0c0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d80250, стало 0x5d833d0

### изменена: 0x5ddc140 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d80210, стало 0x5d83390

### изменена: 0x5ddc1c0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d801d0, стало 0x5d83350

### изменена: 0x5ddc240 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d80190, стало 0x5d83310

### изменена: 0x5ddc2c0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d80150, стало 0x5d832d0

### изменена: 0x5ddc340 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d80110, стало 0x5d83290

### изменена: 0x5ddc3c0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d800d0, стало 0x5d83250

### изменена: 0x5ddc440 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d80090, стало 0x5d83210

### изменена: 0x5ddc4c0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d80050, стало 0x5d831d0

### изменена: 0x5ddc540 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d80010, стало 0x5d83190

### изменена: 0x5ddc5c0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d7ffd0, стало 0x5d83150

### изменена: 0x5ddc640 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d7ff90, стало 0x5d83110

### изменена: 0x5ddc6c0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d7ff50, стало 0x5d830d0

### изменена: 0x5ddc740 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d7ff10, стало 0x5d83090

### изменена: 0x5ddc7c0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d7fed0, стало 0x5d83050

### изменена: 0x5ddc840 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d7fe90, стало 0x5d83010

### изменена: 0x5ddc8c0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d7fe50, стало 0x5d82fd0

### изменена: 0x5ddc940 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d7fe10, стало 0x5d82f90

### изменена: 0x5ddc9c0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d7fdd0, стало 0x5d82f50

### изменена: 0x5ddca40 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d7fd90, стало 0x5d82f10

### изменена: 0x5ddcac0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d7fd50, стало 0x5d82ed0

### изменена: 0x5ddcb40 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d7fd10, стало 0x5d82e90

### изменена: 0x5ddcbc0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d7fcd0, стало 0x5d82e50

### изменена: 0x5ddcc40 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d7fc90, стало 0x5d82e10

### изменена: 0x5ddccc0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d7fc50, стало 0x5d82dd0

### изменена: 0x5ddcd40 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d7fc10, стало 0x5d82d90

### изменена: 0x5ddcdc0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d7fbd0, стало 0x5d82d50

### изменена: 0x5ddce40 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d7fb90, стало 0x5d82d10

### изменена: 0x5ddcec0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d7fb50, стало 0x5d82cd0

### изменена: 0x5ddcf40 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d7fb10, стало 0x5d82c90

### изменена: 0x5ddcfc0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d7fad0, стало 0x5d82c50

### изменена: 0x5ddd040 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d7fa90, стало 0x5d82c10

### изменена: 0x5ddd0c0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d7fa50, стало 0x5d82bd0

### изменена: 0x5ddd140 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d7fa10, стало 0x5d82b90

### изменена: 0x5ddd1c0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d7f9d0, стало 0x5d82b50

### изменена: 0x5ddd240 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d7f9b0, стало 0x5d82b10

### изменена: 0x5ddd2c0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d7f990, стало 0x5d82af0

### изменена: 0x5ddd340 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d7f970, стало 0x5d82ad0

### изменена: 0x5ddd3c0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d7f950, стало 0x5d82ab0

### изменена: 0x5ddd440 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d7f930, стало 0x5d82a90

### изменена: 0x5ddd4c0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d7f910, стало 0x5d82a70

### изменена: 0x5ddd540 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d7f8f0, стало 0x5d82a50

### изменена: 0x5ddd5c0 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d7f880, стало 0x5d82a30

### изменена: 0x5ddd640 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d7f850, стало 0x5d829c0

### изменена: 0x5de6cb0 (5 байт)
- код тот же, но вызывает другую функцию: было 0x3f492b0, стало 0x56365d0

### изменена: 0x5de6cc0 (5 байт)
- код тот же, но вызывает другую функцию: было 0x56334b0, стало 0x3f4c3b0

### изменена: 0x5de9cf0 (5 байт)
- код тот же, но вызывает другую функцию: было 0x3f492c0, стало 0x56365f0

### изменена: 0x5de9d60 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8f070, стало 0x5d921f0

### изменена: 0x5de9e30 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8f060, стало 0x5d921e0

### изменена: 0x5de9f00 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8f050, стало 0x5d921d0

### изменена: 0x5de9fd0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8f040, стало 0x5d921c0

### изменена: 0x5dea0a0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8f030, стало 0x5d921b0

### изменена: 0x5dea170 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8f020, стало 0x5d921a0

### изменена: 0x5dea240 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8f010, стало 0x5d92190

### изменена: 0x5dea310 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8f000, стало 0x5d92180

### изменена: 0x5dea3e0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8eff0, стало 0x5d92170

### изменена: 0x5dea4b0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8efe0, стало 0x5d92160

### изменена: 0x5dea580 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8efd0, стало 0x5d92150

### изменена: 0x5dea650 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8efc0, стало 0x5d92140

### изменена: 0x5dea720 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8efb0, стало 0x5d92130

### изменена: 0x5dea7f0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8efa0, стало 0x5d92120

### изменена: 0x5dea8c0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8ef90, стало 0x5d92110

### изменена: 0x5dea990 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8ef80, стало 0x5d92100

### изменена: 0x5deaa60 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8ef70, стало 0x5d920f0

### изменена: 0x5deab30 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8ef60, стало 0x5d920e0

### изменена: 0x5deac00 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8ef50, стало 0x5d920d0

### изменена: 0x5deacd0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8ef40, стало 0x5d920c0

### изменена: 0x5deada0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8ef30, стало 0x5d920b0

### изменена: 0x5deae70 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8ef20, стало 0x5d920a0

### изменена: 0x5deaf40 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8ef10, стало 0x5d92090

### изменена: 0x5deb010 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8ef00, стало 0x5d92080

### изменена: 0x5deb0e0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8eef0, стало 0x5d92070

### изменена: 0x5deb1b0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8eee0, стало 0x5d92060

### изменена: 0x5deb280 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8eed0, стало 0x5d92050

### изменена: 0x5deb350 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8eec0, стало 0x5d92040

### изменена: 0x5deb420 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8eeb0, стало 0x5d92030

### изменена: 0x5deb4f0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8eea0, стало 0x5d92020

### изменена: 0x5deb5c0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8ee90, стало 0x5d92010

### изменена: 0x5deb690 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8ee80, стало 0x5d92000

### изменена: 0x5deb760 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8ee70, стало 0x5d91ff0

### изменена: 0x5deb830 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8ee60, стало 0x5d91fe0

### изменена: 0x5deb900 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8ee50, стало 0x5d91fd0

### изменена: 0x5deb9d0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8ee40, стало 0x5d91fc0

### изменена: 0x5debaa0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8ee30, стало 0x5d91fb0

### изменена: 0x5debb70 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8ee20, стало 0x5d91fa0

### изменена: 0x5debc40 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8ee10, стало 0x5d91f90

### изменена: 0x5debd10 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8ee00, стало 0x5d91f80

### изменена: 0x5debde0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8edf0, стало 0x5d91f70

### изменена: 0x5debeb0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8ede0, стало 0x5d91f60

### изменена: 0x5debf80 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8edd0, стало 0x5d91f50

### изменена: 0x5dec050 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8edc0, стало 0x5d91f40

### изменена: 0x5dec120 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8edb0, стало 0x5d91f30

### изменена: 0x5dec1f0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8eda0, стало 0x5d91f20

### изменена: 0x5dec2c0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8ed90, стало 0x5d91f10

### изменена: 0x5dec390 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8ed80, стало 0x5d91f00

### изменена: 0x5dec460 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8ed70, стало 0x5d91ef0

### изменена: 0x5dec530 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8ed60, стало 0x5d91ee0

### изменена: 0x5dec600 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8ed50, стало 0x5d91ed0

### изменена: 0x5dec6d0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8ed40, стало 0x5d91ec0

### изменена: 0x5dec7a0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8ed30, стало 0x5d91eb0

### изменена: 0x5dec870 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8ed20, стало 0x5d91ea0

### изменена: 0x5dec940 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8ed10, стало 0x5d91e90

### изменена: 0x5deca10 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8ed00, стало 0x5d91e80

### изменена: 0x5decae0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8ecf0, стало 0x5d91e70

### изменена: 0x5decbb0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8ece0, стало 0x5d91e60

### изменена: 0x5decc80 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8ecd0, стало 0x5d91e50

### изменена: 0x5decd50 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8ecc0, стало 0x5d91e40

### изменена: 0x5dece20 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8ecb0, стало 0x5d91e30

### изменена: 0x5decef0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8eca0, стало 0x5d91e20

### изменена: 0x5decfc0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8ec90, стало 0x5d91e10

### изменена: 0x5ded090 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8ec80, стало 0x5d91e00

### изменена: 0x5ded160 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8ec70, стало 0x5d91df0

### изменена: 0x5ded230 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8ec60, стало 0x5d91de0

### изменена: 0x5ded300 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8ec50, стало 0x5d91dd0

### изменена: 0x5ded3d0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8ec40, стало 0x5d91dc0

### изменена: 0x5ded4a0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8ec30, стало 0x5d91db0

### изменена: 0x5ded570 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8ec20, стало 0x5d91da0

### изменена: 0x5ded640 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8ec10, стало 0x5d91d90

### изменена: 0x5ded710 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8ec00, стало 0x5d91d80

### изменена: 0x5ded7e0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8ebf0, стало 0x5d91d70

### изменена: 0x5ded8b0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8ebe0, стало 0x5d91d60

### изменена: 0x5ded980 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8ebd0, стало 0x5d91d50

### изменена: 0x5deda50 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8ebc0, стало 0x5d91d40

### изменена: 0x5dedb20 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8ebb0, стало 0x5d91d30

### изменена: 0x5dedbf0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8eba0, стало 0x5d91d20

### изменена: 0x5dedcc0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8eb90, стало 0x5d91d10

### изменена: 0x5dedd90 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8eb80, стало 0x5d91d00

### изменена: 0x5dede60 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8eb70, стало 0x5d91cf0

### изменена: 0x5dedf30 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8eb60, стало 0x5d91ce0

### изменена: 0x5dee000 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8eb50, стало 0x5d91cd0

### изменена: 0x5dee0d0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8eb40, стало 0x5d91cc0

### изменена: 0x5dee1a0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8eb30, стало 0x5d91cb0

### изменена: 0x5dee270 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8eb20, стало 0x5d91ca0

### изменена: 0x5dee340 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8eb10, стало 0x5d91c90

### изменена: 0x5dee410 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8eb00, стало 0x5d91c80

### изменена: 0x5dee4e0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8eaf0, стало 0x5d91c70

### изменена: 0x5dee5b0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8eae0, стало 0x5d91c60

### изменена: 0x5dee680 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8ead0, стало 0x5d91c50

### изменена: 0x5dee750 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8eac0, стало 0x5d91c40

### изменена: 0x5dee820 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8eab0, стало 0x5d91c30

### изменена: 0x5dee8f0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8eaa0, стало 0x5d91c20

### изменена: 0x5dee9c0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8ea90, стало 0x5d91c10

### изменена: 0x5deea90 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8ea80, стало 0x5d91c00

### изменена: 0x5deeb60 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8ea70, стало 0x5d91bf0

### изменена: 0x5deec30 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8ea60, стало 0x5d91be0

### изменена: 0x5deed00 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8ea50, стало 0x5d91bd0

### изменена: 0x5deedd0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8ea40, стало 0x5d91bc0

### изменена: 0x5deeea0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8ea30, стало 0x5d91bb0

### изменена: 0x5deef70 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8ea20, стало 0x5d91ba0

### изменена: 0x5def040 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8ea10, стало 0x5d91b90

### изменена: 0x5def110 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8ea00, стало 0x5d91b80

### изменена: 0x5def1e0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8e9f0, стало 0x5d91b70

### изменена: 0x5def2b0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8e9e0, стало 0x5d91b60

### изменена: 0x5def380 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8e9d0, стало 0x5d91b50

### изменена: 0x5def450 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8e9c0, стало 0x5d91b40

### изменена: 0x5def520 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8e9b0, стало 0x5d91b30

### изменена: 0x5def5f0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8e9a0, стало 0x5d91b20

### изменена: 0x5def6c0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8e990, стало 0x5d91b10

### изменена: 0x5def790 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8e980, стало 0x5d91b00

### изменена: 0x5def860 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8e970, стало 0x5d91af0

### изменена: 0x5def930 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8e960, стало 0x5d91ae0

### изменена: 0x5defa00 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8e950, стало 0x5d91ad0

### изменена: 0x5defad0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8e940, стало 0x5d91ac0

### изменена: 0x5defba0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8e930, стало 0x5d91ab0

### изменена: 0x5defc70 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8e920, стало 0x5d91aa0

### изменена: 0x5defd40 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8e910, стало 0x5d91a90

### изменена: 0x5defe10 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8e900, стало 0x5d91a80

### изменена: 0x5defee0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8e8f0, стало 0x5d91a70

### изменена: 0x5deffb0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8e8e0, стало 0x5d91a60

### изменена: 0x5df0080 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8e8d0, стало 0x5d91a50

### изменена: 0x5df0150 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8e8c0, стало 0x5d91a40

### изменена: 0x5df0220 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8e8b0, стало 0x5d91a30

### изменена: 0x5df02f0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8e8a0, стало 0x5d91a20

### изменена: 0x5df03c0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8e890, стало 0x5d91a10

### изменена: 0x5df0490 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8e880, стало 0x5d91a00

### изменена: 0x5df0560 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8e870, стало 0x5d919f0

### изменена: 0x5df0630 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8e860, стало 0x5d919e0

### изменена: 0x5df0700 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8e850, стало 0x5d919d0

### изменена: 0x5df07d0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8e840, стало 0x5d919c0

### изменена: 0x5df08a0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8e830, стало 0x5d919b0

### изменена: 0x5df0970 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8e820, стало 0x5d919a0

### изменена: 0x5df0a40 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8e810, стало 0x5d91990

### изменена: 0x5df0b10 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8e800, стало 0x5d91980

### изменена: 0x5df0be0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8e7f0, стало 0x5d91970

### изменена: 0x5df0cb0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8e7e0, стало 0x5d91960

### изменена: 0x5df0d80 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8e7d0, стало 0x5d91950

### изменена: 0x5df0e50 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8e7c0, стало 0x5d91940

### изменена: 0x5df0f20 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8e7b0, стало 0x5d91930

### изменена: 0x5df0ff0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8e7a0, стало 0x5d91920

### изменена: 0x5df10c0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8e790, стало 0x5d91910

### изменена: 0x5df1190 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8e780, стало 0x5d91900

### изменена: 0x5df1260 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8e770, стало 0x5d918f0

### изменена: 0x5df1330 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8e760, стало 0x5d918e0

### изменена: 0x5df1400 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8e750, стало 0x5d918d0

### изменена: 0x5df14d0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8e740, стало 0x5d918c0

### изменена: 0x5df15a0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8e730, стало 0x5d918b0

### изменена: 0x5df1670 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8e720, стало 0x5d918a0

### изменена: 0x5df1740 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8e710, стало 0x5d91890

### изменена: 0x5df1810 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8e700, стало 0x5d91880

### изменена: 0x5df18e0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8e6f0, стало 0x5d91870

### изменена: 0x5df19b0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8e6e0, стало 0x5d91860

### изменена: 0x5df1a80 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8e6d0, стало 0x5d91850

### изменена: 0x5df1b50 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8e6c0, стало 0x5d91840

### изменена: 0x5df1c20 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8e6b0, стало 0x5d91830

### изменена: 0x5df1cf0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8e6a0, стало 0x5d91820

### изменена: 0x5df1dc0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8e690, стало 0x5d91810

### изменена: 0x5df1e90 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8e680, стало 0x5d91800

### изменена: 0x5df1f60 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8e670, стало 0x5d917f0

### изменена: 0x5df2030 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8e660, стало 0x5d917e0

### изменена: 0x5df2100 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8e650, стало 0x5d917d0

### изменена: 0x5df21d0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8e640, стало 0x5d917c0

### изменена: 0x5df22a0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8e630, стало 0x5d917b0

### изменена: 0x5df2370 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8e620, стало 0x5d917a0

### изменена: 0x5df2440 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8e610, стало 0x5d91790

### изменена: 0x5df2510 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8e600, стало 0x5d91780

### изменена: 0x5df25e0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8e5f0, стало 0x5d91770

### изменена: 0x5df26b0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8e5e0, стало 0x5d91760

### изменена: 0x5df2780 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8e5d0, стало 0x5d91750

### изменена: 0x5df2850 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8e5c0, стало 0x5d91740

### изменена: 0x5df2920 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8e5b0, стало 0x5d91730

### изменена: 0x5df29f0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8e5a0, стало 0x5d91720

### изменена: 0x5df2ac0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8e590, стало 0x5d91710

### изменена: 0x5df2b90 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8e580, стало 0x5d91700

### изменена: 0x5df2c60 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8e570, стало 0x5d916f0

### изменена: 0x5df2d30 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8e560, стало 0x5d916e0

### изменена: 0x5df2e00 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8e550, стало 0x5d916d0

### изменена: 0x5df2ed0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8e540, стало 0x5d916c0

### изменена: 0x5df2fa0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8e530, стало 0x5d916b0

### изменена: 0x5df3070 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8e520, стало 0x5d916a0

### изменена: 0x5df3140 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8e510, стало 0x5d91690

### изменена: 0x5df3210 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8e500, стало 0x5d91680

### изменена: 0x5df32e0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8e4f0, стало 0x5d91670

### изменена: 0x5df33b0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8e4e0, стало 0x5d91660

### изменена: 0x5df3480 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8e4d0, стало 0x5d91650

### изменена: 0x5df3550 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8e4c0, стало 0x5d91640

### изменена: 0x5df3620 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8e4b0, стало 0x5d91630

### изменена: 0x5df36f0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8e4a0, стало 0x5d91620

### изменена: 0x5df37c0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8e490, стало 0x5d91610

### изменена: 0x5df3890 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8e480, стало 0x5d91600

### изменена: 0x5df3960 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8e470, стало 0x5d915f0

### изменена: 0x5df3a30 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8e460, стало 0x5d915e0

### изменена: 0x5df3b00 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8e450, стало 0x5d915d0

### изменена: 0x5df3bd0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8e440, стало 0x5d915c0

### изменена: 0x5df3ca0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8e430, стало 0x5d915b0

### изменена: 0x5df3d70 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8e420, стало 0x5d915a0

### изменена: 0x5df3e40 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8e410, стало 0x5d91590

### изменена: 0x5df3f10 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8e400, стало 0x5d91580

### изменена: 0x5df3fe0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8e3f0, стало 0x5d91570

### изменена: 0x5df40b0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8e3e0, стало 0x5d91560

### изменена: 0x5df4180 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8e3d0, стало 0x5d91550

### изменена: 0x5df4250 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8e3c0, стало 0x5d91540

### изменена: 0x5df4320 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8e3b0, стало 0x5d91530

### изменена: 0x5df43f0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8e3a0, стало 0x5d91520

### изменена: 0x5df44c0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8e390, стало 0x5d91510

### изменена: 0x5df4590 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8e380, стало 0x5d91500

### изменена: 0x5df4660 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8e370, стало 0x5d914f0

### изменена: 0x5df4730 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8e360, стало 0x5d914e0

### изменена: 0x5df4800 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8e350, стало 0x5d914d0

### изменена: 0x5df48d0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8e340, стало 0x5d914c0

### изменена: 0x5df49a0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8e330, стало 0x5d914b0

### изменена: 0x5df4a70 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8e320, стало 0x5d914a0

### изменена: 0x5df4b40 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8e310, стало 0x5d91490

### изменена: 0x5df4c10 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8e300, стало 0x5d91480

### изменена: 0x5df4ce0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8e2f0, стало 0x5d91470

### изменена: 0x5df4db0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8e2e0, стало 0x5d91460

### изменена: 0x5df4e80 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8e2d0, стало 0x5d91450

### изменена: 0x5df4f50 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8e2c0, стало 0x5d91440

### изменена: 0x5df5020 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8e2b0, стало 0x5d91430

### изменена: 0x5df50f0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8e2a0, стало 0x5d91420

### изменена: 0x5df51c0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8e290, стало 0x5d91410

### изменена: 0x5df5290 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8e280, стало 0x5d91400

### изменена: 0x5df5360 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8e270, стало 0x5d913f0

### изменена: 0x5df5430 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8e260, стало 0x5d913e0

### изменена: 0x5df5500 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8e250, стало 0x5d913d0

### изменена: 0x5df55d0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8e240, стало 0x5d913c0

### изменена: 0x5df56a0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8e230, стало 0x5d913b0

### изменена: 0x5df5770 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8e220, стало 0x5d913a0

### изменена: 0x5df5840 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8e210, стало 0x5d91390

### изменена: 0x5df5910 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8e200, стало 0x5d91380

### изменена: 0x5df59e0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8e1f0, стало 0x5d91370

### изменена: 0x5df5ab0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8e1e0, стало 0x5d91360

### изменена: 0x5df5b80 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8e1d0, стало 0x5d91350

### изменена: 0x5df5c50 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8e1c0, стало 0x5d91340

### изменена: 0x5df5d20 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8e1b0, стало 0x5d91330

### изменена: 0x5df5df0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8e1a0, стало 0x5d91320

### изменена: 0x5df5ec0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8e190, стало 0x5d91310

### изменена: 0x5df5f90 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8e180, стало 0x5d91300

### изменена: 0x5df6060 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8e170, стало 0x5d912f0

### изменена: 0x5df6130 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8e160, стало 0x5d912e0

### изменена: 0x5df6200 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8e150, стало 0x5d912d0

### изменена: 0x5df62d0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8e140, стало 0x5d912c0

### изменена: 0x5df63a0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8e130, стало 0x5d912b0

### изменена: 0x5df6470 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8e120, стало 0x5d912a0

### изменена: 0x5df6540 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8e110, стало 0x5d91290

### изменена: 0x5df6610 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8e100, стало 0x5d91280

### изменена: 0x5df66e0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8e0f0, стало 0x5d91270

### изменена: 0x5df67b0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8e0e0, стало 0x5d91260

### изменена: 0x5df6880 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8e0d0, стало 0x5d91250

### изменена: 0x5df6950 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8e0c0, стало 0x5d91240

### изменена: 0x5df6a20 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8e0b0, стало 0x5d91230

### изменена: 0x5df6af0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8e0a0, стало 0x5d91220

### изменена: 0x5df6bc0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8e090, стало 0x5d91210

### изменена: 0x5df6c90 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8e080, стало 0x5d91200

### изменена: 0x5df6d60 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8e070, стало 0x5d911f0

### изменена: 0x5df6e30 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8e060, стало 0x5d911e0

### изменена: 0x5df6f00 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8e050, стало 0x5d911d0

### изменена: 0x5df6fd0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8e040, стало 0x5d911c0

### изменена: 0x5df70a0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8e030, стало 0x5d911b0

### изменена: 0x5df7170 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8e020, стало 0x5d911a0

### изменена: 0x5df7240 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8e010, стало 0x5d91190

### изменена: 0x5df7310 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8e000, стало 0x5d91180

### изменена: 0x5df73e0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8dff0, стало 0x5d91170

### изменена: 0x5df74b0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8dfe0, стало 0x5d91160

### изменена: 0x5df7580 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8dfd0, стало 0x5d91150

### изменена: 0x5df7650 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8dfc0, стало 0x5d91140

### изменена: 0x5df7720 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8dfb0, стало 0x5d91130

### изменена: 0x5df77f0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8dfa0, стало 0x5d91120

### изменена: 0x5df78c0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8df90, стало 0x5d91110

### изменена: 0x5df7990 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8df80, стало 0x5d91100

### изменена: 0x5df7a60 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8df70, стало 0x5d910f0

### изменена: 0x5df7b30 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8df60, стало 0x5d910e0

### изменена: 0x5df7c00 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8df50, стало 0x5d910d0

### изменена: 0x5df7cd0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8df40, стало 0x5d910c0

### изменена: 0x5df7da0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8df30, стало 0x5d910b0

### изменена: 0x5df7e70 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8df20, стало 0x5d910a0

### изменена: 0x5df7f40 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8df10, стало 0x5d91090

### изменена: 0x5df8010 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8df00, стало 0x5d91080

### изменена: 0x5df80e0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8def0, стало 0x5d91070

### изменена: 0x5df81b0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8dee0, стало 0x5d91060

### изменена: 0x5df8280 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8ded0, стало 0x5d91050

### изменена: 0x5df8350 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8dec0, стало 0x5d91040

### изменена: 0x5df8420 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8deb0, стало 0x5d91030

### изменена: 0x5df84f0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8dea0, стало 0x5d91020

### изменена: 0x5df85c0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8de90, стало 0x5d91010

### изменена: 0x5df8690 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8de80, стало 0x5d91000

### изменена: 0x5df8760 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8de70, стало 0x5d90ff0

### изменена: 0x5df8830 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8de60, стало 0x5d90fe0

### изменена: 0x5df8900 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8de50, стало 0x5d90fd0

### изменена: 0x5df89d0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8de40, стало 0x5d90fc0

### изменена: 0x5df8aa0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8de30, стало 0x5d90fb0

### изменена: 0x5df8b70 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8de20, стало 0x5d90fa0

### изменена: 0x5df8c40 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8de10, стало 0x5d90f90

### изменена: 0x5df8d10 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8de00, стало 0x5d90f80

### изменена: 0x5df8de0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8ddf0, стало 0x5d90f70

### изменена: 0x5df8eb0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8d3f0, стало 0x5d90570

### изменена: 0x5df8f80 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8d3e0, стало 0x5d90560

### изменена: 0x5df9050 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8d3d0, стало 0x5d90550

### изменена: 0x5df9120 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8d3c0, стало 0x5d90540

### изменена: 0x5df91f0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8d3b0, стало 0x5d90530

### изменена: 0x5df92c0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8d3a0, стало 0x5d90520

### изменена: 0x5df9390 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8d390, стало 0x5d90510

### изменена: 0x5df9460 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8d380, стало 0x5d90500

### изменена: 0x5df9530 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8d370, стало 0x5d904f0

### изменена: 0x5df9600 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8d360, стало 0x5d904e0

### изменена: 0x5df96d0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8d350, стало 0x5d904d0

### изменена: 0x5df97a0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8d340, стало 0x5d904c0

### изменена: 0x5df9870 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8d330, стало 0x5d904b0

### изменена: 0x5df9940 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8d320, стало 0x5d904a0

### изменена: 0x5df9a10 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8d310, стало 0x5d90490

### изменена: 0x5df9ae0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8d300, стало 0x5d90480

### изменена: 0x5df9bb0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8d2f0, стало 0x5d90470

### изменена: 0x5df9c80 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8d2e0, стало 0x5d90460

### изменена: 0x5df9d50 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8d2d0, стало 0x5d90450

### изменена: 0x5df9e20 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8d2c0, стало 0x5d90440

### изменена: 0x5df9ef0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8d2b0, стало 0x5d90430

### изменена: 0x5df9fc0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8d2a0, стало 0x5d90420

### изменена: 0x5dfa090 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8d290, стало 0x5d90410

### изменена: 0x5dfa160 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8d280, стало 0x5d90400

### изменена: 0x5dfa230 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8d270, стало 0x5d903f0

### изменена: 0x5dfa300 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8d260, стало 0x5d903e0

### изменена: 0x5dfa3d0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8d250, стало 0x5d903d0

### изменена: 0x5dfa4a0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8d240, стало 0x5d903c0

### изменена: 0x5dfa570 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8d230, стало 0x5d903b0

### изменена: 0x5dfa640 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8d220, стало 0x5d903a0

### изменена: 0x5dfa710 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8d210, стало 0x5d90390

### изменена: 0x5dfa7e0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8d200, стало 0x5d90380

### изменена: 0x5dfa8b0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8d1f0, стало 0x5d90370

### изменена: 0x5dfa980 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8d1e0, стало 0x5d90360

### изменена: 0x5dfaa50 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8d1d0, стало 0x5d90350

### изменена: 0x5dfab20 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8d1c0, стало 0x5d90340

### изменена: 0x5dfabf0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8d1b0, стало 0x5d90330

### изменена: 0x5dfacc0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8d1a0, стало 0x5d90320

### изменена: 0x5dfad90 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8d190, стало 0x5d90310

### изменена: 0x5dfae60 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8d180, стало 0x5d90300

### изменена: 0x5dfaf30 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8d170, стало 0x5d902f0

### изменена: 0x5dfb000 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8d160, стало 0x5d902e0

### изменена: 0x5dfb0d0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8d150, стало 0x5d902d0

### изменена: 0x5dfb1a0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8d140, стало 0x5d902c0

### изменена: 0x5dfb270 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8d130, стало 0x5d902b0

### изменена: 0x5dfb340 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8d120, стало 0x5d902a0

### изменена: 0x5dfb410 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8d110, стало 0x5d90290

### изменена: 0x5dfb4e0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8d100, стало 0x5d90280

### изменена: 0x5dfb5b0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8d0f0, стало 0x5d90270

### изменена: 0x5dfb680 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8d0e0, стало 0x5d90260

### изменена: 0x5dfb750 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8d0d0, стало 0x5d90250

### изменена: 0x5dfb820 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8d0c0, стало 0x5d90240

### изменена: 0x5dfb8f0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8d0b0, стало 0x5d90230

### изменена: 0x5dfb9c0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8d0a0, стало 0x5d90220

### изменена: 0x5dfba90 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8d090, стало 0x5d90210

### изменена: 0x5dfbb60 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8d080, стало 0x5d90200

### изменена: 0x5dfbc30 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8d070, стало 0x5d901f0

### изменена: 0x5dfbd00 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8d060, стало 0x5d901e0

### изменена: 0x5dfbdd0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8d050, стало 0x5d901d0

### изменена: 0x5dfbea0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8d040, стало 0x5d901c0

### изменена: 0x5dfbf70 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8d030, стало 0x5d901b0

### изменена: 0x5dfc040 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8d020, стало 0x5d901a0

### изменена: 0x5dfc110 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8d010, стало 0x5d90190

### изменена: 0x5dfc1e0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8d000, стало 0x5d90180

### изменена: 0x5dfc2b0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8cff0, стало 0x5d90170

### изменена: 0x5dfc380 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8cfe0, стало 0x5d90160

### изменена: 0x5dfc450 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8cfd0, стало 0x5d90150

### изменена: 0x5dfc520 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8cfc0, стало 0x5d90140

### изменена: 0x5dfc5f0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8cfb0, стало 0x5d90130

### изменена: 0x5dfc6c0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8cfa0, стало 0x5d90120

### изменена: 0x5dfc790 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8cf90, стало 0x5d90110

### изменена: 0x5dfc860 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8cf80, стало 0x5d90100

### изменена: 0x5dfc930 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8cf70, стало 0x5d900f0

### изменена: 0x5dfca00 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8cf60, стало 0x5d900e0

### изменена: 0x5dfcad0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8cf50, стало 0x5d900d0

### изменена: 0x5dfcba0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8cf40, стало 0x5d900c0

### изменена: 0x5dfcc70 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8cf30, стало 0x5d900b0

### изменена: 0x5dfcd40 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8cf20, стало 0x5d900a0

### изменена: 0x5dfce10 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8cf10, стало 0x5d90090

### изменена: 0x5dfcee0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8cf00, стало 0x5d90080

### изменена: 0x5dfcfb0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8cef0, стало 0x5d90070

### изменена: 0x5dfd080 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8cee0, стало 0x5d90060

### изменена: 0x5dfd150 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8ced0, стало 0x5d90050

### изменена: 0x5dfd220 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8cec0, стало 0x5d90040

### изменена: 0x5dfd2f0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8ceb0, стало 0x5d90030

### изменена: 0x5dfd3c0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8cea0, стало 0x5d90020

### изменена: 0x5dfd490 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8ce90, стало 0x5d90010

### изменена: 0x5dfd560 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8ce80, стало 0x5d90000

### изменена: 0x5dfd630 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8ce70, стало 0x5d8fff0

### изменена: 0x5dfd700 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8ce60, стало 0x5d8ffe0

### изменена: 0x5dfd7d0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8ce50, стало 0x5d8ffd0

### изменена: 0x5dfd8a0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8ce40, стало 0x5d8ffc0

### изменена: 0x5dfd970 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8ce30, стало 0x5d8ffb0

### изменена: 0x5dfda40 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8ce20, стало 0x5d8ffa0

### изменена: 0x5dfdb10 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8ce10, стало 0x5d8ff90

### изменена: 0x5dfdbe0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8ce00, стало 0x5d8ff80

### изменена: 0x5dfdcb0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8cdf0, стало 0x5d8ff70

### изменена: 0x5dfdd80 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8cde0, стало 0x5d8ff60

### изменена: 0x5dfde50 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8cdd0, стало 0x5d8ff50

### изменена: 0x5dfdf20 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8cdc0, стало 0x5d8ff40

### изменена: 0x5dfdff0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8cdb0, стало 0x5d8ff30

### изменена: 0x5dfe0c0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8cda0, стало 0x5d8ff20

### изменена: 0x5dfe190 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8cd90, стало 0x5d8ff10

### изменена: 0x5dfe260 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8cd80, стало 0x5d8ff00

### изменена: 0x5dfe330 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8cd70, стало 0x5d8fef0

### изменена: 0x5dfe400 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8cd60, стало 0x5d8fee0

### изменена: 0x5dfe4d0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8cd50, стало 0x5d8fed0

### изменена: 0x5dfe5a0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8cd40, стало 0x5d8fec0

### изменена: 0x5dfe670 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8cd30, стало 0x5d8feb0

### изменена: 0x5dfe740 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8cd20, стало 0x5d8fea0

### изменена: 0x5dfe810 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8cd10, стало 0x5d8fe90

### изменена: 0x5dfe8e0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8cd00, стало 0x5d8fe80

### изменена: 0x5dfe9b0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8ccf0, стало 0x5d8fe70

### изменена: 0x5dfea80 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8cce0, стало 0x5d8fe60

### изменена: 0x5dfeb50 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8ccd0, стало 0x5d8fe50

### изменена: 0x5dfec20 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8ccc0, стало 0x5d8fe40

### изменена: 0x5dfecf0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8ccb0, стало 0x5d8fe30

### изменена: 0x5dfedc0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8cca0, стало 0x5d8fe20

### изменена: 0x5dfee90 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8cc90, стало 0x5d8fe10

### изменена: 0x5dfef60 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8cc80, стало 0x5d8fe00

### изменена: 0x5dff030 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8cc70, стало 0x5d8fdf0

### изменена: 0x5dff100 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8cc60, стало 0x5d8fde0

### изменена: 0x5dff1d0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8cc50, стало 0x5d8fdd0

### изменена: 0x5dff2a0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8cc40, стало 0x5d8fdc0

### изменена: 0x5dff370 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8cc30, стало 0x5d8fdb0

### изменена: 0x5dff440 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8cc20, стало 0x5d8fda0

### изменена: 0x5dff510 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8cc10, стало 0x5d8fd90

### изменена: 0x5dff5e0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8cc00, стало 0x5d8fd80

### изменена: 0x5dff6b0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8cbf0, стало 0x5d8fd70

### изменена: 0x5dff780 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8cbe0, стало 0x5d8fd60

### изменена: 0x5dff850 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8cbd0, стало 0x5d8fd50

### изменена: 0x5dff920 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8cbc0, стало 0x5d8fd40

### изменена: 0x5dff9f0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8cbb0, стало 0x5d8fd30

### изменена: 0x5dffac0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8cba0, стало 0x5d8fd20

### изменена: 0x5dffb90 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8cb90, стало 0x5d8fd10

### изменена: 0x5dffc60 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8cb80, стало 0x5d8fd00

### изменена: 0x5dffd30 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8cb70, стало 0x5d8fcf0

### изменена: 0x5dffe00 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8cb60, стало 0x5d8fce0

### изменена: 0x5dffed0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8cb50, стало 0x5d8fcd0

### изменена: 0x5dfffa0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8cb40, стало 0x5d8fcc0

### изменена: 0x5e00070 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8cb30, стало 0x5d8fcb0

### изменена: 0x5e00140 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8cb20, стало 0x5d8fca0

### изменена: 0x5e00210 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8cb10, стало 0x5d8fc90

### изменена: 0x5e002e0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8cb00, стало 0x5d8fc80

### изменена: 0x5e003b0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8caf0, стало 0x5d8fc70

### изменена: 0x5e00480 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8cae0, стало 0x5d8fc60

### изменена: 0x5e00550 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8cad0, стало 0x5d8fc50

### изменена: 0x5e00620 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8cac0, стало 0x5d8fc40

### изменена: 0x5e006f0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8cab0, стало 0x5d8fc30

### изменена: 0x5e007c0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8caa0, стало 0x5d8fc20

### изменена: 0x5e00890 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8ca90, стало 0x5d8fc10

### изменена: 0x5e00960 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8ca80, стало 0x5d8fc00

### изменена: 0x5e00a30 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8ca70, стало 0x5d8fbf0

### изменена: 0x5e00b00 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8ca60, стало 0x5d8fbe0

### изменена: 0x5e00bd0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8ca50, стало 0x5d8fbd0

### изменена: 0x5e00ca0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8ca40, стало 0x5d8fbc0

### изменена: 0x5e00d70 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8ca30, стало 0x5d8fbb0

### изменена: 0x5e00e40 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8ca20, стало 0x5d8fba0

### изменена: 0x5e00f10 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8ca10, стало 0x5d8fb90

### изменена: 0x5e00fe0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8ca00, стало 0x5d8fb80

### изменена: 0x5e010b0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8c9f0, стало 0x5d8fb70

### изменена: 0x5e01180 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8c9e0, стало 0x5d8fb60

### изменена: 0x5e01250 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8c9d0, стало 0x5d8fb50

### изменена: 0x5e01320 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8c9c0, стало 0x5d8fb40

### изменена: 0x5e013f0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8c9b0, стало 0x5d8fb30

### изменена: 0x5e014c0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8c9a0, стало 0x5d8fb20

### изменена: 0x5e01590 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8c990, стало 0x5d8fb10

### изменена: 0x5e01660 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8c980, стало 0x5d8fb00

### изменена: 0x5e01730 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8c970, стало 0x5d8faf0

### изменена: 0x5e01800 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8c960, стало 0x5d8fae0

### изменена: 0x5e018d0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8c950, стало 0x5d8fad0

### изменена: 0x5e019a0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8c940, стало 0x5d8fac0

### изменена: 0x5e01a70 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8c930, стало 0x5d8fab0

### изменена: 0x5e01b40 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8c920, стало 0x5d8faa0

### изменена: 0x5e01c10 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8c910, стало 0x5d8fa90

### изменена: 0x5e01ce0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8c900, стало 0x5d8fa80

### изменена: 0x5e01db0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8c8f0, стало 0x5d8fa70

### изменена: 0x5e01e80 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8c8e0, стало 0x5d8fa60

### изменена: 0x5e01f50 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8c8d0, стало 0x5d8fa50

### изменена: 0x5e02020 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8c8c0, стало 0x5d8fa40

### изменена: 0x5e020f0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8c8b0, стало 0x5d8fa30

### изменена: 0x5e021c0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8c8a0, стало 0x5d8fa20

### изменена: 0x5e02290 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8c890, стало 0x5d8fa10

### изменена: 0x5e02360 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8c880, стало 0x5d8fa00

### изменена: 0x5e02430 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8c870, стало 0x5d8f9f0

### изменена: 0x5e02500 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8c860, стало 0x5d8f9e0

### изменена: 0x5e025d0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8c850, стало 0x5d8f9d0

### изменена: 0x5e026a0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8c840, стало 0x5d8f9c0

### изменена: 0x5e02770 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8c830, стало 0x5d8f9b0

### изменена: 0x5e02840 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8c820, стало 0x5d8f9a0

### изменена: 0x5e02910 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8c810, стало 0x5d8f990

### изменена: 0x5e029e0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8c800, стало 0x5d8f980

### изменена: 0x5e02ab0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8c7f0, стало 0x5d8f970

### изменена: 0x5e02b80 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8c7e0, стало 0x5d8f960

### изменена: 0x5e02c50 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8c7d0, стало 0x5d8f950

### изменена: 0x5e02d20 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8c7c0, стало 0x5d8f940

### изменена: 0x5e02df0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8c7b0, стало 0x5d8f930

### изменена: 0x5e02ec0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8c7a0, стало 0x5d8f920

### изменена: 0x5e02f90 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8c790, стало 0x5d8f910

### изменена: 0x5e03060 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8c780, стало 0x5d8f900

### изменена: 0x5e03130 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8c770, стало 0x5d8f8f0

### изменена: 0x5e03200 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8c760, стало 0x5d8f8e0

### изменена: 0x5e032d0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8c750, стало 0x5d8f8d0

### изменена: 0x5e033a0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8c740, стало 0x5d8f8c0

### изменена: 0x5e03470 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8c730, стало 0x5d8f8b0

### изменена: 0x5e03540 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8c720, стало 0x5d8f8a0

### изменена: 0x5e03610 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8c710, стало 0x5d8f890

### изменена: 0x5e036e0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8c700, стало 0x5d8f880

### изменена: 0x5e037b0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8c6f0, стало 0x5d8f870

### изменена: 0x5e03880 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8c6e0, стало 0x5d8f860

### изменена: 0x5e03950 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8c6d0, стало 0x5d8f850

### изменена: 0x5e03a20 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8c6c0, стало 0x5d8f840

### изменена: 0x5e03af0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8c6b0, стало 0x5d8f830

### изменена: 0x5e03bc0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8c6a0, стало 0x5d8f820

### изменена: 0x5e03c90 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8c690, стало 0x5d8f810

### изменена: 0x5e03d60 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8c680, стало 0x5d8f800

### изменена: 0x5e03e30 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8c670, стало 0x5d8f7f0

### изменена: 0x5e03f00 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8c660, стало 0x5d8f7e0

### изменена: 0x5e03fd0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8c650, стало 0x5d8f7d0

### изменена: 0x5e040a0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8c640, стало 0x5d8f7c0

### изменена: 0x5e04170 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8c630, стало 0x5d8f7b0

### изменена: 0x5e04240 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8c620, стало 0x5d8f7a0

### изменена: 0x5e04310 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8c610, стало 0x5d8f790

### изменена: 0x5e043e0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8c600, стало 0x5d8f780

### изменена: 0x5e044b0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8c5f0, стало 0x5d8f770

### изменена: 0x5e04580 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8c5e0, стало 0x5d8f760

### изменена: 0x5e04650 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8c5d0, стало 0x5d8f750

### изменена: 0x5e04720 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8c5c0, стало 0x5d8f740

### изменена: 0x5e047f0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8c5b0, стало 0x5d8f730

### изменена: 0x5e048c0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8c5a0, стало 0x5d8f720

### изменена: 0x5e04990 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8c590, стало 0x5d8f710

### изменена: 0x5e04a60 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8c580, стало 0x5d8f700

### изменена: 0x5e04b30 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8c570, стало 0x5d8f6f0

### изменена: 0x5e04c00 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8c560, стало 0x5d8f6e0

### изменена: 0x5e04cd0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8c550, стало 0x5d8f6d0

### изменена: 0x5e04da0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8c540, стало 0x5d8f6c0

### изменена: 0x5e04e70 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8c530, стало 0x5d8f6b0

### изменена: 0x5e04f40 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8c520, стало 0x5d8f6a0

### изменена: 0x5e05010 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8c510, стало 0x5d8f690

### изменена: 0x5e050e0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8c500, стало 0x5d8f680

### изменена: 0x5e051b0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8c4f0, стало 0x5d8f670

### изменена: 0x5e05280 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8c4e0, стало 0x5d8f660

### изменена: 0x5e05350 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8c4d0, стало 0x5d8f650

### изменена: 0x5e05420 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8c4c0, стало 0x5d8f640

### изменена: 0x5e054f0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8c4b0, стало 0x5d8f630

### изменена: 0x5e055c0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8c4a0, стало 0x5d8f620

### изменена: 0x5e05690 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8c490, стало 0x5d8f610

### изменена: 0x5e05760 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8c480, стало 0x5d8f600

### изменена: 0x5e05830 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8c470, стало 0x5d8f5f0

### изменена: 0x5e05900 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8c460, стало 0x5d8f5e0

### изменена: 0x5e059d0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8c450, стало 0x5d8f5d0

### изменена: 0x5e05aa0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8c440, стало 0x5d8f5c0

### изменена: 0x5e05b70 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8c430, стало 0x5d8f5b0

### изменена: 0x5e05c40 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8c420, стало 0x5d8f5a0

### изменена: 0x5e05d10 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8c410, стало 0x5d8f590

### изменена: 0x5e05de0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8c400, стало 0x5d8f580

### изменена: 0x5e05eb0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8c3f0, стало 0x5d8f570

### изменена: 0x5e05f80 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8c3e0, стало 0x5d8f560

### изменена: 0x5e06050 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8c3d0, стало 0x5d8f550

### изменена: 0x5e06120 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8c3c0, стало 0x5d8f540

### изменена: 0x5e061f0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8c3b0, стало 0x5d8f530

### изменена: 0x5e062c0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8c3a0, стало 0x5d8f520

### изменена: 0x5e06390 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8c390, стало 0x5d8f510

### изменена: 0x5e06460 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8c380, стало 0x5d8f500

### изменена: 0x5e06530 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8c370, стало 0x5d8f4f0

### изменена: 0x5e06600 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8c360, стало 0x5d8f4e0

### изменена: 0x5e066d0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8c350, стало 0x5d8f4d0

### изменена: 0x5e067a0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8c340, стало 0x5d8f4c0

### изменена: 0x5e06870 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8c330, стало 0x5d8f4b0

### изменена: 0x5e06940 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8c320, стало 0x5d8f4a0

### изменена: 0x5e06a10 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8c310, стало 0x5d8f490

### изменена: 0x5e06ae0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8c300, стало 0x5d8f480

### изменена: 0x5e06bb0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8c2f0, стало 0x5d8f470

### изменена: 0x5e06c80 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8c2e0, стало 0x5d8f460

### изменена: 0x5e06d50 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8c2d0, стало 0x5d8f450

### изменена: 0x5e06e20 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8c2c0, стало 0x5d8f440

### изменена: 0x5e06ef0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8c2b0, стало 0x5d8f430

### изменена: 0x5e06fc0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8c2a0, стало 0x5d8f420

### изменена: 0x5e07090 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8c290, стало 0x5d8f410

### изменена: 0x5e07160 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8c280, стало 0x5d8f400

### изменена: 0x5e07230 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8c270, стало 0x5d8f3f0

### изменена: 0x5e07300 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8c260, стало 0x5d8f3e0

### изменена: 0x5e073d0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8c250, стало 0x5d8f3d0

### изменена: 0x5e074a0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8c240, стало 0x5d8f3c0

### изменена: 0x5e07570 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8c230, стало 0x5d8f3b0

### изменена: 0x5e07640 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8c220, стало 0x5d8f3a0

### изменена: 0x5e07710 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8c210, стало 0x5d8f390

### изменена: 0x5e077e0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8c200, стало 0x5d8f380

### изменена: 0x5e078b0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8c1f0, стало 0x5d8f370

### изменена: 0x5e07980 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8c1e0, стало 0x5d8f360

### изменена: 0x5e07a50 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8c1d0, стало 0x5d8f350

### изменена: 0x5e07b20 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8c1c0, стало 0x5d8f340

### изменена: 0x5e07bf0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8c1b0, стало 0x5d8f330

### изменена: 0x5e07cc0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8c1a0, стало 0x5d8f320

### изменена: 0x5e07d90 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8c190, стало 0x5d8f310

### изменена: 0x5e07e60 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8c180, стало 0x5d8f300

### изменена: 0x5e07f30 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8c170, стало 0x5d8f2f0

### изменена: 0x5e08000 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8c160, стало 0x5d8f2e0

### изменена: 0x5e080d0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8c150, стало 0x5d8f2d0

### изменена: 0x5e081a0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8c140, стало 0x5d8f2c0

### изменена: 0x5e08270 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8c130, стало 0x5d8f2b0

### изменена: 0x5e08340 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8c120, стало 0x5d8f2a0

### изменена: 0x5e08410 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8c110, стало 0x5d8f290

### изменена: 0x5e084e0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8c100, стало 0x5d8f280

### изменена: 0x5e085b0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8c0f0, стало 0x5d8f270

### изменена: 0x5e08680 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8c0e0, стало 0x5d8f260

### изменена: 0x5e08750 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8c0d0, стало 0x5d8f250

### изменена: 0x5e08820 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8c0c0, стало 0x5d8f240

### изменена: 0x5e088f0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8c0b0, стало 0x5d8f230

### изменена: 0x5e089c0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8c0a0, стало 0x5d8f220

### изменена: 0x5e08a90 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8c090, стало 0x5d8f210

### изменена: 0x5e08b60 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8c080, стало 0x5d8f200

### изменена: 0x5e08c30 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8c070, стало 0x5d8f1f0

### изменена: 0x5e08d00 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8c060, стало 0x5d8f1e0

### изменена: 0x5e08dd0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8c050, стало 0x5d8f1d0

### изменена: 0x5e08ea0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8c040, стало 0x5d8f1c0

### изменена: 0x5e08f70 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8c030, стало 0x5d8f1b0

### изменена: 0x5e09040 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8c020, стало 0x5d8f1a0

### изменена: 0x5e09110 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8c010, стало 0x5d8f190

### изменена: 0x5e091e0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8c000, стало 0x5d8f180

### изменена: 0x5e092b0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8bff0, стало 0x5d8f170

### изменена: 0x5e09380 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8bfe0, стало 0x5d8f160

### изменена: 0x5e09450 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8bfd0, стало 0x5d8f150

### изменена: 0x5e09520 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8bfc0, стало 0x5d8f140

### изменена: 0x5e095f0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8bfb0, стало 0x5d8f130

### изменена: 0x5e096c0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8bfa0, стало 0x5d8f120

### изменена: 0x5e09790 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8bf90, стало 0x5d8f110

### изменена: 0x5e09860 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8bf80, стало 0x5d8f100

### изменена: 0x5e09930 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8bf70, стало 0x5d8f0f0

### изменена: 0x5e09a00 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8bf60, стало 0x5d8f0e0

### изменена: 0x5e09ad0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8bf50, стало 0x5d8f0d0

### изменена: 0x5e09ba0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8bf40, стало 0x5d8f0c0

### изменена: 0x5e09c70 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8bf30, стало 0x5d8f0b0

### изменена: 0x5e09d40 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8bf20, стало 0x5d8f0a0

### изменена: 0x5e09e10 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8bf10, стало 0x5d8f090

### изменена: 0x5e09ee0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8bf00, стало 0x5d8f080

### изменена: 0x5e09fb0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8bef0, стало 0x5d8f070

### изменена: 0x5e0a080 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8bee0, стало 0x5d8f060

### изменена: 0x5e0a150 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8bed0, стало 0x5d8f050

### изменена: 0x5e0a220 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8bec0, стало 0x5d8f040

### изменена: 0x5e0a2f0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8beb0, стало 0x5d8f030

### изменена: 0x5e0a3c0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8bea0, стало 0x5d8f020

### изменена: 0x5e0a490 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8be90, стало 0x5d8f010

### изменена: 0x5e0a560 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8be80, стало 0x5d8f000

### изменена: 0x5e0a630 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8be70, стало 0x5d8eff0

### изменена: 0x5e0a700 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8be60, стало 0x5d8efe0

### изменена: 0x5e0a7d0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8be50, стало 0x5d8efd0

### изменена: 0x5e0a8a0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8be40, стало 0x5d8efc0

### изменена: 0x5e0a970 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8be30, стало 0x5d8efb0

### изменена: 0x5e0aa40 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8be20, стало 0x5d8efa0

### изменена: 0x5e0ab10 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8be10, стало 0x5d8ef90

### изменена: 0x5e0abe0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8be00, стало 0x5d8ef80

### изменена: 0x5e0acb0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8bdf0, стало 0x5d8ef70

### изменена: 0x5e0ad80 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8bde0, стало 0x5d8ef60

### изменена: 0x5e0ae50 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8bdd0, стало 0x5d8ef50

### изменена: 0x5e0af20 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8bdc0, стало 0x5d8ef40

### изменена: 0x5e0aff0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8bdb0, стало 0x5d8ef30

### изменена: 0x5e0b0c0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8bda0, стало 0x5d8ef20

### изменена: 0x5e0b190 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8bd90, стало 0x5d8ef10

### изменена: 0x5e0b260 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8bd80, стало 0x5d8ef00

### изменена: 0x5e0b330 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8bd70, стало 0x5d8eef0

### изменена: 0x5e0b400 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8bd60, стало 0x5d8eee0

### изменена: 0x5e0b4d0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8bd50, стало 0x5d8eed0

### изменена: 0x5e0b5a0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8bd40, стало 0x5d8eec0

### изменена: 0x5e0b670 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8bd30, стало 0x5d8eeb0

### изменена: 0x5e0b740 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8bd20, стало 0x5d8eea0

### изменена: 0x5e0b810 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8bd10, стало 0x5d8ee90

### изменена: 0x5e0b8e0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8bd00, стало 0x5d8ee80

### изменена: 0x5e0b9b0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8bcf0, стало 0x5d8ee70

### изменена: 0x5e0ba80 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8bce0, стало 0x5d8ee60

### изменена: 0x5e0bb50 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8bcd0, стало 0x5d8ee50

### изменена: 0x5e0bc20 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8bcc0, стало 0x5d8ee40

### изменена: 0x5e0bcf0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8bcb0, стало 0x5d8ee30

### изменена: 0x5e0bdc0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8bca0, стало 0x5d8ee20

### изменена: 0x5e0be90 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8bc90, стало 0x5d8ee10

### изменена: 0x5e0bf60 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8bc80, стало 0x5d8ee00

### изменена: 0x5e0c030 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8bc70, стало 0x5d8edf0

### изменена: 0x5e0c100 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8bc60, стало 0x5d8ede0

### изменена: 0x5e0c1d0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8bc50, стало 0x5d8edd0

### изменена: 0x5e0c2a0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8bc40, стало 0x5d8edc0

### изменена: 0x5e0c370 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8bc30, стало 0x5d8edb0

### изменена: 0x5e0c440 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8bc20, стало 0x5d8eda0

### изменена: 0x5e0c510 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8bc10, стало 0x5d8ed90

### изменена: 0x5e0c5e0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8bc00, стало 0x5d8ed80

### изменена: 0x5e0c6b0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8bbf0, стало 0x5d8ed70

### изменена: 0x5e0c780 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8bbe0, стало 0x5d8ed60

### изменена: 0x5e0c850 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8bbd0, стало 0x5d8ed50

### изменена: 0x5e0c920 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8bbc0, стало 0x5d8ed40

### изменена: 0x5e0c9f0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8bbb0, стало 0x5d8ed30

### изменена: 0x5e0cac0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8bba0, стало 0x5d8ed20

### изменена: 0x5e0cb90 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8bb90, стало 0x5d8ed10

### изменена: 0x5e0cc60 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8bb80, стало 0x5d8ed00

### изменена: 0x5e0cd30 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8bb70, стало 0x5d8ecf0

### изменена: 0x5e0ce00 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8bb60, стало 0x5d8ece0

### изменена: 0x5e0ced0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8bb50, стало 0x5d8ecd0

### изменена: 0x5e0cfa0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8bb40, стало 0x5d8ecc0

### изменена: 0x5e0d070 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8bb30, стало 0x5d8ecb0

### изменена: 0x5e0d140 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8bb20, стало 0x5d8eca0

### изменена: 0x5e0d210 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8bb10, стало 0x5d8ec90

### изменена: 0x5e0d2e0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8bb00, стало 0x5d8ec80

### изменена: 0x5e0d3b0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8baf0, стало 0x5d8ec70

### изменена: 0x5e0d480 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8bae0, стало 0x5d8ec60

### изменена: 0x5e0d550 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8bad0, стало 0x5d8ec50

### изменена: 0x5e0d620 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8bac0, стало 0x5d8ec40

### изменена: 0x5e0d6f0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8bab0, стало 0x5d8ec30

### изменена: 0x5e0d7c0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8baa0, стало 0x5d8ec20

### изменена: 0x5e0d890 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8ba90, стало 0x5d8ec10

### изменена: 0x5e0d960 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8ba80, стало 0x5d8ec00

### изменена: 0x5e0da30 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8ba70, стало 0x5d8ebf0

### изменена: 0x5e0db00 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8ba60, стало 0x5d8ebe0

### изменена: 0x5e0dbd0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8ba50, стало 0x5d8ebd0

### изменена: 0x5e0dca0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8ba40, стало 0x5d8ebc0

### изменена: 0x5e0dd70 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8ba30, стало 0x5d8ebb0

### изменена: 0x5e0de40 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8ba20, стало 0x5d8eba0

### изменена: 0x5e0df10 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8ba10, стало 0x5d8eb90

### изменена: 0x5e0dfe0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8ba00, стало 0x5d8eb80

### изменена: 0x5e0e0b0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8b9f0, стало 0x5d8eb70

### изменена: 0x5e0e180 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8b9e0, стало 0x5d8eb60

### изменена: 0x5e0e250 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8b9d0, стало 0x5d8eb50

### изменена: 0x5e0e320 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8b9c0, стало 0x5d8eb40

### изменена: 0x5e0e3f0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8b9b0, стало 0x5d8eb30

### изменена: 0x5e0e4c0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8b9a0, стало 0x5d8eb20

### изменена: 0x5e0e590 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8b990, стало 0x5d8eb10

### изменена: 0x5e0e660 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8b980, стало 0x5d8eb00

### изменена: 0x5e0e730 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8b970, стало 0x5d8eaf0

### изменена: 0x5e0e800 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8b960, стало 0x5d8eae0

### изменена: 0x5e0e8d0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8b950, стало 0x5d8ead0

### изменена: 0x5e0e9a0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8b940, стало 0x5d8eac0

### изменена: 0x5e0ea70 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8b930, стало 0x5d8eab0

### изменена: 0x5e0eb40 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8b920, стало 0x5d8eaa0

### изменена: 0x5e0ec10 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8b910, стало 0x5d8ea90

### изменена: 0x5e0ece0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8b900, стало 0x5d8ea80

### изменена: 0x5e0edb0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8b8f0, стало 0x5d8ea70

### изменена: 0x5e0ee80 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8b8e0, стало 0x5d8ea60

### изменена: 0x5e0ef50 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8b8d0, стало 0x5d8ea50

### изменена: 0x5e0f020 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8b8c0, стало 0x5d8ea40

### изменена: 0x5e0f0f0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8b8b0, стало 0x5d8ea30

### изменена: 0x5e0f1c0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8b8a0, стало 0x5d8ea20

### изменена: 0x5e0f290 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8b890, стало 0x5d8ea10

### изменена: 0x5e0f360 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8b880, стало 0x5d8ea00

### изменена: 0x5e0f430 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8b870, стало 0x5d8e9f0

### изменена: 0x5e0f500 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8b860, стало 0x5d8e9e0

### изменена: 0x5e0f5d0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8b850, стало 0x5d8e9d0

### изменена: 0x5e0f6a0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8b840, стало 0x5d8e9c0

### изменена: 0x5e0f770 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8b830, стало 0x5d8e9b0

### изменена: 0x5e0f840 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8b820, стало 0x5d8e9a0

### изменена: 0x5e0f910 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8b810, стало 0x5d8e990

### изменена: 0x5e0f9e0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8b800, стало 0x5d8e980

### изменена: 0x5e0fab0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8b7f0, стало 0x5d8e970

### изменена: 0x5e0fb80 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8b7e0, стало 0x5d8e960

### изменена: 0x5e0fc50 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8b7d0, стало 0x5d8e950

### изменена: 0x5e0fd20 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8b7c0, стало 0x5d8e940

### изменена: 0x5e0fdf0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8b7b0, стало 0x5d8e930

### изменена: 0x5e0fec0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8b7a0, стало 0x5d8e920

### изменена: 0x5e0ff90 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8b790, стало 0x5d8e910

### изменена: 0x5e10060 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8b780, стало 0x5d8e900

### изменена: 0x5e10130 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8b770, стало 0x5d8e8f0

### изменена: 0x5e10200 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8b760, стало 0x5d8e8e0

### изменена: 0x5e102d0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8b750, стало 0x5d8e8d0

### изменена: 0x5e103a0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8b740, стало 0x5d8e8c0

### изменена: 0x5e10470 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8b730, стало 0x5d8e8b0

### изменена: 0x5e10540 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8b720, стало 0x5d8e8a0

### изменена: 0x5e10610 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8b710, стало 0x5d8e890

### изменена: 0x5e106e0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8b700, стало 0x5d8e880

### изменена: 0x5e107b0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8b6f0, стало 0x5d8e870

### изменена: 0x5e10880 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8b6e0, стало 0x5d8e860

### изменена: 0x5e10950 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8b6d0, стало 0x5d8e850

### изменена: 0x5e10a20 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8b6c0, стало 0x5d8e840

### изменена: 0x5e10af0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8b6b0, стало 0x5d8e830

### изменена: 0x5e10bc0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8b6a0, стало 0x5d8e820

### изменена: 0x5e10c90 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8b690, стало 0x5d8e810

### изменена: 0x5e10d60 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8b680, стало 0x5d8e800

### изменена: 0x5e10e30 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8b600, стало 0x5d8e7f0

### изменена: 0x5e10f00 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8b610, стало 0x5d8e770

### изменена: 0x5e10fd0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8b620, стало 0x5d8e780

### изменена: 0x5e110a0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8b630, стало 0x5d8e790

### изменена: 0x5e11170 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8b640, стало 0x5d8e7a0

### изменена: 0x5e11240 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8b650, стало 0x5d8e7b0

### изменена: 0x5e11310 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8b660, стало 0x5d8e7c0

### изменена: 0x5e113e0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8b5f0, стало 0x5d8e7d0

### изменена: 0x5e114b0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d8b5e0, стало 0x5d8e760

### изменена: 0x5e11e40 (63 байт)
- код тот же, но вызывает другую функцию: было 0x5d8ddc0, стало 0x5d90f40

### изменена: 0x5e11e80 (63 байт)
- код тот же, но вызывает другую функцию: было 0x5d8dd90, стало 0x5d90f10

### изменена: 0x5e11ec0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x5d8dd60, стало 0x5d90ee0

### изменена: 0x5e11f00 (63 байт)
- код тот же, но вызывает другую функцию: было 0x5d8dd30, стало 0x5d90eb0

### изменена: 0x5e11f40 (63 байт)
- код тот же, но вызывает другую функцию: было 0x5d8dcd0, стало 0x5d90e50

### изменена: 0x5e11f80 (63 байт)
- код тот же, но вызывает другую функцию: было 0x5d8dca0, стало 0x5d90e20

### изменена: 0x5e11fc0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x5d8dc70, стало 0x5d90df0

### изменена: 0x5e12000 (63 байт)
- код тот же, но вызывает другую функцию: было 0x5d8dc40, стало 0x5d90dc0

### изменена: 0x5e12040 (63 байт)
- код тот же, но вызывает другую функцию: было 0x5d8dc10, стало 0x5d90d90

### изменена: 0x5e12080 (63 байт)
- код тот же, но вызывает другую функцию: было 0x5d8dbe0, стало 0x5d90d60

### изменена: 0x5e120c0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x5d8dbb0, стало 0x5d90d30

### изменена: 0x5e12100 (63 байт)
- код тот же, но вызывает другую функцию: было 0x5d8db80, стало 0x5d90d00

### изменена: 0x5e12140 (63 байт)
- код тот же, но вызывает другую функцию: было 0x5d8db50, стало 0x5d90cd0

### изменена: 0x5e12180 (63 байт)
- код тот же, но вызывает другую функцию: было 0x5d8db20, стало 0x5d90ca0

### изменена: 0x5e121c0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x5d8daf0, стало 0x5d90c70

### изменена: 0x5e12200 (63 байт)
- код тот же, но вызывает другую функцию: было 0x5d8dac0, стало 0x5d90c40

### изменена: 0x5e12240 (63 байт)
- код тот же, но вызывает другую функцию: было 0x5d8da90, стало 0x5d90c10

### изменена: 0x5e12280 (63 байт)
- код тот же, но вызывает другую функцию: было 0x5d8da60, стало 0x5d90be0

### изменена: 0x5e122c0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x5d8da30, стало 0x5d90bb0

### изменена: 0x5e12300 (63 байт)
- код тот же, но вызывает другую функцию: было 0x5d8da00, стало 0x5d90b80

### изменена: 0x5e12340 (63 байт)
- код тот же, но вызывает другую функцию: было 0x5d8d9d0, стало 0x5d90b50

### изменена: 0x5e12380 (63 байт)
- код тот же, но вызывает другую функцию: было 0x5d8d9a0, стало 0x5d90b20

### изменена: 0x5e123c0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x5d8d970, стало 0x5d90af0

### изменена: 0x5e12400 (63 байт)
- код тот же, но вызывает другую функцию: было 0x5d8d940, стало 0x5d90ac0

### изменена: 0x5e12440 (63 байт)
- код тот же, но вызывает другую функцию: было 0x5d8d910, стало 0x5d90a90

### изменена: 0x5e12480 (63 байт)
- код тот же, но вызывает другую функцию: было 0x5d8d8e0, стало 0x5d90a60

### изменена: 0x5e124c0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x5d8d8b0, стало 0x5d90a30

### изменена: 0x5e12500 (63 байт)
- код тот же, но вызывает другую функцию: было 0x5d8d880, стало 0x5d90a00

### изменена: 0x5e12540 (63 байт)
- код тот же, но вызывает другую функцию: было 0x5d8d850, стало 0x5d909d0

### изменена: 0x5e12580 (63 байт)
- код тот же, но вызывает другую функцию: было 0x5d8d820, стало 0x5d909a0

### изменена: 0x5e125c0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x5d8d7f0, стало 0x5d90970

### изменена: 0x5e12600 (63 байт)
- код тот же, но вызывает другую функцию: было 0x5d8d7c0, стало 0x5d90940

### изменена: 0x5e12640 (63 байт)
- код тот же, но вызывает другую функцию: было 0x5d8d790, стало 0x5d90910

### изменена: 0x5e12680 (63 байт)
- код тот же, но вызывает другую функцию: было 0x5d8d760, стало 0x5d908e0

### изменена: 0x5e126c0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x5d8d730, стало 0x5d908b0

### изменена: 0x5e12700 (63 байт)
- код тот же, но вызывает другую функцию: было 0x5d8d700, стало 0x5d90880

### изменена: 0x5e12740 (63 байт)
- код тот же, но вызывает другую функцию: было 0x5d8d6d0, стало 0x5d90850

### изменена: 0x5e12780 (63 байт)
- код тот же, но вызывает другую функцию: было 0x5d8d6a0, стало 0x5d90820

### изменена: 0x5e127c0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x5d8d670, стало 0x5d907f0

### изменена: 0x5e12800 (63 байт)
- код тот же, но вызывает другую функцию: было 0x5d8d640, стало 0x5d907c0

### изменена: 0x5e12840 (63 байт)
- код тот же, но вызывает другую функцию: было 0x5d8d610, стало 0x5d90790

### изменена: 0x5e12880 (63 байт)
- код тот же, но вызывает другую функцию: было 0x5d8d5e0, стало 0x5d90760

### изменена: 0x5e128c0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x5d8d5b0, стало 0x5d90730

### изменена: 0x5e12900 (63 байт)
- код тот же, но вызывает другую функцию: было 0x5d8d580, стало 0x5d90700

### изменена: 0x5e12940 (63 байт)
- код тот же, но вызывает другую функцию: было 0x5d8d550, стало 0x5d906d0

### изменена: 0x5e12980 (63 байт)
- код тот же, но вызывает другую функцию: было 0x5d8d520, стало 0x5d906a0

### изменена: 0x5e129c0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x5d8d4f0, стало 0x5d90670

### изменена: 0x5e12a00 (63 байт)
- код тот же, но вызывает другую функцию: было 0x5d8d4c0, стало 0x5d90640

### изменена: 0x5e12a40 (63 байт)
- код тот же, но вызывает другую функцию: было 0x5d8d490, стало 0x5d90610

### изменена: 0x5e12a80 (63 байт)
- код тот же, но вызывает другую функцию: было 0x5d8d460, стало 0x5d905e0

### изменена: 0x5e12ac0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x5d8d430, стало 0x5d905b0

### изменена: 0x5e12b00 (63 байт)
- код тот же, но вызывает другую функцию: было 0x5d8d400, стало 0x5d90580

### изменена: 0x5e12bc0 (111 байт) | строки: "GameTime_t"
- код тот же, но вызывает другую функцию: было 0x5d8dd00, стало 0x5d90e80

### изменена: 0x5e3e5d0 (2934 байт)
- код тот же, но вызывает другую функцию: было 0x5de39a0, стало 0x5de6cd0

### изменена: 0x5ecaee0 (778 байт)
- код тот же, но вызывает другую функцию: было 0x5de69d0, стало 0x5de9d10

### добавлена: 0x5d95d40 (132 байт) | строки: "CDOTA_Ability_Special_Bonus_HP_Regen_4_5"

### добавлена: 0x5f35c00 (444 байт) | строки: "C_DOTA_Ability_Special_Bonus_HP_Regen_4_5"

### добавлена: 0x600c170 (7976 байт) | строки: "DotaRefractionColor"; "DotaReflectionDepth"; "setting.shaderquality"; "DotaClearRefractionColorAndDepth"; "DotaRefraction"; "StaticOverlayLayer"; "OcclusionQueryIssueLayer"; "Translucent Forward"

### добавлена: 0x601a020 (12427 байт) вызывается из: CDotaAddWaterReflectionViews::vfunc#1 | строки: "Water Reflection Stencil View"; "DotaReflectionDepth"; "DotaReflectionColor"; "DotaClearWaterStencil"; "Depth"; "DotaRenderWaterStencil"; "Water Reflection View"; "DotaReflectionBlack"

### удалена: 0x6008870 (13888 байт) вызывается из: CDotaAddWaterReflectionViews::vfunc#1 | строки: "Water Refraction View"; "DotaRefractionColor"; "DotaReflectionDepth"; "setting.shaderquality"; "DotaRefraction"; "StaticOverlayLayer"; "OcclusionQueryIssueLayer"; "Translucent Forward"

### удалена: 0x6018740 (4867 байт) CDotaAddWaterReflectionViews::vfunc#6 | строки: "DotaReflectionColor"; "DotaReflectionDepth"; "Depth"; "DotaReflectionBlack"; "White Quad"; "DotaReflectionSkybox"; "DotaClearReflectionColorAndDepth"

### копии существующего кода (18): шаблонные / склеенные компоновщиком функции, такой же код есть и в другой сборке — не новый код
- ещё одна копия существующего кода: 0x4c8dc50 (19 байт) вызывается из: CDOTA_Modifier_Wisp_Relocate_Thinker::vfunc#88
- ещё одна копия существующего кода: 0x4cfc8c0 (48 байт)
- ещё одна копия существующего кода: 0x5d846b0 (8 байт) C_DOTA_Ability_Special_Bonus_HP_Regen_80::vfunc#330 | строки: "modifier_special_bonus_hp_regen"
- ещё одна копия существующего кода: 0x5d897b0 (8 байт) C_DOTA_Ability_Special_Bonus_Unique_Mirana_7::vfunc#0
- ещё одна копия существующего кода: 0x5d897c0 (1 байт) C_DOTA_Ability_Special_Bonus_Unique_Mirana_7::vfunc#230
- ещё одна копия существующего кода: 0x5d897e0 (6 байт) CDOTA_Modifier_Special_Bonus_Gold::IsHidden
- ещё одна копия существующего кода: 0x5d92270 (12 байт) CBaseTrackedStatsEntity::vfunc#49
- ещё одна копия существующего кода: 0x5dc22e0 (19 байт) C_DOTA_Ability_CDOTA_Ability_Special_Bonus_Unique_Muerta_TrickShotCharges::vfunc#5
- ещё одна копия существующего кода: 0x5dc2300 (49 байт) C_DOTA_Ability_CDOTA_Ability_Special_Bonus_Unique_Muerta_TrickShotCharges::vfunc#6
- ещё одна копия существующего кода: 0x5ddd6c0 (126 байт)
- ещё одна копия существующего кода: 0x5de3b90 (1 байт)
- ещё одна копия существующего кода: 0x5de3c00 (1 байт)
- ещё одна копия существующего кода: 0x5de9d00 (5 байт)
- ещё одна копия существующего кода: 0x5de9d10 (5 байт)
- ещё одна копия существующего кода: 0x5e11580 (206 байт)
- ещё одна копия существующего кода: 0x5e2ca50 (92 байт) CMatchTrackedStatsEntity::vfunc#50
- ещё одна копия существующего кода: 0x6c49ca0 (239 байт) вызывается из: CDOTA_PortraitWorldRenderer::vfunc#2
- одной копией существующего кода меньше: 0x5ff5120 (239 байт) вызывается из: CDOTA_PortraitWorldRenderer::vfunc#2

## libserver.so: функций 221931 → 221948; без изменений 220383, изменено 1533, добавлено 7, удалено 5

### изменена: 0x3bf9340 (808 байт) вызывается из: CDOTA_NPCSpawnerGoodTop::vfunc#22, CDOTA_Ability_Lua::GetIntrinsicModifierName, CDOTA_Ability_Lua::GetAssociatedPrimaryAbilities | строки: "Y<R"; "%g %g %g"; "%g %g %g %g"; "(null)"; "false"; "true"; "%llu"; "%lld"
было: 0x3bf6880 (808 байт)
- строки: +"Y<R"
- инструкций: 203 → 203
```diff
@@ -36,5 +36,5 @@
 cmp al, 0x4f
 ja L
-lea rcx, [D]
+lea rcx, [S:"Y<R"]
 movzx edx, al
 movsxd rdx, dword ptr [rcx + rdx*4]
```

### изменена: 0x3bfada0 (238 байт)
было: 0x3bf82e0 (238 байт)
- строки: −"_TR"
- инструкций: 65 → 65
```diff
@@ -2,5 +2,5 @@
 ja L
 push rbp
-lea rdx, [S:"_TR"]
+lea rdx, [D]
 mov edi, edi
 mov rbp, rsp
```

### изменена: 0x3bfca40 (323 байт) | строки: "CUtlSymbolLarge"; "CNetworkUtlVectorBase"
было: 0x3bf9f80 (323 байт)
- строки: −"LpR"
- инструкций: 99 → 99
```diff
@@ -2,5 +2,5 @@
 ja L
 push rbp
-lea rdx, [S:"LpR"]
+lea rdx, [D]
 mov edi, edi
 mov rbp, rsp
```

### изменена: 0x3bfcbf0 (317 байт)
было: 0x3bfa130 (317 байт)
- строки: −"hrR"
- инструкций: 98 → 98
```diff
@@ -7,5 +7,5 @@
 push rbx
 ja L
-lea rdx, [S:"hrR"]
+lea rdx, [D]
 mov edi, edi
 mov rbx, rsi
```

### изменена: 0x3c29000 (1047 байт) | строки: "3 U"; "Unsupported KV3 basic type '%s' (%d)!"; "Pointers cannot be used as numeric values"
было: 0x3c26540 (1047 байт)
- строки: +"3 U"
- инструкций: 245 → 245
```diff
@@ -47,5 +47,5 @@
 cmp r8b, 6
 ja L
-lea rcx, [D]
+lea rcx, [S:"3 U"]
 movzx edx, r8b
 movsxd rdx, dword ptr [rcx + rdx*4]
```

### изменена: 0x3c29420 (1047 байт) | строки: "7$U"; "Unsupported KV3 basic type '%s' (%d)!"; "Pointers cannot be used as numeric values"
было: 0x3c26960 (1047 байт)
- строки: +"7$U"
- инструкций: 245 → 245
```diff
@@ -47,5 +47,5 @@
 cmp r8b, 6
 ja L
-lea rcx, [D]
+lea rcx, [S:"7$U"]
 movzx edx, r8b
 movsxd rdx, dword ptr [rcx + rdx*4]
```

### изменена: 0x3c29840 (1047 байт) | строки: ";(U"; "Unsupported KV3 basic type '%s' (%d)!"; "Pointers cannot be used as numeric values"
было: 0x3c26d80 (1047 байт)
- строки: +";(U"
- инструкций: 245 → 245
```diff
@@ -47,5 +47,5 @@
 cmp r8b, 6
 ja L
-lea rcx, [D]
+lea rcx, [S:";(U"]
 movzx edx, r8b
 movsxd rdx, dword ptr [rcx + rdx*4]
```

### изменена: 0x3c29c60 (1047 байт) | строки: "?,U"; "Unsupported KV3 basic type '%s' (%d)!"; "Pointers cannot be used as numeric values"
было: 0x3c271a0 (1047 байт)
- строки: +"?,U"
- инструкций: 245 → 245
```diff
@@ -47,5 +47,5 @@
 cmp r8b, 6
 ja L
-lea rcx, [D]
+lea rcx, [S:"?,U"]
 movzx edx, r8b
 movsxd rdx, dword ptr [rcx + rdx*4]
```

### изменена: 0x3c2a080 (1047 байт) | строки: "C0U"; "Unsupported KV3 basic type '%s' (%d)!"; "Pointers cannot be used as numeric values"
было: 0x3c275c0 (1047 байт)
- строки: +"C0U"
- инструкций: 245 → 245
```diff
@@ -47,5 +47,5 @@
 cmp r8b, 6
 ja L
-lea rcx, [D]
+lea rcx, [S:"C0U"]
 movzx edx, r8b
 movsxd rdx, dword ptr [rcx + rdx*4]
```

### изменена: 0x3c2a4a0 (1047 байт) | строки: "G4U"; "Unsupported KV3 basic type '%s' (%d)!"; "Pointers cannot be used as numeric values"
было: 0x3c279e0 (1047 байт)
- строки: +"G4U"
- инструкций: 245 → 245
```diff
@@ -47,5 +47,5 @@
 cmp r8b, 6
 ja L
-lea rcx, [D]
+lea rcx, [S:"G4U"]
 movzx edx, r8b
 movsxd rdx, dword ptr [rcx + rdx*4]
```

### изменена: 0x3c2a8c0 (1047 байт) | строки: "K8U"; "Unsupported KV3 basic type '%s' (%d)!"; "Pointers cannot be used as numeric values"
было: 0x3c27e00 (1047 байт)
- строки: +"K8U"
- инструкций: 245 → 245
```diff
@@ -47,5 +47,5 @@
 cmp r8b, 6
 ja L
-lea rcx, [D]
+lea rcx, [S:"K8U"]
 movzx edx, r8b
 movsxd rdx, dword ptr [rcx + rdx*4]
```

### изменена: 0x3c2b640 (1047 байт) | строки: "Unsupported KV3 basic type '%s' (%d)!"; "Pointers cannot be used as numeric values"
было: 0x3c28b80 (1047 байт)
- строки: −"oDU"
- инструкций: 245 → 245
```diff
@@ -47,5 +47,5 @@
 cmp r8b, 6
 ja L
-lea rcx, [S:"oDU"]
+lea rcx, [D]
 movzx edx, r8b
 movsxd rdx, dword ptr [rcx + rdx*4]
```

### изменена: 0x3c2ba60 (1047 байт) | строки: "Unsupported KV3 basic type '%s' (%d)!"; "Pointers cannot be used as numeric values"
было: 0x3c28fa0 (1047 байт)
- строки: −"sHU"
- инструкций: 245 → 245
```diff
@@ -47,5 +47,5 @@
 cmp r8b, 6
 ja L
-lea rcx, [S:"sHU"]
+lea rcx, [D]
 movzx edx, r8b
 movsxd rdx, dword ptr [rcx + rdx*4]
```

### изменена: 0x3c2d370 (951 байт) | строки: "IKV3TransferInterface_GameTime_Load"
было: 0x3c2a8b0 (951 байт)
- строки: −"NdU"
- инструкций: 235 → 235
```diff
@@ -63,5 +63,5 @@
 cmp al, 6
 ja L
-lea rdx, [S:"NdU"]
+lea rdx, [D]
 movzx eax, al
 movsxd rax, dword ptr [rdx + rax*4]
```

### изменена: 0x3c6c220 (715 байт) CDOTA_NPCSpawnerGoodTop::vfunc#51, CDOTA_NPCSpawnerGoodMid::vfunc#51, CDOTA_NPCSpawnerGoodBot::vfunc#51 | строки: "disableshadows"; "7.Y"; "disablereceiveshadows"; "ownername"; "O.Y"
было: 0x3c69760 (715 байт)
- строки: +"7.Y" +"O.Y"
- инструкций: 189 → 189
```diff
@@ -25,5 +25,5 @@
 cmp dl, 6
 ja L
-lea rcx, [D]
+lea rcx, [S:"7.Y"]
 movzx edx, dl
 movsxd rdx, dword ptr [rcx + rdx*4]
@@ -126,5 +126,5 @@
 cmp dl, 6
 ja L
-lea rcx, [D]
+lea rcx, [S:"O.Y"]
 movzx edx, dl
 movsxd rdx, dword ptr [rcx + rdx*4]
```

### изменена: 0x3c6f000 (1027 байт) | строки: "CEntityIOOutput"; "CBaseFilter"; "CHandle"
было: 0x3c6c540 (1027 байт)
- строки: −"lZY"
- инструкций: 172 → 172
```diff
@@ -2,5 +2,5 @@
 ja L
 push rbp
-lea rdx, [S:"lZY"]
+lea rdx, [D]
 mov edi, edi
 mov rbp, rsp
```

### изменена: 0x3c70320 (653 байт) | строки: "%g %g %g"; "(null)"; "%g %g %g %g"; "%lld"; "%llu"; "%d %d %d %d"; "false"; "true"
было: 0x3c6d860 (653 байт)
- строки: −"AnY"
- инструкций: 159 → 159
```diff
@@ -7,5 +7,5 @@
 cmp al, 0x4f
 ja L
-lea rcx, [S:"AnY"]
+lea rcx, [D]
 movzx edx, al
 movsxd rdx, dword ptr [rcx + rdx*4]
```

### изменена: 0x3c8c550 (478 байт) | строки: "..["
было: 0x3c89a90 (478 байт)
- строки: +"..["
- инструкций: 116 → 116
```diff
@@ -8,5 +8,5 @@
 cmp dil, 0x4f
 ja L
-lea rdx, [D]
+lea rdx, [S:"..["]
 movzx eax, dil
 movsxd rax, dword ptr [rdx + rax*4]
```

### изменена: 0x3cc1ed0 (2479 байт) CBaseLightProbeVolume::vfunc#2 | строки: "box_mins"; "box_maxs"; "moveable"; "handshake"; "@o^"; "indoor_outdoor_level"; "StartDisabled"; "is_selected_in_hammer"
было: 0x3cbf410 (2479 байт)
- строки: +"@o^" +"nn^" −"rm^" −"{m^" −"mm^" −"Xm^" −".m^"
- инструкций: 618 → 618
```diff
@@ -71,5 +71,5 @@
 cmp dl, 6
 ja L
-lea rcx, [D]
+lea rcx, [S:"@o^"]
 movzx edx, dl
 movsxd rdx, dword ptr [rcx + rdx*4]
@@ -231,5 +231,5 @@
 cmp dl, 6
 ja L
-lea rcx, [S:"rm^"]
+lea rcx, [D]
 movzx edx, dl
 movsxd rdx, dword ptr [rcx + rdx*4]
@@ -259,5 +259,5 @@
 cmp dl, 6
 ja L
-lea rcx, [S:"{m^"]
+lea rcx, [D]
 movzx edx, dl
 movsxd rdx, dword ptr [rcx + rdx*4]
@@ -287,5 +287,5 @@
 cmp dl, 6
 ja L
-lea rcx, [S:"mm^"]
+lea rcx, [D]
 movzx edx, dl
 movsxd rdx, dword ptr [rcx + rdx*4]
@@ -315,5 +315,5 @@
 cmp dl, 6
 ja L
-lea rcx, [S:"Xm^"]
+lea rcx, [D]
 movzx edx, dl
 movsxd rdx, dword ptr [rcx + rdx*4]
@@ -344,5 +344,5 @@
 cmp dl, 6
 ja L
-lea rcx, [S:".m^"]
+lea rcx, [S:"nn^"]
 movzx edx, dl
 movsxd rdx, dword ptr [rcx + rdx*4]
```

### изменена: 0x3d24ae0 (1712 байт) CEntityOutputTemplate<SndOpEventGuid_t>::vfunc#2 | строки: "m_Value"; "Stack depth limit hit (%d)"; "qQd"; "public.aabb_min"; "public.aabb_max"
было: 0x3d22020 (1712 байт)
- строки: +"qQd" −"pPd" −"1Pd"
- инструкций: 409 → 409
```diff
@@ -65,5 +65,5 @@
 cmp al, 6
 ja L
-lea rdx, [S:"pPd"]
+lea rdx, [D]
 movzx eax, al
 movsxd rax, dword ptr [rdx + rax*4]
@@ -90,5 +90,5 @@
 cmp al, 6
 ja L
-lea rdx, [S:"1Pd"]
+lea rdx, [S:"qQd"]
 movzx eax, al
 movsxd rax, dword ptr [rdx + rax*4]
```

### изменена: 0x3d32120 (637 байт) | строки: "CInfoFan"; "CHandle"; "VectorWS"
было: 0x3d2f660 (637 байт)
- строки: −"\\$e"
- инструкций: 147 → 147
```diff
@@ -7,5 +7,5 @@
 cmp edi, 6
 ja L
-lea rdx, [S:"\\$e"]
+lea rdx, [D]
 mov edi, edi
 mov rbx, rsi
```

### изменена: 0x3d325a0 (547 байт) | строки: "x(e"; "CHandle"; "CBasePlayerController"; "CNetworkUtlVectorBase"; "CBasePlayerPawn"
было: 0x3d2fae0 (547 байт)
- строки: +"x(e" −"8'e"
- инструкций: 158 → 158
```diff
@@ -2,5 +2,5 @@
 ja L
 push rbp
-lea rdx, [S:"8'e"]
+lea rdx, [S:"x(e"]
 mov edi, edi
 mov rbp, rsp
```

### изменена: 0x3d53840 (117 байт) | строки: "y!g"
было: 0x3d50d80 (117 байт)
- строки: +"y!g" −"9 g"
- инструкций: 39 → 39
```diff
@@ -2,5 +2,5 @@
 cmp edx, 6
 ja L
-lea rcx, [S:"9 g"]
+lea rcx, [S:"y!g"]
 push rbp
 mov rdi, rsi
```

### изменена: 0x3d538c0 (561 байт) | строки: "Unsupported KV3 basic type '%s' (%d)!"; "Pointers cannot be used as numeric values"
было: 0x3d50e00 (561 байт)
- строки: −"c g"
- инструкций: 151 → 151
```diff
@@ -11,5 +11,5 @@
 cmp r8b, 6
 ja L
-lea rdx, [S:"c g"]
+lea rdx, [D]
 movzx eax, r8b
 movsxd rax, dword ptr [rdx + rax*4]
```

### изменена: 0x3d53bc0 (227 байт) | строки: "IPhysicsJoint"
было: 0x3d51100 (227 байт)
- строки: −"X#g"
- инструкций: 73 → 73
```diff
@@ -1,5 +1,5 @@
 cmp edi, 6
 ja L
-lea rcx, [S:"X#g"]
+lea rcx, [D]
 mov edi, edi
 push rbp
```

### изменена: 0x3d546e0 (339 байт) | строки: "D/g"; "VPhysicsCollisionAttribute_t"; "SolidType_t"; "SurroundingBoundsType_t"
было: 0x3d51c20 (339 байт)
- строки: +"D/g"
- инструкций: 99 → 99
```diff
@@ -2,5 +2,5 @@
 ja L
 push rbp
-lea rdx, [D]
+lea rdx, [S:"D/g"]
 mov edi, edi
 mov rbp, rsp
```

### изменена: 0x3d54900 (499 байт) | строки: "P1g"; "GameTime_t"; "BeamType_t"; "CBaseEntity"; "CHandle"; "AttachmentHandle_t"; "VectorWS"
было: 0x3d51e40 (499 байт)
- строки: +"P1g"
- инструкций: 135 → 135
```diff
@@ -2,5 +2,5 @@
 ja L
 push rbp
-lea rdx, [D]
+lea rdx, [S:"P1g"]
 mov edi, edi
 mov rbp, rsp
```

### изменена: 0x3d54cf0 (285 байт) | строки: "VectorWS"
было: 0x3d52230 (285 байт)
- строки: −"L4g"
- инструкций: 81 → 81
```diff
@@ -5,5 +5,5 @@
 push rbx
 ja L
-lea rdx, [S:"L4g"]
+lea rdx, [D]
 mov edi, edi
 mov rbx, rsi
```

### изменена: 0x3d54f50 (893 байт) | строки: "InfoForResourceTypeIParticleSystemDefinition"; "CWeakHandle"; "CResourceNameTyped"; "ParticleAttachment_t"; "PrecipitationFilter_t"
было: 0x3d52490 (893 байт)
- строки: −"@6g"
- инструкций: 188 → 188
```diff
@@ -9,5 +9,5 @@
 cmp edi, 6
 ja F
-lea rdx, [S:"@6g"]
+lea rdx, [D]
 mov edi, edi
 mov rbx, rsi
```

### изменена: 0x3d63ec0 (785 байт) | строки: "Z&h"; "Unsupported KV3 basic type '%s' (%d)!"; "Pointers cannot be used as numeric values"
было: 0x3d61400 (785 байт)
- строки: +"Z&h"
- инструкций: 219 → 219
```diff
@@ -20,5 +20,5 @@
 cmp bl, 6
 ja L
-lea rdx, [D]
+lea rdx, [S:"Z&h"]
 movzx eax, bl
 movsxd rax, dword ptr [rdx + rax*4]
```

### изменена: 0x3d86f50 (243 байт) | строки: "h2j"; "VectorWS"
было: 0x3d84490 (243 байт)
- строки: +"h2j" −"(1j"
- инструкций: 67 → 67
```diff
@@ -1,5 +1,5 @@
 cmp edi, 6
 ja L
-lea rdx, [S:"(1j"]
+lea rdx, [S:"h2j"]
 mov edi, edi
 push rbp
```

### изменена: 0x3d87050 (227 байт) | строки: "T3j"; "VectorWS"
было: 0x3d84590 (227 байт)
- строки: +"T3j"
- инструкций: 74 → 74
```diff
@@ -1,5 +1,5 @@
 cmp edi, 6
 ja L
-lea rcx, [D]
+lea rcx, [S:"T3j"]
 mov edi, edi
 push rbp
```

### изменена: 0x3d87140 (339 байт) | строки: "(4j"; "BASEPTR"; "GameTick_t"
было: 0x3d84680 (339 байт)
- строки: +"(4j"
- инструкций: 90 → 90
```diff
@@ -1,5 +1,5 @@
 cmp edi, 6
 ja L
-lea rdx, [D]
+lea rdx, [S:"(4j"]
 mov edi, edi
 push rbp
```

### изменена: 0x3d87ab0 (243 байт) | строки: "|=j"; "VectorWS"
было: 0x3d84ff0 (243 байт)
- строки: +"|=j" −"<<j"
- инструкций: 76 → 76
```diff
@@ -2,5 +2,5 @@
 ja L
 push rbp
-lea rdx, [S:"<<j"]
+lea rdx, [S:"|=j"]
 mov edi, edi
 mov rbp, rsp
```

### изменена: 0x3d87ec0 (371 байт) | строки: "\\Aj"; "GameTime_t"; "CBaseEntity"; "CHandle"
было: 0x3d85400 (371 байт)
- строки: +"\\Aj"
- инструкций: 112 → 112
```diff
@@ -2,5 +2,5 @@
 ja L
 push rbp
-lea rdx, [D]
+lea rdx, [S:"\\Aj"]
 mov edi, edi
 mov rbp, rsp
```

### изменена: 0x3d884c0 (183 байт)
было: 0x3d85a00 (183 байт)
- строки: −"cFj"
- инструкций: 55 → 55
```diff
@@ -2,5 +2,5 @@
 ja L
 push rbp
-lea rdx, [S:"cFj"]
+lea rdx, [D]
 mov edi, edi
 mov rbp, rsp
```

### изменена: 0x3d885f0 (98 байт) | строки: "bHj"
было: 0x3d85b30 (98 байт)
- строки: +"bHj" −"\"Gj"
- инструкций: 36 → 36
```diff
@@ -2,5 +2,5 @@
 cmp edx, 6
 ja L
-lea rcx, [S:"\"Gj"]
+lea rcx, [S:"bHj"]
 push rbp
 mov rdi, rsi
```

### изменена: 0x3d88660 (98 байт)
было: 0x3d85ba0 (98 байт)
- строки: −"vGj"
- инструкций: 36 → 36
```diff
@@ -2,5 +2,5 @@
 cmp edx, 6
 ja L
-lea rcx, [S:"vGj"]
+lea rcx, [D]
 push rbp
 mov rdi, rsi
```

### изменена: 0x3d88840 (117 байт) | строки: "qJj"
было: 0x3d85d80 (117 байт)
- строки: +"qJj" −"1Ij"
- инструкций: 39 → 39
```diff
@@ -2,5 +2,5 @@
 cmp edx, 6
 ja L
-lea rcx, [S:"1Ij"]
+lea rcx, [S:"qJj"]
 push rbp
 mov rdi, rsi
```

### изменена: 0x3d88a90 (136 байт)
было: 0x3d85fd0 (136 байт)
- строки: −"xKj"
- инструкций: 43 → 43
```diff
@@ -2,5 +2,5 @@
 cmp edx, 6
 ja L
-lea rcx, [S:"xKj"]
+lea rcx, [D]
 push rbp
 mov rax, rsi
```

### изменена: 0x3d89af0 (206 байт) | строки: "?]j"
было: 0x3d87030 (206 байт)
- строки: +"?]j"
- инструкций: 62 → 62
```diff
@@ -2,5 +2,5 @@
 ja L
 push rbp
-lea rdx, [D]
+lea rdx, [S:"?]j"]
 mov edi, edi
 mov rbp, rsp
```

### изменена: 0x3d89f00 (222 байт) | строки: "'aj"
было: 0x3d87440 (222 байт)
- строки: +"'aj"
- инструкций: 64 → 64
```diff
@@ -2,5 +2,5 @@
 ja L
 push rbp
-lea rdx, [D]
+lea rdx, [S:"'aj"]
 mov edi, edi
 mov rbp, rsp
```

### изменена: 0x3d8a0e0 (435 байт) | строки: "Xbj"; "CTransform"; "CNetworkUtlVectorBase"
было: 0x3d87620 (435 байт)
- строки: +"Xbj"
- инструкций: 118 → 118
```diff
@@ -1,5 +1,5 @@
 cmp edi, 6
 ja L
-lea rdx, [D]
+lea rdx, [S:"Xbj"]
 mov edi, edi
 push rbp
```

### изменена: 0x3d8a350 (302 байт) | строки: "sej"
было: 0x3d87890 (302 байт)
- строки: +"sej" −"3dj"
- инструкций: 71 → 71
```diff
@@ -2,5 +2,5 @@
 ja L
 push rbp
-lea rdx, [S:"3dj"]
+lea rdx, [S:"sej"]
 mov edi, edi
 mov rbp, rsp
```

### изменена: 0x3d8a820 (811 байт) | строки: "Xij"
было: 0x3d87d60 (811 байт)
- строки: +"Xij"
- инструкций: 232 → 232
```diff
@@ -9,5 +9,5 @@
 movsxd r13, edx
 push r12
-lea rdx, [D]
+lea rdx, [S:"Xij"]
 mov r12d, ecx
 push rbx
```

### изменена: 0x3d8ab60 (907 байт)
было: 0x3d880a0 (907 байт)
- строки: −"Dkj"
- инструкций: 252 → 252
```diff
@@ -9,5 +9,5 @@
 movsxd r13, edx
 push r12
-lea rdx, [S:"Dkj"]
+lea rdx, [D]
 mov r12d, ecx
 push rbx
```

### изменена: 0x3d8b9d0 (435 байт) | строки: "CPlayerSlot"; "CUtlVector"
было: 0x3d88f10 (435 байт)
- строки: −"`yj"
- инструкций: 115 → 115
```diff
@@ -1,5 +1,5 @@
 cmp edi, 6
 ja L
-lea rdx, [S:"`yj"]
+lea rdx, [D]
 mov edi, edi
 push rbp
```

### изменена: 0x3d97330 (659 байт) | строки: "CTakeDamageInfo"; "DestructiblePartDamageRequest_t"; "CUtlLeanVector"; "VectorWS"; "TakeDamageFlags_t"; "HitGroup_t"
было: 0x3d94870 (659 байт)
- строки: −"t1k"
- инструкций: 151 → 151
```diff
@@ -1,5 +1,5 @@
 cmp edi, 6
 ja L
-lea rdx, [S:"t1k"]
+lea rdx, [D]
 mov edi, edi
 push rbp
```

### изменена: 0x3d975d0 (659 байт) | строки: "85k"; "CTakeDamageInfo"; "CTakeDamageResult"
было: 0x3d94b10 (659 байт)
- строки: +"85k"
- инструкций: 126 → 126
```diff
@@ -2,5 +2,5 @@
 ja L
 push rbp
-lea rdx, [D]
+lea rdx, [S:"85k"]
 mov edi, edi
 mov rbp, rsp
```

### изменена: 0x3d97c00 (563 байт) | строки: "H;k"; "CUtlVector"; "VectorWS"; "GameTime_t"
было: 0x3d95140 (563 байт)
- строки: +"H;k"
- инструкций: 157 → 157
```diff
@@ -2,5 +2,5 @@
 ja L
 push rbp
-lea rdx, [D]
+lea rdx, [S:"H;k"]
 mov edi, edi
 mov rbp, rsp
```

### изменена: 0x3d9ab50 (4083 байт) вызывается из: CTakeDamageInfo::vfunc#2 | строки: "m_vecDamageForce"; "m_bitsDamageType"; "+nk"; "m_vecDamagePosition"; "m_vecReportedPosition"; "m_vecDamageDirection"; "m_hInflictor"; "m_hAttacker"
было: 0x3d98090 (4083 байт)
- строки: +"+nk" +"6xk"
- инструкций: 886 → 886
```diff
@@ -113,5 +113,5 @@
 cmp r8b, 6
 ja L
-lea rdx, [D]
+lea rdx, [S:"+nk"]
 movzx eax, r8b
 movsxd rax, dword ptr [rdx + rax*4]
@@ -362,5 +362,5 @@
 cmp r8b, 6
 ja L
-lea rdx, [D]
+lea rdx, [S:"6xk"]
 movzx eax, r8b
 movsxd rax, dword ptr [rdx + rax*4]
```

### изменена: 0x3da6800 (414 байт) | строки: "P&l"
было: 0x3da3d40 (414 байт)
- строки: +"P&l"
- инструкций: 136 → 136
```diff
@@ -8,5 +8,5 @@
 movsxd r12, edx
 push rbx
-lea rdx, [D]
+lea rdx, [S:"P&l"]
 mov rbx, rsi
 sub rsp, 0x18
```

### изменена: 0x3da7420 (542 байт) | строки: "02l"
было: 0x3da4960 (542 байт)
- строки: +"02l"
- инструкций: 159 → 159
```diff
@@ -9,5 +9,5 @@
 movsxd r12, edx
 push rbx
-lea rdx, [D]
+lea rdx, [S:"02l"]
 mov rbx, rsi
 sub rsp, 0x10
```

### изменена: 0x3dac670 (961 байт) | строки: "Bzl"; "%g %g %g"; "(null)"; "%g %g %g %g"; "unknown_variant_type"; "qzl"; "%lld"; "%llu"
было: 0x3da9bb0 (961 байт)
- строки: +"Bzl" +"qzl" −"1yl"
- инструкций: 213 → 213
```diff
@@ -7,5 +7,5 @@
 cmp al, 0x4f
 ja L
-lea rcx, [D]
+lea rcx, [S:"Bzl"]
 movzx edx, al
 movsxd rdx, dword ptr [rcx + rdx*4]
@@ -91,5 +91,5 @@
 cmp al, 0x47
 ja L
-lea rdx, [S:"1yl"]
+lea rdx, [S:"qzl"]
 movzx eax, al
 movsxd rax, dword ptr [rdx + rax*4]
```

### изменена: 0x3dba2b0 (851 байт) | строки: "|Um"; "%llu"
было: 0x3db77f0 (851 байт)
- строки: +"|Um" −"<Tm"
- инструкций: 190 → 190
```diff
@@ -21,5 +21,5 @@
 mov rbx, rax
 je L
-lea r13, [S:"<Tm"]
+lea r13, [S:"|Um"]
 nop dword ptr [rax + rax]
 mov qword ptr [rbp - 0xc0], 0
```

### изменена: 0x3dbaac0 (819 байт) | строки: "$[m"; "DecalFlags_t"; "GameTime_t"
было: 0x3db8000 (819 байт)
- строки: +"$[m"
- инструкций: 143 → 143
```diff
@@ -2,5 +2,5 @@
 ja L
 push rbp
-lea rdx, [D]
+lea rdx, [S:"$[m"]
 mov edi, edi
 mov rbp, rsp
```

### изменена: 0x3df96a0 (350 байт) | строки: "_.q"
было: 0x3df6be0 (350 байт)
- строки: +"_.q"
- инструкций: 92 → 92
```diff
@@ -2,5 +2,5 @@
 ja L
 push rbp
-lea rdx, [D]
+lea rdx, [S:"_.q"]
 mov edi, edi
 mov rbp, rsp
```

### изменена: 0x3df9880 (407 байт) вызывается из: CVScriptGameSystem::vfunc#85
было: 0x3df6dc0 (407 байт)
- строки: −"D.q"
- инструкций: 104 → 104
```diff
@@ -31,5 +31,5 @@
 ja L
 movzx eax, word ptr [rax + 0x28]
-lea rdx, [S:"D.q"]
+lea rdx, [D]
 movsxd rax, dword ptr [rdx + rax*4]
 add rax, rdx
```

### изменена: 0x3dfb520 (547 байт) | строки: "CHandle"; "CEnvSoundscapeTriggerable"; "CBasePlayerPawn"; "CUtlVector"
было: 0x3df8a60 (547 байт)
- строки: −"hJq"
- инструкций: 144 → 144
```diff
@@ -2,5 +2,5 @@
 ja L
 push rbp
-lea rdx, [S:"hJq"]
+lea rdx, [D]
 mov edi, edi
 mov rbp, rsp
```

### изменена: 0x3dfdfd0 (502 байт) | строки: "4vq"
было: 0x3dfb510 (502 байт)
- строки: +"4vq"
- инструкций: 139 → 139
```diff
@@ -21,5 +21,5 @@
 cmp al, 0x24
 ja L
-lea rcx, [D]
+lea rcx, [S:"4vq"]
 movzx eax, al
 movsxd rax, dword ptr [rcx + rax*4]
```

### изменена: 0x3e1c800 (4702 байт) | строки: "classname"; "connections"; "attributes"; "X]s"
было: 0x3e19d40 (4702 байт)
- строки: −"PWs"
- инструкций: 1086 → 1086
```diff
@@ -208,5 +208,5 @@
 cmp r14b, 0x4f
 ja L
-lea rsi, [S:"PWs"]
+lea rsi, [D]
 movsxd rax, dword ptr [rsi + r14*4]
 add rax, rsi
@@ -617,5 +617,5 @@
 cmp al, 0x4f
 ja L
-lea rsi, [S:"X]s"]
+lea rsi, [D]
 movzx edx, al
 movsxd rdx, dword ptr [rsi + rdx*4]
@@ -747,5 +747,5 @@
 cmp al, 0x4f
 ja L
-lea rsi, [D]
+lea rsi, [S:"X]s"]
 movzx edx, al
 movsxd rdx, dword ptr [rsi + rdx*4]
```

### изменена: 0x3e2d7e0 (542 байт) | строки: "D\\t"
было: 0x3e2ad20 (542 байт)
- строки: +"D\\t"
- инструкций: 159 → 159
```diff
@@ -9,5 +9,5 @@
 movsxd r12, edx
 push rbx
-lea rdx, [D]
+lea rdx, [S:"D\\t"]
 mov rbx, rsi
 sub rsp, 0x10
```

### изменена: 0x3e6ea40 (187 байт) | строки: "Disposition_t"
было: 0x3e6bf80 (187 байт)
- строки: −"hYx"
- инструкций: 59 → 59
```diff
@@ -1,5 +1,5 @@
 cmp edi, 6
 ja L
-lea rdx, [S:"hYx"]
+lea rdx, [D]
 mov edi, edi
 push rbp
```

### изменена: 0x3e6ec30 (275 байт) | строки: "VectorWS"
было: 0x3e6c170 (275 байт)
- строки: −"D[x"
- инструкций: 84 → 84
```diff
@@ -1,5 +1,5 @@
 cmp edi, 6
 ja L
-lea rcx, [S:"D[x"]
+lea rcx, [D]
 mov edi, edi
 push rbp
```

### изменена: 0x3e6edf0 (243 байт) | строки: " ^x"; "VectorWS"
было: 0x3e6c330 (243 байт)
- строки: +" ^x"
- инструкций: 70 → 70
```diff
@@ -1,5 +1,5 @@
 cmp edi, 6
 ja L
-lea rdx, [D]
+lea rdx, [S:" ^x"]
 mov edi, edi
 push rbp
```

### изменена: 0x3e6f840 (451 байт) | строки: "dhx"; "CEconWearable"; "CHandle"; "CNetworkUtlVectorBase"; "RelationshipOverride_t"; "CUtlVector"; "Hull_t"; "CMovementStatsProperty"
было: 0x3e6cd80 (451 байт)
- строки: +"dhx" −"$gx"
- инструкций: 129 → 129
```diff
@@ -2,5 +2,5 @@
 ja L
 push rbp
-lea rdx, [S:"$gx"]
+lea rdx, [S:"dhx"]
 mov edi, edi
 mov rbp, rsp
```

### изменена: 0x3e70e70 (187 байт) | строки: "S~x"
было: 0x3e6e3b0 (187 байт)
- строки: +"S~x"
- инструкций: 52 → 52
```diff
@@ -3,5 +3,5 @@
 ja L
 push rbp
-lea rcx, [D]
+lea rcx, [S:"S~x"]
 mov rdi, rsi
 mov rbp, rsp
```

### изменена: 0x3e70f30 (171 байт) | строки: "HitGroup_t"
было: 0x3e6e470 (171 байт)
- строки: −"@}x"
- инструкций: 54 → 54
```diff
@@ -1,5 +1,5 @@
 cmp edi, 6
 ja L
-lea rdx, [S:"@}x"]
+lea rdx, [D]
 mov edi, edi
 push rbp
```

### изменена: 0x3eac320 (769 байт) вызывается из: CAnimGraphControllerBase::vfunc#2, CEmptyGraphController::vfunc#2, EventGrantDefinition_Emoticon_t::vfunc#2 | строки: "b.|"; "Unsupported KV3 basic type '%s' (%d)!"; "Pointers cannot be used as numeric values"
было: 0x3ea9860 (769 байт)
- строки: +"b.|" −"\"-|"
- инструкций: 220 → 220
```diff
@@ -31,5 +31,5 @@
 cmp bl, 6
 ja L
-lea rdx, [S:"\"-|"]
+lea rdx, [S:"b.|"]
 movzx eax, bl
 movsxd rax, dword ptr [rdx + rax*4]
```

### изменена: 0x3eaec90 (856 байт)
было: 0x3eabe70 (856 байт)
- строки: −"|P|"
- инструкций: 221 → 221
```diff
@@ -10,5 +10,5 @@
 movsxd r12, edx
 push rbx
-lea rdx, [S:"|P|"]
+lea rdx, [D]
 mov rbx, rsi
 sub rsp, 0x58
```

### изменена: 0x3eb0940 (904 байт) | строки: "xq|"
было: 0x3eade80 (904 байт)
- строки: +"xq|" −"8p|"
- инструкций: 237 → 237
```diff
@@ -7,5 +7,5 @@
 mov r15d, edx
 push r14
-lea rdx, [S:"8p|"]
+lea rdx, [S:"xq|"]
 push r13
 push r12
```

### изменена: 0x3ecc260 (904 байт) | строки: "(*~"
было: 0x3ec97a0 (904 байт)
- строки: +"(*~"
- инструкций: 238 → 238
```diff
@@ -7,5 +7,5 @@
 mov r15d, edx
 push r14
-lea rdx, [D]
+lea rdx, [S:"(*~"]
 push r13
 push r12
```

### изменена: 0x4906a00 (6 байт) CDOTA_Modifier_Lycan_Pack_Hunter_Marked::IsPurgable
было: 0x4903f40 (3 байт)
- числа в инструкциях: +1
- инструкций: 2 → 2
```diff
@@ -1,2 +1,2 @@
-xor eax, eax
+mov eax, 1
 ret
```

### изменена: 0x49982a0 (410 байт) CDOTA_Ability_LoneDruid_SpiritBear_SummonDruid::vfunc#364 | строки: "modifier_lone_druid_spirit_bear_summon_druid"; "lone_druid_spirit_bear"; "item_ultimate_scepter"; "scepter_gained_cooldown"
было: 0x4916f60 (101 байт)
- строки: +"lone_druid_spirit_bear" +"item_ultimate_scepter" +"scepter_gained_cooldown"
- константы из данных (числа логики): +-1
- числа в инструкциях: +-1 +-2 +9 +0x3f +0x1ff +0x70 +3 +0 (и ещё 4)
- виртуальные вызовы: +0x908 (слот 289)
- поля объектов: +0x1780 +0x1780 +0x10 +0x5d1 +0x175a
- прямых вызовов: 4 → 13
- цели вызовов: +0x6215660 "<NoAbilityName>"; "dota_empty_ability" +0x52b7440 +0x61d0aa0 +0x53138e0 "<NoAbilityName>" +0x3bbeb20 "AbilityManaCost"; "AbilityHealthCost" +0x507bb20
- инструкций: 35 → 118
```diff
@@ -6,5 +6,5 @@
 mov r12, rdi
 push rbx
-sub rsp, 0x20
+sub rsp, 0x30
 call F
 test rax, rax
@@ -18,14 +18,54 @@
 mov rsi, r14
 call F
-mov rdi, rbx
 xor r9d, r9d
+mov rcx, r14
 mov r8, r13
-mov rcx, r14
 mov rdx, r12
 mov rsi, rbx
+mov rdi, rbx
 call F
+mov ecx, dword ptr [rbx + 0x1780]
+cmp ecx, -1
+je L
+mov rsi, qword ptr [D]
+test rsi, rsi
+je L
+cmp ecx, -2
+je L
+movzx eax, word ptr [rbx + 0x1780]
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
+mov rdi, qword ptr [rax]
+test rdi, rdi
+je L
+cmp byte ptr [rdi + 0x5d1], 3
+jne L
+lea rsi, [S:"lone_druid_spirit_bear"]
+xor edx, edx
+call F
```
(ещё 64 строк диффа: so-query.py fdiff libserver.so 0x49982a0)

### изменена: 0x496c3c0 (136 байт) CDOTA_Modifier_Lycan_Pack_Hunter::vfunc#88 | строки: "mark_duration"; "mark_range"
было: 0x4968d30 (74 байт)
- строки: +"mark_range"
- виртуальные вызовы: +0x1f0 (слот 62)
- поля объектов: +0x1afc
- прямых вызовов: 3 → 6
- инструкций: 24 → 40
```diff
@@ -19,4 +19,20 @@
 movaps xmm1, xmm0
 movss dword ptr [rbx + 0x1af8], xmm1
+mov rdi, rbx
+call F
+mov rdi, rbx
+mov r12, rax
+mov rax, qword ptr [rbx]
+call qword ptr [rax + 0x1f0]
+test r12, r12
+pxor xmm1, xmm1
+je L
+xor ecx, ecx
+xor edx, edx
+mov rdi, r12
+lea rsi, [S:"mark_range"]
+call F
+movaps xmm1, xmm0
+movss dword ptr [rbx + 0x1afc], xmm1
 pop rbx
 pop r12
```

### изменена: 0x4995c80 (1119 байт) | строки: "CNetworkTransmitComponent::StateChanged(%s) @%s:%d"; "Hero_Jakiro.LiquidFrost"; "particles/units/heroes/hero_jakiro/jakiro_liquid_ice.vpcf"; "attach_hitloc"; "modifier_jakiro_liquid_ice"; "duration"; "modifier_jakiro_liquid_ice_debuff"
было: 0x4993210 (927 байт)
- строки: +"CNetworkTransmitComponent::StateChanged(%s) @%s:%d"
- числа в инструкциях: +0x40 +0x3fffffff +3
- поля объектов: +0x28 +0x30 +0x20 +0x2d8 +0x2f6
- прямых вызовов: 29 → 33
- цели вызовов: +V_UnqualifiedFileName() +0x3bbe670 +0x3c21740 +_ZN13CBufferString5PurgeEi()
- инструкций: 223 → 272
```diff
@@ -1,2 +1,51 @@
+push rbp
+mov rbp, rsp
+push r14
+push r13
+lea r13, [D]
+push r12
+mov r12, rsi
+push rbx
+mov rbx, rdi
+sub rsp, 0x110
+mov rdi, qword ptr [rsi + 0x28]
+mov r14d, dword ptr [rsi + 0x30]
+test rdi, rdi
+cmove rdi, r13
+call F
+mov rdx, qword ptr [r12 + 0x20]
+lea r12, [rbp - 0x130]
+mov r8d, r14d
+lea rsi, [S:"CNetworkTransmitComponent::StateChanged(%s) @%s:%d"]
+mov rcx, rax
+mov rdi, r12
+test rdx, rdx
+cmove rdx, r13
+xor eax, eax
+call F
+test byte ptr [rbp - 0x129], 0x40
+lea rsi, [rbp - 0x128]
+jne L
+test dword ptr [rbp - 0x12c], 0x3fffffff
+mov rsi, r13
+je L
+mov rsi, qword ptr [rbp - 0x128]
+mov rdi, rbx
+call F
+xor esi, esi
+mov rdi, r12
+call F
+lock or dword ptr [rbx + 0x2d8], 3
+xor eax, eax
+mov word ptr [rbx + 0x2f6], ax
+add rsp, 0x110
+pop rbx
+pop r12
+pop r13
+pop r14
+pop rbp
```
(ещё 19 строк диффа: so-query.py fdiff libserver.so 0x4995c80)

### изменена: 0x499cc80 (546 байт) вызывается из: CDOTA_Modifier_LoneDruid_SummonDruid_DeathDeferral::vfunc#97 | строки: "modifier_lone_druid_summon_druid_downed"; "item_ultimate_scepter"; "modifier_skeleton_king_reincarnation_scepter_active"; "lone_druid_spirit_bear"
было: 0x4999eb0 (487 байт)
- строки: +"item_ultimate_scepter"
- числа в инструкциях: +1 +0xffffffff
- виртуальные вызовы: +0x940 (слот 296)
- прямых вызовов: 13 → 16
- цели вызовов: +0x61d0aa0 +0x53138e0 "<NoAbilityName>"
- инструкций: 117 → 132
```diff
@@ -73,4 +73,19 @@
 mov qword ptr [rbx], rax
 jmp L
+mov rdi, r12
+call F
+or r8d, 0xffffffff
+xor ecx, ecx
+mov edx, 1
+lea rsi, [S:"item_ultimate_scepter"]
+mov rdi, rax
+call F
+test rax, rax
+mov rdi, rax
+je L
+mov rax, qword ptr [rax]
+call qword ptr [rax + 0x940]
+test al, al
+je L
 mov rax, qword ptr [r12]
 mov rdi, r12
```

### изменена: 0x49bbbd0 (1760 байт) вызывается из: CDOTA_Modifier_Spectre_Arcana::vfunc#128 | строки: "None"
было: 0x49b8da0 (1582 байт)
- числа в инструкциях: +0 +0 +0 +1
- виртуальные вызовы: −0xf0 (слот 30)
- поля объектов: +0xf0 +0x318 +0x48 +0x18 +0x315 +0x30 +0x538 +0x538 +0x530
- прямых вызовов: 33 → 35
- цели вызовов: +CDOTA_NPCSpawnerGoodTop::vfunc#30 +0x4995c80 "CNetworkTransmitComponent::StateChanged("; "Hero_Jakiro.LiquidFrost" +0x3c43760 " ignored"; "%u,"
- инструкций: 334 → 371
```diff
@@ -38,9 +38,9 @@
 je L
 lea rdi, [rbp - 0x60]
-xor r9d, r9d
-pxor xmm0, xmm0
-mov esi, 1
-movaps xmmword ptr [rbp - 0x50], xmm0
-mov word ptr [rbp - 0x34], r9w
+xor r10d, r10d
+pxor xmm0, xmm0
+mov esi, 1
+movaps xmmword ptr [rbp - 0x50], xmm0
+mov word ptr [rbp - 0x34], r10w
 mov qword ptr [rbp - 0x70], 1
 mov qword ptr [rbp - 0x68], 0
@@ -76,9 +76,9 @@
 je L
 lea rdi, [rbp - 0x60]
-xor r8d, r8d
-pxor xmm0, xmm0
-mov esi, 1
-movaps xmmword ptr [rbp - 0x50], xmm0
-mov word ptr [rbp - 0x34], r8w
+xor r9d, r9d
+pxor xmm0, xmm0
+mov esi, 1
+movaps xmmword ptr [rbp - 0x50], xmm0
+mov word ptr [rbp - 0x34], r9w
 mov qword ptr [rbp - 0x70], 1
 mov qword ptr [rbp - 0x68], 0
@@ -130,11 +130,11 @@
 cmp r15b, byte ptr [rbx + 0x2398]
 je L
-xor edi, edi
-mov esi, 1
-pxor xmm0, xmm0
-mov qword ptr [rbp - 0x70], 1
-mov word ptr [rbp - 0x34], di
-lea rdi, [rbp - 0x60]
-movaps xmmword ptr [rbp - 0x50], xmm0
+lea rdi, [rbp - 0x60]
+xor r8d, r8d
+pxor xmm0, xmm0
+mov esi, 1
+movaps xmmword ptr [rbp - 0x50], xmm0
+mov word ptr [rbp - 0x34], r8w
+mov qword ptr [rbp - 0x70], 1
```
(ещё 98 строк диффа: so-query.py fdiff libserver.so 0x49bbbd0)

### изменена: 0x49be180 (1326 байт) CDOTA_Modifier_Jakiro_IcePath_Thinker::OnIntervalThink | строки: "modifier_jakiro_ice_path_stun"; "duration"
было: 0x49c6e80 (1395 байт)
- числа в инструкциях: −1 −1
- поля объектов: −0x1b10 −0x1b10 −0x1b10 −0x1b18 −0x1b20
- цели вызовов: +0x49be120 −0x3bb3ae0
- инструкций: 305 → 292
```diff
@@ -212,5 +212,5 @@
 je L
 add rax, 1
-cmp rax, rdx
+cmp rdx, rax
 jne L
 mov rdi, r15
@@ -229,15 +229,9 @@
 mov esi, dword ptr [rbp - 0x70]
 jmp L
-movsxd rax, dword ptr [rbx + 0x1b10]
-add r14, qword ptr [rbp - 0x68]
-cmp eax, dword ptr [rbx + 0x1b20]
-mov edx, eax
-je L
-add edx, 1
-mov rdi, rbx
-mov dword ptr [rbx + 0x1b10], edx
-mov rdx, qword ptr [rbx + 0x1b18]
-mov ecx, dword ptr [r14]
-mov dword ptr [rdx + rax*4], ecx
+mov rsi, qword ptr [rbp - 0x68]
+lea rdi, [rbx + 0x1b10]
+add rsi, r14
+call F
+mov rdi, rbx
 call F
 test rax, rax
@@ -297,9 +291,2 @@
 call F
 jmp L
-lea rdi, [rbx + 0x1b18]
-mov esi, 1
-mov dword ptr [rbp - 0xb8], eax
-call F
-mov edx, dword ptr [rbx + 0x1b10]
-movsxd rax, dword ptr [rbp - 0xb8]
-jmp L
```

### изменена: 0x49cc570 (540 байт) CDOTA_Ability_Shadow_Demon_Disruption::OnSpellStart | строки: "modifier_shadow_demon_disruption"; "duration"; "Hero_ShadowDemon.Disruption.Cast"; "<NoAbilityName>"; "abilityname"; "disruption_target"
было: 0x49c96c0 (651 байт)
- числа в инструкциях: −2 −2 −0x7fff
- виртуальные вызовы: −0x20 (слот 4) −0x20 (слот 4)
- прямых вызовов: 22 → 19
- цели вызовов: +0x45156b0 −memset() −0x45155b0
- инструкций: 165 → 133
```diff
@@ -36,23 +36,23 @@
 test al, al
 jne L
-lea r13, [rbp - 0x80]
+lea r14, [rbp - 0x80]
 mov rdi, r12
 call F
-lea r14, [S:"modifier_shadow_demon_disruption"]
+lea r13, [S:"modifier_shadow_demon_disruption"]
 xor ecx, ecx
 xor edx, edx
-mov rsi, r14
-mov rdi, r13
+mov rsi, r13
+mov rdi, r14
 movss dword ptr [rbp - 0xa4], xmm0
 call F
 movss xmm0, dword ptr [rbp - 0xa4]
 lea rsi, [S:"duration"]
-mov rdi, r13
+mov rdi, r14
 call F
 mov rdi, r12
 call F
 xor r9d, r9d
-mov r8, r13
-mov rcx, r14
+mov r8, r14
+mov rcx, r13
 mov rsi, rax
 mov rdx, r12
@@ -67,7 +67,7 @@
 call F
 mov rdi, r12
-movzx r14d, byte ptr [rbx + 0x624]
+movzx r13d, byte ptr [rbx + 0x624]
 call F
-cmp byte ptr [rax + 0x624], r14b
+cmp byte ptr [rax + 0x624], r13b
 je L
 mov rax, qword ptr [rbx + 0x10]
@@ -76,6 +76,6 @@
 mov eax, dword ptr [rax + 0x10]
 mov dword ptr [r12 + 0x85c], eax
-lea r14, [rbp - 0x60]
-mov rdi, r14
+lea r13, [rbp - 0x60]
```
(ещё 72 строк диффа: so-query.py fdiff libserver.so 0x49cc570)

### изменена: 0x49d3270 (1212 байт) CDOTA_Modifier_LoneDruid_SummonDruid_Downed::OnCreated | строки: "summon_lockout"; "attacker"; "item_rapier"; "item_gem"; "<NoAbilityName>"; "particles/units/heroes/hero_lone_druid/summon_druid_death.vpcf"; "modifier_lone_druid_spirit_bear_summon_druid_glow"
было: 0x49d0430 (1020 байт)
- строки: +"item_rapier" +"item_gem" +"item_gem" +"<NoAbilityName>"
- числа в инструкциях: +0 +1 +9
- виртуальные вызовы: +0xab8 (слот 343)
- поля объектов: +0x1930 +0x840
- прямых вызовов: 35 → 41
- цели вызовов: +0x61d0aa0 +0x5313140
- инструкций: 219 → 267
```diff
@@ -6,25 +6,25 @@
 mov r13, rsi
 push r12
+mov r12, rdi
 push rbx
-mov rbx, rdi
-sub rsp, 0xf8
-call F
-mov rdi, rbx
-mov r12, rax
-mov rax, qword ptr [rbx]
+sub rsp, 0x108
+call F
+mov rdi, r12
+mov rbx, rax
+mov rax, qword ptr [r12]
 call qword ptr [rax + 0x1f0]
-test r12, r12
+test rbx, rbx
 pxor xmm1, xmm1
 je L
 xor ecx, ecx
 xor edx, edx
-mov rdi, r12
+mov rdi, rbx
 lea rsi, [S:"summon_lockout"]
 call F
 movaps xmm1, xmm0
-xor edx, edx
-movss dword ptr [rbx + 0x1afc], xmm1
+movss dword ptr [r12 + 0x1afc], xmm1
+lea rsi, [S:"attacker"]
+xor edx, edx
 mov rdi, r13
-lea rsi, [S:"attacker"]
 call F
 test rax, rax
@@ -34,23 +34,23 @@
 je L
 mov eax, dword ptr [rax + 0x10]
-mov dword ptr [rbx + 0x1af8], eax
-mov rdi, rbx
-call F
-test rax, rax
-mov r12, rax
-je L
-mov rdi, rax
```
(ещё 181 строк диффа: so-query.py fdiff libserver.so 0x49d3270)

### изменена: 0x49d7240 (555 байт) вызывается из: CDOTA_Modifier_Lycan_Pack_Hunter::vfunc#97 | строки: "modifier_lycan_pack_hunter_marked"
было: 0x49d4340 (465 байт)
- строки: +"modifier_lycan_pack_hunter_marked" +"modifier_lycan_pack_hunter_marked"
- поля объектов: +0x1afc
- прямых вызовов: 12 → 15
- цели вызовов: +0x3c772a0
- инструкций: 129 → 148
```diff
@@ -90,8 +90,28 @@
 cmp byte ptr [rax + 0x7a6], 0
 je L
-lea r14, [S:"modifier_lycan_pack_hunter_marked"]
+mov rdi, r12
+call F
+test rax, rax
+je L
+mov rdi, rax
+call F
+mov rdi, r13
+mov r14, rax
+call F
+movss xmm1, dword ptr [rax + 4]
+movss xmm0, dword ptr [rax]
+subss xmm1, dword ptr [r14 + 4]
+subss xmm0, dword ptr [r14]
+mulss xmm1, xmm1
+mulss xmm0, xmm0
+addss xmm0, xmm1
+movd eax, xmm0
+movd xmm0, eax
+sqrtss xmm0, xmm0
+comiss xmm0, dword ptr [r12 + 0x1afc]
+ja L
+lea rsi, [S:"modifier_lycan_pack_hunter_marked"]
 xor edx, edx
 mov rdi, r15
-mov rsi, r14
 call F
 test rax, rax
@@ -102,27 +122,26 @@
 call F
 jmp L
-lea rax, [rbp - 0x50]
+lea r14, [rbp - 0x50]
 xor ecx, ecx
 xor edx, edx
-mov rsi, r14
-mov rdi, rax
-mov qword ptr [rbp - 0x58], rax
+lea rsi, [S:"modifier_lycan_pack_hunter_marked"]
+mov rdi, r14
 call F
 mov rdi, r12
 call F
 mov rdi, r12
```
(ещё 22 строк диффа: so-query.py fdiff libserver.so 0x49d7240)

### изменена: 0x49f41b0 (444 байт) | строки: "CDOTA_Ability_Lycan_Howl"
было: 0x49f1270 (444 байт)
- числа в инструкциях: +0x3141593e −0x79acbbfa
- прямых вызовов: 10 → 11
- инструкций: 97 → 100
```diff
@@ -56,8 +56,12 @@
 test eax, eax
 je L
-lea rdi, [D]
-mov esi, 0x79acbbfa
+lea r14, [S:"CDOTA_Ability_Lycan_Howl"]
+mov esi, 0x3141593e
+mov rdi, r14
 call F
-lea rdi, [D]
+lea rdi, [r14 + 8]
+mov esi, eax
+call F
+lea rdi, [r14 + 0x10]
 mov esi, eax
 call F
@@ -74,5 +78,5 @@
 shr edx, 0xf
 xor eax, edx
-lea rdx, [S:"CDOTA_Ability_Lycan_Howl"]
+mov rdx, r14
 mov dword ptr [rbp - 0x24], eax
 call F
@@ -84,5 +88,4 @@
 call F
 jmp L
-nop dword ptr [rax]
 lea rdi, [D]
 mov esi, 1
```

### изменена: 0x4a5d920 (828 байт) CDOTA_Ability_Chaos_Knight_Armageddon::OnSpellStart | строки: "max_charge_time"; "modifier_chaos_knight_armageddon_windup"; "duration"; "direction_x"; "direction_y"; "target_x"; "target_y"; "target_z"
было: 0x4a5a2f0 (812 байт)
- прямых вызовов: 17 → 18
- цели вызовов: +0x59a8490 "CNetworkTransmitComponent::StateChanged("
- инструкций: 185 → 188
```diff
@@ -11,8 +11,11 @@
 test rax, rax
 je L
+xor esi, esi
+mov rdi, rbx
+mov r12, rax
+call F
 movss xmm0, dword ptr [K:-1]
 xor edx, edx
 mov rdi, rbx
-mov r12, rax
 lea rsi, [S:"max_charge_time"]
 call F
@@ -130,5 +133,5 @@
 pop rbp
 ret
-nop
+nop dword ptr [rax]
 comiss xmm1, dword ptr [K:1e+17]
 ja L
```

### изменена: 0x4ac82e0 (2131 байт) CDOTA_Modifier_ChaosKnight_Phantasm::OnDestroy | строки: "modifier_chaos_knight_phantasm_illusion"; "illusion_duration"; "outgoing_damage"; "incoming_damage"; "images_count"; "chance_for_extra_illusion"; "illusion_effectiveness"; "modifier_illusion"
было: 0x4ac5380 (2026 байт)
- строки: +"chaos_knight_armageddon"
- числа в инструкциях: +1
- виртуальные вызовы: +0x920 (слот 292)
- прямых вызовов: 77 → 83
- цели вызовов: +0x59a8490 "CNetworkTransmitComponent::StateChanged("
- инструкций: 481 → 505
```diff
@@ -376,5 +376,12 @@
 cmp r14, r13
 jne L
+mov rdi, rbx
 mov r14, qword ptr [rbp - 0xf8]
+call F
+mov rdi, rbx
+mov r12, rax
+call F
+cmp r12, rax
+je L
 mov rdi, rbx
 call F
@@ -440,8 +447,8 @@
 pop rbp
 ret
-nop dword ptr [rax + rax]
+nop dword ptr [rax]
 mov dword ptr [rbp - 0xe0], 0
 jmp L
-nop
+nop word ptr [rax + rax]
 mov rdi, rbx
 call F
@@ -480,2 +487,19 @@
 jne L
 jmp L
+nop word ptr [rax + rax]
+mov rdi, rbx
+call F
+lea rsi, [S:"chaos_knight_armageddon"]
+xor edx, edx
+mov rdi, rax
+call F
+test rax, rax
+mov r12, rax
+je L
+mov rax, qword ptr [rax]
+mov rdi, r12
+call qword ptr [rax + 0x920]
+mov esi, 1
+mov rdi, r12
+call F
+jmp L
```

### изменена: 0x4ae33f0 (3659 байт) CDOTA_Modifier_Disruptor_Thunder_Strike::OnIntervalThink | строки: "particles/units/heroes/hero_disruptor/disruptor_thunder_strike_bolt.vpcf"; "attach_hitloc"; "slow_duration"; "modifier_disruptor_thunderstrike_slow"; "duration"; "particles/units/heroes/hero_disruptor/disruptor_thunder_strike_aoe.vpcf"; "Hero_Disruptor.ThunderStrike.Target"; "modifier_disruptor_kinetic_field"
было: 0x4ae0410 (3571 байт)
- числа в инструкциях: +0 +3 +1
- поля объектов: +0x5d1 +0xd3c +0x175a +0xd58
- цели вызовов: −0x44c2480
- инструкций: 764 → 786
```diff
@@ -401,16 +401,5 @@
 cmp dword ptr [rbp - 0x164], 1
 movzx r14d, byte ptr [rbp - 0x166]
-jle L
-mov rdi, r12
-call F
-mov rdi, rax
-call F
-xor r9d, r9d
-mov ecx, 1
-xor esi, esi
-movzx r8d, byte ptr [rbp - 0x165]
-mov rdi, rax
-mov edx, 0x227
-call F
+jg L
 mov rdi, r12
 call F
@@ -444,5 +433,5 @@
 pop rbp
 ret
-nop dword ptr [rax + rax]
+nop dword ptr [rax]
 xor r14d, r14d
 cmp byte ptr [rbx + 0x5d1], 3
@@ -662,9 +651,42 @@
 jmp L
 nop dword ptr [rax + rax]
+mov rdi, r12
+movzx ebx, byte ptr [rbp - 0x165]
+call F
+test rax, rax
+mov rdi, rax
+je L
+cmp byte ptr [rax + 0x5d1], 3
+jne L
+test byte ptr [rax + 0xd3c], 1
+jne L
+mov rax, qword ptr [rax]
+lea rdx, [T]
+mov rax, qword ptr [rax + 0xd58]
+cmp rax, rdx
+jne L
+xor edi, edi
+xor r9d, r9d
+mov r8d, ebx
+mov ecx, 1
```
(ещё 22 строк диффа: so-query.py fdiff libserver.so 0x4ae33f0)

### изменена: 0x4aef7a0 (1508 байт) CDOTA_Modifier_Chaos_Knight_Armageddon::OnIntervalThink | строки: "speed_per_second"; "max_bonus_speed"; "drain_rate_multiplier"; "modifier_chaos_knight_armageddon_charge"; "modifier_chaos_knight_phantasm_illusion"; "modifier_chaos_knight_armageddon_phantasms"
было: 0x4aec760 (1493 байт)
- числа в инструкциях: +1
- инструкций: 364 → 367
```diff
@@ -18,6 +18,8 @@
 test rax, rax
 je L
-cmp r13b, byte ptr [rax + 0x7a6]
-jne L
+cmp byte ptr [rax + 0x7a6], 1
+jne L
+test r13b, r13b
+je L
 mov rdi, rbx
 call F
@@ -40,9 +42,4 @@
 pop rbp
 jmp rax
-nop word ptr cs:[rax + rax]
-movzx esi, r13b
-mov rdi, rax
-call F
-jmp L
 nop
 mov rdi, rbx
@@ -306,4 +303,9 @@
 jmp L
 nop dword ptr [rax]
+xor esi, esi
+mov rdi, rax
+call F
+jmp L
+nop word ptr [rax + rax]
 xor ecx, ecx
 xor edx, edx
@@ -332,6 +334,7 @@
 jmp L
 nop word ptr [rax + rax]
-cmp dword ptr [rbp - 0x78], r14d
+mov ecx, dword ptr [rbp - 0x78]
 mov eax, r14d
+cmp r14d, ecx
 je L
 mov rcx, qword ptr [rbp - 0x80]
@@ -341,16 +344,16 @@
 mov edi, dword ptr [rbp - 0x50]
 jmp L
+nop word ptr [rax + rax]
 mov dword ptr [rbp - 0x74], 0
 xor r14d, r14d
 mov qword ptr [rbp - 0x80], 0
```
(ещё 15 строк диффа: so-query.py fdiff libserver.so 0x4aef7a0)

### изменена: 0x4c78b10 (76 байт) CDOTA_Modifier_Shredder_Reactive_Armor::vfunc#97
было: 0x4c75ad0 (51 байт)
- числа в инструкциях: +0
- поля объектов: +0xd80 +0xd88
- цели вызовов: +0x4d233b0 +0x4d234b0 −0x4d22cb0 "modifier_shredder_reactive_armor_stack"; "duration"
- инструкций: 7 → 10
```diff
@@ -3,4 +3,7 @@
 mov qword ptr [rdi + 0xd70], rax
 lea rax, [T]
+mov qword ptr [rdi + 0xd80], rax
+lea rax, [T]
+mov qword ptr [rdi + 0xd88], 0
 mov qword ptr [rdi + 0xed0], rax
 mov qword ptr [rdi + 0xed8], 0
```

### изменена: 0x4ce1230 (317 байт) вызывается из: CDOTA_Modifier_Primal_Beast_Colossal::vfunc#97 | строки: "modifier_primal_beast_trample"
было: 0x4cde7e0 (325 байт)
- инструкций: 78 → 76
```diff
@@ -56,9 +56,7 @@
 pxor xmm0, xmm0
 movss xmm2, dword ptr [rbx + 0x1b10]
-cvtsi2ss xmm1, dword ptr [rbx + 0x1b08]
+cvtsi2ss xmm1, dword ptr [rbx + 0x1afc]
 cvtsi2ss xmm0, eax
-mulss xmm0, xmm1
-pxor xmm1, xmm1
-cvtsi2ss xmm1, dword ptr [rbx + 0x1afc]
+mulss xmm0, dword ptr [rbx + 0x1b08]
 addss xmm0, xmm1
 pxor xmm1, xmm1
```

### изменена: 0x4d22cb0 (1778 байт) | строки: "modifier_shredder_reactive_armor_stack"; "duration"; "particles/units/heroes/hero_shredder/shredder_reactive_hit.vpcf"; "attach_chimmney"; "attach_hitloc"; "Hero_Shredder.ReactiveArmor"
было: 0x4cf4230 (1098 байт)
- строки: −"modifier_shredder_reactive_armor_stack" −"modifier_shredder_reactive_armor_stack" −"modifier_shredder_reactive_armor_stack"
- константы из данных (числа логики): +0x00000000000000090000000000000000 +-1,-1,3.402823e+38,3.402823e+38 +0x00000000ffffffff
- числа в инструкциях: +0xffffffff +0 +0 +0 +0 +0 +0 +0 −-1 −-2 −-2 −9 −9 −0x3f −0x3f −0x1ff (и ещё 37)
- поля объектов: −0xd0 −0xd0 −0x10 −0x10 −0x5d1 −0x5d1 −0xcc −0xcc
- прямых вызовов: 40 → 48
- цели вызовов: +__cxa_guard_acquire() +0x6a45230 +__cxa_atexit() +__cxa_guard_release() +0x59ddca0 +0x4cc14f0 +0x4cbf3a0 +0x3bbdd80 +0x552e130 −0x4cb4170
- инструкций: 276 → 351
```diff
@@ -1,123 +1,163 @@
 push rbp
-mov rax, rdx
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
```
(ещё 364 строк диффа: so-query.py fdiff libserver.so 0x4d22cb0)

### изменена: 0x4d64db0 (411 байт) CDOTA_Modifier_Primal_Beast_Colossal::OnRefresh | строки: "model_scale_per_stack"; "base_slow_resist"; "base_aoe"; "hp_per_threshold"; "slow_resistance_per_threshold"; "aoe_per_threshold"; "trample_bonus"
было: 0x4d62f10 (404 байт)
- инструкций: 109 → 110
```diff
@@ -66,6 +66,6 @@
 mov rax, qword ptr [rbx]
 call qword ptr [rax + 0x1f0]
-xor eax, eax
 test r12, r12
+pxor xmm1, xmm1
 je L
 lea rsi, [S:"slow_resistance_per_threshold"]
@@ -73,6 +73,7 @@
 mov rdi, r12
 call F
+movaps xmm1, xmm0
+movss dword ptr [rbx + 0x1b08], xmm1
 mov rdi, rbx
-mov dword ptr [rbx + 0x1b08], eax
 call F
 mov rdi, rbx
```

### изменена: 0x4d7ef00 (2031 байт) CDOTA_Ability_Wisp_Tether::OnSpellStart | строки: "latch_distance"; "modifier_wisp_overcharge"; "modifier_wisp_tether"; "target"; "modifier_wisp_tether_cooldown"; "modifier_wisp_tether_haste"; "wisp_tether_break"; "wisp_tether"
было: 0x4d7bcc0 (2399 байт)
- строки: −"CNetworkTransmitComponent::StateChanged(%s) @%s:%d"
- числа в инструкциях: −3 −0 −0 −0 −1 −0x3fffffff −0x40
- виртуальные вызовы: +0xf0 (слот 30)
- поля объектов: −0xf0 −0x318 −0x48 −0x18 −0x315 −0x310 −0x32e −0x30 −0x538 −0x538 −0x530
- прямых вызовов: 66 → 61
- цели вызовов: −CDOTA_NPCSpawnerGoodTop::vfunc#30 −V_UnqualifiedFileName() −0x3bbe670 −0x3c21740 −_ZN13CBufferString5PurgeEi() −0x3c43760 " ignored"; "%u,"
- инструкций: 491 → 422
```diff
@@ -7,5 +7,5 @@
 push rbx
 mov rbx, rdi
-sub rsp, 0x188
+sub rsp, 0xe8
 call F
 mov rdi, rbx
@@ -32,5 +32,5 @@
 lea r15, [S:"modifier_wisp_overcharge"]
 xor edx, edx
-lea r13, [rbp - 0x140]
+lea r13, [rbp - 0xd0]
 mov rdi, rax
 mov rsi, r15
@@ -88,10 +88,10 @@
 call qword ptr [rax + 0x938]
 mov rdi, rbx
-movss dword ptr [rbp - 0x1a0], xmm0
+movss dword ptr [rbp - 0x100], xmm0
 call F
 xor r8d, r8d
 mov rdx, rbx
 mov rdi, r15
-movss xmm0, dword ptr [rbp - 0x1a0]
+movss xmm0, dword ptr [rbp - 0x100]
 mov rsi, rax
 lea rcx, [S:"modifier_wisp_tether_cooldown"]
@@ -169,9 +169,9 @@
 pxor xmm3, xmm3
 movq xmm2, qword ptr [rax]
-movss dword ptr [rbp - 0x188], xmm3
+movss dword ptr [rbp - 0xe8], xmm3
 subps xmm2, xmm0
 movshdup xmm0, xmm2
 movaps xmm1, xmm2
-movlps qword ptr [rbp - 0x190], xmm2
+movlps qword ptr [rbp - 0xf0], xmm2
 mulss xmm1, xmm2
 mulss xmm0, xmm0
@@ -184,10 +184,10 @@
 comiss xmm1, dword ptr [K:1e+17]
 jbe L
-lea rdi, [rbp - 0x190]
+lea rdi, [rbp - 0xf0]
 call F
 movaps xmm1, xmm0
 pxor xmm0, xmm0
```
(ещё 384 строк диффа: so-query.py fdiff libserver.so 0x4d7ef00)

### изменена: 0x4d90580 (5588 байт) CDOTA_Modifier_VoidSpirit_AetherRemnant_Unit::OnIntervalThink | строки: "rotation_speed"; "modifier_void_spirit_aether_remnant_watch_thinker"; "duration"; "is_artifice"; "npc_dota_hero_rubick"; "particles/units/heroes/hero_void_spirit/aether_remnant/void_spirit_aether_remnan"; "particles/units/heroes/hero_rubick/rubick_aether_remnant_watch.vpcf"; "particles/units/heroes/hero_rubick/aether_remnant/void_spirit_aether_remnant_wat"
было: 0x4d8d4a0 (5604 байт)
- цели вызовов: +0x4422530
- инструкций: 1200 → 1196
```diff
@@ -711,12 +711,8 @@
 call qword ptr [rax + 0xe30]
 lea rsi, [S:"npc_dota_hero_rubick"]
-cmp rax, rsi
-je L
-test rax, rax
-je L
-mov rdi, rax
-call F
-test eax, eax
-je L
+mov rdi, rax
+call F
+test al, al
+jne L
 lea rax, [D]
 mov rax, qword ptr [rax]
@@ -725,5 +721,5 @@
 cmp dword ptr [rax + 0x484], 0x12
 je L
-nop word ptr [rax + rax]
+nop dword ptr [rax]
 mov esi, dword ptr [rbx + 0x1b38]
 sub rsp, 8
```

### изменена: 0x4feab90 (962 байт) CDOTA_Modifier_Item_PyrrhicCloak::vfunc#88 | строки: "damage_pct"; "max_distance"; "target"; "buff"; "particles/items4_fx/retributor_cloak.vpcf"; "attach_hitloc"
было: 0x4fe7aa0 (904 байт)
- числа в инструкциях: +-1 +-2 +9 +0x3f +0x1ff +0x70
- поля объектов: +0x10 +0x1b00
- прямых вызовов: 34 → 33
- цели вызовов: −0x3baa7c0
- инструкций: 213 → 226
```diff
@@ -36,13 +36,25 @@
 test rax, rax
 je L
-mov eax, dword ptr [rax + 0x10]
-mov dword ptr [rbx + 0x1b00], eax
-jmp L
-nop word ptr cs:[rax + rax]
-mov dword ptr [rbx + 0x1b00], 0xffffffff
-lea rdi, [rbx + 0x1b00]
-call F
-test rax, rax
-je L
+mov ecx, dword ptr [rax + 0x10]
+cmp ecx, -1
+mov dword ptr [rbx + 0x1b00], ecx
+je L
+mov rsi, qword ptr [D]
+test rsi, rsi
+je L
+cmp ecx, -2
+je L
+movzx eax, word ptr [rbx + 0x1b00]
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
 mov r13, qword ptr [rax]
 test r13, r13
@@ -209,5 +221,6 @@
 pop rbp
 ret
-nop word ptr [rax + rax]
+nop dword ptr [rax]
+mov dword ptr [rbx + 0x1b00], 0xffffffff
 xor r13d, r13d
 jmp L
```

### изменена: 0x4feb9c0 (378 байт) CDOTA_Modifier_Searing_Signet_Burn::OnCreated | строки: "burn_damage"; "burn_tickrate"; "burn_duration"; "creep_penalty"
было: 0x4fe8890 (354 байт)
- числа в инструкциях: +0xffffffff
- поля объектов: +0x1af8
- инструкций: 88 → 96
```diff
@@ -11,8 +11,16 @@
 mov rax, qword ptr [rbx]
 call qword ptr [rax + 0x1f0]
-lea rsi, [rbx + 0x1af8]
+test r12, r12
+pxor xmm1, xmm1
+je L
+xor r9d, r9d
+xor r8d, r8d
+xor ecx, ecx
+lea rsi, [S:"burn_damage"]
+mov edx, 0xffffffff
 mov rdi, r12
-lea rdx, [S:"burn_damage"]
 call F
+movaps xmm1, xmm0
+movss dword ptr [rbx + 0x1af8], xmm1
 mov rdi, rbx
 call F
@@ -84,5 +92,5 @@
 pop rbp
 jmp F
-nop dword ptr [rax]
+nop
 movss xmm0, dword ptr [rbx + 0x1af8]
 jmp L
```

### изменена: 0x4fecd10 (282 байт) CDOTA_Modifier_Item_Rattlecage::OnRefresh | строки: "bonus_armor"; "damage_threshold"; "damage_reset_interval"; "radius"
было: 0x4fe9bd0 (255 байт)
- числа в инструкциях: +0xffffffff
- поля объектов: +0x1b00
- прямых вызовов: 11 → 12
- цели вызовов: −0x3bbee70
- инструкций: 69 → 78
```diff
@@ -61,9 +61,18 @@
 mov rax, qword ptr [rbx]
 call qword ptr [rax + 0x1f0]
-lea rsi, [rbx + 0x1b00]
+test r12, r12
+pxor xmm1, xmm1
+je L
+xor r9d, r9d
+xor r8d, r8d
+xor ecx, ecx
+lea rsi, [S:"radius"]
+mov edx, 0xffffffff
 mov rdi, r12
+call F
+movaps xmm1, xmm0
+movss dword ptr [rbx + 0x1b00], xmm1
 pop rbx
 pop r12
 pop rbp
-lea rdx, [S:"radius"]
-jmp F
+ret
```

### изменена: 0x4fee4b0 (1860 байт) CDOTA_Modifier_Item_Rattlecage::vfunc#129 | строки: "target_count"; "projectile_speed"; "particles/items2_fx/rattlecage_projectile.vpcf"
было: 0x4feb350 (1956 байт)
- числа в инструкциях: −3 −-1 −-2 −9 −0x3f −0x1ff −0x70
- поля объектов: −0x5d1 −0xcc −0xcc −0x10
- прямых вызовов: 36 → 37
- цели вызовов: +0x44c0130
- инструкций: 392 → 371
```diff
@@ -43,44 +43,23 @@
 mov rdi, r12
 call F
-cvttss2si eax, dword ptr [r13 + 4]
+cvttss2si r14d, dword ptr [r13 + 4]
 pxor xmm0, xmm0
-add eax, dword ptr [r12 + 0x1af8]
-mov dword ptr [r12 + 0x1af8], eax
+add r14d, dword ptr [r12 + 0x1af8]
+mov dword ptr [r12 + 0x1af8], r14d
 ucomiss xmm0, dword ptr [r13 + 4]
 jp L
 jne L
-mov esi, dword ptr [r13 + 0xcc]
-cmp esi, -1
-je L
-mov rdi, qword ptr [D]
-test rdi, rdi
-je L
-cmp esi, -2
-je L
-movzx edx, word ptr [r13 + 0xcc]
-mov rcx, rdx
-shr rcx, 9
-and ecx, 0x3f
-mov rcx, qword ptr [rdi + rcx*8]
-test rcx, rcx
-je L
-and edx, 0x1ff
-imul rdx, rdx, 0x70
-add rdx, rcx
-cmp esi, dword ptr [rdx + 0x10]
-jne L
-mov r14, qword ptr [rdx]
-test r14, r14
-je L
-cmp byte ptr [r14 + 0x5d1], 3
-jne L
-mov rdi, r12
-call F
-cmp r14, rax
-jne L
-mov eax, dword ptr [r12 + 0x1af8]
-nop
-add eax, dword ptr [r13 + 0x4c]
-mov dword ptr [r12 + 0x1af8], eax
+mov rdi, r13
```
(ещё 20 строк диффа: so-query.py fdiff libserver.so 0x4fee4b0)

### изменена: 0x5417830 (3017 байт) | строки: "particles/neutral_fx/neutral_item_drop_lvl%d.vpcf"; "NeutralLootDrop.Spawn"; "<unknown>"; "CNetworkTransmitComponent::StateChanged(%s) @%s:%d"
было: 0x54147f0 (2729 байт)
- строки: +"CNetworkTransmitComponent::StateChanged(%s) @%s:%d"
- числа в инструкциях: +0x40 +0x3fffffff +3
- поля объектов: +0x310 +0x32e
- прямых вызовов: 50 → 53
- цели вызовов: +V_UnqualifiedFileName() +0x3c21740
- инструкций: 507 → 552
```diff
@@ -6,7 +6,7 @@
 push r12
 push rbx
-sub rsp, 0x2f8
+sub rsp, 0x308
 test rsi, rsi
-mov dword ptr [rbp - 0x304], ecx
+mov dword ptr [rbp - 0x30c], ecx
 movq qword ptr [rbp - 0x2b0], xmm0
 movss dword ptr [rbp - 0x2a8], xmm1
@@ -15,12 +15,12 @@
 je L
 mov rax, qword ptr [rsi]
-mov r13, rdi
+mov r14, rdi
 mov rbx, rsi
 mov rdi, rsi
-mov r14d, edx
+mov r13d, edx
 call qword ptr [rax + 0xc70]
 xor ecx, ecx
 xor esi, esi
-mov rdi, r13
+mov rdi, r14
 mov edx, eax
 call F
@@ -68,5 +68,5 @@
 movq xmm0, qword ptr [rbp - 0x290]
 movss xmm1, dword ptr [rbp - 0x288]
-movss dword ptr [rbp - 0x308], xmm7
+movss dword ptr [rbp - 0x310], xmm7
 movaps xmm6, xmmword ptr [rbp - 0x2f0]
 movss xmm2, dword ptr [rbp - 0x2f8]
@@ -89,6 +89,6 @@
 movq xmm2, qword ptr [rbp - 0x2c0]
 movq xmm1, xmm1
-movzx eax, byte ptr [rbx + 0x624]
-cmp dword ptr [r12 + 0x884], eax
+movzx r9d, byte ptr [rbx + 0x624]
+cmp dword ptr [r12 + 0x884], r9d
 addps xmm1, xmm2
 addss xmm0, dword ptr [rbp - 0x2b8]
@@ -97,6 +97,8 @@
 jne L
 mov r15, qword ptr [K:0xffffffffffffffff]
+lea rax, [rbp - 0x1e0]
+mov qword ptr [rbp - 0x2f0], rax
```
(ещё 480 строк диффа: so-query.py fdiff libserver.so 0x5417830)

### изменена: 0x54197e0 (3172 байт) вызывается из: CDOTA_Modifier_MudGolem_RockDestroy::vfunc#97 | строки: "shard_amount"; "shard_health"; "shard_damage"; "shard_duration"; "npc_dota_neutral_mud_golem"; "npc_dota_neutral_mud_golem_split"; "modifier_kill"; "duration"
было: 0x5416680 (3170 байт)
- числа в инструкциях: −1 −1
- цели вызовов: +0x5413a20
- инструкций: 696 → 696
```diff
@@ -121,5 +121,5 @@
 mov rax, qword ptr [r15]
 call qword ptr [rax + 0x1f0]
-lea rsi, [rbp - 0x124]
+lea rsi, [rbp - 0x128]
 mov rdi, rbx
 lea rdx, [S:"shard_amount"]
@@ -165,5 +165,5 @@
 test al, al
 je L
-mov r8d, dword ptr [rbp - 0x124]
+mov r8d, dword ptr [rbp - 0x128]
 xor eax, eax
 test r8d, r8d
@@ -651,11 +651,14 @@
 mov r13, qword ptr [rbp - 0x168]
 jmp L
-xor ecx, ecx
-mov esi, 1
+lea rax, [rbp - 0xa8]
+xor ecx, ecx
 pxor xmm0, xmm0
-mov qword ptr [rbp - 0xb0], 1
-lea rdi, [rbp - 0xa0]
+mov dword ptr [rbp - 0x124], 0x1768
+lea rsi, [rbp - 0x124]
+mov rdi, rax
 mov word ptr [rbp - 0x74], cx
 movaps xmmword ptr [rbp - 0x90], xmm0
+mov qword ptr [rbp - 0x138], rax
+mov qword ptr [rbp - 0xb0], 1
 mov qword ptr [rbp - 0xa8], 0
 mov qword ptr [rbp - 0xa0], 0
@@ -664,12 +667,9 @@
 mov dword ptr [rbp - 0x78], 0xffffffff
 call F
-mov rax, qword ptr [rbp - 0xa0]
+mov rdx, qword ptr [rbx]
 mov rsi, r12
 mov rdi, rbx
-add dword ptr [rbp - 0xa8], 1
-mov dword ptr [rax], 0x1768
-mov rax, qword ptr [rbx]
-call qword ptr [rax + 0xf0]
-lea rdi, [rbp - 0xa8]
+call qword ptr [rdx + 0xf0]
+mov rdi, qword ptr [rbp - 0x138]
```
(ещё 2 строк диффа: so-query.py fdiff libserver.so 0x54197e0)

### изменена: 0x5424380 (3153 байт) CDOTA_Ability_DarkTrollWarlord_Ensnare::vfunc#399 | строки: "modifier_do_not_cast_ensnare"; "neutral_chance_to_cast"; "neutral_cast_attempt_cooldown"; "modifier_neutral_cast_attempt_cooldown"; "duration"
было: 0x5421220 (3313 байт)
- константы из данных (числа логики): −1e+17 −1 −1e-17
- инструкций: 675 → 644
```diff
@@ -118,31 +118,10 @@
 mulss xmm1, xmm3
 movq xmm0, xmm0
-movss dword ptr [rbp - 0x198], xmm1
+movss dword ptr [rbp - 0x190], xmm1
 mulps xmm0, xmm2
-movlps qword ptr [rbp - 0x1a0], xmm0
-movq xmm2, qword ptr [rbp - 0x190]
-pxor xmm3, xmm3
-movss dword ptr [rbp - 0x188], xmm3
-movss xmm7, dword ptr [K:1e-17]
-movshdup xmm1, xmm2
-movaps xmm0, xmm2
-mulss xmm0, xmm2
-mulss xmm1, xmm1
-addss xmm1, xmm3
-addss xmm0, xmm1
-sqrtss xmm0, xmm0
-comiss xmm7, xmm0
-ja L
-comiss xmm0, dword ptr [K:1e+17]
-ja L
-movss xmm1, dword ptr [K:1]
-movq xmm2, xmm2
-divss xmm1, xmm0
-movsldup xmm0, xmm1
-mulss xmm1, xmm3
-movq xmm0, xmm0
-movss dword ptr [rbp - 0x188], xmm1
-mulps xmm0, xmm2
-movlps qword ptr [rbp - 0x190], xmm0
+movlps qword ptr [rbp - 0x198], xmm0
+lea rdi, [rbp - 0x17c]
+mov dword ptr [rbp - 0x174], 0
+call F
 mov rdi, qword ptr [rbp - 0x148]
 add rdi, r13
@@ -163,29 +142,29 @@
 call F
 movq xmm1, qword ptr [r14]
-lea rdi, [rbp - 0x180]
+lea rdi, [rbp - 0x188]
 movq xmm0, qword ptr [rax]
-mov dword ptr [rbp - 0x178], 0
+mov dword ptr [rbp - 0x180], 0
 subps xmm0, xmm1
-movlps qword ptr [rbp - 0x180], xmm0
```
(ещё 92 строк диффа: so-query.py fdiff libserver.so 0x5424380)

### изменена: 0x542c410 (1398 байт) вызывается из: CDOTA_Modifier_BigThunderLizard_Slam_Thinker::OnCreated, CDOTA_Modifier_BigThunderLizard_Slam_Thinker::OnIntervalThink | строки: "particles/neutral_fx/ursa_thunderclap.vpcf"; "n_creep_Thunderlizard_Big.Stomp"; "modifier_beastmaster_thunderhide_bonus_damage"; "non_hero_duration"; "hero_duration"; "thunderhide_slam_duration"; "modifier_big_thunder_lizard_slam"; "duration"
было: 0x5429350 (1323 байт)
- строки: +"modifier_beastmaster_thunderhide_bonus_damage" +"thunderhide_slam_duration"
- константы из данных (числа логики): +-1
- прямых вызовов: 39 → 43
- инструкций: 284 → 303
```diff
@@ -8,5 +8,5 @@
 push rbx
 mov rbx, rdi
-sub rsp, 0x108
+sub rsp, 0x118
 cvtsi2ss xmm0, dword ptr [rdi + 0x1b08]
 mulss xmm0, dword ptr [rdi + 0x1afc]
@@ -14,5 +14,5 @@
 movsldup xmm4, xmm0
 movss dword ptr [rbp - 0x118], xmm0
-movq r15, xmm4
+movlps qword ptr [rbp - 0x120], xmm4
 call F
 mov rdi, rbx
@@ -36,5 +36,5 @@
 lea r8, [rbp - 0xf0]
 push 0
-lea r12, [rbp - 0xd0]
+lea r13, [rbp - 0xd0]
 mov esi, r14d
 push 0
@@ -43,17 +43,16 @@
 movss xmm0, dword ptr [rbp - 0x118]
 call F
-mov rax, qword ptr [rbp - 0xe8]
+mov eax, dword ptr [rbp - 0xdc]
 add rsp, 0x20
-movsxd r14, dword ptr [rbp - 0xf0]
-mov qword ptr [rbp - 0x128], rax
-mov eax, dword ptr [rbp - 0xdc]
-mov dword ptr [rbp - 0x12c], eax
-call F
-mov rdi, rbx
-mov r13, rax
+movsxd r15, dword ptr [rbp - 0xf0]
+mov r12, qword ptr [rbp - 0xe8]
+mov dword ptr [rbp - 0x130], eax
+call F
+mov rdi, rbx
+mov r14, rax
 call F
 movaps xmm0, xmmword ptr [K:-1,-1,3.402823e+38,3.402823e+38]
-mov rdi, r13
-mov rsi, r12
+mov rdi, r14
+mov rsi, r13
 mov qword ptr [rbp - 0xc0], rax
```
(ещё 249 строк диффа: so-query.py fdiff libserver.so 0x542c410)

### изменена: 0x5d37d60 (31 байт) вызывается из: CDOTA_Modifier_Special_Bonus_HP_Regen::vfunc#97
было: 0x5d34c50 (35 байт)
- инструкций: 8 → 7
```diff
@@ -1,4 +1,3 @@
-pxor xmm0, xmm0
-cvtsi2ss xmm0, dword ptr [rsi + 0x1af8]
+movss xmm0, dword ptr [rsi + 0x1af8]
 mov rax, rdi
 mov dword ptr [rdi], 1
```

### изменена: 0x5de6650 (555178 байт)
было: 0x5de3290 (554458 байт)
- константы из данных (числа логики): +0x00000000000000090000000000000000
- числа в инструкциях: +0xffffffff +0 +0 +0 +0 +0 +0 +0 (и ещё 19)
- прямых вызовов: 5392 → 5399
- цели вызовов: +0x5d8eea0 −0x5d8ec20
- инструкций: 86256 → 86368
```diff
@@ -86129,4 +86129,116 @@
 push rbp
 mov rbp, rsp
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
```
(ещё 70 строк диффа: so-query.py fdiff libserver.so 0x5de6650)

### изменена: 0x5e6f8a0 (83 байт) CDOTA_Modifier_Special_Bonus_Corruption_Debuff::OnCreated | строки: "value"
было: 0x5e6d0e0 (76 байт)
- цели вызовов: +0x3bbeb20 "AbilityManaCost"; "AbilityHealthCost" −0x3bbf6f0 "AbilityManaCost"; "AbilityHealthCost"
- инструкций: 25 → 26
```diff
@@ -9,6 +9,6 @@
 mov rax, qword ptr [rbx]
 call qword ptr [rax + 0x1f0]
-xor eax, eax
 test r12, r12
+pxor xmm1, xmm1
 je L
 xor r9d, r9d
@@ -19,5 +19,6 @@
 mov rdi, r12
 call F
-mov dword ptr [rbx + 0x1af8], eax
+movaps xmm1, xmm0
+movss dword ptr [rbx + 0x1af8], xmm1
 pop rbx
 pop r12
```

### изменена: 0x5ee9e40 (119604 байт) | строки: "scripts/height_levels.txt"; "dota_hud_use_mmr_token"; "dota_force_tp_team"; "dota_force_tp_quality"; "dota_force_plus"; "modifier_plus_high_five_requested"; "modifier_plus_high_five_success"; "dota_projectile_debug"
было: 0x5ee6780 (119464 байт)
- числа в инструкциях: +0 +0
- прямых вызовов: 2544 → 2547
- инструкций: 18894 → 18916
```diff
@@ -18533,5 +18533,26 @@
 mov rsi, rbx
 mov qword ptr [rbp - 0xa8], r12
-xor r15d, r15d
+mov qword ptr [D], rax
+mov rax, qword ptr [r14]
+lea rdi, [D]
+mov qword ptr [rbp - 0xa0], 0
+mov qword ptr [D], rax
+lea rax, [D]
+mov qword ptr [r14], rax
+lea rax, [T]
+mov qword ptr [D], rax
+lea rax, [T]
+mov qword ptr [rbp - 0xb0], rax
+call F
+mov rsi, rbx
+mov qword ptr [rbp - 0xa8], r12
+lea rax, [T]
+mov qword ptr [rbp - 0xa0], 0
+lea rdi, [D]
+mov qword ptr [rbp - 0xb0], rax
+call F
+call F
+mov rsi, rbx
+mov qword ptr [rbp - 0xa8], r12
 mov qword ptr [D], rax
 mov rax, qword ptr [r14]
@@ -18751,6 +18772,7 @@
 xor r11d, r11d
 mov r9, rbx
+xor r15d, r15d
+lea rax, [D]
 mov ecx, 4
-lea rax, [D]
 xor edx, edx
 mov word ptr [rbp - 0xac], r11w
```

### изменена: 0x5f2ee80 (8268 байт) | строки: "m_nInitiatingPlayerID"; "int"; "int32"; "m_PingWheelMessageID"; "m_flActiveUntilTime"; "float"; "float32"; "m_vLocation"
было: 0x5f2b720 (8188 байт)
- строки: −"int" −"int" −"int" −"int" −"int" −"int" −"int"
- числа в инструкциях: +1 +1
- инструкций: 1787 → 1807
```diff
@@ -20,16 +20,16 @@
 push r12
 push rbx
-sub rsp, 0x68
+sub rsp, 0x78
 movzx eax, byte ptr [D]
 test al, al
 je L
 lea rax, [D]
-mov qword ptr [rbp - 0x88], rax
+mov qword ptr [rbp - 0x90], rax
 movzx eax, byte ptr [D]
 test al, al
-mov byte ptr [rbp - 0x89], al
-je L
-mov rax, qword ptr [rbp - 0x88]
-add rsp, 0x68
+mov byte ptr [rbp - 0x91], al
+je L
+mov rax, qword ptr [rbp - 0x90]
+add rsp, 0x78
 pop rbx
 pop r12
@@ -40,13 +40,14 @@
 ret
 nop dword ptr [rax]
-lea r13, [S:"m_nInitiatingPlayerID"]
+lea r12, [S:"m_nInitiatingPlayerID"]
 mov esi, 0x31415933
 mov byte ptr [D], 1
-mov rdi, r13
-call F
-lea rdi, [r13 + 8]
+lea r15, [S:"int"]
+mov rdi, r12
+call F
+lea rdi, [r12 + 8]
 mov esi, eax
 call F
-lea rdi, [r13 + 0x10]
+lea rdi, [r12 + 0x10]
 mov esi, eax
 call F
@@ -67,39 +68,156 @@
 mov rsi, rbx
 mov rdi, rax
+mov r13, rax
```
(ещё 2755 строк диффа: so-query.py fdiff libserver.so 0x5f2ee80)

### изменена: 0x3e74dc0 (1059 байт) | строки: "CNetworkUtlVectorBase"; "AnimationAlgorithm_t"; "ExternalAnimGraphHandle_t"; "CGlobalSymbol"; "CBaseAnimGraph"; "CHandle"; "GameTime_t"; "CUtlVectorEmbeddedNetworkVar"
- код тот же, но вызывает другую функцию: было 0x3eac1d0, стало 0x3eaec90

### изменена: 0x5db9920 (634 байт) | строки: "GameTime_t"; "sPlayerSnapshot"; "CUtlVector"
- код тот же, но вызывает другую функцию: было 0x5d3caf0, стало 0x5d3fc00

### изменена: 0x5ddbdc0 (4383 байт)
- код тот же, но вызывает другую функцию: было 0x5d8b960, стало 0x5d8ebf0

### изменена: 0x5e6e050 (419 байт) | строки: "CDOTASpectatorGraphManager"
- код тот же, но вызывает другую функцию: было 0x5d3cb00, стало 0x5d3fc10

### изменена: 0x5f30ed0 (484 байт) | строки: "CDOTA_Ability_Special_Bonus_HP_100"
- код тот же, но вызывает другую функцию: было 0x5d81ba0, стало 0x5d84e00

### изменена: 0x5f310c0 (436 байт) | строки: "CDOTA_Ability_Special_Bonus_HP_125"
- код тот же, но вызывает другую функцию: было 0x5d81b20, стало 0x5d84d80

### изменена: 0x5f31280 (436 байт) | строки: "CDOTA_Ability_Special_Bonus_HP_150"
- код тот же, но вызывает другую функцию: было 0x5d81aa0, стало 0x5d84d00

### изменена: 0x5f31440 (436 байт) | строки: "CDOTA_Ability_Special_Bonus_HP_175"
- код тот же, но вызывает другую функцию: было 0x5d81a20, стало 0x5d84c80

### изменена: 0x5f31600 (436 байт) | строки: "CDOTA_Ability_Special_Bonus_HP_200"
- код тот же, но вызывает другую функцию: было 0x5d819a0, стало 0x5d84c00

### изменена: 0x5f317c0 (436 байт) | строки: "CDOTA_Ability_Special_Bonus_HP_225"
- код тот же, но вызывает другую функцию: было 0x5d81920, стало 0x5d84b80

### изменена: 0x5f31980 (436 байт) | строки: "CDOTA_Ability_Special_Bonus_HP_250"
- код тот же, но вызывает другую функцию: было 0x5d818a0, стало 0x5d84b00

### изменена: 0x5f31b40 (436 байт) | строки: "CDOTA_Ability_Special_Bonus_HP_275"
- код тот же, но вызывает другую функцию: было 0x5d81820, стало 0x5d84a80

### изменена: 0x5f31d00 (436 байт) | строки: "CDOTA_Ability_Special_Bonus_HP_300"
- код тот же, но вызывает другую функцию: было 0x5d817a0, стало 0x5d84a00

### изменена: 0x5f31ec0 (436 байт) | строки: "CDOTA_Ability_Special_Bonus_HP_325"
- код тот же, но вызывает другую функцию: было 0x5d81720, стало 0x5d84980

### изменена: 0x5f32080 (436 байт) | строки: "CDOTA_Ability_Special_Bonus_HP_350"
- код тот же, но вызывает другую функцию: было 0x5d816a0, стало 0x5d84900

### изменена: 0x5f32240 (436 байт) | строки: "CDOTA_Ability_Special_Bonus_HP_375"
- код тот же, но вызывает другую функцию: было 0x5d81620, стало 0x5d84880

### изменена: 0x5f32400 (436 байт) | строки: "CDOTA_Ability_Special_Bonus_HP_400"
- код тот же, но вызывает другую функцию: было 0x5d815a0, стало 0x5d84800

### изменена: 0x5f325c0 (436 байт) | строки: "CDOTA_Ability_Special_Bonus_HP_450"
- код тот же, но вызывает другую функцию: было 0x5d81520, стало 0x5d84780

### изменена: 0x5f32780 (436 байт) | строки: "CDOTA_Ability_Special_Bonus_HP_475"
- код тот же, но вызывает другую функцию: было 0x5d814a0, стало 0x5d84700

### изменена: 0x5f32940 (436 байт) | строки: "CDOTA_Ability_Special_Bonus_HP_500"
- код тот же, но вызывает другую функцию: было 0x5d81420, стало 0x5d84680

### изменена: 0x5f32b00 (436 байт) | строки: "CDOTA_Ability_Special_Bonus_HP_600"
- код тот же, но вызывает другую функцию: было 0x5d813a0, стало 0x5d84600

### изменена: 0x5f32cc0 (436 байт) | строки: "CDOTA_Ability_Special_Bonus_HP_650"
- код тот же, но вызывает другую функцию: было 0x5d81320, стало 0x5d84580

### изменена: 0x5f32e80 (436 байт) | строки: "CDOTA_Ability_Special_Bonus_HP_700"
- код тот же, но вызывает другую функцию: было 0x5d812a0, стало 0x5d84500

### изменена: 0x5f33040 (436 байт) | строки: "CDOTA_Ability_Special_Bonus_HP_800"
- код тот же, но вызывает другую функцию: было 0x5d81220, стало 0x5d84480

### изменена: 0x5f33200 (436 байт) | строки: "CDOTA_Ability_Special_Bonus_HP_900"
- код тот же, но вызывает другую функцию: было 0x5d811a0, стало 0x5d84400

### изменена: 0x5f333c0 (436 байт) | строки: "CDOTA_Ability_Special_Bonus_HP_1000"
- код тот же, но вызывает другую функцию: было 0x5d81120, стало 0x5d84380

### изменена: 0x5f33580 (436 байт) | строки: "CDOTA_Ability_Special_Bonus_MP_100"
- код тот же, но вызывает другую функцию: было 0x5d810a0, стало 0x5d84300

### изменена: 0x5f33740 (436 байт) | строки: "CDOTA_Ability_Special_Bonus_MP_125"
- код тот же, но вызывает другую функцию: было 0x5d81020, стало 0x5d84280

### изменена: 0x5f33900 (436 байт) | строки: "CDOTA_Ability_Special_Bonus_MP_150"
- код тот же, но вызывает другую функцию: было 0x5d80fa0, стало 0x5d84200

### изменена: 0x5f33ac0 (436 байт) | строки: "CDOTA_Ability_Special_Bonus_MP_175"
- код тот же, но вызывает другую функцию: было 0x5d80f20, стало 0x5d84180

### изменена: 0x5f33c80 (436 байт) | строки: "CDOTA_Ability_Special_Bonus_MP_200"
- код тот же, но вызывает другую функцию: было 0x5d80ea0, стало 0x5d84100

### изменена: 0x5f33e40 (436 байт) | строки: "CDOTA_Ability_Special_Bonus_MP_225"
- код тот же, но вызывает другую функцию: было 0x5d80e20, стало 0x5d84080

### изменена: 0x5f34000 (436 байт) | строки: "CDOTA_Ability_Special_Bonus_MP_250"
- код тот же, но вызывает другую функцию: было 0x5d80da0, стало 0x5d84000

### изменена: 0x5f341c0 (436 байт) | строки: "CDOTA_Ability_Special_Bonus_MP_275"
- код тот же, но вызывает другую функцию: было 0x5d80d20, стало 0x5d83f80

### изменена: 0x5f34380 (436 байт) | строки: "CDOTA_Ability_Special_Bonus_MP_300"
- код тот же, но вызывает другую функцию: было 0x5d80ca0, стало 0x5d83f00

### изменена: 0x5f34540 (436 байт) | строки: "CDOTA_Ability_Special_Bonus_MP_350"
- код тот же, но вызывает другую функцию: было 0x5d80c20, стало 0x5d83e80

### изменена: 0x5f34700 (436 байт) | строки: "CDOTA_Ability_Special_Bonus_MP_400"
- код тот же, но вызывает другую функцию: было 0x5d80ba0, стало 0x5d83e00

### изменена: 0x5f348c0 (436 байт) | строки: "CDOTA_Ability_Special_Bonus_MP_500"
- код тот же, но вызывает другую функцию: было 0x5d80b20, стало 0x5d83d80

### изменена: 0x5f34a80 (436 байт) | строки: "CDOTA_Ability_Special_Bonus_MP_600"
- код тот же, но вызывает другую функцию: было 0x5d80aa0, стало 0x5d83d00

### изменена: 0x5f34c40 (436 байт) | строки: "CDOTA_Ability_Special_Bonus_MP_700"
- код тот же, но вызывает другую функцию: было 0x5d80a20, стало 0x5d83c80

### изменена: 0x5f34e00 (436 байт) | строки: "CDOTA_Ability_Special_Bonus_MP_800"
- код тот же, но вызывает другую функцию: было 0x5d809a0, стало 0x5d83c00

### изменена: 0x5f34fc0 (436 байт) | строки: "CDOTA_Ability_Special_Bonus_MP_1000"
- код тот же, но вызывает другую функцию: было 0x5d80920, стало 0x5d83b80

### изменена: 0x5f36f40 (428 байт) | строки: "CDOTA_Ability_Special_Bonus_Base"
- код тот же, но вызывает другую функцию: было 0x5d82020, стало 0x5d85280

### изменена: 0x5f37b10 (436 байт) | строки: "CDOTA_Ability_Special_Bonus_Haste"
- код тот же, но вызывает другую функцию: было 0x5d7f4a0, стало 0x5d82700

### изменена: 0x5f39550 (444 байт) | строки: "CDOTA_Ability_Special_Bonus_Attack_Speed_10"
- код тот же, но вызывает другую функцию: было 0x5d80820, стало 0x5d83a80

### изменена: 0x5f39710 (444 байт) | строки: "CDOTA_Ability_Special_Bonus_Attack_Speed_15"
- код тот же, но вызывает другую функцию: было 0x5d807a0, стало 0x5d83a00

### изменена: 0x5f398d0 (444 байт) | строки: "CDOTA_Ability_Special_Bonus_Attack_Speed_20"
- код тот же, но вызывает другую функцию: было 0x5d80720, стало 0x5d83980

### изменена: 0x5f39a90 (444 байт) | строки: "CDOTA_Ability_Special_Bonus_Attack_Speed_25"
- код тот же, но вызывает другую функцию: было 0x5d806a0, стало 0x5d83900

### изменена: 0x5f39c50 (444 байт) | строки: "CDOTA_Ability_Special_Bonus_Attack_Speed_30"
- код тот же, но вызывает другую функцию: было 0x5d80620, стало 0x5d83880

### изменена: 0x5f39e10 (444 байт) | строки: "CDOTA_Ability_Special_Bonus_Attack_Speed_35"
- код тот же, но вызывает другую функцию: было 0x5d805a0, стало 0x5d83800

### изменена: 0x5f39fd0 (444 байт) | строки: "CDOTA_Ability_Special_Bonus_Attack_Speed_40"
- код тот же, но вызывает другую функцию: было 0x5d80520, стало 0x5d83780

### изменена: 0x5f3a190 (444 байт) | строки: "CDOTA_Ability_Special_Bonus_Attack_Speed_45"
- код тот же, но вызывает другую функцию: было 0x5d804a0, стало 0x5d83700

### изменена: 0x5f3a350 (444 байт) | строки: "CDOTA_Ability_Special_Bonus_Attack_Speed_50"
- код тот же, но вызывает другую функцию: было 0x5d80420, стало 0x5d83680

### изменена: 0x5f3a510 (444 байт) | строки: "CDOTA_Ability_Special_Bonus_Attack_Speed_55"
- код тот же, но вызывает другую функцию: было 0x5d803a0, стало 0x5d83600

### изменена: 0x5f3a6d0 (444 байт) | строки: "CDOTA_Ability_Special_Bonus_Attack_Speed_60"
- код тот же, но вызывает другую функцию: было 0x5d80320, стало 0x5d83580

### изменена: 0x5f3a890 (444 байт) | строки: "CDOTA_Ability_Special_Bonus_Attack_Speed_70"
- код тот же, но вызывает другую функцию: было 0x5d802a0, стало 0x5d83500

### изменена: 0x5f3aa50 (444 байт) | строки: "CDOTA_Ability_Special_Bonus_Attack_Speed_80"
- код тот же, но вызывает другую функцию: было 0x5d80220, стало 0x5d83480

### изменена: 0x5f3ac10 (444 байт) | строки: "CDOTA_Ability_Special_Bonus_Attack_Speed_90"
- код тот же, но вызывает другую функцию: было 0x5d801a0, стало 0x5d83400

### изменена: 0x5f3add0 (444 байт) | строки: "CDOTA_Ability_Special_Bonus_Cleave_100"
- код тот же, но вызывает другую функцию: было 0x5d7f720, стало 0x5d82980

### изменена: 0x5f3af90 (444 байт) | строки: "CDOTA_Ability_Special_Bonus_Cleave_130"
- код тот же, но вызывает другую функцию: было 0x5d7f6a0, стало 0x5d82900

### изменена: 0x5f3b150 (444 байт) | строки: "CDOTA_Ability_Special_Bonus_Cleave_140"
- код тот же, но вызывает другую функцию: было 0x5d7f620, стало 0x5d82880

### изменена: 0x5f3b310 (444 байт) | строки: "CDOTA_Ability_Special_Bonus_Cleave_150"
- код тот же, но вызывает другую функцию: было 0x5d7f5a0, стало 0x5d82800

### изменена: 0x5f3b4d0 (444 байт) | строки: "CDOTA_Ability_Special_Bonus_Cleave_175"
- код тот же, но вызывает другую функцию: было 0x5d7f520, стало 0x5d82780

### изменена: 0x5f3b690 (444 байт) | строки: "CDOTA_Ability_Special_Bonus_TrueStrike"
- код тот же, но вызывает другую функцию: было 0x5d7f420, стало 0x5d82680

### изменена: 0x5f3b850 (444 байт) | строки: "CDOTA_Ability_Special_Bonus_Spell_Block_15"
- код тот же, но вызывает другую функцию: было 0x5d7f220, стало 0x5d82480

### изменена: 0x5f3ba10 (444 байт) | строки: "CDOTA_Ability_Special_Bonus_Spell_Block_18"
- код тот же, но вызывает другую функцию: было 0x5d7f1a0, стало 0x5d82400

### изменена: 0x5f3bbd0 (444 байт) | строки: "CDOTA_Ability_Special_Bonus_Spell_Block_20"
- код тот же, но вызывает другую функцию: было 0x5d7f120, стало 0x5d82380

### изменена: 0x5f3bd90 (444 байт) | строки: "CDOTA_Ability_Special_Bonus_Spell_Immunity"
- код тот же, но вызывает другую функцию: было 0x5d7ee20, стало 0x5d82080

### изменена: 0x5f3bf50 (444 байт) | строки: "CDOTA_Ability_Special_Bonus_HP_Regen_3"
- код тот же, но вызывает другую функцию: было 0x5d7eda0, стало 0x5d82000

### изменена: 0x5f3c110 (444 байт) | строки: "CDOTA_Ability_Special_Bonus_HP_Regen_4"
- код тот же, но вызывает другую функцию: было 0x5d7ed20, стало 0x5d81f80

### изменена: 0x5f4dc90 (436 байт) | строки: "CDOTA_Ability_Special_Bonus_Gold_lvl15_r"
- код тот же, но вызывает другую функцию: было 0x5d81f20, стало 0x5d85180

### изменена: 0x5f4de50 (436 байт) | строки: "CDOTA_Ability_Special_Bonus_Gold_lvl20_r"
- код тот же, но вызывает другую функцию: было 0x5d81ea0, стало 0x5d85100

### изменена: 0x5f4e010 (436 байт) | строки: "CDOTA_Ability_Special_Bonus_Gold_lvl25_r"
- код тот же, но вызывает другую функцию: было 0x5d81e20, стало 0x5d85080

### изменена: 0x5f4e1d0 (436 байт) | строки: "CDOTA_Ability_Special_Bonus_Gold_lvl10_l"
- код тот же, но вызывает другую функцию: было 0x5d81da0, стало 0x5d85000

### изменена: 0x5f4e390 (436 байт) | строки: "CDOTA_Ability_Special_Bonus_Gold_lvl15_l"
- код тот же, но вызывает другую функцию: было 0x5d81d20, стало 0x5d84f80

### изменена: 0x5f4e550 (436 байт) | строки: "CDOTA_Ability_Special_Bonus_Gold_lvl20_l"
- код тот же, но вызывает другую функцию: было 0x5d81ca0, стало 0x5d84f00

### изменена: 0x5f4e710 (436 байт) | строки: "CDOTA_Ability_Special_Bonus_Gold_lvl25_l"
- код тот же, но вызывает другую функцию: было 0x5d81c20, стало 0x5d84e80

### изменена: 0x5f4e8d0 (436 байт) | строки: "CDOTA_Ability_Special_Bonus_Corruption_3"
- код тот же, но вызывает другую функцию: было 0x5d7fc20, стало 0x5d82e80

### изменена: 0x5f4ea90 (436 байт) | строки: "CDOTA_Ability_Special_Bonus_Corruption_4"
- код тот же, но вызывает другую функцию: было 0x5d7fba0, стало 0x5d82e00

### изменена: 0x5f4ec50 (436 байт) | строки: "CDOTA_Ability_Special_Bonus_Corruption_5"
- код тот же, но вызывает другую функцию: было 0x5d7fb20, стало 0x5d82d80

### изменена: 0x5f56c10 (444 байт) | строки: "CDOTA_Ability_Special_Bonus_Undefined"
- код тот же, но вызывает другую функцию: было 0x5d81fa0, стало 0x5d85200

### изменена: 0x5f56dd0 (444 байт) | строки: "CDOTA_Ability_Special_Bonus_Corruption_25"
- код тот же, но вызывает другую функцию: было 0x5d7fca0, стало 0x5d82f00

### изменена: 0x5f56f90 (444 байт) | строки: "CDOTA_Ability_Special_Bonus_Cleave_15"
- код тот же, но вызывает другую функцию: было 0x5d7faa0, стало 0x5d82d00

### изменена: 0x5f57150 (444 байт) | строки: "CDOTA_Ability_Special_Bonus_Cleave_20"
- код тот же, но вызывает другую функцию: было 0x5d7fa20, стало 0x5d82c80

### изменена: 0x5f57310 (444 байт) | строки: "CDOTA_Ability_Special_Bonus_Cleave_25"
- код тот же, но вызывает другую функцию: было 0x5d7f9a0, стало 0x5d82c00

### изменена: 0x5f574d0 (444 байт) | строки: "CDOTA_Ability_Special_Bonus_Cleave_30"
- код тот же, но вызывает другую функцию: было 0x5d7f920, стало 0x5d82b80

### изменена: 0x5f57690 (444 байт) | строки: "CDOTA_Ability_Special_Bonus_Cleave_35"
- код тот же, но вызывает другую функцию: было 0x5d7f8a0, стало 0x5d82b00

### изменена: 0x5f57850 (444 байт) | строки: "CDOTA_Ability_Special_Bonus_Cleave_40"
- код тот же, но вызывает другую функцию: было 0x5d7f820, стало 0x5d82a80

### изменена: 0x5f57a10 (444 байт) | строки: "CDOTA_Ability_Special_Bonus_Cleave_60"
- код тот же, но вызывает другую функцию: было 0x5d7f7a0, стало 0x5d82a00

### изменена: 0x5f57bd0 (444 байт) | строки: "CDOTA_Ability_Special_Bonus_Mana_Break_15"
- код тот же, но вызывает другую функцию: было 0x5d7f0a0, стало 0x5d82300

### изменена: 0x5f57d90 (444 байт) | строки: "CDOTA_Ability_Special_Bonus_Mana_Break_20"
- код тот же, но вызывает другую функцию: было 0x5d7f020, стало 0x5d82280

### изменена: 0x5f57f50 (444 байт) | строки: "CDOTA_Ability_Special_Bonus_Mana_Break_25"
- код тот же, но вызывает другую функцию: было 0x5d7efa0, стало 0x5d82200

### изменена: 0x5f58110 (444 байт) | строки: "CDOTA_Ability_Special_Bonus_Mana_Break_35"
- код тот же, но вызывает другую функцию: было 0x5d7ef20, стало 0x5d82180

### изменена: 0x5f582d0 (444 байт) | строки: "CDOTA_Ability_Special_Bonus_Mana_Break_40"
- код тот же, но вызывает другую функцию: было 0x5d7eea0, стало 0x5d82100

### изменена: 0x5f5dde0 (460 байт) | строки: "CDOTA_Ability_Special_Bonus_Base_Attack_Rate_1"
- код тот же, но вызывает другую функцию: было 0x5d808a0, стало 0x5d83b00

### изменена: 0x5f6fdd0 (444 байт) | строки: "CDOTA_Ability_Special_Bonus_Attack_Speed_100"
- код тот же, но вызывает другую функцию: было 0x5d80120, стало 0x5d83380

### изменена: 0x5f6ff90 (444 байт) | строки: "CDOTA_Ability_Special_Bonus_Attack_Speed_110"
- код тот же, но вызывает другую функцию: было 0x5d800a0, стало 0x5d83300

### изменена: 0x5f70150 (444 байт) | строки: "CDOTA_Ability_Special_Bonus_Attack_Speed_120"
- код тот же, но вызывает другую функцию: было 0x5d80020, стало 0x5d83280

### изменена: 0x5f70310 (444 байт) | строки: "CDOTA_Ability_Special_Bonus_Attack_Speed_140"
- код тот же, но вызывает другую функцию: было 0x5d7ffa0, стало 0x5d83200

### изменена: 0x5f704d0 (444 байт) | строки: "CDOTA_Ability_Special_Bonus_Attack_Speed_160"
- код тот же, но вызывает другую функцию: было 0x5d7ff20, стало 0x5d83180

### изменена: 0x5f70690 (444 байт) | строки: "CDOTA_Ability_Special_Bonus_Attack_Speed_175"
- код тот же, но вызывает другую функцию: было 0x5d7fea0, стало 0x5d83100

### изменена: 0x5f70850 (444 байт) | строки: "CDOTA_Ability_Special_Bonus_Attack_Speed_200"
- код тот же, но вызывает другую функцию: было 0x5d7fe20, стало 0x5d83080

### изменена: 0x5f70a10 (444 байт) | строки: "CDOTA_Ability_Special_Bonus_Attack_Speed_225"
- код тот же, но вызывает другую функцию: было 0x5d7fda0, стало 0x5d83000

### изменена: 0x5f70bd0 (444 байт) | строки: "CDOTA_Ability_Special_Bonus_Attack_Speed_250"
- код тот же, но вызывает другую функцию: было 0x5d7fd20, стало 0x5d82f80

### изменена: 0x5f7a5d0 (460 байт) | строки: "CDOTA_Ability_Special_Bonus_Reincarnation_200"
- код тот же, но вызывает другую функцию: было 0x5d7f3a0, стало 0x5d82600

### изменена: 0x5f7a7a0 (460 байт) | строки: "CDOTA_Ability_Special_Bonus_Reincarnation_250"
- код тот же, но вызывает другую функцию: было 0x5d7f320, стало 0x5d82580

### изменена: 0x5f7a970 (460 байт) | строки: "CDOTA_Ability_Special_Bonus_Reincarnation_300"
- код тот же, но вызывает другую функцию: было 0x5d7f2a0, стало 0x5d82500

### изменена: 0x5d76200 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d344e0, стало 0x5d375f0

### изменена: 0x5d76280 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d344b0, стало 0x5d375c0

### изменена: 0x5d76300 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d34480, стало 0x5d37590

### изменена: 0x5d76380 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d34450, стало 0x5d37560

### изменена: 0x5d76400 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d34420, стало 0x5d37530

### изменена: 0x5d76480 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d343f0, стало 0x5d37500

### изменена: 0x5d76500 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d343c0, стало 0x5d374d0

### изменена: 0x5d76580 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d34390, стало 0x5d374a0

### изменена: 0x5d76600 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d34360, стало 0x5d37470

### изменена: 0x5d76680 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d34330, стало 0x5d37440

### изменена: 0x5d76700 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d34300, стало 0x5d37410

### изменена: 0x5d76780 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d342d0, стало 0x5d373e0

### изменена: 0x5d76800 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d342a0, стало 0x5d373b0

### изменена: 0x5d76880 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d34270, стало 0x5d37380

### изменена: 0x5d76900 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d34240, стало 0x5d37350

### изменена: 0x5d76980 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d34210, стало 0x5d37320

### изменена: 0x5d76a00 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d341e0, стало 0x5d372f0

### изменена: 0x5d76a80 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d341b0, стало 0x5d372c0

### изменена: 0x5d76b00 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d34180, стало 0x5d37290

### изменена: 0x5d76b80 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d34150, стало 0x5d37260

### изменена: 0x5d76c00 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d34120, стало 0x5d37230

### изменена: 0x5d76c80 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d340f0, стало 0x5d37200

### изменена: 0x5d76d00 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d340c0, стало 0x5d371d0

### изменена: 0x5d76d80 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d34090, стало 0x5d371a0

### изменена: 0x5d76e00 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d34060, стало 0x5d37170

### изменена: 0x5d76e80 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d34030, стало 0x5d37140

### изменена: 0x5d76f00 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d34000, стало 0x5d37110

### изменена: 0x5d76f80 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d33fd0, стало 0x5d370e0

### изменена: 0x5d77000 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d33fa0, стало 0x5d370b0

### изменена: 0x5d77080 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d33f70, стало 0x5d37080

### изменена: 0x5d77100 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d33f30, стало 0x5d37040

### изменена: 0x5d77180 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d33f00, стало 0x5d37010

### изменена: 0x5d77200 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d33ed0, стало 0x5d36fe0

### изменена: 0x5d77280 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d33ea0, стало 0x5d36fb0

### изменена: 0x5d77300 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d33e70, стало 0x5d36f80

### изменена: 0x5d77380 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d33e40, стало 0x5d36f50

### изменена: 0x5d77400 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d33e10, стало 0x5d36f20

### изменена: 0x5d77480 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d33de0, стало 0x5d36ef0

### изменена: 0x5d77500 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d33db0, стало 0x5d36ec0

### изменена: 0x5d77580 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d33d80, стало 0x5d36e90

### изменена: 0x5d77600 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d33d50, стало 0x5d36e60

### изменена: 0x5d77680 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d33d20, стало 0x5d36e30

### изменена: 0x5d77700 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d33ce0, стало 0x5d36df0

### изменена: 0x5d77780 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d33cb0, стало 0x5d36dc0

### изменена: 0x5d77800 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d33c80, стало 0x5d36d90

### изменена: 0x5d77880 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d33c50, стало 0x5d36d60

### изменена: 0x5d77900 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d33c20, стало 0x5d36d30

### изменена: 0x5d77980 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d33bf0, стало 0x5d36d00

### изменена: 0x5d77a00 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d33bc0, стало 0x5d36cd0

### изменена: 0x5d77a80 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d33b90, стало 0x5d36ca0

### изменена: 0x5d77b00 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d33b60, стало 0x5d36c70

### изменена: 0x5d77b80 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d33b20, стало 0x5d36c30

### изменена: 0x5d77c00 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d33ae0, стало 0x5d36bf0

### изменена: 0x5d77c80 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d33aa0, стало 0x5d36bb0

### изменена: 0x5d77d00 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d33a60, стало 0x5d36b70

### изменена: 0x5d77d80 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d33a20, стало 0x5d36b30

### изменена: 0x5d77e00 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d339e0, стало 0x5d36af0

### изменена: 0x5d77e80 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d339a0, стало 0x5d36ab0

### изменена: 0x5d77f00 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d33960, стало 0x5d36a70

### изменена: 0x5d77f80 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d33920, стало 0x5d36a30

### изменена: 0x5d78000 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d338e0, стало 0x5d369f0

### изменена: 0x5d78080 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d338a0, стало 0x5d369b0

### изменена: 0x5d78100 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d33860, стало 0x5d36970

### изменена: 0x5d78180 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d33820, стало 0x5d36930

### изменена: 0x5d78200 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d337e0, стало 0x5d368f0

### изменена: 0x5d78280 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d337a0, стало 0x5d368b0

### изменена: 0x5d78300 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d33760, стало 0x5d36870

### изменена: 0x5d78380 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d33720, стало 0x5d36830

### изменена: 0x5d78400 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d336e0, стало 0x5d367f0

### изменена: 0x5d78480 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d336a0, стало 0x5d367b0

### изменена: 0x5d78500 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d33660, стало 0x5d36770

### изменена: 0x5d78580 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d33620, стало 0x5d36730

### изменена: 0x5d78600 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d335e0, стало 0x5d366f0

### изменена: 0x5d78680 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d335a0, стало 0x5d366b0

### изменена: 0x5d78700 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d33560, стало 0x5d36670

### изменена: 0x5d78780 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d33520, стало 0x5d36630

### изменена: 0x5d78800 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d334e0, стало 0x5d365f0

### изменена: 0x5d78880 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d334a0, стало 0x5d365b0

### изменена: 0x5d78900 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d33460, стало 0x5d36570

### изменена: 0x5d78980 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d33420, стало 0x5d36530

### изменена: 0x5d78a00 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d333e0, стало 0x5d364f0

### изменена: 0x5d78a80 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d333a0, стало 0x5d364b0

### изменена: 0x5d78b00 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d33360, стало 0x5d36470

### изменена: 0x5d78b80 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d33320, стало 0x5d36430

### изменена: 0x5d78c00 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d332e0, стало 0x5d363f0

### изменена: 0x5d78c80 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d332a0, стало 0x5d363b0

### изменена: 0x5d78d00 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d33260, стало 0x5d36370

### изменена: 0x5d78d80 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d33220, стало 0x5d36330

### изменена: 0x5d78e00 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d331e0, стало 0x5d362f0

### изменена: 0x5d78e80 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d331a0, стало 0x5d362b0

### изменена: 0x5d78f00 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d33160, стало 0x5d36270

### изменена: 0x5d78f80 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d33120, стало 0x5d36230

### изменена: 0x5d79000 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d330e0, стало 0x5d361f0

### изменена: 0x5d79080 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d330a0, стало 0x5d361b0

### изменена: 0x5d79100 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d33060, стало 0x5d36170

### изменена: 0x5d79180 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d33020, стало 0x5d36130

### изменена: 0x5d79200 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d32fe0, стало 0x5d360f0

### изменена: 0x5d79280 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d32fa0, стало 0x5d360b0

### изменена: 0x5d79300 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d32f60, стало 0x5d36070

### изменена: 0x5d79380 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d32f20, стало 0x5d36030

### изменена: 0x5d79400 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d32ee0, стало 0x5d35ff0

### изменена: 0x5d79480 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d32ea0, стало 0x5d35fb0

### изменена: 0x5d79500 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d32e60, стало 0x5d35f70

### изменена: 0x5d79580 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d32e20, стало 0x5d35f30

### изменена: 0x5d79600 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d32de0, стало 0x5d35ef0

### изменена: 0x5d79680 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d32da0, стало 0x5d35eb0

### изменена: 0x5d79700 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d32d60, стало 0x5d35e70

### изменена: 0x5d79780 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d32d20, стало 0x5d35e30

### изменена: 0x5d79800 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d32ce0, стало 0x5d35df0

### изменена: 0x5d79880 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d32ca0, стало 0x5d35db0

### изменена: 0x5d79900 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d32c60, стало 0x5d35d70

### изменена: 0x5d79980 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d32c20, стало 0x5d35d30

### изменена: 0x5d79a00 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d32be0, стало 0x5d35cf0

### изменена: 0x5d79a80 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d32ba0, стало 0x5d35cb0

### изменена: 0x5d79b00 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d32b60, стало 0x5d35c70

### изменена: 0x5d79b80 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d32b20, стало 0x5d35c30

### изменена: 0x5d79c00 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d32ae0, стало 0x5d35bf0

### изменена: 0x5d79c80 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d32aa0, стало 0x5d35bb0

### изменена: 0x5d79d00 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d32a60, стало 0x5d35b70

### изменена: 0x5d79d80 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d32a20, стало 0x5d35b30

### изменена: 0x5d79e00 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d329e0, стало 0x5d35af0

### изменена: 0x5d79e80 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d329a0, стало 0x5d35ab0

### изменена: 0x5d79f00 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d32960, стало 0x5d35a70

### изменена: 0x5d79f80 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d32920, стало 0x5d35a30

### изменена: 0x5d7a000 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d328e0, стало 0x5d359f0

### изменена: 0x5d7a080 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d328a0, стало 0x5d359b0

### изменена: 0x5d7a100 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d32860, стало 0x5d35970

### изменена: 0x5d7a180 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d32820, стало 0x5d35930

### изменена: 0x5d7a200 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d327e0, стало 0x5d358f0

### изменена: 0x5d7a280 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d327a0, стало 0x5d358b0

### изменена: 0x5d7a300 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d32760, стало 0x5d35870

### изменена: 0x5d7a380 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d32720, стало 0x5d35830

### изменена: 0x5d7a400 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d326e0, стало 0x5d357f0

### изменена: 0x5d7a480 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d326a0, стало 0x5d357b0

### изменена: 0x5d7a500 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d32660, стало 0x5d35770

### изменена: 0x5d7a580 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d32620, стало 0x5d35730

### изменена: 0x5d7a600 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d325e0, стало 0x5d356f0

### изменена: 0x5d7a680 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d325a0, стало 0x5d356b0

### изменена: 0x5d7a700 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d32560, стало 0x5d35670

### изменена: 0x5d7a780 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d32520, стало 0x5d35630

### изменена: 0x5d7a800 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d324e0, стало 0x5d355f0

### изменена: 0x5d7a880 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d324a0, стало 0x5d355b0

### изменена: 0x5d7a900 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d32460, стало 0x5d35570

### изменена: 0x5d7a980 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d32420, стало 0x5d35530

### изменена: 0x5d7aa00 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d323e0, стало 0x5d354f0

### изменена: 0x5d7aa80 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d323a0, стало 0x5d354b0

### изменена: 0x5d7ab00 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d32360, стало 0x5d35470

### изменена: 0x5d7ab80 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d32320, стало 0x5d35430

### изменена: 0x5d7ac00 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d322e0, стало 0x5d353f0

### изменена: 0x5d7ac80 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d322a0, стало 0x5d353b0

### изменена: 0x5d7ad00 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d32260, стало 0x5d35370

### изменена: 0x5d7ad80 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d32220, стало 0x5d35330

### изменена: 0x5d7ae00 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d321e0, стало 0x5d352f0

### изменена: 0x5d7ae80 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d321a0, стало 0x5d352b0

### изменена: 0x5d7af00 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d32160, стало 0x5d35270

### изменена: 0x5d7af80 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d32120, стало 0x5d35230

### изменена: 0x5d7b000 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d320e0, стало 0x5d351f0

### изменена: 0x5d7b080 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d320a0, стало 0x5d351b0

### изменена: 0x5d7b100 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d32060, стало 0x5d35170

### изменена: 0x5d7b180 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d32020, стало 0x5d35130

### изменена: 0x5d7b200 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d31fe0, стало 0x5d350f0

### изменена: 0x5d7b280 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d31fa0, стало 0x5d350b0

### изменена: 0x5d7b300 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d31f60, стало 0x5d35070

### изменена: 0x5d7b380 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d31f20, стало 0x5d35030

### изменена: 0x5d7b400 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d31ee0, стало 0x5d34ff0

### изменена: 0x5d7b480 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d31ea0, стало 0x5d34fb0

### изменена: 0x5d7b500 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d31e60, стало 0x5d34f70

### изменена: 0x5d7b580 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d31e20, стало 0x5d34f30

### изменена: 0x5d7b600 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d31de0, стало 0x5d34ef0

### изменена: 0x5d7b680 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d31da0, стало 0x5d34eb0

### изменена: 0x5d7b700 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d31d60, стало 0x5d34e70

### изменена: 0x5d7b780 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d31d20, стало 0x5d34e30

### изменена: 0x5d7b800 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d31ce0, стало 0x5d34df0

### изменена: 0x5d7b880 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d31ca0, стало 0x5d34db0

### изменена: 0x5d7b900 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d31c60, стало 0x5d34d70

### изменена: 0x5d7b980 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d31c20, стало 0x5d34d30

### изменена: 0x5d7ba00 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d31be0, стало 0x5d34cf0

### изменена: 0x5d7ba80 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d31ba0, стало 0x5d34cb0

### изменена: 0x5d7bb00 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d31b60, стало 0x5d34c70

### изменена: 0x5d7bb80 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d31b20, стало 0x5d34c30

### изменена: 0x5d7bc00 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d31ae0, стало 0x5d34bf0

### изменена: 0x5d7bc80 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d31aa0, стало 0x5d34bb0

### изменена: 0x5d7bd00 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d31a60, стало 0x5d34b70

### изменена: 0x5d7bd80 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d31a20, стало 0x5d34b30

### изменена: 0x5d7be00 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d319e0, стало 0x5d34af0

### изменена: 0x5d7be80 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d319a0, стало 0x5d34ab0

### изменена: 0x5d7bf00 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d31960, стало 0x5d34a70

### изменена: 0x5d7bf80 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d31920, стало 0x5d34a30

### изменена: 0x5d7c000 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d318e0, стало 0x5d349f0

### изменена: 0x5d7c080 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d318a0, стало 0x5d349b0

### изменена: 0x5d7c100 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d31860, стало 0x5d34970

### изменена: 0x5d7c180 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d31820, стало 0x5d34930

### изменена: 0x5d7c200 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d317e0, стало 0x5d348f0

### изменена: 0x5d7c280 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d317a0, стало 0x5d348b0

### изменена: 0x5d7c300 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d31760, стало 0x5d34870

### изменена: 0x5d7c380 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d31720, стало 0x5d34830

### изменена: 0x5d7c400 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d316e0, стало 0x5d347f0

### изменена: 0x5d7c480 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d316a0, стало 0x5d347b0

### изменена: 0x5d7c500 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d31660, стало 0x5d34770

### изменена: 0x5d7c580 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d31620, стало 0x5d34730

### изменена: 0x5d7c600 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d315e0, стало 0x5d346f0

### изменена: 0x5d7c680 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d315a0, стало 0x5d346b0

### изменена: 0x5d7c700 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d31560, стало 0x5d34670

### изменена: 0x5d7c780 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d31520, стало 0x5d34630

### изменена: 0x5d7c800 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d314e0, стало 0x5d345f0

### изменена: 0x5d7c880 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d314a0, стало 0x5d345b0

### изменена: 0x5d7c900 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d31460, стало 0x5d34570

### изменена: 0x5d7c980 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d31420, стало 0x5d34530

### изменена: 0x5d7ca00 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d313e0, стало 0x5d344f0

### изменена: 0x5d7ca80 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d313a0, стало 0x5d344b0

### изменена: 0x5d7cb00 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d31360, стало 0x5d34470

### изменена: 0x5d7cb80 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d31320, стало 0x5d34430

### изменена: 0x5d7cc00 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d312e0, стало 0x5d343f0

### изменена: 0x5d7cc80 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d312a0, стало 0x5d343b0

### изменена: 0x5d7cd00 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d31260, стало 0x5d34370

### изменена: 0x5d7cd80 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d31220, стало 0x5d34330

### изменена: 0x5d7ce00 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d311e0, стало 0x5d342f0

### изменена: 0x5d7ce80 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d311a0, стало 0x5d342b0

### изменена: 0x5d7cf00 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d31160, стало 0x5d34270

### изменена: 0x5d7cf80 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d31120, стало 0x5d34230

### изменена: 0x5d7d000 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d310e0, стало 0x5d341f0

### изменена: 0x5d7d080 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d310a0, стало 0x5d341b0

### изменена: 0x5d7d100 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d31060, стало 0x5d34170

### изменена: 0x5d7d180 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d31020, стало 0x5d34130

### изменена: 0x5d7d200 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d30fe0, стало 0x5d340f0

### изменена: 0x5d7d280 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d30fa0, стало 0x5d340b0

### изменена: 0x5d7d300 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d30f60, стало 0x5d34070

### изменена: 0x5d7d380 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d30f20, стало 0x5d34030

### изменена: 0x5d7d400 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d30ee0, стало 0x5d33ff0

### изменена: 0x5d7d480 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d30ea0, стало 0x5d33fb0

### изменена: 0x5d7d500 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d30e60, стало 0x5d33f70

### изменена: 0x5d7d580 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d30e20, стало 0x5d33f30

### изменена: 0x5d7d600 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d30de0, стало 0x5d33ef0

### изменена: 0x5d7d680 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d30da0, стало 0x5d33eb0

### изменена: 0x5d7d700 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d30d60, стало 0x5d33e70

### изменена: 0x5d7d780 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d30d20, стало 0x5d33e30

### изменена: 0x5d7d800 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d30ce0, стало 0x5d33df0

### изменена: 0x5d7d880 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d30ca0, стало 0x5d33db0

### изменена: 0x5d7d900 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d30c60, стало 0x5d33d70

### изменена: 0x5d7d980 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d30c20, стало 0x5d33d30

### изменена: 0x5d7da00 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d30be0, стало 0x5d33cf0

### изменена: 0x5d7da80 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d30ba0, стало 0x5d33cb0

### изменена: 0x5d7db00 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d30b60, стало 0x5d33c70

### изменена: 0x5d7db80 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d30b20, стало 0x5d33c30

### изменена: 0x5d7dc00 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d30ae0, стало 0x5d33bf0

### изменена: 0x5d7dc80 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d30aa0, стало 0x5d33bb0

### изменена: 0x5d7dd00 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d30a60, стало 0x5d33b70

### изменена: 0x5d7dd80 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d30a20, стало 0x5d33b30

### изменена: 0x5d7de00 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d309e0, стало 0x5d33af0

### изменена: 0x5d7de80 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d309a0, стало 0x5d33ab0

### изменена: 0x5d7df00 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d30960, стало 0x5d33a70

### изменена: 0x5d7df80 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d30920, стало 0x5d33a30

### изменена: 0x5d7e000 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d308e0, стало 0x5d339f0

### изменена: 0x5d7e080 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d308a0, стало 0x5d339b0

### изменена: 0x5d7e100 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d30860, стало 0x5d33970

### изменена: 0x5d7e180 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d30820, стало 0x5d33930

### изменена: 0x5d7e200 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d307e0, стало 0x5d338f0

### изменена: 0x5d7e280 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d307a0, стало 0x5d338b0

### изменена: 0x5d7e300 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d30760, стало 0x5d33870

### изменена: 0x5d7e380 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d30740, стало 0x5d33850

### изменена: 0x5d7e400 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d30720, стало 0x5d33830

### изменена: 0x5d7e480 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d30700, стало 0x5d33810

### изменена: 0x5d7e500 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d306e0, стало 0x5d337f0

### изменена: 0x5d7e580 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d306c0, стало 0x5d337d0

### изменена: 0x5d7e600 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d306a0, стало 0x5d337b0

### изменена: 0x5d7e680 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d30680, стало 0x5d33790

### изменена: 0x5d7e700 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d30660, стало 0x5d33770

### изменена: 0x5d7e780 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d30640, стало 0x5d33750

### изменена: 0x5d7e800 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d30620, стало 0x5d33730

### изменена: 0x5d7e880 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d30600, стало 0x5d33710

### изменена: 0x5d7e900 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d305e0, стало 0x5d336f0

### изменена: 0x5d7e980 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d305c0, стало 0x5d336d0

### изменена: 0x5d7ea00 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d305a0, стало 0x5d336b0

### изменена: 0x5d7ea80 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d30580, стало 0x5d33690

### изменена: 0x5d7eb00 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d30560, стало 0x5d33670

### изменена: 0x5d7eb80 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d30540, стало 0x5d33650

### изменена: 0x5d7ec00 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d30520, стало 0x5d33630

### изменена: 0x5d7ec80 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d30500, стало 0x5d33610

### изменена: 0x5d7ed00 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d304e0, стало 0x5d335f0

### изменена: 0x5d7ed80 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d304c0, стало 0x5d335d0

### изменена: 0x5d7ee00 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d304a0, стало 0x5d335b0

### изменена: 0x5d7ee80 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d30480, стало 0x5d33590

### изменена: 0x5d7ef00 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d30460, стало 0x5d33570

### изменена: 0x5d7ef80 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d30440, стало 0x5d33550

### изменена: 0x5d7f000 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d30420, стало 0x5d33530

### изменена: 0x5d7f080 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d30400, стало 0x5d33510

### изменена: 0x5d7f100 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d303e0, стало 0x5d334f0

### изменена: 0x5d7f180 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d303c0, стало 0x5d334d0

### изменена: 0x5d7f200 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d303a0, стало 0x5d334b0

### изменена: 0x5d7f280 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d30380, стало 0x5d33490

### изменена: 0x5d7f300 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d30360, стало 0x5d33470

### изменена: 0x5d7f380 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d30340, стало 0x5d33450

### изменена: 0x5d7f400 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d30320, стало 0x5d33430

### изменена: 0x5d7f480 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d30300, стало 0x5d33410

### изменена: 0x5d7f500 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d302e0, стало 0x5d333f0

### изменена: 0x5d7f580 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d302c0, стало 0x5d333d0

### изменена: 0x5d7f600 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d302a0, стало 0x5d333b0

### изменена: 0x5d7f680 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d30280, стало 0x5d33390

### изменена: 0x5d7f700 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d30260, стало 0x5d33370

### изменена: 0x5d7f780 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d30240, стало 0x5d33350

### изменена: 0x5d7f800 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d30220, стало 0x5d33330

### изменена: 0x5d7f880 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d30200, стало 0x5d33310

### изменена: 0x5d7f900 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d301e0, стало 0x5d332f0

### изменена: 0x5d7f980 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d301c0, стало 0x5d332d0

### изменена: 0x5d7fa00 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d301a0, стало 0x5d332b0

### изменена: 0x5d7fa80 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d30180, стало 0x5d33290

### изменена: 0x5d7fb00 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d30160, стало 0x5d33270

### изменена: 0x5d7fb80 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d30140, стало 0x5d33250

### изменена: 0x5d7fc00 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d30120, стало 0x5d33230

### изменена: 0x5d7fc80 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d30100, стало 0x5d33210

### изменена: 0x5d7fd00 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d300c0, стало 0x5d331d0

### изменена: 0x5d7fd80 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d30080, стало 0x5d33190

### изменена: 0x5d7fe00 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d30040, стало 0x5d33150

### изменена: 0x5d7fe80 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d30000, стало 0x5d33110

### изменена: 0x5d7ff00 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d2ffc0, стало 0x5d330d0

### изменена: 0x5d7ff80 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d2ff80, стало 0x5d33090

### изменена: 0x5d80000 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d2ff40, стало 0x5d33050

### изменена: 0x5d80080 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d2ff00, стало 0x5d33010

### изменена: 0x5d80100 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d2fec0, стало 0x5d32fd0

### изменена: 0x5d80180 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d2fe80, стало 0x5d32f90

### изменена: 0x5d80200 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d2fe40, стало 0x5d32f50

### изменена: 0x5d80280 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d2fe00, стало 0x5d32f10

### изменена: 0x5d80300 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d2fdc0, стало 0x5d32ed0

### изменена: 0x5d80380 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d2fd80, стало 0x5d32e90

### изменена: 0x5d80400 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d2fd40, стало 0x5d32e50

### изменена: 0x5d80480 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d2fd00, стало 0x5d32e10

### изменена: 0x5d80500 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d2fcc0, стало 0x5d32dd0

### изменена: 0x5d80580 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d2fc80, стало 0x5d32d90

### изменена: 0x5d80600 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d2fc40, стало 0x5d32d50

### изменена: 0x5d80680 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d2fc00, стало 0x5d32d10

### изменена: 0x5d80700 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d2fbc0, стало 0x5d32cd0

### изменена: 0x5d80780 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d2fb80, стало 0x5d32c90

### изменена: 0x5d80800 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d2fb40, стало 0x5d32c50

### изменена: 0x5d80880 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d2fb00, стало 0x5d32c10

### изменена: 0x5d80900 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d2fac0, стало 0x5d32bd0

### изменена: 0x5d80980 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d2fa80, стало 0x5d32b90

### изменена: 0x5d80a00 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d2fa40, стало 0x5d32b50

### изменена: 0x5d80a80 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d2fa00, стало 0x5d32b10

### изменена: 0x5d80b00 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d2f9c0, стало 0x5d32ad0

### изменена: 0x5d80b80 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d2f980, стало 0x5d32a90

### изменена: 0x5d80c00 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d2f940, стало 0x5d32a50

### изменена: 0x5d80c80 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d2f900, стало 0x5d32a10

### изменена: 0x5d80d00 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d2f8c0, стало 0x5d329d0

### изменена: 0x5d80d80 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d2f880, стало 0x5d32990

### изменена: 0x5d80e00 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d2f840, стало 0x5d32950

### изменена: 0x5d80e80 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d2f800, стало 0x5d32910

### изменена: 0x5d80f00 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d2f7c0, стало 0x5d328d0

### изменена: 0x5d80f80 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d2f780, стало 0x5d32890

### изменена: 0x5d81000 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d2f740, стало 0x5d32850

### изменена: 0x5d81080 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d2f700, стало 0x5d32810

### изменена: 0x5d81100 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d2f6c0, стало 0x5d327d0

### изменена: 0x5d81180 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d2f680, стало 0x5d32790

### изменена: 0x5d81200 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d2f640, стало 0x5d32750

### изменена: 0x5d81280 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d2f600, стало 0x5d32710

### изменена: 0x5d81300 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d2f5c0, стало 0x5d326d0

### изменена: 0x5d81380 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d2f580, стало 0x5d32690

### изменена: 0x5d81400 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d2f540, стало 0x5d32650

### изменена: 0x5d81480 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d2f500, стало 0x5d32610

### изменена: 0x5d81500 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d2f4c0, стало 0x5d325d0

### изменена: 0x5d81580 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d2f480, стало 0x5d32590

### изменена: 0x5d81600 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d2f440, стало 0x5d32550

### изменена: 0x5d81680 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d2f400, стало 0x5d32510

### изменена: 0x5d81700 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d2f3c0, стало 0x5d324d0

### изменена: 0x5d81780 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d2f380, стало 0x5d32490

### изменена: 0x5d81800 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d2f340, стало 0x5d32450

### изменена: 0x5d81880 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d2f300, стало 0x5d32410

### изменена: 0x5d81900 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d2f2c0, стало 0x5d323d0

### изменена: 0x5d81980 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d2f280, стало 0x5d32390

### изменена: 0x5d81a00 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d2f240, стало 0x5d32350

### изменена: 0x5d81a80 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d2f200, стало 0x5d32310

### изменена: 0x5d81b00 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d2f1c0, стало 0x5d322d0

### изменена: 0x5d81b80 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d2f180, стало 0x5d32290

### изменена: 0x5d81c00 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d2f140, стало 0x5d32250

### изменена: 0x5d81c80 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d2f100, стало 0x5d32210

### изменена: 0x5d81d00 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d2f0c0, стало 0x5d321d0

### изменена: 0x5d81d80 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d2f080, стало 0x5d32190

### изменена: 0x5d81e00 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d2f040, стало 0x5d32150

### изменена: 0x5d81e80 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d2f000, стало 0x5d32110

### изменена: 0x5d81f00 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d2efc0, стало 0x5d320d0

### изменена: 0x5d81f80 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d2ef80, стало 0x5d32090

### изменена: 0x5d82000 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d2ef40, стало 0x5d32050

### изменена: 0x5d82080 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d2ef00, стало 0x5d32010

### изменена: 0x5d82100 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d2eec0, стало 0x5d31fd0

### изменена: 0x5d82180 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d2ee80, стало 0x5d31f90

### изменена: 0x5d82200 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d2ee40, стало 0x5d31f50

### изменена: 0x5d82280 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d2ee00, стало 0x5d31f10

### изменена: 0x5d82300 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d2edc0, стало 0x5d31ed0

### изменена: 0x5d82380 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d2ed80, стало 0x5d31e90

### изменена: 0x5d82400 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d2ed40, стало 0x5d31e50

### изменена: 0x5d82480 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d2ed00, стало 0x5d31e10

### изменена: 0x5d82500 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d2ecc0, стало 0x5d31dd0

### изменена: 0x5d82580 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d2ec80, стало 0x5d31d90

### изменена: 0x5d82600 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d2ec40, стало 0x5d31d50

### изменена: 0x5d82680 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d2ec00, стало 0x5d31d10

### изменена: 0x5d82700 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d2ebc0, стало 0x5d31cd0

### изменена: 0x5d82780 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d2eb80, стало 0x5d31c90

### изменена: 0x5d82800 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d2eb40, стало 0x5d31c40

### изменена: 0x5d82880 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d2eb00, стало 0x5d31c00

### изменена: 0x5d82900 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d2eac0, стало 0x5d31bc0

### изменена: 0x5d82980 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d2ea80, стало 0x5d31b80

### изменена: 0x5d82a00 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d2ea40, стало 0x5d31b40

### изменена: 0x5d82a80 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d2ea00, стало 0x5d31b00

### изменена: 0x5d82b00 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d2e9c0, стало 0x5d31ac0

### изменена: 0x5d82b80 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d2e980, стало 0x5d31a80

### изменена: 0x5d82c00 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d2e940, стало 0x5d31a40

### изменена: 0x5d82c80 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d2e900, стало 0x5d31a00

### изменена: 0x5d82d00 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d2e8c0, стало 0x5d319c0

### изменена: 0x5d82d80 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d2e880, стало 0x5d31980

### изменена: 0x5d82e00 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d2e840, стало 0x5d31940

### изменена: 0x5d82e80 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d2e800, стало 0x5d31900

### изменена: 0x5d82f00 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d2e7c0, стало 0x5d318c0

### изменена: 0x5d82f80 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d2e780, стало 0x5d31880

### изменена: 0x5d83000 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d2e740, стало 0x5d31840

### изменена: 0x5d83080 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d2e700, стало 0x5d31800

### изменена: 0x5d83100 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d2e6c0, стало 0x5d317c0

### изменена: 0x5d83180 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d2e680, стало 0x5d31780

### изменена: 0x5d83200 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d2e640, стало 0x5d31740

### изменена: 0x5d83280 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d2e600, стало 0x5d31700

### изменена: 0x5d83300 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d2e5c0, стало 0x5d316c0

### изменена: 0x5d83380 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d2e580, стало 0x5d31680

### изменена: 0x5d83400 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d2e540, стало 0x5d31640

### изменена: 0x5d83480 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d2e500, стало 0x5d31600

### изменена: 0x5d83500 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d2e4c0, стало 0x5d315c0

### изменена: 0x5d83580 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d2e480, стало 0x5d31580

### изменена: 0x5d83600 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d2e440, стало 0x5d31540

### изменена: 0x5d83680 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d2e400, стало 0x5d31500

### изменена: 0x5d83700 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d2e3c0, стало 0x5d314c0

### изменена: 0x5d83780 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d2e380, стало 0x5d31480

### изменена: 0x5d83800 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d2e340, стало 0x5d31440

### изменена: 0x5d83880 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d2e300, стало 0x5d31400

### изменена: 0x5d83900 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d2e2c0, стало 0x5d313c0

### изменена: 0x5d83980 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d2e280, стало 0x5d31380

### изменена: 0x5d83a00 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d2e240, стало 0x5d31340

### изменена: 0x5d83a80 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d2e200, стало 0x5d31300

### изменена: 0x5d83b00 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d2e1c0, стало 0x5d312c0

### изменена: 0x5d83b80 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d2e180, стало 0x5d31280

### изменена: 0x5d83c00 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d2e140, стало 0x5d31240

### изменена: 0x5d83c80 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d2e100, стало 0x5d31200

### изменена: 0x5d83d00 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d2e0c0, стало 0x5d311c0

### изменена: 0x5d83d80 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d2e080, стало 0x5d31180

### изменена: 0x5d83e00 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d2e040, стало 0x5d31140

### изменена: 0x5d83e80 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d2e000, стало 0x5d31100

### изменена: 0x5d83f00 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d2dfc0, стало 0x5d310c0

### изменена: 0x5d83f80 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d2df80, стало 0x5d31080

### изменена: 0x5d84000 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d2df40, стало 0x5d31040

### изменена: 0x5d84080 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d2df00, стало 0x5d31000

### изменена: 0x5d84100 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d2dec0, стало 0x5d30fc0

### изменена: 0x5d84180 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d2de80, стало 0x5d30f80

### изменена: 0x5d84200 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d2de40, стало 0x5d30f40

### изменена: 0x5d84280 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d2de00, стало 0x5d30f00

### изменена: 0x5d84300 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d2ddc0, стало 0x5d30ec0

### изменена: 0x5d84380 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d2dd80, стало 0x5d30e80

### изменена: 0x5d84400 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d2dd40, стало 0x5d30e40

### изменена: 0x5d84480 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d2dd00, стало 0x5d30e00

### изменена: 0x5d84500 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d2dcc0, стало 0x5d30dc0

### изменена: 0x5d84580 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d2dc80, стало 0x5d30d80

### изменена: 0x5d84600 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d2dc40, стало 0x5d30d40

### изменена: 0x5d84680 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d2dc00, стало 0x5d30d00

### изменена: 0x5d84700 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d2dbc0, стало 0x5d30cc0

### изменена: 0x5d84780 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d2db80, стало 0x5d30c80

### изменена: 0x5d84800 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d2db40, стало 0x5d30c40

### изменена: 0x5d84880 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d2db00, стало 0x5d30c00

### изменена: 0x5d84900 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d2dac0, стало 0x5d30bc0

### изменена: 0x5d84980 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d2da80, стало 0x5d30b80

### изменена: 0x5d84a00 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d2da40, стало 0x5d30b40

### изменена: 0x5d84a80 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d2da00, стало 0x5d30b00

### изменена: 0x5d84b00 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d2d9c0, стало 0x5d30ac0

### изменена: 0x5d84b80 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d2d980, стало 0x5d30a80

### изменена: 0x5d84c00 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d2d940, стало 0x5d30a40

### изменена: 0x5d84c80 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d2d900, стало 0x5d30a00

### изменена: 0x5d84d00 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d2d8c0, стало 0x5d309c0

### изменена: 0x5d84d80 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d2d880, стало 0x5d30980

### изменена: 0x5d84e00 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d2d860, стало 0x5d30940

### изменена: 0x5d84e80 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d2d840, стало 0x5d30920

### изменена: 0x5d84f00 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d2d820, стало 0x5d30900

### изменена: 0x5d84f80 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d2d800, стало 0x5d308e0

### изменена: 0x5d85000 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d2d7e0, стало 0x5d308c0

### изменена: 0x5d85080 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d2d7c0, стало 0x5d308a0

### изменена: 0x5d85100 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d2d7a0, стало 0x5d30880

### изменена: 0x5d85180 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d2d730, стало 0x5d30860

### изменена: 0x5d85200 (126 байт)
- код тот же, но вызывает другую функцию: было 0x5d2d700, стало 0x5d307f0

### изменена: 0x5d8ebb0 (5 байт)
- код тот же, но вызывает другую функцию: было 0x3e6b970, стало 0x5947bb0

### изменена: 0x5d8ebe0 (5 байт)
- код тот же, но вызывает другую функцию: было 0x5944af0, стало 0x3e6e430

### изменена: 0x5d91c30 (5 байт)
- код тот же, но вызывает другую функцию: было 0x3e6dc50, стало 0x5947be0

### изменена: 0x5d91c40 (5 байт)
- код тот же, но вызывает другую функцию: было 0x3e6dc50, стало 0x5947be0

### изменена: 0x5d91de0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3cae0, стало 0x5d3fbf0

### изменена: 0x5d91eb0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3cad0, стало 0x5d3fbe0

### изменена: 0x5d91f80 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3cac0, стало 0x5d3fbd0

### изменена: 0x5d92050 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3cab0, стало 0x5d3fbc0

### изменена: 0x5d92120 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3caa0, стало 0x5d3fbb0

### изменена: 0x5d921f0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3ca90, стало 0x5d3fba0

### изменена: 0x5d922c0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3ca80, стало 0x5d3fb90

### изменена: 0x5d92390 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3ca70, стало 0x5d3fb80

### изменена: 0x5d92460 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3ca60, стало 0x5d3fb70

### изменена: 0x5d92530 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3ca50, стало 0x5d3fb60

### изменена: 0x5d92600 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3ca40, стало 0x5d3fb50

### изменена: 0x5d926d0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3ca30, стало 0x5d3fb40

### изменена: 0x5d927a0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3ca20, стало 0x5d3fb30

### изменена: 0x5d92870 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3ca10, стало 0x5d3fb20

### изменена: 0x5d92940 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3ca00, стало 0x5d3fb10

### изменена: 0x5d92a10 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3c9f0, стало 0x5d3fb00

### изменена: 0x5d92ae0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3c9e0, стало 0x5d3faf0

### изменена: 0x5d92bb0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3c9d0, стало 0x5d3fae0

### изменена: 0x5d92c80 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3c9c0, стало 0x5d3fad0

### изменена: 0x5d92d50 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3c9b0, стало 0x5d3fac0

### изменена: 0x5d92e20 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3c9a0, стало 0x5d3fab0

### изменена: 0x5d92ef0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3c990, стало 0x5d3faa0

### изменена: 0x5d92fc0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3c980, стало 0x5d3fa90

### изменена: 0x5d93090 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3c970, стало 0x5d3fa80

### изменена: 0x5d93160 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3c960, стало 0x5d3fa70

### изменена: 0x5d93230 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3c950, стало 0x5d3fa60

### изменена: 0x5d93300 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3c940, стало 0x5d3fa50

### изменена: 0x5d933d0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3c930, стало 0x5d3fa40

### изменена: 0x5d934a0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3c920, стало 0x5d3fa30

### изменена: 0x5d93570 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3c910, стало 0x5d3fa20

### изменена: 0x5d93640 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3c900, стало 0x5d3fa10

### изменена: 0x5d93710 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3c8f0, стало 0x5d3fa00

### изменена: 0x5d937e0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3c8e0, стало 0x5d3f9f0

### изменена: 0x5d938b0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3c8d0, стало 0x5d3f9e0

### изменена: 0x5d93980 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3c8c0, стало 0x5d3f9d0

### изменена: 0x5d93a50 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3c8b0, стало 0x5d3f9c0

### изменена: 0x5d93b20 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3c8a0, стало 0x5d3f9b0

### изменена: 0x5d93bf0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3c890, стало 0x5d3f9a0

### изменена: 0x5d93cc0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3c880, стало 0x5d3f990

### изменена: 0x5d93d90 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3c870, стало 0x5d3f980

### изменена: 0x5d93e60 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3c860, стало 0x5d3f970

### изменена: 0x5d93f30 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3c850, стало 0x5d3f960

### изменена: 0x5d94000 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3c840, стало 0x5d3f950

### изменена: 0x5d940d0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3c830, стало 0x5d3f940

### изменена: 0x5d941a0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3c820, стало 0x5d3f930

### изменена: 0x5d94270 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3c810, стало 0x5d3f920

### изменена: 0x5d94340 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3c800, стало 0x5d3f910

### изменена: 0x5d94410 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3c7f0, стало 0x5d3f900

### изменена: 0x5d944e0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3c7e0, стало 0x5d3f8f0

### изменена: 0x5d945b0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3c7d0, стало 0x5d3f8e0

### изменена: 0x5d94680 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3c7c0, стало 0x5d3f8d0

### изменена: 0x5d94750 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3c7b0, стало 0x5d3f8c0

### изменена: 0x5d94820 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3c7a0, стало 0x5d3f8b0

### изменена: 0x5d948f0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3c790, стало 0x5d3f8a0

### изменена: 0x5d949c0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3c780, стало 0x5d3f890

### изменена: 0x5d94a90 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3c770, стало 0x5d3f880

### изменена: 0x5d94b60 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3c760, стало 0x5d3f870

### изменена: 0x5d94c30 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3c750, стало 0x5d3f860

### изменена: 0x5d94d00 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3c740, стало 0x5d3f850

### изменена: 0x5d94dd0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3c730, стало 0x5d3f840

### изменена: 0x5d94ea0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3c720, стало 0x5d3f830

### изменена: 0x5d94f70 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3c710, стало 0x5d3f820

### изменена: 0x5d95040 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3c700, стало 0x5d3f810

### изменена: 0x5d95110 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3c6f0, стало 0x5d3f800

### изменена: 0x5d951e0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3c6e0, стало 0x5d3f7f0

### изменена: 0x5d952b0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3c6d0, стало 0x5d3f7e0

### изменена: 0x5d95380 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3c6c0, стало 0x5d3f7d0

### изменена: 0x5d95480 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3c6b0, стало 0x5d3f7c0

### изменена: 0x5d95550 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3c6a0, стало 0x5d3f7b0

### изменена: 0x5d95620 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3c690, стало 0x5d3f7a0

### изменена: 0x5d956f0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3c680, стало 0x5d3f790

### изменена: 0x5d957c0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3c670, стало 0x5d3f780

### изменена: 0x5d95890 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3c660, стало 0x5d3f770

### изменена: 0x5d95960 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3c650, стало 0x5d3f760

### изменена: 0x5d95a30 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3c640, стало 0x5d3f750

### изменена: 0x5d95b00 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3c630, стало 0x5d3f740

### изменена: 0x5d95bd0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3c620, стало 0x5d3f730

### изменена: 0x5d95ca0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3c610, стало 0x5d3f720

### изменена: 0x5d95d70 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3c600, стало 0x5d3f710

### изменена: 0x5d95e40 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3c5f0, стало 0x5d3f700

### изменена: 0x5d95f10 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3c5e0, стало 0x5d3f6f0

### изменена: 0x5d95fe0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3c5d0, стало 0x5d3f6e0

### изменена: 0x5d960b0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3c5c0, стало 0x5d3f6d0

### изменена: 0x5d96180 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3c5b0, стало 0x5d3f6c0

### изменена: 0x5d96250 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3c5a0, стало 0x5d3f6b0

### изменена: 0x5d96320 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3c590, стало 0x5d3f6a0

### изменена: 0x5d963f0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3c580, стало 0x5d3f690

### изменена: 0x5d964c0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3c570, стало 0x5d3f680

### изменена: 0x5d96590 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3c560, стало 0x5d3f670

### изменена: 0x5d96660 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3c550, стало 0x5d3f660

### изменена: 0x5d96730 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3c540, стало 0x5d3f650

### изменена: 0x5d96800 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3c530, стало 0x5d3f640

### изменена: 0x5d968d0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3c520, стало 0x5d3f630

### изменена: 0x5d969a0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3c510, стало 0x5d3f620

### изменена: 0x5d96a70 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3c500, стало 0x5d3f610

### изменена: 0x5d96b40 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3c4f0, стало 0x5d3f600

### изменена: 0x5d96c10 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3c4e0, стало 0x5d3f5f0

### изменена: 0x5d96ce0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3c4d0, стало 0x5d3f5e0

### изменена: 0x5d96db0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3c4c0, стало 0x5d3f5d0

### изменена: 0x5d96e80 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3c4b0, стало 0x5d3f5c0

### изменена: 0x5d96f50 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3c4a0, стало 0x5d3f5b0

### изменена: 0x5d97020 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3c490, стало 0x5d3f5a0

### изменена: 0x5d970f0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3c480, стало 0x5d3f590

### изменена: 0x5d971c0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3c470, стало 0x5d3f580

### изменена: 0x5d97290 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3c460, стало 0x5d3f570

### изменена: 0x5d97360 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3c450, стало 0x5d3f560

### изменена: 0x5d97430 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3c440, стало 0x5d3f550

### изменена: 0x5d97500 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3c430, стало 0x5d3f540

### изменена: 0x5d975d0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3c420, стало 0x5d3f530

### изменена: 0x5d976a0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3c410, стало 0x5d3f520

### изменена: 0x5d97770 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3c400, стало 0x5d3f510

### изменена: 0x5d97840 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3c3f0, стало 0x5d3f500

### изменена: 0x5d97910 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3c3e0, стало 0x5d3f4f0

### изменена: 0x5d979e0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3c3d0, стало 0x5d3f4e0

### изменена: 0x5d97ab0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3c3c0, стало 0x5d3f4d0

### изменена: 0x5d97b80 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3c3b0, стало 0x5d3f4c0

### изменена: 0x5d97c50 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3c3a0, стало 0x5d3f4b0

### изменена: 0x5d97d20 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3c390, стало 0x5d3f4a0

### изменена: 0x5d97df0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3c380, стало 0x5d3f490

### изменена: 0x5d97ec0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3c370, стало 0x5d3f480

### изменена: 0x5d97f90 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3c360, стало 0x5d3f470

### изменена: 0x5d98060 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3c350, стало 0x5d3f460

### изменена: 0x5d98130 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3c340, стало 0x5d3f450

### изменена: 0x5d98200 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3c330, стало 0x5d3f440

### изменена: 0x5d982d0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3c320, стало 0x5d3f430

### изменена: 0x5d983a0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3c310, стало 0x5d3f420

### изменена: 0x5d98470 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3c300, стало 0x5d3f410

### изменена: 0x5d98540 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3c2f0, стало 0x5d3f400

### изменена: 0x5d98610 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3c2e0, стало 0x5d3f3f0

### изменена: 0x5d986e0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3c2d0, стало 0x5d3f3e0

### изменена: 0x5d987b0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3c2c0, стало 0x5d3f3d0

### изменена: 0x5d98880 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3c2b0, стало 0x5d3f3c0

### изменена: 0x5d98950 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3c2a0, стало 0x5d3f3b0

### изменена: 0x5d98a20 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3c290, стало 0x5d3f3a0

### изменена: 0x5d98af0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3c280, стало 0x5d3f390

### изменена: 0x5d98bc0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3c270, стало 0x5d3f380

### изменена: 0x5d98c90 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3c260, стало 0x5d3f370

### изменена: 0x5d98d60 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3c250, стало 0x5d3f360

### изменена: 0x5d98e30 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3c240, стало 0x5d3f350

### изменена: 0x5d98f00 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3c230, стало 0x5d3f340

### изменена: 0x5d98fd0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3c220, стало 0x5d3f330

### изменена: 0x5d990a0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3c210, стало 0x5d3f320

### изменена: 0x5d99170 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3c200, стало 0x5d3f310

### изменена: 0x5d99240 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3c1f0, стало 0x5d3f300

### изменена: 0x5d99310 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3c1e0, стало 0x5d3f2f0

### изменена: 0x5d993e0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3c1d0, стало 0x5d3f2e0

### изменена: 0x5d994b0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3c1c0, стало 0x5d3f2d0

### изменена: 0x5d99580 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3c1b0, стало 0x5d3f2c0

### изменена: 0x5d99650 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3c1a0, стало 0x5d3f2b0

### изменена: 0x5d99720 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3c190, стало 0x5d3f2a0

### изменена: 0x5d997f0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3c180, стало 0x5d3f290

### изменена: 0x5d998c0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3c170, стало 0x5d3f280

### изменена: 0x5d99990 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3c160, стало 0x5d3f270

### изменена: 0x5d99a60 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3c150, стало 0x5d3f260

### изменена: 0x5d99b30 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3c140, стало 0x5d3f250

### изменена: 0x5d99c00 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3c130, стало 0x5d3f240

### изменена: 0x5d99cd0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3c120, стало 0x5d3f230

### изменена: 0x5d99da0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3c110, стало 0x5d3f220

### изменена: 0x5d99e70 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3c100, стало 0x5d3f210

### изменена: 0x5d99f40 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3c0f0, стало 0x5d3f200

### изменена: 0x5d9a010 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3c0e0, стало 0x5d3f1f0

### изменена: 0x5d9a0e0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3c0d0, стало 0x5d3f1e0

### изменена: 0x5d9a1b0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3c0c0, стало 0x5d3f1d0

### изменена: 0x5d9a280 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3c0b0, стало 0x5d3f1c0

### изменена: 0x5d9a350 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3c0a0, стало 0x5d3f1b0

### изменена: 0x5d9a420 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3c090, стало 0x5d3f1a0

### изменена: 0x5d9a4f0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3c080, стало 0x5d3f190

### изменена: 0x5d9a5c0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3c070, стало 0x5d3f180

### изменена: 0x5d9a690 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3c060, стало 0x5d3f170

### изменена: 0x5d9a760 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3c050, стало 0x5d3f160

### изменена: 0x5d9a830 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3c040, стало 0x5d3f150

### изменена: 0x5d9a900 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3c030, стало 0x5d3f140

### изменена: 0x5d9a9d0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3c020, стало 0x5d3f130

### изменена: 0x5d9aaa0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3c010, стало 0x5d3f120

### изменена: 0x5d9ab70 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3c000, стало 0x5d3f110

### изменена: 0x5d9ac40 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3bff0, стало 0x5d3f100

### изменена: 0x5d9ad10 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3bfe0, стало 0x5d3f0f0

### изменена: 0x5d9ade0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3bfd0, стало 0x5d3f0e0

### изменена: 0x5d9aeb0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3bfc0, стало 0x5d3f0d0

### изменена: 0x5d9af80 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3bfb0, стало 0x5d3f0c0

### изменена: 0x5d9b050 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3bfa0, стало 0x5d3f0b0

### изменена: 0x5d9b120 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3bf90, стало 0x5d3f0a0

### изменена: 0x5d9b1f0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3bf80, стало 0x5d3f090

### изменена: 0x5d9b2c0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3bf70, стало 0x5d3f080

### изменена: 0x5d9b390 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3bf60, стало 0x5d3f070

### изменена: 0x5d9b460 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3bf50, стало 0x5d3f060

### изменена: 0x5d9b530 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3bf40, стало 0x5d3f050

### изменена: 0x5d9b600 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3bf30, стало 0x5d3f040

### изменена: 0x5d9b6d0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3bf20, стало 0x5d3f030

### изменена: 0x5d9b7a0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3bf10, стало 0x5d3f020

### изменена: 0x5d9b870 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3bf00, стало 0x5d3f010

### изменена: 0x5d9b940 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3bef0, стало 0x5d3f000

### изменена: 0x5d9ba10 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3bee0, стало 0x5d3eff0

### изменена: 0x5d9bae0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3bed0, стало 0x5d3efe0

### изменена: 0x5d9bbb0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3bec0, стало 0x5d3efd0

### изменена: 0x5d9bc80 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3beb0, стало 0x5d3efc0

### изменена: 0x5d9bd50 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3bea0, стало 0x5d3efb0

### изменена: 0x5d9be20 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3be90, стало 0x5d3efa0

### изменена: 0x5d9bef0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3be80, стало 0x5d3ef90

### изменена: 0x5d9bfc0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3be70, стало 0x5d3ef80

### изменена: 0x5d9c090 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3be60, стало 0x5d3ef70

### изменена: 0x5d9c160 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3be50, стало 0x5d3ef60

### изменена: 0x5d9c230 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3be40, стало 0x5d3ef50

### изменена: 0x5d9c300 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3be30, стало 0x5d3ef40

### изменена: 0x5d9c3d0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3be20, стало 0x5d3ef30

### изменена: 0x5d9c4a0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3be10, стало 0x5d3ef20

### изменена: 0x5d9c570 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3be00, стало 0x5d3ef10

### изменена: 0x5d9c640 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3bdf0, стало 0x5d3ef00

### изменена: 0x5d9c710 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3bde0, стало 0x5d3eef0

### изменена: 0x5d9c7e0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3bdd0, стало 0x5d3eee0

### изменена: 0x5d9c8b0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3bdc0, стало 0x5d3eed0

### изменена: 0x5d9c980 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3bdb0, стало 0x5d3eec0

### изменена: 0x5d9ca50 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3bda0, стало 0x5d3eeb0

### изменена: 0x5d9cb20 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3bd90, стало 0x5d3eea0

### изменена: 0x5d9cbf0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3bd80, стало 0x5d3ee90

### изменена: 0x5d9ccc0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3bd70, стало 0x5d3ee80

### изменена: 0x5d9cd90 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3bd60, стало 0x5d3ee70

### изменена: 0x5d9ce60 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3bd50, стало 0x5d3ee60

### изменена: 0x5d9cf30 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3bd40, стало 0x5d3ee50

### изменена: 0x5d9d000 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3bd30, стало 0x5d3ee40

### изменена: 0x5d9d0d0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3bd20, стало 0x5d3ee30

### изменена: 0x5d9d1a0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3bd10, стало 0x5d3ee20

### изменена: 0x5d9d270 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3bd00, стало 0x5d3ee10

### изменена: 0x5d9d340 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3bcf0, стало 0x5d3ee00

### изменена: 0x5d9d410 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3bce0, стало 0x5d3edf0

### изменена: 0x5d9d4e0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3bcd0, стало 0x5d3ede0

### изменена: 0x5d9d5b0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3bcc0, стало 0x5d3edd0

### изменена: 0x5d9d680 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3bcb0, стало 0x5d3edc0

### изменена: 0x5d9d750 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3bca0, стало 0x5d3edb0

### изменена: 0x5d9d820 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3bc90, стало 0x5d3eda0

### изменена: 0x5d9d8f0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3bc80, стало 0x5d3ed90

### изменена: 0x5d9d9c0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3bc70, стало 0x5d3ed80

### изменена: 0x5d9da90 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3bc60, стало 0x5d3ed70

### изменена: 0x5d9db60 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3bc50, стало 0x5d3ed60

### изменена: 0x5d9dc30 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3bc40, стало 0x5d3ed50

### изменена: 0x5d9dd00 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3bc30, стало 0x5d3ed40

### изменена: 0x5d9ddd0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3bc20, стало 0x5d3ed30

### изменена: 0x5d9dea0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3bc10, стало 0x5d3ed20

### изменена: 0x5d9df70 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3bc00, стало 0x5d3ed10

### изменена: 0x5d9e040 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3bbf0, стало 0x5d3ed00

### изменена: 0x5d9e110 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3bbe0, стало 0x5d3ecf0

### изменена: 0x5d9e1e0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3bbd0, стало 0x5d3ece0

### изменена: 0x5d9e2b0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3bbc0, стало 0x5d3ecd0

### изменена: 0x5d9e380 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3bbb0, стало 0x5d3ecc0

### изменена: 0x5d9e450 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3bba0, стало 0x5d3ecb0

### изменена: 0x5d9e520 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3bb90, стало 0x5d3eca0

### изменена: 0x5d9e5f0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3bb80, стало 0x5d3ec90

### изменена: 0x5d9e6c0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3bb70, стало 0x5d3ec80

### изменена: 0x5d9e790 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3bb60, стало 0x5d3ec70

### изменена: 0x5d9e860 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3bb50, стало 0x5d3ec60

### изменена: 0x5d9e930 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3bb40, стало 0x5d3ec50

### изменена: 0x5d9ea00 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3bb30, стало 0x5d3ec40

### изменена: 0x5d9ead0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3bb20, стало 0x5d3ec30

### изменена: 0x5d9eba0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3bb10, стало 0x5d3ec20

### изменена: 0x5d9ec70 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3bb00, стало 0x5d3ec10

### изменена: 0x5d9ed40 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3baf0, стало 0x5d3ec00

### изменена: 0x5d9ee10 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3bae0, стало 0x5d3ebf0

### изменена: 0x5d9eee0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3bad0, стало 0x5d3ebe0

### изменена: 0x5d9efb0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3bac0, стало 0x5d3ebd0

### изменена: 0x5d9f080 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3bab0, стало 0x5d3ebc0

### изменена: 0x5d9f150 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3baa0, стало 0x5d3ebb0

### изменена: 0x5d9f220 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3ba90, стало 0x5d3eba0

### изменена: 0x5d9f2f0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3ba80, стало 0x5d3eb90

### изменена: 0x5d9f3c0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3ba70, стало 0x5d3eb80

### изменена: 0x5d9f490 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3ba60, стало 0x5d3eb70

### изменена: 0x5d9f560 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3ba50, стало 0x5d3eb60

### изменена: 0x5d9f630 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3ba40, стало 0x5d3eb50

### изменена: 0x5d9f700 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3ba30, стало 0x5d3eb40

### изменена: 0x5d9f7d0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3ba20, стало 0x5d3eb30

### изменена: 0x5d9f8a0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3ba10, стало 0x5d3eb20

### изменена: 0x5d9f970 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3ba00, стало 0x5d3eb10

### изменена: 0x5d9fa40 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3b9f0, стало 0x5d3eb00

### изменена: 0x5d9fb10 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3b9e0, стало 0x5d3eaf0

### изменена: 0x5d9fbe0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3b9d0, стало 0x5d3eae0

### изменена: 0x5d9fcb0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3b9c0, стало 0x5d3ead0

### изменена: 0x5d9fd80 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3b9b0, стало 0x5d3eac0

### изменена: 0x5d9fe50 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3b9a0, стало 0x5d3eab0

### изменена: 0x5d9ff20 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3b990, стало 0x5d3eaa0

### изменена: 0x5d9fff0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3b980, стало 0x5d3ea90

### изменена: 0x5da00c0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3b970, стало 0x5d3ea80

### изменена: 0x5da0190 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3b960, стало 0x5d3ea70

### изменена: 0x5da0260 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3b950, стало 0x5d3ea60

### изменена: 0x5da0330 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3b940, стало 0x5d3ea50

### изменена: 0x5da0400 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3b930, стало 0x5d3ea40

### изменена: 0x5da04d0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3b920, стало 0x5d3ea30

### изменена: 0x5da05a0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3b910, стало 0x5d3ea20

### изменена: 0x5da0670 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3b900, стало 0x5d3ea10

### изменена: 0x5da0740 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3b8f0, стало 0x5d3ea00

### изменена: 0x5da0810 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3b8e0, стало 0x5d3e9f0

### изменена: 0x5da08e0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3b8d0, стало 0x5d3e9e0

### изменена: 0x5da09b0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3b8c0, стало 0x5d3e9d0

### изменена: 0x5da0a80 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3b8b0, стало 0x5d3e9c0

### изменена: 0x5da0b50 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3b8a0, стало 0x5d3e9b0

### изменена: 0x5da0c20 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3b890, стало 0x5d3e9a0

### изменена: 0x5da0cf0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3b880, стало 0x5d3e990

### изменена: 0x5da0dc0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3b870, стало 0x5d3e980

### изменена: 0x5da0e90 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3b860, стало 0x5d3e970

### изменена: 0x5da0f60 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3ae60, стало 0x5d3df70

### изменена: 0x5da1030 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3ae50, стало 0x5d3df60

### изменена: 0x5da1100 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3ae40, стало 0x5d3df50

### изменена: 0x5da11d0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3ae30, стало 0x5d3df40

### изменена: 0x5da12a0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3ae20, стало 0x5d3df30

### изменена: 0x5da1370 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3ae10, стало 0x5d3df20

### изменена: 0x5da1440 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3ae00, стало 0x5d3df10

### изменена: 0x5da1510 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3adf0, стало 0x5d3df00

### изменена: 0x5da15e0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3ade0, стало 0x5d3def0

### изменена: 0x5da16b0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3add0, стало 0x5d3dee0

### изменена: 0x5da1780 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3adc0, стало 0x5d3ded0

### изменена: 0x5da1850 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3adb0, стало 0x5d3dec0

### изменена: 0x5da1920 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3ada0, стало 0x5d3deb0

### изменена: 0x5da19f0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3ad90, стало 0x5d3dea0

### изменена: 0x5da1ac0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3ad80, стало 0x5d3de90

### изменена: 0x5da1b90 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3ad70, стало 0x5d3de80

### изменена: 0x5da1c60 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3ad60, стало 0x5d3de70

### изменена: 0x5da1d30 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3ad50, стало 0x5d3de60

### изменена: 0x5da1e00 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3ad40, стало 0x5d3de50

### изменена: 0x5da1ed0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3ad30, стало 0x5d3de40

### изменена: 0x5da1fa0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3ad20, стало 0x5d3de30

### изменена: 0x5da2070 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3ad10, стало 0x5d3de20

### изменена: 0x5da2140 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3ad00, стало 0x5d3de10

### изменена: 0x5da2210 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3acf0, стало 0x5d3de00

### изменена: 0x5da22e0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3ace0, стало 0x5d3ddf0

### изменена: 0x5da23b0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3acd0, стало 0x5d3dde0

### изменена: 0x5da2480 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3acc0, стало 0x5d3ddd0

### изменена: 0x5da2550 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3acb0, стало 0x5d3ddc0

### изменена: 0x5da2620 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3aca0, стало 0x5d3ddb0

### изменена: 0x5da26f0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3ac90, стало 0x5d3dda0

### изменена: 0x5da27c0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3ac80, стало 0x5d3dd90

### изменена: 0x5da2890 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3ac70, стало 0x5d3dd80

### изменена: 0x5da2960 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3ac60, стало 0x5d3dd70

### изменена: 0x5da2a30 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3ac50, стало 0x5d3dd60

### изменена: 0x5da2b00 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3ac40, стало 0x5d3dd50

### изменена: 0x5da2bd0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3ac30, стало 0x5d3dd40

### изменена: 0x5da2ca0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3ac20, стало 0x5d3dd30

### изменена: 0x5da2d70 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3ac10, стало 0x5d3dd20

### изменена: 0x5da2e40 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3ac00, стало 0x5d3dd10

### изменена: 0x5da2f10 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3abf0, стало 0x5d3dd00

### изменена: 0x5da2fe0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3abe0, стало 0x5d3dcf0

### изменена: 0x5da30b0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3abd0, стало 0x5d3dce0

### изменена: 0x5da3180 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3abc0, стало 0x5d3dcd0

### изменена: 0x5da3250 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3abb0, стало 0x5d3dcc0

### изменена: 0x5da3320 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3aba0, стало 0x5d3dcb0

### изменена: 0x5da33f0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3ab90, стало 0x5d3dca0

### изменена: 0x5da34c0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3ab80, стало 0x5d3dc90

### изменена: 0x5da3590 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3ab70, стало 0x5d3dc80

### изменена: 0x5da3660 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3ab60, стало 0x5d3dc70

### изменена: 0x5da3730 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3ab50, стало 0x5d3dc60

### изменена: 0x5da3800 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3ab40, стало 0x5d3dc50

### изменена: 0x5da38d0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3ab30, стало 0x5d3dc40

### изменена: 0x5da39a0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3ab20, стало 0x5d3dc30

### изменена: 0x5da3a70 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3ab10, стало 0x5d3dc20

### изменена: 0x5da3b40 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3ab00, стало 0x5d3dc10

### изменена: 0x5da3c10 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3aaf0, стало 0x5d3dc00

### изменена: 0x5da3ce0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3aae0, стало 0x5d3dbf0

### изменена: 0x5da3db0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3aad0, стало 0x5d3dbe0

### изменена: 0x5da3e80 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3aac0, стало 0x5d3dbd0

### изменена: 0x5da3f50 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3aab0, стало 0x5d3dbc0

### изменена: 0x5da4020 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3aaa0, стало 0x5d3dbb0

### изменена: 0x5da40f0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3aa90, стало 0x5d3dba0

### изменена: 0x5da41c0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3aa80, стало 0x5d3db90

### изменена: 0x5da4290 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3aa70, стало 0x5d3db80

### изменена: 0x5da4360 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3aa60, стало 0x5d3db70

### изменена: 0x5da4430 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3aa50, стало 0x5d3db60

### изменена: 0x5da4500 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3aa40, стало 0x5d3db50

### изменена: 0x5da45d0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3aa30, стало 0x5d3db40

### изменена: 0x5da46a0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3aa20, стало 0x5d3db30

### изменена: 0x5da4770 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3aa10, стало 0x5d3db20

### изменена: 0x5da4840 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3aa00, стало 0x5d3db10

### изменена: 0x5da4910 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3a9f0, стало 0x5d3db00

### изменена: 0x5da49e0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3a9e0, стало 0x5d3daf0

### изменена: 0x5da4ab0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3a9d0, стало 0x5d3dae0

### изменена: 0x5da4b80 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3a9c0, стало 0x5d3dad0

### изменена: 0x5da4c50 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3a9b0, стало 0x5d3dac0

### изменена: 0x5da4d20 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3a9a0, стало 0x5d3dab0

### изменена: 0x5da4df0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3a990, стало 0x5d3daa0

### изменена: 0x5da4ec0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3a980, стало 0x5d3da90

### изменена: 0x5da4f90 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3a970, стало 0x5d3da80

### изменена: 0x5da5060 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3a960, стало 0x5d3da70

### изменена: 0x5da5130 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3a950, стало 0x5d3da60

### изменена: 0x5da5200 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3a940, стало 0x5d3da50

### изменена: 0x5da52d0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3a930, стало 0x5d3da40

### изменена: 0x5da53a0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3a920, стало 0x5d3da30

### изменена: 0x5da5470 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3a910, стало 0x5d3da20

### изменена: 0x5da5540 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3a900, стало 0x5d3da10

### изменена: 0x5da5610 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3a8f0, стало 0x5d3da00

### изменена: 0x5da56e0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3a8e0, стало 0x5d3d9f0

### изменена: 0x5da57b0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3a8d0, стало 0x5d3d9e0

### изменена: 0x5da5880 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3a8c0, стало 0x5d3d9d0

### изменена: 0x5da5950 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3a8b0, стало 0x5d3d9c0

### изменена: 0x5da5a20 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3a8a0, стало 0x5d3d9b0

### изменена: 0x5da5af0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3a890, стало 0x5d3d9a0

### изменена: 0x5da5bc0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3a880, стало 0x5d3d990

### изменена: 0x5da5c90 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3a870, стало 0x5d3d980

### изменена: 0x5da5d60 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3a860, стало 0x5d3d970

### изменена: 0x5da5e30 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3a850, стало 0x5d3d960

### изменена: 0x5da5f00 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3a840, стало 0x5d3d950

### изменена: 0x5da5fd0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3a830, стало 0x5d3d940

### изменена: 0x5da60a0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3a820, стало 0x5d3d930

### изменена: 0x5da6170 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3a810, стало 0x5d3d920

### изменена: 0x5da6240 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3a800, стало 0x5d3d910

### изменена: 0x5da6310 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3a7f0, стало 0x5d3d900

### изменена: 0x5da63e0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3a7e0, стало 0x5d3d8f0

### изменена: 0x5da64b0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3a7d0, стало 0x5d3d8e0

### изменена: 0x5da6580 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3a7c0, стало 0x5d3d8d0

### изменена: 0x5da6650 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3a7b0, стало 0x5d3d8c0

### изменена: 0x5da6720 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3a7a0, стало 0x5d3d8b0

### изменена: 0x5da67f0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3a790, стало 0x5d3d8a0

### изменена: 0x5da68c0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3a780, стало 0x5d3d890

### изменена: 0x5da6990 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3a770, стало 0x5d3d880

### изменена: 0x5da6a60 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3a760, стало 0x5d3d870

### изменена: 0x5da6b30 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3a750, стало 0x5d3d860

### изменена: 0x5da6c00 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3a740, стало 0x5d3d850

### изменена: 0x5da6cd0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3a730, стало 0x5d3d840

### изменена: 0x5da6da0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3a720, стало 0x5d3d830

### изменена: 0x5da6e70 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3a710, стало 0x5d3d820

### изменена: 0x5da6f40 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3a700, стало 0x5d3d810

### изменена: 0x5da7010 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3a6f0, стало 0x5d3d800

### изменена: 0x5da70e0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3a6e0, стало 0x5d3d7f0

### изменена: 0x5da71b0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3a6d0, стало 0x5d3d7e0

### изменена: 0x5da7280 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3a6c0, стало 0x5d3d7d0

### изменена: 0x5da7350 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3a6b0, стало 0x5d3d7c0

### изменена: 0x5da7420 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3a6a0, стало 0x5d3d7b0

### изменена: 0x5da74f0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3a690, стало 0x5d3d7a0

### изменена: 0x5da75c0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3a680, стало 0x5d3d790

### изменена: 0x5da7690 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3a670, стало 0x5d3d780

### изменена: 0x5da7760 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3a660, стало 0x5d3d770

### изменена: 0x5da7830 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3a650, стало 0x5d3d760

### изменена: 0x5da7900 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3a640, стало 0x5d3d750

### изменена: 0x5da79d0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3a630, стало 0x5d3d740

### изменена: 0x5da7aa0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3a620, стало 0x5d3d730

### изменена: 0x5da7b70 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3a610, стало 0x5d3d720

### изменена: 0x5da7c40 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3a600, стало 0x5d3d710

### изменена: 0x5da7d10 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3a5f0, стало 0x5d3d700

### изменена: 0x5da7de0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3a5e0, стало 0x5d3d6f0

### изменена: 0x5da7eb0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3a5d0, стало 0x5d3d6e0

### изменена: 0x5da7f80 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3a5c0, стало 0x5d3d6d0

### изменена: 0x5da8050 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3a5b0, стало 0x5d3d6c0

### изменена: 0x5da8120 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3a5a0, стало 0x5d3d6b0

### изменена: 0x5da81f0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3a590, стало 0x5d3d6a0

### изменена: 0x5da82c0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3a580, стало 0x5d3d690

### изменена: 0x5da8390 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3a570, стало 0x5d3d680

### изменена: 0x5da8460 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3a560, стало 0x5d3d670

### изменена: 0x5da8530 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3a550, стало 0x5d3d660

### изменена: 0x5da8600 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3a540, стало 0x5d3d650

### изменена: 0x5da86d0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3a530, стало 0x5d3d640

### изменена: 0x5da87a0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3a520, стало 0x5d3d630

### изменена: 0x5da8870 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3a510, стало 0x5d3d620

### изменена: 0x5da8940 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3a500, стало 0x5d3d610

### изменена: 0x5da8a10 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3a4f0, стало 0x5d3d600

### изменена: 0x5da8ae0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3a4e0, стало 0x5d3d5f0

### изменена: 0x5da8bb0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3a4d0, стало 0x5d3d5e0

### изменена: 0x5da8c80 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3a4c0, стало 0x5d3d5d0

### изменена: 0x5da8d50 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3a4b0, стало 0x5d3d5c0

### изменена: 0x5da8e20 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3a4a0, стало 0x5d3d5b0

### изменена: 0x5da8ef0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3a490, стало 0x5d3d5a0

### изменена: 0x5da8fc0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3a480, стало 0x5d3d590

### изменена: 0x5da9090 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3a470, стало 0x5d3d580

### изменена: 0x5da9160 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3a460, стало 0x5d3d570

### изменена: 0x5da9230 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3a450, стало 0x5d3d560

### изменена: 0x5da9300 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3a440, стало 0x5d3d550

### изменена: 0x5da93d0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3a430, стало 0x5d3d540

### изменена: 0x5da94a0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3a420, стало 0x5d3d530

### изменена: 0x5da9570 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3a410, стало 0x5d3d520

### изменена: 0x5da9640 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3a400, стало 0x5d3d510

### изменена: 0x5da9710 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3a3f0, стало 0x5d3d500

### изменена: 0x5da97e0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3a3e0, стало 0x5d3d4f0

### изменена: 0x5da98b0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3a3d0, стало 0x5d3d4e0

### изменена: 0x5da9980 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3a3c0, стало 0x5d3d4d0

### изменена: 0x5da9a50 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3a3b0, стало 0x5d3d4c0

### изменена: 0x5da9b20 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3a3a0, стало 0x5d3d4b0

### изменена: 0x5da9bf0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3a390, стало 0x5d3d4a0

### изменена: 0x5da9cc0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3a380, стало 0x5d3d490

### изменена: 0x5da9d90 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3a370, стало 0x5d3d480

### изменена: 0x5da9e60 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3a360, стало 0x5d3d470

### изменена: 0x5da9f30 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3a350, стало 0x5d3d460

### изменена: 0x5daa000 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3a340, стало 0x5d3d450

### изменена: 0x5daa0d0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3a330, стало 0x5d3d440

### изменена: 0x5daa1a0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3a320, стало 0x5d3d430

### изменена: 0x5daa270 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3a310, стало 0x5d3d420

### изменена: 0x5daa340 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3a300, стало 0x5d3d410

### изменена: 0x5daa410 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3a2f0, стало 0x5d3d400

### изменена: 0x5daa4e0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3a2e0, стало 0x5d3d3f0

### изменена: 0x5daa5b0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3a2d0, стало 0x5d3d3e0

### изменена: 0x5daa680 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3a2c0, стало 0x5d3d3d0

### изменена: 0x5daa750 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3a2b0, стало 0x5d3d3c0

### изменена: 0x5daa820 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3a2a0, стало 0x5d3d3b0

### изменена: 0x5daa8f0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3a290, стало 0x5d3d3a0

### изменена: 0x5daa9c0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3a280, стало 0x5d3d390

### изменена: 0x5daaa90 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3a270, стало 0x5d3d380

### изменена: 0x5daab60 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3a260, стало 0x5d3d370

### изменена: 0x5daac30 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3a250, стало 0x5d3d360

### изменена: 0x5daad00 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3a240, стало 0x5d3d350

### изменена: 0x5daadd0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3a230, стало 0x5d3d340

### изменена: 0x5daaea0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3a220, стало 0x5d3d330

### изменена: 0x5daaf70 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3a210, стало 0x5d3d320

### изменена: 0x5dab040 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3a200, стало 0x5d3d310

### изменена: 0x5dab110 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3a1f0, стало 0x5d3d300

### изменена: 0x5dab1e0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3a1e0, стало 0x5d3d2f0

### изменена: 0x5dab2b0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3a1d0, стало 0x5d3d2e0

### изменена: 0x5dab380 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3a1c0, стало 0x5d3d2d0

### изменена: 0x5dab450 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3a1b0, стало 0x5d3d2c0

### изменена: 0x5dab520 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3a1a0, стало 0x5d3d2b0

### изменена: 0x5dab5f0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3a190, стало 0x5d3d2a0

### изменена: 0x5dab6c0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3a180, стало 0x5d3d290

### изменена: 0x5dab790 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3a170, стало 0x5d3d280

### изменена: 0x5dab860 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3a160, стало 0x5d3d270

### изменена: 0x5dab930 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3a150, стало 0x5d3d260

### изменена: 0x5daba00 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3a140, стало 0x5d3d250

### изменена: 0x5dabad0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3a130, стало 0x5d3d240

### изменена: 0x5dabba0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3a120, стало 0x5d3d230

### изменена: 0x5dabc70 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3a110, стало 0x5d3d220

### изменена: 0x5dabd40 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3a100, стало 0x5d3d210

### изменена: 0x5dabe10 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3a0f0, стало 0x5d3d200

### изменена: 0x5dabee0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3a0e0, стало 0x5d3d1f0

### изменена: 0x5dabfb0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3a0d0, стало 0x5d3d1e0

### изменена: 0x5dac080 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3a0c0, стало 0x5d3d1d0

### изменена: 0x5dac150 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3a0b0, стало 0x5d3d1c0

### изменена: 0x5dac220 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3a0a0, стало 0x5d3d1b0

### изменена: 0x5dac2f0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3a090, стало 0x5d3d1a0

### изменена: 0x5dac3c0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3a080, стало 0x5d3d190

### изменена: 0x5dac490 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3a070, стало 0x5d3d180

### изменена: 0x5dac560 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3a060, стало 0x5d3d170

### изменена: 0x5dac630 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3a050, стало 0x5d3d160

### изменена: 0x5dac700 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3a040, стало 0x5d3d150

### изменена: 0x5dac7d0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3a030, стало 0x5d3d140

### изменена: 0x5dac8a0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3a020, стало 0x5d3d130

### изменена: 0x5dac970 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3a010, стало 0x5d3d120

### изменена: 0x5daca40 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d3a000, стало 0x5d3d110

### изменена: 0x5dacb10 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d39ff0, стало 0x5d3d100

### изменена: 0x5dacbe0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d39fe0, стало 0x5d3d0f0

### изменена: 0x5daccb0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d39fd0, стало 0x5d3d0e0

### изменена: 0x5dacd80 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d39fc0, стало 0x5d3d0d0

### изменена: 0x5dace50 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d39fb0, стало 0x5d3d0c0

### изменена: 0x5dacf20 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d39fa0, стало 0x5d3d0b0

### изменена: 0x5dacff0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d39f90, стало 0x5d3d0a0

### изменена: 0x5dad0c0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d39f80, стало 0x5d3d090

### изменена: 0x5dad190 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d39f70, стало 0x5d3d080

### изменена: 0x5dad260 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d39f60, стало 0x5d3d070

### изменена: 0x5dad330 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d39f50, стало 0x5d3d060

### изменена: 0x5dad400 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d39f40, стало 0x5d3d050

### изменена: 0x5dad4d0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d39f30, стало 0x5d3d040

### изменена: 0x5dad5a0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d39f20, стало 0x5d3d030

### изменена: 0x5dad670 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d39f10, стало 0x5d3d020

### изменена: 0x5dad740 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d39f00, стало 0x5d3d010

### изменена: 0x5dad810 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d39ef0, стало 0x5d3d000

### изменена: 0x5dad8e0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d39ee0, стало 0x5d3cff0

### изменена: 0x5dad9b0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d39ed0, стало 0x5d3cfe0

### изменена: 0x5dada80 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d39ec0, стало 0x5d3cfd0

### изменена: 0x5dadb50 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d39eb0, стало 0x5d3cfc0

### изменена: 0x5dadc20 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d39ea0, стало 0x5d3cfb0

### изменена: 0x5dadcf0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d39e90, стало 0x5d3cfa0

### изменена: 0x5daddc0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d39e80, стало 0x5d3cf90

### изменена: 0x5dade90 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d39e70, стало 0x5d3cf80

### изменена: 0x5dadf60 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d39e60, стало 0x5d3cf70

### изменена: 0x5dae030 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d39e50, стало 0x5d3cf60

### изменена: 0x5dae100 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d39e40, стало 0x5d3cf50

### изменена: 0x5dae1d0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d39e30, стало 0x5d3cf40

### изменена: 0x5dae2a0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d39e20, стало 0x5d3cf30

### изменена: 0x5dae370 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d39e10, стало 0x5d3cf20

### изменена: 0x5dae440 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d39e00, стало 0x5d3cf10

### изменена: 0x5dae510 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d39df0, стало 0x5d3cf00

### изменена: 0x5dae5e0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d39de0, стало 0x5d3cef0

### изменена: 0x5dae6b0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d39dd0, стало 0x5d3cee0

### изменена: 0x5dae780 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d39dc0, стало 0x5d3ced0

### изменена: 0x5dae850 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d39db0, стало 0x5d3cec0

### изменена: 0x5dae920 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d39da0, стало 0x5d3ceb0

### изменена: 0x5dae9f0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d39d90, стало 0x5d3cea0

### изменена: 0x5daeac0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d39d80, стало 0x5d3ce90

### изменена: 0x5daeb90 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d39d70, стало 0x5d3ce80

### изменена: 0x5daec60 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d39d60, стало 0x5d3ce70

### изменена: 0x5daed30 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d39d50, стало 0x5d3ce60

### изменена: 0x5daee00 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d39d40, стало 0x5d3ce50

### изменена: 0x5daeed0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d39d30, стало 0x5d3ce40

### изменена: 0x5daefa0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d39d20, стало 0x5d3ce30

### изменена: 0x5daf070 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d39d10, стало 0x5d3ce20

### изменена: 0x5daf140 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d39d00, стало 0x5d3ce10

### изменена: 0x5daf210 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d39cf0, стало 0x5d3ce00

### изменена: 0x5daf2e0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d39ce0, стало 0x5d3cdf0

### изменена: 0x5daf3b0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d39cd0, стало 0x5d3cde0

### изменена: 0x5daf480 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d39cc0, стало 0x5d3cdd0

### изменена: 0x5daf550 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d39cb0, стало 0x5d3cdc0

### изменена: 0x5daf620 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d39ca0, стало 0x5d3cdb0

### изменена: 0x5daf6f0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d39c90, стало 0x5d3cda0

### изменена: 0x5daf7c0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d39c80, стало 0x5d3cd90

### изменена: 0x5daf890 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d39c70, стало 0x5d3cd80

### изменена: 0x5daf960 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d39c60, стало 0x5d3cd70

### изменена: 0x5dafa30 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d39c50, стало 0x5d3cd60

### изменена: 0x5dafb00 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d39c40, стало 0x5d3cd50

### изменена: 0x5dafbd0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d39c30, стало 0x5d3cd40

### изменена: 0x5dafca0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d39c20, стало 0x5d3cd30

### изменена: 0x5dafd70 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d39c10, стало 0x5d3cd20

### изменена: 0x5dafe40 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d39c00, стало 0x5d3cd10

### изменена: 0x5daff10 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d39bf0, стало 0x5d3cd00

### изменена: 0x5daffe0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d39be0, стало 0x5d3ccf0

### изменена: 0x5db00b0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d39bd0, стало 0x5d3cce0

### изменена: 0x5db0180 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d39bc0, стало 0x5d3ccd0

### изменена: 0x5db0250 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d39bb0, стало 0x5d3ccc0

### изменена: 0x5db0320 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d39ba0, стало 0x5d3ccb0

### изменена: 0x5db03f0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d39b90, стало 0x5d3cca0

### изменена: 0x5db04c0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d39b80, стало 0x5d3cc90

### изменена: 0x5db0590 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d39b70, стало 0x5d3cc80

### изменена: 0x5db0660 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d39b60, стало 0x5d3cc70

### изменена: 0x5db0730 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d39b50, стало 0x5d3cc60

### изменена: 0x5db0800 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d39b40, стало 0x5d3cc50

### изменена: 0x5db08d0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d39b30, стало 0x5d3cc40

### изменена: 0x5db09a0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d39b20, стало 0x5d3cc30

### изменена: 0x5db0a70 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d39b10, стало 0x5d3cc20

### изменена: 0x5db0b40 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d39b00, стало 0x5d3cc10

### изменена: 0x5db0c10 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d39af0, стало 0x5d3cc00

### изменена: 0x5db0ce0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d39ae0, стало 0x5d3cbf0

### изменена: 0x5db0db0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d39ad0, стало 0x5d3cbe0

### изменена: 0x5db0e80 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d39ac0, стало 0x5d3cbd0

### изменена: 0x5db0f50 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d39ab0, стало 0x5d3cbc0

### изменена: 0x5db1020 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d39aa0, стало 0x5d3cbb0

### изменена: 0x5db10f0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d39a90, стало 0x5d3cba0

### изменена: 0x5db11c0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d39a80, стало 0x5d3cb90

### изменена: 0x5db1290 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d39a70, стало 0x5d3cb80

### изменена: 0x5db1360 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d39a60, стало 0x5d3cb70

### изменена: 0x5db1430 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d39a50, стало 0x5d3cb60

### изменена: 0x5db1500 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d39a40, стало 0x5d3cb50

### изменена: 0x5db15d0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d39a30, стало 0x5d3cb40

### изменена: 0x5db16a0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d39a20, стало 0x5d3cb30

### изменена: 0x5db1770 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d39a10, стало 0x5d3cb20

### изменена: 0x5db1840 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d39a00, стало 0x5d3cb10

### изменена: 0x5db1910 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d399f0, стало 0x5d3cb00

### изменена: 0x5db19e0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d399e0, стало 0x5d3caf0

### изменена: 0x5db1ab0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d399d0, стало 0x5d3cae0

### изменена: 0x5db1b80 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d399c0, стало 0x5d3cad0

### изменена: 0x5db1c50 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d399b0, стало 0x5d3cac0

### изменена: 0x5db1d20 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d399a0, стало 0x5d3cab0

### изменена: 0x5db1df0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d39990, стало 0x5d3caa0

### изменена: 0x5db1ec0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d39980, стало 0x5d3ca90

### изменена: 0x5db1f90 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d39970, стало 0x5d3ca80

### изменена: 0x5db2060 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d39960, стало 0x5d3ca70

### изменена: 0x5db2130 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d39950, стало 0x5d3ca60

### изменена: 0x5db2200 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d39940, стало 0x5d3ca50

### изменена: 0x5db22d0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d39930, стало 0x5d3ca40

### изменена: 0x5db23a0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d39920, стало 0x5d3ca30

### изменена: 0x5db2470 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d39910, стало 0x5d3ca20

### изменена: 0x5db2540 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d39900, стало 0x5d3ca10

### изменена: 0x5db2610 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d398f0, стало 0x5d3ca00

### изменена: 0x5db26e0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d398e0, стало 0x5d3c9f0

### изменена: 0x5db27b0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d398d0, стало 0x5d3c9e0

### изменена: 0x5db2880 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d398c0, стало 0x5d3c9d0

### изменена: 0x5db2950 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d398b0, стало 0x5d3c9c0

### изменена: 0x5db2a20 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d398a0, стало 0x5d3c9b0

### изменена: 0x5db2af0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d39890, стало 0x5d3c9a0

### изменена: 0x5db2bc0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d39880, стало 0x5d3c990

### изменена: 0x5db2c90 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d39870, стало 0x5d3c980

### изменена: 0x5db2d60 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d39860, стало 0x5d3c970

### изменена: 0x5db2e30 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d39850, стало 0x5d3c960

### изменена: 0x5db2f00 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d39840, стало 0x5d3c950

### изменена: 0x5db2fd0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d39830, стало 0x5d3c940

### изменена: 0x5db30a0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d39820, стало 0x5d3c930

### изменена: 0x5db3170 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d39810, стало 0x5d3c920

### изменена: 0x5db3240 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d39800, стало 0x5d3c910

### изменена: 0x5db3310 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d397f0, стало 0x5d3c900

### изменена: 0x5db33e0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d397e0, стало 0x5d3c8f0

### изменена: 0x5db34b0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d397d0, стало 0x5d3c8e0

### изменена: 0x5db3580 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d397c0, стало 0x5d3c8d0

### изменена: 0x5db3650 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d397b0, стало 0x5d3c8c0

### изменена: 0x5db3720 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d397a0, стало 0x5d3c8b0

### изменена: 0x5db37f0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d39790, стало 0x5d3c8a0

### изменена: 0x5db38c0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d39780, стало 0x5d3c890

### изменена: 0x5db3990 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d39770, стало 0x5d3c880

### изменена: 0x5db3a60 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d39760, стало 0x5d3c870

### изменена: 0x5db3b30 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d39750, стало 0x5d3c860

### изменена: 0x5db3c00 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d39740, стало 0x5d3c850

### изменена: 0x5db3cd0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d39730, стало 0x5d3c840

### изменена: 0x5db3da0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d39720, стало 0x5d3c830

### изменена: 0x5db3e70 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d39710, стало 0x5d3c820

### изменена: 0x5db3f40 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d39700, стало 0x5d3c810

### изменена: 0x5db4010 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d396f0, стало 0x5d3c800

### изменена: 0x5db40e0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d396e0, стало 0x5d3c7f0

### изменена: 0x5db41b0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d396d0, стало 0x5d3c7e0

### изменена: 0x5db4280 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d396c0, стало 0x5d3c7d0

### изменена: 0x5db4350 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d396b0, стало 0x5d3c7c0

### изменена: 0x5db4420 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d396a0, стало 0x5d3c7b0

### изменена: 0x5db44f0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d39690, стало 0x5d3c7a0

### изменена: 0x5db45c0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d39680, стало 0x5d3c790

### изменена: 0x5db4690 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d39670, стало 0x5d3c780

### изменена: 0x5db4760 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d39660, стало 0x5d3c770

### изменена: 0x5db4830 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d39650, стало 0x5d3c760

### изменена: 0x5db4900 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d39640, стало 0x5d3c750

### изменена: 0x5db49d0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d39630, стало 0x5d3c740

### изменена: 0x5db4aa0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d39620, стало 0x5d3c730

### изменена: 0x5db4b70 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d39610, стало 0x5d3c720

### изменена: 0x5db4c40 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d39600, стало 0x5d3c710

### изменена: 0x5db4d10 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d395f0, стало 0x5d3c700

### изменена: 0x5db4de0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d395e0, стало 0x5d3c6f0

### изменена: 0x5db4eb0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d395d0, стало 0x5d3c6e0

### изменена: 0x5db4f80 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d395c0, стало 0x5d3c6d0

### изменена: 0x5db5050 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d395b0, стало 0x5d3c6c0

### изменена: 0x5db5120 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d395a0, стало 0x5d3c6b0

### изменена: 0x5db51f0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d39590, стало 0x5d3c6a0

### изменена: 0x5db52c0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d39580, стало 0x5d3c690

### изменена: 0x5db5390 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d39570, стало 0x5d3c680

### изменена: 0x5db5460 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d39560, стало 0x5d3c670

### изменена: 0x5db5530 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d39550, стало 0x5d3c660

### изменена: 0x5db5600 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d39540, стало 0x5d3c650

### изменена: 0x5db56d0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d39530, стало 0x5d3c640

### изменена: 0x5db57a0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d39520, стало 0x5d3c630

### изменена: 0x5db5870 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d39510, стало 0x5d3c620

### изменена: 0x5db5940 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d39500, стало 0x5d3c610

### изменена: 0x5db5a10 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d394f0, стало 0x5d3c600

### изменена: 0x5db5ae0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d394e0, стало 0x5d3c5f0

### изменена: 0x5db5bb0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d394d0, стало 0x5d3c5e0

### изменена: 0x5db5c80 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d394c0, стало 0x5d3c5d0

### изменена: 0x5db5d50 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d394b0, стало 0x5d3c5c0

### изменена: 0x5db5e20 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d394a0, стало 0x5d3c5b0

### изменена: 0x5db5ef0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d39490, стало 0x5d3c5a0

### изменена: 0x5db5fc0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d39480, стало 0x5d3c590

### изменена: 0x5db6090 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d39470, стало 0x5d3c580

### изменена: 0x5db6160 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d39460, стало 0x5d3c570

### изменена: 0x5db6230 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d39450, стало 0x5d3c560

### изменена: 0x5db6300 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d39440, стало 0x5d3c550

### изменена: 0x5db63d0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d39430, стало 0x5d3c540

### изменена: 0x5db64a0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d39420, стало 0x5d3c530

### изменена: 0x5db6570 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d39410, стало 0x5d3c520

### изменена: 0x5db6640 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d39400, стало 0x5d3c510

### изменена: 0x5db6710 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d393f0, стало 0x5d3c500

### изменена: 0x5db67e0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d393e0, стало 0x5d3c4f0

### изменена: 0x5db68b0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d393d0, стало 0x5d3c4e0

### изменена: 0x5db6980 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d393c0, стало 0x5d3c4d0

### изменена: 0x5db6a50 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d393b0, стало 0x5d3c4c0

### изменена: 0x5db6b20 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d393a0, стало 0x5d3c4b0

### изменена: 0x5db6bf0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d39390, стало 0x5d3c4a0

### изменена: 0x5db6cc0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d39380, стало 0x5d3c490

### изменена: 0x5db6d90 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d39370, стало 0x5d3c480

### изменена: 0x5db6e60 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d39360, стало 0x5d3c470

### изменена: 0x5db6f30 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d39350, стало 0x5d3c460

### изменена: 0x5db7000 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d39340, стало 0x5d3c450

### изменена: 0x5db70d0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d39330, стало 0x5d3c440

### изменена: 0x5db71a0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d39320, стало 0x5d3c430

### изменена: 0x5db7270 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d39310, стало 0x5d3c420

### изменена: 0x5db7340 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d39300, стало 0x5d3c410

### изменена: 0x5db7410 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d392f0, стало 0x5d3c400

### изменена: 0x5db74e0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d392e0, стало 0x5d3c3f0

### изменена: 0x5db75b0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d392d0, стало 0x5d3c3e0

### изменена: 0x5db7680 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d392c0, стало 0x5d3c3d0

### изменена: 0x5db7750 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d392b0, стало 0x5d3c3c0

### изменена: 0x5db7820 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d392a0, стало 0x5d3c3b0

### изменена: 0x5db78f0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d39290, стало 0x5d3c3a0

### изменена: 0x5db79c0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d39280, стало 0x5d3c390

### изменена: 0x5db7a90 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d39270, стало 0x5d3c380

### изменена: 0x5db7b60 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d39260, стало 0x5d3c370

### изменена: 0x5db7c30 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d39250, стало 0x5d3c360

### изменена: 0x5db7d00 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d39240, стало 0x5d3c350

### изменена: 0x5db7dd0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d39230, стало 0x5d3c340

### изменена: 0x5db7ea0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d39220, стало 0x5d3c330

### изменена: 0x5db7f70 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d39210, стало 0x5d3c320

### изменена: 0x5db8040 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d39200, стало 0x5d3c310

### изменена: 0x5db8110 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d391f0, стало 0x5d3c300

### изменена: 0x5db81e0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d391e0, стало 0x5d3c2f0

### изменена: 0x5db82b0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d391d0, стало 0x5d3c2e0

### изменена: 0x5db8380 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d391c0, стало 0x5d3c2d0

### изменена: 0x5db8450 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d391b0, стало 0x5d3c2c0

### изменена: 0x5db8520 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d391a0, стало 0x5d3c2b0

### изменена: 0x5db85f0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d39190, стало 0x5d3c2a0

### изменена: 0x5db86c0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d39180, стало 0x5d3c290

### изменена: 0x5db8790 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d39170, стало 0x5d3c280

### изменена: 0x5db8860 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d39160, стало 0x5d3c270

### изменена: 0x5db8930 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d39150, стало 0x5d3c260

### изменена: 0x5db8a00 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d39140, стало 0x5d3c250

### изменена: 0x5db8ad0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d39130, стало 0x5d3c240

### изменена: 0x5db8ba0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d39120, стало 0x5d3c230

### изменена: 0x5db8c70 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d39110, стало 0x5d3c220

### изменена: 0x5db8d40 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d39100, стало 0x5d3c210

### изменена: 0x5db8e10 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d390f0, стало 0x5d3c200

### изменена: 0x5db8ee0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d39070, стало 0x5d3c1f0

### изменена: 0x5db8fb0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d39080, стало 0x5d3c170

### изменена: 0x5db9080 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d39090, стало 0x5d3c180

### изменена: 0x5db9150 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d390a0, стало 0x5d3c190

### изменена: 0x5db9220 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d390b0, стало 0x5d3c1a0

### изменена: 0x5db92f0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d390c0, стало 0x5d3c1b0

### изменена: 0x5db93c0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d390d0, стало 0x5d3c1c0

### изменена: 0x5db9490 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d39060, стало 0x5d3c1d0

### изменена: 0x5db9560 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d39050, стало 0x5d3c160

### изменена: 0x5db9630 (206 байт)
- код тот же, но вызывает другую функцию: было 0x5d38ee0, стало 0x5d3c150

### изменена: 0x5dbaad0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x5d3b830, стало 0x5d3e940

### изменена: 0x5dbab10 (63 байт)
- код тот же, но вызывает другую функцию: было 0x5d3b800, стало 0x5d3e910

### изменена: 0x5dbab50 (63 байт)
- код тот же, но вызывает другую функцию: было 0x5d3b7d0, стало 0x5d3e8e0

### изменена: 0x5dbab90 (63 байт)
- код тот же, но вызывает другую функцию: было 0x5d3b7a0, стало 0x5d3e8b0

### изменена: 0x5dbabd0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x5d3b740, стало 0x5d3e850

### изменена: 0x5dbac10 (63 байт)
- код тот же, но вызывает другую функцию: было 0x5d3b710, стало 0x5d3e820

### изменена: 0x5dbac50 (63 байт)
- код тот же, но вызывает другую функцию: было 0x5d3b6e0, стало 0x5d3e7f0

### изменена: 0x5dbac90 (63 байт)
- код тот же, но вызывает другую функцию: было 0x5d3b6b0, стало 0x5d3e7c0

### изменена: 0x5dbacd0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x5d3b680, стало 0x5d3e790

### изменена: 0x5dbad10 (63 байт)
- код тот же, но вызывает другую функцию: было 0x5d3b650, стало 0x5d3e760

### изменена: 0x5dbad50 (63 байт)
- код тот же, но вызывает другую функцию: было 0x5d3b620, стало 0x5d3e730

### изменена: 0x5dbad90 (63 байт)
- код тот же, но вызывает другую функцию: было 0x5d3b5f0, стало 0x5d3e700

### изменена: 0x5dbadd0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x5d3b5c0, стало 0x5d3e6d0

### изменена: 0x5dbae10 (63 байт)
- код тот же, но вызывает другую функцию: было 0x5d3b590, стало 0x5d3e6a0

### изменена: 0x5dbae50 (63 байт)
- код тот же, но вызывает другую функцию: было 0x5d3b560, стало 0x5d3e670

### изменена: 0x5dbae90 (63 байт)
- код тот же, но вызывает другую функцию: было 0x5d3b530, стало 0x5d3e640

### изменена: 0x5dbaed0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x5d3b500, стало 0x5d3e610

### изменена: 0x5dbaf10 (63 байт)
- код тот же, но вызывает другую функцию: было 0x5d3b4d0, стало 0x5d3e5e0

### изменена: 0x5dbaf50 (63 байт)
- код тот же, но вызывает другую функцию: было 0x5d3b4a0, стало 0x5d3e5b0

### изменена: 0x5dbaf90 (63 байт)
- код тот же, но вызывает другую функцию: было 0x5d3b470, стало 0x5d3e580

### изменена: 0x5dbafd0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x5d3b440, стало 0x5d3e550

### изменена: 0x5dbb010 (63 байт)
- код тот же, но вызывает другую функцию: было 0x5d3b410, стало 0x5d3e520

### изменена: 0x5dbb050 (63 байт)
- код тот же, но вызывает другую функцию: было 0x5d3b3e0, стало 0x5d3e4f0

### изменена: 0x5dbb090 (63 байт)
- код тот же, но вызывает другую функцию: было 0x5d3b3b0, стало 0x5d3e4c0

### изменена: 0x5dbb0d0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x5d3b380, стало 0x5d3e490

### изменена: 0x5dbb110 (63 байт)
- код тот же, но вызывает другую функцию: было 0x5d3b350, стало 0x5d3e460

### изменена: 0x5dbb150 (63 байт)
- код тот же, но вызывает другую функцию: было 0x5d3b320, стало 0x5d3e430

### изменена: 0x5dbb190 (63 байт)
- код тот же, но вызывает другую функцию: было 0x5d3b2f0, стало 0x5d3e400

### изменена: 0x5dbb1d0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x5d3b2c0, стало 0x5d3e3d0

### изменена: 0x5dbb210 (63 байт)
- код тот же, но вызывает другую функцию: было 0x5d3b290, стало 0x5d3e3a0

### изменена: 0x5dbb250 (63 байт)
- код тот же, но вызывает другую функцию: было 0x5d3b260, стало 0x5d3e370

### изменена: 0x5dbb290 (63 байт)
- код тот же, но вызывает другую функцию: было 0x5d3b230, стало 0x5d3e340

### изменена: 0x5dbb2d0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x5d3b200, стало 0x5d3e310

### изменена: 0x5dbb310 (63 байт)
- код тот же, но вызывает другую функцию: было 0x5d3b1d0, стало 0x5d3e2e0

### изменена: 0x5dbb350 (63 байт)
- код тот же, но вызывает другую функцию: было 0x5d3b1a0, стало 0x5d3e2b0

### изменена: 0x5dbb390 (63 байт)
- код тот же, но вызывает другую функцию: было 0x5d3b170, стало 0x5d3e280

### изменена: 0x5dbb3d0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x5d3b140, стало 0x5d3e250

### изменена: 0x5dbb410 (63 байт)
- код тот же, но вызывает другую функцию: было 0x5d3b110, стало 0x5d3e220

### изменена: 0x5dbb450 (63 байт)
- код тот же, но вызывает другую функцию: было 0x5d3b0e0, стало 0x5d3e1f0

### изменена: 0x5dbb490 (63 байт)
- код тот же, но вызывает другую функцию: было 0x5d3b0b0, стало 0x5d3e1c0

### изменена: 0x5dbb4d0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x5d3b080, стало 0x5d3e190

### изменена: 0x5dbb510 (63 байт)
- код тот же, но вызывает другую функцию: было 0x5d3b050, стало 0x5d3e160

### изменена: 0x5dbb550 (63 байт)
- код тот же, но вызывает другую функцию: было 0x5d3b020, стало 0x5d3e130

### изменена: 0x5dbb590 (63 байт)
- код тот же, но вызывает другую функцию: было 0x5d3aff0, стало 0x5d3e100

### изменена: 0x5dbb5d0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x5d3afc0, стало 0x5d3e0d0

### изменена: 0x5dbb610 (63 байт)
- код тот же, но вызывает другую функцию: было 0x5d3af90, стало 0x5d3e0a0

### изменена: 0x5dbb650 (63 байт)
- код тот же, но вызывает другую функцию: было 0x5d3af60, стало 0x5d3e070

### изменена: 0x5dbb690 (63 байт)
- код тот же, но вызывает другую функцию: было 0x5d3af30, стало 0x5d3e040

### изменена: 0x5dbb6d0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x5d3af00, стало 0x5d3e010

### изменена: 0x5dbb710 (63 байт)
- код тот же, но вызывает другую функцию: было 0x5d3aed0, стало 0x5d3dfe0

### изменена: 0x5dbb750 (63 байт)
- код тот же, но вызывает другую функцию: было 0x5d3aea0, стало 0x5d3dfb0

### изменена: 0x5dbb790 (63 байт)
- код тот же, но вызывает другую функцию: было 0x5d3ae70, стало 0x5d3df80

### изменена: 0x5dbbca0 (111 байт) | строки: "GameTime_t"
- код тот же, но вызывает другую функцию: было 0x5d3b770, стало 0x5d3e880

### изменена: 0x5ddf110 (778 байт)
- код тот же, но вызывает другую функцию: было 0x5d8e9c0, стало 0x5d91c60

### изменена: 0x5de4870 (2934 байт)
- код тот же, но вызывает другую функцию: было 0x5d8b970, стало 0x5d8ec00

### изменена: 0x5e8d780 (807 байт)
- код тот же, но вызывает другую функцию: было 0x5d8e9b0, стало 0x5d91c50

### добавлена: 0x3e70c90 (98 байт) | строки: "R|x"

### добавлена: 0x4998980 (232 байт) CDOTA_Ability_LoneDruid_SpiritBear::vfunc#364 | строки: "item_ultimate_scepter"; "scepter_gained_cooldown"

### добавлена: 0x4d233b0 (253 байт) вызывается из: CDOTA_Modifier_Shredder_Reactive_Armor::vfunc#97

### добавлена: 0x4d234b0 (269 байт) вызывается из: CDOTA_Modifier_Shredder_Reactive_Armor::vfunc#97

### добавлена: 0x4fe6790 (559 байт) вызывается из: CDOTA_Modifier_Safety_Bubble::vfunc#97

### добавлена: 0x5d43a90 (132 байт) | строки: "CDOTA_Ability_Special_Bonus_HP_Regen_4_5"

### добавлена: 0x5f4ee10 (436 байт) | строки: "CDOTA_Ability_Special_Bonus_HP_Regen_4_5"

### удалена: 0x3e6df70 (183 байт) | строки: "?yx"

### удалена: 0x3e6e0a0 (183 байт) | строки: "Szx"

### удалена: 0x3e6e240 (98 байт) | строки: "f{x"

### удалена: 0x4d200b0 (2214 байт)

### удалена: 0x4fe2e80 (504 байт) вызывается из: CDOTA_Modifier_Safety_Bubble::vfunc#97

### копии существующего кода (29): шаблонные / склеенные компоновщиком функции, такой же код есть и в другой сборке — не новый код
- ещё одна копия существующего кода: 0x3e70a30 (183 байт)
- ещё одна копия существующего кода: 0x3e70b60 (183 байт)
- ещё одна копия существующего кода: 0x4cf11a0 (408 байт) вызывается из: CDOTA_Modifier_Winter_Wyvern_Winters_Curse_Aura::vfunc#97
- ещё одна копия существующего кода: 0x4d235c0 (1494 байт)
- ещё одна копия существующего кода: 0x4fe5550 (67 байт) CDOTA_Item_Seer_Stone::vfunc#50
- ещё одна копия существующего кода: 0x4fe55a0 (67 байт) CDOTA_Item_SerratedShiv::vfunc#50
- ещё одна копия существующего кода: 0x4fe55f0 (67 байт) CDOTA_Item_Recipe_Angels_Demise::vfunc#50
- ещё одна копия существующего кода: 0x4fe5640 (67 байт) CDOTA_Item_Angels_Demise::vfunc#50
- ещё одна копия существующего кода: 0x5d324f0 (8 байт) CDOTA_Ability_Special_Bonus_HP_Regen_80::GetIntrinsicModifierName | строки: "modifier_special_bonus_hp_regen"
- ещё одна копия существующего кода: 0x5d375f0 (8 байт) CDOTA_Ability_Special_Bonus_Unique_Mirana_7::vfunc#0
- ещё одна копия существующего кода: 0x5d37600 (1 байт) CDOTA_Ability_Special_Bonus_Unique_Mirana_7::vfunc#237
- ещё одна копия существующего кода: 0x5d37620 (6 байт) CDOTA_Modifier_Special_Bonus_Gold::IsHidden
- ещё одна копия существующего кода: 0x5d3fc10 (12 байт) CDOTASpectatorGraphManagerProxy::vfunc#49
- ещё одна копия существующего кода: 0x5d69e10 (15 байт) CDOTA_Ability_CDOTA_Ability_Special_Bonus_Unique_Muerta_TrickShotCharges::vfunc#5
- ещё одна копия существующего кода: 0x5d69e20 (45 байт) CDOTA_Ability_CDOTA_Ability_Special_Bonus_Unique_Muerta_TrickShotCharges::vfunc#6
- ещё одна копия существующего кода: 0x5d85280 (126 байт)
- ещё одна копия существующего кода: 0x5d8ba70 (1 байт)
- ещё одна копия существующего кода: 0x5d8ba80 (1 байт)
- ещё одна копия существующего кода: 0x5d91c60 (5 байт)
- ещё одна копия существующего кода: 0x5d91c70 (5 байт)
- ещё одна копия существующего кода: 0x5db97d0 (206 байт)
- ещё одна копия существующего кода: 0x5dd4b60 (92 байт) CDOTASpectatorGraphManagerProxy::vfunc#50
- одной копией существующего кода меньше: 0x49931fa (10 байт)
- одной копией существующего кода меньше: 0x4cede30 (408 байт) вызывается из: CDOTA_Modifier_Winter_Wyvern_Winters_Curse_Aura::vfunc#97
- одной копией существующего кода меньше: 0x4fe3310 (92 байт)
- одной копией существующего кода меньше: 0x4fe3370 (92 байт) CDOTA_Item_Pupils_gift::vfunc#50
- одной копией существующего кода меньше: 0x4fe33d0 (92 байт) CDOTA_Item_PyrrhicCloak::vfunc#50
- одной копией существующего кода меньше: 0x4fe3430 (92 байт) CDOTA_Item_Recipe_Quickening_Charm::vfunc#50
- одной копией существующего кода меньше: 0x5406f40 (182 байт) | строки: "CNetworkTransmitComponent::StateChanged(%s) @%s:%d"


## Строки библиотек

<details><summary>dota-bin/libclient.so: строки</summary>

**Добавлено — Имена из игры (модификаторы, способности, предметы, юниты, события) (1)**

```
special_bonus_hp_regen_4_5
```

**Добавлено — C++ классы (RTTI) (1)**

```
41C_DOTA_Ability_Special_Bonus_HP_Regen_4_5
```

**Добавлено — Прочие идентификаторы (3)**

```
CDOTA_Ability_Special_Bonus_HP_Regen_4_5
C_DOTA_Ability_Special_Bonus_HP_Regen_4_5
mark_range
```

</details>

<details><summary>dota-bin/libserver.so: строки</summary>

**Добавлено — Имена из игры (модификаторы, способности, предметы, юниты, события) (1)**

```
special_bonus_hp_regen_4_5
```

**Добавлено — C++ классы (RTTI) (1)**

```
40CDOTA_Ability_Special_Bonus_HP_Regen_4_5
```

**Добавлено — Прочие идентификаторы (4)**

```
CDOTA_Ability_Special_Bonus_HP_Regen_4_5
mark_range
scepter_gained_cooldown
thunderhide_slam_duration
```

</details>
