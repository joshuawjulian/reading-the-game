# Coach / film review: 08-01 What Beats What (Concepts Versus Coverages)

Reviewer role: NFL coach and film analyst. I checked the qmd as of 2026-10-07 22:59 and the PDF built at 23:00.
I rasterized all 26 pages at 80 and 150 dpi and cropped every frame-strip panel
(`_pdfbuild/08-01-concepts-versus-coverages/coach/`). I looked at all 13 figures. `coach/probe.py` re-runs
the four simulated plays and prints each catch time, catch spot and nearest defenders. The numbers quoted below
come from it.

**Overall:** this is a strong chapter. The core teaching is right: the four-step read (shell → rotation → key →
throw), the look-off and its cost, the "beaters are bets" argument, the two-way logic and the counter /
counter-counter table. The matrix is mostly sound. The EV arithmetic in tbl-ev and Predict 3 checks out against the
grades. The film-room picks (Corn Dog / Tom and Jerry, the 2025 Seahawks, Stafford) are well chosen and accurately
characterized. There are four animations, which is the cap, and every strip tells its story in print. Formations
are legal throughout: seven on the line, X and Z on the line, slots and the flexed Y off it.

I found **two teaching errors**: the smash-vs-Cover-3 key defender, and the dagger caption saying Y's curl "keeps
the SS busy". There are also **three diagrams that oversell or misdraw a defender** (the Palms SS, the Cover 2 SS,
and the mesh-vs-zone sit point), one football-wrong line in the data section, one dangling reference to a matrix
column that doesn't exist, and a handful of nuances a coach would insist on. Items are in priority order.

---

## A. Must fix (football is wrong or misleading)

### A1. fig-qb-read + the paragraph after it: against Cover 3 the smash key is the flat defender, not the corner
The strip and the text say "He let one defender, the corner, make the decision for him … smash's read (corner
sits, throw over him; corner bails, throw under him) still works against a Cover 3 corner, who bails." A Cover 3
corner bails **every time** by rule, so reading him tells the QB nothing. Once the middle closes, the defender who
decides smash is the **curl-flat player on that side**. Here that is the SS who skied down. If the SS carries or
sinks under Y's corner, the hitch is open. If he widens fast to the hitch, the hitch is dead, and the QB works the
corner route in the hole between him and the bailing corner (if that hole exists), or moves off the concept. Your own
probe shows this: at the catch (t = 2.38) the SS is **2.3 yards** from Z. The strip is really showing the SS
deciding the play.

Fixes:
- Panel 3 title: "+1.3 s · Key moves to the rolled-down SS: still inside. Throw the hitch". Point the eyes at
  the SS (`look=(9.5, 12.5)`), not at the corner.
- Caption, panel 3: "The corner bails, as every Cover 3 corner does, so the decision passes to the strong safety,
  now the curl-flat defender. He is still working out of the middle, so the hitch is open for a moment."
- Text paragraph: replace "He let one defender, the corner, make the decision for him" with "He let one defender
  make the decision for him: against Cover 2 that would have been the corner; once the coverage rotated to Cover 3
  it became the strong safety rolling down to the flat." Keep "smash survived the rotation", but say *why*: the
  hitch sits under a bailing corner and outside a flat defender who has to come from the middle.
- tbl-keys, Cover 3 row: add "(for smash or hitches: the flat defender; the corner always bails)".

### A2. fig-qb-read: the pre-snap shell says quarters, not Cover 2, and the hitch is short of the sticks
- The play uses `nickel("two")`, which puts the corners **7 off** with outside leverage. Two-high with 7-yard
  corners is the classic quarters picture. A QB reading it would hypothesize "quarters or Cover 2", not "Cover 2".
  Use `nickel("c2")` (corners 5 off, rolled up), which is what 06-04 and fig-smash-c2 draw. Or change the panel 1
  label to "Shell: two-high. Guess: Cover 2 or quarters" and the caption to match.
- `to_go=6`, and Z's hitch settles at 5.6 yards with the SS 2.3 yards away. On third-and-6 that is a tackle short of
  the line to gain, and every NFL staff teaches the hitch at sticks + 1 on third down. Either set `to_go=5`, or push
  the hitch: `timed(p, "Z", [(0.95, 7.4, 15.0), (1.3, 6.8, 14.6)], "route")` and `pass_to("Z", t=1.4)`.
