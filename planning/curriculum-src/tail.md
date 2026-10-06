## 7. Pilot chapters

Four pilots stress-test tone, depth, the graphics pipeline, and the analytics pipeline at four points on the level scale. Between
them they use every diagram type and hit the hardest writing problems in the book: being concrete without jargon (L1), explaining
11-man coordination clearly (L3), making invisible post-snap movement visible and measurable (L5), and teaching with shown code
(L4, Part 13).

| Pilot | ID | File | Level | Main test |
|---|---|---|---|---|
| 1 | 01-04 | `chapters/01-foundations/01-04-what-a-play-really-is.qmd` | 1 | Tone; jargon discipline; non-field graphics |
| 2 | 03-02 | `chapters/03-the-run-game/03-02-zone-running.qmd` | 3 | Mid-level depth; field-diagram language; signature animation |
| 3 | 06-06 | `chapters/06-pass-coverage/06-06-disguise-rotation-and-split-field.qmd` | 5 | Prerequisite chain; two-time-state visuals; tracking data |
| 4 | 13-02 | `chapters/13-analytics-and-data/13-02-expected-points-and-success-rate.qmd` | 4 | Code-shown analytics; the EPA primer/deepening split |

### Pilot 1: 01-04 "What a Play Really Is (It Isn't Picking a Card in Madden)" (Level 1)

- **Tests tone.** This is the reader's first real "aha" chapter, aimed squarely at the Madden mental model. If the voice is
  condescending, too jargon-heavy, or too cute here, it will be wrong everywhere. It has to introduce the idea of rules,
  reads, and options without yet having any scheme vocabulary.
- **Tests jargon discipline explicitly.** It decomposes a call into formation, motion, *protection*, *concept*, and *tags*, and
  uses *green dot* and *tempo*, all before they are taught. Every such word must get a one-line gloss and a forward link
  (04-02, 04-04, 08-04). The beginner review checks each one.
- **Tests the staff map (audit M9).** Who actually picks the play: head coach as play-caller vs coordinator, booth vs sideline,
  position coaches, QC, analytics. Play-callers are labelled by season (FACTS-current §9).
- **Tests non-field graphics.** Timelines (play clock with the 15-second radio cut-off), the staff map, communication flow, and
  the "anatomy of a play call" breakdown. These are a different kind of figure from field diagrams and will recur in Parts 8 and 10.
- **Tests the first whole-play animation.** A full play from huddle break to whistle with each player's assignment shown in
  turn is the simplest end-to-end test of the animation and frame-strip pipeline, with no scheme complexity.
- **Tests the drill mechanism** in its simplest form (the formal prediction log itself starts in 01-06).

### Pilot 2: 03-02 "Zone Running: Inside Zone, Outside Zone, Split Zone, and the Cutback" (Level 3)

- **Tests mid-level depth.** Zone blocking is the classic "everyone has heard of it, almost nobody can explain it" topic. It
  needs rules (covered/uncovered), a decision tree (bang-bend-bounce), and 11-player coordination. If the reader can follow this
  chapter, the depth level is right for Parts 3-7. It now includes split zone and the bash/insert/arc tags (audit M21, N5).
- **Tests the core field-diagram language.** Blocking arrows, aiming points, technique numbers, the same play drawn against two
  different fronts (rules adapting), and a forward reference to front names not yet taught (the prerequisite discipline in action).
- **Tests the 'new block' box** (the cut block arrives here, audit N1) and the "You'll need" box at Level 3.
- **Tests the signature animation.** Outside zone with all 11 assignments is the book's model animation: if the frame strip
  is readable in PDF, every later animation will be.
