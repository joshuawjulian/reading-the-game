# Fact-check: 13-04 Tendencies: PROE, Personnel, Motion, and Coverage from Charting Data

Checked 2026-10-08 against FACTS-current.md, nflverse data (every data claim recomputed in the `rtg` container by running the chapter's own cells plus extra checks), the nflfastR / fastrmodels / nflverse-pbp / nflverse-ftn source on GitHub, and web sources.
All 6 `<!-- VERIFY -->` comments are resolved and removed. The chapter builds (`build_pdfs.py 13-04-tendencies-proe-and-charting --html`: OK, 38 pages), and all hidden assert cells still pass.

| Claim | Verdict | Source | Change |
|---|---|---|---|
| Rams 59% / Jets 61% dropbacks, all snaps 2025; Jets trailed on ~3 snaps in 4 | VERIFIED | Own calc (asserted in chapter) | None |
| Stafford 2025 MVP, NFL-leading 46 TD passes; NFL Honors Feb 5, 2026 | VERIFIED | FACTS §1; nfl.com Honors list | None |
| Jets lowest PROE 2025 (−12.2); Rams second (+5.9) behind Arizona (+8.0) | VERIFIED | Own calc | None |
| Raw pass rate vs average WP correlation −0.45 (takeaway hard-codes it) | VERIFIED | Own calc: −0.454 | None |
| Neutral definition: "This course uses the same definition in every chapter" (WP 20–80%) | CORRECTED | 13-01 and 13-02 use WP 10–90% (13-02 line 101; 13-01 lines 651, 1163); 08-02, 08-03, 10-01 use 20–80% | Text now says it uses the play-calling chapters' definition (10-01, 08-02, 08-03); garbage-time sentence says 13-01/13-02 keep 10–90%; glossary entry notes the looser band |
| Filter keeps 43% of 2025 snaps (56% all downs); rank correlations ≥ 0.9 (score-within-7: 0.92; 10–90: 0.96) | VERIFIED | Own calc | None |
| nflverse xpass exists from 2006 | VERIFIED (+ reason added) | nflfastR `add_xpass()` docs: NA before 2006 "since that was before NFL started marking scrambles" | Reason added to text; fn `nflfastr-xpass` |
| xpass is an XGBoost model, by Ben Baldwin, added 2020 | VERIFIED | `R/helper_add_xpass.R` header (Author: Ben Baldwin); fastrmodels `data.R` ("A raw vector representation of a XGBoost model"), DESCRIPTION imports xgboost; nflfastR NEWS 3.1.1 (release 2020-10-22) "Added ... our experimental expected pass model, `add_xpass()`" | Text: "that Ben Baldwin added ... in 2020"; footnote now cites all three |
| xpass feature list (and what nflverse's model "sees") | CORRECTED (made specific) | `prepare_xpass_data()`: down, ydstogo, yardline_100, qtr, wp, vegas_wp, era2–4, score_differential, home, half_seconds_remaining, both timeouts, outdoors/retractable/dome | "Why it exists" box now says nflverse's adds the betting line (via Vegas WP), timeouts, home and roof type; "weather" in our list changed to "the stadium" (nflverse's has roof type, not wind/temp) |
| `pass_oe` = per-snap value ×100 | VERIFIED | `add_xpass()`: `pass_oe = 100 * (pass - xpass)` | None |
| Own model log loss 0.562 / AUC 0.769 vs nflverse 0.536 / 0.786; team PROE correlation 0.98 | VERIFIED | Own calc (chapter tables) | None |
| xpass ≈ 0.79 down 17 with 5:00 left | VERIFIED | Own calc | None |
| PROE on neutral early downs is the convention "used here and by most public analysts" | SOFTENED | nflfastR beginner's guide uses WP 20–80, downs 1–2, but also qtr ≤ 2; other analysts use 5–95 or 20–80 bands | "with small variations in the cut-offs, by most public analysts" |
| Rams vs Ravens "the two ends of the 2025 table among playoff-calibre offenses" | CORRECTED | Ravens 8–9, not an AFC seed (FACTS §1); BAL PROE −11.2, second-lowest | "two teams near opposite ends ...: the Rams, second from the top, and the Ravens, second from the bottom" |
| Rams passed over expected in nearly every situation; Ravens ran under in nearly every one, most in short yardage and red zone | VERIFIED | Own calc: LA negative only on 3rd & 4+; BAL −28.8 (2nd & 1–6), −26.4 (3rd & 1–3), −18.8 (red zone), +0.6 on 3rd & 4+ | None |
| Season PROE rests on 400–500 neutral snaps; "third-and-1 to 3 might hold thirty, SE ~9 points" | CORRECTED (minor) | Own calc: mean 442 neutral early-down snaps; 3rd & 1–3 n = 38 (BAL), 46 (LA), SE 6.4–7.1; per-snap SD 48 | "holds forty or so, ... about seven points" |
| PROE–EPA correlation 0.31 (2016–25); 0.05 in 2024, 0.27 in 2025; range 0.05–0.51 | VERIFIED | Own calc | None |
| Some of the best 2025 offenses sit left of zero | VERIFIED | Own calc: GB (top neutral EPA) −5.7, BUF −2.2, DAL −1.3 | None |
| 2022–24 Bengals top-3 PROE every season | VERIFIED | Own calc (asserted) | None |
| 2024 Eagles PROE −8.2 (2nd-lowest), after +4.9 / +4.4; 4th in neutral EPA; 2025 −0.3 | VERIFIED | Own calc | None |
| Eagles' 13-point PROE swing came "with the same head coach and quarterback, because the roster changed" | CORRECTED (incomplete) | Kellen Moore replaced Brian Johnson as OC/play-caller for 2024 (Inquirer, Feb 5 2024); Patullo OC 2025 (FACTS C10) | Text now names Moore as the second cause, notes Patullo in 2025, and says PROE answers "personnel and play-caller"; fn `eagles` extended |
| Barkley 2,005 rushing yards; SB LIX Feb 9 2025, PHI 40–22 KC | VERIFIED | PFR; FACTS §1; multiple reports (9th 2,000-yard rusher) | None |
| PROE after 4 games predicts rest of season at 0.42; EPA 0.26 at 4, 0.33 at 8 | VERIFIED | Own calc | None |
| Season-to-season PROE r = 0.44 same HC (220), 0.16 new HC (68) | VERIFIED | Own calc | None |
| Petzing's Arizona: among most run-leaning 2023 (29th) to most pass-leaning 2025 (1st), same play-caller | VERIFIED | Own calc; 08-03 (Petzing called ARI offense 2023–25) | None |
| 2026 new OCs: SEA Fleury, DET Petzing, KC Bieniemy, BAL Doyle under Minter, PHI Mannion | VERIFIED | FACTS C1–C3, C10, §8 | None |
| 08-02: alignment alone calls ~2 snaps in 3 | VERIFIED | 08-02 line 1630 | None |
| Dashboard readings: heavy MIA/SF ~2 in 3, BAL/LAC/LA ≥ 1/3; Rams lead under center (72%); Giants lowest motion ~10 pts below next; MIA/SF near 80%; WAS no-huddle 61% | VERIFIED | Own calc (MIA 67.6, SF 63.3, BAL 41.7, LAC 39.3, LA 34.0; NYG 40.4 vs KC 49.8; SF 78.6, MIA 78.3) | None |
| WAS, ATL, CIN, PHI, KC in shotgun/pistol "on three early downs in four or more" | CORRECTED (minor) | Own calc: KC 74.1%, PHI 74.5%, CIN 74.6% | "about three early downs in four or more" |
| NGS: fewer than 3 WRs on 41.7% of 2025 plays | VERIFIED | FACTS §10; nfl.com (Reber) | None |
| FTN is_motion = before or at the snap; 55.1% of 2025 runs and dropbacks; PFF 63.9% in 2025 | VERIFIED | FTN dictionary; own calc; PFF (Carragher, Feb 23 2026) | None |
| ESPN motion-at-the-snap "around a quarter of plays in 2024" | CORRECTED | Could not reach the original ESPN piece; the 2024 figure is only second-hand. Primary-quoted figures: 4% (2017), 22% (2023), Seth Walder via Ben Solak, The Ringer, Jan 25 2024 | Text and fn `motion-series` now give 4% (2017) and 22% (2023) with the Ringer citation |
| In-season pbp "usually within a day of each game" | VERIFIED (tightened) | nflverse-pbp `update_data.yaml` cron: after TNF, Sunday early/late, SNF, MNF windows, plus daily 09:03 UTC, Sep–Feb | Table: "within hours of each game"; fn `ftn-licence` cites the workflow |
| FTN charting arrives "weekly during the season" | CORRECTED | nflverse-ftn `update_ftn.yaml`: pulls every six hours Sep–Feb; participation workflow is manual (after season) | Table: "During the season, as FTN charts each game"; caveat 5 "game by game"; footnote rewritten |
| Participation 2016 on, coverage 2018 on; 2023+ supplied by FTN after the season; CC-BY-SA 4.0 | VERIFIED | FACTS C5, §7; participation dictionary | None |
| 2018–2022 coverage labels "from the NFL's Next Gen Stats" (how produced) | SOFTENED | AWS ML Blog (Feb 10 2023): NGS coverage classifier launched for 2022, uses tracking data, trained on 2018–2020 plays charted manually by football specialists, 88.9% accuracy on 2021; its 8 classes are exactly nflverse's pre-2023 label set. nflverse does not say which seasons are human charts vs model output | Text: "(film charting, and from 2022 a coverage model trained on that charting and fed by tracking data)"; caveat 2 now covers model-inferred labels (~89% in its makers' test); fn `labels` explains and states the uncertainty |
| 2025 league mix: mostly Cover 3, Cover 2, Cover 1, quarters next | VERIFIED | Own calc: C3 27.9, C2 23.1, C1 22.5, C4 10.1 | None |
| Blown/combination tags "about 1 snap in 250" | CORRECTED | Own calc: 0.46% of labelled 2025 dropbacks (1 in 217) | "fewer than 1 snap in 200" (fig-coverage-mix footnote text) |
| Man share 29 → 44 → 49 → 31% (2022–25); C3/C1 swap and swap back; two-high tracks NGS (33.1 vs 32.9; 38.4 vs 37.8; 38.6 vs 40.4; 43.3 vs 42.0) | VERIFIED | Own calc; FACTS §7, §10; nfl.com NGS article | None |
| Formation labels, coverage label set, personnel string and ngs_air_yards changes at the break | VERIFIED | FACTS §7 | None |
| Vikings 2025: fewest man (18%), most two-high (59%), most blitz (51%, avg 29%); on 3rd & 4–8 blitz 39% = league 39%; man 43% of 56 vs league 49% | VERIFIED | Own calc (asserted) | None |
| Flores Vikings DC since 2023, still 2026; vikings.com URL | VERIFIED | vikings.com bio page (joined Feb 6, 2023, Defensive Coordinator); FACTS §8 | Join date added to fn; VERIFY removed |
| 06-06 charted the Vikings' two-high-to-Cover-0 range for 2023–2025 | VERIFIED | 06-06 film room "Vikings 2023–2025" | None |
| Caveat 3: personnel/box "nearly every snap from 2023 but about 80% before; formation about 80% throughout" | CORRECTED | Own calc on participation rows: personnel 76% / box 74% (2016–22), 100% (2023–25); formation 72–73% then 80% | Reworded to "about three in four before"; formation "three in four before 2023, four in five after" |
| Caveat 6: "five to six hundred dropbacks"; third-and-medium cell "sixty or eighty" | CORRECTED | Own calc: mean 617 dropbacks (501–745); MIN 3rd & 4–8 labelled n = 56 | "about six hundred dropbacks"; "perhaps fifty or sixty" |
| Rams card: 13 personnel 34% vs league 6%; pass from 13 47% vs 46%; 11 pass 67% vs 57%; under-center pass 46% vs 34% | VERIFIED | Own calc | None |
| Watch-for-it example "13 personnel under center: expect a pass about 40%, not 30%" | CORRECTED (internal consistency) | Own calc: Rams pass from 13 = league (47 vs 46), so the example contradicted the card | Now "under center: expect a pass about 45% of the time, not the league's 35%" (matches the card) |
| Rams defense: man 26% vs 31%, two-high 49% vs 43%, blitz 25% vs 29% | VERIFIED | Own calc | None |
| Wild card: Rams 34–31 at Panthers; CAR NFC 4 seed (8–9, South champ), Rams 5 (12–5); January 2026 | VERIFIED | PFR box score 202601100car (Jan 10 2026, Bank of America Stadium); MyNorthwest/NBC LA reports (Parkinson 19-yd TD, 0:38 left); FACTS §1 | Fn `wildcard` adds date, venue, PFR link; VERIFY removed |
| McVay was the Rams' 2025 play-caller | VERIFIED | FACTS §8 (LaFleur was OC; McVay calls plays) | None |
| Drill 1: 11 personnel under center = run ~2 in 3 league-wide; Rams 54% of 151; play-action on 79% of Rams' / 84% of league's dropbacks from it | VERIFIED | Own calc | None |
| Drill 3: real first downs in that spot passed 84%; nflverse xpass 0.84; ours 0.67; average WP 11% (below the 20% floor) | VERIFIED | Own calc (510 snaps) | None |
| Baldwin's Open Source Football write-ups of the nflfastR models | VERIFIED | fastrmodels cites opensourcefootball.com/posts/2020-09-28-nflfastr-ep-wp-and-cp-models/ for the xpass model code | URL added to fn `dictionaries` |

## Counts

- VERIFIED: 38 (two of them tightened or extended)
- CORRECTED: 12
- SOFTENED: 2
- REMOVED: 0

## Uncertain / for a human

- ESPN's 2024 motion-at-the-snap figure (~25%) is still only second-hand; the chapter now uses the 2017/2023 figures quoted from Walder in The Ringer. If 02-06 prints the 2024 figure, it should be checked against the ESPN original.
- Which pre-2023 coverage labels in nflverse are human charts and which are NGS model output is undocumented; the chapter now says so.
- Neutral-situation definition still differs between 13-01/13-02 (10–90%) and this chapter (20–80%). The text is now accurate about it; harmonising the course is an editorial decision.
