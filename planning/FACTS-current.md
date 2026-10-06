# Current State of the NFL: Fact Sheet for Writers

_Checked 2026-10-06 against web sources and nflverse data. Covers facts through the start of the 2026 season._

**Confidence labels**
- **VERIFIED**: confirmed by an official or primary source (NFL.com, operations.nfl.com, team site, nflverse data or code), or by two independent reputable outlets.
- **LIKELY**: one reputable secondary source, or several sources that agree but none of them primary.
- **UNVERIFIED**: could not confirm. Do not print it without checking again.

Note: Pro Football Reference blocked automated fetches (HTTP 403). Score lines were therefore checked against Wikipedia, NFL.com, and wire reports. Before a chapter is published, a human should spot-check final scores on PFR.

---

## 0. Curriculum corrections (read this first)

| # | Where in CURRICULUM.md | Problem | Correction |
|---|---|---|---|
| C1 | 12-07 objectives; §9 item 7 | The text says only "Johnson to Chicago, Glenn to the Jets." That leaves out the follow-on changes. | 2025 OC **John Morton** was fired after one season. **Dan Campbell took over play-calling midway through 2025.** The 2026 OC is **Drew Petzing** (formerly Cardinals OC), the Lions' third OC in three years. Kelvin Sheppard remains DC. |
| C2 | 12-03 "Map the tree: McVay, LaFleur, McDaniel, Kubiak, Coen"; 04-08 "Shanahan -> ... McDaniel / Kubiak" | Several jobs changed after 2025. | **Klint Kubiak** is now **Raiders head coach** (2026). **Mike McDaniel** was fired by Miami in Jan 2026 and is now **Chargers OC**. **Mike LaFleur** left as Rams OC to become **Cardinals head coach**. Seattle's 2026 OC is **Brian Fleury**, who came from the 49ers staff. Any "2025 staffs" map has to be labelled 2025, and the 2026 map is different. |
| C3 | 12-05 Ravens case study (Monken 2023, Henry 2024) | The era has ended. | **John Harbaugh was fired in Jan 2026** after 18 seasons and is now **Giants HC**. **Todd Monken** is **Browns HC**. The Ravens' 2026 staff is HC **Jesse Minter**, OC **Declan Doyle**, DC **Anthony Weaver**. Write the case study as a closed 2019–2025 era. |
| C4 | 12-04 Chiefs "2018-2025" | OC detail | **Matt Nagy** was OC from 2023 to 2025 and is now Giants OC. **Eric Bieniemy returned as Chiefs OC** in Jan 2026. Spagnuolo is still DC. |
| C5 | 13-01, 06-05, 06-06, 13-04 (nflverse charts) | §9 item 5 assumes coverage data is "patchy" and that FTN-only seasons may be needed. That is not quite right. | Coverage type is available in `load_participation()` for **2018–2025**, on about 41–50% of rows (essentially dropbacks). It is **missing for 2016–2017**. There is a **source break between 2022 and 2023**: NGS supplies 2016–2022 and FTN supplies 2023 onward. Formation labels and coverage labels are coded differently on each side of the break. See §7. |
| C6 | 11-05 "[C] Two-high rate vs 11-personnel rate vs under-center rate, 2016-2025" | Two-high data starts in 2018. | Start the two-high series in **2018**. Mark the 2022/2023 source break on the chart, or use published NGS numbers (§10). |
| C7 | 02-05 "[C] Motion rate by team, 2022-2025 (FTN charting)" | This is fine, but it needs a definition note. | FTN `is_motion` means "motion occurred on the play before **or at** the time of the snap." It is **not** motion-at-the-snap only, and it is not the same as PFF's "shift/motion" rate. Don't mix the two series. |
| C8 | 09-02 "the 2025 adjustments"; Appendix E "current as of 2025 season" | Kickoff rules changed **again for 2026**. | See §3. Make Appendix E current as of 2026. |
| C9 | 10-03 / 12-06 "2025 tush-push vote" | The facts are right. Add the 2026 follow-up. | The 2025 ban failed **22–10**, two votes short of the 24 needed. In 2026 **no team proposed a ban**, and the play is legal for the 2026 season. |
| C10 | 12-03 / 12-08 "Fangio's 2024 Eagles" | Still accurate. | Fangio **remains Eagles DC in 2026**. The Eagles' OC churn continues: Patullo (2025) left, and **Sean Mannion** is OC in 2026, the fifth straight year with a new OC. |
| C11 | §9 item 1 Super Bowl LX assumption | **Correct.** | Seattle beat New England **29–13**. Details are in §1. |
| C12 | §9 item 10 (NCAA ineligible downfield) | The rule has not changed. | The college threshold is still **3 yards**. NFL is 1 yard. A 2015 proposal to move college to 1 yard was tabled. No 2025 or 2026 change was found. (LIKELY) |

