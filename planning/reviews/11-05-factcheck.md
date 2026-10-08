# Fact-check log: 11-05 The Modern Era (2017-2025)

Checked 2026-10-08 against FACTS-current.md, web sources, and nflverse play-by-play and schedules (recomputed in the `rtg` container; scripts in `_pdfbuild/1105-fc/`). All nine `<!-- VERIFY -->` comments are resolved and removed. I added three footnotes (`[^reidcollege]`, `[^fourthtools]`, `[^lionsmodels]`). The chapter now has 35 footnotes, and each is referenced exactly once. Build `build_pdfs.py 11-05-the-modern-era --html`: OK (27 pages, up from 26 because of the longer footnotes). I looked at the edited pages 6 and 19 as PNGs, and they are clean.

**Totals:** 58 VERIFIED, 10 CORRECTED, 0 SOFTENED, 0 REMOVED.

**Fact-sheet discrepancy (please fix FACTS-current.md §0 C10):** the sheet says Sean Mannion makes 2026 the Eagles' "fifth straight year with a new OC". That is wrong. Steichen was OC for both 2021 and 2022, so new OCs came in 2023, 2024, 2025 and 2026. That is four straight years. Mannion is Sirianni's fifth OC since 2021 (Eagles.com: "fifth OC in six seasons").

