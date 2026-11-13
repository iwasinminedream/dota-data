# Dota 6975: изменения кода по функциям

Снимки `6974-11230346` → `6975-11236380`; funcdiff.py. В диффе: [S:…] — строка, [K:…] — константа из данных, F — вызов другой функции, L — переход внутри функции, [D]/[T] — прочие адреса. Регистры и смещения стека меняются и от перекомпиляции.

## libclient.so: функций 280912 → 280911; без изменений 280892, изменено 19, добавлено 0, удалено 0

### изменена: 0x3ab8100 (13077 байт) | строки: "m_nId"; "m_Name"; "m_strNameToken"; "m_CoverImage"; "m_nNumberOfImages"; "m_URLForImages"; "m_nNumDigitsInFilename"; "m_ImageFileExtension"
было: 0x3ab8000 (13077 байт)
- строки: +"uRl" +"=Rl" +"PRl" +"cRl" +"vRl" +"$Ll" +"<Ml" +"%Jl" −"uQl" −"=Ql" −"PQl" −"cQl" −"vQl" −"$Kl" −"<Ll" −"%Il"
- инструкций: 2855 → 2855
```diff
@@ -706,5 +706,5 @@
 cmp r8b, 6
 ja L
-lea rdx, [S:"uQl"]
+lea rdx, [S:"uRl"]
 movzx eax, r8b
 movsxd rax, dword ptr [rdx + rax*4]
@@ -897,5 +897,5 @@
 cmp r8b, 6
 ja L
-lea rdx, [S:"=Ql"]
+lea rdx, [S:"=Rl"]
 movzx eax, r8b
 movsxd rax, dword ptr [rdx + rax*4]
@@ -1018,5 +1018,5 @@
 cmp r8b, 6
 ja L
-lea rdx, [S:"PQl"]
+lea rdx, [S:"PRl"]
 movzx eax, r8b
 movsxd rax, dword ptr [rdx + rax*4]
@@ -1087,5 +1087,5 @@
 cmp r8b, 6
 ja L
-lea rdx, [S:"cQl"]
+lea rdx, [S:"cRl"]
 movzx eax, r8b
 movsxd rax, dword ptr [rdx + rax*4]
@@ -1110,5 +1110,5 @@
 cmp r8b, 6
 ja L
-lea rdx, [S:"vQl"]
+lea rdx, [S:"vRl"]
 movzx eax, r8b
 movsxd rax, dword ptr [rdx + rax*4]
@@ -1831,5 +1831,5 @@
 cmp r8b, 6
 ja L
-lea rcx, [S:"$Kl"]
+lea rcx, [S:"$Ll"]
 movzx eax, r8b
 movsxd rax, dword ptr [rcx + rax*4]
@@ -1881,5 +1881,5 @@
 cmp r8b, 6
 ja L
-lea rcx, [S:"<Ll"]
+lea rcx, [S:"<Ml"]
 movzx eax, r8b
 movsxd rax, dword ptr [rcx + rax*4]
@@ -2436,5 +2436,5 @@
 cmp al, 6
 ja L
-lea rcx, [S:"%Il"]
+lea rcx, [S:"%Jl"]
 movzx edx, al
 movsxd rdx, dword ptr [rcx + rdx*4]
```

### изменена: 0x3afbfb0 (2277 байт) C_DynamicPropClientFadeOut::vfunc#10 | строки: "fade_out_mode"; "1jp"; "fade_time"; "fade_radius"; "fade_radius_end"; "showatday"; "showatnight"; "hide_in_showcase"
было: 0x3afbeb0 (2277 байт)
- строки: +"1jp" −"1ip"
- инструкций: 559 → 559
```diff
@@ -32,5 +32,5 @@
 cmp al, 6
 ja L
-lea rdx, [S:"1ip"]
+lea rdx, [S:"1jp"]
 movzx eax, al
 movsxd rax, dword ptr [rdx + rax*4]
```

### изменена: 0x3afc8a0 (398 байт) | строки: "8kp"
было: 0x3afc7a0 (398 байт)
- строки: +"8kp" −"8jp"
- инструкций: 128 → 128
```diff
@@ -8,5 +8,5 @@
 movsxd r12, edx
 push rbx
-lea rdx, [S:"8jp"]
+lea rdx, [S:"8kp"]
 mov rbx, rsi
 sub rsp, 0x18
```

