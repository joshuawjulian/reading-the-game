# Coach / film review: 11-03 The College Laboratory

Reviewed 2026-10-08 against `pdfs/11-03-the-college-laboratory.pdf`, built 05:40 after the last .qmd edit. I rasterized all 24 pages at 120 dpi and looked at every figure.

**Verdict.** This is a strong chapter. The lineage story is accurate, and most of the diagrams are drawn the way a staff would draw them: the wishbone count, the four-backfields panel, the zone-read-plus-bubble and the 3-3-5 stack. The fixes below are mostly about assignments: one coverage bust, one set of receivers blocking air, and one pitch relationship that contradicts the film room. There are also two label problems and a few places where a coach would add a nuance. Nothing here is a structural rewrite.

## Must fix (football is wrong or misleading)

1. **fig-335-stack, "Pressure 2: Sam and bandit": the field slot is uncovered.** The Sam and the bandit both come from the offense's right. Every dropper then bails to the left or the middle: MIKE to (8.6, -2.4), WILL to (8.4, -7.0), SP to (8.6, -10.0). Nobody is under F, the right slot at w = +9, which leaves a free hot throw directly where the pressure came from. A real fire zone rotates the underneath droppers toward the blitz. Fix:
   - `go_to(p, "MIKE", (7.5, 5.5), "path")`, as the hook/curl player to the blitz side (he walls F's inside release).
   - `go_to(p, "WILL", (7.8, -1.0), "path")`, the middle hook.
   - SP stays at about (8.0, -8.5), the weak curl/flat.

   The caption can then add: "three under, three deep (two corners and the free safety), the Mike rotating to the side the pressure came from."

2. **fig-three-high, the run panel: the four receivers' "blocks" end in empty grass.** X, H, F and Z each go 2.6 yards and draw a block tee, but no defender is within 4 yards of them (the CBs are at 7, the safeties at 9.5, the W/S apexes at 4.5 inside them). This reads as a blocking scheme that doesn't exist. Pick one of these:
   - (a) Show stalk blocks. X goes to (5.5, -12.8) on the LCB, Z to (5.5, 12.8) on the RCB, and H and F to about (4.0, ∓6.0) on the W and S apexes.
   - (b) More honest for 2017 Big 12 football: run H and F on routes (the RPO tags) and leave W and S unblocked as conflict players.

   The panel also leaves W and S frozen. Give the backside apex (W) a short fit/squeeze step, so it doesn't look like two defenders standing still on a run.

3. **The three-high box count is inconsistent across the figure, its caption, the text and Drill 1's answer.**
   - The caption says "a box that looked like five defenders against five blockers... has six or seven by the time the back arrives."
   - The text after it says "a five-man box against a five-man line."
   - Drill 1's answer says "five... if he's on time, the offense has run into a **seven**-man box."

   The picture actually shows 4i-N-4i plus the Mike (4) in the box, with W and S as apexes (`tight()` puts them at ±5.2 against slots at ±8). One safety flying down makes it **six**, not seven. Fix: say "four in the box and two apex players, so five or six depending on how you count the apexes; the flying safety adds one." Change "seven-man box" in Answer 1 to "six-man box", and "six or seven" in the caption to "one more than it showed."

4. **fig-wishbone-triple: the pitch relationship contradicts the film room.** The Oklahoma 1971 film room teaches the pitch man "four or five yards outside the quarterback and a yard deeper." In the figure the QB pitches from (-1.6, -5.4) and the pitch man is at (-4.0, -9.2)/(-4.2, -9.6), which is about 2.5 yards *deeper* and only about 4 wider. Fix: end the RH path at about (-2.8, -10.2) (via (-5.6, 0.4), (-4.6, -6.0)), move `pitch_arc` to (-1.6, -5.4) → (-2.8, -9.9), and start the pitch branch from (-2.8, -10.2). Make the same change in `bf_bone`/`bf_split`/`bf_flex` in fig-triple-backfields, where the toss ends 2–3 yards deeper than the QB. This is the coaching point of the play: the pitch man stays "4 by 1" so the pitch key can't play both.

5. **Flexbone origin claim.** "Bellard at Mississippi State" is the weak link in the attribution list. Bellard ran the *wishbone* at Mississippi State (1979–85). The flexbone is usually credited to Ken Hatfield and Fisher DeBerry's Air Force staff in the early 1980s, with Paul Johnson's Georgia Southern version following. Suggest: "Its invention is disputed (Ken Hatfield and Fisher DeBerry's Air Force teams of the early 1980s are the usual answer; Paul Johnson's Georgia Southern ran its own version from 1985)." Flag this for the fact-checker to confirm.

6. **Up-tempo row in fig-lab-timeline, and "the no-huddle as a way of life arrived from college" (line ~360).** The NFL had a whole-game no-huddle before Oregon: Sam Wyche's 1988 Bengals and the K-Gun Bills of 1990–93. 11-02 tells that story. Fix: change the timeline note to "spread-run tempo: Kelly's Eagles". In the intro list, say "the spread no-huddle", or add a clause such as "(the NFL had flirted with the no-huddle in the K-Gun era; college made it an identity)". Otherwise a reader who knows the Bills will distrust the whole timeline.

## Should fix (diagram polish and labels)

7. **fig-wishbone-triple: the "pitch" label collides with the SS box.** The label at (7.8, -12.0) sits flush against SS at (7.5, -10.0), with the "3" numeral directly above. Move `label_at` to (5.0, -13.4) or end the pitch branch at (5.0, -12.6).

8. **fig-triple-backfields, spread-option panel: the #2 key (NB at d = 4.0) sits at the top edge of a window that ends at 4.6.** It breaks the 1.5-yard rule, and in print the box touches the frame. Either use `window=(-6.5, 6.0)` for all four panels or put the NB at d = 3.0.

9. **fig-triple-backfields caption: "In every panel the inside runner attacks just inside the dive key (#1)."** This is false for the spread panel, where the give goes the *other* way. Change to "In the three under-center panels…; in the spread option the give goes away from the read."

10. **fig-drill-1: both "short side" / "wide side" labels touch the top of the frame.** They sit at d = 13.5 in a window that ends at 15.0. Move them to d = 12.0, or use `window=(-7.5, 16.5)`.

    The drill also contradicts its own teaching. The text and the Watch-for-it say college defenses align by **field and boundary**, but the drill defense is symmetric about the ball. Shade it:
    - FS about 2 yards to the field (w = +2).
    - The boundary safety tighter and shallower (about 8 deep, w = -6.5).
    - The field safety wider (w = +11).

    Also put Z on the field numbers (w ≈ +19), the way an offense would use a 33-yard field side. This makes the bonus answer ("why you knew it was college") visible in the picture, not only in the hash position.

11. **fig-rodriguez-anim (frame strip): no frame shows the decision.** The ball is thrown at t = 1.45, but the strip jumps from 0.9 (the pull) to 2.2 (the catch or the run). Use `TIMES_ZRB = [0.0, 0.9, 1.45, 2.2]` (four columns still fit at 6.5 in), with notes such as "Nickel widens with H: keep" / "Nickel steps up: ball out".

    In the keep branch the nickel only widens to w = -10.4, still about 4 yards from the QB's lane. That isn't "chasing the bubble", and a sharp reader will think the nickel can still make the tackle. Send him to about (1.0, -12.2) so he is visibly on H.

12. **fig-drill-3: Z stands still at w = +16 with the CB across from him.** In any real version Z either clears the corner out (a go route) or the throw is to Z's side for a reason. Give Z `p.route("Z", [(0,0), (18, 0.5)])`, a go that takes the CB deep and opens the sideline for F's bender.

    Call F's route what it is: "a seam that bends to the sideline" is a corner-shaped route (some staffs call it a "bender" or "seam-out"). "Seam-corner" in the prompt and the caption is clearer.

13. **fig-three-high, pass panel:** the RB check-down is drawn, but the pass to him isn't visible (the brown dashed line at the bottom is the QB's drop). Either draw the throw explicitly with `pitch_arc` from (-7, 0) to the RB, or drop `pass_to` and say "the check-down is all that's left" in a label. The "3 under" label at (10.4, -3.4) is fine.