- Alignment realism: nobody is within 7 yards of Y. The $ is over H, the Mike is at w = 1.8, and the SS is 13 deep.
  A two-high 4-2-5 against 2x2 puts an apex or hip player over the second slot. Move the Mike to a hip spot
  (`MIKE=(4.5, 4.4)`), or the uncovered slot becomes a free bubble a coach would circle. The same applies to
  fig-predict-call (B5).

### A3. fig-dagger-q: Y's curl frees the strong safety, not "keeps him busy"
The caption says "On the right, Y's curl and Z's go keep the strong safety and the Mike busy." By quarters rules
it is the reverse. When #2 (Y) goes **short**, the SS is released from #2 and looks inside for work. That means
poaching or robbing the deep crosser or dig coming from the other side, or doubling #1. The simulation draws exactly
that: the SS drives from w = 7.6 to 4.2 and finishes **5.9 yards** from the catch. That is a window a quarters
coach expects to close against a slower throw. This is the single most common way quarters kills dagger, so the
reader should hear it.

Fixes, pick one:
- **Better football:** give the backside a route that holds the SS. Y runs a seam or bender
  (`timed(p, "Y", [(1.2, 8.0, 9.0), (2.0, 14.0, 8.6), (3.2, 21.0, 7.6)], "route")`) and the SS carries him
  (`timed(p, "SS", [(0.8, 11.5, 7.8), (1.8, 15.0, 8.4), (3.2, 20.0, 8.2)], "drop")`). Caption: "On the right, Y's
  seam holds the strong safety, because a quarters safety must carry a vertical #2. Dagger is usually paired with a
  backside vertical for exactly this reason."
- **Minimal:** keep the drawing and rewrite the caption and text: "On the right, Y stops short, which by rule
  frees the strong safety to look inside. He drives toward the dig and arrives a beat late. A quicker backside
  safety, or a 'poach' call, takes this throw away; that is why many dagger calls pair it with a backside seam."
- Either way, add a row to tbl-counters: "Quarters poach / backside safety robs the dig | dagger, deep crossers |
  the backside #1 one-on-one; the backside seam | backside vertical to hold him; throw the backside iso". Also
  add a clause to "A defense that expects dagger can rob the dig with a safety who ignores the seam": "usually the
  backside safety, freed when his own #2 stays short".

### A4. Data section: "corners who give ground (Cover 2, Cover 3)" is wrong for Cover 2
The fig-route-cov caption ("hitches and curls succeed most against the zones whose corners give ground (Cover 2,
Cover 3)") and the text ("a hitch in front of a corner who is giving ground") contradict the chapter's own smash
section. A Cover 2 corner **squats**; he does not give ground. Hitches and curls do well against Cover 2 because
five underneath defenders dropping to landmarks leave **curl windows between them**, and Cover 2 corners sink when
#2 threatens deep. Suggested caption text: "hitches and curls succeed most against spot-drop zones (Cover 2,
Cover 3), where receivers can settle in windows between underneath defenders, and least against 2-Man, where a
trailing defender is on their hip with a safety behind him." Fix the prose line the same way.

### A5. fig-smash-palms: the SS is drawn under and inside the corner route, not "on top"
`q.path("SS", [(12.5, 9.0), (17.0, 15.5)])` ends 4.5 yards inside and a yard short of Y's corner-route endpoint
(18, 20). On the board, a throw to the corner route lands outside and over the safety, which reads as *open*. The
caption says the safety is "already on top of him". Redraw so he is over the top and inside:
`q.path("SS", [(13.0, 9.4), (19.5, 18.0)], absolute=True)`. Move the label to (22.0, 12.5) so it clears the
arrow.

