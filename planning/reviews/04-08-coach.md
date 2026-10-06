# 04-08 Offensive Systems and Play-Calling Languages: coach / film-analyst review

Reviewer stance: veteran NFL offensive coach and film analyst. Scope: technical accuracy of the
football and of each family's terminology, every diagram (I rebuilt the chapter and looked at all
11 figures in pdfs/04-08-offensive-systems-and-languages.pdf at 80, 150 and 170 dpi), missing nuance, and the film-room
examples. The chapter has no animations or frame strips, which is correct for this spec (all four
spec diagrams are [S]).

Overall: a strong chapter that matches the pilots. The "what does a word stand for" spine, the
three-languages figure, the call-length chips, the Ghost-from-anywhere panels, the fingerprint
heatmap and the checklist card all work, and the trade-off table is right. The problems are concentrated in
(1) the run-and-shoot figure (QB drops onto the RB, and it leaves out the R&S launch point), (2) the
wheel tag running through the out and stacking on the go, (3) Predict 1's answer getting the motion's
direction backwards, and (4) the substitution rule being overstated twice. Fix the MUST items before
publishing.

---

## MUST fix (wrong or misleading football)

### M1. fig-run-and-shoot: the quarterback's drop lands on the running back, and the back has no job
- `rns_offense()` puts QB under center at d = -1.9 and RB at d = -6.5, both at w = 0. `p.dropback(4.5)`
  takes the QB to d = -6.4, **on top of the back**. In print this shows as the dotted Q-to-R line in both
  panels: the QB walks into R. R also has no assignment.
- It also misses what made the run-and-shoot look like the run-and-shoot. Davis and Jones's QB did not take a
  straight seven-step drop. He took a **sprint or half-roll launch** toward the call side, and the back's
  job was protection (often blocking the edge on the roll side) or a check release.
- Fix (minimum): give R a pass-pro assignment (`p.block("RB", pts=[(1.5, 2.6)])`, stepping up to the
  B-gap/edge on the call side) and either (a) offset R (w = -1.0, d = -6.0) and keep a 5-yard drop, or
  better (b) draw the QB's launch as a half-roll: `p.path("QB", [(-1.8, 0.8), (-4.0, 3.5)])` (about 6
  yards deep, just outside the guard). Add to the caption: "the quarterback half-rolls toward the
  call side; the back blocks."
- Nice-to-have (one clause in the text, no new figure): the base R&S plays were built around **motion**. On
  "Go", a slot motions to make trips and the QB rolls toward the motion. The text mentions motion only as a
  man/zone read. Say it is also how the R&S builds trips and sets the launch point.

### M2. fig-tags, left panel ("Ghost, Y Wheel"): the wheel runs through the out and stacks on the go
- Y's wheel (`r.path((1,3),(2.6,7),(6,8.8),(19,9.4))`) turns upfield at w ≈ 13.6 and climbs through 8
  yards, **exactly where and when H's out breaks** (H breaks at 8 yards from w = 10 toward 15.5). Then
  the wheel finishes at w ≈ 14.2, only 3 yards inside Z's go at w = 17. So the tag puts two vertical
  routes on one deep defender's shoulders, and the #2 out runs into the wheel. No staff would draw it this
  way. When #3 wheels, #1 usually converts (post, skinny post or dig) to clear the sideline, and the
  wheel climbs outside the numbers.
- Fix, either:
  (a) Keep "one route changes" but take a different route tag that doesn't collide: **"Ghost, H Out-and-up"**
  (the punishment for a defender jumping the 8-yard out; ties straight to the in-game-adjustment
  paragraph, which already uses "out-and-up"), or "Ghost, Z Comeback". Or
  (b) Keep the wheel and make the tag honest: Z's vertical becomes a post (`r.post(...)` from w = 17,
  break at ~12), Y's wheel widens (flat to w ≈ 17 at 2 to 3 yards, then up at w ≈ 18 to 19), and the
  caption says "a wheel tag also tells #1 to run a post and clear the sideline; good tags carry built-in
  adjustments like this." This is also a useful teaching point.
- Also fix the caption/text claim "Nothing else changes: the two receivers who aren't tagged run exactly
  what they ran" if you choose (b).

### M3. Predict 1 answer: the jet motion goes LEFT, but the answer says it stretches the defense to the right
- In the figure Z starts on the right (w = 9) and motions to (-2.8, 3.2), travelling right to left. The
  answer says: "The jet motion stretches the defense toward the right before the snap, and outside zone
  attacks the edge in that direction with the fullback leading." That's backwards. It's also confusing
  because the **fullback is offset left** while the **tight end and strength are right**.
