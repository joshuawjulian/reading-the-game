# 06-01 Coverage Fundamentals — coach / film-analyst review

Reviewed 2026-10-06 against `pdfs/06-01-coverage-fundamentals.pdf` (rasterized at 90 and 200 dpi,
every figure looked at) and the qmd source. Verdict: a strong chapter. The zone map, the deep-split
trade and the shell plates are what a DB coach would draw. Most fixes below are small. The ones that
need doing are #1 to #6.

Checked and correct (no action needed): NFL hash width (18'6", about 3.1 yd either side of the
middle). Numbers placement: the NFL rulebook puts the number bottoms 12 yd from the sideline, so
`NUM_W = 14.7` is right. Boundary is 23½ yd and field 30 with the ball on a hash. The illegal-contact
pocket condition, the 5-yard penalty and the automatic first down. Mel Blount rule 1978. Ty Law
emphasis 2004. The 2013 Seahawks' triple crown and the 43–8 score. Tampa 2002 yards allowed. Eagles
2024 at 278.4 yd/g. SB LIX won with four-man rushes. Cover 5 = 2-Man. Cover 6 = 4+2.

## Must fix (technical accuracy)

1. **Seattle "press, then bail" is the wrong label** (Film room title and body, l.1146–1162;
   misconception callout l.653). Carroll's step-kick is a **press-mirror technique, not a bail**. The
   corner stays square, takes a patient step, then "kicks" to stay on the receiver's hip and **runs
   with #1 vertically** inside his third. Rules-wise that is man on #1's vertical, inside a Cover 3
   shell. A bail is turning and running to a landmark *without* engaging. The chapter's own source on
   06-02 (Bucky Brooks, NFL.com 2015) says Seattle pressed a **single receiver** and bailed against
   **two-receiver** sides. Fix: retitle to "press Cover 3". Describe step-kick as jam-and-carry. Add
   the Brooks nuance: press to the 1-receiver side, bail or off to the 2-receiver side. Also drop "Watch
   the underneath defenders' heads… It's a zone". CURRICULUM 06-03 is literally "Seattle's **Match**
   Version", and Seattle's curl-flat players carried seams. Say "zone with match rules". Also, Byron
   Maxwell only became the starter late in 2013, replacing Brandon Browner. Say "Sherman and Brandon
   Browner, then Byron Maxwell", and name Kam Chancellor as the rolled-down safety. 06-02 l.715 has
   the same "bailed into deep thirds" wording. Tell the 06-02 owner.

