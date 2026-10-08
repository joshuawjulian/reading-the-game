# Coach / film review: 08-02 Constraint Theory and Sequencing

Reviewer role: NFL coach and film analyst. I checked the qmd as of 2026-10-07 23:03 and the PDF built at 23:03:39.
I rasterized all 20 pages at 90 dpi and the figure pages at 150–170 dpi
(`_pdfbuild/08-02-constraint-theory-and-sequencing/coach/`). I looked at every figure (12 figures plus the frame strip).
I also checked the personnel coding against the 2024 participation data (throwaway scripts `pers*.py` in the same folder).

**Overall:** this is a strong chapter. The core idea is right and well taught: a constraint is defined by the defender
it punishes. The constraint tree is the right shape. The yankee description is correct. The tendency-table analysis
is honest and the cautions are good. The defensive mirror (Cover 0 / fire zone / sim from one mug look) is accurate.
There are, however, **several drawing errors in the signature plate (Fig 2) that any coach would catch**, one backwards
sentence about blitzes, a down-and-distance chain that does not add up, and a terminology gap (BCR) where the chapter
contradicts what 03-05 and 04-05 already taught. Items are in priority order.

---

## A. Must fix (football is wrong)

### A1. Fig 2 panel C (counter) and Fig 5 (strip): the back runs outside his own kick-out block
The RG kicks out the left end at `(0.5, -3.5)`, but the RB's track goes via `(-1.0, -3.9)` to `(6.0, -4.6)`. That puts
the back on or outside the kick-out block, running into the collision. On a kick-out counter the back always cuts
**inside** the kick, in the hole between the playside down-blocks and the puller.
- Panel C: change the RB's track to via `(-4.8, -0.9), (-1.0, -2.9)` and end `(6.0, -3.2)`. Move the RG's kick end
  slightly wider, to `(0.5, -4.1)`, so the hole is visibly between the LT (about -2.2) and the RG.
- Strip (`counter_play`): the RB currently ends at `(7.0, -4.6)` via `(2.0, -4.0)`, which grazes the RG at -4.6. Change
  it to via `(-1.2, -3.0), (2.0, -3.1)` and end `(7.0, -3.4)`. Keep the RG kick at about -4.6 and let the WDE drift to -5.6
  as now.

### A2. Fig 2 panel C: the fullback leads to where the Will *was*
The Will is ringed as having flowed to `(4.2, 0.4)`, but the FB's block ends at `(3.4, -2.6)`, which is the Will's
original spot. As drawn, the fullback blocks air. Fix: end the FB at about `(3.6, -1.0)`, meeting the Will as he
comes back. Alternatively, keep the Will static in panel C and use the strip to show the flow. Also give the LT a
purpose. Right now he steps to `(0.3, -2.2)` and blocks no one. Either have him double the 1-technique with the LG and
climb (`via (0.3,-1.2)` to `(3.0,-1.6)`), or leave him on a down block but have him end on a defender.

### A3. Fig 2 panel D (play-action shot): free rusher on the quarterback's blind side
All five linemen take the zone step right (`oz_first_second`), and the RB, FB and Y all go right as well. Nobody
accounts for the WDE. The QB then sets up at `(-6.4, -1.6)`, on the WDE's side. In a 7- or 8-man shot protection
off wide-zone action, the backside must be covered.
- Option 1: the LT steps right once and then hinges back on the end: `p.block("LT", pts=[(0.2, 1.0), (-0.8, -0.8)])`.
- Option 2 (very Shanahan): the FB fakes the arc and then crosses back to block the backside end
  (`via (-2.8, 3.0), (-3.4, 0.0)`, end `(-1.6, -3.8)`).
Either one makes "seven blockers" true. Today the count is 5 OL + Y + F, with the R ending in the backfield, and the
one man who matters is unblocked.

### A4. Fig 2 panel B (naked boot): X and Z finish in the same spot
X runs a 14.5-yard curl/comeback `(14.5,0),(12.5,1.2)` that finishes exactly where Z's deep over arrives at 15 yards
on the left. The two arrowheads overlap at top-left. On a boot or naked, the outside receiver to the boot side runs a
**clear-out** (go or post) to take the corner away, so the deep over has room. Fix:
`p.route("X", [(0, 0), (19.5, 0.0)])` (a go to the top of the window). Then Z's over at 15 has a cleared space under
it, and the flood is the textbook clear, deep over, intermediate (Y), flat (F).