### изменена: 0x3b3c0d0 (765 байт) CPointClientUIWorldTextPanelPreviewer::vfunc#2 | строки: "horizontal_align"; "vertical_align"; "orientation"; "f=t"
было: 0x3b3bfd0 (765 байт)
- строки: +"f=t" −"f<t"
- инструкций: 185 → 185
```diff
@@ -89,5 +89,5 @@
 cmp dl, 6
 ja L
-lea rcx, [S:"f<t"]
+lea rcx, [S:"f=t"]
 movzx edx, dl
 movsxd rdx, dword ptr [rcx + rdx*4]
```

### изменена: 0x3b4cc90 (355 байт) | строки: "xGu"; "CUtlSymbolLarge"; "C_NetworkUtlVectorBase"
было: 0x3b4cb90 (355 байт)
- строки: +"xGu" −"xFu"
- инструкций: 107 → 107
```diff
@@ -2,5 +2,5 @@
 ja L
 push rbp
-lea rdx, [S:"xFu"]
+lea rdx, [S:"xGu"]
 mov edi, edi
 mov rbp, rsp
```

### изменена: 0x3b4f100 (568 байт) | строки: " ku"
было: 0x3b4f000 (568 байт)
- строки: +" ku" −" ju"
- инструкций: 160 → 160
```diff
@@ -9,5 +9,5 @@
 movsxd r12, edx
 push rbx
-lea rdx, [S:" ju"]
+lea rdx, [S:" ku"]
 mov rbx, rsi
 sub rsp, 0x10
```

### изменена: 0x3b4f340 (568 байт) | строки: "Dmu"
было: 0x3b4f240 (568 байт)
- строки: +"Dmu" −"Dlu"
- инструкций: 160 → 160
```diff
@@ -9,5 +9,5 @@
 movsxd r12, edx
 push rbx
-lea rdx, [S:"Dlu"]
+lea rdx, [S:"Dmu"]
 mov rbx, rsi
 sub rsp, 0x10
```

### изменена: 0x3b4f580 (568 байт) | строки: "hou"
было: 0x3b4f480 (568 байт)
- строки: +"hou" −"hnu"
- инструкций: 160 → 160
```diff
@@ -9,5 +9,5 @@
 movsxd r12, edx
 push rbx
-lea rdx, [S:"hnu"]
+lea rdx, [S:"hou"]
 mov rbx, rsi
 sub rsp, 0x10
```

### изменена: 0x3b8edb0 (1113 байт) CNetworkTransmitComponent::vfunc#3 | строки: "m_nTransmitStateOwnedCounter"; "\\Hy"; "@Hy"; "Unsupported KV3 basic type '%s' (%d)!"; "Pointers cannot be used as numeric values"
было: 0x3b8ecb0 (1113 байт)
- строки: +"\\Hy" +"@Hy" −"\\Gy" −"@Gy"
- инструкций: 259 → 259
```diff
@@ -51,5 +51,5 @@
 cmp r8b, 6
 ja L
-lea rdx, [S:"\\Gy"]
+lea rdx, [S:"\\Hy"]
 movzx eax, r8b
 movsxd rax, dword ptr [rdx + rax*4]
@@ -108,5 +108,5 @@
 cmp r8b, 6
 ja L
-lea rdx, [S:"@Gy"]
+lea rdx, [S:"@Hy"]
 movzx eax, r8b
 movsxd rax, dword ptr [rdx + rax*4]
```

### изменена: 0x3bd0e00 (117 байт) | строки: "A@}"
было: 0x3bd0d00 (117 байт)
- строки: +"A@}" −"A?}"
- инструкций: 39 → 39
```diff
@@ -2,5 +2,5 @@
 cmp edx, 6
 ja L
-lea rcx, [S:"A?}"]
+lea rcx, [S:"A@}"]
 push rbp
 mov rdi, rsi
```

