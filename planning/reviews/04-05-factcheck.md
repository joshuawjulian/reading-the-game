# Fact-check: 04-05 Play-Action, Bootlegs, and Screens

Checked 2026-10-06 against FACTS-current.md, a recomputation of every hard-coded data claim from the chapter's own
FTN + nflverse cell (run in the `rtg` container), the 2026 NFL rulebook (operations.nfl.com, full PDF text) and web
sources. All 7 `<!-- VERIFY -->` comments are resolved and deleted. The chapter builds: `build_pdfs.py
04-05-play-action-boots-screens --html` returns OK. Figures 8, 9, 12 and 17 were re-inspected after the geometry
change.

| Claim | Verdict | Source | Change |
|---|---|---|---|
| Illegal man downfield is a foul if a lineman is more than one yard past the line "on a pass thrown beyond the line"; rule number (VERIFY) | CORRECTED | 2026 NFL Rulebook, Rule 8-3-1 (full text quoted from the PDF): applies "on a scrimmage play during which a legal forward pass is thrown", with no beyond-the-line condition; Art. 2 covers advancing after the throw; 5 yards | Prose now says "on any play with a forward pass"; footnote cites Rule 8, Sec. 3, Art. 1 with the quoted text (it previously said Rule 7) |
| "The one-yard limit applies only to passes thrown beyond the line; on a screen, linemen can be ten yards downfield when the ball is thrown" (VERIFY) | CORRECTED (substantive) | Rule 8-3-1 has no behind-the-line exception. The college rule does: NCAA 7-3-10, "legal forward pass that crosses the neutral zone" (SDCFOA). NFL example of IDP officiated on a screen: PFT, Sept. 27, 2024 (Prescott-to-Dowdle flag picked up by replay assist on lineman position) | Screens paragraph rewritten (NFL linemen release flat and turn up after the throw; college differs). Slow-screen text, the swing/screen "tell", the Watch-for-it bullet, the Takeaway, and Predict 3's question and answer are all reworded. **Diagram geometry changed:** in `slow_screen()` (Figs 8, 9, 17) and `screen_vs_blitz()` (Fig 12), the released linemen now end about 0.6–0.8 yd past the line. Before, they were 2–3 yd past it before the throw. The Fig 8 caption is updated |
| Baldwin's 2018 Football Outsiders column: title and date (VERIFY) | VERIFIED + made precise | "Rushing Success and Play-Action Passing" (FO guest column, Feb 2018, 2011–17 charting; the title appears in the Wikipedia refs; the date and findings come from Acme Packing Co., Aug 3 2018) | Footnote now gives the title, date and source. Prose: the findings are described as "how often or how well it had run before them" (the source's framing), replacing the unsourced list "that season, in that game, earlier on that drive" |
| Baldwin "later helped build the nflfastR models" | VERIFIED (reworded) | nflfastR is authored by Sebastian Carl and Ben Baldwin (nflfastr.com) | Now "later co-created nflfastR"; cited |
| Hermsmeyer, FiveThirtyEight 2018, "Can NFL Coaches Overuse Play-Action? They Haven't Yet"; the linebacker mechanism | VERIFIED + made precise | The Power Rank (Ed Feng, Sept 10 2021) links the 538 URL and summarizes it: tracking data showed middle-linebacker "wasted motion" was the same on the 1st and the 12th play-action pass | Prose now states the actual finding; footnote gives the URL |
| Goff 2018: play-action on "roughly a third" of dropbacks, the league's highest (VERIFY) | VERIFIED + made precise | Robert Mays, The Ringer, Feb 1 2019: 34.6%, "highest mark in the league by more than 4 percentage points, according to PFF" | Text now "about 35 percent"; footnote quotes it (the Wikipedia citation did not contain the stat) |
| "Play-action rates rose across the league afterward" (after 2018) | CORRECTED | The Ringer (Danny Kelly, Sept 3 2019, citing FO Almanac): the rate rose from 18% in 2016 to 24% in 2018, so the rise came before and during 2018; other charters show 2019 flat or slightly down | Now: "The league was already moving that way: 18% (2016) to 24% (2018)", plus a note that charting services are not comparable; new fn `parate` |
| Football etymology of "bootleg" (VERIFY) | SOFTENED | Wikipedia "Bootleg play" (hides the ball by his thigh, like Prohibition bootleggers); Merriam-Webster for the older smuggler sense | Text: "Nobody recorded who named it, but the usual story is…"; footnote rewritten |
| Reid's screen game; Westbrook as its weapon (VERIFY) | VERIFIED | Jeff McLane, Philadelphia Inquirer, Nov 26 2020: Reid, "primarily with Staley, Brian Westbrook and LeSean McCoy, diagramed and dialed up screens like it was an art form" | Footnote cites and quotes it (it previously cited Westbrook's Wikipedia page) |
| Reid: Packers 1992–98 under Holmgren, Eagles HC 1999–2012, Chiefs from 2013 | VERIFIED | PFR coach page | None |
| Super Bowl LIII: the Rams scored 3; New England's defensive plan (VERIFY) | VERIFIED (detail added from source) | Ben Linsey, PFF, Feb 4 2019: pressure on 42.9% of Goff's dropbacks, stunts on 18 dropbacks, the middle of the field packed | The generic "held up against the run looks" replaced with the sourced detail; new fn `sb53` |
| 2018 Rams 13–3, lost SB LIII 13–3 | VERIFIED | PFR 2018 Rams | None |
| Kubiak Denver OC 1995–2005 under Shanahan; Gibbs's zone; Elway's last four seasons (1995–98) | VERIFIED | PFR (Kubiak, Elway) | None |
| Kyle Shanahan ATL OC 2016, Ryan 2016 AP MVP; SF HC 2017 | VERIFIED | PFR 2016 awards; PFR Shanahan | None |
| McVay and LaFleur coached on Kyle Shanahan's staffs (WAS; LaFleur also ATL) (spot-check) | VERIFIED | PFR: McVay WAS assistant 2010–13 while Shanahan was OC; LaFleur WAS QB coach 2010–13, ATL QB coach 2015–16 | Footnote now states the years |
| Seattle 2025: Klint Kubiak OC (one year), Sam Darnold QB, won SB LX 29–13; Kubiak is Raiders HC for 2026 (spot-check) | VERIFIED | FACTS-current §1, C2, §9; CBS Sports (Macdonald: "Sam's our starting quarterback") | None |
| Ben Johnson's Bears (2025); McDaniel's Dolphins, LaFleur's Packers and Kubiak's Seahawks as 2025 Shanahan-tree offenses | VERIFIED | FACTS-current §9 (these are 2025 staffs and are labelled 2025 in the text) | None |
| Forward pass legal from 1906 | VERIFIED | Wikipedia "Forward pass"; PFHOF | Dropped the vague PFHOF "history" pointer that had no URL |
| BDB 2025 = 2022 season weeks 1–9, 10 Hz, `playAction` and `dropbackType` in plays.csv | VERIFIED | Kaggle BDB 2025 data description; `gridiron/bdb.py` | None |
| Data: PA +0.11 vs +0.00 EPA (2022–25); PA ahead in each of the 4 seasons; r = +0.09 (rush EPA) and +0.24 (run rate); 78% of team-seasons | VERIFIED | Recomputed: by season PA/no-PA = .094/−.005, .097/−.026, .144/.025, .120/.020 | None |
| Under center: 82% of dropbacks use PA (2025) ("four of every five"); shotgun 10% | VERIFIED | Recomputed | None |
| UC+PA is the most productive dropback (+0.13); the shotgun fake adds more vs. its own alignment (+0.09 vs +0.05) | VERIFIED | Recomputed (U: .080/.129; S: −.002/.084; n_U,no-fake = 2,559) | None. The writer's warning stands: do not claim the under-center fake "adds more" |
| Air yards equal (7.8 vs 7.7), YAC +1.5 | VERIFIED | Recomputed | None |
| PA out of pocket 30% vs 15% | VERIFIED | Recomputed | None |
| Screens −0.18 (3 rushers) to +0.03 (6+); better than other passes vs 6+ (−0.06); RB screens climb most steeply (−0.17 → +0.14, n = 110) | VERIFIED | Recomputed | None |
| KC most screens (327, +0.11) vs league −0.07 | VERIFIED | Recomputed (DEN 283 next) | None |
| 2025: Rams led PA rate (35%); "Bears next" (31%); MIA/GB/SEA top half (4th/7th/11th); SF 21st; SEA biggest gap (+0.40 vs +0.02); 22 of 32 better with PA | VERIFIED | Recomputed | None |
| "The Chiefs were near the bottom" in PA rate | VERIFIED (made exact) | Recomputed: 32nd of 32 | Now computed inline (`ordinal(RANK['KC'])` renders "32nd") |
| Football-technical claims (LB keys, run-action protection, under-center vs gun mesh, naked/protected boot, leak, shot-play structure, swing vs flare, tunnel/jailbreak naming variance) | VERIFIED (consistent with standard coaching sources and with 03-02, 03-05, 04-02) | Brown, *The Art of Smart Football*; prerequisite chapters | None |

## Counts
VERIFIED 25 (8 of them made more precise or given a better source) · CORRECTED 3 (the IDP rule number and wording, the NFL screen exception, play-action rates "rose afterward") · SOFTENED 1 (bootleg etymology) · REMOVED 0. Seven VERIFY comments were resolved: 2 CORRECTED, 4 VERIFIED, 1 SOFTENED.

## Still uncertain / for a human
- **The screen rule is the big change.** The NFL rule text (8-3-1) has no exception for passes behind the line, so the chapter now teaches "release flat, turn up after the throw". In real NFL games, officials seem to give screen blockers some leeway, but no officiating source states a tolerance, so the chapter does not claim one. 04-06 (RPOs) owns this rule and should use the same NFL-versus-college framing.
- The ProFootballTalk example does not say where the ball was caught. It is cited only to show that the flag is officiated on screens.
- The Baldwin column's own URL could not be fetched (Football Outsiders' archive has moved). Its title and date come from the Wikipedia reference list and from Acme Packing Company.
