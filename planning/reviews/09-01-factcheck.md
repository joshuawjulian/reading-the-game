# Fact-check: 09-01 Field Goals, Extra Points, and the Punting Game

Checked 2026-10-08 against FACTS-current.md, nflverse play-by-play (1999–2025, queried in the rtg container), the NFL rulebook/penalty tables (operations.nfl.com), and the sources linked below. All 8 `<!-- VERIFY -->` markers were resolved and deleted. The chapter rebuilds cleanly (`build_pdfs.py 09-01-kicking-and-punting --html`: OK).

**Totals:** 35 VERIFIED · 9 CORRECTED · 2 SOFTENED · 0 REMOVED

| Claim | Verdict | Source | Change |
|---|---|---|---|
| Goal posts on the end line since 1974 | VERIFIED | Wikipedia, 1974 NFL season | none |
| Crossbar 10 ft, 18'6" wide; uprights 35 ft above; hashes 18'6" apart | VERIFIED | NFL Rulebook Rule 1 (already cited) | none |
| "A kick from either hash is lined up just outside one upright" | CORRECTED | Same geometry: hash and upright are both 9'3" from center | now "lined up directly with one upright" |
| Missed FG: spot of kick, or the 20 if from inside the 20 | VERIFIED | Rule 11-4-2 (already cited) | none |
| "Add 18": share of attempts at LOS+18 | VERIFIED | nflverse (computed in chapter) | none |
| No 60+ yd FG made 1999–2005 | VERIFIED | nflverse query: zero makes ≥60 in 1999–2005 | none |
| Gogolak, Hungarian-born, first soccer-style kicker in pro football, AFL Bills 1964 | VERIFIED | profootballdaly.com "When soccer invaded football"; Cornell HOF | footnote replaced: it cited the PFHOF home page, but Gogolak is not in the HOF |
| Last straight-on kickers left in the 1980s | VERIFIED | Moseley retired in 1986 (SI Vault 2018; Wikipedia) | Moseley added to footnote |
| 2025 K-ball change: 60 balls before preseason, prepared like QB balls; previously a 60-minute pregame window | VERIFIED | Fox Sports / Vikings.com (already cited); American Football International | none |
| Denver air "roughly 15% thinner" | VERIFIED | US Standard Atmosphere: density ratio about 0.855 at 1,600 m | none |
| Dempsey 63 (1970) record for 43 years; tied by Elam 1998, Janikowski 2011 (Denver) and Akers 2012 (Green Bay) | VERIFIED | ESPN longest-FG list (updated Oct 2026); nflverse shows the 2011 and 2012 kicks with venue and date | footnote expanded; VERIFY removed |
| Prater 64, Denver, Dec 2013 | VERIFIED | nflverse; CBS | none |
| Tucker 66: Sept 26 2021 at Detroit, trailing 17–16, 4th-and-19 completion to DET 48, 3 s left, off the crossbar, won 19–17; snapper Moore, holder Koch | VERIFIED | nflverse play-by-play (desc: "Center-46-N.Moore, Holder-4-S.Koch"); CBS/SI (cited) | none |
| Tucker 13 seasons, released May 2025, 10-week suspension | VERIFIED | Wikipedia; ESPN | footnote date corrected from May to June 2025 (the ban was announced June 26) |
| Tucker's 2026 status | CORRECTED (added) | Pro Football Rumors: workouts with NO and IND (late 2025) and NYJ (Sept 2 2026); still unsigned | sentence added: unsigned when the 2026 season began |
| Little 68: Nov 2 2025 at Las Vegas, end of the first half, Jaguars won 30–29 in OT | VERIFIED | CBS (cited); nflverse (Q2, 0:04) | none |
| Little 67 (Jan 4 2026 vs TEN) is the longest outdoor FG | VERIFIED | CBS, "longest outdoor kick" (Jan 2026); ESPN list; nflverse: no longer outdoor make since 1999 | footnote now cites CBS; VERIFY removed |
| 1.3 s operation (pro range 1.2–1.35) | VERIFIED | Baltimore magazine (Tucker); Kicking System; Scouting Academy (about 1.2 s) | none |
| Snap "0.35–0.4 s" | SOFTENED | Published figures conflict (0.5+ s; 0.7–0.75 s, which looks like a punt figure); physics gives 0.4–0.5 s at 35–45 mph | now "roughly 0.4 seconds"; footnote explains the approximation |
| FG/try defensive formation rules (snapper, six per side, no pushing) | VERIFIED | Rule 9-1-3 (writer checked the 2026 text) | none |
| 2017 leaping ban | VERIFIED | Seahawks.com 2017; 2026 penalty table lists Leaping at 12-3-1(o),(r) | none |
| No tee on a FG or try | VERIFIED | Rule 11-3-2(a) | none |
| May 2015 vote 30–2, try kick from the 15 (33 yd), two-point try at the 2, defense can score 2; 2014 preseason test | VERIFIED | CBS Boston (cited) | none |
| Punt: about 0.7 s snap, about 2.0 s snap-to-kick, punter 14–15 yd, 4.5–5 s hang | VERIFIED | Scouting Academy glossary (1.8–2.0 s; 14 yd) | none |
| Ray Guy, Raiders 1973–86, first pure punter in the HOF (2014) | VERIFIED | PFHOF bio | none |
| 1974 release rule: all barred first, then the end men freed after scrimmages showed coverage arriving 12–13 yd away | VERIFIED | Wikipedia, 1974 NFL season, summarizing SI Vault Dec 16 1974 (vault URL now returns 404) | none |
| College allows release at the snap | VERIFIED | NCAA rules (no scrimmage-kick release restriction) | none |
| Gunner voluntarily out of bounds: 5 yd | VERIFIED | Penalty table 9-1-5 | none |
| "One who has been pushed out must come back in at once before he can touch the ball" | CORRECTED | Rule 9-2-3: a kicking player who has been out of bounds for any reason may not be first to touch (illegal touching, 5 yd) | text and footnote rewritten |
| Fair-catch kick "appears about once a decade" | CORRECTED | ESPN Dec 19 2024: Dicker's 57-yarder was the first make since Wersching in 1976; the last attempt before that was Slye in 2019 | now "so rare that Dicker's 57-yarder (Dec 2024) was the first made since 1976"; new footnote [^fckick] |
| Bennett, an Australian rules player, punted for San Diego from 1995 | VERIFIED | ESPN AFL; Wikipedia | footnote replaced: the ESPN URL was wrong/unconfirmed |
| ProKick Australia (Chapman and Smith) | SOFTENED | Sources give 2007 or 2008 | footnote gives both years; prose names no year |
| Fair-catch signal; no block after signal; invalid signal 5 yd | VERIFIED | Rule 10-2 (writer checked) | none |
| KCI 15 yd from the spot, signal or not | VERIFIED | Rule 10-1-1 | none |
| Running into kicker 5 yd; roughing 15 yd + auto first down | VERIFIED | Penalty table 12-2-12 | none |
| Airborne gunner batting the ball from over the end zone; first-touching spot never inside the 1 | VERIFIED | Rule 9-2-2 Note (quoted on officiating forums) | none |
| Muff: kicking team may recover, not advance; first down | VERIFIED | Rule 3 and Rule 9-3-2 (writer checked) | none |
| Predict 3: kicking team recovering an untouched punt "would have been illegal" | CORRECTED | Rule 9-2-2: first touching is a violation, not illegal; receivers take the spot | reworded as first touching/downing |
| Punt touchback at the 20; kickoff touchback at the 35 | VERIFIED | FACTS-current §3 | none |
| Aubrey: Toronto FC first-round pick 2017 (21st overall), Birmingham Stallions | VERIFIED | Toronto FC release; CBS | none |
| Aubrey "then a tryout in Dallas in 2023" | CORRECTED | ESPN/Cowboys.com: signed from the USFL in July 2023 | now "a contract with Dallas in July 2023" |
| Aubrey 35 straight to start his career (record); 14 makes of 50+ in 2024 (record) | VERIFIED | Guinness/CBS; nflverse (first miss was a block on his 36th attempt, Week 18 2023) | none |
| Seahawks fake: Jan 18 2015, trailing 16–0 in Q3, from GB 19, Ryan to Gilliam for 19 yd, Seattle won 28–22 in OT | VERIFIED | Seahawks.com recap; nflverse (score 16–0 at the snap) | footnote now has the specific recap URL |
| Gilliam "a reserve offensive tackle who had reported as an eligible receiver" | CORRECTED | Seahawks.com: a rookie tackle who "lined up as an eligible receiver" | wording fixed |
| Colts fake punt, Oct 2015 vs NE: most players shifted to one side, snap to safety Colt Anderson, loss of 1, illegal formation declined | VERIFIED | nflverse; ESPN Colts blog; SI/AP Oct 19 2015 (4th-and-3, trailing 27–21, lost 34–27) | footnote sources added |

## Left as is (general claims, not specifically sourced)

- College announcers' "add 17", the "Peter!" warning, an edge rusher needing about 1.5 s, and the coaching descriptions (protection rules, vices usually cornerbacks, lanes about 5 yd wide). All are standard coaching knowledge and are worded as typical.
- Every computed statistic (`S[...]`) comes from nflverse in the chapter code. Fake and muff counts are already marked approximate.
- Rule article numbers for 9-1-3, 10-1, 10-2, 11-3 and 11-4-2 come from the writer's check of the 2026 rulebook. operations.nfl.com only serves the TOC and penalty table as HTML, and that table confirms 9-1-5, 12-2-12 and 12-3-1.
