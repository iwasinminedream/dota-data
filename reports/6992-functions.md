# Dota 6992: изменения кода по функциям и строки библиотек

Снимки `6989-11264029` → `6992-11267656`; funcdiff.py. В диффе: [S:…] — строка, [K:…] — константа из данных, F — вызов другой функции, L — переход внутри функции, [D]/[T] — прочие адреса. Регистры и смещения стека меняются и от перекомпиляции. Здесь всё, в том числе игровые функции и изменения от пересборки.

## libclient.so: функций 281893 → 281876; без изменений 281505, изменено 371, добавлено 0, удалено 4

### изменена: 0x3bbdce0 (164 байт) | строки: "0]j"; "Release"; "client"
было: 0x3bbfde0 (164 байт)
- строки: +"0]j" −"0nj"
- инструкций: 34 → 34
```diff
@@ -1,5 +1,5 @@
 cmp edi, 6
 ja F
-lea rdx, [S:"0nj"]
+lea rdx, [S:"0]j"]
 mov edi, edi
 movsxd rax, dword ptr [rdx + rdi*4]
```

### изменена: 0x3beb660 (398 байт) | строки: "D m"
было: 0x3bed760 (398 байт)
- строки: +"D m" −"D1m"
- инструкций: 128 → 128
```diff
@@ -8,5 +8,5 @@
 movsxd r12, edx
 push rbx
-lea rdx, [S:"D1m"]
+lea rdx, [S:"D m"]
 mov rbx, rsi
 sub rsp, 0x18
```

### изменена: 0x3bee640 (13077 байт) | строки: "m_nId"; "m_Name"; "m_strNameToken"; "m_CoverImage"; "m_nNumberOfImages"; "m_URLForImages"; "m_nNumDigitsInFilename"; "m_ImageFileExtension"
было: 0x3bf0740 (13077 байт)
- строки: +"Tym"
- инструкций: 2855 → 2855
```diff
@@ -1719,5 +1719,5 @@
 cmp al, 6
 ja L
-lea rcx, [D]
+lea rcx, [S:"Tym"]
 movzx edx, al
 movsxd rdx, dword ptr [rcx + rdx*4]
```

### изменена: 0x3c0c300 (753 байт) C_PlayerCosmeticPropClientside::vfunc#11 | строки: "playernumber"; "cosmetic_type"; "j&o"
было: 0x3c0e400 (753 байт)
- строки: +"j&o" −"j7o"
- инструкций: 197 → 197
```diff
@@ -103,5 +103,5 @@
 cmp al, 6
 ja L
-lea rdx, [S:"j7o"]
+lea rdx, [S:"j&o"]
 movzx eax, al
 movsxd rax, dword ptr [rdx + rax*4]
```

### изменена: 0x3c71450 (765 байт) CPointClientUIWorldTextPanelPreviewer::vfunc#2 | строки: "horizontal_align"; "(Fu"; "vertical_align"; "\\Eu"; "orientation"
было: 0x3c73550 (765 байт)
- строки: +"(Fu" +"\\Eu" −"(Wu" −"\\Vu"
- инструкций: 185 → 185
```diff
@@ -23,5 +23,5 @@
 cmp dl, 6
 ja L
-lea rcx, [S:"(Wu"]
+lea rcx, [S:"(Fu"]
 movzx edx, dl
 movsxd rdx, dword ptr [rcx + rdx*4]
@@ -53,5 +53,5 @@
 cmp dl, 6
 ja L
-lea rcx, [S:"\\Vu"]
+lea rcx, [S:"\\Eu"]
 movzx edx, dl
 movsxd rdx, dword ptr [rcx + rdx*4]
```

### изменена: 0x3c71770 (334 байт) | строки: "{Hu"
было: 0x3c73870 (334 байт)
- строки: +"{Hu" −"{Yu"
- инструкций: 82 → 82
```diff
@@ -6,5 +6,5 @@
 ja L
 push rbp
-lea rdx, [S:"{Yu"]
+lea rdx, [S:"{Hu"]
 mov edi, edi
 mov rbp, rsp
```

### изменена: 0x3c82d60 (397 байт) | строки: "<]v"
было: 0x3c84e60 (397 байт)
- строки: +"<]v" −"<nv"
- инструкций: 114 → 114
```diff
@@ -12,5 +12,5 @@
 punpcklqdq xmm0, xmm1
 ja L
-lea rdx, [S:"<nv"]
+lea rdx, [S:"<]v"]
 mov edi, edi
 mov rbx, rsi
```

### изменена: 0x3c83180 (1171 байт) | строки: " av"; "C_BaseModelEntity"; "CHandle"; "C_NetworkUtlVectorBase"; "CUtlSymbolLarge"; "CUtlVector"
было: 0x3c85280 (1171 байт)
- строки: +" av" −" rv"
- инструкций: 235 → 235
```diff
@@ -2,5 +2,5 @@
 ja L
 push rbp
-lea rdx, [S:" rv"]
+lea rdx, [S:" av"]
 mov edi, edi
 mov rbp, rsp
```

### изменена: 0x3c84b00 (568 байт) | строки: ",zv"
было: 0x3c86e40 (568 байт)
- строки: +",zv"
- инструкций: 160 → 160
```diff
@@ -9,5 +9,5 @@
 movsxd r12, edx
 push rbx
-lea rdx, [D]
+lea rdx, [S:",zv"]
 mov rbx, rsi
 sub rsp, 0x10
```

### изменена: 0x3c84d40 (568 байт) | строки: "P|v"
было: 0x3c87080 (568 байт)
- строки: +"P|v"
- инструкций: 160 → 160
```diff
@@ -9,5 +9,5 @@
 movsxd r12, edx
 push rbx
-lea rdx, [D]
+lea rdx, [S:"P|v"]
 mov rbx, rsi
 sub rsp, 0x10
```

### изменена: 0x3c84f80 (568 байт) | строки: "t~v"
было: 0x3c872c0 (568 байт)
- строки: +"t~v"
- инструкций: 160 → 160
```diff
@@ -9,5 +9,5 @@
 movsxd r12, edx
 push rbx
-lea rdx, [D]
+lea rdx, [S:"t~v"]
 mov rbx, rsi
 sub rsp, 0x10
```

### изменена: 0x3c8e9c0 (542 байт)
было: 0x3c90ac0 (542 байт)
- строки: −"|)w"
- инструкций: 159 → 159
```diff
@@ -9,5 +9,5 @@
 movsxd r12, edx
 push rbx
-lea rdx, [S:"|)w"]
+lea rdx, [D]
 mov rbx, rsi
 sub rsp, 0x10
```

### изменена: 0x3cb2820 (2029 байт) | строки: "h6y"; "CGlobalSymbol"; "CAnimGraph2ParamOptionalRef"; "CTransform"; "e_choreo_outro_type"; "e_choreo_entry_type"; "t_choreo_exit_warp"; "t_choreo_target_warp"
было: 0x3cb4920 (2029 байт)
- строки: +"h6y" −"hGy"
- инструкций: 393 → 393
```diff
@@ -9,5 +9,5 @@
 cmp edi, 6
 ja F
-lea rdx, [S:"hGy"]
+lea rdx, [S:"h6y"]
 mov edi, edi
 mov rbx, rsi
```

### изменена: 0x3cc35d0 (1113 байт) CNetworkTransmitComponent::vfunc#3 | строки: "m_nTransmitStateOwnedCounter"; "|Fz"; "Unsupported KV3 basic type '%s' (%d)!"; "Pointers cannot be used as numeric values"
было: 0x3cc56d0 (1113 байт)
- строки: +"|Fz" −"|Wz"
- инструкций: 259 → 259
```diff
@@ -108,5 +108,5 @@
 cmp r8b, 6
 ja L
-lea rdx, [S:"|Wz"]
+lea rdx, [S:"|Fz"]
 movzx eax, r8b
 movsxd rax, dword ptr [rdx + rax*4]
```

### изменена: 0x3cc6b30 (625 байт) вызывается из: CChoreo_GraphController::vfunc#6 | строки: "Ryz"; "unknown"; "false"; "true"; "transform"; "vector"; "float"; "globalSymbol"
было: 0x3cc8c30 (625 байт)
- строки: +"Ryz"
- инструкций: 165 → 165
```diff
@@ -18,5 +18,5 @@
 cmp al, 5
 ja L
-lea rdx, [D]
+lea rdx, [S:"Ryz"]
 movzx eax, al
 movsxd rax, dword ptr [rdx + rax*4]
```

### изменена: 0x3cd0ee0 (1127 байт) CHitboxComponent::vfunc#4 | строки: "m_flBoundsExpandRadius"; "Unsupported KV3 basic type '%s' (%d)!"; "Pointers cannot be used as numeric values"
было: 0x3cd2fe0 (1127 байт)
- строки: −"X-{" −"<-{"
- инструкций: 258 → 258
```diff
@@ -51,5 +51,5 @@
 cmp r8b, 6
 ja L
-lea rdx, [S:"X-{"]
+lea rdx, [D]
 movzx eax, r8b
 movsxd rax, dword ptr [rdx + rax*4]
@@ -108,5 +108,5 @@
 cmp r8b, 6
 ja L
-lea rdx, [S:"<-{"]
+lea rdx, [D]
 movzx eax, r8b
 movsxd rax, dword ptr [rdx + rax*4]
```

### изменена: 0x3d00fc0 (183 байт)
было: 0x3d030c0 (183 байт)
- строки: −"+\t~"
- инструкций: 55 → 55
```diff
@@ -2,5 +2,5 @@
 ja L
 push rbp
-lea rdx, [S:"+\t~"]
+lea rdx, [D]
 mov edi, edi
 mov rbp, rsp
```

### изменена: 0x4abf5c0 (32254 байт) | строки: "scripts/height_levels.txt"; "modifier_jakiro_dual_breath"; "modifier_jakiro_dual_breath_slow"; "modifier_jakiro_dual_breath_burn"; "modifier_jakiro_ice_path_stun"; "modifier_jakiro_ice_path"; "modifier_jakiro_liquidice"; "modifier_jakiro_liquid_ice_debuff"
было: 0x4ac1940 (32295 байт)
- строки: −"modifier_lycan_wolf_bite_attack_range"
- прямых вызовов: 1010 → 1008
- инструкций: 5949 → 5941
```diff
@@ -311,5 +311,4 @@
 lea rdi, [T]
 call F
-lea r15, [D]
 call F
 lea r13, [D]
@@ -2326,12 +2325,4 @@
 mov qword ptr [D], rax
 call F
-lea rdx, [S:"modifier_lycan_wolf_bite_attack_range"]
-lea rsi, [D]
-mov rdi, rax
-mov rax, qword ptr [rax]
-call qword ptr [rax]
-lea rax, [D]
-mov qword ptr [D], rax
-call F
 lea rdx, [S:"modifier_lone_wolf_self"]
 lea rsi, [D]
@@ -2809,13 +2800,13 @@
 mov rax, qword ptr [r13]
 lea rdi, [D]
+mov qword ptr [rbp - 0x40], 0
+mov qword ptr [D], rax
+lea rax, [D]
+mov qword ptr [r13], rax
+lea rax, [T]
+mov qword ptr [D], rax
+lea rax, [T]
+mov qword ptr [rbp - 0x50], rax
 lea r13, [D]
-mov qword ptr [rbp - 0x40], 0
-mov qword ptr [D], rax
-lea rax, [D]
-mov qword ptr [r13], rax
-lea rax, [T]
-mov qword ptr [D], rax
-lea rax, [T]
-mov qword ptr [rbp - 0x50], rax
 call F
 mov rsi, rbx
@@ -2898,10 +2889,10 @@
 mov rax, qword ptr [rax]
 call qword ptr [rax]
-mov rdi, r15
+mov rdi, r13
 mov edx, 9
 lea rsi, [S:"dota_roshan_initial_move_timer"]
 call F
 mov rdx, r14
-mov rsi, r15
+mov rsi, r13
 lea rdi, [T]
 call F
@@ -2915,10 +2906,11 @@
 call qword ptr [rax]
 call F
-mov rsi, rbx
-mov qword ptr [rbp - 0x48], r12
-mov qword ptr [D], rax
-mov rax, qword ptr [r13]
-lea rdi, [D]
-mov qword ptr [rbp - 0x40], 0
+lea r13, [D]
+mov rsi, rbx
+mov qword ptr [rbp - 0x48], r12
+mov qword ptr [D], rax
+lea rdi, [D]
+mov qword ptr [rbp - 0x40], 0
+mov rax, qword ptr [r13]
 mov qword ptr [D], rax
 lea rax, [D]
```

### изменена: 0x4adb3b0 (460 байт) | строки: "C_DOTA_Ability_Luna_LunarOrbit"
было: 0x4add770 (468 байт)
- числа в инструкциях: −0x5bd1e995 −0x5bd1e995 −0x6e00285c −0x97da98df
- прямых вызовов: 9 → 10
- инструкций: 101 → 100
```diff
@@ -59,4 +59,7 @@
 mov esi, 0x75d80639
 call F
+lea rdi, [D]
+mov esi, eax
+call F
 lea rcx, [rbp - 0x24]
 mov rsi, rbx
@@ -65,8 +68,4 @@
 mov r9d, 2
 mov r8d, 0x828
-xor eax, 0x6e00285c
-imul eax, eax, 0x5bd1e995
-xor eax, 0x97da98df
-imul eax, eax, 0x5bd1e995
 xor eax, 0xe1d30f75
 imul eax, eax, 0x5bd1e995
```

### изменена: 0x4df9b60 (67 байт) CDOTA_Modifier_Smoke_Of_Deceit::CheckState
было: 0x4dfbf60 (67 байт)
- числа в инструкциях: +0x1000000000 +0xffffffefffffffff −0x81000000000 −0xfffff7efffffffff
- инструкций: 17 → 17
```diff
@@ -5,7 +5,7 @@
 sub rsp, 8
 call F
-movabs rax, 0x81000000000
+movabs rax, 0x1000000000
 or rax, qword ptr [rbx]
-movabs rdx, 0xfffff7efffffffff
+movabs rdx, 0xffffffefffffffff
 and rdx, qword ptr [rbx + 8]
 movq xmm0, rax
```

### изменена: 0x5792cc0 (2490 байт) вызывается из: C_DOTAPlayerController::vfunc#257, C_DOTAPlayerController::vfunc#253 | строки: "particles/ui_mouseactions/range_display.vpcf"
было: 0x5795140 (2420 байт)
- виртуальные вызовы: −0x748 (слот 233)
- поля объектов: +0x58 +0x748 +0x770 +0x770
- прямых вызовов: 59 → 60
- цели вызовов: +CDOTA_Ability_DarkCarnival_Balloon::GetBehavior +0x4f91d90
- инструкций: 554 → 569
```diff
@@ -115,7 +115,7 @@
 call qword ptr [rax + 0xbd0]
 mov rdi, r14
-mov byte ptr [rbp - 0x48], al
-call F
-movzx edx, byte ptr [rbp - 0x48]
+mov byte ptr [rbp - 0x58], al
+call F
+movzx edx, byte ptr [rbp - 0x58]
 test dl, dl
 jne L
@@ -170,9 +170,9 @@
 mov edx, 1
 xor esi, esi
-mov dword ptr [rbp - 0x48], r9d
+mov dword ptr [rbp - 0x58], r9d
 mov ecx, 1
 call F
 mov rdx, qword ptr [rbx + 0xc68]
-mov r9d, dword ptr [rbp - 0x48]
+mov r9d, dword ptr [rbp - 0x58]
 test rdx, rdx
 je L
@@ -191,12 +191,12 @@
 mov qword ptr [rbx + 0xc68], rdi
 mov rdi, r14
-mov dword ptr [rbp - 0x48], r9d
-call F
-mov r9d, dword ptr [rbp - 0x48]
+mov dword ptr [rbp - 0x58], r9d
+call F
+mov r9d, dword ptr [rbp - 0x58]
 test rax, rax
 mov rdi, rax
 je L
 mov rdi, qword ptr [rdi]
-mov dword ptr [rbp - 0x48], r9d
+mov dword ptr [rbp - 0x58], r9d
 call F
 xor r8d, r8d
@@ -207,5 +207,5 @@
 call F
 mov rdi, qword ptr [rbx + 0xc68]
-mov r9d, dword ptr [rbp - 0x48]
+mov r9d, dword ptr [rbp - 0x58]
 cmp rax, rdi
 je L
@@ -266,6 +266,6 @@
 movss xmm2, dword ptr [rax + 0x3c4]
 movss xmm3, dword ptr [rax + 0x3c8]
-movss dword ptr [rbp - 0x48], xmm2
-movss dword ptr [rbp - 0x54], xmm3
+movss dword ptr [rbp - 0x58], xmm2
+movss dword ptr [rbp - 0x48], xmm3
 call F
 test rax, rax
@@ -279,6 +279,6 @@
 movss xmm1, dword ptr [rax + 4]
 movss xmm0, dword ptr [rax]
-subss xmm1, dword ptr [rbp - 0x54]
-subss xmm0, dword ptr [rbp - 0x48]
+subss xmm1, dword ptr [rbp - 0x48]
+subss xmm0, dword ptr [rbp - 0x58]
 mulss xmm1, xmm1
 mulss xmm0, xmm0
@@ -287,5 +287,5 @@
 movd xmm0, eax
 sqrtss xmm0, xmm0
-movss dword ptr [rbp - 0x48], xmm0
+movss dword ptr [rbp - 0x58], xmm0
 call F
 test rax, rax
@@ -300,5 +300,5 @@
 mov rdi, r14
 cvtsi2ss xmm0, eax
-comiss xmm0, dword ptr [rbp - 0x48]
+comiss xmm0, dword ptr [rbp - 0x58]
 seta r13b
 call F
@@ -306,6 +306,13 @@
 je F
 mov rdi, qword ptr [rax]
-mov rax, qword ptr [rdi]
-call qword ptr [rax + 0x748]
+lea rdx, [T]
+mov rax, qword ptr [rdi]
+mov rax, qword ptr [rax + 0x748]
+cmp rax, rdx
+jne L
+mov rax, qword ptr [rdi + 0x770]
+test rax, rax
+je L
+mov rax, qword ptr [rax + 0x58]
 test al, 0x10
 jne L
@@ -332,5 +339,5 @@
 cmovne rax, qword ptr [D]
 jmp L
-nop dword ptr [rax]
+nop word ptr cs:[rax + rax]
 lea r12, [D]
 mov esi, 0x13d
@@ -374,5 +381,5 @@
 pop rbp
 ret
-nop word ptr cs:[rax + rax]
+nop
 mov rax, qword ptr [D]
 jmp L
@@ -520,4 +527,12 @@
 mov r9d, eax
 jmp L
+call rax
+jmp L
+xor esi, esi
+mov qword ptr [rbp - 0x58], rdi
+call F
+mov rdi, qword ptr [rbp - 0x58]
+mov rax, qword ptr [rdi + 0x770]
+jmp L
```
(ещё 14 строк диффа: so-query.py fdiff libclient.so 0x5792cc0)

### изменена: 0x579cb50 (1235 байт) вызывается из: C_DOTAPlayerController::vfunc#114 | строки: "model"; "skin"; "ItemData"
было: 0x579ef90 (1234 байт)
- виртуальные вызовы: +0x150 (слот 42)
- прямых вызовов: 28 → 29
- инструкций: 259 → 262
```diff
@@ -1,71 +1,83 @@
 mov rax, qword ptr [D]
 cmp byte ptr [rax + 0x58], 0
-jne L
-ret
-nop
+je L
 push rbp
 mov rbp, rsp
 push r15
 push r14
-mov r14, rdi
 push r13
 push r12
 push rbx
+mov rbx, rdi
 sub rsp, 0x108
-mov rax, qword ptr [rdi + 0x10]
+lea rax, [D]
+mov rdi, qword ptr [rax]
+mov rax, qword ptr [rdi]
+call qword ptr [rax + 0x150]
+test al, al
+je L
+lea rsp, [rbp - 0x28]
+pop rbx
+pop r12
+pop r13
+pop r14
+pop r15
+pop rbp
+ret
+nop
+mov rax, qword ptr [rbx + 0x10]
 mov edi, dword ptr [rax + 0x38]
 call F
 cmp dword ptr [D], eax
 je L
-mov rdi, r14
-call F
-test rax, rax
-mov rbx, rax
-je L
-mov r12d, dword ptr [r14 + 0xa90]
-mov rdi, rax
-call F
-cmp r12d, eax
+mov rdi, rbx
+call F
+test rax, rax
+mov r12, rax
+je L
+mov r13d, dword ptr [rbx + 0xa90]
+mov rdi, rax
+call F
+cmp eax, r13d
 jne L
-mov r15d, dword ptr [rbx + 0x2028]
+mov r15d, dword ptr [r12 + 0x2028]
 test r15d, r15d
 jle L
-cmp dword ptr [r14 + 0x1008], r15d
-je L
-mov r12, qword ptr [r14 + 0x1018]
-mov dword ptr [r14 + 0x1008], 0
-movsxd rax, dword ptr [r14 + 0x1010]
-lea r13, [r12 + rax*8]
-cmp r12, r13
-je L
-nop word ptr [rax + rax]
-mov rdi, qword ptr [r12]
+cmp r15d, dword ptr [rbx + 0x1008]
+je L
+mov r13, qword ptr [rbx + 0x1018]
+mov dword ptr [rbx + 0x1008], 0
+movsxd rax, dword ptr [rbx + 0x1010]
+lea r14, [r13 + rax*8]
+cmp r13, r14
+je L
+mov rdi, qword ptr [r13]
+add r13, 8
+call F
+cmp r14, r13
+jne L
+mov dword ptr [rbx + 0x1010], 0
+mov dword ptr [rbx + 0x1008], r15d
+call F
+mov rdi, r12
+mov r13, rax
+call F
+xor edx, edx
+mov rdi, r13
+mov esi, eax
+call F
+test rax, rax
+mov qword ptr [rbp - 0x120], rax
+je L
+call F
+mov esi, dword ptr [rbx + 0x1008]
+mov rdi, rax
+call F
+test rax, rax
+mov r12, rax
+je L
+mov rax, qword ptr [rbx + 0x10]
 add r12, 8
-call F
-cmp r13, r12
-jne L
-mov dword ptr [r14 + 0x1010], 0
-mov dword ptr [r14 + 0x1008], r15d
-call F
-mov rdi, rbx
-mov r12, rax
-call F
-xor edx, edx
-mov rdi, r12
-mov esi, eax
-call F
-test rax, rax
```
(ещё 204 строк диффа: so-query.py fdiff libclient.so 0x579cb50)