- Fix: pick one story and make the picture match it. Recommended (the Shanahan-tree picture): wide zone
  **to the tight-end side (right)**, with the jet going left as a sweep threat that pulls the
  linebackers' eyes and keeps the backside honest, so the boot comes back left off the zone fake,
  toward where the jet went. Then offset F to the **right** (w = +1.4), so he can arc to the
  edge or insert on the playside linebacker. Rewrite the answer: "Z's jet motion (right to left)
  threatens a sweep left; the wide zone goes the other way, to the tight end, with F leading; the boot
  fakes that zone and the quarterback rolls back left, where the jet threat already pulled the
  linebackers' eyes." Alternatively keep F left and run the zone *with* the motion (left). Either way,
  state the direction.
- Also "outside zone ... with the fullback leading" is a little I-formation. In Shanahan wide zone, F's
  usual jobs are to arc to the playside edge or to cut the backside. "F arcs to the edge" is the
  more accurate verb.

### M4. The substitution rule is overstated (Tempo paragraph and Predict 2 answer)
- Text: the no-huddle "stops the defense from substituting, because the rules give the defense time to
  change players only when the offense does." Predict 2: "The defense can't substitute because the
  offense hasn't."
- What actually happens: the defense **may** substitute at any time. What it loses is the
  **protection**: when the offense subs, the umpire holds the snap so the defense can match. If the
  offense doesn't sub and snaps quickly, a defense that tries to sub risks being caught with 12 on the
  field, or mid-swap. Fix both places, e.g. "it makes substituting dangerous: the officials hold the snap
  for the defense to match only when the offense changes players; otherwise a defense that tries to
  swap risks being caught with twelve men on the field." Predict 2's question can then be "why is it risky
  for the defense to bring on an extra defensive back?"

---

## SHOULD fix (accuracy and nuance a coach would insist on)

### S1. Film room, Jet Chip Wasp: route and call characterization
- "ran a deep route that began like a crosser toward the middle and broke back toward the sideline".
  Hill's Wasp is usually described as a **deep post-corner**: a post stem off a long Mahomes drop
  (about 15+ yards deep, which is why the ball travelled ~57 yards for a 44-yard gain). "Crosser"
  suggests a shallow horizontal route. Suggest "began like a deep post, then bent back toward the sideline" (fact-check
  against the CBS/Wikipedia sources).
- fig-call-length marks "Chip" as "meaning not public". "Chip" is close to universal: it tells
  the back (or a tight end) to chip the edge rusher before releasing. That was the point on a
  long-developing deep shot. "Jet" is a common protection word too. Either colour "Chip" as protection with
  a hedge in the caption ("'Chip' in nearly every system tells a back to chip-block before releasing"),
  or add that sentence to the film room. Leaving it grey undersells how readable these calls are.

### S2. The opening paragraph uses a no-huddle New England as the one-word archetype, and the chart says the opposite
- The intro has "the New England quarterback walks to the line without a huddle ... a single word". The
  fingerprint chart shows the 2025 Patriots no-huddle on 1% of neutral snaps (31st), and the text
  says McDaniels's Patriots "didn't need the no-huddle". Make the intro "Tom Brady's New England
  quarterback ..." (an era picture), or switch the archetype to Washington.

### S3. "The language belongs to the head coach, usually": add the defensive-head-coach case
- That's true when the head coach is an offensive coach (Shanahan, McVay, Reid, Sirianni). When the head
  coach is a defensive coach, the language usually comes with the coordinator. Then a new OC either
  brings a new language (the whole offense relearns it), or the team hires inside the same tree so
  the words survive. Detroit's run of OCs, used as the churn example, is exactly this case: a non-play-caller
  head coach for most of the run, with continuity kept by promoting from within the tree (fact-check the specifics).
  One or two sentences.

### S4. Kill calls / check-with-me are missing from "in-game adjustment"
- The single most important at-the-line adjustment mechanism in modern languages is the **two-play
  call** (kill or "can" call) and the check-with-me. Erhardt-Perkins and Manning/Brady offenses are built on them,
  and even the Shanahan sentence has "an optional second play" slot (the chapter's own footnote [^order]
  says so). Add one sentence in "In-game adjustment" or the hybrid section, linking the terms' owner,
  01-05 ([kill call], [check-with-me]). Something like: "Every modern language also lets the
  quarterback change the play at the line: a kill call puts two plays in one call and he picks one
  after seeing the defense."

