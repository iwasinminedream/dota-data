# Dota 6985: изменения кода по функциям

Снимки `6984-11257680` → `6985-11258601`; funcdiff.py. В диффе: [S:…] — строка, [K:…] — константа из данных, F — вызов другой функции, L — переход внутри функции, [D]/[T] — прочие адреса. Регистры и смещения стека меняются и от перекомпиляции.

## libclient.so: функций 281883 → 281886; без изменений 281867, изменено 16, добавлено 1, удалено 0

### изменена: 0x3bbfde0 (164 байт) | строки: "0nj"; "Release"; "client"
было: 0x3bbfce0 (164 байт)
- строки: +"0nj" −"0mj"
- инструкций: 34 → 34
```diff
@@ -1,5 +1,5 @@
 cmp edi, 6
 ja F
-lea rdx, [S:"0mj"]
+lea rdx, [S:"0nj"]
 mov edi, edi
 movsxd rax, dword ptr [rdx + rdi*4]
```

### изменена: 0x3bed760 (398 байт) | строки: "D1m"
было: 0x3bed660 (398 байт)
- строки: +"D1m" −"D0m"
- инструкций: 128 → 128
```diff
@@ -8,5 +8,5 @@
 movsxd r12, edx
 push rbx
-lea rdx, [S:"D0m"]
+lea rdx, [S:"D1m"]
 mov rbx, rsi
 sub rsp, 0x18
```

### изменена: 0x3c0e400 (753 байт) C_PlayerCosmeticPropClientside::vfunc#11 | строки: "playernumber"; "cosmetic_type"; "j7o"
было: 0x3c0e300 (753 байт)
- строки: +"j7o" −"j6o"
- инструкций: 197 → 197
```diff
@@ -103,5 +103,5 @@
 cmp al, 6
 ja L
-lea rdx, [S:"j6o"]
+lea rdx, [S:"j7o"]
 movzx eax, al
 movsxd rax, dword ptr [rdx + rax*4]
```

### изменена: 0x3c73550 (765 байт) CPointClientUIWorldTextPanelPreviewer::vfunc#2 | строки: "horizontal_align"; "(Wu"; "vertical_align"; "\\Vu"; "orientation"
было: 0x3c73450 (765 байт)
- строки: +"(Wu" +"\\Vu" −"(Vu" −"\\Uu"
- инструкций: 185 → 185
```diff
@@ -23,5 +23,5 @@
 cmp dl, 6
 ja L
-lea rcx, [S:"(Vu"]
+lea rcx, [S:"(Wu"]
 movzx edx, dl
 movsxd rdx, dword ptr [rcx + rdx*4]
@@ -53,5 +53,5 @@
 cmp dl, 6
 ja L
-lea rcx, [S:"\\Uu"]
+lea rcx, [S:"\\Vu"]
 movzx edx, dl
 movsxd rdx, dword ptr [rcx + rdx*4]
```

### изменена: 0x3c73870 (334 байт) | строки: "{Yu"
было: 0x3c73770 (334 байт)
- строки: +"{Yu" −"{Xu"
- инструкций: 82 → 82
```diff
@@ -6,5 +6,5 @@
 ja L
 push rbp
-lea rdx, [S:"{Xu"]
+lea rdx, [S:"{Yu"]
 mov edi, edi
 mov rbp, rsp
```

### изменена: 0x3c84e60 (397 байт) | строки: "<nv"
было: 0x3c84d60 (397 байт)
- строки: +"<nv" −"<mv"
- инструкций: 114 → 114
```diff
@@ -12,5 +12,5 @@
 punpcklqdq xmm0, xmm1
 ja L
-lea rdx, [S:"<mv"]
+lea rdx, [S:"<nv"]
 mov edi, edi
 mov rbx, rsi
```

### изменена: 0x3c85280 (1171 байт) | строки: " rv"; "C_BaseModelEntity"; "CHandle"; "C_NetworkUtlVectorBase"; "CUtlSymbolLarge"; "CUtlVector"
было: 0x3c85180 (1171 байт)
- строки: +" rv" −" qv"
- инструкций: 235 → 235
```diff
@@ -2,5 +2,5 @@
 ja L
 push rbp
-lea rdx, [S:" qv"]
+lea rdx, [S:" rv"]
 mov edi, edi
 mov rbp, rsp
```

### изменена: 0x3c90ac0 (542 байт) | строки: "|)w"
было: 0x3c909c0 (542 байт)
- строки: +"|)w" −"|(w"
- инструкций: 159 → 159
```diff
@@ -9,5 +9,5 @@
 movsxd r12, edx
 push rbx
-lea rdx, [S:"|(w"]
+lea rdx, [S:"|)w"]
 mov rbx, rsi
 sub rsp, 0x10
```

### изменена: 0x3cb4920 (2029 байт) | строки: "hGy"; "CGlobalSymbol"; "CAnimGraph2ParamOptionalRef"; "CTransform"; "e_choreo_outro_type"; "e_choreo_entry_type"; "t_choreo_exit_warp"; "t_choreo_target_warp"
было: 0x3cb4820 (2029 байт)
- строки: +"hGy" −"hFy"
- инструкций: 393 → 393
```diff
@@ -9,5 +9,5 @@
 cmp edi, 6
 ja F
-lea rdx, [S:"hFy"]
+lea rdx, [S:"hGy"]
 mov edi, edi
 mov rbx, rsi
```

### изменена: 0x3cc56d0 (1113 байт) CNetworkTransmitComponent::vfunc#3 | строки: "m_nTransmitStateOwnedCounter"; "|Wz"; "Unsupported KV3 basic type '%s' (%d)!"; "Pointers cannot be used as numeric values"
было: 0x3cc55d0 (1113 байт)
- строки: +"|Wz" −"|Vz"
- инструкций: 259 → 259
```diff
@@ -108,5 +108,5 @@
 cmp r8b, 6
 ja L
-lea rdx, [S:"|Vz"]
+lea rdx, [S:"|Wz"]
 movzx eax, r8b
 movsxd rax, dword ptr [rdx + rax*4]
```

### изменена: 0x3cd2fe0 (1127 байт) CHitboxComponent::vfunc#4 | строки: "m_flBoundsExpandRadius"; "X-{"; "<-{"; "Unsupported KV3 basic type '%s' (%d)!"; "Pointers cannot be used as numeric values"
было: 0x3cd2ee0 (1127 байт)
- строки: +"X-{" +"<-{" −"X,{" −"<,{"
- инструкций: 258 → 258
```diff
@@ -51,5 +51,5 @@
 cmp r8b, 6
 ja L
-lea rdx, [S:"X,{"]
+lea rdx, [S:"X-{"]
 movzx eax, r8b
 movsxd rax, dword ptr [rdx + rax*4]
@@ -108,5 +108,5 @@
 cmp r8b, 6
 ja L
-lea rdx, [S:"<,{"]
+lea rdx, [S:"<-{"]
 movzx eax, r8b
 movsxd rax, dword ptr [rdx + rax*4]
```

### изменена: 0x3d030c0 (183 байт) | строки: "+\t~"
было: 0x3d02fc0 (183 байт)
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

### изменена: 0x4ae57c0 (3 байт) CDOTA_Modifier_ChaosKnight_Armageddon_Phantasms::IsPurgable
было: 0x4ae56b0 (6 байт)
- числа в инструкциях: −1
- инструкций: 2 → 2
```diff
@@ -1,2 +1,2 @@
-mov eax, 1
+xor eax, eax
 ret
```