### изменена: 0x579d030 (241 байт)
было: 0x579f470 (209 байт)
- виртуальные вызовы: +0x150 (слот 42)
- прямых вызовов: 3 → 4
- инструкций: 63 → 70
```diff
@@ -10,10 +10,16 @@
 cmp byte ptr [rax + 0x58], 0
 je L
-mov ebx, dword ptr [rdi + 0x1010]
+lea rax, [D]
 mov r13, rdi
+mov r15d, esi
+mov rdi, qword ptr [rax]
+mov rax, qword ptr [rdi]
+call qword ptr [rax + 0x150]
+test al, al
+jne L
+mov ebx, dword ptr [r13 + 0x1010]
 sub ebx, 1
 js L
 movsxd r12, ebx
-mov r15d, esi
 shl r12, 3
 mov rax, qword ptr [r13 + 0x1018]
@@ -25,5 +31,5 @@
 mov rdi, r14
 call F
-cmp dword ptr [rax + 8], r15d
+cmp r15d, dword ptr [rax + 8]
 jne L
 mov eax, dword ptr [r13 + 0x1010]
@@ -49,4 +55,5 @@
 cmp ebx, -1
 jne L
+nop dword ptr [rax]
 xor r14d, r14d
 jmp L
```

### изменена: 0x57cca20 (223 байт) вызывается из: C_DOTA_BaseNPC::vfunc#16
было: 0x57cee20 (187 байт)
- виртуальные вызовы: +0x150 (слот 42)
- прямых вызовов: 2 → 3
- инструкций: 52 → 58
```diff
@@ -11,9 +11,15 @@
 cmp byte ptr [rax + 0x58], 0
 je L
-movsxd r13, dword ptr [rdi + 0x1010]
+lea rax, [D]
 mov r12, rdi
+mov rdi, qword ptr [rax]
+mov rax, qword ptr [rdi]
+call qword ptr [rax + 0x150]
+test al, al
+jne L
+movsxd r13, dword ptr [r12 + 0x1010]
 cmp r13d, 0x20
 jg L
-cmp r13d, dword ptr [rdi + 0x1020]
+cmp r13d, dword ptr [r12 + 0x1020]
 mov eax, r13d
 je L
@@ -35,5 +41,5 @@
 pop rbp
 jmp F
-nop
+nop word ptr [rax + rax]
 add rsp, 8
 mov rdi, rbx
@@ -46,5 +52,5 @@
 ret
 nop dword ptr [rax]
-lea rdi, [rdi + 0x1018]
+lea rdi, [r12 + 0x1018]
 mov esi, 1
 call F
```

### изменена: 0x5e2b590 (1088 байт) вызывается из: C_DOTA_Unit_Hero_Rubick::vfunc#538, CDOTA_ParticleManager::vfunc#9, CDOTAGCClientSystem::vfunc#1
было: 0x5e2da40 (976 байт)
- прямых вызовов: 10 → 14
- цели вызовов: +__cxa_guard_acquire() +0x5e2b460 +0x5eca0e0 +__cxa_atexit() +__cxa_guard_release()
- инструкций: 239 → 272
```diff
@@ -1,2 +1,35 @@
+push rbp
+mov rbp, rsp
+push r12
+push rbx
+movzx eax, byte ptr [D]
+lea rbx, [D]
+test al, al
+je L
+mov rax, rbx
+pop rbx
+pop r12
+pop rbp
+ret
+nop dword ptr [rax]
+lea r12, [D]
+lea rbx, [D]
+mov rdi, r12
+call F
+test eax, eax
+je L
+mov rdi, rbx
+call F
+lea rdx, [D]
+mov rsi, rbx
+lea rdi, [T]
+call F
+mov rdi, r12
+call F
+mov rax, rbx
+pop rbx
+pop r12
+pop rbp
+ret
 test rsi, rsi
 je L
```

### изменена: 0x7e66e40 (356 байт) | строки: "msgprotobuf.cpp"
было: 0x7e69200 (218 байт)
- строки: +"msgprotobuf.cpp"
- числа в инструкциях: +2 +0x30
- поля объектов: +0x78 +0x40
- прямых вызовов: 3 → 7
- цели вызовов: +0x756e190 "[M:%u:%u:%u]"; "[C:%u:%u]" +0x7e65df0 "messagelist.cpp"; "GetMessage" +0x7e649c0
- инструкций: 69 → 105
```diff
@@ -7,23 +7,24 @@
 mov r14, rdi
 push r13
-mov r13d, r9d
+mov r13d, edx
+xor edx, edx
 push r12
-mov r12, rcx
+mov r12d, r9d
 push rbx
 mov rbx, rsi
 xor esi, esi
-sub rsp, 0x18
+sub rsp, 0x28
 mov qword ptr [rdi], rax
-mov dword ptr [rbp - 0x34], edx
-xor edx, edx
 mov dword ptr [rdi + 8], 1
 mov rdi, r15
-mov dword ptr [rbp - 0x38], r8d
+mov qword ptr [rbp - 0x48], rcx
+mov dword ptr [rbp - 0x4c], r8d
 call F
-mov qword ptr [r14 + 0x70], r12
+mov rax, qword ptr [rbp - 0x48]
+mov dword ptr [r14 + 0x78], r12d
 mov rdi, rbx
-mov dword ptr [r14 + 0x78], r13d
 mov byte ptr [r14 + 0x7c], 0
 mov qword ptr [r14 + 0x10], rbx
+mov qword ptr [r14 + 0x70], rax
 call F
 mov rax, qword ptr [r14 + 0x10]
@@ -35,5 +36,32 @@
 cmp rcx, rax
 jae L
-add rsp, 0x18
+lea rsp, [rbp - 0x28]
+pop rbx
+pop r12
+pop r13
+pop r14
+pop r15
+pop rbp
+ret
+nop dword ptr [rax]
+mov rsi, qword ptr [rbx + 8]
+mov rdi, r15
+add rsi, 8
+call F
+test al, al
+je L
+cmp r13d, 2
+mov r15d, dword ptr [r14 + 0x50]
+je L
+test r15d, r15d
+jne L
+mov rax, qword ptr [rbp - 0x48]
+or dword ptr [r14 + 0x28], 0x224
+mov qword ptr [r14 + 0x40], rax
+mov eax, dword ptr [rbp - 0x4c]
+mov dword ptr [r14 + 0x50], r13d
+mov dword ptr [r14 + 0x6c], eax
+mov byte ptr [r14 + 0x7c], 1
+lea rsp, [rbp - 0x28]
 pop rbx
 pop r12
@@ -44,26 +72,34 @@
 ret
 nop word ptr [rax + rax]
-mov rsi, qword ptr [rbx + 8]
-mov rdi, r15
-add rsi, 8
+test r15d, r15d
+mov rax, qword ptr [rbp - 0x48]
+je L
+mov rdx, qword ptr [r14 + 0x40]
+cmp rdx, rax
+je L
+lea rdi, [rbp - 0x38]
+mov qword ptr [rbp - 0x38], rdx
 call F
-test al, al
-je L
-mov eax, dword ptr [r14 + 0x50]
-test eax, eax
-jne L
-mov eax, dword ptr [rbp - 0x38]
-mov qword ptr [r14 + 0x40], r12
-or dword ptr [r14 + 0x28], 0x224
-mov dword ptr [r14 + 0x6c], eax
-mov eax, dword ptr [rbp - 0x34]
-mov dword ptr [r14 + 0x50], eax
-mov byte ptr [r14 + 0x7c], 1
-add rsp, 0x18
-pop rbx
-pop r12
-pop r13
-pop r14
-pop r15
-pop rbp
-ret
+lea rdi, [rbp - 0x48]
+mov r12, rax
+call F
+mov r9d, dword ptr [r14 + 0x78]
+mov rbx, rax
+mov edi, r9d
+mov dword ptr [rbp - 0x50], r9d
+call F
+sub rsp, 8
+mov edx, 0x30
+lea rdi, [D]
+push r15
+mov r8, rax
+xor eax, eax
+push r12
+lea rcx, [D]
+push rbx
+mov r9d, dword ptr [rbp - 0x50]
```
(ещё 5 строк диффа: so-query.py fdiff libclient.so 0x7e66e40)

### изменена: 0x7e67250 (280 байт) вызывается из: CInlineJob_CMsgGCToClientAggregateMetricsBackoff::vfunc#12, CInlineJob_CMsgGCToClientEventPointsUpdated::vfunc#12, CInlineJob_CMsgGCToClientPeriodicResourceUpdated::vfunc#12 | строки: "msgprotobuf.cpp"; "CProtoBufMsg::InitFromPacket( IMsgNetPacket )"; "InitFromPacketSafe"
было: 0x7e69580 (280 байт)
- числа в инструкциях: +0xc1 −0xb9
- инструкций: 79 → 79
```diff
@@ -13,5 +13,5 @@
 mov qword ptr [rbp - 0x40], rax
 lea rax, [S:"InitFromPacketSafe"]
-mov dword ptr [rbp - 0x38], 0xb9
+mov dword ptr [rbp - 0x38], 0xc1
 mov qword ptr [rbp - 0x30], rax
 call F
```

### изменена: 0x7e67370 (269 байт) | строки: "msgprotobuf.cpp"; "CProtoBufMsg::BAsyncSendProto"; "BAsyncSendProto"
было: 0x7e696a0 (269 байт)
- числа в инструкциях: +0xf6 −0xee
- инструкций: 77 → 77
```diff
@@ -19,5 +19,5 @@
 lea rdi, [S:"CProtoBufMsg::BAsyncSendProto"]
 lea rax, [S:"BAsyncSendProto"]
-mov dword ptr [rbp - 0x48], 0xee
+mov dword ptr [rbp - 0x48], 0xf6
 mov qword ptr [rbp - 0x40], rax
 call F
```

### изменена: 0x3c8bd20 (1562 байт) | строки: "CUtlSymbolLarge"; "CUtlVector"; "CNetworkUtlVectorBase"; "%s< %s%s >"; "10CUtlVectorI15CUtlSymbolLargei28CNetworkUtlVector_MemoryTypeIS0_Lin1EEE"; "22C_NetworkUtlVectorBaseI15CUtlSymbolLargeN18C_PointClientUIHUD26NetworkVar_m_ve"; "15CUtlSymbolLarge"
- код тот же, но вызывает другую функцию: было 0x3c86c00, стало 0x3c84b00

### изменена: 0x4a82740 (238 байт)
- код тот же, но вызывает другую функцию: было 0x4a510c0, стало 0x4a4eef0

### изменена: 0x4a84280 (266 байт) | строки: "VectorWS"
- код тот же, но вызывает другую функцию: было 0x4a52f80, стало 0x4a50db0

### изменена: 0x4a84490 (467 байт) | строки: "PlayerID_t"
- код тот же, но вызывает другую функцию: было 0x4a523f0, стало 0x4a50220

### изменена: 0x4a84e30 (143 байт)
- код тот же, но вызывает другую функцию: было 0x4a51690, стало 0x4a4f4c0

### изменена: 0x4a852d0 (210 байт) | строки: "GameTime_t"; "CUtlVector"
- код тот же, но вызывает другую функцию: было 0x4a51b70, стало 0x4a4f9a0

### изменена: 0x4a85410 (419 байт)
- код тот же, но вызывает другую функцию: было 0x4a50880, стало 0x4a4e6b0

### изменена: 0x4a88500 (515 байт) | строки: "GameTime_t"; "VectorWS"
- код тот же, но вызывает другую функцию: было 0x4a524a0, стало 0x4a502d0

### изменена: 0x4a93f80 (314 байт) | строки: "AttackRecord_t"; "CUtlVector"; "CDOTA_Buff"
- код тот же, но вызывает другую функцию: было 0x4a520d0, стало 0x4a4ff00

### изменена: 0x4a780d0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x4a53030, стало 0x4a50e60

### изменена: 0x4a781a0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x4a52fc0, стало 0x4a50df0

### изменена: 0x4a78270 (206 байт)
- код тот же, но вызывает другую функцию: было 0x4a52fb0, стало 0x4a50de0

### изменена: 0x4a78340 (206 байт)
- код тот же, но вызывает другую функцию: было 0x4a52f70, стало 0x4a50da0

### изменена: 0x4a78410 (206 байт)
- код тот же, но вызывает другую функцию: было 0x4a52f00, стало 0x4a50d30

### изменена: 0x4a784e0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x4a52e30, стало 0x4a50c60

### изменена: 0x4a785b0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x4a52dc0, стало 0x4a50bf0

### изменена: 0x4a78680 (206 байт)
- код тот же, но вызывает другую функцию: было 0x4a52d40, стало 0x4a50b70

### изменена: 0x4a78750 (206 байт)
- код тот же, но вызывает другую функцию: было 0x4a52cd0, стало 0x4a50b00

### изменена: 0x4a78820 (206 байт)
- код тот же, но вызывает другую функцию: было 0x4a52c60, стало 0x4a50a90

### изменена: 0x4a788f0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x4a52bf0, стало 0x4a50a20

### изменена: 0x4a789c0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x4a52b80, стало 0x4a509b0

### изменена: 0x4a78a90 (206 байт)
- код тот же, но вызывает другую функцию: было 0x4a52b10, стало 0x4a50940

### изменена: 0x4a78b60 (206 байт)
- код тот же, но вызывает другую функцию: было 0x4a52ad0, стало 0x4a50900

### изменена: 0x4a78c30 (206 байт)
- код тот же, но вызывает другую функцию: было 0x4a527f0, стало 0x4a50620

### изменена: 0x4a78d00 (206 байт)
- код тот же, но вызывает другую функцию: было 0x4a52790, стало 0x4a505c0

### изменена: 0x4a78dd0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x4a52650, стало 0x4a50480

### изменена: 0x4a78ea0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x4a52640, стало 0x4a50470

### изменена: 0x4a78f70 (206 байт)
- код тот же, но вызывает другую функцию: было 0x4a525a0, стало 0x4a503d0

### изменена: 0x4a79040 (206 байт)
- код тот же, но вызывает другую функцию: было 0x4a52430, стало 0x4a50260

### изменена: 0x4a79110 (206 байт)
- код тот же, но вызывает другую функцию: было 0x4a523b0, стало 0x4a501e0

### изменена: 0x4a791e0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x4a52310, стало 0x4a50140

### изменена: 0x4a792b0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x4a522a0, стало 0x4a500d0

### изменена: 0x4a79380 (206 байт)
- код тот же, но вызывает другую функцию: было 0x4a52260, стало 0x4a50090

### изменена: 0x4a79450 (206 байт)
- код тот же, но вызывает другую функцию: было 0x4a521f0, стало 0x4a50020

### изменена: 0x4a79520 (206 байт)
- код тот же, но вызывает другую функцию: было 0x4a520c0, стало 0x4a4fef0

### изменена: 0x4a795f0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x4a52080, стало 0x4a4feb0

### изменена: 0x4a796c0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x4a51fd0, стало 0x4a4fe00

### изменена: 0x4a79790 (206 байт)
- код тот же, но вызывает другую функцию: было 0x4a51f60, стало 0x4a4fd90

### изменена: 0x4a79860 (206 байт)
- код тот же, но вызывает другую функцию: было 0x4a51ef0, стало 0x4a4fd20

### изменена: 0x4a79930 (206 байт)
- код тот же, но вызывает другую функцию: было 0x4a51eb0, стало 0x4a4fce0

### изменена: 0x4a79a00 (206 байт)
- код тот же, но вызывает другую функцию: было 0x4a51ea0, стало 0x4a4fcd0

### изменена: 0x4a79ad0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x4a51e30, стало 0x4a4fc60

### изменена: 0x4a79ba0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x4a51e20, стало 0x4a4fc50

### изменена: 0x4a79c70 (206 байт)
- код тот же, но вызывает другую функцию: было 0x4a51d80, стало 0x4a4fbb0

### изменена: 0x4a79d40 (206 байт)
- код тот же, но вызывает другую функцию: было 0x4a51c60, стало 0x4a4fa90

### изменена: 0x4a79e10 (206 байт)
- код тот же, но вызывает другую функцию: было 0x4a51c50, стало 0x4a4fa80

### изменена: 0x4a79ee0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x4a51ba0, стало 0x4a4f9d0

### изменена: 0x4a79fb0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x4a51b60, стало 0x4a4f990

### изменена: 0x4a7a080 (206 байт)
- код тот же, но вызывает другую функцию: было 0x4a518d0, стало 0x4a4f700

### изменена: 0x4a7a150 (206 байт)
- код тот же, но вызывает другую функцию: было 0x4a51860, стало 0x4a4f690

### изменена: 0x4a7a220 (206 байт)
- код тот же, но вызывает другую функцию: было 0x4a517f0, стало 0x4a4f620

### изменена: 0x4a7a2f0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x4a517a0, стало 0x4a4f5d0

### изменена: 0x4a7a3c0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x4a51700, стало 0x4a4f530

### изменена: 0x4a7a490 (206 байт)
- код тот же, но вызывает другую функцию: было 0x4a516c0, стало 0x4a4f4f0

### изменена: 0x4a7a560 (206 байт)
- код тот же, но вызывает другую функцию: было 0x4a51680, стало 0x4a4f4b0

### изменена: 0x4a7a630 (206 байт)
- код тот же, но вызывает другую функцию: было 0x4a51670, стало 0x4a4f4a0

### изменена: 0x4a7a700 (206 байт)
- код тот же, но вызывает другую функцию: было 0x4a51600, стало 0x4a4f430

### изменена: 0x4a7a7d0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x4a515c0, стало 0x4a4f3f0

### изменена: 0x4a7a8a0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x4a51580, стало 0x4a4f3b0

### изменена: 0x4a7a970 (206 байт)
- код тот же, но вызывает другую функцию: было 0x4a51540, стало 0x4a4f370

### изменена: 0x4a7aa40 (206 байт)
- код тот же, но вызывает другую функцию: было 0x4a51500, стало 0x4a4f330

### изменена: 0x4a7ab10 (206 байт)
- код тот же, но вызывает другую функцию: было 0x4a51490, стало 0x4a4f2c0

### изменена: 0x4a7abe0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x4a51410, стало 0x4a4f240

### изменена: 0x4a7acb0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x4a513d0, стало 0x4a4f200

### изменена: 0x4a7ad80 (206 байт)
- код тот же, но вызывает другую функцию: было 0x4a51240, стало 0x4a4f070

### изменена: 0x4a7ae50 (206 байт)
- код тот же, но вызывает другую функцию: было 0x4a51170, стало 0x4a4efa0

### изменена: 0x4a7af20 (206 байт)
- код тот же, но вызывает другую функцию: было 0x4a51100, стало 0x4a4ef30

### изменена: 0x4a7aff0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x4a51080, стало 0x4a4eeb0

### изменена: 0x4a7b0c0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x4a51030, стало 0x4a4ee60

### изменена: 0x4a7b190 (206 байт)
- код тот же, но вызывает другую функцию: было 0x4a51020, стало 0x4a4ee50

### изменена: 0x4a7b260 (206 байт)
- код тот же, но вызывает другую функцию: было 0x4a50fa0, стало 0x4a4edd0

### изменена: 0x4a7b330 (206 байт)
- код тот же, но вызывает другую функцию: было 0x4a50f60, стало 0x4a4ed90

### изменена: 0x4a7b400 (206 байт)
- код тот же, но вызывает другую функцию: было 0x4a50ef0, стало 0x4a4ed20

### изменена: 0x4a7b4d0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x4a50e20, стало 0x4a4ec50

### изменена: 0x4a7b5a0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x4a50da0, стало 0x4a4ebd0

### изменена: 0x4a7b670 (206 байт)
- код тот же, но вызывает другую функцию: было 0x4a50d60, стало 0x4a4eb90

### изменена: 0x4a7b740 (206 байт)
- код тот же, но вызывает другую функцию: было 0x4a50d20, стало 0x4a4eb50

### изменена: 0x4a7b810 (206 байт)
- код тот же, но вызывает другую функцию: было 0x4a50cb0, стало 0x4a4eae0

### изменена: 0x4a7b8e0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x4a50bb0, стало 0x4a4e9e0

### изменена: 0x4a7b9b0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x4a50b40, стало 0x4a4e970

### изменена: 0x4a7ba80 (206 байт)
- код тот же, но вызывает другую функцию: было 0x4a50aa0, стало 0x4a4e8d0

### изменена: 0x4a7bb50 (206 байт)
- код тот же, но вызывает другую функцию: было 0x4a50a60, стало 0x4a4e890

### изменена: 0x4a7bc20 (206 байт)
- код тот же, но вызывает другую функцию: было 0x4a509f0, стало 0x4a4e820

### изменена: 0x4a7bcf0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x4a50980, стало 0x4a4e7b0

### изменена: 0x4a7e9e0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4a53040, стало 0x4a50e70

### изменена: 0x4a7ea20 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4a53000, стало 0x4a50e30

### изменена: 0x4a7ea60 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4a52fd0, стало 0x4a50e00

### изменена: 0x4a7eaa0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4a52f40, стало 0x4a50d70

### изменена: 0x4a7eae0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4a52f10, стало 0x4a50d40

### изменена: 0x4a7eb20 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4a52ed0, стало 0x4a50d00

### изменена: 0x4a7eb60 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4a52ea0, стало 0x4a50cd0

### изменена: 0x4a7eba0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4a52e70, стало 0x4a50ca0

### изменена: 0x4a7ebe0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4a52e40, стало 0x4a50c70

### изменена: 0x4a7ec20 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4a52e00, стало 0x4a50c30

### изменена: 0x4a7ec60 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4a52d80, стало 0x4a50bb0

### изменена: 0x4a7eca0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4a52d50, стало 0x4a50b80

### изменена: 0x4a7ece0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4a52d10, стало 0x4a50b40

### изменена: 0x4a7ed20 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4a52ce0, стало 0x4a50b10

### изменена: 0x4a7ed60 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4a52ca0, стало 0x4a50ad0

### изменена: 0x4a7eda0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4a52c70, стало 0x4a50aa0

### изменена: 0x4a7ede0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4a52c30, стало 0x4a50a60

### изменена: 0x4a7ee20 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4a52c00, стало 0x4a50a30

### изменена: 0x4a7ee60 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4a52b90, стало 0x4a509c0

### изменена: 0x4a7eea0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4a52b50, стало 0x4a50980

### изменена: 0x4a7eee0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4a52b20, стало 0x4a50950

### изменена: 0x4a7ef20 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4a52ae0, стало 0x4a50910

### изменена: 0x4a7ef60 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4a52aa0, стало 0x4a508d0

### изменена: 0x4a7efa0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4a52a70, стало 0x4a508a0

### изменена: 0x4a7efe0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4a52a40, стало 0x4a50870

### изменена: 0x4a7f020 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4a52a10, стало 0x4a50840

### изменена: 0x4a7f060 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4a529e0, стало 0x4a50810

### изменена: 0x4a7f0a0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4a529b0, стало 0x4a507e0

### изменена: 0x4a7f0e0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4a52980, стало 0x4a507b0

### изменена: 0x4a7f120 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4a52950, стало 0x4a50780