### A5. "The blitz that punishes an offense for getting too comfortable with quick throws" is backwards
This is in the defense section, paragraph 1. Quick throws are the answer to the blitz. A blitz punishes slow-developing
dropbacks, long play-action shots, and a predictable protection. Drops and squat zones punish quick throws. Suggested
rewrite: "...its own constraint plays: the blitz that punishes an offense for holding the ball (or for always sliding
the same way), the drop that punishes a quarterback who expects a blitz and throws hot."

### A6. The illustrative drive does not add up (sequencing table)
- Snap 1 is 1st & 10 at own 25, gaining +5, which makes it 2nd & 5 at the 30. Snap 3 then cannot be "1st and 10, own
  34", because a 4-yard gain on snap 2 leaves 3rd & 1.
- Snap 3 gains +7 from 1st & 10, which makes it 2nd & 3, but snap 4 is listed as "1st and 10, own 41".
Snaps 4–7 are consistent with each other once snap 4 is fixed. A version that works:

| Snap | Situation | Call |
|---|---|---|
| 1 | 1st and 10, own 25 | OZ right +5 |
| 3 | 1st and 10, own 36 | OZ right +7 |
| 4 | 2nd and 3, own 43 | Counter left +11 |
| 6 | 2nd and 4, opp. 40 | OZ right +5 |
| 7 | 1st and 10, opp. 35 | Naked boot left +19 |

In this version, snap 2 gains 6 for a first down at the 36, and snap 5 gains 6 from opp. 46 to reach 2nd & 4 at opp. 40.
The prose keeps working.

### A7. The backside end's coaching contradicts 03-05 / 04-05 (missing "boot, counter, reverse")
Branch (2) says the backside end "is coached to squeeze down the line and chase." But 03-05 (l.1494) and 04-05
(l.1667, 1925) teach the reader that the backside end on outside zone is coached to **stay home and check boot,
counter, reverse** before he chases. That is the correct coaching. The naked works because the run game makes him
*break* that rule.
- Fix branch (2): "He is taught to squeeze the cutback while checking boot, counter, reverse; when the cutback hurts
  the defense enough, he starts to chase flat down the line, and that is the cheat the naked boot punishes."
- Reuse "boot, counter, reverse" in Predict 1 (see B1). It is exactly the defense's "constraint on the constraints",
  and it ties the chapter back to two prerequisites.

---

## B. Should fix (precision and realism)

### B1. Predict 1: "squeezes down" and "head across him" mix up kick-out and log
The caption says the end "stayed home and squeezed straight down." The answer then says he is "committed inside, where
the guard can get his head across him." Getting the head across is a **log** block, which seals the end inside and
sends the back *outside* him. But every counter in the chapter is drawn as a **kick-out** with the back inside.
Rewrite both:
- Caption: the end "now plays boot-counter-reverse: squeezes the cutback but keeps his shoulders square and his eyes
  on the quarterback."
- Answer: "...a squeezing end is the man the pulling guard kicks out; if he squeezes so hard he crosses the guard's
  face, the guard logs him and the back bends outside instead."
Also add one line: a disciplined BCR end is also a counter defender (the C in BCR). The counter still wins here
because the *linebackers'* over-flow is the bigger cheat, and that is why the answer is still the counter.

### B2. Fig 1 / Fig 2A / Fig 4 (21 panel): the RB's arrowhead ends on the Sam
The FB's arc block ends at `(3.0, 6.4)`, outside the Sam (who is at 5.2). That is a log or seal of the Sam inside. The
RB then finishes at `(3.8, 6.2)`, inside the FB and right on the Sam's square. That reads as "the back runs into the
man his fullback is sealing." Pick one picture:
- FB seals the Sam inside and the back bounces outside: RB end about `(5.0, 8.2)`.
- FB kicks the Sam out and the back presses Y's outside leg and goes inside him: FB end `(3.4, 5.0)`, RB end `(4.6, 4.2)`.
The first is the classic wide-zone "press, then bounce" picture and needs the least change. Apply it in all three
figures, which share the code.

