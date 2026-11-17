# Dota 6976: изменения кода по функциям

Снимки `6975-11236380` → `6976-11246070`; funcdiff.py. В диффе: [S:…] — строка, [K:…] — константа из данных, F — вызов другой функции, L — переход внутри функции, [D]/[T] — прочие адреса. Регистры и смещения стека меняются и от перекомпиляции.

## libclient.so: функций 280911 → 280911; без изменений 280903, изменено 6, добавлено 2, удалено 1

### изменена: 0x3dbe550 (2226 байт) | строки: "minimap_radar.target"; "minimap_radar.cycle"; "scan_minimap.activate"; "attack"; "impact"; "coins"; "DOTA_Item.SmokeOfDeceit.Activate"; "Rune.Bounty"
было: 0x3dbe410 (2242 байт)
- инструкций: 456 → 452
```diff
@@ -349,17 +349,17 @@
 je L
 call F
+test eax, eax
+je L
 mov rdi, qword ptr [rbp - 0x200]
 lea rsi, [S:"Rune.Illusion"]
 cmp rdi, rsi
 je L
-test eax, eax
-je L
-call F
+call F
+test eax, eax
+je L
 mov rdi, qword ptr [rbp - 0x200]
 lea rsi, [S:"Rune.Invis"]
 cmp rdi, rsi
 je L
-test eax, eax
-je L
 call F
 mov rdi, qword ptr [rbp - 0x200]
@@ -370,20 +370,16 @@
 je L
 call F
+test eax, eax
+je L
 mov rdi, qword ptr [rbp - 0x200]
 lea rsi, [S:"Rune.Regen"]
-cmp rdi, rsi
-je L
-test eax, eax
-je L
-call F
-test eax, eax
-je L
+call F
+test al, al
+jne L
 mov rdi, qword ptr [rbp - 0x200]
 lea rsi, [S:"Rune.Haste"]
-cmp rdi, rsi
-je L
-call F
-test eax, eax
-je L
+call F
+test al, al
+jne L
 mov rdi, qword ptr [rbp - 0x200]
 lea rsi, [S:"Rune.Arcane"]
@@ -431,5 +427,5 @@
 test al, al
 je L
-nop dword ptr [rax + rax]
+nop word ptr [rax + rax]
 movabs rax, 0xffffffff00000000
 mov qword ptr [rbx + 8], 0
```

### изменена: 0x3df85b0 (3869 байт) вызывается из: CPhysicsGameSystem::vfunc#15 | строки: "<empty>"; "world_physics.vphys"; "maps/%s/%s"; "world_physics.vmdl"
было: 0x3df8470 (3882 байт)
- прямых вызовов: 71 → 70
- инструкций: 797 → 802
```diff
@@ -7,8 +7,8 @@
 push rbx
 xor ebx, ebx
-sub rsp, 0x248
+sub rsp, 0x238
 mov qword ptr [rbp - 0x258], rdi
 mov rdi, qword ptr [D]
-mov dword ptr [rbp - 0x24c], esi
+mov dword ptr [rbp - 0x250], esi
 call F
 test rax, rax
@@ -21,5 +21,5 @@
 jne L
 mov ebx, dword ptr [rdi + 0xe0]
-mov esi, dword ptr [rbp - 0x24c]
+mov esi, dword ptr [rbp - 0x250]
 lea r14, [D]
 mov rdi, qword ptr [D]
@@ -37,5 +37,5 @@
 test r14, r14
 cmove r14, rax
-mov eax, dword ptr [rbp - 0x24c]
+mov eax, dword ptr [rbp - 0x250]
 mov r12, qword ptr [D]
 test eax, eax
@@ -64,5 +64,5 @@
 test eax, eax
 jne L
-add rsp, 0x248
+add rsp, 0x238
 mov eax, r15d
 pop rbx
@@ -74,5 +74,5 @@
 ret
 nop dword ptr [rax + rax]
-mov edx, dword ptr [rbp - 0x24c]
+mov edx, dword ptr [rbp - 0x250]
 mov esi, ebx
 mov rdi, qword ptr [rbp - 0x258]
@@ -104,5 +104,5 @@
 je L
 add eax, 1
-mov ecx, dword ptr [rbp - 0x24c]
+mov ecx, dword ptr [rbp - 0x250]
 mov dword ptr [r12 + 0x20], eax
 mov rax, qword ptr [r12 + 0x28]
@@ -110,20 +110,16 @@
 jmp L
 nop dword ptr [rax + rax]
-lea rax, [rbp - 0x230]
+lea r15, [rbp - 0x1f0]
+xor eax, eax
+mov rdx, r14
 pxor xmm0, xmm0
+lea rcx, [S:"world_physics.vphys"]
+mov rdi, r15
+movaps xmmword ptr [rbp - 0x240], xmm0
+lea rsi, [S:"maps/%s/%s"]
 mov qword ptr [rbp - 0x230], 0
-mov rdi, rax
-movaps xmmword ptr [rbp - 0x240], xmm0
-lea r15, [rbp - 0x1f0]
-mov qword ptr [rbp - 0x268], rax
 mov byte ptr [rbp - 0x228], 0
 mov qword ptr [rbp - 0x220], 0
 call F
-xor eax, eax
-mov rdx, r14
-mov rdi, r15
-lea rcx, [S:"world_physics.vphys"]
-lea rsi, [S:"maps/%s/%s"]
-call F
 test dword ptr [rbp - 0x1f0], 0x3fffffff
 jne L
@@ -150,5 +146,5 @@
 lea rax, [D]
 movss xmm5, dword ptr [K:1]
-mov esi, dword ptr [rbp - 0x24c]
+mov esi, dword ptr [rbp - 0x250]
 mov rdi, qword ptr [D]
 movaps xmm0, xmmword ptr [rax]
@@ -173,5 +169,5 @@
 je L
 mov rdi, qword ptr [D]
-mov esi, dword ptr [rbp - 0x24c]
+mov esi, dword ptr [rbp - 0x250]
 call F
 lea rdi, [D]
@@ -211,5 +207,5 @@
 movlhps xmm0, xmm1
 movaps xmmword ptr [rbp - 0x210], xmm0
-mov edx, dword ptr [rbp - 0x24c]
+mov edx, dword ptr [rbp - 0x250]
 mov esi, ebx
 mov rdi, qword ptr [rbp - 0x258]
@@ -248,5 +244,5 @@
 call qword ptr [rax + 0x630]
 mov dword ptr [rbp - 0x248], 0
-nop dword ptr [rax + rax]
+nop word ptr [rax + rax]
 mov rdi, qword ptr [rbp - 0x240]
 xor ebx, ebx
@@ -296,5 +292,5 @@
 jne L
 mov rdi, qword ptr [rbp - 0x240]
-mov eax, dword ptr [rbp - 0x24c]
+mov eax, dword ptr [rbp - 0x250]
 movq xmm0, rdi
 mov dword ptr [rbp - 0x110], eax
@@ -324,18 +320,18 @@
 mov qword ptr [rbp - 0xb8], rax
 mov rax, qword ptr [rbp - 0x258]
-movzx esi, word ptr [rax + 0x82]
+movzx edi, word ptr [rax + 0x82]
 movzx ebx, word ptr [rax + 0x90]
-mov r8d, esi
-and r8w, 0x7fff
+mov edx, edi
+and dx, 0x7fff
 cmp bx, -1
```
(ещё 445 строк диффа: so-query.py fdiff libclient.so 0x3df85b0)

### изменена: 0x3e0c630 (500 байт) | строки: "CEnvSoundscapeProxyAlias_snd_soundscape_proxy"
было: 0x3e0c4f0 (524 байт)
- числа в инструкциях: +0xcf36e6d1 −0x37d2c6a7 −0x5bd1e995 −0x72b7c3d3
- прямых вызовов: 11 → 10
- инструкций: 114 → 110
```diff
@@ -58,9 +58,5 @@
 je L
 lea rdi, [D]
-mov esi, 0x37d2c6a7
-call F
-lea rdi, [D]
-imul esi, eax, 0x5bd1e995
-xor esi, 0x72b7c3d3
+mov esi, 0xcf36e6d1
 call F
 lea rdi, [D]
```

