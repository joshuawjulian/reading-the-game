# 04-07 Quarterback Play: coach / film-analyst review

Reviewed: chapters/04-the-passing-game/04-07-quarterback-play.qmd and pdfs/04-07-quarterback-play.pdf
(24 pages, rasterized and checked page by page; all 15 figures looked at).

Overall: strong chapter. The clock, climb/slide/escape, the scramble-drill rules, the throwaway and grounding
section and the checkdown-as-risk-management framing are all sound football. The frame strips tell their stories
in print. Most diagrams are legal and believable. Fixes are listed by priority.

## A. Must fix (accuracy or consistency with prerequisites)

1. **"He reads defenders, not receivers" contradicts 04-01.** 04-01 teaches *progression reads* (which receiver
   is open, one at a time) and *defender reads* (watch one conflict defender) as two different things
   (04-01 lines ~893-897, 1038ff). 04-07 states as a universal rule that the QB reads defenders, and repeats it in
   the Takeaways ("He reads defenders, not receivers"). Coaches would say: on a progression he looks at receivers'
   *areas*, and each look is answered by where the nearest defender is; on a read concept he keys one defender.
   Fix: rename the paragraph to "Every read has a key defender" and open with "Even on a progression ([Passing
   Game Fundamentals](04-01-passing-fundamentals.qmd) separated progressions from defender reads), each look is
   answered by one defender..." Change the takeaway to "Each read is answered by a defender."

2. **Fig 2 / Fig 3: dagger is drawn against one-high (Cover 3) with a 14-yard dig.** 04-04 defines dagger as
   "built to beat two-high coverages" with a 15-18-yard dig that "takes a deep drop and three seconds" (04-04
   glossary and lines ~1033, 1065, table line 1728). Here it is run against single-high, dig at 14, ball out at
   2.1 s off a gun 3-step. A coach reading both chapters sees a contradiction. Two options:
   - (preferred) Play it against two-high (Quarters or Cover 2, as 04-04 drew it): SS and FS at 12-13 yards,
     +/-9 from the ball; ring the **right-side safety** as read 1's key (does he carry Y's seam?), keep the
     **Mike/nickel hook** as read 2's key. Push Z's break to 15-16 yards, give the QB a gun **5-step** (to ~9
     yards, ending ~1.9-2.0 s) plus a hitch step, and release at ~2.4-2.5 s ("anticipation") vs ~3.1 s ("see it").
   - (minimum) Keep the Cover 3 look but say so in the caption and text: "Dagger is a two-high beater
     (Dropback Concepts); against single-high the seam is carried by the free safety, so the dig into the
     hook-curl window is the throw," and lengthen the dig to 15+.
   Also: the sim QB finishes his drop at 0.95 s but panel 2 (+1.2 s) says "last step of the drop". Per 04-01 a
   gun 3-step ends ~1.45 s; move the drop end to ~1.3-1.45 s (or the panel time to ~1.0 s).

3. **Burrow film room contradicts Fig 8.** "He did it in the pocket. Burrow is not an escape artist" — but the
   chapter's own Fig 8 puts Burrow *above* the diagonal (better outside the pocket than in it, ~+0.18 vs +0.13),
   one of only 11 QBs. Burrow is also known for spin-outs and extended plays. Fix: "Burrow can extend plays (he is
   one of the few above the diagonal in Fig 8), but his 2024 season was built in the pocket: anticipation ... and
   subtle movement ..." Delete "not an escape artist."

4. **History overstated: "for the next forty years ... the scrambler the exception" and NFL offenses only
   learned to coach improvisation "in the last decade."** NFL teams have practised scramble rules for decades:
   Walsh's/Seifert's 49ers with Steve Young, Elway's Broncos, Favre in Green Bay, Randall Cunningham, Roethlisberger's
   Steelers (two titles built partly on extended plays), Russell Wilson's Seahawks, Aaron Rodgers. Fix: keep
   Tarkenton -> Montana/Manning/Brady as the pocket ideal, but add one sentence naming the off-script line
   (Elway, Young, Favre, Roethlisberger, Wilson, Rodgers) and reframe the recent change as *scale and
   normalization* (spread-raised QBs, scramble drill as a weekly emphasis, offenses designing for it), not invention.
   Any new names need sources per AUTHORING §6.

