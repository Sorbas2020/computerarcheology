![Bank 0](Zelda.jpg)

# Bank 0 (Sound)

>>> cpu 6502

>>> binary 8000:roms/Zelda.nes[0010:4010]

>>> memoryTable ram 

[RAM Usage](RAMUse.md)

>>> memoryTable hard 

[Hardware Info](Hardware.md)

```code
; Music descriptor
; 00 -> Note delay set (0-4)
; 01    -> Pointer to Music
; 02    -> ...
; 03 -> Offset for C (A begins at 0)
; 04 -> Offset for B
; 05 -> Offset for D
; 06 -> 0619
; 07 -> 05F1

; DeltaModulation:
;  - Sword-flying sound

; Square 1: 
;  - Harmony component of music (theme, getting object)
;  - Letters appearing on screen
;  - Enemy dieing

; Square 2:
;  - Main component of music (theme, getting object)
;  - Selecting in name-entry
;  - Enemy dieing

; Triangle:
;  - Base component of music

; Noise: 
;  - Drums
;  - Going up and down stairs
;  - Firing sword

8000: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
8020: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
8040: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
8060: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
8080: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
80A0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
80C0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
80E0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
8100: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
8120: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
8140: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
8160: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
8180: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
81A0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
81C0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
81E0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
8200: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
8220: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
8240: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
8260: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
8280: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
82A0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
82C0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
82E0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
8300: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
8320: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
8340: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
8360: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
8380: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
83A0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
83C0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
83E0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
8400: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
8420: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
8440: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
8460: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
8480: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
84A0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
84C0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
84E0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
8500: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
8520: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
8540: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
8560: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
8580: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
85A0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
85C0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
85E0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
8600: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
8620: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
8640: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
8660: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
8680: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
86A0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
86C0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
86E0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
8700: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
8720: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
8740: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
8760: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
8780: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
87A0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
87C0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
87E0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
8800: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
8820: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
8840: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
8860: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
8880: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
88A0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
88C0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
88E0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
8900: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
8920: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
8940: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
8960: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
8980: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
89A0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
89C0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
89E0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
8A00: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
8A20: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
8A40: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
8A60: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
8A80: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
8AA0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
8AC0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
8AE0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
8B00: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
8B20: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
8B40: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
8B60: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
8B80: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
8BA0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
8BC0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
8BE0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
8C00: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
8C20: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
8C40: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
8C60: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
8C80: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
8CA0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
8CC0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
8CE0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
8D00: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
8D20: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
8D40: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 


; ?? Only song numbers with bits set in mask 1001_0001 have drum voices

; Offsets to music descriptors (0x24 songs)
8D60: 7D B5 6E 67 7D AD 64 64 75 7D 85 95 7D 8D 95 9D A5 BD C5 CD D5 DD D5 E5 ED 
8D79: 24 2C 34 3C 44 34 4C 54 5C 44 F5 ; Splash screen fragments (19..24)

;Song25 (24 from 8D60)
8D84: 20 8B 94 3B 1D 4F 80 01 

;Song26 (2C from 8D60)
8D8C: 20 DC 94 27 57 23 01 80 

;Song27 (34 from 8D60)
;Song30 (34 from 8D60)
8D94: 20 A1 95 38 17 B8 80 80 

;Song28 (3C from 8D60)
8D9C: 20 F1 95 6C 26 68 80 80 

;Song29 (44 from 8D60)
;Song34 (44 from 8D60)
8DA4: 20 8D 96 3E 25 21 80 80 

;Song31 (4C from 8D60)
8DAC: 20 EB 96 19 0D 31 80 80 

;Song32 (54 from 8D60)
8DB4: 20 20 97 3F 27 7C 80 80 

;Song33 (5C from 8D60)
8DBC: 20 8F 97 1D 11 0D 80 

;Song6 (64 from 8D60)
;Song7 (64 from 8D60)
8DC3: 80 10 A1 8E 

;Song3 (67 from 8D60)
8DC7: 10 5D 8E 0D 07 00 80       

;Song2 (6E from 8D60)
8DCE: 10 A4 91 46 22 00 80 

;Song8 (75 from 8D60)
8DD5: 10 70 8E 32 5D 8E 01 80 

;Song0 (7D from 8D60)
;Song4 (7D from 8D60)
;Song9 (7D from 8D60)
;Song12 (7D from 8D60)
8DDD: 10 0F 8F 35 16 CE 01 80 

;Song10 (85 from 8D60)
8DE5: 10 55 8F 60 26 88 01 80 

;Song13 (8D from 8D60)
8DED: 10 32 90 59 2D A4 01 80 

;Song11 (95 from 8D60)
;Song14 (95 from 8D60)
8DF5: 10 E4 8F 3B 1A F2 01 80 

;Song15 (9D from 8D60)
8DFD: 00 DD 90 45 22 00 01 01 

;Song16 (A5 from 8D60)
8E05: 00 3A 91 39 1C 00 01 01 

;Song5 (AD from 8D60)
8E0D: 10 FD 91 A5 53 CD 80 80 

;Song1 (B5 from 8D60)
8E15: 10 CC 92 22 10 00 80 01 

;Song17 (BD from 8D60)
8E1D: 08 F7 92 22 50 59 01 80 

;Song18 (C5 from 8D60)
8E25: 08 F7 92 2F 50 59 01 80 

;Song19 (CD from 8D60)
8E2D: 08 52 93 7A 1B C2 80 80 

;Song20 (D5 from 8D60)
;Song22 (D5 from 8D60)
8E35: 08 86 93 46 24 8E 01 80 

;Song21 (DD from 8D60)
8E3D: 08 9D 93 44 23 77 01 80 

;Song23 (E5 from 8D60)
8E45: 08 ED 93 1B 0E 27 01 80 

;Song24 (ED from 8D60)
8E4D: 08 1A 94 40 1A 6B 80 80 

;Song35 (F5 from 8D60)
8E55: 10 C4 97 3F 20 00 80 80 



;Song3A (Song 3 voice A)
;Song3D (Song 3 voice D)
8E5D: 81 1E 20 22 85 24 00                                      ; 1:C4 1:C#4 1:D4 4:E-4 *END* 

;Song3B (Song 3 voice B)
8E64: 81 30 32 34 85 36                                         ; 1:A4 1:B-4 1:B4 4:C5 

;Song3C (Song 3 voice C)
8E6A: 81 28 2A 2C 85 2E                                         ; 1:F4 1:F#4 1:G4 4:G#4 

;Song8A (Main theme intro 32 beats voice A)
8E70: 85 32 82 08 08 32 32 32 32 32 08 2E                       ; 4:B-4 2/3:R 2/3:R 2/3:B-4 2/3:B-4 2/3:B-4
8E7C: 83 32 82 08 08 32 32 32 32 32 08 2E                       ; 2/3:B-4 2/3:B-4 2/3:R 2/3:G#4 2:B-4 2/3:R
8E88: 83 32 82 08 08 32 32 32 32 80 32 08                       ; 2/3:R 2/3:B-4 2/3:B-4 2/3:B-4 2/3:B-4
8E94: 28 28 28 08 28 28 28 08 28 28 81 28                       ; 2/3:B-4 2/3:R 2/3:G#4 2:B-4 2/3:R 2/3:R
8EA0: 28                                                        ; 2/3:B-4 2/3:B-4 2/3:B-4 2/3:B-4 1/2:B-4 1/2:R 1/2:F4 1/2:F4 1/2:F4 1/2:R 1/2:F4 1/2:F4 1/2:F4 1/2:R 1/2:F4 1/2:F4 1:F4 1:F4 

;Song6A (Song 6 voice A)
;Song7A (Song 7 voice A)
8EA1: 00                                                        ; *END* 

;Song8C (Main theme intro 32 beats voice C)
8EA2: 83 1A 82 1A 1A 1A 83 1A 82 1A 1A 1A                       ; 2:B-3 2/3:B-3 2/3:B-3 2/3:B-3 2:B-3 2/3:B-3
8EAE: 83 16 82                                                  ; 2/3:B-3 2/3:B-3 2:G#3 

;Song6C (Song 6 voice C)
;Song7C (Song 7 voice C)
8EB1: 16 16 16 83 16 82 16 16 16 83 12 82                       ; ??:G#3 ??:G#3 ??:G#3 2:G#3 2/3:G#3 2/3:G#3
8EBD: 12 12 12 83 12 82 12 12 12 83 10 10                       ; 2/3:G#3 2:F#3 2/3:F#3 2/3:F#3 2/3:F#3 2:F#3
8EC9: 10 81 14 18                                               ; 2/3:F#3 2/3:F#3 2/3:F#3 2:F3 2:F3 2:F3 1:G3 1:A3 

;Song8B (Main theme intro 32 beats voice B)
8ECD: 85 22 82 08 08 22 22 22 22 1E 08 1E                       ; 4:D4 2/3:R 2/3:R 2/3:D4 2/3:D4 2/3:D4 2/3:D4
8ED9: 83 1E 08 82 1E 1E 1E 20 08 20 83 20                       ; 2/3:C4 2/3:R 2/3:C4 2:C4 2:R 2/3:C4 2/3:C4
8EE5: 82 08 08 20 20 20 20 80 20 08 18 18                       ; 2/3:C4 2/3:C#4 2/3:R 2/3:C#4 2:C#4 2/3:R
8EF1: 81 18 80 18 18 81 18 80 18 18 81 18                       ; 2/3:R 2/3:C#4 2/3:C#4 2/3:C#4 2/3:C#4
8EFD: 18                                                        ; 1/2:C#4 1/2:R 1/2:A3 1/2:A3 1:A3 1/2:A3 1/2:A3 1:A3 1/2:A3 1/2:A3 1:A3 1:A3 

;Song6B (Song 6 voice B)
;Song7B (Song 7 voice B)
;Song8D (Main theme intro 32 beats voice D)
8EFE: B1 90 90 90 B1 90 90 90 B1 90 90 90                       ; 1/2:D6 1/2:D6 
8F0A: D0 D0 D0 50 50                                            ; .

;Song0A (Main theme 1st 8 beats voice A)
;Song4A (Song 4 voice A)
;Song9A (Song 9 voice A)
;Song12A (Song 12 voice A)
8F0F: 81 32 08 84 28 80 08 32 32 36 3A 3C                       ; 1:B-4 1:R 3:F4 1/2:R 1/2:B-4 1/2:B-4 1/2:C5
8F1B: 85 40 81 08 40 82 40 06 44 00                             ; 1/2:D5 1/2:E-5 4:F5 1:R 1:F5 2/3:F5 2/3:F#5 2/3:G#5 *END* 

;Song0B (Main theme 1st 8 beats voice B)
;Song4B (Song 4 voice B)
;Song9B (Song 9 voice B)
;Song12B (Song 12 voice B)
8F25: 81 22 08 82 22 22 1E 81 22 80                             ; 1:D4 1:R 2/3:D4 2/3:D4 2/3:C4 1:D4 

;Song6D (Song 6 voice D)
;Song7D (Song 7 voice D)
8F2F: 08 22 22 24 28 2C 81 2E 80 08 32 32                       ; ??:R ??:D4 ??:D4 ??:E-4 ??:F4 ??:G4 1:G#4
8F3B: 36 3A 3C 83 40 82 2E 32 36                                ; 1/2:R 1/2:B-4 1/2:B-4 1/2:C5 1/2:D5 1/2:E-5 2:F5 2/3:G#4 2/3:B-4 2/3:C5 

;Song0C (Main theme 1st 8 beats voice C)
;Song4C (Song 4 voice C)
;Song9C (Song 9 voice C)
;Song12C (Song 12 voice C)
8F44: 83 1A 82 1A 1A 16 83 1A 1A 16 82 16                       ; 2:B-3 2/3:B-3 2/3:B-3 2/3:G#3 2:B-3 2:B-3
8F50: 16 12 83 16 16                                            ; 2:G#3 2/3:G#3 2/3:G#3 2/3:F#3 2:G#3 2:G#3 

;Song10A (Main theme 2nd 32 beats voice A)
8F55: 85 46 82 08 46 46 46 44 06 82 44 08                       ; 4:B-5 2/3:R 2/3:B-5 2/3:B-5 2/3:B-5 2/3:G#5
8F61: 06 85 40 83 40 81 3C 80 3C 40 85 06                       ; 2/3:F#5 2/3:G#5 2/3:R 2/3:F#5 4:F5 2:F5
8F6D: 81 40 3C 81 38 80 38 3C 85 40 81 3C                       ; 1:E-5 1/2:E-5 1/2:F5 4:F#5 1:F5 1:E-5 1:C#5
8F79: 38 00                                                     ; 1/2:C#5 1/2:E-5 4:F5 1:E-5 1:C#5 *END* 

;Song10B (Main theme 2nd 32 beats voice B)
8F7B: 81 38 80 08 2A 2A 2E 32 36 82 38 08                       ; 1:C#5 1/2:R 1/2:F#4 1/2:F#4 1/2:G#4 1/2:B-4
8F87: 38 38 36 32 38 08 2E 2E 2E 2A 2E 08                       ; 1/2:C5 2/3:C#5 2/3:R 2/3:C#5 2/3:C#5 2/3:C5
8F93: 2E 2E 2A 2E 81 2A 80 2A 28 81 2A 80                       ; 2/3:B-4 2/3:C#5 2/3:R 2/3:G#4 2/3:G#4
8F9F: 2A 2E 83 32 81 2E 2A 81 28 80 28 24                       ; 2/3:G#4 2/3:F#4 2/3:G#4 2/3:R 2/3:G#4
8FAB: 81 28 80 28 2A 83 2E 81 2A 28                             ; 2/3:G#4 2/3:F#4 2/3:G#4 1:F#4 1/2:F#4 1/2:F4 1:F#4 1/2:F#4 1/2:G#4 2:B-4 1:G#4 1:F#4 1:F4 1/2:F4 1/2:E-4 1:F4 1/2:F4 1/2:F#4 2:G#4 1:F#4 1:F4 

;Song10C (Main theme 2nd 32 beats voice C)
8FB5: 83 12 82 12 12 0E 83 12 12 20 82 20                       ; 2:F#3 2/3:F#3 2/3:F#3 2/3:E3 2:F#3 2:F#3
8FC1: 20 1E 83 20 20 1C 82 1C 1C 1A 83 1C                       ; 2:C#4 2/3:C#4 2/3:C#4 2/3:C4 2:C#4 2:C#4
8FCD: 82 1C 1C 1C 83 1A 82 1A 1A 16 83 1A                       ; 2:B3 2/3:B3 2/3:B3 2/3:B-3 2:B3 2/3:B3
8FD9: 82 1A 1A 1A                                               ; 2/3:B3 2/3:B3 2:B-3 2/3:B-3 2/3:B-3 2/3:G#3 2:B-3 2/3:B-3 2/3:B-3 2/3:B-3 

;Song0D (Main theme 1st 8 beats voice D)
;Song4D (Song 4 voice D)
;Song9D (Song 9 voice D)
;Song10D (Main theme 2nd 32 beats voice D)
;Song12D (Song 12 voice D)
8FDD: D0 90 90 90 D0 D0 00                                      ; *END* 

;Song11A (Main theme 3rd 16 beats voice A)
;Song14A (Song 14 voice A)
8FE4: 81 36 80 36 3A 85 3E 83 42 80 40 08                       ; 1:C5 1/2:C5 1/2:D5 4:E5 2:G5 1/2:F5 1/2:R
8FF0: 28 28 28 08 28 28 28 08 28 28 81 28                       ; 1/2:F4 1/2:F4 1/2:F4 1/2:R 1/2:F4 1/2:F4
8FFC: 28 00                                                     ; 1/2:F4 1/2:R 1/2:F4 1/2:F4 1:F4 1:F4 *END* 

;Song11B (Main theme 3rd 16 beats voice B)
;Song14B (Song 14 voice B)
8FFE: 83 26 81 26 80 26 28 81 2C 80 2C 30                       ; 2:E4 1:E4 1/2:E4 1/2:F4 1:G4 1/2:G4 1/2:A4
900A: 81 32 36 81 30 80 18 18 81 18 80 18                       ; 1:B-4 1:C5 1:A4 1/2:A3 1/2:A3 1:A3 1/2:A3
9016: 18 81 18 80 18 18 81 18 18                                ; 1/2:A3 1:A3 1/2:A3 1/2:A3 1:A3 1:A3 

;Song11C (Main theme 3rd 16 beats voice C)
;Song14C (Song 14 voice C)
901F: 83 1E 82 1E 1E 1C 83 1E 82 1E 1E 1E                       ; 2:C4 2/3:C4 2/3:C4 2/3:B3 2:C4 2/3:C4 2/3:C4
902B: 83 10 10 10 81 14 18                                      ; 2/3:C4 2:F3 2:F3 2:F3 1:G3 1:A3 

;Song13A (Song 13 voice A)
9032: 86 46 83 4E 81 02 08 85 48 83 40 86                       ; 6:B-5 2:C#6 1:C6 1:R 4:A5 2:F5 6:F#5 2:B-5
903E: 06 83 46 81 48 08 85 40 83 40 86 06                       ; 1:A5 1:R 4:F5 2:F5 6:F#5 2:B-5 1:A5 1:R 4:F5
904A: 83 46 81 48 08 85 40 83 3A 86 3C 83                       ; 2:D5 6:E-5 2:F#5 1:F5 1:R 4:C#5 2:B-4 *END* 
9056: 06 81 40 08 85 38 83 32 00                                ; .

;Song13B (Song 13 voice B)
905F: 86 38 83 3E 81 3C 08 85 36 83 30 86                       ; 6:C#5 2:E5 1:E-5 1:R 4:C5 2:A4 6:B4 2:C#5
906B: 34 83 38 81 36 08 85 30 83 30 86 34                       ; 1:C5 1:R 4:A4 2:A4 6:B4 2:C#5 1:C5 1:R 4:A4
9077: 83 38 81 36 08 85 30 83 30 86 2A 83                       ; 2:A4 6:F#4 2:B4 1:B-4 1:R 4:F4 2:C#4 
9083: 34 81 32 08 85 28 83 20                                   ; .

;Song13C (Song 13 voice C)
908B: 83 12 82 12 12 0E 83 12 12 10 82 10                       ; 2:F#3 2/3:F#3 2/3:F#3 2/3:E3 2:F#3 2:F#3
9097: 10 0C 83 10 10 82 0E 1A 20 26 32 38                       ; 2:F3 2/3:F3 2/3:F3 2/3:D#3 2:F3 2:F3 2/3:E3
90A3: 85 3E 83 40 82 10 10 10 85 10 82 0E                       ; 2/3:B-3 2/3:C#4 2/3:E4 2/3:B-4 2/3:C#5 4:E5
90AF: 1A 20 26 32 38 85 3E 83 40 82 10 10                       ; 2:F5 2/3:F3 2/3:F3 2/3:F3 4:F3 2/3:E3
90BB: 10 85 10 83 1C 82 1C 1C 1A 83 1C 82                       ; 2/3:B-3 2/3:C#4 2/3:E4 2/3:B-4 2/3:C#5 4:E5
90C7: 1C 1C 1C 83 1A 82 1A 1A 16 83 1A 82                       ; 2:F5 2/3:F3 2/3:F3 2/3:F3 4:F3 2:B3 2/3:B3
90D3: 1A 1A 1A                                                  ; 2/3:B3 2/3:B-3 2:B3 2/3:B3 2/3:B3 2/3:B3 2:B-3 2/3:B-3 2/3:B-3 2/3:G#3 2:B-3 2/3:B-3 2/3:B-3 2/3:B-3 

;Song11D (Main theme 3rd 16 beats voice D)
;Song13D (Song 13 voice D)
;Song14D (Song 14 voice D)
90D6: D0 90 90 90 D0 D0 00                                      ; *END* 

;Song15A (Song 15 voice A)
;Song15D (Song 15 voice D)
90DD: 83 2C 3A 2C 3A 2C 3A 2C 3A 2A 3A 2A                       ; 2:G4 2:D5 2:G4 2:D5 2:G4 2:D5 2:G4 2:D5
90E9: 3A 2A 3A 2A 3A 28 3A 28 3A 28 3A 28                       ; 2:F#4 2:D5 2:F#4 2:D5 2:F#4 2:D5 2:F#4 2:D5
90F5: 3A 26 3A 26 3A 26 3A 26 3A 00                             ; 2:F4 2:D5 2:F4 2:D5 2:F4 2:D5 2:F4 2:D5 2:E4 2:D5 2:E4 2:D5 2:E4 2:D5 2:E4 2:D5 *END* 

;Song15B (Song 15 voice B)
90FF: 81 08 83 32 3C 32 3C 32 3C 32 3C 30                       ; 1:R 2:B-4 2:E-5 2:B-4 2:E-5 2:B-4 2:E-5
910B: 3C 30 3C 30 3C 30 3C 2E 3C 2E 3C 2E                       ; 2:B-4 2:E-5 2:A4 2:E-5 2:A4 2:E-5 2:A4 2:E-5
9117: 3C 2E 3C 2C 3C 2C 3C 2C 3C 2C 3C                          ; 2:A4 2:E-5 2:G#4 2:E-5 2:G#4 2:E-5 2:G#4 2:E-5 2:G#4 2:E-5 2:G4 2:E-5 2:G4 2:E-5 2:G4 2:E-5 2:G4 2:E-5 

;Song15C (Song 15 voice C)
9122: 85 2C 08 32 3A 38 2A 08 08 28 08 83                       ; 4:G4 4:R 4:B-4 4:D5 4:C#5 4:F#4 4:R 4:R 4:F4
912E: 28 81 08 2E 83 08 38 85 36 26 08 08                       ; 4:R 2:F4 1:R 1:G#4 2:R 2:C#5 4:C5 4:E4 4:R 4:R 

;Song16A (Song 16 voice A)
;Song16D (Song 16 voice D)
913A: 83 24 36 24 36 24 36 24 36 22 36 22                       ; 2:E-4 2:C5 2:E-4 2:C5 2:E-4 2:C5 2:E-4 2:C5
9146: 36 22 36 22 36 1E 30 2A 36 30 3C 3C                       ; 2:D4 2:C5 2:D4 2:C5 2:D4 2:C5 2:D4 2:C5 2:C4
9152: 3C 48 48 00                                               ; 2:A4 2:F#4 2:C5 2:A4 2:E-5 2:E-5 2:E-5 2:A5 2:A5 *END* 

;Song16B (Song 16 voice B)
9156: 81 08 83 2C 3A 2C 3A 2C 3A 2C 3A 2C                       ; 1:R 2:G4 2:D5 2:G4 2:D5 2:G4 2:D5 2:G4 2:D5
9162: 3A 2C 3A 2C 3A 2C 3A 2A 36 30 3C 36                       ; 2:G4 2:D5 2:G4 2:D5 2:G4 2:D5 2:G4 2:D5
916E: 36 06 06 06 02                                            ; 2:F#4 2:C5 2:A4 2:E-5 2:C5 2:C5 2:F#5 2:F#5 2:F#5 2:C6 

;Song16C (Song 16 voice C)
9173: 81 24 22 85 24 83 08 2C 81 08 3C 83                       ; 1:E-4 1:D4 4:E-4 2:R 2:G4 1:R 1:E-5 2:R 2:D5
917F: 08 3A 81 22 20 85 22 83 08 2C 81 08                       ; 1:D4 1:C#4 4:D4 2:R 2:G4 1:R 1:D5 2:R 2:C#5
918B: 3A 83 08 38 81 22 2A 30 2A 30 36 30                       ; 1:D4 1:F#4 1:A4 1:F#4 1:A4 1:C5 1:A4 1:C5
9197: 36 3C 36 3C 06 48 06 3C 36 3C 36 30                       ; 1:E-5 1:C5 1:E-5 1:F#5 1:A5 1:F#5 1:E-5 1:C5
91A3: 2A                                                        ; 1:E-5 1:C5 1:A4 1:F#4 

;Song2A (Song 2 voice A)
;Song2D (Song 2 voice D)
91A4: 82 22 22 22 86 2C 80 2C 30 34 36 86                       ; 2/3:D4 2/3:D4 2/3:D4 6:G4 1/2:G4 1/2:A4
91B0: 3A 82 3A 3A 3A 86 42 80 42 48 4A 02                       ; 1/2:B4 1/2:C5 6:D5 2/3:D5 2/3:D5 2/3:D5 6:G5
91BC: 86 50 80 22 22 08 22 84 2C 00                             ; 1/2:G5 1/2:A5 1/2:B5 1/2:C6 6:D6 1/2:D4 1/2:D4 1/2:R 1/2:D4 3:G4 *END* 

;Song2B (Song 2 voice B)
91C6: 85 08 82 0A 0A 0A 86 14 80 14 18 1C                       ; 4:R 2/3:D3 2/3:D3 2/3:D3 6:G3 1/2:G3 1/2:A3
91D2: 1E 86 22 82 22 22 22 86 2C 80 2C 30                       ; 1/2:B3 1/2:C4 6:D4 2/3:D4 2/3:D4 2/3:D4 6:G4
91DE: 34 36 83 3A 80 12 81 12 80 12 84 1C                       ; 1/2:G4 1/2:A4 1/2:B4 1/2:C5 2:D5 1/2:F#3 1:F#3 1/2:F#3 3:B3 

;Song2C (Song 2 voice C)
91EA: 83 08 85 2C 2C 28 28 24 24 22 83 22                       ; 2:R 4:G4 4:G4 4:F4 4:F4 4:E-4 4:E-4 4:D4
91F6: 80 1E 1E 08 1E 84 22                                      ; 2:D4 1/2:C4 1/2:C4 1/2:R 1/2:C4 3:D4 

;Song5A (Song 5 voice A)
91FD: 84 1C 83 1E 81 16 86 18 85 08 84 1C                       ; 3:B3 2:C4 1:G#3 6:A3 4:R 3:B3 2:C4 1:G#3
9209: 83 1E 81 16 86 18 85 08 84 1C 83 1E                       ; 6:A3 4:R 3:B3 2:C4 1:F4 4:E4 1:R 1:B3 4/3:D4
9215: 81 28 85 26 81 08 1C 87 22 20 18 1E                       ; 4/3:C#4 4/3:A3 4/3:C4 4/3:B3 4/3:G#3 4/3:B3
9221: 1C 16 1C 1A 14 84 28 83 2A 81 22 86                       ; 4/3:B-3 4/3:G3 3:F4 2:F#4 1:D4 6:E-4 4:R
922D: 24 85 08 84 28 83 2A 81 22 86 24 85                       ; 3:F4 2:F#4 1:D4 6:E-4 4:R 3:F4 2:F#4 1:B4
9239: 08 84 28 83 2A 81 34 85 32 81 08 28                       ; 4:B-4 1:R 1:F4 4/3:A4 4/3:G#4 4/3:E-4 4/3:G4
9245: 87 30 2E 24 2C 2A 22 2A 28 20 00                          ; 4/3:F#4 4/3:D4 4/3:F#4 4/3:F4 4/3:C#4 *END* 

;Song5B (Song 5 voice B)
9250: 84 10 83 12 81 0A 86 0C 85 08 84 10                       ; 3:F3 2:F#3 1:D3 6:D#3 4:R 3:F3 2:F#3 1:D3
925C: 83 12 81 0A 86 0C 85 08 84 10 83 12                       ; 6:D#3 4:R 3:F3 2:F#3 1:B3 4:B-3 1:R 1:F3
9268: 81 1C 85 1A 81 08 10 87 16 14 0C 12                       ; 4/3:G#3 4/3:G3 4/3:D#3 4/3:F#3 4/3:F3 4/3:D3
9274: 10 0A 10 0E 04 84 1C 83 1E 81 16 86                       ; 4/3:F3 4/3:E3 4/3:C#3 3:B3 2:C4 1:G#3 6:A3
9280: 18 85 08 84 1C 83 1E 81 16 86 18 85                       ; 4:R 3:B3 2:C4 1:G#3 6:A3 4:R 3:B3 2:C4 1:F4
928C: 08 84 1C 83 1E 81 28 85 26 81 08 1C                       ; 4:E4 1:R 1:B3 4/3:D4 4/3:C#4 4/3:A3 4/3:C4
9298: 87 22 20 18 1E 1C 16 1C 1A 14                             ; 4/3:B3 4/3:G#3 4/3:B3 4/3:B-3 4/3:G3 

;Song5C (Song 5 voice C)
92A2: F8 81 1E 1E F0 F8 81 1C 1C F0 F8 81                       ; 1:C4 1:C4 1:B3 1:B3 1:B-3 1:B-3 1:A3 1:A3
92AE: 1A 1A F0 F4 81 18 18 F0 F8 81 2A 2A                       ; 1:F#4 1:F#4 1:F4 1:F4 1:E4 1:E4 1:E-4 1:E-4 
92BA: F0 F8 81 28 28 F0 F8 81 26 26 F0 F4                       ; .
92C6: 81 24 24 F0                                               ; .

;Song5D (Song 5 voice D)
92CA: 49 00                                                     ; ??:A5 *END* 

;Song1A (Song 1 voice A)
;Song1D (Song 1 voice D)
92CC: 81 14 1E 28 16 20 2A 18 22 2C 87 2E                       ; 1:G3 1:C4 1:F4 1:G#3 1:C#4 1:F#4 1:A3 1:D4
92D8: 30 85 32 00                                               ; 1:G4 4/3:G#4 4/3:A4 4:B-4 *END* 

;Song1B (Song 1 voice B)
92DC: 80 08 81 14 1E 28 16 20 2A 18 22 80                       ; 1/2:R 1:G3 1:C4 1:F4 1:G#3 1:C#4 1:F#4 1:A3
92E8: 2C 87 24 26 85 28                                         ; 1:D4 1/2:G4 4/3:E-4 4/3:E4 4:F4 

;Song1C (Song 1 voice C)
92EE: 84 14 16 18 87 32 34 85 36                                ; 3:G3 3:G#3 3:A3 4/3:B-4 4/3:B4 4:C5 

;Song17A (Song 17 voice A)
;Song18A (Song 18 voice A)
92F7: 83 56 42 02 4C 52 42 5C 4A 5A 02 4C                       ; ~20:G6 ~20:G5 ~20:C6 ~20:E6 ~20:E-6 ~20:G5
9303: 5A 56 02 50 4C 5A 02 54 5A 58 02 50                       ; ~20:B6 ~20:B5 ~20:A6 ~20:C6 ~20:E6 ~20:A6
930F: 54 4C 42 02 4C 50 48 4A 50 00                             ; ~20:G6 ~20:C6 ~20:D6 ~20:E6 ~20:A6 ~20:C6 ~20:F6 ~20:A6 ~20:G#6 ~20:C6 ~20:D6 ~20:F6 ~20:E6 ~20:G5 ~20:C6 ~20:E6 ~20:D6 ~20:A5 ~20:B5 ~20:D6 *END* 

;Song17C (Song 17 voice C)
9319: 87 08 08 08 08 08 08 08 83 08 14 18                       ; ~80:R ~80:R ~80:R ~80:R ~80:R ~80:R ~80:R
9325: 1C                                                        ; ~20:R ~20:G3 ~20:A3 ~20:B3 

;Song18C (Song 18 voice C)
9326: 83 1E 2C 14 2C 1C 2C 14 2C 1E 2C 14                       ; ~20:C4 ~20:G4 ~20:G3 ~20:G4 ~20:B3 ~20:G4
9332: 2C 1E 1E 22 26 28 36 1E 36 28 36 1E                       ; ~20:G3 ~20:G4 ~20:C4 ~20:G4 ~20:G3 ~20:G4
933E: 36 26 36 14 2C 1C 14 18 1C                                ; ~20:C4 ~20:C4 ~20:D4 ~20:E4 ~20:F4 ~20:C5 ~20:C4 ~20:C5 ~20:F4 ~20:C5 ~20:C4 ~20:C5 ~20:E4 ~20:C5 ~20:G3 ~20:G4 ~20:B3 ~20:G3 ~20:A3 ~20:B3 

;Song17B (Song 17 voice B)
;Song18B (Song 18 voice B)
9347: 87 08 08 08 08 08 08 08 08                                ; ~80:R ~80:R ~80:R ~80:R ~80:R ~80:R ~80:R ~80:R 

;Song17D (Song 17 voice D)
;Song18D (Song 18 voice D)
9350: C9 00                                                     ; *END* 

;Song19A (Song 19 voice A)
9352: 86 42 83 3E 85 3C 4A 85 48 08 42 08                       ; ~60:G5 ~20:E5 ~40:E-5 ~40:B5 ~40:A5 ~40:R
935E: 86 48 83 4A 85 50 02 86 42 83 3E 85                       ; ~40:G5 ~40:R ~60:A5 ~20:B5 ~40:D6 ~40:C6
936A: 3A 08 00                                                  ; ~60:G5 ~20:E5 ~40:D5 ~40:R *END* 

;Song19B (Song 19 voice B)
936D: 86 3E 83 36 85 34 3C 3E 08 3E 08 86                       ; ~60:E5 ~20:C5 ~40:B4 ~40:E-5 ~40:E5 ~40:R
9379: 40 83 40 85 40 40 86 36 83 36 85 34                       ; ~40:E5 ~40:R ~60:F5 ~20:F5 ~40:F5 ~40:F5
9385: 08                                                        ; ~60:C5 ~20:C5 ~40:B4 ~40:R 

;Song20A (Song 20 voice A)
;Song22A (Song 22 voice A)
9386: 82 42 81 3E 82 3C 80 3C 84 42 80 4A                       ; ~53:G5 ~27:E5 ~53:E-5 ~7:E-5 ~13:G5 ~7:B5
9392: 82 48 81 3E 87 42 82 48 81 4A 00                          ; ~53:A5 ~27:E5 ~80:G5 ~53:A5 ~27:B5 *END* 

;Song21A (Song 21 voice A)
939D: 83 50 85 02 83 48 82 42 81 3E 87 3A                       ; ~20:D6 ~40:C6 ~20:A5 ~53:G5 ~27:E5 ~80:D5
93A9: 00                                                        ; *END* 

;Song20B (Song 20 voice B)
;Song22B (Song 22 voice B)
93AA: 82 3E 81 36 82 34 80 34 84 3C 80 3C                       ; ~53:E5 ~27:C5 ~53:B4 ~7:B4 ~13:E-5 ~7:E-5
93B6: 82 3E 81 36 87 3E 82 36 81 3A                             ; ~53:E5 ~27:C5 ~80:E5 ~53:C5 ~27:D5 

;Song21B (Song 21 voice B)
93C0: 83 40 85 3E 83 36 82 34 81 2C 87 28                       ; ~20:F5 ~40:E5 ~20:C5 ~53:B4 ~27:G4 ~80:F4 

;Song19C (Song 19 voice C)
;Song20C (Song 20 voice C)
;Song22C (Song 22 voice C)
93CC: 83 1E 2C 14 2C 1C 2C 14 2C 1E 2C 14                       ; ~20:C4 ~20:G4 ~20:G3 ~20:G4 ~20:B3 ~20:G4
93D8: 2C 1E 1E 22 26 28 36 1E 36                                ; ~20:G3 ~20:G4 ~20:C4 ~20:G4 ~20:G3 ~20:G4 ~20:C4 ~20:C4 ~20:D4 ~20:E4 ~20:F4 ~20:C5 ~20:C4 ~20:C5 

;Song21C (Song 21 voice C)
93E1: 28 36 1E 36 26 36 14 2C 1C 14 18 1C                       ; ??:F4 ??:C5 ??:C4 ??:C5 ??:E4 ??:C5 ??:G3 ??:G4 ??:B3 ??:G3 ??:A3 ??:B3 

;Song23A (Song 23 voice A)
93ED: 83 50 85 02 83 50 87 4C 85 08 83 4C                       ; ~20:D6 ~40:C6 ~20:D6 ~80:E6 ~40:R ~20:E6
93F9: 4C 00                                                     ; ~20:E6 *END* 

;Song23B (Song 23 voice B)
93FB: 83 40 85 3E 83 40 87 44 85 08 83 44                       ; ~20:F5 ~40:E5 ~20:F5 ~80:G#5 ~40:R ~20:G#5
9407: 44                                                        ; ~20:G#5 

;Song23C (Song 23 voice C)
9408: 28 36 1E 36 26 3E 34 3E 26 3E 34 3E                       ; ??:F4 ??:C5 ??:C4 ??:C5 ??:E4 ??:E5 ??:B4 ??:E5 ??:E4 ??:E5 ??:B4 ??:E5 

;Song19D (Song 19 voice D)
;Song20D (Song 20 voice D)
;Song21D (Song 21 voice D)
;Song22D (Song 22 voice D)
;Song23D (Song 23 voice D)
9414: C8 11 10 C8 D0 00                                         ; ~7:F3 ~7:F3 *END* 

;Song24A (Song 24 voice A)
941A: 85 50 02 08 83 4A 48 86 42 83 3E 85                       ; ~40:D6 ~40:C6 ~40:R ~20:B5 ~20:A5 ~60:G5
9426: 48 3E 83 3A 3E 40 06 85 42 3E 87 36                       ; ~20:E5 ~40:A5 ~40:E5 ~20:D5 ~20:E5 ~20:F5
9432: 08 00                                                     ; ~20:F#5 ~40:G5 ~40:E5 ~80:C5 ~80:R *END* 

;Song24B (Song 24 voice B)
9434: 85 40 40 08 83 40 40 86 36 83 2C 85                       ; ~40:F5 ~40:F5 ~40:R ~20:F5 ~20:F5 ~60:C5
9440: 38 2C 83 28 2C 30 32 85 34 2C 83 26                       ; ~20:G4 ~40:C#5 ~40:G4 ~20:F4 ~20:G4 ~20:A4
944C: 84 26 80 26 84 08 80 28 84 2C 80 28                       ; ~20:B-4 ~40:B4 ~40:G4 ~20:E4 ~13:E4 ~7:E4
9458: 87 26                                                     ; ~13:R ~7:F4 ~13:G4 ~7:F4 ~80:E4 

;Song24C (Song 24 voice C)
945A: 83 28 36 1E 36 28 36 26 22 1E 2C 14                       ; ~20:F4 ~20:C5 ~20:C4 ~20:C5 ~20:F4 ~20:C5
9466: 2C 20 14 18 14 22 26 28 2A 2C 14 18                       ; ~20:E4 ~20:D4 ~20:C4 ~20:G4 ~20:G3 ~20:G4
9472: 1C 1E 84 1E 80 1E 84 08 80 22 84 26                       ; ~20:C#4 ~20:G3 ~20:A3 ~20:G3 ~20:D4 ~20:E4
947E: 80 22 83 1E 14 18 1C                                      ; ~20:F4 ~20:F#4 ~20:G4 ~20:G3 ~20:A3 ~20:B3 ~20:C4 ~13:C4 ~7:C4 ~13:R ~7:D4 ~13:E4 ~7:D4 ~20:C4 ~20:G3 ~20:A3 ~20:B3 

;Song24D (Song 24 voice D)
9485: C8 11 10 C8 D0 00                                         ; ~7:F3 ~7:F3 *END* 

;Song25A (Song 5 voice A)
948B: 81 32 84 08 28 28 32 82 2E 2A 81 2E                       ; ~80:B-4 ~20:R ~20:F4 ~20:F4 ~20:B-4 ~10:G#4
9497: 80 08 81 32 84 08 2A 2A 32 82 30 2C                       ; ~10:F#4 ~80:G#4 ~60:R ~80:B-4 ~20:R ~20:F#4
94A3: 81 30 80 08 00                                            ; ~20:F#4 ~20:B-4 ~10:A4 ~10:G4 ~80:A4 ~60:R *END* 

;Song25B (Song 5 voice B)
94A8: 83 08 81 32 84 08 28 28 32 82 2E 2A                       ; ~5:R ~80:B-4 ~20:R ~20:F4 ~20:F4 ~20:B-4
94B4: 81 2E 80 08 81 32 84 08 2A 2A 32 82                       ; ~10:G#4 ~10:F#4 ~80:G#4 ~60:R ~80:B-4 ~20:R
94C0: 30 2C 81 30 80 08                                         ; ~20:F#4 ~20:F#4 ~20:B-4 ~10:A4 ~10:G4 ~80:A4 ~60:R 

;Song25C (Song 5 voice C)
94C6: 86 1A 28 81 32 86 16 24 81 2E 86 12                       ; ~40:B-3 ~40:F4 ~80:B-4 ~40:G#3 ~40:E-4
94D2: 20 81 2A 86 10 1E 81 28                                   ; ~80:G#4 ~40:F#3 ~40:C#4 ~80:F#4 ~40:F3 ~40:C4 ~80:F4 

;Song25D (Song 5 voice D)
94DA: 40 00                                                     ; ??:F5 *END* 

;Song26A (Song 26 voice A)
94DC: 81 04 08 81 04 08 86 32 80 28 84 32                       ; ~80:C#3 ~80:R ~80:C#3 ~80:R ~40:B-4 ~60:F4
94E8: 82 32 36 3A 3C 81 40 08 86 32 80 28                       ; ~20:B-4 ~10:B-4 ~10:C5 ~10:D5 ~10:E-5 ~80:F5
94F4: 84 32 82 32 36 3A 3C 81 40 08 00                          ; ~80:R ~40:B-4 ~60:F4 ~20:B-4 ~10:B-4 ~10:C5 ~10:D5 ~10:E-5 ~80:F5 ~80:R *END* 

;Song26D (Song 26 voice D)
94FF: 11 90 90 00                                               ; ??:F3 *END* 

;Song26C (Song 26 voice C)
9503: F6 84 1A 82 1A 1A 84 1A 82 1A 1A F0                       ; ~20:B-3 ~10:B-3 ~10:B-3 ~20:B-3 ~10:B-3
950F: F2 84 16 82 16 16 84 16 82 16 16 F0                       ; ~10:B-3 ~20:G#3 ~10:G#3 ~10:G#3 ~20:G#3
951B: F2 84 12 82 12 12 84 12 82 12 12 F0                       ; ~10:G#3 ~10:G#3 ~20:F#3 ~10:F#3 ~10:F#3
9527: F2 84 10 82 10 10 84 10 82 10 10 F0                       ; ~20:F#3 ~10:F#3 ~10:F#3 ~20:F3 ~10:F3 ~10:F3 ~20:F3 ~10:F3 ~10:F3 

;Song26B (Song 26 voice B)
9533: 84 10 82 10 6C 84 10 82 10 6C 84 10                       ; ~20:F3 ~10:F3 ~10:B-2 ~20:F3 ~10:F3 ~10:B-2
953F: 82 10 6C 10 6C 10 6C 84 10 82 10 6C                       ; ~20:F3 ~10:F3 ~10:B-2 ~10:F3 ~10:B-2 ~10:F3
954B: 84 10 82 10 6C 84 10 82 10 6C 10 6C                       ; ~10:B-2 ~20:F3 ~10:F3 ~10:B-2 ~20:F3 ~10:F3
9557: 10 6C 84 10 82 10 6C 84 10 82 10 6C                       ; ~10:B-2 ~20:F3 ~10:F3 ~10:B-2 ~10:F3 ~10:B-2
9563: 84 10 82 10 6C 10 6C 10 6C 84 0C 1A                       ; ~10:F3 ~10:B-2 ~20:F3 ~10:F3 ~10:B-2 ~20:F3
956F: 82 1A 1E 22 24 84 28 82 0C 68 0C 68                       ; ~10:F3 ~10:B-2 ~20:F3 ~10:F3 ~10:B-2 ~10:F3
957B: 0C 68 84 04 82 04 66 84 04 82 04 66                       ; ~10:B-2 ~10:F3 ~10:B-2 ~20:D#3 ~20:B-3
9587: 84 04 82 04 66 04 66 04 66 84 70 1A                       ; ~10:B-3 ~10:C4 ~10:D4 ~10:E-4 ~20:F4 ~10:D#3
9593: 82 1A 1E 22 24 84 28 82 70 64 70 64                       ; ~10:G#2 ~10:D#3 ~10:G#2 ~10:D#3 ~10:G#2
959F: 70 64                                                     ; ~20:C#3 ~10:C#3 ~10:F#2 ~20:C#3 ~10:C#3 ~10:F#2 ~20:C#3 ~10:C#3 ~10:F#2 ~10:C#3 ~10:F#2 ~10:C#3 ~10:F#2 ~20:C3 ~20:B-3 ~10:B-3 ~10:C4 ~10:D4 ~10:E-4 ~20:F4 ~10:C3 ~10:F2 ~10:C3 ~10:F2 ~10:C3 ~10:F2 

;Song27A (Song 27 voice A)
;Song30A (Song 30 voice A)
95A1: 84 32 08 80 28 84 32 82 32 36 3A 3C                       ; ~20:B-4 ~20:R ~60:F4 ~20:B-4 ~10:B-4 ~10:C5
95AD: 81 40 84 08 40 85 40 06 87 44 00                          ; ~10:D5 ~10:E-5 ~80:F5 ~20:R ~20:F5 ~13:F5 ~13:F#5 ~14:G#5 *END* 

;Song27B (Song 27 voice B)
;Song30B (Song 30 voice B)
95B8: 84 22 08 85 22 22 87 1E 84 22 82 08                       ; ~20:D4 ~20:R ~13:D4 ~13:D4 ~14:C4 ~20:D4
95C4: 22 22 24 28 2C 84 2E 82 08 32 32 36                       ; ~10:R ~10:D4 ~10:D4 ~10:E-4 ~10:F4 ~10:G4
95D0: 3A 3C 86 40 85 2E 32 87 36                                ; ~20:G#4 ~10:R ~10:B-4 ~10:B-4 ~10:C5 ~10:D5 ~10:E-5 ~40:F5 ~13:G#4 ~13:B-4 ~14:C5 

;Song27C (Song 27 voice C)
;Song30C (Song 30 voice C)
95D9: F2 84 1A 82 1A 1A 84 1A 82 1A 1A F0                       ; ~20:B-3 ~10:B-3 ~10:B-3 ~20:B-3 ~10:B-3
95E5: F2 84 16 82 16 16 84 16 82 16 16 F0                       ; ~10:B-3 ~20:G#3 ~10:G#3 ~10:G#3 ~20:G#3 ~10:G#3 ~10:G#3 

;Song28A (Song 28 voice A)
95F1: 81 46 85 08 08 46 46 87 44 06 44 85                       ; ~80:B-5 ~13:R ~13:R ~13:B-5 ~13:B-5 ~14:G#5
95FD: 08 06 81 40 86 40 84 3C 82 3C 40 81                       ; ~14:F#5 ~14:G#5 ~13:R ~13:F#5 ~80:F5 ~40:F5
9609: 06 84 40 3C 38 82 38 3C 81 40 84 3C                       ; ~20:E-5 ~10:E-5 ~10:F5 ~80:F#5 ~20:F5
9615: 38 00                                                     ; ~20:E-5 ~20:C#5 ~10:C#5 ~10:E-5 ~80:F5 ~20:E-5 ~20:C#5 *END* 

;Song28B (Song 28 voice B)
9617: 84 2A 82 08 2A 2A 2E 32 36 85 38 08                       ; ~20:F#4 ~10:R ~10:F#4 ~10:F#4 ~10:G#4
9623: 87 38 38 85 36 32 85 38 08 87 32 85                       ; ~10:B-4 ~10:C5 ~13:C#5 ~13:R ~14:C#5 ~14:C#5
962F: 2E 2E 2A 85 2E 08 87 2E 2E 85 2A 2E                       ; ~13:C5 ~13:B-4 ~13:C#5 ~13:R ~14:B-4 ~13:G#4
963B: 84 2A 82 2A 28 84 2A 82 2A 2E 86 32                       ; ~13:G#4 ~13:F#4 ~13:G#4 ~13:R ~14:G#4
9647: 84 2E 2A 84 28 82 28 24 84 28 82 28                       ; ~14:G#4 ~13:F#4 ~13:G#4 ~20:F#4 ~10:F#4
9653: 2A 86 2E 84 2A 28                                         ; ~10:F4 ~20:F#4 ~10:F#4 ~10:G#4 ~40:B-4 ~20:G#4 ~20:F#4 ~20:F4 ~10:F4 ~10:E-4 ~20:F4 ~10:F4 ~10:F#4 ~40:G#4 ~20:F#4 ~20:F4 

;Song27D (Song 27 voice D)
;Song28D (Song 28 voice D)
;Song30D (Song 30 voice D)
9659: 11 90 90 00                                               ; ??:F3 *END* 

;Song28C (Song 28 voice C)
965D: F2 84 12 82 12 12 84 12 82 12 12 F0                       ; ~20:F#3 ~10:F#3 ~10:F#3 ~20:F#3 ~10:F#3
9669: F2 84 20 82 20 20 84 20 82 20 20 F0                       ; ~10:F#3 ~20:C#4 ~10:C#4 ~10:C#4 ~20:C#4
9675: F2 84 1C 82 1C 1C 84 1C 82 1C 1C F0                       ; ~10:C#4 ~10:C#4 ~20:B3 ~10:B3 ~10:B3 ~20:B3
9681: F2 84 1A 82 1A 1A 84 1A 82 1A 1A F0                       ; ~10:B3 ~10:B3 ~20:B-3 ~10:B-3 ~10:B-3 ~20:B-3 ~10:B-3 ~10:B-3 

;Song29A (Song 29 voice A)
;Song34A (Song 34 voice A)
968D: 86 26 84 26 82 26 28 84 2C 82 2C 30                       ; ~40:E4 ~20:E4 ~10:E4 ~10:F4 ~20:G4 ~10:G4
9699: 84 32 36 18 82 18 18 84 16 82 16 16                       ; ~10:A4 ~20:B-4 ~20:C5 ~20:A3 ~10:A3 ~10:A3
96A5: 84 14 82 14 14 84 12 12 00                                ; ~20:G#3 ~10:G#3 ~10:G#3 ~20:G3 ~10:G3 ~10:G3 ~20:F#3 ~20:F#3 *END* 

;Song29D (Song 29 voice D)
;Song34D (Song 34 voice D)
96AE: 11 90 90 00                                               ; ??:F3 *END* 

;Song29B (Song 29 voice B)
;Song34B (Song 34 voice B)
96B2: 84 36 82 36 3A 81 3E 86 42 82 40 08                       ; ~20:C5 ~10:C5 ~10:D5 ~80:E5 ~40:G5 ~10:F5
96BE: 28 28 28 08 28 28 28 08 28 28 84 28                       ; ~10:R ~10:F4 ~10:F4 ~10:F4 ~10:R ~10:F4
96CA: 28                                                        ; ~10:F4 ~10:F4 ~10:R ~10:F4 ~10:F4 ~20:F4 ~20:F4 

;Song29C (Song 29 voice C)
;Song34C (Song 34 voice C)
96CB: F2 84 1E 82 1E 1E 84 1E 82 1E 1E F0                       ; ~20:C4 ~10:C4 ~10:C4 ~20:C4 ~10:C4 ~10:C4
96D7: 84 28 82 10 10 84 10 82 10 10 84 10                       ; ~20:F4 ~10:F3 ~10:F3 ~20:F3 ~10:F3 ~10:F3
96E3: 82 10 10 84 10 82 14 18                                   ; ~20:F3 ~10:F3 ~10:F3 ~20:F3 ~10:G3 ~10:A3 

;Song31A (Song 31 voice A)
96EB: 81 38 86 08 3E 84 3C 08 81 36 86 30                       ; ~80:C#5 ~40:R ~40:E5 ~20:E-5 ~20:R ~80:C5
96F7: 00                                                        ; ~40:A4 *END* 

;Song31B (Song 31 voice B)
96F8: 81 46 86 08 4E 84 02 08 81 48 86 40                       ; ~80:B-5 ~40:R ~40:C#6 ~20:C6 ~20:R ~80:A5 ~40:F5 

;Song31C (Song 31 voice C)
9704: F2 84 12 82 12 12 84 12 82 12 12 F0                       ; ~20:F#3 ~10:F#3 ~10:F#3 ~20:F#3 ~10:F#3
9710: F2 84 10 82 10 10 84 10 82 10 10 F0                       ; ~10:F#3 ~20:F3 ~10:F3 ~10:F3 ~20:F3 ~10:F3 ~10:F3 

;Song31D (Song 31 voice D)
971C: 11 90 90 00                                               ; ??:F3 *END* 

;Song32A (Song 32 voice A)
9720: 85 62 6C 04 0E 87 1A 20 81 26 86 28                       ; ~13:E2 ~13:B-2 ~13:C#3 ~13:E3 ~14:B-3
972C: 85 10 10 87 10 81 10 85 62 6C 04 0E                       ; ~14:C#4 ~80:E4 ~40:F4 ~13:F3 ~13:F3 ~14:F3
9738: 87 1A 20 81 26 86 28 85 10 10 87 10                       ; ~80:F3 ~13:E2 ~13:B-2 ~13:C#3 ~13:E3 ~14:B-3
9744: 81 10 00                                                  ; ~14:C#4 ~80:E4 ~40:F4 ~13:F3 ~13:F3 ~14:F3 ~80:F3 *END* 

;Song32B (Song 32 voice B)
9747: 81 06 86 08 46 84 48 08 81 40 86 40                       ; ~80:F#5 ~40:R ~40:B-5 ~20:A5 ~20:R ~80:F5
9753: 81 06 86 08 46 84 48 08 81 40 86 3A                       ; ~40:F5 ~80:F#5 ~40:R ~40:B-5 ~20:A5 ~20:R ~80:F5 ~40:D5 

;Song32C (Song 32 voice C)
975F: F2 84 0E 82 0E 0E 84 0E 82 0E 0E F0                       ; ~20:E3 ~10:E3 ~10:E3 ~20:E3 ~10:E3 ~10:E3
976B: F2 84 10 82 10 10 84 10 82 10 10 F0                       ; ~20:F3 ~10:F3 ~10:F3 ~20:F3 ~10:F3 ~10:F3
9777: F2 84 0E 82 0E 0E 84 0E 82 0E 0E F0                       ; ~20:E3 ~10:E3 ~10:E3 ~20:E3 ~10:E3 ~10:E3
9783: F2 84 10 82 10 10 84 10 82 10 10 F0                       ; ~20:F3 ~10:F3 ~10:F3 ~20:F3 ~10:F3 ~10:F3 

;Song33A (Song 33 voice A)
978F: 81 2A 86 08 34 84 32 08 81 28 86 20                       ; ~80:F#4 ~40:R ~40:B4 ~20:B-4 ~20:R ~80:F4
979B: 00                                                        ; ~40:C#4 *END* 

;Song32D (Song 32 voice D)
;Song33D (Song 33 voice D)
979C: 11 90 90 00                                               ; ??:F3 *END* 

;Song33B (Song 33 voice B)
97A0: 81 3C 86 08 06 84 40 08 81 38 86 32                       ; ~80:E-5 ~40:R ~40:F#5 ~20:F5 ~20:R ~80:C#5 ~40:B-4 

;Song33C (Song 33 voice C)
97AC: F2 84 1C 82 1C 1C 84 1C 82 1C 1C F0                       ; ~20:B3 ~10:B3 ~10:B3 ~20:B3 ~10:B3 ~10:B3
97B8: F2 84 1A 82 1A 1A 84 1A 82 1A 1A F0                       ; ~20:B-3 ~10:B-3 ~10:B-3 ~20:B-3 ~10:B-3 ~10:B-3 

;Song35A (Song 35 voice A)
;Song35D (Song 35 voice D)
97C4: 85 36 80 36 36 81 36 82 32 2C 3A 85                       ; 4:C5 1/2:C5 1/2:C5 1:C5 2/3:B-4 2/3:G4
97D0: 36 80 36 36 81 36 82 32 2C 3A 83 36                       ; 2/3:D5 4:C5 1/2:C5 1/2:C5 1:C5 2/3:B-4
97DC: 80 1E 1E 1E 1E 85 1E 00                                   ; 2/3:G4 2/3:D5 2:C5 1/2:C4 1/2:C4 1/2:C4 1/2:C4 4:C4 *END* 

;Song35B (Song 35 voice B)
97E4: 85 26 80 26 26 81 26 82 22 1E 28 85                       ; 4:E4 1/2:E4 1/2:E4 1:E4 2/3:D4 2/3:C4 2/3:F4
97F0: 26 80 26 26 81 26 82 22 1E 28 83 2C                       ; 4:E4 1/2:E4 1/2:E4 1:E4 2/3:D4 2/3:C4 2/3:F4
97FC: 80 14 14 14 14 85 14                                      ; 2:G4 1/2:G3 1/2:G3 1/2:G3 1/2:G3 4:G3 

;Song35C (Song 35 voice C)
9803: 82 26 1E 26 2C 26 2C 32 2C 32 3A 32                       ; 2/3:E4 2/3:C4 2/3:E4 2/3:G4 2/3:E4 2/3:G4
980F: 3A 26 1E 26 2C 26 2C 32 2C 32 3A 32                       ; 2/3:B-4 2/3:G4 2/3:B-4 2/3:D5 2/3:B-4 2/3:D5
981B: 3A 83 36 80 1E 1E 1E 1E 85 1E                             ; 2/3:E4 2/3:C4 2/3:E4 2/3:G4 2/3:E4 2/3:G4 2/3:B-4 2/3:G4 2/3:B-4 2/3:D5 2/3:B-4 2/3:D5 2:C5 1/2:C4 1/2:C4 1/2:C4 1/2:C4 4:C4 
```

