# Coach / film review: 12-08 Case Study: Fangio's Two-High Revolution and Macdonald's Answer

Reviewed 2026-10-08 from the source and the built PDF (`pdfs/12-08-two-high-to-macdonald.pdf`, 21 pages,
rasterized to `_pdfbuild/12-08-two-high-to-macdonald/`; diagram pages re-rendered at 130 dpi). Every figure was
looked at: fig-tite-quarters (p4), fig-one-shell (p6), fig-personnel (p10), fig-double-lie strip (p11),
fig-lx (p12), tbl-fingerprint (p14), fig-scatter (p15), fig-staffs (p17), drills 1-3 (p18-19).

Overall, this is a strong chapter. The five-decision structure is how a defensive staff would teach this
system, the Macdonald correction about sims (built on his own quote plus the FTN proxy) is excellent, and the
Super Bowl LX breakdown is the right film to use. The items below are ranked by severity. Items 1-4 are
accuracy problems a coach would catch on the first read.

---

## Must fix

### 1. The 2018 Bears nickel did not have "one linebacker behind them"
Film room, Chicago 2018 (line ~756): "Hicks and Goldman inside, Mack and Leonard Floyd standing up on the edges,
and one linebacker behind them: the tite against three-receiver sets."

That is not what the 2018 Bears put on the field. Against 11 personnel, Fangio's Chicago nickel was a
**2-4-5**: two interior linemen (Hicks plus Goldman or Bilal Nichols/Jonathan Bullard), Mack and Floyd as
stand-up edges, **both inside linebackers, Danny Trevathan and Roquan Smith** (each played roughly 90% of
snaps), and Bryce Callahan at nickel. The 2024 Eagles did the same: Carter with Davis or Milton Williams inside,
Sweat and Nolan Smith on the edges, **Zack Baun and Nakobe Dean** both off the ball, and DeJean at nickel.
In Fangio's system the five-man tite with a single linebacker (the "3-3-5" call in 05-03's glossary) shows up
far more in base personnel (3-4 tite against 12/21) and in Staley- and Evero-style packages than as Chicago's
or Philadelphia's everyday nickel.

Fix (choose one):
- **Minimal:** rewrite the film-room sentence: "Hicks and Goldman inside, Mack and Floyd standing up on the
  edges, Trevathan and Roquan Smith behind them: six in the box against three-receiver sets, the two inside
  linemen often in 4i-techniques so the guards can't climb cleanly." Add a sentence to Decision 2: "Fangio's
  everyday nickel usually kept two inside linebackers and took the nose off (a 2-4-5, see 05-03). The
  five-man tite with one linebacker is the same idea pushed further, and it is his base-defense picture."
- **Better:** keep fig-tite-quarters as the five-man tite but label it truthfully ("the tite: Fangio's base
  front, and the five-man nickel his tree (Staley, Evero) leaned on"), or add a small inset or second panel
  showing the 2-4-5 version (LE at a 5, L at a 4i, R at a 4i, RE at a 9 over Y, Mike at (4.7, +1.6), Will at
  (4.7, -1.8), nickel, corners, safeties). The box count stays six against six, so none of the argument changes.

### 2. "The box stayed light" contradicts its own number (Super Bowl LX bullets)
The rendered text says New England's designed runs met six or fewer in the box on **4 of 13**. That means
nine of thirteen runs met seven or more, so the box was *not* light in that game. Either the heading is
wrong or the metric is. Fix: retitle the bullet "**The run never mattered.**" and say it straight: "Seattle
loaded the box on most of New England's 13 designed runs (seven or more on 9 of them), running backs gained
42 yards, and once New England fell behind it stopped running." This also fits the "multiplicity includes the
option to be heavy" point from the fingerprint section, and it can be tied back to that point. The fig-lx
caption needs no change.

### 3. Drill 3 answer misses the main reason quarters exists
The answer offers three choices: stay and be outnumbered, bring a safety down before the snap, or "rotate a
safety down at the snap." Against 12 personnel with **both tight ends attached**, each quarters safety's #2
*is* that tight end. If the tight ends block, both safeties trigger as run fitters at once. That is the read
rule from Decision 4, not a rotation. So the defense really has **6 in the box + 2 read safeties = 8 fitters
against 7 blockers**, and those two arrive late from 12 yards. This is the classic "quarters is a nine-man
front" argument, and it is the strongest point the chapter can make here.

Fix: replace the third bullet with "**Let the reads do it.** Both safeties key the tight ends. If U and Y
block, both safeties fit (Y's side into the alley, U's side into the cutback), so the defense has eight run
defenders after the snap without showing them before it. The price is that the safeties arrive at four or
five yards, not at the line, and the play-action trap from Drill 1 is now available on both sides." Then
add the option real defenses use most, which the chapter itself documents (base on 29.7% of 2025 snaps):
"**Match personnel**: sub to base (a third linebacker or a 3-4 tite) when 12 comes on the field." Rotation
can stay as a fourth bullet, but it is not the main answer.

### 4. Double lie (fig-double-lie), panel 4: Y's seam is wide open
At +3.0 s, Y (the flexed TE) is about 19 yards deep at roughly w=+7.5 and **nobody is within 8 yards of him**.
FS finishes at (17, -0.5), RCB at (16, +15), and the dropped edge E sits at about 6.5 yards. Anyone who has
coached Cover 3 against 2x2 will see that the quarterback should throw the seam, not the dig. The figure
argues against its own lesson.

Fix (in `double_lie()`):
- The dropping edge is the seam-curl-flat player and must **wall #2**: `p.drop("RE", (9.5, 8.5), ...)` (collision
  and carry), not (6.5, 10.5).
