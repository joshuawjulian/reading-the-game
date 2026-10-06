# Coach / film review: 03-03 Gap Schemes: Power, Counter, Duo, Trap, Wham, Iso, and the Draw

Reviewer role: NFL coach and film analyst. I reviewed the qmd as of 2026-10-06 15:19. `pdfs/03-03-gap-and-power-runs.pdf`
has the same timestamp, so I did not rebuild it. I rasterized all 24 pages at 80 dpi (`_pdfbuild/03-03-gap-and-power-runs/rev-*.png`)
and the counter strip and pin-and-pull at 150 dpi (`hi-05c.png`, `hi-14c.png`), and looked at all 14 figures. I checked
coordinates against the chapter helpers and `gridiron.formations.technique` (3 = 2.35, 5 = 4.0, 7 = 4.2, 9 = 5.7, TE = 4.8).

**Overall:** this is a strong chapter. Power, counter, trap, wham and the Packers sweep are drawn and explained the way real
staffs teach them. Gap-down-backer, the C back block, the hinge, the RG/RT deuce to the backside backer, the GT counter with the
U filling, the trap's inside release and the influence trap are all correct. The film rooms are well chosen and accurately
characterized: Gibbs/Grimm/Jacoby, Riggins 1983, the 2011 49ers wham vs Suh at Detroit, Henry 2020, the 2019 Ravens record and
Barkley 2024. They agree with FACTS-current (Harbaugh fired after 2025, Stoutland gone, Moore to New Orleans). There are
**no illegal formations**. The two animations are well timed and tell their story in print.

What needs fixing: one terminology error that a defensive coach would catch at once (squeeze vs spill), one arithmetic
double-count in the chapter's central figure, two diagram mechanics bugs (pin-and-pull), and several places where the caption
or text does not match the drawing (duo, iso, wham, drill 3). Items are in priority order.

---

## A. Must fix (wrong or misleading football)

### A1. "Squeeze" is used for the spill/wrong-arm technique, which collides with 05-05's term index (log-block section, fig-kick-or-log, drill 3)
Lines 606-610: "The end is told to *squeeze*: to crash hard inside..., wrong-shoulder the puller and plug the hole, forcing the
ball to bounce outside... (Defenses call those two plans *spill* and *box*.)" In the CURRICULUM index, **squeeze is the alias
of box technique (05-05)**. That is the opposite plan: the end squeezes the down block but keeps his outside arm free and
forces the ball back *inside*. The technique described here (attack the puller's inside half with the outside shoulder, pile
up the hole, push the ball outside) is **spill / wrong-arm**. A reader who meets "squeeze = box" in 05-05 will be confused.
The current wording also suggests that the end who keeps his outside arm free is the only one who stays wide, but a boxing
end squeezes too.

Fix:
- Rewrite the paragraph around the real kick/log rule: *the kicker aims for the end man's inside number. If he can get his
  head inside, he kicks out. If the end has crashed so far inside (a hard squeeze, or a spill player wrong-arming) that the
  kicker cannot get his head inside, he logs him and the ball bounces.*
- Name the defensive plans correctly: box/squeeze = keep the outside arm free and force the ball inside; spill/wrong-arm =
  blow up the kick-out from the inside and force the ball outside to the alley player. Link both to 05-05.
- Rename the right panel of fig-kick-or-log from "End squeezes: log him" to **"End crashes inside: log him"**. Change
  "squeezes hard inside" in that caption and in drill 3 (lines 1287, 1292) to "crashes (spills) hard inside".

