# Coach / film review: 12-02 Belichick and Game-Plan Football

Reviewer persona: veteran NFL defensive coach and film analyst. I read the full qmd (1,778 lines) and
the current PDF (`pdfs/12-02-belichick-patriots-game-plan.pdf`, built 07:20, a minute after the qmd's
last save). I rasterized it at 110 dpi and looked at all 11 figures (pp. 4, 6, 8, 9, 11, 13, 14, 16, 18–20).

Overall: the argument is right and well built. The three questions, "the concession is named", the
target being a person, and XLIX as preparation rather than the call are how Belichick's staffs really
talked. The data sections are honest about their limits. The problems are mostly in the
**diagrams' alignments**. In several places the picture contradicts the sentence next to it: corners
labelled "jam" standing 5.5 yards off, "every gap filled" with an uncovered guard, a right tackle
assigned to a wide-9 outside the tight end, and a caption saying "nobody deep in the middle" over a
free safety in the deep middle. All of these are easy fixes. Priority order below.

## A. Must fix (the diagram or text says something wrong)

1. **fig-liii-plan (top): "six on the line, every gap filled" is not what's drawn, and "nobody to climb to"
   is wrong.** As drawn, the widths are W −6.2, E −3.9, T −0.8, T 2.4, E 3.9 and S 6.5, against LT −3.2,
   LG −1.6, C 0, RG 1.6, RT 3.2 and Y 4.8. That leaves the **LG uncovered** (the T at −0.8 is a shade on
   the center), so LG and C have a clean combo onto the shade and LG climbs to the SS at 6.5 yards. The
   SS at (6.5, 0.6) and the $ are second-level players, so there *is* someone to climb to. The real
   coaching point behind a six-man line against outside zone is **cover every blocker**. With no
   uncovered lineman there's no double team (combo block) and no free climber, so every lineman has to
   reach his man alone, and the edge is set hard on both sides.
   **Fix (alignment):** W −4.4 (wide 5 on LT), LDE −2.2 (3-technique on LG), LDT −0.3 (shade nose),
   RDT 2.0 (3-technique on RG), RDE 3.8 (5 on RT), S 6.0 (9 on Y). That covers every one of the six
   blockers, and it also fixes the touching "T E" boxes on the right.
   **Fix (text, body and caption):** replace "every gap was filled at the snap and there were no
   linebackers to climb to" with "every offensive lineman had a defender on him, so there were no double
   teams and no free lineman to climb to the second level; the SS and the nickel are the only fitters left,
   and they come downhill late." Link [covered / uncovered lineman](03-01) and [combo block](03-01).
   Change the on-field label "five DBs behind: nobody for the line to climb to" to "no uncovered
   lineman: nobody free to climb".
2. **fig-liii-plan (bottom) versus fig-liii-data: four rushers versus 54% five-plus.** The diagram and
   the paragraph above it present the plan as "same six, four rush, zone behind" (a simulated pressure).
   Then the chart shows five or more rushers on 54% of dropbacks, and the text says New England blitzed on
   half its snaps. Both are true. The plan *mixed* sim pressure (show six, rush four, drop two) with real
   five-man fire zones and the Cover 0 at the end, and the mix *was* the disguise. As written, the reader
   meets a contradiction. **Fix:** retitle the bottom panel "One of the looks: show six, rush four"; in the
   caption add "On other snaps the same six sent five, with three under and three deep behind (a
   [fire zone](07-03)), or all six"; and in the paragraph after the chart, say plainly that the
   four-rush sim and the five-plus pressure were two halves of one disguise package. Also, "zone *and*
   extra rushers is giving up the safety net" overstates it. A 3-under/3-deep fire zone is a standard,
   sound call. The bill is the three-under spacing (the hook and seam windows), not the absence of a net.
3. **fig-xxv-plan (top): corners labelled "jam, then sit" are aligned 5.5 yards off.** You can't jam
   from there. The plan as drawn (four rush, five under, two deep halves) is Cover 2 with hard corners.
   **Fix:** LCB to (1.2, −14.2) and RCB to (1.2, 14.7), inside-shaded press on X and Z, then
   `p.drop` to about (5.0, −13.0) and (5.0, 14.0), the jam-and-sit flat corner. Keep the label, and move
   it to about (3.0, −10.5) so it's next to the corner rather than floating.
