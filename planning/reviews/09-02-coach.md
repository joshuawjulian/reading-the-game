# 09-02 Kickoffs, Returns, and the Dynamic Kickoff: coach / film-analyst review

Reviewed 2026-10-08 against the chapter source, the built PDF (`pdfs/09-02-kickoffs-and-returns.pdf`, 18 pp.,
every figure page rasterized and inspected at 120-220 dpi), and the text of the *2026 Official Playing Rules*,
Rule 6 (scratchpad copy of the PDF the chapter already cites). w below = yards from the field's center line
(+ = top of the horizontal plates); NFL hashes are at |w| = 3.08; the yard-line numbers run from 7 to 9 yards
off the sideline, so "outside the numbers" means |w| > 19.7 and "between the numbers and the hashes" means
3.08 < |w| < 17.7.

Overall: the chapter is strong. The rules history, the table of drive starts, the touchback math, the hat-math
framing of the return and the film-room picks are right and well chosen. **One mechanism is taught wrong in
several places (hang time), two diagrams show illegal alignments, and the return-blocking section leaves out
the double-team rule.** None of these is hard to fix.

## A. Must fix (technically wrong)

### A1. Hang time does not give the coverage a head start under the dynamic kickoff
The coverage cannot move until the ball hits the ground or a player in the landing zone or end zone
(6-1-3). So hang time buys the coverage **nothing**. Under the old kickoff it bought running time, and that
is the habit these lines carry over. A high, hanging kick actually helps the *returners*, the only receiving
players allowed to move, because they get time to settle under it and build speed. What helps the kicking team
is (1) **depth**: the returner has to cover 30+ yards to reach a wall that the coverage reaches in 5, so the
blocks have to hold for 3-4 seconds; and (2) **a ball that hits the ground first**: a bouncing or line-drive
kick releases all ten cover men while the returner is still chasing the ball. That is why low line drives
that land around the 3-8 and skip became the standard kick, and the chapter's own Drill 1 answer says so ("the
line drive that lands at the 3 and skips in"). Lines that contradict it:
- l.551 (old vs new, point 2): "shifts the drama from the kicker's leg to his accuracy and hang time" -> "to
  where, and how, the ball first comes down: depth, and whether it is caught or bounces."
- l.842-843 (menu item 2): "caught around the 2 or 3 with the coverage closing as it comes down" -> the
  coverage is released at the catch; say instead that a catch at the 2 leaves the returner 33 yards to run
  before he reaches blocks that the coverage reached after 5.
- l.901-902: "a kick that is caught at the 15 with the coverage still far away" -> the coverage is always
  at the 40 when it is released. A catch at the 15 is dangerous because the returner reaches the wall at full
  speed *before the blocks have broken down*. Your own Fig 6 supports this: drive starts rise with shallower
  catches.
- l.1095-1096 (Watch for it): "a kick that hangs four seconds and comes down at the 3 gives the coverage
  time to arrive" -> replace with "Did it bounce first? A bouncing ball releases the coverage while the
  returner is still fielding it. How deep was it caught? The deeper the catch, the longer the blocks must
  hold."
- l.1039-1040 (Saints film room): "How long does it hang? Is the coverage arriving as it is caught?" and "with
  the coverage already moving" -> "Does it come down near the goal line? Does it bounce before it is fielded
  (so the coverage is already moving)?"
- Add one sentence after Fig 6 explaining *why* deeper is worse (returner distance vs. a fixed 5-yard
  coverage start). That causal link is the heart of the kicker's menu, and right now the reader only gets
  the dots.

### A2. The double-team rule is missing, and the "spare blocker" logic breaks it
6-2-1-2(c): "A double team block is permissible only by players who were initially lined up in the setup
zone." The wedge is still banned (6-2-1-2(d): two or more players shoulder to shoulder within 2 yards moving
forward together; 15 yards).
- l.794-800: "spend a spare blocker on a double team." The spare body is the second returner, and **he may
  not take part in a double team**. The real accounting is that a setup-zone player doubles and the second
  returner takes that player's man (a lead/kick-out, as in the sim). The sim already does this legally (L4 +
  F3 double C7, KR2 kicks out C8). Say so in the text: "the second returner can't join a double team (only
  setup-zone players may), so he takes the man the doubling blocker left."