### изменена: 0x4b46190 (927 байт) CDOTA_Unit_Hero_AbyssalUnderlord::vfunc#149 | строки: "abyssal_underlord_dark_portal"; "minimum_distance"; "particles/ui_mouseactions/range_finder_tower_aoe.vpcf"
было: 0x4b46070 (1159 байт)
- константы из данных (числа логики): −-1,-1,3.402823e+38,3.402823e+38
- числа в инструкциях: −-1 −-1 −-2 −9 −0x3f −0x1ff −0x70 −0x7f7fffffffffffff (и ещё 8)
- поля объектов: −0xb1c −0xb1c −0x10
- прямых вызовов: 31 → 32
- инструкций: 245 → 207
```diff
@@ -1,10 +1,9 @@
 push rbp
 mov rbp, rsp
-push r14
 push r13
 push r12
 push rbx
 mov rbx, rdi
-sub rsp, 0x70
+sub rsp, 0x18
 call F
 mov rax, qword ptr [rbx]
@@ -27,5 +26,5 @@
 call F
 mov dword ptr [rbx + 0x209c], 0xffffffff
-lea rsp, [rbp - 0x20]
+lea rsp, [rbp - 0x18]
 mov rdi, rbx
 xor esi, esi
@@ -33,8 +32,7 @@
 pop r12
 pop r13
-pop r14
 pop rbp
 jmp F
-nop
+nop word ptr [rax + rax]
 mov ecx, dword ptr [r12 + 0xb1c]
 cmp ecx, -1
@@ -74,64 +72,30 @@
 cmp dword ptr [rbx + 0x209c], -1
 jne L
-mov edx, dword ptr [r12 + 0xb1c]
-cmp edx, -1
-je L
-mov rsi, qword ptr [D]
-test rsi, rsi
-je L
-cmp edx, -2
-je L
-movzx eax, word ptr [r12 + 0xb1c]
-mov rcx, rax
-shr rcx, 9
-and ecx, 0x3f
-mov rdi, qword ptr [rsi + rcx*8]
-test rdi, rdi
-je L
-and eax, 0x1ff
-imul rax, rax, 0x70
-add rax, rdi
-xor edi, edi
-cmp edx, dword ptr [rax + 0x10]
-jne L
+lea rdi, [r12 + 0xb1c]
+call F
+test rax, rax
+mov rdi, rax
+je L
 mov rdi, qword ptr [rax]
 movss xmm0, dword ptr [K:-1]
 lea rsi, [S:"minimum_distance"]
 xor edx, edx
-lea r12, [rbp - 0x90]
-call F
-mov r13d, eax
-call F
-movaps xmm0, xmmword ptr [K:-1,-1,3.402823e+38,3.402823e+38]
-mov rsi, r12
-mov dword ptr [rbp - 0x88], 2
-mov rdi, rax
-mov qword ptr [rbp - 0x80], rbx
-lea rax, [S:"particles/ui_mouseactions/range_finder_tower_aoe.vpcf"]
-movlps qword ptr [rbp - 0x54], xmm0
-mov qword ptr [rbp - 0x90], rax
-xor eax, eax
-mov word ptr [rbp - 0x58], ax
-movabs rax, 0x7f7fffffffffffff
-mov qword ptr [rbp - 0x30], rax
-movabs rax, 0x7f7fffff7f7fffff
-movhps qword ptr [rbp - 0x4c], xmm0
-mov qword ptr [rbp - 0x78], 0
-mov qword ptr [rbp - 0x70], 0
-mov dword ptr [rbp - 0x68], 0
-mov qword ptr [rbp - 0x60], 0
-mov byte ptr [rbp - 0x56], 0
-mov qword ptr [rbp - 0x44], 0x7f7fffff
-mov qword ptr [rbp - 0x38], 0
-mov qword ptr [rbp - 0x28], rax
+call F
+mov r12d, eax
+call F
+xor r8d, r8d
+mov rcx, rbx
+mov edx, 2
+lea rsi, [S:"particles/ui_mouseactions/range_finder_tower_aoe.vpcf"]
+mov rdi, rax
 call F
 mov dword ptr [rbx + 0x209c], eax
 call F
 mov rdi, rbx
-mov r14, rax
+mov r13, rax
 call F
 mov esi, dword ptr [rbx + 0x209c]
 xor edx, edx
-mov rdi, r14
+mov rdi, r13
 mov rcx, rax
 pxor xmm0, xmm0
@@ -165,10 +129,11 @@
 mov esi, dword ptr [rbx + 0x209c]
 pxor xmm0, xmm0
-cvtsi2ss xmm0, r13d
-mov rdi, rax
-mov rcx, r12
+cvtsi2ss xmm0, r12d
+lea r12, [rbp - 0x30]
+mov rdi, rax
 mov edx, 3
-mov qword ptr [rbp - 0x8c], 0x42c80000
```
(ещё 67 строк диффа: so-query.py fdiff libclient.so 0x4b46190)

### изменена: 0x4b477f0 (5500 байт)
было: 0x4b477c0 (5628 байт)
- поля объектов: −0x58
- прямых вызовов: 69 → 65
- инструкций: 933 → 898
```diff
@@ -1,6 +1,4 @@
 push rbp
 mov rbp, rsp
-push r13
-push r12
 push rbx
 sub rsp, 8
@@ -11,11 +9,8 @@
 test rax, rax
 je L
-add rsp, 8
-pop rbx
-pop r12
-pop r13
-pop rbp
-ret
-nop dword ptr [rax + rax]
+mov rbx, qword ptr [rbp - 8]
+leave
+ret
+nop word ptr [rax + rax]
 lea rbx, [D]
 mov rdi, rbx
@@ -76,5 +71,5 @@
 test rax, rax
 jne L
-nop word ptr cs:[rax + rax]
+nop
 movzx eax, byte ptr [D]
 test al, al
@@ -100,47 +95,17 @@
 movq xmm3, rax
 mov rax, rbx
+mov rbx, qword ptr [rbp - 8]
 punpcklqdq xmm0, xmm3
 movups xmmword ptr [D], xmm0
-add rsp, 8
-pop rbx
-pop r12
-pop r13
-pop rbp
-ret
-nop
-lea rbx, [D]
-mov rdi, rbx
-call F
-test eax, eax
-je L
-movzx eax, byte ptr [D]
-test al, al
-je L
-lea rax, [D]
-mov rdi, rbx
-mov qword ptr [D], rax
-call F
-jmp L
-lea r12, [D]
-mov rdi, r12
-call F
-test eax, eax
-je L
-movzx eax, byte ptr [D]
-test al, al
-je L
-lea rax, [D]
-mov rdi, r12
-mov qword ptr [D], rax
-call F
-jmp L
-lea r13, [D]
-mov rdi, r13
-call F
-test eax, eax
-je L
-call F
-mov rdi, r13
-mov rax, qword ptr [rax + 0x58]
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
 mov qword ptr [D], rax
 call F
```

### изменена: 0x5e2db40 (976 байт) вызывается из: C_DOTA_Unit_Hero_Rubick::vfunc#538, CDOTA_ParticleManager::vfunc#9, C_DOTAWearableItem::vfunc#304
было: 0x5e2da90 (1088 байт)
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

### добавлена: 0x4afcc20 (29 байт) C_DOTA_Ability_ChaosKnight_Phantasm::vfunc#358 | строки: "chaos_knight_armageddon;chaos_knight_armageddons_flank_end"

### копии существующего кода (2): шаблонные / склеенные компоновщиком функции, такой же код есть и в другой сборке — не новый код
- ещё одна копия существующего кода: 0x4ae6050 (3 байт) CDOTA_Ability_Chaos_Knight_ArmageddonsFlank_End::vfunc#345
- ещё одна копия существующего кода: 0x5e2dab0 (112 байт) вызывается из: C_DOTA_Unit_Hero_Rubick::vfunc#538, CDOTA_ParticleManager::vfunc#9, CDOTAGCClientSystem::vfunc#1

## libserver.so: функций 221929 → 221926; без изменений 221827, изменено 93, добавлено 2, удалено 5

### изменена: 0x3bf7500 (808 байт) вызывается из: CDOTA_NPCSpawnerGoodTop::vfunc#22, CDOTA_Ability_Lua::vfunc#355, CDOTA_Ability_Lua::vfunc#381 | строки: "Y;R"; "%g %g %g"; "%g %g %g %g"; "(null)"; "false"; "true"; "%llu"; "%lld"
было: 0x3bf74c0 (808 байт)
- строки: +"Y;R"
- инструкций: 203 → 203
```diff
@@ -36,5 +36,5 @@
 cmp al, 0x4f
 ja L
-lea rcx, [D]
+lea rcx, [S:"Y;R"]
 movzx edx, al
 movsxd rdx, dword ptr [rcx + rdx*4]
```

### изменена: 0x3bf8f60 (238 байт)
было: 0x3bf8f20 (238 байт)
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

### изменена: 0x3bfac00 (323 байт) | строки: "CUtlSymbolLarge"; "CNetworkUtlVectorBase"
было: 0x3bfabc0 (323 байт)
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

### изменена: 0x3bfadb0 (317 байт)
было: 0x3bfad70 (317 байт)
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

### изменена: 0x3c275e0 (1047 байт) | строки: "7#U"; "Unsupported KV3 basic type '%s' (%d)!"; "Pointers cannot be used as numeric values"
было: 0x3c275a0 (1047 байт)
- строки: +"7#U"
- инструкций: 245 → 245
```diff
@@ -47,5 +47,5 @@
 cmp r8b, 6
 ja L
-lea rcx, [D]
+lea rcx, [S:"7#U"]
 movzx edx, r8b
 movsxd rdx, dword ptr [rcx + rdx*4]
```

### изменена: 0x3c27a00 (1047 байт) | строки: ";'U"; "Unsupported KV3 basic type '%s' (%d)!"; "Pointers cannot be used as numeric values"
было: 0x3c279c0 (1047 байт)
- строки: +";'U"
- инструкций: 245 → 245
```diff
@@ -47,5 +47,5 @@
 cmp r8b, 6
 ja L
-lea rcx, [D]
+lea rcx, [S:";'U"]
 movzx edx, r8b
 movsxd rdx, dword ptr [rcx + rdx*4]
```

### изменена: 0x3c27e20 (1047 байт) | строки: "?+U"; "Unsupported KV3 basic type '%s' (%d)!"; "Pointers cannot be used as numeric values"
было: 0x3c27de0 (1047 байт)
- строки: +"?+U"
- инструкций: 245 → 245
```diff
@@ -47,5 +47,5 @@
 cmp r8b, 6
 ja L
-lea rcx, [D]
+lea rcx, [S:"?+U"]
 movzx edx, r8b
 movsxd rdx, dword ptr [rcx + rdx*4]
```

### изменена: 0x3c28240 (1047 байт) | строки: "C/U"; "Unsupported KV3 basic type '%s' (%d)!"; "Pointers cannot be used as numeric values"
было: 0x3c28200 (1047 байт)
- строки: +"C/U"
- инструкций: 245 → 245
```diff
@@ -47,5 +47,5 @@
 cmp r8b, 6
 ja L
-lea rcx, [D]
+lea rcx, [S:"C/U"]
 movzx edx, r8b
 movsxd rdx, dword ptr [rcx + rdx*4]
```

### изменена: 0x3c28660 (1047 байт) | строки: "G3U"; "Unsupported KV3 basic type '%s' (%d)!"; "Pointers cannot be used as numeric values"
было: 0x3c28620 (1047 байт)
- строки: +"G3U"
- инструкций: 245 → 245
```diff
@@ -47,5 +47,5 @@
 cmp r8b, 6
 ja L
-lea rcx, [D]
+lea rcx, [S:"G3U"]
 movzx edx, r8b
 movsxd rdx, dword ptr [rcx + rdx*4]
```

