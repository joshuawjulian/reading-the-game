# Coach / film-analyst review: 02-05 A First Look at Defense

Reviewed 2026-10-06 against the chapter source and `pdfs/02-05-a-first-look-at-defense.pdf`
(21 pages, built 15:11, newer than the .qmd). I rasterized it at 90 dpi and re-rendered the
package and big-nickel/goal-line plates at 200 dpi. I checked helper coordinates in the `rtg`
container: `technique()` values and the `gun_2x2`/`ace`/`goal_line` alignments. I looked at
every figure.

**Verdict:** a strong first look. The five-question budget framing is the right way to teach a
fan to read a defense. The box/shell/rush data sections are honest about selection effects, and
the film rooms are well chosen. The nickel apex, mug and RPO drills are good coaching. There is
**one diagram/caption that teaches wrong protection math** (the blitz plate). There are also
**two captions that contradict the drawings or the text** (the shell plate's "eighth defender"
and the goal-line plate's "six linemen covering every gap"). On top of those come a 3-4
rush-pattern statement that is backwards for passing downs, an ambiguous box count in Drill 1,
and a short list of nuances. All the fixes are local.

---

## Must fix

### 1. `fig-rush-blitz`: the protection math in the caption is wrong
`pass_play()` has **Y and the RB both blocking in both panels** (`p.block(k, ...)` for
`"Y"` in the OL loop and `p.block("RB", ...)` in each branch).
- **Blitz panel:** that gives 7 blockers (5 OL + Y + RB) against 5 rushers. The caption's last
  sentence, "If the back had gone out on a pass route instead, the Mike would have been
  unblocked", is false. With Y still in, there are 6 blockers for 5 rushers, and the protection
  slides to the Mike. Even with 5 OL alone against 4 DL plus the Mike, a slide protection can
  account for him: the center, who has only a shade, takes the A-gap blitzer. A defender is
  "free" only when rushers outnumber blockers.
- **Four-man panel:** 7 blockers against 4 rushers leaves only 3 receivers out (X, H, Z). So
  "seven defenders cover" is covering three men. That is max protection, not the norm the text
  describes ("seven defenders cover five possible receivers").

**Fix:** release **Y** on a route in both panels (for example `p.route("Y", r.stick(6))`, or a
seam). Keep the RB in on the blitz panel and release him in the four-man panel (a check-release
or flat), or keep him in on both. Then:
- Four-man: 5 (or 6) blockers against 4, with 7 covering 4–5 receivers.
- Blitz: 6 blockers (5 OL + RB) against 5 rushers. The RB picks up the Mike, as drawn.

Caption: "The offense has six blockers for five rushers, so everyone can be picked up; the back
steps up to take the Mike. Send a sixth rusher (the Will too) and somebody is free, which is why
the quarterback must throw 'hot.'" Remove "The tight end has stayed in to block here as well."

### 2. `fig-shells` caption: "an eighth defender close to the run" contradicts the drawing and `fig-box`
In the one-high panel the box holds 4 DL + 2 LB + SS = **7**. `fig-box` says the same
("Now seven are in the box"), and so does the text that follows ("If you count seven in the
box, look for the second safety"). **Fix:** "...the strong safety (SS) is down at about 7 yards
beside the tight end, a seventh defender in the box." Also, "the other safety joins the box"
sits in the offense's backfield at (−4.3, 12.5), about 11 yards from the SS, with no pointer.
Move it to about (9.5, 12.5) and add an `arrow()` to the SS. The label is then ~6 yd from the
right edge (lateral ±20.5), which is clear of the field edge.

### 3. Goal-line plate (`fig-heavy-packages`, right): "six linemen covering every gap" is not what is drawn
In `goal_line_d()` the DL are at w = ±0.8, ±2.4, ±5.6. Against `goal_line`, where U and Y sit
at ±4.8 and the wing W at +6.2, that puts linemen in **A, A, B, B**, and the two ends **outside
the tight ends**. Both **C gaps (w ≈ ±4.0) are empty** on the line. The linebackers do not
cover them either: LB1 at −3.2 is stacked on the LT, and LB2 at +1.0 is over the RG. The
offense's right C gap, where it has two TEs and a wing, is about 3 yards from the nearest
defender. A goal-line coach would never draw that.

**Fix (gap-sound 6-3-2 against 23 with a wing right):**
- DL: ±0.8 (A gaps), ±2.4 (B gaps), and the ends to **7 techniques on the TEs' inside
  shoulders**, ±4.2 (C gaps).
- LBs: LB1 at (2.5, −6.0), D gap outside U. LB2 at (2.5, +5.6), D gap between Y and the wing.
  LB3 at (2.0, +7.6), outside the wing.
- CBs: leave LCB at (3.0, −8.5) and RCB at about (3.5, 10.5).

That is nine front players for nine gaps, and the caption can say exactly that: "six linemen in
the A, B and C gaps, three linebackers outside the tight ends and the wing: nine gaps, nine
defenders." Also check that the "6 DL, 3 LB, 2 DB" box stays clear of the wing; it is fine now.

### 4. 3-4 rush pattern stated backwards for passing downs (Common misconception, and the four-man-rush paragraph)
The current text is "a 3-4 team rushing four, with one of the outside linebackers dropping into
coverage **or both rushing and one lineman dropping**, is the normal case", plus "(or, in a 3-4,
three linemen and an outside linebacker)". The second variant, a lineman dropping, is a
**zone-blitz/simulated-pressure** pattern, which the chapter itself later says is a trick. The
normal NFL passing-down case for a 3-4 team is different. The nose comes off for the nickel back
(a **2-4-5 nickel**), and the four rushers are **two interior linemen plus both outside
linebackers**. On early downs in base it is three linemen plus one OLB, with the other OLB
dropping or rushing depending on the call.

**Fix:** "...so a 3-4 team usually rushes four: on passing downs the nose tackle comes off for a
nickel back and both outside linebackers rush with the two remaining linemen; in base, it is
the three linemen and one outside linebacker. A lineman dropping out while a linebacker rushes
is a disguise (simulated pressure, later in this chapter)." Make the same change in the
four-man-rush paragraph: "(in a 3-4 team's nickel, two linemen and both outside linebackers)".

### 5. Drill 1: the box count is ambiguous as drawn
The nickel back is at (5.0, −7.5), only **2.7 yards outside the in-line U** (−4.8). By the
chapter's own definition ("just outside ... including an attached tight end"; the box plates
use ~1.7 yd outside the end man), he is about 1 yard outside the box. Many analysts, and
probably NGS, would count a 5-yard-deep defender that close to a tight end **in** the box. He
is the force player on that side. A careful reader may answer 7 and be "wrong."

**Fix, either one:**
- (a) Widen him to about (5.5, −9.5), which is clearly an apex between U and X, and say so in the
  caption.
- (b) Keep him and make the answer say so: "six in the box, with the nickel back hovering just
  outside the tight end; count him as half. Even at seven, seven blockers against seven defenders
  is a fair fight, and the two deep safeties are 12 yards away." Option (b) is the better
  coaching point because it reinforces the "count him as half" line from the apex section.

---

## Should fix

### Diagrams
- **`fig-packages`, 4-3 caption:** "a linebacker (ringed) has to walk out over the slot receiver".
  The W is drawn at (4.5, −6.0), which is an **apex** between the LT (−3.2) and H (−9.0), not
  over H. Either say "walk out toward the slot" or move him to about (4.5, −8.0), so that he
  reads as "a linebacker matched on a receiver" and the nickel panel's $ apex then looks like an
  improvement. Same for the 3-4 W.
- **`fig-apex`, the "pass: take the slot" arrow** goes from the $ downhill to (2.9, −10.8),
  toward the line of scrimmage. To a coach that reads as "come up and tackle the bubble," not
  "cover the slot." Draw it widening and slightly gaining depth instead, to about (6.0, −10.0),
  as he would when carrying/collisioning the slot or getting to the curl-flat. Keep the label
  where it is.
- **Drill 2 (`fig-predict-2`) label collision:** the mug linebackers at d 1.7, w ±0.95 overlap
  the 3-technique "T" markers (the boxes touch in the PDF). Move M and W to d 2.2. That is still
  clearly "in the A gaps on the line" and it separates the markers.
- **Big-nickel plate:** the defense's right D gap, outside Y, has no one nearer than the SS at 12
  yards, because the SDE is a 7 tech inside Y and the M is at +1.8. That is defensible as a
  two-high run fit (the SS fits the alley). Since this panel sells "nickel speed, base size,"
  consider walking the M out to a 50/stack over Y, about (4.5, 4.0), or noting in the caption
  that the safeties fit the edges after the snap.
- **Man/zone strip** (timing 0 / 0.7 / 1.5 s) tells the story well in print. One nuance for the
  caption: the zone CB's path, sinking to 7.6 and then squatting to 4.0, is a **Cover 2 corner**
  (flat) technique. Say "(as a Cover 2 corner does)" so 06-01 can reuse the picture.

### Football text
- **"The package is not even in the call."** Too absolute. Many NFL call systems lead with the
  package word, for example "Nickel ... Over ... Cover 3", and the coordinator, or a personnel
  coach on the headset, signals personnel first and then the call, often in one signal. Suggest:
  "The package is usually settled a few seconds earlier, when players run on and off, and the
  call then assumes it." Soften the Madden callout's "three separate decisions" in the same way:
  "made at different moments, often by different people."
- **Box arithmetic is missing the quarterback.** The text says "on a normal handoff neither is
  the quarterback." True, but a coach would add the modern caveat in the same paragraph: when
  the QB is a run threat (zone read, RPO) the offense can "block" one defender by **reading** him,
  so it plays with one more effective hat. That is why shotgun offenses can run against seven.
  It is one sentence plus a link to the read-option/RPO chapters, and it sets up Drill 3.
- **Two-high ≠ zone.** The cover-numbers paragraph pairs Cover 0/1 with man and Cover 2/3/4 with
  zone, and the shell section says "one-high is the natural home of man". Name the most common
  exception in a parenthesis, **2-Man** (man underneath with two deep safeties), so the reader
  does not conclude "two-high means zone." Drill 2's answer depends on press plus one-high
  indicating man, which is fine, but readers will see 2-Man on third-and-long every Sunday.
- **"Man coverage is also how most blitzes are played"** is accurate. Add "(the main exception,
  the zone blitz, is in Part 7)" so it does not contradict 07-03.
