# Fact-check: 01-05 The Pre-Snap Phase

Checked 2026-10-06 against FACTS-current.md, the 2026 NFL rulebook text (operations.nfl.com PDF), nflverse play-by-play (recomputed in the `rtg` container, 2016–2025 REG) and web sources.
Both `<!-- VERIFY -->` comments are resolved and removed. Every footnote is referenced exactly once. The chapter builds (`build_pdfs.py 01-05-the-pre-snap-phase --html`: OK).

| Claim | Verdict | Source | Change |
|---|---|---|---|
| Radio cut-off at :15 on the play clock | VERIFIED | 01-04 factcheck (Boston Globe 2017; ESPN 2007) | None |
| "Most huddling offenses spend about ten of those seconds at the line" | REMOVED (specific) | No source | Now "spends most of what is left of the play clock at the line" |
| One-second set for all eleven (7-4-6); interior lineman in a 3-point stance may not move (7-4-2 Item 1) | VERIFIED | 2026 Rulebook R7 S4 | None |
| Shift definition includes the walk to the line (3-30); unlimited shifts, 1-second set after the last; illegal shift 5 yds (7-4-7) | VERIFIED | Rulebook 3-30, 7-4-7 | None |
| Motion: one backfield player, parallel/away; receiver on line sliding must stop; sequential motion legal if the first man stops (7-4-7, 7-4-8) | VERIFIED | Rulebook 7-4-7, 7-4-8 | None |
| A receiver on the line stepping forward after the set is a false start | VERIFIED | Rulebook 7-4-2 Item 2 | None |
| QB obvious attempt to draw offside = false start (Item 5); shotgun hand thrust (Item 4) | VERIFIED | Rulebook 7-4-2 | None |
| Defensive abrupt movements = delay of game (4-6-5-d); disconcerting words = 15-yd UNS (12-3-1-i) | VERIFIED | Rulebook 4-6-5-d, 12-3-1-i and its penalty line | None |
| Neutral zone definition; only the snapper may be in it; encroachment/NZI dead-ball (whistle), offside live | VERIFIED | Rulebook 3-18-2, 3-18-3, 3-19, 7-4-3 to 7-4-5 | None |
| NZI: free path to QB/kicker or nearby player reacts; flinching player not penalized | VERIFIED | Rulebook 7-4-4(a),(b) | None |
| Illegal shift after the two-minute warning with clock running → false start; 10-second runoff possible | VERIFIED | Rulebook 7-4-2 Item 6; 4-7-1 Item 1 (runoff after the two-minute warning) | None |
| Rockne's Notre Dame shift (T then box at the snap) was the famous/targeted version (VERIFY comment) | VERIFIED (with added primary source) | *Notre Dame Alumnus* Oct 1927 (Starrett: ND "hit hardest of all"; Rockne's own column on the one-second stop); Packers.com (Christl); Wikipedia (Stagg → Harper → Rockne) | Sentence added on the alumni magazine; new fn `ndalumnus`; fn `rockne` now quotes Christl and the lineage |
| 1927 rules report: one-second stop, penalty 5 → 15 yards, "most serious" problem | VERIFIED | Dartmouth Alumni Magazine, Feb 1928 | None |
| "Shaughnessy's version of the T with man in motion"; Bears 73–0, Dec 8 1940 | CORRECTED (attribution) | PFHOF 1940 chronology; Lake Forest College HoF (Ralph Jones introduced man-in-motion with the Bears, 1930–32) | Now "Halas's Bears, with extra coaching from Shaughnessy"; fn notes Jones's earlier role |
| T with man in motion "spread through football within a decade" | CORRECTED | Wikipedia "T formation" (Steelers last single-wing NFL team, converted 1953) | Now "by 1953 … every NFL team ran it" |
| Britannica URL (VERIFY comment) | REMOVED | Britannica returns 403 | Replaced with PFHOF and Wikipedia |
| PFF shift/motion 38.4% (2016) → 63.9% (2025); all but Giants ≥50% | VERIFIED | FACTS-current §10 (PFF, Feb 23 2026) | None |
| Illegal shift/motion "about once every eight to ten games" per team | CORRECTED | Own calc: 0.055–0.143 per team-game = once every 7.0–18.3 games, mean ≈ 1 in 12 | Now "about once every dozen games (anywhere from once in 7 to once in 18)" |
| False starts ≈ 1 per team-game (0.97–1.25); rose 2024–25; defensive jumps fell (0.65 → 0.46) | VERIFIED | Own calc | None |
| Situational figure caption: defenses jump / offenses false start "about twice as often" on 3rd and 4th-and-short | CORRECTED | Own calc per 100 snaps: jumps 0.64 (1st/2nd) vs 0.91/1.27/1.26; FS 1.29 vs 1.93/2.24/2.38 | Now "1.4 to 2 times" and "1.5 to 1.8 times"; "offense commits more in every situation" verified |
| Home vs road false starts 2,969 / 2,886; within ~1.6 per 1,000 snaps every season | CORRECTED (home total) | Own calc: 2,929 home, 2,886 road; max gap 1.56 | fn `homeroad` now 2,929 |
| Eagles 121 home / 84 road; home > road in 8 of 10 seasons; 2020 an exception | VERIFIED | Own calc (exceptions 2020 and 2021) | None |
| Romo silent count vs Houston, Oct 5 2014; Martin taps Frederick | VERIFIED | AP via ABC7 | None |
| Inquirer Dec 28 2023: 15 of 22 false starts at home; Mailata quotes; Hurts quote | VERIFIED | Inquirer (Marcus Hayes); nflverse full season 15/8 | None |
| "No quarterback of his era was more associated with the hard count than Rodgers" | SOFTENED | Opinion | Now "Few quarterbacks of his era …" |
| Rodgers: 12 regular-season free-play TD passes since 2008, 3× any other QB, 30.8 avg | VERIFIED | ESPN, Demovsky, Sep 14 2017 (Flacco next with 4) | fn expanded with the definition of a free play |
| "It's one word … we all line up and know what to do" attributed to Rodgers | CORRECTED | Same ESPN article: Jordy Nelson said it | Attribution changed to Nelson |
| Receivers recognise the flag when a defender jumps at the snap (no time for a code) | SOFTENED | Not in source; logical inference | Now a parenthetical inference, not attributed |
| Rodgers 2020 "predicted" quiet stadiums would help hard counts | CORRECTED (framing) | Packers.com, Sep 28 2020 ("I feel like it was going to be an advantage …", said after Week 3 about his camp expectation) | Now "said he had expected"; quote trimmed with an ellipsis (the original has "with who") |
| GB 2016–22 drew 0.43 defensive jumps/game vs league 0.61 (below median) | VERIFIED | Own calc (median team 0.63) | None |
| Kill call definition | VERIFIED | ITP/Scouting Academy glossary | None |
| Kill call "the most common of these in today's NFL" | SOFTENED | No source | Now "a staple of today's NFL" |
| Kill call "halves the chance" of the wrong play | SOFTENED | Unsupported number | Now "sharply cuts the chance" |
| Ditka 2004 quote on Manning's check-with-me | VERIFIED | AP via Spokesman-Review, Oct 3 2004 | None |
| Purdy 2024 quote "we usually have an answer built into the play" | CORRECTED (misquote) | SI, Grant Cohn, Oct 25 2024: "Usually, we just have an answer built into the play" | Quote fixed; second quote verified as is |
| Manning's "Omaha" "partly theatre, and the theatre was the point" | CORRECTED | 01-04 fns (theScore: a real call meaning the play changed and the snap was coming) | Now: a real call, and his joking public explanation did a dummy call's job |
| Kirwan *Take Your Eye Off the Ball* 2010, 2.0 edition 2015; Brown *Art of Smart Football* 2015 | VERIFIED | Triumph Books / pigskinbooks; known publication | None |
| Rule 7-4 "two pages that cover every rule in this chapter" | CORRECTED | 4-6-5-d and 12-3-1-i sit elsewhere | Now "nearly every rule" |
| NFL+ Premium includes All-22 | VERIFIED | NFL.com, Aug 2024 (NFL Pro in NFL+ Premium) | None |
