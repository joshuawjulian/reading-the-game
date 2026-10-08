# Coach / film review: 12-01 Walsh's 49ers and the West Coast Offense

Reviewer persona: veteran NFL offensive coach and film analyst. Read the full qmd and the current PDF
(`pdfs/12-01-walsh-49ers-west-coast.pdf`, built 06:59, newer than the qmd), rasterized at 80 and 150 dpi
and looked at every figure. The beginner and fact-check reviews already cover several layout and
consistency points; where I agree I mark it "(also beginner)" and add only the football reason.

Overall: the argument (pass as run, timing/YAC/placement as design goals, rehearsal, tree) is sound
and well told. Most of the problems are in the diagrams. The Catch figure in particular undercuts its
own text: there's no sideline, Solomon's out is short of the goal line, and Montana ends 13 yards from
out of bounds. Priority order below.

## A. Must fix (diagram says something wrong)

1. **fig-the-catch: Montana is not "out of room".** `Play(..., los=104.0)` uses the default
   `ball_y="middle"`, so the right sideline is at w ≈ +26.7. Montana's path ends at w = 13.4, about
   13 yards from the sideline, and no sideline is drawn (`lateral=(-11, 18)`). Both the text and the
   film say he threw from a few yards inside the right sideline.
   **Fix:** `ball_y="right"` (right hash, sideline at w ≈ +23.6). Extend the QB path to about
   (-8.0, 19.5), via (-4.6, 5.0), (-6.6, 11.0), (-7.6, 16.0). Move Jones/DTR/LBM's chase endpoints the
   same amount, and widen to `lateral=(-11, 25.5)` so the sideline and a strip of out-of-bounds show.
   Only then does "throw it where only Clark can get it, or out of bounds" read on the page.
   (The beginner also noted that no sideline is drawn.)
2. **fig-the-catch / fig-predict-sprint: Solomon's out is short of the goal line.** His route ends at
   d ≈ 2.8–3.6 (the Dallas 3), the "slip" label sits at the 3, and the SS "jumps the out" at d = 4.2.
   The text calls it "a short out toward the right corner of the end zone" and says he scored on it
   earlier. On a sprint-out from the 6 the slot's out breaks at the goal line or 1–2 yards deep.
   **Fix:** Solomon `via=[(5.6, 8.4)]`, end `(6.8, 11.0)`. Put the slip at about (5.6, 8.6), and SS
   `go_to(... (6.4, 11.2))`. Do the same in Predict 3 (`SOL` via (5.6, 8.4) to (6.8, 11.6), number
   "1" at about (7.8, 12.6), SS to (5.8, 10.6)).
3. **fig-the-catch: Clark's marker and the end line.** In panel 4, 87 and his ring touch the top edge,
   and the caption has to tell the reader that "the top edge is the end line". This play is *about*
   the end line. **Fix:** draw the end line explicitly (thick line at d = 16), set `window=(-10, 18)`
   so a strip beyond it shows, and keep Clark at d ≈ 15.0 so the ring sits clear of the edge.
4. **fig-same-job (left): the pulling guard never gets outside.** `go_to(p, "RG", (-0.6, 5.2), kind="pull", via=[(-1.8, 2.2)])`
   ends *behind the tight end*, on the line, so he leads nothing. A toss-sweep puller works around the
   TE's reach and leads up on the force (Sam or SS).
   **Fix:** `via=[(-1.6, 2.4), (-1.2, 6.8)]`, end about (2.4, 9.0) aimed at the SS's path. Label the
   four blockers (RT, Y, RG, Z) with small rings, or move "4 blockers must win" next to them (also beginner).
   The honest picture of the sweep is then: four blocks, plus the Mike flowing over the top unblocked,
   which is the point.