# Sound Processing

```code
SoundProcessing: 
9825: A5 E0           LDA     <$E0                ; {ram.??SND_E0??}
9827: F0 0C           BEQ     $9835               ; {}
9829: A9 00           LDA     #$00                ; Disable all ...
982B: 8D 15 40        STA     $4015               ; {hard.S_Status} ... channels
982E: A9 0F           LDA     #$0F                ; Enable Square1, Square2, ...
9830: 8D 15 40        STA     $4015               ; {hard.S_Status} ... Triangle, and Noise (everything but DMC).
9833: D0 11           BNE     $9846               ; {} Has to be NE so this is a jump to process sound effects
;
9835: A9 FF           LDA     #$FF                ; Set bit 1 (and others)
9837: 8D 17 40        STA     $4017               ; {hard.S_FrameCntr} ?? Sync frame-count to sound procesor ??
983A: 20 D5 9A        JSR     $9AD5               ; {code.MusEffect} Process any music effect or music request on square-2
983D: 20 A0 99        JSR     $99A0               ; {} ?? Process any noise effect or noise request
9840: 20 85 9B        JSR     $9B85               ; {code.DModEffect} Process any delta-modulation effect or delta-modulation request
9843: 20 6B 9C        JSR     $9C6B               ; {code.PlayMusic} Process any music
;
9846: 20 CC 98        JSR     $98CC               ; {code.SndEffect} Process any sound effect or sound-effect request on square-1
;
9849: A9 00           LDA     #$00                ; Clear ...
984B: 8D 04 06        STA     $0604               ; {ram.SND_Request} ... the sound-effect request
984E: 8D 03 06        STA     $0603               ; {ram.??SND_603??}
9851: 8D 02 06        STA     $0602               ; {ram.SND_ReqMusEff} Clear the music-effect request
9854: 8D 01 06        STA     $0601               ; {ram.??SND_601??} Clear the delta-modulation request
9857: 8D 00 06        STA     $0600               ; {ram.SND_ReqMusic}
985A: 60              RTS                         ; 
```

