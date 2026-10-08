# Fact-check log: 13-05 Tracking Data and the Big Data Bowl

Checked 2026-10-08 against FACTS-current.md, web sources, Crossref, and nflverse data (recomputed in the `rtg` container). All 12 `<!-- VERIFY -->` comments are resolved and removed. Build `build_pdfs.py 13-05 --html`: OK (48 pages).

**Important for FACTS-current §8:** the 2027 Big Data Bowl **was announced on Oct 7, 2026**. That contradicts the "not announced as of 2026-10-06" row. The Kaggle page `nfl-big-data-bowl-2027` is live. Its theme is linking 10 Hz Combine sensor tracking (2023-2025 Combines) to later regular-season game performance. Prize $100k, entries close Jan 6, 2027. I updated the chapter but did not edit FACTS-current.

| Claim | Verdict | Source | Change |
|---|---|---|---|
| Two chips per player, one in each shoulder pad | CORRECTED | operations.nfl.com NGS page: "2-3 RFID tags installed into the players' shoulder pads" | Now "two or three small radio chips in his shoulder pads"; "More than one chip per player…" |
| 20-30 receivers per stadium; about 10 times a second | VERIFIED | operations.nfl.com NGS page | Footnote expanded |
| Ball can carry a chip | VERIFIED | operations.nfl.com ("in the ball") | none |
| 2014 trial in 17 stadiums | VERIFIED | ESPN, Seifert, Dec 11 2014 ("17 stadiums… 20 receivers") | Moved into new `[^rollout]` |
| League-wide from the next season (2015) | VERIFIED | CBS Sacramento, Sept 1 2015 ("all 31 NFL stadiums will have sensors") | Added `[^rollout]` |
| Accuracy "within a few inches" | CORRECTED | Zebra via CBS, "margin of error of less than six inches"; NFL "within inches" | Now "within about six inches" + `[^accuracy]` |
| NBA SportVU in every arena from 2013-14 | VERIFIED (URL CORRECTED) | pr.nba.com/nba-stats-llc-partnership (Sept 5 2013). The old nba.com URL returned 404 | URL replaced |
| MLB Statcast in all parks in 2015 | VERIFIED | mlb.com/glossary/statcast | Quote added |
| Kaggle: accept the rules before download; the rules restrict use and sharing | VERIFIED (general) | Kaggle competition pages (rules tab needs a login; the exact clause could not be fetched) | Footnote now says terms differ by edition; no specific clause claimed |
| Hash marks at y = 23.6 / 29.8; field 53⅓ yd | VERIFIED | NFL hashes 70'9" from the sideline = 23.58 yd | none |
| yd/s × 2.05 = mph | VERIFIED | arithmetic (1 yd/s = 2.045 mph) | none |
| Fastest ball carriers "touch 11 or more (22-plus mph)" each season | SOFTENED | NGS season tops are about 22-23 mph; 11 yd/s = 22.5 mph | Now "touch about 11 (around 22 mph)" |
| BDB columns, events, `frameType`, `snap_direct`; 2026 snake_case input/output files | VERIFIED | FACTS §8; public BDB code using `ball_snap`/`snap_direct` (GitHub) | none |
| NGS separation = distance to the nearest defender at catch or incompletion | VERIFIED | nflverse NGS dictionary | none |
| Tee Higgins lowest 2025 avg separation; JSN OPOY | VERIFIED | Recomputed: Higgins 1.85 (next Evans 1.92); FACTS §1 | none |
| Target depth vs separation r and YoY stability | VERIFIED | Recomputed: r = −0.69, slope −0.12; YoY r = 0.73 (n = 89) | none |
| PFF shift/motion 63.9% (2025) vs 43.0% (2018) | VERIFIED | FACTS §10; PFF, Carragher, Feb 23 2026 | none |
| FTN `is_motion` "before or at" the snap "which is why" it runs lower than PFF | CORRECTED (logic) | FACTS C7/§10: lower because the definitions differ (FTN 55.1% vs PFF 63.9% in 2025) | Rewritten: does not count shifts the same way; 55% vs 64% |
| ESPN pass rush win rate = beating the blocker within 2.5 s | VERIFIED | ESPN win-rate explainer | none |
| 2022 W1-9 two-high shares: NE and MIA lowest, KC and BUF highest | VERIFIED | Recomputed: NE 23%, MIA 25%; BUF 60%, KC 60% | Footnote: NGS labels start in 2018, FTN from 2023 |
| NGS split-safety 32.9% (2018), 42.0% (2025), Cover 4 17.2% | VERIFIED | NFL.com, Reber/NGS; FACTS §10 | none |
| NGS coverage labels come from tracking | VERIFIED | AWS ML Blog: NGS classifier "identifies the defense coverage scheme based on the player tracking data" (2022) | Text now "coverage labels come from a model run on tracking data" + `[^ngs-coverage]` |
| FTN 2025 two-high about 43% | VERIFIED | FACTS §10 (43.3%) | none |
| Lopez "led the group… a statistician from academia"; BDB "largely the creation" of his group | CORRECTED | AWS Q&A (Mar 2023): "co-creator of the Big Data Bowl"; ops.nfl.com: "senior director of football data & analytics"; Bates Student: former Skidmore statistics professor | Now "its co-creator is Michael Lopez, a former statistics professor who now leads…" |
| "Only a few dozen people inside teams were allowed to work on it" | REMOVED | No source | Now "a data set that almost nobody outside the league and its clubs could study" |
| "Many past participants hired by NFL clubs" | CORRECTED | ops.nfl.com: "more than 75 Big Data Bowl participants have been hired in data and analytics roles in sports" | Uses the league's figure and wording |
| Finalists present at the Combine | VERIFIED | ops.nfl.com announcements | none |
| 2019: 2017 season, first six weeks | VERIFIED | Deshpande & Evans arXiv:1910.12337 (91 games, Weeks 1-6 2017) | Source added to `[^bdb-ops]` |
| 2020: rushing; 2017-18 runs; scored live on 2019 | VERIFIED (made specific) | ops.nfl.com results (Weeks 13-17 of 2019); Zoo reproduction shows 2017 and 2018 seasons in training | Table now "2019 Weeks 13-17" |
| 2021: defending the pass, 2018 pass plays | VERIFIED | ops.nfl.com third-annual announcement | Source added |
| 2022: special teams 2018-2020 | VERIFIED | ops.nfl.com fourth-annual announcement | Source added |
| 2023: linemen on pass plays, 2021 Weeks 1-8 | VERIFIED | CMU workshop slides; STRAIN paper (first 8 weeks of 2021). The NFL announcement text says "2022 season" (the competition season) | Source added |
| 2024: tackling, 2022 Weeks 1-9 | VERIFIED | ops.nfl.com sixth-annual announcement | Source added |
| 2025: pre-snap; Bajaj & Sandwar (NYU) "Exposing Coverage Tells in the Pre-Snap"; NGS disguise model credits them | VERIFIED | NYU SPS; NYU Stern; NFL.com NGS 2025 metrics article | none |
| 2026: two tracks; Weeks 14-18 2025 scoring; Ferraz (Rice) "Ghostbusters…"; files are 2023 W1-18 | VERIFIED | FACTS §8; ops.nfl.com | "most recent edition" → "2026 edition" |
| 2027 "not announced as of early October 2026" | CORRECTED | Kaggle `nfl-big-data-bowl-2027` (live); Yahoo Sports Oct 7 2026; Kaggle on X (deadline Jan 6 2027) | Table row filled in, heading "2019 to 2027", sentence plus `[^bdb2027]` added in "What is public"; stale footnote sentence removed |
| The Zoo: Singer & Gordeev, Austrian; offense-defense pair network; NGS xRush yards | VERIFIED | NFL.com "Intro to Expected Rushing Yards"; Zoo write-up quoted in a public reproduction ("defense-offense pairs of players") | Source added to `[^bdb2020]` |
| "Judges are coaches and league staff" | SOFTENED | No judge list found | Now "league and club football staff" |
| Deshpande & Evans EHCP, JQAS 16(2), 2020, DOI 10.1515/jqas-2019-0050; from the 2019 BDB | VERIFIED | Crossref (pp. 85-94); arXiv ("work done for the NFL 2019 Big Data Bowl") | Pages and arXiv note added |
| STRAIN, *The American Statistician* 2024, DOI 10.1080/00031305.2024.2350401 | CORRECTED | Crossref: DOI **10.1080/00031305.2023.2242442**, vol. 78 no. 2, pp. 199-208 | DOI fixed; CMU source for the 2023 BDB data added |
| Lopez JQAS intro title "…tracking datasets in sports" | CORRECTED | Crossref: "…an introduction to a special issue on tracking data in the National Football League", 16(2) 73-79 | Title fixed |

**Counts:** VERIFIED 30 · CORRECTED 10 · SOFTENED 2 · REMOVED 1.

**Uncertain:** the exact Kaggle data-use clause (the rules tab needs a login), so the text keeps only the general claim. Whether Nguyen et al.'s 2023 finalist entry was STRAIN itself: the chapter claims only that STRAIN came from the 2023 edition's data, which is verified.
