# 03-02 Zone Running: coach / film-analyst review (round 2)

Reviewer role: veteran NFL coach and film analyst. Scope: football correctness, every diagram (I rasterized
`pdfs/03-02-zone-running.pdf` at 110 to 250 dpi and looked at all 16 figures), animation timing (I re-simulated
both frame strips with `Play.to_tracking()` to get exact positions), missing nuance, film room, and code. I did not edit the chapter.

**Overall:** the revision fixed almost every round-1 P1. Rule 2 is now worded correctly (head-up or play-side,
with the dialect note). The odd front pairs C and LG on the nose. Drill 1 is legal. The EPA chart is now RB/FB
only. The IZ Y-RT combo, the duo, tight-zone, mid-zone and slice notes, the cutback player and the boot routes are all in.
The text is now sound football throughout. What remains is mostly in the **diagrams**: two new
football-misleading pictures (the boot's backside end and the cutback-player panel), one caption that
contradicts its figure, a gap mislabel in the cutback strip, and three round-1 diagram items that were only
half fixed.

Priority: **P1** = misleading football, fix before publishing; **P2** = a coach would object; **P3** = polish.

---

## P1: must fix

### 1. Boot figure: the "end chases the fake" finishes at the quarterback's feet (@fig-zone-boot, l. 1249)
`go_to(p, "BE", (-3.0, -0.5), ...)` ends 3 yards deep behind the LG/C, which is right on the QB's roll path
(the QB passes about (-4, -1.5), about a yard away). The picture says "the end has the QB." The whole point of the caption is the opposite:
the end chased the *back* and is now behind a QB rolling away from him.
**Fix:** send him flat down the line onto the RB's track, play-side of the mesh:
`go_to(p, "BE", (-2.2, 2.6), "path", via=[(0.4, -3.6), (-1.0, -2.6), (-1.9, 0.2)])`.
Move the `point_to` target to `(-1.9, 0.6)`. Check that his arrow ends right of the Q ring and the QB's
arrow runs away from him.
Same panel: the **Y's crosser starts by running through the play-side 5-technique** (first leg `(2.5, -0.8)` goes
straight into the 5's box). Real crossers bluff-block or slip inside the end. Use
`p.route("Y", [(0, 0), (1.2, -1.0), (4.5, -4.0), (7.0, -8.0), (7.5, -12.5)])` so he releases inside the 5,
under the flowing linebackers.

### 2. "Cutback player" panel: the Will is the LG's climb assignment, and the QB is standing in the bend lane (@fig-zone-defense right panel, l. 1172-1185)
- On outside zone right against this front, the LG is uncovered and his rule is to climb to the Will
  (see @fig-outside-zone-assignments). Here every OL just side-steps, so the Will looks unblocked by design. A
  coach reads this as a bust, not a defensive tactic. The real reason a backside-LB cutback player wins is that he
  plays *fast and downhill into the backside A gap before the LG can climb to him* (or the defense uses a safety the
  scheme cannot block).
  **Fix:** draw the LG's attempt: `go_to(p, "LG", (1.4, -0.3), via=[(-0.3, -0.9)])` (he steps play-side and is late),
  move the Will to `(1.0, -1.1)` (into the A gap, at the LOS, beating the climb), and relabel to
  "Will plays fast into the backside A gap before the LG can climb." Alternatively, rotate the FS down to
  `(5.0, -2.0)` as the cutback player and label it "safety rotates down: a defender the line can't block." Either
  version is honest. The current one is not.
- The QB never moves, and the bend branch `(-1.9, 1.0) → (-0.6, -0.9)` runs through his spot. Add the same QB action
  as elsewhere (`go_to(p, "QB", (-3.6, 1.8), "path", speed=3.2); go_to(p, "QB", (-6.0, -5.0), "path", delay=0.15)`)
  in both panels, or drop the QB from this figure.

### 3. Inside-zone caption contradicts the figure (@fig-inside-zone, l. 432)
The caption says "X, H and Z are receivers here (H is a slot receiver) and are not drawn", but all three are
drawn, and the text (l. 470) points the reader to "the H standing on that side in the picture." **Fix:** "X, H and Z are
receivers (H is a slot receiver on the left, too wide to block the end)."

### 4. Cutback strip: the back cuts back through the backside **A** gap, not the B gap, and the press is never shown (@fig-cutback, l. 933-941)
Simulated positions: the back crosses the LOS at about t=2.4 s at **w ≈ -0.7**, between where the C and the LG
started. That is the backside A gap. Frame 5's note and the caption both say "backside B gap". At t=1.5 s (frame 3,
"back presses the Y: no room") he is already at w=3.9 heading back inside. His widest point (w≈4.7, at about 1.25 s) is
never shown, and the Y has already moved to w≈6.9, so "presses the Y's outside leg" is not visible in any frame.
**Fix (minimal):** relabel to "backside A gap" in the note and the caption (the bend bullet already allows A or B).
Retime to `[0.0, 0.75, 1.25, 1.9, 2.45, 2.95]` with notes
`["snap", "handoff; everyone flows right", "back presses: no room", "plant, cut back behind the C",
"through the backside A gap", "the safety must make the tackle"]`. To make the press read as "the Y's outside leg",
widen the press waypoints to `(-1.9, 5.6), (-1.6, 5.2)`.
Also: the cut blockers end *behind* the LOS and never touch their men (`LT → (-0.4, -2.3)`, `U → (-0.4, -4.1)`,
while BT/BE stand at d=0.9). A cut block goes *forward* at the thighs. End them at `(0.5, -2.4)` and `(0.5, -4.2)`.

