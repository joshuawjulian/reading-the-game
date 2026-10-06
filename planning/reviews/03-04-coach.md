# 03-04 Option Football: coach / film-analyst review

Reviewer role: veteran NFL coach and film analyst. Sources: the chapter source and `pdfs/03-04-option-football.pdf`.
All 21 pages were rasterized at 110 dpi and every figure was inspected.

**Verdict:** Strong chapter. The option principle, the hat math, the zone read, the scrape exchange, the
triple-option rules, the midline and the designed-run families are all correct in substance. Blocking
schemes are drawn the way real staffs draw them: power with the RT/RG double to the backside backer and the
backside guard pulling for the play-side backer, GT counter with the guard kicking and the tackle wrapping,
and veer release by the play-side tackle. The fixes below are about accuracy and nuance. **Three are
must-fix:** the "eleventh blocker" arithmetic, the claim that the triple "needs under-center snaps", and the
unblocked nickel in the inverted-veer figure.

---

## A. Technical errors in the text (must fix)

1. **"turns the running back into an eleventh blocker"** (Why it exists, designed QB runs, around line 1032). The
   arithmetic is wrong. With the QB carrying the ball, there are 10 non-carriers, so the back becomes the
   *tenth* blocker. The chapter's own earlier count ("Nine offensive players block or run routes") contradicts
   it. Fix: "turns the running back into an extra (tenth) blocker".
2. **"It needs under-center snaps and backs in the backfield"** (triple-option costs, around line 872). This
   is out of date. Shotgun and pistol triple options are common: zone read plus a pitch man, "gun veer", the
   2012 Washington pistol triple with a pitch back, and Navy's move to more shotgun option under Newberry. Fix:
   "The classic flexbone version needs under-center snaps and three backs in the backfield…"
   Then add one clause: spread teams run a shotgun triple by putting a pitch man (a slot in motion or a
   second back) behind a zone read.
3. **"Every option gains one man"** (Out-number it, around line 1056). This is true of two-way reads. The
   triple option reads **two** defenders and so gains two men, which is the whole reason it is devastating
   and why defenses need "assignment football". Fix: "Every read gains the offense a man (the triple, with two
   reads, gains two)…"
4. **Inverted veer, "It saves the blocker the play needed most"** (around line 689). The sentence says the
   saved blocker is "usually the fullback or a pulling guard… so the pulling guard can go straight to a
   linebacker instead". On power as 03-03 teaches it, the guard *already* goes to the linebacker. What the
   power read saves is the **kick-out man** (the FB/H-back): the back who would have kicked out the end is now
   the edge threat. Fix: "On power, the fullback or H-back kicks out the play-side end (03-03). The inverted
   veer doesn't block him at all; it reads him, so the back who would have been the kick-out man becomes a
   second runner, and the guard still pulls for the linebacker."