### изменена: 0x3e0cc70 (325 байт)
было: 0x3e0cb80 (277 байт)
- прямых вызовов: 3 → 5
- инструкций: 78 → 92
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
 test esi, esi
 jle L
```

### изменена: 0x4f97b80 (557 байт) | строки: "GET"; "HEAD"; "POST"; "PUT"; "DELETE"; "OPTIONS"
было: 0x4f97a00 (555 байт)
- инструкций: 138 → 137
```diff
@@ -33,6 +33,6 @@
 cmp rax, 0x6031f2df
 je L
+add rsp, 0x10
 xor eax, eax
-add rsp, 0x10
 pop rbx
 pop r12
@@ -125,14 +125,13 @@
 je L
 lea rdi, [D]
+mov rsi, rbx
 xor eax, eax
-mov rsi, rbx
 call F
+jmp L
+nop word ptr [rax + rax]
 xor eax, eax
-jmp L
-nop dword ptr [rax]
+ret
+nop dword ptr [rax + rax]
 call F
 mov rsi, rax
 jmp L
-nop dword ptr [rax]
-xor eax, eax
-ret
```

### изменена: 0x4fa73f0 (10012 байт) | строки: "CNetworkUtlVectorBase< EHANDLE, NetworkVar_m_hItems , 25 , int >"; "m_hItems"; "CHandle< T >"; "uint32"; "C_BaseEntity"; "CHandle< %s >"; "ehandle"; "CUtlVector"
было: 0x4fa7270 (10012 байт)
- числа в инструкциях: −0x5bd1e995 −0x258a6424
- прямых вызовов: 237 → 238
- инструкций: 1914 → 1916
```diff
@@ -1307,15 +1307,16 @@
 mov esi, eax
 call F
+lea rdi, [r13 + 0x10]
+mov esi, eax
+call F
 mov rsi, rbx
 mov r9d, 2
 mov r8d, 0xf0
-imul edx, eax, 0x5bd1e995
 lea rbx, [D]
+mov edx, eax
+shr eax, 0xd
 lea rcx, [rbp - 0xc0]
-mov rdi, rbx
-xor edx, 0x258a6424
-mov eax, edx
-shr eax, 0xd
 xor eax, edx
+mov rdi, rbx
 imul eax, eax, 0x5bd1e995
 mov edx, eax
@@ -1332,4 +1333,5 @@
 call F
 jmp L
+nop
 mov eax, r12d
 xor edx, edx
```

### добавлена: 0x3d9fce0 (299 байт) вызывается из: CVScriptGameSystem::vfunc#85 | строки: "dota_camera_set_position "; "+dota_camera_center_on_hero"; "dota_enable_new_player_shop "; "inspectheroinworld"

### добавлена: 0x4f93210 (103 байт)

### удалена: 0x3d9bb80 (40 байт) вызывается из: CVScriptGameSystem::vfunc#85

### копии существующего кода (1): шаблонные / склеенные компоновщиком функции, такой же код есть и в другой сборке — не новый код
- одной копией существующего кода меньше: 0x3e0cb40 (48 байт)

## libserver.so: функций 220000 → 220004; без изменений 219907, изменено 92, добавлено 2, удалено 1

### изменена: 0x3a40ef0 (769 байт) вызывается из: CPulseInlineValueTypeInfo<ParticleIndex_t>::vfunc#17, CPulseInlineValueTypeInfo<CPlayerSlot>::vfunc#17, CGlowProperty::vfunc#2 | строки: "N(L"; "Unsupported KV3 basic type '%s' (%d)!"; "Pointers cannot be used as numeric values"
было: 0x3a40db0 (769 байт)
- строки: +"N(L" −"&%L"
- инструкций: 221 → 221
```diff
@@ -20,5 +20,5 @@
 cmp bl, 6
 ja L
-lea rdx, [S:"&%L"]
+lea rdx, [D]
 movzx eax, bl
 movsxd rax, dword ptr [rdx + rax*4]
@@ -31,5 +31,5 @@
 cmp bl, 6
 ja L
-lea rdx, [D]
+lea rdx, [S:"N(L"]
 movzx eax, bl
 movsxd rax, dword ptr [rdx + rax*4]
```

### изменена: 0x3a53b70 (515 байт) | строки: "CPanoramaImageName"; "ELanguage"; "CUtlVector"; "CUtlOrderedMap"
было: 0x3a53a30 (515 байт)
- строки: −"TMM"
- инструкций: 146 → 146
```diff
@@ -2,5 +2,5 @@
 ja L
 push rbp
-lea rdx, [S:"TMM"]
+lea rdx, [D]
 mov edi, edi
 mov rbp, rsp
```

### изменена: 0x3a742b0 (961 байт) | строки: "JLO"; "%g %g %g"; "(null)"; "%g %g %g %g"; "unknown_variant_type"; "yLO"; "%lld"; "%llu"
было: 0x3a74170 (961 байт)
- строки: +"JLO" +"yLO"
- инструкций: 213 → 213
```diff
@@ -7,5 +7,5 @@
 cmp al, 0x4f
 ja L
-lea rcx, [D]
+lea rcx, [S:"JLO"]
 movzx edx, al
 movsxd rdx, dword ptr [rcx + rdx*4]
@@ -91,5 +91,5 @@
 cmp al, 0x47
 ja L
-lea rdx, [D]
+lea rdx, [S:"yLO"]
 movzx eax, al
 movsxd rax, dword ptr [rdx + rax*4]
```

### изменена: 0x3a86410 (507 байт)
было: 0x3a862d0 (507 байт)
- строки: −",jP"
- инструкций: 133 → 133
```diff
@@ -12,5 +12,5 @@
 cmp al, 0x24
 ja L
-lea rcx, [S:",jP"]
+lea rcx, [D]
 movzx eax, al
 movsxd rax, dword ptr [rcx + rax*4]
```

### изменена: 0x3aa2da0 (403 байт)
было: 0x3aa2ac0 (403 байт)
- строки: −"L#R"
- инструкций: 127 → 127
```diff
@@ -10,5 +10,5 @@
 movsxd r12, edx
 push rbx
-lea rdx, [S:"L#R"]
+lea rdx, [D]
 mov rbx, rsi
 sub rsp, 0x18
```

### изменена: 0x3aa3160 (680 байт) | строки: "4)R"
было: 0x3aa3020 (680 байт)
- строки: +"4)R" −"t(R"
- инструкций: 191 → 191
```diff
@@ -10,5 +10,5 @@
 movsxd r12, edx
 push rbx
-lea rdx, [S:"t(R"]
+lea rdx, [S:"4)R"]
 mov rbx, rsi
 sub rsp, 0x18
```

### изменена: 0x3ab3f80 (561 байт) вызывается из: CHitboxComponent::vfunc#4 | строки: "Unsupported KV3 basic type '%s' (%d)!"; "Pointers cannot be used as numeric values"
было: 0x3ab3e40 (561 байт)
- строки: −"_!S"
- инструкций: 151 → 151
```diff
@@ -11,5 +11,5 @@
 cmp r8b, 6
 ja L
-lea rdx, [S:"_!S"]
+lea rdx, [D]
 movzx eax, r8b
 movsxd rax, dword ptr [rdx + rax*4]
```

### изменена: 0x3ab4290 (488 байт) | строки: "Unsupported KV3 basic type '%s' (%d)!"; "Pointers cannot be used as numeric values"
было: 0x3ab4150 (488 байт)
- строки: −"S$S"
- инструкций: 147 → 147
```diff
@@ -11,5 +11,5 @@
 cmp r8b, 6
 ja L
-lea rdx, [S:"S$S"]
+lea rdx, [D]
 movzx eax, r8b
 movsxd rax, dword ptr [rdx + rax*4]
```

### изменена: 0x3ab5f80 (625 байт)
было: 0x3ab5e40 (625 байт)
- строки: −";CS"
- инструкций: 115 → 115
```diff
@@ -2,5 +2,5 @@
 ja L
 push rbp
-lea rdx, [S:";CS"]
+lea rdx, [D]
 mov edi, edi
 mov rbp, rsp
