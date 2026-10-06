# Fact-check: 01-02 Downs, Distance, and Field Position

Checked 2026-10-06 against FACTS-current.md, nflverse (every inline number recomputed in the `rtg` container, including the 1999 and 2012 Super Bowl play-by-play) and web sources.
All 5 `<!-- VERIFY -->` comments are resolved and removed. The chapter builds (`build_pdfs.py 01-02-downs-distance-and-field-position --html`: OK).

| Claim | Verdict | Source | Change |
|---|---|---|---|
| Princeton–Yale scoreless ties in 1880 and 1881, with the ball-holding "block game" | CORRECTED (precision) | Pigskin Dispatch 1881 (block game, Nov 24 1881, each side held the ball for a half); Action Football Sundays (1880 game, Nov 25 1880, 0–0, frozen field, safeties rather than ball-holding); Wikipedia 1881 Princeton team | Ball-holding now attributed to the 1881 game only; new fn `block` |
| Camp described as a "former player" in 1882 | CORRECTED | Wikipedia "Walter Camp" (played halfback 1876–1882; medical school 1880–83) | Now "a halfback (and by then a medical student)" |
| 1882 rule: 5 yards in 3 downs; committee thought it unworkable and adopted it on condition it could be dropped | VERIFIED | Saturday Evening Post, Sept 2021 (existing fn `camp`) | None |
| Ten yards and the forward pass in 1906; fourth down in 1912 | VERIFIED | Wikipedia "1906 college football season"; PFHOF "Changing the Rules" | Sources added to fn `camp` |
| "Gridiron" nickname comes from the five-yard lines | SOFTENED | Pigskin Dispatch (credits the 1903 lengthwise lines, name in print by 1911); Wikipedia "Gridiron football" (grid of lines on both axes) | Text now gives both explanations; new fn `gridiron` |
| Chain clip set at a nearby five-yard line so the chain can be carried in | VERIFIED | Wikipedia "Chain crew" (clip at the rear edge of the 5-yard line nearest the rear rod); NFHS/SDCFOA chain-crew instructions | New fn `clip` |
| Hawk-Eye from 2025: six 8K cameras, ~30 s, officials still spot, chains as backup, virtual replay on broadcast and stadium boards | VERIFIED | NPR Apr 1 2025; CBS Sports (HOF Game, six 8K cameras, ~30 s); Sony/Hawk-Eye release (virtual recreation on TV and video boards); FACTS §6 | CBS and Sony added to fn `hawkeye` |
| Touchback on a kickoff that lands in the end zone at the 35 since 2025 | VERIFIED | FACTS §3 (unchanged for 2026) | None |
| Garrett's 23-sack single-season record | VERIFIED | FACTS §2; NFL.com | None |
| Carter & Machol, *Operations Research* 19(2): 541–544, 1971; Carter a Bengals QB | VERIFIED | Crossref metadata for doi 10.1287/opre.19.2.541 (Apr 1971) | None |
| Series success 71%; 4th-down punt/FG/go 51/26/23%; go rate on short 4th in close games 25% (2016) → 53% (2025); 380 INT + 248 lost fumbles; fewer-giveaway team won 79% of 204 games; 1,287 sacks, 6.5% of dropbacks | VERIFIED | Own recalculation (inline code; matches) | None |
| Third down: 3rd & 1 ≈ seven in ten, 3rd & 10 under three in ten; 3rd & 8 ≈ a third | VERIFIED | Own recalculation: 69%, 28%, 34% | None |
| "Above 90% [pass] at every [third-down] distance of four or more" | CORRECTED | Own recalculation, 2025 neutral: 3rd & 4 = 87%, 3rd & 5–12 = 91–99% | Now "close to nine times in ten on third-and-4, and above 90% at every longer distance" |
| 1st & 10 passed a little under half the time; 3rd & short still near half | VERIFIED | Own recalculation: 46%, 46% | None |
| 4th-and-short conversion "often around one in two" | CORRECTED | Own recalculation: 4th & 2 converted 58% (2016–2025) | Now "better than one in two" |
| Sack costs "often seven or eight" yards | CORRECTED | Own recalculation, 2025: mean 6.5, median 7 | Now "about six or seven on average" |
| Drives: one-third end in punts, about four in ten in points | VERIFIED | Own recalculation: punt 33%, TD 23%, FG 16% | None |
| A typical drive's points come "more often three than seven" | CORRECTED | Same calculation: TDs (23%) outnumber FGs (16%) | Now "more often seven than three" |
| Takeaway EP values 0 / 1.6 / 2.6 / 4.5 / 6.3 (own 5, own 35, 50, opp 20, opp 1) | VERIFIED | Own recalculation: −0.05, 1.59, 2.60, 4.50, 6.34 | None |
| 1st & 10 run needs four or five yards to break even | VERIFIED | Own recalculation: mean EPA turns positive at 5 yards | None |
| LIX: Eagles 40–22 Feb 9 2025; drive from PHI 31 at 9:40 Q1; Barkley +2, Goedert +20, +3, +2, McDuffie unnecessary roughness on 3rd & 5, −1, Dotson catch ruled TD and reversed to the 1, Hurts sneak TD | VERIFIED | FACTS §1; nflverse 2024_22_KC_PHI | None |
| Hurts interception by Bryan Cook at KC 2 on 3rd & 10 at KC 30 "later in that first quarter" | CORRECTED | nflverse: play at 14:21 of the 2nd quarter (the footnote already said so) | Now "Early in the second quarter" |
| Barkley over 2,000 rushing yards in 2024 | VERIFIED | 2,005 yards (PFR / NFL records) | None |
| XXXIV: Jan 30 2000, Rams 23–16, drive from TEN 12, first-and-goal at the 10 with six seconds, Mike Jones tackles Dyson at the 1 | VERIFIED | Wikipedia; ESPN 2000; nflverse 1999_21_STL_TEN (shows 0:05 on the clock log) | Footnote notes the 0:05 clock-log discrepancy |
| XXXIV: Dyson caught it "at about the 3" | CORRECTED (softened) | Accounts put the catch at the 4 (ESPN, Wikipedia) or the 3 | Now "inside the 5" |
| XXXIV PFR box-score URL `200001300ram.htm` | CORRECTED | PFR's page is `200001300oti.htm` (Titans the designated home team) | URL fixed |
| XLVII: Feb 3 2013, 34–29, 1st & goal at 7, James +2, three incompletions to Crabtree, no flag on Jimmy Smith contact | VERIFIED | Wikipedia; nflverse 2012_21_BAL_SF | nflverse added to fn `xlvii` |
| XLVII: fourth-down incompletion "with 1:46 left" | CORRECTED | nflverse: 4th-down snap at 1:50; Baltimore ball at 1:46 | Text, caption and figure label now say 1:50; "Baltimore's ball ... with 1:46 to play" |
| XLVII: three Ravens runs, Koch safety from 0:12 to 0:04, free kick from the 20, Ginn return ended the game | VERIFIED | nflverse 2012_21_BAL_SF (Ginn 31-yard return to the 50) | None |
| Kirwan "a former NFL coach"; *Take Your Eye Off the Ball* 2nd ed. 2015 | VERIFIED | Wikipedia (Jets defensive assistant 1989); 01-04 fact-check (2.0 edition 2015) | None |
| *The Hidden Game of Football* (1988), Carroll/Palmer/Thorn | VERIFIED | Warner Books 1988 (catalog records) | None |
| Football mechanics: punter ~15 yards deep; holder 7 yards back so FG length = yard line + 17; missed FG beyond the 20 goes to the spot of the kick; punt touchback at the 20; neutral zone is the length of the ball | VERIFIED | NFL rulebook (Rules 3, 11; standard practice) | None |

## Counts
VERIFIED 21 · CORRECTED 10 · SOFTENED 1 (gridiron nickname) · REMOVED 0. Rows that mix several checks are counted by their verdict.

## Still uncertain / for a human
- XXXIV clock: Wikipedia/ESPN say the last timeout came with six seconds left; the nflverse clock log says 0:05. The chapter keeps "six seconds" (the widely reported figure) and the footnote notes the discrepancy.
- PFR and the INFORMS DOI page return 403 to automated fetches; the PFR URL was confirmed via search listing, the Carter paper via Crossref.
- "Above 90% at every longer distance" on third down holds per yard from 5 to 12 and for the 11+ bucket (92%); single-yard values beyond 12 are small samples.
