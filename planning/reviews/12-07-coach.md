# Coach / film review: 12-07 The Lions (Ben Johnson's offense, Campbell's aggression)

Reviewed 2026-10-08 against the rendered `pdfs/12-07-lions-ben-johnson-and-campbell.pdf` (built after the
latest .qmd edit), rasterized at 110 dpi. I looked at every figure. Two data checks were run in the rtg container
(results below). The chapter was not edited.

**Verdict.** The chapter is strong and close to pilot quality. The four-habit framing is right, the habit vs.
head-coach split in @fig-transfer is good teaching, and the fourth-down section is honest about selection and
diminishing returns. Three things must be fixed: one formation is illegal in the way it is used (Drill 3), one
diagram contradicts itself (the "bait" throw lands on the free safety), and one film-room example is
mischaracterized (Answer 2). After that, there are label collisions and some coaching nuance to add.

---

## MUST FIX

### 1. Drill 3 (`fig-predict-3`): the tight end the answer calls "most likely target" is covered (ineligible)
Current alignment: Z `O("Z","WR",-0.7,12.5)` is **on** the line outside Y (`-0.7, 4.8`), and X (`-1.5,-13`)
and Q (`-1.5,-8`) are both **off** it. The seven on the line are LT, LG, C, RG, RT, Y and Z, so **Y is covered and
can't catch a forward pass**. The answer says "the tight ends ... are eligible" and "the tight end on the line is
the most likely target". 02-02 teaches the covered-receiver rule with this exact picture, so a careful reader will
catch it.
- **Fix:** move X onto the line and Z off it: `O("X","WR",-0.7,-13.0)`, `O("Z","WR",-1.5,12.5)`. The line
  becomes X + 5 OL + Y = 7. Y is the end, so he's eligible; U (wing), Z, Q and R are backs. The defense needs no
  change. Optionally put an aqua ring on Y and U to show they're eligible, which is the point of the drill.

