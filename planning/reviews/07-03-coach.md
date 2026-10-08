# 07-03 Coach / film-analyst review

Reviewer role: veteran NFL coach and film analyst. Scope: football correctness, diagrams, missing nuance,
film-room examples, and how the chapter uses gridiron. I reviewed `pdfs/07-03-zone-blitz-and-simulated-pressure.pdf`,
built 21:47, one minute after the qmd's last edit at 21:46. All 21 pages were rasterized at 80 and 150 dpi
(`_pdfbuild/07-03-zone-blitz-and-simulated-pressure/coach/`), and I looked at all 11 figures, with enlarged crops of
Figs 1, 2, 3, 4 and 5. I re-ran the third-down chart's by-season claim against nflverse. It holds: in every season zone is
lowest at 4–6 yards and highest at 11+ (2023: 30/22/34/43%, 2024: 19/16/24/32%, 2025: 33/22/48/64%).

**Verdict:** this is a strong chapter. It has the right big ideas (the exchange, count to eleven, holes live next to the
slowest dropper, protections lose to rules, sim pressure only works if the blitz is real), it frames the history honestly,
and the data section is good. It needs no structural rewrite. But four football errors would get flagged in any staff room:
(1) the "count to eleven" table makes quarters a two-deep coverage; (2) the fire-zone strip has no contain rusher on the
dropper's side and a quarterback throwing hot against a protection that is not short; (3) the fire-zone underneath
structure in Fig 2 and Fig 3A does not match the text (the "middle" dropper is not in the middle, and in 3A a defensive
end is carrying the seam); (4) the hook describes a four-man rush and calls it a zone blitz. The diagrams also have a
recurring readability problem: **rush arrows for the down linemen are nearly invisible** (the targets sit about 0.5 yd
from the start), so the reader cannot count "five rush" in Figs 1, 3 and 4.

---

## A. Football errors (fix these first)

### A1. "Count to eleven" table: quarters is not 4-rush / 5-under / 2-deep
- Row "Four-man rush, quarters or Cover 2 | 4 | 5 | 2" is wrong for quarters. Quarters is Cover 4: four deep and three under.
  The glossary entry the book uses says so ("four defenders each take a deep quarter").
- **Fix:** split the row into **Cover 2: 4 / 5 / 2** and **Quarters (Cover 4): 4 / 3 / 4**. If you want nuance, add one
  clause noting that in match quarters the safeties are run-first and the corners carry #1 deep, so on many snaps it plays
  like 3 under plus 4 deep readers. Also fix the next paragraph: "showing two deep safeties and two off corners" is
  consistent with either shell, so the cap argument still stands.

### A2. Opening hook: the play described is a sim, but the analyst calls it a zone blitz
- As written, six show (four DL plus two A-gap mugs) and a safety creeps. At the snap one LB backs out and the DE drops.
  That leaves three DL and one LB rushing, which is **four**, a creeper by the chapter's own definition (and the safety's
  action is never stated).
- **Fix (one sentence):** say that the creeping safety **comes off the edge**. Then five rush (three DL, one LB, the
  safety), the end drops, and "zone blitz" is right. The alternative is to have the analyst say "simulated pressure", but the
  hook is meant to tee up the zone blitz first.

### A3. Fig 2 (`fig-fire-zone`): no left-side contain, and the hot throw is not justified by the protection
- **Contain:** the rushers are W (left B gap at w −2.9), LDT (left A), MIKE (right A), RDT (right B), RDE (right edge). With
  the LDE dropping, **nobody rushes outside the LT**, so the left edge is open for the QB to escape. No NFL fire zone drops the
  end without replacing his contain, and the chapter itself says in "The price of the creeper" that the rushers have to keep
  their rush lanes.
  **Fix:** make it a real end-drop fire zone. Option 1: LDT slants to the left B gap (end at about (−0.9, −2.4)), the Will
  creeps and loops to the **C gap / contain** (end at about (−1.2, −4.6)), and the Mike stays in the right A gap.
  Option 2: keep the Will in the B gap and have the **nickel** come off the left edge, which turns it into Fig 3A. Option 1
  is cleaner and keeps the strip distinct.
