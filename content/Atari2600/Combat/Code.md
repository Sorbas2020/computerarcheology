![Combat](A2600Combat.jpg)

# Combat NTSC

>>> cpu 6502

>>> binary F000:Combat.bin

>>> memoryTable hard 

[Hardware Info](../Stella.md)

>>> memoryTable ram 

[RAM Usage](RAMUse.md)

This is the NTSC version of the code.

```html
<!-- Cache some commonly-used values -->
<canvas width="0" height="0"
        data-canvasFunction="TileEngine.handleTileCanvas"
        data-labelColor=""
        data-pixWidth="10"
        data-pixHeight="10"
        data-gap="0.25"
        data-gridPad="1">      
</canvas>
<canvas width="0" height="0"
       data-colorsName="TANKPLAYFIELD"
       data-colors='["#BBD46E","#8C2A44"]'>       
</canvas>
<canvas width="0" height="0"
       data-colorsName="PLANEPLAYFIELD"
       data-colors='["#000088","#90B4EC"]'>       
</canvas>
<canvas width="0" height="0"
       data-colorsName="JETPLAYFIELD"
       data-colors='["#783CA4","#689CC0"]'>
</canvas>
<canvas width="0" height="0"
       data-colorsName="TANKP0"
       data-colors='["#BBD46E","#B03C3C"]'>
</canvas>
<canvas width="0" height="0"
       data-colorsName="PLANEP0"
       data-colors='["#000088","#9CCC7C"]'>
</canvas>
<canvas width="0" height="0"
       data-colorsName="JETP0"
       data-colors='["#783CA4","#6E8454"]'>
</canvas>
```

```code
F000: 78              SEI                         ; Turn off interrupts
F001: D8              CLD                         ; Binary mode (not BCD)
F002: A2 FF           LDX     #$FF                ; Stack pointer to 1_FF ...
F004: 9A              TXS                         ; ... ghosts to 0_FF

F005: A2 5D           LDX     #$5D                ; Clear memory ...
F007: 20 BD F5        JSR     $F5BD               ; {} ... 00 through A2 (hardware registers and game variables)
F00A: A9 10           LDA     #$10                ; Console switches are all ...
F00C: 8D 83 02        STA     $0283               ; {hard.SWBCNT} ... inputs (D4 is not used)
F00F: 85 88           STA     $88                 ; {ram.m88} ?? Is this the debounce?

F011: 20 A3 F1        JSR     $F1A3               ; {}
```

# Main Game Loop

```code
main:
F014: 20 32 F0        JSR     $F032               ; {code.StartTVFrame} Start the next TV frame
F017: 20 57 F1        JSR     $F157               ; {} ?? switches ??
F01A: 20 72 F5        JSR     $F572               ; {} ?? pro switches ??
F01D: 20 DA F2        JSR     $F2DA               ; {}
F020: 20 44 F4        JSR     $F444               ; {} ?? Collisions ??
F023: 20 14 F2        JSR     $F214               ; {}
F026: 20 A9 F2        JSR     $F2A9               ; {}
F029: 20 F2 F1        JSR     $F1F2               ; {code.ScoreGraphics} Convert the player scores to graphics offsets
F02C: 20 54 F0        JSR     $F054               ; {code.DrawVisible} Draw the screen
F02F: 4C 14 F0        JMP     $F014               ; {code.main} Back to top of main loop
```

# Start the TV Frame

```code
StartTVFrame:
; Increment the frame counter and trigger the vertical sync.
; The timer is set to time the blanking period.
F032: E6 86           INC     $86                 ; {ram.frameCounter} Bump the frame counter
F034: 85 2B           STA     $2B                 ; {hard.HMCLR} Clear horizontal motion registers
F036: A9 02           LDA     #$02                ; D1 bit ON
F038: 85 02           STA     $02                 ; {hard.WSYNC} Wait for the end of the current line
F03A: 85 01           STA     $01                 ; {hard.VBLANK} Turn the electron beam off
F03C: 85 02           STA     $02                 ; {hard.WSYNC} Wait for all ...
F03E: 85 02           STA     $02                 ; {hard.WSYNC} ... the electrons ...
F040: 85 02           STA     $02                 ; {hard.WSYNC} ... to drain out
F042: 85 00           STA     $00                 ; {hard.VSYNC} Trigger the vertical sync signal
F044: 85 02           STA     $02                 ; {hard.WSYNC} Hold for ...
F046: 85 02           STA     $02                 ; {hard.WSYNC} ... two scan lines
F048: A9 00           LDA     #$00                ; D1 bit OFF
F04A: 85 02           STA     $02                 ; {hard.WSYNC} Hold for a third line
F04C: 85 00           STA     $00                 ; {hard.VSYNC} Release the vertical sync signal
F04E: A9 2B           LDA     #$2B                ; Set timer to 43*64 = 2752 machine ...
F050: 8D 96 02        STA     $0296               ; {hard.TIM64T} ... cycles 2752/(228/3) = 36 scanlines
F053: 60              RTS                         ; Done
```

# Draw the Visible Screen