### 2. `fig-jumbo`, right panel ("the bait"): the throw lands on top of the free safety
Z's deep crosser ends at `(16.0, -5.0)` and the FS moves to `(17.5, -2.6)`. The catch point is about 2.7 yards
from the one defender the caption says X's post is holding, so the picture shows the opposite of the lesson. The
concept is the classic play-action **"Yankee"** (a post from one side and a deep over from the other), so draw it
the way a coach would. The post *holds* the middle-of-the-field safety, the corner bails deep outside, and the over
is caught **under the corner and outside the hash**, in the hole the bitten curl/flat defenders left.
- **Fix:** Z route `[(11.0, 9.0), (14.5, 2.0), (16.5, -10.0)]`, with `pass_to("Z", t≈2.8)`. FS `[(19.0, -3.0)]`
  (stays with the post). LCB bails to `[(21.0, -12.5)]` (deep third over the top). X's post
  `[(12.0,-12.0),(24.0,-4.0)]` is unchanged. Move the label "Z: deep crosser into the space they left" to the left
  side (about `(13.0, -9.0)`, inside the window), and name the concept in the caption ("a play-action 'Yankee'
  concept"). Check that the SS/LB label at `(9.4, 2.4)` still clears the new route.

### 3. Answer 2: the NFC Championship example doesn't support the answer it's attached to
The answer says to "expect a run or a quick play-action throw from under center", then cites Detroit's
fourth-and-2 at the SF 28 as "same reasoning, bad result". The FTN data (checked) shows that snap was **shotgun,
no play-action** ("(Shotgun) 16-J.Goff pass incomplete short left to 8-J.Reynolds", `qb_location = S`,
`is_play_action = False`). The fourth-and-3 that followed was also a shotgun dropback.
- **Fix:** either drop the sentence, or turn it around: "In the 2023 NFC Championship Game the fourth-and-2 from the
  49ers' 28 was a shotgun dropback, not the under-center look: the menu isn't one play."
- **Calibrate the claim with data.** My check of 2022–2024 regular-season fourth-and-1/2 attempts:
  Detroit n = 61, **61% under center** (league 52%), **passed on 46%** (league 41%), **play-action on 15%**
  (league 9%). So "heavy, under center, run or play-action" is the right *tendency* but overstates it: about a
  third were shotgun and almost half were passes. Say "more often than the league: under center, and a run or a
  play-action pass" and give the numbers.

---

## SHOULD FIX (diagram clarity)

### 4. Hook-and-lateral strip (`fig-hook-lateral`), panels 2 to 4: three defenders stack on Z and the labels are unreadable
At t = 1.65, 2.0 and 2.95, RCB, NB and SS converge on the same point, `(2.2–3.2, 13.3–14.1)`. "NB", "CB" and "SS"
overprint each other and Z's marker. The caption's whole point ("three defenders on the wrong man") is hard to see.
- **Fix:** keep them converging but stop them in a triangle around Z. RCB `[(2.8,15.2),(2.4,15.4)]` (outside
  leverage, squeezing from the sideline), NB `[(2.9,12.3),(2.6,12.6)]` (inside), SS `[(5.4,13.4),(4.4,14.0)]`
  (stays about 2.5 yards on top). Z sits at `(1.9,14.2)` in the middle.
- **Defender depths for the down.** The table row is 3rd-and-12 (the SF play), but `to_go=12` is drawn with the CB
  at 5.5 and the NB at 4.5. On 3rd-and-12 a coach expects sticks-aware depth: corners at 7–8 off, the nickel at
  6–7, safeties at 13–15. That depth is *why* a 2-yard hitch pulls everyone downhill, which is the habit the
  constraint attacks. Try `RCB (7.5, 15.0)`, `NB (6.5, 8.4)` and `SS (13.5, 10.0)`, and increase the defenders'
  speeds so they still arrive by the pitch. Say "on third-and-long the defense sits at the sticks and rallies
  forward" in the caption or the text.
- **Wording.** The caption says Z "runs a two-yard hitch toward the sideline". A hitch turns back to the
  quarterback (inside), and the code does that (`(2.3,14.6)→(1.9,14.2)`). Write "a two-yard hitch, turning back to
  the quarterback".
- **Timing (minor).** The catch is at 0.75 and the pitch at 1.95, so Z holds the ball 1.2 s. Real pitches come
  about 0.5–0.8 s after the catch, just as the first tackler closes. H is already level with Z at t = 1.65 in
  panel 2, so `pitch("H", t≈1.6)` would be truer to the play and also make panel 2 read better.

### 5. `fig-jumbo`, left panel ("the leak"): show it as a real boot concept
- **Add the other two levels.** On film, a boot has three: flat, crosser, deep. Right now U and X stand still, so
  the reader can't see *why* the flat is open. Give U (the backside, left end) a drag/crosser at 8–12 yards to the
  boot side: `go(p,"U",[(2.0,-3.0),(9.0,6.0),(11.0,11.0)],"route")`. Then 70 (flat), U (crosser) and Z (clear /
  deep) form the standard flood, and the throw to 70 is the "flat is open because the linebackers chased the fake"
  read.
- **The unblocked end.** The playside RE (`(1.0,5.6)`) is left alone once 70 releases, and the QB boots straight
  at him. That's correct for a naked or block-release boot, but say so: "70's count of blocking is all the
  protection the boot side gets; the throw has to come on time, or the QB pulls up." A coach would insist on this.
  It's also the defense's counter (see item 9).
- The label "linebackers chase the run fake" at `(6.0,-6.4)` sits right against the left CB's marker. Move it to
  about `(7.5,-4.5)`.

### 6. Shift-and-motion strip (`fig-shift-motion`): small overlaps
- **Panel 3.** The LBs slide only about 1.4 yards, so the dashed ghost W/M/S squares half-overlap the solid ones and
  read as clutter. Either drop LB ghosts in panel 3 (keep U, Z, RCB and the safeties) or make the slide bigger
  (Mike to w = 2.8, Will to w = −1.0, which is still realistic for a strength re-declare).
- **Panel 6.** U's ring sits on the Sam's square (it's a block, so contact is right), but the "S" is hidden. Stop U
  about 0.8 yards short, at `(2.4, 7.4)`.
- **Panel 2.** U at the wing `(-1.6, 6.4)` and the tightened Z `(-1.5, 9.0)` touch. That's a real "bunch" look, but
  the caption should say so ("Y, U and Z now form a tight bunch to the right"). Otherwise move Z to w = 10.
- **Football: correct.** The formation is legal before and after the shift (X + 5 OL + Y on the line). Everyone is
  set for 3.3 s before the jet starts, and the jet runner is moving only laterally at the snap (−3.0 depth,
  sideways), so nothing moves forward. The spin is correct: the motion goes left, so the left safety drops and the
  right safety goes to the middle. The run back to the vacated heavy side is the right payoff. Optional: name the
  run (it's drawn as zone-style, everyone stepping right). "Outside zone to the bunch side, behind U and Y" would
  connect it to 03-02.

---

## SHOULD FIX (coaching accuracy and nuance)

### 7. "Its base was familiar: a wide-zone and gap run game"
The Johnson-era Lions weren't a wide-zone-first (Shanahan-tree) team. Their identity runs were inside zone/duo and
gap schemes (counter, power, pin-and-pull) behind Sewell, Ragnow and the guards, with outside zone as one of
several. The "See also" line that calls the Shanahan tree "the other under-center, play-action family" is fine,
but don't imply the run base was the same. **Fix:** "an inside-zone, duo and gap run game (with outside zone in the
mix)". The fact-checker should confirm against a run-scheme charting source if one is cited. Otherwise keep it
generic: "a zone and gap run game".

### 8. Habit 1: name the under-center cost the quarterback pays
The text gives the dropback-depth cost. The bigger cost a QB coach names is that **on the fake the quarterback turns
his back to the defense and loses the coverage for about a second**, so he comes out of it re-reading. That's why
Johnson's play-action throws were mostly high-low reads to defined landmarks (the over, the post, the flat) rather
than full-field progressions. One sentence is enough.

### 9. "How opponents responded" is thin on what defenses actually did, and the Washington paragraph mischaracterizes the loss
- **Name the actual counters.** Defenses (a) kept the backside/boot-side end home ("boot-check" or squeeze, don't
  chase the fake), the standard answer to under-center boot; (b) assigned a linebacker or the walked-down safety to
  the reported lineman, so the leak was covered and the bait still had to beat the curl/flat player; (c) played
  more single-high, eight-man boxes and accepted the play-action risk (the chapter's 2-high number shows this;
  see the next bullet); (d) simplified their motion answers ("lock" or "kill" calls, no rotation) against shift +
  motion. Two or three sentences with these would make the section match the case-study shape ("how opponents
  responded").
- **The two-high number is weak support as written.** It's 36% vs. 39% league, 23rd. A 3-point gap on
  *dropbacks* is selection-biased: play-action dropbacks come on run downs, when defenses are single-high anyway.
  Either compute it on early-down plays (or all plays) or soften to "slightly less often than the league".
- **The divisional loss wasn't a scheme answer.** Calling the Washington game "the most effective response" credits
  the defense with a game decided by five Detroit turnovers, a pick-six included. A coach would also say why the
  Lions gave up 45: the defense had been gutted by injuries since midseason (Aidan Hutchinson broke his leg in the
  same October 2024 Dallas game the chapter cites; the fact-checker should confirm and cite). **Fix:** call it "the
  worst day" rather than "the most effective response", and keep "the bad tail arrived on the worst day".

### 10. Jumbo / reporting: one rule nuance worth a clause
The chapter mentions the Ragnow "ineligible downfield" flag on the Sewell lateral but doesn't connect it.
Play-action from jumbo is exactly where **run-blocking linemen drift more than a yard downfield** while a pass is
thrown beyond the line. That's a real, recurring cost of making a run look and a pass look identical. Add one
sentence to the Habit 2 cost or the "Why it exists" box. It also makes the Sewell footnote earn its place.

### 11. Shift/motion "Why it exists": one detail
"A defender who travels with motion suggests man" is the classic read, but by 2023–25 many defenses
"bumped" linebackers and safeties in zone too, which is partly why Johnson layered a shift first. Add half a
sentence: "less reliable than it used to be, since zone defenses now bump with motion too". It fits 02-06 / 06-06.

---

## Checked and correct (no change)
- **`fig-jumbo` formation:** 7 on the line (U, 5 OL, #70), with #70 the right end and eligible after reporting.
  X and Z are a legal yard off. The 8-man box (4 DL, S/M/W, SS) with a single-high FS and bailing corners is a
  sensible Cover 3 look against jumbo.
- **`fig-predict-1`:** same legal look, with the SS rolled to 6.2 outside #70. The answer (play-action away from
  the rolled safety, the leak as the backup) is how a coordinator would call it. The Week 18 2023 St. Brown
  example fits.
- **`fig-predict-2`:** the field-goal distance convention (+18) matches 10-04 (54-yard kick from the 36), and the
  "go zone" logic is right.
- **Timeline, fourth-down and transfer charts:** no clipped labels. Who held which job matches FACTS C1/§9. The
  "fourth-down habit stayed with the head coach" reading is fair.
- **Opening and film room (Decker/Skipper, Dec 30 2023):** accurately characterized, and the procedural lesson
  ("watch the safeties, not the lineman") is right.
- **Shift rule wording** (everyone set a full second after a shift, otherwise an illegal shift) is correct. The jet
  in the figure is legal at the snap.
- **Trick-play table:** the "constraint play" framing and the cost rows (WAS) are well chosen.

## Optional depth (only if words allow)
- The two-back packages (Gibbs + Montgomery on the field together) and the screen game to Gibbs were Johnson
  signatures that fit the "same players, many formations" theme better than motion volume does.
- Unbalanced "tackle over" looks with Sewell are the other side of the eligible-lineman coin (a lineman moved to
  make the formation lie, not to catch).

## Data checks run (container, nflverse + FTN)
- `2023_21_DET_SF` fourth downs: the 4th-and-2 at SF 28 was `(Shotgun)`, `qb_location S`, no PA. The 4th-and-3 at
  the 30 was also shotgun.
- DET 4th-and-1/2 go plays, 2022–24 REG (n = 61): U 61%, S 34%; dropback 46%; PA 15%. League: U 52%, dropback 41%,
  PA 9%.
