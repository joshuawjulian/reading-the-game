# Fact-check: 08-01 What Beats What (Concepts Versus Coverages)

Checked 2026-10-07. Afterwards `build_pdfs.py 08-01-concepts-versus-coverages` built cleanly, both the PDF and the `--html` build. All 5 `<!-- VERIFY -->` comments are resolved and removed. Each of the 10 footnotes is referenced exactly once. One footnote is new: `[^patternmatch]`. The 1978 footnote was re-sourced.

| Claim | Verdict | Source | Change |
|---|---|---|---|
| SB LVII (Feb 12, 2023): the Eagles played a lot of man coverage; two 4th-quarter TDs on return motion, Toney's the go-ahead score and Moore's the next | VERIFIED | Jones, CBS Sports, Feb 13 2023 (KC trailed 27–21; Moore scored less than three minutes later) | Footnote now states these details |
| Moore quote: "As soon as I went in motion and I saw him come in motion with me, I knew I had him" | VERIFIED (verbatim) | Jones, CBS Sports | none |
| "Andy Reid's name for the play was 'Corn Dog'" (the sentence followed both TDs) | CORRECTED | DeArdo, CBS Sports, Feb 13 2023: Reid gave the name for Toney's TD | Now "Reid's name for Toney's play"; the footnote adds author DeArdo and the full title |
| Toney 5-yd and Moore 4-yd TDs (VERIFY) | n/a | — | The distances are not in the text, so the comment was removed |
| SB LVIII (Feb 11, 2024), OT: same motion, from the 3; "Tom and Jerry"; Reid: "We built corn dog in saying, for sure they'll cover corn dog"; shovel to McKinnon was the first option; 49ers "converged on the shovel", man outside; Hardman TD | VERIFIED | Owens, Yahoo Sports, Feb 13 2024 (quote verbatim); Wikipedia "Tom and Jerry (American football)" (1st-and-goal at the SF 3, 3-yd TD, shovel to McKinnon was the designed primary option) | Text now says "on first-and-goal from the 3-yard line"; footnote updated |
| Chiefs 25, 49ers 22 (OT) | VERIFIED | FACTS-current §1 | none |
| Seahawks 54.8% split-safety from Week 14 (Love's return) through SB LX, the highest of any playoff team; 46% in the 9 games Love missed; 8–0, 15.1 ppg | VERIFIED | NGS Analytics Team, NFL.com (fetched; quotes in footnote) | none |
| League 29.0% first-down rate vs split-safety in 2025, "tied for the lowest rate since NGS began tracking in 2018" | CORRECTED (wording) | Same article: "tied for the lowest mark since at least 2018" | Now "since at least 2018" |
| Author and date of the NGS Seahawks article (VERIFY) | CORRECTED | The NFL.com page is bylined "Next Gen Stats Analytics Team" and shows no date | Byline changed from James Reber to the NGS Analytics Team; date given as "2026, after Super Bowl LX; the page carries no date" |
| 2025: fewer than 3 WR on 41.7% of plays; first season at or above 38% since NGS began in 2016 | VERIFIED | NGS Analytics Team, NFL.com, heavy-personnel article (verbatim quote added to footnote) | Byline changed to the NGS Analytics Team, as for the Seahawks article |
| Stafford 2025 MVP, league-leading 46 TD passes | VERIFIED | FACTS-current §2; NFL.com honors list | none |
| Stafford vs two-high, 2025: 249 dropbacks, +0.26 EPA, 3rd of 25 (min 150), league +0.02 | VERIFIED (computed inline) | nflverse pbp + participation (FTN 2025) | none |
| Route x coverage heatmap, 2018–2022: 63,058 targets, mean 52%, best cell 63%, worst 28%, "most cells within ten points" | VERIFIED (computed) | nflverse; re-ran the chapter code: 46 of 56 cells (n ≥ 100) within 10 points | none |
| "Go routes do best against Cover 2 (43%) and worst against quarters (31%)" | CORRECTED | Same computation: GO vs Cover 0 = 28%, lower than quarters | Added "(only Cover 0, at 28%, is lower)" as inline Python |
| Hitch vs Cover 2 63%, vs 2-Man 38%; corner vs Cover 1 40%; best matchups fail more than a third of the time | VERIFIED (computed) | Same | none |
| Prose against the matrix: "What Cover 3 does well shows up as orange in its column" | CORRECTED | The chapter's own GRADES array: the Cover 3 column has no negative cell | Reworded: Cover 3's strength "hides inside its column, which has no orange because the grid grades whole concepts" |
| "2-Man ... the orange row of the matrix" | CORRECTED | 2-Man is a column in the matrix | Now "the most orange column" |
| Dagger, scissors and yankee "grade orange against both Cover 0 and fire zones" | CORRECTED | GRADES: yankee vs Cover 0 = 0 (grey) | Now: dagger and scissors are orange against both, yankee against fire zones |
| Expected-value table (tbl-ev) and the Predict-3 arithmetic | VERIFIED | Recomputed every expected grade and worst case; all grades match the matrix | none |
| Gillman: Rams HC 1955–59, AFL Chargers 1960s (1960–69, plus 1971); HOF Class of 1983 | VERIFIED | PFHOF bio (URL slug `/players/sid-gillman/` is live); Wikipedia | Footnote adds the years |
| Gillman credited with film study and with stretching the field vertically and horizontally | VERIFIED (as "usually credited") | Wikipedia (newsreel film study; "the length and width of the field", Al Davis) | none |
| "Bill Walsh, who coached under Gillman's influence" | CORRECTED (ambiguous) | Wikipedia: Walsh said "much of what he did derived from Gillman" but never served on Gillman's staff | Now "who said that much of what he did derived from Gillman"; footnote explains the indirect lineage |
| 1978: defenders may contact receivers only within 5 yards (VERIFY: wording on the NFL Operations page) | VERIFIED; source replaced | PFHOF 1978 chronology (quoted). The operations.nfl.com page returned no rule entries when fetched | Footnote re-sourced to PFHOF with the quote, matching the already-checked 04-02 and 11-02 |
| Four verticals a staple of the run-and-shoot and BYU by the 1980s; pattern-matching Cover 3 traced to Saban and Belichick in Cleveland in the early 1990s | VERIFIED / SOFTENED (causation) | Soran, Throw Deep (Feb 24 2021), as already checked in 06-03; Saban was Browns DC 1991–94 | "associated with" changed to "usually traced to"; new `[^patternmatch]` notes that the causal story is the usual coaching account |
| Jet Chip Wasp on 3rd-and-15 in SB LIV; XLIX interception on a rub concept | VERIFIED | Well documented; covered in 12-04 and 12-02 | none |
| ~600 dropbacks per team season | VERIFIED (order of magnitude) | nflverse: teams average roughly 600–650 dropbacks | none |
| Go deeper: Brown, *Essential Smart Football* (2012) and *Art of Smart Football* (2015); Cody Alexander, *Match Quarters* and the MatchQuarters newsletter; Ted Nguyen at The Athletic; Emory Wilhite's newsletter | VERIFIED | Publisher records; matchquarters.com; The Athletic staff page and 2026 activity; emorywilhite.substack.com ("Fundamental Football") | none |
| Football-technical content (coverage rules, keys, look-off mechanics, Palms, Cover 3 match, alerts) | VERIFIED (standard coaching usage; consistent with Parts 4 and 6) | Parts 4 and 6 of this book (already fact-checked); Brown; Alexander | none |
| "Look-off costs perhaps three to five tenths of a second" | VERIFIED as hedged estimate | Coaching estimate, given as "perhaps" | none |

**Counts:** VERIFIED 19 (including 4 computed or arithmetic checks), CORRECTED 9, SOFTENED 1 (the pattern-match causation), REMOVED 0. One VERIFY comment, on the TD distances, needed no change.

**Uncertain:** the two NGS NFL.com articles show no publication date. Both are from early 2026, around Super Bowl LX. The NFL Operations "Evolution of the rules" page could not be read automatically, so the 1978 rule is cited to PFHOF instead.