### изменена: 0x3c28a80 (1047 байт) | строки: "K7U"; "Unsupported KV3 basic type '%s' (%d)!"; "Pointers cannot be used as numeric values"
было: 0x3c28a40 (1047 байт)
- строки: +"K7U"
- инструкций: 245 → 245
```diff
@@ -47,5 +47,5 @@
 cmp r8b, 6
 ja L
-lea rcx, [D]
+lea rcx, [S:"K7U"]
 movzx edx, r8b
 movsxd rdx, dword ptr [rcx + rdx*4]
```

### изменена: 0x3c29800 (1047 байт) | строки: "Unsupported KV3 basic type '%s' (%d)!"; "Pointers cannot be used as numeric values"
было: 0x3c297c0 (1047 байт)
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

### изменена: 0x3c29c20 (1047 байт) | строки: "Unsupported KV3 basic type '%s' (%d)!"; "Pointers cannot be used as numeric values"
было: 0x3c29be0 (1047 байт)
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

### изменена: 0x3c2b530 (951 байт) | строки: "IKV3TransferInterface_GameTime_Load"
было: 0x3c2b4f0 (951 байт)
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

### изменена: 0x3c6a3e0 (715 байт) CDOTA_NPCSpawnerGoodTop::vfunc#51, CDOTA_NPCSpawnerGoodMid::vfunc#51, CDOTA_NPCSpawnerGoodBot::vfunc#51 | строки: "disableshadows"; "7-Y"; "disablereceiveshadows"; "ownername"; "O-Y"
было: 0x3c6a3a0 (715 байт)
- строки: +"7-Y" +"O-Y"
- инструкций: 189 → 189
```diff
@@ -25,5 +25,5 @@
 cmp dl, 6
 ja L
-lea rcx, [D]
+lea rcx, [S:"7-Y"]
 movzx edx, dl
 movsxd rdx, dword ptr [rcx + rdx*4]
@@ -126,5 +126,5 @@
 cmp dl, 6
 ja L
-lea rcx, [D]
+lea rcx, [S:"O-Y"]
 movzx edx, dl
 movsxd rdx, dword ptr [rcx + rdx*4]
```

### изменена: 0x3c6d1c0 (1027 байт) | строки: "CEntityIOOutput"; "CBaseFilter"; "CHandle"
было: 0x3c6d180 (1027 байт)
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

### изменена: 0x3c6e4e0 (653 байт) | строки: "%g %g %g"; "(null)"; "%g %g %g %g"; "%lld"; "%llu"; "%d %d %d %d"; "false"; "true"
было: 0x3c6e4a0 (653 байт)
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

### изменена: 0x3c8a710 (478 байт) | строки: ".-["
было: 0x3c8a6d0 (478 байт)
- строки: +".-["
- инструкций: 116 → 116
```diff
@@ -8,5 +8,5 @@
 cmp dil, 0x4f
 ja L
-lea rdx, [D]
+lea rdx, [S:".-["]
 movzx eax, dil
 movsxd rax, dword ptr [rdx + rax*4]
```

### изменена: 0x3cc0090 (2479 байт) CBaseLightProbeVolume::vfunc#2 | строки: "box_mins"; "box_maxs"; "moveable"; "handshake"; "@n^"; "indoor_outdoor_level"; "StartDisabled"; "is_selected_in_hammer"
было: 0x3cc0050 (2479 байт)
- строки: +"@n^" +"nm^" −"rm^" −"{m^" −"mm^" −"Xm^" −".m^"
- инструкций: 618 → 618
```diff
@@ -71,5 +71,5 @@
 cmp dl, 6
 ja L
-lea rcx, [D]
+lea rcx, [S:"@n^"]
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
+lea rcx, [S:"nm^"]
 movzx edx, dl
 movsxd rdx, dword ptr [rcx + rdx*4]
```

### изменена: 0x3d22ca0 (1712 байт) CEntityOutputTemplate<SndOpEventGuid_t>::vfunc#2 | строки: "m_Value"; "Stack depth limit hit (%d)"; "qPd"; "public.aabb_min"; "public.aabb_max"
было: 0x3d22c60 (1712 байт)
- строки: +"qPd" −"pPd" −"1Pd"
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
+lea rdx, [S:"qPd"]
 movzx eax, al
 movsxd rax, dword ptr [rdx + rax*4]
```

### изменена: 0x3d302e0 (637 байт) | строки: "CInfoFan"; "CHandle"; "VectorWS"
было: 0x3d302a0 (637 байт)
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

### изменена: 0x3d30760 (547 байт) | строки: "x'e"; "CHandle"; "CBasePlayerController"; "CNetworkUtlVectorBase"; "CBasePlayerPawn"
было: 0x3d30720 (547 байт)
- строки: +"x'e" −"8'e"
- инструкций: 158 → 158
```diff
@@ -2,5 +2,5 @@
 ja L
 push rbp
-lea rdx, [S:"8'e"]
+lea rdx, [S:"x'e"]
 mov edi, edi
 mov rbp, rsp
```

### изменена: 0x3d51a00 (117 байт) | строки: "y g"
было: 0x3d519c0 (117 байт)
- строки: +"y g" −"9 g"
- инструкций: 39 → 39
```diff
@@ -2,5 +2,5 @@
 cmp edx, 6
 ja L
-lea rcx, [S:"9 g"]
+lea rcx, [S:"y g"]
 push rbp
 mov rdi, rsi
```

### изменена: 0x3d51a80 (561 байт) | строки: "Unsupported KV3 basic type '%s' (%d)!"; "Pointers cannot be used as numeric values"
было: 0x3d51a40 (561 байт)
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

### изменена: 0x3d51d80 (227 байт) | строки: "IPhysicsJoint"
было: 0x3d51d40 (227 байт)
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

### изменена: 0x3d528a0 (339 байт) | строки: "D.g"; "VPhysicsCollisionAttribute_t"; "SolidType_t"; "SurroundingBoundsType_t"
было: 0x3d52860 (339 байт)
- строки: +"D.g"
- инструкций: 99 → 99
```diff
@@ -2,5 +2,5 @@
 ja L
 push rbp
-lea rdx, [D]
+lea rdx, [S:"D.g"]
 mov edi, edi
 mov rbp, rsp
```

### изменена: 0x3d52ac0 (499 байт) | строки: "P0g"; "GameTime_t"; "BeamType_t"; "CBaseEntity"; "CHandle"; "AttachmentHandle_t"; "VectorWS"
было: 0x3d52a80 (499 байт)
- строки: +"P0g"
- инструкций: 135 → 135
```diff
@@ -2,5 +2,5 @@
 ja L
 push rbp
-lea rdx, [D]
+lea rdx, [S:"P0g"]
 mov edi, edi
 mov rbp, rsp
```

### изменена: 0x3d52eb0 (285 байт) | строки: "VectorWS"
было: 0x3d52e70 (285 байт)
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

### изменена: 0x3d53110 (893 байт) | строки: "InfoForResourceTypeIParticleSystemDefinition"; "CWeakHandle"; "CResourceNameTyped"; "ParticleAttachment_t"; "PrecipitationFilter_t"
было: 0x3d530d0 (893 байт)
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

### изменена: 0x3d62080 (785 байт) | строки: "Z%h"; "Unsupported KV3 basic type '%s' (%d)!"; "Pointers cannot be used as numeric values"
было: 0x3d62040 (785 байт)
- строки: +"Z%h"
- инструкций: 219 → 219
```diff
@@ -20,5 +20,5 @@
 cmp bl, 6
 ja L
-lea rdx, [D]
+lea rdx, [S:"Z%h"]
 movzx eax, bl
 movsxd rax, dword ptr [rdx + rax*4]
```

### изменена: 0x3d85110 (243 байт) | строки: "h1j"; "VectorWS"
было: 0x3d850d0 (243 байт)
- строки: +"h1j" −"(1j"
- инструкций: 67 → 67
```diff
@@ -1,5 +1,5 @@
 cmp edi, 6
 ja L
-lea rdx, [S:"(1j"]
+lea rdx, [S:"h1j"]
 mov edi, edi
 push rbp
```

### изменена: 0x3d85210 (227 байт) | строки: "T2j"; "VectorWS"
было: 0x3d851d0 (227 байт)
- строки: +"T2j"
- инструкций: 74 → 74
```diff
@@ -1,5 +1,5 @@
 cmp edi, 6
 ja L
-lea rcx, [D]
+lea rcx, [S:"T2j"]
 mov edi, edi
 push rbp
```

### изменена: 0x3d85300 (339 байт) | строки: "(3j"; "BASEPTR"; "GameTick_t"
было: 0x3d852c0 (339 байт)
- строки: +"(3j"
- инструкций: 90 → 90
```diff
@@ -1,5 +1,5 @@
 cmp edi, 6
 ja L
-lea rdx, [D]
+lea rdx, [S:"(3j"]
 mov edi, edi
 push rbp
```

### изменена: 0x3d85c70 (243 байт) | строки: "|<j"; "VectorWS"
было: 0x3d85c30 (243 байт)
- строки: +"|<j" −"<<j"
- инструкций: 76 → 76
```diff
@@ -2,5 +2,5 @@
 ja L
 push rbp
-lea rdx, [S:"<<j"]
+lea rdx, [S:"|<j"]
 mov edi, edi
 mov rbp, rsp
```

### изменена: 0x3d86080 (371 байт) | строки: "\\@j"; "GameTime_t"; "CBaseEntity"; "CHandle"
было: 0x3d86040 (371 байт)
- строки: +"\\@j"
- инструкций: 112 → 112
```diff
@@ -2,5 +2,5 @@
 ja L
 push rbp