4. **fig-gronk (panel C) caption contradicts the picture.** The caption says "a cornerback underneath
   and outside", but the purple-ringed underneath player is the **$** (nickel). It also says "nobody deep
   in the middle", but the FS is at (13.5, −3.0), in the deep middle. What the bracket actually costs is
   the **underneath hole player (no robber or rat)** and a box short one defender. **Fix:** caption "a
   nickel back underneath and outside, the strong safety over the top", and "the other receiver (Z) gets
   a linebacker in man with no free defender underneath to help". The on-field label "no robber" is
   already right. Link [robber](06-02).
5. **fig-gronk (panel B) and Predict 2: the right tackle can't block a wide-9 outside the tight end.**
   `dl4()` puts both ends at ±6.0, which is outside an inline TE at ±4.8. In panel B the RT (3.2) is
   assigned the RDE at 6.0 across Gronkowski's face, and in Predict 2 the answer calls the $ "its edge
   player on the right" when the DE at 6.0 on the line is the edge. Against two attached tight ends a
   4-3 end plays a 5 or a 6/7 technique.
   **Fix:** add `dl4(end_w=3.9)` for the 12-personnel panels (B, C and Predict 2), keeping ±6.0 for
   spread looks (Predict 3). Then RT on RDE (5-technique), Y on the $ (now the true overhang/force
   player), and the run goes off tackle at the $ as the text says. In the Predict 2 answer, call the $ "the
   [overhang](02-05) / [force](05-05) player on the right", not "edge player", or keep the word "edge"
   only once the DE is inside.
6. **fig-xlix (strip): the W linebacker sits on the catch point, and the catch is 2 yards deep in the
   end zone.** LB4 drops to (2.4, 4.3), so in panel 4 the boxes for W, Butler's CB, H and the ball all
   pile up, and a reader sees a linebacker who could have made the play. The real point is that the slant
   window was open and only Butler closed it. The text says "intercepted at the goal line", but H's route
   ends at (3.0, 5.8), two yards into the end zone. **Fix:** goal-line linebackers read run. Send LB4
   downhill to about (1.3, 3.6), filling the C-gap (the "just play goal-line" instruction), and end H's
   slant at about (1.6, 6.2) via (−0.2, 9.4), (0.9, 8.2), so the catch point is at the goal line
   (d ≈ 1.2–1.6). Re-key Butler to finish at (cd + 0.1, cw − 0.5). Panel 2 also stacks Z, H, Browner and
   the purple ring into one blob. Start H at (−2.4, 9.2), a slightly wider stack, so the two receivers
   read as front and back.

## B. Should fix (missing nuance a coach would insist on)

7. **XXV: the bill was steeper than "4–5 yards", and that's the more interesting lesson.** Thomas
   averaged 9.0 yards a carry and scored on a 31-yard run. The plan held because Buffalo got so few
   *snaps*: the Giants held the ball for 40:33, so Buffalo had only a handful of possessions and ran only
   15 times with Thomas. The "4–5 yards" label is the plan's budget, not the result. **Fix:** add one
   sentence after "Thomas got his yards": "More than the plan budgeted (9 a carry, including a 31-yard
   touchdown), and that's where the other half of the plan paid: with the Giants holding the ball for
   more than 40 minutes, Buffalo had only N possessions." Check N on PFR's drive chart. Optionally relabel
   the bottom panel "the budget: 4–5 yards a carry".
8. **XXV: name the edge players.** The two standing outside linebackers in a 2-4-5 were the Giants'
   Hall of Fame front (Lawrence Taylor, with Carl Banks; Pepper Johnson and Gary Reasons inside). A
   film-room reader will look for #56. Verify each player's role in the Giants.com and ESPN sources
   before adding it. One clause in the Film room callout is enough.
9. **XXXVI bottom panel: nobody has Y.** Man assignments are drawn for X, Z, H and R, but the tight end
   is unaccounted for, and the M at (4.6, −1.4) is the only possible candidate. **Fix:** `p.man("MIKE",
   "Y")` and say in the caption "two-deep man (2-Man) underneath, with the dime on Faulk", linking
   [2-Man](06-04). This also makes the "jam everyone" picture coherent: it's 2-Man with press, which is
   exactly what you'd play to break Martz's timing while keeping two safeties over the top.
10. **XLIX: say how NE's stack rule differs from the textbook answer.** The standard man answer to a
    stack is a [banjo](06-02) (in/out switch at the release). New England's rule was different and more
    aggressive: re-route the point man (Browner) so the rub never forms, and let the back defender
    (Butler) play the first in-breaker without bailing. One sentence in "The preparation" makes the
    detail coach-accurate and links 06-02, which teaches banjo against stacks.
