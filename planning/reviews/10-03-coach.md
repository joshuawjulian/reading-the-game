# 10-03 coach / film-analyst review: Red Zone, Goal Line, Two-Point Plays, and Short Yardage

Reviewed: `chapters/10-situational-football/10-03-red-zone-goal-line-and-short-yardage.qmd` (1,790 lines)
and `pdfs/10-03-red-zone-goal-line-and-short-yardage.pdf` (22 pp., built 2026-10-08 05:48, newer than the
.qmd). All 15 figures were rasterized at 110 dpi and looked at (`_pdfbuild/10-03-.../coachrev/hi*.png`).

**Verdict.** This is a strong chapter. The compressed-field argument, the leverage lesson (fade or slant,
not both), the rub-versus-pick line, the history of assisting the runner, the ban vote and the sneak data
are all accurate and taught well. Every spec item is present: all six diagram types, the Eagles, Allen and
Brady examples, and the 2025 vote with its 2026 follow-up. Three items must be fixed: a data bug that
inflates the headline red-zone number, a back-shoulder diagram whose catch is not a touchdown, and a
label clash that has offense and defense both using T and W in five figures. The other items are route
spacing, timing and terminology polish.

---

## MUST FIX

### 1. The red-zone trip count includes extra-point and two-point plays (data bug, verified)

`_rz = PB[PB["yardline_100"] <= 20].groupby([...fixed_drive])` runs on **all** of PB. That includes the
extra-point kick, which is snapped from the 15 (`yardline_100` = 15), and the two-point try, snapped from
the 2. Two errors follow:
- Every touchdown scored from outside the 20 counts as a "red-zone trip," because its PAT is snapped from
  the 15. That inflates the TD share.
- After a pick-six or fumble return, the defense's PAT is logged with the *defense* as `posteam` on the
  turnover drive. That creates "red-zone trips" whose result is "Opp touchdown." I checked five of them:
  each is a PAT or 2-pt try after a defensive score (e.g. NE pass intercepted at its own 15, then MIA's
  PAT).

I recomputed with only scrimmage runs and passes (`play_type in run/pass`, `down.notna()`,
`two_point_attempt != 1`):

| | chapter (as built) | corrected |
|---|---|---|
| drives | 8,603 | **6,881** |
| touchdown | 60% | **57.5%** |
| field goal | 26% | **29.3%** |
| turnover / on downs | 4% / 4% | 5.2% / 5.0% |
| "Opp touchdown" | ~3% | **0.3%** |
| missed FG / end of half / punt | 1.5 / 1.5 / <1 | 1.8 / 1.0 / 0.03 |

**Fix:** build `_rz` from `PLAYS[PLAYS["two_point_attempt"].ne(1)]`. `two_point_attempt` must be added to
`_cols`; scrimmage plays only. Then update footnote `[^rz]`, whose breakdown currently names a 3% "Opp
touchdown" bucket that is an artifact. The takeaway sentence "about six red-zone trips in ten end in
touchdowns" becomes "a little under six in ten." The same contamination, in a smaller dose, affects
`_t` (end-zone throw completion: two-point passes from the 2 are included) and `CV` (coverage near the goal
line). Add `PB["two_point_attempt"].ne(1)` to both.

### 2. Fig 4 (back-shoulder): the catch is short of the goal line

From the 8 (goal line at d = 8), X's route is `(2.5,-17.3) → (7.8,-17.8) → (6.6,-19.4)` and the throw ends
at `(6.4,-19.7)`. That is a catch at the **1.5-yard line**, not a touchdown. On third-and-goal that is a
failed play, so the picture teaches the wrong landmark. In the red zone the back-shoulder is thrown to be
caught **in the end zone**, usually one to two yards deep near the sideline. The receiver gets his feet
down before he is carried out the back or side.
**Fix:**
- X's stem goes to about d = 10.5, his break comes back to about (9.3, -19.6), and the throw ends at about
  (9.2, -19.8).
- The corner's branch runs to about d = 12.5 so he is visibly carried past.
- Change the caption from "catches it near the goal line" to "catches it a yard or two deep in the end
  zone".
- Optional coaching line: "Short of the goal line, a back-shoulder catch is just a first-and-goal."

