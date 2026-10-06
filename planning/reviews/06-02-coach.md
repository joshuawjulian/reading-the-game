# 06-02 Man Coverage — coach / film-analyst review

Reviewed the qmd and every figure in `pdfs/06-02-man-coverage.pdf` (rendered at 110 dpi), plus a
check of my own against the nflverse participation data (`_pdfbuild/06-02-man-coverage/coach/c0.py`).

**Verdict:** strong chapter. The structure is right: the free defender is the whole game, leverage
follows the help, the Cover 0 arithmetic, banjo, the bracket bill, and the shadow-versus-zone-corner
contrast. The voice and depth match the pilots. The numbers are honest about the 2022/2023 break.
Five things need fixing before it ships: one diagram bug (the Will never reaches the backfield), a
Cover 0 definition that is too absolute, an outside-leverage rule stated more firmly than coaches
teach it, a bracket corner aligned on the wrong side, and a few figure and caption contradictions.
Nothing here is a scheme error. These are mostly places where a coach would say "it depends", and
the chapter says "always".

## A. Technical accuracy: must fix

1. **Cover 0 is defined as "everyone else rushes". That is too strict.** The glossary says this,
   the section opener says it, and so do the Takeaways ("Cover 0 sends everyone"). Cover 0 means
   *no deep safety*. Many teams also play it with four or five rushers and a free "hole" or "lurk"
   defender low (0 Robber, 0 Hole, 0 Lurk), especially near the goal line. Your own footnote says
   only about 3 in 4 Cover 0 snaps had 5+ rushers. My check of charted Cover 0 inside the 5 found
   only 59% (2018–22) and 70% (2023–25) with 5+ rushers, a median of 5, and many with 4. **Fix:** in
   the glossary write "...and the defenders without a man usually rush (most often a six- or
   seven-man blitz), though some versions keep one free underneath." Add one sentence to the red
   zone paragraph: the goal-line Cover 0 label often means "nobody deep because there is no deep",
   not always an all-out blitz.

2. **"Help inside, so play outside leverage" is presented as a law.** It appears in the section
   heading, in "play away from your help", and in the Takeaways. It is the right *starting* rule,
   but a coach would insist on two qualifiers:
   - **Split rules.** A receiver with a wide split (near the sideline) usually gets *inside*
     leverage, because the sideline is the help. A reduced or tight split gets outside leverage.
   - **Down, distance and the slot.** On third-and-short many Cover 1 teams press with an inside
     shade (or head-up) to take away the slant, and accept the fade, which the free safety cannot
     reach anyway. Slot defenders in Cover 1 are often inside-leveraged against a two-way go.

   **Fix:** add 2–3 sentences after "play away from your help" covering split and situation. Then
   soften the Takeaway to "corners *usually* play outside...".

3. **The bracket corner is aligned outside, but the text says he takes the underneath/inside
   throws** (fig-bracket-3x1, fig-bracket-kinds "Under-over", fig-predict-bracket). In an
   under-over bracket the safety owns the deep ball, fade included. The corner's job is the slant
   and the dig, so he presses **head-up or with an inside shade** and plays inside-trail. As drawn
   (LCB at w=-15.7/-15.6 against X at -15) the dig breaks *away* from him, so "a dig runs into him"
   is false in the picture. **Fix:** in fig-bracket-3x1 and fig-predict-bracket move LCB to
   `(1.2, -14.4)`. In bracket_panel("under") move CB to `(1.2, -14.4)`, and re-centre the "under"
   oval at about `(7.5, -13.5)` so the dig at 9 yards visibly breaks into it. Update the Predict 3
   caption ("a step outside" → "head-up, a step inside") and its answer to match. Keep the in-out
   panel's outside alignment (that one is correct).

4. **Fig-rat-dig: the Will never rushes.** `p.rush("WILL", pts=[(-1.0,-0.6), (-3.6,-1.0)])` gives
   offsets from his start at d=4.5, so he stops at d≈0.9, still on the defense's side of the line.
   In every frame he sits on the line of scrimmage, while the caption says he "joins the rush".
   **Fix:** something like `pts=[(-3.5,-0.4), (-8.6,-0.8)]`, so he meets the stay-in back at about
   d=-4.4.

5. **Fig-free-player: "a safety who started deep, here as if two-high".** The FS is drawn alone in
   the middle at 14 yards, so the picture is single-high. **Fix:** draw the FS at `(13.0, -7.0)` and
   the SS at `(13.0, 7.5)`, both on the hashes, with a short dashed arrow showing the FS spinning to
   the middle (or say so in the caption). Alternatively, drop "as if two-high" from the caption.

6. **Fig-rat-dig caption: the robber "gave the quarterback nothing to see".** The SS sits at 9
   yards, near the middle, over nobody. Predict-the-play 1 teaches exactly that picture as the
   robber *tell*. **Fix:** "he started at 9 yards over the tight end, as if he had him in man".
   Better still, align him at `(9.0, 8.0)` over Y before the snap. Then the Mike takes Y, so update
   the tracks.

