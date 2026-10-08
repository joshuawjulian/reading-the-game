# Fact-check: 13-03 Win Probability and Decision Analysis

Checked 2026-10-08 against FACTS-current.md, nflverse play-by-play (the chapter's code re-run in the `rtg` container, plus direct pbp queries for Super Bowl LI and the 2023 NFC Championship Game), the Romer paper PDF, the nfl4th source on GitHub, Crossref DOI records and web sources.
All 8 `<!-- VERIFY -->` comments are resolved and removed. The chapter builds (`build_pdfs.py 13-03-win-probability-and-fourth-down --html`: OK, 39 pages). Each footnote is still referenced exactly once; two footnotes were added (`ngsguide`, `burke09`).

| Claim | Verdict | Source | Change |
|---|---|---|---|
| SB LI: Feb 5 2017, NRG Stadium; NE 34-28 OT; first OT Super Bowl; 25-point comeback; Coleman TD at 8:31 Q3 made it 28-3 | VERIFIED | Wikipedia SB LI; nflverse pbp `2016_21_NE_ATL` | None |
| nflverse WP for ATL 99% after the Coleman TD | VERIFIED | pbp home_wp_post 0.990 | None |
| NE favoured by about 3 | VERIFIED | pbp spread_line −3.0 | None |
| Fig. caption: Falcons above 95% "for nearly 50 minutes" | CORRECTED | Re-computed from pbp: about 23 minutes, almost all after halftime | Now "more than 20 minutes of game time, nearly all of it after halftime" |
| Annotation times: Hightower strip-sack 8:31 Q4; Flowers sack 3:56; Edelman catch 2:28; TD + 2 at 0:57 | VERIFIED | pbp | None |
| Film room: 4:40, 1st-and-10 at NE 22 up 28-20 (Freeman −1); 3:56 Flowers sack −12; 3:50 holding wipes out 9-yd catch; 3:38 punt | VERIFIED | pbp | None |
| "The scoring plays of the comeback are not on the list... touchdowns early in Q4, down 16 or 8" | CORRECTED | pbp: the tying 2-pt try *is* on the list; NE's TDs were late Q3 and 5:56 Q4 | Reworded: "most of the comeback's scoring plays"; names the Q3 TD, the FG and the 5:56 TD + 2 (down 19, 16, 8) |
| Blount fumble and Alford pick-six "in a scoreless or one-score game" | CORRECTED | pbp: fumble at 0-0, pick-six at 14-0 (two scores) | Now "at 0-0 and 14-0" |
| Shanahan was ATL OC and play-caller; regrets the 2nd-down sack; "I wish I had dialed something up differently" | VERIFIED | CBS Sports, Sean Wagner-McGough, May 19 2017 (Rich Eisen Show) | Footnote byline corrected (was "Will Brinson") |
| Shanahan rejects the "just run it" narrative | VERIFIED | ESPN, Nick Wagoner, Jan 20 2020 (direct quote) | NESN link (redirects to the homepage) replaced with ESPN |
| "Two weeks later he was the 49ers' head coach" | CORRECTED | CBS Sports / NBC Sports Bay Area: hire announced Feb 6 2017, the day after the game | Now "The next day the 49ers announced him as their head coach"; source added to fn `shanahan` |
| Stern 1991: SD about 14 (13.86) around the line; Am. Stat. 45(3):179-183; DOI | VERIFIED | Crossref 10.1080/00031305.1991.10475798 | None |
| Stern 1994 Brownian motion, JASA 89(427):1128-1134; DOI | VERIFIED | Crossref 10.1080/01621459.1994.10476851 | None |
| nflverse wp is XGBoost with about a dozen inputs; vegas_wp adds the spread | VERIFIED | Baldwin, OSF "nflfastR EP, WP, and CP models" (11 features listed) | Footnote date clarified (Sept 2020, updated Feb 2021) |
| nflfastR inputs "include the spread" | CORRECTED | Same: spread only in the second (spread-adjusted) model; home field is an input | Text now lists home field and "(plus the pregame spread in its second version)" |
| Burke's WP model "from 2008 or so" | VERIFIED | The Ringer, Heifetz, Aug 15 2019 (began WP charts in 2008) | Now "begun in 2008"; Ringer added to fn `wphistory` |
| Lock & Nettleton random forest, JQAS 10(2) 2014: 197-205; DOI | VERIFIED | Crossref; Iowa State repository | None |
| nflscrapR GAM "(2017)" | SOFTENED | nflWAR, JQAS 15(3) 2019: 163-183 describes the GAM; exact first-release year not pinned | Now "(late 2010s)"; full title and pages added |
| ESPN/NGS/networks run proprietary models | VERIFIED | General (ESPN Analytics and NGS figures cited in fn `lionsmodels`) | None |
| Calibration: "both a touch overconfident at the edges ... a common finding" | CORRECTED / SOFTENED | Re-run: <5% bin forecast 1.3%, actual 2.3% (nflverse); >95% bin 98.5% vs 98.6% (nflverse on target), random walk 98.7% vs 97.3% | Text and caption now say "at the low end"; notes that nflverse is on target at the top; "a common finding" removed (no source) |
| Leverage index idea and name from Tom Tango | VERIFIED | Tango, "Crucial Situations," THT May 1 2006; FanGraphs Library LI | insidethebook URL replaced |
| Burke adapted LI for football on Advanced NFL Stats | REMOVED | No source found | Now "football analysts borrowed it" |
| Top 10% of plays = 39% of WP movement; leverage peaks down 1-3 late | VERIFIED | Chapter code (re-run) | None |
| NFC CG Jan 28 2024: 4th-and-2 at SF 28, 7:03 Q3, DET up 24-10, Goff incomplete (Reynolds); 4th-and-3 at SF 30, 7:38 Q4, down 27-24, incomplete (St. Brown); final 34-31 | VERIFIED | pbp `2023_21_DET_SF` | None |
| 46-yard FG from the SF 28 | VERIFIED | 28 + 18 | None |
| ESPN: 90.5 vs 90.3 and 39.1 vs 38.8 | VERIFIED | NBC Sports Bay Area, Jordan Elliott, Jan 28 2024 (citing ESPN Stats & Info); NBC Sports, Denny Carter, Jan 29 2024 | Byline and exact date added |
| NGS: 86.8 vs 85.8 and 32.7 vs 30.2 | VERIFIED | The Ringer, Ben Solak, Jan 29 2024 | None |
| Missed FG: ball at the spot of the kick or the 20 | VERIFIED | NFL rule (spot of kick / 20) | None |
| Romer 2006, JPE 114(2):340-365; DOI | VERIFIED | Crossref 10.1086/501171 | Page refs added |
| Romer "suggested coaches may protect their jobs rather than maximise wins" | CORRECTED | Romer pp. 361-362: (1) actors risk-averse over win probability (fans, owners or coaches; possibly agency problems); (2) imperfect maximizers relying on experience and intuition. Job security not named | Madden callout rewritten to his two explanations |
| Romer "concluded that teams' choices cost them wins every season" | CORRECTED | Romer p. 360: rough estimate +2.1 pp a game, "slightly more than one additional win every three seasons" | Now states the estimate |
| Carter & Machol 1978, Mgmt Sci 24(16):1758-1762; DOI | VERIFIED | Crossref | None |
| Carter & Machol: teams kicked too often "near the opponent's goal line" | CORRECTED | Abstract: an FG try on fourth-and-short is "a considerably poorer strategy than is generally thought" | Now quotes the abstract |
| Carter built the first EP table (1971) | VERIFIED | Consistent with 13-02; NYT bot coverage cites Carter & Machol 1971 | None |
| NYT 4th Down Bot, 2013, with Burke; EP for most of the game, WP with about 10 min left in Q4; live on site and Twitter | VERIFIED | Nieman Lab, Dec 6 2013; FanGraphs TechGraphs | Launch month not pinned; text gives only the year, so nothing to change. Footnote now credits the EP/WP switch to the 2013 article |
| Burke joined ESPN in 2015; Times rebuilt the bot | VERIFIED | Nieman Lab, Justin Ellis, Oct 14 2015; ESPN Front Row, June 2015 | "when" changed to "after" |
| Baldwin's nfl4th: Athletic article 2020; R package; model pieces; listed limitations; Twitter bot | VERIFIED | nfl4th README (CRAN); nfl4th research page (Athletic URL dated 2020/10/28); Brill et al. (@ben_bot_baldwin) | None |
| Analysts' fourth-down models often fit conversion on 3rd and 4th downs together | VERIFIED | nfl4th `data-raw/_go_for_it_and_2pt_models.R` (`down %in% c(3, 4)`) | Added to fn `nfl4th` |
| "By the early 2020s most front offices employed analysts whose work includes 4th-down and 2-pt recommendations" | CORRECTED | NFL.com NGS Decision Guide: "Nearly every NFL team has at least one staff member crunching the numbers"; rules ban technology in the coach's booth, so the advice is printed, often on a single card | Rewritten to the NGS wording; new fn `ngsguide` |
| Brill, Yurko & Wyner "Analytics, have some humility"; arXiv 2311.03490, Nov 2023, revised Jan 2025; resample whole games; uncertainty far greater than analysts express | VERIFIED | arXiv abstract and v6 HTML (games, then drives within games, resampled) | None |
| Belichick 2009: 4th-and-2 at own 28, up 34-28, 2:08 left | VERIFIED | Consistent with 11-04; SI Posnanski Nov 16 2009 | None |
| Burke's 2009 analysis: go by about 9 (79 vs 70); 30% after a punt; TD from about the 30 "a little over half" (53%) | VERIFIED | SI, Posnanski, Nov 16 2009 | New fn `burke09` |
| 2025 regular-season OT: both teams get a possession; ties possible | VERIFIED | 2025 rule change (playoff OT rule extended to the regular season) | None |
| 2025 kickoff touchback moved to the 35 | VERIFIED | FACTS-current §3 | None |
| XP moved back in 2015 | VERIFIED | NFL.com May 2015 (as in the 01-01 check) | None |
| Two-point success 47.8%, XP 94.4% (2016-25); down-14 break-even about 35%; go-first 59% vs 46% | VERIFIED | Chapter code (re-run) | None |
| Down 8 after a TD: 0% in 2016-17, 53% in 2025; "about 12 to 21 Q4 tries a season" | VERIFIED | Re-run: 20, 16, 19, 16, 19, 12, 12, 21, 13, 17 | None |
| Clear-go go rate 19% (2016) to 41% (2025); toss-ups about doubled; clear-kick near 0 | VERIFIED | Re-run (6.0% to 13.6% on toss-ups) | None |
| Team scatter caption: "roughly 70-110 clear-go fourth downs" per team | CORRECTED | Re-run: 74 to 140 (CAR 117, max 140) | Now "roughly 75-140" |
| Detroit highest follow rate 2023-25 (67%) and rank 1 for fewest WP lost | VERIFIED | Re-run (DET 0.0157 vs BUF 0.0157, a near tie) | None |
| Belichick model check: our model says punt by about 2; drives needing a TD scored 28% | VERIFIED | Re-run | None |
| Map claims: 4th-and-1 break-even in the 40s; 4th-and-8 at own 30 about mid-40s; punt nets about 40 yd from own 34; 46-yd FG about 80% | VERIFIED | Re-run (45-49%; 44.8%; 43.6 yd; 81%) | None |
| Timeouts worth about +1.7 / −1.1 WP points late in one-score games | VERIFIED | Chapter code | None |
| Iced kicks: 161 (fewer than 200), −6.1 vs −3.5 against expectation | VERIFIED | Chapter code | None |
| Scorecasting: icing doesn't work | VERIFIED | Freakonomics/NFL.com "Why Even Ice a Kicker?" Nov 2011 (2001-09 pressure kicks, distance-controlled) | Chapter title claim dropped; book's full title and the summary link added |
| Detroit 2023 offense and SF defense among the league's best | VERIFIED | PFR 2023 (DET top 5 in points scored; SF top 3 in points allowed) | None |
| 40-second play clock ("about forty seconds to decide") | VERIFIED | NFL rule 4-6 | None |

**Counts (table rows):** VERIFIED 44 · CORRECTED 12 (one of them also SOFTENED: calibration "common finding") · SOFTENED 1 (nflscrapR year) · REMOVED 1 (Burke's football LI).

**Notes / uncertain**
- The SB LI biggest-swing table (computed from nflverse) lists a 27-yard Brady-to-Edelman completion at "Q2 15:00" as worth +10.1 points of WP at 0-0. That is large for that situation and may be a quarter-boundary artifact in nflverse's `home_wp`/`home_wp_post`. It is data, not prose, so it was left as is; worth a look by the writer.
- The NYT bot's exact 2013 launch month could not be confirmed (Nieman Lab returns 403). The text gives only "2013", which is verified.
- The NGS Decision Guide page shows no publication date, so none is given.
