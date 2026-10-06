# Fact-check: 04-07 Quarterback Play

Checked 2026-10-06 against FACTS-current.md, the 2026 NFL rulebook PDF (from operations.nfl.com), nflverse data (recomputed in the `rtg` container) and web sources.
All 9 `<!-- VERIFY -->` comments are resolved and removed. The chapter builds (`build_pdfs.py 04-07-quarterback-play`: OK).

| Claim | Verdict | Source | Change |
|---|---|---|---|
| Tarkenton was a preacher's son from Georgia | VERIFIED (made more precise) | Wikipedia "Fran Tarkenton" (father Dallas Tarkenton, Pentecostal minister; Athens High School, Athens GA) | Now "from Athens, Georgia"; source added to fn `tarkenton` |
| Van Brocklin, his first head coach, objected to the scrambling | VERIFIED | PFHOF bio ("often frustrated Vikings coach Norm Van Brocklin, who favored a more traditional approach"); Wikipedia (trade demand, VB resigned Feb 1967) | Clause added on how the feud ended; both cited in fn `tarkenton` |
| Tarkenton: Vikings from the first game in 1961 (4 TD passes plus a TD run off the bench, 37–13 vs CHI); scramble quote; retired 1978 with career records for completions, yards and TD passes | VERIFIED | PFHOF bio (quote verbatim; 3,686 / 47,003 / 342) | None |
| Intentional grounding: definition; outside the pocket the ball must land at or beyond the LOS extended, out of bounds included | VERIFIED | 2026 Official Playing Rules, Rule 8 §2 Art. 1 and Item 1; Rule 3 §25 (pocket area) | Fn `grounding` now quotes the rule and the 2024 change ("any part of his body or the ball" outside counts; PFT, Jul 31 2024) |
| Grounding penalty "loss of down and ten yards (or the spot of the foul, if worse); safety in the end zone" | CORRECTED (wording) | Rule 8 §2 Penalty: 10 yards from the previous spot, or loss of down at the spot of the pass; safety if the passer's entire body and the ball are in his end zone | Text now says "spot of the pass"; the dead operations.nfl.com video-rulebook URL (404) was replaced |
| Tackle box = area between where the tackles lined up | VERIFIED | Rule 3 §25 | None |
| Super Bowl XLVI: Patriots' first offensive play from their own 6, Tuck pressure, grounding in the end zone, safety; Giants won 21–17 ("by four"), Feb 2012 | VERIFIED | Wikipedia "Super Bowl XLVI" | None |
| "Giants led 2–0 before they had run an offensive play" | CORRECTED | Wikipedia: the Giants received, completed a 19-yarder to Nicks, then punted to the NE 6 | Now "the Giants, who had punted on their own opening drive, led 2–0"; fn `xlvi` updated |
| "The most famous grounding call of the century" | SOFTENED | Superlative can't be checked | Now "of recent decades" |
| Manning 2013: 55 TD passes and 5,477 yards, both records, at 37 | VERIFIED | Wikipedia 2013 Broncos; own nflverse check through 2025 (best since: Mahomes 50 TD in 2018, Brady 5,316 yards in 2021); Brees's 5,476 in 2011 | Fn `manning-2013` says both records still stood after 2025 |
| Manning's 2013 sack rate was the lowest among regular starters; Brady's time to throw in 2021–22 | VERIFIED | Computed inline from nflverse/NGS (2.7%, rank 1; Brady rank 2 of 30 and 1 of 30) | None |
| Brady 2000–2022, ages 44 and 45 in 2021–22 | VERIFIED | Born Aug 3, 1977 | None |
| Mahomes's left-handed throw: Oct 1 2018 MNF at DEN, 3rd-and-5, 3:14 left, down 23–20, Von Miller, 6 yards to Hill, winning TD seven plays later, final 27–23 | VERIFIED | CBS Sports; ESPN | None |
| "Asked later for Mahomes's greatest play, Reid chose that one" | SOFTENED | CBS: asked for the most impressive play, Reid said "I think probably the left-handed throw" | Now "Asked years later for the most impressive play of Mahomes's career" |
| Helmet Catch: Feb 3 2008; NE led 14–10 and was unbeaten; 3rd-and-5 at the NYG 44, 1:15 left; Seymour and Green; Tyree knocked off his route, drifted to the middle; Harrison | VERIFIED | Wikipedia "Helmet Catch" | Details added to fn `helmet` |
| Spot of the catch: Patriots' 24 vs 25 | VERIFIED: 24 | Wikipedia "David Tyree" (NE 24, 59 s left); 44 + 32 yards = NE 24. The "Helmet Catch" article's 25 doesn't match its own 32-yard gain | Text keeps 24; the footnote now says "24" and explains the discrepancy |
| Giants scored four plays later | VERIFIED | Wikipedia "David Tyree" (four plays and 24 seconds later, 13-yard TD to Burress) | Text names Burress's 13-yard TD |
| Allen won the 2024 MVP; listed 6-5, 237 | VERIFIED | NFL.com; 2025 nflverse roster (77 in, 237 lb) | Roster source added to fn `allen-mvp` |
| Allen and Mahomes have the highest out-of-pocket EPA (2022–25); 11 of 32 better outside | VERIFIED | Recomputed from the chapter's setup code: Allen +0.31, Mahomes +0.30, next is Daniels +0.27 | None |
| Burrow led the NFL in 2024 passing yards (4,918) and TDs (43); LSU teammate of Chase | VERIFIED | nflverse player stats; LSU 2018–19 | Numbers and LSU years added to fn `burrow-2024` |
| Purdy: pick 262, "Mr. Irrelevant", 2022 | VERIFIED | NFL.com | None |
| Purdy 2023 "his first full season" | CORRECTED (precision) | He started 5 games late in 2022 | Now "first full season as the starter" |
| Purdy 2023 ranks: EPA #1 and nflverse CPOE #1 of 33; NGS CPOE rank; YAC share at the league rate | VERIFIED (computed inline) | nflverse/NGS. The current build gives an NGS rank of **5th**; the writer's note said 6th, but the text is inline so it is correct either way | None |
| Purdy's 2025 injury cost him "much of the season" | CORRECTED (made specific) | nflverse: he played 9 of 17 games; NBC Bay Area, Oct 23 2025 (turf toe in Week 1, aggravated in Week 4) | Now "a turf-toe injury cost Purdy eight games"; new fn `purdy-toe` |
| Mac Jones played 2022–24 with NE and JAX | VERIFIED | nflverse | None |
| 2025: Stafford MVP, Maye runner-up; Maye had the league's best CPOE (+10.8) and best EPA per dropback (+0.33) and threw about as deep as Stafford (9.1 vs 9.3 aDOT); Purdy bottom-right (2nd-longest time to throw, aDOT below the mean) | VERIFIED | FACTS-current §2; recomputed from the chapter's setup code | None |
| nflverse CP model features | VERIFIED (made more precise) | Baldwin, OSF 2020: air yards, whether air yards = 0, distance to sticks, yard line, down, yards to go, pass location (middle or not), QB hit, home, roof, era | Feature list added to fn `cp-model` |
| NGS completion probability uses receiver separation | VERIFIED | NFL.com, "Next Gen Stats: Introduction to Completion Probability" | The glossary URL (renders no text) was replaced with the NFL.com article |
| Scramble-drill core rules | VERIFIED (team versions vary, as the text already says) | Scouting Academy ITP glossary; Win With The Pass ("If you are shallow go deep, If you are deep come back… If you are left come back to the right"; get into the QB's field of vision) | The footnote quote was paraphrased; it is now verbatim |
| Jaworski/Cosell/Plaut, *The Games That Changed the Game* (2010): "a quarterback's eye view…; the NFL Films analyst who watched more all-22 film than anyone" | CORRECTED / SOFTENED | Random House / Publishers Weekly: seven games broken down from coaches' film; Cosell and Plaut were NFL Films senior producers | Description rewritten; the superlative was removed |
| Chris B. Brown, *The Art of Smart Football* (2015) | VERIFIED | Publication record | None |
| Predict 2: 3rd-and-9 at the 31 is a ~48-yard FG, and an 8-yard sack makes it ~56 | VERIFIED | Arithmetic (LOS + 17) | None |
| Football-technical claims (hitch timing, first-read median 2.3 s, climb/slide/escape, throwaway/sack/INT EPA, checkdown conversion rates) | VERIFIED (computed inline or standard coaching description) | nflverse/FTN computed in the chapter | None |

**Counts:** VERIFIED 25 · CORRECTED 5 · SOFTENED 3 · REMOVED 0. One row, Jaworski, is counted as CORRECTED although its verdict is CORRECTED / SOFTENED.

**Uncertain or left open:** Pro Football Reference blocks automated fetches, so the Helmet Catch spot rests on Wikipedia's "David Tyree" article and on the arithmetic. The claim that Mahomes was "flushed to his left" is the standard account and was not independently confirmed.