No other 2023–2026 example in the chapter specs looked wrong. These items checked out or are plausible: McCaffrey 2023, the Dolphins' 2023 motion, the Chiefs' Super Bowl LVII motion TDs, the 2018 NFC Championship no-call leading to 2019 PI review, Super Bowl LIX's four-man pressure, and Lions jumbo with an eligible tackle.

---

## 1. Super Bowls

| Game | Date / venue | Result | MVP | Confidence |
|---|---|---|---|---|
| **LVIII** | Feb 11, 2024, Allegiant Stadium, Las Vegas | **Chiefs 25, 49ers 22 (OT)**. This was the second Super Bowl to go to OT (after LI) and the first under the 2022 playoff OT rule. SF received first and kicked a FG. KC answered with a TD. | Patrick Mahomes | VERIFIED |
| **LIX** | Feb 9, 2025, Caesars Superdome, New Orleans | **Eagles 40, Chiefs 22**. Hurts scored a TD on a tush push. The Eagles' pressure came from four-man rushes. | Jalen Hurts | VERIFIED |
| **LX** | Feb 8, 2026, Levi's Stadium, Santa Clara | **Seahawks 29, Patriots 13**. By quarter, SEA led 3–0, 12–0, and 19–0 before a 29–13 final. Seattle sacked Drake Maye 6 times. Uchenna Nwosu returned an interception 45 yards for a TD. Jason Myers made **5 FGs, a Super Bowl record**. Kenneth Walker III ran 27 times for 135 yards. Coaches: SEA had HC Mike Macdonald, OC Klint Kubiak, DC Aden Durde. NE had HC Mike Vrabel and OC Josh McDaniels. | Kenneth Walker III (RB) | VERIFIED (score, MVP, venue); LIKELY (quarter-by-quarter scores, Nwosu detail) |

Sources: https://en.wikipedia.org/wiki/Super_Bowl_LX · https://www.fox13seattle.com/news/super-bowl-live-updates-seahawks-patriots · https://www.cbsnews.com/amp/news/nfl-mvp-super-bowl-jalen-hurts-eagles · https://www.nfl.com/videos/49ers-vs-chiefs-highlights-super-bowl-lviii

Caution: one automated summary of the LX Wikipedia page named the wrong Seattle coordinators. Kubiak was OC and Durde was DC, as confirmed on https://en.wikipedia.org/wiki/2026_Seattle_Seahawks_season and in the Fleury hiring reports.

---

## 2. 2025 season

**Playoff seeds** (VERIFIED: seeds and wild-card pairings are internally consistent)
- **AFC:** 1 Denver (14–3, West) · 2 New England (14–3, East) · 3 Jacksonville (13–4, South) · 4 Pittsburgh (10–7, North) · 5 Houston (12–5) · 6 Buffalo (12–5) · 7 LA Chargers (11–6)
- **NFC:** 1 Seattle (14–3, West) · 2 Chicago (11–6, North) · 3 Philadelphia (11–6, East) · 4 Carolina (8–9, South) · 5 LA Rams (12–5) · 6 San Francisco (12–5) · 7 Green Bay (9–7–1)

**Playoff results** (LIKELY, from Wikipedia. Spot-check on PFR before printing scores.)
- Wild Card: Rams 34–31 Panthers · Bears 31–27 Packers · Bills 27–24 Jaguars · 49ers 23–19 Eagles · Patriots 16–3 Chargers · Texans 30–6 Steelers
- Divisional: Broncos 33–30 Bills (OT) · Seahawks 41–6 49ers · Patriots 28–16 Texans · Rams 20–17 Bears (OT)
- Conference: **Patriots 10–7 Broncos** (AFC) · **Seahawks 31–27 Rams** (NFC)

Source: https://en.wikipedia.org/wiki/2025%E2%80%9326_NFL_playoffs

**AP awards (NFL Honors, Feb 5, 2026)** (VERIFIED)
| Award | Winner |
|---|---|
| MVP | **Matthew Stafford**, Rams. He led the NFL with 46 TD passes and edged Drake Maye by one first-place vote, the closest MVP race in 23 years. |
| OPOY | **Jaxon Smith-Njigba**, Seahawks WR |
| DPOY | **Myles Garrett**, Browns DE (unanimous) |
| OROY / DROY | Tetairoa McMillan (CAR WR) / Carson Schwesinger (CLE LB) |
| Comeback | Christian McCaffrey (SF) |
| Coach of the Year | **Mike Vrabel**, Patriots, who went 14–3 in his first year |
| Assistant COY | Josh McDaniels (NE OC) |
| Walter Payton MOY | Bobby Wagner |