- **4-3 vs 3-4 label today:** one sentence would help. Most NFL defenses are "multiple" (they
  play both even and odd fronts week to week), so "a 3-4 team" now mostly describes the bodies
  it drafts: stand-up edge rushers, a nose, 4i ends. This keeps fans from treating the label as
  the scheme.
- **Drill 2 answer:** add who takes the tight end, since a coach would ask. In that Cover 1 look
  the walked-down SS is the likely man on Y, or a "robber" if Y blocks. Also, "the offense has
  six blockers" assumes Y releases; say "(assuming the tight end runs a route)".
- **Eagles LIX "What to notice":** "The Eagles' linemen won their one-on-one blocks". Fangio's
  four still occasionally included a stand-up edge or a linebacker. Write "the four rushers
  (almost always linemen and edge rushers) won..." to stay exact with "zero blitzes" (which counts
  rushers, not who they were).
- **Giants XXV:** "What to notice" could add the other half of Belichick and Parcells' plan.
  The Giants' offense held the ball for about 40 of the 60 minutes, which kept Buffalo's no-huddle
  on the sideline. Fact-check the TOP figure before adding it: PFR box score, roughly 40:33. It
  makes "a decision about which yards you can afford" complete.
- **Landry "defensive coordinator"** in the body text is anachronistic for 1956. The footnote now
  quotes PFHOF ("full-time defensive coach"). Write "the Giants' defensive coach (what we would now
  call the coordinator)".

