# Fact-check log: 15-01 Watching Live

Checked 2026-10-08 against FACTS-current.md, web sources, and nflverse data (pbp, participation, FTN charting, schedules) re-queried in the `rtg` container by running the chapter's own data cells and dumping every drive row. All 3 `<!-- VERIFY -->` comments are resolved and removed. Each footnote is referenced exactly once (script check). Build `build_pdfs.py 15-01-watching-live --html`: OK (25 pages).

| Claim | Verdict | Source | Change |
|---|---|---|---|
| Play clock 40 s from the end of the play; 25 s after certain stoppages | VERIFIED | operations.nfl.com Football Terms glossary (fetched); Rule 4-6-1/4-6-2 (08-04 fact-check) | none |
| Helmet radio cut off at :15 on the play clock (Rule 5-3-3) | VERIFIED | 01-05 / 01-04 fact-checks; 2026 rulebook wording quoted in 01-05 | none |
| Huddling offense spends "ten to fifteen seconds" at the line; tempo "five" (VERIFY 1) | REMOVED (specific) | No source; nflverse `play_clock` empty for 2025; 01-05 removed the same kind of claim | Now "spends most of what is left of the play clock at the line; a team in tempo can snap within a few seconds of setting". Clock figure already captioned as typical/illustrative |
| 2025 pass-rate landmarks (all 60%, 1st&10 50%, 2nd&1–2 31%, 3rd&1–2 UC 19% / gun 52%, 3rd&7–10 94%, no-huddle 70%) | VERIFIED | Chapter code re-run (nflverse + FTN, 2025 REG) | none |
| No-huddle: "mostly two-minute and catch-up football" | CORRECTED | Re-query: of 3,212 no-huddle snaps, 68% trailing but only 18% in the last 2 minutes of a half | "Mostly offenses that are behind; under one in five comes in a two-minute drill" |
| Under center pass rate 31%, "most of those were play-action" | VERIFIED | Re-query: 82% of 2025 under-center dropbacks were play-action | none |
| Gun 79% / pistol 29% / UC 31% pass; empty 95% | VERIFIED | Chapter code re-run | none |
| PFF shift/motion 63.9% in 2025, series high, all but Giants ≥ 50% | VERIFIED | FACTS-current §10; PFF URL resolves | none |
| NGS two-high 42.0% in 2025 (32.9% in 2018), highest since 2018 | VERIFIED | FACTS-current §10; NFL.com URL resolves | none |
| Model accuracies: always-pass 60.1%, situation 69.5%, +personnel 69.9%, +formation 75.2%, +box 75.5%; 32,813 test snaps; personnel ≈ +0.5 pt; motion/tempo/box ≈ +0.3 pt | VERIFIED | Chapter code re-run | none |
| nflverse `xpass` calls 71% of the same snaps | VERIFIED | Re-query: 70.9% on the 32,813 snaps | none |
| Confidence bands: ~1 in 5 snaps at 90%+; "75% calls right three in four; 95% calls right 95 in 100"; "calls come true at about the rate they claim" | CORRECTED (precision) | Re-run: 90%+ band = 19.7% of snaps, right 94.1%; 70–80% band (mean conf 75%) right 71.4%; every band 2–4 pts under its claimed confidence | Text now prints the band accuracies inline (`BANDS[2]`, `BANDS[4]`); caption says calls come true "two to four points less often" than claimed |
| Rush 5+ on 26.8% of dropbacks (38.5% on 3rd&7–10, 27.3% on 3rd&4–6); zone ≈ 69% of 2025 charted dropbacks; FTN man share 28.8/41.2/48.3/30.8% | VERIFIED | Chapter code re-run; FACTS-current §7 | none |
| Rams 2025 under-center passing as "textbook bait" | VERIFIED | 12-03 and 13-04 data (Rams first in under-center and play-action rate, 2025) | none |
| NFC Championship: Rams at Seahawks, Jan 25, 2026, Lumen Field, SEA 31–27; SEA 14–3 No. 1 seed; SB LX SEA 29–13 Feb 8, 2026 | VERIFIED | nflverse schedules (gameday 2026-01-25, Lumen Field, 31–27); FACTS-current §1–2 | none |
| SEA 2025 staff: Macdonald HC, Kubiak OC, Durde DC; 2026 Kubiak to LV, Fleury SEA OC | VERIFIED | FACTS-current §1, §9 | none |
| Darnold SEA 2025 QB; Kupp from Rams to SEA before 2025 (VERIFY 2) | VERIFIED | SI (Kupp released by LAR, signed Mar 14, 2025, 3 yr/$45M; Darnold signed Mar 13, 2025); pbp names | Source and dates added to `[^staff]` |
| Drive context: SEA up 24–13 early Q3 (12:07 TD); Rams TD at 9:45 → 24–20; touchback to SEA 35; 65 yards, 9 snaps; TD on 3rd&3 from LA 13, 13-yd pass to Kupp; 31–20 with 4:52 left | VERIFIED | nflverse pbp, game 2025_21_LA_SEA, Q3 | none |
| Hook: Q3 8:23, 3rd&9 at SEA 36, 11 personnel gun, Rams in dime with 5 in the box, after a −2 run | VERIFIED | pbp/participation/FTN play 2594 | none |
| "Three different personnel groups" (12, 11, 13); base, nickel and dime | VERIFIED | participation | none |
| "Four different coverage labels" | CORRECTED | participation: COVER_9, COVER_3 (×4), COVER_6 only | "three different coverage labels" |
| Snap 1: 12 pers, UC, 1 back, motion, base, box 7; Holani RG +3 | VERIFIED | drive rows | none |
| Snap 2: 12 pers, UC, 2 backs, motion; nickel, box 6; Walker RE −2; "both tight ends near the ball, one an H-back" | SOFTENED | FTN gives 2 backs, personnel 1 RB/2 TE; who the second back was isn't charted | "a second player in the backfield (… most likely a tight end as an H-back)" |
| Snap 3: dime, box 5, 4 rushers, COVER_9 zone, 2.8 s, CHK, 6 air + 6 YAC, quick out to Kupp, +12 | VERIFIED | drive rows | "rather than his first read" dropped (see read codes) |
| Snap 4: 13 pers (1 WR), UC, 2 backs, motion; base with 2 NT, box 7; Walker RG +11 | VERIFIED | drive rows | none |
| Snap 5: empty, 11 pers; 4 rush, Cover 3; CHK to Holani, shallow cross, +9 | VERIFIED | drive rows | "out of the backfield" → "outside the backfield" (clarity) |
| Snap 6: 2nd&1 LA 32, gun 11 motion, nickel box 6; 5 rushers (1 blitzer), Cover 3; screen to Smith-Njigba, 0.7 s, air −4, YAC 16, +12; 2nd&1–2 gun-11 pass rate 57% | VERIFIED | drive rows; chapter code | none |
| Snap 7: 12 pers UC 2 backs motion, base box 7; play-action, out of pocket, 4.7 s, Barner short left +7 | VERIFIED | drive rows | none |
| Snap 8: 2nd&3 LA 13, no-huddle, UC 1 back; 5 rushers, Cover 3; 0.6 s, incomplete to Bobo | VERIFIED | drive rows | none |
| Snap 9: 3rd&3 LA 13, gun 11 motion, nickel box 6; 4 rush with pressure; Cover 6; 2.4 s; post, 7 air + 6 YAC, TD | VERIFIED | drive rows | none |
| Snap 9 thrown "to his first read" | SOFTENED | FTN code is "1". nflverse dictionary says 0 = first read, 1 = second; but in the 2025 file "0" is on almost every run and ~2% of passes, "1" on over half of passes, so "1" looks like the primary read in practice | Text: "to a receiver in his progression rather than a checkdown"; snap 9 caption likewise; `[^read]` explains the conflict |
| `read_thrown` code meanings (VERIFY 3) | CORRECTED | nflverse FTN dictionary (fetched raw): 0/1/2 reads, CHK checkdown, DES designed (screens, RPOs), SD scramble drill | `[^read]` rewritten with the dictionary's codes, the data check, and which drive snaps carry which code |
| Drive score: run/pass 6 of 9; coverage 4 of 6; rush 5 of 6; both coverage misses in the red zone; rush miss = 2nd&1 blitz | VERIFIED | chapter code re-run | none |
| Motion: tempo offenses use less of it | VERIFIED | Re-query: motion on 22% of no-huddle snaps vs 59% of huddled snaps (2025) | none |
| 2026 BDB used the 2023 regular season; no public tracking for the 2025 playoffs; `bdb.load_tracking` / `bdb.prepare(trk, plays, game_id, play_id)` signature | VERIFIED | FACTS-current §8; gridiron/bdb.py | none |
| Gawande, *The Checklist Manifesto* (Metropolitan, 2009); do-confirm vs read-do | VERIFIED | book (standard citation) | none |
| Tetlock & Gardner, *Superforecasting* (Crown, 2015); fine-grained numeric probabilities linked to accuracy | VERIFIED | book; Friedman, Baker, Mellers, Tetlock & Zeckhauser (2018) on the value of precision | none |
| Chris B. Brown, *The Art of Smart Football* (2015); Ted Nguyen at The Athletic; Cody Alexander's MatchQuarters | VERIFIED | standard citations; Ted Nguyen listed as The Athletic NFL writer in 2026 | none |
| Glossary links gl-brier-score, gl-calibration point to the unwritten 15-02 | NOTED | — | Leave in place; 15-02 must define both terms |