Sources: https://amp.nfl.com/news/list-of-nfl-honors-award-winners-from-2025-nfl-season · https://www.cbssports.com/nfl/news/nfl-honors-2026-winners-live-updates/live/

**Records** (curriculum §9 item 8)
- **Myles Garrett set the single-season sack record with 23.0** in Week 18 against CIN. That broke the 22.5 shared by Strahan (2001) and T.J. Watt (2021). VERIFIED. Source: https://www.nfl.com/news/browns-de-myles-garrett-reaches-23-sacks-sets-new-nfl-single-season-record
- Cam Little kicked a 67-yard FG, the longest in an outdoor stadium. Josh Allen reached 76 career QB rushing TDs, a record. The Jets had 4 takeaways, the fewest ever in a season. All three are LIKELY, from https://en.wikipedia.org/wiki/2025_NFL_season. Verify on PFR before citing.

---

## 3. Kickoff rules ("dynamic kickoff")

**2024 (one-year trial)** (VERIFIED)
- The kicker kicks from the kicking team's own 35. The other 10 kicking-team players line up on the **receiving team's 40**.
- The receiving team puts at least 7 players in the **setup zone**, between its 30 and 35, with most of them on the 35 restraining line. **Up to 2 returners** may line up in the landing zone.
- Nobody except the kicker and returners may move until the ball hits the ground or a player in the landing zone or end zone.
- The **landing zone** runs from the receiving team's goal line to its 20. A ball that lands there must be returned.
- Touchback (ball lands in the end zone, or goes out of the back) puts the ball at the **30**.
- A ball that lands in the landing zone and rolls into the end zone can be returned or downed. If downed, it is a touchback at the **20**.
- A kick short of the landing zone, or out of bounds, puts the ball at the receiving team's **40**.
- Onside kicks had to be declared and were allowed only when trailing in the 4th quarter.

Source: https://www.nfl.com/news/2024-nfl-season-explaining-rules-for-new-dynamic-kickoff

**2025 (made permanent and modified)** (VERIFIED)
- Touchback for a ball that **lands in the end zone moved from the 30 to the 35**. Landing zone then end zone, downed, is still the 20.
- The receiving team's setup-zone alignment was loosened: up to 3 players may be off the restraining line, no more than one in each of three areas.
- Onside kicks were adopted on May 21, 2025. They may be **declared any time the team is trailing**, no longer only in the 4th quarter. They still have to be declared, so surprise onside kicks remain illegal.
- Return rate: about 21.8% in 2023, 32.8% in 2024, and about 75–76% in 2025. The nflverse pbp calculation gives 25.2%, 32.9%, and 74.6% for regular-season kickoffs with a returner, and a 2025 touchback rate of 20.7%.

Sources: https://www.nfl.com/news/nfl-owners-vote-to-make-dynamic-kickoff-permanent-adjust-ball-spot-on-touchbacks-to-35-yard-line · https://operations.nfl.com/rules-officiating/featured-rules · https://www.nbcsports.com/nfl/profootballtalk/rumor-mill/news/owners-pass-rule-change-allowing-onside-kicks-at-any-point-when-trailing · https://www.pff.com/news/nfl-kickoffs-are-evolving-as-returns-surged-in-2025

**2026 (approved Mar 31, 2026)** (VERIFIED)
- **An onside kick may be declared at any time, even when not trailing.**
- Kickoffs from the 50 happen after a penalty. Kicking from there, teams had an incentive to kick out of bounds on purpose. That is removed: the result is now a **touchback at the 20**, previously the 25.
- The receiving team's setup zone may have a **4th "floater"**. That means only **5 players are required on the restraining line**, with an anti-overload restriction.

Sources: https://www.seahawks.com/news/nfl-announces-approved-rule-changes-for-2026-season · https://www.footballzebras.com/2026/04/nfl-owners-approve-rule-changes-for-the-2026-season/

---

## 4. Overtime (VERIFIED)
- **Playoffs (since 2022):** both teams get a possession, even if the first team scores a TD. The game is sudden death after that. Periods are 15 minutes. This rule came out of the Jan 2022 Bills–Chiefs "13 seconds" game.
- **Regular season (since 2025):** both teams get a possession, the same as the playoffs. The period stays at **10 minutes**, a length set in 2017, and **ties are still possible**. A safety by the defense on the opening possession ends the game.
- **2026:** no OT change found.

Sources: https://operations.nfl.com/rules-officiating/featured-rules · https://www.espn.com/nfl/story/_/id/46088927/nfl-rules-changes-tush-push-chain-gang-kickoffs-celebrations

---

