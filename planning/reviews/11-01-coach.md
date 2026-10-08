# 11-01 coach / film-analyst review — From the Single Wing to the 1970s Scoring Drought

Reviewer role: veteran NFL coach + film analyst. Scope: technical accuracy, diagrams, film-room choices.
Rendered `pdfs/11-01-single-wing-to-scoring-drought.pdf` (26 pp.) and looked at every figure (Figs 1–13).

**Verdict:** strong chapter. The schemes are described the way coaches teach them: the single-wing
off-tackle (end and wingback double-team the tackle, blocking back kicks out, guards pull, fullback leads),
the Lombardi sweep assignments (on-side guard to the corner, off-side guard turning up inside, FB on the DE,
Y on the Sam, Z on the safety, C back on the weak DT), and the Flex alignment (strong-side end and weak-side
tackle flexed, strong-side tackle on the ball, which matches the D Magazine description). Nothing here is a
blocker. Below are the fixes a coach would insist on, ranked.

## Must fix (accuracy)

1. **Flex "was never a great defense for sacks" (line ~910) overstates it.** The Flex was Landry's
   *run-down* front; on obvious passing downs Dallas lined all four rushers up on the ball and rushed. The
   1977 Doomsday line was one of the best pass rushes of the decade (Harvey Martin's unofficial 23 sacks,
   1977; Too Tall Jones, Randy White). Fix: "Its price was the pass rush *from the Flex itself*: linemen
   reading blocks aren't rushing, so on clear passing downs Landry took his linemen out of the Flex and let
   them rush." (Fact-checker: confirm the Martin figure if it's used.)

2. **Ice Bowl film room picks the wrong play to teach the Flex.** The goal-line sneak was against a
   goal-line defense, not the Flex, so it says nothing about read-and-fill. The Ice Bowl play that *is*
   about the Flex came on the same final drive: **"Give 65"**, on which left guard Gale Gillingham pulled,
   Bob Lilly (taught to read and follow the guard) went with him, and fullback Chuck Mercein ran through
   the space Lilly had left, about 8 yards to the 3 (Kramer, *Instant Replay*). That is the counterpunch
   to every read-and-key defense (an "influence" or "sucker" play) and it fits the chapter's
   action-and-reaction theme exactly. Fix: keep the sneak as the finish, but make Give 65 the "what to
   notice". Also tone down "how rarely the Packers' backs find the big cutback lanes": the frozen field
   explains as much as the Flex does. (Fact-checker: verify the yardage and the guard's name.)

3. **Gillman figure (Fig 8) mixes terms.** The caption says "two-deep 4-3", then says the go route
   "threatens the deep third". Use "the deep half / the outside deep zone". Better still: 1960s pro
   defenses, especially in the AFL, were mostly **man-to-man with a free safety** (the bump-and-run era of
   the Raiders and Chiefs). Either say "against a 1960s 4-3 with two safeties deep" without "zone", or add
   one sentence noting that Gillman's deep-first passing was built largely against man coverage. That is
   the honest history, and it explains why zone coverage became the 1970s answer (cause 4 in the drought
   list).

4. **Drill 3 (Fig 13): the pressed corners are inside the receivers.** LCB at w=−13.4 against X at −14,
   and RCB at 12.0 against Z at 12.5. Cover 2 "hard" corners jam from an **outside** shade so they can
   re-route the receiver inside toward the safety, which is the whole point of the answer text. Fix:
   `"LCB": dict(d=1.2, w=-14.9)`, `"RCB": dict(d=1.2, w=13.4)`. Also widen the safeties slightly
   (w ±9.5, roughly the hashes) so they read as two-deep halves.

5. **Single-wing power caption (Fig 3): "the guard from the short side of the line pulls behind the
   center".** In this diagram both guards are already to the right of the center (the guard-over
   unbalance), so no guard is on the short side. Say "the inside guard (next to the center) pulls and
   leads". Nuance worth one clause in the text near line 413: many single-wing teams unbalanced with
   the **tackle** over instead (strong side guard–tackle–tackle–end), and the chapter's guard-over version
   is one of two common forms.

## Should fix (nuance a coach would add)

