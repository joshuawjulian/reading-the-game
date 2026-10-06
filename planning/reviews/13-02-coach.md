# 13-02 Coach / film-analyst review

Reviewer role: veteran NFL coach and film analyst. Scope: football correctness, diagrams, missing nuance,
film-room examples, and how the code uses gridiron. Reviewed the rendered `pdfs/13-02-expected-points-and-success-rate.pdf`
(built 07:27, after the qmd's last edit at 07:26). All 37 pages were rasterized, and every figure (1–14) was looked at.
Diagram pages 11 and 34–36 were also looked at again at 110 dpi.
Play-level claims were checked against nflverse pbp for `2025_22_SEA_NE`.

**Second pass (re-run of this review, 2026-10-06):** the qmd (07:26) and the PDF (07:27) have not changed since the first pass.
The PDF was rasterized again (`_pdfbuild/13-02-coach/`), and Figs 4 and 12–14 were looked at again. Every finding in A–D still
holds as written: the LCB in Fig 13 makes a 9-man box, the SS/W/wing-W stack sits on the right edge of Fig 14, the panel-1 label
collides with the 30 in Fig 4, and the backward pick arrow in Fig 4 has no explanation. Section E adds the new items.

**Verdict:** the football is sound and the analytics framing is honest. The chapter needs no structural rewrite.
It needs two diagram alignment fixes, one label collision and one unexplained diagram detail. It also needs about six
nuance additions that a coach would expect at Level 4. The most important are the 4th-down caveat on the EP curve,
QB sneaks inside "short-yardage runs", penalty snaps being dropped, and the WP context for the Super Bowl hook.

---

## A. Diagram fixes (exact changes)

### A1. Fig 13 (`fig-drill-short`, 2nd & 1, 22 personnel vs 4-3 Over): the box count is wrong, so the caption is wrong
- **Problem:** the helper puts **LCB at (d=6.5, w=-4.8)**, head-up on the U tight end, 6.5 yards deep. There is no
  receiver on that side, so the corner is sitting *inside the box*. Count the box players: DL 4, then SAM, MIKE and
  WILL, then SS (d=7, w=+6), then LCB. That makes **9 in the box**, but the caption and prompt say "eight". A corner
  head-up on a TE at 6.5 yards is also not how anyone aligns. Against a no-WR side, the corner sits outside the TE as
  the force/alley player.
- **Fix:** in the chapter cell, pass a modified list:
  `dfn = [q.moved(d=5.0, w=-9.0) if q.key == "LCB" else q for q in defense("4-3_over", "single_high", off)]`
  The corner then sits about 4 yards outside U's outside shoulder at 5 yards, and the box is a true 8 (4 DL + 3 LB +
  SS). Optionally `p.highlight("SS")` and add `p.note("8th man", at=(8.5, 6))` so the reader sees *which* player makes
  it eight.
- **Report for gridiron (do not edit):** `defense()` aligns a CB over the outermost eligible player even when that
  player is an in-line TE. On a side with no WR it should default to roughly w = TE.w ∓ 4, d = 5.

### A2. Fig 14 (`fig-drill-goal`, 1st & goal at the 1): second-level depths are too deep for goal line, and two players are both labeled "W"
- **Depths:** MIKE is at d=4.5, SS at d=5.0 and FS (moved) at d=4.0. With the ball at the 1, those players are 3–4
  yards deep in the end zone. On 1st & goal at the 1, goal-line linebackers and safeties sit at **1–2 yards**, toes at
  or just behind the goal line, and fill downhill at the snap. **Fix:** in the `goal_d` comprehension, also set
  `MIKE → d=2.0`, `SS → d=2.0, w=-3.0` and `FS → d=2.5, w=0`. Keep the CBs at d≈2 rather than 2.5 so they can press or
  squeeze the wing and the U.
- **Label collision:** the offensive wing TE (key `W`, at w=+6.2) and the defensive WILL (label "W", on the line at
  w=+7.5) sit almost on top of each other, both reading "W". **Fix:** relabel one of them. Either relabel the
  offensive wing (`H`, or `Y2`), or use the 46 dialect for the defender and label the strong-side WILL **"J"
  (Jack)**. In Buddy Ryan's 46 both outside backers set to the TE side. That is what the helper draws, and it is
  correct.
- Otherwise the picture is right: 7 on the line for the offense (U, 5 OL, Y), the wing off the line, 23 personnel, and
  a 46 front with 0/3/3 interior and both OLBs to strength.

