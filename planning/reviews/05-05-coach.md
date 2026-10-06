# 05-05 Run Fits and Box Math: coach and film review

Reviewer: veteran NFL coach and film analyst, technical pass. Rendered from `pdfs/05-05-run-fits-and-box-math.pdf` (22 pp.). I looked at every figure at 130 dpi: Figs 1 to 11 and the force-finder output.

**Verdict.** The chapter is strong and teachable. Force, spill, box and alley are explained the way a defensive staff teaches them. The power fit chart is the right centerpiece, and the data section is honest. Nothing below is a rewrite. There are **3 football errors** that a coach would circle in red (A1 to A3), some **alignment and label errors** in the diagrams (B), and a list of **nuances** a coach would insist on (C).

---

## A. Errors to fix (wrong as written)

**A1. "Gaps move" paragraph (after the fit table, about line 750).**
- The text says: "After the snap, the right A gap has a nose, a tackle and two linemen in it." That is wrong. The nose is a **1-technique shaded to the offense's left** (`over_front`: `T("1", -s)`), so he is in the *left* A gap, and the center blocks back on him away from the play.
- The play-side A/B area is clogged by the **3-technique and the RT/RG double team**, with the center's back block beside it.
- Fix: "After the snap, the right A and B gaps are full: the 3-technique, the right guard and right tackle doubling him, and the center blocking back next to them."

**A2. The Watch-for-it force rule contradicts corner force.**
- The bullet "outermost defender within about seven yards of the line **and inside the widest receiver**" is also coded in the Go-deeper function `force_candidates(... inside_of_wr=1.0)`.
- That rule can never find the Cover 2 cloud corner. Fig 1, Drill 1 and the text all put him **a step outside** the widest receiver (CB at w=15.8 vs Z at 15.0). So the very next sentence ("Corners squatting at five yards with both safeties deep: corner force") can't come out of that rule.
- Fix the text: "the outermost defender within about seven yards of the line (ignore a corner who is deep or pressed on his man; count a corner squatting at about five yards when both safeties are deep)."
- Fix the code: allow a corner when depth ≤ 6 and two defenders are deeper than 10, or drop the `inside_of_wr` filter and filter by depth ≤ 6 for corners.

**A3. Scrape-exchange "cost" paragraph (after Fig 6) misstates the risk.**
- The text says the Will's backside B gap "was empty for a moment… If the back had kept the ball (if the end had stayed home…)". But in a scrape exchange the end **is** the B/dive player. His crash fills the gap the Will left. The gap is empty only if somebody busts, which is not a cost of the call.
- "If the back had kept the ball" is also garbled; the back never has the ball to keep.
- The real costs coaches worry about:
  1. **Arc/insert.** A TE, H-back or slot arcs to the scraping linebacker, and then nobody has the QB.
  2. **Bend.** A flat, too-deep crash lets the back bend behind the end into the vacated B gap.
  3. **Reading the scraper.** The offense reads the LB instead of the end, or flips the read with inverted veer or a "bluff" block on the end.
  4. **Depth.** The scraper has to get from ~4.5 yards deep to the QB's path, so a deep or wide LB alignment is a pre-snap tell.
- Rewrite the paragraph around arc/bend/read-the-scraper and keep "a gap exchange is a bet on the first picture."

## B. Diagram alignment, label and depiction issues

**B1. The right end is labelled "5" but aligned on the tight end's outside shoulder (a 9).**
- `even4()` puts SE at `T("5", 1) + 1.6` = w 5.6. Y is at 4.8, and gridiron's 9-tech = 5.7, so he is a **9-technique**, not a 5.
- Visible in Figs 4, 5, 7, 9 and 10 (the right "5" sits on top of Y).
- Either label him "9", or align him at `T("6")`/`T("7")` (head-up or inside shoulder of Y) and label accordingly. For Fig 4 (outside zone, reach block) a **6 or 7** is more realistic: nobody reaches a 9 with a TE.
- 05-01's numbering is the reference, and a reader who just learned it will notice.

**B2. "4-3 Over" with the Sam on the line contradicts 05-02.**
- 05-02 defines the 4-3 Over with **the Sam off the ball** outside the TE. A Sam on the line outside the TE is its *Under* tell.
- `over_front()` (inherited from 03-03) stands the Sam on the LOS in a wide 9 (d=1.0, w=7.0). This affects Figs 1, 2, 3 and 11 and the table.
- Fix with words, not geometry: "a 4-3 Over with the Sam walked up on the line outside the tight end (a wide 9)" in the text, the Fig 3 title/caption and Drill 3. Or move the Sam to d≈2.5 to 3, w≈7, still the kick-out target.