```

### изменена: 0x3ac5fb0 (2663 байт) вызывается из: CChoreoComponent::vfunc#2 | строки: "m_hOwner"; "IKV3TransferInterface_EHandle_Load"; "m_nExernalChoreoGraphCount"; "m_sActiveExternalChoreoGraphSlotID"; "m_nNextSceneEventId"; "m_flAllowResponsesEndTime"; "IKV3TransferInterface_GameTime_Load"; "zKT"
было: 0x3ac5e70 (2663 байт)
- строки: +"zKT" −"VHT"
- инструкций: 616 → 616
```diff
@@ -148,5 +148,5 @@
 cmp r8b, 6
 ja L
-lea rdx, [S:"VHT"]
+lea rdx, [D]
 movzx eax, r8b
 movsxd rax, dword ptr [rdx + rax*4]
@@ -212,5 +212,5 @@
 cmp al, 6
 ja L
-lea rdx, [D]
+lea rdx, [S:"zKT"]
 movzx eax, al
 movsxd rax, dword ptr [rdx + rax*4]
```

### изменена: 0x3ac82e0 (1113 байт) CNetworkTransmitComponent::vfunc#3 | строки: "m_nTransmitStateOwnedCounter"; "0gT"; "Unsupported KV3 basic type '%s' (%d)!"; "Pointers cannot be used as numeric values"
было: 0x3ac81a0 (1113 байт)
- строки: +"0gT" −"pfT" −"TfT"
- инструкций: 259 → 259
```diff
@@ -51,5 +51,5 @@
 cmp r8b, 6
 ja L
-lea rdx, [S:"pfT"]
+lea rdx, [S:"0gT"]
 movzx eax, r8b
 movsxd rax, dword ptr [rdx + rax*4]
@@ -108,5 +108,5 @@
 cmp r8b, 6
 ja L
-lea rdx, [S:"TfT"]
+lea rdx, [D]
 movzx eax, r8b
 movsxd rax, dword ptr [rdx + rax*4]
```

### изменена: 0x3ac98d0 (288 байт) вызывается из: CChoreo_GraphController::vfunc#6 | строки: "bzT"; "unknown"; "false"; "true"; "transform"; "vector"; "float"; "globalSymbol"
было: 0x3ac9790 (288 байт)
- строки: +"bzT"
- инструкций: 68 → 68
```diff
@@ -18,5 +18,5 @@
 cmp al, 5
 ja L
-lea rdx, [D]
+lea rdx, [S:"bzT"]
 movzx eax, al
 movsxd rax, dword ptr [rdx + rax*4]
```

### изменена: 0x3b0af40 (183 байт)
было: 0x3b0ae00 (183 байт)
- строки: −"CmX"
- инструкций: 55 → 55
```diff
@@ -2,5 +2,5 @@
 ja L
 push rbp
-lea rdx, [S:"CmX"]
+lea rdx, [D]
 mov edi, edi
 mov rbp, rsp
```

### изменена: 0x3b0b0f0 (117 байт) | строки: "9oX"
было: 0x3b0afb0 (117 байт)
- строки: +"9oX" −"ynX"
- инструкций: 39 → 39
```diff
@@ -2,5 +2,5 @@
 cmp edx, 6
 ja L
-lea rcx, [S:"ynX"]
+lea rcx, [S:"9oX"]
 push rbp
 mov rdi, rsi
```

### изменена: 0x3b28ed0 (2751 байт) CBaseCubemap::vfunc#2 | строки: "customcubemaptexture"; "influenceradius"; "box_mins"; "box_maxs"; "moveable"; "handshake"; "array_index"; "indoor_outdoor_level"
было: 0x3b28d90 (2751 байт)
- строки: +"dTZ" +"QTZ"
- инструкций: 670 → 670
```diff
@@ -264,5 +264,5 @@
 cmp dl, 6
 ja L
-lea rcx, [D]
+lea rcx, [S:"dTZ"]
 movzx edx, dl
 movsxd rdx, dword ptr [rcx + rdx*4]
@@ -314,5 +314,5 @@
 cmp dl, 6
 ja L
-lea rcx, [D]
+lea rcx, [S:"QTZ"]
 movzx edx, dl
 movsxd rdx, dword ptr [rcx + rdx*4]
```

### изменена: 0x3b2a330 (1379 байт) | строки: "\\^Z"; "IPhysicsMotionController"; "CUtlVector"
было: 0x3b2a1f0 (1379 байт)
- строки: +"\\^Z"
- инструкций: 285 → 285
```diff
@@ -2,5 +2,5 @@
 ja L
 push rbp
-lea rdx, [D]
+lea rdx, [S:"\\^Z"]
 mov edi, edi
 mov rbp, rsp
```

### изменена: 0x3b2b6d0 (983 байт) | строки: "]tZ"; "AtZ"; "Unsupported KV3 basic type '%s' (%d)!"; "Pointers cannot be used as numeric values"
было: 0x3b2b590 (983 байт)
- строки: +"]tZ" +"AtZ"
- инструкций: 248 → 248
```diff
@@ -44,5 +44,5 @@
 cmp r8b, 6
 ja L
-lea rdx, [D]
+lea rdx, [S:"]tZ"]
 movzx eax, r8b
 movsxd rax, dword ptr [rdx + rax*4]
@@ -88,5 +88,5 @@
 cmp r8b, 6
 ja L
-lea rdx, [D]
+lea rdx, [S:"AtZ"]
 movzx eax, r8b
 movsxd rax, dword ptr [rdx + rax*4]
```

### изменена: 0x3b38120 (167 байт) | строки: "K:["
было: 0x3b37fe0 (167 байт)
- строки: +"K:["
- инструкций: 51 → 51
```diff
@@ -3,5 +3,5 @@
 ja L
 push rbp
-lea rcx, [D]
+lea rcx, [S:"K:["]
 mov rbp, rsp
 sub rsp, 0x10
```

### изменена: 0x3b3a7b0 (1135 байт)
было: 0x3b3a670 (1135 байт)
- строки: −"Xa["
- инструкций: 280 → 280
```diff
@@ -86,5 +86,5 @@
 je L
 ja L
-lea rcx, [S:"Xa["]
+lea rcx, [D]
 movzx edx, al
 movsxd rdx, dword ptr [rcx + rdx*4]
```

### изменена: 0x3b69980 (190 байт) | строки: "+2^"
было: 0x3b69840 (190 байт)
- строки: +"+2^" −"k1^"
- инструкций: 59 → 59
```diff
@@ -3,5 +3,5 @@
 ja L
 push rbp
-lea rcx, [S:"k1^"]
+lea rcx, [S:"+2^"]
 mov rbp, rsp
 sub rsp, 0x10
```

### изменена: 0x3b6a3b0 (167 байт) | строки: "+<^"
было: 0x3b6a270 (167 байт)
- строки: +"+<^" −"k;^"
- инструкций: 51 → 51
```diff
@@ -3,5 +3,5 @@
 ja L
 push rbp
-lea rcx, [S:"k;^"]
+lea rcx, [S:"+<^"]
 mov rbp, rsp
 sub rsp, 0x10
```

### изменена: 0x3b6a4c0 (206 байт) | строки: "C=^"
было: 0x3b6a380 (206 байт)
- строки: +"C=^"
- инструкций: 62 → 62
```diff
@@ -2,5 +2,5 @@
 ja L
 push rbp
-lea rdx, [D]
+lea rdx, [S:"C=^"]
 mov edi, edi
 mov rbp, rsp
```

### изменена: 0x3b9e630 (183 байт)
было: 0x3b9e4f0 (183 байт)
- строки: −"KMa"
- инструкций: 55 → 55
```diff
@@ -2,5 +2,5 @@
 ja L
 push rbp
-lea rdx, [S:"KMa"]
+lea rdx, [D]
 mov edi, edi
 mov rbp, rsp
```

### изменена: 0x3b9f3e0 (307 байт) | строки: "<[a"; "CLightComponent"
было: 0x3b9f2a0 (307 байт)
- строки: +"<[a" −"|Za"
- инструкций: 93 → 93
```diff
@@ -2,5 +2,5 @@
 ja L
 push rbp
-lea rdx, [S:"|Za"]
+lea rdx, [S:"<[a"]
 mov edi, edi
 mov rbp, rsp
```

### изменена: 0x3ba0eb0 (206 байт) | строки: "Kva"
было: 0x3ba0e40 (206 байт)
- строки: +"Kva" −"?va"
- инструкций: 62 → 62
```diff
@@ -2,5 +2,5 @@
 ja L
 push rbp
