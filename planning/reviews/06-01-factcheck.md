# Fact-check: 06-01 Coverage Fundamentals

Checked 2026-10-06 against FACTS-current.md, nflverse (recomputed in the `rtg` container) and web sources.
All 6 `<!-- VERIFY -->` comments are resolved and removed. The chapter builds (`build_pdfs.py 06-01-coverage-fundamentals --html`: OK).

| Claim | Verdict | Source | Change |
|---|---|---|---|
| NFL hashes ~3 yd either side of the middle; boundary ~23½ yd, field side ~30 with ball on a hash | VERIFIED | NFL Rulebook Rule 1 (hashes 70'9" from sideline → 23.6 yd; field 53⅓) | None |
| Yard-line numbers start 12 yd from the sideline (~15 from the middle) | VERIFIED | Wikipedia, American football field (bottom of numbers 12 yd from sideline) | None |
| Deep thirds ~18, halves ~27, quarters ~13 yd wide | VERIFIED | Arithmetic on 53⅓ yd | None |
| Contact allowed within 5 yd; illegal contact beyond; 5 yd + automatic first down; defensive holding same penalty; Rule 8, Sec. 4 | VERIFIED + CORRECTED (precision) | operations.nfl.com rulebook penalty table (illegal contact 8-4-3, def. holding 12-1-6, 5 yd); PhiladelphiaEagles.com "Football 101" 2014 (pocket condition, automatic first down); SI 2025 (Lions proposal to drop the automatic first down failed); FACTS 2026 rule changes don't touch it | Text adds "as long as the quarterback is still in the pocket with it"; footnote rewritten with article numbers and the 2025/2026 status |
| 1978 "Mel Blount rule" limited contact to 5 yd | VERIFIED | Wikipedia 1978 NFL season; Steelers Depot Feb 2024 (via search; 403 to fetch); CBS Sports | None |
| 2004 crackdown after the Jan 2004 AFC Championship; "Ty Law rule" | VERIFIED | NBC Sports Boston (Patriots 21–14, Jan 19 2004; Law 3 INTs; Fisher quote) | None |
| Saban built pattern-matching Cover 3 with Belichick in Cleveland, early 1990s; Soran quote "simply did not exist" | VERIFIED | Soran, Throw Deep Publishing, Feb 24 2021 (quote confirmed verbatim) | None |
| Soran described as "Saban's coverage expert" | CORRECTED | Soran's own article: "Not being affiliated with – let alone a member of – Alabama's defensive staff" | Now "the coaching writer Cameron Soran, whose guide to Saban's coverages is the most detailed public account"; footnote notes he is an outside student |
| Saban Browns DC 1991–1994 | VERIFIED | Wikipedia, Nick Saban | Source added to fn `saban` |
| Saban numbering: Cover 3 rotates to strength, 6 = weak-rotation Cover 3, 7 = split-field match family | VERIFIED | Soran 2021; Alexander, MatchQuarters Jun 12 2023 ("In the Saban system, '6' refers to weak rotation Cover 3") | None |
| Fangio's Cover 8 = what most call Cover 6, with the Cover 2 half toward the passing strength | VERIFIED | Alexander 2023 ("puts the Cover 2 side to the Ni and the Quarters side away"); Alexander Aug 2 2025 ("putting Cover 2 to the strong side, or passing strength") | Footnote no longer claims the two pieces disagree: both put the half to the nickel/strength side |
| 2022 Seahawks "nickel cover-9 defense (cover-3 with safety rotation away from the nickel defender)" | VERIFIED | West Coast Football Substack, Dec 24 2022 (quote verbatim) | None |
| Madden's Cover 9 = mirror of Cover 6 | VERIFIED | Operation Sports (Becotte), Aug 14 2024: "Cover 9 is ... Cover 6 but flipped" | New fn `madden9`; text adds "quarters on one side and Cover 2 on the other, flipped" |
| Cover 5 = 2-Man "in most systems"; through Cover 4 the number counts the deep defenders | VERIFIED (common usage) | Standard coaching vocabulary; consistent with Soran and Alexander | None |
| NGS split-safety 32.9% (2018) → 42.0% (2025); 2025 Cover 4 17.2%, Cover 2 13.9%, Cover 6 9.2% | VERIFIED | FACTS-current §10 (NFL.com NGS article) | None |
| nflverse COVER_9 only from 2023, undefined in dictionary; 1.5–2.5% a season | VERIFIED | nflreadr participation dictionary; own recalculation: 2.1% / 1.6% / 2.5% (2023–25) | None |
| C1+C3 > half of labelled dropbacks in both periods | VERIFIED | Own recalc: NGS 2018–22 ~59%; FTN 2023–25 ~51.5% pooled (50.3, 54.2, 50.1) | None |
| FTN far more Cover 2, far fewer Cover 3 than NGS; FTN 2025 Cover 2 >20%, Cover 4 ~10% | VERIFIED | Own recalc: C2 NGS 12.6–14.1% vs FTN 15.4–22.9%; C3 30–34% vs 17.7–27.7%; 2025 C2 22.9%, C4 10.1% | None |
| Man share 28.8 / 41.2 / 48.3 / 30.8% (2022–25); label sets; ~90k and ~61k dropbacks | VERIFIED | FACTS-current §7; own recalc (89,689 and 60,666) | None |
| Carroll's step-kick; "step for patience, kick for position"; learned from Willie Brown early 1980s | VERIFIED (precision) | ESPN, Kapadia, Oct 8 2015 ("probably back in 1981 or '82", Brown as Raiders DB coach) | Footnote now quotes Carroll's own wording |
| NFL.com: "press man, Cover Three defense" | VERIFIED | Wesseling, NFL.com, published Jan 28 2015 (page metadata) | Date added to fn `wesseling` |
| 2013 Seahawks led league in points (231), yards (4,378), takeaways (39), first since 1985 Bears; SB XLVIII 43–8 | VERIFIED | Wikipedia 2013 Seahawks season (PFR 403 to automated fetch) | "Spot-check on PFR" note removed |
| Earl Thomas FS; Sherman and Maxwell in the outside thirds (2013) | VERIFIED | Wikipedia 2013 roster (Maxwell replaced the suspended Browner late in the season) | None |
| Dungy "1975 Pittsburgh Steelers playbook" quote; Bud Carson roots | VERIFIED | Wikipedia, Tampa 2 | None |
| 2002 Bucs first in yards allowed, won SB XXXVII | VERIFIED, CORRECTED (context) | Wikipedia 2002 Bucs season (first in total defense, points, INTs; 48–21 over Oakland). The Tampa 2 article cited only mentions 2005 for the yardage title | Footnote cites the 2002 season page; text now says 2002 was after Dungy left, under Gruden with Kiffin's defense |
| Dungy Bucs HC 1996–2001; Kiffin DC 1996–2008 | VERIFIED | Wikipedia, Tony Dungy; Monte Kiffin | Sources added to fn `tampa2` |
| Fangio named Eagles DC Jan 27 2024; 2024 Eagles 278.4 yd/g (1st), 17.8 pts/g (2nd) | VERIFIED | Wikipedia 2024 Eagles season | None |
| SB LIX Eagles 40–22, four-man rushes; Fangio still Eagles DC in 2026 | VERIFIED | FACTS-current §1 and §9 | None |
| Books: *Art of Smart Football* 2015, *Essential Smart Football* 2012, *Quiet Strength* 2007 | VERIFIED | Publisher records (and 01-04 fact-check) | None |

## Counts
VERIFIED 25 · CORRECTED 4 (Soran's role, contact-rule pocket condition/footnote, Fangio Cover 8 footnote, 2002 Bucs context/source) · SOFTENED 0 · REMOVED 0. Precision tweak to the step-kick footnote counted under VERIFIED.

## Still uncertain / for a human
- The rulebook page on operations.nfl.com shows the penalty table (8-4-3) but not the full Rule 8-4 text to an automated fetch; the rule wording is cited from the Eagles' 2014 explainer, which quotes it.
- Pro Football Reference returned 403, so team-season stats rest on Wikipedia (which cites PFR).
