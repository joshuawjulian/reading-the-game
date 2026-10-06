# Fact-check: 01-01 The Game in Fifteen Minutes

Checked 2026-10-06 against FACTS-current.md, the 2026 NFL rulebook PDF (downloaded from operations.nfl.com and read in full for the provisions cited), nflverse play-by-play (recomputed in the `rtg` container), and web sources.
All 7 `<!-- VERIFY -->` comments are resolved and removed. The chapter builds (`build_pdfs.py 01-01-the-game-in-fifteen-minutes --html`: OK). Each footnote is still referenced exactly once.

| Claim | Verdict | Source | Change |
|---|---|---|---|
| About 11 minutes of live action in a broadcast of about three hours (WSJ, Biderman, Jan 15 2010) | CORRECTED (footnote detail) | Fox Sports repost Jan 18 2010 (four broadcasts, 174-minute broadcast); leanblog Jan 17 2010 links the same WSJ article ID | The footnote said broadcasts were "just over three hours". It now says about three hours (174 min) and 10:43 of action, and adds the Fox Sports repost because the WSJ link is paywalled |
| Field 120 × 53⅓ yd (360 × 160 ft); 6-ft white border; lines every 5 yd; 1-yd ticks at the sidelines and hashes | VERIFIED | 2026 rulebook R1 S1–2 | None |
| Numbers every 10 yd; tops about 14 yd from the sideline | VERIFIED | R1-2-4 Item 1 (bottoms 12 yd in, 2 yd tall) | None |
| "A's 19" / "B's 49" yard-line naming | VERIFIED | R3-11-9 | None |
| Goal line and pylons are in the end zone; breaking the plane; out of bounds when touching a boundary line | VERIFIED | R3-11-3, R11-1/2, R3-20-1 | None |
| Pylons at the four corners of each end zone | VERIFIED | R1-2-3 (goal-line corners plus two on each end line) | None |
| Posts: crossbar 10 ft high, 18 ft 6 in wide, uprights 35 ft above it, in the plane of the end line | VERIFIED | R1-3-1 | None |
| Hashes 70 ft 9 in from each sideline, 18 ft 6 in apart | VERIFIED | R1-2-2, R3-11-7; operations.nfl.com field-markings text | None |
| Before 1933, play started where the ball was downed; teams wasted a down moving to the middle | SOFTENED | Wikipedia "Hash mark (sports)" ("all plays began where the ball was declared dead"); Pigskin Dispatch | Now "generally started where the last one ended" and "often spent a play" running back toward the middle. The out-of-bounds detail is left out |
| 1932 Bears–Spartans playoff: tied for first, blizzard, Chicago Stadium, field 80 yd long and 30 ft narrower | VERIFIED | PFHOF "The First Playoff Game" | None |
| "hockey rink's boards right at the sideline"; officials moved the ball away from the walls after every play near them | CORRECTED / SOFTENED | PFHOF ("sidelines butted up against the stands"); Wikipedia 1932 game (inbounds lines 10 yd in) vs Pigskin Dispatch (brought in 15 yd at the cost of a down) | Now "the stands right up against the sidelines" and a special rule let the ball be moved in from the walls ("accounts differ on the details"). Both versions are in fn `firstplayoff` |
| 1933 hash marks and goal posts on the goal line adopted from the 1932 game | VERIFIED | PFHOF 1933 chronology; PFHOF First Playoff Game | None |
| Hashes at 10 yd (1933), 15 yd (1935), 20 yd (1945), 23 yd 1 ft 9 in (1972) | VERIFIED | PFHOF chronology pages for 1935, 1945 and 1972 (primary); Wikipedia for 1933 = 30 ft | fn `hash72` rewritten with the PFHOF year pages |
| The 1972 hash move was meant to help offenses after scoring fell | VERIFIED | AP Mar 24 1972 "Owners give offense big seven-yard boost" (cited in Wikipedia 1972 NFL season); SI "High on the Hash" Aug 28 1972 | New fn `offense72`. Text reworded to "made to help offenses after a drop in scoring". The "75 fewer TDs in 1971 than 1969" figure appears only in secondary sources and was not added |
| College hashes 60 ft from each sideline (40 ft apart) since 1993; NFL spacing 1945–71; HS 53 ft 4 in | VERIFIED | operations.nfl.com 2026 rulebook page ("60' for college football"); NCAA Rule 1-2 text (BAFRA mirror); Wikipedia citing Milwaukee Journal Mar 26 1993 | fn `collegehash` now leads with the NFL Ops primary source |
| Fig. hash-compare ratios: college wide side two-thirds more room, HS twice | VERIFIED | Arithmetic: 33.3/20 = 1.67; 35.6/17.8 = 2.0 | None |
| Scoring values; try from the 15 (kick) or 2 (run/pass); untimed; defense scores 2 on a try; one-point safety on a try | VERIFIED | R11-1-2, R11-3-1/2 | None |
| XP moved to the 15 in 2015; defensive 2-point return rule from 2015 | VERIFIED | NFL.com May 2015 | None |
| NFL 2-pt conversion in 1994; college 1958; AFL 1960–69 | VERIFIED | PFHOF "2-point conversion turns 30 years old"; Deseret News 1994 | None |
| XP success after 2015 "about 94–96%" | CORRECTED | Own nflverse calc: 93.0% (2020) to 95.9% (2023–25) | Now "about 93–96%" |
| Two-point attempts "about 100–150 a season" | CORRECTED | Own calc: 86–154 a season, 2015–2025 | Now "about 90–150" |
| XP 99.3% in 2014; about 57 two-point attempts a season (2010–14) vs about 133 (2021–25); about 10% of tries | VERIFIED | Own calc (inline code) | None |
| FG kick = LOS + about 18; snap 7–8 yd to the holder | VERIFIED | Field geometry (10-yd end zone + hold) | None |
| "Kicks from under 40 yards almost never miss"; caption "inside 40 close to certain" | CORRECTED | Own calc 2021–25: under 30 = 98.0%, 30–39 = 93.4% | Text and caption now split the two ranges ("almost never" applies to under 30; 30–39 misses about one time in fifteen) |
| 50+ made about 7 in 10 now; under 6 in 10 in 2016 and 2019; 69–70% 2022–25 | VERIFIED | Own calc: 56.7% (2016), 57.9% (2019), 68.7–69.9% (2022–25); 50–59 bucket 70.1% | "risky a decade ago … routine" reworded to the figures |
| Twelve made 60+ yd FGs in 2025 | VERIFIED | Own calc (inline) | None |
| Posts on the goal line 1933–73, back to the end line in 1974, to push teams to play for TDs | VERIFIED | PFHOF 1974 chronology (move, "to add action and tempo"); Nexstar 2025 citing PFHOF (purpose; FG attempts 860+ → 553) | The dead PFHOF blog URL was replaced in fn `goalposts74` |
| Safety: free kick from the 20; fumble out of own end zone; 12 safeties in 2025 (about 1 per 23 games) | VERIFIED | R11-5; own calc (12 in 272 games = 1 per 22.7) | None |
| 2025 possessions: about 10.7 per team per game; about 23 pts per team; red-zone TD 57% / FG 29%; TD share 23% | VERIFIED | Own calc (inline) | None |
| "Fewer than four in ten [possessions] produced points; TD:FG about 3:2" | VERIFIED | Own calc: 23.0% + 16.1% = 39.1%; ratio 1.43 | None |
| "A third end in a punt; a quarter end with a touchdown" | CORRECTED | Own calc: punt 32.9%, TD 23.0% | Now "fewer than a quarter end with a touchdown" |
| About 149 snaps a game, about 121 runs and passes | VERIFIED | Own calc | None |
| Coin toss: visiting captain calls it, within 3 min of kickoff; winner may defer; second-half options | VERIFIED | R4-2-2 | None |
| "Most coaches now defer" | VERIFIED (latest published count is from 2018) | ESPN (Goessling) Nov 5 2015: 7.8% in 2008, 76.4% in 2015; FootballScoop Sept 7 2018: about five in six | New fn `defer` |
| Kickoff from the 35; dynamic kickoff 2024; permanent with a touchback to the 35 in 2025; onside kick declarable at any time in 2026 | VERIFIED | FACTS §3; 2026 rulebook "2026 Rules Changes" (6-1-6) and R6-1-2 | None |
| Four 15-minute quarters; switch ends after Q1/Q3 keeping down, distance and spot; 13-minute halftime | VERIFIED | R4-1, R4-2 | None |
| Two-minute warning definition; origin before the 1970 merger (official time on the field) | VERIFIED | R3-41; Football Zebras (Mark Schultz) Oct 18 2019 | None |
| OT: playoffs both-possess since 2022, regular season since 2025; 10-min regular-season OT, ties possible; 15-min playoff periods; 2 OT timeouts | VERIFIED | FACTS §4; R4-5-1 | None |
| Clock: runs after a tackle in bounds; incompletion stops it until the snap; out of bounds restarts on the ready signal except after the 1st-half 2:00 warning, inside the last 5:00, or after a change of possession; free kick starts the clock on a legal touch in the field of play; fouls "as if the foul had not occurred"; injury timeouts before 2:00 likewise | VERIFIED | R4-3-1/2 | None |
| 10-second runoff exists late in halves | VERIFIED | R4-3-2(g), R4-7 | None |
| NCAA stopped the clock on first downs for decades; dropped it in 2023 except in the last 2 min of each half | VERIFIED | ESPN Apr 21 2023 | Footnote adds that the change is in every division except D-III |
| "In the NFL a first down has never stopped the clock" | SOFTENED | No history source found for "never" | Now "a first down doesn't stop the clock" |
| Timeouts: 3 per half, unused don't carry over, head coach or any player may call; 2-minute stoppage; second "freeze" timeout is ignored and penalized | VERIFIED | R4-5-1 Items 1 and 4 | None |
| Play clock 40 s from the end of the play, 25 s after administrative stoppages; delay of game 5 yd; radio cut-off at 15 s | VERIFIED | R4-6-1/2; 01-04 fact-check | None |
| Seven officials | VERIFIED | R19-1-1 (seven officials) | None |
| BUF–KC Divisional, Jan 23 2022: 29–26 at 1:54, Hill 64-yd TD 33–29, Davis 19-yd TD 36–33 at 0:13, touchback, Hill 19 / TO 0:08, Kelce 25 to BUF 31 / TO 0:03, Butker 49-yd FG, OT Kelce 8-yd TD 42–36 | VERIFIED | nflverse pbp `2021_20_BUF_KC`, every play checked | None |
| Playoff OT changed the next season; regular season in 2025 | VERIFIED | FACTS §4 | None |
| Super Bowl LIX, Feb 9 2025, Caesars Superdome, PHI 40–22; every scoring play, time, distance and try result; DeJean INT at the KC 38; 24–0 at half; KC received the second-half kickoff | VERIFIED | FACTS; nflverse pbp `2024_22_KC_PHI` (every scoring play and both kickoffs checked) | None |
| 4th-and-goal from the 1–2, 2016–25: 593 snaps; TD 55% (236/426); FG 99% (166/167); go rate 57% (2016) → 85% (2025); EP at own 1 ≈ −0.5, own 35 ≈ +1.6 | VERIFIED | Own calc: 593; .554; .994; .57/.85; −0.50 / +1.55 | None |
| Kirwan *Take Your Eye Off the Ball* 2010, 2nd ed. 2015 | VERIFIED | 01-04 fact-check | None |

## Counts
VERIFIED 42 · CORRECTED 6 (WSJ footnote, the 1932 "hockey boards" detail (its ground rule also softened), XP range, 2-pt attempt range, FG under-40 wording, TD-share wording) · SOFTENED 2 (pre-1933 practice, "never stopped the clock") · REMOVED 0. One addition was considered and left out as unverified: the "75 fewer TDs" figure.

## Still uncertain / for a human
- Deferral rate: the newest published league-wide count found is from 2018 (about five in six). nflverse has no coin-toss data, so no 2025 figure exists. "Most coaches now do" is very likely still true, but the dynamic kickoff (2024–) could in principle have changed the calculus.
- The 1932 game's special sideline rule: sources disagree (10-yd inbounds lines vs. 15 yd at the cost of a down). The chapter now says that accounts differ.
- WSJ article: the WSJ URL is paywalled (401) and could not be opened, but the article ID matches a contemporaneous link, and the figures come from the Fox Sports repost.
