# 13-02 beginner-reader review

Reviewer persona: casual NFL watcher who has never played and still half-thinks of a play as a
Madden card, analytically minded (data-science grad), and has read 01-01 through 13-01 in
curriculum order. So I know EP/EPA/success rate only as the 01-02 scorecard, I know pbp,
nflreadpy, yardline_100 and the garbage-time filter from 13-01, and I know dime, empty, I-form,
box/light/loaded box, play-action, CPOE (04-07), pass rush win rate (07-01), "on schedule" and
"2nd & short is a shot down" (10-01). I have **not** read 13-03 (win probability), 13-04 (neutral
situation, PROE) or 13-05 (tracking data, Next Gen Stats, Big Data Bowl).

Sources read: `chapters/13-analytics-and-data/13-02-expected-points-and-success-rate.qmd` (qmd line
numbers below as `L###`) and `pdfs/13-02-expected-points-and-success-rate.pdf` (rendered 07:27,
37 pages, rasterized and viewed; PDF pages as `p##`).

---

## 0. Blocker found while doing the drills

**The drill answers are printed right under each drill in the PDF (p34, p35, p36).** They are not
collapsed and not moved to an "Answers to Predict the play" section; there is no "Answer N is at
the end of the chapter" pointer either. I saw "EP before: +0.06 … EPA -0.44" on the same page as
the question before I could cover it. Cause (checked): the answers are plain
`::: {.callout-note collapse="true" title="Answer"}` blocks (L1412, L1446, L1481), and
`filters/print-answers.lua` evidently does not catch them in this build (no "Answers to Predict"
text anywhere in the PDF). The two pilots whose answers *do* move (01-04, 06-06) emit them from a
per-chapter Python helper; 03-02 uses plain callouts like 13-02 and has the same problem. AUTHORING
§8 also specifies `.callout-tip`, not `.callout-note`. Needs a fix in either the chapter or the
filter before the drills work on paper.

---

## 1. Terms used before they're explained (or never explained)

| Where | Term | Problem |
|---|---|---|
| L99-101 code comment; then "neutral game states" L669, Fig 6 caption L673, "neutral situations" Fig 7/Fig 9 captions, Seattle film room L825, Ravens L853/855 | **neutral situation / neutral game state** | Owned by 13-04, which I haven't read. The prose never says "we call the plays that survive the garbage-time filter *neutral*". The only link between the word and the filter is the variable name `neutral` in code. One sentence at L121-126 would fix it ("we'll call these *neutral situations*; [13-04] formalises it"). |
| L99 code comment "win probability 10-90%", `wp` column | **win probability** | Owned by 13-03. Glossed only at L380-382, ~280 lines after it is used to define every team number in the chapter. The "You'll need" box describes the filter as "plays whose result was no longer in doubt" but doesn't say it's a WP cut. |
| L883 | **Next Gen Stats** | Owned by 13-05; linked but not glossed. I know NGS only as "the old participation source" from 13-01. The sentence "Next Gen Stats predicts how many yards…" assumes I know NGS is the league's tracking-data group that publishes models. |
| L886 | **Big Data Bowl** | Owned by 13-05, no gloss, no link. "The model grew out of the 2020 Big Data Bowl" means nothing to me yet. |
| L229-234, L270 code, L372 | **multinomial logistic regression** is glossed (good); **gradient-boosted trees / XGBoost**, **log loss**, **Adam**, **knots** are not | OK for a DS reader in a code chapter, but the prose at L231-234 calls it "about thirty lines of NumPy" and then the cell uses standardisation, Adam, and spline knots with no prose at all. I could copy it; I could not *explain* it, which is objective 1. |
| L380 | **"down 4"** in "A field goal down 4 with two minutes left" | Fine for a fan, but it reads as "fourth down" on first pass because the whole chapter is about downs. Say "trailing by 4". |
| L392 | **wins-above-replacement** | Unexplained (Go-deeper box, so minor). |
| L437 | **"before the extra point, which is valued separately"** | Never explained anywhere: a touchdown is 6 points, the chapter counts 7, and "valued separately" is never cashed out. Where does the PAT's value go? |
| L857 | **`rush_epa`** | "check the `rush_epa` for BAL in the code below" — there is no `rush_epa` in the code; the variable is `rush` and the printout says "designed-run EPA/play". |
| L1116 | **turnover margin**, **regress** | "candidates to regress" assumes regression to the mean. Fine for me as a stats student, but "turnover margin" is never defined in the course (not in the term index). |
| L1306 | **DAVE** | Introduced in a subordinate clause at the end of the DVOA paragraph; OK, but it's a new metric name dropped with no glossary entry. |
| Tables L820, L1073 | **off_sr / def_sr, raw_off / adj_off / change_off** | Raw column names, never explained in prose. "sr" = success rate is guessable; which direction of `change_off` means "faced tough defenses" is not. |
| Fig 7, team tables | **LA** | Text says "the Rams"; chart and table say "LA" (next to "LAC"). A casual fan can't map LA to the Rams with certainty. |
| L1326-1332 | **pass block win rate, run block win rate** | Named in passing, not linked or glossed (RSWR is). |

