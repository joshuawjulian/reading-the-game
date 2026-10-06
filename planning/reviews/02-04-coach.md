# Coach / film-analyst review: 02-04 Spread Formations (2x2, Trips, Bunch, Empty, Condensed)

Reviewed 2026-10-06 against the chapter source and `pdfs/02-04-spread-and-modern-formations.pdf`
(22 pages, rasterized at 80 dpi in `_pdfbuild/02-04-spread-and-modern-formations/coach/`; the slot-dilemma
and empty-pressure figures re-rendered at 200 dpi). I looked at every figure and both frame strips.

**Verdict:** a strong, well-paced chapter. The plates are legal and consistent with 02-02/02-03, the
empty data sections are excellent, and the condensed section explains the "why" the way a coach would.
There is **one rules/legality error** (quads with a back), **one diagram that teaches leverage
backwards** (two-way go, left panel), **one diagram whose labels contradict its caption** (trips
rotation), **two drill answers that misdescribe their own pictures**, and a frame strip whose last
frame doesn't show what its caption says. Fix "Must fix" before sign-off.

---

## Must fix

### 1. Quads with a back is not legal as described (text, "Lopsided: nub and quads", ~l. 960–963)
> "quads leaves either one receiver on the other side and nobody beside the quarterback (...4x1...),
> or a back beside the quarterback and nobody at all on the other side."

The second option can't work with four eligible receivers. If nobody is on the left, the left tackle is
the left end of the line, so both of the other two players on the line must be on the quads side, and
the inner one is **covered**, so he isn't eligible (the 02-02 rule the chapter cites four times). Five
skill players can't fill four eligible quads spots, a back and a second end.
**Fix:** "Since only five players can be eligible and the line needs an eligible end on each side to
throw to both sides, quads almost always means empty: four receivers on one side, one on the line on
the other, nobody beside the quarterback (4x1). Keep a back beside the quarterback and one of the four
on the quads side ends up on the line inside another receiver, covered and ineligible." The glossary
entry ("at most one receiver on the other side") is fine.

### 2. Two-way go, left panel (`fig-two-way-go`): the leverage logic is reversed
The caption says the defender sits on the receiver's **inside** shoulder "because the sideline protects
the outside; the receiver's only real option is to fight back inside", and the drawing shows the solid
(real) route breaking **inside**, into the defender, with the outside break greyed out. That's
backwards. Inside leverage *takes away* the in-breakers. The wide receiver's routes go outside (fade,
out, comeback), and the sideline squeezes them. The defender doesn't have to guess because he
defends one way and lets the sideline handle the other.
- **Code:** in the `w_x < -12` branch, swap the styles. Draw the **outside** break solid
  (`[(-0.7, w_x), (3.2, w_x), (7.4, w_x - 6.0)]`, `style.OFFENSE`) and the **inside** break dotted grey
  (`style.MUTED`). Optionally add a small "taken away" note by the inside branch, about (5.5, w_x + 4.5).
  Keep "sideline = help".
- **Caption:** "Left: a receiver near the sideline. His defender sits on his inside shoulder (inside
  leverage) and takes away everything breaking in; everything breaking out runs toward the sideline,
  which squeezes it. One way to go, and the defender knows which. Right: ..." The body text at
  l. 1030–1031 ("he takes away the inside and lets the sideline take away the rest") is already right.
  Only the figure and caption are wrong.
- Nuance worth one clause: a pure two-way go is most dangerous against man coverage *without help*.
  With a safety or a hook defender helping inside, the cornerback can play outside leverage and stop
  guessing. That's why the two-way go matters most on 3rd down against man.

### 3. Trips figure (`fig-trips-choice`): the "rotate" panel contradicts its caption and the text
Caption and text (l. 636): "the right safety (SS) comes down over the third receiver, so the trips side
gets an extra defender." But in `trips_d(rotate=True)` the Will moves **back into the box** (4.5, 2.8)
as the SS comes down to (6.0, 7.4). The trips side still has three underneath defenders (C, $, SS), and
the panel's own label says "3 receivers vs 3 defenders", where the balanced panel said "3 + safety". A
reader sees trips coverage getting *worse* after the "extra defender" rotation. Choose one picture:
- **(A, recommended, matches the text):** keep the Will apexed in the rotated look, `D("WILL", "WILL",
  4.4, 6.6)`, and drop the SS between #2 and #3, `D("SS", "SS", 7.5, 9.2)`. Relabel to
  "3 receivers vs\n4 defenders". The box stays 5. X is alone.