-lea rdx, [D]
+lea rdx, [S:"\\@j"]
 mov edi, edi
 mov rbp, rsp
```

### изменена: 0x3d86680 (183 байт)
было: 0x3d86640 (183 байт)
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

### изменена: 0x3d867b0 (98 байт) | строки: "bGj"
было: 0x3d86770 (98 байт)
- строки: +"bGj" −"\"Gj"
- инструкций: 36 → 36
```diff
@@ -2,5 +2,5 @@
 cmp edx, 6
 ja L
-lea rcx, [S:"\"Gj"]
+lea rcx, [S:"bGj"]
 push rbp
 mov rdi, rsi
```

### изменена: 0x3d86820 (98 байт)
было: 0x3d867e0 (98 байт)
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

### изменена: 0x3d86a00 (117 байт) | строки: "qIj"
было: 0x3d869c0 (117 байт)
- строки: +"qIj" −"1Ij"
- инструкций: 39 → 39
```diff
@@ -2,5 +2,5 @@
 cmp edx, 6
 ja L
-lea rcx, [S:"1Ij"]
+lea rcx, [S:"qIj"]
 push rbp
 mov rdi, rsi
```

### изменена: 0x3d86c50 (136 байт)
было: 0x3d86c10 (136 байт)
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

### изменена: 0x3d87cb0 (206 байт) | строки: "?\\j"
было: 0x3d87c70 (206 байт)
- строки: +"?\\j"
- инструкций: 62 → 62
```diff
@@ -2,5 +2,5 @@
 ja L
 push rbp
-lea rdx, [D]
+lea rdx, [S:"?\\j"]
 mov edi, edi
 mov rbp, rsp
```

### изменена: 0x3d880c0 (222 байт) | строки: "'`j"
было: 0x3d88080 (222 байт)
- строки: +"'`j"
- инструкций: 64 → 64
```diff
@@ -2,5 +2,5 @@
 ja L
 push rbp
-lea rdx, [D]
+lea rdx, [S:"'`j"]
 mov edi, edi
 mov rbp, rsp
```

### изменена: 0x3d882a0 (435 байт) | строки: "Xaj"; "CTransform"; "CNetworkUtlVectorBase"
было: 0x3d88260 (435 байт)
- строки: +"Xaj"
- инструкций: 118 → 118
```diff
@@ -1,5 +1,5 @@
 cmp edi, 6
 ja L
-lea rdx, [D]
+lea rdx, [S:"Xaj"]
 mov edi, edi
 push rbp
```

### изменена: 0x3d88510 (302 байт) | строки: "sdj"
было: 0x3d884d0 (302 байт)
- строки: +"sdj" −"3dj"
- инструкций: 71 → 71
```diff
@@ -2,5 +2,5 @@
 ja L
 push rbp
-lea rdx, [S:"3dj"]
+lea rdx, [S:"sdj"]
 mov edi, edi
 mov rbp, rsp
```

### изменена: 0x3d889e0 (811 байт) | строки: "Xhj"
было: 0x3d889a0 (811 байт)
- строки: +"Xhj"
- инструкций: 232 → 232
```diff
@@ -9,5 +9,5 @@
 movsxd r13, edx
 push r12
-lea rdx, [D]
+lea rdx, [S:"Xhj"]
 mov r12d, ecx
 push rbx
```

### изменена: 0x3d88d20 (907 байт)
было: 0x3d88ce0 (907 байт)
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

### изменена: 0x3d89b90 (435 байт) | строки: "CPlayerSlot"; "CUtlVector"
было: 0x3d89b50 (435 байт)
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

### изменена: 0x3d954f0 (659 байт) | строки: "CTakeDamageInfo"; "DestructiblePartDamageRequest_t"; "CUtlLeanVector"; "VectorWS"; "TakeDamageFlags_t"; "HitGroup_t"
было: 0x3d954b0 (659 байт)
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

### изменена: 0x3d95790 (659 байт) | строки: "84k"; "CTakeDamageInfo"; "CTakeDamageResult"
было: 0x3d95750 (659 байт)
- строки: +"84k"
- инструкций: 126 → 126
```diff
@@ -2,5 +2,5 @@
 ja L
 push rbp
-lea rdx, [D]
+lea rdx, [S:"84k"]
 mov edi, edi
 mov rbp, rsp
```

### изменена: 0x3d95dc0 (563 байт) | строки: "H:k"; "CUtlVector"; "VectorWS"; "GameTime_t"
было: 0x3d95d80 (563 байт)
- строки: +"H:k"
- инструкций: 157 → 157
```diff
@@ -2,5 +2,5 @@
 ja L
 push rbp
-lea rdx, [D]
+lea rdx, [S:"H:k"]
 mov edi, edi
 mov rbp, rsp
```

### изменена: 0x3d98d10 (4083 байт) вызывается из: CTakeDamageInfo::vfunc#2 | строки: "m_vecDamageForce"; "m_bitsDamageType"; "+mk"; "m_vecDamagePosition"; "m_vecReportedPosition"; "m_vecDamageDirection"; "m_hInflictor"; "m_hAttacker"
было: 0x3d98cd0 (4083 байт)
- строки: +"+mk" +"6wk"
- инструкций: 886 → 886
```diff
@@ -113,5 +113,5 @@
 cmp r8b, 6
 ja L
-lea rdx, [D]
+lea rdx, [S:"+mk"]
 movzx eax, r8b
 movsxd rax, dword ptr [rdx + rax*4]
@@ -362,5 +362,5 @@
 cmp r8b, 6
 ja L
-lea rdx, [D]
+lea rdx, [S:"6wk"]
 movzx eax, r8b
 movsxd rax, dword ptr [rdx + rax*4]
```

### изменена: 0x3da49c0 (414 байт) | строки: "P%l"
было: 0x3da4980 (414 байт)
- строки: +"P%l"
- инструкций: 136 → 136
```diff
@@ -8,5 +8,5 @@
 movsxd r12, edx
 push rbx
-lea rdx, [D]
+lea rdx, [S:"P%l"]
 mov rbx, rsi
 sub rsp, 0x18
```

### изменена: 0x3da55e0 (542 байт) | строки: "01l"
было: 0x3da55a0 (542 байт)
- строки: +"01l"
- инструкций: 159 → 159
```diff
@@ -9,5 +9,5 @@
 movsxd r12, edx
 push rbx
-lea rdx, [D]
+lea rdx, [S:"01l"]
 mov rbx, rsi
 sub rsp, 0x10
```

### изменена: 0x3daa830 (961 байт) | строки: "Byl"; "%g %g %g"; "(null)"; "%g %g %g %g"; "unknown_variant_type"; "qyl"; "%lld"; "%llu"
было: 0x3daa7f0 (961 байт)
- строки: +"Byl" +"qyl" −"1yl"
- инструкций: 213 → 213
```diff
@@ -7,5 +7,5 @@
 cmp al, 0x4f
 ja L
-lea rcx, [D]
+lea rcx, [S:"Byl"]
 movzx edx, al
 movsxd rdx, dword ptr [rcx + rdx*4]
@@ -91,5 +91,5 @@
 cmp al, 0x47
 ja L
-lea rdx, [S:"1yl"]
+lea rdx, [S:"qyl"]
 movzx eax, al
 movsxd rax, dword ptr [rdx + rax*4]
```

### изменена: 0x3db8470 (851 байт) | строки: "|Tm"; "%llu"
было: 0x3db8430 (851 байт)
- строки: +"|Tm" −"<Tm"
- инструкций: 190 → 190
```diff
@@ -21,5 +21,5 @@
 mov rbx, rax
 je L
-lea r13, [S:"<Tm"]
+lea r13, [S:"|Tm"]
 nop dword ptr [rax + rax]
 mov qword ptr [rbp - 0xc0], 0
```

### изменена: 0x3db8c80 (819 байт) | строки: "$Zm"; "DecalFlags_t"; "GameTime_t"
было: 0x3db8c40 (819 байт)
- строки: +"$Zm"
- инструкций: 143 → 143
```diff
@@ -2,5 +2,5 @@
 ja L
 push rbp
-lea rdx, [D]
+lea rdx, [S:"$Zm"]
 mov edi, edi
 mov rbp, rsp
```

### изменена: 0x3df7860 (350 байт) | строки: "_-q"
было: 0x3df7820 (350 байт)
- строки: +"_-q"
- инструкций: 92 → 92
```diff
@@ -2,5 +2,5 @@
 ja L
 push rbp
-lea rdx, [D]
+lea rdx, [S:"_-q"]
 mov edi, edi
 mov rbp, rsp
```

### изменена: 0x3df7a40 (407 байт) вызывается из: CVScriptGameSystem::vfunc#85
было: 0x3df7a00 (407 байт)
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

### изменена: 0x3df96e0 (547 байт) | строки: "CHandle"; "CEnvSoundscapeTriggerable"; "CBasePlayerPawn"; "CUtlVector"
было: 0x3df96a0 (547 байт)
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

### изменена: 0x3dfc190 (502 байт) | строки: "4uq"
было: 0x3dfc150 (502 байт)
- строки: +"4uq"
- инструкций: 139 → 139
```diff
@@ -21,5 +21,5 @@
 cmp al, 0x24
 ja L
-lea rcx, [D]
+lea rcx, [S:"4uq"]
 movzx eax, al
 movsxd rax, dword ptr [rcx + rax*4]