### Terminology dialects worth a line (glossary or a "Go deeper")
- Overhang aliases: **force player**, **alley player** and **flat defender** are all used for the
  same spot by different staffs. The Sam is the traditional 4-3 overhang to the strength.
- "Sub package" means nickel/dime to a defensive coach. The NGS article's "offensive sub packages"
  means the opposite, fewer than three WRs. The footnote explains it, but the film-room text says
  "the heavier groupings", which is fine. Just do not use "sub package" unglossed anywhere.
- "Dollar" and "quarter" are used for 6 *and* 7 DBs by different teams, as the text says, and some
  staffs call a three-safety dime "penny". This is optional.

---

## Checked and correct (no change)
- **Alignments.** The 4-3 Over-style front (7, 3, 1, wide 5) and the 3-4 Tite front (4i-0-4i
  with OLBs at 9 and wide 5) are realistic modern fronts. The nickel 4-2-5 is correct, with the
  $ at a true midpoint apex (−6.1, between LT −3.2 and H −9.0). The dime is fine.
- **Formations.** Every offense is legal: 7 on the line in `off_11` (X and Y on, H and Z off),
  `off_12` (both WRs off) and goal line (wing off).
- **Depths.** Safeties at 12.5 and corners at 7 for two-high; FS 13.5 and SS 6.5 for one-high.
  Press at 1.5 in the mug drill. The text's 12–15 / 10–14 yd ranges are right.
- **Box plate.** It agrees with the box definition, and the in-box ringing is computed, not
  hand-placed.
- **Apex section, and Drill 3's RPO read logic** (give if he widens, throw if he fills). Correct
  and well taught.
- **Data.** The box/success selection-effect discussion is exactly the caveat an analyst should
  make. The rusher/pressure/EPA panel is fairly framed.
- **Film rooms.** Seattle 2025 (Emmanwori), Baltimore/Hamilton (big nickel) and Giants XXV (the
  light box on purpose) are well chosen and accurately characterized. Eagles LIX (four-man rush)
  is likewise accurate, with the hedge above.
- **Labels and animation.** Labels sit inside the field window everywhere I looked, and the only
  collision is the Drill 2 one above. There is one animation (man vs zone), and its frame strip
  reads in print.

## gridiron notes (no edits made)
- `mz_play()` reaches into private API (`p._compile()`, `p._compiled`) to hand-keyframe the man
  and zone defenders, because `man()` closes onto the receiver and hides him. This works, but it
  is fragile if `Play` internals change. A public `p.keyframes(key, array)` or a `man(...,
  cushion=)` floor in gridiron would retire it.
- `no_numbers()` strips yard numbers by matching `alpha == 0.55`. It is also fragile, and a
  `Field(numbers=False)` option would replace it.
- `offense("goal_line")` is fine. A gap-sound `defense("goal_line", ...)` preset would have
  prevented item 3.
