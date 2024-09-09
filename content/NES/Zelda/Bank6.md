![Bank 6](Zelda.jpg)

# Bank 6

>>> cpu 6502

>>> binary 8000:roms/Zelda.nes[18010:1C010]

>>> memoryTable ram 

[RAM Usage](RAMUse.md)

>>> memoryTable hard 

[Hardware Info](Hardware.md)

```code
8000: 00              BRK                         ; 
8001: 84 00           STY     <$00                ; {ram.GP_00}
8003: 87                              ;
8004: 00              BRK                         ; 
8005: 87                              ;
8006: 00              BRK                         ; 
8007: 87                              ;
8008: 00              BRK                         ; 
8009: 87                              ;
800A: 00              BRK                         ; 
800B: 87                              ;
800C: 00              BRK                         ; 
800D: 87                              ;
800E: 00              BRK                         ; 
800F: 8A              TXA                         ; 
8010: 00              BRK                         ; 
8011: 8A              TXA                         ; 
8012: 00              BRK                         ; 
8013: 8A              TXA                         ; 
8014: 00              BRK                         ; 
8015: 93                              ;
8016: FC                              ;
8017: 93                              ;
8018: F8              SED                         ; 
8019: 94 F4           STY     $F4,X               ; {ram.??!BatRamInit??}
801B: 95 F0           STA     $F0,X               ; {ram.00F0}
801D: 96 EC           STX     $EC,Y               ; {ram.00EC}
801F: 97                              ;
8020: E8              INX                         ; 
8021: 98              TYA                         ; 
8022: E4 99           CPX     <$99                ; {ram.0099}
8024: E0 9A           CPX     #$9A                ; 
8026: DC                              ;
8027: 9B                              ;
8028: D8              CLD                         ; 
8029: 9C                              ;
802A: 00              BRK                         ; 
802B: 84 00           STY     <$00                ; {ram.GP_00}
802D: 8D 00 8D        STA     $8D00               ; {}
8030: 00              BRK                         ; 
8031: 8D 00 8D        STA     $8D00               ; {}
8034: 00              BRK                         ; 
8035: 8D 00 8D        STA     $8D00               ; {}
8038: 00              BRK                         ; 
8039: 90 00           BCC     $803B               ; {}
803B: 90 00           BCC     $803D               ; {}
803D: 90 A5           BCC     $7FE4               ; {ram.7FE4}
803F: 13                              ;
8040: 20 E2 E5        JSR     $E5E2               ; 
8043: 47                              ;
8044: 80                              ;
8045: 70 80           BVS     $7FC7               ; {ram.7FC7}
8047: A5 10           LDA     <$10                ; {ram.0010}
8049: 0A              ASL     A                   ; 
804A: AA              TAX                         ; 
804B: A4 16           LDY     <$16                ; {ram.0016}
804D: B9 2D 06        LDA     $062D,Y             ; 
8050: D0 0C           BNE     $805E               ; {}
8052: BD 00 80        LDA     $8000,X             ; {}
8055: 85 00           STA     <$00                ; {ram.GP_00}
8057: E8              INX                         ; 
8058: BD 00 80        LDA     $8000,X             ; {}
805B: 4C 67 80        JMP     $8067               ; {}
805E: BD 2A 80        LDA     $802A,X             ; {}
8061: 85 00           STA     <$00                ; {ram.GP_00}
8063: E8              INX                         ; 
8064: BD 2A 80        LDA     $802A,X             ; {}
8067: 85 01           STA     <$01                ; {ram.GP_01}
8069: 20 A4 80        JSR     $80A4               ; {}
806C: 20 D7 80        JSR     $80D7               ; {}
806F: 60              RTS                         ; 
8070: A5 10           LDA     <$10                ; {ram.0010}
8072: 0A              ASL     A                   ; 
8073: AA              TAX                         ; 
8074: BD 14 80        LDA     $8014,X             ; {}
8077: 85 00           STA     <$00                ; {ram.GP_00}
8079: E8              INX                         ; 
807A: BD 14 80        LDA     $8014,X             ; {}
807D: 85 01           STA     <$01                ; {ram.GP_01}
807F: 20 B5 80        JSR     $80B5               ; {}
8082: 20 D7 80        JSR     $80D7               ; {}
8085: A9 00           LDA     #$00                ; 
8087: 85 13           STA     <$13                ; {ram.0013}
8089: E6 11           INC     <$11                ; {ram.0011}
808B: 60              RTS                         ; 
808C: A2 00           LDX     #$00                ; 
808E: BD 28 80        LDA     $8028,X             ; {}
8091: 85 00           STA     <$00                ; {ram.GP_00}
8093: E8              INX                         ; 
8094: BD 28 80        LDA     $8028,X             ; {}
8097: 85 01           STA     <$01                ; {ram.GP_01}
8099: 20 C6 80        JSR     $80C6               ; {}
809C: 20 D7 80        JSR     $80D7               ; {}
809F: A9 00           LDA     #$00                ; 
80A1: 85 13           STA     <$13                ; {ram.0013}
80A3: 60              RTS                         ; 
80A4: A9 7E           LDA     #$7E                ; 
80A6: 85 02           STA     <$02                ; {ram.GP_02}
80A8: A9 68           LDA     #$68                ; 
80AA: 85 03           STA     <$03                ; {ram.GP_03}
80AC: A9 7D           LDA     #$7D                ; 
80AE: 85 04           STA     <$04                ; {ram.0004}
80B0: A9 6B           LDA     #$6B                ; 
80B2: 85 05           STA     <$05                ; {ram.0005}
80B4: 60              RTS                         ; 
80B5: A9 7E           LDA     #$7E                ; 
80B7: 85 02           STA     <$02                ; {ram.GP_02}
80B9: A9 6B           LDA     #$6B                ; 
80BB: 85 03           STA     <$03                ; {ram.GP_03}
80BD: A9 7D           LDA     #$7D                ; 
80BF: 85 04           STA     <$04                ; {ram.0004}
80C1: A9 6C           LDA     #$6C                ; 
80C3: 85 05           STA     <$05                ; {ram.0005}
80C5: 60              RTS                         ; 
80C6: A9 F0           LDA     #$F0                ; 
80C8: 85 02           STA     <$02                ; {ram.GP_02}
80CA: A9 67           LDA     #$67                ; 
80CC: 85 03           STA     <$03                ; {ram.GP_03}
80CE: A9 7D           LDA     #$7D                ; 
80D0: 85 04           STA     <$04                ; {ram.0004}
80D2: A9 68           LDA     #$68                ; 
80D4: 85 05           STA     <$05                ; {ram.0005}
80D6: 60              RTS                         ; 
80D7: A0 00           LDY     #$00                ; 
80D9: B1 00           LDA     ($00),Y             ; {ram.GP_00}
80DB: 91 02           STA     ($02),Y             ; {ram.GP_02}
80DD: A5 02           LDA     <$02                ; {ram.GP_02}
80DF: C5 04           CMP     <$04                ; {ram.0004}
80E1: D0 09           BNE     $80EC               ; {}
80E3: A5 03           LDA     <$03                ; {ram.GP_03}
80E5: C5 05           CMP     <$05                ; {ram.0005}
80E7: D0 03           BNE     $80EC               ; {}
80E9: E6 13           INC     <$13                ; {ram.0013}
80EB: 60              RTS                         ; 
80EC: A5 02           LDA     <$02                ; {ram.GP_02}
80EE: 18              CLC                         ; 
80EF: 69 01           ADC     #$01                ; 
80F1: 85 02           STA     <$02                ; {ram.GP_02}
80F3: A5 03           LDA     <$03                ; {ram.GP_03}
80F5: 69 00           ADC     #$00                ; 
80F7: 85 03           STA     <$03                ; {ram.GP_03}
80F9: A5 00           LDA     <$00                ; {ram.GP_00}
80FB: 18              CLC                         ; 
80FC: 69 01           ADC     #$01                ; 
80FE: 85 00           STA     <$00                ; {ram.GP_00}
8100: A5 01           LDA     <$01                ; {ram.GP_01}
8102: 69 00           ADC     #$00                ; 
8104: 85 01           STA     <$01                ; {ram.GP_01}
8106: 4C D9 80        JMP     $80D9               ; {}
8109: A4 16           LDY     <$16                ; {ram.0016}
810B: B9 2D 06        LDA     $062D,Y             ; 
810E: F0 1C           BEQ     $812C               ; {}
8110: A5 10           LDA     <$10                ; {ram.0010}
8112: F0 19           BEQ     $812D               ; {}
8114: AA              TAX                         ; 
8115: 0A              ASL     A                   ; 
8116: A8              TAY                         ; 
8117: B9 A2 83        LDA     $83A2,Y             ; {}
811A: 85 00           STA     <$00                ; {ram.GP_00}
811C: B9 A3 83        LDA     $83A3,Y             ; {}
811F: 85 01           STA     <$01                ; {ram.GP_01}
8121: BC B5 83        LDY     $83B5,X             ; {}
8124: B1 00           LDA     ($00),Y             ; {ram.GP_00}
8126: 99 A7 6B        STA     $6BA7,Y             ; 
8129: 88              DEY                         ; 
812A: 10 F8           BPL     $8124               ; {}
812C: 60              RTS                         ; 
812D: A0 07           LDY     #$07                ; 
812F: BE 5F 81        LDX     $815F,Y             ; {}
8132: B9 67 81        LDA     $8167,Y             ; {}
8135: 9D FE 68        STA     $68FE,X             ; 
8138: 88              DEY                         ; 
8139: 10 F4           BPL     $812F               ; {}
813B: A9 7B           LDA     #$7B                ; 
813D: 8D 09 6A        STA     $6A09               ; {ram.6A09}
8140: A9 7B           LDA     #$7B                ; 
8142: 8D 3A 6A        STA     $6A3A               ; {ram.6A3A}
8145: A9 5A           LDA     #$5A                ; 
8147: 8D 72 6A        STA     $6A72               ; {ram.6A72}
814A: A9 72           LDA     #$72                ; 
814C: 8D BA 68        STA     $68BA               ; {ram.68BA}
814F: A9 72           LDA     #$72                ; 
8151: 8D F2 68        STA     $68F2               ; {ram.68F2}
8154: A9 01           LDA     #$01                ; 
8156: 8D 3A 6B        STA     $6B3A               ; {ram.6B3A}
8159: A9 00           LDA     #$00                ; 
815B: 8D 72 6B        STA     $6B72               ; {ram.6B72}
815E: 60              RTS                         ; 
815F: 0E 0F 22        ASL     $220F               ; 
8162: 34                              ;
8163: 3C                              ;
8164: 45 74           EOR     <$74                ; {ram.0074}
8166: 8B                              ;
8167: 7B                              ;
8168: 83                              ;
8169: 84 0F           STY     <$0F                ; {ram.000F}
816B: 0B                              ;
816C: 12                              ;
816D: 7A                              ;
816E: 2F                              ;
816F: C9 AC           CMP     #$AC                ; 
8171: 89                              ;
8172: B7                              ;
8173: 00              BRK                         ; 
8174: E0 77           CPX     #$77                ; 
8176: 08              PHP                         ; 
8177: FF                              ;
8178: 06 01           ASL     <$01                ; {ram.GP_01}
817A: 28              PLP                         ; 
817B: FF                              ;
817C: FF                              ;
817D: FF                              ;
817E: FF                              ;
817F: FF                              ;
8180: FF                              ;
8181: FF                              ;
8182: FF                              ;
8183: FF                              ;
8184: 07                              ;
8185: 00              BRK                         ; 
8186: 00              BRK                         ; 
8187: 00              BRK                         ; 
8188: 00              BRK                         ; 
8189: 00              BRK                         ; 
818A: 00              BRK                         ; 
818B: 00              BRK                         ; 
818C: FF                              ;
818D: DB                              ;
818E: 00              BRK                         ; 
818F: 00              BRK                         ; 
8190: 00              BRK                         ; 
8191: 00              BRK                         ; 
8192: 00              BRK                         ; 
8193: 00              BRK                         ; 
8194: 00              BRK                         ; 
8195: 20 65 42        JSR     $4265               ; 
8198: FF                              ;
8199: 20 85 02        JSR     $0285               ; {ram.0285}
819C: FF                              ;
819D: FB                              ;
819E: 20 A5 02        JSR     $02A5               ; {ram.02A5}
81A1: FF                              ;
81A2: 67                              ;
81A3: 20 C5 42        JSR     $42C5               ; 
81A6: FF                              ;
81A7: FF                              ;
81A8: C9 AC           CMP     #$AC                ; 
81AA: 89                              ;
81AB: 87                              ;
81AC: 05 00           ORA     <$00                ; {ram.GP_00}
81AE: 75 20           ADC     <$20,X              ; {ram.0020}
81B0: FF                              ;
81B1: 06 03           ASL     <$03                ; {ram.GP_03}
81B3: 56 FF           LSR     $FF,X               ; {ram.CUR_2000}
81B5: FF                              ;
81B6: FF                              ;
81B7: FF                              ;
81B8: FF                              ;
81B9: FF                              ;
81BA: FF                              ;
81BB: FF                              ;
81BC: FF                              ;
81BD: 30 00           BMI     $81BF               ; {}
81BF: 00              BRK                         ; 
81C0: 00              BRK                         ; 
81C1: 00              BRK                         ; 
81C2: 00              BRK                         ; 
81C3: 30 00           BMI     $81C5               ; {}
81C5: 00              BRK                         ; 
81C6: 00              BRK                         ; 
81C7: 00              BRK                         ; 
81C8: 7F                              ;
81C9: 03                              ;
81CA: 00              BRK                         ; 
81CB: 00              BRK                         ; 
81CC: 00              BRK                         ; 
81CD: 00              BRK                         ; 
81CE: 20 67 01        JSR     $0167               ; {ram.0167}
81D1: FB                              ;
81D2: 20 82 01        JSR     $0182               ; {ram.0182}
81D5: FF                              ;
81D6: 20 87 C3        JSR     $C387               ; 
81D9: FF                              ;
81DA: 20 C8 01        JSR     $01C8               ; {ram.01C8}
81DD: FF                              ;
81DE: FF                              ;
81DF: C9 AC           CMP     #$AC                ; 
81E1: 89                              ;
81E2: 37                              ;
81E3: 0D C8 79        ORA     $79C8               ; {ram.79C8}
81E6: 1B                              ;
81E7: FF                              ;
81E8: 06 02           ASL     <$02                ; {ram.GP_02}
81EA: 09 0B           ORA     #$0B                ; 
81EC: FF                              ;
81ED: FF                              ;
81EE: FF                              ;
81EF: FF                              ;
81F0: FF                              ;
81F1: FF                              ;
81F2: FF                              ;
81F3: FF                              ;
81F4: 2B                              ;
81F5: 00              BRK                         ; 
81F6: 00              BRK                         ; 
81F7: 00              BRK                         ; 
81F8: 00              BRK                         ; 
81F9: 00              BRK                         ; 
81FA: 00              BRK                         ; 
81FB: 7F                              ;
81FC: EC 7F 00        CPX     $007F               ; {ram.007F}
81FF: 00              BRK                         ; 
8200: 00              BRK                         ; 
8201: 00              BRK                         ; 
8202: 00              BRK                         ; 
8203: 00              BRK                         ; 
8204: 00              BRK                         ; 
8205: 20 64 03        JSR     $0364               ; {ram.0364}
8208: FB                              ;
8209: FF                              ;
820A: FB                              ;
820B: 20 84 03        JSR     $0384               ; {ram.0384}
820E: FF                              ;
820F: 67                              ;
8210: FF                              ;
8211: 20 A4 43        JSR     $43A4               ; 
8214: FF                              ;
8215: 20 C4 03        JSR     $03C4               ; {ram.03C4}
8218: FF                              ;
8219: 24 FF           BIT     <$FF                ; {ram.CUR_2000}
821B: FF                              ;
821C: C9 AC           CMP     #$AC                ; 
821E: 89                              ;
821F: 86 06           STX     <$06                ; {ram.0006}
8221: 10 72           BPL     $8295               ; {}
8223: 00              BRK                         ; 
8224: FF                              ;
8225: 06 05           ASL     <$05                ; {ram.0005}
8227: 21 58           AND     ($58,X)             ; {ram.0058}
8229: 7A                              ;
822A: FF                              ;
822B: FF                              ;
822C: FF                              ;
822D: FF                              ;
822E: FF                              ;
822F: FF                              ;
8230: FF                              ;
8231: 10 00           BPL     $8233               ; {}
8233: 00              BRK                         ; 
8234: 00              BRK                         ; 
8235: 00              BRK                         ; 
8236: 00              BRK                         ; 
8237: 00              BRK                         ; 
8238: CF                              ;
8239: DB                              ;
823A: F3                              ;
823B: 00              BRK                         ; 
823C: 00              BRK                         ; 
823D: 00              BRK                         ; 
823E: 00              BRK                         ; 
823F: 00              BRK                         ; 
8240: 00              BRK                         ; 
8241: 00              BRK                         ; 
8242: 20 64 43        JSR     $4364               ; 
8245: FF                              ;
8246: 20 85 02        JSR     $0285               ; {ram.0285}
8249: FB                              ;
824A: FF                              ;
824B: 20 A4 02        JSR     $02A4               ; {ram.02A4}
824E: FF                              ;
824F: 67                              ;
8250: 20 C4 43        JSR     $43C4               ; 
8253: FF                              ;
8254: FF                              ;
8255: C9 AC           CMP     #$AC                ; 
8257: 89                              ;
8258: 87                              ;
8259: 0A              ASL     A                   ; 
825A: B0 7D           BCS     $82D9               ; {}
825C: 4F                              ;
825D: FF                              ;
825E: 06 04           ASL     <$04                ; {ram.0004}
8260: 0F                              ;
8261: 6A              ROR     A                   ; 
8262: 7F                              ;
8263: FF                              ;
8264: FF                              ;
8265: FF                              ;
8266: FF                              ;
8267: FF                              ;
8268: FF                              ;
8269: FF                              ;
826A: 5F                              ;
826B: 00              BRK                         ; 
826C: 00              BRK                         ; 
826D: 00              BRK                         ; 
826E: 00              BRK                         ; 
826F: 00              BRK                         ; 
8270: 00              BRK                         ; 
8271: FF                              ;
8272: FF                              ;
8273: E7                              ;
8274: 7E 00 00        ROR     $0000,X             ; {ram.GP_00}
8277: 00              BRK                         ; 
8278: 00              BRK                         ; 
8279: 00              BRK                         ; 
827A: 00              BRK                         ; 
827B: 20 64 04        JSR     $0464               ; {ram.0464}
827E: FF                              ;
827F: FF                              ;
8280: FF                              ;
8281: FB                              ;
8282: 20 84 04        JSR     $0484               ; {ram.0484}
8285: FF                              ;
8286: FF                              ;
8287: 67                              ;
8288: FF                              ;
8289: 20 A4 04        JSR     $04A4               ; {ram.04A4}
828C: FF                              ;
828D: FF                              ;
828E: FB                              ;
828F: FF                              ;
8290: 20 C4 04        JSR     $04C4               ; {ram.04C4}
8293: FF                              ;
8294: FF                              ;
8295: FF                              ;
8296: 67                              ;
8297: FF                              ;
8298: 49 79           EOR     #$79                ; 
829A: 89                              ;
829B: 56 04           LSR     $04,X               ; {ram.0004}
829D: 00              BRK                         ; 
829E: 74                              ;
829F: 16 FF           ASL     $FF,X               ; {ram.CUR_2000}
82A1: 06 06           ASL     <$06                ; {ram.0006}
82A3: 03                              ;
82A4: 73                              ;
82A5: 46 FF           LSR     <$FF                ; {ram.CUR_2000}
82A7: FF                              ;
82A8: FF                              ;
82A9: FF                              ;
82AA: FF                              ;
82AB: FF                              ;
82AC: FF                              ;
82AD: 26 00           ROL     <$00                ; {ram.GP_00}
82AF: 00              BRK                         ; 
82B0: 00              BRK                         ; 
82B1: 00              BRK                         ; 
82B2: 00              BRK                         ; 
82B3: 04                              ;
82B4: 0C                              ;
82B5: 7E FF 80        ROR     $80FF,X             ; {}
82B8: F0 00           BEQ     $82BA               ; {}
82BA: 00              BRK                         ; 
82BB: 00              BRK                         ; 
82BC: 00              BRK                         ; 
82BD: 00              BRK                         ; 
82BE: 20 65 03        JSR     $0365               ; {ram.0365}
82C1: FB                              ;
82C2: FF                              ;
82C3: 67                              ;
82C4: 20 68 C2        JSR     $C268               ; 
82C7: FF                              ;
82C8: 20 86 C3        JSR     $C386               ; 
82CB: FF                              ;
82CC: 20 85 83        JSR     $8385               ; {}
82CF: FF                              ;
82D0: FF                              ;
82D1: 67                              ;
82D2: 20 A3 02        JSR     $02A3               ; {ram.02A3}
82D5: FB                              ;
82D6: FF                              ;
82D7: FF                              ;
82D8: C9 AC           CMP     #$AC                ; 
82DA: 89                              ;
82DB: 79 0C C0        ADC     $C00C,Y             ; 
82DE: 7F                              ;
82DF: 2D 7F 07        AND     $077F               ; {ram.077F}
82E2: 08              PHP                         ; 
82E3: 02                              ;
82E4: 03                              ;
82E5: 04                              ;
82E6: 05 20           ORA     <$20                ; {ram.0020}
82E8: 21 26           AND     ($26,X)             ; {ram.0026}
82EA: 2B                              ;
82EB: 2C FF 3D        BIT     $3DFF               ; 
82EE: 00              BRK                         ; 
82EF: 00              BRK                         ; 
82F0: 00              BRK                         ; 
82F1: 00              BRK                         ; 
82F2: FE FE 82        INC     $82FE,X             ; {}
82F5: 82                              ;
82F6: 82                              ;
82F7: BE 80 FF        LDX     $FF80,Y             ; 
82FA: 00              BRK                         ; 
82FB: 00              BRK                         ; 
82FC: 00              BRK                         ; 
82FD: 00              BRK                         ; 
82FE: 20 62 C3        JSR     $C362               ; 
8301: FF                              ;
8302: 20 63 C3        JSR     $C363               ; 
8305: FF                              ;
8306: 20 64 45        JSR     $4564               ; 
8309: 67                              ;
830A: 20 69 C4        JSR     $C469               ; 
830D: FF                              ;
830E: 20 87 C2        JSR     $C287               ; 
8311: FF                              ;
8312: 20 C2 46        JSR     $46C2               ; 
8315: 67                              ;
8316: FF                              ;
8317: C9 AC           CMP     #$AC                ; 
8319: 89                              ;
831A: 57                              ;
831B: 0C                              ;
831C: C0 79           CPY     #$79                ; 
831E: 1B                              ;
831F: 7F                              ;
8320: 07                              ;
8321: 07                              ;
8322: 27                              ;
8323: 30 37           BMI     $835C               ; {}
8325: 60              RTS                         ; 
8326: 67                              ;
8327: 70 FF           BVS     $8328               ; {}
8329: FF                              ;
832A: FF                              ;
832B: FF                              ;
832C: 1C                              ;
832D: 00              BRK                         ; 
832E: 00              BRK                         ; 
832F: 00              BRK                         ; 
8330: 00              BRK                         ; 
8331: 01 01           ORA     ($01,X)             ; {ram.GP_01}
8333: 7D 5D 5D        ADC     $5D5D,X             ; 
8336: 41 7F           EOR     ($7F,X)             ; {ram.007F}
8338: 00              BRK                         ; 
8339: 00              BRK                         ; 
833A: 00              BRK                         ; 
833B: 00              BRK                         ; 
833C: 00              BRK                         ; 
833D: 20 64 45        JSR     $4564               ; 
8340: FB                              ;
8341: 20 84 05        JSR     $0584               ; {ram.0584}
8344: FF                              ;
8345: FB                              ;
8346: FB                              ;
8347: 24 FF           BIT     <$FF                ; {ram.CUR_2000}
8349: 20 A4 43        JSR     $43A4               ; 
834C: FF                              ;
834D: 20 A8 01        JSR     $01A8               ; {ram.01A8}
8350: FF                              ;
8351: 20 C2 46        JSR     $46C2               ; 
8354: FB                              ;
8355: 20 C8 01        JSR     $01C8               ; {ram.01C8}
8358: FF                              ;
8359: FF                              ;
835A: C9 AC           CMP     #$AC                ; 
835C: 89                              ;
835D: B6 04           LDX     $04,Y               ; {ram.0004}
835F: 00              BRK                         ; 
8360: 74                              ;
8361: 07                              ;
8362: 7F                              ;
8363: 07                              ;
8364: 09 71           ORA     #$71                ; 
8366: 72                              ;
8367: 75 76           ADC     <$76,X              ; {ram.0076}
8369: 77                              ;
836A: FF                              ;
836B: FF                              ;
836C: FF                              ;
836D: FF                              ;
836E: FF                              ;
836F: 17                              ;
8370: 00              BRK                         ; 
8371: 00              BRK                         ; 
8372: 00              BRK                         ; 
8373: 00              BRK                         ; 
8374: CC DE 76        CPY     $76DE               ; {ram.76DE}
8377: 7F                              ;
8378: 7F                              ;
8379: 76 DE           ROR     <$DE,X              ; {ram.00DE}
837B: CC 00 00        CPY     $0000               ; {ram.GP_00}
837E: 00              BRK                         ; 
837F: 00              BRK                         ; 
8380: 20 62 48        JSR     $4862               ; 
8383: FF                              ;
8384: 20 64 44        JSR     $4464               ; 
8387: FB                              ;
8388: 20 83 46        JSR     $4683               ; 
838B: FB                              ;
838C: 20 84 44        JSR     $4484               ; 
838F: FF                              ;
8390: 20 A2 08        JSR     $08A2               ; 
8393: FF                              ;
8394: FF                              ;
8395: FB                              ;
8396: FF                              ;
8397: FF                              ;
8398: FB                              ;
8399: FF                              ;
839A: FF                              ;
839B: 20 C3 46        JSR     $46C3               ; 
839E: 67                              ;
839F: 20 C5 42        JSR     $42C5               ; 
83A2: FF                              ;
83A3: FF                              ;
83A4: 6F                              ;
83A5: 81 A8           STA     ($A8,X)             ; {ram.00A8}
83A7: 81 DF           STA     ($DF,X)             ; {ram.00DF}
83A9: 81 1C           STA     ($1C,X)             ; {ram.001C}
83AB: 82                              ;
83AC: 55 82           EOR     $82,X               ; {ram.0082}
83AE: 98              TYA                         ; 
83AF: 82                              ;
83B0: D8              CLD                         ; 
83B1: 82                              ;
83B2: 17                              ;
83B3: 83                              ;
83B4: 5A                              ;
83B5: 83                              ;
83B6: 39 37 3D        AND     $3D37,Y             ; 
83B9: 39 43 40        AND     $4043,Y             ; 
83BC: 3F                              ;
83BD: 43                              ;
83BE: 4A              LSR     A                   ; 
83BF: FF                              ;
83C0: FF                              ;
83C1: FF                              ;
83C2: FF                              ;
83C3: FF                              ;
83C4: FF                              ;
83C5: FF                              ;
83C6: FF                              ;
83C7: FF                              ;
83C8: FF                              ;
83C9: FF                              ;
83CA: FF                              ;
83CB: FF                              ;
83CC: FF                              ;
83CD: FF                              ;
83CE: FF                              ;
83CF: FF                              ;
83D0: FF                              ;
83D1: FF                              ;
83D2: FF                              ;
83D3: FF                              ;
83D4: FF                              ;
83D5: FF                              ;
83D6: FF                              ;
83D7: FF                              ;
83D8: FF                              ;
83D9: FF                              ;
83DA: FF                              ;
83DB: FF                              ;
83DC: FF                              ;
83DD: FF                              ;
83DE: FF                              ;
83DF: FF                              ;
83E0: FF                              ;
83E1: FF                              ;
83E2: FF                              ;
83E3: FF                              ;
83E4: FF                              ;
83E5: FF                              ;
83E6: FF                              ;
83E7: FF                              ;
83E8: FF                              ;
83E9: FF                              ;
83EA: FF                              ;
83EB: FF                              ;
83EC: FF                              ;
83ED: FF                              ;
83EE: FF                              ;
83EF: FF                              ;
83F0: FF                              ;
83F1: FF                              ;
83F2: FF                              ;
83F3: FF                              ;
83F4: FF                              ;
83F5: FF                              ;
83F6: FF                              ;
83F7: FF                              ;
83F8: FF                              ;
83F9: FF                              ;
83FA: FF                              ;
83FB: FF                              ;
83FC: FF                              ;
83FD: FF                              ;
83FE: FF                              ;
83FF: FF                              ;
8400: A3                              ;
8401: 93                              ;
8402: 63                              ;
8403: 73                              ;
8404: C3                              ;
8405: 53                              ;
8406: B3                              ;
8407: A3                              ;
8408: 03                              ;
8409: 93                              ;
840A: 2B                              ;
840B: 73                              ;
840C: 83                              ;
840D: 93                              ;
840E: 57                              ;
840F: 87                              ;
8410: 93                              ;
8411: 53                              ;
8412: 83                              ;
8413: 23                              ;
8414: C3                              ;
8415: C3                              ;
8416: 63                              ;
8417: 0B                              ;
8418: CB                              ;
8419: 4B                              ;
841A: 6B                              ;
841B: 93                              ;
841C: 33                              ;
841D: 27                              ;
841E: CF                              ;
841F: 67                              ;
8420: 50 50           BVC     $8472               ; {}
8422: 73                              ;
8423: 43                              ;
8424: 03                              ;
8425: A3                              ;
8426: 3B                              ;
8427: EB                              ;
8428: EB                              ;
8429: B3                              ;
842A: 03                              ;
842B: B3                              ;
842C: 93                              ;
842D: 5F                              ;
842E: 0F                              ;
842F: 60              RTS                         ; 
8430: 70 70           BVS     $84A2               ; {}
8432: 03                              ;
8433: A3                              ;
8434: 43                              ;
8435: 0B                              ;
8436: 0B                              ;
8437: 73                              ;
8438: 0B                              ;
8439: 03                              ;
843A: C3                              ;
843B: 63                              ;
843C: 72                              ;
843D: 92                              ;
843E: 0F                              ;
843F: 0F                              ;
8440: 00              BRK                         ; 
8441: 00              BRK                         ; 
8442: 63                              ;
8443: 03                              ;
8444: 4B                              ;
8445: 83                              ;
8446: 8A              TXA                         ; 
8447: BA              TSX                         ; 
8448: BA              TSX                         ; 
8449: 32                              ;
844A: B2                              ;
844B: C2                              ;
844C: 02                              ;
844D: C2                              ;
844E: 72                              ;
844F: 0F                              ;
8450: 00              BRK                         ; 
8451: A3                              ;
8452: 03                              ;
8453: 83                              ;
8454: 0A              ASL     A                   ; 
8455: 0A              ASL     A                   ; 
8456: BA              TSX                         ; 
8457: 02                              ;
8458: C2                              ;
8459: 0A              ASL     A                   ; 
845A: 0A              ASL     A                   ; 
845B: 32                              ;
845C: 02                              ;
845D: 02                              ;
845E: 72                              ;
845F: 0F                              ;
8460: C3                              ;
8461: 03                              ;
8462: 63                              ;
8463: 73                              ;
8464: 72                              ;
8465: 0A              ASL     A                   ; 
8466: 72                              ;
8467: 72                              ;
8468: 32                              ;
8469: 0A              ASL     A                   ; 
846A: DA                              ;
846B: 52                              ;
846C: 42                              ;
846D: 62                              ;
846E: C2                              ;
846F: 3F                              ;
8470: B3                              ;
8471: 53                              ;
8472: 43                              ;
8473: 03                              ;
8474: 82                              ;
8475: 2A              ROL     A                   ; 
8476: 62                              ;
8477: 42                              ;
8478: 52                              ;
8479: 63                              ;
847A: 03                              ;
847B: 9F                              ;
847C: 6F                              ;
847D: 6F                              ;
847E: 0F                              ;
847F: 0F                              ;
8480: 27                              ;
8481: 5F                              ;
8482: 6B                              ;
8483: 5F                              ;
8484: 6B                              ;
8485: 27                              ;
8486: 47                              ;
8487: 5F                              ;
8488: 03                              ;
8489: 4F                              ;
848A: 4B                              ;
848B: 17                              ;
848C: 7B                              ;
848D: 6B                              ;
848E: 63                              ;
848F: 8B                              ;
8490: 5B                              ;
8491: 63                              ;
8492: 7F                              ;
8493: 87                              ;
8494: 5F                              ;
8495: 7B                              ;
8496: 5B                              ;
8497: 03                              ;
8498: 6B                              ;
8499: 1F                              ;
849A: 6F                              ;
849B: 17                              ;
849C: 57                              ;
849D: 53                              ;
849E: 5F                              ;
849F: 5A                              ;
84A0: 44                              ;
84A1: 4C 18 53        JMP     $5318               ; 
84A4: 03                              ;
84A5: 77                              ;
84A6: 7F                              ;
84A7: 6B                              ;
84A8: 86 6B           STX     <$6B                ; {ram.SND_Sq2Fine}
84AA: 03                              ;
84AB: 8F                              ;
84AC: 47                              ;
84AD: 87                              ;
84AE: 03                              ;
84AF: 44                              ;
84B0: 18              CLC                         ; 
84B1: 00              BRK                         ; 
84B2: 03                              ;
84B3: 68              PLA                         ; 
84B4: 83                              ;
84B5: 03                              ;
84B6: 03                              ;
84B7: 07                              ;
84B8: 03                              ;
84B9: 02                              ;
84BA: 47                              ;
84BB: 03                              ;
84BC: 0A              ASL     A                   ; 
84BD: 86 03           STX     <$03                ; {ram.GP_03}
84BF: 03                              ;
84C0: 00              BRK                         ; 
84C1: 00              BRK                         ; 
84C2: 1F                              ;
84C3: 02                              ;
84C4: 76 12           ROR     <$12,X              ; {ram.0012}
84C6: 7E 46 86        ROR     $8646,X             ; {}
84C9: 52                              ;
84CA: 76 6A           ROR     <$6A,X              ; {ram.SND_Sq1Fine}
84CC: 02                              ;
84CD: 7E 8E 03        ROR     $038E,X             ; 
84D0: 00              BRK                         ; 
84D1: 8F                              ;
84D2: 03                              ;
84D3: 8A              TXA                         ; 
84D4: 02                              ;
84D5: 02                              ;
84D6: 8E 02 86        STX     $8602               ; {}
84D9: 02                              ;
84DA: 02                              ;
84DB: 8E 02 02        STX     $0202               ; {ram.0202}
84DE: 7A                              ;
84DF: 03                              ;
84E0: 5B                              ;
84E1: 03                              ;
84E2: 8B                              ;
84E3: 5F                              ;
84E4: 6A              ROR     A                   ; 
84E5: 03                              ;
84E6: 7B                              ;
84E7: 86 5E           STX     <$5E                ; {ram.005E}
84E9: 02                              ;
84EA: 5E 8A 22        LSR     $228A,X             ; 
84ED: 22                              ;
84EE: 8E 77 73        STX     $7377               ; {ram.7377}
84F1: 87                              ;
84F2: 5F                              ;
84F3: 03                              ;
84F4: 0F                              ;
84F5: 66 5A           ROR     <$5A                ; {ram.005A}
84F7: 42                              ;
84F8: 6A              ROR     A                   ; 
84F9: 53                              ;
84FA: 03                              ;
84FB: 47                              ;
84FC: 5B                              ;
84FD: 5F                              ;
84FE: 03                              ;
84FF: 03                              ;
8500: 00              BRK                         ; 
8501: 42                              ;
8502: 42                              ;
8503: 1F                              ;
8504: C1 E6           CMP     ($E6,X)             ; {ram.00E6}
8506: E4 02           CPX     <$02                ; {ram.GP_02}
8508: 1F                              ;
8509: 00              BRK                         ; 
850A: 01 10           ORA     ($10,X)             ; {ram.0010}
850C: CE CE 00        DEC     $00CE               ; {ram.00CE}
850F: 00              BRK                         ; 
8510: 41 E4           EOR     ($E4,X)             ; {ram.00E4}
8512: C1 65           CMP     ($65,X)             ; {ram.0065}
8514: 42                              ;
8515: E4 1F           CPX     <$1F                ; {ram.001F}
8517: 1F                              ;
8518: 1F                              ;
8519: 1F                              ;
851A: CE 00 00        DEC     $0000               ; {ram.GP_00}
851D: DA                              ;
851E: CE DA 21        DEC     $21DA               ; 
8521: 21 02           AND     ($02,X)             ; {ram.GP_02}
8523: 42                              ;
8524: 00              BRK                         ; 
8525: 5A                              ;
8526: DA                              ;
8527: DA                              ;
8528: DA                              ;
8529: 50 CF           BVC     $84FA               ; {}
852B: E7                              ;
852C: 4E AA 49        LSR     $49AA               ; 
852F: 00              BRK                         ; 
8530: 21 21           AND     ($21,X)             ; {ram.0021}
8532: E4 00           CPX     <$00                ; {ram.GP_00}
8534: 4F                              ;
8535: 00              BRK                         ; 
8536: 00              BRK                         ; 
8537: 08              PHP                         ; 
8538: E8              INX                         ; 
8539: 2F                              ;
853A: E7                              ;
853B: 4F                              ;
853C: 0A              ASL     A                   ; 
853D: 43                              ;
853E: AA              TAX                         ; 
853F: 09 21           ORA     #$21                ; 
8541: 21 04           AND     ($04,X)             ; {ram.0004}
8543: 2F                              ;
8544: 47                              ;
8545: 1A                              ;
8546: 00              BRK                         ; 
8547: 00              BRK                         ; 
8548: 50 E8           BVC     $8532               ; {}
854A: CD C4 AA        CMP     $AAC4               ; {}
854D: 43                              ;
854E: 43                              ;
854F: AB                              ;
8550: 82                              ;
8551: 83                              ;
8552: 63                              ;
8553: A2 69           LDX     #$69                ; 
8555: 07                              ;
8556: 47                              ;
8557: 69 69           ADC     #$69                ; 
8559: 5A                              ;
855A: 47                              ;
855B: 63                              ;
855C: 43                              ;
855D: 43                              ;
855E: 83                              ;
855F: AA              TAX                         ; 
8560: E4 83           CPX     <$83                ; {ram.0083}
8562: 83                              ;
8563: EC AA 69        CPX     $69AA               ; {ram.69AA}
8566: 69 47           ADC     #$47                ; 
8568: 47                              ;
8569: 47                              ;
856A: 69 EC           ADC     #$EC                ; 
856C: 44                              ;
856D: 44                              ;
856E: EC A8 5A        CPX     $5AA8               ; 
8571: 83                              ;
8572: 62                              ;
8573: 43                              ;
8574: 0E E7 4E        ASL     $4EE7               ; 
8577: 00              BRK                         ; 
8578: 47                              ;
8579: 8D 4D D0        STA     $D04D               ; 
857C: D0 49           BNE     $85C7               ; {}
857E: 48              PHA                         ; 
857F: 09 00           ORA     #$00                ; 
8581: 01 02           ORA     ($02,X)             ; {ram.GP_02}
8583: 03                              ;
8584: 04                              ;
8585: 85 86           STA     <$86                ; {ram.0086}
8587: 07                              ;
8588: 06 08           ASL     <$08                ; {ram.0008}
858A: 09 0A           ORA     #$0A                ; 
858C: 0B                              ;
858D: 0C                              ;
858E: 0D 0E 0F        ORA     $0F0E               ; 
8591: 90 11           BCC     $85A4               ; {}
8593: 92                              ;
8594: 13                              ;
8595: 94 15           STY     $15,X               ; {ram.0015}
8597: 16 17           ASL     $17,X               ; {ram.0017}
8599: 18              CLC                         ; 
859A: 19 1A 1B        ORA     $1B1A,Y             ; 
859D: 1C                              ;
859E: 1D 1E 1F        ORA     $1F1E,X             ; 
85A1: 20 21 22        JSR     $2221               ; 
85A4: 23                              ;
85A5: 24 25           BIT     <$25                ; {ram.0025}
85A7: 26 27           ROL     <$27                ; {ram.0027}
85A9: 28              PLP                         ; 
85AA: 29 AA           AND     #$AA                ; 
85AC: 2B                              ;
85AD: AC 2D 2E        LDY     $2E2D               ; 
85B0: 2F                              ;
85B1: 30 B1           BMI     $8564               ; {}
85B3: 32                              ;
85B4: 33                              ;
85B5: 34                              ;
85B6: 35 36           AND     $36,X               ; {ram.0036}
85B8: B7                              ;
85B9: 38              SEC                         ; 
85BA: B9 3A 0A        LDA     $0A3A,Y             ; 
85BD: 3B                              ;
85BE: BC 3D 3E        LDY     $3E3D,X             ; 
85C1: 3F                              ;
85C2: 38              SEC                         ; 
85C3: 38              SEC                         ; 
85C4: 40              RTI                         ; 
85C5: 41 42           EOR     ($42,X)             ; {ram.0042}
85C7: 43                              ;
85C8: 44                              ;
85C9: C5 46           CMP     <$46                ; {ram.0046}
85CB: 47                              ;
85CC: C8              INY                         ; 
85CD: 49 4A           EOR     #$4A                ; 
85CF: CB                              ;
85D0: 4C 4D CE        JMP     $CE4D               ; 
85D3: CF                              ;
85D4: D0 51           BNE     $8627               ; {}
85D6: 52                              ;
85D7: D3                              ;
85D8: D4                              ;
85D9: 55 56           EOR     $56,X               ; {ram.0056}
85DB: D7                              ;
85DC: 58              CLI                         ; 
85DD: 59 5A CB        EOR     $CB5A,Y             ; 
85E0: DB                              ;
85E1: 5C                              ;
85E2: 5D DE DF        EOR     $DFDE,X             ; 
85E5: E0 E1           CPX     #$E1                ; 
85E7: 62                              ;
85E8: 63                              ;
85E9: 64                              ;
85EA: E5 E6           SBC     <$E6                ; {ram.00E6}
85EC: 67                              ;
85ED: 68              PLA                         ; 
85EE: E9 EA           SBC     #$EA                ; 
85F0: 6B                              ;
85F1: 6C ED 6E        JMP     ($6EED)             ; {ram.6EED}
85F4: 6F                              ;
85F5: F0 71           BEQ     $8668               ; {}
85F7: 72                              ;
85F8: 73                              ;
85F9: 74                              ;
85FA: 06 75           ASL     <$75                ; {ram.0075}
85FC: 76 76           ROR     <$76,X              ; {ram.0076}
85FE: 77                              ;
85FF: 78              SEI                         ; 
8600: 3F                              ;
8601: 01 7F           ORA     ($7F,X)             ; {ram.007F}
8603: 20 3F 5A        JSR     $5A3F               ; 
8606: 7F                              ;
8607: 02                              ;
8608: 7F                              ;
8609: 7F                              ;
860A: 03                              ;
860B: 7F                              ;
860C: 3F                              ;
860D: 3F                              ;
860E: 3F                              ;
860F: 3F                              ;
8610: 3F                              ;
8611: 3F                              ;
8612: 98              TYA                         ; 
8613: 98              TYA                         ; 
8614: D8              CLD                         ; 
8615: 3F                              ;
8616: 3F                              ;
8617: 3F                              ;
8618: 3F                              ;
8619: 15 7F           ORA     $7F,X               ; {ram.007F}
861B: 3F                              ;
861C: 3F                              ;
861D: 3F                              ;
861E: 1F                              ;
861F: 3F                              ;
8620: E0 98           CPX     #$98                ; 
8622: 58              CLI                         ; 
8623: D8              CLD                         ; 
8624: 98              TYA                         ; 
8625: 58              CLI                         ; 
8626: D8              CLD                         ; 
8627: 1C                              ;
8628: 00              BRK                         ; 
8629: C8              INY                         ; 
862A: 1C                              ;
862B: 19 C6 1C        ORA     $1CC6,Y             ; 
862E: 04                              ;
862F: E2                              ;
8630: 19 12 C4        ORA     $C412,Y             ; 
8633: 3F                              ;
8634: 98              TYA                         ; 
8635: 7F                              ;
8636: 3F                              ;
8637: 98              TYA                         ; 
8638: 7F                              ;
8639: 3F                              ;
863A: 98              TYA                         ; 
863B: 7F                              ;
863C: 00              BRK                         ; 
863D: 00              BRK                         ; 
863E: 00              BRK                         ; 
863F: 00              BRK                         ; 
8640: 00              BRK                         ; 
8641: 00              BRK                         ; 
8642: 00              BRK                         ; 
8643: 00              BRK                         ; 
8644: 00              BRK                         ; 
8645: 00              BRK                         ; 
8646: 00              BRK                         ; 
8647: 00              BRK                         ; 
8648: 00              BRK                         ; 
8649: 00              BRK                         ; 
864A: 00              BRK                         ; 
864B: 00              BRK                         ; 
864C: 00              BRK                         ; 
864D: 00              BRK                         ; 
864E: 0A              ASL     A                   ; 
864F: 0A              ASL     A                   ; 
8650: 0A              ASL     A                   ; 
8651: 00              BRK                         ; 
8652: 00              BRK                         ; 
8653: 00              BRK                         ; 
8654: 00              BRK                         ; 
8655: 00              BRK                         ; 
8656: 00              BRK                         ; 
8657: 00              BRK                         ; 
8658: 00              BRK                         ; 
8659: 00              BRK                         ; 
865A: 28              PLP                         ; 
865B: 00              BRK                         ; 
865C: 44                              ;
865D: 05 0A           ORA     <$0A                ; {ram.000A}
865F: 14                              ;
8660: 0A              ASL     A                   ; 
8661: 1E 32 82        ASL     $8232,X             ; {}
8664: 14                              ;
8665: 50 A0           BVC     $8607               ; {}
8667: 64                              ;
8668: 3C                              ;
8669: 5A                              ;
866A: 64                              ;
866B: 0A              ASL     A                   ; 
866C: 50 FA           BVC     $8668               ; {}
866E: 3C                              ;
866F: 00              BRK                         ; 
8670: 1E 00 00        ASL     $0000,X             ; {ram.GP_00}
8673: 64                              ;
8674: 00              BRK                         ; 
8675: 00              BRK                         ; 
8676: 0A              ASL     A                   ; 
8677: 00              BRK                         ; 
8678: FF                              ;
8679: FF                              ;
867A: FF                              ;
867B: FF                              ;
867C: FF                              ;
867D: FF                              ;
867E: FF                              ;
867F: FF                              ;
8680: 83                              ;
8681: 00              BRK                         ; 
8682: 83                              ;
8683: 03                              ;
8684: 00              BRK                         ; 
8685: 45 84           EOR     <$84                ; {ram.0084}
8687: 03                              ;
8688: 00              BRK                         ; 
8689: A4 00           LDY     <$00                ; {ram.GP_00}
868B: 03                              ;
868C: 00              BRK                         ; 
868D: 00              BRK                         ; 
868E: 0B                              ;
868F: 03                              ;
8690: 00              BRK                         ; 
8691: A4 00           LDY     <$00                ; {ram.GP_00}
8693: 00              BRK                         ; 
8694: 00              BRK                         ; 
8695: 80                              ;
8696: 00              BRK                         ; 
8697: 00              BRK                         ; 
8698: 82                              ;
8699: 82                              ;
869A: 03                              ;
869B: A4 02           LDY     <$02                ; {ram.GP_02}
869D: 02                              ;
869E: 00              BRK                         ; 
869F: 03                              ;
86A0: B3                              ;
86A1: 62                              ;
86A2: 03                              ;
86A3: 11 00           ORA     ($00),Y             ; {ram.GP_00}
86A5: 00              BRK                         ; 
86A6: 00              BRK                         ; 
86A7: 40              RTI                         ; 
86A8: 05 84           ORA     <$84                ; {ram.0084}
86AA: 00              BRK                         ; 
86AB: 84 45           STY     <$45                ; {ram.0045}
86AD: 00              BRK                         ; 
86AE: 00              BRK                         ; 
86AF: 03                              ;
86B0: 84 04           STY     <$04                ; {ram.0004}
86B2: 00              BRK                         ; 
86B3: 00              BRK                         ; 
86B4: 02                              ;
86B5: 00              BRK                         ; 
86B6: 00              BRK                         ; 
86B7: 03                              ;
86B8: 00              BRK                         ; 
86B9: 80                              ;
86BA: 84 02           STY     <$02                ; {ram.GP_02}
86BC: 03                              ;
86BD: 02                              ;
86BE: 00              BRK                         ; 
86BF: 00              BRK                         ; 
86C0: 00              BRK                         ; 
86C1: 00              BRK                         ; 
86C2: 01 00           ORA     ($00,X)             ; {ram.GP_00}
86C4: 00              BRK                         ; 
86C5: 03                              ;
86C6: 06 45           ASL     <$45                ; {ram.0045}
86C8: 02                              ;
86C9: 02                              ;
86CA: 00              BRK                         ; 
86CB: 09 00           ORA     #$00                ; 
86CD: 0C                              ;
86CE: 0A              ASL     A                   ; 
86CF: 00              BRK                         ; 
86D0: 00              BRK                         ; 
86D1: 05 08           ORA     <$08                ; {ram.0008}
86D3: 85 00           STA     <$00                ; {ram.GP_00}
86D5: 00              BRK                         ; 
86D6: 06 08           ASL     <$08                ; {ram.0008}
86D8: 8C 00 00        STY     $0000               ; {ram.GP_00}
86DB: 0D 08 08        ORA     $0808               ; 
86DE: 00              BRK                         ; 
86DF: 00              BRK                         ; 
86E0: 84 08           STY     <$08                ; {ram.0008}
86E2: 4B                              ;
86E3: 05 00           ORA     <$00                ; {ram.GP_00}
86E5: 00              BRK                         ; 
86E6: 00              BRK                         ; 
86E7: 40              RTI                         ; 
86E8: 0C                              ;
86E9: 00              BRK                         ; 
86EA: 05 4D           ORA     <$4D                ; {ram.004D}
86EC: 89                              ;
86ED: 49 84           EOR     #$84                ; 
86EF: 00              BRK                         ; 
86F0: 00              BRK                         ; 
86F1: 48              PHA                         ; 
86F2: 8C 08 03        STY     $0308               ; {ram.0308}
86F5: 00              BRK                         ; 
86F6: 00              BRK                         ; 
86F7: 00              BRK                         ; 
86F8: 0C                              ;
86F9: 22                              ;
86FA: 00              BRK                         ; 
86FB: 40              RTI                         ; 
86FC: 00              BRK                         ; 
86FD: 00              BRK                         ; 
86FE: 00              BRK                         ; 
86FF: 00              BRK                         ; 
8700: 22                              ;
8701: 32                              ;
8702: 22                              ;
8703: 22                              ;
8704: 05 26           ORA     <$26                ; {ram.0026}
8706: 36 64           ROL     $64,X               ; {ram.0064}
8708: 3A                              ;
8709: 36 3E           ROL     $3E,X               ; {ram.003E}
870B: 22                              ;
870C: 22                              ;
870D: 26 22           ROL     <$22                ; {ram.0022}
870F: 69 FE           ADC     #$FE                ; 
8711: 92                              ;
8712: 06 E6           ASL     <$E6                ; {ram.00E6}
8714: 22                              ;
8715: 32                              ;
8716: A6 26           LDX     <$26                ; {ram.0026}
8718: 3E B6 06        ROL     $06B6,X             ; 
871B: E6 F6           INC     <$F6                ; {ram.TileFlagB}
871D: 22                              ;
871E: FE 22 16        INC     $1622,X             ; 
8721: 96 26           STX     $26,Y               ; {ram.0026}
8723: 36 E2           ROL     $E2,X               ; {ram.00E2}
8725: 86 26           STX     <$26                ; {ram.0026}
8727: 22                              ;
8728: 1E A2 26        ASL     $26A2,X             ; 
872B: 22                              ;
872C: A2 06           LDX     #$06                ; 
872E: E2                              ;
872F: 12                              ;
8730: A2 A6           LDX     #$A6                ; 
8732: 26 A2           ROL     <$A2                ; {ram.00A2}
8734: E6 36           INC     <$36                ; {ram.0036}
8736: 26 02           ROL     <$02                ; {ram.GP_02}
8738: FE E6 26        INC     $26E6,X             ; 
873B: F6 E6           INC     $E6,X               ; {ram.00E6}
873D: 22                              ;
873E: 02                              ;
873F: 92                              ;
8740: 02                              ;
8741: 26 36           ROL     <$36                ; {ram.0036}
8743: 12                              ;
8744: 32                              ;
8745: A6 36           LDX     <$36                ; {ram.0036}
8747: 02                              ;
8748: 02                              ;
8749: 22                              ;
874A: 22                              ;
874B: A2 22           LDX     #$22                ; 
874D: FE 1E 92        INC     $921E,X             ; {}
8750: 06 22           ASL     <$22                ; {ram.0022}
8752: A6 82           LDX     <$82                ; {ram.0082}
8754: 86 22           STX     <$22                ; {ram.0022}
8756: A2 06           LDX     #$06                ; 
8758: E2                              ;
8759: 1E 06 02        ASL     $0206,X             ; 
875C: 06 E6           ASL     <$E6                ; {ram.00E6}
875E: 02                              ;
875F: 92                              ;
8760: 32                              ;
8761: 02                              ;
8762: 26 16           ROL     <$16                ; {ram.0016}
8764: 26 E6           ROL     <$E6                ; {ram.00E6}
8766: E2                              ;
8767: 32                              ;
8768: 02                              ;
8769: 06 36           ASL     <$36                ; {ram.0036}
876B: 02                              ;
876C: 26 22           ROL     <$22                ; {ram.0022}
876E: 02                              ;
876F: 86 26           STX     <$26                ; {ram.0026}
8771: 02                              ;
8772: 26 A2           ROL     <$A2                ; {ram.00A2}
8774: 26 09           ROL     <$09                ; {ram.0009}
8776: 02                              ;
8777: 86 06           STX     <$06                ; {ram.0006}
8779: 22                              ;
877A: A6 06           LDX     <$06                ; {ram.0006}
877C: 22                              ;
877D: 02                              ;
877E: 06 22           ASL     <$22                ; {ram.0022}
8780: 34                              ;
8781: A3                              ;
8782: 07                              ;
8783: 26 05           ROL     <$05                ; {ram.0005}
8785: 36 A6           ROL     $A6,X               ; {ram.00A6}
8787: 06 1D           ASL     <$1D                ; {ram.001D}
8789: 32                              ;
878A: 92                              ;
878B: 84 26           STY     <$26                ; {ram.0026}
878D: 22                              ;
878E: E6 69           INC     <$69                ; {ram.0069}
8790: 32                              ;
8791: 92                              ;
8792: 9E                              ;
8793: E6 26           INC     <$26                ; {ram.0026}
8795: 24 33           BIT     <$33                ; {ram.0033}
8797: 84 3E           STY     <$3E                ; {ram.003E}
8799: 03                              ;
879A: 03                              ;
879B: 06 26           ASL     <$26                ; {ram.0026}
879D: 26 32           ROL     <$32                ; {ram.0032}
879F: 84 23           STY     <$23                ; {ram.0023}
87A1: 07                              ;
87A2: 36 A7           ROL     $A7,X               ; {ram.00A7}
87A4: 36 A2           ROL     $A2,X               ; {ram.00A2}
87A6: 17                              ;
87A7: A7                              ;
87A8: 32                              ;
87A9: 87                              ;
87AA: 3E 04 22        ROL     $2204,X             ; 
87AD: 07                              ;
87AE: 36 A6           ROL     $A6,X               ; {ram.00A6}
87B0: 37                              ;
87B1: BF                              ;
87B2: 06 27           ASL     <$27                ; {ram.0027}
87B4: 26 3E           ROL     <$3E                ; {ram.003E}
87B6: 06 27           ASL     <$27                ; {ram.0027}
87B8: 26 3F           ROL     <$3F                ; {ram.003F}
87BA: 06 26           ASL     <$26                ; {ram.0026}
87BC: 27                              ;
87BD: 26 21           ROL     <$21                ; {ram.0021}
87BF: 06 27           ASL     <$27                ; {ram.0027}
87C1: 20 E2 16        JSR     $16E2               ; 
87C4: A2 06           LDX     #$06                ; 
87C6: 23                              ;
87C7: 07                              ;
87C8: 26 22           ROL     <$22                ; {ram.0022}
87CA: 16 B6           ASL     $B6,X               ; {ram.00B6}
87CC: B2                              ;
87CD: 85 22           STA     <$22                ; {ram.0022}
87CF: 06 23           ASL     <$23                ; {ram.0023}
87D1: 06 3E           ASL     <$3E                ; {ram.003E}
87D3: 02                              ;
87D4: 06 3F           ASL     <$3F                ; {ram.003F}
87D6: E2                              ;
87D7: 07                              ;
87D8: 27                              ;
87D9: 36 A2           ROL     $A2,X               ; {ram.00A2}
87DB: 12                              ;
87DC: 9E                              ;
87DD: E6 36           INC     <$36                ; {ram.0036}
87DF: A6 32           LDX     <$32                ; {ram.0032}
87E1: 36 A7           ROL     $A7,X               ; {ram.00A7}
87E3: 26 32           ROL     <$32                ; {ram.0032}
87E5: 92                              ;
87E6: 97                              ;
87E7: A4 26           LDY     <$26                ; {ram.0026}
87E9: 26 24           ROL     <$24                ; {ram.0024}
87EB: 26 22           ROL     <$22                ; {ram.0022}
87ED: E2                              ;
87EE: 16 A6           ASL     $A6,X               ; {ram.00A6}
87F0: 22                              ;
87F1: 07                              ;
87F2: 22                              ;
87F3: 03                              ;
87F4: 06 09           ASL     <$09                ; {ram.0009}
87F6: 23                              ;
87F7: 06 36           ASL     <$36                ; {ram.0036}
87F9: A3                              ;
87FA: 07                              ;
87FB: 22                              ;
87FC: 07                              ;
87FD: 23                              ;
87FE: 06 22           ASL     <$22                ; {ram.0022}
8800: 0E DB 09        ASL     $09DB               ; 
8803: 00              BRK                         ; 
8804: 98              TYA                         ; 
8805: 8C 00 69        STY     $6900               ; {ram.6900}
8808: 69 7B           ADC     #$7B                ; 
880A: B3                              ;
880B: 0C                              ;
880C: 00              BRK                         ; 
880D: 00              BRK                         ; 
880E: 32                              ;
880F: 68              PLA                         ; 
8810: 3C                              ;
8811: 35 52           AND     $52,X               ; {ram.0052}
8813: 03                              ;
8814: 00              BRK                         ; 
8815: 0D DB 0F        ORA     $0FDB               ; 
8818: 04                              ;
8819: B3                              ;
881A: A4 FC           LDY     <$FC                ; {ram.CUR_VScroll}
881C: 34                              ;
881D: B3                              ;
881E: 46 0B           LSR     <$0B                ; {ram.000B}
8820: 52                              ;
8821: 55 0A           EOR     $0A,X               ; {ram.000A}
8823: 06 39           ASL     <$39                ; {ram.0039}
8825: 56 70           LSR     $70,X               ; {ram.0070}
8827: B0 7B           BCS     $88A4               ; {}
8829: 7B                              ;
882A: DB                              ;
882B: 0B                              ;
882C: F7                              ;
882D: 72                              ;
882E: E8              INX                         ; 
882F: 55 72           EOR     $72,X               ; {ram.0072}
8831: 52                              ;
8832: B3                              ;
8833: 2A              ROL     A                   ; 
8834: B0 3D           BCS     $8873               ; {}
8836: 00              BRK                         ; 
8837: 0B                              ;
8838: FC                              ;
8839: 52                              ;
883A: FC                              ;
883B: AD 7B 00        LDA     $007B               ; {ram.007B}
883E: 01 EE           ORA     ($EE,X)             ; {ram.00EE}
8840: 53                              ;
8841: 0C                              ;
8842: 15 55           ORA     $55,X               ; {ram.0055}
8844: 06 E7           ASL     <$E7                ; {ram.00E7}
8846: 00              BRK                         ; 
8847: 70 09           BVS     $8852               ; {}
8849: EF                              ;
884A: 5B                              ;
884B: 13                              ;
884C: AD 3C 68        LDA     $683C               ; {ram.683C}
884F: 05 52           ORA     <$52                ; {ram.0052}
8851: DB                              ;
8852: 9B                              ;
8853: 6A              ROR     A                   ; 
8854: DB                              ;
8855: 53                              ;
8856: 31 53           AND     ($53),Y             ; {ram.0053}
8858: DB                              ;
8859: 4B                              ;
885A: EE 0B 0B        INC     $0B0B               ; 
885D: EF                              ;
885E: 46 55           LSR     <$55                ; {ram.0055}
8860: CB                              ;
8861: 12                              ;
8862: 52                              ;
8863: 2A              ROL     A                   ; 
8864: 4C 70 30        JMP     $3070               ; 
8867: 0E 53 CB        ASL     $CB53               ; 
886A: 0D 53 A8        ORA     $A853               ; {}
886D: 68              PLA                         ; 
886E: 28              PLP                         ; 
886F: 95 DB           STA     $DB,X               ; {ram.00DB}
8871: 00              BRK                         ; 
8872: 1B                              ;
8873: 00              BRK                         ; 
8874: 6A              ROR     A                   ; 
8875: C8              INY                         ; 
8876: 00              BRK                         ; 
8877: 56 64           LSR     $64,X               ; {ram.0064}
8879: 00              BRK                         ; 
887A: 64                              ;
887B: 93                              ;
887C: 00              BRK                         ; 
887D: 00              BRK                         ; 
887E: 68              PLA                         ; 
887F: 6A              ROR     A                   ; 
8880: A6 16           LDX     <$16                ; {ram.0016}
8882: 81 29           STA     ($29,X)             ; {ram.0029}
8884: 3F                              ;
8885: 62                              ;
8886: 5A                              ;
8887: 3E 3E CA        ROL     $CA3E,X             ; 
888A: 8A              TXA                         ; 
888B: A6 29           LDX     <$29                ; {ram.0029}
888D: 29 25           AND     #$25                ; 
888F: 3F                              ;
8890: 06 26           ASL     <$26                ; {ram.0026}
8892: 4A              LSR     A                   ; 
8893: 85 29           STA     <$29                ; {ram.0029}
8895: A6 18           LDX     <$18                ; {ram.0018}
8897: A6 85           LDX     <$85                ; {ram.0085}
8899: 93                              ;
889A: 18              CLC                         ; 
889B: 83                              ;
889C: 06 9B           ASL     <$9B                ; {ram.009B}
889E: 0D A6 15        ORA     $15A6               ; 
88A1: 12                              ;
88A2: DA                              ;
88A3: 15 24           ORA     $24,X               ; {ram.0024}
88A5: 07                              ;
88A6: 14                              ;
88A7: 95 8D           STA     $8D,X               ; 
88A9: 94 1D           STY     $1D,X               ; {ram.001D}
88AB: A6 80           LDX     <$80                ; {ram.0080}
88AD: 93                              ;
88AE: 1D 00 98        ORA     $9800,X             ; {}
88B1: 17                              ;
88B2: CA              DEX                         ; 
88B3: 17                              ;
88B4: 1E 04 29        ASL     $2904,X             ; 
88B7: 17                              ;
88B8: CA              DEX                         ; 
88B9: 13                              ;
88BA: E2                              ;
88BB: CA              DEX                         ; 
88BC: 97                              ;
88BD: 29 A5           AND     #$A5                ; 
88BF: 80                              ;
88C0: 15 A6           ORA     $A6,X               ; {ram.00A6}
88C2: 62                              ;
88C3: 1F                              ;
88C4: 02                              ;
88C5: 0D 12 15        ORA     $1512               ; 
88C8: 81 80           STA     ($80,X)             ; {ram.0080}
88CA: 0F                              ;
88CB: 08              PHP                         ; 
88CC: 80                              ;
88CD: 25 02           AND     <$02                ; {ram.GP_02}
88CF: 24 11           BIT     <$11                ; {ram.0011}
88D1: 03                              ;
88D2: 1E 02 03        ASL     $0302,X             ; {ram.0302}
88D5: 13                              ;
88D6: 00              BRK                         ; 
88D7: 17                              ;
88D8: 24 1D           BIT     <$1D                ; {ram.001D}
88DA: 80                              ;
88DB: 00              BRK                         ; 
88DC: 1F                              ;
88DD: 9E                              ;
88DE: 1F                              ;
88DF: 03                              ;
88E0: 3F                              ;
88E1: 02                              ;
88E2: 0C                              ;
88E3: 1E 5A 02        ASL     $025A,X             ; 
88E6: 18              CLC                         ; 
88E7: A6 1D           LDX     <$1D                ; {ram.001D}
88E9: 1B                              ;
88EA: A6 11           LDX     <$11                ; {ram.0011}
88EC: 00              BRK                         ; 
88ED: 03                              ;
88EE: 0D 1E 00        ORA     $001E               ; {ram.001E}
88F1: 21 00           AND     ($00,X)             ; {ram.GP_00}
88F3: 21 1D           AND     ($1D,X)             ; {ram.001D}
88F5: 3F                              ;
88F6: 21 1D           AND     ($1D,X)             ; {ram.001D}
88F8: 1F                              ;
88F9: 21 03           AND     ($03,X)             ; {ram.GP_03}
88FB: 03                              ;
88FC: 21 21           AND     ($21,X)             ; {ram.0021}
88FE: 00              BRK                         ; 
88FF: 3F                              ;
8900: 03                              ;
8901: 99 83 1B        STA     $1B83,Y             ; 
8904: 05 03           ORA     <$03                ; {ram.GP_03}
8906: 03                              ;
8907: 03                              ;
8908: 03                              ;
8909: 03                              ;
890A: 03                              ;
890B: 03                              ;
890C: 1B                              ;
890D: 1B                              ;
890E: 1A                              ;
890F: 0C                              ;
8910: 03                              ;
8911: 03                              ;
8912: 23                              ;
8913: 1A                              ;
8914: 1B                              ;
8915: 03                              ;
8916: 19 03 03        ORA     $0303,Y             ; {ram.0303}
8919: 17                              ;
891A: 99 43 1A        STA     $1A43,Y             ; 
891D: 43                              ;
891E: 40              RTI                         ; 
891F: 03                              ;
8920: 03                              ;
8921: 97                              ;
8922: 03                              ;
8923: 19 1A 63        ORA     $631A,Y             ; 
8926: 19 99 0F        ORA     $0F99,Y             ; 
8929: 99 19 03        STA     $0319,Y             ; 
892C: 43                              ;
892D: 99 03 0F        STA     $0F03,Y             ; 
8930: 83                              ;
8931: 03                              ;
8932: 03                              ;
8933: 19 63 1A        ORA     $1A63,Y             ; 
8936: 1B                              ;
8937: 96 03           STX     $03,Y               ; {ram.GP_03}
8939: 83                              ;
893A: 03                              ;
893B: 03                              ;
893C: 80                              ;
893D: 1B                              ;
893E: 19 00 99        ORA     $9900,Y             ; {}
8941: 03                              ;
8942: 03                              ;
8943: 17                              ;
8944: 1D 39 97        ORA     $9739,X             ; {}
8947: 19 03 19        ORA     $1903,Y             ; 
894A: 00              BRK                         ; 
894B: 19 77 1A        ORA     $1A77,Y             ; 
894E: 19 1E 83        ORA     $831E,Y             ; {}
8951: 19 03 19        ORA     $1903,Y             ; 
8954: 16 19           ASL     $19,X               ; {ram.0019}
8956: 00              BRK                         ; 
8957: 8F                              ;
8958: 19 03 16        ORA     $1603,Y             ; 
895B: 00              BRK                         ; 
895C: 03                              ;
895D: 6F                              ;
895E: 03                              ;
895F: 17                              ;
8960: 0D 03 96        ORA     $9603               ; {}
8963: 03                              ;
8964: 03                              ;
8965: 00              BRK                         ; 
8966: 99 03 16        STA     $1603,Y             ; 
8969: 00              BRK                         ; 
896A: 03                              ;
896B: 19 19 03        ORA     $0319,Y             ; 
896E: 03                              ;
896F: 16 19           ASL     $19,X               ; {ram.0019}
8971: 03                              ;
8972: 19 03 19        ORA     $1903,Y             ; 
8975: 10 03           BPL     $897A               ; {}
8977: 19 03 03        ORA     $0303,Y             ; {ram.0303}
897A: 99 19 03        STA     $0319,Y             ; 
897D: 03                              ;
897E: 19 0A 00        ORA     $000A,Y             ; {ram.000A}
8981: 20 00 30        JSR     $3000               ; 
8984: 30 05           BMI     $898B               ; {}
8986: 00              BRK                         ; 
8987: 00              BRK                         ; 
8988: 00              BRK                         ; 
8989: 05 01           ORA     <$01                ; {ram.GP_01}
898B: 00              BRK                         ; 
898C: 00              BRK                         ; 
898D: 00              BRK                         ; 
898E: 07                              ;
898F: 00              BRK                         ; 
8990: 01 00           ORA     ($00,X)             ; {ram.GP_00}
8992: 04                              ;
8993: 07                              ;
8994: 30 00           BMI     $8996               ; {}
8996: 20 00 01        JSR     $0100               ; {ram.0100}
8999: 07                              ;
899A: 00              BRK                         ; 
899B: 01 07           ORA     ($07,X)             ; {ram.0007}
899D: 00              BRK                         ; 
899E: 17                              ;
899F: 00              BRK                         ; 
89A0: 00              BRK                         ; 
89A1: 00              BRK                         ; 
89A2: 20 37 07        JSR     $0737               ; {ram.0737}
89A5: 00              BRK                         ; 
89A6: 27                              ;
89A7: 20 17 00        JSR     $0017               ; {ram.0017}
89AA: 01 00           ORA     ($00,X)             ; {ram.GP_00}
89AC: 00              BRK                         ; 
89AD: 07                              ;
89AE: 01 07           ORA     ($07,X)             ; {ram.0007}
89B0: 10 01           BPL     $89B3               ; {}
89B2: 05 20           ORA     <$20                ; {ram.0020}
89B4: 01 07           ORA     ($07,X)             ; {ram.0007}
89B6: 20 27 04        JSR     $0427               ; {ram.0427}
89B9: 01 05           ORA     ($05,X)             ; {ram.0005}
89BB: 04                              ;
89BC: 07                              ;
89BD: 00              BRK                         ; 
89BE: 07                              ;
89BF: 00              BRK                         ; 
89C0: 20 00 04        JSR     $0400               ; {ram.0400}
89C3: 00              BRK                         ; 
89C4: 37                              ;
89C5: 10 20           BPL     $89E7               ; {}
89C7: 27                              ;
89C8: 00              BRK                         ; 
89C9: 00              BRK                         ; 
89CA: 07                              ;
89CB: 07                              ;
89CC: 00              BRK                         ; 
89CD: 07                              ;
89CE: 07                              ;
89CF: 07                              ;
89D0: 00              BRK                         ; 
89D1: 10 01           BPL     $89D4               ; {}
89D3: 37                              ;
89D4: 00              BRK                         ; 
89D5: 27                              ;
89D6: 07                              ;
89D7: 27                              ;
89D8: 07                              ;
89D9: 01 00           ORA     ($00,X)             ; {ram.GP_00}
89DB: 07                              ;
89DC: 11 27           ORA     ($27),Y             ; {ram.0027}
89DE: 02                              ;
89DF: 00              BRK                         ; 
89E0: 30 00           BMI     $89E2               ; {}
89E2: 20 00 00        JSR     $0000               ; {ram.GP_00}
89E5: 10 11           BPL     $89F8               ; {}
89E7: 00              BRK                         ; 
89E8: 07                              ;
89E9: 07                              ;
89EA: 00              BRK                         ; 
89EB: 07                              ;
89EC: 00              BRK                         ; 
89ED: 01 00           ORA     ($00,X)             ; {ram.GP_00}
89EF: 10 17           BPL     $8A08               ; {}
89F1: 00              BRK                         ; 
89F2: 17                              ;
89F3: 00              BRK                         ; 
89F4: 00              BRK                         ; 
89F5: 00              BRK                         ; 
89F6: 00              BRK                         ; 
89F7: 27                              ;
89F8: 02                              ;
89F9: 00              BRK                         ; 
89FA: 07                              ;
89FB: 00              BRK                         ; 
89FC: 00              BRK                         ; 
89FD: 00              BRK                         ; 
89FE: 07                              ;
89FF: 20 07 3E        JSR     $3E07               ; 
8A02: 22                              ;
8A03: 26 26           ROL     <$26                ; {ram.0026}
8A05: 26 36           ROL     <$36                ; {ram.0036}
8A07: 32                              ;
8A08: 32                              ;
8A09: 3E 26 36        ROL     $3626,X             ; 
8A0C: 22                              ;
8A0D: 26 3E           ROL     <$3E                ; {ram.003E}
8A0F: 1F                              ;
8A10: 32                              ;
8A11: 1E F6 36        ASL     $36F6,X             ; 
8A14: 22                              ;
8A15: 32                              ;
8A16: A2 92           LDX     #$92                ; 
8A18: 9E                              ;
8A19: E6 26           INC     <$26                ; {ram.0026}
8A1B: A6 E6           LDX     <$E6                ; {ram.00E6}
8A1D: 22                              ;
8A1E: F6 26           INC     $26,X               ; {ram.0026}
8A20: 86 1E           STX     <$1E                ; {ram.001E}
8A22: A6 B6           LDX     <$B6                ; {ram.00B6}
8A24: 02                              ;
8A25: 92                              ;
8A26: 16 92           ASL     $92,X               ; {ram.0092}
8A28: 16 26           ASL     $26,X               ; {ram.0026}
8A2A: 26 26           ROL     <$26                ; {ram.0026}
8A2C: 22                              ;
8A2D: 06 B2           ASL     <$B2                ; {ram.00B2}
8A2F: 4C 36 1E        JMP     $1E36               ; 
8A32: 3E A6 06        ROL     $06A6,X             ; 
8A35: 86 A6           STX     <$A6                ; {ram.00A6}
8A37: 82                              ;
8A38: A6 22           LDX     <$22                ; {ram.0022}
8A3A: 26 22           ROL     <$22                ; {ram.0022}
8A3C: F2                              ;
8A3D: 22                              ;
8A3E: 96 26           STX     $26,Y               ; {ram.0026}
8A40: B6 1E           LDX     $1E,Y               ; {ram.001E}
8A42: FE 32 22        INC     $2232,X             ; 
8A45: 32                              ;
8A46: 22                              ;
8A47: 02                              ;
8A48: 36 E2           ROL     $E2,X               ; {ram.00E2}
8A4A: 1A                              ;
8A4B: 06 86           ASL     <$86                ; {ram.0086}
8A4D: E2                              ;
8A4E: A2 10           LDX     #$10                ; 
8A50: A6 02           LDX     <$02                ; {ram.GP_02}
8A52: E6 96           INC     <$96                ; {ram.0096}
8A54: 02                              ;
8A55: 92                              ;
8A56: 02                              ;
8A57: 06 A2           ASL     <$A2                ; {ram.00A2}
8A59: 12                              ;
8A5A: 32                              ;
8A5B: 22                              ;
8A5C: 26 06           ROL     <$06                ; {ram.0006}
8A5E: F2                              ;
8A5F: 26 14           ROL     <$14                ; {ram.0014}
8A61: 02                              ;
8A62: 26 B6           ROL     <$B6                ; {ram.00B6}
8A64: 06 86           ASL     <$86                ; {ram.0086}
8A66: E2                              ;
8A67: 30 02           BMI     $8A6B               ; {}
8A69: 82                              ;
8A6A: 82                              ;
8A6B: E6 26           INC     <$26                ; {ram.0026}
8A6D: 26 82           ROL     <$82                ; {ram.0082}
8A6F: 7C                              ;
8A70: 63                              ;
8A71: 06 71           ASL     <$71                ; {ram.0071}
8A73: A6 26           LDX     <$26                ; {ram.0026}
8A75: 20 02 52        JSR     $5202               ; 
8A78: 06 02           ASL     <$02                ; {ram.GP_02}
8A7A: 06 29           ASL     <$29                ; {ram.0029}
8A7C: 26 26           ROL     <$26                ; {ram.0026}
8A7E: 02                              ;
8A7F: 26 07           ROL     <$07                ; {ram.0007}
8A81: 37                              ;
8A82: A4 32           LDY     <$32                ; {ram.0032}
8A84: 86 32           STX     <$32                ; {ram.0032}
8A86: 84 26           STY     <$26                ; {ram.0026}
8A88: 32                              ;
8A89: 9E                              ;
8A8A: E6 25           INC     <$25                ; {ram.0025}
8A8C: 33                              ;
8A8D: 86 26           STX     <$26                ; {ram.0026}
8A8F: 1F                              ;
8A90: 26 26           ROL     <$26                ; {ram.0026}
8A92: 36 A7           ROL     $A7,X               ; {ram.00A7}
8A94: 36 A3           ROL     $A3,X               ; {ram.00A3}
8A96: 06 26           ASL     <$26                ; {ram.0026}
8A98: 37                              ;
8A99: B2                              ;
8A9A: 92                              ;
8A9B: 96 A6           STX     $A6,Y               ; {ram.00A6}
8A9D: 32                              ;
8A9E: 9F                              ;
8A9F: 06 26           ASL     <$26                ; {ram.0026}
8AA1: 32                              ;
8AA2: 96 B3           STX     $B3,Y               ; 
8AA4: 87                              ;
8AA5: 36 B2           ROL     $B2,X               ; {ram.00B2}
8AA7: 86 24           STX     <$24                ; {ram.0024}
8AA9: 32                              ;
8AAA: 9E                              ;
8AAB: 06 26           ASL     <$26                ; {ram.0026}
8AAD: 32                              ;
8AAE: 86 3F           STX     <$3F                ; {ram.003F}
8AB0: 32                              ;
8AB1: 86 26           STX     <$26                ; {ram.0026}
8AB3: 33                              ;
8AB4: 87                              ;
8AB5: 26 32           ROL     <$32                ; {ram.0032}
8AB7: 86 3E           STX     <$3E                ; {ram.003E}
8AB9: 13                              ;
8ABA: 86 30           STX     <$30                ; {ram.0030}
8ABC: 86 24           STX     <$24                ; {ram.0024}
8ABE: 3F                              ;
8ABF: E6 27           INC     <$27                ; {ram.0027}
8AC1: 27                              ;
8AC2: 27                              ;
8AC3: 24 22           BIT     <$22                ; {ram.0022}
8AC5: 02                              ;
8AC6: 06 26           ASL     <$26                ; {ram.0026}
8AC8: 24 27           BIT     <$27                ; {ram.0027}
8ACA: 1A                              ;
8ACB: 3F                              ;
8ACC: E6 36           INC     <$36                ; {ram.0036}
8ACE: A6 10           LDX     <$10                ; {ram.0010}
8AD0: 3F                              ;
8AD1: E6 26           INC     <$26                ; {ram.0026}
8AD3: 27                              ;
8AD4: 32                              ;
8AD5: 92                              ;
8AD6: 87                              ;
8AD7: 27                              ;
8AD8: 22                              ;
8AD9: 1E 07 24        ASL     $2407,X             ; 
8ADC: 22                              ;
8ADD: 03                              ;
8ADE: F7                              ;
8ADF: A7                              ;
8AE0: 55 22           EOR     $22,X               ; {ram.0022}
8AE2: 16 A6           ASL     $A6,X               ; {ram.00A6}
8AE4: 22                              ;
8AE5: 03                              ;
8AE6: E4 04           CPX     <$04                ; {ram.0004}
8AE8: 32                              ;
8AE9: 83                              ;
8AEA: 03                              ;
8AEB: 02                              ;
8AEC: 02                              ;
8AED: 07                              ;
8AEE: 26 7C           ROL     <$7C                ; {ram.007C}
8AF0: 05 26           ORA     <$26                ; {ram.0026}
8AF2: 74                              ;
8AF3: 36 A6           ROL     $A6,X               ; {ram.00A6}
8AF5: 61 26           ADC     ($26,X)             ; {ram.0026}
8AF7: 03                              ;
8AF8: 26 23           ROL     <$23                ; {ram.0023}
8AFA: 06 0D           ASL     <$0D                ; {ram.000D}
8AFC: 22                              ;
8AFD: E3                              ;
8AFE: 03                              ;
8AFF: 07                              ;
8B00: 69 EF           ADC     #$EF                ; 
8B02: 0E B3 F7        ASL     $F7B3               ; 
8B05: 7B                              ;
8B06: 0D F1 35        ORA     $35F1               ; 
8B09: BA              TSX                         ; 
8B0A: 45 01           EOR     <$01                ; {ram.GP_01}
8B0C: 31 F9           AND     ($F9),Y             ; {ram.00F9}
8B0E: 4B                              ;
8B0F: 69 F1           ADC     #$F1                ; 
8B11: 3B                              ;
8B12: 3A                              ;
8B13: B3                              ;
8B14: 57                              ;
8B15: 23                              ;
8B16: 08              PHP                         ; 
8B17: FC                              ;
8B18: F5 85           SBC     $85,X               ; {ram.0085}
8B1A: BA              TSX                         ; 
8B1B: 85 38           STA     <$38                ; {ram.0038}
8B1D: 56 33           LSR     $33,X               ; {ram.0033}
8B1F: B8              CLV                         ; 
8B20: 7B                              ;
8B21: 07                              ;
8B22: B3                              ;
8B23: D5 52           CMP     $52,X               ; {ram.0052}
8B25: B3                              ;
8B26: D5 08           CMP     $08,X               ; {ram.0008}
8B28: 36 BA           ROL     $BA,X               ; {ram.00BA}
8B2A: 3D 00 00        AND     $0000,X             ; {ram.GP_00}
8B2D: 35 3C           AND     $3C,X               ; {ram.003C}
8B2F: 77                              ;
8B30: F7                              ;
8B31: FC                              ;
8B32: 37                              ;
8B33: D5 DB           CMP     $DB,X               ; {ram.00DB}
8B35: 7B                              ;
8B36: EF                              ;
8B37: 92                              ;
8B38: BA              TSX                         ; 
8B39: 38              SEC                         ; 
8B3A: 01 10           ORA     ($10,X)             ; {ram.0010}
8B3C: 05 0F           ORA     <$0F                ; {ram.000F}
8B3E: 8C F4 7B        STY     $7BF4               ; {ram.7BF4}
8B41: F6 3E           INC     $3E,X               ; {ram.003E}
8B43: 0C                              ;
8B44: A4 FC           LDY     <$FC                ; {ram.CUR_VScroll}
8B46: A3                              ;
8B47: F1 0F           SBC     ($0F),Y             ; {ram.000F}
8B49: F5 69           SBC     $69,X               ; {ram.0069}
8B4B: 8B                              ;
8B4C: D6 33           DEC     $33,X               ; {ram.0033}
8B4E: F4                              ;
8B4F: 69 53           ADC     #$53                ; 
8B51: 97                              ;
8B52: 07                              ;
8B53: FC                              ;
8B54: 7B                              ;
8B55: 3A                              ;
8B56: B3                              ;
8B57: 7B                              ;
8B58: 31 BA           AND     ($BA),Y             ; {ram.00BA}
8B5A: EA              NOP                         ; 
8B5B: 10 0B           BPL     $8B68               ; {}
8B5D: B0 4C           BCS     $8BAB               ; {}
8B5F: D6 69           DEC     $69,X               ; {ram.0069}
8B61: 07                              ;
8B62: DB                              ;
8B63: 53                              ;
8B64: FC                              ;
8B65: F1 0B           SBC     ($0B),Y             ; {ram.000B}
8B67: C6 EE           DEC     <$EE                ; {ram.00EE}
8B69: 45 DB           EOR     <$DB                ; {ram.00DB}
8B6B: 85 39           STA     <$39                ; {ram.0039}
8B6D: EA              NOP                         ; 
8B6E: 3C                              ;
8B6F: 69 A9           ADC     #$A9                ; 
8B71: 00              BRK                         ; 
8B72: 69 F1           ADC     #$F1                ; 
8B74: 3B                              ;
8B75: 69 00           ADC     #$00                ; 
8B77: 69 68           ADC     #$68                ; 
8B79: 00              BRK                         ; 
8B7A: 01 69           ORA     ($69,X)             ; {ram.0069}
8B7C: F4                              ;
8B7D: 3C                              ;
8B7E: 00              BRK                         ; 
8B7F: EF                              ;
8B80: 3F                              ;
8B81: 93                              ;
8B82: A6 DA           LDX     <$DA                ; {ram.00DA}
8B84: DA                              ;
8B85: CA              DEX                         ; 
8B86: A6 DA           LDX     <$DA                ; {ram.00DA}
8B88: 26 8A           ROL     <$8A                ; {ram.008A}
8B8A: 24 A5           BIT     <$A5                ; {ram.00A5}
8B8C: 23                              ;
8B8D: C8              INY                         ; 
8B8E: 00              BRK                         ; 
8B8F: 3F                              ;
8B90: C8              INY                         ; 
8B91: 25 26           AND     <$26                ; {ram.0026}
8B93: 80                              ;
8B94: 1C                              ;
8B95: 14                              ;
8B96: 8A              TXA                         ; 
8B97: 9F                              ;
8B98: 96 1F           STX     $1F,Y               ; {ram.001F}
8B9A: DA                              ;
8B9B: 00              BRK                         ; 
8B9C: 24 11           BIT     <$11                ; {ram.0011}
8B9E: 24 DA           BIT     <$DA                ; {ram.00DA}
8BA0: DA                              ;
8BA1: A5 9D           LDA     <$9D                ; {ram.009D}
8BA3: 12                              ;
8BA4: 17                              ;
8BA5: 8E 03 8A        STX     $8A03               ; {}
8BA8: 26 DA           ROL     <$DA                ; {ram.00DA}
8BAA: 04                              ;
8BAB: 29 29           AND     #$29                ; 
8BAD: 26 00           ROL     <$00                ; {ram.GP_00}
8BAF: 3E CA A5        ROL     $A5CA,X             ; {}
8BB2: 27                              ;
8BB3: 19 14 A6        ORA     $A614,Y             ; {}
8BB6: 80                              ;
8BB7: 63                              ;
8BB8: 8D 24 A5        STA     $A524               ; {}
8BBB: A6 85           LDX     <$85                ; {ram.0085}
8BBD: A6 23           LDX     <$23                ; {ram.0023}
8BBF: 9B                              ;
8BC0: 96 80           STX     $80,Y               ; {ram.0080}
8BC2: 28              PLP                         ; 
8BC3: A6 00           LDX     <$00                ; {ram.GP_00}
8BC5: 80                              ;
8BC6: 25 9E           AND     <$9E                ; {ram.009E}
8BC8: A6 98           LDX     <$98                ; {ram.0098}
8BCA: 3F                              ;
8BCB: 23                              ;
8BCC: 1C                              ;
8BCD: 25 80           AND     <$80                ; {ram.0080}
8BCF: 3F                              ;
8BD0: 14                              ;
8BD1: 11 9B           ORA     ($9B),Y             ; {ram.009B}
8BD3: A3                              ;
8BD4: 8C 5A 99        STY     $995A               ; {}
8BD7: 94 00           STY     $00,X               ; {ram.GP_00}
8BD9: 82                              ;
8BDA: 19 A6 24        ORA     $24A6,Y             ; 
8BDD: 91 24           STA     ($24),Y             ; {ram.0024}
8BDF: 18              CLC                         ; 
8BE0: 3E DA 26        ROL     $26DA,X             ; 
8BE3: 1B                              ;
8BE4: 9F                              ;
8BE5: 98              TYA                         ; 
8BE6: A6 3E           LDX     <$3E                ; {ram.003E}
8BE8: 80                              ;
8BE9: 23                              ;
8BEA: 09 1E           ORA     #$1E                ; 
8BEC: 24 13           BIT     <$13                ; {ram.0013}
8BEE: 25 3F           AND     <$3F                ; {ram.003F}
8BF0: 3E 1B 3E        ROL     $3E1B,X             ; 
8BF3: 9F                              ;
8BF4: 5A                              ;
8BF5: 3E 21 3E        ROL     $3E21,X             ; 
8BF8: 23                              ;
8BF9: 21 9D           AND     ($9D,X)             ; {ram.009D}
8BFB: 3E DA 23        ROL     $23DA,X             ; 
8BFE: 21 96           AND     ($96,X)             ; {ram.0096}
8C00: 13                              ;
8C01: 83                              ;
8C02: 03                              ;
8C03: 03                              ;
8C04: 03                              ;
8C05: 03                              ;
8C06: 03                              ;
8C07: 03                              ;
8C08: 03                              ;
8C09: 0F                              ;
8C0A: 19 00 00        ORA     $0000,Y             ; {ram.GP_00}
8C0D: 03                              ;
8C0E: 00              BRK                         ; 
8C0F: 0B                              ;
8C10: 03                              ;
8C11: 00              BRK                         ; 
8C12: 0F                              ;
8C13: 83                              ;
8C14: 03                              ;
8C15: 8F                              ;
8C16: 00              BRK                         ; 
8C17: 03                              ;
8C18: 97                              ;
8C19: 03                              ;
8C1A: 23                              ;
8C1B: 00              BRK                         ; 
8C1C: 03                              ;
8C1D: 00              BRK                         ; 
8C1E: 03                              ;
8C1F: 03                              ;
8C20: 03                              ;
8C21: 03                              ;
8C22: 03                              ;
8C23: 00              BRK                         ; 
8C24: 83                              ;
8C25: 00              BRK                         ; 
8C26: 0F                              ;
8C27: 17                              ;
8C28: 03                              ;
8C29: 23                              ;
8C2A: 1A                              ;
8C2B: 1B                              ;
8C2C: 1B                              ;
8C2D: 03                              ;
8C2E: 17                              ;
8C2F: 03                              ;
8C30: 03                              ;
8C31: 03                              ;
8C32: 03                              ;
8C33: 83                              ;
8C34: 0F                              ;
8C35: 16 03           ASL     $03,X               ; {ram.GP_03}
8C37: 00              BRK                         ; 
8C38: 0F                              ;
8C39: 03                              ;
8C3A: 39 23 1A        AND     $1A23,Y             ; 
8C3D: 23                              ;
8C3E: 03                              ;
8C3F: 00              BRK                         ; 
8C40: 0F                              ;
8C41: A3                              ;
8C42: 8E 23 0F        STX     $0F23               ; 
8C45: 03                              ;
8C46: 03                              ;
8C47: 19 03 03        ORA     $0303,Y             ; {ram.0303}
8C4A: 07                              ;
8C4B: 99 39 03        STA     $0339,Y             ; 
8C4E: 0F                              ;
8C4F: 09 83           ORA     #$83                ; 
8C51: 03                              ;
8C52: 23                              ;
8C53: 03                              ;
8C54: 03                              ;
8C55: 03                              ;
8C56: 19 99 0F        ORA     $0F99,Y             ; 
8C59: 03                              ;
8C5A: 96 03           STX     $03,Y               ; {ram.GP_03}
8C5C: 19 99 19        ORA     $1999,Y             ; 
8C5F: 96 03           STX     $03,Y               ; {ram.GP_03}
8C61: 19 0F 03        ORA     $030F,Y             ; 
8C64: 03                              ;
8C65: 83                              ;
8C66: 03                              ;
8C67: 03                              ;
8C68: 00              BRK                         ; 
8C69: 00              BRK                         ; 
8C6A: 83                              ;
8C6B: 03                              ;
8C6C: 00              BRK                         ; 
8C6D: 19 0F 11        ORA     $110F,Y             ; 
8C70: 03                              ;
8C71: 03                              ;
8C72: 03                              ;
8C73: 03                              ;
8C74: 03                              ;
8C75: 03                              ;
8C76: 03                              ;
8C77: 03                              ;
8C78: 19 03 00        ORA     $0003,Y             ; {ram.GP_03}
8C7B: 03                              ;
8C7C: 03                              ;
8C7D: 0F                              ;
8C7E: 03                              ;
8C7F: 99 00 00        STA     $0000,Y             ; {ram.GP_00}
8C82: 00              BRK                         ; 
8C83: 00              BRK                         ; 
8C84: 00              BRK                         ; 
8C85: 05 00           ORA     <$00                ; {ram.GP_00}
8C87: 00              BRK                         ; 
8C88: 00              BRK                         ; 
8C89: 07                              ;
8C8A: 01 07           ORA     ($07,X)             ; {ram.0007}
8C8C: 07                              ;
8C8D: 05 07           ORA     <$07                ; {ram.0007}
8C8F: 00              BRK                         ; 
8C90: 05 07           ORA     <$07                ; {ram.0007}
8C92: 07                              ;
8C93: 00              BRK                         ; 
8C94: 00              BRK                         ; 
8C95: 07                              ;
8C96: 07                              ;
8C97: 10 01           BPL     $8C9A               ; {}
8C99: 01 00           ORA     ($00,X)             ; {ram.GP_00}
8C9B: 07                              ;
8C9C: 01 07           ORA     ($07,X)             ; {ram.0007}
8C9E: 01 01           ORA     ($01,X)             ; {ram.GP_01}
8CA0: 00              BRK                         ; 
8CA1: 20 00 10        JSR     $1000               ; 
8CA4: 00              BRK                         ; 
8CA5: 07                              ;
8CA6: 07                              ;
8CA7: 07                              ;
8CA8: 00              BRK                         ; 
8CA9: 00              BRK                         ; 
8CAA: 07                              ;
8CAB: 00              BRK                         ; 
8CAC: 00              BRK                         ; 
8CAD: 00              BRK                         ; 
8CAE: 07                              ;
8CAF: 00              BRK                         ; 
8CB0: 05 00           ORA     <$00                ; {ram.GP_00}
8CB2: 01 00           ORA     ($00,X)             ; {ram.GP_00}
8CB4: 07                              ;
8CB5: 07                              ;
8CB6: 00              BRK                         ; 
8CB7: 07                              ;
8CB8: 17                              ;
8CB9: 00              BRK                         ; 
8CBA: 07                              ;
8CBB: 00              BRK                         ; 
8CBC: 37                              ;
8CBD: 00              BRK                         ; 
8CBE: 01 07           ORA     ($07,X)             ; {ram.0007}
8CC0: 07                              ;
8CC1: 00              BRK                         ; 
8CC2: 03                              ;
8CC3: 00              BRK                         ; 
8CC4: 07                              ;
8CC5: 00              BRK                         ; 
8CC6: 00              BRK                         ; 
8CC7: 10 10           BPL     $8CD9               ; {}
8CC9: 01 00           ORA     ($00,X)             ; {ram.GP_00}
8CCB: 01 11           ORA     ($11,X)             ; {ram.0011}
8CCD: 01 07           ORA     ($07,X)             ; {ram.0007}
8CCF: 00              BRK                         ; 
8CD0: 01 01           ORA     ($01,X)             ; {ram.GP_01}
8CD2: 01 00           ORA     ($00,X)             ; {ram.GP_00}
8CD4: 00              BRK                         ; 
8CD5: 00              BRK                         ; 
8CD6: 07                              ;
8CD7: 07                              ;
8CD8: 07                              ;
8CD9: 01 00           ORA     ($00,X)             ; {ram.GP_00}
8CDB: 00              BRK                         ; 
8CDC: 07                              ;
8CDD: 00              BRK                         ; 
8CDE: 07                              ;
8CDF: 00              BRK                         ; 
8CE0: 00              BRK                         ; 
8CE1: 10 07           BPL     $8CEA               ; {}
8CE3: 00              BRK                         ; 
8CE4: 00              BRK                         ; 
8CE5: 00              BRK                         ; 
8CE6: 00              BRK                         ; 
8CE7: 00              BRK                         ; 
8CE8: 07                              ;
8CE9: 07                              ;
8CEA: 02                              ;
8CEB: 01 07           ORA     ($07,X)             ; {ram.0007}
8CED: 00              BRK                         ; 
8CEE: 07                              ;
8CEF: 00              BRK                         ; 
8CF0: 00              BRK                         ; 
8CF1: 00              BRK                         ; 
8CF2: 00              BRK                         ; 
8CF3: 00              BRK                         ; 
8CF4: 00              BRK                         ; 
8CF5: 00              BRK                         ; 
8CF6: 00              BRK                         ; 
8CF7: 00              BRK                         ; 
8CF8: 00              BRK                         ; 
8CF9: 00              BRK                         ; 
8CFA: 07                              ;
8CFB: 00              BRK                         ; 
8CFC: 10 07           BPL     $8D05               ; {}
8CFE: 00              BRK                         ; 
8CFF: 00              BRK                         ; 
8D00: 22                              ;
8D01: 26 22           ROL     <$22                ; {ram.0022}
8D03: 04                              ;
8D04: 32                              ;
8D05: 26 26           ROL     <$26                ; {ram.0026}
8D07: 32                              ;
8D08: 26 3B           ROL     <$3B                ; {ram.003B}
8D0A: 36 3A           ROL     $3A,X               ; 
8D0C: 2A              ROL     A                   ; 
8D0D: 32                              ;
8D0E: 26 0E           ROL     <$0E                ; {ram.000E}
8D10: E6 26           INC     <$26                ; {ram.0026}
8D12: 06 22           ASL     <$22                ; {ram.0022}
8D14: 82                              ;
8D15: 36 22           ROL     $22,X               ; {ram.0022}
8D17: 86 26           STX     <$26                ; {ram.0026}
8D19: 22                              ;
8D1A: A2 22           LDX     #$22                ; 
8D1C: 52                              ;
8D1D: 82                              ;
8D1E: 22                              ;
8D1F: 22                              ;
8D20: 22                              ;
8D21: 01 22           ORA     ($22,X)             ; {ram.0022}
8D23: 02                              ;
8D24: 02                              ;
8D25: A2 FE           LDX     #$FE                ; 
8D27: 3E 18 E2        ROL     $E218,X             ; 
8D2A: 0A              ASL     A                   ; 
8D2B: F6 82           INC     $82,X               ; {ram.0082}
8D2D: 02                              ;
8D2E: E6 FE           INC     <$FE                ; {ram.CUR_2001}
8D30: E6 22           INC     <$22                ; {ram.0022}
8D32: E6 0A           INC     <$0A                ; {ram.000A}
8D34: 12                              ;
8D35: 02                              ;
8D36: 06 02           ASL     <$02                ; {ram.GP_02}
8D38: 3E 1E 46        ROL     $461E,X             ; 
8D3B: A6 1E           LDX     <$1E                ; {ram.001E}
8D3D: 06 26           ASL     <$26                ; {ram.0026}
8D3F: EA              NOP                         ; 
8D40: 3E 06 36        ROL     $3606,X             ; 
8D43: 46 92           LSR     <$92                ; {ram.0092}
8D45: E2                              ;
8D46: 51 02           EOR     ($02),Y             ; {ram.GP_02}
8D48: E6 02           INC     <$02                ; {ram.GP_02}
8D4A: 32                              ;
8D4B: 22                              ;
8D4C: 1E 26 26        ASL     $2626,X             ; 
8D4F: 42                              ;
8D50: 1E 26 A6        ASL     $A626,X             ; {}
8D53: 22                              ;
8D54: 82                              ;
8D55: 02                              ;
8D56: 30 02           BMI     $8D5A               ; {}
8D58: 11 1E           ORA     ($1E),Y             ; {ram.001E}
8D5A: 86 02           STX     <$02                ; {ram.GP_02}
8D5C: E2                              ;
8D5D: 26 46           ROL     <$46                ; {ram.0046}
8D5F: F6 06           INC     $06,X               ; {ram.0006}
8D61: 36 22           ROL     $22,X               ; {ram.0022}
8D63: 06 02           ASL     <$02                ; {ram.GP_02}
8D65: 02                              ;
8D66: 36 02           ROL     $02,X               ; {ram.GP_02}
8D68: 32                              ;
8D69: 02                              ;
8D6A: 1F                              ;
8D6B: FE 06 22        INC     $2206,X             ; 
8D6E: 22                              ;
8D6F: A6 26           LDX     <$26                ; {ram.0026}
8D71: A6 02           LDX     <$02                ; {ram.GP_02}
8D73: 06 02           ASL     <$02                ; {ram.GP_02}
8D75: 02                              ;
8D76: A6 02           LDX     <$02                ; {ram.GP_02}
8D78: 86 02           STX     <$02                ; {ram.GP_02}
8D7A: 12                              ;
8D7B: 06 26           ASL     <$26                ; {ram.0026}
8D7D: 02                              ;
8D7E: 06 5E           ASL     <$5E                ; {ram.005E}
8D80: 26 3E           ROL     <$3E                ; {ram.003E}
8D82: 06 24           ASL     <$24                ; {ram.0024}
8D84: 36 BE           ROL     $BE,X               ; {ram.00BE}
8D86: 06 3E           ASL     <$3E                ; {ram.003E}
8D88: 06 7B           ASL     <$7B                ; {ram.007B}
8D8A: 27                              ;
8D8B: 3A                              ;
8D8C: 28              PLP                         ; 
8D8D: 5C                              ;
8D8E: 06 6F           ASL     <$6F                ; {ram.SND_MusEffCnt}
8D90: 36 A6           ROL     $A6,X               ; {ram.00A6}
8D92: 26 3F           ROL     <$3F                ; {ram.003F}
8D94: E7                              ;
8D95: 26 26           ROL     <$26                ; {ram.0026}
8D97: 37                              ;
8D98: A6 22           LDX     <$22                ; {ram.0022}
8D9A: 06 26           ASL     <$26                ; {ram.0026}
8D9C: 2B                              ;
8D9D: 47                              ;
8D9E: 27                              ;
8D9F: 06 26           ASL     <$26                ; {ram.0026}
8DA1: 71 26           ADC     ($26),Y             ; {ram.0026}
8DA3: 2B                              ;
8DA4: 46 24           LSR     <$24                ; {ram.0024}
8DA6: 27                              ;
8DA7: 26 68           ROL     <$68                ; {ram.0068}
8DA9: 33                              ;
8DAA: 86 26           STX     <$26                ; {ram.0026}
8DAC: 23                              ;
8DAD: 12                              ;
8DAE: 87                              ;
8DAF: 27                              ;
8DB0: 26 23           ROL     <$23                ; {ram.0023}
8DB2: 05 33           ORA     <$33                ; {ram.0033}
8DB4: 86 27           STX     <$27                ; {ram.0027}
8DB6: 26 36           ROL     <$36                ; {ram.0036}
8DB8: A6 26           LDX     <$26                ; {ram.0026}
8DBA: 46 26           LSR     <$26                ; {ram.0026}
8DBC: 23                              ;
8DBD: 12                              ;
8DBE: 86 27           STX     <$27                ; {ram.0027}
8DC0: 22                              ;
8DC1: E6 30           INC     <$30                ; {ram.0030}
8DC3: 83                              ;
8DC4: 07                              ;
8DC5: 27                              ;
8DC6: 51 23           EOR     ($23),Y             ; {ram.0023}
8DC8: 07                              ;
8DC9: 37                              ;
8DCA: A2 06           LDX     #$06                ; 
8DCC: 36 AA           ROL     $AA,X               ; 
8DCE: 44                              ;
8DCF: 46 27           LSR     <$27                ; {ram.0027}
8DD1: 22                              ;
8DD2: 17                              ;
8DD3: A3                              ;
8DD4: 07                              ;
8DD5: 26 76           ROL     <$76                ; {ram.0076}
8DD7: 26 22           ROL     <$22                ; {ram.0022}
8DD9: 36 B2           ROL     $B2,X               ; {ram.00B2}
8DDB: 87                              ;
8DDC: 37                              ;
8DDD: BE 06 27        LDX     $2706,Y             ; 
8DE0: 23                              ;
8DE1: 02                              ;
8DE2: 07                              ;
8DE3: 23                              ;
8DE4: 07                              ;
8DE5: 36 A6           ROL     $A6,X               ; {ram.00A6}
8DE7: 32                              ;
8DE8: 86 26           STX     <$26                ; {ram.0026}
8DEA: 1F                              ;
8DEB: 26 22           ROL     <$22                ; {ram.0022}
8DED: E3                              ;
8DEE: 06 26           ASL     <$26                ; {ram.0026}
8DF0: 2B                              ;
8DF1: 46 27           LSR     <$27                ; {ram.0027}
8DF3: 36 27           ROL     $27,X               ; {ram.0027}
8DF5: 27                              ;
8DF6: 26 23           ROL     <$23                ; {ram.0023}
8DF8: 06 27           ASL     <$27                ; {ram.0027}
8DFA: 12                              ;
8DFB: 26 23           ROL     <$23                ; {ram.0023}
8DFD: 03                              ;
8DFE: 06 5E           ASL     <$5E                ; {ram.005E}
8E00: 00              BRK                         ; 
8E01: 63                              ;
8E02: 33                              ;
8E03: 69 DB           ADC     #$DB                ; 
8E05: 03                              ;
8E06: 6D 3D 00        ADC     $003D               ; {ram.003D}
8E09: 68              PLA                         ; 
8E0A: AD 68 12        LDA     $1268               ; 
8E0D: 11 2C           ORA     ($2C),Y             ; {ram.002C}
8E0F: 6B                              ;
8E10: 04                              ;
8E11: 52                              ;
8E12: 2D 7B 7B        AND     $7B7B               ; {ram.7B7B}
8E15: 86 00           STX     <$00                ; {ram.GP_00}
8E17: 05 F9           ORA     <$F9                ; {ram.00F9}
8E19: 3C                              ;
8E1A: 4B                              ;
8E1B: 00              BRK                         ; 
8E1C: FE DB 8C        INC     $8CDB,X             ; {}
8E1F: B8              CLV                         ; 
8E20: 00              BRK                         ; 
8E21: 68              PLA                         ; 
8E22: DD 52 2C        CMP     $2C52,X             ; 
8E25: 36 33           ROL     $33,X               ; {ram.0033}
8E27: 01 6A           ORA     ($6A,X)             ; {ram.SND_Sq1Fine}
8E29: DB                              ;
8E2A: DB                              ;
8E2B: 03                              ;
8E2C: 53                              ;
8E2D: 00              BRK                         ; 
8E2E: 32                              ;
8E2F: 31 86           AND     ($86),Y             ; {ram.0086}
8E31: FC                              ;
8E32: 3C                              ;
8E33: FD DB AA        SBC     $AADB,X             ; {}
8E36: 3C                              ;
8E37: D5 32           CMP     $32,X               ; {ram.0032}
8E39: 70 00           BVS     $8E3B               ; {}
8E3B: 0B                              ;
8E3C: AD B0 35        LDA     $35B0               ; 
8E3F: 0B                              ;
8E40: F7                              ;
8E41: 53                              ;
8E42: 12                              ;
8E43: F6 F1           INC     $F1,X               ; 
8E45: 45 69           EOR     <$69                ; {ram.0069}
8E47: 05 EE           ORA     <$EE                ; {ram.00EE}
8E49: DB                              ;
8E4A: B0 4B           BCS     $8E97               ; {}
8E4C: 8C 4B 0F        STY     $0F4B               ; 
8E4F: 00              BRK                         ; 
8E50: FD 09 FC        SBC     $FC09,X             ; 
8E53: 72                              ;
8E54: FC                              ;
8E55: A8              TAY                         ; 
8E56: 69 6A           ADC     #$6A                ; 
8E58: 68              PLA                         ; 
8E59: 13                              ;
8E5A: 0B                              ;
8E5B: EE FE 3D        INC     $3DFE               ; 
8E5E: B0 38           BCS     $8E98               ; {}
8E60: 72                              ;
8E61: F6 AD           INC     $AD,X               ; {ram.00AD}
8E63: FD 7B 86        SBC     $867B,X             ; {}
8E66: 31 06           AND     ($06),Y             ; {ram.0006}
8E68: 9B                              ;
8E69: 70 6A           BVS     $8ED5               ; {}
8E6B: 13                              ;
8E6C: B8              CLV                         ; 
8E6D: 38              SEC                         ; 
8E6E: 6C 2D DD        JMP     ($DD2D)             ; 
8E71: FD 00 6A        SBC     $6A00,X             ; 
8E74: 00              BRK                         ; 
8E75: C0 E7           CPY     #$E7                ; 
8E77: 00              BRK                         ; 
8E78: 46 00           LSR     <$00                ; {ram.GP_00}
8E7A: 69 70           ADC     #$70                ; 
8E7C: EF                              ;
8E7D: 00              BRK                         ; 
8E7E: 6D 6A 29        ADC     $296A               ; 
8E81: 5C                              ;
8E82: 06 3E           ASL     <$3E                ; {ram.003E}
8E84: 1C                              ;
8E85: 85 46           STA     <$46                ; {ram.0046}
8E87: 04                              ;
8E88: 29 3E           AND     #$3E                ; 
8E8A: A3                              ;
8E8B: 3F                              ;
8E8C: A6 A6           LDX     <$A6                ; {ram.00A6}
8E8E: 5F                              ;
8E8F: 3E 85 1B        ROL     $1B85,X             ; 
8E92: 1B                              ;
8E93: A4 8B           LDY     <$8B                ; {ram.008B}
8E95: 03                              ;
8E96: 29 24           AND     #$24                ; 
8E98: 9B                              ;
8E99: 00              BRK                         ; 
8E9A: 02                              ;
8E9B: 29 95           AND     #$95                ; 
8E9D: 13                              ;
8E9E: 23                              ;
8E9F: CC 29 3E        CPY     $3E29               ; 
8EA2: 1C                              ;
8EA3: 19 47 26        ORA     $2647,Y             ; 
8EA6: 24 9D           BIT     <$9D                ; {ram.009D}
8EA8: 3E 23 0E        ROL     $0E23,X             ; 
8EAB: 85 17           STA     <$17                ; {ram.0017}
8EAD: 60              RTS                         ; 
8EAE: 24 24           BIT     <$24                ; {ram.0024}
8EB0: 1B                              ;
8EB1: 98              TYA                         ; 
8EB2: 25 93           AND     <$93                ; {ram.0093}
8EB4: 0E 23 4A        ASL     $4A23               ; 
8EB7: 1E 25 07        ASL     $0725,X             ; 
8EBA: 1C                              ;
8EBB: 1B                              ;
8EBC: 95 83           STA     $83,X               ; {ram.0083}
8EBE: 26 23           ROL     <$23                ; {ram.0023}
8EC0: 8D 26 A6        STA     $A626               ; {}
8EC3: 94 98           STY     $98,X               ; {ram.0098}
8EC5: 24 3F           BIT     <$3F                ; {ram.003F}
8EC7: 15 98           ORA     $98,X               ; {ram.0098}
8EC9: 23                              ;
8ECA: 8D 0A 06        STA     $060A               ; {ram.SND_SongPC_A}
8ECD: 0A              ASL     A                   ; 
8ECE: A6 29           LDX     <$29                ; {ram.0029}
8ED0: 95 C1           STA     $C1,X               ; {ram.00C1}
8ED2: A3                              ;
8ED3: 95 A4           STA     $A4,X               ; {ram.00A4}
8ED5: 11 3E           ORA     ($3E),Y             ; {ram.003E}
8ED7: 1F                              ;
8ED8: 3E 4A 1E        ROL     $1E4A,X             ; 
8EDB: A3                              ;
8EDC: 9F                              ;
8EDD: 04                              ;
8EDE: CD 24 97        CMP     $9724               ; {}
8EE1: 9D A3 96        STA     $96A3,X             ; {}
8EE4: 8C 0D 25        STY     $250D               ; 
8EE7: 23                              ;
8EE8: 5A                              ;
8EE9: 10 3F           BPL     $8F2A               ; {}
8EEB: 11 9D           ORA     ($9D),Y             ; {ram.009D}
8EED: 23                              ;
8EEE: 1F                              ;
8EEF: 1B                              ;
8EF0: 00              BRK                         ; 
8EF1: 9B                              ;
8EF2: 21 3E           AND     ($3E,X)             ; {ram.003E}
8EF4: 21 21           AND     ($21,X)             ; {ram.0021}
8EF6: 48              PHA                         ; 
8EF7: 21 02           AND     ($02,X)             ; {ram.GP_02}
8EF9: 21 3F           AND     ($3F,X)             ; {ram.003F}
8EFB: 1B                              ;
8EFC: 91 21           STA     ($21),Y             ; {ram.0021}
8EFE: 00              BRK                         ; 
8EFF: 3F                              ;
8F00: 1B                              ;
8F01: 03                              ;
8F02: 19 03 03        ORA     $0303,Y             ; {ram.0303}
8F05: 0F                              ;
8F06: 03                              ;
8F07: 1A                              ;
8F08: 1B                              ;
8F09: 03                              ;
8F0A: 17                              ;
8F0B: 05 03           ORA     <$03                ; {ram.GP_03}
8F0D: 03                              ;
8F0E: 03                              ;
8F0F: 03                              ;
8F10: 1A                              ;
8F11: 23                              ;
8F12: 03                              ;
8F13: 00              BRK                         ; 
8F14: 19 1E 1B        ORA     $1B1E,Y             ; 
8F17: 23                              ;
8F18: 19 19 03        ORA     $0319,Y             ; 
8F1B: 1B                              ;
8F1C: 83                              ;
8F1D: 99 17 03        STA     $0317,Y             ; {ram.0317}
8F20: 1B                              ;
8F21: 03                              ;
8F22: 03                              ;
8F23: 03                              ;
8F24: 03                              ;
8F25: 03                              ;
8F26: 1A                              ;
8F27: 03                              ;
8F28: 03                              ;
8F29: 03                              ;
8F2A: 39 1A 80        AND     $801A,Y             ; {}
8F2D: 03                              ;
8F2E: 03                              ;
8F2F: 03                              ;
8F30: 19 19 0F        ORA     $0F19,Y             ; 
8F33: 03                              ;
8F34: 16 19           ASL     $19,X               ; {ram.0019}
8F36: 43                              ;
8F37: 0F                              ;
8F38: 03                              ;
8F39: 03                              ;
8F3A: 03                              ;
8F3B: 20 03 19        JSR     $1903               ; 
8F3E: 03                              ;
8F3F: 03                              ;
8F40: 03                              ;
8F41: 16 03           ASL     $03,X               ; {ram.GP_03}
8F43: 17                              ;
8F44: 03                              ;
8F45: 17                              ;
8F46: 0D 00 17        ORA     $1700               ; 
8F49: 19 19 00        ORA     $0019,Y             ; {ram.0019}
8F4C: 19 00 03        ORA     $0300,Y             ; {ram.0300}
8F4F: 1B                              ;
8F50: 83                              ;
8F51: 0F                              ;
8F52: 0F                              ;
8F53: 03                              ;
8F54: 03                              ;
8F55: 00              BRK                         ; 
8F56: 03                              ;
8F57: 16 03           ASL     $03,X               ; {ram.GP_03}
8F59: 03                              ;
8F5A: 16 19           ASL     $19,X               ; {ram.0019}
8F5C: 83                              ;
8F5D: 03                              ;
8F5E: 63                              ;
8F5F: 1A                              ;
8F60: 97                              ;
8F61: 0F                              ;
8F62: 83                              ;
8F63: 99 80 03        STA     $0380,Y             ; 
8F66: 1A                              ;
8F67: 19 03 19        ORA     $1903,Y             ; 
8F6A: 0C                              ;
8F6B: 19 16 03        ORA     $0316,Y             ; {ram.0316}
8F6E: 03                              ;
8F6F: 63                              ;
8F70: 99 03 03        STA     $0303,Y             ; {ram.0303}
8F73: 03                              ;
8F74: 03                              ;
8F75: 03                              ;
8F76: 16 03           ASL     $03,X               ; {ram.GP_03}
8F78: 1D 03 0A        ORA     $0A03,X             ; 
8F7B: 0F                              ;
8F7C: 99 03 03        STA     $0303,Y             ; {ram.0303}
8F7F: 11 20           ORA     ($20),Y             ; {ram.0020}
8F81: 04                              ;
8F82: 17                              ;
8F83: 00              BRK                         ; 
8F84: 00              BRK                         ; 
8F85: 07                              ;
8F86: 05 07           ORA     <$07                ; {ram.0007}
8F88: 20 00 27        JSR     $2700               ; 
8F8B: 20 00 06        JSR     $0600               ; {ram.SND_ReqMusic}
8F8E: 05 00           ORA     <$00                ; {ram.GP_00}
8F90: 07                              ;
8F91: 02                              ;
8F92: 00              BRK                         ; 
8F93: 27                              ;
8F94: 31 37           AND     ($37),Y             ; 
8F96: 20 00 27        JSR     $2700               ; 
8F99: 27                              ;
8F9A: 02                              ;
8F9B: 20 00 07        JSR     $0700               ; {ram.0700}
8F9E: 27                              ;
8F9F: 05 20           ORA     <$20                ; {ram.0020}
8FA1: 00              BRK                         ; 
8FA2: 02                              ;
8FA3: 00              BRK                         ; 
8FA4: 05 00           ORA     <$00                ; {ram.GP_00}
8FA6: 37                              ;
8FA7: 01 00           ORA     ($00,X)             ; {ram.GP_00}
8FA9: 01 30           ORA     ($30,X)             ; {ram.0030}
8FAB: 07                              ;
8FAC: 27                              ;
8FAD: 00              BRK                         ; 
8FAE: 01 01           ORA     ($01,X)             ; {ram.GP_01}
8FB0: 01 30           ORA     ($30,X)             ; {ram.0030}
8FB2: 07                              ;
8FB3: 00              BRK                         ; 
8FB4: 00              BRK                         ; 
8FB5: 27                              ;
8FB6: 05 07           ORA     <$07                ; {ram.0007}
8FB8: 01 01           ORA     ($01,X)             ; {ram.GP_01}
8FBA: 00              BRK                         ; 
8FBB: 27                              ;
8FBC: 00              BRK                         ; 
8FBD: 27                              ;
8FBE: 06 01           ASL     <$01                ; {ram.GP_01}
8FC0: 01 27           ORA     ($27,X)             ; {ram.0027}
8FC2: 00              BRK                         ; 
8FC3: 17                              ;
8FC4: 00              BRK                         ; 
8FC5: 21 20           AND     ($20,X)             ; {ram.0020}
8FC7: 17                              ;
8FC8: 31 20           AND     ($20),Y             ; {ram.0020}
8FCA: 17                              ;
8FCB: 27                              ;
8FCC: 27                              ;
8FCD: 27                              ;
8FCE: 00              BRK                         ; 
8FCF: 20 01 35        JSR     $3501               ; 
8FD2: 27                              ;
8FD3: 00              BRK                         ; 
8FD4: 00              BRK                         ; 
8FD5: 27                              ;
8FD6: 00              BRK                         ; 
8FD7: 17                              ;
8FD8: 00              BRK                         ; 
8FD9: 04                              ;
8FDA: 17                              ;
8FDB: 27                              ;
8FDC: 01 01           ORA     ($01,X)             ; {ram.GP_01}
8FDE: 05 07           ORA     <$07                ; {ram.0007}
8FE0: 27                              ;
8FE1: 07                              ;
8FE2: 00              BRK                         ; 
8FE3: 10 27           BPL     $900C               ; {}
8FE5: 00              BRK                         ; 
8FE6: 17                              ;
8FE7: 27                              ;
8FE8: 00              BRK                         ; 
8FE9: 17                              ;
8FEA: 20 17 27        JSR     $2717               ; 
8FED: 01 00           ORA     ($00,X)             ; {ram.GP_00}
8FEF: 00              BRK                         ; 
8FF0: 27                              ;
8FF1: 00              BRK                         ; 
8FF2: 00              BRK                         ; 
8FF3: 00              BRK                         ; 
8FF4: 00              BRK                         ; 
8FF5: 00              BRK                         ; 
8FF6: 25 00           AND     <$00                ; {ram.GP_00}
8FF8: 27                              ;
8FF9: 00              BRK                         ; 
8FFA: 20 27 27        JSR     $2727               ; 
8FFD: 00              BRK                         ; 
8FFE: 00              BRK                         ; 
8FFF: 20 26 22        JSR     $2226               ; 
9002: 18              CLC                         ; 
9003: 29 19           AND     #$19                ; 
9005: 49 26           EOR     #$26                ; 
9007: 3E 22 26        ROL     $2622,X             ; 
900A: 26 26           ROL     <$26                ; {ram.0026}
900C: 26 26           ROL     <$26                ; {ram.0026}
900E: 26 22           ROL     <$22                ; {ram.0022}
9010: 26 06           ROL     <$06                ; {ram.0006}
9012: 26 3E           ROL     <$3E                ; {ram.003E}
9014: 22                              ;
9015: 22                              ;
9016: 46 E6           LSR     <$E6                ; {ram.00E6}
9018: EA              NOP                         ; 
9019: 26 22           ROL     <$22                ; {ram.0022}
901B: 26 26           ROL     <$26                ; {ram.0026}
901D: 26 26           ROL     <$26                ; {ram.0026}
901F: 02                              ;
9020: 08              PHP                         ; 
9021: 6A              ROR     A                   ; 
9022: 32                              ;
9023: 02                              ;
9024: 02                              ;
9025: 02                              ;
9026: 69 78           ADC     #$78                ; 
9028: 56 32           LSR     $32,X               ; {ram.0032}
902A: 06 38           ASL     <$38                ; {ram.0038}
902C: 48              PHA                         ; 
902D: 22                              ;
902E: 22                              ;
902F: 02                              ;
9030: 5B                              ;
9031: 3E 92 F6        ROL     $F692,X             ; 
9034: 12                              ;
9035: 06 3E           ASL     <$3E                ; {ram.003E}
9037: 5C                              ;
9038: A6 86           LDX     <$86                ; {ram.0086}
903A: 3E 3E 3E        ROL     $3E3E,X             ; 
903D: F6 E2           INC     $E2,X               ; {ram.00E2}
903F: 02                              ;
9040: 22                              ;
9041: 16 8A           ASL     $8A,X               ; {ram.008A}
9043: A2 82           LDX     #$82                ; 
9045: 52                              ;
9046: 12                              ;
9047: 2A              ROL     A                   ; 
9048: 26 22           ROL     <$22                ; {ram.0022}
904A: 16 1E           ASL     $1E,X               ; {ram.001E}
904C: 1E B2 1E        ASL     $1EB2,X             ; 
904F: 02                              ;
9050: 06 B6           ASL     <$B6                ; {ram.00B6}
9052: 22                              ;
9053: 02                              ;
9054: 02                              ;
9055: 82                              ;
9056: 82                              ;
9057: 46 2A           LSR     <$2A                ; {ram.002A}
9059: EA              NOP                         ; 
905A: A6 06           LDX     <$06                ; {ram.0006}
905C: 06 82           ASL     <$82                ; {ram.0082}
905E: E2                              ;
905F: 02                              ;
9060: 4A              LSR     A                   ; 
9061: A6 06           LDX     <$06                ; {ram.0006}
9063: 12                              ;
9064: E2                              ;
9065: 06 26           ASL     <$26                ; {ram.0026}
9067: 1A                              ;
9068: 46 46           LSR     <$46                ; {ram.0046}
906A: 26 26           ROL     <$26                ; {ram.0026}
906C: 26 06           ROL     <$06                ; {ram.0006}
906E: 02                              ;
906F: 02                              ;
9070: 2A              ROL     A                   ; 
9071: 73                              ;
9072: 01 86           ORA     ($86,X)             ; {ram.0086}
9074: 02                              ;
9075: 06 45           ASL     <$45                ; {ram.0045}
9077: 00              BRK                         ; 
9078: 26 22           ROL     <$22                ; {ram.0022}
907A: 26 26           ROL     <$26                ; {ram.0026}
907C: 26 26           ROL     <$26                ; {ram.0026}
907E: 06 02           ASL     <$02                ; {ram.GP_02}
9080: 2A              ROL     A                   ; 
9081: 46 6F           LSR     <$6F                ; {ram.SND_MusEffCnt}
9083: 5F                              ;
9084: 4F                              ;
9085: 0A              ASL     A                   ; 
9086: 26 26           ROL     <$26                ; {ram.0026}
9088: 32                              ;
9089: 87                              ;
908A: 22                              ;
908B: F7                              ;
908C: B3                              ;
908D: 9F                              ;
908E: FE E7 3F        INC     $3FE7,X             ; 
9091: E3                              ;
9092: 0B                              ;
9093: 48              PHA                         ; 
9094: 22                              ;
9095: 12                              ;
9096: 9F                              ;
9097: E7                              ;
9098: 22                              ;
9099: E6 26           INC     <$26                ; {ram.0026}
909B: 22                              ;
909C: FE F7 A6        INC     $A6F7,X             ; {}
909F: 27                              ;
90A0: 58              CLI                         ; 
90A1: 4D 37 A3        EOR     $A337               ; {}
90A4: E3                              ;
90A5: 06 3F           ASL     <$3F                ; {ram.003F}
90A7: 3A                              ;
90A8: 23                              ;
90A9: E6 26           INC     <$26                ; {ram.0026}
90AB: 38              SEC                         ; 
90AC: 48              PHA                         ; 
90AD: 26 26           ROL     <$26                ; {ram.0026}
90AF: 24 2E           BIT     <$2E                ; {ram.002E}
90B1: 22                              ;
90B2: 03                              ;
90B3: E2                              ;
90B4: 02                              ;
90B5: 26 06           ROL     <$06                ; {ram.0006}
90B7: 1E 26 27        ASL     $2726,X             ; 
90BA: 3E 04 27        ROL     $2704,X             ; 
90BD: 27                              ;
90BE: 27                              ;
90BF: 26 32           ROL     <$32                ; {ram.0032}
90C1: 9E                              ;
90C2: 02                              ;
90C3: 3F                              ;
90C4: E7                              ;
90C5: 2A              ROL     A                   ; 
90C6: 53                              ;
90C7: 87                              ;
90C8: 36 A6           ROL     $A6,X               ; {ram.00A6}
90CA: 3E 02 E4        ROL     $E402,X             ; 
90CD: 26 27           ROL     <$27                ; {ram.0027}
90CF: 27                              ;
90D0: 37                              ;
90D1: A7                              ;
90D2: 26 27           ROL     <$27                ; {ram.0027}
90D4: 2B                              ;
90D5: 4B                              ;
90D6: 5E 06 3E        LSR     $3E06,X             ; 
90D9: 06 27           ASL     <$27                ; {ram.0027}
90DB: 26 26           ROL     <$26                ; {ram.0026}
90DD: 26 27           ROL     <$27                ; {ram.0027}
90DF: 26 7D           ROL     <$7D                ; {ram.007D}
90E1: 23                              ;
90E2: 1F                              ;
90E3: E3                              ;
90E4: FC                              ;
90E5: 03                              ;
90E6: 07                              ;
90E7: 7C                              ;
90E8: 23                              ;
90E9: 16 A6           ASL     $A6,X               ; {ram.00A6}
90EB: 20 E2 E6        JSR     $E6E2               ; 
90EE: 27                              ;
90EF: 26 2A           ROL     <$2A                ; {ram.002A}
90F1: 35 15           AND     $15,X               ; {ram.0015}
90F3: 22                              ;
90F4: 27                              ;
90F5: 57                              ;
90F6: 45 00           EOR     <$00                ; {ram.GP_00}
90F8: 22                              ;
90F9: 03                              ;
90FA: 03                              ;
90FB: E3                              ;
90FC: 02                              ;
90FD: FE 07 27        INC     $2707,X             ; 
9100: 3B                              ;
9101: 07                              ;
9102: 69 69           ADC     #$69                ; 
9104: 69 69           ADC     #$69                ; 
9106: EC 37 01        CPX     $0137               ; {ram.0137}
9109: 31 AD           AND     ($AD),Y             ; {ram.00AD}
910B: 31 FF           AND     ($FF),Y             ; {ram.CUR_2000}
910D: 38              SEC                         ; 
910E: 85 45           STA     <$45                ; {ram.0045}
9110: 72                              ;
9111: F1 F6           SBC     ($F6),Y             ; {ram.TileFlagB}
9113: 0D ED 7B        ORA     $7BED               ; {ram.7BED}
9116: 08              PHP                         ; 
9117: 3E 86 6C        ROL     $6C86,X             ; 
911A: DB                              ;
911B: 00              BRK                         ; 
911C: 05 4C           ORA     <$4C                ; {ram.004C}
911E: FE EE 69        INC     $69EE,X             ; 
9121: 39 A3 FC        AND     $FCA3,Y             ; 
9124: 00              BRK                         ; 
9125: 00              BRK                         ; 
9126: C5 39           CMP     <$39                ; {ram.0039}
9128: 31 F5           AND     ($F5),Y             ; {ram.TileFlagA}
912A: B8              CLV                         ; 
912B: 39 69 00        AND     $0069,Y             ; {ram.0069}
912E: EE 36 6A        INC     $6A36               ; {ram.6A36}
9131: F7                              ;
9132: FD 00 00        SBC     $0000,X             ; {ram.GP_00}
9135: 2D 72 69        AND     $6972               ; {ram.6972}
9138: FF                              ;
9139: 45 2D           EOR     <$2D                ; {ram.002D}
913B: 11 3C           ORA     ($3C),Y             ; {ram.003C}
913D: 31 33           AND     ($33),Y             ; {ram.0033}
913F: 38              SEC                         ; 
9140: AD 00 53        LDA     $5300               ; 
9143: A4 08           LDY     <$08                ; {ram.0008}
9145: 7B                              ;
9146: 07                              ;
9147: B3                              ;
9148: AA              TAX                         ; 
9149: FF                              ;
914A: F0 00           BEQ     $914C               ; {}
914C: 11 01           ORA     ($01),Y             ; {ram.GP_01}
914E: 8C 85 3A        STY     $3A85               ; 
9151: DD F1 F7        CMP     $F7F1,X             ; 
9154: AD DD 7B        LDA     $7BDD               ; {ram.7BDD}
9157: FD E8 00        SBC     $00E8,X             ; {ram.00E8}
915A: 8C CC 8C        STY     $8CCC               ; {}
915D: BA              TSX                         ; 
915E: 4C E8 69        JMP     $69E8               ; {ram.69E8}
9161: 52                              ;
9162: F6 3B           INC     $3B,X               ; {ram.003B}
9164: 0B                              ;
9165: 7B                              ;
9166: FC                              ;
9167: 69 F5           ADC     #$F5                ; 
9169: DB                              ;
916A: 85 0F           STA     <$0F                ; {ram.000F}
916C: FF                              ;
916D: 3D FE AD        AND     $ADFE,X             ; {}
9170: 39 38 C5        AND     $C538,Y             ; 
9173: FD 00 B5        SBC     $B500,X             ; {}
9176: CA              DEX                         ; 
9177: 46 AD           LSR     <$AD                ; {ram.00AD}
9179: 00              BRK                         ; 
917A: B8              CLV                         ; 
917B: FE F4 3C        INC     $3CF4,X             ; 
917E: FE 00 4A        INC     $4A00,X             ; 
9181: CA              DEX                         ; 
9182: 3E 3E 3E        ROL     $3E3E,X             ; 
9185: 3E 62 27        ROL     $2762,X             ; 
9188: DA                              ;
9189: 24 5F           BIT     <$5F                ; {ram.005F}
918B: 24 95           BIT     <$95                ; {ram.0095}
918D: 24 0C           BIT     <$0C                ; {ram.000C}
918F: 23                              ;
9190: 95 A3           STA     $A3,X               ; {ram.00A3}
9192: 99 A6 00        STA     $00A6,Y             ; {ram.00A6}
9195: CE A3 28        DEC     $28A3               ; 
9198: 62                              ;
9199: 4A              LSR     A                   ; 
919A: 5A                              ;
919B: 29 85           AND     #$85                ; 
919D: 24 9B           BIT     <$9B                ; {ram.009B}
919F: 96 3E           STX     $3E,Y               ; {ram.003E}
91A1: 3E 23 96        ROL     $9623,X             ; {}
91A4: 60              RTS                         ; 
91A5: 60              RTS                         ; 
91A6: 3E 3E 23        ROL     $233E,X             ; 
91A9: CD DF 3F        CMP     $3FDF               ; 
91AC: 3F                              ;
91AD: 29 C1           AND     #$C1                ; 
91AF: 26 3E           ROL     <$3E                ; {ram.003E}
91B1: 81 A3           STA     ($A3,X)             ; {ram.00A3}
91B3: 60              RTS                         ; 
91B4: 60              RTS                         ; 
91B5: 4A              LSR     A                   ; 
91B6: 88              DEY                         ; 
91B7: 3E C8 23        ROL     $23C8,X             ; 
91BA: 62                              ;
91BB: A6 24           LDX     <$24                ; {ram.0024}
91BD: 24 23           BIT     <$23                ; {ram.0023}
91BF: 46 23           LSR     <$23                ; {ram.0023}
91C1: 60              RTS                         ; 
91C2: 26 12           ROL     <$12                ; {ram.0012}
91C4: A3                              ;
91C5: E2                              ;
91C6: A4 A3           LDY     <$A3                ; {ram.00A3}
91C8: 51 C8           EOR     ($C8),Y             ; {ram.00C8}
91CA: 4A              LSR     A                   ; 
91CB: 60              RTS                         ; 
91CC: A6 C7           LDX     <$C7                ; {ram.00C7}
91CE: 23                              ;
91CF: 18              CLC                         ; 
91D0: 24 0D           BIT     <$0D                ; {ram.000D}
91D2: 83                              ;
91D3: 94 96           STY     $96,X               ; {ram.0096}
91D5: 0F                              ;
91D6: 8C DF 62        STY     $62DF               ; {ram.62DF}
91D9: 60              RTS                         ; 
91DA: 23                              ;
91DB: 5F                              ;
91DC: 51 9E           EOR     ($9E),Y             ; {ram.009E}
91DE: 24 51           BIT     <$51                ; {ram.0051}
91E0: 3E 23 A3        ROL     $A323,X             ; {}
91E3: 1D A6 95        ORA     $95A6,X             ; {}
91E6: A3                              ;
91E7: 3E 96 0F        ROL     $0F96,X             ; 
91EA: 5A                              ;
91EB: A6 C8           LDX     <$C8                ; {ram.00C8}
91ED: 04                              ;
91EE: 98              TYA                         ; 
91EF: 4A              LSR     A                   ; 
91F0: 3F                              ;
91F1: 3E 3E 9D        ROL     $9D3E,X             ; {}
91F4: 21 3E           AND     ($3E,X)             ; {ram.003E}
91F6: 3F                              ;
91F7: 3F                              ;
91F8: DF                              ;
91F9: 21 A3           AND     ($A3,X)             ; {ram.00A3}
91FB: 93                              ;
91FC: D1 46           CMP     ($46),Y             ; {ram.0046}
91FE: 95 21           STA     $21,X               ; {ram.0021}
9200: 03                              ;
9201: 03                              ;
9202: 03                              ;
9203: 03                              ;
9204: 03                              ;
9205: 03                              ;
9206: 03                              ;
9207: 03                              ;
9208: 03                              ;
9209: 19 19 03        ORA     $0319,Y             ; 
920C: 80                              ;
920D: 0F                              ;
920E: 03                              ;
920F: 19 0F 03        ORA     $030F,Y             ; 
9212: 03                              ;
9213: 03                              ;
9214: 03                              ;
9215: 03                              ;
9216: 23                              ;
9217: 8E 03 03        STX     $0303               ; {ram.0303}
921A: 03                              ;
921B: 1B                              ;
921C: 1A                              ;
921D: 20 03 96        JSR     $9603               ; {}
9220: 03                              ;
9221: 03                              ;
9222: 03                              ;
9223: 03                              ;
9224: 83                              ;
9225: 03                              ;
9226: 03                              ;
9227: 03                              ;
9228: 03                              ;
9229: 03                              ;
922A: 19 10 0B        ORA     $0B10,Y             ; 
922D: 1B                              ;
922E: 19 03 03        ORA     $0303,Y             ; {ram.0303}
9231: 03                              ;
9232: 19 03 03        ORA     $0303,Y             ; {ram.0303}
9235: 03                              ;
9236: 03                              ;
9237: 03                              ;
9238: 03                              ;
9239: 17                              ;
923A: 03                              ;
923B: 03                              ;
923C: 0F                              ;
923D: 1A                              ;
923E: 03                              ;
923F: 03                              ;
9240: 03                              ;
9241: 03                              ;
9242: 16 03           ASL     $03,X               ; {ram.GP_03}
9244: 0F                              ;
9245: 03                              ;
9246: 17                              ;
9247: 03                              ;
9248: 03                              ;
9249: 03                              ;
924A: 03                              ;
924B: 03                              ;
924C: 03                              ;
924D: 43                              ;
924E: 03                              ;
924F: 03                              ;
9250: 00              BRK                         ; 
9251: 83                              ;
9252: 03                              ;
9253: 03                              ;
9254: 83                              ;
9255: 8F                              ;
9256: 03                              ;
9257: 03                              ;
9258: 03                              ;
9259: 03                              ;
925A: 00              BRK                         ; 
925B: 03                              ;
925C: 03                              ;
925D: 0F                              ;
925E: 0F                              ;
925F: 03                              ;
9260: 03                              ;
9261: 0F                              ;
9262: 03                              ;
9263: 80                              ;
9264: 03                              ;
9265: 83                              ;
9266: 0F                              ;
9267: 03                              ;
9268: 0F                              ;
9269: 03                              ;
926A: 00              BRK                         ; 
926B: 03                              ;
926C: 03                              ;
926D: 03                              ;
926E: 97                              ;
926F: 03                              ;
9270: 07                              ;
9271: 03                              ;
9272: 03                              ;
9273: 03                              ;
9274: 03                              ;
9275: 03                              ;
9276: 09 13           ORA     #$13                ; 
9278: 16 03           ASL     $03,X               ; {ram.GP_03}
927A: 03                              ;
927B: 83                              ;
927C: 03                              ;
927D: 03                              ;
927E: 83                              ;
927F: 03                              ;
9280: 05 05           ORA     <$05                ; {ram.0005}
9282: 00              BRK                         ; 
9283: 00              BRK                         ; 
9284: 00              BRK                         ; 
9285: 00              BRK                         ; 
9286: 05 20           ORA     <$20                ; {ram.0020}
9288: 00              BRK                         ; 
9289: 27                              ;
928A: 15 01           ORA     $01,X               ; {ram.GP_01}
928C: 17                              ;
928D: 17                              ;
928E: 01 27           ORA     ($27,X)             ; {ram.0027}
9290: 17                              ;
9291: 01 00           ORA     ($00,X)             ; {ram.GP_00}
9293: 00              BRK                         ; 
9294: 00              BRK                         ; 
9295: 05 01           ORA     <$01                ; {ram.GP_01}
9297: 03                              ;
9298: 05 05           ORA     <$05                ; {ram.0005}
929A: 00              BRK                         ; 
929B: 20 17 27        JSR     $2717               ; 
929E: 00              BRK                         ; 
929F: 37                              ;
92A0: 00              BRK                         ; 
92A1: 20 00 10        JSR     $1000               ; 
92A4: 00              BRK                         ; 
92A5: 00              BRK                         ; 
92A6: 00              BRK                         ; 
92A7: 00              BRK                         ; 
92A8: 00              BRK                         ; 
92A9: 05 05           ORA     <$05                ; {ram.0005}
92AB: 20 20 20        JSR     $2020               ; 
92AE: 25 00           AND     <$00                ; {ram.GP_00}
92B0: 00              BRK                         ; 
92B1: 01 27           ORA     ($27,X)             ; {ram.0027}
92B3: 00              BRK                         ; 
92B4: 00              BRK                         ; 
92B5: 05 00           ORA     <$00                ; {ram.GP_00}
92B7: 00              BRK                         ; 
92B8: 05 27           ORA     <$27                ; {ram.0027}
92BA: 05 06           ORA     <$06                ; {ram.0006}
92BC: 07                              ;
92BD: 07                              ;
92BE: 01 05           ORA     ($05,X)             ; {ram.0005}
92C0: 00              BRK                         ; 
92C1: 00              BRK                         ; 
92C2: 17                              ;
92C3: 01 27           ORA     ($27,X)             ; {ram.0027}
92C5: 05 27           ORA     <$27                ; {ram.0027}
92C7: 00              BRK                         ; 
92C8: 05 05           ORA     <$05                ; {ram.0005}
92CA: 05 00           ORA     <$00                ; {ram.GP_00}
92CC: 06 05           ASL     <$05                ; {ram.0005}
92CE: 01 00           ORA     ($00,X)             ; {ram.GP_00}
92D0: 17                              ;
92D1: 00              BRK                         ; 
92D2: 00              BRK                         ; 
92D3: 00              BRK                         ; 
92D4: 00              BRK                         ; 
92D5: 37                              ;
92D6: 00              BRK                         ; 
92D7: 05 05           ORA     <$05                ; {ram.0005}
92D9: 00              BRK                         ; 
92DA: 27                              ;
92DB: 05 05           ORA     <$05                ; {ram.0005}
92DD: 17                              ;
92DE: 27                              ;
92DF: 05 00           ORA     <$00                ; {ram.GP_00}
92E1: 17                              ;
92E2: 01 27           ORA     ($27,X)             ; {ram.0027}
92E4: 00              BRK                         ; 
92E5: 00              BRK                         ; 
92E6: 27                              ;
92E7: 00              BRK                         ; 
92E8: 37                              ;
92E9: 00              BRK                         ; 
92EA: 17                              ;
92EB: 00              BRK                         ; 
92EC: 04                              ;
92ED: 01 37           ORA     ($37,X)             ; 
92EF: 05 20           ORA     <$20                ; {ram.0020}
92F1: 00              BRK                         ; 
92F2: 00              BRK                         ; 
92F3: 00              BRK                         ; 
92F4: 00              BRK                         ; 
92F5: 00              BRK                         ; 
92F6: 20 20 15        JSR     $1520               ; 
92F9: 00              BRK                         ; 
92FA: 00              BRK                         ; 
92FB: 01 05           ORA     ($05,X)             ; {ram.0005}
92FD: 04                              ;
92FE: 00              BRK                         ; 
92FF: 00              BRK                         ; 
9300: 3F                              ;
9301: 00              BRK                         ; 
9302: 20 0F 30        JSR     $300F               ; 
9305: 00              BRK                         ; 
9306: 12                              ;
9307: 0F                              ;
9308: 16 27           ASL     $27,X               ; {ram.0027}
930A: 36 0F           ROL     $0F,X               ; {ram.000F}
930C: 1A                              ;
930D: 37                              ;
930E: 12                              ;
930F: 0F                              ;
9310: 17                              ;
9311: 37                              ;
9312: 12                              ;
9313: 0F                              ;
9314: 29 27           AND     #$27                ; 
9316: 17                              ;
9317: 0F                              ;
9318: 02                              ;
9319: 22                              ;
931A: 30 0F           BMI     $932B               ; {}
931C: 16 27           ASL     $27,X               ; {ram.0027}
931E: 30 0F           BMI     $932F               ; {}
9320: 0C                              ;
9321: 1C                              ;
9322: 2C FF 01        BIT     $01FF               ; {ram.01FF}
9325: 04                              ;
9326: 05 06           ORA     <$06                ; {ram.0006}
9328: 8D 57 49        STA     $4957               ; 
932B: 99 69 00        STA     $0069,Y             ; {ram.0069}
932E: 00              BRK                         ; 
932F: 77                              ;
9330: 2A              ROL     A                   ; 
9331: 7F                              ;
9332: 06 00           ASL     <$00                ; {ram.GP_00}
9334: 1D 23 49        ORA     $4923,X             ; 
9337: 79 FF FF        ADC     $FFFF,Y             ; 
933A: FF                              ;
933B: FF                              ;
933C: FF                              ;
933D: FF                              ;
933E: 2A              ROL     A                   ; 
933F: FF                              ;
9340: FF                              ;
9341: FF                              ;
9342: FF                              ;
9343: FF                              ;
9344: FF                              ;
9345: FF                              ;
9346: FF                              ;
9347: FF                              ;
9348: FF                              ;
9349: FF                              ;
934A: FF                              ;
934B: FF                              ;
934C: FF                              ;
934D: FF                              ;
934E: FF                              ;
934F: 20 62 48        JSR     $4862               ; 
9352: F5 20           SBC     $20,X               ; {ram.0020}
9354: 82                              ;
9355: 48              PHA                         ; 
9356: F5 20           SBC     $20,X               ; {ram.0020}
9358: A2 48           LDX     #$48                ; 
935A: F5 20           SBC     $20,X               ; {ram.0020}
935C: C2                              ;
935D: 48              PHA                         ; 
935E: F5 FF           SBC     $FF,X               ; {ram.CUR_2000}
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
93DC: 0F                              ;
93DD: 06 17           ASL     <$17                ; {ram.0017}
93DF: 16 0F           ASL     $0F,X               ; {ram.000F}
93E1: 06 17           ASL     <$17                ; {ram.0017}
93E3: 16 0F           ASL     $0F,X               ; {ram.000F}
93E5: 07                              ;
93E6: 06 16           ASL     <$16                ; {ram.0016}
93E8: 0F                              ;
93E9: 07                              ;
93EA: 06 16           ASL     <$16                ; {ram.0016}
93EC: 0F                              ;
93ED: 0F                              ;
93EE: 07                              ;
93EF: 06 0F           ASL     <$0F                ; {ram.000F}
93F1: 0F                              ;
93F2: 07                              ;
93F3: 06 0F           ASL     <$0F                ; {ram.000F}
93F5: 0F                              ;
93F6: 0F                              ;
93F7: 0F                              ;
93F8: 0F                              ;
93F9: 0F                              ;
93FA: 0F                              ;
93FB: 0F                              ;
93FC: 3F                              ;
93FD: 00              BRK                         ; 
93FE: 20 0F 30        JSR     $300F               ; 
9401: 00              BRK                         ; 
9402: 12                              ;
9403: 0F                              ;
9404: 16 27           ASL     $27,X               ; {ram.0027}
9406: 36 0F           ROL     $0F,X               ; {ram.000F}
9408: 0C                              ;
9409: 1C                              ;
940A: 2C 0F 12        BIT     $120F               ; 
940D: 1C                              ;
940E: 2C 0F 29        BIT     $290F               ; 
9411: 27                              ;
9412: 17                              ;
9413: 0F                              ;
9414: 02                              ;
9415: 22                              ;
9416: 30 0F           BMI     $9427               ; {}
9418: 16 27           ASL     $27,X               ; {ram.0027}
941A: 30 0F           BMI     $942B               ; {}
941C: 0C                              ;
941D: 1C                              ;
941E: 2C FF 03        BIT     $03FF               ; {ram.03FF}
9421: 05 06           ORA     <$06                ; {ram.0006}
9423: 08              PHP                         ; 
9424: DD C9 AC        CMP     $ACC9,X             ; {}
9427: 89                              ;
9428: 87                              ;
9429: 04                              ;
942A: 00              BRK                         ; 
942B: 73                              ;
942C: 36 FF           ROL     $FF,X               ; {ram.CUR_2000}
942E: 06 01           ASL     <$01                ; {ram.GP_01}
9430: 7F                              ;
9431: FF                              ;
9432: FF                              ;
9433: FF                              ;
9434: FF                              ;
9435: FF                              ;
9436: FF                              ;
9437: FF                              ;
9438: FF                              ;
9439: FF                              ;
943A: 35 00           AND     $00,X               ; {ram.GP_00}
943C: 00              BRK                         ; 
943D: 00              BRK                         ; 
943E: 00              BRK                         ; 
943F: 00              BRK                         ; 
9440: 08              PHP                         ; 
9441: 2D 3F 0D        AND     $0D3F               ; 
9444: 18              CLC                         ; 
9445: 10 00           BPL     $9447               ; {}
9447: 00              BRK                         ; 
9448: 00              BRK                         ; 
9449: 00              BRK                         ; 
944A: 00              BRK                         ; 
944B: 20 84 05        JSR     $0584               ; {ram.0584}
944E: 67                              ;
944F: FF                              ;
9450: 24 FB           BIT     <$FB                ; {ram.00FB}
9452: FB                              ;
9453: 20 A3 05        JSR     $05A3               ; {ram.05A3}
9456: 67                              ;
9457: FF                              ;
9458: FF                              ;
9459: FF                              ;
945A: 67                              ;
945B: 20 C4 03        JSR     $03C4               ; {ram.03C4}
945E: FB                              ;
945F: FF                              ;
9460: FB                              ;
9461: FF                              ;
9462: FF                              ;
9463: FF                              ;
9464: FF                              ;
9465: FF                              ;
9466: FF                              ;
9467: FF                              ;
9468: FF                              ;
9469: FF                              ;
946A: FF                              ;
946B: FF                              ;
946C: FF                              ;
946D: FF                              ;
946E: FF                              ;
946F: FF                              ;
9470: FF                              ;
9471: FF                              ;
9472: FF                              ;
9473: FF                              ;
9474: FF                              ;
9475: FF                              ;
9476: FF                              ;
9477: FF                              ;
9478: 0F                              ;
9479: 0C                              ;
947A: 1C                              ;
947B: 2C 0F 12        BIT     $120F               ; 
947E: 1C                              ;
947F: 2C 0F 0C        BIT     $0C0F               ; 
9482: 0C                              ;
9483: 1C                              ;
9484: 0F                              ;
9485: 11 0C           ORA     ($0C),Y             ; {ram.000C}
9487: 1C                              ;
9488: 0F                              ;
9489: 0F                              ;
948A: 0C                              ;
948B: 0C                              ;
948C: 0F                              ;
948D: 02                              ;
948E: 0C                              ;
948F: 0C                              ;
9490: 0F                              ;
9491: 0F                              ;
9492: 0F                              ;
9493: 0F                              ;
9494: 0F                              ;
9495: 0F                              ;
9496: 0F                              ;
9497: 0F                              ;
9498: 0F                              ;
9499: 00              BRK                         ; 
949A: 10 30           BPL     $94CC               ; {}
949C: 0F                              ;
949D: 00              BRK                         ; 
949E: 10 30           BPL     $94D0               ; {}
94A0: 0F                              ;
94A1: 00              BRK                         ; 
94A2: 00              BRK                         ; 
94A3: 10 0F           BPL     $94B4               ; {}
94A5: 00              BRK                         ; 
94A6: 00              BRK                         ; 
94A7: 10 0F           BPL     $94B8               ; {}
94A9: 0F                              ;
94AA: 00              BRK                         ; 
94AB: 00              BRK                         ; 
94AC: 0F                              ;
94AD: 0F                              ;
94AE: 00              BRK                         ; 
94AF: 00              BRK                         ; 
94B0: 0F                              ;
94B1: 0F                              ;
94B2: 0F                              ;
94B3: 0F                              ;
94B4: 0F                              ;
94B5: 0F                              ;
94B6: 0F                              ;
94B7: 0F                              ;
94B8: 0F                              ;
94B9: 0C                              ;
94BA: 1C                              ;
94BB: 2C 0F 12        BIT     $120F               ; 
94BE: 1C                              ;
94BF: 2C 0F 0C        BIT     $0C0F               ; 
94C2: 0C                              ;
94C3: 1C                              ;
94C4: 0F                              ;
94C5: 11 0C           ORA     ($0C),Y             ; {ram.000C}
94C7: 1C                              ;
94C8: 0F                              ;
94C9: 0F                              ;
94CA: 0C                              ;
94CB: 0C                              ;
94CC: 0F                              ;
94CD: 02                              ;
94CE: 0C                              ;
94CF: 0C                              ;
94D0: 0F                              ;
94D1: 0F                              ;
94D2: 0F                              ;
94D3: 0C                              ;
94D4: 0F                              ;
94D5: 0F                              ;
94D6: 0F                              ;
94D7: 0F                              ;
94D8: 0F                              ;
94D9: 06 17           ASL     <$17                ; {ram.0017}
94DB: 16 0F           ASL     $0F,X               ; {ram.000F}
94DD: 06 17           ASL     <$17                ; {ram.0017}
94DF: 16 0F           ASL     $0F,X               ; {ram.000F}
94E1: 07                              ;
94E2: 06 16           ASL     <$16                ; {ram.0016}
94E4: 0F                              ;
94E5: 07                              ;
94E6: 06 16           ASL     <$16                ; {ram.0016}
94E8: 0F                              ;
94E9: 0F                              ;
94EA: 07                              ;
94EB: 06 0F           ASL     <$0F                ; {ram.000F}
94ED: 0F                              ;
94EE: 07                              ;
94EF: 06 0F           ASL     <$0F                ; {ram.000F}
94F1: 0F                              ;
94F2: 0F                              ;
94F3: 0F                              ;
94F4: 0F                              ;
94F5: 0F                              ;
94F6: 0F                              ;
94F7: 0F                              ;
94F8: 3F                              ;
94F9: 00              BRK                         ; 
94FA: 20 0F 30        JSR     $300F               ; 
94FD: 00              BRK                         ; 
94FE: 12                              ;
94FF: 0F                              ;
9500: 16 27           ASL     $27,X               ; {ram.0027}
9502: 36 0F           ROL     $0F,X               ; {ram.000F}
9504: 02                              ;
9505: 12                              ;
9506: 22                              ;
9507: 0F                              ;
9508: 16 12           ASL     $12,X               ; {ram.0012}
950A: 22                              ;
950B: 0F                              ;
950C: 29 27           AND     #$27                ; 
950E: 17                              ;
950F: 0F                              ;
9510: 02                              ;
9511: 22                              ;
9512: 30 0F           BMI     $9523               ; {}
9514: 16 27           ASL     $27,X               ; {ram.0027}
9516: 30 0F           BMI     $9527               ; {}
9518: 02                              ;
9519: 12                              ;
951A: 22                              ;
951B: FF                              ;
951C: 03                              ;
951D: 05 06           ORA     <$06                ; {ram.0006}
951F: 08              PHP                         ; 
9520: DD 89 D6        CMP     $D689,X             ; 
9523: 26 2C           ROL     <$2C                ; {ram.002C}
9525: 0A              ASL     A                   ; 
9526: B0 7D           BCS     $95A5               ; {}
9528: 0D FF 06        ORA     $06FF               ; {ram.06FF}
952B: 02                              ;
952C: FF                              ;
952D: FF                              ;
952E: FF                              ;
952F: FF                              ;
9530: FF                              ;
9531: FF                              ;
9532: FF                              ;
9533: FF                              ;
9534: FF                              ;
9535: FF                              ;
9536: 0E 00 00        ASL     $0000               ; {ram.GP_00}
9539: 00              BRK                         ; 
953A: 00              BRK                         ; 
953B: 00              BRK                         ; 
953C: 00              BRK                         ; 
953D: 02                              ;
953E: 83                              ;
953F: FF                              ;
9540: 7E 00 00        ROR     $0000,X             ; {ram.GP_00}
9543: 00              BRK                         ; 
9544: 00              BRK                         ; 
9545: 00              BRK                         ; 
9546: 00              BRK                         ; 
9547: 20 65 03        JSR     $0365               ; {ram.0365}
954A: 67                              ;
954B: FF                              ;
954C: FB                              ;
954D: 20 86 02        JSR     $0286               ; {ram.0286}
9550: FF                              ;
9551: FF                              ;
9552: 20 A6 02        JSR     $02A6               ; {ram.02A6}
9555: FF                              ;
9556: FF                              ;
9557: 20 C4 04        JSR     $04C4               ; {ram.04C4}
955A: 67                              ;
955B: FF                              ;
955C: FF                              ;
955D: 67                              ;
955E: FF                              ;
955F: FF                              ;
9560: FF                              ;
9561: FF                              ;
9562: FF                              ;
9563: FF                              ;
9564: FF                              ;
9565: FF                              ;
9566: FF                              ;
9567: FF                              ;
9568: FF                              ;
9569: FF                              ;
956A: FF                              ;
956B: FF                              ;
956C: FF                              ;
956D: FF                              ;
956E: FF                              ;
956F: FF                              ;
9570: FF                              ;
9571: FF                              ;
9572: FF                              ;
9573: FF                              ;
9574: 0F                              ;
9575: 02                              ;
9576: 12                              ;
9577: 22                              ;
9578: 0F                              ;
9579: 16 12           ASL     $12,X               ; {ram.0012}
957B: 22                              ;
957C: 0F                              ;
957D: 01 02           ORA     ($02,X)             ; {ram.GP_02}
957F: 12                              ;
9580: 0F                              ;
9581: 17                              ;
9582: 02                              ;
9583: 12                              ;
9584: 0F                              ;
9585: 0F                              ;
9586: 01 02           ORA     ($02,X)             ; {ram.GP_02}
9588: 0F                              ;
9589: 06 01           ASL     <$01                ; {ram.GP_01}
958B: 02                              ;
958C: 0F                              ;
958D: 0F                              ;
958E: 0F                              ;
958F: 0F                              ;
9590: 0F                              ;
9591: 0F                              ;
9592: 0F                              ;
9593: 0F                              ;
9594: 0F                              ;
9595: 00              BRK                         ; 
9596: 10 30           BPL     $95C8               ; {}
9598: 0F                              ;
9599: 00              BRK                         ; 
959A: 10 30           BPL     $95CC               ; {}
959C: 0F                              ;
959D: 00              BRK                         ; 
959E: 00              BRK                         ; 
959F: 10 0F           BPL     $95B0               ; {}
95A1: 00              BRK                         ; 
95A2: 00              BRK                         ; 
95A3: 10 0F           BPL     $95B4               ; {}
95A5: 0F                              ;
95A6: 00              BRK                         ; 
95A7: 00              BRK                         ; 
95A8: 0F                              ;
95A9: 0F                              ;
95AA: 00              BRK                         ; 
95AB: 00              BRK                         ; 
95AC: 0F                              ;
95AD: 0F                              ;
95AE: 0F                              ;
95AF: 0F                              ;
95B0: 0F                              ;
95B1: 0F                              ;
95B2: 0F                              ;
95B3: 0F                              ;
95B4: 0F                              ;
95B5: 02                              ;
95B6: 12                              ;
95B7: 22                              ;
95B8: 0F                              ;
95B9: 16 12           ASL     $12,X               ; {ram.0012}
95BB: 22                              ;
95BC: 0F                              ;
95BD: 01 02           ORA     ($02,X)             ; {ram.GP_02}
95BF: 12                              ;
95C0: 0F                              ;
95C1: 17                              ;
95C2: 02                              ;
95C3: 12                              ;
95C4: 0F                              ;
95C5: 0F                              ;
95C6: 01 02           ORA     ($02,X)             ; {ram.GP_02}
95C8: 0F                              ;
95C9: 06 01           ASL     <$01                ; {ram.GP_01}
95CB: 02                              ;
95CC: 0F                              ;
95CD: 0F                              ;
95CE: 0F                              ;
95CF: 01 0F           ORA     ($0F,X)             ; {ram.000F}
95D1: 0F                              ;
95D2: 0F                              ;
95D3: 0F                              ;
95D4: 0F                              ;
95D5: 06 17           ASL     <$17                ; {ram.0017}
95D7: 16 0F           ASL     $0F,X               ; {ram.000F}
95D9: 06 17           ASL     <$17                ; {ram.0017}
95DB: 16 0F           ASL     $0F,X               ; {ram.000F}
95DD: 07                              ;
95DE: 06 16           ASL     <$16                ; {ram.0016}
95E0: 0F                              ;
95E1: 07                              ;
95E2: 06 16           ASL     <$16                ; {ram.0016}
95E4: 0F                              ;
95E5: 0F                              ;
95E6: 07                              ;
95E7: 06 0F           ASL     <$0F                ; {ram.000F}
95E9: 0F                              ;
95EA: 07                              ;
95EB: 06 0F           ASL     <$0F                ; {ram.000F}
95ED: 0F                              ;
95EE: 0F                              ;
95EF: 0F                              ;
95F0: 0F                              ;
95F1: 0F                              ;
95F2: 0F                              ;
95F3: 0F                              ;
95F4: 3F                              ;
95F5: 00              BRK                         ; 
95F6: 20 0F 30        JSR     $300F               ; 
95F9: 00              BRK                         ; 
95FA: 12                              ;
95FB: 0F                              ;
95FC: 16 27           ASL     $27,X               ; {ram.0027}
95FE: 36 0F           ROL     $0F,X               ; {ram.000F}
9600: 0B                              ;
9601: 1B                              ;
9602: 2B                              ;
9603: 0F                              ;
9604: 16 1B           ASL     $1B,X               ; {ram.001B}
9606: 2B                              ;
9607: 0F                              ;
9608: 29 37           AND     #$37                ; 
960A: 17                              ;
960B: 0F                              ;
960C: 02                              ;
960D: 22                              ;
960E: 30 0F           BMI     $961F               ; {}
9610: 16 27           ASL     $27,X               ; {ram.0027}
9612: 30 0F           BMI     $9623               ; {}
9614: 0B                              ;
9615: 1B                              ;
9616: 2B                              ;
9617: FF                              ;
9618: 03                              ;
9619: 05 06           ORA     <$06                ; {ram.0006}
961B: 08              PHP                         ; 
961C: DD 89 D6        CMP     $D689,X             ; 
961F: 26 2C           ROL     <$2C                ; {ram.002C}
9621: 0C                              ;
9622: C0 7C           CPY     #$7C                ; 
9624: 3D FF 06        AND     $06FF,X             ; {ram.06FF}
9627: 03                              ;
9628: FF                              ;
9629: FF                              ;
962A: FF                              ;
962B: FF                              ;
962C: FF                              ;
962D: FF                              ;
962E: FF                              ;
962F: FF                              ;
9630: FF                              ;
9631: FF                              ;
9632: 4D 00 00        EOR     $0000               ; {ram.GP_00}
9635: 00              BRK                         ; 
9636: 00              BRK                         ; 
9637: 00              BRK                         ; 
9638: 0E 2C 3F        ASL     $3F2C               ; 
963B: 0D 1C 00        ORA     $001C               ; {ram.001C}
963E: 00              BRK                         ; 
963F: 00              BRK                         ; 
9640: 00              BRK                         ; 
9641: 00              BRK                         ; 
9642: 00              BRK                         ; 
9643: 20 84 04        JSR     $0484               ; {ram.0484}
9646: 67                              ;
9647: FF                              ;
9648: 24 FB           BIT     <$FB                ; {ram.00FB}
964A: 20 A3 05        JSR     $05A3               ; {ram.05A3}
964D: FF                              ;
964E: FF                              ;
964F: FF                              ;
9650: FF                              ;
9651: FF                              ;
9652: 20 C3 04        JSR     $04C3               ; {ram.04C3}
9655: 67                              ;
9656: 24 FF           BIT     <$FF                ; {ram.CUR_2000}
9658: FB                              ;
9659: FF                              ;
965A: FF                              ;
965B: FF                              ;
965C: FF                              ;
965D: FF                              ;
965E: FF                              ;
965F: FF                              ;
9660: FF                              ;
9661: FF                              ;
9662: FF                              ;
9663: FF                              ;
9664: FF                              ;
9665: FF                              ;
9666: FF                              ;
9667: FF                              ;
9668: FF                              ;
9669: FF                              ;
966A: FF                              ;
966B: FF                              ;
966C: FF                              ;
966D: FF                              ;
966E: FF                              ;
966F: FF                              ;
9670: 0F                              ;
9671: 0B                              ;
9672: 1B                              ;
9673: 2B                              ;
9674: 0F                              ;
9675: 16 1B           ASL     $1B,X               ; {ram.001B}
9677: 2B                              ;
9678: 0F                              ;
9679: 0B                              ;
967A: 0B                              ;
967B: 1B                              ;
967C: 0F                              ;
967D: 17                              ;
967E: 0B                              ;
967F: 1B                              ;
9680: 0F                              ;
9681: 0F                              ;
9682: 0B                              ;
9683: 0B                              ;
9684: 0F                              ;
9685: 06 0B           ASL     <$0B                ; {ram.000B}
9687: 0B                              ;
9688: 0F                              ;
9689: 0F                              ;
968A: 0F                              ;
968B: 0F                              ;
968C: 0F                              ;
968D: 0F                              ;
968E: 0F                              ;
968F: 0F                              ;
9690: 0F                              ;
9691: 00              BRK                         ; 
9692: 10 30           BPL     $96C4               ; {}
9694: 0F                              ;
9695: 00              BRK                         ; 
9696: 10 30           BPL     $96C8               ; {}
9698: 0F                              ;
9699: 00              BRK                         ; 
969A: 00              BRK                         ; 
969B: 10 0F           BPL     $96AC               ; {}
969D: 00              BRK                         ; 
969E: 00              BRK                         ; 
969F: 10 0F           BPL     $96B0               ; {}
96A1: 0F                              ;
96A2: 00              BRK                         ; 
96A3: 00              BRK                         ; 
96A4: 0F                              ;
96A5: 0F                              ;
96A6: 00              BRK                         ; 
96A7: 00              BRK                         ; 
96A8: 0F                              ;
96A9: 0F                              ;
96AA: 0F                              ;
96AB: 0F                              ;
96AC: 0F                              ;
96AD: 0F                              ;
96AE: 0F                              ;
96AF: 0F                              ;
96B0: 0F                              ;
96B1: 0B                              ;
96B2: 1B                              ;
96B3: 2B                              ;
96B4: 0F                              ;
96B5: 16 1B           ASL     $1B,X               ; {ram.001B}
96B7: 2B                              ;
96B8: 0F                              ;
96B9: 0B                              ;
96BA: 0B                              ;
96BB: 1B                              ;
96BC: 0F                              ;
96BD: 17                              ;
96BE: 0B                              ;
96BF: 1B                              ;
96C0: 0F                              ;
96C1: 0F                              ;
96C2: 0B                              ;
96C3: 0B                              ;
96C4: 0F                              ;
96C5: 06 0B           ASL     <$0B                ; {ram.000B}
96C7: 0B                              ;
96C8: 0F                              ;
96C9: 0F                              ;
96CA: 0F                              ;
96CB: 0B                              ;
96CC: 0F                              ;
96CD: 0F                              ;
96CE: 0F                              ;
96CF: 0F                              ;
96D0: 0F                              ;
96D1: 06 17           ASL     <$17                ; {ram.0017}
96D3: 16 0F           ASL     $0F,X               ; {ram.000F}
96D5: 06 17           ASL     <$17                ; {ram.0017}
96D7: 16 0F           ASL     $0F,X               ; {ram.000F}
96D9: 07                              ;
96DA: 06 16           ASL     <$16                ; {ram.0016}
96DC: 0F                              ;
96DD: 07                              ;
96DE: 06 16           ASL     <$16                ; {ram.0016}
96E0: 0F                              ;
96E1: 0F                              ;
96E2: 07                              ;
96E3: 06 0F           ASL     <$0F                ; {ram.000F}
96E5: 0F                              ;
96E6: 07                              ;
96E7: 06 0F           ASL     <$0F                ; {ram.000F}
96E9: 0F                              ;
96EA: 0F                              ;
96EB: 0F                              ;
96EC: 0F                              ;
96ED: 0F                              ;
96EE: 0F                              ;
96EF: 0F                              ;
96F0: 3F                              ;
96F1: 00              BRK                         ; 
96F2: 20 0F 30        JSR     $300F               ; 
96F5: 00              BRK                         ; 
96F6: 12                              ;
96F7: 0F                              ;
96F8: 16 27           ASL     $27,X               ; {ram.0027}
96FA: 36 0F           ROL     $0F,X               ; {ram.000F}
96FC: 08              PHP                         ; 
96FD: 18              CLC                         ; 
96FE: 28              PLP                         ; 
96FF: 0F                              ;
9700: 12                              ;
9701: 18              CLC                         ; 
9702: 28              PLP                         ; 
9703: 0F                              ;
9704: 29 27           AND     #$27                ; 
9706: 17                              ;
9707: 0F                              ;
9708: 02                              ;
9709: 22                              ;
970A: 30 0F           BMI     $971B               ; {}
970C: 16 27           ASL     $27,X               ; {ram.0027}
970E: 30 0F           BMI     $971F               ; {}
9710: 0F                              ;
9711: 18              CLC                         ; 
9712: 28              PLP                         ; 
9713: FF                              ;
9714: 03                              ;
9715: 05 06           ORA     <$06                ; {ram.0006}
9717: 08              PHP                         ; 
9718: DD DC 99        CMP     $99DC,X             ; {}
971B: 88              DEY                         ; 
971C: 89                              ;
971D: 06 10           ASL     <$10                ; {ram.0010}
971F: 71 03           ADC     ($03),Y             ; {ram.GP_03}
9721: FF                              ;
9722: 06 04           ASL     <$04                ; {ram.0004}
9724: 60              RTS                         ; 
9725: FF                              ;
9726: FF                              ;
9727: FF                              ;
9728: FF                              ;
9729: FF                              ;
972A: FF                              ;
972B: FF                              ;
972C: FF                              ;
972D: FF                              ;
972E: 13                              ;
972F: 00              BRK                         ; 
9730: 00              BRK                         ; 
9731: 00              BRK                         ; 
9732: 00              BRK                         ; 
9733: 00              BRK                         ; 
9734: 00              BRK                         ; 
9735: FD B7 D2        SBC     $D2B7,X             ; 
9738: C0 00           CPY     #$00                ; 
973A: 00              BRK                         ; 
973B: 00              BRK                         ; 
973C: 00              BRK                         ; 
973D: 00              BRK                         ; 
973E: 00              BRK                         ; 
973F: 20 64 04        JSR     $0464               ; {ram.0464}
9742: FF                              ;
9743: 67                              ;
9744: FF                              ;
9745: FF                              ;
9746: 20 84 03        JSR     $0384               ; {ram.0384}
9749: FF                              ;
974A: FF                              ;
974B: FB                              ;
974C: 20 A4 02        JSR     $02A4               ; {ram.02A4}
974F: FF                              ;
9750: FB                              ;
9751: 20 C4 03        JSR     $03C4               ; {ram.03C4}
9754: FB                              ;
9755: FF                              ;
9756: 67                              ;
9757: FF                              ;
9758: FF                              ;
9759: FF                              ;
975A: FF                              ;
975B: FF                              ;
975C: FF                              ;
975D: FF                              ;
975E: FF                              ;
975F: FF                              ;
9760: FF                              ;
9761: FF                              ;
9762: FF                              ;
9763: FF                              ;
9764: FF                              ;
9765: FF                              ;
9766: FF                              ;
9767: FF                              ;
9768: FF                              ;
9769: FF                              ;
976A: FF                              ;
976B: FF                              ;
976C: 0F                              ;
976D: 08              PHP                         ; 
976E: 18              CLC                         ; 
976F: 28              PLP                         ; 
9770: 0F                              ;
9771: 12                              ;
9772: 18              CLC                         ; 
9773: 28              PLP                         ; 
9774: 0F                              ;
9775: 08              PHP                         ; 
9776: 08              PHP                         ; 
9777: 18              CLC                         ; 
9778: 0F                              ;
9779: 11 08           ORA     ($08),Y             ; {ram.0008}
977B: 18              CLC                         ; 
977C: 0F                              ;
977D: 0F                              ;
977E: 08              PHP                         ; 
977F: 08              PHP                         ; 
9780: 0F                              ;
9781: 02                              ;
9782: 08              PHP                         ; 
9783: 08              PHP                         ; 
9784: 0F                              ;
9785: 0F                              ;
9786: 0F                              ;
9787: 0F                              ;
9788: 0F                              ;
9789: 0F                              ;
978A: 0F                              ;
978B: 0F                              ;
978C: 0F                              ;
978D: 00              BRK                         ; 
978E: 10 30           BPL     $97C0               ; {}
9790: 0F                              ;
9791: 00              BRK                         ; 
9792: 10 30           BPL     $97C4               ; {}
9794: 0F                              ;
9795: 00              BRK                         ; 
9796: 00              BRK                         ; 
9797: 10 0F           BPL     $97A8               ; {}
9799: 00              BRK                         ; 
979A: 00              BRK                         ; 
979B: 10 0F           BPL     $97AC               ; {}
979D: 0F                              ;
979E: 00              BRK                         ; 
979F: 00              BRK                         ; 
97A0: 0F                              ;
97A1: 0F                              ;
97A2: 00              BRK                         ; 
97A3: 00              BRK                         ; 
97A4: 0F                              ;
97A5: 0F                              ;
97A6: 0F                              ;
97A7: 0F                              ;
97A8: 0F                              ;
97A9: 0F                              ;
97AA: 0F                              ;
97AB: 0F                              ;
97AC: 0F                              ;
97AD: 08              PHP                         ; 
97AE: 18              CLC                         ; 
97AF: 28              PLP                         ; 
97B0: 0F                              ;
97B1: 12                              ;
97B2: 18              CLC                         ; 
97B3: 28              PLP                         ; 
97B4: 0F                              ;
97B5: 08              PHP                         ; 
97B6: 08              PHP                         ; 
97B7: 18              CLC                         ; 
97B8: 0F                              ;
97B9: 11 08           ORA     ($08),Y             ; {ram.0008}
97BB: 18              CLC                         ; 
97BC: 0F                              ;
97BD: 0F                              ;
97BE: 08              PHP                         ; 
97BF: 08              PHP                         ; 
97C0: 0F                              ;
97C1: 02                              ;
97C2: 08              PHP                         ; 
97C3: 08              PHP                         ; 
97C4: 0F                              ;
97C5: 0F                              ;
97C6: 0F                              ;
97C7: 08              PHP                         ; 
97C8: 0F                              ;
97C9: 0F                              ;
97CA: 0F                              ;
97CB: 0F                              ;
97CC: 0F                              ;
97CD: 06 17           ASL     <$17                ; {ram.0017}
97CF: 16 0F           ASL     $0F,X               ; {ram.000F}
97D1: 06 17           ASL     <$17                ; {ram.0017}
97D3: 16 0F           ASL     $0F,X               ; {ram.000F}
97D5: 07                              ;
97D6: 06 16           ASL     <$16                ; {ram.0016}
97D8: 0F                              ;
97D9: 07                              ;
97DA: 06 16           ASL     <$16                ; {ram.0016}
97DC: 0F                              ;
97DD: 0F                              ;
97DE: 07                              ;
97DF: 06 0F           ASL     <$0F                ; {ram.000F}
97E1: 0F                              ;
97E2: 07                              ;
97E3: 06 0F           ASL     <$0F                ; {ram.000F}
97E5: 0F                              ;
97E6: 0F                              ;
97E7: 0F                              ;
97E8: 0F                              ;
97E9: 0F                              ;
97EA: 0F                              ;
97EB: 0F                              ;
97EC: 3F                              ;
97ED: 00              BRK                         ; 
97EE: 20 0F 30        JSR     $300F               ; 
97F1: 00              BRK                         ; 
97F2: 12                              ;
97F3: 0F                              ;
97F4: 16 27           ASL     $27,X               ; {ram.0027}
97F6: 36 0F           ROL     $0F,X               ; {ram.000F}
97F8: 0A              ASL     A                   ; 
97F9: 1A                              ;
97FA: 2A              ROL     A                   ; 
97FB: 0F                              ;
97FC: 16 1A           ASL     $1A,X               ; {ram.001A}
97FE: 2A              ROL     A                   ; 
97FF: 0F                              ;
9800: 29 27           AND     #$27                ; 
9802: 17                              ;
9803: 0F                              ;
9804: 02                              ;
9805: 22                              ;
9806: 30 0F           BMI     $9817               ; {}
9808: 16 27           ASL     $27,X               ; {ram.0027}
980A: 30 0F           BMI     $981B               ; {}
980C: 0A              ASL     A                   ; 
980D: 1A                              ;
980E: 2A              ROL     A                   ; 
980F: FF                              ;
9810: 03                              ;
9811: 05 06           ORA     <$06                ; {ram.0006}
9813: 08              PHP                         ; 
9814: DD 87 C8        CMP     $C887,X             ; 
9817: 8A              TXA                         ; 
9818: 89                              ;
9819: 02                              ;
981A: F0 76           BEQ     $9892               ; {}
981C: 14                              ;
981D: FF                              ;
981E: 06 05           ASL     <$05                ; {ram.0005}
9820: 07                              ;
9821: 04                              ;
9822: FF                              ;
9823: FF                              ;
9824: FF                              ;
9825: FF                              ;
9826: FF                              ;
9827: FF                              ;
9828: FF                              ;
9829: FF                              ;
982A: 24 00           BIT     <$00                ; {ram.GP_00}
982C: 00              BRK                         ; 
982D: 00              BRK                         ; 
982E: 00              BRK                         ; 
982F: 00              BRK                         ; 
9830: 00              BRK                         ; 
9831: 72                              ;
9832: A6 EF           LDX     <$EF                ; {ram.00EF}
9834: 7F                              ;
9835: 00              BRK                         ; 
9836: 00              BRK                         ; 
9837: 00              BRK                         ; 
9838: 00              BRK                         ; 
9839: 00              BRK                         ; 
983A: 00              BRK                         ; 
983B: 20 64 04        JSR     $0464               ; {ram.0464}
983E: FB                              ;
983F: 67                              ;
9840: FF                              ;
9841: FB                              ;
9842: 20 84 04        JSR     $0484               ; {ram.0484}
9845: FF                              ;
9846: 67                              ;
9847: 67                              ;
9848: FF                              ;
9849: 20 A5 03        JSR     $03A5               ; {ram.03A5}
984C: FB                              ;
984D: FF                              ;
984E: FF                              ;
984F: 20 C4 04        JSR     $04C4               ; {ram.04C4}
9852: 67                              ;
9853: 67                              ;
9854: FF                              ;
9855: FF                              ;
9856: FF                              ;
9857: FF                              ;
9858: FF                              ;
9859: FF                              ;
985A: FF                              ;
985B: FF                              ;
985C: FF                              ;
985D: FF                              ;
985E: FF                              ;
985F: FF                              ;
9860: FF                              ;
9861: FF                              ;
9862: FF                              ;
9863: FF                              ;
9864: FF                              ;
9865: FF                              ;
9866: FF                              ;
9867: FF                              ;
9868: 0F                              ;
9869: 0A              ASL     A                   ; 
986A: 1A                              ;
986B: 2A              ROL     A                   ; 
986C: 0F                              ;
986D: 16 1A           ASL     $1A,X               ; {ram.001A}
986F: 2A              ROL     A                   ; 
9870: 0F                              ;
9871: 0A              ASL     A                   ; 
9872: 0A              ASL     A                   ; 
9873: 1A                              ;
9874: 0F                              ;
9875: 17                              ;
9876: 0A              ASL     A                   ; 
9877: 1A                              ;
9878: 0F                              ;
9879: 0F                              ;
987A: 0A              ASL     A                   ; 
987B: 0A              ASL     A                   ; 
987C: 0F                              ;
987D: 06 0A           ASL     <$0A                ; {ram.000A}
987F: 0A              ASL     A                   ; 
9880: 0F                              ;
9881: 0F                              ;
9882: 0F                              ;
9883: 0F                              ;
9884: 0F                              ;
9885: 0F                              ;
9886: 0F                              ;
9887: 0F                              ;
9888: 0F                              ;
9889: 00              BRK                         ; 
988A: 10 30           BPL     $98BC               ; {}
988C: 0F                              ;
988D: 00              BRK                         ; 
988E: 10 30           BPL     $98C0               ; {}
9890: 0F                              ;
9891: 00              BRK                         ; 
9892: 00              BRK                         ; 
9893: 10 0F           BPL     $98A4               ; {}
9895: 00              BRK                         ; 
9896: 00              BRK                         ; 
9897: 10 0F           BPL     $98A8               ; {}
9899: 0F                              ;
989A: 00              BRK                         ; 
989B: 00              BRK                         ; 
989C: 0F                              ;
989D: 0F                              ;
989E: 00              BRK                         ; 
989F: 00              BRK                         ; 
98A0: 0F                              ;
98A1: 0F                              ;
98A2: 0F                              ;
98A3: 0F                              ;
98A4: 0F                              ;
98A5: 0F                              ;
98A6: 0F                              ;
98A7: 0F                              ;
98A8: 0F                              ;
98A9: 0A              ASL     A                   ; 
98AA: 1A                              ;
98AB: 2A              ROL     A                   ; 
98AC: 0F                              ;
98AD: 16 1A           ASL     $1A,X               ; {ram.001A}
98AF: 2A              ROL     A                   ; 
98B0: 0F                              ;
98B1: 0A              ASL     A                   ; 
98B2: 0A              ASL     A                   ; 
98B3: 1A                              ;
98B4: 0F                              ;
98B5: 17                              ;
98B6: 0A              ASL     A                   ; 
98B7: 1A                              ;
98B8: 0F                              ;
98B9: 0F                              ;
98BA: 0A              ASL     A                   ; 
98BB: 0A              ASL     A                   ; 
98BC: 0F                              ;
98BD: 06 0A           ASL     <$0A                ; {ram.000A}
98BF: 0A              ASL     A                   ; 
98C0: 0F                              ;
98C1: 0F                              ;
98C2: 0F                              ;
98C3: 0A              ASL     A                   ; 
98C4: 0F                              ;
98C5: 0F                              ;
98C6: 0F                              ;
98C7: 0F                              ;
98C8: 0F                              ;
98C9: 06 17           ASL     <$17                ; {ram.0017}
98CB: 16 0F           ASL     $0F,X               ; {ram.000F}
98CD: 06 17           ASL     <$17                ; {ram.0017}
98CF: 16 0F           ASL     $0F,X               ; {ram.000F}
98D1: 07                              ;
98D2: 06 16           ASL     <$16                ; {ram.0016}
98D4: 0F                              ;
98D5: 07                              ;
98D6: 06 16           ASL     <$16                ; {ram.0016}
98D8: 0F                              ;
98D9: 0F                              ;
98DA: 07                              ;
98DB: 06 0F           ASL     <$0F                ; {ram.000F}
98DD: 0F                              ;
98DE: 07                              ;
98DF: 06 0F           ASL     <$0F                ; {ram.000F}
98E1: 0F                              ;
98E2: 0F                              ;
98E3: 0F                              ;
98E4: 0F                              ;
98E5: 0F                              ;
98E6: 0F                              ;
98E7: 0F                              ;
98E8: 3F                              ;
98E9: 00              BRK                         ; 
98EA: 20 0F 30        JSR     $300F               ; 
98ED: 00              BRK                         ; 
98EE: 12                              ;
98EF: 0F                              ;
98F0: 16 27           ASL     $27,X               ; {ram.0027}
98F2: 36 0F           ROL     $0F,X               ; {ram.000F}
98F4: 08              PHP                         ; 
98F5: 18              CLC                         ; 
98F6: 28              PLP                         ; 
98F7: 0F                              ;
98F8: 16 18           ASL     $18,X               ; {ram.0018}
98FA: 28              PLP                         ; 
98FB: 0F                              ;
98FC: 29 27           AND     #$27                ; 
98FE: 17                              ;
98FF: 0F                              ;
9900: 02                              ;
9901: 22                              ;
9902: 30 0F           BMI     $9913               ; {}
9904: 16 27           ASL     $27,X               ; {ram.0027}
9906: 30 0F           BMI     $9917               ; {}
9908: 08              PHP                         ; 
9909: 18              CLC                         ; 
990A: 28              PLP                         ; 
990B: FF                              ;
990C: 03                              ;
990D: 05 06           ORA     <$06                ; {ram.0006}
990F: 08              PHP                         ; 
9910: DD 89 D6        CMP     $D689,X             ; 
9913: 26 2C           ROL     <$2C                ; {ram.002C}
9915: 0D C8 79        ORA     $79C8               ; {ram.79C8}
9918: 0C                              ;
9919: FF                              ;
991A: 06 06           ASL     <$06                ; {ram.0006}
991C: 08              PHP                         ; 
991D: 75 FF           ADC     <$FF,X              ; {ram.CUR_2000}
991F: FF                              ;
9920: FF                              ;
9921: FF                              ;
9922: FF                              ;
9923: FF                              ;
9924: FF                              ;
9925: FF                              ;
9926: 1C                              ;
9927: 00              BRK                         ; 
9928: 00              BRK                         ; 
9929: 00              BRK                         ; 
992A: 00              BRK                         ; 
992B: 00              BRK                         ; 
992C: 7F                              ;
992D: F1 D3           SBC     ($D3),Y             ; {ram.00D3}
992F: C0 F0           CPY     #$F0                ; 
9931: 60              RTS                         ; 
9932: 00              BRK                         ; 
9933: 00              BRK                         ; 
9934: 00              BRK                         ; 
9935: 00              BRK                         ; 
9936: 00              BRK                         ; 
9937: 20 63 06        JSR     $0663               ; {ram.0663}
993A: FB                              ;
993B: FF                              ;
993C: FF                              ;
993D: FF                              ;
993E: FF                              ;
993F: FB                              ;
9940: 20 83 06        JSR     $0683               ; {ram.0683}
9943: FF                              ;
9944: FF                              ;
9945: FB                              ;
9946: 24 FF           BIT     <$FF                ; {ram.CUR_2000}
9948: 67                              ;
9949: 20 A3 01        JSR     $01A3               ; {ram.01A3}
994C: FF                              ;
994D: 20 C3 03        JSR     $03C3               ; {ram.03C3}
9950: FF                              ;
9951: FB                              ;
9952: FF                              ;
9953: FF                              ;
9954: FF                              ;
9955: FF                              ;
9956: FF                              ;
9957: FF                              ;
9958: FF                              ;
9959: FF                              ;
995A: FF                              ;
995B: FF                              ;
995C: FF                              ;
995D: FF                              ;
995E: FF                              ;
995F: FF                              ;
9960: FF                              ;
9961: FF                              ;
9962: FF                              ;
9963: FF                              ;
9964: 0F                              ;
9965: 08              PHP                         ; 
9966: 18              CLC                         ; 
9967: 28              PLP                         ; 
9968: 0F                              ;
9969: 16 18           ASL     $18,X               ; {ram.0018}
996B: 28              PLP                         ; 
996C: 0F                              ;
996D: 08              PHP                         ; 
996E: 08              PHP                         ; 
996F: 18              CLC                         ; 
9970: 0F                              ;
9971: 17                              ;
9972: 08              PHP                         ; 
9973: 18              CLC                         ; 
9974: 0F                              ;
9975: 0F                              ;
9976: 08              PHP                         ; 
9977: 08              PHP                         ; 
9978: 0F                              ;
9979: 06 08           ASL     <$08                ; {ram.0008}
997B: 08              PHP                         ; 
997C: 0F                              ;
997D: 0F                              ;
997E: 0F                              ;
997F: 0F                              ;
9980: 0F                              ;
9981: 0F                              ;
9982: 0F                              ;
9983: 0F                              ;
9984: 0F                              ;
9985: 00              BRK                         ; 
9986: 10 30           BPL     $99B8               ; {}
9988: 0F                              ;
9989: 00              BRK                         ; 
998A: 10 30           BPL     $99BC               ; {}
998C: 0F                              ;
998D: 00              BRK                         ; 
998E: 00              BRK                         ; 
998F: 10 0F           BPL     $99A0               ; {}
9991: 00              BRK                         ; 
9992: 00              BRK                         ; 
9993: 10 0F           BPL     $99A4               ; {}
9995: 0F                              ;
9996: 00              BRK                         ; 
9997: 00              BRK                         ; 
9998: 0F                              ;
9999: 0F                              ;
999A: 00              BRK                         ; 
999B: 00              BRK                         ; 
999C: 0F                              ;
999D: 0F                              ;
999E: 0F                              ;
999F: 0F                              ;
99A0: 0F                              ;
99A1: 0F                              ;
99A2: 0F                              ;
99A3: 0F                              ;
99A4: 0F                              ;
99A5: 08              PHP                         ; 
99A6: 18              CLC                         ; 
99A7: 28              PLP                         ; 
99A8: 0F                              ;
99A9: 16 18           ASL     $18,X               ; {ram.0018}
99AB: 28              PLP                         ; 
99AC: 0F                              ;
99AD: 08              PHP                         ; 
99AE: 08              PHP                         ; 
99AF: 18              CLC                         ; 
99B0: 0F                              ;
99B1: 17                              ;
99B2: 08              PHP                         ; 
99B3: 18              CLC                         ; 
99B4: 0F                              ;
99B5: 0F                              ;
99B6: 08              PHP                         ; 
99B7: 08              PHP                         ; 
99B8: 0F                              ;
99B9: 06 08           ASL     <$08                ; {ram.0008}
99BB: 08              PHP                         ; 
99BC: 0F                              ;
99BD: 0F                              ;
99BE: 0F                              ;
99BF: 08              PHP                         ; 
99C0: 0F                              ;
99C1: 0F                              ;
99C2: 0F                              ;
99C3: 0F                              ;
99C4: 0F                              ;
99C5: 06 17           ASL     <$17                ; {ram.0017}
99C7: 16 0F           ASL     $0F,X               ; {ram.000F}
99C9: 06 17           ASL     <$17                ; {ram.0017}
99CB: 16 0F           ASL     $0F,X               ; {ram.000F}
99CD: 07                              ;
99CE: 06 16           ASL     <$16                ; {ram.0016}
99D0: 0F                              ;
99D1: 07                              ;
99D2: 06 16           ASL     <$16                ; {ram.0016}
99D4: 0F                              ;
99D5: 0F                              ;
99D6: 07                              ;
99D7: 06 0F           ASL     <$0F                ; {ram.000F}
99D9: 0F                              ;
99DA: 07                              ;
99DB: 06 0F           ASL     <$0F                ; {ram.000F}
99DD: 0F                              ;
99DE: 0F                              ;
99DF: 0F                              ;
99E0: 0F                              ;
99E1: 0F                              ;
99E2: 0F                              ;
99E3: 0F                              ;
99E4: 3F                              ;
99E5: 00              BRK                         ; 
99E6: 20 0F 30        JSR     $300F               ; 
99E9: 00              BRK                         ; 
99EA: 12                              ;
99EB: 0F                              ;
99EC: 16 27           ASL     $27,X               ; {ram.0027}
99EE: 36 0F           ROL     $0F,X               ; {ram.000F}
99F0: 0A              ASL     A                   ; 
99F1: 1A                              ;
99F2: 2A              ROL     A                   ; 
99F3: 0F                              ;
99F4: 12                              ;
99F5: 1A                              ;
99F6: 2A              ROL     A                   ; 
99F7: 0F                              ;
99F8: 29 27           AND     #$27                ; 
99FA: 17                              ;
99FB: 0F                              ;
99FC: 02                              ;
99FD: 22                              ;
99FE: 30 0F           BMI     $9A0F               ; {}
9A00: 16 27           ASL     $27,X               ; {ram.0027}
9A02: 30 0F           BMI     $9A13               ; {}
9A04: 0A              ASL     A                   ; 
9A05: 1A                              ;
9A06: 2A              ROL     A                   ; 
9A07: FF                              ;
9A08: 03                              ;
9A09: 05 06           ORA     <$06                ; {ram.0006}
9A0B: 08              PHP                         ; 
9A0C: DD 89 D6        CMP     $D689,X             ; 
9A0F: 26 2C           ROL     <$2C                ; {ram.002C}
9A11: 0D C8 79        ORA     $79C8               ; {ram.79C8}
9A14: 2B                              ;
9A15: 7F                              ;
9A16: 07                              ;
9A17: 07                              ;
9A18: 7B                              ;
9A19: 4A              LSR     A                   ; 
9A1A: FF                              ;
9A1B: FF                              ;
9A1C: FF                              ;
9A1D: FF                              ;
9A1E: FF                              ;
9A1F: FF                              ;
9A20: FF                              ;
9A21: FF                              ;
9A22: 2A              ROL     A                   ; 
9A23: 00              BRK                         ; 
9A24: 00              BRK                         ; 
9A25: 00              BRK                         ; 
9A26: 00              BRK                         ; 
9A27: 00              BRK                         ; 
9A28: 7F                              ;
9A29: FF                              ;
9A2A: B7                              ;
9A2B: E6 C2           INC     <$C2                ; {ram.00C2}
9A2D: 82                              ;
9A2E: 00              BRK                         ; 
9A2F: 00              BRK                         ; 
9A30: 00              BRK                         ; 
9A31: 00              BRK                         ; 
9A32: 00              BRK                         ; 
9A33: 20 63 06        JSR     $0663               ; {ram.0663}
9A36: FB                              ;
9A37: FF                              ;
9A38: 67                              ;
9A39: FF                              ;
9A3A: FF                              ;
9A3B: 67                              ;
9A3C: 20 83 04        JSR     $0483               ; {ram.0483}
9A3F: FF                              ;
9A40: FF                              ;
9A41: FF                              ;
9A42: 67                              ;
9A43: 20 A3 04        JSR     $04A3               ; {ram.04A3}
9A46: FF                              ;
9A47: FF                              ;
9A48: FB                              ;
9A49: FB                              ;
9A4A: 20 C3 06        JSR     $06C3               ; {ram.06C3}
9A4D: FF                              ;
9A4E: FF                              ;
9A4F: FF                              ;
9A50: 67                              ;
9A51: 67                              ;
9A52: 67                              ;
9A53: FF                              ;
9A54: FF                              ;
9A55: FF                              ;
9A56: FF                              ;
9A57: FF                              ;
9A58: FF                              ;
9A59: FF                              ;
9A5A: FF                              ;
9A5B: FF                              ;
9A5C: FF                              ;
9A5D: FF                              ;
9A5E: FF                              ;
9A5F: FF                              ;
9A60: 0F                              ;
9A61: 0A              ASL     A                   ; 
9A62: 1A                              ;
9A63: 2A              ROL     A                   ; 
9A64: 0F                              ;
9A65: 12                              ;
9A66: 1A                              ;
9A67: 2A              ROL     A                   ; 
9A68: 0F                              ;
9A69: 0A              ASL     A                   ; 
9A6A: 0A              ASL     A                   ; 
9A6B: 1A                              ;
9A6C: 0F                              ;
9A6D: 11 0A           ORA     ($0A),Y             ; {ram.000A}
9A6F: 1A                              ;
9A70: 0F                              ;
9A71: 0F                              ;
9A72: 0A              ASL     A                   ; 
9A73: 0A              ASL     A                   ; 
9A74: 0F                              ;
9A75: 02                              ;
9A76: 0A              ASL     A                   ; 
9A77: 0A              ASL     A                   ; 
9A78: 0F                              ;
9A79: 0F                              ;
9A7A: 0F                              ;
9A7B: 0F                              ;
9A7C: 0F                              ;
9A7D: 0F                              ;
9A7E: 0F                              ;
9A7F: 0F                              ;
9A80: 0F                              ;
9A81: 00              BRK                         ; 
9A82: 10 30           BPL     $9AB4               ; {}
9A84: 0F                              ;
9A85: 00              BRK                         ; 
9A86: 10 30           BPL     $9AB8               ; {}
9A88: 0F                              ;
9A89: 00              BRK                         ; 
9A8A: 00              BRK                         ; 
9A8B: 10 0F           BPL     $9A9C               ; {}
9A8D: 00              BRK                         ; 
9A8E: 00              BRK                         ; 
9A8F: 10 0F           BPL     $9AA0               ; {}
9A91: 0F                              ;
9A92: 00              BRK                         ; 
9A93: 00              BRK                         ; 
9A94: 0F                              ;
9A95: 0F                              ;
9A96: 00              BRK                         ; 
9A97: 00              BRK                         ; 
9A98: 0F                              ;
9A99: 0F                              ;
9A9A: 0F                              ;
9A9B: 0F                              ;
9A9C: 0F                              ;
9A9D: 0F                              ;
9A9E: 0F                              ;
9A9F: 0F                              ;
9AA0: 0F                              ;
9AA1: 0A              ASL     A                   ; 
9AA2: 1A                              ;
9AA3: 2A              ROL     A                   ; 
9AA4: 0F                              ;
9AA5: 12                              ;
9AA6: 1A                              ;
9AA7: 2A              ROL     A                   ; 
9AA8: 0F                              ;
9AA9: 0A              ASL     A                   ; 
9AAA: 0A              ASL     A                   ; 
9AAB: 1A                              ;
9AAC: 0F                              ;
9AAD: 11 0A           ORA     ($0A),Y             ; {ram.000A}
9AAF: 1A                              ;
9AB0: 0F                              ;
9AB1: 0F                              ;
9AB2: 0A              ASL     A                   ; 
9AB3: 0A              ASL     A                   ; 
9AB4: 0F                              ;
9AB5: 02                              ;
9AB6: 0A              ASL     A                   ; 
9AB7: 0A              ASL     A                   ; 
9AB8: 0F                              ;
9AB9: 0F                              ;
9ABA: 0F                              ;
9ABB: 0A              ASL     A                   ; 
9ABC: 0F                              ;
9ABD: 0F                              ;
9ABE: 0F                              ;
9ABF: 0F                              ;
9AC0: 0F                              ;
9AC1: 06 17           ASL     <$17                ; {ram.0017}
9AC3: 16 0F           ASL     $0F,X               ; {ram.000F}
9AC5: 06 17           ASL     <$17                ; {ram.0017}
9AC7: 16 0F           ASL     $0F,X               ; {ram.000F}
9AC9: 07                              ;
9ACA: 06 16           ASL     <$16                ; {ram.0016}
9ACC: 0F                              ;
9ACD: 07                              ;
9ACE: 06 16           ASL     <$16                ; {ram.0016}
9AD0: 0F                              ;
9AD1: 0F                              ;
9AD2: 07                              ;
9AD3: 06 0F           ASL     <$0F                ; {ram.000F}
9AD5: 0F                              ;
9AD6: 07                              ;
9AD7: 06 0F           ASL     <$0F                ; {ram.000F}
9AD9: 0F                              ;
9ADA: 0F                              ;
9ADB: 0F                              ;
9ADC: 0F                              ;
9ADD: 0F                              ;
9ADE: 0F                              ;
9ADF: 0F                              ;
9AE0: 3F                              ;
9AE1: 00              BRK                         ; 
9AE2: 20 0F 30        JSR     $300F               ; 
9AE5: 00              BRK                         ; 
9AE6: 12                              ;
9AE7: 0F                              ;
9AE8: 16 27           ASL     $27,X               ; {ram.0027}
9AEA: 36 0F           ROL     $0F,X               ; {ram.000F}
9AEC: 00              BRK                         ; 
9AED: 10 30           BPL     $9B1F               ; {}
9AEF: 0F                              ;
9AF0: 22                              ;
9AF1: 10 30           BPL     $9B23               ; {}
9AF3: 0F                              ;
9AF4: 29 27           AND     #$27                ; 
9AF6: 17                              ;
9AF7: 0F                              ;
9AF8: 02                              ;
9AF9: 22                              ;
9AFA: 30 0F           BMI     $9B0B               ; {}
9AFC: 16 27           ASL     $27,X               ; {ram.0027}
9AFE: 30 0F           BMI     $9B0F               ; {}
9B00: 00              BRK                         ; 
9B01: 10 30           BPL     $9B33               ; {}
9B03: FF                              ;
9B04: 03                              ;
9B05: 05 06           ORA     <$06                ; {ram.0006}
9B07: 08              PHP                         ; 
9B08: DD 89 D6        CMP     $D689,X             ; 
9B0B: 26 2C           ROL     <$2C                ; {ram.002C}
9B0D: 0A              ASL     A                   ; 
9B0E: B0 7E           BCS     $9B8E               ; {}
9B10: 2C 7F 07        BIT     $077F               ; {ram.077F}
9B13: 08              PHP                         ; 
9B14: 2F                              ;
9B15: 0F                              ;
9B16: 6F                              ;
9B17: FF                              ;
9B18: FF                              ;
9B19: FF                              ;
9B1A: FF                              ;
9B1B: FF                              ;
9B1C: FF                              ;
9B1D: FF                              ;
9B1E: 3C                              ;
9B1F: 00              BRK                         ; 
9B20: 00              BRK                         ; 
9B21: 00              BRK                         ; 
9B22: 00              BRK                         ; 
9B23: 00              BRK                         ; 
9B24: 18              CLC                         ; 
9B25: 3D 5D FF        AND     $FF5D,X             ; 
9B28: 55 00           EOR     $00,X               ; {ram.GP_00}
9B2A: 00              BRK                         ; 
9B2B: 00              BRK                         ; 
9B2C: 00              BRK                         ; 
9B2D: 00              BRK                         ; 
9B2E: 00              BRK                         ; 
9B2F: 20 65 03        JSR     $0365               ; {ram.0365}
9B32: FB                              ;
9B33: FF                              ;
9B34: FB                              ;
9B35: 20 83 05        JSR     $0583               ; {ram.0583}
9B38: FB                              ;
9B39: FF                              ;
9B3A: FB                              ;
9B3B: FF                              ;
9B3C: FB                              ;
9B3D: 20 A3 05        JSR     $05A3               ; {ram.05A3}
9B40: 67                              ;
9B41: FF                              ;
9B42: FF                              ;
9B43: FF                              ;
9B44: FB                              ;
9B45: 20 C4 04        JSR     $04C4               ; {ram.04C4}
9B48: FB                              ;
9B49: FB                              ;
9B4A: FF                              ;
9B4B: FB                              ;
9B4C: FF                              ;
9B4D: FF                              ;
9B4E: FF                              ;
9B4F: FF                              ;
9B50: FF                              ;
9B51: FF                              ;
9B52: FF                              ;
9B53: FF                              ;
9B54: FF                              ;
9B55: FF                              ;
9B56: FF                              ;
9B57: FF                              ;
9B58: FF                              ;
9B59: FF                              ;
9B5A: FF                              ;
9B5B: FF                              ;
9B5C: 0F                              ;
9B5D: 00              BRK                         ; 
9B5E: 10 30           BPL     $9B90               ; {}
9B60: 0F                              ;
9B61: 22                              ;
9B62: 10 30           BPL     $9B94               ; {}
9B64: 0F                              ;
9B65: 00              BRK                         ; 
9B66: 00              BRK                         ; 
9B67: 10 0F           BPL     $9B78               ; {}
9B69: 12                              ;
9B6A: 00              BRK                         ; 
9B6B: 10 0F           BPL     $9B7C               ; {}
9B6D: 0F                              ;
9B6E: 00              BRK                         ; 
9B6F: 00              BRK                         ; 
9B70: 0F                              ;
9B71: 02                              ;
9B72: 00              BRK                         ; 
9B73: 00              BRK                         ; 
9B74: 0F                              ;
9B75: 0F                              ;
9B76: 0F                              ;
9B77: 0F                              ;
9B78: 0F                              ;
9B79: 0F                              ;
9B7A: 0F                              ;
9B7B: 0F                              ;
9B7C: 0F                              ;
9B7D: 00              BRK                         ; 
9B7E: 10 30           BPL     $9BB0               ; {}
9B80: 0F                              ;
9B81: 00              BRK                         ; 
9B82: 10 30           BPL     $9BB4               ; {}
9B84: 0F                              ;
9B85: 00              BRK                         ; 
9B86: 00              BRK                         ; 
9B87: 10 0F           BPL     $9B98               ; {}
9B89: 00              BRK                         ; 
9B8A: 00              BRK                         ; 
9B8B: 10 0F           BPL     $9B9C               ; {}
9B8D: 0F                              ;
9B8E: 00              BRK                         ; 
9B8F: 00              BRK                         ; 
9B90: 0F                              ;
9B91: 0F                              ;
9B92: 00              BRK                         ; 
9B93: 00              BRK                         ; 
9B94: 0F                              ;
9B95: 0F                              ;
9B96: 0F                              ;
9B97: 0F                              ;
9B98: 0F                              ;
9B99: 0F                              ;
9B9A: 0F                              ;
9B9B: 0F                              ;
9B9C: 0F                              ;
9B9D: 00              BRK                         ; 
9B9E: 10 30           BPL     $9BD0               ; {}
9BA0: 0F                              ;
9BA1: 22                              ;
9BA2: 10 30           BPL     $9BD4               ; {}
9BA4: 0F                              ;
9BA5: 00              BRK                         ; 
9BA6: 00              BRK                         ; 
9BA7: 10 0F           BPL     $9BB8               ; {}
9BA9: 12                              ;
9BAA: 00              BRK                         ; 
9BAB: 10 0F           BPL     $9BBC               ; {}
9BAD: 0F                              ;
9BAE: 00              BRK                         ; 
9BAF: 00              BRK                         ; 
9BB0: 0F                              ;
9BB1: 02                              ;
9BB2: 00              BRK                         ; 
9BB3: 00              BRK                         ; 
9BB4: 0F                              ;
9BB5: 0F                              ;
9BB6: 0F                              ;
9BB7: 00              BRK                         ; 
9BB8: 0F                              ;
9BB9: 0F                              ;
9BBA: 0F                              ;
9BBB: 0F                              ;
9BBC: 0F                              ;
9BBD: 06 17           ASL     <$17                ; {ram.0017}
9BBF: 16 0F           ASL     $0F,X               ; {ram.000F}
9BC1: 06 17           ASL     <$17                ; {ram.0017}
9BC3: 16 0F           ASL     $0F,X               ; {ram.000F}
9BC5: 07                              ;
9BC6: 06 16           ASL     <$16                ; {ram.0016}
9BC8: 0F                              ;
9BC9: 07                              ;
9BCA: 06 16           ASL     <$16                ; {ram.0016}
9BCC: 0F                              ;
9BCD: 0F                              ;
9BCE: 07                              ;
9BCF: 06 0F           ASL     <$0F                ; {ram.000F}
9BD1: 0F                              ;
9BD2: 07                              ;
9BD3: 06 0F           ASL     <$0F                ; {ram.000F}
9BD5: 0F                              ;
9BD6: 0F                              ;
9BD7: 0F                              ;
9BD8: 0F                              ;
9BD9: 0F                              ;
9BDA: 0F                              ;
9BDB: 0F                              ;
9BDC: 3F                              ;
9BDD: 00              BRK                         ; 
9BDE: 20 0F 30        JSR     $300F               ; 
9BE1: 00              BRK                         ; 
9BE2: 12                              ;
9BE3: 0F                              ;
9BE4: 16 27           ASL     $27,X               ; {ram.0027}
9BE6: 36 0F           ROL     $0F,X               ; {ram.000F}
9BE8: 00              BRK                         ; 
9BE9: 10 30           BPL     $9C1B               ; {}
9BEB: 0F                              ;
9BEC: 16 10           ASL     $10,X               ; {ram.0010}
9BEE: 30 0F           BMI     $9BFF               ; {}
9BF0: 29 27           AND     #$27                ; 
9BF2: 17                              ;
9BF3: 0F                              ;
9BF4: 02                              ;
9BF5: 22                              ;
9BF6: 30 0F           BMI     $9C07               ; {}
9BF8: 16 27           ASL     $27,X               ; {ram.0027}
9BFA: 30 0F           BMI     $9C0B               ; {}
9BFC: 0F                              ;
9BFD: 10 30           BPL     $9C2F               ; {}
9BFF: FF                              ;
9C00: 03                              ;
9C01: 05 06           ORA     <$06                ; {ram.0006}
9C03: 08              PHP                         ; 
9C04: DD 89 D6        CMP     $D689,X             ; 
9C07: 26 2C           ROL     <$2C                ; {ram.002C}
9C09: 04                              ;
9C0A: 00              BRK                         ; 
9C0B: 76 32           ROR     <$32,X              ; {ram.0032}
9C0D: 7F                              ;
9C0E: 07                              ;
9C0F: 09 60           ORA     #$60                ; 
9C11: 70 72           BVS     $9C85               ; {}
9C13: 75 67           ADC     <$67,X              ; {ram.SND_PtrB}
9C15: 77                              ;
9C16: 00              BRK                         ; 
9C17: 4F                              ;
9C18: FF                              ;
9C19: FF                              ;
9C1A: 42                              ;
9C1B: 00              BRK                         ; 
9C1C: 00              BRK                         ; 
9C1D: 00              BRK                         ; 
9C1E: 00              BRK                         ; 
9C1F: 7C                              ;
9C20: FF                              ;
9C21: EE FF FF        INC     $FFFF               ; 
9C24: EE FF 7C        INC     $7CFF               ; {ram.7CFF}
9C27: 00              BRK                         ; 
9C28: 00              BRK                         ; 
9C29: 00              BRK                         ; 
9C2A: 00              BRK                         ; 
9C2B: 20 62 08        JSR     $0862               ; 
9C2E: FB                              ;
9C2F: FF                              ;
9C30: FF                              ;
9C31: FF                              ;
9C32: FF                              ;
9C33: FF                              ;
9C34: FF                              ;
9C35: FB                              ;
9C36: 20 82 08        JSR     $0882               ; 
9C39: FF                              ;
9C3A: FF                              ;
9C3B: 67                              ;
9C3C: FF                              ;
9C3D: FF                              ;
9C3E: 67                              ;
9C3F: FF                              ;
9C40: FF                              ;
9C41: 20 A2 48        JSR     $48A2               ; 
9C44: FF                              ;
9C45: 20 C3 06        JSR     $06C3               ; {ram.06C3}
9C48: FF                              ;
9C49: 67                              ;
9C4A: FF                              ;
9C4B: FF                              ;
9C4C: 67                              ;
9C4D: FF                              ;
9C4E: FF                              ;
9C4F: FF                              ;
9C50: FF                              ;
9C51: FF                              ;
9C52: FF                              ;
9C53: FF                              ;
9C54: FF                              ;
9C55: FF                              ;
9C56: FF                              ;
9C57: FF                              ;
9C58: 0F                              ;
9C59: 00              BRK                         ; 
9C5A: 10 30           BPL     $9C8C               ; {}
9C5C: 0F                              ;
9C5D: 16 10           ASL     $10,X               ; {ram.0010}
9C5F: 30 0F           BMI     $9C70               ; {}
9C61: 00              BRK                         ; 
9C62: 00              BRK                         ; 
9C63: 10 0F           BPL     $9C74               ; {}
9C65: 17                              ;
9C66: 00              BRK                         ; 
9C67: 10 0F           BPL     $9C78               ; {}
9C69: 0F                              ;
9C6A: 00              BRK                         ; 
9C6B: 00              BRK                         ; 
9C6C: 0F                              ;
9C6D: 06 00           ASL     <$00                ; {ram.GP_00}
9C6F: 00              BRK                         ; 
9C70: 0F                              ;
9C71: 0F                              ;
9C72: 0F                              ;
9C73: 0F                              ;
9C74: 0F                              ;
9C75: 0F                              ;
9C76: 0F                              ;
9C77: 0F                              ;
9C78: 0F                              ;
9C79: 00              BRK                         ; 
9C7A: 10 30           BPL     $9CAC               ; {}
9C7C: 0F                              ;
9C7D: 00              BRK                         ; 
9C7E: 10 30           BPL     $9CB0               ; {}
9C80: 0F                              ;
9C81: 00              BRK                         ; 
9C82: 00              BRK                         ; 
9C83: 10 0F           BPL     $9C94               ; {}
9C85: 00              BRK                         ; 
9C86: 00              BRK                         ; 
9C87: 10 0F           BPL     $9C98               ; {}
9C89: 0F                              ;
9C8A: 00              BRK                         ; 
9C8B: 00              BRK                         ; 
9C8C: 0F                              ;
9C8D: 0F                              ;
9C8E: 00              BRK                         ; 
9C8F: 00              BRK                         ; 
9C90: 0F                              ;
9C91: 0F                              ;
9C92: 0F                              ;
9C93: 0F                              ;
9C94: 0F                              ;
9C95: 0F                              ;
9C96: 0F                              ;
9C97: 0F                              ;
9C98: 0F                              ;
9C99: 00              BRK                         ; 
9C9A: 10 30           BPL     $9CCC               ; {}
9C9C: 0F                              ;
9C9D: 16 10           ASL     $10,X               ; {ram.0010}
9C9F: 30 0F           BMI     $9CB0               ; {}
9CA1: 00              BRK                         ; 
9CA2: 00              BRK                         ; 
9CA3: 10 0F           BPL     $9CB4               ; {}
9CA5: 17                              ;
9CA6: 00              BRK                         ; 
9CA7: 10 0F           BPL     $9CB8               ; {}
9CA9: 0F                              ;
9CAA: 00              BRK                         ; 
9CAB: 00              BRK                         ; 
9CAC: 0F                              ;
9CAD: 06 00           ASL     <$00                ; {ram.GP_00}
9CAF: 00              BRK                         ; 
9CB0: 0F                              ;
9CB1: 0F                              ;
9CB2: 0F                              ;
9CB3: 00              BRK                         ; 
9CB4: 0F                              ;
9CB5: 0F                              ;
9CB6: 0F                              ;
9CB7: 0F                              ;
9CB8: 0F                              ;
9CB9: 06 17           ASL     <$17                ; {ram.0017}
9CBB: 16 0F           ASL     $0F,X               ; {ram.000F}
9CBD: 06 17           ASL     <$17                ; {ram.0017}
9CBF: 16 0F           ASL     $0F,X               ; {ram.000F}
9CC1: 07                              ;
9CC2: 06 16           ASL     <$16                ; {ram.0016}
9CC4: 0F                              ;
9CC5: 07                              ;
9CC6: 06 16           ASL     <$16                ; {ram.0016}
9CC8: 0F                              ;
9CC9: 0F                              ;
9CCA: 07                              ;
9CCB: 06 0F           ASL     <$0F                ; {ram.000F}
9CCD: 0F                              ;
9CCE: 07                              ;
9CCF: 06 0F           ASL     <$0F                ; {ram.000F}
9CD1: 0F                              ;
9CD2: 0F                              ;
9CD3: 0F                              ;
9CD4: 0F                              ;
9CD5: 0F                              ;
9CD6: 0F                              ;
9CD7: 0F                              ;
9CD8: 3F                              ;
9CD9: 00              BRK                         ; 
9CDA: 20 0F 30        JSR     $300F               ; 
9CDD: 00              BRK                         ; 
9CDE: 12                              ;
9CDF: 0F                              ;
9CE0: 16 27           ASL     $27,X               ; {ram.0027}
9CE2: 36 0F           ROL     $0F,X               ; {ram.000F}
9CE4: 0C                              ;
9CE5: 1C                              ;
9CE6: 2C 0F 12        BIT     $120F               ; 
9CE9: 1C                              ;
9CEA: 2C 0F 29        BIT     $290F               ; 
9CED: 27                              ;
9CEE: 07                              ;
9CEF: 0F                              ;
9CF0: 22                              ;
9CF1: 27                              ;
9CF2: 07                              ;
9CF3: 0F                              ;
9CF4: 26 27           ROL     <$27                ; {ram.0027}
9CF6: 07                              ;
9CF7: 0F                              ;
9CF8: 15 27           ORA     $27,X               ; {ram.0027}
9CFA: 30 FF           BMI     $9CFB               ; {}
9CFC: 3F                              ;
9CFD: 1C                              ;
9CFE: 04                              ;
9CFF: 0F                              ;
9D00: 0F                              ;
9D01: 0F                              ;
9D02: 0F                              ;
9D03: FF                              ;
9D04: 20 42 07        JSR     $0742               ; {ram.0742}
9D07: 15 0E           ORA     $0E,X               ; {ram.000E}
9D09: 1F                              ;
9D0A: 0E 15 62        ASL     $6215               ; {ram.6215}
9D0D: 00              BRK                         ; 
9D0E: FF                              ;
9D0F: D8              CLD                         ; 
9D10: 9B                              ;
9D11: 0D 9C 3E        ORA     $3E9C               ; 
9D14: 9C                              ;
9D15: 80                              ;
9D16: 9C                              ;
9D17: C4 9C           CPY     <$9C                ; {ram.009C}
9D19: F6 9C           INC     $9C,X               ; {ram.009C}
9D1B: 32                              ;
9D1C: 9D 6D 9D        STA     $9D6D,X             ; {}
9D1F: A8              TAY                         ; 
9D20: 9D E6 9D        STA     $9DE6,X             ; {}
9D23: 27                              ;
9D24: 9E                              ;
9D25: 6C 9E A9        JMP     ($A99E)             ; {}
9D28: 9E                              ;
9D29: DF                              ;
9D2A: 9E                              ;
9D2B: 21 9F           AND     ($9F,X)             ; 
9D2D: 55 9F           EOR     $9F,X               ; 
9D2F: 2A              ROL     A                   ; 
9D30: EE 04 ED        INC     $ED04               ; 
9D33: E9 EA           SBC     #$EA                ; 
9D35: EE FF 2B        INC     $2BFF               ; 
9D38: 0D 06 ED        ORA     $ED06               ; 
9D3B: E9 24           SBC     #$24                ; 
9D3D: 24 EA           BIT     <$EA                ; {ram.00EA}
9D3F: EE FF 2B        INC     $2BFF               ; 
9D42: 2C 08 ED        BIT     $ED08               ; 
9D45: E9 24           SBC     #$24                ; 
9D47: 24 24           BIT     <$24                ; {ram.0024}
9D49: 24 EA           BIT     <$EA                ; {ram.00EA}
9D4B: EE FF 2B        INC     $2BFF               ; 
9D4E: 4B                              ;
9D4F: 0A              ASL     A                   ; 
9D50: ED E9 24        SBC     $24E9               ; 
9D53: 24 24           BIT     <$24                ; {ram.0024}
9D55: 24 24           BIT     <$24                ; {ram.0024}
9D57: 24 EA           BIT     <$EA                ; {ram.00EA}
9D59: EE FF 2B        INC     $2BFF               ; 
9D5C: AC 08 1D        LDY     $1D08               ; 
9D5F: 1B                              ;
9D60: 12                              ;
9D61: 0F                              ;
9D62: 18              CLC                         ; 
9D63: 1B                              ;
9D64: 0C                              ;
9D65: 0E FF FF        ASL     $FFFF               ; 
9D68: FF                              ;
9D69: FF                              ;
9D6A: FF                              ;
9D6B: FF                              ;
9D6C: FF                              ;
9D6D: FF                              ;
9D6E: FF                              ;
9D6F: FF                              ;
9D70: FF                              ;
9D71: FF                              ;
9D72: FF                              ;
9D73: FF                              ;
9D74: FF                              ;
9D75: FF                              ;
9D76: FF                              ;
9D77: FF                              ;
9D78: FF                              ;
9D79: FF                              ;
9D7A: FF                              ;
9D7B: FF                              ;
9D7C: FF                              ;
9D7D: FF                              ;
9D7E: FF                              ;
9D7F: FF                              ;
9D80: FF                              ;
9D81: FF                              ;
9D82: FF                              ;
9D83: FF                              ;
9D84: FF                              ;
9D85: FF                              ;
9D86: FF                              ;
9D87: FF                              ;
9D88: FF                              ;
9D89: FF                              ;
9D8A: FF                              ;
9D8B: FF                              ;
9D8C: FF                              ;
9D8D: FF                              ;
9D8E: FF                              ;
9D8F: FF                              ;
9D90: FF                              ;
9D91: FF                              ;
9D92: FF                              ;
9D93: FF                              ;
9D94: FF                              ;
9D95: FF                              ;
9D96: FF                              ;
9D97: FF                              ;
9D98: FF                              ;
9D99: FF                              ;
9D9A: FF                              ;
9D9B: FF                              ;
9D9C: FF                              ;
9D9D: FF                              ;
9D9E: FF                              ;
9D9F: FF                              ;
9DA0: FF                              ;
9DA1: FF                              ;
9DA2: FF                              ;
9DA3: FF                              ;
9DA4: FF                              ;
9DA5: FF                              ;
9DA6: FF                              ;
9DA7: FF                              ;
9DA8: FF                              ;
9DA9: FF                              ;
9DAA: FF                              ;
9DAB: FF                              ;
9DAC: FF                              ;
9DAD: FF                              ;
9DAE: FF                              ;
9DAF: FF                              ;
9DB0: FF                              ;
9DB1: FF                              ;
9DB2: FF                              ;
9DB3: FF                              ;
9DB4: FF                              ;
9DB5: FF                              ;
9DB6: FF                              ;
9DB7: FF                              ;
9DB8: FF                              ;
9DB9: FF                              ;
9DBA: FF                              ;
9DBB: FF                              ;
9DBC: FF                              ;
9DBD: FF                              ;
9DBE: FF                              ;
9DBF: FF                              ;
9DC0: FF                              ;
9DC1: FF                              ;
9DC2: FF                              ;
9DC3: FF                              ;
9DC4: FF                              ;
9DC5: FF                              ;
9DC6: FF                              ;
9DC7: FF                              ;
9DC8: FF                              ;
9DC9: FF                              ;
9DCA: FF                              ;
9DCB: FF                              ;
9DCC: FF                              ;
9DCD: FF                              ;
9DCE: FF                              ;
9DCF: FF                              ;
9DD0: FF                              ;
9DD1: FF                              ;
9DD2: FF                              ;
9DD3: FF                              ;
9DD4: FF                              ;
9DD5: FF                              ;
9DD6: FF                              ;
9DD7: FF                              ;
9DD8: FF                              ;
9DD9: FF                              ;
9DDA: FF                              ;
9DDB: FF                              ;
9DDC: FF                              ;
9DDD: FF                              ;
9DDE: FF                              ;
9DDF: FF                              ;
9DE0: FF                              ;
9DE1: FF                              ;
9DE2: FF                              ;
9DE3: FF                              ;
9DE4: FF                              ;
9DE5: FF                              ;
9DE6: FF                              ;
9DE7: FF                              ;
9DE8: FF                              ;
9DE9: FF                              ;
9DEA: FF                              ;
9DEB: FF                              ;
9DEC: FF                              ;
9DED: FF                              ;
9DEE: FF                              ;
9DEF: FF                              ;
9DF0: FF                              ;
9DF1: FF                              ;
9DF2: FF                              ;
9DF3: FF                              ;
9DF4: FF                              ;
9DF5: FF                              ;
9DF6: FF                              ;
9DF7: FF                              ;
9DF8: FF                              ;
9DF9: FF                              ;
9DFA: FF                              ;
9DFB: FF                              ;
9DFC: FF                              ;
9DFD: FF                              ;
9DFE: FF                              ;
9DFF: FF                              ;
9E00: FF                              ;
9E01: FF                              ;
9E02: FF                              ;
9E03: FF                              ;
9E04: FF                              ;
9E05: FF                              ;
9E06: FF                              ;
9E07: FF                              ;
9E08: FF                              ;
9E09: FF                              ;
9E0A: FF                              ;
9E0B: FF                              ;
9E0C: FF                              ;
9E0D: FF                              ;
9E0E: FF                              ;
9E0F: FF                              ;
9E10: FF                              ;
9E11: FF                              ;
9E12: FF                              ;
9E13: FF                              ;
9E14: FF                              ;
9E15: FF                              ;
9E16: FF                              ;
9E17: FF                              ;
9E18: FF                              ;
9E19: FF                              ;
9E1A: FF                              ;
9E1B: FF                              ;
9E1C: FF                              ;
9E1D: FF                              ;
9E1E: FF                              ;
9E1F: FF                              ;
9E20: FF                              ;
9E21: FF                              ;
9E22: FF                              ;
9E23: FF                              ;
9E24: FF                              ;
9E25: FF                              ;
9E26: FF                              ;
9E27: FF                              ;
9E28: FF                              ;
9E29: FF                              ;
9E2A: FF                              ;
9E2B: FF                              ;
9E2C: FF                              ;
9E2D: FF                              ;
9E2E: FF                              ;
9E2F: FF                              ;
9E30: FF                              ;
9E31: FF                              ;
9E32: FF                              ;
9E33: FF                              ;
9E34: FF                              ;
9E35: FF                              ;
9E36: FF                              ;
9E37: FF                              ;
9E38: FF                              ;
9E39: FF                              ;
9E3A: FF                              ;
9E3B: FF                              ;
9E3C: FF                              ;
9E3D: FF                              ;
9E3E: FF                              ;
9E3F: FF                              ;
9E40: FF                              ;
9E41: FF                              ;
9E42: FF                              ;
9E43: FF                              ;
9E44: FF                              ;
9E45: FF                              ;
9E46: FF                              ;
9E47: FF                              ;
9E48: FF                              ;
9E49: FF                              ;
9E4A: FF                              ;
9E4B: FF                              ;
9E4C: FF                              ;
9E4D: FF                              ;
9E4E: FF                              ;
9E4F: FF                              ;
9E50: FF                              ;
9E51: FF                              ;
9E52: FF                              ;
9E53: FF                              ;
9E54: FF                              ;
9E55: FF                              ;
9E56: FF                              ;
9E57: FF                              ;
9E58: FF                              ;
9E59: FF                              ;
9E5A: FF                              ;
9E5B: FF                              ;
9E5C: FF                              ;
9E5D: FF                              ;
9E5E: FF                              ;
9E5F: FF                              ;
9E60: FF                              ;
9E61: FF                              ;
9E62: FF                              ;
9E63: FF                              ;
9E64: FF                              ;
9E65: FF                              ;
9E66: FF                              ;
9E67: FF                              ;
9E68: FF                              ;
9E69: FF                              ;
9E6A: FF                              ;
9E6B: FF                              ;
9E6C: FF                              ;
9E6D: FF                              ;
9E6E: FF                              ;
9E6F: FF                              ;
9E70: FF                              ;
9E71: FF                              ;
9E72: FF                              ;
9E73: FF                              ;
9E74: FF                              ;
9E75: FF                              ;
9E76: FF                              ;
9E77: FF                              ;
9E78: FF                              ;
9E79: FF                              ;
9E7A: FF                              ;
9E7B: FF                              ;
9E7C: FF                              ;
9E7D: FF                              ;
9E7E: FF                              ;
9E7F: FF                              ;
9E80: FF                              ;
9E81: FF                              ;
9E82: FF                              ;
9E83: FF                              ;
9E84: FF                              ;
9E85: FF                              ;
9E86: FF                              ;
9E87: FF                              ;
9E88: FF                              ;
9E89: FF                              ;
9E8A: FF                              ;
9E8B: FF                              ;
9E8C: FF                              ;
9E8D: FF                              ;
9E8E: FF                              ;
9E8F: FF                              ;
9E90: FF                              ;
9E91: FF                              ;
9E92: FF                              ;
9E93: FF                              ;
9E94: FF                              ;
9E95: FF                              ;
9E96: FF                              ;
9E97: FF                              ;
9E98: FF                              ;
9E99: FF                              ;
9E9A: FF                              ;
9E9B: FF                              ;
9E9C: FF                              ;
9E9D: FF                              ;
9E9E: FF                              ;
9E9F: FF                              ;
9EA0: FF                              ;
9EA1: FF                              ;
9EA2: FF                              ;
9EA3: FF                              ;
9EA4: FF                              ;
9EA5: FF                              ;
9EA6: FF                              ;
9EA7: FF                              ;
9EA8: FF                              ;
9EA9: FF                              ;
9EAA: FF                              ;
9EAB: FF                              ;
9EAC: FF                              ;
9EAD: FF                              ;
9EAE: FF                              ;
9EAF: FF                              ;
9EB0: FF                              ;
9EB1: FF                              ;
9EB2: FF                              ;
9EB3: FF                              ;
9EB4: FF                              ;
9EB5: FF                              ;
9EB6: FF                              ;
9EB7: FF                              ;
9EB8: FF                              ;
9EB9: FF                              ;
9EBA: FF                              ;
9EBB: FF                              ;
9EBC: FF                              ;
9EBD: FF                              ;
9EBE: FF                              ;
9EBF: FF                              ;
9EC0: FF                              ;
9EC1: FF                              ;
9EC2: FF                              ;
9EC3: FF                              ;
9EC4: FF                              ;
9EC5: FF                              ;
9EC6: FF                              ;
9EC7: FF                              ;
9EC8: FF                              ;
9EC9: FF                              ;
9ECA: FF                              ;
9ECB: FF                              ;
9ECC: FF                              ;
9ECD: FF                              ;
9ECE: FF                              ;
9ECF: FF                              ;
9ED0: FF                              ;
9ED1: FF                              ;
9ED2: FF                              ;
9ED3: FF                              ;
9ED4: FF                              ;
9ED5: FF                              ;
9ED6: FF                              ;
9ED7: FF                              ;
9ED8: FF                              ;
9ED9: FF                              ;
9EDA: FF                              ;
9EDB: FF                              ;
9EDC: FF                              ;
9EDD: FF                              ;
9EDE: FF                              ;
9EDF: FF                              ;
9EE0: FF                              ;
9EE1: FF                              ;
9EE2: FF                              ;
9EE3: FF                              ;
9EE4: FF                              ;
9EE5: FF                              ;
9EE6: FF                              ;
9EE7: FF                              ;
9EE8: FF                              ;
9EE9: FF                              ;
9EEA: FF                              ;
9EEB: FF                              ;
9EEC: FF                              ;
9EED: FF                              ;
9EEE: FF                              ;
9EEF: FF                              ;
9EF0: FF                              ;
9EF1: FF                              ;
9EF2: FF                              ;
9EF3: FF                              ;
9EF4: FF                              ;
9EF5: FF                              ;
9EF6: FF                              ;
9EF7: FF                              ;
9EF8: FF                              ;
9EF9: FF                              ;
9EFA: FF                              ;
9EFB: FF                              ;
9EFC: FF                              ;
9EFD: FF                              ;
9EFE: FF                              ;
9EFF: FF                              ;
9F00: FF                              ;
9F01: FF                              ;
9F02: FF                              ;
9F03: FF                              ;
9F04: FF                              ;
9F05: FF                              ;
9F06: FF                              ;
9F07: FF                              ;
9F08: FF                              ;
9F09: FF                              ;
9F0A: FF                              ;
9F0B: FF                              ;
9F0C: FF                              ;
9F0D: FF                              ;
9F0E: FF                              ;
9F0F: FF                              ;
9F10: FF                              ;
9F11: FF                              ;
9F12: FF                              ;
9F13: FF                              ;
9F14: FF                              ;
9F15: FF                              ;
9F16: FF                              ;
9F17: FF                              ;
9F18: FF                              ;
9F19: FF                              ;
9F1A: FF                              ;
9F1B: FF                              ;
9F1C: FF                              ;
9F1D: FF                              ;
9F1E: FF                              ;
9F1F: FF                              ;
9F20: FF                              ;
9F21: FF                              ;
9F22: FF                              ;
9F23: FF                              ;
9F24: FF                              ;
9F25: FF                              ;
9F26: FF                              ;
9F27: FF                              ;
9F28: FF                              ;
9F29: FF                              ;
9F2A: FF                              ;
9F2B: FF                              ;
9F2C: FF                              ;
9F2D: FF                              ;
9F2E: FF                              ;
9F2F: FF                              ;
9F30: FF                              ;
9F31: FF                              ;
9F32: FF                              ;
9F33: FF                              ;
9F34: FF                              ;
9F35: FF                              ;
9F36: FF                              ;
9F37: FF                              ;
9F38: FF                              ;
9F39: FF                              ;
9F3A: FF                              ;
9F3B: FF                              ;
9F3C: FF                              ;
9F3D: FF                              ;
9F3E: FF                              ;
9F3F: FF                              ;
9F40: FF                              ;
9F41: FF                              ;
9F42: FF                              ;
9F43: FF                              ;
9F44: FF                              ;
9F45: FF                              ;
9F46: FF                              ;
9F47: FF                              ;
9F48: FF                              ;
9F49: FF                              ;
9F4A: FF                              ;
9F4B: FF                              ;
9F4C: FF                              ;
9F4D: FF                              ;
9F4E: FF                              ;
9F4F: FF                              ;
9F50: FF                              ;
9F51: FF                              ;
9F52: FF                              ;
9F53: FF                              ;
9F54: FF                              ;
9F55: FF                              ;
9F56: FF                              ;
9F57: FF                              ;
9F58: FF                              ;
9F59: FF                              ;
9F5A: FF                              ;
9F5B: FF                              ;
9F5C: FF                              ;
9F5D: FF                              ;
9F5E: FF                              ;
9F5F: FF                              ;
9F60: FF                              ;
9F61: FF                              ;
9F62: FF                              ;
9F63: FF                              ;
9F64: FF                              ;
9F65: FF                              ;
9F66: FF                              ;
9F67: FF                              ;
9F68: FF                              ;
9F69: FF                              ;
9F6A: FF                              ;
9F6B: FF                              ;
9F6C: FF                              ;
9F6D: FF                              ;
9F6E: FF                              ;
9F6F: FF                              ;
9F70: FF                              ;
9F71: FF                              ;
9F72: FF                              ;
9F73: FF                              ;
9F74: FF                              ;
9F75: FF                              ;
9F76: FF                              ;
9F77: FF                              ;
9F78: FF                              ;
9F79: FF                              ;
9F7A: FF                              ;
9F7B: FF                              ;
9F7C: FF                              ;
9F7D: FF                              ;
9F7E: FF                              ;
9F7F: FF                              ;
9F80: FF                              ;
9F81: FF                              ;
9F82: FF                              ;
9F83: FF                              ;
9F84: FF                              ;
9F85: FF                              ;
9F86: FF                              ;
9F87: FF                              ;
9F88: FF                              ;
9F89: FF                              ;
9F8A: FF                              ;
9F8B: FF                              ;
9F8C: FF                              ;
9F8D: FF                              ;
9F8E: FF                              ;
9F8F: FF                              ;
9F90: FF                              ;
9F91: FF                              ;
9F92: FF                              ;
9F93: FF                              ;
9F94: FF                              ;
9F95: FF                              ;
9F96: FF                              ;
9F97: FF                              ;
9F98: FF                              ;
9F99: FF                              ;
9F9A: FF                              ;
9F9B: FF                              ;
9F9C: FF                              ;
9F9D: FF                              ;
9F9E: FF                              ;
9F9F: FF                              ;
9FA0: FF                              ;
9FA1: FF                              ;
9FA2: FF                              ;
9FA3: FF                              ;
9FA4: FF                              ;
9FA5: FF                              ;
9FA6: FF                              ;
9FA7: FF                              ;
9FA8: FF                              ;
9FA9: FF                              ;
9FAA: FF                              ;
9FAB: FF                              ;
9FAC: FF                              ;
9FAD: FF                              ;
9FAE: FF                              ;
9FAF: FF                              ;
9FB0: FF                              ;
9FB1: FF                              ;
9FB2: FF                              ;
9FB3: FF                              ;
9FB4: FF                              ;
9FB5: FF                              ;
9FB6: FF                              ;
9FB7: FF                              ;
9FB8: FF                              ;
9FB9: FF                              ;
9FBA: FF                              ;
9FBB: FF                              ;
9FBC: FF                              ;
9FBD: FF                              ;
9FBE: FF                              ;
9FBF: FF                              ;
9FC0: FF                              ;
9FC1: FF                              ;
9FC2: FF                              ;
9FC3: FF                              ;
9FC4: FF                              ;
9FC5: FF                              ;
9FC6: FF                              ;
9FC7: FF                              ;
9FC8: FF                              ;
9FC9: FF                              ;
9FCA: FF                              ;
9FCB: FF                              ;
9FCC: FF                              ;
9FCD: FF                              ;
9FCE: FF                              ;
9FCF: FF                              ;
9FD0: FF                              ;
9FD1: FF                              ;
9FD2: FF                              ;
9FD3: FF                              ;
9FD4: FF                              ;
9FD5: FF                              ;
9FD6: FF                              ;
9FD7: FF                              ;
9FD8: FF                              ;
9FD9: FF                              ;
9FDA: FF                              ;
9FDB: FF                              ;
9FDC: FF                              ;
9FDD: FF                              ;
9FDE: FF                              ;
9FDF: FF                              ;
9FE0: FF                              ;
9FE1: FF                              ;
9FE2: FF                              ;
9FE3: FF                              ;
9FE4: FF                              ;
9FE5: FF                              ;
9FE6: FF                              ;
9FE7: FF                              ;
9FE8: FF                              ;
9FE9: FF                              ;
9FEA: FF                              ;
9FEB: FF                              ;
9FEC: FF                              ;
9FED: FF                              ;
9FEE: FF                              ;
9FEF: FF                              ;
9FF0: FF                              ;
9FF1: FF                              ;
9FF2: FF                              ;
9FF3: FF                              ;
9FF4: FF                              ;
9FF5: FF                              ;
9FF6: FF                              ;
9FF7: FF                              ;
9FF8: FF                              ;
9FF9: FF                              ;
9FFA: FF                              ;
9FFB: FF                              ;
9FFC: FF                              ;
9FFD: FF                              ;
9FFE: FF                              ;
9FFF: FF                              ;


A000: 02                              ;
A001: 03                              ;
A002: FE A3 B4        INC     $B4A3,X             ; {}
A005: A2 14           LDX     #$14                ; 
A007: 68              PLA                         ; 
A008: 8E A2 96        STX     $96A2               ; {}
A00B: A2 1C           LDX     #$1C                ; 
A00D: 68              PLA                         ; 
A00E: D3                              ;
A00F: A2 69           LDX     #$69                ; 
A011: A8              TAY                         ; 
A012: F0 67           BEQ     $A07B               ; {}
A014: 00              BRK                         ; 
A015: A1 83           LDA     ($83,X)             ; {ram.0083}
A017: A1 7E           LDA     ($7E,X)             ; 
A019: 6B                              ;
A01A: 02                              ;
A01B: 03                              ;
A01C: 02                              ;
A01D: 03                              ;
A01E: 1D A2 45        ORA     $45A2,X             ; 
A021: A2 4D           LDX     #$4D                ; 
A023: A2 55           LDX     #$55                ; 
A025: A2 69           LDX     #$69                ; 
A027: A2 02           LDX     #$02                ; 
A029: 03                              ;
A02A: 26 A2           ROL     <$A2                ; {ram.00A2}
A02C: C8              INY                         ; 
A02D: A3                              ;
A02E: 1C                              ;
A02F: 68              PLA                         ; 
A030: 16 A3           ASL     $A3,X               ; {ram.00A3}
A032: 23                              ;
A033: A3                              ;
A034: 37                              ;
A035: A3                              ;
A036: 02                              ;
A037: A2 48           LDX     #$48                ; 
A039: A3                              ;
A03A: 50 A3           BVC     $9FDF               ; {}
A03C: 60              RTS                         ; 
A03D: A3                              ;
A03E: 5D A2 78        EOR     $78A2,X             ; 
A041: A3                              ;
A042: 9C                              ;
A043: A3                              ;
A044: CD 6B D0        CMP     $D06B               ; 
A047: A3                              ;
A048: B0 A3           BCS     $9FED               ; {}
A04A: B9 A3 BE        LDA     $BEA3,Y             ; {}
A04D: A3                              ;
A04E: C3                              ;
A04F: A3                              ;
A050: 2F                              ;
A051: A2 47           LDX     #$47                ; 
A053: 68              PLA                         ; 
A054: 4F                              ;
A055: 68              PLA                         ; 
A056: 59 68 65        EOR     $6568,Y             ; 
A059: 68              PLA                         ; 
A05A: 35 A2           AND     $A2,X               ; {ram.00A2}
A05C: 73                              ;
A05D: 68              PLA                         ; 
A05E: E8              INX                         ; 
A05F: A3                              ;
A060: F4                              ;
A061: A3                              ;
A062: F9 A3 02        SBC     $02A3,Y             ; {ram.02A3}
A065: 03                              ;
A066: 02                              ;
A067: 03                              ;
A068: 02                              ;
A069: 03                              ;
A06A: 0A              ASL     A                   ; 
A06B: A2 9E           LDX     #$9E                ; 
A06D: A2 02           LDX     #$02                ; 
A06F: 03                              ;
A070: 02                              ;
A071: 03                              ;
A072: 02                              ;
A073: 03                              ;
A074: 02                              ;
A075: 03                              ;
A076: A6 A2           LDX     <$A2                ; {ram.00A2}
A078: 72                              ;
A079: A2 7E           LDX     #$7E                ; 
A07B: A2 86           LDX     #$86                ; 
A07D: A2 02           LDX     #$02                ; 
A07F: 03                              ;

A080: A6 14           LDX     <$14                ; {ram.0014}
A082: BD 00 A0        LDA     $A000,X             ; {}
A085: 85 00           STA     <$00                ; {ram.GP_00}
A087: BD 01 A0        LDA     $A001,X             ; {}
A08A: 85 01           STA     <$01                ; {ram.GP_01}
A08C: 20 F6 A0        JSR     $A0F6               ; {}
A08F: A9 3F           LDA     #$3F                ; 
A091: 8D 00 03        STA     $0300               ; {ram.0300}
A094: A2 00           LDX     #$00                ; 
A096: 86 14           STX     <$14                ; {ram.0014}
A098: 86 5C           STX     <$5C                ; {ram.!FlipFlag} Don't let NMI flip name tables
A09A: 8E 01 03        STX     $0301               ; {ram.0301}
A09D: CA              DEX                         ; 
A09E: 8E 02 03        STX     $0302               ; {ram.0302}
A0A1: 60              RTS                         ; 

A0A2: 48              PHA                         ; 
A0A3: 8D 06 20        STA     $2006               ; {hard.P_VRAM_ADDR} [NES] VRAM address select
A0A6: C8              INY                         ; 
A0A7: B1 00           LDA     ($00),Y             ; {ram.GP_00}
A0A9: 8D 06 20        STA     $2006               ; {hard.P_VRAM_ADDR} [NES] VRAM address select
A0AC: C8              INY                         ; 
A0AD: B1 00           LDA     ($00),Y             ; {ram.GP_00}
A0AF: 0A              ASL     A                   ; 
A0B0: 48              PHA                         ; 
A0B1: A5 FF           LDA     <$FF                ; {ram.CUR_2000} Current value of 2000 (PPUCTRL)
A0B3: 09 04           ORA     #$04                ; Increment VRAM by 32 (down)
A0B5: B0 02           BCS     $A0B9               ; {}
A0B7: 29 FB           AND     #$FB                ; Increment VRAM by 1 (across)
A0B9: 8D 00 20        STA     $2000               ; {hard.P_CNTRL_1} Set new VRAM increment ...
A0BC: 85 FF           STA     <$FF                ; {ram.CUR_2000} ... and set cached value
A0BE: 68              PLA                         ; 
A0BF: 0A              ASL     A                   ; 
A0C0: 08              PHP                         ; 
A0C1: 90 03           BCC     $A0C6               ; {}
A0C3: 09 02           ORA     #$02                ; 
A0C5: C8              INY                         ; 
A0C6: 28              PLP                         ; 
A0C7: 18              CLC                         ; 
A0C8: D0 01           BNE     $A0CB               ; {}
A0CA: 38              SEC                         ; 
A0CB: 6A              ROR     A                   ; 
A0CC: 4A              LSR     A                   ; 
A0CD: AA              TAX                         ; 
A0CE: B0 01           BCS     $A0D1               ; {}
A0D0: C8              INY                         ; 
A0D1: B1 00           LDA     ($00),Y             ; {ram.GP_00}
A0D3: 8D 07 20        STA     $2007               ; {hard.P_VRAM_DATA} [NES] VRAM data
A0D6: CA              DEX                         ; 
A0D7: D0 F5           BNE     $A0CE               ; {}
A0D9: 68              PLA                         ; 
A0DA: C9 3F           CMP     #$3F                ; 
A0DC: D0 0C           BNE     $A0EA               ; {}
A0DE: 8D 06 20        STA     $2006               ; {hard.P_VRAM_ADDR} [NES] VRAM address select
A0E1: 8E 06 20        STX     $2006               ; {hard.P_VRAM_ADDR} [NES] VRAM address select
A0E4: 8E 06 20        STX     $2006               ; {hard.P_VRAM_ADDR} [NES] VRAM address select
A0E7: 8E 06 20        STX     $2006               ; {hard.P_VRAM_ADDR} [NES] VRAM address select
A0EA: 38              SEC                         ; 
A0EB: 98              TYA                         ; 
A0EC: 65 00           ADC     <$00                ; {ram.GP_00}
A0EE: 85 00           STA     <$00                ; {ram.GP_00}
A0F0: A9 00           LDA     #$00                ; 
A0F2: 65 01           ADC     <$01                ; {ram.GP_01}
A0F4: 85 01           STA     <$01                ; {ram.GP_01}

A0F6: AE 02 20        LDX     $2002               ; {hard.P_STATUS} [NES] PPU status
A0F9: A0 00           LDY     #$00                ; 
A0FB: B1 00           LDA     ($00),Y             ; {ram.GP_00}
A0FD: 10 A3           BPL     $A0A2               ; {}
A0FF: 60              RTS                         ; 

A100: 23                              ;
A101: C0 7F           CPY     #$7F                ; 
A103: 00              BRK                         ; 
A104: 23                              ;
A105: D4                              ;
A106: 03                              ;
A107: 40              RTI                         ; 
A108: 50 50           BVC     $A15A               ; {}
A10A: 23                              ;
A10B: DC                              ;
A10C: 03                              ;
A10D: 44                              ;
A10E: 55 55           EOR     $55,X               ; {ram.0055}
A110: 23                              ;
A111: E4 03           CPX     <$03                ; {ram.GP_03}
A113: 44                              ;
A114: 55 55           EOR     $55,X               ; {ram.0055}
A116: 20 A8 0F        JSR     $0FA8               ; 
A119: 62                              ;
A11A: 24 1C           BIT     <$1C                ; {ram.001C}
A11C: 24 0E           BIT     <$0E                ; {ram.000E}
A11E: 24 15           BIT     <$15                ; {ram.0015}
A120: 24 0E           BIT     <$0E                ; {ram.000E}
A122: 24 0C           BIT     <$0C                ; {ram.000C}
A124: 24 1D           BIT     <$1D                ; {ram.001D}
A126: 24 62           BIT     <$62                ; {ram.0062}
A128: 21 03           AND     ($03,X)             ; {ram.GP_03}
A12A: 01 69           ORA     ($69,X)             ; {ram.0069}
A12C: 21 04           AND     ($04,X)             ; {ram.0004}
A12E: 58              CLI                         ; 
A12F: 6A              ROR     A                   ; 
A130: 21 1C           AND     ($1C,X)             ; {ram.001C}
A132: 01 6B           ORA     ($6B,X)             ; {ram.SND_Sq2Fine}
A134: 21 23           AND     ($23,X)             ; {ram.0023}
A136: D0 6C           BNE     $A1A4               ; {}
A138: 21 3C           AND     ($3C,X)             ; {ram.003C}
A13A: D0 6C           BNE     $A1A8               ; {}
A13C: 23                              ;
A13D: 23                              ;
A13E: 01 6E           ORA     ($6E,X)             ; {ram.SND_MusEffRel}
A140: 23                              ;
A141: 24 58           BIT     <$58                ; {ram.0058}
A143: 6A              ROR     A                   ; 
A144: 23                              ;
A145: 3C                              ;
A146: 01 6D           ORA     ($6D,X)             ; {ram.SND_MusEffBell}
A148: 21 0A           AND     ($0A,X)             ; {ram.000A}
A14A: 06 24           ASL     <$24                ; {ram.0024}
A14C: 17                              ;
A14D: 0A              ASL     A                   ; 
A14E: 16 0E           ASL     $0E,X               ; {ram.000E}
A150: 24 21           BIT     <$21                ; {ram.0021}
A152: 13                              ;
A153: 06 24           ASL     <$24                ; {ram.0024}
A155: 15 12           ORA     $12,X               ; {ram.0012}
A157: 0F                              ;
A158: 0E 24 22        ASL     $2224               ; 
A15B: A6 12           LDX     <$12                ; {ram.0012}
A15D: 1B                              ;
A15E: 0E 10 12        ASL     $1210               ; 
A161: 1C                              ;
A162: 1D 0E 1B        ORA     $1B0E,X             ; 
A165: 24 22           BIT     <$22                ; {ram.0022}
A167: 18              CLC                         ; 
A168: 1E 1B 24        ASL     $241B,X             ; 
A16B: 17                              ;
A16C: 0A              ASL     A                   ; 
A16D: 16 0E           ASL     $0E,X               ; {ram.000E}
A16F: 22                              ;
A170: E6 10           INC     <$10                ; {ram.0010}
A172: 0E 15 12        ASL     $1215               ; 
A175: 16 12           ASL     $12,X               ; {ram.0012}
A177: 17                              ;
A178: 0A              ASL     A                   ; 
A179: 1D 12 18        ORA     $1812,X             ; 
A17C: 17                              ;
A17D: 24 16           BIT     <$16                ; {ram.0016}
A17F: 18              CLC                         ; 
A180: 0D 0E FF        ORA     $FF0E               ; 
A183: 22                              ;
A184: 05 01           ORA     <$01                ; {ram.GP_01}
A186: 69 22           ADC     #$22                ; 
A188: 06 55           ASL     <$55                ; {ram.0055}
A18A: 6A              ROR     A                   ; 
A18B: 22                              ;
A18C: 1B                              ;
A18D: 01 6B           ORA     ($6B,X)             ; {ram.SND_Sq2Fine}
A18F: 22                              ;
A190: 25 C7           AND     <$C7                ; {ram.00C7}
A192: 6C 22 3B        JMP     ($3B22)             ; 
A195: C7                              ;
A196: 6C 23 05        JMP     ($0523)             ; {ram.0523}
A199: 01 6E           ORA     ($6E,X)             ; {ram.SND_MusEffRel}
A19B: 23                              ;
A19C: 06 55           ASL     <$55                ; {ram.0055}
A19E: 6A              ROR     A                   ; 
A19F: 23                              ;
A1A0: 1B                              ;
A1A1: 01 6D           ORA     ($6D,X)             ; {ram.SND_MusEffBell}
A1A3: 22                              ;
A1A4: 26 15           ROL     <$15                ; {ram.0015}
A1A6: 0A              ASL     A                   ; 
A1A7: 24 0B           BIT     <$0B                ; {ram.000B}
A1A9: 24 0C           BIT     <$0C                ; {ram.000C}
A1AB: 24 0D           BIT     <$0D                ; {ram.000D}
A1AD: 24 0E           BIT     <$0E                ; {ram.000E}
A1AF: 24 0F           BIT     <$0F                ; {ram.000F}
A1B1: 24 10           BIT     <$10                ; {ram.0010}
A1B3: 24 11           BIT     <$11                ; {ram.0011}
A1B5: 24 12           BIT     <$12                ; {ram.0012}
A1B7: 24 13           BIT     <$13                ; {ram.0013}
A1B9: 24 14           BIT     <$14                ; {ram.0014}
A1BB: 22                              ;
A1BC: 66 15           ROR     <$15                ; {ram.0015}
A1BE: 15 24           ORA     $24,X               ; {ram.0024}
A1C0: 16 24           ASL     $24,X               ; {ram.0024}
A1C2: 17                              ;
A1C3: 24 18           BIT     <$18                ; {ram.0018}
A1C5: 24 19           BIT     <$19                ; {ram.0019}
A1C7: 24 1A           BIT     <$1A                ; {ram.001A}
A1C9: 24 1B           BIT     <$1B                ; {ram.001B}
A1CB: 24 1C           BIT     <$1C                ; {ram.001C}
A1CD: 24 1D           BIT     <$1D                ; {ram.001D}
A1CF: 24 1E           BIT     <$1E                ; {ram.001E}
A1D1: 24 1F           BIT     <$1F                ; {ram.001F}
A1D3: 22                              ;
A1D4: A6 15           LDX     <$15                ; {ram.0015}
A1D6: 20 24 21        JSR     $2124               ; 
A1D9: 24 22           BIT     <$22                ; {ram.0022}
A1DB: 24 23           BIT     <$23                ; {ram.0023}
A1DD: 24 62           BIT     <$62                ; {ram.0062}
A1DF: 24 63           BIT     <$63                ; {ram.0063}
A1E1: 24 28           BIT     <$28                ; {ram.0028}
A1E3: 24 29           BIT     <$29                ; {ram.0029}
A1E5: 24 2A           BIT     <$2A                ; {ram.002A}
A1E7: 24 2B           BIT     <$2B                ; {ram.002B}
A1E9: 24 2C           BIT     <$2C                ; {ram.002C}
A1EB: 22                              ;
A1EC: E6 13           INC     <$13                ; {ram.0013}
A1EE: 00              BRK                         ; 
A1EF: 24 01           BIT     <$01                ; {ram.GP_01}
A1F1: 24 02           BIT     <$02                ; {ram.GP_02}
A1F3: 24 03           BIT     <$03                ; {ram.GP_03}
A1F5: 24 04           BIT     <$04                ; {ram.0004}
A1F7: 24 05           BIT     <$05                ; {ram.0005}
A1F9: 24 06           BIT     <$06                ; {ram.0006}
A1FB: 24 07           BIT     <$07                ; {ram.0007}
A1FD: 24 08           BIT     <$08                ; {ram.0008}
A1FF: 24 09           BIT     <$09                ; {ram.0009}
A201: FF                              ;
A202: 3F                              ;
A203: 1C                              ;
A204: 04                              ;
A205: 0F                              ;
A206: 16 2C           ASL     $2C,X               ; {ram.002C}
A208: 3C                              ;
A209: FF                              ;
A20A: 3F                              ;
A20B: 08              PHP                         ; 
A20C: 08              PHP                         ; 
A20D: 0F                              ;
A20E: 22                              ;
A20F: 10 00           BPL     $A211               ; {}
A211: 0F                              ;
A212: 2A              ROL     A                   ; 
A213: 10 00           BPL     $A215               ; {}
A215: 3F                              ;
A216: 1C                              ;
A217: 04                              ;
A218: 0F                              ;
A219: 27                              ;
A21A: 06 16           ASL     <$16                ; {ram.0016}
A21C: FF                              ;
A21D: 21 A4           AND     ($A4,X)             ; {ram.00A4}
A21F: 58              CLI                         ; 
A220: 24 21           BIT     <$21                ; {ram.0021}
A222: C4 58           CPY     <$58                ; {ram.0058}
A224: 24 FF           BIT     <$FF                ; {ram.CUR_2000}
A226: 21 E4           AND     ($E4,X)             ; {ram.00E4}
A228: 58              CLI                         ; 
A229: 24 22           BIT     <$22                ; {ram.0022}
A22B: C8              INY                         ; 
A22C: 4D 24 FF        EOR     $FF24               ; 
A22F: 2A              ROL     A                   ; 
A230: CF                              ;
A231: 02                              ;
A232: ED EE FF        SBC     $FFEE               ; 
A235: 2B                              ;
A236: 6A              ROR     A                   ; 
A237: 0C                              ;
A238: EB                              ;
A239: EF                              ;
A23A: F1 F1           SBC     ($F1),Y             ; 
A23C: F1 F1           SBC     ($F1),Y             ; 
A23E: F1 F1           SBC     ($F1),Y             ; 
A240: F1 F1           SBC     ($F1),Y             ; 
A242: F0 EC           BEQ     $A230               ; {}
A244: FF                              ;
A245: 3F                              ;
A246: 1C                              ;
A247: 04                              ;
A248: 0F                              ;
A249: 30 00           BMI     $A24B               ; {}
A24B: 12                              ;
A24C: FF                              ;
A24D: 3F                              ;
A24E: 1C                              ;
A24F: 04                              ;
A250: 0F                              ;
A251: 1A                              ;
A252: 37                              ;
A253: 12                              ;
A254: FF                              ;
A255: 3F                              ;
A256: 1C                              ;
A257: 04                              ;
A258: 0F                              ;
A259: 17                              ;
A25A: 37                              ;
A25B: 12                              ;
A25C: FF                              ;
A25D: 3F                              ;
A25E: 08              PHP                         ; 
A25F: 08              PHP                         ; 
A260: 0F                              ;
A261: 30 00           BMI     $A263               ; {}
A263: 12                              ;
A264: 0F                              ;
A265: 07                              ;
A266: 0F                              ;
A267: 17                              ;
A268: FF                              ;
A269: 23                              ;
A26A: D0 60           BNE     $A2CC               ; {}
A26C: AA              TAX                         ; 
A26D: 23                              ;
A26E: F0 50           BEQ     $A2C0               ; {}
A270: AA              TAX                         ; 
A271: FF                              ;
A272: 3F                              ;
A273: 08              PHP                         ; 
A274: 08              PHP                         ; 
A275: 0F                              ;
A276: 30 30           BMI     $A2A8               ; {}
A278: 30 0F           BMI     $A289               ; {}
A27A: 30 30           BMI     $A2AC               ; {}
A27C: 30 FF           BMI     $A27D               ; {}
A27E: 3F                              ;
A27F: 1C                              ;
A280: 04                              ;
A281: 0F                              ;
A282: 0F                              ;
A283: 1C                              ;
A284: 16 FF           ASL     $FF,X               ; {ram.CUR_2000}
A286: 3F                              ;
A287: 1C                              ;
A288: 04                              ;
A289: 0F                              ;
A28A: 2A              ROL     A                   ; 
A28B: 1A                              ;
A28C: 0C                              ;
A28D: FF                              ;
A28E: 3F                              ;
A28F: 1C                              ;
A290: 04                              ;
A291: 0F                              ;
A292: 0A              ASL     A                   ; 
A293: 29 30           AND     #$30                ; 
A295: FF                              ;
A296: 3F                              ;
A297: 1C                              ;
A298: 04                              ;
A299: 0F                              ;
A29A: 17                              ;
A29B: 27                              ;
A29C: 30 FF           BMI     $A29D               ; {}
A29E: 22                              ;
A29F: CD 04 62        CMP     $6204               ; {ram.6204}
A2A2: 01 00           ORA     ($00,X)             ; {ram.GP_00}
A2A4: 00              BRK                         ; 
A2A5: FF                              ;
A2A6: 22                              ;
A2A7: CB                              ;
A2A8: 0A              ASL     A                   ; 
A2A9: 62                              ;
A2AA: 01 24           ORA     ($24,X)             ; {ram.0024}
A2AC: 24 24           BIT     <$24                ; {ram.0024}
A2AE: 24 24           BIT     <$24                ; {ram.0024}
A2B0: 62                              ;
A2B1: 05 00           ORA     <$00                ; {ram.GP_00}
A2B3: FF                              ;
A2B4: 23                              ;
A2B5: C0 7F           CPY     #$7F                ; 
A2B7: 00              BRK                         ; 
A2B8: 21 4A           AND     ($4A,X)             ; {ram.004A}
A2BA: 08              PHP                         ; 
A2BB: 0C                              ;
A2BC: 18              CLC                         ; 
A2BD: 17                              ;
A2BE: 1D 12 17        ORA     $1712,X             ; 
A2C1: 1E 0E 21        ASL     $210E,X             ; 
A2C4: AA              TAX                         ; 
A2C5: 04                              ;
A2C6: 1C                              ;
A2C7: 0A              ASL     A                   ; 
A2C8: 1F                              ;
A2C9: 0E 22 0A        ASL     $0A22               ; 
A2CC: 05 1B           ORA     <$1B                ; {ram.001B}
A2CE: 0E 1D 1B        ASL     $1B1D               ; 
A2D1: 22                              ;
A2D2: FF                              ;
A2D3: 23                              ;
A2D4: C2                              ;
A2D5: 0E 40 00        ASL     $0040               ; {ram.0040}
A2D8: 00              BRK                         ; 
A2D9: 44                              ;
A2DA: 55 55           EOR     $55,X               ; {ram.0055}
A2DC: 00              BRK                         ; 
A2DD: 00              BRK                         ; 
A2DE: 04                              ;
A2DF: 00              BRK                         ; 
A2E0: 00              BRK                         ; 
A2E1: 44                              ;
A2E2: 55 55           EOR     $55,X               ; {ram.0055}
A2E4: 20 6F 0E        JSR     $0E6F               ; 
A2E7: 69 0B           ADC     #$0B                ; 
A2E9: 6B                              ;
A2EA: 69 0A           ADC     #$0A                ; 
A2EC: 6B                              ;
A2ED: 24 24           BIT     <$24                ; {ram.0024}
A2EF: 62                              ;
A2F0: 15 12           ORA     $12,X               ; {ram.0012}
A2F2: 0F                              ;
A2F3: 0E 62 20        ASL     $2062               ; 
A2F6: CF                              ;
A2F7: 06 6E           ASL     <$6E                ; {ram.SND_MusEffRel}
A2F9: 6A              ROR     A                   ; 
A2FA: 6D 6E 6A        ADC     $6A6E               ; {ram.6A6E}
A2FD: 6D 20 8F        ADC     $8F20               ; {}
A300: C2                              ;
A301: 6C 20 91        JMP     ($9120)             ; {}
A304: C2                              ;
A305: 6C 20 92        JMP     ($9220)             ; {}
A308: C2                              ;
A309: 6C 20 94        JMP     ($9420)             ; {}
A30C: C2                              ;
A30D: 6C 20 6B        JMP     ($6B20)             ; {ram.6B20}
A310: 84 F7           STY     <$F7                ; {ram.00F7}
A312: 24 F9           BIT     <$F9                ; {ram.00F9}
A314: 61 FF           ADC     ($FF,X)             ; {ram.CUR_2000}
A316: 29 84           AND     #$84                ; 
A318: 09 12           ORA     #$12                ; 
A31A: 17                              ;
A31B: 1F                              ;
A31C: 0E 17 1D        ASL     $1D17               ; 
A31F: 18              CLC                         ; 
A320: 1B                              ;
A321: 22                              ;
A322: FF                              ;
A323: 29 C7           AND     #$C7                ; 
A325: 04                              ;
A326: 69 6A           ADC     #$6A                ; 
A328: 6A              ROR     A                   ; 
A329: 6B                              ;
A32A: 29 CF           AND     #$CF                ; 
A32C: 01 69           ORA     ($69,X)             ; {ram.0069}
A32E: 29 D0           AND     #$D0                ; 
A330: 4B                              ;
A331: 6A              ROR     A                   ; 
A332: 29 DB           AND     #$DB                ; 
A334: 01 6B           ORA     ($6B,X)             ; {ram.SND_Sq2Fine}
A336: FF                              ;
A337: 29 E7           AND     #$E7                ; 
A339: C2                              ;
A33A: 6C 29 EA        JMP     ($EA29)             ; 
A33D: C2                              ;
A33E: 6C 29 EF        JMP     ($EF29)             ; 
A341: C4 6C           CPY     <$6C                ; {ram.006C}
A343: 29 FB           AND     #$FB                ; 
A345: C4 6C           CPY     <$6C                ; {ram.006C}
A347: FF                              ;
A348: 2A              ROL     A                   ; 
A349: 27                              ;
A34A: 04                              ;
A34B: 6E 6A 6A        ROR     $6A6A               ; {ram.6A6A}
A34E: 6D FF 2A        ADC     $2AFF               ; 
A351: 42                              ;
A352: 0C                              ;
A353: 1E 1C 0E        ASL     $0E1C,X             ; 
A356: 24 0B           BIT     <$0B                ; {ram.000B}
A358: 24 0B           BIT     <$0B                ; {ram.000B}
A35A: 1E 1D 1D        ASL     $1D1D,X             ; 
A35D: 18              CLC                         ; 
A35E: 17                              ;
A35F: FF                              ;
A360: 2A              ROL     A                   ; 
A361: 64                              ;
A362: 08              PHP                         ; 
A363: 0F                              ;
A364: 18              CLC                         ; 
A365: 1B                              ;
A366: 24 1D           BIT     <$1D                ; {ram.001D}
A368: 11 12           ORA     ($12),Y             ; {ram.0012}
A36A: 1C                              ;
A36B: 2A              ROL     A                   ; 
A36C: 6F                              ;
A36D: 01 6E           ORA     ($6E,X)             ; {ram.SND_MusEffRel}
A36F: 2A              ROL     A                   ; 
A370: 70 4B           BVS     $A3BD               ; {}
A372: 6A              ROR     A                   ; 
A373: 2A              ROL     A                   ; 
A374: 7B                              ;
A375: 01 6D           ORA     ($6D,X)             ; {ram.SND_MusEffBell}
A377: FF                              ;
A378: 2B                              ;
A379: 43                              ;
A37A: 07                              ;
A37B: 0C                              ;
A37C: 18              CLC                         ; 
A37D: 16 19           ASL     $19,X               ; {ram.0019}
A37F: 0A              ASL     A                   ; 
A380: 1C                              ;
A381: 1C                              ;
A382: 2A              ROL     A                   ; 
A383: A5 03           LDA     <$03                ; {ram.GP_03}
A385: 16 0A           ASL     $0A,X               ; {ram.000A}
A387: 19 2A 8C        ORA     $8C2A,Y             ; {}
A38A: 10 F5           BPL     $A381               ; {}
A38C: F5 FD           SBC     $FD,X               ; {ram.CUR_HScroll}
A38E: F5 F5           SBC     $F5,X               ; {ram.TileFlagA}
A390: FD F5 F5        SBC     $F5F5,X             ; 
A393: FD F5 F5        SBC     $F5F5,X             ; 
A396: F5 FD           SBC     $FD,X               ; {ram.CUR_HScroll}
A398: F5 F5           SBC     $F5,X               ; {ram.TileFlagA}
A39A: F5 FF           SBC     $FF,X               ; {ram.CUR_2000}
A39C: 2B                              ;
A39D: AC 10 F5        LDY     $F510               ; 
A3A0: FE F5 F5        INC     $F5F5,X             ; 
A3A3: F5 FE           SBC     $FE,X               ; {ram.CUR_2001}
A3A5: F5 F5           SBC     $F5,X               ; {ram.TileFlagA}
A3A7: F5 F5           SBC     $F5,X               ; {ram.TileFlagA}
A3A9: FE F5 F5        INC     $F5F5,X             ; 
A3AC: F5 FE           SBC     $FE,X               ; {ram.CUR_2001}
A3AE: F5 FF           SBC     $FF,X               ; {ram.CUR_2000}
A3B0: 2B                              ;
A3B1: D9 43 05        CMP     $0543,Y             ; 
A3B4: 2B                              ;
A3B5: DC                              ;
A3B6: 4B                              ;
A3B7: 00              BRK                         ; 
A3B8: FF                              ;
A3B9: 2B                              ;
A3BA: E9 56           SBC     #$56                ; 
A3BC: 55 FF           EOR     $FF,X               ; {ram.CUR_2000}
A3BE: 2B                              ;
A3BF: A0 60           LDY     #$60                ; 
A3C1: 24 FF           BIT     <$FF                ; {ram.CUR_2000}
A3C3: 28              PLP                         ; 
A3C4: E0 60           CPX     #$60                ; 
A3C6: 24 FF           BIT     <$FF                ; {ram.CUR_2000}
A3C8: 3F                              ;
A3C9: 10 04           BPL     $A3CF               ; {}
A3CB: 0F                              ;
A3CC: 10 30           BPL     $A3FE               ; {}
A3CE: 00              BRK                         ; 
A3CF: FF                              ;
A3D0: 23                              ;
A3D1: E3                              ;
A3D2: 03                              ;
A3D3: 0F                              ;
A3D4: 0F                              ;
A3D5: CF                              ;
A3D6: 22                              ;
A3D7: 4C 0A 10        JMP     $100A               ; 
A3DA: 0A              ASL     A                   ; 
A3DB: 16 0E           ASL     $0E,X               ; {ram.000E}
A3DD: 24 18           BIT     <$18                ; {ram.0018}
A3DF: 1F                              ;
A3E0: 0E 1B 24        ASL     $241B               ; 
A3E3: 22                              ;
A3E4: 6C 4A 24        JMP     ($244A)             ; 
A3E7: FF                              ;
A3E8: 3F                              ;
A3E9: 08              PHP                         ; 
A3EA: 08              PHP                         ; 
A3EB: 0F                              ;
A3EC: 17                              ;
A3ED: 16 26           ASL     $26,X               ; {ram.0026}
A3EF: 0F                              ;
A3F0: 17                              ;
A3F1: 16 26           ASL     $26,X               ; {ram.0026}
A3F3: FF                              ;
A3F4: 23                              ;
A3F5: D0 58           BNE     $A44F               ; {}
A3F7: FF                              ;
A3F8: FF                              ;
A3F9: 23                              ;
A3FA: E8              INX                         ; 
A3FB: 58              CLI                         ; 
A3FC: FF                              ;
A3FD: FF                              ;
A3FE: 20 00 20        JSR     $2000               ; {hard.P_CNTRL_1} [NES] PPU setup #1
A401: 24 24           BIT     <$24                ; {ram.0024}
A403: 24 24           BIT     <$24                ; {ram.0024}
A405: 24 24           BIT     <$24                ; {ram.0024}
A407: 24 24           BIT     <$24                ; {ram.0024}
A409: 24 24           BIT     <$24                ; {ram.0024}
A40B: 24 24           BIT     <$24                ; {ram.0024}
A40D: 24 24           BIT     <$24                ; {ram.0024}
A40F: 24 24           BIT     <$24                ; {ram.0024}
A411: 24 24           BIT     <$24                ; {ram.0024}
A413: 24 24           BIT     <$24                ; {ram.0024}
A415: 24 24           BIT     <$24                ; {ram.0024}
A417: 24 24           BIT     <$24                ; {ram.0024}
A419: 24 24           BIT     <$24                ; {ram.0024}
A41B: 24 24           BIT     <$24                ; {ram.0024}
A41D: 24 24           BIT     <$24                ; {ram.0024}
A41F: 24 24           BIT     <$24                ; {ram.0024}
A421: 20 20 20        JSR     $2020               ; 
A424: 24 24           BIT     <$24                ; {ram.0024}
A426: 24 24           BIT     <$24                ; {ram.0024}
A428: 24 24           BIT     <$24                ; {ram.0024}
A42A: 24 24           BIT     <$24                ; {ram.0024}
A42C: 24 24           BIT     <$24                ; {ram.0024}
A42E: 24 24           BIT     <$24                ; {ram.0024}
A430: 24 24           BIT     <$24                ; {ram.0024}
A432: 24 24           BIT     <$24                ; {ram.0024}
A434: 24 24           BIT     <$24                ; {ram.0024}
A436: 24 24           BIT     <$24                ; {ram.0024}
A438: 24 24           BIT     <$24                ; {ram.0024}
A43A: 24 24           BIT     <$24                ; {ram.0024}
A43C: 24 24           BIT     <$24                ; {ram.0024}
A43E: 24 24           BIT     <$24                ; {ram.0024}
A440: 24 24           BIT     <$24                ; {ram.0024}
A442: 24 24           BIT     <$24                ; {ram.0024}
A444: 20 40 20        JSR     $2040               ; 
A447: 24 24           BIT     <$24                ; {ram.0024}
A449: 24 24           BIT     <$24                ; {ram.0024}
A44B: 24 24           BIT     <$24                ; {ram.0024}
A44D: 24 24           BIT     <$24                ; {ram.0024}
A44F: 24 24           BIT     <$24                ; {ram.0024}
A451: 24 24           BIT     <$24                ; {ram.0024}
A453: 24 24           BIT     <$24                ; {ram.0024}
A455: 24 24           BIT     <$24                ; {ram.0024}
A457: 24 24           BIT     <$24                ; {ram.0024}
A459: 24 24           BIT     <$24                ; {ram.0024}
A45B: 24 24           BIT     <$24                ; {ram.0024}
A45D: 24 24           BIT     <$24                ; {ram.0024}
A45F: 24 24           BIT     <$24                ; {ram.0024}
A461: 24 24           BIT     <$24                ; {ram.0024}
A463: 24 24           BIT     <$24                ; {ram.0024}
A465: 24 24           BIT     <$24                ; {ram.0024}
A467: 20 60 20        JSR     $2060               ; 
A46A: 24 24           BIT     <$24                ; {ram.0024}
A46C: 24 24           BIT     <$24                ; {ram.0024}
A46E: 24 24           BIT     <$24                ; {ram.0024}
A470: 24 24           BIT     <$24                ; {ram.0024}
A472: 24 24           BIT     <$24                ; {ram.0024}
A474: 24 24           BIT     <$24                ; {ram.0024}
A476: 24 24           BIT     <$24                ; {ram.0024}
A478: 24 24           BIT     <$24                ; {ram.0024}
A47A: 24 24           BIT     <$24                ; {ram.0024}
A47C: 24 24           BIT     <$24                ; {ram.0024}
A47E: 24 24           BIT     <$24                ; {ram.0024}
A480: 24 24           BIT     <$24                ; {ram.0024}
A482: 24 24           BIT     <$24                ; {ram.0024}
A484: 24 24           BIT     <$24                ; {ram.0024}
A486: 24 24           BIT     <$24                ; {ram.0024}
A488: 24 24           BIT     <$24                ; {ram.0024}
A48A: 20 80 20        JSR     $2080               ; 
A48D: 24 24           BIT     <$24                ; {ram.0024}
A48F: E6 E4           INC     <$E4                ; {ram.00E4}
A491: E5 24           SBC     <$24                ; {ram.0024}
A493: 1D 11 0E        ORA     $0E11,X             ; 
A496: 24 15           BIT     <$15                ; {ram.0015}
A498: 0E 10 0E        ASL     $0E10               ; 
A49B: 17                              ;
A49C: 0D 24 18        ORA     $1824               ; 
A49F: 0F                              ;
A4A0: 24 23           BIT     <$23                ; {ram.0023}
A4A2: 0E 15 0D        ASL     $0D15               ; 
A4A5: 0A              ASL     A                   ; 
A4A6: 24 E5           BIT     <$E5                ; {ram.00E5}
A4A8: E4 E5           CPX     <$E5                ; {ram.00E5}
A4AA: E6 24           INC     <$24                ; {ram.0024}
A4AC: 24 20           BIT     <$20                ; {ram.0020}
A4AE: A0 20           LDY     #$20                ; 
A4B0: 24 24           BIT     <$24                ; {ram.0024}
A4B2: E2                              ;
A4B3: 24 24           BIT     <$24                ; {ram.0024}
A4B5: 24 24           BIT     <$24                ; {ram.0024}
A4B7: 24 24           BIT     <$24                ; {ram.0024}
A4B9: 24 24           BIT     <$24                ; {ram.0024}
A4BB: 24 24           BIT     <$24                ; {ram.0024}
A4BD: 24 24           BIT     <$24                ; {ram.0024}
A4BF: 24 24           BIT     <$24                ; {ram.0024}
A4C1: 24 24           BIT     <$24                ; {ram.0024}
A4C3: 24 24           BIT     <$24                ; {ram.0024}
A4C5: 24 24           BIT     <$24                ; {ram.0024}
A4C7: 24 24           BIT     <$24                ; {ram.0024}
A4C9: 24 24           BIT     <$24                ; {ram.0024}
A4CB: 24 24           BIT     <$24                ; {ram.0024}
A4CD: E3                              ;
A4CE: 24 24           BIT     <$24                ; {ram.0024}
A4D0: 20 C0 20        JSR     $20C0               ; 
A4D3: 24 24           BIT     <$24                ; {ram.0024}
A4D5: E3                              ;
A4D6: 24 24           BIT     <$24                ; {ram.0024}
A4D8: 24 24           BIT     <$24                ; {ram.0024}
A4DA: 24 24           BIT     <$24                ; {ram.0024}
A4DC: 24 24           BIT     <$24                ; {ram.0024}
A4DE: 24 24           BIT     <$24                ; {ram.0024}
A4E0: 24 24           BIT     <$24                ; {ram.0024}
A4E2: 24 24           BIT     <$24                ; {ram.0024}
A4E4: 24 24           BIT     <$24                ; {ram.0024}
A4E6: 24 24           BIT     <$24                ; {ram.0024}
A4E8: 24 24           BIT     <$24                ; {ram.0024}
A4EA: 24 24           BIT     <$24                ; {ram.0024}
A4EC: 24 24           BIT     <$24                ; {ram.0024}
A4EE: 24 24           BIT     <$24                ; {ram.0024}
A4F0: E2                              ;
A4F1: 24 24           BIT     <$24                ; {ram.0024}
A4F3: 20 E0 20        JSR     $20E0               ; 
A4F6: 24 24           BIT     <$24                ; {ram.0024}
A4F8: E2                              ;
A4F9: 24 16           BIT     <$16                ; {ram.0016}
A4FB: 0A              ASL     A                   ; 
A4FC: 17                              ;
A4FD: 22                              ;
A4FE: 24 24           BIT     <$24                ; {ram.0024}
A500: 22                              ;
A501: 0E 0A 1B        ASL     $1B0A               ; 
A504: 1C                              ;
A505: 24 24           BIT     <$24                ; {ram.0024}
A507: 0A              ASL     A                   ; 
A508: 10 18           BPL     $A522               ; {}
A50A: 24 24           BIT     <$24                ; {ram.0024}
A50C: 19 1B 12        ORA     $121B,Y             ; 
A50F: 17                              ;
A510: 0C                              ;
A511: 0E 24 E3        ASL     $E324               ; 
A514: 24 24           BIT     <$24                ; {ram.0024}
A516: 21 00           AND     ($00,X)             ; {ram.GP_00}
A518: 20 24 24        JSR     $2424               ; 
A51B: E3                              ;
A51C: 24 24           BIT     <$24                ; {ram.0024}
A51E: 24 24           BIT     <$24                ; {ram.0024}
A520: 24 24           BIT     <$24                ; {ram.0024}
A522: 24 24           BIT     <$24                ; {ram.0024}
A524: 24 24           BIT     <$24                ; {ram.0024}
A526: F8              SED                         ; 
A527: 24 24           BIT     <$24                ; {ram.0024}
A529: 24 24           BIT     <$24                ; {ram.0024}
A52B: 24 24           BIT     <$24                ; {ram.0024}
A52D: 24 F8           BIT     <$F8                ; {ram.00F8}
A52F: 24 24           BIT     <$24                ; {ram.0024}
A531: 24 24           BIT     <$24                ; {ram.0024}
A533: 24 24           BIT     <$24                ; {ram.0024}
A535: 24 E2           BIT     <$E2                ; {ram.00E2}
A537: 24 24           BIT     <$24                ; {ram.0024}
A539: 21 20           AND     ($20,X)             ; {ram.0020}
A53B: 20 24 24        JSR     $2424               ; 
A53E: E2                              ;
A53F: 24 0D           BIT     <$0D                ; {ram.000D}
A541: 0A              ASL     A                   ; 
A542: 1B                              ;
A543: 14                              ;
A544: 17                              ;
A545: 0E 1C 1C        ASL     $1C1C               ; 
A548: 24 24           BIT     <$24                ; {ram.0024}
A54A: 24 10           BIT     <$10                ; {ram.0010}
A54C: 0A              ASL     A                   ; 
A54D: 17                              ;
A54E: 17                              ;
A54F: 18              CLC                         ; 
A550: 17                              ;
A551: 24 24           BIT     <$24                ; {ram.0024}
A553: 1C                              ;
A554: 1D 18 15        ORA     $1518,X             ; 
A557: 0E 24 E3        ASL     $E324               ; 
A55A: 24 24           BIT     <$24                ; {ram.0024}
A55C: 21 40           AND     ($40,X)             ; {ram.0040}
A55E: 20 24 24        JSR     $2424               ; 
A561: E3                              ;
A562: 24 24           BIT     <$24                ; {ram.0024}
A564: 24 24           BIT     <$24                ; {ram.0024}
A566: 24 24           BIT     <$24                ; {ram.0024}
A568: 24 24           BIT     <$24                ; {ram.0024}
A56A: 24 24           BIT     <$24                ; {ram.0024}
A56C: 24 24           BIT     <$24                ; {ram.0024}
A56E: 24 24           BIT     <$24                ; {ram.0024}
A570: 24 24           BIT     <$24                ; {ram.0024}
A572: 24 24           BIT     <$24                ; {ram.0024}
A574: 24 24           BIT     <$24                ; {ram.0024}
A576: 24 24           BIT     <$24                ; {ram.0024}
A578: 24 24           BIT     <$24                ; {ram.0024}
A57A: 24 24           BIT     <$24                ; {ram.0024}
A57C: E2                              ;
A57D: 24 24           BIT     <$24                ; {ram.0024}
A57F: 21 60           AND     ($60,X)             ; {ram.0060}
A581: 20 24 24        JSR     $2424               ; 
A584: E2                              ;
A585: 24 18           BIT     <$18                ; {ram.0018}
A587: 17                              ;
A588: 0E 24 18        ASL     $1824               ; 
A58B: 0F                              ;
A58C: 24 1D           BIT     <$1D                ; {ram.001D}
A58E: 11 0E           ORA     ($0E),Y             ; {ram.000E}
A590: 24 1D           BIT     <$1D                ; {ram.001D}
A592: 1B                              ;
A593: 12                              ;
A594: 0F                              ;
A595: 18              CLC                         ; 
A596: 1B                              ;
A597: 0C                              ;
A598: 0E 24 20        ASL     $2024               ; 
A59B: 12                              ;
A59C: 1D 11 24        ORA     $2411,X             ; 
A59F: E3                              ;
A5A0: 24 24           BIT     <$24                ; {ram.0024}
A5A2: 21 80           AND     ($80,X)             ; {ram.0080}
A5A4: 20 24 24        JSR     $2424               ; 
A5A7: E3                              ;
A5A8: 24 24           BIT     <$24                ; {ram.0024}
A5AA: 24 24           BIT     <$24                ; {ram.0024}
A5AC: 24 24           BIT     <$24                ; {ram.0024}
A5AE: 24 24           BIT     <$24                ; {ram.0024}
A5B0: 24 24           BIT     <$24                ; {ram.0024}
A5B2: 24 24           BIT     <$24                ; {ram.0024}
A5B4: 24 24           BIT     <$24                ; {ram.0024}
A5B6: 24 24           BIT     <$24                ; {ram.0024}
A5B8: 24 24           BIT     <$24                ; {ram.0024}
A5BA: 24 24           BIT     <$24                ; {ram.0024}
A5BC: 24 24           BIT     <$24                ; {ram.0024}
A5BE: 24 24           BIT     <$24                ; {ram.0024}
A5C0: 24 24           BIT     <$24                ; {ram.0024}
A5C2: E2                              ;
A5C3: 24 24           BIT     <$24                ; {ram.0024}
A5C5: 21 A0           AND     ($A0,X)             ; {ram.00A0}
A5C7: 20 24 24        JSR     $2424               ; 
A5CA: E2                              ;
A5CB: 24 19           BIT     <$19                ; {ram.0019}
A5CD: 18              CLC                         ; 
A5CE: 20 0E 1B        JSR     $1B0E               ; 
A5D1: 63                              ;
A5D2: 24 24           BIT     <$24                ; {ram.0024}
A5D4: 24 24           BIT     <$24                ; {ram.0024}
A5D6: 19 1B 12        ORA     $121B,Y             ; 
A5D9: 17                              ;
A5DA: 0C                              ;
A5DB: 0E 1C 1C        ASL     $1C1C               ; 
A5DE: 24 23           BIT     <$23                ; {ram.0023}
A5E0: 0E 15 0D        ASL     $0D15               ; 
A5E3: 0A              ASL     A                   ; 
A5E4: 24 E3           BIT     <$E3                ; {ram.00E3}
A5E6: 24 24           BIT     <$24                ; {ram.0024}
A5E8: 21 C0           AND     ($C0,X)             ; {ram.00C0}
A5EA: 20 24 24        JSR     $2424               ; 
A5ED: E3                              ;
A5EE: 24 24           BIT     <$24                ; {ram.0024}
A5F0: 24 24           BIT     <$24                ; {ram.0024}
A5F2: 24 24           BIT     <$24                ; {ram.0024}
A5F4: 24 24           BIT     <$24                ; {ram.0024}
A5F6: 24 24           BIT     <$24                ; {ram.0024}
A5F8: 24 24           BIT     <$24                ; {ram.0024}
A5FA: 24 24           BIT     <$24                ; {ram.0024}
A5FC: 24 24           BIT     <$24                ; {ram.0024}
A5FE: 24 24           BIT     <$24                ; {ram.0024}
A600: 24 24           BIT     <$24                ; {ram.0024}
A602: 24 24           BIT     <$24                ; {ram.0024}
A604: 24 24           BIT     <$24                ; {ram.0024}
A606: 24 24           BIT     <$24                ; {ram.0024}
A608: E2                              ;
A609: 24 24           BIT     <$24                ; {ram.0024}
A60B: 21 E0           AND     ($E0,X)             ; {ram.??SND_E0??}
A60D: 20 24 24        JSR     $2424               ; 
A610: E2                              ;
A611: 24 11           BIT     <$11                ; {ram.0011}
A613: 0A              ASL     A                   ; 
A614: 0D 24 24        ORA     $2424               ; 
A617: 18              CLC                         ; 
A618: 17                              ;
A619: 0E 24 18        ASL     $1824               ; 
A61C: 0F                              ;
A61D: 24 1D           BIT     <$1D                ; {ram.001D}
A61F: 11 0E           ORA     ($0E),Y             ; {ram.000E}
A621: 24 1D           BIT     <$1D                ; {ram.001D}
A623: 1B                              ;
A624: 12                              ;
A625: 0F                              ;
A626: 18              CLC                         ; 
A627: 1B                              ;
A628: 0C                              ;
A629: 0E 24 E3        ASL     $E324               ; 
A62C: 24 24           BIT     <$24                ; {ram.0024}
A62E: 22                              ;
A62F: 00              BRK                         ; 
A630: 20 24 24        JSR     $2424               ; 
A633: E3                              ;
A634: 24 24           BIT     <$24                ; {ram.0024}
A636: 24 24           BIT     <$24                ; {ram.0024}
A638: 24 24           BIT     <$24                ; {ram.0024}
A63A: 24 24           BIT     <$24                ; {ram.0024}
A63C: 24 24           BIT     <$24                ; {ram.0024}
A63E: 24 24           BIT     <$24                ; {ram.0024}
A640: 24 24           BIT     <$24                ; {ram.0024}
A642: 24 24           BIT     <$24                ; {ram.0024}
A644: 24 24           BIT     <$24                ; {ram.0024}
A646: 24 24           BIT     <$24                ; {ram.0024}
A648: 24 24           BIT     <$24                ; {ram.0024}
A64A: 24 24           BIT     <$24                ; {ram.0024}
A64C: 24 24           BIT     <$24                ; {ram.0024}
A64E: E2                              ;
A64F: 24 24           BIT     <$24                ; {ram.0024}
A651: 22                              ;
A652: 20 20 24        JSR     $2420               ; 
A655: 24 E2           BIT     <$E2                ; {ram.00E2}
A657: 24 20           BIT     <$20                ; {ram.0020}
A659: 12                              ;
A65A: 1D 11 24        ORA     $2411,X             ; 
A65D: 20 12 1C        JSR     $1C12               ; 
A660: 0D 18 16        ORA     $1618               ; 
A663: 63                              ;
A664: 24 1C           BIT     <$1C                ; {ram.001C}
A666: 11 0E           ORA     ($0E),Y             ; {ram.000E}
A668: 24 0D           BIT     <$0D                ; {ram.000D}
A66A: 12                              ;
A66B: 1F                              ;
A66C: 12                              ;
A66D: 0D 0E 0D        ORA     $0D0E               ; 
A670: 24 E2           BIT     <$E2                ; {ram.00E2}
A672: 24 24           BIT     <$24                ; {ram.0024}
A674: 22                              ;
A675: 40              RTI                         ; 
A676: 20 24 24        JSR     $2424               ; 
A679: E3                              ;
A67A: 24 24           BIT     <$24                ; {ram.0024}
A67C: 24 24           BIT     <$24                ; {ram.0024}
A67E: 24 24           BIT     <$24                ; {ram.0024}
A680: 24 24           BIT     <$24                ; {ram.0024}
A682: F8              SED                         ; 
A683: 24 24           BIT     <$24                ; {ram.0024}
A685: F8              SED                         ; 
A686: 24 24           BIT     <$24                ; {ram.0024}
A688: 24 24           BIT     <$24                ; {ram.0024}
A68A: 24 24           BIT     <$24                ; {ram.0024}
A68C: 24 24           BIT     <$24                ; {ram.0024}
A68E: 24 24           BIT     <$24                ; {ram.0024}
A690: 24 24           BIT     <$24                ; {ram.0024}
A692: 24 24           BIT     <$24                ; {ram.0024}
A694: E3                              ;
A695: 24 24           BIT     <$24                ; {ram.0024}
A697: 22                              ;
A698: 60              RTS                         ; 
A699: 20 24 24        JSR     $2424               ; 
A69C: E2                              ;
A69D: 24 12           BIT     <$12                ; {ram.0012}
A69F: 1D 24 12        ORA     $1224,X             ; 
A6A2: 17                              ;
A6A3: 1D 18 24        ORA     $2418,X             ; 
A6A6: 24 08           BIT     <$08                ; {ram.0008}
A6A8: 24 1E           BIT     <$1E                ; {ram.001E}
A6AA: 17                              ;
A6AB: 12                              ;
A6AC: 1D 1C 24        ORA     $241C,X             ; 
A6AF: 1D 18 24        ORA     $2418,X             ; 
A6B2: 11 12           ORA     ($12),Y             ; {ram.0012}
A6B4: 0D 0E 24        ORA     $240E               ; 
A6B7: E3                              ;
A6B8: 24 24           BIT     <$24                ; {ram.0024}
A6BA: 22                              ;
A6BB: 80                              ;
A6BC: 20 24 24        JSR     $2424               ; 
A6BF: E3                              ;
A6C0: 24 24           BIT     <$24                ; {ram.0024}
A6C2: 24 24           BIT     <$24                ; {ram.0024}
A6C4: 24 24           BIT     <$24                ; {ram.0024}
A6C6: 24 24           BIT     <$24                ; {ram.0024}
A6C8: 24 F8           BIT     <$F8                ; {ram.00F8}
A6CA: 24 24           BIT     <$24                ; {ram.0024}
A6CC: 24 24           BIT     <$24                ; {ram.0024}
A6CE: 24 24           BIT     <$24                ; {ram.0024}
A6D0: 24 F8           BIT     <$F8                ; {ram.00F8}
A6D2: 24 24           BIT     <$24                ; {ram.0024}
A6D4: 24 24           BIT     <$24                ; {ram.0024}
A6D6: 24 24           BIT     <$24                ; {ram.0024}
A6D8: 24 24           BIT     <$24                ; {ram.0024}
A6DA: E2                              ;
A6DB: 24 24           BIT     <$24                ; {ram.0024}
A6DD: 22                              ;
A6DE: A0 20           LDY     #$20                ; 
A6E0: 24 24           BIT     <$24                ; {ram.0024}
A6E2: E2                              ;
A6E3: 24 12           BIT     <$12                ; {ram.0012}
A6E5: 1D 24 0F        ORA     $0F24,X             ; 
A6E8: 1B                              ;
A6E9: 18              CLC                         ; 
A6EA: 16 24           ASL     $24,X               ; {ram.0024}
A6EC: 24 24           BIT     <$24                ; {ram.0024}
A6EE: 10 0A           BPL     $A6FA               ; {}
A6F0: 17                              ;
A6F1: 17                              ;
A6F2: 18              CLC                         ; 
A6F3: 17                              ;
A6F4: 24 24           BIT     <$24                ; {ram.0024}
A6F6: 0B                              ;
A6F7: 0E 0F 18        ASL     $180F               ; 
A6FA: 1B                              ;
A6FB: 0E 24 E3        ASL     $E324               ; 
A6FE: 24 24           BIT     <$24                ; {ram.0024}
A700: 22                              ;
A701: C0 20           CPY     #$20                ; 
A703: 24 24           BIT     <$24                ; {ram.0024}
A705: E3                              ;
A706: 24 24           BIT     <$24                ; {ram.0024}
A708: 24 24           BIT     <$24                ; {ram.0024}
A70A: 24 24           BIT     <$24                ; {ram.0024}
A70C: 24 24           BIT     <$24                ; {ram.0024}
A70E: 24 24           BIT     <$24                ; {ram.0024}
A710: 24 24           BIT     <$24                ; {ram.0024}
A712: 24 24           BIT     <$24                ; {ram.0024}
A714: 24 24           BIT     <$24                ; {ram.0024}
A716: 24 24           BIT     <$24                ; {ram.0024}
A718: 24 24           BIT     <$24                ; {ram.0024}
A71A: 24 24           BIT     <$24                ; {ram.0024}
A71C: 24 24           BIT     <$24                ; {ram.0024}
A71E: 24 24           BIT     <$24                ; {ram.0024}
A720: E2                              ;
A721: 24 24           BIT     <$24                ; {ram.0024}
A723: 22                              ;
A724: E0 20           CPX     #$20                ; 
A726: 24 24           BIT     <$24                ; {ram.0024}
A728: E2                              ;
A729: 24 1C           BIT     <$1C                ; {ram.001C}
A72B: 11 0E           ORA     ($0E),Y             ; {ram.000E}
A72D: 24 20           BIT     <$20                ; {ram.0020}
A72F: 0A              ASL     A                   ; 
A730: 1C                              ;
A731: 24 0C           BIT     <$0C                ; {ram.000C}
A733: 0A              ASL     A                   ; 
A734: 19 1D 1E        ORA     $1E1D,Y             ; 
A737: 1B                              ;
A738: 0E 0D 63        ASL     $630D               ; {ram.630D}
A73B: 24 24           BIT     <$24                ; {ram.0024}
A73D: 24 24           BIT     <$24                ; {ram.0024}
A73F: 24 24           BIT     <$24                ; {ram.0024}
A741: 24 24           BIT     <$24                ; {ram.0024}
A743: E3                              ;
A744: 24 24           BIT     <$24                ; {ram.0024}
A746: 23                              ;
A747: 00              BRK                         ; 
A748: 20 24 24        JSR     $2424               ; 
A74B: E3                              ;
A74C: 24 24           BIT     <$24                ; {ram.0024}
A74E: 24 24           BIT     <$24                ; {ram.0024}
A750: 24 24           BIT     <$24                ; {ram.0024}
A752: 24 24           BIT     <$24                ; {ram.0024}
A754: 24 24           BIT     <$24                ; {ram.0024}
A756: 24 24           BIT     <$24                ; {ram.0024}
A758: 24 24           BIT     <$24                ; {ram.0024}
A75A: F8              SED                         ; 
A75B: 24 24           BIT     <$24                ; {ram.0024}
A75D: F8              SED                         ; 
A75E: 24 24           BIT     <$24                ; {ram.0024}
A760: 24 24           BIT     <$24                ; {ram.0024}
A762: 24 24           BIT     <$24                ; {ram.0024}
A764: 24 24           BIT     <$24                ; {ram.0024}
A766: E2                              ;
A767: 24 24           BIT     <$24                ; {ram.0024}
A769: 23                              ;
A76A: 20 20 24        JSR     $2420               ; 
A76D: 24 E2           BIT     <$E2                ; {ram.00E2}
A76F: 24 24           BIT     <$24                ; {ram.0024}
A771: 24 10           BIT     <$10                ; {ram.0010}
A773: 18              CLC                         ; 
A774: 24 0F           BIT     <$0F                ; {ram.000F}
A776: 12                              ;
A777: 17                              ;
A778: 0D 24 1D        ORA     $1D24               ; 
A77B: 11 0E           ORA     ($0E),Y             ; {ram.000E}
A77D: 24 24           BIT     <$24                ; {ram.0024}
A77F: 08              PHP                         ; 
A780: 24 1E           BIT     <$1E                ; {ram.001E}
A782: 17                              ;
A783: 12                              ;
A784: 1D 1C 24        ORA     $241C,X             ; 
A787: 24 24           BIT     <$24                ; {ram.0024}
A789: E3                              ;
A78A: 24 24           BIT     <$24                ; {ram.0024}
A78C: 23                              ;
A78D: 40              RTI                         ; 
A78E: 20 24 24        JSR     $2424               ; 
A791: E3                              ;
A792: 24 24           BIT     <$24                ; {ram.0024}
A794: 24 F8           BIT     <$F8                ; {ram.00F8}
A796: 24 24           BIT     <$24                ; {ram.0024}
A798: 24 24           BIT     <$24                ; {ram.0024}
A79A: 24 F8           BIT     <$F8                ; {ram.00F8}
A79C: 24 24           BIT     <$24                ; {ram.0024}
A79E: 24 24           BIT     <$24                ; {ram.0024}
A7A0: 24 24           BIT     <$24                ; {ram.0024}
A7A2: 24 24           BIT     <$24                ; {ram.0024}
A7A4: 24 24           BIT     <$24                ; {ram.0024}
A7A6: 24 24           BIT     <$24                ; {ram.0024}
A7A8: 24 24           BIT     <$24                ; {ram.0024}
A7AA: 24 24           BIT     <$24                ; {ram.0024}
A7AC: E2                              ;
A7AD: 24 24           BIT     <$24                ; {ram.0024}
A7AF: 23                              ;
A7B0: 60              RTS                         ; 
A7B1: 20 24 24        JSR     $2424               ; 
A7B4: E2                              ;
A7B5: 24 24           BIT     <$24                ; {ram.0024}
A7B7: 24 24           BIT     <$24                ; {ram.0024}
A7B9: 24 15           BIT     <$15                ; {ram.0015}
A7BB: 12                              ;
A7BC: 17                              ;
A7BD: 14                              ;
A7BE: 24 24           BIT     <$24                ; {ram.0024}
A7C0: 1D 18 24        ORA     $2418,X             ; 
A7C3: 1C                              ;
A7C4: 0A              ASL     A                   ; 
A7C5: 1F                              ;
A7C6: 0E 24 11        ASL     $1124               ; 
A7C9: 0E 1B 63        ASL     $631B               ; {ram.631B}
A7CC: 24 24           BIT     <$24                ; {ram.0024}
A7CE: 24 E3           BIT     <$E3                ; {ram.00E3}
A7D0: 24 24           BIT     <$24                ; {ram.0024}
A7D2: 23                              ;
A7D3: 80                              ;
A7D4: 20 24 24        JSR     $2424               ; 
A7D7: E3                              ;
A7D8: 24 24           BIT     <$24                ; {ram.0024}
A7DA: 24 24           BIT     <$24                ; {ram.0024}
A7DC: 24 24           BIT     <$24                ; {ram.0024}
A7DE: 24 24           BIT     <$24                ; {ram.0024}
A7E0: 24 24           BIT     <$24                ; {ram.0024}
A7E2: 24 24           BIT     <$24                ; {ram.0024}
A7E4: 24 24           BIT     <$24                ; {ram.0024}
A7E6: 24 24           BIT     <$24                ; {ram.0024}
A7E8: 24 24           BIT     <$24                ; {ram.0024}
A7EA: 24 24           BIT     <$24                ; {ram.0024}
A7EC: 24 24           BIT     <$24                ; {ram.0024}
A7EE: 24 24           BIT     <$24                ; {ram.0024}
A7F0: 24 24           BIT     <$24                ; {ram.0024}
A7F2: E2                              ;
A7F3: 24 24           BIT     <$24                ; {ram.0024}
A7F5: 23                              ;
A7F6: A0 20           LDY     #$20                ; 
A7F8: 24 24           BIT     <$24                ; {ram.0024}
A7FA: E6 E4           INC     <$E4                ; {ram.00E4}
A7FC: E5 E4           SBC     <$E4                ; {ram.00E4}
A7FE: E5 E4           SBC     <$E4                ; {ram.00E4}
A800: E5 E4           SBC     <$E4                ; {ram.00E4}
A802: E5 E4           SBC     <$E4                ; {ram.00E4}
A804: E5 E4           SBC     <$E4                ; {ram.00E4}
A806: E5 E4           SBC     <$E4                ; {ram.00E4}
A808: E5 E4           SBC     <$E4                ; {ram.00E4}
A80A: E5 E4           SBC     <$E4                ; {ram.00E4}
A80C: E5 E4           SBC     <$E4                ; {ram.00E4}
A80E: E5 E4           SBC     <$E4                ; {ram.00E4}
A810: E5 E4           SBC     <$E4                ; {ram.00E4}
A812: E5 E4           SBC     <$E4                ; {ram.00E4}
A814: E5 E6           SBC     <$E6                ; {ram.00E6}
A816: 24 24           BIT     <$24                ; {ram.0024}
A818: 23                              ;
A819: C0 20           CPY     #$20                ; 
A81B: FF                              ;
A81C: FF                              ;
A81D: 00              BRK                         ; 
A81E: 00              BRK                         ; 
A81F: 00              BRK                         ; 
A820: 00              BRK                         ; 
A821: FF                              ;
A822: FF                              ;
A823: FF                              ;
A824: 0B                              ;
A825: 0A              ASL     A                   ; 
A826: 0A              ASL     A                   ; 
A827: 0A              ASL     A                   ; 
A828: 0A              ASL     A                   ; 
A829: 0E FF FF        ASL     $FFFF               ; 
A82C: 00              BRK                         ; 
A82D: 00              BRK                         ; 
A82E: 4A              LSR     A                   ; 
A82F: 5A                              ;
A830: 52                              ;
A831: 00              BRK                         ; 
A832: FF                              ;
A833: FF                              ;
A834: 00              BRK                         ; 
A835: 00              BRK                         ; 
A836: 00              BRK                         ; 
A837: 00              BRK                         ; 
A838: 58              CLI                         ; 
A839: 5A                              ;
A83A: FF                              ;
A83B: 23                              ;
A83C: E0 20           CPX     #$20                ; 
A83E: FF                              ;
A83F: 00              BRK                         ; 
A840: 00              BRK                         ; 
A841: 10 00           BPL     $A843               ; {}
A843: 00              BRK                         ; 
A844: 00              BRK                         ; 
A845: FF                              ;
A846: FF                              ;
A847: 00              BRK                         ; 
A848: 00              BRK                         ; 
A849: 0A              ASL     A                   ; 
A84A: 0A              ASL     A                   ; 
A84B: 02                              ;
A84C: 00              BRK                         ; 
A84D: FF                              ;
A84E: FF                              ;
A84F: FA                              ;
A850: FA                              ;
A851: BA              TSX                         ; 
A852: AA              TAX                         ; 
A853: AA              TAX                         ; 
A854: AA              TAX                         ; 
A855: FF                              ;
A856: FF                              ;
A857: FF                              ;
A858: FF                              ;
A859: FF                              ;
A85A: FF                              ;
A85B: FF                              ;
A85C: FF                              ;
A85D: FF                              ;
A85E: 2B                              ;
A85F: D0 02           BNE     $A863               ; {}
A861: FF                              ;
A862: FF                              ;
A863: 2B                              ;
A864: D6 02           DEC     $02,X               ; {ram.GP_02}
A866: FF                              ;
A867: FF                              ;
A868: FF                              ;
A869: 20 00 20        JSR     $2000               ; {hard.P_CNTRL_1} [NES] PPU setup #1
A86C: 24 24           BIT     <$24                ; {ram.0024}
A86E: 24 24           BIT     <$24                ; {ram.0024}
A870: 24 24           BIT     <$24                ; {ram.0024}
A872: 24 24           BIT     <$24                ; {ram.0024}
A874: 24 24           BIT     <$24                ; {ram.0024}
A876: 24 24           BIT     <$24                ; {ram.0024}
A878: 24 24           BIT     <$24                ; {ram.0024}
A87A: 24 24           BIT     <$24                ; {ram.0024}
A87C: 24 24           BIT     <$24                ; {ram.0024}
A87E: 24 24           BIT     <$24                ; {ram.0024}
A880: 24 24           BIT     <$24                ; {ram.0024}
A882: 24 24           BIT     <$24                ; {ram.0024}
A884: 24 24           BIT     <$24                ; {ram.0024}
A886: 24 24           BIT     <$24                ; {ram.0024}
A888: 24 24           BIT     <$24                ; {ram.0024}
A88A: 24 24           BIT     <$24                ; {ram.0024}
A88C: 20 20 20        JSR     $2020               ; 
A88F: 24 24           BIT     <$24                ; {ram.0024}
A891: 24 24           BIT     <$24                ; {ram.0024}
A893: 24 24           BIT     <$24                ; {ram.0024}
A895: 24 24           BIT     <$24                ; {ram.0024}
A897: 24 24           BIT     <$24                ; {ram.0024}
A899: 24 24           BIT     <$24                ; {ram.0024}
A89B: 24 24           BIT     <$24                ; {ram.0024}
A89D: 24 24           BIT     <$24                ; {ram.0024}
A89F: 24 24           BIT     <$24                ; {ram.0024}
A8A1: 24 24           BIT     <$24                ; {ram.0024}
A8A3: 24 24           BIT     <$24                ; {ram.0024}
A8A5: 24 24           BIT     <$24                ; {ram.0024}
A8A7: 24 24           BIT     <$24                ; {ram.0024}
A8A9: 24 24           BIT     <$24                ; {ram.0024}
A8AB: 24 24           BIT     <$24                ; {ram.0024}
A8AD: 24 24           BIT     <$24                ; {ram.0024}
A8AF: 20 40 20        JSR     $2040               ; 
A8B2: E0 D5           CPX     #$D5                ; 
A8B4: 24 24           BIT     <$24                ; {ram.0024}
A8B6: 24 24           BIT     <$24                ; {ram.0024}
A8B8: 24 24           BIT     <$24                ; {ram.0024}
A8BA: 24 24           BIT     <$24                ; {ram.0024}
A8BC: 24 24           BIT     <$24                ; {ram.0024}
A8BE: 24 24           BIT     <$24                ; {ram.0024}
A8C0: 24 24           BIT     <$24                ; {ram.0024}
A8C2: 24 24           BIT     <$24                ; {ram.0024}
A8C4: 24 24           BIT     <$24                ; {ram.0024}
A8C6: 24 24           BIT     <$24                ; {ram.0024}
A8C8: 24 24           BIT     <$24                ; {ram.0024}
A8CA: 24 24           BIT     <$24                ; {ram.0024}
A8CC: 24 24           BIT     <$24                ; {ram.0024}
A8CE: 24 24           BIT     <$24                ; {ram.0024}
A8D0: D4                              ;
A8D1: E0 20           CPX     #$20                ; 
A8D3: 60              RTS                         ; 
A8D4: 20 DC D7        JSR     $D7DC               ; 
A8D7: 24 24           BIT     <$24                ; {ram.0024}
A8D9: 24 24           BIT     <$24                ; {ram.0024}
A8DB: 24 24           BIT     <$24                ; {ram.0024}
A8DD: 24 24           BIT     <$24                ; {ram.0024}
A8DF: 24 24           BIT     <$24                ; {ram.0024}
A8E1: 24 24           BIT     <$24                ; {ram.0024}
A8E3: 24 24           BIT     <$24                ; {ram.0024}
A8E5: 24 24           BIT     <$24                ; {ram.0024}
A8E7: 24 24           BIT     <$24                ; {ram.0024}
A8E9: 24 24           BIT     <$24                ; {ram.0024}
A8EB: 24 24           BIT     <$24                ; {ram.0024}
A8ED: 24 24           BIT     <$24                ; {ram.0024}
A8EF: 24 24           BIT     <$24                ; {ram.0024}
A8F1: 24 24           BIT     <$24                ; {ram.0024}
A8F3: D6 DD           DEC     $DD,X               ; 
A8F5: 20 80 20        JSR     $2080               ; 
A8F8: DC                              ;
A8F9: EE 24 24        INC     $2424               ; 
A8FC: 24 24           BIT     <$24                ; {ram.0024}
A8FE: 24 24           BIT     <$24                ; {ram.0024}
A900: 24 24           BIT     <$24                ; {ram.0024}
A902: 24 24           BIT     <$24                ; {ram.0024}
A904: 24 24           BIT     <$24                ; {ram.0024}
A906: 24 24           BIT     <$24                ; {ram.0024}
A908: 24 24           BIT     <$24                ; {ram.0024}
A90A: 24 24           BIT     <$24                ; {ram.0024}
A90C: 24 24           BIT     <$24                ; {ram.0024}
A90E: 24 24           BIT     <$24                ; {ram.0024}
A910: 24 24           BIT     <$24                ; {ram.0024}
A912: 24 24           BIT     <$24                ; {ram.0024}
A914: 24 24           BIT     <$24                ; {ram.0024}
A916: D6 DB           DEC     $DB,X               ; {ram.00DB}
A918: 20 A0 20        JSR     $20A0               ; 
A91B: DE D7 24        DEC     $24D7,X             ; 
A91E: 24 24           BIT     <$24                ; {ram.0024}
A920: E6 E4           INC     <$E4                ; {ram.00E4}
A922: E5 E4           SBC     <$E4                ; {ram.00E4}
A924: E5 E4           SBC     <$E4                ; {ram.00E4}
A926: E5 E4           SBC     <$E4                ; {ram.00E4}
A928: E5 E4           SBC     <$E4                ; {ram.00E4}
A92A: E5 E4           SBC     <$E4                ; {ram.00E4}
A92C: E5 E4           SBC     <$E4                ; {ram.00E4}
A92E: E5 E4           SBC     <$E4                ; {ram.00E4}
A930: E5 E4           SBC     <$E4                ; {ram.00E4}
A932: E5 E4           SBC     <$E4                ; {ram.00E4}
A934: E5 E6           SBC     <$E6                ; {ram.00E6}
A936: 24 24           BIT     <$24                ; {ram.0024}
A938: 24 D6           BIT     <$D6                ; {ram.00D6}
A93A: DB                              ;
A93B: 20 C0 20        JSR     $20C0               ; 
A93E: DC                              ;
A93F: D7                              ;
A940: 24 24           BIT     <$24                ; {ram.0024}
A942: 24 E2           BIT     <$E2                ; {ram.00E2}
A944: 24 24           BIT     <$24                ; {ram.0024}
A946: 24 24           BIT     <$24                ; {ram.0024}
A948: 24 24           BIT     <$24                ; {ram.0024}
A94A: 24 24           BIT     <$24                ; {ram.0024}
A94C: 24 24           BIT     <$24                ; {ram.0024}
A94E: 24 24           BIT     <$24                ; {ram.0024}
A950: 24 24           BIT     <$24                ; {ram.0024}
A952: 24 24           BIT     <$24                ; {ram.0024}
A954: 24 24           BIT     <$24                ; {ram.0024}
A956: 24 24           BIT     <$24                ; {ram.0024}
A958: E3                              ;
A959: 24 24           BIT     <$24                ; {ram.0024}
A95B: 24 D6           BIT     <$D6                ; {ram.00D6}
A95D: DF                              ;
A95E: 20 E0 20        JSR     $20E0               ; 
A961: DE EE 24        DEC     $24EE,X             ; 
A964: 24 24           BIT     <$24                ; {ram.0024}
A966: E3                              ;
A967: 24 24           BIT     <$24                ; {ram.0024}
A969: 71 72           ADC     ($72),Y             ; {ram.0072}
A96B: 73                              ;
A96C: 74                              ;
A96D: 75 76           ADC     <$76,X              ; {ram.0076}
A96F: 77                              ;
A970: 78              SEI                         ; 
A971: 79 79 79        ADC     $7979,Y             ; {ram.7979}
A974: 7A                              ;
A975: 7B                              ;
A976: 24 24           BIT     <$24                ; {ram.0024}
A978: 24 24           BIT     <$24                ; {ram.0024}
A97A: 24 E2           BIT     <$E2                ; {ram.00E2}
A97C: 24 24           BIT     <$24                ; {ram.0024}
A97E: 24 D6           BIT     <$D6                ; {ram.00D6}
A980: DB                              ;
A981: 21 00           AND     ($00,X)             ; {ram.GP_00}
A983: 20 DE D8        JSR     $D8DE               ; 
A986: EF                              ;
A987: 24 24           BIT     <$24                ; {ram.0024}
A989: E2                              ;
A98A: 24 7C           BIT     <$7C                ; {ram.007C}
A98C: 7D 7E 7F        ADC     $7F7E,X             ; 
A98F: 80                              ;
A990: 81 82           STA     ($82,X)             ; {ram.0082}
A992: 83                              ;
A993: 84 85           STY     <$85                ; {ram.0085}
A995: 86 87           STX     <$87                ; {ram.0087}
A997: 88              DEY                         ; 
A998: 89                              ;
A999: 8A              TXA                         ; 
A99A: 8B                              ;
A99B: 24 24           BIT     <$24                ; {ram.0024}
A99D: 24 E3           BIT     <$E3                ; {ram.00E3}
A99F: 24 24           BIT     <$24                ; {ram.0024}
A9A1: 24 D6           BIT     <$D6                ; {ram.00D6}
A9A3: DF                              ;
A9A4: 21 20           AND     ($20,X)             ; {ram.0020}
A9A6: 20 DC DA        JSR     $DADC               ; 
A9A9: D7                              ;
A9AA: 24 24           BIT     <$24                ; {ram.0024}
A9AC: E3                              ;
A9AD: 24 8C           BIT     <$8C                ; {ram.008C}
A9AF: 8D 8E 8F        STA     $8F8E               ; {}
A9B2: 90 91           BCC     $A945               ; {}
A9B4: 92                              ;
A9B5: 93                              ;
A9B6: 94 95           STY     $95,X               ; {ram.0095}
A9B8: 96 97           STX     $97,Y               ; {ram.0097}
A9BA: 98              TYA                         ; 
A9BB: 99 9A 9B        STA     $9B9A,Y             ; {}
A9BE: 9C                              ;
A9BF: 24 24           BIT     <$24                ; {ram.0024}
A9C1: E2                              ;
A9C2: 24 24           BIT     <$24                ; {ram.0024}
A9C4: D4                              ;
A9C5: D9 DB 21        CMP     $21DB,Y             ; 
A9C8: 40              RTI                         ; 
A9C9: 20 DC D9        JSR     $D9DC               ; 
A9CC: EE 24 24        INC     $2424               ; 
A9CF: E2                              ;
A9D0: 24 9D           BIT     <$9D                ; {ram.009D}
A9D2: 9E                              ;
A9D3: 9F                              ;
A9D4: A0 A1           LDY     #$A1                ; 
A9D6: A2 A3           LDX     #$A3                ; 
A9D8: A4 A5           LDY     <$A5                ; {ram.00A5}
A9DA: A6 A7           LDX     <$A7                ; {ram.00A7}
A9DC: A8              TAY                         ; 
A9DD: A9 AA           LDA     #$AA                ; 
A9DF: AB                              ;
A9E0: AC AD AE        LDY     $AEAD               ; {}
A9E3: 24 E3           BIT     <$E3                ; {ram.00E3}
A9E5: 24 24           BIT     <$24                ; {ram.0024}
A9E7: D6 DB           DEC     $DB,X               ; {ram.00DB}
A9E9: DF                              ;
A9EA: 21 60           AND     ($60,X)             ; {ram.0060}
A9EC: 20 DE DB        JSR     $DBDE               ; 
A9EF: D7                              ;
A9F0: 24 24           BIT     <$24                ; {ram.0024}
A9F2: E3                              ;
A9F3: 70 AF           BVS     $A9A4               ; {}
A9F5: B0 B1           BCS     $A9A8               ; {}
A9F7: B2                              ;
A9F8: B3                              ;
A9F9: B4 B5           LDY     $B5,X               ; {ram.00B5}
A9FB: B6 B7           LDX     $B7,Y               ; {ram.00B7}
A9FD: B8              CLV                         ; 
A9FE: B9 BA BB        LDA     $BBBA,Y             ; {}
AA01: BC BD BE        LDY     $BEBD,X             ; {}
AA04: BF                              ;
AA05: C0 24           CPY     #$24                ; 
AA07: E2                              ;
AA08: 24 24           BIT     <$24                ; {ram.0024}
AA0A: D6 DB           DEC     $DB,X               ; {ram.00DB}
AA0C: DB                              ;
AA0D: 21 80           AND     ($80,X)             ; {ram.0080}
AA0F: 20 DC DD        JSR     $DDDC               ; 
AA12: D7                              ;
AA13: 24 24           BIT     <$24                ; {ram.0024}
AA15: E2                              ;
AA16: 24 24           BIT     <$24                ; {ram.0024}
AA18: 24 24           BIT     <$24                ; {ram.0024}
AA1A: 24 24           BIT     <$24                ; {ram.0024}
AA1C: 24 C1           BIT     <$C1                ; {ram.00C1}
AA1E: C2                              ;
AA1F: C3                              ;
AA20: C4 C5           CPY     <$C5                ; {ram.00C5}
AA22: 24 24           BIT     <$24                ; {ram.0024}
AA24: 24 24           BIT     <$24                ; {ram.0024}
AA26: 24 24           BIT     <$24                ; {ram.0024}
AA28: 24 24           BIT     <$24                ; {ram.0024}
AA2A: E3                              ;
AA2B: 24 24           BIT     <$24                ; {ram.0024}
AA2D: D6 DB           DEC     $DB,X               ; {ram.00DB}
AA2F: DF                              ;
AA30: 21 A0           AND     ($A0,X)             ; {ram.00A0}
AA32: 20 DE DB        JSR     $DBDE               ; 
AA35: EE 24 24        INC     $2424               ; 
AA38: E3                              ;
AA39: 24 C6           BIT     <$C6                ; {ram.00C6}
AA3B: C7                              ;
AA3C: C8              INY                         ; 
AA3D: C8              INY                         ; 
AA3E: C8              INY                         ; 
AA3F: 24 C9           BIT     <$C9                ; {ram.00C9}
AA41: CA              DEX                         ; 
AA42: CB                              ;
AA43: CC CD C8        CPY     $C8CD               ; 
AA46: C8              INY                         ; 
AA47: C8              INY                         ; 
AA48: C8              INY                         ; 
AA49: E8              INX                         ; 
AA4A: E9 D3           SBC     #$D3                ; 
AA4C: 24 E2           BIT     <$E2                ; {ram.00E2}
AA4E: 24 24           BIT     <$24                ; {ram.0024}
AA50: D6 DB           DEC     $DB,X               ; {ram.00DB}
AA52: DB                              ;
AA53: 21 C0           AND     ($C0,X)             ; {ram.00C0}
AA55: 20 DC DB        JSR     $DBDC               ; 
AA58: D7                              ;
AA59: 24 24           BIT     <$24                ; {ram.0024}
AA5B: E2                              ;
AA5C: 24 24           BIT     <$24                ; {ram.0024}
AA5E: 24 24           BIT     <$24                ; {ram.0024}
AA60: 24 24           BIT     <$24                ; {ram.0024}
AA62: 24 24           BIT     <$24                ; {ram.0024}
AA64: 24 CE           BIT     <$CE                ; {ram.00CE}
AA66: CF                              ;
AA67: 24 24           BIT     <$24                ; {ram.0024}
AA69: 24 24           BIT     <$24                ; {ram.0024}
AA6B: 24 EA           BIT     <$EA                ; {ram.00EA}
AA6D: EB                              ;
AA6E: EC 24 E3        CPX     $E324               ; 
AA71: 24 24           BIT     <$24                ; {ram.0024}
AA73: D6 DB           DEC     $DB,X               ; {ram.00DB}
AA75: DF                              ;
AA76: 21 E0           AND     ($E0,X)             ; {ram.??SND_E0??}
AA78: 20 DC DB        JSR     $DBDC               ; 
AA7B: D7                              ;
AA7C: 24 24           BIT     <$24                ; {ram.0024}
AA7E: E3                              ;
AA7F: 24 24           BIT     <$24                ; {ram.0024}
AA81: 24 24           BIT     <$24                ; {ram.0024}
AA83: 24 24           BIT     <$24                ; {ram.0024}
AA85: 24 24           BIT     <$24                ; {ram.0024}
AA87: 24 D1           BIT     <$D1                ; {ram.00D1}
AA89: D2                              ;
AA8A: 24 24           BIT     <$24                ; {ram.0024}
AA8C: 24 24           BIT     <$24                ; {ram.0024}
AA8E: 24 24           BIT     <$24                ; {ram.0024}
AA90: 24 24           BIT     <$24                ; {ram.0024}
AA92: 24 E2           BIT     <$E2                ; {ram.00E2}
AA94: 24 24           BIT     <$24                ; {ram.0024}
AA96: D6 DB           DEC     $DB,X               ; {ram.00DB}
AA98: DB                              ;
AA99: 22                              ;
AA9A: 00              BRK                         ; 
AA9B: 20 DC D8        JSR     $D8DC               ; 
AA9E: E1 D5           SBC     ($D5,X)             ; 
AAA0: 24 E6           BIT     <$E6                ; {ram.00E6}
AAA2: E4 E5           CPX     <$E5                ; {ram.00E5}
AAA4: E4 E5           CPX     <$E5                ; {ram.00E5}
AAA6: E4 E5           CPX     <$E5                ; {ram.00E5}
AAA8: E4 E5           CPX     <$E5                ; {ram.00E5}
AAAA: E4 E5           CPX     <$E5                ; {ram.00E5}
AAAC: E4 E5           CPX     <$E5                ; {ram.00E5}
AAAE: E4 E5           CPX     <$E5                ; {ram.00E5}
AAB0: E4 E5           CPX     <$E5                ; {ram.00E5}
AAB2: E4 E5           CPX     <$E5                ; {ram.00E5}
AAB4: E4 E5           CPX     <$E5                ; {ram.00E5}
AAB6: E6 24           INC     <$24                ; {ram.0024}
AAB8: D4                              ;
AAB9: E1 D9           SBC     ($D9,X)             ; {ram.00D9}
AABB: DD 22 20        CMP     $2022,X             ; 
AABE: 20 DC DA        JSR     $DADC               ; 
AAC1: DC                              ;
AAC2: D7                              ;
AAC3: 24 24           BIT     <$24                ; {ram.0024}
AAC5: 24 24           BIT     <$24                ; {ram.0024}
AAC7: 24 24           BIT     <$24                ; {ram.0024}
AAC9: 24 24           BIT     <$24                ; {ram.0024}
AACB: 24 F0           BIT     <$F0                ; {ram.00F0}
AACD: 01 09           ORA     ($09,X)             ; {ram.0009}
AACF: 08              PHP                         ; 
AAD0: 06 24           ASL     <$24                ; {ram.0024}
AAD2: 17                              ;
AAD3: 12                              ;
AAD4: 17                              ;
AAD5: 1D 0E 17        ORA     $170E,X             ; 
AAD8: 0D 18 24        ORA     $2418               ; 
AADB: D6 DC           DEC     $DC,X               ; 
AADD: DB                              ;
AADE: DF                              ;
AADF: 22                              ;
AAE0: 40              RTI                         ; 
AAE1: 20 DC DA        JSR     $DADC               ; 
AAE4: DC                              ;
AAE5: EE 24 24        INC     $2424               ; 
AAE8: 24 24           BIT     <$24                ; {ram.0024}
AAEA: 24 24           BIT     <$24                ; {ram.0024}
AAEC: 24 24           BIT     <$24                ; {ram.0024}
AAEE: 24 24           BIT     <$24                ; {ram.0024}
AAF0: 24 24           BIT     <$24                ; {ram.0024}
AAF2: 24 24           BIT     <$24                ; {ram.0024}
AAF4: 24 24           BIT     <$24                ; {ram.0024}
AAF6: 24 24           BIT     <$24                ; {ram.0024}
AAF8: 24 24           BIT     <$24                ; {ram.0024}
AAFA: 24 24           BIT     <$24                ; {ram.0024}
AAFC: 24 24           BIT     <$24                ; {ram.0024}
AAFE: D6 DE           DEC     $DE,X               ; {ram.00DE}
AB00: ED DD 22        SBC     $22DD               ; 
AB03: 60              RTS                         ; 
AB04: 20 DC DA        JSR     $DADC               ; 
AB07: DE D7 24        DEC     $24D7,X             ; 
AB0A: 24 24           BIT     <$24                ; {ram.0024}
AB0C: 24 24           BIT     <$24                ; {ram.0024}
AB0E: 24 24           BIT     <$24                ; {ram.0024}
AB10: 24 24           BIT     <$24                ; {ram.0024}
AB12: 24 24           BIT     <$24                ; {ram.0024}
AB14: 24 24           BIT     <$24                ; {ram.0024}
AB16: 24 24           BIT     <$24                ; {ram.0024}
AB18: 24 24           BIT     <$24                ; {ram.0024}
AB1A: 24 24           BIT     <$24                ; {ram.0024}
AB1C: 24 24           BIT     <$24                ; {ram.0024}
AB1E: 24 24           BIT     <$24                ; {ram.0024}
AB20: 24 D6           BIT     <$D6                ; {ram.00D6}
AB22: DE DB DD        DEC     $DDDB,X             ; 
AB25: 22                              ;
AB26: 80                              ;
AB27: 20 E1 D9        JSR     $D9E1               ; 
AB2A: DC                              ;
AB2B: ED E0 EF        SBC     $EFE0               ; 
AB2E: 24 24           BIT     <$24                ; {ram.0024}
AB30: 19 1E 1C        ORA     $1C1E,Y             ; 
AB33: 11 24           ORA     ($24),Y             ; {ram.0024}
AB35: 1C                              ;
AB36: 1D 0A 1B        ORA     $1B0A,X             ; 
AB39: 1D 24 0B        ORA     $0B24,X             ; 
AB3C: 1E 1D 1D        ASL     $1D1D,X             ; 
AB3F: 18              CLC                         ; 
AB40: 17                              ;
AB41: 24 24           BIT     <$24                ; {ram.0024}
AB43: 24 D6           BIT     <$D6                ; {ram.00D6}
AB45: D8              CLD                         ; 
AB46: E1 D9           SBC     ($D9,X)             ; {ram.00D9}
AB48: 22                              ;
AB49: A0 20           LDY     #$20                ; 
AB4B: DD ED DE        CMP     $DEED,X             ; 
AB4E: D8              CLD                         ; 
AB4F: E1 E1           SBC     ($E1,X)             ; {ram.00E1}
AB51: D5 24           CMP     $24,X               ; {ram.0024}
AB53: 24 24           BIT     <$24                ; {ram.0024}
AB55: 24 24           BIT     <$24                ; {ram.0024}
AB57: 24 24           BIT     <$24                ; {ram.0024}
AB59: 24 24           BIT     <$24                ; {ram.0024}
AB5B: 24 24           BIT     <$24                ; {ram.0024}
AB5D: 24 24           BIT     <$24                ; {ram.0024}
AB5F: 24 24           BIT     <$24                ; {ram.0024}
AB61: 24 24           BIT     <$24                ; {ram.0024}
AB63: 24 24           BIT     <$24                ; {ram.0024}
AB65: 24 24           BIT     <$24                ; {ram.0024}
AB67: D6 DA           DEC     $DA,X               ; {ram.00DA}
AB69: DD ED 22        CMP     $22ED,X             ; 
AB6C: C0 20           CPY     #$20                ; 
AB6E: DD DB DE        CMP     $DEDB,X             ; 
AB71: DA                              ;
AB72: DC                              ;
AB73: DD D8 E0        CMP     $E0D8,X             ; 
AB76: E0 EF           CPX     #$EF                ; 
AB78: 24 24           BIT     <$24                ; {ram.0024}
AB7A: 24 24           BIT     <$24                ; {ram.0024}
AB7C: D4                              ;
AB7D: E0 E0           CPX     #$E0                ; 
AB7F: D5 24           CMP     $24,X               ; {ram.0024}
AB81: 24 24           BIT     <$24                ; {ram.0024}
AB83: 24 24           BIT     <$24                ; {ram.0024}
AB85: 24 24           BIT     <$24                ; {ram.0024}
AB87: 24 D4           BIT     <$D4                ; {ram.00D4}
AB89: EF                              ;
AB8A: DA                              ;
AB8B: DA                              ;
AB8C: DF                              ;
AB8D: DB                              ;
AB8E: 22                              ;
AB8F: E0 20           CPX     #$20                ; 
AB91: DF                              ;
AB92: DB                              ;
AB93: DC                              ;
AB94: DA                              ;
AB95: DE DF DA        DEC     $DADF,X             ; 
AB98: DC                              ;
AB99: DD DB 26        CMP     $26DB,X             ; 
AB9C: 26 26           ROL     <$26                ; {ram.0026}
AB9E: 26 DA           ROL     <$DA                ; {ram.00DA}
ABA0: DC                              ;
ABA1: DD ED E0        CMP     $E0ED,X             ; 
ABA4: E0 EF           CPX     #$EF                ; 
ABA6: 24 D4           BIT     <$D4                ; {ram.00D4}
ABA8: E0 E0           CPX     #$E0                ; 
ABAA: E0 D9           CPX     #$D9                ; 
ABAC: DB                              ;
ABAD: DA                              ;
ABAE: DA                              ;
ABAF: DF                              ;
ABB0: DB                              ;
ABB1: 23                              ;
ABB2: 00              BRK                         ; 
ABB3: 20 ED D8        JSR     $D8ED               ; 
ABB6: E1 D9           SBC     ($D9,X)             ; {ram.00D9}
ABB8: DE D8 E1        DEC     $E1D8,X             ; 
ABBB: D9 DF DB        CMP     $DBDF,Y             ; 
ABBE: 26 26           ROL     <$26                ; {ram.0026}
ABC0: 26 26           ROL     <$26                ; {ram.0026}
ABC2: DA                              ;
ABC3: DC                              ;
ABC4: D8              CLD                         ; 
ABC5: E1 D9           SBC     ($D9,X)             ; {ram.00D9}
ABC7: DC                              ;
ABC8: D8              CLD                         ; 
ABC9: E0 D9           CPX     #$D9                ; 
ABCB: DC                              ;
ABCC: DD DD D8        CMP     $D8DD,X             ; 
ABCF: E1 E1           SBC     ($E1,X)             ; {ram.00E1}
ABD1: D9 DD ED        CMP     $EDDD,Y             ; 
ABD4: 23                              ;
ABD5: 20 20 ED        JSR     $ED20               ; 
ABD8: DA                              ;
ABD9: DD ED DE        CMP     $DEED,X             ; 
ABDC: DA                              ;
ABDD: DC                              ;
ABDE: DB                              ;
ABDF: DD DB 26        CMP     $26DB,X             ; 
ABE2: 26 26           ROL     <$26                ; {ram.0026}
ABE4: 26 DA           ROL     <$DA                ; {ram.00DA}
ABE6: DE DA DC        DEC     $DCDA,X             ; 
ABE9: DB                              ;
ABEA: DE DA DD        DEC     $DDDA,X             ; 
ABED: ED DC DC        SBC     $DCDC               ; 
ABF0: DD DA DC        CMP     $DCDA,X             ; 
ABF3: DC                              ;
ABF4: DB                              ;
ABF5: DD ED 23        CMP     $23ED,X             ; 
ABF8: 40              RTI                         ; 
ABF9: 20 ED DA        JSR     $DAED               ; 
ABFC: DD D8 E1        CMP     $E1D8,X             ; 
ABFF: DA                              ;
AC00: DC                              ;
AC01: DB                              ;
AC02: DF                              ;
AC03: DB                              ;
AC04: 26 26           ROL     <$26                ; {ram.0026}
AC06: 26 26           ROL     <$26                ; {ram.0026}
AC08: DA                              ;
AC09: D8              CLD                         ; 
AC0A: D9 DC DB        CMP     $DBDC,Y             ; 
AC0D: DC                              ;
AC0E: DA                              ;
AC0F: D8              CLD                         ; 
AC10: E1 D9           SBC     ($D9,X)             ; {ram.00D9}
AC12: DE DF DA        DEC     $DADF,X             ; 
AC15: D8              CLD                         ; 
AC16: E1 E1           SBC     ($E1,X)             ; {ram.00E1}
AC18: D9 E1 23        CMP     $23E1,Y             ; 
AC1B: 60              RTS                         ; 
AC1C: 20 ED D9        JSR     $D9ED               ; 
AC1F: DF                              ;
AC20: DA                              ;
AC21: DC                              ;
AC22: DA                              ;
AC23: DE DB DD        DEC     $DDDB,X             ; 
AC26: DB                              ;
AC27: 26 26           ROL     <$26                ; {ram.0026}
AC29: 26 26           ROL     <$26                ; {ram.0026}
AC2B: DA                              ;
AC2C: DA                              ;
AC2D: ED DE D8        SBC     $D8DE               ; 
AC30: E1 E1           SBC     ($E1,X)             ; {ram.00E1}
AC32: D9 DC DB        CMP     $DBDC,Y             ; 
AC35: DE D8 E1        DEC     $E1D8,X             ; 
AC38: D9 DD DD        CMP     $DDDD,Y             ; 
AC3B: DB                              ;
AC3C: DC                              ;
AC3D: 23                              ;
AC3E: 80                              ;
AC3F: 20 DF DB        JSR     $DBDF               ; 
AC42: DF                              ;
AC43: DA                              ;
AC44: DC                              ;
AC45: DB                              ;
AC46: DE DB DD        DEC     $DDDB,X             ; 
AC49: DB                              ;
AC4A: 26 26           ROL     <$26                ; {ram.0026}
AC4C: 26 26           ROL     <$26                ; {ram.0026}
AC4E: DA                              ;
AC4F: DA                              ;
AC50: DB                              ;
AC51: DD DA DE        CMP     $DEDA,X             ; 
AC54: D8              CLD                         ; 
AC55: E1 D9           SBC     ($D9,X)             ; {ram.00D9}
AC57: DB                              ;
AC58: DE DA DD        DEC     $DDDA,X             ; 
AC5B: DB                              ;
AC5C: DE DF D8        DEC     $D8DF,X             ; 
AC5F: E1 23           SBC     ($23,X)             ; {ram.0023}
AC61: A0 20           LDY     #$20                ; 
AC63: DF                              ;
AC64: DB                              ;
AC65: DF                              ;
AC66: DA                              ;
AC67: DC                              ;
AC68: DB                              ;
AC69: DE DB DD        DEC     $DDDB,X             ; 
AC6C: DB                              ;
AC6D: 26 26           ROL     <$26                ; {ram.0026}
AC6F: 26 26           ROL     <$26                ; {ram.0026}
AC71: DA                              ;
AC72: DA                              ;
AC73: DB                              ;
AC74: DD DA DE        CMP     $DEDA,X             ; 
AC77: DA                              ;
AC78: DD DB DB        CMP     $DBDB,X             ; 
AC7B: DE DA DD        DEC     $DDDA,X             ; 
AC7E: DB                              ;
AC7F: DE DF DC        DEC     $DCDF,X             ; 
AC82: DF                              ;
AC83: 23                              ;
AC84: C0 20           CPY     #$20                ; 
AC86: 05 05           ORA     <$05                ; {ram.0005}
AC88: 05 05           ORA     <$05                ; {ram.0005}
AC8A: 05 05           ORA     <$05                ; {ram.0005}
AC8C: 05 05           ORA     <$05                ; {ram.0005}
AC8E: 08              PHP                         ; 
AC8F: 6A              ROR     A                   ; 
AC90: 5A                              ;
AC91: 5A                              ;
AC92: 5A                              ;
AC93: 5A                              ;
AC94: 9A              TXS                         ; 
AC95: 22                              ;
AC96: 00              BRK                         ; 
AC97: 66 55           ROR     <$55                ; {ram.0055}
AC99: 55 55           EOR     $55,X               ; {ram.0055}
AC9B: 55 99           EOR     $99,X               ; {ram.0099}
AC9D: 00              BRK                         ; 
AC9E: 00              BRK                         ; 
AC9F: 6E 5F 55        ROR     $555F               ; 
ACA2: 5D DF BB        EOR     $BBDF,X             ; {}
ACA5: 00              BRK                         ; 
ACA6: 23                              ;
ACA7: E0 20           CPX     #$20                ; 
ACA9: 00              BRK                         ; 
ACAA: 0A              ASL     A                   ; 
ACAB: 0A              ASL     A                   ; 
ACAC: 0A              ASL     A                   ; 
ACAD: 0A              ASL     A                   ; 
ACAE: 0A              ASL     A                   ; 
ACAF: 0A              ASL     A                   ; 
ACB0: 00              BRK                         ; 
ACB1: 00              BRK                         ; 
ACB2: 00              BRK                         ; 
ACB3: C0 30           CPY     #$30                ; 
ACB5: 00              BRK                         ; 
ACB6: 00              BRK                         ; 
ACB7: 00              BRK                         ; 
ACB8: 00              BRK                         ; 
ACB9: 00              BRK                         ; 
ACBA: 00              BRK                         ; 
ACBB: CC 33 00        CPY     $0033               ; {ram.0033}
ACBE: 00              BRK                         ; 
ACBF: 00              BRK                         ; 
ACC0: 00              BRK                         ; 
ACC1: 00              BRK                         ; 
ACC2: 20 FC F3        JSR     $F3FC               ; 
ACC5: 00              BRK                         ; 
ACC6: 00              BRK                         ; 
ACC7: F0 F0           BEQ     $ACB9               ; {}
ACC9: FF                              ;
ACCA: FF                              ;
ACCB: FF                              ;
ACCC: FF                              ;
ACCD: FF                              ;
ACCE: FF                              ;
ACCF: FF                              ;


ACD0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF 
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
;  C CHR ROM bank mode. Zelda uses 0: 8KB at a time (one single 8K RAM bank)
;  PP Program ROM switch mode. Zelda uses 3: 16K fixed, 16K switched banks
;  MM Name table mirroring. Zelda switches between 2 and 3: vertical or horizontal
; R1 - CHR bank size ***CCCCC
;  Ignored in Zelda since R0.C is 0
; R2 - CHR bank select ***CCCCC
;  Zelda sets bank 0 -- the only bank (one single 8K RAM bank)
; R3 - PRG bank select ***RPPPP
;  R PRG RAM enabled. Zelda sends 0 which means it DOES have battery backed RAM.
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