# Misc Sounds

```code
MiscSounds: 
; Various sound effects played on the square-1 channel. The table of offsets gives the
; priority if multiple effects are requested. Thus 1) bouncing-off-shield is higher
; priority than the lowest 7) near-death-beeping.
;
; The near-death beeping is prioritized in hard-code. If any sound effect is playing
; then the near-death-beep will NOT preempt it.
;
; These "scripts" are read one byte at a time. These bytes are note numbers whose tones
; are written to the square-1 channel every music pass. Thus these effects are really,
; really short and one-shot fire-and-forget effects not intended to be stopped.
;
; Bytes with the upper-bit set are control values written to square-1 followed immediately
; by a note number. A 00 ends the script.
;
; See the note-table at 9F00.
;
985B: 1C 4C 27 5C 46 67 07 
;
9862: 95 50 08 08 08 08 08 90         ; 7 Near-death beeping
986A: 08 08 08 08 08 08 08 08 
9872: 08 08 08 08 00 

9877: 82 4A 48 4A 08 08 08 08         ; 1 Bouncing off shield
987F: 08 08 00 

9882: 9F 1E 22 24 26 9F 28 2A         ; 3 Wizzrobe magic attack (thanks James Vanderhyde)
988A: 2C 2E 9A 28 2A 2C 2E 9C 
9892: 28 2A 2C 2E 96 28 2A 2C 
989A: 2E 98 28 2A 2C 2E 00 

98A1: 99 42 4A 50 54 00               ; 5 Letters popping up

98A7: 99 70 0A 70 0E 70 10 9F         ; 2 Enemy death
98AF: 70 2A 12 1E 2A 70 1E 00 

98B7: 9A 42 08 08 56 08 08 00         ; 4 Picking up a heart (thanks James Vanderhyde)
98BF: 08 08 00 

98C2: 9F 40 30 40 3A 28 00            ; 6 Picking a letter when entering name

; Request a sound effect. If the upper bit of 604 is set, sound effect processing is
; suspended. If 604 is 0, current sound effect (in 605) continues. The near-death-beeping
; can't interrupt any playing effect (this beeping is a continual effect that will play 
; in the background).
;
98C9: 4C 46 9D        JMP     $9D46               ; {} Jump over large data area (area too big for a relative jump)
```