---

## P2: a coach would object

### 5. Overtake blocks are still invisible at print size (@fig-outside-zone-assignments l. 586-587; @fig-outside-zone-odd l. 758-759)
The green dashed overtakes (C on the 1, RT on the 5; RG on the 4i, C on the nose) render as 2-4 px stubs hidden
under the RG/Y lines and the defender boxes. This is round-1 item 9, and the figure exists to teach it.
**Fix:** draw them as visible wraps that end *play-side* of the defender:
`overtake(fld, p, "RT", [(-0.4, 3.9), (0.1, 5.0)], (0.9, 5.6))`,
`overtake(fld, p, "C", [(-0.4, 0.5), (0.1, 1.3)], (0.9, 1.8))`;
odd front: `overtake(fld, p, "RG", [(-0.5, 2.0), (0.1, 2.8)], (0.9, 3.2))`,
`overtake(fld, p, "C", [(-0.4, 0.3), (0.2, 0.8)], (0.9, 1.0))`. Use lw=2.4 and put a small "overtake" tag
between C and RG. Also give the odd-front RT a visible "hands on the 4i" first point:
`go_to(p, "RT", (3.4, 3.0), via=[(0.5, 2.4)])`.

### 6. OZ animation: the back brushes his own RT, and the 1-technique is never overtaken (@fig-outside-zone-animation, `oz_play`)
Simulated: from 1.8 to 2.4 s the back runs at w=4.7 while the RT sits at w=5.9 (markers overlap in frame 5). The C finishes at
(0.5, 1.3), *inside* the 1 at (1.3, 1.9), after the RG has left. So the 1 is free in frame 6.
**Fix:** RB `via=[(-4.4, 2.4), (-1.4, 5.1), (0.4, 4.4)]`, end `(6.6, 4.4)` (crease centered between the RG/Mike at 3.2 and
the RT at 5.9). C: `go_to(p, "C", (1.0, 2.2), speed=2.2, via=[(-0.4, 0.9)])` so he ends play-side of the 1, and stop the
1 at `(1.2, 1.7)`. The timing is now realistic (handoff 0.75 s, back at the LOS about 1.75 s); keep it.

### 7. Drill 3: the backside end's arrow still runs through the LT (@fig-predict-3, l. 1641)
The via `(0.3, -3.6) → (-2.0, -2.0)` crosses the LOS at w≈-3.0, which is the LT's spot. An end who beats the U's
cut-off crashes through the C gap (between U and LT), then flattens behind the heels.
**Fix:** `go_to(p, "BE", (-3.0, 1.4), "path", via=[(0.3, -4.0), (-1.3, -3.9), (-2.5, -1.6)])`.