- l.831-834 (Why it exists): "Under the old rules, double teams and wedges were restricted ... the league
  allows them" overstates it. Double teams are still restricted (setup-zone players only) and wedges are
  still illegal. What changed is that with everyone starting 5 yards apart, a double team at the point of
  attack became *practical*. Reword.
- In the "blocks are run-game blocks" bullet (l.813-814): "the same idea as a combo block" -> a combo means
  one blocker climbs to a second-level defender, and there is no second level here. Call it a drive double
  team (a "deuce"), as on power.

### A3. Illegal receiving-team front line in every dynamic-kickoff diagram
6-1-3(b)(1): of the players on the 35, at least one must be inside the hashes, at least one between the
numbers and the hash **on each side**, and at least one **between the sideline and the outside of the numbers
on each side**. `dynamic_units(line=(-16, -8, 0, 8, 16))` puts nobody outside the numbers (|16| is 10.7 yd
off the sideline, inside the numbers). This affects Fig 2 (plate), Fig 4 right, Fig 5 (return strip), and
Drills 2 and 3.
- Fix: default `line=(-21, -10, 0, 10, 21)` (L1/L5 outside the numbers, L2/L4 between numbers and hash, L3
  inside the hashes). The floaters (-19, ±2.5, 19) are legal under 6-1-3(b)(2)-(3) (no more than two per
  area, one outside the hash each side, three or more outside the hashes on each side). For the return play,
  the C2/C10 engagements then move: L1 takes C2 at about w = -21 and F1 takes C3, or simply re-pair the
  blockers by proximity. Keep the L3 seal / L4+F3 double team / KR2 kick-out story as is.
- Gridiron note (do not edit the library; mention it to the library owner): `gridiron/field.py`
  `NUMBERS_IN = 12.0` draws the numbers about 12 yd off the sideline. On an NFL field the numbers sit 7-9 yd
  off it, so the drawn numbers make players look "outside the numbers" when they are not. Until that is
  fixed, place outside-the-numbers players at |w| >= 20.5 so they read correctly against either.

### A4. Illegal onside-kick alignment (Fig 8)
6-1-6(c)(3): on each side of the ball, at least **two** kicking players outside the numbers and two between
the numbers and the hashes. The figure has `[-21, -17, -13, -8, -3.5, 3.5, 8, 13, 17, 21]`, which puts only
±21 outside the numbers (±17 is just inside the top of the numbers).
- Fix: `[-23.5, -20.5, -14, -9, -4, 4, 9, 14, 20.5, 23.5]`. Five per side is still legal.
- The kick-side arrows (C1-C4) stop at d = 8.5-9.5, *short* of the 10-yard line, while the hop lands at
  d = 12. It reads as if they pull up. Run C1-C3 to about (11.5-13, -21..-15), converging on the X, and leave
  C4 trailing as the "scoop" player at about (10.5, -10). The label "must go 10 yards before the kicking team
  may touch it" already explains the timing.
- Worth one clause in the text: a declared onside kick that goes untouched past the 15-yard onside setup zone
  is a 15-yard unsportsmanlike penalty and the receiving team's ball (6-1-6(k)), so the kicking team cannot
  declare onside and then kick deep. Also, the ball may lean against the tee and a holder may be used on a
  declared onside (6-1-1), which is how kickers get the big top-spin hop.

### A5. The squib is described with pre-2024 tactics
- l.14 (glossary), l.844-846 and l.927-933: "often aimed at a blocker." Under the dynamic kickoff a kick that
  first touches a setup-zone player (their 30-35) or the ground short of the 20 is dead, and it is the
  receiving team's ball at its 40 (6-1-4(d)(3)). The old squib aimed at a front-line blocker is now a
  giveaway. Today's squib or "bounce kick" is a low line drive that must **first touch the ground inside the
  20**. It is aimed away from the dangerous returner: at the up returner, or at the gap between the returners.
