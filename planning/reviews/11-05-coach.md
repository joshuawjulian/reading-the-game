# 11-05 The Modern Era: coach and film-analyst review

Reviewed: `chapters/11-history/11-05-the-modern-era.qmd` plus `pdfs/11-05-the-modern-era.pdf` (built 2026-10-08 07:02 from the current source). I rasterized pages 1-27 at 80 dpi and the figure pages at 120 dpi, and looked at all 13 figures.

**Verdict:** the chapter is strong. The arms-race spine is correct football: single-high and the 8-man box, then play-action into the intermediate middle, then two-high with the light box, then the extra blocker and under center, then base and big nickel. The box-count arithmetic is right. The quarters post off a run-blocking #2 (fig-pa-two-high) is exactly the right beater to show. There are still four errors a coach would catch immediately: the substitution premise of Predict 3, the miscount in Predict 1, the fake handoffs in both play-action strips that never actually mesh, and a title collision in fig-pa-two-high. A few explanations also need tightening.

---

## MUST FIX (football is wrong or the diagram misleads)

### 1. Predict 3 (`fig-predict-heavy`): the substitution premise contradicts the rules and 02-01
The caption says the offense used three receivers on the previous play and has now lined up in 12 personnel "without huddling", so the defense is "unable to substitute". That isn't possible. Under the NFL's substitution rule, if the offense swaps a receiver for a tight end, the umpire stands over the ball until the defense has had a chance to match. [Personnel Groupings](../02-personnel-and-formations/02-01-personnel-groupings.qmd) teaches this rule ("Substitution matching": "when the offense substitutes, the defense must get a chance to respond before the snap"), so this drill contradicts an earlier chapter.

**Fix (this is the real-world version of the trick):** the offense had 12 personnel on the field on the previous play too, but lined up spread, with U split out as a slot or wide receiver, and the defense matched that look with nickel. Now, at tempo and with **no substitution**, it compresses both tight ends into the formation. Suggested caption: "On the previous play this same 12 personnel lined up spread, with the second tight end (U) split out as a receiver, and the defense answered with nickel. Now, at tempo and without substituting, the offense has brought U in tight and put the quarterback under center. The defense can't change players, so it is still in nickel with two safeties deep…" This also ties the drill to the move tight end, which is the chapter's own thread. In Answer 3, change "the defense will try very hard to get a base package … the next time those two tight ends come in" to "…the next time this personnel group comes in, before it knows whether the tight ends will be tight or split."

### 2. Predict 1 (`fig-predict-creep`): wrong count, and the SS isn't where the text says
- The answer says the creeping SS "is now a **ninth** run defender". The count is E, T, T, E, W, M, SAM = 7, plus the SS = **8**, which is what the caption says. Change it to "eighth".
- The SS is drawn at `D("SS","SS",5.0,9.6)`, which puts him directly over Z (w=9.5) and outside the chapter's own dashed box (±8). He reads as a man-to-man defender on Z, not as a "crept down outside the tight end" box player. **Move him to (5.5, 7.0)**: outside Y (4.8) and the SAM (7.4 is already close, so also move the SAM to `(1.0, 6.6)` as a stand-up end on the line, or to `(3.5, 6.2)`). Then he clearly sits in the box, inside Z. Move the "crept down" pointer target to match.
- The caption says "The two linebackers are at 4.5 yards", but this is a base 4-3 with three linebackers (W, M, S). Change it to "The Mike and Will are at 4.5 yards; the Sam is outside the tight end."
- Answer 1 says "the tight end leaking up the seam behind the strong safety is the shot". On a **boot left** that throw goes back across the field to the right seam, against the QB's momentum. No Shanahan-tree QB is taught to make that read. Either drop it, or recast it as a **different** call off the same action: "or, from the same outside-zone fake *without* the boot, the Y-leak/seam or a Z post behind the safety who came down." The boot's own three-level read is X (clear-out), Z (deep over), F (flat), and it reads high-to-low to the boot side, which is correct as written.

