![Journal](../../img/journal.jpg)

# Journal

# Questions to answer in the dig

## 7/16/2026

## Why the padding before certain routines to land them on nice addresses?

Both things I found confirm the answer. There are really two distinct kinds of "landing on a nice address" in the Phoenix ROM, and they exist for different reasons.

## 1. Code routines padded up to round entry points

You see gaps like these right before subroutines:

```
123:130:(computerarcheology Phoenix disassembly)
; not used
004C: FF FF FF FF
...
InitSoundScreen:
0050: 26 68  LD  H,$68        ; entry lands on $0050
```

```
564:571:(computerarcheology Phoenix disassembly)
0252: C9  RET
0253: FF FF FF FF FF
...
CompareBCtoMem:
0258: 7E  LD  A,(HL)          ; entry lands on $0258
```

```
588:595:(computerarcheology Phoenix disassembly)
0267: C9  RET
0268: FF FF FF FF FF FF FF FF
...
SubtractFromMemory:
0270: 7E  LD  A,(HL)          ; entry lands on $0270
```

`$0050`, `$0258`, `$0270` — clean multiples of 8/16. A few important points about these:

- The filler is `$FF`, not `$00`. `$FF` is an *erased/unprogrammed* EPROM cell. So these aren't `NOP` instructions the CPU runs through — they're simply address space the assembler skipped over (via `ORG`/`DS`), leaving the ROM blank there.

- The real reason is absolute addressing. The Z80's `CALL`/`JP` encode a fixed 16 bit target. Every reference to a routine hard codes its entry address. If a routine were placed immediately after the previous one, then editing/growing any early routine would shove everything after it downward and break *every* absolute `CALL`/`JP` to those later routines. By giving each routine a fixed, hand chosen entry address with slack after it, a routine can be rewritten or grown in a later revision without relocating anything downstream — all the hardcoded addresses stay valid.

- The "ghost code bytes from an older version" comments are the proof. Those leftover bytes and the `FF` gaps are what remains after routines were *shortened* across revisions. The slack was there deliberately; later edits made routines smaller, exposing the padding. Round entry points also just made the code far easier to remember, document, and patch by hand during development.

## 2. Data tables aligned so they sit inside one 256 byte page

The second kind of alignment is for lookup tables, and it's driven by a pervasive optimization: the code loads the table's high byte once as an immediate and then indexes using only the low byte:

```
1309:1667:(computerarcheology Phoenix disassembly)
061F: 26 15  LD  H,$15   ; MSB for T1540-T15E0
0731: 26 07  LD  H,$07   ; MSB for jump table
0790: 26 14  LD  H,$14   ; T14xx alien character block shapes table
0D3F: 26 17  LD  H,$17   ; MSB for movement direction table (T1700)
```

This `LD H,$xx` + compute `L` pattern (used for `T1740`, `T17B0`, `T1C00`, `T1D00`, `T1E00/20/40`, `T2800/2900`, `T3F00`, the jump tables, etc.) is only correct if the whole table lives within that single `$xx00`–`$xxFF` page. If the table straddled a page boundary, incrementing `L` would wrap back to the start of the page instead of moving to the next page — a bug. So those tables are padded to start on (or fit within) a page boundary. That guarantees `H` never has to change while walking the table, which is smaller and faster than carrying 16‑bit pointer arithmetic.

## Summary

- The `$FF` gaps before routines are blank EPROM left by `ORG`/`DS` placement, not executed padding.
- Code is placed at fixed round addresses with slack because Z80 `CALL`/`JP` are absolute — fixed entry points + headroom let routines be edited across revisions without breaking every downstream reference (and the "ghost bytes" show exactly that history).
- Data tables are page aligned so the code can use the "constant MSB" trick — set `H` once, index with `L` only — which requires the table not to cross a `$xx00` page boundary.

## How does the two player mode work?

Phoenix runs two players on one machine by keeping two complete banks of work RAM, selected by the video bank hardware register at `$5000`.
"Changing the player" means copying the whole game context from one bank into the other and leaving `$5000` pointed at the new bank. Here's how it works.

## The state that identifies the player