### изменена: 0x5bc7940 (200 байт) | строки: "#DOTA_PlayerReportPopup_GoodTeamwork_Title"; "#DOTA_PlayerReportPopup_ToxicVoice_Title"; "#DOTA_PlayerReportPopup_Smurfing_Title"; "#DOTA_PlayerReportPopup_Griefing_Title"; "#DOTA_PlayerReportPopup_Cheating_Title"; "#DOTA_PlayerReportPopup_DidNotPlayRole_Title"; "#DOTA_PlayerReportPopup_Botting_Title"; "#DOTA_PlayerReportPopup_GoodCommunication_Title"
было: 0x5bc7840 (184 байт)
- строки: +"#DOTA_PlayerReportPopup_Botting_Title"
- инструкций: 37 → 40
```diff
@@ -7,5 +7,11 @@
 jmp rax
 nop word ptr [rax + rax]
+lea rax, [S:"#DOTA_PlayerReportPopup_GoodTeamwork_Title"]
+ret
+nop dword ptr [rax + rax]
 lea rax, [D]
+ret
+nop dword ptr [rax + rax]
+lea rax, [S:"#DOTA_PlayerReportPopup_ToxicVoice_Title"]
 ret
 nop dword ptr [rax + rax]
@@ -22,4 +28,7 @@
 ret
 nop dword ptr [rax + rax]
+lea rax, [S:"#DOTA_PlayerReportPopup_Botting_Title"]
+ret
+nop dword ptr [rax + rax]
 lea rax, [S:"#DOTA_PlayerReportPopup_GoodCommunication_Title"]
 ret
@@ -28,10 +37,4 @@
 ret
 nop dword ptr [rax + rax]
-lea rax, [S:"#DOTA_PlayerReportPopup_GoodTeamwork_Title"]
-ret
-nop dword ptr [rax + rax]
-lea rax, [S:"#DOTA_PlayerReportPopup_ToxicVoice_Title"]
-ret
-nop dword ptr [rax + rax]
 lea rax, [S:"#DOTA_PlayerReportPopup_ToxicText_Title"]
 ret
```

### изменена: 0x5bca8d0 (1088 байт) вызывается из: C_DOTA_Unit_Hero_Rubick::vfunc#534, CDOTA_ParticleManager::vfunc#9, CDOTAGCClientSystem::vfunc#1
было: 0x5bca840 (976 байт)
- прямых вызовов: 10 → 14
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

### изменена: 0x6570340 (604 байт)
было: 0x6570240 (604 байт)
- числа в инструкциях: +0xf8 −0xf0
- инструкций: 166 → 166
```diff
@@ -101,5 +101,5 @@
 xor r10d, r10d
 lea rax, [D]
-mov edi, 0xf0
+mov edi, 0xf8
 cmp dword ptr [r13 + 0xfc], 7
 mov rax, qword ptr [rax]
```

### изменена: 0x6807b30 (352 байт) CDOTA_DB_Popup_ReportPlayerNew::vfunc#63
было: 0x6807a30 (352 байт)
- числа в инструкциях: +0xf8 −0xf0
- инструкций: 83 → 83
```diff
@@ -73,5 +73,5 @@
 mov rdi, rbx
 mov rbx, qword ptr [rbp - 8]
-mov esi, 0xf0
+mov esi, 0xf8
 leave
 jmp F
```

### изменена: 0x6807c90 (296 байт)
было: 0x6807b90 (296 байт)
- числа в инструкциях: +0xf8 −0xf0
- инструкций: 86 → 86
```diff
@@ -75,5 +75,5 @@
 pop rbx
 mov rdi, r12
-mov esi, 0xf0
+mov esi, 0xf8
 pop r12
 pop rbp
```

