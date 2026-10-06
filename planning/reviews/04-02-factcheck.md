# Fact-check: 04-02 Pass Protection

Checked 2026-10-06 against FACTS-current.md, the 2026 NFL Rulebook PDF (operations.nfl.com), nflverse data
(recomputed in the `rtg` container) and web sources. All 6 `<!-- VERIFY -->` comments are resolved and removed.
The chapter builds (`build_pdfs.py 04-02-pass-protection --html`: OK, 28 pages).

| Claim | Verdict | Source | Change |
|---|---|---|---|
| 2024–25 REG dropbacks: 4 rushers ~69%, 5 ~20%, 6+ ~7%, ≤3 ~4% | VERIFIED | Own recalculation, nflverse participation joined to pbp dropbacks: 69.0 / 19.9 / 6.7 / 4.4% | None |
| Sacks ~6–7 per 100 dropbacks | VERIFIED | Own calc 2024–25: 6.5% | None |
| Average time to throw "a little under three seconds"; 2.64 s (2016) → 2.84 s (2025) | VERIFIED | Computed in chapter from NGS | None |
| League sack rate "stayed in a narrow band"; QBs hold longer "without being sacked more often" | CORRECTED | Chapter's own computed values: 5.6% (2016) → 6.5% (2025), a rise | Now "within a point or so ... sacked only a little more often" |
| ~4–5 pressures per sack | VERIFIED | Chapter's computed FTN numbers: 30% pressure rate, 21% of pressures become sacks (1 in ~4.8) | None |
| Pressure flag: NGS 2016–2022, FTN 2023+ | VERIFIED (source fixed) | FACTS-current §7; nflverse-data release notes. The nflreadr participation dictionary itself does not state the split | Fn `pressure` now cites the release notes for the split |
| NGS time-to-throw definition (quote) | CORRECTED (wording) | nflreadr NGS dictionary: "Average time elapsed from the time of snap to throw on every pass attempt for a passer (sacks excluded)." | Quote in fn `ngs` made verbatim |
| Brady/Patriots changed Mike IDs and protections at the line; "the same pass play could be run with several protection calls" | SOFTENED / partly REMOVED | Edelman via Pewter Report, Sep 1 2022 ("Hey no, he's the Mike"); Boston Sports Journal (Cory Bailey), Nov 7 2018 | Patriots-specific claim about several protection calls per play removed (unsourced); now Brady overruling the Mike ID, sourced; new fn `brady` |
| Scat = back free-releases, five-man protection, QB hot; usage varies | VERIFIED | Matty F. Brown, SI, Jun 22 2022 ("200/300 Scat") | New fn `scat`; parenthetical generalised to "one numbered protection / a tag" |
| Holding: hands outside the frame + restricting = holding; officials told to watch hands outside; inside hands "the only place a hold is not likely to be called" | CORRECTED | 2026 Rulebook, Rule 12-1-2 (may contact on or outside the frame, must work immediately to get inside) and 12-1-3(c) (material restriction is holding "regardless of whether the blocker's hands are inside or outside the frame") | Text rewritten to match; fn `holding` quotes Art. 2 and 3(c). The old video-rulebook URL returned 404 and was removed |
| 1978: blockers allowed to extend arms and open hands; paired with receiver-contact limit | VERIFIED | Wikipedia "1978 NFL season" rule changes | None |
| SI "The Name of the Game Is Now Armball," Nov 19 1979 | VERIFIED (citation); URL dead | Search confirms title, date, author Paul Zimmerman; the vault URL returns 404 | Fn `1978-2` now a print citation with author, plus the 1978 rules source |
| Lawrence Taylor, Giants OLB from 1981 | VERIFIED | PFHOF; common record | None |
| Gibbs built one-back/two-TE and H-back sets partly to block Taylor | VERIFIED (attribution flagged as widely repeated) | PFHOF "Gold Jacket Spotlight: Lawrence Taylor created havoc" (2023) quotes Gibbs: "You get a back blocking Lawrence Taylor, you lose"; Michael Lewis, *The Blind Side* (2006) ch. 2 | Gibbs's words and Lewis added to fn `lt` |
| Garrett 23 sacks in 2025, single-season record | VERIFIED | FACTS-current; NFL.com | None |
| Bears 68 sacks in 2024, team record | VERIFIED | Windy City Gridiron Sackwatch 2024 (most in team history); nflverse computed 68 | Fn `bears`: unlinked *Bear Digest* cite replaced by WCG URL |
| Bears 2025: Johnson HC; Thuney traded from KC, Jackson from LAR, Dalman signed; 24 sacks "among the fewest" | VERIFIED / CORRECTED (precision) | chicagobears.com 2025 OL position review (24 sacks, third fewest) | "among the fewest" → "the third fewest" |
| Williams 3.19 s TTT in 2025, longest; 2.92 in 2024 | VERIFIED | Computed in chapter (NGS) | None |
| Burrow 2021: 51 sacks (league high) + 19 in playoffs | VERIFIED | Pro Football Rumors, Aug 2022 | None |
| 9 sacks in divisional round at Tennessee | VERIFIED | theScore, Jan 22 2022 (ties the playoff record) | Fn previously said "same CBS piece", which does not mention it; theScore added |
| 7 sacks in Super Bowl LVI tied the record | VERIFIED | CBS Sports | None |
| 2022 additions Karras, Cappa, Collins (FA), Volson (draft) | VERIFIED | Pro Football Rumors | None |
| Buffalo, Jan 22 2023: 27–10; "three linemen who had not started a game before late December"; Burrow sacked once | CORRECTED | Bengals.com (Carman's first NFL start; Scharping and Adeniji had started playoff games before; sacked once, hit three times); PFR roundup (Collins, Cappa, J. Williams out) | Now "three backups: Carman (first NFL start, LT), Scharping (RG), Adeniji (RT)"; Bengals.com added to fn `buffalo` |
| "Watch the protection that day ... help for the backup tackles, quick throws that made the rush irrelevant" | SOFTENED | No source describes the protection plan | Recast as what to look for on a rewatch |
| AFC Championship Jan 29 2023: KC 23–20, 5 sacks, 2 by Chris Jones incl. on the last possession | VERIFIED | AP via News4Jax, Jan 30 2023 | Detail tightened: Jones's second sack on 3rd down of CIN's last possession forced the punt |
| Karlaftis sack "beat a backup right tackle" | REMOVED (specific) | AP gives only that Karlaftis had the first sack, on the game's fifth play | Replaced with the AP detail |
| "With backups they kept more men in and threw faster" | REMOVED (unverified) | No source / not checkable in nflverse (blocker counts not charted) | Recast as a question for the viewer |
| Stoutland Eagles OL coach 2013–2025, 13 seasons, LII and LIX | VERIFIED | NFL.com; NBC Sports Philadelphia, Feb 4 2026 | NBC added to fn `stoutland`. **FACTS-current.md §9 says "14 seasons"; that is wrong (2013–2025 = 13)** |
| Stoutland "widely regarded as the best position coach in the league" | SOFTENED | Coverage calls him "revered", "one of the NFL's most revered" | Now "regarded as one of the best offensive line coaches in the league" |
| Center ran the line's communication (Kelce/Jurgens) | CORRECTED (precision) | Philadelphia Magazine 2013 (Kelce makes protection calls); NBC Sports Philadelphia, Jul 27 2024 (Kelce carried most calls; Jurgens and Hurts share them from 2024) | Text now says so; new fn `eaglescalls` |
| Johnson RT, Mailata LT, Kelce then Jurgens C | VERIFIED | Team rosters / coverage above | None |
| *The Art of Smart Football* (2015) | VERIFIED | Per 01-04 fact-check | None |
| *Finding the Winning Edge* (1998) "the West Coast offense's protection and hot-route thinking" | VERIFIED (book, year: 1997/98 per listings) / CORRECTED (description) | Sports Publishing; PigskinBooks review: a coaching/management blueprint | Description changed to game planning and staff thinking |
| Football-technical claims (slide, BOB, half-slide as foundation six-man protection, check-release, chip, kick slide, vertical/45/jump sets, T-E stunt, switch vs stay, inside-out rule) | VERIFIED (general) | Boston Sports Journal coach's view (Mike / 3x3 six-man protection as the base NFL protection); standard OL coaching material | None |

## Counts
VERIFIED 22 · CORRECTED 8 · SOFTENED 3 · REMOVED 2 (Karlaftis-vs-backup-RT detail; "kept more men in and threw faster"). The Brady row is counted as SOFTENED.

## Still uncertain / for a human
- FACTS-current.md §9 (Eagles row) says Stoutland "departed after 14 seasons"; NFL.com, NBC Sports Philadelphia, WFMZ and CBS all say 13 (2013–2025). The chapter uses 13; FACTS should be corrected.
- PFHOF Gold Jacket Spotlight URL appears in search results with the Gibbs quote but returned 404 to a direct fetch at check time; kept as cited.
- SI vault article (1979) has no working URL; cited in print form.
- "Two teams can hold the ball equally long and be sacked at rates three times apart" is read off the chapter's own scatter, not separately recomputed.