- `GameOrAttract` (`$43A2`) — `1` = one player mode (switching is skipped entirely).
- `GameAndDemoOrSplash` (`$43A3`) — the "who is playing now" flag: `0` = player 1, `1` = player 2, `2` = intro splash.
- `Player1Lives` (`$4390`) / `Player2Lives` (`$4391`) — separate life counts.
- `Score1` (`$4380`–`$4383`) / `Score2` (`$4384`–`$4387`) — separate BCD scores, drawn to opposite corners of the top rows:

```
755:762:(computerarcheology Phoenix disassembly)
033A: 2E 83     LD L,$83        ; print player 1 score
033C: 11 61 42  LD DE,$4261     ; Score1 screen coordinates
033F: 06 06     LD B,$06
0341: CD C4 00  CALL PrintNumber
0344: 2E 87     LD L,$87        ; print player 2 score
0346: 11 21 40  LD DE,$4021     ; Score2 screen coordinates
```

## The actual switch — bank copy via `$5000`

The switch is performed by `CopyMemoryBank` (`$0460`). `B` = source bank, `C` = destination bank.
For every byte it writes the source bank to `$5000`, reads the byte,
writes the destination bank to `$5000`, and stores the byte — moving the data across the two hardware banks:

```
999:1043:(computerarcheology Phoenix disassembly)
CopyMemoryBank:
0460: 21 00 50  LD HL,$5000     ; video/RAM bank-select register
0463: 11 20 43  LD DE,ForegroundScreen+320
L0466:
0466: 70        LD (HL),B       ; select SOURCE bank
0467: 1A        LD A,(DE)       ; read byte from source bank
0468: 71        LD (HL),C       ; select DEST bank
0469: 12        LD (DE),A       ; write byte to dest bank
... (walks the whole visible screen from $4320 down) ...
0481: 11 80 43  LD DE,M4380     ; then the state/score block...
... (copies $4380-$43B7) ...
048F: 11 C0 4B  LD DE,B4BC0     ; then the object buffer...
... (copies $4BC0-$4BFF) ...
049D: C9        RET
```

So three regions are transferred:
1. the visible playfield/scoreboard (from `$4320`, i.e. the whole foreground screen),
2. the game state + score block `$4380`–`$43B7` (scores, level/round, counters),
3. the object buffer `$4BC0`–`$4BFF`.

When it returns, `$5000` is left holding the destination bank, so that player's screen is now the one being displayed.

## When and which direction

The handover happens in game state 0 ("new game start" / new turn processing), `L0430`.
It first bails out for splash and for one player mode, then routes to the correct direction:

```
971:990:(computerarcheology Phoenix disassembly)
043D: FE 02     CP $02
043F: C8        RET Z           ; was intro splash -> nothing
0440: 77        LD (HL),A
0442: 7E        LD A,(HL)       ; GameOrAttract
0443: FE 01     CP $01
0445: C8        RET Z           ; one-player mode -> no switch
0447: 7E        LD A,(HL)       ; GameAndDemoOrSplash
0449: CA A0 04  JP Z,L04A0      ; currently player 1 -> switch to player 2
044C: 2E 90     LD L,$90
044E: 7E        LD A,(HL)       ; else currently player 2: check Player1Lives
0450: C8        RET Z           ; player 1 has no lives -> don't switch back
0453: 36 00     LD (HL),$00     ; $43A3 = 0  (player 1)
0455: 01 00 01  LD BC,$0100     ; bank 1 -> bank 0
0458: CD 60 04  CALL CopyMemoryBank
```

And the player 1->player 2 direction:

```
1050:1055:(computerarcheology Phoenix disassembly)
L04A0:
04A0: 2E A3     LD L,$A3
04A2: 36 01     LD (HL),$01     ; $43A3 = 1  (player 2)
04A4: 01 01 00  LD BC,$0001     ; bank 0 -> bank 1
04A7: CD 60 04  CALL CopyMemoryBank
```