### изменена: 0x681a480 (3243 байт) | строки: "panel_fatal_cast"; "file://{resources}/layout/popups/popup_report_player_new.xml"; "Report_Negative"; "Report_Positive"; "AvoidDefault"; "avoid_state"; "player_report_counts_updated"; "ToxicTextButton"
было: 0x681a380 (3002 байт)
- строки: +"BottingButton" +"!pPanel || pResult" +"Attempted to cast panel '%s' to type '%s'"
- числа в инструкциях: +0x5b2 +0xffffff80 +0x16
- виртуальные вызовы: +0x198 (слот 51) +0x48 (слот 9) +0x1e8 (слот 61) +0x1d0 (слот 58)
- поля объектов: +0x10 +0xf0
- прямых вызовов: 75 → 81
- инструкций: 699 → 755
```diff
@@ -75,6 +75,6 @@
 cmp al, 0xaf
 ja L
-movzx ecx, byte ptr [rbx + 0x70]
-lea edx, [rcx - 1]
+movzx esi, byte ptr [rbx + 0x70]
+lea edx, [rsi - 1]
 cmp dl, 3
 ja L
@@ -364,4 +364,34 @@
 mov rdi, qword ptr [rbx + 8]
 mov qword ptr [rbx + 0xe8], rcx
+lea rsi, [S:"BottingButton"]
+mov rax, qword ptr [rdi]
+call qword ptr [rax + 0x198]
+test rax, rax
+mov rdi, rax
+je L
+mov rax, qword ptr [rax]
+call qword ptr [rax + 0x48]
+mov rcx, rax
+lea rax, [D]
+test rcx, rcx
+movzx edx, word ptr [rax]
+mov word ptr [rbp - 0x70], dx
+mov dword ptr [rbp - 0x84], edx
+je L
+mov rax, qword ptr [rcx]
+mov rdi, rcx
+mov qword ptr [rbp - 0x80], rcx
+call qword ptr [rax + 0x1e8]
+mov edx, dword ptr [rbp - 0x84]
+mov rcx, qword ptr [rbp - 0x80]
+jmp L
+nop dword ptr [rax + rax]
+mov rax, qword ptr [rax + 0x10]
+test rax, rax
+je L
+cmp dx, word ptr [rax]
+jne L
+mov rdi, qword ptr [rbx + 8]
+mov qword ptr [rbx + 0xf0], rcx
 lea rsi, [S:"OverwatchReportToggle"]
 mov rax, qword ptr [rdi]
@@ -503,4 +533,7 @@
 xor ecx, ecx
 jmp L
+nop word ptr [rax + rax]
+xor ecx, ecx
+jmp L
 mov ecx, dword ptr [rbx + 0x69]
 test ecx, ecx
@@ -611,4 +644,96 @@
 movdqa xmm0, xmmword ptr [rbp - 0xa0]
 mov rdi, r13
+mov qword ptr [rbp - 0x78], rcx
+mov qword ptr [rbp - 0x40], rax
+movzx eax, byte ptr [rbp - 0x34]
+movaps xmmword ptr [rbp - 0x50], xmm0
+mov dword ptr [rbp - 0x38], 0x5b2
+and eax, 0xffffff80
+or eax, 0x16
+mov byte ptr [rbp - 0x34], al
+call F
+mov rcx, qword ptr [rbp - 0x78]
+mov rbx, rax
+mov rax, qword ptr [rcx]
+mov rdi, rcx
+call qword ptr [rax + 0x1d0]
+mov rcx, rbx
+mov rdi, r14
+lea rsi, [S:"Attempted to cast panel '%s' to type '%s'"]
+mov rdx, rax
+xor eax, eax
+call F
+lea rax, [S:"!pPanel || pResult"]
+movdqa xmm0, xmmword ptr [rbp - 0xa0]
+mov rdi, r13
+mov qword ptr [rbp - 0x78], rcx
+mov qword ptr [rbp - 0x40], rax
+movzx eax, byte ptr [rbp - 0x34]
+movaps xmmword ptr [rbp - 0x50], xmm0
+mov dword ptr [rbp - 0x38], 0x5b2
+and eax, 0xffffff80
+or eax, 0x16
+mov byte ptr [rbp - 0x34], al
+call F
+mov rcx, qword ptr [rbp - 0x78]
+mov rbx, rax
+mov rax, qword ptr [rcx]
+mov rdi, rcx
+call qword ptr [rax + 0x1d0]
+mov rcx, rbx
+mov rdi, r14
+lea rsi, [S:"Attempted to cast panel '%s' to type '%s'"]
+mov rdx, rax
+xor eax, eax
+call F
+lea rax, [S:"!pPanel || pResult"]
+movdqa xmm0, xmmword ptr [rbp - 0xa0]
+mov rdi, r13
+mov qword ptr [rbp - 0x78], rcx
+mov qword ptr [rbp - 0x40], rax
+movzx eax, byte ptr [rbp - 0x34]
+movaps xmmword ptr [rbp - 0x50], xmm0
+mov dword ptr [rbp - 0x38], 0x5b2
+and eax, 0xffffff80
+or eax, 0x16
+mov byte ptr [rbp - 0x34], al
+call F
+mov rcx, qword ptr [rbp - 0x78]
+mov rbx, rax
+mov rax, qword ptr [rcx]
+mov rdi, rcx
+call qword ptr [rax + 0x1d0]
+mov rcx, rbx
+mov rdi, r14
+lea rsi, [S:"Attempted to cast panel '%s' to type '%s'"]
+mov rdx, rax
+xor eax, eax
```
(ещё 101 строк диффа: so-query.py fdiff libclient.so 0x681a480)