5. **fig-same-job (right): name the read, not "no one there".** The caption says the only nearby
   defender (the SS) "has dropped back under the tight end's curl", as though the flat is empty by
   design. Against a 4-3 Cover 3 sky, the SS *is* the strong curl/flat defender. The flat throw works
   because he's in a curl-flat bind: if he widens to the flat, the curl to Y is the throw. Say so in
   one clause and link [curl-flat](../../appendices/glossary.qmd#gl-curl-flat). That's the horizontal
   stretch the next paragraph introduces, shown in the picture you already have. Also, "run after the
   catch" (at w = 17.8) sits to the right of **Z's** go route, not H's. Move it to about (5.0, 9.0) or
   give it a leader to H's run arrow.
6. **fig-placement: A is not "away from both defenders".** The Will's path ends at (6.4, -6.4) and ball
   A is at (8.5, -7.0), about two yards from him on his side. B, "behind", is actually farther from
   W. The corner is also drawn *driving forward and inside* (6.0 to 7.6 deep), not "trailing behind
   and outside after bailing". **Fix:** start the CB at about (9.5, -15.5), already bailed, with his
   path to (8.6, -12.0) so he trails behind and outside. Stop the Will at about (5.2, -4.6), still
   inside but underneath. Then A at (8.6, -6.6) is truly in the void between and in front of them.
   Keep B behind X's back hip (6.4, -9.4) and C outside and upfield toward the CB (8.4, -11.0). Add
   a small arrow through the dashed ring for X's direction (also beginner), and `window=(-2.5, 14)`
   so X's ring isn't cut by the bottom edge.
7. **fig-slant-flat-strip: X and W overlap in panels 3–4.** X's slant ends at (7.6, -6.2) and the
   Will sinks to (5.8, -6.6), so the markers sit on top of each other. **Fix:** stop the Will at
   (5.4, -5.0), inside and under the slant window, and end X's slant at (7.8, -7.0). The point
   (W took the slant away) still reads, with no collision.

## B. Technique and timing (a coach would correct these)

8. **Slant break depth and release time.** The figures break X at 1.8 yards and release the ball at
   0.95–1.0 s on a three-step drop from **under center**. A 1980s under-center three-step (QB from about
   1 to 5 yards deep) gets the ball out at about **1.2–1.4 s**, and the classic Walsh/Rice slant is
   three hard steps (about 4 yards) and then the break, caught at 5–7. That's what 11-02's fig-walsh
   says ("breaks inside at 5 or 6 yards ... catching at about 7"), and what this chapter's own
   timing paragraph says ("routes that break at 5 or 6 yards").
   **Fix:** slant `[(0,0), (4.0,0), (8.6,-5.0)]`, `pass_to(..., t=1.3)`. Re-time the strip moments
   to about `[0, 1.3, 2.1, 3.2]`. Change Fig 1's label to "ball out in ~1.3 s". Keep the text's
   "routes that break at 5 or 6" consistent with the figure (or "caught at 5–7", as the beginner suggests).
9. **Split-back width.** The text says "one back behind each tackle", but `split_backs()` puts them at
   w = ±2.4, which is behind the guard-tackle gap with tackles at ±3.2. Walsh's split backs ("Red" in
   his numbering) sat behind the tackles at about 4.5–5 yards. **Fix:** w = ±3.2, d = -5.0, which also
   gives the flat routes a more realistic angle. If you keep ±2.4, change the text to "behind the
   guard-tackle gaps".
10. **Drive read order (also beginner).** 04-04 reads drive low to high (shallow, dig, back), and this
    chapter reverses it with no explanation. Either match 04-04, or keep high-to-low and give the
    coach's reason in one sentence: on a five-step drop with a hitch, the 12-yard dig is timed to the
    top of the drop, while the shallow keeps running across the field and is still available on the
    next hitch. That makes the Walsh version "dig on time, shallow late, back last". I'd keep the
    Walsh order and explain it. That's case-study nuance.
11. **fig-wco-drive spacing.** Y's shallow (3.2 deep) finishes at w = -14 and H's flat finishes at
    (1.6, -9.0). That puts two receivers in the Will's area 1.5 yards apart, and the shallow runs
    straight through X's stem. Real teams space the backside back away from the shallow's landing
    spot. **Fix:** either have H run a check-swing that stays at or behind the LOS (end around (-0.5,
    -8.0)), or, more Walsh, put H on a "check-angle"/option back under the Mike (end around (4.0, -2.0)).
    Then flatten Y's shallow to finish about (4.0, -11.0), inside X's go. Minor: the RCB's marker sits
    on Z's vertical stem. Start the RCB at (7.0, 14.5) with outside leverage.
