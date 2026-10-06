# 04-03 The Quick Game: coach / film-analyst review

Reviewer stance: veteran NFL offensive coach and film analyst. Scope: technical accuracy of the
football, the diagrams (I looked at every figure in pdfs/04-03-quick-game.pdf, rasterized at 75 and
130 dpi), the animation/frame-strip timing, missing nuance, and the film-room examples. I also pulled
simulated tracking for the two strips to check positions frame by frame.

Overall: strong chapter. The voice, the "one defender, two receivers" spine, the leverage section,
numbers/leverage/grass, the data charts and the film rooms are all at pilot level. The problems are
concentrated in (1) the five-man-pressure frame strip, (2) the double-slants leverage, (3) blitz
arithmetic in the text and Predict 2, and (4) a handful of route/label details. Fix the MUST items
before publishing.

---

## MUST fix (wrong or misleading football)

### M1. fig-pressure (frame strip): the press corner ends up in the offensive backfield, and X is still on the LOS at 1.0 s
Tracking pulled from `pressure_play()`:

| t | X depth | LCB depth |
|---|---|---|
| 0.5 s | -0.2 | +0.7 |
| 0.8 s | +0.2 | **-1.6** |
| 1.0 s | +0.5 | **-1.6** |
| 1.3 s | +2.2 | **-1.2** |
| 2.1 s (throw) | +6.3 | +3.4 |

- The CB sits 1.2 to 1.6 yards **behind the line of scrimmage** from 0.8 s to 1.3 s (panel 2 shows it
  plainly: "CB" box below the blue line). Cause: `trail(..., off=(-1.6, -1.2))` puts him 1.6 yd
  "down" from where X was 0.35 s earlier, and X is still at the LOS. Fix: clamp the chaser's depth to
  `max(chase_d, X_d - 0.6, LOS + 0.3)` while X is within 2 yd of the line (so the press corner is
  hip to hip at the line, then trails a step behind once X is past him), or use
  `off=(-0.8, -0.9)` and `t_on=1.3`.
- X at +0.5 yd one full second after the snap means the press won. Even against press, the release
  should be done by about 0.6 to 0.7 s (jab, swipe, through). Make the hand-fight segment faster
  (the `(1.0, -1.4)` segment at speed 2.6 → about 4.5) so X is ~2 yd deep at 1.0 s, breaks at ~5 yd
  around 1.6 to 1.8 s, and the 2.1 s throw is "on his break" as the note says. As drawn, at 2.1 s X is
  already 6.3 yd deep and 3 yd past the break.
- Panel 4 reads "+3.2 s". With `catch_time()` using 18 yd/s, a ~17-yard throw flies 1.1 s, which
  makes a quick-game catch look slow and is slower than a real NFL slant (roughly 22 to 26 yd/s on a
  firm throw). Use ~24 yd/s in `catch_time()` (also tightens the slant-flat strip: ball out ~1.15 s,
  caught 1.95 s, which is also a slow 0.8 s flight).
- The ball marker is drawn on top of the QB in panels 2 and 3, hiding "Q". Offset the ball 0.6 yd
  toward his throwing shoulder or draw it smaller with a higher zorder for the QB circle.