```code
DrawVisible:
;
; TODO Blurb on Frame 30 and the key
;
F054: A9 20           LDA     #$20                ; Start counting at 32 ...
F056: 85 B4           STA     $B4                 ; {ram.scanlineNumber} ... makes the playfield math easier
F058: 85 02           STA     $02                 ; {hard.WSYNC} Wait for the end of the current line (ensure HMOVE is in the horiz blanking)
F05A: 85 2A           STA     $2A                 ; {hard.HMOVE} Apply horizontal movement to all objects
F05C: AD 84 02        LDA     $0284               ; {hard.INTIM} Wait for the visible TV to ...
F05F: D0 FB           BNE     $F05C               ; {} ... reach the visible area
F061: 85 02           STA     $02                 ; {hard.WSYNC} 37th scanline
F063: 85 2C           STA     $2C                 ; {hard.CXCLR} Clear the collision flags
F065: 85 01           STA     $01                 ; {hard.VBLANK} Turn the electron beam back on
F067: BA              TSX                         ; Save stack ...
F068: 86 D3           STX     $D3                 ; {ram.stackPointer} ... pointer
F06A: A9 02           LDA     #$02                ; Playfield left/right color of P0/P1
F06C: 85 0A           STA     $0A                 ; {hard.CTRLPF} ... on top?
F06E: A6 DC           LDX     $DC                 ; {ram.mDC}
F070: 85 02           STA     $02                 ; {hard.WSYNC}
F072: CA              DEX                         ; 
F073: D0 FB           BNE     $F070               ; {}
F075: A5 DC           LDA     $DC                 ; {ram.mDC} ??
F077: C9 0E           CMP     #$0E                
F079: F0 52           BEQ     $F0CD               ; {} Skip drawing the top numbers
F07B: A2 05           LDX     #$05                ; 5 rows per digit
F07D: A9 00           LDA     #$00                ; Clear ...
F07F: 85 DE           STA     $DE                 ; {ram.nextLeft} ... next pattern for left two digits
F081: 85 DF           STA     $DF                 ; {ram.nextRight} Clear next pattern for right two digits
;
; Loop for drawing digits
; From Z26 log for frame 30
; Lines 42 through 53
;
; 42|                     *.|.....................................................| At F083
;
; Loop from F083 to F0CA
; 43|...1...................|.............1........................*..............| First pass - blanks
; 44|.........1.............|................1.....*..............................| Digit row 1
;
; 45|...1...................|.............1........................*..............| Duplicate row 1
; 46|.........1.............|................1.....*..............................| Digit row 2
; 47|...1...................|.............1........................*..............| Duplicate row 2
; 48|.........1.............|................1.....*..............................| Digit row 3
; 49|...1...................|.............1........................*..............| Duplicate row 3
; 50|.........1.............|................1.....*..............................| Digit row 4
; 51|...1...................|.............1........................*..............| Duplicate row 4
; 52|.........1.............|................1.....*..............................| Digit row 5
; 53|...1...................|.............1........................*..............| Duplicate row 5
;
; 54|.........1.........1..*|.....................................................| Digit ... aborted at F0CD
;
F083: 85 02           STA     $02                 ; {hard.WSYNC} 42 21 {-hard_WSYNC} Wait for next row
F085: A5 DE           LDA     $DE                 ; {ram.nextLeft} 43  0 {-ram_nextLeft} Digit graphics calculated last row
F087: 85 0E           STA     $0E                 ; {hard.PF1} 43  3 {-hard_PF1} Duplicate the left number from last row
F089: A4 E2           LDY     $E2                 ; {ram.leftDigitMSD} 43  6 {-ram_leftDigitMSD} Index to left number left digit
F08B: B9 C5 F5        LDA     $F5C5,Y             ; {} 43  9 Get graphics for digit
F08E: 29 F0           AND     #$F0                ; 43 13 Only the left part of the pattern
F090: 85 DE           STA     $DE                 ; {ram.nextLeft} 43 15 {-ram_nextLeft}  New graphics for left number
F092: A4 E0           LDY     $E0                 ; {ram.leftDigitLSD} 43 18 {-ram_leftDigitLSD} Index to left number right digit
F094: B9 C5 F5        LDA     $F5C5,Y             ; {} 43 21 Get graphics for digit
F097: 29 0F           AND     #$0F                ; 43 25 Only the right part of the pattern
F099: 05 DE           ORA     $DE                 ; {ram.nextLeft} 43 27 {-ram_nextLeft} Combine left and right digits
F09B: 85 DE           STA     $DE                 ; {ram.nextLeft} 43 30 {-ram_nextLeft} We'll use it next row
;
F09D: A5 DF           LDA     $DF                 ; {ram.nextRight} 43 33 {-ram_nextRight} Digit graphics calculated last row
F09F: 85 0E           STA     $0E                 ; {hard.PF1} 43 36 {-hard_PF1} ** Duplicate the right number from last row
F0A1: A4 E3           LDY     $E3                 ; {ram.rightDigitMSD} 43 39 {-ram_rightDigitMSD} Index to right number left digit
F0A3: B9 C5 F5        LDA     $F5C5,Y             ; {} 43 42 Get graphics for digit
F0A6: 29 F0           AND     #$F0                ; 43 46 Only the left part of the pattern
F0A8: 85 DF           STA     $DF                 ; {ram.nextRight} 43 48 {-ram_nextRight} New graphics for right number
F0AA: A4 E1           LDY     $E1                 ; {ram.rightDigitLSD} 43 51 {-ram_rightDigitLSD} Index to the right number right digit
F0AC: B9 C5 F5        LDA     $F5C5,Y             ; {} 43 54 Get graphics for digit
F0AF: 25 87           AND     $87                 ; {ram.maskRightNumber} 43 58 {-ram_maskRightNumber} Blank the right number right digit if in game-select
F0B1: 85 02           STA     $02                 ; {hard.WSYNC} 43 61 {-hard_WSYNC} Wait for next row
; 
F0B3: 05 DF           ORA     $DF                 ; {ram.nextRight} 44  0 {-ram_nextRight} Combine left and right digits
F0B5: 85 DF           STA     $DF                 ; {ram.nextRight} 44  3 {-ram_nextRight} We'll use it later on this row
F0B7: A5 DE           LDA     $DE                 ; {ram.nextLeft} 44  6 {-ram_nextLeft} Get the newly calculated graphics
F0B9: 85 0E           STA     $0E                 ; {hard.PF1} 44  9 {-hard_PF1} Draw the new left number
F0BB: CA              DEX                         ; 44 12 All digit rows done?
F0BC: 30 0F           BMI     $F0CD               ; {} 44 14 Yes ... done
; On the last row we write a bogus value for the first number, but we quickly clear it out at F0CD before
; it gets drawn
F0BE: E6 E0           INC     $E0                 ; {ram.leftDigitLSD} 44 16 {-ram_leftDigitLSD} Next row in left digit LSD
F0C0: E6 E2           INC     $E2                 ; {ram.leftDigitMSD} 44 21 {-ram_leftDigitMSD} Next row in left digit MSD
F0C2: E6 E1           INC     $E1                 ; {ram.rightDigitLSD} 44 26 {-ram_rightDigitLSD} Next row in right digit LSD
F0C4: E6 E3           INC     $E3                 ; {ram.rightDigitMSD} 44 31 {-ram_rightDigitMSD} Next row in right digit MSD
F0C6: A5 DF           LDA     $DF                 ; {ram.nextRight} 44 36 {-ram_nextRight} Get the newly calculated graphics
F0C8: 85 0E           STA     $0E                 ; {hard.PF1} 44 39 {-hard_PF1} **  Draw the right number
F0CA: 4C 83 F0        JMP     $F083               ; {} 44 42 Back for all rows of digits
;
; Draw the play area
F0CD: A9 00           LDA     #$00                ; 54 17 Clear the score for ...
F0CF: 85 0E           STA     $0E                 ; {hard.PF1} 54 19 {-hard_PF1} ... next row
F0D1: 85 02           STA     $02                 ; {hard.WSYNC} 54 22 {-hard_WSYNC} Make a blank line
;
; 55|..W.....C.....c        |                                                     |
;
F0D3: A9 05           LDA     #$05                ; 55  0 Playfield over players and ...
F0D5: 85 0A           STA     $0A                 ; {hard.CTRLPF} 55  2 {-hard_CTRLPF} 55  2 ... reflect playfield
F0D7: A5 D6           LDA     $D6                 ; {ram.colorP0} 55  5 {-ram_colorP0} 55  5 Set color ...
F0D9: 85 06           STA     $06                 ; {hard.COLUP0} 55  8 {-hard_COLUP0} 55  8 ... player 0
F0DB: A5 D7           LDA     $D7                 ; {ram.colorP1} 55 11 {-ram_colorP1} 55 11 Set color ...
F0DD: 85 07           STA     $07                 ; {hard.COLUP1} 55 14 {-hard_COLUP1} 55 14 ... player 1
;
; Top of loop
;
; Same loop for the rest of the screen, but at 155 we are in the middle of the screen
; where the players are. Let's pick up the video timing at the top of the loop midway
; across the scanline 155.
; 155|                       |                   .........................*........|
; 156|X..........u..........t|....................................................Y|
; 157|.........0.......1.....|..2.........................................*........|
; 
; Using the stackpointer here to speed up the writes.
; We start pointing to ENAM1 and work lower in memory.
; This is the playing area where the players and missiles are.
F0DF: A2 1E           LDX     #$1E                ; 155 42 Pointer to ...
F0E1: 9A              TXS                         ; 155 44 ... ENAM1
;
;Player 0
;
F0E2: 38              SEC                         ; 155 46 Clear the borrow flag
F0E3: A5 A4           LDA     $A4                 ; {ram.player0row} 155 48 {-ram_player0row} Player 0's row number
F0E5: E5 B4           SBC     $B4                 ; {ram.scanlineNumber} 155 51 {-ram_scanlineNumber} Compare it to the current row
; To speed up the lookup, the players graphics are interleaved. Even rows
; are for player 0 and odd rows are for player 1.
F0E7: 29 FE           AND     #$FE                ; 155 54 Even is for player 0
F0E9: AA              TAX                         ; 155 56 Hold the graphics pointer
F0EA: 29 F0           AND     #$F0                ; 155 68 Within the 16 row window?
F0EC: F0 04           BEQ     $F0F2               ; {} 155 60 Yes ... draw the player
F0EE: A9 00           LDA     #$00                ; No player 0 graphics on this row
F0F0: F0 02           BEQ     $F0F4               ; {} JMP $F0F4
F0F2: B5 BD           LDA     $BD,X               ; {ram.playerXpicture} 155 63 {-ram_playerXpicture} 155 63 Get the graphics for this row
F0F4: 85 02           STA     $02                 ; {hard.WSYNC} 155 67 {-hard_WSYNC} 155 67 Wait for next row
F0F6: 85 1B           STA     $1B                 ; {hard.GRP0} 156  0 {-hard_GRP0} 156  0 Draw player 0 on this row
;
; Missile 1
;
F0F8: A5 A7           LDA     $A7                 ; {ram.missile1row} 156  3 {-ram_missile1row} Missile 1 row
F0FA: 45 B4           EOR     $B4                 ; {ram.scanlineNumber} 156  6 {-ram_scanlineNumber} Compare it to the current row
F0FC: 29 FE           AND     #$FE                ; 156  9 Odd and even rows (doubling)
; The Z flag is in the D1 position of the status register. This maps to
; D1 of the Enable-Missile-1. Thus when the current row is the same as the
; missile the Z flag will be set and will enable the missile with the push.
F0FE: 08              PHP                         ; 156  11 Turn missile 1 on or off
;
; Missile 0
; 
F0FF: A5 A6           LDA     $A6                 ; {ram.missile0row} 156 14 {-ram_missile0row} Missile 0 row
F101: 45 B4           EOR     $B4                 ; {ram.scanlineNumber} 156 17 {-ram_scanlineNumber} Compare it to the current row
F103: 29 FE           AND     #$FE                ; 156 20 Odd and even rows (doubling)
F105: 08              PHP                         ; 156 22 Turn missile 0 on or off
;
; Playfield graphics pointers.
;
; The playfield pattern is a table of 12 entries. This loop runs the table forwards with
; each entry drawn over 8 rows. 8*12 = 96 rows. Then the loop runs the table backwards
; with each entry drawn over 8 rows. 96 rows again. The bottom of the screen reflects
; the top.
;
; The reflection happens with the upper bit of the row count in B4. Positive values are the
; upper half of the screen. Negative values are the lower half. The number "12", as in
; twelve entries, is difficult to work with but "16" is easy. The math assumes the table
; is 16 values and starts with the fourth value. The loop uses entries 4-16 on the positive
; top half. Then 16-4 on the bottom half. The graphics pointers are backed up 4 bytes so
; that the table looks like 16 bytes. B4 starts at 32 (32/8=4) at the top half of the
; screen. In the bottom half the check at F10C keeps the code from drawing the bogus
; values in the table entries 3, 2, 1, and 0.
;  
F106: A5 B4           LDA     $B4                 ; {ram.scanlineNumber} 156 25 {-ram_scanlineNumber} Current row
F108: 10 02           BPL     $F10C               ; {} 156 28 We are in the top (non reflected) region
; $B4 is 80, scanline 152
F10A: 49 F8           EOR     #$F8                ; 156 30 Reflection: run the table backwards from 15
F10C: C9 20           CMP     #$20                ; 156 32 At the bottom of the screen just use ...
F10E: 90 04           BCC     $F114               ; {} 156 34 ... the last pattern over and over
; Playfield graphics are 8-rows tall
F110: 4A              LSR     A                   ; 156 36 Divide ...
F111: 4A              LSR     A                   ; 156 38 ... by ...
F112: 4A              LSR     A                   ; 156 40 ... 8 (each playfield value covers 8 rows)
F113: A8              TAY                         ; 156 42 Graphics offset to Y for later
;
F114: A5 A5           LDA     $A5                 ; {ram.player1row} 156 44 {-ram_player1row} Player 1's row number
F116: 38              SEC                         ; 156 47 Clear the borrow flag (this is how 6502 works)
F117: E5 B4           SBC     $B4                 ; {ram.scanlineNumber} 156 49 {-ram_scanlineNumber} Compare the row numbers
F119: E6 B4           INC     $B4                 ; {ram.scanlineNumber} 156 52 {-ram_scanlineNumber} Bump to next row (doubling)
F11B: EA              NOP                         ; 156 57 ?? Timing ?
F11C: 09 01           ORA     #$01                ; 156 59 Odd is for player 1
F11E: AA              TAX                         ; 156 61 Hold the graphics pointer
F11F: 29 F0           AND     #$F0                ; 156 63 Within the 16 row window?
F121: F0 04           BEQ     $F127               ; {} 156 65 Yes ... draw the player
F123: A9 00           LDA     #$00                ; No player 1 graphics on this row
F125: F0 02           BEQ     $F129               ; {} JMP $F129
F127: B5 BD           LDA     $BD,X               ; {ram.playerXpicture} 156 68 {-ram_playerXpicture} Get the graphics for this row
F129: 24 82           BIT     $82                 ; {ram.skipPlayfield} 156 72 {-ram_skipPlayfield} Bit 7 goes to the M flag
F12B: 85 1C           STA     $1C                 ; {hard.GRP1} 156 75 {-hard_GRP1} Draw player 1 on this row
; 
F12D: 30 0C           BMI     $F13B               ; {} 157  2 If D7 of $82 is set, skip the playfield
F12F: B1 B5           LDA     ($B5),Y             ; {ram.pf0Graphics} 157  4 {-ram_pf0Graphics} Copy the ...
F131: 85 0D           STA     $0D                 ; {hard.PF0} 157  9 {-hard_PF0} ... PF0 graphics
F133: B1 B7           LDA     ($B7),Y             ; {ram.pf1Graphics} 157 12 {-ram_pf1Graphics} Copy the ...
F135: 85 0E           STA     $0E                 ; {hard.PF1} 157 17 {-hard_PF1} ... PF1 graphics
F137: B1 B9           LDA     ($B9),Y             ; {ram.pf2Graphics} 157 20 {-ram_pf2Graphics} Copy the ...
F139: 85 0F           STA     $0F                 ; {hard.PF2} 157 25 {-hard_PF2} ... PF2 graphics
F13B: E6 B4           INC     $B4                 ; {ram.scanlineNumber} 157 28 {-ram_scanlineNumber} Next row (we are doing 2 at a time)
F13D: A5 B4           LDA     $B4                 ; {ram.scanlineNumber} 157 33 {-ram_scanlineNumber} Have we done all ...
F13F: 49 EC           EOR     #$EC                ; 157 36 ... 236 rows?
F141: D0 9C           BNE     $F0DF               ; {} 157 38 No ... go back for more
;
; End of frame
;
; 258|x..........u..........t|.............................................y.......|
; 259|..0.......1.......2....|...............t..u..x..y..x..0..1..2...             |
; ?? See the "x..y..x" on this last line? Why clear the GRP0 twice ??
;
F143: A6 D3           LDX     $D3                 ; {ram.stackPointer} 259 33 {-ram_stackPointer} Restore the ...
F145: 9A              TXS                         ; 259 36 ... stack pointer
; We just EORed with EC (11101100) and checked for zero.
; The only way we get a zero is when A = EC, which means D1 is
; zero for the stores below.
F146: 85 1D           STA     $1D                 ; {hard.ENAM0} 259 38 {-hard_ENAM0} Turn off missile 0
F148: 85 1E           STA     $1E                 ; {hard.ENAM1} 259 41 {-hard_ENAM1} Turn off missile 1
F14A: 85 1B           STA     $1B                 ; {hard.GRP0} 259 44 {-hard_GRP0} Turn off player 0
F14C: 85 1C           STA     $1C                 ; {hard.GRP1} 259 47 {-hard_GRP1} Turn off player 1
F14E: 85 1B           STA     $1B                 ; {hard.GRP0} 259 50 {-hard_GRP0} Turn off player 0 (?? why again)
F150: 85 0D           STA     $0D                 ; {hard.PF0} 259 53 {-hard_PF0} Turn off playfield 0
F152: 85 0E           STA     $0E                 ; {hard.PF1} 259 56 {-hard_PF1} Turn off playfield 1
F154: 85 0F           STA     $0F                 ; {hard.PF2} 259 59 {-hard_PF2} Turn off playfield 2
F156: 60              RTS                         ; 259 62 Done

; ?? Called from main loop
F157: AD 82 02        LDA     $0282               ; {hard.SWCHB} Console switches
F15A: 4A              LSR     A                   ; RESET switch to carry
F15B: B0 13           BCS     $F170               ; {} 1 means NOT pressed ... skip
F15D: A9 0F           LDA     #$0F                ; No longer blanking ...
F15F: 85 87           STA     $87                 ; {ram.maskRightNumber} ... the right digit for P1 score
F161: A9 FF           LDA     #$FF                
F163: 85 88           STA     $88                 ; {ram.m88}
F165: A9 80           LDA     #$80                
F167: 85 DD           STA     $DD                 ; {ram.mDD}
F169: A2 E6           LDX     #$E6                
F16B: 20 BD F5        JSR     $F5BD               ; {}
F16E: F0 60           BEQ     $F1D0               ; {} JMP F1D0
;
F170: A0 02           LDY     #$02                
F172: A5 DD           LDA     $DD                 ; {ram.mDD}
F174: 25 88           AND     $88                 ; {ram.m88}
F176: C9 F0           CMP     #$F0                
F178: 90 08           BCC     $F182               ; {}
F17A: A5 86           LDA     $86                 ; {ram.frameCounter}
F17C: 29 30           AND     #$30                
F17E: D0 02           BNE     $F182               ; {}
F180: A0 0E           LDY     #$0E                
;
F182: 84 DC           STY     $DC                 ; {ram.mDC}
F184: A5 86           LDA     $86                 ; {ram.frameCounter}
F186: 29 3F           AND     #$3F                
F188: D0 08           BNE     $F192               ; {}
F18A: 85 89           STA     $89                 ; {ram.m89}
F18C: E6 DD           INC     $DD                 ; {ram.mDD}
F18E: D0 02           BNE     $F192               ; {}
F190: 85 88           STA     $88                 ; {ram.m88}
F192: AD 82 02        LDA     $0282               ; {hard.SWCHB} Console switches
F195: 29 02           AND     #$02                ; SELECT pressed?
F197: F0 04           BEQ     $F19D               ; {} 0 means YES
F199: 85 89           STA     $89                 ; {ram.m89}
F19B: D0 54           BNE     $F1F1               ; {} JMP F1F1
;
F19D: 24 89           BIT     $89                 ; {ram.m89}
F19F: 30 50           BMI     $F1F1               ; {}
F1A1: E6 80           INC     $80                 ; {ram.m80}

; ?? Called before main loop ... initialization?
F1A3: A2 DF           LDX     #$DF                
F1A5: 20 BD F5        JSR     $F5BD               ; {}
F1A8: A9 FF           LDA     #$FF                
F1AA: 85 89           STA     $89                 ; {ram.m89}
F1AC: A4 80           LDY     $80                 ; {ram.m80}
F1AE: B9 D8 F7        LDA     $F7D8,Y             ; {}
F1B1: 85 A3           STA     $A3                 ; {ram.mA3}
F1B3: 49 FF           EOR     #$FF                
F1B5: D0 04           BNE     $F1BB               ; {}
F1B7: A2 DD           LDX     #$DD                
F1B9: D0 EA           BNE     $F1A5               ; {}
F1BB: A5 81           LDA     $81                 ; {ram.m81}
F1BD: F8              SED                         
F1BE: 18              CLC                         
F1BF: 69 01           ADC     #$01                
F1C1: 85 81           STA     $81                 ; {ram.m81}
F1C3: 85 A1           STA     $A1                 ; {ram.scoreP1}
F1C5: D8              CLD                         
F1C6: 24 A3           BIT     $A3                 ; {ram.mA3}
F1C8: 10 06           BPL     $F1D0               ; {}
F1CA: E6 85           INC     $85                 ; {ram.m85}
F1CC: 50 02           BVC     $F1D0               ; {}
F1CE: E6 85           INC     $85                 ; {ram.m85}
F1D0: 20 25 F5        JSR     $F525               ; {}
F1D3: A9 32           LDA     #$32                
F1D5: 85 A5           STA     $A5                 ; {ram.player1row}
F1D7: A9 86           LDA     #$86                
F1D9: 85 A4           STA     $A4                 ; {ram.player0row}
F1DB: 24 A3           BIT     $A3                 ; {ram.mA3}
F1DD: 30 12           BMI     $F1F1               ; {}
F1DF: 85 A5           STA     $A5                 ; {ram.player1row}
F1E1: 85 11           STA     $11                 ; {hard.RESP1} RESP1:28,11
F1E3: A9 08           LDA     #$08                
F1E5: 85 96           STA     $96                 ; {ram.m96}
F1E7: A9 20           LDA     #$20                
F1E9: 85 20           STA     $20                 ; {hard.HMP0} HMP0:29,12
F1EB: 85 21           STA     $21                 ; {hard.HMP1} HMP1:29,12
F1ED: 85 02           STA     $02                 ; {hard.WSYNC} WSYNC:29,12
F1EF: 85 2A           STA     $2A                 ; {hard.HMOVE} HMOVE:30,13
F1F1: 60              RTS                         

ScoreGraphics:
; Convert the score values in A1 to 5-byte digit offsets in E0,E2
; Convert the score values in A2 to 5-byte digit offsets in E1,E3
F1F2: A2 01           LDX     #$01                ; Loop over 1 and 0 ... score for each player
F1F4: B5 A1           LDA     $A1,X               ; {ram.scoreP1} Get score
F1F6: 29 0F           AND     #$0F                ; Just the lower digit
F1F8: 85 D2           STA     $D2                 ; {ram.mD2} We will add this back to make 5
F1FA: 0A              ASL     A                   ; Digit * 2
F1FB: 0A              ASL     A                   ; Digit * 4
F1FC: 18              CLC                         ; No carry
F1FD: 65 D2           ADC     $D2                 ; {ram.mD2} Digit * 5
F1FF: 95 E0           STA     $E0,X               ; {ram.leftDigitLSD} Store offset
F201: B5 A1           LDA     $A1,X               ; {ram.scoreP1} Get score again
F203: 29 F0           AND     #$F0                ; Upper digit this time
F205: 4A              LSR     A                   ; Digit*16 / 2 = Digit*8
F206: 4A              LSR     A                   ; Digit*4
F207: 85 D2           STA     $D2                 ; {ram.mD2} Hold Digit*4
F209: 4A              LSR     A                   ; Digit*2
F20A: 4A              LSR     A                   ; Digit*1
F20B: 18              CLC                         ; No carry
F20C: 65 D2           ADC     $D2                 ; {ram.mD2} Now Digit*5
F20E: 95 E2           STA     $E2,X               ; {ram.leftDigitMSD} Store offset
F210: CA              DEX                         ; Loop back for ...
F211: 10 E1           BPL     $F1F4               ; {} ... players 1 and 0
F213: 60              RTS                         ; Done

; ?? Called from main loop
F214: 24 83           BIT     $83                 ; {ram.m83}
F216: 50 04           BVC     $F21C               ; {}
F218: A9 30           LDA     #$30                
F21A: 10 02           BPL     $F21E               ; {}
F21C: A9 20           LDA     #$20                
F21E: 85 B1           STA     $B1                 ; {ram.mB1}
F220: A2 03           LDX     #$03                
F222: 20 54 F2        JSR     $F254               ; {}
F225: CA              DEX                         
F226: 20 54 F2        JSR     $F254               ; {}
F229: CA              DEX                         
F22A: B5 8D           LDA     $8D,X               ; {ram.m8D}
F22C: 29 08           AND     #$08                
F22E: 4A              LSR     A                   
F22F: 4A              LSR     A                   
F230: 86 D1           STX     $D1                 ; {ram.mD1}
F232: 18              CLC                         
F233: 65 D1           ADC     $D1                 ; {ram.mD1}
F235: A8              TAY                         
F236: B9 A8 00        LDA     $00A8,Y             ; {ram.mA8}
F239: 38              SEC                         
F23A: 30 01           BMI     $F23D               ; {}
F23C: 18              CLC                         
F23D: 2A              ROL     A                   
F23E: 99 A8 00        STA     $00A8,Y             ; {ram.mA8}
F241: 90 0D           BCC     $F250               ; {}
F243: B5 AC           LDA     $AC,X               ; {ram.mAC}
F245: 29 01           AND     #$01                
F247: 0A              ASL     A                   
F248: 0A              ASL     A                   
F249: 0A              ASL     A                   
F24A: 0A              ASL     A                   
F24B: 85 B1           STA     $B1                 ; {ram.mB1}
F24D: 20 54 F2        JSR     $F254               ; {}
F250: CA              DEX                         
F251: F0 D7           BEQ     $F22A               ; {}
F253: 60              RTS                         
F254: F6 AC           INC     $AC,X               ; {ram.mAC}
F256: B5 95           LDA     $95,X               ; {ram.m95}
F258: 29 0F           AND     #$0F                
F25A: 18              CLC                         
F25B: 65 B1           ADC     $B1                 ; {ram.mB1}
F25D: A8              TAY                         
F25E: B9 F7 F5        LDA     $F5F7,Y             ; {} ??DATA??
F261: 85 B0           STA     $B0                 ; {ram.mB0}
F263: 24 82           BIT     $82                 ; {ram.skipPlayfield}
F265: 70 13           BVS     $F27A               ; {}
F267: B5 95           LDA     $95,X               ; {ram.m95}
F269: 38              SEC                         
F26A: E9 02           SBC     #$02                
F26C: 29 03           AND     #$03                
F26E: D0 0A           BNE     $F27A               ; {}
F270: B5 AC           LDA     $AC,X               ; {ram.mAC}
F272: 29 03           AND     #$03                
F274: D0 04           BNE     $F27A               ; {}
F276: A9 08           LDA     #$08                
F278: 85 B0           STA     $B0                 ; {ram.mB0}
F27A: A5 B0           LDA     $B0                 ; {ram.mB0}
F27C: 95 20           STA     $20,X               ; {hard.HMP0} HMP0:28,20,22 HMP1:26,18,19 HMM1:lots HMM0:lots
F27E: 29 0F           AND     #$0F                
F280: 38              SEC                         
F281: E9 08           SBC     #$08                
F283: 85 D4           STA     $D4                 ; {ram.mD4}
F285: 18              CLC                         
F286: 75 A4           ADC     $A4,X               ; {ram.player0row}
F288: 24 A3           BIT     $A3                 ; {ram.mA3}
F28A: 30 04           BMI     $F290               ; {}
F28C: E0 02           CPX     #$02                
F28E: B0 10           BCS     $F2A0               ; {}
F290: C9 DB           CMP     #$DB                
F292: B0 04           BCS     $F298               ; {}
F294: C9 25           CMP     #$25                
F296: B0 08           BCS     $F2A0               ; {}
F298: A9 D9           LDA     #$D9                
F29A: 24 D4           BIT     $D4                 ; {ram.mD4}
F29C: 30 02           BMI     $F2A0               ; {}
F29E: A9 28           LDA     #$28                
F2A0: 95 A4           STA     $A4,X               ; {ram.player0row}
F2A2: E0 02           CPX     #$02                
F2A4: B0 02           BCS     $F2A8               ; {}
F2A6: 95 25           STA     $25,X               ; {hard.VDELP0} VDELP1:27,26,19,20 VDELP0:29,21,22
F2A8: 60              RTS                         

; ?? Called from main loop
F2A9: A9 01           LDA     #$01                
F2AB: 25 86           AND     $86                 ; {ram.frameCounter}
F2AD: AA              TAX                         
F2AE: B5 95           LDA     $95,X               ; {ram.m95}
F2B0: 95 0B           STA     $0B,X               ; {hard.REFP0} REFP1:20,19,18,21 REFP0:lots
F2B2: 29 0F           AND     #$0F                
F2B4: A8              TAY                         
F2B5: 24 83           BIT     $83                 ; {ram.m83}
F2B7: 10 02           BPL     $F2BB               ; {}
F2B9: 94 97           STY     $97,X               ; {ram.m97}
F2BB: 8A              TXA                         
F2BC: 49 0E           EOR     #$0E                
F2BE: AA              TAX                         
F2BF: 98              TYA                         
F2C0: 0A              ASL     A                   
F2C1: 0A              ASL     A                   
F2C2: 0A              ASL     A                   
F2C3: C9 3F           CMP     #$3F                
F2C5: 18              CLC                         
F2C6: 30 03           BMI     $F2CB               ; {}
F2C8: 38              SEC                         
F2C9: 49 47           EOR     #$47                
F2CB: A8              TAY                         
F2CC: B1 BB           LDA     ($BB),Y             ; {ram.mBB}
F2CE: 95 BD           STA     $BD,X               ; {ram.playerXpicture}
F2D0: 90 02           BCC     $F2D4               ; {}
F2D2: 88              DEY                         
F2D3: 88              DEY                         
F2D4: C8              INY                         
F2D5: CA              DEX                         
F2D6: CA              DEX                         
F2D7: 10 F3           BPL     $F2CC               ; {}
F2D9: 60              RTS                         

; ?? Called from main loop
F2DA: A5 8A           LDA     $8A                 ; {ram.m8A}
F2DC: 38              SEC                         
F2DD: E9 02           SBC     #$02                
F2DF: 90 2B           BCC     $F30C               ; {}
F2E1: 85 8A           STA     $8A                 ; {ram.m8A}
F2E3: C9 02           CMP     #$02                
F2E5: 90 24           BCC     $F30B               ; {}
F2E7: 29 01           AND     #$01                
F2E9: AA              TAX                         
F2EA: F6 95           INC     $95,X               ; {ram.m95}
F2EC: B5 D8           LDA     $D8,X               ; {ram.mD8}
F2EE: 95 D6           STA     $D6,X               ; {ram.colorP0}
F2F0: A5 8A           LDA     $8A                 ; {ram.m8A}
F2F2: C9 F7           CMP     #$F7                
F2F4: 90 03           BCC     $F2F9               ; {}
F2F6: 20 08 F5        JSR     $F508               ; {}
F2F9: A5 8A           LDA     $8A                 ; {ram.m8A}
F2FB: 10 0E           BPL     $F30B               ; {}
F2FD: 4A              LSR     A                   
F2FE: 4A              LSR     A                   
F2FF: 4A              LSR     A                   
F300: 95 19           STA     $19,X               ; {hard.AUDV0} AUDV0:12,13
F302: A9 08           LDA     #$08                
F304: 95 15           STA     $15,X               ; {hard.AUDC0} AUDC0:12,13
F306: BD FE F7        LDA     $F7FE,X             ; {} Negative number??
F309: 95 17           STA     $17,X               ; {hard.AUDF0} AUDF0:12,13
F30B: 60              RTS                         

F30C: A2 01           LDX     #$01                
F30E: AD 82 02        LDA     $0282               ; {hard.SWCHB} SWCHB:7,16,14
F311: 85 D5           STA     $D5                 ; {ram.mD5}
F313: AD 80 02        LDA     $0280               ; {hard.SWCHA} SWCHA:7,16,14
F316: 24 88           BIT     $88                 ; {ram.m88}
F318: 30 02           BMI     $F31C               ; {}
F31A: A9 FF           LDA     #$FF                
F31C: 49 FF           EOR     #$FF                
F31E: 29 0F           AND     #$0F                
F320: 85 D2           STA     $D2                 ; {ram.mD2}
F322: A4 85           LDY     $85                 ; {ram.m85}
F324: B9 0F F7        LDA     $F70F,Y             ; {}
F327: 18              CLC                         
F328: 65 D2           ADC     $D2                 ; {ram.mD2}
F32A: A8              TAY                         
F32B: B9 12 F7        LDA     $F712,Y             ; {}
F32E: 29 0F           AND     #$0F                
F330: 85 D1           STA     $D1                 ; {ram.mD1}
F332: F0 04           BEQ     $F338               ; {}
F334: D5 91           CMP     $91,X               ; {ram.m91}
F336: D0 04           BNE     $F33C               ; {}
F338: D6 93           DEC     $93,X               ; {ram.m93}
F33A: D0 0D           BNE     $F349               ; {}
F33C: 95 91           STA     $91,X               ; {ram.m91}
F33E: A9 0F           LDA     #$0F                
F340: 95 93           STA     $93,X               ; {ram.m93}
F342: A5 D1           LDA     $D1                 ; {ram.mD1}
F344: 18              CLC                         
F345: 75 95           ADC     $95,X               ; {ram.m95}
F347: 95 95           STA     $95,X               ; {ram.m95}
F349: F6 8D           INC     $8D,X               ; {ram.m8D}
F34B: 30 1E           BMI     $F36B               ; {}
F34D: B9 12 F7        LDA     $F712,Y             ; {}
F350: 4A              LSR     A                   
F351: 4A              LSR     A                   
F352: 4A              LSR     A                   
F353: 4A              LSR     A                   
F354: 24 D5           BIT     $D5                 ; {ram.mD5}
F356: 30 23           BMI     $F37B               ; {}
F358: 95 8B           STA     $8B,X               ; {ram.m8B}
F35A: 0A              ASL     A                   
F35B: A8              TAY                         
F35C: B9 37 F6        LDA     $F637,Y             ; {}
F35F: 95 A8           STA     $A8,X               ; {ram.mA8}
F361: C8              INY                         
F362: B9 37 F6        LDA     $F637,Y             ; {}
F365: 95 AA           STA     $AA,X               ; {ram.mAA}
F367: A9 F0           LDA     #$F0                
F369: 95 8D           STA     $8D,X               ; {ram.m8D}
F36B: 20 80 F3        JSR     $F380               ; {}
F36E: AD 80 02        LDA     $0280               ; {hard.SWCHA} SWCHA:lots
F371: 4A              LSR     A                   
F372: 4A              LSR     A                   
F373: 4A              LSR     A                   
F374: 4A              LSR     A                   
F375: 06 D5           ASL     $D5                 ; {ram.mD5}
F377: CA              DEX                         
F378: F0 9C           BEQ     $F316               ; {}
F37A: 60              RTS                         
F37B: 38              SEC                         
F37C: E5 85           SBC     $85                 ; {ram.m85}
F37E: 10 D8           BPL     $F358               ; {}
F380: A5 A3           LDA     $A3                 ; {ram.mA3}
F382: 30 08           BMI     $F38C               ; {}
F384: 29 01           AND     #$01                
F386: F0 04           BEQ     $F38C               ; {}
F388: A5 DB           LDA     $DB                 ; {ram.mDB}
F38A: 95 D6           STA     $D6,X               ; {ram.colorP0}
F38C: B5 99           LDA     $99,X               ; {ram.m99}
F38E: F0 27           BEQ     $F3B7               ; {}
F390: B5 D8           LDA     $D8,X               ; {ram.mD8}
F392: 95 D6           STA     $D6,X               ; {ram.colorP0}
F394: B5 99           LDA     $99,X               ; {ram.m99}
F396: C9 07           CMP     #$07                
F398: 90 14           BCC     $F3AE               ; {}
F39A: 24 D5           BIT     $D5                 ; {ram.mD5}
F39C: 10 04           BPL     $F3A2               ; {}
F39E: C9 1C           CMP     #$1C                
F3A0: 90 0C           BCC     $F3AE               ; {}
F3A2: C9 30           CMP     #$30                
F3A4: 90 1F           BCC     $F3C5               ; {}
F3A6: C9 37           CMP     #$37                
F3A8: B0 21           BCS     $F3CB               ; {}
F3AA: 24 83           BIT     $83                 ; {ram.m83}
F3AC: 50 1D           BVC     $F3CB               ; {}
F3AE: A9 00           LDA     #$00                
F3B0: 95 99           STA     $99,X               ; {ram.m99}
F3B2: A9 FF           LDA     #$FF                
F3B4: 95 28           STA     $28,X               ; {hard.RESMP0} RESMP1:10,18,19,17 RESMP0:lots
F3B6: 60              RTS                         
F3B7: 24 88           BIT     $88                 ; {ram.m88}
F3B9: 10 04           BPL     $F3BF               ; {}
F3BB: B5 3C           LDA     $3C,X               ; {hard.INPT4} INPT5:9 INPT4:11,12
F3BD: 10 37           BPL     $F3F6               ; {}
F3BF: 20 10 F4        JSR     $F410               ; {}
F3C2: 4C AE F3        JMP     $F3AE               ; {}
F3C5: 20 10 F4        JSR     $F410               ; {}
F3C8: 4C DE F3        JMP     $F3DE               ; {}
F3CB: B5 9F           LDA     $9F,X               ; {ram.m9F}
F3CD: F0 0A           BEQ     $F3D9               ; {}
F3CF: 20 10 F4        JSR     $F410               ; {}
F3D2: A9 30           LDA     #$30                
F3D4: 95 99           STA     $99,X               ; {ram.m99}
F3D6: 4C DE F3        JMP     $F3DE               ; {}
F3D9: B5 99           LDA     $99,X               ; {ram.m99}
F3DB: 20 00 F3        JSR     $F300               ; {}
F3DE: A5 86           LDA     $86                 ; {ram.frameCounter}
F3E0: 29 03           AND     #$03                
F3E2: F0 0C           BEQ     $F3F0               ; {}
F3E4: 24 84           BIT     $84                 ; {ram.m84}
F3E6: 70 0A           BVS     $F3F2               ; {}
F3E8: 24 82           BIT     $82                 ; {ram.skipPlayfield}
F3EA: 50 04           BVC     $F3F0               ; {}
F3EC: 29 01           AND     #$01                
F3EE: D0 02           BNE     $F3F2               ; {}
F3F0: D6 99           DEC     $99,X               ; {ram.m99}
F3F2: A9 00           LDA     #$00                
F3F4: F0 BE           BEQ     $F3B4               ; {}
F3F6: A9 3F           LDA     #$3F                
F3F8: 95 99           STA     $99,X               ; {ram.m99}
F3FA: 38              SEC                         
F3FB: B5 A4           LDA     $A4,X               ; {ram.player0row}
F3FD: E9 06           SBC     #$06                
F3FF: 95 A6           STA     $A6,X               ; {ram.missile0row}
F401: B5 95           LDA     $95,X               ; {ram.m95}
F403: 95 97           STA     $97,X               ; {ram.m97}
F405: A9 1F           LDA     #$1F                
F407: 95 9B           STA     $9B,X               ; {ram.m9B}
F409: A9 00           LDA     #$00                
F40B: 95 9D           STA     $9D,X               ; {ram.m9D}
F40D: 4C CB F3        JMP     $F3CB               ; {}
F410: B5 9F           LDA     $9F,X               ; {ram.m9F}
F412: F0 0D           BEQ     $F421               ; {}
F414: A9 04           LDA     #$04                
F416: 95 15           STA     $15,X               ; {hard.AUDC0}
F418: A9 07           LDA     #$07                
F41A: 95 19           STA     $19,X               ; {hard.AUDV0}
F41C: B5 9B           LDA     $9B,X               ; {ram.m9B}
F41E: 95 17           STA     $17,X               ; {hard.AUDF0}
F420: 60              RTS                         
F421: A4 85           LDY     $85                 ; {ram.m85}
F423: B9 33 F7        LDA     $F733,Y             ; {}
F426: 25 88           AND     $88                 ; {ram.m88}
F428: 95 19           STA     $19,X               ; {hard.AUDV0} AUDV0:13,12,21,19 AUDV1:10,9,18,16
F42A: B9 36 F7        LDA     $F736,Y             ; {}
F42D: 95 15           STA     $15,X               ; {hard.AUDC0} AUDC1:10,9,18,16 AUDC0:13,12,21,19
F42F: 18              CLC                         
F430: A9 00           LDA     #$00                
F432: 88              DEY                         
F433: 30 04           BMI     $F439               ; {}
F435: 69 0C           ADC     #$0C                
F437: 10 F9           BPL     $F432               ; {}
F439: 75 8B           ADC     $8B,X               ; {ram.m8B}
F43B: A8              TAY                         
F43C: 8A              TXA                         
F43D: 0A              ASL     A                   
F43E: 79 39 F7        ADC     $F739,Y             ; {}
F441: 95 17           STA     $17,X               ; {hard.AUDF0} AUDF1:10,9,18,17 AUDF0:lots
F443: 60              RTS                         

; ?? Called from main loop
F444: A2 01           LDX     #$01                ; Start with Player 1 (back again from F504)
F446: B5 30           LDA     $30,X               ; {hard.CXM0P} Collisions between this player's missile and other player
F448: 10 2C           BPL     $F476               ; {} D7 clear -- this player's missile did not hit other player
F44A: 24 84           BIT     $84                 ; {ram.m84}
F44C: 50 06           BVC     $F454               ; {}
F44E: B5 9B           LDA     $9B,X               ; {ram.m9B}
F450: C9 1F           CMP     #$1F                
F452: F0 22           BEQ     $F476               ; {}
F454: F6 95           INC     $95,X               ; {ram.m95}
F456: F6 97           INC     $97,X               ; {ram.m97}
;
F458: F8              SED                         ; BCD mode for 2-digit score
F459: B5 A1           LDA     $A1,X               ; {ram.scoreP1} Player score
F45B: 18              CLC                         ; No carry
F45C: 69 01           ADC     #$01                ; Give 1 point ...
F45E: 95 A1           STA     $A1,X               ; {ram.scoreP1} ... to player
F460: D8              CLD                         ; Out of BCD mode for normal math
;
F461: 8A              TXA                         
F462: 18              CLC                         
F463: 69 FD           ADC     #$FD                
F465: 85 8A           STA     $8A                 ; {ram.m8A}
F467: A9 FF           LDA     #$FF                
F469: 85 28           STA     $28                 ; {hard.RESMP0}
F46B: 85 29           STA     $29                 ; {hard.RESMP1}
F46D: A9 00           LDA     #$00                
F46F: 95 19           STA     $19,X               ; {hard.AUDV0}
F471: 85 99           STA     $99                 ; {ram.m99}
F473: 85 9A           STA     $9A                 ; {ram.m9A}
F475: 60              RTS                         
;
F476: 24 A3           BIT     $A3                 ; {ram.mA3}
F478: 10 03           BPL     $F47D               ; {}
F47A: 4C 01 F5        JMP     $F501               ; {}
F47D: B5 9F           LDA     $9F,X               ; {ram.m9F}
F47F: F0 0A           BEQ     $F48B               ; {}
F481: C9 04           CMP     #$04                
F483: F6 9F           INC     $9F,X               ; {ram.m9F}
F485: 90 04           BCC     $F48B               ; {}
F487: A9 00           LDA     #$00                
F489: 95 9F           STA     $9F,X               ; {ram.m9F}
F48B: B5 34           LDA     $34,X               ; {hard.CXM0FB} Collisions between this player's missile and the playfield
F48D: 30 07           BMI     $F496               ; {} Bit set ... this player's missile hit the playfield
F48F: A9 00           LDA     #$00                
F491: 95 9D           STA     $9D,X               ; {ram.m9D}
F493: 4C D6 F4        JMP     $F4D6               ; {}
;
F496: 24 82           BIT     $82                 ; {ram.skipPlayfield}
F498: 50 36           BVC     $F4D0               ; {}
F49A: B5 9D           LDA     $9D,X               ; {ram.m9D}
F49C: D0 19           BNE     $F4B7               ; {}
F49E: F6 9F           INC     $9F,X               ; {ram.m9F}
F4A0: D6 9B           DEC     $9B,X               ; {ram.m9B}
F4A2: B5 97           LDA     $97,X               ; {ram.m97}
F4A4: 95 B2           STA     $B2,X               ; {ram.mB2}
F4A6: 49 FF           EOR     #$FF                
F4A8: 95 97           STA     $97,X               ; {ram.m97}
F4AA: F6 97           INC     $97,X               ; {ram.m97}
F4AC: B5 97           LDA     $97,X               ; {ram.m97}
F4AE: 29 03           AND     #$03                
F4B0: D0 02           BNE     $F4B4               ; {}
F4B2: F6 97           INC     $97,X               ; {ram.m97}
F4B4: 4C D4 F4        JMP     $F4D4               ; {}
F4B7: C9 01           CMP     #$01                
F4B9: F0 0B           BEQ     $F4C6               ; {}
F4BB: C9 03           CMP     #$03                
F4BD: 90 15           BCC     $F4D4               ; {}
F4BF: D0 13           BNE     $F4D4               ; {}
F4C1: B5 B2           LDA     $B2,X               ; {ram.mB2}
F4C3: 4C C8 F4        JMP     $F4C8               ; {}
F4C6: B5 97           LDA     $97,X               ; {ram.m97}
F4C8: 18              CLC                         
F4C9: 69 08           ADC     #$08                
F4CB: 95 97           STA     $97,X               ; {ram.m97}
F4CD: 4C D4 F4        JMP     $F4D4               ; {}
;
F4D0: A9 01           LDA     #$01                
F4D2: 95 99           STA     $99,X               ; {ram.m99}
F4D4: F6 9D           INC     $9D,X               ; {ram.m9D}
F4D6: B5 32           LDA     $32,X               ; {hard.CXP0FB} Collisions between this player and the playfield
F4D8: 30 04           BMI     $F4DE               ; {} Bit set ... this player hit the playfield
F4DA: A5 37           LDA     $37                 ; {hard.CXPPMM} Collisions between players
F4DC: 10 09           BPL     $F4E7               ; {} Bit is clear ... no collisions
F4DE: A5 8A           LDA     $8A                 ; {ram.m8A}
F4E0: C9 02           CMP     #$02                
F4E2: 90 09           BCC     $F4ED               ; {}
F4E4: 20 08 F5        JSR     $F508               ; {}
F4E7: A9 03           LDA     #$03                
F4E9: 95 E4           STA     $E4,X               ; {ram.mE4}
F4EB: D0 14           BNE     $F501               ; {}
F4ED: D6 E4           DEC     $E4,X               ; {ram.mE4}
F4EF: 30 06           BMI     $F4F7               ; {}
F4F1: B5 8B           LDA     $8B,X               ; {ram.m8B}
F4F3: F0 0C           BEQ     $F501               ; {}
F4F5: D0 02           BNE     $F4F9               ; {}
F4F7: F6 95           INC     $95,X               ; {ram.m95}
F4F9: B5 95           LDA     $95,X               ; {ram.m95}
F4FB: 18              CLC                         
F4FC: 69 08           ADC     #$08                
F4FE: 20 0F F5        JSR     $F50F               ; {}
F501: CA              DEX                         
F502: 30 03           BMI     $F507               ; {}
F504: 4C 46 F4        JMP     $F446               ; {}
F507: 60              RTS                         
F508: 8A              TXA                         
F509: 49 01           EOR     #$01                
F50B: A8              TAY                         
F50C: B9 97 00        LDA     $0097,Y             ; {ram.m97}
F50F: 29 0F           AND     #$0F                
F511: A8              TAY                         
F512: B9 27 F6        LDA     $F627,Y             ; {}
F515: 20 7C F2        JSR     $F27C               ; {}
F518: A9 00           LDA     #$00                
F51A: 95 A8           STA     $A8,X               ; {ram.mA8}
F51C: 95 AA           STA     $AA,X               ; {ram.mAA}
F51E: 95 8D           STA     $8D,X               ; {ram.m8D}
F520: B5 D8           LDA     $D8,X               ; {ram.mD8}
F522: 95 D6           STA     $D6,X               ; {ram.colorP0}
F524: 60              RTS                         

F525: A6 85           LDX     $85                 ; {ram.m85} Player type (0=tank, 1=jet, 2=plane)
F527: BD C6 F7        LDA     $F7C6,X             ; {} Get picture ...
F52A: 85 BB           STA     $BB                 ; {ram.mBB} ... pointer LSB
F52C: BD C9 F7        LDA     $F7C9,X             ; {} Get picture ...
F52F: 85 BC           STA     $BC                 ; {ram.mBC} ... pointer MSB

F531: A5 A3           LDA     $A3                 ; {ram.mA3}
F533: 4A              LSR     A                   
F534: 4A              LSR     A                   
F535: 29 03           AND     #$03                
F537: AA              TAX                         
F538: A5 A3           LDA     $A3                 ; {ram.mA3}
F53A: 10 0A           BPL     $F546               ; {}
F53C: 29 08           AND     #$08                
F53E: F0 04           BEQ     $F544               ; {}
F540: A2 03           LDX     #$03                
F542: 10 04           BPL     $F548               ; {}
F544: A9 80           LDA     #$80                
F546: 85 82           STA     $82                 ; {ram.skipPlayfield}
F548: A5 A3           LDA     $A3                 ; {ram.mA3}
F54A: 0A              ASL     A                   
F54B: 0A              ASL     A                   
F54C: 24 A3           BIT     $A3                 ; {ram.mA3}
F54E: 30 06           BMI     $F556               ; {}
F550: 85 02           STA     $02                 ; {hard.WSYNC} WSYNC:27,10
F552: 85 84           STA     $84                 ; {ram.m84}
F554: 29 80           AND     #$80                
F556: 85 83           STA     $83                 ; {ram.m83}
F558: A9 F7           LDA     #$F7                ; MSB of tables ... F7xx
F55A: 85 B6           STA     $B6                 ; {ram.pf0Graphics+1} For PF0 pointer
F55C: 85 B8           STA     $B8                 ; {ram.pf1Graphics+1} For PF1 pointer
F55E: 85 BA           STA     $BA                 ; {ram.pf2Graphics+1} For PF2 pointer
F560: BD CC F7        LDA     $F7CC,X             ; {} Lookup LSB
F563: 85 10           STA     $10                 ; {hard.RESP0} Set horizontal position of P0
F565: 85 B5           STA     $B5                 ; {ram.pf0Graphics} LSB for PF0 pointer
F567: BD D0 F7        LDA     $F7D0,X             ; {} LSB for ...
F56A: 85 B7           STA     $B7                 ; {ram.pf1Graphics} ... PF1 pointer
F56C: BD D4 F7        LDA     $F7D4,X             ; {} LSB for ...
F56F: 85 B9           STA     $B9                 ; {ram.pf2Graphics} ... PF2 pointer
F571: 60              RTS                         ; Done

; ?? Called from main loop
F572: A5 A3           LDA     $A3                 ; {ram.mA3}
F574: 29 87           AND     #$87                
F576: 30 02           BMI     $F57A               ; {}
F578: A9 00           LDA     #$00                
F57A: 0A              ASL     A                   ; Two bytes each
F57B: AA              TAX                         
F57C: BD 5D F7        LDA     $F75D,X             ; {code.plyrNumSize} Number and size of player 0
F57F: 85 04           STA     $04                 ; {hard.NUSIZ0}
F581: BD 5E F7        LDA     $F75E,X             ; {} Number and size of player 1
F584: 85 05           STA     $05                 ; {hard.NUSIZ1}
F586: A5 A3           LDA     $A3                 ; {ram.mA3}
F588: 29 C0           AND     #$C0                
F58A: 4A              LSR     A                   
F58B: 4A              LSR     A                   
F58C: 4A              LSR     A                   
F58D: 4A              LSR     A                   
F58E: A8              TAY                         
F58F: A5 88           LDA     $88                 ; {ram.m88}
F591: 8D 82 02        STA     $0282               ; {hard.SWCHB}
F594: 49 FF           EOR     #$FF                
F596: 25 DD           AND     $DD                 ; {ram.mDD}
F598: 85 D1           STA     $D1                 ; {ram.mD1}
F59A: A2 FF           LDX     #$FF                
F59C: AD 82 02        LDA     $0282               ; {hard.SWCHB}
F59F: 29 08           AND     #$08                
F5A1: D0 04           BNE     $F5A7               ; {}
F5A3: A0 10           LDY     #$10                
F5A5: A2 0F           LDX     #$0F                
F5A7: 86 D2           STX     $D2                 ; {ram.mD2}
F5A9: A2 03           LDX     #$03                
F5AB: B9 65 F7        LDA     $F765,Y             ; {}
F5AE: 45 D1           EOR     $D1                 ; {ram.mD1}
F5B0: 25 D2           AND     $D2                 ; {ram.mD2}
F5B2: 95 06           STA     $06,X               ; {hard.COLUP0}
F5B4: 95 D6           STA     $D6,X               ; {ram.colorP0}
F5B6: 95 D8           STA     $D8,X               ; {ram.mD8}
F5B8: C8              INY                         
F5B9: CA              DEX                         
F5BA: 10 EF           BPL     $F5AB               ; {}
F5BC: 60              RTS                         
                   
; Clear memory ($A2+X) incrementing X until X=0
; From F007 X=5D to FF (clear 00 through A2)  All registers and variables RAM
; From F16B X=E6 to FF (clear 89 through A2)
; From F1A5 X=DF to FF (clear 82 through A2)  
F5BD: A9 00           LDA     #$00                ; Value 0
F5BF: E8              INX                         ; Next location
F5C0: 95 A2           STA     $A2,X               ; {-} Clear memory
F5C2: D0 FB           BNE     $F5BF               ; {} All done?
F5C4: 60              RTS                         ; No ... back for more

; -----------------------------------------------------------------------------------------------------------------------------
```

