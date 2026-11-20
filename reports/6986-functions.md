# Dota 6986: изменения кода по функциям и строки библиотек

Снимки `6985-11258601` → `6986-11259680`; funcdiff.py. В диффе: [S:…] — строка, [K:…] — константа из данных, F — вызов другой функции, L — переход внутри функции, [D]/[T] — прочие адреса. Регистры и смещения стека меняются и от перекомпиляции. Здесь всё, в том числе игровые функции и изменения от пересборки.

## libtier0.so: функций 9326 → 9326; без изменений 9323, изменено 3, добавлено 0, удалено 0

### изменена: 0x235370 (179 байт)
было: 0x235370 (190 байт)
- виртуальные вызовы: −0x20 (слот 4)
- цели вызовов: +free()
- инструкций: 61 → 58
```diff
@@ -49,9 +49,6 @@
 mov rdi, rbx
 call F
-mov rax, qword ptr [D]
-mov rsi, r12
-mov rdi, qword ptr [rax]
-mov rax, qword ptr [rdi]
-call qword ptr [rax + 0x20]
+mov rdi, r12
+call F
 add rsp, 0x18
 pop rbx
```

### изменена: 0x239af0 (268 байт) вызывается из: CCommandLine::vfunc#2 | строки: "Plat_GetModuleFilenameNoSymlink"; "%s: Unable to get executable filename (%d byte buffer)."; "Plat_VirtualAlloc"; "false"; "WARNING: Large virtual reservation of %llu bytes of memory (limit %llu)"
было: 0x239af0 (268 байт)
- числа в инструкциях: +0x1420 −0x141d
- инструкций: 61 → 61
```diff
@@ -41,5 +41,5 @@
 add eax, 1
 mov rdx, rsi
-mov dword ptr [rbp - 0x38], 0x141d
+mov dword ptr [rbp - 0x38], 0x1420
 movq xmm0, qword ptr [D]
 mov dword ptr [D], eax
```

### изменена: 0x23baa0 (1073 байт) | строки: "../public/tier0/globallist.h"; "platform.cpp"
было: 0x23baa0 (1073 байт)
- числа в инструкциях: +0x1da0 −0x1d9d
- инструкций: 230 → 230
```diff
@@ -184,5 +184,5 @@
 lea r12, [rbx + 0x20]
 lea rsi, [S:"platform.cpp"]
-mov edx, 0x1d9d
+mov edx, 0x1da0
 mov rdi, r13
 call F
```

## libclient.so: функций 281886 → 281886; без изменений 281875, изменено 6, добавлено 1, удалено 2

### изменена: 0x49f55e0 (6148 байт)
было: 0x49f5280 (6020 байт)
- поля объектов: +0x58
- прямых вызовов: 64 → 68
- цели вызовов: +0x7e1d7e0
- инструкций: 967 → 1002
```diff
@@ -1,4 +1,6 @@
 push rbp
 mov rbp, rsp
+push r13
+push r12
 push rbx
 sub rsp, 8
@@ -9,8 +11,11 @@
 test rax, rax
 je L
-mov rbx, qword ptr [rbp - 8]
-leave
-ret
-nop word ptr [rax + rax]
+add rsp, 8
+pop rbx
+pop r12
+pop r13
+pop rbp
+ret
+nop dword ptr [rax + rax]
 lea rbx, [D]
 mov rdi, rbx
@@ -71,5 +76,5 @@
 test rax, rax
 jne L
-nop
+nop word ptr cs:[rax + rax]
 movzx eax, byte ptr [D]
 test al, al
@@ -95,17 +100,47 @@
 movq xmm3, rax
 mov rax, rbx
-mov rbx, qword ptr [rbp - 8]
 punpcklqdq xmm0, xmm3
 movups xmmword ptr [D], xmm0
-leave
-ret
-nop dword ptr [rax]
-lea rbx, [D]
-mov rdi, rbx
-call F
-test eax, eax
-je L
-call F
-mov rdi, rbx
+add rsp, 8
+pop rbx
+pop r12
+pop r13
+pop rbp
+ret
+nop
+lea rbx, [D]
+mov rdi, rbx
+call F
+test eax, eax
+je L
+movzx eax, byte ptr [D]
+test al, al
+je L
+lea rax, [D]
+mov rdi, rbx
+mov qword ptr [D], rax
+call F
+jmp L
+lea r12, [D]
+mov rdi, r12
+call F
+test eax, eax
+je L
+movzx eax, byte ptr [D]
+test al, al
+je L
+lea rax, [D]
+mov rdi, r12
+mov qword ptr [D], rax
+call F
+jmp L
+lea r13, [D]
+mov rdi, r13
+call F
+test eax, eax
+je L
+call F
+mov rdi, r13
+mov rax, qword ptr [rax + 0x58]
 mov qword ptr [D], rax
 call F
```

### изменена: 0x49f47a0 (803 байт) вызывается из: CDOTA_Modifier_Huskar_Berserkers_Blood::vfunc#88 | строки: "modifier_huskar_berserkers_blood_transfusion_debuff"
было: 0x4a14c50 (680 байт)
- константы из данных (числа логики): +100 +100 +100 +1 +1.85 +1.85
- прямых вызовов: 21 → 22
- цели вызовов: +V_powf()
- инструкций: 163 → 187
```diff
@@ -66,10 +66,9 @@
 imul eax, dword ptr [r12 + 0x1b04]
 mov rdi, r12
-pxor xmm2, xmm2
-cvtsi2ss xmm2, eax
-divss xmm2, dword ptr [K:100]
-movss dword ptr [rbp - 0x24], xmm2
+pxor xmm0, xmm0
+cvtsi2ss xmm0, eax
+divss xmm0, dword ptr [K:100]
+movss dword ptr [rbp - 0x24], xmm0
 call F
-movss xmm2, dword ptr [rbp - 0x24]
 mov rdi, rax
 mov rax, qword ptr [rax]
@@ -78,18 +77,39 @@
 jne L
 mov eax, dword ptr [rdi + 0x4b8]
-pxor xmm1, xmm1
-cvtsi2ss xmm1, eax
+pxor xmm2, xmm2
+cvtsi2ss xmm2, eax
 mov rdi, r12
 movss dword ptr [rbp - 0x28], xmm2
-movss dword ptr [rbp - 0x24], xmm1
 call F
+movss xmm4, dword ptr [rbp - 0x24]
+pxor xmm1, xmm1
+movss xmm2, dword ptr [rbp - 0x28]
+cvtsi2ss xmm1, dword ptr [rax + 0x4bc]
+ucomiss xmm4, xmm2
+jp L
+je L
+movss xmm0, dword ptr [rbp - 0x24]
+subss xmm1, xmm2
+subss xmm0, xmm2
+movss xmm2, dword ptr [K:1]
+divss xmm1, xmm0
 pxor xmm0, xmm0
-movss xmm2, dword ptr [rbp - 0x28]
+cmpltss xmm0, xmm1
+andps xmm1, xmm0
+minss xmm1, xmm2
+movss xmm0, dword ptr [K:100]
+mulss xmm0, xmm1
+pxor xmm1, xmm1
+addss xmm0, xmm1
+movss xmm1, dword ptr [K:1.85]
+call F
+movss xmm1, dword ptr [K:1.85]
+movd r13d, xmm0
+movss xmm0, dword ptr [K:100]
+call F
+movd xmm3, r13d
 mov rdi, r12
-cvtsi2ss xmm0, dword ptr [rax + 0x4bc]
-movss xmm1, dword ptr [rbp - 0x24]
-call F
-mov rdi, r12
-movss dword ptr [rbp - 0x24], xmm0
+divss xmm3, xmm0
+movss dword ptr [rbp - 0x24], xmm3
 call F
 test rax, rax
@@ -135,5 +155,5 @@
 movups xmmword ptr [rbx + 8], xmm0
 jmp L
-nop
+nop dword ptr [rax]
 call rax
 test al, al
@@ -147,13 +167,17 @@
 call F
 jmp L
-movss xmm5, dword ptr [rbp - 0x24]
+subss xmm1, xmm4
+pxor xmm0, xmm0
+movss xmm7, dword ptr [K:100]
+cmpless xmm0, xmm1
+andps xmm0, xmm7
+jmp L
+movss xmm7, dword ptr [rbp - 0x24]
 pxor xmm0, xmm0
 mov dword ptr [rbx], 1
 movups xmmword ptr [rbx + 8], xmm0
-movss dword ptr [rbx + 4], xmm5
+movss dword ptr [rbx + 4], xmm7
 jmp L
-movss dword ptr [rbp - 0x24], xmm2
 call rax
-movss xmm2, dword ptr [rbp - 0x24]
 jmp L
 call rax
```

### изменена: 0x4bee4d0 (245 байт) CDOTA_Modifier_Ogre_Magi_Bloodlust::OnCreated, CDOTA_Modifier_Ogre_Magi_Bloodlust::OnRefresh | строки: "bonus_attack_speed"; "bonus_movement_speed"; "self_bonus"; "modelscale"
было: 0x4beed70 (293 байт)
- поля объектов: −0x1af8 −0x1b00
- прямых вызовов: 14 → 12
- цели вызовов: −0x4f61a80 −0x4f61d80
- инструкций: 81 → 67
```diff
@@ -62,20 +62,6 @@
 movaps xmm1, xmm0
 movss dword ptr [rbx + 0x1b04], xmm1
-mov rdi, rbx
-call F
-mov rdi, rbx
-mov r12, rax
-call F
-cmp r12, rax
-je L
 pop rbx
 pop r12
 pop rbp
 ret
-nop dword ptr [rax]
-movss xmm0, dword ptr [rbx + 0x1b00]
-movss dword ptr [rbx + 0x1af8], xmm0
-pop rbx
-pop r12
-pop rbp
-ret
```

### изменена: 0x49b1da0 (5 байт) C_DOTA_Ability_Furion_ForceOfNature::CastFilterResultLocation
- код тот же, но вызывает другую функцию: было 0x56359a0, стало 0x4f7cc30

### изменена: 0x49b1df0 (5 байт)
- код тот же, но вызывает другую функцию: было 0x56359c0, стало 0x56359e0

### изменена: 0x4a102e0 (6534 байт)
- код тот же, но вызывает другую функцию: было 0x49b1df0, стало 0x49b1e00

### добавлена: 0x4b95910 (108 байт) вызывается из: CDOTA_Modifier_Ogre_Magi_Bloodlust::vfunc#88

### удалена: 0x4a13d80 (3782 байт)

### удалена: 0x4a1efd0 (82 байт) C_DOTA_Ability_Furion_ForceOfNature::CastFilterResultLocation | строки: "area_of_effect"

### копии существующего кода (7): шаблонные / склеенные компоновщиком функции, такой же код есть и в другой сборке — не новый код
- ещё одна копия существующего кода: 0x498bb50 (3 байт) CDOTA_Ability_Dazzle_ThroughTheRealm::vfunc#346
- ещё одна копия существующего кода: 0x49b1e00 (5 байт)
- ещё одна копия существующего кода: 0x49f4ad0 (117 байт) CDOTA_Unit_Hero_Alchemist::vfunc#50
- ещё одна копия существующего кода: 0x4a14160 (6020 байт)
- одной копией существующего кода меньше: 0x49f4090 (92 байт) C_DOTA_Ability_Invoker_Innate_Mastermind::vfunc#50
- одной копией существующего кода меньше: 0x4a14f00 (2420 байт)
- одной копией существующего кода меньше: 0x4b92a50 (31 байт) вызывается из: CDOTA_Modifier_Ogre_Magi_Bloodlust::vfunc#88

## libserver.so: функций 221926 → 221943; без изменений 221574, изменено 334, добавлено 20, удалено 6

### изменена: 0x3bb3ca0 (258 байт) | строки: "@!N"
было: 0x3bb3a20 (258 байт)
- строки: +"@!N"
- инструкций: 86 → 86
```diff
@@ -7,5 +7,5 @@
 mov rbx, rsi
 movsxd rsi, edx
-lea rdx, [D]
+lea rdx, [S:"@!N"]
 sub rsp, 0x18
 movsxd rax, dword ptr [rdx + rdi*4]
```

### изменена: 0x3bbd6a0 (1145 байт) | строки: "<NoAbilityName>"; "AlertSpecialValueFloatIntoInteger"; "false"
было: 0x3bbd420 (1145 байт)
- числа в инструкциях: +0x28e −0x28d
- инструкций: 258 → 258
```diff
@@ -244,5 +244,5 @@
 movq xmm1, rax
 mov rsi, r14
-mov dword ptr [rbp - 0xa8], 0x28d
+mov dword ptr [rbp - 0xa8], 0x28e
 lea rax, [S:"false"]
 punpcklqdq xmm0, xmm1
```

### изменена: 0x3bd91c0 (323 байт) | строки: "xiP"; "CUtlString"; "CUtlVector"
было: 0x3bd8f40 (323 байт)
- строки: +"xiP"
- инструкций: 99 → 99
```diff
@@ -2,5 +2,5 @@
 ja L
 push rbp
-lea rdx, [D]
+lea rdx, [S:"xiP"]
 mov edi, edi
 mov rbp, rsp
```

### изменена: 0x3bf7780 (808 байт) вызывается из: CDOTA_NPCSpawnerGoodTop::vfunc#22, CDOTA_Ability_Lua::GetIntrinsicModifierName, CDOTA_Ability_Lua::GetAssociatedPrimaryAbilities | строки: "%g %g %g"; "%g %g %g %g"; "(null)"; "false"; "true"; "%llu"; "%lld"; "%g %g"
было: 0x3bf7500 (808 байт)
- строки: −"Y;R"
- инструкций: 203 → 203
```diff
@@ -36,5 +36,5 @@
 cmp al, 0x4f
 ja L
-lea rcx, [S:"Y;R"]
+lea rcx, [D]
 movzx edx, al
 movsxd rdx, dword ptr [rcx + rdx*4]
```

### изменена: 0x3bfb030 (317 байт) | строки: "(sR"
было: 0x3bfadb0 (317 байт)
- строки: +"(sR"
- инструкций: 98 → 98
```diff
@@ -7,5 +7,5 @@
 push rbx
 ja L
-lea rdx, [D]
+lea rdx, [S:"(sR"]
 mov edi, edi
 mov rbx, rsi
```

### изменена: 0x3c19b20 (602 байт) | строки: "dGT"; "CGlobalSymbol"; "CAnimGraph2ParamOptionalRef"; "CTransform"
было: 0x3c198a0 (602 байт)
- строки: +"dGT"
- инструкций: 169 → 169
```diff
@@ -9,5 +9,5 @@
 cmp edi, 6
 ja F
-lea rdx, [D]
+lea rdx, [S:"dGT"]
 mov edi, edi
 mov rbx, rsi
```

### изменена: 0x3c27860 (1047 байт) | строки: "Unsupported KV3 basic type '%s' (%d)!"; "Pointers cannot be used as numeric values"
было: 0x3c275e0 (1047 байт)
- строки: −"7#U"
- инструкций: 245 → 245
```diff
@@ -47,5 +47,5 @@
 cmp r8b, 6
 ja L
-lea rcx, [S:"7#U"]
+lea rcx, [D]
 movzx edx, r8b
 movsxd rdx, dword ptr [rcx + rdx*4]
```

### изменена: 0x3c27c80 (1047 байт) | строки: "Unsupported KV3 basic type '%s' (%d)!"; "Pointers cannot be used as numeric values"
было: 0x3c27a00 (1047 байт)
- строки: −";'U"
- инструкций: 245 → 245
```diff
@@ -47,5 +47,5 @@
 cmp r8b, 6
 ja L
-lea rcx, [S:";'U"]
+lea rcx, [D]
 movzx edx, r8b
 movsxd rdx, dword ptr [rcx + rdx*4]
```

### изменена: 0x3c280a0 (1047 байт) | строки: "Unsupported KV3 basic type '%s' (%d)!"; "Pointers cannot be used as numeric values"
было: 0x3c27e20 (1047 байт)
- строки: −"?+U"
- инструкций: 245 → 245
```diff
@@ -47,5 +47,5 @@
 cmp r8b, 6
 ja L
-lea rcx, [S:"?+U"]
+lea rcx, [D]
 movzx edx, r8b
 movsxd rdx, dword ptr [rcx + rdx*4]
```

### изменена: 0x3c284c0 (1047 байт) | строки: "Unsupported KV3 basic type '%s' (%d)!"; "Pointers cannot be used as numeric values"
было: 0x3c28240 (1047 байт)
- строки: −"C/U"
- инструкций: 245 → 245
```diff
@@ -47,5 +47,5 @@
 cmp r8b, 6
 ja L
-lea rcx, [S:"C/U"]
+lea rcx, [D]
 movzx edx, r8b
 movsxd rdx, dword ptr [rcx + rdx*4]
```

### изменена: 0x3c288e0 (1047 байт) | строки: "Unsupported KV3 basic type '%s' (%d)!"; "Pointers cannot be used as numeric values"
было: 0x3c28660 (1047 байт)
- строки: −"G3U"
- инструкций: 245 → 245
```diff
@@ -47,5 +47,5 @@
 cmp r8b, 6
 ja L
-lea rcx, [S:"G3U"]
+lea rcx, [D]
 movzx edx, r8b
 movsxd rdx, dword ptr [rcx + rdx*4]
```

### изменена: 0x3c28d00 (1047 байт) | строки: "Unsupported KV3 basic type '%s' (%d)!"; "Pointers cannot be used as numeric values"
было: 0x3c28a80 (1047 байт)
- строки: −"K7U"
- инструкций: 245 → 245
```diff
@@ -47,5 +47,5 @@
 cmp r8b, 6
 ja L
-lea rcx, [S:"K7U"]
+lea rcx, [D]
 movzx edx, r8b
 movsxd rdx, dword ptr [rcx + rdx*4]
```

### изменена: 0x3c29a80 (1047 байт) | строки: "/EU"; "Unsupported KV3 basic type '%s' (%d)!"; "Pointers cannot be used as numeric values"
было: 0x3c29800 (1047 байт)
- строки: +"/EU"
- инструкций: 245 → 245
```diff
@@ -47,5 +47,5 @@
 cmp r8b, 6
 ja L
-lea rcx, [D]
+lea rcx, [S:"/EU"]
 movzx edx, r8b
 movsxd rdx, dword ptr [rcx + rdx*4]
```

### изменена: 0x3c29ea0 (1047 байт) | строки: "3IU"; "Unsupported KV3 basic type '%s' (%d)!"; "Pointers cannot be used as numeric values"
было: 0x3c29c20 (1047 байт)
- строки: +"3IU"
- инструкций: 245 → 245
```diff
@@ -47,5 +47,5 @@
 cmp r8b, 6
 ja L
-lea rcx, [D]
+lea rcx, [S:"3IU"]
 movzx edx, r8b
 movsxd rdx, dword ptr [rcx + rdx*4]
```

### изменена: 0x3c6a660 (715 байт) CDOTA_NPCSpawnerGoodTop::vfunc#51, CDOTA_NPCSpawnerGoodMid::vfunc#51, CDOTA_NPCSpawnerGoodBot::vfunc#51 | строки: "disableshadows"; "disablereceiveshadows"; "ownername"
было: 0x3c6a3e0 (715 байт)
- строки: −"7-Y" −"O-Y"
- инструкций: 189 → 189
```diff
@@ -25,5 +25,5 @@
 cmp dl, 6
 ja L
-lea rcx, [S:"7-Y"]
+lea rcx, [D]
 movzx edx, dl
 movsxd rdx, dword ptr [rcx + rdx*4]
@@ -126,5 +126,5 @@
 cmp dl, 6
 ja L
-lea rcx, [S:"O-Y"]
+lea rcx, [D]
 movzx edx, dl
 movsxd rdx, dword ptr [rcx + rdx*4]
```

### изменена: 0x3c6d440 (1027 байт) | строки: ",[Y"; "CEntityIOOutput"; "CBaseFilter"; "CHandle"
было: 0x3c6d1c0 (1027 байт)
- строки: +",[Y"
- инструкций: 172 → 172
```diff
@@ -2,5 +2,5 @@
 ja L
 push rbp
-lea rdx, [D]
+lea rdx, [S:",[Y"]
 mov edi, edi
 mov rbp, rsp
```

### изменена: 0x3c7c690 (1801 байт) вызывается из: CPulseInputParameterAdapterWithCPPSignature::vfunc#1, CPulseInputParameterAdapterWithCPPSignature::vfunc#2 | строки: "xNZ"; "CPulseInstanceLoadAPI"; "IKV3TransferInterface_GameTime_Load"; "IKV3TransferInterface_EHandle_Load"; "IKV3TransferInterface_Worldspace_Load"; "CKV3TransferInterface_PulseEnum_Load"
было: 0x3c7c410 (1801 байт)
- строки: +"xNZ"
- инструкций: 406 → 406
```diff
@@ -53,5 +53,5 @@
 cmp edx, 0x14
 ja L
-lea rcx, [D]
+lea rcx, [S:"xNZ"]
 movsxd rdx, dword ptr [rcx + rdx*4]
 add rdx, rcx
```

### изменена: 0x3c8a990 (478 байт)
было: 0x3c8a710 (478 байт)
- строки: −".-["
- инструкций: 116 → 116
```diff
@@ -8,5 +8,5 @@
 cmp dil, 0x4f
 ja L
-lea rdx, [S:".-["]
+lea rdx, [D]
 movzx eax, dil
 movsxd rax, dword ptr [rdx + rax*4]
```

### изменена: 0x3cbc460 (989 байт) | строки: "_Target"; "param"; "M*^"; "%g %g %g"; "(null)"; "%g %g %g %g"; "%lld"; "%llu"
было: 0x3cbc1e0 (989 байт)
- строки: +"M*^"
- инструкций: 228 → 228
```diff
@@ -76,5 +76,5 @@
 cmp al, 0x4f
 ja L
-lea rcx, [D]
+lea rcx, [S:"M*^"]
 movzx edx, al
 movsxd rdx, dword ptr [rcx + rdx*4]
```