### 3. Both play-action strips: the fake handoff never meshes
In `pa_cover3()` (fig-pa-cover3) and `pa_two_high()` (fig-pa-two-high), the QB reaches his "fake" point at about 0.4 s, at (-3.2, 1.0) and (-3.0, 1.0). At that moment the RB is still at about (-5.6, 2.4), roughly 2.5-3 yards away. In the +0.9 s panel the QB is already 5 yards deep and booting or dropping, while the RB is off to the right on his own. A reader sees no fake at all, and the caption ("the quarterback has turned his back to the defense to fake the handoff") describes something the picture doesn't show. On an under-center outside-zone action, the QB opens or reverse-pivots, meets the back at about 4-5 yards deep and 1.5-2.5 yards playside at about 0.6-0.8 s, extends the ball, and only then boots or finishes his drop.

**Fix (chapter code, no gridiron change needed):**
- QB: `p.path("QB", [(-4.6, 1.8)], absolute=True, speed=4.0)` (mesh reached at about 0.7 s), then `p.path("QB", [(-6.8, -3.5), (-7.2, -6.5)], absolute=True, speed=6.0)` for the boot. For pa_two_high, use `[(-7.8, 0.6)]` for the drop.
- RB: slow the first leg so he arrives at the mesh with the QB, `p.path("RB", [(-4.8, 2.4)], absolute=True, speed=4.2)`, then `[(-2.4, 6.6)]` at about 6.0.
- Keep the 0.9 s panel. It should now show Q and R together at the mesh, with the "run fake" label next to them.

### 4. fig-pa-two-high: the QB throws a 22-yard post off a full fake at 2.0 s, which is too early
A reverse-out fake, a 7-plus-yard drop and a set takes about 2.6-2.9 s on a play-action shot. Z's post also breaks at 9 yards, which makes it a skinny post at dig depth, not a shot. Use `r.path((12.0, 0.5), (24.0, -7.0))` (stem to about 12-13 yards and break at the safety's original depth), and move the throw to about `t=2.6` (`PA2_T = [0.0, 0.8, 2.6, catch]`). It also lets the SS's trigger-and-recover read naturally. Right now he gets down to 4.6 yards. A quarters safety triggering on #2's run block fits at 6-8 yards, so use `(6.5, 6.0)` instead of `(4.6, 6.0)`.

### 5. fig-pa-two-high: panel titles collide (print)
"Snap · 12 personnel under center, two-high" runs into "+0.9 s · the strong safety fits the 'run'" (page 13: "two-high+0.9"). Shorten it to "Snap · 12 personnel, two-high" or "Snap · 12 under center vs two-high". Alternatively, drop `width_in=5.9` back to 6.5, though that alone won't clear the overlap.

### 6. fig-pa-cover3: the backside end is shown in the QB's face, but the caption says "clear of the unblocked end"
At +2.6 s, WDE is at about (-4.5, -6.2) and the QB at about (-6.4, -6.2): the end is between the QB and the line, 2 yards away, at the throw. That is the picture of a boot that has *failed*. Either make the end lag (squeeze first to `(0.3, -2.6)`, then chase to `(-3.5, -4.0)` with `delay=0.5`, so he ends behind and inside the QB), or rewrite the caption to "throws with the unblocked end closing", which is also realistic. The QB fix in item 3 moves the QB deeper and wider, which helps on its own.

---

## SHOULD FIX (explanations a coach would correct)

7. **"A quarters safety is the first run defender to the edge on his side"** (Common misconception, two-high). That's wrong in most dialects. In quarters the apex or overhang player (nickel, OLB) is the **force** player, and the safety is the **alley** fitter, inside-out off the force, triggered by #2's run block. Suggested wording: "a quarters safety reads the tight end or slot in front of him and, the moment that player blocks, becomes an alley run defender at 7 or 8 yards". This also matches the chapter's own fig-pa-two-high caption.