## 2. Leaps (a step whose "why" is missing or assumed)

1. **Rule of thumb contradicts the success-rate explanation (L360-364 vs L590-591).** The chapter
   teaches "each yard ≈ 0.06" and "a down ≈ 0.7 points". Then it says the 40%-on-first-down rule
   agrees with EPA "because gaining 40% of 10 yards on first down is roughly where EP stays level."
   I tested it with the chapter's own heuristics: 4 yards × 0.06 = +0.24, minus 0.7 for the down =
   **−0.46**, so by the rules I was just taught, a 4-yard first-down run is clearly negative. What's
   missing is the value of **shorter distance to go** (2nd & 6 vs 2nd & 10). The chapter never gives
   a per-yard-of-distance number. The anchors and Fig 3 only cover "& 10". This is the single
   biggest hole in "work any play's EPA by hand."
2. **"A down is worth roughly 0.7 points" (L362) vs Fig 3 (p8).** At midfield the 3rd & 10 to 4th & 10
   gap on the chart is about 1.5 points, and the caption says "two-thirds of a point to a point."
   The Watch-for-it rule (L1366-1368) says "two-thirds per down … (more on third and fourth down)"
   with no number for "more". So which is it for a third-down estimate? Give per-down costs (1st→2nd,
   2nd→3rd, 3rd→4th) at one spot.
3. **"Forty yards of field position is worth more than two and a half points" (L360-361).** The bullet
   right above it says 0.06 per yard; 40 × 0.06 = 2.4. Either show 0.064 or say "about two and a half."
   A numerate reader stops here. Also L200 says midfield is "about two and a half" and the anchor
   table (L1362, p33) says 2.7.
4. **Fig 3 caption (L338): "on fourth down in your own half the value falls fastest."** The 4th-down
   line in your own half is the *flattest* line on the chart. I think it means "the gap from 3rd to
   4th is largest there," but I had to guess.
5. **L329-331: "even at your own 25 the single most likely outcome is that *you* score next."** On
   Fig 2 the single largest band at the own 25 is TD (~27%), with Opp TD close behind (~25%); "you
   score" is TD + FG combined. "Single most likely outcome" and "you score next" (two outcomes)
   don't fit together.
6. **L331-332: "'no score' is a thin band except at the extremes of the clock."** Fig 2 is drawn at
   one fixed clock value (the code uses 900 s, not stated in the caption). Nothing on the page shows
   what happens at the end of a half, so I can't see the claim. Same for the Watch-for-it bullet
   "long gains as the half's clock runs out … EPA scores near zero or below" (L1373-1374): the `late`
   feature is mentioned once (L233-234) and never shown.
7. **Fig 2 caption: "field goals take over in the middle of the opponent's half."** On the chart TD
   stays the biggest band everywhere in the opponent's half; the FG band grows but never "takes
   over."
8. **Success rate is "steadier" (L606) but is the worst stat in the table at L569-573** (same-game r
   0.56 vs 0.78 for EPA; weeks 1-9 → later points 0.44, the lowest of the four). The prose after the
   table (L576-581) discusses EPA vs yards and never mentions that success rate came last. Then
   Fig 9 says success rate repeats *better*. That tension is the most interesting thing on the page
   and it goes unexplained. Why does a steadier stat predict later scoring worse?
9. **`old_success = … | (plays.epa > 3)` (L596).** The yardage definition is patched with an EPA
   condition, "count TDs/long gains." Why would the yardage rule miss a touchdown? It inflates the
   92% agreement figure. Explain it or drop it.
10. **Selection effect #2 (L659-660): "That pushes in both directions at once."** Both examples given
    (runs on short yardage look good; passes on 3rd & long look bad) push the *same* way, in runs'
    favour. I couldn't work out what the two directions are.
11. **Fig 5 title "Dropbacks win on average, not on the typical play" (L646)** while the legend shows
    dropback success 46% vs runs 42%. On success rate, the "typical-play" measure the chapter just
    taught, dropbacks *also* win. Also unexplained: **why are both medians negative (−0.17, −0.16)?**
    If EP is an average, I expected the typical play to be about zero. (See gaps.)