# Data Area

All data from here down

## Numbers 

```html
<canvas width="900" height="60"
    data-getTileDataFunction="Stella.get8x5Data"
    data-address="F5C5"
    data-gridX="8"
    data-gridY="5"
    data-command="#TANKPLAYFIELD,0,+x,1,+x,2,+x,3,+x,4,+x,5,+x,6,+x,7,+x,8,+x,9">
</canvas>
```

```code
F5C5: 0E 0A 0A 0A 0E  ;  0
 ; .... ***.
 ; .... *.*.
 ; .... *.*.
 ; .... *.*.
 ; .... ****
  
F5CA: 22 22 22 22 22  ; 11
; ..*. ..*.
; ..*. ..*.
; ..*. ..*.
; ..*. ..*.
; ..*. ..*.
                                  
F5CF: EE 22 EE 88 EE  ; 22
; ***. ***.
; ..*. ..*.
; ***. ***.
; *... *...
; ***. ***.

F5D4: EE 22 66 22 EE  ; 33
; ***. ***.
; ..*. ..*.
; .**. .**.
; ..*. ..*.
; ***. ***.

F5D9: AA AA EE 22 22  ; 44
; *.*. *.*.
; *.*. *.*.
; ***. ***.
; ..*. ..*.
    
F5DE: EE 88 EE 22 EE  ; 55
; ***. ***.
; *... *...
; ***. ***.
; ..*. ..*.
; ***. ***.

F5E3: EE 88 EE AA EE  ; 66
; ***. ***.
; *... *...
; ***. ***.
; *.*. *.*.
; ***. ***.
    
F5E8: EE 22 22 22 22  ; 77
; ***. ***.
; ..*. ..*.
; ..*. ..*.
; ..*. ..*.
; ..*. ..*.
                                  
F5ED: EE AA EE AA EE  ; 88
; ***. ***.
; *.*. *.*.
; ***. ***.
; *.*. *.*.
; ***. ***.

F5F2: EE AA EE 22 EE  ; 99
; ***. ***.
; *.*. *.*.
; ***. ***.
; ..*. ..*.
; ***. ***.    

; ?? From F25E
F5F7: F8
F5F8: F7
F5F9: F6 06
F5FB: 06 06
F5FD: 16 17
F5FF: 18
F600: 19 1A 0A
F603: 0A
F604: 0A
F605: FA
F606: F9 F8 F7
F609: F6 F6
F60B: 06 16
F60D: 16 17

; ??
               
F60F: 18 19 1A 1A 0A FA FA F9 
F617: E8 E6 E4 F4 04 14 24 26
F61F: 28 2A 2C 1C 0C FC EC EA 
F627: C8 C4 C0 E0 00 20 40 44
F62F: 48 4C 4F 2F 0F EF CF CC
F637: 00 00 80 80 84 20 88 88
F63F: 92 48 A4 A4 A9 52 AA AA
F647: D5 AA DA DA DB 6D EE EE
```