**B3. Fig 5 (plus-one): the rotated safety lands outside the shaded box.**
- The box shading runs w −5.4…6.9, but the SS is sent to (5.8, **7.0**). The ringed "plus-one" sits on or just outside the edge of the box the caption says he is now inside.
- Land him at about (5.5, 6.0), outside the Y but inside the shading, or widen the shading to 7.6 (still ~2.8 yds outside the TE, consistent with how NGS draws the box).

**B4. Fig 3 (fit chart): the puller loops too deep.**
- The LG's pull goes via (−3.4, 0.2) and (−3.4, 3.4), three and a half yards deep, almost at the fullback's depth. Power pullers pull flat (about 1 to 1.5 yds, skimming the heels of the down blockers) and turn up at the kick-out.
- Use `via=[(-1.0,-1.3), (-1.3,0.4), (-1.3,3.4), (-0.6,4.8)]`. In Fig 2 the spill/box pull at −2.3/−2.4 is acceptable but could also come up a yard.

**B5. Fig 3 badges.**
- Badge 2 (NT) floats up and right of the nose, next to the Will's arrow and the RG's climb line, so it reads as belonging to them. Use offset (0.0, −1.6) for NT.
- Badge 4 (play-side end) sits on the RG's climb path. Use (1.6, +0.9).
- Badge 5 sits between the Y's block bar and the Sam. Use (+1.4, +1.6).