### изменена: 0x4a7f160 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4a52920, стало 0x4a50750

### изменена: 0x4a7f1a0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4a528f0, стало 0x4a50720

### изменена: 0x4a7f1e0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4a528c0, стало 0x4a506f0

### изменена: 0x4a7f220 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4a52890, стало 0x4a506c0

### изменена: 0x4a7f260 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4a52860, стало 0x4a50690

### изменена: 0x4a7f2a0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4a52830, стало 0x4a50660

### изменена: 0x4a7f2e0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4a52800, стало 0x4a50630

### изменена: 0x4a7f320 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4a527a0, стало 0x4a505d0

### изменена: 0x4a7f360 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4a52760, стало 0x4a50590

### изменена: 0x4a7f3a0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4a52730, стало 0x4a50560

### изменена: 0x4a7f3e0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4a526d0, стало 0x4a50500

### изменена: 0x4a7f420 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4a52660, стало 0x4a50490

### изменена: 0x4a7f460 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4a52610, стало 0x4a50440

### изменена: 0x4a7f4a0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4a525e0, стало 0x4a50410

### изменена: 0x4a7f4e0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4a52570, стало 0x4a503a0

### изменена: 0x4a7f520 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4a52540, стало 0x4a50370

### изменена: 0x4a7f560 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4a52510, стало 0x4a50340

### изменена: 0x4a7f5a0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4a524e0, стало 0x4a50310

### изменена: 0x4a7f5e0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4a52470, стало 0x4a502a0

### изменена: 0x4a7f620 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4a52440, стало 0x4a50270

### изменена: 0x4a7f660 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4a52400, стало 0x4a50230

### изменена: 0x4a7f6a0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4a523c0, стало 0x4a501f0

### изменена: 0x4a7f6e0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4a52380, стало 0x4a501b0

### изменена: 0x4a7f720 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4a52350, стало 0x4a50180

### изменена: 0x4a7f760 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4a52320, стало 0x4a50150

### изменена: 0x4a7f7a0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4a522e0, стало 0x4a50110

### изменена: 0x4a7f7e0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4a522b0, стало 0x4a500e0

### изменена: 0x4a7f820 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4a52270, стало 0x4a500a0

### изменена: 0x4a7f860 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4a52230, стало 0x4a50060

### изменена: 0x4a7f8a0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4a52200, стало 0x4a50030

### изменена: 0x4a7f8e0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4a521c0, стало 0x4a4fff0

### изменена: 0x4a7f920 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4a52190, стало 0x4a4ffc0

### изменена: 0x4a7f960 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4a52160, стало 0x4a4ff90

### изменена: 0x4a7f9a0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4a52130, стало 0x4a4ff60

### изменена: 0x4a7f9e0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4a52100, стало 0x4a4ff30

### изменена: 0x4a7fa20 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4a52090, стало 0x4a4fec0

### изменена: 0x4a7fa60 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4a52050, стало 0x4a4fe80

### изменена: 0x4a7faa0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4a52010, стало 0x4a4fe40

### изменена: 0x4a7fae0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4a51fe0, стало 0x4a4fe10

### изменена: 0x4a7fb20 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4a51fa0, стало 0x4a4fdd0

### изменена: 0x4a7fb60 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4a51f70, стало 0x4a4fda0

### изменена: 0x4a7fba0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4a51f30, стало 0x4a4fd60

### изменена: 0x4a7fbe0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4a51e70, стало 0x4a4fca0

### изменена: 0x4a7fc20 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4a51e40, стало 0x4a4fc70

### изменена: 0x4a7fc60 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4a51df0, стало 0x4a4fc20

### изменена: 0x4a7fca0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4a51dc0, стало 0x4a4fbf0

### изменена: 0x4a7fce0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4a51d90, стало 0x4a4fbc0

### изменена: 0x4a7fd20 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4a51d50, стало 0x4a4fb80

### изменена: 0x4a7fd60 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4a51d20, стало 0x4a4fb50

### изменена: 0x4a7fda0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4a51ce0, стало 0x4a4fb10

### изменена: 0x4a7fde0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4a51ca0, стало 0x4a4fad0

### изменена: 0x4a7fe20 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4a51c70, стало 0x4a4faa0

### изменена: 0x4a7fe60 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4a51c20, стало 0x4a4fa50

### изменена: 0x4a7fea0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4a51bf0, стало 0x4a4fa20

### изменена: 0x4a7fee0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4a51bb0, стало 0x4a4f9e0

### изменена: 0x4a7ff20 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4a51b00, стало 0x4a4f930

### изменена: 0x4a7ff60 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4a51ad0, стало 0x4a4f900

### изменена: 0x4a7ffa0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4a51aa0, стало 0x4a4f8d0

### изменена: 0x4a7ffe0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4a51a60, стало 0x4a4f890

### изменена: 0x4a80020 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4a519d0, стало 0x4a4f800

### изменена: 0x4a80060 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4a519a0, стало 0x4a4f7d0

### изменена: 0x4a800a0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4a51970, стало 0x4a4f7a0

### изменена: 0x4a800e0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4a51940, стало 0x4a4f770

### изменена: 0x4a80120 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4a51910, стало 0x4a4f740

### изменена: 0x4a80160 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4a518e0, стало 0x4a4f710

### изменена: 0x4a801a0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4a518a0, стало 0x4a4f6d0

### изменена: 0x4a801e0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4a51870, стало 0x4a4f6a0

### изменена: 0x4a80220 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4a51830, стало 0x4a4f660

### изменена: 0x4a80260 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4a51800, стало 0x4a4f630

### изменена: 0x4a802a0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4a517b0, стало 0x4a4f5e0

### изменена: 0x4a802e0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4a51770, стало 0x4a4f5a0

### изменена: 0x4a80320 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4a51740, стало 0x4a4f570

### изменена: 0x4a80360 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4a51710, стало 0x4a4f540

### изменена: 0x4a803a0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4a516d0, стало 0x4a4f500

### изменена: 0x4a803e0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4a51610, стало 0x4a4f440

### изменена: 0x4a80420 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4a515d0, стало 0x4a4f400

### изменена: 0x4a80460 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4a51590, стало 0x4a4f3c0

### изменена: 0x4a804a0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4a51550, стало 0x4a4f380

### изменена: 0x4a804e0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4a51510, стало 0x4a4f340

### изменена: 0x4a80520 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4a514d0, стало 0x4a4f300

### изменена: 0x4a80560 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4a514a0, стало 0x4a4f2d0

### изменена: 0x4a805a0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4a51450, стало 0x4a4f280

### изменена: 0x4a805e0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4a51420, стало 0x4a4f250

### изменена: 0x4a80620 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4a513e0, стало 0x4a4f210

### изменена: 0x4a80660 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4a513a0, стало 0x4a4f1d0

### изменена: 0x4a806a0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4a51370, стало 0x4a4f1a0

### изменена: 0x4a806e0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4a51340, стало 0x4a4f170

### изменена: 0x4a80720 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4a51310, стало 0x4a4f140

### изменена: 0x4a80760 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4a512e0, стало 0x4a4f110

### изменена: 0x4a807a0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4a512b0, стало 0x4a4f0e0

### изменена: 0x4a807e0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4a51280, стало 0x4a4f0b0

### изменена: 0x4a80820 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4a51250, стало 0x4a4f080

### изменена: 0x4a80860 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4a51210, стало 0x4a4f040

### изменена: 0x4a808a0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4a511e0, стало 0x4a4f010

### изменена: 0x4a808e0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4a511b0, стало 0x4a4efe0

### изменена: 0x4a80920 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4a51180, стало 0x4a4efb0

### изменена: 0x4a80960 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4a51140, стало 0x4a4ef70

### изменена: 0x4a809a0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4a51110, стало 0x4a4ef40

### изменена: 0x4a809e0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4a510d0, стало 0x4a4ef00

### изменена: 0x4a80a20 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4a51040, стало 0x4a4ee70

### изменена: 0x4a80a60 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4a50ff0, стало 0x4a4ee20

### изменена: 0x4a80aa0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4a50fb0, стало 0x4a4ede0

### изменена: 0x4a80ae0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4a50f70, стало 0x4a4eda0

### изменена: 0x4a80b20 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4a50f30, стало 0x4a4ed60

### изменена: 0x4a80b60 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4a50ec0, стало 0x4a4ecf0

### изменена: 0x4a80ba0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4a50e90, стало 0x4a4ecc0

### изменена: 0x4a80be0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4a50e60, стало 0x4a4ec90

### изменена: 0x4a80c20 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4a50e30, стало 0x4a4ec60

### изменена: 0x4a80c60 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4a50de0, стало 0x4a4ec10

### изменена: 0x4a80ca0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4a50d70, стало 0x4a4eba0

### изменена: 0x4a80ce0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4a50d30, стало 0x4a4eb60

### изменена: 0x4a80d20 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4a50cf0, стало 0x4a4eb20

### изменена: 0x4a80d60 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4a50cc0, стало 0x4a4eaf0

### изменена: 0x4a80da0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4a50c80, стало 0x4a4eab0

### изменена: 0x4a80de0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4a50c50, стало 0x4a4ea80

### изменена: 0x4a80e20 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4a50c20, стало 0x4a4ea50

### изменена: 0x4a80e60 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4a50bf0, стало 0x4a4ea20

### изменена: 0x4a80ea0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4a50bc0, стало 0x4a4e9f0

### изменена: 0x4a80ee0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4a50b80, стало 0x4a4e9b0

### изменена: 0x4a80f20 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4a50b50, стало 0x4a4e980

### изменена: 0x4a80f60 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4a50b10, стало 0x4a4e940

### изменена: 0x4a80fa0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4a50ae0, стало 0x4a4e910

### изменена: 0x4a80fe0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4a50ab0, стало 0x4a4e8e0

### изменена: 0x4a81020 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4a50a70, стало 0x4a4e8a0

### изменена: 0x4a81060 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4a50a00, стало 0x4a4e830

### изменена: 0x4a810a0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4a509c0, стало 0x4a4e7f0

### изменена: 0x4a810e0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4a50990, стало 0x4a4e7c0

### изменена: 0x4a81120 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4a50950, стало 0x4a4e780

### изменена: 0x4a81160 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4a50920, стало 0x4a4e750

### изменена: 0x4a811a0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4a508f0, стало 0x4a4e720

### изменена: 0x4a811e0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4a508c0, стало 0x4a4e6f0

### изменена: 0x4a81220 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4a50890, стало 0x4a4e6c0

### изменена: 0x4a81260 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4a50850, стало 0x4a4e620

### изменена: 0x4a812a0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4a507c0, стало 0x4a4e5f0

### изменена: 0x4a812e0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4a50790, стало 0x4a4e5b0

### изменена: 0x4a81320 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4a50750, стало 0x4a4e570

### изменена: 0x4a81360 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4a50710, стало 0x4a4e540

### изменена: 0x4a813a0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4a506e0, стало 0x4a4e500

### изменена: 0x4a813e0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4a506a0, стало 0x4a4e4d0

### изменена: 0x4a81420 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4a50670, стало 0x4a4e480

### изменена: 0x4a81460 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4a50620, стало 0x4a4e440

### изменена: 0x4a814a0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4a505e0, стало 0x4a4e3a0

### изменена: 0x4a814e0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4a50540, стало 0x4a4e370

### изменена: 0x4a81520 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4a50510, стало 0x4a4e300

### изменена: 0x4a81560 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4a504a0, стало 0x4a4e2c0

### изменена: 0x4a815a0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4a50460, стало 0x4a4e280

### изменена: 0x4a815e0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4a50420, стало 0x4a4e250

### изменена: 0x4a81620 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4a503f0, стало 0x4a4e220

### изменена: 0x4a81660 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4a503c0, стало 0x4a4e1e0

### изменена: 0x4a816a0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4a50380, стало 0x4a4e1b0

### изменена: 0x4a816e0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4a50350, стало 0x4a4e170

### изменена: 0x4a81720 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4a50310, стало 0x4a4e130

### изменена: 0x4a81760 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4a502d0, стало 0x4a4e0e0

### изменена: 0x4a817a0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4a50280, стало 0x4a4e0b0

### изменена: 0x4a817e0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4a50250, стало 0x4a4e080

### изменена: 0x4a81820 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4a50220, стало 0x4a4e040

### изменена: 0x4a81860 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4a501e0, стало 0x4a4dff0

### изменена: 0x4a818a0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4a50190, стало 0x4a4dfc0

### изменена: 0x4a818e0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4a50160, стало 0x4a4df90

### изменена: 0x4a81920 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4a50130, стало 0x4a4df60

### изменена: 0x4a81960 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4a50100, стало 0x4a4df10

### изменена: 0x4a819a0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4a500b0, стало 0x4a4dee0

### изменена: 0x4a819e0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4a50080, стало 0x4a4dea0

### изменена: 0x4a81a20 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4a50040, стало 0x4a4de50

### изменена: 0x4a81a60 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4a4fff0, стало 0x4a4de10

### изменена: 0x4a81aa0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4a4ffb0, стало 0x4a4ddd0

### изменена: 0x4a81ae0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4a4ff70, стало 0x4a4dd80

### изменена: 0x4a81b20 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4a4ff20, стало 0x4a4dd10

### изменена: 0x4a81b60 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4a4feb0, стало 0x4a4dcc0

### изменена: 0x4a81ba0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4a4fe60, стало 0x4a4dc90

### изменена: 0x4a81be0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4a4fe30, стало 0x4a4dc60

### изменена: 0x4a81c20 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4a4fe00, стало 0x4a4dc30

### изменена: 0x4a81c60 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4a4fdd0, стало 0x4a4dbc0

### изменена: 0x4a81ca0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4a4fd60, стало 0x4a4db50

### изменена: 0x4a81ce0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4a4fcf0, стало 0x4a4db10

### изменена: 0x4a81d20 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4a4fcb0, стало 0x4a4dae0

### изменена: 0x4a81d60 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4a4fc80, стало 0x4a4daa0

### изменена: 0x4a81da0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4a4fc40, стало 0x4a4da50

### изменена: 0x4a81de0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4a4fbf0, стало 0x4a4da10

### изменена: 0x4a81e20 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4a4fbb0, стало 0x4a4d9d0

### изменена: 0x4a81e60 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4a4fb70, стало 0x4a4d990

### изменена: 0x4a81ea0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4a4fb30, стало 0x4a4d960

### изменена: 0x4a81ee0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4a4fb00, стало 0x4a4d930

### изменена: 0x4a81f20 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4a4fad0, стало 0x4a4d8f0

### изменена: 0x4a81f60 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4a4fa90, стало 0x4a4d8c0

### изменена: 0x4a81fa0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4a4fa60, стало 0x4a4d890

### изменена: 0x4a81fe0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4a4fa30, стало 0x4a4d850

### изменена: 0x4a82020 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4a4f9f0, стало 0x4a4d810

### изменена: 0x4a82060 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4a4f9b0, стало 0x4a4d7c0

### изменена: 0x4a820a0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4a4f960, стало 0x4a4d780

### изменена: 0x4a820e0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4a4f920, стало 0x4a4d750

### изменена: 0x4a82120 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4a4f8f0, стало 0x4a4d720

### изменена: 0x4a82160 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4a4f8c0, стало 0x4a4d6f0

### изменена: 0x4a821a0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4a4f890, стало 0x4a4d6b0

### изменена: 0x4a821e0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4a4f850, стало 0x4a4d640

### изменена: 0x4a82220 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4a4f7e0, стало 0x4a4d590

### изменена: 0x4a82260 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4a4f730, стало 0x4a4d550

### изменена: 0x4a822a0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4a4f6f0, стало 0x4a4d520

### изменена: 0x4a822e0 (222 байт)
- код тот же, но вызывает другую функцию: было 0x4a526c0, стало 0x4a504f0

### изменена: 0x4a823c0 (222 байт)
- код тот же, но вызывает другую функцию: было 0x4a51d10, стало 0x4a4fb40

### изменена: 0x4a824a0 (222 байт)
- код тот же, но вызывает другую функцию: было 0x4a50fe0, стало 0x4a4ee10

### изменена: 0x4a82c20 (318 байт)
- код тот же, но вызывает другую функцию: было 0x4a52db0, стало 0x4a50be0

### изменена: 0x4a82d60 (318 байт)
- код тот же, но вызывает другую функцию: было 0x4a527e0, стало 0x4a50610

### изменена: 0x4a82ea0 (318 байт)
- код тот же, но вызывает другую функцию: было 0x4a52040, стало 0x4a4fe70

### изменена: 0x4a82fe0 (318 байт)
- код тот же, но вызывает другую функцию: было 0x4a51cd0, стало 0x4a4fb00

### изменена: 0x4a83120 (318 байт)
- код тот же, но вызывает другую функцию: было 0x4a517e0, стало 0x4a4f610

### изменена: 0x4a83260 (318 байт)
- код тот же, но вызывает другую функцию: было 0x4a51480, стало 0x4a4f2b0

### изменена: 0x4a833a0 (318 байт)
- код тот же, но вызывает другую функцию: было 0x4a50e10, стало 0x4a4ec40

### изменена: 0x4a83c60 (350 байт)
- код тот же, но вызывает другую функцию: было 0x4a51070, стало 0x4a4eea0

### изменена: 0x4a83fe0 (291 байт) | строки: "VectorWS"
- код тот же, но вызывает другую функцию: было 0x4a527d0, стало 0x4a50600

### изменена: 0x4a84390 (119 байт) | строки: "VectorWS"
- код тот же, но вызывает другую функцию: было 0x4a52dd0, стало 0x4a50c00

### изменена: 0x4a84410 (119 байт) | строки: "VectorWS"
- код тот же, но вызывает другую функцию: было 0x4a50a30, стало 0x4a4e860

### изменена: 0x4a84670 (111 байт) | строки: "GameTime_t"
- код тот же, но вызывает другую функцию: было 0x4a52690, стало 0x4a504c0

### изменена: 0x4a846e0 (111 байт) | строки: "GameTime_t"
- код тот же, но вызывает другую функцию: было 0x4a525b0, стало 0x4a503e0

### изменена: 0x4a84750 (111 байт) | строки: "GameTime_t"
- код тот же, но вызывает другую функцию: было 0x4a51f00, стало 0x4a4fd30

### изменена: 0x4a847c0 (111 байт) | строки: "GameTime_t"
- код тот же, но вызывает другую функцию: было 0x4a51ec0, стало 0x4a4fcf0

### изменена: 0x4a84830 (111 байт) | строки: "GameTime_t"
- код тот же, но вызывает другую функцию: было 0x4a51a30, стало 0x4a4f860

### изменена: 0x4a848a0 (111 байт) | строки: "GameTime_t"
- код тот же, но вызывает другую функцию: было 0x4a51640, стало 0x4a4f470

### изменена: 0x4a84910 (111 байт) | строки: "GameTime_t"
- код тот же, но вызывает другую функцию: было 0x4a50f00, стало 0x4a4ed30

### изменена: 0x4a849f0 (119 байт) | строки: "VectorWS"
- код тот же, но вызывает другую функцию: было 0x4a52700, стало 0x4a50530

### изменена: 0x4a84a70 (119 байт) | строки: "VectorWS"
- код тот же, но вызывает другую функцию: было 0x4a524b0, стало 0x4a502e0

### изменена: 0x4a84af0 (119 байт) | строки: "VectorWS"
- код тот же, но вызывает другую функцию: было 0x4a51b30, стало 0x4a4f960

### изменена: 0x4a84b70 (119 байт) | строки: "VectorWS"
- код тот же, но вызывает другую функцию: было 0x4a51a00, стало 0x4a4f830

### изменена: 0x4a84da0 (143 байт) | строки: "GameTime_t"
- код тот же, но вызывает другую функцию: было 0x4a53070, стало 0x4a50ea0

### изменена: 0x4a85080 (270 байт)
- код тот же, но вызывает другую функцию: было 0x4a51a90, стало 0x4a4f8c0

### изменена: 0x4a876f0 (302 байт)
- код тот же, но вызывает другую функцию: было 0x4a51be0, стало 0x4a4fa10

### изменена: 0x4a88790 (119 байт) | строки: "VectorWS"
- код тот же, но вызывает другую функцию: было 0x4a52bc0, стало 0x4a509f0

### изменена: 0x4a92060 (175 байт) | строки: "AttackRecord_t"; "CUtlVector"
- код тот же, но вызывает другую функцию: было 0x4a50db0, стало 0x4a4ebe0

### изменена: 0x4a92110 (175 байт) | строки: "AttackRecord_t"; "CUtlVector"
- код тот же, но вызывает другую функцию: было 0x4a51090, стало 0x4a4eec0

### удалена: 0x4a47a90 (8 байт) CDOTA_Modifier_Lycan_Wolf_Bite_Attack_Range::vfunc#5 | строки: "CDOTA_Modifier_Lycan_Wolf_Bite_Attack_Range"

### удалена: 0x4a47aa0 (8 байт) CDOTA_Modifier_Lycan_Wolf_Bite_Attack_Range::vfunc#4 | строки: "modifier_lycan_wolf_bite_attack_range"

### удалена: 0x4a47ab0 (26 байт) CDOTA_Modifier_Lycan_Wolf_Bite_Attack_Range::vfunc#88

### удалена: 0x4a92090 (65 байт) CDOTA_Modifier_Lycan_Wolf_Bite_Attack_Range::OnCreated | строки: "attack_range"

### копии существующего кода (13): шаблонные / склеенные компоновщиком функции, такой же код есть и в другой сборке — не новый код
- одной копией существующего кода меньше: 0x4a47ad0 (35 байт) вызывается из: CDOTA_Modifier_Lycan_Wolf_Bite_Attack_Range::vfunc#88
- одной копией существующего кода меньше: 0x4a47b20 (3 байт) CDOTA_Modifier_Lycan_Innate_Spirit_Wolves_Self::IsHidden
- одной копией существующего кода меньше: 0x4a47b30 (3 байт) CDOTA_Modifier_Lycan_Innate_Spirit_Wolves_Self::IsPurgable
- одной копией существующего кода меньше: 0x4a47b40 (8 байт) CDOTA_Modifier_Lycan_Innate_Spirit_Wolves_Self::vfunc#6
- одной копией существующего кода меньше: 0x4a530a0 (16 байт) CDOTA_Modifier_Weaver_Threads_Of_Fate_Linger::vfunc#0
- одной копией существующего кода меньше: 0x4a530b0 (18 байт)
- одной копией существующего кода меньше: 0x4a63bc0 (83 байт) CModifierFactory<CDOTA_Modifier_Weaver_Threads_Of_Fate_Linger>::vfunc#2
- одной копией существующего кода меньше: 0x4a67130 (25 байт) CDOTA_Modifier_Jakiro_DualBreath_Thinker::vfunc#1
- одной копией существующего кода меньше: 0x4a6add0 (50 байт) CDOTA_Modifier_Jakiro_DualBreath_Thinker::vfunc#2
- одной копией существующего кода меньше: 0x4a6e360 (33 байт) CModifierFactory<CDOTA_Modifier_Weaver_Threads_Of_Fate_Linger>::vfunc#1
- одной копией существующего кода меньше: 0x4a845a0 (63 байт)
- одной копией существующего кода меньше: 0x4a8f390 (78 байт) CModifierFactory<CDOTA_Modifier_Jakiro_DualBreath_Burn>::vfunc#0
- одной копией существующего кода меньше: 0x5e2d9b0 (112 байт) вызывается из: C_DOTA_Unit_Hero_Rubick::vfunc#538, CDOTA_ParticleManager::vfunc#9, CDOTAGCClientSystem::vfunc#1

