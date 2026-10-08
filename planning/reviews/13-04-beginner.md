# Beginner review: 13-04 Tendencies: PROE, Personnel, Motion, and Coverage from Charting Data

Reviewer persona: casual NFL watcher who never played, comfortable in Python, who has read everything
before 13-04 in curriculum order (Parts 1-12, 13-01 to 13-03). Read the rendered PDF
(`pdfs/13-04-tendencies-proe-and-charting.pdf`, 38 pages, built 2026-10-08 08:21) start to finish,
with the source open for line numbers. Drills attempted before opening the answers.

**Overall:** strong chapter. The Jets/Rams opening is a great hook, the filter-then-model progression
lands, and the source-break section and caveat list are the most useful "how not to fool yourself"
pages in Part 13. The problems are concentrated in four places: (a) the "PROE belongs to the coach"
argument contradicts what 08-03 taught with the same Petzing example; (b) the scouting card has
internal inconsistencies a careful reader will catch; (c) Drill 2's answer reasons past its own
numbers; (d) about eight pages of matplotlib plumbing printed in full.

---

## 1. Terms used before they're explained, or never explained

| Where | Quote | Problem |
|---|---|---|
| Coverage table (p.23), Fig 9 legend and caption (l.1005) | "Cover 9" … "Blues are single-high zone (Cover 3 and Cover 9)" | Cover 9 is the one coverage label not linked, and 06-01 taught it as a *dialect* term ("often Cover 3 match or a split-field call, depending on the team"). Here it is filed as single-high without saying what FTN means by it. One sentence and a link to `#gl-cover-9` would fix it. Cover 0, 2-Man, Cover 2 and Cover 6 are also used unlinked in this section while Cover 1/3/quarters get links. |
| Dashboard and card, "League" row | "PROE … League **−1.5**" | Never explained. I expected the league-average PROE to be 0 by construction. Why is the average team −1.5? (League drift toward the run in 2025 versus a model trained on earlier seasons? The neutral filter?) An analytically minded reader will stop here. |
| Card, "Defense in four numbers" | "5+ rushers … league 27%" | `rush5` appears on the card but is never discussed. Caveat 1 contrasts `n_blitzers` with `number_of_pass_rushers` only in passing, so I can't interpret "25% 1+ blitzer, 19% 5+ rushers" together. |
| neutral-defs table (l.309) | "Rank correlation with the course's" | Rank (Spearman) correlation isn't named or glossed. It's fine for this reader, but one clause would help. |
| "Why it exists" (l.492) | "a Vegas-adjusted win probability" | The betting line hasn't been tied to win probability anywhere I remember; worth a half-clause. |
| xpass features (l.358) | "once in a straight line and once raised to the fourth power … `np.abs(sd) * gone**4`" | The `abs(sd)` term (blowout in either direction) isn't explained by the prose. |
| Drill 3 prompt (l.1535) | "What does the run add to the team's `pass_oe`?" | `pass_oe` is per snap. "Add to the team's" muddles that: it should be "what is this snap's `pass_oe`?" |

Terms checked and fine (taught earlier or defined here): neutral situation, xpass, PROE, AUC,
log loss, logistic regression, knots, standard error, two-high, mug, A gap, Shanahan tree, simulated
pressure, pattern matching, tendency breaker, self-scout.

## 2. Leaps: a missing or assumed "why"