### M2. fig-pressure and "The arithmetic of a blitz": 5 blockers vs 5 rushers does not produce a free rusher
Text (around line 1279): "if it sends five receivers out, one rusher may come free". Five
blockers against five rushers is fully accounted for on paper. The caption repeats this
("five blockers face five rushers, and the blitzer ... is too far outside for the left tackle to
reach") and the picture shows the center with nobody over him. A coach would call this a protection
bust, not a designed hot.
- Fix the text: a free rusher comes from (a) **six** rushers against a five-man protection, or
  (b) five rushers when the protection is turned **away** from the blitz (it slides to the
  linebackers' side and the back releases), so the edge blitzer is the protection's "hot"
  player and the quarterback's responsibility.
- Fix the figure story to (b), which keeps the spec's "five-man pressure": say "the line slides
  right toward the Mike and the walked-down SS; the LT has the end, and the $ off the left edge is
  nobody's: he is *hot*." Animate it: C and RG/RT step right (`p.block("C", pts=[(-1.0, 1.2)])`
  etc.), LT kicks to the WDE. Now the free blitzer is legitimate and X's slant is the hot answer.
- Also add "or a fire zone behind it" to "the defenders who are left behind are usually playing man
  coverage": five-man pressures are very often 3-under/3-deep fire zones (07-03), where the hot throw
  goes to the area the blitzer vacated, which is exactly what the "Watch for it" bullet says.

### M3. fig-pairs, double slants: the defenders are drawn with INSIDE leverage, the caption says outside
`LCB` at w = -14.4 against X at -15.0 and `NB` at -8.4 against H at -9.0: on the offense's left that
is 0.6 yd **inside** each receiver. Caption: "start on the receivers' outside shoulders and have to
chase from behind". Inside-shade press is exactly the look you do NOT run double slants into (the
chapter's own rule). Fix: `LCB` w = -15.6, `NB` w = -9.6. Also the man defenders never move (no
reaction drawn, while the legend lists "defender's drop" and "defender's reaction"): add `trail()`
lines for CB and $ (behind and outside each receiver) so "chase from behind" is visible, and drop the
unused "drop" legend entry from that panel or the figure.

### M4. Predict the play 2 (Cover 0): rush count and leverage
- "If all of them come, the defense rushes as many as eight". With five eligible receivers out, a
  pure-man zero can rush six and still cover all five (seven if the back stays in and his man
  "hugs"/green-dogs). Eight rushers leave three defenders on five receivers. Rewrite: "Zero lets
  the defense bring six with a man on every receiver; if the back stays in, his man can come too, so
  seven against six blockers."
- Leverage contradiction: the chapter teaches "a defender lines up on the side where he has no
  help". In zero there is no inside help, so zero corners are coached to press with **inside**
  leverage and use the sideline. The figure has both CBs 0.8 yd outside (w = ±15.8 vs ±15) and the
  answer says "slant". Either (preferred) put the corners inside-shaded (w = ±14.3) and make the
  answer "throw away from leverage: the quick fade/back-shoulder or speed out outside, or the slot's
  hot route into the area the blitzing $ leaves, out in ~1.5 s", or keep outside shade and add one
  sentence explaining it is a disguised/"bluff" alignment.

### M5. Stick: role assignment contradicts the version readers already learned in 01-04
01-04 (the book's anchor play) is Trips Right Stick: Z go, **H (#2) arrow to the flat, Y (#3)
stick**. 04-03 says "#2 sticks, #3 (often the running back) runs to the flat" and draws the 2x2 +
back version, while saying "you met it in What a Play Really Is". Both versions are real (2x2 with
the back in the flat is the classic NFL Gruden/Reid drawing; Y-stick from trips with #2 on the
arrow is the Air Raid/BYU drawing), so keep the figure but say so: "Y is the stick runner wherever he
lines up; the flat comes from whoever is outside or under him: H's arrow in the trips version you saw
in Chapter 1, the back's flat here." Also note the flat landmark: get to the numbers or wider (the
back's flat in fig-stick ends at w ≈ 12.5, inside the numbers; push the last point to ~w = 15).

### M6. Drop/step counts from the shotgun conflict with 04-01
04-01 pairs **1-step gun = quick game (5-6 yd routes)** and 3-step gun = 10-14 yd routes. 04-03
says "a one- or three-step drop from the shotgun is timed to a receiver who breaks at about five or
six yards" and the speed-out caption says "throws on his third step from the shotgun", while the
code uses `dropback(1.5)` (one step). Fix: "from the shotgun, one step (some teams teach three quick,
short 'rhythm' steps that cover the same ground)" and in the speed-out caption "throws as his
one-step drop lands (from under center: on the third step)".

---

## SHOULD fix (diagram accuracy, clarity, conventions)