### B3. Fig 4 panel 4 ("motion away"): Z is in the mesh at the snap
`p.motion("Z", to=(-3.0, 1.2))` puts Z at 3 yards deep and 1.2 yards *right* of the ball at the snap. That is exactly
where the QB opens (`(-3.3, 1.7)`) to hand off outside zone right. Snap it once Z has cleared the ball:
`p.motion("Z", to=(-2.4, -3.0))`, then continue the path to `(-2.6, -10.0)`. Alternatively, make it the more common
Shanahan picture: jet motion *toward* the play, with the ball snapped as the receiver passes the tackle and the jet
fake carried on. That is "same look, different eye candy" rather than "decoy away".

### B4. Fig 2 panel B: the fullback's first step gives away the naked
The FB's route starts via `(-3.0, -1.5)`, which is immediately to the left. In panel A he arcs right. The text claims
"same line steps and the back's same track". That is true of R, but the FB is a primary key for second-level defenders
reading "near back/fullback". Either have F take one step on his arc path before slicing back (`via (-3.6, 2.6),
(-2.6, -2.0), (-1.0, -6.0)`), or add F's opposite path to the "Look closely, the plays aren't perfectly identical"
paragraph as a third clue, next to the guard pull and the unblocked end.

### B5. Fig 5 caption: "kicks the backside end out"
On the counter left, the left end is the counter's **play-side** end. He is backside only relative to the zone fake.
Write "the end on the left (the backside end of the zone fake)". Readers who just learned frontside/backside will
trip on this.

### B6. Fig 9 / Fig 12: the "walked-up" nickel and strong safety are not walked up
The NB is at 5.0 and the SS at 6.0 deep. Those are normal nickel/overhang depths, yet both are ringed as part of the
pressure look, and the caption says they are "up". Move the NB to `(3.0, -6.6)` (inside shade of H, a real edge-blitz
threat) and the SS to `(4.0, 6.6)`. Then "six at the line plus two more threatening" is visible. It also makes the
Predict 3 answer ("the nickel off the edge") look plausible.

### B7. Fig 9 panel A: a 13-yard free safety manning the running back
For a pre-snap single-high look, this is not how teams play zero. Either show the FS rotating down at the snap (a
short path to about `(4, 0)` before the man line), or give the back to a second-level player, using the common "hug"
rule: if the back blocks, the man assigned to him rushes. Simplest fix: a caption clause, "the free safety comes down
late to take the back".

### B8. Fig 2 caption, panel C: "the line steps right"
Say why it looks identical: the play-side linemen **block down** (inside, to the right), so their first step matches
the zone step. One clause will stop a sharp reader from asking why the line runs away from a counter left.

### B9. Formation is more than where the quarterback stands
The objective says "by formation/personnel", but the table uses QB alignment as the only formation variable. (In 2024,
participation's `offense_formation` holds the same three values, so there is nothing better in nflverse.) Add one
sentence in "Building a tendency table": real tendency reports chart dozens of formation codes (2x2/3x1/bunch/nub,
backfield offset, motion direction), plus hash and field zone ("run to the field / to the TE / to the back's offset").
So the 67% here is a **floor** on what a pro staff gets from the look. This also strengthens the "Hide it" point.

### B10. Sixth-lineman snaps are folded into 11/12 personnel
`backs_tes` ignores the OL count, so 6-OL "jumbo" snaps are counted as 11 or 12 personnel. For 2024 neutral snaps this
is 6.7% of Detroit's plays (28 snaps, mostly coded 12) and 3% league-wide. It is not large enough to move the
headline numbers, but it matters for the team the chapter features *because* of its sixth-lineman use. Either count
an extra OL as a TE (the common "jumbo 12/13" convention) or add a line to the `[^neutral]` footnote.

### B11. Defense section: the Predict 3 protection language
"Slides its protection toward the mugs" is vague, because both mugs are in both A gaps. A coach would say the offense
IDs the Mike and **puts the center and back on the two mugged linebackers**, with the QB hot off any seventh rusher.
Use that in the Fig 9 prose and the Predict 3 answer.

---

## C. Nuance a coach would add (one or two sentences each)

1. **Credit Alex Gibbs.** "The outside-zone system of Mike Shanahan's Broncos" should name Gibbs (Denver OL coach from
   1995), who built the zone-and-boot package. 03-02 already tells his story (l.1513), so a link is enough.
2. **The Wing-T mechanism, not only the list.** The reason the buck series sequences is the **guard key**. Both guards
   pull on the buck sweep, so linebackers learn to read the guards. The buck trap hits where the pulling guards just
   left, and the waggle uses the same guard pull as the quarterback's escort. One sentence turns a list of plays into
   the cleanest example of "the constraint looks like the base play to the defender's key."
3. **Terminology dialects.** Coaches rarely say "constraint play". Staffs say "complementary plays", "answers",
   "if-then calls", "keepers" (a play that keeps the defense honest, not the QB run), "play-pass off it", "plays that
   hold". A "Madden vs real life" or margin note listing these helps the reader decode clinic talk and broadcasts.
4. **Within-run variety is part of the Eagles story.** The 2024 Eagles' pistol tendency was run/pass, but the runs
   themselves carried built-in constraints (QB read keeps, RPO tags, varied schemes and directions). Knowing "run"
   didn't tell the defense *which* run. That is a sharper "what to notice" than "they won at the line anyway".
5. **2025 family tree.** The Jets' 2025 offensive coordinator was Tanner Engstrand, Ben Johnson's passing-game
   coordinator in Detroit. That fits the chapter's "family tree" reading of the 2025 chart neatly. (Not in
   FACTS-current; verify before printing. FACTS lists Frank Reich as the 2026 OC.)