- **Why the QB throws hot:** the strip shows six blockers (5 OL plus RB stepping left) against five rushers, all blocked. A
  well-coached QB is *not* hot in that picture. The text's "He doesn't count blockers; he trusts his rule" reads like a QB
  error, not a defensive win. The classic fire-zone kill is the **5-man (back-out) protection** or a **check-release back**:
  the QB is hot by rule off the second-level defender on that side ("hot off the Will"). He has to decide at the snap, before
  he can see that the end dropped.
  **Fix:** release the RB (for example a short flat or check-swing, `r.path((0.5, -1.5), (1.5, -5.0))` on the left) so the
  protection is five blockers against six possible rushers (4 DL + 2 LB). Rewrite one sentence: "With the back out, his rule
  is simple: if the Will comes, the ball comes out hot to H." Update the caption sentence "Six blockers handled five rushers
  perfectly" to "Five blockers handled five rushers; the defense won with the man it took out of the rush." The point
  survives and the football is now right.
- **Timing:** the ball is out at 0.85 s and caught at 1.55 s, a 0.7 s flight for about 9 yards, which is slow for a slant.
  Throw at about 1.0 s and catch at about 1.45 s. Keep the DE's spot (5.9, −4.8) or deepen it slightly.
- **Frame 1 does not show the creep:** at −1.0 s the Will is still at 4.5 deep, level with the Mike, so "the Will creeps up"
  is invisible. Either take frame 1 at about −0.15 s (after the creep) with a short orange creep arrow drawn from his start,
  or retitle it "The look". The ghost in frame 2 sits at the crept spot, which helps only once you know.

### A4. Fire-zone underneath structure: the text's "middle dropper" is not in the middle in Fig 2, and in Fig 3A a DE is carrying the seam
- The text (fire-zone section) says the three under are seam-flat / middle hole / seam-flat, and "that middle spot is where
  the dropper usually goes". In Fig 2 the underneath defenders end at **NB (6.5, −11.5)**, **LDE (5.9, −4.8)** and
  **SS (15, 9.3)**. The dropper is a left curl/"hot" player, not the hole player, and **w −1 to +7 at 5–10 yards has nobody**.
  The SS also ends 15 yards deep, so he is effectively a fourth deep player and the right underneath is empty.
  **Fix:** (a) NB is the left seam-flat at about (6.5, −10); (b) LDE drops to the **hole** at about (6.0, −2.5) (a 3–4 yd
  lateral, realistic in 1.3 s); (c) extend H's slant so it breaks at about 2 yd and is caught near (4.5, −4.5), across the
  hole; (d) the SS walls Y and carries him only to about 11–12 yd (end at about (11.5, 9.0)), then passes him to the deep
  third. Then the text, the caption and the picture agree.
- **Soften the text claim** too. In practice an **end** usually drops to the curl/"hot" window on his own side (or plays the
  boundary seam-flat), and a **tackle** drops to the hole. Suggested wording: "That middle spot, the 'hole', is where a dropping
  tackle usually goes; a dropping end usually takes the curl window on his own side, right where the hot slant wants to go."
- **Fig 3A (edge fire):** the LDE replaces the nickel as the **left seam-flat** (5.5, −6.5) against a 2x2. His first job, by
  the chapter's own rule, is walling #2's vertical, and a defensive end cannot carry H up the seam. This is the best-known
  fire-zone beater ("seam vs. the dropping end") and the panel doesn't show it.
  **Fix:** add a third red hole labelled "seam" at about (13, −8.5), between the LCB's third and the FS. Add to the caption:
  "...and the seam over his head if H runs vertical, the classic fire-zone beater." Then add a clause to the reading paragraph.

---

## B. Diagram fixes (readability and realism)