### A2. Power's arithmetic counts the RG twice (fig-power-count and lines 484-491)
The figure says that before the snap the play side has 3 blockers (RG, RT, Y) against 4 defenders, and that after the snap
it is 5 on 4. The next paragraph then sends the **same RG** to the backside Will ("The right guard's climb takes care of the
Will"). The RG cannot be one of the five play-side blockers and also be the backside's Will blocker. A sharp reader will
catch this in the chapter's key figure.

The honest count is 7 blockers (5 OL, Y, F) against 7 in the box. Y→5, RT(+RG)→3, F→S and LG→M give the play side a hat on
every defender *plus a double team*. The RG's spare hat then goes backside to the Will. The C takes the 1, the LT's hinge
is a hat spent on nobody, and the end is free.

Fix:
- Label: "after the snap: + LG + F = a hat on every play-side defender, with a double team to spare".
- Text: "five blockers for four defenders, which lets the RG help on the 3 and still climb to the Will".
- Add one sentence to make the trade explicit: "Power does not add a blocker to the box. It moves one, and the backside end
  is the receipt."

### A3. "Loaded boxes" (gap or zone section, table row "Beats…")
Lines 1083-1084 say that against "a safety down, seven or eight in it", power and counter "manufacture one". The table says
"Beats... loaded boxes (with numbers)". A gap scheme relocates hats; it does not create them. Against 8 in the box, power still
leaves two men free: the backside end and the down safety, who becomes the play-side alley player. Coaches answer 8-man boxes
with a QB read of one defender (03-04) or a throw.

Fix: "Against a seven-man box, power and counter win the point of attack by moving hats; against eight, even they leave a
defender free, which is when offenses read him with the quarterback or throw." Change the table cell to "seven-man boxes
(moves hats to the hole)".

### A4. "Every gap run is down blocks + kick-out + puller" contradicts the chapter's own duo, iso and draw (line 361, takeaway 1)
Line 361 says "Every gap run... is assembled from three parts", and takeaway 1 repeats it. Duo, iso and the draw have no puller
or kick-out, and the chapter says so itself ("Not every gap run pulls anybody").

Fix: "The *classic* gap run (power, counter, the sweep) is assembled from three parts...". In takeaway 1: "The core gap run is
down blocks, a kick-out and a puller; the rest of the family drops or swaps one part."

### A5. Duo caption names the wrong gap, and the drawn read arrow goes to the C gap (fig-duo, lines 672, 689)
The caption says the back hits "the A gap if the Mike fills outside, or the B gap if he fills inside". The second dashed read
arrow ends at w=3.9, between the RT (3.2) and the Y (4.8): that is the **C gap**. The 3-technique being doubled *is* the B gap
(w=2.35). Fix one of these:
- move the arrow to end at (2.6, 2.4) and keep "B gap", which is the classic duo coaching ("press the A, bounce to the B
  off the double"); or
- keep the arrow and say "or bounce outside the RG-RT double".

Also change "Nobody is assigned to the linebackers" to **"the double teams own the linebackers: the 1-double owns the Will,
the 3-double owns the Mike, and whoever the backer attacks decides which man comes off"**. That is how duo is taught, and the
green dashes already show it.

### A6. Iso: the definition of "bubble" doesn't match the drawing (fig-iso, lines 873-876)
The text says iso "usually aims at a bubble, the gap behind an uncovered lineman". The drawing hits the strong A gap, between
a C with a backside-shaded 1 and an RG who is **covered** by the 3. The only uncovered lineman is the LG (the weak-side
bubble, where the Will sits).

Fix: define a bubble as "an open gap or uncovered lineman, where the nearest defender is a linebacker", and say why the A gap
is open here (the 1 is shaded away and the 3 is outside the RG). Or add one line: "against this Over front, iso can also go
weak at the Will, over the uncovered LG".

Also on iso, lines 880-882: "leading a tight end or H-back through the hole, which is zone insert by another name" is wrong.
Insert is an *inside-zone* play: the line zone-blocks and the H takes a linebacker. Iso man-blocks the DL. Fix: "most teams
now lead a tight end or H-back through the hole instead, either as a true iso from 12/13 personnel or as the insert block on
inside zone (03-02)".

### A7. Wham: "every lineman climbs" is false in the chapter's own drawing (glossary def line 11, line 812, fig-wham caption)
In fig-wham the C back-blocks the 1, the LT blocks the backside end and the RT blocks the 5. Only the two guards climb. The
caption's "three linemen are on linebackers" is also wrong: it is LG, RG and the **Y**.

Fix:
- Glossary: "...the line leaves a defensive tackle unblocked, the lineman who would have blocked him releases to a
  linebacker, and a tight end or H-back comes across and hits the tackle from the side."
- Line 812: "the guards climb to the second level".
- Caption: "both guards and the Y are on linebackers".

### A8. Drill 3 is labelled counter, but the second puller is missing and the RG blocks the wrong linebacker (fig-drill-3, answer)
On counter (as fig-counter teaches) the RG climbs to the *backside* backer, the LT wraps for the play-side backer, and when
the guard logs, **the wrapping tackle follows the log outside and takes the first threat**, usually the scraping Mike or the
alley safety. Drill 3 draws only the LG, sends the RG to the M, and the answer says the counter-move to the SS is "a crack
block or a second puller", as if counter didn't already have one.

Fix:
- Add `O("LT","LT",-1.9,-2.2,"LT")`, trailing the LG with a purple ring, pathing to about (-1.6, 1.5).
- Retag the climbing RG's target as W at (4.6, 0.4).
- Answer: "Log him and bounce. The pulling tackle, who was going to turn up inside, now follows the log outside and takes the
  first defender to show (the Mike scraping, or the strong safety). Whoever is left over, often the safety, must be beaten by
  the back; that is why spill defenses build around a fast alley player."

The same RG→M issue appears in fig-kick-or-log. There, either drop the RG's climb or relabel the LB "W".

---

## B. Diagram fixes (mechanics, clipping, collisions)

### B1. Pin-and-pull: the toss lands in empty space (fig-pin-and-pull, `p.pitch("RB", t=0.3)`)
The brown dashed pitch ends at about (-2.6, 2.9). The back's drawn path passes w=2.6 at d=-5.6, about 3 yards deeper. In print
the ball is pitched to nobody. Fix: pitch later (t≈0.45) or move the RB's first via point shallower, e.g. `via=[(-5.0, 2.0),
(-3.6, 5.0), (-0.6, 5.6)]`, and confirm the arrowhead lands on the thick path. If `Play.pitch` targets the RB's position at
t + flight time incorrectly, note it for gridiron rather than editing it.

### B2. Pin-and-pull: pin/pull labels collide and float (same figure)
The RT's "pin" label at (-2.6, 3.2) sits on the toss line. The LG/RG "pull" labels at d=-4.7 are far from their players and
read as labels on the RB's path. Fix: put the four tags *above* the defenders' squares or directly under each lineman at
d=-1.9, nudged sideways so they avoid the Q circle (C's tag at w=-0.9). Or drop the C/RT tags and rely on the caption plus
purple rings. The "first puller kicks the end man..." label at (4.2, 10.0) touches the CB box: move it to (2.0, 10.4).

### B3. Pin-and-pull: the stated rule says the Y should pull, but he climbs; and the free defender is not named
The bullets say "Is it empty? Pull." The Y's backside (C) gap is empty, yet the caption has him go inside to the Mike. Add one
clause: "the tight end's rule differs: with a 9 outside him that he can't reach, he climbs to the play-side backer." Also name
the free player, as the chapter does on every other play: the **strong safety** (11, 7) is unblocked and is the back's to
beat.

### B4. Iso: the RB's arrowhead runs into the "...onto the Mike" label
The arrow ends at (6.2, 3.0). The label at (6.0, 5.0) sits on it in print. Move the label to (6.4, -4.8) with its leader to
the M, or end the RB at (5.4, 2.6).

### B5. Wham right panel: markers pile up at the point of attack
At 1.8 s the M square covers the "RG" text, the LG sits under the W, and the R, H and 3 rings overlap. Use t_hit + 0.15
(≈1.6 s), or widen `lat` to (-8.6, 8.6) and nudge the Mike's path to (3.6, 0.2) so the RG can be read. In the trap figure, the
caption says "about 1.5 seconds" but the panel title says "1.4 s": make them agree.

### B6. Power: the puller's turn-up passes through the Y's marker
The via point (-0.6, 4.75) is the Y's starting spot. In print the LG appears to run through the Y. Use (-0.9, 5.3) and
then (2.75, 4.4), which is also truer to the real technique: the puller turns up *off the Y's down-block hip*.

### B7. Kick-or-log: the LG starts 1.6 yards deep in the backfield, alone
Add the C at (-0.7, 0) and start the LG on the line at (-0.7, -1.6) with the same pull path. Or say in the caption "the
puller is shown already in his pull". As drawn, a beginner may think the guard aligns in the backfield.

### B8. Counter strip (looks good): optional polish
Frames 4-6 stack the R, LT and LG rings on one spot. Widening `lateral` to (-6.2, 8.4) would separate them. The Mike's
"false step toward the jab" (text line 530, "frame 2") is barely visible. Make his first leg longer (to (4.2, -0.4) at
speed 3.0) so frame 2 actually shows it.

### B9. Draw strip: name the climbers
The caption says "the center has released to the second level". The C ends at d=5.3 between both backers, and the Y "blocks
the Mike" but never reaches him (frame 4: Y at about 6.5, M at about 9). Say "the C climbs for the Will, the Y releases for
the Mike", and let the Y's last leg reach about (8.0, 2.2) so the frame matches.

---

## C. Nuance a coach would insist on

1. **The backside problem on power and counter.** The C's back block only works because the backside defender is a 1 shaded
   on him. Against a backside 2i or 3 on the pulling guard, the C cannot reach him. Offenses then check out of power, pull
   the tackle instead (**dart**, "T-power"), or fill with an H-back or fullback. Add two sentences after "power toward a
   3-technique and away from a 1". This also gives the "Follow the guard" checklist its main exception: on dart the guard
   stays home and the **tackle** pulls, so watch the backside guard *and* tackle.
2. **Who reads kick or log.** On power the kick-out man is the **fullback/H**, not the puller. The guard in power is the
   wrapper who reads the kick. The section says "the puller adjusts" generically. Say "the kick-out man (the fullback on
   power, the guard on counter) reads the end; the lead puller turns up off whatever he does".
3. **Puller technique words.** Readers will hear "bucket step", "skip pull" and "hug the down blocks" on broadcasts and in
   clinic tape. Line 1172 says "(some coaches call it a drop step)". Add *bucket step*, and one line that the puller stays
   tight to the down blocks ("hug the butts") and turns up with eyes inside for the first color.
4. **Watch-for-it: "Two pullers means counter" is too strong** (line 1193). The Packers sweep and pin-and-pull, both in this
   chapter, pull two guards. Fix: "Two pullers *with the back stepping away first* = counter; two guards pulling wide with the
   back flowing with them = sweep / pin-and-pull."
5. **The draw and the blitz** (lines 1058-1061). The draw is helpless against *interior* pressure or a mugged/sugar
   linebacker. Edge pressure often makes it better, because the rushers run past it. One clause fixes it. Also, "flip the
   field position" overstates a 5-6 yard gain: use "shorten the punt".
6. **Terminology dialects** (one short "Go deeper" or paragraph):
   - *G* or *Power G*: the guard kicks out, no fullback.
   - *GT counter*, *counter trey* and *counter OH* all describe guard plus tackle. *GH* and *GY counter* describe guard plus
     H-back or tight end, now the more common NFL version.
   - Duo is called "iso", "Dave" or "Ace" in some NFL playbooks, which is why broadcasters mix up iso and duo. Verify with a
     source before printing the specific names, or give it as "some playbooks call duo 'iso'".
   - Lead vs iso.
   - Pin-and-pull is grouped with the *outside-zone* family by many NFL staffs. The chapter half-says this ("thinks like
     zone"), which is fine.
7. **Front context.** Every figure is an even 4-3/4-2 front. One sentence noting that odd and tite fronts (4i techniques in
   the B gaps) are built partly to clog pullers' paths and remove down-block angles would set up 05-05 well. Hedge it or
   source it.

---

## D. Facts and film rooms (checked, fine)
- Gibbs/counter trey (1981 install; Grimm 68, Jacoby 66; the Nebraska credit with the dating caveat), Riggins 1983
  (1,347 yards, 24 TDs, then a record; 14-2), the Packers sweep (Kramer/Thurston, five titles 1961-67, *Run to Daylight!*
  1963), Henry 2020 (378/2,027/17, eighth 2,000-yard rusher), the 49ers at Detroit in Week 6 of 2011 (25-19, Walker wham,
  Suh), the Ravens 2019 record (3,296; Jackson 1,206), Barkley 2024 (2,005, ninth; SB LIX 40-22), and Shanahan 2019
  (ESPN) are all correctly characterized and sourced. Staff changes are labelled by season, consistent with FACTS-current
  C3, C10 and §9.
- The Packers sweep reconstruction matches Lombardi's 49 sweep: RT down, C back, FB on the end, Y on the Sam, onside guard
  outside, offside guard turns up inside, flanker on the safety. The caption hedges it appropriately.

## E. Code (eval: false BDB cell)
`ol = one[(one["side"] == "off") & ...]` includes the QB, backs and receivers. The "farthest sideways" player will usually be
the RB or a motion WR, not the puller. Merge `players.csv` and filter `position.isin(["T", "G", "C"])` (BDB 2025 tracking has
no position column) before the groupby.