## libserver.so: функций 221950 → 221932; без изменений 221522, изменено 406, добавлено 2, удалено 6

### изменена: 0x3bf82e0 (238 байт) | строки: "_TR"
было: 0x3bf9220 (238 байт)
- строки: +"_TR" −"_UR"
- инструкций: 65 → 65
```diff
@@ -2,5 +2,5 @@
 ja L
 push rbp
-lea rdx, [S:"_UR"]
+lea rdx, [S:"_TR"]
 mov edi, edi
 mov rbp, rsp
```

### изменена: 0x3bf9f80 (323 байт) | строки: "LpR"; "CUtlSymbolLarge"; "CNetworkUtlVectorBase"
было: 0x3bfaec0 (323 байт)
- строки: +"LpR" −"LqR"
- инструкций: 99 → 99
```diff
@@ -2,5 +2,5 @@
 ja L
 push rbp
-lea rdx, [S:"LqR"]
+lea rdx, [S:"LpR"]
 mov edi, edi
 mov rbp, rsp
```

### изменена: 0x3bfa130 (317 байт) | строки: "hrR"
было: 0x3bfb070 (317 байт)
- строки: +"hrR" −"hsR"
- инструкций: 98 → 98
```diff
@@ -7,5 +7,5 @@
 push rbx
 ja L
-lea rdx, [S:"hsR"]
+lea rdx, [S:"hrR"]
 mov edi, edi
 mov rbx, rsi
```

### изменена: 0x3c28b80 (1047 байт) | строки: "oDU"; "Unsupported KV3 basic type '%s' (%d)!"; "Pointers cannot be used as numeric values"
было: 0x3c29ac0 (1047 байт)
- строки: +"oDU" −"oEU"
- инструкций: 245 → 245
```diff
@@ -47,5 +47,5 @@
 cmp r8b, 6
 ja L
-lea rcx, [S:"oEU"]
+lea rcx, [S:"oDU"]
 movzx edx, r8b
 movsxd rdx, dword ptr [rcx + rdx*4]
```

### изменена: 0x3c28fa0 (1047 байт) | строки: "sHU"; "Unsupported KV3 basic type '%s' (%d)!"; "Pointers cannot be used as numeric values"
было: 0x3c29ee0 (1047 байт)
- строки: +"sHU" −"sIU"
- инструкций: 245 → 245
```diff
@@ -47,5 +47,5 @@
 cmp r8b, 6
 ja L
-lea rcx, [S:"sIU"]
+lea rcx, [S:"sHU"]
 movzx edx, r8b
 movsxd rdx, dword ptr [rcx + rdx*4]
```

### изменена: 0x3c2a8b0 (951 байт) | строки: "IKV3TransferInterface_GameTime_Load"; "NdU"
было: 0x3c2b7f0 (951 байт)
- строки: +"NdU" −"NeU"
- инструкций: 235 → 235
```diff
@@ -63,5 +63,5 @@
 cmp al, 6
 ja L
-lea rdx, [S:"NeU"]
+lea rdx, [S:"NdU"]
 movzx eax, al
 movsxd rax, dword ptr [rdx + rax*4]
```

### изменена: 0x3c6c540 (1027 байт) | строки: "lZY"; "CEntityIOOutput"; "CBaseFilter"; "CHandle"
было: 0x3c6d480 (1027 байт)
- строки: +"lZY" −"l[Y"
- инструкций: 172 → 172
```diff
@@ -2,5 +2,5 @@
 ja L
 push rbp
-lea rdx, [S:"l[Y"]
+lea rdx, [S:"lZY"]
 mov edi, edi
 mov rbp, rsp
```

### изменена: 0x3c6d860 (653 байт) | строки: "AnY"; "%g %g %g"; "(null)"; "%g %g %g %g"; "%lld"; "%llu"; "%d %d %d %d"; "false"
было: 0x3c6e7a0 (653 байт)
- строки: +"AnY" −"AoY"
- инструкций: 159 → 159
```diff
@@ -7,5 +7,5 @@
 cmp al, 0x4f
 ja L
-lea rcx, [S:"AoY"]
+lea rcx, [S:"AnY"]
 movzx edx, al
 movsxd rdx, dword ptr [rcx + rdx*4]
```

### изменена: 0x3cbf410 (2479 байт) CBaseLightProbeVolume::vfunc#2 | строки: "box_mins"; "box_maxs"; "moveable"; "handshake"; "indoor_outdoor_level"; "StartDisabled"; "is_selected_in_hammer"; "voxel_size"
было: 0x3cc0350 (2479 байт)
- строки: +"rm^" +"{m^" +"mm^" +"Xm^" +".m^" −"rn^" −"{n^" −"mn^" −"Xn^" −".n^"
- инструкций: 618 → 618
```diff
@@ -231,5 +231,5 @@
 cmp dl, 6
 ja L
-lea rcx, [S:"rn^"]
+lea rcx, [S:"rm^"]
 movzx edx, dl
 movsxd rdx, dword ptr [rcx + rdx*4]
@@ -259,5 +259,5 @@
 cmp dl, 6
 ja L
-lea rcx, [S:"{n^"]
+lea rcx, [S:"{m^"]
 movzx edx, dl
 movsxd rdx, dword ptr [rcx + rdx*4]
@@ -287,5 +287,5 @@
 cmp dl, 6
 ja L
-lea rcx, [S:"mn^"]
+lea rcx, [S:"mm^"]
 movzx edx, dl
 movsxd rdx, dword ptr [rcx + rdx*4]
@@ -315,5 +315,5 @@
 cmp dl, 6
 ja L
-lea rcx, [S:"Xn^"]
+lea rcx, [S:"Xm^"]
 movzx edx, dl
 movsxd rdx, dword ptr [rcx + rdx*4]
@@ -344,5 +344,5 @@
 cmp dl, 6
 ja L
-lea rcx, [S:".n^"]
+lea rcx, [S:".m^"]
 movzx edx, dl
 movsxd rdx, dword ptr [rcx + rdx*4]
```

### изменена: 0x3d22020 (1712 байт) CEntityOutputTemplate<SndOpEventGuid_t>::vfunc#2 | строки: "m_Value"; "Stack depth limit hit (%d)"; "pPd"; "1Pd"; "public.aabb_min"; "public.aabb_max"
было: 0x3d22f60 (1712 байт)
- строки: +"pPd" +"1Pd" −"pQd" −"1Qd"
- инструкций: 409 → 409
```diff
@@ -65,5 +65,5 @@
 cmp al, 6
 ja L
-lea rdx, [S:"pQd"]
+lea rdx, [S:"pPd"]
 movzx eax, al
 movsxd rax, dword ptr [rdx + rax*4]
@@ -90,5 +90,5 @@
 cmp al, 6
 ja L
-lea rdx, [S:"1Qd"]
+lea rdx, [S:"1Pd"]
 movzx eax, al
 movsxd rax, dword ptr [rdx + rax*4]
```

### изменена: 0x3d2f660 (637 байт) | строки: "\\$e"; "CInfoFan"; "CHandle"; "VectorWS"
было: 0x3d305a0 (637 байт)
- строки: +"\\$e" −"\\%e"
- инструкций: 147 → 147
```diff
@@ -7,5 +7,5 @@
 cmp edi, 6
 ja L
-lea rdx, [S:"\\%e"]
+lea rdx, [S:"\\$e"]
 mov edi, edi
 mov rbx, rsi
```

### изменена: 0x3d2fae0 (547 байт) | строки: "8'e"; "CHandle"; "CBasePlayerController"; "CNetworkUtlVectorBase"; "CBasePlayerPawn"
было: 0x3d30a20 (547 байт)
- строки: +"8'e" −"8(e"
- инструкций: 158 → 158
```diff
@@ -2,5 +2,5 @@
 ja L
 push rbp
-lea rdx, [S:"8(e"]
+lea rdx, [S:"8'e"]
 mov edi, edi
 mov rbp, rsp
```

### изменена: 0x3d50c50 (183 байт)
было: 0x3d51b90 (183 байт)
- строки: −"g g"
- инструкций: 55 → 55
```diff
@@ -2,5 +2,5 @@
 ja L
 push rbp
-lea rdx, [S:"g g"]
+lea rdx, [D]
 mov edi, edi
 mov rbp, rsp
```

### изменена: 0x3d50d80 (117 байт) | строки: "9 g"
было: 0x3d51cc0 (117 байт)
- строки: +"9 g" −"9!g"
- инструкций: 39 → 39
```diff
@@ -2,5 +2,5 @@
 cmp edx, 6
 ja L
-lea rcx, [S:"9!g"]
+lea rcx, [S:"9 g"]
 push rbp
 mov rdi, rsi
```

### изменена: 0x3d50e00 (561 байт) | строки: "c g"; "Unsupported KV3 basic type '%s' (%d)!"; "Pointers cannot be used as numeric values"
было: 0x3d51d40 (561 байт)
- строки: +"c g" −"c!g"
- инструкций: 151 → 151
```diff
@@ -11,5 +11,5 @@
 cmp r8b, 6
 ja L
-lea rdx, [S:"c!g"]
+lea rdx, [S:"c g"]
 movzx eax, r8b
 movsxd rax, dword ptr [rdx + rax*4]
```

### изменена: 0x3d51100 (227 байт) | строки: "X#g"; "IPhysicsJoint"
было: 0x3d52040 (227 байт)
- строки: +"X#g" −"X$g"
- инструкций: 73 → 73
```diff
@@ -1,5 +1,5 @@
 cmp edi, 6
 ja L
-lea rcx, [S:"X$g"]
+lea rcx, [S:"X#g"]
 mov edi, edi
 push rbp
```

### изменена: 0x3d52230 (285 байт) | строки: "L4g"; "VectorWS"
было: 0x3d53170 (285 байт)
- строки: +"L4g" −"L5g"
- инструкций: 81 → 81
```diff
@@ -5,5 +5,5 @@
 push rbx
 ja L
-lea rdx, [S:"L5g"]
+lea rdx, [S:"L4g"]
 mov edi, edi
 mov rbx, rsi
```

### изменена: 0x3d52490 (893 байт) | строки: "@6g"; "InfoForResourceTypeIParticleSystemDefinition"; "CWeakHandle"; "CResourceNameTyped"; "ParticleAttachment_t"; "PrecipitationFilter_t"
было: 0x3d533d0 (893 байт)
- строки: +"@6g" −"@7g"
- инструкций: 188 → 188
```diff
@@ -9,5 +9,5 @@
 cmp edi, 6
 ja F
-lea rdx, [S:"@7g"]
+lea rdx, [S:"@6g"]
 mov edi, edi
 mov rbx, rsi
```

### изменена: 0x3d84490 (243 байт) | строки: "(1j"; "VectorWS"
было: 0x3d853d0 (243 байт)
- строки: +"(1j" −"(2j"
- инструкций: 67 → 67
```diff
@@ -1,5 +1,5 @@
 cmp edi, 6
 ja L
-lea rdx, [S:"(2j"]
+lea rdx, [S:"(1j"]
 mov edi, edi
 push rbp
```

### изменена: 0x3d84ff0 (243 байт) | строки: "<<j"; "VectorWS"
было: 0x3d85f30 (243 байт)
- строки: +"<<j" −"<=j"
- инструкций: 76 → 76
```diff
@@ -2,5 +2,5 @@
 ja L
 push rbp
-lea rdx, [S:"<=j"]
+lea rdx, [S:"<<j"]
 mov edi, edi
 mov rbp, rsp
```

### изменена: 0x3d85a00 (183 байт) | строки: "cFj"
было: 0x3d86940 (183 байт)
- строки: +"cFj" −"cGj"
- инструкций: 55 → 55
```diff
@@ -2,5 +2,5 @@
 ja L
 push rbp
-lea rdx, [S:"cGj"]
+lea rdx, [S:"cFj"]
 mov edi, edi
 mov rbp, rsp
```

### изменена: 0x3d85b30 (98 байт) | строки: "\"Gj"
было: 0x3d86a70 (98 байт)
- строки: +"\"Gj" −"\"Hj"
- инструкций: 36 → 36
```diff
@@ -2,5 +2,5 @@
 cmp edx, 6
 ja L
-lea rcx, [S:"\"Hj"]
+lea rcx, [S:"\"Gj"]
 push rbp
 mov rdi, rsi
```

### изменена: 0x3d85ba0 (98 байт) | строки: "vGj"
было: 0x3d86ae0 (98 байт)
- строки: +"vGj" −"vHj"
- инструкций: 36 → 36
```diff
@@ -2,5 +2,5 @@
 cmp edx, 6
 ja L
-lea rcx, [S:"vHj"]
+lea rcx, [S:"vGj"]
 push rbp
 mov rdi, rsi
```

### изменена: 0x3d85d80 (117 байт) | строки: "1Ij"
было: 0x3d86cc0 (117 байт)
- строки: +"1Ij" −"1Jj"
- инструкций: 39 → 39
```diff
@@ -2,5 +2,5 @@
 cmp edx, 6
 ja L
-lea rcx, [S:"1Jj"]
+lea rcx, [S:"1Ij"]
 push rbp
 mov rdi, rsi
```

### изменена: 0x3d85fd0 (136 байт) | строки: "xKj"
было: 0x3d86f10 (136 байт)
- строки: +"xKj" −"xLj"
- инструкций: 43 → 43
```diff
@@ -2,5 +2,5 @@
 cmp edx, 6
 ja L
-lea rcx, [S:"xLj"]
+lea rcx, [S:"xKj"]
 push rbp
 mov rax, rsi
```

### изменена: 0x3d87890 (302 байт) | строки: "3dj"
было: 0x3d887d0 (302 байт)
- строки: +"3dj" −"3ej"
- инструкций: 71 → 71
```diff
@@ -2,5 +2,5 @@
 ja L
 push rbp
-lea rdx, [S:"3ej"]
+lea rdx, [S:"3dj"]
 mov edi, edi
 mov rbp, rsp
```

### изменена: 0x3d880a0 (907 байт) | строки: "Dkj"
было: 0x3d88fe0 (907 байт)
- строки: +"Dkj" −"Dlj"
- инструкций: 252 → 252
```diff
@@ -9,5 +9,5 @@
 movsxd r13, edx
 push r12
-lea rdx, [S:"Dlj"]
+lea rdx, [S:"Dkj"]
 mov r12d, ecx
 push rbx
```

### изменена: 0x3d88f10 (435 байт) | строки: "`yj"; "CPlayerSlot"; "CUtlVector"
было: 0x3d89e50 (435 байт)
- строки: +"`yj" −"`zj"
- инструкций: 115 → 115
```diff
@@ -1,5 +1,5 @@
 cmp edi, 6
 ja L
-lea rdx, [S:"`zj"]
+lea rdx, [S:"`yj"]
 mov edi, edi
 push rbp
```

### изменена: 0x3d94870 (659 байт) | строки: "t1k"; "CTakeDamageInfo"; "DestructiblePartDamageRequest_t"; "CUtlLeanVector"; "VectorWS"; "TakeDamageFlags_t"; "HitGroup_t"
было: 0x3d957b0 (659 байт)
- строки: +"t1k" −"t2k"
- инструкций: 151 → 151
```diff
@@ -1,5 +1,5 @@
 cmp edi, 6
 ja L
-lea rdx, [S:"t2k"]
+lea rdx, [S:"t1k"]
 mov edi, edi
 push rbp
```

### изменена: 0x3da9bb0 (961 байт) | строки: "%g %g %g"; "(null)"; "%g %g %g %g"; "unknown_variant_type"; "1yl"; "%lld"; "%llu"; "%d %d %d %d"
было: 0x3daaaf0 (961 байт)
- строки: +"1yl" −"1zl"
- инструкций: 213 → 213
```diff
@@ -91,5 +91,5 @@
 cmp al, 0x47
 ja L
-lea rdx, [S:"1zl"]
+lea rdx, [S:"1yl"]
 movzx eax, al
 movsxd rax, dword ptr [rdx + rax*4]
```

### изменена: 0x3db77f0 (851 байт) | строки: "<Tm"; "%llu"
было: 0x3db8730 (851 байт)
- строки: +"<Tm" −"<Um"
- инструкций: 190 → 190
```diff
@@ -21,5 +21,5 @@
 mov rbx, rax
 je L
-lea r13, [S:"<Um"]
+lea r13, [S:"<Tm"]
 nop dword ptr [rax + rax]
 mov qword ptr [rbp - 0xc0], 0
```

### изменена: 0x3df6dc0 (407 байт) вызывается из: CVScriptGameSystem::vfunc#85 | строки: "D.q"
было: 0x3df7d00 (407 байт)
- строки: +"D.q" −"D/q"
- инструкций: 104 → 104
```diff
@@ -31,5 +31,5 @@
 ja L
 movzx eax, word ptr [rax + 0x28]
-lea rdx, [S:"D/q"]
+lea rdx, [S:"D.q"]
 movsxd rax, dword ptr [rdx + rax*4]
 add rax, rdx
```

### изменена: 0x3df8a60 (547 байт) | строки: "hJq"; "CHandle"; "CEnvSoundscapeTriggerable"; "CBasePlayerPawn"; "CUtlVector"
было: 0x3df99a0 (547 байт)
- строки: +"hJq" −"hKq"
- инструкций: 144 → 144
```diff
@@ -2,5 +2,5 @@
 ja L
 push rbp
-lea rdx, [S:"hKq"]
+lea rdx, [S:"hJq"]
 mov edi, edi
 mov rbp, rsp
```

### изменена: 0x3e19d40 (4702 байт) | строки: "classname"; "PWs"; "connections"; "attributes"; "X]s"
было: 0x3e1ac80 (4702 байт)
- строки: +"PWs" +"X]s" −"PXs" −"X^s"
- инструкций: 1086 → 1086
```diff
@@ -208,5 +208,5 @@
 cmp r14b, 0x4f
 ja L
-lea rsi, [S:"PXs"]
+lea rsi, [S:"PWs"]
 movsxd rax, dword ptr [rsi + r14*4]
 add rax, rsi
@@ -617,5 +617,5 @@
 cmp al, 0x4f
 ja L
-lea rsi, [S:"X^s"]
+lea rsi, [S:"X]s"]
 movzx edx, al
 movsxd rdx, dword ptr [rsi + rdx*4]
```

### изменена: 0x3e6bf80 (187 байт) | строки: "hYx"; "Disposition_t"
было: 0x3e6cec0 (187 байт)
- строки: +"hYx" −"hZx"
- инструкций: 59 → 59
```diff
@@ -1,5 +1,5 @@
 cmp edi, 6
 ja L
-lea rdx, [S:"hZx"]
+lea rdx, [S:"hYx"]
 mov edi, edi
 push rbp
```

### изменена: 0x3e6c170 (275 байт) | строки: "D[x"; "VectorWS"
было: 0x3e6d0b0 (275 байт)
- строки: +"D[x" −"D\\x"
- инструкций: 84 → 84
```diff
@@ -1,5 +1,5 @@
 cmp edi, 6
 ja L
-lea rcx, [S:"D\\x"]
+lea rcx, [S:"D[x"]
 mov edi, edi
 push rbp
```

### изменена: 0x3e6cd80 (451 байт) | строки: "$gx"; "CEconWearable"; "CHandle"; "CNetworkUtlVectorBase"; "RelationshipOverride_t"; "CUtlVector"; "Hull_t"; "CMovementStatsProperty"
было: 0x3e6dcc0 (451 байт)
- строки: +"$gx" −"$hx"
- инструкций: 129 → 129
```diff
@@ -2,5 +2,5 @@
 ja L
 push rbp
-lea rdx, [S:"$hx"]
+lea rdx, [S:"$gx"]
 mov edi, edi
 mov rbp, rsp
```

### изменена: 0x3e6df70 (183 байт) | строки: "?yx"
было: 0x3e6eeb0 (183 байт)
- строки: +"?yx" −"?zx"
- инструкций: 55 → 55
```diff
@@ -2,5 +2,5 @@
 ja L
 push rbp
-lea rdx, [S:"?zx"]
+lea rdx, [S:"?yx"]
 mov edi, edi
 mov rbp, rsp
```

### изменена: 0x3e6e0a0 (183 байт) | строки: "Szx"
было: 0x3e6efe0 (183 байт)
- строки: +"Szx" −"S{x"
- инструкций: 55 → 55
```diff
@@ -2,5 +2,5 @@
 ja L
 push rbp
-lea rdx, [S:"S{x"]
+lea rdx, [S:"Szx"]
 mov edi, edi
 mov rbp, rsp
```

### изменена: 0x3e6e240 (98 байт) | строки: "f{x"
было: 0x3e6f180 (98 байт)
- строки: +"f{x" −"f|x"
- инструкций: 36 → 36
```diff
@@ -2,5 +2,5 @@
 cmp edx, 6
 ja L
-lea rcx, [S:"f|x"]
+lea rcx, [S:"f{x"]
 push rbp
 mov rdi, rsi
```

### изменена: 0x3e6e470 (171 байт) | строки: "@}x"; "HitGroup_t"
было: 0x3e6f3b0 (171 байт)
- строки: +"@}x" −"@~x"
- инструкций: 54 → 54
```diff
@@ -1,5 +1,5 @@
 cmp edi, 6
 ja L
-lea rdx, [S:"@~x"]
+lea rdx, [S:"@}x"]
 mov edi, edi
 push rbp
```

### изменена: 0x3ea9860 (769 байт) вызывается из: CAnimGraphControllerBase::vfunc#2, CEmptyGraphController::vfunc#2, EventGrantDefinition_Emoticon_t::vfunc#2 | строки: "\"-|"; "Unsupported KV3 basic type '%s' (%d)!"; "Pointers cannot be used as numeric values"
было: 0x3eaa7a0 (769 байт)
- строки: +"\"-|" −"\".|"
- инструкций: 220 → 220
```diff
@@ -31,5 +31,5 @@
 cmp bl, 6
 ja L
-lea rdx, [S:"\".|"]
+lea rdx, [S:"\"-|"]
 movzx eax, bl
 movsxd rax, dword ptr [rdx + rax*4]
