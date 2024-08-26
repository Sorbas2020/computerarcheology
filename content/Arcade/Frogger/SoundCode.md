![Frogger Sound Board](Frogger.jpg)

# Frogger Sound Board

>>> cpu Z80

>>> binary 0000:roms/frogger.608*swap(0,1) + roms/frogger.609 + roms/frogger.610

>>> memoryTable hard 

[Hardware Info](SoundHardware.md)

>>> memoryTable ram 

[RAM Usage](SoundRAMUse.md)

```code
;I14
; Reset program to program entry

;C14
; Reset program to program entry

START: 
0000: 06 00           LD      B,$00               ; Fill value of 0
0002: 21 00 40        LD      HL,$4000            ; First location of RAM
0005: C3 0B 01        JP      $010B               ; {} Continue init
```

# Write to AY Chip

```code
WriteToAY: 
; A is address, B is value
0008: D3 80           OUT     ($80),A             ; {hard.AY_ADDR} Write the address to the AY
000A: 78              LD      A,B                 ; Write the ...
000B: D3 40           OUT     ($40),A             ; {hard.AY_DATA} ... value to the AY register
000D: C9              RET                         ; Done
000E: FF FF  

0010: C3 B7 02        JP      $02B7               ; {code.ReadAmplitude} Read voice amplitude
0013: FF FF FF FF FF                 

0018: C3 7C 02        JP      $027C               ; {code.SetAmplitude} Set voice amplitude
001B: FF FF FF FF FF                 

0020: C3 C7 02        JP      $02C7               ; {code.Filter00} Remove all voice capacitor filters
0023: FF FF FF FF FF               

0028: C3 3C 02        JP      $023C               ; {code.WriteTune} Write to voice tune registers (coarse/fine)
002B: FF FF FF FF FF                 

0030: C3 60 02        JP      $0260               ; {code.EnableTone} Enable tone

;C00 Not used
0033: 3E FF           LD      A,$FF               ; Return ...
0035: C9              RET                         ; ... end processing
0036: FF FF 
```

# Interrupt

```code
Interrupt: 
; Interrupt Mode 1 - everything comes here
; Command from main processor is on AY Port A
; 00: clear all commands
; FF: RST 0 (Restart program)
;
; There is some bit shuffling that goes on here for bytes with bits in the upper nibble but
; all zeros in the lower nibble. Perhaps this means something on other hardware where this
; is a fragment on common software? Possibly related to the capacitor filters on the outputs.
;
; I need to investigate this shuffling.
;
0038: 08              EX      AF,AF'              ; Swap ...
0039: D9              EXX                         ; ... register sets
003A: 21 6D 00        LD      HL,$006D            ; Return address
003D: E5              PUSH    HL                  ; Push return
003E: 3E 0E           LD      A,$0E               ; Read from ...
0040: CD C1 02        CALL    $02C1               ; {code.ReadAY} ... AY IO port A
0043: B7              OR      A                   ; Reset everything?
0044: 28 2B           JR      Z,$71               ; {code.ClearCommands} Yes ... go reset all command info and out
;
; TOPHER patch to always play the same sound -- for recording the sound effects.
;
; 0046: 3E xx           LD      A,$xx   SWAPPED: 3D yy
; 0048: 57              LD      D,A     SWAPPED: 57
; 0049: 00 00 00        NOP             SWAPPED: 00 00 00
;
0046: 57              LD      D,A                 ; Copy command to D
0047: FE FF           CP      $FF                 ; Is it a RESET command?
0049: 20 01           JR      NZ,$4C              ; {} No ... keep going
004B: C7              RST     $00                 ; Software reset (won't come back)

004C: E6 0F           AND     $0F                 ; Lower 4 bits of command ...
004E: 4F              LD      C,A                 ; ... to C
004F: 7A              LD      A,D                 ; Original command back to A
0050: A9              XOR     C                   ; Any of the upper 4 bits set (the lowers get cleared here)
0051: 28 07           JR      Z,$5A               ; {} No ... maybe ???
0053: 79              LD      A,C                 ; Are the lower 4 bits ...
0054: B7              OR      A                   ; ... all 0?
0055: 28 03           JR      Z,$5A               ; {} Yes ... ???
0057: 7A              LD      A,D                 ; Original command
0058: 18 3D           JR      $97                 ; {code.CmdRequest} Process original command as-is
;
005A: 7A              LD      A,D                 ; Original command
005B: E6 0F           AND     $0F                 ; Just the lower bits
005D: 20 38           JR      NZ,$97              ; {code.CmdRequest} Lower 4 is not 0 ... processes lower 4 as command
005F: 7A              LD      A,D                 ; Original command
0060: C6 12           ADD     A,$12               ; ??? ...
0062: 07              RLCA                        ; ... the ...
0063: 07              RLCA                        ; ... bits ...
0064: 07              RLCA                        ; ... around
0065: CB 7F           BIT     7,A                 ; Upper bit set?
0067: 28 2E           JR      Z,$97               ; {code.CmdRequest} No ... use this as command
0069: CB BF           RES     7,A                 ; Reset the bit
006B: 18 13           JR      $80                 ; {code.StopCommand} Stop the requested command

; Return from interrupt
006D: D9              EXX                         ; Swap ...
006E: 08              EX      AF,AF'              ; ... register sets
006F: FB              EI                          ; Interrupts allowed again
0070: C9              RET                         ; Back to interrupted main loop

ClearCommands: 
0071: 06 06           LD      B,$06               ; Six bytes (2 per voice)
0073: 21 40 40        LD      HL,$4040            ; Start of command data
0076: 77              LD      (HL),A              ; Store 0
0077: 23              INC     HL                  ; Do all ...
0078: 10 FC           DJNZ    $76                 ; {} ... command structs
007A: 3E 07           LD      A,$07               ; Enable register
007C: 06 3F           LD      B,$3F               ; Turn off all ...
007E: CF              RST     $08                 ; ... voices (tone and noise)
007F: C9              RET                         ; back to 6D and out

StopCommand: 
0080: CD E6 00        CALL    $00E6               ; {code.ReinitCommand} Attempt to reinit running command
0083: D0              RET     NC                  ; Return if not there
0084: CD 8C 00        CALL    $008C               ; {code.FindDat} Find command data
0087: AF              XOR     A                   ; Zero
0088: 77              LD      (HL),A              ; Clear command
0089: 23              INC     HL                  ; Clear ...
008A: 77              LD      (HL),A              ; ... init flag
008B: C9              RET                         ; Back to 6D and out

FindDat: 
; Return 2-byte command descriptor for voice in A.
; Return in HL
008C: 47              LD      B,A                 ; Voice number to B (1,2, or 3)
008D: 21 3E 40        LD      HL,$403E            ; Pointer to voice commands
0090: 11 02 00        LD      DE,$0002            ; 2 bytes each
0093: 19              ADD     HL,DE               ; Find the ...
0094: 10 FD           DJNZ    $93                 ; {} ... 2 byte pointer
0096: C9              RET                         ; Done

CmdRequest: 
; Process a command request. Request is in A. The lowest priority voice is 
; preempted with the request if the request is higher priority. Otherwise the
; request is ignored.
0097: 32 46 40        LD      ($4046),A           ; {ram.cmdRequest} Hold requested command
009A: CD E6 00        CALL    $00E6               ; {code.ReinitCommand} Reinit command if running
009D: D8              RET     C                   ; Command now running ... out
009E: CD E6 00        CALL    $00E6               ; {code.ReinitCommand} If not found, A=0. So look for a idle voice
00A1: 38 38           JR      C,$DB               ; {} Found idle voice ... use it
00A3: 3A 40 40        LD      A,($4040)           ; {ram.v1Command} Voice 1 command
00A6: CD 02 01        CALL    $0102               ; {code.GetComPriority} Priority of current ...
00A9: 47              LD      B,A                 ; ... voice 1 command to B
00AA: 3A 42 40        LD      A,($4042)           ; {ram.v2Command} Priority of  ...
00AD: CD 02 01        CALL    $0102               ; {code.GetComPriority} ... current ...
00B0: 4F              LD      C,A                 ; ... voice 2 command to C
00B1: 3A 44 40        LD      A,($4044)           ; {ram.v3Command} Priority of ...
00B4: CD 02 01        CALL    $0102               ; {code.GetComPriority} ... current ...
00B7: 32 49 40        LD      ($4049),A           ; {ram.v3priority} ... voice 3 command to 4049
00BA: 3A 46 40        LD      A,($4046)           ; {ram.cmdRequest} Requested command
00BD: CD 02 01        CALL    $0102               ; {code.GetComPriority} Priority of requested command ...
00C0: 5F              LD      E,A                 ; ... to E
00C1: 21 49 40        LD      HL,$4049            ; Voice 3 priority ...
00C4: 56              LD      D,(HL)              ; ... E (B=1, C=2, D=3, E=requested)

; Find lowest priority command (will be the lowest number) and replace (if request is higher)
00C5: 78              LD      A,B                 ; Compare ...
00C6: B9              CP      C                   ; ... voice 1 and 2 (A-C)
00C7: 38 01           JR      C,$CA               ; {} Voice 1 value is lower than 2 ... continue with 1
00C9: 79              LD      A,C                 ; Voice 2 value is lower ... continue with 2
00CA: BA              CP      D                   ; Comapre lowest so far with voice 3
00CB: 38 01           JR      C,$CE               ; {} The lowest is still lowest ... continue with it
00CD: 7A              LD      A,D                 ; Voice 3 is the lowest ... continue with voice 3
00CE: BB              CP      E                   ; Compare lowest so far with requested voice
00CF: D0              RET     NC                  ; All current commands are higher priority ... ignore
;
00D0: 1E 01           LD      E,$01               ; Are we replacing ...
00D2: B8              CP      B                   ; ... voice 1?
00D3: 28 05           JR      Z,$DA               ; {} Yes ... E is 1
00D5: 1C              INC     E                   ; Are we replacing ...
00D6: B9              CP      C                   ; ... voice 2?
00D7: 28 01           JR      Z,$DA               ; {} Yes ... E is 2
00D9: 1C              INC     E                   ; Must be replacing voice 3
00DA: 7B              LD      A,E                 
;
00DB: CD 8C 00        CALL    $008C               ; {code.FindDat} Find voice structure
00DE: 3A 46 40        LD      A,($4046)           ; {ram.cmdRequest} Store command ...
00E1: 77              LD      (HL),A              ; ... in structure
00E2: 23              INC     HL                  ; Flag init ...
00E3: 36 00           LD      (HL),$00            ; ... needs doing
00E5: C9              RET                         ; Out

ReinitCommand: 
00E6: 0E 01           LD      C,$01               ; Voice number 1
00E8: 21 40 40        LD      HL,$4040            ; Voice 1's data
00EB: BE              CP      (HL)                ; Is this command already running?
00EC: 28 0E           JR      Z,$FC               ; {} Yes ... just reinit it
00EE: 0C              INC     C                   ; ...
00EF: 23              INC     HL                  ; Check all 3 voices ...
00F0: 23              INC     HL                  ; ... and reinit if found
00F1: BE              CP      (HL)                ; ...
00F2: 28 08           JR      Z,$FC               ; {} ...
00F4: 0C              INC     C                   ; ...
00F5: 23              INC     HL                  ; ...
00F6: 23              INC     HL                  ; ...
00F7: BE              CP      (HL)                ; ...
00F8: 28 02           JR      Z,$FC               ; {} ...
00FA: AF              XOR     A                   ; C=0 ... not found
00FB: C9              RET                         ; Done
;
00FC: 23              INC     HL                  ; Point to init flag
00FD: 36 00           LD      (HL),$00            ; Flag the command for initialize
00FF: 79              LD      A,C                 ; Found voice number
0100: 37              SCF                         ; Flag found
0101: C9              RET                         ; Done

GetComPriority: 
; Command number in A, return priority in A
0102: 21 83 02        LD      HL,$0283            ; Priority table
0105: 5F              LD      E,A                 ; Convert A ...
0106: 16 00           LD      D,$00               ; ... to 16 bit value in DE
0108: 19              ADD     HL,DE               ; Offset
0109: 7E              LD      A,(HL)              ; Get command priority
010A: C9              RET                         ; Return in A

; Initialization continues here
010B: 70              LD      (HL),B              ; Clear ...
010C: 23              INC     HL                  ; ... RAM ...
010D: 7C              LD      A,H                 ; ... from 4000 ...
010E: D6 44           SUB     $44                 ; ... to ...
0110: 20 F9           JR      NZ,$10B             ; {} ... 4400
0112: F9              LD      SP,HL               ; Set SP to 4400
0113: 3D              DEC     A                   ; FF
0114: 32 80 42        LD      ($4280),A           ; {ram.m4280} Disable sound processing
0117: ED 56           IM      1                   ; Interrupt mode 1 (everything goes to 0038)
0119: 11 3F 00        LD      DE,$003F            ; D=0 (all off) then E=3F ...
011C: CD 6D 02        CALL    $026D               ; {code.AYEnable} ... port A and B inputs, all noise and voice off
011F: 3E 08           LD      A,$08               ; Amplitude A register
0121: 06 00           LD      B,$00               ; 0
0123: CF              RST     $08                 ; Set voice A amplitude to 0
0124: 3E 09           LD      A,$09               ; Amplitude B register
0126: CF              RST     $08                 ; Set voice B amplitude to 0
0127: 3E 0A           LD      A,$0A               ; Amplitude C register
0129: CF              RST     $08                 ; Set voice C amplitude to 0
012A: 3E 07           LD      A,$07               ; ? We just set this ...
012C: 06 3F           LD      B,$3F               ; ... in the call to ...
012E: CF              RST     $08                 ; ... 026D above ?
012F: 21 00 60        LD      HL,$6000            ; Current capacitor filter value (none)
0132: 22 4E 40        LD      ($404E),HL          ; {ram.curFilter} Hold current
0135: 77              LD      (HL),A              ; Set the capacitor network hardware
```

# Main Loop

```code

;
; Commands are processed for all three voices one by one. Interrupts are turned on for a
; brief time between voices to allow new commands to come in. Each voice has a two-byte
; pointer. The first byte is the command number (0 for none). The second byte is the
; init flag. If the init flag is 0 then the loop calls the command's init function and sets
; the flag. Otherwise the continuation command is called each pass until a return of not-0
; marks the end of the command. Then the structure is cleared.
;
; Through experimentation and MAME code it appears bit 4 changes with the master clock divided
; by 1280. Thus 1789750 / 1280 = 1398.24 Hz. The main loop divides that by two. Yielding
; a sound tick of 700Hz.

MainLoop: 

0136: FB              EI                          ; Enable interrupts
0137: 21 3F 40        LD      HL,$403F            ; 700Hz timer value ...
013A: 34              INC     (HL)                ; ... is never used
013B: 3E 0F           LD      A,$0F               ; Register IO port B (timing tick)
013D: CD C1 02        CALL    $02C1               ; {code.ReadAY} Read IO port B
0140: E6 08           AND     $08                 ; Watch for bit 4
0142: 20 F7           JR      NZ,$13B             ; {} Not a 0 ... wait until 0
;
0144: 3E 0F           LD      A,$0F               ; Now wait ...
0146: CD C1 02        CALL    $02C1               ; {code.ReadAY} ... for ...
0149: E6 08           AND     $08                 ; ... bit to ...
014B: 28 F7           JR      Z,$144              ; {} ... go to 1
;
014D: F3              DI                          ; Interrupts off
014E: 3E 01           LD      A,$01               ; Start with ...
0150: 32 4B 40        LD      ($404B),A           ; {ram.voiceNum} ... voice 1
0153: 21 41 40        LD      HL,$4041            ; Get ...
0156: 7E              LD      A,(HL)              ; ... init flag
0157: 2B              DEC     HL                  ; Point to command
0158: B7              OR      A                   ; This command has been initialized?
0159: 28 30           JR      Z,$18B              ; {} No ... go do it
015B: 7E              LD      A,(HL)              ; Get command number
015C: CD E8 01        CALL    $01E8               ; {code.VCommandCont} Do continuation command
015F: FB              EI                          ; Interrupts on
0160: 00              NOP                         ; For ...
0161: 00              NOP                         ; ... just ...
0162: 00              NOP                         ; ... an instant
0163: F3              DI                          ; Interrupts back off
;
0164: 21 4B 40        LD      HL,$404B            ; Now for ...
0167: 34              INC     (HL)                ; ... voice 2
0168: 21 43 40        LD      HL,$4043            ; Get ...
016B: 7E              LD      A,(HL)              ; ... init flag
016C: 2B              DEC     HL                  ; Point to command
016D: B7              OR      A                   ; This command has been initialized?
016E: 28 21           JR      Z,$191              ; {} No ... go do it
0170: 7E              LD      A,(HL)              ; Get command number
0171: CD E8 01        CALL    $01E8               ; {code.VCommandCont} Do continuation command
0174: FB              EI                          ; Interrupts on
0175: 00              NOP                         ; For ...
0176: 00              NOP                         ; ... just ...
0177: 00              NOP                         ; ... an instance
0178: F3              DI                          ; Interrupts back off
;
0179: 21 4B 40        LD      HL,$404B            ; And finally ...
017C: 34              INC     (HL)                ; ... voice 3
017D: 21 45 40        LD      HL,$4045            ; Get ...
0180: 7E              LD      A,(HL)              ; ... init flag
0181: 2B              DEC     HL                  ; Point to command
0182: B7              OR      A                   ; This command has been initialized?
0183: 28 12           JR      Z,$197              ; {} No ... go do it
0185: 7E              LD      A,(HL)              ; Get command number
0186: CD E8 01        CALL    $01E8               ; {code.VCommandCont} Do continuation command
0189: 18 AB           JR      $136                ; {code.MainLoop} Back to top of loop
;
018B: 7E              LD      A,(HL)              ; Get command number
018C: CD D9 01        CALL    $01D9               ; {code.VCommandInit} Do the initialization command
018F: 18 CE           JR      $15F                ; {} Back to voice 2
;
0191: 7E              LD      A,(HL)              ; Get command number
0192: CD D9 01        CALL    $01D9               ; {code.VCommandInit} Do the initialization command
0195: 18 DD           JR      $174                ; {} Back to voice 3
;
0197: 7E              LD      A,(HL)              ; Get command number
0198: CD D9 01        CALL    $01D9               ; {code.VCommandInit} Do the initialization command
019B: 18 99           JR      $136                ; {code.MainLoop} Back to the top of the loop

JumpTabler: 
; Look up address in jump table and jump to it.
; A = entry number
; HL = table
019D: 87              ADD     A,A                 ; Two bytes per address
019E: 5F              LD      E,A                 ; LSB
019F: 16 00           LD      D,$00               ; MSB is 0
01A1: 19              ADD     HL,DE               ; Add offset to table pointer
01A2: 5E              LD      E,(HL)              ; Get LSB from table
01A3: 23              INC     HL                  ; Get ...
01A4: 56              LD      D,(HL)              ; ... MSB from table
01A5: EB              EX      DE,HL               ; Address to HL
01A6: E9              JP      (HL)                ; Take the jump
```

# Command Init Functions

```code
CommandInit: 
; These functions are called once to initialize a voice function. After that the
; corresponding continue-function is called each pass.
; Shown with priorities (higher the number, higher the priority -- 18 hopping cannot be interrupted)
01A7: 9C 02 ; 00 I00 Shutdown voice
01A9: 0F 03 ; 05 I01 Coin inserted
01AB: BD 03 ; 0A I02 Die in water
01AD: 5D 04 ; 0D I03 Die in road
01AF: 82 14 ; 18 I04 Frog hopping
01B1: 65 14 ; 07 I05 Time running out
01B3: 9D 0B ; 0E I06 Next life begins  
01B5: 8D 04 ; 0C I07 Extra frog
01B7: 67 0B ; 06 I08 Music interlude after getting frog home (changes each frog)
01B9: 7F 07 ; 15 I09 Music main song intro (1st 16 beats)
01BB: 8B 07 ; 14 I0A Music voice B
01BD: 8E 07 ; 13 I0B Music voice C
01BF: B0 0A ; 10 I0C Music game over song   
01C1: C4 0A ; 0F I0D Music voice B
01C3: 8C 0B ; 04 I0E Music voice B        
01C5: 15 10 ; 16 I0F Main song after intro
01C7: EB 06 ; 03 I10 Frogger landing safe
01C9: 3B 0B ; 12 I11 Music level complete          
01CB: 53 0B ; 11 I12 Music voice B              
01CD: 5D 0B ; 02 I13 Music voice C               
01CF: 00 00 ; 09 I14 Reset program
01D1: 05 05 ; 08 I15 Snake on the ground  
01D3: 23 10 ; 01 I16 Music voice B
01D5: C3 05 ; 16 I17 Race car           
01D7: 3D 06 ; 17 I18 Pick up mate

VCommandInit: 
; Call the initialization function for a voice command
01D9: 21 A7 01        LD      HL,$01A7            ; Initialization functions
01DC: CD 9D 01        CALL    $019D               ; {code.JumpTabler} Do initialization function
01DF: 3A 4B 40        LD      A,($404B)           ; {ram.voiceNum} Voice number
01E2: CD 8C 00        CALL    $008C               ; {code.FindDat} Get the voice command structure
01E5: 23              INC     HL                  ; Point to voice's init flag
01E6: 77              LD      (HL),A              ; Mark initialized (happens to be voice number)
01E7: C9              RET                         ; Done

VCommandCont: 
; Call the continuation function for a voice command
01E8: B7              OR      A                   ; Entry valid?
01E9: C8              RET     Z                   ; No ... ignore
01EA: 21 25 02        LD      HL,$0225            ; Return address right after table
01ED: E5              PUSH    HL                  ; Push return
01EE: 21 F3 01        LD      HL,$01F3            ; Jump table of commands
01F1: 18 AA           JR      $19D                ; {code.JumpTabler} Take the jump
```

# Command Continue Functions

```code
CommandCont: 
; These functions are called to continue a voice command each pass. They return 0 to continue or
; not-zero to terminate the continuation.
01F3: 33 00 ; C00 Set A to FF, but never used because of check at 1E9
01F5: 33 03 ; C01 effect Coin inserted                      
01F7: D2 03 ; C02 effect Die in water
01F9: 75 04 ; C03 effect Die in road                        
01FB: 8C 14 ; C04 effect Frog hopping                        
01FD: 72 14 ; C05 effect Time running out
01FF: A7 0B ; C06 song Next life begins                        
0201: AA 04 ; C07 effect Extra frog                        
0203: 8F 0B ; C08 song Interlude after getting frog home (20 tunes, changes each frog)                      
0205: 91 07 ; C09 Main song intro (1st 16 beats)                           
0207: 97 07 ; C0A Music voice B
0209: 9D 07 ; C0B Music voice C                            
020B: BD 0A ; C0C Game over song                 
020D: C7 0A ; C0D Music voice B                  
020F: 96 0B ; C0E Music voice B                     
0211: 26 10 ; C0F Main song after intro                 
0213: 0E 07 ; C10 effect Frogger landing safe                 
0215: 4C 0B ; C11 song Level complete
0217: 56 0B ; C12 Music voice B                    
0219: 60 0B ; C13 Music voice C                       
021B: 00 00 ; C14 Reset program                                   
021D: 1C 05 ; C15 effect Snake on ground                         
021F: 2D 10 ; C16 Music voice B
0221: E5 05 ; C17 effect Race car                         
0223: 61 06 ; C18 effect Pick up mate

; All continuation functions RET here
0225: B7              OR      A                   ; Return "continue"?
0226: C8              RET     Z                   ; Yes ... out
0227: CD 9C 02        CALL    $029C               ; {code.ShutdownVoice} Not "continue" ... shutdown voice
022A: 3A 4B 40        LD      A,($404B)           ; {ram.voiceNum} Voice number
022D: C3 84 00        JP      $0084               ; {} Clear out 2-byte voice command (with 0,0)

AmplitudeOff: 
0230: 3A 4B 40        LD      A,($404B)           ; {ram.voiceNum} Voice number
0233: E6 03           AND     $03                 ; Is it valid?
0235: C8              RET     Z                   ; No ... skip
0236: C6 07           ADD     A,$07               ; Offset to amplitude register
0238: 06 00           LD      B,$00               ; Value 0 (silence)
023A: CF              RST     $08                 ; Write to AY
023B: C9              RET                         ; Done

WriteTune: 
; Write HL to voice's coarse/fine reigsters
023C: 3A 4B 40        LD      A,($404B)           ; {ram.voiceNum} Voice number (1,2, or 3)
023F: 3D              DEC     A                   ; Make it 0 based
0240: 87              ADD     A,A                 ; Voice * 2
0241: 47              LD      B,A                 ; To B
0242: CD 09 03        CALL    $0309               ; {code.WriteAYAL} Write L to voice's fine register
0245: 04              INC     B                   ; Bump to ...
0246: 78              LD      A,B                 ; ... coarse register
0247: D3 80           OUT     ($80),A             ; {hard.AY_ADDR} Write register address
0249: 7C              LD      A,H                 ; Coarse value
024A: D3 40           OUT     ($40),A             ; {hard.AY_DATA} Write coarse value
024C: C9              RET                         ; Done

ReadTune: 
; Read voice's coarse/fine registers to HL
024D: 3A 4B 40        LD      A,($404B)           ; {ram.voiceNum} Voice number (1,3, or 3)
0250: 3D              DEC     A                   ; Make it 0 based
0251: 87              ADD     A,A                 ; Voiced * 2
0252: 47              LD      B,A                 ; To B
0253: D3 80           OUT     ($80),A             ; {hard.AY_ADDR} Latch address
0255: DB 40           IN      A,($40)             ; {hard.AY_DATA} Read fine value
0257: 6F              LD      L,A                 ; To L
0258: 04              INC     B                   ; Bump to ...
0259: 78              LD      A,B                 ; ... coarse register
025A: D3 80           OUT     ($80),A             ; {hard.AY_ADDR} Latch address
025C: DB 40           IN      A,($40)             ; {hard.AY_DATA} Read coarse value
025E: 67              LD      H,A                 ; To H
025F: C9              RET                         ; Done

EnableTone: 
; Sets a voice to TONE and disables NOISE. 
0260: 11 04 7F        LD      DE,$7F04            ; One 0 in AND and one 1 in OR
0263: 3A 4B 40        LD      A,($404B)           ; {ram.voiceNum} Roll the one target bit ...
0266: 47              LD      B,A                 ; ... to the propper ...
0267: CB 02           RLC     D                   ; ... spot
0269: CB 03           RLC     E                   ; ...
026B: 10 FA           DJNZ    $267                ; {} ...

AYEnable: 
; Current value is ANDed with D
; and then ORed with E
026D: 3E 07           LD      A,$07               ; The ENABLE register
026F: D3 80           OUT     ($80),A             ; {hard.AY_ADDR} Select register in AY chip
0271: 3A 4C 40        LD      A,($404C)           ; {ram.curEnable} Get current enable value
0274: A2              AND     D                   ; Mask bits off
0275: B3              OR      E                   ; OR bits on
0276: 32 4C 40        LD      ($404C),A           ; {ram.curEnable} New enable value
0279: D3 40           OUT     ($40),A             ; {hard.AY_DATA} Write value to AY chip
027B: C9              RET                         ; Done

SetAmplitude: 
; Set the voice's amplitude to B
027C: 3A 4B 40        LD      A,($404B)           ; {ram.voiceNum} Voice number
027F: C6 07           ADD     A,$07               ; Offset to amplitude register
0281: CF              RST     $08                 ; Write B to voice's amplitude
0282: C9              RET                         ; Done
```

# Command Priorities