8. **Missing: the front that makes a 6-man box work.** "The defensive line has to win its own fights" leaves out the structural answer that made the counterrevolution possible: Fangio and Staley's **tite (mint) front**, with a nose on the center and two 4i's on the guards' inside shoulders, which walls off the A and B gaps, keeps the two linebackers clean, and spills the run outside to the safeties and the force players. Add one sentence and a link in the two-high section's point 2: `[tite front](../../appendices/glossary.qmd#gl-tite-front)` (owned by 05-03, Odd and Hybrid Fronts). Without it, the reader wonders how six can hold up against six.

9. **Rams 2018 film room: the mechanism of the 6-1 is misdescribed, and the Fangio link is overstated.** "With a defender over every gap, the line's sideways steps found nobody to cut off" isn't how a coach would put it. What actually happened: with every interior lineman *covered* (no uncovered linemen), outside zone loses its double teams and combos. Every lineman has to reach a defender already shaded to his playside, which is the hardest block in football, and nobody climbs freely to the linebackers. Also, the 2018 Bears were not yet the two-high Fangio of Denver; their game plan was front structure plus disguise (the chapter's own source calls it "complex zone schemes that incorporate man concepts"). Suggested wording: "Fangio's lesson from that night, cover up the interior so the zone has no combinations, and win the run with the front, not an eighth man, became the base of the two-high system he installed in Denver in 2019 and Staley took to the Rams in 2020."

10. **The two-high section has no film room.** It is the conceptual centre of the chapter, and it is the only major section without one. Suggestions: the 2020 Rams under Staley (fewest points; Ramsey as a moving star, Donald inside the tite), or the 2021 Chiefs against two-high (already footnoted, 45.9 percent; the "patience" story, with Kelce underneath). Link 12-08 for depth.

11. **The motion story is under-told, and the writer's-note number is missing.** The curriculum notes ask for **PFF shift/motion 63.9% (2025)**, and the chapter never cites it. Motion is also the offense's most direct counter to *rotation*: motion at the snap makes a rotating safety declare (or arrive late), and the 2023 Dolphins (about 60 percent motion at the snap, per ESPN) are the extreme case. Add 2-3 sentences in "The offense answers" (or after the McVay five points), using FACTS §10. Keep the PFF and FTN series separate and attribute each.

12. **The McVay hallmark a coach would add:** the Rams broke the huddle early so McVay could keep talking into Goff's helmet until the radio cut off with 15 seconds on the play clock. They saw the defense's alignment and adjusted the call at the line. That is the "sameness" idea's partner: the same look, with the play chosen late. Also name the specific motion, **jet/fly motion at the snap** as an outside-zone and sweep threat, rather than "motion" in general. (Fact-check the 15-second radio cutoff before printing; it's long-standing NFL procedure.)

13. **The light-box arithmetic leaves out the shotgun answer.** "From 11 personnel the answer is six" is right for blockers. But 11-personnel offenses' main answer to a light box was the **RPO and the QB read** (a "plus-one" without a seventh blocker), and the chapter only covers that later, in the QB section. Add a clause in the three-choices paragraph: "or keep 11 and make the quarterback the extra man, with a read or an RPO (the Eagles' and Ravens' way, below)."

14. **The star and big-nickel paragraph needs the dialect, and the Chancellor point is muddled.**
- "Defenses call him the star." In the Saban dialect, **Star is the nickel** (any fifth DB, often a corner) and Money is the dime. Others call the nickel "Nickel" or "$" and the third-safety version "big nickel". Say so in one line, since the chapter uses both "nickel / star" and "big nickel".
- "Seattle answered the move tight end this way a decade earlier with Kam Chancellor." Chancellor was Seattle's *base* strong safety, a box safety matched on the tight end, not a third safety in a nickel spot. Seattle's nickel was a corner. Reword: "Seattle had used a linebacker-sized strong safety, Kam Chancellor, on tight ends a decade earlier; the two-high era made a third safety in the nickel spot standard."

15. **Ravens 2019 film room:** "often a fullback and three tight ends". FB plus 3 TE plus RB is 23 personnel with zero receivers, which the Ravens used only occasionally. Reword: "two and three tight ends (Andrews, Hurst, Boyle) and a fullback-tight end (Ricard), far more than the league did." Also consider naming one signature concept the reader can spot, for example the inverted veer/QB counter or pin-pull outside zone. 12-05 owns the detail, so a single named concept is enough.