## Nuance a coach would add (short sentences, optional)

- **The ruling in Drill 3 (NFL).** The pass is incomplete anyway (one foot), so the defense *chooses* between the incompletion and 5 yards with the down replayed; it doesn't get both. Reword: "flag for illegal man downfield: the defense can take five yards and replay the down, or simply decline it and take the incompletion."
- **Tite text (line ~1093):** "two 4-techniques on the tackles' inside shoulders" should say **4i-techniques**, to match the "4i" labels in fig-three-high and 05-03's convention (a plain 4 is head-up on the tackle in most systems).
- **3-3-5 text:** "with eight potential rushers standing up" is off by three, since only five are standing. Say "with eight potential rushers and only three hands in the dirt."
- **Hybrid-safety names are a dialect.** Spur/bandit is Casteel's West Virginia vocabulary. TCU's 4-2-5 says strong/weak safety, Saban-tree nickels say Star, others say Rover or Viper. One clause saves a reader confused by a broadcast.
- **The pre-1993 college hash** sat 53 ft 4 in from each sideline (the high-school spot), so the wishbone and veer eras had an even shorter boundary (about 17.8 yards). One clause in "A wider field" strengthens the field-geometry argument.
- **Texas Tech 2008 film room:** "the Texas defensive linemen had to rush a long way around blockers" is a slightly odd reason for Leach's splits. The usual coaching reason is that wide splits widen the rush lanes and the gaps between defensive linemen. That makes stunts and games harder to run, gives the QB clear throwing windows on a quick 3- or 5-step drop, and forces the defense to declare where the pressure comes from. Suggest that wording.
- **Kingsbury (line ~762):** fine as past tense. If you want it current, he was Washington's OC in 2024–25 and is the Rams' assistant head coach for 2026 (FACTS-current §9).

## Checked and correct (no change)

- Wishbone assignments: the veer release by the playside tackle to the Mike, the 5-tech as #1 and the on-line OLB as #2, the lead halfback arc-releasing to the alley safety, the split end on the corner. The four-number count is labelled consistently, and Drill 2's answer is a good teaching rep.
- Zone read plus bubble (fig-rodriguez): the zone-right assignments add up. LT takes the 3, LG climbs to W, C takes the 1, RG climbs to M, RT takes the 5, and the backside 5 is read. That is six box defenders accounted for with five blockers plus the read. The second read on the apex nickel is correct.
- Spread math (fig-spread-math): 8 v 7 in the I-formation panel, and 6 v 5 plus the read in the spread panel, are counted correctly. The apex placement and the 7-technique inside the TE are fine.
- 3-3-5 stack "Pressure 1" is sound: the slant away and the Mike/Will through the vacated A and C gaps, with three under and three deep.
- The shotgun chart and the inline numbers match the data and the text. The rules table matches 04-06 on the ineligible rule (the NFL applies to any forward pass; college only when the pass crosses the neutral zone).
- Film-room picks are well chosen and accurately characterized: OU–Nebraska 1971, Texas Tech–Texas 2008, WVU–Georgia Sugar Bowl 2006.
- The figure count (one animation) is within the limit. Gridiron use is sensible, and the college-hash context manager is a clean local workaround (no gridiron edits).
