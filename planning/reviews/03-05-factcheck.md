# Fact-check log: 03-05 Perimeter Runs and Misdirection

Checked 2026-10-06 against FACTS-current.md, the 2026 NFL rulebook PDF (linked from operations.nfl.com), web sources and
nflverse data (recomputed in the `rtg` container). All 12 `<!-- VERIFY -->` comments resolved and removed. Every footnote is
referenced exactly once. Build `build_pdfs.py 03-05-perimeter-and-misdirection --html`: OK (20 pages).

| Claim | Verdict | Source | Change |
|---|---|---|---|
| Crackback rule is Rule 12-2-6, 15 yards; applies within 5 yds of LOS to a player >2 yds outside the tackle or from the backfield, moving toward the snap; no contact below the waist or to head/neck | CORRECTED (precision) | 2026 rulebook text, 12-2-6 Items 1–2 (backfield player who *moves* flexed also counts; banned contact = below waist or any defenseless-player contact per 12-2-9(b)(1–3)) | Prose now covers the backfield clause and "any other contact banned against a defenseless player"; footnote rebuilt on the rulebook (secondary blog link and the 2025 penalty-table link dropped) |
| Blindside block foul since 2019, path toward or parallel to own end line | VERIFIED + CORRECTED (detail) | NFL "Health and safety-related rules changes since 2002" (2009 head/neck version; 2019 expansion, quoted); rulebook 12-2-7 (close-line exemption) | Footnote quote now exact and notes the 2009 precursor; prose adds helmet/forearm/shoulder and the close-line exemption |
| "A legal crack is thrown with the hands and shoulders" | CORRECTED | 12-2-7: forcible shoulder contact on a path parallel to the end line is a blindside foul outside the close-line area | Now "a hands-first block, from the side and chest-high, not a shoulder shot" |
| 2026 three-strike policy: five fouls incl. blindside blocks; three in a season = one-game suspension | VERIFIED | FACTS-current.md (LIKELY); PFT/NBC Sports; multiple Aug–Sept 2026 reports | Footnote adds Aug 2026 agreement, starts with 2026 regular season, preseason fouls excluded. Note: reports differ on whether the three must be the same foul; text does not specify |
| Forward pass = ball moves forward from passer's hand (Rule 8-1); jet flips forward are scored as passes; Kansas City as an example | VERIFIED | 2026 rulebook 8-1-1(a); nflverse pbp: Hill 1-yd TD at LAC, Sept. 9, 2018 = "Mahomes pass short middle", air yards −3 | Footnote adds the concrete play |
| PFF: 174 jet sweeps (5.1 ypc) 2017, 309 (6.1) 2018; Rams 48 incl. playoffs, 2.3/game, 6.8 ypc, 3 TD; Patriots and Chargers next at 24; Woods 16 | VERIFIED | Daniel Rymer, PFF, May 13, 2019 | none |
| Nelson built the Wing-T at Maine, then Delaware 1951–65 | VERIFIED | Wikipedia "David M. Nelson" (Maine 1949–50, Delaware 1951–65; began developing Wing-T at Maine) | Source added to footnote |
| Raymond succeeded Nelson, 36 seasons to 2001, 300 wins; 300th on Nov. 10, 2001, 10–6 vs Richmond; 300–119–3 | VERIFIED | UDaily obituary, Dec. 2017; Wikipedia "Tubby Raymond"; bluehens.com | Obituary added |
| Raymond a Michigan graduate who painted portraits of his senior players | VERIFIED | UDaily obituary (Michigan 1950; acrylic portraits of seniors, featured by SI, GMA) | Source added |
| *The Delaware Wing-T: An Order of Football*, Raymond and Kempski, Parker Publishing, West Nyack NY, 1986 | VERIFIED | Open Library ISBN 0131983261 (Parker Pub. Co., West Nyack, 1986) | ISBN + record added |
| Nelson's problem: smaller, slower players | SOFTENED | (standard account; no primary quote found) | "is usually said to have faced" |
| Brown quote "each time a team tries to stop one thing, it opens itself up to something else" | VERIFIED | Brown, Grantland, Jan. 3, 2014 (Brown's own words) | Footnote adds Raymond's own line, "It is sequence football" |
| Fly sweep series spread in HS/college in the 1990s–2000s, out of Wing-T motion | SOFTENED + CORRECTED | Ross Dellenger, SI, Sept. 25, 2018 (Gene Beck, Delano HS, 1950s "many believe" first; Speckman 1980s–90s clinics; Hawkins Siskiyous → Willamette → Boise State 1999–2000) | Paragraph rewritten: origin murky, Beck credited, Speckman/Hawkins spread; Wing-T link stated as adoption, not invention; "fly waggle" list dropped; new `[^fly]` |
| Lombardi's 1960s Packers sweep pulled both guards | VERIFIED | Packers.com ("Jerry Kramer was lineman at forefront of Lombardi's power sweep"); standard record | none |
| Malzahn taught himself from Raymond/Kempski's book as a young Arkansas HS coach, early 1990s | VERIFIED | Brown, Grantland (Hughes HS, offense from 1992, "word-for-word") | Footnote detail added |
| Malzahn "soon moved" to an up-tempo shotgun spread | CORRECTED | Brown, Grantland (spread by 1999 at Shiloh Christian) | Now "by the late 1990s" |
| Auburn 2013 >300 rush yds/game, first SEC team in almost 30 years; buck sweep from shotgun with receiver faking end-around | VERIFIED | Brown, Grantland (Mason TD vs Missouri) | none |
| Auburn 2013: Marshall QB, Mason RB, reached national championship game | VERIFIED | Grantland; Saturday Down South (328.3 ypg, Mason 1,816 yds, BCS title game) | New `[^auburn]` footnote |
| Malzahn's *The Hurry-Up, No-Huddle: An Offensive Philosophy* (2003) | VERIFIED | Wikipedia "Hurry-up offense" (Coaches Choice, Jan. 2003) | Publisher added |
| McVay Rams and Shanahan 49ers "made jet motion part of almost every play" | CORRECTED | FACTS-current.md: motion at the snap ~4% of plays league-wide in 2017 (ESPN) | Now "a weekly staple" |
| Woods 2018: 19 carries, 157 yds, 1 TD; Rams WR carries 35 (+0.44 EPA), among the league's best | VERIFIED | nflverse recomputed (LA ranks 2nd among teams with 20+ WR carries); Cooks 10 carries = the other main jet runner | none |
| Deebo Samuel 2019: rookie, 14 carries, 159 yds, 3 TD | VERIFIED | nflverse recomputed; PFR | PFR link added |
| SB LIV: Samuel 3 carries, 53 yds (32, 7, 14) | VERIFIED | nflverse recomputed | none |
| 53 yds a Super Bowl record for a WR | VERIFIED (added, "at the time") | NBC Sports Bay Area, Feb. 2, 2020 (broke Harvin's 45, SB XLVIII) | Added to prose with "at the time" (later Super Bowls not checked) |
| Data: WR EPA/carry > RB every season 2016–25, WR positive in 8 of 10; WR −0.07 vs +0.10, success 39/51%, lost 10/15%, 10+ 10/22%; 0.6–0.9 WR carries per team-game | VERIFIED | Recomputed (WR negative only 2017 and 2024; per-game 0.60–0.89); build asserts pass | none |
| BDB 2025 = 2022 season weeks 1–9, `inMotionAtBallSnap` in player_play | VERIFIED (weeks LIKELY per FACTS) | FACTS-current.md §8 | none |
| Football-technical: force/pursuit, crack/seal/replace, crack-toss, end-around vs reverse, backside contain, buck sweep/trap/waggle mechanics, eye-candy half-second arithmetic (illustrative model, consistent with 02-06) | VERIFIED | standard coaching material; Raymond & Kempski; 02-06 model | none |

Counts: VERIFIED 19 · CORRECTED 5 (crack rule precision, legal-crack technique, Malzahn timing, "almost every play", fly-sweep history) · SOFTENED 2 (Nelson's problem, fly-sweep origin) · REMOVED 0. (Blindside footnote counted under VERIFIED with a detail fix.)