### 3. One letter means two players: offensive T and W versus defensive T and W

The diagram key says T is a defensive tackle and W the Will linebacker, and R is the running back. But:
- **Fig 9** (goal-line fronts) labels the offensive tailback **T** and the offensive wing **W**, on the same
  picture as defensive T's and a W linebacker.
- **Figs 10, 11 and 15** (sneak, tush push, predict 3) label the offensive wing **W** while the defense has
  a **W** linebacker. The Fig 11 caption even says "the linebackers (M, W) come forward."

A beginner cannot tell them apart in print, where both are just letters.
**Fix:** tailback → **R** (as the key says). Wing → **H** (H-back), and add "H can also be an H-back/wing"
to the key. Alternatively use **Y2** or **U2**. This affects `jumbo()`, `sneak_off()` and the captions of
Figs 9 and 10.

---

## SHOULD FIX (diagram football)

### 4. Fig 5 left (slant from the 5): H's route runs into the slant window

H, the slot at w = -9, runs `(6.0,-9.0) → (11.5,-6.0)`. That is a vertical stem to the exact spot where
X's slant is caught, `(6.4,-9.8)`. Against man, the nickel follows H **into the slant's catch point**.
Against zone, H stands in the throwing lane. No coach draws that spacing.
**Fix:** make it the textbook **slant-flat**. H runs a flat to about (1.0, -16.5); the arrow can stay short
of the sideline. This pulls the $ outside and gives the reader the high-low that 04-03 already taught.
Alternatively, H runs a speed out at 3 yards. Link "slant" to
[Quick Game](../04-the-passing-game/04-03-quick-game.qmd) (slant-flat, beating press), not only to 04-01.

### 5. Fig 6 (stack rub, frame strip): the ball is released too early, and the cross is deep

- `p.pass_to("H", t=0.6)` from a 5-yard shotgun is not achievable. The snap alone takes about 0.3–0.4 s to
  arrive, and catch-and-throw needs another 0.4–0.5 s. Realistic release on a quick rub is **about
  1.0–1.2 s**. At 0.6 s, H has not yet cleared the traffic (panel 2 shows him still behind the LOS), so the
  strip reads like a throw to a covered man. **Fix:** throw at about 1.0 s, catch at about 2.0–2.1 s. Move
  the frame times to [0.0, 0.6, 1.0, 2.0] so panel 3 is "ball out" and the $ is visibly a step behind.
- Z's slant crosses the $'s path about 3–4 yards deep. The text says offenses "design the crossing to
  happen as close to the line as they can." **Fix:** align the $ at about 2.0 deep (not 3.4) and break Z at
  about 1.0 yard, so the "rub point" sits within about 1–2 yards. That matches the legal-pick lesson.
- The caption says "in the end zone near the pylon," but the catch is at w = 19.4, about 7 yards inside the
  sideline. Either say "toward the corner of the end zone" or push the catch to w ≈ 22. If you do, widen
  `RUB_LAT` to about 25.
- The text says "Watch the animation." In print this is a frame strip, so write "Watch the animation (the
  frame strip in print)."

### 6. Fig 8C (two-point sprint-out option): the QB's run lane goes through H