5. **Drill 3 answer: "Man coverage… nobody in the box needs to worry about a short pass to them."** This is
   misleading, and it misses the key coaching point against man. When the RB stays in to block (QB power,
   QB draw), the defender assigned to the RB in man coverage becomes a free run defender (a **"hug" or "green
   dog"** player). Against Cover 1, QB power/draw is good *because* it is 7 v 7 with the QB as a runner, but
   the offense must account for the hug player. Rewrite the sentence and add one line on the hug rush. Also
   mention that a read (zone read / power read) is the other way to get hat-for-hat. The drill asks "which
   kind of run", so only naming designed runs undersells the option.
6. **"Chess match"** (line 1057, "the box-count chess match"). AUTHORING §3 allows this phrase at most once in
   the whole book. Replace it with "box-count battle" or similar.

## B. Diagram fixes (concrete)

### fig-emolos (Fig 1)
- **Right panel label collision.** "the 5 is now inside him" (at d=5.6, w=2.8) sits on top of the **M** square.
  Fix: move the label to about (d=-2.6, w=4.6), below the LOS beside the Y, or use `point_to` from (6.0, 3.6) to
  the 5 at (1.0, 4.6) with a leader.

### fig-zone-read (Fig 2, frame strip)
- Assignments are correct: LT on the 3, LG to the Will, C on the 1, RG to the Mike, RT on the 5, Y to the
  Sam, backside end read. It is 7 v 7 with the read.
- **Keep row, frame 2:** at +0.85 s the crashing end is 2.5 yards deep in the backfield, almost on the mesh. A
  real crash is flat down the line, about 1 yard deep, aiming at the back's near hip. Fix:
  `go_to(p,"BE",(-1.2,-2.2),"path",speed=4.0,delay=0.15)` and then `(-1.4,-0.6)`. As drawn, he looks like he
  came through untouched off a missed block rather than squeezing.
- Optional: the gap between frames 2 (0.85 s) and 3 (2.4 s) is large. A frame at about 1.4 s, showing the QB
  clearing the end's original spot, would tell the keep story better in print. Three columns become four;
  that is within the strip budget.

### fig-scrape-exchange (Fig 3)
- The RB's fake track is drawn as a thick dark ball-carrier arrow while the keep branch is the green dashed
  arrow. The legend says thick dark = ball carrier, so the reader sees two carriers. Fix: draw the RB as a
  `path` (thin) or label it "R: fake".
- Nice detail worth one label: the LG's block ends where the Will *used to be*. Add `point_to` "LG climbs
  to an empty spot" near (3.4, -1.6). It shows why the exchange works.

### fig-inverted-veer (Fig 4) (must fix)
- **The nickel (NB at 4.0, 8.4) is unblocked, and the give path runs right past him.** As drawn, the give is a
  1-on-1 between the back and a free force defender. Real teams block him with the #2 receiver, or hold him
  with a bubble/RPO tag. Fix: add `O("H","WR",-1.0,9.8,"H")` and `go_to(p,"H",(3.4,8.8),via=[(1.0,9.6)])`.
  This is the slot reaching or walling the nickel, and the give then bends outside it (end the give at
  (3.0, 11.6)). Add the slot's block to the caption.
- The **keep path** runs straight over the RT circle (w≈3.3). The keep hits the C gap off the RT's down
  block, just inside the read end. Fix: keep points `[(-5.0,0.0),(-3.8,2.0),(-1.4,3.9),(1.4,4.1),(5.6,4.0)]`.
- The caption says the RT down-blocks "with help from the right guard", but the RG's line goes straight to
  the Will. Either add a via point on the 3 (`via=[(-0.2,1.9),(0.5,2.4),(1.2,1.0)]`) so the double shows, or
  drop "with help".

### fig-speed-option (Fig 5)
- The QB path ends at the end man's **inside** shoulder (w≈4.6), but the caption says he attacks the
  **outside** shoulder. The QB must aim outside to force the end to declare. Fix: QB end (-1.6, 5.6). The pitch
  then comes from about (-1.6, 5.8) to the back at (-2.8, 9.4). Move the RB end to (-2.8, 9.4) to keep about 4 x 1
  pitch relationship, and the pitch branch to start at (-2.8, 9.4).
- The keep branch goes straight up through the ringed end's spot. Turn it up at w≈5.2 after the end
  widens, which is fine once the QB aims outside.
- The backside 5 is unblocked and the LT climbs to the Will. That is acceptable on a fast perimeter play, but
  most teams have the backside tackle cut off or hinge the backside end. Optional: LT to the end, LG to the
  Will.

### fig-triple-option (Fig 6) and fig-drill-2 (Fig 13)
- **The arc block runs through the pitch key.** The play-side A-back's path (via (0.2, 7.0), (2.4, 9.2))
  crosses d=1 at w≈7.8, on top of the Sam at w=8.6. The caption says he "arcs around" the Sam, and the pitch
  key must be left **untouched** (touching him ruins the read). Fix:
  `go_to(p,"RA",(4.6,10.2),via=[(-0.6,7.4),(0.6,10.2),(2.6,10.8)],speed=5.0)`. That puts him at least 1.5
  yards outside the Sam when he passes him.
- **Label collision:** the leader for "A-back arcs to the safety" ends at (2.4, 9.0), right on the "2" label at
  (2.6, 8.6). Point the leader at the new arc path near (1.8, 10.6).
- The QB under center at d=-1.9 is about a yard deeper than a real under-center QB (about -1.0 to -1.2 behind
  the ball). Optional: `O("QB","QB",-1.2,0.0,"Q")` in `flexbone()`. This affects Figs 6, 7, 8 and 13.

### fig-triple-anim (Fig 7)
- **Frame 2:** the B-back is hidden under the ringed dive key, so the reader can't see the dive being
  "squeezed". Stop the dive key at (0.2, 2.9) instead of (-0.5, 2.7), or end the FB at (0.6, 2.2), so both
  markers show.
- **Frame 4:** the pitch man, the arc-blocking A-back and the SS are stacked in one clump at about (4.5, 10).
  This happens because the SS barely triggers (8.0 to 5.6 deep). The caption ("A-back outside the last
  defender") is not visible. Fix: have the SS fill the alley hard (`go_to(p,"SS",(3.0,9.0),"path",
  speed=5.0,delay=0.3)`), have the arc block meet him there (RA end (2.6, 9.6)), and bend the pitch man
  outside it: via (-0.6, 11.0), end (6.0, 12.0). Then time frame 4 at about 2.5 s.

### fig-midline (Fig 8)
- The assignments are right: PSG climbs to the Mike, PST on the 5, C back, B-back to the A gap, read the
  first DL on or outside the PSG. The keep arrow at w≈3.2 brushes the right edge of the ringed 3. Shift the
  keep to w≈3.6 so it is clearly "off his hip".
- Text nit: "the midline is a chain-mover, not a home-run play". The *give* is a chain-mover, but midline
  *keeps* are among Navy's and Army's most common long runs. Soften to "the dive is a chain-mover; the keep
  can go the distance if the read is clean".

### fig-qb-power (Fig 9)
- **The RB is ringed in green** (`p.highlight("RB")` defaults to the THIRD colour). Every other figure uses
  the green ring as "who has the ball", so readers will think the back is the carrier. Fix:
  `p.highlight("RB", color=PURPLE)`. `PURPLE` is already defined in the helpers.
- Optional: the QB path at w≈5.0–5.2 draws over the Y's starting circle. Shift it to w≈5.5 (via (0.8, 5.5),
  end (6.6, 5.6)) so it reads as "outside the Y's down block, inside the kick-out".

### fig-qb-counter-draw (Fig 10)
- Counter is correct (GT: the guard kicks, the tackle wraps, the RB fills for the pulled tackle on the
  backside end).
- QB draw: the interior DL rush arrows end inside or behind the pass-setting guards (the 1 ends at w=-2.6,
  through the LG). Engaged rushers should stop at the blockers. Fix: PT to (-1.4, 2.6) and BT to (-1.4, -1.6),
  and push the two ends wider and deeper (-4.5, ±6.4) so the "rushers ran past the QB" picture is clear.

### fig-drill-3 (Fig 14)
- On 3rd-and-2 the Mike and Will would be at 3–4 yards, not 4.5. Optional: set them to d=3.5. The 7-man box
  and single-high safety are good.

## C. Missing nuance a coach would insist on

1. **Dialect: "read option".** Broadcasters and most NFL fans call the zone read the **read option**, and the
   chapter itself uses "read-option fake" and "read-option wave" without ever equating the two. Add to the
   zone-read definition: "(on broadcasts, usually the **read option**)". Propose adding *read option* as a
   glossary alias of *zone read* in the CURRICULUM term index. Other dialects worth one parenthetical each:
   power read = "dash read" (Malzahn) / "Q power read"; speed option = "speed pitch"; slow-play = "squeeze
   and play" / "sit"; the dive key and pitch key are coached as **#1 and #2**.
2. **The count system (numbering defenders).** Option coaches number defenders from the inside out on each
   side: **#1 dive key, #2 pitch key, #3 alley/force (the arc block), #4 deep or corner (the receiver's
   block)**. Fig 6 already labels 1 and 2. Adding 3 (SS) and 4 (CB) costs one sentence, gives the reader the
   real coaching vocabulary, and makes "every defender on the right side is blocked or read" countable.
3. **Mesh mechanics: the decision point.** Add one sentence. The ride goes from the QB's back hip to his front
   hip, and the QB must decide **before the mesh passes his front hip**. A late pull is the classic fumble.
4. **Houston's veer was a split-back play.** Yeoman's veer ran from split backs: the play-side halfback dives
   and the backside halfback is the pitch man. The wishbone (1968) and flexbone came later. As written, a
   reader assumes the veer was a flexbone play.
5. **Watch-for-it heuristic flips on the power read.** "A back offset to one side runs to the other side… which
   makes the end on *his* side the read key" is right for the zone read. On the inverted veer the back still
   crosses the QB's face, but the read is the **play-side** end, on the side *away* from his alignment. Add
   one line, or the reader will mis-key the Ravens and Eagles power reads.
6. **Designed QB runs from empty.** Many NFL designed QB runs (QB draw, QB counter) come from **empty**, where
   no back blocks. Instead the offense spreads the box to 5 v 5 and the QB makes it 6 v 5 on the ball side.
   That is a second way QB runs change the count, and Allen and Hurts use it constantly. Also worth one bullet:
   **QB dart / QB zone** (QB inside zone with the backside tackle or guard pulling as a lead), now a staple
   NFL QB run.
7. **Jet / motion as the sweep runner.** Many NFL power reads and speed options now use a jet-motion
   receiver as the outside threat rather than the RB (e.g. "jet power read"). One sentence in the
   inverted-veer section connects to 02-06 and 03-05.
8. **Distinguish "QB power" from "power read".** They are adjacent sections with similar names, and a beginner
   will conflate them. Add a one-line contrast: power *read* has a read and two runners; QB power has no read
   and the back blocks.

## D. Film room and history

- **Washington 2012:** accurately characterized. Worth adding that Washington also ran a true **pistol triple
  option** (zone read with a pitch back), which strengthens fix A2.
- **49ers vs Packers, Jan 12, 2013:** the score, 181 yards, record and eighth start are right. The
  play-level details (a 13-yard keep on 3rd-and-2 midway through Q1; the 56-yard TD with Bruce Miller
  sealing Walden) come from a single Grantland source. Most retellings of the 56-yarder describe **Walden
  crashing on Gore** and Kaepernick keeping untouched, which contradicts the "Miller sealing Walden" claim. The
  fact-checker should re-verify against the game film or play-by-play before print.
- **Ravens 2019:** correct (3,296 team yards, 1,206 QB yards, unanimous MVP). Per FACTS-current, the Harbaugh
  and Monken era is closed. The chapter's phrasing ("2010s Baltimore", "the Ravens era") is consistent with
  that; keep it that way and do not imply current staff.
- **Hurts SB LVII** (70 yards, 3 TD) and **Daniels breaking RG3's rookie QB rushing record** (2024): correct.
- **Navy / Georgia Tech:** the spec lists them as examples, but they appear only in passing (GT 2008–2018 is
  correct). Optional: a short "Film room: Georgia Tech / Navy" on a midline or triple series, such as GT's
  2014 Orange Bowl season or Navy's 2015 Keenan Reynolds offense. Reynolds set the FBS career rushing-TD
  record. This would give the triple-option sections a real-team anchor.
- **History bullets** (Faurot 1941, Wilkinson via Iowa Pre-Flight, 47 straight, Yeoman 1965, Bellard 1968,
  Glenville State 1991 and Drenning, Ault's pistol and Nevada's three 1,000-yard rushers in 2009): all
  consistent with my knowledge. Rodriguez also ran the zone read at Clemson (OC 1999–2000) between Tulane
  and WVU. That is optional.

## E. Animation / strip timing

- There are two animations (the zone read with two branches, and the triple), well under the cap of four.
  Both strips tell the story in print, apart from the triple frames 2 and 4 clutter (section B).
- The zone-read strip times (0, 0.85, 2.4 s) are realistic for the mesh. The triple's pull at 0.85 s and pitch
  at 1.45 s are realistic.

## F. Data section (coach's eye only)

- The caveats (selection, situation, survivorship) are exactly right and well put. "The read's main product
  is the give" is the best line in the section.
- The chart annotation "Lamar Jackson starts (2018)" is fine. Jackson became the starter in Week 11.

## Summary of priorities

Must fix:
- A1 (tenth blocker), A2 (the triple is not under-center only), A3 (the triple gains two men), A4 (what the
  power read saves).
- B: inverted-veer nickel unblocked, triple arc path through the pitch key, QB power green ring on the RB,
  Fig 1 label on the M.

Should fix:
- A5 (hug player against man), the C1 "read option" dialect, C2 the count system, C5 the power-read
  watch-for-it flip, C6 designed runs from empty.
- B: speed-option QB aim, triple-anim frames 2 and 4, verify the 49ers play details.

Nice to have:
- Mesh decision point, split-back veer, jet power read, QB dart.
- Navy/GT film room.
- Under-center QB depth, LB depth in Drill 3.
