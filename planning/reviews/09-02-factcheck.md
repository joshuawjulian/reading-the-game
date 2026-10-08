# 09-02 Kickoffs, Returns, and the Dynamic Kickoff: fact-check

Checked 2026-10-08. Main primary source: NFL, *2026 Official Playing Rules* (PDF linked from operations.nfl.com/the-rules/nfl-rulebook/),
https://static.www.nfl.com/image/upload/fl_attachment/league/tqivdkzt9mu6wdgsh1ku.pdf, Rule 6. Data claims were re-run
from the chapter's own nflverse code in the rtg container. All 11 `VERIFY` comments are resolved and deleted. The chapter builds (`build_pdfs.py`, 18 pages).

| Claim | Verdict | Source | Change |
|---|---|---|---|
| Kickoff from own 35; safety kick from the 20, may be a punt | VERIFIED | 2026 rulebook 6-1-1, 6-1-2 | none |
| Kickoff spot 40 to 35 (1974), to the 30 (1994), back to the 35 (2011) | VERIFIED | Wikipedia "Kickoff (gridiron football)" (cites ESPN, NFL.com, PFR) | VERIFY removed |
| 2009: wedges limited to two players; 2018 banned all wedges | VERIFIED | Wikipedia (2009: "three or more blockers" banned); CBS Sports 2018 rule-change article | footnote re-sourced (CBS link added) |
| 2016 touchback 20 to 25, one-year trial | VERIFIED | FOX6 (Mar 2016); PFT (2017 extension) | footnote re-sourced, extension added |
| 2018 redesign: no running start (within 1 yd), 5 a side, 8 in a 15-yd setup zone, wedges banned | VERIFIED | SI 2018 (existing); CBS 2018 | none |
| 2023 fair catch inside the 25 = ball at 25 | VERIFIED | CBS Sports (approved May 23, 2023, one-year trial) | footnote re-sourced |
| Concussions ~5x as likely on kickoffs in 2017; 71 kickoff concussions 2015-17 | VERIFIED | ESPN 2018 (both figures, from Rich McKay); NFL.com May 2, 2018 (the 71) | footnote reworded: who said which |
| 2023 return rate lowest on record (nflverse back to 1999) | VERIFIED | Course calculation: 25.2% in 2023, the lowest of 1999-2025 (1999-2009 were 81-89%) | none |
| Return rates 25.2 / 32.9 / 74.6%; touchback rate 64.3% (2024), 20.7% (2025) | VERIFIED | FACTS-current §3; re-run | none |
| 2025 brought returns "back to 2010 levels" | CORRECTED | Re-run: 2010 = 79.8%, 2025 = 74.6% | changed to "close to 2010 levels" |
| Drive starts around the 22 (TB at the 20) and the 25 (TB at the 25); up ~4 yd in 2024 | VERIFIED | Re-run (21.4-21.9 in 2011-15; 24.5-25.2 in 2016-23; 29.6 in 2024) | none |
| XFL 2020 kickoff invented by Sam Schwartzstein, "director of football operations, innovation and strategy"; former Stanford center; simulated 1,000+ times | VERIFIED, wording simplified | Wikipedia "Sam Schwartzstein"; SI (Manzano, Sept 5, 2024) | title shortened to "director of football operations" (sources differ on the full title); new footnote [^schwartz] |
| John Fassel among special-teams coaches who presented the XFL model to the committee | VERIFIED | SI Cowboys Country (one of three coordinators) | none |
| Owners approved the 2024 trial on March 26, 2024 | VERIFIED | AP via KSAT (29-3 vote, Mar 26, 2024) | date added to text and footnote |
| 2024 setup: 9 in the zone, 7 on the 35, the other 2 outside the hashes; up to 2 returners; kicker may not cross midfield | VERIFIED | NFL.com 2024 explainer; 2026 rulebook 6-1-3(a)(4) | none |
| 2025: touchback to the 35, made permanent; 6 on the line + up to 3 off | VERIFIED | NFL.com (Apr 2025); FACTS-current §3 | none |
| 2026 floater anti-overload rule | CORRECTED | 2026 rulebook 6-1-3(b)(2): max four off the line, "never more than two players in each of the three areas ... bordered by the sidelines and inbounds lines"; with four, at least one outside the inbounds lines on each side | vague "spread across the field" replaced with the exact rule |
| 2026 onside kick declarable "at any time during the game" | VERIFIED | 2026 rulebook 6-1-6; Vikings.com | none |
| Kicks from the 50, 2024-2025 touchback spot (sources said 30 or 35) | CORRECTED | 2026 rulebook 6-1-5 adds the 50-yard-line touchback clause as a 2026 change, so before 2026 the ordinary spot applied: 30 (2024), 35 (2025). The 2025 35 vs 25 out-of-bounds incentive is confirmed by Football Zebras (Nov 2025) and Walt Anderson's rules video as reported | table: 2025 = "the 35 / the 25" |
| Kicks from the 50, 2026 out-of-bounds spot (sources said 20 or 40) | CORRECTED | 2026 rulebook 6-2-4: out of bounds = 25 yards from the spot of the kick, so the 25. Only the touchback moved, to the 20. Football Zebras/Vikings ("OOB at the 20") and Buccaneers.com ("the 40") are both wrong against the rule text | table 2026 = "the 20 / the 25"; text, takeaway, [^rules2026] and [^fifty26] corrected; table caption explains the 25-yards-from-the-kick rule |
| Dallas tried the out-of-bounds kick vs KC in 2025 | VERIFIED, with detail | CBS (existing); Football Zebras Nov 2025: a Dallas player (Tolbert) left early, illegal-formation flag, KC took a re-kick | "tried" kept; footnote notes the re-kick |
| 2024: kickoff concussion rate -43% vs 2021-23; returns +57% | VERIFIED | NFL.com "Concussions decrease to historic low in 2024" | none |
| Onside alignment: kicking team beside the ball, receiving team 10 yards away | VERIFIED | 2026 rulebook 6-1-6(b),(c),(g),(h): kicking team on its 35, at most five on either side; receiving restraining line 10 yards ahead; 8-9 players within 15 yards of it | caption now states the rule rather than "generic"; CBS "ball at the 34" detail dropped (not in the rulebook); VERIFY removed |
| "Any kickoff becomes a free ball once it has traveled 10 yards" | CORRECTED | 2026 rulebook 6-1-6(e), 6-1-4(c): under the dynamic kickoff only an onside kick is recoverable after 10 yards | now "An onside kick ... reaches the receiving team's restraining line, 10 yards away" |
| Onside kicks "used to work more often than" one in five | CORRECTED | Course calculation: 2010-17 recovery about 11-21% a season, averaging about 15% | now "rarely worked even that often ... roughly one in seven"; new footnote [^calcons2] |
| Declared onside recovery 6.0% (2024), 9.6% (2025), about 50 a season | VERIFIED | Re-run (50 and 52 attempts) | none |
| Troy Vincent, Oct 2025: under 5% might make owners "revisit" | VERIFIED | AP (Whyno, Oct 21, 2025); Vincent is EVP of football operations | none |
| Eagles/others' 4th-and-long alternative never adopted | VERIFIED | FACTS-current; CBS | none |
| Grupe: "in Week 1 every one of his first nine kickoffs" landed at or inside the 5 | CORRECTED | The Ringer (Gayle, Sept 12, 2024): "his first nine kicks" | dropped "in Week 1" ("first nine kickoffs of the season") |
| Bears Week 1 double team; "within a week at least eight other teams" | CORRECTED | The Ringer: double team plus a pulled blocker to pick off an unblocked man; nine other teams used double teams in Week 1 | play description and count fixed (text, [^bears], [^ringer], [^ringer2]) |
| Saints 2024 best opponent drive start after kickoffs (28.2 vs league 29.6) | VERIFIED | Re-run | none |
| Seattle 2025 best (28.0 vs 30.3, 11.7% touchbacks); SB LX champions; Myers 5 FG record | VERIFIED | Re-run; FACTS-current §1 | none |
| Scatter caption: SEA/CAR landing zone and good coverage; Rams ~half touchbacks and better than average; ARI and TB worst | VERIFIED | Re-run (LA 49.5% TB, 29.6; ARI 33.1; TB 32.8) | none |
| Best unit ~2 yd below average, worst ~3 yd above | VERIFIED | Re-run (-2.4 / +2.7) | none |
| "eight or nine kickoffs in a typical game ... two or three points a game" | CORRECTED | Re-run: about 87.5 kickoffs per team-season, so about 10 a game; 0.30 EP × 10 ≈ 3 | "about ten kickoffs ... about three points a game" |
| Touchback-math claims (28 at the goal line, 31 at the 10; 2024 kicks past the 2 beyond the 30; landing-zone returns near the 29; most returns stopped at the 25-35; end-zone returns avg the 26, 9% reach the 35) | VERIFIED | Re-run (2025: 28.0 / 31.1; 2024: 30.3-31.7; LZ 29.5; 63% at 25-35; EZ 26.2, 8.8%) | none |
| EPA: returned +0.19, touchback +0.47, roll-in touchback -0.38 (2025) | VERIFIED | Re-run | none |
| Super Bowl XLIV "Ambush": Feb 7, 2010, Morstead, off a Colts player, Saints recovered, TD drive, 31-17, trailing 10-6 | VERIFIED | Wikipedia SB XLIV; PFR box score; ESPN "Saints' top play: Ambush onside kick" (name; off Hank Baskett) | ESPN source added for the name |
| "still the most famous onside kick ever" | SOFTENED | opinion | "probably the most famous" |
| BDB 2022: special-teams theme, 2018-2020 seasons, games/plays/tracking CSVs | VERIFIED | NFL Football Operations BDB finalists release; CMU CMSAC 2022 workshop | VERIFY removed |
| eval:false cell: home/away/football mapping; `specialTeamsPlayType`; `homeTeamAbbr` | VERIFIED (from memory of the 2022 data dictionary; Kaggle needs a login) | — | fixed a bug: the cell took `ko.iloc[0]` (a 2018 game) but loaded `tracking2020.csv`, so it returned no frames. It now loads tracking2018.csv and picks a kickoff from games in that file |

## Counts

VERIFIED 30 · CORRECTED 12 · SOFTENED 1 · REMOVED 0 (one minor sub-detail dropped: the CBS "ball at the 34" onside spot).

## Outside this chapter

- 13-02's line that drives after kickoffs now "far more often begin at the 35" overstates it: only 20.7% of 2025 kickoffs were touchbacks (re-run). This is the writer's flag and I confirm it.
- FACTS-current §3 (2026) says the kick from the 50 "is now a touchback at the 20, previously the 25". The rulebook says touchback 20 (previously 35 in 2025), with out of bounds still at the 25. Worth tightening the fact sheet.
- Appendix E should use 6-1-5 / 6-2-4 as above for the kick-from-the-50 row.