2. **"One legal jam" is not the rule** (l.704–706 "one legal shot", Takeaways "limits press to one
   legal jam", Predict-3 answer "one legal jam"). Inside 5 yards, contact is legal and may be
   continuous: the corner can jam, re-jam and ride the receiver until he passes 5 yards. The real
   limit is a **5-yard window**, not a count. "Only one chuck" was the **1977** rule, the year before
   Blount. Reword all three to "all the contact has to happen in the first 5 yards". On the history
   (l.695), "Until 1978 a defender could hit a receiver anywhere" is too strong. The league trimmed
   contact in the mid-1970s, and 1977 allowed one chuck downfield before 1978 set the 5-yard limit.
   Send that to the fact-checker to verify and footnote.

3. **The option-route explanation breaks on Cover 3** (l.881–889). The text says MOFC means
   "break away" *because Cover 1 is man*, then ignores Cover 3. Cover 3 is also MOFC, and it is a
   zone, where the right answer is to sit in the window between the hook and curl-flat defenders. It
   also says MOFO means "deep defenders far away, so sit". But quarters safeties at 8–11 yd are the
   *closest* deep defenders and drive on #2's sit route, and 2-Man is MOFO with man underneath. Fix:
   say the primary rule is **man → break away, zone → sit**, as 04-01 already teaches. Then explain
   the shell version as a vertical-stem rule. The real system rule is "vs MOFC bend or stay away from
   the post safety; vs MOFO split the safeties or take the post". Also say that some systems use MOFC
   as shorthand because MOFC + tight leverage usually means man. 04-01 l.643–645 promised that "06-01
   explains why", so the explanation has to be right.

4. **Shell plates and Predict 2: the tight-end side has no apex defender.** In the Cover 2 and
   quarters plates of `fig-shells`, and in `fig-predict-quarters`, the SS is deep, so nobody is
   outside the box over Y. MIKE is at (4.5, 1.8–2.6) and WILL at (4.5, -2.2 to -2.6). Against 2x2 a
   real nickel defense always puts somebody in the apex to each slot. Otherwise Y's flat, quick out
   and bubble are free, and the "three/five underneath" counts in the text don't match the picture.
   Fix: `MIKE=(4.8, 5.6)` (apex between RT and Y) and `WILL=(4.5, -0.8)` (stacked over the ball) in
   both MOFO plates and in pr2. The nickel stays in the left apex.

5. **Bail is defined only as a disguise** (glossary l.15, text l.640). For coaches, *bail* is first
   a **technique**: turn the hips and run at the snap instead of backpedalling. It is used from 5–8 yd
   off alignments every week, and it is the default for Cover 3 corners against speed. "Press-bail"
   (or "fake press") is the disguise version. Fix the glossary: "A cornerback technique: at the snap,
   turn and run to a deep landmark instead of backpedalling. From a press look ('press-bail') it makes
   zone look like man." 06-06's term table (l.571) can stay as it is.

6. **Depth tells are overstated for the NFL** (Safety depth bullet l.929–934; Watch-for-it "12 to
   14 means halves, 8 to 11 suggests quarters"). The Fangio film room (l.1188) then says his
   quarters safeties are "deep", which contradicts the tell two pages later. Modern NFL two-high teams
   (Fangio, and everyone who copied him) deliberately play quarters, Cover 6 and Cover 2 from the same
   12–14 yd depth, so depth is a *college* tell that NFL defenses neutralize. Add one sentence: "In
   the NFL, many two-high teams align every safety at 12–14 so depth won't give it away; width and the
   corners' leverage and stance, and above all what happens at the snap, are the better tells." Soften
   the Watch-for-it numbers to "deep and wide leans halves; shallow and narrow leans quarters, but
   many NFL teams hide it".

## Should fix (nuance a coach would insist on)

7. **Press isn't only man: say so with Cover 2.** The corner-tells bullet (l.940) has Cover 2 corners
   "squat at about 5". The classic Cover 2 or Tampa 2 corner is often a **press/jam corner who reroutes
   #1 and sinks to the flat** (hard corner, "cloud"). It is the best counter-example to "press = man",
   better than Seattle. Add it to the misconception callout and to the Cover 2 tell.

8. **Quarters is match, not four spot-droppers.** The deep-quarter bullet (l.554–560) and
   `fig-deep-splits` present quarters as "four deep defenders each guarding a narrow lane". Add one
   sentence: in quarters the safeties read #2 (vertical: carry him; out or under: help on #1 or fit
   the run) and the corners take #1 deep unless he runs short. That makes it the purest match
   coverage. Predict-2's answer half-says this. Put it in the body so the section on three ways to
   guard a receiver can point to it.

9. **Tampa 2 isn't pure spot-drop.** In the film room (l.1173–1177), the Tampa Mike's run down the
   middle is a rule-based carry of #2 or #3 up the seam. That is a match rule inside a spot-drop
   coverage. Say "spot-drop at heart, with one key match rule (the Mike carries the inside seam)". The
   Bucs' corners also routinely jammed (Ronde Barber), which helps #7.

10. **"Strength" is used without definition** (glossary Cover 9; l.1041, l.1048, l.1051). Link the
    first use to formation strength (`02-02`, `#gl-formation-strength`), and add one gloss line on
    *passing strength* (the side with more receivers). Also state that ordinary Cover 6 puts the
    **quarters side to the strength or field and the half to the weak side or boundary**. Only then
    is Fangio's Cover 8 "mirror" meaningful.

11. **Press leverage in fig-press-off-bail contradicts the text.** The caption says press is "shaded
    to the inside". The leverage paragraph, the shell tells ("shading toward the side away from their
    help") and `fig-shells`/pr3 (corners at w=±15.7, outside X) all imply outside shade with a post
    safety. Either move the press CB to `(1.0, -15.6)` and change the caption to "outside shade, with
    his help in the middle", or keep inside and say why ("no inside help, e.g. Cover 0, or vs a
    slant team").

12. **Option-route section on 2-Man:** add 2-Man to the MOFO list of exceptions. It is two-high, but
    every underneath defender is in trail man, so "sit down" is wrong there too (ties to #3).

## Diagrams (looked at every one)

- **fig-zone-map (Fig 1):** good. The hook boxes (3.5–10.5 deep) sit shallower than coaches' hook
  landmarks (about 8–12 yd for a hook drop). Shift them to 5–12 and say "5 to 12" in the text and
  glossary ("5 to 10" reads like a short-zone drop). No clipping. The labels are clear.
- **fig-deep-splits (Fig 2):** correct counts and landmarks. A small polish: the white "3 deep" label
  sits on a gridline at x=1 to 2. Fine as it is.
- **fig-press-off-bail (Fig 3):** see #11. The bail panel's arrow runs straight upfield. A real bail
  opens the hips and the path bends slightly outside, toward the third's landmark at about
  `(12, -18)`. Optional. Labels are inside the window, with no collisions.
- **fig-three-ways (Fig 4, frame strip):** the story reads well in print, and the timings (snap /
  +1.2 / +2.4, throw at 1.3) are right. Problems:
  - The **QB leaves the window after the snap**. WIN starts at -7 and the dropback goes deeper, so
    the throw trail in the spot-drop row comes from off-panel and the ball runs off the bottom-right
    corner. Use `WIN = (-9.5, 20.5)`, or a 1- or 3-step drop so Q stays visible.
  - Spot-drop +2.4: X is caught about 3 yd from the $, and W is about 9 yd away. That doesn't read as
    "sits between $ and W", and a coach would say the $ should break on it. Either widen the window
    (dig at 12, throw arriving at about w=-8) or move the $ landmark to `(10.5, -14.5)`. Also, a dig
    doesn't "sit"; it settles or throttles in the window. Change "the dig sits down" to "settles" in
    the caption and the text (l.732, l.826).
  - Man row: fine (CB trailing X's hip, the paths cross). Consider ringing W in the man row and
    noting "W: rat / hole". Right now readers may think W is in zone during a man call.
- **fig-shells (Fig 5):** see #4 (apex over Y in both MOFO plates). The Cover 2 safeties at ±10 are
  outside the slots (±9). That is wide for the NFL, where the usual landmark is 1–3 yd outside the
  hash. ±7 to ±8 would still read "wider than quarters (±6.5)". The labels "13 deep, 10 out" are
  fine.
- **fig-dialects (Fig 6):** clear. Cover 6 and Cover 8 are mirror images, but no strength is marked,
  so the reader can't see what distinguishes them. Add a small "strength →" arrow, or a slot dot on
  one side, under the Cover 6 and 8 (and 9) panels.
- **fig-coverage-mix (Fig 7):** fine (data, not football). The caption's FTN-vs-NGS caveat is right.
- **Predict 1 (Fig 8):** correct Cover 3 picture (apex $ and SS, off corners with outside leverage).
- **Predict 2 (Fig 9):** see #4.
- **Predict 3 (Fig 10):** correct Cover 1 picture, and the line to gain is at 6. Fine.
- No label is clipped by the field edge and no labels collide anywhere. 1 animation (≤4).

## Film-room choices

All three examples are well chosen and match the spec (Seattle press Cover 3, Tampa 2 Bucs, Fangio
quarters). The fixes are characterization only (#1, #9). Fangio: "from the 2018 Bears" is fine.
"From his Bears years (2015–18)" is more accurate, since the two-high identity predates 2018 and goes
back to his 49ers years.

## Minor

- Hole zone vs rat: fine, and it matches the term index (rat zone → hole zone; robber → 06-02).
- l.1302 Predict 3: "linebackers likely have the back" is good. Add "the one without the back is the
  rat (hole) or a green-dog rusher".
- Cushion paragraph: one line on the corner's rule, "keep the cushion until the receiver eats it to
  about 3 yd, then break on his break", would make *cushion* operational.