### изменена: 0x3cc0310 (2479 байт) CBaseLightProbeVolume::vfunc#2 | строки: "box_mins"; "box_maxs"; "moveable"; "handshake"; "indoor_outdoor_level"; "StartDisabled"; "is_selected_in_hammer"; "voxel_size"
было: 0x3cc0090 (2479 байт)
- строки: +"\\n^" +"2n^" +";n^" +"-n^" −"@n^" −"nm^"
- инструкций: 618 → 618
```diff
@@ -71,5 +71,5 @@
 cmp dl, 6
 ja L
-lea rcx, [S:"@n^"]
+lea rcx, [D]
 movzx edx, dl
 movsxd rdx, dword ptr [rcx + rdx*4]
@@ -202,5 +202,5 @@
 cmp dl, 6
 ja L
-lea rcx, [D]
+lea rcx, [S:"\\n^"]
 movzx edx, dl
 movsxd rdx, dword ptr [rcx + rdx*4]
@@ -231,5 +231,5 @@
 cmp dl, 6
 ja L
-lea rcx, [D]
+lea rcx, [S:"2n^"]
 movzx edx, dl
 movsxd rdx, dword ptr [rcx + rdx*4]
@@ -259,5 +259,5 @@
 cmp dl, 6
 ja L
-lea rcx, [D]
+lea rcx, [S:";n^"]
 movzx edx, dl
 movsxd rdx, dword ptr [rcx + rdx*4]
@@ -287,5 +287,5 @@
 cmp dl, 6
 ja L
-lea rcx, [D]
+lea rcx, [S:"-n^"]
 movzx edx, dl
```
(ещё 8 строк диффа: so-query.py fdiff libserver.so 0x3cc0310)

### изменена: 0x3d00960 (651 байт) | строки: "h7b"; "CUtlVector"; "PointTemplateClientOnlyEntityBehavior_t"; "PointTemplateOwnerSpawnGroupType_t"; "CEntityHandle"; "CEntityOutputTemplate"
было: 0x3d006e0 (651 байт)
- строки: +"h7b"
- инструкций: 181 → 181
```diff
@@ -2,5 +2,5 @@
 ja L
 push rbp
-lea rdx, [D]
+lea rdx, [S:"h7b"]
 mov edi, edi
 mov rbp, rsp
```

### изменена: 0x3d22f20 (1712 байт) CEntityOutputTemplate<SndOpEventGuid_t>::vfunc#2 | строки: "m_Value"; "Stack depth limit hit (%d)"; "0Qd"; "public.aabb_min"; "public.aabb_max"
было: 0x3d22ca0 (1712 байт)
- строки: +"0Qd" −"qPd"
- инструкций: 409 → 409
```diff
@@ -65,5 +65,5 @@
 cmp al, 6
 ja L
-lea rdx, [D]
+lea rdx, [S:"0Qd"]
 movzx eax, al
 movsxd rax, dword ptr [rdx + rax*4]
@@ -90,5 +90,5 @@
 cmp al, 6
 ja L
-lea rdx, [S:"qPd"]
+lea rdx, [D]
 movzx eax, al
 movsxd rax, dword ptr [rdx + rax*4]
```

### изменена: 0x3d309e0 (547 байт) | строки: "CHandle"; "CBasePlayerController"; "CNetworkUtlVectorBase"; "CBasePlayerPawn"
было: 0x3d30760 (547 байт)
- строки: −"x'e"
- инструкций: 158 → 158
```diff
@@ -2,5 +2,5 @@
 ja L
 push rbp
-lea rdx, [S:"x'e"]
+lea rdx, [D]
 mov edi, edi
 mov rbp, rsp
```

### изменена: 0x3d33bd0 (270 байт) | строки: "nZe"
было: 0x3d33950 (270 байт)
- строки: +"nZe"
- инструкций: 69 → 69
```diff
@@ -5,5 +5,5 @@
 cmp edi, 6
 ja L
-lea rdx, [D]
+lea rdx, [S:"nZe"]
 mov edi, edi
 mov rbx, rsi
```

### изменена: 0x3d51b50 (183 байт) | строки: "' g"
было: 0x3d518d0 (183 байт)
- строки: +"' g"
- инструкций: 55 → 55
```diff
@@ -2,5 +2,5 @@
 ja L
 push rbp
-lea rdx, [D]
+lea rdx, [S:"' g"]
 mov edi, edi
 mov rbp, rsp
```

### изменена: 0x3d51c80 (117 байт)
было: 0x3d51a00 (117 байт)
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

### изменена: 0x3d51d00 (561 байт) | строки: "#!g"; "Unsupported KV3 basic type '%s' (%d)!"; "Pointers cannot be used as numeric values"
было: 0x3d51a80 (561 байт)
- строки: +"#!g"
- инструкций: 151 → 151
```diff
@@ -11,5 +11,5 @@
 cmp r8b, 6
 ja L
-lea rdx, [D]
+lea rdx, [S:"#!g"]
 movzx eax, r8b
 movsxd rax, dword ptr [rdx + rax*4]
```

### изменена: 0x3d52700 (190 байт) | строки: "O+g"
было: 0x3d52480 (190 байт)
- строки: +"O+g"
- инструкций: 59 → 59
```diff
@@ -3,5 +3,5 @@
 ja L
 push rbp
-lea rcx, [D]
+lea rcx, [S:"O+g"]
 mov rbp, rsp
 sub rsp, 0x10
```

### изменена: 0x3d52900 (206 байт) | строки: "C-g"
было: 0x3d52680 (206 байт)
- строки: +"C-g"
- инструкций: 55 → 55
```diff
@@ -1,5 +1,5 @@
 cmp edi, 6
 ja L
-lea rcx, [D]
+lea rcx, [S:"C-g"]
 mov edi, edi
 push rbp
```

### изменена: 0x3d52b20 (339 байт) | строки: "VPhysicsCollisionAttribute_t"; "SolidType_t"; "SurroundingBoundsType_t"
было: 0x3d528a0 (339 байт)
- строки: −"D.g"
- инструкций: 99 → 99
```diff
@@ -2,5 +2,5 @@
 ja L
 push rbp
-lea rdx, [S:"D.g"]
+lea rdx, [D]
 mov edi, edi
 mov rbp, rsp
```

### изменена: 0x3d52d40 (499 байт) | строки: "GameTime_t"; "BeamType_t"; "CBaseEntity"; "CHandle"; "AttachmentHandle_t"; "VectorWS"
было: 0x3d52ac0 (499 байт)
- строки: −"P0g"
- инструкций: 135 → 135
```diff
@@ -2,5 +2,5 @@
 ja L
 push rbp
-lea rdx, [S:"P0g"]
+lea rdx, [D]
 mov edi, edi
 mov rbp, rsp
```

### изменена: 0x3d62300 (785 байт) | строки: "R(h"; "Unsupported KV3 basic type '%s' (%d)!"; "Pointers cannot be used as numeric values"
было: 0x3d62080 (785 байт)
- строки: +"R(h" −"Z%h"
- инструкций: 219 → 219
```diff
@@ -20,5 +20,5 @@
 cmp bl, 6
 ja L
-lea rdx, [S:"Z%h"]
+lea rdx, [D]
 movzx eax, bl
 movsxd rax, dword ptr [rdx + rax*4]
@@ -31,5 +31,5 @@
 cmp bl, 6
 ja L
-lea rdx, [D]
+lea rdx, [S:"R(h"]
 movzx eax, bl
 movsxd rax, dword ptr [rdx + rax*4]
```

### изменена: 0x3d85390 (243 байт) | строки: "VectorWS"
было: 0x3d85110 (243 байт)
- строки: −"h1j"
- инструкций: 67 → 67
```diff
@@ -1,5 +1,5 @@
 cmp edi, 6
 ja L
-lea rdx, [S:"h1j"]
+lea rdx, [D]
 mov edi, edi
 push rbp
```

### изменена: 0x3d85490 (227 байт) | строки: "VectorWS"
было: 0x3d85210 (227 байт)
- строки: −"T2j"
- инструкций: 74 → 74
```diff
@@ -1,5 +1,5 @@
 cmp edi, 6
 ja L
-lea rcx, [S:"T2j"]
+lea rcx, [D]
 mov edi, edi
 push rbp
```

### изменена: 0x3d85580 (339 байт) | строки: "BASEPTR"; "GameTick_t"
было: 0x3d85300 (339 байт)
- строки: −"(3j"
- инструкций: 90 → 90
```diff
@@ -1,5 +1,5 @@
 cmp edi, 6
 ja L
-lea rdx, [S:"(3j"]
+lea rdx, [D]
 mov edi, edi
 push rbp
```

### изменена: 0x3d85ef0 (243 байт) | строки: "VectorWS"
было: 0x3d85c70 (243 байт)
- строки: −"|<j"
- инструкций: 76 → 76
```diff
@@ -2,5 +2,5 @@
 ja L
 push rbp
-lea rdx, [S:"|<j"]
+lea rdx, [D]
 mov edi, edi
 mov rbp, rsp
```

### изменена: 0x3d86180 (307 байт) | строки: "x?j"; "VectorWS"
было: 0x3d85f00 (307 байт)
- строки: +"x?j"
- инструкций: 94 → 94
```diff
@@ -2,5 +2,5 @@
 ja L
 push rbp
-lea rdx, [D]
+lea rdx, [S:"x?j"]
 mov edi, edi
 mov rbp, rsp
```

### изменена: 0x3d86300 (371 байт) | строки: "GameTime_t"; "CBaseEntity"; "CHandle"
было: 0x3d86080 (371 байт)
- строки: −"\\@j"
- инструкций: 112 → 112
```diff
@@ -2,5 +2,5 @@
 ja L
 push rbp
-lea rdx, [S:"\\@j"]
+lea rdx, [D]
 mov edi, edi
 mov rbp, rsp
```

### изменена: 0x3d86900 (183 байт) | строки: "#Gj"
было: 0x3d86680 (183 байт)
- строки: +"#Gj"
- инструкций: 55 → 55
```diff
@@ -2,5 +2,5 @@
 ja L
 push rbp
-lea rdx, [D]
+lea rdx, [S:"#Gj"]
 mov edi, edi
 mov rbp, rsp
```

### изменена: 0x3d86a30 (98 байт)
было: 0x3d867b0 (98 байт)
- строки: −"bGj"
- инструкций: 36 → 36
```diff
@@ -2,5 +2,5 @@
 cmp edx, 6
 ja L
-lea rcx, [S:"bGj"]
+lea rcx, [D]
 push rbp
 mov rdi, rsi
```

### изменена: 0x3d86aa0 (98 байт) | строки: "6Hj"
было: 0x3d86820 (98 байт)
- строки: +"6Hj"
- инструкций: 36 → 36
```diff
@@ -2,5 +2,5 @@
 cmp edx, 6
 ja L
-lea rcx, [D]
+lea rcx, [S:"6Hj"]
 push rbp
 mov rdi, rsi
```

### изменена: 0x3d86ba0 (176 байт) | строки: "hIj"
было: 0x3d86920 (176 байт)
- строки: +"hIj"
- инструкций: 45 → 45
```diff
@@ -1,5 +1,5 @@
 cmp edi, 6
 ja L
-lea rcx, [D]
+lea rcx, [S:"hIj"]
 mov edi, edi
 push rbp
```

### изменена: 0x3d86c80 (117 байт)
было: 0x3d86a00 (117 байт)
- строки: −"qIj"
- инструкций: 39 → 39
```diff
@@ -2,5 +2,5 @@
 cmp edx, 6
 ja L
-lea rcx, [S:"qIj"]
+lea rcx, [D]
 push rbp
 mov rdi, rsi
```

### изменена: 0x3d86ed0 (136 байт) | строки: "8Lj"
было: 0x3d86c50 (136 байт)
- строки: +"8Lj"
- инструкций: 43 → 43
```diff
@@ -2,5 +2,5 @@
 cmp edx, 6
 ja L
-lea rcx, [D]
+lea rcx, [S:"8Lj"]
 push rbp
 mov rax, rsi
```

### изменена: 0x3d87f30 (206 байт)
было: 0x3d87cb0 (206 байт)
- строки: −"?\\j"
- инструкций: 62 → 62
```diff
@@ -2,5 +2,5 @@
 ja L
 push rbp
-lea rdx, [S:"?\\j"]
+lea rdx, [D]
 mov edi, edi
 mov rbp, rsp
```

### изменена: 0x3d88000 (206 байт) | строки: "s]j"
было: 0x3d87d80 (206 байт)
- строки: +"s]j"
- инструкций: 62 → 62
```diff
@@ -2,5 +2,5 @@
 ja L
 push rbp
-lea rdx, [D]
+lea rdx, [S:"s]j"]
 mov edi, edi
 mov rbp, rsp
```

### изменена: 0x3d88340 (222 байт)
было: 0x3d880c0 (222 байт)
- строки: −"'`j"
- инструкций: 64 → 64
```diff
@@ -2,5 +2,5 @@
 ja L
 push rbp
-lea rdx, [S:"'`j"]
+lea rdx, [D]
 mov edi, edi
 mov rbp, rsp
```

### изменена: 0x3d88520 (435 байт) | строки: "CTransform"; "CNetworkUtlVectorBase"
было: 0x3d882a0 (435 байт)
- строки: −"Xaj"
- инструкций: 118 → 118
```diff
@@ -1,5 +1,5 @@
 cmp edi, 6
 ja L
-lea rdx, [S:"Xaj"]
+lea rdx, [D]
 mov edi, edi
 push rbp
```

### изменена: 0x3d88790 (302 байт)
было: 0x3d88510 (302 байт)
- строки: −"sdj"
- инструкций: 71 → 71
```diff
@@ -2,5 +2,5 @@
 ja L
 push rbp
-lea rdx, [S:"sdj"]
+lea rdx, [D]
 mov edi, edi
 mov rbp, rsp
```

### изменена: 0x3d88c60 (811 байт)
было: 0x3d889e0 (811 байт)
- строки: −"Xhj"
- инструкций: 232 → 232
```diff
@@ -9,5 +9,5 @@
 movsxd r13, edx
 push r12
-lea rdx, [S:"Xhj"]
+lea rdx, [D]
 mov r12d, ecx
 push rbx
```

### изменена: 0x3d89e10 (435 байт) | строки: " zj"; "CPlayerSlot"; "CUtlVector"
было: 0x3d89b90 (435 байт)
- строки: +" zj"
- инструкций: 115 → 115
```diff
@@ -1,5 +1,5 @@
 cmp edi, 6
 ja L
-lea rdx, [D]
+lea rdx, [S:" zj"]
 mov edi, edi
 push rbp
```

### изменена: 0x3d95770 (659 байт) | строки: "42k"; "CTakeDamageInfo"; "DestructiblePartDamageRequest_t"; "CUtlLeanVector"; "VectorWS"; "TakeDamageFlags_t"; "HitGroup_t"
было: 0x3d954f0 (659 байт)
- строки: +"42k"
- инструкций: 151 → 151
```diff
@@ -1,5 +1,5 @@
 cmp edi, 6
 ja L
-lea rdx, [D]
+lea rdx, [S:"42k"]
 mov edi, edi
 push rbp
```

### изменена: 0x3d95a10 (659 байт) | строки: "CTakeDamageInfo"; "CTakeDamageResult"
было: 0x3d95790 (659 байт)
- строки: −"84k"
- инструкций: 126 → 126
```diff
@@ -2,5 +2,5 @@
 ja L
 push rbp
-lea rdx, [S:"84k"]
+lea rdx, [D]
 mov edi, edi
 mov rbp, rsp
```

### изменена: 0x3d96040 (563 байт) | строки: "CUtlVector"; "VectorWS"; "GameTime_t"
было: 0x3d95dc0 (563 байт)
- строки: −"H:k"
- инструкций: 157 → 157
```diff
@@ -2,5 +2,5 @@
 ja L
 push rbp
-lea rdx, [S:"H:k"]
+lea rdx, [D]
 mov edi, edi
 mov rbp, rsp
```

### изменена: 0x3d98f90 (4083 байт) вызывается из: CTakeDamageInfo::vfunc#2 | строки: "m_vecDamageForce"; "m_bitsDamageType"; "m_vecDamagePosition"; "m_vecReportedPosition"; "m_vecDamageDirection"; "m_hInflictor"; "m_hAttacker"; "m_hAbility"
было: 0x3d98d10 (4083 байт)
- строки: −"+mk" −"6wk"
- инструкций: 886 → 886
```diff
@@ -113,5 +113,5 @@
 cmp r8b, 6
 ja L
-lea rdx, [S:"+mk"]
+lea rdx, [D]
 movzx eax, r8b
 movsxd rax, dword ptr [rdx + rax*4]
@@ -362,5 +362,5 @@
 cmp r8b, 6
 ja L
-lea rdx, [S:"6wk"]
+lea rdx, [D]
 movzx eax, r8b
 movsxd rax, dword ptr [rdx + rax*4]
```

### изменена: 0x3da4c40 (414 байт)
было: 0x3da49c0 (414 байт)
- строки: −"P%l"
- инструкций: 136 → 136
```diff
@@ -8,5 +8,5 @@
 movsxd r12, edx
 push rbx
-lea rdx, [S:"P%l"]
+lea rdx, [D]
 mov rbx, rsi
 sub rsp, 0x18
```

### изменена: 0x3da4f00 (766 байт) | строки: "t(l"
было: 0x3da4c80 (766 байт)
- строки: +"t(l"
- инструкций: 201 → 201
```diff
@@ -9,5 +9,5 @@
 movsxd r12, edx
 push rbx
-lea rdx, [D]
+lea rdx, [S:"t(l"]
 mov rbx, rsi
 sub rsp, 0x10
```

### изменена: 0x3da5860 (542 байт)
было: 0x3da55e0 (542 байт)
- строки: −"01l"
- инструкций: 159 → 159
```diff
@@ -9,5 +9,5 @@
 movsxd r12, edx
 push rbx
-lea rdx, [S:"01l"]
+lea rdx, [D]
 mov rbx, rsi
 sub rsp, 0x10
```

### изменена: 0x3daaab0 (961 байт) | строки: "%g %g %g"; "(null)"; "%g %g %g %g"; "unknown_variant_type"; "%lld"; "%llu"; "%d %d %d %d"; "false"
было: 0x3daa830 (961 байт)
- строки: −"Byl" −"qyl"
- инструкций: 213 → 213
```diff
@@ -7,5 +7,5 @@
 cmp al, 0x4f
 ja L
-lea rcx, [S:"Byl"]
+lea rcx, [D]
 movzx edx, al
 movsxd rdx, dword ptr [rcx + rdx*4]
@@ -91,5 +91,5 @@
 cmp al, 0x47
 ja L
-lea rdx, [S:"qyl"]
+lea rdx, [D]
 movzx eax, al
 movsxd rax, dword ptr [rdx + rax*4]
```

### изменена: 0x3db86f0 (851 байт) | строки: "%llu"
было: 0x3db8470 (851 байт)
- строки: −"|Tm"
- инструкций: 190 → 190
```diff
@@ -21,5 +21,5 @@
 mov rbx, rax
 je L
-lea r13, [S:"|Tm"]
+lea r13, [D]
 nop dword ptr [rax + rax]
 mov qword ptr [rbp - 0xc0], 0
```

### изменена: 0x3db8f00 (819 байт) | строки: "DecalFlags_t"; "GameTime_t"
было: 0x3db8c80 (819 байт)
- строки: −"$Zm"
- инструкций: 143 → 143
```diff
@@ -2,5 +2,5 @@
 ja L
 push rbp
-lea rdx, [S:"$Zm"]
+lea rdx, [D]
 mov edi, edi
 mov rbp, rsp
```

### изменена: 0x3df7ae0 (350 байт)
было: 0x3df7860 (350 байт)
- строки: −"_-q"
- инструкций: 92 → 92
```diff
@@ -2,5 +2,5 @@
 ja L
 push rbp
-lea rdx, [S:"_-q"]
+lea rdx, [D]
 mov edi, edi
 mov rbp, rsp
```

### изменена: 0x3df9960 (547 байт) | строки: "(Kq"; "CHandle"; "CEnvSoundscapeTriggerable"; "CBasePlayerPawn"; "CUtlVector"
было: 0x3df96e0 (547 байт)
- строки: +"(Kq"
- инструкций: 144 → 144
```diff
@@ -2,5 +2,5 @@
 ja L
 push rbp
-lea rdx, [D]
+lea rdx, [S:"(Kq"]
 mov edi, edi
 mov rbp, rsp
```

### изменена: 0x3dfc410 (502 байт)
было: 0x3dfc190 (502 байт)
- строки: −"4uq"
- инструкций: 139 → 139
```diff
@@ -21,5 +21,5 @@
 cmp al, 0x24
 ja L
-lea rcx, [S:"4uq"]
+lea rcx, [D]
 movzx eax, al
 movsxd rax, dword ptr [rcx + rax*4]
```

### изменена: 0x3e1ac40 (4702 байт) | строки: "classname"; "connections"; "attributes"
было: 0x3e1a9c0 (4702 байт)
- строки: −"X\\s"
- инструкций: 1086 → 1086
```diff
@@ -747,5 +747,5 @@
 cmp al, 0x4f
 ja L
-lea rsi, [S:"X\\s"]
+lea rsi, [D]
 movzx edx, al
 movsxd rdx, dword ptr [rsi + rdx*4]
```

### изменена: 0x3e2bc20 (542 байт)
было: 0x3e2b9a0 (542 байт)
- строки: −"D[t"
- инструкций: 159 → 159
```diff
@@ -9,5 +9,5 @@
 movsxd r12, edx
 push rbx