1. **fig-snag, "snag" label is on the wrong route.** It sits at (6.6, 9.4), beside Y's vertical
   stem where Y breaks to the corner, not beside Z's settle point (~(5.2, 11.5)). Readers will think
   Y runs the snag. Move it to about (3.0, 13.6) or point_to Z's endpoint. "corner (high)" floats 5
   yd above the route end; move to ~(14.0, 12.5). The legend says "window that opens" for what is the
   triangle; add a "the triangle" patch entry or relabel.
2. **fig-spacing: no flat threat.** Every receiver sits at 5.5 to 6 yd, so nobody is stretching
   the curl-flat defenders low. The classic spacing drawings (BYU/Air Raid, Gruden) keep receivers
   ~5 yd apart at 5-6 yd **plus an arrow/flat** from #3 or the back. Suggest: H or the RB runs an
   arrow to ~2 yd at the numbers on one side, and say in the text "spacing almost always includes one
   flat route underneath". Also X and Z are *outside* the curl-flat defenders, not "between two
   defenders" as the caption's last sentence says; reword ("between two defenders, or between the
   curl-flat defender and the sideline").
3. **fig-pairs, hitch-seam: one seam doesn't stress the middle safety.** With a single seam the FS
   can just lean on it. The text's "can't be in both seams at once" needs seams from both slots (or
   the QB holding the FS with his eyes). Either show a backside seam arrow from Y or change the text
   to "the quarterback holds the middle safety with his eyes, or runs seams from both slots so he
   can't take both". Also add the Cover 3 textbook: the seam-curl-flat defender is coached to carry
   #2 vertical, which is why the hitch is usually the answer.
4. **fig-release panel 4 (slant-and-go): the go runs straight through the corner.** CB drives to
   (4.2, -14.0) and X turns up from (4.3, -13.7): same spot. The CB should drive to a point in front of
   the slant (≈(4.6, -12.6)) and X should turn up behind/outside him (≈(4.4, -14.4) → (10.8, -15.0)),
   bending slightly to the sideline as a real sluggo does.
5. **fig-release panels 1-2 labels within 1 yd of the bottom edge.** "jab out" and "sell inside" at
   d = -1.6 with the window bottom at -2.5. Widen `WIN_R` to (-3.5, 11.5) or raise the labels to -1.0
   (convention: ≥1.5 yd inside).
6. **fig-leverage, left panel: the "taken" out is drawn as a diagonal to 6.2 yd deep and 4.5 yd
   outside**, which reads as a corner/flag. Draw it square: (-0.7,-15) → (5.0,-15) → (4.7,-20.0).
7. **fig-stick: H is cut by the left window edge** (H at w = -9.0, window -9.5). Widen to -11.5 or
   drop H from the plot. Also r.stick(7.5) puts the turn at ~6 yd past a 6-to-go line; fine, but say
   "settles at or just past the sticks" to match 01-04.
8. **fig-bubble and Predict 3: bubble to the tight end.** Y is the TE (spread() docstring) and is
   the bubble runner in fig-bubble and in Answer 3. Bubbles go to receivers; in 11-personnel trips the
   TE is usually #3 and blocks or runs a route, and the bubble goes to #2 (H) with #1 blocking the
   corner and #3 the overhang, or the offense uses a WR at #3. Either relabel Y as a slot receiver for
   these two figures or restructure: H bubble, Z on the CB, Y on the $.
9. **Predict 3 figure.** (a) The "3 receivers, 2 defenders" bracket spans w = 7.5 to 21.5 and leaves
   Y (w = 6.8) outside it; start it at ~5.8. (b) The SS "in the box" at w = 4.8 is two yards inside Y,
   so a bubble to Y (the innermost) is thrown into his lap. Move the SS to w ≈ 2.5 (stacked behind the
   DE/B gap) and/or widen the trips (Y 8.5, H 13, Z 19) so the answer's grass claim is true.
10. **fig-slant-flat strip**: note says "Caught about seven yards deep"; tracking has the catch at
    8.3 yd, 3.5 yd in front of the Will. Say "about eight yards deep". And with the faster flight
    (M1) the catch frame becomes ~+1.6 s, which reads properly "quick".