- **Tests the data box.** EPA by run location (nflverse) with a real team example (Shanahan's 49ers), so the analytics thread
  appears in a Level-3 football chapter. It depends on the EPA primer in 01-02 (audit M2); if the chart needs more than that
  primer to read, the primer is too thin.
- **Tests history and team-example integration** (Alex Gibbs' Broncos -> Kyle Shanahan -> the 2025 Seahawks, labelled as
  Kubiak's single season before he became Raiders head coach).

### Pilot 3: 06-06 "Disguise, Rotation, and Split-Field Coverage" (Level 5)

- **Tests advanced depth.** It needs all of Part 6 plus motion (02-06). If a reader who has done the prerequisites can follow it,
  the scaffolding works. If not, earlier chapters need repair. It is the best single test of the prerequisite chain.
- **Tests the "You'll need" box as part of the pilot.** The chapter sits on roughly 15 unwritten prerequisites, so the beginner
  review judges it through its recap box. If the box cannot carry the load in a page, the box design (or the prerequisites) changes.
- **Tests the hardest visual problem.** Disguise is movement relative to the snap: what the defense showed vs what it played.
  The animations must show two time-states clearly, and the PDF frame strips must keep the "lie" legible without motion.
- **Tests the tracking-data bridge.** The safety-depth-around-the-snap figure uses Big Data Bowl tracking data drawn through the
  same diagram library as the synthetic plays. Its home is decided: it is built in 13-05 and 06-06 shows the result (audit S21);
  12-08 links. The pre-snap-shell agreement figure must come from BDB 2025 pre-snap tracking, not nflverse.
- **Tests the live-watching payoff and the part-end card.** The "call it twice" drill is real anticipation, then checking it;
  the chapter also closes Part 6 with the 'checklist so far' card.

### Pilot 4: 13-02 "Expected Points, EPA, and Success Rate" (Level 4)

- **Tests code-shown analytics.** Part 13 shows its code (AUTHORING §5); everything else folds it. This pilot checks that shown
  code stays readable in the PDF and that the nflreadpy cache and filters are stated.
- **Tests the primer/deepening split (audit M2).** EP, EPA, and success rate are owned by 01-02. 13-02 must deepen (the model,
  stability, selection effects, turnover randomness) without redefining, and its glossary front matter must not repeat 01-02's terms.
- **Tests the broadcast-metrics bridge and Appendix G.** Placing passer rating, QBR, ANY/A, DVOA, PFF grades, and ESPN win rates
  relative to EPA is the template for the metric cards in Appendix G.

**Still untested by the pilots:** the Part 12 case-study body shape and rule currency (kickoff rules changed in 2024, 2025, and 2026).
Before mass production, run a one-page outline smoke test of 12-03 (case study, with the 2025-vs-2026 staff box) and of 09-02
(rule currency against FACTS-current §3).

**Runner-up considered:** 08-01 "What Beats What". It is equally advanced but mostly reuses diagram types already tested by
03-02 and 06-06, and it has no tracking-data component.

## 8. Diagram library requirements

Derived from the chapter specifications ({{NS}} static, {{NA}} animated, {{NC}} data charts, {{NT}} tracking figures in chapters, plus ~200 atlas plates and cards).

- **One play model, three renderings.** A `Play` object (players, roles, keyframed paths, blocks, zones, annotations) renders
  to (a) a static diagram, (b) an HTML animation, and (c) a PDF frame strip (4-8 numbered panels with timestamps). Quarto uses
  `.content-visible when-format="html"` / `when-format="pdf"` blocks so each chapter cites one figure ID.
- **Coordinates match the tracking data.** Field in yards, x 0-120 (including end zones), y 0-53.3, the same as Big Data Bowl
  data after direction standardisation. Synthetic plays and real tracking frames then go through the same renderer.
- **Notation (front matter key).** Offense as circles (OL as squares, QB and ball carrier highlighted); defense as labelled
  chevrons or Xs; solid lines for routes and runs; T-bars for blocks; dashed lines for pre-snap motion; dotted lines for
  option/read branches; translucent polygons for zones (shape = zone type); numbered circles for QB progressions; one
  colour-blind-safe palette with distinct offense, defense, and highlight colours, legible in greyscale print.
- **Plate templates.** Formation, front, and coverage plates must be generated from the same definitions in the chapters and
  in the atlas (Appendices A-D), so a fix propagates everywhere.
- **One home per signature diagram.** A diagram reused in a later chapter is the same figure (or a static recap plate of it),
  never a second build: tush push (10-03), safety rotation from tracking (13-05), mesh/Y-cross (04-04), "one formation, four
  plays" (08-02), Jet Chip Wasp (12-04), Super Bowl XLIX and the Belichick plans (12-02), smash vs Cover 2 (06-04).
- **Branching plays.** Option, RPO, and "two-way concept" animations need branch support: one pre-snap state with two or more
  post-snap continuations shown side by side.
- **Two-time-state overlays.** Disguise and rotation figures show the pre-snap position as a ghost and the post-snap position as solid.
- **Non-field figures.** Timelines, flowcharts (catch rule, clock), matrices (concept x coverage), staff maps, coaching-tree
  networks, call-sheet mock-ups, checklist cards, and metric cards (Appendix G).
- **Data charts.** nflverse via `nflreadpy`; consistent chart theme; code folded in Parts 1-12 and shown in Part 13. Charts that
  cross the 2022/2023 participation source break mark it on the axis.
- **No broadcast screenshots.** All real plays are recreated as diagrams or from tracking data, which avoids licensing problems.

## 9. Fact-check flags and open questions

Items that are recent, disputed, or likely to change. `planning/FACTS-current.md` (checked 2026-10-06) resolves most of them;
re-verify anything marked LIKELY or UNVERIFIED there at writing time.

1. **Super Bowl LX (Feb 8, 2026): RESOLVED.** Seattle 29, New England 13, at Levi's Stadium; MVP Kenneth Walker III. Seattle's
   staff: HC Mike Macdonald, OC Klint Kubiak, DC Aden Durde (FACTS-current §1).
2. **Kickoff rules: RESOLVED.** 2024 trial, 2025 permanent version (touchback to the 35; onside when trailing), and the 2026
   changes (onside any time; 5 on the restraining line with a floater; kickoff-from-the-50 spot fixed at the 20). Re-check the
   2025 baseline against the primary source when writing 09-02 (FACTS-current §3).
3. **Tush push: RESOLVED.** The May 2025 ban failed 22-10 (24 needed); no proposal in 2026; legal for the 2026 season
   (FACTS-current §5).
4. **Overtime: RESOLVED.** Playoffs since 2022 and regular season since 2025: both teams possess; regular-season period 10 minutes,
   ties possible; no 2026 change found (FACTS-current §4).
5. **Data availability: RESOLVED.** `nflreadpy` (0.1.5, polars) replaces the archived `nfl_data_py`. Coverage type exists in
   participation for 2018-2025 only; participation is NGS for 2016-2022 and FTN from 2023 with different labels; FTN charting
   (2022+) has `is_motion` (before or at the snap) and `is_qb_sneak` but no coverage and no tush-push flag (FACTS-current §7).
6. **Big Data Bowl: RESOLVED for 2026.** 2026 theme: player movement while the ball is in the air (training files are 2023 Weeks
   1-18). 2027 not announced as of Oct 6, 2026; check before 13-05 goes to print (FACTS-current §8).
7. **Staff moves through 2026: RESOLVED, keep labelling seasons.** Kubiak became Raiders HC (2026), so "Kubiak's Seahawks" is the
   2025 season only; McDaniel is Chargers OC; Mike LaFleur is Cardinals HC; Fleury is Seattle's OC; Harbaugh is Giants HC and the
   Ravens are led by Jesse Minter; Bieniemy is back as Chiefs OC; the Lions' 2026 OC is Drew Petzing; Fangio remains Eagles DC with
   Sean Mannion as OC (FACTS-current §0 and §9).
8. **Single-season records cited in passing.** Myles Garrett's 23.0 sacks (2025) is VERIFIED; other 2025 records are LIKELY; verify or omit.
9. **Specific historical game plans** (Super Bowls XXV, XXXVI, LIII, the Super Bowl LIV 'Jet Chip Wasp' details, the Super Bowl
   LIX blitz count). Confirm against film and reputable breakdowns before drawing them. Do not reconstruct from memory.
10. **College ineligible-downfield distance: RESOLVED.** Still 3 yards in college vs 1 yard in the NFL. The year of the tabled
    1-yard proposal differs between the audit (2025) and FACTS-current C12 (2015); confirm it before printing. 2026 college changes
    (OPI 10 yards, fair-catch kick, two challenges, targeting carryover removed) need an NCAA primary source.
11. **Replay assist and the 2026 rule list.** The 2026 replay power is officially worded "consult" on ejections; the "sideline
    assistant may throw the challenge flag" item is UNVERIFIED and must not be cited. The three-strike suspension policy is LIKELY.
12. **Smaller items flagged by the audit.** 01-02 uses "One Yard Short" as a last-play stop, not a 4th-down stop (verify the
    Super Bowl XLVII alternative before using it); 04-02's Bengals-Chiefs game is the 2022-season AFC Championship (confirm);
    14-01 frames Purdy's rookie deal as the 2022-24 window (extension May 2025); 02-02 keeps the 2014 season and the January 2015
    game date distinct; 12-04 lists Super Bowl appearances (won LIV, LVII, LVIII; lost LV, LIX).

Open questions for the author:

- **Title and voice: SETTLED.** The book is *Reading the Game*; second person throughout (AUTHORING.md).
- **History placement.** Keep Part 11 late (current plan, so the history can use the full vocabulary), or move a lighter version earlier?
- **Animation format.** HTML5 video (matplotlib -> mp4) vs JS-driven (Plotly/Observable) animations. JS allows scrubbing and
  pausing at the snap, which matters for 06-06-style figures.
- **Environment: SETTLED.** Book build and data work run in the `rtg` dev container (Quarto + Python + nflreadpy).