## 5. Tush push
- **2024:** no ban was proposed. LIKELY. Source: https://www.cbssports.com/nfl/news/tush-push-rule-change-nfl-will-not-propose-banning-controversial-play-for-2024-season
- **2025:** Green Bay proposed banning pushing, pulling, lifting, or grasping a runner. The proposal was **tabled at the March/April annual meeting**. A revised version **failed 22–10 on May 21, 2025** in Eagan, MN, two short of the required 24. The league then **tightened officiating guidance** on false starts and alignment for the play. VERIFIED. Sources: https://www.si.com/nfl/packers/packers-proposal-to-ban-eagles-tush-push-fails-again · https://www.inquirer.com/eagles/eagles-tush-push-packers-ban-vote-20250519.html
- **2026:** **no team submitted a ban proposal.** Rich McKay said in February 2026 that he did not expect one. Troy Vincent said the league would "lightly" revisit how the play is officiated. **The play is legal for the 2026 season.** VERIFIED. Sources: https://www.nfl.com/news/competition-committee-co-chairman-rich-mckay-doesn-t-expect-tush-push-ban-proposal-in-2026 · https://www.washingtontimes.com/news/2026/feb/24/nfl-receives-no-tush-push-ban-proposal-year-effort-last-year-ban/
- History: the rule against pushing or pulling the runner was **removed in 2005**. That change is what made the modern tush push legal. LIKELY, from memory and consistent with the coverage above.

---

## 6. Other strategy-relevant rules, 2023–2026

| Rule | Status | Confidence / source |
|---|---|---|
| **Hip-drop tackle ban** | Adopted March 2024. Penalty is 15 yards plus an automatic first down. | VERIFIED. https://www.nfl.com/news/nfl-owners-vote-to-ban-hip-drop-tackle-at-annual-league-meeting |
| **Three-strike suspension policy (2026)** | NFL/NFLPA agreement, Aug 2026. Covers 5 fouls: hip-drop, horse-collar, launching, hits on a defenseless player, and blindside blocks. **Any 3 in a season means a one-game suspension.** Some carryover into the next season. Starts with the 2026 regular season. | LIKELY. https://www.nbcsports.com/nfl/profootballtalk/rumor-mill/news/nfls-new-three-strike-system-doesnt-apply-until-the-2026-regular-season |
| **Challenges** | Two challenges. Since 2024, a **third is granted if either of the first two succeeds**; before that, both had to succeed. This came from a Detroit proposal. | VERIFIED. https://operations.nfl.com/updates/the-rules/approved-2024-playing-rules/ |
| **Replay assist ("sky judge-lite")** | 2025: replay can advise on objective facts. It may **overturn** flags for hits on a defenseless player, face mask, horse-collar, tripping, and roughing or running into the kicker. It **cannot add** uncalled fouls. 2026: league personnel may consult on ejections for flagrant and non-football acts. Reports say replay can drop flags and eject on flagrant acts even without a flag, but the official wording is only "consult." There is no full sky judge. | VERIFIED (2025, 2026 official wording). https://www.cbssports.com/nfl/news/five-new-nfl-rules-to-know-heading-into-week-1-of-preseason-here-are-the-biggest-changes-for-2025 · https://www.seahawks.com/news/nfl-announces-approved-rule-changes-for-2026-season |
| **Virtual first-down measurement** | 2025: Sony Hawk-Eye (6 cameras, 8K) replaces chain measurements. Chains remain as a backup. | VERIFIED. ESPN link in §4 |
| **Two-point conversion** | Unchanged: snapped from the 2. | LIKELY. No proposal found |
| **Onside-kick alternative (4th-and-20)** | Rejected or stalled repeatedly: 2019, Eagles proposals in 2020, 2021, 2023, and 2024. Nothing adopted. The 2026 "onside any time" rule is the only change. | VERIFIED. https://www.cbssports.com/nfl/news/eagles-onside-kick-alternative-among-several-rule-change-proposals-submitted-by-nfl-teams |
| **Fair catch / kickoff touchback-25** | The 2023 fair-catch-inside-the-25 rule was superseded by the dynamic kickoff in 2024. | LIKELY |
| **Playoff seeding** | Lions 2025 proposal: wild cards with better records could outrank division winners, later changed to reseeding after the wild-card round. **Withdrawn before a vote** in May 2025. No change; division winners still get the top 4 seeds. | VERIFIED. https://www.acmepackingcompany.com/2025/5/21/24434469/nfl-news-playoff-seeding-change-detroit-lions-proposal-update-2025 |
| **Emergency 3rd QB** | Since 2023, a 3rd QB on the 53-man roster can be designated without counting against the game-day actives (47/48). Conditions: the team has 2 QBs active, and the 3rd QB is not an elevated practice-squad player. | VERIFIED. https://www.cbssports.com/nfl/news/emergency-third-quarterback-rule-explained-things-to-know-about-nfls-new-bylaw-for-roster-management-in-2023 |
| **Game-day actives** | 48 (eighth OL rule). Practice-squad elevations are allowed. | LIKELY |
| **Guardian Cap** | Allowed in games since 2024 and optional. Mandatory in contact practices for most positions; WR and DB were added in 2024. "Guardian Cap 2.0" was approved for 2026. | LIKELY. https://guardiansports.com/2026/04/08/nfl-allows-guardian-cap-2-0-for-2026-season/ |
| **18-game season** | **Not adopted.** No formal CBA talks as of mid-2026. The CBA runs through the 2030 season. The model being floated is 18 regular-season games plus 2 preseason games. The 2026 schedule is 17 games over 18 weeks, Sept 9, 2026 to Jan 10, 2027, with a record 9 international games. | VERIFIED (not adopted). https://www.profootballrumors.com/2026/06/formal-negotiations-on-18-game-season-yet-to-begin |
| "Sideline assistant may throw challenge flag" (2026) | Appears in one Wikipedia summary. **Not in the official approved list.** | UNVERIFIED. Do not cite |