### изменена: 0x682eb70 (4614 байт) | строки: "panel_fatal_cast"; "file://{resources}/layout/popups/popup_short_film_workshop_vote.xml"; "http://cdn.dota2.com.cn/apps/dota2/videos/international2025/short_film/%s.webm"; "https://www.youtube.com/embed/%s?autoplay=1&amp;modestbranding=1&amp;rel=0&amp;t"; "PrevButton"; "NextButton"; "Skip"; "Yes"
было: 0x682e9b0 (4827 байт)
- строки: −"!pPanel || pResult" −"Attempted to cast panel '%s' to type '%s'"
- числа в инструкциях: −0x5b2 −0xffffff80 −0x16
- виртуальные вызовы: −0x198 (слот 51) −0x48 (слот 9) −0x1e8 (слот 61) −0x1d0 (слот 58)
- поля объектов: −0x10
- прямых вызовов: 109 → 104
- инструкций: 857 → 812
```diff
@@ -365,30 +365,8 @@
 mov dword ptr [rbx + 0x230], 0
 mov qword ptr [rbx + 0x68], rax
-mov rax, qword ptr [rdi]
-call qword ptr [rax + 0x198]
-test rax, rax
-mov rdi, rax
-je L
-mov rax, qword ptr [rax]
-call qword ptr [rax + 0x48]
-mov r13, rax
-lea rax, [D]
-test r13, r13
-movzx r12d, word ptr [rax]
-mov word ptr [rbp - 0x160], r12w
-je L
-mov rax, qword ptr [r13]
-mov rdi, r13
-call qword ptr [rax + 0x1e8]
-jmp L
-nop word ptr [rax + rax]
-mov rax, qword ptr [rax + 0x10]
-test rax, rax
-je L
-cmp r12w, word ptr [rax]
-jne L
+call F
 mov rdi, qword ptr [rbx + 8]
 lea rsi, [S:"NextButton"]
-mov qword ptr [rbx + 0x80], r13
+mov qword ptr [rbx + 0x80], rax
 call F
 mov rdi, qword ptr [rbx + 8]
@@ -789,5 +767,5 @@
 xor r13d, r13d
 jmp L
-xor r13d, r13d
+mov qword ptr [r14 + 0x10], r13
 jmp L
 lea rax, [S:"!pPanel || pResult"]
@@ -833,25 +811,2 @@
 xor eax, eax
 call F
-mov qword ptr [r14 + 0x10], r13
-jmp L
-lea rax, [S:"!pPanel || pResult"]
-movdqa xmm2, xmmword ptr [rbp - 0x190]
-mov dword ptr [rbp - 0x128], 0x5b2
-mov qword ptr [rbp - 0x130], rax
-movzx eax, byte ptr [rbp - 0x124]
-lea rdi, [rbp - 0x160]
-movaps xmmword ptr [rbp - 0x140], xmm2
-and eax, 0xffffff80
-or eax, 0x16
-mov byte ptr [rbp - 0x124], al
-call F
-mov rdi, r13
-mov rbx, rax
-mov rax, qword ptr [r13]
-call qword ptr [rax + 0x1d0]
-mov rcx, rbx
-mov rdi, r14
-lea rsi, [S:"Attempted to cast panel '%s' to type '%s'"]
-mov rdx, rax
-xor eax, eax
-call F
```