# Sound Effect

```code
SndEffect: 
98CC: AD 04 06        LDA     $0604               ; {ram.SND_Request} Sound request
98CF: 30 F8           BMI     $98C9               ; {} Sounds suspended .... out
98D1: F0 09           BEQ     $98DC               ; {} No request ... keep playing the current
98D3: C9 40           CMP     #$40                ; Near death beeping?
98D5: D0 0B           BNE     $98E2               ; {} No ... start this effect
98D7: AE 05 06        LDX     $0605               ; {ram.SND_CurEffect} Is there any effect playing?
98DA: F0 06           BEQ     $98E2               ; {} No ... heart sound can play
98DC: AD 05 06        LDA     $0605               ; {ram.SND_CurEffect} Is there a sound effect playing?
98DF: D0 10           BNE     $98F1               ; {} Yes ... go process the tones
98E1: 60              RTS                         ; Done

98E2: 8D 05 06        STA     $0605               ; {ram.SND_CurEffect} Current sound effect
98E5: A0 00           LDY     #$00                ; Bit number ...
98E7: C8              INY                         ; ... in A ...
98E8: 4A              LSR     A                   ; ... to ...
98E9: 90 FC           BCC     $98E7               ; {} ... Y (sound priority from left to right if multiple are given)
98EB: B9 5A 98        LDA     $985A,Y             ; {} Lookup sound effect script
98EE: 8D 0E 06        STA     $060E               ; {ram.060E} Save script for sound effect
;
98F1: AC 0E 06        LDY     $060E               ; {ram.060E} Script pointer to Y
98F4: EE 0E 06        INC     $060E               ; {ram.060E} Bump script pointer
98F7: B9 5B 98        LDA     $985B,Y             ; {code.MiscSounds} Get command
98FA: 30 15           BMI     $9911               ; {} Upper bit set ... this is control and next is note
98FC: D0 1F           BNE     $991D               ; {} If it is just a note, go play it (0 ends script)
;
98FE: A2 90           LDX     #$90                ; Disable decay, no looping, duty cycle to 8+/8-
9900: 8E 00 40        STX     $4000               ; {hard.S_SQR1_A} Reset square 1 [NES] Audio -> Square 1 Control
9903: A2 18           LDX     #$18                ; Wavelength = 0, length counter = 6
9905: 8E 03 40        STX     $4003               ; {hard.S_SQR1_D} Reset square 1 [NES] Audio -> Square 1 Coarse tune
9908: A2 00           LDX     #$00                ; Clear fine ...
990A: 8E 02 40        STX     $4002               ; {hard.S_SQR1_C} ... tune [NES] Audio -> Square 1 Fine tune
990D: 8E 05 06        STX     $0605               ; {ram.SND_CurEffect} Clear the sound-effect-playing flag
9910: 60              RTS                         ; Done

9911: 8D 00 40        STA     $4000               ; {hard.S_SQR1_A} Store sq1 control value [NES] Audio -> Square 1 Control
9914: AC 0E 06        LDY     $060E               ; {ram.060E} Get script pointer
9917: EE 0E 06        INC     $060E               ; {ram.060E} Bump pointer
991A: B9 5B 98        LDA     $985B,Y             ; {code.MiscSounds} Get note value
;
991D: 20 0D 9C        JSR     $9C0D               ; {} Play the note on square 1
9920: A9 7F           LDA     #$7F                ; Bit 7=0 ...
9922: 8D 01 40        STA     $4001               ; {hard.S_SQR1_B} ... disable sweep [NES] Audio -> Square 1 Ramp control
9925: 60              RTS                         ; Done



9926: A9 0F           LDA     #$0F                ; Enable Pulse1, Pulse2, ...
9928: 8D 15 40        STA     $4015               ; {hard.S_Status} ... Triangle, and Noise. [NES] IRQ status / Sound enable
992B: A9 00           LDA     #$00                ; 
992D: 8D 08 06        STA     $0608               ; {ram.SND_DMod1}
9930: 8D 07 06        STA     $0607               ; {ram.SND_CurMusEff}
9933: 8D 1A 06        STA     $061A               ; {ram.061A}
9936: 8D F6 05        STA     $05F6               ; {ram.05F6}
9939: 60              RTS                         ; 

993A: 8C 06 06        STY     $0606               ; {ram.0606}
993D: A9 05           LDA     #$05                ; 
993F: 85 69           STA     <$69                ; {ram.0069}
9941: AD 04 06        LDA     $0604               ; {ram.SND_Request} If anything is requested alongside ...
9944: 29 EF           AND     #$EF                ; ... "letters popping up" then ...
9946: D0 03           BNE     $994B               ; {} ... drop request for ...
9948: 8D 04 06        STA     $0604               ; {ram.SND_Request} ... "letters popping up"
994B: A4 69           LDY     <$69                ; {ram.0069}
994D: B9 BB 9F        LDA     $9FBB,Y             ; {}
9950: D0 1C           BNE     $996E               ; {}
9952: 8C 06 06        STY     $0606               ; {ram.0606}
9955: A9 38           LDA     #$38                ; 
9957: 85 69           STA     <$69                ; {ram.0069}
9959: A9 0D           LDA     #$0D                ; Initialize ...
995B: 85 68           STA     <$68                ; {ram.0068} ... count
995D: C6 68           DEC     <$68                ; {ram.0068} Drop the count
995F: A4 68           LDY     <$68                ; {ram.0068} End of sample table?
9961: F0 F6           BEQ     $9959               ; {} Yes ... go reset
9963: C0 07           CPY     #$07                ; 
9965: 90 04           BCC     $996B               ; {}
9967: A9 10           LDA     #$10                ; 
9969: D0 10           BNE     $997B               ; {}

996B: B9 F8 9E        LDA     $9EF8,Y             ; {}

996E: AA              TAX                         ; Hold value
996F: 29 0F           AND     #$0F                ; Lower 4 bits ...
9971: 8D 0E 40        STA     $400E               ; {hard.S_NOI_C} ... to sample rate [NES] Audio -> Noise Frequency reg #1
9974: 8A              TXA                         ; Restore value
9975: 4A              LSR     A                   ; Get ...
9976: 4A              LSR     A                   ; ... upper ...
9977: 4A              LSR     A                   ; ... four ...
9978: 4A              LSR     A                   ; ... bits
9979: 09 10           ORA     #$10                ; Disable envelope decay
997B: 8D 0C 40        STA     $400C               ; {hard.S_NOI_A} Set noise volume [NES] Audio -> Noise control reg
997E: A9 08           LDA     #$08                ; Set length counter reload ...
9980: 8D 0F 40        STA     $400F               ; {hard.S_NOI_D} ... to 00001 [NES] Audio -> Noise Frequency reg #2
9983: C6 69           DEC     <$69                ; {ram.0069}
9985: D0 0A           BNE     $9991               ; {}
9987: A9 F0           LDA     #$F0                ; Volume ...
9989: 8D 0C 40        STA     $400C               ; {hard.S_NOI_A} ... zero [NES] Audio -> Noise control reg
998C: A9 00           LDA     #$00                ; 
998E: 8D 06 06        STA     $0606               ; {ram.0606}
9991: 60              RTS                         ; 

9992: 8C 06 06        STY     $0606               ; {ram.0606}
9995: A9 0A           LDA     #$0A                ; 
9997: 85 69           STA     <$69                ; {ram.0069}
9999: A4 69           LDY     <$69                ; {ram.0069}
999B: B9 B1 9F        LDA     $9FB1,Y             ; {}
999E: D0 CE           BNE     $996E               ; {}
;
99A0: AC 03 06        LDY     $0603               ; {ram.??SND_603??}
99A3: 30 81           BMI     $9926               ; {}
99A5: AD 06 06        LDA     $0606               ; {ram.0606}
99A8: 4E 03 06        LSR     $0603               ; {ram.??SND_603??}
99AB: B0 E5           BCS     $9992               ; {}
99AD: 4A              LSR     A                   ; 
99AE: B0 E9           BCS     $9999               ; {}
99B0: 4E 03 06        LSR     $0603               ; {ram.??SND_603??}
99B3: B0 85           BCS     $993A               ; {}
99B5: 4A              LSR     A                   ; 
99B6: B0 93           BCS     $994B               ; {}
99B8: 4E 03 06        LSR     $0603               ; {ram.??SND_603??}
99BB: B0 2A           BCS     $99E7               ; {}
99BD: 4A              LSR     A                   ; 
99BE: B0 2E           BCS     $99EE               ; {}
99C0: 4E 03 06        LSR     $0603               ; {ram.??SND_603??}
99C3: B0 8D           BCS     $9952               ; {}
99C5: 4A              LSR     A                   ; 
99C6: B0 95           BCS     $995D               ; {}
99C8: 4E 03 06        LSR     $0603               ; {ram.??SND_603??}
99CB: B0 0C           BCS     $99D9               ; {}
99CD: 4A              LSR     A                   ; 
99CE: B0 10           BCS     $99E0               ; {}
99D0: 4A              LSR     A                   ; 
99D1: B0 36           BCS     $9A09               ; {}
99D3: 4E 03 06        LSR     $0603               ; {ram.??SND_603??}
99D6: B0 25           BCS     $99FD               ; {}
99D8: 60              RTS                         ; 


99D9: 8C 06 06        STY     $0606               ; {ram.0606}
99DC: A9 18           LDA     #$18                ; 
99DE: 85 69           STA     <$69                ; {ram.0069}

99E0: A4 69           LDY     <$69                ; {ram.0069}
99E2: B9 3C 9A        LDA     $9A3C,Y             ; {}
99E5: D0 87           BNE     $996E               ; {}
99E7: 8C 06 06        STY     $0606               ; {ram.0606}
99EA: A9 20           LDA     #$20                ; 
99EC: 85 69           STA     <$69                ; {ram.0069}
99EE: A5 69           LDA     <$69                ; {ram.0069}
99F0: 4A              LSR     A                   ; 
99F1: A8              TAY                         ; 
99F2: A2 0E           LDX     #$0E                ; Coversion to 11 bits as ...
99F4: 8E 0E 40        STX     $400E               ; {hard.S_NOI_C} ... note E6 [NES] Audio -> Noise Frequency reg #1
99F7: B9 C0 9F        LDA     $9FC0,Y             ; {}
99FA: 4C 7B 99        JMP     $997B               ; {}

99FD: 8C 06 06        STY     $0606               ; {ram.0606}
9A00: A9 D0           LDA     #$D0                ; 
9A02: 8D F3 05        STA     $05F3               ; {ram.05F3}
9A05: A9 10           LDA     #$10                ; Volume all ...
9A07: 85 68           STA     <$68                ; {ram.0068} ... the way down
9A09: AD F3 05        LDA     $05F3               ; {ram.05F3}
9A0C: C9 BF           CMP     #$BF                ; 
9A0E: 90 04           BCC     $9A14               ; {}
9A10: E6 68           INC     <$68                ; {ram.0068} Increase the volume
9A12: D0 14           BNE     $9A28               ; {} Didn't overflow ... use it
9A14: AD F3 05        LDA     $05F3               ; {ram.05F3}
9A17: 4A              LSR     A                   ; 
9A18: 90 0E           BCC     $9A28               ; {}
9A1A: 4A              LSR     A                   ; 
9A1B: 90 0B           BCC     $9A28               ; {}
9A1D: 4A              LSR     A                   ; 
9A1E: 90 08           BCC     $9A28               ; {}

9A20: A5 68           LDA     <$68                ; {ram.0068} Current noise volume
9A22: C9 10           CMP     #$10                ; At its lowest?
9A24: F0 02           BEQ     $9A28               ; {} Yes ... leave it there
9A26: C6 68           DEC     <$68                ; {ram.0068} Drop the volume
9A28: A5 68           LDA     <$68                ; {ram.0068} New volume value
9A2A: 8D 0C 40        STA     $400C               ; {hard.S_NOI_A} Set new volume [NES] Audio -> Noise control reg
9A2D: A2 03           LDX     #$03                ; 4 bit conversion ...
9A2F: 8E 0E 40        STX     $400E               ; {hard.S_NOI_C} ... to note  A12 [NES] Audio -> Noise Frequency reg #1
9A32: A9 08           LDA     #$08                ; Length counter load ...
9A34: 8D 0F 40        STA     $400F               ; {hard.S_NOI_D} ... to 00001 [NES] Audio -> Noise Frequency reg #2
9A37: CE F3 05        DEC     $05F3               ; {ram.05F3}
9A3A: 4C 85 99        JMP     $9985               ; {}

9A3D: 1F 2F 2E 3F 3F 4C 4E 5F 6F 6F 7E 8F 9E AF BE CF DE EF FE FD FE FF FF FE  
```