---

## 7. Data: nflreadpy and what is in it

**Package status** (VERIFIED)
- **`nflreadpy` is the nflverse Python package.** The `nfl_data_py` repo is **archived**. Its README says it is "deprecated in favour of nflreadpy… No further maintenance." Sources: https://github.com/nflverse/nfl_data_py · https://github.com/nflverse/nflreadpy
- **Version:** the latest on PyPI is **0.1.5** (released Nov 19, 2025). The repo was still being committed to in Sep 2026. The package uses **Polars**, so call `.to_pandas()` when you need pandas.
- **Loaders** (from the source tree): `load_pbp` (1999+), `load_participation` (2016+), `load_ftn_charting` (2022+), `load_nextgen_stats` (2016+), `load_snap_counts` (2012+, PFR), `load_player_stats`/`load_team_stats`, `load_schedules`, `load_rosters`, `load_rosters_weekly`, `load_depth_charts`, `load_injuries`, `load_pfr_advstats`, `load_officials`, `load_draft_picks`, `load_combine`, `load_contracts`, `load_trades`, `load_players`, `load_teams`, `load_ff*`.

**Participation (`load_participation`)** (VERIFIED from the release files)
- Columns: `nflverse_game_id, old_game_id, play_id, possession_team, offense_formation, offense_personnel, defenders_in_box, defense_personnel, number_of_pass_rushers, players_on_play, offense_players, defense_players, n_offense, n_defense, ngs_air_yards, time_to_throw, was_pressure, route, defense_man_zone_type, defense_coverage_type`. From 2023 on it adds `offense_names, defense_names, offense_positions, defense_positions, offense_numbers, defense_numbers`.
- **2016–2022 come from NGS. 2023–2025 come from FTN.** FTN supplies participation **after the season ends**, under a CC-BY-SA 4.0 licence, so the **current season (2026) is not available** until about February 2027. 2023 and 2024 were re-released in Sep 2025, 2025 in Feb 2026, and an old NGS-based 2023 file is kept as `pbp_participation_old_2023`.
- **Field coverage by season**, measured as the share of rows filled:

| Field | 2016–17 | 2018–22 | 2023–25 |
|---|---|---|---|
| offense/defense_personnel, defenders_in_box | ~82% | ~83% | ~100% |
| offense_formation | ~80% | ~80% | ~80% |
| was_pressure, time_to_throw, route | ~42–46% (dropbacks) | ~41–43% | was_pressure ~100% (FALSE filled); route and time_to_throw ~42% |
| **defense_coverage_type / defense_man_zone_type** | **0%** | **~41–43%** | **~49–50%** |

- **Source-break traps for writers and chart code:**
  - `offense_formation` values: through 2022 they are SHOTGUN, SINGLEBACK, I_FORM, EMPTY, PISTOL, JUMBO, WILDCAT. From 2023 they are **only SHOTGUN, UNDER CENTER, PISTOL**.
  - Coverage labels: through 2022 they are COVER_0/1/2/3/4/6, 2_MAN, PREVENT. From 2023 they **add COVER_9, COMBO, and BLOWN**, and PREVENT is dropped.
  - The **man/zone split jumps between seasons**: man share of labelled dropbacks is 28.8% (2022), 41.2% (2023), 48.3% (2024), and 30.8% (2025). That looks like a coding artefact. **Do not chart a man-coverage trend across 2022→2025 without a caveat.**
  - Personnel strings change format. Through 2022 they look like "1 RB, 1 TE, 3 WR". From 2023 they list every position, for example "1 C, 2 G, 1 QB, 1 RB, 2 T, 1 TE, 3 WR".
  - `ngs_air_yards` is NA from 2024 on. Use pbp `air_yards` instead.