-lea rdx, [S:"?va"]
+lea rdx, [S:"Kva"]
 mov edi, edi
 mov rbp, rsp
```

### изменена: 0x3ba1120 (206 байт) | строки: "gxa"
было: 0x3ba10b0 (206 байт)
- строки: +"gxa" −"[xa"
- инструкций: 62 → 62
```diff
@@ -2,5 +2,5 @@
 ja L
 push rbp
-lea rdx, [S:"[xa"]
+lea rdx, [S:"gxa"]
 mov edi, edi
 mov rbp, rsp
```

### изменена: 0x3ba1500 (222 байт)
было: 0x3ba13c0 (222 байт)
- строки: −"C{a"
- инструкций: 64 → 64
```diff
@@ -2,5 +2,5 @@
 ja L
 push rbp
-lea rdx, [S:"C{a"]
+lea rdx, [D]
 mov edi, edi
 mov rbp, rsp
```

### изменена: 0x3ba16f0 (275 байт) | строки: "`}a"; "fogparams_t"
было: 0x3ba15b0 (275 байт)
- строки: +"`}a"
- инструкций: 82 → 82
```diff
@@ -2,5 +2,5 @@
 ja L
 push rbp
-lea rdx, [D]
+lea rdx, [S:"`}a"]
 mov edi, edi
 mov rbp, rsp
```

### изменена: 0x3bae2c0 (275 байт) | строки: "8Gb"; "CPointCamera"
было: 0x3bae180 (275 байт)
- строки: +"8Gb" −"xFb"
- инструкций: 88 → 88
```diff
@@ -2,5 +2,5 @@
 ja L
 push rbp
-lea rdx, [S:"xFb"]
+lea rdx, [S:"8Gb"]
 mov edi, edi
 mov rbp, rsp
```

### изменена: 0x3bae440 (206 байт)
было: 0x3bae300 (206 байт)
- строки: −"SHb"
- инструкций: 62 → 62
```diff
@@ -2,5 +2,5 @@
 ja L
 push rbp
-lea rdx, [S:"SHb"]
+lea rdx, [D]
 mov edi, edi
 mov rbp, rsp
```

### изменена: 0x3bae990 (190 байт) | строки: "7Nb"
было: 0x3bae850 (190 байт)
- строки: +"7Nb" −"wMb"
- инструкций: 59 → 59
```diff
@@ -3,5 +3,5 @@
 ja L
 push rbp
-lea rcx, [S:"wMb"]
+lea rcx, [S:"7Nb"]
 mov rbp, rsp
 sub rsp, 0x10
```

### изменена: 0x3bcc7b0 (1712 байт) CEntityOutputTemplate<SndOpEventGuid_t>::vfunc#2 | строки: "m_Value"; "Stack depth limit hit (%d)"; "A d"; "public.aabb_min"; "public.aabb_max"
было: 0x3bcc670 (1712 байт)
- строки: +"A d"
- инструкций: 409 → 409
```diff
@@ -90,5 +90,5 @@
 cmp al, 6
 ja L
-lea rdx, [D]
+lea rdx, [S:"A d"]
 movzx eax, al
 movsxd rax, dword ptr [rdx + rax*4]
```

### изменена: 0x3bd0cd0 (270 байт) | строки: "'cd"
было: 0x3bd0b90 (270 байт)
- строки: +"'cd" −"gbd"
- инструкций: 67 → 67
```diff
@@ -2,5 +2,5 @@
 ja L
 push rbp
-lea rdx, [S:"gbd"]
+lea rdx, [S:"'cd"]
 mov edi, edi
 mov rbp, rsp
```

### изменена: 0x3bd0e80 (334 байт)
было: 0x3bd0d40 (334 байт)
- строки: −";dd"
- инструкций: 75 → 75
```diff
@@ -2,5 +2,5 @@
 ja L
 push rbp
-lea rdx, [S:";dd"]
+lea rdx, [D]
 mov edi, edi
 mov rbp, rsp
```

### изменена: 0x3bd1200 (238 байт)
было: 0x3bd10c0 (238 байт)
- строки: −"#gd"
- инструкций: 65 → 65
```diff
@@ -2,5 +2,5 @@
 ja L
 push rbp
-lea rdx, [S:"#gd"]
+lea rdx, [D]
 mov edi, edi
 mov rbp, rsp
```

### изменена: 0x3bdd6d0 (270 байт) | строки: ".,e"
было: 0x3bdd590 (270 байт)
- строки: +".,e" −"n+e"
- инструкций: 69 → 69
```diff
@@ -5,5 +5,5 @@
 cmp edi, 6
 ja L
-lea rdx, [S:"n+e"]
+lea rdx, [S:".,e"]
 mov edi, edi
 mov rbx, rsi
```

### изменена: 0x3be09e0 (680 байт) | строки: "\\^e"
было: 0x3be08a0 (680 байт)
- строки: +"\\^e"
- инструкций: 191 → 191
```diff
@@ -10,5 +10,5 @@
 movsxd r12, edx
 push rbx
-lea rdx, [D]
+lea rdx, [S:"\\^e"]
 mov rbx, rsi
 sub rsp, 0x18
```

### изменена: 0x3be12e0 (680 байт) | строки: "$ge"
было: 0x3be11a0 (680 байт)
- строки: +"$ge" −"dfe"
- инструкций: 191 → 191
```diff
@@ -10,5 +10,5 @@
 movsxd r12, edx
 push rbx
-lea rdx, [S:"dfe"]
+lea rdx, [S:"$ge"]
 mov rbx, rsi
 sub rsp, 0x18
```

### изменена: 0x3c314c0 (243 байт) | строки: "x*j"; "VectorWS"
было: 0x3c31380 (243 байт)
- строки: +"x*j"
- инструкций: 67 → 67
```diff
@@ -1,5 +1,5 @@
 cmp edi, 6
 ja L
-lea rdx, [D]
+lea rdx, [S:"x*j"]
 mov edi, edi
 push rbp
```

### изменена: 0x3c315c0 (227 байт) | строки: "d+j"; "VectorWS"
было: 0x3c31480 (227 байт)
- строки: +"d+j"
- инструкций: 74 → 74
```diff
@@ -1,5 +1,5 @@
 cmp edi, 6
 ja L
-lea rcx, [D]
+lea rcx, [S:"d+j"]
 mov edi, edi
 push rbp
```

### изменена: 0x3c316b0 (339 байт) | строки: "8,j"; "BASEPTR"; "GameTick_t"
было: 0x3c31570 (339 байт)
- строки: +"8,j" −"x+j"
- инструкций: 90 → 90
```diff
@@ -1,5 +1,5 @@
 cmp edi, 6
 ja L
-lea rdx, [S:"x+j"]
+lea rdx, [S:"8,j"]
 mov edi, edi
 push rbp
```

### изменена: 0x3c31f90 (243 байт) | строки: "VectorWS"
было: 0x3c31e50 (243 байт)
- строки: −"<4j"
- инструкций: 76 → 76
```diff
@@ -2,5 +2,5 @@
 ja L
 push rbp
-lea rdx, [S:"<4j"]
+lea rdx, [D]
 mov edi, edi
 mov rbp, rsp
```

### изменена: 0x3c32200 (307 байт) | строки: "X7j"; "VectorWS"
было: 0x3c320c0 (307 байт)
- строки: +"X7j"
- инструкций: 94 → 94
```diff
@@ -2,5 +2,5 @@
 ja L
 push rbp
-lea rdx, [D]
+lea rdx, [S:"X7j"]
 mov edi, edi
 mov rbp, rsp
```

### изменена: 0x3c32340 (371 байт) | строки: "|8j"; "GameTime_t"; "CBaseEntity"; "CHandle"
было: 0x3c32200 (371 байт)
- строки: +"|8j"
- инструкций: 112 → 112
```diff
@@ -2,5 +2,5 @@
 ja L
 push rbp
-lea rdx, [D]
+lea rdx, [S:"|8j"]
 mov edi, edi
 mov rbp, rsp
```

### изменена: 0x3c328c0 (183 байт) | строки: "C>j"
было: 0x3c32780 (183 байт)
- строки: +"C>j"
- инструкций: 55 → 55
```diff
@@ -2,5 +2,5 @@
 ja L
 push rbp