```

### изменена: 0x3eabe70 (856 байт) | строки: "|P|"
было: 0x3eacdb0 (856 байт)
- строки: +"|P|" −"|Q|"
- инструкций: 221 → 221
```diff
@@ -10,5 +10,5 @@
 movsxd r12, edx
 push rbx
-lea rdx, [S:"|Q|"]
+lea rdx, [S:"|P|"]
 mov rbx, rsi
 sub rsp, 0x58
```

### изменена: 0x3eade80 (904 байт) | строки: "8p|"
было: 0x3eaedc0 (904 байт)
- строки: +"8p|" −"8q|"
- инструкций: 237 → 237
```diff
@@ -7,5 +7,5 @@
 mov r15d, edx
 push r14
-lea rdx, [S:"8q|"]
+lea rdx, [S:"8p|"]
 push r13
 push r12
```

### изменена: 0x482c750 (457 байт) CDOTA_Modifier_Chen_Zealot_Aura::GetAuraEntityReject | строки: "modifier_kill"; "modifier_chen_zealot_buff"
было: 0x47de0d0 (240 байт)
- строки: +"modifier_kill"
- числа в инструкциях: +-1 +-2 +9 +0x3f +0x1ff +0x70 +3
- поля объектов: +0xd3c +0xc18 +0x1780 +0x1780 +0x10 +0x5d1
- прямых вызовов: 7 → 12
- цели вызовов: +CDOTA_BaseNPC::vfunc#387
- инструкций: 72 → 129
```diff
@@ -30,13 +30,14 @@
 cmp byte ptr [rbx + 0x175a], 0
 jne L
-movzx r13d, byte ptr [rbx + 0xd8d]
-test r13b, r13b
+mov rdx, qword ptr [rbx]
+lea rcx, [T]
+mov rdx, qword ptr [rdx + 0xc18]
+cmp rdx, rcx
 jne L
 test eax, 0x110
 je L
-nop dword ptr [rax + rax]
-mov r13d, 1
+mov r14d, 1
 pop rbx
-mov eax, r13d
+mov eax, r14d
 pop r12
 pop r13
@@ -56,6 +57,30 @@
 cmp eax, r14d
 jne L
+movzx r14d, byte ptr [rbx + 0xd8d]
+xor edx, edx
+test r14b, r14b
+je L
+lea rsi, [S:"modifier_kill"]
+mov rdi, rbx
+call F
+test rax, rax
+mov rdi, rax
+je L
+call F
+mov rdi, r13
+mov rbx, rax
+call F
+cmp rbx, rax
+sete r14b
+xor r14d, 1
+jmp L
+nop dword ptr [rax + rax]
+mov rdi, rbx
+call rdx
+test al, al
+jne L
+mov eax, dword ptr [rbx + 0xd3c]
+jmp L
 lea rsi, [S:"modifier_chen_zealot_buff"]
-xor edx, edx
 mov rdi, rbx
 call F
@@ -66,7 +91,39 @@
 cmp r12, rax
 je L
-mov r13, qword ptr [rbx + 0x1248]
-shr r13, 0x1f
-and r13d, 1
-xor r13d, 1
+mov r14, qword ptr [rbx + 0x1248]
+shr r14, 0x1f
+and r14d, 1
 jmp L
+mov edx, dword ptr [rbx + 0x1780]
+cmp edx, -1
+je L
+cmp edx, -2
+mov rax, qword ptr [D]
+je L
+test rax, rax
+je L
+movzx ecx, word ptr [rbx + 0x1780]
+mov rsi, rcx
+shr rsi, 9
+and esi, 0x3f
+mov rax, qword ptr [rax + rsi*8]
```
(ещё 20 строк диффа: so-query.py fdiff libserver.so 0x482c750)

### изменена: 0x48543b0 (1199 байт) CDOTA_Modifier_Batrider_FlamingLasso::vfunc#2 | строки: "modifier_faceless_void_chronosphere_freeze"; "modifier_enigma_black_hole_pull"
было: 0x48551f0 (1111 байт)
- числа в инструкциях: +-1 +-2 +9 +0x3f +0x1ff +0x70
- поля объектов: +0x1b14 +0x1b14 +0x10
- прямых вызовов: 20 → 19
- инструкций: 267 → 287
```diff
@@ -48,11 +48,26 @@
 call F
 movss dword ptr [rbp - 0x64], xmm0
-lea r13, [rbx + 0x1b14]
+mov ecx, dword ptr [rbx + 0x1b14]
+cmp ecx, -1
+je L
+mov rsi, qword ptr [D]
+test rsi, rsi
+je L
+cmp ecx, -2
+je L
+movzx eax, word ptr [rbx + 0x1b14]
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
+mov r13, qword ptr [rax]
 mov rdi, r13
-call F
-test rax, rax
-mov rdi, rax
-je L
-mov rdi, qword ptr [rax]
 call F
 pxor xmm0, xmm0
@@ -82,4 +97,5 @@
 pop rbp
 ret
+nop word ptr [rax + rax]
 mov rdi, rbx
 call F
@@ -138,27 +154,27 @@
 mov rdi, r12
 call F
-mov ecx, dword ptr [rbx + 0x1b14]
+mov edx, dword ptr [rbx + 0x1b14]
 mov r14, rax
-cmp ecx, -1
-je L
-mov rsi, qword ptr [D]
-test rsi, rsi
-je L
-cmp ecx, -2
+cmp edx, -1
+je L
+mov rsi, qword ptr [D]
+test rsi, rsi
+je L
+cmp edx, -2
 je L
 movzx eax, word ptr [rbx + 0x1b14]
-mov rdx, rax
-shr rdx, 9
-and edx, 0x3f
-mov rdx, qword ptr [rsi + rdx*8]
-test rdx, rdx
-je L
-and eax, 0x1ff
-imul rax, rax, 0x70
-add rax, rdx
-cmp ecx, dword ptr [rax + 0x10]
-jne L
-mov r13, qword ptr [rax]
-mov rdi, r13
+mov rcx, rax
+shr rcx, 9
+and ecx, 0x3f
+mov rdi, qword ptr [rsi + rcx*8]
```
(ещё 46 строк диффа: so-query.py fdiff libserver.so 0x48543b0)

### изменена: 0x4858140 (9536 байт) | строки: "Hero_Batrider.Firefly.Loop"
было: 0x4859300 (8816 байт)
- константы из данных (числа логики): +0x00000000000000090000000000000000
- числа в инструкциях: +0xffffffff +0 +0 +0 +0 +0 +0 +0 (и ещё 19)
- прямых вызовов: 90 → 97
- цели вызовов: +0x47ee820 +0x480dc60
- инструкций: 1386 → 1498
```diff
@@ -1,2 +1,114 @@
+push rbp
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
```
(ещё 39 строк диффа: so-query.py fdiff libserver.so 0x4858140)

### изменена: 0x485dfe0 (1083 байт) | строки: "PlayerID_t"
было: 0x485e380 (3963 байт)
- константы из данных (числа логики): −0x00000000000000090000000000000000 −0x00000000000000090000000000000000 −0x00000000000000090000000000000000 −0x00000000000000090000000000000000
- числа в инструкциях: −0xffffffff −0xffffffff −0xffffffff −0xffffffff −0 −0 −0 −0 (и ещё 100)
- прямых вызовов: 40 → 12
- цели вызовов: −__cxa_guard_acquire() −0x6a41870 −__cxa_atexit() −__cxa_guard_release() −0x59dabe0 −0x4810390 −0x480dfe0 −0x3bbb2c0 −0x48103a0 −0x480e000 −0x48103b0 −0x480e020 −0x48103c0 −0x480e040
- инструкций: 677 → 229
```diff
@@ -1,450 +1,2 @@
-push rbp
-mov rbp, rsp
-push rbx
-sub rsp, 8
-movzx eax, byte ptr [D]
-test al, al
-je L
-mov rax, qword ptr [D]
-test rax, rax
-je L
-mov rbx, qword ptr [rbp - 8]
-leave
-ret
-nop word ptr [rax + rax]
-lea rbx, [D]
-mov rdi, rbx
-call F
-test eax, eax
-je L
-pxor xmm0, xmm0
-mov eax, 0xffffffff
-movdqa xmm1, xmmword ptr [K:0x00000000000000090000000000000000]
-movups xmmword ptr [D], xmm0
-movups xmmword ptr [D], xmm0
-lea rsi, [D]
-movups xmmword ptr [D], xmm0
-movups xmmword ptr [D], xmm0
-movups xmmword ptr [D], xmm0
-movups xmmword ptr [D], xmm1
-movups xmmword ptr [D], xmm0
-mov qword ptr [D], rax
-mov qword ptr [D], 0
-mov qword ptr [D], 0
-mov qword ptr [D], 0
-mov qword ptr [D], 0
-mov qword ptr [D], 0
-mov qword ptr [D], 0
-mov qword ptr [D], 0
-mov qword ptr [D], 0
-mov qword ptr [D], 0
-mov qword ptr [D], 0
-mov qword ptr [D], 0
-mov qword ptr [D], 0
-mov qword ptr [D], 0
-mov qword ptr [D], 0
-mov qword ptr [D], 0
-mov qword ptr [D], 0
-mov qword ptr [D], 0x20
-mov qword ptr [D], 0
-mov qword ptr [D], 0
-mov qword ptr [D], 0
-mov qword ptr [D], 0
-mov qword ptr [D], 0
-mov qword ptr [D], 0
-mov qword ptr [D], 0
-lea rax, [D]
-lea rdi, [T]
-mov rdx, qword ptr [rax]
-mov qword ptr [rax], rsi
-mov qword ptr [D], rdx
-lea rdx, [D]
-mov eax, dword ptr [rdx]
-lea ecx, [rax + 1]
-mov dword ptr [D], eax
-mov dword ptr [rdx], ecx
-lea rdx, [D]
-call F
-mov rdi, rbx
-call F
-mov rax, qword ptr [D]
-test rax, rax
-jne L
-nop
-movzx eax, byte ptr [D]
-test al, al
```
(ещё 375 строк диффа: so-query.py fdiff libserver.so 0x485dfe0)

### изменена: 0x48b63c0 (860 байт) | строки: "scepter_brewling_items"; "<NoAbilityName>"; "modifier_brewmaster_primal_split_scepter_item"; "original_item"; "brewling_item"
было: 0x48ac550 (899 байт)
- числа в инструкциях: +1 +1 +1 +1
- цели вызовов: +0x3bbf080
- инструкций: 216 → 216
```diff
@@ -9,5 +9,5 @@
 mov r12, rdi
 push rbx
-sub rsp, 0x68
+sub rsp, 0x58
 call F
 test rax, rax
@@ -55,5 +55,5 @@
 call F
 cmp eax, 5
-mov dword ptr [rbp - 0x88], eax
+mov dword ptr [rbp - 0x78], eax
 jbe L
 lea rsp, [rbp - 0x28]
@@ -65,5 +65,5 @@
 pop rbp
 ret
-nop
+nop dword ptr [rax + rax]
 mov rdi, r13
 call F
@@ -95,5 +95,5 @@
 push 0
 push 0
-mov ecx, dword ptr [rbp - 0x88]
+mov ecx, dword ptr [rbp - 0x78]
 call F
 add rsp, 0x20
@@ -116,10 +116,10 @@
 mov rdi, rax
 call F
-mov ecx, dword ptr [rbp - 0x88]
+mov ecx, dword ptr [rbp - 0x78]
 cmp eax, ecx
 je L
 mov rdi, r13
 call F
-mov edx, dword ptr [rbp - 0x88]
+mov edx, dword ptr [rbp - 0x78]
 mov rsi, r15
 mov rdi, rax
@@ -133,14 +133,11 @@
 cmp byte ptr [r15 + 0x874], 0
 lea rax, [rbp - 0x70]
-mov qword ptr [rbp - 0x88], rax
-je L
-lea rax, [rbp - 0x68]
+mov qword ptr [rbp - 0x78], rax
+je L
+lea rdi, [rbp - 0x60]
 xor edx, edx
 pxor xmm0, xmm0
-mov dword ptr [rbp - 0x74], 0x874
-lea rsi, [rbp - 0x74]
-mov rdi, rax
+mov esi, 1
 movaps xmmword ptr [rbp - 0x50], xmm0
-mov qword ptr [rbp - 0x90], rax
 mov word ptr [rbp - 0x34], dx
 mov qword ptr [rbp - 0x70], 1
@@ -151,22 +148,22 @@
 mov dword ptr [rbp - 0x38], 0xffffffff
 call F
-mov rdx, qword ptr [r15]
-mov rdi, r15
-mov rsi, qword ptr [rbp - 0x88]
-call qword ptr [rdx + 0xf0]
-mov rdi, qword ptr [rbp - 0x90]
+mov rax, qword ptr [rbp - 0x60]
+mov rdi, r15
+add dword ptr [rbp - 0x68], 1
+mov rsi, qword ptr [rbp - 0x78]
+mov dword ptr [rax], 0x874
+mov rax, qword ptr [r15]
+call qword ptr [rax + 0xf0]
+lea rdi, [rbp - 0x68]
```
(ещё 51 строк диффа: so-query.py fdiff libserver.so 0x48b63c0)

### изменена: 0x48b7070 (1136 байт) CDOTA_Ability_Primal_Companion::OnSpellStart | строки: "brewmaster_primal_split"; "brewmaster_drunken_brawler"; "npc_dota_brewmaster_fire_%1d"; "npc_dota_brewmaster_earth_%1d"; "modifier_brewmaster_primal_companion"; "npc_dota_brewmaster_storm_%1d"
было: 0x48b05c0 (1040 байт)
- числа в инструкциях: +1
- поля объектов: +0x1afc
- прямых вызовов: 29 → 33
- цели вызовов: +0x61fcda0 +0x5a891f0 "<NoAbilityName>"
- инструкций: 239 → 259
```diff
@@ -238,2 +238,22 @@
 movss xmm1, dword ptr [rbp - 0x148]
 jmp L
+mov rbx, qword ptr [rbp - 0x200]
+mov rdi, rbx
+call F
+pxor xmm0, xmm0
+mov edx, 1
+xor edi, edi
+cvtsi2ss xmm0, dword ptr [rbx + 0x1afc]
+mov rsi, rax
+call F
+mov rdi, rbx
+movss dword ptr [rbp - 0x1d8], xmm0
+call F
+movss xmm0, dword ptr [rbp - 0x1d8]
+xor edx, edx
+lea rdi, [D]
+mov rsi, rax
+cvttss2si ecx, xmm0
+call F
+mov eax, dword ptr [0xd3c]
+ud2
```

### изменена: 0x48b8c50 (4111 байт) CDOTA_Ability_Enchantress_Enchant::OnSpellStart | строки: "dominate_duration"; "slow_duration"; "modifier_enchantress_enchant_controlled"; "modifier_dominated"; "enchanted_creep"; "xp_gain_pct"; "modifier_kill"; "duration"
было: 0x48b9bd0 (4111 байт)
- числа в инструкциях: +1 +1
- инструкций: 889 → 890
```diff
@@ -7,5 +7,5 @@
 push rbx
 mov rbx, rdi
-sub rsp, 0x1c8
+sub rsp, 0x1b8
 call F
 test rax, rax
@@ -23,10 +23,10 @@
 xor edx, edx
 mov rdi, rbx
-movss dword ptr [rbp - 0x1c0], xmm0
+movss dword ptr [rbp - 0x1b0], xmm0
 movss xmm0, dword ptr [K:-1]
 lea rsi, [S:"slow_duration"]
 call F
 test byte ptr [r12 + 0x1249], 2
-movss dword ptr [rbp - 0x1b4], xmm0
+movss dword ptr [rbp - 0x1a4], xmm0
 je L
 lea rsp, [rbp - 0x28]
@@ -69,5 +69,5 @@
 mov rdi, r12
 mov rsi, rax
-mov qword ptr [rbp - 0x1e0], rax
+mov qword ptr [rbp - 0x1d0], rax
 call F
 test rax, rax
@@ -105,5 +105,5 @@
 mov esi, r13d
 mov rdi, rax
-mov qword ptr [rbp - 0x1d0], rax
+mov qword ptr [rbp - 0x1c0], rax
 call F
 sub dword ptr [rbx + 0x860], 1
@@ -148,5 +148,5 @@
 mov r15, rax
 mov rdi, rax
-mov qword ptr [rbp - 0x1d8], rax
+mov qword ptr [rbp - 0x1c8], rax
 lea rsi, [S:"enchanted_creep"]
 call F
@@ -159,5 +159,5 @@
 cmp qword ptr [rbp - 0x180], 0
 je L
-mov rdi, qword ptr [rbp - 0x1d8]
+mov rdi, qword ptr [rbp - 0x1c8]
 call F
 mov rax, qword ptr [r12]
@@ -261,5 +261,5 @@
 pxor xmm1, xmm1
 comiss xmm0, xmm1
-movss dword ptr [rbp - 0x1c8], xmm0
+movss dword ptr [rbp - 0x1b8], xmm0
 ja L
 mov rdi, rbx
@@ -288,5 +288,5 @@
 call F
 test rax, rax
-mov qword ptr [rbp - 0x1c8], rax
+mov qword ptr [rbp - 0x1b8], rax
 je L
 test r14b, r14b
@@ -295,13 +295,13 @@
 mov edi, dword ptr [rax + 0x38]
 call F
-mov rdx, qword ptr [rbp - 0x1c8]
-movss dword ptr [rbp - 0x1e8], xmm0
+mov rdx, qword ptr [rbp - 0x1b8]
+movss dword ptr [rbp - 0x1d8], xmm0
 mov rax, qword ptr [rdx]
 mov rdi, rdx
 call qword ptr [rax + 0x1d0]
-subss xmm0, dword ptr [rbp - 0x1e8]
-movss xmm3, dword ptr [rbp - 0x1c0]
+subss xmm0, dword ptr [rbp - 0x1d8]
+movss xmm3, dword ptr [rbp - 0x1b0]
```
(ещё 372 строк диффа: so-query.py fdiff libserver.so 0x48b8c50)

### изменена: 0x48d48d0 (6232 байт) вызывается из: CDOTA_Ability_Dazzle_NothlProjection::OnSpellStart | строки: "shadow_wave_cdr"; "healing_amp"; "leash_start"; "base_leash_pull"; "leash_increase"; "modifier_dazzle_nothl_projection_soul_clone"; "<NoAbilityName>"; "dazzle_nothl_projection_end"
было: 0x48d5850 (6248 байт)
- числа в инструкциях: +1 +1
- поля объектов: −0x7b0 −0x7b0
- инструкций: 1239 → 1237
```diff
@@ -158,8 +158,6 @@
 je L
 cmp byte ptr [r12 + 0x818], 0
-jne L
-mov eax, dword ptr [r12 + 0x7b0]
-cmp dword ptr [r14 + 0x7b0], eax
-jge L
+je L
+jmp L
 nop dword ptr [rax]
 xor esi, esi
@@ -1109,14 +1107,11 @@
 mov dword ptr [r12 + 0x85c], eax
 jmp L
-lea rdx, [rbp - 0x138]
 xor eax, eax
+mov esi, 1
 pxor xmm1, xmm1
-movss dword ptr [rbp - 0x1d8], xmm0
-mov rdi, rdx
+movss dword ptr [rbp - 0x1c8], xmm0
+lea rdi, [rbp - 0x130]
 movaps xmmword ptr [rbp - 0x120], xmm1
-lea rsi, [rbp - 0x180]
-mov qword ptr [rbp - 0x1c8], rdx
 mov word ptr [rbp - 0x104], ax
-mov dword ptr [rbp - 0x180], 0x7dc
 mov qword ptr [rbp - 0x140], 1
 mov qword ptr [rbp - 0x138], 0
@@ -1126,11 +1121,14 @@
 mov dword ptr [rbp - 0x108], 0xffffffff
 call F
+mov rax, qword ptr [rbp - 0x130]
+mov rdi, r14
+add dword ptr [rbp - 0x138], 1
+mov rsi, qword ptr [rbp - 0x1d0]
+mov dword ptr [rax], 0x7dc
 mov rax, qword ptr [r14]
-mov rdi, r14
-mov rsi, qword ptr [rbp - 0x1d0]
 call qword ptr [rax + 0xf0]
-mov rdi, qword ptr [rbp - 0x1c8]
-call F
-movss xmm0, dword ptr [rbp - 0x1d8]
+lea rdi, [rbp - 0x138]
+call F
+movss xmm0, dword ptr [rbp - 0x1c8]
 movss dword ptr [r14 + 0x7dc], xmm0
 jmp L
@@ -1144,5 +1142,5 @@
 xor esi, esi
 jmp L
-nop dword ptr [rax]
+nop word ptr [rax + rax]
 mov r14, qword ptr [rbp - 0x1d0]
 xor ecx, ecx
```

### изменена: 0x48d7e00 (2356 байт) CDOTA_Modifier_Batrider_Firefly::OnIntervalThink | строки: "particles/units/heroes/hero_batrider/batrider_firefly_debuff.vpcf"
было: 0x48d8da0 (2336 байт)
- числа в инструкциях: +0x3fffffff −0
- виртуальные вызовы: +0x20 (слот 4)
- поля объектов: +0x1b38
- цели вызовов: −0x44e2130
- инструкций: 473 → 477
```diff
@@ -7,5 +7,5 @@
 mov r12, rdi
 push rbx
-sub rsp, 0x118
+sub rsp, 0x128
 call F
 mov rdi, r12
@@ -36,4 +36,5 @@
 mov edi, eax
 call F
+mov edx, dword ptr [r12 + 0x1b38]
 movaps xmm1, xmm0
 movss xmm0, dword ptr [r12 + 0x1b20]
@@ -42,5 +43,4 @@
 je L
 jbe L
-mov edx, dword ptr [r12 + 0x1b38]
 test edx, edx
 jle L
@@ -147,9 +147,7 @@
 pop rbp
 jmp F
-mov ecx, dword ptr [r12 + 0x1b38]
-mov dword ptr [rbp - 0xfc], 0
 addss xmm0, dword ptr [r12 + 0x1b14]
+test edx, edx
 movss dword ptr [r12 + 0x1b20], xmm0
-test ecx, ecx
 jle L
 xor r13d, r13d
@@ -157,10 +155,11 @@
 xor ebx, ebx
 mov qword ptr [rbp - 0x120], 0
+mov dword ptr [rbp - 0x118], 0
+mov r14, r13
 mov dword ptr [rbp - 0x114], 0
-mov r14, r13
-mov byte ptr [rbp - 0x139], 0
-movss dword ptr [rbp - 0x118], xmm2
-movss dword ptr [rbp - 0x140], xmm1
-nop
+mov byte ptr [rbp - 0x13d], 0
+movss dword ptr [rbp - 0x13c], xmm2
+movss dword ptr [rbp - 0x144], xmm1
+nop word ptr [rax + rax]
 mov qword ptr [rbp - 0xf0], 0
 mov rdi, r12