```

### изменена: 0x3e1a9c0 (4702 байт) | строки: "classname"; "connections"; "attributes"; "X\\s"
было: 0x3e1a980 (4702 байт)
- строки: +"X\\s" −"PWs" −"X]s"
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
+lea rsi, [S:"X\\s"]
 movzx edx, al
 movsxd rdx, dword ptr [rsi + rdx*4]
```

### изменена: 0x3e2b9a0 (542 байт) | строки: "D[t"
было: 0x3e2b960 (542 байт)
- строки: +"D[t"
- инструкций: 159 → 159
```diff
@@ -9,5 +9,5 @@
 movsxd r12, edx
 push rbx
-lea rdx, [D]
+lea rdx, [S:"D[t"]
 mov rbx, rsi
 sub rsp, 0x10
```

### изменена: 0x3e6cc00 (187 байт) | строки: "Disposition_t"
было: 0x3e6cbc0 (187 байт)
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

### изменена: 0x3e6cdf0 (275 байт) | строки: "VectorWS"
было: 0x3e6cdb0 (275 байт)
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

### изменена: 0x3e6cfb0 (243 байт) | строки: " ]x"; "VectorWS"
было: 0x3e6cf70 (243 байт)
- строки: +" ]x"
- инструкций: 70 → 70
```diff
@@ -1,5 +1,5 @@
 cmp edi, 6
 ja L
-lea rdx, [D]
+lea rdx, [S:" ]x"]
 mov edi, edi
 push rbp
```

### изменена: 0x3e6da00 (451 байт) | строки: "dgx"; "CEconWearable"; "CHandle"; "CNetworkUtlVectorBase"; "RelationshipOverride_t"; "CUtlVector"; "Hull_t"; "CMovementStatsProperty"
было: 0x3e6d9c0 (451 байт)
- строки: +"dgx" −"$gx"
- инструкций: 129 → 129
```diff
@@ -2,5 +2,5 @@
 ja L
 push rbp
-lea rdx, [S:"$gx"]
+lea rdx, [S:"dgx"]
 mov edi, edi
 mov rbp, rsp
```

### изменена: 0x3e6f030 (187 байт) | строки: "S}x"
было: 0x3e6eff0 (187 байт)
- строки: +"S}x"
- инструкций: 52 → 52
```diff
@@ -3,5 +3,5 @@
 ja L
 push rbp
-lea rcx, [D]
+lea rcx, [S:"S}x"]
 mov rdi, rsi
 mov rbp, rsp
```

### изменена: 0x3e6f0f0 (171 байт) | строки: "HitGroup_t"
было: 0x3e6f0b0 (171 байт)
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

### изменена: 0x3e6f1a0 (133 байт) | строки: "U~x"
было: 0x3e6f160 (133 байт)
- строки: +"U~x"
- инструкций: 41 → 41
```diff
@@ -2,5 +2,5 @@
 cmp edx, 6
 ja L
-lea rcx, [D]
+lea rcx, [S:"U~x"]
 push rbp
 mov rdi, rsi
```

### изменена: 0x3eaa4e0 (769 байт) вызывается из: CAnimGraphControllerBase::vfunc#2, CEmptyGraphController::vfunc#2, EventGrantDefinition_Emoticon_t::vfunc#2 | строки: "b-|"; "Unsupported KV3 basic type '%s' (%d)!"; "Pointers cannot be used as numeric values"
было: 0x3eaa4a0 (769 байт)
- строки: +"b-|" −"\"-|"
- инструкций: 220 → 220
```diff
@@ -31,5 +31,5 @@
 cmp bl, 6
 ja L
-lea rdx, [S:"\"-|"]
+lea rdx, [S:"b-|"]
 movzx eax, bl
 movsxd rax, dword ptr [rdx + rax*4]
```

### изменена: 0x3eace50 (856 байт)
было: 0x3eacab0 (856 байт)
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

### изменена: 0x3eaeb00 (904 байт) | строки: "xp|"
было: 0x3eaeac0 (904 байт)
- строки: +"xp|" −"8p|"
- инструкций: 237 → 237
```diff
@@ -7,5 +7,5 @@
 mov r15d, edx
 push r14
-lea rdx, [S:"8p|"]
+lea rdx, [S:"xp|"]
 push r13
 push r12
```

### изменена: 0x3eca420 (904 байт) | строки: "()~"
было: 0x3eca3e0 (904 байт)
- строки: +"()~"
- инструкций: 238 → 238
```diff
@@ -7,5 +7,5 @@
 mov r15d, edx
 push r14
-lea rdx, [D]
+lea rdx, [S:"()~"]
 push r13
 push r12
```

### изменена: 0x4744a50 (740 байт) вызывается из: CDOTA_Modifier_Venomancer_Snakebite::vfunc#97 | строки: "luna_lunar_orbit"; "luna_moon_glaive"; "particles/units/heroes/hero_venomancer/venomancer_snakebite_dmg.vpcf"; "attach_hitloc"; "Hero_Venomancer.Snakebite.Punish"; "<NoAbilityName>"
было: 0x4744a10 (669 байт)
- строки: +"luna_moon_glaive" +"<NoAbilityName>"
- прямых вызовов: 21 → 22
- инструкций: 174 → 186
```diff
@@ -68,14 +68,23 @@
 test rax, rax
 je L
-mov rdi, qword ptr [rax]
-test rdi, rdi
+mov r13, qword ptr [rax]
+test r13, r13
 je L
 lea rsi, [S:"luna_lunar_orbit"]
-cmp rdi, rsi
+cmp r13, rsi
 je L
+mov rdi, r13
 call F
 test eax, eax
 je L
-nop
+nop dword ptr [rax]
+lea rax, [D]
+test r13, r13
+cmovne rax, r13
+mov rdi, rax
+lea rsi, [S:"luna_moon_glaive"]
+call F
+test al, al
+jne L
 cmp byte ptr [r12 + 0x1b1c], 0
 jne L
@@ -173,2 +182,5 @@
 pop rdx
 jmp L
+nop word ptr [rax + rax]
+lea rdi, [S:"<NoAbilityName>"]
+jmp L
```

### изменена: 0x47816b0 (1043 байт) CDOTA_Ability_WitchDoctor_DeathWard::vfunc#156 | строки: "CNetworkTransmitComponent::StateChanged(%s) @%s:%d"
было: 0x47815f0 (579 байт)
- константы из данных (числа логики): +-1 +5
- числа в инструкциях: +-1 +-2 +9 +0x3f +0x1ff +0x70 +0 +0 (и ещё 9)
- виртуальные вызовы: +0xf0 (слот 30)
- поля объектов: +0x85c +0x85c +0x85c +0x10 +0x10 +0x10 +0x870 +0x870 +0x870 +0x38 +0x38 +0x5d1
- прямых вызовов: 8 → 17
- инструкций: 116 → 223
```diff
@@ -1,2 +1,109 @@
+push rbp
+mov rbp, rsp
+push r13
+push r12
+push rbx
+mov rbx, rdi
+sub rsp, 0x58
+call F
+mov ecx, dword ptr [rbx + 0x85c]
+cmp ecx, -1
+je L
+cmp ecx, -2
+mov rsi, qword ptr [D]
+je L
+test rsi, rsi
+je L
+movzx eax, word ptr [rbx + 0x85c]
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
+cmp qword ptr [rax], 0
+je L
+movss xmm1, dword ptr [rbx + 0x870]
+pxor xmm0, xmm0
+comiss xmm1, xmm0
+jp L
+je L
+jbe L
+mov rax, qword ptr [rbx + 0x10]
+mov edi, dword ptr [rax + 0x38]
+call F
+comiss xmm0, dword ptr [rbx + 0x870]
+jp L
+je L
+jbe L
+lea r12, [rbx + 0x85c]
+mov rdi, r12
+call F
+test rax, rax
+je L
+mov rdi, qword ptr [rax]
+test rdi, rdi
+je L
+cmp byte ptr [rdi + 0x5d1], 3
+jne L
```
(ещё 56 строк диффа: so-query.py fdiff libserver.so 0x47816b0)

### изменена: 0x4787f60 (949 байт) CDOTA_Unit_TargetDummy::vfunc#263
было: 0x4790440 (965 байт)
- числа в инструкциях: −1 −1
- инструкций: 202 → 203
```diff
@@ -4,4 +4,5 @@
 mov edx, 8
 mov rbp, rsp
+push r14
 push r13
 push r12
@@ -10,5 +11,5 @@
 push rbx
 mov rbx, rdi
-sub rsp, 0x58
+sub rsp, 0x60
 mov rax, qword ptr [rdi]
 movss xmm1, dword ptr [K:-999]
@@ -52,5 +53,5 @@
 mov rdi, rbx
 call F
-add rsp, 0x58
+add rsp, 0x60
 mov rsi, r12
 mov rdi, rbx
@@ -58,4 +59,5 @@
 pop r12
 pop r13
+pop r14
 pop rbp
 jmp F
@@ -67,35 +69,34 @@
 jp L
 je L
+lea r13, [rbp - 0x58]
 xor edx, edx
-mov esi, 1
-movss dword ptr [rbp - 0x64], xmm0
 pxor xmm1, xmm1
-lea rdi, [rbp - 0x50]
+movss dword ptr [rbp - 0x74], xmm0
+lea rsi, [rbp - 0x64]
+mov rdi, r13
 movaps xmmword ptr [rbp - 0x40], xmm1
 mov word ptr [rbp - 0x24], dx
-lea r13, [rbp - 0x60]
-mov qword ptr [rbp - 0x60], 1
-mov qword ptr [rbp - 0x58], 0
-mov qword ptr [rbp - 0x50], 0
-mov qword ptr [rbp - 0x48], 0
-mov qword ptr [rbp - 0x30], 0xffffffffffffffff
-mov dword ptr [rbp - 0x28], 0xffffffff
-call F
-mov rax, qword ptr [rbp - 0x50]
-mov rsi, r13
-mov rdi, rbx
-add dword ptr [rbp - 0x58], 1
-mov dword ptr [rax], 0x2398
-mov rax, qword ptr [rbx]
```
(ещё 90 строк диффа: so-query.py fdiff libserver.so 0x4787f60)