11. **LIII: the near-miss that shows the bill.** In the third quarter Goff had Cooks open deep in the
    end zone, and Jason McCourty closed from across the field to break it up. That is the zone/disguise
    bill almost coming due, and it is the best counter-example for the "Common misconception" logic
    (verify quarter and down in nflverse pbp `2018_21_NE_LA`). Also consider, after verifying, the
    widely reported point that New England held its final alignment until after the helmet radio cut out
    at 15 seconds, which is precisely why McVay's in-helmet help didn't save Goff. Add it only if a source
    supports it.
12. **Gronk dilemma: big nickel is missing.** The league's real answer to a "move" or "flex" tight end,
    and Belichick's own answer as a defensive coach, was **big nickel**: a third safety instead of a
    corner or linebacker, big enough to play the run and fast enough to cover. That breaks the base/nickel
    dilemma in panel D. **Fix:** add a fourth row to panel D, "Big nickel (3 safeties) | the honest
    answer: no mismatch to pick", and one sentence linking [big nickel](02-05). This also connects to the
    "versatile players" bullet in "What survives".
13. **"How opponents responded": hire-his-assistants list.** Add Joe Judge (Giants HC 2020–21) and Jerod
    Mayo (Belichick's successor in New England, 2024). Mayo's single season is the sharpest version of
    "takes the habits but not the building". Charlie Weis was a head coach only in college, so either say
    "head coaches in the NFL or college" or drop him. Manning beat New England in three AFC title games
    (the 2006, 2013 and 2015 seasons), not two.

## C. Polish (legibility, labels)

14. **Q over C in every under-center diagram** (figs 2, 3, 6, 9 and 10). `UC = -1.3` against
    `LINE_D = -0.7` puts the Q disc over the center's "C" letter, which renders as a garbled "Ç". Use
    `UC = -1.7`, or drop the C letter when the QB is under center.
15. **fig-liii-plan (bottom):** the "Jones ($): blitz look, then drops" box touches the right CB box.
    Move it to about (3.6, 14.6) with `ha="left"`, or widen `lateral` to (−13.5, 19.5). The "crosser meets a
    zone defender" leader ends on empty grass. Point it at the X route at about (9.0, 1.0), where the
    NB's drop arrow ends.
16. **fig-gronk layout:** panel C sits lower than panel D's heading, which leaves a blank band under
    panel A. Use `gridspec_kw={"height_ratios": [1, 1]}` with equal panel heights, or put the table panel
    in the same row as C (C | D) with a shared top.
17. **fig-xxxvi (bottom):** the "hit" badge sits on top of the R's release arrow. Nudge it to (−2.6, 7.6).
18. **fig-fingerprint (middle panel), an analytics caution.** Nearly every defense sits *above* zero
    (median about +0.7 pp), which is a selection artifact: games where the top receiver had no target are
    dropped. So "most defenses barely change it" isn't what the dots show. Either re-centre the panel on
    the league median ("NE is about 2 points below the typical defense") or keep zero-target games
    (share = 0) when the player was active. The NE-is-last conclusion survives either way.

## D. Checked and fine

- XXV K-Gun formation is legal (X and Y on the line, H and Z off). Two-down-linemen 2-4-5 matches
  Parcells's description, and the five-under/two-deep structure is right for the era.
- XXXVI: the run/pass key on Faulk's alignment, jamming to break Martz's timing, and blitzing over
  Faulk are faithfully stated from Belichick's own words. Vrabel's pressure leading to Law's pick-six is
  correct.
- LIII: the Rams' condensed 11-personnel set under center is right, as are the 15-second radio cutoff,
  Gurley 10–35, 3 of 13 on third down and the final Cover 0 with Gilmore on Cooks.
- XLIX: the clock and timeout logic on both sidelines is fair and well sourced. The stack (Kearse
  point, Lockette back) and Browner's jam/Butler's jump are correctly characterized. The formation is
  legal, and there is one animation with a 4-frame strip that tells the story in print, so the
  animation budget is fine.
- The chameleon chart, the Blount and BAL numbers, the 2008 and 2021 Buffalo wind games, the 2003 Denver
  safety, XLVI "let him score" and the 2015 eligibility-rule game are all accurately characterized.
- Predict 1 (break the alignment key with a draw or screen) and Predict 3 (attack a soft shell before
  the half when you've deferred) are sound football. Predict 2 is sound once the DE alignment in A5 is
  fixed.
- Labels are inside the windows. No field-edge clipping found.