6. **Lombardi sweep: say what the HB reads.** The text says "reads the block on the Sam", which is right.
   Add that the pulling guards read it too: the on-side guard logs or kicks out the corner depending on
   his leverage, and the off-side guard turns up through whatever seam the Y block opens. That is the
   "option blocking" the next paragraph describes, so connect the two. In Fig 6 the decision point
   (0.8, 8.4) sits ~3.6 yd outside the TE and already at the LOS; Lombardi's back pressed the hole about
   a yard outside the TE and decided there. Move the fork to about (−0.6, 6.6) so "inside the Sam" isn't a
   cut back across the Sam's original spot.

7. **Umbrella (Fig 5): the halfbacks finish deeper than the safeties** (RH drops to 17, safeties to 16.5),
   which turns the "umbrella" into a flat four-deep line. Keep the umbrella shape after the drop: halfbacks
   about 13–14 deep and wide, safeties about 16–17 deep inside (`RH → (14.0, 14.6)`, `LH → (13.5, −13.6)`).
   Also note in the caption that against a run the dropping ends become the force/contain players (that is
   the trade the text names).

8. **Gillman: give the mechanism, not just the slogan.** One sentence: Gillman tied each route's depth and
   break to the quarterback's drop (3-, 5- and 7-step) so the ball came out on rhythm, and he numbered the
   routes so a call could name them (an early form of the route tree). That is what Coryell and Walsh
   inherited, and it sets up 11-02.

9. **Drill 1 (wildcat) answer.** Third-and-1 near midfield against a *base 4-3* is fine, but a coach would
   add the real modern reason the look works: the unbalanced line forces the defense to re-declare its
   strength before the snap, and a defense that doesn't shift is outnumbered (exactly what Fig 11 shows:
   the SS is still on the left over Z). One sentence.

10. **"Cover 2 ... a middle linebacker dropping deep" (cause 4, line ~1162).** That is specifically the
    Steelers' version with Jack Lambert, the ancestor of Tampa 2, not Cover 2 in general. Say "and, in
    Pittsburgh, a middle linebacker (Jack Lambert) who ran deep down the middle".

11. **"Fearsome Foursome" in the 1970s list.** The Rams' line peaked in the 1960s (Deacon Jones left after
    1971). Either swap in another 1970s line or say "the Rams' Fearsome Foursome, still going early in
    the decade".

12. **Term links:** "buck sweep" (Watch for it) is owned by 03-05 and isn't linked. Link it to
    `../03-the-run-game/03-05-perimeter-and-misdirection.qmd`.

## Diagram polish (labels and collisions)

- **Fig 3 (single-wing strip), panel 1:** the ball sits on the defensive "G" label over the center. Start
  the defensive guards at d=1.3, or draw the ball under the defender boxes.
- **Fig 4 (T counter), panels 1–2:** the two defensive "G" boxes at ±0.9 touch, and the ball overlaps the
  left one. Use ±1.2 for the defensive guards.
- **Fig 5 (umbrella), panel 2:** the offensive Y is hidden under the dropping right end's ring. Delay
  dRE's drop by 0.2 s or move Y to w=9.6.
- **Fig 8 (Gillman):** the X comeback's arrowhead touches the "intermediate" band label, and the Y dig's
  arrowhead lands on the FS box. Move the band labels to the right edge (w≈+16) and end the dig at
  (13.0, −4.0).
- **Fig 11 (wildcat):** the line-to-gain (gold, at 1 yd) runs straight through the four DL label boxes.
  Either draw `to_go=None` and say "third-and-1" in the caption, or put the DL at d=1.3.
- **Fig 10 (hashes):** "ball on the hash" sits close to the top edge of the strip; nudge it down ~0.5.
- Everything else is clean: no labels clipped by the field edge; the strips (Figs 3, 4, 5) each tell
  the story in four numbered frames; there are 3 animations, under the limit.

## Checked and correct (no change)

Single-wing personnel and depths (Fig 2); seven on the line with only the end men eligible in every
formation (the `check_legal` guard is good practice); man-in-motion counter logic and blocking (Fig 4);
Lombardi sweep assignments (Fig 6); Flex alignment and gap ownership, all seven gaps (Fig 7; strong-side
DE and weak-side DT flexed, matching period descriptions); shotgun drill alignment and the "rush the
center" answer (Fig 12); the 1972 hash geometry (Fig 10); the chuck-rule sequence 1974 → 1977 → 1978; the
points chart and its annotations (Fig 9); the timeline (Fig 1).