- l.932-933: "a squib that dies short of the 20" -> "a squib that first hits the ground short of the 20."
  Where it *first lands* is what counts, not where it dies.
- Related nuance a coach would insist on: a ball that lands in the landing zone is live for **both** teams.
  The coverage may recover it (6-1-4(c)), and that is the real risk of letting a bouncer go or muffing it.
  The chapter never says this. Add it to the "lands in the landing zone: live, must be returned" sentence
  (l.403-404). Strictly, it need not be returned: if nobody tries to possess it and it comes to rest, it is
  dead at that spot, 6-1-4(e). So "must be returned" is the practical answer, not the literal rule; write
  "live: field it or risk the coverage recovering it."

### A6. Smaller rule/wording fixes
- l.471: "the touchback is set deliberately high so that kneeling is not free" reads backwards. The touchback
  is set high so that *kicking it into the end zone* costs the kicking team.
- Fig 3 label (l.440) says "penalty, ball at the 40" and the caption says "a big penalty in field position,"
  but the text (l.401-402) rightly says "enforced with field position, not flags." Change the label to "dead:
  ball at the 40." Change the caption to "a big loss of field position." Change menu item 4 (l.847) "costs a
  penalty" to "gives the ball at the 40."
- Watch for it (l.1087-1088), "one deep with an extra blocker up front": add that with ten in the setup zone
  the rule requires **six** on the 35, not five (6-1-3(b)(1)). That is a countable pre-snap tell.
- l.948-950 and Drill 1 use `EZ25`, which mixes balls that landed in the end zone (knee = 35) with balls that
  landed in the landing zone and rolled in (knee = 20). The kneel/run advice is right, but compute the "only
  9% reached the 35" figure on fly-landed balls only (or say the figure pools both kinds of kick).

## B. Diagrams (looked at every one)

| Fig | Verdict | Fixes |
|---|---|---|
| 1 return rate / drive start | Good. The labels and the stepped rule annotations are clean. | none |
| 2 plate (2026) | Clean labels, nothing clipped. Front line illegal (A3). The kicking ten are legal (two outside the numbers, two between the numbers and the hashes, two inside the hashes, per 6-1-3(a)(2)). | Fix the front line. Optionally label the coverage L5..L1 / R1..R5 (see C1). |
| 3 outcomes map | Good teaching device. | "penalty" -> "dead" (A6). |
| 4 old vs new | Right panel: front line illegal (A3); the "contact here" box sits on the "30" numeral and 5 yards behind the shaded band, so move it to about R(33.5), w = -21. **Left panel: the coverage arrows end at R(27), 2.5 yards *past* the blockers' arrow tips at R(29.5)**, so the coverage appears to run through the return team. End the coverage at about R(30) and the blockers at about R(27), so the arrowheads meet facing each other inside the shaded band. Unlabeled up-back at R(14): either tag it "up back" or drop it. | as stated |
| 5 return strip | The story reads well in print; the timing is realistic (hang 3.9 s, cover men ~0.9 s to contact, returner 8.2 yd/s, tackle at 7.9 s, a 31-yard return). Issues: (a) front line illegal (A3). (b) **Panel 4 has the kicker arriving *through the lane* at the 35 to make the tackle, at the line of blocks**, so the lane the scheme built is filled by the man it chose to leave free. Coaches teach the returner to "make the kicker miss": the kicker is the returner's man. The more typical good return clears the lane and is tackled 5-8 yards past it by the kicker or the backside man in space. Suggest moving K's endpoint to about (27.5, 4) and the returner's last points to about (29.5, 5) -> (27.8, 4.6) (tackled near the 37-38), with C1 arriving a beat late from the left; update the caption's "33" and the "tackled at the 33" tag. (c) In panel 3, C8 (blue, through clean at about their 32.7, right of the double team) is unlabeled and looks like a missed block. Tag it "kick-out man" there, or tag KR2's target. (d) The blockers *step forward* to meet the cover men at the 34-35. Many units take a drop or kick-slide step or two to set before contact. Not wrong, but a slight drop (engage around the 33) reads more like real film. | as stated |
| 6 touchback math | Good. | Add the causal sentence (A1). |
| 7 team scatter | Good; the labels are clear. SEA/CAR/LA/ARI/TB are characterized correctly. | none |
| 8 onside | Alignment illegal and arrows short (A4). The hands-team geometry is plausible: 9 in the 15-yard onside setup zone, a deep player and a returner behind. In practice the front hands line usually sets a yard or two *behind* the receiving restraining line (about 11-13 yd from the ball) to play the hop, not on it. Consider H1-H7 at d ≈ 12. | as stated |
| 9 Drill 1 | OK; the coverage is released and closing, the blockers are retreating. | none needed |
| 10, 11 Drills 2-3 | The bold scenario box overlaps the top cover man (C1 at w = -22.5) and covers the "30/40/50" numerals. | Move the box to about d = 2, w = -12 (behind the coverage line, below the top numerals), or give it a narrower width. Front line illegal (A3). |