## Tank Pictures 

```html
<canvas width="1000" height="100"
    data-getTileDataFunction="Stella.get8x8Data"
    data-address="F64F"
    data-gridX="8"
    data-gridY="8"
    data-command="#TANKP0,0,+x,1,+x,2,+x,3,+x,4,+x,5,+x,6,+x,7">
</canvas>
```

```code
F64F: 00 FC FC 38 3F 38 FC FC
F657: 1C 78 FB 7C 1C 1F 3E 18 
F65F: 19 3A 7C FF DF 0E 1C 18
F667: 24 64 79 FF FF 4E 0E 04
F66F: 08 08 6B 7F 7F 7F 63 63
F677: 24 26 9E FF FF 72 70 20
F67F: 98 5C 3E FF FB 70 38 18
F687: 38 1E DF 3E 38 F8 7C 18
```

## Jet Pictures 

```html
<canvas width="1000" height="100"
    data-getTileDataFunction="Stella.get8x8Data"
    data-address="F68F"
    data-gridX="8"
    data-gridY="8"
    data-command="#JETP0,0,+x,1,+x,2,+x,3,+x,4,+x,5,+x,6,+x,7">
</canvas>
```

```code                 
F68F: 60 70 78 FF 78 70 60 00
F697: 00 C1 FE 7C 78 30 30 30
F69F: 00 03 06 FC FC 3C 0C 0C
F6A7: 02 04 0C 1C FC FC 1E 06
F6AF: 10 10 10 38 7C FE FE 10
F6B7: 40 20 30 38 3F 3F 78 60
F6BF: 40 60 3F 1F 1E 1E 18 18
F6C7: 00 83 7F 3E 1E 0C 0C 0C
```