**FTN charting (`load_ftn_charting`)** (VERIFIED)
- Available from **2022** and **updated weekly during the season**; the 2026 file was updated Oct 5, 2026.
- Columns: `ftn_game_id, nflverse_game_id, season, week, ftn_play_id, nflverse_play_id, starting_hash, qb_location (U/S/P), n_offense_backfield, n_defense_box, is_no_huddle, is_motion, is_play_action, is_screen_pass, is_rpo, is_trick_play, is_qb_out_of_pocket, is_interception_worthy, is_throw_away, read_thrown, is_catchable_ball, is_contested_ball, is_created_reception, is_drop, is_qb_sneak, n_blitzers, n_pass_rushers, is_qb_fault_sack, date_pulled`.
- `is_motion` = "motion occurred on the play before or at the time of the snap". There is no separate motion-at-snap flag.
- **There is no tush-push flag.** Use `is_qb_sneak`, which covers both sneaks and pushes.
- Coverage type is **not** in FTN charting. It is only in participation.

Sources: https://nflreadr.nflverse.com/articles/dictionary_participation.html · https://nflreadr.nflverse.com/articles/dictionary_ftn_charting.html · https://cran.csail.mit.edu/web/packages/nflreadr/news/news.html · release assets at https://github.com/nflverse/nflverse-data/releases

---

## 8. Big Data Bowl

| Edition | Theme | Data | Confidence |
|---|---|---|---|
| **2025** (7th) | **Pre-snap behaviour**: use pre-snap tracking to predict or understand post-snap outcomes and tendencies. It was the first edition with full-play tracking including pre-snap frames. | 2022 season, Weeks 1–9 | VERIFIED theme; LIKELY weeks |
| **2026** (8th) | **Player movement while the ball is in the air.** It ran two competitions. **Prediction** (`nfl-big-data-bowl-2026-prediction`) was a live Kaggle leaderboard predicting player x,y after the throw from pre-throw data, scored against 2025 games in Weeks 14–18. **Analytics** (`nfl-big-data-bowl-2026-analytics`) had University and Broadcast Visualization tracks. Winner: **Lucca Ferraz** (Rice), "Ghostbusters: Back off man, I'm a Data Scientist!", which modelled ghost defenders. Sign-up opened Sept 25, 2025. Prize $100k. Finalists presented at the 2026 Combine. | Released training files are **2023 season Weeks 1–18** (`input_2023_w01..w18.csv`, `output_2023_w01..w18.csv`, `supplementary_data.csv`). The NFL press text mentions "2023 and 2024 seasons", which conflicts with the files. | VERIFIED theme and winner; VERIFIED file names |
| **2027** (9th) | **Not announced as of 2026-10-06.** No NFL release was found, and `kaggle.com/competitions/nfl-big-data-bowl-2027` returns 404. In past years the launch came in late September or October, so check again before 13-05 goes to print. | — | LIKELY (absence) |

**Exact tracking column names**
- **BDB 2025** uses camelCase. VERIFIED via several public solution repos.
  - `tracking_week_N.csv`: `gameId, playId, nflId, displayName, frameId, frameType (BEFORE_SNAP/SNAP/AFTER_SNAP), time, jerseyNumber, club, playDirection, x, y, s, a, dis, o, dir, event`
  - `plays.csv`: includes `offenseFormation, receiverAlignment, pff_passCoverage, pff_manZone, pff_runPassOption, playAction, dropbackType, ...`
  - `player_play.csv`: includes `inMotionAtBallSnap, shiftSinceLineset, motionSinceLineset, wasRunningRoute, routeRan, pff_defensiveCoverageAssignment, pff_primaryDefensiveCoverageMatchupNflId, ...`
- **BDB 2026** uses **snake_case**. VERIFIED via public solution code.
  - `input_*.csv`: `game_id, play_id, player_to_predict, nfl_id, frame_id, play_direction, absolute_yardline_number, player_name, player_height, player_weight, player_birth_date, player_position, player_side, player_role, x, y, s, a, dir, o, num_frames_output, ball_land_x, ball_land_y`
  - `output_*.csv`: `game_id, play_id, nfl_id, frame_id, x, y`
  - `supplementary_data.csv`: includes `season, week, play_description, quarter, game_clock, down, yards_to_go, possession_team, defensive_team, pass_result, pass_length, offense_formation, receiver_alignment, route_of_targeted_receiver, play_action, dropback_type, dropback_distance, pass_location_type, defenders_in_the_box, team_coverage_man_zone, team_coverage_type, expected_points_added, ...`