### S5. West Coast verbiage: the spec asks for a Walsh/Holmgren-era example; the WCO row oversimplifies
- The spec's examples include "Walsh/Holmgren WCO verbiage". The only real WCO call in the section is
  Brown's "Scatter-Two Bunch-Right-Zip-Fire 2 Jet Texas Right-F Flat X-Q", and it isn't attributed to
  that lineage. Add a famous Walsh-tree call, e.g. Jon Gruden's **"Spider 2 Y Banana"** (a Walsh-era
  49ers play Gruden made famous), and decode it: formation/protection ("Spider 2"), then the tagged
  receiver and route ("Y Banana"). Have fact-check source it.
- Real WCO calls usually name a **base pattern word plus receiver tags** ("2 Jet Texas, F Flat, X Q"),
  not every route from scratch. The text half-says this ("a word for the pattern plus a route word for most
  receivers"), but fig-three-names' WEST COAST row ("Z Go, H Out, Y Flat, X Dig") has no pattern word,
  and the WCO protection would usually be a number plus a word ("2 Jet"/"Jet") rather than "60".
  Optional: change the row to "Trips Right 2 Jet, Z Go, H Out, Y Flat, X Dig" and say in the caption
  that WCO protections are named this way. At minimum, add a caption clause: "real WCO calls often add a
  pattern word; the receiver-by-receiver part is what marks the family".

### S6. Coryell: add the rule that makes three digits work, and a modern carrier
- Without the **"evens break in, odds break out"** convention of the numbered tree, the reader can't see
  why one digit per receiver is enough. Add one clause in the Coryell section; it also explains
  why the language "travels well".
- "Today pure Coryell calls are rare in the NFL." That's true, but a coach would name the
  long-running modern carrier: Dallas's Turner/Garrett-lineage numbering lasted into the 2020s and
  went with its coaches (fact-check before adding). Mike Martz's 1999–2001 Rams "Greatest Show on Turf"
  is the vivid NFL showcase; one clause would help.
- The table's Coryell tempo "quick" is generous. Coryell teams huddled and the call carries formation,
  protection, digits and tags. "Moderate: short to say, but usually huddled" is fairer.

### S7. Air Raid "wide splits": say which splits
- In the fingerprints and the Watch-for-it list, "wide splits" reads as receiver splits. The signature
  Leach tell is **wide offensive-line splits** (3 to 4 feet or more between linemen), along with wide
  receiver splits. Write "wide splits, both the receivers and the offensive linemen", and add "huge
  line splits" to the Air Raid film tells.

### S8. Boot Ghost panel: the boot is missing its backside crosser and its edge threat
- 04-05 defines the classic boot as a three-depth flood **plus a backside over route at 15+ yards**.
  The panel's window (lateral -10) cuts X out entirely, so the boot shows no crosser, and the
  unblocked backside (right-side) end, the one man the boot must account for, isn't shown either.
  Fix: widen to `lateral=(-17, 21)` and draw X's dig as the over route (cross at ~14 to 16 yards to
  w ≈ 8). Optional: a ghosted "E" on the right edge with a "naked: the end must chase the fake" label. Or
  keep it as it is but say in the caption "X's backside route and the edge are left out; see 04-05 for the full boot".
- Y's boot-side flat at 1.5 yards is shallow for a boot. Boot flats usually settle at 3 to 5 yards near the
  sideline, so they can be thrown on the run. Use `r.flat(3.5, 10.0)` on the boot side.