Also reconcile this plate with the matrix. Per 06-05's own Palms definition, when #2 goes vertical Palms plays like
quarters (safety carries #2, corner man on #1), yet the matrix grades smash vs quarters "·". Add one sentence:
"Plain quarters handles smash in much the same way; Palms adds the trap, so if the offense answers with a quick out
by #2, the corner jumps it." Otherwise a careful reader asks why quarters is "even" but Palms "wins".

### A6. fig-smash-c2: the Cover 2 safety does nothing
`p.drop("SS", (18.0, 11.0))` is nearly straight back. A Cover 2 half-field safety reads #2 to #1: with #1 short and
#2 bending outside, he gains width toward the numbers. As drawn he finishes 9 yards inside the throw, which
oversells the window and teaches that the safety is irrelevant. Use `p.drop("SS", (17.5, 14.5))` and mirror it
with `p.drop("FS", (17.5, -14.5))`. The corner route still wins at (16.5, 18): the safety started on the hash and
is late, which is the true lesson. The text already says this ("starting near the hash, is a long way from the
sideline").

### A7. Seahawks film room cites "the matrix's quarters and Cover 6 columns", but there is no Cover 6 column
Either add a Cover 6 column to fig-matrix (see C2; it would also give split-field reading a home), or reword to
"the matrix's quarters column (and Cover 6, which plays quarters on one half)".

### A8. Matrix: quick game vs 2-Man ("−") contradicts the text
The 2-Man paragraph says its weaknesses are "short and outside, away from the trailing defenders". tbl-counters
lists "quick outs" as the counter to 2-Man. Yet the quick-game row grades 2-Man "−". Slants die against trail
technique, but outs, stops and slant-flat's flat route are exactly what trail defenders give up. Change the cell to
"·" (0). It affects no EV table.

---

## B. Diagram realism and label fixes

### B1. fig-mesh-two-way, bottom (Cover 3): Y's sit point is on the nickel
Y's zone route ends at (5.4, −8.4), and the green window is drawn there. That is exactly the $'s pre-snap marker
(5.0, −8.6). In print, the "open" crosser looks like it is thrown into the nickel. Static plates show pre-snap
spots, so either:
- draw the bottom panel with the chapter's own `snapshot()` at about t = 1.6 (defenders at their landmarks, ghosts
  for where they started), which tells the truth about the windows, or
- move Y's sit to (6.2, −6.8), between the Will's drop (7.5, −4.5) and the $'s drop (7.5, −12.0), and move the
  window ellipse there.

Top panel (Cover 1): the Mike has a solid rush arrow, but the caption never mentions it. Add "(the Mike blitzes: it
is Cover 1 with five rushers, so the back releases)". A reader otherwise sees an unexplained arrow.

### B2. fig-verts-match: labels name the wrong player, and the FS needs one line
- "$ runs to his curl spot" and "$ walls H and carries him" sit at (6, −19.6), beside the **CB**, and read as CB
  labels. Use `point_to(fld, q, (2.5, -19.5), (5.0, -8.6), "...")` with a leader to the $, or move the text to
  (3.0, −13.5).
- Caption: the left window only exists because the FS has *two* seams to split (the mirrored right side holds him).
  As drawn, he finishes 6 yards from the window, apparently idle. Add "the free safety, splitting two seams (the
  right side is the mirror), can't take both". Optionally `say` "FS: two seams, one man" near (21, −1).
- Diagram key: solid orange arrows (a defender carrying or matching a receiver; also the Palms SS and CB) are not
  in "Reading the diagrams". Add "solid orange: a defender carrying a receiver or rushing".

### B3. fig-flood-c3
- Panel 3: the "eyes" label sits on the $'s ghost, and in panels 3–4 the $ ring overlaps the RCB's ghost at
  (7.0, 15.8). Drop "RCB" from `ghosts` (the caption tells his story), or pass `look_off=(-1.6, -2.6)` for panel 3.
- Timing: the sail is thrown at 1.7 s while Y is still on his stem at about 11 yards. A sail off a 2.5-yard gun drop
  is a top-of-drop or hitch throw, about 2.0–2.3 s. Use `pass_to("Y", t=2.0)` with panel 3 at 2.0. The $ has
  already widened by then (he is at about w = 15 at 2.1), so the story holds.

### B4. fig-look-off
- Panel 4 (t = 3.0, the catch): the nickel is 2.4 yards and the robber 3.8 yards from H, and the SS ghost and $
  crowd the window. In print it looks like a contested ball, not "the space the robber left". Flatten H's in-cut and
  catch it earlier and wider: `timed(p, "H", [(1.45, 9.5, -9.2), (2.2, 10.6, -5.6), (2.95, 10.8, -3.2)], "route")`.
  Move the window to (10.8, −3.0). The robber is then about 5 yards away.
- Panels 2–4: the W box overlaps the Y marker and the RCB box overlaps Z. Trail the Will half a yard inside and
  under Y (e.g. WILL to (16.0, 9.6) at 3.0).
- Optional nuance: when the back stays in, the Mike's sit-and-rush is a "hug" or "green dog". Name it in the
  caption, since 07-02 uses the term.

### B5. fig-predict-call and fig-qb-read: the uncovered slot
Both use `nickel("two")` with nobody over Y (see A2). In Predict 3 specifically, a coach would note "uncovered
slot, give me the bubble" before running any EV table. Put the Mike at a hip spot: `MIKE=(4.5, 4.2)`.

