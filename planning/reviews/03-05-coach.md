# Coach / film review: 03-05 Perimeter Runs and Misdirection

Reviewed 2026-10-06 against the current `pdfs/03-05-perimeter-and-misdirection.pdf` (built after the last qmd edit),
rasterized at 100 dpi (`_pdfbuild/03-05-perimeter-and-misdirection/coach-*.png`); every figure and both frame strips
inspected. Chapter not edited.

**Overall:** strong chapter, pilot-level voice and structure. The ideas (race to the edge, crack/seal/replace,
series football, eye candy, constraint plays) are right and well sequenced. The fixes are mostly in the diagrams.
There are three real football errors: Drill 1's safety rotation, the crack-toss "seal" that is actually a reach, and
the buck sweep's force player. There are also some coaching-language slips. No label is clipped by the field edge.
Labels don't collide, except for the overloaded "W" (below).

## Must fix (football is wrong or self-contradictory)

1. **Drill 1 (fig-predict-1): the spin is backwards, and it contradicts 02-06.** The SS starts at (12, +8) on the
   right and ends at (6, -11.5): a ~20-yard diagonal trip during a jet motion. 02-06 defines spin as the safety on
   the side the motion is heading to coming down, with the other safety going to the middle (its figure uses
   `p.motion("FS", to=(8.0, -11.0))`). Fix: **FS** (left, ghost at (12, -8)) rotates down to about (7, -11). **SS**
   (right, ghost at (12, +8)) rotates to the deep middle, about (13, 0). Ring the FS. Change the drill text to "the
   free safety (FS, ringed) comes down hard ... and the strong safety rotates to the middle". In the Answer, "the
   side the strong safety just left" stays true. Keep both ghosts.

2. **Crack-toss (fig-crack-seal): the "seal" on a 9-technique is really a reach.** The chapter defines a seal as
   "pinning an inside defender inside" and says "the tight end steps down onto the end lined up over him". But the
   figure puts the end in a **9 (outside Y)**, and the prose says Y "gets his body on the end's outside shoulder".
   That is a reach on a wide-9, the hardest block a TE has. Fix (preferred): align DE_R as a **7-technique (inside
   shoulder of Y, w≈4.2)** or a 6 (head-up, w≈4.8). Y then genuinely seals him inside, and the Sam stays outside as
   the force. Rewrite the paragraph after the figure to match ("the end is lined up on the tight end, so Y only has
   to keep him inside"). If the 9 stays, call it a reach and drop the word "seal" for this block.

3. **Crack-toss: the RG's reach of the 3-technique with the RT gone.** The RG is asked to reach a 3 (outside
   shade) on a toss while his tackle pulls. That is near impossible, and a coach will circle it. Use pin-and-pull
   logic, as 03-03 teaches it: **RT blocks down on the 3 (pin)** and **RG pulls** to replace on the corner, which
   gives a slightly longer pull. Or keep RT pulling and move DT_R to a **2i/2 (w≈1.0–1.6)** so the RG's block is a
   realistic scoop. Update "the tackle, who has the shortest path ..." accordingly. (In NFL toss-crack both versions
   exist. Some teams pull both the tackle and the guard, the second puller taking the alley/SS.) Adding that one
   clause would also explain why the SS is "left over".

4. **Crack-toss: the runner's path goes straight through the puller.** R's path turns up at w≈10.2 to (12.5, 10.4),
   and the RT's block ends at (4.9, 10.6). In print the ball-carrier arrow and the replace block share one line.
   Decide the read and draw it: the RT **kicks out** the corner and R turns up **inside** him, at about w 9.0–9.3
   (between the crack at about 7.5 and the kick-out at 10.6). The caption already says "the back's lane is between the
   crack and the pulling tackle", so make the drawing match.