16. **fig-positions: Mike and Will are on the wrong sides.** M is at w = -1.2 (away from the passing strength) and W at +3.6 (toward Y and Z). In 2-linebacker nickel most systems put the Mike to the strength and the Will away from it, as every other figure in this chapter does (figs 2, 3, 5, 6, 12, 13). Swap them, `MIKE (4.8, 2.6)` and `WILL (4.5, -2.2)`, and keep the hybrid ring on the W. Or label the ringed player "M" and move the "Hybrid LB/S" pointer to him.

17. **The fig-pa-cover3 explanation should name the real coverage beater.** The text credits the linebackers' bite. That bite matters, but the boot is a **high-low on the weak curl-flat player** (the $): H's flat pulls him wide, and the deep over settles behind him and in front of the sinking corner. Add one sentence after "nobody is left in the middle": "the nickel had to choose between the flat and the over; he took the flat." This gives the reader the read the QB actually makes. Also move the "nobody left in the hole" note in panel 4 from (16.2, -6) (next to the FS) to about (9.0, -9.5), where the hole actually is.

18. **Predict 3 answer, option list:** add the cheap pre-snap check every DC has. Without substituting, the defense can **shift the front and bump the linebackers to the tight-end side** (an over or strong front, with the $ walked down weak or the backside safety rotated toward the strength). The box stays at six, but the gaps are right. Its cost is the weak side. As written, the answer suggests the defense has to stand there, out-leveraged, with the nickel on the far side.

19. **Rules table:** the prose counts five kickoff changes, "2018, 2023, 2024, 2025 and 2026", but the table has no 2023 row. Add "2023 | Fair catch of a kickoff inside the 25 is a touchback at the 25 | a stopgap before the 2024 redesign" (FACTS §6). Optional, for the "league kept protecting the passing game" point: the 2018 roughing-the-passer "body weight" emphasis is better evidence than the helmet rule.

## NICE TO HAVE

20. fig-predict-heavy: the "7 blockers" label sits under X on the far left, away from the blockers it counts, which are on the right. Move it to about (-4.0, 9.5), as in fig-two-snaps.
21. fig-pa-cover3, Snap panel: the corners are at 6.5 yards off, but the text calls Seattle's corners "press-and-bail". Either draw LCB and RCB at about 1.5 yards (press) or say "off". Strictly, Seattle taught a "step-kick" technique from press, so "press corners" is enough.
22. fig-arms-race caption says "2010-2025", but the first node is 2013-2016.
23. fig-qb-rushing caption: "the Lamar Jackson era is a second, larger step". On the chart the 2019 bar (12.8) is no higher than 2013. The step is 2020 (14.1) and 2024 (16.5). Say "from 2020" or "the 2020s".
24. Wasp film room: "Jet" is Reid's protection call and "Chip" the back's chip-release. The chapter defines chip but not Jet. One clause would complete it, or leave "Jet" undefined deliberately and say so.
25. fig-light-box-run: both safeties converge on the frontside ball. In quarters the backside safety's fit is the cutback/fold. It's fine as the tackle picture, but if you touch the code, give FS a fold path to about (6.0, 0.5) so he fits the backside A/B gap.

## What is right and should not change
- 11 personnel, condensed splits, under center, outside zone, and play-action on the same action: the five-point list is correct and well ordered.
- fig-two-snaps: legal formations (7 on the line in both), correct box counts (8 v 6 blockers; 6 v 7), and the right defensive personnel for the era.
- Quarters vs a run-blocking #2 with the post behind the triggering safety: the correct beater, explained from the safety's point of view.
- The reasons for going under center (the run gets better, the fake gets better, the safety has to decide, the back's alignment gives less away), with the cost stated (slower setup, third-and-long stays a shotgun down).
- The plus-one logic for the running QB, and "count the defenders watching Jackson at the mesh".
- Animation count (3) is within the limit, and the strips tell the story in print once item 3 makes the mesh visible.
- Every label is inside the window; nothing is clipped by the field edge. The only collision is the strip title in item 5.