## Plane Pictures 

```html
<canvas width="1000" height="100"
    data-getTileDataFunction="Stella.get8x8Data"
    data-address="F6CF"
    data-gridX="8"
    data-gridY="8"
    data-command="#PLANEP0,0,+x,1,+x,2,+x,3,+x,4,+x,5,+x,6,+x,7">
</canvas>
```

```code        
F6CF: 00 8E 84 FF FF 04 0E 00
F6D7: 00 0E 04 8F 7F 72 07 00        
F6DF: 10 36 2E 0C 1F B2 E0 40
F6E7: 24 2C 5D 1A 1A 30 F0 60
F6EF: 18 5A 7E 5A 18 18 18 78
F6F7: 34 36 5A 78 2C 0C 06 0C
F6FF: 08 6C 70 B8 DC 4E 07 06
F707: 38 10 F0 7C 4F E3 02 00
        
; ?? From F324 guidance for 0=tanks, 1=jets, 2=planes
F70F: 00 0B 16 

; ?? From F32B guides the tanks in pre-game
F712: 00
F713: 10 00
F715: FF
F716: 01 11 ; There are more tank levels than others. is this why there are more in this table??
F718: 01 FF
F71A: 0F
F71B: 1F
F71C: 0F
; ?? guides jets in pre-game
F71D: 50 5F
F71F: 51 FF
F721: 30
F722: 3F
F723: 31 FF
F725: 70 7F
F727: 71 90
F729: B0 70
F72B: FF
F72C: 91 B1
F72E: 71 FF
F730: 9F
F731: BF
F732: 7F

; ?? From F423
F733: 08 02 02

; ?? From F42A
F736: 02
F737: 03
F738: 08

; ?? From F43E
F739: 1D 05 00
F73C: 00
F73D: 00
F73E: 00
F73F: 00
F740: 00
F741: 00
F742: 00
F743: 00
F744: 00
F745: 00
F746: 00
F747: 1D 1D 16
F74A: 16 0F
F74C: 0F                                    
F74D: 00                      
F74E: 00                      
F74F: 00                     
F750: 00                       
F751: 00                      
F752: 00                     
F753: 00                    
F754: 00                     
F755: 00                     
F756: 12                                    
F757: 10 10
F759: 0C                                    
F75A: 0C                                    
F75B: 07                                    
F75C: 07                                    

plyrNumSize:
; Number/size of players, width of missile
;                    copies    width            copies    width
F75D: 00 00   ; P0 = 1         1           P1 = 1         1         
F75F: 01 01   ; P0 = 2 close   1           P1 = 2 close   1        
F761: 00 03   ; P0 = 1         1           P1 = 3 close   1                                    
F763: 27 03   ; P0 = 1 quad    4           P1 = 3 close   1                         
    
; ?? Colors from F5AB    
F765: EA 3C 
F767: 82                                    
F768: 44                                    
F769: 32                                    
F76A: 2C 8A DA
F76D: 80                                    
F76E: 9C                                    
F76F: DA                                    
F770: 3A                                    
F771: 64                                    
F772: A8                
F773: DA                                    
F774: 4A         
F775: 08 04 00 0E     

; There are 4 play field patterns
; - Empty tank field
; - Simple tank field
; - Complex tank field
; - Clouds
; The empty-air-field is just no playfield at all

; Each pattern has three tables of 12 bytes. Each pattern is used over 8 rows.
; 12*2*8 = 192 rows of the playfield

; 12 bytes each mirrored left, right, top, bottom

; PF0 for all tank levels
F779: F0 10 10 10 10 10 10 10 10 10 10 10

; PF1 for complex tanks 
F785: FF 00 00 00 38 00 00 00 60 20 20 23

; PF2 for complex tanks 
F791: FF 80 80 00 00 00 1C 04 00 00 00 00

; PF1 and PF2 for blank tanks (vertical line)        
F79D: FF

; PF0 for air (all off) 
F79E: 00 00 00 

; PF1 and PF2 for air
F7A1: 00 00 00 00 00 00 00 00 00 07 1F 3F 

; If you start the clouds PF1 and PF2 at F7A2 then this makes a fatter cloud!
; You could also back up for smaller clouds. I bet the larger cloud was
; intended for a second air playfield ... different for planes and jets.
; Maybe they ran out of code space to use it. 

F7AD: 7F 

; PF1 for simple tanks
F7AE: FF 00 00 00 00 00 00 00 00 60 20 21

; PF2 for simple tanks 
F7BA: FF 00 00 00 80 80 80 80 00 00 00 07

; Pointers to player pictures 0=tank, 1=jet, 2=plane  
PlayerPicLSB:                                  
F7C6: 4F CF 8F ; Picture pointers LSB                                  

PlayerPicMSB:
F7C9: F6 F6 F6 ; Picture pointers MSB

; Four different play fields
; F779, F785, F791  ' Complex tanks
; F779, F79D, F79D  ' Blank tanks
; F779, F7AE, F7BA  ' Simple tanks
; F79E, F7A1, F7A1  ' Clouds

;      0  1  2  3
F7CC: 75 75 75 9A  ; PF0 LSB (add 4 the drawing loop treats this as entries 4 through 16 (1)
F7D0: 81 99 AA 9D  ; PF1 LSB (add 4)
F7D4: 8D 99 B6 9D  ; PF2 LSB (add 4)
```