- The deep-middle player shades to the two-receiver seam threat: `p.drop("FS", (18.0, 2.5), ...)`.
- Optionally stop Y's stem at 16-17 yards. Then re-check panel 4 so that the SS (robber) still meets the dig at
  about (12, 4).
- In the caption, add: "the dropped edge carries Y up the seam until the free safety takes him."

---

## Should fix

### 5. Quarters safeties are drawn bailing like Cover 4 spot-droppers (fig-tite-quarters, fig-one-shell B)
Both safeties backpedal straight from 12.5 to 17.5 yards, and the zone ellipses sit at 15-22 yards. Match-
quarters safeties play **flat-footed at 8-10 yards off the line of scrimmage to start**: they shuffle or slow-pedal
while reading #2, and they don't gain depth until #2 goes vertical. The drawing contradicts the label "read #2,
cover him or fit the run" and the text's whole run-fit argument. Fix: shorten the safeties' drops to about
(14.0, ±6.2) with a short arrow, and keep the deep-quarter shading. The corners can keep their bail. Optionally
add a small "read #2" tag at each safety's endpoint.

### 6. The tite claim "no free blockers to send up to the lone linebacker" overstates it (Decision 2)
With six blockers against a five-man tite, the five offensive linemen face three interior defenders plus the
left edge, so one lineman is free on paper (the guards are uncovered). The tite does not remove that free
blocker. It makes him *useless*: the 4i in the B gap and the 0 on the center force the uncovered guard to help
on a double or lose a gap, so he can't climb cleanly to the Mike. 05-03 draws it the right way ("Neither double
moves its man, so neither can send a blocker up"). Reword: "so the guards, uncovered on paper, are stuck helping
on the nose and the 4is and can't climb cleanly to the lone linebacker."

### 7. Cover 6 / Cover 8 terminology is stated two ways
The You'll-need box says "Fangio calls his version of Cover 6 Cover 8" (as does the 06-01 glossary entry:
Cover 8 = Fangio's name for quarters/Cover 2 split-field). Decision 4 says Cover 6 is QQH with the half *away*
from strength and Cover 8 is the version with the half *toward* the nickel. Pick one and say it once. The
MatchQuarters source supports the second. Suggested wording in the box: "Fangio has two names for split-field
coverage, Cover 6 (half away from the passing strength) and Cover 8 (half toward it); 06-01 treats 8 as his
generic term." Flag the 06-01 glossary line for whoever owns 06-01. Add a dialect note too: plenty of college
staffs (Saban's included) number these differently, with 6 meaning quarters to the field, half to the
boundary, and "7"/"Cover 6 Weak" variants.

### 8. Strength dialect in the "weak rotation" (fig-one-shell D)
In the drawn formation, passing strength (X and H) is on the left and run strength (attached Y) is on the right.
"Weak rotation, away from the passing strength" therefore brings the safety down **to the tight-end side**,
which is also the natural run-fit rotation (an eighth man to the TE). A coach would point this out because
staffs set strength in different ways (TE, field, or receiver count). Add one clause to the panel-D caption: "Weak
here means away from the two-receiver side, which in this formation is the tight end's side, so the rotating
safety also becomes the eighth run defender where the run strength is."

### 9. Drill 2 answer: "don't throw hot into the A gap the Mike vacates"
A quarterback doesn't throw "into the A gap." He throws hot to the **zone the blitzer vacates** (the short
middle/hook behind the mugged Mike). Reword: "don't throw hot to the short middle the Mike appears to vacate:
that is exactly where he drops." Add the classic sim-beater a coordinator would teach: **attack the dropper**.
When a defensive lineman or edge drops (here the right edge), the throw is to his zone: Y on a quick out/stick
or a seam that the dropped edge has to carry. This connects to prediction 4 in "What offenses do next."