-lea rdx, [S:"D[t"]
+lea rdx, [D]
 mov rbx, rsi
 sub rsp, 0x10
```

### изменена: 0x3e4b3b0 (2071 байт) вызывается из: CWorldGameSystem::vfunc#15 | строки: "_dotatilegrid_minheight"; "_dotatilegrid_maxheight"; "rZv"; "_dotatilegrid_stepheight"; "nZv"
было: 0x3e4b130 (2071 байт)
- строки: +"rZv" +"nZv"
- инструкций: 485 → 485
```diff
@@ -62,5 +62,5 @@
 cmp al, 6
 ja L
-lea rdx, [D]
+lea rdx, [S:"rZv"]
 movzx eax, al
 movsxd rax, dword ptr [rdx + rax*4]
@@ -96,5 +96,5 @@
 cmp al, 6
 ja L
-lea rdx, [D]
+lea rdx, [S:"nZv"]
 movzx eax, al
 movsxd rax, dword ptr [rdx + rax*4]
```

### изменена: 0x3e4c200 (2322 байт) CWorldGameSystem::vfunc#15 | строки: "maxpropscreenwidth"; "minpropscreenwidth"; "newunit"; "startdark"; "startcolor"; "update_nav_obstacle_splits_only_on_final_tick"; "_dotatilegrid_heightshift"; "\\iv"
было: 0x3e4bf80 (2322 байт)
- строки: +"\\iv"
- инструкций: 567 → 567
```diff
@@ -187,5 +187,5 @@
 cmp al, 6
 ja L
-lea rdx, [D]
+lea rdx, [S:"\\iv"]
 movzx eax, al
 movsxd rax, dword ptr [rdx + rax*4]
```

### изменена: 0x3e6cda0 (211 байт) | строки: "dYx"; "GameTime_t"
было: 0x3e6cb20 (211 байт)
- строки: +"dYx"
- инструкций: 63 → 63
```diff
@@ -1,5 +1,5 @@
 cmp edi, 6
 ja L
-lea rdx, [D]
+lea rdx, [S:"dYx"]
 mov edi, edi
 push rbp
```

### изменена: 0x3e6ce80 (187 байт) | строки: "(Zx"; "Disposition_t"
было: 0x3e6cc00 (187 байт)
- строки: +"(Zx"
- инструкций: 59 → 59
```diff
@@ -1,5 +1,5 @@
 cmp edi, 6
 ja L
-lea rdx, [D]
+lea rdx, [S:"(Zx"]
 mov edi, edi
 push rbp
```

### изменена: 0x3e6d230 (243 байт) | строки: "VectorWS"
было: 0x3e6cfb0 (243 байт)
- строки: −" ]x"
- инструкций: 70 → 70
```diff
@@ -1,5 +1,5 @@
 cmp edi, 6
 ja L
-lea rdx, [S:" ]x"]
+lea rdx, [D]
 mov edi, edi
 push rbp
```

### изменена: 0x3e6dc80 (451 байт) | строки: "CEconWearable"; "CHandle"; "CNetworkUtlVectorBase"; "RelationshipOverride_t"; "CUtlVector"; "Hull_t"; "CMovementStatsProperty"
было: 0x3e6da00 (451 байт)
- строки: −"dgx"
- инструкций: 129 → 129
```diff
@@ -2,5 +2,5 @@
 ja L
 push rbp
-lea rdx, [S:"dgx"]
+lea rdx, [D]
 mov edi, edi
 mov rbp, rsp
```

### изменена: 0x3e6f2b0 (187 байт)
было: 0x3e6f030 (187 байт)
- строки: −"S}x"
- инструкций: 52 → 52
```diff
@@ -3,5 +3,5 @@
 ja L
 push rbp
-lea rcx, [S:"S}x"]
+lea rcx, [D]
 mov rdi, rsi
 mov rbp, rsp
```

### изменена: 0x3e6f420 (133 байт)
было: 0x3e6f1a0 (133 байт)
- строки: −"U~x"
- инструкций: 41 → 41
```diff
@@ -2,5 +2,5 @@
 cmp edx, 6
 ja L
-lea rcx, [S:"U~x"]
+lea rcx, [D]
 push rbp
 mov rdi, rsi
```

### изменена: 0x3e7b9f0 (436 байт) | строки: "y?y"
было: 0x3e7b770 (436 байт)
- строки: +"y?y"
- инструкций: 100 → 100
```diff
@@ -5,5 +5,5 @@
 cmp edi, 6
 ja L
-lea rdx, [D]
+lea rdx, [S:"y?y"]
 mov edi, edi
 mov rbx, rsi
```

### изменена: 0x3eaa760 (769 байт) вызывается из: CAnimGraphControllerBase::vfunc#2, CEmptyGraphController::vfunc#2, EventGrantDefinition_Emoticon_t::vfunc#2 | строки: "z+|"; "Unsupported KV3 basic type '%s' (%d)!"; "Pointers cannot be used as numeric values"
было: 0x3eaa4e0 (769 байт)
- строки: +"z+|" −"b-|"
- инструкций: 220 → 220
```diff
@@ -20,5 +20,5 @@
 cmp bl, 6
 ja L
-lea rdx, [D]
+lea rdx, [S:"z+|"]
 movzx eax, bl
 movsxd rax, dword ptr [rdx + rax*4]
@@ -31,5 +31,5 @@
 cmp bl, 6
 ja L
-lea rdx, [S:"b-|"]
+lea rdx, [D]
 movzx eax, bl
 movsxd rax, dword ptr [rdx + rax*4]
```

### изменена: 0x3eacd70 (856 байт) | строки: "<Q|"
было: 0x3eace50 (856 байт)
- строки: +"<Q|"
- инструкций: 221 → 221
```diff
@@ -10,5 +10,5 @@
 movsxd r12, edx
 push rbx
-lea rdx, [D]
+lea rdx, [S:"<Q|"]
 mov rbx, rsi
 sub rsp, 0x58
```

### изменена: 0x3eca6a0 (904 байт)
было: 0x3eca420 (904 байт)
- строки: −"()~"
- инструкций: 238 → 238
```diff
@@ -7,5 +7,5 @@
 mov r15d, edx
 push r14
-lea rdx, [S:"()~"]
+lea rdx, [D]
 push r13
 push r12
```

### изменена: 0x445a320 (251 байт) CDOTA_Modifier_Morphling_Replicate_Echo::vfunc#97
было: 0x445a0a0 (176 байт)
- числа в инструкциях: +0 +0 +0
- поля объектов: +0x1960 +0x1150 +0x1968 +0x1158 +0x1160 +0x1168
- цели вызовов: +0x44a83a0 +0x44be040 "<NoAbilityName>" +0x44a4140 "tusk_snowball"; "snowball_windup" +0x4485390
- инструкций: 22 → 31
```diff
@@ -13,4 +13,10 @@
 mov qword ptr [rdi + 0xd20], rax
 lea rax, [T]
+mov qword ptr [rdi + 0xe20], rax
+lea rax, [T]
+mov qword ptr [rdi + 0x1960], rax
+lea rax, [T]
+mov qword ptr [rdi + 0x1150], rax
+lea rax, [T]
 mov qword ptr [rdi + 0xbb8], 0
 mov qword ptr [rdi + 0x3c8], 0
@@ -18,5 +24,8 @@
 mov qword ptr [rdi + 0x558], 0
 mov qword ptr [rdi + 0xd28], 0
-mov qword ptr [rdi + 0xe20], rax
 mov qword ptr [rdi + 0xe28], 0
+mov qword ptr [rdi + 0x1968], 0
+mov qword ptr [rdi + 0x1158], 0
+mov qword ptr [rdi + 0x1160], rax
+mov qword ptr [rdi + 0x1168], 0
 ret
```

### изменена: 0x445a450 (39 байт) вызывается из: CDOTA_Modifier_Morphling_Replicate_Echo::vfunc#97
было: 0x445a180 (39 байт)
- поля объектов: +0x1b30 −0x1b14
- инструкций: 8 → 8
```diff
@@ -1,3 +1,3 @@
-movss xmm0, dword ptr [rsi + 0x1b14]
+movss xmm0, dword ptr [rsi + 0x1b30]
 mov rax, rdi
 mov dword ptr [rdi], 1
```

### изменена: 0x4486740 (39 байт) вызывается из: CDOTA_Modifier_Morphling_Replicate_Echo::vfunc#97
было: 0x44864e0 (39 байт)
- поля объектов: +0x1b30 −0x1b14
- инструкций: 8 → 8
```diff
@@ -1,3 +1,3 @@
-movss xmm0, dword ptr [rsi + 0x1b14]
+movss xmm0, dword ptr [rsi + 0x1b30]
 mov rax, rdi
 mov dword ptr [rdi], 1
```

### изменена: 0x4486770 (39 байт) вызывается из: CDOTA_Modifier_Morphling_Replicate_Echo::vfunc#97
было: 0x4486510 (39 байт)
- поля объектов: +0x1b30 −0x1b14
- инструкций: 8 → 8
```diff
@@ -1,3 +1,3 @@
-movss xmm0, dword ptr [rsi + 0x1b14]
+movss xmm0, dword ptr [rsi + 0x1b30]
 mov rax, rdi
 mov dword ptr [rdi], 1
```

### изменена: 0x449c030 (146 байт) CModifierFactory<CDOTA_Modifier_Morphling_Replicate_Echo>::vfunc#0
было: 0x449c290 (116 байт)
- числа в инструкциях: +0x1b38 +0x1b38 +0 +0 −0x1b20 −0x1b20
- поля объектов: +0x1b18 +0x1b20 +0x1b28
- инструкций: 26 → 29
```diff
@@ -1,9 +1,9 @@
 push rbp
-mov edi, 0x1b20
+mov edi, 0x1b38
 mov rbp, rsp
 push rbx
 sub rsp, 0x18
 call F
-mov edx, 0x1b20
+mov edx, 0x1b38
 xor esi, esi
 mov rdi, rax
@@ -20,6 +20,9 @@
 movabs rax, 0xffffffff00000000
 mov qword ptr [rbx + 0x1b08], rax
+mov qword ptr [rbx + 0x1b10], rax
 mov rax, rbx
-mov dword ptr [rbx + 0x1b10], 0
+mov qword ptr [rbx + 0x1b18], 0
+mov qword ptr [rbx + 0x1b20], 0
+mov qword ptr [rbx + 0x1b28], 0
 mov rbx, qword ptr [rbp - 8]
 leave
```

### изменена: 0x44b6c70 (394 байт) вызывается из: CDOTA_Modifier_Drow_Ranger_Multishot::vfunc#97 | строки: "drow_ranger_glacier"
было: 0x44b6540 (635 байт)
- строки: +"drow_ranger_glacier" −"bane_daunting_presence"
- числа в инструкциях: +3 +0x15 +4 +0x1a +0xa −-1 −-1 −-2 −-2 −9 −0x3f −0x3f −0x1ff (и ещё 4)
- виртуальные вызовы: +0x840 (слот 264)
- поля объектов: +0x5d1 +0x50 −0x10 −0x10 −0xd8 −0xd8 −0xd8 −0xd8 −0xcc −0xcc −0x840 −0x59
- прямых вызовов: 7 → 4
- цели вызовов: −0x5040ef0 −0x5090110
- инструкций: 159 → 113
```diff
@@ -3,32 +3,35 @@
 push r14
 push r13
-mov r13, rdx
 push r12
-mov r12, rsi
 push rbx
-mov edx, dword ptr [rdx + 0xd4]
+mov ecx, dword ptr [rdx + 0xd4]
 mov rbx, rdi
-cmp edx, -1
+cmp ecx, -1
 je L
+mov r13, rsi
 mov rsi, qword ptr [D]
 test rsi, rsi
 je L
-cmp edx, -2
+cmp ecx, -2
 je L
-movzx eax, word ptr [r13 + 0xd4]
-mov rcx, rax
-shr rcx, 9
-and ecx, 0x3f
-mov r14, qword ptr [rsi + rcx*8]
-test r14, r14
+movzx eax, word ptr [rdx + 0xd4]
+mov r12, rdx
+mov rdx, rax
+shr rdx, 9
+and edx, 0x3f
+mov rdx, qword ptr [rsi + rdx*8]
+test rdx, rdx
 je L
```
(ещё 153 строк диффа: so-query.py fdiff libserver.so 0x44b6c70)

### изменена: 0x44ba780 (559 байт) CDOTA_Modifier_Morphling_Replicate_Echo::OnCreated | строки: "scepter_echo_visible_duration"; "echo_power"; "echo_fire_delay"; "echo_target"; "echo_ability"
было: 0x44b9ec0 (559 байт)
- поля объектов: +0x1b34 +0x1b30 +0x1b30 −0x1b18 −0x1b14 −0x1b14
- инструкций: 137 → 137
```diff
@@ -21,6 +21,6 @@
 movaps xmm1, xmm0
 test r12, r12
-movss dword ptr [rbx + 0x1b18], xmm1
-mov dword ptr [rbx + 0x1b14], 0
+movss dword ptr [rbx + 0x1b34], xmm1
+mov dword ptr [rbx + 0x1b30], 0
 je L
 lea rsi, [S:"echo_power"]
@@ -32,5 +32,5 @@
 je L
 call F
-movss dword ptr [rbx + 0x1b14], xmm0
+movss dword ptr [rbx + 0x1b30], xmm0
 lea rsi, [S:"echo_fire_delay"]
 xor edx, edx
```

### изменена: 0x44be570 (99 байт) вызывается из: CDOTA_Modifier_DrowRanger_Marksmanship::vfunc#132, CDOTA_Modifier_Tiny_CraggyExterior::vfunc#128, CDOTA_Modifier_Windrunner_TailwindIntrinsic::vfunc#128
было: 0x44bd950 (211 байт)
- числа в инструкциях: −9 −9 −9 −0x12 −0x12 −0x12 −0xff
- поля объектов: −0x10
- прямых вызовов: 1 → 0
- цели вызовов: −0x3c75e80
- инструкций: 64 → 30
```diff
@@ -1,36 +1,2 @@
-push rbp
-mov rbp, rsp
-sub rsp, 0x20
-call F
-movaps xmm0, xmmword ptr [rax + 0x10]
-lea rax, [D]
-movaps xmm4, xmm0
-movaps xmm5, xmm0
-shufps xmm4, xmm0, 9
-shufps xmm5, xmm0, 0x12
-shufps xmm0, xmm0, 0xff
-movaps xmm3, xmmword ptr [rax]
-leave
-movaps xmm2, xmm3
-movaps xmm1, xmm3
-shufps xmm2, xmm3, 0x12
-shufps xmm1, xmm3, 9
-mulps xmm2, xmm4
-mulps xmm1, xmm5
-subps xmm2, xmm1
-addps xmm2, xmm2
-mulps xmm0, xmm2
-movaps xmm1, xmm2
-shufps xmm1, xmm2, 0x12
-mulps xmm1, xmm4
-movaps xmm4, xmm2
-shufps xmm4, xmm2, 9
-mulps xmm4, xmm5
-addps xmm0, xmm3
-subps xmm1, xmm4
-addps xmm1, xmm0
-movdqa xmm0, xmm1
-unpckhps xmm1, xmm1
```
(ещё 3 строк диффа: so-query.py fdiff libserver.so 0x44be570)

### изменена: 0x44ddd80 (4662 байт) | строки: "<NoAbilityName>"
было: 0x44dd1c0 (4483 байт)
- строки: +"<NoAbilityName>"
- числа в инструкциях: +8 +8 +1
- поля объектов: +0x840
- прямых вызовов: 46 → 48
- инструкций: 723 → 771
```diff
@@ -678,4 +678,6 @@
 mov rdi, rsi
 mov rbp, rsp
+push r13
+push r12
 push rbx
 mov rbx, rsi
@@ -700,21 +702,67 @@
 mov eax, dword ptr [rax + 0x54]
 cmp eax, 1
-mov rbx, qword ptr [rbp - 8]
-leave
-setne al
-ret
+je L
+mov rax, qword ptr [rbx + 0x840]
+lea rbx, [D]
+lea r13, [rbx + 0x88]
+test rax, rax
+je L
+mov r12, qword ptr [rax]
+lea rax, [D]
+test r12, r12
+cmove r12, rax
+jmp L
+nop dword ptr [rax]
+test rsi, rsi
+je L
+mov rdi, r12
+call F
+test eax, eax
+je L
+add rbx, 8
+cmp rbx, r13
```
(ещё 57 строк диффа: so-query.py fdiff libserver.so 0x44ddd80)

### изменена: 0x44df160 (880 байт) вызывается из: CDOTA_Modifier_Morphling_Replicate_Echo::OnIntervalThink
было: 0x44de4f0 (864 байт)
- числа в инструкциях: +1 +0
- поля объектов: +0x858 +0x858
- инструкций: 218 → 220
```diff
@@ -118,4 +118,5 @@
 call F
 mov rdi, r12
+mov byte ptr [rbx + 0x858], 1
 call F
 mov rdi, r12
@@ -131,4 +132,5 @@
 call F
 cmp byte ptr [rbx + 0x788], 0
+mov byte ptr [rbx + 0x858], 0
 je L
 mov rax, qword ptr [rbx]
@@ -151,5 +153,5 @@
 call F
 jmp L
-nop dword ptr [rax]
+nop
 mov ecx, dword ptr [r12 + 0x1afc]
 cmp ecx, -1
@@ -180,5 +182,5 @@
 xor r14d, r14d
 jmp L
-nop
+nop word ptr [rax + rax]
 mov ecx, dword ptr [r12 + 0x1afc]
 cmp ecx, -1
```

### изменена: 0x44df4d0 (700 байт) CDOTA_Modifier_Morphling_Replicate_Echo::OnIntervalThink | строки: "modifier_item_lotus_orb_channel_check"; "modifier_death_seeker_out_of_world"; "modifier_hoodwink_arcing_boomerang"; "modifier_marci_lunge_tracking_motion"; "modifier_marci_lunge_arc"; "modifier_grimstroke_spirit_walk_buff"; "modifier_tusk_snowball_movement"; "modifier_illusion"
было: 0x44de850 (198 байт)
- строки: +"modifier_death_seeker_out_of_world" +"modifier_hoodwink_arcing_boomerang" +"modifier_marci_lunge_tracking_motion" +"modifier_marci_lunge_arc" +"modifier_grimstroke_spirit_walk_buff" +"modifier_tusk_snowball_movement" +"modifier_illusion"
- константы из данных (числа логики): +0.5
- числа в инструкциях: +1 +1 +-1 +-2 +9 +0x3f +0x1ff +0x70 (и ещё 1)
- виртуальные вызовы: +0x1f8 (слот 63) +0x1f8 (слот 63) +0x2f8 (слот 95)
- поля объектов: +0x1b34 +0x1b34 +0x1b34 +0x1b08 +0x1af8 +0x1af8 +0x10 +0x5d1 +0x2f8 −0x1b18
- прямых вызовов: 7 → 19
- инструкций: 56 → 180
```diff
@@ -1,4 +1,6 @@
 push rbp
 mov rbp, rsp
+push r13
+push r12
 push rbx
 mov rbx, rdi
@@ -9,12 +11,12 @@
 cmp byte ptr [rbx + 0x1b04], 0
 jne L
-movss xmm2, dword ptr [rbx + 0x1b18]
+movss xmm1, dword ptr [rbx + 0x1b34]
 mov rdi, rbx
 mov byte ptr [rbx + 0x1b04], 1
-movss dword ptr [rbp - 0x14], xmm2
+movss dword ptr [rbp - 0x24], xmm1
 call F
 mov edi, eax
 call F
-addss xmm0, dword ptr [rbp - 0x14]
+addss xmm0, dword ptr [rbp - 0x24]
 mov rdi, rbx
 movss dword ptr [rbx + 0x1b08], xmm0
@@ -22,35 +24,157 @@
 test al, al
 je L
+add rsp, 0x18
 mov rdi, rbx
-mov rbx, qword ptr [rbp - 8]
 pxor xmm0, xmm0
-leave
+pop rbx
+pop r12
+pop r13
```
(ещё 158 строк диффа: so-query.py fdiff libserver.so 0x44df4d0)

### изменена: 0x44f9a20 (485 байт) CDOTA_Modifier_Morphling_Replicate_Echo_Source::OnCreated | строки: "scepter_echo_count"; "scepter_echo_cast_delay"; "scepter_echo_appear_distance"; "scepter_echo_visible_duration"; "scepter_echo_retarget_radius"; "scepter_echo_damage_outgoing_pct"; "scepter_echo_damage_falloff_pct"; "scepter_echo_min_model_scale"
было: 0x44f8590 (485 байт)
- поля объектов: +0x1b18 +0x1b1c +0x1b20 −0x1af8 −0x1afc −0x1b00
- инструкций: 127 → 127
```diff
@@ -17,5 +17,5 @@
 call F
 mov rdi, rbx
-mov dword ptr [rbx + 0x1af8], eax
+mov dword ptr [rbx + 0x1b04], eax
 call F
 mov rdi, rbx
@@ -31,5 +31,5 @@
 call F
 movaps xmm1, xmm0
-movss dword ptr [rbx + 0x1afc], xmm1
+movss dword ptr [rbx + 0x1b08], xmm1
 mov rdi, rbx
 call F
@@ -46,5 +46,5 @@
 call F
 movaps xmm1, xmm0
-movss dword ptr [rbx + 0x1b00], xmm1
+movss dword ptr [rbx + 0x1b0c], xmm1
 mov rdi, rbx
 call F
@@ -61,5 +61,5 @@
 call F
 movaps xmm1, xmm0
