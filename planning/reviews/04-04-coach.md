# 04-04 Dropback Concepts: coach / film-analyst review

Reviewer stance: veteran NFL offensive coach and film analyst. Scope: the football (assignments,
landmarks, technique, terminology), every diagram (I looked at all of pdfs/04-04-dropback-concepts.pdf
at 75 dpi and the strips and rub figure at 150 dpi), the two frame strips (I also pulled simulated
tracking frame by frame from `mesh_play()` and `verts_play()`), missing nuance, and the film rooms.

Overall: a strong chapter at pilot level. The four-family frame is the right spine. The 14 plates
share one style and read like a real playbook, the rub/pick section is clear and correct on the
NFL rule, the heatmap is honest about selection bias, and the film rooms are well chosen. The
problems: (1) the mesh frame strip does not show what its notes say; (2) the smash corner-route
conversion is stated backwards; (3) two plates (post-wheel, yankee) give the wrong mechanism for
how the concept beats the coverage drawn; (4) dagger and scissors leave out the real Quarters
mechanism; (5) a handful of drawing details. Fix the MUST items before publishing.

---

## MUST fix (wrong or misleading football)

### M1. fig-mesh-movie: the strong safety jumps ahead of Y, then teleports, and the notes describe a different play
Tracking from `mesh_play()` (d = depth, w = width):

| t | H | Y | SS (on Y) |
|---|---|---|---|
| 1.0 | (5.1, -7.2) | (4.4, +5.6) | **(3.0, +2.5)**: 3 yd *inside* Y, undercutting him |
| 1.2 | (6.0, -6.0) | (4.8, +4.2) | (3.1, +2.5) |
| 1.4 | (6.0, -4.5) | (4.9, +2.7) | **(2.5, +6.9)**: moves 4.4 yd in 0.2 s (22 yd/s) and ends up 4 yd *behind* Y |
| 1.9 (throw) | (6.1, -0.8) | (5.0, -1.1) | (4.0, +5.4): 6.5 yd behind |
| 2.8 (catch) | | (5.1, -7.8) | (4.2, -1.4): 6.4 yd behind |

- Panel 2 note says "H and Y cross at the mesh point" at +1.0 s, but they are 12.8 yd apart. They
  actually cross at about 1.75 s, at w ≈ -1.
- At 1.0 s the SS is in front of Y's path, and the reader sees that (panel 2). Cause:
  `detour=(0.75, 1.45, (3.2, 1.8))` pulls him toward a point Y has not reached yet. Then
  `lag_after=0.75` throws him 6 yd behind.
- "Ball out at 1.9 s: Y is a step and a half clear": at 1.9 s Y is exactly *at* the mesh point,
  and the SS is 6.5 yd away. The caption says "a two-yard lead".
- Fix: trail Y tightly until the mesh, then get caught on H. For example,
  `chase(p, "SS", "Y", lag=0.2, off=(-0.7, 0.7), detour=(1.55, 2.15, (6.6, 0.4)), lag_after=0.4)`,
  so he has to go over the top of H, who is a step deeper. Throw at **2.1 s** as Y clears
  (`pass_to("Y", t=2.1)`), and use strip times `[0, 1.2, 1.8, 2.1, catch]` or `[0, 1.8, 2.1, catch]`
  so one panel actually shows the mesh. Re-dump positions and check that the SS is within about
  1 yd of Y until about 1.7 s and about 2 yd behind at the throw.
- Use `ball_speed(24)` for the catch time, as the verts strip does. An 11-yd throw that flies
  0.9 s (catch at 2.8 s) looks slow; it should be about 0.5 s.
- The press corners trail X and Z by **3 yd** from 1.0 s on (LCB at 3.5 vs X at 6.8). Two pressed
  corners beaten by 3 yd make the corner routes the obvious throw and undercut the story. Use
  `lag=0.15, off=(-0.6, ±0.6)`.
- The Mike "rushes" but stops at d = +1.5 at 0.8 s and stands there for the rest of the play
  (`pts=[(-3.0, 0.4)]` from 4.5 deep). Either rush him into the center (`pts=[(-4.6, 0.2)]` plus a
  `p.block("C", ...)`), or make him the robber the Predict-2 answer talks about and say so in the
  note.
- The deep FS (at 13.5 to 15) is never in the window (`window=(-8, 13)`). Panel 1 says "one safety
  deep", and the caption says "before the deep safety can come down". Use `window=(-9, 17)`.
