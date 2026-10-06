# Fact-check: 04-03 The Quick Game

Checked 2026-10-06 against FACTS-current.md, nflverse (recomputed in the `rtg` container) and web sources.
All 10 `<!-- VERIFY -->` comments are resolved and removed. The chapter builds (`build_pdfs.py 04-03-quick-game --html`: OK; 23 pages).
Every footnote is referenced exactly once (20 footnotes; `[^walshrun]` and `[^airraid]` are new).

| Claim | Verdict | Source | Change |
|---|---|---|---|
| Median 2025 attempt out at 2.5 s; ~half under 2.5 s (48% <2.5, 52% <=2.5; n = 17,394) | VERIFIED | Own nflverse recalculation (exact match) | None |
| 2.5 s is an analysts' convention "Next Gen Stats and PFF both use it" | CORRECTED | PFF "Signature Stat Snapshot: Time To Throw" uses the 2.5 s split; no primary NGS definition found | Footnote now cites PFF only |
| Quick completion 72% vs 57%; success 51% vs 45% | VERIFIED | Own recalculation (72.2/57.1; 51.5/44.9) | None |
| 59% of quick-completion yards after the catch vs 38% | VERIFIED | Own recalculation (58.7/38.5) | None |
| EPA by rush count: quick +0.118/+0.226, held -0.014/-0.098; 27% five-plus rushers | VERIFIED | Own recalculation (held 5+ = -0.102 with spikes excluded; within rounding of "about -0.10") | None |
| Walsh thought of short throws as an extension of the run, "a handoff through the air" | SOFTENED | Walsh to Tom FitzGerald (SF Chronicle) via Encyclopedia.com: "We couldn't control the football with the run… high-percentage, short, controlled passing game"; same profile: "effectively extended handoffs". No Walsh "extension of the run" wording found | Prose now: built from a team that couldn't run, used short throws to do the run's job, "often described as extended handoffs"; new fn `walshrun` |
| Walsh a Bengals assistant in 1970 under Paul Brown; Bengals a "three-year-old" team | VERIFIED | Wikipedia "West Coast offense"; Bengals began play 1968 | Footnote notes 1968 |
| Greg Cook wrecked his shoulder as a rookie in 1969 | VERIFIED | Wikipedia "Greg Cook" (torn rotator cuff, game 3 of 1969; surgeries; out the next three seasons) | Footnote said "1970 shoulder injury": CORRECTED to the 1969 injury |
| Carter accurate but weak-armed; Walsh built the short game around him | VERIFIED | Wikipedia "West Coast offense" | Source added |
| Carter led NFL in completion % in 1971 (62.2%) | VERIFIED | PFR 1971 leaders (138/222, 62.2%) via search; Wikipedia "Virgil Carter" (PFR passing page returned 403 to the fetcher) | URL switched to PFR leaders page |
| Carter studied statistics (BYU), MBA at Northwestern during playing career | VERIFIED | ESPN 2024 (Carter's EPA legacy): "majored in statistics… at BYU", MBA at Northwestern while with the Bears | Source added |
| Carter & Machol, *Operations Research* 19(2), 1971, 541–544; 1969 data | VERIFIED | RePEc/IDEAS record (8,373 plays, first 56 games of 1969) | Detail + URL added |
| *Finding the Winning Edge* (Sports Publishing, 1998) | CORRECTED | ISBN 9781571671721, published 1997 | 1998 -> 1997 in footnote and Go deeper |
| Walsh to San Diego, Stanford, 49ers 1979; three SB titles after 1981, 1984, 1988 | VERIFIED | PFHOF Walsh bio (Class of 1993; 1979–88; XVI, XIX, XXIII); Wikipedia | None |
| Rice 22 TD catches in 12 games in 1987, a record | VERIFIED | PFHOF Rice bio (Class of 2010); Wikipedia (record stood 20 years) | Footnote notes Moss's 23 (2007) |
| 1978: contact barred beyond 5 yards; 1977 one-contact limit; "Mel Blount rule" | VERIFIED | PFHOF chronology 1977 and 1978 (quoted); Steelers Depot 2024 | Dead PFHOF URL (1970-1979 path, 404) replaced with the 1960-1979 path; quotes added |
| Rule detail: chuck within 5 yards; beyond 5 contact is illegal contact or holding | VERIFIED (made precise) | NFL Rulebook TOC (Rule 8 Sec. 4 "Legal and Illegal Contact With Eligible Receivers"); Video Rulebook text (Arts. 1–3; restriction applies while passer in pocket with ball; 5 yds + auto first down); holding is Rule 12 Sec. 1 | Footnote gives articles and the pocket condition; prose unchanged |
| 2004 crackdown after the 2003-season AFC Championship Game | VERIFIED | NBC Sports Boston "Ty Law Rule" | Source added |
| Backward pass hitting the ground is live; either team may recover | VERIFIED | Rule 8 Sec. 7 "Backward Pass and Fumble"; Video Rulebook summary (either team may recover and advance) | None in prose |
| Footnote: "defense may not advance it in some situations" | CORRECTED | Same; the 4th-down/two-minute limits apply to fumbles only (matches 04-01 fact-check) | Footnote rewritten |
| Spacing "associated above all" with the Air Raid, "thrown on every down" | SOFTENED | AP (Russo, Aug 24 2022): Air Raid foundations "mesh, Y cross, four verts, the quick game"; no source ranks spacing as its signature | Prose: "a natural fit for" the Air Raid, which spread receivers wide and made the quick game a foundation; new fn `airraid` |
| Payton HC 2006–2021; Brees QB 2006–2020 | VERIFIED | Common record; Payton suspended for 2012 | Footnote notes the suspension |
| Brees completion record 72.0% (2017), 74.4% (2018); still the record | VERIFIED | Guinness World Records; PFR; own nflverse check 2019–2025 (best since: Brees 2019 ~74%, Maye 2025 ~72%) | Guinness source added |
| Brees 2019 second-fastest TTT (2.57 s, of 26 with 300+ att) and aDOT ~6.5 | VERIFIED | Own recalculation (2.570 s, 2nd of 26; aDOT 6.4 on completions+incompletions) | None |
| Thomas 149 catches in 2019, passing Harrison's 143 (2002) | VERIFIED | NFL.com Dec 22 2019; NFL.com OPOY article | Dead NFL.com URL replaced |
| Thomas catches "a huge share of them on slants and other quick routes" | CORRECTED (replaced with a charted figure) | Own nflverse calc: 104 of 149 (70%) under 10 air yards, half within 5 | Prose: "about seven in ten of them on throws that traveled less than ten yards in the air" |
| Welker 112 (2007, tied with Houshmandzadeh), 123 (2009), 122 (2011), led league 3 times in 5 years | VERIFIED | Wikipedia "Wes Welker"; nflverse (Houshmandzadeh 112 in 2007) | Tie stated in footnote |
| Most Welker catches within a few yards of the LOS | VERIFIED | Own nflverse calc: 51–65% of his catches at <=5 air yards in 2007/09/11 | Numbers added to footnote |
| Brady fastest TTT of regular starters in 2022, at 45, with Tampa Bay; 2nd in 2021 | VERIFIED | Own recalculation (2.45 s, 1st of 30 with 300+ att; 2021 2nd behind Roethlisberger); born Aug 3 1977 | None |
| Hill traded to Miami March 2022 for five picks | VERIFIED | NFL.com Mar 23 2022 (2022 1st/2nd/4th, 2023 4th/6th) | Dead URL replaced with the live article |
| KC aDOT 9.06 (5th) 2018; 7.24 (23rd) 2022; 6.47/6.37 (31st) 2023–24; 7.80 (17th) 2025; "second-shortest" | VERIFIED | Own recalculation with the chapter's filter (exact match) | None |
| Kelce 153 targets in 2022, 72.5% under 10 air yards | VERIFIED | Own recalc (152 with air yards, 73%) | None |
| Chiefs won SB after 2022 and 2023 seasons; Mahomes first starter season 2018 | VERIFIED | Common record; FACTS-current consistent | None |
| Contested-catch shares (13.9%, 41.9% vs 71.1%) | VERIFIED (not recomputed) | Course calc from FTN `is_contested_ball`; method stated in footnote | None |
| BDB 2025: 2022 season weeks 1–9; plays.csv `timeToThrow`, player_play `routeRan` | VERIFIED | FACTS-current §BDB; public BDB 2025 header dumps on GitHub list `timeToThrow` | None |
| Football-technical: three-step drop timing, leverage rules, slant-flat/stick/snag/spacing/speed out/double slants/hitch-seam reads, release/stem/stack, now/bubble screens, numbers-leverage-grass | VERIFIED (standard coaching doctrine) | Consistent with 04-01/04-02 and Chris Brown's Smart Football essays | None |

Counts: VERIFIED 30 · CORRECTED 4 (plus the Cook injury-year fix inside a VERIFIED row) · SOFTENED 2 · REMOVED 0.

Notes:
- PFR pages returned 403 to the fetcher; PFR figures were confirmed through search snippets and nflverse.
- The NFL Video Rulebook URLs (illegal contact, backward pass) 404'd to the fetcher (as in the 04-01 check); the rule text was confirmed through search summaries of those pages and the rulebook TOC.