- The field is in yards, x 0–120 (including end zones) and y 0–53.3, in both editions.

Sources: https://operations.nfl.com/gameday/analytics/big-data-bowl · https://github.com/lneuendorf/nlf-big-data-bowl-2026 (column usage) · https://github.com/ZekeWeng/BigDataBowl2025 · https://github.com/chasko-labs/nfl-big-data-bowl-2027 ("2027: not announced")

---

## 9. Coaching landscape for the 2026 season

Head coaches are VERIFIED. Coordinators are VERIFIED where a hiring report was found; the rest are LIKELY.

| Team | HC | OC (play-caller note) | DC | 2026 change? |
|---|---|---|---|---|
| 49ers | Kyle Shanahan | Klay Kubiak (Shanahan calls plays) | **Raheem Morris** (new) | Saleh left to become **Titans HC**. Brian Fleury left to become Seattle OC. |
| Rams | Sean McVay | **Nathan Scheelhaase** (promoted) | Chris Shula | Mike LaFleur left to become **Cardinals HC**. Kliff Kingsbury added as assistant HC. |
| Chiefs | Andy Reid | **Eric Bieniemy** (returned) | Steve Spagnuolo | Matt Nagy left to become Giants OC. |
| Ravens | **Jesse Minter** (new) | **Declan Doyle** (from CHI) | **Anthony Weaver** | **Harbaugh was fired Jan 6, 2026, and became Giants HC.** Monken became Browns HC. |
| Eagles | Nick Sirianni | **Sean Mannion** (new, from GB) | **Vic Fangio (still)** | Patullo out. OL coach Stoutland departed after 14 seasons. |
| Lions | Dan Campbell | **Drew Petzing** (new) | Kelvin Sheppard | Morton fired; Campbell called plays for the second half of 2025. |
| Seahawks | Mike Macdonald | **Brian Fleury** (new, from SF) | Aden Durde | Kubiak became **Raiders HC**. |
| Bills | **Joe Brady** (promoted) | **Pete Carmichael Jr.** | **Jim Leonhard** | McDermott fired Jan 19, 2026. Babich went to GB. |
| Patriots | Mike Vrabel | Josh McDaniels | **Zak Kuhr** (named full-time Feb 2026) | Terrell Williams, the DC on paper in 2025, missed the season for cancer treatment and is now assistant HC. |
| Bears | Ben Johnson (yr 2) | **Press Taylor** (promoted) | Dennis Allen | Doyle left for BAL. Johnson calls plays. |
| Dolphins | **Jeff Hafley** (new) | Bobby Slowik | Sean Duggan | **McDaniel fired Jan 8, 2026, and is now Chargers OC.** |
| Packers | Matt LaFleur | Adam Stenavich (LaFleur calls plays) | **Jonathan Gannon** (new) | Hafley became MIA HC. |
| Texans | DeMeco Ryans | Nick Caley | Matt Burke | No coordinator change found. |
| Vikings | Kevin O'Connell | Wes Phillips (KOC calls plays) | **Brian Flores (still)** | GM Adofo-Mensah fired; Nolan Teasley hired. |
| Jets | Aaron Glenn (yr 2) | Frank Reich | Brian Duker (Glenn calls the defense) | — |
| Raiders | **Klint Kubiak** | Andrew Janocko | Rob Leonard | Pete Carroll fired after one season (3–14). |

Other 2026 HC changes:
- ARI: Mike LaFleur
- ATL: Kevin Stefanski
- CLE: Todd Monken
- NYG: John Harbaugh
- PIT: **Mike McCarthy** (Tomlin resigned)
- TEN: Robert Saleh

Sources: https://en.wikipedia.org/wiki/2026_NFL_season (HC table) · https://www.profootballrumors.com/2026/02/2026-nfl-offensive-defensive-coordinator-search-tracker · https://www.espn.com/nfl/story/_/id/47662766/sources-lions-finalizing-deal-hire-drew-petzing-new-oc · https://www.nbcsports.com/nfl/profootballtalk/rumor-mill/news/chiefs-finalize-deal-with-eric-bieniemy-to-return-as-their-oc · https://www.bostonglobe.com/2026/02/17/sports/patriots-zak-kuhr-defensive-coordinator · https://www.ksat.com/sports/2026/02/16/seahawks-expected-to-hire-49ers-tight-end-coach-fleury-as-offensive-coordinator-ap-source-says/ · https://kogo.iheart.com/content/2026-01-20-mike-mcdaniel-lands-nfl-coaching-gig-report · https://www.newyorkjets.com/news/aaron-glenn-talks-self-reflection-jets-second-season-03-31-2026

---

## 10. Scheme trend numbers you can cite