-movss dword ptr [rbx + 0x1b04], xmm1
+movss dword ptr [rbx + 0x1b10], xmm1
 mov rdi, rbx
 call F
@@ -76,5 +76,5 @@
 call F
 movaps xmm1, xmm0
-movss dword ptr [rbx + 0x1b08], xmm1
+movss dword ptr [rbx + 0x1b14], xmm1
 mov rdi, rbx
```
(ещё 22 строк диффа: so-query.py fdiff libserver.so 0x44f9a20)

### изменена: 0x4504440 (6840 байт) CDOTA_Modifier_Juggernaut_Omnislash::OnIntervalThink | строки: "Hero_Juggernaut.SwiftSlash"; "dispel"; "particles/units/heroes/hero_juggernaut/juggernaut_omni_slash_tgt.vpcf"; "particles/units/heroes/hero_juggernaut/juggernaut_omni_slash_tgt_scepter.vpcf"; "attach_hitloc"; "particles/units/heroes/hero_juggernaut/juggernaut_omni_slash_trail.vpcf"; "particles/units/heroes/hero_juggernaut/juggernaut_omni_slash_trail_scepter.vpcf"; "ImmuneToOmnislash"
было: 0x4502fb0 (6840 байт)
- инструкций: 1478 → 1478
```diff
@@ -59,6 +59,6 @@
 mov dword ptr [rbx + 0x1af8], 0xffffffff
 movss xmm6, dword ptr [K:325]
-movss dword ptr [rbp - 0x160], xmm6
-mov qword ptr [rbp - 0x158], rax
+movss dword ptr [rbp - 0x158], xmm6
+mov qword ptr [rbp - 0x160], rax
 mov byte ptr [rbx + 0x1b2a], 0
 xor r12d, r12d
@@ -224,5 +224,5 @@
 mov rax, qword ptr [rax]
 call qword ptr [rax + 0xfc0]
-mov rdi, qword ptr [rbp - 0x158]
+mov rdi, qword ptr [rbp - 0x160]
 xor r8d, r8d
 mov rcx, r13
@@ -230,5 +230,5 @@
 mov edx, eax
 mov esi, 0x2d
-movss xmm0, dword ptr [rbp - 0x160]
+movss xmm0, dword ptr [rbp - 0x158]
 call F
 mov rdi, rbx
@@ -555,7 +555,7 @@
 movss xmm1, dword ptr [K:0.4]
 movaps xmm0, xmm3
-movss dword ptr [rbp - 0x160], xmm3
-mov rdi, rax
-mov qword ptr [rbp - 0x158], rax
+movss dword ptr [rbp - 0x158], xmm3
+mov rdi, rax
+mov qword ptr [rbp - 0x160], rax
 call F
 mov rdi, rbx
```

### изменена: 0x44e5ff0 (1564 байт) вызывается из: CDOTA_Modifier_AntiMage_ManaBreak::vfunc#97 | строки: "modifier_antimage_empowered_mana_break"; "Hero_Antimage.ManaBreak.Empowered"; "empowered_max_burn_pct"; "empowered_mana_break_debuff_duration"; "modifier_antimage_empowered_mana_break_debuff"; "Hero_Antimage.ManaBreak"; "particles/generic_gameplay/generic_manaburn.vpcf"; "particles/units/heroes/hero_antimage/antimage_blade_hit.vpcf"
было: 0x4504a70 (1573 байт)
- цели вызовов: +0x44e5fc0 −0x44e5af0 "AbilityManaCost"; "AbilityHealthCost"
- инструкций: 371 → 368
```diff
@@ -29,18 +29,18 @@
 cmp ecx, dword ptr [rax + 0x10]
 jne L
-mov r14, qword ptr [rax]
-test r14, r14
-je L
-cmp byte ptr [r14 + 0x5d1], 3
-jne L
-mov rdi, r12
-movzx r13d, byte ptr [r14 + 0x624]
+mov r15, qword ptr [rax]
+test r15, r15
+je L
+cmp byte ptr [r15 + 0x5d1], 3
+jne L
+mov rdi, r12
+movzx r13d, byte ptr [r15 + 0x624]
 call F
 cmp r13b, byte ptr [rax + 0x624]
 je L
 pxor xmm0, xmm0
-comiss xmm0, dword ptr [r14 + 0xd70]
+comiss xmm0, dword ptr [r15 + 0xd70]
 jae L
-test byte ptr [r14 + 0x1249], 2
+test byte ptr [r15 + 0x1249], 2
 je L
 nop dword ptr [rax]
@@ -76,5 +76,5 @@
 cvtsi2ss xmm1, dword ptr [r12 + 0x1afc]
 movss xmm0, dword ptr [r12 + 0x1b00]
-mulss xmm0, dword ptr [r14 + 0xd70]
+mulss xmm0, dword ptr [r15 + 0xd70]
 divss xmm0, dword ptr [K:100]
```
(ещё 199 строк диффа: so-query.py fdiff libserver.so 0x44e5ff0)

### изменена: 0x450aac0 (3023 байт) вызывается из: CDOTA_Modifier_Earthshaker_Slugger_Intrinsic::vfunc#97 | строки: "projectile_body_on_kill"; "earthshaker_enchant_totem"; "projectile_body_speed"; "projectile_body_distance"; "projectile_body_width_creep"; "projectile_body_width_hero"; "projectile_body_vision"; "projectile_body_damage_creep"
было: 0x4509c60 (2941 байт)
- числа в инструкциях: +9 +9 +9 +0x12 +0x12 +0x12 +0xff
- поля объектов: +0x10
- цели вызовов: +0x3c75e80
- инструкций: 621 → 647
```diff
@@ -88,7 +88,7 @@
 call F
 mov rdi, rbx
-mov qword ptr [rbp - 0x158], rax
-call F
-mov rdi, qword ptr [rbp - 0x158]
+mov qword ptr [rbp - 0x150], rax
+call F
+mov rdi, qword ptr [rbp - 0x150]
 mov rsi, rax
 call F
@@ -100,7 +100,7 @@
 call F
 mov rdi, r13
-mov qword ptr [rbp - 0x158], rax
-call F
-cmp qword ptr [rbp - 0x158], 0
+mov qword ptr [rbp - 0x150], rax
+call F
+cmp qword ptr [rbp - 0x150], 0
 mov r15, rax
 je L
@@ -150,6 +150,6 @@
 cmp dword ptr [rbp - 0x160], r13d
 jg L
-pxor xmm6, xmm6
-ucomiss xmm0, xmm6
+pxor xmm7, xmm7
+ucomiss xmm0, xmm7
 mov edx, 0
 setnp al
@@ -179,5 +179,5 @@
 mov rax, qword ptr [rbx]
 call qword ptr [rax + 0x1f0]
```
(ещё 329 строк диффа: so-query.py fdiff libserver.so 0x450aac0)

### изменена: 0x4511c40 (1324 байт) CDOTA_Ability_Lich_Sinister_Gaze::OnSpellStart | строки: "channel_duration"; "aoe_scepter"; "duration"; "modifier_lich_sinister_gaze"; "Hero_Lich.SinisterGaze.Cast"; "modifier_lich_sinister_gaze_self"
было: 0x450c850 (1272 байт)
- числа в инструкциях: +1 +1
- поля объектов: +0x860 +0x860 +0x860 +0x870 +0x868
- цели вызовов: −0x450aa60
- инструкций: 307 → 316
```diff
@@ -254,4 +254,5 @@
 call F
 movzx esi, byte ptr [r13 + 0x624]
+mov r14d, 0xffffffff
 movss xmm0, dword ptr [rbp - 0x94]
 mov rdi, rax
@@ -266,15 +267,18 @@
 mov rdi, r12
 call F
-mov dword ptr [rbp - 0x50], 0xffffffff
 mov rax, qword ptr [r13 + 0x10]
-lea rdi, [rbx + 0x860]
 test rax, rax
 je L
-mov eax, dword ptr [rax + 0x10]
-mov dword ptr [rbp - 0x50], eax
-mov rsi, r12
-call F
-jmp L
-nop dword ptr [rax + rax]
+mov r14d, dword ptr [rax + 0x10]
+movsxd r13, dword ptr [rbx + 0x860]
+cmp r13d, dword ptr [rbx + 0x870]
+mov eax, r13d
+je L
+add eax, 1
+mov dword ptr [rbx + 0x860], eax
+mov rax, qword ptr [rbx + 0x868]
+mov dword ptr [rax + r13*4], r14d
+jmp L
+nop dword ptr [rax]
 mov rdi, rbx
 call F
@@ -306,2 +310,7 @@
```
(ещё 7 строк диффа: so-query.py fdiff libserver.so 0x4511c40)

### изменена: 0x450f000 (805 байт) вызывается из: CDOTA_Modifier_Earthshaker_Fissure_Shard::vfunc#97 | строки: "npc_dota_hero_rubick"; "earthshaker_fissure"; "rubick_telekinesis_land"; "rubick_telekinesis_land_self"; "earthshaker_enchant_totem"; "<NoAbilityName>"; "earthshaker_echo_slam"; "earthshaker_aftershock"
было: 0x450e640 (821 байт)
- инструкций: 212 → 209
```diff
@@ -135,11 +135,8 @@
 je L
 lea rsi, [S:"rubick_telekinesis_land_self"]
-cmp r14, rsi
-je L
-mov rdi, r14
-call F
-test eax, eax
-je L
-nop word ptr cs:[rax + rax]
+mov rdi, r14
+call F
+test al, al
+jne L
 call F
 test al, al
```

### изменена: 0x4512cc0 (539 байт) | строки: "modifier_morphling_replicate_echo"
было: 0x4511de0 (539 байт)
- поля объектов: +0x1b14 +0x1b14 −0x1b08 −0x1b08
- инструкций: 152 → 152
```diff
@@ -22,5 +22,5 @@
 je L
 pxor xmm0, xmm0
-comiss xmm0, dword ptr [r14 + 0x1b08]
+comiss xmm0, dword ptr [r14 + 0x1b14]
 jae L
 mov rsi, rcx
@@ -29,5 +29,5 @@
 call F
 mov rdi, rbx
-movss xmm0, dword ptr [r14 + 0x1b08]
+movss xmm0, dword ptr [r14 + 0x1b14]
 mov qword ptr [rbp - 0x50], 0
 movzx r15d, al
```

### изменена: 0x4512ee0 (1839 байт) вызывается из: CDOTA_Modifier_Morphling_Replicate_Echo_Source::OnIntervalThink | строки: "replicate_echo"; "nodraw"; "no_effect_on_original"; "invulnerability_on_creation"; "duration"; "permit_illusion_recycling"; "illusion_"; "modifier_morphling_replicate_echo"
было: 0x4512000 (1677 байт)
- строки: +"ogre_magi_multicast" +"<NoAbilityName>"
- числа в инструкциях: +0 +9 +9 +0x12 +0x12 +0x12 +0xff +0x3fffffff −-1 −-2 −0x3f −0x1ff −0x70 −3 −1 −1 (и ещё 1)
- виртуальные вызовы: +0x7a8 (слот 245) +0x20 (слот 4)
- поля объектов: +0x1b04 +0x1b08 +0x1b08 +0x840 +0x1b1c +0x1b18 +0x1b20 +0x20 −0x5d1 −0x1af8 −0x1af8 −0x1afc −0x1afc −0x1b14 −0x1b00
- прямых вызовов: 38 → 37
- цели вызовов: +0x3c75e80 +0x6212b60 "<NoAbilityName>"; "dota_empty_ability" −0x5079b90 −0x44bed10 −0x44be570 −0x44e3030
- инструкций: 356 → 409
```diff
@@ -3,128 +3,110 @@
 push r15
 push r14
+mov r14, rdi
 push r13
-mov r13, rdx
 push r12
 push rbx
 mov rbx, rsi
-sub rsp, 0x108
-mov qword ptr [rbp - 0xd8], rdi
-mov rdi, rsi
-call F
-mov ecx, dword ptr [r13]
-mov qword ptr [rbp - 0xe0], rax
-cmp ecx, -1
-je L
-mov rsi, qword ptr [D]
-test rsi, rsi
-je L
-cmp ecx, -2
-je L
-movzx eax, word ptr [r13]
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
```
(ещё 565 строк диффа: so-query.py fdiff libserver.so 0x4512ee0)

### изменена: 0x4515ac0 (1627 байт) вызывается из: CDOTA_Ability_Kunkka_XMarksTheSpot::OnUnStolen, CDOTA_Modifier_Kunkka_XMarksTheSpot::vfunc#86, CDOTA_Ability_Kunkka_Return::OnSpellStart | строки: "kunkka_return"; "kunkka_x_marks_the_spot"; "modifier_kunkka_x_marks_the_spot"; "Ability.XMarksTheSpot.Return"; "x_return"; "kunkka_torrent"; "delay"; "modifier_kunkka_x_marks_the_spot_marker"
было: 0x4514760 (1575 байт)
- числа в инструкциях: +0 +0x3fffffff
- виртуальные вызовы: +0x20 (слот 4)
- цели вызовов: −0x44e3030
- инструкций: 367 → 375
```diff
@@ -34,12 +34,12 @@
 cmp ecx, dword ptr [rax + 0x10]
 jne L
-mov r14, qword ptr [rax]
-test r14, r14
-je L
-cmp byte ptr [r14 + 0x5d1], 3
-jne L
-test byte ptr [r14 + 0x1249], 2
-jne L
-cmp byte ptr [r14 + 0x174c], 0
+mov r15, qword ptr [rax]
+test r15, r15
+je L
+cmp byte ptr [r15 + 0x5d1], 3
+jne L
+test byte ptr [r15 + 0x1249], 2
+jne L
+cmp byte ptr [r15 + 0x174c], 0
 je L
 nop dword ptr [rax]
@@ -81,18 +81,18 @@
 ret
 nop
-test byte ptr [r14 + 0x1249], 1
+test byte ptr [r15 + 0x1249], 1
 jne L
 lea rsi, [S:"modifier_kunkka_x_marks_the_spot"]
 xor edx, edx
-mov rdi, r14
+mov rdi, r15
 call F
 test rax, rax
 mov r13, rax
```
(ещё 292 строк диффа: so-query.py fdiff libserver.so 0x4515ac0)

### изменена: 0x45236e0 (2001 байт) вызывается из: CDOTA_Modifier_Earthshaker_Aftershock::vfunc#97 | строки: "earthshaker_aftershock"; "aftershock_damage"; "npc_dota_hero_morphling"; "modifier_earthshaker_arcana"; "earthshaker_enchant_totem"; "modifier_stunned"; "duration"; "<NoAbilityName>"
было: 0x4522360 (2004 байт)
- инструкций: 447 → 450
```diff
@@ -92,8 +92,17 @@
 call qword ptr [rax + 0xe30]
 lea rsi, [S:"npc_dota_hero_morphling"]
-mov rdi, rax
-call F
-test al, al
-jne L
+cmp rax, rsi
+mov rdi, rax
+je L
+test rax, rax
+je L
+call F
+test eax, eax
+jne L
+mov rax, qword ptr [r15]
+mov rdi, r15
+call qword ptr [rax + 0x900]
+test al, al
+je L
 mov rdi, r13
 mov dword ptr [rbp - 0x58], 0
@@ -115,6 +124,6 @@
 mov rdi, rax
 call F
+mov dword ptr [rbp - 0xe8], 0xffffffff
 mov qword ptr [rbp - 0xf0], 0
-mov dword ptr [rbp - 0xe8], 0xffffffff
 mov dword ptr [rbp - 0xe4], 0
 mov eax, dword ptr [rbp - 0xe4]
@@ -137,10 +146,4 @@
 mov rax, qword ptr [rdi]
 call qword ptr [rax + 0x20]
-jmp L
```
(ещё 7 строк диффа: so-query.py fdiff libserver.so 0x45236e0)

### изменена: 0x458da60 (446 байт) CDOTA_Ability_ShadowShaman_Shackles::OnChannelThink | строки: "modifier_shadow_shaman_shackles"
было: 0x458c560 (414 байт)
- прямых вызовов: 8 → 10
- инструкций: 120 → 124
```diff
@@ -4,24 +4,24 @@
 push r14
 push r13
-mov r13, rdi
 push r12
+mov r12, rdi
 push rbx
 sub rsp, 8
 mov ebx, dword ptr [rdi + 0x860]
-mov r12d, ebx
-sub r12d, 1
+mov r13d, ebx
+sub r13d, 1
 js L
-movsxd r12, r12d
-shl r12, 2
+movsxd r13, r13d
+shl r13, 2
 jmp L
 nop word ptr cs:[rax + rax]
 nop dword ptr [rax + rax]
-sub r12, 4
+sub r13, 4
 test ebx, ebx
 je L
-mov rax, qword ptr [r13 + 0x868]
+mov rax, qword ptr [r12 + 0x868]
 mov r15d, ebx
 sub ebx, 1
-add rax, r12
+add rax, r13
 mov ecx, dword ptr [rax]
 cmp ecx, -1
@@ -49,15 +49,17 @@
```
(ещё 80 строк диффа: so-query.py fdiff libserver.so 0x458da60)

### изменена: 0x4592e80 (1029 байт) CDOTA_Ability_ShadowShaman_Shackles::OnChannelFinish | строки: "modifier_shadow_shaman_shackles"; "ward_linger_duration"; "modifier_shadow_shaman_serpent_ward_shackle_tracker"; "modifier_shadow_shaman_serpent_ward"
было: 0x4591ac0 (1029 байт)
- прямых вызовов: 23 → 24
- инструкций: 260 → 262
```diff
@@ -42,9 +42,11 @@
 cmp ecx, 1
 jne L
-xor ecx, ecx
-xor edx, edx
+mov rdi, rbx
 mov dword ptr [rbx + 0x860], eax
+call F
+mov rcx, rbx
 mov rdi, r13
 lea rsi, [S:"modifier_shadow_shaman_shackles"]
+mov rdx, rax
 call F
 test r12b, r12b
@@ -74,5 +76,5 @@
 call F
 jmp L
-nop dword ptr [rax + rax]
+nop word ptr [rax + rax]
 test r8d, r8d
 jne L
@@ -135,5 +137,5 @@
 xor eax, eax
 jmp L
-nop word ptr [rax + rax]
+nop
 add rax, 1
 cmp rax, rdi
```

### изменена: 0x45ca1f0 (1716 байт) CDOTA_Ability_Tidehunter_Gush::OnSpellStart | строки: "gush_damage"; "projectile_speed"; "speed_scepter"; "aoe_scepter"; "particles/units/heroes/hero_tidehunter/tidehunter_gush_upgrade.vpcf"; "Hero_Tidehunter.Gush.AghsProjectile"; "Ability.GushCast"; "particles/units/heroes/hero_tidehunter/tidehunter_gush.vpcf"
было: 0x45c8930 (1723 байт)
- инструкций: 340 → 340
```diff
@@ -22,15 +22,16 @@
 mov rdi, rbx
 lea rsi, [S:"speed_scepter"]
+mov r14d, eax
+call F
+movss xmm0, dword ptr [K:-1]
+xor edx, edx
+mov rdi, rbx
+lea rsi, [S:"aoe_scepter"]
 mov r13d, eax
 call F
-movss xmm0, dword ptr [K:-1]
-xor edx, edx
-mov rdi, rbx
-lea rsi, [S:"aoe_scepter"]
-mov r14d, eax
-call F
 mov rdi, rbx
 movd r15d, xmm0
 call F
+mov rdi, rbx
 test rax, rax
 je L
@@ -38,5 +39,4 @@
 mov r12, rax
 jne L
-mov rdi, rbx
 call F
 test rax, rax
@@ -47,120 +47,7 @@
 call F
 test al, al
-jne L
-mov r14, qword ptr [K:0xffffffffffffffff]
```
(ещё 287 строк диффа: so-query.py fdiff libserver.so 0x45ca1f0)

### изменена: 0x45cd4a0 (1880 байт) CDOTA_Ability_VengefulSpirit_Magic_Missile::vfunc#371 | строки: "bFirstTarget"; "bShouldBounce"; "bounce_range_pct"; "magic_missile_stun"; "magic_missile_damage"; "damage_per_lasthit"; "modifier_stunned"; "Hero_VengefulSpirit.MagicMissileImpact"
было: 0x45cbbe0 (1917 байт)
- числа в инструкциях: +0 +0 +0 −-1 −-2 −9 −0x3f −0x1ff −0x70
- поля объектов: −0x10
- прямых вызовов: 42 → 43
- цели вызовов: +0x3ba8c00
- инструкций: 405 → 388
```diff
@@ -6,8 +6,8 @@
 mov r15, rsi
 push r14
-lea r14, [S:"bFirstTarget"]
 push r13
-lea r13, [rbp - 0xd0]
+lea r13, [S:"bFirstTarget"]
 push r12
+lea r12, [rbp - 0xd0]
 push rbx
 mov rbx, rdi
@@ -15,5 +15,5 @@
 mov rdi, qword ptr [rsi + 0x20]
 mov qword ptr [rbp - 0xd0], rax
-mov rsi, r13
+mov rsi, r12
 lea rax, [S:"bShouldBounce"]
 mov qword ptr [rbp - 0xc8], rax
@@ -21,7 +21,7 @@
 mov rdi, qword ptr [r15 + 0x20]
 xor edx, edx
-mov rsi, r13
-mov r12d, eax
-mov qword ptr [rbp - 0xc8], r14
+mov rsi, r12
+mov r14d, eax
+mov qword ptr [rbp - 0xc8], r13
 movabs rax, 0xffffffff5f6555de
 mov qword ptr [rbp - 0xd0], rax
@@ -30,8 +30,8 @@
 cmp ecx, -1
 je L
+cmp ecx, -2
 mov rdi, qword ptr [D]