12. **Seattle film room ledger (L828-833, p20).** The table shows the **winner, Seattle, with total EPA
    −3.52 and a 34% success rate, below New England's 40%**, in a 29-13 game. The text goes straight
    to "What to notice" about turnovers and never addresses it. Four sections earlier I was told EPA
    "lines up with the scoreboard" (r 0.78). The obvious answer (defensive TD, field goals, special
    teams and the pick-six credited to NE's offense) needs to be said, or the reader concludes EPA
    failed on the chapter's own showcase game.
13. **Seattle film room "top five" (L842-848).** The text names the three turnovers and then talks
    about Walker's "two long runs (30 and 29 yards)", but only one of them is in the top-five table.
    Row 4 (NE 1 & 10 at 35, 35 yards, +3.38, apparently a New England TD) is skipped. "The top five
    usually *are* the story of the game" is undercut by not telling the story of #4.
14. **Interception figure, bottom panel of Fig 4 (p11).** The dashed pass arrow goes *backwards* from
    the line of scrimmage before the return arrow starts (code comment: "pass caught behind the
    line"). Neither the caption nor the text says the ball was picked behind the line. I thought the
    diagram was wrong.
15. **L515-517: "A typical interception at midfield … costs about three and a half to four points."**
    No calculation shown. Using the anchors I get about 2.7 + (opponent's EP after a return, ~1.5-2)
    = 4.2-4.7. A two-line worked version would let me check myself.
16. **Passer rating (L1204-1216, L1234-1236).** "Each part scored 1.0 for an average passer" → "an
    average passer would rate about 66.7" requires knowing the sum is divided by 6 and × 100. Why
    divide by 6? Why cap at 2.375? Why is perfect 158.3? The code has the numbers but no reason. Also
    "**It is open**" is the fourth bullet under "its limits are now easy to see": a virtue listed as a
    limit.
17. **ANY/A weights (L1250-1252).** "Those weights are rough exchange rates between yards and points"
    is exactly the link I wanted, but it isn't made: why 45 yards for an interception? The chapter
    already gave me ~0.06-0.08 points per yard and ~3.5-4 points per interception. 4 / 0.08 ≈ 50
    yards. Say so and it clicks.
18. **QB table (L1271-1279).** "The 2025 table shows the useful disagreements: a quarterback with a high
    rating but middling EPA…" The table is the top 10 *by EPA*, so no middling-EPA quarterback is in
    it, and the text names nobody. The only visible disagreement (Mahomes: rating 90, EPA 0.17) isn't
    pointed out.
19. **RYOE is "the cleanest split in football analytics" (L887-888), then Fig 9 shows RYOE repeats at
    only 0.22, below plain yards per carry (0.27).** The stability lesson (L1046-1049) talks about the
    line, not about whether RYOE is mostly noise. So should I use RYOE or not? Objective 5 depends on
    the answer.
20. **RYOE table: McCaffrey near the bottom (−0.54)** with no comment. A casual fan knows him as a star;
    this is exactly the "a back can be valuable and still sit near the bottom" point (L908-909) and the
    text doesn't use it. Also L906-907: "a back with **a pretty average** behind a great line" reads as
    a typo (pretty *yards-per-carry* average?).
21. **Opponent adjustment table (L1073, p26).** No row is interpreted. I can't tell from the prose
    whether TEN's +0.061 means "faced hard defenses, so better than it looked." One sentence on one
    row would make the method concrete.
22. **"Offense is more stable than defense. Offenses keep their quarterback and play-caller" (L1038).**
    Defenses keep their coordinators too. The real reason given next (defenses depend on which QBs they
    faced) is fine; the first half is a leap.
23. **Win rates: "the 2.5-second clock removes the quarterback's role from pass rush" (L1332-1333).**
    Why? (Because a QB who holds the ball 5 s gives every rusher a "win.") One clause.
24. **Drill 2 answer (L1454-1461).** The chapter just spent a section on selection effects, then reads
    the 2nd & 1 table naively: "dropbacks still hold a small edge". Dropbacks on 2nd & 1 out of 22
    personnel are mostly play-action shots against loaded boxes, a selected sample. The answer
    should practise the section's own lesson. It also ends by recommending a play-action shot right
    after telling me "Run is the likely call," so I'm not sure what the "prediction" was.

## 3. Diagrams I couldn't decode, or whose caption didn't say what to notice

- **Fig 2 (p7) next-score stack.** Seven bands, but "Safety" is invisible and "Opp safety" is a
  sliver. Fine, but the caption claims ("field goals take over") don't match what I see (see leap 7).
  The clock value is fixed and unstated. The x-axis "40 50 40" labels sit almost on top of each other
  (also Fig 3).
- **Fig 3 (p8) EP by down.** Readable; caption's "value falls fastest" is backwards to my eye (leap 4).
- **Fig 4 (p11) three Super Bowl plays.** Top panel: the "EP after (4th & 4, own 27)" box is drawn at
  the *old* line of scrimmage (19), not at the 27 where the play ended; I read it as belonging to the
  start spot. Bottom panel: backwards dashed pass arrow, unexplained (leap 14). The yellow
  line-to-gain is drawn on all three panels but never mentioned; on panel 1 it's the reason the play
  is negative and the caption should say "notice the catch stops short of the yellow line."
- **Fig 5 (p14) EPA histograms.** Y-axis "Share of plays (density)" goes to 0.7; with 0.2-wide bins
  that's 14% of plays, not 70%. I read it as 70% first. Use percent per bin, or say "density." The
  spikes at ±4 are clipping pile-ups and look like real data; the caption doesn't mention them.
- **Fig 6 (p16) run vs dropback dumbbells.** Clear. The "(54% run)" labels are good.
- **Fig 7 (p18) team scatter.** Clear, the flipped axis is explained. The caption says "the two Super
  Bowl teams are in orange" but NE sits right on the average-defense line, while the text a few lines
  later calls the Rams, Seahawks and Patriots "top-right teams… good at both." NE is not visibly good
  at defense.
- **Fig 8 (p23) sample size.** Clear and the best figure in the chapter. The caption tells me what to
  notice.
- **Fig 9 (p25) stability bars.** Clear. But it quietly undercuts RYOE (leap 19), and the "success
  rate a little better than EPA" claim is 0.42 vs 0.40 on offense and 0.21 vs 0.21 on defense, which
  is not much of a difference. Say "about the same on defense."
- **Fig 10 (p27) fumble recovery.** Clear, good caption.
- **Fig 11 (p29) metric map.** The y-axis looks continuous (Passer rating higher than ANY/A, which is
  higher than CPOE…) but the text says it's open vs proprietary, a yes/no. I spent time trying to
  read meaning into vertical position within each half. Also **RYOE is plotted as proprietary**, yet
  the chapter downloads it from nflverse three pages earlier (L892). The caption should say
  "proprietary = you can download the number but can't recompute it," if that's the intent.
- **Drill figures 12-14 (p34-36).** Legible, but **none of the three questions uses the picture.** The
  questions are EP/EPA arithmetic; the dime shell in drill 1 and the stacked 46 in drill 3 never
  enter the reasoning (except one after-the-fact sentence in answer 1). The symbols `$`, `D`, `M`
  appear without a legend (I learned them earlier, but a reader landing from search won't have). In
  drill 3 the code moves the corners and FS by hand; the result reads fine.

## 4. Drag and repetition

- **p1-3: about 50 lines of setup code before any football** (COLS list plus the `md_table` formatter).
  `md_table` is pure presentation plumbing and costs a page of attention up front. Move it to
  `gridiron` or fold it with a code-summary like the repel helper.
- **p16-17: the 40-line `repel_labels` helper** sits in the middle of the team-EPA section, between
  "Put every team's EPA on one chart" and the chart. It has a code-summary label but it isn't folded
  in the PDF. It breaks the section's flow completely.
- **Explosive play rate is explained three times**: L608-626, the stability bullets L1042-1043, and the
  whole "Explosive play rate" subsection L1340-1345, which is a near-verbatim recap ("more than a
  third of all positive EPA", "repeats … less well than efficiency", "check the definition").
- **"EP values an average team, which is what lets EPA measure the difference"** appears at L142-144,
  L383-385 and the takeaways. Twice is enough.
- **"Turnovers dominate EPA"** is made in the worked play (L513-517), the Seattle film room, turnover
  luck (L1084) and drill 3. The film room adds nothing new on this point.
- The chart-styling code (ticks, legends, colours) in every cell is long. That's the Part-13 contract,
  but the figure cells could stay shorter if the tick labels were a helper.

## 5. Could I do each "You'll be able to…" item? (and the drills)

**Drills.** I covered the answers with my hand (they were visible, see §0) and used only the
chapter's rules of thumb.

- **Drill 1 (3rd & 9 own 30, 7-yard out).** My EP before: own 25 anchor 1.1 + 5 × 0.06 = 1.4, minus two
  downs × 0.7 = **≈0.0**, "a bit more off for third down," so ≈ −0.2. After: 4th & 2 at own 37: 1.1 + 0.7
  − 3 × 0.7 − "more" ≈ **−0.5**. EPA ≈ −0.3 to −0.5, not a success. Answer: +0.06 and −0.44. **Got it,
  but by luck on the vague "more on third/fourth down" fudge.** The answer doesn't give EP for
  4th & 2 at the 37, so I can't check my *after* number, only the average of a bucket of similar
  plays.
- **Drill 2 (2nd & 1 midfield, 22 personnel).** Predicted run (10-01 taught me shot plays on 2nd &
  short, so I also hedged "play-action"). On "is the run wrong by EPA," I guessed "gap much smaller
  than first down, roughly even." Answer: run 78%, EPA −0.01 vs +0.05. **Got it.** But the answer
  doesn't apply the selection-effect lesson (leap 24).
- **Drill 3 (1st & goal at the 1).** From L202 ("first-and-goal at the 1, more than six"): EP ≈ 6.3. TD ≈
  +0.7; stuff ≈ −0.7 (one down); fumble/touchback: opponent 1st & 10 at their 20 ≈ +0.7 for them →
  ≈ −7.0. Answer: +0.58 / −0.51 / −7.21. **Got it.** One snag: the chapter told me at L200 that the
  touchback moved to the 30 (2024) and 35 (2025). For a moment I put the ball at the 35. The answer's
  code comment says "their own 20" with no note that a turnover touchback is still at the 20 and
  only kickoff touchbacks moved. Say it in the answer.

**Objectives.**

1. *Explain the EP model and fit one.* **Explain: yes.** The next-score idea, the seven outcomes and
   why it's an average land well. **Fit one myself: only by copying.** The feature engineering
   (knots, interactions), standardisation and Adam loop get no prose.
2. *Work any play's EPA by hand; EPA per play and success rate; why EPA beats yards.* **Partly.**
   First-and-10 plays, yes. Any other distance, no: there's no value for yards-to-go, and the
   per-down costs are vague (leaps 1-2). Punts, field goals, penalties, kickoffs, and the PAT
   ("valued separately") are never priced, so "any play" is overstated. Why EPA beats yards: yes,
   and the 8-yard table is excellent.
3. *Compare run and pass honestly.* **Yes.** The best section. Fix the "both directions" sentence and
   the Fig 5 title.
4. *Signal vs noise.* **Yes** for sample size, stability and fumble luck. **Weak** for opponent
   adjustment, because no row of the table is interpreted.
5. *Use CPOE and RYOE.* **No for CPOE.** It gets one paragraph, a column in one table, and no scale: is
   +3 good? Is 10.78 (Maye) historic? **Shaky for RYOE.** I can read the table, but the stability chart
   tells me RYOE barely repeats, and the chapter doesn't reconcile that with calling it "the
   cleanest split."
6. *Place the broadcast metrics.* **Yes.** The map plus the subsections work, apart from the
   pseudo-continuous y-axis and RYOE's placement.

## 6. What I still wonder after finishing

1. **Why are median EPA values negative, and what is league-average EPA per play?** If EP is "average
   next score," does all EPA sum to zero? Why do dropbacks average +0.06 and runs −0.04? Something
   has to be negative on average: kickoffs? penalties? Never stated.
2. **What does a good number look like?** I'd like a scale card: team EPA/play (+0.1 good, +0.2 elite?),
   success rate (45% average?), CPOE (+3 good?), RYOE/att, QBR, DVOA %. The chapter has the data and
   gives scattered pieces (0.1 = "very good", L920).
3. **How did Seattle win 29-13 with negative offensive EPA?** (§2 item 12.) More generally: does team
   EPA include defense and special teams, and how do the defensive TD and field goals show up?
4. **How much is one yard of distance-to-go worth** (2nd & 2 vs 2nd & 10)? I need it for the mental
   ledger.
5. **How do penalties, punts and kickoffs get EPA, and who gets credited?** The setup cell drops
   them; the chapter never says how they're valued or why leaving them out is OK.
6. **How does nflverse split a completion's EPA between the throw and the run after catch?** "EPA
   divides credit poorly" (L1315), but nflverse ships `air_epa`/`yac_epa`. One sentence plus a
   pointer would answer "is that 60-yard catch-and-run the QB's or the receiver's?"
7. **Did the 2024-2026 kickoff and touchback changes shift the EP curve?** The model pools 2016-2025
   while the touchback spot moved twice. Does that matter for 2026 games I'll watch? Also, does
   nflverse's "era" variable handle it?
8. **Where do I get QBR, DVOA, PFF grades and win rates in Python, and which are free?** The chapter says
   which are proprietary but not which ones I can actually pull (nflreadpy has ESPN QBR; PFF is
   paywalled).
9. **What exactly do I write in the prediction log** for the EPA-in-your-head drill (L1378-1380)? The
   instruction is "add the result," with no format.
10. **How is the extra point valued, and why count a TD as 7?** (L437.)
11. **Is RYOE a skill?** (§2 item 19.)

## Highest-value fixes (in order)

1. Make the print answers actually collapse or move (§0).
2. Give a per-yard-of-distance value and explicit per-down costs, then make the "40% on first down"
   explanation consistent with them (leaps 1-3).
3. Explain Seattle's negative EPA in its own Super Bowl win (leap 12).
4. Say what "neutral situation" means where the filter is introduced (§1).
5. Reconcile success rate's poor predictive r with "steadier" (leap 8) and RYOE's low stability with
   "cleanest split" (leap 19).
6. Add a "what's good" scale for EPA/play, success rate and CPOE; explain why EPA medians are negative.
7. Move `md_table` and `repel_labels` out of the reading path; cut the third explosive-play
   explanation.

---

## Revision (2026-10-06)

Revised `chapters/13-analytics-and-data/13-02-expected-points-and-success-rate.qmd` against this review
and `13-02-coach.md`. Rebuilt with `build_pdfs.py 13-02-expected-points-and-success-rate --html`: OK, zero
errors, 42 pages. Every figure page was rasterized and looked at (Figs 4, 7 and 12-14 at 100-130 dpi).
New factual claims were checked against nflverse data or a cited source (listed at the end).

### Beginner review

| Finding | Action |
|---|---|
| §0 Drill answers print inline | **Root cause was the filter, not the chapter.** On Quarto 1.10 callouts become custom `Callout` nodes before user filters run, so `filters/print-answers.lua`'s `Div` handler never matched any callout, nested or not (tested on a scratch doc). Added a `Callout` handler (the `Div` path is kept) to the shared filter. Answers now move to "Answers to Predict the play" with a pointer. This also fixes 03-02 and any chapter using the AUTHORING §8 convention. Answers switched to `callout-tip`. |
| §1 neutral situation | Defined where the filter is introduced (now "four choices" paragraph), with links to the glossary and 13-04. |
| §1 win probability | Glossed at the filter, with a link to 13-03. |
| §1 Next Gen Stats, Big Data Bowl | Both glossed at first use and linked to the glossary; BDB links to 13-05. |
| §1 knots / log loss / Adam / standardisation | New four-bullet walkthrough before the model cell (features, knots, softmax and log loss, standardising and Adam). |
| §1 "down 4" | Now "trailing by 4". |
| §1 wins-above-replacement | One-clause gloss. |
| §1 extra point "valued separately" | Explained: TD booked at 7 because the PAT is nearly automatic; a made PAT gets about +0.07, a miss about −0.93 (checked in nflverse). |
| §1 `rush_epa` | Removed; the text now points at the printed designed-run EPA. |
| §1 turnover margin / regress | Turnover margin defined; "regress to the mean" spelled out. |
| §1 DAVE | Already glossed inline; left as is (not in the term index, so no glossary entry). |
| §1 table column names | Team table, opponent-adjustment table and RYOE table columns are now explained in prose (including the sign of `change_off`). |
| §1 LA | Fig 7 labels the point "LA (Rams)"; the caption says LA = Rams, LAC = Chargers. |
| §1 pass/run block win rate | Both glossed inline. |
| Leap 1 (40% rule vs rules of thumb) | New `rules-of-thumb` cell: per-yard value (0.061), per-down costs (0.68 / 0.97 / 1.43 at midfield), value per yard of distance (0.069) and the 4- and 5-yard first-down gains (−0.12 / +0.04). Success-rate text now says 40% sits a little below EP break-even, which is also what the disagreement data shows. |
| Leap 2 (0.7 per down vs Fig 3) | Explicit per-down costs replace "two-thirds ... more on third down", in the habits list and in the Watch-for-it ledger. |
| Leap 3 (40 × 0.06) | Now printed inline as `40 * slope` (≈2.5). Anchors elsewhere are inline from the plotted curve, so prose and figure agree. |
| Leap 4 (Fig 3 "falls fastest") | Caption rewritten to the 3rd-to-4th gap, widest from about midfield to the opponent's 40 (checked on the rendered chart). |
| Leap 5 ("single most likely outcome") | Rewritten with inline values: TD+FG 55% vs opponent's 35% at the own 25. |
| Leap 6 (clock not shown) | Caption states 15 minutes left; text gives "no score" at the own 25 with a full quarter (10%) vs under two minutes (63%), computed from the model's late feature. |
| Leap 7 ("FGs take over") | Caption corrected: the FG band widens but never overtakes TD. |
| Leap 8 (success rate "steadier" yet worst predictor) | Reconciled in the success-rate section and the stability bullets: it is only marginally steadier (0.42 vs 0.40 offense, 0.21 vs 0.21 defense) and loses the size information that produces points. Fig 9 caption and takeaway now say "about as well as EPA". |
| Leap 9 (`| (epa > 3)` patch) | Patch removed; agreement is still 92%. Added what the disagreements are (69% first-down 4-5-yard gains; turnovers about 3%). |
| Leap 10 ("both directions") | Rewritten: short-yardage runs and third-and-long passes both flatter runs; give-up draws and play-action on second-and-short push the other way. |
| Leap 11 (Fig 5 title; negative medians) | Title now "Dropbacks win on average; the typical play is a small loss either way". New paragraph explains the skew (2025 mean +0.01, median −0.17). |
| Leap 12 (Seattle negative EPA in a 29-13 win) | Explained in the film room: five Myers FGs, punts and the pick-six sit outside Seattle's offensive ledger (checked in pbp). |
| Leap 13 (top-five row 4 skipped) | Row 4 identified as the Hollins 35-yard TD at NE WP 0.03; a `wp` column was added to the table. |
| Leap 14 (backward pass arrow) | Fig 4 adds an on-field note "picked off at NE 45, 11 yds behind the line" (pbp `air_yards` −11), and the caption explains it. |
| Leap 15 (midfield interception arithmetic) | New `int-arithmetic` cell computes it with the chapter model. |
| Leap 16 (passer rating 6, 2.375, 158.3; "It is open" listed as a limit) | Arithmetic explained; "open" moved out of the limits list and stated as the virtue. |
| Leap 17 (ANY/A weights) | Exchange-rate arithmetic added (45 yds × 0.08 ≈ 3.6 points; 20 yds ≈ 1.6). |
| Leap 18 (QB table disagreement unnamed) | Table adds rating and EPA ranks; the text names the biggest disagreements inline (2025: L. Jackson rating 4th vs EPA 19th; Mahomes 23rd vs 8th). |
| Leap 19 (RYOE "cleanest split" vs 0.22 stability) | Now "cleanest idea", followed by a paragraph on why it is cleaner in idea than in practice (handoff snapshot, post-handoff blocking booked to the runner, sample noise). Advice: one season is a hint, several are evidence. |
| Leap 20 (McCaffrey; "pretty average" typo) | McCaffrey interpreted; typo fixed. |
| Leap 21 (opponent table not interpreted) | Columns explained; the biggest mover (TEN, −0.201 → −0.140) is interpreted inline. |
| Leap 22 (offense more stable reason) | Reason rewritten around the quarterback. |
| Leap 23 (2.5-second clock) | Clause added: a QB who holds the ball would otherwise hand rushers "wins". |
| Leap 24 (drill 2 ignores selection; unclear prediction) | Answer now applies the selection lesson with data (44% play-action on 2nd-and-1 dropbacks vs 27% overall, FTN 2022-25), and states the prediction ("run") plus what to watch for. |
| §3 Fig 2/3 crowded x labels | Ticks are now Own 1 / Own 25 / 50 / Opp 25 / Opp 1. |
| §3 Fig 4 "EP after" box at the old LOS | The box is anchored at the end spot, between the yard numbers. Caption mentions the yellow line. |
| §3 Fig 5 density axis; spikes at ±4 | The y axis is now the share of plays per bin (%). The caption explains the end-bin pile-up. |
| §3 Fig 7 NE "good at both" | Text and caption say NE's defense was league-average (18th); the three teams got their net EPA by different routes. |
| §3 Fig 9 "a little better" | Now "about as well". |
| §3 Fig 11 pseudo-continuous y; RYOE as proprietary | Two shaded bands, labelled "open: rebuildable" / "closed: numbers only". The caption says height within a band is only for spacing, and that closed means downloadable but not rebuildable (RYOE, QBR). |
| §3 Drill figures unused; no symbol legend | Position-letter legend added before the drills. Drill 1 now draws the out route, the catch at +7 and the rallying dime back; drill 2 highlights the eighth man; the question text asks about the picture. |
| §4 setup code drag | `md_table` cut to 9 lines. |
| §4 `repel_labels` mid-section | Replaced with a 17-line `label_points` (labels avoid markers too). No library alternative exists in the container (no adjustText/tabulate), so it stays inline with a code summary. |
| §4 explosive explained three times | Third explanation cut to one sentence. |
| §4 "EP values an average team" ×3 | The duplicate in "what EP leaves out" was removed. |
| §4 turnovers repeated in film room | The film room now teaches new things (ledger scope, WP, scheme) rather than restating it. |
| §4 chart styling code length | **Not applied**: Part 13 shows its code by contract, and a tick helper would hide the matplotlib a reader is meant to copy. |
| §5 Drill 1 "after" EP not given | The answer prints model EP for 3rd & 9 at own 30 and 4th & 2 at own 37. |
| §5 Drill 3 touchback spot | Answer explains that turnover touchbacks are still at the 20; only kickoff touchbacks moved. |
| §5 Obj 2 "any play" (punts, FGs, penalties, PAT) | PAT and penalty snaps are now priced. **Punts, FGs and kickoffs are not worked**: the chapter's objective is scrimmage plays, and pricing kicks belongs with 13-03's decision analysis. |
| §5 Obj 5 CPOE scale | Units explained (+3 = three more completions per hundred). New "What a good number looks like" table (10th / 50th / 90th percentile for team EPA, success rate, QB EPA, CPOE, RYOE). Maye's +10.8 ranks 1st of 328 QB seasons. |
| §6 Q1 medians / league average | Answered (Fig 5 paragraph). |
| §6 Q2 scale card | Added (see above). |
| §6 Q3 Seattle | Answered (film room). |
| §6 Q4 yard of distance | Answered (`rules-of-thumb`). |
| §6 Q5 penalties / kicks | Penalty snaps: new cell and paragraph. Kicks: see Obj 2 above. |
| §6 Q6 air/YAC split | One paragraph on `air_epa`/`yac_epa`. |
| §6 Q7 kickoff changes and EP | Paragraph added: EP stops at the next score, so kickoff changes move where drives start, not what a spot is worth. |
| §6 Q8 where to get QBR/DVOA/PFF in Python | **Not applied**: no source-checked list of which loaders exist for each; flagged as open. |
| §6 Q9 prediction-log format | Line format specified. |
| §6 Q10 PAT | Answered. |
| §6 Q11 Is RYOE a skill? | Answered (RYOE paragraph). |

### Coach review

| Finding | Action |
|---|---|
| A1 Fig 13 9-man box | LCB moved to (d=5, w=−9), outside U; SS highlighted with an "8th man" note; caption names the eighth defender (E5). |
| A2 Fig 14 depths and "W" collision | MIKE and SS at d=2.3, FS at 3.0, CBs at d=2; offensive wing relabelled **H**. The lateral window was tightened to (−11, 11) so the second level doesn't crowd the line (the coach's exact 2.0/2.5 depths overlapped the DL markers at this scale; still within 1-2 yards of the goal line). |
| A3 Fig 12 MIKE on #3; draw the empty yards | MIKE at w=+2.5. `situation_diagram` now takes a `setup(p)` callback. Drill 1 draws H's quick out (catch at +7), the dropback and throw, the DB's rally drop, highlights and a note. |
| A4 Fig 4 label on the 30; backward arrow | Fixed (see beginner §3 and leap 14). Phrasing follows the pbp exactly: Witherspoon is credited with the QB hit and the pass defensed. "Blitz" was not asserted. |
| A5 Fig 7 caption wording | "allowing less EPA is higher". |
| B1 4th-down curve caveat | New Common-misconception callout with a link to 13-03. Go rate 13% (2016) → 23% (2025), nflverse. |
| B2 QB sneaks | New `sneak-split` cell (FTN `is_qb_sneak`, 2022-25): sneaks are 13.5% of short-yardage runs at +0.37 EPA and 78% success. Without them runs earn +0.02 vs dropbacks +0.04 but still succeed more (61% vs 57%). |
| B3 penalty snaps | New `penalty-snaps` cell (1,488 snaps; 279 DPI at +1.73; 374 holds at −1.06; dropback EPA +0.043 → +0.063 with penalties). Cited nflfastR's beginner's guide for the `pass == 1 | rush == 1` convention. The rbsdm.com claim was **not** printed (unverified). |
| B4 WP context for the hook | Added after the worked plays (NE WP 3% at the pick, SEA 89% at the Kupp catch, computed inline). |
| B5 screens, RPOs, play-action in selection #1 | Added. |
| B6 coach dialect | Added "staying on schedule / winning first down / efficiency" with a link to 10-01. The "4+ yards" staff grading convention was framed only as what the 40% rule means; not attributed. |
| B7 12+/16+ definition | Now defined first in the explosives section and the glossary, sourced to the 2012 Raiders (Dennis Allen) and 2016 Cowboys (Scott Linehan). Both definitions are computed (12/16: 10.5% of plays, 44% of positive EPA). **Note for fact-check:** the Hoppen piece does *not* list 12/16 (it proposes 10/25); its footnote was reworded. |
| B8 RYOE limits | Added (post-handoff blocking, vision). |
| B9 CPOE limits | Added (drops, separation). |
| B10 play-action wording | Rewritten: the fake has to look like your real run game. |
| B11 fumble type | **Not applied**: no sourced recovery-by-type numbers; the conclusion doesn't depend on it. |
| C Seattle scheme | Third film-room callout computes Seattle's two-high share (52% of 2025 dropbacks, 3rd; 73% in the Super Bowl, four or fewer rushers on 48 of 57) from nflverse participation, and cites the NFL.com NGS piece. No claim is made about who called the defense. |
| C Ravens "option look" | Reworded to designed runs and keeps. The "gap and duo" scheme detail was not printed (unsourced). |
| C Geno Smith | Team named (Raiders). The "tipped balls" mechanism was deleted. The coach's "high count of risky throws" did **not** check out: his interception-worthy rate ranked 11th of 24. The text now prints that rank and says the excess is part luck, part charting judgement. |
| C Drill 2 "first down very likely" | Replaced with third-and-1 conversion (70%, computed inline). |
| C Drill 3 "dominated by fumbles" | Now "one goal-line fumble can erase ... a whole season of EPA". |
| D `situation_diagram` returns/callback | `setup(p)` callback added. |
| D gridiron report items | Not edited (per instructions): `defense()` puts a CB head-up on an in-line TE when no WR is on that side; the `goal_line` wing is keyed and labelled `W`, colliding with the WILL. Both were worked around in the chapter. |
| E1 4th & 2 at own 37 | "a situation where most teams still punt", with a 13-03 link and a note that 4th-down models now rate it near a toss-up. |
| E2 "success rate 4%" | The success figure was dropped; the answer prints the share with positive EPA and calls them oddities (pbp shows mostly post-catch defensive penalties). |
| E3 empty: pressure / Cover 1 | Added, with a link to 13-04. |
| E4 inline answers in PDF | Fixed in the shared filter (see §0). |
| E5 Fig 13 caption | Done. |

### Other fixes found while revising
- The Seattle film-room callout grew past one page, and Typst clipped it (text overprinted). It is now split into three callouts.
- Cells whose `md_table` was no longer the last expression lost their tables; fixed by reordering or `display()`.
- `md_table` printed seasons as "2,024"; fixed.

### Still open
- Where to fetch QBR / DVOA / PFF / win rates in Python (beginner §6 Q8).
- Pricing punts, field goals and kickoffs by hand (beginner Obj 2).
- Fumble recovery by fumble type (coach B11).
- Fact-check should look at the new claims: Raiders 2012 / Cowboys 2016 explosive definitions; nflfastR guide wording; the NFL.com Seahawks coverage piece as the "split-safety ... title run" source; and "since about 2018" for fourth-down aggressiveness, which is backed only by this chapter's nflverse go-rate numbers.