**B6. Fig 3: the back's arrow is the bounce, not the play.**
- The RB's thick arrow goes *outside* the Sam to the SS. That is the bounce after the spill, not power's designed path (between the Y's down block and the kick-out).
- Caption: "…and the running back's path after the spill (the bounce)." Optional: a thin dashed line for the designed path inside the kick-out.

**B7. Fig 2, frame 6 (box, +2.0 s): the payoff is unreadable.**
- The RB (green ring), the Mike and the pulling LG stack on one spot, so the reader can't see "the M filling the hole."
- End RB at (0.3, 4.0), MIKE at (1.6, 4.3) and LG at (0.9, 5.3) so the three markers touch but don't overlap. Or use t≈1.8.

**B8. Fig 4 (outside zone): the SS has no label.**
- The play-side safety's arrow is unlabelled while the backside FS is labelled "cutback alley." Add "SS: alley" (or put it in the caption) so the force/alley pairing taught earlier appears on both sides.

**B9. Fig 9 (Drill 1): safeties too wide.**
- Safeties at w = ±10 (between the hash and the numbers) is wider than a Cover 2 safety with the ball in the middle. NFL hashes are about ±3.1, and a half-field safety is typically 1 to 3 yds outside the hash. Use ±7 to 8 at 12 to 13 deep. The caption claim "outside the hashes" stays true.

**B10. Formation legality.**
- Every formation is legal: 7 on the line, X on the line in 21/11 I-form and singleback, Z and H off. Drill 3's Z at 9 yds off the line keeps Y as the end. No issue.
- Defensive depths are realistic (LBs 4.5 to 5, rolled SS 6 to 6.5, corners 7 / squat 4.5, safeties 12 to 13).

**B11. Labels.** No field-edge clipping in any figure. Minor overlap only in Fig 6 frame 4, where the tackle X sits on the W/Q markers. Acceptable, but nudge the X spot 0.6 yd downfield.

## C. Nuance a coach would insist on (add a sentence or two each)

**C1. The offense's answer to spill: kick vs log.** When the end man wrong-arms, the puller doesn't run into the pile; he **logs** (wraps outside and seals the spiller in) and the back bounces behind him. That is why the force must be there. Against box, the kick-out *is* the right block. One sentence in "Why choose one or the other?" closes the loop.

**C2. Two-level spill.** Many spill defenses also have the play-side linebacker spill the **puller** (attack his inside half). Fit chart row 6 instead has the Mike scrape over the top. Both are taught. Say so in the "spill inside, force outside" paragraph, and say who then owns the C gap inside the pile: the play-side end fighting across the Y's down block (row 4 already implies it).

**C3. The vacated play-side A gap in the fit chart.**
- The Mike leaves the right A gap to run over the top. The table doesn't say who inherits it. The answer is the 3-technique holding the double and the Will folding from the backside.
- Row 7 ("own the backside A gap") duplicates row 2 (the nose owns backside A), which is the "two in one gap" the chapter warns about.
- Rewrite row 7: "Slow flow: backside B gap and the cutback first, then fold over the double team into the play-side A gap the Mike left."

**C4. "Squeeze" has two meanings in this chapter.**
- Glossary: squeeze = box technique vs the kick-out.
- Table rows 1 and 4 and 05-01: squeeze = an end closing down on a down block.
- Add one sentence after the box definition: "Coaches also say squeeze for an end closing down behind a down block (05-01). The two usually happen in sequence: squeeze the down block, then box or spill the kick-out."

**C5. "Cloud" ≠ only Cover 2.**
- Sky = safety force, cloud = corner force. That's right, but cloud is also a Cover 3 call (Cover 3 cloud to the boundary), and Cover 3 also has **buzz** (safety to the curl, the OLB/nickel becomes the force).
- Add half a sentence to the force section so readers don't equate "cloud" with Cover 2 or "Cover 3" with "the safety is the force."

**C6. The overhang (apex) defender is the forgotten run fitter.**
- In Figs 5 and 7 and Drill 2 the nickel ($) stands at 4.5 deep, ~3 yds outside the LT. He is unblocked, and on a zone read toward his side he is the natural QB player.
- Drill 2's answer ("seven against six, free men are twelve yards away") should note that the $ makes the read side 7 v 7. That is exactly why offenses attach a bubble/glance RPO to "block" him (link the [overhang defender](04-06) / [apex](05-04) glossary entries).
- This is the most important missing modern-NFL nuance.

**C7. QB-designed runs make the RB a blocker.** "Count the quarterback" covers the read. Add that on **QB-designed runs** (QB power/counter, the Ravens' and Eagles' staple) the back becomes an extra lead blocker: the same +1 from the other direction. It strengthens the Ravens 2019 box.

**C8. Drill 2 vs the Ravens film room.** Drill 2 calls "two-high, six in the box, end sitting still" "the Ravens' 2019 picture." The Ravens film room says defenses met Baltimore with 7+ boxes 65% of the time. Change the drill line to "the picture the Ravens punished whenever they got it" or "the picture every defense tried to avoid against them."

**C9. Drill 3 answer: "check out of the spill call when a receiver cracks."**
- A defense can't check after the snap. Reword: "Many defenses tie it to the split: a reduced split pre-snap triggers a 'crack' call, and the corner and safety communicate crack-replace (some staffs also switch the end man to box so the ball stays inside)."
- Also mention that a tight Z is the classic tell for **crack toss/sweep**, not just power with a crack.

**C10. Tite front phrasing (end of plus-one section).**
- "Two-gapping linemen… let six defenders cover seven gaps, which is the whole idea behind the tite front" misstates 05-03.
- 05-03 sells the tite as five men on the line walling off the center and both B gaps so the linebackers stay unblocked; the nose is the main two-gapper.
- Reword: "…or put five men on the line, with a nose who two-gaps the center, so the linebackers stay clean: the tite front of 05-03."

**C11. Force technique sentence.** "Come up too fast and too far inside… a 'leaky' or 'soft' edge" mixes terms. In coach-speak, "soft" force is the slow, deep version and "hard" force is the fast, tight version. Name **hard vs soft force** (a cloud corner plays hard force, a deep-third or quarters safety soft/secondary force). It's one line and very standard.

**C12. Outside zone edge.** "There is no kick-out to spill" is true for outside zone. Add half a sentence that **split zone / insert** brings back a kick-out-like block (the slice), where the end chooses spill or box again. The Svec footnote already cites "Defending Split Zone", so the text should mention it.

## D. Film room / examples

- **Seattle 2012–15 (Chancellor as the eighth man):** well chosen and accurately characterised (single-high Cover 3, Thomas post, Chancellor box/force; scoring-defense leader 2012–15).
- **Eagles 2024 D (Fangio light box):** accurate and well sourced. The Week 2 Atlanta wobble is a nice honest touch. Consider naming the interior players the bet relied on (Jalen Carter, Jordan Davis, Milton Williams in 2024) to make "the front must be good enough" concrete.
- **Ravens 2019:** good, and it correctly reframes the spec's "vs light boxes" into what the data show (defenses loaded up and still lost). See C7 and C8.
- **Eagles 2024 offense (Barkley vs light boxes):** good. Mention Hurts' run threat and the QB-run game as part of why the box was light (C7).
- "The two-high coverage that has grown fastest" (quarters) is a slight overreach from the cited numbers (Cover 4 17.2% vs 13.9%). Prefer "that has grown fastest among the named coverages in NGS charting" or just "a fast-growing two-high coverage". Leave to the fact-checker.

## E. Gridiron use / animations

- Two animations (spill/box strip, scrape-exchange strip), well under the cap. Strip timing tells the story in print, apart from B7.
- Helpers are local to the chapter (`over_front`, `even4`, `strip`/`video`), and gridiron is untouched.
- Possible library gap for notes: `defense()` has no Over front with a walked-up Sam, and there is no technique-labelled TE alignment helper. That is why B1/B2 crept in.
- BDB handling is correct: simulated play labelled "simulated, BDB-format", and the real-data cell is `eval: false` via `bdb.prepare()`.
- Data chart (Fig 8): sound filters, source break marked, CIs shown, and the "budget" interpretation is appropriately hedged for the thin FTN 8+ dropback bin.

## Priority order
A1, A2, A3 → B1, B2, B3 → C3, C6, C1 → the rest.