| Claim | Verdict | Source | Change |
|---|---|---|---|
| SB LX Feb 8 2026, SEA 29-13 NE; Walker 27-135 MVP; 6 sacks of Maye; Myers 5 FG; Nwosu pick-six; Kubiak OC, Durde DC | VERIFIED | FACTS §1 | none |
| Seattle 2025: under center 53%, 2nd to Rams 59%; <3 WR 55%; two-high 52%, 3rd | VERIFIED (book calc) | Writer's nflverse/FTN calc; consistent with FACTS §10 league totals | none |
| Rams 224 pts in 2016 (fewest), 478 in 2017 (most) | VERIFIED | nflverse schedules; PFR consistent | none |
| McVay hired Jan 12 2017 at 30, youngest modern HC; Shanahan to SF Feb 2017; ATL 2016 led NFL (540) | VERIFIED | Wikipedia (McVay, Shanahan) | none |
| McVay and K. Shanahan together on Washington staff 2010-2013 | VERIFIED | Wikipedia | none |
| Seattle Cover 3 copied by Carroll assistants in JAX (Bradley) and ATL (Quinn); Falcons reached SB LI | VERIFIED | Common record | none |
| Shotgun 64% in 2016 | VERIFIED | FACTS §10 (64.2) | none |
| Rams 2018: 11 personnel ~93%; Goff under center 60.9% (1st), league 36.1%; play-action ~1/3 of dropbacks, most in NFL | VERIFIED | Book calc; The Ringer (Dec 10 2018) gives the Rams' season PA rate as about 36% | none |
| Rams 2018 13-3, 527 pts; beat KC 54-51 Nov 19 (MNF) | VERIFIED | nflverse schedules | none |
| Dec 9 2018: Bears 15, Rams 6; Goff 4 INT (R. Smith, E. Jackson, K. Fuller, Amukamara) | VERIFIED | nflverse pbp, recomputed (Peters, Robey and J. Johnson's INTs were thrown by Trubisky) | none |
| SB LIII Feb 3 2019, NE 13-3; "eight weeks later" | VERIFIED | nflverse schedules | none |
| **How the Bears and Patriots defended the Rams' play-action** ("defenders sank toward the intermediate middle") | CORRECTED | TheRams.com (Oct 23 2020): Bears' 6-1 front, reused by NE in SB LIII; Ringer (Dec 10 2018): PA on 11 of 48 dropbacks vs ~36% season; Sun-Times: Gurley 11-28; ESPN Graziano (Feb 4 2019): NE six on the line, zone on ~40% after a man-heavy season, Goff pressured on 38% | "What to notice" rewritten: the six-man front killed the zone run, so play-action stopped working and the Rams stopped calling it; NE's zone surprise. `[^bears18]` sources added |
| Mahomes drafted 10th in 2017 (trade up from 27), Texas Tech/Kingsbury; 2018 5,097 yds, 50 TD, MVP; KC 565 pts (most) | VERIFIED | Wikipedia; nflverse schedules | none |
| "Mahomes sat for a season" | CORRECTED | He started the 2017 Week 17 game at Denver | "sat for almost all of his rookie season (he started only the final regular-season game)" |
| Reid HC since 1999, from Holmgren's Packers staffs | VERIFIED | Wikipedia | none |
| **Reid's college borrowing** (RPO, shovel option, jet motion, Air Raid) | VERIFIED, specifics added | Deadspin (Sep 8 2017): Reid quote about going back to Smith's Utah material, and the shovel option; Boston Globe (Volin, Oct 7 2017): "run-pass options, zone reads, and shovel passes to Travis Kelce" | Added a 2017 Alex Smith sentence with Reid's quote and new `[^reidcollege]`. The Chris Ault consulting job (2013) is only mentioned in the footnote: SI framed it as being about defending the pistol, so it is not presented as college borrowing |
| Mahomes's left-handed throw | VERIFIED | Oct 1 2018 at Denver (common record) | none |
| KC 2021 faced two-high 45.9% (3rd), league 38.4% | VERIFIED (book calc) | Matches FACTS §10 league 38.4 | none |
| KC in five of six SBs 2019-2024, won three | VERIFIED | LIV W, LV L, LVII W, LVIII W, LIX L | none |
| SB LIV 3rd-and-15 at KC 35, 7:13 left, trailing 20-10, 44 yds to Hill at SF 21; won 31-20 | VERIFIED | nflverse pbp; Wikipedia | none |
| **Play name "Jet Chip Wasp"** | VERIFIED | Wikipedia "Jet Chip Wasp"; CBS Sports; Reid to Peter King: "We call it 'Wasp'"; King: "2-3 Jet Chip Wasp" | Name variants added to `[^sb54]` |
| Fangio: assistant 30+ years, Bears DC 2015-18, Denver HC 2019 at 60; Eagles DC to the 2024 title | VERIFIED | Wikipedia; FACTS C10 | none |
| Staley to Rams 2020; Rams allowed the fewest points (296); Chargers HC a year later | VERIFIED | nflverse schedules (LA 296, BAL 303) | none |
| Tree: Barry, Desai, Evero, Shula | VERIFIED | PFF tree piece (2021); FACTS §9 | none |
| Light-box YPC and EPA (4.64 / −0.042 vs 4.09 / −0.085); deep-attempt shares | VERIFIED (book calc) | Writer's reproducible code | none |
| NGS split-safety 32.9 / 37.8 / 40.4 / 42.0; every defense >30%; Cover 4 17.2% | VERIFIED | FACTS §10, NFL.com NGS | none |
| nflverse two-high 33.1→43.3, under center 36.1/27.8/33.8 and FTN 27.3/28.8/33.6; 11 personnel; shotgun peak 72% (2023) | VERIFIED | FACTS §10 tables | none |
| <3 WR 41.7% (first ≥38% since 2016); base 29.7% vs 20.5% in 2023; 12 pers 24.4, 13 pers 5.1 | VERIFIED | FACTS §10 (Reber, NGS) | none |
| 2020 Rams, 2023 Ravens, 2024 Eagles led the league in fewest points or yards | VERIFIED | nflverse schedules (LA 296 in 2020; BAL 280 in 2023); 2024 PHI fewest yards (common record) | none |
| 2024 Eagles post-snap two-high 33.7% (27th) | VERIFIED (book calc) | Writer's calc | none |
| Barkley 2,005 yds; SB LIX 40-22; four-man rush with no blitz | VERIFIED | Wikipedia; FACTS §1 | none |
| Rams 2025 13 personnel 31%, 49ers 21 personnel 37%; team under-center list | VERIFIED (book calc) | Writer's calc | none |
| DB share 66 / 78 / 69% | VERIFIED (book calc) | Writer's calc | none |
| Simmons 8th overall in 2020 (ARI), traded to NYG 2023; Hamilton 1st round 2022; Branch 2nd round 2023 | VERIFIED | Wikipedia | none |
| **Bowers 112 catches, rookie record (all positions)** | VERIFIED | NFL.com video "breaks Puka Nacua's single-season record for most receptions by rookie"; Guinness | Sources added; VERIFY removed |
| **Garrett ($160M/4 yrs, $40M, Mar 2025), Watt ($123M/3 yrs, $41M, Jul 17 2025), Parsons ($188M/4 yrs, $47M, Aug 28 2025), each richest non-QB at signing** | VERIFIED | ESPN (Garrett); Boston Globe/AP (Watt, "surpasses Garrett's $40M"); AP (Parsons, "highest-paid non-quarterback in NFL history") | Exact values, dates and sources in `[^edge]` |
| Garrett 23 sacks, single-season record | VERIFIED | FACTS §2 (NFL.com) | none |
| **Juszczyk, March 2017, 4 yrs / $21M, richest fullback contract** | VERIFIED | ESPN 49ers blog; CBS Sports; NFL.com via search ("highest paid fullback in NFL history") | "about $21 million" made exact, with sources |
| Two-back personnel ~7-8% | VERIFIED | FACTS §10 (21 personnel 6.3-8.4) | none |
| Lamar: 32nd pick in 2018; 2019 1,206 rush yds (QB record then), 36 TD passes, unanimous MVP; Ravens 3,296 (team record), 14-2, most points; 2023 MVP | VERIFIED | Wikipedia | none |
| "when he took over midseason they rebuilt the offense around him under coordinator Greg Roman" | CORRECTED | CBS Sports / Ravens.com: Roman was promoted from assistant HC to OC on Jan 11 2019, replacing Mornhinweg (OC 2016-18) | Text now says the 2019 rebuild came under the newly promoted Roman; `[^lamar19]` adds a source |
| Hurts: two SB trips (2022, 2024 seasons); tush push | VERIFIED | Common record; FACTS §5 | none |
| Allen 6-5; double-digit rush TDs in several seasons; 2024 MVP | VERIFIED | nflverse: 15 (2023), 12 (2024), 14 (2025) | none |
| **Allen "76 career rushing TDs by the end of 2025"** | CORRECTED | CBS Sports / NFL.com: 76th TD in Wk 13 2025 broke Newton's 75; nflverse recount 8+9+8+6+7+15+12+14 = 79 at the end of the regular season | Body ("more than any QB in history") kept; footnote now gives the Wk 13 record and 79 at season's end |
| **Daniels 2024 rushing ("about 890")** | CORRECTED (precision) | nflverse: 891 | Footnote says 891; body "more than 850" kept |
| Daniels OROY; NFCCG lost 55-23 at PHI | VERIFIED | nflverse schedules; common record | none |
| QB share of rushing yards, 400-yd QB counts, designed-run rates | VERIFIED (book calc) | Writer's code | none |
| Tush-push ban failed 22-10 on May 21 2025; no 2026 proposal | VERIFIED | FACTS §5 | none |
| Harbaugh fired Jan 2026, now Giants HC | VERIFIED | FACTS §9 | none |
| Romer 2006; Belichick 4th-and-2 in 2009; go rates (book calc) | VERIFIED | Common record; writer's code | none |
| **nflfastR released 2020 (Baldwin and Carl)** | VERIFIED | Announced late April 2020; first on CRAN Sep 1 2020; authors Carl and Baldwin | New `[^fourthtools]` |
| **"Fourth-down calculators appeared on websites and then on broadcasts"** | VERIFIED, made specific | Baldwin's 2020 calculator, cited as "Baldwin (2020a)" in Williams et al., arXiv 2102.01846; NGS Decision Guide announced by NFL/AWS for broadcasters for 2021-22 (GeekWire; NFL.com) | Text names both. The NYT/Burke 4th Down Bot (2013) is noted in the footnote as online only |
| Philly Special: 4th-and-goal at the 1, 38 s left in the half, Clement→Burton→Foles; SB LII 41-33 | VERIFIED | Wikipedia | none |
| Pederson's 2017 Eagles went for it 26 times, 2nd in NFL | VERIFIED | nflverse recount: GB 27, PHI 26 | none |
| Lions most competitive-situation go-for-its in 2021-23 | VERIFIED (book calc) | Writer's code | none |
| NFCCG Jan 28 2024: DET led 24-7 at half; 4th-and-2 at SF 28 up 24-10; 4th-and-3 at SF 30 down 27-24; both incomplete; 34-31 | VERIFIED | nflverse pbp; CBS/AP | none |
| **What public models said about the two Lions fourth downs** ("Models differed... none treated going for it as reckless") | CORRECTED (made specific) | ESPN Analytics: 90.5 vs 90.3 and 39.1 vs 38.8, "toss-ups... leaned very slightly towards going for it" (NBC Sports Bay Area; NBC Sports, Carter); NGS: 86.8 vs 85.8 and 32.7 vs 30.2 (Solak, The Ringer) | Text now quotes the numbers; new `[^lionsmodels]`. "Models differed" was dropped because both models leaned go on both downs |
| Rules table: 2017 OT 10 min; 2018 helmet rule and kickoff alignment; 2019 PI review for one season; 2022 playoff OT; 2024 dynamic kickoff, hip-drop ban, third challenge; 2025 permanent kickoff with TB at the 35, regular-season OT, replay assist; 2026 onside any time, kick from the 50 out of bounds = TB at the 20, fourth floater, ejection consult | VERIFIED | FACTS §3, §4, §6; operations.nfl.com | none |
| Kickoff return rate ~1 in 5 (2023) to ~3 in 4 (2025) | VERIFIED | FACTS §3 (21.8% → 75%) | none |
| "Kickoffs ... four redesigns in nine seasons" | CORRECTED | Kickoff rule changes in 2018, 2023 (fair catch inside the 25), 2024, 2025 and 2026 | "five rule changes in nine seasons (2018, 2023, 2024, 2025 and 2026)" |
| Macdonald Ravens DC 2022-23; 2023 Ravens fewest points (280) and most sacks (60); Seattle HC 2024 | VERIFIED | nflverse schedules; Wikipedia | none |
| Seattle 2025 14-3, fewest points (292) | VERIFIED | FACTS §2; nflverse schedules (SEA 292, HOU 295) | none |
| Kubiak to the Raiders; Fleury from SF; McDaniel Chargers OC; LaFleur Cardinals HC | VERIFIED | FACTS §9, C2 | none |
| "a fifth straight new offensive coordinator in Philadelphia" | CORRECTED | Eagles.com (Mannion hired Jan 29 2026; Sirianni's fifth OC); Steichen covered 2021-22 | "a fourth straight new offensive coordinator"; `[^staffs26]` explains the count (see fact-sheet note above) |
| No 18-game season | VERIFIED | FACTS §6 | none |