### 8. Insert panel: wording and overlapping tracks (@fig-zone-tags, l. 1047, 1052-1058)
The H at (-3.6, -1.8) is an **offset fullback**, 2.5 yards behind an under-center QB, not "beside the quarterback".
Caption: "the H (here an offset fullback)". His path and the RB's converge on the same point behind the RG. Shift the
H's entry to `via=[(-2.6, 0.6), (0.3, 2.1)]` and end `(3.8, 1.8)`, and start the RB's track a beat later
(`delay=0.2`) so the lead is visibly ahead of the back.

### 9. Drill 2 answer: name the Sam's fit (l. 1616-1625)
With a wide 9 and the Sam stacked behind the RT, the C gap the answer sends the back into is *the Sam's gap*.
The bang works only if the uncovered RT climbs to the Sam (he has no one on him or play-side). Add one sentence:
"Who blocks the Sam? The right tackle, uncovered, climbs straight to him; if he gets there, bang; if the Sam beats
him into the C gap, the back bends."

---

## P3: nuance and polish

10. **Super Bowl XXXII film room:** "this one is all Gibbs zone" overstates it. Say "dominated by Gibbs zone." Denver
    also ran some gap and play-action looks. Davis's TD runs are fine examples.
11. **Pre-snap tell worth one bullet in "Watch for it":** OL splits. Wide-zone teams often tighten splits (it
    shortens the reach), and an under-center back at 7+ yards points to outside zone/boot. One clause each, with the
    usual "varies by team."
12. **Web video loses the cut blocks.** On HTML, `zone_animation` calls `show_animation(play)` without the `down`
    fading or the notes, so online the backside 3 and 5 just stand at the LOS while the back cuts past them. Either
    add the strip to the HTML too, or add `p.note("LT and U cut the 3 and 5", at=(-2.5, -6.0))` to the play.
13. **EPA prose:** "only 1 team(s) averaged above zero" reads as code output. Pluralize it with an inline
    conditional (`"team" if n_pos == 1 else "teams"`).
14. **Split zone H path** (l. 1000): `d=-1.9` is behind the mesh line of the OL heels but deeper than "just behind
    the linemen's heels." Use `-1.4` for both crossing waypoints. It still clears the shotgun mesh (≈ -4).
15. **Penetration panel dead code** (l. 1155-1156): the `BE`/`PE` `moved()` calls reassign the same widths
    `even_front(-1)` already gives. Delete them, or the comment misleads a reader who copies the cell.

## Film room
Picks and characterizations are good: 1998 Broncos/SB XXXII, the 2019 NFCCG with the zone-vs-gap drill caveat, 2025
Seahawks consistent with FACTS-current, and McCaffrey correctly framed as a contrast rather than the one-cut archetype.
McVay's Rams and LaFleur's Packers appear only in the tree paragraph and the ESPN 70.3% stat. That is acceptable.

## Code and gridiron use
- Sensible use: `Play`/`Player`/`technique`/`to_tracking`/`show_animation`, fronts built by hand, `p.read()`,
  and an `eval: false` BDB cell with real API names (`bdb.load_tracking`, `bdb.prepare`).
- Round-1 private imports are gone. Remaining private use is `p._cur(key)` in `go_to()`. **Gridiron gap to report:** a
  public `Play.current(key)` (end of the player's last action), or `absolute=True` on `block()` like `run()`/`path()`
  already have. Then `go_to` disappears.
- Still-relevant gridiron requests: `frame_strip`/`show_animation` should take `lateral=`/`window=`, per-frame
  `notes`, `rings=`, and a "player down from t" state (the chapter reimplements all of these in its 45-line `strip()`).
  `Field` should clip its own texts so `clean()` isn't needed.

## Round-1 items now resolved (keep)
Rule 2 wording and dialect note; odd-front C+LG on the nose and U hinge; Drill 1 legality; split-zone H path in
front of the mesh; bend paths routed behind the 1 with his flow arrow; EPA RB/FB filter and caption; boot route depths
(flat/cross/over); RT-Y combo on IZ; tight zone/mid zone/slice/back-away/duo box; cutback player, spill/squeeze; cut-block
frequency today; OZ second read named; insert-on-backside clause; OZ handoff timing.