-lea rdx, [D]
+lea rdx, [S:"C>j"]
 mov edi, edi
 mov rbp, rsp
```

### изменена: 0x3c329f0 (98 байт)
было: 0x3c328b0 (98 байт)
- строки: −"B>j"
- инструкций: 36 → 36
```diff
@@ -2,5 +2,5 @@
 cmp edx, 6
 ja L
-lea rcx, [S:"B>j"]
+lea rcx, [D]
 push rbp
 mov rdi, rsi
```

### изменена: 0x3c32a60 (98 байт) | строки: "V?j"
было: 0x3c32920 (98 байт)
- строки: +"V?j"
- инструкций: 36 → 36
```diff
@@ -2,5 +2,5 @@
 cmp edx, 6
 ja L
-lea rcx, [D]
+lea rcx, [S:"V?j"]
 push rbp
 mov rdi, rsi
```

### изменена: 0x3c32c40 (117 байт)
было: 0x3c32b00 (117 байт)
- строки: −"Q@j"
- инструкций: 39 → 39
```diff
@@ -2,5 +2,5 @@
 cmp edx, 6
 ja L
-lea rcx, [S:"Q@j"]
+lea rcx, [D]
 push rbp
 mov rdi, rsi
```

### изменена: 0x3c32e90 (136 байт) | строки: "XCj"
было: 0x3c32d50 (136 байт)
- строки: +"XCj"
- инструкций: 43 → 43
```diff
@@ -2,5 +2,5 @@
 cmp edx, 6
 ja L
-lea rcx, [D]
+lea rcx, [S:"XCj"]
 push rbp
 mov rax, rsi
```

### изменена: 0x3c33d80 (206 байт) | строки: "oRj"
было: 0x3c33c40 (206 байт)
- строки: +"oRj"
- инструкций: 62 → 62
```diff
@@ -2,5 +2,5 @@
 ja L
 push rbp
-lea rdx, [D]
+lea rdx, [S:"oRj"]
 mov edi, edi
 mov rbp, rsp
```

### изменена: 0x3c33e50 (206 байт) | строки: "#Sj"
было: 0x3c33d10 (206 байт)
- строки: +"#Sj" −"cRj"
- инструкций: 62 → 62
```diff
@@ -2,5 +2,5 @@
 ja L
 push rbp
-lea rdx, [S:"cRj"]
+lea rdx, [S:"#Sj"]
 mov edi, edi
 mov rbp, rsp
```

### изменена: 0x3c34190 (254 байт) | строки: "wVj"
было: 0x3c34050 (254 байт)
- строки: +"wVj"
- инструкций: 69 → 69
```diff
@@ -2,5 +2,5 @@
 ja L
 push rbp
-lea rdx, [D]
+lea rdx, [S:"wVj"]
 mov edi, edi
 mov rbp, rsp
```

### изменена: 0x3c34900 (811 байт)
было: 0x3c347c0 (811 байт)
- строки: −"4\\j"
- инструкций: 232 → 232
```diff
@@ -9,5 +9,5 @@
 movsxd r13, edx
 push r12
-lea rdx, [S:"4\\j"]
+lea rdx, [D]
 mov r12d, ecx
 push rbx
```

### изменена: 0x3c34c40 (907 байт) | строки: " `j"
было: 0x3c34b00 (907 байт)
- строки: +" `j" −"`_j"
- инструкций: 252 → 252
```diff
@@ -9,5 +9,5 @@
 movsxd r13, edx
 push r12
-lea rdx, [S:"`_j"]
+lea rdx, [S:" `j"]
 mov r12d, ecx
 push rbx
```

### изменена: 0x3c35860 (435 байт) | строки: "CPlayerSlot"; "CUtlVector"
было: 0x3c35720 (435 байт)
- строки: −"Hkj"
- инструкций: 115 → 115
```diff
@@ -1,5 +1,5 @@
 cmp edi, 6
 ja L
-lea rdx, [S:"Hkj"]
+lea rdx, [D]
 mov edi, edi
 push rbp
```

### изменена: 0x3c35be0 (579 байт) | строки: "toj"; "CUtlVector"; "SoundOpvarTraceResult_t"; "AutoRoomDoorwayPairs_t"
было: 0x3c35aa0 (579 байт)
- строки: +"toj"
- инструкций: 143 → 143
```diff
@@ -2,5 +2,5 @@
 ja L
 push rbp
-lea rdx, [D]
+lea rdx, [S:"toj"]
 mov edi, edi
 mov rbp, rsp
```

### изменена: 0x3c360a0 (515 байт) | строки: "VectorWS"; "DamageTypes_t"; "AmmoIndex_t"; "TakeDamageFlags_t"; "HitGroup_t"; "DestructiblePartDamageRequest_t"; "CUtlLeanVector"
было: 0x3c35f60 (515 байт)
- строки: −"Psj"
- инструкций: 142 → 142
```diff
@@ -2,5 +2,5 @@
 ja L
 push rbp
-lea rdx, [S:"Psj"]
+lea rdx, [D]
 mov edi, edi
 mov rbp, rsp
```

### изменена: 0x3c36690 (502 байт)
было: 0x3c36550 (502 байт)
- строки: −"$yj"
- инструкций: 139 → 139
```diff
@@ -21,5 +21,5 @@
 cmp al, 0x24
 ja L
-lea rcx, [S:"$yj"]
+lea rcx, [D]
 movzx eax, al
 movsxd rax, dword ptr [rcx + rax*4]
```

### изменена: 0x3c40eb0 (659 байт) | строки: "CTakeDamageInfo"; "DestructiblePartDamageRequest_t"; "CUtlLeanVector"; "VectorWS"; "TakeDamageFlags_t"; "HitGroup_t"
было: 0x3c40d70 (659 байт)
- строки: −"L k"
- инструкций: 151 → 151
```diff
@@ -1,5 +1,5 @@
 cmp edi, 6
 ja L
-lea rdx, [S:"L k"]
+lea rdx, [D]
 mov edi, edi
 push rbp
```

### изменена: 0x3c41440 (723 байт) | строки: "d&k"; "CUtlVector"; "ragdollelement_t"; "ragdollhierarchyjoint_t"
было: 0x3c41300 (723 байт)
- строки: +"d&k"
- инструкций: 181 → 181
```diff
@@ -2,5 +2,5 @@
 ja L
 push rbp
-lea rdx, [D]
+lea rdx, [S:"d&k"]
 mov edi, edi
 mov rbp, rsp
```

### изменена: 0x3c44670 (4083 байт) вызывается из: CTakeDamageInfo::vfunc#2 | строки: "m_vecDamageForce"; "m_bitsDamageType"; "#\\k"; "m_vecDamagePosition"; "m_vecReportedPosition"; "m_vecDamageDirection"; "m_hInflictor"; "m_hAttacker"
было: 0x3c44530 (4083 байт)
- строки: +"#\\k" +".fk" −"c[k" −"nek" −"Rek"
- инструкций: 886 → 886
```diff
@@ -113,5 +113,5 @@
 cmp r8b, 6
 ja L
-lea rdx, [S:"c[k"]
+lea rdx, [S:"#\\k"]
 movzx eax, r8b
 movsxd rax, dword ptr [rdx + rax*4]
@@ -362,5 +362,5 @@
 cmp r8b, 6
 ja L
-lea rdx, [S:"nek"]
+lea rdx, [S:".fk"]
 movzx eax, r8b
 movsxd rax, dword ptr [rdx + rax*4]
@@ -640,5 +640,5 @@
 cmp r8b, 6
 ja L
-lea rdx, [S:"Rek"]
+lea rdx, [D]
 movzx eax, r8b
 movsxd rax, dword ptr [rdx + rax*4]
```

### изменена: 0x3c46380 (479 байт) | строки: "(uk"
было: 0x3c46240 (479 байт)
- строки: +"(uk" −"htk"
- инструкций: 146 → 146
```diff
@@ -11,5 +11,5 @@
 push rbx
 movsxd rbx, edx
-lea rdx, [S:"htk"]
+lea rdx, [S:"(uk"]
 sub rsp, 0x38
 movsxd rax, dword ptr [rdx + rdi*4]
```

### изменена: 0x3c46560 (479 байт)
было: 0x3c46420 (479 байт)
- строки: −",vk"
- инструкций: 146 → 146
```diff
@@ -11,5 +11,5 @@
 push rbx
 movsxd rbx, edx