7. **Predict 2 caption contradicts itself.** It says "Every receiver has a defender within two
   yards of him", then that the FS is at 5 yards over R (R is 1.5 off the ball, so they are about 6
   yards apart). The SS is also about 4 yards from Y. **Fix:** "every receiver has a defender
   squared up on him, inside, within a few yards". Or move the FS to `(2.0, 5.6)` and the SS to
   `(1.8, 9.9)`, but then the "deepest defender at 5 yards" line has to change.

8. **The Cover 0 time-to-throw arithmetic is loose.** "2.1 to 2.25 s, about three tenths faster
   than any other coverage": in the NGS era 2.25 vs 2.4 is 0.15 s, and the chart shows 2.00 vs 2.40.
   Also, "a third of a second ... the difference between a dig and a slant" overstates it: a slant
   comes out around 1.0–1.3 s and a dig around 2.3–2.6 s. **Fix:** "about two to four tenths
   faster", and "the difference between throwing on the last step of the drop and taking one more
   hitch".

9. **Spagnuolo paragraph.** The Super Bowl XLII upset is remembered for the four-man "NASCAR"
   rush (Strahan, Tuck, Umenyiora, Kiwanuka/Robbins), not for Cover 0. Juxtaposed with Cover 0, the
   paragraph implies the wrong thing. **Fix:** "His 2007 Giants beat the 18–0 Patriots largely with
   a four-man rush; the Cover 0 reputation is from Kansas City". Also, "the coordinator most
   identified with the call" needs company. In the same data, **Wink Martindale's** defenses led
   the league in Cover 0 rate in 2019 (BAL) and in 2022 and 2023 (NYG), and **Brian Flores's
   Dolphins** led in 2020 and 2021. Spagnuolo was 1st only in 2025. Suggest: "Spagnuolo, Wink
   Martindale and Brian Flores have been the modern league's heaviest Cover 0 callers; Spagnuolo is
   the most famous for when he calls it."

10. **Sherman: "a zone corner in a zone defense" oversimplifies.** Carroll's Seattle was a
    single-high system that played a lot of **Cover 1 as well as Cover 3**. Sherman stayed on the
    left in both. The point that survives: Seattle didn't travel him. **Fix:** "Seattle's defense
    was built on single-high coverage, mostly Cover 3 with plenty of Cover 1, and Sherman stayed
    on the left side in both". Bonus: Kam Chancellor in Seattle's Cover 1 was the textbook
    robber/"rat" of that era, which could fit the robber section in one line (generalize it; no
    specific play).

11. **Red-zone rationale.** "Zones, meanwhile, get crowded and leaky" is debatable, because a
    compressed field helps zone droppers too. The stronger coaching reason: near the goal line
    there is no depth to bail into, routes are quick and break-driven, and zone droppers end up
    sitting on the end line with receivers working in front of them. Man contests the catch point
    instead. Rephrase.

12. **SB LVIII film room: "a play-action pass designed for Jauan Jennings".** Please verify the
    play-action part. My recollection is a straight dropback on the OT third-and-4, but I'm not
    certain. If it can't be confirmed, write "a pass designed for Jauan Jennings". The rest (six
    rushers, Cover 0, Jones free, Purdy's "They brought Zero") matches the cited sources.

## B. Missing nuance a coach would insist on (add briefly)

- **Rubs and the rules.** The man-beater table should note that a rub is legal only if the receiver
  doesn't *block* the defender more than 1 yard past the line before the pass. A deliberate pick
  downfield is offensive pass interference. Offenses design "rubs" so the contact is incidental.
  This is why bunch spacing matters. Link to 09-03.
- **Banjo variants and the "both go the same way" rule.** Besides in/out there is **low/high**
  (short/deep: the first to break short goes to one defender, the first vertical to the other).
  Teams also need a rule for when both receivers release the same way or both go vertical:
  usually revert to the pre-snap match, or outside takes #1. Also say *why* banjo defenders play
  off (about 5 yards, as the figure correctly draws): they need time to read the release. Against
  bunch, name the common **"point" call**: one defender presses the point receiver, the other two
  play first-in and first-out.
- **In-phase and out-of-phase.** The core man technique for the catch point: a defender "in phase"
  (on top, hip to hip) can turn his head and find the ball, and one out of phase plays the
  receiver's hands. It explains the chapter's "reacts to the receiver's hands" line, and it is the
  first thing a DB coach teaches after the release. One short paragraph in the techniques section.
- **The robber's key.** In most Cover 1 Robber teaching he reads a *receiver*, typically #2 or #3
  to the passing strength, "robbing the first in-breaker", while also feeling the QB's eyes. "Eyes
  on the QB only" undersells it. Add one clause.
- **Cover 0 alignment varieties.** Cover 0 DBs are often **off and inside** (5–7 yards, "zero
  off") rather than pressed, so they can break on the hot throw and tackle without being beaten
  vertically. Fig-cover0-empty shows the press version, which is fine; mention the other in one
  sentence.
- **TE brackets.** In today's NFL the most common bracket is often on a **tight end** (a
  linebacker or nickel under, a safety over), not only on a wide receiver. One sentence in
  Brackets.
