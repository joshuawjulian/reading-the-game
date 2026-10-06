## 7. Pilot chapters

Three pilots chosen to stress-test tone, depth, and the graphics pipeline at three points on the level scale. Between them
they use every diagram type except tracking-heavy analysis, and they hit the three hardest writing problems in the book:
being concrete without jargon (L1), explaining 11-man coordination clearly (L3), and making invisible post-snap movement
visible and measurable (L5).

### Pilot 1: 01-04 "What a Play Really Is (It Isn't Picking a Card in Madden)" (Level 1)

- **Tests tone.** This is the reader's first real "aha" chapter, aimed squarely at the Madden mental model. If the voice is
  condescending, too jargon-heavy, or too cute here, it will be wrong everywhere. It has to introduce the idea of rules,
  reads, and options without yet having any scheme vocabulary.
- **Tests non-field graphics.** Timelines (play clock with the 15-second radio cut-off), communication flow, and the
  "anatomy of a play call" breakdown. These are a different kind of figure from field diagrams and will recur in Parts 8 and 10.
- **Tests the first whole-play animation.** A full play from huddle break to whistle with each player's assignment shown in
  turn is the simplest end-to-end test of the animation and frame-strip pipeline, with no scheme complexity.
- **Tests the drill/prediction-log mechanism** in its simplest form.

### Pilot 2: 03-02 "Zone Running: Inside Zone, Outside Zone, and the Cutback" (Level 3)

- **Tests mid-level depth.** Zone blocking is the classic "everyone has heard of it, almost nobody can explain it" topic. It
  needs rules (covered/uncovered), a decision tree (bang-bend-bounce), and 11-player coordination. If the reader can follow this
  chapter, the depth level is right for Parts 3-7.
- **Tests the core field-diagram language.** Blocking arrows, aiming points, technique numbers, the same play drawn against two
  different fronts (rules adapting), and a forward reference to front names not yet taught (the prerequisite discipline in action).
- **Tests the signature animation.** Outside zone with all 11 assignments is the book's model animation: if the frame strip
  is readable in PDF, every later animation will be.
- **Tests the data box.** EPA by run location (nflverse) with a real team example (Shanahan's 49ers), so the analytics thread
  appears in a Level-3 football chapter, not only in Part 13.
- **Tests history and team-example integration** (Alex Gibbs' Broncos -> Kyle Shanahan -> the 2025 Seahawks).

### Pilot 3: 06-06 "Disguise, Rotation, and Split-Field Coverage" (Level 5)

- **Tests advanced depth.** It needs all of Part 6 plus motion (02-05). If a reader who has done the prerequisites can follow it,
  the scaffolding works. If not, earlier chapters need repair. It is the best single test of the prerequisite chain.
- **Tests the hardest visual problem.** Disguise is movement relative to the snap: what the defense showed vs what it played.
  The animations must show two time-states clearly, and the PDF frame strips must keep the "lie" legible without motion.
- **Tests the tracking-data bridge.** The safety-depth-around-the-snap figure uses Big Data Bowl tracking data drawn through the
  same diagram library as the synthetic plays. This proves the data adapter the reader will later use for their own BDB work.
- **Tests the live-watching payoff.** The "call it twice" drill is what the reader asked for: real anticipation, then checking it.

**Runner-up considered:** 08-01 "What Beats What". It is equally advanced but mostly reuses diagram types already tested by
03-02 and 06-06, and it has no tracking-data component.

## 8. Diagram library requirements

Derived from the chapter specifications ({{NS}} static, {{NA}} animated, {{NC}} data charts, {{NT}} tracking figures in chapters, plus ~175 atlas plates).

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
- **Branching plays.** Option, RPO, and "two-way concept" animations need branch support: one pre-snap state with two or more
  post-snap continuations shown side by side.
- **Two-time-state overlays.** Disguise and rotation figures show the pre-snap position as a ghost and the post-snap position as solid.
- **Non-field figures.** Timelines, flowcharts, matrices (concept x coverage), coaching-tree networks, and call-sheet mock-ups.
- **Data charts.** nflverse via `nflreadpy`; consistent chart theme; code folded in Parts 1-12 and shown in Part 13.
- **No broadcast screenshots.** All real plays are recreated as diagrams or from tracking data, which avoids licensing problems.

## 9. Fact-check flags and open questions

Items that are recent, disputed, or likely to change. Each must be verified at writing time:

1. **Super Bowl LX (Feb 2026).** The plan assumes Seattle beat New England, with Macdonald's defense and Klint Kubiak's wide-zone
   offense. Verify the result, score, and scheme details before 11-05, 12-03, and 12-08 use it.
2. **Kickoff rules.** 2024 dynamic kickoff specifications, the 2025 changes (touchback spot, onside-kick declaration window), and any 2026 change.
3. **Tush push.** The 2025 ban proposal fell short; check 2026 offseason votes before writing 10-03 and 12-06.
4. **Overtime.** Confirm the 2025 regular-season rule (both teams possess) and current playoff rules.
5. **Data availability.** Confirm `nflreadpy` as the successor to `nfl_data_py`, and which participation/FTN fields (personnel,
   formation, motion, box count, coverage) exist for 2023-2025. Coverage-type data is patchy, so 06-05, 06-06, and 13-04 charts may
   need FTN-only seasons.
6. **Big Data Bowl 2026 theme and data release.** Needed for 13-05.
7. **Staff moves through 2026.** Ben Johnson (Bears), Aaron Glenn (Jets), Fangio, Kubiak, Macdonald, and other coordinator changes.
8. **Single-season records cited in passing** (e.g., 2025 sack totals). Verify or omit.
9. **Specific historical game plans** (Super Bowls XXV, XXXVI, LIII, the Super Bowl LIV 'Jet Chip Wasp' details). Confirm against film and
   reputable breakdowns before drawing them. Do not reconstruct from memory.
10. **College ineligible-downfield distance.** Historically 3 yards; confirm the current NCAA rule.

Open questions for the author:

- **Title and voice.** A working title is needed. Should the voice be second person ("you'll notice") throughout? (Recommended.)
- **History placement.** Keep Part 11 late (current plan, so the history can use the full vocabulary), or move a lighter version earlier?
- **Animation format.** HTML5 video (matplotlib -> mp4) vs JS-driven (Plotly/Observable) animations. JS allows scrubbing and
  pausing at the snap, which matters for 06-06-style figures.
- **Environment.** Book build and data work in a `.devcontainer/` (Quarto + Python + nflreadpy), per the host-lean policy.