# Misc Music

```code
MiscMusic: 
;
; Note number ... upper bit set for set delay
;
9A55: 0C 08 11 1C 28 33 40 62 
;
9A5D: 8A 4E 58 60                             ; 2 ?? 
9A61: 8A 5E 94 60 00                          ; 1 ?? Change selection

9A66: 8A 42 06 3C 30 2E 3E 44 CC 02 00        ; 3 Discover secret

9A71: 83 40 42 48 4A 02 50 4C 54 94 56 00     ; 4 Picked up something

9A7D: 94 3A 3E A8 50 8A 4E 02 CC 4A 00        ; 5 ?? Short music

9A88: 81 28 3E 24 82 3A 81 16 30 1A 82 34 00  ; 6 Enemy death

9A95: 94 56 42 02 4C 52 42 5C 4A 5A 02 4C 5A  ; 7 ?? Long music ?
9AA2: 56 02 50 4C 5A 02 54 5A 58 02 50 54 4C  ;
9AAF: 42 02 4C 50 48 4A 50 00                 ;

9AB7: 8A 08 08 08 85 3C 3A 38 36 3A 38 36 34  ; 8 ?? Spiraling down ?
9AC4: 38 36 34 32 36 34 32 30 34 32 30 2E 2A  ;
9AD1: 28 A8 26 00                             ;
```

# Music Effect

```code
MusEffect: 
9AD5: AD 02 06        LDA     $0602               ; {ram.SND_ReqMusEff} Get music effect request
9AD8: 30 08           BMI     $9AE2               ; {}
9ADA: D0 0B           BNE     $9AE7               ; {} Requested sound ... do it
9ADC: AD 07 06        LDA     $0607               ; {ram.SND_CurMusEff} Is any sound playing?
9ADF: D0 19           BNE     $9AFA               ; {} Yes ... process it
9AE1: 60              RTS                         ; Out

9AE2: 20 46 9D        JSR     $9D46               ; {}
9AE5: A9 80           LDA     #$80                ; Effect #8 ?? spiraling down

9AE7: 8D 07 06        STA     $0607               ; {ram.SND_CurMusEff} Store effect
9AEA: A0 00           LDY     #$00                ; Count 1st ...
9AEC: C8              INY                         ; ... bit ...
9AED: 4A              LSR     A                   ; ... number ...
9AEE: 90 FC           BCC     $9AEC               ; {} ... from right
9AF0: B9 54 9A        LDA     $9A54,Y             ; {} Get offset to script
9AF3: 8D 18 06        STA     $0618               ; {ram.SND_MusEffDel} Store new script offset
9AF6: A9 01           LDA     #$01                ; Script starts ...
9AF8: 85 6F           STA     <$6F                ; {ram.SND_MusEffCnt} ... now (no delay)
;
9AFA: C6 6F           DEC     <$6F                ; {ram.SND_MusEffCnt} Decrement delay
9AFC: D0 49           BNE     $9B47               ; {} Not time ... warble or hold note
9AFE: AC 18 06        LDY     $0618               ; {ram.SND_MusEffDel} Get script pointer
9B01: EE 18 06        INC     $0618               ; {ram.SND_MusEffDel} Bump script pointer
9B04: B9 55 9A        LDA     $9A55,Y             ; {code.MiscMusic} Get command
9B07: 30 1C           BMI     $9B25               ; {} Delay+note ... go store delay first
9B09: D0 27           BNE     $9B32               ; {} Not end of script ... go do note
;
9B0B: AD 07 06        LDA     $0607               ; {ram.SND_CurMusEff} Ending ...
9B0E: C9 40           CMP     #$40                ; ... the long music ?
9B10: F0 D5           BEQ     $9AE7               ; {} Yes ... start it over
;
9B12: A2 90           LDX     #$90                ; Volume all ...
9B14: 8E 04 40        STX     $4004               ; {hard.S_SQR2_A} ... the way down [NES] Audio -> Square 2 Control
9B17: A2 18           LDX     #$18                ; Wavelength = 0, length counter = 6
9B19: 8E 07 40        STX     $4007               ; {hard.S_SQR2_D} Reset square 2 [NES] Audio -> Square 2 Coarse tune
9B1C: A2 00           LDX     #$00                ; Clear ...
9B1E: 8E 07 06        STX     $0607               ; {ram.SND_CurMusEff} ... current playing music effect
9B21: 8E 06 40        STX     $4006               ; {hard.S_SQR2_C} Clear wavelength [NES] Audio -> Square 2 Fine tune
9B24: 60              RTS                         ; Done
;
9B25: 29 7F           AND     #$7F                ; Mask off upper bit
9B27: 85 6E           STA     <$6E                ; {ram.SND_MusEffRel} Store new delay reload
9B29: AC 18 06        LDY     $0618               ; {ram.SND_MusEffDel} Get pointer to next in script
9B2C: EE 18 06        INC     $0618               ; {ram.SND_MusEffDel} Bump script pointer
9B2F: B9 55 9A        LDA     $9A55,Y             ; {code.MiscMusic} Get note value
;
9B32: 20 2B 9C        JSR     $9C2B               ; {} Note on square 2 (fine value goes to 6B)
9B35: A9 7F           LDA     #$7F                ; Bit 7=0 ...
9B37: 8D 05 40        STA     $4005               ; {hard.S_SQR2_B} ... disable [NES] Audio -> Square 2 Ramp control
9B3A: A9 86           LDA     #$86                ; Set envelope decay rate ...
9B3C: 8D 04 40        STA     $4004               ; {hard.S_SQR2_A} ... to 6 [NES] Audio -> Square 2 Control
9B3F: A5 6E           LDA     <$6E                ; {ram.SND_MusEffRel} Get last delay reload
9B41: 85 6F           STA     <$6F                ; {ram.SND_MusEffCnt} Reset reload
9B43: A9 1F           LDA     #$1F                ; Reset ...
9B45: 85 6D           STA     <$6D                ; {ram.SND_MusEffBell} ... bell-curve envelope
;
9B47: AD 07 06        LDA     $0607               ; {ram.SND_CurMusEff} Current music effect
9B4A: 29 90           AND     #$90                ; Is this effect 1 or 8?
9B4C: F0 16           BEQ     $9B64               ; {} No ... just let the note play as is
9B4E: A4 6D           LDY     <$6D                ; {ram.SND_MusEffBell} Bell curve envelope counter
9B50: F0 02           BEQ     $9B54               ; {} Reached the bottom ... hold that value
9B52: C6 6D           DEC     <$6D                ; {ram.SND_MusEffBell} Decrement the envelope counter
9B54: B9 65 9B        LDA     $9B65,Y             ; {} Get the volume value
9B57: 8D 04 40        STA     $4004               ; {hard.S_SQR2_A} Set volume as per the bell curve [NES] Audio -> Square 2 Control
9B5A: A5 6F           LDA     <$6F                ; {ram.SND_MusEffCnt} Warble count (use current delay count)
9B5C: A6 6B           LDX     <$6B                ; {ram.SND_Sq2Fine} Current frequency
9B5E: 20 54 9C        JSR     $9C54               ; {code.Warble} Do the warble
9B61: 8E 06 40        STX     $4006               ; {hard.S_SQR2_C} Play the note on square 2 [NES] Audio -> Square 2 Fine tune
9B64: 60              RTS                         ; Done

; This table contains volumes for notes played on sq2 over 32 consecutive intervals.
; These basically form a bell curve that rises quickly, holds, then decays quickly.
;
9B65: 95 96 97 98 99 9A 9B 9C 9D 9E 9F 9F 9F 9F 9F 9F 
9B75: 9F 9F 9F 9F 9F 9F 9F 9E 9D 9C 9B 9A 99 98 97 96 
```

