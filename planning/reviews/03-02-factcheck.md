# Fact-check log: 03-02 Zone Running

Checked 2026-10-06 against FACTS-current.md and web sources. All 9 `<!-- VERIFY -->` comments resolved and removed. Build `build_pdfs.py 03-02-zone-running`: OK (21 pages).

| Claim | Verdict | Source | Change |
|---|---|---|---|
| Colts' "stretch" a Manning-era signature under Howard Mudd, with Edgerrin James and Joseph Addai | VERIFIED | Farrar, Sports Press NW 2010; X&O Labs; Wikipedia (Mudd, Colts 1998–2009) | Footnote rewritten with real sources (old one leaned on an unchecked book cite). Dropped "from three-receiver sets" (no source found tying the stretch to 3-WR sets); named Mudd in text |
| Low-block rule wording: "legal only ... inside the area between the tackles ... before the ball has left that area" | CORRECTED | ESPN 2021 rule-change guide; NFL health & safety rule-change list | Since 2021, low blocks on scrimmage plays are legal only inside the **tight end box** (2 yds outside each tackle, 5 yds either side of the LOS), which is wider than "between the tackles." Text now says that |
| Low blocks from behind or toward own goal line illegal | VERIFIED (dated) | NFL health & safety list; AP Mar 2013 | Added "(since 2013)" and the "peel-back" name |
| All chop blocks illegal since 2016 | VERIFIED | NFL.com Mar 22, 2016 | Footnote source added |
| Defenders criticized Denver's cut blocks "in the Gibbs era" | CORRECTED / narrowed | AP "Cutting remarks irk Shanahan," Oct 29, 2004; Grantland (Brown) 2012 | The best-documented criticism (Foster on Tony Williams, MNF 2004; Lewis, Cowher, Michaels/Madden) came in 2004, after Gibbs left for Atlanta. Text now says "Mike Shanahan's Denver lines" and names that 2004 episode, which is confirmed |
| Bash = "back away"; RB runs away from zone flow, QB becomes inside runner; answer to squeeze-scrape | VERIFIED | USA Football blog; Buckeye Huddle 2023 | Footnote `[^bash]` added |
| Gibbs: Denver OL coach under Shanahan from 1995 (tenure 1995–2003; also 1984–87); died 2021 | VERIFIED | Wikipedia; PFT Jul 12, 2021 (died aged 80) | Footnote now gives tenure and death date |
| Gibbs's clinic tapes "copied and passed around for decades" | SOFTENED | CoachTube listing of Gibbs clinic videos | Now reads "circulated widely among coaches and are still sold as coaching videos" |
| Gibbs system: light linemen, backside cuts, one-cut backs, bootleg pairing | VERIFIED | Chris B. Brown, Grantland, Jan 10, 2012 | Cited in `[^bbb]`, `[^cutcrit]`, `[^gibbstapes]` |
| Broncos won Super Bowls after 1997 and 1998 seasons | VERIFIED | Wikipedia (Gibbs: XXXII, XXXIII) | none |
| Terrell Davis 6th-round pick, 2,008 yds in 1998, MVP | VERIFIED | PFHOF; Wikipedia (196th overall, 1995) | Footnote detail added |
| Later Denver 1,000-yd rushers, several mid/late picks | VERIFIED | Westword; FantasyNerds; Wikipedia (Droughns) | Footnote lists Gary 1999 (R4), Anderson 2000/2005 (R6), Portis 2002–03 (R2), Droughns 2004 (R3, DET), Bell 2006 (R2) |
| Kubiak: Shanahan's Denver OC, Houston HC, back to Denver, won SB 50 after 2015 | VERIFIED | Wikipedia (Kubiak OC 1995–2005, HOU 2006–13); NFL.com | none |
| Kyle Shanahan under Kubiak in Houston, under his father in Washington, 49ers HC 2017 | VERIFIED | Wikipedia (HOU WR coach 2006, OC 2008–09) | none |
| McVay and LaFleur from Kyle Shanahan's staffs | VERIFIED | CBS Sports (2013 Washington staff) | Source added |
| Klint Kubiak called plays for 2025 Seahawks, Raiders HC 2026 | VERIFIED | FACTS-current §1, §9 | none |
| 49ers 37–20 over GB, Jan 19, 2020; 8 passes; Mostert 220 yds, 4 TD; Mostert undrafted | VERIFIED | ESPN; AP (Garoppolo 6 of 8, 77 yds) | ESPN source added |
| Elway was Denver's QB in 1998 | VERIFIED | common record / PFR | none |
| Super Bowl LX: SEA 29–13 NE; Walker 27–135, MVP | VERIFIED | FACTS-current §1 | none |
| Seattle 2025 under Kubiak: outside zone, two-TE/tight formations, run-to-boot pairing | VERIFIED | Everett Herald Aug 13, 2025; NFL.com NGS trend watch (condensed 2nd-highest, 12 personnel 7.5 YPP) | Footnote `[^sea]` added |
| McCaffrey 2023: led NFL with 1,459 rush yds, AP OPOY | VERIFIED | NFL.com; 49ers.com | NFL.com source added |
| *Run to Daylight!*, Lombardi with W. C. Heinz, Prentice-Hall 1963 | VERIFIED | archive.org scan; publisher listings | none |
| BDB 2025 `plays.csv` has `pff_runConceptPrimary`; outside zone value `OUTSIDE ZONE` | VERIFIED | Public repos (header probe; cadenweigel/NFLPreSnap summary shows top value OUTSIDE ZONE, 2,450 of 9,071) | Footnote `[^bdbcol]` added; code's case-insensitive match is right |
| BDB 2025 = 2022 season, weeks 1–9, pre-snap frames | VERIFIED (weeks LIKELY) | FACTS-current §8 | none |
| Chart caption: 49ers' advantage "largest on outside runs" | CORRECTED (narrowed) | Recomputed in container: SF−league EPA gap End +0.060 vs about +0.016 elsewhere; success-rate gap is largest at Guard | Caption now says "EPA advantage" |
| Prose: End is the only lane with positive league EPA (+0.002), SF middle still below zero, SF rank, "nearly every offense" below zero | VERIFIED | Recomputed: league End +0.002, Middle −0.081; SF End +0.062, Middle −0.065; SF 6th (−0.026 vs −0.057); only BAL positive | Numbers are inline-computed anyway |
| nflverse run_location/run_gap semantics; success = EPA > 0 | VERIFIED | nflverse pbp data dictionary | none |
| Technique numbers (5 = tackle outside shoulder, 3 = guard outside, 1 = shade on center, 4i, 9, 0) | VERIFIED | standard technique numbering (03-01) | none |
| Two-high defenses rising in the 2020s | VERIFIED | FACTS-current §10 (NGS 2018 32.9% to 2025 42.0%) | none |

Counts: VERIFIED 24 · CORRECTED 3 · SOFTENED 1 · REMOVED 1 (the "three-receiver sets" detail).

Still uncertain / for the editor:
- The bang-bend-bounce *order* for outside zone ("bounce, bang, bend") differs by coach; the chapter already says so, and its footnote cites Brown generally rather than a specific page.
- Lombardi sweep + "run to daylight" footnote links the HOF bio; the bio wasn't fetched to confirm it mentions the sweep.
- Pro Football Reference returned 403 to the fetcher; PFR links kept as given, and the facts were cross-checked elsewhere.