### S9. fig-ghost-anywhere, bunch panel: #1's vertical should release outside
- From the bunch, Z (#1, w = 9.6) runs a straight go at w = 9.6, so #2's out (8 yards, to w = 15.6) and
  #3's flat (to w = 12.6) both finish **outside** the vertical, and H's out crosses Z's stem. In a
  real bunch flood the outside man releases outside and stems to the numbers (w ≈ 13 to 14) to carry
  the corner, the point man's out goes under him, and #3 flattens underneath. Fix: give #1 in the
  bunch panel a bending vertical, `r.path((3.0, 1.5), (8.0, 3.5), (21.5 - o.d, 4.0))`. The
  caption's "the routes cross" then reads as the bunch's deliberate traffic rather than an accident.

### S10. Checklist line 10: "did someone pull (gap)" excludes duo/iso
- Gap schemes don't always pull: duo and iso are gap/man runs with double teams and no puller. Make it
  "did the line step together (zone), or block down with double teams and maybe a puller (gap)?"

---

## NICE to have

- **Weekly install figure:** add a small "Mon: corrections · Tue: staff builds plan (players off)" stub
  above Wednesday. Mention the **opening script** (Walsh's first 15) as the weekly package's first page,
  with a link to 08-03 (owner of "opening script"). It's a West Coast institution and belongs in a systems
  chapter even as one line.
- **Runs and protections have dialects too.** One sentence: run calls are the least dialect-heavy part (the
  hole-numbering "26 Power" from 01-04, or scheme words like "wide zone"), while protections vary
  sharply (number series like "60/70", WCO "2 Jet", word-based slides). That way readers don't assume
  only the passing game has languages.
- **Erhardt-Perkins lineage detail:** Ray Perkins was the Giants' head coach (1979–1982) before
  Parcells, so the language reached New York with Perkins/Erhardt, and Parcells kept it. One clause;
  fact-check.
- **Ghost vs 04-04's flood:** Ghost's #2 is an 8-yard out, while 04-04 draws flood's #2 as a ~13-yard sail. Add a clause
  ("Ghost is the Erhardt-Perkins word for a flood with a shallower, 8-yard out") so readers don't think
  one of the chapters is wrong.
- **Predict 3 caption:** "the tight end Y flexed a few yards off the line" mixes up width and depth. Write
  "flexed out a few yards from the tackle, a step off the line of scrimmage".
- **Watch-for-it "Condensed?":** give a concrete threshold, e.g. "outside receiver aligned inside the
  painted numbers".
- **Shanahan/WCO call order** "the same one the West Coast family has always used" is a bit absolute;
  "the same order most West Coast staffs use" is safer.
- **Fingerprint text:** "skipped the huddle on under 6%". The Rams' cell prints "6%". Check that the
  unrounded value is < 6%, or write "about 6% or less". "The 49ers ran more motion than anyone else on
  the chart" undersells it: they were 1st in the league.
- **Wristbands:** "notably cool on wristbands" is sourced to 2017; add "at least early in his 49ers
  tenure" unless there's a newer source.
- **fig-three-names:** the "'60': five linemen and the back block" label's lower line sits ~0.5 yd
  above the field's bottom edge (window -7.0, label at -5.6 with two lines). Move it to d = -5.0, or
  widen the window to -7.8 for the 1.5-yd margin rule.
- **fig-run-and-shoot, right panel:** the slots' grey not-taken stubs at ~6 yards nearly touch the W and M
  boxes. Nudge the stubs to d = 6.5 to 7.5 or shorten them.

---

## Checked and correct (no change)

- Coryell digit order X-Y-Z and "619 = X dig, Y flat, Z go", with H's route named separately. "896" =
  post/seam/dig as Brown has it. The route numbers match 04-01's tree.
- Every formation is legal (7 on the line in all the figures I checked: trips, bunch, empty, double slot,
  21-personnel I with an attached TE, 10 personnel, empty trips left). The receivers are numbered
  outside-in correctly in all three Ghost panels and in Predict 3.
- The Ghost definition, Ghost-Tosser two-sided calls, and the position-not-letter principle are right.
- Shanahan "one look, many plays" logic, the radio cutoff, McVay talking to the cutoff, and the huddle and
  tempo cost.
- R&S reads (outside: go if you can beat him, hook if you can't; slots: split two-high, break off
  vs one-high, away from the defender over them), and the R&S defensive shells (4-2-5 single-high with the SS rolled
  down; Cover 2 with low corners).
- Air Raid character (small menu, reps, one-word or signal calls, weak power-run and under-center PA in the
  pure form). Washington as the NFL Air Raid-lineage example matches the chart (no-huddle 63% 1st,
  under center 15% 32nd, QB designed runs 2nd).
- Spread-option-as-language framing, and its "package inside another system" conclusion.
- Install layers (base → tags → weekly) and the Wed/Thu/Fri/Sat rhythm (sourced, and hedged).
- The fingerprint method (neutral situations, FTN motion definition, sneaks and kneels excluded from QB runs)
  is sound. The contrasts drawn from it (Rams/49ers vs Chiefs, Washington) match the cells.
- Predict 2 and 3 defenses are sensible (nickel stuck vs 10 personnel; Cover 3 vs 3x1 empty with the
  SS as the trips-side flat defender). The Predict 3 read (curl-flat defender, with the third-and-7 YAC
  caveat) is right.
