# 12-05 coach / film-analyst review: Ravens' option run game (2019–2025)

Reviewed: chapters/12-case-studies/12-05-ravens-lamar-run-game.qmd, rebuilt PDF (2026-10-08 07:00), all 11
figures viewed at 110 dpi (pdf pages 4, 6–11, 13, 18–20).

**Overall:** strong and technically sound. The box arithmetic is right in every figure: 7 + read v 8,
8 + read v 8, 6 + read v 6, and a +1 for the offense in Drill 3. The blocking rules on the power read are
correct: Y and RT block down, the double on the 3 climbs to the backside LB, the puller leads for the
play-side LB, and C blocks back on a backside shade. The voice matches the pilots. The fixes below are
ordered by importance. None of them is a rewrite.

## A. Must fix (accuracy)

1. **"The Ravens' runs gained [expected points], season after season" (data section, para 1) is false for
   2021.** Fig 5 shows BAL at about −0.02 EPA per designed run that year. Reword to "gained them in every
   season but 2021", or "beat the league average every season".
2. **QB counter blocking (fig-qb-counter, `qb_counter()`): the RG blocks back on a 1-technique shaded to the
   *backside* (DT1 at w = −0.7), while the C climbs past him to the Will.** That asks the RG to reach across
   the center's face to a man aligned on the far side of the ball. No counter rule does that. Standard
   counter (GT/GY) rules are: C blocks back on a backside A-gap shade, and the play-side guard with no down
   defender climbs to the backside LB. Swap them in code: `C -> (0.4, -0.6)` (back on the 1), and
   `RG -> (2.9, -2.2)` via `(-0.2, 1.0), (1.0, 0.0)` (to the Will). Update the code comments to match. The
   caption needs no change.