- The ball marker sits on top of the QB in panels 2 and 3 and hides "Q", the same bug as 04-03 M1.
  Offset the ball about 0.6 yd toward his throwing shoulder, or draw it under the QB disc.

### M2. Smash corner-route conversion is backwards (and contradicts the paragraph before it)
Text near line 783 says "against two deep safeties, flatten it and stay under the safety; against
one deep safety, push it deeper toward the pylon". The conversion paragraph near line 1659 says
the same thing ("flattens under a two-high safety and pushes deeper against one-high"). Two
sentences earlier the chapter says "Too flat and the cornerback can recover under it", which is the
Cover 2 case.
- Common teaching is the reverse. Against **two-high** (the corner squats), take the corner route
  **to depth**, over the corner and away from the half-field safety, landing near the sideline at
  about 15 to 20 yd. Against **one-high** (Cover 3, the corner bails into his deep third), a
  pylon-depth corner runs straight into him. So the route either **flattens** at about 12 to 14
  yd, under the bailing corner, or the hitch becomes the throw (and some teams convert the corner
  to a post or seam against MOFC).
- Rewrite both sentences so they match fig-smash and the "What smash gives up" paragraph.

### M3. fig-post-wheel: the mechanism contradicts the text and the coverage drawn
- The text (near line 1505) says "A Cover 3 cornerback is taught ... to hand the post over to the
  free safety". If he does that, he is free to stay on the wheel and there is no conflict. Against
  spot-drop Cover 3 the post runs straight at the middle-third FS, so the caption's "the post
  breaks open inside him, in front of the free safety" is not a real window.
- Pick one true story:
  - (a) **Match Cover 3** (the norm in the NFL today): the corner's rule is to carry #1 vertical,
    so he gets "posted" and squeezes inside with Z. The wheel then belongs to the curl-flat
    defender ($), who started at 5 yd and cannot carry it up the sideline. If you choose this,
    ring the **$** (or ring both and say "the pair"), draw the RCB's reaction as a dashed branch
    squeezing inside with the post, and make the wheel #1.
  - (b) Redraw it against **Quarters or Cover 1**, where post-wheel is a textbook beater. In
    Quarters, #2 going out tells the safety to help on #1's post, the corner is on #1, and the
    wheel is left to the apex/$.