@@ -365,18 +364,22 @@
 cmp dword ptr [r12 + 0x1b38], eax
 jg L
-movss xmm2, dword ptr [rbp - 0x118]
+movss xmm2, dword ptr [rbp - 0x13c]
 pxor xmm0, xmm0
 mov r13, r14
-movss xmm1, dword ptr [rbp - 0x140]
+movss xmm1, dword ptr [rbp - 0x144]
 comiss xmm2, xmm0
 ja L
-mov eax, dword ptr [rbp - 0x114]
-lea rdi, [rbp - 0x110]
-movss dword ptr [rbp - 0x120], xmm1
-mov dword ptr [rbp - 0x110], ebx
-mov qword ptr [rbp - 0x108], r13
-mov dword ptr [rbp - 0x100], eax
-call F
-movss xmm1, dword ptr [rbp - 0x120]
+cmp dword ptr [rbp - 0x118], 0x3fffffff
+ja L
+test r13, r13
+je L
+mov rax, qword ptr [D]
+movss dword ptr [rbp - 0x114], xmm1
+mov rsi, r13
+mov rdi, qword ptr [rax]
+mov rax, qword ptr [rdi]
+call qword ptr [rax + 0x20]
```
(ещё 98 строк диффа: so-query.py fdiff libserver.so 0x48d7e00)

### изменена: 0x4995760 (388 байт) CDOTA_Ability_Lycan_Wolf_Bite::OnSpellStart | строки: "lycan_shapeshift"; "modifier_lycan_shapeshift_transform"; "transformation_time"; "duration"
было: 0x4996920 (452 байт)
- строки: −"modifier_lycan_wolf_bite_attack_range"
- прямых вызовов: 17 → 13
- инструкций: 118 → 100
```diff
@@ -7,5 +7,5 @@
 mov r12, rdi
 push rbx
-sub rsp, 0x58
+sub rsp, 0x38
 call F
 test rax, rax
@@ -22,5 +22,5 @@
 cmp byte ptr [rax + 0x624], r13b
 je L
-add rsp, 0x58
+add rsp, 0x38
 pop rbx
 pop r12
@@ -52,5 +52,5 @@
 xor r8d, r8d
 mov rdi, r13
-lea r14, [rbp - 0x70]
+lea r14, [rbp - 0x50]
 mov ecx, 1
 mov edx, 1
@@ -62,7 +62,7 @@
 mov rsi, r15
 mov rdi, r14
-movss dword ptr [rbp - 0x74], xmm0
+movss dword ptr [rbp - 0x54], xmm0
 call F
-movss xmm0, dword ptr [rbp - 0x74]
+movss xmm0, dword ptr [rbp - 0x54]
 lea rsi, [S:"duration"]
 mov rdi, r14
@@ -70,33 +70,15 @@
 mov rdi, r12
 call F
+mov rdi, rbx
 xor r9d, r9d
 mov r8, r14
+mov rsi, rax
 mov rcx, r15
 mov rdx, r13
-mov rdi, rbx
-mov rsi, rax
-call F
-lea r13, [rbp - 0x50]
-xor ecx, ecx
-xor edx, edx
-lea r15, [S:"modifier_lycan_wolf_bite_attack_range"]
-mov rdi, r13
-mov rsi, r15
-call F
-mov rdi, r12
-call F
-xor r9d, r9d
-mov r8, r13
-mov rcx, r15
-mov rsi, rax
-mov rdx, r12
-mov rdi, rbx
-call F
-mov rdi, r13
 call F
 mov rdi, r14
 call F
 jmp L
-nop word ptr [rax + rax]
+nop dword ptr [rax]
 cmp byte ptr [r12 + 0x7e0], 0
 je L
```

### изменена: 0x49d8e60 (3113 байт) CDOTA_Ability_SpiritBreaker_ChargeOfDarkness::vfunc#372 | строки: "modifier_spirit_breaker_greater_bash"; "bash_radius"; "particles/units/heroes/hero_spirit_breaker/spirit_breaker_charge_tree.vpcf"; "modifier_spirit_breaker_charge_of_darkness_vision"; "modifier_spirit_breaker_charge_of_darkness_target"; "target"
было: 0x49da0e0 (3081 байт)
- числа в инструкциях: +0 +0x3fffffff
- виртуальные вызовы: +0x20 (слот 4)
- цели вызовов: −0x44e3320
- инструкций: 623 → 631
```diff
@@ -519,11 +519,19 @@
 mov edx, eax
 je L
+add edx, 1
 mov ecx, dword ptr [rbx + 0x888]
-lea rdi, [rbp - 0x48]
-add edx, 1
 mov dword ptr [rbx + 0x890], edx
 mov rdx, qword ptr [rbx + 0x898]
 mov dword ptr [rdx + rax*4], ecx
-call F
+cmp dword ptr [rbp - 0x34], 0x3fffffff
+mov dword ptr [rbp - 0x48], 0
+ja L
+mov rsi, qword ptr [rbp - 0x40]
+test rsi, rsi
+je L
+mov rax, qword ptr [D]
+mov rdi, qword ptr [rax]
+mov rax, qword ptr [rdi]
+call qword ptr [rax + 0x20]
 mov rdi, qword ptr [rbp - 0x168]
 call F
```

### изменена: 0x49da900 (32909 байт) | строки: "scripts/height_levels.txt"; "modifier_jakiro_dual_breath"; "modifier_jakiro_dual_breath_slow"; "modifier_jakiro_dual_breath_burn"; "modifier_jakiro_ice_path_stun"; "modifier_jakiro_ice_path"; "modifier_jakiro_liquidice"; "modifier_jakiro_liquid_ice_debuff"
было: 0x49dbb80 (32950 байт)
- строки: −"modifier_lycan_wolf_bite_attack_range"
- прямых вызовов: 1012 → 1010
- инструкций: 6062 → 6054
```diff
@@ -400,5 +400,4 @@
 lea rdi, [T]
 call F
-lea r15, [D]
 call F
 lea r13, [D]
@@ -2415,12 +2414,4 @@
 mov qword ptr [D], rax
 call F
-lea rdx, [S:"modifier_lycan_wolf_bite_attack_range"]
-lea rsi, [D]
-mov rdi, rax
-mov rax, qword ptr [rax]
-call qword ptr [rax]
-lea rax, [D]
-mov qword ptr [D], rax
-call F
 lea rdx, [S:"modifier_lone_wolf_self"]
 lea rsi, [D]
@@ -2898,13 +2889,13 @@
 mov rax, qword ptr [r13]
 lea rdi, [D]
+mov qword ptr [rbp - 0x40], 0
+mov qword ptr [D], rax
+lea rax, [D]
+mov qword ptr [r13], rax
+lea rax, [T]
+mov qword ptr [D], rax
+lea rax, [T]
+mov qword ptr [rbp - 0x50], rax
 lea r13, [D]
-mov qword ptr [rbp - 0x40], 0
-mov qword ptr [D], rax
-lea rax, [D]
-mov qword ptr [r13], rax
-lea rax, [T]
-mov qword ptr [D], rax
-lea rax, [T]
-mov qword ptr [rbp - 0x50], rax
 call F
 lea rax, [T]
@@ -2987,10 +2978,10 @@
 mov rax, qword ptr [rax]
 call qword ptr [rax]
+mov rdi, r13
 mov edx, 9
-mov rdi, r15
 lea rsi, [S:"dota_roshan_initial_move_timer"]
 call F
+mov rsi, r13
 mov rdx, r14
-mov rsi, r15
 lea rdi, [T]
 call F
@@ -3004,10 +2995,11 @@
 call qword ptr [rax]
 call F
-mov rsi, rbx
-mov qword ptr [rbp - 0x48], r12
-mov qword ptr [D], rax
-mov rax, qword ptr [r13]
-lea rdi, [D]
-mov qword ptr [rbp - 0x40], 0
+lea r13, [D]
+mov rsi, rbx
+mov qword ptr [rbp - 0x48], r12
+mov qword ptr [D], rax
+lea rdi, [D]
+mov qword ptr [rbp - 0x40], 0
+mov rax, qword ptr [r13]
 mov qword ptr [D], rax
 lea rax, [D]
```

### изменена: 0x49f15f0 (444 байт) | строки: "CDOTA_NPC_Rattletrap_Cog"
было: 0x49f2890 (444 байт)
- числа в инструкциях: +0x3141593e −0x15bc763b
- прямых вызовов: 10 → 11
- инструкций: 97 → 100
```diff
@@ -56,8 +56,12 @@
 test eax, eax
 je L
-lea rdi, [D]
-mov esi, 0x15bc763b
+lea r14, [S:"CDOTA_NPC_Rattletrap_Cog"]
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
-lea rdx, [S:"CDOTA_NPC_Rattletrap_Cog"]
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

### изменена: 0x4ebf970 (67 байт) CDOTA_Modifier_Smoke_Of_Deceit::CheckState
было: 0x4ec0bf0 (67 байт)
- числа в инструкциях: +0x1000000000 +0xffffffefffffffff −0x81000000000 −0xfffff7efffffffff
- инструкций: 17 → 17
```diff
@@ -5,7 +5,7 @@
 sub rsp, 8
 call F
-movabs rax, 0x81000000000
+movabs rax, 0x1000000000
 or rax, qword ptr [rbx]
-movabs rdx, 0xfffff7efffffffff
+movabs rdx, 0xffffffefffffffff
 and rdx, qword ptr [rbx + 8]
 movq xmm0, rax
```

### изменена: 0x56b2ad0 (336 байт)
было: 0x56b3d70 (439 байт)
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

### изменена: 0x5bf5340 (723 байт) | строки: "CVDataLocalizedToken"; "EMonsterHunterCodexAuthor"
было: 0x5c014f0 (659 байт)
- числа в инструкциях: +0 +0
- поля объектов: +0x48 +0x40
- прямых вызовов: 16 → 21
- инструкций: 164 → 183
```diff
@@ -103,16 +103,29 @@
 test rsi, rsi
 je L
-mov rdi, rsi
+cmp qword ptr [rsi + 0x48], 0
+je L
+lea rdi, [rsi + 0x48]
+call F
+cmp qword ptr [rbx + 0x40], 0
+je L
+lea rdi, [rbx + 0x40]
+call F
+lea rdi, [rbx + 0x30]
+xor esi, esi
+call F
+lea rdi, [rbx + 0x20]
+xor esi, esi
+call F
+lea rdi, [rbx + 0x10]
+xor esi, esi
+call F
+xor esi, esi
+mov rdi, rbx
 call F
 mov esi, 0x78
 mov rdi, rbx
 call F
-pop rbx
-mov eax, 1
-pop r12
-pop r13
-pop r14
-pop rbp
-ret
+jmp L
+nop
 movabs rax, 0xc000000800000000
 pxor xmm0, xmm0
@@ -156,9 +169,15 @@
 mov rdi, rbx
 call F
-jmp L
-nop dword ptr [rax + rax]
+pop rbx
+mov eax, 1
+pop r12
+pop r13
+pop r14
+pop rbp
+ret
+nop dword ptr [rax]
 xor eax, eax
 jmp L
-nop word ptr [rax + rax]
+nop
 xor eax, eax
 ret
```

### изменена: 0x5c1b840 (2515 байт) CDOTA_Neutral_Creep_BehaviorController::vfunc#3 | строки: "modifier_roshan_moving"
было: 0x5c1cac0 (2354 байт)
- константы из данных (числа логики): +3
- числа в инструкциях: +0
- поля объектов: +0x194f +0x24 +0x24 −0x11cc
- прямых вызовов: 57 → 62
- инструкций: 519 → 561
```diff
@@ -4,7 +4,7 @@
 push r15
 push r14
+mov r14, rdi
 push r13
 push r12
-mov r12, rdi
 push rbx
 sub rsp, 0x48
@@ -14,10 +14,10 @@
 cmp rax, rdx
 jne L
-mov r13, qword ptr [rbx + 0x1788]
+mov r15, qword ptr [rbx + 0x1788]
 test byte ptr [rbx + 0x124b], 0x80
 jne L
 cmp qword ptr [rbx + 0x1308], 0
 je L
-mov byte ptr [r12 + 0x35], 0
+mov byte ptr [r14 + 0x35], 0
 cmp byte ptr [rbx + 0x194d], 0
 jne L
@@ -32,5 +32,5 @@
 pop rbp
 ret
-nop word ptr [rax + rax]
+nop word ptr cs:[rax + rax]
 cmp byte ptr [rbx + 0x174c], 0
 jne L
@@ -39,30 +39,30 @@
 test rax, rax
 jne L
-cmp byte ptr [r12 + 0x34], 0
+cmp byte ptr [r14 + 0x34], 0
 je L
 mov rax, qword ptr [rbx]
-lea r14, [T]
+lea r12, [T]
 mov rax, qword ptr [rax + 0xbf0]
-cmp rax, r14
+cmp rax, r12
 jne L
 test byte ptr [rbx + 0xd3e], 8
 je L
 movss xmm0, dword ptr [rbx + 0x17a4]
-ucomiss xmm0, dword ptr [r12 + 0x38]
+ucomiss xmm0, dword ptr [r14 + 0x38]
 jp L
 jne L
-movss xmm0, dword ptr [rbx + 0x17a8]
-ucomiss xmm0, dword ptr [r12 + 0x3c]
+movss xmm0, dword ptr [r14 + 0x3c]
+ucomiss xmm0, dword ptr [rbx + 0x17a8]
 jp L
 je L
-nop dword ptr [rax]
-mov byte ptr [r12 + 0x34], 1
+nop
+mov byte ptr [r14 + 0x34], 1
+mov rax, qword ptr [rbx + 0x17a4]
 pxor xmm0, xmm0
 mov edx, 0
 movss xmm1, dword ptr [rbx + 0x17a8]
-mov rax, qword ptr [rbx + 0x17a4]
+movss xmm2, dword ptr [rbx + 0x17a4]
 ucomiss xmm1, xmm0
-movss xmm2, dword ptr [rbx + 0x17a4]
-mov qword ptr [r12 + 0x38], rax
+mov qword ptr [r14 + 0x38], rax
 setnp al
 cmovne eax, edx
@@ -77,22 +77,22 @@
 call F
 mov rax, qword ptr [rax]
-mov qword ptr [r12 + 0x38], rax
+mov qword ptr [r14 + 0x38], rax
```
(ещё 559 строк диффа: so-query.py fdiff libserver.so 0x5c1b840)

### изменена: 0x5c78a20 (7160 байт) | строки: "m_vecMaterials"; "m_vecEconItems"; "m_vecCraftableRewards"; "m_vecHeroes"; "m_vecTradeRecipes"; "m_mapCodexEntriesLocalized"; "m_strTokenLocStringPrefix"; "m_vecSmallRewards"
было: 0x5c79c20 (7256 байт)
- строки: −"m_vecMaterials"
- числа в инструкциях: +0 +0xffffffff +0x9ce441ba −2 −0xf −1 −9 −0xffffffff9ce441ba
- поля объектов: −0x140 −0x128
- прямых вызовов: 170 → 168
- цели вызовов: −0x6512ae0 "<unknown>"
- инструкций: 1523 → 1502
```diff
@@ -16,31 +16,21 @@
 test rax, rax
 jne L
-mov rax, qword ptr [r14 + 0x128]
-movzx edi, word ptr [rax]
-shr di, 2
-and edi, 0xf
-cmp dil, 1
-je L
-cmp dil, 9
-jne L
-lea r12, [rbp - 0xb0]
-xor ecx, ecx
-mov rdi, rax
-mov qword ptr [rbp - 0xb0], 0xffffffff9ce441ba
-lea r13, [S:"m_vecMaterials"]
-mov rsi, r12
-lea rdx, [rbp - 0xbc]
-mov qword ptr [rbp - 0xa8], r13
+lea r12, [S:"m_vecMaterials"]
+mov edx, 0xffffffff
+mov esi, 0x9ce441ba
+lea r8, [rbp - 0xbc]
+mov rcx, r12
+mov rdi, r14
 call F
 test rax, rax
 mov rbx, rax
 je L
-mov rsi, r12
-mov rdi, r14
+lea rsi, [rbp - 0xb0]
+mov rdi, r14
+mov qword ptr [rbp - 0xa8], r12
 mov r12, rbx
 mov qword ptr [rbp - 0xb0], 0xffffffff9ce441ba
-mov qword ptr [rbp - 0xa8], r13
-call F
-movzx eax, word ptr [rbx]
+call F
+movzx eax, word ptr [r12]
 xor edx, edx
 xor r15d, r15d
@@ -100,5 +90,5 @@
 test r15d, r15d
 jg L
-test r12, r12
+test rbx, rbx
 je L
 mov rdi, r14
@@ -670,18 +660,7 @@
 test al, al
 jne L
-mov rax, qword ptr [r14 + 0x140]
-test rax, rax
-je L
 jmp L
 nop word ptr [rax + rax]
-movzx edi, dil
-call F
-lea rsi, [D]
-mov rdi, r14
-mov rdx, rax
-xor eax, eax
-call F
-mov r12, qword ptr [r14 + 0x140]
-test r12, r12
+cmp qword ptr [r14 + 0x140], 0
 je L
 xor esi, esi
@@ -748,5 +727,5 @@
 mov rax, qword ptr [rbp - 0xc8]
 mov rdi, r15
-mov r13, qword ptr [rax + 0x38]
+mov r13, qword ptr [rax + 0xd8]
 call F
```
(ещё 463 строк диффа: so-query.py fdiff libserver.so 0x5c78a20)

### изменена: 0x6bfa580 (356 байт) | строки: "msgprotobuf.cpp"
было: 0x6bfb7c0 (218 байт)
- строки: +"msgprotobuf.cpp"
- числа в инструкциях: +2 +0x30
- поля объектов: +0x78 +0x40
- прямых вызовов: 3 → 7
- цели вызовов: +0x652f660 "[M:%u:%u:%u]"; "[C:%u:%u]" +0x6bf9530 "messagelist.cpp"; "GetMessage" +0x6bf8180
- инструкций: 69 → 105
```diff
@@ -7,23 +7,24 @@
 mov r14, rdi
 push r13
-mov r13d, r9d
+mov r13d, edx
+xor edx, edx
 push r12
-mov r12, rcx
+mov r12d, r9d
 push rbx
 mov rbx, rsi
 xor esi, esi
-sub rsp, 0x18
+sub rsp, 0x28
 mov qword ptr [rdi], rax
-mov dword ptr [rbp - 0x34], edx
-xor edx, edx
 mov dword ptr [rdi + 8], 1
 mov rdi, r15
-mov dword ptr [rbp - 0x38], r8d
+mov qword ptr [rbp - 0x48], rcx
+mov dword ptr [rbp - 0x4c], r8d
 call F
-mov qword ptr [r14 + 0x70], r12
+mov rax, qword ptr [rbp - 0x48]
+mov dword ptr [r14 + 0x78], r12d
 mov rdi, rbx
-mov dword ptr [r14 + 0x78], r13d
 mov byte ptr [r14 + 0x7c], 0
 mov qword ptr [r14 + 0x10], rbx
+mov qword ptr [r14 + 0x70], rax
 call F
 mov rax, qword ptr [r14 + 0x10]
@@ -35,5 +36,32 @@
 cmp rcx, rax
 jae L
-add rsp, 0x18
+lea rsp, [rbp - 0x28]
+pop rbx
+pop r12
+pop r13
+pop r14
+pop r15
+pop rbp
+ret
+nop dword ptr [rax]
+mov rsi, qword ptr [rbx + 8]
+mov rdi, r15
+add rsi, 8
+call F
+test al, al
+je L
+cmp r13d, 2
+mov r15d, dword ptr [r14 + 0x50]
+je L
+test r15d, r15d
+jne L
+mov rax, qword ptr [rbp - 0x48]
+or dword ptr [r14 + 0x28], 0x224
+mov qword ptr [r14 + 0x40], rax
+mov eax, dword ptr [rbp - 0x4c]
+mov dword ptr [r14 + 0x50], r13d
+mov dword ptr [r14 + 0x6c], eax
+mov byte ptr [r14 + 0x7c], 1
+lea rsp, [rbp - 0x28]
 pop rbx
 pop r12
@@ -44,26 +72,34 @@
 ret
 nop word ptr [rax + rax]
-mov rsi, qword ptr [rbx + 8]
-mov rdi, r15
-add rsi, 8
+test r15d, r15d
+mov rax, qword ptr [rbp - 0x48]
+je L
```
(ещё 49 строк диффа: so-query.py fdiff libserver.so 0x6bfa580)

### изменена: 0x6bfa990 (280 байт) вызывается из: CGCTournamentItemEventResponse::vfunc#12, CInlineJob_CMsgGCToServerCheerData::vfunc#12, CInlineJob_CMsgGCToServerCheerScalesOverride::vfunc#12 | строки: "msgprotobuf.cpp"; "CProtoBufMsg::InitFromPacket( IMsgNetPacket )"; "InitFromPacketSafe"
было: 0x6bfbb40 (280 байт)
- числа в инструкциях: +0xc1 −0xb9
- инструкций: 79 → 79
```diff
@@ -13,5 +13,5 @@
 mov qword ptr [rbp - 0x40], rax
 lea rax, [S:"InitFromPacketSafe"]
-mov dword ptr [rbp - 0x38], 0xb9
+mov dword ptr [rbp - 0x38], 0xc1
 mov qword ptr [rbp - 0x30], rax
 call F
```

### изменена: 0x6bfaab0 (269 байт) | строки: "msgprotobuf.cpp"; "CProtoBufMsg::BAsyncSendProto"; "BAsyncSendProto"
было: 0x6bfbc60 (269 байт)
- числа в инструкциях: +0xf6 −0xee
- инструкций: 77 → 77
```diff
@@ -19,5 +19,5 @@
 lea rdi, [S:"CProtoBufMsg::BAsyncSendProto"]
 lea rax, [S:"BAsyncSendProto"]
-mov dword ptr [rbp - 0x48], 0xee
+mov dword ptr [rbp - 0x48], 0xf6
 mov qword ptr [rbp - 0x40], rax
 call F
```

### изменена: 0x4944600 (238 байт)
- код тот же, но вызывает другую функцию: было 0x490dff0, стало 0x490cfa0

### изменена: 0x4944b60 (266 байт) | строки: "VectorWS"
- код тот же, но вызывает другую функцию: было 0x4910100, стало 0x490f0b0

### изменена: 0x4944f70 (111 байт) | строки: "GameTick_t"
- код тот же, но вызывает другую функцию: было 0x490fd70, стало 0x490ed20

### изменена: 0x4945750 (143 байт)
- код тот же, но вызывает другую функцию: было 0x490e600, стало 0x490d5b0

### изменена: 0x4945bc0 (210 байт) | строки: "GameTime_t"; "CUtlVector"
- код тот же, но вызывает другую функцию: было 0x490eb70, стало 0x490db20