3. **"Pulling the backside tackle … leaves the backside end free to chase" (QB counter, "The pullers are a tight
   end and a guard").** This is misleading. On a GT counter the backside end is handled by the back, or by
   an H-back, anyway (03-04's shotgun version does exactly that). Suggested rewrite of the reason for GY/GH
   counter: pulling the tackle opens a hole in the backside B/C gap that has to be hinged or filled. Pulling the
   tight end keeps the tackle home on the 5, and the tight end is the better athlete for wrapping up to a
   linebacker in space. The back still takes the backside 9. The "eight against eight" count stands.
4. **Drill 3 answer: "two deep safeties and six underneath" is wrong.** With a four-man rush the defense has
   two deep and **five** underneath (NB, M, W, two CBs). Fix the number. The point survives unchanged.
5. **Playoff losses: calendar years vs season labels.** The text says "the Chargers in 2019 and the Titans in
   2020", but Fig 8 labels games by season (2018 LAC, 2019 TEN, **2020 TEN**, which was a *win*). Write "the
   January 2019 Chargers game and the January 2020 Titans game", or use season years throughout.
6. **"Look at the losses one at a time" skips the January 2021 loss at Buffalo (2020 BUF, 17–3).** A coach
   would name it, because it fits the thesis. Jackson's goal-line interception was returned 101 yards for a touchdown by Taron
   Johnson, and Jackson then left with a concussion, so Huntley finished. One sentence is enough; factcheck
   should verify the details. Also clarify "three in four of the six losses" (meaning unclear), and note that
   the six losses include the Huntley game.

## B. Diagram fixes

7. **Pistol inverted veer mesh (fig-pistol-iv, and the RB path in fig-drill-2).** The back's dashed path runs
   about 1.5 yards *behind* the quarterback (through (−5.6, 1.2), with Q at (−4, 0)), so no mesh is possible
   as drawn. Route it through the QB's play-side hip: `(-7,0) -> (-5.0,0.6) -> (-4.4,1.3) -> (-3.6,4.2) -> …`.
   From the pistol the back comes *around the play-side hip*, not "across his face" (that phrase is the
   shotgun version). Change the caption and the Drill 2 wording ("sweeping right around Jackson's hip").
8. **QB counter strip, panel 4 (t = 2.6):** the U ring, the Q ring and the M square overlap, so the label
   collides and the QB is level with his lead blocker instead of behind him. Add about 0.15 s to the QB run
   delay, or end the QB path about 1.5 yd behind and outside U (for example (4.6, 4.9)), so the panel shows U
   engaging the Mike with Jackson a step behind. **Panel 3 (t = 1.6):** Y is hidden under the LG/9/5 cluster.
   Let the squeezing 9 end at about w = 6.4 and the kick-out at (0.4, 6.0), so the guard meets him visibly
   *outside* the Y.
9. **Seven-DB figure (fig-seven-db):** the Ravens are drawn in **11 personnel**, which undercuts the story.
   Seven DBs against three receivers is just a big dime. The radical part of the Chargers' plan was playing
   seven DBs *against Baltimore's two- and three-tight-end sets*. Redraw the Ravens in pistol 12 or 21 personnel
   (add U inline left, or a FB/H; drop X/H). The box then reads **6 v 7 blockers + a read**, the defense
   conceding two hats, which is exactly the trade the text describes ("the defense concedes the box count").
   Update the caption and the "box:" label to match.
10. **Drill 1 text vs picture:** the stem says "the defense walks a safety down", but the picture is a 6-2 with
   no safety visible in the box (two 9s, two 5s, a 1, a 3, M, W). Either relabel the play-side 9 as `SS`
   (a walked-down safety playing the edge) or drop "walks a safety down" from the stem.
11. **Fig 5:** the "13th" rank label for 2021 sits on the league-average line and among the gray dots. Put it
   above the point (xytext +7) or to the right.
12. **Fig 3 (13 personnel):** the caption puts the lone WR "split wide, out of the picture". Say he is **off the
   line (flanker)**. If he is on the line outside Y, Y is covered and his seam route in the left panel is
   illegal. A similar one-line note belongs in "How to read the diagrams": receivers left out of the
   picture are assumed to be off the line, so the inline tight ends are the ends of the line.
13. *(Optional realism.)* Fig 1, left panel: with a pocket QB, most staffs would have U cut off the backside 9
   and leave the backside *linebacker* as the free man, rather than climb U and leave the end. The lesson
   (one unblocked defender, who is free to chase) is the same. Either keep it as is, or add "(or the
   backside linebacker)" to the caption.

## C. Missing nuance a coach would insist on

14. **Linebacker keys and the counter.** The IV section says LBs are "taught to follow a pulling guard", and
   the QB counter section says LBs follow the back's first step. Both are coached, but they are different keys,
   and the counter beats them differently. Backfield-flow LBs are beaten by the counter step. Guard-key LBs
   actually see the G + TE pull correctly, and what beats them is hesitation: the mesh fake and Jackson's
   keep threat freeze them for a beat, so they arrive late against a wrapping TE. Add two sentences.
15. **Defensive answers miss the most common in-game tactics:** (a) the **scrape / gap exchange** and the
   **mesh charge** (the end attacks the mesh to force a fast decision). These are linked from 03-04 but never
   applied to the Ravens. (b) **"Make the QB pay"**: give the keep and hit Jackson on every one, as a
   per-game tax. (c) **Late safety rotation**: fitting the alley from two-high depth after the snap. This is
   the Fangio-era answer, and the hook to 12-08. A short "and the everyday answers" paragraph under
   "How opponents responded" would cover them.
16. **Cover 0 vs Jackson (Answer 3):** add that zero against a running QB usually comes with
   **hug / green-dog** rushers (a man-defender rushes when his back stays in to block) and disciplined rush
   lanes. Without them, zero simply concedes the QB run. That is how Miami's November 2021 plan avoided
   giving Jackson the scramble.
17. **Perimeter on the power-read give:** both the caption and the text leave the alley player unblocked. Say
   who handles him: in 12 personnel the play-side WR (or a TE arc) blocks the corner/force player. Otherwise
   the give looks like a back against the whole secondary.
18. **The people up front:** the chapter credits scheme and QB, but a coach would name the 2019 line and lead
   blockers in one sentence: Ronnie Stanley, Marshal Yanda, Orlando Brown Jr., and FB Patrick Ricard as a lead
   blocker. Factcheck should verify. The 2021 dip also coincided with Stanley's lost season, alongside the RB
   injuries already cited (verify).
19. **"Watch for it" cues:** "Beside him: … expect the run (or the read) to go the other way" should say
   *usually*, for zone and zone-read. Gun gap runs often go to the back's side. Also add to the puller
   cue: G + TE pulling with the *back* following them = counter read or counter bash, not QB counter.
20. **Box definition:** "within about five yards" conflicts with the glossary's "5 to 7 yards deep". Use
   "about 5–7 yards".
21. **"What survives / The pistol didn't":** "the backfield of choice for read plays from under-center teams"
   is self-contradictory, because the pistol is not under center. Reword as "a change-up look that
   under-center-based offenses use when they want a read".

## D. Film room

- The TEN (January 2020) and KC (January 2024) film rooms are well chosen and accurately characterized as
  scoreboard and turnover losses.
- The "Baltimore 2019 (watching the pistol)" film room names no game. AUTHORING §2.6 asks for team, season and
  ideally the game and situation. Pick one specific 2019 game that shows the pistol power read or QB
  counter (pull it from pbp: Jackson designed runs with run_gap/run_location, week, quarter, and verify on
  film). Give the drive and quarter so the reader can find it.
- Consider one *positive* Henry-era film room, for example the 2024 wild card against PIT (Henry 186 yards),
  pointing at the under-center duo and the pistol-read change-up the data section describes.

## E. Data sanity checks (for factcheck / author)

- Fig 6, "fewer than 3 WRs": **86% in 2022**, between 48% (2021) and 43% (2023), looks like a labeling
  artifact (FB or RB counted differently in 2022 participation). Check it against an independent 11-personnel
  rate for the 2022 Ravens before quoting "86%" in text.
- Fig 6 pistol panel: the NGS 2022 point (33%) and the FTN 2023 point (7%) come from different sources. FTN
  2022 is already loaded (`QBLOC.loc[(2022, True), "P"]`), so plot it as a second 2022 marker. That way the
  2022→2023 drop is like-for-like, as it already is in the Monken bullet.

## Gridiron use

Sensible. Helpers are local to the chapter, as required, and `check_legal` is used on drawn players. The frame
strip is 4 panels and tells the story in print. There is only one animation. Labels sit inside the field
windows, and none is clipped by the field edge.
