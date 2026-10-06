# 06-04 Cover 2 and Tampa 2: coach / film-analyst review

Reviewed 2026-10-06 against `pdfs/06-04-cover-2-and-tampa-2.pdf` (built 18:08, matching the qmd),
rasterized at 80 and 110 dpi. I looked at every figure (Figs 1–11).

**Verdict:** strong chapter. The core football is right: deep halves, squat corners with outside
leverage funnelling #1 inside, corner force and safety alley in the run fit, smash as a high-low
on the corner, Tampa 2 Mike carrying the inside vertical, and 2-Man with inside-leverage trail
technique. The history is accurately framed (Carson, Lambert, Dungy, Kiffin, Lovie). It needs one
real correction (Palms), two arithmetic or caption fixes, a few small diagram fixes, and some
nuance that a coach would insist on (the corner's #2 key, hook defenders walling #2, 3x1
adjustments, and cloud/sky terminology).

## A. Errors to fix (must)

1. **Palms is described backwards** (line ~714, "trap the corner route with a corner who bails
   and a safety who drives on the hitch (Palms)"). In Palms / 2-Read, the safety reads #2. If #2
   goes vertical (smash's corner route has a vertical stem), the **safety takes #2**, so he plays
   the corner route. The **corner stays on #1 from an off, quarters-style alignment**, so he plays
   the hitch. If #2 goes quickly to the flat, the corner jumps #2 and the safety takes #1. A safety
   at 10–12 yards over the slot does not drive on the outside receiver's 6-yard hitch.
   Replacement: "...or play Palms (2-Read), where the corner plays off and stays on the outside
   receiver while the safety reads the slot and takes him when he goes vertical, so the corner
   route runs into the safety and the hitch runs into the corner."
   (A "trap" corner is a different idea: the corner sinks while reading #2, then traps an out by
   #2. Keep it out of this sentence.)
2. **Tampa 2 arithmetic** (Fig 6 caption, last sentence: "Five defenders underneath, three deep
   after the first second"). That makes eight droppers out of seven. Fix: "Five underneath at
   the snap; a second later, four underneath and three deep: that is the Tampa 2 bargain." The
   Why-it-exists box says the same thing more softly ("without giving up ... five defenders
   underneath"). Reword it to "keeps five underneath against the quick game, and gives one up
   only once the Mike has run past the short routes", which matches the body text at line ~786.
3. **Fig 6 caption timing:** the caption says "+3.0 s" but the panel and `TAMPA_T` say +3.3 s. Make
   the caption say +3.3 s.
4. **Fig 5 caption, Y's break depth:** the caption says Y "has broken toward the sideline at 8 or 9
   yards", but the route breaks at 10 (`r.path((10.0, 0.0), ...)`) and the text says "10 or 12".
   Change the caption to "at about 10 yards".
5. **Dungy "stayed in Pittsburgh as an assistant from 1981"** (line ~817). He was traded to the
   49ers for 1979 and coached at Minnesota in 1980, so "stayed" is wrong. Use "returned to
   Pittsburgh as an assistant in 1981 and stayed through 1988, the last five years as defensive
   coordinator."

## B. Diagram fixes

- **Fig 5 (smash strip), panel 1:** H (w = −9) sits outside `lateral=(-8.0, HALF)`, so a
  half-circle is clipped at the left edge with its label trimmed. Either widen to `lateral=(-11, HALF)`
  (and keep the right-side ruler) or drop H and X from this play. The caption already says the left
  side is not shown.
- **Fig 5, panel 2 (+0.9 s):** the football marker sits on top of Q, so the quarterback disappears.
  This is minor. Offset the ball slightly, or accept it.
- **Fig 5, panel 4:** the SS's dashed path runs flat across at 18.6 yards. A half safety breaking on
  a corner route drives downhill and outside, so make the path angle down, e.g. SS
  `path([(17.5, 17.6)])` instead of `(18.6, 17.4)`. Keep the "couple of steps away" picture.
- **Fig 6 (Tampa strip), panel 4:** the ringed M marker completely covers Y. Nudge the Mike's last
  point (`(19.0, 3.8)`) to `(19.5, 3.0)`, so he is on Y's inside hip and slightly deeper, which is
  also correct technique (top-down, inside leverage on the seam).
- **Fig 10 (Predict 2, trips):** Y's route line is drawn straight through the E box and the M box.
  Start the stem with a small outside release (`r.path((2.0, 0.6), (12.0, -3.5), (22.0, -4.0))`) so
  the line clears both boxes. Also, M (w = 2.0) and W (w = −3.0) are both at 4.5 deep and their
  boxes nearly touch. Move the Will to (5.0, −4.0).
- **Fig 7 (2-Man):** the leverage is right in the numbers (CB 1 yd inside X, $ 0.8 inside H). But at
  print size the corners look head-up, so the "inside shade" pointer points at something the
  reader can't see. Move the corners and the nickel to about 1.5 yd inside (LCB w = −13.5, RCB
  13.5, NB −7.6).
- **Fig 2, left panel:** the label "bail: turn and run with him, eyes on Q" mixes two techniques
  (man-turn and spot-drop eyes). For a spot-drop Cover 3 corner use "bail: open, run to his
  third, eyes on Q". For match use "...stay on top of #1".
- Everything else checks out: Figs 1, 3, 9 and 11 (alignments, depths, the hash at 3.1 yd and
  the numbers at about 13.7 yd from the middle, legal 2x2 and trips sets with 7 on the line, no
  clipped labels, no collisions). Fig 1 drops (safeties to 18.5/±12, corners to 8.5/±18.5,
  hook/curl to 10/±9, Mike to 10.5) are realistic. Two animations (spec asks for two), and both
  strips tell the story in print.

## C. Missing nuance a coach would insist on

1. **The corner's key is #2.** This is the single biggest coaching point missing from "The hard
   corner". Before the snap he looks at #1; at the snap his eyes go to #2. If #2 goes to the flat,
   he squats. If #2 goes vertical or there is no flat threat, he sinks (often to 10–12, "cloud
   sink") to squeeze the hole shot. Add one sentence to step 2 or 3. That sentence also sets up
   the smash fight-back bullet ("sink further"), which currently appears from nowhere.
2. **Hook/curl defenders wall #2.** In nearly every Cover 2 teaching the curl-hook defenders (Will,
   nickel/Sam) collide with or "wall" a #2 vertical and carry it to about 10–12 yards before
   passing it to the safety. That is how the defense softens the two-on-one on the half safety
   that the hole-shot section describes. Add it to the curl-hook bullet ("...and if the slot runs
   straight up the seam, he gets in his way and carries him until the safety takes over").
3. **Safety's read.** Add the half safety's read: he reads #2 to #1. He stays "as deep as the
   deepest and as wide as the widest", and his landmark is roughly the top of the numbers at
   18–20 yards by the time the quarterback hits his drop. This makes the "stays deeper than the
   deepest receiver" rule concrete.
4. **Terminology dialects.** In many systems the side where the corner takes the flat is called
   **"cloud"** (C = corner) and the side where the safety rolls down to the flat is **"sky"**
   (S = safety). The chapter already links cloud rotation from 06-03, so one sentence in the
   Madden box or in "The hard corner" ties the two chapters together. Also say that Dungy's and
   Kiffin's staffs called their base defense "Cover 2"; "Tampa 2" was the league's name for it
   (verify with the fact-checker before stating it as fact; otherwise write "coaches around the
   league called it..."). For 2-Man, note that the number is system-specific: "Cover 5" means
   2-Man in many books, but not all.
5. **3x1 / trips adjustments.** Predict 2's answer says that in plain Cover 2 "almost nobody"
   covers #3 up the middle. As a pure rule that is fair. A coach would add that this is exactly
   the formation where Cover 2 teams *check*. Against 3x1, the backside half safety has only X
   (and the backside corner is squatting on X), so many teams tell that safety to help on #3
   vertical, tell the Mike to wall #3 (a Tampa rule), or check out of Cover 2 entirely (into a
   trips check such as solo or special coverage, covered in 06-05 and 06-06). Add one or two
   sentences to the answer. Otherwise the reader comes away thinking the defense just accepts
   the hole.
6. **Tampa 2 Mike technique.** He doesn't just "run straight down the middle". He opens (usually
   toward the passing strength or #3), reads the quarterback's eyes and the inside vertical
   threat, and gets to the "pole" or "pipe" at about 15–20 yards. He matches a vertical from #2 or
   #3 with inside, top-down leverage and walls crossers on the way. One clause in the Tampa 2
   section ("reading the quarterback and widening to whichever inside receiver goes vertical")
   is enough.
7. **Name the concepts that beat Tampa 2:** **dagger** (seam clears the Mike, a dig behind it) and
   **levels / drive** sit in the hole the Mike vacates. The text describes the dig but never names
   these. Link them to 04-04 or 08-01 if they are defined there.
8. **2-Man vs the running QB: the defense's answer.** When the back stays in to block, the
   defender who has him either rushes ("hug" / "green dog") or spies. This is the standard
   counter to the scramble weakness and is worth one clause in the 2-Man risk bullet and in the
   Predict 3 answer.
9. **Telling Cover 2 from 2-Man after the snap.** "Still with the receiver at 12 yards" can be
   fooled by a cloud corner who sinks with no flat threat. Add a hips/eyes cue: a zone corner is
   square or facing the QB; a man corner has his hips turned and his eyes on the receiver.
10. **Modern Cover 2 isn't always squat-corner pre-snap.** Today's NFL Cover 2 is often disguised:
    the corners line up at 7–8 and only squat after the snap, or the defense plays **Cover 2
    invert** (corners bail to the halves, safeties drop to the flats). The squat corner is also
    the cloud side of Cover 6 and of cloud Cover 3. The Watch-for-it box line "Corners 7 or 8 off
    and ready to backpedal? Probably not Cover 2" needs a hedge ("...unless they squat at the
    snap; see 06-06").
11. **Data caveat:** the nflverse coverage labels don't separate Tampa 2 from Cover 2 (no
    "Mike runs the pole" flag), so the charts are Cover 2 family only. Add one clause, because
    readers will want to chart Tampa 2's decline.

## D. Film rooms

- **Steelers 1974–77:** well chosen and fairly characterised. Hedge slightly on "Twenty years
  before it had a name, that is Tampa 2": Carson's Steelers mixed Cover 2 with plenty of other
  coverage, and the Lambert drop was a feature, not every snap. Suggested wording: "the seed of
  what became Tampa 2."
- **Bucs 2002:** excellent, and the facts match the footnotes. "Watch Brooks: he plays the
  curl-hook zone on his side" is right (Will, weak hook/curl).
- **Colts/Bears 2006:** good. Two coach additions:
  - Name the coordinators: Ron Rivera (Bears DC 2004–06, who mixed in more pressure than a pure
    Tampa 2) and Ron Meeks (Colts DC).
  - The best "what to notice" from Super Bowl XLI is the **Colts' offense beating the Bears'
    Cover 2 by being patient**: checkdowns and runs into the two-high light box rather than shots
    over the top. Dominic Rhodes ran for about 113 yards and Joseph Addai caught about 10 passes
    (have the fact-checker verify both before using them). That illustrates "Cover 2 is a bet that
    you won't complete enough hard throws" better than anything else in the chapter.

## E. Small text points

- Line ~339, "Five underneath defenders is the most any common zone puts there": true for the
  standard zones. Fine as written.
- Line ~831: Sapp described as "undersized". He was about 6-2 and 300 lb, so "quick" or
  "penetrating" is safer than "undersized".
- Hole-shot arithmetic (line ~508): the safety starts moving at the snap (he opens and gains
  depth), so "reading for a few tenths of a second and then running" slightly overstates his
  delay. The conclusion still holds. Optionally say "while gaining depth".
- Takeaway 3, "more often than against any other coverage": in the FTN seasons Cover 2 is 29.4%
  against 28.0% for quarters, so "as often as or more often than" is safer.
