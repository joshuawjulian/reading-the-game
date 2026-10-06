# Fact-check: 05-05 Run Fits: Gap Integrity, Force, Spill, and Box Math

Checked 2026-10-06 against FACTS-current.md, nflverse play-by-play + participation + FTN charting (recomputed in the
`rtg` container with the chapter's filters) and web sources. All 3 `<!-- VERIFY -->` comments are resolved and removed.
The chapter builds (`build_pdfs.py 05-05-run-fits-and-box-math`: OK, 22 pages). Footnotes: 18 definitions (one new,
`quarters`), each referenced exactly once.

| Claim | Verdict | Source | Change |
|---|---|---|---|
| Six-or-fewer box share on designed runs: 37–40% 2018–22, 43% 2023, 58% 2024, 55% 2025 | VERIFIED | Recomputed: 36.7, 38.4, 39.6, 38.4, 38.9, 43.3, 57.7, 54.6% | None (2018 is 36.7%, "37–40%" rounds fine) |
| Pooled neutral-situation EPA by box: runs −0.03/−0.05/−0.09/−0.15; SR 41/40/37/34%; YPC 5.1/4.8/4.6/4.2; n ≈ 1,600/21,800/20,100/6,700; dropbacks +0.06/+0.08/+0.12/+0.16 | VERIFIED | Recomputed (−0.027, −0.052, −0.094, −0.148; n 1,603/21,800/20,109/6,721; dropbacks 0.063/0.078/0.120/0.162) | None |
| FTN-era 8+ dropback point rests on ~800 plays | VERIFIED | Recomputed n = 808 | None |
| Light box vs 7 / 8+: "a quarter of a yard" / "more than half a yard" more per carry | VERIFIED | 4.83 vs 4.55 vs 4.18 | None |
| fig-box-epa caption: each extra box defender costs runs "about 0.03 to 0.05" EPA | CORRECTED | Steps are 0.025, 0.042, 0.054 (runs) and 0.015, 0.042, 0.042 (passes) | Now "about 0.02 to 0.05" |
| Fangio defenses top-5 in six-or-fewer share every season 2019–21, 2023–25 (5th, 2nd, 3rd, 2nd, 3rd, 3rd); avg-box ranks 7, 2, 3, 10, 5, 5; EPA/run allowed rank 1st 2024, 7th 2025 | VERIFIED | Recomputed, exact match | None |
| 2024 PHI faced six-or-fewer on 66% (league 58%), allowed −0.18 EPA per designed run, lowest of 32 | VERIFIED | Recomputed 66.3%, league 57.7%; −0.182 on plays with a recorded box (−0.173 on all designed runs; rank 1 either way) | None |
| BAL 2019: 7+ boxes on 65% (league 62%); +0.10 vs 7 (league −0.10), +0.04 vs 8+ (league −0.13); +0.09 overall, 1st; Jackson 120 designed runs, 7.1 YPC | VERIFIED | Recomputed (0.650/0.616; 0.100/−0.102; 0.042/−0.125; +0.089 on box-recorded plays; 120 runs, 7.12) | None |
| PHI 2024 offense: 61% light boxes (league 59%), 5.4 YPC (league **4.6**), 14% 10+ (league **11%**), 4.6 vs 7+, Barkley 5.9 | CORRECTED | Recomputed excluding FTN `is_qb_sneak`: 61.3%/58.6%; 5.43 vs **4.68**; 14.3% vs **11.8%**; vs 7+ **4.73**; Barkley 5.87 | League YPC 4.6→4.7 (text and fn), league 10+ 11%→12%, PHI vs 7+ 4.6→4.7 (league 4.0 added) |
| Inquirer: 73.5% light boxes, third-highest rate, "through the first **three** weeks"; the Inquirer "counted" | CORRECTED | EJ Smith, Inquirer, Sept 19 2024 (fetched): through the first **two** weeks, written after the Week 2 loss to Atlanta | "three weeks" → "two weeks"; "counted" → "reported" |
| Inquirer "steal" back gaps quote | VERIFIED | Same article, verbatim | None |
| Fangio: born 1958; first NFL job 1986 (Saints LB coach); "NFL assistant for more than thirty years"; first-time HC at 60 (DEN 2019–21); SF DC 2011–14, CHI DC 2015–18, Eagles consultant 2022, MIA DC 2023, PHI DC 2024– (still 2026) | VERIFIED (VERIFY #3) | Wikipedia "Vic Fangio" (born Aug 22 1958; hired Jan 10 2019); FACTS §9 | Footnote now states 1986 start and 32 NFL seasons as an assistant |
| "copied across the league by the coaches who worked for him" | SOFTENED (VERIFY #2) | PFF, Diante Lee, Sept 15 2021 (Staley, Barry, Desai carrying the scheme); Wikipedia (Staley followed Fangio CHI→DEN) | Now "spread across the league, carried first by coaches who had worked for him, such as Brandon Staley"; PFF source added to fn `fangio` (Barry did not work directly for Fangio, so he is named only as part of the PFF tree) |
| Force/alley by coverage: Cover 3 safety force, Cover 2 corner force; clinic vocabulary | VERIFIED (VERIFY #1) | Ed Raby Jr., "Simplifying Your 2nd Level Run Fits," AFCA, May 9 2023 (Cover 3: SS force/fold; Cover 2: corners force) | fn `fitwords` rewritten around the AFCA article; unverified "lever-spill-lever"/"fast players" wording removed; text's vocabulary list now "fold," "stack," "vice," "secondary contain" |
| Quarters is "the shape most of the NFL plays on early downs today" | CORRECTED | NGS via FACTS §10: Cover 4 17.2% in 2025 (2018–24 avg 13.9%); Cover 3 still more common | Now "the two-high coverage that has grown fastest in today's NFL" with new fn `quarters` |
| Svec, "Defending Split Zone" (Jan 12 2022) spill = "fight INSIDE the blocker by using a Wrong Arm Technique"; box end "will fight hard to stonewall the [kick-out]" | CORRECTED (quote wording) | jonsvec.substack.com (fetched): "should use their shoulder or hands to stonewall the Slice Block and set the edge" | Quote fragment now matches the source: "stonewall the Slice Block [split zone's kick-out] and set the edge" |
| Heavy personnel 41.7% in 2025, first season ≥38% since NGS began in 2016; base 29.7% in 2025 vs low 20.5% in 2023 | VERIFIED | FACTS §10 (NGS, Reber) | None |
| Split-safety 32.9% (2018), 40.4% (2024), 42.0% (2025), highest since tracking began | VERIFIED | FACTS §10 (NGS) | None |
| Seattle led NFL in scoring defense 2012–2015; Carroll/Quinn Cover 3; Thomas deep middle, Chancellor in the box | VERIFIED | Wikipedia "Seattle Cover 3 defense" ("four straight years from 2012 to 2015"); "Legion of Boom" | None |
| Super Bowl LIX: Eagles 40, Chiefs 22 | VERIFIED | FACTS §1 | None |
| 2019 Ravens 3,296 rushing yards, breaking 1978 Patriots' 3,165 | VERIFIED | NFL.com (fetched) | None |
| Jackson 1,206 rushing yards, unanimous MVP 2019 | VERIFIED | Wikipedia "2019 Baltimore Ravens season" | None |
| Harbaugh fired January 2026 | VERIFIED | FACTS §0 C3, §9 | None |
| Barkley 2,005 yards, ninth 2,000-yard season | VERIFIED | NFL.com (fetched: "season total to 2,005", ninth player) | None |
| Football-technical: spill = wrong-arm the kick-out to bounce the ball; box/squeeze = outside arm free; force outside-in; alley inside force; crack-replace; plus-one; QB counts as a blocker on reads; scrape exchange; slant as front-wide gap exchange | VERIFIED (standard coaching doctrine) | Svec (above); AFCA Raby (above); consistent with 03-04, 05-01 | None |
| "Spill inside, force outside" organization | VERIFIED (general; already hedged "though staffs differ") | AFCA Raby (spill players inside, force/fold outside) | None |
| Fit chart, diagrams | VERIFIED as illustrative | Captions say typical, not one team's playbook | None |

**Counts:** VERIFIED 21 · CORRECTED 6 · SOFTENED 1 · REMOVED 0 (the unsourced "lever-spill-lever"/"fast players"
clinic wording was replaced inside the CORRECTED/VERIFIED `fitwords` fix rather than counted separately).

**Uncertain / for a human:** PFR blocks automated fetches, so Ravens/Barkley/Jackson totals were checked on NFL.com and
Wikipedia. The "Barry" mention in the PFF tree piece: Joe Barry worked under Staley (Rams 2020), not Fangio directly;
the chapter text names only Staley.