### B6. fig-predict-tampa
At 1.1 s, X sits on the LCB's marker and Z on the RCB's (corners squatting at ±17 at 6.5 yd, receivers released
to ±15.6–16). Widen the squat spot to `(6.0, ±18.0)` so the markers separate. The football is right: Tampa Mike in
the pipe, safeties wide, curl players at 8.5.

### B7. fig-qb-read panel 4
The LCB box overlaps the X marker at the top left. Leave the LCB at (18.0, −16.8) at 2.9.

---

## C. Nuances a coach would insist on

1. **Split-field reading and Cover 6.** The prerequisite (06-06) teaches split-field coverage, the mirrored smash
   plate says "pick a side", and the film room cites Cover 6. Yet the chapter never says the QB must read **each
   half** against a split-field defense: smash to the Cover 2 side, dagger or a #2 out to the quarters side. Add two
   or three sentences after the smash plate, and ideally a Cover 6 column in the matrix (smash +1, dagger +1, four
   verticals −1, flood +1, mesh 0; grade it as a blend of the two halves).
2. **Field, boundary and hash.** Coverage calls and rotations are set by the field and boundary (Cover 6 rolls,
   which side gets the hard corner), and route landmarks change with the hash. One line in Step 1 ("note the hash:
   which side is the field, and which way the strength call goes") would cover it.
3. **Protection comes first.** Every NFL QB's pre-snap process starts with the protection (Mike ID, box count,
   who's hot) before coverage. Step 1 mentions protection in passing; make it the first clause of Step 1 and add
   "count the rushers" to Step 2's one-second question for Cover 0 and fire zones.
4. **Route depth vs. the sticks.** The chapter makes the point in "Beaters are bets" (4) but doesn't apply it in
   the drills. In Predict 3 (third-and-7), mesh's crossers settle at 5–6 yards against zone, short of the sticks.
   That is a real reason a coordinator wouldn't call it despite the safe floor. Add a sentence to Answer 3.
5. **Route conversions inside the concepts.** NFL smash and four verticals carry built-in conversions. The #2
   corner route converts (to a post or a sit) against middle-closed coverage, and the seams bend away from or split
   the safeties against two-high. This is why smash "survived the rotation" in real offenses. One sentence in the
   four-verticals paragraph, linking to route conversion (already glossed in the two-way section), would cover it.
6. **Tampa 2 answer (Predict 2).** Tie it to the look-off: the QB holds the Mike with his eyes on one seam and
   throws the other. Note too that the seam runners are often coached to bend away from the Mike.
7. **History line on quarters.** "Smash and the quick game against Cover 2 helped produce Palms and the quarters
   family" overreaches. Quarters spread mainly as a two-high coverage that still let both safeties fit the run
   against spread and option offenses (06-05 tells it that way). Restrict the claim: "Smash and the quick out by #2
   helped produce Palms, the quarters check that traps them."
8. **Smash vs Cover 1 wording.** "The free safety in the middle can help on the deep one": a middle safety can do
   little against a corner route breaking toward the sideline. What hurts smash against Cover 1 is the slot
   defender's outside leverage (the route breaks into him) and the corner sitting on the hitch with nothing to
   fear. Reword to say that, since it matches the "leverage" point two sentences later.

---

## D. Film room
All three are accurate and well chosen. Corn Dog and Tom and Jerry are a superb pairing of "beater" and "designed
for the counter". Small adds:
- Corn Dog: one clause that return motion only creates the edge against defenders who **travel** with motion. A
  defense that bumps, banjos or zones off the motion neutralizes it. That is the same man/zone tell the "what to
  notice" line teaches.
- Seahawks: fix the Cover 6 reference (A7). Otherwise fine and consistent with FACTS-current.
- Stafford: the "what to notice" is generic. That is acceptable, but if the fact-checker can verify one 2025 Rams
  play (a dig behind a read safety, or a look-off throw) with game and quarter, it would make the box land.

## E. Animations and gridiron use
There are four animations (qb-read, look-off, flood, dagger), at the cap, and the recaps (smash-C2, mesh) are static
plates as the spec asks. Strip times tell the story. The flood throw time (B3) and the look-off catch spot (B4) are
the only timing tweaks. Ball flight runs at gridiron's 18 yd/s, which is plausible. The chapter's helpers (`timed`,
`snapshot`, `strip`, `ghost_marker`) are sensible in-chapter implementations and touch nothing in gridiron/.
Gridiron gap worth noting for the library owner: `Play.draw` has no notion of "solid orange = carry/match", so
`q.path` defender arrows look like rush arrows. A `p.carry(def, rcv)` helper would make match coverages read
correctly book-wide.
