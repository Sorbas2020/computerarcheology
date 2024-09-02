![Bank 5](Zelda.jpg)

# Bank 5

>>> cpu 6502

>>> binary 8000:roms/Zelda.nes[14010:18010]

>>> memoryTable ram 

[RAM Usage](RAMUse.md)

>>> memoryTable hard 

[Hardware Info](Hardware.md)

```code
8000: 20 06 80        JSR     $8006               ; {}
8003: 4C 89 ED        JMP     $ED89               ; 
8006: A5 E1           LDA     <$E1                ; {ram.00E1}
8008: A4 10           LDY     <$10                ; {ram.0010}
800A: F0 15           BEQ     $8021               ; {}
800C: 20 E2 E5        JSR     $E5E2               ; 
800F: 56 80           LSR     $80,X               ; {ram.0080}
8011: 38              SEC                         ; 
8012: 80                              ;
8013: 57                              ;
8014: 80                              ;
8015: 5E 80 62        LSR     $6280,X             ; 
8018: 80                              ;
8019: 66 80           ROR     <$80                ; {ram.0080}
801B: 76 80           ROR     <$80,X              ; {ram.0080}
801D: D4                              ;
801E: 80                              ;
801F: 0F                              ;
8020: 81 20           STA     ($20,X)             ; {ram.0020}
8022: E2                              ;
8023: E5 56           SBC     <$56                ; {ram.0056}
8025: 80                              ;
8026: 9A              TXS                         ; 
8027: 81 38           STA     ($38,X)             ; {ram.0038}
8029: 80                              ;
802A: 57                              ;
802B: 80                              ;
802C: 5E 80 62        LSR     $6280,X             ; 
802F: 80                              ;
8030: 6C 80 70        JMP     ($7080)             ; {ram.7080}
8033: 80                              ;
8034: D4                              ;
8035: 80                              ;
8036: 0F                              ;
8037: 81 20           STA     ($20,X)             ; {ram.0020}
8039: F7                              ;
803A: E5 20           SBC     <$20                ; {ram.0020}
803C: DE 71 20        DEC     $2071,X             ; 
803F: 79 E6 A9        ADC     $A9E6,Y             ; {}
8042: EF                              ;
8043: 85 FC           STA     <$FC                ; {ram.CUR_VScroll}
8045: 85 5C           STA     <$5C                ; {ram.!FlipFlag}
8047: A9 01           LDA     #$01                ; 
8049: 20 30 81        JSR     $8130               ; {}
804C: E6 E1           INC     <$E1                ; {ram.00E1}
804E: A9 2B           LDA     #$2B                ; 
8050: 85 5E           STA     <$5E                ; {ram.005E}
8052: A9 7F           LDA     #$7F                ; 
8054: 85 5D           STA     <$5D                ; {ram.005D}
8056: 60              RTS                         ; 
8057: A9 48           LDA     #$48                ; 
8059: 85 14           STA     <$14                ; {ram.0014}
805B: E6 E1           INC     <$E1                ; {ram.00E1}
805D: 60              RTS                         ; 
805E: A9 4A           LDA     #$4A                ; 
8060: D0 F7           BNE     $8059               ; {}
8062: A9 4C           LDA     #$4C                ; 
8064: D0 F3           BNE     $8059               ; {}
8066: 20 3A B2        JSR     $B23A               ; {}
8069: 4C 5B 80        JMP     $805B               ; {}
806C: A9 5C           LDA     #$5C                ; 
806E: D0 E9           BNE     $8059               ; {}
8070: 20 82 B2        JSR     $B282               ; {}
8073: 4C 79 80        JMP     $8079               ; {}
8076: 20 3A B2        JSR     $B23A               ; {}
8079: A9 03           LDA     #$03                ; 
807B: 20 30 81        JSR     $8130               ; {}
807E: A5 FC           LDA     <$FC                ; {ram.CUR_VScroll}
8080: 38              SEC                         ; 
8081: E9 03           SBC     #$03                ; 
8083: 85 FC           STA     <$FC                ; {ram.CUR_VScroll}
8085: C9 41           CMP     #$41                ; 
8087: D0 4A           BNE     $80D3               ; {}
8089: E6 E1           INC     <$E1                ; {ram.00E1}
808B: A5 10           LDA     <$10                ; {ram.0010}
808D: F0 44           BEQ     $80D3               ; {}
808F: A5 12           LDA     <$12                ; {ram.0012}
8091: C9 09           CMP     #$09                ; 
8093: F0 3E           BEQ     $80D3               ; {}
8095: A5 EB           LDA     <$EB                ; {ram.00EB}
8097: 29 0F           AND     #$0F                ; 
8099: 0A              ASL     A                   ; 
809A: 0A              ASL     A                   ; 
809B: 0A              ASL     A                   ; 
809C: 85 00           STA     <$00                ; {ram.GP_00}
809E: AD AB 6B        LDA     $6BAB               ; {ram.6BAB}
80A1: C9 08           CMP     #$08                ; 
80A3: 90 0E           BCC     $80B3               ; {}
80A5: A9 10           LDA     #$10                ; 
80A7: ED AB 6B        SBC     $6BAB               ; {ram.6BAB}
80AA: 0A              ASL     A                   ; 
80AB: 0A              ASL     A                   ; 
80AC: 0A              ASL     A                   ; 
80AD: 20 21 70        JSR     $7021               ; {ram.7021}
80B0: 4C B6 80        JMP     $80B6               ; {}
80B3: 0A              ASL     A                   ; 
80B4: 0A              ASL     A                   ; 
80B5: 0A              ASL     A                   ; 
80B6: 18              CLC                         ; 
80B7: 65 00           ADC     <$00                ; {ram.GP_00}
80B9: 18              CLC                         ; 
80BA: 69 62           ADC     #$62                ; 
80BC: 8D 53 02        STA     $0253               ; {ram.0253}
80BF: A5 EB           LDA     <$EB                ; {ram.00EB}
80C1: 29 F0           AND     #$F0                ; 
80C3: 4A              LSR     A                   ; 
80C4: 69 69           ADC     #$69                ; 
80C6: 8D 50 02        STA     $0250               ; {ram.0250}
80C9: A9 3E           LDA     #$3E                ; 
80CB: 8D 51 02        STA     $0251               ; {ram.0251}
80CE: A9 00           LDA     #$00                ; 
80D0: 8D 52 02        STA     $0252               ; {ram.0252}
80D3: 60              RTS                         ; 
80D4: 20 A7 B6        JSR     $B6A7               ; {}
80D7: 20 26 B7        JSR     $B726               ; {}
80DA: A5 FB           LDA     <$FB                ; {ram.00FB}
80DC: 29 88           AND     #$88                ; 
80DE: C9 88           CMP     #$88                ; 
80E0: D0 11           BNE     $80F3               ; {}
80E2: 20 A3 EB        JSR     $EBA3               ; 
80E5: 85 E1           STA     <$E1                ; {ram.00E1}
80E7: A9 08           LDA     #$08                ; 
80E9: 85 12           STA     <$12                ; {ram.0012}
80EB: A9 00           LDA     #$00                ; 
80ED: 8D 19 06        STA     $0619               ; {ram.0619}
80F0: 4C 8E 8A        JMP     $8A8E               ; {}
80F3: A5 F8           LDA     <$F8                ; {ram.00F8}
80F5: 29 10           AND     #$10                ; 
80F7: F0 58           BEQ     $8151               ; {}
80F9: AD 54 02        LDA     $0254               ; {ram.0254}
80FC: 48              PHA                         ; 
80FD: AD 58 02        LDA     $0258               ; {ram.0258}
8100: 48              PHA                         ; 
8101: 20 F7 E5        JSR     $E5F7               ; 
8104: 68              PLA                         ; 
8105: 8D 58 02        STA     $0258               ; {ram.0258}
8108: 68              PLA                         ; 
8109: 8D 54 02        STA     $0254               ; {ram.0254}
810C: E6 E1           INC     <$E1                ; {ram.00E1}
810E: 60              RTS                         ; 
810F: A9 FD           LDA     #$FD                ; 
8111: 20 30 81        JSR     $8130               ; {}
8114: A5 FC           LDA     <$FC                ; {ram.CUR_VScroll}
8116: 18              CLC                         ; 
8117: 69 03           ADC     #$03                ; 
8119: 85 FC           STA     <$FC                ; {ram.CUR_VScroll}
811B: C9 F0           CMP     #$F0                ; 
811D: 90 32           BCC     $8151               ; {}
811F: 85 5C           STA     <$5C                ; {ram.!FlipFlag}
8121: A5 10           LDA     <$10                ; {ram.0010}
8123: F0 03           BEQ     $8128               ; {}
8125: 20 12 75        JSR     $7512               ; {ram.7512}
8128: A9 00           LDA     #$00                ; 
812A: 85 FC           STA     <$FC                ; {ram.CUR_VScroll}
812C: 85 E1           STA     <$E1                ; {ram.00E1}
812E: A9 02           LDA     #$02                ; 
8130: 85 00           STA     <$00                ; {ram.GP_00}
8132: AD 54 02        LDA     $0254               ; {ram.0254}
8135: C9 F8           CMP     #$F8                ; 
8137: F0 06           BEQ     $813F               ; {}
8139: 18              CLC                         ; 
813A: 65 00           ADC     <$00                ; {ram.GP_00}
813C: 8D 54 02        STA     $0254               ; {ram.0254}
813F: A5 10           LDA     <$10                ; {ram.0010}
8141: F0 0E           BEQ     $8151               ; {}
8143: 20 EB B5        JSR     $B5EB               ; {}
8146: F0 09           BEQ     $8151               ; {}
8148: AD 58 02        LDA     $0258               ; {ram.0258}
814B: 18              CLC                         ; 
814C: 65 00           ADC     <$00                ; {ram.GP_00}
814E: 8D 58 02        STA     $0258               ; {ram.0258}
8151: 60              RTS                         ; 
8152: 00              BRK                         ; 
8153: 08              PHP                         ; 
8154: 09 01           ORA     #$01                ; 
8156: 0A              ASL     A                   ; 
8157: 0B                              ;
8158: 12                              ;
8159: 1E 1F 17        ASL     $171F,X             ; 
815C: 24 25           BIT     <$25                ; {ram.0025}
815E: 13                              ;
815F: 14                              ;
8160: 21 13           AND     ($13,X)             ; {ram.0013}
8162: 20 21 15        JSR     $1521               ; 
8165: 16 22           ASL     $22,X               ; {ram.0022}
8167: 16 22           ASL     $22,X               ; {ram.0022}
8169: 23                              ;
816A: E7                              ;
816B: E7                              ;
816C: F5 E8           SBC     $E8,X               ; {ram.00E8}
816E: F5 E8           SBC     $E8,X               ; {ram.00E8}
8170: E7                              ;
8171: E7                              ;
8172: F5 E8           SBC     $E8,X               ; {ram.00E8}
8174: F5 E8           SBC     $E8,X               ; {ram.00E8}
8176: E5 F5           SBC     <$F5                ; {ram.TileFlagA}
8178: E5 E8           SBC     <$E8                ; {ram.00E8}
817A: F5 E8           SBC     $E8,X               ; {ram.00E8}
817C: F5 E6           SBC     $E6,X               ; {ram.00E6}
817E: E6 E7           INC     <$E7                ; {ram.00E7}
8180: E7                              ;
8181: F5 E9           SBC     $E9,X               ; {ram.00E9}
8183: E9 24           SBC     #$24                ; 
8185: EA              NOP                         ; 
8186: 24 EA           BIT     <$EA                ; {ram.00EA}
8188: E9 E9           SBC     #$E9                ; 
818A: 24 EA           BIT     <$EA                ; {ram.00EA}
818C: 24 EA           BIT     <$EA                ; {ram.00EA}
818E: 24 24           BIT     <$24                ; {ram.0024}
8190: 24 24           BIT     <$24                ; {ram.0024}
8192: 24 24           BIT     <$24                ; {ram.0024}
8194: 24 24           BIT     <$24                ; {ram.0024}
8196: 24 24           BIT     <$24                ; {ram.0024}
8198: 24 24           BIT     <$24                ; {ram.0024}
819A: A0 17           LDY     #$17                ; 
819C: BE 52 81        LDX     $8152,Y             ; {}
819F: B9 82 81        LDA     $8182,Y             ; {}
81A2: 9D 4B 68        STA     $684B,X             ; 
81A5: 88              DEY                         ; 
81A6: 10 F4           BPL     $819C               ; {}
81A8: C8              INY                         ; 
81A9: A9 01           LDA     #$01                ; 
81AB: 85 06           STA     <$06                ; {ram.0006}
81AD: A9 03           LDA     #$03                ; 
81AF: 85 07           STA     <$07                ; {ram.0007}
81B1: BE 52 81        LDX     $8152,Y             ; {}
81B4: A5 06           LDA     <$06                ; {ram.0006}
81B6: 2C 71 06        BIT     $0671               ; {ram.0671}
81B9: F0 16           BEQ     $81D1               ; {}
81BB: BD 4B 68        LDA     $684B,X             ; 
81BE: C9 E5           CMP     #$E5                ; 
81C0: F0 0A           BEQ     $81CC               ; {}
81C2: C9 E6           CMP     #$E6                ; 
81C4: F0 06           BEQ     $81CC               ; {}
81C6: B9 6A 81        LDA     $816A,Y             ; {}
81C9: 4C CE 81        JMP     $81CE               ; {}
81CC: A9 F5           LDA     #$F5                ; 
81CE: 9D 4B 68        STA     $684B,X             ; 
81D1: C8              INY                         ; 
81D2: C6 07           DEC     <$07                ; {ram.0007}
81D4: D0 DB           BNE     $81B1               ; {}
81D6: 06 06           ASL     <$06                ; {ram.0006}
81D8: D0 D3           BNE     $81AD               ; {}
81DA: E6 E1           INC     <$E1                ; {ram.00E1}
81DC: 60              RTS                         ; 
81DD: A5 15           LDA     <$15                ; {ram.0015}
81DF: 29 03           AND     #$03                ; 
81E1: A4 10           LDY     <$10                ; {ram.0010}
81E3: D0 02           BNE     $81E7               ; {}
81E5: 29 01           AND     #$01                ; 
81E7: C5 E6           CMP     <$E6                ; {ram.00E6}
81E9: D0 6A           BNE     $8255               ; {}
81EB: A9 08           LDA     #$08                ; 
81ED: 24 98           BIT     <$98                ; {ram.0098}
81EF: F0 37           BEQ     $8228               ; {}
81F1: C6 E9           DEC     <$E9                ; {ram.00E9}
81F3: A5 84           LDA     <$84                ; {ram.0084}
81F5: C9 DD           CMP     #$DD                ; 
81F7: B0 04           BCS     $81FD               ; {}
81F9: 69 08           ADC     #$08                ; 
81FB: 85 84           STA     <$84                ; {ram.0084}
81FD: A5 E2           LDA     <$E2                ; {ram.00E2}
81FF: 38              SEC                         ; 
8200: E9 20           SBC     #$20                ; 
8202: 85 E2           STA     <$E2                ; {ram.00E2}
8204: B0 02           BCS     $8208               ; {}
8206: C6 58           DEC     <$58                ; {ram.0058}
8208: C9 E0           CMP     #$E0                ; 
820A: D0 12           BNE     $821E               ; {}
820C: A5 58           LDA     <$58                ; {ram.0058}
820E: C9 20           CMP     #$20                ; 
8210: F0 0D           BEQ     $821F               ; {}
8212: C9 27           CMP     #$27                ; 
8214: D0 08           BNE     $821E               ; {}
8216: A9 23           LDA     #$23                ; 
8218: 85 58           STA     <$58                ; {ram.0058}
821A: A9 A0           LDA     #$A0                ; 
821C: 85 E2           STA     <$E2                ; {ram.00E2}
821E: 60              RTS                         ; 
821F: E6 58           INC     <$58                ; {ram.0058}
8221: A9 00           LDA     #$00                ; 
8223: 85 E2           STA     <$E2                ; {ram.00E2}
8225: E6 13           INC     <$13                ; {ram.0013}
8227: 60              RTS                         ; 
8228: 4A              LSR     A                   ; 
8229: 24 98           BIT     <$98                ; {ram.0098}
822B: F0 28           BEQ     $8255               ; {}
822D: E6 E9           INC     <$E9                ; {ram.00E9}
822F: A5 84           LDA     <$84                ; {ram.0084}
8231: C9 3E           CMP     #$3E                ; 
8233: 90 04           BCC     $8239               ; {}
8235: E9 08           SBC     #$08                ; 
8237: 85 84           STA     <$84                ; {ram.0084}
8239: A5 E2           LDA     <$E2                ; {ram.00E2}
823B: 18              CLC                         ; 
823C: 69 20           ADC     #$20                ; 
823E: 85 E2           STA     <$E2                ; {ram.00E2}
8240: 90 02           BCC     $8244               ; {}
8242: E6 58           INC     <$58                ; {ram.0058}
8244: C9 C0           CMP     #$C0                ; 
8246: D0 3F           BNE     $8287               ; {}
8248: A5 58           LDA     <$58                ; {ram.0058}
824A: C9 23           CMP     #$23                ; 
824C: D0 39           BNE     $8287               ; {}
824E: A9 28           LDA     #$28                ; 
8250: 85 58           STA     <$58                ; {ram.0058}
8252: 4C 21 82        JMP     $8221               ; {}
8255: A9 02           LDA     #$02                ; 
8257: A2 FE           LDX     #$FE                ; 
8259: A4 10           LDY     <$10                ; {ram.0010}
825B: D0 03           BNE     $8260               ; {}
825D: 0A              ASL     A                   ; 
825E: A2 FC           LDX     #$FC                ; 
8260: 85 00           STA     <$00                ; {ram.GP_00}
8262: 86 01           STX     <$01                ; {ram.GP_01}
8264: A9 02           LDA     #$02                ; 
8266: 24 98           BIT     <$98                ; {ram.0098}
8268: F0 1E           BEQ     $8288               ; {}
826A: C6 E8           DEC     <$E8                ; {ram.00E8}
826C: A5 70           LDA     <$70                ; {ram.0070}
826E: C9 F0           CMP     #$F0                ; 
8270: B0 04           BCS     $8276               ; {}
8272: 65 00           ADC     <$00                ; {ram.GP_00}
8274: 85 70           STA     <$70                ; {ram.0070}
8276: A5 FD           LDA     <$FD                ; {ram.CUR_HScroll}
8278: 38              SEC                         ; 
8279: E5 00           SBC     <$00                ; {ram.GP_00}
827B: 85 FD           STA     <$FD                ; {ram.CUR_HScroll}
827D: F0 A6           BEQ     $8225               ; {}
827F: C5 01           CMP     <$01                ; {ram.GP_01}
8281: D0 04           BNE     $8287               ; {}
8283: A9 01           LDA     #$01                ; 
8285: 85 5F           STA     <$5F                ; {ram.005F}
8287: 60              RTS                         ; 
8288: 4A              LSR     A                   ; 
8289: 24 98           BIT     <$98                ; {ram.0098}
828B: F0 FA           BEQ     $8287               ; {}
828D: E6 E8           INC     <$E8                ; {ram.00E8}
828F: A5 70           LDA     <$70                ; {ram.0070}
8291: C9 01           CMP     #$01                ; 
8293: 90 04           BCC     $8299               ; {}
8295: E5 00           SBC     <$00                ; {ram.GP_00}
8297: 85 70           STA     <$70                ; {ram.0070}
8299: A5 FD           LDA     <$FD                ; {ram.CUR_HScroll}
829B: 18              CLC                         ; 
829C: 65 00           ADC     <$00                ; {ram.GP_00}
829E: 85 FD           STA     <$FD                ; {ram.CUR_HScroll}
82A0: D0 E5           BNE     $8287               ; {}
82A2: 20 83 82        JSR     $8283               ; {}
82A5: 4C 25 82        JMP     $8225               ; {}
82A8: A5 13           LDA     <$13                ; {ram.0013}
82AA: 20 E2 E5        JSR     $E5E2               ; 
82AD: 0E 83 BB        ASL     $BB83               ; {}
82B0: 82                              ;
82B1: 1F                              ;
82B2: 83                              ;
82B3: 3D 83 3D        AND     $3D83,X             ; 
82B6: 83                              ;
82B7: 5C                              ;
82B8: 83                              ;
82B9: 9E                              ;
82BA: 83                              ;
82BB: 20 3D EA        JSR     $EA3D               ; 
82BE: 20 38 F2        JSR     $F238               ; 
82C1: A5 EE           LDA     <$EE                ; {ram.00EE}
82C3: 8D 21 05        STA     $0521               ; {ram.0521}
82C6: 20 C2 83        JSR     $83C2               ; {}
82C9: C6 ED           DEC     <$ED                ; {ram.00ED}
82CB: E6 13           INC     <$13                ; {ram.0013}
82CD: 20 8F E6        JSR     $E68F               ; 
82D0: A5 EC           LDA     <$EC                ; {ram.00EC}
82D2: 30 20           BMI     $82F4               ; {}
82D4: A5 EB           LDA     <$EB                ; {ram.00EB}
82D6: 48              PHA                         ; 
82D7: A4 98           LDY     <$98                ; {ram.0098}
82D9: C0 08           CPY     #$08                ; 
82DB: F0 04           BEQ     $82E1               ; {}
82DD: A5 EC           LDA     <$EC                ; {ram.00EC}
82DF: 85 EB           STA     <$EB                ; {ram.00EB}
82E1: 20 D7 83        JSR     $83D7               ; {}
82E4: A9 15           LDA     #$15                ; 
82E6: 85 E9           STA     <$E9                ; {ram.00E9}
82E8: A4 98           LDY     <$98                ; {ram.0098}
82EA: C0 08           CPY     #$08                ; 
82EC: F0 07           BEQ     $82F5               ; {}
82EE: 20 C4 A8        JSR     $A8C4               ; {}
82F1: 68              PLA                         ; 
82F2: 85 EB           STA     <$EB                ; {ram.00EB}
82F4: 60              RTS                         ; 
82F5: 20 FB 82        JSR     $82FB               ; {}
82F8: 4C F1 82        JMP     $82F1               ; {}
82FB: A5 10           LDA     <$10                ; {ram.0010}
82FD: F0 0E           BEQ     $830D               ; {}
82FF: A5 EE           LDA     <$EE                ; {ram.00EE}
8301: 48              PHA                         ; 
8302: AD 21 05        LDA     $0521               ; {ram.0521}
8305: 85 EE           STA     <$EE                ; {ram.00EE}
8307: 20 F6 A4        JSR     $A4F6               ; {}
830A: 68              PLA                         ; 
830B: 85 EE           STA     <$EE                ; {ram.00EE}
830D: 60              RTS                         ; 
830E: AD 22 05        LDA     $0522               ; {ram.0522}
8311: F0 04           BEQ     $8317               ; {}
8313: A5 EA           LDA     <$EA                ; {ram.00EA}
8315: 85 EB           STA     <$EB                ; {ram.00EB}
8317: AD 1A 05        LDA     $051A               ; {ram.051A}
831A: F0 1E           BEQ     $833A               ; {}
831C: 4C 34 FF        JMP     $FF34               ; 
831F: 20 24 A9        JSR     $A924               ; {}
8322: AD 02 03        LDA     $0302               ; {ram.0302}
8325: 29 0F           AND     #$0F                ; 
8327: 18              CLC                         ; 
8328: 69 27           ADC     #$27                ; 
832A: 8D 02 03        STA     $0302               ; {ram.0302}
832D: A5 98           LDA     <$98                ; {ram.0098}
832F: C9 04           CMP     #$04                ; 
8331: B0 03           BCS     $8336               ; {}
8333: EE 02 03        INC     $0302               ; {ram.0302}
8336: C6 E9           DEC     <$E9                ; {ram.00E9}
8338: 10 02           BPL     $833C               ; {}
833A: E6 13           INC     <$13                ; {ram.0013}
833C: 60              RTS                         ; 
833D: A9 08           LDA     #$08                ; 
833F: 24 98           BIT     <$98                ; {ram.0098}
8341: D0 05           BNE     $8348               ; {}
8343: 4A              LSR     A                   ; 
8344: 24 98           BIT     <$98                ; {ram.0098}
8346: F0 10           BEQ     $8358               ; {}
8348: A9 C0           LDA     #$C0                ; 
834A: A0 17           LDY     #$17                ; 
834C: A6 13           LDX     <$13                ; {ram.0013}
834E: E0 03           CPX     #$03                ; 
8350: F0 03           BEQ     $8355               ; {}
8352: 20 8C 84        JSR     $848C               ; {}
8355: 4C A4 8C        JMP     $8CA4               ; {}
8358: A9 D0           LDA     #$D0                ; 
835A: D0 EE           BNE     $834A               ; {}
835C: A9 00           LDA     #$00                ; 
835E: 8D 1C 05        STA     $051C               ; {ram.051C}
8361: A5 98           LDA     <$98                ; {ram.0098}
8363: C9 04           CMP     #$04                ; 
8365: B0 04           BCS     $836B               ; {}
8367: A0 4E           LDY     #$4E                ; 
8369: 84 14           STY     <$14                ; {ram.0014}
836B: C9 08           CMP     #$08                ; 
836D: D0 0D           BNE     $837C               ; {}
836F: A5 EB           LDA     <$EB                ; {ram.00EB}
8371: 48              PHA                         ; 
8372: A5 EC           LDA     <$EC                ; {ram.00EC}
8374: 85 EB           STA     <$EB                ; {ram.00EB}
8376: 20 C4 A8        JSR     $A8C4               ; {}
8379: 68              PLA                         ; 
837A: 85 EB           STA     <$EB                ; {ram.00EB}
837C: A4 EC           LDY     <$EC                ; {ram.00EC}
837E: 20 8D B6        JSR     $B68D               ; {}
8381: F0 20           BEQ     $83A3               ; {}
8383: A4 EB           LDY     <$EB                ; {ram.00EB}
8385: 20 8D B6        JSR     $B68D               ; {}
8388: D0 0D           BNE     $8397               ; {}
838A: A9 00           LDA     #$00                ; 
838C: 8D 1F 05        STA     $051F               ; {ram.051F}
838F: A9 40           LDA     #$40                ; 
8391: 8D 1C 05        STA     $051C               ; {ram.051C}
8394: E6 13           INC     <$13                ; {ram.0013}
8396: 60              RTS                         ; 
8397: AD 1F 05        LDA     $051F               ; {ram.051F}
839A: D0 EE           BNE     $838A               ; {}
839C: F0 05           BEQ     $83A3               ; {}
839E: 20 B7 74        JSR     $74B7               ; {ram.74B7}
83A1: D0 0A           BNE     $83AD               ; {}
83A3: A5 EC           LDA     <$EC                ; {ram.00EC}
83A5: 85 EB           STA     <$EB                ; {ram.00EB}
83A7: 20 B2 83        JSR     $83B2               ; {}
83AA: 20 90 6C        JSR     $6C90               ; {ram.6C90}
83AD: 60              RTS                         ; 
83AE: 27                              ;
83AF: 61 20           ADC     ($20,X)             ; {ram.0020}
83B1: 58              CLI                         ; 
83B2: A9 01           LDA     #$01                ; 
83B4: 85 E3           STA     <$E3                ; {ram.00E3}
83B6: A0 03           LDY     #$03                ; 
83B8: B9 AE 83        LDA     $83AE,Y             ; {}
83BB: 99 00 02        STA     $0200,Y             ; {ram.0200}
83BE: 88              DEY                         ; 
83BF: 10 F7           BPL     $83B8               ; {}
83C1: 60              RTS                         ; 
83C2: A5 98           LDA     <$98                ; {ram.0098}
83C4: 4A              LSR     A                   ; 
83C5: 29 05           AND     #$05                ; 
83C7: 85 00           STA     <$00                ; {ram.GP_00}
83C9: A5 98           LDA     <$98                ; {ram.0098}
83CB: 0A              ASL     A                   ; 
83CC: 29 0A           AND     #$0A                ; 
83CE: 05 00           ORA     <$00                ; {ram.GP_00}
83D0: 85 EE           STA     <$EE                ; {ram.00EE}
83D2: 60              RTS                         ; 
83D3: 00              BRK                         ; 
83D4: 55 AA           EOR     $AA,X               ; 
83D6: FF                              ;
83D7: A8              TAY                         ; 
83D8: B9 7E 68        LDA     $687E,Y             ; 
83DB: 29 03           AND     #$03                ; 
83DD: AA              TAX                         ; 
83DE: BD D3 83        LDA     $83D3,X             ; {}
83E1: A2 2F           LDX     #$2F                ; 
83E3: 9D 30 05        STA     $0530,X             ; 
83E6: CA              DEX                         ; 
83E7: 10 FA           BPL     $83E3               ; {}
83E9: B9 FE 68        LDA     $68FE,Y             ; 
83EC: 29 03           AND     #$03                ; 
83EE: AA              TAX                         ; 
83EF: A0 09           LDY     #$09                ; 
83F1: 98              TYA                         ; 
83F2: 29 07           AND     #$07                ; 
83F4: F0 0E           BEQ     $8404               ; {}
83F6: C9 07           CMP     #$07                ; 
83F8: F0 0A           BEQ     $8404               ; {}
83FA: C0 21           CPY     #$21                ; 
83FC: B0 0C           BCS     $840A               ; {}
83FE: BD D3 83        LDA     $83D3,X             ; {}
8401: 99 30 05        STA     $0530,Y             ; 
8404: C8              INY                         ; 
8405: C0 27           CPY     #$27                ; 
8407: 90 E8           BCC     $83F1               ; {}
8409: 60              RTS                         ; 
840A: BD D3 83        LDA     $83D3,X             ; {}
840D: 29 0F           AND     #$0F                ; 
840F: 85 00           STA     <$00                ; {ram.GP_00}
8411: B9 30 05        LDA     $0530,Y             ; 
8414: 29 F0           AND     #$F0                ; 
8416: 05 00           ORA     <$00                ; {ram.GP_00}
8418: 99 30 05        STA     $0530,Y             ; 
841B: 4C 04 84        JMP     $8404               ; {}
841E: 20 24 84        JSR     $8424               ; {}
8421: 4C 38 F2        JMP     $F238               ; 
8424: A5 13           LDA     <$13                ; {ram.0013}
8426: 20 E2 E5        JSR     $E5E2               ; 
8429: 39 84 7E        AND     $7E84,Y             ; 
842C: 84 92           STY     <$92                ; {ram.0092}
842E: 84 A4           STY     <$A4                ; {ram.00A4}
8430: 84 DF           STY     <$DF                ; {ram.00DF}
8432: 84 E8           STY     <$E8                ; {ram.00E8}
8434: 84 BA           STY     <$BA                ; {ram.00BA}
8436: 84 CC           STY     <$CC                ; {ram.00CC}
8438: 84 A9           STY     <$A9                ; {ram.00A9}
843A: 00              BRK                         ; 
843B: 85 E2           STA     <$E2                ; {ram.00E2}
843D: 85 FD           STA     <$FD                ; {ram.CUR_HScroll}
843F: A9 08           LDA     #$08                ; 
8441: 24 98           BIT     <$98                ; {ram.0098}
8443: D0 2C           BNE     $8471               ; {}
8445: 4A              LSR     A                   ; 
8446: 24 98           BIT     <$98                ; {ram.0098}
8448: F0 0D           BEQ     $8457               ; {}
844A: A9 21           LDA     #$21                ; 
844C: 85 58           STA     <$58                ; {ram.0058}
844E: A9 FF           LDA     #$FF                ; 
8450: 85 E9           STA     <$E9                ; {ram.00E9}
8452: E6 13           INC     <$13                ; {ram.0013}
8454: E6 13           INC     <$13                ; {ram.0013}
8456: 60              RTS                         ; 
8457: A0 A0           LDY     #$A0                ; 
8459: A6 10           LDX     <$10                ; {ram.0010}
845B: D0 02           BNE     $845F               ; {}
845D: A0 E0           LDY     #$E0                ; 
845F: 4A              LSR     A                   ; 
8460: 24 98           BIT     <$98                ; {ram.0098}
8462: F0 08           BEQ     $846C               ; {}
8464: A0 81           LDY     #$81                ; 
8466: A6 10           LDX     <$10                ; {ram.0010}
8468: D0 02           BNE     $846C               ; {}
846A: A0 41           LDY     #$41                ; 
846C: 84 E8           STY     <$E8                ; {ram.00E8}
846E: 4C 52 84        JMP     $8452               ; {}
8471: A9 28           LDA     #$28                ; 
8473: 85 58           STA     <$58                ; {ram.0058}
8475: A9 16           LDA     #$16                ; 
8477: 85 E9           STA     <$E9                ; {ram.00E9}
8479: A5 EB           LDA     <$EB                ; {ram.00EB}
847B: 20 D7 83        JSR     $83D7               ; {}
847E: 20 84 84        JSR     $8484               ; {}
8481: 4C 01 85        JMP     $8501               ; {}
8484: A9 D0           LDA     #$D0                ; 
8486: A0 17           LDY     #$17                ; 
8488: A6 13           LDX     <$13                ; {ram.0013}
848A: F0 05           BEQ     $8491               ; {}
848C: A0 2F           LDY     #$2F                ; 
848E: 18              CLC                         ; 
848F: 69 18           ADC     #$18                ; 
8491: 60              RTS                         ; 
8492: E6 13           INC     <$13                ; {ram.0013}
8494: A5 15           LDA     <$15                ; {ram.0015}
8496: 18              CLC                         ; 
8497: 69 01           ADC     #$01                ; 
8499: 29 03           AND     #$03                ; 
849B: A4 10           LDY     <$10                ; {ram.0010}
849D: D0 02           BNE     $84A1               ; {}
849F: 29 01           AND     #$01                ; 
84A1: 85 E6           STA     <$E6                ; {ram.00E6}
84A3: 60              RTS                         ; 
84A4: 20 DD 81        JSR     $81DD               ; {}
84A7: 20 06 85        JSR     $8506               ; {}
84AA: A5 13           LDA     <$13                ; {ram.0013}
84AC: C9 03           CMP     #$03                ; 
84AE: F0 09           BEQ     $84B9               ; {}
84B0: A0 FF           LDY     #$FF                ; 
84B2: 84 E9           STY     <$E9                ; {ram.00E9}
84B4: 84 ED           STY     <$ED                ; {ram.00ED}
84B6: C8              INY                         ; 
84B7: 84 E8           STY     <$E8                ; {ram.00E8}
84B9: 60              RTS                         ; 
84BA: A5 10           LDA     <$10                ; {ram.0010}
84BC: F0 0E           BEQ     $84CC               ; {}
84BE: A4 EB           LDY     <$EB                ; {ram.00EB}
84C0: 20 8D B6        JSR     $B68D               ; {}
84C3: F0 07           BEQ     $84CC               ; {}
84C5: A9 00           LDA     #$00                ; 
84C7: 85 E9           STA     <$E9                ; {ram.00E9}
84C9: E6 13           INC     <$13                ; {ram.0013}
84CB: 60              RTS                         ; 
84CC: A9 01           LDA     #$01                ; 
84CE: 85 13           STA     <$13                ; {ram.0013}
84D0: 4A              LSR     A                   ; 
84D1: 85 11           STA     <$11                ; {ram.0011}
84D3: 8D 0C 01        STA     $010C               ; {ram.010C}
84D6: 85 E7           STA     <$E7                ; {ram.00E7}
84D8: 85 E3           STA     <$E3                ; {ram.00E3}
84DA: A9 04           LDA     #$04                ; 
84DC: 85 12           STA     <$12                ; {ram.0012}
84DE: 60              RTS                         ; 
84DF: A9 08           LDA     #$08                ; 
84E1: 24 98           BIT     <$98                ; {ram.0098}
84E3: F0 03           BEQ     $84E8               ; {}
84E5: 4C 52 84        JMP     $8452               ; {}
84E8: A9 D0           LDA     #$D0                ; 
84EA: A0 17           LDY     #$17                ; 
84EC: A6 13           LDX     <$13                ; {ram.0013}
84EE: E0 04           CPX     #$04                ; 
84F0: F0 0F           BEQ     $8501               ; {}
84F2: 48              PHA                         ; 
84F3: A5 98           LDA     <$98                ; {ram.0098}
84F5: C9 04           CMP     #$04                ; 
84F7: B0 04           BCS     $84FD               ; {}
84F9: A9 00           LDA     #$00                ; 
84FB: 85 5F           STA     <$5F                ; {ram.005F}
84FD: 68              PLA                         ; 
84FE: 20 8C 84        JSR     $848C               ; {}
8501: A2 23           LDX     #$23                ; 
8503: 4C A6 8C        JMP     $8CA6               ; {}
8506: A5 E9           LDA     <$E9                ; {ram.00E9}
8508: C9 16           CMP     #$16                ; 
850A: B0 09           BCS     $8515               ; {}
850C: C5 ED           CMP     <$ED                ; {ram.00ED}
850E: F0 10           BEQ     $8520               ; {}
8510: 85 ED           STA     <$ED                ; {ram.00ED}
8512: 4C 24 A9        JMP     $A924               ; {}
8515: A5 E8           LDA     <$E8                ; {ram.00E8}
8517: F0 07           BEQ     $8520               ; {}
8519: C9 21           CMP     #$21                ; 
851B: B0 03           BCS     $8520               ; {}
851D: 4C DE A8        JMP     $A8DE               ; {}
8520: 60              RTS                         ; 
8521: AD 02 20        LDA     $2002               ; {hard.P_STATUS} [NES] PPU status
8524: 29 40           AND     #$40                ; 
8526: F0 F9           BEQ     $8521               ; {}
8528: AD 02 20        LDA     $2002               ; {hard.P_STATUS} [NES] PPU status
852B: A0 03           LDY     #$03                ; 
852D: A2 30           LDX     #$30                ; 
852F: CA              DEX                         ; 
8530: 10 FD           BPL     $852F               ; {}
8532: 88              DEY                         ; 
8533: 10 F8           BPL     $852D               ; {}
8535: EA              NOP                         ; 
8536: EA              NOP                         ; 
8537: EA              NOP                         ; 
8538: EA              NOP                         ; 
8539: EA              NOP                         ; 
853A: EA              NOP                         ; 
853B: EA              NOP                         ; 
853C: EA              NOP                         ; 
853D: EA              NOP                         ; 
853E: A5 12           LDA     <$12                ; {ram.0012}
8540: C9 08           CMP     #$08                ; 
8542: B0 48           BCS     $858C               ; {}
8544: A5 13           LDA     <$13                ; {ram.0013}
8546: F0 43           BEQ     $858B               ; {}
8548: A5 98           LDA     <$98                ; {ram.0098}
854A: C9 04           CMP     #$04                ; 
854C: 90 1F           BCC     $856D               ; {}
854E: A0 5E           LDY     #$5E                ; 
8550: EA              NOP                         ; 
8551: 88              DEY                         ; 
8552: 10 FC           BPL     $8550               ; {}
8554: EA              NOP                         ; 
8555: EA              NOP                         ; 
8556: EA              NOP                         ; 
8557: EA              NOP                         ; 
8558: EA              NOP                         ; 
8559: AD 02 20        LDA     $2002               ; {hard.P_STATUS} [NES] PPU status
855C: A5 58           LDA     <$58                ; {ram.0058}
855E: A4 E2           LDY     <$E2                ; {ram.00E2}
8560: 8D 06 20        STA     $2006               ; {hard.P_VRAM_ADDR} [NES] VRAM address select
8563: 8C 06 20        STY     $2006               ; {hard.P_VRAM_ADDR} [NES] VRAM address select
8566: AD 07 20        LDA     $2007               ; {hard.P_VRAM_DATA} [NES] VRAM data
8569: AD 07 20        LDA     $2007               ; {hard.P_VRAM_DATA} [NES] VRAM data
856C: 60              RTS                         ; 
856D: A0 5E           LDY     #$5E                ; 
856F: EA              NOP                         ; 
8570: 88              DEY                         ; 
8571: 10 FC           BPL     $856F               ; {}
8573: EA              NOP                         ; 
8574: EA              NOP                         ; 
8575: EA              NOP                         ; 
8576: A5 FF           LDA     <$FF                ; {ram.CUR_2000}
8578: 29 FE           AND     #$FE                ; 
857A: 05 5F           ORA     <$5F                ; {ram.005F}
857C: 85 FF           STA     <$FF                ; {ram.CUR_2000}
857E: 8D 00 20        STA     $2000               ; {hard.P_CNTRL_1} [NES] PPU setup #1
8581: A5 FD           LDA     <$FD                ; {ram.CUR_HScroll}
8583: 8D 05 20        STA     $2005               ; {hard.P_BKG_SCROLL} [NES] PPU scroll
8586: A9 00           LDA     #$00                ; 
8588: 8D 05 20        STA     $2005               ; {hard.P_BKG_SCROLL} [NES] PPU scroll
858B: 60              RTS                         ; 
858C: C9 11           CMP     #$11                ; 
858E: B0 03           BCS     $8593               ; {}
8590: 4C 25 E6        JMP     $E625               ; 
8593: A5 FF           LDA     <$FF                ; {ram.CUR_2000}
8595: 09 01           ORA     #$01                ; 
8597: 85 FF           STA     <$FF                ; {ram.CUR_2000}
8599: 8D 00 20        STA     $2000               ; {hard.P_CNTRL_1} [NES] PPU setup #1
859C: 60              RTS                         ; 
859D: FF                              ;
859E: FF                              ;
859F: FF                              ;
85A0: FF                              ;
85A1: FF                              ;
85A2: FF                              ;
85A3: FF                              ;
85A4: FF                              ;
85A5: FF                              ;
85A6: FF                              ;
85A7: FF                              ;
85A8: FF                              ;
85A9: FF                              ;
85AA: FF                              ;
85AB: FF                              ;
85AC: FF                              ;
85AD: FF                              ;
85AE: FF                              ;
85AF: FF                              ;
85B0: FF                              ;
85B1: FF                              ;
85B2: FF                              ;
85B3: FF                              ;
85B4: FF                              ;
85B5: FF                              ;
85B6: FF                              ;
85B7: FF                              ;
85B8: FF                              ;
85B9: FF                              ;
85BA: FF                              ;
85BB: FF                              ;
85BC: FF                              ;
85BD: FF                              ;
85BE: FF                              ;
85BF: FF                              ;
85C0: FF                              ;
85C1: FF                              ;
85C2: FF                              ;
85C3: FF                              ;
85C4: FF                              ;
85C5: FF                              ;
85C6: FF                              ;
85C7: FF                              ;
85C8: FF                              ;
85C9: FF                              ;
85CA: FF                              ;
85CB: FF                              ;
85CC: FF                              ;
85CD: FF                              ;
85CE: FF                              ;
85CF: FF                              ;
85D0: FF                              ;
85D1: FF                              ;
85D2: FF                              ;
85D3: FF                              ;
85D4: FF                              ;
85D5: FF                              ;
85D6: FF                              ;
85D7: FF                              ;
85D8: FF                              ;
85D9: FF                              ;
85DA: FF                              ;
85DB: FF                              ;
85DC: FF                              ;
85DD: FF                              ;
85DE: FF                              ;
85DF: FF                              ;
85E0: FF                              ;
85E1: FF                              ;
85E2: FF                              ;
85E3: FF                              ;
85E4: FF                              ;
85E5: FF                              ;
85E6: FF                              ;
85E7: FF                              ;
85E8: FF                              ;
85E9: FF                              ;
85EA: FF                              ;
85EB: FF                              ;
85EC: FF                              ;
85ED: FF                              ;
85EE: FF                              ;
85EF: FF                              ;
85F0: FF                              ;
85F1: FF                              ;
85F2: FF                              ;
85F3: FF                              ;
85F4: FF                              ;
85F5: FF                              ;
85F6: FF                              ;
85F7: FF                              ;
85F8: FF                              ;
85F9: FF                              ;
85FA: FF                              ;
85FB: FF                              ;
85FC: FF                              ;
85FD: FF                              ;
85FE: FF                              ;
85FF: FF                              ;
8600: 20 25 E6        JSR     $E625               ; 
8603: A5 13           LDA     <$13                ; {ram.0013}
8605: D0 0C           BNE     $8613               ; {}
8607: 8D 5A 00        STA     $005A               ; {ram.005A}
860A: 20 6D E4        JSR     $E46D               ; 
860D: 20 2B EA        JSR     $EA2B               ; 
8610: 4C 00 EA        JMP     $EA00               ; 
8613: A9 04           LDA     #$04                ; 
8615: 85 14           STA     <$14                ; {ram.0014}
8617: 4C 90 6C        JMP     $6C90               ; {ram.6C90}
861A: 20 6D E4        JSR     $E46D               ; 
861D: 20 AC B4        JSR     $B4AC               ; {code.FormatBBR}
8620: B0 03           BCS     $8625               ; {}
8622: 4C 90 6C        JMP     $6C90               ; {ram.6C90}
8625: 4C 50 FF        JMP     $FF50               ; 
8628: A2 00           LDX     #$00                ; 
862A: 20 F4 ED        JSR     $EDF4               ; 
862D: C9 24           CMP     #$24                ; 
862F: D0 12           BNE     $8643               ; {}
8631: A9 00           LDA     #$00                ; 
8633: 8D 19 06        STA     $0619               ; {ram.0619}
8636: A9 08           LDA     #$08                ; 
8638: 8D 03 06        STA     $0603               ; {ram.??SND_603??}
863B: A5 84           LDA     <$84                ; {ram.0084}
863D: 18              CLC                         ; 
863E: 69 10           ADC     #$10                ; 
8640: 8D 12 04        STA     $0412               ; {ram.0412}
8643: E6 11           INC     <$11                ; {ram.0011}
8645: 60              RTS                         ; 
8646: 4E 57 60        LSR     $6057               ; {ram.6057}
8649: 69 86           ADC     #$86                ; 
864B: 86 86           STX     <$86                ; {ram.0086}
864D: 86 55           STX     <$55                ; {ram.0055}
864F: B5 78           LDA     $78,X               ; 
8651: 98              TYA                         ; 
8652: 7A                              ;
8653: 9A              TXS                         ; 
8654: 6C AC 8D        JMP     ($8DAC)             ; {}
8657: 82                              ;
8658: 63                              ;
8659: A3                              ;
865A: 75 95           ADC     <$95,X              ; {ram.0095}
865C: 77                              ;
865D: 97                              ;
865E: 5A                              ;
865F: BA              TSX                         ; 
8660: A3                              ;
8661: 75 B5           ADC     <$B5,X              ; {ram.00B5}
8663: 96 87           STX     $87,Y               ; {ram.0087}
8665: 99 7A BA        STA     $BA7A,Y             ; {}
8668: AC 63 55        LDY     $5563               ; 
866B: 95 76           STA     $76,X               ; {ram.0076}
866D: 88              DEY                         ; 
866E: 79 5A 9A        ADC     $9A5A,Y             ; {}
8671: 6C 18 E8        JMP     ($E818)             ; 
8674: 28              PLP                         ; 
8675: D8              CLD                         ; 
8676: 03                              ;
8677: 03                              ;
8678: 04                              ;
8679: 03                              ;
867A: 04                              ;
867B: 03                              ;
867C: 04                              ;
867D: 03                              ;
867E: 04                              ;
867F: 1A                              ;
8680: 1A                              ;
8681: 02                              ;
8682: 01 02           ORA     ($02,X)             ; {ram.GP_02}
8684: 01 01           ORA     ($01,X)             ; {ram.GP_01}
8686: 02                              ;
8687: 01 02           ORA     ($02,X)             ; {ram.GP_02}
8689: 01 0F           ORA     ($0F,X)             ; {ram.000F}
868B: 02                              ;
868C: 01 10           ORA     ($10,X)             ; {ram.0010}
868E: 02                              ;
868F: 0F                              ;
8690: 1A                              ;
8691: 10 1A           BPL     $86AD               ; {}
8693: 0F                              ;
8694: 1A                              ;
8695: 09 08           ORA     #$08                ; 
8697: 08              PHP                         ; 
8698: 08              PHP                         ; 
8699: 08              PHP                         ; 
869A: 08              PHP                         ; 
869B: 07                              ;
869C: 08              PHP                         ; 
869D: 07                              ;
869E: 08              PHP                         ; 
869F: 09 08           ORA     #$08                ; 
86A1: 09 08           ORA     #$08                ; 
86A3: 0A              ASL     A                   ; 
86A4: 07                              ;
86A5: 0A              ASL     A                   ; 
86A6: 07                              ;
86A7: 07                              ;
86A8: 03                              ;
86A9: 0A              ASL     A                   ; 
86AA: 04                              ;
86AB: 0A              ASL     A                   ; 
86AC: 04                              ;
86AD: 04                              ;
86AE: 4A              LSR     A                   ; 
86AF: 00              BRK                         ; 
86B0: 00              BRK                         ; 
86B1: 00              BRK                         ; 
86B2: 13                              ;
86B3: 13                              ;
86B4: 00              BRK                         ; 
86B5: 13                              ;
86B6: 4A              LSR     A                   ; 
86B7: 00              BRK                         ; 
86B8: 00              BRK                         ; 
86B9: 00              BRK                         ; 
86BA: 1B                              ;
86BB: 1B                              ;
86BC: 1B                              ;
86BD: 1B                              ;
86BE: 2B                              ;
86BF: 2B                              ;
86C0: 2B                              ;
86C1: 13                              ;
86C2: 13                              ;
86C3: 1B                              ;
86C4: 1B                              ;
86C5: 1B                              ;
86C6: 16 30           ASL     $30,X               ; {ram.0030}
86C8: 30 1B           BMI     $86E5               ; {}
86CA: 1B                              ;
86CB: 16 00           ASL     $00,X               ; {ram.GP_00}
86CD: 00              BRK                         ; 
86CE: 2B                              ;
86CF: 2B                              ;
86D0: 2B                              ;
86D1: 23                              ;
86D2: 23                              ;
86D3: 24 23           BIT     <$23                ; {ram.0023}
86D5: 24 2B           BIT     <$2B                ; {ram.002B}
86D7: 2B                              ;
86D8: 12                              ;
86D9: 12                              ;
86DA: 12                              ;
86DB: 00              BRK                         ; 
86DC: 00              BRK                         ; 
86DD: 00              BRK                         ; 
86DE: 2B                              ;
86DF: 2B                              ;
86E0: 13                              ;
86E1: 13                              ;
86E2: 17                              ;
86E3: 17                              ;
86E4: 2B                              ;
86E5: 2B                              ;
86E6: 0C                              ;
86E7: 0B                              ;
86E8: 0B                              ;
86E9: 30 30           BMI     $871B               ; {}
86EB: 30 2B           BMI     $8718               ; {}
86ED: 2B                              ;
86EE: 05 05           ORA     <$05                ; {ram.0005}
86F0: 05 1B           ORA     <$1B                ; {ram.001B}
86F2: 1B                              ;
86F3: 1B                              ;
86F4: 4A              LSR     A                   ; 
86F5: 00              BRK                         ; 
86F6: 00              BRK                         ; 
86F7: 00              BRK                         ; 
86F8: 17                              ;
86F9: 17                              ;
86FA: 17                              ;
86FB: 17                              ;
86FC: 4A              LSR     A                   ; 
86FD: 00              BRK                         ; 
86FE: 00              BRK                         ; 
86FF: 00              BRK                         ; 
8700: 23                              ;
8701: 24 23           BIT     <$23                ; {ram.0023}
8703: 24 16           BIT     <$16                ; {ram.0016}
8705: 0C                              ;
8706: 0B                              ;
8707: 0C                              ;
8708: 0B                              ;
8709: 16 2B           ASL     $2B,X               ; {ram.002B}
870B: 2B                              ;
870C: 2B                              ;
870D: 27                              ;
870E: 27                              ;
870F: 27                              ;
8710: 27                              ;
8711: 27                              ;
8712: 05 06           ORA     <$06                ; {ram.0006}
8714: 06 05           ASL     <$05                ; {ram.0005}
8716: 06 05           ASL     <$05                ; {ram.0005}
8718: 00              BRK                         ; 
8719: 00              BRK                         ; 
871A: 23                              ;
871B: 23                              ;
871C: 24 23           BIT     <$23                ; {ram.0023}
871E: 24 2B           BIT     <$2B                ; {ram.002B}
8720: 17                              ;
8721: 23                              ;
8722: 23                              ;
8723: 17                              ;
8724: 24 17           BIT     <$17                ; {ram.0017}
8726: 24 2D           BIT     <$2D                ; {ram.002D}
8728: 2D 2D 2C        AND     $2C2D               ; 
872B: 23                              ;
872C: 24 23           BIT     <$23                ; {ram.0023}
872E: 24 2D           BIT     <$2D                ; {ram.002D}
8730: 2D 2D 2C        AND     $2C2D               ; 
8733: 0C                              ;
8734: 0B                              ;
8735: 0C                              ;
8736: 0B                              ;
8737: 2D 2D 2D        AND     $2D2D               ; 
873A: 2C 27 27        BIT     $2727               ; 
873D: 27                              ;
873E: 27                              ;
873F: 76 86           ROR     <$86,X              ; {ram.0086}
8741: 7B                              ;
8742: 86 7F           STX     <$7F                ; {ram.007F}
8744: 86 85           STX     <$85                ; {ram.0085}
8746: 86 89           STX     <$89                ; {ram.0089}
8748: 86 8F           STX     <$8F                ; {ram.008F}
874A: 86 95           STX     <$95                ; {ram.0095}
874C: 86 9A           STX     <$9A                ; {ram.009A}
874E: 86 9E           STX     <$9E                ; {ram.009E}
8750: 86 A3           STX     <$A3                ; {ram.00A3}
8752: 86 A8           STX     <$A8                ; {ram.00A8}
8754: 86 AE           STX     <$AE                ; {ram.00AE}
8756: 86 B6           STX     <$B6                ; {ram.00B6}
8758: 86 BE           STX     <$BE                ; {ram.00BE}
875A: 86 C6           STX     <$C6                ; {ram.00C6}
875C: 86 CE           STX     <$CE                ; {ram.00CE}
875E: 86 D6           STX     <$D6                ; {ram.00D6}
8760: 86 DE           STX     <$DE                ; {ram.00DE}
8762: 86 E4           STX     <$E4                ; {ram.00E4}
8764: 86 EC           STX     <$EC                ; {ram.00EC}
8766: 86 F4           STX     <$F4                ; {ram.??!BatRamInit??}
8768: 86 FC           STX     <$FC                ; {ram.CUR_VScroll}
876A: 86 04           STX     <$04                ; {ram.0004}
876C: 87                              ;
876D: 0A              ASL     A                   ; 
876E: 87                              ;
876F: 12                              ;
8770: 87                              ;
8771: 1A                              ;
8772: 87                              ;
8773: 1F                              ;
8774: 87                              ;
8775: 27                              ;
8776: 87                              ;
8777: 2F                              ;
8778: 87                              ;
8779: 37                              ;
877A: 87                              ;
877B: A6 13           LDX     <$13                ; {ram.0013}
877D: F0 47           BEQ     $87C6               ; {}
877F: CA              DEX                         ; 
8780: D0 0C           BNE     $878E               ; {}
8782: A5 E9           LDA     <$E9                ; {ram.00E9}
8784: 30 05           BMI     $878B               ; {}
8786: 20 16 AC        JSR     $AC16               ; {}
8789: 90 02           BCC     $878D               ; {}
878B: E6 13           INC     <$13                ; {ram.0013}
878D: 60              RTS                         ; 
878E: CA              DEX                         ; 
878F: D0 28           BNE     $87B9               ; {}
8791: A4 EB           LDY     <$EB                ; {ram.00EB}
8793: 20 8D B6        JSR     $B68D               ; {}
8796: D0 26           BNE     $87BE               ; {}
8798: A5 98           LDA     <$98                ; {ram.0098}
879A: 20 60 B5        JSR     $B560               ; {}
879D: 38              SEC                         ; 
879E: E5 EB           SBC     <$EB                ; {ram.00EB}
87A0: 20 21 70        JSR     $7021               ; {ram.7021}
87A3: 18              CLC                         ; 
87A4: 65 EB           ADC     <$EB                ; {ram.00EB}
87A6: A8              TAY                         ; 
87A7: 20 8D B6        JSR     $B68D               ; {}
87AA: F0 12           BEQ     $87BE               ; {}
87AC: AD 1F 05        LDA     $051F               ; {ram.051F}
87AF: D0 0D           BNE     $87BE               ; {}
87B1: A9 C0           LDA     #$C0                ; 
87B3: 8D 1C 05        STA     $051C               ; {ram.051C}
87B6: E6 13           INC     <$13                ; {ram.0013}
87B8: 60              RTS                         ; 
87B9: 20 B7 74        JSR     $74B7               ; {ram.74B7}
87BC: D0 FA           BNE     $87B8               ; {}
87BE: A9 00           LDA     #$00                ; 
87C0: 85 13           STA     <$13                ; {ram.0013}
87C2: 8D 1F 05        STA     $051F               ; {ram.051F}
87C5: 60              RTS                         ; 
87C6: 20 3D EA        JSR     $EA3D               ; 
87C9: 20 51 EA        JSR     $EA51               ; 
87CC: A9 05           LDA     #$05                ; 
87CE: A0 1F           LDY     #$1F                ; 
87D0: 20 08 E6        JSR     $E608               ; 
87D3: A9 00           LDA     #$00                ; 
87D5: 85 54           STA     <$54                ; {ram.0054}
87D7: 85 55           STA     <$55                ; {ram.0055}
87D9: A4 EB           LDY     <$EB                ; {ram.00EB}
87DB: B9 FE 6A        LDA     $6AFE,Y             ; 
87DE: 8D CD 04        STA     $04CD               ; {ram.04CD}
87E1: 20 B6 B0        JSR     $B0B6               ; {}
87E4: A5 5A           LDA     <$5A                ; {ram.005A}
87E6: F0 38           BEQ     $8820               ; {}
87E8: A5 10           LDA     <$10                ; {ram.0010}
87EA: D0 29           BNE     $8815               ; {}
87EC: A4 EB           LDY     <$EB                ; {ram.00EB}
87EE: B9 7E 68        LDA     $687E,Y             ; 
87F1: 29 F0           AND     #$F0                ; 
87F3: 85 70           STA     <$70                ; {ram.0070}
87F5: B9 FE 6A        LDA     $6AFE,Y             ; 
87F8: 29 07           AND     #$07                ; 
87FA: 0A              ASL     A                   ; 
87FB: 0A              ASL     A                   ; 
87FC: 0A              ASL     A                   ; 
87FD: 0A              ASL     A                   ; 
87FE: 69 4D           ADC     #$4D                ; 
8800: 85 84           STA     <$84                ; {ram.0084}
8802: A4 65           LDY     <$65                ; {ram.0065}
8804: C0 24           CPY     #$24                ; 
8806: D0 0D           BNE     $8815               ; {}
8808: 8D 12 04        STA     $0412               ; {ram.0412}
880B: 18              CLC                         ; 
880C: 69 10           ADC     #$10                ; 
880E: 85 84           STA     <$84                ; {ram.0084}
8810: A9 08           LDA     #$08                ; 
8812: 8D 03 06        STA     $0603               ; {ram.??SND_603??}
8815: A9 04           LDA     #$04                ; 
8817: 85 98           STA     <$98                ; {ram.0098}
8819: A9 00           LDA     #$00                ; 
881B: 85 53           STA     <$53                ; {ram.0053}
881D: 4C 59 88        JMP     $8859               ; {}
8820: A5 98           LDA     <$98                ; {ram.0098}
8822: 85 53           STA     <$53                ; {ram.0053}
8824: 20 13 70        JSR     $7013               ; {ram.7013}
8827: 25 EE           AND     <$EE                ; {ram.00EE}
8829: 85 55           STA     <$55                ; {ram.0055}
882B: F0 04           BEQ     $8831               ; {}
882D: A9 02           LDA     #$02                ; 
882F: 85 54           STA     <$54                ; {ram.0054}
8831: A5 10           LDA     <$10                ; {ram.0010}
8833: F0 24           BEQ     $8859               ; {}
8835: A0 00           LDY     #$00                ; 
8837: A5 98           LDA     <$98                ; {ram.0098}
8839: 29 03           AND     #$03                ; 
883B: F0 08           BEQ     $8845               ; {}
883D: 29 01           AND     #$01                ; 
883F: D0 02           BNE     $8843               ; {}
8841: A0 F0           LDY     #$F0                ; 
8843: 84 70           STY     <$70                ; {ram.0070}
8845: 20 C3 B0        JSR     $B0C3               ; {}
8848: 29 07           AND     #$07                ; 
884A: F0 0A           BEQ     $8856               ; {}
884C: C9 05           CMP     #$05                ; 
884E: F0 06           BEQ     $8856               ; {}
8850: C9 06           CMP     #$06                ; 
8852: F0 02           BEQ     $8856               ; {}
8854: C8              INY                         ; 
8855: C8              INY                         ; 
8856: B9 72 86        LDA     $8672,Y             ; {}
8859: 8D 94 03        STA     $0394               ; {ram.0394}
885C: 20 5E B0        JSR     $B05E               ; {}
885F: A2 0B           LDX     #$0B                ; 
8861: 8E 40 03        STX     $0340               ; {ram.0340}
8864: DE 92 04        DEC     $0492,X             ; 
8867: 20 E4 EE        JSR     $EEE4               ; 
886A: 95 AC           STA     $AC,X               ; {ram.00AC}
886C: 95 98           STA     $98,X               ; {ram.0098}
886E: 95 3D           STA     $3D,X               ; {ram.003D}
8870: FE D0 03        INC     $03D0,X             ; {ram.03D0}
8873: FE 05 04        INC     $0405,X             ; {ram.0405}
8876: A9 20           LDA     #$20                ; 
8878: 9D BC 03        STA     $03BC,X             ; {ram.03BC}
887B: CA              DEX                         ; 
887C: D0 E6           BNE     $8864               ; {}
887E: A4 EB           LDY     <$EB                ; {ram.00EB}
8880: B9 7E 69        LDA     $697E,Y             ; 
8883: 48              PHA                         ; 
8884: 29 3F           AND     #$3F                ; 
8886: 85 02           STA     <$02                ; {ram.GP_02}
8888: B9 FE 69        LDA     $69FE,Y             ; 
888B: 0A              ASL     A                   ; 
888C: 90 07           BCC     $8895               ; {}
888E: A5 02           LDA     <$02                ; {ram.GP_02}
8890: 18              CLC                         ; 
8891: 69 40           ADC     #$40                ; 
8893: 85 02           STA     <$02                ; {ram.GP_02}
8895: 68              PLA                         ; 
8896: 29 C0           AND     #$C0                ; 
8898: 18              CLC                         ; 
8899: 2A              ROL     A                   ; 
889A: 2A              ROL     A                   ; 
889B: 2A              ROL     A                   ; 
889C: A8              TAY                         ; 
889D: B9 A2 6B        LDA     $6BA2,Y             ; 
88A0: A4 02           LDY     <$02                ; {ram.GP_02}
88A2: C0 62           CPY     #$62                ; 
88A4: B0 06           BCS     $88AC               ; {}
88A6: C0 32           CPY     #$32                ; 
88A8: 90 02           BCC     $88AC               ; {}
88AA: A9 01           LDA     #$01                ; 
88AC: 85 03           STA     <$03                ; {ram.GP_03}
88AE: A5 10           LDA     <$10                ; {ram.0010}
88B0: D0 06           BNE     $88B8               ; {}
88B2: 20 AE 90        JSR     $90AE               ; {}
88B5: 4C C7 88        JMP     $88C7               ; {}
88B8: 20 93 92        JSR     $9293               ; {}
88BB: A5 12           LDA     <$12                ; {ram.0012}
88BD: C9 09           CMP     #$09                ; 
88BF: D0 06           BNE     $88C7               ; {}
88C1: A9 00           LDA     #$00                ; 
88C3: 85 02           STA     <$02                ; {ram.GP_02}
88C5: 85 03           STA     <$03                ; {ram.GP_03}
88C7: A5 03           LDA     <$03                ; {ram.GP_03}
88C9: 8D 4E 03        STA     $034E               ; {ram.034E}
88CC: F0 3B           BEQ     $8909               ; {}
88CE: A5 02           LDA     <$02                ; {ram.GP_02}
88D0: F0 37           BEQ     $8909               ; {}
88D2: C9 62           CMP     #$62                ; 
88D4: B0 0F           BCS     $88E5               ; {}
88D6: A2 00           LDX     #$00                ; 
88D8: A5 02           LDA     <$02                ; {ram.GP_02}
88DA: 9D 50 03        STA     $0350,X             ; {ram.0350}
88DD: E8              INX                         ; 
88DE: C6 03           DEC     <$03                ; {ram.GP_03}
88E0: D0 F6           BNE     $88D8               ; {}
88E2: 4C 03 89        JMP     $8903               ; {}
88E5: A5 02           LDA     <$02                ; {ram.GP_02}
88E7: 38              SEC                         ; 
88E8: E9 62           SBC     #$62                ; 
88EA: 0A              ASL     A                   ; 
88EB: A8              TAY                         ; 
88EC: B9 3F 87        LDA     $873F,Y             ; {}
88EF: 85 04           STA     <$04                ; {ram.0004}
88F1: C8              INY                         ; 
88F2: B9 3F 87        LDA     $873F,Y             ; {}
88F5: 85 05           STA     <$05                ; {ram.0005}
88F7: A0 00           LDY     #$00                ; 
88F9: B1 04           LDA     ($04),Y             ; {ram.0004}
88FB: 99 50 03        STA     $0350,Y             ; {ram.0350}
88FE: C8              INY                         ; 
88FF: C4 03           CPY     <$03                ; {ram.GP_03}
8901: D0 F6           BNE     $88F9               ; {}
8903: AD 50 03        LDA     $0350               ; {ram.0350}
8906: 8D 5F 03        STA     $035F               ; {ram.035F}
8909: 20 6E 89        JSR     $896E               ; {}
890C: A5 10           LDA     <$10                ; {ram.0010}
890E: D0 03           BNE     $8913               ; {}
8910: 20 41 89        JSR     $8941               ; {}
8913: 20 DE 71        JSR     $71DE               ; {ram.71DE}
8916: A9 00           LDA     #$00                ; 
8918: 85 3D           STA     <$3D                ; {ram.003D}
891A: 85 C0           STA     <$C0                ; {ram.00C0}
891C: 85 D3           STA     <$D3                ; {ram.00D3}
891E: A9 04           LDA     #$04                ; 
8920: 8D D0 03        STA     $03D0               ; {ram.03D0}
8923: 20 66 B3        JSR     $B366               ; {}
8926: 20 D3 EA        JSR     $EAD3               ; 
8929: 20 40 6E        JSR     $6E40               ; {ram.6E40}
892C: A5 12           LDA     <$12                ; {ram.0012}
892E: C9 0B           CMP     #$0B                ; 
8930: F0 07           BEQ     $8939               ; {}
8932: C9 0C           CMP     #$0C                ; 
8934: F0 03           BEQ     $8939               ; {}
8936: 20 38 F2        JSR     $F238               ; 
8939: A5 5A           LDA     <$5A                ; {ram.005A}
893B: F0 03           BEQ     $8940               ; {}
893D: 20 AB 8B        JSR     $8BAB               ; {}
8940: 60              RTS                         ; 
8941: A5 EB           LDA     <$EB                ; {ram.00EB}
8943: C9 3F           CMP     #$3F                ; 
8945: F0 04           BEQ     $894B               ; {}
8947: C9 55           CMP     #$55                ; 
8949: D0 05           BNE     $8950               ; {}
894B: A9 61           LDA     #$61                ; 
894D: 4C 5D 89        JMP     $895D               ; {}
8950: AD 2C 05        LDA     $052C               ; {ram.052C}
8953: 85 7B           STA     <$7B                ; {ram.007B}
8955: AD 2D 05        LDA     $052D               ; {ram.052D}
8958: 85 8F           STA     <$8F                ; {ram.008F}
895A: AD 2B 05        LDA     $052B               ; {ram.052B}
895D: 8D 5A 03        STA     $035A               ; {ram.035A}
8960: 20 B7 6D        JSR     $6DB7               ; {ram.6DB7}
8963: 85 B7           STA     <$B7                ; {ram.00B7}
8965: 60              RTS                         ; 
8966: 20 60 90        JSR     $9060               ; {}
8969: D0 9D           BNE     $8908               ; {}
896B: 5D 7D 9D        EOR     $9D7D,X             ; {}
896E: AC 4E 03        LDY     $034E               ; {ram.034E}
8971: A5 02           LDA     <$02                ; {ram.GP_02}
8973: F0 4F           BEQ     $89C4               ; {}
8975: C9 37           CMP     #$37                ; 
8977: F0 4B           BEQ     $89C4               ; {}
8979: A5 10           LDA     <$10                ; {ram.0010}
897B: D0 07           BNE     $8984               ; {}
897D: AD CD 04        LDA     $04CD               ; {ram.04CD}
8980: 29 08           AND     #$08                ; 
8982: D0 40           BNE     $89C4               ; {}
8984: AD 4E 03        LDA     $034E               ; {ram.034E}
8987: F0 3B           BEQ     $89C4               ; {}
8989: A5 98           LDA     <$98                ; {ram.0098}
898B: A0 FF           LDY     #$FF                ; 
898D: C8              INY                         ; 
898E: 4A              LSR     A                   ; 
898F: 90 FC           BCC     $898D               ; {}
8991: B9 46 86        LDA     $8646,Y             ; {}
8994: 85 06           STA     <$06                ; {ram.0006}
8996: B9 4A 86        LDA     $864A,Y             ; {}
8999: 85 07           STA     <$07                ; {ram.0007}
899B: AC 24 05        LDY     $0524               ; {ram.0524}
899E: A2 01           LDX     #$01                ; 
89A0: B1 06           LDA     ($06),Y             ; {ram.0006}
89A2: 48              PHA                         ; 
89A3: 0A              ASL     A                   ; 
89A4: 0A              ASL     A                   ; 
89A5: 0A              ASL     A                   ; 
89A6: 0A              ASL     A                   ; 
89A7: 95 70           STA     $70,X               ; {ram.0070}
89A9: 68              PLA                         ; 
89AA: 29 F0           AND     #$F0                ; 
89AC: 09 0D           ORA     #$0D                ; 
89AE: 95 84           STA     $84,X               ; {ram.0084}
89B0: 20 04 8A        JSR     $8A04               ; {}
89B3: B0 01           BCS     $89B6               ; {}
89B5: E8              INX                         ; 
89B6: C8              INY                         ; 
89B7: C0 09           CPY     #$09                ; 
89B9: 90 02           BCC     $89BD               ; {}
89BB: A0 00           LDY     #$00                ; 
89BD: E0 0A           CPX     #$0A                ; 
89BF: 90 DF           BCC     $89A0               ; {}
89C1: 8C 24 05        STY     $0524               ; {ram.0524}
89C4: A5 12           LDA     <$12                ; {ram.0012}
89C6: C9 09           CMP     #$09                ; 
89C8: D0 15           BNE     $89DF               ; {}
89CA: A2 03           LDX     #$03                ; 
89CC: A9 1B           LDA     #$1B                ; 
89CE: 9D 50 03        STA     $0350,X             ; {ram.0350}
89D1: BD 66 89        LDA     $8966,X             ; {}
89D4: 95 71           STA     $71,X               ; {ram.0071}
89D6: B9 6A 89        LDA     $896A,Y             ; {}
89D9: 95 85           STA     $85,X               ; {ram.0085}
89DB: CA              DEX                         ; 
89DC: 10 EE           BPL     $89CC               ; {}
89DE: 60              RTS                         ; 
89DF: C9 0B           CMP     #$0B                ; 
89E1: F0 04           BEQ     $89E7               ; {}
89E3: C9 0C           CMP     #$0C                ; 
89E5: D0 1C           BNE     $8A03               ; {}
89E7: A2 07           LDX     #$07                ; 
89E9: A9 00           LDA     #$00                ; 
89EB: 9D 50 03        STA     $0350,X             ; {ram.0350}
89EE: CA              DEX                         ; 
89EF: 10 FA           BPL     $89EB               ; {}
89F1: A4 EB           LDY     <$EB                ; {ram.00EB}
89F3: B9 FE 68        LDA     $68FE,Y             ; 
89F6: 29 FC           AND     #$FC                ; 
89F8: 38              SEC                         ; 
89F9: E9 40           SBC     #$40                ; 
89FB: 4A              LSR     A                   ; 
89FC: 4A              LSR     A                   ; 
89FD: 18              CLC                         ; 
89FE: 69 6A           ADC     #$6A                ; 
8A00: 8D 50 03        STA     $0350               ; {ram.0350}
8A03: 60              RTS                         ; 
8A04: 98              TYA                         ; 
8A05: 48              PHA                         ; 
8A06: 20 F4 ED        JSR     $EDF4               ; 
8A09: 68              PLA                         ; 
8A0A: A8              TAY                         ; 
8A0B: BD 9E 04        LDA     $049E,X             ; {ram.049E}
8A0E: CD 4A 03        CMP     $034A               ; {ram.034A}
8A11: B0 1A           BCS     $8A2D               ; {}
8A13: A5 70           LDA     <$70                ; {ram.0070}
8A15: 38              SEC                         ; 
8A16: F5 70           SBC     $70,X               ; {ram.0070}
8A18: 20 1F 70        JSR     $701F               ; {ram.701F}
8A1B: C9 22           CMP     #$22                ; 
8A1D: B0 0C           BCS     $8A2B               ; {}
8A1F: A5 84           LDA     <$84                ; {ram.0084}
8A21: 38              SEC                         ; 
8A22: F5 84           SBC     $84,X               ; {ram.0084}
8A24: 20 1F 70        JSR     $701F               ; {ram.701F}
8A27: C9 22           CMP     #$22                ; 
8A29: 90 02           BCC     $8A2D               ; {}
8A2B: 18              CLC                         ; 
8A2C: 60              RTS                         ; 
8A2D: 38              SEC                         ; 
8A2E: 60              RTS                         ; 
8A2F: A2 00           LDX     #$00                ; 
8A31: 20 98 FE        JSR     $FE98               ; 
8A34: 20 3C F2        JSR     $F23C               ; 
8A37: A5 13           LDA     <$13                ; {ram.0013}
8A39: D0 25           BNE     $8A60               ; {}
8A3B: 20 F7 E5        JSR     $E5F7               ; 
8A3E: 20 79 E6        JSR     $E679               ; 
8A41: 20 29 89        JSR     $8929               ; {}
8A44: 20 8A E7        JSR     $E78A               ; 
8A47: 20 59 B5        JSR     $B559               ; {}
8A4A: A9 00           LDA     #$00                ; 
8A4C: 85 E0           STA     <$E0                ; {ram.??SND_E0??}
8A4E: 8D 70 06        STA     $0670               ; {ram.0670}
8A51: 20 00 6D        JSR     $6D00               ; {ram.6D00}
8A54: E6 13           INC     <$13                ; {ram.0013}
8A56: A9 10           LDA     #$10                ; 
8A58: 8D F0 04        STA     $04F0               ; {ram.04F0}
8A5B: A9 21           LDA     #$21                ; 
8A5D: 85 28           STA     <$28                ; {ram.0028}
8A5F: 60              RTS                         ; 
8A60: A5 28           LDA     <$28                ; {ram.0028}
8A62: D0 32           BNE     $8A96               ; {}
8A64: 20 5A E8        JSR     $E85A               ; 
8A67: 29 3E           AND     #$3E                ; 
8A69: C9 3E           CMP     #$3E                ; 
8A6B: F0 08           BEQ     $8A75               ; {}
8A6D: A5 EE           LDA     <$EE                ; {ram.00EE}
8A6F: 8D 21 05        STA     $0521               ; {ram.0521}
8A72: 20 FB 82        JSR     $82FB               ; {}
8A75: A9 60           LDA     #$60                ; 
8A77: 8D 1C 05        STA     $051C               ; {ram.051C}
8A7A: A9 02           LDA     #$02                ; 
8A7C: 85 32           STA     <$32                ; {ram.0032}
8A7E: A9 00           LDA     #$00                ; 
8A80: 85 13           STA     <$13                ; {ram.0013}
8A82: 85 E9           STA     <$E9                ; {ram.00E9}
8A84: 85 AC           STA     <$AC                ; {ram.00AC}
8A86: A9 04           LDA     #$04                ; 
8A88: 85 E5           STA     <$E5                ; {ram.00E5}
8A8A: 85 98           STA     <$98                ; {ram.0098}
8A8C: E6 11           INC     <$11                ; {ram.0011}
8A8E: A9 80           LDA     #$80                ; 
8A90: 8D 04 06        STA     $0604               ; {ram.SND_Request}
8A93: 8D 03 06        STA     $0603               ; {ram.??SND_603??}
8A96: 60              RTS                         ; 
8A97: 20 CE E6        JSR     $E6CE               ; 
8A9A: 1D BE E6        ORA     $E6BE,X             ; 
8A9D: 91 00           STA     ($00),Y             ; {ram.GP_00}
8A9F: 60              RTS                         ; 
8AA0: 20 CE E6        JSR     $E6CE               ; 
8AA3: BD BE E6        LDA     $E6BE,X             ; 
8AA6: 49 FF           EOR     #$FF                ; 
8AA8: 31 00           AND     ($00),Y             ; {ram.GP_00}
8AAA: 91 00           STA     ($00),Y             ; {ram.GP_00}
8AAC: 60              RTS                         ; 
8AAD: AD CE 04        LDA     $04CE               ; {ram.04CE}
8AB0: F0 10           BEQ     $8AC2               ; {}
8AB2: A9 08           LDA     #$08                ; 
8AB4: 85 0E           STA     <$0E                ; {ram.000E}
8AB6: A5 0E           LDA     <$0E                ; {ram.000E}
8AB8: 25 EE           AND     <$EE                ; {ram.00EE}
8ABA: F0 0C           BEQ     $8AC8               ; {}
8ABC: 46 0E           LSR     <$0E                ; {ram.000E}
8ABE: A5 0E           LDA     <$0E                ; {ram.000E}
8AC0: D0 F4           BNE     $8AB6               ; {}
8AC2: A9 00           LDA     #$00                ; 
8AC4: 8D CE 04        STA     $04CE               ; {ram.04CE}
8AC7: 60              RTS                         ; 
8AC8: A5 0E           LDA     <$0E                ; {ram.000E}
8ACA: 85 02           STA     <$02                ; {ram.GP_02}
8ACC: 20 F6 A3        JSR     $A3F6               ; {}
8ACF: C9 07           CMP     #$07                ; 
8AD1: D0 E9           BNE     $8ABC               ; {}
8AD3: AD 54 00        LDA     $0054               ; {ram.0054}
8AD6: D0 0A           BNE     $8AE2               ; {}
8AD8: A5 02           LDA     <$02                ; {ram.GP_02}
8ADA: 8D 55 00        STA     $0055               ; {ram.0055}
8ADD: A9 06           LDA     #$06                ; 
8ADF: 8D 54 00        STA     $0054               ; {ram.0054}
8AE2: 60              RTS                         ; 
8AE3: F3                              ;
8AE4: 02                              ;
8AE5: 40              RTI                         ; 
8AE6: 4F                              ;
8AE7: 67                              ;
8AE8: 7F                              ;
8AE9: 03                              ;
8AEA: 0D 00 23        ORA     $2300               ; 
8AED: D2                              ;
8AEE: 43                              ;
8AEF: 00              BRK                         ; 
8AF0: FF                              ;
8AF1: D2                              ;
8AF2: DA                              ;
8AF3: E2                              ;
8AF4: A5 13           LDA     <$13                ; {ram.0013}
8AF6: 0A              ASL     A                   ; 
8AF7: B0 3C           BCS     $8B35               ; {}
8AF9: A5 F8           LDA     <$F8                ; {ram.00F8}
8AFB: 29 10           AND     #$10                ; 
8AFD: D0 2B           BNE     $8B2A               ; {}
8AFF: A5 F8           LDA     <$F8                ; {ram.00F8}
8B01: 29 20           AND     #$20                ; 
8B03: F0 11           BEQ     $8B16               ; {}
8B05: A9 01           LDA     #$01                ; 
8B07: 8D 04 06        STA     $0604               ; {ram.SND_Request}
8B0A: E6 13           INC     <$13                ; {ram.0013}
8B0C: A5 13           LDA     <$13                ; {ram.0013}
8B0E: C9 03           CMP     #$03                ; 
8B10: D0 04           BNE     $8B16               ; {}
8B12: A9 00           LDA     #$00                ; 
8B14: 85 13           STA     <$13                ; {ram.0013}
8B16: A0 02           LDY     #$02                ; 
8B18: B9 E3 8A        LDA     $8AE3,Y             ; {}
8B1B: 99 01 02        STA     $0201,Y             ; {ram.0201}
8B1E: 88              DEY                         ; 
8B1F: 10 F7           BPL     $8B18               ; {}
8B21: A4 13           LDY     <$13                ; {ram.0013}
8B23: B9 E6 8A        LDA     $8AE6,Y             ; {}
8B26: 8D 00 02        STA     $0200               ; {ram.0200}
8B29: 60              RTS                         ; 
8B2A: A5 13           LDA     <$13                ; {ram.0013}
8B2C: 09 80           ORA     #$80                ; 
8B2E: 85 13           STA     <$13                ; {ram.0013}
8B30: A9 40           LDA     #$40                ; 
8B32: 85 29           STA     <$29                ; {ram.0029}
8B34: 60              RTS                         ; 
8B35: A5 29           LDA     <$29                ; {ram.0029}
8B37: F0 24           BEQ     $8B5D               ; {}
8B39: A0 04           LDY     #$04                ; 
8B3B: B9 EC 8A        LDA     $8AEC,Y             ; {}
8B3E: 99 02 03        STA     $0302,Y             ; {ram.0302}
8B41: 88              DEY                         ; 
8B42: 10 F7           BPL     $8B3B               ; {}
8B44: A5 13           LDA     <$13                ; {ram.0013}
8B46: 29 03           AND     #$03                ; 
8B48: A8              TAY                         ; 
8B49: B9 F1 8A        LDA     $8AF1,Y             ; {}
8B4C: 8D 03 03        STA     $0303               ; {ram.0303}
8B4F: A0 00           LDY     #$00                ; 
8B51: A5 29           LDA     <$29                ; {ram.0029}
8B53: 29 04           AND     #$04                ; 
8B55: F0 02           BEQ     $8B59               ; {}
8B57: A0 55           LDY     #$55                ; 
8B59: 8C 05 03        STY     $0305               ; {ram.!BckGndBuf}
8B5C: 60              RTS                         ; 
8B5D: A5 13           LDA     <$13                ; {ram.0013}
8B5F: 29 03           AND     #$03                ; 
8B61: 85 13           STA     <$13                ; {ram.0013}
8B63: 20 51 EA        JSR     $EA51               ; 
8B66: A4 13           LDY     <$13                ; {ram.0013}
8B68: B9 E9 8A        LDA     $8AE9,Y             ; {}
8B6B: 85 12           STA     <$12                ; {ram.0012}
8B6D: AD 6F 06        LDA     $066F               ; {ram.066F}
8B70: 29 F0           AND     #$F0                ; 
8B72: 09 02           ORA     #$02                ; 
8B74: 8D 6F 06        STA     $066F               ; {ram.066F}
8B77: A9 FF           LDA     #$FF                ; 
8B79: 8D 70 06        STA     $0670               ; {ram.0670}
8B7C: 20 A3 EB        JSR     $EBA3               ; 
8B7F: C0 02           CPY     #$02                ; 
8B81: D0 05           BNE     $8B88               ; {}
8B83: 88              DEY                         ; 
8B84: 84 13           STY     <$13                ; {ram.0013}
8B86: E6 11           INC     <$11                ; {ram.0011}
8B88: 4C E9 6E        JMP     $6EE9               ; {ram.6EE9}
8B8B: AD 9E 04        LDA     $049E               ; {ram.049E}
8B8E: C9 24           CMP     #$24                ; 
8B90: D0 0F           BNE     $8BA1               ; {}
8B92: A5 15           LDA     <$15                ; {ram.0015}
8B94: 29 03           AND     #$03                ; 
8B96: D0 10           BNE     $8BA8               ; {}
8B98: E6 84           INC     <$84                ; {ram.0084}
8B9A: A5 84           LDA     <$84                ; {ram.0084}
8B9C: CD 12 04        CMP     $0412               ; {ram.0412}
8B9F: D0 07           BNE     $8BA8               ; {}
8BA1: A5 5B           LDA     <$5B                ; {ram.005B}
8BA3: 85 12           STA     <$12                ; {ram.0012}
8BA5: 20 A3 EB        JSR     $EBA3               ; 
8BA8: 20 3C F2        JSR     $F23C               ; 
8BAB: AD 4A 02        LDA     $024A               ; {ram.024A}
8BAE: 09 20           ORA     #$20                ; 
8BB0: 8D 4A 02        STA     $024A               ; {ram.024A}
8BB3: AD 4E 02        LDA     $024E               ; {ram.024E}
8BB6: 09 20           ORA     #$20                ; 
8BB8: 8D 4E 02        STA     $024E               ; {ram.024E}
8BBB: 60              RTS                         ; 
8BBC: 20 FA 8B        JSR     $8BFA               ; {}
8BBF: AD CD 04        LDA     $04CD               ; {ram.04CD}
8BC2: 29 07           AND     #$07                ; 
8BC4: F0 20           BEQ     $8BE6               ; {}
8BC6: 20 E7 8B        JSR     $8BE7               ; {}
8BC9: 90 1B           BCC     $8BE6               ; {}
8BCB: AD CD 04        LDA     $04CD               ; {ram.04CD}
8BCE: 29 07           AND     #$07                ; 
8BD0: C9 07           CMP     #$07                ; 
8BD2: D0 12           BNE     $8BE6               ; {}
8BD4: A5 BF           LDA     <$BF                ; {ram.00BF}
8BD6: F0 0E           BEQ     $8BE6               ; {}
8BD8: 20 14 73        JSR     $7314               ; {ram.7314}
8BDB: D0 09           BNE     $8BE6               ; {}
8BDD: A9 00           LDA     #$00                ; 
8BDF: 85 BF           STA     <$BF                ; {ram.00BF}
8BE1: A9 02           LDA     #$02                ; 
8BE3: 8D 02 06        STA     $0602               ; {ram.SND_ReqMusEff}
8BE6: 60              RTS                         ; 
8BE7: 20 E2 E5        JSR     $E5E2               ; 
8BEA: E6 8B           INC     <$8B                ; {ram.008B}
8BEC: 1A                              ;
8BED: 8C 28 8C        STY     $8C28               ; {}
8BF0: 6F                              ;
8BF1: 8C 4C 8C        STY     $8C4C               ; {}
8BF4: 53                              ;
8BF5: 8C 76 8C        STY     $8C76               ; {}
8BF8: 1A                              ;
8BF9: 8C AC 40        STY     $40AC               ; 
8BFC: 03                              ;
8BFD: B9 50 03        LDA     $0350,Y             ; {ram.0350}
8C00: F0 0C           BEQ     $8C0E               ; {}
8C02: C9 2B           CMP     #$2B                ; 
8C04: 90 13           BCC     $8C19               ; {}
8C06: C9 2E           CMP     #$2E                ; 
8C08: 90 04           BCC     $8C0E               ; {}
8C0A: C9 49           CMP     #$49                ; 
8C0C: 90 0B           BCC     $8C19               ; {}
8C0E: 88              DEY                         ; 
8C0F: 10 EC           BPL     $8BFD               ; {}
8C11: A9 00           LDA     #$00                ; 
8C13: 8D 12 05        STA     $0512               ; {ram.0512}
8C16: EE 4D 03        INC     $034D               ; {ram.034D}
8C19: 60              RTS                         ; 
8C1A: AD 4D 03        LDA     $034D               ; {ram.034D}
8C1D: F0 07           BEQ     $8C26               ; {}
8C1F: A9 01           LDA     #$01                ; 
8C21: 8D CE 04        STA     $04CE               ; {ram.04CE}
8C24: 38              SEC                         ; 
8C25: 60              RTS                         ; 
8C26: 18              CLC                         ; 
8C27: 60              RTS                         ; 
8C28: AD 50 03        LDA     $0350               ; {ram.0350}
8C2B: F0 04           BEQ     $8C31               ; {}
8C2D: C9 53           CMP     #$53                ; 
8C2F: 90 F5           BCC     $8C26               ; {}
8C31: AC 40 03        LDY     $0340               ; {ram.0340}
8C34: B9 50 03        LDA     $0350,Y             ; {ram.0350}
8C37: F0 0E           BEQ     $8C47               ; {}
8C39: C9 53           CMP     #$53                ; 
8C3B: B0 0A           BCS     $8C47               ; {}
8C3D: B9 06 04        LDA     $0406,Y             ; {ram.0406}
8C40: D0 05           BNE     $8C47               ; {}
8C42: A9 10           LDA     #$10                ; 
8C44: 99 06 04        STA     $0406,Y             ; {ram.0406}
8C47: 88              DEY                         ; 
8C48: 10 EA           BPL     $8C34               ; {}
8C4A: 38              SEC                         ; 
8C4B: 60              RTS                         ; 
8C4C: AD CF 04        LDA     $04CF               ; {ram.04CF}
8C4F: F0 D5           BEQ     $8C26               ; {}
8C51: D0 CC           BNE     $8C1F               ; {}
8C53: AD CF 04        LDA     $04CF               ; {ram.04CF}
8C56: F0 CE           BEQ     $8C26               ; {}
8C58: 4A              LSR     A                   ; 
8C59: 90 CB           BCC     $8C26               ; {}
8C5B: EE CF 04        INC     $04CF               ; {ram.04CF}
8C5E: A2 0B           LDX     #$0B                ; 
8C60: A9 D0           LDA     #$D0                ; 
8C62: 95 70           STA     $70,X               ; {ram.0070}
8C64: A9 60           LDA     #$60                ; 
8C66: 95 84           STA     $84,X               ; {ram.0084}
8C68: A9 70           LDA     #$70                ; 
8C6A: 20 62 E8        JSR     $E862               ; 
8C6D: 38              SEC                         ; 
8C6E: 60              RTS                         ; 
8C6F: AD 72 06        LDA     $0672               ; {ram.0672}
8C72: D0 AB           BNE     $8C1F               ; {}
8C74: 18              CLC                         ; 
8C75: 60              RTS                         ; 
8C76: AD 50 03        LDA     $0350               ; {ram.0350}
8C79: F0 A4           BEQ     $8C1F               ; {}
8C7B: 18              CLC                         ; 
8C7C: 60              RTS                         ; 
8C7D: A5 13           LDA     <$13                ; {ram.0013}
8C7F: 20 E2 E5        JSR     $E5E2               ; 
8C82: A1 8C           LDA     ($8C,X)             ; {ram.008C}
8C84: 9C                              ;
8C85: 8C AC 8C        STY     $8CAC               ; {}
8C88: BE 8C C3        LDX     $C38C,Y             ; 
8C8B: 8C C8 8C        STY     $8CC8               ; {}
8C8E: D1 8C           CMP     ($8C),Y             ; {ram.008C}
8C90: DA                              ;
8C91: 8C FB 8C        STY     $8CFB               ; {}
8C94: 01 8D           ORA     ($8D,X)             ; 
8C96: 0D 8D 56        ORA     $568D               ; 
8C99: 8D 63 8D        STA     $8D63               ; {}
8C9C: A9 80           LDA     #$80                ; 
8C9E: 8D 02 06        STA     $0602               ; {ram.SND_ReqMusEff}
8CA1: 20 84 84        JSR     $8484               ; {}
8CA4: A2 2B           LDX     #$2B                ; 
8CA6: 20 E1 B0        JSR     $B0E1               ; {}
8CA9: E6 13           INC     <$13                ; {ram.0013}
8CAB: 60              RTS                         ; 
8CAC: 20 10 AC        JSR     $AC10               ; {}
8CAF: 90 03           BCC     $8CB4               ; {}
8CB1: 20 B2 83        JSR     $83B2               ; {}
8CB4: AD 02 03        LDA     $0302               ; {ram.0302}
8CB7: 18              CLC                         ; 
8CB8: 69 08           ADC     #$08                ; 
8CBA: 8D 02 03        STA     $0302               ; {ram.0302}
8CBD: 60              RTS                         ; 
8CBE: A9 60           LDA     #$60                ; 
8CC0: 4C 2E B1        JMP     $B12E               ; {}
8CC3: A9 62           LDA     #$62                ; 
8CC5: 4C C0 8C        JMP     $8CC0               ; {}
8CC8: A9 00           LDA     #$00                ; 
8CCA: 85 E3           STA     <$E3                ; {ram.00E3}
8CCC: A9 5E           LDA     #$5E                ; 
8CCE: 4C C0 8C        JMP     $8CC0               ; {}
8CD1: A5 FF           LDA     <$FF                ; {ram.CUR_2000}
8CD3: 29 FE           AND     #$FE                ; 
8CD5: 85 FF           STA     <$FF                ; {ram.CUR_2000}
8CD7: E6 13           INC     <$13                ; {ram.0013}
8CD9: 60              RTS                         ; 
8CDA: A5 E5           LDA     <$E5                ; {ram.00E5}
8CDC: F0 F9           BEQ     $8CD7               ; {}
8CDE: A5 33           LDA     <$33                ; {ram.0033}
8CE0: D0 10           BNE     $8CF2               ; {}
8CE2: A9 05           LDA     #$05                ; 
8CE4: 85 33           STA     <$33                ; {ram.0033}
8CE6: A5 98           LDA     <$98                ; {ram.0098}
8CE8: 4A              LSR     A                   ; 
8CE9: 4A              LSR     A                   ; 
8CEA: 90 09           BCC     $8CF5               ; {}
8CEC: C6 E5           DEC     <$E5                ; {ram.00E5}
8CEE: A9 04           LDA     #$04                ; 
8CF0: 85 98           STA     <$98                ; {ram.0098}
8CF2: 4C 3C F2        JMP     $F23C               ; 
8CF5: D0 F9           BNE     $8CF0               ; {}
8CF7: A9 08           LDA     #$08                ; 
8CF9: D0 F5           BNE     $8CF0               ; {}
8CFB: 20 B7 74        JSR     $74B7               ; {ram.74B7}
8CFE: F0 D7           BEQ     $8CD7               ; {}
8D00: 60              RTS                         ; 
8D01: A9 2C           LDA     #$2C                ; 
8D03: 85 14           STA     <$14                ; {ram.0014}
8D05: A9 0F           LDA     #$0F                ; 
8D07: 85 E5           STA     <$E5                ; {ram.00E5}
8D09: A9 18           LDA     #$18                ; 
8D0B: D0 44           BNE     $8D51               ; {}
8D0D: A5 33           LDA     <$33                ; {ram.0033}
8D0F: D0 44           BNE     $8D55               ; {}
8D11: A2 62           LDX     #$62                ; 
8D13: A5 E5           LDA     <$E5                ; {ram.00E5}
8D15: C9 06           CMP     #$06                ; 
8D17: B0 02           BCS     $8D1B               ; {}
8D19: A2 64           LDX     #$64                ; 
8D1B: A5 84           LDA     <$84                ; {ram.0084}
8D1D: 8D 48 02        STA     $0248               ; {ram.0248}
8D20: 8D 4C 02        STA     $024C               ; {ram.024C}
8D23: 8E 49 02        STX     $0249               ; {ram.0249}
8D26: 8E 4D 02        STX     $024D               ; {ram.024D}
8D29: A9 01           LDA     #$01                ; 
8D2B: 8D 4A 02        STA     $024A               ; {ram.024A}
8D2E: A9 41           LDA     #$41                ; 
8D30: 8D 4E 02        STA     $024E               ; {ram.024E}
8D33: A5 70           LDA     <$70                ; {ram.0070}
8D35: 8D 4B 02        STA     $024B               ; {ram.024B}
8D38: 18              CLC                         ; 
8D39: 69 08           ADC     #$08                ; 
8D3B: 8D 4F 02        STA     $024F               ; {ram.024F}
8D3E: C6 E5           DEC     <$E5                ; {ram.00E5}
8D40: D0 13           BNE     $8D55               ; {}
8D42: A9 10           LDA     #$10                ; 
8D44: 8D 04 06        STA     $0604               ; {ram.SND_Request}
8D47: A9 F8           LDA     #$F8                ; 
8D49: 8D 48 02        STA     $0248               ; {ram.0248}
8D4C: 8D 4C 02        STA     $024C               ; {ram.024C}
8D4F: A9 2E           LDA     #$2E                ; 
8D51: 85 33           STA     <$33                ; {ram.0033}
8D53: E6 13           INC     <$13                ; {ram.0013}
8D55: 60              RTS                         ; 
8D56: A5 33           LDA     <$33                ; {ram.0033}
8D58: D0 FB           BNE     $8D55               ; {}
8D5A: A9 60           LDA     #$60                ; 
8D5C: 85 33           STA     <$33                ; {ram.0033}
8D5E: A9 46           LDA     #$46                ; 
8D60: 4C C0 8C        JMP     $8CC0               ; {}
8D63: A5 33           LDA     <$33                ; {ram.0033}
8D65: D0 18           BNE     $8D7F               ; {}
8D67: 20 A3 EB        JSR     $EBA3               ; 
8D6A: A9 08           LDA     #$08                ; 
8D6C: 85 12           STA     <$12                ; {ram.0012}
8D6E: A9 40           LDA     #$40                ; 
8D70: 8D 02 06        STA     $0602               ; {ram.SND_ReqMusEff}
8D73: A6 16           LDX     <$16                ; {ram.0016}
8D75: BD 30 06        LDA     $0630,X             ; 
8D78: C9 FF           CMP     #$FF                ; 
8D7A: F0 03           BEQ     $8D7F               ; {}
8D7C: FE 30 06        INC     $0630,X             ; 
8D7F: 60              RTS                         ; 
8D80: D6 45           DEC     $45,X               ; {ram.0045}
8D82: E9 07           SBC     #$07                ; 
8D84: C6 55           DEC     <$55                ; {ram.0055}
8D86: D9 17 BE        CMP     $BE17,Y             ; {}
8D89: 54                              ;
8D8A: D1 1F           CMP     ($1F),Y             ; {ram.001F}
8D8C: A5 98           LDA     <$98                ; {ram.0098}
8D8E: 20 13 70        JSR     $7013               ; {ram.7013}
8D91: 85 00           STA     <$00                ; {ram.GP_00}
8D93: 20 13 70        JSR     $7013               ; {ram.7013}
8D96: A5 70           LDA     <$70                ; {ram.0070}
8D98: C0 02           CPY     #$02                ; 
8D9A: B0 02           BCS     $8D9E               ; {}
8D9C: A5 84           LDA     <$84                ; {ram.0084}
8D9E: 85 02           STA     <$02                ; {ram.GP_02}
8DA0: 98              TYA                         ; 
8DA1: 48              PHA                         ; 
8DA2: 18              CLC                         ; 
8DA3: 69 08           ADC     #$08                ; 
8DA5: A8              TAY                         ; 
8DA6: A9 80           LDA     #$80                ; 
8DA8: 20 C5 8D        JSR     $8DC5               ; {}
8DAB: 68              PLA                         ; 
8DAC: A8              TAY                         ; 
8DAD: A5 01           LDA     <$01                ; {ram.GP_01}
8DAF: C9 FF           CMP     #$FF                ; 
8DB1: D0 07           BNE     $8DBA               ; {}
8DB3: A5 98           LDA     <$98                ; {ram.0098}
8DB5: 85 00           STA     <$00                ; {ram.GP_00}
8DB7: 20 13 70        JSR     $7013               ; {ram.7013}
8DBA: A5 10           LDA     <$10                ; {ram.0010}
8DBC: F0 05           BEQ     $8DC3               ; {}
8DBE: 98              TYA                         ; 
8DBF: 18              CLC                         ; 
8DC0: 69 04           ADC     #$04                ; 
8DC2: A8              TAY                         ; 
8DC3: A9 00           LDA     #$00                ; 
8DC5: 85 01           STA     <$01                ; {ram.GP_01}
8DC7: A5 00           LDA     <$00                ; {ram.GP_00}
8DC9: 29 0A           AND     #$0A                ; 
8DCB: F0 27           BEQ     $8DF4               ; {}
8DCD: A5 02           LDA     <$02                ; {ram.GP_02}
8DCF: D9 80 8D        CMP     $8D80,Y             ; {}
8DD2: 90 27           BCC     $8DFB               ; {}
8DD4: A5 F8           LDA     <$F8                ; {ram.00F8}
8DD6: 25 01           AND     <$01                ; {ram.GP_01}
8DD8: 85 F8           STA     <$F8                ; {ram.00F8}
8DDA: A5 10           LDA     <$10                ; {ram.0010}
8DDC: F0 15           BEQ     $8DF3               ; {}
8DDE: A5 01           LDA     <$01                ; {ram.GP_01}
8DE0: D0 11           BNE     $8DF3               ; {}
8DE2: A0 0C           LDY     #$0C                ; 
8DE4: A5 98           LDA     <$98                ; {ram.0098}
8DE6: 29 0C           AND     #$0C                ; 
8DE8: D0 02           BNE     $8DEC               ; {}
8DEA: A0 03           LDY     #$03                ; 
8DEC: 98              TYA                         ; 
8DED: 2D F8 03        AND     $03F8               ; {ram.03F8}
8DF0: 8D F8 03        STA     $03F8               ; {ram.03F8}
8DF3: 60              RTS                         ; 
8DF4: A5 02           LDA     <$02                ; {ram.GP_02}
8DF6: D9 80 8D        CMP     $8D80,Y             ; {}
8DF9: 90 D9           BCC     $8DD4               ; {}
8DFB: A9 FF           LDA     #$FF                ; 
8DFD: 85 01           STA     <$01                ; {ram.GP_01}
8DFF: 60              RTS                         ; 
8E00: AD 57 06        LDA     $0657               ; {ram.0657}
8E03: F0 FA           BEQ     $8DFF               ; {}
8E05: A2 0D           LDX     #$0D                ; 
8E07: B5 AC           LDA     $AC,X               ; {ram.00AC}
8E09: D0 F4           BNE     $8DFF               ; {}
8E0B: A9 05           LDA     #$05                ; 
8E0D: 9D D0 03        STA     $03D0,X             ; {ram.03D0}
8E10: A9 01           LDA     #$01                ; 
8E12: 20 8F 8E        JSR     $8E8F               ; {}
8E15: A9 01           LDA     #$01                ; 
8E17: 4C 80 6D        JMP     $6D80               ; {ram.6D80}
8E1A: 31 FF           AND     ($FF),Y             ; {ram.CUR_2000}
8E1C: AD 56 06        LDA     $0656               ; {ram.0656}
8E1F: C9 0F           CMP     #$0F                ; 
8E21: F0 4E           BEQ     $8E71               ; {}
8E23: 20 E2 E5        JSR     $E5E2               ; 
8E26: 38              SEC                         ; 
8E27: 8E DD 70        STX     $70DD               ; {ram.70DD}
8E2A: 72                              ;
8E2B: 8E A6 8E        STX     $8EA6               ; {}
8E2E: 4F                              ;
8E2F: 71 71           ADC     ($71),Y             ; {ram.0071}
8E31: EF                              ;
8E32: A7                              ;
8E33: 8E B6 8E        STX     $8EB6               ; {}
8E36: C7                              ;
8E37: 8E AD 74        STX     $74AD               ; {ram.74AD}
8E3A: 06 0D           ASL     <$0D                ; {ram.000D}
8E3C: 75 06           ADC     <$06,X              ; {ram.0006}
8E3E: F0 31           BEQ     $8E71               ; {}
8E40: A2 0F           LDX     #$0F                ; 
8E42: B5 AC           LDA     $AC,X               ; {ram.00AC}
8E44: F0 03           BEQ     $8E49               ; {}
8E46: 0A              ASL     A                   ; 
8E47: 90 28           BCC     $8E71               ; {}
8E49: A9 10           LDA     #$10                ; 
8E4B: 95 AC           STA     $AC,X               ; {ram.00AC}
8E4D: AC 75 06        LDY     $0675               ; {ram.0675}
8E50: B9 1A 8E        LDA     $8E1A,Y             ; {}
8E53: 9D 80 03        STA     $0380,X             ; 
8E56: 20 1B 71        JSR     $711B               ; {ram.711B}
8E59: A9 C0           LDA     #$C0                ; 
8E5B: 9D BC 03        STA     $03BC,X             ; {ram.03BC}
8E5E: A9 03           LDA     #$03                ; 
8E60: 9D D0 03        STA     $03D0,X             ; {ram.03D0}
8E63: A9 01           LDA     #$01                ; 
8E65: 8D D0 03        STA     $03D0               ; {ram.03D0}
8E68: AD F8 03        LDA     $03F8               ; {ram.03F8}
8E6B: D0 02           BNE     $8E6F               ; {}
8E6D: A5 98           LDA     <$98                ; {ram.0098}
8E6F: 95 98           STA     $98,X               ; {ram.0098}
8E71: 60              RTS                         ; 
8E72: AD 5A 06        LDA     $065A               ; {ram.065A}
8E75: F0 2F           BEQ     $8EA6               ; {}
8E77: A2 12           LDX     #$12                ; 
8E79: B5 AC           LDA     $AC,X               ; {ram.00AC}
8E7B: F0 03           BEQ     $8E80               ; {}
8E7D: 0A              ASL     A                   ; 
8E7E: 90 26           BCC     $8EA6               ; {}
8E80: AD 6D 06        LDA     $066D               ; {ram.066D}
8E83: F0 21           BEQ     $8EA6               ; {}
8E85: A9 02           LDA     #$02                ; 
8E87: 20 80 6D        JSR     $6D80               ; {ram.6D80}
8E8A: EE 7E 06        INC     $067E               ; {ram.067E}
8E8D: A9 10           LDA     #$10                ; 
8E8F: 95 AC           STA     $AC,X               ; {ram.00AC}
8E91: A9 C0           LDA     #$C0                ; 
8E93: 9D BC 03        STA     $03BC,X             ; {ram.03BC}
8E96: 20 16 71        JSR     $7116               ; {ram.7116}
8E99: B5 98           LDA     $98,X               ; {ram.0098}
8E9B: 29 0C           AND     #$0C                ; 
8E9D: F0 07           BEQ     $8EA6               ; {}
8E9F: B5 70           LDA     $70,X               ; {ram.0070}
8EA1: 18              CLC                         ; 
8EA2: 69 03           ADC     #$03                ; 
8EA4: 95 70           STA     $70,X               ; {ram.0070}
8EA6: 60              RTS                         ; 
8EA7: A2 0F           LDX     #$0F                ; 
8EA9: B5 AC           LDA     $AC,X               ; {ram.00AC}
8EAB: D0 19           BNE     $8EC6               ; {}
8EAD: A9 FF           LDA     #$FF                ; 
8EAF: 95 28           STA     $28,X               ; {ram.0028}
8EB1: A9 80           LDA     #$80                ; 
8EB3: 4C 14 71        JMP     $7114               ; {ram.7114}
8EB6: AD 5E 06        LDA     $065E               ; {ram.065E}
8EB9: F0 0B           BEQ     $8EC6               ; {}
8EBB: CE 5E 06        DEC     $065E               ; {ram.065E}
8EBE: A9 01           LDA     #$01                ; 
8EC0: 85 63           STA     <$63                ; {ram.0063}
8EC2: A9 02           LDA     #$02                ; 
8EC4: 85 E0           STA     <$E0                ; {ram.??SND_E0??}
8EC6: 60              RTS                         ; 
8EC7: A2 12           LDX     #$12                ; 
8EC9: B5 AC           LDA     $AC,X               ; {ram.00AC}
8ECB: D0 F9           BNE     $8EC6               ; {}
8ECD: A9 05           LDA     #$05                ; 
8ECF: 9D D0 03        STA     $03D0,X             ; {ram.03D0}
8ED2: A9 31           LDA     #$31                ; 
8ED4: 4C 8F 8E        JMP     $8E8F               ; {}
8ED7: A5 12           LDA     <$12                ; {ram.0012}
8ED9: C9 09           CMP     #$09                ; 
8EDB: D0 3F           BNE     $8F1C               ; {}
8EDD: A5 84           LDA     <$84                ; {ram.0084}
8EDF: C9 40           CMP     #$40                ; 
8EE1: B0 E3           BCS     $8EC6               ; {}
8EE3: AD F8 03        LDA     $03F8               ; {ram.03F8}
8EE6: 29 08           AND     #$08                ; 
8EE8: F0 DC           BEQ     $8EC6               ; {}
8EEA: A0 06           LDY     #$06                ; 
8EEC: A5 EB           LDA     <$EB                ; {ram.00EB}
8EEE: 48              PHA                         ; 
8EEF: 88              DEY                         ; 
8EF0: D9 B2 6B        CMP     $6BB2,Y             ; 
8EF3: D0 FA           BNE     $8EEF               ; {}
8EF5: A8              TAY                         ; 
8EF6: A5 70           LDA     <$70                ; {ram.0070}
8EF8: C9 80           CMP     #$80                ; 
8EFA: B0 06           BCS     $8F02               ; {}
8EFC: B9 7E 68        LDA     $687E,Y             ; 
8EFF: 4C 05 8F        JMP     $8F05               ; {}
8F02: B9 FE 68        LDA     $68FE,Y             ; 
8F05: 20 58 8F        JSR     $8F58               ; {}
8F08: 68              PLA                         ; 
8F09: A8              TAY                         ; 
8F0A: B9 7E 69        LDA     $697E,Y             ; 
8F0D: 48              PHA                         ; 
8F0E: 29 F0           AND     #$F0                ; 
8F10: 85 70           STA     <$70                ; {ram.0070}
8F12: 68              PLA                         ; 
8F13: 0A              ASL     A                   ; 
8F14: 0A              ASL     A                   ; 
8F15: 0A              ASL     A                   ; 
8F16: 0A              ASL     A                   ; 
8F17: 09 0D           ORA     #$0D                ; 
8F19: 85 84           STA     <$84                ; {ram.0084}
8F1B: 60              RTS                         ; 
8F1C: 48              PHA                         ; 
8F1D: 20 46 6E        JSR     $6E46               ; {ram.6E46}
8F20: 68              PLA                         ; 
8F21: C9 0C           CMP     #$0C                ; 
8F23: D0 4E           BNE     $8F73               ; {}
8F25: AD 94 03        LDA     $0394               ; {ram.0394}
8F28: D0 48           BNE     $8F72               ; {}
8F2A: A5 84           LDA     <$84                ; {ram.0084}
8F2C: C9 9D           CMP     #$9D                ; 
8F2E: D0 43           BNE     $8F73               ; {}
8F30: A0 01           LDY     #$01                ; 
8F32: A5 70           LDA     <$70                ; {ram.0070}
8F34: C9 50           CMP     #$50                ; 
8F36: F0 0A           BEQ     $8F42               ; {}
8F38: C8              INY                         ; 
8F39: C9 80           CMP     #$80                ; 
8F3B: F0 05           BEQ     $8F42               ; {}
8F3D: C8              INY                         ; 
8F3E: C9 B0           CMP     #$B0                ; 
8F40: D0 30           BNE     $8F72               ; {}
8F42: 84 00           STY     <$00                ; {ram.GP_00}
8F44: A0 FF           LDY     #$FF                ; 
8F46: A5 EB           LDA     <$EB                ; {ram.00EB}
8F48: C8              INY                         ; 
8F49: D9 B2 6B        CMP     $6BB2,Y             ; 
8F4C: D0 FA           BNE     $8F48               ; {}
8F4E: 98              TYA                         ; 
8F4F: 18              CLC                         ; 
8F50: 65 00           ADC     <$00                ; {ram.GP_00}
8F52: 29 03           AND     #$03                ; 
8F54: A8              TAY                         ; 
8F55: B9 B2 6B        LDA     $6BB2,Y             ; 
8F58: 85 EB           STA     <$EB                ; {ram.00EB}
8F5A: 20 C6 E6        JSR     $E6C6               ; 
8F5D: A9 0A           LDA     #$0A                ; 
8F5F: 85 12           STA     <$12                ; {ram.0012}
8F61: A9 00           LDA     #$00                ; 
8F63: 85 13           STA     <$13                ; {ram.0013}
8F65: 85 11           STA     <$11                ; {ram.0011}
8F67: 85 0F           STA     <$0F                ; {ram.000F}
8F69: 85 AC           STA     <$AC                ; {ram.00AC}
8F6B: 85 C0           STA     <$C0                ; {ram.00C0}
8F6D: 85 D3           STA     <$D3                ; {ram.00D3}
8F6F: 8D F0 04        STA     $04F0               ; {ram.04F0}
8F72: 60              RTS                         ; 
8F73: 20 61 F1        JSR     $F161               ; 
8F76: A5 11           LDA     <$11                ; {ram.0011}
8F78: F0 E3           BEQ     $8F5D               ; {}
8F7A: 60              RTS                         ; 
8F7B: A6 64           LDX     <$64                ; {ram.0064}
8F7D: F0 49           BEQ     $8FC8               ; {}
8F7F: B5 AC           LDA     $AC,X               ; {ram.00AC}
8F81: F0 3E           BEQ     $8FC1               ; {}
8F83: B5 98           LDA     $98,X               ; {ram.0098}
8F85: 29 0C           AND     #$0C                ; 
8F87: F0 11           BEQ     $8F9A               ; {}
8F89: A5 70           LDA     <$70                ; {ram.0070}
8F8B: D5 70           CMP     $70,X               ; {ram.0070}
8F8D: D0 32           BNE     $8FC1               ; {}
8F8F: A5 84           LDA     <$84                ; {ram.0084}
8F91: 18              CLC                         ; 
8F92: 69 03           ADC     #$03                ; 
8F94: 38              SEC                         ; 
8F95: F5 84           SBC     $84,X               ; {ram.0084}
8F97: 4C A8 8F        JMP     $8FA8               ; {}
8F9A: A5 84           LDA     <$84                ; {ram.0084}
8F9C: 18              CLC                         ; 
8F9D: 69 03           ADC     #$03                ; 
8F9F: D5 84           CMP     $84,X               ; {ram.0084}
8FA1: D0 1E           BNE     $8FC1               ; {}
8FA3: A5 70           LDA     <$70                ; {ram.0070}
8FA5: 38              SEC                         ; 
8FA6: F5 70           SBC     $70,X               ; {ram.0070}
8FA8: 20 1F 70        JSR     $701F               ; {ram.701F}
8FAB: 85 00           STA     <$00                ; {ram.GP_00}
8FAD: C9 10           CMP     #$10                ; 
8FAF: 90 18           BCC     $8FC9               ; {}
8FB1: C9 10           CMP     #$10                ; 
8FB3: D0 0C           BNE     $8FC1               ; {}
8FB5: A5 98           LDA     <$98                ; {ram.0098}
8FB7: D5 98           CMP     $98,X               ; {ram.0098}
8FB9: D0 06           BNE     $8FC1               ; {}
8FBB: B5 AC           LDA     $AC,X               ; {ram.00AC}
8FBD: C9 01           CMP     #$01                ; 
8FBF: F0 0C           BEQ     $8FCD               ; {}
8FC1: A9 00           LDA     #$00                ; 
8FC3: 85 64           STA     <$64                ; {ram.0064}
8FC5: 20 B1 FE        JSR     $FEB1               ; 
8FC8: 60              RTS                         ; 
8FC9: A9 02           LDA     #$02                ; 
8FCB: 95 AC           STA     $AC,X               ; {ram.00AC}
8FCD: AD F8 03        LDA     $03F8               ; {ram.03F8}
8FD0: F0 3F           BEQ     $9011               ; {}
8FD2: A5 98           LDA     <$98                ; {ram.0098}
8FD4: A4 00           LDY     <$00                ; {ram.GP_00}
8FD6: F0 04           BEQ     $8FDC               ; {}
8FD8: D5 98           CMP     $98,X               ; {ram.0098}
8FDA: F0 35           BEQ     $9011               ; {}
8FDC: B5 98           LDA     $98,X               ; {ram.0098}
8FDE: C5 0F           CMP     <$0F                ; {ram.000F}
8FE0: F0 2F           BEQ     $9011               ; {}
8FE2: 20 13 70        JSR     $7013               ; {ram.7013}
8FE5: C5 98           CMP     <$98                ; {ram.0098}
8FE7: F0 28           BEQ     $9011               ; {}
8FE9: C9 04           CMP     #$04                ; 
8FEB: D0 22           BNE     $900F               ; {}
8FED: AD F8 03        LDA     $03F8               ; {ram.03F8}
8FF0: C9 08           CMP     #$08                ; 
8FF2: D0 1B           BNE     $900F               ; {}
8FF4: 20 1F 90        JSR     $901F               ; {}
8FF7: A5 84           LDA     <$84                ; {ram.0084}
8FF9: 48              PHA                         ; 
8FFA: 38              SEC                         ; 
8FFB: E9 08           SBC     #$08                ; 
8FFD: 85 84           STA     <$84                ; {ram.0084}
8FFF: 20 FA ED        JSR     $EDFA               ; 
9002: 68              PLA                         ; 
9003: 85 84           STA     <$84                ; {ram.0084}
9005: A5 0F           LDA     <$0F                ; {ram.000F}
9007: AC 9E 04        LDY     $049E               ; {ram.049E}
900A: CC 4A 03        CPY     $034A               ; {ram.034A}
900D: 90 BE           BCC     $8FCD               ; {}
900F: A9 00           LDA     #$00                ; 
9011: 48              PHA                         ; 
9012: A6 64           LDX     <$64                ; {ram.0064}
9014: 20 93 FA        JSR     $FA93               ; 
9017: A0 0C           LDY     #$0C                ; 
9019: A9 00           LDA     #$00                ; 
901B: 20 0C 79        JSR     $790C               ; {ram.790C}
901E: 68              PLA                         ; 
901F: 85 0F           STA     <$0F                ; {ram.000F}
9021: A2 00           LDX     #$00                ; 
9023: 60              RTS                         ; 
9024: AD 25 05        LDA     $0525               ; {ram.0525}
9027: 85 0A           STA     <$0A                ; {ram.000A}
9029: A0 10           LDY     #$10                ; 
902B: A5 0A           LDA     <$0A                ; {ram.000A}
902D: 29 0F           AND     #$0F                ; 
902F: F0 06           BEQ     $9037               ; {}
9031: A0 F0           LDY     #$F0                ; 
9033: C9 0F           CMP     #$0F                ; 
9035: D0 06           BNE     $903D               ; {}
9037: 98              TYA                         ; 
9038: 18              CLC                         ; 
9039: 65 0A           ADC     <$0A                ; {ram.000A}
903B: 85 0A           STA     <$0A                ; {ram.000A}
903D: A5 0A           LDA     <$0A                ; {ram.000A}
903F: 29 F0           AND     #$F0                ; 
9041: C9 E0           CMP     #$E0                ; 
9043: D0 05           BNE     $904A               ; {}
9045: E6 0A           INC     <$0A                ; {ram.000A}
9047: 4C 50 90        JMP     $9050               ; {}
904A: C9 40           CMP     #$40                ; 
904C: D0 02           BNE     $9050               ; {}
904E: C6 0A           DEC     <$0A                ; {ram.000A}
9050: 20 07 AC        JSR     $AC07               ; {}
9053: A5 0A           LDA     <$0A                ; {ram.000A}
9055: 29 0F           AND     #$0F                ; 
9057: A8              TAY                         ; 
9058: F0 08           BEQ     $9062               ; {}
905A: A9 2C           LDA     #$2C                ; 
905C: 20 76 72        JSR     $7276               ; {ram.7276}
905F: 88              DEY                         ; 
9060: D0 F8           BNE     $905A               ; {}
9062: A5 0A           LDA     <$0A                ; {ram.000A}
9064: 29 F0           AND     #$F0                ; 
9066: 38              SEC                         ; 
9067: E9 40           SBC     #$40                ; 
9069: 4A              LSR     A                   ; 
906A: 4A              LSR     A                   ; 
906B: 4A              LSR     A                   ; 
906C: A8              TAY                         ; 
906D: B1 00           LDA     ($00),Y             ; {ram.GP_00}
906F: C9 84           CMP     #$84                ; 
9071: 90 07           BCC     $907A               ; {}
9073: A5 0A           LDA     <$0A                ; {ram.000A}
9075: CD 25 05        CMP     $0525               ; {ram.0525}
9078: D0 AF           BNE     $9029               ; {}
907A: A5 0A           LDA     <$0A                ; {ram.000A}
907C: 8D 25 05        STA     $0525               ; {ram.0525}
907F: 60              RTS                         ; 
9080: A5 13           LDA     <$13                ; {ram.0013}
9082: 20 E2 E5        JSR     $E5E2               ; 
9085: 17                              ;
9086: B1 4F           LDA     ($4F),Y             ; 
9088: B1 30           LDA     ($30),Y             ; {ram.0030}
908A: B1 4D           LDA     ($4D),Y             ; {ram.004D}
908C: AB                              ;
908D: 10 AC           BPL     $903B               ; {}
908F: 6B                              ;
9090: B1 73           LDA     ($73),Y             ; {ram.0073}
9092: B1 89           LDA     ($89),Y             ; {ram.0089}
9094: 6D 80 B1        ADC     $B180               ; {}
9097: A5 13           LDA     <$13                ; {ram.0013}
9099: 20 E2 E5        JSR     $E5E2               ; 
909C: 17                              ;
909D: B1 4F           LDA     ($4F),Y             ; 
909F: B1 30           LDA     ($30),Y             ; {ram.0030}
90A1: B1 5E           LDA     ($5E),Y             ; {ram.005E}
90A3: AB                              ;
90A4: 10 AC           BPL     $9052               ; {}
90A6: 6B                              ;
90A7: B1 73           LDA     ($73),Y             ; {ram.0073}
90A9: B1 89           LDA     ($89),Y             ; {ram.0089}
90AB: 6D 80 B1        ADC     $B180               ; {}
90AE: A0 05           LDY     #$05                ; 
90B0: A5 EB           LDA     <$EB                ; {ram.00EB}
90B2: D9 21 06        CMP     $0621,Y             ; 
90B5: F0 13           BEQ     $90CA               ; {}
90B7: 88              DEY                         ; 
90B8: 10 F8           BPL     $90B2               ; {}
90BA: 20 CE E6        JSR     $E6CE               ; 
90BD: 29 07           AND     #$07                ; 
90BF: C9 07           CMP     #$07                ; 
90C1: D0 07           BNE     $90CA               ; {}
90C3: B1 00           LDA     ($00),Y             ; {ram.GP_00}
90C5: 29 F8           AND     #$F8                ; 
90C7: 91 00           STA     ($00),Y             ; {ram.GP_00}
90C9: 60              RTS                         ; 
90CA: 20 CE E6        JSR     $E6CE               ; 
90CD: 29 07           AND     #$07                ; 
90CF: F0 F8           BEQ     $90C9               ; {}
90D1: C9 07           CMP     #$07                ; 
90D3: F0 09           BEQ     $90DE               ; {}
90D5: 85 04           STA     <$04                ; {ram.0004}
90D7: A5 03           LDA     <$03                ; {ram.GP_03}
90D9: 38              SEC                         ; 
90DA: E5 04           SBC     <$04                ; {ram.0004}
90DC: 10 04           BPL     $90E2               ; {}
90DE: A9 00           LDA     #$00                ; 
90E0: 85 02           STA     <$02                ; {ram.GP_02}
90E2: 85 03           STA     <$03                ; {ram.GP_03}
90E4: 60              RTS                         ; 
90E5: 20 CE E6        JSR     $E6CE               ; 
90E8: 29 07           AND     #$07                ; 
90EA: 85 02           STA     <$02                ; {ram.GP_02}
90EC: B1 00           LDA     ($00),Y             ; {ram.GP_00}
90EE: 29 F8           AND     #$F8                ; 
90F0: 91 00           STA     ($00),Y             ; {ram.GP_00}
90F2: AD 4F 03        LDA     $034F               ; {ram.034F}
90F5: CD 4E 03        CMP     $034E               ; {ram.034E}
90F8: B0 09           BCS     $9103               ; {}
90FA: 29 07           AND     #$07                ; 
90FC: 18              CLC                         ; 
90FD: 65 02           ADC     <$02                ; {ram.GP_02}
90FF: C9 07           CMP     #$07                ; 
9101: 90 02           BCC     $9105               ; {}
9103: A9 07           LDA     #$07                ; 
9105: 11 00           ORA     ($00),Y             ; {ram.GP_00}
9107: 91 00           STA     ($00),Y             ; {ram.GP_00}
9109: 60              RTS                         ; 
910A: A5 13           LDA     <$13                ; {ram.0013}
910C: 20 E2 E5        JSR     $E5E2               ; 
910F: 17                              ;
9110: B1 33           LDA     ($33),Y             ; {ram.0033}
9112: B1 3C           LDA     ($3C),Y             ; {ram.003C}
9114: B1 62           LDA     ($62),Y             ; {ram.0062}
9116: AB                              ;
9117: 10 AC           BPL     $90C5               ; {}
9119: 2C B1 43        BIT     $43B1               ; 
911C: B1 3C           LDA     ($3C),Y             ; {ram.003C}
911E: B1 99           LDA     ($99),Y             ; {ram.0099}
9120: B1 CD           LDA     ($CD),Y             ; 
9122: B1 A0           LDA     ($A0),Y             ; {ram.00A0}
9124: 00              BRK                         ; 
9125: F0 02           BEQ     $9129               ; {}
9127: A0 01           LDY     #$01                ; 
9129: 84 0C           STY     <$0C                ; {ram.000C}
912B: BC 4F 03        LDY     $034F,X             ; {ram.034F}
912E: C8              INY                         ; 
912F: 85 0D           STA     <$0D                ; {ram.000D}
9131: 84 0E           STY     <$0E                ; {ram.000E}
9133: 86 08           STX     <$08                ; {ram.0008}
9135: A9 40           LDA     #$40                ; 
9137: 8D 43 03        STA     $0343               ; {ram.0343}
913A: A9 44           LDA     #$44                ; 
913C: 4C 04 78        JMP     $7804               ; {ram.7804}
913F: A5 53           LDA     <$53                ; {ram.0053}
9141: F0 1B           BEQ     $915E               ; {}
9143: AC F8 03        LDY     $03F8               ; {ram.03F8}
9146: F0 16           BEQ     $915E               ; {}
9148: A5 98           LDA     <$98                ; {ram.0098}
914A: 2D F8 03        AND     $03F8               ; {ram.03F8}
914D: D0 0C           BNE     $915B               ; {}
914F: A5 98           LDA     <$98                ; {ram.0098}
9151: 20 13 70        JSR     $7013               ; {ram.7013}
9154: 2D F8 03        AND     $03F8               ; {ram.03F8}
9157: D0 02           BNE     $915B               ; {}
9159: A5 98           LDA     <$98                ; {ram.0098}
915B: 8D F8 03        STA     $03F8               ; {ram.03F8}
915E: 60              RTS                         ; 
915F: A9 F8           LDA     #$F8                ; 
9161: 8D 40 02        STA     $0240               ; {ram.0240}
9164: 8D 44 02        STA     $0244               ; {ram.0244}
9167: 60              RTS                         ; 
9168: 78              SEI                         ; 
9169: 78              SEI                         ; 
916A: 8D 8D 3D        STA     $3D8D               ; 
916D: BD 00 CF        LDA     $CF00,X             ; 
9170: 5E DE 21        LSR     $21DE,X             ; 
9173: F1 3D           SBC     ($3D),Y             ; {ram.003D}
9175: BF                              ;
9176: 00              BRK                         ; 
9177: D2                              ;
9178: 5C                              ;
9179: DE 1F F1        DEC     $F11F,X             ; 
917C: A5 53           LDA     <$53                ; {ram.0053}
917E: D0 22           BNE     $91A2               ; {}
9180: A5 98           LDA     <$98                ; {ram.0098}
9182: 20 0F 92        JSR     $920F               ; {}
9185: A0 03           LDY     #$03                ; 
9187: A5 00           LDA     <$00                ; {ram.GP_00}
9189: D9 68 91        CMP     $9168,Y             ; {}
918C: D0 0C           BNE     $919A               ; {}
918E: A5 01           LDA     <$01                ; {ram.GP_01}
9190: D9 6C 91        CMP     $916C,Y             ; {}
9193: 90 05           BCC     $919A               ; {}
9195: D9 70 91        CMP     $9170,Y             ; {}
9198: 90 3C           BCC     $91D6               ; {}
919A: 88              DEY                         ; 
919B: 10 EA           BPL     $9187               ; {}
919D: A9 00           LDA     #$00                ; 
919F: 85 53           STA     <$53                ; {ram.0053}
91A1: 60              RTS                         ; 
91A2: 48              PHA                         ; 
91A3: 20 0F 92        JSR     $920F               ; {}
91A6: 68              PLA                         ; 
91A7: 20 13 70        JSR     $7013               ; {ram.7013}
91AA: A5 01           LDA     <$01                ; {ram.GP_01}
91AC: D9 6C 91        CMP     $916C,Y             ; {}
91AF: 90 0B           BCC     $91BC               ; {}
91B1: D9 70 91        CMP     $9170,Y             ; {}
91B4: B0 06           BCS     $91BC               ; {}
91B6: A5 53           LDA     <$53                ; {ram.0053}
91B8: C5 98           CMP     <$98                ; {ram.0098}
91BA: F0 C4           BEQ     $9180               ; {}
91BC: A0 03           LDY     #$03                ; 
91BE: A5 00           LDA     <$00                ; {ram.GP_00}
91C0: D9 68 91        CMP     $9168,Y             ; {}
91C3: D0 0C           BNE     $91D1               ; {}
91C5: A5 01           LDA     <$01                ; {ram.GP_01}
91C7: D9 74 91        CMP     $9174,Y             ; {}
91CA: 90 05           BCC     $91D1               ; {}
91CC: D9 78 91        CMP     $9178,Y             ; {}
91CF: 90 05           BCC     $91D6               ; {}
91D1: 88              DEY                         ; 
91D2: 10 EA           BPL     $91BE               ; {}
91D4: 30 C7           BMI     $919D               ; {}
91D6: 84 0E           STY     <$0E                ; {ram.000E}
91D8: AD F8 03        LDA     $03F8               ; {ram.03F8}
91DB: 29 0F           AND     #$0F                ; 
91DD: 85 02           STA     <$02                ; {ram.GP_02}
91DF: 85 0C           STA     <$0C                ; {ram.000C}
91E1: D9 C3 6D        CMP     $6DC3,Y             ; 
91E4: D0 25           BNE     $920B               ; {}
91E6: 20 F6 A3        JSR     $A3F6               ; {}
91E9: 85 0D           STA     <$0D                ; {ram.000D}
91EB: 20 20 92        JSR     $9220               ; {}
91EE: A4 0E           LDY     <$0E                ; {ram.000E}
91F0: 30 19           BMI     $920B               ; {}
91F2: B9 C3 6D        LDA     $6DC3,Y             ; 
91F5: 85 98           STA     <$98                ; {ram.0098}
91F7: 85 0F           STA     <$0F                ; {ram.000F}
91F9: 85 53           STA     <$53                ; {ram.0053}
91FB: A5 0D           LDA     <$0D                ; {ram.000D}
91FD: 29 07           AND     #$07                ; 
91FF: C9 02           CMP     #$02                ; 
9201: F0 09           BEQ     $920C               ; {}
9203: C9 03           CMP     #$03                ; 
9205: F0 05           BEQ     $920C               ; {}
9207: C9 04           CMP     #$04                ; 
9209: F0 01           BEQ     $920C               ; {}
920B: 60              RTS                         ; 
920C: 4C 82 F1        JMP     $F182               ; 
920F: A6 70           LDX     <$70                ; {ram.0070}
9211: A4 84           LDY     <$84                ; {ram.0084}
9213: 29 03           AND     #$03                ; 
9215: F0 04           BEQ     $921B               ; {}
9217: A4 70           LDY     <$70                ; {ram.0070}
9219: A6 84           LDX     <$84                ; {ram.0084}
921B: 86 00           STX     <$00                ; {ram.GP_00}
921D: 84 01           STY     <$01                ; {ram.GP_01}
921F: 60              RTS                         ; 
9220: 29 07           AND     #$07                ; 
9222: 20 E2 E5        JSR     $E5E2               ; 
9225: 39 92 35        AND     $3592,Y             ; 
9228: 92                              ;
9229: 3A                              ;
922A: 92                              ;
922B: 3A                              ;
922C: 92                              ;
922D: 4A              LSR     A                   ; 
922E: 92                              ;
922F: 6B                              ;
9230: 92                              ;
9231: 6B                              ;
9232: 92                              ;
9233: 51 92           EOR     ($92),Y             ; {ram.0092}
9235: A0 FF           LDY     #$FF                ; 
9237: 84 0E           STY     <$0E                ; {ram.000E}
9239: 60              RTS                         ; 
923A: A5 28           LDA     <$28                ; {ram.0028}
923C: F0 05           BEQ     $9243               ; {}
923E: C9 01           CMP     #$01                ; 
9240: D0 05           BNE     $9247               ; {}
9242: 60              RTS                         ; 
9243: A9 18           LDA     #$18                ; 
9245: 85 28           STA     <$28                ; {ram.0028}
9247: 4C 35 92        JMP     $9235               ; {}
924A: A5 0C           LDA     <$0C                ; {ram.000C}
924C: 25 EE           AND     <$EE                ; {ram.00EE}
924E: F0 E5           BEQ     $9235               ; {}
9250: 60              RTS                         ; 
9251: A5 54           LDA     <$54                ; {ram.0054}
9253: D0 E0           BNE     $9235               ; {}
9255: A5 0C           LDA     <$0C                ; {ram.000C}
9257: 25 EE           AND     <$EE                ; {ram.00EE}
9259: F0 DA           BEQ     $9235               ; {}
925B: 2D 19 05        AND     $0519               ; {ram.0519}
925E: F0 02           BEQ     $9262               ; {}
9260: D0 2C           BNE     $928E               ; {}
9262: AD 19 05        LDA     $0519               ; {ram.0519}
9265: 05 0C           ORA     <$0C                ; {ram.000C}
9267: 8D 19 05        STA     $0519               ; {ram.0519}
926A: 60              RTS                         ; 
926B: A5 0C           LDA     <$0C                ; {ram.000C}
926D: 25 EE           AND     <$EE                ; {ram.00EE}
926F: D0 21           BNE     $9292               ; {}
9271: A5 54           LDA     <$54                ; {ram.0054}
9273: D0 19           BNE     $928E               ; {}
9275: AD 64 06        LDA     $0664               ; {ram.0664}
9278: D0 08           BNE     $9282               ; {}
927A: AD 6E 06        LDA     $066E               ; {ram.066E}
927D: F0 0C           BEQ     $928B               ; {}
927F: CE 6E 06        DEC     $066E               ; {ram.066E}
9282: A5 0C           LDA     <$0C                ; {ram.000C}
9284: 20 DA 8A        JSR     $8ADA               ; {}
9287: A9 20           LDA     #$20                ; 
9289: 85 28           STA     <$28                ; {ram.0028}
928B: 4C 35 92        JMP     $9235               ; {}
928E: A5 28           LDA     <$28                ; {ram.0028}
9290: D0 F9           BNE     $928B               ; {}
9292: 60              RTS                         ; 
9293: A0 05           LDY     #$05                ; 
9295: A5 EB           LDA     <$EB                ; {ram.00EB}
9297: D9 21 06        CMP     $0621,Y             ; 
929A: F0 2A           BEQ     $92C6               ; {}
929C: 88              DEY                         ; 
929D: 10 F8           BPL     $9297               ; {}
929F: 20 CE E6        JSR     $E6CE               ; 
92A2: 29 C0           AND     #$C0                ; 
92A4: C9 C0           CMP     #$C0                ; 
92A6: D0 1E           BNE     $92C6               ; {}
92A8: A5 02           LDA     <$02                ; {ram.GP_02}
92AA: C9 32           CMP     #$32                ; 
92AC: 90 0C           BCC     $92BA               ; {}
92AE: C9 3A           CMP     #$3A                ; 
92B0: F0 08           BEQ     $92BA               ; {}
92B2: C9 3B           CMP     #$3B                ; 
92B4: F0 04           BEQ     $92BA               ; {}
92B6: C9 49           CMP     #$49                ; 
92B8: 90 16           BCC     $92D0               ; {}
92BA: B1 00           LDA     ($00),Y             ; {ram.GP_00}
92BC: 29 3F           AND     #$3F                ; 
92BE: 91 00           STA     ($00),Y             ; {ram.GP_00}
92C0: A9 00           LDA     #$00                ; 
92C2: 99 60 05        STA     $0560,Y             ; 
92C5: 60              RTS                         ; 
92C6: A4 EB           LDY     <$EB                ; {ram.00EB}
92C8: A5 03           LDA     <$03                ; {ram.GP_03}
92CA: 38              SEC                         ; 
92CB: F9 60 05        SBC     $0560,Y             ; 
92CE: 10 04           BPL     $92D4               ; {}
92D0: A9 00           LDA     #$00                ; 
92D2: 85 02           STA     <$02                ; {ram.GP_02}
92D4: 85 03           STA     <$03                ; {ram.GP_03}
92D6: 60              RTS                         ; 
92D7: 20 CE E6        JSR     $E6CE               ; 
92DA: 29 3F           AND     #$3F                ; 
92DC: 91 00           STA     ($00),Y             ; {ram.GP_00}
92DE: AD 4E 03        LDA     $034E               ; {ram.034E}
92E1: F0 33           BEQ     $9316               ; {}
92E3: AD 4F 03        LDA     $034F               ; {ram.034F}
92E6: F0 13           BEQ     $92FB               ; {}
92E8: AC 5F 03        LDY     $035F               ; {ram.035F}
92EB: C0 32           CPY     #$32                ; 
92ED: 90 0C           BCC     $92FB               ; {}
92EF: C0 3A           CPY     #$3A                ; 
92F1: F0 08           BEQ     $92FB               ; {}
92F3: C0 3B           CPY     #$3B                ; 
92F5: F0 04           BEQ     $92FB               ; {}
92F7: C0 49           CPY     #$49                ; 
92F9: 90 1B           BCC     $9316               ; {}
92FB: CD 4E 03        CMP     $034E               ; {ram.034E}
92FE: B0 16           BCS     $9316               ; {}
9300: A4 EB           LDY     <$EB                ; {ram.00EB}
9302: 18              CLC                         ; 
9303: 79 60 05        ADC     $0560,Y             ; 
9306: 99 60 05        STA     $0560,Y             ; 
9309: C9 03           CMP     #$03                ; 
930B: 90 02           BCC     $930F               ; {}
930D: A9 02           LDA     #$02                ; 
930F: 18              CLC                         ; 
9310: 6A              ROR     A                   ; 
9311: 6A              ROR     A                   ; 
9312: 6A              ROR     A                   ; 
9313: 4C 1F 93        JMP     $931F               ; {}
9316: A4 EB           LDY     <$EB                ; {ram.00EB}
9318: A9 0F           LDA     #$0F                ; 
931A: 99 60 05        STA     $0560,Y             ; 
931D: A9 C0           LDA     #$C0                ; 
931F: 11 00           ORA     ($00),Y             ; {ram.GP_00}
9321: 91 00           STA     ($00),Y             ; {ram.GP_00}
9323: 60              RTS                         ; 
9324: 00              BRK                         ; 
9325: 10 20           BPL     $9347               ; {}
9327: 40              RTI                         ; 
9328: 20 CE E6        JSR     $E6CE               ; 
932B: AC BC 6B        LDY     $6BBC               ; {ram.6BBC}
932E: B1 00           LDA     ($00),Y             ; {ram.GP_00}
9330: 29 C0           AND     #$C0                ; 
9332: C9 C0           CMP     #$C0                ; 
9334: F0 17           BEQ     $934D               ; {}
9336: A4 EB           LDY     <$EB                ; {ram.00EB}
9338: B9 7E 6A        LDA     $6A7E,Y             ; 
933B: 29 60           AND     #$60                ; 
933D: 0A              ASL     A                   ; 
933E: 2A              ROL     A                   ; 
933F: 2A              ROL     A                   ; 
9340: 2A              ROL     A                   ; 
9341: AA              TAX                         ; 
9342: BD 24 93        LDA     $9324,X             ; {}
9345: F0 06           BEQ     $934D               ; {}
9347: 09 80           ORA     #$80                ; 
9349: 8D 01 06        STA     $0601               ; {ram.??SND_601??}
934C: 60              RTS                         ; 
934D: A9 80           LDA     #$80                ; 
934F: 4C 80 6D        JMP     $6D80               ; {ram.6D80}
9352: FF                              ;
9353: FF                              ;
9354: FF                              ;
9355: FF                              ;
9356: FF                              ;
9357: FF                              ;
9358: FF                              ;
9359: FF                              ;
935A: FF                              ;
935B: FF                              ;
935C: FF                              ;
935D: FF                              ;
935E: FF                              ;
935F: FF                              ;
9360: FF                              ;
9361: FF                              ;
9362: FF                              ;
9363: FF                              ;
9364: FF                              ;
9365: FF                              ;
9366: FF                              ;
9367: FF                              ;
9368: FF                              ;
9369: FF                              ;
936A: FF                              ;
936B: FF                              ;
936C: FF                              ;
936D: FF                              ;
936E: FF                              ;
936F: FF                              ;
9370: FF                              ;
9371: FF                              ;
9372: FF                              ;
9373: FF                              ;
9374: FF                              ;
9375: FF                              ;
9376: FF                              ;
9377: FF                              ;
9378: FF                              ;
9379: FF                              ;
937A: FF                              ;
937B: FF                              ;
937C: FF                              ;
937D: FF                              ;
937E: FF                              ;
937F: FF                              ;
9380: FF                              ;
9381: FF                              ;
9382: FF                              ;
9383: FF                              ;
9384: FF                              ;
9385: FF                              ;
9386: FF                              ;
9387: FF                              ;
9388: FF                              ;
9389: FF                              ;
938A: FF                              ;
938B: FF                              ;
938C: FF                              ;
938D: FF                              ;
938E: FF                              ;
938F: FF                              ;
9390: FF                              ;
9391: FF                              ;
9392: FF                              ;
9393: FF                              ;
9394: FF                              ;
9395: FF                              ;
9396: FF                              ;
9397: FF                              ;
9398: FF                              ;
9399: FF                              ;
939A: FF                              ;
939B: FF                              ;
939C: FF                              ;
939D: FF                              ;
939E: FF                              ;
939F: FF                              ;
93A0: FF                              ;
93A1: FF                              ;
93A2: FF                              ;
93A3: FF                              ;
93A4: FF                              ;
93A5: FF                              ;
93A6: FF                              ;
93A7: FF                              ;
93A8: FF                              ;
93A9: FF                              ;
93AA: FF                              ;
93AB: FF                              ;
93AC: FF                              ;
93AD: FF                              ;
93AE: FF                              ;
93AF: FF                              ;
93B0: FF                              ;
93B1: FF                              ;
93B2: FF                              ;
93B3: FF                              ;
93B4: FF                              ;
93B5: FF                              ;
93B6: FF                              ;
93B7: FF                              ;
93B8: FF                              ;
93B9: FF                              ;
93BA: FF                              ;
93BB: FF                              ;
93BC: FF                              ;
93BD: FF                              ;
93BE: FF                              ;
93BF: FF                              ;
93C0: FF                              ;
93C1: FF                              ;
93C2: FF                              ;
93C3: FF                              ;
93C4: FF                              ;
93C5: FF                              ;
93C6: FF                              ;
93C7: FF                              ;
93C8: FF                              ;
93C9: FF                              ;
93CA: FF                              ;
93CB: FF                              ;
93CC: FF                              ;
93CD: FF                              ;
93CE: FF                              ;
93CF: FF                              ;
93D0: FF                              ;
93D1: FF                              ;
93D2: FF                              ;
93D3: FF                              ;
93D4: FF                              ;
93D5: FF                              ;
93D6: FF                              ;
93D7: FF                              ;
93D8: FF                              ;
93D9: FF                              ;
93DA: FF                              ;
93DB: FF                              ;
93DC: FF                              ;
93DD: FF                              ;
93DE: FF                              ;
93DF: FF                              ;
93E0: FF                              ;
93E1: FF                              ;
93E2: FF                              ;
93E3: FF                              ;
93E4: FF                              ;
93E5: FF                              ;
93E6: FF                              ;
93E7: FF                              ;
93E8: FF                              ;
93E9: FF                              ;
93EA: FF                              ;
93EB: FF                              ;
93EC: FF                              ;
93ED: FF                              ;
93EE: FF                              ;
93EF: FF                              ;
93F0: FF                              ;
93F1: FF                              ;
93F2: FF                              ;
93F3: FF                              ;
93F4: FF                              ;
93F5: FF                              ;
93F6: FF                              ;
93F7: FF                              ;
93F8: FF                              ;
93F9: FF                              ;
93FA: FF                              ;
93FB: FF                              ;
93FC: FF                              ;
93FD: FF                              ;
93FE: FF                              ;
93FF: FF                              ;
9400: A4 09           LDY     <$09                ; {ram.0009}
9402: B9 E3 A5        LDA     $A5E3,Y             ; {}
9405: 18              CLC                         ; 
9406: 65 07           ADC     <$07                ; {ram.0007}
9408: A8              TAY                         ; 
9409: B9 D5 A5        LDA     $A5D5,Y             ; {}
940C: A8              TAY                         ; 
940D: B1 02           LDA     ($02),Y             ; {ram.GP_02}
940F: 9D 02 03        STA     $0302,X             ; {ram.0302}
9412: E8              INX                         ; 
9413: E6 07           INC     <$07                ; {ram.0007}
9415: C6 04           DEC     <$04                ; {ram.0004}
9417: 60              RTS                         ; 
9418: 00              BRK                         ; 
9419: 00              BRK                         ; 
941A: 00              BRK                         ; 
941B: 00              BRK                         ; 
941C: 00              BRK                         ; 
941D: 00              BRK                         ; 
941E: 00              BRK                         ; 
941F: 50 01           BVC     $9422               ; {}
9421: 01 81           ORA     ($81,X)             ; {ram.0081}
9423: 01 01           ORA     ($01,X)             ; {ram.GP_01}
9425: 01 01           ORA     ($01,X)             ; {ram.GP_01}
9427: 01 01           ORA     ($01,X)             ; {ram.GP_01}
9429: F1 C8           SBC     ($C8),Y             ; {ram.00C8}
942B: A0 A1           LDY     #$A1                ; 
942D: A0 06           LDY     #$06                ; 
942F: 38              SEC                         ; 
9430: A1 D2           LDA     ($D2,X)             ; 
9432: A5 A4           LDA     <$A4                ; {ram.00A4}
9434: A2 A3           LDX     #$A3                ; 
9436: F0 A6           BEQ     $93DE               ; {}
9438: 01 01           ORA     ($01,X)             ; {ram.GP_01}
943A: 01 50           ORA     ($50,X)             ; {ram.0050}
943C: 01 01           ORA     ($01,X)             ; {ram.GP_01}
943E: 81 01           STA     ($01,X)             ; {ram.GP_01}
9440: 01 A7           ORA     ($A7,X)             ; {ram.00A7}
9442: A9 C8           LDA     #$C8                ; 
9444: C7                              ;
9445: A0 06           LDY     #$06                ; 
9447: 06 A1           ASL     <$A1                ; {ram.00A1}
9449: A5 A4           LDA     <$A4                ; {ram.00A4}
944B: A8              TAY                         ; 
944C: F0 A6           BEQ     $93F4               ; {}
944E: 01 81           ORA     ($81,X)             ; {ram.0081}
9450: 01 01           ORA     ($01,X)             ; {ram.GP_01}
9452: 50 00           BVC     $9454               ; {}
9454: 00              BRK                         ; 
9455: 00              BRK                         ; 
9456: 00              BRK                         ; 
9457: 00              BRK                         ; 
9458: 00              BRK                         ; 
9459: E6 06           INC     <$06                ; {ram.0006}
945B: 06 A1           ASL     <$A1                ; {ram.00A1}
945D: A0 E7           LDY     #$E7                ; 
945F: E6 A1           INC     <$A1                ; {ram.00A1}
9461: 84 90           STY     <$90                ; {ram.0090}
9463: 02                              ;
9464: 10 02           BPL     $9468               ; {}
9466: 02                              ;
9467: A8              TAY                         ; 
9468: A9 A8           LDA     #$A8                ; 
946A: A9 03           LDA     #$03                ; 
946C: 05 E4           ORA     <$E4                ; {ram.00E4}
946E: 24 02           BIT     <$02                ; {ram.GP_02}
9470: 02                              ;
9471: 03                              ;
9472: 05 22           ORA     <$22                ; {ram.0022}
9474: 24 02           BIT     <$02                ; {ram.GP_02}
9476: A8              TAY                         ; 
9477: A6 A7           LDX     <$A7                ; {ram.00A7}
9479: A6 A7           LDX     <$A7                ; {ram.00A7}
947B: F1 A9           SBC     ($A9),Y             ; {ram.00A9}
947D: A8              TAY                         ; 
947E: A9 A2           LDA     #$A2                ; 
9480: A3                              ;
9481: A8              TAY                         ; 
9482: A6 A7           LDX     <$A7                ; {ram.00A7}
9484: A6 A7           LDX     <$A7                ; {ram.00A7}
9486: A6 01           LDX     <$01                ; {ram.GP_01}
9488: 01 01           ORA     ($01,X)             ; {ram.GP_01}
948A: 01 01           ORA     ($01,X)             ; {ram.GP_01}
948C: 50 01           BVC     $948F               ; {}
948E: A7                              ;
948F: F1 F0           SBC     ($F0),Y             ; {ram.00F0}
9491: A6 81           LDX     <$81                ; {ram.0081}
9493: 01 A7           ORA     ($A7,X)             ; {ram.00A7}
9495: A6 01           LDX     <$01                ; {ram.GP_01}
9497: 01 A7           ORA     ($A7,X)             ; {ram.00A7}
9499: A9 A8           LDA     #$A8                ; 
949B: A9 71           LDA     #$71                ; 
949D: 32                              ;
949E: 33                              ;
949F: 02                              ;
94A0: 34                              ;
94A1: 02                              ;
94A2: 34                              ;
94A3: 02                              ;
94A4: 34                              ;
94A5: A8              TAY                         ; 
94A6: F0 00           BEQ     $94A8               ; {}
94A8: 00              BRK                         ; 
94A9: A9 10           LDA     #$10                ; 
94AB: 53                              ;
94AC: 54                              ;
94AD: B1 55           LDA     ($55),Y             ; {ram.0055}
94AF: B2                              ;
94B0: 54                              ;
94B1: 54                              ;
94B2: 54                              ;
94B3: 56 02           LSR     $02,X               ; {ram.GP_02}
94B5: B5 A8           LDA     $A8,X               ; {ram.00A8}
94B7: 00              BRK                         ; 
94B8: 00              BRK                         ; 
94B9: F1 A9           SBC     ($A9),Y             ; {ram.00A9}
94BB: B7                              ;
94BC: 02                              ;
94BD: B7                              ;
94BE: 67                              ;
94BF: 68              PLA                         ; 
94C0: 70 B7           BVS     $9479               ; {}
94C2: 02                              ;
94C3: B7                              ;
94C4: A5 A4           LDA     <$A4                ; {ram.00A4}
94C6: A8              TAY                         ; 
94C7: 00              BRK                         ; 
94C8: 00              BRK                         ; 
94C9: 00              BRK                         ; 
94CA: 00              BRK                         ; 
94CB: 00              BRK                         ; 
94CC: 00              BRK                         ; 
94CD: 50 A7           BVC     $9476               ; {}
94CF: A9 10           LDA     #$10                ; 
94D1: 02                              ;
94D2: A2 A3           LDX     #$A3                ; 
94D4: F0 F1           BEQ     $94C7               ; {}
94D6: A9 02           LDA     #$02                ; 
94D8: 02                              ;
94D9: 02                              ;
94DA: A8              TAY                         ; 
94DB: F0 F1           BEQ     $94CE               ; {}
94DD: A9 A5           LDA     #$A5                ; 
94DF: A4 02           LDY     <$02                ; {ram.GP_02}
94E1: D2                              ;
94E2: C8              INY                         ; 
94E3: C7                              ;
94E4: A0 38           LDY     #$38                ; 
94E6: E7                              ;
94E7: 00              BRK                         ; 
94E8: 80                              ;
94E9: 80                              ;
94EA: 80                              ;
94EB: 80                              ;
94EC: 80                              ;
94ED: 96 80           STX     $80,Y               ; {ram.0080}
94EF: 80                              ;
94F0: 80                              ;
94F1: 80                              ;
94F2: 13                              ;
94F3: 13                              ;
94F4: 13                              ;
94F5: 13                              ;
94F6: 13                              ;
94F7: 13                              ;
94F8: 13                              ;
94F9: 00              BRK                         ; 
94FA: 02                              ;
94FB: 02                              ;
94FC: 67                              ;
94FD: 70 02           BVS     $9501               ; {}
94FF: 67                              ;
9500: D7                              ;
9501: 70 02           BVS     $9505               ; {}
9503: 67                              ;
9504: 70 02           BVS     $9508               ; {}
9506: 00              BRK                         ; 
9507: 13                              ;
9508: 00              BRK                         ; 
9509: F1 A9           SBC     ($A9),Y             ; {ram.00A9}
950B: 02                              ;
950C: 33                              ;
950D: 02                              ;
950E: 32                              ;
950F: B6 34           LDX     $34,Y               ; {ram.0034}
9511: D2                              ;
9512: 02                              ;
9513: 64                              ;
9514: F2                              ;
9515: F3                              ;
9516: 02                              ;
9517: 64                              ;
9518: 66 02           ROR     <$02                ; {ram.GP_02}
951A: E5 D8           SBC     <$D8                ; {ram.00D8}
951C: 66 02           ROR     <$02                ; {ram.GP_02}
951E: 02                              ;
951F: B6 71           LDX     $71,Y               ; {ram.0071}
9521: 02                              ;
9522: 32                              ;
9523: 02                              ;
9524: 33                              ;
9525: 02                              ;
9526: A8              TAY                         ; 
9527: 00              BRK                         ; 
9528: 00              BRK                         ; 
9529: E6 06           INC     <$06                ; {ram.0006}
952B: 83                              ;
952C: 06 A1           ASL     <$A1                ; {ram.00A1}
952E: 84 90           STY     <$90                ; {ram.0090}
9530: D2                              ;
9531: 64                              ;
9532: F2                              ;
9533: F3                              ;
9534: 64                              ;
9535: F2                              ;
9536: F3                              ;
9537: 64                              ;
9538: 66 02           ROR     <$02                ; {ram.GP_02}
953A: D2                              ;
953B: C8              INY                         ; 
953C: C7                              ;
953D: A0 06           LDY     #$06                ; 
953F: 06 06           ASL     <$06                ; {ram.0006}
9541: 06 83           ASL     <$83                ; {ram.0083}
9543: 06 A1           ASL     <$A1                ; {ram.00A1}
9545: 84 90           STY     <$90                ; {ram.0090}
9547: 02                              ;
9548: 02                              ;
9549: A2 A3           LDX     #$A3                ; 
954B: B7                              ;
954C: 02                              ;
954D: 02                              ;
954E: B7                              ;
954F: 02                              ;
9550: 02                              ;
9551: B7                              ;
9552: B5 02           LDA     $02,X               ; {ram.GP_02}
9554: D2                              ;
9555: B7                              ;
9556: C8              INY                         ; 
9557: A0 06           LDY     #$06                ; 
9559: E7                              ;
955A: E6 38           INC     <$38                ; {ram.0038}
955C: 06 E7           ASL     <$E7                ; {ram.00E7}
955E: E6 A1           INC     <$A1                ; {ram.00A1}
9560: A2 A3           LDX     #$A3                ; 
9562: A8              TAY                         ; 
9563: A9 D2           LDA     #$D2                ; 
9565: B5 A8           LDA     $A8,X               ; {ram.00A8}
9567: A9 A8           LDA     #$A8                ; 
9569: A9 A2           LDA     #$A2                ; 
956B: A3                              ;
956C: A8              TAY                         ; 
956D: A9 D2           LDA     #$D2                ; 
956F: 02                              ;
9570: A0 06           LDY     #$06                ; 
9572: A1 A6           LDA     ($A6,X)             ; {ram.00A6}
9574: A7                              ;
9575: F1 A9           SBC     ($A9),Y             ; {ram.00A9}
9577: 02                              ;
9578: A5 A4           LDA     <$A4                ; {ram.00A4}
957A: C8              INY                         ; 
957B: A0 83           LDY     #$83                ; 
957D: 06 B4           ASL     <$B4                ; {ram.00B4}
957F: B0 B0           BCS     $9531               ; {}
9581: B0 B0           BCS     $9533               ; {}
9583: 73                              ;
9584: 73                              ;
9585: 73                              ;
9586: 73                              ;
9587: 73                              ;
9588: 73                              ;
9589: 73                              ;
958A: 73                              ;
958B: 73                              ;
958C: 73                              ;
958D: 73                              ;
958E: 73                              ;
958F: 73                              ;
9590: 72                              ;
9591: 72                              ;
9592: 72                              ;
9593: 72                              ;
9594: D4                              ;
9595: 72                              ;
9596: 72                              ;
9597: 72                              ;
9598: 72                              ;
9599: 72                              ;
959A: 72                              ;
959B: 72                              ;
959C: D4                              ;
959D: 72                              ;
959E: 72                              ;
959F: 72                              ;
95A0: 72                              ;
95A1: 72                              ;
95A2: 72                              ;
95A3: 72                              ;
95A4: 72                              ;
95A5: 72                              ;
95A6: 72                              ;
95A7: 72                              ;
95A8: 72                              ;
95A9: 72                              ;
95AA: 72                              ;
95AB: 72                              ;
95AC: 72                              ;
95AD: 72                              ;
95AE: C1 06           CMP     ($06,X)             ; {ram.0006}
95B0: 06 06           ASL     <$06                ; {ram.0006}
95B2: 06 06           ASL     <$06                ; {ram.0006}
95B4: 06 83           ASL     <$83                ; {ram.0083}
95B6: 06 01           ASL     <$01                ; {ram.GP_01}
95B8: 01 A7           ORA     ($A7,X)             ; {ram.00A7}
95BA: A9 32           LDA     #$32                ; 
95BC: 02                              ;
95BD: 33                              ;
95BE: 02                              ;
95BF: 11 32           ORA     ($32),Y             ; {ram.0032}
95C1: 02                              ;
95C2: 32                              ;
95C3: 02                              ;
95C4: 71 A8           ADC     ($A8),Y             ; {ram.00A8}
95C6: A6 01           LDX     <$01                ; {ram.GP_01}
95C8: A7                              ;
95C9: A9 02           LDA     #$02                ; 
95CB: B5 02           LDA     $02,X               ; {ram.GP_02}
95CD: B6 02           LDX     $02,Y               ; {ram.GP_02}
95CF: B7                              ;
95D0: 02                              ;
95D1: B7                              ;
95D2: 02                              ;
95D3: B7                              ;
95D4: 02                              ;
95D5: B7                              ;
95D6: 02                              ;
95D7: 02                              ;
95D8: 02                              ;
95D9: 02                              ;
95DA: B5 71           LDA     $71,X               ; {ram.0071}
95DC: A8              TAY                         ; 
95DD: 00              BRK                         ; 
95DE: E6 04           INC     <$04                ; {ram.0004}
95E0: 04                              ;
95E1: D6 97           DEC     $97,X               ; {ram.0097}
95E3: 91 51           STA     ($51),Y             ; {ram.0051}
95E5: B8              CLV                         ; 
95E6: 51 51           EOR     ($51),Y             ; {ram.0051}
95E8: 51 51           EOR     ($51),Y             ; {ram.0051}
95EA: 51 51           EOR     ($51),Y             ; {ram.0051}
95EC: 51 B8           EOR     ($B8),Y             ; 
95EE: 51 01           EOR     ($01),Y             ; {ram.GP_01}
95F0: 01 90           ORA     ($90,X)             ; {ram.0090}
95F2: 02                              ;
95F3: 02                              ;
95F4: D2                              ;
95F5: 02                              ;
95F6: 02                              ;
95F7: 02                              ;
95F8: 02                              ;
95F9: 02                              ;
95FA: 64                              ;
95FB: 66 E5           ROR     <$E5                ; {ram.00E5}
95FD: D8              CLD                         ; 
95FE: 65 66           ADC     <$66                ; {ram.SND_PtrA}
9600: E5 F3           SBC     <$F3                ; {ram.00F3}
9602: 64                              ;
9603: F2                              ;
9604: F3                              ;
9605: 02                              ;
9606: 00              BRK                         ; 
9607: 13                              ;
9608: 00              BRK                         ; 
9609: 00              BRK                         ; 
960A: E2                              ;
960B: 82                              ;
960C: 07                              ;
960D: 07                              ;
960E: 88              DEY                         ; 
960F: 07                              ;
9610: 07                              ;
9611: 82                              ;
9612: 07                              ;
9613: 07                              ;
9614: 82                              ;
9615: 07                              ;
9616: 02                              ;
9617: 02                              ;
9618: 02                              ;
9619: 02                              ;
961A: 07                              ;
961B: 82                              ;
961C: 07                              ;
961D: 07                              ;
961E: 82                              ;
961F: 07                              ;
9620: 07                              ;
9621: 88              DEY                         ; 
9622: 07                              ;
9623: 07                              ;
9624: 82                              ;
9625: 07                              ;
9626: 15 15           ORA     $15,X               ; {ram.0015}
9628: 00              BRK                         ; 
9629: 00              BRK                         ; 
962A: 02                              ;
962B: B7                              ;
962C: B7                              ;
962D: B7                              ;
962E: 67                              ;
962F: D7                              ;
9630: F5 70           SBC     $70,X               ; {ram.0070}
9632: B7                              ;
9633: B7                              ;
9634: B7                              ;
9635: 02                              ;
9636: 00              BRK                         ; 
9637: 00              BRK                         ; 
9638: 00              BRK                         ; 
9639: A9 02           LDA     #$02                ; 
963B: 71 32           ADC     ($32),Y             ; {ram.0032}
963D: 34                              ;
963E: B5 A8           LDA     $A8,X               ; {ram.00A8}
9640: 00              BRK                         ; 
9641: 00              BRK                         ; 
9642: A9 02           LDA     #$02                ; 
9644: 02                              ;
9645: B5 02           LDA     $02,X               ; {ram.GP_02}
9647: 02                              ;
9648: 02                              ;
9649: 02                              ;
964A: B7                              ;
964B: A8              TAY                         ; 
964C: A9 B7           LDA     #$B7                ; 
964E: A2 A3           LDX     #$A3                ; 
9650: B7                              ;
9651: 02                              ;
9652: B6 B7           LDX     $B7,Y               ; {ram.00B7}
9654: A2 A3           LDX     #$A3                ; 
9656: B7                              ;
9657: 02                              ;
9658: 02                              ;
9659: 02                              ;
965A: B7                              ;
965B: B6 B5           LDX     $B5,Y               ; {ram.00B5}
965D: B7                              ;
965E: A2 A3           LDX     #$A3                ; 
9660: B7                              ;
9661: 02                              ;
9662: 10 B7           BPL     $961B               ; {}
9664: 02                              ;
9665: B6 A8           LDX     $A8,Y               ; {ram.00A8}
9667: 00              BRK                         ; 
9668: 00              BRK                         ; 
9669: A9 07           LDA     #$07                ; 
966B: D3                              ;
966C: 02                              ;
966D: A8              TAY                         ; 
966E: F0 F1           BEQ     $9661               ; {}
9670: A9 39           LDA     #$39                ; 
9672: 91 51           STA     ($51),Y             ; {ram.0051}
9674: 97                              ;
9675: 91 51           STA     ($51),Y             ; {ram.0051}
9677: 97                              ;
9678: 91 51           STA     ($51),Y             ; {ram.0051}
967A: 97                              ;
967B: 91 51           STA     ($51),Y             ; {ram.0051}
967D: 97                              ;
967E: 13                              ;
967F: C3                              ;
9680: 58              CLI                         ; 
9681: 58              CLI                         ; 
9682: 58              CLI                         ; 
9683: 91 51           STA     ($51),Y             ; {ram.0051}
9685: 97                              ;
9686: 85 47           STA     <$47                ; {ram.0047}
9688: 61 61           ADC     ($61,X)             ; {ram.0061}
968A: 61 61           ADC     ($61,X)             ; {ram.0061}
968C: 61 61           ADC     ($61,X)             ; {ram.0061}
968E: 60              RTS                         ; 
968F: 76 76           ROR     <$76,X              ; {ram.0076}
9691: 17                              ;
9692: 17                              ;
9693: 26 17           ROL     <$17                ; {ram.0017}
9695: 31 28           AND     ($28),Y             ; {ram.0028}
9697: 17                              ;
9698: F9 F9 F9        SBC     $F9F9,Y             ; 
969B: F9 F9 F9        SBC     $F9F9,Y             ; 
969E: F9 F9 F9        SBC     $F9F9,Y             ; 
96A1: F9 F9 F9        SBC     $F9F9,Y             ; 
96A4: F9 F9 F9        SBC     $F9F9,Y             ; 
96A7: F9 F9 F9        SBC     $F9F9,Y             ; 
96AA: C4 C4           CPY     <$C4                ; {ram.00C4}
96AC: C4 C4           CPY     <$C4                ; {ram.00C4}
96AE: C4 C4           CPY     <$C4                ; {ram.00C4}
96B0: C4 C4           CPY     <$C4                ; {ram.00C4}
96B2: C4 C4           CPY     <$C4                ; {ram.00C4}
96B4: C4 C4           CPY     <$C4                ; {ram.00C4}
96B6: C4 F9           CPY     <$F9                ; {ram.00F9}
96B8: F9 C4 C4        SBC     $C4C4,Y             ; 
96BB: C4 C4           CPY     <$C4                ; {ram.00C4}
96BD: C4 C4           CPY     <$C4                ; {ram.00C4}
96BF: C4 C4           CPY     <$C4                ; {ram.00C4}
96C1: C4 C4           CPY     <$C4                ; {ram.00C4}
96C3: C4 C4           CPY     <$C4                ; {ram.00C4}
96C5: C4 F9           CPY     <$F9                ; {ram.00F9}
96C7: F9 02 02        SBC     $0202,Y             ; {ram.0202}
96CA: 02                              ;
96CB: B6 02           LDX     $02,Y               ; {ram.GP_02}
96CD: 03                              ;
96CE: 05 21           ORA     <$21                ; {ram.0021}
96D0: 21 E4           AND     ($E4,X)             ; {ram.00E4}
96D2: 24 02           BIT     <$02                ; {ram.GP_02}
96D4: A0 06           LDY     #$06                ; 
96D6: 06 06           ASL     <$06                ; {ram.0006}
96D8: 06 06           ASL     <$06                ; {ram.0006}
96DA: 83                              ;
96DB: A1 02           LDA     ($02,X)             ; {ram.GP_02}
96DD: D2                              ;
96DE: A2 18           LDX     #$18                ; 
96E0: 18              CLC                         ; 
96E1: 35 36           AND     $36,X               ; {ram.0036}
96E3: 36 36           ROL     $36,X               ; {ram.0036}
96E5: 36 36           ROL     $36,X               ; {ram.0036}
96E7: 36 36           ROL     $36,X               ; {ram.0036}
96E9: 36 52           ROL     $52,X               ; {ram.0052}
96EB: 52                              ;
96EC: 52                              ;
96ED: 52                              ;
96EE: 52                              ;
96EF: 52                              ;
96F0: 86 E1           STX     <$E1                ; {ram.00E1}
96F2: 13                              ;
96F3: 13                              ;
96F4: 13                              ;
96F5: 13                              ;
96F6: 13                              ;
96F7: 13                              ;
96F8: 00              BRK                         ; 
96F9: 02                              ;
96FA: 67                              ;
96FB: 70 02           BVS     $96FF               ; {}
96FD: 67                              ;
96FE: 87                              ;
96FF: 70 02           BVS     $9703               ; {}
9701: 67                              ;
9702: 70 02           BVS     $9706               ; {}
9704: 02                              ;
9705: 00              BRK                         ; 
9706: 00              BRK                         ; 
9707: 00              BRK                         ; 
9708: 00              BRK                         ; 
9709: 00              BRK                         ; 
970A: 18              CLC                         ; 
970B: 94 18           STY     $18,X               ; {ram.0018}
970D: 18              CLC                         ; 
970E: 94 18           STY     $18,X               ; {ram.0018}
9710: 18              CLC                         ; 
9711: 94 18           STY     $18,X               ; {ram.0018}
9713: 18              CLC                         ; 
9714: 94 18           STY     $18,X               ; {ram.0018}
9716: A3                              ;
9717: 02                              ;
9718: 02                              ;
9719: A2 18           LDX     #$18                ; 
971B: 94 18           STY     $18,X               ; {ram.0018}
971D: 18              CLC                         ; 
971E: 94 18           STY     $18,X               ; {ram.0018}
9720: 18              CLC                         ; 
9721: 94 18           STY     $18,X               ; {ram.0018}
9723: 18              CLC                         ; 
9724: 94 18           STY     $18,X               ; {ram.0018}
9726: 16 16           ASL     $16,X               ; {ram.0016}
9728: F0 F1           BEQ     $971B               ; {}
972A: A9 C8           LDA     #$C8                ; 
972C: C7                              ;
972D: A0 06           LDY     #$06                ; 
972F: 83                              ;
9730: A1 A5           LDA     ($A5,X)             ; {ram.00A5}
9732: A4 C8           LDY     <$C8                ; {ram.00C8}
9734: C7                              ;
9735: A6 01           LDX     <$01                ; {ram.GP_01}
9737: 01 01           ORA     ($01,X)             ; {ram.GP_01}
9739: A7                              ;
973A: 02                              ;
973B: B7                              ;
973C: 02                              ;
973D: B7                              ;
973E: B6 B7           LDX     $B7,Y               ; {ram.00B7}
9740: 02                              ;
9741: B7                              ;
9742: D2                              ;
9743: B7                              ;
9744: 02                              ;
9745: B6 00           LDX     $00,Y               ; {ram.GP_00}
9747: 00              BRK                         ; 
9748: 00              BRK                         ; 
9749: A9 B7           LDA     #$B7                ; 
974B: 02                              ;
974C: B7                              ;
974D: 02                              ;
974E: B7                              ;
974F: 02                              ;
9750: 07                              ;
9751: 39 47 47        AND     $4747,Y             ; 
9754: 47                              ;
9755: 47                              ;
9756: 91 78           STA     ($78),Y             ; 
9758: 78              SEI                         ; 
9759: 78              SEI                         ; 
975A: 78              SEI                         ; 
975B: 78              SEI                         ; 
975C: B8              CLV                         ; 
975D: 51 97           EOR     ($97),Y             ; {ram.0097}
975F: 91 51           STA     ($51),Y             ; {ram.0051}
9761: 51 51           EOR     ($51),Y             ; {ram.0051}
9763: 97                              ;
9764: 91 51           STA     ($51),Y             ; {ram.0051}
9766: 51 97           EOR     ($97),Y             ; {ram.0097}
9768: 91 97           STA     ($97),Y             ; {ram.0097}
976A: 58              CLI                         ; 
976B: 58              CLI                         ; 
976C: 91 51           STA     ($51),Y             ; {ram.0051}
976E: 97                              ;
976F: 91 97           STA     ($97),Y             ; {ram.0097}
9771: 13                              ;
9772: 13                              ;
9773: 13                              ;
9774: 13                              ;
9775: 13                              ;
9776: 13                              ;
9777: 13                              ;
9778: 13                              ;
9779: 00              BRK                         ; 
977A: 02                              ;
977B: 64                              ;
977C: F2                              ;
977D: F3                              ;
977E: 64                              ;
977F: 65 66           ADC     <$66                ; {ram.SND_PtrA}
9781: E5 D8           SBC     <$D8                ; {ram.00D8}
9783: 66 02           ROR     <$02                ; {ram.GP_02}
9785: 02                              ;
9786: 01 12           ORA     ($12,X)             ; {ram.0012}
9788: 12                              ;
9789: 12                              ;
978A: 12                              ;
978B: 12                              ;
978C: 12                              ;
978D: 12                              ;
978E: 44                              ;
978F: 18              CLC                         ; 
9790: 18              CLC                         ; 
9791: 17                              ;
9792: 28              PLP                         ; 
9793: 17                              ;
9794: 25 17           AND     <$17                ; {ram.0017}
9796: 17                              ;
9797: 15 00           ORA     $00,X               ; {ram.GP_00}
9799: A9 02           LDA     #$02                ; 
979B: 77                              ;
979C: 02                              ;
979D: 53                              ;
979E: 54                              ;
979F: D1 D1           CMP     ($D1),Y             ; {ram.00D1}
97A1: 54                              ;
97A2: 56 02           LSR     $02,X               ; {ram.GP_02}
97A4: 77                              ;
97A5: 02                              ;
97A6: A8              TAY                         ; 
97A7: 00              BRK                         ; 
97A8: 00              BRK                         ; 
97A9: 00              BRK                         ; 
97AA: C6 C6           DEC     <$C6                ; {ram.00C6}
97AC: C6 C6           DEC     <$C6                ; {ram.00C6}
97AE: C6 C5           DEC     <$C5                ; {ram.00C5}
97B0: C5 C6           CMP     <$C6                ; {ram.00C6}
97B2: C6 C6           DEC     <$C6                ; {ram.00C6}
97B4: C6 C6           DEC     <$C6                ; {ram.00C6}
97B6: C6 F9           DEC     <$F9                ; {ram.00F9}
97B8: F9 C6 C6        SBC     $C6C6,Y             ; 
97BB: C6 C6           DEC     <$C6                ; {ram.00C6}
97BD: C6 C6           DEC     <$C6                ; {ram.00C6}
97BF: C6 C6           DEC     <$C6                ; {ram.00C6}
97C1: C6 C6           DEC     <$C6                ; {ram.00C6}
97C3: C6 C5           DEC     <$C5                ; {ram.00C5}
97C5: C5 00           CMP     <$00                ; {ram.GP_00}
97C7: 00              BRK                         ; 
97C8: 15 76           ORA     $76,X               ; {ram.0076}
97CA: 26 76           ROL     <$76                ; {ram.0076}
97CC: 26 76           ROL     <$76                ; {ram.0076}
97CE: 49 18           EOR     #$18                ; 
97D0: 18              CLC                         ; 
97D1: 49 76           EOR     #$76                ; 
97D3: 26 76           ROL     <$76                ; {ram.0076}
97D5: 25 76           AND     <$76                ; {ram.0076}
97D7: 15 00           ORA     $00,X               ; {ram.GP_00}
97D9: 00              BRK                         ; 
97DA: D5 08           CMP     $08,X               ; {ram.0008}
97DC: 08              PHP                         ; 
97DD: 08              PHP                         ; 
97DE: 08              PHP                         ; 
97DF: 08              PHP                         ; 
97E0: 08              PHP                         ; 
97E1: 35 36           AND     $36,X               ; {ram.0036}
97E3: 36 36           ROL     $36,X               ; {ram.0036}
97E5: 36 36           ROL     $36,X               ; {ram.0036}
97E7: 36 36           ROL     $36,X               ; {ram.0036}
97E9: 36 36           ROL     $36,X               ; {ram.0036}
97EB: 36 36           ROL     $36,X               ; {ram.0036}
97ED: 52                              ;
97EE: D0 52           BNE     $9842               ; {}
97F0: 86 E1           STX     <$E1                ; {ram.00E1}
97F2: 13                              ;
97F3: 13                              ;
97F4: 13                              ;
97F5: 13                              ;
97F6: 13                              ;
97F7: 13                              ;
97F8: 00              BRK                         ; 
97F9: 00              BRK                         ; 
97FA: D5 93           CMP     $93,X               ; {ram.0093}
97FC: 08              PHP                         ; 
97FD: 08              PHP                         ; 
97FE: 93                              ;
97FF: 08              PHP                         ; 
9800: 08              PHP                         ; 
9801: 93                              ;
9802: 08              PHP                         ; 
9803: 08              PHP                         ; 
9804: 93                              ;
9805: 08              PHP                         ; 
9806: B5 02           LDA     $02,X               ; {ram.GP_02}
9808: 02                              ;
9809: 02                              ;
980A: 08              PHP                         ; 
980B: 93                              ;
980C: 08              PHP                         ; 
980D: 08              PHP                         ; 
980E: 93                              ;
980F: 08              PHP                         ; 
9810: 08              PHP                         ; 
9811: 93                              ;
9812: 08              PHP                         ; 
9813: 08              PHP                         ; 
9814: 93                              ;
9815: 08              PHP                         ; 
9816: 15 15           ORA     $15,X               ; {ram.0015}
9818: 00              BRK                         ; 
9819: A9 02           LDA     #$02                ; 
981B: 77                              ;
981C: 10 77           BPL     $9895               ; {}
981E: 02                              ;
981F: 07                              ;
9820: 18              CLC                         ; 
9821: 45 13           EOR     <$13                ; {ram.0013}
9823: 13                              ;
9824: 13                              ;
9825: 13                              ;
9826: 13                              ;
9827: 13                              ;
9828: 13                              ;
9829: 00              BRK                         ; 
982A: 02                              ;
982B: 02                              ;
982C: 67                              ;
982D: 70 02           BVS     $9831               ; {}
982F: 67                              ;
9830: D7                              ;
9831: 70 02           BVS     $9835               ; {}
9833: 67                              ;
9834: 70 02           BVS     $9838               ; {}
9836: 00              BRK                         ; 
9837: 13                              ;
9838: 13                              ;
9839: 13                              ;
983A: 13                              ;
983B: 13                              ;
983C: 13                              ;
983D: 13                              ;
983E: 43                              ;
983F: 92                              ;
9840: 52                              ;
9841: F7                              ;
9842: 62                              ;
9843: 62                              ;
9844: 62                              ;
9845: 62                              ;
9846: 62                              ;
9847: 62                              ;
9848: 62                              ;
9849: 62                              ;
984A: 62                              ;
984B: 62                              ;
984C: 62                              ;
984D: 62                              ;
984E: 62                              ;
984F: 62                              ;
9850: 62                              ;
9851: 62                              ;
9852: 62                              ;
9853: F7                              ;
9854: 62                              ;
9855: 62                              ;
9856: 62                              ;
9857: 62                              ;
9858: 62                              ;
9859: 62                              ;
985A: 62                              ;
985B: 48              PHA                         ; 
985C: 48              PHA                         ; 
985D: 48              PHA                         ; 
985E: 41 18           EOR     ($18,X)             ; {ram.0018}
9860: 18              CLC                         ; 
9861: 17                              ;
9862: 17                              ;
9863: 17                              ;
9864: 17                              ;
9865: 14                              ;
9866: 15 15           ORA     $15,X               ; {ram.0015}
9868: 15 15           ORA     $15,X               ; {ram.0015}
986A: 17                              ;
986B: 75 17           ADC     <$17,X              ; {ram.0017}
986D: 16 16           ASL     $16,X               ; {ram.0016}
986F: 18              CLC                         ; 
9870: 18              CLC                         ; 
9871: 16 16           ASL     $16,X               ; {ram.0016}
9873: 16 16           ASL     $16,X               ; {ram.0016}
9875: 16 16           ASL     $16,X               ; {ram.0016}
9877: 16 F0           ASL     $F0,X               ; {ram.00F0}
9879: F1 A9           SBC     ($A9),Y             ; {ram.00A9}
987B: A2 A3           LDX     #$A3                ; 
987D: 77                              ;
987E: 02                              ;
987F: 08              PHP                         ; 
9880: 08              PHP                         ; 
9881: 02                              ;
9882: 77                              ;
9883: 10 02           BPL     $9887               ; {}
9885: A8              TAY                         ; 
9886: F0 F1           BEQ     $9879               ; {}
9888: 16 76           ASL     $76,X               ; {ram.0076}
988A: 27                              ;
988B: 76 76           ROR     <$76,X              ; {ram.0076}
988D: 76 26           ROR     <$26,X              ; {ram.0026}
988F: 76 25           ROR     <$25,X              ; {ram.0025}
9891: 76 15           ROR     <$15,X              ; {ram.0015}
9893: 14                              ;
9894: 18              CLC                         ; 
9895: 18              CLC                         ; 
9896: 15 15           ORA     $15,X               ; {ram.0015}
9898: 00              BRK                         ; 
9899: F1 A2           SBC     ($A2),Y             ; {ram.00A2}
989B: A3                              ;
989C: A2 A3           LDX     #$A3                ; 
989E: A0 83           LDY     #$83                ; 
98A0: 06 06           ASL     <$06                ; {ram.0006}
98A2: A1 A2           LDA     ($A2,X)             ; {ram.00A2}
98A4: A3                              ;
98A5: A6 01           LDX     <$01                ; {ram.GP_01}
98A7: A7                              ;
98A8: 16 23           ASL     $23,X               ; {ram.0023}
98AA: 25 18           AND     <$18                ; {ram.0018}
98AC: 25 23           AND     <$23                ; {ram.0023}
98AE: 26 23           ROL     <$23                ; {ram.0023}
98B0: 23                              ;
98B1: 25 23           AND     <$23                ; {ram.0023}
98B3: 26 18           ROL     <$18                ; {ram.0018}
98B5: 31 23           AND     ($23),Y             ; {ram.0023}
98B7: 16 16           ASL     $16,X               ; {ram.0016}
98B9: 28              PLP                         ; 
98BA: 17                              ;
98BB: 17                              ;
98BC: 17                              ;
98BD: 49 17           EOR     #$17                ; 
98BF: 17                              ;
98C0: 17                              ;
98C1: 17                              ;
98C2: 49 17           EOR     #$17                ; 
98C4: 17                              ;
98C5: 17                              ;
98C6: 28              PLP                         ; 
98C7: 15 00           ORA     $00,X               ; {ram.GP_00}
98C9: 00              BRK                         ; 
98CA: E6 A1           INC     <$A1                ; {ram.00A1}
98CC: A2 18           LDX     #$18                ; 
98CE: 18              CLC                         ; 
98CF: 18              CLC                         ; 
98D0: 18              CLC                         ; 
98D1: 45 12           EOR     <$12                ; {ram.0012}
98D3: 13                              ;
98D4: 12                              ;
98D5: 13                              ;
98D6: 13                              ;
98D7: 13                              ;
98D8: 00              BRK                         ; 
98D9: 00              BRK                         ; 
98DA: 04                              ;
98DB: 04                              ;
98DC: 04                              ;
98DD: 04                              ;
98DE: 04                              ;
98DF: 04                              ;
98E0: 04                              ;
98E1: 04                              ;
98E2: 04                              ;
98E3: 04                              ;
98E4: 04                              ;
98E5: 04                              ;
98E6: 83                              ;
98E7: 00              BRK                         ; 
98E8: 15 28           ORA     $28,X               ; {ram.0028}
98EA: 17                              ;
98EB: 25 17           AND     <$17                ; {ram.0017}
98ED: 25 17           AND     <$17                ; {ram.0017}
98EF: 25 17           AND     <$17                ; {ram.0017}
98F1: 31 76           AND     ($76),Y             ; {ram.0076}
98F3: 76 16           ROR     <$16,X              ; {ram.0016}
98F5: 16 16           ASL     $16,X               ; {ram.0016}
98F7: 16 16           ASL     $16,X               ; {ram.0016}
98F9: 16 17           ASL     $17,X               ; {ram.0017}
98FB: 17                              ;
98FC: 30 57           BMI     $9955               ; {}
98FE: 57                              ;
98FF: 74                              ;
9900: 74                              ;
9901: 57                              ;
9902: 57                              ;
9903: 57                              ;
9904: 57                              ;
9905: 57                              ;
9906: 30 30           BMI     $9938               ; {}
9908: 30 30           BMI     $993A               ; {}
990A: 17                              ;
990B: 17                              ;
990C: 76 76           ROR     <$76,X              ; {ram.0076}
990E: 31 18           AND     ($18),Y             ; {ram.0018}
9910: 18              CLC                         ; 
9911: 76 27           ROR     <$27,X              ; {ram.0027}
9913: 76 17           ROR     <$17,X              ; {ram.0017}
9915: 76 28           ROR     <$28,X              ; {ram.0028}
9917: 16 16           ASL     $16,X               ; {ram.0016}
9919: 16 17           ASL     $17,X               ; {ram.0017}
991B: 76 76           ROR     <$76,X              ; {ram.0076}
991D: 26 17           ROL     <$17                ; {ram.0017}
991F: 23                              ;
9920: 23                              ;
9921: 46 52           LSR     <$52                ; {ram.0052}
9923: 48              PHA                         ; 
9924: 48              PHA                         ; 
9925: 52                              ;
9926: 37                              ;
9927: 37                              ;
9928: 37                              ;
9929: 37                              ;
992A: 52                              ;
992B: 52                              ;
992C: 86 13           STX     <$13                ; {ram.0013}
992E: 13                              ;
992F: 92                              ;
9930: D0 52           BNE     $9984               ; {}
9932: 36 52           ROL     $52,X               ; {ram.0052}
9934: 36 52           ROL     $52,X               ; {ram.0052}
9936: 37                              ;
9937: 37                              ;
9938: 37                              ;
9939: 37                              ;
993A: 37                              ;
993B: 48              PHA                         ; 
993C: 48              PHA                         ; 
993D: 48              PHA                         ; 
993E: 41 23           EOR     ($23,X)             ; {ram.0023}
9940: 23                              ;
9941: 17                              ;
9942: 31 17           AND     ($17),Y             ; {ram.0017}
9944: 25 25           AND     <$25                ; {ram.0025}
9946: 17                              ;
9947: 17                              ;
9948: 17                              ;
9949: 17                              ;
994A: 17                              ;
994B: 27                              ;
994C: 17                              ;
994D: 27                              ;
994E: 17                              ;
994F: 26 17           ROL     <$17                ; {ram.0017}
9951: 26 17           ROL     <$17                ; {ram.0017}
9953: 27                              ;
9954: 17                              ;
9955: 26 17           ROL     <$17                ; {ram.0017}
9957: 26 26           ROL     <$26                ; {ram.0026}
9959: 17                              ;
995A: 26 76           ROL     <$76                ; {ram.0076}
995C: 27                              ;
995D: 76 26           ROR     <$26,X              ; {ram.0026}
995F: 18              CLC                         ; 
9960: 18              CLC                         ; 
9961: 26 76           ROL     <$76                ; {ram.0076}
9963: 26 76           ROL     <$76                ; {ram.0076}
9965: 27                              ;
9966: 76 16           ROR     <$16,X              ; {ram.0016}
9968: 16 16           ASL     $16,X               ; {ram.0016}
996A: 16 16           ASL     $16,X               ; {ram.0016}
996C: 16 16           ASL     $16,X               ; {ram.0016}
996E: 16 18           ASL     $18,X               ; {ram.0018}
9970: 18              CLC                         ; 
9971: 63                              ;
9972: 42                              ;
9973: 42                              ;
9974: 42                              ;
9975: 42                              ;
9976: 42                              ;
9977: 42                              ;
9978: 42                              ;
9979: 42                              ;
997A: 42                              ;
997B: 61 61           ADC     ($61,X)             ; {ram.0061}
997D: 61 60           ADC     ($60,X)             ; {ram.0060}
997F: 76 76           ROR     <$76,X              ; {ram.0076}
9981: 76 76           ROR     <$76,X              ; {ram.0076}
9983: 17                              ;
9984: 17                              ;
9985: 25 76           AND     <$76                ; {ram.0076}
9987: 17                              ;
9988: 17                              ;
9989: 18              CLC                         ; 
998A: 31 18           AND     ($18),Y             ; {ram.0018}
998C: 18              CLC                         ; 
998D: 18              CLC                         ; 
998E: 25 18           AND     <$18                ; {ram.0018}
9990: 25 18           AND     <$18                ; {ram.0018}
9992: 26 17           ROL     <$17                ; {ram.0017}
9994: 18              CLC                         ; 
9995: 23                              ;
9996: 17                              ;
9997: 30 30           BMI     $99C9               ; {}
9999: 30 30           BMI     $99CB               ; {}
999B: 30 57           BMI     $99F4               ; {}
999D: 29 29           AND     #$29                ; 
999F: 29 29           AND     #$29                ; 
99A1: 29 29           AND     #$29                ; 
99A3: 29 76           AND     #$76                ; 
99A5: 16 16           ASL     $16,X               ; {ram.0016}
99A7: 16 16           ASL     $16,X               ; {ram.0016}
99A9: 16 16           ASL     $16,X               ; {ram.0016}
99AB: 18              CLC                         ; 
99AC: 16 16           ASL     $16,X               ; {ram.0016}
99AE: 16 16           ASL     $16,X               ; {ram.0016}
99B0: 16 16           ASL     $16,X               ; {ram.0016}
99B2: 16 16           ASL     $16,X               ; {ram.0016}
99B4: 18              CLC                         ; 
99B5: 16 16           ASL     $16,X               ; {ram.0016}
99B7: 16 F1           ASL     $F1,X               ; 
99B9: A9 02           LDA     #$02                ; 
99BB: 02                              ;
99BC: 77                              ;
99BD: A2 A3           LDX     #$A3                ; 
99BF: 10 A8           BPL     $9969               ; {}
99C1: F0 F1           BEQ     $99B4               ; {}
99C3: A9 77           LDA     #$77                ; 
99C5: 02                              ;
99C6: A8              TAY                         ; 
99C7: 00              BRK                         ; 
99C8: 15 15           ORA     $15,X               ; {ram.0015}
99CA: 23                              ;
99CB: 23                              ;
99CC: 23                              ;
99CD: 23                              ;
99CE: 23                              ;
99CF: 23                              ;
99D0: 23                              ;
99D1: 23                              ;
99D2: 23                              ;
99D3: 23                              ;
99D4: 23                              ;
99D5: 23                              ;
99D6: 28              PLP                         ; 
99D7: 16 16           ASL     $16,X               ; {ram.0016}
99D9: 16 16           ASL     $16,X               ; {ram.0016}
99DB: 16 16           ASL     $16,X               ; {ram.0016}
99DD: 16 16           ASL     $16,X               ; {ram.0016}
99DF: 16 16           ASL     $16,X               ; {ram.0016}
99E1: 16 18           ASL     $18,X               ; {ram.0018}
99E3: 18              CLC                         ; 
99E4: 16 16           ASL     $16,X               ; {ram.0016}
99E6: 16 16           ASL     $16,X               ; {ram.0016}
99E8: 16 16           ASL     $16,X               ; {ram.0016}
99EA: 16 16           ASL     $16,X               ; {ram.0016}
99EC: 16 19           ASL     $19,X               ; {ram.0019}
99EE: 18              CLC                         ; 
99EF: 76 14           ROR     <$14,X              ; {ram.0014}
99F1: 19 19 19        ORA     $1919,Y             ; 
99F4: 19 19 28        ORA     $2819,Y             ; 
99F7: 28              PLP                         ; 
99F8: 28              PLP                         ; 
99F9: 28              PLP                         ; 
99FA: 17                              ;
99FB: 26 23           ROL     <$23                ; {ram.0023}
99FD: 23                              ;
99FE: 31 18           AND     ($18),Y             ; {ram.0018}
9A00: 18              CLC                         ; 
9A01: 18              CLC                         ; 
9A02: 26 18           ROL     <$18                ; {ram.0018}
9A04: 27                              ;
9A05: 18              CLC                         ; 
9A06: 28              PLP                         ; 
9A07: 16 F0           ASL     $F0,X               ; {ram.00F0}
9A09: F1 A9           SBC     ($A9),Y             ; {ram.00A9}
9A0B: 08              PHP                         ; 
9A0C: 08              PHP                         ; 
9A0D: A4 77           LDY     <$77                ; {ram.0077}
9A0F: 10 A5           BPL     $99B6               ; {}
9A11: 08              PHP                         ; 
9A12: 08              PHP                         ; 
9A13: A4 A5           LDY     <$A5                ; {ram.00A5}
9A15: 08              PHP                         ; 
9A16: A4 02           LDY     <$02                ; {ram.GP_02}
9A18: 02                              ;
9A19: A5 08           LDA     <$08                ; {ram.0008}
9A1B: E3                              ;
9A1C: 18              CLC                         ; 
9A1D: 12                              ;
9A1E: 12                              ;
9A1F: 08              PHP                         ; 
9A20: 08              PHP                         ; 
9A21: 08              PHP                         ; 
9A22: 33                              ;
9A23: 08              PHP                         ; 
9A24: 32                              ;
9A25: 08              PHP                         ; 
9A26: A4 02           LDY     <$02                ; {ram.GP_02}
9A28: 02                              ;
9A29: 02                              ;
9A2A: 02                              ;
9A2B: 33                              ;
9A2C: 33                              ;
9A2D: 33                              ;
9A2E: 33                              ;
9A2F: 10 32           BPL     $9A63               ; {}
9A31: 32                              ;
9A32: 32                              ;
9A33: E8              INX                         ; 
9A34: 07                              ;
9A35: 07                              ;
9A36: A8              TAY                         ; 
9A37: F0 F1           BEQ     $9A2A               ; {}
9A39: A9 02           LDA     #$02                ; 
9A3B: 33                              ;
9A3C: 02                              ;
9A3D: 33                              ;
9A3E: 02                              ;
9A3F: D3                              ;
9A40: 07                              ;
9A41: A8              TAY                         ; 
9A42: A9 02           LDA     #$02                ; 
9A44: 33                              ;
9A45: 02                              ;
9A46: A8              TAY                         ; 
9A47: F0 F1           BEQ     $9A3A               ; {}
9A49: A9 31           LDA     #$31                ; 
9A4B: 18              CLC                         ; 
9A4C: 26 18           ROL     <$18                ; {ram.0018}
9A4E: 27                              ;
9A4F: 18              CLC                         ; 
9A50: 18              CLC                         ; 
9A51: 26 18           ROL     <$18                ; {ram.0018}
9A53: 27                              ;
9A54: 18              CLC                         ; 
9A55: 26 18           ROL     <$18                ; {ram.0018}
9A57: 16 16           ASL     $16,X               ; {ram.0016}
9A59: 28              PLP                         ; 
9A5A: 25 17           AND     <$17                ; {ram.0017}
9A5C: 17                              ;
9A5D: 26 17           ROL     <$17                ; {ram.0017}
9A5F: 23                              ;
9A60: 23                              ;
9A61: 40              RTI                         ; 
9A62: 48              PHA                         ; 
9A63: 48              PHA                         ; 
9A64: 48              PHA                         ; 
9A65: 48              PHA                         ; 
9A66: 48              PHA                         ; 
9A67: 48              PHA                         ; 
9A68: 48              PHA                         ; 
9A69: 48              PHA                         ; 
9A6A: 48              PHA                         ; 
9A6B: 48              PHA                         ; 
9A6C: 48              PHA                         ; 
9A6D: 48              PHA                         ; 
9A6E: 41 23           EOR     ($23,X)             ; {ram.0023}
9A70: 23                              ;
9A71: 23                              ;
9A72: 23                              ;
9A73: 17                              ;
9A74: 31 17           AND     ($17),Y             ; {ram.0017}
9A76: 23                              ;
9A77: 17                              ;
9A78: 17                              ;
9A79: 23                              ;
9A7A: 25 23           AND     <$23                ; {ram.0023}
9A7C: 23                              ;
9A7D: 23                              ;
9A7E: 25 23           AND     <$23                ; {ram.0023}
9A80: 31 23           AND     ($23),Y             ; {ram.0023}
9A82: 26 76           ROL     <$76                ; {ram.0076}
9A84: 18              CLC                         ; 
9A85: 76 28           ROR     <$28,X              ; {ram.0028}
9A87: 16 16           ASL     $16,X               ; {ram.0016}
9A89: 16 16           ASL     $16,X               ; {ram.0016}
9A8B: 16 19           ASL     $19,X               ; {ram.0019}
9A8D: 14                              ;
9A8E: 28              PLP                         ; 
9A8F: 17                              ;
9A90: 17                              ;
9A91: 17                              ;
9A92: 17                              ;
9A93: 17                              ;
9A94: 23                              ;
9A95: 30 30           BMI     $9AC7               ; {}
9A97: 30 30           BMI     $9AC9               ; {}
9A99: 30 17           BMI     $9AB2               ; {}
9A9B: 23                              ;
9A9C: 29 29           AND     #$29                ; 
9A9E: 29 29           AND     #$29                ; 
9AA0: 29 29           AND     #$29                ; 
9AA2: 14                              ;
9AA3: 29 19           AND     #$19                ; 
9AA5: 16 16           ASL     $16,X               ; {ram.0016}
9AA7: 16 16           ASL     $16,X               ; {ram.0016}
9AA9: 28              PLP                         ; 
9AAA: 17                              ;
9AAB: 26 26           ROL     <$26                ; {ram.0026}
9AAD: 26 17           ROL     <$17                ; {ram.0017}
9AAF: 27                              ;
9AB0: 27                              ;
9AB1: 17                              ;
9AB2: 25 25           AND     <$25                ; {ram.0025}
9AB4: 25 25           AND     <$25                ; {ram.0025}
9AB6: 17                              ;
9AB7: 17                              ;
9AB8: A3                              ;
9AB9: 02                              ;
9ABA: 02                              ;
9ABB: 10 A2           BPL     $9A5F               ; {}
9ABD: 18              CLC                         ; 
9ABE: 18              CLC                         ; 
9ABF: 18              CLC                         ; 
9AC0: 18              CLC                         ; 
9AC1: 45 13           EOR     <$13                ; {ram.0013}
9AC3: 13                              ;
9AC4: 13                              ;
9AC5: 13                              ;
9AC6: 13                              ;
9AC7: 13                              ;
9AC8: 00              BRK                         ; 
9AC9: A7                              ;
9ACA: F1 A9           SBC     ($A9),Y             ; {ram.00A9}
9ACC: 02                              ;
9ACD: 64                              ;
9ACE: F2                              ;
9ACF: F3                              ;
9AD0: 64                              ;
9AD1: F2                              ;
9AD2: F3                              ;
9AD3: 10 02           BPL     $9AD7               ; {}
9AD5: 02                              ;
9AD6: 02                              ;
9AD7: 02                              ;
9AD8: 02                              ;
9AD9: 02                              ;
9ADA: 02                              ;
9ADB: A5 A4           LDA     <$A4                ; {ram.00A4}
9ADD: D2                              ;
9ADE: 02                              ;
9ADF: 02                              ;
9AE0: 02                              ;
9AE1: A5 08           LDA     <$08                ; {ram.0008}
9AE3: 08              PHP                         ; 
9AE4: A4 A8           LDY     <$A8                ; {ram.00A8}
9AE6: F0 F1           BEQ     $9AD9               ; {}
9AE8: 16 16           ASL     $16,X               ; {ram.0016}
9AEA: F4                              ;
9AEB: F4                              ;
9AEC: F4                              ;
9AED: F4                              ;
9AEE: 74                              ;
9AEF: 74                              ;
9AF0: 30 30           BMI     $9B22               ; {}
9AF2: 30 30           BMI     $9B24               ; {}
9AF4: 30 30           BMI     $9B26               ; {}
9AF6: 30 30           BMI     $9B28               ; {}
9AF8: 30 30           BMI     $9B2A               ; {}
9AFA: 30 30           BMI     $9B2C               ; {}
9AFC: 30 30           BMI     $9B2E               ; {}
9AFE: 30 23           BMI     $9B23               ; {}
9B00: 23                              ;
9B01: 23                              ;
9B02: 27                              ;
9B03: 23                              ;
9B04: 17                              ;
9B05: 23                              ;
9B06: 28              PLP                         ; 
9B07: 16 F1           ASL     $F1,X               ; 
9B09: A9 02           LDA     #$02                ; 
9B0B: 02                              ;
9B0C: B7                              ;
9B0D: 02                              ;
9B0E: B7                              ;
9B0F: 67                              ;
9B10: F5 70           SBC     $70,X               ; {ram.0070}
9B12: B7                              ;
9B13: 02                              ;
9B14: B7                              ;
9B15: 02                              ;
9B16: A8              TAY                         ; 
9B17: 00              BRK                         ; 
9B18: 00              BRK                         ; 
9B19: A9 10           LDA     #$10                ; 
9B1B: C0 E3           CPY     #$E3                ; 
9B1D: 13                              ;
9B1E: 13                              ;
9B1F: A3                              ;
9B20: 33                              ;
9B21: 02                              ;
9B22: 32                              ;
9B23: 02                              ;
9B24: 33                              ;
9B25: 02                              ;
9B26: 02                              ;
9B27: 02                              ;
9B28: 02                              ;
9B29: 02                              ;
9B2A: 34                              ;
9B2B: 02                              ;
9B2C: 02                              ;
9B2D: 34                              ;
9B2E: D2                              ;
9B2F: 02                              ;
9B30: 33                              ;
9B31: 02                              ;
9B32: 32                              ;
9B33: A5 08           LDA     <$08                ; {ram.0008}
9B35: 08              PHP                         ; 
9B36: F0 A6           BEQ     $9ADE               ; {}
9B38: 01 A7           ORA     ($A7,X)             ; {ram.00A7}
9B3A: 84 90           STY     <$90                ; {ram.0090}
9B3C: 10 02           BPL     $9B40               ; {}
9B3E: A5 08           LDA     <$08                ; {ram.0008}
9B40: 08              PHP                         ; 
9B41: A0 06           LDY     #$06                ; 
9B43: 06 06           ASL     <$06                ; {ram.0006}
9B45: 06 01           ASL     <$01                ; {ram.GP_01}
9B47: 01 A7           ORA     ($A7,X)             ; {ram.00A7}
9B49: F1 25           SBC     ($25),Y             ; {ram.0025}
9B4B: 23                              ;
9B4C: 31 23           AND     ($23),Y             ; {ram.0023}
9B4E: 26 23           ROL     <$23                ; {ram.0023}
9B50: 23                              ;
9B51: 26 23           ROL     <$23                ; {ram.0023}
9B53: 26 23           ROL     <$23                ; {ram.0023}
9B55: 26 23           ROL     <$23                ; {ram.0023}
9B57: 17                              ;
9B58: A3                              ;
9B59: C8              INY                         ; 
9B5A: C7                              ;
9B5B: A0 E7           LDY     #$E7                ; 
9B5D: E6 A2           INC     <$A2                ; {ram.00A2}
9B5F: A3                              ;
9B60: 71 32           ADC     ($32),Y             ; {ram.0032}
9B62: 34                              ;
9B63: 02                              ;
9B64: A8              TAY                         ; 
9B65: A6 01           LDX     <$01                ; {ram.GP_01}
9B67: 01 01           ORA     ($01,X)             ; {ram.GP_01}
9B69: A7                              ;
9B6A: A6 01           LDX     <$01                ; {ram.GP_01}
9B6C: A7                              ;
9B6D: F1 A9           SBC     ($A9),Y             ; {ram.00A9}
9B6F: 39 47 85        AND     $8547,Y             ; {}
9B72: 47                              ;
9B73: 58              CLI                         ; 
9B74: 58              CLI                         ; 
9B75: 58              CLI                         ; 
9B76: 47                              ;
9B77: 47                              ;
9B78: 47                              ;
9B79: 47                              ;
9B7A: 47                              ;
9B7B: 47                              ;
9B7C: 47                              ;
9B7D: 47                              ;
9B7E: 85 47           STA     <$47                ; {ram.0047}
9B80: 47                              ;
9B81: 47                              ;
9B82: 47                              ;
9B83: 47                              ;
9B84: 47                              ;
9B85: 47                              ;
9B86: 47                              ;
9B87: 47                              ;
9B88: 47                              ;
9B89: 47                              ;
9B8A: 91 51           STA     ($51),Y             ; {ram.0051}
9B8C: 97                              ;
9B8D: 91 51           STA     ($51),Y             ; {ram.0051}
9B8F: 51 51           EOR     ($51),Y             ; {ram.0051}
9B91: 97                              ;
9B92: 91 51           STA     ($51),Y             ; {ram.0051}
9B94: 97                              ;
9B95: 91 97           STA     ($97),Y             ; {ram.0097}
9B97: 91 97           STA     ($97),Y             ; {ram.0097}
9B99: 91 51           STA     ($51),Y             ; {ram.0051}
9B9B: 51 97           EOR     ($97),Y             ; {ram.0097}
9B9D: 58              CLI                         ; 
9B9E: 58              CLI                         ; 
9B9F: 58              CLI                         ; 
9BA0: F6 E0           INC     $E0,X               ; {ram.??SND_E0??}
9BA2: 13                              ;
9BA3: 13                              ;
9BA4: 13                              ;
9BA5: 13                              ;
9BA6: 13                              ;
9BA7: 13                              ;
9BA8: 00              BRK                         ; 
9BA9: 00              BRK                         ; 
9BAA: 95 95           STA     $95,X               ; {ram.0095}
9BAC: 95 95           STA     $95,X               ; {ram.0095}
9BAE: 95 C2           STA     $C2,X               ; {ram.00C2}
9BB0: C2                              ;
9BB1: 95 95           STA     $95,X               ; {ram.0095}
9BB3: 95 95           STA     $95,X               ; {ram.0095}
9BB5: 95 00           STA     $00,X               ; {ram.GP_00}
9BB7: 00              BRK                         ; 
9BB8: 00              BRK                         ; 
9BB9: 00              BRK                         ; 
9BBA: 95 95           STA     $95,X               ; {ram.0095}
9BBC: 95 F8           STA     $F8,X               ; {ram.00F8}
9BBE: 95 C2           STA     $C2,X               ; {ram.00C2}
9BC0: F8              SED                         ; 
9BC1: 95 95           STA     $95,X               ; {ram.0095}
9BC3: F8              SED                         ; 
9BC4: 95 95           STA     $95,X               ; {ram.0095}
9BC6: 00              BRK                         ; 
9BC7: 00              BRK                         ; 
9BC8: 00              BRK                         ; 
9BC9: A9 64           LDA     #$64                ; 
9BCB: 66 02           ROR     <$02                ; {ram.GP_02}
9BCD: 53                              ;
9BCE: 54                              ;
9BCF: D1 54           CMP     ($54),Y             ; {ram.0054}
9BD1: 54                              ;
9BD2: 56 02           LSR     $02,X               ; {ram.GP_02}
9BD4: 64                              ;
9BD5: 66 A8           ROR     <$A8                ; {ram.00A8}
9BD7: 00              BRK                         ; 
9BD8: DB                              ;
9BD9: 5B                              ;
9BDA: 5B                              ;
9BDB: DB                              ;
9BDC: 5B                              ;
9BDD: 1B                              ;
9BDE: 0E 1A 5B        ASL     $5B1A               ; 
9BE1: DB                              ;
9BE2: 4E 4E 4E        LSR     $4E4E               ; 
9BE5: 0E 1A 1B        ASL     $1B1A               ; 
9BE8: DB                              ;
9BE9: 4E 32 1B        LSR     $1B32               ; 
9BEC: 34                              ;
9BED: 4E 1A 1B        LSR     $1B1A               ; 
9BF0: DB                              ;
9BF1: 5B                              ;
9BF2: 1B                              ;
9BF3: 4E 4E 4E        LSR     $4E4E               ; 
9BF6: DB                              ;
9BF7: 0E 32 5B        ASL     $5B32               ; 
9BFA: 1B                              ;
9BFB: 4E 1A 1B        LSR     $1B1A               ; 
9BFE: DB                              ;
9BFF: 5B                              ;
9C00: 1B                              ;
9C01: 4E 4E 1A        LSR     $1A4E               ; 
9C04: 1B                              ;
9C05: DB                              ;
9C06: CE 4E 4E        DEC     $4E4E               ; 
9C09: 4E 0E 1A        LSR     $1A0E               ; 
9C0C: 1B                              ;
9C0D: 9B                              ;
9C0E: 0C                              ;
9C0F: 4E 4E 4E        LSR     $4E4E               ; 
9C12: 0E 1A 1B        ASL     $1B1A               ; 
9C15: CA              DEX                         ; 
9C16: 4E 0E 4E        LSR     $4E0E               ; 
9C19: 4E 4A C5        LSR     $C54A               ; 
9C1C: 45 05           EOR     <$05                ; {ram.0005}
9C1E: 0B                              ;
9C1F: C5 45           CMP     <$45                ; {ram.0045}
9C21: 05 45           ORA     <$45                ; {ram.0045}
9C23: 45 45           EOR     <$45                ; {ram.0045}
9C25: D9 28 59        CMP     $5928,Y             ; 
9C28: D9 59 59        CMP     $5959,Y             ; 
9C2B: 19 D9 59        ORA     $59D9,Y             ; 
9C2E: 4E 0E 59        LSR     $590E               ; 
9C31: D9 4E 4E        CMP     $4E4E,Y             ; 
9C34: 4E 0E 59        LSR     $590E               ; 
9C37: 8E 4E 4E        STX     $4E4E               ; 
9C3A: CE 4E 4E        DEC     $4E4E               ; 
9C3D: 0E D9 59        ASL     $59D9               ; 
9C40: 0E 4E 4E        ASL     $4E4E               ; 
9C43: 4E DB 0E        LSR     $0EDB               ; 
9C46: 5B                              ;
9C47: 5B                              ;
9C48: 4E 1A 1B        LSR     $1B1A               ; 
9C4B: DB                              ;
9C4C: 0E 33 5B        ASL     $5B33               ; 
9C4F: 1B                              ;
9C50: 4E 1A 1B        LSR     $1B1A               ; 
9C53: CE 4E 4E        DEC     $4E4E               ; 
9C56: 4E 0E 59        LSR     $590E               ; 
9C59: DB                              ;
9C5A: 4E 33 1B        LSR     $1B33               ; 
9C5D: 35 4E           AND     $4E,X               ; {ram.004E}
9C5F: 1A                              ;
9C60: 1B                              ;
9C61: D9 4E 19        CMP     $194E,Y             ; 
9C64: 0E 19 4E        ASL     $4E19               ; 
9C67: D9 0E 19        CMP     $190E,Y             ; 
9C6A: 0E 19 0E        ASL     $0E19               ; 
9C6D: 19 0E D9        ORA     $D90E,Y             ; 
9C70: 4E 0E 19        LSR     $190E               ; 
9C73: 0E 4E D9        ASL     $D94E               ; 
9C76: 19 4E 4E        ORA     $4E4E,Y             ; 
9C79: 0E 19 D9        ASL     $D919               ; 
9C7C: 0E 59 59        ASL     $5959               ; 
9C7F: 59 D9 0E        EOR     $0ED9,Y             ; 
9C82: 59 59 19        EOR     $1959,Y             ; 
9C85: 0E D9 4E        ASL     $4ED9               ; 
9C88: 19 0E 28        ORA     $280E,Y             ; 
9C8B: 4E 59 DB        LSR     $DB59               ; 
9C8E: 4E 13 0E        LSR     $0E13               ; 
9C91: 13                              ;
9C92: 4E 1A 1B        LSR     $1B1A               ; 
9C95: DB                              ;
9C96: 0E 13 0E        ASL     $0E13               ; 
9C99: 13                              ;
9C9A: 0E 13 0E        ASL     $0E13               ; 
9C9D: 1A                              ;
9C9E: 1B                              ;
9C9F: DB                              ;
9CA0: 4E 0E 13        LSR     $130E               ; 
9CA3: 4E 0E 1A        LSR     $1A0E               ; 
9CA6: 1B                              ;
9CA7: C8              INY                         ; 
9CA8: 48              PHA                         ; 
9CA9: 17                              ;
9CAA: 4E 4E 1A        LSR     $1A4E               ; 
9CAD: 1B                              ;
9CAE: C5 45           CMP     <$45                ; {ram.0045}
9CB0: 07                              ;
9CB1: 4E 4E 1A        LSR     $1A4E               ; 
9CB4: 1B                              ;
9CB5: C5 45           CMP     <$45                ; {ram.0045}
9CB7: 07                              ;
9CB8: 0E 1A DB        ASL     $DB1A               ; 
9CBB: 5B                              ;
9CBC: 1B                              ;
9CBD: 4E 4E 4A        LSR     $4A4E               ; 
9CC0: DB                              ;
9CC1: 4E 4E 15        LSR     $154E               ; 
9CC4: C8              INY                         ; 
9CC5: 48              PHA                         ; 
9CC6: 17                              ;
9CC7: 4E 4E 59        LSR     $594E               ; 
9CCA: C9 49           CMP     #$49                ; 
9CCC: 18              CLC                         ; 
9CCD: 4E 4E D9        LSR     $D94E               ; 
9CD0: 59 4E 06        EOR     $064E,Y             ; {ram.064E}
9CD3: C5 45           CMP     <$45                ; {ram.0045}
9CD5: 45 C9           EOR     <$C9                ; {ram.00C9}
9CD7: 49 09           EOR     #$09                ; 
9CD9: 0B                              ;
9CDA: 49 49           EOR     #$49                ; 
9CDC: 09 C8           ORA     #$C8                ; 
9CDE: 48              PHA                         ; 
9CDF: 08              PHP                         ; 
9CE0: 48              PHA                         ; 
9CE1: C8              INY                         ; 
9CE2: 48              PHA                         ; 
9CE3: 17                              ;
9CE4: 4E 4E 4E        LSR     $4E4E               ; 
9CE7: DB                              ;
9CE8: 4E 4E 06        LSR     $064E               ; {ram.064E}
9CEB: C5 45           CMP     <$45                ; {ram.0045}
9CED: 07                              ;
9CEE: 4E 4E D9        LSR     $D94E               ; 
9CF1: 4E 2C 4E        LSR     $4E2C               ; 
9CF4: 4E 59 DB        LSR     $DB59               ; 
9CF7: 5B                              ;
9CF8: 1B                              ;
9CF9: 0E 4A 4A        ASL     $4A4A               ; 
9CFC: 0A              ASL     A                   ; 
9CFD: DB                              ;
9CFE: 5B                              ;
9CFF: 4E 06 C5        LSR     $C506               ; 
9D02: 45 07           EOR     <$07                ; {ram.0007}
9D04: 4E 4E 4E        LSR     $4E4E               ; 
9D07: DB                              ;
9D08: 0E 15 48        ASL     $4815               ; 
9D0B: 17                              ;
9D0C: 4E 1A 1B        LSR     $1B1A               ; 
9D0F: DB                              ;
9D10: 0E 06 45        ASL     $4506               ; 
9D13: 07                              ;
9D14: 4E 1A 1B        LSR     $1B1A               ; 
9D17: DB                              ;
9D18: 0E 06 05        ASL     $0506               ; {ram.0506}
9D1B: 45 45           EOR     <$45                ; {ram.0045}
9D1D: 45 DB           EOR     <$DB                ; {ram.00DB}
9D1F: 0E 16 49        ASL     $4916               ; 
9D22: 18              CLC                         ; 
9D23: 4E 1A 1B        LSR     $1B1A               ; 
9D26: D9 0E 59        CMP     $590E,Y             ; 
9D29: 59 19 0E        EOR     $0E19,Y             ; 
9D2C: CE 4E 4E        DEC     $4E4E               ; 
9D2F: 06 45           ASL     <$45                ; {ram.0045}
9D31: 45 D9           EOR     <$D9                ; {ram.00D9}
9D33: 4E 4E 16        LSR     $164E               ; 
9D36: 49 49           EOR     #$49                ; 
9D38: D9 4E 4E        CMP     $4E4E,Y             ; 
9D3B: 06 C5           ASL     <$C5                ; {ram.00C5}
9D3D: 45 07           EOR     <$07                ; {ram.0007}
9D3F: 4E D9 59        LSR     $59D9               ; 
9D42: 4E 15 48        LSR     $4815               ; 
9D45: 48              PHA                         ; 
9D46: DB                              ;
9D47: 0E 1C 1F        ASL     $1F1C               ; 
9D4A: 4E 4E 1A        LSR     $1A4E               ; 
9D4D: 1B                              ;
9D4E: DB                              ;
9D4F: 0E 1D 0C        ASL     $0C1D               ; 
9D52: 4E 4E 1A        LSR     $1A4E               ; 
9D55: 1B                              ;
9D56: DB                              ;
9D57: 0E 1E 20        ASL     $201E               ; 
9D5A: 4E 4E 1A        LSR     $1A4E               ; 
9D5D: 1B                              ;
9D5E: DB                              ;
9D5F: 0E 21 24        ASL     $2421               ; 
9D62: 4E 4E 1A        LSR     $1A4E               ; 
9D65: 1B                              ;
9D66: DB                              ;
9D67: 0E 22 0C        ASL     $0C22               ; 
9D6A: 4E 4E 4A        LSR     $4A4E               ; 
9D6D: DB                              ;
9D6E: 0E 23 25        ASL     $2523               ; 
9D71: 4E 4E 1A        LSR     $1A4E               ; 
9D74: 1B                              ;
9D75: DB                              ;
9D76: 4E 0E 26        LSR     $260E               ; 
9D79: 4E 0E 1A        LSR     $1A0E               ; 
9D7C: 1B                              ;
9D7D: DB                              ;
9D7E: 5B                              ;
9D7F: 07                              ;
9D80: 4E 1A 1B        LSR     $1B1A               ; 
9D83: DB                              ;
9D84: 5B                              ;
9D85: 07                              ;
9D86: 4E 4E 1A        LSR     $1A4E               ; 
9D89: 1B                              ;
9D8A: CE 0E 59        DEC     $590E               ; 
9D8D: 59 19 0E        EOR     $0E19,Y             ; 
9D90: D9 4E 0E        CMP     $0E4E,Y             ; 
9D93: 26 4E           ROL     <$4E                ; {ram.004E}
9D95: 0E D9 4E        ASL     $4ED9               ; 
9D98: 4E 4E 4E        LSR     $4E4E               ; 
9D9B: 0E DB 4E        ASL     $4EDB               ; 
9D9E: 19 0E 19        ORA     $190E,Y             ; 
9DA1: 4E 1A 1B        LSR     $1B1A               ; 
9DA4: DB                              ;
9DA5: 5B                              ;
9DA6: 5B                              ;
9DA7: 45 C5           EOR     <$C5                ; {ram.00C5}
9DA9: 05 5B           ORA     <$5B                ; {ram.005B}
9DAB: 5B                              ;
9DAC: DB                              ;
9DAD: 5B                              ;
9DAE: 27                              ;
9DAF: 0E 1A 5B        ASL     $5B1A               ; 
9DB2: DB                              ;
9DB3: 0E 14 0E        ASL     $0E14               ; 
9DB6: 14                              ;
9DB7: 0E 14 4E        ASL     $4E14               ; 
9DBA: 0E CA 4A        ASL     $4ACA               ; 
9DBD: 0A              ASL     A                   ; 
9DBE: 4E 4E 1A        LSR     $1A4E               ; 
9DC1: 1B                              ;
9DC2: DB                              ;
9DC3: 1B                              ;
9DC4: 35 4E           AND     $4E,X               ; {ram.004E}
9DC6: 4E 0E 1A        LSR     $1A0E               ; 
9DC9: 1B                              ;
9DCA: 9B                              ;
9DCB: 27                              ;
9DCC: 4E 4E 06        LSR     $064E               ; {ram.064E}
9DCF: C5 45           CMP     <$45                ; {ram.0045}
9DD1: 05 2F           ORA     <$2F                ; {ram.002F}
9DD3: 4E 4E 0E        LSR     $0E4E               ; 
9DD6: DB                              ;
9DD7: 0E 22 0C        ASL     $0C22               ; 
9DDA: 4E 4E 4A        LSR     $4A4E               ; 
9DDD: DB                              ;
9DDE: 0E 14 0E        ASL     $0E14               ; 
9DE1: 29 0E           AND     #$0E                ; 
9DE3: 14                              ;
9DE4: 4E 0E DB        LSR     $DB0E               ; 
9DE7: 35 4E           AND     $4E,X               ; {ram.004E}
9DE9: 4E 4E 1A        LSR     $1A4E               ; 
9DEC: 1B                              ;
9DED: DB                              ;
9DEE: 1B                              ;
9DEF: 34                              ;
9DF0: 4E 06 C5        LSR     $C506               ; 
9DF3: 45 05           EOR     <$05                ; {ram.0005}
9DF5: 2E 4E 4E        ROL     $4E4E               ; 
9DF8: 0E CE 0E        ASL     $0ECE               ; 
9DFB: 14                              ;
9DFC: 0E 14 0E        ASL     $0E14               ; 
9DFF: 14                              ;
9E00: 0E 1A 1B        ASL     $1B1A               ; 
9E03: CE 0E 14        DEC     $140E               ; 
9E06: 0E 14 0E        ASL     $0E14               ; 
9E09: 14                              ;
9E0A: 4E 0E DB        LSR     $DB0E               ; 
9E0D: 4D 4D 4D        EOR     $4D4D               ; 
9E10: 0D 1A 1B        ORA     $1B1A               ; 
9E13: C5 05           CMP     <$05                ; {ram.0005}
9E15: 1B                              ;
9E16: 0C                              ;
9E17: 4E 0E 4A        LSR     $4A0E               ; 
9E1A: 0A              ASL     A                   ; 
9E1B: DB                              ;
9E1C: 1B                              ;
9E1D: 35 4E           AND     $4E,X               ; {ram.004E}
9E1F: 06 45           ASL     <$45                ; {ram.0045}
9E21: C5 4E           CMP     <$4E                ; {ram.004E}
9E23: 4E 4E 0E        LSR     $0E4E               ; 
9E26: 45 DB           EOR     <$DB                ; {ram.00DB}
9E28: 5B                              ;
9E29: 34                              ;
9E2A: 4E 4E 1A        LSR     $1A4E               ; 
9E2D: 1B                              ;
9E2E: DB                              ;
9E2F: 5B                              ;
9E30: 35 4E           AND     $4E,X               ; {ram.004E}
9E32: 4E 1A 1B        LSR     $1B1A               ; 
9E35: 9B                              ;
9E36: 35 4E           AND     $4E,X               ; {ram.004E}
9E38: 4E 4E 0E        LSR     $0E4E               ; 
9E3B: 33                              ;
9E3C: 1B                              ;
9E3D: 9B                              ;
9E3E: 34                              ;
9E3F: 4E 4E 4E        LSR     $4E4E               ; 
9E42: 0E 32 1B        ASL     $1B32               ; 
9E45: 9B                              ;
9E46: 34                              ;
9E47: 4E 4E 4E        LSR     $4E4E               ; 
9E4A: 0E 1A 1B        ASL     $1B1A               ; 
9E4D: 9B                              ;
9E4E: 35 4E           AND     $4E,X               ; {ram.004E}
9E50: 4E 4E 0E        LSR     $0E4E               ; 
9E53: 1A                              ;
9E54: 1B                              ;
9E55: DB                              ;
9E56: 5B                              ;
9E57: 34                              ;
9E58: 0E 32 DB        ASL     $DB32               ; 
9E5B: 5B                              ;
9E5C: 35 0E           AND     $0E,X               ; {ram.000E}
9E5E: 33                              ;
9E5F: 5B                              ;
9E60: DB                              ;
9E61: 34                              ;
9E62: 4E 4E 0E        LSR     $0E4E               ; 
9E65: 32                              ;
9E66: DB                              ;
9E67: 35 4E           AND     $4E,X               ; {ram.004E}
9E69: 4E 0E 33        LSR     $330E               ; 
9E6C: DB                              ;
9E6D: 5B                              ;
9E6E: 07                              ;
9E6F: 4E 4E 4E        LSR     $4E4E               ; 
9E72: DB                              ;
9E73: 0E 06 05        ASL     $0506               ; {ram.0506}
9E76: 45 2F           EOR     <$2F                ; {ram.002F}
9E78: 0E 1A 1B        ASL     $1B1A               ; 
9E7B: DB                              ;
9E7C: 0E 06 05        ASL     $0506               ; {ram.0506}
9E7F: 45 2E           EOR     <$2E                ; {ram.002E}
9E81: 0E 1A 1B        ASL     $1B1A               ; 
9E84: CA              DEX                         ; 
9E85: 4A              LSR     A                   ; 
9E86: 0A              ASL     A                   ; 
9E87: 0E 1A DB        ASL     $DB1A               ; 
9E8A: 5B                              ;
9E8B: 15 45           ORA     $45,X               ; {ram.0045}
9E8D: 45 45           EOR     <$45                ; {ram.0045}
9E8F: DB                              ;
9E90: 4E 4E 4E        LSR     $4E4E               ; 
9E93: 0E CA 4E        ASL     $4ECA               ; 
9E96: 4E 4E 0E        LSR     $0E4E               ; 
9E99: 1A                              ;
9E9A: 1B                              ;
9E9B: DB                              ;
9E9C: 4E 2C 0E        LSR     $0E2C               ; 
9E9F: 2C 4E 1A        BIT     $1A4E               ; 
9EA2: 1B                              ;
9EA3: CA              DEX                         ; 
9EA4: 4A              LSR     A                   ; 
9EA5: 4E 06 45        LSR     $4506               ; 
9EA8: 45 9B           EOR     <$9B                ; {ram.009B}
9EAA: 35 4E           AND     $4E,X               ; {ram.004E}
9EAC: 0E 13 4E        ASL     $4E13               ; 
9EAF: 0E 1A 1B        ASL     $1B1A               ; 
9EB2: F6 76           INC     $76,X               ; {ram.0076}
9EB4: 0F                              ;
9EB5: 4E 1A 1B        LSR     $1B1A               ; 
9EB8: 5B                              ;
9EB9: DB                              ;
9EBA: 4D 4D 4D        EOR     $4D4D               ; 
9EBD: 4D 0D CE        EOR     $CE0D               ; 
9EC0: 4E 0E 30        LSR     $300E               ; 
9EC3: 45 45           EOR     <$45                ; {ram.0045}
9EC5: 05 DB           ORA     <$DB                ; {ram.00DB}
9EC7: F7                              ;
9EC8: F7                              ;
9EC9: 77                              ;
9ECA: 77                              ;
9ECB: 37                              ;
9ECC: 77                              ;
9ECD: 1A                              ;
9ECE: 1B                              ;
9ECF: DB                              ;
9ED0: 1B                              ;
9ED1: 34                              ;
9ED2: 4E 4E 0E        LSR     $0E4E               ; 
9ED5: 1A                              ;
9ED6: 1B                              ;
9ED7: DB                              ;
9ED8: 34                              ;
9ED9: 0E 4E 4E        ASL     $4E4E               ; 
9EDC: 0E 1A 1B        ASL     $1B1A               ; 
9EDF: C5 45           CMP     <$45                ; {ram.0045}
9EE1: 0B                              ;
9EE2: 4E 4E 4E        LSR     $4E4E               ; 
9EE5: DB                              ;
9EE6: 0E 06 45        ASL     $4506               ; 
9EE9: 07                              ;
9EEA: 4E 4E 9B        LSR     $9B4E               ; {}
9EED: 27                              ;
9EEE: 4E 4E 4E        LSR     $4E4E               ; 
9EF1: 0E 1A 1B        ASL     $1B1A               ; 
9EF4: 9B                              ;
9EF5: 27                              ;
9EF6: 4E 4E 4E        LSR     $4E4E               ; 
9EF9: 4E 0E DB        LSR     $DB0E               ; 
9EFC: 1B                              ;
9EFD: 27                              ;
9EFE: 07                              ;
9EFF: 4E 1A 5B        LSR     $5B1A               ; 
9F02: 1B                              ;
9F03: CE 4E 4E        DEC     $4E4E               ; 
9F06: 4E 33 5B        LSR     $5B33               ; 
9F09: DB                              ;
9F0A: 5B                              ;
9F0B: 1B                              ;
9F0C: 0E 15 48        ASL     $4815               ; 
9F0F: 48              PHA                         ; 
9F10: DB                              ;
9F11: 0E 2D 0C        ASL     $0C2D               ; 
9F14: 4E 4E 4A        LSR     $4A4E               ; 
9F17: DB                              ;
9F18: 0E 1C 1F        ASL     $1F1C               ; 
9F1B: 0E 1E 20        ASL     $201E               ; 
9F1E: 0E 1A 1B        ASL     $1B1A               ; 
9F21: C8              INY                         ; 
9F22: 48              PHA                         ; 
9F23: 08              PHP                         ; 
9F24: C5 45           CMP     <$45                ; {ram.0045}
9F26: 45 08           EOR     <$08                ; {ram.0008}
9F28: 48              PHA                         ; 
9F29: 48              PHA                         ; 
9F2A: DB                              ;
9F2B: 35 CE           AND     $CE,X               ; {ram.00CE}
9F2D: 4E 4E 4E        LSR     $4E4E               ; 
9F30: 0E 33 1B        ASL     $1B33               ; 
9F33: DB                              ;
9F34: 0E 33 5B        ASL     $5B33               ; 
9F37: 27                              ;
9F38: 4E 1A 1B        LSR     $1B1A               ; 
9F3B: DB                              ;
9F3C: 4E 4E 1C        LSR     $1C4E               ; 
9F3F: 1F                              ;
9F40: 0E 1A 1B        ASL     $1B1A               ; 
9F43: DB                              ;
9F44: 5B                              ;
9F45: 1B                              ;
9F46: 35 4E           AND     $4E,X               ; {ram.004E}
9F48: 33                              ;
9F49: DB                              ;
9F4A: 5B                              ;
9F4B: 1B                              ;
9F4C: 34                              ;
9F4D: 4E 32 DB        LSR     $DB32               ; 
9F50: 4E 4E 4E        LSR     $4E4E               ; 
9F53: 0E 33 9B        ASL     $9B33               ; {}
9F56: 5B                              ;
9F57: 34                              ;
9F58: 4E 0E 32        LSR     $320E               ; 
9F5B: DB                              ;
9F5C: 1B                              ;
9F5D: 35 4E           AND     $4E,X               ; {ram.004E}
9F5F: 0E 33 1B        ASL     $1B33               ; 
9F62: DB                              ;
9F63: 0E 1E 20        ASL     $201E               ; 
9F66: 0E 1C 1F        ASL     $1F1C               ; 
9F69: 0E 1A 1B        ASL     $1B1A               ; 
9F6C: DB                              ;
9F6D: 4E 4E 1E        LSR     $1E4E               ; 
9F70: 20 0E 1A        JSR     $1A0E               ; 
9F73: 1B                              ;
9F74: D9 59 19        CMP     $1959,Y             ; 
9F77: 4E 4E 59        LSR     $594E               ; 
9F7A: DB                              ;
9F7B: 0E 2D 0C        ASL     $0C2D               ; 
9F7E: 4E 4E 1A        LSR     $1A4E               ; 
9F81: 1B                              ;
9F82: CE 4E 0E        DEC     $0E4E               ; 
9F85: 31 05           AND     ($05),Y             ; {ram.0005}
9F87: C5 45           CMP     <$45                ; {ram.0045}
9F89: 07                              ;
9F8A: 4E 28 59        LSR     $5928               ; 
9F8D: 19 DB 4D        ORA     $4DDB,Y             ; 
9F90: 4D 12 4D        EOR     $4D12               ; 
9F93: 1A                              ;
9F94: 1B                              ;
9F95: DB                              ;
9F96: 77                              ;
9F97: 77                              ;
9F98: 77                              ;
9F99: 37                              ;
9F9A: 1A                              ;
9F9B: 1B                              ;
9F9C: 18              CLC                         ; 
9F9D: 94 D8           STY     $D8,X               ; {ram.00D8}
9F9F: 9B                              ;
9FA0: E0 F5           CPX     #$F5                ; 
9FA2: F5 F5           SBC     $F5,X               ; {ram.TileFlagA}
9FA4: F5 B8           SBC     $B8,X               ; 
9FA6: F5 D4           SBC     $D4,X               ; {ram.00D4}
9FA8: F5 F5           SBC     $F5,X               ; {ram.TileFlagA}
9FAA: F5 C4           SBC     $C4,X               ; {ram.00C4}
9FAC: DE DE BC        DEC     $BCDE,X             ; {}
9FAF: C8              INY                         ; 
9FB0: DE BC DE        DEC     $DEBC,X             ; 
9FB3: DE F5 DC        DEC     $DCF5,X             ; 
9FB6: C4 DE           CPY     <$DE                ; {ram.00DE}
9FB8: C8              INY                         ; 
9FB9: DE BC C8        DEC     $C8BC,X             ; 
9FBC: DE DE F5        DEC     $F5DE,X             ; 
9FBF: DC                              ;
9FC0: DC                              ;
9FC1: 00              BRK                         ; 
9FC2: C0 D0           CPY     #$D0                ; 
9FC4: DC                              ;
9FC5: 00              BRK                         ; 
9FC6: F5 DC           SBC     $DC,X               ; 
9FC8: CC 00 F5        CPY     $F500               ; 
9FCB: DC                              ;
9FCC: DC                              ;
9FCD: 00              BRK                         ; 
9FCE: F5 CC           SBC     $CC,X               ; {ram.00CC}
9FD0: D0 00           BNE     $9FD2               ; {}
9FD2: F5 DC           SBC     $DC,X               ; 
9FD4: DC                              ;
9FD5: 00              BRK                         ; 
9FD6: C0 D0           CPY     #$D0                ; 
9FD8: DC                              ;
9FD9: 00              BRK                         ; 
9FDA: F5 DC           SBC     $DC,X               ; 
9FDC: CC 00 F5        CPY     $F500               ; 
9FDF: DC                              ;
9FE0: DC                              ;
9FE1: 00              BRK                         ; 
9FE2: D8              CLD                         ; 
9FE3: CC D0 00        CPY     $00D0               ; {ram.00D0}
9FE6: F5 DC           SBC     $DC,X               ; 
9FE8: DC                              ;
9FE9: 00              BRK                         ; 
9FEA: F5 DC           SBC     $DC,X               ; 
9FEC: DC                              ;
9FED: 00              BRK                         ; 
9FEE: 88              DEY                         ; 
9FEF: 74                              ;
9FF0: 8A              TXA                         ; 
9FF1: 24 87           BIT     <$87                ; {ram.0087}
9FF3: 87                              ;
9FF4: 75 89           ADC     <$89,X              ; {ram.0089}
9FF6: 24 8B           BIT     <$8B                ; {ram.008B}
9FF8: 87                              ;
9FF9: 87                              ;
9FFA: 88              DEY                         ; 
9FFB: A4 8A           LDY     <$8A                ; {ram.008A}
9FFD: A6 87           LDX     <$87                ; {ram.0087}
9FFF: 87                              ;
A000: A5 89           LDA     <$89                ; {ram.0089}
A002: A7                              ;
A003: 8B                              ;
A004: 87                              ;
A005: 87                              ;
A006: 88              DEY                         ; 
A007: AC 8A AE        LDY     $AE8A               ; {}
A00A: 87                              ;
A00B: 87                              ;
A00C: AD 89 AF        LDA     $AF89               ; {}
A00F: 8B                              ;
A010: 87                              ;
A011: 87                              ;
A012: DF                              ;
A013: DF                              ;
A014: DF                              ;
A015: DF                              ;
A016: F5 F5           SBC     $F5,X               ; {ram.TileFlagA}
A018: DF                              ;
A019: DF                              ;
A01A: DF                              ;
A01B: DF                              ;
A01C: F5 F5           SBC     $F5,X               ; {ram.TileFlagA}
A01E: DF                              ;
A01F: 24 DF           BIT     <$DF                ; {ram.00DF}
A021: 92                              ;
A022: F5 F5           SBC     $F5,X               ; {ram.TileFlagA}
A024: 24 DF           BIT     <$DF                ; {ram.00DF}
A026: 93                              ;
A027: DF                              ;
A028: F5 F5           SBC     $F5,X               ; {ram.TileFlagA}
A02A: 82                              ;
A02B: 82                              ;
A02C: 83                              ;
A02D: 24 85           BIT     <$85                ; {ram.0085}
A02F: 76 82           ROR     <$82,X              ; {ram.0082}
A031: 82                              ;
A032: 24 84           BIT     <$84                ; {ram.0084}
A034: 77                              ;
A035: 86 82           STX     <$82                ; {ram.0082}
A037: 82                              ;
A038: 83                              ;
A039: A0 85           LDY     #$85                ; 
A03B: A2 82           LDX     #$82                ; 
A03D: 82                              ;
A03E: A1 84           LDA     ($84,X)             ; {ram.0084}
A040: A3                              ;
A041: 86 82           STX     <$82                ; {ram.0082}
A043: 82                              ;
A044: 83                              ;
A045: AC 85 AE        LDY     $AE85               ; {}
A048: 82                              ;
A049: 82                              ;
A04A: AD 84 AF        LDA     $AF84               ; {}
A04D: 86 F5           STX     <$F5                ; {ram.TileFlagA}
A04F: F5 DE           SBC     $DE,X               ; {ram.00DE}
A051: DE DE DE        DEC     $DEDE,X             ; 
A054: F5 F5           SBC     $F5,X               ; {ram.TileFlagA}
A056: DE DE DE        DEC     $DEDE,X             ; 
A059: DE F5 F5        DEC     $F5F5,X             ; 
A05C: DE 90 DE        DEC     $DE90,X             ; 
A05F: 24 F5           BIT     <$F5                ; {ram.TileFlagA}
A061: F5 91           SBC     $91,X               ; {ram.0091}
A063: DE 24 DE        DEC     $DE24,X             ; 
A066: 7E 7F 7D        ROR     $7D7F,X             ; 
A069: 76 24           ROR     <$24,X              ; {ram.0024}
A06B: 7D 74 24        ADC     $2474,X             ; 
A06E: 7D 80 81        ADC     $8180,X             ; {}
A071: 7D 7E 7F        ADC     $7F7E,X             ; 
A074: 7D 9C 9D        ADC     $9D9C,X             ; {}
A077: 7D 9E 9F        ADC     $9F9E,X             ; {}
A07A: 7D 80 81        ADC     $8180,X             ; {}
A07D: 7D 7E 7F        ADC     $7F7E,X             ; 
A080: 7D A8 A9        ADC     $A9A8,X             ; {}
A083: 7D AA AB        ADC     $ABAA,X             ; {}
A086: 7D 80 81        ADC     $8180,X             ; {}
A089: 7D DD DD        ADC     $DDDD,X             ; 
A08C: F5 DD           SBC     $DD,X               ; 
A08E: DD F5 DD        CMP     $DDF5,X             ; 
A091: DD F5 DD        CMP     $DDF5,X             ; 
A094: DD F5 DD        CMP     $DDF5,X             ; 
A097: DD F5 24        CMP     $24F5,X             ; 
A09A: 8E F5 24        STX     $24F5               ; 
A09D: 8F                              ;
A09E: F5 DD           SBC     $DD,X               ; 
A0A0: DD F5 78        CMP     $78F5,X             ; 
A0A3: 79 7A 78        ADC     $787A,Y             ; 
A0A6: 24 77           BIT     <$77                ; {ram.0077}
A0A8: 78              SEI                         ; 
A0A9: 24 75           BIT     <$75                ; {ram.0075}
A0AB: 78              SEI                         ; 
A0AC: 7B                              ;
A0AD: 7C                              ;
A0AE: 78              SEI                         ; 
A0AF: 79 7A 78        ADC     $787A,Y             ; 
A0B2: 98              TYA                         ; 
A0B3: 99 78 9A        STA     $9A78,Y             ; {}
A0B6: 9B                              ;
A0B7: 78              SEI                         ; 
A0B8: 7B                              ;
A0B9: 7C                              ;
A0BA: 78              SEI                         ; 
A0BB: 79 7A 78        ADC     $787A,Y             ; 
A0BE: A8              TAY                         ; 
A0BF: A9 78           LDA     #$78                ; 
A0C1: AA              TAX                         ; 
A0C2: AB                              ;
A0C3: 78              SEI                         ; 
A0C4: 7B                              ;
A0C5: 7C                              ;
A0C6: F5 DC           SBC     $DC,X               ; 
A0C8: DC                              ;
A0C9: F5 DC           SBC     $DC,X               ; 
A0CB: DC                              ;
A0CC: F5 DC           SBC     $DC,X               ; 
A0CE: DC                              ;
A0CF: F5 DC           SBC     $DC,X               ; 
A0D1: DC                              ;
A0D2: F5 DC           SBC     $DC,X               ; 
A0D4: DC                              ;
A0D5: F5 8C           SBC     $8C,X               ; {ram.008C}
A0D7: 24 F5           BIT     <$F5                ; {ram.TileFlagA}
A0D9: 8D 24 F5        STA     $F524               ; 
A0DC: DC                              ;
A0DD: DC                              ;
A0DE: 00              BRK                         ; 
A0DF: 00              BRK                         ; 
A0E0: 00              BRK                         ; 
A0E1: 00              BRK                         ; 
A0E2: 00              BRK                         ; 
A0E3: 00              BRK                         ; 
A0E4: 00              BRK                         ; 
A0E5: 00              BRK                         ; 
A0E6: 00              BRK                         ; 
A0E7: 00              BRK                         ; 
A0E8: 00              BRK                         ; 
A0E9: 00              BRK                         ; 
A0EA: 00              BRK                         ; 
A0EB: 31 23           AND     ($23),Y             ; {ram.0023}
A0ED: 00              BRK                         ; 
A0EE: 00              BRK                         ; 
A0EF: 00              BRK                         ; 
A0F0: 00              BRK                         ; 
A0F1: 00              BRK                         ; 
A0F2: 00              BRK                         ; 
A0F3: 23                              ;
A0F4: 31 00           AND     ($00),Y             ; {ram.GP_00}
A0F6: 00              BRK                         ; 
A0F7: 00              BRK                         ; 
A0F8: 23                              ;
A0F9: 00              BRK                         ; 
A0FA: 00              BRK                         ; 
A0FB: 00              BRK                         ; 
A0FC: 00              BRK                         ; 
A0FD: 00              BRK                         ; 
A0FE: 00              BRK                         ; 
A0FF: 23                              ;
A100: 00              BRK                         ; 
A101: 00              BRK                         ; 
A102: 00              BRK                         ; 
A103: 00              BRK                         ; 
A104: 12                              ;
A105: 00              BRK                         ; 
A106: 00              BRK                         ; 
A107: 00              BRK                         ; 
A108: 00              BRK                         ; 
A109: 00              BRK                         ; 
A10A: 00              BRK                         ; 
A10B: 12                              ;
A10C: 00              BRK                         ; 
A10D: 00              BRK                         ; 
A10E: 00              BRK                         ; 
A10F: 00              BRK                         ; 
A110: 00              BRK                         ; 
A111: 00              BRK                         ; 
A112: 00              BRK                         ; 
A113: 00              BRK                         ; 
A114: 00              BRK                         ; 
A115: 01 01           ORA     ($01,X)             ; {ram.GP_01}
A117: 06 04           ASL     <$04                ; {ram.0004}
A119: 04                              ;
A11A: 05 05           ORA     <$05                ; {ram.0005}
A11C: 07                              ;
A11D: 16 17           ASL     $17,X               ; {ram.0017}
A11F: 00              BRK                         ; 
A120: 00              BRK                         ; 
A121: 17                              ;
A122: 16 07           ASL     $07,X               ; {ram.0007}
A124: 05 05           ORA     <$05                ; {ram.0005}
A126: 72                              ;
A127: 31 00           AND     ($00),Y             ; {ram.GP_00}
A129: 02                              ;
A12A: 00              BRK                         ; 
A12B: 00              BRK                         ; 
A12C: 00              BRK                         ; 
A12D: 00              BRK                         ; 
A12E: 02                              ;
A12F: 00              BRK                         ; 
A130: 31 53           AND     ($53),Y             ; {ram.0053}
A132: 00              BRK                         ; 
A133: 11 11           ORA     ($11),Y             ; {ram.0011}
A135: 11 11           ORA     ($11),Y             ; {ram.0011}
A137: 11 11           ORA     ($11),Y             ; {ram.0011}
A139: 11 11           ORA     ($11),Y             ; {ram.0011}
A13B: 11 11           ORA     ($11),Y             ; {ram.0011}
A13D: 00              BRK                         ; 
A13E: 00              BRK                         ; 
A13F: 12                              ;
A140: 12                              ;
A141: 12                              ;
A142: 12                              ;
A143: 12                              ;
A144: 12                              ;
A145: 12                              ;
A146: 12                              ;
A147: 12                              ;
A148: 13                              ;
A149: 00              BRK                         ; 
A14A: 00              BRK                         ; 
A14B: 00              BRK                         ; 
A14C: 13                              ;
A14D: 12                              ;
A14E: 12                              ;
A14F: 12                              ;
A150: 12                              ;
A151: 12                              ;
A152: 12                              ;
A153: 13                              ;
A154: 00              BRK                         ; 
A155: 00              BRK                         ; 
A156: 00              BRK                         ; 
A157: 00              BRK                         ; 
A158: 00              BRK                         ; 
A159: 00              BRK                         ; 
A15A: 31 00           AND     ($00),Y             ; {ram.GP_00}
A15C: 00              BRK                         ; 
A15D: 31 00           AND     ($00),Y             ; {ram.GP_00}
A15F: 00              BRK                         ; 
A160: 00              BRK                         ; 
A161: 00              BRK                         ; 
A162: 00              BRK                         ; 
A163: 61 73           ADC     ($73,X)             ; {ram.0073}
A165: 41 41           EOR     ($41,X)             ; {ram.0041}
A167: 41 41           EOR     ($41,X)             ; {ram.0041}
A169: 41 41           EOR     ($41,X)             ; {ram.0041}
A16B: 74                              ;
A16C: 74                              ;
A16D: 00              BRK                         ; 
A16E: 00              BRK                         ; 
A16F: 57                              ;
A170: 34                              ;
A171: 54                              ;
A172: 25 13           AND     <$13                ; {ram.0013}
A174: 00              BRK                         ; 
A175: 35 25           AND     $25,X               ; {ram.0025}
A177: 13                              ;
A178: 33                              ;
A179: 55 00           EOR     $00,X               ; {ram.GP_00}
A17B: 11 00           ORA     ($00),Y             ; {ram.GP_00}
A17D: 11 00           ORA     ($00),Y             ; {ram.GP_00}
A17F: 11 11           ORA     ($11),Y             ; {ram.0011}
A181: 00              BRK                         ; 
A182: 11 00           ORA     ($00),Y             ; {ram.GP_00}
A184: 11 00           ORA     ($00),Y             ; {ram.GP_00}
A186: 00              BRK                         ; 
A187: 00              BRK                         ; 
A188: 00              BRK                         ; 
A189: 00              BRK                         ; 
A18A: 60              RTS                         ; 
A18B: 00              BRK                         ; 
A18C: 00              BRK                         ; 
A18D: 60              RTS                         ; 
A18E: 00              BRK                         ; 
A18F: 00              BRK                         ; 
A190: 00              BRK                         ; 
A191: 00              BRK                         ; 
A192: 23                              ;
A193: 23                              ;
A194: 23                              ;
A195: 23                              ;
A196: 23                              ;
A197: 23                              ;
A198: 23                              ;
A199: 23                              ;
A19A: 23                              ;
A19B: 23                              ;
A19C: 23                              ;
A19D: 23                              ;
A19E: 00              BRK                         ; 
A19F: 13                              ;
A1A0: 00              BRK                         ; 
A1A1: 13                              ;
A1A2: 00              BRK                         ; 
A1A3: 13                              ;
A1A4: 13                              ;
A1A5: 00              BRK                         ; 
A1A6: 13                              ;
A1A7: 00              BRK                         ; 
A1A8: 13                              ;
A1A9: 00              BRK                         ; 
A1AA: 20 12 21        JSR     $2112               ; 
A1AD: 31 33           AND     ($33),Y             ; {ram.0033}
A1AF: 25 02           AND     <$02                ; {ram.GP_02}
A1B1: 26 31           ROL     <$31                ; {ram.0031}
A1B3: 30 12           BMI     $A1C7               ; {}
A1B5: 17                              ;
A1B6: 00              BRK                         ; 
A1B7: 74                              ;
A1B8: 74                              ;
A1B9: 75 75           ADC     <$75,X              ; {ram.0075}
A1BB: 41 41           EOR     ($41,X)             ; {ram.0041}
A1BD: 75 75           ADC     <$75,X              ; {ram.0075}
A1BF: 74                              ;
A1C0: 74                              ;
A1C1: 00              BRK                         ; 
A1C2: 00              BRK                         ; 
A1C3: 00              BRK                         ; 
A1C4: 00              BRK                         ; 
A1C5: 00              BRK                         ; 
A1C6: 00              BRK                         ; 
A1C7: 00              BRK                         ; 
A1C8: 00              BRK                         ; 
A1C9: 00              BRK                         ; 
A1CA: 61 00           ADC     ($00,X)             ; {ram.GP_00}
A1CC: 00              BRK                         ; 
A1CD: 00              BRK                         ; 
A1CE: 00              BRK                         ; 
A1CF: 62                              ;
A1D0: 66 66           ROR     <$66                ; {ram.SND_PtrA}
A1D2: 66 66           ROR     <$66                ; {ram.SND_PtrA}
A1D4: 66 66           ROR     <$66                ; {ram.SND_PtrA}
A1D6: 66 66           ROR     <$66                ; {ram.SND_PtrA}
A1D8: 62                              ;
A1D9: 00              BRK                         ; 
A1DA: 00              BRK                         ; 
A1DB: 62                              ;
A1DC: 66 64           ROR     <$64                ; {ram.0064}
A1DE: 82                              ;
A1DF: 82                              ;
A1E0: 82                              ;
A1E1: 82                              ;
A1E2: 64                              ;
A1E3: 66 62           ROR     <$62                ; {ram.0062}
A1E5: 00              BRK                         ; 
A1E6: 73                              ;
A1E7: 70 67           BVS     $A250               ; {}
A1E9: 65 73           ADC     <$73                ; {ram.0073}
A1EB: 66 66           ROR     <$66                ; {ram.SND_PtrA}
A1ED: 73                              ;
A1EE: 65 67           ADC     <$67                ; {ram.SND_PtrB}
A1F0: 70 73           BVS     $A265               ; {}
A1F2: 73                              ;
A1F3: 70 71           BVS     $A266               ; {}
A1F5: 70 63           BVS     $A25A               ; {}
A1F7: 32                              ;
A1F8: 43                              ;
A1F9: 71 70           ADC     ($70),Y             ; {ram.0070}
A1FB: 63                              ;
A1FC: 70 73           BVS     $A271               ; {}
A1FE: 43                              ;
A1FF: 43                              ;
A200: 43                              ;
A201: 43                              ;
A202: 43                              ;
A203: 43                              ;
A204: 43                              ;
A205: 43                              ;
A206: 43                              ;
A207: 43                              ;
A208: 43                              ;
A209: 43                              ;
A20A: 66 66           ROR     <$66                ; {ram.SND_PtrA}
A20C: 66 66           ROR     <$66                ; {ram.SND_PtrA}
A20E: 66 66           ROR     <$66                ; {ram.SND_PtrA}
A210: 66 66           ROR     <$66                ; {ram.SND_PtrA}
A212: 66 66           ROR     <$66                ; {ram.SND_PtrA}
A214: 66 66           ROR     <$66                ; {ram.SND_PtrA}
A216: 00              BRK                         ; 
A217: 00              BRK                         ; 
A218: 00              BRK                         ; 
A219: 00              BRK                         ; 
A21A: 31 23           AND     ($23),Y             ; {ram.0023}
A21C: 10 23           BPL     $A241               ; {}
A21E: 31 00           AND     ($00),Y             ; {ram.GP_00}
A220: 00              BRK                         ; 
A221: 00              BRK                         ; 
A222: 00              BRK                         ; 
A223: 00              BRK                         ; 
A224: 00              BRK                         ; 
A225: 00              BRK                         ; 
A226: 00              BRK                         ; 
A227: 00              BRK                         ; 
A228: 00              BRK                         ; 
A229: 00              BRK                         ; 
A22A: 06 04           ASL     <$04                ; {ram.0004}
A22C: 04                              ;
A22D: 03                              ;
A22E: 00              BRK                         ; 
A22F: 13                              ;
A230: 12                              ;
A231: 12                              ;
A232: 12                              ;
A233: 11 11           ORA     ($11),Y             ; {ram.0011}
A235: 15 14           ORA     $14,X               ; {ram.0014}
A237: 02                              ;
A238: 24 00           BIT     <$00                ; {ram.GP_00}
A23A: 00              BRK                         ; 
A23B: 00              BRK                         ; 
A23C: 22                              ;
A23D: 22                              ;
A23E: 00              BRK                         ; 
A23F: 00              BRK                         ; 
A240: 00              BRK                         ; 
A241: 00              BRK                         ; 
A242: 22                              ;
A243: 22                              ;
A244: 00              BRK                         ; 
A245: 00              BRK                         ; 
A246: 00              BRK                         ; 
A247: 00              BRK                         ; 
A248: 00              BRK                         ; 
A249: 00              BRK                         ; 
A24A: 00              BRK                         ; 
A24B: 22                              ;
A24C: 22                              ;
A24D: 00              BRK                         ; 
A24E: 00              BRK                         ; 
A24F: 00              BRK                         ; 
A250: 00              BRK                         ; 
A251: 00              BRK                         ; 
A252: 00              BRK                         ; 
A253: 12                              ;
A254: 12                              ;
A255: 00              BRK                         ; 
A256: 00              BRK                         ; 
A257: 31 31           AND     ($31),Y             ; {ram.0031}
A259: 00              BRK                         ; 
A25A: 00              BRK                         ; 
A25B: 12                              ;
A25C: 12                              ;
A25D: 00              BRK                         ; 
A25E: 04                              ;
A25F: 04                              ;
A260: 04                              ;
A261: 04                              ;
A262: 04                              ;
A263: 80                              ;
A264: 31 04           AND     ($04),Y             ; {ram.0004}
A266: 04                              ;
A267: 04                              ;
A268: 04                              ;
A269: 04                              ;
A26A: 00              BRK                         ; 
A26B: 93                              ;
A26C: 00              BRK                         ; 
A26D: 95 94           STA     $94,X               ; 
A26F: 96 96           STX     $96,Y               ; {ram.0096}
A271: 98              TYA                         ; 
A272: 95 00           STA     $00,X               ; {ram.GP_00}
A274: 97                              ;
A275: 00              BRK                         ; 
A276: 00              BRK                         ; 
A277: 00              BRK                         ; 
A278: 00              BRK                         ; 
A279: 00              BRK                         ; 
A27A: 00              BRK                         ; 
A27B: 31 00           AND     ($00),Y             ; {ram.GP_00}
A27D: 00              BRK                         ; 
A27E: 00              BRK                         ; 
A27F: 00              BRK                         ; 
A280: 00              BRK                         ; 
A281: 00              BRK                         ; 
A282: 00              BRK                         ; 
A283: 00              BRK                         ; 
A284: 00              BRK                         ; 
A285: 00              BRK                         ; 
A286: 87                              ;
A287: 00              BRK                         ; 
A288: 00              BRK                         ; 
A289: 88              DEY                         ; 
A28A: 00              BRK                         ; 
A28B: 00              BRK                         ; 
A28C: 00              BRK                         ; 
A28D: 00              BRK                         ; 
A28E: 85 00           STA     <$00                ; {ram.GP_00}
A290: 00              BRK                         ; 
A291: 00              BRK                         ; 
A292: 00              BRK                         ; 
A293: 00              BRK                         ; 
A294: 00              BRK                         ; 
A295: 00              BRK                         ; 
A296: 00              BRK                         ; 
A297: 00              BRK                         ; 
A298: 00              BRK                         ; 
A299: 52                              ;
A29A: 77                              ;
A29B: 77                              ;
A29C: 77                              ;
A29D: 77                              ;
A29E: 77                              ;
A29F: 77                              ;
A2A0: 77                              ;
A2A1: 77                              ;
A2A2: 77                              ;
A2A3: 77                              ;
A2A4: 77                              ;
A2A5: 77                              ;
A2A6: 76 76           ROR     <$76,X              ; {ram.0076}
A2A8: 76 76           ROR     <$76,X              ; {ram.0076}
A2AA: 76 76           ROR     <$76,X              ; {ram.0076}
A2AC: 76 76           ROR     <$76,X              ; {ram.0076}
A2AE: 76 76           ROR     <$76,X              ; {ram.0076}
A2B0: 76 76           ROR     <$76,X              ; {ram.0076}
A2B2: 60              RTS                         ; 
A2B3: 17                              ;
A2B4: 83                              ;
A2B5: 86 36           STX     <$36                ; {ram.0036}
A2B7: 90 90           BCC     $A249               ; {}
A2B9: 56 86           LSR     $86,X               ; {ram.0086}
A2BB: 50 17           BVC     $A2D4               ; {}
A2BD: 60              RTS                         ; 
A2BE: 84 76           STY     <$76                ; {ram.0076}
A2C0: 44                              ;
A2C1: 40              RTI                         ; 
A2C2: 81 42           STA     ($42,X)             ; {ram.0042}
A2C4: 42                              ;
A2C5: 81 40           STA     ($40,X)             ; {ram.0040}
A2C7: 44                              ;
A2C8: 76 51           ROR     <$51,X              ; {ram.0051}
A2CA: 00              BRK                         ; 
A2CB: 13                              ;
A2CC: 12                              ;
A2CD: 46 91           LSR     <$91                ; {ram.0091}
A2CF: 25 25           AND     <$25                ; {ram.0025}
A2D1: 92                              ;
A2D2: 45 12           EOR     <$12                ; {ram.0012}
A2D4: 13                              ;
A2D5: 00              BRK                         ; 
A2D6: E1 80           SBC     ($80,X)             ; {ram.0080}
A2D8: C1 00           CMP     ($00,X)             ; {ram.GP_00}
A2DA: 01 A0           ORA     ($A0,X)             ; {ram.00A0}
A2DC: 04                              ;
A2DD: A0 01           LDY     #$01                ; 
A2DF: A0 31           LDY     #$31                ; 
A2E1: 90 21           BCC     $A304               ; {}
A2E3: 90 21           BCC     $A306               ; {}
A2E5: 00              BRK                         ; 
A2E6: 81 00           STA     ($00,X)             ; {ram.GP_00}
A2E8: 01 04           ORA     ($04,X)             ; {ram.0004}
A2EA: 81 00           STA     ($00,X)             ; {ram.GP_00}
A2EC: 01 00           ORA     ($00,X)             ; {ram.GP_00}
A2EE: 01 00           ORA     ($00,X)             ; {ram.GP_00}
A2F0: 81 00           STA     ($00,X)             ; {ram.GP_00}
A2F2: 21 00           AND     ($00,X)             ; {ram.GP_00}
A2F4: 81 40           STA     ($40,X)             ; {ram.0040}
A2F6: 81 20           STA     ($20,X)             ; {ram.0020}
A2F8: 01 00           ORA     ($00,X)             ; {ram.GP_00}
A2FA: 81 00           STA     ($00,X)             ; {ram.GP_00}
A2FC: 04                              ;
A2FD: 00              BRK                         ; 
A2FE: 01 00           ORA     ($00,X)             ; {ram.GP_00}
A300: 01 90           ORA     ($90,X)             ; {ram.0090}
A302: 41 80           EOR     ($80,X)             ; {ram.0080}
A304: D1 80           CMP     ($80),Y             ; {ram.0080}
A306: 21 00           AND     ($00,X)             ; {ram.GP_00}
A308: 91 20           STA     ($20),Y             ; {ram.0020}
A30A: 91 00           STA     ($00),Y             ; {ram.GP_00}
A30C: 01 00           ORA     ($00,X)             ; {ram.GP_00}
A30E: 11 D0           ORA     ($D0),Y             ; {ram.00D0}
A310: 81 00           STA     ($00,X)             ; {ram.GP_00}
A312: 41 B1           EOR     ($B1,X)             ; {ram.00B1}
A314: 00              BRK                         ; 
A315: 91 00           STA     ($00),Y             ; {ram.GP_00}
A317: A1 00           LDA     ($00,X)             ; {ram.GP_00}
A319: 21 B1           AND     ($B1,X)             ; {ram.00B1}
A31B: 06 91           ASL     <$91                ; {ram.0091}
A31D: 00              BRK                         ; 
A31E: B1 00           LDA     ($00),Y             ; {ram.GP_00}
A320: 81 00           STA     ($00,X)             ; {ram.GP_00}
A322: 21 90           AND     ($90,X)             ; {ram.0090}
A324: 17                              ;
A325: 02                              ;
A326: 91 17           STA     ($17),Y             ; {ram.0017}
A328: 01 17           ORA     ($17,X)             ; {ram.0017}
A32A: 81 16           STA     ($16,X)             ; {ram.0016}
A32C: B1 07           LDA     ($07),Y             ; {ram.0007}
A32E: 91 06           STA     ($06),Y             ; {ram.0006}
A330: 31 87           AND     ($87),Y             ; {ram.0087}
A332: 31 17           AND     ($17),Y             ; {ram.0017}
A334: 81 00           STA     ($00,X)             ; {ram.GP_00}
A336: 01 03           ORA     ($03,X)             ; {ram.GP_03}
A338: 81 00           STA     ($00,X)             ; {ram.GP_00}
A33A: 01 02           ORA     ($02,X)             ; {ram.GP_02}
A33C: 01 80           ORA     ($80,X)             ; {ram.0080}
A33E: 01 10           ORA     ($10,X)             ; {ram.0010}
A340: 11 83           ORA     ($83),Y             ; {ram.0083}
A342: 47                              ;
A343: 83                              ;
A344: 41 03           EOR     ($03,X)             ; {ram.GP_03}
A346: D1 03           CMP     ($03),Y             ; {ram.GP_03}
A348: 90 01           BCC     $A34B               ; {}
A34A: 10 91           BPL     $A2DD               ; {}
A34C: 00              BRK                         ; 
A34D: 11 90           ORA     ($90),Y             ; {ram.0090}
A34F: 17                              ;
A350: 03                              ;
A351: 11 C0           ORA     ($C0),Y             ; {ram.00C0}
A353: 11 E0           ORA     ($E0),Y             ; {ram.??SND_E0??}
A355: E6 81           INC     <$81                ; {ram.0081}
A357: C6 81           DEC     <$81                ; {ram.0081}
A359: 86 01           STX     <$01                ; {ram.GP_01}
A35B: 06 01           ASL     <$01                ; {ram.GP_01}
A35D: 06 81           ASL     <$81                ; {ram.0081}
A35F: 06 21           ASL     <$21                ; {ram.0021}
A361: 86 01           STX     <$01                ; {ram.GP_01}
A363: 26 01           ROL     <$01                ; {ram.GP_01}
A365: 86 41           STX     <$41                ; {ram.0041}
A367: 86 01           STX     <$01                ; {ram.GP_01}
A369: 46 D1           LSR     <$D1                ; {ram.00D1}
A36B: 02                              ;
A36C: A6 01           LDX     <$01                ; {ram.GP_01}
A36E: 26 81           ROL     <$81                ; {ram.0081}
A370: 56 81           LSR     $81,X               ; {ram.0081}
A372: 16 11           ASL     $11,X               ; {ram.0011}
A374: 16 E7           ASL     $E7,X               ; {ram.00E7}
A376: E5 81           SBC     <$81                ; {ram.0081}
A378: 10 01           BPL     $A37B               ; {}
A37A: 10 81           BPL     $A2FD               ; {}
A37C: 27                              ;
A37D: A1 06           LDA     ($06,X)             ; {ram.0006}
A37F: 21 80           AND     ($80,X)             ; {ram.0080}
A381: 01 10           ORA     ($10,X)             ; {ram.0010}
A383: 11 82           ORA     ($82),Y             ; {ram.0082}
A385: 47                              ;
A386: 82                              ;
A387: 41 02           EOR     ($02,X)             ; {ram.GP_02}
A389: 80                              ;
A38A: 01 10           ORA     ($10,X)             ; {ram.0010}
A38C: A1 02           LDA     ($02,X)             ; {ram.GP_02}
A38E: A1 03           LDA     ($03,X)             ; {ram.GP_03}
A390: 21 80           AND     ($80,X)             ; {ram.0080}
A392: 27                              ;
A393: 21 81           AND     ($81,X)             ; {ram.0081}
A395: 00              BRK                         ; 
A396: 02                              ;
A397: 11 00           ORA     ($00),Y             ; {ram.GP_00}
A399: 81 00           STA     ($00,X)             ; {ram.GP_00}
A39B: 03                              ;
A39C: 11 00           ORA     ($00),Y             ; {ram.GP_00}
A39E: 81 02           STA     ($02,X)             ; {ram.GP_02}
A3A0: 81 02           STA     ($02,X)             ; {ram.GP_02}
A3A2: 01 02           ORA     ($02,X)             ; {ram.GP_02}
A3A4: 01 02           ORA     ($02,X)             ; {ram.GP_02}
A3A6: 05 C1           ORA     <$C1                ; {ram.00C1}
A3A8: 15 B1           ORA     $B1,X               ; {ram.00B1}
A3AA: 25 81           AND     <$81                ; {ram.0081}
A3AC: 03                              ;
A3AD: 81 03           STA     ($03,X)             ; {ram.GP_03}
A3AF: 01 03           ORA     ($03,X)             ; {ram.GP_03}
A3B1: 01 03           ORA     ($03,X)             ; {ram.GP_03}
A3B3: 05 04           ORA     <$04                ; {ram.0004}
A3B5: 04                              ;
A3B6: 00              BRK                         ; 
A3B7: 01 00           ORA     ($00,X)             ; {ram.GP_00}
A3B9: 00              BRK                         ; 
A3BA: 00              BRK                         ; 
A3BB: 00              BRK                         ; 
A3BC: 00              BRK                         ; 
A3BD: 00              BRK                         ; 
A3BE: 00              BRK                         ; 
A3BF: 00              BRK                         ; 
A3C0: 01 00           ORA     ($00,X)             ; {ram.GP_00}
A3C2: 04                              ;
A3C3: 04                              ;
A3C4: 04                              ;
A3C5: 04                              ;
A3C6: 00              BRK                         ; 
A3C7: 01 00           ORA     ($00,X)             ; {ram.GP_00}
A3C9: 00              BRK                         ; 
A3CA: 00              BRK                         ; 
A3CB: 03                              ;
A3CC: 03                              ;
A3CD: 03                              ;
A3CE: 03                              ;
A3CF: 02                              ;
A3D0: 03                              ;
A3D1: 03                              ;
A3D2: 04                              ;
A3D3: 04                              ;
A3D4: 82                              ;
A3D5: 43                              ;
A3D6: 43                              ;
A3D7: 43                              ;
A3D8: 02                              ;
A3D9: 0C                              ;
A3DA: 43                              ;
A3DB: 80                              ;
A3DC: 41 41           EOR     ($41,X)             ; {ram.0041}
A3DE: 41 41           EOR     ($41,X)             ; {ram.0041}
A3E0: 43                              ;
A3E1: 82                              ;
A3E2: 43                              ;
A3E3: 42                              ;
A3E4: 0C                              ;
A3E5: 01 41           ORA     ($41,X)             ; {ram.0041}
A3E7: 43                              ;
A3E8: 82                              ;
A3E9: 43                              ;
A3EA: 42                              ;
A3EB: 0C                              ;
A3EC: 03                              ;
A3ED: 02                              ;
A3EE: 0C                              ;
A3EF: 43                              ;
A3F0: 82                              ;
A3F1: 43                              ;
A3F2: 43                              ;
A3F3: 43                              ;
A3F4: 43                              ;
A3F5: 43                              ;

A3F6: A9 01           LDA     #$01                ; 
A3F8: 85 01           STA     <$01                ; {ram.GP_01}
A3FA: A9 03           LDA     #$03                ; 
A3FC: 85 03           STA     <$03                ; {ram.GP_03}
A3FE: A4 EB           LDY     <$EB                ; {ram.00EB}
A400: B9 7E 68        LDA     $687E,Y             ; 
A403: A4 03           LDY     <$03                ; {ram.GP_03}
A405: C0 02           CPY     #$02                ; 
A407: 90 05           BCC     $A40E               ; {}
A409: A4 EB           LDY     <$EB                ; {ram.00EB}
A40B: B9 FE 68        LDA     $68FE,Y             ; 
A40E: 85 00           STA     <$00                ; {ram.GP_00}
A410: A5 03           LDA     <$03                ; {ram.GP_03}
A412: 29 01           AND     #$01                ; 
A414: D0 06           BNE     $A41C               ; {}
A416: 46 00           LSR     <$00                ; {ram.GP_00}
A418: 46 00           LSR     <$00                ; {ram.GP_00}
A41A: 46 00           LSR     <$00                ; {ram.GP_00}
A41C: 46 00           LSR     <$00                ; {ram.GP_00}
A41E: 46 00           LSR     <$00                ; {ram.GP_00}
A420: A5 02           LDA     <$02                ; {ram.GP_02}
A422: 24 01           BIT     <$01                ; {ram.GP_01}
A424: D0 09           BNE     $A42F               ; {}
A426: 06 01           ASL     <$01                ; {ram.GP_01}
A428: C6 03           DEC     <$03                ; {ram.GP_03}
A42A: 10 D2           BPL     $A3FE               ; {}
A42C: A9 08           LDA     #$08                ; 
A42E: 60              RTS                         ; 
A42F: A5 00           LDA     <$00                ; {ram.GP_00}
A431: 29 07           AND     #$07                ; 
A433: 60              RTS                         ; 
A434: A9 13           LDA     #$13                ; 
A436: 85 06           STA     <$06                ; {ram.0006}
A438: A2 19           LDX     #$19                ; 
A43A: D0 48           BNE     $A484               ; {}
A43C: 20 98 72        JSR     $7298               ; {ram.7298}
A43F: 4C 8E A4        JMP     $A48E               ; {}
A442: A9 A0           LDA     #$A0                ; 
A444: 85 00           STA     <$00                ; {ram.GP_00}
A446: A9 9F           LDA     #$9F                ; 
A448: 85 01           STA     <$01                ; {ram.GP_01}
A44A: A9 47           LDA     #$47                ; 
A44C: 85 02           STA     <$02                ; {ram.GP_02}
A44E: A9 65           LDA     #$65                ; 
A450: 85 03           STA     <$03                ; {ram.GP_03}
A452: A9 5A           LDA     #$5A                ; 
A454: 85 04           STA     <$04                ; {ram.0004}
A456: A9 65           LDA     #$65                ; 
A458: 85 05           STA     <$05                ; {ram.0005}
A45A: A9 0A           LDA     #$0A                ; 
A45C: 85 06           STA     <$06                ; {ram.0006}
A45E: A0 00           LDY     #$00                ; 
A460: B1 00           LDA     ($00),Y             ; {ram.GP_00}
A462: F0 D0           BEQ     $A434               ; {}
A464: 91 02           STA     ($02),Y             ; {ram.GP_02}
A466: 91 04           STA     ($04),Y             ; {ram.0004}
A468: C9 DE           CMP     #$DE                ; 
A46A: F0 08           BEQ     $A474               ; {}
A46C: C9 E2           CMP     #$E2                ; 
A46E: B0 04           BCS     $A474               ; {}
A470: 69 01           ADC     #$01                ; 
A472: 91 04           STA     ($04),Y             ; {ram.0004}
A474: A9 01           LDA     #$01                ; 
A476: A2 01           LDX     #$01                ; 
A478: C6 06           DEC     <$06                ; {ram.0006}
A47A: D0 08           BNE     $A484               ; {}
A47C: A9 0A           LDA     #$0A                ; 
A47E: 85 06           STA     <$06                ; {ram.0006}
A480: A9 0D           LDA     #$0D                ; 
A482: A2 1F           LDX     #$1F                ; 
A484: 20 82 72        JSR     $7282               ; {ram.7282}
A487: 8A              TXA                         ; 
A488: CA              DEX                         ; 
A489: F0 B1           BEQ     $A43C               ; {}
A48B: 20 8E 72        JSR     $728E               ; {ram.728E}
A48E: 20 74 72        JSR     $7274               ; {ram.7274}
A491: C9 EE           CMP     #$EE                ; 
A493: D0 CB           BNE     $A460               ; {}
A495: A9 30           LDA     #$30                ; 
A497: 85 02           STA     <$02                ; {ram.GP_02}
A499: A9 65           LDA     #$65                ; 
A49B: 85 03           STA     <$03                ; {ram.GP_03}
A49D: A9 EF           LDA     #$EF                ; 
A49F: 85 04           STA     <$04                ; {ram.0004}
A4A1: A9 67           LDA     #$67                ; 
A4A3: 85 05           STA     <$05                ; {ram.0005}
A4A5: B1 02           LDA     ($02),Y             ; {ram.GP_02}
A4A7: 91 04           STA     ($04),Y             ; {ram.0004}
A4A9: C9 DD           CMP     #$DD                ; 
A4AB: F0 22           BEQ     $A4CF               ; {}
A4AD: C9 E0           CMP     #$E0                ; 
A4AF: B0 0D           BCS     $A4BE               ; {}
A4B1: C9 DC           CMP     #$DC                ; 
A4B3: B0 04           BCS     $A4B9               ; {}
A4B5: 69 01           ADC     #$01                ; 
A4B7: 91 04           STA     ($04),Y             ; {ram.0004}
A4B9: 18              CLC                         ; 
A4BA: 69 01           ADC     #$01                ; 
A4BC: 91 04           STA     ($04),Y             ; {ram.0004}
A4BE: 20 98 72        JSR     $7298               ; {ram.7298}
A4C1: 20 80 72        JSR     $7280               ; {ram.7280}
A4C4: C9 90           CMP     #$90                ; 
A4C6: D0 DD           BNE     $A4A5               ; {}
A4C8: A5 03           LDA     <$03                ; {ram.GP_03}
A4CA: C9 66           CMP     #$66                ; 
A4CC: D0 D7           BNE     $A4A5               ; {}
A4CE: 60              RTS                         ; 
A4CF: A9 DC           LDA     #$DC                ; 
A4D1: D0 E9           BNE     $A4BC               ; {}
A4D3: 01 02           ORA     ($02,X)             ; {ram.GP_02}
A4D5: 04                              ;
A4D6: 08              PHP                         ; 
A4D7: EE 2A 66        INC     $662A               ; {ram.662A}
A4DA: A2 9F           LDX     #$9F                ; 
A4DC: A0 A0           LDY     #$A0                ; 
A4DE: A0 A1           LDY     #$A1                ; 
A4E0: 4F                              ;
A4E1: 76 65           ROR     <$65,X              ; {ram.0065}
A4E3: 67                              ;
A4E4: 65 66           ADC     <$66                ; {ram.SND_PtrA}
A4E6: 66 14           ROR     <$14                ; {ram.0014}
A4E8: 01 01           ORA     ($01,X)             ; {ram.GP_01}
A4EA: 02                              ;
A4EB: 02                              ;
A4EC: 2C 2C 03        BIT     $032C               ; {ram.032C}
A4EF: 03                              ;
A4F0: 02                              ;
A4F1: 02                              ;
A4F2: 01 01           ORA     ($01,X)             ; {ram.GP_01}
A4F4: 02                              ;
A4F5: 02                              ;
A4F6: A2 03           LDX     #$03                ; 
A4F8: A9 01           LDA     #$01                ; 
A4FA: 85 06           STA     <$06                ; {ram.0006}
A4FC: 8A              TXA                         ; 
A4FD: 48              PHA                         ; 
A4FE: 85 0B           STA     <$0B                ; {ram.000B}
A500: BD D3 A4        LDA     $A4D3,X             ; {}
A503: 85 02           STA     <$02                ; {ram.GP_02}
A505: 20 F6 A3        JSR     $A3F6               ; {}
A508: C9 05           CMP     #$05                ; 
A50A: B0 1C           BCS     $A528               ; {}
A50C: C9 04           CMP     #$04                ; 
A50E: D0 08           BNE     $A518               ; {}
A510: A9 08           LDA     #$08                ; 
A512: D0 14           BNE     $A528               ; {}
A514: A9 09           LDA     #$09                ; 
A516: D0 2F           BNE     $A547               ; {}
A518: 48              PHA                         ; 
A519: A5 02           LDA     <$02                ; {ram.GP_02}
A51B: 49 FF           EOR     #$FF                ; 
A51D: 25 EE           AND     <$EE                ; {ram.00EE}
A51F: 85 EE           STA     <$EE                ; {ram.00EE}
A521: 68              PLA                         ; 
A522: C9 01           CMP     #$01                ; 
A524: B0 02           BCS     $A528               ; {}
A526: A9 04           LDA     #$04                ; 
A528: 48              PHA                         ; 
A529: A5 EE           LDA     <$EE                ; {ram.00EE}
A52B: 25 02           AND     <$02                ; {ram.GP_02}
A52D: AA              TAX                         ; 
A52E: 68              PLA                         ; 
A52F: E4 02           CPX     <$02                ; {ram.GP_02}
A531: D0 14           BNE     $A547               ; {}
A533: A8              TAY                         ; 
A534: 68              PLA                         ; 
A535: 48              PHA                         ; 
A536: AA              TAX                         ; 
A537: 98              TYA                         ; 
A538: C9 07           CMP     #$07                ; 
A53A: F0 09           BEQ     $A545               ; {}
A53C: 48              PHA                         ; 
A53D: 20 97 8A        JSR     $8A97               ; {}
A540: 68              PLA                         ; 
A541: C9 08           CMP     #$08                ; 
A543: F0 CF           BEQ     $A514               ; {}
A545: A9 04           LDA     #$04                ; 
A547: A6 06           LDX     <$06                ; {ram.0006}
A549: F0 0A           BEQ     $A555               ; {}
A54B: A6 0B           LDX     <$0B                ; {ram.000B}
A54D: 48              PHA                         ; 
A54E: 20 F6 A3        JSR     $A3F6               ; {}
A551: 20 41 B6        JSR     $B641               ; {}
A554: 68              PLA                         ; 
A555: C9 04           CMP     #$04                ; 
A557: 90 4C           BCC     $A5A5               ; {}
A559: 38              SEC                         ; 
A55A: E9 03           SBC     #$03                ; 
A55C: A8              TAY                         ; 
A55D: C0 03           CPY     #$03                ; 
A55F: 90 01           BCC     $A562               ; {}
A561: 88              DEY                         ; 
A562: 68              PLA                         ; 
A563: 48              PHA                         ; 
A564: 20 B4 A5        JSR     $A5B4               ; {}
A567: A5 06           LDA     <$06                ; {ram.0006}
A569: D0 0B           BNE     $A576               ; {}
A56B: BD EA A4        LDA     $A4EA,X             ; {}
A56E: 20 76 72        JSR     $7276               ; {ram.7276}
A571: A9 06           LDA     #$06                ; 
A573: 20 82 72        JSR     $7282               ; {ram.7282}
A576: A0 00           LDY     #$00                ; 
A578: BD EE A4        LDA     $A4EE,X             ; {}
A57B: 85 05           STA     <$05                ; {ram.0005}
A57D: 68              PLA                         ; 
A57E: 48              PHA                         ; 
A57F: AA              TAX                         ; 
A580: BD F2 A4        LDA     $A4F2,X             ; {}
A583: AA              TAX                         ; 
A584: B1 02           LDA     ($02),Y             ; {ram.GP_02}
A586: 91 00           STA     ($00),Y             ; {ram.GP_00}
A588: 20 80 72        JSR     $7280               ; {ram.7280}
A58B: BD E7 A4        LDA     $A4E7,X             ; {}
A58E: 20 76 72        JSR     $7276               ; {ram.7276}
A591: E0 00           CPX     #$00                ; 
A593: D0 09           BNE     $A59E               ; {}
A595: 68              PLA                         ; 
A596: 48              PHA                         ; 
A597: C9 02           CMP     #$02                ; 
A599: B0 03           BCS     $A59E               ; {}
A59B: 20 74 72        JSR     $7274               ; {ram.7274}
A59E: CA              DEX                         ; 
A59F: 10 E3           BPL     $A584               ; {}
A5A1: C6 05           DEC     <$05                ; {ram.0005}
A5A3: D0 D8           BNE     $A57D               ; {}
A5A5: 68              PLA                         ; 
A5A6: AA              TAX                         ; 
A5A7: C6 06           DEC     <$06                ; {ram.0006}
A5A9: 30 03           BMI     $A5AE               ; {}
A5AB: 4C FC A4        JMP     $A4FC               ; {}
A5AE: CA              DEX                         ; 
A5AF: 30 23           BMI     $A5D4               ; {}
A5B1: 4C F8 A4        JMP     $A4F8               ; {}
A5B4: AA              TAX                         ; 
A5B5: BD D7 A4        LDA     $A4D7,X             ; {}
A5B8: 85 02           STA     <$02                ; {ram.GP_02}
A5BA: BD DB A4        LDA     $A4DB,X             ; {}
A5BD: 85 03           STA     <$03                ; {ram.GP_03}
A5BF: BD DF A4        LDA     $A4DF,X             ; {}
A5C2: 85 00           STA     <$00                ; {ram.GP_00}
A5C4: BD E3 A4        LDA     $A4E3,X             ; {}
A5C7: 85 01           STA     <$01                ; {ram.GP_01}
A5C9: 88              DEY                         ; 
A5CA: F0 08           BEQ     $A5D4               ; {}
A5CC: A9 0C           LDA     #$0C                ; 
A5CE: 20 82 72        JSR     $7282               ; {ram.7282}
A5D1: 4C C9 A5        JMP     $A5C9               ; {}
A5D4: 60              RTS                         ; 
A5D5: 01 03           ORA     ($03,X)             ; {ram.GP_03}
A5D7: 06 08           ASL     <$08                ; {ram.0008}
A5D9: 03                              ;
A5DA: 05 08           ORA     <$08                ; {ram.0008}
A5DC: 0A              ASL     A                   ; 
A5DD: 03                              ;
A5DE: 06 04           ASL     <$04                ; {ram.0004}
A5E0: 07                              ;
A5E1: 05 08           ORA     <$08                ; {ram.0008}
A5E3: 00              BRK                         ; 
A5E4: 04                              ;
A5E5: 08              PHP                         ; 
A5E6: 0A              ASL     A                   ; 
A5E7: 22                              ;
A5E8: 22                              ;
A5E9: 23                              ;
A5EA: 21 5C           AND     ($5C,X)             ; {ram.!FlipFlag}
A5EC: 42                              ;
A5ED: 4F                              ;
A5EE: 4F                              ;
A5EF: 01 FF           ORA     ($FF,X)             ; {ram.CUR_2000}
A5F1: 10 F0           BPL     $A5E3               ; {}
A5F3: A5 12           LDA     <$12                ; {ram.0012}
A5F5: C9 12           CMP     #$12                ; 
A5F7: F0 DB           BEQ     $A5D4               ; {}
A5F9: A5 27           LDA     <$27                ; {ram.0027}
A5FB: D0 D7           BNE     $A5D4               ; {}
A5FD: A5 54           LDA     <$54                ; {ram.0054}
A5FF: F0 D3           BEQ     $A5D4               ; {}
A601: 29 07           AND     #$07                ; 
A603: A0 01           LDY     #$01                ; 
A605: 84 02           STY     <$02                ; {ram.GP_02}
A607: 24 02           BIT     <$02                ; {ram.GP_02}
A609: F0 01           BEQ     $A60C               ; {}
A60B: 4A              LSR     A                   ; 
A60C: C9 02           CMP     #$02                ; 
A60E: D0 04           BNE     $A614               ; {}
A610: A0 30           LDY     #$30                ; 
A612: 84 28           STY     <$28                ; {ram.0028}
A614: 29 03           AND     #$03                ; 
A616: 38              SEC                         ; 
A617: E9 01           SBC     #$01                ; 
A619: 29 02           AND     #$02                ; 
A61B: 85 08           STA     <$08                ; {ram.0008}
A61D: A5 54           LDA     <$54                ; {ram.0054}
A61F: C9 05           CMP     #$05                ; 
A621: B0 0E           BCS     $A631               ; {}
A623: A5 55           LDA     <$55                ; {ram.0055}
A625: 85 02           STA     <$02                ; {ram.GP_02}
A627: 20 F6 A3        JSR     $A3F6               ; {}
A62A: C9 07           CMP     #$07                ; 
A62C: F0 03           BEQ     $A631               ; {}
A62E: 4C 82 A6        JMP     $A682               ; {}
A631: 20 B1 A6        JSR     $A6B1               ; {}
A634: A5 06           LDA     <$06                ; {ram.0006}
A636: 85 04           STA     <$04                ; {ram.0004}
A638: A5 00           LDA     <$00                ; {ram.GP_00}
A63A: 9D 02 03        STA     $0302,X             ; {ram.0302}
A63D: E8              INX                         ; 
A63E: A5 01           LDA     <$01                ; {ram.GP_01}
A640: 9D 02 03        STA     $0302,X             ; {ram.0302}
A643: E8              INX                         ; 
A644: A5 06           LDA     <$06                ; {ram.0006}
A646: 9D 02 03        STA     $0302,X             ; {ram.0302}
A649: E8              INX                         ; 
A64A: 20 00 94        JSR     $9400               ; {}
A64D: D0 FB           BNE     $A64A               ; {}
A64F: A9 20           LDA     #$20                ; 
A651: 05 01           ORA     <$01                ; {ram.GP_01}
A653: 85 01           STA     <$01                ; {ram.GP_01}
A655: C6 05           DEC     <$05                ; {ram.0005}
A657: D0 DB           BNE     $A634               ; {}
A659: A9 FF           LDA     #$FF                ; 
A65B: 9D 02 03        STA     $0302,X             ; {ram.0302}
A65E: 8A              TXA                         ; 
A65F: 8D 01 03        STA     $0301               ; {ram.0301}
A662: E6 54           INC     <$54                ; {ram.0054}
A664: A5 54           LDA     <$54                ; {ram.0054}
A666: 29 03           AND     #$03                ; 
A668: F0 05           BEQ     $A66F               ; {}
A66A: A9 08           LDA     #$08                ; 
A66C: 85 27           STA     <$27                ; {ram.0027}
A66E: 60              RTS                         ; 
A66F: A5 54           LDA     <$54                ; {ram.0054}
A671: C9 04           CMP     #$04                ; 
A673: D0 14           BNE     $A689               ; {}
A675: A6 09           LDX     <$09                ; {ram.0009}
A677: 20 A0 8A        JSR     $8AA0               ; {}
A67A: A5 55           LDA     <$55                ; {ram.0055}
A67C: 49 0F           EOR     #$0F                ; 
A67E: 25 EE           AND     <$EE                ; {ram.00EE}
A680: 85 EE           STA     <$EE                ; {ram.00EE}
A682: A9 00           LDA     #$00                ; 
A684: 85 54           STA     <$54                ; {ram.0054}
A686: 4C F6 A4        JMP     $A4F6               ; {}
A689: A5 55           LDA     <$55                ; {ram.0055}
A68B: 85 02           STA     <$02                ; {ram.GP_02}
A68D: 20 F6 A3        JSR     $A3F6               ; {}
A690: C9 07           CMP     #$07                ; 
A692: F0 16           BEQ     $A6AA               ; {}
A694: A6 09           LDX     <$09                ; {ram.0009}
A696: 20 97 8A        JSR     $8A97               ; {}
A699: 98              TYA                         ; 
A69A: 18              CLC                         ; 
A69B: 7D EF A5        ADC     $A5EF,X             ; {}
A69E: A8              TAY                         ; 
A69F: 8A              TXA                         ; 
A6A0: 49 01           EOR     #$01                ; 
A6A2: AA              TAX                         ; 
A6A3: B1 00           LDA     ($00),Y             ; {ram.GP_00}
A6A5: 1D BE E6        ORA     $E6BE,X             ; 
A6A8: 91 00           STA     ($00),Y             ; {ram.GP_00}
A6AA: A5 55           LDA     <$55                ; {ram.0055}
A6AC: 05 EE           ORA     <$EE                ; {ram.00EE}
A6AE: 4C 80 A6        JMP     $A680               ; {}
A6B1: A5 55           LDA     <$55                ; {ram.0055}
A6B3: 85 02           STA     <$02                ; {ram.GP_02}
A6B5: 20 F6 A3        JSR     $A3F6               ; {}
A6B8: C9 05           CMP     #$05                ; 
A6BA: 90 07           BCC     $A6C3               ; {}
A6BC: 48              PHA                         ; 
A6BD: A9 04           LDA     #$04                ; 
A6BF: 20 7C 6D        JSR     $6D7C               ; {ram.6D7C}
A6C2: 68              PLA                         ; 
A6C3: C9 04           CMP     #$04                ; 
A6C5: D0 02           BNE     $A6C9               ; {}
A6C7: A9 08           LDA     #$08                ; 
A6C9: C9 01           CMP     #$01                ; 
A6CB: D0 02           BNE     $A6CF               ; {}
A6CD: A9 04           LDA     #$04                ; 
A6CF: 38              SEC                         ; 
A6D0: E9 03           SBC     #$03                ; 
A6D2: A8              TAY                         ; 
A6D3: A5 08           LDA     <$08                ; {ram.0008}
A6D5: F0 06           BEQ     $A6DD               ; {}
A6D7: C0 05           CPY     #$05                ; 
A6D9: F0 07           BEQ     $A6E2               ; {}
A6DB: A0 01           LDY     #$01                ; 
A6DD: C0 03           CPY     #$03                ; 
A6DF: 90 01           BCC     $A6E2               ; {}
A6E1: 88              DEY                         ; 
A6E2: A9 03           LDA     #$03                ; 
A6E4: 38              SEC                         ; 
A6E5: E5 03           SBC     <$03                ; {ram.GP_03}
A6E7: 20 B4 A5        JSR     $A5B4               ; {}
A6EA: BD E7 A5        LDA     $A5E7,X             ; {}
A6ED: 85 00           STA     <$00                ; {ram.GP_00}
A6EF: BD EB A5        LDA     $A5EB,X             ; {}
A6F2: 85 01           STA     <$01                ; {ram.GP_01}
A6F4: 86 09           STX     <$09                ; {ram.0009}
A6F6: AE 01 03        LDX     $0301               ; {ram.0301}
A6F9: A9 00           LDA     #$00                ; 
A6FB: 85 07           STA     <$07                ; {ram.0007}
A6FD: A9 02           LDA     #$02                ; 
A6FF: 85 06           STA     <$06                ; {ram.0006}
A701: 85 05           STA     <$05                ; {ram.0005}
A703: 60              RTS                         ; 
A704: D6 A2           DEC     $A2,X               ; {ram.00A2}
A706: E6 A2           INC     <$A2                ; {ram.00A2}
A708: 04                              ;
A709: A3                              ;
A70A: 15 A3           ORA     $A3,X               ; {ram.00A3}
A70C: 26 A3           ROL     <$A3                ; {ram.00A3}
A70E: 3D A3 54        AND     $54A3,X             ; 
A711: A3                              ;
A712: 65 A3           ADC     <$A3                ; {ram.00A3}
A714: 77                              ;
A715: A3                              ;
A716: 91 A3           STA     ($A3),Y             ; {ram.00A3}
A718: B0 74           BCS     $A78E               ; {}
A71A: 94 B4           STY     $B4,X               ; {ram.00B4}
A71C: 70 68           BVS     $A786               ; {}
A71E: F4                              ;
A71F: 24 20           BIT     <$20                ; {ram.0020}
A721: 5A                              ;
A722: E8              INX                         ; 
A723: 48              PHA                         ; 
A724: A9 DE           LDA     #$DE                ; 
A726: 85 02           STA     <$02                ; {ram.GP_02}
A728: A9 A0           LDA     #$A0                ; 
A72A: 85 03           STA     <$03                ; {ram.GP_03}
A72C: 68              PLA                         ; 
A72D: 0A              ASL     A                   ; 
A72E: 0A              ASL     A                   ; 
A72F: 85 00           STA     <$00                ; {ram.GP_00}
A731: 20 82 72        JSR     $7282               ; {ram.7282}
A734: A5 00           LDA     <$00                ; {ram.GP_00}
A736: 20 82 72        JSR     $7282               ; {ram.7282}
A739: A5 00           LDA     <$00                ; {ram.GP_00}
A73B: 20 82 72        JSR     $7282               ; {ram.7282}
A73E: A9 8C           LDA     #$8C                ; 
A740: 85 00           STA     <$00                ; {ram.GP_00}
A742: A9 65           LDA     #$65                ; 
A744: 85 01           STA     <$01                ; {ram.GP_01}
A746: A0 00           LDY     #$00                ; 
A748: 84 06           STY     <$06                ; {ram.0006}
A74A: A4 06           LDY     <$06                ; {ram.0006}
A74C: B1 02           LDA     ($02),Y             ; {ram.GP_02}
A74E: 29 F0           AND     #$F0                ; 
A750: 4A              LSR     A                   ; 
A751: 4A              LSR     A                   ; 
A752: 4A              LSR     A                   ; 
A753: AA              TAX                         ; 
A754: BD 04 A7        LDA     $A704,X             ; {}
A757: 85 04           STA     <$04                ; {ram.0004}
A759: BD 05 A7        LDA     $A705,X             ; {}
A75C: 85 05           STA     <$05                ; {ram.0005}
A75E: B1 02           LDA     ($02),Y             ; {ram.GP_02}
A760: 29 0F           AND     #$0F                ; 
A762: AA              TAX                         ; 
A763: A0 00           LDY     #$00                ; 
A765: B1 04           LDA     ($04),Y             ; {ram.0004}
A767: 10 03           BPL     $A76C               ; {}
A769: CA              DEX                         ; 
A76A: 30 04           BMI     $A770               ; {}
A76C: C8              INY                         ; 
A76D: 4C 65 A7        JMP     $A765               ; {}
A770: 98              TYA                         ; 
A771: 20 8E 72        JSR     $728E               ; {ram.728E}
A774: A9 00           LDA     #$00                ; 
A776: 85 07           STA     <$07                ; {ram.0007}
A778: 85 08           STA     <$08                ; {ram.0008}
A77A: A0 00           LDY     #$00                ; 
A77C: B1 04           LDA     ($04),Y             ; {ram.0004}
A77E: 29 07           AND     #$07                ; 
A780: AA              TAX                         ; 
A781: BD 18 A7        LDA     $A718,X             ; {}
A784: A0 00           LDY     #$00                ; 
A786: 20 C1 A7        JSR     $A7C1               ; {}
A789: A9 02           LDA     #$02                ; 
A78B: 20 76 72        JSR     $7276               ; {ram.7276}
A78E: A0 00           LDY     #$00                ; 
A790: B1 04           LDA     ($04),Y             ; {ram.0004}
A792: 29 70           AND     #$70                ; 
A794: 4A              LSR     A                   ; 
A795: 4A              LSR     A                   ; 
A796: 4A              LSR     A                   ; 
A797: 4A              LSR     A                   ; 
A798: C5 08           CMP     <$08                ; {ram.0008}
A79A: F0 05           BEQ     $A7A1               ; {}
A79C: E6 08           INC     <$08                ; {ram.0008}
A79E: 4C A8 A7        JMP     $A7A8               ; {}
A7A1: A9 00           LDA     #$00                ; 
A7A3: 85 08           STA     <$08                ; {ram.0008}
A7A5: 20 8C 72        JSR     $728C               ; {ram.728C}
A7A8: E6 07           INC     <$07                ; {ram.0007}
A7AA: A5 07           LDA     <$07                ; {ram.0007}
A7AC: C9 07           CMP     #$07                ; 
A7AE: 90 CA           BCC     $A77A               ; {}
A7B0: A9 1E           LDA     #$1E                ; 
A7B2: 20 76 72        JSR     $7276               ; {ram.7276}
A7B5: E6 06           INC     <$06                ; {ram.0006}
A7B7: A5 06           LDA     <$06                ; {ram.0006}
A7B9: C9 0C           CMP     #$0C                ; 
A7BB: B0 03           BCS     $A7C0               ; {}
A7BD: 4C 4A A7        JMP     $A74A               ; {}
A7C0: 60              RTS                         ; 
A7C1: C9 70           CMP     #$70                ; 
A7C3: 90 1B           BCC     $A7E0               ; {}
A7C5: C9 F3           CMP     #$F3                ; 
A7C7: B0 17           BCS     $A7E0               ; {}
A7C9: AA              TAX                         ; 
A7CA: 91 00           STA     ($00),Y             ; {ram.GP_00}
A7CC: C8              INY                         ; 
A7CD: E8              INX                         ; 
A7CE: 8A              TXA                         ; 
A7CF: 91 00           STA     ($00),Y             ; {ram.GP_00}
A7D1: 98              TYA                         ; 
A7D2: 18              CLC                         ; 
A7D3: 69 15           ADC     #$15                ; 
A7D5: A8              TAY                         ; 
A7D6: E8              INX                         ; 
A7D7: 8A              TXA                         ; 
A7D8: 91 00           STA     ($00),Y             ; {ram.GP_00}
A7DA: E8              INX                         ; 
A7DB: 8A              TXA                         ; 
A7DC: C8              INY                         ; 
A7DD: 91 00           STA     ($00),Y             ; {ram.GP_00}
A7DF: 60              RTS                         ; 
A7E0: 91 00           STA     ($00),Y             ; {ram.GP_00}
A7E2: C8              INY                         ; 
A7E3: 91 00           STA     ($00),Y             ; {ram.GP_00}
A7E5: 48              PHA                         ; 
A7E6: 98              TYA                         ; 
A7E7: 18              CLC                         ; 
A7E8: 69 15           ADC     #$15                ; 
A7EA: A8              TAY                         ; 
A7EB: 68              PLA                         ; 
A7EC: 91 00           STA     ($00),Y             ; {ram.GP_00}
A7EE: 4C DC A7        JMP     $A7DC               ; {}
A7F1: A9 00           LDA     #$00                ; 
A7F3: 85 B7           STA     <$B7                ; {ram.00B7}
A7F5: 85 A3           STA     <$A3                ; {ram.00A3}
A7F7: 20 5A E8        JSR     $E85A               ; 
A7FA: C9 21           CMP     #$21                ; 
A7FC: D0 0A           BNE     $A808               ; {}
A7FE: A9 40           LDA     #$40                ; 
A800: 85 7B           STA     <$7B                ; {ram.007B}
A802: 0A              ASL     A                   ; 
A803: 85 8F           STA     <$8F                ; {ram.008F}
A805: 4C 2D A8        JMP     $A82D               ; {}
A808: A2 08           LDX     #$08                ; 
A80A: A0 0A           LDY     #$0A                ; 
A80C: BD 00 E4        LDA     $E400,X             ; 
A80F: 85 00           STA     <$00                ; {ram.GP_00}
A811: BD 01 E4        LDA     $E401,X             ; 
A814: 85 01           STA     <$01                ; {ram.GP_01}
A816: B1 00           LDA     ($00),Y             ; {ram.GP_00}
A818: C9 B0           CMP     #$B0                ; 
A81A: F0 08           BEQ     $A824               ; {}
A81C: E8              INX                         ; 
A81D: E8              INX                         ; 
A81E: E8              INX                         ; 
A81F: E8              INX                         ; 
A820: E0 34           CPX     #$34                ; 
A822: D0 E8           BNE     $A80C               ; {}
A824: 8A              TXA                         ; 
A825: 0A              ASL     A                   ; 
A826: 0A              ASL     A                   ; 
A827: 85 7B           STA     <$7B                ; {ram.007B}
A829: A9 90           LDA     #$90                ; 
A82B: 85 8F           STA     <$8F                ; {ram.008F}
A82D: A9 68           LDA     #$68                ; 
A82F: 8D 5A 03        STA     $035A               ; {ram.035A}
A832: 60              RTS                         ; 
A833: A9 04           LDA     #$04                ; 
A835: 8D 00 06        STA     $0600               ; {ram.SND_ReqMusic}
A838: A9 20           LDA     #$20                ; 
A83A: 85 7C           STA     <$7C                ; {ram.007C}
A83C: A9 01           LDA     #$01                ; 
A83E: 85 7D           STA     <$7D                ; {ram.007D}
A840: A9 30           LDA     #$30                ; 
A842: 85 28           STA     <$28                ; {ram.0028}
A844: A9 24           LDA     #$24                ; 
A846: 85 0A           STA     <$0A                ; {ram.000A}
A848: 20 D8 E8        JSR     $E8D8               ; 
A84B: E6 11           INC     <$11                ; {ram.0011}
A84D: 20 1D 6E        JSR     $6E1D               ; {ram.6E1D}
A850: A9 1B           LDA     #$1B                ; 
A852: 8D 05 05        STA     $0505               ; {ram.0505}
A855: 4C 0C E8        JMP     $E80C               ; 
A858: 20 1D 6E        JSR     $6E1D               ; {ram.6E1D}
A85B: 20 17 E8        JSR     $E817               ; 
A85E: A5 13           LDA     <$13                ; {ram.0013}
A860: 20 E2 E5        JSR     $E5E2               ; 
A863: 6D A8 77        ADC     $77A8               ; {ram.77A8}
A866: A8              TAY                         ; 
A867: 8F                              ;
A868: A8              TAY                         ; 
A869: 97                              ;
A86A: A8              TAY                         ; 
A86B: AB                              ;
A86C: A8              TAY                         ; 
A86D: A5 28           LDA     <$28                ; {ram.0028}
A86F: D0 16           BNE     $A887               ; {}
A871: A9 30           LDA     #$30                ; 
A873: 85 28           STA     <$28                ; {ram.0028}
A875: D0 15           BNE     $A88C               ; {}
A877: A0 18           LDY     #$18                ; 
A879: A5 28           LDA     <$28                ; {ram.0028}
A87B: F0 0B           BEQ     $A888               ; {}
A87D: 29 07           AND     #$07                ; 
A87F: C9 04           CMP     #$04                ; 
A881: 90 02           BCC     $A885               ; {}
A883: A0 78           LDY     #$78                ; 
A885: 84 14           STY     <$14                ; {ram.0014}
A887: 60              RTS                         ; 
A888: A9 02           LDA     #$02                ; 
A88A: 85 63           STA     <$63                ; {ram.0063}
A88C: E6 13           INC     <$13                ; {ram.0013}
A88E: 60              RTS                         ; 
A88F: 20 89 ED        JSR     $ED89               ; 
A892: A5 63           LDA     <$63                ; {ram.0063}
A894: F0 0E           BEQ     $A8A4               ; {}
A896: 60              RTS                         ; 
A897: A5 28           LDA     <$28                ; {ram.0028}
A899: D0 0F           BNE     $A8AA               ; {}
A89B: 20 48 72        JSR     $7248               ; {ram.7248}
A89E: A5 7C           LDA     <$7C                ; {ram.007C}
A8A0: C9 11           CMP     #$11                ; 
A8A2: B0 06           BCS     $A8AA               ; {}
A8A4: A9 80           LDA     #$80                ; 
A8A6: 85 28           STA     <$28                ; {ram.0028}
A8A8: E6 13           INC     <$13                ; {ram.0013}
A8AA: 60              RTS                         ; 
A8AB: A5 28           LDA     <$28                ; {ram.0028}
A8AD: D0 FB           BNE     $A8AA               ; {}
A8AF: 20 F7 E5        JSR     $E5F7               ; 
A8B2: A5 FF           LDA     <$FF                ; {ram.CUR_2000}
A8B4: 29 FB           AND     #$FB                ; 
A8B6: 85 FF           STA     <$FF                ; {ram.CUR_2000}
A8B8: 8D 00 20        STA     $2000               ; {hard.P_CNTRL_1} [NES] PPU setup #1
A8BB: 4C 47 B5        JMP     $B547               ; {}
A8BE: 20 F4 A9        JSR     $A9F4               ; {}
A8C1: 4C 73 AB        JMP     $AB73               ; {}
A8C4: 20 30 AB        JSR     $AB30               ; {}
A8C7: A5 10           LDA     <$10                ; {ram.0010}
A8C9: F0 F3           BEQ     $A8BE               ; {}
A8CB: A9 F6           LDA     #$F6                ; 
A8CD: 85 0A           STA     <$0A                ; {ram.000A}
A8CF: 20 D8 E8        JSR     $E8D8               ; 
A8D2: 20 6C B6        JSR     $B66C               ; {}
A8D5: 20 42 A4        JSR     $A442               ; {}
A8D8: 20 F6 A4        JSR     $A4F6               ; {}
A8DB: 4C 20 A7        JMP     $A720               ; {}
A8DE: A9 1A           LDA     #$1A                ; 
A8E0: 85 00           STA     <$00                ; {ram.GP_00}
A8E2: A9 65           LDA     #$65                ; 
A8E4: 85 01           STA     <$01                ; {ram.GP_01}
A8E6: A6 E8           LDX     <$E8                ; {ram.00E8}
A8E8: CA              DEX                         ; 
A8E9: 8A              TXA                         ; 
A8EA: AC 01 03        LDY     $0301               ; {ram.0301}
A8ED: 99 03 03        STA     $0303,Y             ; {ram.0303}
A8F0: A9 21           LDA     #$21                ; 
A8F2: 99 02 03        STA     $0302,Y             ; {ram.0302}
A8F5: A9 16           LDA     #$16                ; 
A8F7: 20 76 72        JSR     $7276               ; {ram.7276}
A8FA: CA              DEX                         ; 
A8FB: 10 F8           BPL     $A8F5               ; {}
A8FD: A9 96           LDA     #$96                ; 
A8FF: 99 04 03        STA     $0304,Y             ; {ram.0304}
A902: 8A              TXA                         ; 
A903: 99 1B 03        STA     $031B,Y             ; 
A906: 98              TYA                         ; 
A907: AA              TAX                         ; 
A908: A0 00           LDY     #$00                ; 
A90A: 84 06           STY     <$06                ; {ram.0006}
A90C: B1 00           LDA     ($00),Y             ; {ram.GP_00}
A90E: 9D 05 03        STA     $0305,X             ; {ram.!BckGndBuf}
A911: 20 74 72        JSR     $7274               ; {ram.7274}
A914: E8              INX                         ; 
A915: E6 06           INC     <$06                ; {ram.0006}
A917: A5 06           LDA     <$06                ; {ram.0006}
A919: C9 16           CMP     #$16                ; 
A91B: 90 EF           BCC     $A90C               ; {}
A91D: E8              INX                         ; 
A91E: E8              INX                         ; 
A91F: E8              INX                         ; 
A920: 8E 01 03        STX     $0301               ; {ram.0301}
A923: 60              RTS                         ; 
A924: A9 65           LDA     #$65                ; 
A926: 85 01           STA     <$01                ; {ram.GP_01}
A928: A5 E9           LDA     <$E9                ; {ram.00E9}
A92A: AA              TAX                         ; 
A92B: 18              CLC                         ; 
A92C: 69 30           ADC     #$30                ; 
A92E: 85 00           STA     <$00                ; {ram.GP_00}
A930: 90 02           BCC     $A934               ; {}
A932: E6 01           INC     <$01                ; {ram.GP_01}
A934: A9 20           LDA     #$20                ; 
A936: 8D 02 03        STA     $0302               ; {ram.0302}
A939: A9 E0           LDA     #$E0                ; 
A93B: 8D 03 03        STA     $0303               ; {ram.0303}
A93E: AD 03 03        LDA     $0303               ; {ram.0303}
A941: 18              CLC                         ; 
A942: 69 20           ADC     #$20                ; 
A944: 8D 03 03        STA     $0303               ; {ram.0303}
A947: 90 03           BCC     $A94C               ; {}
A949: EE 02 03        INC     $0302               ; {ram.0302}
A94C: CA              DEX                         ; 
A94D: 10 EF           BPL     $A93E               ; {}
A94F: A9 20           LDA     #$20                ; 
A951: 8D 04 03        STA     $0304               ; {ram.0304}
A954: 8E 25 03        STX     $0325               ; {ram.0325}
A957: A2 00           LDX     #$00                ; 
A959: A0 00           LDY     #$00                ; 
A95B: B1 00           LDA     ($00),Y             ; {ram.GP_00}
A95D: 9D 05 03        STA     $0305,X             ; {ram.!BckGndBuf}
A960: A9 16           LDA     #$16                ; 
A962: 20 76 72        JSR     $7276               ; {ram.7276}
A965: E8              INX                         ; 
A966: E0 20           CPX     #$20                ; 
A968: 90 F1           BCC     $A95B               ; {}
A96A: A9 23           LDA     #$23                ; 
A96C: 8D 01 03        STA     $0301               ; {ram.0301}
A96F: 60              RTS                         ; 
A970: 62                              ;
A971: 63                              ;
A972: 64                              ;
A973: 65 66           ADC     <$66                ; {ram.SND_PtrA}
A975: 67                              ;
A976: C8              INY                         ; 
A977: D8              CLD                         ; 
A978: C4 BC           CPY     <$BC                ; {ram.00BC}
A97A: C0 C0           CPY     #$C0                ; 
A97C: 24 6F           BIT     <$6F                ; {ram.SND_MusEffCnt}
A97E: F3                              ;
A97F: FA                              ;
A980: 98              TYA                         ; 
A981: 90 8F           BCC     $A912               ; {}
A983: 95 8E           STA     $8E,X               ; 
A985: 90 74           BCC     $A9FB               ; {}
A987: 76 F3           ROR     <$F3,X              ; {ram.00F3}
A989: 24 26           BIT     <$26                ; {ram.0026}
A98B: 89                              ;
A98C: 03                              ;
A98D: 04                              ;
A98E: 70 C8           BVS     $A958               ; {}
A990: BC 8D 8F        LDY     $8F8D,X             ; {}
A993: 93                              ;
A994: 95 C4           STA     $C4,X               ; {ram.00C4}
A996: CE D8 B0        DEC     $B0D8               ; {}
A999: B4 AA           LDY     $AA,X               ; 
A99B: AC B8 9C        LDY     $9CB8               ; {}
A99E: A6 9A           LDX     <$9A                ; {ram.009A}
A9A0: A2 A0           LDX     #$A0                ; 
A9A2: E5 E6           SBC     <$E6                ; {ram.00E6}
A9A4: E7                              ;
A9A5: E8              INX                         ; 
A9A6: E9 EA           SBC     #$EA                ; 
A9A8: C0 E0           CPY     #$E0                ; 
A9AA: 78              SEI                         ; 
A9AB: 7A                              ;
A9AC: 7E 80 CC        ROR     $CC80,X             ; 
A9AF: D0 D4           BNE     $A985               ; {}
A9B1: DC                              ;
A9B2: 89                              ;
A9B3: 84 24           STY     <$24                ; {ram.0024}
A9B5: 24 24           BIT     <$24                ; {ram.0024}
A9B7: 24 6F           BIT     <$6F                ; {ram.SND_MusEffCnt}
A9B9: 6F                              ;
A9BA: 6F                              ;
A9BB: 6F                              ;
A9BC: F3                              ;
A9BD: F3                              ;
A9BE: F3                              ;
A9BF: F3                              ;
A9C0: FA                              ;
A9C1: FA                              ;
A9C2: FA                              ;
A9C3: FA                              ;
A9C4: 98              TYA                         ; 
A9C5: 95 26           STA     $26,X               ; {ram.0026}
A9C7: 26 90           ROL     <$90                ; {ram.0090}
A9C9: 95 90           STA     $90,X               ; {ram.0090}
A9CB: 95 8F           STA     $8F,X               ; {ram.008F}
A9CD: 90 8F           BCC     $A95E               ; {}
A9CF: 90 95           BCC     $A966               ; {}
A9D1: 96 95           STX     $95,Y               ; {ram.0095}
A9D3: 96 8E           STX     $8E,Y               ; 
A9D5: 93                              ;
A9D6: 90 95           BCC     $A96D               ; {}
A9D8: 90 95           BCC     $A96F               ; {}
A9DA: 92                              ;
A9DB: 97                              ;
A9DC: 74                              ;
A9DD: 74                              ;
A9DE: 75 75           ADC     <$75,X              ; {ram.0075}
A9E0: 76 77           ROR     <$77,X              ; {ram.0077}
A9E2: 76 77           ROR     <$77,X              ; {ram.0077}
A9E4: F3                              ;
A9E5: 24 F3           BIT     <$F3                ; {ram.00F3}
A9E7: 24 24           BIT     <$24                ; {ram.0024}
A9E9: 24 24           BIT     <$24                ; {ram.0024}
A9EB: 24 26           BIT     <$26                ; {ram.0026}
A9ED: 26 26           ROL     <$26                ; {ram.0026}
A9EF: 26 89           ROL     <$89                ; {ram.0089}
A9F1: 88              DEY                         ; 
A9F2: 8B                              ;
A9F3: 88              DEY                         ; 
A9F4: AD 9C 9F        LDA     $9F9C               ; {}
A9F7: 85 02           STA     <$02                ; {ram.GP_02}
A9F9: AD 9D 9F        LDA     $9F9D               ; {}
A9FC: 85 03           STA     <$03                ; {ram.GP_03}
A9FE: A9 00           LDA     #$00                ; 
AA00: 85 06           STA     <$06                ; {ram.0006}
AA02: A6 EB           LDX     <$EB                ; {ram.00EB}
AA04: BD FE 69        LDA     $69FE,X             ; 
AA07: 0A              ASL     A                   ; 
AA08: 0A              ASL     A                   ; 
AA09: 26 06           ROL     <$06                ; {ram.0006}
AA0B: 0A              ASL     A                   ; 
AA0C: 26 06           ROL     <$06                ; {ram.0006}
AA0E: 0A              ASL     A                   ; 
AA0F: 26 06           ROL     <$06                ; {ram.0006}
AA11: 65 02           ADC     <$02                ; {ram.GP_02}
AA13: 85 02           STA     <$02                ; {ram.GP_02}
AA15: A5 06           LDA     <$06                ; {ram.0006}
AA17: 65 03           ADC     <$03                ; {ram.GP_03}
AA19: 85 03           STA     <$03                ; {ram.GP_03}
AA1B: AD AF 6B        LDA     $6BAF               ; {ram.6BAF}
AA1E: 85 08           STA     <$08                ; {ram.0008}
AA20: AD B0 6B        LDA     $6BB0               ; {ram.6BB0}
AA23: 85 09           STA     <$09                ; {ram.0009}
AA25: 20 07 AC        JSR     $AC07               ; {}
AA28: A9 00           LDA     #$00                ; 
AA2A: 85 0C           STA     <$0C                ; {ram.000C}
AA2C: 85 06           STA     <$06                ; {ram.0006}
AA2E: A4 06           LDY     <$06                ; {ram.0006}
AA30: B1 02           LDA     ($02),Y             ; {ram.GP_02}
AA32: 29 F0           AND     #$F0                ; 
AA34: 4A              LSR     A                   ; 
AA35: 4A              LSR     A                   ; 
AA36: 4A              LSR     A                   ; 
AA37: AA              TAX                         ; 
AA38: BD 27 68        LDA     $6827,X             ; {ram.6827}
AA3B: 85 04           STA     <$04                ; {ram.0004}
AA3D: BD 28 68        LDA     $6828,X             ; {ram.6828}
AA40: 85 05           STA     <$05                ; {ram.0005}
AA42: B1 02           LDA     ($02),Y             ; {ram.GP_02}
AA44: 29 0F           AND     #$0F                ; 
AA46: AA              TAX                         ; 
AA47: A0 FF           LDY     #$FF                ; 
AA49: C8              INY                         ; 
AA4A: B1 04           LDA     ($04),Y             ; {ram.0004}
AA4C: 10 FB           BPL     $AA49               ; {}
AA4E: CA              DEX                         ; 
AA4F: 10 F8           BPL     $AA49               ; {}
AA51: 98              TYA                         ; 
AA52: 20 8E 72        JSR     $728E               ; {ram.728E}
AA55: A9 00           LDA     #$00                ; 
AA57: 85 07           STA     <$07                ; {ram.0007}
AA59: A0 00           LDY     #$00                ; 
AA5B: B1 04           LDA     ($04),Y             ; {ram.0004}
AA5D: 29 3F           AND     #$3F                ; 
AA5F: 85 0D           STA     <$0D                ; {ram.000D}
AA61: AA              TAX                         ; 
AA62: BD 7C A9        LDA     $A97C,X             ; {}
AA65: 48              PHA                         ; 
AA66: A4 EB           LDY     <$EB                ; {ram.00EB}
AA68: B1 08           LDA     ($08),Y             ; {ram.0008}
AA6A: 29 80           AND     #$80                ; 
AA6C: F0 1A           BEQ     $AA88               ; {}
AA6E: 68              PLA                         ; 
AA6F: C9 E7           CMP     #$E7                ; 
AA71: F0 08           BEQ     $AA7B               ; {}
AA73: C9 E6           CMP     #$E6                ; 
AA75: F0 0C           BEQ     $AA83               ; {}
AA77: C9 EA           CMP     #$EA                ; 
AA79: D0 0C           BNE     $AA87               ; {}
AA7B: A9 10           LDA     #$10                ; 
AA7D: 85 0D           STA     <$0D                ; {ram.000D}
AA7F: A9 70           LDA     #$70                ; 
AA81: D0 04           BNE     $AA87               ; {}
AA83: A9 0C           LDA     #$0C                ; 
AA85: 85 0D           STA     <$0D                ; {ram.000D}
AA87: 48              PHA                         ; 
AA88: 68              PLA                         ; 
AA89: 20 BF AA        JSR     $AABF               ; {}
AA8C: A0 00           LDY     #$00                ; 
AA8E: 20 F1 AA        JSR     $AAF1               ; {}
AA91: A9 02           LDA     #$02                ; 
AA93: 20 76 72        JSR     $7276               ; {ram.7276}
AA96: A0 00           LDY     #$00                ; 
AA98: B1 04           LDA     ($04),Y             ; {ram.0004}
AA9A: 29 40           AND     #$40                ; 
AA9C: F0 06           BEQ     $AAA4               ; {}
AA9E: 45 0C           EOR     <$0C                ; {ram.000C}
AAA0: 85 0C           STA     <$0C                ; {ram.000C}
AAA2: D0 03           BNE     $AAA7               ; {}
AAA4: 20 8C 72        JSR     $728C               ; {ram.728C}
AAA7: E6 07           INC     <$07                ; {ram.0007}
AAA9: A5 07           LDA     <$07                ; {ram.0007}
AAAB: C9 0B           CMP     #$0B                ; 
AAAD: D0 AA           BNE     $AA59               ; {}
AAAF: A9 16           LDA     #$16                ; 
AAB1: 20 76 72        JSR     $7276               ; {ram.7276}
AAB4: E6 06           INC     <$06                ; {ram.0006}
AAB6: A5 06           LDA     <$06                ; {ram.0006}
AAB8: C9 10           CMP     #$10                ; 
AABA: B0 34           BCS     $AAF0               ; {}
AABC: 4C 2E AA        JMP     $AA2E               ; {}
AABF: A2 EA           LDX     #$EA                ; 
AAC1: 86 0A           STX     <$0A                ; {ram.000A}
AAC3: A2 05           LDX     #$05                ; 
AAC5: C5 0A           CMP     <$0A                ; {ram.000A}
AAC7: F0 07           BEQ     $AAD0               ; {}
AAC9: C6 0A           DEC     <$0A                ; {ram.000A}
AACB: CA              DEX                         ; 
AACC: 10 F7           BPL     $AAC5               ; {}
AACE: 30 20           BMI     $AAF0               ; {}
AAD0: BD 76 A9        LDA     $A976,X             ; {}
AAD3: 48              PHA                         ; 
AAD4: BD 70 A9        LDA     $A970,X             ; {}
AAD7: 8D 2B 05        STA     $052B               ; {ram.052B}
AADA: A5 06           LDA     <$06                ; {ram.0006}
AADC: 0A              ASL     A                   ; 
AADD: 0A              ASL     A                   ; 
AADE: 0A              ASL     A                   ; 
AADF: 0A              ASL     A                   ; 
AAE0: 8D 2C 05        STA     $052C               ; {ram.052C}
AAE3: A5 07           LDA     <$07                ; {ram.0007}
AAE5: 0A              ASL     A                   ; 
AAE6: 0A              ASL     A                   ; 
AAE7: 0A              ASL     A                   ; 
AAE8: 0A              ASL     A                   ; 
AAE9: 18              CLC                         ; 
AAEA: 69 40           ADC     #$40                ; 
AAEC: 8D 2D 05        STA     $052D               ; {ram.052D}
AAEF: 68              PLA                         ; 
AAF0: 60              RTS                         ; 
AAF1: A6 0D           LDX     <$0D                ; {ram.000D}
AAF3: E0 10           CPX     #$10                ; 
AAF5: 90 17           BCC     $AB0E               ; {}
AAF7: AA              TAX                         ; 
AAF8: 91 00           STA     ($00),Y             ; {ram.GP_00}
AAFA: C8              INY                         ; 
AAFB: E8              INX                         ; 
AAFC: 8A              TXA                         ; 
AAFD: 91 00           STA     ($00),Y             ; {ram.GP_00}
AAFF: 98              TYA                         ; 
AB00: 18              CLC                         ; 
AB01: 69 15           ADC     #$15                ; 
AB03: A8              TAY                         ; 
AB04: E8              INX                         ; 
AB05: 8A              TXA                         ; 
AB06: 91 00           STA     ($00),Y             ; {ram.GP_00}
AB08: E8              INX                         ; 
AB09: 8A              TXA                         ; 
AB0A: C8              INY                         ; 
AB0B: 91 00           STA     ($00),Y             ; {ram.GP_00}
AB0D: 60              RTS                         ; 
AB0E: 8A              TXA                         ; 
AB0F: 0A              ASL     A                   ; 
AB10: 0A              ASL     A                   ; 
AB11: AA              TAX                         ; 
AB12: BD B4 A9        LDA     $A9B4,X             ; {}
AB15: 91 00           STA     ($00),Y             ; {ram.GP_00}
AB17: C8              INY                         ; 
AB18: E8              INX                         ; 
AB19: BD B4 A9        LDA     $A9B4,X             ; {}
AB1C: 91 00           STA     ($00),Y             ; {ram.GP_00}
AB1E: 98              TYA                         ; 
AB1F: 18              CLC                         ; 
AB20: 69 15           ADC     #$15                ; 
AB22: A8              TAY                         ; 
AB23: E8              INX                         ; 
AB24: BD B4 A9        LDA     $A9B4,X             ; {}
AB27: 91 00           STA     ($00),Y             ; {ram.GP_00}
AB29: E8              INX                         ; 
AB2A: BD B4 A9        LDA     $A9B4,X             ; {}
AB2D: 4C 0A AB        JMP     $AB0A               ; {}
AB30: AD 9E 9F        LDA     $9F9E               ; {}
AB33: AE 9F 9F        LDX     $9F9F               ; {}
AB36: A4 10           LDY     <$10                ; {ram.0010}
AB38: F0 04           BEQ     $AB3E               ; {}
AB3A: A9 D4           LDA     #$D4                ; 
AB3C: A2 A3           LDX     #$A3                ; 
AB3E: 8D 27 68        STA     $6827               ; {ram.6827}
AB41: 8E 28 68        STX     $6828               ; {ram.6828}
AB44: 60              RTS                         ; 
AB45: A8              TAY                         ; 
AB46: 9B                              ;
AB47: B8              CLV                         ; 
AB48: 9B                              ;
AB49: B4 A3           LDY     $A3,X               ; {ram.00A3}
AB4B: C4 A3           CPY     <$A3                ; {ram.00A3}
AB4D: A2 00           LDX     #$00                ; 
AB4F: BD 45 AB        LDA     $AB45,X             ; {}
AB52: 85 02           STA     <$02                ; {ram.GP_02}
AB54: BD 46 AB        LDA     $AB46,X             ; {}
AB57: 85 03           STA     <$03                ; {ram.GP_03}
AB59: E6 13           INC     <$13                ; {ram.0013}
AB5B: 4C 1B AA        JMP     $AA1B               ; {}
AB5E: A2 02           LDX     #$02                ; 
AB60: D0 ED           BNE     $AB4F               ; {}
AB62: A9 00           LDA     #$00                ; 
AB64: 85 E9           STA     <$E9                ; {ram.00E9}
AB66: A2 04           LDX     #$04                ; 
AB68: 20 5A E8        JSR     $E85A               ; 
AB6B: 29 01           AND     #$01                ; 
AB6D: F0 E0           BEQ     $AB4F               ; {}
AB6F: A2 06           LDX     #$06                ; 
AB71: D0 DC           BNE     $AB4F               ; {}
AB73: 20 CE E6        JSR     $E6CE               ; 
AB76: 0A              ASL     A                   ; 
AB77: B0 42           BCS     $ABBB               ; {}
AB79: B1 00           LDA     ($00),Y             ; {ram.GP_00}
AB7B: 29 20           AND     #$20                ; 
AB7D: F0 3C           BEQ     $ABBB               ; {}
AB7F: 20 07 AC        JSR     $AC07               ; {}
AB82: 20 8A 71        JSR     $718A               ; {ram.718A}
AB85: 4A              LSR     A                   ; 
AB86: 4A              LSR     A                   ; 
AB87: AA              TAX                         ; 
AB88: BD 00 E4        LDA     $E400,X             ; 
AB8B: 85 00           STA     <$00                ; {ram.GP_00}
AB8D: BD 01 E4        LDA     $E401,X             ; 
AB90: 85 01           STA     <$01                ; {ram.GP_01}
AB92: 98              TYA                         ; 
AB93: 38              SEC                         ; 
AB94: E9 40           SBC     #$40                ; 
AB96: 4A              LSR     A                   ; 
AB97: 4A              LSR     A                   ; 
AB98: 4A              LSR     A                   ; 
AB99: A8              TAY                         ; 
AB9A: B1 00           LDA     ($00),Y             ; {ram.GP_00}
AB9C: C9 C4           CMP     #$C4                ; 
AB9E: F0 1C           BEQ     $ABBC               ; {}
ABA0: C9 BC           CMP     #$BC                ; 
ABA2: F0 17           BEQ     $ABBB               ; {}
ABA4: C9 D8           CMP     #$D8                ; 
ABA6: D0 14           BNE     $ABBC               ; {}
ABA8: AD 2B 05        LDA     $052B               ; {ram.052B}
ABAB: C9 62           CMP     #$62                ; 
ABAD: F0 0D           BEQ     $ABBC               ; {}
ABAF: A9 00           LDA     #$00                ; 
ABB1: 8D 2B 05        STA     $052B               ; {ram.052B}
ABB4: A9 0C           LDA     #$0C                ; 
ABB6: 85 0D           STA     <$0D                ; {ram.000D}
ABB8: 20 F1 AA        JSR     $AAF1               ; {}
ABBB: 60              RTS                         ; 
ABBC: A9 10           LDA     #$10                ; 
ABBE: 85 0D           STA     <$0D                ; {ram.000D}
ABC0: A9 70           LDA     #$70                ; 
ABC2: D0 F4           BNE     $ABB8               ; {}
ABC4: 8A              TXA                         ; 
ABC5: 48              PHA                         ; 
ABC6: B5 70           LDA     $70,X               ; {ram.0070}
ABC8: 29 F0           AND     #$F0                ; 
ABCA: 4A              LSR     A                   ; 
ABCB: 4A              LSR     A                   ; 
ABCC: AA              TAX                         ; 
ABCD: BD 00 E4        LDA     $E400,X             ; 
ABD0: 85 00           STA     <$00                ; {ram.GP_00}
ABD2: BD 01 E4        LDA     $E401,X             ; 
ABD5: 85 01           STA     <$01                ; {ram.GP_01}
ABD7: 68              PLA                         ; 
ABD8: 48              PHA                         ; 
ABD9: AA              TAX                         ; 
ABDA: B5 84           LDA     $84,X               ; {ram.0084}
ABDC: 29 F0           AND     #$F0                ; 
ABDE: 38              SEC                         ; 
ABDF: E9 40           SBC     #$40                ; 
ABE1: 4A              LSR     A                   ; 
ABE2: 4A              LSR     A                   ; 
ABE3: 4A              LSR     A                   ; 
ABE4: 20 76 72        JSR     $7276               ; {ram.7276}
ABE7: A0 00           LDY     #$00                ; 
ABE9: A2 10           LDX     #$10                ; 
ABEB: A5 05           LDA     <$05                ; {ram.0005}
ABED: C9 27           CMP     #$27                ; 
ABEF: 90 04           BCC     $ABF5               ; {}
ABF1: C9 F3           CMP     #$F3                ; 
ABF3: 90 0A           BCC     $ABFF               ; {}
ABF5: A2 0E           LDX     #$0E                ; 
ABF7: DD 7C A9        CMP     $A97C,X             ; {}
ABFA: F0 03           BEQ     $ABFF               ; {}
ABFC: CA              DEX                         ; 
ABFD: D0 F8           BNE     $ABF7               ; {}
ABFF: 86 0D           STX     <$0D                ; {ram.000D}
AC01: 20 F1 AA        JSR     $AAF1               ; {}
AC04: 68              PLA                         ; 
AC05: AA              TAX                         ; 
AC06: 60              RTS                         ; 
AC07: A9 30           LDA     #$30                ; 
AC09: 85 00           STA     <$00                ; {ram.GP_00}
AC0B: A9 65           LDA     #$65                ; 
AC0D: 85 01           STA     <$01                ; {ram.GP_01}
AC0F: 60              RTS                         ; 
AC10: 20 16 AC        JSR     $AC16               ; {}
AC13: B0 12           BCS     $AC27               ; {}
AC15: 60              RTS                         ; 
AC16: 20 24 A9        JSR     $A924               ; {}
AC19: E6 E9           INC     <$E9                ; {ram.00E9}
AC1B: A5 E9           LDA     <$E9                ; {ram.00E9}
AC1D: C9 16           CMP     #$16                ; 
AC1F: 60              RTS                         ; 
AC20: 20 C4 A8        JSR     $A8C4               ; {}
AC23: A9 00           LDA     #$00                ; 
AC25: 85 E9           STA     <$E9                ; {ram.00E9}
AC27: E6 13           INC     <$13                ; {ram.0013}
AC29: 60              RTS                         ; 
AC2A: FF                              ;
AC2B: FF                              ;
AC2C: FF                              ;
AC2D: FF                              ;
AC2E: FF                              ;
AC2F: FF                              ;
AC30: FF                              ;
AC31: FF                              ;
AC32: FF                              ;
AC33: FF                              ;
AC34: FF                              ;
AC35: FF                              ;
AC36: FF                              ;
AC37: FF                              ;
AC38: FF                              ;
AC39: FF                              ;
AC3A: FF                              ;
AC3B: FF                              ;
AC3C: FF                              ;
AC3D: FF                              ;
AC3E: FF                              ;
AC3F: FF                              ;
AC40: FF                              ;
AC41: FF                              ;
AC42: FF                              ;
AC43: FF                              ;
AC44: FF                              ;
AC45: FF                              ;
AC46: FF                              ;
AC47: FF                              ;
AC48: FF                              ;
AC49: FF                              ;
AC4A: FF                              ;
AC4B: FF                              ;
AC4C: FF                              ;
AC4D: FF                              ;
AC4E: FF                              ;
AC4F: FF                              ;
AC50: FF                              ;
AC51: FF                              ;
AC52: FF                              ;
AC53: FF                              ;
AC54: FF                              ;
AC55: FF                              ;
AC56: FF                              ;
AC57: FF                              ;
AC58: FF                              ;
AC59: FF                              ;
AC5A: FF                              ;
AC5B: FF                              ;
AC5C: FF                              ;
AC5D: FF                              ;
AC5E: FF                              ;
AC5F: FF                              ;
AC60: FF                              ;
AC61: FF                              ;
AC62: FF                              ;
AC63: FF                              ;
AC64: FF                              ;
AC65: FF                              ;
AC66: FF                              ;
AC67: FF                              ;
AC68: FF                              ;
AC69: FF                              ;
AC6A: FF                              ;
AC6B: FF                              ;
AC6C: FF                              ;
AC6D: FF                              ;
AC6E: FF                              ;
AC6F: FF                              ;
AC70: FF                              ;
AC71: FF                              ;
AC72: FF                              ;
AC73: FF                              ;
AC74: FF                              ;
AC75: FF                              ;
AC76: FF                              ;
AC77: FF                              ;
AC78: FF                              ;
AC79: FF                              ;
AC7A: FF                              ;
AC7B: FF                              ;
AC7C: FF                              ;
AC7D: FF                              ;
AC7E: FF                              ;
AC7F: FF                              ;
AC80: FF                              ;
AC81: FF                              ;
AC82: FF                              ;
AC83: FF                              ;
AC84: FF                              ;
AC85: FF                              ;
AC86: FF                              ;
AC87: FF                              ;
AC88: FF                              ;
AC89: FF                              ;
AC8A: FF                              ;
AC8B: FF                              ;
AC8C: FF                              ;
AC8D: FF                              ;
AC8E: FF                              ;
AC8F: FF                              ;
AC90: FF                              ;
AC91: FF                              ;
AC92: FF                              ;
AC93: FF                              ;
AC94: FF                              ;
AC95: FF                              ;
AC96: FF                              ;
AC97: FF                              ;
AC98: FF                              ;
AC99: FF                              ;
AC9A: FF                              ;
AC9B: FF                              ;
AC9C: FF                              ;
AC9D: FF                              ;
AC9E: FF                              ;
AC9F: FF                              ;
ACA0: FF                              ;
ACA1: FF                              ;
ACA2: FF                              ;
ACA3: FF                              ;
ACA4: FF                              ;
ACA5: FF                              ;
ACA6: FF                              ;
ACA7: FF                              ;
ACA8: FF                              ;
ACA9: FF                              ;
ACAA: FF                              ;
ACAB: FF                              ;
ACAC: FF                              ;
ACAD: FF                              ;
ACAE: FF                              ;
ACAF: FF                              ;
ACB0: FF                              ;
ACB1: FF                              ;
ACB2: FF                              ;
ACB3: FF                              ;
ACB4: FF                              ;
ACB5: FF                              ;
ACB6: FF                              ;
ACB7: FF                              ;
ACB8: FF                              ;
ACB9: FF                              ;
ACBA: FF                              ;
ACBB: FF                              ;
ACBC: FF                              ;
ACBD: FF                              ;
ACBE: FF                              ;
ACBF: FF                              ;
ACC0: FF                              ;
ACC1: FF                              ;
ACC2: FF                              ;
ACC3: FF                              ;
ACC4: FF                              ;
ACC5: FF                              ;
ACC6: FF                              ;
ACC7: FF                              ;
ACC8: FF                              ;
ACC9: FF                              ;
ACCA: FF                              ;
ACCB: FF                              ;
ACCC: FF                              ;
ACCD: FF                              ;
ACCE: FF                              ;
ACCF: FF                              ;
ACD0: FF                              ;
ACD1: FF                              ;
ACD2: FF                              ;
ACD3: FF                              ;
ACD4: FF                              ;
ACD5: FF                              ;
ACD6: FF                              ;
ACD7: FF                              ;
ACD8: FF                              ;
ACD9: FF                              ;
ACDA: FF                              ;
ACDB: FF                              ;
ACDC: FF                              ;
ACDD: FF                              ;
ACDE: FF                              ;
ACDF: FF                              ;
ACE0: FF                              ;
ACE1: FF                              ;
ACE2: FF                              ;
ACE3: FF                              ;
ACE4: FF                              ;
ACE5: FF                              ;
ACE6: FF                              ;
ACE7: FF                              ;
ACE8: FF                              ;
ACE9: FF                              ;
ACEA: FF                              ;
ACEB: FF                              ;
ACEC: FF                              ;
ACED: FF                              ;
ACEE: FF                              ;
ACEF: FF                              ;
ACF0: FF                              ;
ACF1: FF                              ;
ACF2: FF                              ;
ACF3: FF                              ;
ACF4: FF                              ;
ACF5: FF                              ;
ACF6: FF                              ;
ACF7: FF                              ;
ACF8: FF                              ;
ACF9: FF                              ;
ACFA: FF                              ;
ACFB: FF                              ;
ACFC: FF                              ;
ACFD: FF                              ;
ACFE: FF                              ;
ACFF: FF                              ;
AD00: FF                              ;
AD01: FF                              ;
AD02: FF                              ;
AD03: FF                              ;
AD04: FF                              ;
AD05: FF                              ;
AD06: FF                              ;
AD07: FF                              ;
AD08: FF                              ;
AD09: FF                              ;
AD0A: FF                              ;
AD0B: FF                              ;
AD0C: FF                              ;
AD0D: FF                              ;
AD0E: FF                              ;
AD0F: FF                              ;
AD10: FF                              ;
AD11: FF                              ;
AD12: FF                              ;
AD13: FF                              ;
AD14: FF                              ;
AD15: FF                              ;
AD16: FF                              ;
AD17: FF                              ;
AD18: FF                              ;
AD19: FF                              ;
AD1A: FF                              ;
AD1B: FF                              ;
AD1C: FF                              ;
AD1D: FF                              ;
AD1E: FF                              ;
AD1F: FF                              ;
AD20: FF                              ;
AD21: FF                              ;
AD22: FF                              ;
AD23: FF                              ;
AD24: FF                              ;
AD25: FF                              ;
AD26: FF                              ;
AD27: FF                              ;
AD28: FF                              ;
AD29: FF                              ;
AD2A: FF                              ;
AD2B: FF                              ;
AD2C: FF                              ;
AD2D: FF                              ;
AD2E: FF                              ;
AD2F: FF                              ;
AD30: FF                              ;
AD31: FF                              ;
AD32: FF                              ;
AD33: FF                              ;
AD34: FF                              ;
AD35: FF                              ;
AD36: FF                              ;
AD37: FF                              ;
AD38: FF                              ;
AD39: FF                              ;
AD3A: FF                              ;
AD3B: FF                              ;
AD3C: FF                              ;
AD3D: FF                              ;
AD3E: FF                              ;
AD3F: FF                              ;
AD40: FF                              ;
AD41: FF                              ;
AD42: FF                              ;
AD43: FF                              ;
AD44: FF                              ;
AD45: FF                              ;
AD46: FF                              ;
AD47: FF                              ;
AD48: FF                              ;
AD49: FF                              ;
AD4A: FF                              ;
AD4B: FF                              ;
AD4C: FF                              ;
AD4D: FF                              ;
AD4E: FF                              ;
AD4F: FF                              ;
AD50: FF                              ;
AD51: FF                              ;
AD52: FF                              ;
AD53: FF                              ;
AD54: FF                              ;
AD55: FF                              ;
AD56: FF                              ;
AD57: FF                              ;
AD58: FF                              ;
AD59: FF                              ;
AD5A: FF                              ;
AD5B: FF                              ;
AD5C: FF                              ;
AD5D: FF                              ;
AD5E: FF                              ;
AD5F: FF                              ;
AD60: FF                              ;
AD61: FF                              ;
AD62: FF                              ;
AD63: FF                              ;
AD64: FF                              ;
AD65: FF                              ;
AD66: FF                              ;
AD67: FF                              ;
AD68: FF                              ;
AD69: FF                              ;
AD6A: FF                              ;
AD6B: FF                              ;
AD6C: FF                              ;
AD6D: FF                              ;
AD6E: FF                              ;
AD6F: FF                              ;
AD70: FF                              ;
AD71: FF                              ;
AD72: FF                              ;
AD73: FF                              ;
AD74: FF                              ;
AD75: FF                              ;
AD76: FF                              ;
AD77: FF                              ;
AD78: FF                              ;
AD79: FF                              ;
AD7A: FF                              ;
AD7B: FF                              ;
AD7C: FF                              ;
AD7D: FF                              ;
AD7E: FF                              ;
AD7F: FF                              ;
AD80: FF                              ;
AD81: FF                              ;
AD82: FF                              ;
AD83: FF                              ;
AD84: FF                              ;
AD85: FF                              ;
AD86: FF                              ;
AD87: FF                              ;
AD88: FF                              ;
AD89: FF                              ;
AD8A: FF                              ;
AD8B: FF                              ;
AD8C: FF                              ;
AD8D: FF                              ;
AD8E: FF                              ;
AD8F: FF                              ;
AD90: FF                              ;
AD91: FF                              ;
AD92: FF                              ;
AD93: FF                              ;
AD94: FF                              ;
AD95: FF                              ;
AD96: FF                              ;
AD97: FF                              ;
AD98: FF                              ;
AD99: FF                              ;
AD9A: FF                              ;
AD9B: FF                              ;
AD9C: FF                              ;
AD9D: FF                              ;
AD9E: FF                              ;
AD9F: FF                              ;
ADA0: FF                              ;
ADA1: FF                              ;
ADA2: FF                              ;
ADA3: FF                              ;
ADA4: FF                              ;
ADA5: FF                              ;
ADA6: FF                              ;
ADA7: FF                              ;
ADA8: FF                              ;
ADA9: FF                              ;
ADAA: FF                              ;
ADAB: FF                              ;
ADAC: FF                              ;
ADAD: FF                              ;
ADAE: FF                              ;
ADAF: FF                              ;
ADB0: FF                              ;
ADB1: FF                              ;
ADB2: FF                              ;
ADB3: FF                              ;
ADB4: FF                              ;
ADB5: FF                              ;
ADB6: FF                              ;
ADB7: FF                              ;
ADB8: FF                              ;
ADB9: FF                              ;
ADBA: FF                              ;
ADBB: FF                              ;
ADBC: FF                              ;
ADBD: FF                              ;
ADBE: FF                              ;
ADBF: FF                              ;
ADC0: FF                              ;
ADC1: FF                              ;
ADC2: FF                              ;
ADC3: FF                              ;
ADC4: FF                              ;
ADC5: FF                              ;
ADC6: FF                              ;
ADC7: FF                              ;
ADC8: FF                              ;
ADC9: FF                              ;
ADCA: FF                              ;
ADCB: FF                              ;
ADCC: FF                              ;
ADCD: FF                              ;
ADCE: FF                              ;
ADCF: FF                              ;
ADD0: FF                              ;
ADD1: FF                              ;
ADD2: FF                              ;
ADD3: FF                              ;
ADD4: FF                              ;
ADD5: FF                              ;
ADD6: FF                              ;
ADD7: FF                              ;
ADD8: FF                              ;
ADD9: FF                              ;
ADDA: FF                              ;
ADDB: FF                              ;
ADDC: FF                              ;
ADDD: FF                              ;
ADDE: FF                              ;
ADDF: FF                              ;
ADE0: FF                              ;
ADE1: FF                              ;
ADE2: FF                              ;
ADE3: FF                              ;
ADE4: FF                              ;
ADE5: FF                              ;
ADE6: FF                              ;
ADE7: FF                              ;
ADE8: FF                              ;
ADE9: FF                              ;
ADEA: FF                              ;
ADEB: FF                              ;
ADEC: FF                              ;
ADED: FF                              ;
ADEE: FF                              ;
ADEF: FF                              ;
ADF0: FF                              ;
ADF1: FF                              ;
ADF2: FF                              ;
ADF3: FF                              ;
ADF4: FF                              ;
ADF5: FF                              ;
ADF6: FF                              ;
ADF7: FF                              ;
ADF8: FF                              ;
ADF9: FF                              ;
ADFA: FF                              ;
ADFB: FF                              ;
ADFC: FF                              ;
ADFD: FF                              ;
ADFE: FF                              ;
ADFF: FF                              ;
AE00: FF                              ;
AE01: FF                              ;
AE02: FF                              ;
AE03: FF                              ;
AE04: FF                              ;
AE05: FF                              ;
AE06: FF                              ;
AE07: FF                              ;
AE08: FF                              ;
AE09: FF                              ;
AE0A: FF                              ;
AE0B: FF                              ;
AE0C: FF                              ;
AE0D: FF                              ;
AE0E: FF                              ;
AE0F: FF                              ;
AE10: FF                              ;
AE11: FF                              ;
AE12: FF                              ;
AE13: FF                              ;
AE14: FF                              ;
AE15: FF                              ;
AE16: FF                              ;
AE17: FF                              ;
AE18: FF                              ;
AE19: FF                              ;
AE1A: FF                              ;
AE1B: FF                              ;
AE1C: FF                              ;
AE1D: FF                              ;
AE1E: FF                              ;
AE1F: FF                              ;
AE20: FF                              ;
AE21: FF                              ;
AE22: FF                              ;
AE23: FF                              ;
AE24: FF                              ;
AE25: FF                              ;
AE26: FF                              ;
AE27: FF                              ;
AE28: FF                              ;
AE29: FF                              ;
AE2A: FF                              ;
AE2B: FF                              ;
AE2C: FF                              ;
AE2D: FF                              ;
AE2E: FF                              ;
AE2F: FF                              ;
AE30: FF                              ;
AE31: FF                              ;
AE32: FF                              ;
AE33: FF                              ;
AE34: FF                              ;
AE35: FF                              ;
AE36: FF                              ;
AE37: FF                              ;
AE38: FF                              ;
AE39: FF                              ;
AE3A: FF                              ;
AE3B: FF                              ;
AE3C: FF                              ;
AE3D: FF                              ;
AE3E: FF                              ;
AE3F: FF                              ;
AE40: FF                              ;
AE41: FF                              ;
AE42: FF                              ;
AE43: FF                              ;
AE44: FF                              ;
AE45: FF                              ;
AE46: FF                              ;
AE47: FF                              ;
AE48: FF                              ;
AE49: FF                              ;
AE4A: FF                              ;
AE4B: FF                              ;
AE4C: FF                              ;
AE4D: FF                              ;
AE4E: FF                              ;
AE4F: FF                              ;
AE50: FF                              ;
AE51: FF                              ;
AE52: FF                              ;
AE53: FF                              ;
AE54: FF                              ;
AE55: FF                              ;
AE56: FF                              ;
AE57: FF                              ;
AE58: FF                              ;
AE59: FF                              ;
AE5A: FF                              ;
AE5B: FF                              ;
AE5C: FF                              ;
AE5D: FF                              ;
AE5E: FF                              ;
AE5F: FF                              ;
AE60: FF                              ;
AE61: FF                              ;
AE62: FF                              ;
AE63: FF                              ;
AE64: FF                              ;
AE65: FF                              ;
AE66: FF                              ;
AE67: FF                              ;
AE68: FF                              ;
AE69: FF                              ;
AE6A: FF                              ;
AE6B: FF                              ;
AE6C: FF                              ;
AE6D: FF                              ;
AE6E: FF                              ;
AE6F: FF                              ;
AE70: FF                              ;
AE71: FF                              ;
AE72: FF                              ;
AE73: FF                              ;
AE74: FF                              ;
AE75: FF                              ;
AE76: FF                              ;
AE77: FF                              ;
AE78: FF                              ;
AE79: FF                              ;
AE7A: FF                              ;
AE7B: FF                              ;
AE7C: FF                              ;
AE7D: FF                              ;
AE7E: FF                              ;
AE7F: FF                              ;
AE80: FF                              ;
AE81: FF                              ;
AE82: FF                              ;
AE83: FF                              ;
AE84: FF                              ;
AE85: FF                              ;
AE86: FF                              ;
AE87: FF                              ;
AE88: FF                              ;
AE89: FF                              ;
AE8A: FF                              ;
AE8B: FF                              ;
AE8C: FF                              ;
AE8D: FF                              ;
AE8E: FF                              ;
AE8F: FF                              ;
AE90: FF                              ;
AE91: FF                              ;
AE92: FF                              ;
AE93: FF                              ;
AE94: FF                              ;
AE95: FF                              ;
AE96: FF                              ;
AE97: FF                              ;
AE98: FF                              ;
AE99: FF                              ;
AE9A: FF                              ;
AE9B: FF                              ;
AE9C: FF                              ;
AE9D: FF                              ;
AE9E: FF                              ;
AE9F: FF                              ;
AEA0: FF                              ;
AEA1: FF                              ;
AEA2: FF                              ;
AEA3: FF                              ;
AEA4: FF                              ;
AEA5: FF                              ;
AEA6: FF                              ;
AEA7: FF                              ;
AEA8: FF                              ;
AEA9: FF                              ;
AEAA: FF                              ;
AEAB: FF                              ;
AEAC: FF                              ;
AEAD: FF                              ;
AEAE: FF                              ;
AEAF: FF                              ;
AEB0: FF                              ;
AEB1: FF                              ;
AEB2: FF                              ;
AEB3: FF                              ;
AEB4: FF                              ;
AEB5: FF                              ;
AEB6: FF                              ;
AEB7: FF                              ;
AEB8: FF                              ;
AEB9: FF                              ;
AEBA: FF                              ;
AEBB: FF                              ;
AEBC: FF                              ;
AEBD: FF                              ;
AEBE: FF                              ;
AEBF: FF                              ;
AEC0: FF                              ;
AEC1: FF                              ;
AEC2: FF                              ;
AEC3: FF                              ;
AEC4: FF                              ;
AEC5: FF                              ;
AEC6: FF                              ;
AEC7: FF                              ;
AEC8: FF                              ;
AEC9: FF                              ;
AECA: FF                              ;
AECB: FF                              ;
AECC: FF                              ;
AECD: FF                              ;
AECE: FF                              ;
AECF: FF                              ;
AED0: FF                              ;
AED1: FF                              ;
AED2: FF                              ;
AED3: FF                              ;
AED4: FF                              ;
AED5: FF                              ;
AED6: FF                              ;
AED7: FF                              ;
AED8: FF                              ;
AED9: FF                              ;
AEDA: FF                              ;
AEDB: FF                              ;
AEDC: FF                              ;
AEDD: FF                              ;
AEDE: FF                              ;
AEDF: FF                              ;
AEE0: FF                              ;
AEE1: FF                              ;
AEE2: FF                              ;
AEE3: FF                              ;
AEE4: FF                              ;
AEE5: FF                              ;
AEE6: FF                              ;
AEE7: FF                              ;
AEE8: FF                              ;
AEE9: FF                              ;
AEEA: FF                              ;
AEEB: FF                              ;
AEEC: FF                              ;
AEED: FF                              ;
AEEE: FF                              ;
AEEF: FF                              ;
AEF0: FF                              ;
AEF1: FF                              ;
AEF2: FF                              ;
AEF3: FF                              ;
AEF4: FF                              ;
AEF5: FF                              ;
AEF6: FF                              ;
AEF7: FF                              ;
AEF8: FF                              ;
AEF9: FF                              ;
AEFA: FF                              ;
AEFB: FF                              ;
AEFC: FF                              ;
AEFD: FF                              ;
AEFE: FF                              ;
AEFF: FF                              ;
AF00: FF                              ;
AF01: FF                              ;
AF02: FF                              ;
AF03: FF                              ;
AF04: FF                              ;
AF05: FF                              ;
AF06: FF                              ;
AF07: FF                              ;
AF08: FF                              ;
AF09: FF                              ;
AF0A: FF                              ;
AF0B: FF                              ;
AF0C: FF                              ;
AF0D: FF                              ;
AF0E: FF                              ;
AF0F: FF                              ;
AF10: FF                              ;
AF11: FF                              ;
AF12: FF                              ;
AF13: FF                              ;
AF14: FF                              ;
AF15: FF                              ;
AF16: FF                              ;
AF17: FF                              ;
AF18: FF                              ;
AF19: FF                              ;
AF1A: FF                              ;
AF1B: FF                              ;
AF1C: FF                              ;
AF1D: FF                              ;
AF1E: FF                              ;
AF1F: FF                              ;
AF20: FF                              ;
AF21: FF                              ;
AF22: FF                              ;
AF23: FF                              ;
AF24: FF                              ;
AF25: FF                              ;
AF26: FF                              ;
AF27: FF                              ;
AF28: FF                              ;
AF29: FF                              ;
AF2A: FF                              ;
AF2B: FF                              ;
AF2C: FF                              ;
AF2D: FF                              ;
AF2E: FF                              ;
AF2F: FF                              ;
AF30: FF                              ;
AF31: FF                              ;
AF32: FF                              ;
AF33: FF                              ;
AF34: FF                              ;
AF35: FF                              ;
AF36: FF                              ;
AF37: FF                              ;
AF38: FF                              ;
AF39: FF                              ;
AF3A: FF                              ;
AF3B: FF                              ;
AF3C: FF                              ;
AF3D: FF                              ;
AF3E: FF                              ;
AF3F: FF                              ;
AF40: FF                              ;
AF41: FF                              ;
AF42: FF                              ;
AF43: FF                              ;
AF44: FF                              ;
AF45: FF                              ;
AF46: FF                              ;
AF47: FF                              ;
AF48: FF                              ;
AF49: FF                              ;
AF4A: FF                              ;
AF4B: FF                              ;
AF4C: FF                              ;
AF4D: FF                              ;
AF4E: FF                              ;
AF4F: FF                              ;
AF50: FF                              ;
AF51: FF                              ;
AF52: FF                              ;
AF53: FF                              ;
AF54: FF                              ;
AF55: FF                              ;
AF56: FF                              ;
AF57: FF                              ;
AF58: FF                              ;
AF59: FF                              ;
AF5A: FF                              ;
AF5B: FF                              ;
AF5C: FF                              ;
AF5D: FF                              ;
AF5E: FF                              ;
AF5F: FF                              ;
AF60: FF                              ;
AF61: FF                              ;
AF62: FF                              ;
AF63: FF                              ;
AF64: FF                              ;
AF65: FF                              ;
AF66: FF                              ;
AF67: FF                              ;
AF68: FF                              ;
AF69: FF                              ;
AF6A: FF                              ;
AF6B: FF                              ;
AF6C: FF                              ;
AF6D: FF                              ;
AF6E: FF                              ;
AF6F: FF                              ;
AF70: FF                              ;
AF71: FF                              ;
AF72: FF                              ;
AF73: FF                              ;
AF74: FF                              ;
AF75: FF                              ;
AF76: FF                              ;
AF77: FF                              ;
AF78: FF                              ;
AF79: FF                              ;
AF7A: FF                              ;
AF7B: FF                              ;
AF7C: FF                              ;
AF7D: FF                              ;
AF7E: FF                              ;
AF7F: FF                              ;
AF80: FF                              ;
AF81: FF                              ;
AF82: FF                              ;
AF83: FF                              ;
AF84: FF                              ;
AF85: FF                              ;
AF86: FF                              ;
AF87: FF                              ;
AF88: FF                              ;
AF89: FF                              ;
AF8A: FF                              ;
AF8B: FF                              ;
AF8C: FF                              ;
AF8D: FF                              ;
AF8E: FF                              ;
AF8F: FF                              ;
AF90: FF                              ;
AF91: FF                              ;
AF92: FF                              ;
AF93: FF                              ;
AF94: FF                              ;
AF95: FF                              ;
AF96: FF                              ;
AF97: FF                              ;
AF98: FF                              ;
AF99: FF                              ;
AF9A: FF                              ;
AF9B: FF                              ;
AF9C: FF                              ;
AF9D: FF                              ;
AF9E: FF                              ;
AF9F: FF                              ;
AFA0: FF                              ;
AFA1: FF                              ;
AFA2: FF                              ;
AFA3: FF                              ;
AFA4: FF                              ;
AFA5: FF                              ;
AFA6: FF                              ;
AFA7: FF                              ;
AFA8: FF                              ;
AFA9: FF                              ;
AFAA: FF                              ;
AFAB: FF                              ;
AFAC: FF                              ;
AFAD: FF                              ;
AFAE: FF                              ;
AFAF: FF                              ;
AFB0: FF                              ;
AFB1: FF                              ;
AFB2: FF                              ;
AFB3: FF                              ;
AFB4: FF                              ;
AFB5: FF                              ;
AFB6: FF                              ;
AFB7: FF                              ;
AFB8: FF                              ;
AFB9: FF                              ;
AFBA: FF                              ;
AFBB: FF                              ;
AFBC: FF                              ;
AFBD: FF                              ;
AFBE: FF                              ;
AFBF: FF                              ;
AFC0: FF                              ;
AFC1: FF                              ;
AFC2: FF                              ;
AFC3: FF                              ;
AFC4: FF                              ;
AFC5: FF                              ;
AFC6: FF                              ;
AFC7: FF                              ;
AFC8: FF                              ;
AFC9: FF                              ;
AFCA: FF                              ;
AFCB: FF                              ;
AFCC: FF                              ;
AFCD: FF                              ;
AFCE: FF                              ;
AFCF: FF                              ;
AFD0: FF                              ;
AFD1: FF                              ;
AFD2: FF                              ;
AFD3: FF                              ;
AFD4: FF                              ;
AFD5: FF                              ;
AFD6: FF                              ;
AFD7: FF                              ;
AFD8: FF                              ;
AFD9: FF                              ;
AFDA: FF                              ;
AFDB: FF                              ;
AFDC: FF                              ;
AFDD: FF                              ;
AFDE: FF                              ;
AFDF: FF                              ;
AFE0: FF                              ;
AFE1: FF                              ;
AFE2: FF                              ;
AFE3: FF                              ;
AFE4: FF                              ;
AFE5: FF                              ;
AFE6: FF                              ;
AFE7: FF                              ;
AFE8: FF                              ;
AFE9: FF                              ;
AFEA: FF                              ;
AFEB: FF                              ;
AFEC: FF                              ;
AFED: FF                              ;
AFEE: FF                              ;
AFEF: FF                              ;
AFF0: FF                              ;
AFF1: FF                              ;
AFF2: FF                              ;
AFF3: FF                              ;
AFF4: FF                              ;
AFF5: FF                              ;
AFF6: FF                              ;
AFF7: FF                              ;
AFF8: FF                              ;
AFF9: FF                              ;
AFFA: FF                              ;
AFFB: FF                              ;
AFFC: FF                              ;
AFFD: FF                              ;
AFFE: FF                              ;
AFFF: FF                              ;
B000: A5 EB           LDA     <$EB                ; {ram.00EB}
B002: 20 D7 83        JSR     $83D7               ; {}
B005: A9 18           LDA     #$18                ; 
B007: D0 0F           BNE     $B018               ; {}
B009: A9 D0           LDA     #$D0                ; 
B00B: A0 17           LDY     #$17                ; 
B00D: 4C 01 85        JMP     $8501               ; {}
B010: A9 E8           LDA     #$E8                ; 
B012: A0 2F           LDY     #$2F                ; 
B014: D0 F7           BNE     $B00D               ; {}
B016: A9 0E           LDA     #$0E                ; 
B018: 85 14           STA     <$14                ; {ram.0014}
B01A: E6 13           INC     <$13                ; {ram.0013}
B01C: 60              RTS                         ; 
B01D: A5 10           LDA     <$10                ; {ram.0010}
B01F: F0 05           BEQ     $B026               ; {}
B021: 20 EF B5        JSR     $B5EF               ; {}
B024: F0 F4           BEQ     $B01A               ; {}
B026: A9 44           LDA     #$44                ; 
B028: D0 EE           BNE     $B018               ; {}
B02A: AD B1 6B        LDA     $6BB1               ; {ram.6BB1}
B02D: F0 EB           BEQ     $B01A               ; {}
B02F: 8D 25 68        STA     $6825               ; {ram.6825}
B032: A9 0C           LDA     #$0C                ; 
B034: D0 E2           BNE     $B018               ; {}
B036: 20 C4 A8        JSR     $A8C4               ; {}
B039: A0 10           LDY     #$10                ; 
B03B: 84 7C           STY     <$7C                ; {ram.007C}
B03D: C8              INY                         ; 
B03E: 84 7D           STY     <$7D                ; {ram.007D}
B040: A9 00           LDA     #$00                ; 
B042: 85 17           STA     <$17                ; {ram.0017}
B044: A9 08           LDA     #$08                ; 
B046: 85 98           STA     <$98                ; {ram.0098}
B048: A9 78           LDA     #$78                ; 
B04A: 85 70           STA     <$70                ; {ram.0070}
B04C: AD A6 6B        LDA     $6BA6               ; {ram.6BA6}
B04F: 85 84           STA     <$84                ; {ram.0084}
B051: 4C 90 6C        JMP     $6C90               ; {ram.6C90}
B054: 11 E0           ORA     ($E0),Y             ; {ram.??SND_E0??}
B056: 4E CD 89        LSR     $89CD               ; {}
B059: 21 D0           AND     ($D0,X)             ; {ram.00D0}
B05B: 5E BD 78        LSR     $78BD,X             ; 
B05E: A0 05           LDY     #$05                ; 
B060: A5 10           LDA     <$10                ; {ram.0010}
B062: D0 04           BNE     $B068               ; {}
B064: A0 00           LDY     #$00                ; 
B066: 84 53           STY     <$53                ; {ram.0053}
B068: A2 00           LDX     #$00                ; 
B06A: B9 54 B0        LDA     $B054,Y             ; {}
B06D: 9D 46 03        STA     $0346,X             ; {ram.0346}
B070: C8              INY                         ; 
B071: E8              INX                         ; 
B072: E0 05           CPX     #$05                ; 
B074: D0 F4           BNE     $B06A               ; {}
B076: 60              RTS                         ; 
B077: 28              PLP                         ; 
B078: D8              CLD                         ; 
B079: 00              BRK                         ; 
B07A: 20 51 EA        JSR     $EA51               ; 
B07D: 20 3D EA        JSR     $EA3D               ; 
B080: A5 10           LDA     <$10                ; {ram.0010}
B082: F0 03           BEQ     $B087               ; {}
B084: 20 12 75        JSR     $7512               ; {ram.7512}
B087: 20 38 F2        JSR     $F238               ; 
B08A: 20 64 B4        JSR     $B464               ; {}
B08D: A5 10           LDA     <$10                ; {ram.0010}
B08F: F0 1A           BEQ     $B0AB               ; {}
B091: 20 C3 B0        JSR     $B0C3               ; {}
B094: 48              PHA                         ; 
B095: 29 07           AND     #$07                ; 
B097: C9 02           CMP     #$02                ; 
B099: D0 05           BNE     $B0A0               ; {}
B09B: A9 04           LDA     #$04                ; 
B09D: 8D 02 06        STA     $0602               ; {ram.SND_ReqMusEff}
B0A0: 68              PLA                         ; 
B0A1: 29 07           AND     #$07                ; 
B0A3: C9 02           CMP     #$02                ; 
B0A5: 90 04           BCC     $B0AB               ; {}
B0A7: C9 05           CMP     #$05                ; 
B0A9: 90 02           BCC     $B0AD               ; {}
B0AB: A0 02           LDY     #$02                ; 
B0AD: B9 77 B0        LDA     $B077,Y             ; {}
B0B0: 8D 94 03        STA     $0394               ; {ram.0394}
B0B3: 20 DD EA        JSR     $EADD               ; 
B0B6: A9 00           LDA     #$00                ; 
B0B8: 85 64           STA     <$64                ; {ram.0064}
B0BA: A0 05           LDY     #$05                ; 
B0BC: 99 B9 00        STA     $00B9,Y             ; {ram.00B9}
B0BF: 88              DEY                         ; 
B0C0: 10 FA           BPL     $B0BC               ; {}
B0C2: 60              RTS                         ; 
B0C3: A0 00           LDY     #$00                ; 
B0C5: A5 98           LDA     <$98                ; {ram.0098}
B0C7: 29 05           AND     #$05                ; 
B0C9: F0 01           BEQ     $B0CC               ; {}
B0CB: C8              INY                         ; 
B0CC: 84 0F           STY     <$0F                ; {ram.000F}
B0CE: A5 98           LDA     <$98                ; {ram.0098}
B0D0: A4 12           LDY     <$12                ; {ram.0012}
B0D2: C0 06           CPY     #$06                ; 
B0D4: F0 03           BEQ     $B0D9               ; {}
B0D6: 20 13 70        JSR     $7013               ; {ram.7013}
B0D9: 85 02           STA     <$02                ; {ram.GP_02}
B0DB: 20 F6 A3        JSR     $A3F6               ; {}
B0DE: A4 0F           LDY     <$0F                ; {ram.000F}
B0E0: 60              RTS                         ; 
B0E1: 8E 02 03        STX     $0302               ; {ram.0302}
B0E4: 8D 03 03        STA     $0303               ; {ram.0303}
B0E7: A2 18           LDX     #$18                ; 
B0E9: 8E 04 03        STX     $0304               ; {ram.0304}
B0EC: A9 FF           LDA     #$FF                ; 
B0EE: 9D 05 03        STA     $0305,X             ; {ram.!BckGndBuf}
B0F1: B9 30 05        LDA     $0530,Y             ; 
B0F4: 9D 04 03        STA     $0304,X             ; {ram.0304}
B0F7: 88              DEY                         ; 
B0F8: CA              DEX                         ; 
B0F9: D0 F6           BNE     $B0F1               ; {}
B0FB: 60              RTS                         ; 
B0FC: A5 13           LDA     <$13                ; {ram.0013}
B0FE: 20 E2 E5        JSR     $E5E2               ; 
B101: 17                              ;
B102: B1 53           LDA     ($53),Y             ; {ram.0053}
B104: B1 47           LDA     ($47),Y             ; {ram.0047}
B106: B1 3C           LDA     ($3C),Y             ; {ram.003C}
B108: B1 20           LDA     ($20),Y             ; {ram.0020}
B10A: AC 10 AC        LDY     $AC10               ; {}
B10D: 66 B1           ROR     <$B1                ; {ram.00B1}
B10F: 73                              ;
B110: B1 4B           LDA     ($4B),Y             ; {ram.004B}
B112: B1 3C           LDA     ($3C),Y             ; {ram.003C}
B114: B1 5A           LDA     ($5A),Y             ; {ram.005A}
B116: B1 A9           LDA     ($A9),Y             ; {ram.00A9}
B118: 00              BRK                         ; 
B119: 85 E9           STA     <$E9                ; {ram.00E9}
B11B: 85 EE           STA     <$EE                ; {ram.00EE}
B11D: A5 10           LDA     <$10                ; {ram.0010}
B11F: D0 06           BNE     $B127               ; {}
B121: 20 27 B1        JSR     $B127               ; {}
B124: 4C B2 83        JMP     $83B2               ; {}
B127: E6 13           INC     <$13                ; {ram.0013}
B129: 4C 3D EA        JMP     $EA3D               ; 
B12C: A9 26           LDA     #$26                ; 
B12E: 85 14           STA     <$14                ; {ram.0014}
B130: E6 13           INC     <$13                ; {ram.0013}
B132: 60              RTS                         ; 
B133: A9 00           LDA     #$00                ; 
B135: A4 10           LDY     <$10                ; {ram.0010}
B137: F0 F7           BEQ     $B130               ; {}
B139: 20 B3 87        JSR     $87B3               ; {}
B13C: A4 10           LDY     <$10                ; {ram.0010}
B13E: F0 F0           BEQ     $B130               ; {}
B140: 4C FB 8C        JMP     $8CFB               ; {}
B143: A9 A0           LDA     #$A0                ; 
B145: D0 EE           BNE     $B135               ; {}
B147: A9 20           LDA     #$20                ; 
B149: D0 EA           BNE     $B135               ; {}
B14B: A9 80           LDA     #$80                ; 
B14D: D0 E6           BNE     $B135               ; {}
B14F: A9 3E           LDA     #$3E                ; 
B151: D0 DB           BNE     $B12E               ; {}
B153: A5 10           LDA     <$10                ; {ram.0010}
B155: D0 D9           BNE     $B130               ; {}
B157: 4C 2B EA        JMP     $EA2B               ; 
B15A: 20 B6 B0        JSR     $B0B6               ; {}
B15D: A9 00           LDA     #$00                ; 
B15F: 85 13           STA     <$13                ; {ram.0013}
B161: A9 04           LDA     #$04                ; 
B163: 85 12           STA     <$12                ; {ram.0012}
B165: 60              RTS                         ; 
B166: A5 EB           LDA     <$EB                ; {ram.00EB}
B168: 4C 6D B1        JMP     $B16D               ; {}
B16B: A9 44           LDA     #$44                ; 
B16D: 20 D7 83        JSR     $83D7               ; {}
B170: 4C 09 B0        JMP     $B009               ; {}
B173: 20 10 B0        JSR     $B010               ; {}
B176: 4C 7B B1        JMP     $B17B               ; {}
B179: E6 13           INC     <$13                ; {ram.0013}
B17B: A9 00           LDA     #$00                ; 
B17D: 85 E3           STA     <$E3                ; {ram.00E3}
B17F: 60              RTS                         ; 
B180: AD 94 03        LDA     $0394               ; {ram.0394}
B183: F0 0F           BEQ     $B194               ; {}
B185: A5 98           LDA     <$98                ; {ram.0098}
B187: 8D F8 03        STA     $03F8               ; {ram.03F8}
B18A: 85 0F           STA     <$0F                ; {ram.000F}
B18C: A2 00           LDX     #$00                ; 
B18E: 20 8D F0        JSR     $F08D               ; 
B191: 4C C5 ED        JMP     $EDC5               ; 
B194: 4C DD EA        JMP     $EADD               ; 
B197: 30 C0           BMI     $B159               ; {}
B199: A5 13           LDA     <$13                ; {ram.0013}
B19B: 48              PHA                         ; 
B19C: 20 C6 87        JSR     $87C6               ; {}
B19F: 20 B6 B0        JSR     $B0B6               ; {}
B1A2: 68              PLA                         ; 
B1A3: 85 13           STA     <$13                ; {ram.0013}
B1A5: A4 EB           LDY     <$EB                ; {ram.00EB}
B1A7: A2 00           LDX     #$00                ; 
B1A9: AD 27 05        LDA     $0527               ; {ram.0527}
B1AC: D9 7E 68        CMP     $687E,Y             ; 
B1AF: F0 01           BEQ     $B1B2               ; {}
B1B1: E8              INX                         ; 
B1B2: BD 97 B1        LDA     $B197,X             ; {}
B1B5: 85 70           STA     <$70                ; {ram.0070}
B1B7: A9 41           LDA     #$41                ; 
B1B9: 85 84           STA     <$84                ; {ram.0084}
B1BB: A9 04           LDA     #$04                ; 
B1BD: 85 98           STA     <$98                ; {ram.0098}
B1BF: A9 E4           LDA     #$E4                ; 
B1C1: 8D 94 03        STA     $0394               ; {ram.0394}
B1C4: A9 00           LDA     #$00                ; 
B1C6: 85 11           STA     <$11                ; {ram.0011}
B1C8: 85 53           STA     <$53                ; {ram.0053}
B1CA: E6 13           INC     <$13                ; {ram.0013}
B1CC: 60              RTS                         ; 
B1CD: A5 98           LDA     <$98                ; {ram.0098}
B1CF: 8D F8 03        STA     $03F8               ; {ram.03F8}
B1D2: 20 A0 ED        JSR     $EDA0               ; 
B1D5: A5 84           LDA     <$84                ; {ram.0084}
B1D7: C9 5D           CMP     #$5D                ; 
B1D9: D0 0A           BNE     $B1E5               ; {}
B1DB: A9 00           LDA     #$00                ; 
B1DD: 85 AC           STA     <$AC                ; {ram.00AC}
B1DF: A9 01           LDA     #$01                ; 
B1E1: 85 5A           STA     <$5A                ; {ram.005A}
B1E3: 85 11           STA     <$11                ; {ram.0011}
B1E5: 60              RTS                         ; 
B1E6: A5 63           LDA     <$63                ; {ram.0063}
B1E8: F0 29           BEQ     $B213               ; {}
B1EA: A9 10           LDA     #$10                ; 
B1EC: 8D 04 06        STA     $0604               ; {ram.SND_Request}
B1EF: AD 70 06        LDA     $0670               ; {ram.0670}
B1F2: C9 F8           CMP     #$F8                ; 
B1F4: B0 07           BCS     $B1FD               ; {}
B1F6: 18              CLC                         ; 
B1F7: 69 06           ADC     #$06                ; 
B1F9: 8D 70 06        STA     $0670               ; {ram.0670}
B1FC: 60              RTS                         ; 
B1FD: A9 00           LDA     #$00                ; 
B1FF: 8D 70 06        STA     $0670               ; {ram.0670}
B202: 20 6C 74        JSR     $746C               ; {ram.746C}
B205: D0 0D           BNE     $B214               ; {}
B207: CE 70 06        DEC     $0670               ; {ram.0670}
B20A: A9 00           LDA     #$00                ; 
B20C: 8D 2E 05        STA     $052E               ; {ram.052E}
B20F: 85 63           STA     <$63                ; {ram.0063}
B211: 85 E0           STA     <$E0                ; {ram.??SND_E0??}
B213: 60              RTS                         ; 
B214: EE 6F 06        INC     $066F               ; {ram.066F}
B217: 60              RTS                         ; 
B218: 00              BRK                         ; 
B219: 00              BRK                         ; 
B21A: 00              BRK                         ; 
B21B: 30 32           BMI     $B24F               ; {}
B21D: 34                              ;
B21E: 38              SEC                         ; 
B21F: 3A                              ;
B220: 3C                              ;
B221: 00              BRK                         ; 
B222: 00              BRK                         ; 
B223: 00              BRK                         ; 
B224: 40              RTI                         ; 
B225: 00              BRK                         ; 
B226: 00              BRK                         ; 
B227: 00              BRK                         ; 
B228: 30 32           BMI     $B25C               ; {}
B22A: 34                              ;
B22B: 38              SEC                         ; 
B22C: 3A                              ;
B22D: 3C                              ;
B22E: 00              BRK                         ; 
B22F: 00              BRK                         ; 
B230: 00              BRK                         ; 
B231: 00              BRK                         ; 
B232: 00              BRK                         ; 
B233: 00              BRK                         ; 
B234: 50 52           BVC     $B288               ; {}
B236: 54                              ;
B237: 56 58           LSR     $58,X               ; {ram.0058}
B239: 5A                              ;
B23A: A5 5E           LDA     <$5E                ; {ram.005E}
B23C: 30 1C           BMI     $B25A               ; {}
B23E: 4A              LSR     A                   ; 
B23F: A8              TAY                         ; 
B240: B0 19           BCS     $B25B               ; {}
B242: C9 0D           CMP     #$0D                ; 
B244: B0 06           BCS     $B24C               ; {}
B246: B9 18 B2        LDA     $B218,Y             ; {}
B249: 4C 91 B2        JMP     $B291               ; {}
B24C: C9 15           CMP     #$15                ; 
B24E: D0 05           BNE     $B255               ; {}
B250: A9 42           LDA     #$42                ; 
B252: 4C 49 B2        JMP     $B249               ; {}
B255: 20 7F B5        JSR     $B57F               ; {}
B258: C6 5E           DEC     <$5E                ; {ram.005E}
B25A: 60              RTS                         ; 
B25B: A9 28           LDA     #$28                ; 
B25D: 8D 02 03        STA     $0302               ; {ram.0302}
B260: A9 C0           LDA     #$C0                ; 
B262: 18              CLC                         ; 
B263: 69 20           ADC     #$20                ; 
B265: 90 03           BCC     $B26A               ; {}
B267: EE 02 03        INC     $0302               ; {ram.0302}
B26A: 88              DEY                         ; 
B26B: 10 F5           BPL     $B262               ; {}
B26D: 8D 03 03        STA     $0303               ; {ram.0303}
B270: A9 60           LDA     #$60                ; 
B272: 8D 04 03        STA     $0304               ; {ram.0304}
B275: A9 24           LDA     #$24                ; 
B277: 8D 05 03        STA     $0305               ; {ram.!BckGndBuf}
B27A: A9 FF           LDA     #$FF                ; 
B27C: 8D 06 03        STA     $0306               ; {ram.0306}
B27F: 4C 58 B2        JMP     $B258               ; {}
B282: A5 5E           LDA     <$5E                ; {ram.005E}
B284: 30 0F           BMI     $B295               ; {}
B286: 4A              LSR     A                   ; 
B287: A8              TAY                         ; 
B288: B0 D1           BCS     $B25B               ; {}
B28A: C9 15           CMP     #$15                ; 
B28C: B0 05           BCS     $B293               ; {}
B28E: B9 25 B2        LDA     $B225,Y             ; {}
B291: 85 14           STA     <$14                ; {ram.0014}
B293: C6 5E           DEC     <$5E                ; {ram.005E}
B295: 60              RTS                         ; 
B296: 0C                              ;
B297: 0C                              ;
B298: 03                              ;
B299: 03                              ;
B29A: A5 AC           LDA     <$AC                ; {ram.00AC}
B29C: D0 1C           BNE     $B2BA               ; {}
B29E: 20 8C 8D        JSR     $8D8C               ; {}
B2A1: A5 4C           LDA     <$4C                ; {ram.004C}
B2A3: 0D 2E 05        ORA     $052E               ; {ram.052E}
B2A6: D0 09           BNE     $B2B1               ; {}
B2A8: A5 F8           LDA     <$F8                ; {ram.00F8}
B2AA: 29 80           AND     #$80                ; 
B2AC: F0 03           BEQ     $B2B1               ; {}
B2AE: 20 00 8E        JSR     $8E00               ; {}
B2B1: A5 F8           LDA     <$F8                ; {ram.00F8}
B2B3: 29 40           AND     #$40                ; 
B2B5: F0 03           BEQ     $B2BA               ; {}
B2B7: 20 1C 8E        JSR     $8E1C               ; {}
B2BA: A2 00           LDX     #$00                ; 
B2BC: A5 C0           LDA     <$C0                ; {ram.00C0}
B2BE: D0 3C           BNE     $B2FC               ; {}
B2C0: A5 10           LDA     <$10                ; {ram.0010}
B2C2: F0 03           BEQ     $B2C7               ; {}
B2C4: 20 3F 91        JSR     $913F               ; {}
B2C7: AD 94 03        LDA     $0394               ; {ram.0394}
B2CA: F0 03           BEQ     $B2CF               ; {}
B2CC: 4C 8D B3        JMP     $B38D               ; {}
B2CF: 85 0B           STA     <$0B                ; {ram.000B}
B2D1: 85 0C           STA     <$0C                ; {ram.000C}
B2D3: 85 57           STA     <$57                ; {ram.0057}
B2D5: A0 03           LDY     #$03                ; 
B2D7: AD F8 03        LDA     $03F8               ; {ram.03F8}
B2DA: 39 C3 6D        AND     $6DC3,Y             ; 
B2DD: F0 16           BEQ     $B2F5               ; {}
B2DF: 85 0F           STA     <$0F                ; {ram.000F}
B2E1: 98              TYA                         ; 
B2E2: 48              PHA                         ; 
B2E3: E6 0B           INC     <$0B                ; {ram.000B}
B2E5: 20 FA ED        JSR     $EDFA               ; 
B2E8: CD 4A 03        CMP     $034A               ; {ram.034A}
B2EB: B0 06           BCS     $B2F3               ; {}
B2ED: A5 0F           LDA     <$0F                ; {ram.000F}
B2EF: 85 0D           STA     <$0D                ; {ram.000D}
B2F1: E6 0C           INC     <$0C                ; {ram.000C}
B2F3: 68              PLA                         ; 
B2F4: A8              TAY                         ; 
B2F5: 88              DEY                         ; 
B2F6: 10 DF           BPL     $B2D7               ; {}
B2F8: A4 0B           LDY     <$0B                ; {ram.000B}
B2FA: D0 01           BNE     $B2FD               ; {}
B2FC: 60              RTS                         ; 
B2FD: A5 0F           LDA     <$0F                ; {ram.000F}
B2FF: C0 01           CPY     #$01                ; 
B301: F0 5C           BEQ     $B35F               ; {}
B303: A5 0C           LDA     <$0C                ; {ram.000C}
B305: D0 03           BNE     $B30A               ; {}
B307: 4C AB B3        JMP     $B3AB               ; {}
B30A: A8              TAY                         ; 
B30B: E6 57           INC     <$57                ; {ram.0057}
B30D: A2 00           LDX     #$00                ; 
B30F: A5 0D           LDA     <$0D                ; {ram.000D}
B311: C0 01           CPY     #$01                ; 
B313: F0 4A           BEQ     $B35F               ; {}
B315: A4 10           LDY     <$10                ; {ram.0010}
B317: F0 46           BEQ     $B35F               ; {}
B319: A4 70           LDY     <$70                ; {ram.0070}
B31B: C0 20           CPY     #$20                ; 
B31D: F0 04           BEQ     $B323               ; {}
B31F: C0 D0           CPY     #$D0                ; 
B321: D0 10           BNE     $B333               ; {}
B323: A4 84           LDY     <$84                ; {ram.0084}
B325: C0 85           CPY     #$85                ; 
B327: D0 24           BNE     $B34D               ; {}
B329: A5 98           LDA     <$98                ; {ram.0098}
B32B: 29 04           AND     #$04                ; 
B32D: F0 1E           BEQ     $B34D               ; {}
B32F: A5 98           LDA     <$98                ; {ram.0098}
B331: D0 2C           BNE     $B35F               ; {}
B333: A5 98           LDA     <$98                ; {ram.0098}
B335: A6 56           LDX     <$56                ; {ram.0056}
B337: F0 14           BEQ     $B34D               ; {}
B339: A4 10           LDY     <$10                ; {ram.0010}
B33B: F0 22           BEQ     $B35F               ; {}
B33D: A4 70           LDY     <$70                ; {ram.0070}
B33F: C0 78           CPY     #$78                ; 
B341: D0 1C           BNE     $B35F               ; {}
B343: A4 84           LDY     <$84                ; {ram.0084}
B345: C0 5D           CPY     #$5D                ; 
B347: D0 16           BNE     $B35F               ; {}
B349: 29 03           AND     #$03                ; 
B34B: F0 E2           BEQ     $B32F               ; {}
B34D: A5 98           LDA     <$98                ; {ram.0098}
B34F: E8              INX                         ; 
B350: 20 13 70        JSR     $7013               ; {ram.7013}
B353: AD F8 03        LDA     $03F8               ; {ram.03F8}
B356: 48              PHA                         ; 
B357: 39 96 B2        AND     $B296,Y             ; {}
B35A: 85 0C           STA     <$0C                ; {ram.000C}
B35C: 68              PLA                         ; 
B35D: 45 0C           EOR     <$0C                ; {ram.000C}
B35F: 86 56           STX     <$56                ; {ram.0056}
B361: 20 A9 B3        JSR     $B3A9               ; {}
B364: A2 00           LDX     #$00                ; 
B366: A9 60           LDA     #$60                ; 
B368: 85 00           STA     <$00                ; {ram.GP_00}
B36A: A5 10           LDA     <$10                ; {ram.0010}
B36C: D0 19           BNE     $B387               ; {}
B36E: AD 9E 04        LDA     $049E               ; {ram.049E}
B371: C9 74           CMP     #$74                ; 
B373: F0 04           BEQ     $B379               ; {}
B375: C9 75           CMP     #$75                ; 
B377: D0 0E           BNE     $B387               ; {}
B379: A9 30           LDA     #$30                ; 
B37B: 85 00           STA     <$00                ; {ram.GP_00}
B37D: CD BC 03        CMP     $03BC               ; {ram.03BC}
B380: F0 05           BEQ     $B387               ; {}
B382: A9 00           LDA     #$00                ; 
B384: 8D A8 03        STA     $03A8               ; {ram.03A8}
B387: A5 00           LDA     <$00                ; {ram.GP_00}
B389: 8D BC 03        STA     $03BC               ; {ram.03BC}
B38C: 60              RTS                         ; 
B38D: AD F8 03        LDA     $03F8               ; {ram.03F8}
B390: F0 FA           BEQ     $B38C               ; {}
B392: 20 13 70        JSR     $7013               ; {ram.7013}
B395: B9 C3 6D        LDA     $6DC3,Y             ; 
B398: C5 98           CMP     <$98                ; {ram.0098}
B39A: F0 CA           BEQ     $B366               ; {}
B39C: 05 98           ORA     <$98                ; {ram.0098}
B39E: C9 03           CMP     #$03                ; 
B3A0: F0 04           BEQ     $B3A6               ; {}
B3A2: C9 0C           CMP     #$0C                ; 
B3A4: D0 09           BNE     $B3AF               ; {}
B3A6: B9 C3 6D        LDA     $6DC3,Y             ; 
B3A9: 85 98           STA     <$98                ; {ram.0098}
B3AB: 8D F8 03        STA     $03F8               ; {ram.03F8}
B3AE: 60              RTS                         ; 
B3AF: A5 57           LDA     <$57                ; {ram.0057}
B3B1: D0 B3           BNE     $B366               ; {}
B3B3: AD 94 03        LDA     $0394               ; {ram.0394}
B3B6: 20 1F 70        JSR     $701F               ; {ram.701F}
B3B9: 48              PHA                         ; 
B3BA: A5 98           LDA     <$98                ; {ram.0098}
B3BC: 20 13 70        JSR     $7013               ; {ram.7013}
B3BF: 85 01           STA     <$01                ; {ram.GP_01}
B3C1: 68              PLA                         ; 
B3C2: C9 04           CMP     #$04                ; 
B3C4: B0 2D           BCS     $B3F3               ; {}
B3C6: A5 98           LDA     <$98                ; {ram.0098}
B3C8: 29 0A           AND     #$0A                ; 
B3CA: F0 07           BEQ     $B3D3               ; {}
B3CC: AD 94 03        LDA     $0394               ; {ram.0394}
B3CF: 10 22           BPL     $B3F3               ; {}
B3D1: 30 05           BMI     $B3D8               ; {}
B3D3: AD 94 03        LDA     $0394               ; {ram.0394}
B3D6: 30 1B           BMI     $B3F3               ; {}
B3D8: A5 01           LDA     <$01                ; {ram.GP_01}
B3DA: 85 98           STA     <$98                ; {ram.0098}
B3DC: A9 08           LDA     #$08                ; 
B3DE: AC 94 03        LDY     $0394               ; {ram.0394}
B3E1: 30 02           BMI     $B3E5               ; {}
B3E3: A9 F8           LDA     #$F8                ; 
B3E5: 48              PHA                         ; 
B3E6: 98              TYA                         ; 
B3E7: 20 21 70        JSR     $7021               ; {ram.7021}
B3EA: 85 01           STA     <$01                ; {ram.GP_01}
B3EC: 68              PLA                         ; 
B3ED: 38              SEC                         ; 
B3EE: E5 01           SBC     <$01                ; {ram.GP_01}
B3F0: 8D 94 03        STA     $0394               ; {ram.0394}
B3F3: 60              RTS                         ; 
B3F4: A5 5A           LDA     <$5A                ; {ram.005A}
B3F6: 0D 94 03        ORA     $0394               ; {ram.0394}
B3F9: D0 73           BNE     $B46E               ; {}
B3FB: A5 10           LDA     <$10                ; {ram.0010}
B3FD: D0 0E           BNE     $B40D               ; {}
B3FF: A5 EB           LDA     <$EB                ; {ram.00EB}
B401: C9 22           CMP     #$22                ; 
B403: D0 08           BNE     $B40D               ; {}
B405: A5 70           LDA     <$70                ; {ram.0070}
B407: 29 07           AND     #$07                ; 
B409: D0 63           BNE     $B46E               ; {}
B40B: F0 06           BEQ     $B413               ; {}
B40D: A5 70           LDA     <$70                ; {ram.0070}
B40F: 29 0F           AND     #$0F                ; 
B411: D0 5B           BNE     $B46E               ; {}
B413: A5 84           LDA     <$84                ; {ram.0084}
B415: 29 0F           AND     #$0F                ; 
B417: C9 0D           CMP     #$0D                ; 
B419: D0 53           BNE     $B46E               ; {}
B41B: 20 F4 ED        JSR     $EDF4               ; 
B41E: AD 9E 04        LDA     $049E               ; {ram.049E}
B421: A4 10           LDY     <$10                ; {ram.0010}
B423: F0 4A           BEQ     $B46F               ; {}
B425: C9 70           CMP     #$70                ; 
B427: 90 45           BCC     $B46E               ; {}
B429: C9 74           CMP     #$74                ; 
B42B: B0 41           BCS     $B46E               ; {}
B42D: 20 64 B4        JSR     $B464               ; {}
B430: A5 EB           LDA     <$EB                ; {ram.00EB}
B432: 8D 27 05        STA     $0527               ; {ram.0527}
B435: A2 FF           LDX     #$FF                ; 
B437: E8              INX                         ; 
B438: BD B2 6B        LDA     $6BB2,X             ; 
B43B: A8              TAY                         ; 
B43C: A5 EB           LDA     <$EB                ; {ram.00EB}
B43E: D9 7E 68        CMP     $687E,Y             ; 
B441: F0 05           BEQ     $B448               ; {}
B443: D9 FE 68        CMP     $68FE,Y             ; 
B446: D0 EF           BNE     $B437               ; {}
B448: 84 EB           STY     <$EB                ; {ram.00EB}
B44A: A9 09           LDA     #$09                ; 
B44C: 85 5B           STA     <$5B                ; {ram.005B}
B44E: C9 09           CMP     #$09                ; 
B450: F0 08           BEQ     $B45A               ; {}
B452: 20 E9 6E        JSR     $6EE9               ; {ram.6EE9}
B455: 8D 02 06        STA     $0602               ; {ram.SND_ReqMusEff}
B458: 85 3C           STA     <$3C                ; {ram.003C}
B45A: A9 10           LDA     #$10                ; 
B45C: 85 12           STA     <$12                ; {ram.0012}
B45E: 20 59 B5        JSR     $B559               ; {}
B461: 4C 61 8F        JMP     $8F61               ; {}
B464: A5 10           LDA     <$10                ; {ram.0010}
B466: D0 03           BNE     $B46B               ; {}
B468: 4C E5 90        JMP     $90E5               ; {}
B46B: 20 D7 92        JSR     $92D7               ; {}
B46E: 60              RTS                         ; 
B46F: 85 65           STA     <$65                ; {ram.0065}
B471: C9 24           CMP     #$24                ; 
B473: F0 11           BEQ     $B486               ; {}
B475: C9 88           CMP     #$88                ; 
B477: F0 0D           BEQ     $B486               ; {}
B479: C9 70           CMP     #$70                ; 
B47B: 90 F1           BCC     $B46E               ; {}
B47D: C9 74           CMP     #$74                ; 
B47F: B0 ED           BCS     $B46E               ; {}
B481: A9 70           LDA     #$70                ; 
B483: 8D 9E 04        STA     $049E               ; {ram.049E}
B486: 20 64 B4        JSR     $B464               ; {}
B489: A4 EB           LDY     <$EB                ; {ram.00EB}
B48B: B9 FE 68        LDA     $68FE,Y             ; 
B48E: 29 FC           AND     #$FC                ; 
B490: C9 40           CMP     #$40                ; 
B492: 90 0B           BCC     $B49F               ; {}
B494: A0 0B           LDY     #$0B                ; 
B496: C9 50           CMP     #$50                ; 
B498: D0 01           BNE     $B49B               ; {}
B49A: C8              INY                         ; 
B49B: 98              TYA                         ; 
B49C: 4C 4C B4        JMP     $B44C               ; {}
B49F: 4A              LSR     A                   ; 
B4A0: 4A              LSR     A                   ; 
B4A1: 85 10           STA     <$10                ; {ram.0010}
B4A3: A5 EB           LDA     <$EB                ; {ram.00EB}
B4A5: 8D 26 05        STA     $0526               ; {ram.0526}
B4A8: A9 02           LDA     #$02                ; 
B4AA: D0 A0           BNE     $B44C               ; {}
```

# Format BBR

```code
FormatBBR: 
; Clear area in battery backed ram if 6001 and 7FFF aren't 5A.
; Also store FF to 652A, 652B, and 652C
; Return C=1 if formatting was done. Return C=0 if nothing was needed
;
B4AC: AD 01 60        LDA     $6001               ; {ram.MARK_A} ?? What about $6000 ?
B4AF: C9 5A           CMP     #$5A                ; Format byte?
B4B1: D0 07           BNE     $B4BA               ; {} No ... go clear persistent memory
B4B3: AD FF 7F        LDA     $7FFF               ; {ram.MARK_B} End format ...
B4B6: C9 A5           CMP     #$A5                ; ... byte?
B4B8: F0 2C           BEQ     $B4E6               ; {} Yes ... persistent memory is good.
;
B4BA: A9 FF           LDA     #$FF                ; 
B4BC: 8D 2A 65        STA     $652A               ; {ram.Q_SG1}
B4BF: 8D 2B 65        STA     $652B               ; {ram.Q_SG2}
B4C2: 8D 2C 65        STA     $652C               ; {ram.Q_SQ3}
;
B4C5: A9 65           LDA     #$65                ; Clear ...
B4C7: 85 01           STA     <$01                ; {ram.GP_01} ... battery ...
B4C9: A9 30           LDA     #$30                ; ... backed ...
B4CB: 85 00           STA     <$00                ; {ram.GP_00} ... RAM ...
B4CD: A0 00           LDY     #$00                ; ... from ...
B4CF: A9 00           LDA     #$00                ; ... 6530 to 7FFF
B4D1: 91 00           STA     ($00),Y             ; {ram.GP_00} ...
B4D3: A5 00           LDA     <$00                ; {ram.GP_00} ...
B4D5: 18              CLC                         ; ...
B4D6: 69 01           ADC     #$01                ; ...
B4D8: 85 00           STA     <$00                ; {ram.GP_00} ...
B4DA: A5 01           LDA     <$01                ; {ram.GP_01} ...
B4DC: 69 00           ADC     #$00                ; ...
B4DE: 85 01           STA     <$01                ; {ram.GP_01} ...
B4E0: C9 80           CMP     #$80                ; ...
B4E2: D0 EB           BNE     $B4CF               ; {} .
B4E4: 38              SEC                         ; Set carry if RAM was formatted
B4E5: 60              RTS                         ; Done
B4E6: 18              CLC                         ; Clear carry if RAM was good
B4E7: 60              RTS                         ; Done

B4E8: A9 07           LDA     #$07                ; 
B4EA: A0 FE           LDY     #$FE                ; 
B4EC: 20 08 E6        JSR     $E608               ; 
B4EF: A9 00           LDA     #$00                ; 
B4F1: 85 F7           STA     <$F7                ; {ram.00F7}
B4F3: 85 F5           STA     <$F5                ; {ram.TileFlagA}
B4F5: 85 F6           STA     <$F6                ; {ram.TileFlagB}
B4F7: 85 F3           STA     <$F3                ; {ram.00F3}
B4F9: A0 EF           LDY     #$EF                ; 
B4FB: 99 00 00        STA     $0000,Y             ; {ram.GP_00}
B4FE: 88              DEY                         ; 
B4FF: C0 FF           CPY     #$FF                ; 
B501: D0 F8           BNE     $B4FB               ; {}
B503: A9 40           LDA     #$40                ; 
B505: 8D 25 05        STA     $0525               ; {ram.0525}
B508: 85 18           STA     <$18                ; {ram.0018}
B50A: A9 01           LDA     #$01                ; 
B50C: 8D 36 06        STA     $0636               ; {ram.0636}
B50F: 8D 37 06        STA     $0637               ; {ram.0637}
B512: 60              RTS                         ; 

B513: F0 10           BEQ     $B525               ; {}
B515: FF                              ;
B516: 01 A9           ORA     ($A9,X)             ; {ram.00A9}
B518: 00              BRK                         ; 
B519: 85 E7           STA     <$E7                ; {ram.00E7}
B51B: 60              RTS                         ; 
B51C: 06 00           ASL     <$00                ; {ram.GP_00}
B51E: CA              DEX                         ; 
B51F: 4C 28 B5        JMP     $B528               ; {}
B522: A9 01           LDA     #$01                ; 
B524: 85 00           STA     <$00                ; {ram.GP_00}
B526: A2 03           LDX     #$03                ; 
B528: A5 E7           LDA     <$E7                ; {ram.00E7}
B52A: 24 00           BIT     <$00                ; {ram.GP_00}
B52C: F0 EE           BEQ     $B51C               ; {}
B52E: 20 5A E8        JSR     $E85A               ; 
B531: 8D E4 04        STA     $04E4               ; {ram.04E4}
B534: BD 13 B5        LDA     $B513,X             ; {}
B537: 18              CLC                         ; 
B538: 65 EB           ADC     <$EB                ; {ram.00EB}
B53A: 85 EC           STA     <$EC                ; {ram.00EC}
B53C: A5 10           LDA     <$10                ; {ram.0010}
B53E: D0 03           BNE     $B543               ; {}
B540: 20 2F 75        JSR     $752F               ; {ram.752F}
B543: A5 EC           LDA     <$EC                ; {ram.00EC}
B545: 10 12           BPL     $B559               ; {}
B547: 20 A3 EB        JSR     $EBA3               ; 
B54A: 85 E7           STA     <$E7                ; {ram.00E7}
B54C: 85 10           STA     <$10                ; {ram.0010}
B54E: A9 02           LDA     #$02                ; 
B550: 85 12           STA     <$12                ; {ram.0012}
B552: 85 5A           STA     <$5A                ; {ram.005A}
B554: A9 80           LDA     #$80                ; 
B556: 8D 04 06        STA     $0604               ; {ram.SND_Request}
B559: A5 FE           LDA     <$FE                ; {ram.CUR_2001}
B55B: 29 FE           AND     #$FE                ; 
B55D: 85 FE           STA     <$FE                ; {ram.CUR_2001}
B55F: 60              RTS                         ; 
B560: A2 01           LDX     #$01                ; 
B562: 86 00           STX     <$00                ; {ram.GP_00}
B564: A2 03           LDX     #$03                ; 
B566: 24 00           BIT     <$00                ; {ram.GP_00}
B568: D0 06           BNE     $B570               ; {}
B56A: 06 00           ASL     <$00                ; {ram.GP_00}
B56C: CA              DEX                         ; 
B56D: 4C 66 B5        JMP     $B566               ; {}
B570: BD 13 B5        LDA     $B513,X             ; {}
B573: 18              CLC                         ; 
B574: 65 EB           ADC     <$EB                ; {ram.00EB}
B576: 60              RTS                         ; 
B577: 80                              ;
B578: 40              RTI                         ; 
B579: 20 10 08        JSR     $0810               ; 
B57C: 04                              ;
B57D: 02                              ;
B57E: 01 A0           ORA     ($A0,X)             ; {ram.00A0}
B580: 10 A5           BPL     $B527               ; {}
B582: 5E 4A AA        LSR     $AA4A,X             ; {}
B585: A9 FF           LDA     #$FF                ; 
B587: 99 05 03        STA     $0305,Y             ; {ram.!BckGndBuf}
B58A: A9 10           LDA     #$10                ; 
B58C: 8D 04 03        STA     $0304               ; {ram.0304}
B58F: A9 28           LDA     #$28                ; 
B591: 8D 02 03        STA     $0302               ; {ram.0302}
B594: A9 EC           LDA     #$EC                ; 
B596: 18              CLC                         ; 
B597: 69 20           ADC     #$20                ; 
B599: 90 03           BCC     $B59E               ; {}
B59B: EE 02 03        INC     $0302               ; {ram.0302}
B59E: CA              DEX                         ; 
B59F: 10 F5           BPL     $B596               ; {}
B5A1: 8D 03 03        STA     $0303               ; {ram.0303}
B5A4: A5 5D           LDA     <$5D                ; {ram.005D}
B5A6: 48              PHA                         ; 
B5A7: 20 08 B6        JSR     $B608               ; {}
B5AA: C6 5D           DEC     <$5D                ; {ram.005D}
B5AC: 88              DEY                         ; 
B5AD: D0 F8           BNE     $B5A7               ; {}
B5AF: 68              PLA                         ; 
B5B0: 38              SEC                         ; 
B5B1: E9 10           SBC     #$10                ; 
B5B3: 85 5D           STA     <$5D                ; {ram.005D}
B5B5: AE AB 6B        LDX     $6BAB               ; {ram.6BAB}
B5B8: F0 17           BEQ     $B5D1               ; {}
B5BA: AD 14 03        LDA     $0314               ; {ram.0314}
B5BD: 48              PHA                         ; 
B5BE: A0 0E           LDY     #$0E                ; 
B5C0: B9 05 03        LDA     $0305,Y             ; {ram.!BckGndBuf}
B5C3: 99 06 03        STA     $0306,Y             ; {ram.0306}
B5C6: 88              DEY                         ; 
B5C7: 10 F7           BPL     $B5C0               ; {}
B5C9: 68              PLA                         ; 
B5CA: 8D 05 03        STA     $0305               ; {ram.!BckGndBuf}
B5CD: CA              DEX                         ; 
B5CE: 4C B8 B5        JMP     $B5B8               ; {}
B5D1: A5 5E           LDA     <$5E                ; {ram.005E}
B5D3: 38              SEC                         ; 
B5D4: E9 1A           SBC     #$1A                ; 
B5D6: 4A              LSR     A                   ; 
B5D7: AA              TAX                         ; 
B5D8: A0 0F           LDY     #$0F                ; 
B5DA: B9 BD 6B        LDA     $6BBD,Y             ; 
B5DD: 3D 77 B5        AND     $B577,X             ; {}
B5E0: D0 05           BNE     $B5E7               ; {}
B5E2: A9 F5           LDA     #$F5                ; 
B5E4: 99 05 03        STA     $0305,Y             ; {ram.!BckGndBuf}
B5E7: 88              DEY                         ; 
B5E8: 10 F0           BPL     $B5DA               ; {}
B5EA: 60              RTS                         ; 

B5EB: A2 10           LDX     #$10                ; 
B5ED: D0 02           BNE     $B5F1               ; {}
B5EF: A2 11           LDX     #$11                ; 
B5F1: A5 10           LDA     <$10                ; {ram.0010}
B5F3: F0 12           BEQ     $B607               ; {}
B5F5: 38              SEC                         ; 
B5F6: E9 01           SBC     #$01                ; 
B5F8: C9 08           CMP     #$08                ; 
B5FA: 90 02           BCC     $B5FE               ; {}
B5FC: E8              INX                         ; 
B5FD: E8              INX                         ; 
B5FE: 29 07           AND     #$07                ; 
B600: A8              TAY                         ; 
B601: BD 57 06        LDA     $0657,X             ; {ram.0657}
B604: 39 BE E6        AND     $E6BE,Y             ; 
B607: 60              RTS                         ; 

B608: 98              TYA                         ; 
B609: 48              PHA                         ; 
B60A: 20 CE E6        JSR     $E6CE               ; 
B60D: A5 EB           LDA     <$EB                ; {ram.00EB}
B60F: 48              PHA                         ; 
B610: A5 5D           LDA     <$5D                ; {ram.005D}
B612: 85 EB           STA     <$EB                ; {ram.00EB}
B614: A9 13           LDA     #$13                ; 
B616: 8D 3F 03        STA     $033F               ; {ram.033F}
B619: A4 EB           LDY     <$EB                ; {ram.00EB}
B61B: B1 00           LDA     ($00),Y             ; {ram.GP_00}
B61D: 29 20           AND     #$20                ; 
B61F: F0 11           BEQ     $B632               ; {}
B621: A9 08           LDA     #$08                ; 
B623: 85 02           STA     <$02                ; {ram.GP_02}
B625: A2 03           LDX     #$03                ; 
B627: 20 F6 A3        JSR     $A3F6               ; {}
B62A: 20 41 B6        JSR     $B641               ; {}
B62D: CA              DEX                         ; 
B62E: 46 02           LSR     <$02                ; {ram.GP_02}
B630: D0 F5           BNE     $B627               ; {}
B632: 68              PLA                         ; 
B633: 85 EB           STA     <$EB                ; {ram.00EB}
B635: 68              PLA                         ; 
B636: A8              TAY                         ; 
B637: AD 3F 03        LDA     $033F               ; {ram.033F}
B63A: 18              CLC                         ; 
B63B: 69 E2           ADC     #$E2                ; 
B63D: 99 04 03        STA     $0304,Y             ; {ram.0304}
B640: 60              RTS                         ; 
B641: A0 00           LDY     #$00                ; 
B643: 48              PHA                         ; 
B644: C9 04           CMP     #$04                ; 
B646: 90 1D           BCC     $B665               ; {}
B648: 8A              TXA                         ; 
B649: 48              PHA                         ; 
B64A: 98              TYA                         ; 
B64B: 48              PHA                         ; 
B64C: 20 CE E6        JSR     $E6CE               ; 
B64F: 18              CLC                         ; 
B650: 3D BE E6        AND     $E6BE,X             ; 
B653: F0 01           BEQ     $B656               ; {}
B655: 38              SEC                         ; 
B656: 68              PLA                         ; 
B657: A8              TAY                         ; 
B658: 68              PLA                         ; 
B659: AA              TAX                         ; 
B65A: B9 3F 03        LDA     $033F,Y             ; {ram.033F}
B65D: 2A              ROL     A                   ; 
B65E: 29 0F           AND     #$0F                ; 
B660: 99 3F 03        STA     $033F,Y             ; {ram.033F}
B663: 68              PLA                         ; 
B664: 60              RTS                         ; 
B665: C9 00           CMP     #$00                ; 
B667: F0 F1           BEQ     $B65A               ; {}
B669: 18              CLC                         ; 
B66A: 90 EE           BCC     $B65A               ; {}
B66C: 20 CE E6        JSR     $E6CE               ; 
B66F: A2 03           LDX     #$03                ; 
B671: B1 00           LDA     ($00),Y             ; {ram.GP_00}
B673: 3D BE E6        AND     $E6BE,X             ; 
B676: F0 04           BEQ     $B67C               ; {}
B678: 05 EE           ORA     <$EE                ; {ram.00EE}
B67A: 85 EE           STA     <$EE                ; {ram.00EE}
B67C: CA              DEX                         ; 
B67D: 10 F2           BPL     $B671               ; {}
B67F: 60              RTS                         ; 
B680: A5 EB           LDA     <$EB                ; {ram.00EB}
B682: 48              PHA                         ; 
B683: 29 0F           AND     #$0F                ; 
B685: A8              TAY                         ; 
B686: 68              PLA                         ; 
B687: 4A              LSR     A                   ; 
B688: 4A              LSR     A                   ; 
B689: 4A              LSR     A                   ; 
B68A: 4A              LSR     A                   ; 
B68B: AA              TAX                         ; 
B68C: 60              RTS                         ; 
B68D: A5 10           LDA     <$10                ; {ram.0010}
B68F: F0 05           BEQ     $B696               ; {}
B691: B9 7E 6A        LDA     $6A7E,Y             ; 
B694: 29 80           AND     #$80                ; 
B696: 60              RTS                         ; 
B697: 80                              ;
B698: 98              TYA                         ; 
B699: AC B4 C8        LDY     $C8B4               ; 
B69C: 80                              ;
B69D: 98              TYA                         ; 
B69E: B0 C8           BCS     $B668               ; {}
B6A0: 80                              ;
B6A1: 94 A0           STY     $A0,X               ; {ram.00A0}
B6A3: B0 C0           BCS     $B665               ; {}
B6A5: CC B0 A2        CPY     $A2B0               ; {}
B6A8: 1E BD 57        ASL     $57BD,X             ; 
B6AB: 06 D0           ASL     <$D0                ; {ram.00D0}
B6AD: 07                              ;
B6AE: CA              DEX                         ; 
B6AF: E0 1C           CPX     #$1C                ; 
B6B1: D0 F6           BNE     $B6A9               ; {}
B6B3: F0 0D           BEQ     $B6C2               ; {}
B6B5: A9 36           LDA     #$36                ; 
B6B7: 85 01           STA     <$01                ; {ram.GP_01}
B6B9: A9 80           LDA     #$80                ; 
B6BB: 85 00           STA     <$00                ; {ram.GP_00}
B6BD: 8A              TXA                         ; 
B6BE: A8              TAY                         ; 
B6BF: 20 35 E7        JSR     $E735               ; 
B6C2: A2 01           LDX     #$01                ; 
B6C4: BD 57 06        LDA     $0657,X             ; {ram.0657}
B6C7: E0 10           CPX     #$10                ; 
B6C9: D0 05           BNE     $B6D0               ; {}
B6CB: 20 EB B5        JSR     $B5EB               ; {}
B6CE: A2 10           LDX     #$10                ; 
B6D0: E0 11           CPX     #$11                ; 
B6D2: D0 05           BNE     $B6D9               ; {}
B6D4: 20 EF B5        JSR     $B5EF               ; {}
B6D7: A2 11           LDX     #$11                ; 
B6D9: C9 00           CMP     #$00                ; 
B6DB: F0 3A           BEQ     $B717               ; {}
B6DD: E0 0F           CPX     #$0F                ; 
B6DF: D0 05           BNE     $B6E6               ; {}
B6E1: AD 5E 06        LDA     $065E               ; {ram.065E}
B6E4: D0 31           BNE     $B717               ; {}
B6E6: 8A              TXA                         ; 
B6E7: 48              PHA                         ; 
B6E8: A8              TAY                         ; 
B6E9: BD 97 B6        LDA     $B697,X             ; {}
B6EC: 85 00           STA     <$00                ; {ram.GP_00}
B6EE: A9 36           LDA     #$36                ; 
B6F0: E0 05           CPX     #$05                ; 
B6F2: 90 1C           BCC     $B710               ; {}
B6F4: A9 46           LDA     #$46                ; 
B6F6: E0 0F           CPX     #$0F                ; 
B6F8: F0 16           BEQ     $B710               ; {}
B6FA: E0 09           CPX     #$09                ; 
B6FC: 90 12           BCC     $B710               ; {}
B6FE: A9 1E           LDA     #$1E                ; 
B700: E0 10           CPX     #$10                ; 
B702: 90 0C           BCC     $B710               ; {}
B704: A9 2C           LDA     #$2C                ; 
B706: 85 00           STA     <$00                ; {ram.GP_00}
B708: A9 9E           LDA     #$9E                ; 
B70A: E0 11           CPX     #$11                ; 
B70C: 90 02           BCC     $B710               ; {}
B70E: A9 76           LDA     #$76                ; 
B710: 85 01           STA     <$01                ; {ram.GP_01}
B712: 20 1C B8        JSR     $B81C               ; {}
B715: 68              PLA                         ; 
B716: AA              TAX                         ; 
B717: E8              INX                         ; 
B718: E0 12           CPX     #$12                ; 
B71A: 90 A8           BCC     $B6C4               ; {}
B71C: 60              RTS                         ; 
B71D: 80                              ;
B71E: 98              TYA                         ; 
B71F: B0 B0           BCS     $B6D1               ; {}
B721: C8              INY                         ; 
B722: 80                              ;
B723: 98              TYA                         ; 
B724: B0 C8           BCS     $B6EE               ; {}
B726: AE 56 06        LDX     $0656               ; {ram.0656}
B729: D0 0E           BNE     $B739               ; {}
B72B: A2 1E           LDX     #$1E                ; 
B72D: BD 57 06        LDA     $0657,X             ; {ram.0657}
B730: D0 07           BNE     $B739               ; {}
B732: CA              DEX                         ; 
B733: E0 1C           CPX     #$1C                ; 
B735: D0 F6           BNE     $B72D               ; {}
B737: F0 1D           BEQ     $B756               ; {}
B739: BD 57 06        LDA     $0657,X             ; {ram.0657}
B73C: F0 18           BEQ     $B756               ; {}
B73E: E0 0F           CPX     #$0F                ; 
B740: D0 07           BNE     $B749               ; {}
B742: AD 5E 06        LDA     $065E               ; {ram.065E}
B745: D0 0F           BNE     $B756               ; {}
B747: A9 01           LDA     #$01                ; 
B749: 85 04           STA     <$04                ; {ram.0004}
B74B: A9 36           LDA     #$36                ; 
B74D: 85 01           STA     <$01                ; {ram.GP_01}
B74F: A9 40           LDA     #$40                ; 
B751: 85 00           STA     <$00                ; {ram.GP_00}
B753: 20 1C B8        JSR     $B81C               ; {}
B756: AC 56 06        LDY     $0656               ; {ram.0656}
B759: C0 0F           CPY     #$0F                ; 
B75B: D0 0A           BNE     $B767               ; {}
B75D: A0 07           LDY     #$07                ; 
B75F: B9 57 06        LDA     $0657,Y             ; {ram.0657}
B762: F0 03           BEQ     $B767               ; {}
B764: 8C 56 06        STY     $0656               ; {ram.0656}
B767: B9 1D B7        LDA     $B71D,Y             ; {}
B76A: 8D 1F 02        STA     $021F               ; {ram.021F}
B76D: 18              CLC                         ; 
B76E: 69 08           ADC     #$08                ; 
B770: 8D 23 02        STA     $0223               ; {ram.0223}
B773: A9 36           LDA     #$36                ; 
B775: C0 05           CPY     #$05                ; 
B777: 90 02           BCC     $B77B               ; {}
B779: A9 46           LDA     #$46                ; 
B77B: 8D 1C 02        STA     $021C               ; {ram.021C}
B77E: 8D 20 02        STA     $0220               ; {ram.0220}
B781: A9 1E           LDA     #$1E                ; 
B783: 8D 1D 02        STA     $021D               ; {ram.021D}
B786: 8D 21 02        STA     $0221               ; {ram.0221}
B789: A5 15           LDA     <$15                ; {ram.0015}
B78B: 29 08           AND     #$08                ; 
B78D: 4A              LSR     A                   ; 
B78E: 4A              LSR     A                   ; 
B78F: 4A              LSR     A                   ; 
B790: 69 01           ADC     #$01                ; 
B792: 8D 1E 02        STA     $021E               ; {ram.021E}
B795: 09 40           ORA     #$40                ; 
B797: 8D 22 02        STA     $0222               ; {ram.0222}
B79A: AD F8 03        LDA     $03F8               ; {ram.03F8}
B79D: C5 EF           CMP     <$EF                ; {ram.00EF}
B79F: F0 50           BEQ     $B7F1               ; {}
B7A1: AA              TAX                         ; 
B7A2: F0 24           BEQ     $B7C8               ; {}
B7A4: E0 04           CPX     #$04                ; 
B7A6: B0 20           BCS     $B7C8               ; {}
B7A8: A2 01           LDX     #$01                ; 
B7AA: 8E 02 06        STX     $0602               ; {ram.SND_ReqMusEff}
B7AD: AA              TAX                         ; 
B7AE: AD 56 06        LDA     $0656               ; {ram.0656}
B7B1: 48              PHA                         ; 
B7B2: 8A              TXA                         ; 
B7B3: 20 C8 B7        JSR     $B7C8               ; {}
B7B6: 68              PLA                         ; 
B7B7: CD 56 06        CMP     $0656               ; {ram.0656}
B7BA: F0 08           BEQ     $B7C4               ; {}
B7BC: AC 56 06        LDY     $0656               ; {ram.0656}
B7BF: B9 57 06        LDA     $0657,Y             ; {ram.0657}
B7C2: D0 03           BNE     $B7C7               ; {}
B7C4: 4E 02 06        LSR     $0602               ; {ram.SND_ReqMusEff}
B7C7: 60              RTS                         ; 

B7C8: 85 EF           STA     <$EF                ; {ram.00EF}
B7CA: A2 09           LDX     #$09                ; 
B7CC: 20 21 B8        JSR     $B821               ; {}
B7CF: C0 00           CPY     #$00                ; 
B7D1: F0 1F           BEQ     $B7F2               ; {}
B7D3: C0 03           CPY     #$03                ; 
B7D5: F0 09           BEQ     $B7E0               ; {}
B7D7: B9 57 06        LDA     $0657,Y             ; {ram.0657}
B7DA: D0 09           BNE     $B7E5               ; {}
B7DC: C0 07           CPY     #$07                ; 
B7DE: F0 28           BEQ     $B808               ; {}
B7E0: CA              DEX                         ; 
B7E1: 10 E9           BPL     $B7CC               ; {}
B7E3: A0 00           LDY     #$00                ; 
B7E5: C0 02           CPY     #$02                ; 
B7E7: D0 05           BNE     $B7EE               ; {}
B7E9: AD 5A 06        LDA     $065A               ; {ram.065A}
B7EC: F0 DE           BEQ     $B7CC               ; {}
B7EE: 8C 56 06        STY     $0656               ; {ram.0656}
B7F1: 60              RTS                         ; 
B7F2: A0 1E           LDY     #$1E                ; 
B7F4: B9 57 06        LDA     $0657,Y             ; {ram.0657}
B7F7: D0 0A           BNE     $B803               ; {}
B7F9: 88              DEY                         ; 
B7FA: C0 1C           CPY     #$1C                ; 
B7FC: D0 F6           BNE     $B7F4               ; {}
B7FE: A0 00           LDY     #$00                ; 
B800: 4C E0 B7        JMP     $B7E0               ; {}
B803: A0 00           LDY     #$00                ; 
B805: 4C E5 B7        JMP     $B7E5               ; {}
B808: A0 0F           LDY     #$0F                ; 
B80A: B9 57 06        LDA     $0657,Y             ; {ram.0657}
B80D: D0 04           BNE     $B813               ; {}
B80F: A0 07           LDY     #$07                ; 
B811: D0 CD           BNE     $B7E0               ; {}
B813: AD 5E 06        LDA     $065E               ; {ram.065E}
B816: F0 D6           BEQ     $B7EE               ; {}
B818: A0 07           LDY     #$07                ; 
B81A: D0 D2           BNE     $B7EE               ; {}
B81C: 8A              TXA                         ; 
B81D: A8              TAY                         ; 
B81E: 4C 35 E7        JMP     $E735               ; 
B821: A5 EF           LDA     <$EF                ; {ram.00EF}
B823: 29 03           AND     #$03                ; 
B825: F0 12           BEQ     $B839               ; {}
B827: C8              INY                         ; 
B828: 4A              LSR     A                   ; 
B829: B0 02           BCS     $B82D               ; {}
B82B: 88              DEY                         ; 
B82C: 88              DEY                         ; 
B82D: C0 FF           CPY     #$FF                ; 
B82F: D0 02           BNE     $B833               ; {}
B831: A0 08           LDY     #$08                ; 
B833: C0 09           CPY     #$09                ; 
B835: D0 02           BNE     $B839               ; {}
B837: A0 00           LDY     #$00                ; 
B839: 60              RTS                         ; 
B83A: A9 00           LDA     #$00                ; 
B83C: 85 BF           STA     <$BF                ; {ram.00BF}
B83E: A5 10           LDA     <$10                ; {ram.0010}
B840: F0 47           BEQ     $B889               ; {}
B842: 20 14 73        JSR     $7314               ; {ram.7314}
B845: D0 1C           BNE     $B863               ; {}
B847: A4 EB           LDY     <$EB                ; {ram.00EB}
B849: B9 7E 6A        LDA     $6A7E,Y             ; 
B84C: 29 1F           AND     #$1F                ; 
B84E: C9 03           CMP     #$03                ; 
B850: D0 02           BNE     $B854               ; {}
B852: C6 BF           DEC     <$BF                ; {ram.00BF}
B854: 85 AB           STA     <$AB                ; {ram.00AB}
B856: B9 FE 6A        LDA     $6AFE,Y             ; 
B859: 29 07           AND     #$07                ; 
B85B: C9 03           CMP     #$03                ; 
B85D: F0 04           BEQ     $B863               ; {}
B85F: C9 07           CMP     #$07                ; 
B861: D0 02           BNE     $B865               ; {}
B863: C6 BF           DEC     <$BF                ; {ram.00BF}
B865: B9 FE 69        LDA     $69FE,Y             ; 
B868: 29 40           AND     #$40                ; 
B86A: F0 03           BEQ     $B86F               ; {}
B86C: 20 F1 A7        JSR     $A7F1               ; {}
B86F: 20 8A 71        JSR     $718A               ; {ram.718A}
B872: 85 83           STA     <$83                ; {ram.0083}
B874: 84 97           STY     <$97                ; {ram.0097}
B876: A4 EB           LDY     <$EB                ; {ram.00EB}
B878: B9 7E 6A        LDA     $6A7E,Y             ; 
B87B: 29 1F           AND     #$1F                ; 
B87D: C9 1B           CMP     #$1B                ; 
B87F: D0 07           BNE     $B888               ; {}
B881: A5 83           LDA     <$83                ; {ram.0083}
B883: 38              SEC                         ; 
B884: E9 08           SBC     #$08                ; 
B886: 85 83           STA     <$83                ; {ram.0083}
B888: 60              RTS                         ; 
B889: A9 1A           LDA     #$1A                ; 
B88B: 85 AB           STA     <$AB                ; {ram.00AB}
B88D: A9 C0           LDA     #$C0                ; 
B88F: A0 90           LDY     #$90                ; 
B891: A6 12           LDX     <$12                ; {ram.0012}
B893: E0 05           CPX     #$05                ; 
B895: D0 06           BNE     $B89D               ; {}
B897: A6 EB           LDX     <$EB                ; {ram.00EB}
B899: E0 5F           CPX     #$5F                ; 
B89B: F0 D5           BEQ     $B872               ; {}
B89D: C6 BF           DEC     <$BF                ; {ram.00BF}
B89F: 60              RTS                         ; 

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