So:
- Player 1 -> Player 2: set `$43A3 = 1`, `CopyMemoryBank(bank 0 -> bank 1)`; `$5000` ends on bank 1 (player 2's screen).
- Player 2 -> Player 1: set `$43A3 = 0`, `CopyMemoryBank(bank 1 -> bank 0)`; `$5000` ends on bank 0 (player 1's screen) 
   — but only if `Player1Lives ≠ 0`, otherwise player 1 is out and no switch occurs.

Player 1 therefore always lives in bank 0 and player 2 in bank 1;
the copy carries each player's in progress world (their partly cleared wave, ship position, level, counters)
plus the shared scoreboard into the bank that is about to become active.

## The rest of state 1 (score flash) keys off the same flag

While the just ended player's score flashes (game state 1, `L04AC`),
the code reads `GameAndDemoOrSplash` to decide which score/screen area to flash/redraw — player 1 at `$4261`, player 2 at `$4021`:

```
1082:1089:(computerarcheology Phoenix disassembly)
04CD: 21 A3 43  LD HL,GameAndDemoOrSplash
04D0: 7E        LD A,(HL)
04D1: A7        AND A
04D2: 2E 83     LD L,$83        ; player 1 score
04D4: 11 61 42  LD DE,$4261
04D7: CA DF 04  JP Z,L04DF
04DA: 2E 87     LD L,$87        ; player 2 score
04DC: 11 21 40  LD DE,$4021     ; player 2 screen area
```

## Summary

- Two player mode uses two RAM/video banks selected by the register at `$5000`; player 1 = bank 0, player 2 = bank 1.
- The current player is tracked by `GameAndDemoOrSplash` (`$43A3`) (0/1), with `GameOrAttract` (`$43A2`) marking one‑player mode.
- At each turn boundary (game state 0, `L0430`) the game flips `$43A3` and calls `CopyMemoryBank`,
  which transfers the visible screen, the `$4380`–`$43B7` state/score block,
  and the `$4BC0`–`$4BFF` object buffer between banks by toggling `$5000` per byte, ending with `$5000` on the incoming player's bank.
- Separate `Player1Lives`/`Player2Lives` and `Score1`/`Score2` persist across turns; a player is skipped once their lives hit 0.

## How does the call-stack work when RAM banks are changed?

Great question — it works because the stack itself lives in the banked RAM, and the switch routine is written specifically to keep it valid across the bank change. Here's the full picture.

## 1. The stack is inside the banked RAM window

At boot the stack pointer is set to the very top of the `$4000`–`$4BFF` RAM, and the RAM bank is selected through bit 0 of the `$5000` register:

```
84:86:(computerarcheology Phoenix disassembly)
0008: 31 FF 4B  LD   SP,$4BFF        ; Top-ish of RAM (stack grows downward from here)
...
000D: 36 00     LD   (HL),$00        ; ($5000) Select the first bank of RAM
```

The whole `$4000`–`$4BFF` region — screen memory *and* the stack — is one bank switched block. The clue is right there in `ClearRAMBank`, whose own header explains why it stops short of the top:

```
145:153:(computerarcheology Phoenix disassembly)
;* Clear a RAM Bank (bank 0 or 1)
;* Set the lower bit of the video register to pick the bank before calling.
;* 4000 - 4BF8
;* We call this function, which means we don't want to clear the return on the stack.
;* That's why we start clearing at 4BF8 instead of 4BFF.
;* Since screen memory is part of this bank, we are clearing the screen too.
006B: 21 F8 4B  LD   HL,$4BF8        ; Highest point ... skip the top of the stack
```

So each bank (0 and 1) has its own physical stack at `$4BF0`–`$4BFF`. Boot even clears both banks separately, selecting bank 0, clearing it (stopping at `$4BF8` so the live return address survives), then selecting bank 1 and clearing that one too.

## 2. During a turn: nothing special happens

While a single player is playing, the bank bit never changes. Every `CALL`/`RET`/`PUSH`/`POP` hits that bank's stack consistently, exactly like a normal machine. The banking is invisible to ordinary code.

## 3. The only bank change is "CopyMemoryBank", and it protects the stack

The bank bit is toggled for gameplay in exactly one place — `CopyMemoryBank` (the two player switch). The trick is that it copies the stack from the old bank into the new bank before returning, and touches nothing stack related in between:

- `CopyMemoryBank` is reached by a `CALL`, so the return address is sitting on the source bank's stack (`$4BFx`), and `SP` points at it.
- Its final region copy transfers `$4BC0`–`$4BFF` — which includes the entire stack area `$4BF0`–`$4BFF` — from the source bank (`B`) to the destination bank (`C`):

```
1032:1043:(computerarcheology Phoenix disassembly)
048F: 11 C0 4B  LD   DE,B4BC0        ; object buffer ... and the stack live up here
L0492:
0492: 70        LD   (HL),B          ; select source bank
0493: 1A        LD   A,(DE)          ; read byte from source bank
0494: 71        LD   (HL),C          ; select destination bank
0495: 12        LD   (DE),A          ; write byte to destination bank
0496: 1C        INC  E
0497: 7B        LD   A,E
0498: FE 00     CP   $00             ; ...through $4BFF (covers $4BF0-$4BFF = the stack)
049A: C2 92 04  JP   NZ,L0492
049D: C9        RET                  ; $5000 now = C: return via the freshly-copied stack
```

- Crucially, `CopyMemoryBank`'s loops use only jumps (`JP`, plus `LD`/`INC`/`DEC`/`CP`) — there are no `CALL`/`PUSH`/`POP` anywhere inside it. So `SP` and the stack contents do not change between the moment the stack is copied and the final `RET`.
- The routine leaves `$5000` holding `C` (the destination bank). The closing `RET` therefore pops the return address from the destination bank's stack — which is a byte for byte copy of what was on the source stack, so it's the correct address.

Because the copy duplicates the *whole* `$4BF0`–`$4BFF` region, it isn't just the immediate return address that survives — the entire pending call chain (every return address currently on the stack) is mirrored into the new bank, so unwinding continues to work all the way back up.

## 4. Why it doesn't corrupt

Put together, the invariants that make it safe are:

1. Stacks are kept in sync at the switch point — the destination bank's stack is overwritten with the source bank's stack as the last step, so `SP` is meaningful in both banks.
2. No stack operations occur after the bank flips — the routine is deliberately branch‑only, so `SP` is stable from the copy through the `RET`.
3. `$5000` ends on the destination bank, so the `RET` (and everything after) runs against the just synchronized stack.

## Summary

- `$4BF0`–`$4BFF` is part of the bank switched `$4000`–`$4BFF` RAM, so each bank has its own stack (confirmed by `SP=$4BFF` and by `ClearRAMBank` skipping `$4BF8`+ to avoid wiping the live return address).
- Ordinary code never notices, because the bank only changes inside `CopyMemoryBank`.
- `CopyMemoryBank` survives the change because it copies the stack region (`$4BC0`–`$4BFF`) into the destination bank, performs no stack operations after switching, and returns with `$5000` pointing at that destination bank — so the `RET` (and the whole return chain) reads a valid, freshly copied stack.

## What happens when aliens leave the visible area of the screen?

I now have the full mechanism. The key is the coordinate system plus the screen-address lookup — let me lay it out.

## Aliens have logical coordinates that are independent of the screen

Every alien slot in the `$4B70` structure holds a single‑byte X grid coordinate and a single‑byte Y grid coordinate. Movement is nothing more than repeatedly *adding* signed increments to those bytes, taken from the movement choreography (`T1000` -> `T1700`):

```
2733:2748:(computerarcheology Phoenix disassembly)
0D4B: 2B        DEC  HL              ; value for X movement
0D4C: 0A        LD   A,(BC)          ; get alien screen coordinate X
0D4D: 86        ADD  A,(HL)          ; add the X delta from T1700
0D4E: 02        LD   (BC),A          ; save it back
L0D4F:
0D4F: 03        INC  BC              ; -> Y coordinate
0D50: 23        INC  HL
0D51: 0A        LD   A,(BC)          ; get alien screen coordinate Y
0D52: 86        ADD  A,(HL)          ; add the Y delta
0D53: 02        LD   (BC),A          ; save it back
```

There is no clamping and no edge test here. The coordinates are 8 bit, so they simply wrap modulo 256 (`$FF + 1 -> $00`). The only "border" check (`AND $07`) just detects when the alien has crossed a whole character cell so the pattern can step to its next entry — it has nothing to do with the screen edge. So logically an alien keeps moving forever along its pattern, on screen or not.

## The screen edge lives entirely in the coordinate -> address lookup

An alien is only *shown* when its coordinate is translated into a screen RAM address by `GetScreenRamAddress`. That routine takes the X coordinate, drops the sub cell pixel bits, and uses `X >> 3` (the column number) as an index into the `T0A00` address table:

```
2131:2150:(computerarcheology Phoenix disassembly)
09BA: 21 00 0A  LD  HL,T0A00     ; Screen ram addresses for the top row
09BD: 0A        LD  A,(BC)       ; get the X coordinate
09BE: E6 F8     AND $F8          ; drop the low 3 (sub-cell) bits
09C0: 0F        RRCA
09C1: 0F        RRCA             ; A = column * 2  (2-byte entries)
09C2: 85        ADD A,L
09C3: 6F        LD  L,A          ; HL = T0A00 + column*2
09C4: 7E        LD  A,(HL)       ; MSB of that column's screen address
...
09CF: 86        ADD A,(HL)       ; LSB += (Y >> 3)  -> row within the column
```

`T0A00` only has 26 real entries — columns 0–25, the visible width of the (rotated) playfield:

```
2158:2192:(computerarcheology Phoenix disassembly)
T0A00:
0A00: 43 20 ; column 0  (upper-left corner)
...
0A32: 40 00 ; column 25 (upper-right corner)
; Mapping the 'out of screen' objects
0A34: 00 00
0A36: 00 00
0A38: 00 00
0A3A: 00 00
0A3C: 00 00
0A3E: 00 00
```

## What actually happens off-screen

Because `column = X >> 3`, a byte X can address columns 0–31. Columns 0–25 are visible; columns 26–31 (X ≥ `$D0`) fall into the six `00 00` entries at `$0A34`–`$0A3F`. So for an off screen alien, `GetScreenRamAddress` returns address `$00xx` — the bottom of ROM.

That's the whole trick:

- Drawing/erasing an off-screen alien writes to `$00xx`, which is ROM. Writes to ROM do nothing, so the alien silently vanishes — no corruption, no wraparound garbage on the opposite edge.
- The alien's logical coordinate keeps advancing (and wrapping mod 256) the entire time it's off-screen, because movement is decoupled from rendering.
- When the coordinate comes back into columns 0–25, the lookup returns a real screen address again and the alien reappears seamlessly at the correct spot. Its "old address" (used for erasing) was also `$0000` while off-screen, so the erase step is equally harmless.

Collision detection uses these same screen addresses/coordinates, so an off-screen alien can neither be hit by the player's bullet nor collide with the ship while it's parked in the `$00xx` region — consistent with it being invisible.

## Two layers of movement

- Formation aliens all share one looping choreography: the movement list pointer (`T4B50`) walks `T1000`, which indexes the X/Y delta pairs in `T1700`; when the list hits its end marker, `L0DDE` resets it to the start. That pattern is what sweeps the block side to side and down — it's authored so the formation turns around near the edges rather than actually running off.
- Diving / flying aliens run their own patterns and *do* routinely swing past the edges; those are the ones that exploit the `$0000` off screen mapping to disappear on one side and re‑enter later.

## Summary

Aliens move by accumulating signed X/Y deltas into 8‑bit coordinates that wrap mod 256 and are never clamped. "Leaving the screen" isn't handled by the movement code at all — it's handled by `GetScreenRamAddress`, whose `T0A00` table only maps the 26 visible columns and sends columns 26–31 to the six `$0000` "out‑of‑screen" entries. Off screen aliens therefore draw/erase to harmless ROM (invisible), keep updating their position, and pop back into view unchanged once their coordinate re enters the visible range.

## How does the JP (HL) at $0EE5 work?

This is a hand rolled non local return (a "longjmp" style stack unwind), not an offset calculation at all. Here's exactly what's going on.

## The three instructions

```
3063:3066:(computerarcheology Phoenix disassembly)
0EE2: 35        DEC  (HL)            ; AliensLeft--
0EE3: E1        POP  HL              ; discard one return address
0EE4: E1        POP  HL              ; pop the NEXT return address into HL
0EE5: E9        JP   (HL)            ; jump to it -> $0DF9, $0027, $2199, $2006
```

This is the tail of the shared "enemy destroyed" routine (`L0EA4`/`L0EAD`). By the time execution gets here the alien has been cleared, the explosion slot filled, the "enemy hit" flag set, and `AliensLeft` decremented.

There is no computed offset. `JP (HL)` jumps to whatever address is in `HL`, and `HL` is filled by `POP` — i.e. it is taken straight off the Z80 call stack. The two `POP HL` instructions throw away two levels of nested `CALL` return addresses, and the second popped value becomes the jump target. So the destination is decided *dynamically* by how the collision code was entered — which is why the disassembler lists four possibilities.

## Why exactly two POPs — a stack trace

The destroy tail is always reached from inside a per alien scanning loop, which is itself inside a collision entry routine. Take an in formation alien hit by the first player bullet:

```
$2003: CALL L0DF0        ; push $2006   (dispatcher return)
  $0DF6: CALL L0E10      ; push $0DF9   (continuation in L0DF0)
    $0E83: CALL NZ,L0E90 ; push $0E86   (per-alien scan loop in L0E70)
      L0E90 hit -> falls into L0EA4/L0EAD -> $0EE3
```

Stack at `$0EE3` (top -> bottom): `$0E86`, `$0DF9`, `$2006`.

- `POP HL` → `$0E86` discarded — abandons the alien scan loop (we must *not* keep iterating the alien array we just modified, or we could double‑hit).
- `POP HL` → `$0DF9` — this becomes the target.
- `JP (HL)` → `$0DF9`, which is the instruction right after `CALL L0E10` in `L0DF0`, i.e. it goes on to run the second bullet's collision check. `$2006` stays on the stack for later.

## Why the target varies (the four listed addresses)

The trick is that the second collision pass is entered by a `JP`, not a `CALL`:

```
2882:2882:(computerarcheology Phoenix disassembly)
0DFF: C3 10 0E  JP  L0E10           ; second bullet check - no return pushed
```

So depending on the entry path there is one fewer frame on the stack, and the second `POP` lands on a different address:

| Situation | 1st POP discards | 2nd POP -> `JP (HL)` |
|---|---|---|
| 1st bullet destroys an alien (entered `L0E10` via `CALL`) | scan loop return (`$0E86`/`$0E4D`) | `$0DF9` — go do the 2nd bullet check |
| 2nd bullet destroys an alien (entered `L0E10` via `JP`) | scan loop return | `$2006` — return to the frame dispatcher after `CALL L0DF0` (`$2003`) |
| Alien touches ship (`L0F00`, entered via `CALL` at `$2196`) | scan loop return (`$0F2B`) | `$2199` — return to the dispatcher after `CALL L0F00` |
| Same pattern in the top level update chain | scan loop return | `$0027` — return in the main game‑update sequence |

I verified those call sites in the ROM:

```
101:102:(computerarcheology Phoenix disassembly)
0024: CD 00 04  CALL GameStateMachine     ; return = $0027
0027: CD 00 27  CALL UpdateScoresAndSound
```

```
4310:4310:(computerarcheology Phoenix disassembly)
2003: CD F0 0D  CALL L0DF0                 ; return = $2006
```

```
4590:4591:(computerarcheology Phoenix disassembly)
2196: CD 00 0F  CALL L0F00                 ; return = $2199
2199: CD 60 25  CALL L2560
```

## Summary

- `$0EE3`–`$0EE5` = `POP HL` / `POP HL` / `JP (HL)`.
- It gets its target from the call stack, not from any offset: it pops two saved return addresses and jumps to the second one.
- The first `POP` deliberately unwinds out of the inner alien scanning loop (so the loop doesn't keep running over an array that just changed); the second `POP` yields the point where the game should resume.
- That resume point is `$0DF9`, `$2006`, `$2199`, or `$0027` depending on which collision entry path (and which of `CALL`/`JP`) led into the shared destroy routine. It's essentially a structured exception style early exit implemented by manual stack popping.

## 6/5/2024

I got an awesome merge request from Peter (Sorbas2020 on github). He added lots of comments and data disassembly.

## 6/2/2023 

I did a little decoding of the first part of the ROM. It contains general purpose functions like 2-bit adds/subtracts
and 6-digit BCD math for the scores. There is a 6-digit BCD subtract, but it is never called. A score never
goes down.

I commented the "wait for VBLANK and handle coins" code. Too funny: the code only counts up to 9 coins. Any coins
that are put in after that are not counted. There are two digits on the screen for coins, but the code doesn't
handle two digits.

## 6/1/2023

I got the web site graphics working. You can switch between the two color pallettes with the click of a button.

I looked at the Mame video driver. The cocktail screen flip is tied to the RAM bank selected. If the coctail switch
is set, then switching to the second back automatically flips the screen. That's a sure tell that the banks are for
different players. But now I wonder how the stack works with bank flips.

Two byte values are referenced by pointers to the second (LSB). The code subtracts one to get to the MSB.

## 5/27/2023

I'm following the startup sequence. That should initialize the hardware and clear the screen.

There is a routine at 0x006B that clears a large chunk of memory from 0x4000 to 0x4BF8. It is called twice: once
for each bank of ram (switched by the lower bit in the video register). Let me change "clearing to 0" to
"clearing to 1" to verify at runtime.

I found the strings for the splash screen. The screen memory is just a map of bytes. I need to figure out how the color
palette works. The number chars are red while the letters are blue. There is nothing in the tile grids to suggest a
difference.

I have seen in videos that the palettes do change. The double-ring planet changes color in one of the videos.

## 5/26/2023

I'm going to keep a detailed journal of this one -- step by step!

Why Phoenix? I remember it as a minor arcade game (not a mainstream game like PacMan) found at the grocery store. I'd play while my mom shopped.

It's not a complex game with only one 8085 CPU. I disassembled it as Z80 opcodes.

The mame source shows how the individual ROM files map to program space:

```
    ROM_REGION( 0x10000, "maincpu", 0 )
	ROM_LOAD( "ic45",         0x0000, 0x0800, CRC(9f68086b) SHA1(fc3cef299bf03bf0586c4047c6b96ca666846220) )
	ROM_LOAD( "ic46",         0x0800, 0x0800, CRC(273a4a82) SHA1(6f3019a074e73ff50ceb92f655fcf15659f34919) )
	ROM_LOAD( "ic47",         0x1000, 0x0800, CRC(3d4284b9) SHA1(6e69f8f0d537fe89140cd95d2398531d7e93d102) )
	ROM_LOAD( "ic48",         0x1800, 0x0800, CRC(cb5d9915) SHA1(49bcf55a5721cfcc02c3b811a4b601e35ea576db) )
	ROM_LOAD( "h5-ic49.5a",   0x2000, 0x0800, CRC(a105e4e7) SHA1(b35142a91b6b7fdf7535202671793393c9f4685f) )
	ROM_LOAD( "h6-ic50.6a",   0x2800, 0x0800, CRC(ac5e9ec1) SHA1(0402e5241d99759d804291998efd43f37ce99917) )
	ROM_LOAD( "h7-ic51.7a",   0x3000, 0x0800, CRC(2eab35b4) SHA1(849bf8273317cc869bdd67e50c68399ee8ece81d) )
	ROM_LOAD( "h8-ic52.8a",   0x3800, 0x0800, CRC(aff8e9c5) SHA1(e4164f85ec12d4d9bcbffba27ab1f51b3599f6d0) )

	ROM_REGION( 0x1000, "bgtiles", 0 )
	ROM_LOAD( "ic23.3d",      0x0000, 0x0800, CRC(3c7e623f) SHA1(e7ff5fc371664af44785c079e92eeb2d8530187b) )
	ROM_LOAD( "ic24.4d",      0x0800, 0x0800, CRC(59916d3b) SHA1(71aec70a8e096ed1f0c2297b3ae7dca1b8ecc38d) )

	ROM_REGION( 0x1000, "fgtiles", 0 )
	ROM_LOAD( "b1-ic39.3b",   0x0000, 0x0800, CRC(53413e8f) SHA1(d772358505b973b10da840d204afb210c0c746ec) )
	ROM_LOAD( "b2-ic40.4b",   0x0800, 0x0800, CRC(0be2ba91) SHA1(af9243ee23377b632b9b7d0b84d341d06bf22480) )

	ROM_REGION( 0x0200, "proms", 0 )
	ROM_LOAD( "mmi6301.ic40",   0x0000, 0x0100, CRC(79350b25) SHA1(57411be4c1d89677f7919ae295446da90612c8a8) )  /* palette low bits */
	ROM_LOAD( "mmi6301.ic41",   0x0100, 0x0100, CRC(e176b768) SHA1(e2184dd495ed579f10b6da0b78379e02d7a6229f) )  /* palette high bits */
```

First up is to create the boilerplate directory in the content area so the web-render program will function. I'll
make binary files for the background tiles, foreground tiles, and proms.

The mame source "phoenix.cpp" has a lot of good info:

```
    map(0x0000, 0x3fff).rom();
	map(0x4000, 0x4fff).bankr("bank1").w(FUNC(phoenix_state::phoenix_videoram_w)); /* 2 pages selected by bit 0 of the video register */
	map(0x5000, 0x53ff).w(FUNC(phoenix_state::phoenix_videoreg_w));
	map(0x5800, 0x5bff).w(FUNC(phoenix_state::phoenix_scroll_w));
	map(0x6000, 0x63ff).w("cust", FUNC(phoenix_sound_device::control_a_w));
	map(0x6800, 0x6bff).w("cust", FUNC(phoenix_sound_device::control_b_w));
	map(0x7000, 0x73ff).portr("IN0");                            /* IN0 or IN1 */
	map(0x7800, 0x7bff).portr("DSW0");                           /* DSW */
```

I looked through the code for "$50", "$58", "$60", etc and noted these hardware references in the comments.

Mame allows you to change the dip switch settings. I looked at the fields the code reads from the switches and found that Mame is
showing the switches left to right (backwards). Here are the switches from the code's point of view (MSb first):

```
LL_BB_C_xx_M

LL: Number of lives
  11 = three
  01 = four
  10 = five
  00 = six

BB: Bonus lives at
  11 = 3K/30K
  01 = 4K/40K
  10 = 5K/50K
  00 = 6K/60K

C: Coinage
  1 = 1 coin for 1 credit
  0 = 2 coins for 1 credit

M: Cabinet mode
  1 = cocktail
  0 = upright
```

There are two sets of sprites: background and foreground. The foreground is drawn over the scrolling background.

My intuition says the tiles are like the tiles in other systems (like Moon Patrol): split into two "bit planes" in the rom.
I ran a quick program to print text representations of the combined planes. I found the letters and numbers as expected,
though the images need to be rotated counter-clock-wise and then mirrored left to right. That's easy to do in code.

There are 256 tiles for foreground and 256 for background. Each tile is 8 bytes (8 bits by 8 bits). Each pixel can be one
of four colors (2 bits). One of the bits comes from the first plane in rom. The other comes from the second. 

I duplicated the javascript from other digs and got the tile sets displayed. Pretty cool looking. There is still a lot of
work to be done on the color palettes.

I made an intial pass through the code just looking around. There are a lot of padding FF bytes to start some functions
at nice addresses. For instance, the rountine at 0x200 has 8 padding bytes before it to land it on 0x200 exactly. I'm not
sure why the developers cared for the numeric address. Maybe I'll find that out!

I loked for "JP (HL)" and found a jump table at 0x400. Jump tables are easy to debug at runtime by changing the destinations.

I looked through the code for long sections of code that look "funny". These are data sections. Data seems to be sprinkled all
through the code and not neatly separated out to the end.