# 15-02 Film Study, Charting, Scoring Yourself: beginner-reader review

Reviewer role: casual fan, never played, has read 01-01 through 15-01 in order. Read the rendered
PDF (`pdfs/15-02-film-study-and-charting.pdf`, 27 pages, built 2026-10-08 10:02) start to finish
and looked at every figure page at 110 dpi. Page numbers are PDF pages.

**Overall:** this is a strong capstone. The strip-sack worked example (pp. 7–10) and the Brier/
calibration section (pp. 15–21) are the best teaching in the chapter, and the "same play, three
different lessons" payoff (p. 10) lands. The problems are mostly small contradictions a careful
beginner trips on, a few columns and objects that are never explained, and two promised skills
(joining log to chart; turning a chart into tendencies) that are described but never shown.

---

## 1. Terms used before they're explained, or never explained

| Where | Quote | Problem |
|---|---|---|
| p. 1 "You'll need" vs p. 2 | "coaches film shows every snap ... with no replays or graphics" then "**The game clock in the film is your index**" | If the coaches film has no graphics, where is the game clock? A beginner reads this as a contradiction. Say where the clock actually appears (the NFL+ play list / the stadium clock in shot / the pbp `time`), or drop "in the film". |
| p. 11, Fig 4 | columns `l2`, `l2c`, `succ`, `hash`, `dn&to` | Caption says "Abbreviations are in the codebook below", but Table 1 has none of these. `l2`/`l2c` are especially opaque (15-01 called it `l2conf`, so the name also drifted). |
| p. 11 Fig 4 vs p. 21 code | `l2 = "1-hi", l2c = .55` (confidence in the *call*) vs `l2conf = "the stated chance of two-high"` | Two different conventions for the same column in the same chapter. The "it doesn't matter which way round" sentence (p. 16) is about the first layer and comes later; say it explicitly for `l2c`. |
| p. 17 | "the reader beat **the scorebug**" | "The scorebug" as a nickname for xpass is never introduced. I had to infer "xpass only knows what's on the scorebug". Add that gloss the first time (the table row "xpass" is the natural place). |
| p. 14, Fig 5 caption | "a successful play (one that gained enough of the yards needed, by nflverse's EPA-based definition)" | 13-02 taught success = positive EPA. "Gained enough of the yards needed" is the *other* (40/60/100%) definition. The caption mixes both; footnote 8 then says EPA > 0. Pick EPA > 0. |
| p. 6 | "explosive play (a run of 10 yards or more, a pass of 20 or more)" | 13-02 said staffs often use 12/16 and analysts 10/20. Fine to choose 10/20, but say "the analysts' version" and link 13-02's term. |
| p. 20, score_log output / p. 19 | `clue` values `align` / `sit` | 15-01's clue column was "the clue that decided it" (free text). Here it's suddenly two codes. The meaning of `align` is only half-explained on p. 20 ("the fair test of a clue..."); say up front "align = the formation clue moved the call off the situation; sit = the situation alone". |
| p. 17–18 | **Brier skill score**, **proper**, **resolution**, **overconfidence** are bolded | Bolded like key terms but not in the glossary front matter (only the four owned terms are). Either add them as aliases/sub-entries or un-bold. "Resolution" in particular is a learning objective. |
| p. 8 Fig 2 | two defenders both labelled **B** (Hall on the left, the right-side rusher) | I couldn't tell at first which B was Hall; the ring rescues it, but the duplicate label is a trap. Same in Fig 3. |
| p. 24 Fig 10 | defense has **S** and **SS**; offense **T** (tailback) next to defensive **T**s (tackles) | Caption covers T; nothing says S = Sam linebacker. A beginner reads S and SS as two safeties and then the box count "8" stops adding up. |
| p. 22 | "Coach of the Year Clinics (long Nike-branded)" | Cryptic aside; either explain ("they ran as the Nike Coach of the Year Clinics for decades") or cut. |

## 2. Leaps (a missing or assumed "why")