5. **Buck sweep (fig-buck-sweep): who forces?** The SS is rolled down at (8.5, 10.4), outside, at 8 yards (a
   cover-3 "sky" look). The CB at (6.5, 10.0) is directly in front of him at the same width, and the CB is the one
   who "comes up to force" and gets kicked out. With a rolled-down SS, the SS is the force and the corner bails to
   his deep third. Fix: either (a) keep the SS as the force: move him to about (6, 8.5), have the RG kick **him**
   out, and send the CB deep (8, 13). Or (b) make it cloud: the CB at (5, 10.5) forces, and the SS goes to about
   (13, 8) deep half. Then fix the caption. Either way, separate the two markers. They currently stack.

6. **The edge-dilemma figure has 9 offensive players.** `dilemma()` builds 5 OL + Q + R + Y + U and never calls
   `check_legal`, but the defense has two corners covering nobody. Add **X and Z off the line** (OFF_D, w≈±12.5,
   inside the ±13.5 window) so the corners have men. U and Y must remain the ends of the line. Call `check_legal`.

7. **The two "W"s.** In every Wing-T figure (buck sweep, waggle, Drill 2), offense **W = wingback** and defense
   **W = Will** appear side by side. Drill 2 rings "W" (the Will) next to the wingback "W". Relabel the wingback
   **WB** (the How-to-read paragraph and captions too), or the Will **Wi**. WB is better, because W is the Will
   everywhere else in the book.

8. **The cornerback's crack answer is described wrongly (two places).** The text after fig-crack-seal says "leaves the
   puller blocking air", and "Answer the crack" says "The puller then has nobody to block". Both are wrong. When the
   corner crack-replaces, the puller still has the corner. The difference is that the corner arrives tighter and
   sooner, outside-in, so the puller has to kick him out instead of logging him, and the back is forced to cut up
   inside into the pursuit. Rewrite: "...comes up to take the force job himself, so the puller meets him tighter and
   sooner than planned, can only kick him out, and the back has to cut inside, back toward the pursuit." Drill 3's
   answer already has it right ("ideally before the pulling tackle reaches him").

9. **The Watch-for-it line contradicts the backside rule.** The checklist says "Did the backside end squeeze down
   the line, or stay home?", which treats "squeeze" as chasing. But the reverse section (correctly) teaches squeeze
   as part of the right rule ("squeeze, stay behind the ball"). Fix: "Did the backside end **chase flat** down the
   line, or squeeze and stay home for the bootleg/reverse?"

## Should fix (nuance a coach would insist on)

10. **The backside rule's real name.** In the reverse section, add the term coaches use: the backside end's rule
    is **"BCR" (boot, counter, reverse)**, played with a **trail technique** at the depth of the ball. One sentence.
    It also ties the waggle (B), the counter (C) and the reverse (R) into one defensive responsibility, which is
    exactly the chapter's point. The bullet "Keep the backside honest" could reuse it.

11. **Waggle blocking is half the Delaware version.** In the Delaware waggle **both guards pull to the waggle
    side**: the near guard (LG here) kicks out the first defender outside the tackle, and the far guard (RG) pulls
    flat behind him as the QB's personal protector, turning up on the first threat to the edge (flat defender or
    corner). As drawn, the RG just reach-steps right. Fix: add the RG pull, ending about (-1.0, -7.0), and say in
    the caption "both guards pull to the boot side". This is also the series point: the guards go *opposite* the
    backfield flow, which is why linebackers who read the backs get beaten. Route structure (FB flat, Y deep cross,
    X clear) is correct.

12. **The waggle Y route is drawn through the Sam.** Y's release passes exactly over S at (4.3, 4.6). Start the
    release inside (via (2.0, 3.0), then (6.0, 0.0)), or move the Sam to about 5.6 outside Y.

13. **End-around/reverse: the QB lead duplicates the LT.** The LT "invites then blocks" the ringed end, ending at
    (0.0, -5.2), and the QB's lead ends at (0.0, -5.6), on the same man. Send the QB up the alley for the first
    pursuer to show (for example to (3.5, -6.5): the Will turning back or the FS), or give the end to the QB and
    have the LT hinge (cut off the 1/3 inside). Update the caption sentence.