Animation count: one (the web return video). Fine.

## C. Missing nuance a coach would insist on

1. **Terminology dialect.** Every staff numbers kickoff coverage outward from the ball as **L5-L1, K, R1-R5**
   (L1/R1 nearest the kicker), and the return front line similarly by position. The chapter's "C1-C10" is
   invented. Labeling the plate's cover men L5..R5 (and calling the unblocked man "the backside L5") would let
   readers match real coaching tape and broadcast graphics. Return calls are named by direction ("middle
   right," "return left," "sideline/boundary"). Punt "return wall" is already cross-referenced.
2. **The kicker is the returner's man.** In hat math, the 11th hat (the kicker) is not "unblocked" in the
   coaching sense: he is assigned to the returner, who has to beat him one on one. Add a sentence to the hat
   math paragraph.
3. **Backside pursuit (l.819-822).** "The coverage players farthest from the ball sprint across the field ...
   they are the ones the return cannot afford to block" is muddled. They are the ones the return *chooses* not
   to block. Coverage teaches them to pursue flat to the ball but stay behind it, keeping the cutback lane
   (lane integrity), not to run straight across. Rewrite along those lines.
4. **Penalties as the hidden cost of returns.** Blockers start face to face with cover men who use rip and
   swim moves at 5 yards. Holding and illegal blocks in the back (10 yards, and from the spot on the return)
   wipe out a large share of good returns. Early movement by either unit is a 5-yard illegal-formation foul and
   a re-kick (6-1-3 penalty). One sentence in the "ceiling is low" bullet would cover it.
5. **Personnel shift.** With contact at 5 yards and no wedge, staffs moved toward bigger setup-zone bodies
   (tight ends, fullbacks, linebackers) on the return front line. "Mostly backups" (l.223) is fine, but one
   clause on the size trend fits the "a return is a run play" theme.
6. **Directional kicking.** Kicking to a corner of the landing zone uses the sideline as a twelfth defender
   and dictates the return call. It is the other half of the kicker's menu, alongside depth and trajectory.
   One line under menu item 2.

## D. Film room

- Saints 2024 (Grupe, first nine kicks at or inside the 5; best opponent drive start): well chosen and
  accurate. Fix the "what to notice" wording (A1).
- Seattle 2025: accurate. Myers took all 103 of Seattle's 2025 regular-season kickoffs (checked in pbp), so
  "kicked off for them" stands.
- Bears 2024 Week 1 double team: well chosen. A coach would add that the pulled blocker had to be a
  setup-zone player for the double team to be legal (A2).
- Super Bowl XLIV "Ambush": accurate (trailing 10-6 at the half, Morstead, ball off Hank Baskett, Saints
  recovery, touchdown drive). Good contrast with declared onside kicks.

## E. Gridiron use

Sensible. Simulated tracking is labeled "simulated, BDB-format", and the real-data path is shown in an
`eval: false` cell. Helpers `wait_until`/`to` reach into private `Play._compile()`/`Play._cur()`, which is
fragile if the library changes. Mention it in the notes; no change needed now.