- Either way, delete "hand the post over to the free safety" and fix the table row ("Defender in
  conflict: Cornerback" → "Curl-flat defender (and the corner)" for (a)).
- The "wheel" label (d = 10, w = 22.4) sits on the orange line to gain. Move it to about (13.5, 22.4).

### M4. fig-yankee: the deep over finishes in the left corner's deep third, and the FS is too shallow
- The over (Z) crosses the middle at (15.5, 2) and the FS drops only to (16.5, 0), so the route runs
  through the safety's spot. The caption says "deep over under the FS".
- The over then finishes at (19.5, -13), with its "2" at (21.4, -14.6), right on top of the LCB's
  bail landmark (17, -16.6). In Cover 3 the over is the *corner's* problem as much as the FS's.
- Fix: FS drops to about (20, -1) (he must respect the post). The over climbs to 18 to 20 and is
  thrown at about the far hash or bottom of the numbers (finish about w = -9). Draw the LCB
  squeezing X's post inside (a dashed reaction toward (18, -10)) or holding outside with his
  third. Name the real bind in the caption: the post holds the FS deep; the over is thrown in
  front of the deep-third corner and behind the run-faked linebackers. If you want the read to be
  "FS only", say MOFC/Cover 1 instead of Cover 3.

### M5. fig-dagger and fig-scissors: the real Quarters mechanism is missing
- **Dagger:** in Quarters, when #2 goes vertical the safety takes him, and the **corner is on #1**
  (man-everywhere, outside leverage). The dig works because (1) the safety, whose job would be to
  rob #1's in-cut, has been carried off by the seam, and (2) the corner has outside leverage on an
  inside-breaking route. The plate has the RCB bail straight to (17.5, 16) and ignore Z, which
  teaches nothing. Draw the RCB trailing Z from outside (a dashed branch from (7.5, 16) to about
  (15, 10)) and add a clause to the caption: "the corner, playing Z from outside, trails the dig".
  Without that, "Quarters beater" is not explained.
- **Scissors:** "the corner route is one-on-one against a nickel who can't run with it" is wrong
  for Quarters. When #2 goes vertical, the $ is not on him; the safety and the corner are each
  matched up. The real point, and the reason scissors beats Quarters, is that the crossing
  **inverts both defenders' leverage**. The inside-leveraged safety has to cross outside with the
  corner route, and the outside-leveraged corner has to cross inside with the post. Each loses
  leverage, and the crossing adds a rub at depth. Rewrite the caption and the paragraph near line
  1543 accordingly.

### M6. fig-angle: progression 2 is not a real condition
"(2) Y's seam, if the deep safety jumps the angle." A middle-of-the-field safety at 13 to 15 yd
never jumps a 5-yd angle. Use "(2) Y's seam (one-on-one against the SS) if the Mike stays inside
or a robber sits in the hole". Also, the back breaks while still **1.6 yd behind the LOS** and his
path back inside runs straight through the SDE/RT rush lane (drawn crossing the E marker). Have him
release wider, to about (-0.8, 7.5), and plant just past the LOS, about (0.8, 7.2), so the line
clears the end.

### M7. fig-conversion, MOFC panel: the route bends *toward* the safety
Caption: "bends slightly away from the safety". The route is drawn (8, 7.6) to (22, 6.6), which
moves inside toward the FS at w = 0. End it at about (22, 9.0).

---

## SHOULD fix (diagram realism, labels, timing)

### S1. fig-four-verts-movie
- The QB is invisible in panels 2 to 4: he sits at d = -8.0 and the window starts at -8, so the
  filter `x between los+window0+0.4` drops him. The whole lesson is the QB's eyes (the look-off), so
  use `window=(-10.5, 31)`.
- Panel 4 (+3.7 s): X and its CB, and Z and its CB, overlap and sit on the top edge of the window.
  The ball marker hides H at the catch. Raise the window top or end the routes about 2 yd earlier,
  and offset the ball.
- Corners bail at 7 yd/s and are **6.6 yd over the top** of X and Z at the throw (LCB 22.4 vs X 15.8).
  Real Cover 3 bail keeps about 2 to 3 yd of cushion: use speed about 5.5 and a landmark about 25.
- Panel 2 note: "the seams run past the curl-flat defenders" at +1.2 s, but H and Y are at 7.4 and
  the SS and $ at 9 to 9.5, so they have not passed yet (that happens at about 1.5 s). Use t = 1.6.
- Caption: "the curl-flat defenders run with the seams for a few steps". In the sim they just drop
  to 9 yd and stop. Either give the SS and $ a short carry (`path` to about (12, ±7.5) then stop)
  or reword the caption.
- The FS freezes at (18.5, 4.8) after 2.2 s and never breaks on the throw. Add a short break toward
  the catch point after the release (it still arrives late, which is the point).

### S2. fig-smash: corner-route break depth
The text says the corner breaks at 10 to 12; the plate (and Predict 1) breaks it at **8.5**. Use
`route_to(p, "Y", (10.5, 9.0), (17.0, 17.5))` (same for H in Predict 1 and the grey ghost).

### S3. fig-families, Triangle panel: the triangle doesn't surround the two defenders
D2 sits at (6.0, -2.5), 4 yd outside the shaded triangle. Move D2 to about (6.0, 1.5) (the hook
defender over the C route's end) so both D's sit inside or on the edges of the triangle, as the
caption says.

### S4. Dagger: protection text vs plate
The text says dagger is "usually called with six- or seven-man protection", but the plate shows
5-man protection with the back check-releasing. Either keep R in (and drop the "3") or say
"six-man protection, or five with the back checking before he releases".

### S5. Smash Predict 1 and the hook: the hitch is short of the sticks
It is third-and-8 in both the opening hook and Predict 1, and the hitch is at 5 yd. A coach would
say it out loud: on 3rd-and-8 the hitch needs 3 yards after the catch. That is why the QB wants the
corner route, and why many teams push the hitch to 6 or tag it to a "stop" at the sticks. Add one
sentence to Answer 1 ("If the corner sinks, the hitch is open, but it's short of the sticks; it
needs yards after the catch").

### S6. Heatmap caption and text: which concepts throw into the boxed cells
"where levels, drive, shallow cross, dagger and Y-cross throw": the shallow and the angle are
0-to-5-yd throws, and Y-cross finishes at the far numbers (charted left or right, not middle). Say
"where the digs of levels, drive, shallow cross and dagger are thrown".

### S7. Small label and position issues
- fig-curl-flat: the "3" (hook) at (6.4, 4.4) sits beside the M's drop arrow and reads as
  belonging to the Mike. Move it to about (4.3, 6.2), right of the hook's end.
- fig-mesh plate and Predict 2: "the Will (on) the back", but the W is at w = -2.6 and R at
  w = +1.5, so the man line crosses the formation. Put the W at about (4.5, 1.0).
- fig-predict-man caption: "the defenders pressing H and Y" (Answer 2). The SS is 4.5 yd off Y, not
  pressing. Say "the defenders on H and Y".
- fig-levels caption: "(3) the back ... releases to the flat". `swing()` draws a swing that ends
  3 yd behind the LOS. Call it a swing (the same in drive, dagger and the other plates using `swing`).

---

## Missing nuance a coach would insist on

1. **Landmarks.** Real playbooks teach landmarks, not just depths, and the reader can see them on a
   broadcast. Add one sentence in "How to read the plates": seams about 2 yd outside the hash
   (wider against one-high), go routes on or outside the top of the numbers (leave about 5 to 6 yd
   to the sideline for the back-shoulder throw), the smash corner and sail "to the sideline, about
   6 yd from it", the Y-cross "to the far numbers".
2. **Pressure answers.** Every dropback concept carries a built-in hot or sight adjustment. The
   drive shallow and the mesh crossers are natural hots; on smash or flood the back's check-release
   is the outlet. One sentence in the QB-clock section ("If the defense brings one more than the
   protection can block, the concept's quickest route is the hot") ties back to 04-02 and 04-03.
3. **Y-cross conversion.** The chapter lists conversions for levels, mesh and dagger but not for
   the most conversion-heavy route in the Air Raid. The crosser keeps running against Cover 3 and
   man (to the sideline) and sits in the window against two-high or a robber. Add it to the
   conversion paragraph.
4. **Field and boundary.** All plates are centered, and the "How to read" note says most concepts
   go to the wide side. Name the common ones once: flood and Y-cross toward the field; smash often
   to the boundary against Cover 2 (shorter throw for the corner route); post-wheel to the field.
5. **Post-snap rotation.** Predict 1 mentions it. A one-line reminder in the QB-clock section ("the
   pre-snap shell is a hypothesis; he confirms it with the first step of the safeties") ties to
   06-06 and would stop readers treating the pre-snap picture as final.
6. **Patriots option/choice (spec item).** The E-P paragraph is generic. Name the slot option
   routes of Wes Welker and Julian Edelman as the concrete example of receivers converting routes
   after the snap. These are well known, but give them a source (Brown's "Speak My Language" covers
   it).
7. **Terminology dialects (light touch).** You already give flood/sail, levels/"Dig" (Colts) and
   angle/Texas. Add one line that teams name the same concept differently and some reuse a name for
   a different concept, so readers don't over-trust any one name. Cite Brown. Avoid inventing
   specific dialect names without a source.

---

## Film room

- **Texas Tech 2007–08:** well chosen. The stats match what I know (Harrell 5,705 yd; Crabtree
  134-1,962-22; Biletnikoff 2007 and 2008). The Kingsbury line is fine. (FACTS: Kingsbury is the
  2026 Rams assistant HC, so you could add "now on McVay's staff", but it's optional.)
- **Rams 2018:** good, and the yankee citation (ESPN, Wagoner) supports it. Its "What to notice"
  section ("the deep over crossing behind them at 18 to 20 yards") is right.
- **Chiefs 2018:** the stats are fine, but the four-verticals link is asserted, not shown. Nothing
  cites the Chiefs running four verts or its variants specifically. Either find a source (a Brown or
  Ringer breakdown of a specific 2018 Chiefs verticals TD) or soften it to "vertical routes from
  Hill and Kelce made every deep defender declare early", which is what the EPA numbers support.

---

## gridiron use / notes for the library maintainer

- `strip()` and `frame_panel()` drop any player within 0.4 yd of the window edge. That is how the QB
  vanished from the verts strip. Worth a library-level warning, or always pad the window by 2 yd
  past the deepest QB position.
- The ball-over-QB occlusion bug recurs from 04-03. A small z-order or offset fix in the chapter's
  `frame_panel` (or later in gridiron) would solve it in both chapters.
- The default `BALL_SPEED` (18 yd/s) makes every catch_time look slow. 24 yd/s is right for firm
  intermediate throws.

## Legality and formation check

All plates pass. `spread()` has 5 OL + X + Z on the line (7) with H and Y off the ball. In
fig-yankee, 5 OL + U + Y are on the line, X and Z are off it, the ends are eligible and there is no
motion. Defensive alignments are realistic: Cover 2 squat corners at 5, Quarters safeties at 10,
Cover 3 corners at 7, press at 1.3.
