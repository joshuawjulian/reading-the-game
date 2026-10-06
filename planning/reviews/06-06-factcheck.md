# Fact-check: 06-06 Disguise, Rotation, and Split-Field Coverage

Checked 2026-10-06 against FACTS-current.md, the 2026 NFL rulebook PDF (operations.nfl.com), nflverse (recomputed in the `rtg` container) and web sources.
All 9 `<!-- VERIFY -->` comments are resolved and removed. The chapter builds (`build_pdfs.py 06-06-disguise-rotation-and-split-field`: OK, 21 pages).

| Claim | Verdict | Source | Change |
|---|---|---|---|
| Safety backpedals 4–5 yd/s, turned and running ~7 yd/s | SOFTENED | NGS via Colts.com 2017 (fastest safeties ~22 mph); NASE study of college DBs (cross-over faster than backpedal over 0–5 yd). No source gives yd/s for a backpedal | Specific speeds removed; now "backpedal is noticeably slower than turning and running; fastest safeties ~22 mph, ~10 yd/s, rarely near full speed while reading"; new fn `dbspeed` |
| Deep pass released "around 2.5 to 3 seconds" | CORRECTED | Own nflverse calc, 2025 REG: air_yards ≥ 20, median time_to_throw 3.1 s, IQR 2.6–3.6 s (n = 1,993) | Now "around 3 seconds (middle half 2.6–3.6 s)"; new fn `ttt` |
| Offense set 1 s; one man in motion, not toward the line; defense free to move; no disconcerting signals | VERIFIED / CORRECTED (precision) | 2026 Rulebook 7-4-6, 7-4-7, 7-4-8; 7-4-3/4/5; 12-3-1(i) ("acts or words ... designed to disconcert an offensive team at the snap") | Text now "words or acts meant to disconcert the offense at the snap, such as imitating its snap count"; fn `rules` gives exact rule numbers |
| Saban was Belichick's DC in Cleveland 1991–1994 | VERIFIED | Eleven Warriors (Mar 23 2020); Wikipedia | None |
| Cover 7 lineage to the "Saban-Belichick vocabulary" | SOFTENED | Soran/Throw Deep (pattern-match coverage dates to Saban's Cleveland years with Belichick); Eleven Warriors ("Man-Match Quarters coverage, which Saban calls Cover 7") | Text and glossary now "Nick Saban's vocabulary, whose pattern-matching roots go back to Cleveland"; fn `saban7` expanded |
| Cover 7 "the work horse", "a form of quarters coverage"; per-side calls | VERIFIED | Soran, Throw Deep (Feb 24 2021): quotes exact; "7 Mod", "Triple 7 Clip" | Per-side calls noted in fn |
| MSU (Dantonio/Narduzzi), TCU (Patterson), Iowa as split-field quarters reference programs studied at clinics | VERIFIED | FootballScoop 2014 (Narduzzi's 80-min Cover 4 talk at Angelo clinic); Chris B. Brown, Grantland 2015 (Patterson clinic talks on quarters "Blue"); MatchQuarters 2024 (Iowa, Phil Parker "Under 4-3 Quarters", split-field) | New fn `quartershistory` |
| Saban carried his version to MSU, LSU, Alabama | VERIFIED | Eleven Warriors 2020 (Dantonio learned Cover 7 as Saban's DB coach at MSU, 1995–) | Added clause on Dantonio |
| NGS two-high 32.9/37.8/40.4/42.0%; Cover 6 9.2% in 2025 | VERIFIED | FACTS §10 (NFL.com NGS) | None |
| Evero "successor in Staley's coaching tree"; Denver DC 2022, Carolina from 2023; split-field emphasis | CORRECTED (precision) / VERIFIED | Wikipedia (Rams safeties coach 2017–20, so on Staley's 2020 staff; Fangio 49ers staff); MatchQuarters Apr 20 2026 (Carolina ~1:1 two-high static vs rotated) | Now "coaches from that staff and Fangio's tree, such as Evero (Rams safeties coach in 2020 ...)"; fn `evero` rewritten |
| Evero 2026 status (extension Jan 2026) | VERIFIED | Panthers.com Feb 1 2026 (returns as DC); Wikipedia (Canales announced extension Jan 11 2026) | In fn `evero` |
| Poach beaters: X-iso, "slant, dig or back-shoulder fade" | SOFTENED | Wilhite (Dec 29 2025) shows an over-the-ball route behind the poaching safety; no source lists those three routes | Now "attack him knowing no safety is coming, or attack the poaching safety with a route breaking behind him"; fn dated |
| Solo: Mike takes #3, backside safety freed as run fitter (Lehigh) | VERIFIED | X&O Labs (Kuchar with Nagy) via search snippet (page 403 to fetch) | None |
| Solo: "others let him rob the lone receiver's in-breaking routes" | REMOVED | No source found | Clause cut from text, figure caption and on-field label ("FS free: extra run fitter") |
| Solo/stubbie/poach are dialect-dependent | VERIFIED, strengthened | Cody Alexander, MatchQuarters (Jul 11 2022): his "Solo" = backside safety takes #3 vertical (this chapter's poach); Soran: Saban's poach call is "Clip" | Added "names collide" sentence; glossary def says "one common version of Solo" and notes the collision |
| Stubbie assignments in Saban's system (corner MEG #1, apex #2, hook walls #3, safety #3 vertical/over #2) | VERIFIED | Soran, Throw Deep | None |
| "Mable" = Saban's rotate-to-trips version | VERIFIED | Soran: "Mable means the safety is dropping down to the passing strength" (Cover 3/6 adjustment to 3x1) | None |
| PFF motion 63.9% (2025) vs 43.0% (2018) | VERIFIED | FACTS §10 (PFF, Feb 23 2026) | None |
| BDB 2025: pre-snap theme, first full pre-snap frames, 2022 Weeks 1–9 | VERIFIED | Kaggle overview; arXiv:2502.16313 (first nine weeks of 2022; all frames pre- to post-snap) | Footnote: dead/irrelevant ops.nfl.com link (now shows 2026) replaced with Kaggle + arXiv |
| Winners Bajaj and Sandwar (NYU), "Exposing Coverage Tells in the Pre-Snap" | VERIFIED | NYU SPS; NYU Stern (Aug 24 2025) | Stern added for the title |
| NGS pre-snap disguise model credits BDB winners; quote "If a defense shows split-safety zone ... we flag it as disguised." | VERIFIED | NFL.com NGS 2025 metrics article (quote exact) | Footnote date "Sept. 3, 2025" not confirmable; now "2025" |
| Flores Vikings DC since 2023, still in 2026 | VERIFIED | FACTS §9 | None |
| Vikings 2023 blitz rate 50.7%, highest | VERIFIED | CBS (Trapasso, Sept 26 2024) | None |
| Week 2 2024 Vikings 23–17 49ers; Purdy to Flores "The scheme, man, it's crazy." | VERIFIED | CBS (postgame handshake) | None |
| Vikings 2025 blitz 46.3%, next-highest 38.7% | VERIFIED (dated) | SI (Olsen, Dec 18 2025) linking NFL Pro | Now "Through mid-December 2025" (article is pre-season-end) |
| Vikings 51.4% two-high (1st), 5.8% Cover 0 (2nd); KC close | VERIFIED | Own recalc 2023–25 REG: MIN 51.4/5.8; KC 49.7/6.3 (KC 1st in C0) | League median two-high corrected 40.7% -> 40.6% in fn `labels` |
| Staley: first-time NFL DC in 2020, from Fangio's Denver staff; Donald and Ramsey | VERIFIED | The Ringer (Jan 13 2021) | New fn `ringer` |
| Rams 2020 two-high shell, rotations post-snap, Ramsey moved around | VERIFIED / CORRECTED (precision) | The Ringer: "showing ... one coverage before rotating into a different look right after"; Ramsey often the nickel/"Star"; "much lighter boxes" | "outside corner to the slot" -> "outside corner to the nickel ('star') spot" |
| Rams 2020 "rarely had to blitz" | CORRECTED | Own nflverse calc (2020 participation, NGS): 5+ rushers on 26.0% of dropbacks, 15th-lowest, median 27.4%; secondary report 27.3%, mid-pack | Now "didn't need to blitz more than an average defense (about a quarter of dropbacks, close to the median)" |
| Rams 2020: 18.6 PPG, 281.9 YPG, 190.7 pass YPG, all 1st | VERIFIED | therams.com (Jan 7 2021); The Ringer (190.7). PFR blocks automated fetches | Note in fn to spot-check PFR |
| Staley hired as Chargers HC after one season | VERIFIED | AP via KSAT (Jan 17–18 2021) | Added to fn `rams2020` |
| Cody Alexander, *Match Quarters: A Modern Guidebook to Split-Field Coverages* | VERIFIED | MatchQuarters; AbeBooks (2019) | None |
| *The Art of Smart Football* (2012) | CORRECTED | Published 2015 (Eleven Warriors review Aug 2015; catalogs) | Now 2015 |
| *The Essential Smart Football* (2012) | VERIFIED | CreateSpace 2012 | None |
| Tracking at 10 Hz from shoulder-pad chips | VERIFIED | NGS (RFID chips in shoulder pads); arXiv:2502.16313 (10 Hz) | None |
| pff_passCoverage label strings in eval:false code | NOT CHECKED (code comment already says to check the year's label list) | — | None |

Counts: VERIFIED 25 · CORRECTED 6 · SOFTENED 3 · REMOVED 1 (plus 1 not checked).

Still uncertain: X&O Labs Solo article could only be read via search snippets (403); Rams 2020 stats not seen on PFR itself; NGS article's exact publication date.