```code
CommandPriority: 
; One value (0-18) for each command number (0-18). The higher the number the
; higher the prioirty. Nobody can preempt command 4 (frog hopping).
;      0  1  2  3  4  5  6  7  8  9  A  B  C  D  E  F 10 11 12 13 14 15 16 17 18
0283: 00 05 0A 0D 18 07 0E 0C 06 15 14 13 10 0F 04 16 03 12 11 02 09 08 01 16 17             

ShutdownVoice: 
;I00 Shutdown
; Disable TONE and NOISe on a voice, set amplitude to 0, and remove cap filtering.    
029C: 3A 4B 40        LD      A,($404B)           ; {ram.voiceNum} Voice number
029F: 47              LD      B,A                 ; Copy to B
02A0: 3E 84           LD      A,$84               ; 10000100
02A2: 07              RLCA                        ; Shift bits
02A3: 10 FD           DJNZ    $2A2                ; {} Build OR part of enable
02A5: 5F              LD      E,A                 ; Hold in E
02A6: 16 FF           LD      D,$FF               ; AND part of enable ... leave everything alone
02A8: CD 6D 02        CALL    $026D               ; {code.AYEnable} Turn off a voice (NOISE and TONE)
02AB: CD 30 02        CALL    $0230               ; {code.AmplitudeOff} Turn off voice amplitude
02AE: 18 17           JR      $2C7                ; {code.Filter00} Set voice's cap filtering to "none"

EnableNoise: 
; Sets a voice to NOISE and disables TONE. 
02B0: 11 80 FB        LD      DE,$FB80            ; Rotate bit pattern
02B3: 18 AE           JR      $263                ; {} Continue with mask and set

WriteAYR: 
; Here is yet another way to write to the AY register. Why would a caller prefer this
; instead of RST 08 directly?
02B5: CF              RST     $08                 ; Write B to A
02B6: C9              RET                         ; Out

ReadAmplitude: 
02B7: 3A 4B 40        LD      A,($404B)           ; {ram.voiceNum} Voice number
02BA: E6 03           AND     $03                 ; Any requested?
02BC: C8              RET     Z                   ; No ... skip
02BD: C6 07           ADD     A,$07               ; Offset to amplitude
02BF: 18 00           JR      $2C1                ; {code.ReadAY} Read voice's amplitude register

ReadAY: 
; Read AY register (A) to B (and A).
02C1: D3 80           OUT     ($80),A             ; {hard.AY_ADDR} Latch the address
02C3: DB 40           IN      A,($40)             ; {hard.AY_DATA} Read the value
02C5: 47              LD      B,A                 ; To B ... not sure why ... we already mangled A
02C6: C9              RET                         ; Done

Filter00: 
; Remove all capacitor filtering from voice
02C7: 01 00 00        LD      BC,$0000            ; OR mask ... all 0's here
;
02CA: 11 FF FC        LD      DE,$FCFF            ; 11111100 11111111
02CD: 3A 4B 40        LD      A,($404B)           ; {ram.voiceNum} Voice number
02D0: FE 02           CP      $02                 ; Is it voice 2?
02D2: 28 15           JR      Z,$2E9              ; {} Yes ... DE is good
02D4: 38 08           JR      C,$2DE              ; {} 3 ... go handle that
;
02D6: 16 F3           LD      D,$F3               ; 11110011 11111111
02D8: CB 00           RLC     B                   ; Shift OR mask left 2 ..
02DA: CB 00           RLC     B                   ; ....xx.. ........
02DC: 18 0B           JR      $2E9                ; {} Continue
;
02DE: 11 3F FF        LD      DE,$FF3F            ; 11111111 00111111
02E1: CB 38           SRL     B                   ; Shift OR mask right 2 ...
02E3: CB 19           RR      C                   ; ........ xx......
02E5: CB 38           SRL     B                   ; ...
02E7: CB 19           RR      C                   ; ...
;
02E9: 2A 4E 40        LD      HL,($404E)          ; {ram.curFilter} Current value of capacitor filter
02EC: 7C              LD      A,H                 ; Mask for requested voice ...
02ED: A2              AND     D                   ; ...
02EE: B0              OR      B                   ; ...
02EF: 67              LD      H,A                 ; ...
02F0: 7D              LD      A,L                 ; ...
02F1: A3              AND     E                   ; ...
02F2: B1              OR      C                   ; ...
02F3: 6F              LD      L,A                 ; ...
02F4: 22 4E 40        LD      ($404E),HL          ; {ram.curFilter} New capacitor filter value
02F7: 77              LD      (HL),A              ; Change hardware
02F8: C9              RET                         ; Done

Filter11: 
; Set 0.047uF + 0.220uF
02F9: 01 00 03        LD      BC,$0300            ; Turn on ...
02FC: C3 CA 02        JP      $02CA               ; {} ... both caps

Filter01: 
; Set 0.220uF
02FF: 01 00 01        LD      BC,$0100            ; Turn on ...
0302: 18 C6           JR      $2CA                ; {} ... one cap

Filter10: 
; Set 0.047uF
0304: 01 00 02        LD      BC,$0200            ; Turn on ...
0307: 18 C1           JR      $2CA                ; {} ... one cap

WriteAYAL: 
; Another write-to-AY
; A is register, L is value
0309: D3 80           OUT     ($80),A             ; {hard.AY_ADDR} Write address
030B: 7D              LD      A,L                 ; Write ...
030C: D3 40           OUT     ($40),A             ; {hard.AY_DATA} ... value
030E: C9              RET                         ; Out
```

## Insert Coin Sound

[insertCoin.mp3](sounds/insertCoin.mp3)

```code
;I01 Coin inserted
030F: E7              RST     $20                 
0310: 3E 20           LD      A,$20               
0312: 21 60 40        LD      HL,$4060            
0315: 77              LD      (HL),A              
0316: 3E 03           LD      A,$03               
0318: 23              INC     HL                  
0319: 77              LD      (HL),A              
031A: 3E 14           LD      A,$14               
031C: 23              INC     HL                  
031D: 77              LD      (HL),A              
031E: 3E 01           LD      A,$01               
0320: 23              INC     HL                  
0321: 77              LD      (HL),A              
0322: AF              XOR     A                   
0323: 23              INC     HL                  
0324: 77              LD      (HL),A              
0325: 21 10 00        LD      HL,$0010            
0328: 22 65 40        LD      ($4065),HL          ; {ram.m4065}
032B: 2E 20           LD      L,$20               
032D: EF              RST     $28                 
032E: F7              RST     $30                 
032F: 06 09           LD      B,$09               
0331: DF              RST     $18                 
0332: C9              RET                         
;
;C01 Coin inserted
0333: 3A 64 40        LD      A,($4064)           ; {ram.m4064}
0336: A7              AND     A                   
0337: 28 0D           JR      Z,$346              ; {}
0339: FE 01           CP      $01                 
033B: 28 1F           JR      Z,$35C              ; {}
033D: FE 03           CP      $03                 
033F: 38 2B           JR      C,$36C              ; {}
0341: 28 49           JR      Z,$38C              ; {}
0343: C3 71 06        JP      $0671               ; {}
0346: 21 60 40        LD      HL,$4060            
0349: 35              DEC     (HL)                
034A: 20 6F           JR      NZ,$3BB             ; {}
034C: 36 20           LD      (HL),$20            
034E: D7              RST     $10                 
034F: 3D              DEC     A                   
0350: 28 04           JR      Z,$356              ; {}
0352: 47              LD      B,A                 
0353: DF              RST     $18                 
0354: 18 65           JR      $3BB                ; {}
0356: 21 64 40        LD      HL,$4064            
0359: 34              INC     (HL)                
035A: 18 F6           JR      $352                ; {}
035C: 21 00 03        LD      HL,$0300            
035F: 22 67 40        LD      ($4067),HL          ; {ram.m4067}
0362: EF              RST     $28                 
0363: 06 08           LD      B,$08               
0365: DF              RST     $18                 
0366: 21 64 40        LD      HL,$4064            
0369: 34              INC     (HL)                
036A: 18 4F           JR      $3BB                ; {}
036C: 21 61 40        LD      HL,$4061            
036F: 35              DEC     (HL)                
0370: 20 49           JR      NZ,$3BB             ; {}
0372: 36 03           LD      (HL),$03            
0374: CD 4D 02        CALL    $024D               ; {code.ReadTune}
0377: B7              OR      A                   
0378: 11 08 00        LD      DE,$0008            
037B: ED 52           SBC     HL,DE               
037D: EF              RST     $28                 
037E: 21 62 40        LD      HL,$4062            
0381: 35              DEC     (HL)                
0382: 20 37           JR      NZ,$3BB             ; {}
0384: 36 14           LD      (HL),$14            
0386: 21 64 40        LD      HL,$4064            
0389: 34              INC     (HL)                
038A: 18 2F           JR      $3BB                ; {}
038C: 21 63 40        LD      HL,$4063            
038F: 35              DEC     (HL)                
0390: 20 1D           JR      NZ,$3AF             ; {}
0392: 36 01           LD      (HL),$01            
0394: B7              OR      A                   
0395: 2A 67 40        LD      HL,($4067)          ; {ram.m4067}
0398: 11 20 00        LD      DE,$0020            
039B: ED 52           SBC     HL,DE               
039D: 22 67 40        LD      ($4067),HL          ; {ram.m4067}
03A0: EF              RST     $28                 
03A1: 2A 65 40        LD      HL,($4065)          ; {ram.m4065}
03A4: 2B              DEC     HL                  
03A5: 7D              LD      A,L                 
03A6: B4              OR      H                   
03A7: 20 0B           JR      NZ,$3B4             ; {}
03A9: 21 64 40        LD      HL,$4064            
03AC: 34              INC     (HL)                
03AD: 18 0C           JR      $3BB                ; {}
03AF: 2A 67 40        LD      HL,($4067)          ; {ram.m4067}
03B2: 18 EC           JR      $3A0                ; {}
03B4: 22 65 40        LD      ($4065),HL          ; {ram.m4065}
03B7: 21 64 40        LD      HL,$4064            
03BA: 35              DEC     (HL)                
03BB: AF              XOR     A                   
03BC: C9              RET                         
```

## Die in the Water Sound

[dieWater.mp3](sounds/dieWater.mp3)

