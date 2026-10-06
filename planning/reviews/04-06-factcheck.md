# Fact-check log: 04-06 Run-Pass Options

Checked 2026-10-06. Sources: the 2026 NFL rulebook PDF (text extracted locally), the 2026 NCAA rules study compilation (amarefs.org PDF, text extracted in the `rtg` container), web sources, and nflverse pbp + FTN charting re-queried in `rtg`. All six `<!-- VERIFY -->` comments are resolved and removed. Every footnote is referenced exactly once; one footnote was added (`[^belichick]`). Build `build_pdfs.py 04-06-rpos --html`: OK, 20 pages. Page 9 (fig-ineligible) was re-rasterized and checked after its labels changed.

| Claim | Verdict | Source | Change |
|---|---|---|---|
| NFL 8-3-1: foul if entire body >1 yd past LOS before a legal forward pass; exception for contact within 1 yd on initial charge; Item 2 (let go and advance); 5 yds from previous spot, no loss of down | VERIFIED | 2026 NFL rulebook, 8-3-1 Items 1–2 + penalty | none |
| NFL rule has no "crosses the line" clause; it applies to any legal forward pass | VERIFIED | 2026 rulebook 8-3-1 ("On a scrimmage play during which a legal forward pass is thrown") | none |
| OPI 8-5-1 "regardless of ... whether it crosses the line"; 8-5-4(a) blocking >1 yd "clearly prior" to the pass | VERIFIED | 2026 rulebook 8-5-1, 8-5-4 | none |
| VERIFY 1: how strictly officials call OPI on screens/RPOs "varies" | SOFTENED | Hartwell, NBC Sports Boston, Dec. 6, 2019 (Belichick: "a tough call for the officials") | Now says it is a full-speed judgment of "clearly prior," quoting Belichick; new `[^belichick]` |
| VERIFY 2: NCAA 7-3-10, 3 yds beyond NZ, only for passes that cross the NZ, 5 yds | VERIFIED | 2026 NCAA rules compilation (amarefs.org), Rule 7-3-10 and A.R. 7-3-10-I–III | Footnote now quotes the 2026 text; adds that NCAA judges *any part* of the body (A.R. 7-3-10-III) and NFL the entire body |
| College: "three yards is enough for a guard to climb onto a linebacker"; fig-ineligible says guards "climbed onto both linebackers ... legally"; college linemen "run-block more or less normally ... over linebackers who have been blocked" | CORRECTED | NCAA 7-3-8-b + A.R. 7-3-10-II: contact beyond the NZ during a pass that crosses it is OPI unless it began on the initial charge within 1 yd of the NZ and is kept within 3 yds | Text: release toward the LB is legal, but blocking him downfield is OPI. College bullet reworded. Caption and two on-field labels ("RG climbing to / the Mike", "LG to the Will") reworded. Drill 3 college answer gets a one-sentence OPI caveat. 7-3-8-b quoted in `[^ncaa]` |
| 2015 NCAA proposal to move to 1 yd, tabled by the oversight panel; still 3 yds in 2026 | VERIFIED | SI Wire, Mar. 6, 2015; FootballScoop; 2026 NCAA text | The dead ncaa.org link (it now redirects to /news) is replaced with FootballScoop |
| Neutral zone = the length of the ball between the lines | VERIFIED | standard definition (NCAA Rule 2) | none |
| Referee's announcement is "usually" "ineligible man downfield" | SOFTENED | announcements vary ("ineligible downfield on the pass") | "usually" → "often" |
| VERIFY 3: CBS origins piece, byline and date | CORRECTED | cbssports.com page | Now Dennis Dodd, Nov. 8, 2018 |
| Leach brought the Air Raid to Oklahoma in 1999; Rodriguez a "founding father" of the zone read | VERIFIED | Dodd, CBS 2018 | Leach is paraphrased (the earlier "forefathers" quote wasn't checked word for word) |
| Mumme/Kentucky gave Couch bubble-or-handoff tags; Rodriguez put slants and bubbles in his offense at Tulane and Clemson | VERIFIED (secondary) | Calabrese, Action Network, June 2024 | Source added to `[^origins]` |
| Rodriguez's zone read grew out of a fumbled practice handoff at Glenville State | VERIFIED | consistent with 03-04 (AP via SI, 2014; fact-checked there) | none |
| Meyer: Utah, early 2000s, a receiver's missed assignment became a bubble; Mullen and Whittingham put it in the playbook | VERIFIED (as Meyer's claim) | Farner, Saturday Down South, Sept. 3, 2019 | none (already framed as a disputed story) |
| Favre's "bored" RPO story; did it before telling his coach; on Gruden's QB Camp | VERIFIED (as Favre's claim) | Dubin, CBS Sports, June 11, 2018 | none |
| VERIFY 4: NFL.com Shanahan/Baylor article date | VERIFIED | page metadata datePublished 2012-09-12 | Footnote dated Sept. 12, 2012 |
| The "we had running plays called ... bubbles early" quote, which the text implicitly gave to Griffin | CORRECTED | Rosenthal, NFL.com: the speaker is Mike Shanahan | Now "After Griffin's first game, Shanahan put it this way: ..." |
| RG3 came from Art Briles's Baylor to Washington in 2012 | VERIFIED | NFL.com 2012; Washington Times, Sept. 2012 | none |
| PFF: league RPO share about 4% (2016) to about 8% (2018); KC led in 2017 (17.1%) and 2018 (25.0%); Eagles 2nd in 2017; Pederson on Reid's KC staff 2013–15; Nagy was Pederson's successor; Bears 2.7% → 19.2% | VERIFIED | Treash, PFF, May 17, 2019 | none |
| PFF series 2016–2025 (peak 10.52% in 2023; 8.96% in 2024; 7.95% in 2025) | VERIFIED | Carragher, PFF, June 25, 2026 | none |
| Mahomes has the most RPO pass attempts since 2020 (391; Rodgers 287, Allen 268) | VERIFIED | Carragher 2026 | none |
| PFF 2021–25: 4.53 vs 5.43 yds/play; 52.3% vs 48.1% success | VERIFIED | Carragher 2026 | none |
| PFF 8–10.5% vs FTN 4–6% for the same seasons | VERIFIED | Carragher; recomputed FTN | none |
| VERIFY 5: Wentz tore his ACL against the Rams in December 2017 | VERIFIED | AP via Boston.com, Dec. 11, 2017 (game Dec. 10, 43–35 at LA); pbp 2017_14_PHI_LA dated 2017-12-10 | Source added to `[^foles]` |
| Reich quote ("centered around accurate throwing...") | VERIFIED | McManus, ESPN, Jan. 26, 2018 | Footnote no longer claims the NFC line is from ESPN |
| Foles completed 93.9% of his RPO throws that season (PFF) | VERIFIED | Browne, theScore ("this season, according to PFF") | none |
| VERIFY 6: theScore article date | SOFTENED | page shows no date; written before Super Bowl LII | "Jan. 2018" → "before Super Bowl LII, 2018" |
| VERIFY 6: NFC Championship: Foles 26/33, 352 yds, 3 TD; Eagles 38–7 vs MIN, Jan. 21, 2018 | VERIFIED | nflverse pbp 2017_20_MIN_PHI (PFR returned 403) | Cited in `[^foles]` |
| Super Bowl LII: Feb. 4, 2018, Minneapolis, 41–33; Foles 373 yds, 3 TD passes, caught a TD; MVP | VERIFIED | pbp 2017_21_PHI_NE (TD catch from T. Burton); NFL.com; Wikipedia | none |
| Ajayi, Blount and Clement in the 2017 Eagles backfield | VERIFIED | standard record (Ajayi acquired Oct. 2017) | none |
| Chiefs QB went from Alex Smith to Mahomes | VERIFIED | standard record | none |
| Steichen was Eagles OC 2021–22 and became Colts HC in Feb. 2023; Eagles reached Super Bowl LVII in the 2022 season | VERIFIED | Wikipedia; FACTS | none |
| FTN RPO rate 5.0 / 5.3 / 3.6 / 6.2% for 2022–25 | VERIFIED | recomputed in rtg: 5.04 / 5.30 / 3.57 / 6.16% | none |
| Leaders: PHI 2022 (13.5%), IND 2023 (18.3%, highest team-season of the four), KC 2025 (14.4%, more than twice the league rate) | VERIFIED | recomputed | none |
| Shanahan-tree, under-center teams barely use RPOs | VERIFIED | recomputed: SF and LA among the lowest each year (SF 0.7%, LA 0.5% in 2025) | none |
| 69% of charted RPOs were handed off | VERIFIED | recomputed: 69.2% | none |
| 246 ineligible-downfield-pass fouls (REG 2022–25); 24% on RPOs | VERIFIED | recomputed: 246 REG (84/46/70/46), all 246 match an FTN row, 23.6% RPO; 257 with the postseason included | none. The writer's "270" was probably a different filter; 246 is right for the regular season |
| Air yards (57% vs 21% at or behind the LOS), EPA, success and box-count splits | VERIFIED (live code) | chapter's own inline code (same join as above) | none |
| BDB 2025 `plays.csv` has `pff_runPassOption`; `pass_forward` event | VERIFIED | FACTS §8 | none |
| Glance footnote quotes ("five-step skinny post that looks similar to a slant", "decides to come down and play the run") | CORRECTED | Hammer and Rails, Aug. 30, 2022: neither phrase appears | Replaced with the article's real wording ("incorporates a skinny post route into the RPO system", "drops into a zone, this is a hand-off", "commits to the run ... replaces the linebacker with his route") |
| Scouting Academy post-snap RPO read | VERIFIED | page (Rodgers reading LB Lofton) | none |
| "You'll need" play-action recap vs 04-05 | VERIFIED | 04-05 (line fires out as if run-blocking, can't really run-block) | none |

**Counts:** VERIFIED 35 (including two verified as secondary sources or as the coach's own claim), CORRECTED 5, SOFTENED 3, REMOVED 0.

**Uncertain or for other chapters:**
- The NCAA text comes from an officials' association's 2026 study compilation, not the NCAA's own PDF. It matches SDCFOA and Wikipedia.
- **04-05 consistency:** the 04-05 slow-screen figure has linemen releasing "two or three yards past the line" before a pass caught behind the line. NFL 8-3-1 has no exemption for passes behind the line. That chapter's fact-checker should look at how it frames this.
