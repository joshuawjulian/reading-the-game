# 04-05 Play-Action, Bootlegs, and Screens: coach / film-analyst review

Reviewer role: veteran NFL coach and film analyst. Scope: technical accuracy, diagrams, timing, missing nuance.
I read the full chapter, rasterized `pdfs/04-05-play-action-boots-screens.pdf` (24 pp, built after the last
qmd edit) and looked at all 17 figures. I also ran the chapter's play code to check where the linemen are when
each pass is thrown (`_pdfbuild/04-05-play-action-boots-screens/rev/run.py`).

**Overall:** strong chapter. The core teaching (run-fit triggers, "match the run, not the run stats", three
windows, the naked-boot bet, screens as a tax on pressure) is right and well sequenced. The data sections are
sound. The problems are mostly in a few diagrams. The middle and jailbreak screens break the chapter's own
one-yard rule or timing, the shot play has frozen corners and no named coverage, and the TE's boot release
runs through the Mike. Some coaching nuance is also missing (BCR, the U's fake cut-off on the naked, the
grounding exception, the QB's throwing hand on boots).

## Must fix (football is wrong or self-contradictory)

1. **Middle screen breaks the chapter's own ineligible rule (fig-te-middle right; text line ~1388).**
   The caption and body say the guards and center "release straight upfield to the linebackers." In the sim,
   at the throw (t = 1.62 s) LG is at d = 1.15 and C at d = 1.06, and their block paths end 3.0–3.6 yards
   downfield. The chapter spends a whole paragraph saying NFL screen linemen release flat and turn up only
   after the throw, and the Predict-3 answer depends on that.
   *Fix:* LG, C and RG set, let the DTs through, then shuffle to about d = 0.5 (in front of the back's catch
   spot). Draw them climbing to the LBs only after the throw: add a second block leg with `delay` past the
   throw time, or draw the climb as a dashed "after the throw" branch. Reword to "...let the defensive tackles
   through, set up a wall at the line, and climb to the linebackers as the ball is thrown."

2. **Jailbreak screen is thrown 0.17 s after the snap (fig-tunnel-jailbreak right).** With `throw_at` and a
   short H route, the ball leaves almost at the snap. The linemen haven't moved and the play is really a now
   screen. A jailbreak works because the linemen are out in front *before* the catch. Real NFL timing is about
   0.9–1.3 s.
   *Fix:* give H a 2–3-step "stem" first (upfield or a short arrow), then come back toward the ball behind the
   LOS. Catch around 1.4 s, throw around 1.0 s. Check that LT, LG and C are within a yard at the throw; they
   already end at d = 2.6–3.8, so add a delay so the turn-up comes after the throw. The text's "thrown in
   about a second" is right; the sim is not.

3. **Shot play (fig-shot-play): the coverage is never named and both corners stand still.** In the caption's
   logic, the FS alone can't cover the post and the over. That holds against Cover 1 but not against Cover 3,
   where the boot-side corner's deep third is where the over lands. With frozen corners at 6.5 yards, both
   routes look uncovered, which misleads the reader.
   *Fix:* name it. Cover 1 (man, FS in the middle, SS down) is the cleanest for yankee. Draw LCB trailing X
   (inside the post, a step behind) and RCB chasing Z across the field (the over runs away from him). The read
   is then the FS: if he stays on the post, throw the over in front of him; if he drives on the over, throw
   the post. Optionally add one caption sentence for Cover 3 (the over attacks the deep third the corner
   bailed into, so the read is that corner). Fix the caption sentence "He cannot be in both places" to name
   Cover 1.

4. **The naked boot: "the man zone blocking leaves unblocked anyway" contradicts 03-02.** In 03-02's outside
   zone from this same 12-personnel look, the **U cuts off the backside end** (03-02, around line 764). The
   whole sell of the naked boot is that the U *shows that cut-off block* and then slips past the end into the
   flat, so the end sees run and chases.
   *Fix (text):* "On the real run the U cuts this end off. On the naked boot the U fakes that block, lets him
   go and releases to the flat, so nobody blocks him." *Fix (diagrams fig-naked-boot, fig-boot-animation):*
   give U a short block step into BE (about 0.3 s, `kind="block"`) before his flat release. The current
   0.5 s idle delay reads as standing still.

5. **Boot strip (fig-boot-animation): the Y's crosser runs through the Mike.** Y's path goes (0.2, 5.6) →
   (1.6, 3.6) → (5.6, −0.8), crossing at 1–2 yards depth exactly where the Mike steps up. In frame 1 (+0.7 s)
   the Y marker sits on M and their rings overlap. A real boot TE sells his outside-zone block on the
   end or Sam (a reach step for about 0.4 s), then works across *behind* the linebackers' flow at 6–10 yards.
   *Fix:* Y path roughly (0.3, 5.8) block-step with a 0.4 s hold, then (4.5, 2.5), (7.5, −3.0), (10.5, −9.0),
   (11.5, −15). Check that at 0.7 s he is still at the line selling, and at 1.7 s he is behind M and W. Drop
   the Y ring from frame 1 or move frame 1 to 0.6 s so the rings don't overlap.

6. **Swing vs screen timing contradicts itself (fig-swing-vs-screen and text).**
   - The text says a swing is "thrown in about a second" and gives that as a tell. In the next breath it calls
     the swing a checkdown, and checkdowns come *late* (2–3 s). As a broadcast tell, timing is unreliable.
     The reliable tells are (a) the line still pass-blocking and (b) the back's release: a swing back leaves
     at the snap and runs his path, while a screen back delays (sets to block) and *settles* behind the
     released linemen. Rewrite the "second tell" in those terms. The fig-predict-screen answer's "ball comes
     out in about a second" needs the same change.
   - The right panel label says "ball out at ~2.5 s", but the sim throws at 2.02 s (same in fig-slow-screen
     and the predict figure). Real NFL slow screens are usually thrown around 2.3–2.8 s. Either push the
     throw later (raise the LT/LG/C and RB delays by about 0.3 s) or change the label to "~2 s". I prefer
     the later throw, so the predict frame at 1.9 s still shows the QB holding the ball.

## Should fix (nuance a coach would insist on)

7. **Leak: the glossary and the body describe different routes.** The glossary example says "back across the
   field behind a bootleg." The body and figure show the play-side Y blocking, then releasing to *his own*
   flat as a throwback. Both exist in playbooks. Pick the drawn one and change the glossary example to "for
   example, the play-side tight end releasing into the flat the quarterback just ran away from (a
   throwback)." Also add one sentence on why it's rare: for a right-handed QB rolling left, throwing back
   across the field means stopping, resetting his feet and making a long throw against his momentum.

8. **The QB's throwing hand decides the boot's direction.** All the boots here go left, which for a
   right-handed QB is the hard way: he has to open his hips and shoulders to throw. Coaches teach it ("flip
   the hips, square the shoulders, belly the path"), and offenses with a right-handed QB tend to favor boots
   to the right, with the run fake going left. Add one sentence in "What the bootleg gives up." If you keep
   boots left, say the QB is right-handed and that the throw is harder.

9. **Predict 2 answer.**
   - Name the defense's rule: the backside end's checklist is **boot, counter, reverse (BCR)**, which 03-05
     already teaches (03-05, around lines 1494 and 1577). Link it. That is exactly what this end has started
     doing.
   - "A keeper the other way (... keeping it to the play side)" is confused: a QB keep to the run side runs
     into the flow. Replace the third option with **split zone or a sift block** (03-02 owns split zone): an
     H or tight end comes across behind the line and kicks out the end who is sitting for the boot. The run
     look is the same and the end gets blocked. Or use the boot with a slice/sift blocker (see 10).
   - Mention the escape: once outside the tackle box, the QB may throw the ball away legally if it reaches
     the line of scrimmage (the intentional-grounding exception). That is why "throw it away" is a real
     option on a busted naked. Gloss and footnote it to the NFL rulebook (fact-check the article number).

10. **Protected boot: show the more common NFL protector.** The text says "usually a guard pulling from the
    line or a tight end or fullback." In current Shanahan/McVay-tree offenses the boot-side end is very
    often blocked by an H, fullback or tight end coming across behind the line (a "sift" or "slice", which
    also matches split zone, the companion run). The guard pull is real but rarer at the NFL level.
    Suggestion: keep the guard pull in the figure but make the text "a guard pulling or, very often, a
    fullback or H-back sifting across behind the line." *Diagram:* in fig-boot-family left, the BE "5" square
    sits on top of the ringed LG. Stop the LG about 1 yard short (or move the frame to 1.4 s) so both labels
    read.

11. **"The defensive linemen are not fooled at all" (Why it exists callout and the fake rules section) is too
    absolute.** Run-first DL on early downs (two-gappers, and the backside end on outside zone, which is the
    whole boot premise) *are* held for a beat. Better: "fooled less and for less time than the linebackers;
    they feel pass protection almost at once." This also removes a tension with the boot section, which
    depends on the backside end being fooled.

12. **Link the line's first-step key to the term the course already taught.** 01-06 teaches "high hat, low
    hat" (run blockers stay low, pass blockers pop up). The linebacker-keys paragraph describes exactly that.
    Use the phrase and link 01-06; it also helps the Watch-for-it bullet about the guard.

13. **Defensive answers to play-action and boots are thin.** Besides the end staying home, a coach would
    name: linebackers **cross-keying the guards** (a guard pulling the other way or popping up means boot or
    pass), the back-side linebacker or a robber safety **carrying the crosser** ("crosser rules" in
    match/quarters coverage), and the boot-side flat defender sinking under the over route. One short
    paragraph, linking 05-04 and 05-05, would complete "each answer has an answer."

14. **Watch for it: "Two tight ends, a back seven yards deep" is too specific.** The Rams film room correctly
    says the 2018 Rams faked from 11-personnel tight-split sets. Generalize: "whatever formation the offense
    runs its main run from, often 12 personnel or tight-split 11; that is the formation it fakes from."

15. **Screens vs man coverage.** Add one line to "Screens punish pressure": against man, the defender
    assigned to the back (usually a linebacker) chases him straight into the released linemen, which is why
    screens pair so well with Cover 0/1 blitzes (the fig-screen-blitz scenario). Against zone, an underneath
    defender sitting in the flat can wreck a slow screen.

16. **Crosser depth.** "Crosser ... at 8–12 yards" is a little deep for the classic boot drag. Shanahan-tree
    boots usually run the TE crosser at about 6–10 yards, with the over at 15–20. Say "6–12" or "about
    8–10."

17. **Optional reality note on the one-yard rule for screens.** The rule statement is right. On film,
    released screen linemen are often a yard or two past the line at the throw and rarely flagged; the 2024
    Dowdle flag in the footnote was itself picked up. A sentence like "officials judge it by eye and give a
    little leeway, but coaches teach the flat release because the flag wipes out the gain" is the
    film-room truth. Only add it if a source can be found; otherwise skip it.

## Diagram polish (labels, collisions, captions)

- **fig-pa-teams:** the "No run fake / Play-action" legend sits in the lower left over the KC and CIN rows.
  KC's orange (no-fake) dot looks hidden behind it. Move the legend to the top (`loc="upper center",
  bbox_to_anchor=(0.45, 1.0), ncol=2`) or into the empty middle right.
- **fig-predict-screen (1.9 s):** the SDT "T" and SDE "E" squares sit on top of the RG and RT markers, so their
  labels can't be read. Slow those two rushers (or end them about 1.2 yards short) so the RG and RT stay visible.
- **fig-screen-blitz frame 2 (+1.2 s):** R, E, W (ringed) and T form a single cluster and the rings overlap.
  Move frame 2 to about 1.0 s, or route the Will slightly more inside (his via point w −0.6 instead of −1.2)
  so the back's slide is visible beside, not under, the blitzers.
- **fig-boot-animation frame 1:** the SS and RCB squares touch near Z. Give RCB a wider endpoint (w 6.0).
- **fig-slow-screen:** the "three linemen out in front" label is about 10 yards downfield, among the
  linebackers, while the point of the figure is that the linemen are within a yard of the LOS. Move it to
  about (−2.5, −11) or use `point_to` aimed at the LT/LG release points.
- **fig-te-middle caption:** "the receivers not involved are outside the picture" is false for the right
  panel (H and Y are visible). Say "receivers not involved stand still" or crop with `lateral=(-8.5, 8.5)`.
- **fig-uc-vs-gun right panel:** the back's path passes through the QB marker, so it looks like the arrow
  starts at Q. Offset the mesh point slightly (via (−4.0, 0.9)) so the ride reads as two players meeting.
- **fig-lb-void:** the two safeties never move in 1.5 s (they sit at 11.5 yards) while the dig breaks at 13,
  *behind* them. Give both safeties a 2–3 yard bail (dropback) or a read step and then a bail (play-action),
  so the dig is clearly underneath them.

## Checked and fine

- One-yard NFL rule statement and citation; college three-yard and "crosses the neutral zone" contrast;
  consistent with 04-06.
- Under-center vs shotgun play-action rates (82% vs 10% in 2025) and the table's selection caveats.
- Run-game vs PA-boost analysis (r = +0.09) and its framing; YAC finding; screen EPA by rush count with
  sample sizes and selection caveat.
- Bootleg structure (flat / crosser / over, plus a boot-side clear-out), high-to-low read, naked vs
  protected, keeper definition.
- Slow-screen sequence (sell, let go, release on a count, drift and loft), linemen's release rules, and the
  "smelling" failure mode.
- History: Shanahan/Kubiak Denver 1995–2005, Elway's final four seasons, Kyle Shanahan 2016 ATL, McVay and
  LaFleur lineage, Reid's screen game. Rams 2018 (13–3, 34.6% PA per PFF, SB LIII 13–3).
  Seattle 2025 (Kubiak OC, Darnold, SB LX 29–13; Kubiak now Raiders HC) matches FACTS-current.
- Animation count (2) is within budget; both frame strips tell the story in print.