```
(ещё 231 строк диффа: so-query.py fdiff libserver.so 0x45cd4a0)

### изменена: 0x45a6db0 (1268 байт) вызывается из: CDOTA_Modifier_Windrunner_UnfocusedFire::vfunc#97 | строки: "modifier_windrunner_shackle_shot"
было: 0x45da640 (1205 байт)
- виртуальные вызовы: +0x40 (слот 8)
- поля объектов: +0x80
- прямых вызовов: 25 → 26
- цели вызовов: −0x45dbe60
- инструкций: 294 → 310
```diff
@@ -106,5 +106,5 @@
 mov rdi, r12
 mov ecx, dword ptr [rax + rbx + 4]
-mov dword ptr [rbp - 0xcc], ecx
+mov dword ptr [rbp - 0xd0], ecx
 call F
 mov rdi, r14
@@ -116,5 +116,5 @@
 xor r8d, r8d
 mov edx, 0x330
-mov ecx, dword ptr [rbp - 0xcc]
+mov ecx, dword ptr [rbp - 0xd0]
 mov rdi, rax
 mov rsi, qword ptr [rbp - 0xc8]
@@ -153,5 +153,5 @@
 mov rax, r13
 movups xmmword ptr [r13 + 8], xmm0
-add rsp, 0xa8
+lea rsp, [rbp - 0x28]
 pop rbx
 pop r12
@@ -280,10 +280,24 @@
 call F
 lea rax, [D]
-xor edx, edx
+mov r14, qword ptr [D]
+mov r12, qword ptr [rax]
+mov rsi, r14
+mov rax, qword ptr [r12]
+mov r10, qword ptr [rax + 0x80]
+lea rax, [D]
+mov qword ptr [rbp - 0xd0], r10
+mov rdi, qword ptr [rax]
+mov rax, qword ptr [rdi]
```
(ещё 23 строк диффа: so-query.py fdiff libserver.so 0x45a6db0)

### изменена: 0x45e0dd0 (784 байт) | строки: "CNetworkTransmitComponent::StateChanged(%s) @%s:%d"
было: 0x45df9f0 (1609 байт)
- строки: −"CNetworkTransmitComponent::StateChanged(%s) @%s:%d" −"modifier_shadow_shaman_shackles"
- числа в инструкциях: −1 −1 −1 −1 −1 −0 −0 −0 (и ещё 20)
- виртуальные вызовы: −0x20 (слот 4) −0x1d8 (слот 59) −0x1d8 (слот 59)
- поля объектов: −0x868 −0x860 −0x860 −0xf0 −0x318 −0x48 −0x18 −0x315 −0x310 −0x32e −0x30 −0x538 (и ещё 6)
- прямых вызовов: 22 → 11
- цели вызовов: −0x61d5bf0
- инструкций: 337 → 162
```diff
@@ -161,177 +161,2 @@
 call F
 jmp L
-push rbp
-mov rbp, rsp
-push r15
-push r14
-push r13
-mov r13, rdi
-push r12
-push rbx
-sub rsp, 0x168
-mov esi, dword ptr [rdi + 0x860]
-test esi, esi
-jle L
-mov dword ptr [rbp - 0x184], 0
-xor r12d, r12d
-lea rbx, [S:"modifier_shadow_shaman_shackles"]
-nop dword ptr [rax]
-mov rax, qword ptr [r13 + 0x868]
-lea rax, [rax + r12*4]
-mov ecx, dword ptr [rax]
-cmp ecx, -1
-je L
-mov rdi, qword ptr [D]
-test rdi, rdi
-je L
-cmp ecx, -2
-je L
-movzx eax, word ptr [rax]
-mov rdx, rax
-shr rdx, 9
-and edx, 0x3f
-mov rdx, qword ptr [rdi + rdx*8]
```
(ещё 144 строк диффа: so-query.py fdiff libserver.so 0x45e0dd0)

### изменена: 0x45f6e80 (1831 байт) вызывается из: CDOTA_Modifier_StormSpirit_Electric_Rave::vfunc#97 | строки: "particles/units/heroes/hero_stormspirit/stormspirit_overload_discharge.vpcf"; "modifier_storm_spirit_overload_debuff"; "duration"; "Hero_StormSpirit.Overload"; "storm_spirit_overload"; "overload_bounces"; "overloadpop"; "damage"
было: 0x45f5a80 (1831 байт)
- инструкций: 412 → 412
```diff
@@ -395,5 +395,5 @@
 mov rsi, r12
 call F
-movss xmm0, dword ptr [rbp - 0x278]
+movss xmm0, dword ptr [rbp - 0x288]
 lea rsi, [S:"duration"]
 mov rdi, rbx
```

### изменена: 0x45f75b0 (5568 байт) CDOTA_Ability_Windrunner_Shackleshot::vfunc#371 | строки: "bouncing_attack"; "attack_damage"; "shackle_distance"; "shackle_angle"; "unlimited_shackles"; "damage_buff_duration"; "bonus_damage_per_hero"; "bonus_damage_per_other_pct"
было: 0x45f61b0 (5640 байт)
- числа в инструкциях: −0 −0 −1
- цели вызовов: −0x3bb1f20
- инструкций: 1140 → 1125
```diff
@@ -185,5 +185,5 @@
 movq xmm1, qword ptr [r15 + 0x86c]
 mov dword ptr [rbp - 0x220], 0
-movss dword ptr [rbp - 0x2bc], xmm0
+movss dword ptr [rbp - 0x2b8], xmm0
 movq xmm0, qword ptr [r12 + 0xc]
 subps xmm0, xmm1
@@ -192,5 +192,5 @@
 mov rdi, r15
 movabs rax, 0x8000000000000040
-mov dword ptr [rbp - 0x1fc], 0
+mov qword ptr [rbp - 0x200], 0
 mov qword ptr [rbp - 0x140], rax
 lea rax, [rbp - 0x150]
@@ -246,5 +246,5 @@
 mov esi, dword ptr [r15 + 0x85c]
 test esi, esi
-mov dword ptr [rbp - 0x288], esi
+mov dword ptr [rbp - 0x280], esi
 jle L
 mov r14, qword ptr [rbp - 0x258]
@@ -259,5 +259,5 @@
 lea rsi, [S:"bonus_damage_per_other_pct"]
 mov r15d, eax
-mov dword ptr [rbp - 0x2b0], eax
+mov dword ptr [rbp - 0x2b4], eax
 call F
 pxor xmm0, xmm0
@@ -266,14 +266,13 @@
 divss xmm0, dword ptr [K:100]
 cvttss2si eax, xmm0
-mov dword ptr [rbp - 0x2c0], eax
+mov dword ptr [rbp - 0x2bc], eax
 xor r15d, r15d
```
(ещё 455 строк диффа: so-query.py fdiff libserver.so 0x45f75b0)

### изменена: 0x467bfd0 (670 байт) вызывается из: CDOTA_Modifier_FountainPassive::vfunc#97 | строки: "modifier_fountain_fury_swipes_damage_increase"; "duration"
было: 0x467a010 (790 байт)
- строки: +"modifier_fountain_fury_swipes_damage_increase" +"modifier_fountain_fury_swipes_damage_increase"
- числа в инструкциях: +1 −-1 −-2 −9 −0x3f −0x1ff −0x70 −3 −0
- поля объектов: −0x10 −0x5d1 −0xd0 −0xd0
- прямых вызовов: 13 → 14
- цели вызовов: +0x44be570 +0x44bed10
- инструкций: 196 → 168
```diff
@@ -12,5 +12,5 @@
 cmp ecx, -1
 je L
-mov r14, rsi
+mov r13, rsi
 mov rsi, qword ptr [D]
 test rsi, rsi
@@ -30,32 +30,32 @@
 cmp ecx, dword ptr [rax + 0x10]
 jne L
-mov r13, qword ptr [rax]
-test r13, r13
+mov r14, qword ptr [rax]
+test r14, r14
 je L
-cmp byte ptr [r13 + 0x5d1], 3
+cmp byte ptr [r14 + 0x5d1], 3
 jne L
-mov rdi, r14
+mov rdi, r13
 call F
-cmp r13, rax
+cmp r14, rax
 je L
-mov r15d, dword ptr [r12 + 0xd0]
-cmp r15d, -1
+mov ecx, dword ptr [r12 + 0xd0]
+cmp ecx, -1
 je L
-mov rdx, qword ptr [D]
+mov rsi, qword ptr [D]
+test rsi, rsi
+je L
+cmp ecx, -2
```
(ещё 145 строк диффа: so-query.py fdiff libserver.so 0x467bfd0)

### изменена: 0x469f590 (2770 байт) CDOTA_Modifier_Beastmaster_DrumsOfSlom::OnIntervalThink | строки: "particles/units/heroes/hero_beastmaster/beastmaster_drums_of_slom_stop.vpcf"; "attach_hitloc"; "Hero_Beastmaster.DrumsOfSlom.Strike"; "particles/units/heroes/hero_beastmaster/beastmaster_drums_of_slom_hit.vpcf"; "particles/units/heroes/hero_phoenix/phoenix_sunray_beam_friend.vpcf"
было: 0x469e1d0 (2738 байт)
- числа в инструкциях: +-1 +-2 +9 +0x3f +0x1ff +0x70
- поля объектов: +0x10
- прямых вызовов: 78 → 77
- инструкций: 565 → 576
```diff
@@ -83,9 +83,9 @@
 addss xmm1, dword ptr [rbx + 0x1b28]
 mov rdi, rbx
-movss dword ptr [rbp - 0x188], xmm1
+movss dword ptr [rbp - 0x184], xmm1
 call F
 mov edi, eax
 call F
-movss xmm1, dword ptr [rbp - 0x188]
+movss xmm1, dword ptr [rbp - 0x184]
 comiss xmm1, xmm0
 jp L
@@ -128,5 +128,4 @@
 mov r8d, 5
 call F
-lea r14, [rbp - 0x150]
 call F
 mov rdi, rbx
@@ -155,5 +154,5 @@
 pxor xmm0, xmm0
 mov rcx, rax
-mov qword ptr [rbp - 0x1a8], rax
+mov qword ptr [rbp - 0x1a0], rax
 movlps qword ptr [rbp - 0x130], xmm1
 call F
@@ -169,5 +168,5 @@
 mov qword ptr [rbp - 0x150], 0
 mov qword ptr [rbp - 0x148], 0
-movss dword ptr [rbp - 0x188], xmm0
+movss dword ptr [rbp - 0x184], xmm0
 mov qword ptr [rbp - 0x140], 0
 call F
@@ -182,28 +181,28 @@
 mov rdi, rax
```
(ещё 449 строк диффа: so-query.py fdiff libserver.so 0x469f590)

### изменена: 0x4773f80 (2051 байт) CDOTA_Ability_Venomancer_NoxiousPlague::vfunc#371 | строки: "spread_count"; "spreads"; "first_projectile"; "do_impact"; "debuff_duration"; "modifier_venomancer_noxious_plague_primary"; "modifier_venomancer_noxious_plague_contagious"; "debuff_copy_id"
было: 0x4772b80 (2040 байт)
- виртуальные вызовы: +0x538 (слот 167)
- прямых вызовов: 48 → 49
- инструкций: 481 → 484
```diff
@@ -119,4 +119,9 @@
 test al, al
 je L
+mov rax, qword ptr [r13]
+mov rdi, r13
+call qword ptr [rax + 0x538]
+test al, al
+je L
 lea rsi, [S:"modifier_venomancer_noxious_plague_contagious"]
 xor edx, edx
@@ -141,6 +146,5 @@
 jne L
 jmp L
-nop word ptr cs:[rax + rax]
-nop
+nop dword ptr [rax + rax]
 add rdx, 0x28
 cmp rcx, rdx
@@ -398,4 +402,10 @@
 mov ecx, 1
 jmp L
+nop word ptr [rax + rax]
+lea edx, [r15 - 1]
+mov rsi, r13
+mov rdi, r14
+call F
+jmp L
 xor ecx, ecx
 xor edx, edx
@@ -429,5 +439,5 @@
 jne L
 jmp L
-nop dword ptr [rax]
+nop
```
(ещё 12 строк диффа: so-query.py fdiff libserver.so 0x4773f80)

### изменена: 0x4789380 (997 байт) CDOTA_Unit_TargetDummy::vfunc#263
было: 0x4787f60 (949 байт)
- числа в инструкциях: +0 +0x3fffffff
- виртуальные вызовы: +0x20 (слот 4)
- инструкций: 203 → 213
```diff
@@ -156,10 +156,20 @@
 mov rax, qword ptr [rbx]
 call qword ptr [rax + 0xf0]
-lea rdi, [rbp - 0x58]
-call F
+cmp dword ptr [rbp - 0x44], 0x3fffffff
+mov dword ptr [rbp - 0x58], 0
+movss xmm0, dword ptr [rbp - 0x74]
+ja L
+mov rsi, qword ptr [rbp - 0x50]
+test rsi, rsi
+je L
+mov rax, qword ptr [D]
+movss dword ptr [rbp - 0x74], xmm0
+mov rdi, qword ptr [rax]
+mov rax, qword ptr [rdi]
+call qword ptr [rax + 0x20]
 movss xmm0, dword ptr [rbp - 0x74]
 movss dword ptr [rbx + 0x2394], xmm0
 jmp L
-nop dword ptr [rax]
+nop word ptr cs:[rax + rax]
 lea rdi, [rbp - 0x50]
 xor esi, esi
```

### изменена: 0x47a61e0 (3310 байт) CDOTA_RoshanSpawner::vfunc#237 | строки: "Unit"; "UseNeutralCreepBehavior"; "npc_dota_roshan"; "particles/neutral_fx/roshan_timer.vpcf"
было: 0x47a4da0 (3374 байт)
- числа в инструкциях: −-1 −-2 −9 −0x3f −0x1ff −0x70
- поля объектов: −0x10 −0x794 −0x794
- прямых вызовов: 75 → 76
- цели вызовов: +0x3ba8c00
- инструкций: 665 → 648
```diff
@@ -9,6 +9,6 @@
 push rbx
 sub rsp, 0xd8
-lea r15, [D]
-mov rdx, qword ptr [r15]
+lea r14, [D]
+mov rdx, qword ptr [r14]
 movsxd rax, dword ptr [rdx + 0x418]
 cmp eax, 0xc
@@ -35,5 +35,5 @@
 mov rdi, rbx
 call F
-lea r14, [rbp - 0x90]
+lea r15, [rbp - 0x90]
 mov edx, 1
 mov rdi, rbx
@@ -42,5 +42,5 @@
 mov edx, 2
 xor esi, esi
-mov rdi, r14
+mov rdi, r15
 lea rax, [T]
 mov qword ptr [rbp - 0xc0], 0
@@ -54,5 +54,5 @@
 mov qword ptr [rbp - 0x48], r12
 call F
-mov r8, r14
+mov r8, r15
 mov rcx, rbx
 xor edx, edx
@@ -62,5 +62,5 @@
 movss xmm1, dword ptr [rax + 8]
 call F
-mov rdi, r14
```
(ещё 252 строк диффа: so-query.py fdiff libserver.so 0x47a61e0)

### изменена: 0x48565c0 (475 байт) вызывается из: CDOTA_Modifier_Broodmother_Spider_HP::vfunc#97
было: 0x4855060 (392 байт)
- числа в инструкциях: +1 +3
- поля объектов: +0x5d1 +0xd3c +0xd58
- прямых вызовов: 4 → 6
- цели вызовов: +0x3ba8c00 +0x44be570
- инструкций: 103 → 125
```diff
@@ -64,4 +64,17 @@
 cmp ecx, dword ptr [rax + 0x10]
 jne L
+mov rax, qword ptr [rax]
+test rax, rax
+je L
+cmp byte ptr [rax + 0x5d1], 3
+jne L
+test byte ptr [rax + 0xd3c], 1
+je L
+cmp byte ptr [rax + 0x175a], 0
+jne L
+lea rdi, [r12 + 0xd0]
+call F
+test rax, rax
+je L
 mov r13, qword ptr [rax]
 test r13, r13
@@ -70,7 +83,11 @@
 jne L
 test byte ptr [r13 + 0xd3c], 1
-je L
-cmp byte ptr [r13 + 0x175a], 0
 jne L
+mov rax, qword ptr [r13]
+lea rdx, [T]
+mov rax, qword ptr [rax + 0xd58]
+cmp rax, rdx
+jne L
+xor r13d, r13d
 mov rdi, r12
 call F
@@ -93,5 +110,4 @@
 call F
```
(ещё 13 строк диффа: so-query.py fdiff libserver.so 0x48565c0)

### изменена: 0x485ed80 (1083 байт) | строки: "PlayerID_t"
было: 0x485cc80 (3963 байт)
- константы из данных (числа логики): −0x00000000000000090000000000000000 −0x00000000000000090000000000000000 −0x00000000000000090000000000000000 −0x00000000000000090000000000000000
- числа в инструкциях: −0xffffffff −0xffffffff −0xffffffff −0xffffffff −0 −0 −0 −0 (и ещё 100)
- прямых вызовов: 40 → 12
- цели вызовов: −__cxa_guard_acquire() −0x6a42730 −__cxa_atexit() −__cxa_guard_release() −0x59dbb20 −0x4811300 −0x480ef60 −0x3bbc1c0 −0x4811310 −0x480ef80 −0x4811320 −0x480efa0 −0x4811330 −0x480efc0
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
```
(ещё 417 строк диффа: so-query.py fdiff libserver.so 0x485ed80)

### изменена: 0x4b1e1f0 (8 байт) CDOTA_Ability_Marci_Companion_Run::vfunc#239
было: 0x4b1cc30 (3 байт)
- поля объектов: +0x858
- инструкций: 2 → 2
```diff
@@ -1,2 +1,2 @@
-xor eax, eax
+movzx eax, byte ptr [rdi + 0x858]
 ret
```

### изменена: 0x4bbafc0 (2797 байт) CDOTA_Modifier_Marci_Grapple_VictimMotion::OnDestroy | строки: "particles/units/heroes/hero_marci/marci_dispose_aoe_damage.vpcf"; "attach_hitloc"; "modifier_marci_dispose_debuff"; "duration"; "Hero_Marci.Grapple.Stun"; "particles/units/heroes/hero_marci/marci_dispose_land.vpcf"; "particles/units/heroes/hero_marci/marci_dispose_land_aoe.vpcf"; "Hero_Marci.Grapple.Impact"
было: 0x4bb98c0 (2797 байт)
- инструкций: 572 → 572
```diff
@@ -88,9 +88,9 @@
 mov rax, qword ptr [K:0x00000000ffffffff]
 xor r13d, r13d
-mov dword ptr [rbp - 0x13c], 0
+mov dword ptr [rbp - 0x130], 0
 movaps xmm6, xmmword ptr [K:-1,-1,3.402823e+38,3.402823e+38]
 movss xmm5, dword ptr [K:3.402823e+38]
-movaps xmmword ptr [rbp - 0x150], xmm6
-mov qword ptr [rbp - 0x138], rax
+movaps xmmword ptr [rbp - 0x140], xmm6
+mov qword ptr [rbp - 0x148], rax
 lea rax, [rbp - 0xd0]
 mov qword ptr [rbp - 0x118], rax
@@ -138,7 +138,7 @@
 mov dword ptr [rbp - 0xc8], 2
 mov qword ptr [rbp - 0xb0], rax
-mov rax, qword ptr [rbp - 0x138]
+mov rax, qword ptr [rbp - 0x148]
 lea rcx, [S:"particles/units/heroes/hero_marci/marci_dispose_aoe_damage.vpcf"]
-movaps xmm4, xmmword ptr [rbp - 0x150]
+movaps xmm4, xmmword ptr [rbp - 0x140]
 mov qword ptr [rbp - 0xd0], rcx
 xor ecx, ecx
@@ -269,5 +269,5 @@
 cmp byte ptr [r12 + 0x175a], 0
 jne L
-add dword ptr [rbp - 0x13c], 1
+add dword ptr [rbp - 0x130], 1
 cmp byte ptr [r12 + 0x5d1], 3
 jne L
@@ -299,5 +299,5 @@
 cmp esi, r13d
 jg L
-cmp dword ptr [rbp - 0x13c], 1
```
(ещё 33 строк диффа: so-query.py fdiff libserver.so 0x4bbafc0)

### изменена: 0x4bf1260 (251 байт) CDOTA_Modifier_Ogre_Magi_Bloodlust::OnCreated, CDOTA_Modifier_Ogre_Magi_Bloodlust::OnRefresh | строки: "bonus_attack_speed"; "bonus_movement_speed"; "self_bonus"; "modelscale"
было: 0x4bf0380 (301 байт)
- поля объектов: −0x1af8 −0x1b00
- прямых вызовов: 14 → 12
- цели вызовов: −0x5040ef0 −0x5043810
- инструкций: 84 → 70
```diff
@@ -65,20 +65,6 @@
 movaps xmm1, xmm0
 movss dword ptr [rbx + 0x1b04], xmm1
-mov rdi, rbx
-call F
-mov rdi, rbx
-mov r12, rax
-call F
-cmp r12, rax
-je L
 pop rbx
 pop r12
 pop rbp
 ret
-nop dword ptr [rax + rax]
-movss xmm0, dword ptr [rbx + 0x1b00]
-movss dword ptr [rbx + 0x1af8], xmm0
-pop rbx
-pop r12
-pop rbp
-ret
```

