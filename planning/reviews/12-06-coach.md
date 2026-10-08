# 12-06 coach / film review: The Eagles: Trenches, RPOs, and the Tush Push

Reviewer stance: veteran NFL coach and film analyst. I checked technical accuracy, every diagram (PDF rasterized
at 80 and 120 dpi; all 8 figures viewed) and missing nuance. The prose is strong and the data sections are honest.
The problems are in the diagrams: one depicts an illegal play, and two contradict their own captions or answers.

## Critical (the football in the diagram is wrong)

1. **Philly Special, panel 3: the pitch goes forward, which would make Burton's throw an illegal second
   forward pass.** At the exchange (t = 1.0 to 1.15), Clement (RB) is at d ≈ −6.4. Burton (Y) is at d ≈ −4.6 to
   −5.0, so the ball travels about 1.5 yards *toward* the line. The rasterized panel 3 shows this: Y holds the
   ball clearly above R. On the real play the toss was backward or level. That legality is the whole reason
   Burton is allowed to throw.
   *Fix:* keep Burton deeper than Clement through the exchange. For example, change Y's keyframes to
   `(0.5, -4.2, -6.4), (1.0, -6.8, -3.8), (1.3, -7.0, -1.2), (1.7, -6.8, 1.4), (2.0, -6.2, 3.2)`, or pull
   Clement shallower (RB at `(1.0, -5.6, -3.4)`), so the pitch is level or backward. Add a sentence in step 3:
   "the pitch has to go sideways or backward; a forward toss would be the play's one forward pass, and Burton
   could not throw."

2. **Predict the play 1 (2017 RPO) counts Y twice.** Y is a flexed tight end at w = 6.6, outside the nickel
   (w = 5.6). The answer counts him as one of "three receivers outside the box" and also as one of "six
   blockers" against a seven-man box. He cannot be both. If Y is part of the screen, the run has 5 blockers
   against 7.
   *Fix (cleanest):* attach Y on the line at w ≈ 4.8, move Z off the line at w ≈ 16.5 so X and Y are the ends
   and the formation stays legal, and put H in the slot at w ≈ 10.5. The count then reads: box 4 DL + W + M +
   nickel = 7 against 5 OL + Y = 6 blockers. Outside on the right: H and Z against the CB and a 9-yard SS, so the
   throw is right. Update the caption ("two receivers to the right, tight end attached") and the answer to
   match.
   Also, the caption says the QB "decides after the snap", but the answer is a pre-snap box count. Say both:
   the count can be made before the snap, and the post-snap read of the nickel confirms it. That is how the
   2017 Eagles' alerts and RPOs worked together.

3. **Fig 5 (Super Bowl LIX four-man rush): the caption describes routes that aren't drawn.** "Every route has a
   defender above or beside it" is stated, but no receiver has a route. Only the dropback and the RB check
   are drawn. *Fix:* draw a plausible KC dropback concept against quarters, e.g. X 12-yard dig, H seam, Y
   option at 6, Z curl at 12. Each should end inside or under an oval. Alternatively, rewrite the sentence
   ("every area a receiver can reach quickly has a defender in or above it").

4. **Fig 2 right (outside zone): the blocking assignments don't add up.**
   - RT (w 3.2 → (0.4, 4.6)) steps into empty grass between the 3-technique and the E. No defender is there.
   - The Mike (M, w 1.4) is unblocked. The caption's "six blockers against six" therefore isn't drawn.
   - The center steps playside to (0.3, 0.2), *away* from the backside-shaded NT (w −0.8). LG leaves
     immediately for the Will, so nobody blocks the NT.
   - LT ends at w −1.9, which cuts off nothing.

   *Fix (standard wide zone right vs this 4-2):* LT scoops the backside B gap to about (0.4, −2.2). The
   backside E is left unblocked; say so, see nuance 11. LG and C combo the NT: C reaches his playside shoulder
   at about (0.4, −0.3), and LG overtakes then climbs to the Will at about (3.6, −2.0). RG and RT combo the
   3-tech: RG reaches to about (0.4, 2.9), and RT climbs to the Mike at about (3.6, 1.8). Y reaches the E at
   (0.4, 6.6). Draw the two climbs with the same green dashes as the duo panel. "The whole line steps right"
   is then true *and* every second-level player has a hat.

## Major

5. **Philly Special pre-snap timing shows an illegal shift.** Foles's walk-up is a shift. All 11 must then be
   set for a full second before the snap. In the keyframes he arrives at t = −0.7, and panel 1 (t = −1.1)
   still shows him moving. *Fix:* start the walk at −3.2, have him set by −1.4, and draw panel 1 at about −1.0
   so he is standing set with the dashed walk path behind him. Pass `t_first` as `-3.6` to `set_tracks`, and
   change the first keyframe of `ease` to match. Add a note to step 1: "set for a full second, as the rules
   require after a shift".
   Also, the caption says Clement "has motioned in", but the animation shows no RB motion: R starts at
   (−6.0, 0) and never moves before the snap. Either delete "who has motioned in" or animate it. If you animate
   it, make sure only one player is moving at the snap. I couldn't confirm a Clement motion from memory, so
   check the film or the NBC Sports breakdown before keeping the claim.

6. **"Blitz" is glossed wrong.** The text says a blitz is "any rusher beyond the defensive linemen". The
   owning glossary entry (02-05) defines it as **five or more rushers**, and that is also the Next Gen Stats
   definition behind "zero blitzes". Under the chapter's gloss, a simulated pressure (a linebacker rushes and a
   lineman drops, so four rush) would count as a blitz. That muddles the Super Bowl story and Predict 3.
   *Fix:* use the glossary wording. Add one clause saying the four were "usually, though not always, the four
   down linemen". FTN's `n_blitzers` counts non-line rushers, so note in [^lixftn] that FTN's single "blitz"
   could be a sim rather than a fifth rusher.