### изменена: 0x47a4da0 (3374 байт) CDOTA_RoshanSpawner::vfunc#237 | строки: "Unit"; "UseNeutralCreepBehavior"; "npc_dota_roshan"; "particles/neutral_fx/roshan_timer.vpcf"
было: 0x47a4d20 (3310 байт)
- числа в инструкциях: +-1 +-2 +9 +0x3f +0x1ff +0x70
- поля объектов: +0x10 +0x794 +0x794
- прямых вызовов: 76 → 75
- инструкций: 648 → 665
```diff
@@ -9,6 +9,6 @@
 push rbx
 sub rsp, 0xd8
-lea r14, [D]
-mov rdx, qword ptr [r14]
+lea r15, [D]
+mov rdx, qword ptr [r15]
 movsxd rax, dword ptr [rdx + 0x418]
 cmp eax, 0xc
@@ -35,5 +35,5 @@
 mov rdi, rbx
 call F
-lea r15, [rbp - 0x90]
+lea r14, [rbp - 0x90]
 mov edx, 1
 mov rdi, rbx
@@ -42,5 +42,5 @@
 mov edx, 2
 xor esi, esi
-mov rdi, r15
+mov rdi, r14
 lea rax, [T]
 mov qword ptr [rbp - 0xc0], 0
@@ -54,5 +54,5 @@
 mov qword ptr [rbp - 0x48], r12
 call F
-mov r8, r15
+mov r8, r14
 mov rcx, rbx
 xor edx, edx
@@ -62,5 +62,5 @@
 movss xmm1, dword ptr [rax + 8]
 call F
-mov rdi, r15
+mov rdi, r14
 call F
 mov rdi, rbx
@@ -69,5 +69,5 @@
 cmp byte ptr [r12 + 0x778], 0
 jne L
-mov rdx, qword ptr [r14]
+mov rdx, qword ptr [r15]
 cmp dword ptr [rdx + 0x1410], 1
 je L
@@ -92,8 +92,24 @@
 jmp F
 nop dword ptr [rax]
-lea rdi, [r12 + 0x794]
-call F
-test rax, rax
-je L
+mov ecx, dword ptr [r12 + 0x794]
+cmp ecx, -1
+je L
```
(ещё 233 строк диффа: so-query.py fdiff libserver.so 0x47a4da0)

### изменена: 0x49fe3a0 (3 байт) CDOTA_Modifier_ChaosKnight_Armageddon_Phantasms::IsPurgable
было: 0x49fe2d0 (6 байт)
- числа в инструкциях: −1
- инструкций: 2 → 2
```diff
@@ -1,2 +1,2 @@
-mov eax, 1
+xor eax, eax
 ret
```

### изменена: 0x4a8d0b0 (1889 байт) CDOTA_Modifier_Disruptor_KineticWall_Thinker::OnIntervalThink | строки: "disruptor_electromagnetic_repulsion"; "modifier_disruptor_kinetic_field"; "duration"; "angle"; "aura_origin_x"; "aura_origin_y"; "aura_origin_z"; "right_x"
было: 0x4a8cfb0 (1703 байт)
- числа в инструкциях: +0 +0
- поля объектов: +0x7e0 +0x7e1
- прямых вызовов: 51 → 56
- инструкций: 363 → 399
```diff
@@ -12,7 +12,7 @@
 mov rdi, rbx
 call F
-test rax, rax
-je L
-mov rdi, rbx
+mov rdi, rbx
+test rax, rax
+je L
 call F
 lea rsi, [S:"disruptor_electromagnetic_repulsion"]
@@ -27,6 +27,12 @@
 xor ecx, ecx
 call F
-test rax, rax
+mov rdi, rbx
 mov r12, rax
+call F
+test rax, rax
+je L
+mov rdi, rbx
+call F
+cmp byte ptr [rax + 0x7e0], 0
 je L
 mov rdi, rbx
@@ -109,4 +115,24 @@
 ret
 nop dword ptr [rax + rax]
+call F
+test rax, rax
+je L
+xor r12d, r12d
+jmp L
+nop word ptr [rax + rax]
+mov rdi, rbx
+call F
+cmp byte ptr [rax + 0x7e1], 0
+jne L
+test r12, r12
+je L
+jmp L
+nop word ptr [rax + rax]
+mov rdi, rbx
+call F
+test rax, rax
+jne L
+jmp L
+nop
 lea rdx, [rbp - 0x7c]
 lea rsi, [rbp - 0x88]
@@ -186,27 +212,47 @@
 comiss xmm0, dword ptr [rbp - 0xb4]
 movss dword ptr [rbp - 0x48], xmm1
-movss xmm4, dword ptr [rbp - 0x50]
```
(ещё 104 строк диффа: so-query.py fdiff libserver.so 0x4a8d0b0)

### изменена: 0x4ac6980 (2680 байт) CDOTA_Ability_EarthSpirit_RollingBoulder::vfunc#371 | строки: "modifier_earthspirit_petrify"; "npc_dota_earth_spirit_stone"; "earth_spirit_stone_caller"; "particles/units/heroes/hero_earth_spirit/espirit_rollingboulder_stone.vpcf"; "Hero_EarthSpirit.RollingBoulder.Stone"; "Hero_EarthSpirit.RollingBoulder.Target"; "Hero_EarthSpirit.RollingBoulder.Damage"; "stun_duration"
было: 0x4ac67c0 (2664 байт)
- инструкций: 573 → 577
```diff
@@ -74,8 +74,12 @@
 call qword ptr [rax + 0xe30]
 lea rsi, [S:"npc_dota_earth_spirit_stone"]
-mov rdi, rax
-call F
-test al, al
-je L
+cmp rax, rsi
+je L
+test rax, rax
+je L
+mov rdi, rax
+call F
+test eax, eax
+jne L
 movss xmm1, dword ptr [rbx + 0x8ac]
 mov rdi, rbx
@@ -210,5 +214,5 @@
 xor esi, esi
 call F
-nop dword ptr [rax]
+nop word ptr [rax + rax]
 xor eax, eax
 lea rsp, [rbp - 0x28]
```

### изменена: 0x4acd5c0 (10004 байт) вызывается из: CDOTA_Modifier_AbyssalUnderlord_Underling_Spawn_Thinker::OnIntervalThink | строки: "abyssal_underlord_dark_portal"; "DOTA_Item.Necronomicon.Activate"; "modifier_underlord_underling_autoattack"; "target"; "duration"; "npc_dota_necronomicon_archer_%d"; "particles/items_fx/necronomicon_spawn.vpcf"; "necronomicon_archer_aoe"
было: 0x4acd3f0 (10020 байт)
- строки: −"<NoAbilityName>"
- инструкций: 1981 → 1980
```diff
@@ -1751,15 +1751,15 @@
 jne L
 mov rax, qword ptr [rbx + 0x840]
-lea rdi, [S:"<NoAbilityName>"]
 test rax, rax
 je L
 mov rdi, qword ptr [rax]
-lea rax, [D]
 test rdi, rdi
-cmove rdi, rax
+je L
 lea rsi, [S:"grimstroke_ink_creature"]
-call F
-test al, al
-je L
+cmp rdi, rsi
+je L
+call F
+test eax, eax
+jne L
 mov rdi, qword ptr [rbp - 0x78]
 call F
@@ -1788,5 +1788,5 @@
 pop rbp
 jmp F
-nop dword ptr [rax]
+nop
 lea r12, [D]
 jmp L
@@ -1798,5 +1798,4 @@
 mov dword ptr [r14 + 0x1368], 0xffffffff
 jmp L
-nop dword ptr [rax + rax]
 mov rax, qword ptr [K:0x7f7fffff7f7fffff]
 movss xmm1, dword ptr [K:3.402823e+38]
```

### изменена: 0x4adfdf0 (3659 байт) CDOTA_Modifier_Disruptor_Thunder_Strike::OnIntervalThink | строки: "particles/units/heroes/hero_disruptor/disruptor_thunder_strike_bolt.vpcf"; "attach_hitloc"; "slow_duration"; "modifier_disruptor_thunderstrike_slow"; "duration"; "particles/units/heroes/hero_disruptor/disruptor_thunder_strike_aoe.vpcf"; "Hero_Disruptor.ThunderStrike.Target"; "modifier_disruptor_kinetic_field"
было: 0x4adfc30 (3571 байт)
- числа в инструкциях: +0 +3 +1
- поля объектов: +0x5d1 +0xd3c +0x175a +0xd58
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
+mov edx, 0x227
+xor esi, esi
+call F
+jmp L
+nop dword ptr [rax]
 mov rbx, qword ptr [rbp - 0x148]
 mov rdi, r15
```
(ещё 15 строк диффа: so-query.py fdiff libserver.so 0x4adfdf0)

### изменена: 0x4c41ab0 (2485 байт) CDOTA_Ability_Kez_GrapplingClaw::vfunc#334 | строки: "projectile_speed"; "tree"; "tree_ptr"; "particles/units/heroes/hero_kez/kez_kunai.vpcf"; "attach_attack2"; "Hero_Kez.GrapplingClaw.Katana.Cast"; "attach_hitloc"
было: 0x4c41870 (2469 байт)
- прямых вызовов: 62 → 63
- инструкций: 467 → 474
```diff
@@ -187,12 +187,11 @@
 mov qword ptr [rbp - 0x1c0], rax
 call F