### изменена: 0x4c1a860 (6457 байт) вызывается из: CDOTA_Ability_Muerta_PartingShot::vfunc#371 | строки: "CreateSoul"; "modifier_muerta_parting_shot_soul_clone"; "<NoAbilityName>"; "invoker_invoke"; "invoker_quas"; "modifier_invoker_quas_instance"; "modifier_invoker_wex_instance"; "invoker_wex"
было: 0x4c191a0 (6457 байт)
- числа в инструкциях: +0xcfe −0xcf5
- инструкций: 1333 → 1333
```diff
@@ -1160,5 +1160,5 @@
 mov rdi, r15
 movdqa xmm5, xmmword ptr [rbp - 0x1f0]
-mov dword ptr [rbp - 0x128], 0xcf5
+mov dword ptr [rbp - 0x128], 0xcfe
 mov qword ptr [rbp - 0x130], rax
 movzx eax, byte ptr [rbp - 0x124]
```

### изменена: 0x4c21aa0 (1788 байт) CDOTA_Ability_Ogre_Magi_Smash::OnSpellStart | строки: "damage"; "duration"; "modifier_ogre_magi_smash_buff"; "Hero_OgreMagi.FireShield.Cast"; "Hero_OgreMagi.FireShield.Target"; "ogre_magi_multicast"; "modifier_ogre_magi_arcana"; "multicast_fireshield_aoe"
было: 0x4c31fe0 (1820 байт)
- числа в инструкциях: −1 −1
- цели вызовов: +0x4c20ff0 −0x3bb1f20
- инструкций: 407 → 399
```diff
@@ -84,5 +84,5 @@
 cmp byte ptr [rax + 0x7e1], 0
 jne L
-lea rsi, [rbp - 0xd4]
+lea rsi, [rbp - 0xd8]
 mov rdi, rax
 call F
@@ -98,5 +98,5 @@
 mov esi, dword ptr [rbp - 0x110]
 mov rdi, rax
-movss xmm0, dword ptr [rbp - 0xd4]
+movss xmm0, dword ptr [rbp - 0xd8]
 call F
 mov esi, dword ptr [rbp - 0x110]
@@ -140,5 +140,5 @@
 mov rdi, qword ptr [rbp - 0x120]
 call F
-mov dword ptr [rbp - 0x128], eax
+mov dword ptr [rbp - 0x120], eax
 call F
 mov ecx, dword ptr [rbp - 0x110]
@@ -146,15 +146,15 @@
 mov edx, 1
 mov rdi, rax
-mov esi, dword ptr [rbp - 0x128]
+mov esi, dword ptr [rbp - 0x120]
 mov qword ptr [rbp - 0x6c], 0x3f800000
 lea eax, [rcx + 1]
 cvtsi2ss xmm0, eax
 lea rcx, [rbp - 0x70]
-mov qword ptr [rbp - 0x120], rcx
+mov qword ptr [rbp - 0x128], rcx
 movss dword ptr [rbp - 0x70], xmm0
 pxor xmm0, xmm0
```
(ещё 99 строк диффа: so-query.py fdiff libserver.so 0x4c21aa0)

### изменена: 0x5322180 (1872 байт) CDOTA_Modifier_XP_Fountain_Aura::OnIntervalThink | строки: "particles/base_static/experience_shrine_ambient_endcap.vpcf"
было: 0x53208c0 (1840 байт)
- константы из данных (числа логики): +300
- числа в инструкциях: +0xffffffff
- прямых вызовов: 28 → 30
- цели вызовов: +0x552e0e0
- инструкций: 442 → 449
```diff
@@ -297,4 +297,11 @@
 call F
 call F
+xor edx, edx
+mov esi, r12d
+mov ecx, 0xffffffff
+movss xmm0, dword ptr [K:300]
+mov rdi, rax
+call F
+call F
 mov esi, r12d
 movsxd r12, r14d
@@ -340,5 +347,5 @@
 cmp rax, rdx
 jne L
-nop dword ptr [rax + rax]
+nop word ptr [rax + rax]
 add r15, 4
 cmp r15, r12
```

### изменена: 0x533a840 (4006 байт) | строки: "dota_item_combined"; "<NoAbilityName>"; "PlayerID"; "itemname"; "itemcost"
было: 0x5338f80 (4022 байт)
- числа в инструкциях: +1 +1
- цели вызовов: −0x5325770
- инструкций: 880 → 880
```diff
@@ -138,8 +138,6 @@
 mov esi, r12d
 call F
+lea rdi, [rbp - 0x50]
 mov dword ptr [rbp - 0x50], eax
-lea rax, [rbp - 0x50]
-mov rdi, rax
-mov qword ptr [rbp - 0xd8], rax
 call F
 test rax, rax
@@ -165,5 +163,5 @@
 mov qword ptr [rbp - 0xc8], rbx
 jmp L
-nop dword ptr [rax]
+nop word ptr [rax + rax]
 movsxd rax, dword ptr [rbp - 0x70]
 cmp eax, dword ptr [rbp - 0x60]
@@ -205,6 +203,5 @@
 xor eax, eax
 jmp L
-nop word ptr cs:[rax + rax]
-nop
+nop dword ptr [rax + rax]
 add rax, 1
 cmp rsi, rax
@@ -300,5 +297,7 @@
 xor r14d, r14d
 nop word ptr cs:[rax + rax]
-nop word ptr [rax + rax]
+nop word ptr cs:[rax + rax]
+nop word ptr cs:[rax + rax]
+nop dword ptr [rax]
 mov rax, qword ptr [rdx]
 mov r8d, 1
```
(ещё 136 строк диффа: so-query.py fdiff libserver.so 0x533a840)

### изменена: 0x5bf4360 (553 байт) вызывается из: CDOTA_ItemSpawner::vfunc#237 | строки: "Spawn"; "../../game/shared/entityspawner.h"; "classname"; "CALLBACKS"
было: 0x5bf29e0 (628 байт)
- числа в инструкциях: −0 −1
- поля объектов: −0x58 −0x50 −0x50 −0x38 −0x48
- цели вызовов: +0x5bf1280
- инструкций: 157 → 136
```diff
@@ -10,17 +10,17 @@
 cmp qword ptr [rdi + 8], 0
 je L
-lea r13, [rbp - 0x50]
+lea r12, [rbp - 0x50]
 mov r15, rdi
 mov dword ptr [rbp - 0x48], 0x4bb
-lea r14, [S:"Spawn"]
-mov rdx, r13
+lea r13, [S:"Spawn"]
+mov rdx, r12
 lea rax, [S:"../../game/shared/entityspawner.h"]
-mov rdi, r14
-mov qword ptr [rbp - 0x40], r14
+mov rdi, r13
+mov qword ptr [rbp - 0x40], r13
 lea rsi, [D]
 mov qword ptr [rbp - 0x50], rax
 call F
 mov rdi, qword ptr [r15 + 8]
-mov rsi, r13
+mov rsi, r12
 mov qword ptr [rbp - 0x50], 0xffffffffc61b1c62
 mov qword ptr [rbp - 0x78], rax
@@ -49,14 +49,14 @@
 mov r8d, dword ptr [r15 + 0x28]
 call F
-mov rbx, rax
+mov r14, rax
 pop rax
-test rbx, rbx
+test r14, r14
 pop rdx
 je L
```
(ещё 108 строк диффа: so-query.py fdiff libserver.so 0x5bf4360)

### изменена: 0x5c011b0 (659 байт) | строки: "CVDataLocalizedToken"; "EMonsterHunterCodexAuthor"
было: 0x5bf4940 (723 байт)
- числа в инструкциях: −0 −0
- поля объектов: −0x48 −0x40
- прямых вызовов: 21 → 16
- инструкций: 183 → 164
```diff
@@ -103,29 +103,16 @@
 test rsi, rsi
 je L
-cmp qword ptr [rsi + 0x48], 0
-je L
-lea rdi, [rsi + 0x48]
-call F
-cmp qword ptr [rbx + 0x40], 0
-je L
-lea rdi, [rbx + 0x40]
-call F
-lea rdi, [rbx + 0x30]
-xor esi, esi
-call F
-lea rdi, [rbx + 0x20]
-xor esi, esi
-call F
-lea rdi, [rbx + 0x10]
-xor esi, esi
-call F
-xor esi, esi
-mov rdi, rbx
+mov rdi, rsi
 call F
 mov esi, 0x78
 mov rdi, rbx
 call F
-jmp L
-nop
+pop rbx
+mov eax, 1
+pop r12
+pop r13
+pop r14
```
(ещё 23 строк диффа: so-query.py fdiff libserver.so 0x5c011b0)

### изменена: 0x5bfc400 (1792 байт) | строки: "classname"; "dota_item_drop"; "ContainedItem"; "origin"; "angles"; "Spawn"; "../../game/shared/entityspawner.h"; "CALLBACKS"
было: 0x5bfacc0 (1179 байт)
- строки: +"Spawn" +"../../game/shared/entityspawner.h" +"../../game/shared/entityspawner.h" +"CALLBACKS"
- числа в инструкциях: +0 +0 +1 +0xffffffffc61b1c62 +0xffffffffc61b1c62 +0xffffffff +0x4bb +0x1ffffffffffff (и ещё 2)
- виртуальные вызовы: +0x118 (слот 35)
- поля объектов: +0x10 +0x10 +0x10 +0x10 +0x31 +0x58
- прямых вызовов: 24 → 36
- цели вызовов: +_ZN16VProfScopeHelperILi0ELb0EE29EnterScopeInternalBudgetFlagsEPKcR24VProfBudgetGroupCallSiteRK18CUtlSourceLocation() +0x6a54a80 +0x6a9a5a0 "<no class info>" +0x6a91950 +0x5bf1280 +0x6a954d0 −0x5bf4360 "Spawn"; "../../game/shared/entityspawner.h"
- инструкций: 260 → 377
```diff
@@ -6,14 +6,14 @@
 mov r14, rsi
 push r13
-mov r13, rdi
 push r12
+mov r12, rdi
 push rbx
-sub rsp, 0xb8
-lea r15, [D]
-movq qword ptr [rbp - 0xe0], xmm0
-movss dword ptr [rbp - 0xd8], xmm1
+sub rsp, 0x108
+lea r13, [D]
+movq qword ptr [rbp - 0x110], xmm0
+movss dword ptr [rbp - 0x108], xmm1
 mov qword ptr [rbp - 0xa0], 0
 mov byte ptr [rbp - 0x5f], 0
-mov rbx, qword ptr [r15]
+mov rbx, qword ptr [r13]
 mov qword ptr [rbp - 0x58], 0
 mov qword ptr [rbp - 0xc0], rax
@@ -24,5 +24,5 @@
 add rbx, 0xd00
 call F
-mov rdi, qword ptr [r15]
+mov rdi, qword ptr [r13]
 mov dword ptr [rbp - 0x94], eax
 call F
@@ -56,10 +56,10 @@
 mov rsi, qword ptr [rbp - 0xb0]
 mov edx, 3
-mov r12, rax
+mov r15, rax
 mov rdi, rax
```
(ещё 396 строк диффа: so-query.py fdiff libserver.so 0x5bfc400)

### изменена: 0x5c01450 (3671 байт) | строки: "m_strLocHeroName"; "Double-save to Member '%s'"; "m_strLocFieldNotes"; "m_strLocNonHeroName"; "m_strLocPersonaFieldNotes"; "m_bAlwaysUnlocked"; "m_bIsHero"; "m_bIsForeword"
было: 0x5bff810 (3943 байт)
- строки: −"Double-save to Member '%s'" −"Double-save to Member '%s'" −"m_strNonHeroStickerDisplayName" −"m_strNonHeroStickerDisplayName" −"m_strNonHeroStickerName" −"m_strNonHeroStickerName"
- числа в инструкциях: +0xf550d329 +0xc93a46ef −0x1b −0x1b −0xfffffffff550d329 −0xffffffffc93a46ef
- поля объектов: −0x120 −0x120 −0x120 −0x120 −0x48 −0x40
- прямых вызовов: 94 → 88
- цели вызовов: +0x5bf6300 "Double-save to Member '%s'"
- инструкций: 818 → 769
```diff
@@ -258,11 +258,13 @@
 mov rdi, r12
 call F
-lea rsi, [r13 + 0x40]
-mov rdi, rbx
-call F
-test al, al
-jne L
-lea rsi, [r13 + 0x48]
-mov rdi, rbx
+lea r12, [r13 + 0x40]
+mov rdi, rbx
+mov rsi, r12
+call F
+test al, al
+jne L
+lea r12, [r13 + 0x48]
+mov rdi, rbx
+mov rsi, r12
 call F
 test al, al
@@ -547,5 +549,5 @@
 pop rbp
 ret
-nop
+nop dword ptr [rax]
 mov rdi, qword ptr [rbx + 0x120]
 mov rsi, r12
@@ -556,4 +558,5 @@
 mov r14, rax
 jmp L
+nop dword ptr [rax + rax]
 mov rdi, qword ptr [rbx + 0x120]
 mov rsi, r12
```
(ещё 96 строк диффа: so-query.py fdiff libserver.so 0x5c01450)

### изменена: 0x5c02c70 (857 байт) | строки: "m_eCategory"; "Double-save to Member '%s'"; "m_unActionID"; "m_strLocName"
было: 0x5c01140 (842 байт)
- числа в инструкциях: +0 +0 +0
- поля объектов: +0x140 +0x148
- цели вызовов: −0x5bf03e0
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
```
(ещё 139 строк диффа: so-query.py fdiff libserver.so 0x5c02c70)

### изменена: 0x5c03fe0 (442 байт) | строки: "npc_dota_observer_wards"; "npc_dota_sentry_wards"
было: 0x5c024a0 (218 байт)
- числа в инструкциях: +1 +0xffffffff
- виртуальные вызовы: +0x868 (слот 269) +0x878 (слот 271)
- поля объектов: +0x14 +0xb78
- прямых вызовов: 5 → 8
- инструкций: 61 → 115
```diff
@@ -1,30 +1,36 @@
 push rbp
+mov rbp, rsp
+push r14
+mov r14, rdi
+push r13
+push r12
+sub rsp, 0x18
+test rsi, rsi
+movzx eax, byte ptr [rdi + 0x14]
+je L
+cmp byte ptr [rsi + 0x5d1], 3
+jne L
+test al, al
+mov r12, rsi
+jne L
+mov rax, qword ptr [r14]
 mov edx, 1
-mov rbp, rsp
-push r12
-mov r12, rdi
-push rbx
-mov rbx, rsi
-sub rsp, 0x10
-mov rax, qword ptr [rdi]
 mov rdi, qword ptr [rax + 8]
 mov rax, qword ptr [rdi]
 call qword ptr [rax + 0xb78]
-test rbx, rbx
-je L
-cmp byte ptr [rbx + 0x5d1], 3
-jne L
-mov rax, qword ptr [r12]
+mov rax, qword ptr [r14]
```
(ещё 106 строк диффа: so-query.py fdiff libserver.so 0x5c03fe0)

### изменена: 0x5c04540 (931 байт) | строки: "npc_dota_mutation_pocket_roshan"
было: 0x5c02920 (1007 байт)
- числа в инструкциях: −-1 −0x18 −0
- поля объектов: −0x13b0 −0x152c
- цели вызовов: +0x4babff0 −0x5059ff0
- инструкций: 241 → 223
```diff
@@ -212,22 +212,4 @@
 xor ebx, ebx
 jmp L
-movzx eax, word ptr [r14 + 0x152c]
-cmp ax, -1
-je L
-mov rdx, qword ptr [r14 + 0x13b0]
-mov rdx, qword ptr [rdx + rax*8]
-mov rax, qword ptr [rdx + 8]
-movsxd rdx, dword ptr [rdx]
-lea rdx, [rdx + rdx*2]
-lea rdx, [rax + rdx*8]
-cmp rax, rdx
-jne L
-jmp L
-nop dword ptr [rax]
-add rax, 0x18
-cmp rdx, rax
-je L
-cmp qword ptr [rax], 0
-je L
 lea rdx, [D]
 xor ecx, ecx
```

### изменена: 0x5c16650 (781 байт)
было: 0x5c14a50 (837 байт)
- числа в инструкциях: −-1 −-2 −9 −0x3f −0x1ff −0x70
- поля объектов: −0x10 −0x198c −0x198c
- прямых вызовов: 16 → 17
- цели вызовов: +0x3ba8c00
- инструкций: 197 → 181
```diff
@@ -18,14 +18,14 @@
 test al, al
 jne L
-mov esi, dword ptr [rbx + 0xd3c]
-test esi, 0x10000
+mov r14d, dword ptr [rbx + 0xd3c]
+test r14d, 0x10000
 jne L
 mov ecx, dword ptr [rbx + 0x179c]
 cmp ecx, -1
 je L
-mov rdi, qword ptr [D]
-test rdi, rdi
+cmp ecx, -2
+mov rsi, qword ptr [D]
 je L
-cmp ecx, -2
+test rsi, rsi
 je L
 movzx eax, word ptr [rbx + 0x179c]
@@ -33,5 +33,5 @@
 shr rdx, 9
 and edx, 0x3f
-mov rdx, qword ptr [rdi + rdx*8]
+mov rdx, qword ptr [rsi + rdx*8]
 test rdx, rdx
 je L
@@ -51,5 +51,5 @@
 call F
 jmp L
-nop dword ptr [rax]
+nop dword ptr [rax + rax]
 mov edi, 0x48
 call F
```
(ещё 38 строк диффа: so-query.py fdiff libserver.so 0x5c16650)

### изменена: 0x5c1bf10 (2189 байт) CDOTA_Lane_Creep_BehaviorController::vfunc#3
было: 0x5c1a350 (2077 байт)
- константы из данных (числа логики): +300
- прямых вызовов: 41 → 44
- инструкций: 462 → 488
```diff
@@ -234,8 +234,8 @@
 cmp byte ptr [rbx + 0x17a0], 0
 jne L
-movss xmm0, dword ptr [rbp - 0x7c]
-movss xmm1, dword ptr [rbp - 0x78]
-mulss xmm0, dword ptr [rbp - 0x8c]
-mulss xmm1, dword ptr [rbp - 0x88]
+movss xmm0, dword ptr [rbp - 0x78]
+movss xmm1, dword ptr [rbp - 0x7c]
+mulss xmm0, dword ptr [rbp - 0x88]
+mulss xmm1, dword ptr [rbp - 0x8c]
 addss xmm0, xmm1
 movss xmm1, dword ptr [rbp - 0x80]
@@ -399,11 +399,37 @@
 cmp byte ptr [r15 + 0x19], 0
 jne L
+lea r14, [r15 + 0x1c]
+mov rdi, rbx
+call F
+mov rdi, r14
+movss xmm7, dword ptr [rax + 4]
+mov r13d, dword ptr [rax]
+movss dword ptr [rbp - 0x98], xmm7
+call F
+test rax, rax
+mov rdi, rax
+je L
+mov rdi, qword ptr [rax]
+call F
+movss xmm1, dword ptr [rbp - 0x98]
+movd xmm0, r13d
+subss xmm1, dword ptr [rax + 4]
+subss xmm0, dword ptr [rax]
+mulss xmm1, xmm1
```
(ещё 19 строк диффа: so-query.py fdiff libserver.so 0x5c1bf10)

### изменена: 0x5c60ff0 (3924 байт) | строки: "m_flLastSpawnTime"; "float"; "float32"; "m_flNextSpawnTime"; "m_bNextRuneIsWater"; "bool"; "CDOTA_Item_RuneSpawner_Powerup"; "15CNetworkVarBaseIbN30CDOTA_Item_RuneSpawner_Powerup29NetworkVar_m_bNextRuneIsWa"
было: 0x5c5f3b0 (4220 байт)
- числа в инструкциях: −0 −0 −0 −0 −0 −0 −0 −0 (и ещё 18)
- поля объектов: −0x10 −0x120 −0x38 −0x58 −0x68 −0x78 −0x88 −0x18 −0x20 −0x40 −0x48 −0x50 (и ещё 22)
- прямых вызовов: 131 → 132
- инструкций: 911 → 874
```diff
@@ -252,7 +252,7 @@
 mov rdi, rbx
 call F
-lea r13, [r12 + 0x18]
+lea r15, [r12 + 0x18]
 lea rsi, [S:"float"]
-mov rdi, r13
+mov rdi, r15
 call F
 mov rax, qword ptr [K:0x00000bc400000004]
@@ -262,15 +262,15 @@
 test al, al
 je L
-mov r14, qword ptr [D]
-test r14, r14
-je L
-mov rdi, r14
+mov r13, qword ptr [D]
+test r13, r13
+je L
+mov rdi, r13
 call F
 test eax, eax
 jg L
-xor r15d, r15d
+xor r14d, r14d
 mov rsi, qword ptr [rbp - 0x70]
 mov qword ptr [rbp - 0x50], 0
-lea r14, [D]
+lea r13, [D]
 mov rdi, qword ptr [rbp - 0x68]
 call F
@@ -279,5 +279,5 @@
 mov rdi, qword ptr [rbp - 0x58]
```
(ещё 656 строк диффа: so-query.py fdiff libserver.so 0x5c60ff0)

### изменена: 0x61c0b40 (288 байт) CDOTA_BaseNPC::vfunc#430, CDOTA_Unit_Announcer::vfunc#430, CDOTA_Unit_CustomGameAnnouncer::vfunc#430
было: 0x61befe0 (1363 байт)
- числа в инструкциях: −1 −1 −1 −1 −1 −1 −1 −1 (и ещё 32)
- прямых вызовов: 4 → 3
- инструкций: 376 → 91
```diff
@@ -90,287 +90,2 @@
 pop rbp
 ret
