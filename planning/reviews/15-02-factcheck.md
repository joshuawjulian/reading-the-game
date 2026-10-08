# Fact-check log: 15-02 Film Study, Charting, and Scoring Yourself

Checked 2026-10-08 against FACTS-current.md, web sources, and nflverse data. I re-queried the data in the `rtg` container by running the chapter's two data cells and dumping SBX, SEASON, the strip-sack row, every drive of Super Bowl LX, the per-game log scores, and the calibration bins. All 5 `<!-- VERIFY -->` comments are resolved and removed. There are now 16 footnotes, each referenced exactly once (script check). Build `build_pdfs.py 15-02-film-study-and-charting --html`: OK (27 pages).

| Claim | Verdict | Source | Change |
|---|---|---|---|
| SB LX: Feb 8, 2026, Levi's Stadium, SEA 29–13 | VERIFIED | FACTS §1; nflverse game `2025_22_SEA_NE` | none |
| SEA led 12–0 late in Q3, all Myers FGs | VERIFIED | FACTS §1 (corrected line score); pbp drives (SEA FG drives Q1 15:00, Q2 14:10, Q2 2:50, Q3 14:02) | none |
| Seattle sacked Maye 6 times; 5 of the 6 with four rushers; 4 rushers on 45 of 53 NE dropbacks | VERIFIED | FACTS §1 (6 sacks); chapter code re-run (SBX) | none |
| Strip-sack: 3rd&6 at NE 44, 0:16 Q3, NE down 12; 11 pers, shotgun 1 back, motion; dime, box 6; 4 rushers; 2_MAN | VERIFIED | pbp/FTN/participation row (desc "(:16) (Shotgun) 10-D.Maye sacked at NE 37 for -7 yards (58-D.Hall). FUMBLES … RECOVERED by SEA-91-B.Murphy at NE 37") | none |
| Hall #58 forced it, Byron Murphy II #91 recovered at NE 37 | VERIFIED | same pbp desc | none |
| "Five snaps later" SEA's first TD, 16-yd pass to AJ Barner, 19–0 | VERIFIED | pbp: SEA drive 11, 1, inc, 9, TD (13:29 Q4); all earlier SEA drives FG/punt | none |
| Board caption: NE's first nine drives ≤ 8 snaps, eight punts then the strip-sack; SEA scored FGs on four of its first seven drives | VERIFIED | Drive dump (NE 8,4,3,3,6,3,3,3,5 snaps; SEA FG, punt, punt, FG, punt, FG, FG) | none |
| NE trailed from Q1 on and spent Q4 chasing three scores; SEA ahead all night | VERIFIED | pbp (SEA FG on the opening drive; 19–0 at 13:29 Q4) | none |
| Walker 27 carries, 135 yards | VERIFIED | FACTS §1; SBX | none |
| SEA 2025 staff Macdonald / Kubiak / Durde; NE OC McDaniels | VERIFIED | FACTS §1, §9 | none |
| Seattle's two-high: 73% in the SB vs 52% in the regular season (league 43%); rushed four on 76% of dropbacks (league 70%) | VERIFIED | Chapter code re-run; league two-high agrees with FACTS §10 nflverse 43.3% | none |
| Participation covers the playoffs (the SB is labelled) | VERIFIED | SB rows carry coverage labels (51 labelled) | none |
| Panthers 2025: 17 regular-season games plus the wild-card loss to the Rams (18 games, 1,054 snaps) | VERIFIED | FACTS §2 (Rams 34–31 Panthers); N_GAMES = 18, REG+POST | none |
| Example-log numbers (hit 74%; always-pass 59%; d&d rule 60%; xpass 66%; 70–75% band 60%; 90%+ band 85%; Murphy split; readers A and B) | VERIFIED | Chapter code re-run (all inline values are computed) | none |
| Calibration caption: early groups "about ten points" short in the 70s and 80s | CORRECTED | Re-run bins for games 1–8: 70% → 52%, 75% → 65%, 80% → 65%, 85% → 70% (13–15 points short when paired) | Changed to "about fifteen points" |
| Calibration caption: early reader put about half his calls at 90%+ | VERIFIED | 49.0% of the 506 calls in games 1–8 | none |
| Progress caption: 43 to 76 calls a game; first two games easier; beats xpass in most games | VERIFIED | Per-game re-run (n 43–76; hit rate 78% and 83% in games 1–2; beats xpass Brier in 12 of 18) | none |
| Drill 3 caption: A at 90%+ on most calls; B never above 85%, most calls 50–65% | VERIFIED | A 66% at ≥ 90%; B max 0.85, 70% at ≤ 65% | none |
| "One game … every bar would span thirty points" | CORRECTED (precision) | Wilson 95% interval for n = 12: about 36 points wide at p = 0.9 and 46 at p = 0.6 | "more than thirty points" |
| xpass "fitted on seasons that include 2025, so it has a small home advantage" | CORRECTED | nflfastR-data `models/_dropback_model_data.R`: `seasons <- 2006:2019` | Table caption now says it was trained on 2006–2019 and has never seen these snaps; source added to fn `sim` |
| Coaches film "within a day or two" (VERIFY 1) | CORRECTED (precision) | NFL+ Help Center "How do I watch Coaches Film": "available 24-36 hours after the completion of each game" (quoted through search; the page returns 403 to fetches); Premium is required | Text: "24 to 36 hours after the final whistle"; help-page URL added to fn `nflplus` |
| All-22 sold to fans since 2012; in NFL+ Premium in 2026; archive back to 2022 per the 2024 description | VERIFIED | 01-06 fact-check; Bills 2012; NFL.com 2024 NFL Pro launch | none |
| nflverse in-season pbp timing (VERIFY 4): "within a day or so" | CORRECTED (precision) | nflverse-pbp `update_data.yaml` cron jobs (TNF, Sunday early and late, SNF/MNF, daily 09:03 UTC, Sep–Feb); matches the 13-04 fact-check | "within hours" in both places; footnote rewritten with the workflow URL |
| FTN charting "updated weekly during the season" | CORRECTED (precision) | nflverse-ftn workflows poll every six hours (13-04 fact-check); FACTS §7 says "weekly" (the 2026 file was updated Oct 5) | "arrives game by game during the season"; fn `timing` rewritten |
| Participation (personnel and coverage) only after the season, around February | VERIFIED | FACTS §7 | none |
| Glenn Brier at the U.S. Weather Bureau in 1950 (VERIFY 2) | VERIFIED | Wikipedia "Glenn W. Brier": Office of Meteorological Research, U.S. Weather Bureau, from 1939 into the 1980s; "statistician, weather forecaster" | "statistician and meteorologist"; source added to fn `brier` |
| Brier 1950, *Monthly Weather Review* 78(1): 1–3; the original version runs 0–2 | VERIFIED | Wikipedia (DOI 10.1175/1520-0493(1950)078<0001:VOFEIT>2.0.CO;2); scores library docs | none |
| Murphy 1973, *J. Applied Meteorology* 12: 595–600 (vector partition) | VERIFIED | Standard citation (AMS, JAM 12(4)) | none |
| Murphy & Winkler 1977, *JRSS C (Applied Statistics)* 26: 41–47 | VERIFIED | Standard citation (26(1)) | none |
| Wilson 1927, *JASA* 22: 209–212 | VERIFIED | Standard citation (22(158)) | none |
| Cohen 1960, *Educ. Psych. Meas.* 20: 37–46 | VERIFIED | Standard citation (20(1)) | none |
| Simons & Chabris 1999, *Perception* 28: 1059–1074; about half missed the gorilla | VERIFIED | Standard citation; about 46% failed to notice overall | none |
| Good Judgment Project: IARPA tournament from 2011, scored with Brier; *Superforecasting* (Crown, 2015) ch. 3 | VERIFIED | IARPA ACE program (2011–15); ch. 3 "Keeping Score" | none |
| Silver, *Signal and the Noise* (Penguin, 2012) ch. 4 on NWS calibration | VERIFIED | Ch. 4 is the weather chapter (NWS calibration vs. the commercial "wet bias") | none |
| "[Brier is] what forecasting tournaments use for people" | SOFTENED | Some platforms use log scores; GJP/IARPA used Brier | Now "what the best-known forecasting tournament for people, the one behind *Superforecasting*, used" |
| Log loss vs Brier numbers (95% miss: 0.90 / 3.0; 99%: 0.98 / 4.6) | VERIFIED | Arithmetic | none |
| Three-call Brier table = 0.40; confident miss 20× the hit | VERIFIED | Arithmetic (1.21/3; 0.81/0.04) | none |
| Walsh, Billick and Peterson, *Finding the Winning Edge* (1997) | VERIFIED | Sports Publishing, ISBN 1571671722, Dec 1997 (a review site gives 1998) | none |
| Brown, *Art of Smart Football* (2015); Layden, *Blood, Sweat and Chalk* | VERIFIED | Course bibliography | none |
| Clinics: AFCA convention; "Nike Coach of the Year and Glazier clinics" still run (VERIFY 3) | CORRECTED | AFCA 2026 convention (Charlotte, Jan 11–13, 2026); Glazier 2026 calendar of 27 clinics; Coaches Insider lists 2026 "Coach of the Year Clinics" (Nike branding on series through 2024) | Text: "Glazier Clinics and the Coach of the Year Clinics (long Nike-branded)"; new fn `clinics` |
| Ted Nguyen "at *The Athletic*" (VERIFY 5) | REMOVED (outlet) | Could not confirm a 2026 Athletic byline (nytimes.com blocks fetches); 2026 activity found is podcasts and social media | "Ted Nguyen's All-22 breakdowns" with no outlet named |
| Cody Alexander MatchQuarters; Kollmann; JT O'Sullivan QB School; Greg Cosell at NFL Films | VERIFIED | Well-established public profiles | none |
| Ben Baldwin explains the EPA and xpass models | VERIFIED | 13-04 fact-check (xpass author; OSF write-ups) | none |
| Big Data Bowl every year since 2019; 2026 = eighth, ball in the air, 2023 data; 2027 not announced; fall launches | VERIFIED | operations.nfl.com BDB page ("2019-2025 Big Data Bowls", eighth annual); search on 2026-10-08 found no 2027 announcement; FACTS §8 | none (the footnote's "as of October 6" date still holds) |
| Explosive play = run of 10+, pass of 20+ | VERIFIED | Matches the analysts' convention in the 13-02 glossary | none |
| 60–65 offensive snaps a side | VERIFIED | NFL average; SB LX had 66 NE and 71 SEA runs and dropbacks | none |
| Football technique (2-Man trail technique on the inside hip; power's backside end left unblocked, BSG pull, FB kick-out; off corners with outside leverage bail in Cover 3; box definition) | VERIFIED | Consistent with 03-03, 06-02, 06-03, 06-06 | none |
| Strip-sack routes, protection, Y motion, 3.3 s timing | VERIFIED (labelled) | Text and captions call these illustrative | none |

**Counts:** VERIFIED 34 · CORRECTED 8 · SOFTENED 1 · REMOVED 1.
