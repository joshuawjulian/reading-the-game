# Coach / film-analyst review: 11-04 Dynasties and Counterpunches (2000-2016)

Reviewed 2026-10-08 against the chapter source and `pdfs/11-04-dynasties-and-counterpunches.pdf` (18 pp.,
rasterized at 110 dpi to `_pdfbuild/11-04-coach/`). I looked at all nine figures. The chapter isn't edited here.

**Overall:** the history and the punch/counterpunch structure are sound. The explanations of Tampa 2's Mike,
the substitution dilemma and the zone-read arithmetic are what a coach would teach. There are no clipped labels
and no serious collisions. The fixes below are mostly about **diagram assignments that a coach would circle in
red** (the 12-personnel run, the hybrid-edge figure's labels and rush path, the pistol mesh). There is also
**one film room that mis-characterizes how the comeback happened**, plus several nuances that are missing.

---

## A. Must fix (technically wrong or misleading)

### A1. Film room, Colts at Bucs 2003: the comeback was not a "patient Tampa 2 beater" drive sequence
The nflverse play-by-play (`2003_05_IND_TB`, Q4/OT) shows the following:
- 35-14 at 5:09. **Brad Pyatt returned the kickoff 90 yards to the TB 12.** The first TD came on a 12-yard
  "drive", a Mungro 3-yard run.
- After Harrison's 28-yard TD (2:38) the **onside kick failed**, because Tampa recovered. The Colts got the ball
  back on a punt at their own 15 with 1:48 left.
- The tying drive was helped by a **Warren Sapp roughing-the-passer** flag and a **52-yard Harrison catch** to
  the TB 6. Ricky Williams scored on a 1-yard run.
- OT: **Vanderjagt's 40-yarder missed wide right**, and Simeon Rice was flagged for unsportsmanlike conduct
  (the leaping rule). The re-kick from 29 was good.

The current "What to notice" says the drives were "a lesson in how to play the Tampa 2 patiently: short throws,
quick snaps, then the shot over the middle when the linebackers' legs go". The game doesn't support that. Most of
the 21 points came from a kick return, a penalty-aided two-minute drive and a re-kick after a penalty.
**Fix:** keep the game, because it is Dungy's homecoming and the Tampa 2 mostly won it. Rewrite "What to notice"
to say so honestly:
1. For 55 minutes the Bucs' Tampa 2 held the league's best offense. Barber's pick-six came off a throw to
   Harrison, so it's worth watching how the corner squatted.
2. The comeback came from a short field, penalties and Manning's two-minute operation from the shotgun, with
   Harrison catching 28- and 52-yard balls.
3. The leaping penalty in overtime is a rules footnote that suits this chapter.

Optionally, point readers to a better Tampa-2-vs-Colts film example, such as any Colts vs. Lovie Smith's Bears.
SB XLI is the obvious one, though there Dungy is on the Tampa 2 side.

### A2. Hybrid-edge figure (fig-hybrid-edge): the labels undercut the figure's own thesis
- The caption says "One player, two labels", but the ringed player is labeled **E in both panels**. The 3-4 panel
  also labels both 3-4 defensive ends **E**, so four "E"s stand on the line and nothing visible says "outside
  linebacker". **Fix:** in the 3-4 panel, label both OLBs `O` (or `OLB`), keep the two DEs as `E` and the nose
  as `N`, and update the "Reading the diagrams" key. The ringed player's label then changes from E to O, which is
  the whole point of the figure.
- **The rush arrow runs straight through the left tackle.** The edge is at (1.0, -5.6). With pts (-3.5, 1.6),
  (-6.0, 4.3) the path crosses the LT's spot at w = -3.2, which reads as "run through the tackle". A speed rush
  turns the corner. **Fix:** about `pts=[(-1.2, -1.0), (-4.0, 0.2), (-6.2, 3.6)]`, i.e. up the field outside
  the LT's outside shoulder, then flattening to the QB's drop spot (about d = -7, w = 0). Keep the "rush" label
  where it is.
- "In the 4-3 his menu is mostly one item, rush" is too absolute. 4-3 zone-blitz teams (LeBeau's own Bengals
  in the early 1990s, and fire-zone 4-3s since) dropped ends. Say "**rarely** asked to drop".

### A3. 12-personnel dilemma, left panel (fig-pats-dilemma): the run's blocking doesn't add up
The ball goes **outside** (the RB path bends to w ≈ 9.8 and then 10.6, outside Y and around the $). The blocks
are drawn as a power/iso inside:
- **Y "drives the end."** SDE is at w = 5.6, *outside* Y (4.8). On a run outside Y, driving him out pushes him
  into the ball's path. Y has to **reach and seal him inside** (hook block).
- **F's lead path goes inside Y.** It runs (2.0, 4.1) to (6.4, 5.2), through the Y–SDE block, and in print the
  line crosses Y's gold ring. On a lead toss or outside run the lead back **arcs outside Y** to the $.
  **Fix:** `a.pull("F", [(-1.5, 5.6), (1.5, 7.2)], target="NB")` or similar, so F stays outside Y's block.
- **The backside line (LT, LG, C) has no assignment**, so three linemen stand still. **Fix:** draw cutoff blocks.
  C or LG cuts off the WDT, LT cuts off the WDE or climbs to the Will. Short reach arrows (`block(k, pts=[(0.6, 1.2)])`)
  are enough.
- RT on the 3-tech (SDT) and RG climbing to the Mike are fine as a combo. Better still, draw it as RG and RT
  combining the 3-tech up to the Mike.
- **Caption:** "Gronkowski **seals the end inside**, Hernandez **arcs around him** to lead on the nickel back
  ($), and the back follows them outside." Optionally call the play a "lead toss".

### A4. Predict 3 (fig-predict-read): there is no mesh, and the slot is uncovered
- **The QB and RB never meet.** The QB path goes (-4.0, -3.0) first, a 3-yard step to the *left*. The RB comes
  from (-7, 0) through (-4, 2), so they're about 5 yards apart at the "mesh". In the pistol zone read the back
  runs past the QB's right hip, the QB "rides" the ball in his belly while reading the edge, and only then
  pulls it.
  **Fix:** show the mesh at about (-3.8, 0.6), with RB `path [(-4.0, 0.9), (2.0, 4.0)]` and QB
  `path [(-3.8, 0.4), (-3.0, -2.0), (-0.5, -6.8), (5.0, -7.8)]`. Optionally add a small "mesh" label (keep it
  well inside the window).
- **H in the left slot (w = -9) has nobody within 7 yards.** That's because the defense is a 3-4 *base*
  single-high against 11 personnel, and an NFL defense wouldn't leave a slot uncovered. It also hands the
  offense the bubble screen this chapter later calls the packaged play. **Fix, either of:**
  - (a) Swap H for a second TE (12 personnel, the 2012 49ers' and Seahawks' bread and butter) so base is
    realistic.
  - (b) Keep 11 personnel and walk the W linebacker out to an apex at about (5.0, -6.0). The answer can then
    note that the apex player is the one an RPO bubble would read, which ties in neatly to the Kelly section.
- The caption says "the defense's right edge player". It is correct, but beginners will trip on it. Use
  "the edge player on the offense's left (the defense's right)".

### A5. Manning seam (fig-manning-seam): timing too fast for under-center play-action
The ball comes out at **1.6 s** after a play-action fake from under center. A real Colts stretch-action shot is a
5- or 7-step drop with a fake and takes about **2.4–2.8 s**. At 1.6 s Y is only about 10 yards up the field. The
picture still teaches the idea, but a coach will say "that ball's out before the fake is finished."
**Fix:**
- `p.pass_to("Y", t=2.4)` and slow the Mike's recovery slightly, so the catch lands around 22–24 yards at about
  3.4 s. Update `SEAM_T` to [0, 0.8, 2.4, arrival] and the panel title "+2.4 s · Y is past him: throw".
- Shorten the ball flight. The current 1.5 s for about 27 air yards is floaty, and a seam ball is closer to
  1.0–1.2 s.

The second-order issues are minor but real:
- **Corners stop at 10 yards** while X and Z run free to 25. A Tampa 2 corner with no flat threat **sinks**
  under #1 to about 12–15 yards (squeezing the hole shot). Fix with `p.drop("LCB", (14.0, -16.5), ...)` and the
  same for RCB, so the safeties' widening is a choice between two verticals, not chasing an uncovered receiver.
  The teaching point (two verticals in each half, the Mike carries the inside one) gets stronger.
- **Frame "+0.8 s": Y's ring touches the W label** (Y at about 4.5 yards, next to W). Nudge the Will's first step
  to (3.4, 6.0) or move his alignment to w = 5.0 so the ring clears.
- The DL stop after 1 yard and are still on the LOS at 3.1 s. That's acceptable for clarity, but let them
  penetrate about 2–3 yards so the clock looks real.

---

## B. Should fix (accuracy and nuance a coach would insist on)

1. **Seattle "played mostly one coverage, Cover 3".** Carroll's Seahawks were a **single-high** team that lived
   in **Cover 3 and Cover 1 (man-free)**. Cover 1 was heavy on third down and was a big part of the plan in
   SB XLVIII. **Fix:** "played almost exclusively single-high: Cover 3, and its man-to-man twin Cover 1".
   - Also note the corners' **"step-kick"** technique. In Seattle's Cover 3 the corners often aligned in press
     but stepped and bailed rather than full-jamming, while the true jam was a Cover 1 tool. That makes "the
     press corners used every inch of the 5 yards" accurate for Cover 1 and a slight overstatement for Cover 3.
2. **Opening hook, "an eighth defender walked up near the line".** Against Denver's shotgun 11 personnel, Seattle
   was mostly in nickel with a 6–7-man box. The "eighth man in the box" was the early-down, base-defense
   (Chancellor) picture. **Fix:** "a strong safety rolled down into the box or underneath".
3. **Seattle was a hybrid-edge team too, and the chapter misses it.** Carroll's base was the **4-3 Under with a
   "Leo"** (Chris Clemons, Bruce Irvin, Cliff Avril). The Leo is exactly the hybrid edge in a 4-3, and it ties
   sections 4 and 5 together. Add one sentence in the Seattle section. It is also a great tie-in to the
   hybrid-edge figure, since the 4-3 Under panel *is* Seattle's front.
4. **Dialect names for the hybrid edge.** Section 4 should list them, because readers will hear them on
   broadcasts: **Leo** (Carroll/Kiffin 4-3 Under), **Jack** (many 3-4s, e.g. Ravens), **Buck**, **Elephant**
   (the 49ers, Charles Haley era), **Rush/Predator**, and "EDGE" on draft boards.
   - Note the collision: some defensive staffs use **"Joker"** for this hybrid player, which is the same word as
     the offensive "joker" tight end this chapter defines. One clause in the move-TE paragraph prevents
     confusion.
5. **The 3-4 had two branches, and the chapter names only one implicitly.** It says New England built its 3-4
   "the other way, around two-gap linemen". Make the contrast explicit:
   - **Two-gap** (Belichick/Parcells, and LeBeau's base) needs 300-plus-pound ends and a nose.
   - **One-gap/attacking** (Wade Phillips in Dallas, Capers's zone-pressure 3-4) is basically 4-3 principles
     with a standing end.
   - This matters for the "What it costs" paragraph, which describes only the two-gap cost.
6. **Tampa Bay won SB XXXVII under Jon Gruden, a year after firing Dungy.** The text says "Tony Dungy and Monte
   Kiffin's Tampa 2 ... In 2002 Tampa Bay ... won Super Bowl XXXVII", which lets a reader assume Dungy coached it.
   One clause fixes it: "Dungy, fired after the 2001 season, watched the defense he built win it under Jon Gruden."
   It also sharpens the homecoming film room.
7. **The 2007 Giants: where the rush came from.** The lesson is not only "four rushers win". It is that the
   pressure came **up the middle** (Tuck over a guard, plus twists/"games" among the ends), into Brady's face,
   where a pocket passer can't step up.
   - Spagnuolo was a Jim Johnson-school pressure coordinator who mixed in blitzes. The NASCAR idea was to *not
     need* them on passing downs, so avoid implying the Giants never blitzed.
8. **Illegal-contact rule wording (2004 section and the Predict 2 answer).** The restriction beyond 5 yards
   applies only while the QB is **in the pocket with the ball**, and before the pass. Once he leaves the pocket,
   or the ball is thrown, illegal contact no longer applies, though defensive holding and pass interference
   still do.
   - The Predict 2 answer says "any contact past 5 yards before the throw is a flag", which is slightly
     overstated. Add "while the quarterback is in the pocket".
   - Also mention that the 2004 emphasis covered **defensive holding** as well, which is why some counts (PFT's)
     combine the two.
9. **Logic slip at the end of the 2004 section.** "The first team to show the league what the new passing game
   could do, though, was not the Colts. It was the team that had beaten them." But Manning's 49-TD 2004 season,
   described a page earlier, *was* the first showing. **Fix:** "The team that took the new rules furthest, though,
   was not the Colts..." or "The most dramatic demonstration..."
10. **Kelly's packaged plays: pre-snap vs. post-snap.** The text says the QB "chose after the snap by reading one
    defender". Many of Kelly's 2013 packaged plays were decided **pre-snap** by numbers and leverage: count the
    box, and throw the bubble if the slot side is outnumbered or the apex is soft. Others were true post-snap
    reads of a conflict defender. Say both, because that distinction is the line between a "packaged play" and
    a modern RPO in 04-06.
    - Worth one more sentence: Kelly's 2013 offense led the league in rushing with **Nick Foles**, a non-runner,
      at QB. The read's *threat* on the backside end did the work, which is a great argument for "the read
      survived".
11. **Predict 2 caption:** it says "one safety deep in the middle", but the drawing has the SS at 9.5 yards just
    left of center. Name him: "the strong safety sits underneath as a **robber** in the middle (the 'hole'
    player)". Otherwise a reader counts two safeties and calls it two-high.
12. **Fourth-and-2 film room:** add the detail coaches always add. New England had already burned its last
    timeout (before the third-down play), so Belichick could not challenge the spot. It also explains why
    the decision was so tightly argued. Verify the timeout sequence before adding it.

---

## C. Nice to have

- **Hybrid-edge figure, 4-3 Under panel.** Say in one line of the caption that the 4-3 Under is "a 3-4 with the
  weak outside linebacker's hand on the ground". Five men on the line in both panels (Sam on the line in the
  Under, both OLBs on it in the 3-4) is exactly why teams moved between the two so easily. The figure already
  shows it, so just say it.
- **12-personnel dilemma, right panel.** The Mike is unassigned. Add a small "Mike: rat / rush" note, or a
  dotted arrow to the hole at about (8, 0). A coach would ask what he does in Cover 1 against empty.
- **The move-TE letters.** "Many staffs call the move tight end the F or the H." Add **U** (common in
  Shanahan-tree and Kubiak systems) so readers who meet "U" in 04-08 aren't confused.
- **Saints paragraph.** Darren Sproles in 2011 was Payton's other "unlabelable" player, a running back used as a
  slot receiver. One clause would show the principle wasn't only about tight ends.
- **QB-run chart.** "Ravens (Jackson)" floats with no pointer. Ring the 2018–2020 BAL dots in grey, the way
  Denver 2011 is ringed.
- **Watch for it on Sunday.** Counting DBs on a broadcast is hard. Add "or count the linebackers: three
  stand-up players behind the line means base". Also add: "if the TE motions and a *linebacker* travels with
  him, it's man coverage, and the offense has found its matchup."

---

## D. Diagram-by-diagram status

| Figure | Legal formation | Alignments | Assignments | Labels / clipping | Verdict |
|---|---|---|---|---|---|
| fig-era-timeline | n/a | n/a | n/a | Clean | OK |
| fig-manning-seam (strip + 1 animation) | Yes (7 on line: X, OL, Y; Z and H off) | Realistic. Cover 2 safeties at ±9.5 are a touch wide but fine | Concept right; corners should sink; ball out too early | Y ring touches W in frame 2 | Fix A5 |
| fig-passing-boom | n/a | n/a | n/a | Clean | OK |
| fig-pats-dilemma | Yes (both panels: 7 on line) | Realistic | Left: Y must reach, F must arc outside, backside unassigned | Clean | Fix A3 |
| fig-hybrid-edge | Yes | 4-3 Under is correct (strong-shade nose, weak 3-tech, Sam on LOS); 3-4 4i ends OK | Rush path goes through the LT | Ringed player labeled E in both, four E's in the 3-4 | Fix A2 |
| fig-qb-runs | n/a | n/a | n/a | Ravens label unpointed | Minor |
| fig-predict-nohuddle | Yes | Realistic base single-high vs. 12-personnel spread | Fine | Q/R markers touch | OK |
| fig-predict-press | Yes | Press at 1.2 yd, inside shade: correct | Fine | SS role unnamed in caption | Fix B11 |
| fig-predict-read | Yes | Slot uncovered; base vs. 11 | No mesh; QB steps away from RB | Clean | Fix A4 |

Animations: one (the seam), well within the limit. The print strip tells the story. After A5, retime it so the
"throw" panel is at about 2.4 s.

Gridiron use is sensible. All the custom helpers (`snapshot`, `strip`, `pointer`, `say`, `ruler`, `trim`) live
in the chapter, and nothing in gridiron/ needs changing.