-mov rax, rsi
-sub rax, rdi
-cmp rax, 0x40
-jle L
-push rbp
-mov rbp, rsp
-push r14
-push r13
-mov r13, rdx
-mov rdx, rax
-sar rax, 3
-sar rdx, 2
-test r13, r13
-push r12
-mov r12, rdi
-push rbx
-je L
-lea r8, [r12 + rax*4]
-mov ecx, dword ptr [r12 + 4]
-sub r13, 1
-mov eax, dword ptr [r8]
-lea rbx, [r12 + 4]
-mov edi, dword ptr [rsi - 4]
-mov edx, dword ptr [r12]
-cmp ecx, eax
-jge L
-cmp eax, edi
-jl L
-cmp ecx, edi
-jl L
-mov eax, dword ptr [r12 + 4]
```
(ещё 254 строк диффа: so-query.py fdiff libserver.so 0x61c0b40)

### изменена: 0x61d3600 (1508 байт) вызывается из: CDOTA_BaseNPC::vfunc#399 | строки: "N/A"
было: 0x61d1a80 (1492 байт)
- числа в инструкциях: +1
- поля объектов: +0xc −0x1cf0 −0x1cf0 −0x1cf0
- прямых вызовов: 22 → 23
- инструкций: 317 → 322
```diff
@@ -18,5 +18,5 @@
 je L
 movsxd rsi, dword ptr [rdi + 0x1cf0]
-mov r14, rdi
+mov r15, rdi
 movaps xmm2, xmm0
 test esi, esi
@@ -55,5 +55,5 @@
 movss dword ptr [rbp - 0x44], xmm2
 xor esi, esi
-xor r15d, r15d
+xor r14d, r14d
 mov rax, qword ptr [rdi]
 call qword ptr [rax + 0x368]
@@ -83,15 +83,15 @@
 lea rdi, [D]
 call F
-mov esi, dword ptr [r14 + 0x1cf0]
-test esi, esi
+mov eax, dword ptr [r15 + 0x1cf0]
+test eax, eax
 jle L
 nop dword ptr [rax]
-mov rax, qword ptr [r14 + 0x1cf8]
-lea r12, [r15 + r15*4]
-lea r13, [r12*4]
-add rax, r13
+mov rax, qword ptr [r15 + 0x1cf8]
+lea r13, [r14 + r14*4]
+lea r12, [r13*4]
+add rax, r12
 cmp byte ptr [rax + 8], 0
 mov edx, dword ptr [rax + 4]
-jne L
```
(ещё 279 строк диффа: so-query.py fdiff libserver.so 0x61d3600)

### изменена: 0x61e9010 (1404 байт) | строки: "../../../_build_/game/server/_vpc_server_dota/unity/linuxsteamrt64/_proto_/../_s"; "AttackDamageType"; "TeamName"; "UnitRelationshipClass"; "CNetworkTransmitComponent::StateChanged(%s) @%s:%d"; "DOTA_NPC_UNIT_RELATIONSHIP_TYPE_DEFAULT"; "DOTA_NPC_UNIT_RELATIONSHIP_TYPE_HERO"; "DOTA_NPC_UNIT_RELATIONSHIP_TYPE_BUILDING"
было: 0x61e7490 (1404 байт)
- константы из данных (числа логики): +0xffffffff000032b9 −0xffffffff000032bd
- числа в инструкциях: +0x32b9 −0x32bd
- инструкций: 289 → 289
```diff
@@ -73,5 +73,5 @@
 mov qword ptr [rbp - 0x180], 0
 mov rax, qword ptr [rbx]
-mov rdx, qword ptr [K:0xffffffff000032bd]
+mov rdx, qword ptr [K:0xffffffff000032b9]
 mov qword ptr [rbp - 0x178], 0
 movdqa xmm3, xmmword ptr [rbp - 0x1a0]
@@ -119,5 +119,5 @@
 mov rdi, r13
 mov rcx, rax
-mov r8d, 0x32bd
+mov r8d, 0x32b9
 test rdx, rdx
 cmove rdx, r12
```

### изменена: 0x61f2e02 (74 байт) | строки: "iSlot == -1"
было: 0x61f1282 (74 байт)
- числа в инструкциях: +0x2a88 −0x2a8c
- инструкций: 13 → 13
```diff
@@ -1,5 +1,5 @@
 lea rax, [S:"iSlot == -1"]
 movdqa xmm3, xmmword ptr [rbp - 0x170]
-mov dword ptr [rbp - 0x118], 0x2a8c
+mov dword ptr [rbp - 0x118], 0x2a88
 mov qword ptr [rbp - 0x120], rax
 movzx eax, byte ptr [rbp - 0x114]
```

### изменена: 0x61f2e4d (105 байт) | строки: "<NoAbilityName>"; "iSlotReplace == -1"
было: 0x61f12cd (105 байт)
- числа в инструкциях: +0x2a91 −0x2a95
- инструкций: 19 → 19
```diff
@@ -7,5 +7,5 @@
 lea rax, [S:"iSlotReplace == -1"]
 movdqa xmm4, xmmword ptr [rbp - 0x170]
-mov dword ptr [rbp - 0x118], 0x2a95
+mov dword ptr [rbp - 0x118], 0x2a91
 mov qword ptr [rbp - 0x120], rax
 movzx eax, byte ptr [rbp - 0x114]
```

### изменена: 0x6211da0 (1313 байт) | строки: "StartGesture"; "iSlot >= 0"
было: 0x6210220 (1313 байт)
- числа в инструкциях: +0x361f −0x3623
- инструкций: 293 → 293
```diff
@@ -276,5 +276,5 @@
 movq xmm0, qword ptr [D]
 movq xmm6, rax
-mov dword ptr [rbp - 0xa8], 0x3623
+mov dword ptr [rbp - 0xa8], 0x361f
 lea rax, [S:"iSlot >= 0"]
 mov qword ptr [rbp - 0xb0], rax
```

### изменена: 0x6232c20 (2143 байт) | строки: "../../../_build_/game/server/_vpc_server_dota/unity/linuxsteamrt64/_proto_/../_s"; "CDOTA_BaseNPC::CheckForCollisionsWithNPCs"; "CheckForCollisionsWithNPCs"
было: 0x62310a0 (2143 байт)
- числа в инструкциях: +0x399e −0x39a2
- инструкций: 457 → 457
```diff
@@ -21,5 +21,5 @@
 lea rax, [S:"CheckForCollisionsWithNPCs"]
 mov byte ptr [rbp - 0x208], r8b
-mov dword ptr [rbp - 0x1c8], 0x39a2
+mov dword ptr [rbp - 0x1c8], 0x399e
 mov qword ptr [rbp - 0x1c0], rax
 call F
```

### изменена: 0x6280b60 (312 байт)
было: 0x627efe0 (339 байт)
- числа в инструкциях: −1 −1
- инструкций: 104 → 95
```diff
@@ -1,28 +1,22 @@
 push rbp
+pxor xmm1, xmm1
 mov rbp, rsp
 push r14
 push r13
-mov r13d, edx
+mov r13d, ecx
+mov ecx, 1
 push r12
+mov r12d, edx
 push rbx
 sub rsp, 0x10
 lea rax, [D]
-mov rax, qword ptr [rax + 8]
-movzx eax, byte ptr [rax + 0x58]
-xor eax, 1
-test ecx, ecx
-sete dl
-or eax, edx
+ucomiss xmm0, xmm1
+mov rdx, qword ptr [rax + 8]
+setp al
+cmovne eax, ecx
+and al, byte ptr [rdx + 0x58]
+je L
 test rsi, rsi
-sete dl
-or eax, edx
-cmp al, 1
-je L
-pxor xmm1, xmm1
-ucomiss xmm0, xmm1
-mov edx, 1
```
(ещё 60 строк диффа: so-query.py fdiff libserver.so 0x6280b60)

### изменена: 0x6280ca0 (583 байт)
было: 0x627f140 (580 байт)
- числа в инструкциях: +0
- инструкций: 154 → 150
```diff
@@ -16,6 +16,12 @@
 mov rbx, rdx
 xor r13d, r13d
-jmp L
-nop word ptr cs:[rax + rax]
+nop dword ptr [rax]
+mov r15, r13
+movss xmm2, dword ptr [rbp - 0x44]
+shl r15, 5
+add r15, qword ptr [rbx + 8]
+ucomiss xmm2, dword ptr [K:3.402823e+38]
+jp L
+jne L
 movss xmm3, dword ptr [rbp - 0x4c]
 mulss xmm3, dword ptr [r15 + 8]
@@ -46,9 +52,6 @@
 call F
 lea rax, [D]
-mov r14d, dword ptr [rbp - 0x38]
-mov rdx, qword ptr [rax + 8]
-test r14d, r14d
-setne al
-and al, byte ptr [rdx + 0x58]
+mov rax, qword ptr [rax + 8]
+cmp byte ptr [rax + 0x58], 0
 je L
 movss xmm5, dword ptr [rbp - 0x48]
@@ -59,51 +62,22 @@
 cmovne eax, edx
 test al, al
-jne L
-add r13, 1
-cmp dword ptr [rbx], r13d
-jle L
```
(ещё 111 строк диффа: so-query.py fdiff libserver.so 0x6280ca0)

### изменена: 0x6281c40 (6179 байт)
было: 0x6280100 (6453 байт)
- числа в инструкциях: +1 −0 −0 −4 −4 −0x10 −0x3fffffff −0x3fffffff −0x3fffffff (и ещё 6)
- поля объектов: −0xc −0xc −0xc −0xc −0xc
- прямых вызовов: 86 → 83
- цели вызовов: −UtlVectorMemory_CalcNewAllocationCount() −UtlVectorMemory_Alloc() −UtlVectorMemory_FailedAllocation()
- инструкций: 1325 → 1251
```diff
@@ -124,14 +124,12 @@
 mov qword ptr [rbp - 0x358], 0
 mov dword ptr [rbp - 0x34c], 0
-lea rax, [rbp - 0x2b0]
 xor r12d, r12d
 xor r14d, r14d
-mov qword ptr [rbp - 0x308], r10
 mov dword ptr [rbp - 0x350], 0
 mov dword ptr [rbp - 0x310], 0
-mov qword ptr [rbp - 0x370], rax
+mov qword ptr [rbp - 0x308], r10
 mov qword ptr [rbp - 0x328], r11
 jmp L
-nop dword ptr [rax + rax]
+nop dword ptr [rax]
 mov rax, qword ptr [r13]
 lea rcx, [T]
@@ -164,5 +162,4 @@
 mov rdi, qword ptr [rbx]
 mov esi, r15d
-mov dword ptr [rbp - 0x150], r15d
 call F
 test al, al
@@ -170,5 +167,5 @@
 mov r15d, dword ptr [rbp - 0x270]
 jmp L
-nop word ptr [rax + rax]
+nop dword ptr [rax]
 mov qword ptr [rbp - 0x310], rdx
 mov rdi, rsi
@@ -342,11 +339,9 @@
 cmp r8, rax
 jne L
-mov eax, dword ptr [rbp - 0x350]
```
(ещё 452 строк диффа: so-query.py fdiff libserver.so 0x6281c40)

### изменена: 0x628c620 (6645 байт) | строки: "CNetworkTransmitComponent::StateChanged(%s) @%s:%d"; "Hero_Melee.Miss"; "modifier_backdoor_protection_active"; "Damage.Building.Protected"; "%s.Attack"; "Damage.Building"; "arcana_melee"; "particles/econ/attack/attack_modifier_empty.vpcf"
было: 0x628aae0 (6615 байт)
- прямых вызовов: 79 → 80
- цели вызовов: +0x4420970
- инструкций: 1240 → 1246
```diff
@@ -1217,4 +1217,10 @@
 jne L
 jmp L
+mov rsi, rdi
+mov qword ptr [rbp - 0x2c0], rdi
+call F
+mov rdi, qword ptr [rbp - 0x2c0]
+test al, al
+je L
 mov rax, qword ptr [D]
 cmp dword ptr [rax + 0x58], 1
```

### изменена: 0x62e45c0 (11079 байт) CDOTA_BaseNPC_Hero::vfunc#129, CDOTA_Unit_Hero_AncientApparition::vfunc#129, CDOTA_Unit_Hero_AntiMage::vfunc#129 | строки: "DOTAMusic.Death"; "item_travel_boots"; "item_travel_boots_2"; "duration"; "modifier_rune_doubledamage"; "modifier_rune_arcane"; "modifier_rune_haste"; "modifier_rune_shield"
было: 0x62e2a80 (11169 байт)
- виртуальные вызовы: +0x538 (слот 167) +0x538 (слот 167)
- поля объектов: −0x538 −0x538
- прямых вызовов: 306 → 304
- цели вызовов: −CDOTA_BaseNPC::vfunc#167 −0x5653990
- инструкций: 2275 → 2258
```diff
@@ -42,5 +42,5 @@
 movss xmm0, dword ptr [K:500]
 mov rdi, rax
-mov qword ptr [rbp - 0x500], rax
+mov qword ptr [rbp - 0x508], rax
 call F
 movabs rax, 0xffffffff00000000
@@ -112,5 +112,5 @@
 mov rsi, rbx
 mov rdi, rcx
-mov qword ptr [rbp - 0x508], rcx
+mov qword ptr [rbp - 0x500], rcx
 call F
 mov rax, qword ptr [rbp - 0x4d8]
@@ -288,5 +288,5 @@
 mov esi, eax
 call F
-mov rsi, qword ptr [rbp - 0x508]
+mov rsi, qword ptr [rbp - 0x500]
 mov rdi, r15
 movss xmm5, dword ptr [rbp - 0x4e0]
@@ -530,5 +530,5 @@
 mov rdi, rax
 call F
-mov rdi, qword ptr [rbp - 0x500]
+mov rdi, qword ptr [rbp - 0x508]
 mov rsi, r15
 call F
@@ -594,5 +594,5 @@
 nop dword ptr [rax]
 lea rax, [D]
-mov qword ptr [rbp - 0x500], rax
+mov qword ptr [rbp - 0x508], rax
 jmp L
