# Fact-check log: 02-02 Formation Rules and the Language of Alignment

Checked 2026-10-06 against FACTS-current.md, the NFL rulebook page (operations.nfl.com, current edition), web sources, and recomputed nflverse data in the `rtg` container. All 11 `<!-- VERIFY -->` comments resolved and removed. Build `build_pdfs.py 02-02-formation-rules-and-vocabulary --html`: OK (19 pages); figure 1 re-inspected after its label change.

| Claim | Verdict | Source | Change |
|---|---|---|---|
| Seven or more on the line; ends eligible; one player may be directly behind the snapper; illegal formation 5 yds | VERIFIED | NFL Rule 7-5-1 | Footnote `[^formrules]` rewritten with exact rule numbers and quotes |
| "On the line" = helmet breaks plane through the center's waist, shoulders square | VERIFIED (wording) | NFL Rule 3-18-3 ("beltline of the snapper"; shoulders facing B's goal line) | Footnote corrected: it is Rule 3, Section 18, Art. 3, and the rule says "beltline" and "facing", not "roughly parallel" |
| Backs at least a yard behind the line; QB under center the one exception | VERIFIED | Rules 8-1-5, 3-42, 7-5-1 ("neither clearly on nor clearly off") | Cited in footnote |
| Fig. 1 label "line of scrimmage (the back tip of the ball)" | CORRECTED | Rule 3-18-1 (NFL line of scrimmage = plane through the *forward* point; neutral zone between the points) | Label now "the offense's line (the back tip of the ball)" |
| Receivers check on/off with the wing officials (line judge, down judge) | SOFTENED | CBS Sports Dec 19 2022 (referee John Hussey pool report) | Added: the official usually answers but isn't required to; new footnote `[^wing]` |
| Covered tight end is legal, just ineligible | VERIFIED | NFL Rule 7-5-1; operations.nfl.com glossary "Ineligible receiver" | none |
| Seven-on-the-line rule adopted 1910 after mass-play deaths; 1905 near-ban | VERIFIED | Dartmouth Alumni Magazine Nov 1910; Wikipedia; Miller | Contemporary source added |
| Flanker a "1950s innovation" of the Rams, Hirsch moved from halfback | CORRECTED | PFHOF Hirsch page; PFRA Coffin Corner | Now "around 1949–50" (Shaughnessy made him a flanker in 1949; three-end offense 1950); footnote URL fixed (old one 404) and dating dispute noted |
| Hirsch one of the great receivers of the decade | VERIFIED | PFHOF (1,495 yds 1951, record; HOF 1968) | none |
| Shotgun: Red Hickey's 49ers 1960, beat the Colts; Landry revived 1975 for Staubach | VERIFIED | PFHOF "The Shotgun Formation" (Nov 27 1960, 30–22 at Baltimore); Wikipedia | PFHOF source added |
| Shotgun on ~1 in 5 plays in 2006, ~2 in 3 in the 2020s | VERIFIED | Recomputed nflverse `shotgun`: 19.4% (2006); 65.8–72.0% (2020–25) | none |
| Pistol designed by Chris Ault at Nevada, 2005 | VERIFIED | Nevada Sagebrush 2015 "Ten years later"; Wikipedia | Sources added |
| Kaepernick (Nevada) took it to NFL; 49ers and Washington pistol option 2012 | VERIFIED | common record; 03-04 covers | none |
| QB depth stats: 69% / 34% / 28% pass; PA 81% / 21%; 3rd-and-7+ 97% gun; 3rd/4th-and-1 61% UC | VERIFIED | Recomputed: S 69.4, U 33.5, P 27.7; PA U 81.0, S 20.7; 97.5; 61.1 | none (computed inline, asserted) |
| Under-center share 27.3% (2023) → 33.6% (2025); neutral 36% → 44% | VERIFIED | FACTS-current §10; recomputed 27.4/29.0/33.7 and 35.9/38.0/44.0 | none |
| NFL numerals: bottoms 12 yds in, 2 yds tall; hashes 70'9"; college 60' (13 vs 6 yd difference) | VERIFIED | NFL Rule 1 (Art. 4 Item 1; inbounds lines) | none |
| "On the numbers" ~17 yds from ball field side, ~11 boundary | VERIFIED (arithmetic) | 53.33 − 13 − 23.58 = 16.75; 23.58 − 13 = 10.6 | none |
| OL numbered 50–79; reporting to referee, who informs defense | VERIFIED | Rule 5-1-2, 5-3-1 | Footnote `[^reporting]` given exact article numbers |
| Reported status must be kept / re-reported each play | VERIFIED | Rule 5-3-1, 5-3-2 | Added to footnote (stays until timeout, quarter end, 2-min warning, foul, review, TD, kick, change of possession, or a snap out) |
| NCAA: linemen can't report eligible; five 50–79 required; "the only exception is a scrimmage-kick formation" | CORRECTED | NCAA 7-1-4-a via SDCFOA; Wikipedia "Eligible receiver" | The kick-formation exception lets eligible-numbered players fill interior line spots (as ineligibles); it never makes a 50–79 player eligible. Text and footnote rule numbers (7-1-4-a, not 7-1) fixed |
| A-11: Piedmont HS, Bryan and Humphries, 2007; NFHS closed loophole 2009 | VERIFIED | Wikipedia; Philadelphia Inquirer Mar 16 2009 (closed Feb 2009) | "any player could be eligible" sharpened to "every player wore an eligible number"; "February 2009" |
| NE 35–31 BAL, Jan 10 2015; BAL led 14–0 and 28–14 | VERIFIED | nflverse pbp `2014_19_BAL_NE` | none |
| Formation: four OL; Vereen reported ineligible and "lined up out wide"; Hoomanawanui at the tackle spot | CORRECTED | Boston Globe Jan 12 2015; CBS Sports; ESPN Mar 25 2015 (three snaps, Vereen "as a slot receiver") | Vereen was in the right slot *on the line* inside Edelman, not wide; Hoomanawanui at left tackle with Solder moved to guard. "Several snaps" → three; table and later "out wide" fixed; new footnote `[^patsform]` |
| Hoomanawanui 16 yds, then 14 to BAL 10 with "NE 34-Vereen ineligible" | VERIFIED | nflverse pbp (9:33 and 7:19, Q3) | none |
| Harbaugh protested no time to identify eligibles; bench unsportsmanlike, half the distance | VERIFIED | CBS Boston Jan 10 2015 (quotes); pbp (5 yds from BAL 10, "Penalty on BAL bench") | none |
| Gronkowski TD "on the next play" | CORRECTED | pbp: incomplete to Edelman (6:57), then Gronk 5-yd TD (6:52) | "Two plays later" |
| Brady "study the rule book"; Harbaugh "deception" | VERIFIED | CBS Boston Jan 10 2015 | Direct URL and exact quotes in `[^bradyquote]`; text now quotes "clearly deception" |
| 2015 rule: player reporting ineligible must line up inside the core | VERIFIED | ESPN Mar 25 2015; Rule 5-3-1 and penalty (illegal substitution, 5 yds) | Footnote `[^rule2015]` with URL and exact wording; "stand out wide" → "split out" |
| Six-lineman snaps and report shares by season (1,771 in 2025, ~80% reported, 21–28% passes) | VERIFIED | computed inline with assertions in the chapter | none |
| Lions linemen targeted 9 times 2016–25, most; KC second with seven | CORRECTED (minor) | Recount (nflverse rosters T/G/C, REG): DET 9, KC 6 | "Kansas City was next with six" |
| Sewell 9-yd catch vs MIN Dec 11 2022 (34–23); Skipper 4 yds vs MIN Wk 18 2023; Skipper 9-yd TD vs BUF Dec 15 2024 (48–42) | VERIFIED | nflverse pbp | none |
| DET 170 reported plays 2022–24, third most; 35% pass vs 24% league | VERIFIED | Recount: CLE 270, BUF 258, DET 170 (35.3%); league 24.0% | none |
| St. Brown 70-yd TD, 2nd-and-5, Skipper reported, Jan 7 2024 | VERIFIED | pbp `2023_18_MIN_DET` Q4 15:00 | none |
| Ben Johnson DET OC 2022–24, Bears HC 2025 | VERIFIED | FACTS-current | none |
| Lions' Dec 2023 two-point try at Dallas wiped out over reporting | VERIFIED | told in 02-01; FACTS-current | none |
| Kirwan, *Take Your Eye Off the Ball* (2010; 2.0 2015); Brown, *Art of Smart Football* (2015) | VERIFIED | publisher listings (common record) | none |

Counts: VERIFIED 27 · CORRECTED 7 · SOFTENED 1 · REMOVED 0.

Still uncertain / for the editor:
- Which of the three Patriots snaps had which ineligible player is not fully documented: the Globe describes the first (Vereen), the pbp records Vereen on the last (7:19). Reports differ on the middle one (one says Hoomanawanui reported ineligible, another shows Gronkowski at "left tackle"), so the chapter now names Vereen only for the first and last.
- The text's "half the distance to the goal" and "Hoomanawanui 16 yds" being one of the three trick snaps is consistent with the pbp but not separately confirmed.