### A3. Fig 12 (`fig-drill-empty`, 3rd & 9, empty 3x2 vs dime two-high): legal and realistic; one optional improvement
- Formation is legal: X and Z on the line plus 5 OL, with H, the RB-as-slot and Y off the line. Depths are realistic
  for 3rd & 9: CBs at 6.5, safeties at 12, DEs wide.
- To the trips side, the nickel (`$`) is over Y (#2). The #3 receiver (the back split out at w=+5.5) is owned by the
  MIKE at w=0. That is a correct 4-1-6 rule, but the picture does not show it. **Optional:** move MIKE to `w=+2.5`
  (inside-shade on #3), so the reader sees every receiver accounted for.
- **Stronger teaching fix:** the drill is about "empty yards", so draw them. Add `p.route("H", r.quick_out(6, 5))`
  (H is the left slot), `p.dropback(1.0)` and `p.pass_to("H", t=1.2)`. Add `p.highlight("H")` and a
  `p.note("catch at +7", ...)` short of the yellow line. Also give the flat/curl defender over H (`DB`) a
  `p.drop("DB", (7, -12))`, with a note "rally and tackle short of the sticks". This needs a small change to
  `situation_diagram`: return `p` before drawing, or take a callback. Right now the reader has to imagine the very
  play the answer is about.

### A4. Fig 4 (`fig-epa-worked`, three Super Bowl LX plays)
- **Panel 1:** the "EP after: −1.70 (4th & 4, own 27)" box sits on top of the "30" yard number. Move it to y≈16.5,
  or offset it to x = end − 3.
- **Panel 3:** the dashed pass arrow goes **backward 11 yards** (SEA 44 → NE 45). That matches pbp: the pick was at the
  NE 45 and returned 45 yards for the TD. But nothing on the figure says why a "short middle" pass ended up 11 yards
  *behind* the line, and a reader will think the drawing is wrong. The pbp line credits **Devon Witherspoon** with both
  the pass defensed and the QB hit (`(21-D.Witherspoon) [21-D.Witherspoon]`). **Fix:** add a short note at the
  catch point, "pick after Witherspoon's blitz hits Maye" (fact-check to confirm the deflection from video or a
  game report), or add one clause to the caption.
- LOS, line-to-gain and direction are correct in all three panels: 3rd & 12 from own 19 gives a line at own 31, and
  1st & 10 at opp 16 gives a line at opp 6.

### A5. Charts (Figs 1–3, 5–11): no football errors
- Fig 3 is fine as a picture, but see B1 for the caveat it needs.
- Fig 6: see B2 (QB sneaks).
- Fig 7: quadrant labels and the flipped defensive axis are correct. The text's "first, second, third in net EPA (LA,
  SEA, NE)" matches the table (0.201 / 0.194 / 0.176). Minor: the caption says "allowing fewer points is higher".
  Make it "allowing less EPA is higher".

---

## B. Nuance a coach would insist on

**B1. The 4th-down curve values what coaches *did*, not what they *should* do (Fig 3 and its caption).** EP on fourth
down is built from historical decisions. Those were mostly punts and field goals, and aggressiveness has shifted a lot
since about 2018. The "4th & 10" line in the plus-territory FG range and the steep fall in your own half reflect
league-average choices. Add one sentence plus a link to 13-03: "On fourth down EP bakes in the league's usual
decision; whether that decision is right is a win-probability question." Without it a reader will read the curve as
the value of the situation under good coaching.

**B2. Short-yardage "runs" include QB sneaks and the tush push (Fig 6 and the 2nd & 1 drill).** Sneaks convert far
more often than handoffs. They make up a large share of 2nd–4th & 1–2 runs, and they lift the run success rate in
exactly the bucket where the chapter says "runs succeed more often". Either split them out or say so. FACTS-current
says to use FTN `is_qb_sneak`, available 2022+. The chapter's 2021–2025 window would need 2022–2025 for that split.
Suggested sentence: "Part of that edge is the quarterback sneak, which converts far more often than a handoff; take
sneaks out and the run's short-yardage edge shrinks." Re-run the split and check the numbers before you print them.

**B3. Penalty snaps are thrown out (setup cell).** The filter `play_type.isin(["pass","run"])` drops every
`no_play`. In 2025 that is about **1,490 regular-season pass/rush snaps**, including **279 defensive pass
interferences (mean EPA +1.73)** and 374 offensive holds. To a coach, drawing DPI on a go route and getting flagged for
holding are part of what a play call produces. The cell comment does disclose it. Add a sentence to the three-choices
paragraph: this is why the chapter's EPA per play won't match rbsdm.com or other sites that keep `pass==1 | rush==1`
including penalties. Also say that dropping them makes passing look a little worse, because DPI is mostly a deep-ball
outcome.

**B4. The Super Bowl hook needs win-probability context.** At the Nwosu interception (4:37, 4th quarter), nflverse WP
had New England at **0.03**. At the Kupp catch, Seattle was at **0.89**. The "almost ten points" is right in EP terms,
but it hardly changed who won, which is exactly the "EP ignores the score" point the chapter makes later. One sentence
at the end of the worked example ties this together and sets up 13-03: "EPA says this was the costliest play of the
night; win probability says the game was already decided."

**B5. Selection effect #1 should name screens, RPOs and play-action.** Coaches treat screens as "long handoffs", an
extension of the run game, yet they count as dropbacks. On RPOs the run/pass label is whatever the QB decided
post-snap, so the run and pass piles are not clean play *calls*. Add these to item 1 alongside sacks and scrambles.

**B6. Success rate in coach dialect.** Staffs rarely say "success rate". They say "**efficiency**", "**win first
down**" and "**stay on schedule / ahead of the chains**", and many grade a first-down win as **4+ yards**. That is the
40% rule in practice. Mention this so the reader can map broadcast or coach talk onto the metric. It is a common
convention that varies by staff, so phrase it that way and don't attribute it to a single source.

**B7. The explosive-play definition: lead with the coaching one too.** The chapter uses 10/20 and only mentions 12/16
at the very end. Many NFL staffs chart explosives as **12+ runs / 16+ passes**. Say this in the explosives section
where the term is defined, so the 37% figure is read with its definition. Fact-check should source it (the Hoppen
piece already cited covers the competing definitions).

**B8. Limits of RYOE that a coach sees on film.** Expected yards come from the snapshot **at the handoff**. Anything
the blocking does *after* that counts as runner value: second-level climbs, a WR's crack or stalk block downfield,
and an outside-zone cut that only opens 4–5 yards later. So does vision, for example pressing the hole to set up a
block. That is part of why RYOE is only moderately stable (0.22). Add one sentence after the RYOE table. Also note
that RYOE ignores pass protection and receiving, which the chapter already says, so keep that.

**B9. Limits of CPOE.** Receiver drops count as incompletions, and receivers who separate inflate the expected
completion rate. So CPOE still carries some of the receivers' quality. Add a clause in the CPOE paragraph.

**B10. Play-action misconception callout: sharpen the "why".** "The fake works because runs exist in the playbook" is
close, but the coaching point is that **the fake has to look like your real run game**: the same OL footwork and
backfield action. Linebackers key that action, not the season's yards per carry. Change the wording to that and
keep the 04-05 link.

**B11. Turnover luck by fumble type (optional).** Recovery odds are not literally 50/50 by type. Strip-sacks in the
pocket and muffed punts lean toward the defense or kicking team, and aborted snaps lean toward the offense. The
team-level rate still doesn't repeat, so the conclusion stands. One clause adds credibility with coaches.

---

## C. Film room and named examples

- **Seattle 2025 film room: accurate, but it has no scheme in it.** The numbers check out: SEA has the best
  neutral-situation defensive EPA (−0.149) and New England lost three turnovers. The Walker runs were 30 yds at
  2Q 14:04 (2nd & 10, own 24) and 29 yds at 13:34 (2nd & 10, NE 46), as stated. Hall's strip-sack was recovered by
  Byron Murphy, also as stated. Sack EPAs ran −0.98 to −1.78, which fits "roughly one to two points". But "what to
  notice" is all ledger and no football. Add one line on *how* Seattle produced those plays. Use the 2025 split-safety
  trend in FACTS §10 (the NFL.com piece "The coverage that turned the Seahawks into Super Bowl winners") and the six
  sacks. If you say Macdonald called the defense in 2025, fact-check must source it, because FACTS lists only
  "HC Macdonald, DC Durde".
- **Ravens 2024 film room: mostly right, with one dated phrase.** "One of about a quarter of teams with positive
  designed-run EPA" checks out: 8 of 32 in neutral situations, with BAL 4th at +0.049. "Lamar ... on every option
  look" describes the Roman-era (2019–22) Ravens better than the 2024 Monken offense. That offense was built around
  Henry on gap and duo runs, with Lamar as a designed or keep runner. Reword to "with Lamar Jackson's designed runs
  and keeps forcing the defense to account for the quarterback". The football point, a QB run threat lightening the
  box, is correct.
- **Interception-luck paragraph.** Caleb Williams (7 INT vs 18 interception-worthy) is a fair "lucky" example. **Geno
  Smith** (17 INT vs 14 interception-worthy, with the Raiders in 2025; name the team) is called "unlucky", but he
  also charted among the most interception-worthy throws in the table. The honest read is mostly poor decisions with
  slight bad luck. Also delete "tipped balls and receivers' mistakes count against him": that is a plausible
  mechanism, not a verified one. Suggested wording: "...had more interceptions than interception-worthy throws, a
  small dose of bad luck on top of a high count of risky throws."
- **2nd & 1 drill answer:** "a first down very likely on the next snap anyway" is loose, because after a failed shot
  it is 3rd & 1. Replace it with: "and even if the shot falls incomplete, third-and-1 still converts about 70% of the
  time." That is 0.698 for neutral 2021–2025, checked with nflverse `first_down`.
- **Goal-line drill answer:** "why EPA rankings of short-yardage backs are dominated by fumbles" overstates it, since
  goal-line fumbles are rare. Change to "why one goal-line fumble can erase a short-yardage back's whole season of
  EPA."

---

## D. Code and gridiron use

- Sensible overall. `situation_diagram` is a clean wrapper, and the per-figure edits (`goal_d` comprehension) follow
  AUTHORING §4 ("adjust anything that's wrong with `.moved()`"). Fig 4 draws on a `Field` axis by hand, which is the
  right call because no gridiron helper exists for an EPA ledger strip.
- `situation_diagram` should return the `Play`, or accept a `setup(p)` callback, so the drills can add a route,
  `highlight` or `note` (see A3) without repeating the boilerplate.
- No animations. That is fine for this chapter, which has no motion or timing concepts.
- **Report items for gridiron (not edited):** (1) `defense()` puts a CB head-up on an in-line TE when there is no WR to
  that side (A1). (2) `goal_line` offense keys the wing as `W`, which collides with the defensive WILL label (A2).
  Consider `H` or `Y2` as the default wing label.

---

## E. Additions from the second pass

- **E1. Empty-drill answer (Fig 12): "fourth-and-2 at the 37, a punting situation" is the old-school read.** Most 4th-down
  models (for example Ben Baldwin's nflverse-based 4th-down bot) put 4th & 2 at the offense's own 37, tied in the 2nd quarter, close to a toss-up and
  often a slight "go". Keep the point (the 7-yard gain has negative EPA because the *expected* next play is a punt, see B1),
  but word it as "a situation where most teams still punt", and link 13-03.
- **E2. Same answer: the "success rate 4%" for 6–8-yard third-down gains short of the sticks needs one clause.** On 3rd
  down a gain short of the line should almost never have positive EPA. A reader will ask where the 4% comes from: mostly
  long gains deep in the opponent's half and field-goal-range shifts. Either say so, or drop the success figure and print
  only the mean EPA.
- **E3. Empty drill, what defenses actually do:** two-high dime against empty on 3rd & 9 is a legitimate call, but the
  answer reads as if it's *the* answer. Add a half-sentence: against empty, defenses also like to bring a five-man
  pressure or play Cover 1 / man, because the QB has no back to help protect. Two-high "rally and tackle" is the
  conservative choice. This also sets up the 13-04 tendencies chapter.
- **E4. Drill answers print inline in the PDF (pp. 34–36).** The Answer callouts render right under each Predict-the-play
  box instead of being moved to "Answers to Predict the play" by `filters/print-answers.lua`, so the reader sees the
  answer before trying. The callouts are `callout-note` (AUTHORING §8 says `callout-tip`, though the filter matches any
  callout) and appear nested inside the Predict box. Un-nest each answer, or make the filter recurse into nested divs,
  and switch them to `callout-tip`. (This is not a football issue; it is flagged because it breaks the drills.)
- **E5. Fig 13 caption: name the eighth defender.** Once A1 is applied, change the caption to "...a base 4-3 Over front
  with the strong safety rolled down to the tight-end side, eight in the box". The reader can then find the extra man the
  answer depends on.