## Playfields 

```html
<canvas width="410" height="250"
        data-getTileDataFunction="Combat.getPlayfield"
        data-pixWidth="20"
        data-pixHeight="20"
        data-gap="0.5"
        data-gridPad="2"
        data-gridX="20"
        data-gridY="12"
        data-command="#TANKPLAYFIELD,0">
</canvas> 
<canvas width="325" height="250"
        data-getTileDataFunction="Combat.getPlayfield"
        data-pixWidth="8"
        data-pixHeight="8"
        data-gap="0.25"
        data-gridPad="1"
        data-gridX="20"
        data-gridY="12"
        data-command="#TANKPLAYFIELD,0,H0,*,V0,VH0">
</canvas><br>
```

```html
<canvas width="410" height="250"
        data-getTileDataFunction="Combat.getPlayfield"
        data-pixWidth="20"
        data-pixHeight="20"
        data-gap="0.5"
        data-gridPad="2"
        data-gridX="20"
        data-gridY="12"
        data-command="#TANKPLAYFIELD,1">
</canvas> 
<canvas width="325" height="250"
        data-getTileDataFunction="Combat.getPlayfield"
        data-pixWidth="8"
        data-pixHeight="8"
        data-gap="0.25"
        data-gridPad="1"
        data-gridX="20"
        data-gridY="12"
        data-command="#TANKPLAYFIELD,1,H1,*,V1,VH1">
</canvas><br> 
```

