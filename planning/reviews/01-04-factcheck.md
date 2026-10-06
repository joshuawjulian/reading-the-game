# Fact-check: 01-04 What a Play Really Is

Checked 2026-10-06 against FACTS-current.md, nflverse (recomputed in the `rtg` container) and web sources.
All 14 `<!-- VERIFY -->` comments are resolved and removed. The chapter builds (`build_pdfs.py 01-04-what-a-play-really-is`: OK).

| Claim | Verdict | Source | Change |
|---|---|---|---|
| Typical staff "20–30 coaches" | CORRECTED | Steelers Now, Jan 27 2025 (PIT 19; PHI/WAS 23; BUF/KC 22) | Now "around twenty to twenty-five on-field coaches", plus strength coaches; new fn `staffsize` |
| Kicking plays ≈ 1 snap in 6 | VERIFIED | Own nflverse calc, 2025 REG: 7,083 of 40,536 plays (17.5%) | New fn `stshare` |
| Every NFL team has analysts | VERIFIED | ESPN NFL analytics survey 2024 (all 32 teams have a designated analytics staffer) | New fn `analytics` |
| Sideline coaching restricted "for decades" | CORRECTED | PFHOF chronology 1944: "Coaching from the bench was legalized on April 20" | Now "illegal in the NFL until 1944"; new fn `bench` |
| Paul Brown: Browns HC 1946–62, former teacher, playbooks and tests, messenger guards | VERIFIED | Encyclopedia of Cleveland History; Britannica; PFHOF | The Miami Univ. URL in fn `brown` redirects to a host with a bad TLS certificate, so it was replaced |
| 1956 Ratterman radio helmet: Campbell and Sarles, Bell banned it after a handful of games | VERIFIED | PFHOF (exhibition vs DET plus 3 games); SI 2014 | The old PFHOF URL returns 404; replaced with the live URL |
| QB radio 1994, defensive radio 2008, one green dot on the field | VERIFIED | Ravens.com 2008; NFL.com/AP 2008 | None |
| Booth coaches allowed on the radio since 2016 | VERIFIED | Colts.com 2016; Buccaneers.com "7 rule changes approved for 2016" | Second source added to fn `cutoff` |
| Radio cut-off at :15 or at the snap, whichever comes first | VERIFIED | Boston Globe, Feb 3 2017; ESPN 2007; AP 2022 | Source added to fn `cutoff` |
| 40-second and 25-second play clocks; delay of game is 5 yards | VERIFIED | operations.nfl.com terms glossary | None |
| 175 offensive delay-of-game penalties in 2025, ≈ 1 every 1.5 games | VERIFIED | Own recalculation: 175 flags, all on the offense, in 272 games | None |
| Belichick started with the 1975 Colts doing film work for a tiny salary | VERIFIED | CNBC, Jan 31 2019 ($25 a week, special assistant to Marchibroda); Halberstam | CNBC added to fn `belichick` |
| Walsh's 49ers made the opening script famous; scripts of 10–20 plays | VERIFIED | AP obituary via NFL.com, 2007 ("scripting the first 15 offensive plays"; laminated sheets) | AP added to fn `walsh`; page reference dropped; fn notes that accounts of his script length range from 15 to 25 |
| Shanahan/McVay-family calls of a dozen words or more | VERIFIED (Shanahan); McVay by family association | NBC Sports Bay Area, Jun 16 2020 (a call of about 20 words) | Source added to fn `layden` |
| Erhardt-Perkins named for Ron Erhardt and Ray Perkins; Patriots; one-word concepts | VERIFIED | Chris B. Brown, Grantland, Jan 25 2013 | New fn `ep` |
| Bills under Allen as a sugar-huddle user | REMOVED, replaced | No source found for the Bills. SI Bear Digest (Jul 10 2025) and Pride of Detroit (Dec 2024) document Ben Johnson's Lions | Team changed to Ben Johnson's Lions; new fn `sugarlions` |
| Wristbands: NFL use for no-huddle, young QBs, punt team; "some offenses issue them to every skill player"; Chiefs example | CORRECTED / REMOVED | AP Nov 25 2022 (about 20 starting QBs wear one, so the caller can radio a number); ESPN Aug 5 2017 (Shanahan bans them) | Unsourced specifics removed (punt team, every skill player, Chiefs); the AP figure and the Shanahan contrast added; new fn `wristband` |
| Manning "Omaha" said 44 times; Broncos 24–17 Chargers, Jan 12 2014; Manning quote | VERIFIED | NFL.com (Rosenthal), "all 44 times"; AP via Fox News for the score; denverbroncos.com Jan 15 2014 for the quote | Text now says "44 times by NFL.com's count, in a 24–17 win on January 12, 2014"; new fn `omahacount` |
| Shanahan calls the 49ers' plays (2026 OC Klay Kubiak); Johnson calls Chicago's plays; Campbell took over in mid-2025; Petzing is the 2026 OC; Glenn calls the Jets' defense | VERIFIED | FACTS-current §0 C1 and §9; Shaw Local Jan 2025; ESPN (Petzing) | None |
| Kingsbury: ARI HC 2019–22, WAS OC 2024–25 | VERIFIED | Wikipedia; NFL.com (Commanders and Kingsbury part ways, Jan 2026) | NFL.com added to fn `kingsbury`; Rams 2026 role noted (consistent with FACTS §9) |
| WAS no-huddle 68% (2024) and 63% (2025); ARI led the league 2019–22; median team under 5% | VERIFIED | Own recalculation: WAS .676/.633; ARI #1 in 2019, 2020, 2021 and 2022; 2025 median team 4.6%, league 7.8% | None |
| Washington's no-huddle was about control, not speed | VERIFIED | The Ringer, Oct 3 2024 (led the league in no-huddle; only 13th in play clock left at the snap) | New fn `ringer` |
| Defensive 12 men at the snap: live-ball foul, so the offense gets a free play | CORRECTED (precision) | Football Zebras 2012: live-ball only when the 12th man is trying to leave; a 12th man settled in the formation is a dead-ball foul | One sentence added on the dead-ball case (the drill's player is leaving, so the answer stands); fn `twelve` cites Rule 5 §1–2 plus Football Zebras |
| Officials hold the snap only when the offense substitutes | CORRECTED (precision) | Rule 5, Section 2 (Art. 10 per secondary sources); Football Zebras, Oct 2 2025 | Added "outside the last two minutes of each half" and that the umpire stands over the ball; new fn `subs` |
| *The Art of Smart Football* (2012) | CORRECTED | Published 2015 (Eleven Warriors review; catalog records) | Year changed to 2015 |
| *Take Your Eye Off the Ball* 2010; 2nd ed. 2015 | VERIFIED | Triumph Books (2.0, Oct 2015) | None |
| Halberstam *Education of a Coach* (2005); Layden *Blood, Sweat and Chalk* (2010) | VERIFIED | Publisher records | None |

## Counts
VERIFIED 20 · CORRECTED 6 · REMOVED/replaced 1 (Bills sugar huddle) · SOFTENED 0. The wristband row was part corrected and part removed; it is counted once, as CORRECTED.

## Still uncertain / for a human
- The Rule 5-2-10 article number comes from secondary sources only (the NFL rulebook PDF could not be fetched). The chapter cites "Rule 5, Section 2" without an article number.
- The sugar-huddle source for the Lions is SI's Bear Digest (team-site tier) plus a Pride of Detroit film breakdown, which returned 403 so its wording is unconfirmed. Rated LIKELY.
- Pro Football Reference was not reachable (as noted in FACTS-current). Score lines come from AP.
- Uncited but general claims were left as they are: playbooks live mostly on tablets; the call sheet held over the mouth is to stop lip-reading; a huddle takes about 10 seconds.