6. **Protected boot vs naked, and the end's key.** On wide zone the backside end is usually cut or cut off by the
   backside tackle (04-05 says so). So the naked's tell is precisely "nobody touched me", and a well-coached end's
   rule is "no cut, no block: think boot." The chapter half-says this. Make it explicit in "Look closely..."

---

## D. Diagrams: clipping, collisions, gridiron use

- **Clipping:** no labels are cut by the field edge. The Fig 1 badge "4" sits about 1.3 yd from the top of the window,
  which is marginal but fine because it is a badge, not text.
- **Collisions:**
  - Fig 2D: the dashed throw line runs straight through the W square. Bend the post's catch point to about `(18.0, -2.5)`,
    or move the QB's set point to `(-6.6, -0.6)`, so the throw clears the Will.
  - Fig 2B: the X/Z arrowheads overlap (fixed by A4).
  - Fig 1 / Fig 2A: the RB arrowhead sits on the S (fixed by B2).
  - Fig 10: the Mike's ghost arrow ends touching the S square. End it at `(3.0, 4.2)`.
- **Frame strip (Fig 5):** the timings tell the story (0.5 / 1.2 / 1.8 / 2.8 s; handoff at 1.17 s is realistic for a
  counter mesh). In frame 2 the RG and F markers overlap. Delay the FB to 0.35 s or route him half a yard deeper.
  There is only one animation in the chapter, well under the cap.
- **gridiron use:** the chapter re-implements a frame-strip/video renderer (`panel`, `strip`, `video`) and a `clean()`
  that strips hash marks by matching line width 0.5 and text alpha 0.55. That is fragile if `gridiron.Field` styling
  changes. It works today. Note for the library owner: expose `Field(..., hashes=False, numbers=False)` for zoomed
  `Play.draw` calls, and let `show_animation` accept per-frame captions and ring overlays, so chapters stop
  copy-pasting this.
- **Legality / alignment check:** all offensive formations have 7 on the line with only the ends eligible: offset I
  (Y and X on), gun 11 (Y and X on), wing 12 (U a legal wing off the ball), ace 12 (U and Y attached, X and Z off), and the
  spread (X and Z on). The 4-3 over (5/1/3/9, Sam over Y, SS in an 8-man box) and the nickel mug front are realistic.
  Fire zone (3 under / 3 deep with an end dropping) and sim (4 rush including the Mike, a DT dropping, 4 under / 3 deep)
  are drawn correctly.

## E. Checked and correct (no change)
- Yankee definition; play-action as "fake that looks like the run, not a successful run game" (consistent with 04-05).
- The RPO "built-in constraint" box, including the ineligible-downfield limit on depth.
- "Bang, bend, bounce" and the counter as the run version of the boot.
- Corn Dog (Toney 12:04, Moore 9:22 Q4) and the "Tom and Jerry" relative in LVIII; the Lions' 2023 Decker/Skipper
  two-point play; Detroit's 564 points in 2024; Barkley's 2,005 yards; and Johnson as DET OC 2022–24, then CHI HC
  in 2025. All consistent with FACTS-current.
- Kovash and Levitt's negative serial correlation; Walsh's script; Raymond's "sequence football" quote.
- The data sections: the neutral filter, leave-one-game-out prediction, and the PA split explaining the run-look pass
  premium. These are honest and well caveated.
