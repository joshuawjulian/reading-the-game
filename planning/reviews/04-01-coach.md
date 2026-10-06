# Coach / film review: 04-01 Passing Game Fundamentals

Reviewed 2026-10-06 by a veteran NFL coach and film analyst. I rebuilt the chapter
(`build_pdfs.py 04-01-passing-fundamentals --html`: OK, 21 pages), rasterized every page at 110 dpi
and looked at all 14 figures and the table. Overall it is strong. The route definitions, the
drop-to-route pairing, the two kinds of read, the stretches, the air-yards and YAC section and both
film rooms are right and well pitched for this reader. The problems are mostly in the geometry of
four diagrams, where the picture teaches something a coach would correct in the meeting room. There
are also a few missing coaching points: landmarks and field versus boundary, hot routes, and the
different names systems use for the same route.

## A. Diagram fixes (must fix)

1. **fig-predict-corner (Predict 2, smash vs Cover 2). The drawing sends the throw straight to the safety.**
   - H's corner route ends at about (15.5, w = -15), and the FS is at (16, -11). The landing spot is
     4 yards from the deep-half safety, which contradicts the answer ("over the cornerback, in front
     of the safety").
   - Fix: a real smash corner bends toward the sideline, 3–5 yards inside it, at 18–20 deep. Use
     `pp.route("H", r.path((10.5, 0.0), (18.5, 11.0)))` so it lands near w ≈ -20 to -21. If the
     snapshot time stays at 1.9 s, check that H is still visibly breaking toward the sideline.
   - **The Cover 2 cornerback's leverage is also wrong.** LCB lines up at w = -14.5 and squats at
     w = -13.8, which is *inside* X (w = -16). A Cover 2 corner is the force player and keeps outside
     leverage: he jams, funnels #1 inside, and sits in the flat. Use
     `mv["LCB"] = (5.0, -17.5)` and squat to `(4.0, -17.0)`.
   - Caption: change "just inside X" to "just outside X, in front of the hitch."
2. **fig-horizontal-stretch: the Mike is not actually stretched.**
   - The back's sit spot is (9.4, w ≈ +0.6) and the Mike drops to (7.0, +1.6), so R sits in the
     Mike's lap rather than on one side of him.
   - Fix: sit R at about (5.5, -2.5). He then sits between W (w = -5) and M, and every underneath
     defender has a receiver on each side, as the caption claims.
   - Re-aim the two dotted "lean" lines from M to about (7.4, -1.0) and (7.4, 4.5).
   - The code comment says Y sits "at the hash", but Y finishes at w ≈ 5.5 and the hash is at 3.1.
     Either sit Y at w ≈ 4 or drop the word.
3. **fig-timing-route: the timing contradicts the chapter's own timing chart.**
   - The chart (fig-drop-timing) puts the intermediate throw at 1.85 s and the break at 1.95 s. The
     strip releases at 1.75 s and Z breaks at 2.2 s. That is 0.45 s early, about 3 yards before the
     break, which is extreme anticipation for a 12-yard out. Z also breaks at 13.5 yards, not 12.
   - Fix: `r.path((12.0, 0.0), (12.0, 9.5))` with Z timed to break at about 1.95–2.0 s, and
     `pass_to("Z", t=1.85)`. Re-pick `TIMES` (e.g. 0.9, 1.85, 2.0, catch) and update the prose
     ("13 or so yards", "at about 2.2 seconds").
   - In the last panel the CB box sits on top of Z's ring. End the drive at about (13.0, 21.0) so he
     is visibly a step behind and inside.
   - Optional coaching point: with Y blocking, the curl-flat SS has no #2 threat and is free to widen
     under the out. That is why the out against Cover 3 is usually paired with a flat route from #2
     (out-flat). One clause in the prose would cover it.
4. **fig-progressions: the full-field order is not one any staff would teach.**
   - The comeback (Z) is read 4, thrown late from the far hash. A comeback is a timing route that is
     dead once the corner recovers, and a late comeback across the field is the classic pick-six.
   - Fix: make Z a clear-out go with no number. The order becomes 1 X post (shot), 2 H dig, 3 Y curl,
     4 R checkdown. Alternatively, keep the comeback but make it read 1, left to right.
   - Half-field panel: the back's outlet runs through the RT/Y area. Release him outside the tackle
     to the flat (2 yards deep, w ≈ 10–12).
   - Half-field caption: "both reading the same cornerback" blurs the progression and defender-read
     ideas. Say the smash pair is read high to low off the cornerback, which is why the corner is 1
     and the hitch 2.
   - Both panels are tiny in print and R and Q touch. Stack the panels or make the figure taller, and
     offset the back to w = ±2.5.
5. **fig-off-tree: the wheel is not a wheel yet.**
   - It turns up at w ≈ 13.8, inside the numbers, with Z standing at w = 17 on the same side. A wheel
     goes up the sideline outside the numbers (w ≈ 19–21).
   - Fix: widen the vertical part to w ≈ 20. Add Z on a faded inside-breaking route (post or dig),
     or say in the text that #1 must clear inside for the wheel to have room. Every coach teaches the
     wheel with the clear-out attached.
6. **fig-option-route, man panel: the defender beats the route.**
   - The nickel's first waypoint is (5.6, 9.6), outside Y's stem (w = 8.5), *before* Y breaks. He has
     crossed over and undercut the out, which by the chapter's own rule means Y should have broken in.
   - Fix: keep him on the inside hip and trailing, e.g.
     `p.path("NB", [(5.0, 7.9), (6.0, 11.0)], absolute=True, speed=6.0, delay=0.25)`.
7. **fig-high-low strip: a label is in the wrong place.**
   - The "low" note is at (-3.8, 15.5), behind the line in the backfield, but it is meant to mark the
     flat route at about 3 yards. Move it to about (1.2, 20.5), next to the flat route's end.
8. **fig-route-tree: the label contradicts the chapter's own legend.**
   - The receiver is labelled Z but stands on the line (d = -0.7, the same as the center), and the
     legend says Z is the receiver off the line. Relabel him X, or set d = -1.5.

Checked and correct:
- Formations: 7 on the line. In Predict 1, X is cropped out of the window but is not needed.
- Hash marks at ±3.1.
- Cover 3 and Cover 2 shells and drops in the high-low and horizontal figures, apart from item 2.
- Predict 3 (flood: Z go, H out at 12, Y flat, X backside slant).
- Drop-depth chart.
- Animation count (2) and frame-strip storytelling.
- Labels sit inside the window everywhere else.

## B. Text accuracy and nuance

1. **Landmarks and field versus boundary (missing; a coach would insist).** No sentence says how
   the ball's position decides which routes go where.
   - Outs and comebacks usually go to the boundary (the short side), because the throw is shorter.
     The deep out from the far hash to the wide side is the NFL's arm-strength test throw.
   - Receivers keep a sideline rule: they stay 5–6 yards from the sideline so an out, comeback or
     fade has room to finish.
   - Route depths are measured from the line of scrimmage, not from the receiver's alignment.
   - Suggested place: two or three sentences after the out and comeback bullets, linking
     [the numbers](../../appendices/glossary.qmd#gl-the-numbers-alignment-landmark) and
     [reduced split](../../appendices/glossary.qmd#gl-reduced-split), both owned by 02-02.
2. **Hot routes and sight adjusts (missing link).** The slant is called "a staple when the defense
   brings extra rushers", but the hot throw is never named. One sentence in the slant bullet and one
   in "Reads" would fix it: against a blitz the quarterback's first check is the hot or sight
   adjustment, before any progression. Link
   [hot route](../../appendices/glossary.qmd#gl-hot-route) and
   [sight adjust](../../appendices/glossary.qmd#gl-sight-adjust) to 04-02, which owns both and
   exists.
3. **Kinds of break.** In the anatomy bullet "The break", add that breaks are either *speed*
   (rounded, no plant; quick outs against zone, to keep speed) or *sink and plant* (hard stop; deep
   outs and comebacks, to separate against man). Many NFL staffs teach the 12-yard out to break
   slightly back downhill toward 10–11 rather than dead square. That explains why the cheat-sheet
   "out, square" is only roughly true.
4. **Terminology dialects.** The chapter says names are "close to universal". They are close, but a
   reader will hear the following:
   - go / fly / streak / 9 (fade when it widens)
   - dig / square-in / in (and "basic" in some trees)
   - hitch / stop / quick hitch
   - curl versus hook (in some systems the hook turns straight back and the curl rounds inside)
   - corner / flag
   - skinny post / glance / bang-8
   - whip, a cousin of the pivot or return route
   - option / choice
   - high-low / hi-lo / levels
   A short "Same route, different names" line or callout would serve the "route caller" goal. The
   progression section could also note the system difference: Coryell-family reads go deep to short
   (a shot, then the intermediate, then the check), while Walsh-family reads often go short to deep in
   rhythm.
5. **Answer 1 overstates the seven-step drop.** "[The post] usually goes with a seven-step drop or
   with play-action" is dated. Today the post is thrown off a five-step drop with a hitch (three from
   the gun), often as the second read (dig-post, dagger), and the chapter itself says the seven-step
   is rare. Suggested wording: "it is usually a deeper read or a shot off play-action; as the first
   throw off a five-step drop, the out is the match."
6. **The route pairs.** "The curl and the corner make the same pair inside a single stem" is weak:
   no defender is really choosing between those two. Use pairs coaches actually teach, such as
   slant/sluggo (already in the chapter), hitch/hitch-and-go or post/post-corner.
7. **The slant is "the quickest-developing route in football."** It is tied with the hitch and the
   quick out. Say "one of the quickest".
8. **Option route rule.** Optionally add the third case: against head-up or off man, the receiver
   stems at the defender to make him declare, then breaks away. Many systems also tie the decision
   to the safeties: against one high safety (middle closed) he breaks away from leverage; against two
   high (middle open) he sits. MOFO and MOFC are owned by 06-01, so gloss and link them.
9. **Film room, SB XXIII.** Accurate as written; the fact-checker verified it. **Film room,
   2022 Brady and Mahomes.** Well chosen and fairly characterized. No changes.

## C. Things that are right and should stay

- The route definitions and depths match NFL teaching (Bowen tree). The odd-out and even-in rule is
  stated with the right hedges.
- Drop pairings: 3/5/7 under center and 1/3/5 from the gun, about 5/7/9 yards. The hitch step on the
  five-step drop. Footwork tied to the progression (last step, hitch, second hitch).
- The curl-flat high-low, including the defense's three answers (man, pattern-match, bait).
- Counting underneath defenders: 4 in Cover 3 and 5 in Cover 2, with a four-man rush.
- Cover 2's hole against smash and the flood answer in Predict 3.
- Neither the air-yards and YAC section nor the receiver table makes analytics claims a coach would
  dispute.
