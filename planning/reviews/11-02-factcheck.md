# Fact-check log: 11-02 1978 and the Passing Revolution (1978–1999)

Checked 2026-10-08 against FACTS-current.md, web sources, and nflverse play-by-play (recomputed in the `rtg` container; scripts are in `_pdfbuild/1102-fc/`). I resolved and removed all 10 `<!-- VERIFY -->` comments. No footnotes were added or removed: there are still 31, each referenced exactly once. Sources were added inside existing notes (`[^matheson]`, `[^lt]`, `[^openup]`, `[^sb22]`, `[^bodybag]`, `[^tupa]`, `[^fa]`, `[^broncos]`, `[^hof7477]`). Build `build_pdfs.py 11-02-the-1978-liberation`: OK (22 pages). No figure code changed.

The writer's chart CSV (1970–1999) was checked against Pro Football Reference's "League Year-by-Year Averages". PFR returns 403, so I used the Internet Archive snapshot of Dec 28, 2024 (fetched with curl and parsed). All 30 rows match exactly in points per game, NY/A, attempts, completions, interceptions, TDs and rush attempts. The print-time spot-check the writer asked for is done.

**Totals:** 60 VERIFIED, 6 CORRECTED, 0 SOFTENED, 0 REMOVED.

| Claim | Verdict | Source | Change |
|---|---|---|---|
| 1977: 17.2 points per team-game, fewest since 1942 | VERIFIED | PFR league averages (archived): 1942 15.9; every season 1943–1976 is above 17.2 | none |
| Chart CSV, 1970–1999 (all 30 rows) | VERIFIED | PFR league averages, IA snapshot 2024-12-28 | none |
| Derived rates: 40% passes in 1977 → 49% in 1980, never below half after 1983; INT% 5.7 → 4.6 (1979–80) → 3.4 (1999); Cmp% 51 → 56; NY/A 5.2 → 6.0, then 5.7–6.1; points 17.2 → 20.5 | VERIFIED | Recomputed from the same table | none |
| 1992 and 1993 at 18.7 ppg, "the lowest since 1977" | CORRECTED | PFR: 1978 was 18.3, which is lower than 18.7 | Now "the lowest since 1978" |
| 1998 Vikings 556 points, a record at the time | VERIFIED | Wikipedia, 1998 Minnesota Vikings season | none |
| 1974: downfield contact restricted, kickoffs moved 40 → 35, goalposts to the end line, "to add action and tempo" | VERIFIED | PFHOF Chronology 1974 | none |
| "Isaac Curtis rule": named for a receiver "so fast that defenses double- and triple-covered him" | CORRECTED | Wikipedia, Isaac Curtis: Shula's DBs couldn't keep up, so they would "push, bump, and hold him down the field," and others copied it; that is what prompted the rule | The reason now names the bumping and holding; the footnote quotes the source |
| 1977: one contact per receiver; head slap banned | VERIFIED | PFHOF Chronology 1977 | none |
| Oct 1977 TV contracts with all three networks from 1978, the largest package ever; 16 games | VERIFIED | PFHOF Chronology 1977 | none |
| March 1978: five-yard contact zone ("Mel Blount Rule"); extended arms and open hands; side judge; 16 games; second wild card | VERIFIED | PFHOF Chronology 1978; Wikipedia, 1978 NFL season | none |
| Mel Blount 6 ft 3 in, 1975 Defensive Player of the Year | VERIFIED | Wikipedia, Mel Blount (infobox; DPOY 1975) | none |
| 1979 "clearly in the grasp" | VERIFIED | PFHOF Chronology 1979 | none |
| Illegal contact enforced strictly from 2004 ("Ty Law rule") | VERIFIED | 11-04 fact-check (AP/STATS) | none |
| Bradshaw 1978 MVP; Super Bowl XIII 318 yards, 4 TD, 35–31 (VERIFY) | VERIFIED | Wikipedia, Terry Bradshaw (NFL MVP 1978) and Super Bowl XIII (17/30, 318 yds, 4 TD, then records) | VERIFY removed; source added to `[^openup]` |
| Coryell: SDSU in the 1960s, Cardinals from 1973, took over the Chargers Sept 25, 1978 after a 1–3 start | VERIFIED | Wikipedia, Don Coryell | none |
| Fouts: 4,082 yards in 1979 (beat Namath's 4,007), 4,802 in 1981, first with three straight 4,000-yard seasons | VERIFIED | Wikipedia, Dan Fouts; Epic in Miami page (NFL-record 4,802) | none |
| Chargers led the NFL in passing 1978–83; 1979 the first AFC West champion with more passes than runs | VERIFIED | Wikipedia, Air Coryell | none |
| Winslow a 1979 first-round pick | VERIFIED | Wikipedia, Kellen Winslow | none |
| Epic in Miami: Jan 2, 1982; 24–0 after Q1; 41–38 OT; Fouts 33/53, 433 yards, all postseason records; Winslow 13 rec, 166 yds, blocked FG | VERIFIED | Wikipedia, Epic in Miami ("His attempts, completions, and passing yards were all NFL postseason records") | none |
| Walsh hired Jan 1979; 49ers 2–14 in 1978 and in 1979; Montana in round 3 of 1979; SB XVI 26–21 | VERIFIED | Wikipedia, Bill Walsh; PFHOF 1982 | none |
| Walsh's Super Bowls after the 1981, 1984 and 1988 seasons | VERIFIED | Common record | none |
| Nickel traced to Jerry Williams (1960), named by George Allen, popularized by Shula and Arnsparger | VERIFIED (presented as "usually traced") | Wikipedia, Nickel defense | none |
| Matheson acquired before 1971 at Arnsparger's request | VERIFIED | Wikipedia, Bob Matheson (Miami News, Sept 2, 1971) | none |
| First season of the 53 (VERIFY) | VERIFIED: 1972 | Wikipedia, 1973 Miami Dolphins season ("devised at the beginning of the 1972 season"); NYT, Jan 13, 1974, "Matheson Is Key to Miami '53' Defense" (via Bob Matheson page) | Text now says the package dates from the start of 1972; VERIFY removed; sources added to `[^matheson]` |
| 1972 Dolphins 17–0, "No-Name Defense" | VERIFIED | Wikipedia, 1972 Miami Dolphins season | none |
| Arnsparger: "rush five guys and cover with six"; "safe pressure" | VERIFIED | Chris B. Brown, Grantland, "Controlled Chaos" (2012): the quote to Tim Layden; "safe pressure" is Arnsparger's catchphrase per LeBeau | none |
| 3-4 the most common base by the late 1970s / early 1980s | VERIFIED | Wikipedia, 3–4 defense ("predominant" late 1970s to early 1980s); SI 2013 "Line shifts"; Super Bowl XV the first with two 3-4 teams | none |
| 1974 Patriots (Fairbanks) and Oilers (Phillips) | VERIFIED | 05-03 fact-check | none |
| Taylor: No. 2 pick in 1981; DPOY 1981, 1982, 1986; 20.5 sacks; first unanimous MVP among defensive players | VERIFIED | Wikipedia, Lawrence Taylor | none |
| Parcells DC then HC; Belichick DC from 1985 | VERIFIED | Common record | none |
| Walsh put a guard on Taylor in the January 1982 playoff game (VERIFY) | VERIFIED | Wikipedia, Lawrence Taylor ("Walsh assigned guard John Ayers, the team's best blocker, to block Taylor", 1981-season divisional playoff, 38–24) | Ayers named in the text; VERIFY removed; quote added to `[^lt]` |
| Taylor rushed mostly from the defense's right / offense's left (VERIFY) | VERIFIED | PFHOF player page: game listings show him starting at right outside linebacker (SB XXI, SB XXV, NFC title games); Theismann play came from behind the QB's left shoulder (Lewis excerpt) | "(he was the Giants' right outside linebacker)" added; VERIFY removed; HOF source added to `[^lt]` |
| Theismann sack, MNF, November 1985; opens *The Blind Side* | VERIFIED | Wikipedia, Lawrence Taylor; Lewis | none |
| Gibbs quote on a game plan "just for Lawrence Taylor" | VERIFIED | Wikipedia, H-back (verbatim; the ellipsis drops "Now you didn't do that very often in this league but I think") | none |
| H-back name from Q/H/F notation | VERIFIED | Wikipedia, H-back | none |
| "70 Chip" on fourth-and-1, Super Bowl XVII | VERIFIED | 03-01 fact-check | none |
| Gibbs: Super Bowls after the 1982, 1987 and 1991 seasons with Theismann, Williams, Rypien | VERIFIED | PFHOF Chronology | none |
| 1985 Bears allowed the fewest points; SB XX 46–10; the 46 named for Plank | VERIFIED | Wikipedia, 46 defense; PFHOF 1986 | none |
| SB XXII: Jan 31, 1988, San Diego, 42–10; Denver led 10–0 after Q1; 35 in Q2 (still the record); Williams 340 yds, 4 TD in Q2; Sanders TDs of 80 and 50 | VERIFIED | Wikipedia, Super Bowl XXII | none |
| Doug Williams the first Black QB to *start* a Super Bowl (VERIFY) | VERIFIED | Wikipedia, Super Bowl XXII ("the first African-American quarterback ever to start in an NFL league championship game, let alone a Super Bowl"); AP/Fox 2023 | VERIFY removed; quote added to `[^sb22]` |
| Timmy Smith's first NFL start; 204 yards, a record (VERIFY) | VERIFIED | Wikipedia, Timmy Smith; Guinness | VERIFY removed; source added to `[^sb22]` |
| Body Bag Game Nov 12, 1990, 28–14, nine injured including both QBs; wild card 20–6 "seven weeks later" | CORRECTED (minor) | Wikipedia, Body Bag Game; the wild-card game was Jan 5, 1991, 54 days later | "seven weeks" → "eight weeks" |
| Ryan's firing by Philadelphia (VERIFY) | VERIFIED | Wikipedia, Buddy Ryan (Jan 8, 1991); Deseret News/AP, Jan 8, 1991 | "Ryan was soon out of a job" → "three days after that the Eagles fired Ryan"; VERIFY removed; sources added to `[^bodybag]` |
| Run-and-shoot in Detroit, Houston and Atlanta; Moon led the NFL in passing yards in 1990 and 1991 | VERIFIED | 04-08 sources; common record | none |
| Ryan's "chuck and duck"; sideline altercation with Gilbride, Jan 2, 1994, vs Jets, nationally televised | VERIFIED | Wikipedia, Buddy Ryan | none |
| 1990 Bills 13–3, 428 points, 51–3 AFC title, four straight SB losses | VERIFIED | Wikipedia, Super Bowl XXV | none |
| SB XXV: Jan 27, 1991, Tampa, 20–19; Norwood 47-yard try, 8 s left; 95 playoff points; Belichick's extra-DB plan and "more than 100 yards"; Giants the best run defense; Thomas 135; TOP 40:33 record; game plan in the HOF | VERIFIED | Wikipedia, Super Bowl XXV | none |
| LeBeau Bengals DC from 1984; zone-blitz origin disputed | VERIFIED (already presented as disputed) | Wikipedia; 07-03 | none |
| 1994 Steelers 55 sacks, league lead | VERIFIED | 07-03 fact-check (Steelers.com, Steelers Depot) | none |
| 1996 Panthers 12–4 and in the NFC title game; Capers to Carolina in 1995 | VERIFIED | Wikipedia, 1996 Carolina Panthers season | none |
| March 1994 package: line play, chucking, roughing the passer, two-point conversion, kickoffs to the 30; neutral zone infraction | VERIFIED | PFHOF 1994; Wikipedia, 1994 NFL season | none |
| College two-point try adopted in 1958 (VERIFY) | VERIFIED | NCAA News, "Two-point conversion turns 50" (2008): adopted January 1958 | VERIFY removed; source added to `[^tupa]` |
| "the NFL took 25 years after the merger to adopt it" | CORRECTED | Merger completed 1970; adopted 1994 | Now "waited until 1994, 24 seasons after the merger" |
| AFL used it 1960–69; Tupa's first NFL two-pointer, week 1 of 1994 vs Cincinnati | VERIFIED | Wikipedia, Two-point conversion | none |
| 1999–2014 regular seasons: 18,592 XP kicks, 98.8%; 1,041 two-point tries, 46.9% | VERIFIED | Recomputed from nflverse pbp (`_pdfbuild/1102-fc/twopt.py`): 18,592, 0.9883; 1,041, 0.4688 | none |
| 1993: 68% of kickoffs returned; 1994: 88%; spot back to the 35 in 2011 | VERIFIED | Wikipedia, Kickoff (citing NFL Operations "Evolution of the rules") | none |
| Plan B 1989–92, 37 protected; 1992 jury verdict in a suit by eight players led by Freeman McNeil (VERIFY) | VERIFIED | Wikipedia, Free agent; UPI, Sept 10, 1992; Baltimore Sun and NFLPA (*McNeil v. NFL*, Judge Doty) | VERIFY removed; sources added to `[^fa]` |
| Jan 1993 settlement (*White v. NFL*, Reggie White lead plaintiff); free agency from March 1, 1993 | VERIFIED | PFHOF 1993; NFLPA "60 Heroes"; Wikipedia, Free agent | none |
| UFA after four accrued seasons; RFA otherwise | VERIFIED | Wikipedia, Free agent | none |
| Reggie White: 4 years, $17M, "then the third-largest [contract] in the league" | CORRECTED | Wikipedia, Reggie White: "the 3rd highest paid player in the NFL, trailing only John Elway and Dan Marino" | Now "made him the third-highest-paid player in the league" |
| Reggie White's three sacks in SB XXXI, a Super Bowl record | VERIFIED | Wikipedia, Reggie White | none |
| Salary cap 1994 at $34.6M against an expected $32M, raised by Fox's bid; hard cap; prorated bonuses | VERIFIED | Wikipedia, Salary cap | none |
| Broncos: "the league found that Denver had deferred money owed to Elway and Davis outside the cap between 1996 and 1998" (VERIFY) | CORRECTED | UPI, Dec 5, 2001: a 2002 third-round pick and $968,000 (incl. $663,000 interest) under deferred-compensation fund rules, a dispute that began over Elway and Davis deferrals. ESPN/AP, Sept 16, 2004: $950,000 and a 2005 third-round pick for "circumventing the salary cap between 1996-98" through agreements to defer salary with interest; no players named | Rewritten as two penalties, with Elway and Davis tied only to the 2001 dispute; VERIFY removed; both sources added to `[^broncos]` |
| 1998 Broncos 14–2; Davis 2,008; SB XXXIII 34–19 over Atlanta, Elway MVP in his last game; Alex Gibbs to Denver in 1995 | VERIFIED | Wikipedia, 1998 Denver Broncos season; 03-02 | none |
| SB XXXIV: Rams 23, Titans 16 | VERIFIED | Wikipedia, Super Bowl XXXIV | none |
| Timeline: 1982 57-day strike and nine games; 1987 24-day strike; replay 1986–91 and back in 1999 with challenges; Marino 5,084 in 1984; Plan B 1989 | VERIFIED | PFHOF Chronology 1980–99; Wikipedia, Instant replay; Dan Marino | none |

**Uncertain or not independently checked:**
- "Today the right tackle is paid almost as well" is a present-day market claim. It is consistent with 2024–25 tackle contracts, but I did not tie it to a source.
- Winslow's 13 catches as a playoff record "at the time" rests on Wikipedia's Epic in Miami page.
- The Arnsparger quote reaches us second-hand (Layden, via Brown/Grantland).