```html
<canvas width="410" height="250"
        data-getTileDataFunction="Combat.getPlayfield"
        data-pixWidth="20"
        data-pixHeight="20"
        data-gap="0.5"
        data-gridPad="2"
        data-gridX="20"
        data-gridY="12"
        data-command="#TANKPLAYFIELD,2">
</canvas> 
<canvas width="325" height="250"
        data-getTileDataFunction="Combat.getPlayfield"
        data-pixWidth="8"
        data-pixHeight="8"
        data-gap="0.25"
        data-gridPad="1"
        data-gridX="20"
        data-gridY="12"
        data-command="#TANKPLAYFIELD,2,H2,*,V2,VH2">
</canvas><br> 
```

```html
<canvas width="410" height="250"
        data-getTileDataFunction="Combat.getPlayfield"
        data-pixWidth="20"
        data-pixHeight="20"
        data-gap="0.5"
        data-gridPad="2"
        data-gridX="20"
        data-gridY="12"
        data-command="#PLANEPLAYFIELD,3">
</canvas> 
<canvas width="325" height="250"
        data-getTileDataFunction="Combat.getPlayfield"
        data-pixWidth="8"
        data-pixHeight="8"
        data-gap="0.25"
        data-gridPad="1"
        data-gridX="20"
        data-gridY="12"
        data-command="#PLANEPLAYFIELD,3,H3,*,V3,VH3">
</canvas><br> 
```

```code
; ?? From F1AE
F7D8: 24 28
F7DA: 08
F7DB: 20 00 48
F7DE: 40
F7DF: 54                                    
F7E0: 58
F7E1: 25 29
F7E3: 49 55
F7E5: 59 A8 88
F7E8: 98
F7E9: 90 A1
F7EB: 83                                    
F7EC: E8  
F7ED: C8
F7EE: E0 C0
F7F0: E9 E2
F7F2: C1 FF
             
F7F4: 00 00 00 00 00 00 
```

# Vectors

```code
F7FA: 00 00        ; NMI Vector (not used)
F7FC: 00 F0        ; Reset vector to F000
F7FE: 0F 11        ; IRQ/vector to 110F (maybe debug hardware?)
```

```html
<script src="Combat.js"></script>
<script src="../Stella.js"></script>
<script src="/js/Binary.js"></script>
<script>
    window.onload = function() {   
        Stella.data = Binary.readBinary('Code.md.bin') 
	Stella.origin = 0xF000 
        Canvas.redrawGraphics()       
    }            
</script>
<script src="/js/TileEngine.js"></script>
<script src="/js/Canvas.js"></script>
```