- **(B, real Cover 3 "sky" rotation):** keep the picture and change the words. "The SS comes down over
  #3, which lets the Will return to the box. The defense gains a sixth run defender, keeps three over
  three on the trips side with the middle safety's help, and X is on an island." Relabel the right
  label "3 vs 3 +\nmiddle safety" and add a "6 in the box" tag.
- **Coach's addition (either way), one or two sentences + link to 06-06:** modern two-high defenses
  have a third answer. They keep both safeties deep and let the *backside* safety help on the trips
  side's #3 (Saban's "poach", or "solo"/"MEG" on the backside corner). The X receiver is still on an
  island, and the defense never shows one-high. That's the answer the reader will actually see most
  Sundays.

### 4. Drill 3 answer: X and Z are *outside* the nickel and linebackers, not inside them
Answer 3, item 1: "X and Z are already inside the nickel and the linebackers, so they can block down on
them". In the picture X is at w −8.6 and the nickel at −6.4, so X is **outside** the nickel and **inside
the cornerback**. That's exactly what makes a crack possible: you crack *down* (inward) on a defender
inside you.
**Fix:** "X and Z line up just outside the nickel and the linebackers and inside the cornerbacks, so
they can crack down on them in a step or two while a pulling lineman takes the cornerback..." Also
tighten the body sentence at l. 1071–1072 ("A receiver who lines up close to the formation is *already
inside* the defenders who would normally be his problem"), which invites the same confusion. Better:
"is already *inside the cornerback* and right next to the defenders he wants to block, close enough to
hit them from the side."

### 5. Drill 2 answer: the SS is not 12–13 yards deep
"...with the nearest safety twelve or thirteen yards deep." In `fig-predict-empty` the SS is at 7.5
yards over Y. Only the FS (13) is deep. **Fix:** "...the strong safety walked out over the tight end
and the free safety alone, thirteen yards deep." The draw logic (5 v 5, QB vs retreating DBs) stays
right. A coaching touch: against Cover 1 dime, the man-coverage defenders turn their backs to the QB,
which is *why* the draw works.

### 6. Bunch frame strip (`fig-bunch-traffic`): frame 4 shows the ball in flight, not the catch
`pass_to("Y", t=1.25)` with `BALL_SPEED` 18 yd/s from about (−6.5, 0) to about (1, 16) means the catch is at about
**2.2 s**. At 1.6 s (frame 4) the ball is still about 10 yards short of Y (visible at the LOS around
w 6), but the note says "Y catches it". Two more football problems:
- **The SS's path:** `(7.0, 7.6) → (7.8, 10.8) → (3.2, 14.8)` takes the man defender on a *flat*
  route **deeper and wider** first, so in frames 3–4 he reads as covering H's corner route. A man
  defender on a flat release triggers downhill and tries to go *over the top of the rub at shallow
  depth* (or under it), and gets caught in the traffic. Suggested:
  `bp.path("SS", [(5.4, 7.4), (4.6, 9.4), (3.4, 12.6), (1.8, 15.6)], absolute=True, speed=6.2, delay=0.35)`,
  so the delay is the traffic, not a wrong drop.
- **Times:** `BUNCH_T = [0.0, 0.5, 1.0, 2.2]` (or throw at t=1.0 and keep 1.9 as the last frame).
  Re-check that Y is still inside the window at the new last frame. `lateral=(-4.5, 19.5)` leaves
  about 3.5 yd outside y≈16, which is enough.
- Minor: in frame 3 the `$`, `C` and `H` markers overlap. That's acceptable for tracking, but if you
  move the SS, check it again.

### 7. Empty vs six-man pressure (`fig-empty-pressure`): label collision + undefined label
- The **M** box overlaps the right **T** box (Mike at (1.4, 1.5), SDT at (1.0, 2.35)). Move the Mike to
  the A gap and widen the 3-technique: `D("MIKE", "MIKE", 1.5, 0.8)`, `D("SDT", "DT", 1.0, 3.0)`, then
  re-aim the meet points (`("MIKE", 0.2)`, `("SDT", 2.2)`).
- **D** (the sixth DB on Y) isn't defined in the caption. Add "D = dime back (a sixth defensive back)".
- Nuance a coach would want named: leaving the **widest** rusher free is deliberate (inside-out
  protection: he has the longest path), and the answer has names: **hot** throw / **sight
  adjustment**, the receiver who converts his route into the area the blitzer vacated. One sentence
  in the text ("Coaches call that a hot throw...") gives the reader the term he'll hear on broadcasts.

---

## Should fix

8. **Crack toss strip (`fig-crack-toss`).**
   - With the LG pulling, nobody blocks the backside-shaded 1-technique (WDT at (1.0, −0.7)) or the
     Mike. They stand still in every frame, and the last caption says "only the safety is left". Add
     the real rules. The center reaches (cuts off) the 1-tech, `cp.block("C", pts=[(0.6, -1.1)])`, and
     the RG climbs to the Mike, `cp.block("RG", target="MIKE", speed=3.4)`. Or add a caption clause:
     "backside blocks omitted".
   - Add the rule every coach teaches with the crack: **the crackback block must be above the waist
     and to the front of the defender.** Blocking low on a crack from more than 2 yards outside the
     tackle, moving toward the ball, is an illegal crackback (15 yards), and hitting him from behind is
     a block in the back. One sentence plus a footnote to the NFL rulebook (Rule 12, Section 2). This
     also explains why the receiver needs the condensed split: he has to get his eyes and face on the
     defender's front.
   - Dialect note: the NFL's most common version pulls the **playside tackle** (or tackle and guard)
     for the corner, with the tight end or receiver cracking ("crack toss" / "crack-replace"). The
     guard pull drawn here is fine, but say "a pulling lineman, here the guard" so readers don't take
     it as the only version.

9. **Slot dilemma (`fig-slot-dilemma`, left panel).** The ball's dashed path ends about 3 yards inside
   Y's route and short of it (pass at t=0.9 while Y is barely 3 yards into a 5-yard hitch). The hitch's
   turn-back also isn't visible, so it reads as a 4-yard vertical. Use `p.pass_to("Y", t=1.3)` and
   `r.hitch(6)` (or draw the hitch with a visible 1-yard comeback toward the QB) so the throw meets the
   receiver at the top of the stem.

10. **Wide vs condensed (`fig-wide-vs-condensed`) caption overstates it.** "His corner route has little
    room": X has about 10 yards to the sideline, which is plenty for a corner or out. The real costs of
    the wide split are a **longer throw** (it travels 25-plus yards from the far hash, and gives the
    corner time to close), the **sideline acting as a 12th defender** on fades and back-shoulders,
    and a cornerback who can play inside-out with no penalty. Suggested: "...has less room and a long
    throw, and the cornerback can sit inside him and let the sideline do the rest." Also say the ball
    is in the middle of the field (on a hash, the boundary-side receiver may have only about 7 yards).

11. **"Empty shows the quarterback everything" (l. 668–671): the man/zone tell is too absolute.** "If a
    linebacker runs out with the running back, that's man. If he stays inside and lets a safety take
    the back, that's probably zone." A linebacker walking out over a split back is just as common in
    zone (he's the curl/flat player to that side), and a safety walking down onto the back is often
    *man* (the safety has the back). Better tells: who **travels with motion**, **press vs off
    alignment**, and **inside leverage with eyes on the receiver** (man) vs eyes on the QB (zone).
    Rewrite as "the quarterback can often make a good guess... For example, if a linebacker has to run
    out with the back when he motions, that's a strong man tell", and point to 02-06.

12. **Receiver numbering was already taught in 02-02** (l. 507 of 02-02: "#1, #2, #3", passing
    strength, "a back isn't counted until he picks a side"). This chapter introduces it as new ("you
    need the coaches' counting system") and gives it a glossary entry. Recast the paragraph as a recap
    with a link ("You met the count in [Formation Rules]..."), and decide which chapter owns the
    `Receiver numbering` glossary entry (it isn't in the CURRICULUM term index; neither is `Spread
    formation`, so add both to the index under whichever chapter keeps them). Add the dialect nuance a
    defensive coach would insist on: many coverage systems **count an offset back as #3 (or #4) to his
    side** before the snap, and **re-number after motion**, so "#3" can change between the huddle and
    the snap.

13. **Nub (l. 956–958).** "There's no wide receiver to put a cornerback on, so the defense often has a
    linebacker or an end responsible for him". That's only half the picture. The usual answer is that
    the **backside corner stays on the nub side** and aligns over or outside the tight end at 5–7
    yards ("nub" rules). That gives the defense a free force player against the run to the tight end
    and lets the corner carry a vertical release. Some teams instead travel that corner to the trips
    side. Either is the defense "deciding", which is the chapter's point.

14. **Wildcat figure and section.**
    - Caption: "so it has one fewer defender for a run play in which every blocker is accounted for" is
      hard to parse. Try "...so it has one fewer defender in the box, and the offense can block every
      box defender and still have a runner."
    - The Sam is labelled **S**, undefined in the caption, while the swinging-gate figure uses **S** for
      safeties and **L** for linebackers. Define it ("S = strongside linebacker") or label it "Sam".
    - Film-room nuance (verify before adding): Miami's 2008 Wildcat often lined up **unbalanced**, with
      the tackles side by side. If confirmed, that's a nice bridge between the two specialty sections
      ("the Dolphins stacked both tricks: wildcat plus tackle over").
    - The common NFL Wildcat runs **power/counter with a pulling guard** off the jet fake, not just an
      A-gap keep. The "keep" arrow straight up the A gap into the Mike is the weakest version to draw.
      Consider aiming the keep off-tackle to the right (away from the jet) with
      `branch(... [(GUN, 0.0), (-1.4, 1.0), (1.2, 3.6), (4.0, 4.4)])`.

15. **Condensed: two missing reasons a coach would name.**
    - **Motion.** A receiver 8 yards from the ball can motion across (jet, orbit, return motion) in
      about a second, which is how the Rams and 49ers paired condensed splits with snap-time motion.
      One sentence plus a link to 02-06.
    - **Play-action crossers.** From a condensed split the receiver starts *inside* the corner and
      just outside the linebackers' run fits, the ideal launch point for the deep over and crossers off
      outside-zone action (the Shanahan/McVay staple). Add it to "Everything looks the same".
    - **Dialect.** Coaches say "**plus/minus** split" (wider/tighter than the base landmark),
      "**nasty**" (about 2–3 yards outside the tackle or tight end), "**reduced**", "**squeeze**". A
      one-line callout or parenthetical helps the reader decode broadcast terms.

16. **Chiefs film room: check the characterization.** The two famous Super Bowl LVII touchdowns
    against man (Kadarius Toney, Skyy Moore) are usually described as **return motion** (the receiver
    motions across and comes back, and the man defender is caught going with him), not as bunch or
    stack. Re-read the Defector piece. If it is about the motion trick, either say "stacked and
    motioned receivers" and pair it with the motion chapter, or choose a cleaner cluster example (the
    Chiefs' bunch/stack red-zone work is real, but cite a source that describes clusters
    specifically). Don't let the motion example stand in for clusters.

17. **Drill 3 caption: say it's a defense that hasn't adjusted.** Corners sitting *inside* condensed
    receivers 6 yards off is a busted or lazy alignment (good defenses already cheat outside against
    tight splits). The drill works, but the caption should say "...a defense that has lined up as if
    the receivers were wide, both corners inside them..." so the reader doesn't learn it as normal.

---

## Nice to have

- **Bunch vs zone (l. 938–943).** "At their best against man" is the standard line, but bunch is also
  a staple against zone through **triangle/flood reads** (three levels on one defender's area, e.g.
  corner-flat-curl vs Cover 3's flat defender). One clause keeps the reader from thinking bunch is
  man-only.
- **Unbalanced.** In today's NFL the extra-blocker side usually comes from a **sixth offensive
  lineman** (jumbo packages) as often as from moving the left tackle, which keeps the left side intact.
  Also worth one clause: the defense's simplest answer is to **re-declare strength to the
  extra-tackle side** and slide the front, which is what the chapter describes as "shift a gap over".
- **Swinging gate.** The gate drawn has 4 linemen + 3 eligibles vs 4 defenders, so the real numbers
  edge is **blockers**: 4 linemen + Y + U can block all 4 defenders while Z carries. Saying "six
  blockers for four defenders" makes the arithmetic concrete.
- **2007 Patriots.** The Ringer source also supports their heavy **empty / four-wide shotgun** use;
  one sentence would tie this film room to the empty section.
- **Fig. 1 / fig. 2.** Both are correct. The 7-to-6 and 6-to-5 box counts match the drawings.

## Checked and correct (no change)

- Every plate is legal (`check_legal` passes, and I re-checked by eye): 2x2, 3x1, trey, empty, bunch,
  stack, trips nub, quads 4x1, the crack-toss and drill-3 condensed 2x2, tackle over (X on the line on
  the weak side), wildcat, swinging gate (X + C + 4 linemen + Y = 7 on the line, ends eligible).
- Depths and splits are realistic: shotgun 5, slots off the ball, corners 6–7 off, safeties 12–14,
  nickel apexed, outside receivers at about 15.5 (wide) vs 8.5 (condensed).
- Empty protection logic (5 vs 6, widest rusher free, hot throw where the blitzer came from), the
  Cover 0 structure, and the dime/draw arithmetic in Drill 2.
- Trips to the field / into the boundary, running away from trips, the 2x2 mirrored-concept logic.
- Crack-and-replace concept (receiver cracks the force player, puller kicks the corner), and the
  "defender with two jobs" framing.
- All data figures and the empty-by-situation chart match the text. The 2022/2023 source break is
  handled correctly.
- Labels stay inside the drawn windows in every figure. The only collisions are items 6 (minor, frame 3)
  and 7 (M/T).
