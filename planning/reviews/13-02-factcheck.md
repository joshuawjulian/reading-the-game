# Fact-check log: 13-02 Expected Points, EPA, and Success Rate

Checked 2026-10-06 against FACTS-current.md, web sources, and the nflverse pbp (re-queried in the `rtg` container). All 19 `<!-- VERIFY -->` comments are resolved and removed. Build `build_pdfs.py 13-02-expected-points-and-success-rate`: OK (37 pages).

| Claim | Verdict | Source | Change |
|---|---|---|---|
| SB LX: Darnold to Kupp, 8 yds on 3rd & 12 at SEA 19, Q3; Seattle punts next snap | VERIFIED | nflverse pbp `2025_22_SEA_NE` play 2858 (Q3 2:48), next play Dickson punt | none |
| SB LX: Darnold to Barner, 16-yd TD, 1st & 10 at NE 16, start of Q4 | VERIFIED | pbp play 3166 (Q4 13:29) | none |
| SB LX: Maye intercepted by Nwosu, 45-yd return TD, Q4, EPA −9.81 | VERIFIED | pbp play 3910; FACTS §1 | none |
| Next three costliest plays: Julian Love INT, Derick Hall strip-sack (recovered by SEA) | VERIFIED | pbp (Love INT Q4 8:49, −5.44; Hall strip-sack Q3 0:16, recovered by B. Murphy, −4.37) | none |
| Seattle's other sacks cost NE about 1–2 points each | VERIFIED | pbp: Maye sacks −1.52, −1.59, −1.78, −0.98, −0.98 | none |
| Walker's 30- and 29-yd runs in Q2, both on 2nd & 10, SEA's biggest gains | VERIFIED | pbp (Q2 14:04 and 13:34; biggest SEA gain otherwise a 23-yd Kupp catch) | none |
| "Pressured throw" description of the Nwosu pick | N/A | gamebook bracket `[21-D.Witherspoon]` = QB hit | The claim isn't in the current text, so there's nothing to change |
| SEA 2025 staff: HC Macdonald, DC Durde | VERIFIED | FACTS §1/§9 | none |
| Seattle 2025 allowed the fewest neutral EPA/play | VERIFIED | Recomputed: SEA −0.149, HOU −0.145, PHI −0.139 | none |
| 2025 net EPA order Rams, Seahawks, Patriots | VERIFIED | Chapter output table (rendered) | none |
| Baltimore 2024 best neutral offense, narrowly ahead of Buffalo | VERIFIED | Recomputed: BAL 0.200, BUF 0.192 | none |
| Ravens "one of the few teams" whose designed runs had positive EPA | CORRECTED | Recomputed: 8 of 32 teams positive in 2024 (BAL 4th) | Now "one of only about a quarter of teams ... in neutral situations" |
| Sacks about −1.7 EPA, scrambles about +0.4 (2025) | CORRECTED | Recomputed: sacks −1.74, scrambles +0.48 | Scrambles now "+0.5" |
| A typical midfield interception without the return costs 4–5 points | CORRECTED | Recomputed 2016–25: non-TD INTs at the 45–55 average −3.7 (median −3.9) | Now "about three and a half to four points", "without a touchdown return" |
| Explosive plays: <10% of plays, "about a third" of positive EPA | CORRECTED (wording) | Chapter output: 8.9%, 37% | Now "more than a third" (twice) |
| Explosive 10+/20+ is "the most common" definition | SOFTENED | Hoppen, "How should we define an explosive play?" (12/15, 12/20, 12/16, 10/15, 10/20 all used) | Now "a common one"; glossary "most often" → "often"; added `[^explosive]` |
| 2nd & 1: ~3 of 4 snaps are runs; ~half of runs negative EPA; dropbacks hold a small edge | VERIFIED | Recomputed 2016–25 neutral: 78% runs; 49.5% of runs negative; EPA 0.05 vs −0.01 | none |
| 1st & 10: dropbacks ~0.2 EPA better than runs (2021–25 neutral) | VERIFIED | Recomputed 0.100 vs −0.089 | none |
| Short yardage: about equal EPA, runs succeed more often | VERIFIED | Recomputed 0.076 vs 0.054 EPA; 64% vs 58% success | none |
| 3rd & 9 at own 30 worth slightly more than 0; converted well under half the time | VERIFIED | Recomputed EP +0.06; conversion 32% | none |
| Own 25 = "the usual spot after a touchback" | CORRECTED | FACTS §3 / NFL.com: kickoff touchback moved to 30 (2024) and 35 (2025) | Now "for decades the spot after a kickoff touchback (moved to the 30 in 2024, 35 in 2025)" + `[^touchback]` |
| 1st & 10 at own 25 "happens thousands of times a season" | CORRECTED | Recomputed: 2,063 plays in 2023, only 199 in 2025 | Now "happened about two thousand times a season while it was the touchback spot" |
| nflfastR by Baldwin and Carl, 2020; XGBoost; features: seconds in half, yard line, home, roof, down, distance, era, timeouts | VERIFIED | Baldwin, Open Source Football write-up | none |
| nflfastR weights plays "so that blowouts and very long drives do not dominate" | CORRECTED | Same write-up: weights are by score differential and by drives-from-the-next-score | Rewritten to "down-weights plays from lopsided games and plays several drives away from the next score" |
| nflscrapR (Horowitz, Yurko, Ventura, CMU), 2017, plays since 2009; multinomial logit | VERIFIED | nflWAR paper (arXiv 1802.00998) | Footnote got the DOI 10.1515/jqas-2018-0010 |
| Carter & Machol, *Operations Research* 19(2), 1971, 541–544; Carter with Bengals; Machol Northwestern professor | VERIFIED | RePEc listing; Wikipedia; ESPN | Footnote title now "Technical Note: ..." |
| "A season of play-by-play ... thousands of first-and-10 situations ... done with punch cards" | CORRECTED / REMOVED | ESPN: data from team PR offices for 56 games in the first half of 1969, 8,373 plays; no source for punch cards | Now gives 1969, 56 games, 8,373 plays, PR offices, 10-yard strips; "punch cards" replaced with "before personal computers" |
| Carter studied at Northwestern while playing | VERIFIED (sharpened) | Wikipedia (master's during first Bears stint); ESPN (MBA program) | Now "earned a master's degree at Northwestern while playing for the Bears" |
| Carter QB of Walsh's early Cincinnati offense, later the West Coast offense | VERIFIED | Wikipedia; ESPN | none |
| *Hidden Game of Football* (1988) linear EP: −2 at own goal line, +6 at opponent's, 0.08/yd, 0 at own 25 | VERIFIED (LIKELY) | cfbfastR EP fundamentals Part III (endpoints −2 and +6, straight line); the slope and zero point follow from them | Source added to `[^hidden]`. Note: the cfbfastR text also says "0 at the 20, 2 at the 40", which doesn't fit its own endpoints, so the book itself should be spot-checked |
| Brian Burke, former Navy pilot; Advanced NFL Stats late 2000s; popularised EPA; joined ESPN | VERIFIED (sharpened) | ESPN Front Row, June 2015; ESPN Press Room bio (F/A-18 carrier pilot; site founded 2007) | Now "F/A-18 pilot", "from 2007", "helped popularise", "in 2015"; footnote replaced |
| Success rate 40/60/100 "popularised by Football Outsiders"; origin in Hidden Game | SOFTENED | Schatz, FO explainer on ESPN (2007): success rate at 40/60/100, defensive stops at 45/60/100; Steelers Depot (origin in Hidden Game; FO later used 45%) | Text now credits Hidden Game and notes FO's 45% variant; footnote replaced (old URL was a 403 FTN page cited for FO's wording) |
| Play-action doesn't depend on run frequency or success (Baldwin; Hermsmeyer) | VERIFIED | Baldwin FO guest column, Feb 2018 (2011–17 data); Hermsmeyer, "Can NFL Coaches Overuse Play-Action? They Haven't Yet," FiveThirtyEight 2018; summarised on Wikipedia "Play-action pass" | Footnote titles and years fixed |
| NGS Expected Rushing Yards built on the 2020 BDB winner (The Zoo: Singer, Gordeev) | VERIFIED | NFL.com NGS "Intro to Expected Rushing Yards"; operations.nfl.com 2020 BDB results | Named the winners in the text; footnote URLs replaced (the NGS glossary wasn't the right page) |
| Passer rating adopted 1973; committee Don Smith (PFHOF), Seymour Siwoff (Elias) | VERIFIED + CORRECTED | PFHOF "NFL's Passer Rating"; Wikipedia | Added Don Weiss (NFL) |
| Anchored on a "1970-era" average passer | CORRECTED | PFHOF: standards from all qualified passers since 1960; Wikipedia: 1960–1970 | Now "an average passer of 1960-1970" |
| Pre-1973 problem: "several separate stats and the rankings disagreed" | CORRECTED | Palmer, *Coffin Corner* 7(1), 1985: passers were ranked in categories and the ranks summed; the categories changed repeatedly; ratings depended on other passers | Rewritten to describe the summed-rank system and why it couldn't be compared across seasons |
| Average 66.7, cap 2.375, max 158.3 | VERIFIED | Palmer 1985; PFHOF | none |
| ANY/A: weights trace to Hidden Game; PFR uses 20/TD and 45/INT | VERIFIED | PFR glossary (as quoted in search results; PFR returned 403 to the fetcher): "now using 20 yards per TD instead of 10" | Footnote notes the book's 10 |
| QBR introduced 2011; 0–100, 50 average; EPA basis, credit division, includes runs, sacks, penalties; opponent adjustment | VERIFIED | ESPN QBR explainer, Sept 8, 2016; Wikipedia (opponent adjustment) | none |
| QBR "weights plays by their effect on win probability, so a big throw in a close fourth quarter counts for more" | CORRECTED | ESPN 2016: blowout plays are down-weighted; the 2011 clutch up-weighting was removed | Rewritten: down-weights plays when the game is out of reach; notes that the clutch boost was dropped |
| The year QBR added its opponent adjustment (2016?) | REMOVED (was only in the VERIFY note) | No source found | Text gives no year |
| DVOA: Schatz, Football Outsiders, early 2000s; FTN since FO closed in 2023 | VERIFIED (sharpened) | Wikipedia "Football Outsiders" (Schatz to FTN Aug 29, 2023; FO offline Sept 1, 2023) | Now "since August 2023, when Schatz moved there and Football Outsiders shut down" |
| Early-season DVOA "leans on preseason projections in some versions" | VERIFIED (clarified) | FTN DAVE ("DVOA Adjusted for Variation Early") blends projection and results | Now names DAVE explicitly |
| PFF founded in England 2004 by Neil Hornsby; −2 to +2 in 0.5 steps; scaled to 0–100 | VERIFIED | pff.com/grades; Wikipedia | Footnote describes both |
| ESPN's four win rates "introduced from 2018 on" | CORRECTED (sharpened) | Burke, ESPN, Oct 5, 2018 (PRWR/PBWR); Burke, ESPN, Sept 8, 2020 (RSWR/RBWR) | Now "pass rates in 2018, run rates in 2020, both designed by Brian Burke" |
| PRWR = beat the block within 2.5 s; PBWR = sustain 2.5 s | VERIFIED | Burke 2018 | none |
| RSWR = "beats his block quickly enough to disrupt the run" | CORRECTED | Burke 2020: win = fit/fill, spill (penetrate), force (contain), or tackle within 3 yds while blocked | Definition rewritten |
| Footnote URLs (PFHOF, ESPN QBR, FTN DVOA, PFF grades, ESPN win rates) | VERIFIED / REPLACED | PFHOF old 2005 path replaced with the live page; QBR, PFF and 2018 win-rate URLs load; FTN DVOA explainer returns 403 to the fetcher but is FTN's page (kept) | Footnotes updated |
| Interception-worthy charting available 2022+ (FTN) | VERIFIED | FACTS §7 | none |
| Caleb Williams (most INT-worthy throws above INTs), Geno Smith (more INTs than INT-worthy) in 2025 | VERIFIED | Chapter output (C. Williams 7 INT / 18 IW; G. Smith 17 / 14) | none |
| Drake Maye led 2025 in EPA/dropback, CPOE +10.8 | VERIFIED | Chapter output | none |
| Goal-line fumble recovered by the defense in the end zone = touchback at the 20 | VERIFIED | NFL rule (touchback on a turnover is the 20; the 2025 move to the 35 is kickoffs only) | none |

**Counts:** VERIFIED 33 · CORRECTED 16 · SOFTENED 2 · REMOVED 2 (punch cards; the QBR opponent-adjustment year) · N/A 1 (the pressured-throw note).

**Still uncertain:**
- The exact straight-line values in *The Hidden Game of Football*. The endpoints come from a secondary source whose own middle values don't fit them. Check against the book.
- The PFR glossary returned 403. The "20 instead of 10" note comes from a search snippet of that page.
- The FTN DVOA explainer URL returned 403 and was not read. DVOA's "success-style values" description is FO's long-standing method, but this check didn't confirm it on that page.
- I found no exact title for Baldwin's February 2018 FO guest column, so the footnote describes it instead.
