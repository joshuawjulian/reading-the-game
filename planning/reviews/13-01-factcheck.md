# Fact-check: 13-01 Working with nflverse Data in Python

Checked 2026-10-08 against FACTS-current.md, nflverse data (every data claim recomputed in the `rtg` container, using the chapter's own filters), the installed nflreadpy 0.1.5 source, and web sources.
All 7 `<!-- VERIFY -->` comments are resolved and removed. The chapter builds (`build_pdfs.py 13-01-nflverse-in-python --html`: OK), and all the hidden assert cells pass, including two new ones (wp/vegas_wp, fourth-down footnote).

| Claim | Verdict | Source | Change |
|---|---|---|---|
| Raw pbp is the league's record: official stat crew's play descriptions, same text as the gamebook | VERIFIED (reworded) | nflfastR CRAN description ("NFL play-by-play data from nfl.com"); nflfastR README (JSON NFL pbp back to 1999, updated nightly) | Now "which nflfastR reads from the NFL's game-data feeds"; new fn `source`; VERIFY removed |
| nflscrapR by Horowitz, Yurko, Ventura (CMU) | VERIFIED | nflfastR README credits; nflWAR paper (JQAS 15(3), DOI 10.1515/jqas-2018-0010); 13-02 fact-check | None |
| nflscrapR fitted "the first widely used public" EP/WP models | SOFTENED | Public EP/WP models predate it (e.g. Advanced NFL Stats), but not open-source ones | "first widely used open-source" |
| "When the league changed its data feeds around 2020", Baldwin and Carl wrote nflfastR | REMOVED (cause) / VERIFIED (date, authors) | No source found for an API change prompting it; Baldwin tweet Apr 27, 2020 (embedded on The Mockup blog); CRAN archive: first release 2.2.1 on 2020-09-01; authors Carl and Baldwin | Now "In April 2020 Ben Baldwin and Sebastian Carl released nflfastR ... now reaches back to 1999"; dates added to fn `fastr` |
| When the "nflverse" name was adopted | REMOVED (date never printed) | No dated source found | Text keeps the undated "took the name nflverse" |
| ~48,000 rows a season; 372 columns | VERIFIED | Own count: 47,260–49,922 rows 2019–2025; 2025 = 48,771 × 372 | None |
| First download is "a file of a few tens of megabytes" | CORRECTED | nflverse-data `pbp` release: play_by_play_2025.parquet = 20.3 MB | "a Parquet file of about 20 megabytes" |
| nfl_data_py archived/deprecated; nflreadpy 0.1.5 (Nov 19 2025) is current; Polars | VERIFIED | GitHub API (`archived: true`); PyPI JSON (0.1.5, 2025-11-19, still latest Oct 8 2026); FACTS §7 | None |
| nflreadpy default cache: memory, 24 h; `update_config`, `clear_cache()`, `get_current_season()`; loaders take `True` | VERIFIED | nflreadpy 0.1.5 source (`cache_mode` default MEMORY, `cache_duration` 86400); README utility functions | None |
| Walker run: SB LX, 2nd qtr 14:04, 2nd & 10 at SEA 24, 30 yds, pushed out at NE 46, desc text, ep 0.12, epa +2.62 | VERIFIED | nflverse pbp game 2025_22_SEA_NE play 1015 | None |
| `wp` (53%) is "from the score, the clock, the field position and the pre-game point spread" | CORRECTED | nflverse: `wp` = 0.534 ignores the spread; `vegas_wp` = 0.716 includes it (nflfastR field descriptions) | Text now says `wp` ignores the betting line and `vegas_wp` gives 72%; new assert |
| Seattle the designated away team; spread_line −4.5 means NE 4.5-pt underdogs | VERIFIED | nflverse schedules; Covers (SEA −4.5 on game day) | None |
| Super Bowl LX Feb 8 2026, SEA 29–13, Walker MVP 27-135 | VERIFIED | FACTS §1; nflverse merge | None |
| Walker's carries total negative EPA; 30- and 29-yard bursts | VERIFIED | Own calc: 27 carries, 135 yds, −2.04 EPA; longest 30 and 29 | None |
| ~70% of rows are runs and passes | VERIFIED | Own calc: 71.0% | None |
| No-play-type rows include "the two-minute warning" | CORRECTED | Own calc: the 2025 file has no two-minute-warning rows; NA rows are GAME, END QUARTER n, END GAME, weather delays | "the end of each quarter and of the game, and the odd weather delay" |
| `no_play` is either a penalty or a timeout; kneels/spikes have own play_type and no flags; 2-pt tries have no down | VERIFIED | Own calc (45% of no_play rows are timeouts; kneel/spike pass = rush = 0; 2-pt down all NA) | None |
| Scrambles ≈ 1,000 a season; play_type-based pass rate "a couple of points low" | CORRECTED (minor) | Own calc: 1,089 scrambles; 60.1% vs 56.8% = 3.3 pts | "about three points low" (matches drill 2) |
| Garbage-time filter removes ~3 in 10; 1st-down pass rate moves ~3 pts; 4th down 67% → 57% | VERIFIED | Own calc: 31.2%; 49.8 → 46.4; 66.8 → 56.8 | None |
| 1st-and-10 pass rate by WP: ~50% → a bit over 40% across 20–80; ~70% below 10%; < 30% above 90% | VERIFIED | Own calc: 50.3 → 43.3; 72.8; 27.8 | None |
| Course filter 10–90% = 13-02's; 01-02 and 02-01 use 20–80% | VERIFIED | 13-02 line 101; 01-02 line 103; 02-01 line 732 | None |
| nflfastR guides "use similar ranges" | CORRECTED (made specific) | Beginner's guide: `wp > .20 & wp < .80 & down <= 2 & qtr <= 2 & half_seconds_remaining > 120` | Text and fn `gt` now quote the guide's filter; VERIFY removed |
| Guide filters `rush == 1 \| pass == 1`, which keeps penalty snaps; drop `no_play` to match official stats | VERIFIED | Beginner's guide | None |
| Participation keys, 2016–2022 NGS / 2023+ FTN, published after season, re-releases Sept 2025 | VERIFIED | FACTS §7; nflreadr 1.5.0 news ("after each season has ended") | None |
| Participation licence CC-BY-SA 4.0 | VERIFIED | nflreadr 1.5.0 release notes ("licensed under CC-BY-SA 4.0 ... credited (for 2023 onwards) to FTN Data via nflverse") | Source added to fn `ftn` |
| FTN charting licence CC-BY-SA 4.0 | VERIFIED | nflreadpy README License section ("the FTN data is CC-BY-SA 4.0") | Source added to fn `ftn`; VERIFY removed |
| FTN charting from 2022, weekly; `is_motion` before or at the snap; no tush-push flag; no coverage | VERIFIED | nflreadr FTN dictionary; FACTS §7 | None |
| Rosters back to 1920; NGS summaries from 2016; schedules/pbp from 1999 | VERIFIED | nflreadpy 0.1.5 loader source | None |
| Join match 100%; formation ~99%; coverage 0% 2016–17, "a little over half" after | VERIFIED | Own calc: 53–61% of runs and dropbacks 2018–2025 | None |
| Shotgun label 55% → 69% across the break; empty folded into shotgun; 7 labels → 3 | VERIFIED | Own calc 54.9 → 68.8; FACTS §7 | None |
| Coverage labels add COVER_9/COMBO/BLOWN, drop PREVENT; `ngs_air_yards` NA from 2024; personnel string formats | VERIFIED | FACTS §7; participation dictionary (`ngs_air_yards`) | None |
| Man share 29% / 41% / 48% / 31% (2022–25) | VERIFIED | FACTS §7; chapter asserts | None |
| pbp shotgun peaks ~72% (2023), ~66% (2025); FTN under center 27% → 34% | VERIFIED | FACTS §10; chapter asserts | None |
| Walker play: participation and FTN say under center, FTN RPO, 8 in box; 43 shotgun/U disagreements in 2025 | VERIFIED | Own lookup (FTN `qb_location` U, `is_rpo` True, `n_defense_box` 8) | None |
| Personnel shares 58.8 / 24.4 / 5.1 (2025), 64.6 (2018, 11) | VERIFIED | FACTS §10; chapter asserts | None |
| 1st-down pass rate 44–49% every season 1999–2025; 2nd ~55 → ~60; 3rd peak ~86% 2013–19, < 80% 2025; 4th ~43% → ~57% | VERIFIED | Own calc: 1st 44.0–48.8; 2nd 55.2 → 59.6; 3rd 86.4/86.0/85.8/86.2/86.1, 2025 79.5; 4th 42.7 → 56.8 | None |
| 2004 illegal-contact point of emphasis | VERIFIED | 09-03 fact-check (NBC Sports Boston 2019; PFT 2014; nflverse 49 → 123) | VERIFY removed (09-03 holds the sources) |
| 4th-down pass share rose because teams go for it more at longer distances | CORRECTED | Own calc: snaps at 4+ yds fell from 30% (1999) to 18% (2025); the rise is in the call at 2+ yds (1999: 55/67/77% pass at 2/3/4+; 2025: 89/96/95%) | Bullet rewritten; new fn `fourth`; new assert |
| BDB 2025 gameId/playId match nflverse old_game_id/play_id | VERIFIED (with caveat) | Own check: old_game_id is a 10-digit text key (2022090800 = 2022_01_BUF_LA); the widely used BDB 2025 example play 2022090800/56 is the same play in nflverse (Allen to Diggs, 6 yds) | Example play changed from 2022091100/55 (no play 55 exists in that game) to 2022090800/56; comment notes the cast to int; VERIFY removed |
| Example log is "Seattle's first fifteen snaps" | CORRECTED | Own calc: the log skips SEA's 1:25, :40 and :37 snaps in Q1 | "fifteen Seattle snaps from the first quarter and the start of the second (Seattle's last three snaps of the first quarter are missing ...)" |
| Log scores: you 10/15, always pass 9/15, D&D 9/15; 01-06 guesser rule | VERIFIED | Chapter asserts; 01-06 line 1209 (same rule) | None |
| Holding drill: no_play, yards_gained 0, rush = 1; 176 such plays, mean EPA −1.12; 1st & 20 at own 15 | VERIFIED | Own calc; 10-yard foul at the line enforced from the previous spot | None |
| 13-02 says leaving penalty snaps out makes passing look worse (DPI deep) | VERIFIED | 13-02 lines 144–149 | None |
| nfl_data_py README wording; Reber NGS 41.7% | VERIFIED | FACTS §7, §10 | None |

**Counts:** VERIFIED 33 · CORRECTED 7 · SOFTENED 1 · REMOVED 2.

**Uncertain:** the BDB key match rests on one well-known example play plus the ID format, not on the Kaggle file itself (not downloaded). nflfastR's raw source is documented only as "nfl.com" feeds; the "official statistics crew / gamebook" wording is standard knowledge, not quoted from nflverse.
