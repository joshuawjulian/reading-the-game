# Coach / film-analyst review: 01-06 How to Watch a Broadcast Like You Mean It

Reviewed 2026-10-06 against AUTHORING.md, FACTS-current.md, the 01-06 spec, 02-02 (which owns
"split" / "reduced split") and the rendered `pdfs/01-06-how-to-watch-a-broadcast.pdf`. I looked
at every figure, rasterized at 90–200 dpi. The chapter is strong: the camera-footprint idea, the
"watch one thing" table and the bar-to-beat ladder are excellent teaching. The problems are a few
football-logic errors in the drills, two misleading defender placements, and some missing
nuance that a coach would insist on (play-action and RPOs break the "line goes forward = run"
read). Everything below is a concrete fix. I did not edit the chapter.

## A. Correctness: fix before publishing

1. **Answer 2 points the wrong way (around line 1185).** "For your log this should *lower* your
   confidence in a pass on first down … a defense that adds a man near the line is often
   inviting the throw." Those two halves contradict each other, and the first half is backwards.
   A one-high shell with a seventh man in the box is exactly the look offenses check *out of*
   the run against. RPOs throw behind that safety, and run/pass checks go to the pass ("run
   against two-high, throw against one-high"). Fix: "Nudge your lean *toward* pass, but only a
   little. With eight seconds left the quarterback may not have time to check, and the
   walk-down may be a bluff. A defense that adds a man near the line is often inviting the
   throw."

2. **Predict 2 figure: no one is left in the middle of the field.** The SS walks down to (8, 5),
   but the FS stays at (13, −9.5), outside the left hash. The answer says "the deep part of the
   field now has only one safety, *in the middle*." As drawn, the defense has no middle-of-field
   player and the whole right half of the deep field is empty, which no defense would line up
   in. Fix: also move the FS to about `d=14, w=-1.5` and draw a ghost plus a dashed arrow for
   him too ("FS slides to the middle"). Or keep him at the hash and say in the caption and the
   answer that he will rotate to the middle at the snap. The first option is clearer for
   Level 1.

3. **Predict 3 figure: the left corner is covering nobody.** X is moved to `w=-7.8`, but LCB
   stays at the default `w=-15` (seven yards outside the man he covers, visible on p.17). Fix:
   `dfn = [p.moved(w=-8.8, d=6.5) if p.key == "LCB" else p for p in dfn]` (slight outside
   leverage on a reduced split). Consider also moving the FS to `w=-7` (backside safety
   cheating toward the isolated receiver), which is a real tell in its own right.

4. **Reduced-split meaning contradicts itself and the owning chapter.** 02-02's glossary
   (the owner) says a reduced split means "a block on the inside or a route breaking toward the
   sideline." The 01-06 splits section says "crack block, crossing route, or room outside." The
   Predict 3 answer says "a route that breaks inside (a slant or a dig)." A slant is the
   *weakest* fit, because a reduced split shrinks the inside space a slant needs. Coaching
   convention:
   - **Reduced:** crack block; digs and shallow crossers (shorter trip); out-breaking routes
     (out, corner, comeback) that need room to the sideline.
   - **Wide / plus split:** verticals; inside breakers that want space (slant, post, dig); a
     clear-out; screens and hitches. Out-breaking routes are *cramped* from a wide split.

   Fix the panel C label for "wide" (drop "quick outside"; use "deep, or breaking inside, or
   clearing space"), the bullet in "Receiver splits", and Answer 3 ("set up for a dig or crosser
   underneath, an out-breaking route like a corner, or a crack block if the run comes his way").
   Also link "reduced split" to `02-02…#gl-reduced-split` instead of plain bold.

5. **Shot play (figs 2 and 4): X is wide open deep and nobody seems to care.** X runs `go(24)`
   and parks at d=24, while LCB stops at (19, −15.5) and FS at (19, −6). In the "On the
   replays" panel, the receiver labeled (8) is five yards behind both deep defenders on his
   side. That is a blown two-high coverage, and it sends a reader looking at the wrong lesson.
   Fix: `p.path("LCB", [(25.5, -15.5)], speed=7.0, absolute=True)` and
   `p.drop("FS", (22.0, -8.0), speed=5.0)` so the corner stays on top of X, and the H seam (18)
   has the FS over it. Alternatively, change X to a `comeback(14)` so he is underneath.

6. **"Line goes forward = run" needs the play-action and RPO caveat (fig 4 caption, the "No
   idea" and "Run" rows of tbl-one-thing, the takeaways).** The chapter itself says 82% of
   under-center dropbacks are play-action, and in those plays the line fires out on purpose. A
   coach would teach the **high hat / low hat** read and its PA refinement. On a real run the
   linemen drive forward *and climb to the linebackers*. On play-action they fire out low but
   stop at the line, because an offensive lineman more than one yard downfield on a forward pass
   is illegal. On RPOs the line run-blocks while the QB throws. On screens the linemen let
   rushers through and then release. Add one sentence to the table's "No idea" row ("if they
   fire out but never get past the line, think play-action"), and a "usually" in the caption.

7. **Win probability "is not a judgment about these two teams" (glossed-numbers bullet).** Many
   broadcast and public models (ESPN's; nflfastR's `vegas_wp`) start from the pregame point
   spread or a team-strength rating and then update on the situation. Fix: "Mostly about the
   situation; many models also start from the pregame betting line, so a little about the
   teams." Leave the details for 13-03.

8. **Play-action "needs" a working run game (Rams film room).** "An under-center offense that
   runs well trains the defense…" and "when an under-center team is having a good day running,
   the play fake is coming" present a play-caller tendency as cause and effect. Public analytics
   work has repeatedly found that play-action's effectiveness does *not* depend on how well, or
   how often, the team has been running (e.g., Ben Baldwin, Football Outsiders, 2018; Josh
   Hermsmeyer, FiveThirtyEight, 2018). The fact-checker must verify these before citing. Keep
   the tendency ("play-callers often reach for the fake after a good run") and add the
   counterpoint in one sentence. It reinforces the chapter's own "tells are odds" theme. The
   alignment tell (under center, so the defense expects run) is the real mechanism. Also, PA
   chiefly attacks the **linebackers'** eyes (the throw goes behind them), so "watch the safeties
   on the snap after a big run" should be "watch the linebackers' first step, then the safety."

## B. Missing nuance a coach would insist on

9. **Short yardage kills the stance tell (Predict 1 answer).** On third-and-1, every lineman is
   in a heavy three- or four-point stance, including on play-action, because play-action
   protection on short yardage fires out too. So "heavy hands" adds almost nothing *in that
   picture*. The useful stance tells come on normal downs, where the stance varies. Rewrite to:
   "the heavy hands agree, but on short yardage everyone is heavy, so don't give them much
   weight." Also mention the **QB sneak**: from under center on third-and-1 a sneak is a big
   share of the runs (and it counts as a run in the log). The fact-checker can pull
   `is_qb_sneak` per FACTS §5 if a number is wanted.

10. **Stance section, modern reality.** "Linemen on both sides mostly use three-point stances"
    is dated for the 2025 NFL. Interior linemen are mostly in three-point stances. Offensive
    tackles in shotgun offenses are often in two-point stances on most snaps. Many edge rushers
    stand up (two-point), especially in odd fronts. Add the tells coaches actually look for on
    film, at one line each:
    - **Tackle's stagger.** A deeper back-foot stagger means a kick-slide pass set.
    - **Guard tipping the pull.** Weight leaning, or eyes toward the pull side, means
      power/counter that way.
    - **A team that stands up only on passes.** If its linemen put a hand down only for runs,
      the stance itself is the tell.
    - **Defensive line, in reverse.** A DT sitting back may be about to loop on a stunt, not
      only drop or play the run.

11. **Scorebug walk-through: the two-minute warning.** At 2:41, the two-minute warning is
    effectively a fourth timeout for the offense, and every coach would mention it. Add it to the
    clock item and the example: "and the two-minute warning will stop the clock for free, so a
    run is not crazy. But third-and-6 is still a passing down." Optionally, also note that on a
    fourth-and-short at the opponent's 34, a modern coach may go for it rather than kick the
    51-yarder.

12. **Opening hook does not match its own simulation.** The hook is third-and-6 from (implicitly)
    the shotgun, and the analyst says "the safety bit on the play fake." Play-action on
    third-and-medium is uncommon, and the simulated play (shot_play, shotgun, no fake) has no
    fake. Either change the analyst's line to "the safety jumped the underneath route" (which
    matches the figure), or make the hook "second-and-6" under center. If you change it, update
    the Rams film room's callback ("that is the 'bit on the play-action' moment from the
    opening").

13. **Base defense in figs 1 and 2: H is unaccounted for.** With nickel at w=+9.5 over Y and the
    WILL at w=−2, nobody is within seven yards of H (w=−9) except the FS at 13. Real 2-high
    nickel teams *apex* the WILL between the LT and the slot. Fix in `base_play()`: add
    `"WILL": dict(d=5.0, w=-5.5)`. He stays inside the TV trapezoid, so the count of 16 is
    unchanged. Update `p.drop("WILL", …)` in shot_play if needed.

14. **Tells card B: depths contradict the text and 02-02.** The text says gun QB about 5 yards,
    pistol QB about 4 yards with the back at 6–7, and under-center back at 6–7. 02-02 says 7.
    The panel draws gun QB about 3.7 yards behind the line, pistol QB about 2.6 with the back
    about 5.6, and under-center back about 5.6. The pistol QB is therefore barely deeper than
    under center, which defeats the panel's point. Fix the tuples: shotgun `qb_d=-5.0`,
    `rb=(1.5,-5.0)`; pistol `qb_d=-4.0`, `rb=(0,-7.0)`; under center `rb=(0,-7.0)`. Then move
    the name and rate text down (about −9.5 and −11) and the footnote line to about −13.5, and
    set `ylim` to about (−15, 3.5). A small 5-yard tick on the side would help.

15. **Tells card A: the two-point figure.** The "two-point upright" figure reads as a person
    walking. A lineman's two-point stance is a crouch: feet wider than the shoulders, knees
    bent, hips at about knee height, back at about 45°, hands relaxed at or inside the knees.
    Redraw it so the contrast with the three-point figures is about the hand, not standing vs
    crouching.

16. **Predict 3 caption: say the trips includes an attached TE.** The three receivers to the right
    are Y (in-line), H and Z. Write "trips to the right with the tight end attached (Y, H, Z)" so
    the reader does not look for three wide-outs.

17. **Watch-for-it drill: spikes and log row 4.** Skip **spikes** too, not only kneel-downs. In
    the paper log, row 4 ("shotgun, no back", 75%) undersells empty, one of the most pass-heavy
    looks in football. Either raise it to 85–90% or let the fact-checker give the 2025 empty
    pass rate (`n_offense_backfield == 0` in FTN, which the chapter already loads).

## C. Diagram mechanics (labels, clipping, collisions)

18. **Fig 4 (where-to-look), "Ball in the air":** the catch-point ellipse reaches the top of the
    window, and badge 5 sits *above* the drawn field. In "On the replays", badge 8 sits on the
    "50" numeral. Fix: widen `WIN` to `(-9.5, 42.0)`, which also helps fig 2 panel 4. Move
    badge 8 to `badge_at=(d + 3.6, w - 3.8)` (the inside of X), or nudge it off the numeral.

19. **Fig 1:** "◄ camera: high on this sideline" sits against the left field edge and straddles
    the dashed All-22 line. Move it to about `(-5.6, -19.5)` (inside the grey, below the
    off-screen box), or shorten it to "◄ camera side".

20. **Fig 3 (scorebug):** the possession football overlaps the "HOME" text. Shift the ellipse to
    `x≈17.9` and the HOME text `dx≈1.4`, or put the ball on the left of the score chip.

21. **Fig 10 (Predict 2):** the "showed two deep…" label sits about 1 yard from the top edge.
    Widen to `window=(-8.5, 19.5)`.

22. **Fig 4 general:** at print size the markers are tiny in the 2×2 grid. Acceptable, but if you
    rebuild, consider `figsize=(6.5, 6.6)`.

## D. Checked and fine

- **Legality.** All formations are legal. gun_2x2 has X and Z on the line with H and Y off.
  i_form_22 has U and Y on the line with Z off. gun_trips has X and Y on the line with H and Z
  off.
- **Alignments.** Safety depths (13), corner depths (6–7), the I-formation fullback (4.5) and
  tailback (7) depths, and the 9-defenders-within-5-yards count in Predict 1 are all correct.
  The DL techniques are sensible: over front with a 3-technique to the strength.
- **Camera geometry.** The near-narrow / far-wide trapezoid is correct for a press-box camera,
  and the count of 16 on screen matches the drawing.
- **Animation.** One animation (well under the cap of 4). The frame-strip times (−1.0, +1.4,
  mid-flight, catch) tell the story in print, and the roughly 2-second hang time on a 40-yard air
  throw is realistic.
- **Facts.** The coaches-film description (All-22 + high end zone, no replays) is correct.
  Skycam and yellow-line history, the NGS definitions, and the ladder and situational numbers
  were already verified in 01-06-factcheck.md. The 51-yard field-goal arithmetic is right. NFL
  numbers sit 12 yards from the sideline, so panel C and gridiron are consistent.
- **Film rooms.** Prime Vision and the Rams 2025 under-center rates are well chosen and
  accurately characterized, apart from the causal framing in A8.