### изменена: 0x4945ca0 (210 байт) | строки: "AttackRecord_t"; "CUtlVector"
- код тот же, но вызывает другую функцию: было 0x490e410, стало 0x490d3c0

### изменена: 0x4945f60 (419 байт)
- код тот же, но вызывает другую функцию: было 0x490d730, стало 0x490c6e0

### изменена: 0x49469c0 (435 байт) | строки: "VectorWS"
- код тот же, но вызывает другую функцию: было 0x490f780, стало 0x490e730

### изменена: 0x4947440 (270 байт)
- код тот же, но вызывает другую функцию: было 0x490e750, стало 0x490d700

### изменена: 0x4948260 (403 байт) | строки: "PlayerID_t"
- код тот же, но вызывает другую функцию: было 0x490f470, стало 0x490e420

### изменена: 0x4948f60 (515 байт) | строки: "GameTime_t"; "VectorWS"
- код тот же, но вызывает другую функцию: было 0x490f560, стало 0x490e510

### изменена: 0x49494b0 (723 байт) | строки: "VectorWS"; "CDOTA_Tree"; "CUtlVector"
- код тот же, но вызывает другую функцию: было 0x490f8b0, стало 0x490e860

### изменена: 0x4951270 (314 байт) | строки: "AttackRecord_t"; "CUtlVector"; "CDOTA_Buff"
- код тот же, но вызывает другую функцию: было 0x490f150, стало 0x490e100

### изменена: 0x493a2c0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x49101b0, стало 0x490f160

### изменена: 0x493a390 (206 байт)
- код тот же, но вызывает другую функцию: было 0x4910140, стало 0x490f0f0

### изменена: 0x493a460 (206 байт)
- код тот же, но вызывает другую функцию: было 0x4910130, стало 0x490f0e0

### изменена: 0x493a530 (206 байт)
- код тот же, но вызывает другую функцию: было 0x4910080, стало 0x490f030

### изменена: 0x493a600 (206 байт)
- код тот же, но вызывает другую функцию: было 0x490ffb0, стало 0x490ef60

### изменена: 0x493a6d0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x490fe80, стало 0x490ee30

### изменена: 0x493a7a0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x490fe10, стало 0x490edc0

### изменена: 0x493a870 (206 байт)
- код тот же, но вызывает другую функцию: было 0x490fda0, стало 0x490ed50

### изменена: 0x493a940 (206 байт)
- код тот же, но вызывает другую функцию: было 0x490fd30, стало 0x490ece0

### изменена: 0x493aa10 (206 байт)
- код тот же, но вызывает другую функцию: было 0x490fcc0, стало 0x490ec70

### изменена: 0x493aae0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x490fc50, стало 0x490ec00

### изменена: 0x493abb0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x490fc10, стало 0x490ebc0

### изменена: 0x493ac80 (206 байт)
- код тот же, но вызывает другую функцию: было 0x490f930, стало 0x490e8e0

### изменена: 0x493ad50 (206 байт)
- код тот же, но вызывает другую функцию: было 0x490f870, стало 0x490e820

### изменена: 0x493ae20 (206 байт)
- код тот же, но вызывает другую функцию: было 0x490f710, стало 0x490e6c0

### изменена: 0x493aef0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x490f700, стало 0x490e6b0

### изменена: 0x493afc0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x490f660, стало 0x490e610

### изменена: 0x493b090 (206 байт)
- код тот же, но вызывает другую функцию: было 0x490f4f0, стало 0x490e4a0

### изменена: 0x493b160 (206 байт)
- код тот же, но вызывает другую функцию: было 0x490f430, стало 0x490e3e0

### изменена: 0x493b230 (206 байт)
- код тот же, но вызывает другую функцию: было 0x490f390, стало 0x490e340

### изменена: 0x493b300 (206 байт)
- код тот же, но вызывает другую функцию: было 0x490f320, стало 0x490e2d0

### изменена: 0x493b3d0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x490f2e0, стало 0x490e290

### изменена: 0x493b4a0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x490f270, стало 0x490e220

### изменена: 0x493b570 (206 байт)
- код тот же, но вызывает другую функцию: было 0x490f140, стало 0x490e0f0

### изменена: 0x493b640 (206 байт)
- код тот же, но вызывает другую функцию: было 0x490f100, стало 0x490e0b0

### изменена: 0x493b710 (206 байт)
- код тот же, но вызывает другую функцию: было 0x490f010, стало 0x490dfc0

### изменена: 0x493b7e0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x490efa0, стало 0x490df50

### изменена: 0x493b8b0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x490ef30, стало 0x490dee0

### изменена: 0x493b980 (206 байт)
- код тот же, но вызывает другую функцию: было 0x490eef0, стало 0x490dea0

### изменена: 0x493ba50 (206 байт)
- код тот же, но вызывает другую функцию: было 0x490eee0, стало 0x490de90

### изменена: 0x493bb20 (206 байт)
- код тот же, но вызывает другую функцию: было 0x490ee60, стало 0x490de10

### изменена: 0x493bbf0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x490edc0, стало 0x490dd70

### изменена: 0x493bcc0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x490ec60, стало 0x490dc10

### изменена: 0x493bd90 (206 байт)
- код тот же, но вызывает другую функцию: было 0x490ec50, стало 0x490dc00

### изменена: 0x493be60 (206 байт)
- код тот же, но вызывает другую функцию: было 0x490eba0, стало 0x490db50

### изменена: 0x493bf30 (206 байт)
- код тот же, но вызывает другую функцию: было 0x490eb60, стало 0x490db10

### изменена: 0x493c000 (206 байт)
- код тот же, но вызывает другую функцию: было 0x490e8d0, стало 0x490d880

### изменена: 0x493c0d0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x490e860, стало 0x490d810

### изменена: 0x493c1a0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x490e7f0, стало 0x490d7a0

### изменена: 0x493c270 (206 байт)
- код тот же, но вызывает другую функцию: было 0x490e710, стало 0x490d6c0

### изменена: 0x493c340 (206 байт)
- код тот же, но вызывает другую функцию: было 0x490e670, стало 0x490d620

### изменена: 0x493c410 (206 байт)
- код тот же, но вызывает другую функцию: было 0x490e630, стало 0x490d5e0

### изменена: 0x493c4e0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x490e5f0, стало 0x490d5a0

### изменена: 0x493c5b0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x490e5e0, стало 0x490d590

### изменена: 0x493c680 (206 байт)
- код тот же, но вызывает другую функцию: было 0x490e570, стало 0x490d520

### изменена: 0x493c750 (206 байт)
- код тот же, но вызывает другую функцию: было 0x490e530, стало 0x490d4e0

### изменена: 0x493c820 (206 байт)
- код тот же, но вызывает другую функцию: было 0x490e4f0, стало 0x490d4a0

### изменена: 0x493c8f0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x490e4b0, стало 0x490d460

### изменена: 0x493c9c0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x490e470, стало 0x490d420

### изменена: 0x493ca90 (206 байт)
- код тот же, но вызывает другую функцию: было 0x490e400, стало 0x490d3b0

### изменена: 0x493cb60 (206 байт)
- код тот же, но вызывает другую функцию: было 0x490e340, стало 0x490d2f0

### изменена: 0x493cc30 (206 байт)
- код тот же, но вызывает другую функцию: было 0x490e300, стало 0x490d2b0

### изменена: 0x493cd00 (206 байт)
- код тот же, но вызывает другую функцию: было 0x490e170, стало 0x490d120

### изменена: 0x493cdd0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x490e0a0, стало 0x490d050

### изменена: 0x493cea0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x490e030, стало 0x490cfe0

### изменена: 0x493cf70 (206 байт)
- код тот же, но вызывает другую функцию: было 0x490dfb0, стало 0x490cf60

### изменена: 0x493d040 (206 байт)
- код тот же, но вызывает другую функцию: было 0x490df20, стало 0x490ced0

### изменена: 0x493d110 (206 байт)
- код тот же, но вызывает другую функцию: было 0x490df10, стало 0x490cec0

### изменена: 0x493d1e0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x490de90, стало 0x490ce40

### изменена: 0x493d2b0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x490de50, стало 0x490ce00

### изменена: 0x493d380 (206 байт)
- код тот же, но вызывает другую функцию: было 0x490dde0, стало 0x490cd90

### изменена: 0x493d450 (206 байт)
- код тот же, но вызывает другую функцию: было 0x490dd10, стало 0x490ccc0

### изменена: 0x493d520 (206 байт)
- код тот же, но вызывает другую функцию: было 0x490dc50, стало 0x490cc00

### изменена: 0x493d5f0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x490dc10, стало 0x490cbc0

### изменена: 0x493d6c0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x490dbd0, стало 0x490cb80

### изменена: 0x493d790 (206 байт)
- код тот же, но вызывает другую функцию: было 0x490db60, стало 0x490cb10

### изменена: 0x493d860 (206 байт)
- код тот же, но вызывает другую функцию: было 0x490da60, стало 0x490ca10

### изменена: 0x493d930 (206 байт)
- код тот же, но вызывает другую функцию: было 0x490d9f0, стало 0x490c9a0

### изменена: 0x493da00 (206 байт)
- код тот же, но вызывает другую функцию: было 0x490d950, стало 0x490c900

### изменена: 0x493dad0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x490d910, стало 0x490c8c0

### изменена: 0x493dba0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x490d8a0, стало 0x490c850

### изменена: 0x493dc70 (206 байт)
- код тот же, но вызывает другую функцию: было 0x490d830, стало 0x490c7e0

### изменена: 0x4940a00 (63 байт)
- код тот же, но вызывает другую функцию: было 0x49101c0, стало 0x490f170

### изменена: 0x4940a40 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4910180, стало 0x490f130

### изменена: 0x4940a80 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4910150, стало 0x490f100

### изменена: 0x4940ac0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x49100c0, стало 0x490f070

### изменена: 0x4940b00 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4910090, стало 0x490f040

### изменена: 0x4940b40 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4910050, стало 0x490f000

### изменена: 0x4940b80 (63 байт)
- код тот же, но вызывает другую функцию: было 0x4910020, стало 0x490efd0

### изменена: 0x4940bc0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x490fff0, стало 0x490efa0

### изменена: 0x4940c00 (63 байт)
- код тот же, но вызывает другую функцию: было 0x490ffc0, стало 0x490ef70

### изменена: 0x4940c40 (63 байт)
- код тот же, но вызывает другую функцию: было 0x490ff80, стало 0x490ef30

### изменена: 0x4940c80 (63 байт)
- код тот же, но вызывает другую функцию: было 0x490fec0, стало 0x490ee70

### изменена: 0x4940cc0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x490fe90, стало 0x490ee40

### изменена: 0x4940d00 (63 байт)
- код тот же, но вызывает другую функцию: было 0x490fe50, стало 0x490ee00

### изменена: 0x4940d40 (63 байт)
- код тот же, но вызывает другую функцию: было 0x490fe20, стало 0x490edd0

### изменена: 0x4940d80 (63 байт)
- код тот же, но вызывает другую функцию: было 0x490fde0, стало 0x490ed90

### изменена: 0x4940dc0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x490fdb0, стало 0x490ed60

### изменена: 0x4940e00 (63 байт)
- код тот же, но вызывает другую функцию: было 0x490fd40, стало 0x490ecf0

### изменена: 0x4940e40 (63 байт)
- код тот же, но вызывает другую функцию: было 0x490fcd0, стало 0x490ec80

### изменена: 0x4940e80 (63 байт)
- код тот же, но вызывает другую функцию: было 0x490fc90, стало 0x490ec40

### изменена: 0x4940ec0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x490fc60, стало 0x490ec10

### изменена: 0x4940f00 (63 байт)
- код тот же, но вызывает другую функцию: было 0x490fc20, стало 0x490ebd0

### изменена: 0x4940f40 (63 байт)
- код тот же, но вызывает другую функцию: было 0x490fbe0, стало 0x490eb90

### изменена: 0x4940f80 (63 байт)
- код тот же, но вызывает другую функцию: было 0x490fbb0, стало 0x490eb60

### изменена: 0x4940fc0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x490fb80, стало 0x490eb30

### изменена: 0x4941000 (63 байт)
- код тот же, но вызывает другую функцию: было 0x490fb50, стало 0x490eb00

### изменена: 0x4941040 (63 байт)
- код тот же, но вызывает другую функцию: было 0x490fb20, стало 0x490ead0

### изменена: 0x4941080 (63 байт)
- код тот же, но вызывает другую функцию: было 0x490faf0, стало 0x490eaa0

### изменена: 0x49410c0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x490fac0, стало 0x490ea70

### изменена: 0x4941100 (63 байт)
- код тот же, но вызывает другую функцию: было 0x490fa90, стало 0x490ea40

### изменена: 0x4941140 (63 байт)
- код тот же, но вызывает другую функцию: было 0x490fa60, стало 0x490ea10

### изменена: 0x4941180 (63 байт)
- код тот же, но вызывает другую функцию: было 0x490fa30, стало 0x490e9e0

### изменена: 0x49411c0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x490fa00, стало 0x490e9b0

### изменена: 0x4941200 (63 байт)
- код тот же, но вызывает другую функцию: было 0x490f9d0, стало 0x490e980

### изменена: 0x4941240 (63 байт)
- код тот же, но вызывает другую функцию: было 0x490f9a0, стало 0x490e950

### изменена: 0x4941280 (63 байт)
- код тот же, но вызывает другую функцию: было 0x490f970, стало 0x490e920

### изменена: 0x49412c0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x490f940, стало 0x490e8f0

### изменена: 0x4941300 (63 байт)
- код тот же, но вызывает другую функцию: было 0x490f840, стало 0x490e7f0

### изменена: 0x4941340 (63 байт)
- код тот же, но вызывает другую функцию: было 0x490f810, стало 0x490e7c0

### изменена: 0x4941380 (63 байт)
- код тот же, но вызывает другую функцию: было 0x490f7b0, стало 0x490e760

### изменена: 0x49413c0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x490f720, стало 0x490e6d0

### изменена: 0x4941400 (63 байт)
- код тот же, но вызывает другую функцию: было 0x490f6d0, стало 0x490e680

### изменена: 0x4941440 (63 байт)
- код тот же, но вызывает другую функцию: было 0x490f6a0, стало 0x490e650

### изменена: 0x4941480 (63 байт)
- код тот же, но вызывает другую функцию: было 0x490f630, стало 0x490e5e0

### изменена: 0x49414c0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x490f600, стало 0x490e5b0

### изменена: 0x4941500 (63 байт)
- код тот же, но вызывает другую функцию: было 0x490f5d0, стало 0x490e580

### изменена: 0x4941540 (63 байт)
- код тот же, но вызывает другую функцию: было 0x490f5a0, стало 0x490e550

### изменена: 0x4941580 (63 байт)
- код тот же, но вызывает другую функцию: было 0x490f530, стало 0x490e4e0

### изменена: 0x49415c0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x490f500, стало 0x490e4b0

### изменена: 0x4941600 (63 байт)
- код тот же, но вызывает другую функцию: было 0x490f4c0, стало 0x490e470

### изменена: 0x4941640 (63 байт)
- код тот же, но вызывает другую функцию: было 0x490f440, стало 0x490e3f0

### изменена: 0x4941680 (63 байт)
- код тот же, но вызывает другую функцию: было 0x490f400, стало 0x490e3b0

### изменена: 0x49416c0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x490f3d0, стало 0x490e380

### изменена: 0x4941700 (63 байт)
- код тот же, но вызывает другую функцию: было 0x490f3a0, стало 0x490e350

### изменена: 0x4941740 (63 байт)
- код тот же, но вызывает другую функцию: было 0x490f360, стало 0x490e310

### изменена: 0x4941780 (63 байт)
- код тот же, но вызывает другую функцию: было 0x490f330, стало 0x490e2e0

### изменена: 0x49417c0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x490f2f0, стало 0x490e2a0

### изменена: 0x4941800 (63 байт)
- код тот же, но вызывает другую функцию: было 0x490f2b0, стало 0x490e260

### изменена: 0x4941840 (63 байт)
- код тот же, но вызывает другую функцию: было 0x490f280, стало 0x490e230

### изменена: 0x4941880 (63 байт)
- код тот же, но вызывает другую функцию: было 0x490f240, стало 0x490e1f0

### изменена: 0x49418c0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x490f210, стало 0x490e1c0

### изменена: 0x4941900 (63 байт)
- код тот же, но вызывает другую функцию: было 0x490f1e0, стало 0x490e190

### изменена: 0x4941940 (63 байт)
- код тот же, но вызывает другую функцию: было 0x490f1b0, стало 0x490e160

### изменена: 0x4941980 (63 байт)
- код тот же, но вызывает другую функцию: было 0x490f180, стало 0x490e130

### изменена: 0x49419c0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x490f110, стало 0x490e0c0

### изменена: 0x4941a00 (63 байт)
- код тот же, но вызывает другую функцию: было 0x490f0d0, стало 0x490e080

### изменена: 0x4941a40 (63 байт)
- код тот же, но вызывает другую функцию: было 0x490f050, стало 0x490e000

### изменена: 0x4941a80 (63 байт)
- код тот же, но вызывает другую функцию: было 0x490f020, стало 0x490dfd0

### изменена: 0x4941ac0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x490efe0, стало 0x490df90

### изменена: 0x4941b00 (63 байт)
- код тот же, но вызывает другую функцию: было 0x490efb0, стало 0x490df60

### изменена: 0x4941b40 (63 байт)
- код тот же, но вызывает другую функцию: было 0x490ef70, стало 0x490df20

### изменена: 0x4941b80 (63 байт)
- код тот же, но вызывает другую функцию: было 0x490eeb0, стало 0x490de60

### изменена: 0x4941bc0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x490ee80, стало 0x490de30

### изменена: 0x4941c00 (63 байт)
- код тот же, но вызывает другую функцию: было 0x490ee30, стало 0x490dde0

### изменена: 0x4941c40 (63 байт)
- код тот же, но вызывает другую функцию: было 0x490ee00, стало 0x490ddb0

### изменена: 0x4941c80 (63 байт)
- код тот же, но вызывает другую функцию: было 0x490edd0, стало 0x490dd80

### изменена: 0x4941cc0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x490ed90, стало 0x490dd40

### изменена: 0x4941d00 (63 байт)
- код тот же, но вызывает другую функцию: было 0x490ed60, стало 0x490dd10

### изменена: 0x4941d40 (63 байт)
- код тот же, но вызывает другую функцию: было 0x490ed20, стало 0x490dcd0

### изменена: 0x4941d80 (63 байт)
- код тот же, но вызывает другую функцию: было 0x490eca0, стало 0x490dc50

### изменена: 0x4941dc0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x490ec70, стало 0x490dc20

### изменена: 0x4941e00 (63 байт)
- код тот же, но вызывает другую функцию: было 0x490ec20, стало 0x490dbd0

### изменена: 0x4941e40 (63 байт)
- код тот же, но вызывает другую функцию: было 0x490ebb0, стало 0x490db60

### изменена: 0x4941e80 (63 байт)
- код тот же, но вызывает другую функцию: было 0x490eb00, стало 0x490dab0

### изменена: 0x4941ec0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x490ead0, стало 0x490da80

### изменена: 0x4941f00 (63 байт)
- код тот же, но вызывает другую функцию: было 0x490eaa0, стало 0x490da50

### изменена: 0x4941f40 (63 байт)
- код тот же, но вызывает другую функцию: было 0x490ea60, стало 0x490da10

### изменена: 0x4941f80 (63 байт)
- код тот же, но вызывает другую функцию: было 0x490e9d0, стало 0x490d980

### изменена: 0x4941fc0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x490e9a0, стало 0x490d950

### изменена: 0x4942000 (63 байт)
- код тот же, но вызывает другую функцию: было 0x490e970, стало 0x490d920

### изменена: 0x4942040 (63 байт)
- код тот же, но вызывает другую функцию: было 0x490e940, стало 0x490d8f0

### изменена: 0x4942080 (63 байт)
- код тот же, но вызывает другую функцию: было 0x490e910, стало 0x490d8c0

### изменена: 0x49420c0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x490e8e0, стало 0x490d890

### изменена: 0x4942100 (63 байт)
- код тот же, но вызывает другую функцию: было 0x490e8a0, стало 0x490d850

### изменена: 0x4942140 (63 байт)
- код тот же, но вызывает другую функцию: было 0x490e870, стало 0x490d820

### изменена: 0x4942180 (63 байт)
- код тот же, но вызывает другую функцию: было 0x490e830, стало 0x490d7e0

### изменена: 0x49421c0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x490e800, стало 0x490d7b0

### изменена: 0x4942200 (63 байт)
- код тот же, но вызывает другую функцию: было 0x490e720, стало 0x490d6d0

### изменена: 0x4942240 (63 байт)
- код тот же, но вызывает другую функцию: было 0x490e6e0, стало 0x490d690

### изменена: 0x4942280 (63 байт)
- код тот же, но вызывает другую функцию: было 0x490e6b0, стало 0x490d660

### изменена: 0x49422c0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x490e680, стало 0x490d630

### изменена: 0x4942300 (63 байт)
- код тот же, но вызывает другую функцию: было 0x490e640, стало 0x490d5f0

### изменена: 0x4942340 (63 байт)
- код тот же, но вызывает другую функцию: было 0x490e580, стало 0x490d530

### изменена: 0x4942380 (63 байт)
- код тот же, но вызывает другую функцию: было 0x490e540, стало 0x490d4f0

### изменена: 0x49423c0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x490e500, стало 0x490d4b0

### изменена: 0x4942400 (63 байт)
- код тот же, но вызывает другую функцию: было 0x490e4c0, стало 0x490d470

### изменена: 0x4942440 (63 байт)
- код тот же, но вызывает другую функцию: было 0x490e480, стало 0x490d430

### изменена: 0x4942480 (63 байт)
- код тот же, но вызывает другую функцию: было 0x490e440, стало 0x490d3f0

### изменена: 0x49424c0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x490e380, стало 0x490d330

### изменена: 0x4942500 (63 байт)
- код тот же, но вызывает другую функцию: было 0x490e350, стало 0x490d300

### изменена: 0x4942540 (63 байт)
- код тот же, но вызывает другую функцию: было 0x490e310, стало 0x490d2c0

### изменена: 0x4942580 (63 байт)
- код тот же, но вызывает другую функцию: было 0x490e2d0, стало 0x490d280

### изменена: 0x49425c0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x490e2a0, стало 0x490d250

### изменена: 0x4942600 (63 байт)
- код тот же, но вызывает другую функцию: было 0x490e270, стало 0x490d220

### изменена: 0x4942640 (63 байт)
- код тот же, но вызывает другую функцию: было 0x490e240, стало 0x490d1f0

### изменена: 0x4942680 (63 байт)
- код тот же, но вызывает другую функцию: было 0x490e210, стало 0x490d1c0