- **Predict 3 alternative.** A leaning weak safety against a 3x1 backside X is also the
  split-field "Solo"/"Cone" family (the weak safety helps on X unless #3 goes vertical). One line
  in the answer: "the same look can be split-field, see 06-06".

## C. Diagram-by-diagram notes (beyond section A)

- **fig-cover1-2x2:** the football is correct (4 rush, 5 manned, FS deep, Mike rat). The outside
  shades are fine as the textbook picture. There are no clipped labels.
- **fig-techniques:** (1) Off-man panel: the CB's final drive goes *upfield and inside*, from
  (10.4,-14.2) to (11.6,-12.9). On a curl the corner drives **downhill** through the receiver's
  inside/upfield shoulder. End the branch at about `(11.0, -13.6)`, coming from above the curl
  point, with the last leg pointing toward the LOS. (2) Press panel: the "jam" label at w=-19.8 sits
  about 5 yards outside the action. Move it to about `(2.2, -12.4)` (just inside the CB). (3) In the
  trail panel the CB line almost overlays the route. Nudge the trail path 0.6 yd shallower so both
  read.
- **fig-free-player:** a composite with no man lines leaves Y and R visibly uncovered. If you keep
  it as one field, add the caption clause "each version changes who covers Y and the back". The
  better fix is three narrow panels (rat, robber, lurk), each with its own assignments. See A5 for
  the two-high fix.
- **fig-rat-dig (strip):** apart from A4 and A6, the Mike's trail in frames 2–4 shows a loop (up and
  back) caused by the chase() smoothing as Y releases flat. Start his chase with `t_start=0.3` or a
  shorter `t_on` so his path reads as a clean flat chase. Timing (0 / 1.0 / 2.15 / ~3.2 s) tells the
  story well, and the throw distance and flight time are realistic.
- **fig-cover0-empty:** the "inside shade: no help anywhere" label floats at 10 yards in empty grass.
  Move it to the LOS area by the left CB, about `(-3.8, -19.6)` as in Fig 1. R at w=6.2 is almost
  under the right E (5.8). Widen R to about 7.6 and Y to about 11.5 (same in Predict 2) so the end
  isn't head-up on a receiver.
- **fig-banjo (strip):** this is the right concept and it reads correctly in print. In "Locked man +0.6
  s" the CB, $, Z and H markers pile on top of each other. That is meant as traffic, but the labels
  are unreadable. Offset the RCB keyframe at 0.6 s to about `(3.0, 14.9)` and the NB to `(5.4,
  12.4)` so the boxes touch without overlapping.
- **fig-bracket-3x1:** apart from A3, it is correct. The arithmetic and the "empty hole" are right. The
  defense is essentially "Cover 1, X doubled". Many staffs would call it a bracket check or the cone
  family (see B).
- **fig-bracket-kinds:** apart from A3, the in-out panel's slant arrow ends short of the "SS: in" area.
  Extend the slant to about `(8.0, -9.5)` so it visibly "runs into him".
- **fig-shadow:** this is correct and legal (7 on the line in both snaps). It is a good choice to show
  the nickel sliding out.
- **fig-predict-robber:** this is correct. Optional: once H's motion makes it 3x1, a robber SS
  would usually cheat slightly toward trips. He is at w=2.6, which is fine.
- **Charts (fig-cover0-bargain, fig-man-situations):** they are clean and correctly caveated. The
  Cover 0 by field position panel would benefit from a caption note per A1 ("near the goal line
  'Cover 0' often means nobody deep, not necessarily six rushers").

## D. Film room

- The Patriots 2003 and 2019 examples are well chosen and accurately characterized. Gilmore
  (DPOY, 6 INT, 2 pick-sixes, first Patriot DPOY) and the 2019 points and yards numbers are
  correct. The "Just beat them up" quote is sourced.
- SB LVIII OT Cover 0: excellent choice, but see A12.
- Revis 2009 and Surtain 2024: good choices.
- **Suggested addition (the Cover 0 downside, which the chapter tells but never shows):** Jets vs.
  Raiders, Week 13 of 2020. With seconds left, Gregg Williams called an all-out Cover 0 blitz, and
  Henry Ruggs beat his man for the game-winning long touchdown. The Jets fired Williams the next
  day. That is the "one lost footrace is a touchdown" bargain in one snap, and a perfect
  counterweight to the LVIII box. Verify the details (Dec. 6, 2020, Raiders 31–28, Ruggs 46-yard
  TD with about 5 s left) before using it.
- The spec's "Patriots brackets" is covered only in prose. One sentence in the 2019 box about
  doubling the opponent's top receiver or tight end would close the loop. Keep it generalized
  unless sourced.

## E. Terminology dialects (what's there is good; small adds)

- Rat, robber and lurk: the hedged treatment is right. You could add "hole player" and "Cover 1
  Hole" as common synonyms for the rat, and note that some staffs reserve "lurk" for a *defensive
  lineman or safety* who drops into the hole off a pressure look.
- Banjo: in/out, "switch". Add low/high and "point" (see B).
- Man-free / Cover 1: fine. You could mention that "Cover 1 Robber" and "Cover 1 Rat" are the call
  names a reader will hear on broadcasts.