### B1. Rush arrows are invisible for the down linemen (Figs 1, 3A–C, 4)
- `to(p, k, (0.2–0.4, w), "rush")` moves a DL starting at d=1.0 only 0.6–0.8 yd, so the arrow is hidden under the marker.
  In Fig 3 the caption says "five rush in every variant", but you can see only two arrows per panel. In Fig 1 the nose, the
  weak end and the weak OLB look like they are standing still.
- **Fix:** end every rush in the backfield at **d ≈ −1.8 to −2.5** (QB depth −5), aimed at the rusher's gap and landmark
  (for example the NT to (−2.0, −0.6), the WDE to (−2.2, −3.0), the WOLB/contain to (−2.5, −5.8)). Keep the paths crossing the OL
  markers; that is how staffs draw rush lanes.

### B2. Fig 1 (Steelers plate)
- **Mike's rush and the SDE's drop share one line:** the Mike rushes from (4.5, ~1.6) to (0, 2.5) straight through the SDE
  ring, and the SDE's dashed drop to (6.5, 1.5) is hidden under the Mike's marker. The defining exchange of the figure is the
  one thing you can't see. **Fix:** drop the SDE on a slight inside-out path, `drop_to(p, "SDE", (6.5, 0.5), via=[(2.5, 2.2)])`,
  and bring the Mike just outside him through the B gap with a curved rush, `via=[(2.2, 3.0)]`, ending at (−2.0, 2.4).
- **"B" for the outside linebackers is a dialect trap.** In the LeBeau/Capers Steelers 3-4 that this plate depicts, the
  **Buck** (and the Mack) were the *inside* linebackers. Readers who look up Steelers terminology will be confused. **Fix:**
  label the OLBs **S** and **J** (Sam / Jack) or simply **OLB**, and change the caption to match. If "B" is a book-wide
  gridiron default, note it as a gridiron issue.
- The SS starts at (4.2, 8.2) and the SOLB drops to the flat at (6.5, 10.5), which swaps the two. That is a good exchange; say
  "the safety and the outside linebacker trade jobs" in the caption, because that is how a coach would describe it.

### B3. Fig 3C (corner fire)
- The "hot hitch" hole is drawn at (6, 17), **outside** Z (w 15). A hitch sits in front of Z. **Fix:** hole center about
  (5.5, 14.5).
- The SS's dashed drop line runs through the right edge of the (11.5, 9) hole label. **Fix:** move that hole to about
  (11.0, 7.5), or send the SS via (12, 11.5).
- Optional realism: the SS rotating from (8, 8) to (15, 15) is a 10-yard trip. Many staffs would start him at about 10 deep and
  w 6–7 in a "sky" look before the corner fire, so the rotation is believable.

### B4. Fig 4 (`fig-protection-bust`): who is hot by rule?
- With a full slide right (LT left B, LG left A, C right A, RG right B, RT right C) and the back on the left end, the walked-up
  **SS on the right edge is unblocked by rule**, so the QB's pre-snap hot is to the **right**, off the SS, not H's slant on the
  left. As drawn, the caption says the hot is "the slot receiver's slant into the space the nickel left". That is a
  post-snap sight adjust, not the protection's hot.
- **Better teaching picture (and more accurate):** add Y at (−1.5, 9.0) with a hot slant/seam-replace route, and have the SS
  drop straight into Y's hot window ("the man who made the QB hot drops into the hot throw"). The nickel still comes free off
  the left edge because the back's man (the LDE) dropped. Keep H, but describe his slant as a sight adjust. This adds one
  receiver (fine for a half-field view) and makes the "protection bust" logic airtight.
- "The nickel comes off the left edge untouched": a coached back whose end drops scans outside next. Say "the back, set on an
  end who left, is late to him". That is the same wording as the creeper caption, and it is truthful.
- Again, the LDT and RDT rush arrows are invisible (B1).

### B5. Fig 5 (`fig-creeper`)
- **Frame 1 is titled "Six at the line" but shows five** (E, T, M, T, E). The nickel is still 5 yards deep at −1.2 s (his
  creep has not started) and the Will is at 4.5. **Fix:** take frame 1 at about −0.1 s, or start the nickel's motion earlier
  so he is at about 2.6 deep by −1.2 s. The caption's "six defenders at the line" then matches. The same applies to the web
  `times`.