The green "or run" option path, from (-3.6, 8.0) to (2.2, 8.6), is drawn through H's starting marker at
(-1.5, 8.5). In a static picture it looks as if the QB runs into his own receiver.
**Fix:** run the option lane at about w = 10.5–11 (outside H's release), or align H at w = 10 and Z at
w = 14.5. Also: in 8C both Y (block to (0.4, 5.6)) and the RB (block to (-1.6, 6.4)) are aimed at the same
end (E at 6.4). Have Y **reach the end** and send the RB to **arc to the force/contain player**, or the
reverse (RB kicks the end, Y climbs to the Mike). Do not leave two blockers on one man while the $ is the
read.

### 7. Fig 8D (QB power): the hole is not the C gap, and the blocking is sloppy

- Y is attached at 4.65. The QB's path (`… (0.4,5.6) → (2.6,6.0)`) and the pull go **outside Y**, which is
  the D gap ("off the tight end's down block, inside the kick-out" in 03-04's words). The caption says "C
  gap." **Fix:** reword to "through the hole between the tight end's down block and the back's kick-out,"
  or move the kick-out inside so it really is the C gap. Keep the wording consistent with 03-04's QB-power
  figure.
- Y's block goes to (2.4, 3.0), 2.4 yards deep into empty grass. In power, Y **blocks down** (on the
  3-tech, double with the RT) or **climbs to the backside LB**. RG's block ends at (0.2, 0.6), basically
  standing. **Fix:** RT and Y double the 3-tech T (2.4) and climb. RG climbs to the Mike (3.5, 1.0). C
  blocks back. LG pulls for the play-side LB/$. RB kicks out the E. This mirrors 03-04, so the reader sees
  the same play.

### 8. Fig 4 (fade): X is aligned too far inside for the chapter's own rule

The text says a fade receiver aligns with "five to eight yards between himself and the sideline." In Fig 4,
X is at w = -17.0, which is about 9.7 yards from the sideline with the ball in the middle. Predict 1 uses
-19.5 (about 7 yards). **Fix:** X at about -19.5 and CB at about -18.7, matching Predict 1. Keep labels at
least 1.5 yards inside the window: the "over the outside shoulder" label is centred at -18.6 and would need
to move to about -17.

### 9. Fig 1 (red-zone map): "GOAL LINE inside the 5" sits beside the painted goal line

The label reads as if it names the line itself. **Fix:** "GOAL-LINE AREA / inside the 5" or "GOAL TO GO,
inside the 5." This is minor.

---

## TECHNICAL / TERMINOLOGY ACCURACY

### 10. COVER_9 counted as two-high: inconsistent with the rest of the book and with FACTS

`CV["two_high"]` includes `COVER_9`. But 06-01 defines Cover 9 as "on some staffs a Cover 3 with weak
rotation, Cover 3 match or split-field on others," and 06-06 and FACTS-current §10 count COVER_9 **in
neither group**. **Fix:** drop COVER_9 from both groups, or exclude it like BLOWN/COMBO, and say so in
`[^twohigh]`. The text "Cover 2, Cover 4 and their relatives" is fine once that is done.

### 11. Red-zone leverage: say *why* corners choose inside leverage

The chapter says the fade "beats exactly what the compressed field invites." A DB coach would put it the
other way round: **red-zone corners play inside leverage on purpose**. They use the sideline and end line
as help and concede the low-percentage fade to take away the high-percentage slant. Your own number (about
40% completion on outside end-zone throws, against 68% short) is the reason. Add one sentence to "The
slant, and leverage": "Defenses know the odds: most red-zone corners play inside, daring the offense to
complete the hardest throw on the field." The leverage lesson then becomes a two-sided bet rather than
an offensive trick.

### 12. "Compressed field" section: two freed-defender uses are missing

The chapter names three uses for the defenders the end line frees up (zones shrink, man/press, box fills).
Coaches would add two more:
- **Rob the middle.** A Cover 1 robber or lurk ("hole" player) sits at the goal line to kill slants and
  crossers. This is exactly the danger in the slant section.
- **Double the best target.** A bracket on the star TE or WR (Kelce, Kittle) becomes affordable when no
  one is needed deep.

Both are defined in 06-02 (robber/lurk, bracket), so link rather than redefine. One short paragraph would
cover it.

### 13. Super Bowl XLIX film room: the matching details are missing

This is accurate as written. But the play is the perfect bridge to Fig 6 and is not used:
- Seattle was in a **stack to the right**, with Kearse in front and Lockette behind. Browner pressed the
  front man and Butler was the off defender on the back man. That is the Fig 6 alignment, and Butler beat
  the rub from the off spot.
- **Personnel context** that coaches always cite (verify before printing): New England had its goal-line
  defense with three corners against Seattle's three-receiver personnel. Seattle said it threw because a
  pass against that personnel could use second down without burning its last timeout, and an incomplete
  pass stops the clock.

This ties to the goal-line personnel section ("defense matches the offense body for body"). Flag both for
fact-check if added.

### 14. Sneak blocking: use the coaching word

"The center and guards drive straight ahead … everyone else fires low and forward" describes **wedge**
blocking without naming it. Add "(coaches call this **wedge** blocking: every lineman drives toward the
center's hip so the pile has no seams)." Also note that the QB reads the center's hip or "follows his
butt," which is what `QB alone: follow the center` already hints at.

### 15. Tush push details a line coach would want

- **Splits.** `SNEAK_SPLIT = 1.5` is barely tighter than the chapter's normal 1.6. On the push, the
  Eagles' line goes nearly foot-to-foot, about 1.2–1.3 yards centre-to-centre. Try 1.3 with `mr=0.55`
  markers (Fig 11 already uses the smaller markers). Check for overlap.
- **Pusher depth.** P1 and P2 sit 1.4 yards behind the QB (-3.3 vs -1.9). On the real play they are
  practically touching his hips, about 0.8–1.0 yards. Move them to about -2.8.
- **Successors.** The Eagles film room says "Kelce retired after the 2023 season and the play kept
  working." Name **Cam Jurgens** (Kelce's successor at center from 2024) so the claim has a cause.
  Fact-check if added.
- **The 2025 officiating point of emphasis** is described as "false starts and how players line up." It
  helps to say concretely what that means: linemen moving before the snap, and players lining up in or
  across the neutral zone. Keep it as general as FACTS §5 allows.

### 16. Answer 3 uses "hard count" without a link

"Hard count" is owned by 01-05 (term index: `hard count -> 01-05`). Link it there:
`../01-foundations/01-05-the-pre-snap-phase.qmd`.

### 17. Snag is not linked

The Fig 8B caption and text use "snag triangle," but snag is defined and owned in 04-03 (Quick Game). Link
it at first use in the text: "the [snag](../04-the-passing-game/04-03-quick-game.qmd) triangle (B)."

### 18. "Sprint-out" is bolded but neither defined in the glossary nor linked

It is not in this chapter's key terms. Either drop the bold, or link the closest owner (04-05 boot/
play-action, or 04-08, which describes sprint-out systems). Do not add a glossary entry without a
term-index change.