**Split-safety (two-high) coverage rate. Source: NFL Next Gen Stats.** VERIFIED
- 2018 32.9% → 2021 37.8% → 2024 40.4% → **2025 42.0%**, the highest since tracking began in 2018.
- In 2025 every defense was above 30%.
- 2025 by coverage: Cover 4 17.2%, Cover 2 13.9%, Cover 6 9.2%. The 2018–24 Cover 4 average was 13.9%.
- Source: https://www.nfl.com/news/the-coverage-that-turned-the-seahawks-into-super-bowl-winners-and-is-taking-the-nfl-by-storm
- A different series circulates from TruMedia/538: 26.8% (2019) to 34.6% (2024), measured on early downs. **Don't mix the two series.**

**nflverse cross-check.** This is my own calculation: post-snap two-high (COVER_2/2_MAN/COVER_4/COVER_6) as a share of labelled regular-season dropbacks, excluding BLOWN/COMBO/PREVENT.

| | 2018 | 2019 | 2020 | 2021 | 2022 | 2023* | 2024* | 2025* |
|---|---|---|---|---|---|---|---|---|
| Two-high | 33.1% | 34.8% | 35.7% | 38.4% | 40.6% | 41.2% | 38.6% | 43.3% |
| Single-high (C1+C3) | 63.1% | 60.7% | 59.3% | 56.9% | 55.2% | 53.4% | 55.4% | 50.4% |

\* FTN source. The trend agrees with NGS, which makes it a usable [C] chart if the source break is marked.

**Pre-snap shift/motion rate. Source: PFF.** VERIFIED
- 2014 37.6% · 2016 38.4% · 2018 43.0% · 2019 46.8% · 2020 50.0% · 2021 51.8% · 2022 55.4% · 2023 56.4% · 2024 61.5% · **2025 63.9%**
- Every team except the Giants used motion on at least half of plays in 2025.
- Source: https://www.pff.com/news/nfl-pre-snap-motion-usage-reaches-new-highs-across-the-nfl (Daire Carragher, Feb 23, 2026)

**Motion at the snap. Source: ESPN Analytics.** LIKELY
- About 4% of plays in 2017 → about 20% in 2023 → about 25% in 2024.
- The 2023 Dolphins were at about 60%, the highest since ESPN began tracking in 2017.
- Exact league figures are second-hand, so re-check the ESPN piece before quoting.

**FTN `is_motion` rate** (my calculation; regular-season pass and run plays)
- 2022 37.6% · 2023 45.2% · 2024 49.3% · 2025 55.1%
- This series is lower than PFF's because the two sources define motion differently.

**Personnel and heavy sets. Source: NGS (James Reber).** VERIFIED
- In 2025, offenses used fewer than three WRs on **41.7%** of plays. That is the first season at or above 38% since NGS began in 2016.
- The rate rose from 38.8% in Weeks 1–9 to 44.5% from Week 10 on.
- Defenses played base on 29.7% in 2025, against a low of 20.5% in 2023.
- Source: https://www.nfl.com/news/nfl-trend-watch-heavy-personnel-could-shape-super-bowl-lx-showdown-between-patriots-and-seahawks

**nflverse personnel share** (my calculation, regular-season pass and run plays)

| | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|---|---|---|---|---|
| 11 | 60.7 | 59.6 | 64.6 | 60.3 | 59.4 | 60.5 | 62.8 | 64.2 | 62.7 | **58.8** |
| 12 | 18.8 | 20.6 | 17.8 | 20.9 | 20.1 | 21.6 | 20.1 | 20.4 | 23.5 | **24.4** |
| 13 | 3.1 | 4.2 | 3.5 | 3.0 | 3.6 | 3.6 | 4.1 | 3.4 | 3.7 | **5.1** |
| 21 | 7.9 | 8.4 | 8.0 | 7.9 | 8.3 | 7.3 | 8.2 | 7.4 | 6.3 | 7.0 |
| Shotgun (pbp) | 64.2 | 59.3 | 63.9 | 64.7 | 66.1 | 66.2 | 67.9 | 72.2 | 70.6 | 66.2 |

- In 2025, 11 personnel fell to its lowest share of the decade, 12 personnel reached a decade high, and shotgun use fell back.
- FTN under-center share (`qb_location == 'U'`) was 31.6% (2022), 27.3% (2023), 28.8% (2024), and **33.6% (2025)**. That supports the curriculum's "under-center comeback" framing.

Method for all my calculations: nflverse pbp, participation, and FTN release files downloaded 2026-10-06. Plays are regular season with `play_type` in pass or run and down not missing. Personnel is RB+FB count followed by TE count. Reproduce the numbers in 13-01 code rather than hard-coding them.