- **LT standing alone while the nickel runs past him (frame 4):** a man-side tackle whose end drops does not stand still. His
  rule is "if my man drops, help inside" (or "look outside"). The realistic and more instructive version: **LT turns in to help
  the LG on the 1-technique**, which is *why* the edge opens and leaves the back alone on the nickel. **Fix:** LT's second
  waypoint at about (1.3, −2.0, −2.0) facing inside, and change the caption to "the left tackle, his end gone, turns in to help
  the guard".
- The note "C: no one to block" at (−5.6, 6.5) floats 6 yards right of the center with no leader, so readers may tie it to
  the RT or to empty grass. **Fix:** put it at about (−4.0, 2.5) or give it a leader line with `point_to` (the snapshot
  `notes` would need a leader option inside the chapter helper).
- In frame 1 the ball marker sits on the mugged Mike's box. Nudge the Mike to d=1.5.

### B6. Fig 8 (Predict 1): the double A-gap mug overlaps the tackles
- The Mike and Will at d=1.3 and w ±0.8 sit almost on the DL row (d=1.0) and touch the T boxes and each other, so the rings
  overlap. Real mugs stand about 1–2 yd off the ball. **Fix:** MIKE=(1.9, −0.9), WILL=(1.9, 0.9).

### B7. Fig 10 (Predict 3): green rings are never explained
- The reading guide defines purple (dropper) and red (rusher to watch), but the CB/$/CB rings are green. **Fix:** add
  "(ringed)" to the caption: "...both corners pressed (ringed)... the nickel (ringed) is up tight on the slot."

### B8. Layout (print)
- Pages 4 and 6 are roughly half empty because the figures float. If the print filter allows it, put each fire-zone figure
  before the paragraph that introduces it, or reduce its height slightly. This is cosmetic, but a reader notices it.

---

## C. Missing nuance a coach would insist on

1. **Fire zones are not only a passing-down call.** "That is why zone blitzes are mostly a passing-down call" overstates it.
   The 1990s Steelers, and many college and NFL staffs today, call fire zones on first-and-10 as **run/pass pressures**: the
   slanting DL and the linebacker through a gap wreck zone-run blocking, and three deep still protects against play-action.
   **Suggested wording:** "That is why zone blitzes are mostly a passing-down call, though defenses also use them on early
   downs as run-and-pass pressures, slanting the line into one gap and bringing a linebacker through the next."
2. **The "53" defense.** Arnsparger's Matheson package was known as the **"53" defense**, after Matheson's jersey number.
   It is the detail every coach knows and it humanizes the history. Add it (Brown's Grantland piece and the Zone blitz
   Wikipedia article cover it; have fact-check confirm).
3. **Hot vs. sight adjust.** The chapter uses "hot throw" for two different things: the QB's protection-based hot (more
   rushers than blockers, so throw off the unblocked man) and a receiver's sight adjust or "hot off the LB" read. Fire zones
   beat the first by making the protection *think* it is short, and the second by putting a dropper in the replace window.
   One sentence in "Why the protection loses" would fix A3 and B4 conceptually as well.
4. **Seam-flat rules in one line.** "Wall #2, carry him to about 10–12 yards, then sink or squeeze the flat when #1 breaks
   out" is the coaching point that explains why fire zones die against seam routes and win against quick outs. The chapter
   has most of this; add the depth.
5. **Dialects** (the brief asks for terminology across systems). Add a short "Go deeper"-style aside: Saban/Belichick staffs
   say "fire zone" (also "Fire X", "Field/Boundary fire"); LeBeau's linebacker blitzes were "dogs" (e.g., "Crash Dog");
   many staffs name the underneath players "hot 2 / hot 3" or "seam-flat / hole"; "creeper" sometimes means specifically an
   off-ball player replacing a dropping lineman, while "sim" covers any four-man pressure look; protections ID the "Mike" with
   calls like "Ringo/Lucy" or numbered "56" points. Even three lines would satisfy the dialect requirement.
