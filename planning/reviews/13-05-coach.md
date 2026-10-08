# Coach / film-analyst review: 13-05 Tracking Data and the Big Data Bowl

Reviewed 2026-10-08 against `pdfs/13-05-tracking-data-and-big-data-bowl.pdf`, built 08:51, after the qmd's last edit at 08:50. All 48 pages were rasterized and every figure was viewed (pp. 5, 7, 12, 14, 17 and 24 at 110 dpi). I also cross-checked 06-01 and 06-06 for alignment and terminology conventions.

**Verdict:** the data side is strong. The coordinate system, angle convention, standardising, alignment on events, the BDB column details, the separation caveats and the project traps are all correct and well taught. The weak spots are in the *football* of the simulated chapter play and in a few shell-definition thresholds. Those thresholds contradict the book's own coverage chapters, and a coach would catch them right away. None of this needs a gridiron edit; every fix below can be made in the chapter's code or text.

---

## A. Must fix (football is wrong or misleading)

### A1. Man matchups are backwards: a linebacker is locked on a slot WR and the nickel is on the TE
`chapter_play()` (l. 282) and `sim_coverage()` "man" (l. 1428) assign `NB -> Y` (the flexed TE) and `WILL -> H` (the slot WR). The chapter play then has the Will run across the whole formation with a WR in jet motion at 6 yd/s and trail him to the flat. No NFL defense would choose that matchup in Cover 1. The nickel is on the field to cover the slot receiver, and the TE goes to a linebacker or safety. 06-01's own figures put the nickel ($) on the slot WR and the SS on the TE (06-01 l. 1429, 1521).

**Fix:**
- Align the nickel over H in the left slot (about d 5.5, w -8.5, inside leverage) and use `p.man("NB", "H")`, so the nickel travels with the motion.
- Align the Will to the right, over or inside the flexed Y (about d 5, w +6), and use `p.man("WILL", "Y")`. A safety on Y also works, but the SS is the robber here, so the Will is the cleaner choice.
- Keep the Mike as the RB/hole player.
- Do the same in `sim_coverage()`: `("NB","H"), ("WILL","Y")`.

**Text to update afterwards:**
- the chapter-play paragraph (l. 249: "the nickel and the Will linebacker play man");
- the fig-chapter-play-diagram caption (dotted-line list);
- the fig-chapter-play caption ("the Will linebacker (W) travelling across with him");
- the fig-separation caption ("the Will linebacker who followed him");
- fig-motion: the caption and the bottom panel, which should highlight `NB` instead of `WILL`, with the label "nickel";
- the "If a defender moves across the field with the motion man" paragraph.

A DB running across with the motion is the classic man tell anyway. It also teaches the right picture.

Drill 1 (zone) can keep the Will/Mike bump. That bump is correct zone behaviour.

### A2. The two-high depth cutoff (11 yd, "12 to 14 yards") contradicts the book and real alignments
L. 1324 says that with two high safeties the second-deepest defender is "about 12 to 14 yards". The team chart and Project 3 use "above about 11 yards means two-high". NFL two-high safeties routinely align 9–12 yards deep, and quarters safeties often sit 8–10 so they can fit the run. 06-01's own two-high example is "two safeties about 10 yards deep" (06-01 l. 1485). An 11-yard depth cut would call most quarters looks one-high.

**Fix:** define the shell with width as well as depth. For example: two-high when the two deepest defenders inside the widest receivers are each 9 yards or more deep, on opposite sides of the ball, and each about 3 yards or more from the middle (on or outside the hash). One-high when the deepest is within about 3 yards of the middle and the second-deepest is under about 9 yards or on the same side.

Change the prose to "usually 10 to 14 yards, quarters often shallower". In the team-chart sim, draw two-high depths from about 9.5–14 so the clusters overlap the way they will in real data. Also align the Watch-for-it, which says "count the safeties deeper than about 10 yards" (l. 1698), with whatever cutoff you choose.

### A3. The team chart conflates "shell at the snap" with "coverage played"
Fig-safety-depth-teams says that "each team's mix of shells is real", but the mix is taken from *post-snap coverage labels* (COVER_2/2_MAN/COVER_4/COVER_6). That is exactly the gap this book teaches as disguise. A team that shows two-high and rotates to Cover 3 gets counted one-high here, while its at-the-snap depth would be two-high.