(Don't frogs swim?)

```code
;I02 Die in water
03BD: 3E 80           LD      A,$80               
03BF: 32 5D 40        LD      ($405D),A           ; {ram.m405D}
03C2: 06 0E           LD      B,$0E               
03C4: CD 7C 02        CALL    $027C               ; {code.SetAmplitude}
03C7: 21 70 00        LD      HL,$0070            
03CA: CD 3C 02        CALL    $023C               ; {code.WriteTune}
03CD: F7              RST     $30                 
03CE: CD 04 03        CALL    $0304               ; {code.Filter10} Set filtering 0.047uF
03D1: C9              RET                         
;
;C02 Die in water
03D2: 3A 5D 40        LD      A,($405D)           ; {ram.m405D}
03D5: 3D              DEC     A                   
03D6: 32 5D 40        LD      ($405D),A           ; {ram.m405D}
03D9: 28 25           JR      Z,$400              ; {}
03DB: FE FF           CP      $FF                 
03DD: 28 3A           JR      Z,$419              ; {}
03DF: FE 20           CP      $20                 
03E1: 38 0A           JR      C,$3ED              ; {}
03E3: FE 30           CP      $30                 
03E5: 38 0C           JR      C,$3F3              ; {}
03E7: FE 70           CP      $70                 
03E9: 38 02           JR      C,$3ED              ; {}
03EB: AF              XOR     A                   
03EC: C9              RET                         
03ED: 06 00           LD      B,$00               
03EF: CD 7C 02        CALL    $027C               ; {code.SetAmplitude}
03F2: C9              RET                         
03F3: 21 3C 00        LD      HL,$003C            
03F6: CD 3C 02        CALL    $023C               ; {code.WriteTune}
03F9: 06 0B           LD      B,$0B               
03FB: CD 7C 02        CALL    $027C               ; {code.SetAmplitude}
03FE: AF              XOR     A                   
03FF: C9              RET                         
0400: CD 04 03        CALL    $0304               ; {code.Filter10}
0403: 3E 80           LD      A,$80               
0405: 32 5E 40        LD      ($405E),A           ; {ram.m405E}
0408: 06 0A           LD      B,$0A               
040A: CD 7C 02        CALL    $027C               ; {code.SetAmplitude}
040D: 21 FC 00        LD      HL,$00FC            
0410: CD 3C 02        CALL    $023C               ; {code.WriteTune}
0413: F7              RST     $30                 
0414: AF              XOR     A                   
0415: 32 5D 40        LD      ($405D),A           ; {ram.m405D}
0418: C9              RET                         
0419: 3A 5E 40        LD      A,($405E)           ; {ram.m405E}
041C: 3D              DEC     A                   
041D: 32 5E 40        LD      ($405E),A           ; {ram.m405E}
0420: FE 41           CP      $41                 
0422: 38 0B           JR      C,$42F              ; {}
0424: CD 4D 02        CALL    $024D               ; {code.ReadTune}
0427: 2D              DEC     L                   
0428: 2D              DEC     L                   
0429: EF              RST     $28                 
042A: AF              XOR     A                   
042B: 32 5D 40        LD      ($405D),A           ; {ram.m405D}
042E: C9              RET                         
042F: FE 40           CP      $40                 
0431: 28 0E           JR      Z,$441              ; {}
0433: B7              OR      A                   
0434: 28 11           JR      Z,$447              ; {}
0436: CD 4D 02        CALL    $024D               ; {code.ReadTune}
0439: 2C              INC     L                   
043A: 2C              INC     L                   
043B: EF              RST     $28                 
043C: AF              XOR     A                   
043D: 32 5D 40        LD      ($405D),A           ; {ram.m405D}
0440: C9              RET                         
0441: D7              RST     $10                 
0442: 05              DEC     B                   
0443: DF              RST     $18                 
0444: C3 33 04        JP      $0433               ; {}
0447: D7              RST     $10                 
0448: 05              DEC     B                   
0449: 28 0F           JR      Z,$45A              ; {}
044B: DF              RST     $18                 
044C: 21 00 00        LD      HL,$0000            
044F: CD 3C 02        CALL    $023C               ; {code.WriteTune}
0452: 3E 80           LD      A,$80               
0454: 32 5E 40        LD      ($405E),A           ; {ram.m405E}
0457: C3 19 04        JP      $0419               ; {}
045A: 3E FF           LD      A,$FF               
045C: C9              RET                         
```

## Die in the Road Sound

[dieRoad.mp3](sounds/dieRoad.mp3)

```code
;I03 Die in road
045D: CD C7 02        CALL    $02C7               ; {code.Filter00}
0460: CD 60 02        CALL    $0260               ; {code.EnableTone}
0463: 21 00 01        LD      HL,$0100            
0466: CD 3C 02        CALL    $023C               ; {code.WriteTune}
0469: 06 0A           LD      B,$0A               
046B: CD 7C 02        CALL    $027C               ; {code.SetAmplitude}
046E: 21 90 02        LD      HL,$0290            
0471: 22 30 41        LD      ($4130),HL          ; {ram.m4130}
0474: C9              RET                         
;
;C03 Die in road
0475: 2A 30 41        LD      HL,($4130)          ; {ram.m4130}
0478: 2B              DEC     HL                  
0479: 22 30 41        LD      ($4130),HL          ; {ram.m4130}
047C: 7C              LD      A,H                 
047D: B5              OR      L                   
047E: 3E FF           LD      A,$FF               
0480: C8              RET     Z                   
0481: CD 4D 02        CALL    $024D               ; {code.ReadTune}
0484: 11 03 00        LD      DE,$0003            
0487: 19              ADD     HL,DE               
0488: CD 3C 02        CALL    $023C               ; {code.WriteTune}
048B: AF              XOR     A                   
048C: C9              RET                         
```

## Free Life Sound

[freeLife.mp3](sounds/freeLife.mp3)

```code
;I07 Extra frog
048D: E7              RST     $20                 
048E: 3E 08           LD      A,$08               
0490: 32 70 41        LD      ($4170),A           ; {ram.m4170}
0493: 3E 0C           LD      A,$0C               
0495: 32 71 41        LD      ($4171),A           ; {ram.m4171}
0498: 3E 10           LD      A,$10               
049A: 32 72 41        LD      ($4172),A           ; {ram.m4172}
049D: AF              XOR     A                   
049E: 32 73 41        LD      ($4173),A           ; {ram.m4173}
04A1: 21 50 00        LD      HL,$0050            
04A4: EF              RST     $28                 
04A5: F7              RST     $30                 
04A6: 06 00           LD      B,$00               
04A8: DF              RST     $18                 
04A9: C9              RET                         
;
;C07 Extra frog
04AA: 3A 73 41        LD      A,($4173)           ; {ram.m4173}
04AD: A7              AND     A                   
04AE: 28 17           JR      Z,$4C7              ; {}
04B0: FE 01           CP      $01                 
04B2: 28 21           JR      Z,$4D5              ; {}
04B4: FE 03           CP      $03                 
04B6: 38 22           JR      C,$4DA              ; {}
04B8: 28 2C           JR      Z,$4E6              ; {}
04BA: 21 72 41        LD      HL,$4172            
04BD: 35              DEC     (HL)                
04BE: 3E FF           LD      A,$FF               
04C0: C8              RET     Z                   
04C1: AF              XOR     A                   
04C2: 32 73 41        LD      ($4173),A           ; {ram.m4173}
04C5: AF              XOR     A                   
04C6: C9              RET                         
04C7: D7              RST     $10                 
04C8: 3C              INC     A                   
04C9: FE 0D           CP      $0D                 
04CB: 20 04           JR      NZ,$4D1             ; {}
04CD: 21 73 41        LD      HL,$4173            
04D0: 34              INC     (HL)                
04D1: 47              LD      B,A                 
04D2: DF              RST     $18                 
04D3: 18 F0           JR      $4C5                ; {}
04D5: CD EB 04        CALL    $04EB               ; {}
04D8: 18 EB           JR      $4C5                ; {}
04DA: D7              RST     $10                 
04DB: 3D              DEC     A                   
04DC: 20 04           JR      NZ,$4E2             ; {}
04DE: 21 73 41        LD      HL,$4173            
04E1: 34              INC     (HL)                
04E2: 47              LD      B,A                 
04E3: DF              RST     $18                 
04E4: 18 DF           JR      $4C5                ; {}
04E6: CD F8 04        CALL    $04F8               ; {}
04E9: 18 DA           JR      $4C5                ; {}
04EB: 21 70 41        LD      HL,$4170            
04EE: 35              DEC     (HL)                
04EF: C0              RET     NZ                  
04F0: 3E 08           LD      A,$08               
04F2: 77              LD      (HL),A              
04F3: 21 73 41        LD      HL,$4173            
04F6: 34              INC     (HL)                
04F7: C9              RET                         
04F8: 21 71 41        LD      HL,$4171            
04FB: 35              DEC     (HL)                
04FC: C0              RET     NZ                  
04FD: 3E 0C           LD      A,$0C               
04FF: 77              LD      (HL),A              
0500: 21 73 41        LD      HL,$4173            
0503: 34              INC     (HL)                
0504: C9              RET                         
```

## Snake on Ground Sound

[snakeOnGround.mp3](sounds/snakeOnGround.mp3)

```code
;I15 Snake on ground
0505: CD 04 03        CALL    $0304               ; {code.Filter10}
0508: 21 00 01        LD      HL,$0100            
050B: 22 76 41        LD      ($4176),HL          ; {ram.m4176}
050E: F7              RST     $30                 
050F: 06 06           LD      B,$06               
0511: DF              RST     $18                 
0512: 3E 08           LD      A,$08               
0514: 32 75 41        LD      ($4175),A           ; {ram.m4175}
0517: AF              XOR     A                   
0518: 32 78 41        LD      ($4178),A           ; {ram.m4178}
051B: C9              RET                         
;
;C15 Snake on ground
051C: 3A 78 41        LD      A,($4178)           ; {ram.m4178}
051F: FE 01           CP      $01                 
0521: 28 34           JR      Z,$557              ; {}
0523: FE 02           CP      $02                 
0525: 28 48           JR      Z,$56F              ; {}
0527: FE 03           CP      $03                 
0529: 28 69           JR      Z,$594              ; {}
052B: FE 04           CP      $04                 
052D: 28 76           JR      Z,$5A5              ; {}
052F: 21 75 41        LD      HL,$4175            
0532: 35              DEC     (HL)                
0533: 20 16           JR      NZ,$54B             ; {}
0535: 36 08           LD      (HL),$08            
0537: 11 F0 FF        LD      DE,$FFF0            
053A: 2A 76 41        LD      HL,($4176)          ; {ram.m4176}
053D: 19              ADD     HL,DE               
053E: 22 76 41        LD      ($4176),HL          ; {ram.m4176}
0541: 7C              LD      A,H                 
0542: A7              AND     A                   
0543: 20 05           JR      NZ,$54A             ; {}
0545: 7D              LD      A,L                 
0546: FE 38           CP      $38                 
0548: 38 03           JR      C,$54D              ; {}
054A: EF              RST     $28                 
054B: AF              XOR     A                   
054C: C9              RET                         
054D: 3E 20           LD      A,$20               
054F: 32 75 41        LD      ($4175),A           ; {ram.m4175}
0552: 44              LD      B,H                 
0553: 3E 01           LD      A,$01               
0555: 18 12           JR      $569                ; {}
0557: 21 75 41        LD      HL,$4175            
055A: 35              DEC     (HL)                
055B: 20 EE           JR      NZ,$54B             ; {}
055D: 36 05           LD      (HL),$05            
055F: 3E 03           LD      A,$03               
0561: 21 60 00        LD      HL,$0060            
0564: 06 02           LD      B,$02               
0566: 22 76 41        LD      ($4176),HL          ; {ram.m4176}
0569: 32 78 41        LD      ($4178),A           ; {ram.m4178}
056C: DF              RST     $18                 
056D: AF              XOR     A                   
056E: C9              RET                         
056F: 21 75 41        LD      HL,$4175            
0572: 35              DEC     (HL)                
0573: 20 D6           JR      NZ,$54B             ; {}
0575: 36 06           LD      (HL),$06            
0577: 11 FC FF        LD      DE,$FFFC            
057A: 2A 76 41        LD      HL,($4176)          ; {ram.m4176}
057D: 19              ADD     HL,DE               
057E: 22 76 41        LD      ($4176),HL          ; {ram.m4176}
0581: 7C              LD      A,H                 
0582: A7              AND     A                   
0583: 20 C5           JR      NZ,$54A             ; {}
0585: 7D              LD      A,L                 
0586: FE 30           CP      $30                 
0588: 30 C0           JR      NC,$54A             ; {}
058A: 3E 30           LD      A,$30               
058C: 32 75 41        LD      ($4175),A           ; {ram.m4175}
058F: 44              LD      B,H                 
0590: 3E 03           LD      A,$03               
0592: 18 D5           JR      $569                ; {}
0594: 21 75 41        LD      HL,$4175            
0597: 35              DEC     (HL)                
0598: 20 B1           JR      NZ,$54B             ; {}
059A: 36 04           LD      (HL),$04            
059C: 3E 04           LD      A,$04               
059E: 21 60 00        LD      HL,$0060            
05A1: 06 04           LD      B,$04               
05A3: 18 C1           JR      $566                ; {}
05A5: 21 75 41        LD      HL,$4175            
05A8: 35              DEC     (HL)                
05A9: 20 A0           JR      NZ,$54B             ; {}
05AB: 36 04           LD      (HL),$04            
05AD: 11 10 00        LD      DE,$0010            
05B0: 2A 76 41        LD      HL,($4176)          ; {ram.m4176}
05B3: 19              ADD     HL,DE               
05B4: 22 76 41        LD      ($4176),HL          ; {ram.m4176}
05B7: 7C              LD      A,H                 
05B8: A7              AND     A                   
05B9: 28 8F           JR      Z,$54A              ; {}
05BB: 7D              LD      A,L                 
05BC: FE 80           CP      $80                 
05BE: 38 8A           JR      C,$54A              ; {}
05C0: C3 05 05        JP      $0505               ; {}
```

## Race Car Sound

[raceCar.mp3](sounds/raceCar.mp3)

```code
;I17 Race car
05C3: AF              XOR     A                   
05C4: 21 10 41        LD      HL,$4110            
05C7: 77              LD      (HL),A              
05C8: 23              INC     HL                  
05C9: 36 04           LD      (HL),$04            
05CB: 23              INC     HL                  
05CC: 36 04           LD      (HL),$04            
05CE: 23              INC     HL                  
05CF: 36 04           LD      (HL),$04            
05D1: 23              INC     HL                  
05D2: 36 68           LD      (HL),$68            
05D4: CD B0 02        CALL    $02B0               ; {code.EnableNoise}
05D7: 3E 06           LD      A,$06               
05D9: 06 18           LD      B,$18               
05DB: CF              RST     $08                 ; Write to AY
05DC: 06 04           LD      B,$04               
05DE: CD 7C 02        CALL    $027C               ; {code.SetAmplitude}
05E1: CD C7 02        CALL    $02C7               ; {code.Filter00}
05E4: C9              RET                         
;
;C17 Race car
05E5: CD 1C 06        CALL    $061C               ; {}
05E8: CD ED 05        CALL    $05ED               ; {}
05EB: AF              XOR     A                   
05EC: C9              RET                         
05ED: 3A 10 41        LD      A,($4110)           ; {ram.m4110}
05F0: CB 47           BIT     0,A                 
05F2: 28 10           JR      Z,$604              ; {}
05F4: 21 12 41        LD      HL,$4112            
05F7: 35              DEC     (HL)                
05F8: C0              RET     NZ                  
05F9: 36 04           LD      (HL),$04            
05FB: 06 00           LD      B,$00               
05FD: CD 7C 02        CALL    $027C               ; {code.SetAmplitude}
0600: 0E 01           LD      C,$01               
0602: 18 10           JR      $614                ; {}
0604: 21 11 41        LD      HL,$4111            
0607: 35              DEC     (HL)                
0608: C0              RET     NZ                  
0609: 36 04           LD      (HL),$04            
060B: 3A 13 41        LD      A,($4113)           ; {ram.m4113}
060E: 47              LD      B,A                 
060F: CD 7C 02        CALL    $027C               ; {code.SetAmplitude}
0612: 0E 01           LD      C,$01               
0614: 3A 10 41        LD      A,($4110)           ; {ram.m4110}
0617: A9              XOR     C                   
0618: 32 10 41        LD      ($4110),A           ; {ram.m4110}
061B: C9              RET                         
061C: 21 14 41        LD      HL,$4114            
061F: 35              DEC     (HL)                
0620: C0              RET     NZ                  
0621: 36 68           LD      (HL),$68            
0623: 21 13 41        LD      HL,$4113            
0626: 3A 10 41        LD      A,($4110)           ; {ram.m4110}
0629: CB 4F           BIT     1,A                 
062B: 20 09           JR      NZ,$636             ; {}
062D: 34              INC     (HL)                
062E: 3E 07           LD      A,$07               
0630: BE              CP      (HL)                
0631: 0E 02           LD      C,$02               
0633: 28 DF           JR      Z,$614              ; {}
0635: C9              RET                         
0636: 35              DEC     (HL)                
0637: 7E              LD      A,(HL)              
0638: 3C              INC     A                   
0639: C0              RET     NZ                  
063A: E1              POP     HL                  
063B: 3D              DEC     A                   
063C: C9              RET                         
```

## Pick up Friend Sound

[pickUpMate.mp3](sounds/pickUpMate.mp3)

```code
;I18 Pick up mate
063D: E7              RST     $20                 
063E: 3E 20           LD      A,$20               
0640: 21 E0 41        LD      HL,$41E0            
0643: 77              LD      (HL),A              
0644: 3E 03           LD      A,$03               
0646: 23              INC     HL                  
0647: 77              LD      (HL),A              
0648: 3E 14           LD      A,$14               
064A: 23              INC     HL                  
064B: 77              LD      (HL),A              
064C: 3E 01           LD      A,$01               
064E: 23              INC     HL                  
064F: 77              LD      (HL),A              
0650: 23              INC     HL                  
0651: 36 00           LD      (HL),$00            
0653: 21 10 00        LD      HL,$0010            
0656: 22 E5 41        LD      ($41E5),HL          ; {ram.m41E5}
0659: 2E 20           LD      L,$20               
065B: EF              RST     $28                 
065C: F7              RST     $30                 
065D: 06 09           LD      B,$09               
065F: DF              RST     $18                 
0660: C9              RET                         
;
;C18 Pick up mate
0661: 3A E4 41        LD      A,($41E4)           ; {ram.m41E4}
0664: A7              AND     A                   
0665: 28 1C           JR      Z,$683              ; {}
0667: FE 01           CP      $01                 
0669: 28 1F           JR      Z,$68A              ; {}
066B: FE 03           CP      $03                 
066D: 38 2B           JR      C,$69A              ; {}
066F: 28 49           JR      Z,$6BA              ; {}
0671: D7              RST     $10                 
0672: 3D              DEC     A                   
0673: 28 04           JR      Z,$679              ; {}
0675: 47              LD      B,A                 
0676: DF              RST     $18                 
0677: AF              XOR     A                   
0678: C9              RET                         
0679: AF              XOR     A                   ; 0
067A: 32 A5 42        LD      ($42A5),A           ; {ram.m42A5} Allow music to preempt
067D: 3D              DEC     A                   
067E: C9              RET                         
067F: 47              LD      B,A                 
0680: DF              RST     $18                 
0681: 18 66           JR      $6E9                ; {}
0683: 21 E4 41        LD      HL,$41E4            
0686: 34              INC     (HL)                
0687: AF              XOR     A                   
0688: 18 F5           JR      $67F                ; {}
068A: 21 00 03        LD      HL,$0300            
068D: 22 E7 41        LD      ($41E7),HL          ; {ram.m41E7}
0690: EF              RST     $28                 
0691: 06 08           LD      B,$08               
0693: DF              RST     $18                 
0694: 21 E4 41        LD      HL,$41E4            
0697: 34              INC     (HL)                
0698: 18 4F           JR      $6E9                ; {}
069A: 21 E1 41        LD      HL,$41E1            
069D: 35              DEC     (HL)                
069E: 20 49           JR      NZ,$6E9             ; {}
06A0: 36 03           LD      (HL),$03            
06A2: CD 4D 02        CALL    $024D               ; {code.ReadTune}
06A5: B7              OR      A                   
06A6: 11 08 00        LD      DE,$0008            
06A9: ED 52           SBC     HL,DE               
06AB: EF              RST     $28                 
06AC: 21 E2 41        LD      HL,$41E2            
06AF: 35              DEC     (HL)                
06B0: 20 37           JR      NZ,$6E9             ; {}
06B2: 36 14           LD      (HL),$14            
06B4: 21 E4 41        LD      HL,$41E4            
06B7: 34              INC     (HL)                
06B8: 18 2F           JR      $6E9                ; {}
06BA: 21 E3 41        LD      HL,$41E3            
06BD: 35              DEC     (HL)                
06BE: 20 1D           JR      NZ,$6DD             ; {}
06C0: 36 01           LD      (HL),$01            
06C2: B7              OR      A                   
06C3: 2A E7 41        LD      HL,($41E7)          ; {ram.m41E7}
06C6: 11 20 00        LD      DE,$0020            
06C9: ED 52           SBC     HL,DE               
06CB: 22 E7 41        LD      ($41E7),HL          ; {ram.m41E7}
06CE: EF              RST     $28                 
06CF: 2A E5 41        LD      HL,($41E5)          ; {ram.m41E5}
06D2: 2B              DEC     HL                  
06D3: 7D              LD      A,L                 
06D4: B4              OR      H                   
06D5: 20 0B           JR      NZ,$6E2             ; {}
06D7: 21 E4 41        LD      HL,$41E4            
06DA: 34              INC     (HL)                
06DB: 18 0C           JR      $6E9                ; {}
06DD: 2A E7 41        LD      HL,($41E7)          ; {ram.m41E7}
06E0: 18 EC           JR      $6CE                ; {}
06E2: 22 E5 41        LD      ($41E5),HL          ; {ram.m41E5}
06E5: 21 E4 41        LD      HL,$41E4            
06E8: 35              DEC     (HL)                
06E9: AF              XOR     A                   
06EA: C9              RET                         
```

## Frog Landing Safe Sound

[landingSafe.mp3](sounds/landingSafe.mp3)

```code
;I10 Frog landing safe
06EB: 21 50 00        LD      HL,$0050            
06EE: 22 80 41        LD      ($4180),HL          ; {ram.m4180}
06F1: 21 24 09        LD      HL,$0924            
06F4: 22 82 41        LD      ($4182),HL          ; {ram.m4182}
06F7: 3E 00           LD      A,$00               
06F9: 32 84 41        LD      ($4184),A           ; {ram.m4184}
06FC: 06 0D           LD      B,$0D               
06FE: CD 7C 02        CALL    $027C               ; {code.SetAmplitude}
0701: 21 50 00        LD      HL,$0050            
0704: CD 3C 02        CALL    $023C               ; {code.WriteTune}
0707: CD 60 02        CALL    $0260               ; {code.EnableTone}
070A: CD C7 02        CALL    $02C7               ; {code.Filter00}
070D: C9              RET                         
;
;C10 Frog landing safe
070E: 2A 80 41        LD      HL,($4180)          ; {ram.m4180}
0711: 2B              DEC     HL                  
0712: 22 80 41        LD      ($4180),HL          ; {ram.m4180}
0715: 7C              LD      A,H                 
0716: B5              OR      L                   
0717: 3E 00           LD      A,$00               
0719: 28 47           JR      Z,$762              ; {}
071B: 3A 84 41        LD      A,($4184)           ; {ram.m4184}
071E: CB 47           BIT     0,A                 
0720: 3E 00           LD      A,$00               
0722: 28 0E           JR      Z,$732              ; {}
0724: 21 82 41        LD      HL,$4182            
0727: 35              DEC     (HL)                
0728: C0              RET     NZ                  
0729: 36 24           LD      (HL),$24            
072B: 06 0D           LD      B,$0D               
072D: CD 7C 02        CALL    $027C               ; {code.SetAmplitude}
0730: 18 25           JR      $757                ; {}
0732: CD 4D 02        CALL    $024D               ; {code.ReadTune}
0735: 11 0A 00        LD      DE,$000A            
0738: 3A 84 41        LD      A,($4184)           ; {ram.m4184}
073B: CB 4F           BIT     1,A                 
073D: 28 04           JR      Z,$743              ; {}
073F: AF              XOR     A                   
0740: ED 52           SBC     HL,DE               
0742: 3E 19           LD      A,$19               
0744: CD 3C 02        CALL    $023C               ; {code.WriteTune}
0747: 0E 02           LD      C,$02               
0749: CD 59 07        CALL    $0759               ; {}
074C: 21 83 41        LD      HL,$4183            
074F: 35              DEC     (HL)                
0750: C0              RET     NZ                  
0751: 36 09           LD      (HL),$09            
0753: 47              LD      B,A                 
0754: CD 7C 02        CALL    $027C               ; {code.SetAmplitude}
0757: 0E 01           LD      C,$01               
0759: 3A 84 41        LD      A,($4184)           ; {ram.m4184}
075C: A9              XOR     C                   
075D: 32 84 41        LD      ($4184),A           ; {ram.m4184}
0760: AF              XOR     A                   
0761: C9              RET                         
0762: 21 84 41        LD      HL,$4184            
0765: CB 56           BIT     2,(HL)              
0767: 20 0E           JR      NZ,$777             ; {}
0769: CD EB 06        CALL    $06EB               ; {}
076C: 06 00           LD      B,$00               
076E: CD 7C 02        CALL    $027C               ; {code.SetAmplitude}
0771: 21 84 41        LD      HL,$4184            
0774: CB D6           SET     2,(HL)              
0776: C9              RET                         
0777: 06 00           LD      B,$00               
0779: CD 7C 02        CALL    $027C               ; {code.SetAmplitude}
077C: 3E FF           LD      A,$FF               
077E: C9              RET                         

;I09 Main song intro
077F: E7              RST     $20                 ; Cap filters off
0780: AF              XOR     A                   ; 0
0781: 32 C8 42        LD      ($42C8),A           ; {ram.m42C8} ??
0784: 32 A3 42        LD      ($42A3),A           ; {ram.m42A3} Song 0
0787: F7              RST     $30                 ; Enable tone
0788: C3 61 09        JP      $0961               ; {} Setup voice descriptors

;I0A Music voice B
078B: E7              RST     $20                 ; Cap filters off
078C: F7              RST     $30                 ; Enable tone
078D: C9              RET                         ; Done

;I0B Music voice C
078E: E7              RST     $20                 ; Cap filters off
078F: F7              RST     $30                 ; Enable tone
0790: C9              RET                         ; Done

;C09 Main song intro
0791: DD 21 80 42     LD      IX,$4280            ; Process ...
0795: 18 0A           JR      $7A1                ; {} ... voice A

;C0A Music voice B
0797: DD 21 88 42     LD      IX,$4288            ; Process ...
079B: 18 04           JR      $7A1                ; {} ... voice B

;C0B Music voice C
079D: DD 21 90 42     LD      IX,$4290            ; Process voice C
;
07A1: DD 7E 00        LD      A,(IX+$00)          ; Coarse counter
07A4: FE FF           CP      $FF                 ; FF means end
07A6: 28 05           JR      Z,$7AD              ; {} End of song ... return end
07A8: CD B7 07        CALL    $07B7               ; {code.Music} Process music command
07AB: AF              XOR     A                   ; Return ...
07AC: C9              RET                         ; ... continue

07AD: AF              XOR     A                   ; 0
07AE: 32 A5 42        LD      ($42A5),A           ; {ram.m42A5} Allow music to preempt
07B1: 32 A6 42        LD      ($42A6),A           ; {ram.m42A6} ??
07B4: 3E FF           LD      A,$FF               ; Return ...
07B6: C9              RET                         ; ... end command
```

# Music

```code
Music: 

; 4280 Descriptor voice 1
; 4288 Descriptor voice 2
; 4290 Descriptor voice 3
;
; IX  ... music descriptor
; ss dd pp pp nn nn vr vv
;   dd: base tempo delay count
;   ss: note counter (volume decreases every other tick)
;   pp: music pointer
;   nn: note frequency table
;   vr: volume reload each note
;   vv: current note volume

; 42A2 base note tempo reloat
; 42A3 song number
; 42A4 ?
; 42A5 allow music to preempt ... 0=allow, not zero=disallow
; 42A6 ?
; 42A7 current frog-home song
; 42A8 ?

; ccc_11111   COMMAND  ccc is a command number to execute from the table
; ccc_00000   REST     ccc is a bit number used for the coarse note length and set volume to 0
; ccc_nnnnn   NOTE     ccc is note length and n is note number in note table

07B7: DD 35 01        DEC     (IX+$01)            ; Base tempo delay ...
07BA: C0              RET     NZ                  ; ... not time
07BB: 3A A2 42        LD      A,($42A2)           ; {ram.m42A2} Master tempo delay
07BE: DD 77 01        LD      (IX+$01),A          ; Reset tempo counter
;
07C1: DD CB 00 46     BIT     0,(IX+$00)          ; Time to change volume?
07C5: C2 D5 07        JP      NZ,$07D5            ; {} No ... skip changing
07C8: DD 7E 07        LD      A,(IX+$07)          ; Current volume
07CB: D6 01           SUB     $01                 ; Bump volume
07CD: FA D5 07        JP      M,$07D5             ; {} Already as low as possible ... skip
07D0: DD 77 07        LD      (IX+$07),A          ; Store new volume
07D3: 47              LD      B,A                 ; Volume to B
07D4: DF              RST     $18                 ; Set voice amplitude to value in B
;
07D5: DD 35 00        DEC     (IX+$00)            ; Dec note time
07D8: C0              RET     NZ                  ; Not done ... keep delaying
07D9: DD 6E 02        LD      L,(IX+$02)          ; Get music ...
07DC: DD 66 03        LD      H,(IX+$03)          ; ... pointer
07DF: 7E              LD      A,(HL)              ; Get next command
07E0: 47              LD      B,A                 ; Hold command for a sec
07E1: E6 1F           AND     $1F                 ; Check lower 5 bits
07E3: CA 6A 08        JP      Z,$086A             ; {code.MusicREST} All zero ... rest command
07E6: FE 1F           CP      $1F                 ; All ones?
07E8: C2 84 08        JP      NZ,$0884            ; {code.MusicNOTE} No ... note command

;ccc_11111 Do command c
07EB: 23              INC     HL                  ; Bump ...
07EC: DD 75 02        LD      (IX+$02),L          ; ... music ...
07EF: DD 74 03        LD      (IX+$03),H          ; ... pointer
07F2: 78              LD      A,B                 ; Original command
07F3: E6 E0           AND     $E0                 ; Keep top bits
07F5: 0F              RRCA                        ; Command ...
07F6: 0F              RRCA                        ; ... number ...
07F7: 0F              RRCA                        ; ... times ...
07F8: 0F              RRCA                        ; ... two
07F9: 4F              LD      C,A                 ; Into LSB of BC
07FA: 06 00           LD      B,$00               ; MSB is 0
07FC: 21 05 08        LD      HL,$0805            ; Jump table
07FF: 09              ADD     HL,BC               ; Offset to command jump
0800: 5E              LD      E,(HL)              ; Get LSB
0801: 23              INC     HL                  ; Next byte
0802: 56              LD      D,(HL)              ; Get MSB
0803: D5              PUSH    DE                  ; Push address as return
0804: C9              RET                         ; Jump to the address

MusicSubs: 
0805: 15 08      ; Set the note-set        
0807: 2F 08      ; Set base tempo value        
0809: 45 08      ; Change music volume        
080B: 62 08      ; Volume off and end of song       
080D: 62 08      ; Volume off and end of song        
080F: 62 08      ; Volume off and end of song        
0811: 62 08      ; Volume off and end of song        
0813: 62 08      ; Volume off and end of song        

MusicCmd0: 
; Change start of note range. Next byte in music is an index into the lookup table.
0815: DD 6E 02        LD      L,(IX+$02)          ; Get ...
0818: DD 66 03        LD      H,(IX+$03)          ; ... music pointer
081B: 4E              LD      C,(HL)              ; Get the note-set index
081C: CB 21           SLA     C                   ; * 2
081E: 06 00           LD      B,$00               ; MSB is 0
0820: 21 B3 08        LD      HL,$08B3            ; Note-set table
0823: 09              ADD     HL,BC               ; Offset to table
0824: 5E              LD      E,(HL)              ; Get ...
0825: 23              INC     HL                  ; ... the ...
0826: 56              LD      D,(HL)              ; ... base pointer
0827: DD 73 04        LD      (IX+$04),E          ; Set ...
082A: DD 72 05        LD      (IX+$05),D          ; ... note-set
082D: 18 23           JR      $852                ; {} Bump music pointer and out

MusicCmd1: 
; Change the music tempo. Next byte in music is an index into the lookup table.
082F: DD 6E 02        LD      L,(IX+$02)          ; Get ...
0832: DD 66 03        LD      H,(IX+$03)          ; ... music pointer
0835: 4E              LD      C,(HL)              ; Get new base-delay value index
0836: 06 00           LD      B,$00               ; MSB of index is 0
0838: 21 4B 09        LD      HL,$094B            ; Table of base delays
083B: 09              ADD     HL,BC               ; Offset to new value
083C: 7E              LD      A,(HL)              ; New tempo
083D: 32 A2 42        LD      ($42A2),A           ; {ram.m42A2} Set the tempo for here on out
0840: DD 77 01        LD      (IX+$01),A          ; Reset the current note's count
0843: 18 0D           JR      $852                ; {} Bump music pointer and out

MusicCmd2: 
; Change the note volume. Next byte in the music is the new volume. This takes effect on the
; next note.
0845: DD 6E 02        LD      L,(IX+$02)          ; Get ...
0848: DD 66 03        LD      H,(IX+$03)          ; ... music pointer
084B: 7E              LD      A,(HL)              ; Get new note volume
084C: DD 77 06        LD      (IX+$06),A          ; Set reload volume
084F: DD 77 07        LD      (IX+$07),A          ; Set current volume
;
0852: DD 6E 02        LD      L,(IX+$02)          ; Get ...
0855: DD 66 03        LD      H,(IX+$03)          ; ... music pointer
0858: 23              INC     HL                  ; Bump to next
0859: DD 75 02        LD      (IX+$02),L          ; Store new ...
085C: DD 74 03        LD      (IX+$03),H          ; ... music pointer
085F: C3 D9 07        JP      $07D9               ; {} Process next music command
;
0862: 06 00           LD      B,$00               ; Volume ...
0864: DF              RST     $18                 ; ... off
0865: DD 36 00 FF     LD      (IX+$00),$FF        ; Mark end of song
0869: C9              RET                         ; Done

MusicREST: 
;ccc_0000 Rest command
086A: CD 72 08        CALL    $0872               ; {} Upper 3 to power of 2 for note length
086D: 06 00           LD      B,$00               ; Set voice volume ...
086F: DF              RST     $18                 ; ... to 0
0870: 18 33           JR      $8A5                ; {} Bump music pointer and out

; Upper three bits to power of 2 in note length
; Delay = 2 ^ (ccc - 1)
0872: 78              LD      A,B                 ; Full command
0873: E6 E0           AND     $E0                 ; Keep upper 3 bits
0875: 07              RLCA                        ; Move ...
0876: 07              RLCA                        ; ... upper 3 ...
0877: 07              RLCA                        ; ... to lower 3
0878: 47              LD      B,A                 ; Into B (the counter)
0879: 3E 01           LD      A,$01               ; Far right bit
; We decrement first here. So the values in ccc map to delays as:
;   - 001 -> 00000001 (1)
;   - 010 -> 00000010 (2)
;   - 011 -> 00000100 (4)
;   - 100 -> 00001000 (8)
;   - etc
087B: 10 04           DJNZ    $881                ; {} Set ...
087D: DD 77 00        LD      (IX+$00),A          ; ... note length ...
0880: C9              RET                         ; ... to ...
0881: 07              RLCA                        ; ... value ...
0882: 18 F7           JR      $87B                ; {} ... 2 ^ (ccc-1)

MusicNOTE: 
;ccc_nnnnn NOTE command. c is bit number for length, n is offset in note table
0884: C5              PUSH    BC                  ; Original command is in B
0885: CD 72 08        CALL    $0872               ; {} Set note length
0888: C1              POP     BC                  ; Restore original command
0889: 78              LD      A,B                 ; Get ...
088A: E6 1F           AND     $1F                 ; ... note value
```

# Bug: Pitch is off by one

There are 60 notes defined in the frequency table. The music is defined with 5-bit
note pitches providing a range of 32 notes for the song. Two of the values are special:
0 means rest and 31 means "special command". Each song defines a base offset that is 
added to the pitch value allowing the range of 30 notes to be defined anywhere in the 
note table.

The DEC below seems to make sense at first: a pitch value of 0 is a rest -- we should 
decrement each note so that pitch value 1 is the first note (starting at 0) in the range. 
But the ranges can be (and seem to be) defined with the "ignore 0" built-in. The DEC wastes 
CPU cycles, which isn't really a big deal. 

But it is a big deal if you want to play along on the piano! The music offsets in the data 
below seem to be defined without the want of the DEC. If you look at the main song intro 
notes without the decrement, they land on the big friendly white keys of the piano. With the 
decrement, they are 1/2 step down landing them on the black "accidentals".

I believe this decrement was unintentional -- a bug in the code. I believe the notes were 
defined on the piano a half step higher than they are played by the code. You can NOP the DEC 
out to play the tune more easily on the piano.

```code
; 088C: 00              NOP                         ; Path the rom with a NOP to raise all notes up 1/2 step
088C: 3D              DEC     A                   ; 0 is a rest, 1 is first note (base 0 now)
;
088D: 07              RLCA                        ; Two bytes per entry
088E: 4F              LD      C,A                 ; LSB of BC is offset
088F: 06 00           LD      B,$00               ; MSB of BC is 0
0891: DD 6E 04        LD      L,(IX+$04)          ; Get the ...
0894: DD 66 05        LD      H,(IX+$05)          ; ... note table
0897: 09              ADD     HL,BC               ; Offset to note value
0898: 5E              LD      E,(HL)              ; Get ...
0899: 23              INC     HL                  ; ... note ...
089A: 56              LD      D,(HL)              ; ... value
089B: EB              EX      DE,HL               ; Fine/coarse value to HL
089C: EF              RST     $28                 ; Set note value
089D: DD 46 06        LD      B,(IX+$06)          ; Get note volume reload
08A0: 78              LD      A,B                 ; To A and B
08A1: DD 77 07        LD      (IX+$07),A          ; Set running note volume
08A4: DF              RST     $18                 ; Set physical volume

08A5: DD 6E 02        LD      L,(IX+$02)          ; Get music ...
08A8: DD 66 03        LD      H,(IX+$03)          ; ... pointer
08AB: 23              INC     HL                  ; Bump to next
08AC: DD 75 02        LD      (IX+$02),L          ; Store new ...
08AF: DD 74 03        LD      (IX+$03),H          ; ... music pointer
08B2: C9              RET                         ; Done

NoteSets: 
; Base note sets (base offsets into master note table)
08B3: D3 08  ;  0:   1=G#1 ... 30=C#4  Never used         
08B5: D7 08  ;  1:   1=A#1 ... 30=D#4  Never used
08B7: DB 08  ;  2:   1=C2  ... 30=F4   Never used                  
08B9: DF 08  ;  3:   1=D2  ... 30=G4   Never used                       
08BB: E3 08  ;  4:   1=E2  ... 30=A4   Never used  
08BD: E7 08  ;  5:   1=F#2 ... 30=B4   Intro-B, Main-B, Intro-C, Home-3B, Home-4B, Home-5B, Home-11B, Home-12B, Home-20B
;
08BF: EB 08  ;  6:   1=G#2 ... 30=C#5  GameOver-B
08C1: EF 08  ;  7:   1=A#2 ... 30=D#5  Never used                        
08C3: F3 08  ;  8:   1=C3  ... 30=F5   Never used  
08C5: F7 08  ;  9:   1=D3  ... 30=G5   Never used  
08C7: FB 08  ; 10:   1=E3  ... 30=A5   Never used  
08C9: FF 08  ; 11:   1=F#3 ... 30=B5   Respawn, Intro-A, Main-A, LevelComplete-AB, Home-1AB, Home-2AB, Home-3A, Home-4A, 
;                                      Home-5A, Home-6AB, Home-7AB, Home-8AB, Home-9AB, Home-10AB, Home-11A, Home-12A, 
;                                      Home-13A, Home-14AB, Home-15AB, Home-16AB, Home-17AB, Home-18AB, Home-19AB, Home-20A
;
08CB: 03 09  ; 12:   1=G#3 ... 30=C#6  GameOver-A
08CD: 07 09  ; 13:   1=A#3 ... 30=D#6  Never used  
08CF: 0B 09  ; 14:   1=C4  ... 30=F6   Never used  
08D1: 0F 09  ; 15:   1=D4  ... 30=G6   Never used  
```

# Note Frequencies

```code
NoteTable: 
; Coarse/Fine master note table
; AY runs at 1.789750
; frq = 1789570Hz / (16 * val)
;                 Freq  MIDI Notation
08D3: 6B 08   ;   51.90   32 G#1
08D5: F2 07   ;   54.98   33 A1
08D7: 80 07   ;   58.25   34 A#1
08D9: 14 07   ;   61.72   35 B1
08DB: AE 06   ;   65.40   36 C2
08DD: 4E 06   ;   69.29   37 C#2
08DF: F3 05   ;   73.43   38 D2
08E1: 9E 05   ;   77.78   39 D#2
08E3: 4E 05   ;   82.36   40 E2
08E5: 01 05   ;   87.31   41 F2
08E7: B9 04   ;   92.51   42 F#2
08E9: 76 04   ;   97.94   43 G2
08EB: 36 04   ;  103.75   44 G#2
08ED: F9 03   ;  109.97   45 A2
08EF: C0 03   ;  116.50   46 A#2
08F1: 8A 03   ;  123.45   47 B2
08F3: 57 03   ;  130.81   48 C3
08F5: 27 03   ;  138.59   49 C#3
08F7: FA 02   ;  146.78   50 D3
08F9: CF 02   ;  155.56   51 D#3
08FB: A7 02   ;  164.72   52 E3
08FD: 81 02   ;  174.49   53 F3
08FF: 5D 02   ;  184.87   54 F#3
0901: 3B 02   ;  195.88   55 G3
0903: 1B 02   ;  207.51   56 G#3
0905: FD 01   ;  219.74   57 A3
0907: E0 01   ;  233.01   58 A#3
0909: C5 01   ;  246.90   59 B3
090B: AC 01   ;  261.32   60 C4
090D: 94 01   ;  276.85   61 C#4
090F: 7D 01   ;  293.56   62 D4
0911: 68 01   ;  310.68   63 D#4
0913: 53 01   ;  329.93   64 E4
0915: 40 01   ;  349.52   65 F4
0917: 2E 01   ;  370.35   66 F#4
0919: 1D 01   ;  392.44   67 G4
091B: 0D 01   ;  415.79   68 G#4
091D: FE 00   ;  440.34   69 A4
091F: F0 00   ;  466.03   70 A#4
0921: E3 00   ;  492.72   71 B4
0923: D6 00   ;  522.65   72 C5
0925: CA 00   ;  553.70   73 C#5
0927: BE 00   ;  588.67   74 D5
0929: B4 00   ;  621.37   75 D#5
092B: AA 00   ;  657.93   76 E5
092D: A0 00   ;  699.05   77 F5
092F: 97 00   ;  740.71   78 F#5
0931: 8F 00   ;  782.15   79 G5
0933: 87 00   ;  828.50   80 G#5
0935: 7F 00   ;  880.69   81 A5
0937: 78 00   ;  932.06   82 A#5
0939: 71 00   ;  989.80   82 B5
093B: 6B 00   ; 1045.3    84 C6
093D: 65 00   ; 1107.4    85 C#6
093F: 5F 00   ; 1177.3    86 D6
0941: 5A 00   ; 1242.7    87 D#6
0943: 55 00   ; 1315.8    88 E6
0945: 50 00   ; 1398.1    89 F6
0947: 4C 00   ; 1471.6    90 F#6
0949: 47 00   ; 1575.3    91 G6

DelayTable: 
; Base note delay table (song's overall tempo)
; There are 700 sound ticks/sec. In our music below, we'll say that 2^4 is a
; quarter note. In the table below, a quarter note lasts x*16 ticks. A tick
; lasts 1/700 seconds. The length of a quarter is x*16/700.
; This table shows tempo in quarternotes / minute
094B: 04 ;  0: 656 Never used
094C: 08 ;  1: 328 Never used
094D: 34 ;  2:  50 Never used
094E: 2C ;  3:  60 Never used
094F: 25 ;  4:  71 Never used
0950: 21 ;  5:  80 Never used
0951: 1D ;  6:  91 Never used
0952: 1A ;  7: 101 Never used
0953: 18 ;  8: 109 Never used
0954: 16 ;  9: 119 Never used
0955: 14 ; 10: 131 Intro
0956: 13 ; 11: 138 Never used
0957: 11 ; 12: 154 Main, LevelComplete, Home-11
0958: 10 ; 13: 164 Home-1, Home-2, Home-3, Home-4, Home-5, Home-6, Home-7, Home-8, Home-9, Home-10
;                  Home-12, Home-13, Home-14, Home-15, Home-16, Home-17, Home-18, Home-19, Home-20
0959: 0F ; 14: 175 Respawn
095A: 0A ; 15: 263 GameOver
           
095B: 21 A5 42        LD      HL,$42A5            ; Get ...
095E: 7E              LD      A,(HL)              ; ... preempt flag
095F: A7              AND     A                   ; Preempting allowed
0960: C0              RET     NZ                  ; No ... out

; Set music pointers for all 3 descriptors from a lookup table.
0961: 21 93 09        LD      HL,$0993            ; Initialization data for all 3 music descriptors
0964: 11 80 42        LD      DE,$4280            ; Descriptors
0967: 01 18 00        LD      BC,$0018            ; 8+8+8 = 18
096A: ED B0           LDIR                        ; Initialize music descriptors
096C: 3A A3 42        LD      A,($42A3)           ; {ram.m42A3} Song number to A
096F: 87              ADD     A,A                 ; A*2
0970: 4F              LD      C,A                 ; Hold *2 value
0971: 87              ADD     A,A                 ; A*4
0972: 81              ADD     A,C                 ; A*6
0973: 4F              LD      C,A                 ; C=A*6
0974: 06 00           LD      B,$00               ; MSB 0
0976: 21 AB 09        LD      HL,$09AB            ; Song table
0979: 09              ADD     HL,BC               ; Get song info
097A: 11 82 42        LD      DE,$4282            ; Load music pointer of ...
097D: CD 89 09        CALL    $0989               ; {} ... first descriptor
0980: 11 8A 42        LD      DE,$428A            ; Load music pointer of ...
0983: CD 89 09        CALL    $0989               ; {} ... second descriptor
0986: 11 92 42        LD      DE,$4292            ; Third descriptor
0989: 7E              LD      A,(HL)              ; Value from table
098A: 12              LD      (DE),A              ; Store it in descriptor
098B: CD 90 09        CALL    $0990               ; {} Bump pointers
098E: 7E              LD      A,(HL)              ; Value from table
098F: 12              LD      (DE),A              ; Store it in table
0990: 23              INC     HL                  ; Bump ...
0991: 13              INC     DE                  ; ... pointers
0992: C9              RET                         ; Done

; Initialization values for all 3 music descriptors. This sets the
; note to reload on first tick.
0993: 01 01 00 00 00 00 00 00                                       
099B: 01 01 00 00 00 00 00 00                                       
09A3: 01 01 00 00 00 00 00 00                                       
```

# Song Table

```code
SongTable: 
; Music pointers for all 3 voices for each song. There are 25 songs. Frogger has
; a very rich music base.
;
09AB: 47 0A    6A 0A    8D 0A   ; Main song intro [songIntroAndMain.mp3](./sounds/songIntroAndMain.mp3)
;
; Fixed main song and intro [songIntroAndMain_fix.mp3](./sounds/songIntroAndMain_fix.mp3) [.txt](./sounds/songIntroAndMain_G.txt) [.mid](./sounds/songIntroAndMain_G.mid)
;
09B1: CE 0A    E7 0A    3A 0B   ; Game over [songGameOver.mp3](./sounds/songGameOver.mp3) [.txt](./sounds/songGameOver_G.txt) [.mid](./sounds/songGameOver_G.mid)
09B7: FB 0A    19 0B    3A 0B   ; Level complete [songLevelComplete.mp3](./sounds/songLevelComplete.mp3) [.txt](./sounds/songLevelComplete_G.txt) [.mid](./sounds/songLevelComplete_G.mid)
09BD: 15 0C    3A 0B    3A 0B   ; New life begins [songRespawn.mp3](./sounds/songRespawn.mp3) [.txt](./sounds/songRespawn_G.txt) [.mid](./sounds/songRespawn_G.mid)
;
; Unused
09C3: 00 00    00 00    00 00
;
; 20 Frog-home songs [songzHomeXX_G.txt](./sounds/songzHomeXX_G.txt) [.mid](./sounds/songzHomeXX_G.mid)
09C9: B5 0B    E6 0B    3A 0B   ; Home-1 [songHome01.mp3](./sounds/songzHome01.mp3) 
09CF: 2A 0C    55 0C    3A 0B   ; Home-2 [songHome02.mp3](./sounds/songzHome02.mp3)
09D5: 7E 0C    BA 0C    3A 0B   ; Home-3 [songHome03.mp3](./sounds/songzHome03.mp3) 
09DB: EE 0C    1A 0D    3A 0B   ; Home-4 [songHome04.mp3](./sounds/songzHome04.mp3)
;
09E1: 43 0D    7B 0D    3A 0B   ; Home-5 [songHome05.mp3](./sounds/songzHome05.mp3)
09E7: 9F 0D    D2 0D    3A 0B   ; Home-6 [songHome06.mp3](./sounds/songzHome06.mp3)
09ED: 03 0E    5C 0E    3A 0B   ; Home-7 [songHome07.mp3](./sounds/songzHome07.mp3)
09F3: 81 0E    B0 0E    3A 0B   ; Home-8 [songHome08.mp3](./sounds/songzHome08.mp3) 
;
09F9: DD 0E    13 0F    3A 0B   ; Home-9 [songHome09.mp3](./sounds/songzHome09.mp3) 
09FF: 47 0F    78 0F    3A 0B   ; Home-10 [songHome10.mp3](./sounds/songzHome10.mp3)
0A05: A7 0F    E2 0F    3A 0B   ; Home-11 [songHome11.mp3](./sounds/songzHome11.mp3)
0A0B: 74 11    C7 11    3A 0B   ; Home-12 [songHome12.mp3](./sounds/songzHome12.mp3) 
;
0A11: F1 11    17 12    3A 0B   ; Home-13 [songHome13.mp3](./sounds/songzHome13.mp3)
0A17: 18 12    40 12    3A 0B   ; Home-14 [songHome14.mp3](./sounds/songzHome14.mp3)
0A1D: 66 12    92 12    3A 0B   ; Home-15 [songHome15.mp3](./sounds/songzHome15.mp3) 
0A23: BE 12    DD 12    3A 0B   ; Home-16 [songHome16.mp3](./sounds/songzHome16.mp3) 
;
0A29: F6 12    19 13    3A 0B   ; Home-17 [songHome17.mp3](./sounds/songzHome17.mp3)
0A2F: 3A 13    7A 13    3A 0B   ; Home-18 [songHome18.mp3](./sounds/songzHome18.mp3)
0A35: B8 13    EC 13    3A 0B   ; Home-19 [songHome19.mp3](./sounds/songzHome19.mp3)
0A3B: 1E 14    48 14    3A 0B   ; Home-20 [songHome20.mp3](./sounds/songzHome20.mp3)
;
0A41: 34 10    CA 10    3A 0B   ; Main song [songIntroAndMain.mp3](./sounds/songIntroAndMain.mp3) [.txt](./sounds/songIntroAndMain_G.txt) [.mid](./sounds/songIntroAndMain_G.mid)
```

# Song: Main Intro

```code
;S0A Main song intro
; Song=0 Voice=A
0A47: 1F 0B    ; 000_11111 0B SC00:Use note set index 11 (note 1 = F#3)
0A49: 3F 0A    ; 001_11111 0A SC01:Set tempo index 10 (value 20 = 131 quarters/minute)
0A4B: 5F 07    ; 010_11111 07 SC02:Set volume to 07

; Take the first note below for example:
; The value is 100_10001 -- note 17 (decremented to 16) for 2^3=8 counts.
; The base note set = 11, which points to 8FF (note 1 = F#3).
; $3FF + 16*2 = $91F = A#4
;
; I think they wrote the music to the pre-decremented value (17) which would land on B4.
; I believe the decrement in the code is a bug. The pre-decremented values makes the score 
; much friendlier on the piano. Thus the notes below are shown raised 1/2 step. For the real 
; frequency heard in the game, subtract 1/2 step.

0A4D: 91       ; NOTE 8B4
0A4E: 8D       ; NOTE 8G4
0A4F: 8D       ; NOTE 8G4
0A50: 8D       ; NOTE 8G4
0A51: 91       ; NOTE 8B4
0A52: 8D       ; NOTE 8G4
0A53: 8D       ; NOTE 8G4
0A54: 8D       ; NOTE 8G4
0A55: 92       ; NOTE 8C5
0A56: 92       ; NOTE 8C5
0A57: 91       ; NOTE 8B4
0A58: 91       ; NOTE 8B4
0A59: AF       ; NOTE 4A4
0A5A: A0       ; NOTE 4R
0A5B: 92       ; NOTE 8C5
0A5C: 92       ; NOTE 8C5
0A5D: 91       ; NOTE 8B4
0A5E: 91       ; NOTE 8B4
0A5F: 8F       ; NOTE 8A4
0A60: 8F       ; NOTE 8A4
0A61: 96       ; NOTE 8E5
0A62: 96       ; NOTE 8E5
0A63: 94       ; NOTE 8D5
0A64: 92       ; NOTE 8C5
0A65: 91       ; NOTE 8B4
0A66: 8F       ; NOTE 8A4
0A67: AD       ; NOTE 4G4
0A68: A0       ; NOTE 4R
0A69: FF       ; END OF VOICE
;
;S0B Main song intro
; Song=0 Voice=B
0A6A: 1F 05    ; SC00:Use note set index 5 (note 1 = F#2)
0A6C: 5F 07    ; SC02:Set volume to 07
0A6E: 8D       ; NOTE 8G3
0A6F: 91       ; NOTE 8B3
0A70: 88       ; NOTE 8D3
0A71: 91       ; NOTE 8B3
0A72: 8D       ; NOTE 8G3
0A73: 91       ; NOTE 8B3
0A74: 88       ; NOTE 8D3
0A75: 91       ; NOTE 8B3
0A76: 8F       ; NOTE 8A3
0A77: 92       ; NOTE 8C4
0A78: 88       ; NOTE 8D3
0A79: 92       ; NOTE 8C4
0A7A: 8F       ; NOTE 8A3
0A7B: 92       ; NOTE 8C4
0A7C: 88       ; NOTE 8D3
0A7D: 92       ; NOTE 8C4
0A7E: 8F       ; NOTE 8A3
0A7F: 92       ; NOTE 8C4
0A80: 88       ; NOTE 8D3
0A81: 92       ; NOTE 8C4
0A82: 8F       ; NOTE 8A3
0A83: 92       ; NOTE 8C4
0A84: 88       ; NOTE 8D3
0A85: 92       ; NOTE 8C4
0A86: 8F       ; NOTE 8A3
0A87: 92       ; NOTE 8C4
0A88: 88       ; NOTE 8D3
0A89: 92       ; NOTE 8C4
0A8A: B1       ; NOTE 4B3
0A8B: A0       ; NOTE 4R
0A8C: FF       ; END OF VOICE
;
;S0C Main song intro
; Song=0 Voice=C
0A8D: 1F 05    ; SC00:Use note set index 5 (note 1 = F#2)
0A8F: 5F 07    ; SC02:Set volume to 07
0A91: 80       ; NOTE 8R
0A92: 8D       ; NOTE 8G3
0A93: 80       ; NOTE 8R
0A94: 8D       ; NOTE 8G3
0A95: 80       ; NOTE 8R
0A96: 8D       ; NOTE 8G3
0A97: 80       ; NOTE 8R
0A98: 8D       ; NOTE 8G3
0A99: 80       ; NOTE 8R
0A9A: 8F       ; NOTE 8A3
0A9B: 80       ; NOTE 8R
0A9C: 8F       ; NOTE 8A3
0A9D: 80       ; NOTE 8R
0A9E: 8F       ; NOTE 8A3
0A9F: 80       ; NOTE 8R
0AA0: 8F       ; NOTE 8A3
0AA1: 80       ; NOTE 8R
0AA2: 8F       ; NOTE 8A3
0AA3: 80       ; NOTE 8R
0AA4: 8F       ; NOTE 8A3
0AA5: 80       ; NOTE 8R
0AA6: 8F       ; NOTE 8A3
0AA7: 80       ; NOTE 8R
0AA8: 8F       ; NOTE 8A3
0AA9: 80       ; NOTE 8R
0AAA: 8F       ; NOTE 8A3
0AAB: 80       ; NOTE 8R
0AAC: 8F       ; NOTE 8A3
0AAD: AD       ; NOTE 4G3
0AAE: A0       ; NOTE 4R
0AAF: FF       ; END OF VOICE

;I0C Game over song 
0AB0: E7              RST     $20                 
0AB1: 3E 01           LD      A,$01               
0AB3: 32 A3 42        LD      ($42A3),A           ; {ram.m42A3}
0AB6: 32 A6 42        LD      ($42A6),A           ; {ram.m42A6}
0AB9: F7              RST     $30                 
0ABA: C3 61 09        JP      $0961               ; {}

;C0C Game over song
0ABD: DD 21 80 42     LD      IX,$4280            
0AC1: C3 A1 07        JP      $07A1               ; {}

;I0D Music voice B
0AC4: E7              RST     $20                 
0AC5: F7              RST     $30                 
0AC6: C9              RET                         

;C0D Music voice B
0AC7: DD 21 88 42     LD      IX,$4288            
0ACB: C3 A1 07        JP      $07A1               ; {}
```

# Song: Game Over

```code
;S1A Game over
; Song=1 Voice=A
0ACE: 1F 0C    ; SC00:Use note set index 12 (note 1 = G#3)
0AD0: 3F 0F    ; SC01:Set tempo index 15 (value 10 = 263 quarters/minute)
0AD2: 5F 07    ; SC02:Set volume to 07
0AD4: AD       ; NOTE 4A4
0AD5: 80       ; NOTE 8R
0AD6: 8A       ; NOTE 8F#4
0AD7: B2       ; NOTE 4D5
0AD8: B2       ; NOTE 4D5
0AD9: B6       ; NOTE 4F#5
0ADA: 74       ; NOTE 16E5
0ADB: 72       ; NOTE 16D5
0ADC: 71       ; NOTE 16C#5
0ADD: 6F       ; NOTE 16B4
0ADE: CD       ; NOTE 2A4
0ADF: AB       ; NOTE 4G4
0AE0: AD       ; NOTE 4A4
0AE1: A8       ; NOTE 4E4
0AE2: AD       ; NOTE 4A4
0AE3: AA       ; NOTE 4F#4
0AE4: AD       ; NOTE 4A4
0AE5: C6       ; NOTE 2D4
0AE6: FF       ; END OF VOICE
;
;S1B Game over
; Song=1 Voice=B
0AE7: 1F 06    ; SC00:Use note set index 6 (note 1 = G#2)
0AE9: 5F 07    ; SC02:Set volume to 07
0AEB: AA       ; NOTE 4F#3
0AEC: AD       ; NOTE 4A3
0AED: AA       ; NOTE 4F#3
0AEE: AD       ; NOTE 4A3
0AEF: A6       ; NOTE 4D3
0AF0: AD       ; NOTE 4A3
0AF1: AA       ; NOTE 4F#3
0AF2: AD       ; NOTE 4A3
0AF3: A8       ; NOTE 4E3
0AF4: AD       ; NOTE 4A3
0AF5: AB       ; NOTE 4G3
0AF6: AD       ; NOTE 4A3
0AF7: A6       ; NOTE 4D3
0AF8: AD       ; NOTE 4A3
0AF9: CA       ; NOTE 2F#3
0AFA: FF       ; END OF VOICE
```

# Song: Level Complete

```code
;S2A Level complete
; Song=2 Voice=A
0AFB: 1F 0B    ; SC00:Use note set index 11 (note 1 = F#3)
0AFD: 3F 0C    ; SC01:Set tempo index 12 (154 quarters/minute)
0AFF: 5F 07    ; SC02:Set volume to 07
0B01: 8D       ; NOTE 8G4
0B02: 8F       ; NOTE 8A4
0B03: 91       ; NOTE 8B4
0B04: 92       ; NOTE 8C5
0B05: B4       ; NOTE 4D5
0B06: B1       ; NOTE 4B4
0B07: 8D       ; NOTE 8G4
0B08: 8F       ; NOTE 8A4
0B09: 91       ; NOTE 8B4
0B0A: 8F       ; NOTE 8A4
0B0B: AD       ; NOTE 4G4
0B0C: AD       ; NOTE 4G4
0B0D: 8D       ; NOTE 8G4
0B0E: 8F       ; NOTE 8A4
0B0F: 91       ; NOTE 8B4
0B10: 92       ; NOTE 8C5
0B11: B4       ; NOTE 4D5
0B12: B1       ; NOTE 4B4
0B13: 94       ; NOTE 8D5
0B14: 92       ; NOTE 8C5
0B15: 91       ; NOTE 8B4
0B16: 8F       ; NOTE 8A4
0B17: CD       ; NOTE 2G4
0B18: FF       ; END OF VOICE
;
;S2B Level complete
; Song=2 Voice=B
0B19: 1F 0B    ; SC00:Use note set index 11 (note 1 = F#3)
0B1B: 5F 07    ; SC02:Set volume to 07
0B1D: 85       ; NOTE 8B3
0B1E: 88       ; NOTE 8D4
0B1F: 85       ; NOTE 8B3
0B20: 88       ; NOTE 8D4
0B21: 85       ; NOTE 8B3
0B22: 88       ; NOTE 8D4
0B23: 85       ; NOTE 8B3
0B24: 88       ; NOTE 8D4
0B25: 85       ; NOTE 8B3
0B26: 88       ; NOTE 8D4
0B27: 85       ; NOTE 8B3
0B28: 88       ; NOTE 8D4
0B29: 85       ; NOTE 8B3
0B2A: 88       ; NOTE 8D4
0B2B: 85       ; NOTE 8B3
0B2C: 88       ; NOTE 8D4
0B2D: 85       ; NOTE 8B3
0B2E: 88       ; NOTE 8D4
0B2F: 85       ; NOTE 8B3
0B30: 88       ; NOTE 8D4
0B31: 85       ; NOTE 8B3
0B32: 88       ; NOTE 8D4
0B33: 85       ; NOTE 8B3
0B34: 88       ; NOTE 8D4
0B35: 86       ; NOTE 8C4
0B36: 88       ; NOTE 8D4
0B37: 86       ; NOTE 8C4
0B38: 88       ; NOTE 8D4
0B39: C5       ; NOTE 2B3
0B3A: FF       ; END OF VOICE

;I11 Level complete song
0B3B: E7              RST     $20                 
0B3C: AF              XOR     A                   
0B3D: 32 C8 42        LD      ($42C8),A           ; {ram.m42C8}
0B40: 3E 02           LD      A,$02               
0B42: 32 A3 42        LD      ($42A3),A           ; {ram.m42A3}
0B45: 32 A6 42        LD      ($42A6),A           ; {ram.m42A6}
0B48: F7              RST     $30                 
0B49: C3 61 09        JP      $0961               ; {}

;C11 Level complete song
0B4C: DD 21 80 42     LD      IX,$4280            
0B50: C3 A1 07        JP      $07A1               ; {}

;I12 Music voice B 
0B53: E7              RST     $20                 
0B54: F7              RST     $30                 
0B55: C9              RET                         

;C12 Music voice B
0B56: DD 21 88 42     LD      IX,$4288            
0B5A: C3 A1 07        JP      $07A1               ; {}

;I13 Music voice C
0B5D: E7              RST     $20                 
0B5E: F7              RST     $30                 
0B5F: C9              RET                         

;C13 Music voice C
0B60: DD 21 90 42     LD      IX,$4290            
0B64: C3 A1 07        JP      $07A1               ; {}

;I08 Song interludes after frog home
0B67: E7              RST     $20                 ; Remove all capacitor filtering
0B68: 21 A7 42        LD      HL,$42A7            ; Current frog-home song
0B6B: 34              INC     (HL)                ; Bump to next frog-home song
0B6C: 7E              LD      A,(HL)              ; Get new frog-home song
0B6D: FE 01           CP      $01                 ; Is this the first pass
0B6F: 28 10           JR      Z,$B81              ; {} Yes ... use song 5 and up
0B71: FE 18           CP      $18                 ; End of frog-home songs?
0B73: 28 11           JR      Z,$B86              ; {} Yes ... reset to beginning
0B75: 32 A3 42        LD      ($42A3),A           ; {ram.m42A3} Set song number
0B78: F7              RST     $30                 ; Enable tone
0B79: 3E 01           LD      A,$01               ; Interlude after frog home ...
0B7B: 32 A5 42        LD      ($42A5),A           ; {ram.m42A5} ... can't be preempted
0B7E: C3 61 09        JP      $0961               ; {} Set up song descriptors
;
0B81: 36 05           LD      (HL),$05            ; Start sequence with
0B83: 7E              LD      A,(HL)              ; ... song 5
0B84: 18 EF           JR      $B75                ; {} Start song 5
;
0B86: 36 04           LD      (HL),$04            ; Next song will increment to 5
0B88: 3E 18           LD      A,$18               ; Last song is 18
0B8A: 18 E9           JR      $B75                ; {} Start song 18

;I0E Music voice B
0B8C: E7              RST     $20                 
0B8D: F7              RST     $30                 
0B8E: C9              RET                         

;C08 Song interludes after frog home
0B8F: DD 21 80 42     LD      IX,$4280            
0B93: C3 A1 07        JP      $07A1               ; {}

;C0E Music voice B
0B96: DD 21 88 42     LD      IX,$4288            
0B9A: C3 A1 07        JP      $07A1               ; {}

;I06 Next life begins
0B9D: E7              RST     $20                 
0B9E: 3E 03           LD      A,$03               
0BA0: 32 A3 42        LD      ($42A3),A           ; {ram.m42A3}
0BA3: F7              RST     $30                 
0BA4: C3 5B 09        JP      $095B               ; {}
;
;C06 Next life begins
0BA7: 3A A5 42        LD      A,($42A5)           ; {ram.m42A5} Music preemption ...
0BAA: A7              AND     A                   ; ... allowed
0BAB: C2 B4 07        JP      NZ,$07B4            ; {} No ...
0BAE: DD 21 80 42     LD      IX,$4280            
0BB2: C3 A1 07        JP      $07A1               ; {}
```

# Song: Frog Home 1

```code
;S5A Frog-home 1
; Song=5 Voice=A
0BB5: 1F 0B    ; SC00:Use note set index 11  (note 1 = F#3)
0BB7: 3F 0D    ; SC01:Set tempo index 13 (164 quarters/minute)
0BB9: 5F 06    ; SC02:Set volume to 06
0BBB: 9B       ; NOTE 8A5
0BBC: 60       ; NOTE 16R
0BBD: 7D       ; NOTE 16B5
0BBE: BB       ; NOTE 4A5
0BBF: A6       ; NOTE 4C4
0BC0: 9B       ; NOTE 8A5
0BC1: 60       ; NOTE 16R
0BC2: 7D       ; NOTE 16B5
0BC3: BB       ; NOTE 4A5
0BC4: B8       ; NOTE 4F#5
0BC5: 9B       ; NOTE 8A5
0BC6: 60       ; NOTE 16R
0BC7: 7B       ; NOTE 16A5
0BC8: BD       ; NOTE 4B5
0BC9: 80       ; NOTE 8R
0BCA: 9B       ; NOTE 8A5
0BCB: 99       ; NOTE 8G5
0BCC: 93       ; NOTE 8C#5
0BCD: B8       ; NOTE 4F#5
0BCE: A0       ; NOTE 4R
0BCF: 8F       ; NOTE 8A4
0BD0: 60       ; NOTE 16R
0BD1: 6F       ; NOTE 16A4
0BD2: 8F       ; NOTE 8A4
0BD3: 93       ; NOTE 8C#5
0BD4: B6       ; NOTE 4E5
0BD5: 8F       ; NOTE 8A4
0BD6: 60       ; NOTE 16R
0BD7: 6F       ; NOTE 16A4
0BD8: 8F       ; NOTE 8A4
0BD9: 94       ; NOTE 8D5
0BDA: B8       ; NOTE 4F#5
0BDB: 9B       ; NOTE 8A5
0BDC: 60       ; NOTE 16R
0BDD: 7B       ; NOTE 16A5
0BDE: BD       ; NOTE 4B5
0BDF: 80       ; NOTE 8R
0BE0: 9B       ; NOTE 8A5
0BE1: 99       ; NOTE 8G5
0BE2: 93       ; NOTE 8C#5
0BE3: B4       ; NOTE 4D5
0BE4: A0       ; NOTE 4R
0BE5: FF       ; END OF VOICE
;
;S5B Frog-home 1 
; Song=5 Voice=B
0BE6: 1F 0B    ; SC00:Use note set index 11  (note 1 = F#3)
0BE8: 5F 06    ; SC02:Set volume to 06
0BEA: 98       ; NOTE 8F#5
0BEB: 60       ; NOTE 16R
0BEC: 77       ; NOTE 16F5
0BED: B8       ; NOTE 4F#5
0BEE: B4       ; NOTE 4D5
0BEF: 98       ; NOTE 8F#5
0BF0: 60       ; NOTE 16R
0BF1: 77       ; NOTE 16F5
0BF2: B8       ; NOTE 4F#5
0BF3: B4       ; NOTE 4D5
0BF4: 98       ; NOTE 8F#5
0BF5: 60       ; NOTE 16R
0BF6: 76       ; NOTE 16E5
0BF7: B5       ; NOTE 4D#5
0BF8: 80       ; NOTE 8R
0BF9: 95       ; NOTE 8D#5
0BFA: 96       ; NOTE 8E5
0BFB: 97       ; NOTE 8F5
0BFC: B4       ; NOTE 4D5
0BFD: A0       ; NOTE 4R
0BFE: 8F       ; NOTE 8A4
0BFF: 60       ; NOTE 16R
0C00: 6F       ; NOTE 16A4
0C01: 8F       ; NOTE 8A4
0C02: 93       ; NOTE 8C#5
0C03: B6       ; NOTE 4E5
0C04: 8F       ; NOTE 8A4
0C05: 60       ; NOTE 16R
0C06: 6D       ; NOTE 16G4
0C07: 8C       ; NOTE 8F#4
0C08: 8F       ; NOTE 8A4
0C09: B4       ; NOTE 4D5
0C0A: 98       ; NOTE 8F#5
0C0B: 60       ; NOTE 16R
0C0C: 76       ; NOTE 16E5
0C0D: B4       ; NOTE 4D5
0C0E: 80       ; NOTE 8R
0C0F: 93       ; NOTE 8C#5
0C10: 8F       ; NOTE 8A4
0C11: 8D       ; NOTE 8G4
0C12: AC       ; NOTE 4F#4
0C13: A0       ; NOTE 4R
0C14: FF       ; END OF VOICE
```

# Song: Respawn

```code
;S3A New life begins
; Song=3 Voice=A
0C15: 1F 0B    ; SC00:Use note set index 11  (note 1 = F#3)
0C17: 3F 0E    ; SC01:Set tempo index 14 (175 quarters/minute)
0C19: 5F 06    ; SC02:Set volume to 06
0C1B: 8F       ; NOTE 8A4
0C1C: 60       ; NOTE 16R
0C1D: 6F       ; NOTE 16A4
0C1E: 93       ; NOTE 8C#5
0C1F: 96       ; NOTE 8E5
0C20: BB       ; NOTE 4A5
0C21: A0       ; NOTE 4R
0C22: 98       ; NOTE 8F#5
0C23: 60       ; NOTE 16R
0C24: 78       ; NOTE 16F#5
0C25: 9B       ; NOTE 8A5
0C26: 98       ; NOTE 8F#5
0C27: B6       ; NOTE 4E5
0C28: A0       ; NOTE 4R
0C29: FF       ; END OF VOICE
```

# Song: Frog Home 2

```code
;S6A Frog-home 2
; Song=6 Voice=A
0C2A: 1F 0B    ; SC00:Use note set index 11  (note 1 = F#3)
0C2C: 3F 0D    ; SC01:Set tempo index 13 (164 quarters/minute)
0C2E: 5F 06    ; SC02:Set volume to 06
0C30: 8D       ; NOTE 8G4
0C31: 96       ; NOTE 8E5
0C32: B6       ; NOTE 4E5
0C33: 80       ; NOTE 8R
0C34: 97       ; NOTE 8F5
0C35: B6       ; NOTE 4E5
0C36: 94       ; NOTE 8D5
0C37: 8D       ; NOTE 8G4
0C38: B4       ; NOTE 4D5
0C39: 8D       ; NOTE 8G4
0C3A: 97       ; NOTE 8F5
0C3B: B7       ; NOTE 4F5
0C3C: 80       ; NOTE 8R
0C3D: 99       ; NOTE 8G5
0C3E: B7       ; NOTE 4F5
0C3F: 96       ; NOTE 8E5
0C40: 8D       ; NOTE 8G4
0C41: B6       ; NOTE 4E5
0C42: 96       ; NOTE 8E5
0C43: 99       ; NOTE 8G5
0C44: B9       ; NOTE 4G5
0C45: 80       ; NOTE 8R
0C46: 9B       ; NOTE 8A5
0C47: B9       ; NOTE 4G5
0C48: 97       ; NOTE 8F5
0C49: 96       ; NOTE 8E5
0C4A: 94       ; NOTE 8D5
0C4B: 92       ; NOTE 8C5
0C4C: 91       ; NOTE 8B4
0C4D: 94       ; NOTE 8D5
0C4E: 9B       ; NOTE 8A5
0C4F: 99       ; NOTE 8G5
0C50: 97       ; NOTE 8F5
0C51: 91       ; NOTE 8B4
0C52: D2       ; NOTE 2C5
0C53: A0       ; NOTE 4R
0C54: FF       ; END OF VOICE
;
;S6B Frog-home 2
; Song=6 Voice=B
0C55: 1F 0B    ; SC00:Use note set index 11 (note 1 = F#3)
0C57: 5F 06    ; SC02:Set volume to 06
0C59: 8D       ; NOTE 8G4
0C5A: 92       ; NOTE 8C5
0C5B: B2       ; NOTE 4C5
0C5C: 80       ; NOTE 8R
0C5D: 91       ; NOTE 8B4
0C5E: B2       ; NOTE 4C5
0C5F: 91       ; NOTE 8B4
0C60: 8D       ; NOTE 8G4
0C61: B1       ; NOTE 4B4
0C62: 8D       ; NOTE 8G4
0C63: 94       ; NOTE 8D5
0C64: B4       ; NOTE 4D5
0C65: 80       ; NOTE 8R
0C66: 96       ; NOTE 8E5
0C67: B4       ; NOTE 4D5
0C68: 92       ; NOTE 8C5
0C69: 8D       ; NOTE 8G4
0C6A: B2       ; NOTE 4C5
0C6B: 92       ; NOTE 8C5
0C6C: 96       ; NOTE 8E5
0C6D: B6       ; NOTE 4E5
0C6E: 80       ; NOTE 8R
0C6F: 97       ; NOTE 8F5
0C70: B6       ; NOTE 4E5
0C71: 94       ; NOTE 8D5
0C72: 92       ; NOTE 8C5
0C73: 91       ; NOTE 8B4
0C74: 8F       ; NOTE 8A4
0C75: 8D       ; NOTE 8G4
0C76: 91       ; NOTE 8B4
0C77: 97       ; NOTE 8F5
0C78: 96       ; NOTE 8E5
0C79: 94       ; NOTE 8D5
0C7A: 8D       ; NOTE 8G4
0C7B: D2       ; NOTE 2C5
0C7C: A0       ; NOTE 4R
0C7D: FF       ; END OF VOICE
```

# Song: Frog Home 3

```code
;S7A Frog-home 3
; Song=7 Voice=A
0C7E: 1F 0B    ; SC00:Use note set index 11 (note 1 = F#3)
0C80: 3F 0D    ; SC01:Set tempo index 13 (164 quarters/minute)
0C82: 5F 06    ; SC02:Set volume to 06
0C84: C0       ; NOTE 2R
0C85: A0       ; NOTE 4R
0C86: 94       ; NOTE 8D5
0C87: 60       ; NOTE 16R
0C88: 75       ; NOTE 16D#5
0C89: 96       ; NOTE 8E5
0C8A: 9E       ; NOTE 8C6
0C8B: 96       ; NOTE 8E5
0C8C: 9E       ; NOTE 8C6
0C8D: B6       ; NOTE 4E5
0C8E: 96       ; NOTE 8E5
0C8F: 60       ; NOTE 16R
0C90: 75       ; NOTE 16D#5
0C91: 94       ; NOTE 8D5
0C92: 9D       ; NOTE 8B5
0C93: 94       ; NOTE 8D5
0C94: 9D       ; NOTE 8B5
0C95: B4       ; NOTE 4D5
0C96: 9D       ; NOTE 8B5
0C97: 60       ; NOTE 16R
0C98: 73       ; NOTE 16C#5
0C99: B2       ; NOTE 4C5
0C9A: BB       ; NOTE 4A5
0C9B: B9       ; NOTE 4G5
0C9C: B8       ; NOTE 4F#5
0C9D: B9       ; NOTE 4G5
0C9E: BB       ; NOTE 4A5
0C9F: BD       ; NOTE 4B5
0CA0: 94       ; NOTE 8D5
0CA1: 60       ; NOTE 16R
0CA2: 75       ; NOTE 16D#5
0CA3: 96       ; NOTE 8E5
0CA4: 92       ; NOTE 8C5
0CA5: 96       ; NOTE 8E5
0CA6: 92       ; NOTE 8C5
0CA7: B6       ; NOTE 4E5
0CA8: 96       ; NOTE 8E5
0CA9: 60       ; NOTE 16R
0CAA: 79       ; NOTE 16G5
0CAB: 94       ; NOTE 8D5
0CAC: 99       ; NOTE 8G5
0CAD: 94       ; NOTE 8D5
0CAE: 99       ; NOTE 8G5
0CAF: BD       ; NOTE 4B5
0CB0: 94       ; NOTE 8D5
0CB1: 60       ; NOTE 16R
0CB2: 74       ; NOTE 16D5
0CB3: B4       ; NOTE 4D5
0CB4: BB       ; NOTE 4A5
0CB5: B9       ; NOTE 4G5
0CB6: B8       ; NOTE 4F#5
0CB7: D9       ; NOTE 2G5
0CB8: C0       ; NOTE 2R
0CB9: FF       ; END OF VOICE
;
;S7B Frog-home 3
; Song=7 Voice=B
0CBA: 1F 05    ; SC00:Use note set index 5  (note 1 = F#2)
0CBC: 5F 06    ; SC02:Set volume to 06
0CBE: E0       ; NOTE 1R
0CBF: B2       ; NOTE 4C4
0CC0: 80       ; NOTE 8R
0CC1: 8D       ; NOTE 8G3
0CC2: 92       ; NOTE 8C4
0CC3: AD       ; NOTE 4G3
0CC4: 92       ; NOTE 8C4
0CC5: AD       ; NOTE 4G3
0CC6: 80       ; NOTE 8R
0CC7: 88       ; NOTE 8D3
0CC8: 8D       ; NOTE 8G3
0CC9: A8       ; NOTE 4D3
0CCA: 8D       ; NOTE 8G3
0CCB: A8       ; NOTE 4D3
0CCC: 80       ; NOTE 8R
0CCD: 88       ; NOTE 8D3
0CCE: 88       ; NOTE 8D3
0CCF: A8       ; NOTE 4D3
0CD0: 88       ; NOTE 8D3
0CD1: AD       ; NOTE 4G3
0CD2: 80       ; NOTE 8R
0CD3: 88       ; NOTE 8D3
0CD4: 8D       ; NOTE 8G3
0CD5: 94       ; NOTE 8D4
0CD6: 91       ; NOTE 8B3
0CD7: 8D       ; NOTE 8G3
0CD8: B2       ; NOTE 4C4
0CD9: 80       ; NOTE 8R
0CDA: 8D       ; NOTE 8G3
0CDB: 92       ; NOTE 8C4
0CDC: AD       ; NOTE 4G3
0CDD: 92       ; NOTE 8C4
0CDE: AD       ; NOTE 4G3
0CDF: 80       ; NOTE 8R
0CE0: 88       ; NOTE 8D3
0CE1: 8D       ; NOTE 8G3
0CE2: A8       ; NOTE 4D3
0CE3: 8D       ; NOTE 8G3
0CE4: 88       ; NOTE 8D3
0CE5: 94       ; NOTE 8D4
0CE6: 83       ; NOTE 8A2
0CE7: 94       ; NOTE 8D4
0CE8: 88       ; NOTE 8D3
0CE9: 94       ; NOTE 8D4
0CEA: 88       ; NOTE 8D3
0CEB: 94       ; NOTE 8D4
0CEC: E0       ; NOTE 1R
0CED: FF       ; END OF VOICE
```

# Song: Frog Home 4

```code
;S8A Frog-home 4
; Song=8 Voice=A
0CEE: 1F 0B    ; SC00:Use note set index 11 (note 1 = F#3)
0CF0: 3F 0D    ; SC01:Set tempo index 13 (164 quarters/minute)
0CF2: 5F 06    ; SC02:Set volume to 06
0CF4: B8       ; NOTE 4F#5
0CF5: 80       ; NOTE 8R
0CF6: 96       ; NOTE 8E5
0CF7: 96       ; NOTE 8E5
0CF8: 94       ; NOTE 8D5
0CF9: B3       ; NOTE 4C#5
0CFA: B1       ; NOTE 4B4
0CFB: 80       ; NOTE 8R
0CFC: AF       ; NOTE 4A4
0CFD: 8D       ; NOTE 8G4
0CFE: AC       ; NOTE 4F#4
0CFF: CA       ; NOTE 2E4
0D00: AF       ; NOTE 4A4
0D01: B6       ; NOTE 4E5
0D02: DB       ; NOTE 2A5
0D03: 9B       ; NOTE 8A5
0D04: 80       ; NOTE 8R
0D05: 8C       ; NOTE 8F#4
0D06: 8D       ; NOTE 8G4
0D07: AF       ; NOTE 4A4
0D08: B8       ; NOTE 4F#5
0D09: 94       ; NOTE 8D5
0D0A: 80       ; NOTE 8R
0D0B: 8C       ; NOTE 8F#4
0D0C: 8D       ; NOTE 8G4
0D0D: AF       ; NOTE 4A4
0D0E: B8       ; NOTE 4F#5
0D0F: 94       ; NOTE 8D5
0D10: 80       ; NOTE 8R
0D11: 98       ; NOTE 8F#5
0D12: 99       ; NOTE 8G5
0D13: B8       ; NOTE 4F#5
0D14: B6       ; NOTE 4E5
0D15: B8       ; NOTE 4F#5
0D16: B6       ; NOTE 4E5
0D17: D4       ; NOTE 2D5
0D18: A0       ; NOTE 4R
0D19: FF       ; END OF VOICE
;
;S8B Frog-home 4
; Song=8 Voice=B
0D1A: 1F 05    ; SC00:Use note set index 5 (note 1 = F#2)
0D1C: 5F 06    ; SC02:Set volume to 06
0D1E: A3       ; NOTE 4A2
0D1F: 80       ; NOTE 8R
0D20: AF       ; NOTE 4A3
0D21: 8F       ; NOTE 8A3
0D22: AF       ; NOTE 4A3
0D23: A3       ; NOTE 4A2
0D24: 80       ; NOTE 8R
0D25: AF       ; NOTE 4A3
0D26: 8F       ; NOTE 8A3
0D27: AF       ; NOTE 4A3
0D28: A3       ; NOTE 4A2
0D29: AF       ; NOTE 4A3
0D2A: AF       ; NOTE 4A3
0D2B: AF       ; NOTE 4A3
0D2C: A3       ; NOTE 4A2
0D2D: AF       ; NOTE 4A3
0D2E: 8F       ; NOTE 8A3
0D2F: 8F       ; NOTE 8A3
0D30: 83       ; NOTE 8A2
0D31: 83       ; NOTE 8A2
0D32: A8       ; NOTE 4D3
0D33: B4       ; NOTE 4D4
0D34: A8       ; NOTE 4D3
0D35: B4       ; NOTE 4D4
0D36: A8       ; NOTE 4D3
0D37: B4       ; NOTE 4D4
0D38: A8       ; NOTE 4D3
0D39: B4       ; NOTE 4D4
0D3A: AA       ; NOTE 4E3
0D3B: B3       ; NOTE 4C#4
0D3C: AF       ; NOTE 4A3
0D3D: B3       ; NOTE 4C#4
0D3E: B4       ; NOTE 4D4
0D3F: AF       ; NOTE 4A3
0D40: 88       ; NOTE 8D3
0D41: 80       ; NOTE 8R
0D42: FF       ; END OF VOICE
```

# Song: Frog Home 5

```code
;S9A Frog-home 5
; Song=9 Voice=A
0D43: 1F 0B    ; SC00:Use note set index 11 (note 1 = F#3)
0D45: 3F 0D    ; SC01:Set tempo index 13 (164 quarters/minute)
0D47: 5F 06    ; SC02:Set volume to 06
0D49: 98       ; NOTE 8F#5
0D4A: 98       ; NOTE 8F#5
0D4B: 98       ; NOTE 8F#5
0D4C: 98       ; NOTE 8F#5
0D4D: 98       ; NOTE 8F#5
0D4E: 98       ; NOTE 8F#5
0D4F: 96       ; NOTE 8E5
0D50: 98       ; NOTE 8F#5
0D51: 99       ; NOTE 8G5
0D52: B1       ; NOTE 4B4
0D53: 80       ; NOTE 8R
0D54: B1       ; NOTE 4B4
0D55: B1       ; NOTE 4B4
0D56: 96       ; NOTE 8E5
0D57: 96       ; NOTE 8E5
0D58: 96       ; NOTE 8E5
0D59: 96       ; NOTE 8E5
0D5A: B6       ; NOTE 4E5
0D5B: 94       ; NOTE 8D5
0D5C: 96       ; NOTE 8E5
0D5D: 98       ; NOTE 8F#5
0D5E: AF       ; NOTE 4A4
0D5F: 80       ; NOTE 8R
0D60: AF       ; NOTE 4A4
0D61: AF       ; NOTE 4A4
0D62: 98       ; NOTE 8F#5
0D63: 98       ; NOTE 8F#5
0D64: 98       ; NOTE 8F#5
0D65: 98       ; NOTE 8F#5
0D66: 98       ; NOTE 8F#5
0D67: 98       ; NOTE 8F#5
0D68: 96       ; NOTE 8E5
0D69: 98       ; NOTE 8F#5
0D6A: 99       ; NOTE 8G5
0D6B: 99       ; NOTE 8G5
0D6C: 99       ; NOTE 8G5
0D6D: 99       ; NOTE 8G5
0D6E: B1       ; NOTE 4B4
0D6F: 91       ; NOTE 8B4
0D70: 94       ; NOTE 8D5
0D71: 93       ; NOTE 8C#5
0D72: B3       ; NOTE 4C#5
0D73: 80       ; NOTE 8R
0D74: 8F       ; NOTE 8A4
0D75: 8F       ; NOTE 8A4
0D76: 98       ; NOTE 8F#5
0D77: 96       ; NOTE 8E5
0D78: D4       ; NOTE 2D5
0D79: A0       ; NOTE 4R
0D7A: FF       ; END OF VOICE
;
;S9B Frog-home 5
; Song=9 Voice=B
0D7B: 1F 05    ; SC00:Use note set index 5  (note 1 = F#2)
0D7D: 5F 06    ; SC02:Set volume to 06
0D7F: A8       ; NOTE 4D3
0D80: 80       ; NOTE 8R
0D81: 88       ; NOTE 8D3
0D82: C8       ; NOTE 2D3
0D83: AA       ; NOTE 4E3
0D84: 80       ; NOTE 8R
0D85: 8A       ; NOTE 8E3
0D86: CA       ; NOTE 2E3
0D87: AF       ; NOTE 4A3
0D88: 80       ; NOTE 8R
0D89: 8F       ; NOTE 8A3
0D8A: CF       ; NOTE 2A3
0D8B: B4       ; NOTE 4D4
0D8C: 80       ; NOTE 8R
0D8D: 8F       ; NOTE 8A3
0D8E: AF       ; NOTE 4A3
0D8F: AC       ; NOTE 4F#3
0D90: A8       ; NOTE 4D3
0D91: 80       ; NOTE 8R
0D92: 88       ; NOTE 8D3
0D93: C8       ; NOTE 2D3
0D94: AA       ; NOTE 4E3
0D95: 80       ; NOTE 8R
0D96: 8A       ; NOTE 8E3
0D97: CA       ; NOTE 2E3
0D98: A3       ; NOTE 4A2
0D99: 80       ; NOTE 8R
0D9A: 83       ; NOTE 8A2
0D9B: C3       ; NOTE 2A2
0D9C: A8       ; NOTE 4D3
0D9D: C0       ; NOTE 2R
0D9E: FF       ; END OF VOICE
```

# Song: Frog Home 6

```code
;S10A Frog-home 6
; Song=10 Voice=A
0D9F: 1F 0B    ; SC00:Use note set index 11 (note 1 = F#3)
0DA1: 3F 0D    ; SC01:Set tempo index 13 (164 quarters/minute)
0DA3: 5F 06    ; SC02:Set volume to 06
0DA5: 94       ; NOTE 8D5
0DA6: 60       ; NOTE 16R
0DA7: 72       ; NOTE 16C5
0DA8: 91       ; NOTE 8B4
0DA9: 94       ; NOTE 8D5
0DAA: B9       ; NOTE 4G5
0DAB: 9B       ; NOTE 8A5
0DAC: 99       ; NOTE 8G5
0DAD: 96       ; NOTE 8E5
0DAE: 99       ; NOTE 8G5
0DAF: AF       ; NOTE 4A4
0DB0: 9B       ; NOTE 8A5
0DB1: 60       ; NOTE 16R
0DB2: 79       ; NOTE 16G5
0DB3: 98       ; NOTE 8F#5
0DB4: 60       ; NOTE 16R
0DB5: 76       ; NOTE 16E5
0DB6: 94       ; NOTE 8D5
0DB7: 94       ; NOTE 8D5
0DB8: 96       ; NOTE 8E5
0DB9: 94       ; NOTE 8D5
0DBA: D4       ; NOTE 2D5
0DBB: 94       ; NOTE 8D5
0DBC: 60       ; NOTE 16R
0DBD: 72       ; NOTE 16C5
0DBE: 91       ; NOTE 8B4
0DBF: 94       ; NOTE 8D5
0DC0: B9       ; NOTE 4G5
0DC1: 9B       ; NOTE 8A5
0DC2: 99       ; NOTE 8G5
0DC3: 96       ; NOTE 8E5
0DC4: 99       ; NOTE 8G5
0DC5: AF       ; NOTE 4A4
0DC6: 9B       ; NOTE 8A5
0DC7: 60       ; NOTE 16R
0DC8: 79       ; NOTE 16G5
0DC9: 98       ; NOTE 8F#5
0DCA: 60       ; NOTE 16R
0DCB: 76       ; NOTE 16E5
0DCC: 94       ; NOTE 8D5
0DCD: 94       ; NOTE 8D5
0DCE: 96       ; NOTE 8E5
0DCF: 98       ; NOTE 8F#5
0DD0: D9       ; NOTE 2G5
0DD1: FF       ; END OF VOICE
;
;S10B Frog-home 6
; Song=10 Voice=B
0DD2: 1F 0B    ; SC00:Use note set index 11 (note 1 = F#3)
0DD4: 5F 06    ; SC02:Set volume to 06
0DD6: 94       ; NOTE 8D5
0DD7: 60       ; NOTE 16R
0DD8: 72       ; NOTE 16C5
0DD9: 91       ; NOTE 8B4
0DDA: 94       ; NOTE 8D5
0DDB: B9       ; NOTE 4G5
0DDC: 98       ; NOTE 8F#5
0DDD: 94       ; NOTE 8D5
0DDE: 92       ; NOTE 8C5
0DDF: 91       ; NOTE 8B4
0DE0: B2       ; NOTE 4C5
0DE1: 92       ; NOTE 8C5
0DE2: 60       ; NOTE 16R
0DE3: 76       ; NOTE 16E5
0DE4: 94       ; NOTE 8D5
0DE5: 60       ; NOTE 16R
0DE6: 74       ; NOTE 16D5
0DE7: 92       ; NOTE 8C5
0DE8: 92       ; NOTE 8C5
0DE9: 92       ; NOTE 8C5
0DEA: 92       ; NOTE 8C5
0DEB: D1       ; NOTE 2B4
0DEC: 94       ; NOTE 8D5
0DED: 60       ; NOTE 16R
0DEE: 72       ; NOTE 16C5
0DEF: 91       ; NOTE 8B4
0DF0: 94       ; NOTE 8D5
0DF1: B9       ; NOTE 4G5
0DF2: 98       ; NOTE 8F#5
0DF3: 94       ; NOTE 8D5
0DF4: 92       ; NOTE 8C5
0DF5: 91       ; NOTE 8B4
0DF6: B2       ; NOTE 4C5
0DF7: 92       ; NOTE 8C5
0DF8: 60       ; NOTE 16R
0DF9: 76       ; NOTE 16E5
0DFA: 94       ; NOTE 8D5
0DFB: 60       ; NOTE 16R
0DFC: 74       ; NOTE 16D5
0DFD: 92       ; NOTE 8C5
0DFE: 92       ; NOTE 8C5
0DFF: 92       ; NOTE 8C5
0E00: 92       ; NOTE 8C5
0E01: D1       ; NOTE 2B4
0E02: FF       ; END OF VOICE
```

# Song: Frog Home 7

```code
;S11A Frog-home 7
; Song=11 Voice=A
0E03: 1F 0B    ; SC00:Use note set index 11 (note 1 = F#3)
0E05: 3F 0D    ; SC01:Set tempo index 13 (164 quarters/minute)
0E07: 5F 06    ; SC02:Set volume to 06
0E09: 88       ; NOTE 8D4
0E0A: 86       ; NOTE 8C4
0E0B: 65       ; NOTE 16B3
0E0C: 68       ; NOTE 16D4
0E0D: 6D       ; NOTE 16G4
0E0E: 71       ; NOTE 16B4
0E0F: B4       ; NOTE 4D5
0E10: 80       ; NOTE 8R
0E11: 92       ; NOTE 8C5
0E12: 71       ; NOTE 16B4
0E13: 74       ; NOTE 16D5
0E14: 6D       ; NOTE 16G4
0E15: 71       ; NOTE 16B4
0E16: A8       ; NOTE 4D4
0E17: 80       ; NOTE 8R
0E18: 91       ; NOTE 8B4
0E19: 6F       ; NOTE 16A4
0E1A: 72       ; NOTE 16C5
0E1B: 6C       ; NOTE 16F#4
0E1C: 6F       ; NOTE 16A4
0E1D: A8       ; NOTE 4D4
0E1E: 80       ; NOTE 8R
0E1F: 92       ; NOTE 8C5
0E20: 71       ; NOTE 16B4
0E21: 74       ; NOTE 16D5
0E22: 6D       ; NOTE 16G4
0E23: 71       ; NOTE 16B4
0E24: A8       ; NOTE 4D4
0E25: 88       ; NOTE 8D4
0E26: 60       ; NOTE 16R
0E27: 66       ; NOTE 16C4
0E28: 65       ; NOTE 16B3
0E29: 68       ; NOTE 16D4
0E2A: 6D       ; NOTE 16G4
0E2B: 71       ; NOTE 16B4
0E2C: B4       ; NOTE 4D5
0E2D: 8D       ; NOTE 8G4
0E2E: 60       ; NOTE 16R
0E2F: 6B       ; NOTE 16F4
0E30: 6A       ; NOTE 16E4
0E31: 6D       ; NOTE 16G4
0E32: 72       ; NOTE 16C5
0E33: 76       ; NOTE 16E5
0E34: B9       ; NOTE 4G5
0E35: 98       ; NOTE 8F#5
0E36: 96       ; NOTE 8E5
0E37: 94       ; NOTE 8D5
0E38: 60       ; NOTE 16R
0E39: 71       ; NOTE 16B4
0E3A: 96       ; NOTE 8E5
0E3B: 60       ; NOTE 16R
0E3C: 71       ; NOTE 16B4
0E3D: 94       ; NOTE 8D5
0E3E: 60       ; NOTE 16R
0E3F: 71       ; NOTE 16B4
0E40: 72       ; NOTE 16C5
0E41: 68       ; NOTE 16D4
0E42: 6C       ; NOTE 16F#4
0E43: 6F       ; NOTE 16A4
0E44: B4       ; NOTE 4D5
0E45: 80       ; NOTE 8R
0E46: 92       ; NOTE 8C5
0E47: 71       ; NOTE 16B4
0E48: 68       ; NOTE 16D4
0E49: 6D       ; NOTE 16G4
0E4A: 71       ; NOTE 16B4
0E4B: B4       ; NOTE 4D5
0E4C: 80       ; NOTE 8R
0E4D: 91       ; NOTE 8B4
0E4E: 6F       ; NOTE 16A4
0E4F: 68       ; NOTE 16D4
0E50: 71       ; NOTE 16B4
0E51: 60       ; NOTE 16R
0E52: 6F       ; NOTE 16A4
0E53: 68       ; NOTE 16D4
0E54: 71       ; NOTE 16B4
0E55: 60       ; NOTE 16R
0E56: 6F       ; NOTE 16A4
0E57: 68       ; NOTE 16D4
0E58: 74       ; NOTE 16D5
0E59: 60       ; NOTE 16R
0E5A: D9       ; NOTE 2G5
0E5B: FF       ; END OF VOICE
;
;S11B Frog-home 7
; Song=11 Voice=B
0E5C: 1F 0B    ; SC00:Use note set index 11 (note 1 = F#3)
0E5E: 5F 06    ; SC02:Set volume to 06
0E60: A0       ; NOTE 4R
0E61: AD       ; NOTE 4G4
0E62: AC       ; NOTE 4F#4
0E63: A0       ; NOTE 4R
0E64: AA       ; NOTE 4E4
0E65: A8       ; NOTE 4D4
0E66: A0       ; NOTE 4R
0E67: A6       ; NOTE 4C4
0E68: A5       ; NOTE 4B3
0E69: A0       ; NOTE 4R
0E6A: A8       ; NOTE 4D4
0E6B: A6       ; NOTE 4C4
0E6C: A0       ; NOTE 4R
0E6D: AD       ; NOTE 4G4
0E6E: A7       ; NOTE 4C#4
0E6F: A0       ; NOTE 4R
0E70: AA       ; NOTE 4E4
0E71: A8       ; NOTE 4D4
0E72: A0       ; NOTE 4R
0E73: A5       ; NOTE 4B3
0E74: A6       ; NOTE 4C4
0E75: A5       ; NOTE 4B3
0E76: A8       ; NOTE 4D4
0E77: A6       ; NOTE 4C4
0E78: A0       ; NOTE 4R
0E79: A8       ; NOTE 4D4
0E7A: A5       ; NOTE 4B3
0E7B: A0       ; NOTE 4R
0E7C: A6       ; NOTE 4C4
0E7D: A8       ; NOTE 4D4
0E7E: A6       ; NOTE 4C4
0E7F: C5       ; NOTE 2B3
0E80: FF       ; END OF VOICE
```

# Song: Frog Home 8

```code
;S12A Frog-home 8
; Song=12 Voice=A
0E81: 1F 0B    ; SC00:Use note set index 11  (note 1 = F#3)
0E83: 3F 0D    ; SC01:Set tempo index 13 (164 quarters/minute)
0E85: 5F 06    ; SC02:Set volume to 06
0E87: 94       ; NOTE 8D5
0E88: 99       ; NOTE 8G5
0E89: 99       ; NOTE 8G5
0E8A: 9B       ; NOTE 8A5
0E8B: 9B       ; NOTE 8A5
0E8C: 9D       ; NOTE 8B5
0E8D: 9D       ; NOTE 8B5
0E8E: 98       ; NOTE 8F#5
0E8F: 9B       ; NOTE 8A5
0E90: B9       ; NOTE 4G5
0E91: B6       ; NOTE 4E5
0E92: B4       ; NOTE 4D5
0E93: 80       ; NOTE 8R
0E94: 92       ; NOTE 8C5
0E95: 91       ; NOTE 8B4
0E96: 8F       ; NOTE 8A4
0E97: 91       ; NOTE 8B4
0E98: 92       ; NOTE 8C5
0E99: 94       ; NOTE 8D5
0E9A: B4       ; NOTE 4D5
0E9B: 99       ; NOTE 8G5
0E9C: 98       ; NOTE 8F#5
0E9D: 94       ; NOTE 8D5
0E9E: 96       ; NOTE 8E5
0E9F: 98       ; NOTE 8F#5
0EA0: B9       ; NOTE 4G5
0EA1: 80       ; NOTE 8R
0EA2: 92       ; NOTE 8C5
0EA3: 91       ; NOTE 8B4
0EA4: 8F       ; NOTE 8A4
0EA5: 91       ; NOTE 8B4
0EA6: 92       ; NOTE 8C5
0EA7: 94       ; NOTE 8D5
0EA8: B4       ; NOTE 4D5
0EA9: 99       ; NOTE 8G5
0EAA: 98       ; NOTE 8F#5
0EAB: 94       ; NOTE 8D5
0EAC: 96       ; NOTE 8E5
0EAD: 98       ; NOTE 8F#5
0EAE: B9       ; NOTE 4G5
0EAF: FF       ; END OF VOICE
;
;S12B Frog-home 8
; Song=12 Voice=B
0EB0: 1F 0B    ; SC00:Use note set index 11 (note 1 = F#3)
0EB2: 5F 06    ; SC02:Set volume to 06
0EB4: 94       ; NOTE 8D5
0EB5: 94       ; NOTE 8D5
0EB6: 94       ; NOTE 8D5
0EB7: 94       ; NOTE 8D5
0EB8: 94       ; NOTE 8D5
0EB9: 94       ; NOTE 8D5
0EBA: 94       ; NOTE 8D5
0EBB: 92       ; NOTE 8C5
0EBC: 92       ; NOTE 8C5
0EBD: B1       ; NOTE 4B4
0EBE: B3       ; NOTE 4C#5
0EBF: B4       ; NOTE 4D5
0EC0: 80       ; NOTE 8R
0EC1: 8F       ; NOTE 8A4
0EC2: 8D       ; NOTE 8G4
0EC3: 8C       ; NOTE 8F#4
0EC4: 8D       ; NOTE 8G4
0EC5: 8F       ; NOTE 8A4
0EC6: 8F       ; NOTE 8A4
0EC7: 8F       ; NOTE 8A4
0EC8: B4       ; NOTE 4D5
0EC9: 92       ; NOTE 8C5
0ECA: 92       ; NOTE 8C5
0ECB: 92       ; NOTE 8C5
0ECC: 92       ; NOTE 8C5
0ECD: B1       ; NOTE 4B4
0ECE: 80       ; NOTE 8R
0ECF: 8F       ; NOTE 8A4
0ED0: 8D       ; NOTE 8G4
0ED1: 8C       ; NOTE 8F#4
0ED2: 8D       ; NOTE 8G4
0ED3: 8F       ; NOTE 8A4
0ED4: 8F       ; NOTE 8A4
0ED5: 8F       ; NOTE 8A4
0ED6: B4       ; NOTE 4D5
0ED7: 92       ; NOTE 8C5
0ED8: 92       ; NOTE 8C5
0ED9: 92       ; NOTE 8C5
0EDA: 92       ; NOTE 8C5
0EDB: B1       ; NOTE 4B4
0EDC: FF       ; END OF VOICE
```

# Song: Frog Home 9

```code
;S13A Frog-home 9
; Song=13 Voice=A
0EDD: 1F 0B    ; SC00:Use note set index 11 (note 1 = F#3)
0EDF: 3F 0D    ; SC01:Set tempo index 13 (164 quarters/minute)
0EE1: 5F 06    ; SC02:Set volume to 06
0EE3: 87       ; NOTE 8C#4
0EE4: 60       ; NOTE 16R
0EE5: 68       ; NOTE 16D4
0EE6: AA       ; NOTE 4E4
0EE7: 80       ; NOTE 8R
0EE8: 8F       ; NOTE 8A4
0EE9: 8E       ; NOTE 8G#4
0EEA: 60       ; NOTE 16R
0EEB: 6C       ; NOTE 16F#4
0EEC: CA       ; NOTE 2E4
0EED: 8F       ; NOTE 8A4
0EEE: 60       ; NOTE 16R
0EEF: 6F       ; NOTE 16A4
0EF0: 6E       ; NOTE 16G#4
0EF1: 71       ; NOTE 16B4
0EF2: 94       ; NOTE 8D5
0EF3: 9A       ; NOTE 8G#5
0EF4: 60       ; NOTE 16R
0EF5: 78       ; NOTE 16F#5
0EF6: 96       ; NOTE 8E5
0EF7: 8E       ; NOTE 8G#4
0EF8: 8F       ; NOTE 8A4
0EF9: 93       ; NOTE 8C#5
0EFA: 8A       ; NOTE 8E4
0EFB: 80       ; NOTE 8R
0EFC: 87       ; NOTE 8C#4
0EFD: 60       ; NOTE 16R
0EFE: 68       ; NOTE 16D4
0EFF: AA       ; NOTE 4E4
0F00: 80       ; NOTE 8R
0F01: 8F       ; NOTE 8A4
0F02: 8E       ; NOTE 8G#4
0F03: 60       ; NOTE 16R
0F04: 6C       ; NOTE 16F#4
0F05: CA       ; NOTE 2E4
0F06: 8F       ; NOTE 8A4
0F07: 60       ; NOTE 16R
0F08: 6F       ; NOTE 16A4
0F09: 6E       ; NOTE 16G#4
0F0A: 71       ; NOTE 16B4
0F0B: 94       ; NOTE 8D5
0F0C: 9A       ; NOTE 8G#5
0F0D: 60       ; NOTE 16R
0F0E: 78       ; NOTE 16F#5
0F0F: 96       ; NOTE 8E5
0F10: 8E       ; NOTE 8G#4
0F11: CF       ; NOTE 2A4
0F12: FF       ; END OF VOICE
;
;S13B Frog-home 9
; Song=13 Voice=B
0F13: 1F 0B    ; SC00:Use note set index 11 (note 1 = F#3)
0F15: 5F 06    ; SC02:Set volume to 06
0F17: 87       ; NOTE 8C#4
0F18: 60       ; NOTE 16R
0F19: 68       ; NOTE 16D4
0F1A: AA       ; NOTE 4E4
0F1B: 80       ; NOTE 8R
0F1C: 8F       ; NOTE 8A4
0F1D: 8E       ; NOTE 8G#4
0F1E: 60       ; NOTE 16R
0F1F: 6C       ; NOTE 16F#4
0F20: CA       ; NOTE 2E4
0F21: 8F       ; NOTE 8A4
0F22: 60       ; NOTE 16R
0F23: 6F       ; NOTE 16A4
0F24: 6E       ; NOTE 16G#4
0F25: 6E       ; NOTE 16G#4
0F26: 91       ; NOTE 8B4
0F27: 96       ; NOTE 8E5
0F28: 60       ; NOTE 16R
0F29: 74       ; NOTE 16D5
0F2A: 91       ; NOTE 8B4
0F2B: 88       ; NOTE 8D4
0F2C: 87       ; NOTE 8C#4
0F2D: 88       ; NOTE 8D4
0F2E: 87       ; NOTE 8C#4
0F2F: 80       ; NOTE 8R
0F30: 87       ; NOTE 8C#4
0F31: 60       ; NOTE 16R
0F32: 68       ; NOTE 16D4
0F33: AA       ; NOTE 4E4
0F34: 80       ; NOTE 8R
0F35: 87       ; NOTE 8C#4
0F36: 88       ; NOTE 8D4
0F37: 60       ; NOTE 16R
0F38: 68       ; NOTE 16D4
0F39: C7       ; NOTE 2C#4
0F3A: 8F       ; NOTE 8A4
0F3B: 60       ; NOTE 16R
0F3C: 6F       ; NOTE 16A4
0F3D: 6E       ; NOTE 16G#4
0F3E: 6E       ; NOTE 16G#4
0F3F: 91       ; NOTE 8B4
0F40: 96       ; NOTE 8E5
0F41: 60       ; NOTE 16R
0F42: 74       ; NOTE 16D5
0F43: 91       ; NOTE 8B4
0F44: 88       ; NOTE 8D4
0F45: C7       ; NOTE 2C#4
0F46: FF       ; END OF VOICE
```

# Song: Frog Home 10

```code
;S14A Frog-home 10
; Song=14 Voice=A
0F47: 1F 0B    ; SC00:Use note set index 11 (note 1 = F#3)
0F49: 3F 0D    ; SC01:Set tempo index 13 (164 quarters/minute)
0F4B: 5F 06    ; SC02:Set volume to 06
0F4D: 8A       ; NOTE 8E4
0F4E: 8F       ; NOTE 8A4
0F4F: 8E       ; NOTE 8G#4
0F50: 91       ; NOTE 8B4
0F51: AA       ; NOTE 4E4
0F52: 8C       ; NOTE 8F#4
0F53: 8E       ; NOTE 8G#4
0F54: 8F       ; NOTE 8A4
0F55: 93       ; NOTE 8C#5
0F56: AA       ; NOTE 4E4
0F57: 8A       ; NOTE 8E4
0F58: 8F       ; NOTE 8A4
0F59: 8E       ; NOTE 8G#4
0F5A: 91       ; NOTE 8B4
0F5B: AA       ; NOTE 4E4
0F5C: 8C       ; NOTE 8F#4
0F5D: 8E       ; NOTE 8G#4
0F5E: 8F       ; NOTE 8A4
0F5F: 93       ; NOTE 8C#5
0F60: AA       ; NOTE 4E4
0F61: 87       ; NOTE 8C#4
0F62: 60       ; NOTE 16R
0F63: 68       ; NOTE 16D4
0F64: AA       ; NOTE 4E4
0F65: 80       ; NOTE 8R
0F66: 8F       ; NOTE 8A4
0F67: 8E       ; NOTE 8G#4
0F68: 60       ; NOTE 16R
0F69: 6C       ; NOTE 16F#4
0F6A: CA       ; NOTE 2E4
0F6B: 8F       ; NOTE 8A4
0F6C: 60       ; NOTE 16R
0F6D: 6F       ; NOTE 16A4
0F6E: 6E       ; NOTE 16G#4
0F6F: 71       ; NOTE 16B4
0F70: 94       ; NOTE 8D5
0F71: 9A       ; NOTE 8G#5
0F72: 60       ; NOTE 16R
0F73: 78       ; NOTE 16F#5
0F74: 96       ; NOTE 8E5
0F75: 8E       ; NOTE 8G#4
0F76: CF       ; NOTE 2A4
0F77: FF       ; END OF VOICE
;
;S14B Frog-home 10
; Song=14 Voice=B
0F78: 1F 0B    ; SC00:Use note set index 11 (note 1 = F#3)
0F7A: 5F 06    ; SC02:Set volume to 06
0F7C: 8A       ; NOTE 8E4
0F7D: 87       ; NOTE 8C#4
0F7E: 88       ; NOTE 8D4
0F7F: 88       ; NOTE 8D4
0F80: A8       ; NOTE 4D4
0F81: 88       ; NOTE 8D4
0F82: 88       ; NOTE 8D4
0F83: 87       ; NOTE 8C#4
0F84: 8A       ; NOTE 8E4
0F85: A7       ; NOTE 4C#4
0F86: 87       ; NOTE 8C#4
0F87: 87       ; NOTE 8C#4
0F88: 88       ; NOTE 8D4
0F89: 88       ; NOTE 8D4
0F8A: A8       ; NOTE 4D4
0F8B: 88       ; NOTE 8D4
0F8C: 88       ; NOTE 8D4
0F8D: 87       ; NOTE 8C#4
0F8E: 8A       ; NOTE 8E4
0F8F: A7       ; NOTE 4C#4
0F90: 87       ; NOTE 8C#4
0F91: 60       ; NOTE 16R
0F92: 68       ; NOTE 16D4
0F93: AA       ; NOTE 4E4
0F94: 80       ; NOTE 8R
0F95: 87       ; NOTE 8C#4
0F96: 88       ; NOTE 8D4
0F97: 60       ; NOTE 16R
0F98: 68       ; NOTE 16D4
0F99: C7       ; NOTE 2C#4
0F9A: 8F       ; NOTE 8A4
0F9B: 60       ; NOTE 16R
0F9C: 6F       ; NOTE 16A4
0F9D: 6E       ; NOTE 16G#4
0F9E: 6E       ; NOTE 16G#4
0F9F: 91       ; NOTE 8B4
0FA0: 96       ; NOTE 8E5
0FA1: 60       ; NOTE 16R
0FA2: 74       ; NOTE 16D5
0FA3: 91       ; NOTE 8B4
0FA4: 88       ; NOTE 8D4
0FA5: C7       ; NOTE 2C#4
0FA6: FF       ; END OF VOICE
```

# Song: Frog Home 11

```code
;S15A Frog-home 11
; Song=15 Voice=A
0FA7: 1F 0B    ; SC00:Use note set index 11 (note 1 = F#3)
0FA9: 3F 0C    ; SC01:Set tempo index 12 (154 quarters/minute)
0FAB: 5F 06    ; SC02:Set volume to 06
0FAD: B4       ; NOTE 4D5
0FAE: 91       ; NOTE 8B4
0FAF: 8D       ; NOTE 8G4
0FB0: B9       ; NOTE 4G5
0FB1: 98       ; NOTE 8F#5
0FB2: 96       ; NOTE 8E5
0FB3: B4       ; NOTE 4D5
0FB4: 99       ; NOTE 8G5
0FB5: 91       ; NOTE 8B4
0FB6: 8F       ; NOTE 8A4
0FB7: B4       ; NOTE 4D5
0FB8: 80       ; NOTE 8R
0FB9: 94       ; NOTE 8D5
0FBA: 94       ; NOTE 8D5
0FBB: 94       ; NOTE 8D5
0FBC: 94       ; NOTE 8D5
0FBD: 96       ; NOTE 8E5
0FBE: 94       ; NOTE 8D5
0FBF: 91       ; NOTE 8B4
0FC0: 8D       ; NOTE 8G4
0FC1: 99       ; NOTE 8G5
0FC2: 99       ; NOTE 8G5
0FC3: 99       ; NOTE 8G5
0FC4: 99       ; NOTE 8G5
0FC5: 9B       ; NOTE 8A5
0FC6: 99       ; NOTE 8G5
0FC7: 96       ; NOTE 8E5
0FC8: 92       ; NOTE 8C5
0FC9: 94       ; NOTE 8D5
0FCA: 94       ; NOTE 8D5
0FCB: 94       ; NOTE 8D5
0FCC: 94       ; NOTE 8D5
0FCD: 96       ; NOTE 8E5
0FCE: 94       ; NOTE 8D5
0FCF: 91       ; NOTE 8B4
0FD0: 8D       ; NOTE 8G4
0FD1: 99       ; NOTE 8G5
0FD2: 99       ; NOTE 8G5
0FD3: 99       ; NOTE 8G5
0FD4: 99       ; NOTE 8G5
0FD5: 9B       ; NOTE 8A5
0FD6: 99       ; NOTE 8G5
0FD7: 96       ; NOTE 8E5
0FD8: 92       ; NOTE 8C5
0FD9: 94       ; NOTE 8D5
0FDA: 91       ; NOTE 8B4
0FDB: 80       ; NOTE 8R
0FDC: 91       ; NOTE 8B4
0FDD: B9       ; NOTE 4G5
0FDE: B1       ; NOTE 4B4
0FDF: 94       ; NOTE 8D5
0FE0: CF       ; NOTE 2A4
0FE1: FF       ; END OF VOICE
;
;S15B Frog-home 11
; Song=15 Voice=B
0FE2: 1F 05    ; SC00:Use note set index 5 (note 1 = F#2)
0FE4: 5F 06    ; SC02:Set volume to 06
0FE6: D9       ; NOTE 2G4
0FE7: D6       ; NOTE 2E4
0FE8: D9       ; NOTE 2G4
0FE9: D8       ; NOTE 2F#4
0FEA: 8D       ; NOTE 8G3
0FEB: 91       ; NOTE 8B3
0FEC: 88       ; NOTE 8D3
0FED: 91       ; NOTE 8B3
0FEE: 8D       ; NOTE 8G3
0FEF: 91       ; NOTE 8B3
0FF0: 88       ; NOTE 8D3
0FF1: 91       ; NOTE 8B3
0FF2: 8D       ; NOTE 8G3
0FF3: 92       ; NOTE 8C4
0FF4: 8A       ; NOTE 8E3
0FF5: 92       ; NOTE 8C4
0FF6: 8D       ; NOTE 8G3
0FF7: 92       ; NOTE 8C4
0FF8: 8A       ; NOTE 8E3
0FF9: 92       ; NOTE 8C4
0FFA: 8D       ; NOTE 8G3
0FFB: 91       ; NOTE 8B3
0FFC: 88       ; NOTE 8D3
0FFD: 91       ; NOTE 8B3
0FFE: 8D       ; NOTE 8G3
0FFF: 91       ; NOTE 8B3
1000: 88       ; NOTE 8D3
1001: 91       ; NOTE 8B3
1002: 8D       ; NOTE 8G3
1003: 92       ; NOTE 8C4
1004: 8A       ; NOTE 8E3
1005: 92       ; NOTE 8C4
1006: 8D       ; NOTE 8G3
1007: 92       ; NOTE 8C4
1008: 8A       ; NOTE 8E3
1009: 92       ; NOTE 8C4
100A: 8D       ; NOTE 8G3
100B: 91       ; NOTE 8B3
100C: 88       ; NOTE 8D3
100D: 91       ; NOTE 8B3
100E: 8D       ; NOTE 8G3
100F: 91       ; NOTE 8B3
1010: 88       ; NOTE 8D3
1011: 91       ; NOTE 8B3
1012: 8F       ; NOTE 8A3
1013: 94       ; NOTE 8D4
1014: FF       ; END OF VOICE

;I0F Main song
1015: E7              RST     $20                 
1016: AF              XOR     A                   
1017: 32 C8 42        LD      ($42C8),A           ; {ram.m42C8}
101A: 3E 19           LD      A,$19               
101C: 32 A3 42        LD      ($42A3),A           ; {ram.m42A3}
101F: F7              RST     $30                 
1020: C3 61 09        JP      $0961               ; {}

;I16 Music voice B
1023: E7              RST     $20                 
1024: F7              RST     $30                 
1025: C9              RET                         

;C0F Main song
1026: DD 21 80 42     LD      IX,$4280            
102A: C3 A1 07        JP      $07A1               ; {}

;C16 Music voice B
102D: DD 21 88 42     LD      IX,$4288            
1031: C3 A1 07        JP      $07A1               ; {}
```

# Song: Main song

```code
;S25A Main song
; Song=25 Voice=A
1034: 1F 0B    ; SC00:Use note set index 11  (note 1 = F#3)
1036: 3F 0C    ; SC01:Set tempo index 12 (154 quarters/minute)
1038: 5F 05    ; SC02:Set volume to 05
103A: B4       ; NOTE 4D5
103B: 91       ; NOTE 8B4
103C: 8D       ; NOTE 8G4
103D: B9       ; NOTE 4G5
103E: 98       ; NOTE 8F#5
103F: 96       ; NOTE 8E5
1040: B4       ; NOTE 4D5
1041: 99       ; NOTE 8G5
1042: 91       ; NOTE 8B4
1043: 8F       ; NOTE 8A4
1044: B4       ; NOTE 4D5
1045: 80       ; NOTE 8R
1046: 80       ; NOTE 8R
1047: 94       ; NOTE 8D5
1048: 94       ; NOTE 8D5
1049: 94       ; NOTE 8D5
104A: 94       ; NOTE 8D5
104B: 91       ; NOTE 8B4
104C: 8F       ; NOTE 8A4
104D: 8D       ; NOTE 8G4
104E: 80       ; NOTE 8R
104F: 99       ; NOTE 8G5
1050: 99       ; NOTE 8G5
1051: 99       ; NOTE 8G5
1052: 9B       ; NOTE 8A5
1053: 99       ; NOTE 8G5
1054: 98       ; NOTE 8F#5
1055: 96       ; NOTE 8E5
1056: 94       ; NOTE 8D5
1057: 91       ; NOTE 8B4
1058: 80       ; NOTE 8R
1059: 91       ; NOTE 8B4
105A: B9       ; NOTE 4G5
105B: B1       ; NOTE 4B4
105C: 94       ; NOTE 8D5
105D: CF       ; NOTE 2A4
105E: 80       ; NOTE 8R
105F: A0       ; NOTE 4R
1060: 80       ; NOTE 8R
1061: 91       ; NOTE 8B4
1062: 91       ; NOTE 8B4
1063: 92       ; NOTE 8C5
1064: 94       ; NOTE 8D5
```

# Bug: Missing eighth note

If you listen to the [original song](https://www.youtube.com/watch?v=2YMH5ntJEZ0)
you'll hear a few "stretched out" notes in the rhythem around the 30 seconds marks. 
The stretching appears in two adjacent phrases of the music at this point. But the 
music defined below has straight eighth notes. The second voice of the music (farther 
below) has a half note starting at beat one of the measure. The music just below is 
missing an eighth note duration, and the half note starts an eighth note later than it 
should. The second voice lags behind the first by an eighth note from that point on (but 
drops out because of the bug below).

I fixed this by extending one of the eighth notes to a quarter note, which matches
the timing of the very next phrase.

```code
;
; 1065: B6       ; >NOTE 4E5 change quater to half
1065: 96       ; NOTE 8E5
;
1066: 98       ; NOTE 8F#5
1067: D6       ; NOTE 2E5
1068: C0       ; NOTE 2R
1069: 80       ; NOTE 8R
106A: 92       ; NOTE 8C5
106B: 92       ; NOTE 8C5
106C: 94       ; NOTE 8D5
106D: B6       ; NOTE 4E5
106E: 98       ; NOTE 8F#5
106F: 99       ; NOTE 8G5
1070: D8       ; NOTE 2F#5
1071: A0       ; NOTE 4R
1072: B4       ; NOTE 4D5
1073: D9       ; NOTE 2G5
1074: 99       ; NOTE 8G5
1075: 98       ; NOTE 8F#5
1076: 96       ; NOTE 8E5
1077: 94       ; NOTE 8D5
1078: D8       ; NOTE 2F#5
1079: B6       ; NOTE 4E5
107A: B6       ; NOTE 4E5
107B: B4       ; NOTE 4D5
107C: BB       ; NOTE 4A5
107D: B9       ; NOTE 4G5
107E: B8       ; NOTE 4F#5
107F: D9       ; NOTE 2G5
1080: C0       ; NOTE 2R
1081: 99       ; NOTE 8G5
1082: 99       ; NOTE 8G5
1083: 99       ; NOTE 8G5
1084: 99       ; NOTE 8G5
1085: 99       ; NOTE 8G5
1086: 99       ; NOTE 8G5
1087: 98       ; NOTE 8F#5
1088: 96       ; NOTE 8E5
1089: D9       ; NOTE 2G5
108A: B4       ; NOTE 4D5
108B: 91       ; NOTE 8B4
108C: 91       ; NOTE 8B4
108D: AF       ; NOTE 4A4
108E: 8F       ; NOTE 8A4
108F: 8F       ; NOTE 8A4
1090: 99       ; NOTE 8G5
1091: 99       ; NOTE 8G5
1092: 98       ; NOTE 8F#5
1093: 96       ; NOTE 8E5
1094: D6       ; NOTE 2E5
1095: D4       ; NOTE 2D5
1096: 94       ; NOTE 8D5
1097: 91       ; NOTE 8B4
1098: 91       ; NOTE 8B4
1099: 91       ; NOTE 8B4
109A: B1       ; NOTE 4B4
109B: 8F       ; NOTE 8A4
109C: 8D       ; NOTE 8G4
109D: 92       ; NOTE 8C5
109E: 91       ; NOTE 8B4
109F: 92       ; NOTE 8C5
10A0: 94       ; NOTE 8D5
10A1: B6       ; NOTE 4E5
10A2: A0       ; NOTE 4R
10A3: 94       ; NOTE 8D5
10A4: 92       ; NOTE 8C5
10A5: 8F       ; NOTE 8A4
10A6: 8F       ; NOTE 8A4
10A7: AF       ; NOTE 4A4
10A8: 8D       ; NOTE 8G4
10A9: 8C       ; NOTE 8F#4
10AA: 8D       ; NOTE 8G4
10AB: 8C       ; NOTE 8F#4
10AC: 8D       ; NOTE 8G4
10AD: 8F       ; NOTE 8A4
10AE: D1       ; NOTE 2B4
10AF: 94       ; NOTE 8D5
10B0: 91       ; NOTE 8B4
10B1: 91       ; NOTE 8B4
10B2: 91       ; NOTE 8B4
10B3: B1       ; NOTE 4B4
10B4: 8F       ; NOTE 8A4
10B5: 8D       ; NOTE 8G4
10B6: 92       ; NOTE 8C5
10B7: 91       ; NOTE 8B4
10B8: 92       ; NOTE 8C5
10B9: 94       ; NOTE 8D5
10BA: B6       ; NOTE 4E5
10BB: 98       ; NOTE 8F#5
10BC: 96       ; NOTE 8E5
10BD: B4       ; NOTE 4D5
10BE: 94       ; NOTE 8D5
10BF: 96       ; NOTE 8E5
10C0: 94       ; NOTE 8D5
10C1: 92       ; NOTE 8C5
10C2: 91       ; NOTE 8B4
10C3: 8F       ; NOTE 8A4
10C4: CA       ; NOTE 2E4
10C5: AC       ; NOTE 4F#4
10C6: AF       ; NOTE 4A4
10C7: CD       ; NOTE 2G4
10C8: C0       ; NOTE 2R
10C9: FF       ; END OF VOICE
;
;S25B Main song
; Song=25 Voice=B
10CA: 1F 05    ; SC00:Use note set index 5 (note 1 = F#2)
10CC: 5F 05    ; SC02:Set volume to 05
10CE: D9       ; NOTE 2G4
10CF: D6       ; NOTE 2E4
10D0: D9       ; NOTE 2G4
10D1: D8       ; NOTE 2F#4
10D2: 8D       ; NOTE 8G3
10D3: 91       ; NOTE 8B3
10D4: 88       ; NOTE 8D3
10D5: 91       ; NOTE 8B3
10D6: 8D       ; NOTE 8G3
10D7: 91       ; NOTE 8B3
10D8: 88       ; NOTE 8D3
10D9: 91       ; NOTE 8B3
10DA: 8D       ; NOTE 8G3
10DB: 92       ; NOTE 8C4
10DC: 8A       ; NOTE 8E3
10DD: 92       ; NOTE 8C4
10DE: 8D       ; NOTE 8G3
10DF: 92       ; NOTE 8C4
10E0: 8A       ; NOTE 8E3
10E1: 92       ; NOTE 8C4
10E2: 8D       ; NOTE 8G3
10E3: 91       ; NOTE 8B3
10E4: 88       ; NOTE 8D3
10E5: 91       ; NOTE 8B3
10E6: 8D       ; NOTE 8G3
10E7: 91       ; NOTE 8B3
10E8: 88       ; NOTE 8D3
10E9: 91       ; NOTE 8B3
10EA: 8F       ; NOTE 8A3
10EB: 94       ; NOTE 8D4
10EC: 88       ; NOTE 8D3
10ED: 94       ; NOTE 8D4
10EE: 8A       ; NOTE 8E3
10EF: 94       ; NOTE 8D4
10F0: 8C       ; NOTE 8F#3
10F1: 94       ; NOTE 8D4
10F2: 8D       ; NOTE 8G3
10F3: 91       ; NOTE 8B3
10F4: 88       ; NOTE 8D3
10F5: 91       ; NOTE 8B3
10F6: 8D       ; NOTE 8G3
10F7: 91       ; NOTE 8B3
10F8: 88       ; NOTE 8D3
10F9: 91       ; NOTE 8B3
10FA: 8D       ; NOTE 8G3
10FB: 92       ; NOTE 8C4
10FC: 8A       ; NOTE 8E3
10FD: 92       ; NOTE 8C4
10FE: 8D       ; NOTE 8G3
10FF: 92       ; NOTE 8C4
1100: 8A       ; NOTE 8E3
1101: 92       ; NOTE 8C4
1102: 8D       ; NOTE 8G3
1103: 92       ; NOTE 8C4
1104: 8A       ; NOTE 8E3
1105: 92       ; NOTE 8C4
1106: 8D       ; NOTE 8G3
1107: 92       ; NOTE 8C4
1108: 8A       ; NOTE 8E3
1109: 92       ; NOTE 8C4
110A: 8F       ; NOTE 8A3
110B: 94       ; NOTE 8D4
110C: 88       ; NOTE 8D3
110D: 94       ; NOTE 8D4
110E: 8F       ; NOTE 8A3
110F: 94       ; NOTE 8D4
1110: 88       ; NOTE 8D3
1111: 94       ; NOTE 8D4
1112: 8D       ; NOTE 8G3
1113: 91       ; NOTE 8B3
1114: 88       ; NOTE 8D3
1115: 91       ; NOTE 8B3
1116: 8D       ; NOTE 8G3
1117: 91       ; NOTE 8B3
1118: 88       ; NOTE 8D3
1119: 91       ; NOTE 8B3
111A: 8D       ; NOTE 8G3
111B: 91       ; NOTE 8B3
111C: 89       ; NOTE 8D#3
111D: 91       ; NOTE 8B3
111E: 8A       ; NOTE 8E3
111F: 92       ; NOTE 8C4
1120: 8F       ; NOTE 8A3
1121: 92       ; NOTE 8C4
1122: 8F       ; NOTE 8A3
1123: 94       ; NOTE 8D4
1124: 88       ; NOTE 8D3
1125: 94       ; NOTE 8D4
1126: 8F       ; NOTE 8A3
1127: 94       ; NOTE 8D4
1128: 88       ; NOTE 8D3
1129: 94       ; NOTE 8D4
112A: 8D       ; NOTE 8G3
112B: 91       ; NOTE 8B3
112C: 88       ; NOTE 8D3
112D: 91       ; NOTE 8B3
112E: AD       ; NOTE 4G3
112F: A0       ; NOTE 4R
1130: D2       ; NOTE 2C4
1131: C0       ; NOTE 2R
1132: D1       ; NOTE 2B3
1133: C0       ; NOTE 2R
```

# Bug: Garbage note stops the voice

This is about midway through the second voice of the main song. There are plenty of
notes left, but the next note is mangled a bit. The note's duration is correct, but 
the note number is all 1s, which stops the voice from playing. I listened to the song 
on youtube and found the missing note should be an A. It seems a singe bit got flipped 
in the definition:

Original: 110_11111

Needed: 110_01111

I corrected this flipped bit, and you can hear the remainder of the second voice as
intended. Note in game play, the timer expires before you get to this point in the
music. You couldn't hear this part of the tune anyway. But now you can! Enjoy!

```code
; This note's duration is correct, but the note frequency is 1F, which stops the music. 
; I listened to the original song -- this should be an 3A for 2^6. One bit is flipped:
; Original: 110_11111
; Needed:   110_01111
; 1134: CF      ; >NOTE 2A3 ; This is the correct value
1134: DF       ; SC06:Volume off and end song
;
1135: C0       ; NOTE 2R
1136: D2       ; NOTE 2C4
1137: D2       ; NOTE 2C4
1138: 8D       ; NOTE 8G3
1139: 91       ; NOTE 8B3
113A: 88       ; NOTE 8D3
113B: 91       ; NOTE 8B3
113C: 8D       ; NOTE 8G3
113D: 91       ; NOTE 8B3
113E: 88       ; NOTE 8D3
113F: 91       ; NOTE 8B3
1140: 8D       ; NOTE 8G3
1141: 92       ; NOTE 8C4
1142: 8A       ; NOTE 8E3
1143: 92       ; NOTE 8C4
1144: 8D       ; NOTE 8G3
1145: 92       ; NOTE 8C4
1146: 8A       ; NOTE 8E3
1147: 92       ; NOTE 8C4
1148: 8F       ; NOTE 8A3
1149: 94       ; NOTE 8D4
114A: 88       ; NOTE 8D3
114B: 94       ; NOTE 8D4
114C: 8F       ; NOTE 8A3
114D: 94       ; NOTE 8D4
114E: 88       ; NOTE 8D3
114F: 94       ; NOTE 8D4
1150: 8D       ; NOTE 8G3
1151: 91       ; NOTE 8B3
1152: 88       ; NOTE 8D3
1153: 91       ; NOTE 8B3
1154: 8D       ; NOTE 8G3
1155: 91       ; NOTE 8B3
1156: 88       ; NOTE 8D3
1157: 91       ; NOTE 8B3
1158: 8D       ; NOTE 8G3
1159: 91       ; NOTE 8B3
115A: 88       ; NOTE 8D3
115B: 91       ; NOTE 8B3
115C: 8D       ; NOTE 8G3
115D: 91       ; NOTE 8B3
115E: 88       ; NOTE 8D3
115F: 91       ; NOTE 8B3
1160: 8D       ; NOTE 8G3
1161: 92       ; NOTE 8C4
1162: 8A       ; NOTE 8E3
1163: 92       ; NOTE 8C4
1164: 8D       ; NOTE 8G3
1165: 92       ; NOTE 8C4
1166: 8A       ; NOTE 8E3
1167: 92       ; NOTE 8C4
1168: 8F       ; NOTE 8A3
1169: 94       ; NOTE 8D4
116A: 88       ; NOTE 8D3
116B: 94       ; NOTE 8D4
116C: 8F       ; NOTE 8A3
116D: 94       ; NOTE 8D4
116E: 88       ; NOTE 8D3
116F: 94       ; NOTE 8D4
1170: D2       ; NOTE 2C4
1171: D4       ; NOTE 2D4
1172: 8D       ; NOTE 8G3
1173: FF       ; END OF VOICE
```

# Song: Frog Home 12

```code
;S16A Frog-home 12
; Song=16 Voice=A
1174: 1F 0B    ; SC00:Use note set index 11 (note 1 = F#3)
1176: 3F 0D    ; SC01:Set tempo index 13 (164 quarters/minute)
1178: 5F 06    ; SC02:Set volume to 06
117A: 8F       ; NOTE 8A4
117B: 60       ; NOTE 16R
117C: 6F       ; NOTE 16A4
117D: 8F       ; NOTE 8A4
117E: 60       ; NOTE 16R
117F: 6F       ; NOTE 16A4
1180: 91       ; NOTE 8B4
1181: 60       ; NOTE 16R
1182: 71       ; NOTE 16B4
1183: 93       ; NOTE 8C#5
1184: 60       ; NOTE 16R
1185: 73       ; NOTE 16C#5
1186: 74       ; NOTE 16D5
1187: 74       ; NOTE 16D5
1188: 74       ; NOTE 16D5
1189: 60       ; NOTE 16R
118A: 94       ; NOTE 8D5
118B: 60       ; NOTE 16R
118C: 76       ; NOTE 16E5
118D: D8       ; NOTE 2F#5
118E: B9       ; NOTE 4G5
118F: B9       ; NOTE 4G5
1190: 98       ; NOTE 8F#5
1191: 60       ; NOTE 16R
1192: B9       ; NOTE 4G5
1193: 60       ; NOTE 16R
1194: 8F       ; NOTE 8A4
1195: 60       ; NOTE 16R
1196: 6F       ; NOTE 16A4
1197: 91       ; NOTE 8B4
1198: 60       ; NOTE 16R
1199: D2       ; NOTE 2C5
119A: 60       ; NOTE 16R
119B: 94       ; NOTE 8D5
119C: 60       ; NOTE 16R
119D: 76       ; NOTE 16E5
119E: 94       ; NOTE 8D5
119F: 60       ; NOTE 16R
11A0: 72       ; NOTE 16C5
11A1: 91       ; NOTE 8B4
11A2: 60       ; NOTE 16R
11A3: 71       ; NOTE 16B4
11A4: 92       ; NOTE 8C5
11A5: 60       ; NOTE 16R
11A6: D4       ; NOTE 2D5
11A7: 60       ; NOTE 16R
11A8: A0       ; NOTE 4R
11A9: 74       ; NOTE 16D5
11AA: 76       ; NOTE 16E5
11AB: 78       ; NOTE 16F#5
11AC: 60       ; NOTE 16R
11AD: B9       ; NOTE 4G5
11AE: B9       ; NOTE 4G5
11AF: 98       ; NOTE 8F#5
11B0: 60       ; NOTE 16R
11B1: B9       ; NOTE 4G5
11B2: 60       ; NOTE 16R
11B3: 8F       ; NOTE 8A4
11B4: 60       ; NOTE 16R
11B5: 6F       ; NOTE 16A4
11B6: 91       ; NOTE 8B4
11B7: 60       ; NOTE 16R
11B8: 72       ; NOTE 16C5
11B9: 80       ; NOTE 8R
11BA: 60       ; NOTE 16R
11BB: 76       ; NOTE 16E5
11BC: 94       ; NOTE 8D5
11BD: 60       ; NOTE 16R
11BE: 73       ; NOTE 16C#5
11BF: 94       ; NOTE 8D5
11C0: 80       ; NOTE 8R
11C1: B2       ; NOTE 4C5
11C2: B1       ; NOTE 4B4
11C3: 8F       ; NOTE 8A4
11C4: 60       ; NOTE 16R
11C5: CD       ; NOTE 2G4
11C6: FF       ; END OF VOICE
;
;S16B Frog-home 12
; Song=16 Voice=B
11C7: 1F 05    ; SC00:Use note set index 5 (note 1 = F#2)
11C9: 5F 06    ; SC02:Set volume to 06
11CB: B9       ; NOTE 4G4
11CC: B9       ; NOTE 4G4
11CD: B9       ; NOTE 4G4
11CE: B9       ; NOTE 4G4
11CF: B8       ; NOTE 4F#4
11D0: B2       ; NOTE 4C4
11D1: B1       ; NOTE 4B3
11D2: AF       ; NOTE 4A3
11D3: AD       ; NOTE 4G3
11D4: B4       ; NOTE 4D4
11D5: B6       ; NOTE 4E4
11D6: B6       ; NOTE 4E4
11D7: B6       ; NOTE 4E4
11D8: B6       ; NOTE 4E4
11D9: B6       ; NOTE 4E4
11DA: B6       ; NOTE 4E4
11DB: B8       ; NOTE 4F#4
11DC: B8       ; NOTE 4F#4
11DD: B8       ; NOTE 4F#4
11DE: B8       ; NOTE 4F#4
11DF: B4       ; NOTE 4D4
11E0: B1       ; NOTE 4B3
11E1: BD       ; NOTE 4B4
11E2: B4       ; NOTE 4D4
11E3: B4       ; NOTE 4D4
11E4: B4       ; NOTE 4D4
11E5: B6       ; NOTE 4E4
11E6: B6       ; NOTE 4E4
11E7: B6       ; NOTE 4E4
11E8: B6       ; NOTE 4E4
11E9: B6       ; NOTE 4E4
11EA: B6       ; NOTE 4E4
11EB: 98       ; NOTE 8F#4
11EC: 80       ; NOTE 8R
11ED: A0       ; NOTE 4R
11EE: B6       ; NOTE 4E4
11EF: B4       ; NOTE 4D4
11F0: FF       ; END OF VOICE
```

# Song: Frog Home 13

```code
;S17A Frog-home 13
; Song=17 Voice=A
11F1: 1F 0B    ; SC00:Use note set index 11 (note 1 = F#3)
11F3: 3F 0D    ; SC01:Set tempo index 13 (164 quarters/minute)
11F5: 5F 06    ; SC02:Set volume to 06
11F7: 92       ; NOTE 8C5
11F8: 97       ; NOTE 8F5
11F9: 97       ; NOTE 8F5
11FA: 99       ; NOTE 8G5
11FB: 9B       ; NOTE 8A5
11FC: 97       ; NOTE 8F5
11FD: 9B       ; NOTE 8A5
11FE: 99       ; NOTE 8G5
11FF: 92       ; NOTE 8C5
1200: 97       ; NOTE 8F5
1201: 97       ; NOTE 8F5
1202: 99       ; NOTE 8G5
1203: 9B       ; NOTE 8A5
1204: B7       ; NOTE 4F5
1205: 96       ; NOTE 8E5
1206: 92       ; NOTE 8C5
1207: 97       ; NOTE 8F5
1208: 97       ; NOTE 8F5
1209: 99       ; NOTE 8G5
120A: 9B       ; NOTE 8A5
120B: 9C       ; NOTE 8A#5
120C: 9B       ; NOTE 8A5
120D: 99       ; NOTE 8G5
120E: 97       ; NOTE 8F5
120F: 96       ; NOTE 8E5
1210: 92       ; NOTE 8C5
1211: 94       ; NOTE 8D5
1212: 96       ; NOTE 8E5
1213: B7       ; NOTE 4F5
1214: 97       ; NOTE 8F5
1215: 80       ; NOTE 8R
1216: FF       ; END OF VOICE
;
;S17B Frog-home 13
; Song=17 Voice=B
1217: FF       ; END OF VOICE
```

# Song: Frog Home 14

```code
;S18A Frog-home 14
; Song=18 Voice=A
1218: 1F 0B    ; SC00:Use note set index 11 (note 1 = F#3)
121A: 3F 0D    ; SC01:Set tempo index 13 (164 quarters/minute)
121C: 5F 06    ; SC02:Set volume to 06
121E: 94       ; NOTE 8D5
121F: 60       ; NOTE 16R
1220: 76       ; NOTE 16E5
1221: 94       ; NOTE 8D5
1222: 92       ; NOTE 8C5
1223: 94       ; NOTE 8D5
1224: 96       ; NOTE 8E5
1225: B7       ; NOTE 4F5
1226: 92       ; NOTE 8C5
1227: 60       ; NOTE 16R
1228: 74       ; NOTE 16D5
1229: 92       ; NOTE 8C5
122A: 90       ; NOTE 8A#4
122B: 8F       ; NOTE 8A4
122C: 90       ; NOTE 8A#4
122D: 92       ; NOTE 8C5
122E: 80       ; NOTE 8R
122F: 94       ; NOTE 8D5
1230: 60       ; NOTE 16R
1231: 76       ; NOTE 16E5
1232: 94       ; NOTE 8D5
1233: 92       ; NOTE 8C5
1234: 94       ; NOTE 8D5
1235: 96       ; NOTE 8E5
1236: 97       ; NOTE 8F5
1237: 94       ; NOTE 8D5
1238: 94       ; NOTE 8D5
1239: 97       ; NOTE 8F5
123A: 96       ; NOTE 8E5
123B: 99       ; NOTE 8G5
123C: B7       ; NOTE 4F5
123D: 97       ; NOTE 8F5
123E: 80       ; NOTE 8R
123F: FF       ; END OF VOICE
;
;S18B Frog-home 14
; Song=18 Voice=B
1240: 1F 0B    ; SC00:Use note set index 11 (note 1 = F#3)
1242: 5F 06    ; SC02:Set volume to 06
1244: 90       ; NOTE 8A#4
1245: 60       ; NOTE 16R
1246: 70       ; NOTE 16A#4
1247: 90       ; NOTE 8A#4
1248: 92       ; NOTE 8C5
1249: 90       ; NOTE 8A#4
124A: 90       ; NOTE 8A#4
124B: B0       ; NOTE 4A#4
124C: 8F       ; NOTE 8A4
124D: 60       ; NOTE 16R
124E: 70       ; NOTE 16A#4
124F: 8F       ; NOTE 8A4
1250: 8D       ; NOTE 8G4
1251: 8B       ; NOTE 8F4
1252: 8B       ; NOTE 8F4
1253: 8B       ; NOTE 8F4
1254: 80       ; NOTE 8R
1255: 90       ; NOTE 8A#4
1256: 60       ; NOTE 16R
1257: 70       ; NOTE 16A#4
1258: 90       ; NOTE 8A#4
1259: 92       ; NOTE 8C5
125A: 90       ; NOTE 8A#4
125B: 90       ; NOTE 8A#4
125C: 90       ; NOTE 8A#4
125D: 90       ; NOTE 8A#4
125E: 8F       ; NOTE 8A4
125F: 92       ; NOTE 8C5
1260: 92       ; NOTE 8C5
1261: 90       ; NOTE 8A#4
1262: AF       ; NOTE 4A4
1263: 8F       ; NOTE 8A4
1264: 80       ; NOTE 8R
1265: FF       ; END OF VOICE
```

# Song: Frog Home 15

```code
;S19A Frog-home 15
; Song=19 Voice=A
1266: 1F 0B    ; SC00:Use note set index 11 (note 1 = F#3)
1268: 3F 0D    ; SC01:Set tempo index 13 (164 quarters/minute)
126A: 5F 06    ; SC02:Set volume to 06
126C: 72       ; NOTE 16C5
126D: 74       ; NOTE 16D5
126E: B6       ; NOTE 4E5
126F: 96       ; NOTE 8E5
1270: B6       ; NOTE 4E5
1271: 96       ; NOTE 8E5
1272: B7       ; NOTE 4F5
1273: 96       ; NOTE 8E5
1274: B6       ; NOTE 4E5
1275: 7B       ; NOTE 16A5
1276: 7B       ; NOTE 16A5
1277: B9       ; NOTE 4G5
1278: 96       ; NOTE 8E5
1279: 96       ; NOTE 8E5
127A: 94       ; NOTE 8D5
127B: 92       ; NOTE 8C5
127C: B4       ; NOTE 4D5
127D: 94       ; NOTE 8D5
127E: B4       ; NOTE 4D5
127F: 80       ; NOTE 8R
1280: B6       ; NOTE 4E5
1281: 96       ; NOTE 8E5
1282: B6       ; NOTE 4E5
1283: 96       ; NOTE 8E5
1284: B7       ; NOTE 4F5
1285: 96       ; NOTE 8E5
1286: B6       ; NOTE 4E5
1287: 9B       ; NOTE 8A5
1288: B9       ; NOTE 4G5
1289: 96       ; NOTE 8E5
128A: 94       ; NOTE 8D5
128B: 96       ; NOTE 8E5
128C: 94       ; NOTE 8D5
128D: B2       ; NOTE 4C5
128E: 92       ; NOTE 8C5
128F: B2       ; NOTE 4C5
1290: 80       ; NOTE 8R
1291: FF       ; END OF VOICE
;
;S19B Frog-home 15
; Song=19 Voice=B
1292: 1F 0B    ; SC00:Use note set index 11 (note 1 = F#3)
1294: 5F 06    ; SC02:Set volume to 06
1296: 72       ; NOTE 16C5
1297: 74       ; NOTE 16D5
1298: B6       ; NOTE 4E5
1299: 8D       ; NOTE 8G4
129A: 8D       ; NOTE 8G4
129B: 8F       ; NOTE 8A4
129C: 8D       ; NOTE 8G4
129D: AF       ; NOTE 4A4
129E: 92       ; NOTE 8C5
129F: B2       ; NOTE 4C5
12A0: 80       ; NOTE 8R
12A1: AD       ; NOTE 4G4
12A2: 8D       ; NOTE 8G4
12A3: 8F       ; NOTE 8A4
12A4: 91       ; NOTE 8B4
12A5: 92       ; NOTE 8C5
12A6: B2       ; NOTE 4C5
12A7: 91       ; NOTE 8B4
12A8: B1       ; NOTE 4B4
12A9: 72       ; NOTE 16C5
12AA: 74       ; NOTE 16D5
12AB: B6       ; NOTE 4E5
12AC: 8D       ; NOTE 8G4
12AD: 8D       ; NOTE 8G4
12AE: 8F       ; NOTE 8A4
12AF: 8D       ; NOTE 8G4
12B0: AF       ; NOTE 4A4
12B1: 92       ; NOTE 8C5
12B2: B2       ; NOTE 4C5
12B3: 97       ; NOTE 8F5
12B4: B6       ; NOTE 4E5
12B5: 92       ; NOTE 8C5
12B6: 91       ; NOTE 8B4
12B7: 92       ; NOTE 8C5
12B8: 9D       ; NOTE 8B5
12B9: AA       ; NOTE 4E4
12BA: 8A       ; NOTE 8E4
12BB: AA       ; NOTE 4E4
12BC: 80       ; NOTE 8R
12BD: FF       ; END OF VOICE
```

# Song: Frog Home 16

```code
;S20A Frog-home 16
; Song=20 Voice=A
12BE: 1F 0B    ; SC00:Use note set index 11 (note 1 = F#3)
12C0: 3F 0D    ; SC01:Set tempo index 13 (164 quarters/minute)
12C2: 5F 06    ; SC02:Set volume to 06
12C4: 8A       ; NOTE 8E4
12C5: AF       ; NOTE 4A4
12C6: 8E       ; NOTE 8G#4
12C7: 8C       ; NOTE 8F#4
12C8: AA       ; NOTE 4E4
12C9: 80       ; NOTE 8R
12CA: 8A       ; NOTE 8E4
12CB: AC       ; NOTE 4F#4
12CC: AE       ; NOTE 4G#4
12CD: AF       ; NOTE 4A4
12CE: 8A       ; NOTE 8E4
12CF: 8A       ; NOTE 8E4
12D0: 8C       ; NOTE 8F#4
12D1: 8A       ; NOTE 8E4
12D2: 88       ; NOTE 8D4
12D3: 87       ; NOTE 8C#4
12D4: 8C       ; NOTE 8F#4
12D5: 8A       ; NOTE 8E4
12D6: 88       ; NOTE 8D4
12D7: 87       ; NOTE 8C#4
12D8: A5       ; NOTE 4B3
12D9: AA       ; NOTE 4E4
12DA: AA       ; NOTE 4E4
12DB: 80       ; NOTE 8R
12DC: FF       ; END OF VOICE
;
;S20B Frog-home 16
; Song=20 Voice=B
12DD: 1F 0B    ; SC00:Use note set index 11 (note 1 = F#3)
12DF: 5F 06    ; SC02:Set volume to 06
12E1: 8A       ; NOTE 8E4
12E2: AF       ; NOTE 4A4
12E3: 8E       ; NOTE 8G#4
12E4: 8C       ; NOTE 8F#4
12E5: AA       ; NOTE 4E4
12E6: 80       ; NOTE 8R
12E7: 8A       ; NOTE 8E4
12E8: A9       ; NOTE 4D#4
12E9: A8       ; NOTE 4D4
12EA: A7       ; NOTE 4C#4
12EB: 87       ; NOTE 8C#4
12EC: 83       ; NOTE 8A3
12ED: 88       ; NOTE 8D4
12EE: 87       ; NOTE 8C#4
12EF: 85       ; NOTE 8B3
12F0: 83       ; NOTE 8A3
12F1: A3       ; NOTE 4A3
12F2: A5       ; NOTE 4B3
12F3: A1       ; NOTE 4G3
12F4: 80       ; NOTE 8R
12F5: FF       ; END OF VOICE
```

# Song: Frog Home 17

```code
;S21A Frog-home 17
; Song=21 Voice=A
12F6: 1F 0B    ; SC00:Use note set index 11 (note 1 = F#3)
12F8: 3F 0D    ; SC01:Set tempo index 13 (164 quarters/minute)
12FA: 5F 06    ; SC02:Set volume to 06
12FC: 8A       ; NOTE 8E4
12FD: 87       ; NOTE 8C#4
12FE: 8A       ; NOTE 8E4
12FF: 8A       ; NOTE 8E4
1300: 8A       ; NOTE 8E4
1301: 8C       ; NOTE 8F#4
1302: 8A       ; NOTE 8E4
1303: 8A       ; NOTE 8E4
1304: 8A       ; NOTE 8E4
1305: 87       ; NOTE 8C#4
1306: 8A       ; NOTE 8E4
1307: 8A       ; NOTE 8E4
1308: 8A       ; NOTE 8E4
1309: 8C       ; NOTE 8F#4
130A: 8A       ; NOTE 8E4
130B: 8A       ; NOTE 8E4
130C: 8A       ; NOTE 8E4
130D: AF       ; NOTE 4A4
130E: B1       ; NOTE 4B4
130F: 93       ; NOTE 8C#5
1310: 60       ; NOTE 16R
1311: 6F       ; NOTE 16A4
1312: 8F       ; NOTE 8A4
1313: 8F       ; NOTE 8A4
1314: B1       ; NOTE 4B4
1315: AE       ; NOTE 4G#4
1316: AF       ; NOTE 4A4
1317: 80       ; NOTE 8R
1318: FF       ; END OF VOICE
;
;S21B Frog-home 17
; Song=21 Voice=B
1319: 1F 0B    ; SC00:Use note set index 11 (note 1 = F#3)
131B: 5F 06    ; SC02:Set volume to 06
131D: 87       ; NOTE 8C#4
131E: 83       ; NOTE 8A3
131F: 87       ; NOTE 8C#4
1320: 87       ; NOTE 8C#4
1321: 87       ; NOTE 8C#4
1322: 86       ; NOTE 8C4
1323: 87       ; NOTE 8C#4
1324: 87       ; NOTE 8C#4
1325: 87       ; NOTE 8C#4
1326: 83       ; NOTE 8A3
1327: 87       ; NOTE 8C#4
1328: 87       ; NOTE 8C#4
1329: 87       ; NOTE 8C#4
132A: 87       ; NOTE 8C#4
132B: 85       ; NOTE 8B3
132C: 87       ; NOTE 8C#4
132D: 88       ; NOTE 8D4
132E: AA       ; NOTE 4E4
132F: AA       ; NOTE 4E4
1330: 8A       ; NOTE 8E4
1331: 60       ; NOTE 16R
1332: 67       ; NOTE 16C#4
1333: 87       ; NOTE 8C#4
1334: 8A       ; NOTE 8E4
1335: A8       ; NOTE 4D4
1336: A8       ; NOTE 4D4
1337: A7       ; NOTE 4C#4
1338: 80       ; NOTE 8R
1339: FF       ; END OF VOICE
```

# Song: Frog Home 18

```code
;S22A Frog-home 18
; Song=22 Voice=A
133A: 1F 0B    ; SC00:Use note set index 11 (note 1 = F#3)
133C: 3F 0D    ; SC01:Set tempo index 13 (164 quarters/minute)
133E: 5F 06    ; SC02:Set volume to 06
1340: 8F       ; NOTE 8A4
1341: 93       ; NOTE 8C#5
1342: B6       ; NOTE 4E5
1343: B6       ; NOTE 4E5
1344: BB       ; NOTE 4A5
1345: 9A       ; NOTE 8G#5
1346: 98       ; NOTE 8F#5
1347: 96       ; NOTE 8E5
1348: 96       ; NOTE 8E5
1349: 93       ; NOTE 8C#5
134A: 94       ; NOTE 8D5
134B: 96       ; NOTE 8E5
134C: 80       ; NOTE 8R
134D: BA       ; NOTE 4G#5
134E: 98       ; NOTE 8F#5
134F: 98       ; NOTE 8F#5
1350: 94       ; NOTE 8D5
1351: 98       ; NOTE 8F#5
1352: 96       ; NOTE 8E5
1353: 96       ; NOTE 8E5
1354: 9B       ; NOTE 8A5
1355: 9B       ; NOTE 8A5
1356: 9A       ; NOTE 8G#5
1357: 98       ; NOTE 8F#5
1358: 96       ; NOTE 8E5
1359: 9A       ; NOTE 8G#5
135A: 9B       ; NOTE 8A5
135B: 80       ; NOTE 8R
135C: 8F       ; NOTE 8A4
135D: 93       ; NOTE 8C#5
135E: B6       ; NOTE 4E5
135F: B6       ; NOTE 4E5
1360: BB       ; NOTE 4A5
1361: 9A       ; NOTE 8G#5
1362: 98       ; NOTE 8F#5
1363: 96       ; NOTE 8E5
1364: 96       ; NOTE 8E5
1365: 93       ; NOTE 8C#5
1366: 94       ; NOTE 8D5
1367: 96       ; NOTE 8E5
1368: 80       ; NOTE 8R
1369: BA       ; NOTE 4G#5
136A: 98       ; NOTE 8F#5
136B: 98       ; NOTE 8F#5
136C: 94       ; NOTE 8D5
136D: 98       ; NOTE 8F#5
136E: 96       ; NOTE 8E5
136F: 96       ; NOTE 8E5
1370: 9B       ; NOTE 8A5
1371: 9B       ; NOTE 8A5
1372: 9A       ; NOTE 8G#5
1373: 98       ; NOTE 8F#5
1374: 96       ; NOTE 8E5
1375: 9A       ; NOTE 8G#5
1376: 9B       ; NOTE 8A5
1377: 80       ; NOTE 8R
1378: A0       ; NOTE 4R
1379: FF       ; END OF VOICE
;
;S22B Frog-home 18
; Song=22 Voice=B
137A: 1F 0B    ; SC00:Use note set index 11 (note 1 = F#3)
137C: 5F 06    ; SC02:Set volume to 06
137E: 8F       ; NOTE 8A4
137F: 8F       ; NOTE 8A4
1380: B3       ; NOTE 4C#5
1381: B3       ; NOTE 4C#5
1382: B8       ; NOTE 4F#5
1383: 96       ; NOTE 8E5
1384: 94       ; NOTE 8D5
1385: 93       ; NOTE 8C#5
1386: 93       ; NOTE 8C#5
1387: 8F       ; NOTE 8A4
1388: 91       ; NOTE 8B4
1389: 93       ; NOTE 8C#5
138A: 80       ; NOTE 8R
138B: B6       ; NOTE 4E5
138C: 94       ; NOTE 8D5
138D: 94       ; NOTE 8D5
138E: 8F       ; NOTE 8A4
138F: 94       ; NOTE 8D5
1390: 93       ; NOTE 8C#5
1391: 93       ; NOTE 8C#5
1392: 93       ; NOTE 8C#5
1393: 93       ; NOTE 8C#5
1394: 96       ; NOTE 8E5
1395: 93       ; NOTE 8C#5
1396: 8F       ; NOTE 8A4
1397: 91       ; NOTE 8B4
1398: 93       ; NOTE 8C#5
1399: 80       ; NOTE 8R
139A: 8F       ; NOTE 8A4
139B: 8F       ; NOTE 8A4
139C: B3       ; NOTE 4C#5
139D: B3       ; NOTE 4C#5
139E: B8       ; NOTE 4F#5
139F: 96       ; NOTE 8E5
13A0: 94       ; NOTE 8D5
13A1: 93       ; NOTE 8C#5
13A2: 93       ; NOTE 8C#5
13A3: 8F       ; NOTE 8A4
13A4: 91       ; NOTE 8B4
13A5: 93       ; NOTE 8C#5
13A6: 80       ; NOTE 8R
13A7: B6       ; NOTE 4E5
13A8: 94       ; NOTE 8D5
13A9: 94       ; NOTE 8D5
13AA: 8F       ; NOTE 8A4
13AB: 94       ; NOTE 8D5
13AC: 93       ; NOTE 8C#5
13AD: 93       ; NOTE 8C#5
13AE: 93       ; NOTE 8C#5
13AF: 93       ; NOTE 8C#5
13B0: 96       ; NOTE 8E5
13B1: 93       ; NOTE 8C#5
13B2: 8F       ; NOTE 8A4
13B3: 91       ; NOTE 8B4
13B4: 93       ; NOTE 8C#5
13B5: 80       ; NOTE 8R
13B6: A0       ; NOTE 4R
13B7: FF       ; END OF VOICE
```

# Song: Frog Home 19

```code
;S23A Frog-home 19
; Song=23 Voice=A
13B8: 1F 0B    ; SC00:Use note set index 11 (note 1 = F#3)
13BA: 3F 0D    ; SC01:Set tempo index 13 (164 quarters/minute)
13BC: 5F 06    ; SC02:Set volume to 06
13BE: 8D       ; NOTE 8G4
13BF: 92       ; NOTE 8C5
13C0: 96       ; NOTE 8E5
13C1: B9       ; NOTE 4G5
13C2: 99       ; NOTE 8G5
13C3: 96       ; NOTE 8E5
13C4: B7       ; NOTE 4F5
13C5: 97       ; NOTE 8F5
13C6: 94       ; NOTE 8D5
13C7: B6       ; NOTE 4E5
13C8: B9       ; NOTE 4G5
13C9: 80       ; NOTE 8R
13CA: 96       ; NOTE 8E5
13CB: 97       ; NOTE 8F5
13CC: 99       ; NOTE 8G5
13CD: BB       ; NOTE 4A5
13CE: 9B       ; NOTE 8A5
13CF: 9B       ; NOTE 8A5
13D0: 9B       ; NOTE 8A5
13D1: 99       ; NOTE 8G5
13D2: 9B       ; NOTE 8A5
13D3: 9C       ; NOTE 8A#5
13D4: DD       ; NOTE 2B5
13D5: A0       ; NOTE 4R
13D6: 9D       ; NOTE 8B5
13D7: 9D       ; NOTE 8B5
13D8: BD       ; NOTE 4B5
13D9: 9B       ; NOTE 8A5
13DA: 99       ; NOTE 8G5
13DB: BB       ; NOTE 4A5
13DC: 99       ; NOTE 8G5
13DD: 97       ; NOTE 8F5
13DE: 9B       ; NOTE 8A5
13DF: 80       ; NOTE 8R
13E0: B9       ; NOTE 4G5
13E1: A0       ; NOTE 4R
13E2: 96       ; NOTE 8E5
13E3: 97       ; NOTE 8F5
13E4: B9       ; NOTE 4G5
13E5: 98       ; NOTE 8F#5
13E6: 99       ; NOTE 8G5
13E7: BB       ; NOTE 4A5
13E8: 99       ; NOTE 8G5
13E9: 97       ; NOTE 8F5
13EA: D6       ; NOTE 2E5
13EB: FF       ; END OF VOICE
;
;S23B Frog-home 19
; Song=23 Voice=B
13EC: 1F 0B    ; SC00:Use note set index 11 (note 1 = F#3)
13EE: 5F 06    ; SC02:Set volume to 06
13F0: 8D       ; NOTE 8G4
13F1: 92       ; NOTE 8C5
13F2: 96       ; NOTE 8E5
13F3: B6       ; NOTE 4E5
13F4: 96       ; NOTE 8E5
13F5: 92       ; NOTE 8C5
13F6: B4       ; NOTE 4D5
13F7: 94       ; NOTE 8D5
13F8: 91       ; NOTE 8B4
13F9: B2       ; NOTE 4C5
13FA: B6       ; NOTE 4E5
13FB: 80       ; NOTE 8R
13FC: 92       ; NOTE 8C5
13FD: 94       ; NOTE 8D5
13FE: 96       ; NOTE 8E5
13FF: B7       ; NOTE 4F5
1400: 97       ; NOTE 8F5
1401: 97       ; NOTE 8F5
1402: 97       ; NOTE 8F5
1403: 96       ; NOTE 8E5
1404: 97       ; NOTE 8F5
1405: 98       ; NOTE 8F#5
1406: D9       ; NOTE 2G5
1407: A0       ; NOTE 4R
1408: 99       ; NOTE 8G5
1409: 99       ; NOTE 8G5
140A: B9       ; NOTE 4G5
140B: 97       ; NOTE 8F5
140C: 96       ; NOTE 8E5
140D: B7       ; NOTE 4F5
140E: 96       ; NOTE 8E5
140F: 94       ; NOTE 8D5
1410: 97       ; NOTE 8F5
1411: 80       ; NOTE 8R
1412: B6       ; NOTE 4E5
1413: A0       ; NOTE 4R
1414: 92       ; NOTE 8C5
1415: 94       ; NOTE 8D5
1416: B6       ; NOTE 4E5
1417: 95       ; NOTE 8D#5
1418: 96       ; NOTE 8E5
1419: B7       ; NOTE 4F5
141A: 96       ; NOTE 8E5
141B: 94       ; NOTE 8D5
141C: D2       ; NOTE 2C5
141D: FF       ; END OF VOICE
```

# Song: Frog Home 20

```code
;S24A Frog-home 20
; Song=24 Voice=A
141E: 1F 0B    ; SC00:Use note set index 11 (note 1 = F#3)
1420: 3F 0D    ; SC01:Set tempo index 13 (164 quarters/minute)
1422: 5F 06    ; SC02:Set volume to 06
1424: 8C       ; NOTE 8F#4
1425: B1       ; NOTE 4B4
1426: 91       ; NOTE 8B4
1427: 94       ; NOTE 8D5
1428: B8       ; NOTE 4F#5
1429: 80       ; NOTE 8R
142A: 8C       ; NOTE 8F#4
142B: 90       ; NOTE 8A#4
142C: 90       ; NOTE 8A#4
142D: 90       ; NOTE 8A#4
142E: 93       ; NOTE 8C#5
142F: B6       ; NOTE 4E5
1430: A0       ; NOTE 4R
1431: B6       ; NOTE 4E5
1432: 98       ; NOTE 8F#5
1433: 96       ; NOTE 8E5
1434: 94       ; NOTE 8D5
1435: 94       ; NOTE 8D5
1436: 93       ; NOTE 8C#5
1437: 91       ; NOTE 8B4
1438: 93       ; NOTE 8C#5
1439: 93       ; NOTE 8C#5
143A: 94       ; NOTE 8D5
143B: 96       ; NOTE 8E5
143C: B8       ; NOTE 4F#5
143D: A0       ; NOTE 4R
143E: 96       ; NOTE 8E5
143F: 76       ; NOTE 16E5
1440: 74       ; NOTE 16D5
1441: 96       ; NOTE 8E5
1442: 76       ; NOTE 16E5
1443: 74       ; NOTE 16D5
1444: AC       ; NOTE 4F#4
1445: B0       ; NOTE 4A#4
1446: D1       ; NOTE 2B4
1447: FF       ; END OF VOICE
;
;S24B Frog-home 20
; Song=24 Voice=B
1448: 1F 05    ; SC00:Use note set index 5 (note 1 = F#2)
144A: 5F 06    ; SC02:Set volume to 06
144C: 80       ; NOTE 8R
144D: B1       ; NOTE 4B3
144E: B1       ; NOTE 4B3
144F: B1       ; NOTE 4B3
1450: B1       ; NOTE 4B3
1451: AC       ; NOTE 4F#3
1452: AC       ; NOTE 4F#3
1453: AC       ; NOTE 4F#3
1454: AC       ; NOTE 4F#3
1455: AA       ; NOTE 4E3
1456: AA       ; NOTE 4E3
1457: AA       ; NOTE 4E3
1458: AA       ; NOTE 4E3
1459: AC       ; NOTE 4F#3
145A: AC       ; NOTE 4F#3
145B: AC       ; NOTE 4F#3
145C: AC       ; NOTE 4F#3
145D: 8A       ; NOTE 8E3
145E: 80       ; NOTE 8R
145F: 8A       ; NOTE 8E3
1460: 80       ; NOTE 8R
1461: AC       ; NOTE 4F#3
1462: AC       ; NOTE 4F#3
1463: B1       ; NOTE 4B3
1464: FF       ; END OF VOICE
```

## Time Running Out Sound

[runningOutOfTime.mp3](sounds/runningOutOfTime.mp3)

```code
;I05 Time running out
1465: E7              RST     $20                 
1466: 3E 01           LD      A,$01               
1468: 32 C8 42        LD      ($42C8),A           ; {ram.m42C8}
146B: 32 C3 42        LD      ($42C3),A           ; {ram.m42C3}
146E: F7              RST     $30                 
146F: C3 70 16        JP      $1670               ; {} Continue
;
;C05 Time running out
1472: DD 21 B0 42     LD      IX,$42B0            
1476: DD 7E 00        LD      A,(IX+$00)          
1479: FE FF           CP      $FF                 
147B: 28 25           JR      Z,$14A2             ; {}
147D: CD A9 14        CALL    $14A9               ; {}
1480: AF              XOR     A                   
1481: C9              RET                         
```

## Frog Hopping Sound

[hop.mp3](sounds/hop.mp3)

```code
;I04 Frog hopping
1482: E7              RST     $20                 
1483: 3E 00           LD      A,$00               
1485: 32 C3 42        LD      ($42C3),A           ; {ram.m42C3}
1488: F7              RST     $30                 
1489: C3 6B 16        JP      $166B               ; {}
;
;C04 Frog hopping
148C: 3A C8 42        LD      A,($42C8)           ; {ram.m42C8}
148F: A7              AND     A                   
1490: 20 14           JR      NZ,$14A6            ; {}
1492: E7              RST     $20                 
1493: DD 21 B0 42     LD      IX,$42B0            
1497: DD 7E 00        LD      A,(IX+$00)          
149A: FE FF           CP      $FF                 
149C: C8              RET     Z                   
149D: CD A9 14        CALL    $14A9               ; {}
14A0: AF              XOR     A                   
14A1: C9              RET                         
14A2: AF              XOR     A                   
14A3: 32 C8 42        LD      ($42C8),A           ; {ram.m42C8}
14A6: 3E FF           LD      A,$FF               
14A8: C9              RET                         
14A9: DD 35 01        DEC     (IX+$01)            
14AC: C0              RET     NZ                  
14AD: 3A C2 42        LD      A,($42C2)           ; {ram.m42C2}
14B0: DD 77 01        LD      (IX+$01),A          
14B3: DD 7E 08        LD      A,(IX+$08)          
14B6: A7              AND     A                   
14B7: 28 16           JR      Z,$14CF             ; {}
14B9: 21 C4 42        LD      HL,$42C4            
14BC: 35              DEC     (HL)                
14BD: 7E              LD      A,(HL)              
14BE: A7              AND     A                   
14BF: 28 0B           JR      Z,$14CC             ; {}
14C1: CD 4D 02        CALL    $024D               ; {code.ReadTune}
14C4: ED 5B C5 42     LD      DE,($42C5)          ; {ram.m42C5}
14C8: 19              ADD     HL,DE               
14C9: EF              RST     $28                 
14CA: 18 03           JR      $14CF               ; {}
14CC: DD 77 08        LD      (IX+$08),A          
14CF: DD CB 00 46     BIT     0,(IX+$00)          
14D3: C2 E3 14        JP      NZ,$14E3            ; {}
14D6: DD 7E 07        LD      A,(IX+$07)          
14D9: D6 01           SUB     $01                 
14DB: FA E3 14        JP      M,$14E3             ; {}
14DE: DD 77 07        LD      (IX+$07),A          
14E1: 47              LD      B,A                 
14E2: DF              RST     $18                 
14E3: DD 35 00        DEC     (IX+$00)            
14E6: C0              RET     NZ                  
14E7: DD 6E 02        LD      L,(IX+$02)          
14EA: DD 66 03        LD      H,(IX+$03)          
14ED: 7E              LD      A,(HL)              
14EE: 47              LD      B,A                 
14EF: E6 1F           AND     $1F                 
14F1: CA 94 15        JP      Z,$1594             ; {}
14F4: FE 1F           CP      $1F                 
14F6: C2 AE 15        JP      NZ,$15AE            ; {}
14F9: 23              INC     HL                  
14FA: DD 75 02        LD      (IX+$02),L          
14FD: DD 74 03        LD      (IX+$03),H          
1500: 78              LD      A,B                 
1501: E6 E0           AND     $E0                 
1503: 0F              RRCA                        
1504: 0F              RRCA                        
1505: 0F              RRCA                        
1506: 0F              RRCA                        
1507: 4F              LD      C,A                 
1508: 06 00           LD      B,$00               
150A: 21 16 15        LD      HL,$1516            
150D: 09              ADD     HL,BC               
150E: 5E              LD      E,(HL)              
150F: 23              INC     HL                  
1510: 56              LD      D,(HL)              
1511: 2A B2 42        LD      HL,($42B2)          ; {ram.m42B2}
1514: D5              PUSH    DE                  
1515: C9              RET                         
;
1516: 26 15           LD      H,$15               
1518: 39              ADD     HL,SP               
1519: 15              DEC     D                   
151A: 49              LD      C,C                 
151B: 15              DEC     D                   
151C: 52              LD      D,D                 
151D: 15              DEC     D                   
151E: 8C              ADC     A,H                 
151F: 15              DEC     D                   
1520: 8C              ADC     A,H                 
1521: 15              DEC     D                   
1522: 8C              ADC     A,H                 
1523: 15              DEC     D                   
1524: 8C              ADC     A,H                 
1525: 15              DEC     D                   
1526: 4E              LD      C,(HL)              
1527: CB 21           SLA     C                   
1529: CB 21           SLA     C                   
152B: 06 00           LD      B,$00               
152D: 21 E3 15        LD      HL,$15E3            
1530: 09              ADD     HL,BC               
1531: DD 75 04        LD      (IX+$04),L          
1534: DD 74 05        LD      (IX+$05),H          
1537: 18 43           JR      $157C               ; {}
1539: 4E              LD      C,(HL)              
153A: 06 00           LD      B,$00               
153C: 21 5B 16        LD      HL,$165B            
153F: 09              ADD     HL,BC               
1540: 7E              LD      A,(HL)              
1541: 32 C2 42        LD      ($42C2),A           ; {ram.m42C2}
1544: DD 77 01        LD      (IX+$01),A          
1547: 18 33           JR      $157C               ; {}
1549: 7E              LD      A,(HL)              
154A: DD 77 06        LD      (IX+$06),A          
154D: DD 77 07        LD      (IX+$07),A          
1550: 18 2A           JR      $157C               ; {}
1552: 7E              LD      A,(HL)              
1553: DD 77 08        LD      (IX+$08),A          
1556: DD 77 09        LD      (IX+$09),A          
1559: A7              AND     A                   
155A: 28 20           JR      Z,$157C             ; {}
155C: 47              LD      B,A                 
155D: E6 E0           AND     $E0                 
155F: 07              RLCA                        
1560: 07              RLCA                        
1561: 07              RLCA                        
1562: 32 C4 42        LD      ($42C4),A           ; {ram.m42C4}
1565: 78              LD      A,B                 
1566: 16 00           LD      D,$00               
1568: 21 00 00        LD      HL,$0000            
156B: E6 0F           AND     $0F                 
156D: 87              ADD     A,A                 
156E: 5F              LD      E,A                 
156F: 78              LD      A,B                 
1570: E6 10           AND     $10                 
1572: 20 04           JR      NZ,$1578            ; {}
1574: ED 52           SBC     HL,DE               
1576: 18 01           JR      $1579               ; {}
1578: 19              ADD     HL,DE               
1579: 22 C5 42        LD      ($42C5),HL          ; {ram.m42C5}
157C: DD 6E 02        LD      L,(IX+$02)          
157F: DD 66 03        LD      H,(IX+$03)          
1582: 23              INC     HL                  
1583: DD 75 02        LD      (IX+$02),L          
1586: DD 74 03        LD      (IX+$03),H          
1589: C3 E7 14        JP      $14E7               ; {}
158C: 06 00           LD      B,$00               
158E: DF              RST     $18                 
158F: DD 36 00 FF     LD      (IX+$00),$FF        
1593: C9              RET                         
1594: CD 9C 15        CALL    $159C               ; {}
1597: 06 00           LD      B,$00               
1599: DF              RST     $18                 
159A: 18 39           JR      $15D5               ; {}
159C: 78              LD      A,B                 
159D: E6 E0           AND     $E0                 
159F: 07              RLCA                        
15A0: 07              RLCA                        
15A1: 07              RLCA                        
15A2: 47              LD      B,A                 
15A3: 3E 01           LD      A,$01               
15A5: 10 04           DJNZ    $15AB               ; {}
15A7: DD 77 00        LD      (IX+$00),A          
15AA: C9              RET                         
15AB: 07              RLCA                        
15AC: 18 F7           JR      $15A5               ; {}
15AE: C5              PUSH    BC                  
15AF: CD 9C 15        CALL    $159C               ; {}
15B2: C1              POP     BC                  
15B3: 78              LD      A,B                 
15B4: E6 1F           AND     $1F                 
15B6: 3D              DEC     A                   
15B7: 07              RLCA                        
15B8: 4F              LD      C,A                 
15B9: 06 00           LD      B,$00               
15BB: DD 6E 04        LD      L,(IX+$04)          
15BE: DD 66 05        LD      H,(IX+$05)          
15C1: 09              ADD     HL,BC               
15C2: 5E              LD      E,(HL)              
15C3: 23              INC     HL                  
15C4: 56              LD      D,(HL)              
15C5: EB              EX      DE,HL               
15C6: EF              RST     $28                 
15C7: DD 7E 09        LD      A,(IX+$09)          
15CA: DD 77 08        LD      (IX+$08),A          
15CD: DD 46 06        LD      B,(IX+$06)          
15D0: 78              LD      A,B                 
15D1: DD 77 07        LD      (IX+$07),A          
15D4: DF              RST     $18                 
15D5: DD 6E 02        LD      L,(IX+$02)          
15D8: DD 66 03        LD      H,(IX+$03)          
15DB: 23              INC     HL                  
15DC: DD 75 02        LD      (IX+$02),L          
15DF: DD 74 03        LD      (IX+$03),H          
15E2: C9              RET                         

15E3: 6B              LD      L,E                 
15E4: 08              EX      AF,AF'              
15E5: F2 07 80        JP      P,$8007             ; 
15E8: 07              RLCA                        
15E9: 14              INC     D                   
15EA: 07              RLCA                        
15EB: AE              XOR     (HL)                
15EC: 06 4E           LD      B,$4E               
15EE: 06 F3           LD      B,$F3               
15F0: 05              DEC     B                   
15F1: 9E              SBC     (HL)                
15F2: 05              DEC     B                   
15F3: 4E              LD      C,(HL)              
15F4: 05              DEC     B                   
15F5: 01 05 B9        LD      BC,$B905            
15F8: 04              INC     B                   
15F9: 76              HALT                        
15FA: 04              INC     B                   
15FB: 36 04           LD      (HL),$04            
15FD: F9              LD      SP,HL               
15FE: 03              INC     BC                  
15FF: C0              RET     NZ                  
1600: 03              INC     BC                  
1601: 8A              ADC     A,D                 
1602: 03              INC     BC                  
1603: 57              LD      D,A                 
1604: 03              INC     BC                  
1605: 27              DAA                         
1606: 03              INC     BC                  
1607: FA 02 CF        JP      M,$CF02             ; 
160A: 02              LD      (BC),A              
160B: A7              AND     A                   
160C: 02              LD      (BC),A              
160D: 81              ADD     A,C                 
160E: 02              LD      (BC),A              
160F: 5D              LD      E,L                 
1610: 02              LD      (BC),A              
1611: 3B              DEC     SP                  
1612: 02              LD      (BC),A              
1613: 1B              DEC     DE                  
1614: 02              LD      (BC),A              
1615: FD 
1616: 01 E0 01        LD      BC,$01E0            
1619: C5              PUSH    BC                  
161A: 01 AC 01        LD      BC,$01AC            
161D: 94              SUB     H                   
161E: 01 7D 01        LD      BC,$017D            
1621: 68              LD      L,B                 
1622: 01 53 01        LD      BC,$0153            
1625: 40              LD      B,B                 
1626: 01 2E 01        LD      BC,$012E            
1629: 1D              DEC     E                   
162A: 01 0D 01        LD      BC,$010D            
162D: FE 00           CP      $00                 
162F: F0              RET     P                   
1630: 00              NOP                         
1631: E3              EX      (SP),HL             
1632: 00              NOP                         
1633: D6 00           SUB     $00                 
1635: CA 00 BE        JP      Z,$BE00             ; 
1638: 00              NOP                         
1639: B4              OR      H                   
163A: 00              NOP                         
163B: AA              XOR     D                   
163C: 00              NOP                         
163D: A0              AND     B                   
163E: 00              NOP                         
163F: 97              SUB     A                   
1640: 00              NOP                         
1641: 8F              ADC     A,A                 
1642: 00              NOP                         
1643: 87              ADD     A,A                 
1644: 00              NOP                         
1645: 7F              LD      A,A                 
1646: 00              NOP                         
1647: 78              LD      A,B                 
1648: 00              NOP                         
1649: 71              LD      (HL),C              
164A: 00              NOP                         
164B: 6B              LD      L,E                 
164C: 00              NOP                         
164D: 65              LD      H,L                 
164E: 00              NOP                         
164F: 5F              LD      E,A                 
1650: 00              NOP                         
1651: 5A              LD      E,D                 
1652: 00              NOP                         
1653: 55              LD      D,L                 
1654: 00              NOP                         
1655: 50              LD      D,B                 
1656: 00              NOP                         
1657: 4C              LD      C,H                 
1658: 00              NOP                         
1659: 47              LD      B,A                 
165A: 00              NOP                         
165B: 11 0F 0D        LD      DE,$0D0F            
165E: 0B              DEC     BC                  
165F: 0A              LD      A,(BC)              
1660: 09              ADD     HL,BC               
1661: 08              EX      AF,AF'              
1662: 07              RLCA                        
1663: 03              INC     BC                  
1664: 05              DEC     B                   
1665: 14              INC     D                   
1666: 13              INC     DE                  
1667: 11 10 0F        LD      DE,$0F10            
166A: 0E 3A           LD      C,$3A               
166C: C8              RET     Z                   
166D: 42              LD      B,D                 
166E: A7              AND     A                   
166F: C0              RET     NZ                  

; Continue time-running-out initialization
1670: 21 94 16        LD      HL,$1694            
1673: 11 B0 42        LD      DE,$42B0            
1676: 01 0A 00        LD      BC,$000A            
1679: ED B0           LDIR                        
167B: 3A C3 42        LD      A,($42C3)           ; {ram.m42C3}
167E: 87              ADD     A,A                 ; times 2
167F: 4F              LD      C,A                 ; times ...
1680: 87              ADD     A,A                 ; ... four
1681: 81              ADD     A,C                 ; times 5
1682: 4F              LD      C,A                 
1683: 21 9E 16        LD      HL,$169E            
1686: 09              ADD     HL,BC               ; B is zero from before
1687: 11 B2 42        LD      DE,$42B2            
168A: 7E              LD      A,(HL)              
168B: 12              LD      (DE),A              
168C: CD 91 16        CALL    $1691               ; {}
168F: 7E              LD      A,(HL)              
1690: 12              LD      (DE),A              
1691: 23              INC     HL                  
1692: 13              INC     DE                  
1693: C9              RET                         

1694: 01 01 00 00 00 00 00 00 00 00                        

169E: AA                                
169F: 16 CD                          
16A1: 16 CD           LD      D,$CD               
16A3: 16 B8           LD      D,$B8               
16A5: 16 CD           LD      D,$CD               
16A7: 16 CD           LD      D,$CD               
16A9: 16 1F           LD      D,$1F               
16AB: 0F              RRCA                        
16AC: 3F              CCF                         
16AD: 09              ADD     HL,BC               
16AE: 5F              LD      E,A                 
16AF: 09              ADD     HL,BC               
16B0: 7F              LD      A,A                 
16B1: 00              NOP                         
16B2: 6D              LD      L,L                 
16B3: 71              LD      (HL),C              
16B4: 74              LD      (HL),H              
16B5: 79              LD      A,C                 
16B6: D6 FF           SUB     $FF                 
16B8: 1F              RRA                         
16B9: 02              LD      (BC),A              
16BA: 3F              CCF                         
16BB: 07              RLCA                        
16BC: 5F              LD      E,A                 
16BD: 09              ADD     HL,BC               
16BE: 7F              LD      A,A                 
16BF: 00              NOP                         
16C0: 94              SUB     H                   
16C1: 8D              ADC     A,L                 
16C2: 88              ADC     A,B                 
16C3: 94              SUB     H                   
16C4: 8D              ADC     A,L                 
16C5: 88              ADC     A,B                 
16C6: 94              SUB     H                   
16C7: 8D              ADC     A,L                 
16C8: 88              ADC     A,B                 
16C9: 94              SUB     H                   
16CA: 8D              ADC     A,L                 
16CB: C8              RET     Z                   
```

# Unused Area

```code                
16CC: FF FF FF FF
16D0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
16E0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF    
16F0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF    
1700: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF    
1710: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF    
1720: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF    
1730: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF    
1740: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF    
1750: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF    
1760: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF    
1770: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
1780: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF  
1790: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF  
17A0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF  
17B0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF  
17C0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF  
17D0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF  
17E0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF  
17F0: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF                  
```