```
(ещё 311 строк диффа: so-query.py fdiff libserver.so 0x62e45c0)

### изменена: 0x3ec3f00 (1578 байт) | строки: "uint8"; "CUtlVector"; "CNetworkUtlVectorBase"; "%s< %s%s >"; "21CNetworkUtlVectorBaseIhN24CBaseAnimGraphController42NetworkVar_m_SerializePose"; "10CUtlVectorIhi28CNetworkUtlVector_MemoryTypeIhLin1EEE"
- код тот же, но вызывает другую функцию: было 0x3eacaf0, стало 0x3eacd70

### изменена: 0x3edc1d0 (6642 байт) | строки: "m_Handle"; "ModelConfigHandle_t"; "uint32"; "m_Name"; "string_t"; "CUtlSymbolLarge"; "m_AssociatedEntities"; "CNetworkUtlVectorBase< CHandle< CBaseModelEntity >, NetworkVar_m_AssociatedEntit"
- код тот же, но вызывает другую функцию: было 0x3eae760, стало 0x3eae9e0

### изменена: 0x448d490 (63 байт)
- код тот же, но вызывает другую функцию: было 0x445f590, стало 0x445f830

### изменена: 0x448d4d0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x445f560, стало 0x445f7d0

### изменена: 0x448d510 (63 байт)
- код тот же, но вызывает другую функцию: было 0x445f500, стало 0x445f7a0

### изменена: 0x448d550 (63 байт)
- код тот же, но вызывает другую функцию: было 0x445f4d0, стало 0x445f770

### изменена: 0x448d590 (63 байт)
- код тот же, но вызывает другую функцию: было 0x445f4a0, стало 0x445f740

### изменена: 0x448d5d0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x445f470, стало 0x445f710

### изменена: 0x448d610 (63 байт)
- код тот же, но вызывает другую функцию: было 0x445f440, стало 0x445f6e0

### изменена: 0x448d650 (63 байт)
- код тот же, но вызывает другую функцию: было 0x445f410, стало 0x445f6b0

### изменена: 0x448d690 (63 байт)
- код тот же, но вызывает другую функцию: было 0x445f3e0, стало 0x445f680

### изменена: 0x448d6d0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x445f3b0, стало 0x445f650

### изменена: 0x448d710 (63 байт)
- код тот же, но вызывает другую функцию: было 0x445f380, стало 0x445f600

### изменена: 0x448d750 (63 байт)
- код тот же, но вызывает другую функцию: было 0x445f330, стало 0x445f5d0

### изменена: 0x448d790 (63 байт)
- код тот же, но вызывает другую функцию: было 0x445f300, стало 0x445f590

### изменена: 0x448d7d0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x445f2c0, стало 0x445f560

### изменена: 0x448d810 (63 байт)
- код тот же, но вызывает другую функцию: было 0x445f290, стало 0x445f4e0

### изменена: 0x448d850 (63 байт)
- код тот же, но вызывает другую функцию: было 0x445f210, стало 0x445f480

### изменена: 0x448d890 (63 байт)
- код тот же, но вызывает другую функцию: было 0x445f1b0, стало 0x445f370

### изменена: 0x448d8d0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x445f0a0, стало 0x445f340

### изменена: 0x448d910 (63 байт)
- код тот же, но вызывает другую функцию: было 0x445f070, стало 0x445f2c0

### изменена: 0x448d950 (63 байт)
- код тот же, но вызывает другую функцию: было 0x445eff0, стало 0x445f290

### изменена: 0x448d990 (63 байт)
- код тот же, но вызывает другую функцию: было 0x445efc0, стало 0x445f250

### изменена: 0x448d9d0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x445ef80, стало 0x445f220

### изменена: 0x448da10 (63 байт)
- код тот же, но вызывает другую функцию: было 0x445ef50, стало 0x445f1b0

### изменена: 0x448da50 (63 байт)
- код тот же, но вызывает другую функцию: было 0x445eee0, стало 0x445f170

### изменена: 0x448da90 (63 байт)
- код тот же, но вызывает другую функцию: было 0x445eea0, стало 0x445f140

### изменена: 0x448dad0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x445ee70, стало 0x445f080

### изменена: 0x448db10 (63 байт)
- код тот же, но вызывает другую функцию: было 0x445edb0, стало 0x445f050

### изменена: 0x448db50 (63 байт)
- код тот же, но вызывает другую функцию: было 0x445ed80, стало 0x445f010

### изменена: 0x448db90 (63 байт)
- код тот же, но вызывает другую функцию: было 0x445ed40, стало 0x445efe0

### изменена: 0x448dbd0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x445ed10, стало 0x445ef70

### изменена: 0x448dc10 (63 байт)
- код тот же, но вызывает другую функцию: было 0x445eca0, стало 0x445ef30

### изменена: 0x448dc50 (63 байт)
- код тот же, но вызывает другую функцию: было 0x445ec60, стало 0x445ef00

### изменена: 0x448dc90 (63 байт)
- код тот же, но вызывает другую функцию: было 0x445ec30, стало 0x445eed0

### изменена: 0x448dcd0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x445ec00, стало 0x445eea0

### изменена: 0x448dd10 (63 байт)
- код тот же, но вызывает другую функцию: было 0x445ebd0, стало 0x445ee20

### изменена: 0x448dd50 (63 байт)
- код тот же, но вызывает другую функцию: было 0x445eb50, стало 0x445edd0

### изменена: 0x448dd90 (63 байт)
- код тот же, но вызывает другую функцию: было 0x445eb00, стало 0x445eda0

### изменена: 0x448ddd0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x445ead0, стало 0x445ed10

### изменена: 0x448de10 (63 байт)
- код тот же, но вызывает другую функцию: было 0x445ea40, стало 0x445ece0

### изменена: 0x448de50 (63 байт)
- код тот же, но вызывает другую функцию: было 0x445ea10, стало 0x445ecb0

### изменена: 0x448de90 (63 байт)
- код тот же, но вызывает другую функцию: было 0x445e9e0, стало 0x445ec20

### изменена: 0x448ded0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x445e950, стало 0x445ebf0

### изменена: 0x448df10 (63 байт)
- код тот же, но вызывает другую функцию: было 0x445e920, стало 0x445ebb0

### изменена: 0x448df50 (63 байт)
- код тот же, но вызывает другую функцию: было 0x445e8e0, стало 0x445eb80

### изменена: 0x448df90 (63 байт)
- код тот же, но вызывает другую функцию: было 0x445e8b0, стало 0x445eb40

### изменена: 0x448dfd0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x445e870, стало 0x445eb10

### изменена: 0x448e010 (63 байт)
- код тот же, но вызывает другую функцию: было 0x445e840, стало 0x445eae0

### изменена: 0x448e050 (63 байт)
- код тот же, но вызывает другую функцию: было 0x445e810, стало 0x445eaa0

### изменена: 0x448e090 (63 байт)
- код тот же, но вызывает другую функцию: было 0x445e7d0, стало 0x445ea60

### изменена: 0x448e0d0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x445e790, стало 0x445ea30

### изменена: 0x448e110 (63 байт)
- код тот же, но вызывает другую функцию: было 0x445e760, стало 0x445ea00

### изменена: 0x448e150 (63 байт)
- код тот же, но вызывает другую функцию: было 0x445e730, стало 0x445e9c0

### изменена: 0x448e190 (63 байт)
- код тот же, но вызывает другую функцию: было 0x445e6f0, стало 0x445e920

### изменена: 0x448e1d0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x445e650, стало 0x445e8f0

### изменена: 0x448e210 (63 байт)
- код тот же, но вызывает другую функцию: было 0x445e620, стало 0x445e8c0

### изменена: 0x448e250 (63 байт)
- код тот же, но вызывает другую функцию: было 0x445e5f0, стало 0x445e890

### изменена: 0x448e290 (63 байт)
- код тот же, но вызывает другую функцию: было 0x445e5c0, стало 0x445e830

### изменена: 0x448e2d0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x445e560, стало 0x445e7e0

### изменена: 0x448e310 (63 байт)
- код тот же, но вызывает другую функцию: было 0x445e510, стало 0x445e7b0

### изменена: 0x448e350 (63 байт)
- код тот же, но вызывает другую функцию: было 0x445e4e0, стало 0x445e740

### изменена: 0x448e390 (63 байт)
- код тот же, но вызывает другую функцию: было 0x445e470, стало 0x445e710

### изменена: 0x448e3d0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x445e440, стало 0x445e6d0

### изменена: 0x448e410 (63 байт)
- код тот же, но вызывает другую функцию: было 0x445e400, стало 0x445e690

### изменена: 0x448e450 (63 байт)
- код тот же, но вызывает другую функцию: было 0x445e3c0, стало 0x445e660

### изменена: 0x448e490 (63 байт)
- код тот же, но вызывает другую функцию: было 0x445e390, стало 0x445e630

### изменена: 0x448e4d0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x445e360, стало 0x445e5c0

### изменена: 0x448e510 (63 байт)
- код тот же, но вызывает другую функцию: было 0x445e2f0, стало 0x445e530

### изменена: 0x448e550 (63 байт)
- код тот же, но вызывает другую функцию: было 0x445e260, стало 0x445e4c0

### изменена: 0x448e590 (63 байт)
- код тот же, но вызывает другую функцию: было 0x445e1f0, стало 0x445e480

### изменена: 0x448e5d0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x445e1b0, стало 0x445e450

### изменена: 0x448e610 (63 байт)
- код тот же, но вызывает другую функцию: было 0x445e180, стало 0x445e410

### изменена: 0x448e650 (63 байт)
- код тот же, но вызывает другую функцию: было 0x445e140, стало 0x445e3d0

### изменена: 0x448e690 (63 байт)
- код тот же, но вызывает другую функцию: было 0x445e100, стало 0x445e380

### изменена: 0x448e6d0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x445e0b0, стало 0x445e350

### изменена: 0x448e710 (63 байт)
- код тот же, но вызывает другую функцию: было 0x445e080, стало 0x445e310

### изменена: 0x448e750 (63 байт)
- код тот же, но вызывает другую функцию: было 0x445e040, стало 0x445e290

### изменена: 0x448e790 (63 байт)
- код тот же, но вызывает другую функцию: было 0x445dfc0, стало 0x445e240

### изменена: 0x448e7d0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x445df70, стало 0x445e210

### изменена: 0x448e810 (63 байт)
- код тот же, но вызывает другую функцию: было 0x445df40, стало 0x445e1e0

### изменена: 0x448e850 (63 байт)
- код тот же, но вызывает другую функцию: было 0x445df10, стало 0x445e1b0

### изменена: 0x448e890 (63 байт)
- код тот же, но вызывает другую функцию: было 0x445dee0, стало 0x445e170

### изменена: 0x448e8d0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x445dea0, стало 0x445e140

### изменена: 0x448e910 (63 байт)
- код тот же, но вызывает другую функцию: было 0x445de70, стало 0x445e110

### изменена: 0x448e950 (63 байт)
- код тот же, но вызывает другую функцию: было 0x445de40, стало 0x445e0e0

### изменена: 0x448e990 (63 байт)
- код тот же, но вызывает другую функцию: было 0x445de10, стало 0x445e050

### изменена: 0x448e9d0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x445dd80, стало 0x445e010

### изменена: 0x448ea10 (63 байт)
- код тот же, но вызывает другую функцию: было 0x445dd40, стало 0x445dfe0

### изменена: 0x448ea50 (63 байт)
- код тот же, но вызывает другую функцию: было 0x445dd10, стало 0x445dfb0

### изменена: 0x448ea90 (63 байт)
- код тот же, но вызывает другую функцию: было 0x445dce0, стало 0x445df70

### изменена: 0x448ead0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x445dca0, стало 0x445df40

### изменена: 0x448eb10 (63 байт)
- код тот же, но вызывает другую функцию: было 0x445dc70, стало 0x445df10

### изменена: 0x448eb50 (63 байт)
- код тот же, но вызывает другую функцию: было 0x445dc40, стало 0x445dee0

### изменена: 0x448eb90 (63 байт)
- код тот же, но вызывает другую функцию: было 0x445dc10, стало 0x445ddd0

### изменена: 0x448ebd0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x445db00, стало 0x445dda0

### изменена: 0x448ec10 (63 байт)
- код тот же, но вызывает другую функцию: было 0x445dad0, стало 0x445dd70

### изменена: 0x448ec50 (63 байт)
- код тот же, но вызывает другую функцию: было 0x445daa0, стало 0x445dd40

### изменена: 0x448ec90 (63 байт)
- код тот же, но вызывает другую функцию: было 0x445da70, стало 0x445dcd0

### изменена: 0x448ecd0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x445da00, стало 0x445dca0

### изменена: 0x448ed10 (63 байт)
- код тот же, но вызывает другую функцию: было 0x445d9d0, стало 0x445dc10

### изменена: 0x448ed50 (63 байт)
- код тот же, но вызывает другую функцию: было 0x445d940, стало 0x445dbe0

### изменена: 0x448ed90 (63 байт)
- код тот же, но вызывает другую функцию: было 0x445d910, стало 0x445dbb0

### изменена: 0x448edd0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x445d8e0, стало 0x445db70

### изменена: 0x448ee10 (63 байт)
- код тот же, но вызывает другую функцию: было 0x445d8a0, стало 0x445dad0

### изменена: 0x448ee50 (63 байт)
- код тот же, но вызывает другую функцию: было 0x445d800, стало 0x445da60

### изменена: 0x448ee90 (63 байт)
- код тот же, но вызывает другую функцию: было 0x445d790, стало 0x445da30

### изменена: 0x448eed0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x445d760, стало 0x445da00

### изменена: 0x448ef10 (63 байт)
- код тот же, но вызывает другую функцию: было 0x445d730, стало 0x445d9d0

### изменена: 0x448ef50 (63 байт)
- код тот же, но вызывает другую функцию: было 0x445d700, стало 0x445d9a0

### изменена: 0x448ef90 (63 байт)
- код тот же, но вызывает другую функцию: было 0x445d6d0, стало 0x445d930

### изменена: 0x448efd0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x445d660, стало 0x445d8c0

### изменена: 0x448f010 (63 байт)
- код тот же, но вызывает другую функцию: было 0x445d5f0, стало 0x445d880

### изменена: 0x448f050 (63 байт)
- код тот же, но вызывает другую функцию: было 0x445d5b0, стало 0x445d850

### изменена: 0x448f090 (63 байт)
- код тот же, но вызывает другую функцию: было 0x445d580, стало 0x445d820

### изменена: 0x448f0d0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x445d550, стало 0x445d780

### изменена: 0x448f110 (63 байт)
- код тот же, но вызывает другую функцию: было 0x445d4b0, стало 0x445d750

### изменена: 0x448f150 (63 байт)
- код тот же, но вызывает другую функцию: было 0x445d480, стало 0x445d710

### изменена: 0x448f190 (63 байт)
- код тот же, но вызывает другую функцию: было 0x445d440, стало 0x445d6e0

### изменена: 0x448f1d0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x445d410, стало 0x445d6a0

### изменена: 0x448f210 (63 байт)
- код тот же, но вызывает другую функцию: было 0x445d3d0, стало 0x445d640

### изменена: 0x448f250 (63 байт)
- код тот же, но вызывает другую функцию: было 0x445d370, стало 0x445d610

### изменена: 0x448f290 (63 байт)
- код тот же, но вызывает другую функцию: было 0x445d340, стало 0x445d5d0

### изменена: 0x448f2d0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x445d300, стало 0x445d5a0

### изменена: 0x448f310 (63 байт)
- код тот же, но вызывает другую функцию: было 0x445d2d0, стало 0x445d520

### изменена: 0x448f350 (63 байт)
- код тот же, но вызывает другую функцию: было 0x445d250, стало 0x445d4f0

### изменена: 0x448f390 (63 байт)
- код тот же, но вызывает другую функцию: было 0x445d220, стало 0x445d4c0

### изменена: 0x448f3d0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x445d1f0, стало 0x445d480

### изменена: 0x448f410 (63 байт)
- код тот же, но вызывает другую функцию: было 0x445d1b0, стало 0x445d440

### изменена: 0x448f450 (63 байт)
- код тот же, но вызывает другую функцию: было 0x445d170, стало 0x445d410

### изменена: 0x448f490 (63 байт)
- код тот же, но вызывает другую функцию: было 0x445d140, стало 0x445d3d0

### изменена: 0x448f4d0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x445d100, стало 0x445d3a0

### изменена: 0x448f510 (63 байт)
- код тот же, но вызывает другую функцию: было 0x445d0d0, стало 0x445d2e0

### изменена: 0x448f550 (63 байт)
- код тот же, но вызывает другую функцию: было 0x445d010, стало 0x445d2a0

### изменена: 0x448f590 (63 байт)
- код тот же, но вызывает другую функцию: было 0x445cfd0, стало 0x445d270

### изменена: 0x448f5d0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x445cfa0, стало 0x445d240

### изменена: 0x448f610 (63 байт)
- код тот же, но вызывает другую функцию: было 0x445cf70, стало 0x445d190

### изменена: 0x448f650 (63 байт)
- код тот же, но вызывает другую функцию: было 0x445cec0, стало 0x445d160

### изменена: 0x448f690 (63 байт)
- код тот же, но вызывает другую функцию: было 0x445ce90, стало 0x445d130

### изменена: 0x448f6d0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x445ce60, стало 0x445d100

### изменена: 0x448f710 (63 байт)
- код тот же, но вызывает другую функцию: было 0x445ce30, стало 0x445d0c0

### изменена: 0x448f750 (63 байт)
- код тот же, но вызывает другую функцию: было 0x445cdf0, стало 0x445d090

### изменена: 0x448f790 (63 байт)
- код тот же, но вызывает другую функцию: было 0x445cdc0, стало 0x445d050

### изменена: 0x448f7d0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x445cd80, стало 0x445cfc0

### изменена: 0x448f810 (63 байт)
- код тот же, но вызывает другую функцию: было 0x445ccf0, стало 0x445cf90

### изменена: 0x448f850 (63 байт)
- код тот же, но вызывает другую функцию: было 0x445ccc0, стало 0x445cf50

### изменена: 0x448f890 (63 байт)
- код тот же, но вызывает другую функцию: было 0x445cc80, стало 0x445cf20

### изменена: 0x448f8d0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x445cc50, стало 0x445cef0

### изменена: 0x448f910 (63 байт)
- код тот же, но вызывает другую функцию: было 0x445cc20, стало 0x445cec0

### изменена: 0x448f950 (63 байт)
- код тот же, но вызывает другую функцию: было 0x445cbf0, стало 0x445ce90

### изменена: 0x448f990 (63 байт)
- код тот же, но вызывает другую функцию: было 0x445cbc0, стало 0x445ce50

### изменена: 0x448f9d0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x445cb80, стало 0x445ce20

### изменена: 0x448fa10 (63 байт)
- код тот же, но вызывает другую функцию: было 0x445cb50, стало 0x445cd90

### изменена: 0x448fa50 (63 байт)
- код тот же, но вызывает другую функцию: было 0x445cac0, стало 0x445cd60

### изменена: 0x448fa90 (63 байт)
- код тот же, но вызывает другую функцию: было 0x445ca90, стало 0x445ccd0

### изменена: 0x448fad0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x445ca00, стало 0x445cca0

### изменена: 0x448fb10 (63 байт)
- код тот же, но вызывает другую функцию: было 0x445c9d0, стало 0x445cc60

### изменена: 0x448fb50 (63 байт)
- код тот же, но вызывает другую функцию: было 0x445c990, стало 0x445cc30

### изменена: 0x448fb90 (63 байт)
- код тот же, но вызывает другую функцию: было 0x445c960, стало 0x445cc00

### изменена: 0x448fbd0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x445c930, стало 0x445cbd0

### изменена: 0x448fc10 (63 байт)
- код тот же, но вызывает другую функцию: было 0x445c900, стало 0x445cb70

### изменена: 0x448fc50 (63 байт)
- код тот же, но вызывает другую функцию: было 0x445c8a0, стало 0x445cb40

### изменена: 0x448fc90 (63 байт)
- код тот же, но вызывает другую функцию: было 0x445c870, стало 0x445cb00

### изменена: 0x448fcd0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x445c830, стало 0x445cad0

### изменена: 0x448fd10 (63 байт)
- код тот же, но вызывает другую функцию: было 0x445c800, стало 0x445ca90

### изменена: 0x448fd50 (63 байт)
- код тот же, но вызывает другую функцию: было 0x445c7c0, стало 0x445ca60

### изменена: 0x448fd90 (63 байт)
- код тот же, но вызывает другую функцию: было 0x445c790, стало 0x445c9c0

### изменена: 0x448fdd0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x445c6f0, стало 0x445c990

### изменена: 0x448fe10 (63 байт)
- код тот же, но вызывает другую функцию: было 0x445c6c0, стало 0x445c950

### изменена: 0x448fe50 (63 байт)
- код тот же, но вызывает другую функцию: было 0x445c680, стало 0x445c920

### изменена: 0x448fe90 (63 байт)
- код тот же, но вызывает другую функцию: было 0x445c650, стало 0x445c8f0

### изменена: 0x448fed0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x445c620, стало 0x445c8a0

### изменена: 0x448ff10 (63 байт)
- код тот же, но вызывает другую функцию: было 0x445c5d0, стало 0x445c830

### изменена: 0x448ff50 (63 байт)
- код тот же, но вызывает другую функцию: было 0x445c560, стало 0x445c800

### изменена: 0x448ff90 (63 байт)
- код тот же, но вызывает другую функцию: было 0x445c530, стало 0x445c7d0

### изменена: 0x448ffd0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x445c500, стало 0x445c7a0

### изменена: 0x4490010 (63 байт)
- код тот же, но вызывает другую функцию: было 0x445c4d0, стало 0x445c770

### изменена: 0x4490050 (63 байт)
- код тот же, но вызывает другую функцию: было 0x445c4a0, стало 0x445c710

### изменена: 0x4490090 (63 байт)
- код тот же, но вызывает другую функцию: было 0x445c440, стало 0x445c6c0

### изменена: 0x44900d0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x445c3f0, стало 0x445c690

### изменена: 0x4490110 (63 байт)
- код тот же, но вызывает другую функцию: было 0x445c3c0, стало 0x445c660

### изменена: 0x4490150 (63 байт)
- код тот же, но вызывает другую функцию: было 0x445c390, стало 0x445c5d0

### изменена: 0x4490190 (63 байт)
- код тот же, но вызывает другую функцию: было 0x445c300, стало 0x445c5a0

### изменена: 0x44901d0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x445c2d0, стало 0x445c550

### изменена: 0x4490210 (63 байт)
- код тот же, но вызывает другую функцию: было 0x445c280, стало 0x445c510

### изменена: 0x4490250 (63 байт)
- код тот же, но вызывает другую функцию: было 0x445c240, стало 0x445c4c0

### изменена: 0x4490290 (63 байт)
- код тот же, но вызывает другую функцию: было 0x445c1f0, стало 0x445c480

### изменена: 0x44902d0 (63 байт)
- код тот же, но вызывает другую функцию: было 0x445c1b0, стало 0x445c450

### изменена: 0x4490310 (63 байт)
- код тот же, но вызывает другую функцию: было 0x445c180, стало 0x445c3b0

### изменена: 0x4490350 (63 байт)
- код тот же, но вызывает другую функцию: было 0x445c0e0, стало 0x445c370

### изменена: 0x4490390 (63 байт)
- код тот же, но вызывает другую функцию: было 0x445c0a0, стало 0x445c2b0

### добавлена: 0x3e6f140 (98 байт) | строки: "&|x"

### добавлена: 0x3eae9e0 (904 байт) | строки: "tm|"

### добавлена: 0x449beb0 (99 байт) CModifierFactory<CDOTA_Modifier_Morphling_Replicate_Echo_Source>::vfunc#0

### добавлена: 0x44a36c0 (305 байт) CDOTA_Ability_Bane_Nightmare::vfunc#241 | строки: "morphling_replicate"

### добавлена: 0x44a4140 (272 байт) вызывается из: CDOTA_Modifier_Morphling_Replicate_Echo::vfunc#97 | строки: "tusk_snowball"; "snowball_windup"

### добавлена: 0x44a83a0 (717 байт) вызывается из: CDOTA_Modifier_Morphling_Replicate_Echo::vfunc#97

### добавлена: 0x44be040 (853 байт) вызывается из: CDOTA_Modifier_Morphling_Replicate_Echo::vfunc#97 | строки: "<NoAbilityName>"

### добавлена: 0x4513610 (528 байт) вызывается из: CDOTA_Modifier_Morphling_Replicate_Echo_Source::vfunc#97 | строки: "tusk_snowball"; "snowball_windup"

### добавлена: 0x4513820 (456 байт) CDOTA_Modifier_Morphling_Replicate_Echo_Source::OnIntervalThink | строки: "modifier_tusk_snowball_movement"; "tusk_launch_snowball"

### добавлена: 0x45e1810 (860 байт) вызывается из: CDOTA_Ability_ShadowShaman_Shackles::OnSpellStart | строки: "modifier_shadow_shaman_shackles"; "CNetworkTransmitComponent::StateChanged(%s) @%s:%d"

### добавлена: 0x4667890 (143 байт) CDOTA_Ability_Beastmaster_SummonThunderhide::OnUnStolen

### добавлена: 0x482dbf0 (340 байт) CDOTA_Ability_Chen_Zealot::OnUnStolen

### добавлена: 0x4b1e240 (32 байт) CDOTA_Ability_Marci_Companion_Run::vfunc#241

### добавлена: 0x4b36490 (108 байт) вызывается из: CDOTA_Modifier_Ogre_Magi_Bloodlust::vfunc#97

### добавлена: 0x4b878f0 (305 байт) CDOTA_Ability_Muerta_DeadShot::vfunc#241 | строки: "morphling_replicate"

### добавлена: 0x4ce7860 (369 байт) CDOTA_Ability_Tusk_WalrusKick::vfunc#241 | строки: "morphling_replicate"

### добавлена: 0x596e320 (112 байт)

### добавлена: 0x5bf1280 (113 байт)

### добавлена: 0x5bf6300 (192 байт) | строки: "Double-save to Member '%s'"

### добавлена: 0x61d5040 (342 байт) вызывается из: CDOTA_Item_Courier::vfunc#431, CDOTA_Bot_AbilityUsage_Dazzle_ShadowWave::vfunc#5

### удалена: 0x3e6ee50 (98 байт) | строки: "R{x"

### удалена: 0x3eaeb00 (904 байт) | строки: "xp|"

### удалена: 0x447d460 (39 байт) вызывается из: CDOTA_Modifier_Morphling_Replicate_Echo::vfunc#97

### удалена: 0x4b51fc0 (81 байт) CDOTA_Ability_Muerta_DeadShot::vfunc#241

### удалена: 0x61d34b0 (160 байт) вызывается из: CDOTA_Item_Courier::vfunc#431, CDOTA_Bot_AbilityUsage_Dazzle_ShadowWave::vfunc#5

### удалена: 0x61d3560 (182 байт) вызывается из: CDOTA_Ability_Kunkka_Torrent::vfunc#411, CDOTA_Ability_Kunkka_Tidebringer::vfunc#411, CDOTA_Ability_Lina_DragonSlave::vfunc#411

### копии существующего кода (17): шаблонные / склеенные компоновщиком функции, такой же код есть и в другой сборке — не новый код
- ещё одна копия существующего кода: 0x4485390 (19 байт) вызывается из: CDOTA_Modifier_Morphling_Replicate_Echo::vfunc#97
- ещё одна копия существующего кода: 0x4491a40 (111 байт) | строки: "GameTime_t"
- ещё одна копия существующего кода: 0x4492c30 (103 байт) CDOTA_Modifier_Morphling_Replicate_Echo::vfunc#8
- ещё одна копия существующего кода: 0x44930e0 (95 байт) CDOTA_Modifier_Morphling_Replicate_Echo::vfunc#7
- ещё одна копия существующего кода: 0x44b76c0 (635 байт) вызывается из: CDOTA_Modifier_Bane_Nightmare::vfunc#97 | строки: "bane_daunting_presence"
- ещё одна копия существующего кода: 0x47d5f00 (3 байт) CDOTA_Ability_Dazzle_ThroughTheRealm::vfunc#385
- ещё одна копия существующего кода: 0x485e230 (2880 байт)
- ещё одна копия существующего кода: 0x4ceded0 (329 байт) вызывается из: CDOTA_Modifier_Rubick_SpellSteal::vfunc#97
- ещё одна копия существующего кода: 0x61c0c80 (1075 байт)
- ещё одна копия существующего кода: 0x6283480 (277 байт)
- одной копией существующего кода меньше: 0x4476460 (25 байт) CDOTA_Modifier_AncientApparition_DeathRime::vfunc#7
- одной копией существующего кода меньше: 0x4479ba0 (50 байт) CDOTA_Modifier_AncientApparition_DeathRime::vfunc#8
- одной копией существующего кода меньше: 0x4490170 (63 байт)
- одной копией существующего кода меньше: 0x4498500 (78 байт) CModifierFactory<CDOTA_Modifier_Juggernaut_Vaulted_Strike_Slashes>::vfunc#0
- одной копией существующего кода меньше: 0x44b54e0 (394 байт) вызывается из: CDOTA_Modifier_Drow_Ranger_Multishot::vfunc#97 | строки: "drow_ranger_glacier"
- одной копией существующего кода меньше: 0x4b25680 (31 байт) вызывается из: CDOTA_Modifier_Ogre_Magi_Bloodlust::vfunc#97
- одной копией существующего кода меньше: 0x4cec380 (329 байт) вызывается из: CDOTA_Modifier_Rubick_SpellSteal::vfunc#97


## Строки библиотек

<details><summary>dota-bin/libserver.so: строки</summary>

**Добавлено — Прочие идентификаторы (4)**

```
m_flPendingSnowballWindupEnd
m_hDebuffTarget
m_hPendingSnowball
m_hPendingSnowballTarget
```

</details>