# Modulation Effect

```code
DModEffect: 
; The request value in 0601 is used as data in the effect getting stored in 608. If the upper bit
; of the request is 1 then the D/A is initialized with 7F. Otherwise it is initialized with 00.
;
; If either 05F6 or 0608 holds a non-zero value then an effect is in progress and continues. The 05F6
; only gets cleared at 9926. 
;
9B85: AD 01 06        LDA     $0601               ; {ram.??SND_601??} Delta-modulation effect request
9B88: 30 29           BMI     $9BB3               ; {} Upper bit set ... initialize with D/A = 7F
9B8A: D0 23           BNE     $9BAF               ; {} Anything else ... initialize with D/A = 00
;
9B8C: AD 08 06        LDA     $0608               ; {ram.SND_DMod1}
9B8F: F0 18           BEQ     $9BA9               ; {}
9B91: CE F2 05        DEC     $05F2               ; {ram.05F2}
9B94: D0 18           BNE     $9BAE               ; {}
9B96: AD 08 06        LDA     $0608               ; {ram.SND_DMod1}
9B99: 30 18           BMI     $9BB3               ; {}
9B9B: 29 70           AND     #$70                ; 
9B9D: D0 10           BNE     $9BAF               ; {}
9B9F: A9 00           LDA     #$00                ; 
9BA1: 8D 08 06        STA     $0608               ; {ram.SND_DMod1}
9BA4: A9 0F           LDA     #$0F                ; Enable Pulse1, Pulse2, (NOTE NO DeltaMod) ...
9BA6: 8D 15 40        STA     $4015               ; {hard.S_Status} ... Triangle, and Noise. [NES] IRQ status / Sound enable
9BA9: AD F6 05        LDA     $05F6               ; {ram.05F6}
9BAC: D0 09           BNE     $9BB7               ; {}
9BAE: 60              RTS                         ; Done
;
9BAF: A2 00           LDX     #$00                ; D/A to ...
9BB1: F0 04           BEQ     $9BB7               ; {} ... (BRA) full-off
;
9BB3: A2 7F           LDX     #$7F                ; D/A to full-on
9BB5: 29 F0           AND     #$F0                ; 
;
9BB7: 8E 11 40        STX     $4011               ; {hard.S_DMC_B} [NES] Audio -> DPCM D/A data
9BBA: 8D 08 06        STA     $0608               ; {ram.SND_DMod1}
9BBD: AA              TAX                         ; 
9BBE: 29 F0           AND     #$F0                ; 
9BC0: F0 03           BEQ     $9BC5               ; {}
9BC2: 8D F6 05        STA     $05F6               ; {ram.05F6}
9BC5: 8A              TXA                         ; 
9BC6: A0 00           LDY     #$00                ; Count ...
9BC8: C8              INY                         ; ... first bit ...
9BC9: 4A              LSR     A                   ; ... from ...
9BCA: 90 FC           BCC     $9BC8               ; {} ... right (must be 1 to 7)
9BCC: B9 FB 9B        LDA     $9BFB,Y             ; {} Lookup ...
9BCF: 8D 10 40        STA     $4010               ; {hard.S_DMC_A} ... control value [NES] Audio -> DPCM control
9BD2: B9 ED 9B        LDA     $9BED,Y             ; {} Lookup ...
9BD5: 8D 12 40        STA     $4012               ; {hard.S_DMC_C} ... address value [NES] Audio -> DPCM address
9BD8: B9 F4 9B        LDA     $9BF4,Y             ; {} Lookup ...
9BDB: 8D 13 40        STA     $4013               ; {hard.S_DMC_D} ... data length value [NES] Audio -> DPCM data length
9BDE: A9 A0           LDA     #$A0                ; Reset a timer ...
9BE0: 8D F2 05        STA     $05F2               ; {ram.05F2} ... in the effect
9BE3: A9 0F           LDA     #$0F                ; Enable Pulse1, Pulse2, ...
9BE5: 8D 15 40        STA     $4015               ; {hard.S_Status} ... Triangle, and Noise. [NES] IRQ status / Sound enable
9BE8: A9 1F           LDA     #$1F                ; Enable DeltaModulation, Pulse1, Pulse2, ...
9BEA: 8D 15 40        STA     $4015               ; {hard.S_Status} ... Triangle, and Noise. [NES] IRQ status / Sound enable
9BED: 60              RTS                         ; Done
;
; Table of DPCM addresses
9BEE: 00 4C 80 1D 20 28 4C
;
; Table of DPCM data lengths 
9BF5: 75 C0 40 0A B0 90 D0 
;
; Table of DPCM controls
9BFC: 0F 0F 0D 0F 0E 0F 0E 



9C03: 8C 01 40        STY     $4001               ; {hard.S_SQR1_B} Set control [NES] Audio -> Square 1 Ramp control
9C06: 8E 00 40        STX     $4000               ; {hard.S_SQR1_A} Set ramp [NES] Audio -> Square 1 Control
9C09: 60              RTS                         ; Done
;
NoteOnSq1: 
9C0A: 20 03 9C        JSR     $9C03               ; {} Store X and Y to Square 1 Control/Ramp
9C0D: A8              TAY                         ; Note number to Y
9C0E: B9 01 9F        LDA     $9F01,Y             ; {} Fine note frequency
9C11: F0 0D           BEQ     $9C20               ; {} Fine is 0 for silence
9C13: 85 6A           STA     <$6A                ; {ram.SND_Sq1Fine} Remember fine value (for warbling)
9C15: 8D 02 40        STA     $4002               ; {hard.S_SQR1_C} Set fine value [NES] Audio -> Square 1 Fine tune
9C18: B9 00 9F        LDA     $9F00,Y             ; {code.NoteTable} Coarse note frequency
9C1B: 09 08           ORA     #$08                ; Base value
9C1D: 8D 03 40        STA     $4003               ; {hard.S_SQR1_D} Set coarse value [NES] Audio -> Square 1 Coarse tune
9C20: 60              RTS                         ; Done

9C21: 8E 04 40        STX     $4004               ; {hard.S_SQR2_A} Set control [NES] Audio -> Square 2 Control
9C24: 8C 05 40        STY     $4005               ; {hard.S_SQR2_B} Set ramp [NES] Audio -> Square 2 Ramp control
9C27: 60              RTS                         ; Done
;
NoteOnSq2: 
9C28: 20 21 9C        JSR     $9C21               ; {} Store X and Y to Square 2 Control/Ramp
9C2B: A8              TAY                         ; Note number to Y
9C2C: B9 01 9F        LDA     $9F01,Y             ; {} Fine note frequency
9C2F: F0 EF           BEQ     $9C20               ; {} Fine is 0 for silence
9C31: 85 6B           STA     <$6B                ; {ram.SND_Sq2Fine} Remember fine value (for warbling)
9C33: 8D 06 40        STA     $4006               ; {hard.S_SQR2_C} Set fine value [NES] Audio -> Square 2 Fine tune
9C36: B9 00 9F        LDA     $9F00,Y             ; {code.NoteTable} Coarse note frequency
9C39: 09 08           ORA     #$08                ; Length counter load = 00001
9C3B: 8D 07 40        STA     $4007               ; {hard.S_SQR2_D} Set coarse value [NES] Audio -> Square 2 Coarse tune
9C3E: 60              RTS                         ; Done

NoteOnTri: 
9C3F: A8              TAY                         ; Note number to Y
9C40: B9 01 9F        LDA     $9F01,Y             ; {} Fine note frequency
9C43: F0 DB           BEQ     $9C20               ; {} Fine is 0 for silence
9C45: 8D F0 05        STA     $05F0               ; {ram.SND_TriFine} Remember fine value (for warbling)
9C48: 8D 0A 40        STA     $400A               ; {hard.S_TRI_C} Set fine value [NES] Audio -> Triangle Frequency reg1
9C4B: B9 00 9F        LDA     $9F00,Y             ; {code.NoteTable} Coarse note frequency
9C4E: 09 08           ORA     #$08                ; Length counter load = 00001
9C50: 8D 0B 40        STA     $400B               ; {hard.S_TRI_D} Set coarse value [NES] Audio -> Triangle Frequency reg2
9C53: 60              RTS                         ; Done
```

# Warble

```code
Warble: 
; Modify X (A<10 do nothing, A:3==1 then --X, A:3==0 then ++X without wrapping)
; Warbling counts from 0 up and back around.
; 1st 16 leave frequency alone. Then 4 increments (no wrapping) followed by 4 decrements, 4 inc, 
; 4 dec, and so on. Notice how wrapping is only checked on the increment. The decrement doesn't 
; need it since we either did increment 4 (and can come back down 4) or we topped out in which 
; case there is plenty of room to come down. 
;
; If A<10 then X is left alone
; If A bit 3 is 1 OR X=FF 
;   X=X-1 then A=X
; ELSE
;   X=X+1 then A=X
;
9C54: C9 10           CMP     #$10                ; If warble count is less than 10 ...
9C56: 90 0F           BCC     $9C67               ; {} ... keep the original frequency
9C58: 4A              LSR     A                   ; Check ...
9C59: 4A              LSR     A                   ; ... bit ...
9C5A: 4A              LSR     A                   ; ... 3
9C5B: B0 05           BCS     $9C62               ; {} Bit is set ...
9C5D: 8A              TXA                         ; ... go decrement
9C5E: 69 01           ADC     #$01                ; Bit is clear ... increment
9C60: D0 04           BNE     $9C66               ; {} No overflow ... use result
9C62: 8A              TXA                         ; Decrement ...
9C63: 18              CLC                         ; ... by ...
9C64: 69 FF           ADC     #$FF                ; ... adding -1
9C66: AA              TAX                         ; Result back to X
9C67: 60              RTS                         ; Done


9C68: 4C 2C 9D        JMP     $9D2C               ; {} Jump to processing music
```

# Play Music