14. **The belly series is missing.** The spec's objective lists "buck sweep, trap, **belly**, waggle". Add a short
    paragraph, or a fifth box in fig-buck-series, on the Wing-T's other base series. That is the **belly** (fullback
    off-tackle, with down blocks and a guard kick-out, a cousin of power), with belly keep/option off it. Note that
    Delaware ran the buck and belly series as mirror conversations. Or change the spec's word, but a coach will
    look for belly.

15. **A legal crack is aimed at the front side.** Add one coaching point in the Madden callout or the crack
    paragraph: the cracker aims at the target's **near number/armpit on the front side**. If he only sees the back
    of the defender's jersey, the block is a **block in the back** (or a clip, if low) and he should push off and
    find the next man. Beginners routinely think every crack is a cheap shot. This tells them what a legal one looks
    like on film.

16. **The jet-flip nuance.** In "What it gives up", add half a sentence: one reason offenses use the forward
    "pop"/shovel flip is that a botched exchange becomes an **incomplete pass, not a fumble**. That is the
    flip's answer to the fumble risk mentioned there.

17. **"The angle" bullet.** "By the time he has the ball, the runner is already level with the guard on the far
    side". At the mesh he is in front of the QB, roughly over the center (see panel 2 of the jet strip). Say
    "...within a stride or two he is past the far guard, already outside the box".

18. **Film room, Rams: "half the time".** "Half the time the ball goes the other way" reads as a statistic that
    has not been checked. Use "often".

19. **Film room, 49ers: "ran Raheem Mostert inside".** San Francisco's base run was **outside/wide zone**, not
    inside. Say "ran Mostert on the zone run the other way" (or "back away from the motion"). Mostert's 2019
    postseason damage was largely outside zone.

20. **Constraint section, the EPA analogy.** "0.17 ... roughly the gap between a good passing play and a bad run" is
    vague. A cleaner anchor: 0.17 EPA/play is about the gap between a top-five and a bottom-five offense over a
    season (13-02 has the scale). Optional, since this point is analytics rather than coaching.

## Diagrams: checks that passed

- **Legality:** crack-toss, Drill 3, jet formation, Wing-T and reverse sets all have 7 on the line, with only end
  men eligible (`check_legal` runs). The exception is the dilemma figure (item 6).
- **Alignments:** Wing-T spacing (wing 1 yard outside and 1 yard behind Y; H behind the tackle at 4.5; F behind the
  QB at 4.5), condensed Z at 8½, safeties at 11–13, and LBs at 4–4.5 are all realistic.
- **Buck-sweep assignments** are the textbook Delaware rules: W down on the end, Y down on the backer, RT down on
  the 3, RG kicks out, LG turns up, C blocks back, F fills the gap the RG left, LT hinges.
- **Jet strip (−1.0/0.4/1.2/2.4 s)** tells the story in print, with the Z/W/M rings visible. **Eye-candy strip
  (−0.9/0.5/1.0/2.2 s)**: the ghost Mike works very well. The inside-zone assignments (LT/LG combo on the 3 and LG
  to the Will, C on the 1 with the RG climbing to the Mike, the backside 5 left unblocked and widening for the jet)
  are correct. Two animations, under the cap.
- No label touches the field edge. The waggle "clear" label at 17.4 sits in a 20.5 window, and the jet-strip X sits
  2.7 yards inside the edge.

## gridiron notes (no edits made)

- The chapter re-implements `panel/strip/video` to support ghosts and rings. That is fine, but if `show_animation`
  gains `ghosts=`/`rings=`, these ~100 lines could go.
- `clean()` removes hash ticks and yard numbers by matching `linewidth == 0.5` / `alpha == 0.55`. That breaks
  silently if gridiron's styling changes. A `Field(numbers=False, hashes=False)` pass-through on `Play.draw` would
  be the robust fix (library request).