-lea rdx, [S:",vk"]
+lea rdx, [D]
 sub rsp, 0x38
 movsxd rax, dword ptr [rdx + rdi*4]
```

### изменена: 0x3c641f0 (851 байт) | строки: "<Hm"; "%llu"
было: 0x3c640b0 (851 байт)
- строки: +"<Hm" −"|Gm"
- инструкций: 190 → 190
```diff
@@ -21,5 +21,5 @@
 mov rbx, rax
 je L
-lea r13, [S:"|Gm"]
+lea r13, [S:"<Hm"]
 nop dword ptr [rax + rax]
 mov qword ptr [rbp - 0xc0], 0
```

### изменена: 0x3c64a00 (819 байт) | строки: "DecalFlags_t"; "GameTime_t"
было: 0x3c648c0 (819 байт)
- строки: −"$Mm"
- инструкций: 143 → 143
```diff
@@ -2,5 +2,5 @@
 ja L
 push rbp
-lea rdx, [S:"$Mm"]
+lea rdx, [D]
 mov edi, edi
 mov rbp, rsp
```

### изменена: 0x3ca3850 (350 байт)
было: 0x3ca3610 (350 байт)
- строки: −"#\"q"
- инструкций: 92 → 92
```diff
@@ -2,5 +2,5 @@
 ja L
 push rbp
-lea rdx, [S:"#\"q"]
+lea rdx, [D]
 mov edi, edi
 mov rbp, rsp
```

### изменена: 0x3ca56b0 (547 байт) | строки: "CHandle"; "CEnvSoundscapeTriggerable"; "CBasePlayerPawn"; "CUtlVector"
было: 0x3ca5470 (547 байт)
- строки: −"T?q"
- инструкций: 144 → 144
```diff
@@ -2,5 +2,5 @@
 ja L
 push rbp
-lea rdx, [S:"T?q"]
+lea rdx, [D]
 mov edi, edi
 mov rbp, rsp
```

### изменена: 0x3ca7fa0 (502 байт)
было: 0x3ca7d60 (502 байт)
- строки: −" hq"
- инструкций: 139 → 139
```diff
@@ -21,5 +21,5 @@
 cmp al, 0x24
 ja L
-lea rcx, [S:" hq"]
+lea rcx, [D]
 movzx eax, al
 movsxd rax, dword ptr [rcx + rax*4]
```

### изменена: 0x3cc5770 (4702 байт) | строки: "classname"; "connections"; "attributes"
было: 0x3cc5530 (4702 байт)
- строки: −"8:s" −"@@s"
- инструкций: 1086 → 1086
```diff
@@ -208,5 +208,5 @@
 cmp r14b, 0x4f
 ja L
-lea rsi, [S:"8:s"]
+lea rsi, [D]
 movsxd rax, dword ptr [rsi + r14*4]
 add rax, rsi
@@ -617,5 +617,5 @@
 cmp al, 0x4f
 ja L
-lea rsi, [S:"@@s"]
+lea rsi, [D]
 movzx edx, al
 movsxd rdx, dword ptr [rsi + rdx*4]
```

### изменена: 0x3cc8f80 (2602 байт) | строки: "uint64"; "vks"
было: 0x3cc8d40 (2602 байт)
- строки: +"vks"
- инструкций: 588 → 588
```diff
@@ -554,5 +554,5 @@
 cmp al, 0x39
 ja L
-lea rdx, [D]
+lea rdx, [S:"vks"]
 movsxd rax, dword ptr [rdx + rax*4]
 add rax, rdx
```

### изменена: 0x3cd5ee0 (542 байт) | строки: "D7t"
было: 0x3cd5ca0 (542 байт)
- строки: +"D7t"
- инструкций: 159 → 159
```diff
@@ -9,5 +9,5 @@
 movsxd r12, edx
 push rbx
-lea rdx, [D]
+lea rdx, [S:"D7t"]
 mov rbx, rsi
 sub rsp, 0x10
```

### изменена: 0x3cda090 (754 байт) | строки: "<yt"
было: 0x3cd9e50 (754 байт)
- строки: +"<yt" −"|wt"
- инструкций: 202 → 202
```diff
@@ -3,5 +3,5 @@
 ja L
 push rbp
-lea rdx, [S:"|wt"]
+lea rdx, [S:"<yt"]
 mov rbp, rsp
 push r14
```

### изменена: 0x3cde440 (10439 байт) | строки: "GetLocalPlayer"; "GetLocalPlayerPawn"; "First"; "!The global list of entities"; "CScriptEntityIterator"; "Begin an iteration over the list of entities"; "Continue an iteration over the list of entities, providing reference to a previo"; "Get the local player controller (backcompat)."
было: 0x3cde200 (10535 байт)
- строки: −"FindByNameWithin"
- числа в инструкциях: −0 −1 −1 −0xff1d
- поля объектов: −0x18 −0x20 −0x20 −0x20 −0x28 −0x28 −0x30 −0x10
- инструкций: 2683 → 2664
```diff
@@ -1644,10 +1644,11 @@
 mov byte ptr [rax + 0x19], 0xc
 lea rdx, [T]
+mov qword ptr [rax + 0x38], r12
 mov rdi, rbx
-mov qword ptr [rax + 0x38], r12
+mov r12d, 0x20
 mov qword ptr [rax + 0x40], rdx
-lea rbx, [S:"Find entities by model name."]
 mov dword ptr [rax + 0x48], 1
 call F
+lea rdi, [S:"Find entities by model name."]
 movddup xmm0, qword ptr [D]
 cdqe
@@ -1656,12 +1657,11 @@
 add rax, qword ptr [r15 + 0x28]
 movsx rsi, byte ptr [rax + 0x1a]
-mov qword ptr [rax + 0x10], rbx
-mov ebx, 0x20
 mov qword ptr [rax + 0x30], r15
+mov qword ptr [rax + 0x10], rdi
 movups xmmword ptr [rax], xmm0
 mov rcx, rsi
 mov byte ptr [rax + rsi + 0x1b], 0x1e
 add ecx, 1
-mov word ptr [rax + 0x18], bx
+mov word ptr [rax + 0x18], r12w
 mov byte ptr [rax + 0x1a], cl
 movsx ecx, cl
@@ -1750,161 +1750,150 @@
 jne L
 mov byte ptr [rax + 0x19], 0xc
-lea rbx, [T]
+lea rdx, [T]
 mov qword ptr [rax + 0x38], r13
-mov qword ptr [rax + 0x40], rbx
+mov rdi, rbx
+mov qword ptr [rax + 0x40], rdx
 mov dword ptr [rax + 0x48], 1
-movsxd rbx, dword ptr [r15 + 0x20]
-cmp ebx, dword ptr [r15 + 0x30]
-je L
-mov eax, ebx
-mov rcx, qword ptr [r15 + 0x28]
-add eax, 1
-pxor xmm0, xmm0
+call F
+movddup xmm0, qword ptr [D]
 mov r11d, 0x1f
-mov dword ptr [r15 + 0x20], eax
-lea rax, [rbx + rbx*4]
-lea rbx, [S:"Find entities by model name within a radius. Pass 'null' to start an iteration, or reference to a previously found entit"]
-shl rax, 4
-add rcx, rax
+cdqe
+lea rcx, [rax + rax*4]
```
(ещё 297 строк диффа: so-query.py fdiff libserver.so 0x3cde440)

### изменена: 0x3ce9f20 (317 байт) вызывается из: CVScriptGameSystem::vfunc#85, CDOTAVScriptGameSystem::vfunc#85
было: 0x3ce9d40 (145 байт)
- числа в инструкциях: +2 +0x1e +0x4f +0 +0xc000000800000000 +0x200
- прямых вызовов: 4 → 6
- инструкций: 46 → 94
```diff
@@ -1,31 +1,50 @@
+push rbp
+mov rbp, rsp
+push r15
+push r14
+push r13
+push r12
+mov r12, rdx
+push rbx
+sub rsp, 0x28
 test r8, r8
 sete al
 test rsi, rsi
-setne sil
-or al, sil
+setne dl
+or al, dl
 jne L
 cmp ecx, 2
 je L
+add rsp, 0x28
 xor eax, eax