### 10. Double-lie strip, smaller items
- Caption: "Four rush, from two places the offense didn't expect" is true of only one rusher (W). Say:
  "Four rush: one of them (W) a player the protection had to guess about, and two of the six it counted (M, E)
  in coverage."
- Panel 4: the W square sits on top of R, which reads as if the Will beat the back. Stop the Will's second
  segment at (-2.6, 2.4) and the back at (-3.3, 2.5) so the pickup is visible.
- Panel 2 and Drill 2 (fig-predict-2): the mugged Mike's square touches both T squares, and in Drill 2 his
  ring clips them. A mugged linebacker usually stands 1.5 yards off the ball, not in the line. Put him at
  d=1.7 (from 1.3/1.9) and keep w=-0.8. That is more realistic and clears the collision.
- Panel 3: the dropping E's square sits on Y's route line. This goes away once item 4 moves him inside to
  wall Y.

### 11. Personnel figure: "dime" is not necessarily three safeties
The fig-personnel caption says Seattle "lived in three-safety packages, big nickel and dime, on about seven snaps
in ten." The code's `dime (6+ DBs)` bucket does not check the safety count. Either say "five- and six-DB
packages built around a third safety (big nickel 56%) or a sixth DB (dime 16%)", or split dime by `saf >= 3`.

---

## Nice to have (nuance a coach would add)

- **Decision 3, who drops in the tite:** besides the TE-side edge, Fangio drops a 4i or the nose on
  "creeper"-style calls (07-03 owns the term; link it). One clause is enough.
- **Fig-tite-quarters:** match-quarters corners in this system usually align 8-9 yards off with outside
  leverage and bail. 7 off is fine, but "7 to 9 off, outside leverage" in the caption is more accurate.
- **Decision 5:** name the shell vocabulary once: "two-high = middle of the field open (MOFO), one-high =
  closed (MOFC)," linked to 06-01, which owns those terms. Readers will hear those acronyms on broadcasts and
  in film breakdowns.
- **Disguise audit timing:** column 1 "as the quarterback starts his cadence" captures the shell *before* the
  pre-snap spin that many defenses use about a second out. Suggest charting at "set" *and* at the snap (the
  center's head going down), so pre-snap and post-snap rotation can be told apart, which matches the caution
  in "What the data can't see."
- **Drill 1 answer:** when the offense motions Z into a wing or crack position, a match-quarters corner usually
  travels with him or "cancels" with the safety, so the extra blocker is not entirely free. One clause keeps
  this honest. Link 05-03's tite-vs-outside-zone figure as the reason the wide run is the answer.
- **Drill 3 figure:** the nickel at (5.5, -9) against two attached tight ends and no slot is fine as an apex,
  but a real staff would often walk him to 4 yards over the U's outside shoulder as a force player. It is
  optional, but if the answer adds him as a fitter, draw him there.
- **Big nickel tie-in:** in the double-lie and Drill 2, the nickel could be shown as Seattle's third safety
  (label stays "$", caption says "the nickel, here a third safety, as Seattle played it"). That links the
  diagram to the personnel argument right before it.

## Checked and fine
- Formations are all legal (7 on the line in every offensive set; X/Z on/off the ball correctly). Splits,
  depths and hash positions are realistic, and the safeties sit just outside the hashes at 12-13 yards.
- Fig-one-shell B/C/D: each panel accounts for 11 (4 rush, 7 cover), and the Cover 6 cloud corner and Cover 3
  4-under/3-deep structures are correct.
- Fig-lx, the table, the scatter and the staff box have no clipped or colliding labels. The ranks in the text
  match the table (e.g. 2018 Bears 21% blitz, 28th).
- Bio and tree facts were already verified by 12-08-factcheck.md. I found no football-technical errors
  beyond the above. The Dome Patrol, the 2018 Bears personnel names, the Eagles' 2024 interior and the
  Macdonald career line are right.
- Film-room selection (2018 Bears, 2024 Eagles + SB LIX, 2023 Ravens, SB LX) is well chosen. The "what to
  notice" prompts are concrete (find #14 before and one second after the snap; count rushers then watch
  the safeties).

## Rendering bug (not football, but visible)
Line ~877 starts with "2025. Seattle has them, ...". Pandoc reads it as an **ordered-list item numbered 2025**
inside the bullet, and it renders that way on p10 of the PDF. Reflow the line so "November 2025." does
not start a line (e.g. move "November" to the next line: "on Seattle radio in November 2025.").