7. **Predict 3 (double-A-gap mug) is not a Fangio picture.** Fangio's signature, and the Eagles' Super Bowl LIX
   plan, was the opposite: a quiet two-high shell, linebackers at normal depth, nothing shown, four rushing.
   Double-A mugs belong to Spagnuolo, who coordinated KC's defense, and to Macdonald. Captioned "Super Bowl LIX,
   the Eagles show six players at the line", it implies a game plan I can't confirm.
   *Fix:* either (a) relabel the drill as a hypothetical ("third-and-9 against a Fangio-style defense") and
   keep the mug, or (b) redraw with W and M at 5 yards, two-high at 13, and the question "how many rush?". The
   lesson is then "a Fangio defense shows nothing and rushes four".
   Either way, tighten the answer's logic. The real gain from a mug is that KC must keep the RB in to have six
   blockers for six potential rushers, so only four receivers release into seven defenders. When the mugged
   linebackers drop, the center and guards are freed to *double* a tackle, so "a one-on-one they wouldn't
   otherwise see" is not automatic. The rush wins by running a twist into a protection that has slid the
   wrong way.

8. **Fig 3 (OC churn): the "designed runs" line includes the tush push.** Sneaks are designed runs, and the
   Eagles ran about 30–40 a year at high success and high EPA on 1 yard to go. That inflates the run line
   exactly where the text credits "the line, more than the coordinator". *Fix:* exclude `SNK`-flagged plays from
   `RUNS` for 2022–25, or plot a third faint "runs excluding sneaks" line. Then say whether the conclusion
   survives. It probably does, but the reader deserves to see it.

9. **Fig 5 draws quarters as spot-drop zone.** The four deep defenders bail to fixed spots 15–16 yards deep. In
   Fangio's quarters and Cover 6, the safeties read #2 and fit the run or carry the seam, and the corners play
   MOD/MEG technique. It is pattern-matched coverage. *Fix:* in the caption, say "the ovals are the areas each
   defender starts responsible for; in Fangio's match quarters the safeties read the slot receiver and can
   come down hard (see 06-05)". Optionally, start the safety drops at 12 → 13.5 rather than 16.

## Missing nuance a coach would insist on

10. **Super Bowl LIX was a matchup, not just a roster.** KC's left tackle problem forced Joe Thuney (an All-Pro
    left *guard*) to left tackle late in 2024, and he started there in the Super Bowl. That weakened the
    interior and the edge together. It is the reason "four can win" was true *that night*. One sentence, after
    fact-check. Also, Zack Baun was signed as an edge/special-teams player, and Fangio moved him to off-ball
    inside linebacker. That is a coaching-development story that belongs in the roster-building thesis.

11. **Outside zone: the unblocked backside end.** On wide zone, the backside end is usually left alone, and the
    QB's keep or boot threat holds him. That is the "QB as an extra blocker" idea from the previous section
    applied directly, so tie the two together. Add the third RB read too: bounce (drawn), bang (drawn) and
    *bend*, the cutback, which is what light boxes over-pursuing outside zone give up most.

12. **Duo's family.** The chapter files duo under Gap Schemes, and the prerequisite chapter does the same. Many
    staffs (Shanahan trees, most college coaches) teach duo as an inside-zone cousin, "power without the
    puller". Add one clause so a reader who hears it called a zone play isn't confused.

13. **Tush push mechanics, one sentence (10-03 owns the rest).** The Eagles' edge was the center and the
    *guards* firing low on the first sound, Hurts taking the snap already in his squat, and the pushers
    aligned to drive his hips rather than his back. "Kelce quick and low" names only one of the three moving
    parts.

14. **A concrete "how opponents responded" film example.** The paragraph is generic. A strong candidate: the
    2024 Commanders, with Frankie Luvu's legal hurdles over the pile in the regular season and repeated
    neutral-zone/offside flags on push attempts in the January 2025 NFC Championship. Verify the counts before
    using it. Also say that leaping over the line is legal on scrimmage plays but has been banned on field
    goal and extra-point tries since 2017, so readers don't conflate the two.

15. **Philly Special panel 4 vs the caption.** The caption says "nobody within three yards" of Foles. The W ends
    at (2.0, 3.1), about 2.9 yards from Foles at (2.7, 5.9). Move W's last keyframe to about (2.0, 1.6).

## Small checks

- Stoutland: the chapter says 13 seasons, and the table gives 2013–2025, which is 13 seasons inclusive.
  FACTS-current §9 says "after 14 seasons". The chapter's count looks right, so ask fact-check to correct
  FACTS-current or the chapter, whichever is wrong.
- The RPO and SB-LIX figures' formations are legal: 7 on the line, ends eligible. Predict 2 is fine (6 v 6,
  two-high at 12.5). The duo panel is correct: C+LG on the 1-tech, RG+RT on the 3-tech, Y on the end, climbs
  to W and M, and the back offset away and reading the Mike.
- Labels: no field-edge clipping and no collisions in any figure. Frame-strip timing (−1.1, 0.6, 1.1, 2.6)
  tells the story in print, apart from items 1 and 5.
- Text facts I'd expect fact-check to confirm, and which read correctly to me: Peters's injury on Oct 23, 2017;
  4th-and-goal from the 1 at 0:38, 15–12; Hurts 17/22, 221 yards, 2 TD and 72 rushing; DeJean's 38-yard
  pick-six on his birthday; four 2022 double-digit sackers; Kelce's six first-team All-Pros; 2021 at 2–5 → 9–8.