6. **Cover 0 from a two-high look (Predict 1 answer).** The answer argues six won't come from two-high and off corners. That is
   right on percentages, but Spagnuolo-style "two-high to zero" late spins are real on third-and-long. Add: "Watch the
   safeties at the snap: if both drive down late, it's zero, and the hot throw is now right."
7. **Two-high behind sims.** "Played with two-high coverage behind it as often as Cover 3" is an unsourced frequency claim.
   Either cite it (FTN/participation can show the shell behind four-man rushes with a blitzer) or soften it to "often with
   two-high coverage behind it, not just Cover 3".
8. **Protection answers.** The list of offensive answers is good. Add the most common NFL one: **turning the protection
   toward the dropper's side / "fan" the back to the edge and let the QB be hot off the interior**. Also add the TE "check-stay"
   (stays in if the edge threat shows, releases if it drops), which beats the exchange outright.

---

## D. Film rooms and history (accuracy)

- **Super Bowl XLIII, Harrison INT:** well chosen and honestly caveated. The framing is right: the QB reacted to expected
  pressure, and a counted rusher was in the lane. "The most famous coverage drop in Super Bowl history" is fair. (Fact-check
  should confirm the spot: the text says "1-yard line" from Patriots.com; other accounts give the 2. Keep it whichever way it
  is sourced.)
- **Ken Riley quote — timeline check:** Riley played for Cincinnati through **1983**, and LeBeau became DC in **1984**. The
  text places the quote among the "early tries" after LeBeau took the job and visited Arnsparger. Either the try happened
  while LeBeau was DB coach (1980–83), or the timeline needs rewording ("one of his first experiments, before he was even
  coordinator"). Flag for fact-check against Layden.
- **Ravens 2023 / Macdonald:** accurate and well characterized (low blitz rate, sim-heavy, interior DL dropping, Hamilton as
  the surprise rusher). Seattle 2025 facts match FACTS-current (SB LX 29–13, Durde DC, Macdonald calling the defense).
  Suggest one concrete "what to notice" tag that matches a diagram: "a 'Tag' sim (MatchQuarters, Oct. 2023): the nose drops
  and Hamilton or a linebacker comes through the vacated A gap." It is already sourced in [^matchq].
- **Flores 2023–24:** good, and the SIS four-vs-blitz pressure split is exactly the right evidence. FACTS-current confirms
  Flores is still Vikings DC in 2026; you could add "(still Minnesota's DC in 2026)".
- **Spagnuolo:** fine. The data line is good.
- **History framing** (Arnsparger idea, LeBeau system, Capers/LeBeau fame) is honest and matches AUTHORING §6's disputed-origin
  rule.

---

## E. gridiron use / chapter code

- The chapter-local helpers (`to`, `drop_to`, `timed`, `snapshot`, `strip`) are sensible workarounds for gridiron gaps:
  multi-point drops, time-scripted paths, and print strips with ghosts and rings. Worth listing for the library maintainer:
  (1) `Play.drop` takes only a straight line; (2) there is no time-keyed waypoint API; (3) there is no ghost/ring support in
  frame strips; (4) rush paths drawn under the start marker are invisible, so gridiron could enforce a minimum visible arrow
  length.
- `no_numbers()` finds yard numbers by `alpha == 0.55`, which breaks if style changes. That is fine for now; note it.
- The "B" OLB label (B2) may be a gridiron `defense("3-4")` default; check it and fix it there if so.
- Two animations, within the cap of about 4. Strip timing is good apart from frame 1 in both strips (A3, B5).

---

## Priority order
1. A1 (quarters row), A3 (contain + 5-man protection), A4 (fire-zone underneath structure + 3A seam hole), A2 (hook rusher count).
2. B1 (visible rush arrows everywhere), B5 frame 1 + LT, B4 (hot by rule), B2 (Mike/SDE overlap, "B" label).
3. C1, C2, C3, C5; D Riley timeline.
4. The rest.
