# 13-01 Working with nflverse Data in Python — beginner-reader review

Reviewer role: casual NFL watcher who has never played and is comfortable in pandas. Has read the
chapters before 13-01 in curriculum order (Parts 1-12). Where it matters, I also note what a reader
on the sanctioned shortcut (13-01 straight after Part 2) would hit. I read the qmd start to finish and
looked at all 34 PDF pages (`pdfs/13-01-nflverse-in-python.pdf`, built 08:12 after the 08:11 qmd).
Line numbers refer to the qmd; "p." means the PDF page.

**Overall:** strong, honest and useful. The source-break section, the funnel, and "reproduce before
you extend" are the best data-literacy teaching in the book so far. The main problems: (a) **I can't
actually run it**, because `gridiron` is imported in the first cell and never explained as something I
can install; (b) a few **internal contradictions** that a careful reader will catch ("most events are
not snaps"; 1,160 vs 1,089 scrambles; three different "neutral" definitions); (c) **print drag**: about a
third of the PDF is matplotlib styling code; (d) the **frame strip** doesn't show what its caption claims.
At about 7,200 prose words plus captions and roughly 600 lines of code, it runs 45% over the 5,000-word target.

---

## 1. Terms used before they're explained, or never explained

| Where | Quote | Problem |
|---|---|---|
| l.80, p.2 (first code cell) | `from gridiron import Play, Field, ...` / `from gridiron.data import nfl, pbp` | **Biggest gap.** l.62-64 tell me to "run them as you go", but the chapter never says what `gridiron` is to *me*: whether it's on PyPI, where the repo is, or how to install it. l.336-338 say "on your machine you can call nflreadpy directly", yet every later cell uses `pbp(range(1999, 2026), columns=HCOLS)` (l.699), `nfl()`, `Play`, `Field`. Give a one-line install or repo link, plus the plain-nflreadpy equivalent of `pbp(seasons, columns=)` (`nfl.load_pbp(s).select(cols).to_pandas()`). |
| l.459-460, l.510-511, schema fig p.8 | "`wp` and `wpa` for winning, `cp` and `cpoe` for passing accuracy, `xpass` and `pass_oe` for play-calling tendencies" | `wpa`, `cp`, `xpass` and `pass_oe` are never expanded. The schema shows `xpass 0.61` and `wpa +0.077` for Walker's run, and I can't say what 0.61 *means*. One gloss each would do it ("xpass: the model's chance this situation produces a pass, 61%"; "pass_oe: pass over expected"). Link to the owning chapters (WPA → 13-03, xpass → 13-04). |
| l.440 ff., funnel and garbage-time sections | "win probability" | This is central to the chapter's filter, but it's never bold-linked to the glossary (owner 13-03). Only the prose gloss at l.440 explains it. |
| l.748 | "formalises the idea as the [**neutral situation**] (13-04)" | I've **already met** "neutral situations" twice, defined differently each time. 02-01 used 1st and 2nd down only, WP 20-80%, outside the last 2 min. 01-02's grid used all downs at 20-80%, and this chapter's l.1120 caption calls it "neutral situations as 01-02 defined them". Presenting it as a future idea while two earlier definitions exist confuses me. Say plainly: "earlier chapters used 'neutral' loosely for X and Y; 13-04 pins it down." |
| l.38 (YBAT), l.625 | "runs and dropbacks" | "Dropback" is used in the objectives and the You'll-need area before it's bolded at l.625. That's fine for the linear reader but not for the shortcut reader; bold-define it earlier or gloss it at first use. |
| l.601-602 | "**scramble**", "**sack**" bolded | These are bolded as if defined here but carry no glossary link (sack is owned by 01-02). |
| l.183-185, fig-flow p.3 | "Next Gen Stats: chip tracking" | "Chip tracking" is unexplained (RFID chips in the shoulder pads). Next Gen Stats is linked only at l.860, after the figure. |
| l.956 | "FTN added COVER_9, COMBO and BLOWN, and dropped PREVENT" | COMBO and BLOWN are never glossed. A shortcut reader has no Cover 9 (06-01) or prevent (10-04) either. Half a sentence each would do it. |
| l.555 caption, l.592 | "x = 110 − yardline_100" | *Why 110?* The 10-yard end zone at x 0-10 is never stated. One clause fixes it. |
| l.1278, p.26 | tracking table columns `s`, `dir`, `frameType` | I can't decode these. "Positions ten times a second" covers x and y only. What are `s` (speed, yd/s), the units and zero direction of `dir`, and the BDB y-axis convention (why does a run "to the left" make y go *up*)? Either gloss them in one sentence or don't print those columns. |
| l.1611, checklist | "`game_id` + `play_id` for participation" | This contradicts l.853, which says participation is keyed by `nflverse_game_id` + `play_id`. A beginner copying the checklist will look for a column that doesn't exist. Also, three game-ID schemes appear (`game_id`, `nflverse_game_id`, `old_game_id`) with no single sentence saying how they relate. |

## 2. Leaps: a missing or assumed "why"

1. **"Regular season only" (funnel, l.654).** No reason is given. Why do analysts drop playoffs (only 12 teams, a few games, a different context)? The opening example *is* a playoff play, so the omission stands out.
2. **Filtering on `play_type` right after being told it's a trap.** The flags section (l.598-636) says `play_type == "pass"` miscounts passes. The funnel then filters with `play_type.isin(["pass","run"])` (l.649). The reason this is fine (scrambles are inside "run", so the *row set* is right and only the *classification* is wrong) is never said. One sentence prevents a "wait, what?".
3. **When to use 10-90 and when to use 20-80 (l.738-748).** The garbage-time rationale at l.684-691 is entirely about *play-calling* ("the score made those calls, not the coaches' preferences"). Then l.742-743 says 20-80 is for play-calling "where the score's pull starts earlier". So what is 10-90 for? The funnel intro says "play-calling and efficiency". I finish the section unable to choose a filter for a new question. Give a rule: 10-90 for efficiency (EPA, success), 20-80 for tendencies, or whatever the course actually means.
4. **"Most events are not snaps" (l.528-529).** The very next table shows about 71% runs and passes, and kicks are snaps too, so roughly 90% of rows *are* snaps. The sentence is wrong. It should say "not every event is a run or pass."
5. **The no_play row (l.540).** It is described as "a play wiped out by an accepted penalty or a timeout". Where do pre-snap fouls (false starts) go? They are no_play rows too, but they aren't a "play wiped out." I'd want that named.
6. **Shotgun jump arithmetic (fig-formation-break caption).** "Empty backfields were folded into shotgun, which is why 'shotgun' jumps from 55% to 69%." Empty was about 8% in 2022, so that explains 8 of the 14 points. The table on p.20 shows the pbp shotgun flag rising about 4 points 2022→2023 anyway. Say "mostly why" and point to the real rise, or a numerate reader will think the caption is fudging.
7. **Rule 2, "translate to what both sides can say" (l.979-982).** It is stated but never demonstrated for formation. The obvious demo is to collapse NGS SINGLEBACK, I_FORM and JUMBO into "under center" and compare with FTN's UNDER CENTER across the break. As written, I can't do it for formation, the very column the section is about.
8. **Personnel reproduction filter (fig-personnel).** The chapter just spent pages on WP filters, then rebuilds 02-01's personnel chart with *no* WP filter (`snaps` only), without saying so. It matches 02-01, but the caption should say "all runs and dropbacks, no garbage-time filter (as in 02-01)", because the chapter's own checklist (#2, #6) demands it.
9. **Walker's MVP with negative EPA (l.845-847).** This is a great hook, but "a run of short gains on early downs each cost a little" deserves one number: his success rate or median gain. Otherwise it's an assertion I'm asked to take on faith in a chapter about checking things.
10. **The hook's promise (l.27-28 → l.1034-1035).** "You'll find out why two respectable sources disagree" pays off as "Without the film you can't say who is right." That tells me *that* they disagree, not *why*. Add one sentence on how each is produced: the press box types live from the stadium view, while FTN charts later from broadcast and All-22. Also note that the pistol, or a QB who starts under center and steps back, is the kind of edge case that splits them.

## 3. Diagrams I couldn't decode, or captions that don't say what to notice

- **fig-walker-anim frame strip (p.27): the strip doesn't tell the story.**
  - The caption says "the run past the yellow line", but in the +2.6s frame the ball is still well short of it, about 6 yards downfield.
  - After the snap, the **R marker vanishes**: frames 2-4 show only a football icon on a faint trail. I hunted for R.
  - **All 21 other players are frozen**: no blocking, no pursuit, and the QB never turns. The caption should say "only the ball carrier is simulated", or I'll think the simulation is broken.
  - The **painted "30" numbers sit under the C boxes** in all four frames (drop_numbers isn't applied to animation frames), which is a label collision.
  - The +2.6s frame should be later (≥3.5s) so the back actually crosses the yellow line.
- **fig-row-to-play (p.26).** The arrow ends at the yellow line, about 10 yards, while the "+30 yds to NE 46" label floats at the top left, detached from the arrow tip. The window cuts the run, so the label should sit *at* the tip or say "(continues off the diagram)." The handoff isn't visible either. Otherwise it decodes well: the 8-man box and the Shotgun ghost ring are excellent.
- **fig-timeline (p.15).**
  - The "Big Data Bowl tracking" row puts bars at **2022-2023** next to a label reading "**BDB 2025 and 2026 editions**". A beginner reads that as a contradiction. Say "BDB 2025 edition = 2022 season data; BDB 2026 = 2023."
  - The dotted "source break" line runs through the play-by-play, schedules and rosters rows, which *have no break*. It should span only the participation rows.
  - The legend omits grey (nflverse's own) and the dashed "after the season" box.
- **fig-personnel (p.22).** A solid grey gridline at 2022 sits next to the dotted break line at 2022.5, so at a glance there are two vertical lines and I wasn't sure which was the break. Drop the x-grid or the 2022 gridline.
- **fig-formation-break (p.18).** SHOTGUN (blue) and EMPTY (light blue) are hard to tell apart in print. Pistol jumps to 9% in 2024 and back to about 5% in 2025 with no comment; is that another coding quirk? A data-literacy chapter should flag it or the reader will wonder.
- **fig-flow (p.3).** Clear. The only thing to add to the caption is what to notice: "nflverse is a republisher" is the takeaway, but it's in the prose, not the caption.
- **Drill diagrams (pp.30-32)** render cleanly. But see §5: they don't carry information the question needs. In Drill 1, an "S" linebacker box sits right beside "SS", which briefly read as a duplicate.

## 4. Drag and repetition

- **Plotting boilerplate in print.** Pages 7, 9, 11-13, 17-18, 21-23 and 25 are dominated by `fontsize=`, `zorder=`, `ha="center"` and `bbox=` code. The chapter rightly hides the three "pure illustration" helpers (l.138-141), but the **yardline figure** (l.556-583, almost pure illustration from two numbers), the **schema regex families** (l.451-503), and the styling halves of the funnel, WP, formation, personnel and grid charts are printed in full. Split each into a short shown *data* cell and a folded/hidden *plotting* cell. That would cut the PDF by several pages without losing any teaching.
- **The `md_table` and `drop_numbers` helpers** open the chapter (p.2) before any football. Move them into the hidden illustration-helpers cell.
- **"Two things…/Two facts…/Two definitions…/Two habits…"** opens six paragraphs (l.303, 376, 508, 859, 878, 1461). It's a noticeable tic.
- **"Sacks and scrambles count as passes"** appears 6 times. That's fine in captions, but the drill-2 answer re-teaches the whole flags section.
- **Fourth-down Film-room bullet (l.1209-1215)** is the densest paragraph in the chapter. Distances, shares by bucket and decades are all crammed into one bullet, plus a footnote with six more numbers. Cut it to two sentences and leave the rest to 13-03.
- **The 10-90 vs 20-80 discussion** recurs in four places (l.738-779, l.1116, l.1156, takeaways). Settle it once (see §2.3) and the later mentions can be one clause.

## 5. Can I do each "You'll be able to…" item?

| Objective | Verdict |
|---|---|
| Install nflreadpy, load a season in two lines, move Polars↔pandas | **Yes.** It's clear, and the side-by-side by-down example is perfect. |
| Load schedules, rosters, participation, FTN; say what each adds and which seasons | **Yes**, thanks to the timeline (once the BDB label confusion is fixed). |
| Read a pbp row: situation, result, model columns | **Mostly.** Situation and result, yes. Model columns: `ep`/`epa`/`wp` yes, but not `wpa`/`xpass`/`cp` (see §1). |
| Filter to "real" plays and state the filter | **Yes** for the mechanics. **No** for *choosing* 10-90 vs 20-80 (§2.3). |
| Join participation and FTN without being fooled by the source break | **Partly.** I can do the join and spot a break. I can't "translate" formation across it, because rule 2 is never demonstrated (§2.7). Coverage: I know not to chart man share across 2022-23, but not what to do instead. |
| Reproduce a chart end to end, and score my prediction log weekly | **On paper, yes; on my machine, no**: I don't have `gridiron` (§1, row 1). The Sunday notebook also uses `df25` and `game` from earlier cells, so I need a sentence on which variable to swap for `week_pbp`. |

### Predict-the-play, attempted before opening answers

- **Drill 1 (write the row).** My prediction: run / pass 0 / rush 1 / down 3 / ydstogo 2 / yardline_100 40 / yards_gained 3 / first_down 1; next row 1 / 10 / 37. **All correct.** Two issues:
  - The chapter itself taught "a row is not always a play", so I hesitated over "the *next* row". It might be a timeout or the end of the quarter. The answer ignores this; it should say "the next *snap*" or acknowledge the case.
  - The diagram (12 personnel, 4-3, single-high) is **decoration**: nothing in it bears on the answer. Make it earn its place by also asking for the 2025 `offense_personnel` string ("1 C, 2 G, 1 QB, 1 RB, 2 T, 2 TE, 2 WR"), which tests the source-break lesson.
- **Drill 2 (scramble).** My prediction: play_type run, qb_scramble 1, pass 1, rush 0; use `pass == 1`; about 3 points. **Correct**, but the last part is recall of l.635-636, not reasoning. **Number clash:** the answer says **1,089** scrambles in the 2025 regular season, while the flags table on p.11 says **1,160**. (The table counts no-play scrambles too.) The reader sees two different "how many scrambles" figures pages apart. Reconcile them or footnote the difference. The diagram is again decoration.
- **Drill 3 (called back).** My prediction: no_play; dropped by the course filter; negative EPA, which I got right. Then "Would the nflfastR guide's filter, `pass == 1 | rush == 1`, keep it?" **That filter is never shown in the body before the drill.** The only nflfastR filter quoted (l.744-746, [^gt]) is the WP 20-80 one. I guessed "keeps it" from l.629-630, but the flags table (no-play `rush_flag` = 0.07) made me doubt it. Introduce `pass == 1 | rush == 1` in the funnel section, or note it in the drill stem. The first-and-20 at the 15 enforcement I could get from 09-03.

## 6. Knowledge gaps: what I still wonder

1. **In-season personnel.** My goal is reading live games. Participation for 2026 doesn't arrive until February 2027 and FTN charting has no personnel grouping. So how do I get this week's personnel for my Sunday notebook? (Log it myself? Use `n_offense_backfield`?) The chapter should say plainly that in-season personnel isn't in nflverse.
2. **The 40 columns I'll use regularly** (l.445). Name them. A compact cheat sheet (`success`, `air_yards`, `yards_after_catch`, `complete_pass`, `interception`, `fumble_lost`, `touchdown`, `penalty`, `pass_location`, `run_gap`, `qb_dropback`, `no_huddle`, ...) would be the most-used page of Part 13. Note that the `success` column is never shown, though the You'll-need box mentions success rate.
3. **Team abbreviations across relocations** (OAK→LV, SD→LAC, STL→LA). The chapter says nflverse "fixes" them but not what I filter on to get "the Raiders, 2016-2025".
4. **How fast is "nightly during the season"?** If I run the Sunday notebook on Monday morning, is Sunday night's game in? Is Monday night's? A one-line expectation would save a confused first week.
5. **How trustworthy are FTN's judgement columns** (catchable, contested, interception-worthy)? Is there any inter-charter agreement figure? The chapter says "somebody's judgement, recorded at speed" but gives no sense of the error rate beyond the 43-play shotgun disagreement.
6. **Are 2016-2017 personnel as reliable as later years?** Coverage is missing there, and formation matches at 99%, but there's no word on NGS's early-year quality.
7. **The `rusher` vs `rusher_player_id` vs roster join.** Why does the merge use `rusher_player_id` when l.810-811 says pbp stores the ID in `rusher_id`? Both exist, and I don't know which to use.

## Quick-fix priority list

1. Say how to get/install `gridiron`, or give plain-nflreadpy equivalents (§1).
2. Fix "most events are not snaps" (l.528-529), the 1,160 vs 1,089 scramble clash, and the checklist key (l.1611).
3. Give a rule for 10-90 vs 20-80 and reconcile "neutral situation" with 01-02 and 02-01.
4. Fix the frame strip: a later last frame, a visible R, a caption that says only the carrier moves, and painted numbers off the C boxes. Also attach "+30 yds" to the arrow on fig-row-to-play.
5. Fix the timeline: BDB edition vs season, and the break line only across participation rows.
6. Introduce `pass == 1 | rush == 1` before Drill 3. Make the Drill 1 and Drill 2 diagrams carry needed information.
7. Fold or hide the plotting halves of the data-chart cells to cut print drag. Gloss `wpa`/`xpass`/`cp`/`pass_oe`, and `s`/`dir`.

---

## Revision (2026-10-08): finding -> action

Covers this review and `13-01-coach.md`. The fact-check stays intact: no verified claim was changed. Every new number is computed in the chapter and backed by a hidden assert. Build: `build_pdfs.py 13-01-nflverse-in-python --html` gives OK with zero errors (34 pages, down from 35 even though content was added). I looked at every diagram page at 60 dpi and zoomed to 110–140 dpi on Figs 6, 11, 12 and 13–15.

### Beginner §1: terms
| Finding | Action |
|---|---|
| `gridiron` never explained as installable | "How to read this chapter" now says what gridiron is and gives `pip install "git+https://github.com/joshuawjulian/reading-the-game"` (the repo is public; pyproject builds with hatchling). The install section adds the plain-nflreadpy equivalents of `nfl()` and `pbp(seasons, columns=)`. |
| `wpa`, `cp`, `xpass`, `pass_oe` unexplained | New bullet list after the schema glosses each one, using Walker's live values (wpa +7.7 pts, xpass 0.61 = 61%, pass_oe −61). Links: WPA (13-03), CPOE (04-07), xpass and PROE (13-04). `success` is explained too. |
| "win probability" not glossary-linked | Bold-linked at first use (`gl-win-probability`, owner 13-03). |
| Three "neutral" definitions | Settled once in a two-bullet rule: 10–90% is the default and is for efficiency; 20–80% "neutral" is for comparing play-callers. The rule names 01-02's version (all downs) and 02-01's (1st and 2nd down) and says 13-04 formalises it. Later mentions are one clause. |
| "Dropback" used before definition | The objectives gloss it. "Dropback" and "Scramble" are added to this chapter's glossary front matter (neither has an owner in the term index or another chapter; see note). |
| scramble/sack bolded without links | Both are linked now: scramble to this chapter's glossary entry, sack to `gl-sack` (01-02). |
| "chip tracking" unexplained; NGS linked late | The flow box now reads "shoulder-pad chips". The caption and the following paragraph explain the radio chips, link Next Gen Stats at first prose use, and link 13-05. |
| COMBO/BLOWN/Cover 9/prevent unglossed | Half-sentence glosses plus links to Cover 9 (06-01), combo coverage (06-02) and prevent defense (10-04). |
| Why x = 110 − yardline_100 | Stated in the prose, the caption and the end-zone labels ("x 0–10", "x 110–120"). The cell now prints the arithmetic. |
| `s`, `dir`, `frameType` undecoded | New paragraph after the tracking table covers frameType, time, x, the y direction (it increases to the offense's left, which is why a left run climbs), s in yd/s, and dir in degrees clockwise from +y. |
| Checklist key wrong; three game IDs | Checklist #3 is rewritten (pbp `game_id`+`play_id` = participation `nflverse_game_id`+`play_id`, etc.). A new paragraph explains `game_id` / `nflverse_game_id` / `old_game_id` (the BDB key), with an assert on SB LX's `2026020800`. |

### Beginner §2: missing whys
| Finding | Action |
|---|---|
| Why regular season only | Explained: 12–14 teams, at most four games, a different context. The SB LX example is called the exception. |
| Filtering on `play_type` after calling it a trap | New paragraph: use `play_type` to *choose rows* (scrambles are inside "run" and sacks inside "pass") and the `pass` flag to *classify* them. |
| 10–90 vs 20–80 | See §1. The table's labels are now "10–90% (default)" and "20–80% (neutral)", and the text explains why a league history can use the default. |
| "Most events are not snaps" wrong | Now reads "not every event is a run or a pass". |
| Where pre-snap fouls go | no_play is split into three cases: called-back play, pre-snap foul (false start, the most common, checked: 658 of the 2025 no-play penalties) and timeout. |
| Shotgun 55→69 arithmetic | Caption now says "mostly because empty (8% in 2022) was folded in; the remaining few points are a real rise the pbp flag also shows". |
| Rule 2 never demonstrated | Done. The `cross-check` cell collapses NGS SINGLEBACK/I_FORM/JUMBO into "under center" and sets it beside pbp "not shotgun" and FTN U/P. The translated series is continuous. 2022, the overlap year, gives NGS 32.0% vs FTN 31.7%. Asserts cover agreement within 2 pts in every season. |
| Personnel caption doesn't state filter | It now says "all of them, with no garbage-time filter, as in 02-01". |
| Walker MVP negative EPA: give a number | Added: 26% success (7 of 27), median 2 yards, 15 of 27 for ≤2 yards (asserted). |
| Hook's "why they disagree" unpaid | New paragraph: the stat crew types live from the press box, while FTN charts from video later. Disagreements cluster on pistol and step-back alignments. |

### Beginner §3: diagrams
| Finding | Action |
|---|---|
| Frame strip doesn't show caption's claim; R vanishes; statues; numbers | Rebuilt. Times are now 0 / 0.8 / 2.2 / 3.6 s, so the back is past the yellow line in the last panel (asserted). The ball is drawn 1.1 yd beside the carrier, so R stays visible. The animated play adds a QB carry-out fake and pursuit by W, M, FS, SS and the stalked LCB. I checked pairwise distances at each panel time so no defender covers the carrier. A chapter-side `show_animation_clean` helper strips the painted yard numbers from the strip and the video. The caption states which parts are simulated. |
| Fig 11 arrow ends at the yellow line; detached label | The run now leaves the top of the window, with the "+30 yds ↑" label beside the path. The caption says the arrow runs off the diagram to NE 46. |
| Timeline: BDB edition vs season; break line through pbp rows; legend | The labels read "2025 edition: 2022 season / 2026 edition: 2023 season", moved off the row label after a first render collided. The break line spans only the participation rows. The legend adds grey (league feed via nflverse) and the dashed after-season box. |
| Personnel: gridline beside the break line | The x grid is off. |
| Formation chart: SHOTGUN vs EMPTY colours; pistol spike | EMPTY is now warm grey. The pistol 4→9→5% spike gets its own paragraph as a within-supplier artefact. |
| Flow caption lacks "what to notice" | Added at the start of the caption. |
| Drill 1: S beside SS | The SS moved down outside U (coach A4), so S and SS are now on opposite sides. |

### Beginner §4: drag
| Finding | Action |
|---|---|
| Plotting boilerplate in print | All styling code (yardline, schema families, funnel, WP bars, formation, personnel, pass grid, history) moved into `plot_…` helpers. They sit in html-only folded cells ("Show the plotting code") right before each chart, so print shows only the data code. |
| md_table / drop_numbers open the chapter | Moved into the folded helpers cell. The setup cell is imports only. |
| "Two things/facts/definitions/habits" tic | Five of the six openers are reworded. The one "Two cautions" left introduces a genuinely two-item list. |
| "Sacks and scrambles count as passes" ×6 | The drill-2 answer no longer re-teaches the flags section. Captions keep the short clause. |
| Fourth-down bullet too dense | Cut to two sentences. The footnote is kept, referenced once. |
| 10-90 vs 20-80 repeated in four places | Settled once (§2.3). The other mentions are now one clause. |

### Beginner §5–6: objectives, drills, knowledge gaps
| Finding | Action |
|---|---|
| Can't run on my machine | See §1, row 1. |
| Sunday notebook: which variable to swap | Code comment: "swap df25 for week_pbp and put in your game_id and team". The routine prints the loaded game IDs. |
| Drill 1 "next row"; decorative diagram | The answer now says "next snap", and in code "the next row *that has a down*". The drill also asks for the 2025 `offense_personnel` string (and gives the pre-2023 form), which tests the source-break lesson. |
| Drill 2: 1,089 vs 1,160 clash; decorative | The flags table now checks no_play first, so its scramble row is 1,089. The 71 called-back scrambles sit in the no-play row and the text says so. The drill uses the same computed `N_SCR` (asserted). The diagram now shows 2-Man (man lines, Will apexed over H) and routes past the sticks. |
| Drill 3 uses a filter never shown | `pass == 1 \| rush == 1` is introduced in the funnel paragraph, and the drill stem adds a downfield-hold question. |
| In-season personnel | New paragraph: nflverse has no personnel during the season (participation arrives after it; FTN has backfield count, not grouping), so you log it yourself. Added to takeaways. |
| The 40 columns | New cheat-sheet table of about 50 columns by job, including `success`. A hidden assert checks every name exists in the 2025 file. |
| Team abbreviations across relocations | nflverse uses current abbreviations in every season (checked: 1999 has LV/LA/LAC, no OAK). Stated with an assert. |
| How fast is "nightly" | "Sunday games normally in by Monday morning, Monday night's a day later; check the IDs". New footnote [^nightly] (nflfastR README). |
| FTN judgement reliability | Stated plainly that FTN publishes no inter-charter agreement figure, so treat those columns as one trained viewer's opinion. **Declined** to give an error rate: no public source exists. |
| 2016–17 personnel reliability | **Not added as prose.** The match-rate table already shows personnel coverage by season, and FACTS §7 shows 2016–17 fill rates matching 2018–22. I found no source on NGS early-year *accuracy*, so I make no claim. |
| `rusher_id` vs `rusher_player_id` | Explained, checked in data: the `*_player_id` set follows the box score (scrambler = rusher_player_id), while the short set follows the pass/rush flags (scrambler = passer_id, rusher_id empty). |

### Coach review
| Finding | Action |
|---|---|
| A1 nickel over the TE, slot uncovered; "three corners" | `$` moved to apex the slot (4.5, −7.0). The box outline is widened to −8.4 so it clears the `$` marker. The caption says "five defensive backs (three corners, two safeties)" and "participation lists the edge players as outside linebackers; they are labelled E". |
| A2 arrow on the yellow line; no blocks; RPO tag | The arrow exits the top. LT hooks WDE, H seals `$`, X stalks the LCB. The caption adds the FTN RPO tag and says the throw it offered isn't recorded, so none is drawn. |
| A3 strip | See beginner §3. |
| A4 unsound 4-3 vs 12 personnel | SS is down outside U at (5.5, −6.5), corners at 5 yards, and the caption describes it. |
| A5 Drill 2 slot uncovered, routes short, RB idle, note collision | The Will is apexed over H. Five man-coverage lines make "everyone covered" visible. X and Z run go routes off the window, and H and Y run outs at 9 yards, past the sticks (the first render showed 7.5 because slots start 1.5 off the ball; fixed). RB steps up in protection. The note is moved, and the QB path is nudged clear of Y's route and the end. The answer adds the 2-Man/scramble nuance with links to 2-Man (06-04) and spy (10-02). |
| A6 Drill 3 no play-side blocks, path through the E | Inside zone right is drawn as a full scheme: Y on a wide-9 end, RG on the 3-technique, RT and LG climbing to Mike and Will, C on the nose, LT cutting off the backside end. The back hits the gap outside the RT. The WDE is nudged to (1.3, −4.9) so the LT's ring clears it. The Sam and SS are placed outside so no unblocked defender sits on the path. *Departure:* I used a wide-9 end instead of the coach's 7-technique double team. With gridiron's 1.6-yard splits, the 7-tech double left no drawable lane between markers. |
| A7 not every hold on a run is a no_play | Added to the drill-3 answer from data: 62 of 238 accepted offensive holds on designed runs in 2025 stay `play_type == "run"` (spot-of-foul enforcement downfield). Fix: add `penalty == 0`. Asserted. |
| B1 flags are post-snap decisions on RPOs; screens/PA | New "Two cautions" paragraph in the flags section. The "intended" wording is softened to "the play the offense set out to run" and "closest the data comes to the call". |
| B2 "first-and-10 unpredictable" contradicts 01-06 | Reworded: it's an average, the scorebug alone tells you little, the formation tells you a lot. The closing lesson links 01-06. |
| B3 third-down decline: mix vs call | New `third-down-split` cell. The distance mix barely moved (max 2 pts, asserted). On third-and-2–3 the pass rate fell from 80% to 64% (asserted), so it was the call. The bullet is rewritten. |
| B4 personnel is who, not where | New paragraph covering jumbo (6+ OL now counted in the parser: 3–6% of snaps a season, asserted), FB/TE roster labels, and personnel ≠ formation. |
| B5 FTN pistol spike | See beginner §3. |
| B6 pbp shotgun "no source break" but not uniform | Now "one supplier since 1999, typed by a different home stadium's crew each week… about thirty recorders who mostly agree". |
| B7 "next row" | See drill 1. |
| B8 garbage time bends efficiency too | Added: soft shells inflate a trailing offense's efficiency, and a leading defense concedes yards. This is part of why 10–90% is the efficiency filter. |
| D notes for gridiron | Not edited (per instructions). These are worked around in-chapter: the nickel, SS and Will positions are moved by hand, and `show_animation_clean` drops the yard numbers. Still open for the maintainer: (1) `defense()` nickel tie-break against inline/slot TEs; (2) 4-3 vs two-TE sets; (3) a numbers-off option for `show_animation`/`frame_strip`; (4) the ball marker (zorder 11) hides the carrier's label after a handoff. |

### Length
The prose grew to about 9,100 words including captions and callouts (the review counted about 7,200 plus captions). Most of the growth is answers to the findings: the column cheat sheet, the Rule 2 demo, the third-down split, the RPO/hold nuances and the in-season gap. Print drag fell sharply because about 250 lines of plotting code left the PDF. The PDF went from 35 to 34 pages despite the additions. I judged every addition a "why" the beginner or coach asked for, so I did not cut further.
