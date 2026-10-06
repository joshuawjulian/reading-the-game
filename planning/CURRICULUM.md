# Football, Explained: Curriculum

_Planning document for a Quarto book. Curriculum only; no chapter prose. Prepared October 2026; content current through the 2025 NFL season._

**Size:** 15 parts, 70 chapters, 6 reference appendices. Estimated length 971 printed pages of chapters plus roughly 120-160 pages of atlas and glossary.

**Diagram inventory (chapters only):** 165 static, 68 animations (each also rendered as a PDF frame strip), 62 nflverse data charts, 6 tracking-data figures.

## Contents

1. Design principles
2. The chapter template
3. Part and chapter overview
4. Chapter specifications
5. Reference appendices (the atlas)
6. Master term index (glossary seed)
7. Pilot chapters
8. Diagram library requirements
9. Fact-check flags and open questions

## 1. Design principles

- **Every concept answers 'why does this exist?'** Each formation, coverage, and scheme is taught as a solution to a problem, and the problem it creates for the other side is named. The arms race is the course's narrative spine, not just Part 11.
- **Never use a concept before it is taught.** Every chapter lists its prerequisites; the build order below satisfies them. Where a diagram must show something not yet taught (e.g., a front name in a run-game diagram), it is labelled generically and the chapter states an explicit forward reference.
- **Spiral, then deepen.** A deliberately shallow first look at defense (02-06) lets the offense parts mention defenders. Technique numbers appear in 03-01 and are deepened in 05-01; disguise is hinted at in 02-05 and fully taught in 06-06.
- **Pictures first, words second.** Every chapter has diagrams in one consistent visual language (Section 8). Movement is shown as animation in HTML and as a numbered frame strip in PDF, so nothing depends on the format.
- **Real teams, real plays, real data.** Every scheme is anchored to teams that did it well, with season ranges. Charts use nflverse data; early chapters show the chart with code folded, and Part 13 teaches the reader to build them.
- **Watching is the goal.** Every chapter ends with a 'Watch for this on Sunday' drill. The drills feed one prediction log started in 01-02 and scored in 15-01, so the reader can measure their own improvement.
- **Two ways in: learn and look up.** The narrative path (Parts 1-15) teaches; the atlas appendices (A-F) and glossary give one-page reference cards with consistent fields, each linking back to the teaching chapter.
- **Honest about uncertainty.** Coverage names differ by team; charting data has errors; 'beaters' are probabilistic. The book says so instead of presenting one dialect as truth.
- **Levels are stated.** Level 1 = casual-fan basics; 3 = what a well-informed analyst knows; 5 = coach/film-room level. Chapters at Level 4-5 open with a short 'you'll need' recap box.

## 2. The chapter template

Every teaching chapter (8-20 printed pages) uses the same skeleton so readers know where to look:

1. **Cold open:** one real play described in two paragraphs, with the question it raises.
2. **What you'll learn / You'll need:** objectives and prerequisite links (the 'you'll need' box carries a two-line recap of each prerequisite).
3. **The problem:** why the concept exists (whose problem does it solve).
4. **The concept:** diagrams first, then rules, then variations.
5. **How the other side answers:** the counter, and the counter to the counter.
6. **History sidebar:** where it came from (college origins where relevant) and which rule changes mattered.
7. **Who does it best:** team/era examples with seasons.
8. **By the numbers:** one or two nflverse charts (code folded; reproducible in Part 13).
9. **Predict the play:** 3-5 frozen pre-snap pictures; the reader predicts, then the answer shows the animation/frame strip.
10. **Watch for this on Sunday:** the drill, plus what to record in the prediction log.
11. **Key terms:** each term linked to the glossary.

Case-study chapters (Part 12) use: the problem -> the scheme answer -> signature plays -> data fingerprint -> how opponents responded -> what survives.

## 3. Part and chapter overview

| Part | Title | Levels | Chapters | Est. pages |
|---|---|---|---|---|
| 01 | Foundations: The Game Beneath the Broadcast | 1 | 6 | 69 |
| 02 | Personnel and Formations: Reading the Offense Before the Snap | 1-2 | 6 | 70 |
| 03 | The Run Game | 2-3 | 5 | 71 |
| 04 | The Passing Game | 2-4 | 8 | 114 |
| 05 | Defensive Fronts and Run Defense | 3-4 | 5 | 66 |
| 06 | Pass Coverage | 3-5 | 6 | 84 |
| 07 | Pressure: Rush, Blitz, and Simulated Pressure | 3-4 | 3 | 39 |
| 08 | The Chess Match | 4-5 | 4 | 56 |
| 09 | Special Teams and the Rules That Shape Strategy | 2-3 | 3 | 38 |
| 10 | Situational Football | 3-4 | 4 | 54 |
| 11 | History: The Arms Race | 2-3 | 5 | 78 |
| 12 | Case Studies: Teams That Did It Best | 4-5 | 8 | 118 |
| 13 | Analytics and Data | 3-5 | 5 | 78 |
| 14 | The Business of Scheme: Roster, Cap, Draft, and Fantasy | 3 | 1 | 18 |
| 15 | Capstone: Watching Like a Coach | 5 | 1 | 18 |
| | **Total** | | **70** | **971** |

Full chapter list:

| ID | Slug (filename) | Title | Level | Pages | Prerequisites |
|---|---|---|---|---|---|
| 01-01 | `01-01-the-game-in-fifteen-minutes.qmd` | The Game in Fifteen Minutes: Field, Scoring, and Clock | 1 | 10 | none |
| 01-02 | `01-02-downs-distance-and-field-position.qmd` | Downs, Distance, and Field Position | 1 | 10 | 01-01 |
| 01-03 | `01-03-the-twenty-two.qmd` | The Twenty-Two: Every Position and What It Actually Does | 1 | 14 | 01-01 |
| 01-04 | `01-04-what-a-play-really-is.qmd` | What a Play Really Is (It Isn't Picking a Card in Madden) | 1 | 14 | 01-02, 01-03 |
| 01-05 | `01-05-the-pre-snap-phase.qmd` | The Pre-Snap Phase: Shifts, Motion, Cadence, and Audibles | 2 | 12 | 01-04 |
| 01-06 | `01-06-how-to-watch-a-broadcast.qmd` | How to Watch a Broadcast Like You Mean It | 1 | 9 | 01-05 |
| 02-01 | `02-01-personnel-groupings.qmd` | Personnel: Who's on the Field Before Anything Else | 1 | 11 | 01-03, 01-06 |
| 02-02 | `02-02-formation-rules-and-vocabulary.qmd` | Formation Rules and the Language of Alignment | 2 | 12 | 02-01 |
| 02-03 | `02-03-classic-formations.qmd` | Classic Formations: I, Power I, Pro Set, Singleback, and Their Ancestors | 2 | 11 | 02-02 |
| 02-04 | `02-04-spread-and-modern-formations.qmd` | Spread Formations: 2x2, Trips, Bunch, Empty, and the Condensed Revolution | 2 | 12 | 02-02 |
| 02-05 | `02-05-motion-and-shifts.qmd` | Motion and Shifts as Weapons | 3 | 12 | 02-04, 01-05 |
| 02-06 | `02-06-a-first-look-at-defense.qmd` | A First Look at Defense: Packages, the Box, Man vs Zone, One-High vs Two-High | 2 | 12 | 02-01, 01-03 |
| 03-01 | `03-01-run-game-language.qmd` | The Language of the Run Game: Gaps, Techniques, and Blocks | 2 | 13 | 02-03, 02-06 |
| 03-02 | `03-02-zone-running.qmd` | Zone Running: Inside Zone, Outside Zone, and the Cutback | 3 | 16 | 03-01 |
| 03-03 | `03-03-gap-and-power-runs.qmd` | Gap Schemes: Power, Counter, Duo, Trap, and Iso | 3 | 15 | 03-01 |
| 03-04 | `03-04-option-football.qmd` | Option Football: Reading Defenders Instead of Blocking Them | 3 | 15 | 03-02, 03-03 |
| 03-05 | `03-05-perimeter-and-misdirection.qmd` | Perimeter Runs and Misdirection: Jet Sweeps, Reverses, and the Wing-T's Children | 3 | 12 | 03-03, 02-05 |
| 04-01 | `04-01-passing-fundamentals.qmd` | Passing Game Fundamentals: Routes, Timing, and Reads | 2 | 14 | 02-04, 02-06 |
| 04-02 | `04-02-pass-protection.qmd` | Pass Protection: Slides, Man Schemes, and Who Blocks the Extra Guy | 3 | 14 | 04-01, 03-01, 01-05 |
| 04-03 | `04-03-quick-game.qmd` | The Quick Game: Slant-Flat, Stick, Snag, and Getting the Ball Out | 3 | 12 | 04-01, 04-02 |
| 04-04 | `04-04-dropback-concepts.qmd` | Dropback Concepts: Smash, Flood, Mesh, Levels, Dagger, and Four Verticals | 3 | 18 | 04-03 |
| 04-05 | `04-05-play-action-boots-screens.qmd` | Play-Action, Bootlegs, and Screens | 3 | 14 | 04-04, 03-02 |
| 04-06 | `04-06-rpos.qmd` | Run-Pass Options: Plays That Are Two Plays | 3 | 13 | 04-05, 03-04 |
| 04-07 | `04-07-quarterback-play.qmd` | Quarterback Play: Progressions, Eyes, the Pocket, and the Scramble Drill | 4 | 15 | 04-04, 04-02 |
| 04-08 | `04-08-offensive-systems-and-languages.qmd` | Offensive Systems and Play-Calling Languages | 4 | 14 | 04-07 |
| 05-01 | `05-01-dl-techniques-and-gap-control.qmd` | Defensive Line Play: Techniques, One-Gap and Two-Gap | 3 | 12 | 03-01, 02-06 |
| 05-02 | `05-02-even-fronts.qmd` | Even Fronts: 4-3 Over, Under, Wide-9, and the 46 Bear | 3 | 13 | 05-01 |
| 05-03 | `05-03-odd-and-hybrid-fronts.qmd` | Odd and Hybrid Fronts: 3-4, Okie, Tite, and Modern Nickel Fronts | 3 | 14 | 05-02 |
| 05-04 | `05-04-linebackers-and-second-level.qmd` | Linebackers: Keys, Flow, and the Hardest Job on the Field | 3 | 12 | 05-02, 04-05 |
| 05-05 | `05-05-run-fits-and-box-math.qmd` | Run Fits: Gap Integrity, Force, Spill, and Box Math | 4 | 15 | 05-04, 03-04 |
| 06-01 | `06-01-coverage-fundamentals.qmd` | Coverage Fundamentals: Zones, Leverage, and Reading the Shell | 3 | 14 | 04-04, 02-06 |
| 06-02 | `06-02-man-coverage.qmd` | Man Coverage: Cover 0, Cover 1, Robbers, and Brackets | 3 | 13 | 06-01 |
| 06-03 | `06-03-cover-3-family.qmd` | Cover 3: Sky, Buzz, Cloud, and Seattle's Match Version | 3 | 13 | 06-01 |
| 06-04 | `06-04-cover-2-and-tampa-2.qmd` | Cover 2 and Tampa 2 | 3 | 12 | 06-03 |
| 06-05 | `06-05-quarters-and-match.qmd` | Quarters and the Two-High Match Family: Cover 4, Cover 6, Palms | 4 | 16 | 06-04, 05-05 |
| 06-06 | `06-06-disguise-rotation-and-split-field.qmd` | Disguise, Rotation, and Split-Field Coverage | 5 | 16 | 06-05, 02-05 |
| 07-01 | `07-01-pass-rush.qmd` | The Pass Rush: Moves, Stunts, and Why Pressure Beats Sacks | 3 | 12 | 04-02, 05-01 |
| 07-02 | `07-02-blitz-and-man-pressure.qmd` | Blitzing: Numbers, Overloads, A-Gap Mugs, and Cover 0 | 3 | 13 | 07-01, 06-02 |
| 07-03 | `07-03-zone-blitz-and-simulated-pressure.qmd` | Zone Blitzes, Fire Zones, and Simulated Pressure | 4 | 14 | 07-02, 06-03 |
| 08-01 | `08-01-concepts-versus-coverages.qmd` | What Beats What: Pass Concepts Versus Coverages | 4 | 16 | 06-06, 04-04, 06-02 |
| 08-02 | `08-02-constraint-theory-and-sequencing.qmd` | Constraint Theory: How Plays Talk to Each Other | 4 | 13 | 08-01, 03-05, 04-05 |
| 08-03 | `08-03-game-planning-week.qmd` | The Game Plan: A Week Inside an NFL Building | 4 | 14 | 08-02 |
| 08-04 | `08-04-in-game-adjustments-and-tempo.qmd` | In-Game Adjustments, Tempo, and the Sideline Battle | 4 | 13 | 08-03 |
| 09-01 | `09-01-kicking-and-punting.qmd` | Field Goals, Extra Points, and the Punting Game | 2 | 12 | 01-02, 01-03 |
| 09-02 | `09-02-kickoffs-and-returns.qmd` | Kickoffs, Returns, and the Dynamic Kickoff | 2 | 11 | 09-01, 07-02 |
| 09-03 | `09-03-rules-that-shape-strategy.qmd` | The Rulebook as Strategy: Contact Rules, Penalties, and Officiating | 3 | 15 | 06-01, 04-06, 04-02 |
| 10-01 | `10-01-down-distance-and-field-zones.qmd` | Down, Distance, and Field Zones | 3 | 12 | 01-02, 08-02 |
| 10-02 | `10-02-third-down.qmd` | Third Down: The Money Down | 3 | 13 | 10-01, 07-03 |
| 10-03 | `10-03-red-zone-goal-line-and-short-yardage.qmd` | Red Zone, Goal Line, and Short Yardage (Including the Tush Push) | 3 | 14 | 10-02, 09-03, 03-04 |
| 10-04 | `10-04-clock-and-game-management.qmd` | The Clock, the Two-Minute Drill, and Fourth Down | 4 | 15 | 10-03, 09-01, 08-04 |
| 11-01 | `11-01-single-wing-to-dead-ball-era.qmd` | From the Single Wing to the Dead-Ball Era (1906-1977) | 2 | 15 | 02-03, 06-04 |
| 11-02 | `11-02-the-1978-liberation.qmd` | 1978 and the Passing Revolution (1978-1999) | 3 | 16 | 11-01, 04-08, 07-03, 05-02 |
| 11-03 | `11-03-the-college-laboratory.qmd` | The College Laboratory: Wing-T, Wishbone, Air Raid, Spread Option, and the RPO | 3 | 16 | 11-02, 03-04, 04-06, 06-05 |
| 11-04 | `11-04-dynasties-and-counterpunches.qmd` | Dynasties and Counterpunches (2000-2016) | 3 | 15 | 11-03 |
| 11-05 | `11-05-the-modern-era.qmd` | The Modern Era: McVay, Mahomes, Two-High, and the Under-Center Comeback (2017-2025) | 3 | 16 | 11-04, 06-06 |
| 12-01 | `12-01-walsh-49ers-west-coast.qmd` | Case Study: Bill Walsh's 49ers and the West Coast Offense | 4 | 14 | 11-02, 04-04 |
| 12-02 | `12-02-belichick-patriots-game-plan.qmd` | Case Study: Belichick and Game-Plan Football | 4 | 15 | 11-04, 08-03 |
| 12-03 | `12-03-shanahan-wide-zone-tree.qmd` | Case Study: The Shanahan Tree - Wide Zone, Boots, and the Illusion of Complexity | 4 | 16 | 11-05, 08-02 |
| 12-04 | `12-04-reid-chiefs.qmd` | Case Study: Andy Reid and the Kansas City Chiefs | 4 | 15 | 11-05, 07-02 |
| 12-05 | `12-05-ravens-lamar-run-game.qmd` | Case Study: The Ravens' Option Run Game with Lamar Jackson | 4 | 14 | 11-05, 03-04, 05-05 |
| 12-06 | `12-06-eagles-trenches-and-tush-push.qmd` | Case Study: The Eagles - Trenches, RPOs, and the Tush Push | 4 | 14 | 11-05, 10-03 |
| 12-07 | `12-07-lions-ben-johnson-and-campbell.qmd` | Case Study: The Lions - Ben Johnson's Offense and Dan Campbell's Aggression | 4 | 14 | 11-05, 10-04 |
| 12-08 | `12-08-two-high-to-macdonald.qmd` | Case Study: Fangio's Two-High Revolution and Macdonald's Answer | 5 | 16 | 11-05, 06-06, 07-03 |
| 13-01 | `13-01-nflverse-in-python.qmd` | Working with nflverse Data in Python | 3 | 14 | 01-02, 02-01 |
| 13-02 | `13-02-expected-points-and-success-rate.qmd` | Expected Points, EPA, and Success Rate | 4 | 16 | 13-01 |
| 13-03 | `13-03-win-probability-and-fourth-down.qmd` | Win Probability and Decision Analysis: Fourth Downs, Two-Pointers, Timeouts | 4 | 15 | 13-02, 10-04 |
| 13-04 | `13-04-tendencies-proe-and-charting.qmd` | Tendencies: PROE, Personnel, Motion, and Coverage from Charting Data | 4 | 15 | 13-02, 08-02 |
| 13-05 | `13-05-tracking-data-and-big-data-bowl.qmd` | Tracking Data and the Big Data Bowl | 5 | 18 | 13-04, 06-06 |
| 14-01 | `14-01-scheme-roster-and-fantasy.qmd` | Scheme, Roster, and Fantasy: How X's and O's Shape Money and Points | 3 | 18 | 13-02, 08-03 |
| 15-01 | `15-01-watching-like-a-coach.qmd` | Watching Like a Coach: The Master Checklist, All-22, and Charting a Game | 5 | 18 | 08-04, 10-04, 13-04 |

**Reading-order note:** the order above satisfies every prerequisite. Two sanctioned shortcuts: 13-01 (nflverse in Python) can be read any time after Part 2; Part 11 (history) can be read any time after Part 7 by readers who prefer the story first, skipping the few references to situational and special-teams material.

## 4. Chapter specifications

Diagram tags: **[S]** static; **[A]** animation, also rendered as a numbered frame strip in PDF; **[C]** nflverse data chart; **[T]** tracking-data figure (Big Data Bowl / NGS).

### Part 01: Foundations: The Game Beneath the Broadcast

_Levels 1._ Everything a casual viewer half-knows, made precise: the field, the clock, downs, the 22 players, and, most importantly, what a 'play' actually is in real life versus a Madden play card. Ends by starting the reader's prediction log, the course-long habit that every later chapter sharpens.

#### 01-01 The Game in Fifteen Minutes: Field, Scoring, and Clock

- **Slug:** `01-01-the-game-in-fifteen-minutes` | **Level:** 1 | **Est. length:** 10 pp
- **Prerequisites:** none
- **Forward references (flag in text):** 10-04 (overtime and clock strategy in depth)
- **Learning objectives:**
  - Read every marking on the field: yard lines, numbers, hash marks, goal line, end zone, sidelines.
  - Explain the wide (field) side vs short (boundary) side and why the ball's hash position changes play design.
  - Score every way points are made (TD, PAT, two-point try, field goal, safety) and why 7-vs-3 is the game's central tension.
  - Explain when the game clock runs and stops (incompletions, out of bounds, scores, change of possession, two-minute warning).
  - Distinguish the game clock from the play clock (40 / 25 seconds).
  - Describe the shape of a game: kickoff, possessions, quarters, halftime, overtime (details deferred to 10-04).
- **Key terms introduced:** end zone; goal line; yard line; hash marks; field side (wide side); boundary side (short side); sideline; touchdown; extra point (PAT); two-point conversion; field goal; safety (score); possession; quarter; two-minute warning; timeout; game clock; play clock
- **Diagrams:**
  - [S] Full field overhead, every marking labelled; ball on left hash with field/boundary shaded
  - [S] NFL vs college hash width side-by-side (why college has a much bigger wide side)
  - [S] Scoring summary card (6/1/2/3/2 with where each happens)
  - [S] Clock flowchart: 'after this play, does the clock run?'
- **Team / era examples:** Walk-through of Super Bowl LIX (Eagles 40-22 Chiefs) scoring plays located on the field diagram
- **Watch for this on Sunday:** Clock watcher: for one quarter, before each snap say aloud whether the clock is running and why.

#### 01-02 Downs, Distance, and Field Position

- **Slug:** `01-02-downs-distance-and-field-position` | **Level:** 1 | **Est. length:** 10 pp
- **Prerequisites:** 01-01
- **Forward references (flag in text):** 13-02 (Expected Points formalises 'field position as currency')
- **Learning objectives:**
  - Explain four downs, the line to gain, and why teams usually punt on fourth down.
  - Read the on-screen down-and-distance graphic and bucket it as short, medium, or long.
  - Define the line of scrimmage, the spot, and the chain crew / sticks.
  - Explain turnovers: interception, fumble, turnover on downs.
  - Treat field position as a currency (preview of Expected Points, 13-02).
  - Define a drive and the red zone.
- **Key terms introduced:** down; line to gain; first down; line of scrimmage; spot (of the ball); the sticks (chains); turnover; interception; fumble; turnover on downs; punt; field position; drive (possession); red zone
- **Diagrams:**
  - [A] Series of downs: 1st & 10 -> 2nd & 6 -> 3rd & 2 -> first down, chains moving (frame strip)
  - [S] Field-position map: own territory / midfield / opponent territory / red zone
  - [C] League 3rd-down conversion % by yards to go (nflverse, 2016-2025), code folded
- **Team / era examples:** League-average conversion rates; A famous 4th-down stop (e.g. Super Bowl XXXIV 'One Yard Short', Titans-Rams)
- **Watch for this on Sunday:** Down-and-distance forecaster: before each snap predict run or pass from down & distance alone; tally hit rate. This baseline accuracy is the first entry in the course-long prediction log.

#### 01-03 The Twenty-Two: Every Position and What It Actually Does

- **Slug:** `01-03-the-twenty-two` | **Level:** 1 | **Est. length:** 14 pp
- **Prerequisites:** 01-01
- **Learning objectives:**
  - Name the offensive positions and their jobs: QB, RB/HB, FB, WR (X/Z/slot), TE, OL (C, G, T).
  - Name the defensive positions: DT/NT, DE/edge, LB (Mike, Will, Sam), CB, slot corner, FS, SS.
  - Name the special-teams specialists: K, P, LS, holder, returner, gunner.
  - Distinguish eligible from ineligible receivers and the jersey-number convention.
  - Explain why body types map to jobs (combine data).
  - Separate position (who you are) from alignment and assignment (what you do this play).
- **Key terms introduced:** quarterback; running back (halfback); fullback; wide receiver; tight end; offensive line; center; guard; tackle (position); defensive tackle; nose tackle; defensive end; edge rusher; linebacker; Mike linebacker; Will linebacker; Sam linebacker; cornerback; slot cornerback (nickel back); safety (position); free safety; strong safety; kicker; punter; long snapper; holder; returner; gunner; eligible receiver; ineligible receiver; skill positions; front seven; secondary; alignment; assignment
- **Diagrams:**
  - [S] Offense (two-back) vs 4-3 base, every position labelled
  - [S] 11 personnel vs nickel, same labels (teaser for 02-01 / 02-06)
  - [C] Height/weight scatter by position from combine data
  - [S] Jersey-number ranges after the 2021 numbering change
- **Team / era examples:** Kyle Juszczyk (FB); Travis Kelce (TE); Penei Sewell (T); Aaron Donald (DT); T.J. Watt (edge); Fred Warner (LB); Kyle Hamilton (S)
- **Watch for this on Sunday:** One-player game: watch only the center for an entire drive and narrate what he did each play.

#### 01-04 What a Play Really Is (It Isn't Picking a Card in Madden)

- **Slug:** `01-04-what-a-play-really-is` | **Level:** 1 | **Est. length:** 14 pp
- **Prerequisites:** 01-02, 01-03
- **Forward references (flag in text):** 04-08 (play-calling languages); 08-04 (tempo)
- **Learning objectives:**
  - Trace the real chain: call sheet -> coordinator -> helmet radio -> QB / green-dot defender -> huddle or signals -> snap.
  - Decompose a play call into formation, motion, protection, concept, and tags.
  - Explain the 40-second play clock, the radio cut-off at 15 seconds, and delay of game.
  - Explain why both coordinators call blind and simultaneously, and why that creates the pre-snap chess match.
  - Contrast Madden with reality: 11 people executing rules, reads after the snap, one call = a family of outcomes.
  - Explain huddle vs no-huddle, wristbands, and sideline signal boards.
  - Describe what happens in the 3-7 seconds after the snap: assignments, reads, adjustments.
- **Key terms introduced:** play call; call sheet; helmet radio (coach-to-player communication); green dot; huddle; no-huddle; wristband; delay of game; snap; read (post-snap); verbiage (terminology); tag; playbook; install
- **Diagrams:**
  - [A] Play-clock timeline: whistle -> call in -> radio cuts at 15 -> huddle break -> set -> snap (frame strip)
  - [S] Communication flow: OC/DC -> QB/green dot -> teammates
  - [S] Anatomy of a play call: one long call split into labelled chunks
  - [S] Madden play art vs a coach's diagram of the same idea (rules, options, reads)
  - [A] One play from huddle break to whistle, every player's assignment highlighted in turn
- **Team / era examples:** Shanahan/McVay-style long verbal calls vs Erhardt-Perkins one-word concepts (teaser for 04-08); Peyton Manning's 'Omaha' era; Chiefs and wristband offenses; Bills' sugar huddle
- **Watch for this on Sunday:** Huddle stopwatch: time whistle-to-snap for several drives; note who huddles, who doesn't, and who snaps with under 5 seconds on the play clock.

#### 01-05 The Pre-Snap Phase: Shifts, Motion, Cadence, and Audibles

- **Slug:** `01-05-the-pre-snap-phase` | **Level:** 2 | **Est. length:** 12 pp
- **Prerequisites:** 01-04
- **Forward references (flag in text):** 02-05 (motion as a man/zone indicator); 07-02 (A-gap mugs and protection)
- **Learning objectives:**
  - Define set, shift, and motion and the legal-motion rules (one man moving, not toward the line at the snap; one-second set after a shift).
  - Explain cadence and hard counts and the penalties they draw (offside, encroachment, neutral zone infraction, false start).
  - Define audibles, checks, kill calls, and check-with-me systems.
  - Explain Mike identification and why it sets the protection.
  - Recognise defensive pre-snap movement: shifting fronts, safeties walking down, linebackers showing blitz.
  - List what each side is trying to learn before the snap.
- **Key terms introduced:** set; shift; motion; false start; offside; encroachment; neutral zone infraction; illegal motion; cadence (snap count); hard count; silent count; audible; check; kill call; check-with-me; Mike identification (MIKE ID); dummy call
- **Diagrams:**
  - [S] Legal vs illegal motion side by side
  - [A] Shift: TE crosses formation, everyone resets one second (frame strip)
  - [S] Kill call: two plays called, check made on box count
  - [A] Defense moves pre-snap: safety walks down, linebacker creeps to A-gap
- **Team / era examples:** Peyton Manning pre-snap theatre; Aaron Rodgers' hard count free plays; Eagles' silent count at home vs on the road
- **Watch for this on Sunday:** Count the movement: after the huddle breaks, count offensive players who move before the snap and whether any defender moves with them.

#### 01-06 How to Watch a Broadcast Like You Mean It

- **Slug:** `01-06-how-to-watch-a-broadcast` | **Level:** 1 | **Est. length:** 9 pp
- **Prerequisites:** 01-05
- **Forward references (flag in text):** 15-01 (All-22 film study in depth)
- **Learning objectives:**
  - Know what the broadcast camera hides (safeties, receivers downfield) and what replays, skycam, and end-zone angles reveal.
  - Use the pre-snap pause: read down, distance, clock, score, and timeouts in under five seconds.
  - Adopt the 'watch one thing' strategy by play type.
  - Read broadcast graphics: win-probability bars, Next Gen Stats overlays.
  - Set up the prediction log used for the rest of the course.
- **Key terms introduced:** All-22; end-zone camera; sideline camera; skycam; coaches film; prediction log
- **Diagrams:**
  - [S] Broadcast frame vs All-22 frame, field coverage shaded
  - [S] 'Where to look' by phase: pre-snap, first second, ball in air
  - [S] Prediction-log template (paper and a 10-line pandas version)
- **Team / era examples:** NFL+ Premium (All-22 access); Prime Vision alternate broadcast; Typical replay sequence on a big play
- **Watch for this on Sunday:** Prediction log, game 1: for one half log run/pass guess and outcome; compute accuracy (compare to 01-02 baseline).

### Part 02: Personnel and Formations: Reading the Offense Before the Snap

_Levels 1-2._ Who is on the field and where they stand. Personnel and formation are the first two clues of every pre-snap read. The part closes with a deliberately shallow first look at defense (packages, the box, man vs zone, one-high vs two-high) so Parts 3-4 can talk about defenders without waiting for Parts 5-6.

#### 02-01 Personnel: Who's on the Field Before Anything Else

- **Slug:** `02-01-personnel-groupings` | **Level:** 1 | **Est. length:** 11 pp
- **Prerequisites:** 01-03, 01-06
- **Learning objectives:**
  - Decode two-digit personnel (RBs then TEs; WRs = 5 - RB - TE): 11, 12, 21, 13, 22, 10, 20, 00.
  - Explain why personnel is the first pre-snap clue and how it forces the defense's substitution.
  - Explain substitution rules: the defense gets to match when the offense subs.
  - Read league personnel trends 2016-2025 (rise of 11; recent 12/13 and six-OL rebound).
  - Link personnel to run/pass tendencies with real data.
- **Key terms introduced:** personnel grouping; 11 personnel; 12 personnel; 21 personnel; 13 personnel; 22 personnel; 10 personnel; substitution matching; heavy personnel; jumbo (six offensive linemen)
- **Diagrams:**
  - [S] Personnel card deck: one neutral-alignment plate per grouping
  - [A] Offense subs in 12; defense swaps a DB for a LB (frame strip)
  - [C] League personnel share by season, 2016-2025
  - [C] Pass rate by personnel grouping (neutral situations)
- **Team / era examples:** McVay Rams 11 personnel (2017-2019); 49ers 21 personnel with Juszczyk; Ravens 2019 heavy sets; Eagles 2024 12 personnel with Saquon Barkley; Lions six-OL jumbo with an eligible tackle
- **Watch for this on Sunday:** Call the personnel: count RBs and TEs before each snap, say the number, then guess run/pass from the personnel chart.

#### 02-02 Formation Rules and the Language of Alignment

- **Slug:** `02-02-formation-rules-and-vocabulary` | **Level:** 2 | **Est. length:** 12 pp
- **Prerequisites:** 02-01
- **Learning objectives:**
  - Apply formation legality: seven on the line, ends eligible, covered receivers, illegal formation.
  - Define formation strength and how each side declares it (TE side, receiver side, field side).
  - Use the receiver labels X, Y, Z, H/F plus slot, wing, flanker, split end, in-line, off-ball.
  - Describe QB/backfield alignments: under center, shotgun, pistol, offset, sidecar.
  - Read splits (wide, normal, reduced, tight) and alignment landmarks (the numbers, the hash).
  - Recognise how the 2015 ineligible-receiver trick produced a rule change.
- **Key terms introduced:** on the line / off the line; covered receiver; illegal formation; formation strength; strong side; weak side; X receiver (split end); Z receiver (flanker); Y receiver; H / F (move player); slot; wing; in-line tight end; under center; shotgun; pistol; offset back; split (receiver split); reduced split; the numbers (alignment landmark)
- **Diagrams:**
  - [S] Legal vs illegal (six on the line; TE covered by a WR)
  - [S] Label map: X/Y/Z/H/F on a 2x2 and on a 3x1
  - [S] QB depth comparison: under center / pistol / shotgun with typical depths
  - [S] Split ladder: wide -> numbers -> reduced -> tight
  - [S] Strength declaration examples (TE strength vs passing strength vs field)
- **Team / era examples:** Patriots' ineligible-receiver formations vs Ravens (2014 season divisional round) and the subsequent rule change
- **Watch for this on Sunday:** Strength caller: name the strong side before each snap, then watch which way the defense set its front.

#### 02-03 Classic Formations: I, Power I, Pro Set, Singleback, and Their Ancestors

- **Slug:** `02-03-classic-formations` | **Level:** 2 | **Est. length:** 11 pp
- **Prerequisites:** 02-02
- **Learning objectives:**
  - Identify I-form, offset I, Power I, pro set (split backs), singleback, ace, T, wishbone, Wing-T, jumbo/goal line.
  - Explain each formation's purpose: lead blocker, downhill angles, balance, misdirection.
  - Explain why two-back, under-center formations declined and where they survive (21 personnel, short yardage, play-action).
  - Match each formation to its typical personnel.
- **Key terms introduced:** I-formation; offset I; Power I; pro set (split backs); singleback; ace formation; T-formation; wishbone; Wing-T; goal-line formation; full house backfield
- **Diagrams:**
  - [S] Atlas plates for each classic formation (10 plates, consistent style)
  - [C] Under-center vs shotgun share 2006-2025
  - [S] Family tree: T -> wishbone / I / pro set
- **Team / era examples:** Lombardi Packers pro set; Joe Gibbs' one-back/ace Redskins; 49ers 21 personnel I-form; Ravens 2024 with Patrick Ricard at FB
- **Watch for this on Sunday:** Name that formation: for 10 snaps name the formation, under center or gun, one back or two.

#### 02-04 Spread Formations: 2x2, Trips, Bunch, Empty, and the Condensed Revolution

- **Slug:** `02-04-spread-and-modern-formations` | **Level:** 2 | **Est. length:** 12 pp
- **Prerequisites:** 02-02
- **Learning objectives:**
  - Identify 2x2 (doubles), 3x1 (trips), empty (3x2), bunch, stack, nub, quads.
  - Explain why spreading the field forces the defense to declare itself and creates space.
  - Explain condensed/tight splits and why modern offenses use them (crack blocks, two-way go, rubs).
  - Recognise specialty looks: wildcat, unbalanced (tackle over), swinging gate.
- **Key terms introduced:** 2x2 (doubles); 3x1 (trips); empty (3x2); bunch; stack; nub; quads; condensed formation; wildcat; unbalanced line (tackle over); swinging gate
- **Diagrams:**
  - [S] Atlas plates for each spread formation
  - [S] Wide vs condensed split: same play, space created shaded
  - [C] Formation usage trend (shotgun 2x2 / 3x1 / empty) by season
- **Team / era examples:** 2007 Patriots spread (Brady, Moss, Welker); 2018 Rams condensed 3x1; 2008 Dolphins Wildcat; Bills empty with Josh Allen; Chiefs bunch sets
- **Watch for this on Sunday:** Formation & leverage: name the formation, then count receivers vs defenders on each side.

#### 02-05 Motion and Shifts as Weapons

- **Slug:** `02-05-motion-and-shifts` | **Level:** 3 | **Est. length:** 12 pp
- **Prerequisites:** 02-04, 01-05
- **Forward references (flag in text):** 06-06 (disguise defeats the motion indicator)
- **Learning objectives:**
  - Distinguish jet, orbit, fly, return (yo-yo), zoom, shift-to-bunch, and motion at the snap.
  - Explain what motion does: reveals man vs zone, changes strength, creates leverage, gives a running start, stresses communication.
  - Explain the NFL motion-at-the-snap rule vs college/CFL differences.
  - Describe the 2023-2025 motion boom with data.
  - Name defensive responses: travel (man), bump/slide (zone), spin (safety rotation).
- **Key terms introduced:** jet motion; orbit motion; return motion (yo-yo); fly motion; zoom motion; motion at the snap; man/zone indicator; bump (defensive adjustment); travel (man defender follows motion); spin (safety rotation on motion)
- **Diagrams:**
  - [S] Motion family plate
  - [A] Jet motion vs man: the corner runs across (frame strip)
  - [A] Same jet motion vs zone: defenders bump, safety spins (frame strip)
  - [C] Motion rate by team, 2022-2025 (FTN charting)
- **Team / era examples:** Mike McDaniel's 2023 Dolphins (Tyreek Hill motion at the snap); Shanahan 49ers (Deebo Samuel); McVay Rams; Chiefs orbit motion
- **Watch for this on Sunday:** Follow the motion: when a receiver motions, watch who follows; call man or zone; check after the play.

#### 02-06 A First Look at Defense: Packages, the Box, Man vs Zone, One-High vs Two-High

- **Slug:** `02-06-a-first-look-at-defense` | **Level:** 2 | **Est. length:** 12 pp
- **Prerequisites:** 02-01, 01-03
- **Forward references (flag in text):** Part 5 (fronts); Part 6 (coverages); Part 7 (pressure)
- **Learning objectives:**
  - Name defensive packages (base 4-3 / 3-4, nickel, dime, quarter, big nickel, goal line) and where 'nickel' and 'dime' come from.
  - Count the box and explain why box count drives run/pass choices.
  - Distinguish man and zone coverage at the concept level.
  - Distinguish one-high and two-high safety shells and what each is good at.
  - Explain why nickel is the modern NFL base defense.
  - Signpost what comes later: fronts (Part 5), coverages (Part 6), pressure (Part 7).
- **Key terms introduced:** defensive package; base defense; 4-3; 3-4; nickel; dime; quarter (dollar); big nickel; box; box count; light box; loaded box; man coverage; zone coverage; one-high (single-high); two-high; shell (coverage shell)
- **Diagrams:**
  - [S] Package plates: base / nickel / dime vs 11 personnel
  - [S] The box: tackle-to-tackle, ~5-7 yards deep, with counting examples
  - [S] One-high vs two-high silhouettes
  - [A] Same two routes vs man and vs zone (frame strip)
  - [C] Share of defensive snaps in nickel or lighter, by season
- **Team / era examples:** Belichick dime vs pass-heavy offenses; Ravens big nickel with Kyle Hamilton; Lions/Packers nickel as base
- **Watch for this on Sunday:** Box and shell: every snap count the box and say one-high or two-high; log alongside run/pass.

### Part 03: The Run Game

_Levels 2-3._ How offenses run the ball: the vocabulary of gaps and blocks, then the two great blocking families (zone and gap), option football, and misdirection. Defensive front names appear in diagrams with forward references to Part 5.

#### 03-01 The Language of the Run Game: Gaps, Techniques, and Blocks

- **Slug:** `03-01-run-game-language` | **Level:** 2 | **Est. length:** 13 pp
- **Prerequisites:** 02-03, 02-06
- **Forward references (flag in text):** 05-01 (technique numbers from the defense's side)
- **Learning objectives:**
  - Label gaps A-D and the common hole-numbering system.
  - Describe defensive alignments with technique numbers (0, 1, 2i, 2, 3, 4i, 4, 5, 6, 7, 9).
  - Define the core blocks: drive, down, reach, cut-off, combo, pull, kick-out, log, lead, cut, seal, crack.
  - Use covered/uncovered linemen and 'hat on a hat' arithmetic.
  - Explain why a non-running QB leaves the offense a defender short.
  - Contrast zone and gap philosophies at a high level.
- **Key terms introduced:** gap (A, B, C, D); hole numbering; technique (alignment number); shade; head-up; drive block; down block; reach block; cut-off block; combo block (double team); pull; kick-out; log block (wrap); lead block; cut block; seal block; crack block; covered / uncovered lineman; point of attack; playside / backside; hat math (numbers advantage)
- **Diagrams:**
  - [S] Master gap & technique chart
  - [S] Block library plate (one mini-diagram per block)
  - [S] Hat math: seven in the box vs six blockers + RB
  - [A] Combo block: guard and center double the 1-tech, one climbs to the Mike (frame strip)
- **Team / era examples:** Joe Gibbs' Hogs; Jason Kelce as a climbing/pulling center; Lions OL (Sewell, Ragnow)
- **Watch for this on Sunday:** Find the hole: predict the gap from the RB's first step; afterwards name the gap he actually hit.

#### 03-02 Zone Running: Inside Zone, Outside Zone, and the Cutback

- **Slug:** `03-02-zone-running` | **Level:** 3 | **Est. length:** 16 pp
- **Prerequisites:** 03-01
- **Forward references (flag in text):** 05-02 (front names); 04-05 (bootleg play-action); 12-03 (Shanahan case study)
- **Learning objectives:**
  - Explain zone rules: step playside, covered/uncovered, combo to the second level.
  - Distinguish inside zone, outside (wide) zone, and stretch by aiming point and intent.
  - Explain the RB's bang-bend-bounce read and the one-cut style.
  - Explain the cutback and the backside cut-off (and why cut blocks are controversial).
  - Show why wide zone pairs with bootleg play-action.
  - Evaluate zone efficiency with nflverse rushing EPA by run location.
- **Key terms introduced:** zone blocking; inside zone; outside zone (wide zone); stretch; aiming point; bang-bend-bounce; cutback; backside cut-off; one-cut runner; reach-and-overtake
- **Diagrams:**
  - [S] Inside zone vs an even (4-3 Over) front
  - [A] Outside zone vs an even front, all 11 assignments (frame strip, 6-8 frames)
  - [S] Same outside zone vs an odd front: the rules adapt
  - [S] RB decision tree: bang / bend / bounce
  - [C] EPA per rush by run location, 49ers vs league, 2019-2025
- **Team / era examples:** Alex Gibbs & Mike Shanahan's Broncos (Terrell Davis, 1996-98); Kyle Shanahan's 49ers (Christian McCaffrey 2023); McVay Rams; LaFleur Packers; Klint Kubiak's 2025 Seahawks
- **Watch for this on Sunday:** Bang, bend, bounce: on every zone run, call which option the RB took and where the backside end was.

#### 03-03 Gap Schemes: Power, Counter, Duo, Trap, and Iso

- **Slug:** `03-03-gap-and-power-runs` | **Level:** 3 | **Est. length:** 15 pp
- **Prerequisites:** 03-01
- **Forward references (flag in text):** 05-05 (how defenses fit gap runs)
- **Learning objectives:**
  - Explain gap schemes: down blocks, pullers, kick-outs, and wraps.
  - Diagram power, counter, duo, trap, iso, toss/sweep, pin-and-pull.
  - Explain how gap schemes manufacture extra blockers at the point of attack.
  - Know when coaches choose gap vs zone (front, personnel, OL body types).
  - Spot pre-snap tells of a pulling lineman.
- **Key terms introduced:** gap scheme (man/power blocking); power (Power O); counter (counter trey / GT counter); duo; trap; iso (isolation); toss / sweep; pin-and-pull; puller
- **Diagrams:**
  - [S] Power vs 4-3 Over
  - [A] Counter (GT) vs even front, guard kicks out and tackle wraps (frame strip)
  - [S] Duo vs two-high
  - [S] Trap vs a 3-technique
  - [S] Iso vs 4-3
  - [S] Pin-and-pull vs wide front
- **Team / era examples:** Gibbs Redskins counter trey (John Riggins era); Lombardi's power sweep as ancestor of pin-and-pull; Titans Derrick Henry duo/power; Ravens 2019 gap game; Eagles 2024 with Saquon Barkley
- **Watch for this on Sunday:** Follow the guard: watch the backside guard; if he pulls, call gap scheme and its direction.

#### 03-04 Option Football: Reading Defenders Instead of Blocking Them

- **Slug:** `03-04-option-football` | **Level:** 3 | **Est. length:** 15 pp
- **Prerequisites:** 03-02, 03-03
- **Forward references (flag in text):** 05-05 (defending option); 11-03 (college origins); 12-05 (Ravens case study)
- **Learning objectives:**
  - Explain the option principle: leave a defender unblocked, read him, gain a man.
  - Diagram zone read, inverted veer (power read), speed option, triple option, midline.
  - Explain dive / keep / pitch roles and the QB's read key.
  - Explain designed QB runs (QB power, QB counter, QB draw) as blocker-count changers.
  - Name defensive answers (scrape exchange, gap exchange) with a forward reference to 05-05.
  - Explain the NFL's on-and-off relationship with option (2012 wave, fade, Lamar/Hurts/Allen era).
- **Key terms introduced:** option; read key (read defender); zone read; give / keep; inverted veer (power read); speed option; triple option; dive; pitch; midline option; veer; QB power; QB counter; QB draw; scrape exchange
- **Diagrams:**
  - [A] Zone read, two branches: end crashes (keep) vs end stays (give) (frame strips)
  - [S] Triple option from flexbone
  - [S] Inverted veer
  - [S] Speed option
  - [S] QB power with RB as lead blocker
  - [C] Designed QB run EPA vs RB run EPA, 2016-2025
- **Team / era examples:** 2012 Washington (RGIII, pistol zone read); Kaepernick 49ers; Ravens 2019 rushing record with Lamar; Jalen Hurts' Eagles; Navy / Georgia Tech flexbone; Nevada pistol (Chris Ault)
- **Watch for this on Sunday:** Find the read key: on read looks, locate the unblocked end-man-on-line and predict give/keep from his first step.

#### 03-05 Perimeter Runs and Misdirection: Jet Sweeps, Reverses, and the Wing-T's Children

- **Slug:** `03-05-perimeter-and-misdirection` | **Level:** 3 | **Est. length:** 12 pp
- **Prerequisites:** 03-03, 02-05
- **Forward references (flag in text):** 08-02 (constraint theory); 04-05 (waggle -> bootleg)
- **Learning objectives:**
  - Explain jet sweep, end-around, reverse, crack-toss, and buck sweep and how each punishes over-pursuit.
  - Understand the Wing-T's series logic (buck sweep, trap, belly, waggle) and its NFL descendants.
  - Explain 'eye candy': motion and backfield action that freeze linebackers.
  - Connect misdirection to constraint theory (forward reference 08-02).
- **Key terms introduced:** jet sweep; end-around; reverse; crack-toss; buck sweep; series football; misdirection; eye candy; waggle
- **Diagrams:**
  - [S] Wing-T buck sweep
  - [A] Jet sweep with LB flow shown (frame strip)
  - [S] Crack-toss
  - [S] Reverse
  - [A] Eye candy: jet fake freezes the Mike for 0.5s, inside run hits (frame strip)
- **Team / era examples:** Delaware Wing-T (Tubby Raymond); Gus Malzahn; 2018 Rams jet motion; 49ers Deebo Samuel; Chiefs shovel/jet packages
- **Watch for this on Sunday:** Watch the second level: on jet motion, watch the linebackers' eyes and feet. Did they chase?

### Part 04: The Passing Game

_Levels 2-4._ Routes, timing, protection, the major concept families, play-action and screens, RPOs, quarterback play, and the systems/languages coaches use. Concepts are taught as stretches of generic defenders; the explicit 'what beats what' matrix waits until coverages are taught (08-01).

#### 04-01 Passing Game Fundamentals: Routes, Timing, and Reads

- **Slug:** `04-01-passing-fundamentals` | **Level:** 2 | **Est. length:** 14 pp
- **Prerequisites:** 02-04, 02-06
- **Forward references (flag in text):** 06-01 (zones the routes attack); 08-01 (what beats what)
- **Learning objectives:**
  - Use the numbered route tree and common non-tree routes (seam, wheel, whip, option, sluggo).
  - Link drop depth to route depth (3/5/7-step under center; 1/3/5 from shotgun) and timing.
  - Distinguish progression reads from defender reads; full-field vs half-field.
  - Explain vertical (high-low) and horizontal stretches of a single defender.
  - Define air yards, YAC, and average depth of target.
- **Key terms introduced:** route tree; flat route; slant; hitch (curl); out; dig (in); corner route; post; go (fly / 9); comeback; wheel; seam; option route; whip; sluggo; drop (3/5/7-step); timing route; progression; high-low read (vertical stretch); horizontal stretch; conflict defender; air yards; YAC (yards after catch); aDOT (average depth of target)
- **Diagrams:**
  - [S] Route tree with numbers
  - [S] Drop-to-route timing chart
  - [A] High-low stretch of a flat defender, both branches (frame strip)
  - [S] Horizontal stretch of a hook defender
  - [C] Completion % and EPA by target depth
- **Team / era examples:** Coryell numbering of the tree; Walsh timing passing; Mahomes off-platform vs Brady rhythm
- **Watch for this on Sunday:** Route caller: on replays, name every receiver's route.

#### 04-02 Pass Protection: Slides, Man Schemes, and Who Blocks the Extra Guy

- **Slug:** `04-02-pass-protection` | **Level:** 3 | **Est. length:** 14 pp
- **Prerequisites:** 04-01, 03-01, 01-05
- **Forward references (flag in text):** 07-01 / 07-02 (rush and blitz from the defense's side)
- **Learning objectives:**
  - Explain five-, six-, and seven-man protections; slide, man (BOB), half-slide, max protect.
  - Define RB/TE protection roles: check-release, chip.
  - Explain hot routes and sight adjustments when rushers outnumber blockers.
  - Connect Mike ID to the protection call.
  - Describe pocket geometry: depth, launch point, step-up; vertical vs jump sets.
  - Read protection metrics: pressure rate, time to throw.
- **Key terms introduced:** slide protection; man protection (BOB); half-slide; max protect; chip; check-release; hot route; sight adjust; free rusher; pocket; launch point; vertical set; jump set; time to throw; pressure rate
- **Diagrams:**
  - [S] Half-slide vs four-man rush
  - [A] Six-man protection; RB picks up a blitzing LB (frame strip)
  - [S] Five blockers vs six rushers -> hot throw
  - [T] Pocket shape over time from tracking data (convex hull of OL), frame strip
  - [C] Sack rate vs time to throw, team-season scatter
- **Team / era examples:** Patriots protection calls; 2022 Bengals OL vs Chiefs; Eagles OL (Kelce, Johnson)
- **Watch for this on Sunday:** Rushers vs blockers: right after the snap count rushers and blockers; if one came free, guess who owned him.

#### 04-03 The Quick Game: Slant-Flat, Stick, Snag, and Getting the Ball Out

- **Slug:** `04-03-quick-game` | **Level:** 3 | **Est. length:** 12 pp
- **Prerequisites:** 04-01, 04-02
- **Learning objectives:**
  - Explain why quick game exists: beats pressure, keeps the offense on schedule, extends the run game.
  - Diagram slant-flat, stick, snag, spacing, speed out, double slants, hitch-seam.
  - Use receiver leverage (inside/outside) to make a pre-snap decision.
  - Recognise quick game as the answer to press and blitz.
- **Key terms introduced:** quick game; slant-flat; stick; snag; spacing; speed out; double slants; hitch-seam; leverage (inside / outside); pre-snap read; rhythm throw
- **Diagrams:**
  - [S] Stick vs the flat defender
  - [A] Slant-flat high-low read (frame strip)
  - [S] Snag triangle
  - [S] Speed out
  - [A] Quick game vs a five-man pressure, ball out in 2.1s (frame strip)
- **Team / era examples:** Walsh 49ers; Brady Patriots; Payton/Brees Saints; Chiefs Kelce/quick game 2022-24
- **Watch for this on Sunday:** One-two-throw: stopwatch time to throw on quick game; under ~2.5s?

#### 04-04 Dropback Concepts: Smash, Flood, Mesh, Levels, Dagger, and Four Verticals

- **Slug:** `04-04-dropback-concepts` | **Level:** 3 | **Est. length:** 18 pp
- **Prerequisites:** 04-03
- **Forward references (flag in text):** 08-01 (concept vs coverage); 06-03 (four verts vs Cover 3)
- **Learning objectives:**
  - Diagram and explain smash, flood (sail), levels, mesh, drive, shallow cross, curl-flat, dagger, Y-cross, four verticals, post-wheel, yankee.
  - Classify each as vertical stretch, horizontal stretch, triangle, or man-beater.
  - Walk the QB's progression for each.
  - Explain tags and route conversions (break differently vs man and zone).
  - Forward-reference the coverage matchups (08-01).
- **Key terms introduced:** pass concept; smash; flood (sail); levels; mesh; drive (concept); shallow cross; curl-flat; dagger; Y-cross; four verticals; post-wheel; yankee; man-beater; route conversion; triangle read
- **Diagrams:**
  - [S] Concept plates (12) in consistent style with numbered progressions
  - [A] Four verticals vs generic deep defenders (frame strip)
  - [A] Mesh vs man: the rub (frame strip)
  - [C] Pass EPA heatmap by target depth x field width
- **Team / era examples:** Air Raid mesh and Y-cross (Leach); Patriots option/choice concepts; McVay yankee; Chiefs four verts variants
- **Watch for this on Sunday:** Name the concept: on replays, find two-receiver combinations and name the stretch.

#### 04-05 Play-Action, Bootlegs, and Screens

- **Slug:** `04-05-play-action-boots-screens` | **Level:** 3 | **Est. length:** 14 pp
- **Prerequisites:** 04-04, 03-02
- **Learning objectives:**
  - Explain why play-action works (run-fit triggers) and the data finding that it does not require a successful run game.
  - Distinguish under-center vs shotgun play-action, boot, naked, keeper, leak, shot plays.
  - Diagram RB slow screen, bubble, tunnel, jailbreak, TE screen, middle screen.
  - Explain screen timing, OL release, and why screens punish pressure.
  - Compare team play-action rates and efficiency with data.
- **Key terms introduced:** play-action; bootleg; naked bootleg; keeper; leak; shot play; screen; slow screen (RB screen); bubble screen; tunnel screen; jailbreak screen; swing route
- **Diagrams:**
  - [A] Wide-zone play-action boot: LBs step up, crosser opens (frame strip)
  - [S] Naked boot
  - [S] RB slow screen
  - [S] Tunnel screen
  - [S] Bubble screen
  - [C] EPA/dropback with vs without play-action by team (FTN/nflverse)
- **Team / era examples:** 2018 Rams (Goff play-action); Kubiak/Shanahan boots; Chiefs screen game; Ben Baldwin's play-action research
- **Watch for this on Sunday:** Watch the linebackers' feet: on play-action, did they step forward? How many yards did the crosser gain?

#### 04-06 Run-Pass Options: Plays That Are Two Plays

- **Slug:** `04-06-rpos` | **Level:** 3 | **Est. length:** 13 pp
- **Prerequisites:** 04-05, 03-04
- **Forward references (flag in text):** 05-05 (fits vs RPO); 08-02 (RPOs as constraints); 11-03 (college lineage)
- **Learning objectives:**
  - Define the RPO and distinguish it from play-action and from the option.
  - Diagram pre-snap (box-count) and post-snap (read-a-defender) RPOs: bubble, glance, stick, slant, pop pass.
  - Explain the NFL ineligible-downfield rule and how it limits RPOs vs college.
  - Identify the apex/overhang defender as the usual read.
  - Preview defensive answers.
- **Key terms introduced:** RPO (run-pass option); pre-snap RPO; post-snap RPO; apex (overhang) defender; glance RPO; bubble RPO; illegal man downfield; pop pass; packaged play
- **Diagrams:**
  - [A] Inside zone + glance RPO reading the LB, both branches (frame strips)
  - [S] Bubble RPO by box count
  - [S] Slant RPO
  - [S] Ineligible-downfield limit: NFL 1 yard vs college
- **Team / era examples:** 2017 Eagles (Foles, Super Bowl LII); Chiefs RPOs; Oregon / Auburn / Baylor college roots; Jalen Hurts' Eagles
- **Watch for this on Sunday:** Is he reading you? At the mesh point, find the defender the QB is looking at.

#### 04-07 Quarterback Play: Progressions, Eyes, the Pocket, and the Scramble Drill

- **Slug:** `04-07-quarterback-play` | **Level:** 4 | **Est. length:** 15 pp
- **Prerequisites:** 04-04, 04-02
- **Forward references (flag in text):** 06-06 (reading disguise); 14-01 (QB value)
- **Learning objectives:**
  - Map the QB's process: ID, protection, shell -> key -> progression.
  - Explain eye manipulation of safeties (look-offs).
  - Describe pocket movement: climb, slide, escape, throwaway.
  - Explain scramble-drill rules and off-script play.
  - Profile QB styles using time to throw, aDOT, CPOE, and EPA.
  - Explain why QBs dominate value (forward ref 14-01).
- **Key terms introduced:** look-off; climbing the pocket; throwaway; scramble drill; off-script (off-schedule) play; anticipation throw; checkdown; CPOE (completion % over expected)
- **Diagrams:**
  - [A] Progression read with numbered reads lighting up (frame strip)
  - [A] Safety look-off: QB eyes hold the safety, throws opposite (frame strip)
  - [S] Scramble-drill rules plate
  - [C] QB style map: time to throw vs aDOT, coloured by EPA/dropback
- **Team / era examples:** Tom Brady; Peyton Manning; Patrick Mahomes (off-script); Josh Allen; Joe Burrow; Brock Purdy (system QB debate)
- **Watch for this on Sunday:** Watch the eyes: on replays count how many reads the QB got through before throwing.

#### 04-08 Offensive Systems and Play-Calling Languages

- **Slug:** `04-08-offensive-systems-and-languages` | **Level:** 4 | **Est. length:** 14 pp
- **Prerequisites:** 04-07
- **Forward references (flag in text):** 11-02 / 11-03 (history of these systems); Part 12 (case studies)
- **Learning objectives:**
  - Distinguish the major families: West Coast, Air Coryell, Erhardt-Perkins, run-and-shoot, Air Raid, Shanahan/McVay, spread-option.
  - Explain how each names plays and why that matters for installation and tempo.
  - Map coaching trees onto 2025 NFL staffs.
  - Recognise a system's fingerprints on film.
- **Key terms introduced:** offensive system; West Coast offense; Air Coryell; Erhardt-Perkins; run-and-shoot; choice route; Air Raid; concept-based terminology; coaching tree
- **Diagrams:**
  - [S] One concept named three ways (WCO / Coryell / EP)
  - [S] Coaching-tree network, 1970-2025
  - [S] Run-and-shoot base with choice routes
  - [S] Air Raid mesh and Y-cross from 2x2
- **Team / era examples:** Walsh; Coryell; Erhardt/Perkins -> Parcells -> Belichick/Weis/McDaniels; Mouse Davis & June Jones; Mumme & Leach; Shanahan -> McVay / LaFleur / McDaniel / Kubiak
- **Watch for this on Sunday:** Fingerprint the system: chart under-center %, motion, condensed sets, empty for one team; guess its tree.

### Part 05: Defensive Fronts and Run Defense

_Levels 3-4._ The defense's side of Part 3: how linemen align and play, the even and odd front families, linebackers, and the integrated system of run fits that makes every gap someone's job.

#### 05-01 Defensive Line Play: Techniques, One-Gap and Two-Gap

- **Slug:** `05-01-dl-techniques-and-gap-control` | **Level:** 3 | **Est. length:** 12 pp
- **Prerequisites:** 03-01, 02-06
- **Learning objectives:**
  - Map DL roles to techniques: nose (0/1), 3-technique, 4i, 5-technique, wide-9, edge.
  - Distinguish one-gap (penetrate) and two-gap (control and read) play.
  - Explain reactions to down blocks, reaches, and double teams.
  - Define setting the edge and contain.
  - Describe line movement: slants and angles.
- **Key terms introduced:** one-gap; two-gap; 3-technique; 4i technique; 5-technique; wide-9; set the edge; contain; penetration; slant (line movement); angle (line movement)
- **Diagrams:**
  - [S] Technique map with archetype silhouettes
  - [A] Two-gap nose controls the center then sheds either way (frame strip)
  - [A] One-gap 3-tech penetrates (frame strip)
  - [S] Slant and angle movements
- **Team / era examples:** Vince Wilfork (two-gap nose); Warren Sapp / Aaron Donald (3-tech); Reggie White; Wide-9 under Jim Washburn / Jim Schwartz
- **Watch for this on Sunday:** Find the 3-technique: before the snap find the DT outside the guard; which way did the run go?

#### 05-02 Even Fronts: 4-3 Over, Under, Wide-9, and the 46 Bear

- **Slug:** `05-02-even-fronts` | **Level:** 3 | **Est. length:** 13 pp
- **Prerequisites:** 05-01
- **Learning objectives:**
  - Diagram 4-3 Over and Under and their strength rules.
  - Explain the wide-9 trade-off (pass rush for run lanes).
  - Diagram the 46 / bear front and why covering the center and both guards wrecks blocking schemes.
  - Show how even fronts adjust from 21 to 11 personnel.
  - Identify the front from the broadcast angle.
- **Key terms introduced:** even front; 4-3 Over; 4-3 Under; 46 defense; bear front
- **Diagrams:**
  - [S] 4-3 Over and Under plates
  - [A] Bear front vs I-form: nobody left to block the backers (frame strip)
  - [S] Wide-9 rush lanes
  - [S] Under front vs 11 personnel
- **Team / era examples:** Buddy Ryan's 1985 Bears; Pete Carroll's Seattle Under; Jim Schwartz's 2017 Eagles; Lovie Smith's Bears
- **Watch for this on Sunday:** Over or under? Find the 3-tech relative to the TE before each snap.

#### 05-03 Odd and Hybrid Fronts: 3-4, Okie, Tite, and Modern Nickel Fronts

- **Slug:** `05-03-odd-and-hybrid-fronts` | **Level:** 3 | **Est. length:** 14 pp
- **Prerequisites:** 05-02
- **Forward references (flag in text):** 11-01 / 11-02 (3-4 history)
- **Learning objectives:**
  - Diagram the 3-4 Okie and contrast two-gap vs one-gap 3-4s.
  - Explain the tite (mint) front and why it walls off inside runs vs spread offenses.
  - Diagram nickel fronts: 4-2-5, 3-3-5, 2-4-5.
  - Explain why front labels blur (stand-up edges, 'multiple' defenses).
  - Show how a front chooses to defend inside vs outside zone.
- **Key terms introduced:** odd front; 3-4 Okie; tite front (mint); 4-2-5; 3-3-5; 2-4-5; stand-up edge (outside linebacker); multiple (hybrid) defense; reduced front
- **Diagrams:**
  - [S] Okie plate
  - [A] Tite front vs inside zone (frame strip)
  - [S] 4-2-5 vs 2x2
  - [S] 2-4-5
  - [A] Same personnel, two fronts: stand-up edge puts hand down (frame strip)
- **Team / era examples:** Bum Phillips / Fritz Shurmur early 3-4; Wade Phillips one-gap 3-4 (J.J. Watt Texans, 2015 Broncos); Fangio tite (2018 Bears, 2024 Eagles); Kirby Smart's Georgia
- **Watch for this on Sunday:** Count the hands down: three, four, or five? Who is standing on the edge?

#### 05-04 Linebackers: Keys, Flow, and the Hardest Job on the Field

- **Slug:** `05-04-linebackers-and-second-level` | **Level:** 3 | **Est. length:** 12 pp
- **Prerequisites:** 05-02, 04-05
- **Learning objectives:**
  - Explain alignments (stack, apex, walk-out) and keys (guards, near back).
  - Explain flow (fast, slow) and fit actions: fill, scrape, plug, run-through.
  - Describe LB coverage jobs (hook/curl, man on backs, rat/hole) and pressure roles.
  - Explain the decline of the Sam and the rise of safety-sized linebackers.
  - Describe the green-dot communicator's job.
- **Key terms introduced:** stack alignment; apex alignment; walk-out; key (read key, defense); flow (fast / slow); fill; scrape; plug; run-through; hook / curl defender
- **Diagrams:**
  - [A] LB key read: guard pulls, Mike flows (frame strip)
  - [S] Apex alignment vs 2x2
  - [S] Scrape vs zone read
  - [A] LB conflict on play-action, revisited from 04-05 (frame strip)
- **Team / era examples:** Ray Lewis; Luke Kuechly; Bobby Wagner; Fred Warner; Roquan Smith
- **Watch for this on Sunday:** Mirror the Mike: watch only the Mike for 10 snaps. First step forward or back?

#### 05-05 Run Fits: Gap Integrity, Force, Spill, and Box Math

- **Slug:** `05-05-run-fits-and-box-math` | **Level:** 4 | **Est. length:** 15 pp
- **Prerequisites:** 05-04, 03-04
- **Learning objectives:**
  - Explain run fits and gap integrity: every gap owned.
  - Distinguish force/contain, spill vs box (squeeze), and the alley player.
  - Explain the plus-one principle and how safety rotation adds a fitter.
  - Show fits vs zone, power, and zone read (gap exchange).
  - Explain two-high light-box run defense and its costs.
  - Evaluate box count vs EPA with data.
- **Key terms introduced:** run fit; gap integrity; force (defender); spill; box technique (squeeze); alley player; plus-one; gap exchange; overhang defender
- **Diagrams:**
  - [S] Full 11-man fit chart vs power
  - [A] Spill vs box comparison on the same kick-out (frame strips)
  - [S] Plus-one with a rotated safety
  - [A] Scrape exchange vs zone read (frame strip)
  - [C] EPA/rush by defenders in the box
- **Team / era examples:** Fangio light-box philosophy; Ravens 2019 vs light boxes; 2024 Eagles run game vs two-high
- **Watch for this on Sunday:** Who's the force? Find the outermost defender each side pre-snap; did the run bounce?

### Part 06: Pass Coverage

_Levels 3-5._ From zone vocabulary to the modern disguise game. Each coverage chapter has the same spine: structure, strengths, holes, pre-snap tells, post-snap tells, and which teams made it famous.

#### 06-01 Coverage Fundamentals: Zones, Leverage, and Reading the Shell

- **Slug:** `06-01-coverage-fundamentals` | **Level:** 3 | **Est. length:** 14 pp
- **Prerequisites:** 04-04, 02-06
- **Forward references (flag in text):** 09-03 (contact rules)
- **Learning objectives:**
  - Name the zones: flat, curl, hook, hole, deep third, deep half, deep quarter.
  - Define press, off, bail, cushion, trail, and eye discipline.
  - Distinguish spot-drop zone, pattern-match, and man.
  - Read the shell: MOFC vs MOFO, safety depth and width tells.
  - Decode the Cover 0-6 numbering and its inconsistencies across teams.
  - Connect coverage rules to the 5-yard contact rule (forward ref 09-03).
- **Key terms introduced:** flat zone; curl zone; hook zone; hole (rat) zone; deep third; deep half; deep quarter; press; off coverage; bail; cushion; trail technique; landmark; spot-drop zone; pattern matching; MOFC (middle of field closed); MOFO (middle of field open); coverage numbering (Cover 0-6)
- **Diagrams:**
  - [S] Zone map grid
  - [S] Press vs off vs bail alignment
  - [S] MOFC vs MOFO plates
  - [A] Spot-drop vs pattern-match vs the same routes, side by side (frame strips)
- **Team / era examples:** Seattle press Cover 3; Tampa 2 Bucs; Fangio quarters
- **Watch for this on Sunday:** One or two? At the snap call MOFC or MOFO; one second later say whether it stayed.

#### 06-02 Man Coverage: Cover 0, Cover 1, Robbers, and Brackets

- **Slug:** `06-02-man-coverage` | **Level:** 3 | **Est. length:** 13 pp
- **Prerequisites:** 06-01
- **Learning objectives:**
  - Diagram Cover 1 (man-free), Cover 1 robber/rat, and Cover 0.
  - Explain man techniques (press-man, off-man, trail) and inside help.
  - Explain banjo/combo vs stacks and bunches; brackets on stars; shadow corners.
  - Explain when defenses prefer man (third down, red zone, talent).
  - Revisit man-beaters (mesh, rubs, slants, double moves).
- **Key terms introduced:** Cover 1 (man-free); Cover 0; robber; lurk; banjo; combo coverage; bracket; shadow corner; inside help
- **Diagrams:**
  - [S] Cover 1 vs 2x2
  - [S] Cover 0 vs empty
  - [A] Banjo vs stack release (frame strip)
  - [S] Bracket on #1 in 3x1
  - [A] Cover 1 rat robbing a dig (frame strip)
- **Team / era examples:** Patriots Cover 1 & brackets (Ty Law, Stephon Gilmore); Spagnuolo's Cover 0; Darrelle Revis; Seattle's Richard Sherman (contrast: zone corner)
- **Watch for this on Sunday:** Who's facing the QB? Man defenders turn to the receiver; zone defenders read the QB.

#### 06-03 Cover 3: Sky, Buzz, Cloud, and Seattle's Match Version

- **Slug:** `06-03-cover-3-family` | **Level:** 3 | **Est. length:** 13 pp
- **Prerequisites:** 06-01
- **Learning objectives:**
  - Diagram Cover 3 base (three deep, four under) and the sky, buzz, cloud rotations.
  - Explain Cover 3's strengths (eight-man front) and holes (seams, curl-flat, flood).
  - Explain Cover 3 match and how it handles four verticals.
  - Recognise Cover 3 pre-snap and post-snap.
- **Key terms introduced:** Cover 3; sky rotation; buzz rotation; cloud (corner) rotation; seam-flat defender; curl-flat defender; Cover 3 match
- **Diagrams:**
  - [S] Cover 3 sky vs 2x2
  - [S] Buzz
  - [S] Cloud
  - [A] Four verticals vs spot-drop Cover 3: the seam opens (frame strip)
  - [A] Four verticals vs Cover 3 match: seam carried (frame strip)
- **Team / era examples:** Pete Carroll's 2012-2015 Seahawks (Sherman, Thomas, Chancellor); Gus Bradley; Dan Quinn
- **Watch for this on Sunday:** Count deep defenders one second after the snap: three means a Cover 3 family call.

#### 06-04 Cover 2 and Tampa 2

- **Slug:** `06-04-cover-2-and-tampa-2` | **Level:** 3 | **Est. length:** 12 pp
- **Prerequisites:** 06-03
- **Learning objectives:**
  - Diagram Cover 2 zone (two halves, five under) and hard/squat corners.
  - Explain Tampa 2 (Mike runs the deep middle) and why it existed.
  - Diagram 2-Man (two-deep, man under).
  - Locate Cover 2's holes: hole shot, smash corner, deep middle, sideline hole.
  - Explain why classic Tampa 2 faded and what survived.
- **Key terms introduced:** Cover 2; hard (squat) corner; hole shot; Tampa 2; 2-Man (Cover 5)
- **Diagrams:**
  - [S] Cover 2 vs 2x2
  - [A] Tampa 2: Mike carries the seam (frame strip)
  - [S] 2-Man
  - [A] Smash vs Cover 2 (frame strip)
- **Team / era examples:** Tony Dungy / Monte Kiffin 2002 Bucs; Dungy's 2006 Colts; Lovie Smith's 2006 Bears; Bud Carson's 1970s Steelers Cover 2
- **Watch for this on Sunday:** Squat-corner spotter: corners at 5-7 yards, outside leverage, not bailing -> think Cover 2.

#### 06-05 Quarters and the Two-High Match Family: Cover 4, Cover 6, Palms

- **Slug:** `06-05-quarters-and-match` | **Level:** 4 | **Est. length:** 16 pp
- **Prerequisites:** 06-04, 05-05
- **Forward references (flag in text):** 12-08 (Fangio case study)
- **Learning objectives:**
  - Diagram Cover 4 (quarters) and its run support (safeties fit off #2).
  - Explain match rules: MOD, MEG, read-the-#2 safety.
  - Diagram Cover 6 (quarter-quarter-half) and Palms / 2-read (trap).
  - Explain why two-high match coverage spread through the NFL 2019-2023.
  - Identify the weaknesses: light-box runs, flood from boot, RB wheel.
- **Key terms introduced:** quarters (Cover 4); Cover 6; Palms (2-read, trap); MOD (man only deep); MEG (man everywhere he goes); read safety
- **Diagrams:**
  - [S] Cover 4 vs 2x2 with match responsibilities
  - [A] Quarters safety fits the run (frame strip)
  - [S] Cover 6 vs 3x1
  - [A] Palms: corner traps the out (frame strip)
  - [C] League two-high rate by season (charting data where available)
- **Team / era examples:** Saban/Belichick rip-liz match; Fangio 2018 Bears; Brandon Staley 2020 Rams; Fangio 2024 Eagles; Michigan State / Iowa quarters
- **Watch for this on Sunday:** Two-high, now what? Watch both safeties' first steps: backpedal, downhill, or rotate?

#### 06-06 Disguise, Rotation, and Split-Field Coverage

- **Slug:** `06-06-disguise-rotation-and-split-field` | **Level:** 5 | **Est. length:** 16 pp
- **Prerequisites:** 06-05, 02-05
- **Forward references (flag in text):** 13-05 (tracking data); 12-08 (Macdonald case study)
- **Learning objectives:**
  - Explain disguise and post-snap rotation (two-high to one-high, one-high to two-high).
  - List tells: safety depth/width, corner leverage, weight, timing of movement.
  - Explain split-field coverage and 3x1 checks (poach, solo, stubbie).
  - Explain how late rotation forces post-snap reading and how offenses respond (motion, tempo, hard counts).
  - Measure safety movement around the snap with tracking data.
- **Key terms introduced:** disguise; post-snap rotation; split-field coverage; Cover 7 (match family); poach; 3x1 check (solo / stubbie); late rotation
- **Diagrams:**
  - [A] Two-high shell rotates to Cover 3 robber at the snap (frame strip)
  - [A] One-high spins to Cover 2 (frame strip)
  - [S] Split-field Cover 6 vs 2x2
  - [S] Poach vs 3x1
  - [T] Safety depth and lateral position from snap-30 to snap+20 frames (BDB tracking)
  - [C] Pre-snap shell vs post-snap coverage agreement rate by team
- **Team / era examples:** Fangio 2024 Eagles; Mike Macdonald 2023 Ravens / 2024-25 Seahawks; Brian Flores Vikings
- **Watch for this on Sunday:** Call it twice: name the coverage pre-snap and again one second after; log how often the defense lied.

### Part 07: Pressure: Rush, Blitz, and Simulated Pressure

_Levels 3-4._ How defenses attack the quarterback: winning one-on-one, adding rushers, and the modern art of making four rushers look like six.

#### 07-01 The Pass Rush: Moves, Stunts, and Why Pressure Beats Sacks

- **Slug:** `07-01-pass-rush` | **Level:** 3 | **Est. length:** 12 pp
- **Prerequisites:** 04-02, 05-01
- **Learning objectives:**
  - Explain get-off, the rush arc, and the main moves (speed, bull, long arm, swim, rip, spin, counters).
  - Diagram stunts/games: T-E, E-T, loop, twist.
  - Explain rush lanes and contain vs mobile QBs.
  - Explain why pressure is more stable than sacks and how QBs drive sack rate.
  - Use pass-rush win rate and time-to-pressure metrics.
- **Key terms introduced:** get-off; speed rush; bull rush; long arm; swim move; rip move; spin move; stunt (game); T-E stunt; E-T stunt; rush lane; pressure; sack; QB hit / hurry; pass rush win rate (PRWR)
- **Diagrams:**
  - [S] Rush-move sequence frames (6 mini panels)
  - [A] T-E stunt vs slide protection (frame strip)
  - [S] Rush lanes vs a mobile QB
  - [C] Sack rate vs pressure rate, team-season scatter
- **Team / era examples:** Lawrence Taylor; Reggie White; Aaron Donald; T.J. Watt; Myles Garrett; Micah Parsons
- **Watch for this on Sunday:** Count the seconds: stopwatch from snap to first pressure; note whether the ball was already out.

#### 07-02 Blitzing: Numbers, Overloads, A-Gap Mugs, and Cover 0

- **Slug:** `07-02-blitz-and-man-pressure` | **Level:** 3 | **Est. length:** 13 pp
- **Prerequisites:** 07-01, 06-02
- **Learning objectives:**
  - Define a blitz (5+ rushers) versus a four-man rush.
  - Do blitz math: rushers vs protectors, who is free, where the hot throw goes.
  - Diagram man pressures: Cover 1 blitz, Cover 0, overloads.
  - Explain double A-gap mugs and why they break protection rules.
  - Analyse blitz rate vs EPA allowed (high variance, situational value).
- **Key terms introduced:** blitz; four-man rush; five-man pressure; overload blitz; double A-gap mug; Cover 0 blitz; Cover 1 blitz; unblocked rusher
- **Diagrams:**
  - [A] Overload blitz vs half-slide, RB picks wrong man (frame strip)
  - [S] Double A-gap mug: three post-snap variants from one look
  - [S] Cover 0 blitz vs empty -> hot throw
  - [C] Blitz rate vs EPA/dropback allowed by team
- **Team / era examples:** Buddy Ryan; Rex Ryan; Steve Spagnuolo (2007 Giants, Chiefs Cover 0); Brian Flores (Dolphins, Vikings 2024)
- **Watch for this on Sunday:** Count the rushers: four or more? If more, predict a quick throw and to which side.

#### 07-03 Zone Blitzes, Fire Zones, and Simulated Pressure

- **Slug:** `07-03-zone-blitz-and-simulated-pressure` | **Level:** 4 | **Est. length:** 14 pp
- **Prerequisites:** 07-02, 06-03
- **Forward references (flag in text):** 12-08 (Macdonald)
- **Learning objectives:**
  - Explain the zone-blitz idea: rush an unexpected defender, drop a lineman, play three-deep three-under.
  - Diagram fire-zone variants and their hot-zone holes.
  - Define simulated pressure (creeper): four rushers from unexpected places, seven in coverage.
  - Explain how sim pressure wins one-on-ones by defeating protection rules without sacrificing coverage.
  - Narrate the protection-vs-pressure chess: Mike ID, slide direction, hot throws.
- **Key terms introduced:** zone blitz; fire zone (3-under 3-deep); simulated pressure (creeper); dropper (DL in coverage); pressure look
- **Diagrams:**
  - [A] Fire zone vs 2x2: DE drops to the hook (frame strip)
  - [A] Creeper from nickel (frame strip)
  - [S] Protection bust: slide toward the threat, rush from the other side
  - [S] 1990s Steelers zone-blitz plate
- **Team / era examples:** Dick LeBeau (Bengals origin, 'Blitzburgh' Steelers); Dom Capers; Mike Macdonald Ravens/Seahawks; Brian Flores 2024 Vikings; Spagnuolo
- **Watch for this on Sunday:** Who dropped? After the snap find the lineman who dropped into coverage, and who replaced him as a rusher.

### Part 08: The Chess Match

_Levels 4-5._ Offense and defense together: which concepts beat which coverages, how plays are sequenced to set each other up, how a week of game-planning works, and how adjustments and tempo play out on Sunday.

#### 08-01 What Beats What: Pass Concepts Versus Coverages

- **Slug:** `08-01-concepts-versus-coverages` | **Level:** 4 | **Est. length:** 16 pp
- **Prerequisites:** 06-06, 04-04, 06-02
- **Learning objectives:**
  - Build the concept x coverage matrix (smash vs Cover 2, four verts and flood vs Cover 3, dagger vs quarters, mesh vs man, ...).
  - Explain why 'beaters' are probabilistic given match rules and disguise.
  - Explain two-way concepts with a man answer and a zone answer built in.
  - Show the defense's counters (Cover 3 match vs four verts, Palms vs smash).
  - Practise identify-then-predict on animated plays.
- **Key terms introduced:** coverage beater; two-way concept; alert (shot alert)
- **Diagrams:**
  - [S] Concept x coverage matrix, colour-coded by expected advantage
  - [A] Smash vs Cover 2 (frame strip)
  - [A] Flood vs Cover 3 (frame strip)
  - [A] Dagger vs quarters (frame strip)
  - [A] Mesh vs Cover 1 (frame strip)
  - [A] Smash vs Palms: the defense wins (frame strip)
- **Team / era examples:** Chiefs' 3rd-and-15 'Jet Chip Wasp' in Super Bowl LIV; Malcolm Butler's Super Bowl XLIX interception vs a stack/pick
- **Watch for this on Sunday:** Predict the open man: once you ID the coverage at the snap, name who will be open before the throw.

#### 08-02 Constraint Theory: How Plays Talk to Each Other

- **Slug:** `08-02-constraint-theory-and-sequencing` | **Level:** 4 | **Est. length:** 13 pp
- **Prerequisites:** 08-01, 03-05, 04-05
- **Learning objectives:**
  - Explain base plays vs constraint plays and the 'illusion of complexity'.
  - Explain sequencing: setting up a counter, tendency breakers, play-action off the base run.
  - Explain self-scouting and formation tells.
  - Show the defense's version: one pressure look, several coverages.
  - Find a team's tendencies by formation/personnel in data.
- **Key terms introduced:** base play; constraint play; illusion of complexity; sequencing; tendency; tendency breaker; self-scout; tell
- **Diagrams:**
  - [S] Constraint tree: wide zone -> boot / naked / keeper / counter
  - [S] One formation, four plays (Shanahan-style plate)
  - [C] Tendency table: formation x personnel -> pass rate for one team
- **Team / era examples:** Shanahan wide-zone family; Wing-T series; Reid's Chiefs; Ben Johnson's Lions sequencing
- **Watch for this on Sunday:** Call the follow-up: after a big run from a look, predict play-action from the same look within the next few snaps.

#### 08-03 The Game Plan: A Week Inside an NFL Building

- **Slug:** `08-03-game-planning-week` | **Level:** 4 | **Est. length:** 14 pp
- **Prerequisites:** 08-02
- **Forward references (flag in text):** 12-02 (Belichick case study)
- **Learning objectives:**
  - Walk through a game week: film, install, situational practice days.
  - Explain call sheets organised by situation and the opening script.
  - Explain matchup hunting and 'take away their best thing'.
  - Explain how a staff scouts an opposing coordinator and QB.
  - Describe tendency reports and the analytics staff's role.
- **Key terms introduced:** game plan; opening script; situational call sheet; matchup (mismatch); tendency report; game-plan package
- **Diagrams:**
  - [S] Annotated call-sheet mock-up
  - [S] Game-week calendar
  - [C] Matchup heatmap for a sample game (slot vs nickel, TE vs LB, etc.)
  - [S] 'Take away the best thing': normal alignment vs game-plan alignment
- **Team / era examples:** Belichick: Giants vs Bills (Super Bowl XXV), Patriots vs Rams (Super Bowls XXXVI and LIII); Walsh's scripted 15; Andy Reid's play sheet
- **Watch for this on Sunday:** Script detector: watch the first 15 offensive plays; list anything you haven't seen from this team before.

#### 08-04 In-Game Adjustments, Tempo, and the Sideline Battle

- **Slug:** `08-04-in-game-adjustments-and-tempo` | **Level:** 4 | **Est. length:** 13 pp
- **Prerequisites:** 08-03
- **Learning objectives:**
  - Explain between-series adjustments (tablets, coaching booth) and halftime adjustments.
  - Explain tempo and no-huddle: freezing substitutions and simplifying the defense.
  - Explain defensive answers to tempo (simplified calls, check-with-me).
  - Describe coordinator-vs-coordinator 'call after the call'.
  - Test the halftime-adjustment narrative with second-half data.
- **Key terms introduced:** tempo; hurry-up offense; sugar huddle; substitution freeze; halftime adjustment; coaching booth
- **Diagrams:**
  - [C] Seconds between snaps by team (tempo distribution)
  - [S] Substitution-matching rule timeline
  - [S] Before/after adjustment example as frame pairs
- **Team / era examples:** Bills K-Gun; Peyton Manning's no-huddle; Chip Kelly's 2013 Eagles; Chiefs' second-half motion TDs in Super Bowl LVII
- **Watch for this on Sunday:** Adjustment hunter: list what changed after halftime (personnel, motion, coverage, pressure).

### Part 09: Special Teams and the Rules That Shape Strategy

_Levels 2-3._ The third phase and the rulebook. Placed before situational football because fourth-down, end-of-half, and red-zone decisions depend on kicking ranges and on the contact/penalty rules.

#### 09-01 Field Goals, Extra Points, and the Punting Game

- **Slug:** `09-01-kicking-and-punting` | **Level:** 2 | **Est. length:** 12 pp
- **Prerequisites:** 01-02, 01-03
- **Learning objectives:**
  - Explain FG/PAT mechanics: snap-hold-kick timing, protection, block units.
  - Compute FG distance from the line of scrimmage and reason about range (kicker, weather, altitude).
  - Explain the 2015 PAT change and its effect on two-point attempts.
  - Diagram punt formations (shield/spread), gunners, vices; directional and coffin-corner punting; fair catch and downing.
  - Explain fakes and why they are rare.
  - Show FG accuracy by distance across eras.
- **Key terms introduced:** field goal range; snap-hold-kick; shield (spread) punt; vice (jammer); fair catch; coffin-corner punt; touchback; net punting average; fake punt / fake field goal
- **Diagrams:**
  - [S] FG formation and protection
  - [A] Shield punt and coverage lanes (frame strip)
  - [C] FG% by distance by era
  - [C] Punt landing spot heatmap
- **Team / era examples:** Justin Tucker; Brandon Aubrey's long-range kicking; Notable fake punts
- **Watch for this on Sunday:** Range finder: on every 4th down, predict go / punt / FG before the offense lines up.

#### 09-02 Kickoffs, Returns, and the Dynamic Kickoff

- **Slug:** `09-02-kickoffs-and-returns` | **Level:** 2 | **Est. length:** 11 pp
- **Prerequisites:** 09-01, 07-02
- **Learning objectives:**
  - Explain the traditional kickoff and why the league kept changing it (injury data).
  - Explain the 2024 dynamic kickoff (setup zone, landing zone) and the 2025 adjustments.
  - Explain the strategic consequences: return rates, squibs, landing-zone choices, touchback math.
  - Explain onside kicks under current rules.
  - Describe return schemes at a high level.
- **Key terms introduced:** kickoff; dynamic kickoff; landing zone; setup zone; onside kick; squib kick; kick coverage unit; return unit
- **Diagrams:**
  - [S] Dynamic kickoff alignment plate
  - [A] Dynamic kickoff from kick to tackle (frame strip)
  - [S] Old vs new kickoff side by side
  - [C] Return rate and average starting field position by season, 2019-2025
- **Team / era examples:** League-wide 2024 vs 2025 return behaviour; Teams that exploited landing-zone rules
- **Watch for this on Sunday:** Field-position ledger: log each kickoff's starting yard line; compute the game average.

#### 09-03 The Rulebook as Strategy: Contact Rules, Penalties, and Officiating

- **Slug:** `09-03-rules-that-shape-strategy` | **Level:** 3 | **Est. length:** 15 pp
- **Prerequisites:** 06-01, 04-06, 04-02
- **Forward references (flag in text):** 11-02 / 11-04 (rule changes in historical context); Appendix E (rule-change timeline)
- **Learning objectives:**
  - Explain the 5-yard contact zone, defensive holding, illegal contact, DPI and OPI, and their scheme consequences (spot foul, throwing deep for DPI).
  - Explain offensive holding, chop/cut-block legality, and ineligible-downfield enforcement.
  - Explain QB protection rules (roughing, sliding) and their effect on QB run games.
  - Explain free plays, challenges, and replay review.
  - Show penalty rates by type and crew, and how penalties enter EPA.
  - Summarise live rule debates (tush push, hip-drop tackle).
- **Key terms introduced:** illegal contact; defensive holding; offensive holding; defensive pass interference (DPI); offensive pass interference (OPI); spot foul; roughing the passer; unnecessary roughness; free play; coach's challenge; replay review; accept / decline (penalty); half the distance
- **Diagrams:**
  - [S] The 5-yard contact zone
  - [S] Pick-play legality within 1 yard
  - [S] DPI enforcement: NFL spot foul vs college 15-yard cap
  - [C] Penalty rates by type 2015-2025
  - [C] Accepted penalties per game by officiating crew
- **Team / era examples:** 2003 AFC Championship and the 2004 illegal-contact emphasis; 2018 NFC Championship no-call -> 2019 PI review experiment; 2024 hip-drop tackle ban; 2025 tush-push vote
- **Watch for this on Sunday:** Flag predictor: when a flag flies, guess the foul before the announcement and how it changes the series.

### Part 10: Situational Football

_Levels 3-4._ The same plays mean different things on 3rd & 8, at the 4-yard line, or with 1:12 left. This part teaches situations as the frame for everything before it.

#### 10-01 Down, Distance, and Field Zones

- **Slug:** `10-01-down-distance-and-field-zones` | **Level:** 3 | **Est. length:** 12 pp
- **Prerequisites:** 01-02, 08-02
- **Learning objectives:**
  - Explain early-down philosophy (first-down pass rate, the 'establish the run' debate).
  - Bucket second downs (and why 2nd & short is a shot down).
  - Define field zones: backed up, coming out, open field, fringe (four-down territory), plus territory.
  - Explain how play-calling changes by zone.
  - Read pass rate and EPA by down, distance, and yard line.
- **Key terms introduced:** early down; backed up; coming out; open field; four-down territory (fringe); plus territory; on schedule / behind schedule
- **Diagrams:**
  - [S] Field-zone map
  - [C] Pass-rate heatmap, down x distance
  - [C] EPA by yard line and down
- **Team / era examples:** 2018 Chiefs and Rams early-down passing; Lions 2023-24; Ravens 2019
- **Watch for this on Sunday:** Situation tag: before each snap tag the play with its situation bucket; compare your run/pass accuracy by bucket.

#### 10-02 Third Down: The Money Down

- **Slug:** `10-02-third-down` | **Level:** 3 | **Est. length:** 13 pp
- **Prerequisites:** 10-01, 07-03
- **Learning objectives:**
  - Bucket third downs (short, medium, long) with league conversion rates.
  - Explain offensive third-down concepts: sticks routes, man-beaters, long-yardage screens and draws.
  - Explain defensive third-down packages: sticks defense, sim pressure, Cover 0, rush three/drop eight, spy.
  - Explain why 'past the sticks' matters and when it doesn't.
- **Key terms introduced:** sticks route; third-down package; rush three, drop eight; spy (QB spy); draw play
- **Diagrams:**
  - [S] 3rd & 7 concept vs Cover 1
  - [S] Rush three / drop eight
  - [S] QB spy
  - [A] 3rd-and-long draw vs dime (frame strip)
  - [C] Conversion rate by distance and play type
- **Team / era examples:** Patriots' option routes (Welker, Edelman); Spagnuolo third-down pressure; Flores' third-down Cover 0
- **Watch for this on Sunday:** Past the sticks? Predict whether the target will be beyond the line to gain.

#### 10-03 Red Zone, Goal Line, and Short Yardage (Including the Tush Push)

- **Slug:** `10-03-red-zone-goal-line-and-short-yardage` | **Level:** 3 | **Est. length:** 14 pp
- **Prerequisites:** 10-02, 09-03, 03-04
- **Learning objectives:**
  - Explain the compressed field: why deep zones vanish and man/press increases.
  - Diagram red-zone concepts: fade, back-shoulder, rub/pick, slants, shovel, sprint-out.
  - Diagram goal-line personnel and fronts on both sides.
  - Explain the QB sneak and tush push mechanics, the 2005 push-the-runner rule change, and the ban debate.
  - Analyse red-zone TD rates and sneak success with data.
- **Key terms introduced:** compressed field; fade; back-shoulder throw; rub (pick) route; shovel pass; goal-line defense; QB sneak; tush push; assisting the runner (push rule)
- **Diagrams:**
  - [S] Red-zone field map with compressed zones
  - [A] Rub concept vs man near the goal line (frame strip)
  - [A] Tush push: formation and push (frame strip)
  - [S] Goal-line 6-2 and 5-3 defenses
  - [C] QB-sneak/tush-push success rate by team, 2021-2025
- **Team / era examples:** Eagles tush push (Hurts, Kelce, Johnson); Bills' Allen sneak; Brady sneak
- **Watch for this on Sunday:** Fade or rub? Inside the 10, predict the pass concept from receiver splits.

#### 10-04 The Clock, the Two-Minute Drill, and Fourth Down

- **Slug:** `10-04-clock-and-game-management` | **Level:** 4 | **Est. length:** 15 pp
- **Prerequisites:** 10-03, 09-01, 08-04
- **Forward references (flag in text):** 13-03 (win probability and the fourth-down model)
- **Learning objectives:**
  - Run a two-minute offense: sideline routes, spikes, timeouts, the 10-second runoff.
  - Run a four-minute offense: running inbounds, killing clock, the victory formation.
  - Make end-of-half decisions (points vs risk, FG range, Hail Mary, prevent).
  - Use fourth-down and two-point heuristics; explain the 2018-2025 aggression shift (math in 13-03).
  - Apply current overtime rules (playoff 2022 and regular season 2025) and their strategy.
- **Key terms introduced:** two-minute drill; spike; 10-second runoff; four-minute offense; victory formation (kneel-down); Hail Mary; prevent defense; go-for-it decision; two-point chart; overtime rules
- **Diagrams:**
  - [S] Annotated two-minute drive timeline
  - [S] Clock decision flowchart
  - [C] Fourth-down go rate by season 2010-2025
  - [C] Go rate by yards to go x field position
- **Team / era examples:** Chiefs-Bills '13 seconds' (Jan 2022) and the playoff OT change; Dan Campbell's Lions; Super Bowl LVIII overtime; Andy Reid clock-management critiques
- **Watch for this on Sunday:** Coach the clock: in the last two minutes of each half, predict timeouts, spikes, and kneels before they happen.

### Part 11: History: The Arms Race

_Levels 2-3._ A chronological retelling of how we got here, told as action and reaction: each offensive innovation, the defensive answer, and the rule changes that tilted the board. Earlier chapters already contain history sidebars; this part connects them into one story.

#### 11-01 From the Single Wing to the Dead-Ball Era (1906-1977)

- **Slug:** `11-01-single-wing-to-dead-ball-era` | **Level:** 2 | **Est. length:** 15 pp
- **Prerequisites:** 02-03, 06-04
- **Learning objectives:**
  - Trace the forward pass from legalisation (1906) to slow adoption.
  - Explain the single wing -> T-formation shift (1940 Bears 73-0).
  - Describe Paul Brown's innovations (playbooks, film study, messenger guards).
  - Describe Landry's 4-3 and Flex, Lombardi's sweep, Gillman's vertical passing.
  - Explain 1970s defensive dominance and the rules (1972 hashes, 1974 changes) that failed to fix it.
- **Key terms introduced:** single wing; platoon football; Flex defense; dead-ball era; chuck rule
- **Diagrams:**
  - [S] Single wing plate
  - [S] 1940 T-formation
  - [S] Lombardi power sweep
  - [S] Landry Flex
  - [C] Points per game 1932-1977
  - [S] Timeline graphic
- **Team / era examples:** Halas, Shaughnessy & Luckman (1940 Bears); Paul Brown's Browns; Lombardi Packers; Landry Cowboys; Gillman Chargers; 1970s Steelers; 1972 Dolphins
- **Watch for this on Sunday:** Spot the ancestor: find one modern play with single-wing or T-formation DNA (wildcat, direct snap, buck sweep).

#### 11-02 1978 and the Passing Revolution (1978-1999)

- **Slug:** `11-02-the-1978-liberation` | **Level:** 3 | **Est. length:** 16 pp
- **Prerequisites:** 11-01, 04-08, 07-03, 05-02
- **Learning objectives:**
  - Explain the 1978 rules (Mel Blount rule, pass-blocking hands) and their effect.
  - Describe Air Coryell, the West Coast offense, Gibbs' one-back and counter trey, run-and-shoot, the K-Gun.
  - Describe the defensive answers: nickel/dime, the 46, Lawrence Taylor and the blind-side tackle, the zone blitz.
  - Explain free agency (1993) and the salary cap (1994).
  - Explain the 1994 two-point conversion and kickoff changes.
- **Key terms introduced:** Mel Blount rule (1978); blind-side tackle; free agency (1993); salary cap
- **Diagrams:**
  - [C] League passing yards per attempt and points per game, 1970-1999 (season-level data)
  - [S] Why the left tackle matters: right-handed QB's blind side
  - [S] 46 vs one-back counter
  - [S] Timeline graphic
- **Team / era examples:** Coryell Chargers; Walsh 49ers; Gibbs Washington; 1985 Bears; Parcells/Belichick Giants; Run-and-shoot Oilers/Lions/Falcons; Bills K-Gun; Blitzburgh Steelers; 1998 Broncos
- **Watch for this on Sunday:** Classic film: watch a 1980s game on NFL Films/YouTube; identify the formations and coverages you now know.

#### 11-03 The College Laboratory: Wing-T, Wishbone, Air Raid, Spread Option, and the RPO

- **Slug:** `11-03-the-college-laboratory` | **Level:** 3 | **Est. length:** 16 pp
- **Prerequisites:** 11-02, 03-04, 04-06, 06-05
- **Learning objectives:**
  - Explain why college innovates (talent gaps, wide hashes, ineligible-downfield leeway, tempo).
  - Trace wishbone/veer/flexbone, Wing-T, BYU passing, Air Raid, spread option, pistol, RPO.
  - Trace college defensive answers: 3-3-5, quarters, pattern match, tite fronts, three-safety looks.
  - Explain when and how each crossed into the NFL.
- **Key terms introduced:** flexbone; spread offense; spread option; 3-3-5 stack; three-high safety defense
- **Diagrams:**
  - [S] Wishbone triple option
  - [S] Air Raid four verts
  - [S] Rich Rodriguez zone read with bubble attached
  - [S] 3-3-5 stack
  - [C] NFL shotgun rate with college-import annotations
- **Team / era examples:** Texas/Oklahoma wishbone; Houston veer; Delaware Wing-T; BYU (LaVell Edwards); Kentucky/Texas Tech Air Raid; Rodriguez and Meyer spread option; Oregon (Chip Kelly); Auburn (Malzahn, Cam Newton); Oklahoma (Riley: Mayfield, Murray); Saban's Alabama and Smart's Georgia defenses
- **Watch for this on Sunday:** Saturday vs Sunday: watch one college and one NFL game; list three structural differences.

#### 11-04 Dynasties and Counterpunches (2000-2016)

- **Slug:** `11-04-dynasties-and-counterpunches` | **Level:** 3 | **Est. length:** 15 pp
- **Prerequisites:** 11-03
- **Learning objectives:**
  - Explain the Tampa 2 dynasty and its counters (seam TEs, Peyton Manning).
  - Explain the Patriots' adaptability: EP system, 2007 spread, 2010s two-TE 12 personnel.
  - Explain the 2004 illegal-contact emphasis and the passing boom that followed.
  - Explain the 3-4 revival and the hybrid edge.
  - Explain the 2012 read-option wave and why it receded; Seattle's Cover 3; Chip Kelly's 2013 Eagles.
  - Describe the early analytics movement.
- **Key terms introduced:** move tight end (joker); hybrid edge; read-option wave (2012)
- **Diagrams:**
  - [S] Manning vs Tampa 2 seam
  - [S] Patriots 12 personnel dilemma: base vs nickel
  - [C] League EPA/dropback 1999-2016
  - [C] Designed QB run share, 2012 spike
- **Team / era examples:** Manning Colts; Patriots; Steelers 2005/2008; 2007 Giants pass rush; Brees/Payton Saints; 2013 Seahawks; 2015 Broncos defense; Romer (2006) and Brian Burke's Advanced NFL Stats
- **Watch for this on Sunday:** Personnel dilemma: when a team uses 12 personnel with an athletic TE, does the defense stay nickel or go base?

#### 11-05 The Modern Era: McVay, Mahomes, Two-High, and the Under-Center Comeback (2017-2025)

- **Slug:** `11-05-the-modern-era` | **Level:** 3 | **Est. length:** 16 pp
- **Prerequisites:** 11-04, 06-06
- **Learning objectives:**
  - Explain the McVay/Shanahan revival: 11 personnel, condensed sets, play-action, motion.
  - Explain Mahomes/Reid off-script and college-concept passing.
  - Explain the two-high counterrevolution and the offensive response (light-box runs, under center, heavier personnel).
  - Explain the normalisation of the QB run game (Lamar, Hurts, Allen).
  - Explain analytics-driven aggression.
  - Summarise rule-era changes (helmet rule, dynamic kickoff, OT, hip-drop, tush push) and where the game stands entering 2026.
- **Key terms introduced:** two-high counterrevolution; under-center revival; light-box run game
- **Diagrams:**
  - [C] Two-high rate vs 11-personnel rate vs under-center rate, 2016-2025
  - [S] Arms-race loop diagram (offensive move -> defensive answer -> ...)
  - [C] Fourth-down go rate by season
  - [S] Timeline graphic
- **Team / era examples:** Rams 2017-18; Chiefs 2018-24; 49ers; Ravens 2019/2023; Eagles 2022/2024; Lions 2023-24; Bills; Seahawks 2025; Fangio/Staley/Evero; Macdonald
- **Watch for this on Sunday:** Arms-race spotting: in one game, identify one offensive trend and the defensive counter you see against it.

### Part 12: Case Studies: Teams That Did It Best

_Levels 4-5._ Deep dives, each structured the same way: the problem the team faced, the scheme answer, the signature plays (diagrammed and animated), the data fingerprint, how opponents responded, and what survives today.

#### 12-01 Case Study: Bill Walsh's 49ers and the West Coast Offense

- **Slug:** `12-01-walsh-49ers-west-coast` | **Level:** 4 | **Est. length:** 14 pp
- **Prerequisites:** 11-02, 04-04
- **Learning objectives:**
  - Explain the WCO's short horizontal passing as a substitute run game.
  - Explain timing, YAC, and ball placement as design goals.
  - Explain scripting and Walsh's practice methods.
  - Break down 'The Catch' (1981 NFC Championship).
  - Trace the Walsh tree to modern staffs.
- **Key terms introduced:** horizontal passing game
- **Diagrams:**
  - [A] 'Sprint Right Option' / The Catch recreated (frame strip)
  - [S] WCO drive and slant-flat from split backs
  - [S] Walsh coaching tree
- **Team / era examples:** 1981-1989 49ers (Montana, Rice, Craig); Holmgren Packers; Andy Reid; Jon Gruden; the Shanahan link
- **Watch for this on Sunday:** WCO census: count short horizontal throws on early downs for a WCO-descended team.

#### 12-02 Case Study: Belichick and Game-Plan Football

- **Slug:** `12-02-belichick-patriots-game-plan` | **Level:** 4 | **Est. length:** 15 pp
- **Prerequisites:** 11-04, 08-03
- **Learning objectives:**
  - Explain game-plan-specific defense and 'take away their best thing'.
  - Break down the defensive plans in Super Bowls XXV (as Giants DC), XXXVI, and LIII.
  - Explain the offense's chameleon identity (2007 spread, 2011 12 personnel, 2018 run heavy).
  - Analyse situational mastery (end of half, fourth down, clock).
  - Break down Super Bowl XLIX's final play.
- **Key terms introduced:** game-plan defense
- **Diagrams:**
  - [S] Giants' Super Bowl XXV plan vs the K-Gun
  - [S] Patriots' plan vs the 2018 Rams (verify specifics on film)
  - [A] Super Bowl XLIX goal-line interception (frame strip)
  - [S] Gronkowski 12-personnel dilemma
- **Team / era examples:** 1990 Giants; 2001-2019 Patriots
- **Watch for this on Sunday:** Take-away test: before a game, guess the opponent's best thing; afterwards decide whether it was taken away.

#### 12-03 Case Study: The Shanahan Tree - Wide Zone, Boots, and the Illusion of Complexity

- **Slug:** `12-03-shanahan-wide-zone-tree` | **Level:** 4 | **Est. length:** 16 pp
- **Prerequisites:** 11-05, 08-02
- **Learning objectives:**
  - Trace wide zone from Alex Gibbs' Broncos to Kyle Shanahan's 49ers.
  - Explain the 49ers' marriage of wide zone, FB, motion, and YAC passing.
  - Explain why the system makes QBs efficient (and the debate it creates).
  - Map the tree: McVay, LaFleur, McDaniel, Kubiak, Coen and others.
  - Show the data fingerprint (under-center rate, PA rate, YAC over expected).
- **Key terms introduced:** YAC over expected (YACOE)
- **Diagrams:**
  - [S] Wide zone vs bear look
  - [A] Keeper/boot off wide zone (frame strip)
  - [S] One look, four plays
  - [C] 49ers EPA/play rank 2019-2025
  - [C] YAC over expected by team
- **Team / era examples:** 1990s Broncos; 2016 Falcons; 2017-2025 49ers; McVay Rams; McDaniel Dolphins; Kubiak 2025 Seahawks
- **Watch for this on Sunday:** Same look? Track one team's formation+motion combinations and list the different plays run from each.

#### 12-04 Case Study: Andy Reid and the Kansas City Chiefs

- **Slug:** `12-04-reid-chiefs` | **Level:** 4 | **Est. length:** 15 pp
- **Prerequisites:** 11-05, 07-02
- **Learning objectives:**
  - Explain Reid's blend of WCO roots, college spread/RPO, and trick plays.
  - Explain how Mahomes' off-script ability changes defensive math.
  - Contrast the Tyreek Hill era with the 2022+ Kelce/quick-game era.
  - Explain Spagnuolo's pressure defense as the complement.
  - Review the Super Bowl run (LIV, LV, LVII, LVIII, LIX).
- **Key terms introduced:** none new (consolidation chapter; uses terms from prerequisites)
- **Diagrams:**
  - [A] 'Jet Chip Wasp' 3rd & 15 in Super Bowl LIV (frame strip)
  - [S] Kelce option route vs man and vs zone
  - [S] Spagnuolo Cover 0 pressure
  - [C] Chiefs EPA/play 2018-2025
- **Team / era examples:** 2018-2025 Chiefs
- **Watch for this on Sunday:** Off-script counter: count plays that leave structure; note the result vs in-structure plays.

#### 12-05 Case Study: The Ravens' Option Run Game with Lamar Jackson

- **Slug:** `12-05-ravens-lamar-run-game` | **Level:** 4 | **Est. length:** 14 pp
- **Prerequisites:** 11-05, 03-04, 05-05
- **Learning objectives:**
  - Explain Greg Roman's 2019 design: heavy personnel, pistol, option variants, QB power/counter.
  - Explain why a QB runner changes defensive arithmetic in every run fit.
  - Explain the Todd Monken changes (2023) and the Derrick Henry pairing (2024).
  - Analyse defensive answers and playoff struggles honestly with data.
- **Key terms introduced:** pistol option offense
- **Diagrams:**
  - [S] Pistol inverted veer
  - [S] Ravens 2019 13-personnel plate
  - [A] QB counter (frame strip)
  - [C] Ravens rushing EPA vs league 2018-2025
- **Team / era examples:** 2019 Ravens; 2023-2024 Ravens
- **Watch for this on Sunday:** Count the defenders: on Ravens runs, count box defenders vs blockers (with the QB as a runner).

#### 12-06 Case Study: The Eagles - Trenches, RPOs, and the Tush Push

- **Slug:** `12-06-eagles-trenches-and-tush-push` | **Level:** 4 | **Est. length:** 14 pp
- **Prerequisites:** 11-05, 10-03
- **Learning objectives:**
  - Explain the 2017 RPO offense and the Philly Special.
  - Explain the Sirianni/Hurts run game and OL investment (Jeff Stoutland).
  - Analyse the tush push as a scheme and as a talent edge.
  - Explain the 2024 team: Saquon Barkley and Fangio's defense, and Super Bowl LIX's four-man pressure.
  - Connect roster building to scheme.
- **Key terms introduced:** Philly Special
- **Diagrams:**
  - [A] Philly Special (frame strip)
  - [S] Tush push, revisited from 10-03
  - [S] 2024 outside zone / duo with Barkley
  - [S] Super Bowl LIX four-man pressure without blitzing
  - [C] Eagles QB sneak conversion rate vs league
- **Team / era examples:** 2017 Eagles; 2022 Eagles; 2024 Eagles
- **Watch for this on Sunday:** Trench check: on Eagles third-and-short, guess sneak/tush push vs other; note what the defense does.

#### 12-07 Case Study: The Lions - Ben Johnson's Offense and Dan Campbell's Aggression

- **Slug:** `12-07-lions-ben-johnson-and-campbell` | **Level:** 4 | **Est. length:** 14 pp
- **Prerequisites:** 11-05, 10-04
- **Learning objectives:**
  - Explain the 2021 rebuild philosophy.
  - Explain Ben Johnson's offense (2022-2024): under center, motion, jumbo with eligible linemen, trick plays.
  - Analyse Campbell's fourth-down aggression with data.
  - Explain the 2024 team and the 2025 coordinator departures (Johnson to Chicago, Glenn to the Jets).
  - Assess what transferred with Johnson to the Bears.
- **Key terms introduced:** eligible tackle (tackle-eligible)
- **Diagrams:**
  - [S] Jumbo eligible-tackle play
  - [A] Shift + motion sequence (frame strip)
  - [C] Lions fourth-down go rate and EPA vs league
- **Team / era examples:** 2022-2025 Lions; 2025 Bears
- **Watch for this on Sunday:** Trick detector: in a Lions or Bears game, flag every snap with an unusual alignment or eligible lineman.

#### 12-08 Case Study: Fangio's Two-High Revolution and Macdonald's Answer

- **Slug:** `12-08-two-high-to-macdonald` | **Level:** 5 | **Est. length:** 16 pp
- **Prerequisites:** 11-05, 06-06, 07-03
- **Learning objectives:**
  - Explain Fangio's principles: two-high, light box, four-man rush, tite front, match quarters/Cover 6.
  - Trace the spread (Staley, Evero and others) and Fangio's 2024 Eagles.
  - Explain Macdonald's multiplicity: disguise, sim pressure, and front variety (2023 Ravens, 2024-25 Seahawks).
  - Compare philosophies with data (pressure rate, disguise rate, EPA allowed).
  - Predict what offenses do next.
- **Key terms introduced:** multiplicity (defensive)
- **Diagrams:**
  - [S] Fangio tite + quarters vs 11 personnel
  - [A] Macdonald sim pressure from a two-high look (frame strip)
  - [T] Safety rotation measured from tracking
  - [C] Two-high rate vs pressure rate by team
- **Team / era examples:** 2018 Bears; 2020 Rams; 2024 Eagles; 2023 Ravens; 2024-2025 Seahawks
- **Watch for this on Sunday:** Disguise audit: chart pre-snap shell vs post-snap coverage for one defense; compute its lie rate.

### Part 13: Analytics and Data

_Levels 3-5._ The reader's home turf. Earlier chapters show nflverse charts with code folded; this part teaches the reader to build them and then goes further, ending with tracking data and the Big Data Bowl. 13-01 can be read early (right after Part 2) by readers who want to run code alongside the course.

#### 13-01 Working with nflverse Data in Python

- **Slug:** `13-01-nflverse-in-python` | **Level:** 3 | **Est. length:** 14 pp
- **Prerequisites:** 01-02, 02-01
- **Learning objectives:**
  - Install and use nflreadpy (polars) and convert to pandas where needed.
  - Load play-by-play, schedules, rosters, participation, and FTN charting data.
  - Understand the pbp row structure (play_type, down, ydstogo, yardline_100, epa, wp, ...).
  - Filter to 'real' plays (rush/pass, no-play penalties, garbage time).
  - Join participation data for personnel and formation.
  - Reproduce a chart from an earlier chapter end-to-end.
- **Key terms introduced:** play-by-play (pbp); nflverse; nflreadpy; participation data; FTN charting data; yardline_100; garbage-time filter
- **Diagrams:**
  - [S] pbp schema diagram
  - [C] Reproduce 02-01's personnel usage chart
  - [S] Data flow: nflverse -> course diagram library
- **Team / era examples:** League pass rate by down, reproduced
- **Watch for this on Sunday:** Sunday notebook: after each week, load the new pbp and score your prediction log against it.

#### 13-02 Expected Points, EPA, and Success Rate

- **Slug:** `13-02-expected-points-and-success-rate` | **Level:** 4 | **Est. length:** 16 pp
- **Prerequisites:** 13-01
- **Learning objectives:**
  - Explain the expected-points model (down, distance, yard line).
  - Compute EPA per play and success rate; explain why EPA beats yards.
  - Compare run and pass EPA honestly (selection effects).
  - Use CPOE and RYOE for player evaluation.
  - Handle stability, noise, sample size, and opponent adjustment.
- **Key terms introduced:** expected points (EP); EPA (expected points added); success rate; RYOE (rush yards over expected); year-over-year stability; opponent adjustment
- **Diagrams:**
  - [C] EP curve by yard line for each down
  - [C] EPA distribution, run vs pass
  - [C] Team offense vs defense EPA scatter
  - [S] One play's EPA, worked by hand
- **Team / era examples:** 2024 and 2025 team rankings
- **Watch for this on Sunday:** EPA in your head: estimate EP before and after a play; check with the model.

#### 13-03 Win Probability and Decision Analysis: Fourth Downs, Two-Pointers, Timeouts

- **Slug:** `13-03-win-probability-and-fourth-down` | **Level:** 4 | **Est. length:** 15 pp
- **Prerequisites:** 13-02, 10-04
- **Learning objectives:**
  - Explain win-probability models and WPA; leverage.
  - Build a fourth-down decision framework (conversion probability x WP outcomes vs punt/FG).
  - Analyse two-point decisions (down 8, down 14).
  - Critique model uncertainty and calibration.
  - Measure coaches' changing behaviour.
- **Key terms introduced:** win probability (WP); WPA (win probability added); leverage (game situation); fourth-down model (bot); break-even conversion rate
- **Diagrams:**
  - [C] WP chart for Super Bowl LI (28-3)
  - [C] Fourth-down recommendation heatmap
  - [S] Decision tree for one fourth down
  - [C] Team aggressiveness vs model recommendation
- **Team / era examples:** Ben Baldwin's fourth-down model; NYT 4th Down Bot; Lions under Campbell
- **Watch for this on Sunday:** Be the bot: make every fourth-down call live; compare with the model afterwards.

#### 13-04 Tendencies: PROE, Personnel, Motion, and Coverage from Charting Data

- **Slug:** `13-04-tendencies-proe-and-charting` | **Level:** 4 | **Est. length:** 15 pp
- **Prerequisites:** 13-02, 08-02
- **Learning objectives:**
  - Explain expected pass rate (xpass) and PROE; compute by team, season, and situation.
  - Measure personnel, formation, motion, and play-action tendencies.
  - Measure coverage tendencies where charting data exists.
  - Build a one-page data scouting report.
  - State the caveats of charting data (definitions, coverage, errors).
- **Key terms introduced:** xpass (expected pass rate); PROE (pass rate over expected); neutral situation; coverage charting
- **Diagrams:**
  - [C] Team PROE vs EPA scatter
  - [C] Team tendency dashboard (personnel x pass rate x PA x motion)
  - [C] Coverage mix by team
  - [S] Scouting-report template
- **Team / era examples:** 2024-2025 team tendencies
- **Watch for this on Sunday:** Opponent card: produce a one-page tendency card before a game and grade it live.

#### 13-05 Tracking Data and the Big Data Bowl

- **Slug:** `13-05-tracking-data-and-big-data-bowl` | **Level:** 5 | **Est. length:** 18 pp
- **Prerequisites:** 13-04, 06-06
- **Learning objectives:**
  - Understand NGS tracking (10 Hz; x, y, s, a, o, dir) and the coordinate system.
  - Standardise play direction and align frames to the snap and the throw.
  - Plot and animate tracking frames with the course's diagram library.
  - Derive features: separation, pocket area, safety rotation, motion detection.
  - Sketch projects: man/zone classification, route classification, disguise measurement.
  - Survey Big Data Bowl themes and winning approaches.
- **Key terms introduced:** tracking data; Next Gen Stats (NGS); frame (tracking); orientation vs direction; standardised play direction; separation; Big Data Bowl
- **Diagrams:**
  - [S] Tracking coordinate system
  - [T] One real play animated from BDB data with the course library (frame strip)
  - [T] Separation over time for each receiver
  - [T] Safety depth at the snap, team distribution
- **Team / era examples:** Big Data Bowl themes 2019-2026
- **Watch for this on Sunday:** First tracking chart: choose a play you watched live and plot it with the library.

### Part 14: The Business of Scheme: Roster, Cap, Draft, and Fantasy

_Levels 3._ How X's and O's turn into money and fantasy points.

#### 14-01 Scheme, Roster, and Fantasy: How X's and O's Shape Money and Points

- **Slug:** `14-01-scheme-roster-and-fantasy` | **Level:** 3 | **Est. length:** 18 pp
- **Prerequisites:** 13-02, 08-03
- **Learning objectives:**
  - Explain positional value with data (QB, edge, LT, WR, CB vs RB, LB, S).
  - Explain cap mechanics: cap hit, dead money, rookie-contract window, fifth-year option, franchise tag, void years.
  - Explain scheme fit in the draft (wide-zone OL vs gap OL, two-gap nose vs 3-tech, press vs off corners).
  - Explain roster construction: 53, game-day actives, practice squad.
  - Translate scheme into fantasy: route participation, target share, YPRR, RB usage, TE in 12 personnel, PROE and pace.
  - Predict how a coordinator change shifts fantasy value.
- **Key terms introduced:** cap hit; dead money; rookie-contract window; fifth-year option; franchise tag; void years; positional value; scheme fit; route participation; target share; YPRR (yards per route run); snap share; game script
- **Diagrams:**
  - [C] Positional cap share vs wins
  - [C] Draft pick value curve
  - [C] Target share vs team PROE
  - [S] Scheme-fit archetype chart (body type by scheme and position)
- **Team / era examples:** 2021 Rams trade-heavy build; Eagles OL investment; 49ers' mid-round wide-zone linemen; Brock Purdy's rookie contract; Saquon Barkley in 2024
- **Watch for this on Sunday:** Scheme-shift draft: for one team with a new coordinator, predict which fantasy assets rise and fall.

### Part 15: Capstone: Watching Like a Coach

_Levels 5._ Integrates every per-chapter drill into one protocol and scores the reader's prediction log from Chapter 01-02 onward.

#### 15-01 Watching Like a Coach: The Master Checklist, All-22, and Charting a Game

- **Slug:** `15-01-watching-like-a-coach` | **Level:** 5 | **Est. length:** 18 pp
- **Prerequisites:** 08-04, 10-04, 13-04
- **Learning objectives:**
  - Run the master pre-snap checklist in ~20 seconds: situation -> personnel -> formation/strength -> motion response -> box -> shell -> leverage -> pressure tells -> prediction.
  - Get and watch All-22 with a four-pass film protocol (OL, QB, coverage, skill players).
  - Chart a full game with a template.
  - Break down a complete annotated drive.
  - Score the season's prediction log with Brier score and calibration plots in Python.
  - Know where to keep learning (coaching clinics, analytics community, BDB).
- **Key terms introduced:** film-study protocol; charting (game charting); Brier score; calibration
- **Diagrams:**
  - [S] Master checklist one-page card
  - [A] Full drive (8-12 plays) annotated, frame strips
  - [C] Calibration plot of the reader's prediction log
  - [S] Charting sheet template
- **Team / era examples:** A recent playoff drive chosen for variety (verify at writing time)
- **Watch for this on Sunday:** Chart a full game: every snap, all checklist fields, prediction, outcome; then score it.

## 5. Reference appendices (the atlas)

The atlas is built from the same diagram source as the chapters (one plate definition, rendered in both places). Every atlas card has the same fields: **name and aliases | diagram | what it is (2-3 sentences) | why it exists | strong against / weak against | pre-snap tells | teams known for it | taught in (chapter link)**. Cards are one per half-page in PDF, searchable in HTML.

| Appendix | Slug | Title | Contents |
|---|---|---|---|
| A | `appendix-a-offense-atlas.qmd` | Offensive Atlas: Personnel and Formations | All personnel groupings (02-01); classic and spread formations (02-03, 02-04); backfield alignments; motion family (02-05); specialty looks. ~45 cards. |
| B | `appendix-b-concept-atlas.qmd` | Concept Atlas: Runs, Passes, Screens, RPOs | Run concepts (zone, gap, option, perimeter; 03-02 to 03-05); route tree; quick, dropback, play-action, screen, RPO concepts (04-03 to 04-06); red-zone and short-yardage concepts (10-03). ~60 cards. |
| C | `appendix-c-defense-atlas.qmd` | Defensive Atlas: Packages, Techniques, and Fronts | Packages (02-06); technique chart (03-01/05-01); even, odd, hybrid, nickel, goal-line fronts (05-02, 05-03, 10-03); run-fit cheat sheet (05-05). ~30 cards. |
| D | `appendix-d-coverage-pressure-atlas.qmd` | Coverage and Pressure Atlas | Cover 0, 1 (robber/rat), 2, Tampa 2, 2-Man, 3 (sky/buzz/cloud/match), 4, 6, Palms, 7/split-field, poach (Part 6); fire zones, sim pressures, overloads, mugs (Part 7); plus the concept x coverage matrix (08-01) and a 'coverage dialects' table mapping different teams' names for the same call. ~40 cards. |
| E | `appendix-e-rules-timeline-trees.qmd` | Rules, Timeline, and Coaching Trees | Penalty quick-reference table (yardage, auto first down, enforcement spot); kickoff/punt/OT rule summaries (current as of 2025 season); rule-change timeline 1906-2025 with each change's strategic effect; Super Bowl results with a one-line scheme note each; coaching-tree diagrams. |
| F | `appendix-f-glossary.qmd` | Glossary | Alphabetical; every term from Section 6 with a one-sentence definition, aliases/dialect variants (e.g., 'Cover 5 = 2-Man'), and a link to the defining chapter. Generated from a single YAML terms file so chapter key-term boxes and the glossary never drift. |

Front matter (unnumbered `index.qmd`): how to use the book, the level system, the diagram notation key, and how to set up the Python environment.

## 6. Master term index (glossary seed)

632 terms, each defined in exactly one chapter (validated by the generator: no term is defined twice). Later chapters may deepen a term; the glossary links to the defining chapter.

**0-9**

- 10 personnel -> 02-01
- 10-second runoff -> 10-04
- 11 personnel -> 02-01
- 12 personnel -> 02-01
- 13 personnel -> 02-01
- 2-4-5 -> 05-03
- 2-Man (Cover 5) -> 06-04
- 21 personnel -> 02-01
- 22 personnel -> 02-01
- 2x2 (doubles) -> 02-04
- 3-3-5 -> 05-03
- 3-3-5 stack -> 11-03
- 3-4 -> 02-06
- 3-4 Okie -> 05-03
- 3-technique -> 05-01
- 3x1 (trips) -> 02-04
- 3x1 check (solo / stubbie) -> 06-06
- 4-2-5 -> 05-03
- 4-3 -> 02-06
- 4-3 Over -> 05-02
- 4-3 Under -> 05-02
- 46 defense -> 05-02
- 4i technique -> 05-01
- 5-technique -> 05-01

**A**

- accept / decline (penalty) -> 09-03
- ace formation -> 02-03
- aDOT (average depth of target) -> 04-01
- aiming point -> 03-02
- Air Coryell -> 04-08
- Air Raid -> 04-08
- air yards -> 04-01
- alert (shot alert) -> 08-01
- alignment -> 01-03
- All-22 -> 01-06
- alley player -> 05-05
- angle (line movement) -> 05-01
- anticipation throw -> 04-07
- apex (overhang) defender -> 04-06
- apex alignment -> 05-04
- assignment -> 01-03
- assisting the runner (push rule) -> 10-03
- audible -> 01-05

**B**

- back-shoulder throw -> 10-03
- backed up -> 10-01
- backside cut-off -> 03-02
- bail -> 06-01
- bang-bend-bounce -> 03-02
- banjo -> 06-02
- base defense -> 02-06
- base play -> 08-02
- bear front -> 05-02
- Big Data Bowl -> 13-05
- big nickel -> 02-06
- blind-side tackle -> 11-02
- blitz -> 07-02
- bootleg -> 04-05
- boundary side (short side) -> 01-01
- box -> 02-06
- box count -> 02-06
- box technique (squeeze) -> 05-05
- bracket -> 06-02
- break-even conversion rate -> 13-03
- Brier score -> 15-01
- bubble RPO -> 04-06
- bubble screen -> 04-05
- buck sweep -> 03-05
- bull rush -> 07-01
- bump (defensive adjustment) -> 02-05
- bunch -> 02-04
- buzz rotation -> 06-03

**C**

- cadence (snap count) -> 01-05
- calibration -> 15-01
- call sheet -> 01-04
- cap hit -> 14-01
- center -> 01-03
- charting (game charting) -> 15-01
- check -> 01-05
- check-release -> 04-02
- check-with-me -> 01-05
- checkdown -> 04-07
- chip -> 04-02
- choice route -> 04-08
- chuck rule -> 11-01
- climbing the pocket -> 04-07
- cloud (corner) rotation -> 06-03
- coach's challenge -> 09-03
- coaches film -> 01-06
- coaching booth -> 08-04
- coaching tree -> 04-08
- coffin-corner punt -> 09-01
- combo block (double team) -> 03-01
- combo coverage -> 06-02
- comeback -> 04-01
- coming out -> 10-01
- compressed field -> 10-03
- concept-based terminology -> 04-08
- condensed formation -> 02-04
- conflict defender -> 04-01
- constraint play -> 08-02
- contain -> 05-01
- corner route -> 04-01
- cornerback -> 01-03
- counter (counter trey / GT counter) -> 03-03
- Cover 0 -> 06-02
- Cover 0 blitz -> 07-02
- Cover 1 (man-free) -> 06-02
- Cover 1 blitz -> 07-02
- Cover 2 -> 06-04
- Cover 3 -> 06-03
- Cover 3 match -> 06-03
- Cover 6 -> 06-05
- Cover 7 (match family) -> 06-06
- coverage beater -> 08-01
- coverage charting -> 13-04
- coverage numbering (Cover 0-6) -> 06-01
- covered / uncovered lineman -> 03-01
- covered receiver -> 02-02
- CPOE (completion % over expected) -> 04-07
- crack block -> 03-01
- crack-toss -> 03-05
- curl zone -> 06-01
- curl-flat -> 04-04
- curl-flat defender -> 06-03
- cushion -> 06-01
- cut block -> 03-01
- cut-off block -> 03-01
- cutback -> 03-02

**D**

- dagger -> 04-04
- dead money -> 14-01
- dead-ball era -> 11-01
- deep half -> 06-01
- deep quarter -> 06-01
- deep third -> 06-01
- defensive end -> 01-03
- defensive holding -> 09-03
- defensive package -> 02-06
- defensive pass interference (DPI) -> 09-03
- defensive tackle -> 01-03
- delay of game -> 01-04
- dig (in) -> 04-01
- dime -> 02-06
- disguise -> 06-06
- dive -> 03-04
- double A-gap mug -> 07-02
- double slants -> 04-03
- down -> 01-02
- down block -> 03-01
- draw play -> 10-02
- drive (concept) -> 04-04
- drive (possession) -> 01-02
- drive block -> 03-01
- drop (3/5/7-step) -> 04-01
- dropper (DL in coverage) -> 07-03
- dummy call -> 01-05
- duo -> 03-03
- dynamic kickoff -> 09-02

**E**

- E-T stunt -> 07-01
- early down -> 10-01
- edge rusher -> 01-03
- eligible receiver -> 01-03
- eligible tackle (tackle-eligible) -> 12-07
- empty (3x2) -> 02-04
- encroachment -> 01-05
- end zone -> 01-01
- end-around -> 03-05
- end-zone camera -> 01-06
- EPA (expected points added) -> 13-02
- Erhardt-Perkins -> 04-08
- even front -> 05-02
- expected points (EP) -> 13-02
- extra point (PAT) -> 01-01
- eye candy -> 03-05

**F**

- fade -> 10-03
- fair catch -> 09-01
- fake punt / fake field goal -> 09-01
- false start -> 01-05
- field goal -> 01-01
- field goal range -> 09-01
- field position -> 01-02
- field side (wide side) -> 01-01
- fifth-year option -> 14-01
- fill -> 05-04
- film-study protocol -> 15-01
- fire zone (3-under 3-deep) -> 07-03
- first down -> 01-02
- five-man pressure -> 07-02
- flat route -> 04-01
- flat zone -> 06-01
- Flex defense -> 11-01
- flexbone -> 11-03
- flood (sail) -> 04-04
- flow (fast / slow) -> 05-04
- fly motion -> 02-05
- force (defender) -> 05-05
- formation strength -> 02-02
- four verticals -> 04-04
- four-down territory (fringe) -> 10-01
- four-man rush -> 07-02
- four-minute offense -> 10-04
- fourth-down model (bot) -> 13-03
- frame (tracking) -> 13-05
- franchise tag -> 14-01
- free agency (1993) -> 11-02
- free play -> 09-03
- free rusher -> 04-02
- free safety -> 01-03
- front seven -> 01-03
- FTN charting data -> 13-01
- full house backfield -> 02-03
- fullback -> 01-03
- fumble -> 01-02

**G**

- game clock -> 01-01
- game plan -> 08-03
- game script -> 14-01
- game-plan defense -> 12-02
- game-plan package -> 08-03
- gap (A, B, C, D) -> 03-01
- gap exchange -> 05-05
- gap integrity -> 05-05
- gap scheme (man/power blocking) -> 03-03
- garbage-time filter -> 13-01
- get-off -> 07-01
- give / keep -> 03-04
- glance RPO -> 04-06
- go (fly / 9) -> 04-01
- go-for-it decision -> 10-04
- goal line -> 01-01
- goal-line defense -> 10-03
- goal-line formation -> 02-03
- green dot -> 01-04
- guard -> 01-03
- gunner -> 01-03

**H**

- H / F (move player) -> 02-02
- Hail Mary -> 10-04
- half the distance -> 09-03
- half-slide -> 04-02
- halftime adjustment -> 08-04
- hard (squat) corner -> 06-04
- hard count -> 01-05
- hash marks -> 01-01
- hat math (numbers advantage) -> 03-01
- head-up -> 03-01
- heavy personnel -> 02-01
- helmet radio (coach-to-player communication) -> 01-04
- high-low read (vertical stretch) -> 04-01
- hitch (curl) -> 04-01
- hitch-seam -> 04-03
- holder -> 01-03
- hole (rat) zone -> 06-01
- hole numbering -> 03-01
- hole shot -> 06-04
- hook / curl defender -> 05-04
- hook zone -> 06-01
- horizontal passing game -> 12-01
- horizontal stretch -> 04-01
- hot route -> 04-02
- huddle -> 01-04
- hurry-up offense -> 08-04
- hybrid edge -> 11-04

**I**

- I-formation -> 02-03
- illegal contact -> 09-03
- illegal formation -> 02-02
- illegal man downfield -> 04-06
- illegal motion -> 01-05
- illusion of complexity -> 08-02
- in-line tight end -> 02-02
- ineligible receiver -> 01-03
- inside help -> 06-02
- inside zone -> 03-02
- install -> 01-04
- interception -> 01-02
- inverted veer (power read) -> 03-04
- iso (isolation) -> 03-03

**J**

- jailbreak screen -> 04-05
- jet motion -> 02-05
- jet sweep -> 03-05
- jumbo (six offensive linemen) -> 02-01
- jump set -> 04-02

**K**

- keeper -> 04-05
- key (read key, defense) -> 05-04
- kick coverage unit -> 09-02
- kick-out -> 03-01
- kicker -> 01-03
- kickoff -> 09-02
- kill call -> 01-05

**L**

- landing zone -> 09-02
- landmark -> 06-01
- late rotation -> 06-06
- launch point -> 04-02
- lead block -> 03-01
- leak -> 04-05
- levels -> 04-04
- leverage (game situation) -> 13-03
- leverage (inside / outside) -> 04-03
- light box -> 02-06
- light-box run game -> 11-05
- line of scrimmage -> 01-02
- line to gain -> 01-02
- linebacker -> 01-03
- loaded box -> 02-06
- log block (wrap) -> 03-01
- long arm -> 07-01
- long snapper -> 01-03
- look-off -> 04-07
- lurk -> 06-02

**M**

- man coverage -> 02-06
- man protection (BOB) -> 04-02
- man-beater -> 04-04
- man/zone indicator -> 02-05
- matchup (mismatch) -> 08-03
- max protect -> 04-02
- MEG (man everywhere he goes) -> 06-05
- Mel Blount rule (1978) -> 11-02
- mesh -> 04-04
- midline option -> 03-04
- Mike identification (MIKE ID) -> 01-05
- Mike linebacker -> 01-03
- misdirection -> 03-05
- MOD (man only deep) -> 06-05
- MOFC (middle of field closed) -> 06-01
- MOFO (middle of field open) -> 06-01
- motion -> 01-05
- motion at the snap -> 02-05
- move tight end (joker) -> 11-04
- multiple (hybrid) defense -> 05-03
- multiplicity (defensive) -> 12-08

**N**

- naked bootleg -> 04-05
- net punting average -> 09-01
- neutral situation -> 13-04
- neutral zone infraction -> 01-05
- Next Gen Stats (NGS) -> 13-05
- nflreadpy -> 13-01
- nflverse -> 13-01
- nickel -> 02-06
- no-huddle -> 01-04
- nose tackle -> 01-03
- nub -> 02-04

**O**

- odd front -> 05-03
- off coverage -> 06-01
- off-script (off-schedule) play -> 04-07
- offensive holding -> 09-03
- offensive line -> 01-03
- offensive pass interference (OPI) -> 09-03
- offensive system -> 04-08
- offset back -> 02-02
- offset I -> 02-03
- offside -> 01-05
- on schedule / behind schedule -> 10-01
- on the line / off the line -> 02-02
- one-cut runner -> 03-02
- one-gap -> 05-01
- one-high (single-high) -> 02-06
- onside kick -> 09-02
- open field -> 10-01
- opening script -> 08-03
- opponent adjustment -> 13-02
- option -> 03-04
- option route -> 04-01
- orbit motion -> 02-05
- orientation vs direction -> 13-05
- out -> 04-01
- outside zone (wide zone) -> 03-02
- overhang defender -> 05-05
- overload blitz -> 07-02
- overtime rules -> 10-04

**P**

- packaged play -> 04-06
- Palms (2-read, trap) -> 06-05
- participation data -> 13-01
- pass concept -> 04-04
- pass rush win rate (PRWR) -> 07-01
- pattern matching -> 06-01
- penetration -> 05-01
- personnel grouping -> 02-01
- Philly Special -> 12-06
- pin-and-pull -> 03-03
- pistol -> 02-02
- pistol option offense -> 12-05
- pitch -> 03-04
- platoon football -> 11-01
- play call -> 01-04
- play clock -> 01-01
- play-action -> 04-05
- play-by-play (pbp) -> 13-01
- playbook -> 01-04
- playside / backside -> 03-01
- plug -> 05-04
- plus territory -> 10-01
- plus-one -> 05-05
- poach -> 06-06
- pocket -> 04-02
- point of attack -> 03-01
- pop pass -> 04-06
- positional value -> 14-01
- possession -> 01-01
- post -> 04-01
- post-snap rotation -> 06-06
- post-snap RPO -> 04-06
- post-wheel -> 04-04
- power (Power O) -> 03-03
- Power I -> 02-03
- pre-snap read -> 04-03
- pre-snap RPO -> 04-06
- prediction log -> 01-06
- press -> 06-01
- pressure -> 07-01
- pressure look -> 07-03
- pressure rate -> 04-02
- prevent defense -> 10-04
- pro set (split backs) -> 02-03
- PROE (pass rate over expected) -> 13-04
- progression -> 04-01
- pull -> 03-01
- puller -> 03-03
- punt -> 01-02
- punter -> 01-03

**Q**

- QB counter -> 03-04
- QB draw -> 03-04
- QB hit / hurry -> 07-01
- QB power -> 03-04
- QB sneak -> 10-03
- quads -> 02-04
- quarter -> 01-01
- quarter (dollar) -> 02-06
- quarterback -> 01-03
- quarters (Cover 4) -> 06-05
- quick game -> 04-03

**R**

- reach block -> 03-01
- reach-and-overtake -> 03-02
- read (post-snap) -> 01-04
- read key (read defender) -> 03-04
- read safety -> 06-05
- read-option wave (2012) -> 11-04
- red zone -> 01-02
- reduced front -> 05-03
- reduced split -> 02-02
- replay review -> 09-03
- return motion (yo-yo) -> 02-05
- return unit -> 09-02
- returner -> 01-03
- reverse -> 03-05
- rhythm throw -> 04-03
- rip move -> 07-01
- robber -> 06-02
- rookie-contract window -> 14-01
- roughing the passer -> 09-03
- route conversion -> 04-04
- route participation -> 14-01
- route tree -> 04-01
- RPO (run-pass option) -> 04-06
- rub (pick) route -> 10-03
- run fit -> 05-05
- run-and-shoot -> 04-08
- run-through -> 05-04
- running back (halfback) -> 01-03
- rush lane -> 07-01
- rush three, drop eight -> 10-02
- RYOE (rush yards over expected) -> 13-02

**S**

- sack -> 07-01
- safety (position) -> 01-03
- safety (score) -> 01-01
- salary cap -> 11-02
- Sam linebacker -> 01-03
- scheme fit -> 14-01
- scramble drill -> 04-07
- scrape -> 05-04
- scrape exchange -> 03-04
- screen -> 04-05
- seal block -> 03-01
- seam -> 04-01
- seam-flat defender -> 06-03
- secondary -> 01-03
- self-scout -> 08-02
- separation -> 13-05
- sequencing -> 08-02
- series football -> 03-05
- set -> 01-05
- set the edge -> 05-01
- setup zone -> 09-02
- shade -> 03-01
- shadow corner -> 06-02
- shallow cross -> 04-04
- shell (coverage shell) -> 02-06
- shield (spread) punt -> 09-01
- shift -> 01-05
- shot play -> 04-05
- shotgun -> 02-02
- shovel pass -> 10-03
- sideline -> 01-01
- sideline camera -> 01-06
- sight adjust -> 04-02
- silent count -> 01-05
- simulated pressure (creeper) -> 07-03
- single wing -> 11-01
- singleback -> 02-03
- situational call sheet -> 08-03
- skill positions -> 01-03
- sky rotation -> 06-03
- skycam -> 01-06
- slant -> 04-01
- slant (line movement) -> 05-01
- slant-flat -> 04-03
- slide protection -> 04-02
- slot -> 02-02
- slot cornerback (nickel back) -> 01-03
- slow screen (RB screen) -> 04-05
- sluggo -> 04-01
- smash -> 04-04
- snag -> 04-03
- snap -> 01-04
- snap share -> 14-01
- snap-hold-kick -> 09-01
- spacing -> 04-03
- speed option -> 03-04
- speed out -> 04-03
- speed rush -> 07-01
- spike -> 10-04
- spill -> 05-05
- spin (safety rotation on motion) -> 02-05
- spin move -> 07-01
- split (receiver split) -> 02-02
- split-field coverage -> 06-06
- spot (of the ball) -> 01-02
- spot foul -> 09-03
- spot-drop zone -> 06-01
- spread offense -> 11-03
- spread option -> 11-03
- spy (QB spy) -> 10-02
- squib kick -> 09-02
- stack -> 02-04
- stack alignment -> 05-04
- stand-up edge (outside linebacker) -> 05-03
- standardised play direction -> 13-05
- stick -> 04-03
- sticks route -> 10-02
- stretch -> 03-02
- strong safety -> 01-03
- strong side -> 02-02
- stunt (game) -> 07-01
- substitution freeze -> 08-04
- substitution matching -> 02-01
- success rate -> 13-02
- sugar huddle -> 08-04
- swim move -> 07-01
- swing route -> 04-05
- swinging gate -> 02-04

**T**

- T-E stunt -> 07-01
- T-formation -> 02-03
- tackle (position) -> 01-03
- tag -> 01-04
- Tampa 2 -> 06-04
- target share -> 14-01
- technique (alignment number) -> 03-01
- tell -> 08-02
- tempo -> 08-04
- tendency -> 08-02
- tendency breaker -> 08-02
- tendency report -> 08-03
- the numbers (alignment landmark) -> 02-02
- the sticks (chains) -> 01-02
- third-down package -> 10-02
- three-high safety defense -> 11-03
- throwaway -> 04-07
- tight end -> 01-03
- time to throw -> 04-02
- timeout -> 01-01
- timing route -> 04-01
- tite front (mint) -> 05-03
- toss / sweep -> 03-03
- touchback -> 09-01
- touchdown -> 01-01
- tracking data -> 13-05
- trail technique -> 06-01
- trap -> 03-03
- travel (man defender follows motion) -> 02-05
- triangle read -> 04-04
- triple option -> 03-04
- tunnel screen -> 04-05
- turnover -> 01-02
- turnover on downs -> 01-02
- tush push -> 10-03
- two-gap -> 05-01
- two-high -> 02-06
- two-high counterrevolution -> 11-05
- two-minute drill -> 10-04
- two-minute warning -> 01-01
- two-point chart -> 10-04
- two-point conversion -> 01-01
- two-way concept -> 08-01

**U**

- unbalanced line (tackle over) -> 02-04
- unblocked rusher -> 07-02
- under center -> 02-02
- under-center revival -> 11-05
- unnecessary roughness -> 09-03

**V**

- veer -> 03-04
- verbiage (terminology) -> 01-04
- vertical set -> 04-02
- vice (jammer) -> 09-01
- victory formation (kneel-down) -> 10-04
- void years -> 14-01

**W**

- waggle -> 03-05
- walk-out -> 05-04
- weak side -> 02-02
- West Coast offense -> 04-08
- wheel -> 04-01
- whip -> 04-01
- wide receiver -> 01-03
- wide-9 -> 05-01
- wildcat -> 02-04
- Will linebacker -> 01-03
- win probability (WP) -> 13-03
- wing -> 02-02
- Wing-T -> 02-03
- wishbone -> 02-03
- WPA (win probability added) -> 13-03
- wristband -> 01-04

**X**

- X receiver (split end) -> 02-02
- xpass (expected pass rate) -> 13-04

**Y**

- Y receiver -> 02-02
- Y-cross -> 04-04
- YAC (yards after catch) -> 04-01
- YAC over expected (YACOE) -> 12-03
- yankee -> 04-04
- yard line -> 01-01
- yardline_100 -> 13-01
- year-over-year stability -> 13-02
- YPRR (yards per route run) -> 14-01

**Z**

- Z receiver (flanker) -> 02-02
- zone blitz -> 07-03
- zone blocking -> 03-02
- zone coverage -> 02-06
- zone read -> 03-04
- zoom motion -> 02-05

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

Derived from the chapter specifications (165 static, 68 animated, 62 data charts, 6 tracking figures in chapters, plus ~175 atlas plates).

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