12. **Slant-flat read, tie it to 11-02.** 11-02's fig-walsh shows the W *widening*, so the ball goes to
    the slant. This strip shows the W *sinking*, so the ball goes to the flat. That's the other half
    of the same read. Say it in one line ("11-02 showed the slant side of this read; here's the flat
    side, with the clock running"). That turns the repetition the beginner flagged into a payoff.
13. **The rub on The Catch isn't on the field (also beginner).** Clark's first leg (2.0, 11.4) is at the
    same width the SS reaches only much later, so no panel shows the crossing. As drawn, his first
    leg also points at Walls, his own defender. If the 49ers' alignment really had Clark outside
    Solomon, the mechanism is an inside release by Clark *across* Solomon's out-breaking path. **Fix:**
    Clark's first point at about (3.0, 9.2), crossing over the SS's starting spot (2.8, 7.4) at
    ~0.5 s, then the diagonal to (12.2, 4.4). Add a panel at about 0.6 s ("Clark crosses Solomon's
    man: the rub"). The strip can carry 5 panels (3 rows of 2 with one blank, or use ncols=3 for 6
    panels). Also shift panel 2's time so Clark is visibly mid-crossing when the note says he is.
    Clean up the H/F/L/T trail spaghetti near Q by dropping trails for the backs and DL (draw trails
    only for QB, 87, 88, 72, 24).
14. **The Catch's TE side is unsourced.** The code puts Y on the *left*. The text, the caption and the
    fact-check source the backs and both receivers, but not the tight end. Either verify on the NFL
    Films footage, or add "(tight end's side illustrative)" to the caption. The same goes for the
    Cowboys' front: Dallas in 1981 played Landry's **Flex** 4-3, with one or two linemen set off the
    ball. The caption already says the alignment is illustrative, but a Flex-shaped front (offset the
    weak DT and strong DE by about 1 yard) is a five-minute change that a film person would notice.
15. **Predict 2's front isn't the Giants'.** The setup says "The Giants of the mid-1980s did something
    like this", but the diagram is a 4-3. The 1985–86 Giants (Parcells, DC Belichick) were a **3-4**
    whose rushing outside linebacker (Lawrence Taylor) was the problem. Either draw a 3-4 (NT 0,
    DEs in 5, four LBs, with LT at the weak OLB rushing and the ILBs taking the backs), or cut the
    Giants sentence and call it "a physical man-coverage defense". Also give the unassigned Mike a job
    (also beginner). In Cover 1 he's a "rat"/hole defender or the fifth rusher. Ringing him "rat"
    makes the answer's crossing-route advice smarter, since crossers have to clear him.
16. **Predict 1's answer should pick a side.** The SS has walked down to the *strong* (TE) side, so
    the strong flat is now crowded (S and SS). The coaching answer is to throw **weak**, where the Will
    is the lone underneath defender over X and the halfback. That's exactly the slant-flat in
    fig-slant-flat-strip. Say it ("throw away from the rotation: slant-flat to the weak side"), which
    also gives the drill a transfer link back to Figure 2. The beginner's two wording fixes ("wrong
    side of the line", "no deep help") also stand.
17. **Predict 3 down-and-distance.** "Third-and-goal at the 6" is inconsistent with The Catch's
    third-and-3 (also beginner). Since this drill is "a different day", either make it genuinely
    goal-to-go (and then the orange line should vanish, which it already does with `to_go=None`) and
    say so, or match the third-and-3 frame. Also state timeouts in the setup.

## C. Missing nuance a coach would insist on

18. **Sam Wyche and Super Bowl XXIII.** Wyche was Walsh's quarterbacks coach (1979–82) and is in the
    tree figure, but the text never mentions him. He took the system to Cincinnati, added the no-huddle,
    and lost Super Bowl XXIII to Walsh, which makes it "two branches meeting for the title" seven years
    before XXXII. One sentence in the dynasty or tree section, and it explains why the figure has him.
    (Verify Wyche's 49ers years and the no-huddle attribution.)
19. **The backs' route tree.** The chapter says the backs were receivers but shows only flats and
    swings. Walsh's signature back routes were the **halfback option** (Craig vs a linebacker, break
    in or out based on leverage), the **angle/"Texas"** route and the check-release swing. Predict 2's
    answer mentions the angle. Give the option route one sentence in the Craig bullet or the SB XIX
    film room ("watch for the back stemming at the linebacker and breaking away from his leverage").
    That's the most WCO thing a back does, and it's what Craig's 92 catches were made of.
20. **Hot throws and sight adjustments.** "A defense that blitzed found a back already in its way"
    covers one rusher. A coach would add one line on what happens when the blitz outnumbers the
    protection: in Walsh's five-step game the QB had a **hot** read (usually the TE or the back to the
    blitz side, or a receiver converting to a quick slant). That's the honest counter to the zone-blitz
    paragraph later, and it links to the existing 07 chapters.