---

## Checked and correct (no change)

- Geometry: 30/20/12 yards to the end line; PAT snapped from the 15 (a 33-yard kick); 2-pt try from the 2
  in the NFL and the 3 in college; 2015 change; defensive 2-pt return.
- Leverage teaching (inside: fade, outside: slant). Fade landmarks and release. Back-shoulder mechanics and
  the receiver's-head coaching point. Rodgers–Nelson characterization.
- Rub vs pick: the 1-yard rule, "run through the path, not at the man," banjo and jam answers.
- Shovel: unblocked play-side end, backside guard pull, inside flip; the NFL ineligible-downfield rule
  applies even to passes caught behind the line, unlike college. Fig 7 blocking (RT down on the 3-tech, C
  back, LT backside) is correct.
- Goal-line fronts (Fig 9): the 6-2 puts DL in A, C and D gaps and LBs in the B gaps (a true gap-8). The
  5-3 has a 0-tech nose, B-gap tackles, outside ends and three LBs. Legal 23-personnel offense with 7 on
  the line. 6+2+3 and 5+3+3 both make 11. "Low man wins," four-point stances and LBs over the top are all
  right.
- Sneak rationale: ball nearest the line, speed, QB as the extra hat. Quick-count note. Brady
  characterization.
- Tush-push frame strip: it tells the story in four panels; the timing (decided in about 1.2 s) and the
  scale (about 1.5 yards) are realistic.
- Assisting-the-runner history (2005/2006 dispute handled honestly), pulling still a 10-yard foul, Bush Push
  2005, NCAA 2013. Ban votes: tabled, then 22–10 on May 21, 2025, 24 needed; no 2026 proposal. Leaping is
  restricted only on kicks.
- Fig 12 (sneaks by team) is honest about noise (90% intervals, n ≥ 15). The volume-vs-rate and selection
  lessons are exactly right.
- Predict drills: all three pictures are legal and realistic. The answers read the right cues (3x1
  isolation fade with rotated help; tight bunch vs man with banjo as the counter; push alignment and the
  defense's snap-timing answers).
- Label clipping: no on-field label is cut by the window edge in any figure. Apart from item 3 (letters)
  and item 6 (the path through H), there are no collisions.
- Animations: 2 (rub, tush push), well under the cap.