5. **Purdy wording overstated twice.** (a) "NGS ... ranked his CPOE only 5th that season, well below the nflverse
   model's ranking" — 5th vs 1st is not "well below"; say "5th rather than 1st". (b) "Purdy sits deep in the
   bottom-right corner" of Fig 12 — he is far right but only just below the aDOT line (≈7.6 vs ≈7.85). Say "at the
   far right, just below the average depth line."

6. **Watch-for-it timing contradicts Fig 1.** "Ball out before two: quick game or first read." Fig 1's own median
   first-read throw is 2.3 s. Fix: "Ball out by about two and a half: quick game or first read. Out after three:
   off schedule, or a deep shot with max protection."

7. **Fig 1 phase bar implies the drop starts after the rush count.** "Count the rush" (0-0.6) then "Drop" (0.6-1.7)
   reads as sequential; the count happens *during* the first steps of the drop. Fix: make "Count the rush" a
   thin band above/overlapping the start of the drop bar, or relabel the first block "First steps of the drop:
   count the rush". Minor: the vertical grid lines run through the phase-bar labels; set zorder of the bars above
   the grid or turn off x-grid in the top band.

## B. Diagram fixes

8. **Fig 7 (scramble drill strip): label collisions.** Panel 2: Y and SS squares touch; QB's "Q" touches the RE
   square. Panels 2-3: "$" and "W" overlap. Panel 3: the two "E" squares sit on top of each other under Q. Fix:
   nudge LE's late path (e.g. finish at (-7.0, 8.0) not (-6.6, 9.2)) so the two ends are ~1.5 yd apart; trail SS
   0.8 yd further outside Y (w +1.0); move NB to w-1 behind H. Also state in the caption what the Will does: R
   stays in to block, so the Will (his man-coverage assignment) mirrors/spies the QB — that is what his path shows.

9. **Fig 3 right panel: Z's circle is hidden under the Mike square** at the catch (the 1.1-yd point). Draw Z at a
   higher zorder or offset the Mike by ~0.5 yd so the reader sees both. Left panel: the ringed FS sits visually
   right on top of Z while the caption says "room to spare"; with 2.6 yd say "a step to spare" (or let the
   two-high rebuild in item 2 change the picture).

10. **Tackle box drawn through the tackles' centers (±3.2).** The rule (Rule 3-25) is the *outside edges* of the
    normal tackle positions. Widen the shaded box to about ±3.8-4.0 in Figs 4, 9 and 14 (`(-0.7, ±3.2)` ->
    `(-0.7, ±3.9)`).

11. **Fig 4 escape panel.** The DT is in the right A/B gap and the QB escapes right, passing ~3 yards behind him.
    Legal and possible, but the principle the text teaches is "interior collapsed -> escape outside the tackle on
    the side the end was run past." Make the picture unambiguous: put the penetrating DT over the center
    (w ≈ 0 to -0.5, driving the C or LG back) so the choice of side is decided by the ends (LE inside on the left,
    RE pushed past on the right). No other changes needed.

12. **Fig 6 (scramble rules plate) leaves R standing with no rule**, and the text has no rule for linemen. Add a
    fifth, short rule and a small green arrow: "R: if he stayed in to block, he leaks to the scramble side, short,
    as the outlet." In the bullet list add: "Linemen stay on their men and do not drift downfield; if the ball is
    thrown past the line, an offensive lineman more than a yard downfield is a foul." (Cite the ineligible-downfield
    rule if added.)

13. **Predict 3 answer: X and Y end on the same level.** X "comes back" from 19 yards and Y crosses "at about 12";
    say X settles at 8-10 yards so the four levels are H deep, Z deep-crossing, Y ~12, X ~8-10. Add the coaching
    point a QB coach would insist on here: a right-handed QB rolling *left* has to open his hips and square his
    shoulders to throw, which is exactly why the come-back routes on that side matter more than the deep ones.