-xor edi, edi
-pxor xmm0, xmm0
+pxor xmm0, xmm0
+xor r11d, r11d
+mov rdi, qword ptr [rbp - 0x1c0]
 movaps xmmword ptr [rbp - 0x160], xmm0
-mov word ptr [rbp - 0x138], di
-mov rdi, qword ptr [rbp - 0x1c0]
+movaps xmm0, xmmword ptr [K:-1,-1,3.402823e+38,3.402823e+38]
+mov rsi, r13
 lea rdx, [S:"particles/units/heroes/hero_kez/kez_kunai.vpcf"]
-mov rsi, r13
-movaps xmm0, xmmword ptr [K:-1,-1,3.402823e+38,3.402823e+38]
 mov qword ptr [rbp - 0x110], r15
 mov qword ptr [rbp - 0x170], rdx
@@ -201,4 +200,5 @@
 mov dword ptr [rbp - 0x148], 0
 mov qword ptr [rbp - 0x140], 0
+mov word ptr [rbp - 0x138], r11w
 mov byte ptr [rbp - 0x136], 0
 movlps qword ptr [rbp - 0x134], xmm0
@@ -231,6 +231,6 @@
 movq xmm0, qword ptr [K:0x7f7fffff7f7fffff]
 push 1
+xor edx, edx
 mov rcx, rax
-xor edx, edx
 movss xmm1, dword ptr [K:3.402823e+38]
 mov r8d, 1
@@ -238,6 +238,6 @@
 call F
 test r12, r12
-pop rcx
-pop rsi
+pop r9
+pop r10
 je L
 call F
@@ -317,8 +317,8 @@
 pop rbp
 ret
-nop dword ptr [rax]
+nop dword ptr [rax + rax]
 mov dword ptr [rbx + 0x860], 0xffffffff
 jmp L
-nop word ptr [rax + rax]
+nop
 mov dword ptr [rbp - 0xa8], 0xffffffff
 test r12, r12
@@ -361,4 +361,8 @@
 jmp L
```
(ещё 26 строк диффа: so-query.py fdiff libserver.so 0x4c41ab0)

### изменена: 0x4e30bd0 (3594 байт) | строки: "m_iStoredRuneType"; "int"; "int32"; "OnStoredRuneChanged"; "CDOTA_Item_EmptyBottle"; "15CNetworkVarBaseIiN22CDOTA_Item_EmptyBottle28NetworkVar_m_iStoredRuneTypeEE"
было: 0x4e30a00 (3546 байт)
- прямых вызовов: 63 → 65
- инструкций: 725 → 739
```diff
@@ -1,2 +1,16 @@
+push rbp
+mov rbp, rsp
+push rbx
+sub rsp, 8
+call F
+mov rdi, rax
+mov rbx, rax
+call F
+mov rdi, rbx
+mov rbx, qword ptr [rbp - 8]
+mov qword ptr [D], rax
+mov rsi, rax
+leave
+jmp F
 push rbp
 mov rbp, rsp
```

### изменена: 0x4f4bc80 (17659 байт)
было: 0x4f4c500 (14971 байт)
- числа в инструкциях: +0 +0 +0 +0 +0 +0 +0 +0 (и ещё 8)
- прямых вызовов: 340 → 404
- инструкций: 2771 → 3347
```diff
@@ -1,2 +1,578 @@
+push rbp
+mov rbp, rsp
+push r12
+push rbx
+movzx eax, byte ptr [D]
+test al, al
+je L
+mov rax, qword ptr [D]
+test rax, rax
+je L
+pop rbx
+pop r12
+pop rbp
+ret
+nop dword ptr [rax + rax]
+lea rbx, [D]
+mov rdi, rbx
+call F
+test eax, eax
+je L
+lea r12, [D]
+mov rdi, r12
+call F
+lea rdi, [T]
+lea rdx, [D]
+mov rsi, r12
+call F
+mov rdi, rbx
+call F
+mov rax, qword ptr [D]
+test rax, rax
+jne L
+nop dword ptr [rax]
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
+movq xmm1, rax
+punpcklqdq xmm0, xmm1
+lea rax, [T]
+movups xmmword ptr [D], xmm0
```
(ещё 525 строк диффа: so-query.py fdiff libserver.so 0x4f4bc80)

### изменена: 0x5048600 (268 байт) CDOTA_Modifier_BackdoorProtectionInBase::vfunc#9
было: 0x50483f0 (258 байт)
- инструкций: 63 → 65
```diff
@@ -62,2 +62,4 @@
 jbe L
 jmp L
+mov rax, qword ptr [0]
+ud2
```

### изменена: 0x56b21b0 (439 байт)
было: 0x56b1f90 (336 байт)
- числа в инструкциях: +0 +0 +-1 +-1 +0x7fff +4
- поля объектов: +0x7c +0x84 +0xa
- инструкций: 72 → 90
```diff
@@ -71,2 +71,20 @@
 call F
 jmp L
+movzx eax, word ptr [D]
+cmp ax, -1
+je L
+xor ecx, ecx
+test word ptr [D], 0x7fff
+cmovne rcx, qword ptr [D]
+nop word ptr cs:[rax + rax]
+nop word ptr cs:[rax + rax]
+nop word ptr cs:[rax + rax]
+shl rax, 4
+add rax, rcx
+mov rdx, qword ptr [rax]
+mov qword ptr [rdx + 0x7c], 0
+mov dword ptr [rdx + 0x84], 0
+movzx eax, word ptr [rax + 0xa]
+cmp ax, -1
+jne L
+ret
```

### изменена: 0x5c02920 (1007 байт) | строки: "npc_dota_mutation_pocket_roshan"
было: 0x5c02720 (931 байт)
- числа в инструкциях: +-1 +0x18 +0
- поля объектов: +0x13b0 +0x152c
- инструкций: 223 → 241
```diff
@@ -212,4 +212,22 @@
 xor ebx, ebx
 jmp L
+movzx eax, word ptr [r14 + 0x152c]
+cmp ax, -1
+je L
+mov rdx, qword ptr [r14 + 0x13b0]
+mov rdx, qword ptr [rdx + rax*8]
+mov rax, qword ptr [rdx + 8]
+movsxd rdx, dword ptr [rdx]
+lea rdx, [rdx + rdx*2]
+lea rdx, [rax + rdx*8]
+cmp rax, rdx
+jne L
+jmp L
+nop dword ptr [rax]
+add rax, 0x18
+cmp rdx, rax
+je L
+cmp qword ptr [rax], 0
+je L
 lea rdx, [D]
 xor ecx, ecx
```

### изменена: 0x5c1ab70 (2354 байт) CDOTA_Neutral_Creep_BehaviorController::vfunc#3 | строки: "modifier_roshan_moving"
было: 0x5c1a930 (2213 байт)
- числа в инструкциях: +0 +0 +1 +0xffffffff +0xffffffff
- поля объектов: +0x194c +0x790 +0xc70 +0x794 +0xc68
- прямых вызовов: 53 → 57
- инструкций: 485 → 519
```diff
@@ -249,6 +249,6 @@
 mov dword ptr [rbx + 0x1204], 0xffffffff
 mov ecx, 0
-movss xmm0, dword ptr [r12 + 0x38]
-ucomiss xmm0, dword ptr [r13 + 0xa0]
+movss xmm0, dword ptr [r12 + 0x3c]
+ucomiss xmm0, dword ptr [r13 + 0xa4]
 mov rdx, qword ptr [r12 + 0x38]
 setnp al
@@ -256,6 +256,6 @@
 test al, al
 je L
-movss xmm0, dword ptr [r12 + 0x3c]
-ucomiss xmm0, dword ptr [r13 + 0xa4]
+movss xmm0, dword ptr [r12 + 0x38]
+ucomiss xmm0, dword ptr [r13 + 0xa0]
 setnp al
 cmovne eax, ecx
@@ -371,6 +371,6 @@
 je L
 mov rsi, rax
-mov rdi, rbx
 mov edx, 0xffffffff
+mov rdi, rbx
 call F
 xor edx, edx
@@ -384,4 +384,34 @@
 mov rsi, r13
 call F
+cmp byte ptr [rbx + 0x194c], 0
+je L
+lea r15, [T]
+xor r13d, r13d
+lea r14, [T]
+jmp L
+mov byte ptr [r12 + 0x790], 0
+mov rax, qword ptr [rax + 0xc70]
+cmp rax, r14
+jne L
+mov dword ptr [r12 + 0x794], 0xffffffff
+add r13d, 1
+mov rdi, rbx
+call F
+cmp eax, r13d
+jle L
+mov esi, r13d
+mov rdi, rbx
+call F
+test rax, rax
+mov r12, rax
+je L
+mov rax, qword ptr [rax]
+mov rdx, qword ptr [rax + 0xc68]
+cmp rdx, r15
```
(ещё 34 строк диффа: so-query.py fdiff libserver.so 0x5c1ab70)

### изменена: 0x5c1c1b0 (2314 байт)
было: 0x5c1bee0 (2330 байт)
- инструкций: 532 → 529
```diff
@@ -222,17 +222,14 @@
 mov rdi, r12
 call F
-movaps xmm1, xmm0
-movss xmm0, dword ptr [r15 + 0x54]
+test al, al
+je L
+movss xmm1, dword ptr [r15 + 0x54]
+pxor xmm0, xmm0
 comiss xmm1, xmm0
 jp L
 je L
 jbe L