1. **PROE "belongs to the coach" contradicts 08-03 (l.778-789).** The text says "Across seasons,
   PROE belongs to the coach", then cites 08-03's Petzing example: "whose Arizona offenses went
   from among the most run-leaning in 2023 to among the most pass-leaning by 2025, under the same
   play-caller." That example shows that the *same* play-caller produced opposite PROEs. 08-03 drew
   exactly that lesson ("The season averages followed Arizona's roster and its quarterback
   situation, not Petzing's character"). Then the next sentence here says "A new play-caller resets
   the prior almost completely." As a reader I'm left holding two opposite rules. The Eagles film
   room makes it worse ("PROE moved by about thirteen points in one year with the same head coach
   and quarterback"). This needs reconciling: PROE persists when coach **and roster** persist;
   either one changing resets it. The heading claim should be softened to fit.
2. **"Steadiest numbers in football" vs r = 0.44 (l.711-713, Fig 6).** A year-over-year correlation
   of 0.44 with the same head coach is moderate, not "one of the steadiest". The text never gives
   EPA's year-over-year correlation for comparison, although the code computes it
   (`R_YOY[...][1]`). Print it. Then "steadier than efficiency" is shown, not just asserted.
3. **"Mostly measures the scoreboard" vs r = −0.45 (l.254-260, takeaway 1).** A team-level r of −0.45
   means win probability explains about 20% of the variance in raw pass rate across teams. "Most of
   a raw pass rate is decided before the play-caller opens his call sheet" may be true *per snap*
   (down and distance), but the chart shown doesn't demonstrate "mostly". Either reword it or show
   the snap-level share.
4. **Drill 2 answer reasons past its numbers (l.1522-1525).** The printed result is "Vikings 43% man
   of 56 snaps (±7%); league 49%". So on third-and-medium the Vikings played man about as often as
   the league (within one SE), and far more often than their season 18%. The answer still concludes
   "probably zone behind it … don't count on beating a man-to-man defender". At 43% ± 7 I *should*
   be ready for man. The honest lesson is "on third-and-medium the Vikings look ordinary, coverage
   and pressure both", and that is the twist the blitz numbers already make.
5. **Drill 2 ignores Cover 0.** The Film room just told me about Flores's "two-high-to-Cover-0
   range", and the drill shows a two-high shell with a double-A-gap mug. My first instinct was Cover
   0. The answer never mentions it or gives the Vikings' Cover 0 share on these downs.
6. **Drill 3: "one snap like this moves an average more than ten neutral snaps do" (l.1574).** Why?
   Its `pass_oe` is about −84, and a typical neutral snap swings ±48. I can't reconstruct "ten". Next
   sentence: "Keep it, and a trailing team's coach looks more run-minded than he is." If he really ran
   while down 10, isn't that run-minded? The argument for exclusion (situations where xpass is
   untrustworthy and the choice isn't free) is good but gets muddied here.
7. **Why the per-snap SD is about 48 (l.623-629).** One clause would do it: a 0/1 outcome whose
   probability is near one half has an SD near 0.5.
8. **Where the Vikings' "dashboard row" is (l.1040-1041).** "the dashboard row behind it is stranger
   than the bar". There is no defensive dashboard; Fig 7 is offense only. I went looking for it. Either
   add a small defensive dashboard (man, two-high, blitz, 5+ rushers for 32 teams, since the code
   already computes `DEF25`) or reword.
9. **"Some of the best offenses sit left of zero" (Fig 5 caption).** Which ones? Name BUF/DET/BAL
   in the text so I can find them.

## 3. Diagrams

- **Fig 11, scouting card (p.31), the most important figure, has several decode problems:**
  - Header says "Offense: neutral 1st & 2nd downs … 467 snaps", but panel A includes "3rd & 1-3 (46)"
    and "3rd & 4+ (61)", and the counts match Fig 4's *all-downs* neutral numbers (Leading 122 + Tied
    199 + Trailing 270 = 591, not 467). The header and panel A disagree.
  - Personnel panel: rows "21: 0% of snaps" and "22: 0% of snaps" are empty, wasted space. For 12 and
    13 the blue team dot sits on top of the grey league tick, so I can't see the league value the
    text then quotes ("47% against 46%").
  - Coverage bars have no legend on the card. Only slices of 12% or more are labelled, so the
    light-blue/green slices (Cover 9, quarters, Cover 6) are unreadable on a card meant to stand alone.
    The faded "League" bars also read as different colours. "Cover 3" text is split by a slice
    divider ("Cove|r 3").
  - "Biggest tells" 1 and 2 are the same tell twice (under center 72%; throws from under center 46%),
    and all three are offense. Suggest dropping correlated tells or picking one per family.
  - Panel A x-label "points over expected (snaps)" is cryptic.
- **Fig 8, rotation strip (p.22).** The FS-to-middle and SS-down story reads. But by +1.2s and +2.1s
  the four rushers are *behind* the offensive line, sitting on the quarterback and ball. It looks like
  a sack, and the blockers appear to have vanished. The X/Z go routes and the bailing corners end at
  the top edge of the window (corner "C" touching the edge at +2.1s; convention (c)). The caption
  should say "watch FS and SS between frames 1 and 4". Labelling the three deep-third landmarks in
  the last frame would make "Cover 3" visible rather than asserted.
- **Fig 9 vs Fig 10 colours.** In Fig 9 blue = single-high zone (Cover 3 dark blue) and orange = man
  (Cover 1 orange). In Fig 10 blue = two-high, green = Cover 3, purple = Cover 1, orange = man. The
  two figures are adjacent and I misread Fig 10 on the first pass. Reuse `COV_COLOR` for Cover 3 and
  Cover 1 in Fig 10.
- **Fig 1, snap-as-data.** Clear and genuinely helpful. Small point: the Sam linebacker "S" sits
  right beside "SS", and the arrow "is this safety in the box?" ends between them, so I briefly
  thought the S was the safety in question.
- **Fig 13 (Drill 2).** The highlight rings on W and M crowd the T boxes ("T W M T" reads as one
  clump). **Fig 14 (Drill 3):** the R highlight ring overlaps Q.
- **Fig 12 (Drill 1) caption gives away half the answer:** "For most offenses this look means run
  about two times in three."
- **First table after `proe` (p.11-12).** The header "Pass %, all snaps" wraps badly, and "Rank" is
  ambiguous (rank of what?). Use "Raw pass-rate rank".
- **Fig 7 dashboard (p.20)** works well. It is the best figure in the chapter, and "read by columns,
  then rows" is a great instruction.

## 4. Drag and repetition

- **Printed plumbing.** With `code-fold: false` and `echo: true`, the PDF prints `md_table`, `say`,
  the dashboard's imshow/tick code (all of p.19), and ~150 lines of `stat_tile`/`panel`/`dot_rows`/
  `scouting_card` layout (p.27-30). About six pages are matplotlib layout with no football in them.
  Part 13 shows code by design, but presentation-only cells (`md_table`, `say`, dashboard and card
  layout) should be folded or `echo: false`. Keep `xp_features`, `fit_logistic`, `offense_metrics`,
  `defense_metrics`, `biggest_tells`.
- **Half-empty pages** at p.5, 14, 19, 30, 33 (figure floats after long code cells).
- **"The Rams throw from under center"** appears five times: dashboard bullet, row reading, card walk,
  card tells, Drill 1. By Drill 1 I've been told the answer four times, so it isn't a test. Either cut
  one or two mentions or turn Drill 1 into something not yet stated (e.g. Rams in 13 personnel).
- **The neutral definition** is restated in body, Fig 4 caption, card header, Watch for it and
  takeaways. That's acceptable, but the card header version contradicts panel A (above).

## 5. Can I do the "You'll be able to…" items?

1. *Raw pass rate measures the score; pick neutral situations.* **Yes.**
2. *Explain xpass/PROE, fit a model, compute by team/season/situation.* **Yes**, although the
   score-by-clock feature design is a bit "trust me".
3. *Measure offensive tendencies; read a dashboard.* **Yes.** Formation beyond QB alignment is not
   measured, which the card section admits.
4. *Measure coverage tendencies; say what labels can/cannot tell.* **Mostly.** Cover 9 is unclear,
   and there is no defensive equivalent of the dashboard.
5. *State charting caveats.* **Yes.** This is the chapter's strongest section.
6. *Build a card and grade it live.* **Build: yes** (one function call). **Grade: only partly.** No
   code or worked example scores a card against the two baselines. "Call the coverage after the snap"
   on a broadcast assumes I can see the safeties, and the TV angle usually can't show them.

**Drills (attempted before opening the answers):**

- **Drill 1 (Rams 11/under center).** My answer: league ≈ run two times in three (the caption told
  me); Rams ≈ coin flip from the dashboard's "Pass from UC 46%", and if it's a pass, play-action.
  **Correct** (actual 54% pass on 151; 79% PA). Too easy, because the text had already given the
  answer.
- **Drill 2 (Vikings, 3rd & 6, two-high plus double mug).** My answer: blitz likely (season 51%,
  most in the league), zone behind it (18% man), with Cover 0 also possible given 06-06. **Wrong on
  the blitz.** On third-and-4 to 8 they blitzed 39%, the same as the league, and the chapter never
  showed the situational split before the drill. That's a fair "split your card" lesson, but the
  answer then over-claims zone (see leap 4).
- **Drill 3 (down 10, 6:10 left, run).** From Fig 3's left panel I estimated xpass ≈ 0.65-0.7 on the
  chapter's model, so `pass_oe` ≈ −65 to −70. I guessed it falls out of the neutral filter but
  couldn't verify that WP < 20%: nothing in the chapter lets me estimate WP for down 10 with 6 min
  left. **Mostly correct** (our model 0.67; nflverse 0.84; WP 11%, excluded). Suggest the prompt
  give the WP, or point to 13-03's rule of thumb.

## 6. Knowledge gaps: what I still wonder

- Why is league PROE −1.5 and not 0, and is there a league-wide PROE trend over 2016-2025? That is the
  "is the NFL running more?" question, and it's the obvious next chart.
- What is EPA's year-over-year correlation, for comparison with PROE's 0.44/0.16?
- How do I call man vs zone live from a broadcast angle that hides the deep safeties? Point me to a
  specific tell from Part 6, or concede that it's an All-22 task and refer to 15-02.
- For a 2026 opponent mid-season, defensive coverage labels don't exist yet. How much does a team's
  coverage mix carry over year to year (same DC vs new DC)? Run the same stability test as Fig 6 on
  man share or two-high share.
- The box count (Fig 1's judgement call) and defensive personnel are introduced and then never used.
  Does a team's light-box rate or nickel-vs-base rate belong on the card?
- FTN's RPO and screen flags are listed in the data table and then never used. RPO rate seems like an
  obvious tendency column.
- How do opponents exploit a known PROE? Does facing a high-PROE team change the defense's
  personnel? This is the "so what" for a defensive coordinator.
- Grading: what hit rate does the alignment rule actually get on neutral early downs (the "two snaps
  in three" from 08-02)? Print that number so I know the bar to beat.

---

## Revision (2026-10-08)

Addresses this review and `13-04-coach.md`. Rebuilt with `build_pdfs.py 13-04-tendencies-proe-and-charting --html`:
OK, 41 pages, zero errors, every hidden assert passes. Every diagram page was rasterized and checked
(Figs 1, 4, 5, 8, 12, 13-15 also at 100-150 dpi). New numbers are the chapter's own nflverse
calculations, each guarded by an assert. The fact-check's verified claims are unchanged. The model
table is identical (0.562 / 0.769), because the dropped feature was redundant.

### Beginner review

| Finding | Action |
|---|---|
| §1 Cover 9 (and Cover 0, 2-Man, Cover 2, Cover 6) unlinked/undefined | New paragraph before the coverage table links all of them, explains Cover 9 as 06-01's dialect term, notes FTN tags every COVER_9 snap as zone (asserted), and says it is shaded single-high but kept out of the two-high share, as in 06-06. The Fig 9 caption says the same. |
| §1 League PROE −1.5, not 0 | New `league-proe` cell and paragraph. nflverse's xpass slightly over-expects passing on neutral early downs every season (53% vs 52%). League PROE ranges from −2.4 to +0.3 over 2016-25, so read a team against the league line. It also answers "is the NFL running more?": the neutral pass rate was flat at 50-53%, while 2025 heavy personnel (18→24%) and under-center snaps (38→44%) rose. |
| §1 `rush5` never discussed | New paragraph before the new defensive dashboard explains blitzers vs rushers: 5+ rush, simulated pressure (blitzer but four rushers), plain rush. Caveat 1 points to it. The card walk now reads the two pressure tiles together (the Rams' blitzes were sims a third of the time). |
| §1 Rank correlation unglossed | Glossed in a clause (correlation on rank positions, "Spearman's"). |
| §1 Vegas-adjusted WP | Half-clause: a win probability that starts from the pre-game point spread. |
| §1 `abs(sd)` term unexplained | It was an exact linear combination of `sd` and `behind`, so I removed it rather than explain it. The prose now explains the fourth-power term (0.5⁴ ≈ 0.06) and `behind`. |
| §1 Drill 3 "add to the team's pass_oe" | Now "What is this snap's `pass_oe`?" |
| §2.1 "PROE belongs to the coach" contradicts 08-03 | Heading and paragraph rewritten: "PROE carries over when the coach and the roster both stay". Petzing is now cited for 08-03's own conclusion (roster and QB drove it). Takes the Eagles as the mirror case. Working rule: PROE persists when the play-caller **and** key personnel persist; either changing can reset it. Takeaway updated. |
| §2.2 "Steadiest numbers in football" vs r = 0.44 | Claim softened to "steadier than efficiency". EPA's year-over-year r in the same pairs is now printed (0.43), and the text says a correlation of 0.4 is moderate. |
| §2.3 "Mostly measures the scoreboard" vs r = −0.45 | Reworded throughout (objectives, description, misconception, takeaway) to "as much as the play-caller". The text squares r (≈21% of the spread from WP alone, a single number) and adds a concrete measure: the situations alone predicted a pass on 70% of the Jets' snaps (highest) and 56% of the Rams' (lowest). |
| §2.4 Drill 2 answer reasons past its numbers | Rewritten. On 3rd & 4-8 the Vikings were ordinary: blitz 39% = league, man 43% ± 7 vs league 49% (asserted within 1.2 SE), more than twice their season man rate. So "be ready for both", with answers that beat either. |
| §2.5 Drill 2 ignores Cover 0 | The answer gives the Vikings' Cover 0 rate on these downs (7%, 4 of 56) against the league's 6%. |
| §2.6 Drill 3 "ten neutral snaps" / "run-minded" | Removed. There are two reasons now: the choice isn't the early-down style PROE measures (time for two drives; a light-box two-high defense invites the run; xpass can't see the defense), and the two models disagree by 17 points on this one snap. |
| §2.7 Why per-snap SD ≈ 48 | One clause added: a 0/1 outcome near one half has an SD near 0.5, so 50 points ×100. |
| §2.8 Missing defensive "dashboard row" | Added the **defensive dashboard** (Fig 10): man, two-high, Cover 0, 1+ blitzer, 5+ rushers, sim pressure, for all 32 defenses. The film room now points to it, and the Vikings also lead 5+ rushers (46%). |
| §2.9 "Some of the best offenses sit left of zero" | Named in the caption and the text: Green Bay (top neutral EPA, −5.7), Dallas, Buffalo. GB and DAL are labelled, and the BUF/DAL labels no longer collide. |
| §3 Card: header vs panel A | The header now states panel A = all neutral downs and B-D = neutral 1st & 2nd downs (467 snaps). Panels are lettered. |
| §3 Card: empty 21/22 rows; dot hides league tick | Only groups the team used on ≥3% of snaps appear. The league tick is a dark bar drawn above the dot, and both values are printed at the right ("team / lg"). |
| §3 Card: no coverage legend; faded league bars; "Cove\|r 3" | Added a key under the bars. Slices ≥7% carry short codes (C1, C3, Q...), so text never spans a divider. League bars are no longer faded. The x-grid behind the bars is removed. |
| §3 Card: duplicate tells, all offense | `biggest_tells` now takes one tell per family (alignment, personnel, coverage, pressure...) and always at least one defensive tell. Rams: under center 72%; PROE +5.9; rarely rushes more than four. |
| §3 Card: cryptic panel A x-label | "pass rate over expected, percentage points (snaps in brackets)". |
| §3 Fig 8 rushers through an unblocking line; edge; caption | Rebuilt with the 06-03/06-06 `protect()` convention, so the rush engages and stops. The caption says "watch FS and SS between the first and last frames" and names the buzz rotation with a link. The last frame marks the three deep thirds (dashed dividers and labels, inside the window), via a print-only helper. |
| §3 Fig 9 vs Fig 10 colours | The source-break chart now uses the coverage-mix colours: green two-high, dark-blue Cover 3, orange Cover 1, dashed dark orange for all man. |
| §3 Fig 1 Sam "S" beside "SS" | SS sits a little wider and deeper (7.3, 7.4) with a highlight ring. The arrow ends on him, and the caption names S as the Sam linebacker. |
| §3 Fig 13/14 rings crowd T/W/M and Q | Rings removed from Drills 2 and 3. Drill 2 uses a boxed note ("M and W: A-gap mug") clear of the markers. The Drill 3 back is set 2.2 yd off the QB. |
| §3 Fig 12 caption gives away the answer | Drill 1 is new (see §4), and its caption describes only the picture. |
| §3 PROE table header/rank | "Raw pass %", "Raw rank", "Neutral pass %", "PROE (ours)", plus a one-line note on what each uses and "rank 1 = most dropbacks". |
| §4 Printed plumbing | `pct`, `ordinal`, `md_table`, `say`, the new `heat_table`, `show_with_thirds` and the whole card layout (`stat_tile`, `panel`, `dot_rows`, `scouting_card`) now sit in folded cells wrapped in `content-visible when-format="html"`. They still run in both formats, but print shows a one-line note instead of about 6 pages of layout. The dashboard cell went from ~35 lines to 6. `TELLS`/`biggest_tells`, the metrics functions and all football/analysis code stay shown. |
| §4 Half-empty pages | Fewer, since the plumbing is gone. A few remain where a tall figure floats after a code cell (after the Fig 2 and Fig 8 cells, and before the drills). That is Typst float placement. I left it alone and didn't add page-break hacks. |
| §4 "Rams throw from under center" ×5 | The row reading no longer restates it. The card walk gives it one clause ("repeats the dashboard's alarm"). The tells keep only one alignment tell. **Drill 1 is now the shotgun flip side**, which the text points to but never answers: Rams 11-personnel gun 85% pass vs league 70%; all gun 89% of 132. |
| §4 Neutral definition restated | Kept. The card header no longer contradicts panel A. |
| §5.6 Grading: no worked example; broadcast can't show safeties | New `grading` cell. On 2025 neutral early downs the alignment rule (gun = pass; under center or pistol = run) hits 68%, majority guess 54%, team-specific "card rule" 68%. On the Rams the alignment rule falls to 64% and the card rule gains nothing. Lesson: a card changes confidence more than calls, so score probabilities with log loss. Watch-for-it now concedes the sideline camera often hides the safeties, gives a corners'-first-steps tell, and sends the full call to the All-22 (15-02). |
| §6 EPA YoY; league PROE trend; coverage carryover; RPO and screens; box count; alignment hit rate | All added (above, plus a `coverage-carryover` cell: two-high share r = 0.46 and 0.69, man ≈ 0.45 across FTN seasons; no DC split possible). RPO/screen/scramble/QB-run mechanics are in a new subsection (see coach B3). Box count and defensive personnel are named as good first additions in "What the card can't say". |
| §6 How opponents exploit a known PROE | **Partly declined.** Drill 1's answer now says what a defense does with a near-certain pass look. A full "facing a high-PROE team" analysis (opponent personnel response) would need a new section and dataset, so it's left for 08-03 / 15-01. |

### Coach review

| Finding | Action |
|---|---|
| A1 Fig 8 jailbreak rush | Fixed with `protect()` (copied into the chapter, not imported). |
| A2 Uncovered slots (Figs 8, 12, 13, 14) | Fig 8 and Drill 3: Will walked to an apex over H at (5, −6). Drill 2: option (a), safeties at (9.5, ∓8) capping the slots; the caption says so, and the answer says the capped slots let the defense play either way. Drill 1 (now gun trips vs nickel) has no uncovered receiver. Gridiron note below. |
| A2 Fig 13 empty B gaps | DTs at (1.0, ±2.4) as 3-techniques, ends at (1.0, ±5.5). |
| A3 Fig 1 corner stays put; Sam label | The RCB motions in with Z, to (6.5, 10). Sam named in the caption and in the drills legend. The optional `n_defense_box` note was **declined**: FTN's and participation's box counts agree on 99.8% of 2025 snaps (participation is FTN-supplied from 2023), so there is no disagreement to show. |
| A4 Buzz naming; FS depth; RB "flat" | Caption names the buzz rotation with a link. FS ends at 17 yd. RB uses `r.flat(6.0, 5)` and reaches the flat by +2.1 s. |
| A5 Field numbers behind X/Z | Left as is (realistic, per the reviewer). |
| B1 Pistol is a run look | Dashboard has a Pistol column. The alignment bullet gives the league pass rate by alignment (gun 71%, UC 34%, pistol 30%). The baseline is now "shotgun means pass, under center or pistol means run" in the grading text, Watch-for-it and takeaways. Atlanta is described as the pistol team (43%, league high). |
| B2 Rams' shotgun tell | Became Drill 1 (89% of 132 gun snaps; 85% in 11 personnel vs league 70%). The card walk points to it. |
| B3 PROE = play run, not called | New subsection "What PROE counts": RPOs (7.6% of neutral early downs, 77% recorded as runs; KC most; Jets top five), check-with-me and kill calls (glossary links to 01-05), screens (PIT 18% of dropbacks), scrambles, designed QB runs. The misconception box drops its confusing scramble clause. **Declined:** naming Stafford/McVay as the textbook check-at-the-line case, because I had no source in hand. The point is made generally instead. |
| B4 CIN/KC play-action + RPO | Bullet rewritten: true shotgun offenses that use play-action least while ranking among the heaviest RPO users (KC 1st, CIN 4th, asserted). |
| B5 6-OL "heavy" | OL counted from both string formats (`C+G+T` from 2023, the `OL` token before). `heavy` now includes ≥6 OL. Caption and bullet updated. Pittsburgh rises to third (47%, mostly jumbo); asserts updated. |
| B6 Hash is available | Taken out of the "can't" list. The text names `starting_hash` + `run_location` as the route to a field/boundary split. Receiver splits, bunch/nub, concepts and run scheme stay in the list. |
| B7 Drill 3 "use clock" reasoning | Replaced with the reviewer's framing: time for two drives with timeouts; a two-high light box hands over four free yards. |
| B8 Cover 9 | See beginner §1. |
| C "everyone throws inside 2:00 of the first half" | Now "about four snaps in five" (81% in 2016-25, asserted). |

**For the gridiron maintainer (not edited):** `defense("nickel", ...)` against 2x2 leaves the weak #2 uncovered (the Will stays in the box). Apexing the Will to about (5, ∓6) when there are two slots would fix it everywhere. `show_animation` has no hook for annotating the print frame strip, so this chapter has a small `show_with_thirds` wrapper around `frame_strip`.