### изменена: 0x6837d70 (601 байт) CDOTA_DB_Popup_ReportPlayerNew::vfunc#57 | строки: "Report_AnyCategorySelected"; "reason"; "OverwatchApplicableReport"
было: 0x6837c70 (601 байт)
- числа в инструкциях: +0 +0 +0 +0
- инструкций: 162 → 162
```diff
@@ -18,5 +18,5 @@
 movzx eax, r12b
 mov edx, eax
-mov dword ptr [rbp - 0x64], eax
+mov dword ptr [rbp - 0x68], eax
 movzx esi, word ptr [rbp - 0x40]
 mov rax, qword ptr [rdi]
@@ -38,12 +38,13 @@
 cmp eax, esi
 jne L
-xor r15d, r15d
-nop dword ptr [rax + rax]
-lea rax, [rbx + 0xf0]
+mov byte ptr [rbp - 0x61], 0
+nop dword ptr [rax]
+lea rax, [rbx + 0xf8]
 mov qword ptr [rbp - 0x58], rax
 lea rax, [rbp - 0x48]
 lea r12, [rbx + 0xc0]
 mov qword ptr [rbp - 0x60], rax
-nop word ptr [rax + rax]
+lea r15, [D]
+nop dword ptr [rax]
 mov r13, qword ptr [r12]
 lea rsi, [S:"reason"]
@@ -57,9 +58,9 @@
 mov edx, dword ptr [rbx + 0x69]
 mov rsi, r14
+mov rdi, r15
 mov rcx, qword ptr [rbx + 0x78]
 mov dword ptr [rbp - 0x40], eax
 mov dword ptr [rbp - 0x3c], edx
-lea rdx, [D]
-mov rdi, rdx
+mov rdx, r15
 mov qword ptr [rbp - 0x38], rcx
 call F
@@ -83,5 +84,5 @@
 jne L
 xor r12d, r12d
-test r15b, r15b
+cmp byte ptr [rbp - 0x61], 0
 je L
 lea rax, [D]
@@ -104,5 +105,5 @@
 call qword ptr [rax + 0x248]
 mov rax, qword ptr [rbx + 0xb8]
-mov esi, dword ptr [rbp - 0x64]
+mov esi, dword ptr [rbp - 0x68]
 mov rdi, qword ptr [rax + 8]
 mov rax, qword ptr [rdi]
@@ -116,10 +117,10 @@
 pop rbp
 jmp rax
+nop word ptr [rax + rax]
+cmp eax, esi
+mov byte ptr [rbp - 0x61], 0
+je L
 nop dword ptr [rax]
-xor r15d, r15d
-cmp eax, esi
-je L
-nop dword ptr [rax + rax]
-test r15b, r15b
+cmp byte ptr [rbp - 0x61], 0
 jne L
 movsxd rdx, eax
@@ -128,5 +129,5 @@
 sub edx, 5
 cmp dl, 1
-setbe r15b
+setbe byte ptr [rbp - 0x61]
 lea ecx, [rax + 1]
 cmp ecx, esi
@@ -137,6 +138,5 @@
 mov eax, ecx
 jmp L
-nop word ptr cs:[rax + rax]
-nop dword ptr [rax]
+nop dword ptr [rax + rax]
 add eax, 1
 add rdx, 0x14
```

### изменена: 0x71c3640 (259 байт) | строки: "OverwatchReport"
было: 0x71c3540 (259 байт)
- числа в инструкциях: +0xf8 −0xf0
- инструкций: 74 → 74
```diff
@@ -45,5 +45,5 @@
 mov r13d, eax
 call F
-mov edi, 0xf0
+mov edi, 0xf8
 cmp r13d, eax
 mov rax, qword ptr [r15 + 0x18]
```

### копии существующего кода (1): шаблонные / склеенные компоновщиком функции, такой же код есть и в другой сборке — не новый код
- одной копией существующего кода меньше: 0x5bca7b0 (112 байт) вызывается из: C_DOTA_Unit_Hero_Rubick::vfunc#534, CDOTA_ParticleManager::vfunc#9, CDOTAGCClientSystem::vfunc#1

## libserver.so: функций 220000 → 220000; без изменений 220000, изменено 0, добавлено 0, удалено 0