+pop rbx
+pop r12
+pop r13
+pop r14
+pop r15
+pop rbp
 ret
 nop word ptr [rax + rax]
-push rbp
-mov rbp, rsp
-push r13
-push r12
-mov r12, rdi
-mov rdi, rdx
-push rbx
+movzx edx, byte ptr [r12 + 8]
+mov r13, rdi
 mov rbx, r8
-sub rsp, 0x18
-mov r13, qword ptr [rdx + 0x10]
-call F
-mov rdi, rax
-mov rsi, r13
-call r12
-lea rdi, [rbp - 0x30]
+mov rax, qword ptr [r12 + 0x10]
+cmp dl, 0x1e
+je L
+cmp dl, 2
+je L
+cmp dl, 0x4f
+jne L
+mov rdx, qword ptr [r12]
+lea rdi, [D]
```
(ещё 53 строк диффа: so-query.py fdiff libserver.so 0x3ce9f20)

### изменена: 0x3d144a0 (171 байт) | строки: "0\tx"; "HitGroup_t"
было: 0x3d14220 (171 байт)
- строки: +"0\tx"
- инструкций: 54 → 54
```diff
@@ -1,5 +1,5 @@
 cmp edi, 6
 ja L
-lea rdx, [D]
+lea rdx, [S:"0\tx"]
 mov edi, edi
 push rbp
```

### изменена: 0x3d146a0 (136 байт)
было: 0x3d14420 (136 байт)
- строки: −" \tx"
- инструкций: 45 → 45
```diff
@@ -2,5 +2,5 @@
 cmp edx, 6
 ja L
-lea rcx, [S:" \tx"]
+lea rcx, [D]
 push rbp
 mov rax, rsi
```

### изменена: 0x3d14730 (171 байт) | строки: "VectorWS"
было: 0x3d144b0 (171 байт)
- строки: −"P\tx"
- инструкций: 56 → 56
```diff
@@ -1,5 +1,5 @@
 cmp edi, 6
 ja L
-lea rcx, [S:"P\tx"]
+lea rcx, [D]
 mov edi, edi
 push rbp
```

### изменена: 0x3d172b0 (206 байт) | строки: "k4x"
было: 0x3d17030 (206 байт)
- строки: +"k4x" −"k2x"
- инструкций: 62 → 62
```diff
@@ -2,5 +2,5 @@
 ja L
 push rbp
-lea rdx, [S:"k2x"]
+lea rdx, [S:"k4x"]
 mov edi, edi
 mov rbp, rsp
```

### изменена: 0x3d19840 (483 байт) | строки: "hXx"; "soundlevel_t"; "dynpitchvol_t"; "CGameSoundEventName"
было: 0x3d195c0 (483 байт)
- строки: +"hXx" −"hVx"
- инструкций: 118 → 118
```diff
@@ -2,5 +2,5 @@
 ja L
 push rbp
-lea rdx, [S:"hVx"]
+lea rdx, [S:"hXx"]
 mov edi, edi
 mov rbp, rsp
```

### изменена: 0x3d1a240 (483 байт) | строки: "(bx"; "CRangeInt"; "AmmoFlags_t"; "CRangeFloat"
было: 0x3d19fc0 (483 байт)
- строки: +"(bx" −"(`x"
- инструкций: 123 → 123
```diff
@@ -2,5 +2,5 @@
 ja L
 push rbp
-lea rdx, [S:"(`x"]
+lea rdx, [S:"(bx"]
 mov edi, edi
 mov rbp, rsp
```

### изменена: 0x3d1a670 (499 байт) | строки: ",fx"; "AI_MotorServices_DebugSnapshotData_t::MotorPathWaypoint_t"; "CUtlVector"
было: 0x3d1a3f0 (499 байт)
- строки: +",fx" −",dx"
- инструкций: 129 → 129
```diff
@@ -1,5 +1,5 @@
 cmp edi, 6
 ja L
-lea rdx, [S:",dx"]
+lea rdx, [S:",fx"]
 mov edi, edi
 push rbp
```

### изменена: 0x3d1b180 (612 байт) | строки: "arx"
было: 0x3d1af00 (612 байт)
- строки: +"arx" −"apx"
- инструкций: 139 → 139
```diff
@@ -2,5 +2,5 @@
 ja L
 push rbp
-lea rdx, [S:"apx"]
+lea rdx, [S:"arx"]
 mov edi, edi
 mov rbp, rsp
```

### изменена: 0x3d699e0 (904 байт) | строки: "XW}"
было: 0x3d69760 (904 байт)
- строки: +"XW}" −"XU}"
- инструкций: 238 → 238
```diff
@@ -7,5 +7,5 @@
 mov r15d, edx
 push r14
-lea rdx, [S:"XU}"]
+lea rdx, [S:"XW}"]
 push r13
 push r12
```

### изменена: 0x3d6b400 (904 байт) | строки: "\\q}"
было: 0x3d6b180 (904 байт)
- строки: +"\\q}" −"\\o}"
- инструкций: 238 → 238
```diff
@@ -7,5 +7,5 @@
 mov r15d, edx
 push r14
-lea rdx, [S:"\\o}"]
+lea rdx, [S:"\\q}"]
 push r13
 push r12
```

### изменена: 0x5119230 (613 байт) | строки: "GET"; "HEAD"; "POST"; "PUT"; "DELETE"; "OPTIONS"
было: 0x5118f30 (571 байт)
- поля объектов: +0x18 +0x210
- инструкций: 143 → 147
```diff
@@ -32,6 +32,6 @@
 cmp rax, 0x6031f2df
 je L
+add rsp, 0x10
 xor eax, eax
-add rsp, 0x10
 pop rbx
 pop r12
@@ -40,11 +40,5 @@
 pop rbp
 ret
-nop dword ptr [rax + rax]
-lea rdi, [rax + 0x850]
-call F
-test rax, rax
-mov rdx, rax
-jne L
-nop dword ptr [rax]
+nop word ptr [rax + rax]
 lea rdi, [D]
 call F
@@ -99,4 +93,15 @@
 ret
 nop dword ptr [rax]
+lea rdi, [rax + 0x850]
+call F
+test rax, rax
+mov rdx, rax
+je L
+mov rax, qword ptr [rdx + 0x18]
+mov rax, qword ptr [rax + 0x210]
+test rax, rax
+jne L
+jmp L
+nop dword ptr [rax]
 lea rsi, [S:"HEAD"]
 mov rdi, rbx
@@ -130,14 +135,13 @@
 je L
 lea rdi, [D]
+mov rsi, rbx
 xor eax, eax
-mov rsi, rbx
 call F
+jmp L
+nop word ptr [rax + rax]
 xor eax, eax
-jmp L
-nop dword ptr [rax]
+ret
+nop dword ptr [rax + rax]
 call F
 mov rsi, rax
 jmp L
-nop dword ptr [rax]
-xor eax, eax
```
(ещё 1 строк диффа: so-query.py fdiff libserver.so 0x5119230)

### изменена: 0x5122300 (1756 байт) | строки: "<NoAbilityName>"
было: 0x5121fc0 (1829 байт)
- числа в инструкциях: −1 −5
- виртуальные вызовы: +0xed0 (слот 474)
- поля объектов: −0x840 −0x840 −0xed0 −0x2ae
- прямых вызовов: 40 → 39
- инструкций: 423 → 407
```diff
@@ -315,14 +315,6 @@
 je L
 mov rax, qword ptr [r12]
-lea rdx, [T]
-mov rax, qword ptr [rax + 0xed0]
-cmp rax, rdx
-jne L
-mov rax, qword ptr [r12 + 0x840]
-test rax, rax
-je L
-movzx eax, byte ptr [rax + 0x2ae]
-shr al, 5
-and eax, 1
+mov rdi, r12
+call qword ptr [rax + 0xed0]
 test al, al
 jne L
@@ -341,5 +333,5 @@
 jne L
 jmp L
-nop
+nop dword ptr [rax + rax]
 xor esi, esi
 mov rdi, r12
@@ -399,12 +391,4 @@
 call rax
 jmp L
-mov rdi, r12
-call rax
-jmp L
-xor esi, esi
-mov rdi, r12
-call F
-mov rax, qword ptr [r12 + 0x840]
-jmp L
 xor esi, esi
 mov rdi, r12