### изменена: 0x49426c0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x490e1e0, стало 0x490d190

### изменена: 0x4942700 (63 байт)
- код тот же, но вызывает другую функцию: было 0x490e1b0, стало 0x490d160

### изменена: 0x4942740 (63 байт)
- код тот же, но вызывает другую функцию: было 0x490e180, стало 0x490d130

### изменена: 0x4942780 (63 байт)
- код тот же, но вызывает другую функцию: было 0x490e140, стало 0x490d0f0

### изменена: 0x49427c0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x490e110, стало 0x490d0c0

### изменена: 0x4942800 (63 байт)
- код тот же, но вызывает другую функцию: было 0x490e0e0, стало 0x490d090

### изменена: 0x4942840 (63 байт)
- код тот же, но вызывает другую функцию: было 0x490e0b0, стало 0x490d060

### изменена: 0x4942880 (63 байт)
- код тот же, но вызывает другую функцию: было 0x490e070, стало 0x490d020

### изменена: 0x49428c0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x490e040, стало 0x490cff0

### изменена: 0x4942900 (63 байт)
- код тот же, но вызывает другую функцию: было 0x490e000, стало 0x490cfb0

### изменена: 0x4942940 (63 байт)
- код тот же, но вызывает другую функцию: было 0x490df30, стало 0x490cee0

### изменена: 0x4942980 (63 байт)
- код тот же, но вызывает другую функцию: было 0x490dee0, стало 0x490ce90

### изменена: 0x49429c0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x490dea0, стало 0x490ce50

### изменена: 0x4942a00 (63 байт)
- код тот же, но вызывает другую функцию: было 0x490de60, стало 0x490ce10

### изменена: 0x4942a40 (63 байт)
- код тот же, но вызывает другую функцию: было 0x490de20, стало 0x490cdd0

### изменена: 0x4942a80 (63 байт)
- код тот же, но вызывает другую функцию: было 0x490ddb0, стало 0x490cd60

### изменена: 0x4942ac0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x490dd80, стало 0x490cd30

### изменена: 0x4942b00 (63 байт)
- код тот же, но вызывает другую функцию: было 0x490dd50, стало 0x490cd00

### изменена: 0x4942b40 (63 байт)
- код тот же, но вызывает другую функцию: было 0x490dd20, стало 0x490ccd0

### изменена: 0x4942b80 (63 байт)
- код тот же, но вызывает другую функцию: было 0x490dc90, стало 0x490cc40

### изменена: 0x4942bc0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x490dc20, стало 0x490cbd0

### изменена: 0x4942c00 (63 байт)
- код тот же, но вызывает другую функцию: было 0x490dbe0, стало 0x490cb90

### изменена: 0x4942c40 (63 байт)
- код тот же, но вызывает другую функцию: было 0x490dba0, стало 0x490cb50

### изменена: 0x4942c80 (63 байт)
- код тот же, но вызывает другую функцию: было 0x490db70, стало 0x490cb20

### изменена: 0x4942cc0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x490db30, стало 0x490cae0

### изменена: 0x4942d00 (63 байт)
- код тот же, но вызывает другую функцию: было 0x490db00, стало 0x490cab0

### изменена: 0x4942d40 (63 байт)
- код тот же, но вызывает другую функцию: было 0x490dad0, стало 0x490ca80

### изменена: 0x4942d80 (63 байт)
- код тот же, но вызывает другую функцию: было 0x490daa0, стало 0x490ca50

### изменена: 0x4942dc0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x490da70, стало 0x490ca20

### изменена: 0x4942e00 (63 байт)
- код тот же, но вызывает другую функцию: было 0x490da30, стало 0x490c9e0

### изменена: 0x4942e40 (63 байт)
- код тот же, но вызывает другую функцию: было 0x490da00, стало 0x490c9b0

### изменена: 0x4942e80 (63 байт)
- код тот же, но вызывает другую функцию: было 0x490d9c0, стало 0x490c970

### изменена: 0x4942ec0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x490d990, стало 0x490c940

### изменена: 0x4942f00 (63 байт)
- код тот же, но вызывает другую функцию: было 0x490d960, стало 0x490c910

### изменена: 0x4942f40 (63 байт)
- код тот же, но вызывает другую функцию: было 0x490d920, стало 0x490c8d0

### изменена: 0x4942f80 (63 байт)
- код тот же, но вызывает другую функцию: было 0x490d8b0, стало 0x490c860

### изменена: 0x4942fc0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x490d870, стало 0x490c820

### изменена: 0x4943000 (63 байт)
- код тот же, но вызывает другую функцию: было 0x490d840, стало 0x490c7f0

### изменена: 0x4943040 (63 байт)
- код тот же, но вызывает другую функцию: было 0x490d800, стало 0x490c7b0

### изменена: 0x4943080 (63 байт)
- код тот же, но вызывает другую функцию: было 0x490d7d0, стало 0x490c780

### изменена: 0x49430c0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x490d7a0, стало 0x490c750

### изменена: 0x4943100 (63 байт)
- код тот же, но вызывает другую функцию: было 0x490d770, стало 0x490c720

### изменена: 0x4943140 (63 байт)
- код тот же, но вызывает другую функцию: было 0x490d740, стало 0x490c6f0

### изменена: 0x4943180 (63 байт)
- код тот же, но вызывает другую функцию: было 0x490d700, стало 0x490c610

### изменена: 0x49431c0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x490d630, стало 0x490c5e0

### изменена: 0x4943200 (63 байт)
- код тот же, но вызывает другую функцию: было 0x490d600, стало 0x490c560

### изменена: 0x4943240 (63 байт)
- код тот же, но вызывает другую функцию: было 0x490d580, стало 0x490c530

### изменена: 0x4943280 (63 байт)
- код тот же, но вызывает другую функцию: было 0x490d550, стало 0x490c4f0

### изменена: 0x49432c0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x490d510, стало 0x490c4c0

### изменена: 0x4943300 (63 байт)
- код тот же, но вызывает другую функцию: было 0x490d4e0, стало 0x490c430

### изменена: 0x4943340 (63 байт)
- код тот же, но вызывает другую функцию: было 0x490d450, стало 0x490c3f0

### изменена: 0x4943380 (63 байт)
- код тот же, но вызывает другую функцию: было 0x490d410, стало 0x490c350

### изменена: 0x49433c0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x490d370, стало 0x490c320

### изменена: 0x4943400 (63 байт)
- код тот же, но вызывает другую функцию: было 0x490d340, стало 0x490c2b0

### изменена: 0x4943440 (63 байт)
- код тот же, но вызывает другую функцию: было 0x490d2d0, стало 0x490c270

### изменена: 0x4943480 (63 байт)
- код тот же, но вызывает другую функцию: было 0x490d290, стало 0x490c230

### изменена: 0x49434c0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x490d250, стало 0x490c200

### изменена: 0x4943500 (63 байт)
- код тот же, но вызывает другую функцию: было 0x490d220, стало 0x490c1d0

### изменена: 0x4943540 (63 байт)
- код тот же, но вызывает другую функцию: было 0x490d1f0, стало 0x490c190

### изменена: 0x4943580 (63 байт)
- код тот же, но вызывает другую функцию: было 0x490d1b0, стало 0x490c160

### изменена: 0x49435c0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x490d180, стало 0x490c120

### изменена: 0x4943600 (63 байт)
- код тот же, но вызывает другую функцию: было 0x490d140, стало 0x490c0e0

### изменена: 0x4943640 (63 байт)
- код тот же, но вызывает другую функцию: было 0x490d100, стало 0x490c090

### изменена: 0x4943680 (63 байт)
- код тот же, но вызывает другую функцию: было 0x490d0b0, стало 0x490c060

### изменена: 0x49436c0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x490d080, стало 0x490c030

### изменена: 0x4943700 (63 байт)
- код тот же, но вызывает другую функцию: было 0x490d050, стало 0x490bff0

### изменена: 0x4943740 (63 байт)
- код тот же, но вызывает другую функцию: было 0x490d010, стало 0x490bfa0

### изменена: 0x4943780 (63 байт)
- код тот же, но вызывает другую функцию: было 0x490cfc0, стало 0x490bf70

### изменена: 0x49437c0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x490cf90, стало 0x490bf40

### изменена: 0x4943800 (63 байт)
- код тот же, но вызывает другую функцию: было 0x490cf60, стало 0x490bf10

### изменена: 0x4943840 (63 байт)
- код тот же, но вызывает другую функцию: было 0x490cf30, стало 0x490bec0

### изменена: 0x4943880 (63 байт)
- код тот же, но вызывает другую функцию: было 0x490cee0, стало 0x490be90

### изменена: 0x49438c0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x490ceb0, стало 0x490be50

### изменена: 0x4943900 (63 байт)
- код тот же, но вызывает другую функцию: было 0x490ce70, стало 0x490bdc0

### изменена: 0x4943940 (63 байт)
- код тот же, но вызывает другую функцию: было 0x490cde0, стало 0x490bd40

### изменена: 0x4943980 (63 байт)
- код тот же, но вызывает другую функцию: было 0x490cd60, стало 0x490bd00

### изменена: 0x49439c0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x490cd20, стало 0x490bcb0

### изменена: 0x4943a00 (63 байт)
- код тот же, но вызывает другую функцию: было 0x490ccd0, стало 0x490bc40

### изменена: 0x4943a40 (63 байт)
- код тот же, но вызывает другую функцию: было 0x490cc60, стало 0x490bbf0

### изменена: 0x4943a80 (63 байт)
- код тот же, но вызывает другую функцию: было 0x490cc10, стало 0x490bbc0

### изменена: 0x4943ac0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x490cbe0, стало 0x490bb90

### изменена: 0x4943b00 (63 байт)
- код тот же, но вызывает другую функцию: было 0x490cbb0, стало 0x490bb60

### изменена: 0x4943b40 (63 байт)
- код тот же, но вызывает другую функцию: было 0x490cb80, стало 0x490baf0

### изменена: 0x4943b80 (63 байт)
- код тот же, но вызывает другую функцию: было 0x490cb10, стало 0x490ba80

### изменена: 0x4943bc0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x490caa0, стало 0x490ba40

### изменена: 0x4943c00 (63 байт)
- код тот же, но вызывает другую функцию: было 0x490ca60, стало 0x490ba10

### изменена: 0x4943c40 (63 байт)
- код тот же, но вызывает другую функцию: было 0x490ca30, стало 0x490b9d0

### изменена: 0x4943c80 (63 байт)
- код тот же, но вызывает другую функцию: было 0x490c9f0, стало 0x490b940

### изменена: 0x4943cc0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x490c960, стало 0x490b900

### изменена: 0x4943d00 (63 байт)
- код тот же, но вызывает другую функцию: было 0x490c920, стало 0x490b8c0

### изменена: 0x4943d40 (63 байт)
- код тот же, но вызывает другую функцию: было 0x490c8e0, стало 0x490b880

### изменена: 0x4943d80 (63 байт)
- код тот же, но вызывает другую функцию: было 0x490c8a0, стало 0x490b850

### изменена: 0x4943dc0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x490c870, стало 0x490b820

### изменена: 0x4943e00 (63 байт)
- код тот же, но вызывает другую функцию: было 0x490c840, стало 0x490b7e0

### изменена: 0x4943e40 (63 байт)
- код тот же, но вызывает другую функцию: было 0x490c800, стало 0x490b780

### изменена: 0x4943e80 (63 байт)
- код тот же, но вызывает другую функцию: было 0x490c7a0, стало 0x490b740

### изменена: 0x4943ec0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x490c760, стало 0x490b700

### изменена: 0x4943f00 (63 байт)
- код тот же, но вызывает другую функцию: было 0x490c720, стало 0x490b670

### изменена: 0x4943f40 (63 байт)
- код тот же, но вызывает другую функцию: было 0x490c690, стало 0x490b630

### изменена: 0x4943f80 (63 байт)
- код тот же, но вызывает другую функцию: было 0x490c650, стало 0x490b600

### изменена: 0x4943fc0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x490c620, стало 0x490b5d0

### изменена: 0x4944000 (63 байт)
- код тот же, но вызывает другую функцию: было 0x490c5f0, стало 0x490b5a0

### изменена: 0x4944040 (63 байт)
- код тот же, но вызывает другую функцию: было 0x490c5c0, стало 0x490b560

### изменена: 0x4944080 (63 байт)
- код тот же, но вызывает другую функцию: было 0x490c580, стало 0x490b4f0

### изменена: 0x49440c0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x490c510, стало 0x490b440

### изменена: 0x4944100 (63 байт)
- код тот же, но вызывает другую функцию: было 0x490c460, стало 0x490b400

### изменена: 0x4944140 (63 байт)
- код тот же, но вызывает другую функцию: было 0x490c420, стало 0x490b3d0

### изменена: 0x4944180 (222 байт)
- код тот же, но вызывает другую функцию: было 0x490ed50, стало 0x490dd00

### изменена: 0x4944260 (222 байт)
- код тот же, но вызывает другую функцию: было 0x490ded0, стало 0x490ce80

### изменена: 0x4944500 (254 байт)
- код тот же, но вызывает другую функцию: было 0x49100f0, стало 0x490f0a0

### изменена: 0x4944c70 (119 байт) | строки: "VectorWS"
- код тот же, но вызывает другую функцию: было 0x490ff50, стало 0x490ef00

### изменена: 0x4944cf0 (119 байт) | строки: "VectorWS"
- код тот же, но вызывает другую функцию: было 0x490f570, стало 0x490e520

### изменена: 0x4944d70 (119 байт) | строки: "VectorWS"
- код тот же, но вызывает другую функцию: было 0x490d8e0, стало 0x490c890

### изменена: 0x4944fe0 (111 байт) | строки: "GameTime_t"
- код тот же, но вызывает другую функцию: было 0x490f880, стало 0x490e830

### изменена: 0x4945050 (111 байт) | строки: "GameTime_t"
- код тот же, но вызывает другую функцию: было 0x490f750, стало 0x490e700

### изменена: 0x49450c0 (111 байт) | строки: "GameTime_t"
- код тот же, но вызывает другую функцию: было 0x490f670, стало 0x490e620

### изменена: 0x4945130 (111 байт) | строки: "GameTime_t"
- код тот же, но вызывает другую функцию: было 0x490ef40, стало 0x490def0

### изменена: 0x49451a0 (111 байт) | строки: "GameTime_t"
- код тот же, но вызывает другую функцию: было 0x490ef00, стало 0x490deb0

### изменена: 0x4945210 (111 байт) | строки: "GameTime_t"
- код тот же, но вызывает другую функцию: было 0x490ea30, стало 0x490d9e0

### изменена: 0x4945280 (111 байт) | строки: "GameTime_t"
- код тот же, но вызывает другую функцию: было 0x490e5b0, стало 0x490d560

### изменена: 0x49452f0 (111 байт) | строки: "GameTime_t"
- код тот же, но вызывает другую функцию: было 0x490ddf0, стало 0x490cda0

### изменена: 0x4945440 (119 байт) | строки: "VectorWS"
- код тот же, но вызывает другую функцию: было 0x490f7e0, стало 0x490e790

### изменена: 0x49454c0 (119 байт) | строки: "VectorWS"
- код тот же, но вызывает другую функцию: было 0x490eb30, стало 0x490dae0

### изменена: 0x4945540 (119 байт) | строки: "VectorWS"
- код тот же, но вызывает другую функцию: было 0x490ea00, стало 0x490d9b0

### изменена: 0x49456c0 (143 байт) | строки: "GameTime_t"
- код тот же, но вызывает другую функцию: было 0x49101f0, стало 0x490f1a0

### изменена: 0x4945910 (270 байт)
- код тот же, но вызывает другую функцию: было 0x490ea90, стало 0x490da40

### изменена: 0x49462c0 (119 байт) | строки: "VectorWS"
- код тот же, но вызывает другую функцию: было 0x490ebf0, стало 0x490dba0

### изменена: 0x4946340 (119 байт) | строки: "VectorWS"
- код тот же, но вызывает другую функцию: было 0x490fd00, стало 0x490ecb0

### изменена: 0x49468a0 (286 байт)
- код тот же, но вызывает другую функцию: было 0x490ff40, стало 0x490eef0

### изменена: 0x4946c90 (334 байт)
- код тот же, но вызывает другую функцию: было 0x490ebe0, стало 0x490db90

### изменена: 0x4946ef0 (270 байт)
- код тот же, но вызывает другую функцию: было 0x490fef0, стало 0x490eea0

### изменена: 0x4947000 (270 байт)
- код тот же, но вызывает другую функцию: было 0x490f8e0, стало 0x490e890

### изменена: 0x4947110 (270 байт)
- код тот же, но вызывает другую функцию: было 0x490f080, стало 0x490e030

### изменена: 0x4947220 (270 байт)
- код тот же, но вызывает другую функцию: было 0x490ecd0, стало 0x490dc80

### изменена: 0x4947330 (270 байт)
- код тот же, но вызывает другую функцию: было 0x490e7a0, стало 0x490d750

### изменена: 0x4947550 (270 байт)
- код тот же, но вызывает другую функцию: было 0x490e3b0, стало 0x490d360

### изменена: 0x4947660 (270 байт)
- код тот же, но вызывает другую функцию: было 0x490dcc0, стало 0x490cc70

### изменена: 0x4947dd0 (286 байт)
- код тот же, но вызывает другую функцию: было 0x490df60, стало 0x490cf10

### изменена: 0x4949310 (414 байт)
- код тот же, но вызывает другую функцию: было 0x490ee70, стало 0x490de20

### изменена: 0x4950870 (175 байт) | строки: "AttackRecord_t"; "CUtlVector"
- код тот же, но вызывает другую функцию: было 0x490dc60, стало 0x490cc10

### изменена: 0x4950920 (175 байт) | строки: "AttackRecord_t"; "CUtlVector"
- код тот же, но вызывает другую функцию: было 0x490dfc0, стало 0x490cf70

### добавлена: 0x56b2c40 (103 байт) вызывается из: CSource1GameConfiguration::vfunc#22

### добавлена: 0x69f98f0 (3221 байт)

### удалена: 0x48b83f0 (96 байт) вызывается из: CDOTA_Modifier_Invoker_EMP::OnDestroy

### удалена: 0x4904760 (8 байт) CDOTA_Modifier_Lycan_Wolf_Bite_Attack_Range::vfunc#11 | строки: "CDOTA_Modifier_Lycan_Wolf_Bite_Attack_Range"

### удалена: 0x4904770 (8 байт) CDOTA_Modifier_Lycan_Wolf_Bite_Attack_Range::vfunc#10 | строки: "modifier_lycan_wolf_bite_attack_range"

### удалена: 0x4904780 (26 байт) CDOTA_Modifier_Lycan_Wolf_Bite_Attack_Range::vfunc#97

### удалена: 0x49a1e30 (65 байт) CDOTA_Modifier_Lycan_Wolf_Bite_Attack_Range::OnCreated | строки: "attack_range"

### удалена: 0x69fb300 (1237 байт)

### копии существующего кода (16): шаблонные / склеенные компоновщиком функции, такой же код есть и в другой сборке — не новый код
- ещё одна копия существующего кода: 0x485d490 (2880 байт)
- одной копией существующего кода меньше: 0x4858f20 (980 байт)
- одной копией существующего кода меньше: 0x48a72f0 (82 байт) вызывается из: CDOTA_Ability_Enchantress_Enchant::OnSpellStart
- одной копией существующего кода меньше: 0x49047a0 (35 байт) вызывается из: CDOTA_Modifier_Lycan_Wolf_Bite_Attack_Range::vfunc#97
- одной копией существующего кода меньше: 0x49047f0 (3 байт) CDOTA_Modifier_Lycan_Innate_Spirit_Wolves_Self::IsHidden
- одной копией существующего кода меньше: 0x4904800 (3 байт) CDOTA_Modifier_Lycan_Innate_Spirit_Wolves_Self::IsPurgable
- одной копией существующего кода меньше: 0x4904810 (8 байт) CDOTA_Modifier_Lycan_Innate_Spirit_Wolves_Self::vfunc#12
- одной копией существующего кода меньше: 0x4910220 (16 байт) CDOTA_Modifier_Weaver_Threads_Of_Fate_Linger::vfunc#0
- одной копией существующего кода меньше: 0x4910230 (18 байт)
- одной копией существующего кода меньше: 0x491d2f0 (33 байт) CModifierFactory<CDOTA_Modifier_Weaver_Threads_Of_Fate_Linger>::vfunc#1
- одной копией существующего кода меньше: 0x4923980 (83 байт) CModifierFactory<CDOTA_Modifier_Weaver_Threads_Of_Fate_Linger>::vfunc#2
- одной копией существующего кода меньше: 0x492ad30 (25 байт) CDOTA_Modifier_Jakiro_DualBreath_Thinker::vfunc#7
- одной копией существующего кода меньше: 0x492e810 (50 байт) CDOTA_Modifier_Jakiro_DualBreath_Thinker::vfunc#8
- одной копией существующего кода меньше: 0x49452c0 (63 байт)
- одной копией существующего кода меньше: 0x494e750 (78 байт) CModifierFactory<CDOTA_Modifier_Jakiro_DualBreath_Burn>::vfunc#0
- одной копией существующего кода меньше: 0x69fab30 (1984 байт)


## Строки библиотек

<details><summary>dota-bin/libclient.so: строки</summary>

**Добавлено — Сообщения и описания (1)**

```
Message %s(%u) from %s claimed client_steam_id %s with gc_msg_src %d.
```

**Удалено — Имена из игры (модификаторы, способности, предметы, юниты, события) (1)**

```
modifier_lycan_wolf_bite_attack_range
```

**Удалено — C++ классы (RTTI) (2)**

```
16CModifierFactoryI43CDOTA_Modifier_Lycan_Wolf_Bite_Attack_RangeE
43CDOTA_Modifier_Lycan_Wolf_Bite_Attack_Range
```

**Удалено — Прочие идентификаторы (1)**

```
CDOTA_Modifier_Lycan_Wolf_Bite_Attack_Range
```

</details>

<details><summary>dota-bin/libserver.so: строки</summary>

**Добавлено — Сообщения и описания (1)**

```
Message %s(%u) from %s claimed client_steam_id %s with gc_msg_src %d.
```

**Удалено — Имена из игры (модификаторы, способности, предметы, юниты, события) (1)**

```
modifier_lycan_wolf_bite_attack_range
```

**Удалено — C++ классы (RTTI) (2)**

```
16CModifierFactoryI43CDOTA_Modifier_Lycan_Wolf_Bite_Attack_RangeE
43CDOTA_Modifier_Lycan_Wolf_Bite_Attack_Range
```

**Удалено — Прочие идентификаторы (1)**

```
CDOTA_Modifier_Lycan_Wolf_Bite_Attack_Range
```

</details>