```code
PlayMusic: 
9C6B: AD 00 06        LDA     $0600               ; {ram.SND_ReqMusic} Get any music request
9C6E: D0 06           BNE     $9C76               ; {} There is one ... go start it
9C70: AD 09 06        LDA     $0609               ; {ram.SND_CurSong} Currently playing music
9C73: D0 F3           BNE     $9C68               ; {} There is a song playing ... keep it going
9C75: 60              RTS                         ; Done

; Initialize a new song
9C76: 8D 09 06        STA     $0609               ; {ram.SND_CurSong} Newly requested music
9C79: 30 18           BMI     $9C93               ; {}
9C7B: C9 06           CMP     #$06                ; 
9C7D: D0 04           BNE     $9C83               ; {}
9C7F: A0 24           LDY     #$24                ; 
9C81: D0 62           BNE     $9CE5               ; {}
9C83: C9 01           CMP     #$01                ; 
9C85: F0 14           BEQ     $9C9B               ; {}
9C87: C9 40           CMP     #$40                ; 
9C89: F0 0C           BEQ     $9C97               ; {}
9C8B: C9 10           CMP     #$10                ; 
9C8D: D0 10           BNE     $9C9F               ; {}
9C8F: A0 11           LDY     #$11                ; 
9C91: D0 0A           BNE     $9C9D               ; {}
;
9C93: A0 19           LDY     #$19                ; 
9C95: D0 06           BNE     $9C9D               ; {}
9C97: A0 0F           LDY     #$0F                ; 
9C99: D0 02           BNE     $9C9D               ; {}
9C9B: A0 08           LDY     #$08                ; 
9C9D: 84 6C           STY     <$6C                ; {ram.006C}
;
9C9F: AA              TAX                         ; 
9CA0: 30 30           BMI     $9CD2               ; {}
9CA2: C9 01           CMP     #$01                ; 
9CA4: F0 20           BEQ     $9CC6               ; {}
9CA6: C9 40           CMP     #$40                ; 
9CA8: F0 10           BEQ     $9CBA               ; {}
9CAA: C9 10           CMP     #$10                ; 
9CAC: D0 30           BNE     $9CDE               ; {}

; Song fragments 14..19 (loop)
9CAE: E6 6C           INC     <$6C                ; {ram.006C}
9CB0: A4 6C           LDY     <$6C                ; {ram.006C}
9CB2: C0 1A           CPY     #$1A                ; 
9CB4: D0 2F           BNE     $9CE5               ; {}
9CB6: A0 14           LDY     #$14                ; 
9CB8: D0 E3           BNE     $9C9D               ; {}

; Song fragments 0F..11 (loop)
9CBA: E6 6C           INC     <$6C                ; {ram.006C}
9CBC: A4 6C           LDY     <$6C                ; {ram.006C}
9CBE: C0 12           CPY     #$12                ; 
9CC0: D0 23           BNE     $9CE5               ; {}
9CC2: A0 0F           LDY     #$0F                ; 
9CC4: D0 D7           BNE     $9C9D               ; {}

; Song fragments 09..0F (loop) Main background music
9CC6: E6 6C           INC     <$6C                ; {ram.006C}
9CC8: A4 6C           LDY     <$6C                ; {ram.006C}
9CCA: C0 10           CPY     #$10                ; 
9CCC: D0 17           BNE     $9CE5               ; {}
9CCE: A0 09           LDY     #$09                ; 
9CD0: D0 CB           BNE     $9C9D               ; {}
;
; Song fragments 19..23 (loop) Splash screen music
9CD2: E6 6C           INC     <$6C                ; {ram.006C} Next song number
9CD4: A4 6C           LDY     <$6C                ; {ram.006C} Have we reached ...
9CD6: C0 24           CPY     #$24                ; ... the end?
9CD8: D0 0B           BNE     $9CE5               ; {} No ... use it
9CDA: A0 19           LDY     #$19                ; Restart ...
9CDC: D0 BF           BNE     $9C9D               ; {} ... at 19
;
9CDE: 8A              TXA                         ; Song number
9CDF: A0 00           LDY     #$00                ; Find ...
9CE1: C8              INY                         ; .. first ...
9CE2: 4A              LSR     A                   ; ... bit from ...
9CE3: 90 FC           BCC     $9CE1               ; {} ... right

9CE5: B9 5F 8D        LDA     $8D5F,Y             ; {} Set ...
9CE8: A8              TAY                         ; ... note ...
9CE9: B9 60 8D        LDA     $8D60,Y             ; {} ... duration ...
9CEC: 8D F4 05        STA     $05F4               ; {ram.05F4} ... list
9CEF: B9 61 8D        LDA     $8D61,Y             ; {} Set ...
9CF2: 85 66           STA     <$66                ; {ram.SND_PtrA} ... pointer ...
9CF4: B9 62 8D        LDA     $8D62,Y             ; {} ... to ...
9CF7: 85 67           STA     <$67                ; {ram.SND_PtrB} ... music
9CF9: B9 63 8D        LDA     $8D63,Y             ; {} Set offset for ...
9CFC: 8D 0C 06        STA     $060C               ; {ram.SND_SongPC_C} ... voice C
9CFF: B9 64 8D        LDA     $8D64,Y             ; {} Set offset for ...
9D02: 8D 0B 06        STA     $060B               ; {ram.SND_SongPC_B} ... voice B
9D05: B9 65 8D        LDA     $8D65,Y             ; {} Set offset for ...
9D08: 8D 0D 06        STA     $060D               ; {ram.SND_SongPC_D} ... voice D
9D0B: 8D F5 05        STA     $05F5               ; {ram.SND_DrumRep} ?? Copy of D for reload
9D0E: B9 66 8D        LDA     $8D66,Y             ; {}
9D11: 8D 19 06        STA     $0619               ; {ram.0619}
9D14: B9 67 8D        LDA     $8D67,Y             ; {}
9D17: 8D F1 05        STA     $05F1               ; {ram.05F1}
9D1A: A9 01           LDA     #$01                ; Music begins on ...
9D1C: 8D 11 06        STA     $0611               ; {ram.SND_Timer} ... next tick
9D1F: 8D 13 06        STA     $0613               ; {ram.0613}
9D22: 8D 16 06        STA     $0616               ; {ram.0616}
9D25: 8D 17 06        STA     $0617               ; {ram.0617}
9D28: 4A              LSR     A                   ; Music program counter for voice A ...
9D29: 8D 0A 06        STA     $060A               ; {ram.SND_SongPC_A} ... to zero (start of song)

9D2C: CE 11 06        DEC     $0611               ; {ram.SND_Timer} Decrement event timer
9D2F: D0 52           BNE     $9D83               ; {} Not time for a new event ... skip on
9D31: AC 0A 06        LDY     $060A               ; {ram.SND_SongPC_A} Get music program counter
9D34: EE 0A 06        INC     $060A               ; {ram.SND_SongPC_A} Bump counter
9D37: B1 66           LDA     ($66),Y             ; {ram.SND_PtrA} Get next music byte
9D39: F0 04           BEQ     $9D3F               ; {} 0 means end of song
9D3B: 10 28           BPL     $9D65               ; {} Upper bit clear ... regular note event
9D3D: D0 18           BNE     $9D57               ; {} (BRA) Upper bit set ... set duration
;
9D3F: AD 09 06        LDA     $0609               ; {ram.SND_CurSong} Current song playing
9D42: 29 F1           AND     #$F1                ; 1111_0001 Part of a sequence of song fragments?
9D44: D0 0E           BNE     $9D54               ; {} Yes ... go back and play next fragment (9C9F)
;
9D46: A9 00           LDA     #$00                ; Stop ...
9D48: 8D 09 06        STA     $0609               ; {ram.SND_CurSong} ... current song
9D4B: 8D 15 40        STA     $4015               ; {hard.S_Status} all sounds. [NES] IRQ status / Sound enable
9D4E: A9 0F           LDA     #$0F                ; Enable Pulse1, Pulse2, ...
9D50: 8D 15 40        STA     $4015               ; {hard.S_Status} ... Triangle, and Noise. [NES] IRQ status / Sound enable
9D53: 60              RTS                         ; Done
9D54: 4C 9F 9C        JMP     $9C9F               ; {} Long BNE from 9D44
;
9D57: 20 E6 9E        JSR     $9EE6               ; {code.GetNoteLen} Look up note duration based on song's note set
9D5A: 8D 10 06        STA     $0610               ; {ram.SND_LenReload} New event timer reload
9D5D: AC 0A 06        LDY     $060A               ; {ram.SND_SongPC_A} Get music program counter
9D60: EE 0A 06        INC     $060A               ; {ram.SND_SongPC_A} Bump counter
9D63: B1 66           LDA     ($66),Y             ; {ram.SND_PtrA} S Get next music byte
;
9D65: AE 07 06        LDX     $0607               ; {ram.SND_CurMusEff} Is there a music effect playing?
9D68: D0 13           BNE     $9D7D               ; {} Yes ... let it have this voice
9D6A: 20 2B 9C        JSR     $9C2B               ; {} Note on square 2
9D6D: F0 03           BEQ     $9D72               ; {} If it was silence, skip next
9D6F: 20 72 9F        JSR     $9F72               ; {}
9D72: 8D 12 06        STA     $0612               ; {ram.0612}
9D75: 20 21 9C        JSR     $9C21               ; {} Set sq2 ramp
9D78: A9 00           LDA     #$00                ; 
9D7A: 8D 1B 06        STA     $061B               ; {ram.061B}
;
9D7D: AD 10 06        LDA     $0610               ; {ram.SND_LenReload} Reset event timer ...
9D80: 8D 11 06        STA     $0611               ; {ram.SND_Timer} ... to current default

9D83: AC 07 06        LDY     $0607               ; {ram.SND_CurMusEff} Is there a music effect playing?
9D86: D0 26           BNE     $9DAE               ; {} Yes ... let it have this voice
9D88: EE 1B 06        INC     $061B               ; {ram.061B}
9D8B: AC 12 06        LDY     $0612               ; {ram.0612}
9D8E: F0 03           BEQ     $9D93               ; {}
9D90: CE 12 06        DEC     $0612               ; {ram.0612}
9D93: 20 7C 9F        JSR     $9F7C               ; {}
9D96: 8D 04 40        STA     $4004               ; {hard.S_SQR2_A} [NES] Audio -> Square 2 Control
9D99: A2 7F           LDX     #$7F                ; 
9D9B: 8E 05 40        STX     $4005               ; {hard.S_SQR2_B} [NES] Audio -> Square 2 Ramp control
9D9E: AD 09 06        LDA     $0609               ; {ram.SND_CurSong}
9DA1: 10 0B           BPL     $9DAE               ; {}
9DA3: AD 1B 06        LDA     $061B               ; {ram.061B}
9DA6: A6 6B           LDX     <$6B                ; {ram.SND_Sq2Fine}
9DA8: 20 54 9C        JSR     $9C54               ; {code.Warble}
9DAB: 8E 06 40        STX     $4006               ; {hard.S_SQR2_C} [NES] Audio -> Square 2 Fine tune

9DAE: AC 0B 06        LDY     $060B               ; {ram.SND_SongPC_B}
9DB1: F0 66           BEQ     $9E19               ; {}
9DB3: CE 13 06        DEC     $0613               ; {ram.0613}
9DB6: D0 36           BNE     $9DEE               ; {}
9DB8: AC 0B 06        LDY     $060B               ; {ram.SND_SongPC_B} S
9DBB: EE 0B 06        INC     $060B               ; {ram.SND_SongPC_B}
9DBE: B1 66           LDA     ($66),Y             ; {ram.SND_PtrA}
9DC0: 10 0E           BPL     $9DD0               ; {}
9DC2: 20 E6 9E        JSR     $9EE6               ; {code.GetNoteLen}
9DC5: 8D 0F 06        STA     $060F               ; {ram.060F}
9DC8: AC 0B 06        LDY     $060B               ; {ram.SND_SongPC_B}
9DCB: EE 0B 06        INC     $060B               ; {ram.SND_SongPC_B}
9DCE: B1 66           LDA     ($66),Y             ; {ram.SND_PtrA}
9DD0: AE 05 06        LDX     $0605               ; {ram.SND_CurEffect} Is there a sound effect playing?
9DD3: D0 13           BNE     $9DE8               ; {} Yes ... skip this
9DD5: 20 0D 9C        JSR     $9C0D               ; {} Note on square 2
9DD8: F0 03           BEQ     $9DDD               ; {}
9DDA: 20 72 9F        JSR     $9F72               ; {}
9DDD: 8D 14 06        STA     $0614               ; {ram.0614}
9DE0: 20 03 9C        JSR     $9C03               ; {}
9DE3: A9 00           LDA     #$00                ; 
9DE5: 8D 1C 06        STA     $061C               ; {ram.061C}
;
9DE8: AD 0F 06        LDA     $060F               ; {ram.060F}
9DEB: 8D 13 06        STA     $0613               ; {ram.0613}
9DEE: AE 05 06        LDX     $0605               ; {ram.SND_CurEffect} Is there a sound effect playing?
9DF1: D0 26           BNE     $9E19               ; {}
9DF3: EE 1C 06        INC     $061C               ; {ram.061C}
9DF6: AC 14 06        LDY     $0614               ; {ram.0614}
9DF9: F0 03           BEQ     $9DFE               ; {}
9DFB: CE 14 06        DEC     $0614               ; {ram.0614}
9DFE: 20 7C 9F        JSR     $9F7C               ; {}
9E01: 8D 00 40        STA     $4000               ; {hard.S_SQR1_A} [NES] Audio -> Square 1 Control
9E04: AD 09 06        LDA     $0609               ; {ram.SND_CurSong}
9E07: 10 0B           BPL     $9E14               ; {}
9E09: AD 1C 06        LDA     $061C               ; {ram.061C}
9E0C: A6 6A           LDX     <$6A                ; {ram.SND_Sq1Fine}
9E0E: 20 54 9C        JSR     $9C54               ; {code.Warble}
9E11: 8E 02 40        STX     $4002               ; {hard.S_SQR1_C} [NES] Audio -> Square 1 Fine tune
9E14: A9 7F           LDA     #$7F                ; 
9E16: 8D 01 40        STA     $4001               ; {hard.S_SQR1_B} [NES] Audio -> Square 1 Ramp control

9E19: AD 0C 06        LDA     $060C               ; {ram.SND_SongPC_C}
9E1C: D0 03           BNE     $9E21               ; {}
9E1E: 4C 95 9E        JMP     $9E95               ; {}

9E21: CE 16 06        DEC     $0616               ; {ram.0616}
9E24: D0 52           BNE     $9E78               ; {}
9E26: AC 0C 06        LDY     $060C               ; {ram.SND_SongPC_C}
9E29: EE 0C 06        INC     $060C               ; {ram.SND_SongPC_C}
9E2C: B1 66           LDA     ($66),Y             ; {ram.SND_PtrA}
9E2E: F0 62           BEQ     $9E92               ; {}
9E30: 10 38           BPL     $9E6A               ; {}
9E32: C9 F0           CMP     #$F0                ; 
9E34: F0 11           BEQ     $9E47               ; {}
9E36: 90 1D           BCC     $9E55               ; {}
9E38: 38              SEC                         ; 
9E39: E9 F0           SBC     #$F0                ; 
9E3B: 8D 1E 06        STA     $061E               ; {ram.061E}
9E3E: AD 0C 06        LDA     $060C               ; {ram.SND_SongPC_C}
9E41: 8D 1F 06        STA     $061F               ; {ram.061F}
9E44: 4C 26 9E        JMP     $9E26               ; {}
9E47: CE 1E 06        DEC     $061E               ; {ram.061E}
9E4A: F0 06           BEQ     $9E52               ; {}
9E4C: AD 1F 06        LDA     $061F               ; {ram.061F}
9E4F: 8D 0C 06        STA     $060C               ; {ram.SND_SongPC_C}
9E52: 4C 26 9E        JMP     $9E26               ; {}
9E55: 20 E6 9E        JSR     $9EE6               ; {code.GetNoteLen}
9E58: 8D 15 06        STA     $0615               ; {ram.0615}
9E5B: A9 1F           LDA     #$1F                ; 
9E5D: 8D 08 40        STA     $4008               ; {hard.S_TRI_A} [NES] Audio -> Triangle Control
9E60: AC 0C 06        LDY     $060C               ; {ram.SND_SongPC_C}
9E63: EE 0C 06        INC     $060C               ; {ram.SND_SongPC_C}
9E66: B1 66           LDA     ($66),Y             ; {ram.SND_PtrA}
9E68: F0 28           BEQ     $9E92               ; {}
9E6A: 20 3F 9C        JSR     $9C3F               ; {code.NoteOnTri}
9E6D: A9 00           LDA     #$00                ; 
9E6F: 8D 1D 06        STA     $061D               ; {ram.061D}
9E72: AE 15 06        LDX     $0615               ; {ram.0615}
9E75: 8E 16 06        STX     $0616               ; {ram.0616}
;
9E78: EE 1D 06        INC     $061D               ; {ram.061D} Bump warble
9E7B: AD 1D 06        LDA     $061D               ; {ram.061D} Get the warble count ...
9E7E: AE F0 05        LDX     $05F0               ; {ram.SND_TriFine} .. and the current note frequency
9E81: 20 54 9C        JSR     $9C54               ; {code.Warble} Warble the note frequency in X
9E84: 8E 0A 40        STX     $400A               ; {hard.S_TRI_C} Play the note on triangle voice [NES] Audio -> Triangle Frequence reg1
9E87: AD F1 05        LDA     $05F1               ; {ram.05F1}
9E8A: 10 04           BPL     $9E90               ; {}
9E8C: A9 1F           LDA     #$1F                ; 
9E8E: D0 02           BNE     $9E92               ; {}
9E90: A9 FF           LDA     #$FF                ; 
9E92: 8D 08 40        STA     $4008               ; {hard.S_TRI_A} ?? intro music voice [NES] Audio -> Triangle Control
;
9E95: AD 09 06        LDA     $0609               ; {ram.SND_CurSong} Current song number
9E98: 29 91           AND     #$91                ; 1001_0001 Does song have drums in it?
9E9A: F0 37           BEQ     $9ED3               ; {} No ... skip drums
9E9C: CE 17 06        DEC     $0617               ; {ram.0617}
9E9F: D0 32           BNE     $9ED3               ; {}
9EA1: AC 0D 06        LDY     $060D               ; {ram.SND_SongPC_D}
9EA4: EE 0D 06        INC     $060D               ; {ram.SND_SongPC_D}
9EA7: B1 66           LDA     ($66),Y             ; {ram.SND_PtrA}
9EA9: D0 08           BNE     $9EB3               ; {}
9EAB: AD F5 05        LDA     $05F5               ; {ram.SND_DrumRep}
9EAE: 8D 0D 06        STA     $060D               ; {ram.SND_SongPC_D}
9EB1: D0 EE           BNE     $9EA1               ; {}

; Music drums

9EB3: 20 E0 9E        JSR     $9EE0               ; {}
9EB6: 8D 17 06        STA     $0617               ; {ram.0617}
9EB9: 8A              TXA                         ; 
9EBA: 29 3E           AND     #$3E                ; 00111110
9EBC: 4A              LSR     A                   ; 00000011
9EBD: 4A              LSR     A                   ; 
9EBE: 4A              LSR     A                   ; 
9EBF: 4A              LSR     A                   ; 
9EC0: A8              TAY                         ; 
9EC1: B9 D4 9E        LDA     $9ED4,Y             ; {}
9EC4: 8D 0C 40        STA     $400C               ; {hard.S_NOI_A}
9EC7: B9 D8 9E        LDA     $9ED8,Y             ; {}
9ECA: 8D 0E 40        STA     $400E               ; {hard.S_NOI_C}
9ECD: B9 DC 9E        LDA     $9EDC,Y             ; {}
9ED0: 8D 0F 40        STA     $400F               ; {hard.S_NOI_D}
9ED3: 60              RTS                         ; 

; Four different drum notes. ?? seems to be the durration of the noise 
; all at the same frequency. ?? First note is "off"
9ED4: 10 1C 1C 1C 
9ED8: 00 03 0A 03 
9EDC: 00 18 18 58 

; abcdefg
; g->CAR
; bcdefgg
; cdefgga
; defggab

9EE0: AA              TAX                         ; 
9EE1: 6A              ROR     A                   ; 
9EE2: 8A              TXA                         ; 
9EE3: 2A              ROL     A                   ; 
9EE4: 2A              ROL     A                   ; 
9EE5: 2A              ROL     A                   ; 
;
GetNoteLen: 
; Get the note duration indexed within the current song's
; set of durations.
9EE6: 29 07           AND     #$07                ; Each duration-set has 8 entries
9EE8: 18              CLC                         ; Index into ...
9EE9: 6D F4 05        ADC     $05F4               ; {ram.05F4} ... set defined for song
9EEC: A8              TAY                         ; Get ...
9EED: B9 D1 9F        LDA     $9FD1,Y             ; {code.NoteDelaySet} ... note duration
9EF0: 60              RTS                         ; Done

Get0NoteLen: 
; Get the note duration indexed within the first
; set of durations.
9EF1: 29 07           AND     #$07                ; Within set 0
9EF3: A8              TAY                         ; Get ...
9EF4: B9 D1 9F        LDA     $9FD1,Y             ; {code.NoteDelaySet} ... note duration
9EF7: 60              RTS                         ; Done

9EF8: CB 0E 0E 4C 6D 8C CD FF  
```

