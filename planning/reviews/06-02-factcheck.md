# Fact-check log: 06-02 Man Coverage: Cover 0, Cover 1, Robbers, and Brackets

Checked 2026-10-06 against FACTS-current.md, web sources, and nflverse participation + pbp (re-queried in the `rtg` container with the chapter's own filters). All 7 `<!-- VERIFY -->` comments are resolved and removed. Build `build_pdfs.py 06-02-man-coverage --html`: OK (22 pages).

| Claim | Verdict | Source | Change |
|---|---|---|---|
| Willie Brown: linebacker at Grambling, began jamming at the line in 1963 (with Denver) | VERIFIED | Wikipedia "Bump and run coverage"; ESPN obit (Oct. 22, 2019) | Footnote now says Brown *said* so (his own account) |
| Davis modelled bump-and-run on Wooden's UCLA full-court press | VERIFIED (attribution fixed) | ESPN obit (not in the Wikipedia article the footnote cited) | Text "Davis said he borrowed" → "Davis modelled the Raiders' version on"; footnote moves the claim to ESPN |
| Brown: 12 seasons with the Raiders (from 1967), HOF 1984, died at 78 | VERIFIED | ESPN obit; Wikipedia (Raiders 1967–78, HOF 1984) | ESPN headline/date corrected in footnote; VERIFY removed |
| Mel Blount rule 1978 (contact limited to 5 yards) | VERIFIED | Wikipedia bump-and-run / 1978 season; consistent with 06-01 | none |
| Ty Law: 3 INTs of Manning, 2003-season AFC CG, 24–14, Jan. 18, 2004 | VERIFIED | NBC Sports Boston (Curran); accesswdun AP report (Jan. 18, 2004, Gillette Stadium, 24–14) | Date sourced; VERIFY removed |
| "Just beat them up" quote (Law) | VERIFIED | Curran, NBC Sports Boston: "This was probably the most simple game plan we had. Just beat them up." | Fuller quote put in footnote |
| Curran article byline | VERIFIED | Article byline "Tom E. Curran" | VERIFY removed |
| 2004 Competition Committee illegal-contact crackdown ("Ty Law rule"); Polian (Colts president) and Dungy involved | VERIFIED | Curran article | none |
| Rule 8-4: contact allowed within 5 yards; beyond, no contact while passer in pocket with ball; 5 yards + automatic first down; Rule 8-5 = PI | VERIFIED | operations.nfl.com rulebook (Rule 8 section titles; 8-4-3 penalty); NFL video rulebook "Illegal Contact" | none |
| Seattle's 2010s Cover 3 corners pressed then played zone | VERIFIED | Bucky Brooks, NFL.com (2015): corners press single-receiver side, bail vs two | Source added to `[^sherman]` |
| Sherman usually on the defense's left, didn't shadow | VERIFIED (source replaced) | NFL.com "defining stats" (2018): "primarily lines up on the left side of the defense"; Brooks (2015) | PFF citation dropped: the PFF piece says nothing about side ("61 snaps, 41 in coverage") |
| Sherman followed Julio Jones "in the January 2017 playoffs" | CORRECTED | Kapadia ESPN (Jan. 10, 2017) is a playoff *preview*; the 30-of-46 figure is the Week 6 game (Oct. 16, 2016). Playoff shadowing appears only in a paywalled AJC recap | Text → "as against Atlanta's Julio Jones in October 2016"; footnote clarified |
| Revis 2009 under Rex Ryan held Moss (twice), A. Johnson, Owens (twice), Wayne, Ochocinco | VERIFIED | AP (Waszak, July 30, 2023); NFL.com Revis Island; PFHOF Gold Jacket piece | Jets X-Factor source (403; author unverifiable) replaced by AP |
| Ochocinco "no catches at all in their game" | CORRECTED | SI (Reiter, Jan. 7, 2010): 0 catches in Week 17, ending a 120-game streak; the teams also met in the wild-card round | "their game" → "their regular-season meeting" |
| Jets 2009 allowed 236 points, fewest in NFL | VERIFIED | Wikipedia 2009 Jets season; Rotowire/StatsCrew | VERIFY removed |
| Revis HOF Class of 2023, first year of eligibility | VERIFIED | PFHOF; AP | none |
| Surtain: 2024 AP DPOY; on Metcalf for 24 of 25 routes in 2024 Week 1 (NGS); Vance Joseph DC since 2023 | VERIFIED | Legwold, ESPN (Sept. 10, 2024); CBS Colorado | none |
| Spagnuolo: Giants DC 2007–08, SB XLII (Feb. 3, 2008) 17–14 ended 18–0 Patriots; Chiefs DC since 2019 | VERIFIED | Wikipedia SB XLII / Spagnuolo | none |
| KC Cover 0 rank top 5 every season 2019–2025, 1st in 2025 (ranks 3,2,3,3,5,2,1; 4th in 2018) | VERIFIED | Recomputed from nflverse participation | none |
| Man share by season 35.2/37.3/34.6/30.4/28.9/43.8/49.6/31.1 | VERIFIED | Recomputed (chapter filters: BLOWN/COMBO/PREVENT out). Differs slightly from FACTS §7 (28.8/41.2/48.3/30.8) because FACTS keeps those labels in the denominator | none |
| man = COVER_0, COVER_1, 2_MAN, matching `defense_man_zone_type` | VERIFIED | Crosstab 2022+2024 participation (COMBO is coded ZONE_COVERAGE) | none |
| Third-and-3–6 man ~60% both eras; first down 25.5/35.6; 3rd&11+ lowest (20.9/26.0) | VERIFIED | Recomputed | — |
| "roughly twice their first-down rate" | CORRECTED | 59.2/25.5 = 2.3× (NGS) but 60.1/35.6 = 1.7× (FTN) | → "far more than on first down (about 25 to 36%)" |
| Inside the 5: man 78–88%, Cover 0 41–62% | VERIFIED | Recomputed (87.8/77.6; 61.5/41.4) | none |
| Team man-share leaders NE 2018–19 (60.8, 67.6), MIA 2020–21, DEN 2024–25; NE 2019 ≈ two-thirds | VERIFIED | Recomputed | none |
| Cover 0 with 5+ rushers ~3 in 4 (73.4/75.3%) | VERIFIED | Recomputed | none |
| Cover 0 median time to throw "2.0 to 2.25 s, three or four tenths faster" | CORRECTED | Recomputed: all field 2.25 (NGS) / 2.10 (FTN), next-fastest 2.54 / 2.40 (gap ≈0.3 s) | → "2.1 to 2.25 seconds, about three tenths" |
| Bargain chart "between the 20s": 20+ yd gains Cover 0 13.8%, C1 10.9 … | CORRECTED | Figure code filtered only `yardline_100 > 20` (included the offense's own 1–20). With `< 80` added: C0 14.1, C1 11.0, C3 9.7, C2 7.6, Q 7.1; NGS C0 12.9, C1 12.5; median TTT C0 2.0 s | Code filter fixed to match caption; footnote numbers updated; text ("one in seven", "about 2.0 s", "nearly twice the two-high zones") now exact |
| Sacks left out of time-to-throw medians | VERIFIED | 97.6% of sacks have no `time_to_throw` | none |
| COMBO label exists from 2023 on; FTN meaning | SOFTENED | nflreadr participation dictionary lists COMBO without definition; FACTS §7 | Text now says the dictionary doesn't define it; VERIFY removed |
| BDB 2025 `pff_passCoverage` value "Cover-1", `passResult` "IN" = interception | VERIFIED | Public BDB 2025 repo (ChrisKornaros/NFL_Big_Data_Bowl_2025, plays_rf.sql: 'Cover-1', 'Cover-1 Double', passResult C/I/S/IN/R); same spelling used in 06-06 | VERIFY removed |
| BDB 2025 = 2022 season Weeks 1–9 with pre-snap frames | VERIFIED | FACTS §8 | none |
| Corn Dog TDs SB LVII beat man after return motion | VERIFIED | Consistent with 02-06 (fact-checked) | none |
| SB LVIII (Feb. 11, 2024): OT 3rd-and-4 at KC 9, play-action for Jennings, six rushers, Jones unblocked, FG, Mahomes TD drive, 25–22 | VERIFIED | Defector (Petchesky); NFL.com (Shook); NFL.com NGS (22nd blitz, Jones unblocked, errant pass over open Jennings) | — |
| "Purdy had to throw the ball away before the routes could develop" | CORRECTED | NGS/CBS: Purdy threw early to an open Jennings and the pass sailed over his head | Rewritten |
| Coverage behind that pressure was Cover 0 | VERIFIED | Purdy postgame via KNBR, in CBS Sports (Feb. 12, 2024): "They brought Zero" | "in Cover 0" + Purdy quote added; CBS added to `[^sb58]`; VERIFY removed |
| Bolton "On third down, we brought the house" | VERIFIED | Defector | none |
| Gilmore 2019: first Patriot DPOY, 6 INTs (tied for lead), 2 pick-sixes; NE No. 1 in points allowed (14.1) and total defense (275.9) | VERIFIED | Patriots.com (Feb. 1, 2020); CBS Sports | none |
| Flores Patriots assistant 2004–2018, Miami HC 2019–2021 | VERIFIED | Wikipedia (Brian Flores) | none |
| Chris B. Brown books (2012, 2015); Cody Alexander MatchQuarters | VERIFIED | Publisher listings (well established) | none |
| Football-technical claims (Cover 1/0 structure, leverage follows help, robber 8–12 yd, rat 5–8 yd, banjo in/out rules, bracket shapes, Cover 0 inside leverage) | VERIFIED (general) | Standard coaching usage; consistent with 06-01/06-06 and the Brooks NFL.com piece; ranges presented as varying by team | none |

**Counts:** VERIFIED 33 · CORRECTED 7 · SOFTENED 1 · REMOVED 0.

Uncertain / for a human: whether Sherman also shadowed Jones in the Jan. 14, 2017 playoff (an AJC recap says "frequently"; paywalled, so the text now cites only October 2016). PFR was not fetched (blocked in earlier checks); 2009 Jets points allowed came from Wikipedia and stat aggregators.