**Fix:** reword the lead-in (l. 1326–1329) and the caption to say "each team's share of two-high *coverages played* (charted after the snap), used as a stand-in for its shell at the snap." Add one sentence noting that late-rotation teams will show *more* two-high at the snap than this, and that the gap is Project 3. (Optional: also say the two-high label set leaves out any Cover 9 / Cover 2-invert style codes if they exist in that season's labels. Check `defense_coverage_type.unique()` for 2022.)

### A4. "Buzz" is not a two-high-to-two-high rotation
L. 1318: "a 'buzz' or 'cloud' rotation changes who has which zone without changing the shell". 06-06 (l. 302–304, 555) defines buzz as a safety rotating down to the curl, which is a rotation *into Cover 3*, one-high. Cloud is the corner squatting to the flat, which can stay two-high on that side.

**Fix:** use "a cloud rotation, or an invert Cover 2 (safeties fill the flats while the corners bail to the deep halves)". Link [cloud rotation](../../appendices/glossary.qmd#gl-cloud-rotation). Note that the invert case breaks the "two deepest defenders before the snap are the safeties" rule, because the deep defenders after the snap are corners. That is a good concrete warning for the real-data step.

### A5. The comeback route and the throw timing are off
`chapter_play()` l. 280: `r.path((14, 0), (11.5, 2.5), (8.5, 2.0))`. Z works back 5.5 yards to 8.5 yards, and his last leg drifts back *inside* (w 2.5 → 2.0). A pro comeback is stemmed to 12–15+ and broken at about 45° back toward the sideline, and the catch is made about 2–3 yards back from the break (11–13 yards). Coaches teach "come back toward the sideline, never drift inside", because drifting inside lets the corner undercut the ball.

The throw comes at 1.95 s from a 2.5-yard gun drop and arrives about 3.2 s, so the ball is in the air for more than 1.2 s. A 14-yard comeback is normally a gun 3-step-and-hitch timing throw, released about 2.2–2.5 s at the top of the stem, with about 0.8–1.0 s of flight.

**Fix:** `p.route("Z", r.comeback(14))`, which is the library's own (14,0)→(11.5,2.5) and is already used in `ROUTE_MENU`, or `r.path((15,0),(12.5,3.0))`. Set `t_throw` to about 2.3 and `dropback(3.0)`. Then re-check that the separation narrative still holds (blanketed at the top, about 3–4 yd mid-flight, closing to about 1.5 at the catch), and update the numbers in the fig-separation caption, the "two lessons" paragraph and the l. 690 sentence.

The text is also inconsistent about the release point:
- l. 251: "the ball leaves his hand as Z starts his break";
- l. 690: "releases the ball before Z has broken";
- fig-separation: "at the top of his stem".

Pick one wording. "Releases as Z reaches the top of his stem, before the break" is what a timing comeback is.

---

## B. Should fix (diagram quality, realism, nuance)

### B1. Frame strip (fig-chapter-play) skips the key moment, and labels collide
`times=[-1.5, 0.0, 1.5, T_ARR]`. The rotation is complete by about 1.0 s. The chapter's teaching point here is the release before the break, and the strip doesn't show the throw. Use `times=[-1.5, 0.0, T_THROW, T_ARR]` and caption the third panel "throw: rotation done, Z at the top of his stem".

In the +3.2 s panel:
- the RCB "C" box sits on top of Z and the ball;
- the LCB box sits on X at the top edge (X is only about 1.5 yd inside the window);
- the "$" box touches Y in both post-snap panels.

Tight man coverage makes some overlap unavoidable. Still, pass a wider `lateral_pad` or window through `**kw` if `frame_strip` accepts it, or accept the overlap and say "the corner is on Z's hip" in the caption. The A1 fix will also move the nickel off Y.

### B2. Pocket figure: the back is drawn on top of the left tackle
Fig-pocket (p. 24): at the throw, "R" overlaps the LT circle. `p.block("RB", pts=[(0.3, -1.0)])` moves the back toward the LT's kick-slide lane. A gun back in pass pro steps up to check the A/B gap at about QB depth minus 1, inside the tackle's set. Use `pts=[(1.0, 0.5)]` (up and slightly inside), or keep him beside the QB. Check that the hull figure has no marker overlap afterwards.

### B3. Off-man corners give up the cushion far too early (library artifact, visible in two places)
`p.man()` shrinks the initial cushion to 20% by 1.44 s whatever the route depth. As a result:
- **Fig-separation:** Z's nearest defender is about 0.3 yd at 1.2 s, when Z is only about 9 yards into a 14-yard stem.
- **Drill 3 (fig-drill-rows):** at 0.7 s the LCB ("A") is about 1 yd in front of X, who has already "eaten" 6 of the 7 yards of cushion.

A 7-yard off-man corner keeps about 2–3 yd of cushion until the receiver is at 10–12 yards (the speed-turn point). The answer text calls A "giving ground in off coverage before he turns", but the picture shows a beaten corner.

**Chapter-side fix:** author the two corners' paths by hand with `p.drop(...)` waypoints. For the RCB vs the comeback: backpedal to about (10, 15.5) by 1.2 s, open to about (13, 16) by 2.0 s, then drive to the break point at about (11.5, 17.5). For the LCB on X's go: backpedal, then turn and run. Or keep `man()` and edit the caption to say "the simulator's man defenders close the cushion faster than real off-man corners". Note this for the gridiron maintainer as well (man() needs a cushion-vs-depth model or a `cushion=` parameter).

### B4. Free safety "from the left hash" is actually 7.5 yards off the middle
With the ball in the middle, the NFL hashes are about 3.1 yd from the middle, so w = ±7.5 is about 4.4 yd outside the hash, between the hash and the numbers. That is wide for two-high vs 2x2. Late-rotation teams in particular "cheat" the post safety narrower so he can reach the middle. Either:
- move both safeties in `chapter_play()` to w ≈ ±5.5–6 (and use 4.5–7 in `sim_dropback`), or
- change the caption wording to "from outside the left hash".

Also note that the `nickel_vs_2x2` docstring, "outside the hashes", is correct, but the fig-chapter-play-diagram caption says "left hash".

### B5. Robber depth conflicts with 06-06
06-06 defines the robber as a safety in the hole "10–12 yards deep" (l. 298) and puts the SS at "about 11 yards" (l. 579). Here the robber finishes at 9 (`SS -> (9.0, 2.0)`, rot1 at 8–10.5), and `rotation_onset()` requires the other safety to end shallower than 11. Either move the robber to about 10 and raise the rule threshold to about 12, or say once that robber depth varies from 8 to 12 by call and by down and distance. As written, a robber at 06-06's 11 yards would make the rule fail.

### B6. Orientation nuance: shoulders vs eyes, and QB posture
- Fig-orientation hard-codes the QB's `o` = 90 for the whole drop, and the caption states "faces downfield (o ≈ 90°)" as fact. A right-handed QB drops and sets with his front (left) shoulder toward the target. His chest therefore faces partly toward the offense's right, and in real data `o` will sit well off 90 and swing as he works through his progressions. Add a half-sentence: "(simulated; a real right-handed QB's chest turns toward his right as he sets to throw, so expect `o` well off 90)".
- L. 498–501: in off-*man*, a corner's eyes are on the receiver, not the QB. In off-*zone* (Cover 3), corners commonly bail or shuffle with their hips open about 45°, not a square backpedal. `o` is the chest and shoulders, not the eyes. Suggested wording: "A corner in off coverage gives ground with his shoulders square to the line ... A zone defender keeps his shoulders open to the quarterback as he drops; a man defender turns his shoulders to run with his receiver. Note that `o` is the chest, not the eyes: a man corner looking at the receiver's hips and a zone corner reading the quarterback can have the same `o`."

### B7. The motion rule's legality statement is slightly off
L. 957: "Linemen and the quarterback are excluded; they can't legally be in motion." The rule a coach would cite: only one player may be in motion at the snap; he must be a backfield (off-the-line) player; and he may not be moving toward the line. Players on the line, including split ends and attached TEs, can't be moving at the snap. A shotgun QB *can* legally move laterally; it is just rare.

Suggested wording: "Linemen can't be moving at the snap and the quarterback almost never is, so exclude them as noise. Only one player, an off-the-ball player, may be in motion, and not toward the line." Then add a one-line data-quality check: more than one skill player above the threshold at the snap means a shift that wasn't set for a full second, a flag, or a labelling or tracking problem.

### B8. Route classifier: "his sideline" should be relative to the ball, not the field centre
`route_features()` (l. 1519) and the fig-routes plot use `y < FIELD_WIDTH/2` to decide which way is "out". On a hash play, a slot aligned to the boundary side of the ball but on the field side of centre gets the wrong sign, so his out becomes an "in". Use the ball's y at the snap (`ball_y`). Even better, use the receiver's side of the ball at the snap, which also handles H after motion. It works in the simulation only because the ball is in the middle.

Also tell the reader that `routeRan` uses PFF's label set, which as I recall includes HITCH, OUT, FLAT, CROSS, GO, SLANT, SCREEN, CORNER, IN, ANGLE, POST and WHEEL (check this against the files). So "dig" maps to IN, drags and shallows to CROSS, and the flat, screen, angle and wheel classes need rules of their own. That is a real trap for a first attempt.

### B9. Drill 2 answer: "Cover 2 or quarters" should be Cover 2
Both deep players finish 15–18 yards deep and about 10 yards either side of the middle at +2 s. That is a halves bail: Cover 2 or 2-Man. Quarters safeties stay shallower (about 10–13) and inside the slot receivers, reading #2. They would not be 18 deep and at the numbers at 2 s. **Fix:** "two deep halves: Cover 2 (or 2-Man); quarters safeties would sit shallower and inside, reading the slot."

### B10. The Seattle film room isn't about Seattle
"Film room: Seattle Seahawks 2025" gives only league-wide NGS rates, and "watch Seattle's safeties" points to 12-08. The cited NFL.com piece is titled "The coverage that turned the Seahawks into Super Bowl winners". If it gives Seattle's own split-safety or Cover 4 rate, quote it, so the box has one Seattle-specific number and one Seattle-specific thing to notice. One example: Macdonald's safeties holding a two-high look into the cadence, then the post-snap rotation timing that the onset measure captures. Verify against the article before writing it in. Otherwise retitle the box "Film room: the league in 2025".

### B11. Minor consistency points
- **Label vocabulary.** The drill-1 strip labels the corners "CB" (via `nickel_vs_2x2` `label="CB"`), but the Predict-the-play legend (l. 1716) says "C a cornerback", and the chapter play uses "C". Use `label="C"`.
- **Sim comment.** `sim_coverage` says "two deep/robber" (l. 1427), but the setup is one deep (FS) plus two robbers (Mike and SS): "Cover 1 with a double robber (rat + robber); the back blocks."
- **"Every line starts high" (fig-separation).** H's line starts at about 3 yd, below the "5 to 8 yards off" range. Say "most lines start high".
- **"A defense with both high" (l. 1285).** This is ambiguous next to "two-high". Say "high on both numbers".
- **Chapter-play description (l. 244).** Say "with the tight end flexed into the right slot", so the reader isn't looking for an attached TE. The formation is legal: X, Z and the five OL make seven on the line, and Y and H are off the ball. Good.
- **Fig-standardise panels (a) and (b).** The "Z" and "QB" labels nearly touch. Nudge Z's label above its marker in those panels.

### B12. Nuance a coach would add on separation (one or two sentences)
Season separation reflects the *play-caller* as well as the receiver. Motion, stacks, bunches, condensed splits and play-action manufacture free releases and open throws (the Shanahan and McVay offenses). Alignment role matters too: a boundary X who sees press and the opponent's top corner, like Higgins, will measure low. That belongs in the Higgins film room ("what to notice") next to the catch-point point, which is well characterized.

---

## C. Checked and correct (no change)
- **Coordinate figure.** x 0–120, y 0–53.3; hashes at 23.6 / 29.75 (70'9"); angles clockwise from +y with dx = sin and dy = cos; 25-yard lines at x = 35 / 85. The labels sit inside the frame.
- **Standardising.** The rotation-not-mirror explanation and figure are right; X stays on the QB's left in (c) and (d).
- **Raw-row reading.** In a left-going play the defender faces +x (o ≈ 90) and backpedals toward x = 0 (dir ≈ 270). Correct.
- **Drill 3.** The A/B/C reading is correct for the numbers shown (A: o 272 / dir 100, a backpedal; B: dir 154, toward the offense's right; C: s 0.5, ignore dir), apart from the cushion issue in B3.
- **Rotation figures.** Fig-rotation-one, fig-safety-rotation and fig-rotation-onset are clean, with labels inside and no collisions. They are consistent with 06-06's figure (same seed and story). The divergence framing and the "a simulation gives back only the timings it was given" honesty are good.
- **Drill 1.** H's jet path between the OL and QB, legal lateral motion, and the Will/Mike bump plus the nickel widening are all sensible zone responses. The answer's "which zone?" caveat is exactly right.
- **Motion definitions.** Shift = everyone reset, then set for one second. The FTN vs PFF definitional difference is handled well.
- **Pocket caveats.** Pressure from the front, blocked vs unblocked rushers, and ESPN PRWR at 2.5 s are all good.
- **Project 1 trap.** Pattern-match, split-field, and splitting by game are all good. Cover 3 landmarks are reasonable: corners deep thirds about 16 deep, nickel and Will curl-flat at 7–8, Mike and SS hooks at about 9, seam-carry by the curl-flat player.
- **Other sections.** The BDB table, history and "what winners have in common" read accurately, and the eval:false real-data cells are sensible.
- **Animations.** 2 in total (the chapter play and Drill 1), within the limit of 4.
- **FACTS note.** FACTS-current §8 still says the 2027 BDB was "not announced as of 2026-10-06". The chapter (per the fact-check) says it launched Oct 7, 2026. That is consistent with the newer finding, but FACTS-current should be updated by whoever owns it.