```

### изменена: 0x512f170 (9020 байт) | строки: "m_hItems"; "CNetworkUtlVectorBase< EHANDLE, NetworkVar_m_hItems , 25 , int >"; "CHandle< T >"; "uint32"; "CBaseEntity"; "CHandle< %s >"; "ehandle"; "CUtlVector"
было: 0x512ee70 (9116 байт)
- строки: −"m_bStashEnabled" −"m_bStashEnabled" −"m_bStashEnabled"
- числа в инструкциях: +0 +0
- прямых вызовов: 247 → 245
- инструкций: 1786 → 1763
```diff
@@ -618,14 +618,15 @@
 mov rdi, qword ptr [rbp - 0x108]
 call F
-lea rdi, [S:"m_bStashEnabled"]
+lea r14, [S:"m_bStashEnabled"]
 mov esi, 0x31415929
-call F
-lea rdi, [D]
+mov rdi, r14
+call F
+lea rdi, [r14 + 4]
 mov esi, eax
 call F
-lea rdi, [D]
+lea rdi, [r14 + 8]
 mov esi, eax
 call F
-lea rdi, [D]
+lea rdi, [r14 + 0xc]
 mov esi, eax
 call F
@@ -635,14 +636,13 @@
 mov rsi, r15
 mov dword ptr [rbp - 0xc0], r12d
+mov rdi, rax
+mov rbx, rax
+mov qword ptr [rbp - 0xb8], r14
+call F
+mov eax, dword ptr [D]
 lea r12, [S:"bool"]
-mov rbx, rax
-lea rax, [S:"m_bStashEnabled"]
-mov rdi, rbx
-mov qword ptr [rbp - 0xb8], rax
-call F
-mov eax, dword ptr [D]
-mov rsi, r12
 mov rdi, r15
 mov qword ptr [rbp - 0xc0], 0
+mov rsi, r12
 mov dword ptr [rbx + 0x28], eax
 mov rax, qword ptr [D]
@@ -665,7 +665,8 @@
 mov rdi, r15
 call F
-lea r13, [rbx + 0x18]
-mov rsi, r12
-mov rdi, r13
+lea rax, [rbx + 0x18]
+mov rsi, r12
+mov rdi, rax
+mov qword ptr [rbp - 0x118], rax
 call F
 mov rax, qword ptr [K:0x000000ad00000001]
@@ -675,22 +676,22 @@
 test al, al
```
(ещё 459 строк диффа: so-query.py fdiff libserver.so 0x512f170)

### изменена: 0x594dfe0 (28348 байт) вызывается из: CDOTA_Modifier_Lich_FrostArmor_Autocast::vfunc#126, CDOTA_Ability_Juggernaut_HealingWard::OnSpellStart, CDOTA_Ability_AntiMage_Mana_Overload::OnSpellStart | строки: "../../game/server/dota/dota_execute_orders.cpp"; "DOTA_ExecuteOrders"; "<NoAbilityName>"; "modifier_vengefulspirit_hybrid_special"; "dota_item_used"; "ItemEntityIndex"; "UnitEntityIndex"; "PlayerID"
было: 0x594dd60 (28288 байт)
- числа в инструкциях: +0xffffffff +0xc +0x20 +0x20 +0x3a +0xffff −1 −0 −0 −0 −0 −0 −0 −0 (и ещё 10)
- поля объектов: +0x410 +0x24
- прямых вызовов: 603 → 608
- инструкций: 5655 → 5709
```diff
@@ -3,10 +3,10 @@
 mov rbp, rsp
 push r15
-lea r15, [rbp - 0x150]
+mov r15, rdi
 push r14
+lea rdi, [S:"DOTA_ExecuteOrders"]
 push r13
-mov r13, rdi
+lea r13, [rbp - 0x150]
 push r12
-lea rdi, [S:"DOTA_ExecuteOrders"]
 push rbx
 mov ebx, esi
@@ -15,5 +15,5 @@
 mov byte ptr [rbp - 0x1e6], dl
 lea rsi, [D]
-mov rdx, r15
+mov rdx, r13
 mov qword ptr [rbp - 0x140], rdi
 mov byte ptr [rbp - 0x1e4], cl
@@ -23,5 +23,5 @@
 mov byte ptr [D], 1
 mov qword ptr [rbp - 0x1d8], rax
-mov eax, dword ptr [r13 + 0x28]
+mov eax, dword ptr [r15 + 0x28]
 mov dword ptr [D], eax
 lea rax, [D]
@@ -44,5 +44,5 @@
 cmp qword ptr [r12 + 0xa10], 0
 je L
-mov rsi, r13
+mov rsi, r15
 mov rdi, r12
 call qword ptr [rax + 0x9b0]
@@ -60,5 +60,5 @@
 jmp rax
 nop
-mov eax, dword ptr [r13 + 0x2c]
+mov eax, dword ptr [r15 + 0x2c]
 cmp eax, 0x1b
 mov dword ptr [rbp - 0x1e0], eax
@@ -96,5 +96,5 @@
 test al, al
 jne L
-cmp dword ptr [r13 + 0x24], -1
+cmp dword ptr [r15 + 0x24], -1
 je L
 lea r12, [D]
@@ -102,5 +102,5 @@
 test rdi, rdi
 je L
-mov esi, dword ptr [r13 + 0x24]
+mov esi, dword ptr [r15 + 0x24]
 call F
 test rax, rax
```
(ещё 6728 строк диффа: so-query.py fdiff libserver.so 0x594dfe0)

### изменена: 0x5c26600 (947 байт)
было: 0x5c262b0 (1027 байт)
- числа в инструкциях: −2 −1 −0x38 −3 −0xffffffffffffffff
- поля объектов: −0x61
- прямых вызовов: 12 → 11
- инструкций: 232 → 208
```diff
@@ -1,26 +1,2 @@
-push rbp
-mov rbp, rsp
-push rbx
-mov ebx, esi
-sub rsp, 0x28
-movzx eax, byte ptr [rdi + 0x61]
-test al, 2
-je L
-test al, 1
-je L
-movsxd rax, ebx
-mov rbx, qword ptr [rbp - 8]
-imul rax, rax, 0x38
-add rax, qword ptr [rdi + 8]
-leave
-ret
-nop dword ptr [rax + rax]
-lea rdx, [rbp - 0x18]
-mov esi, 3
-mov qword ptr [rbp - 0x28], rdi
-mov qword ptr [rbp - 0x18], 0xffffffffffffffff
-call F
-mov rdi, qword ptr [rbp - 0x28]
-jmp L
 test edx, edx
 jle L
```

### изменена: 0x3a9ac20 (595 байт) | строки: "CBaseModelEntity"; "CHandle"; "CNetworkUtlVectorBase"; "CUtlSymbolLarge"; "CUtlVector"
- код тот же, но вызывает другую функцию: было 0x3aa2c60, стало 0x3aa2da0

### изменена: 0x3ba0f80 (206 байт)
- код тот же, но вызывает другую функцию: было 0x3b9af70, стало 0x3b9b0c0

### изменена: 0x3ba11f0 (206 байт)
- код тот же, но вызывает другую функцию: было 0x3b9af10, стало 0x3b9b040

### добавлена: 0x3c9e5e0 (415 байт) вызывается из: CVScriptGameSystem::vfunc#85 | строки: "dota_camera_set_position "; "+dota_camera_center_on_hero"; "dota_enable_new_player_shop "; "inspectheroinworld"

### добавлена: 0x50fed30 (151 байт)

### удалена: 0x3c9e4a0 (326 байт) вызывается из: CVScriptGameSystem::vfunc#85 | строки: "Push"; "CTSQueue corruption"; "nTries < 10000000"

### копии существующего кода (3): шаблонные / склеенные компоновщиком функции, такой же код есть и в другой сборке — не новый код
- ещё одна копия существующего кода: 0x3c9e780 (84 байт) вызывается из: CPhysicsGameSystem::vfunc#63 | строки: "Push"; "CTSQueue corruption"; "nTries < 10000000"
- ещё одна копия существующего кода: 0x3c9e7e0 (70 байт) вызывается из: CVScriptGameSystem::vfunc#85, CDOTAVScriptGameSystem::vfunc#85
- ещё одна копия существующего кода: 0x5c26590 (80 байт)
