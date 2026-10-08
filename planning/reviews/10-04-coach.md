# 10-04 The Clock, the Two-Minute Drill, and Fourth Down: coach / film-analyst review

Reviewer role: veteran NFL coach and film analyst, checking technical accuracy and completeness. I read the
whole .qmd, rasterized `pdfs/10-04-clock-and-game-management.pdf` (all 25 pages at 60 dpi; pages 4, 6, 8, 9,
11-16, 18, 19 and 21-24 at 110-130 dpi) and looked at every figure. I spot-checked the film rooms against
nflverse pbp (SB LVIII regulation and OT, SB XXXVI, Falcons-Lions 2017, Eagles-Cowboys 2007). All of those
match the text.

**Verdict:** this is a strong, accurate chapter. The price list, the LVIII drive chart, the kneel chart and the
fair-catch-kick plate are what a game-management coach would actually show a staff. The clock rules,
spike rule, runoff, OT rules and fourth-down framing are right. There are two real errors (the kneel
threshold and the reasoning in Predict-1's answer). The other diagram fixes are about realism: the Hail Mary
catch point, how the prevent defense is set up, and the defense in Predict-3. There are also about eight
pieces of late-game nuance a coach would insist on.

---

## A. Must fix (wrong, or contradicts itself)

1. **The kneel-down threshold leaves out the fourth-down play clock** (fig-kneel-math, the l. 718 rule of
   thumb, the flowchart box, Watch-for-it, Takeaways). The beginner review flagged this too, and I agree it
   is the top fix. After the third kneel, the offense still has a full 40-second play clock before it must
   snap on fourth down. So the real "game over without a fourth-down snap" thresholds are about **2:43 / 2:04
   / 1:25 / ~0:47** for 0/1/2/3 defensive timeouts, not 2:03 / 1:24 / 0:45 / 0:45. Predict-2's answer already
   uses the extra 40 s and reaches "yes" from 1:40 with one timeout. A reader who uses the chart's "1:24"
   gets "no". Fix: give each bar a hatched "4th-down play clock (≈40 s)" segment, or put a "game over if
   time left ≤" tick on each row. Restate the rule in coaching terms: *after the two-minute warning, a first
   down ends the game if the defense has 0 or 1 timeout; with 2 it needs ≤ ~1:25; with 3, ≤ ~0:45.* That
   version is easier to use on the couch than the subtraction. Add one line on the fourth-down **"burn"
   play**: if a few seconds would remain, the QB takes the snap and runs backward or sideways, or a punt
   team burns the clock, instead of handing over the ball with time left.

2. **The arithmetic in Predict-1's answer contradicts the chapter's own price list** (l. 1495-1497). The text
   says a real play followed by a catch in bounds "would leave the offense needing to spike ... and perhaps
   ten seconds left, which is fine." Using the chapter's numbers: the completion was snapped at about 0:36.
   A hurry-up real play is snapped at about 0:15 (21 s). A catch in bounds ends around 0:10, and the spike
   needs another ~16 s from that snap, which is past 0:00. **That path loses the game**, which makes the
   case for the spike stronger. Rewrite it as "...would leave the clock running with about ten seconds and
   no way to stop it in time: game over." Also add the coaching point for the second-down play after the
   spike: it must be a *ball-out-fast, never-take-a-sack* call (quick out, or throw it away). A sack with no
   timeouts and about 0:15 left on a running clock ends the game.

3. **"The field-goal unit realistically can't run on ... while the clock is running"** (Predict-1 answer)
   is too absolute. Every NFL team practises a **running-clock field goal**, called a "fire FG", "hurry FG"
   or "field goal, field goal!" depending on the staff: the unit sprints on and kicks off a live clock, and
   about 12-18 s is enough. It is an emergency option, not a plan. Change the wording to "can run on with a
   running clock only in an emergency, and it needs roughly 15 seconds". This matters for the reader's
   predictions, because they *will* see it.

4. **The runoff paragraph contradicts itself** (l. 529-531). It says "A defense is never charged a runoff",
   then "a defensive time-saving foul can end the half." The beginner review flagged this as well. Either
   cut the second clause or state the actual Rule 4-7-3 mechanism in a concrete sentence. Have the
   fact-checker confirm the wording.

5. **The two-point chart's "+12" label is misleading** (fig-two-point-chart, `WHY[12]`). At up 13 the
   opponent *also* needs two touchdowns. The real gain from going is that two TDs with kicks now only **tie**
   instead of winning. Change the label to "→ up 14: two TDs only tie". Also consider **down 9**: it is
   marked "close", but kicking (down 8, one score with a two-pointer, ~94%) clearly beats 48% to reach down
   7 against 52% to stay down 9 (two scores). Every published chart and nfl4th say kick there. Mark it
   "kick". Up 10 is arguably at least "close": going to up 12 means TD + 2 + FG (11) no longer ties.

6. **"The spike costs about 1 second of clock ... That second cost is the real one"** (l. 495-496, as
   rendered). This is a "1 second / second cost" pun that reads like a typo. Change it to "about one second
   of clock, and a down. The down is the real cost."

## B. Diagrams

**fig-two-minute-menu (p. 4).** It is legal and readable: 7 on the line, CBs outside the receivers as the
text says, and labels well inside the window. Coach fixes:
- **R's "flat" route** is a 3-4 yard swing *behind* the LOS that stops near the left tackle (`r.flat(1.0,
  6.0)`). A flat route should get outside the numbers. Use about `flat(1.5, 11)` so it ends near w ≈ -12,
  where a catch can actually get out of bounds. That is the point of the figure.
- On the left the concept is H corner (high), X 12-yard out (middle) and R flat (low): a three-level flood
  without the usual clear-out. Name it in the caption ("a three-level flood to the left: corner over the
  squatting corner, out under the half-field safety, flat underneath"). A coach will recognise it, and the
  reader learns that two-minute calls are real concepts, not random sideline routes.
- Z's comeback at 15 against a Cover-2 corner who sinks is a low-percentage throw. It would be better
  against the off corner in Cover 3 or quarters. Either change the shell to quarters (the caption's "soft
  two-deep" still holds) or have Z run a 15-18-yard "hole shot" fade or go. Optional.

**fig-lviii-drive (p. 6).** It is accurate: every snap, clock, timeout and spot matches pbp `2023_22_SF_KC`.
- The **vertical nudges** (±4.5 yards on dots 5, 6, 8, 9, 10, 11) move dots off their real yard line. Dot 5
  (SF 43) is drawn near the 50. On a chart whose y-axis is field position, nudge horizontally (time) by
  1-2 s instead. Same-yard-line snaps 4/5 and 8/9 will then separate cleanly.
- The **"SF timeout at 0:10"** comes right after a play on which the pbp lists *two SF defensive backs
  injured* (J. Brown, D. Lenoir), with the clock already stopped by Kelce going out of bounds. The reader will
  ask why a defense calls a timeout on a stopped clock. Add a parenthetical, "(after two 49ers defenders
  were hurt on the play)". That is also a natural place to teach the injury-stoppage rule (see C4).

**fig-kneel-math (p. 8).** See A1. The visuals are otherwise clean.

**fig-victory (p. 9).** It is legal (U, LT, LG, C, RG, RT, Y on the line; Q, R, F, S off) and the labels
are clear. Small realism points:
- The QB is drawn 2.2 yards deep, which is a pistol-ish depth. Under center he should be about 1.2-1.4
  yards behind the ball, with the two up-backs at roughly -2.5 yards, ±1.2-1.5, on his hips. Real teams
  set them tight enough to wall off an A-gap shooter.
- Defense: a trailing team facing a kneel with timeouts left lines up tight (both safeties and corners
  within about 5 yards, everyone near the ball) to try for a strip. The drawn base 4-3 with safeties at 10
  is the "we've given up" look. That is fine for this figure, but **Predict-2 should use the tight,
  everyone-down look**, because there the defense still has a timeout and a reason to try.

**fig-hail-mary (p. 11).** The left panel is good. The close-ups contradict the caption:
- At **+6.3 s, X, H, Y and Z stand in one horizontal line** at the spot. The caption says "one man (Y)
  goes up for it, and the others position themselves in front of and behind him". Real teams name the
  roles: **jumper** (Y, at the spot), **front tipper** (H, about 3 yd short), **back tipper/trailer** (Z,
  about 3 yd deeper), and **two "sides"** (X and RB, about 3 yd left and right, short). Set the route
  endpoints so the frame shows that diamond.
- The defense ends up *in front of and below* the receivers. FS and SS finish short of the pile, and the
  three L droppers sit 7-8 yards short, out of the play. Real Hail Mary defense puts **2-3 DBs at or above
  the jump point** (its own jumpers, whose job is to bat the ball *down*, never tip it up) plus one
  "goalie" deeper. The underneath players collapse to the front of the pile to swat tips. Move FS/SS
  endpoints to SPOT ± 1 and up to SPOT + 1, and bring the L's to SPOT - 3/-4.
- The throw at 3.0 s is early. Most NFL Hail Marys from about 50+ yards are released at 4-6 s, with the QB
  climbing or drifting to buy time, because receivers need about 5 s to cover 45 yards. The current timing
  works for a simulation, but "throws at about three seconds" in the caption teaches the wrong number. Use
  4-4.5 s.
- Text, l. 877-879: the parenthetical about first-half risk ("a team that throws a Hail Mary from its own
  40 is risking very little") does not fit, because a throw from its own 40 is not Hail Mary range. Replace
  it with the real coaching point: *beyond Hail Mary range (about 60+ yards) teams switch to the
  hook-and-lateral or a multi-lateral "river" play.*

**fig-prevent (p. 12).**
- The structure is fine (3 rush, 4 deep at 21-24, 4 under at 9.5). But a real prevent defense is built to
  **take away the sideline**, because that is the throw that stops the clock. The diagram spreads the four
  underneath droppers evenly at w ≈ ±4.5 and ±13. Move the two outside droppers (U1, U4) to **w ≈ ±17-19 at
  10-12 yards with outside leverage** ("sideline sinks" or "cloud" players), and relabel: *"take away the
  sideline: make every catch happen inside, then tackle it."* That ties the figure to the chapter's main
  idea (offense pulls the ball outside, defense pushes it inside).
- The caption says "dashed zones", but the zones are drawn as filled ellipses. Also, the go routes end at
  about 18 yards, short of the deep zones. Draw them to 26+ so the "nothing over the top" relationship is
  visible.
- The RB route crosses behind the QB from his left to the right flat. That is fine, but the caption says
  "checkdown at 4 yards" while the route ends at about 8.5 yards deep (`(8.5, 8.5)`). Make them agree.

**fig-safety-plate (p. 13).**
- Panel A draws four rushers and **no punt protection**. Add the three-man shield (about 5 yards deep) and
  the line. Without them, "the rush has the shortest path" reads as "nobody blocks". The precise coaching
  point: a normal punter sets at 14-15 yards; at the 2 he can only be 11-12 deep (the end line). The rush is
  3-4 yards closer than usual, and **a bad snap or a muffed catch is a safety or a touchdown**. Say that in
  the label or caption.
- Panel B: "punter runs out of the end zone" sits next to the 20-yard line, about 20 yards from the punter.
  Move it next to his path (around x = 12-14).
- **Verify before printing:** "his blockers may hold on purpose: a hold in your own end zone costs only the
  safety." That was true for the Ravens in SB XLVII. Since then the league has given officials authority
  over clock manipulation through multiple fouls (Rule 4-7 and the unfair-acts provisions; I recall a
  2019-20 change). Have the fact-checker confirm whether the referee can now reset the clock after
  deliberate mass holding on a safety. If he can, soften to "historically, his blockers could hold on
  purpose...".

**fig-fck-plate (p. 14).**
- **Label collision:** the bold "fair catch, spotted at the DEN 47 / kick from the spot..." box overlaps the
  top of the defense's dashed 10-yard line and the top defender square. Move it to about x = 92, y = 38, or
  below the ball path.
- The left label "a field goal from a snap here: 47 + 18 = 65 yards" extends past the window's left edge
  (`window=(-14, 57)` starts at x = 49 and the text runs to about x = 46). Widen the window to `(-20, 57)`.
- Add the rule detail that makes the play safe: the defense **may not cross its line until the ball is
  kicked**, exactly like a kickoff. That is why there is "no realistic rush".

**fig-go-rate, fig-go-heatmap (pp. 15-16).** These are correct and clean. The text's reading of the heatmap
checks out (opp 30-39, fourth-and-3: 26% to 52%). One honest caveat to add to the heuristic "even
fourth-and-4 or 5 is usually a go there": the heatmap shows teams actually go about 30% of the time.
Phrase it as "the models usually say go; teams still go only about a third of the time."

**fig-two-point-chart (p. 18).** See A5. The WHY labels sit far below their boxes. Tighten the y-limits so
each note reads as part of its box.

**fig-ot-flow (p. 19).** This is correct for 2026. One case is missing: if **B's defense returns a turnover
for a touchdown** on A's first possession, B wins, because B has now possessed. The left branch says only
"safety". Change it to "B's defense scores (safety, or a return TD)". Optional strategy line under the 2026
onside rule: a kicking team could declare an onside kick to start OT, and recovering it uses up A's
"opportunity to possess". Recovery rates make that a curiosity rather than a strategy.

**fig-clock-flow (p. 21).** Fine. Once A1 is fixed, update the kneel box numbers. Add a fourth option to
the "Tight" box: "or get out of bounds (play call)". The cheapest stoppage is a sideline throw *called*
with the clock running.

**Predict-1 (p. 22).** The offense is drawn fully set in a 2x2 shotgun, but the caption says it is
"sprinting back to the line". More important, **the spike requires the QB under center**. A gun team that
is about to spike lines up with the QB under center, and that is *the* pre-snap tell a coach would teach.
Draw Q under center (d about -1.3) with some receivers still 1-3 yards off their spots, and label it "QB
under center from a gun team = spike coming". Then the drill trains a real cue.

**Predict-2 (p. 23).** Putting the victory formation in the question picture gives the answer away. Draw
the offense in a regular I or jumbo look, with the defense tight and everyone down (see the fig-victory
note), and keep the victory formation for the answer. The "defense: one timeout left" label sits on the
yellow line-to-gain. Drop it about 2 yards, or drop it entirely (the score bug already says it).

**Predict-3 (p. 24).** The defense on fourth-and-2 is a **soft nickel two-high** (safeties about 17 deep,
corners about 7 off). Hardly any DC plays that on fourth-and-2: expect press or squat corners, a rotated
single-high or Cover 0/1, and 6-7 in the box. Either (a) switch to `defense("nickel", "single_high")` with
the CBs pressed (d ≈ 1.5) and the SS walked down to about 6, or (b) keep the soft shell and *use* it in the
answer: "the defense is daring them to throw the quick stick or hitch, so expect exactly that." Right now
the shell goes unremarked and looks like a default.

## C. Nuance a coach would insist on (add a sentence or two each)

1. **First downs do not stop the NFL clock.** In college they stop it briefly. Readers who watch Saturdays
   will expect it. One line in the out-of-bounds section, or a "Madden vs. real life" aside.
2. **The two-minute warning is a free timeout.** Trailing offenses plan around it, for example by snapping
   at about 2:05 so the warning stops the clock after the play. Leading offenses try to burn to it. The
   chapter mentions it only inside the kneel arithmetic.
3. **The half cannot end on an accepted defensive foul.** The offense gets an untimed down. It cannot be
   extended for an offensive foul. This is central to the Hail Mary and the prevent (defenders are coached
   never to hold or commit pass interference on the last play) and to the fair-catch-kick extension
   already mentioned.
4. **An injury inside 2:00 is a clock rule.** After the two-minute warning, an injury stoppage costs the
   injured player's team a timeout, or a 10-second runoff if it has none. This deters faked injuries. It
   belongs in the runoff section and explains LVIII's 0:10 timeout (B, fig-lviii-drive). Have the
   fact-checker confirm the exact wording of Rule 4.
5. **The spike needs the QB under center.** Shotgun teams move the QB under center to spike, and a spike
   from the gun is grounding. The rule quoted in the footnote ("T-Formation Quarterback") already says
   this. Put it in the body: it is the tell (see the Predict-1 fix).
6. **Communication:** the coach-to-QB radio cuts out with 15 seconds on the play clock. That is why
   two-minute offenses use **"clock" plays** and a call sheet on the wristband: the QB has to call the next
   play himself. The bullet at l. 421 implies the radio is always available.
7. **Four-minute ball-carrier technique:** the RB "goes down" in bounds, and the QB slides or takes the sack
   in bounds rather than throwing it away. Leading by 1-8 late, the QB is coached to *take* the sack rather
   than throw incomplete. That is the exact mirror of the two-minute rule "no sacks", and a good symmetry
   line for the reader.
8. **Terminology dialects** (one sentence somewhere): the hurry-up goes by "NASCAR", "Indy", "Sugar" or
   "lightning". A spike call is "clock" or "clock it". The four-minute offense is also the "four-minute
   drill" or "kill the clock". The Hail Mary has team names ("Rocket", "Big Ben", "Jump ball"). The
   running-clock field goal is "fire FG" (not to be confused with the "fire" call on a botched snap). The
   prevent often appears as "dime" or "quarter" personnel in "max", "umbrella" or "prevent quarters".
   Readers will hear these on broadcasts and in coach interviews.

## D. Film rooms

- **SB LVIII regulation:** accurate. One addition a coach would make in "Notice also what San Francisco
  did before the drive": the 49ers threw **incomplete on third-and-5 at 2:00** (pbp) before the 53-yard
  field goal. A run in bounds would have made Kansas City spend a timeout or lose about 40 s. That is the
  most-cited 49ers clock decision of the game, and it fits the chapter's thesis. Note: the 49ers'
  third-down call is the critique, not the kick.
- **SB LVIII OT:** accurate (SF drive 15:00 to 7:25; KC fourth-and-1 at its own 34 at 6:05, a KC timeout
  before it; Mahomes 19 on third-and-1; Hardman TD snapped at 0:06, the game ending at 0:03). Worth adding:
  KC **burned a timeout before the fourth-and-1** (6:05 in pbp). The "information" side still spends
  resources.
- **Falcons-Lions 2017:** accurate. Good choice.
- **SB XXXVI:** the sequence matches pbp exactly (spikes at 0:41 and 0:07). A nice detail to point out: the
  0:41 spike came on *first down* after an in-bounds catch, the textbook spike that the spike section
  describes.
- **Westbrook 2007:** matches pbp (Dallas timeout #3 at 2:19, kneels at 2:00, 1:15 and 0:30). It is also the
  cleanest live illustration of the A1 fix: three kneels from 2:00 with 0 timeouts, with the play clock
  used fully each time.
- **Reid critiques:** fair and well framed ("both drives scored; the problem was the price"). "Four or five
  minutes" saved by hurrying overstates it, because several of those snaps followed incompletions or went
  out of bounds with the clock already stopped. Say "two to three minutes" unless you compute it from pbp
  (sum of gaps after in-bounds plays × (1 - 20/40)).
- **Lions NFC Championship:** accurate. Add that the first decision (fourth-and-2 at the 28) was a
  **46-yard** kick and the second (fourth-and-3 at the 30) a **48-yarder**, so the reader can place both in
  the heatmap.

## E. gridiron use

- The local helpers (`say`, `lead`, `band`, `scorebug`, `show_play`) are sensible, and nothing in
  `gridiron/` needed editing. The custom-built Hail Mary print panel (`draw_frame` on cropped tracking) is
  a good pattern, but its endpoints need the B fixes.
- There is one animation, which is well within the limit of about 4. The Hail Mary is the right play to
  animate. The kneel-math or LVIII charts are better as static figures, as they are now.