-pxor xmm1, xmm1
-comiss xmm0, xmm1
-jp L
-je L
-jbe L
-movss xmm0, dword ptr [r15 + 0x50]
-comiss xmm0, xmm1
+movss xmm1, dword ptr [r15 + 0x50]
+comiss xmm1, xmm0
 ja L
 pxor xmm0, xmm0
```

### изменена: 0x62020d0 (343 байт) CDOTA_BaseNPC_Creep_Neutral::vfunc#351
было: 0x6201e50 (240 байт)
- числа в инструкциях: +0 +0 +0xffffffff +0xffffffff
- поля объектов: +0xc68 +0x790 +0xc70 +0x794 +0x194c
- прямых вызовов: 8 → 9
- инструкций: 65 → 90
```diff
@@ -1,16 +1,20 @@
 push rbp
 mov rbp, rsp
+push r15
+push r14
 push r13
 push r12
 push rbx
 mov rbx, rdi
-sub rsp, 8
+sub rsp, 0x18
 call F
 cmp byte ptr [rbx + 0x174c], 0
 je L
-add rsp, 8
+add rsp, 0x18
 pop rbx
 pop r12
 pop r13
+pop r14
+pop r15
 pop rbp
 ret
@@ -35,5 +39,7 @@
 jbe L
 movss xmm1, dword ptr [K:1.25]
+lea r15, [T]
 movss xmm0, dword ptr [K:0.75]
+lea r14, [T]
 call F
 mov rdi, r13
@@ -44,7 +50,13 @@
 jg L
 jmp L
-nop dword ptr [rax + rax]
-call rax
-nop word ptr [rax + rax]
+nop dword ptr [rax]
+mov rcx, qword ptr [rdx + 0xc68]
+cmp rcx, r14
+jne L
+mov byte ptr [rax + 0x790], 0
+mov rdx, qword ptr [rdx + 0xc70]
+cmp rdx, r13
+jne L
+mov dword ptr [rax + 0x794], 0xffffffff
 add r12d, 1
 cmp r12d, dword ptr [rbx + 0x1320]
@@ -55,11 +67,24 @@
 test rax, rax
 je L
-mov rdi, rbx
-mov esi, r12d
-call F
```
(ещё 26 строк диффа: so-query.py fdiff libserver.so 0x62020d0)

### изменена: 0x6225380 (3812 байт) CDOTA_BaseNPC_Hero::vfunc#263, CDOTA_Unit_Hero_AncientApparition::vfunc#263, CDOTA_Unit_Hero_AntiMage::vfunc#263 | строки: "dota_player_take_tower_damage"; "PlayerID"; "damage"
было: 0x6225080 (3780 байт)
- числа в инструкциях: +-1 +-2 +9 +0x3f +0x1ff +0x70
- поля объектов: +0x10
- прямых вызовов: 52 → 51
- инструкций: 786 → 799
```diff
@@ -109,9 +109,9 @@
 call qword ptr [rax + 0x5b0]
 mov rdi, rbx
-mov dword ptr [rbp - 0x16c], eax
+mov dword ptr [rbp - 0x168], eax
 call F
 pxor xmm0, xmm0
 mov rdi, rbx
-mov dword ptr [rbp - 0x168], eax
+mov dword ptr [rbp - 0x164], eax
 mov rax, qword ptr [r12]
 mov ecx, dword ptr [rax + 0x78]
@@ -122,8 +122,8 @@
 movss dword ptr [rbp - 0x158], xmm0
 call qword ptr [rax + 0xc70]
-mov r9d, dword ptr [rbp - 0x16c]
+mov r9d, dword ptr [rbp - 0x168]
 mov esi, r15d
 mov rdi, r13
-mov r8d, dword ptr [rbp - 0x168]
+mov r8d, dword ptr [rbp - 0x164]
 mov edx, eax
 mov ecx, dword ptr [rbp - 0x160]
@@ -517,5 +517,5 @@
 jmp L
 nop word ptr cs:[rax + rax]
-mov dword ptr [rbp - 0x168], r8d
+mov dword ptr [rbp - 0x164], r8d
 mov rdi, rsi
 mov qword ptr [rbp - 0x160], rsi
@@ -523,5 +523,5 @@
 mov rsi, qword ptr [rbp - 0x160]
 test al, al
-mov r8d, dword ptr [rbp - 0x168]
+mov r8d, dword ptr [rbp - 0x164]
 jne L
 jmp L
@@ -558,14 +558,12 @@
 jmp L
 nop dword ptr [rax]
-lea r14, [D]
+lea r13, [D]
 lea rax, [rbp - 0x150]
-xor r13d, r13d
+xor r15d, r15d
 movzx edx, byte ptr [rbx + 0x624]
 mov rdi, rax
-mov qword ptr [rbp - 0x160], rax
-mov rsi, qword ptr [r14]
-call F
-lea rax, [rbp - 0x130]
 mov qword ptr [rbp - 0x158], rax
+mov rsi, qword ptr [r13]
+call F
```
(ещё 92 строк диффа: so-query.py fdiff libserver.so 0x6225380)

### изменена: 0x6280100 (6453 байт)
было: 0x627fe00 (6179 байт)
- числа в инструкциях: +0 +0 +4 +4 +0x10 +0x3fffffff +0x3fffffff +0x3fffffff −1 (и ещё 6)
- поля объектов: +0xc +0xc +0xc +0xc +0xc
- прямых вызовов: 83 → 86
- инструкций: 1251 → 1325
```diff
@@ -124,12 +124,14 @@
 mov qword ptr [rbp - 0x358], 0
 mov dword ptr [rbp - 0x34c], 0
+lea rax, [rbp - 0x2b0]
 xor r12d, r12d
 xor r14d, r14d
+mov qword ptr [rbp - 0x308], r10
 mov dword ptr [rbp - 0x350], 0
 mov dword ptr [rbp - 0x310], 0
-mov qword ptr [rbp - 0x308], r10
+mov qword ptr [rbp - 0x370], rax
 mov qword ptr [rbp - 0x328], r11
 jmp L
-nop dword ptr [rax]
+nop dword ptr [rax + rax]
 mov rax, qword ptr [r13]
 lea rcx, [T]
@@ -162,4 +164,5 @@
 mov rdi, qword ptr [rbx]
 mov esi, r15d
+mov dword ptr [rbp - 0x150], r15d
 call F
 test al, al
@@ -167,5 +170,5 @@
 mov r15d, dword ptr [rbp - 0x270]
 jmp L
-nop dword ptr [rax]
+nop word ptr [rax + rax]
 mov qword ptr [rbp - 0x310], rdx
 mov rdi, rsi
@@ -339,9 +342,11 @@
 cmp r8, rax
 jne L
-cmp dword ptr [rbp - 0x350], r12d
+mov eax, dword ptr [rbp - 0x350]
+cmp r12d, eax
 je L
 mov dword ptr [r14 + r8*4], r15d
 add r12d, 1
 jmp L
+nop word ptr [rax + rax]
 mov r10, qword ptr [rbp - 0x328]
 mov dword ptr [rbp - 0x310], r12d
@@ -358,9 +363,7 @@
 mov dword ptr [rbp - 0x368], eax
 call F
-lea rcx, [rbp - 0x2b0]
 mov r11, qword ptr [rbp - 0x308]
 test al, al
 mov r10, qword ptr [rbp - 0x328]
-mov qword ptr [rbp - 0x370], rcx
 je L
 mov eax, dword ptr [rbp - 0x310]
@@ -369,8 +372,95 @@
```
(ещё 434 строк диффа: so-query.py fdiff libserver.so 0x6280100)

### изменена: 0x3e72f80 (1059 байт) | строки: "CNetworkUtlVectorBase"; "AnimationAlgorithm_t"; "ExternalAnimGraphHandle_t"; "CGlobalSymbol"; "CBaseAnimGraph"; "CHandle"; "GameTime_t"; "CUtlVectorEmbeddedNetworkVar"
- код тот же, но вызывает другую функцию: было 0x3eace10, стало 0x3eace50

### добавлена: 0x3e6ee50 (98 байт) | строки: "R{x"

### добавлена: 0x4a213f0 (29 байт) CDOTA_Ability_ChaosKnight_Phantasm::vfunc#382 | строки: "chaos_knight_armageddon;chaos_knight_armageddons_flank_end"

### удалена: 0x3e6ebb0 (183 байт) | строки: "?yx"

### удалена: 0x3e6ece0 (183 байт) | строки: "Szx"

### удалена: 0x3e6ee80 (98 байт) | строки: "f{x"

### удалена: 0x4790260 (470 байт) CDOTA_Ability_WitchDoctor_DeathWard::vfunc#156

### удалена: 0x56b2100 (103 байт) вызывается из: CSource1GameConfiguration::vfunc#22

### копии существующего кода (8): шаблонные / склеенные компоновщиком функции, такой же код есть и в другой сборке — не новый код
- ещё одна копия существующего кода: 0x3e6ebf0 (183 байт)
- ещё одна копия существующего кода: 0x3e6ed20 (183 байт)
- ещё одна копия существующего кода: 0x49fec30 (3 байт) CDOTA_Ability_Chaos_Knight_ArmageddonsFlank_End::vfunc#384
- ещё одна копия существующего кода: 0x49fec40 (6 байт) CDOTA_Ability_Chaos_Knight_ArmageddonsFlank_End::vfunc#387
- одной копией существующего кода меньше: 0x4e309c0 (48 байт)
- одной копией существующего кода меньше: 0x4f4ba70 (2688 байт)
- одной копией существующего кода меньше: 0x5048500 (10 байт) вызывается из: CDOTA_Modifier_Gold_Bag_Launch::OnDestroy
- одной копией существующего кода меньше: 0x6281640 (277 байт)
