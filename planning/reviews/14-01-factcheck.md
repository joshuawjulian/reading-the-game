# Fact-check log: 14-01 Building a Roster

Checked 2026-10-08 against FACTS-current.md, web sources, and nflverse data (trades, draft picks, contracts) re-queried in the `rtg` container. All 25 `<!-- VERIFY -->` comments are resolved and removed. Each footnote is referenced exactly once (script check). Build `build_pdfs.py 14-01-building-a-roster --html`: OK (25 pages).

| Claim | Verdict | Source | Change |
|---|---|---|---|
| 2025 cap $279.2M; 2026 cap $301.2M (first above $300M) | VERIFIED | ESPN, NFL salary cap hits milestone at $301.2M for 2026 | `[^cap]` rewritten with URL; "first time past $300 million" added |
| Cap table 2011–2024 used in code | VERIFIED | OTC salary-cap page; ESPN 2026 piece (2021 = $182.5M) | none |
| Players' share about 48% under the 2020 CBA | CORRECTED (wording) | ESPN CBA explainer (48% floor from 2021, up to 48.5–48.8%) | "about 48" → "at least 48 percent"; new `[^cba]` |
| CBA signed 2020, runs through 2030; FA 1993, cap 1994 | VERIFIED | general record; 11-02 | none |
| Brady retired Feb 1, 2023; about $35M dead money in 2023 from void years | VERIFIED | Pro Football Rumors 2023 dead money; Sportsnaut | `[^brady]` given URLs, $35.1M stated |
| Wilson: $85M dead money, record; split $53M 2024 / $32M 2025 **via a post-June 1 designation** | CORRECTED | AP via KOAA (record $53M 2024 hit; post-June 1 would have been $35.4M/$49.6M) | Removed the post-June 1 claim; text now "split across two league years: a record $53M on 2024 and $32M on 2025"; footnote gives Mar 4 announcement / Mar 13 processing |
| Denver: Nix rookie, playoffs 2024; 14–3 AFC No. 1 seed 2025 | VERIFIED | FACTS-current §2 | none |
| Accrued season = 6+ games on full pay; UFA 4+, RFA 3, ERFA <3; RFA tender compensation | VERIFIED | CBA Arts. 8–9 (OTC) | none |
| Franchise tag formulas, two firsts, exclusive tag, transition top-10, deadline mid-July | VERIFIED | NFL Football Operations, Franchise Tags (deadline July 15, 2026) | none |
| Second tag = 120% of first; third = 144% of second | CORRECTED | NFL Football Operations, Franchise Tags (third = greatest of QB tag, 120% of top-5 avg, 144% of second) | "at least 120 / at least 144 percent ... or the quarterback tag if higher" |
| Cousins tagged 2016 and 2017; Vikings 3 yr $84M fully guaranteed, 2018 | VERIFIED | NFL.com, Inside Kirk Cousins' historic contract | Added $84M and "first multi-year fully guaranteed QB deal"; new `[^cousins]` |
| Comp picks: up to 32, rounds 3–7, max 4/team, salary/snaps/honors | VERIFIED | NFL Ops comp-pick announcement | `[^comp]` URLs |
| Comp picks tradable since 2017 | VERIFIED | ESPN, owners OK comp-pick trading (2017 draft) | URL added |
| 2020 resolution: 3rd-round picks in two straight drafts for losing a minority coach/exec to HC/GM | VERIFIED | NFL.com, owners pass resolution (Nov 2020) | URL added |
| Ravens most comp picks since 1994 | VERIFIED | Baltimore Ravens site (60 through 2025; DAL 58) | new `[^ravens]` |
| Trade deadline after Week 9 since 2024 | VERIFIED | NFL.com, owners extend trade deadline | new `[^deadline]` |
| Waivers: <4 accrued seasons, all players after deadline, worst record priority, prior-season order early | VERIFIED | NFL waiver rules (standard; consistent with Beckham 2021 case) | none |
| Rams: Stafford (Goff, 2021 3rd No. 101, 2022 1st No. 32, 2023 1st No. 6), Ramsey (two 1sts + 4th), Miller Nov 2, 2021 (2022 2nd + 3rd) | VERIFIED | nflverse `load_trades()` | none |
| Beckham released by CLE, cleared waivers, signed with LAR a week after Miller deal | VERIFIED | CNBC (released Nov 8, signed Nov 11, 2021) | dates + URL in `[^rams]` |
| SB LVI: Rams 23–20, Feb 13, 2022; Beckham TD, Miller 2 sacks | VERIFIED | ESPN box score; PFR (Beckham 17-yd TD Q1; Stafford 3 TD) | Vague "central to the win" replaced with the verified specifics |
| Rams: no 1st-round pick 2017–2023; Verse No. 19 in 2024; 5–12 in 2022; Nacua 2023 5th; playoffs 2023 | VERIFIED | nflverse draft picks; schedules | none |
| Snead "picks" T-shirt at parade | VERIFIED | widely reported (Feb 2022) | none |
| Bradford 2010: 6 yr, up to $78M, $50M guaranteed | VERIFIED | NFL.com, Bradford's a big deal | URL in `[^rookie]` |
| Rookie scale 2011; extensions after 3rd season; 5th-year option guaranteed + tiered since 2020 | VERIFIED | CBA Art. 7 (OTC) | none |
| Johnson chart built 1991 for Cowboys; attributed to "part-owner" Mike McCoy | CORRECTED (wording) | Dartmouth Sports Analytics (VP Mike McCoy, at Johnson's request, past trades + judgment) | "Cowboys vice president Mike McCoy drew it up ... 1991"; new `[^jjchart]` |
| Johnson chart values (1=3000, 16=1000, 32=590, 64=270, 100=100; full table in code) | VERIFIED (picks 1–160); approx. 161–224 | Drafttek chart (identical through 160; 7th-round tail differs by ≤0.4 pt among published versions) | code comment updated; no numeric change (effect on figures negligible) |
| Massey–Thaler: 2005 working paper; *Management Science* 59(7) 2013, 1479–1495, DOI 10.1287/mnsc.1120.1657 | VERIFIED | RePEc listing | DOI link added |
| Massey–Thaler: surplus peaks "around the early second round" | SOFTENED | Secondary summaries say highest in round 2; exact peak not confirmed | "sat in the second round" |
| Thaler Nobel prize | VERIFIED | 2017 Nobel in economics | none |
| Next-contract value method "popularized by Ben Baldwin" | CORRECTED | Brill & Wyner / OTC: the second-contract chart is Fitzgerald–Spielberger (OTC) | attribution changed in `[^mt]` |
| Lance trade: No. 12, 2022 1st (No. 29), 2023 1st (No. 29), 2022 3rd (No. 102) | VERIFIED | nflverse trades; 2023 No. 29 was used by NO (pick passed MIA→DEN→NO) | none (the Writer's "three firsts plus a third" stands) |
| Lance: 4 starts in two seasons, ankle 2022, traded to DAL Aug 25, 2023 for a 2024 4th | VERIFIED | nflverse trades | none |
| Purdy: No. 262, last pick 2022; rookie cap hits < 1% (<0.5%) of cap; NFC CG 2022, SB 2023 | VERIFIED | nflverse draft picks / contracts | none |
| Purdy extension May 2025: 5 yr, $265M, $53M APY; $100M fully guaranteed at signing | VERIFIED | Over the Cap; AP | guarantee added to text and `[^purdy]` |
| 49ers drafted 10 OL 2017–2025; McGlinchey No. 9 2018, Banks 2nd 2021, Puni 3rd 2024, Burford 4th 2022, McKivitz 5th 2020 | VERIFIED | nflverse draft picks | none |
| Trent Williams trade April 2020 for 2020 5th + 2021 3rd | VERIFIED | nflverse trades | none |
| Kelce 6th round (2011); Mailata 7th round 2018, rugby league | VERIFIED | nflverse draft picks | none |
| Eagles OL share above league every year 2014–2025, ≥5 pts in about half | VERIFIED | rendered figure (6 of 12 seasons ≥ ~5 pts) | none |
| Market tiers: guards/centers + S/LB/RB/TE "all between 5 and 7 percent" | CORRECTED | rendered fig-market (G/C 8.5%, S 7.1%, TE 5.5%) | "guards and centers at about 8.5 percent, then ... roughly 5.5 to 7 percent" |
| QB top-10 ≈1.5× edge, >3× RB | VERIFIED | rendered fig-market (22.4 / 14.2 / 6.2) | none |
| Barkley 2,005 yards in 2024 | VERIFIED | record | none |
| Combine: Indianapolis since 1987; "roughly 300" invitees | CORRECTED (wording) | Giants.com: 319 invited in 2026 | "more than 300 (319 in 2026)"; glossary "about 300" → "more than 300" |
| RAS: Kent Lee Platte, 0–10, percentiles vs position since 1987 | VERIFIED | ras.football | none |
| OL weights: zone 295–315, gap 315–340 | SOFTENED | No authoritative source; chapter's own data show 311 vs 314 lb | Reworded as rough tendencies, with a pointer to the 49ers data |
| Seahawks (Carroll) corners: 6 ft+ with long arms | VERIFIED (made specific) | ESPN Seahawks blog: every drafted corner 2010–2020 had 32"+ arms; 7 of 8 were 6 ft+ | Text now states 32-inch arms, nearly all 6 ft+; new `[^seacb]` |
| Practice squad 16 (+1 international), up to 6 veterans; 2 elevations a game, 3 per player; IR 4-game minimum, 8 returns | VERIFIED | CBS Sports 2022 rule changes; 2026 team reporting (same limits) | `[^ps]` given URL |
| 48 actives with 8 OL (else 47); inactives 90 min before kickoff | VERIFIED | NFL roster rules | none |
| Emergency 3rd QB since 2023 | VERIFIED | FACTS-current §4; CBS Sports | none |
| 2022 NFC CG: 49ers "finished the game with McCaffrey taking snaps" | CORRECTED | NBC Sports Bay Area: injured Purdy returned after Johnson's concussion | Now says McCaffrey was the only emergency option and Purdy returned barely able to throw; URL added to `[^eqb]` |
| Go deeper: Massey–Thaler 2013; Brandt (ex-Packers, SI, Villanova); Fitzgerald and Spielberger at OTC; Kirwan | VERIFIED | general record | none |

## Counts

VERIFIED 40 (incl. 1 made more specific) · CORRECTED 9 · SOFTENED 2 · REMOVED 0.

## Uncertain / notes

- The Massey–Thaler round-2 peak comes from secondary summaries; the text now says only "in the second round".
- The 7th-round values on the Johnson chart differ slightly across published versions. The code's tail is within 0.4 points of Drafttek's, which doesn't visibly change any figure.
- Waiver-priority timing ("until the fourth week") is standard but was not re-sourced.