## C. Missing nuance a coach would insist on (add a sentence each)

14. **Progression order is timed, not only ranked.** "Deep to short" is common, but many concepts read short to
    deep (stick: flat then stick; smash vs some looks; hi-lo reads of the flat defender), and the real rule is that
    each read is built to come open *as the QB's feet get to it*. Add to "The order is a ranking of risk and
    reward": "...and a timetable: each route is built to come open as his feet arrive at that read." Mention
    half-field vs full-field progressions in one clause with a link back to 04-01.

15. **Step 0: the pre-snap job.** The clock starts at the snap, but the QB's post-snap plan is set pre-snap: Mike
    ID and protection call (04-02), which half of the field he will work, any alert/shot check (owned by 08-01).
    One sentence before the numbered list, with links to 01-05, 04-02 and 08-01.

16. **Ball security when moving.** Every QB coach drills "two hands on the ball" when climbing/sliding/escaping;
    strip-sacks come from the one-handed carry. One line in the pocket section.

17. **The defense's side of the scramble drill.** Defenses have rules too: rush-lane integrity and contain (why the
    escape lane opens when an end rushes too far upfield), a **spy** (as in Predict 2), and "plaster" in zone
    (when the QB leaves the pocket, each zone defender locks onto the nearest receiver). One sentence in the
    "Why does any of this work?" paragraph; it also explains why Allen/Mahomes value comes against defenses that
    plaster poorly.

18. **"Off-script value" sentence is ambiguous about FTN.** "FTN charts whether the quarterback was outside the
    pocket ..., whether he left on purpose (a designed rollout) or by escaping" reads as if FTN distinguishes the
    two. It does not (the footnote says so). Fix: "...outside the pocket, whether by design or by escape (the flag
    does not say which)."

19. **Watch-for-it "long stare" bullet.** Add the third possibility: "or he was holding a defender with his eyes
    (a look-off, [Concepts Versus Coverages](../08-the-chess-match/08-01-concepts-versus-coverages.qmd))."

20. **"Hitch" means two things in this chapter.** The QB's *hitch* (step) and receivers' *hitch* routes (Figs 6,
    7, 15 and Predict 3). 04-01 calls the QB move a "hitch step (not to be confused with the hitch route)". Use
    "hitch step" for the QB throughout (clock list item 3, Fig 2 notes, Takeaways, Watch for it).

21. **Terminology links.** "Intentional grounding" (owned by 09-04) is bolded without a glossary link; link
    `#gl-intentional-grounding`. "man coverage"/"zone coverage" in the scramble section are bolded but not linked
    to their owning Part 6 chapters. "system quarterback" is bolded as if a term but is not in the term index;
    unbold or quote it.

## D. Checked and fine

- Formations legal in every diagram (5 OL + X + Z on the line; Y and H off). Four-man front alignments
  (1-tech, 3-tech, wide ends) realistic; pass-set depths and the tackles riding ends past the launch point are right.
- Climb strip (Fig 5) timing and story are good; Predict 1 picture and answer are correct (climb and slide left).
- Throwaway / grounding (Fig 9, Predict 2): rule statement, 2024 "any part of body or ball" wording, end-zone
  safety, and the FG-range logic are correct. Super Bowl XLVI safety correctly characterized.
- Film rooms: Manning 2013, Brady pocket economy, Mahomes left-handed flip (Oct 1, 2018 at DEN), Helmet Catch,
  Allen 2024 MVP all well chosen and accurately characterized (subject to fact-check). Burrow and Purdy need the
  wording fixes above.
- Charts (Figs 8, 10-12) are readable with no clipped labels; Fig 12 corner labels sit clear of points.
- No on-field label clipped by the window edge; the only collisions are those in items 8 and 9.
- Animation count: 3 (Figs 2, 5, 7), within budget.