21. **Cover 2 vs the flat.** Design goal 2 says the flat catches the back "with the cornerback
    backpedaling away from him". That's Cover 3. Against Cover 2 (the corner squatting in the flat)
    the flat throw is the one being taken away, and the WCO answer was the hole shot or hi-lo behind
    the corner (curl, corner route). One clause keeps a reader from over-generalizing, and it sets up
    the Tampa 2 paragraph.
22. **The run game was real.** I agree with the beginner. "Couldn't run" was true of 1979. By 1984–89
    the 49ers were a balanced offense with Craig and Wendell Tyler, and their play-action from split
    backs (the bridge to Shanahan's boots) depended on that. Pull the run/pass split from PFR (team
    offense pages, 1981 and 1984) and give one sentence. Or soften the takeaway to "a team that
    *couldn't yet* run the ball".
23. **Harbaugh in "offensive branches only".** John Harbaugh was a special-teams coordinator (and
    one year as DB coach) on Reid's staff, not an offensive coach. Either change the caption to "the
    branches through Walsh's offensive assistants" or footnote that Harbaugh is a special-teams
    coach. The misconception box (Ravens = quarterback-run offense) then makes even more sense.
24. **McVay's solid line.** Agree with the beginner. McVay's formative staff years were in Washington
    (2010–13, under Mike Shanahan with Kyle as OC), not his one season (2008) on Gruden's Tampa staff.
    Make Mike Shanahan to McVay the solid (blue) edge and Gruden to McVay the dashed one. That also
    fixes the text/colour contradiction and puts O'Connell, Taylor and Coen in the Shanahan colour,
    which matches the prose.

## D. Smaller items

25. fig-fingerprint labels: "Pass, caught behind the line" should be "thrown behind the line"
    (air yards include incompletions). The body's "26% were caught at or behind the line" has the same
    problem. Change to "thrown to a receiver at or behind the line". Analyst nuance worth one clause:
    early-down passes and runs aren't randomly assigned (defenses in base vs nickel, 2nd-and-long), so
    the bars show association, not a controlled test.
26. fig-predict-box: "one deep safety" (d = 15.0) sits on the 15-yard line and about 1 yard from the
    top edge. Move it to (13.2, 4.6), beside the FS.
27. fig-predict-sprint: the "chased" label at d = -9.0 is 2 yards from the bottom edge, fine. But
    once the QB path is extended toward the sideline (item 1 applies here too), move it to about
    (-9.4, 16.0).
28. fig-same-job (left): the FB's backside cut block on the end is a legitimate 1980s split-back toss
    assignment. It's fine; leave it.
29. Code hygiene (no visible effect): `textwrap`, `Rectangle` and `from gridiron.play import draw_marker`
    are imported but unused, and `xe = p.players["X"]` (line 701) is unused. Drop them. This uses
    gridiron sensibly otherwise: `Play.to_tracking()` frames for the two strips, and hand-placed
    `Player`s where the helpers don't fit the 1980s look. Nothing needs to go into `gridiron/`.
30. Print layout (also beginner): page 9 is two-thirds blank before The Catch strip, and page 14 is
    three-quarters blank before the tree. Shortening the Catch strip notes to two lines, or letting
    the tree figure float (`fig-pos: "t"` / a slightly shorter `H`), should close both gaps.

## What's right (keep)

- The sweep-vs-flat comparison is the right teaching picture. The fix above only makes the sweep's
  blocking honest.
- Formation legality everywhere: seven on the line (X, five OL, Y), Z and the backs off the ball.
- 4-3 Over technique placement (5 / 3 / 1 / 5, Sam outside the TE, corners at 7) is a fair 1980s
  look, and Too Tall Jones (left end, over the offense's right tackle) and Walls (on Clark, offense's
  right) are on the correct sides.
- The check-release delay on the backs in drive, footwork as the progression clock, the 5-yard
  contact rule and the LeBeau/Tampa-2/terminology answers are all accurately characterized.
- The film-room picks (SB XIX for Craig as a receiver, SB XXIV for the system without Walsh) are well
  chosen and accurately described.