# Note Table

```code
NoteTable: 
; Note table (coarse/fine). Frequencies to the duty cycle are 1.79MHz/(N+1).
; Frequencies are divided down by 16. There may be some other small factor
; in the formula since large frequencies begin to show errors with expected
; frequencies. The notes in the table are mostly in order with a few notes
; left out and moved to the beginning or end.
;
9F00: 00 23 ; 3107.6    G7
9F02: 00 6A ; 1045.5    C6
9F04: 03 27 ; 138.4     C#3
9F06: 00 97 ; 736.0     F#5
9F08: 00 00 ;   0.0     R
9F0A: 02 F9 ; 146.8     D3
9F0C: 02 CF ; 155.3     D#3
9F0E: 02 A6 ; 164.7     E3
9F10: 02 80 ; 174.5     F3
9F12: 02 5C ; 184.9     F#3
9F14: 02 3A ; 195.9     G3
9F16: 02 1A ; 207.5     G#3
9F18: 01 FC ; 219.7     A3
9F1A: 01 DF ; 233.0     B-3
9F1C: 01 C4 ; 246.9     B3
9F1E: 01 AB ; 261.3     C4
9F20: 01 93 ; 276.9     C#4
9F22: 01 7C ; 293.6     D4
9F24: 01 67 ; 310.7     E-4
9F26: 01 53 ; 329.0     E4
9F28: 01 40 ; 348.5     F4
9F2A: 01 2E ; 369.2     F#4
9F2C: 01 1D ; 391.1     G4
9F2E: 01 0D ; 414.3     G#4
9F30: 00 FE ; 438.7     A4
9F32: 00 EF ; 466.1     B-4
9F34: 00 E2 ; 492.8     B4
9F36: 00 D5 ; 522.7     C5
9F38: 00 C9 ; 553.8     C#5
9F3A: 00 BE ; 585.7     D5
9F3C: 00 B3 ; 621.5     E-5
9F3E: 00 A9 ; 658.0     E5
9F40: 00 A0 ; 694.8     F5
9F42: 00 8E ; 782.3     G5
9F44: 00 86 ; 828.7     G#5
9F46: 00 77 ; 932.2     B-5
9F48: 00 7E ; 880.9     A5
9F4A: 00 71 ; 981.3     B5
9F4C: 00 54 ; 1316.1    E6
9F4E: 00 64 ; 1107.6    C#6
9F50: 00 5F ; 1165.3    D6
9F52: 00 59 ; 1243.0    E-6
9F54: 00 50 ; 1381.1    F6
9F56: 00 47 ; 1553.8    G6
9F58: 00 43 ; 1645.2    G#6
9F5A: 00 3F ; 1748.0    A6
9F5C: 00 38 ; 1962.7    B6
9F5E: 00 32 ; 2193.6    C7
9F60: 00 21 ; 3290.4    G#7
9F62: 05 4D ; 82.3      E2
9F64: 05 01 ; 87.2      F2
9F66: 04 B9 ; 92.4      F#2
9F68: 04 35 ; 103.7     G#2
9F6A: 03 F8 ; 110.0     A2
9F6C: 03 BF ; 116.5     B-2
9F6E: 03 89 ; 123.4     B2
9F70: 03 57 ; 130.6     C3

9F72: AD 19 06        LDA     $0619               ; {ram.0619}
9F75: A9 20           LDA     #$20                ; 
9F77: A2 82           LDX     #$82                ; 
9F79: A0 7F           LDY     #$7F                ; 
9F7B: 60              RTS                         ; 

9F7C: AD 19 06        LDA     $0619               ; {ram.0619}
9F7F: 10 07           BPL     $9F88               ; {}
9F81: B9 92 9F        LDA     $9F92,Y             ; {}
9F84: 29 0F           AND     #$0F                ; 
9F86: D0 07           BNE     $9F8F               ; {}
9F88: B9 92 9F        LDA     $9F92,Y             ; {}
9F8B: 4A              LSR     A                   ; 
9F8C: 4A              LSR     A                   ; 
9F8D: 4A              LSR     A                   ; 
9F8E: 4A              LSR     A                   ; 
9F8F: 09 90           ORA     #$90                ; 
9F91: 60              RTS                         ; 

; ?? Control values for square-voice (controlls durration -- short values create short notes) 
9F92: 04 24 24 34 34 35 35 35 45 45 46 46 46 46 46 46 
9FA2: 46 46 57 57 57 57 68 68 68 68 79 79 79 68 68 

9FB1: 57 47 67 87 A8 B9 9A 8A 5A 9B 

9FBB: 8B FB F9 9D 6E 3F
 
9FC1: 1A 1A 1C 1D 1D 1E 1E 1F 1F 1E 1A 19 16 13 11 11 
```

# Note Delay Set

```code
NoteDelaySet: 
; Each song points to a set of 8 note duration values. For songs with harmony these beats have
; to be timed carefully. The comments below are in the form I:T(D) where:
;   I is the index in the note set (0 - 7)
;   T is the number of timer tics
;   D is the translated duration in either beats (like 1/3, 1, 2) or pure tics (like ~7).
;
9FD1: 03 0A 01 14 05 28 3C 70 ; 0:3(1/3)  1:10(1)   2:1(1/10) 3:20(2)   4:5(1/2)  5:40(4)   6:60(6)   7:112(10/112)
9FD9: 07 1B 35 14 0D 28 3C 50 ; 0:7(~7)   1:27(~27) 2:53(~53) 3:20(~20) 4:13(~13) 5:40(~40) 6:60(~60) 7:80(~80)                                
9FE1: 06 0C 08 18 24 30 48 10 ; 0:6(1/2)  1:12(1)   2:8(2/3)  3:24(2)   4:36(3)   5:48(4)   6:72(6)   7:16(4/3) <- main theme uses this
9FE9: 07 0D 09 1B 24 36 48 10 ; 0:7(~7)   1:13(~13) 2:9(~9)   3:27(~27) 4:36(~36) 5:54(~54) 6:72(~72) 7:16(~16)
9FF1: 3C 50 0A 05 14 0D 28 0E ; 0:60(~60) 1:80(~80) 2:10(~10) 3:5(~5)   4:20(~20) 5:13(~13) 6:40(~40) 7:14(~14)

9FF9: FF FF FF FF FF FF FF 
A000: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
A020: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
A040: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
A060: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
A080: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
A0A0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
A0C0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
A0E0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
A100: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
A120: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
A140: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
A160: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
A180: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
A1A0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
A1C0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
A1E0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
A200: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
A220: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
A240: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
A260: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
A280: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
A2A0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
A2C0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
A2E0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
A300: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
A320: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
A340: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
A360: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
A380: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
A3A0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
A3C0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
A3E0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
A400: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
A420: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
A440: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
A460: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
A480: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
A4A0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
A4C0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
A4E0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
A500: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
A520: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
A540: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
A560: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
A580: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
A5A0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
A5C0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
A5E0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
A600: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
A620: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
A640: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
A660: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
A680: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
A6A0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
A6C0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
A6E0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
A700: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
A720: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
A740: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
A760: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
A780: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
A7A0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
A7C0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
A7E0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
A800: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
A820: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
A840: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
A860: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
A880: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
A8A0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
A8C0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
A8E0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
A900: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
A920: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
A940: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
A960: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
A980: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
A9A0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
A9C0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
A9E0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
AA00: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
AA20: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
AA40: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
AA60: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
AA80: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
AAA0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
AAC0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
AAE0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
AB00: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
AB20: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
AB40: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
AB60: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
AB80: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
ABA0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
ABC0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
ABE0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
AC00: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
AC20: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
AC40: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
AC60: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
AC80: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
ACA0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
ACC0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
ACE0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
AD00: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
AD20: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
AD40: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
AD60: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
AD80: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
ADA0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
ADC0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
ADE0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
AE00: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
AE20: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
AE40: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
AE60: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
AE80: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
AEA0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
AEC0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
AEE0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
AF00: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
AF20: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
AF40: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
AF60: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
AF80: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
AFA0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
AFC0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
AFE0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
B000: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
B020: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
B040: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
B060: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
B080: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
B0A0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
B0C0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
B0E0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
B100: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
B120: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
B140: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
B160: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
B180: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
B1A0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
B1C0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
B1E0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
B200: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
B220: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
B240: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
B260: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
B280: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
B2A0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
B2C0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
B2E0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
B300: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
B320: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
B340: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
B360: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
B380: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
B3A0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
B3C0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
B3E0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
B400: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
B420: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
B440: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
B460: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
B480: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
B4A0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
B4C0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
B4E0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
B500: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
B520: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
B540: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
B560: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
B580: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
B5A0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
B5C0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
B5E0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
B600: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
B620: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
B640: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
B660: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
B680: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
B6A0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
B6C0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
B6E0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
B700: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
B720: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
B740: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
B760: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
B780: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
B7A0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
B7C0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
B7E0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
B800: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
B820: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
B840: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
B860: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
B880: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
B8A0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
B8C0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
B8E0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
B900: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
B920: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
B940: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
B960: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
B980: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
B9A0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
B9C0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
B9E0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
BA00: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
BA20: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
BA40: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
BA60: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
BA80: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
BAA0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
BAC0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
BAE0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
BB00: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
BB20: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
BB40: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
BB60: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
BB80: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
BBA0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
BBC0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
BBE0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
BC00: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
BC20: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
BC40: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
BC60: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
BC80: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
BCA0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
BCC0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
BCE0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
BD00: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
BD20: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
BD40: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
BD60: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
BD80: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
BDA0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
BDC0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
BDE0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
BE00: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
BE20: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
BE40: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
BE60: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
BE80: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
BEA0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
BEC0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
BEE0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
BF00: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
BF20: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
BF40: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 

; From here down is the same in all banks (except for the origin
; difference in bank 7).
```

# RESET 

```code
RESET: 
;
; Configure the MMC1 and jump to E440 (Bank 7) for startup.
;
BF50: 78              SEI                         ; Disable interrupts
BF51: D8              CLD                         ; Clear decimal flag
BF52: A9 00           LDA     #$00                ; Clear the PPU control register ...
BF54: 8D 00 20        STA     $2000               ; {hard.P_CNTRL_1} ... truns off NMIs
BF57: A2 FF           LDX     #$FF                ; Stack to ...
BF59: 9A              TXS                         ; ... 01FF
BF5A: AD 02 20        LDA     $2002               ; {hard.P_STATUS} Wait ...
BF5D: 29 80           AND     #$80                ; ... for ...
BF5F: F0 F9           BEQ     $BF5A               ; {} ... VBLANK
BF61: AD 02 20        LDA     $2002               ; {hard.P_STATUS} Wait ...
BF64: 29 80           AND     #$80                ; ... for another ...
BF66: F0 F9           BEQ     $BF61               ; {} ... VBLANK (1st might have been a leftover flag)
BF68: 09 FF           ORA     #$FF                ; Reset ...
BF6A: 8D 00 80        STA     $8000               ; {} ... ...
BF6D: 8D 00 A0        STA     $A000               ; {} ... all ...
BF70: 8D 00 C0        STA     $C000               ; ... four ...
BF73: 8D 00 E0        STA     $E000               ; ... MMC1 registers
BF76: A9 0F           LDA     #$0F                ; Set MMC control to 8K CHR ROM, fixed/bank 16K PRG pages, ...
BF78: 20 98 BF        JSR     $BF98               ; {code.MMC_Control} ... and horizontal mirroring (vertical scrolling)
BF7B: A9 00           LDA     #$00                ; Set MMC reg1 VROM bank
BF7D: 8D 00 A0        STA     $A000               ; {} The cartridge doesn't ...
BF80: 4A              LSR     A                   ; ... swap VROM pages. ...
BF81: 8D 00 A0        STA     $A000               ; {} ... Just ...
BF84: 4A              LSR     A                   ; ... set ...
BF85: 8D 00 A0        STA     $A000               ; {} ... to ...
BF88: 4A              LSR     A                   ; ...
BF89: 8D 00 A0        STA     $A000               ; {} ...
BF8C: 4A              LSR     A                   ; ...
BF8D: 8D 00 A0        STA     $A000               ; {} ... --00000
BF90: A9 07           LDA     #$07                ; Interesting! Put bank 7 ...
BF92: 20 AC BF        JSR     $BFAC               ; {code.MMC_Bank} ... in the low ROM bank
BF95: 4C 40 E4        JMP     $E440               ; Start of game

; MMC1 Info
; R0 - Control ***CPPMM
;  C CHR ROM bank mode. Zelda uses 0: 8KB at a time
;  PP Program ROM switch mode. Zelda uses 3: 16K fixed, 16K switched banks
;  MM Name table mirroring. Zelda uses 2 or 3: vertical or horizontal
; R1 - CHR bank size ***CCCCC
;  Ignored in Zelda since R0.C is 0
; R2 - CHR bank select ***CCCCC
;  Ignored in Zelda since R0.C is 0
; R3 - PRG bank select ***RPPPP
;  R PRG RAM enabled. Zelda sends 0, but battery-backed RAM is always enabled.
;  PPPP bank select. Zelda switches banks 0-6.
```

# MMC Control

```code
MMC_Control: 
; Set the MMC Control register (0) to value in A
BF98: 8D 00 80        STA     $8000               ; {} MMC Register 0 (control): --edcba ...
BF9B: 4A              LSR     A                   ; ... mirroring
BF9C: 8D 00 80        STA     $8000               ; {} ... mirroring
BF9F: 4A              LSR     A                   ; ... switch: c=0 high ROM, C=1 low ROM
BFA0: 8D 00 80        STA     $8000               ; {} ... size: d=0 32K (full), D=1 16K (half)
BFA3: 4A              LSR     A                   ; ... chrrom mode: e=0 8K banks, B=1 4K banks
BFA4: 8D 00 80        STA     $8000               ; {} The MMC is write-trigger (write to ROM ...
BFA7: 4A              LSR     A                   ; .. has no affect anyway).
BFA8: 8D 00 80        STA     $8000               ; {} Bits are written from LSB to MSB ...
BFAB: 60              RTS                         ; ... only 5 bits
```

# MMC Bank

```code
MMC_Bank: 
; Set the MMC Bank register (3) to value in A
BFAC: 8D 00 E0        STA     $E000               ; MMC Register 3 (ROM page switching): --edcba ...
BFAF: 4A              LSR     A                   ; ...
BFB0: 8D 00 E0        STA     $E000               ; ... Write the ...
BFB3: 4A              LSR     A                   ; ... switching ...
BFB4: 8D 00 E0        STA     $E000               ; ... page ...
BFB7: 4A              LSR     A                   ; ... number
BFB8: 8D 00 E0        STA     $E000               ; The MMC is write-trigger (write to ROM ...
BFBB: 4A              LSR     A                   ; .. has no affect anyway).
BFBC: 8D 00 E0        STA     $E000               ; Bits are written from LSB to MSB ...
BFBF: 60              RTS                         ; ... only 5 bits

BFC0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
BFD0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
BFE0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
BFF0: FF FF FF FF FF FF FF FF FF FF
```

# Vectors

```code
BFFA: 84 E4       ; NMI to E484
BFFC: 50 BF       ; RESET to BF50
BFFE: F0 BF       ; IRQ to BFF0 (this bank should never be at end)
```

