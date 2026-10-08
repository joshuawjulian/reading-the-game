# Fact-check: 10-03 Red Zone, Goal Line, Two-Point Plays, and Short Yardage

Checked 2026-10-08 against FACTS-current.md, the 2026 NFL rulebook text (operations.nfl.com), nflverse play-by-play / FTN charting / participation (recomputed in the `rtg` container) and web sources.
All 10 `<!-- VERIFY -->` comments are resolved and removed. The chapter builds (`build_pdfs.py 10-03-red-zone-goal-line-and-short-yardage`: OK, 22 pages). Every footnote is referenced exactly once.

| Claim | Verdict | Source | Change |
|---|---|---|---|
| End zone 10 yd deep; red zone = last 20; 30/20/12 yd from the 20/10/2 to the end line | VERIFIED | Rulebook geometry | None |
| Two-high 44% outside the RZ vs 19% inside the 5 (FTN 2023–25) | VERIFIED | Recomputed (same code) | None |
| 06-02: "roughly four in five" dropbacks inside the 5 are man; Cover 0 the most common call there | VERIFIED | 06-02 fn `manshare`: man 87.8% (NGS) / 77.6% (FTN); Cover 0 61.5% / 41.4% | None |
| 8,603 RZ drives; 60% TD, 26% FG | VERIFIED | Recomputed: 59.5% / 25.5% | None |
| fn `rz`: the remainder = turnovers 4%, downs 4%, missed FG and end of half 1.5% each | CORRECTED | Recomputed: also "Opp touchdown" 3.1% and punts 0.4% were missing | Footnote lists all categories |
| First-and-goal TD rate: 90% from the 1, under 60% from the 10; +3 pts/yd from 10 to 5, +8 from 2 to 1 | VERIFIED | Recomputed: 90.4%, 58.1%; (74.0-58.1)/5 = 3.2; 90.4-82.7 = 7.7 | None |
| Neutral pass rate 55% at the 11–20 "about the same as anywhere else on the field" | CORRECTED | Recomputed: 54.7% vs 59.1% at 21+ | Now "a little below the [59%] everywhere farther out" (inline computed) |
| From the 1: dropbacks 52%, runs 55%, sneaks 67% TD | VERIFIED | Recomputed (n = 371 / 848 / 184) | None |
| End-zone outside throws 40% complete vs 68% short of goal line | VERIFIED | Inline computed | None |
| Packers HOF: back-shoulder "began as a red-zone play", used all over the field; Nelson 6-3 | VERIFIED (quote fixed) | packers.com HOF profile: "The origin of the back-shoulder pass was as a red-zone play"; "anywhere on the field" | Footnote now quotes the exact wording |
| ESPN blog author/date; Nelson: throw is a reaction, no signal | VERIFIED | Rob Demovsky, ESPN, Oct 23, 2014: "For us, it's a complete reaction"; "it's not a play" | Date and quotes added to fn `bs` |
| Shovel: linemen may block downfield because the rule only applies to passes that cross the line | CORRECTED | 2026 Rulebook 8-3-1 (applies to any legal forward pass; 1 yd; exception only while engaged); NCAA (3 yd, exception for passes caught behind the line) per Wikipedia "Ineligible receiver downfield" | Paragraph rewritten (NFL has no behind-the-line exception; the flip comes before linemen release); new fn `ineligible` |
| Shovel dropped = incomplete pass, not fumble | VERIFIED | Forward-pass rules (Rule 8-1) | None |
| Super Bowl XLIX: Feb 1 2015, Glendale; NE 28–24; 2nd-and-goal at the 1, ~26 s, one timeout; Kearse pick route, Lockette slant, Browner jam, rookie Butler INT | VERIFIED | nflverse pbp 2014_21 (0:26, 2nd-and-1 at NE 1, SEA 1 timeout, "pass short right intended for R.Lockette INTERCEPTED by M.Butler"); NBC Sports Boston; Wikipedia | Footnote cites pbp for clock/timeout |
| Kelce 2017 shovel TD was the go-ahead score in KC's 27–20 win | VERIFIED | PFR box score; nflverse (6:32 Q4, 2nd down at PHI 15, 13–13 → 19–13); AP | Footnote now cites PFR and the tie; Inquirer live-blog link dropped |
| NFL adopted 2-pt in 1994 from college (try at the 3) and the AFL | VERIFIED | PFHOF (AFL 1960–69; NFL 1994; Tupa); Wikipedia (pro 2, amateur 3) | Fn `twopt`: "line at the 2" no longer attributed to PFHOF (it doesn't say so); Wikipedia added. AFL spot not stated in text, so not needed |
| 2015: XP snap moved to the 15 (33-yd kick); defense can score 2 on a failed try | VERIFIED | CBS Sports (cited) | None |
| Two-point: 47% of 1,297 (2015–25), runs 55%, passes 44%, 73% passes | VERIFIED | Recomputed (run 54.8% n=356; pass 44.2% n=941) | None |
| Super Bowl LI: 28–3 in Q3; Amendola TD 28–18 (5:56), White direct-snap 2-pt; White 1-yd TD, Brady–Amendola 2-pt 28–28; 34–28 OT | VERIFIED / CORRECTED (precision) | nflverse pbp 2016_21 (2-pt at 5:56 and 0:57; White TD snapped at 1:00); Press Herald; ESPN; Concord Monitor ("Ride 34 Direct") | "58 seconds" → "57 seconds"; alignment added (Brady in shotgun, White motions beside him, direct snap up the middle); fn `li` expanded |
| Perry: rookie DT, 1-yd TD in Super Bowl XX (Jan 26 1986), third quarter | VERIFIED | Wikipedia; NFL.com 100 Greatest Plays (#79); Patriots.com (37–3 → 44–3, late Q3) | Footnote adds 44–3 and NFL.com |
| 6-2 / 5-3 personnel definitions; "low man wins" | VERIFIED | Standard coaching usage | None |
| Brady 6-4; 187 carries on ≤1 to go, 86% | VERIFIED | Recomputed (86.1%; seasons 2001–2022) | None |
| Patriots "went on the first sound" | SOFTENED | No source for the specific cadence | Now "often ran it on a quick count" |
| Pushing the runner was illegal; 10-yard foul | VERIFIED | Deseret News 2023 / Acme Packing Co. 2025 (via search; Acme 403); current 12-1-4 penalty 10 yd | None |
| Pushing legalized in 2005 | SOFTENED | 2005: Deseret News, most coverage, Goodell's "pre-2005 rule"; ESPN (Seifert) gives both 2004 and 2005. 2006: NFL historian Joel Bussert (Packers.com, May 1 2025), Dean Blandino (Fox), New Yorker ("the next year" after Oct 2005) | Text now says "mid-2000s ... Most coverage says 2005, but the league's historian ... and Blandino date the rulebook change to 2006"; glossary, description, objective and takeaway changed to "mid-2000s (2005 or 2006)"; "almost two decades" → "more than 15 years" |
| Pereira: pushing "really too difficult to officiate" | VERIFIED (quote fixed) | Boston Globe (Ben Volin): "So it became really too difficult to officiate" (said in 2022) | Quote extended to "became really too difficult"; author/title/year added |
| Current rule citation | VERIFIED | 2026 Rulebook 12-1-4 "Assisting the runner and interlocking interference": no player may "pull a runner in any direction at any time"; 10 yd | Fn `push2005` quotes it |
| NCAA removed "push" in 2013 | VERIFIED | ESPN (Bonagura, Oct 15 2025) | Fn `ncaa` now cites ESPN instead of Acme |
| Bush Push: Oct 15 2005, USC 34–31 at Notre Dame; illegal under college rules, no flag | VERIFIED | ESPN (Bonagura): title is "The legacy and legality of the Bush Push 20 years later"; USC trailed 31–28 with 7 s left | Footnote title corrected |
| Eagles push 2022–25: 51% of 1-to-go snaps vs league median 14%; Hurts 83% of 179 | VERIFIED | Recomputed | None |
| Jason Kelce retired after 2023; Lane Johnson RT; Stoutland OL coach | VERIFIED | Common record; FACTS §9 (Stoutland left after 2025) | Added "(with the Eagles through 2025)" |
| Hurts scored Super Bowl LIX's first TD on a tush push; Eagles 40–22 | VERIFIED | FACTS §1; CBS News | None |
| 2025 Packers proposal: banning "any pushing, pulling, lifting or grasping"; tabled; revised version failed 22–10 on May 21 | CORRECTED (precision) | ESPN (Seifert, Apr 1 2025): first version barred "immediately pushing a teammate who is lined up directly behind the snapper"; SI: revision barred "pushing, pulling, lifting, or assisting the runner except by individually blocking opponents"; 22–10 (FACTS §5) | Text distinguishes the narrow first version from the broader revision; fn `ban` quotes both |
| Officiating guidance tightened (false starts, alignment); no 2026 proposal; McKay; Vincent "lightly"; legal for 2026 | VERIFIED | FACTS §5; NFL.com; Washington Times | None |
| Going over the pile is legal; leaping restriction applies to kicks | VERIFIED | 2026 Rulebook 12-3-1(r) (FG/Try kick only); no hurdling foul in current book | New fn `leap` |
| Sneaks on 1 to go 81% (n=1,089), other runs 70%, passes 58%; 2 to go 54% of 37 | VERIFIED | Recomputed | None |
| Bills second-most sneaks; KC charted with 1 | VERIFIED | Recomputed: PHI 140, BUF 80, SF 63; KC 1 | None |
| Allen 86% of 181, "a hair better than Brady's career mark" | CORRECTED | Recomputed: Allen 85.6% vs Brady 86.1% | Now "essentially level with Brady's career mark" |
| By-season sneak rates 85/80/83/78% | VERIFIED | Inline computed | None |
| BDB 2025 release = 2022 weeks 1–9, pre- and post-snap frames | VERIFIED | Consistent with 06-06 fact-check (Kaggle; arXiv:2502.16313) | None |

**Counts:** VERIFIED 28 · CORRECTED 7 (rz footnote, pass-rate comparison, ineligible-downfield rule, Super Bowl LI time, Allen vs Brady, Packers proposal wording, plus precision fixes to quotes/titles counted within VERIFIED rows) · SOFTENED 2 (2005 vs 2006 push-rule date; Patriots' "first sound") · REMOVED 0.

**Follow-up for FACTS-current.md §5:** the "removed in 2005" history line is marked LIKELY; the NFL's historian (Bussert) and Blandino say 2006. Suggest changing it to "mid-2000s (2005 per most coverage; 2006 per the league historian)". CURRICULUM 10-03 objective text also says "the 2005 push-the-runner rule change".