11. **fig-speed-out**: name the two danger looks a coach would insist on in the caption or text:
    the Cover 2 corner squatting in the flat and the Cover 3 curl-flat defender "sinking and
    widening" under the out (the $ here). That's where the pick-six comes from, more than from the
    corner on top. Also note the quarters logic that makes the drawing correct: with #2 vertical the
    safety takes #2 and the corner is left man on #1 backing up.

---

## Nuance a coach would add (short, high value)

- **Splits drive leverage.** The leverage section says "the sideline can't [help]". Coaches say the
  opposite: the sideline is the corner's 12th man. A receiver in a wide split near the boundary
  usually sees **inside** leverage; a reduced split gives him room for outside breaks and tips
  out-breaking routes. One sentence on splits (receiver's and the defender's reading of them) would
  correct this and help the leverage read.
- **Quick-game protection and batted balls.** Quick throws are low, from a shallow launch point, so
  linemen use firm/"jump" sets (and in many systems cut the defensive linemen) to keep hands down in
  the throwing lanes; the slant window is the B-gap lane. One sentence in "Job 1" or the press/blitz
  section.
- **Ineligible-downfield rule makes the bubble RPO-friendly.** A pass caught behind the line of
  scrimmage lets linemen block downfield on the run; a forward pass beyond the line with a lineman
  more than a yard downfield is a foul. That is why bubbles and now screens pair so well with runs.
  One sentence before the RPO link.
- **Rubs: the NFL line is one yard.** "Running a receiver into a defender on purpose ... is illegal"
  - add "more than a yard past the line of scrimmage before the pass" (NFL), which is why bunch rubs
  try to make contact at the line. Keep the deeper treatment in 04-04.
- **Double slants dialect.** Teams split on which slant goes under: many NFL playbooks have #2 run
  the deeper slant and #1 the flatter one underneath (or #2 widen first). One clause ("teams differ on
  which one goes underneath") avoids a reader with a playbook calling it wrong.
- **Stick dialects and the stick-nod.** Mention "Y-stick" (trips) vs 2x2 stick (see M5) and the
  stick-nod / stick-and-go double move as the counter defenses force, tying to the double-move
  section.
- **Speed out vs quick out naming.** In some systems the "speed out" is the 5-yard rounded cut;
  in others "speed out" is a deeper rounded out on a 5-step and the 5-yard one is the "quick out". A
  dialect note matches the course's terminology-across-systems promise.

---

## Text accuracy checks that passed (no change)

Rhythm-throw definition; 3-step under center to 5-6 yd breaks; one-look/one-defender post-snap read;
slant-flat read (widen → slant, sit/sink → flat) and the Cover 2 caveat; stick read of the flat
defender and the option rule vs man; snag landmarks and the Cover 3 vs Cover 2 read order; "Spot" as
an alias; now screen blocking rule (#2 takes the first threat inside-out, #1 beats the corner);
numbers/leverage/grass; backward-pass live-ball rule; five-yard chuck rule and the 1978 change; the
Walsh/Carter history; Welker's option routes and Brady's clock; Thomas winning inside on the slant;
Kelce stick/option at 5-8 yd vs two-high. Film-room choices are well chosen and accurately
characterized; the KC chart caption correctly notes 2022 was still near the median and the real drop
came in 2023-24.

## Animation / strips

Two animations (slant-flat, pressure): within the ≤4 budget. Slant-flat strip tells its story in
print; the pressure strip does not until M1/M2 are fixed (CB in the backfield, X still at the line at
+1.0 s, catch at +3.2 s, QB hidden by the ball).

## gridiron notes (do not edit gridiron/; fix in chapter code)

- `trail()` (chapter helper) needs a depth clamp so a trailing defender never goes behind the LOS.
- `catch_time()` uses 18 yd/s; use ~24 yd/s for quick throws.
- Frame panels draw the ball over the QB; offset or reorder zorder in `frame_panel()`.