1. **The 2.5 s / 3.5 s rule vs the 3.3 s sack (p. 5 vs p. 9).** Pass 1 says under 2.5 s = protection lost; still holding at 3.5 s = something else failed first. The worked example's sack lands at **3.3 s**, in the gap the rule doesn't cover, and the text just calls it "late". Tell me what to conclude in the 2.5–3.5 window (it's the shared zone where you need pass 2 and pass 4 to decide), since that's exactly where the example sits.
2. **"Two deep, five in man" (Fig 2 panel 2 title) vs "the four man defenders ... and the middle linebacker sitting in the short middle" (Fig 3 caption, p. 9 text).** The text's story is that M was freed because the back stayed in. The panel title says five in man. Fix the title ("four in man, M free") or the text; as is, the count contradicts the lesson.
3. **"Brier by quarter of the season" is printed and never discussed (p. 20).** The numbers (games 1–4: 0.177; 5–8: 0.201; 9–13: 0.189; 14–18: 0.178) say the reader's *best* stretch was his *most overconfident* one, which cuts against "starts overconfident and settles down". Fig 8's caption ("the first two were [easy]") and the Go-deeper box explain it, but only if you connect them yourself. One sentence after the output would do it: "The score barely moved, because the early games were easy ones; the calibration plot, not the raw score, shows the improvement."
4. **Report card vs Drill 3 (p. 20 vs p. 27).** The report-card row "All calls between 50% and 65% → Hedging; low resolution → use the formation step" would misdiagnose Reader B, whose calls are mostly 50–65% but who *has* resolution (his dots climb steeply) and is underconfident. Make the row conditional: "...and the dots are flat" = low resolution; "...and the dots sit above the line" = underconfident.
5. **"Brier worse than the base rate → your clues are pointing the wrong way" (p. 20).** Heavy overconfidence alone can push you below the base rate with perfectly good clues (Reader A is close). Add "or you're badly overconfident: check the calibration plot first".
6. **"Situation + formation model ... the honest ceiling" (p. 17).** Ceiling only for a reader using those two clues; the course has taught many more (box, shell, tells). Say "the bar for those two clues", or a beginner concludes 0.175 is the best possible.
7. **The second-layer result (p. 21): "Brier 0.221"** with no baseline. Is 0.221 good? Give the same comparison the first layer got (always-50% = 0.25; always-say-73% would have scored ~0.20). Also "far too timid" is the wrong word: a 53% average stated chance against a 73% outcome is *mis-aimed* for this game, not timid.
8. **Pressure 28% (p. 15 table)** has no comparison ("—"). Is 28% a lot? Give the league 2025 rate so "the four-man rush still got home" has evidence.
9. **The skeleton says "67 snaps" (p. 13); the board/table says "80% of 66" (p. 15).** Explain the extra row (presumably a two-point try: the skeleton doesn't filter `down.notna()`, but footnote 8 says two-point tries are off the board). A beginner who runs the code will notice.
10. **Drill 2 answer vs Fig 10 (p. 24/27).** The answer says the fullback "kicks out the defender on the end of the line on the right" after the TE blocks down. In the figure the right-side E is *inside* the TE (x≈522 vs Y at 530), and the next defender outside is S at linebacker depth. When I tried to trace "who blocks whom", I couldn't find the kick-out man. Either move E outside Y (a 9-technique) or say the kick-out is on the Sam.

## 3. Diagrams

- **Fig 1 (protocol card, p. 4):** clear, and I could use it as a checklist. Fine.
- **Fig 2 (strip-sack strip, p. 8):** readable; duplicate B labels (above); panel 2 title count (above). The snap panel shows Y *already* across the formation with his motion trail, which works, but the panel title "Y's defender went with him" would be clearer as "Y motioned left; D went with him".
- **Fig 3 (four passes, p. 9):** the fading idea is excellent and the best diagram in the chapter. One problem: the **Pass 4** panel's label says "a defender on every route", but the defenders are faded so heavily I couldn't verify the attachment it claims. Keep the four man defenders at half strength in that panel.
- **Fig 4 (charting sheet, p. 11):** undecodable columns (`l2`, `l2c`, `succ`, `hash`). The caption names grey, blue, orange, green and cream but not the lavender "after the snap" header, and the defense header reads pink/salmon in print, not orange.
- **Fig 5 (game board, p. 14):** excellent once you read the caption; the "4·C2" code is explained. The success definition in the caption is muddled (§1).
- **Fig 6 (proper scoring, p. 17):** clear. The text below says "stating 90% when the truth is 95% costs very little, while stating 99% when the truth is 85% costs a lot", but there is no 95% or 85% curve to look at. Use the drawn curves (e.g. "say 100% when the truth is 75%").
- **Fig 7 (calibration, p. 18):** clear and well captioned.
- **Fig 8 (season, p. 21):** "down-and-distance rule" and "always pass" lines sit on top of each other (60% vs 59%), so you see one line with two labels. Say so in the caption ("the two bars nearly coincide").
- **Fig 9 (Drill 1):** good. The boundary safety is labelled FS and the field safety SS. A beginner who learned "the strong safety comes down" may be thrown; consider generic "S" labels or one sentence.
- **Fig 10 (Drill 2):** S/SS ambiguity; kick-out target unclear (§2.10).
- **Fig 11 (Drill 3):** clear.

## 4. Drag / repetition

- The **angle table (pp. 2–3)** repeats the angle column of the Fig 1 card one page later. Cut the table or the card's angle column.
- Each pass ends with a "Why first/second/third/last" paragraph, and then **"Why this order, and why not more passes" (p. 6)** says it all again. Keep one.
- **Three framing pieces before the protocol** ("What Sunday can't tell you", the gorilla box, the Madden box), all making roughly the "you can't see it all live" point. The gorilla box earns its place; the Madden box mostly repeats the "inference" point made again in Pass 3.
- "Film-study protocol" is defined twice in a row (the glossary-style sentence on p. 3 and the Fig 1 caption).
- Answer 3: "Their hit rates are almost identical (75% and 75%)", which is redundant.
- The skeleton output prints `down 1.0`, `togo 10.0`, `success 1.0` as floats. Cast to int so it looks like a chart.

## 5. Can I do the "You'll be able to…" items?

1. **Get All-22, set up, run the protocol: mostly yes.** I can run the protocol (the worked example is excellent). I can't really "get" the film: no price, no word on which devices and players support frame-stepping, and the sentence about the package ("which offered it for the 2026 season and, when the league described the package in 2024, kept an archive back to the 2022 season") is hard to parse. I also can't *time* anything: the chapter asks me to count 2.5 s vs 3.5 s but never says how (count frames? stopwatch? the film player's timer?).
2. **Chart a game with template and codebook: yes for the template, no for "turn the finished chart into tendencies".** The chapter reads the *public* chart into a table (p. 14–15) but never shows a `groupby` over my own film columns (e.g. coverage by personnel, run direction by strength). That's the payoff of charting and it's missing. There is also no downloadable blank template or CSV, only a picture of one.
3. **Score a log in Python: partly.** `score_log` is great and I could run it on my own CSV. But (a) `prediction_log_2025.csv` isn't offered, so I can't reproduce the example; (b) **no calibration-plot code is shown** in print (only a table), and the objective says "and a calibration plot"; (c) the second-layer code uses hidden objects (`SB`, `cv`, `TWO_HIGH`, `ONE_HIGH`, `sea_two_rate`, `qb_dropback`) and **never joins a log to a chart**, though the text says "Join the log to the chart on the snap". A 6-line `merge(on="play_id")` example on the skeleton would fix it.
4. **Calibration vs resolution: yes.** It's clear in the prose and the Murphy box. Drill 3 tested it well.
5. **Where to keep learning: yes.**

**Drills (attempted before opening answers):**

- **Drill 1:** I said "rotation to single-high, Cover 3, about 60%, watch the field safety's first step", using 15-01's "shallower, pinched safety = rotator" tell. That matches the answer. Good drill, fairly answerable from 15-01 + 06-06.
- **Drill 2:** I said "gap/power to the right, left guard pulls, backside (left) end unblocked, run ~75%". That matches. But I couldn't fill in the *pass 1 picture* (who kicks out whom) from the diagram (§2.10).
- **Drill 3:** I got the diagnoses (A overconfident, B underconfident). On "which has the better Brier" I could only guess B, because the chapter never gives me a way to estimate a Brier score from a calibration plot. A one-line tool would make this solvable rather than a guess: expected Brier for a group = hit·(1−c)² + (1−hit)·c². With it, A's huge 96%-stated/81%-true bin works out to ≈0.18 per call and the whole comparison comes out ≈0.195 vs ≈0.189. Put that back-of-envelope in the answer.

## 6. What I still wonder (should the chapter answer it?)

- **How do I time a snap on film?** (frame counting at 30/60 fps, or a stopwatch app). Needed for pass 1 and the strip-sack's 3.3 s.
- **How do I identify players on All-22?** Jersey numbers are tiny in the wide shot; do I need a roster/depth chart open?
- **No-huddle/tempo:** how do I log the live call when there are 12 seconds between snaps?
- **Hindsight bias in step 0:** how do I keep "I knew it was two-high" honest once I've seen the snap? (The rule "don't overwrite the log" helps, but the notes column is still post-hoc.)
- **Without NFL+:** which chart columns can I realistically fill from the broadcast alone? A one-line "broadcast-only chart" subset would help the many readers who won't pay.
- **How many calls before I trust my calibration plot?** The text says a season, and roughly 30 per group; a rule of thumb ("about 300 calls, 50+ in each confidence group") would be concrete.
- **What does a good human Brier score look like?** The Panthers table gives 0.186; is that typical for a strong fan? Is it a target?
- **Second layer over a season:** an example calibration plot for coverage calls, or at least the expected shape ("flatter") drawn once.
- **Where's the template?** A downloadable blank sheet (CSV with the codebook as a header row) would turn the Watch-for-it drill from aspiration into action.

---

## Revision (2026-10-08)

Addresses this review and the coach review (`15-02-coach.md`). Rebuilt with
`build_pdfs.py 15-02-film-study-and-charting --html` (OK, zero errors, 31 pages) and every figure page re-checked at
60 and 110 dpi. Footnotes: still 16, each referenced once; no fact-checked claim was changed.

### Beginner review

| Finding | Action |
|---|---|
| §1 "no graphics" vs "the game clock in the film" | "You'll need" now says no scorebug or clock; new "Keeping the three lined up" paragraph: the play-by-play is the index (qtr, time, down, ydstogo, yrdln), matched to the film by snap order, down and distance and the yard line. |
| §1 Fig 4 columns `l2`, `l2c`, `succ`, `hash`, `dn&to` undecoded | Codebook now has a row for every sheet column (qtr clock, dn&to, ball on, hash, yds, succ, call/conf, l2/l2conf); caption says "every column is decoded in the codebook". |
| §1 `l2c` vs `l2conf`, two conventions | One convention everywhere, matching 15-01: `l2` is the call, `l2conf` the confidence *in that call*. The sheet column is renamed `l2conf`; the second-layer code now uses the same call + confidence form and scores it like the first layer. |
| §1 "the scorebug" nickname | Glossed at first use ("xpass knows only what the scorebug shows") and in the baseline table row. |
| §1 Fig 5 success definition mixed | Caption now says positive EPA only. |
| §1 explosive 10/20 | Now "the analysts' version from 13-02 … staffs vary, many count runs of 12+ and passes of 16+", with a link. |
| §1 `clue` codes `align`/`sit` | Defined up front when the example log is introduced, with a note that 15-01's free-text clue is coded so it can be counted. |
| §1 bolded terms not in glossary | Added glossary entries for Brier skill score, Proper scoring rule and Resolution (none is owned elsewhere in the term index), linked at first use; "overconfidence" un-bolded. |
| §1 two "B"s in Figs 2–3 | Hall is now lettered **58** (his number); the other edge keeps B. Captions updated. |
| §1 Fig 10 S vs SS, T vs T | Caption names S = Sam linebacker, SS = strong safety, and says the tailback is the offense's T. |
| §1 "long Nike-branded" | Now "(for years sponsored by Nike, so older notes call them the Nike Coach of the Year Clinics)". |
| §2.1 3.3 s sits in the 2.5–3.5 gap | Pass 1 now names the "shared ground" between 2.5 and 3.5 s and says passes 2–4 decide the split; the worked example says the sack lands there. |
| §2.2 "five in man" vs the text | Panel title now "two deep, four in man, M free". |
| §2.3 Brier by quarter never discussed | New paragraph after the scoring output, with the four values computed inline, explaining why the overconfident first stretch scored well (readable early games) and that the calibration plot, not the raw score, shows improvement. |
| §2.4 report-card row misdiagnoses Reader B | Split into two rows: flat dots = low resolution; steep dots above the line = underconfident with good resolution. |
| §2.5 worse than base rate | Row now reads "badly overconfident, or clues pointing the wrong way: check the calibration plot first". |
| §2.6 "honest ceiling" | Now "the bar for a reader who uses only those two clues", with a note that the box, shell and tells can take a reader past it. |
| §2.7 second-layer 0.221 with no baseline; "timid" | Printout now gives always-50% (0.250) and the hindsight bar of knowing the game's two-high rate (0.199); text says the calls were "aimed at the wrong number for this game", not timid. |
| §2.8 pressure 28% with no comparison | Table row now has Seattle's 2025 rate (34%) and the league's (30%), same `was_pressure` definition. This changed the story: the paragraph now says the rush did *not* pressure more often than usual; it finished (6 sacks). |
| §2.9 67 vs 66 snaps | Skeleton now filters `down.notna()` (drops the two-point try) and prints 66; comment says why. |
| §2.10 Drill 2 kick-out target | Sam moved onto the line outside the TE (9-technique), so "the last man on the line" is literal; answer rewritten (see coach A4). |
| §3 Fig 2 snap panel title | Now "Y motioned left; D went with him". |
| §3 Fig 3 pass 4 defenders invisible | `wash()` gained a `half=` option; the four man defenders are drawn at half strength in pass 4. |
| §3 Fig 4 colours | Caption names the blue, peach and lavender blocks correctly (the defence tint is peach, not orange). |
| §3 Fig 6 text cites curves that aren't drawn | Rewritten on the drawn 75% curve: 80% costs 0.0025 a call, 100% costs 0.0625 (25×). |
| §3 Fig 8 (now Fig 9) lines coincide | Caption says the two bars nearly coincide. |
| §3 Fig 9 (now Fig 10) FS/SS labels | Both safeties lettered S, and the caption says why. |
| §4 angle table repeats the card | Table cut; one paragraph before the card says which angle serves which pass and why. |
| §4 "Why this order" repeats the per-pass whys | Cut to "Why four passes, and not more" (one paragraph). |
| §4 three framing pieces | Madden box cut; its one unique point (you never see the call sheet; a corner who ran with a receiver may be in man or beaten) moved into Pass 3. |
| §4 protocol defined twice | Fig 1 caption shortened to what the card adds (angle and why-here columns). |
| §4 "75% and 75%" | Now "Both were right on about 75% of calls". |
| §4 skeleton floats | down, togo, yds, success cast to int. |
| §5.1 price, frame-stepping, package sentence, timing | Package sentence rewritten; "packages and prices change, check before you pay" (no verified 2026 price, so none given); frame-stepping tip; new "Timing a snap" paragraph (stopwatch, or frames at 30/60 fps). |
| §5.2 chart → tendencies never shown; no template | New "From rows to tendencies" section with a shown `tendency()` function run on the Super Bowl chart (shell played and rushers by down), plus the film-column questions it answers; the skeleton is now called out as the blank template (`to_csv`), with a `notes` column added. |
| §5.3 no log file, no calibration-plot code, hidden objects, no join | Text says where the example log is built and how to write it; new shown `calibration_plot()` cell with its own figure; second-layer code rewritten to be self-contained (scouting card as literals, asserted against the data in a hidden cell) and to join log to chart on quarter and clock. |
| Drill 3 not solvable | New "A Brier score you can read off the plot" paragraph (h(1−c)² + (1−h)c², worked) in the calibration section; the answer applies it to A's 90%+ group and B's 50–65% group with computed numbers. |
| §6 wonders | Answered: timing a snap; identifying players (rosters, alignment first, end-zone angle); no-huddle (leave the call blank, never fill it in after); hindsight in step 0 (test: was it visible at the snap?; notes column marked as after the fact); broadcast-only chart (new "TV?" column in the codebook); how many calls (≈50 per group, ±12 points; ≈300 calls); what a good Brier looks like (no published fan benchmark; the bars are the baselines on your own snaps). **Declined:** a second-layer season calibration figure (we have no season of second-layer calls, real or defensibly simulated; the text now describes the expected shape instead); a downloadable CSV hosted with the book (publishing pipeline unchanged; the skeleton code writes the template). |

### Coach review

| Finding | Action |
|---|---|
| A1 RB parked beside Hall, LT quits | Protection rebuilt: C + LG double the DT, RG and RT one-on-one, the back checks the A gap and stays to help inside, the LT rides Hall in a vertical set to ~5 yd depth; Hall arcs past the launch point and comes back under as the QB climbs (arrives at 3.3 s). Pass 1 text now asks "where did the spares go?". |
| A2 man defenders drawn on top of receivers | New `TrailPlay` subclass in the chapter (gridiron untouched): man defenders settle 1 yd behind and 1.1 yd inside their receivers within ~1 s (trail technique). Receivers and defenders are both readable in every panel. |
| A3 two "B" labels | Hall lettered 58. |
| A4 power answer vs drawn front; 8th man | Sam walked onto the line (9-tech) so the kick-out target is the end man on the line; answer now: C blocks back on the 1-tech, RG/RT deuce the 3-tech to the backside LB, TE down on the 7-tech, FB kicks out the Sam, LG pulls for the Mike; two free defenders, the backside end by design and the walked-down SS by arithmetic, with the play-action/crack answer and a second "because" line. |
| B1 field safety at the C2 landmark; tells; corner wording; robber | Field safety moved to 14 yd just outside the far hash; answer adds the "nobody over the boundary slot" tell, the field safety's width as the counter-argument, the corrected corner wording ("off, outside leverage, eyes inside … bail to a deep third"), and the Cover 1 robber reading of the pinched safety. |
| B2 Y's route converges with H's | Y now runs a true flat (2 yd) under H's out at the sticks (7 yd): a high-low on the left, Z's dig as the backside; Pass 4 text describes it. |
| B3 X's split; FS width | X on the numbers (w = −18.5), lateral widened to (−24, 21); FS deep-half landmark (19, −14). |
| B4 Mike vs a mobile QB | Pass 3 text: the Mike's hug-or-sit choice, the low hole watching Maye, 2-Man's scramble weakness and rush-lane integrity; one sentence added to the misconception callout. |
| B5 motion: travel is a vote; motion path through OL | Step 0 text adds "a vote, not a verdict … a bump says zone or match" (linked to 12-08 for Seattle's match/disguise). Y's motion now runs 3 yd behind the line (well behind the linemen) and settles on the wing; D travels at 2.8 yd depth, clear of the DL and Mike. |
| B6 line tells: RPO, play-action, duo, IZ backside | Pass 1 adds high hats/low hats, the 1-yard ineligible rule on play-action, the RPO exception, duo (straight-ahead doubles, no puller), and the inside-zone backside end. |
| B7 safety first-step heuristic | Rewritten: pedal and widen = half; flat-footed reading the slot = quarter (comes down on runs); toward the middle = single high. |
| C `rot` mixes direction and timing | `rot` is now B/F with a `*` late flag (`B*`); Drill 1 answer uses it. |
| C `concept` codes; scrambles | Added TRAP, TOSS, ZR, QB; the `play` rule says scrambles are dropbacks and designed QB runs are runs; the skeleton's `play` now uses `qb_dropback`. |
| C `box` definition | Codebook now uses 02-05's definition (just outside the end men, about 5–7 yd deep), counted at the snap after motion, linked to box count. (Not adopted: the "FTN/NGS ~7–8 yd" figure, which I couldn't source.) |
| C explosives "(staffs vary)" | Done (see beginner §1). |
| C shotgun drop steps | "a three- or five-step drop from the shotgun (roughly the timing of a five- or seven-step drop from under center)". |
| C full-speed look first | Added to the protocol intro, the card's step 0, and Step 0's text. |
| C Predict 2 LG depth | Caption: "in reality a matter of inches, and he must still be on the line". |
| C the defense's call as a "because" | Six candidates now: the offense's call and the defense's call (sim pressure example, linked to 07-03); the card's ✓ row says "either side's call". |
| C special teams | One line: coaches chart the kicking game too; this chapter sticks to snaps from scrimmage. |

New factual content and its sources: league and Seattle 2025 pressure rates (nflverse participation `was_pressure`, course calculation, stated in the table caption); Seattle's 2025 two-high rates by down for the scouting card (computed from the same data as the fact-checked season rate, asserted in a hidden cell); the 1-yard ineligible-downfield rule (taught in 11-03). No new historical or attributional claims.
