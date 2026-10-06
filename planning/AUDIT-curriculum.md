# Curriculum gap audit

_Independent audit of `CURRICULUM.md` (70 chapters, 632 terms) against `AUTHORING.md` and the user's goal. Done 2026-10-06. No chapters exist yet (`chapters/` is empty), so every fix below is cheap now and expensive later._

How to read this: Section A is the prioritized fix list, which is the deliverable. Sections B-F hold the evidence behind it: the coverage checklist, ordering defects, lookup audit, redundancy, and fact check. Each fix is tagged **MUST** (breaks a stated design principle or the user's stated goal, or is factually wrong), **SHOULD** (a real gap a high-level viewer would notice), or **NICE** (polish).

Mechanical check passed: every chapter's "Key terms introduced" list matches the Section 6 index exactly (632 terms, no term defined twice by ID). The problems below are about which terms exist, where they are defined, and when they are used. They are not bookkeeping errors.

---

## A. Prioritized fix list

### MUST (21)

**Ordering and prerequisite defects. These break the book's own rule, "Never use a concept before it is taught."**

- **M1. Swap 02-05 and 02-06.** 02-05 (Motion and Shifts) teaches "reveals man vs zone", "man/zone indicator", "spin (safety rotation)" and diagrams "jet motion vs man" and "vs zone: safety spins". But man coverage, zone coverage and safeties/shells are defined in 02-06, which comes *after* it. New order: 02-05 = A First Look at Defense, 02-06 = Motion and Shifts as Weapons. Change the Motion chapter's prerequisites to `02-04, 01-05, 02-05(new)`. Rename the slugs and update every downstream prerequisite (03-01 and 05-01 cite 02-06; 03-05 and 06-06 cite 02-05).
- **M2. Give EPA and success rate an early owner.** EPA appears in objectives and charts in 03-02, 03-04, 04-01, 04-04, 04-05, 05-05, 07-02, 10-01 and more, but it is defined in 13-02 (around chapter 61, Level 4). Add to **01-02** the objective "Read EPA and success rate as a per-play scorecard: what the number means, not how it is modelled." Move ownership of the terms *expected points (EP)*, *EPA* and *success rate* to 01-02. 13-02 keeps the model, its stability, and the selection-effect caveats, as a deepening. 01-02 already frames "field position as currency", so this is a natural fit.
- **M3. Move "blitz" and "four-man rush" to 02-06(new 02-05).** "Blitz" is used in 01-05 ("linebackers showing blitz"), 04-02 ("RB picks up a blitzing LB"), 04-03 ("answer to press and blitz") and 04-05, but it is defined in 07-02. The user explicitly listed it as a word they've heard but don't understand. Add the objective "Define a blitz (5+ rushers) vs a four-man rush; preview Part 7" to the first-look-at-defense chapter. 07-02 keeps blitz math and families.
- **M4. Move "rub (pick) route" from 10-03 to 04-04.** It is used in 02-04 ("rubs"), 04-04 (the "Mesh vs man: the rub" animation) and 06-02 (man-beaters), and 09-03 diagrams "Pick-play legality within 1 yard". All of these come before 10-03 defines it. Define it where mesh is first animated.
- **M5. Move "eligible tackle (tackle-eligible)" from 12-07 to 02-02.** 02-01's team example is "Lions six-OL jumbo with an eligible tackle". Formation legality (02-02) is where reporting as eligible belongs. Add the term *reporting eligible*, and the objective "Explain how an ineligible-numbered player reports eligible, and the 2015 reporting rule." 12-07 keeps the Lions-specific usage.
- **M6. Move "flexbone" from 11-03 to 02-03 (with wishbone).** 03-04 diagrams the "Triple option from flexbone" and cites "Navy / Georgia Tech flexbone". 11-03 keeps the lineage.
- **M7. Fix 01-05's premature vocabulary.** Its "Kill call: two plays called, check made on box count" diagram uses *box count* (02-06), and its "linebacker creeps to A-gap" animation uses *A-gap* (03-01). "Mike identification... sets the protection" (Level 2) assumes protection, which is not taught until 04-02. Either:
  - (preferred) move the term *Mike identification* and its objective to 04-02, leaving 01-05 a one-line gloss ("the offense names a reference defender so everyone blocks the same men"), and relabel the 01-05 diagrams generically ("defender walks into the gap between center and guard"); **or**
  - add explicit glosses plus forward links for box count, A-gap and protection to 01-05's forward-reference list.
- **M8. Add the missing forward-reference flags.** The book's rule requires them, and these are currently unflagged:
  - 01-03 → 02-01/02-06. Its diagrams are titled "vs 4-3 base" and "11 personnel vs nickel".
  - 01-06 → 13-03/13-05. Its broadcast-graphics objective uses win probability and Next Gen Stats.
  - 02-01 → 13-04. It charts "neutral situations".
  - 02-04 → 03-01 and 04-04. It uses crack blocks and rubs. "Two-way go" is never defined anywhere, so define it in 02-04 or 04-03.
  - 04-03 → 06-01 and 07-02. It uses press and blitz, and currently lists no forward references at all.
  - 04-05 → 05-05. It uses "run-fit triggers".
  - 09-03 → 10-03. It uses "tush push" in its live-rule-debates objective, but 10-03 defines the term.

**Coverage gaps a high-level viewer would hit on day one**

- **M9. Coaching staff roles are missing.** The terms *head coach, offensive coordinator, defensive coordinator, special teams coordinator, play-caller, position coach, quality control* and *game-management/analytics staff* are absent from the 632-term index. The user's entry point ("a play is what I pick in Madden") is precisely *who* picks the play. Add to **01-04** the objective "Map the staff: who calls plays (HC-as-caller vs coordinator), booth vs sideline, position coaches, QC and analytics staff", plus those terms. 08-03 deepens.
- **M10. The rules of the ball are missing.** There is no *catch rule* (rewritten in 2018), *forward progress*, *down by contact*, *fumble vs incomplete pass*, *fumble out of the end zone = touchback*, *lateral vs forward pass*, *intentional grounding* or *tackle box*. These are the most-argued calls on any broadcast, and grounding is strategically central (throwaways in 04-07, spikes in 10-04). Add them to 09-03, or to the new 09-04 (see S1). Add *tackle box* and *intentional grounding* to the term index. 04-07's "throwaway" objective must cross-reference them.
- **M11. Glossary aliases are unspecified, so lookups fail.** Terms are stored as `name (alias)`, for example *quarters (Cover 4)*, *simulated pressure (creeper)*, *man protection (BOB)*, *outside zone (wide zone)*, *quarter (dollar)*, *2-Man (Cover 5)*, *Palms (2-read, trap)*. A reader scanning "C" for **Cover 4** finds nothing, and there is nothing under "W" for **wide zone** or under "B" for **BOB**. Add an `aliases:` list to the glossary YAML schema in AUTHORING.md §3. The generator should emit a "see …" redirect entry and an anchor for each alias. Required aliases include, at minimum: Cover 4, Cover 5, creeper, sim pressure, BOB / big-on-big, wide zone, Power O, GT counter, counter trey, dollar, sail, nickel back, mug, man-free, rat, fire zone, fringe, yo-yo, power read, flanker, split end, trips, doubles, 2-read, trap coverage.
- **M12. Add comparison cards to the atlas.** The questions the user will actually ask are comparative, and the atlas has only one card per item:
  - **Appendix C**: a "4-3 vs 3-4 vs nickel" card. Cover hands down, who two-gaps, who the edge players are, body types, and why the labels blur. Today "4-3" and "3-4" are owned by 02-06 (the shallow chapter), with the real content split across 05-02, 05-03, 11-01 and 11-02.
  - **Appendix D**: a one-page "coverage family table" (Cover 0-9). Columns: deep defenders, under defenders, man/zone/match, strength, weakness, pre-snap tell, *post-snap* tell, chapter.
  - **Appendix A**: a "positions and labels" card (X/Y/Z/H/F, Mike/Will/Sam, nickel/star/money, technique numbers on one diagram).
- **M13. Add "post-snap tells" to the atlas card fields.** The current fields are name, diagram, what, why, strong/weak, *pre-snap* tells, teams, taught-in. For coverages and pressures the identifying evidence is post-snap (safety first step, corner bail vs squat, who drops). Add a `post-snap tells` field and a `see also` field, which also absorbs the case-study links.
- **M14. Correct the factual errors.** See Section F:
  - (a) 01-02 calls Super Bowl XXXIV's "One Yard Short" a "famous 4th-down stop". It was the game's final play (6 seconds left, ball at the Rams 10), not a fourth-down stop. Relabel it "last-play stop", or swap in a true 4th-down example such as the Super Bowl XLVII goal-line stand (verify first).
  - (b) Update fact flag #1 to resolved: Seattle 29, New England 13, Feb 8 2026, Levi's Stadium.
  - (c) Add the 2026 kickoff changes to 09-02 and Appendix E as "changed after the 2025 season".
  - (d) Resolve flags #3 and #10 (details in Section F).
- **M15. Reconcile AUTHORING.md and CURRICULUM.md.** AUTHORING.md says it wins, but the two conflict:
  - The chapter templates differ: "Opening hook / You'll be able to / Film room / Takeaways / Connections" vs "Cold open / You'll need / The problem / How the other side answers / By the numbers / Key terms".
  - Predict-the-play counts differ: 1-3 vs 3-5.
  - Length differs: 3,000-7,000 words vs 8-20 pages.
  - The glossary source differs: per-chapter front matter vs "a single YAML terms file".
  - The callout name differs: "Watch for it" vs "Watch for this on Sunday".
  - The book title differs: "Reading the Game" vs "Football, Explained".

  Write one merged template into AUTHORING.md and make CURRICULUM §2 point to it. Writers given both documents will produce inconsistent chapters.

**Ordering and level jumps**

- **M16. Move the coverage-reading half of 04-07 after Part 6.** 04-07 (Level 4) teaches "shell → key → progression" and safety look-offs, but coverages are taught in 06-01 to 06-06, *after* it. Split the chapter:
  - Keep pocket movement, progressions, scramble drill and QB style metrics in 04-07. Rename it "Quarterback Play: Progressions, the Pocket, and Off-Script Football", and drop its prerequisite-free use of "shell → key".
  - Move "reading the shell / key defender / look-offs" into 08-01 as a new first section, "How the quarterback reads coverage", with the objective "Map the QB's pre- and post-snap coverage read: shell, rotation, key defender, where the ball should go". Move the term *look-off* to 08-01.
- **M17. Move "draw play" from 10-02 to 03-03, and "sack" from 07-01 to 01-02.**
  - The draw is a basic run concept. Its QB version is defined in 03-04, before the generic one.
  - "Sack" is Level-1 vocabulary but is defined in 07-01, while 04-02 already charts "sack rate".
- **M18. Fix "pressure" vs "pressure rate".** 04-02 defines *pressure rate*, but *pressure* and *QB hit / hurry* are defined later in 07-01. Move *pressure* and *QB hit / hurry* to 04-02. 07-01 keeps "why pressure beats sacks".
- **M19. Consolidate the apex/overhang triple definition.** *apex (overhang) defender* is defined in 04-06, *apex alignment* in 05-04 and *overhang defender* in 05-05. That is the same idea under three entries. Define *apex* (an alignment) and *overhang defender* (a role) once, in the first-look-at-defense chapter (new 02-05), where the box is taught. 04-06 uses them as the RPO read, and 05-04/05-05 deepen without redefining.
- **M20. Define "end man on the line of scrimmage (EMOLOS)" in 03-04.** The 03-04 drill tells the reader to "locate the unblocked end-man-on-line", but the term is never defined. It is the core option and RPO read concept.
- **M21. Bring "split zone" into 03-02.** It is one of the most-run NFL plays of the Shanahan/McVay era (inside zone plus backside kick by the H/TE) and is absent. Add the term and a static diagram. Also add *wham* to 03-03 (trap family; see S-list).

### SHOULD (27)

**New or split chapters (keep the count small: three splits, no wholly new topics)**

- **S1. Split 09-03 into two chapters.** 09-03 already carries contact rules, holding, cut blocks, ineligible downfield, QB protection, free plays, challenges, replay, penalty data and live rule debates. With M10 added it becomes unwieldy.
  - **09-03 "Contact Rules and Penalties as Strategy"**: illegal contact, DPI/OPI, holding, illegal hands to the face, block in the back, chop/cut, roughing and the sliding QB, *defenseless player*, *use of the helmet (2018)*, horse-collar and the hip-drop tackle; accept/decline and half the distance.
  - **New 09-04 "Officiating, Replay, and the Rules of the Ball"** (Level 2, ~12 pp):
    - Objectives: name the seven on-field officials and where each stands (referee, umpire, down judge, line judge, side judge, field judge, back judge) and which fouls each watches; explain challenges vs booth review (scoring plays, turnovers, inside two minutes) and replay assist (introduced 2023, expanded since; check the 2026 ejection-review power); apply the catch rule, forward progress, down by contact, fumble/touchback rules, lateral vs forward pass, intentional grounding and the tackle box; read a referee's announcement.
    - Terms: *referee, umpire, down judge, line judge, side judge, field judge, back judge, booth review, replay assist, catch (completed pass), forward progress, down by contact, intentional grounding, tackle box, backward pass (lateral), fumble through the end zone*.
    - Diagrams: crew positions plate; catch-rule flowchart; tackle-box grounding plate.
  - Also add a college-vs-NFL rules table (see S4).
- **S2. Split 14-01 into two chapters.** Roster/cap/draft and fantasy were one of the four extras the user chose. One 18-page chapter covering positional value, cap mechanics, draft, roster rules *and* fantasy is too thin to be useful.
  - **14-01 "Building a Roster: Positional Value, the Cap, Free Agency, and the Draft"**: cap hit, signing-bonus proration, guarantees, dead money, void years, franchise/transition tag, UFA/RFA, compensatory picks, the rookie wage scale and fifth-year option, the trade deadline, waivers, IR and practice-squad elevations, draft value charts (Jimmy Johnson chart vs surplus-value curves, Massey-Thaler), the combine and pro days, and **player evaluation by position**. The last item is currently missing: what scouts grade at each position (QB processing/arm/accuracy; OL length, anchor, feet; edge bend and get-off; CB press/mirror, long speed; and so on), plus RAS as a data proxy and its limits.
  - **14-02 "Scheme and Fantasy"**: route participation, target share, air-yards share/WOPR, YPRR, snap share, RB usage, TE in 12 personnel, PROE, pace, game script, red-zone usage, PPR/half/standard scoring, ADP, and coordinator change as signal. Keep the existing scheme-shift drill.
- **S3. Split 15-01 into two chapters.** How-to-watch guides were a chosen extra. One chapter currently holds the master checklist, an All-22 four-pass protocol, game charting, a full annotated drive *and* Brier/calibration scoring.
  - **15-01 "Watching Live: The Master Checklist and Anticipation"**: checklist, tells catalogue (S7), the annotated drive, and in-game prediction.
  - **15-02 "Film Study: All-22, Charting a Game, and Scoring Yourself"**: the four-pass protocol, charting sheet, Brier score and calibration, and where to keep learning.

**Coverage additions folded into existing chapters**

- **S4. Add a college vs NFL rules difference table to Appendix E, owned by an objective in 11-03.** The table should cover:
  - hash width
  - one foot vs two feet in bounds
  - ineligible downfield: 3 yards in college vs 1 in the NFL (still 3 in 2026; a move to 1 was tabled in 2025)
  - DPI as a spot foul vs a 15-yard cap
  - OPI: 10 yards in college from 2026
  - the college clock (since 2023 it no longer stops on first downs except late in halves)
  - overtime format
  - targeting/disqualification
  - fair catch on kickoffs inside the 25, and the new college fair-catch kick (2026)
  - motion
  - two-minute timeouts
  - helmet communication

  Today these are scattered across 01-01, 04-06, 09-03 and 02-05. 11-03's drill already asks the reader to watch a college game.
- **S5. Add WR technique to 04-03.** Add the objective "Beat press: release moves, stem, stacking the defender, the break, the catch point", and the terms *release, stem, stacking (a defender), contested catch, double move*. The book teaches press from the DB side (06-01) but never the receiver side. Note that *double move* is used in 06-02 but never defined.
- **S6. Fill in OL technique and stunt pickup in 04-02.** Add the objective "How linemen pass off stunts and twists (switch vs stay)", and the terms *kick slide, punch, anchor, pass-off/switch*. 07-01 diagrams a "T-E stunt vs slide protection", but the offense's answer is never taught. Also add *scat protection* (6-man with a free-releasing back) and *empty protection (5-man)*.
- **S7. Add a tells catalogue to the first how-to-watch chapter and to 15-01.** Stance (heavy vs light hand, OL weight back on a pass set), RB depth/offset as run-direction tell, pistol vs gun, receiver splits (reduced split = crack or inside-breaking route), TE stance, LB depth, DB depth and leverage, safety width. Today only "pulling-lineman tells" (03-03) and coverage tells (06-06) exist. A tells catalogue was explicitly on the user's list ("anticipation").
- **S8. Add part-end "checklist so far" cards.** Place them at the ends of Parts 2, 4, 6 and 7, ideally as a closing section of the last chapter in each part. The master pre-snap sequence currently appears only in the final chapter. The user wants anticipation throughout, and the checklist should grow with the reader.
- **S9. Add broadcast metrics to 13-02.** The reader will hear *DVOA*, *PFF grades*, *passer rating*, *QBR*, *ANY/A*, *explosive play rate* and *ESPN pass-rush/run-stop win rate* every week, and none of them is in the curriculum. Add the objective "Place the broadcast metrics (passer rating, QBR, DVOA, PFF grades, win rates) relative to EPA: what each measures, open vs proprietary, when to distrust it", with those terms. Add a matching "metric cards" page to the atlas (see S10).
- **S10. Add a new Appendix G "Metrics and Data Atlas".** One card per metric: EPA, success rate, CPOE, aDOT, YAC/YACOE, RYOE, PROE/xpass, time to throw, pressure rate, PRWR, YPRR, target share, WP/WPA, DVOA, PFF grade, passer rating/QBR. Each card gives definition, scale and a "good" range, source (nflverse / NGS / FTN / proprietary), stability, and the chapter link. "Easy to look up" covers stats as much as schemes.
- **S11. Add clock-rule nuance to 10-04.** The game clock restarts on the ready signal after an out-of-bounds play, except in the last 2:00 of the first half and the last 5:00 of the second. Also cover the intentional safety, the free kick after a safety, and the fair-catch kick. Clock management cannot be explained without the out-of-bounds rule.
- **S12. Add two-point play design to 10-03.** Add the objective "Two-point plays from the 2: concepts and the best-percentage calls". It complements 10-04's two-point chart, which covers *whether*; 10-03 covers *what*.
- **S13. Fill out special-teams schemes in 09-01 and 09-02.**
  - 09-01: punt return schemes (wall/return left-right, middle return, punt rush/block, punt safe), rugby and pooch punts, muffed punt vs fumble, first touching, kick-catch interference, punt out of bounds. Terms: *muff, first touching, punt safe, punt block, rugby punt, pooch punt, kick-catch interference*.
  - 09-02: return blocking under the dynamic kickoff (setup-zone blocks, double teams), the onside "hands team", and *free kick*.
  - Change 09-02's prerequisite from 07-02 (blitzing) to 03-01. Return blocking uses blocking vocabulary; nothing in 09-02 needs blitz knowledge.
- **S14. Add a coverage number dialect objective to 06-01.** Widen "Cover 0-6 numbering" to **Cover 0-9**. Name *Cover 7* (match family / split-field in some dialects), *Cover 9* (often Cover 3 match or a split-field call, depending on the team), and *Cover 8* (rare), and point to the Appendix D dialect table. The user listed "Cover 0-9". As written, a reader who hears "Cover 9" on a broadcast cannot look it up.
- **S15. Add more motion types to the Motion chapter.** Add *glide* (motion parallel to the LOS behind the formation, to the flat at the snap), *trade* (TE trades sides), *short/"rip-liz" motion* and *rocket/rock motion*. The user specifically listed glide.
- **S16. Add tackling and pursuit to 05-04 or 05-05.** Add the objective "Pursuit angles, leverage tackling, and why missed tackles cluster at the second level", and the term *pursuit angle*. Tackling is absent from a 70-chapter football course. The single "pursuit" mention is incidental.
- **S17. Add history disputes and origins.**
  - **11-01**: Steve Owen's "umbrella" defense as an ancestor of the 4-3 (alongside Landry); Red Hickey's 1960 shotgun; the AFL (1960-69) as a passing laboratory (Gillman, Stram) and the merger.
  - **11-02**: Bill Arnsparger's 1972 Dolphins "53" defense as a 3-4 origin, and Arnsparger's 1980s Dolphins zone pressures alongside LeBeau's zone-blitz claim.

  AUTHORING §6 requires disputed origins to be presented as disputed.
- **S18. Add positional evolution to 11-05.** Add the objective "Why positions mutated: slot CB → nickel as base, big nickel/star, hybrid LB/S, move TE, the edge as the premium defender, the FB's niche revival". The pieces exist (11-04 move TE/hybrid edge, 05-04 safety-sized LBs, 02-06 big nickel) but no chapter connects them, and the user asked "why we are where we are".
- **S19. Add a light screen expansion to 04-05.** Add *now/smoke (quick) screen*, *flare* and *RB swing vs screen*. Now/smoke screens are the most common WR screens in the NFL and are absent. Consider moving the screens half to 04-03 as "quick game's cousins". Play-action, boots, *and* screens in one 14-page chapter is crowded.
- **S20. Add missing pass concepts to 04-04.** Add *angle (Texas) route*, *scissors* and *choice vs option*. Merge 04-08's *choice route* into 04-01's *option route* as an alias. They are the same idea under two names in two chapters.
- **S21. Fix the redundant signature diagrams (one home each).** Each diagram is built twice or three times:

  | Diagram | Appears in | Keep in | Other chapters |
  |---|---|---|---|
  | "One formation/look, four plays" | 08-02 and 12-03 | 08-02 (generic) | 12-03 links |
  | "Jet Chip Wasp" | 08-01 example and 12-04 [A] | 12-04 | 08-01 links |
  | Super Bowl XLIX interception | 08-01 example and 12-02 [A] | 12-02 | 08-01 links |
  | Tush push | 10-03 [A], 12-06 [S] and two near-identical [C] sneak-success charts | 10-03 | 12-06 shows only the Eagles-vs-league delta |
  | Safety rotation from tracking | 06-06 [T], 12-08 [T] and 13-05 [T] | 13-05 (built) | 06-06 shows the result; 12-08 links |
  | Air Raid mesh/Y-cross | 04-04, 04-08 and 11-03 | 04-04 | 04-08 and 11-03 link |
  | Super Bowl XXV/XXXVI/LIII game plans | 08-03 examples and 12-02 | 12-02 | 08-03 links |

  This saves an estimated 8-10 figures.
- **S22. Narrow 04-08 to naming and installing, and leave the stories to Part 11 and Part 12.** WCO, Air Coryell, run-and-shoot and Air Raid are taught in 04-08, again in 11-02/11-03, and WCO a third time in 12-01. Its objectives should be "how each system names plays, installs, and looks on film". Origins go in 11-02/11-03 and the WCO deep dive in 12-01. Drop the coaching-tree network from 04-08, or keep it only in Appendix E.
- **S23. Narrow the overlap between 12-08 and 06-05/06-06.** Fangio's 2018 Bears and 2024 Eagles, and Macdonald's Ravens/Seahawks, are the film-room examples in 06-05 and 06-06 *and* the subject of 12-08. Choose different film-room examples for 06-05/06-06 (Staley 2020 Rams, Evero, Flores, college quarters) so that 12-08 is fresh.
- **S24. Rename 10-01.** "Down, Distance, and Field Zones" is nearly the same title as 01-02 "Downs, Distance, and Field Position", which harms lookup. Rename it "Early Downs and Field Zones: How Situation Shapes the Call".
- **S25. Make sequencing shortcuts explicit in the reading-order note.** Add "09-01 and 09-02 can be read any time after Part 1". They are Level 2 but sit after a Level 5 part, so a linear reader drops from coach-level to beginner material.
- **S26. Clarify the prediction log origin.** The design principles say the prediction log is "started in 01-02", and 01-02's drill says "first entry", but the term and the setup belong to 01-06. Say once: baseline in 01-02, formal log from 01-06.
- **S27. Pilots: add a fourth, small pilot or a template smoke test.** See Section E. The three pilots never exercise:
  - (a) the **case-study template** (Part 12 uses a different skeleton);
  - (b) **code-shown analytics** (Part 13 shows code, everything else folds it);
  - (c) **rule currency** (09-02 kickoff rules change yearly: 2024, 2025 and 2026).

  Recommend 13-02 as pilot 4. It also validates the EPA primer moved by M2.

### NICE (16)

- **N1.** 03-01 is very dense for Level 2: gaps, hole numbers, 11 technique numbers, 12 block types, hat math and zone-vs-gap. Defer half the block library (log, seal, crack, cut) to the chapters that first use them, as "new block" boxes.
- **N2.** Let 03-01 own *3-technique*, *4i* and *5-technique*. It already teaches the full technique chart. 05-01 deepens the archetypes. (Lookup is unaffected either way, since the glossary links to one chapter.)
- **N3.** Add *Cover 2 invert*, *Cover 3 "Mable"/rip-liz* naming, and *2-read vs Palms* naming to the Appendix D dialect table.
- **N4.** Add the *Eagle* and *G* fronts as dialect notes in 05-03.
- **N5.** Add *wham* (03-03), *bash/insert/arc* (03-02) and *QB sweep* (03-04) as run concepts.
- **N6.** Add *rush plan, speed-to-power, cross-chop, ghost* to 07-01, and *mush rush* (contain vs mobile QBs) next to rush lanes.
- **N7.** Add *nickel/slot ("cat") blitz, safety blitz, edge pressure and "bear" pressure* as blitz-family labels in 07-02.
- **N8.** 09-01: weather, wind, altitude and dome effects on kicking. "Weather" appears once; give it a short data box.
- **N9.** 10-04: add the *intentional safety* and the *fair-catch kick* (see S11) as one-paragraph "rare but decisive" sidebars.
- **N10.** 01-03: note the 2023 jersey change (#0 allowed, wider ranges) alongside 2021. Note Aaron Donald retired after 2023, which is fine as an archetype if labelled.
- **N11.** 11-01: "dead-ball era" is borrowed from baseball and isn't standard football usage. Either define it explicitly as the book's own label, or call it "the 1970s scoring drought".
- **N12.** Add "turnover randomness" (fumble-recovery luck, interception variance) to 13-02. It is a staple of analytics talk.
- **N13.** Use a "you'll need" recap box (Design principles) for every Level 3+ chapter, not only Level 4-5. Part 3 chapters are the first to assume a lot.
- **N14.** Add a "see also: case study" line on Part 3-7 chapters, so readers moving between narrative and case studies can navigate.
- **N15.** Add a "Rule changes since the 2025 season" box to Appendix E (2026: onside declarable any time; receiving team 5 on the restraining line; kickoff-from-the-50 spotting fix; replay-center ejection power). Writers then won't silently mix 2025 and 2026 rules.
- **N16.** Add a "Recent staff moves" box to 12-03 and 12-08 and update fact flag #7. Klint Kubiak became Raiders head coach in Feb 2026, so "Kubiak's Seahawks" is a single season (2025). The Shanahan tree map must show him in Las Vegas.

---

## B. Coverage checklist (independent)

COVERED = taught with objectives and terms. THIN = mentioned, but not enough for a high-level viewer. MISSING = absent.

| Topic | Status | Where / fix |
|---|---|---|
| Field, scoring, clock basics | COVERED | 01-01 |
| Clock nuance (OOB restart outside 2:00/5:00) | MISSING | S11 |
| Downs, field position | COVERED | 01-02 |
| Positions and labels | COVERED | 01-03, 02-02 |
| Player evaluation and traits by position | MISSING | S2 |
| Who calls plays, staff roles | MISSING | M9 |
| Communication (radio, green dot, wristbands) | COVERED | 01-04 |
| Personnel groupings | COVERED | 02-01 |
| Formation legality and strength | COVERED | 02-02 |
| Classic formations (I, Power I, pro set, ace, wishbone) | COVERED | 02-03 |
| Spread, bunch, stack, empty, condensed | COVERED | 02-04 |
| Motion: jet, orbit, fly, return, zoom | COVERED | 02-05 |
| Motion: glide, trade | MISSING | S15 |
| Shifts and legal-motion rules | COVERED | 01-05 |
| Tempo / no-huddle | COVERED | 08-04 |
| Gaps, techniques, blocks | COVERED | 03-01 |
| Inside/outside zone | COVERED | 03-02 |
| Split zone | MISSING | M21 |
| Power, counter, duo, trap, iso, pin-pull | COVERED | 03-03 |
| Wham | MISSING | N5 |
| Draw | Defined too late | M17 |
| Option: zone read, veer, speed, triple, midline | COVERED | 03-04 |
| EMOLOS | MISSING | M20 |
| QB run game (power, counter, draw) | COVERED | 03-04 |
| Jet, reverse, Wing-T series | COVERED | 03-05 |
| Route tree and numbering | COVERED | 04-01 |
| WR release vs press, stems, double moves | MISSING | S5 |
| Pass protection (slide, half-slide, BOB, 6/7-man, max, chip, hot/sight) | COVERED | 04-02 |
| Scat and empty protection | THIN | S6 |
| OL stunt pickup, punch/anchor | MISSING | S6 |
| Quick game | COVERED | 04-03 |
| Dropback concepts | COVERED | 04-04 |
| Texas/angle, scissors | MISSING | S20 |
| Play-action, boot, naked | COVERED | 04-05 |
| Screens | THIN (no now/smoke) | S19 |
| RPO types incl. ineligible-downfield | COVERED | 04-06 |
| QB progressions, pocket, scramble | COVERED but misordered | M16 |
| Offensive systems and terminology | COVERED (redundant) | 04-08, S22 |
| DL techniques, one/two-gap | COVERED | 05-01 |
| Even fronts: Over, Under, wide-9, bear/46 | COVERED | 05-02 |
| Odd and nickel fronts: Okie, tite/mint | COVERED | 05-03 |
| LB keys and fits | COVERED | 05-04 |
| Tackling and pursuit | MISSING | S16 |
| Run fits: gap integrity, spill/box, force, plus-one | COVERED | 05-05 |
| Zones, press/off/bail/trail, MOFC/MOFO | COVERED | 06-01 |
| Cover 0/1, robber/rat, banjo, bracket | COVERED | 06-02 |
| Cover 3 (sky/buzz/cloud/match) | COVERED | 06-03 |
| Cover 2, Tampa 2, 2-Man | COVERED | 06-04 |
| Quarters, Cover 6, Palms, MOD/MEG | COVERED | 06-05 |
| Cover 7/9 dialects | THIN / MISSING | S14 |
| Disguise, rotation, split-field, poach | COVERED | 06-06 |
| Defensive communication / checks | THIN | 06-06 (3x1 checks); acceptable |
| Pass-rush moves and stunts | COVERED | 07-01 |
| Blitz math, overloads, mugs, Cover 0 | COVERED | 07-02 |
| Zone blitz, fire zone, sim pressure, creeper | COVERED | 07-03 |
| Concept vs coverage | COVERED | 08-01 |
| Constraint theory / sequencing / self-scout | COVERED | 08-02 |
| Weekly game plan | COVERED | 08-03 |
| In-game adjustments, substitution battle | COVERED | 08-04, 02-01 |
| FG/PAT/punt | COVERED | 09-01 |
| Punt return / block schemes, muffs | THIN | S13 |
| Kickoff 2024/2025 | COVERED | 09-02 |
| Kickoff 2026 | MISSING | M14c |
| Onside / squib | COVERED | 09-02 |
| Contact rules, PI, holding, roughing | COVERED | 09-03 |
| Intentional grounding, catch rule, forward progress, fumble rules | MISSING | M10 |
| Officiating crew mechanics, replay assist | MISSING / THIN | S1 |
| Challenges / replay | COVERED | 09-03 |
| College vs NFL rules | THIN (scattered) | S4 |
| Situational: early downs, 3rd down, red zone, goal line, 4th down, 2-min, 4-min, OT | COVERED | 10-01 to 10-04 |
| Two-point play design | MISSING | S12 |
| History: single wing, T, Paul Brown, Lombardi, Landry, Coryell, WCO, 46, zone blitz, R&S, Tampa 2, Air Raid, spread, RPO, two-high | COVERED | Part 11 |
| History: AFL, umbrella defense, 53 defense | MISSING | S17 |
| Positional evolution narrative | THIN | S18 |
| Analytics: EPA, SR, CPOE, WP, 4th-down bot, PROE, aDOT, YAC, pressure rate, TTT | COVERED but EPA misordered | M2 |
| DVOA, PFF, passer rating, QBR, explosives | MISSING | S9 |
| Tracking / NGS / BDB | COVERED | 13-05 |
| Roster, cap, draft, FA | THIN | S2 |
| Fantasy | THIN | S2 |
| How to watch: camera limits, All-22, where to look by phase | COVERED | 01-06, 15-01 |
| Pre-snap read sequence | COVERED, too late | S8 |
| Tells (stance, splits, depth, alignment) | THIN | S7 |

---

## C. Ordering and prerequisite defects (detail)

All of these appear in the fix list. This section records the evidence.

| Term or concept | First used | Defined | Fix |
|---|---|---|---|
| man / zone coverage, safety shells | 02-05 objectives and 2 animations | 02-06 | M1 |
| EPA | 03-02, 03-04, 04-01, 04-04, 04-05, 05-05, 07-02, 10-01, etc. | 13-02 | M2 |
| blitz | 01-05, 04-02, 04-03 | 07-02 | M3 |
| rub (pick) route | 02-04, 04-04, 06-02, 09-03 | 10-03 | M4 |
| eligible tackle | 02-01 | 12-07 | M5 |
| flexbone | 03-04 | 11-03 | M6 |
| box count, A-gap, protection | 01-05 | 02-06, 03-01, 04-02 | M7 |
| 4-3, 11 personnel, nickel | 01-03 diagrams | 02-01, 02-06 | M8 |
| WP, NGS | 01-06 | 13-03, 13-05 | M8 |
| neutral situation | 02-01 | 13-04 | M8 |
| crack block, two-way go | 02-04 | 03-01, never | M8 |
| press | 04-03 | 06-01 | M8 |
| run fit | 04-05 | 05-05 | M8 |
| tush push | 09-03 | 10-03 | M8 |
| coverage reading (shell → key, look-offs) | 04-07 | Part 6 | M16 |
| draw play | 03-04 (QB draw) | 10-02 | M17 |
| sack | 04-02 | 07-01 | M17 |
| pressure (vs pressure rate) | 04-02 | 07-01 | M18 |
| apex / overhang | 04-06, 05-04, 05-05 | three definitions | M19 |
| end man on line | 03-04 | never | M20 |
| double move | 06-02 | never | S5 |
| choice route vs option route | 04-04, 04-08 | duplicate concept | S20 |

**Level jumps.**
- 01-05 asks a Level 2 reader to absorb Mike ID and check-with-me systems.
- 02-05 (Level 3) sits inside a Level 1-2 part. After M1 it at least follows its prerequisite.
- 04-07 is Level 4 before any coverage chapter (M16).
- Part 9 (Level 2) follows Part 8 (Level 4-5) (S25).

---

## D. Lookup-ability audit

Five test queries:

| Query | Where it resolves today | Verdict |
|---|---|---|
| "What is Cover 6?" | Glossary C → 06-05; Appendix D card | OK |
| "What is 12 personnel?" | Glossary 0-9 → 02-01; Appendix A card | OK |
| "What is a 3-technique?" | Glossary → 05-01; Appendix C technique chart | OK. Technique numbers are taught in 03-01, so consider N2. |
| "Difference between a 4-3 and a 3-4?" | Glossary links each term to 02-06 (the shallow chapter); no comparison card; content spread over 02-06, 05-02, 05-03, 11-01, 11-02 | **Fails.** M12 |
| "What is an RPO?" | Glossary → 04-06; Appendix B | OK |
| "What is Cover 4?" / "wide zone" / "BOB" / "creeper" | Stored only as parenthetical aliases | **Fails.** M11 |
| "What is Cover 9?" | Absent | **Fails.** S14 |
| "What does DVOA / PFF grade mean?" | Absent | **Fails.** S9, S10 |
| "Was that a catch?" / "Why was that grounding?" | Absent | **Fails.** M10, S1 |
| "Who calls the plays for X?" | Absent | **Fails.** M9 |

**Atlas specification issues.**
- Card fields lack post-snap tells and see-also links (M13).
- There are no comparison or summary pages (M12).
- There is no metrics atlas (S10).
- The college-vs-NFL table is missing (S4).
- The rule-changes-since-2025 box is missing (N15).
- The glossary schema has no `aliases` field (M11).

---

## E. Pilot sanity

**01-04 (Level 1, tone).** A good choice. It is also the chapter most at risk of jargon leakage: it decomposes a call into formation, motion, *protection*, *concept* and *tags*, and uses *green dot* and *tempo*, all before they are taught. Treat that as the explicit test: every such word must be glossed and forward-linked. Fold M9 (staff roles) in before writing it.

**03-02 (Level 3, zone).** A good choice. It tests forward-reference discipline (front names) and the signature animation. Add split zone (M21) first. Note that it depends on the EPA primer (M2), because it has an EPA chart.

**06-06 (Level 5, disguise).** A sound test of the visual problem and the BDB adapter, with two risks:
- It sits on top of roughly 15 unwritten prerequisites, so a "beginner review" can only judge it through its "you'll need" box. Make that box an explicit part of the pilot test.
- Its tracking figure is duplicated in 12-08 and 13-05 (S21). Decide its home before building it.

**Missing from the pilot set:** the case-study template, a code-shown analytics chapter, and rule currency. 13-02 is the cheapest single addition (S27). 09-02 would test rule currency.

---

## F. Fact check

**Author's flags in §9, re-checked:**

1. **Super Bowl LX: verified.** Seattle 29, New England 13, Feb 8 2026, Levi's Stadium ([PFR box score](https://www.pro-football-reference.com/boxscores/202602080nwe.htm)). Kubiak was hired as Raiders head coach on Feb 9-10, 2026 ([AP via ABC30](https://abc30.com/amp/post/raiders-officially-hire-klint-kubiak-head-coach-super-bowl-win-seahawks/18579239/)). Update flag #7 and N16.
2. **Kickoff.** Changed again for 2026 ([Football Zebras](https://www.footballzebras.com/2026/04/nfl-owners-approve-rule-changes-for-the-2026-season/); [Buccaneers.com, Mar 31 2026](https://www.buccaneers.com/news/kickoffs-tweaked-again-in-nfl-short-list-2026-rules-changes)):
   - An onside kick can be declared at any point regardless of score.
   - The receiving team needs only 5 players on the restraining line (was 6).
   - A loophole in out-of-bounds/touchback spotting on kickoffs from the 50 was fixed.
   - Replay can eject a player for unflagged flagrant acts.

   The 2025 baseline (touchback to the 35) still needs a primary-source check at writing time.
3. **Tush push.** The May 2025 ban failed 22-10 (24 votes needed). No proposal was on the 2026 agenda, so it is legal for 2026 ([NBC Philadelphia](https://www.nbcphiladelphia.com/news/sports/nfl/philadelphia-eagles/without-a-proposal-this-year-is-the-tush-push-debate-finally-over/4374619/); [SteelersNOW](https://steelersnow.com/here-to-stay-no-discussion-on-banning-tush-push-in-2026/)).
4. **OT.** Not re-checked online. The 2025 regular-season "both teams possess" adoption matches my knowledge; verify at writing time.
10. **NCAA ineligible downfield.** Still 3 yards. A 2025 proposal to move to 1 yard was tabled ([FootballScoop](https://www.footballscoop.com/2025/03/04/ineligible-receiver-downfield-rule-tabled-ncaa)). 2026 college changes relevant to S4 ([2026 NCAA summary](https://gothunderwolves.com/news/2026/8/11/important-rule-changes-for-the-2026-college-football-season.aspx)): OPI reduced to 10 yards; a fair-catch kick added; two challenges per game; targeting second-half carryover removed.

**New red flags found in this audit:**

- **01-02: "One Yard Short" labelled a 4th-down stop.** Wrong framing. It was the final play with 6 seconds left, ball at the Rams 10 ([Wikipedia: Super Bowl XXXIV](https://en.wikipedia.org/wiki/Super_Bowl_XXXIV); [NFL 100](https://www.nfl.com/100/originals/100-greatest/games-16)). → M14a.
- **05-03: "Bum Phillips / Fritz Shurmur early 3-4."** Incomplete or misleading. The usual origins cited are Bill Arnsparger's "53" (1972 Dolphins) and Chuck Fairbanks (1974 Patriots), alongside Bum Phillips (1974 Oilers). Shurmur's 3-4 "Eagle" work is 1980s Rams. Verify and re-attribute. → S17.
- **07-03 / 11-02: zone blitz credited to LeBeau (Bengals origin).** Commonly repeated but disputed (Arnsparger's 1980s Dolphins, and earlier precedents). Present both. → S17.
- **11-01: "Landry's 4-3".** Present Steve Owen's umbrella defense as the precursor. → S17.
- **04-01: "Coryell numbering of the tree".** The attribution is plausible but loose (it is the Gillman-Coryell lineage, and numbering varies by system). Phrase it as "popularized by".
- **04-02: "2022 Bengals OL vs Chiefs".** Ambiguous: the 2021-season AFC title game (Jan 2022) or the 2022-season one (Jan 2023)? Specify the game.
- **14-01: "Brock Purdy's rookie contract".** He signed a 5-year extension in May 2025. Frame this as the 2022-24 surplus-value window, not current.
- **12-04: "Review the Super Bowl run (LIV, LV, LVII, LVIII, LIX)".** These are appearances; the Chiefs lost LV and LIX. Wording only.
- **02-02: "2015 ineligible-receiver trick".** The game was Jan 10, 2015 (2014 season divisional round) and the rule change came in 2015. Keep the season and the calendar year distinct.
- **11-01: "dead-ball era".** Not standard football usage (N11).
- **12-06: "Super Bowl LIX four-man pressure".** Consistent with reports that the Eagles generated pressure without blitzing; confirm the blitz count from a charting source before stating it.
- **03-02 / 12-03 / 11-05: "Kubiak's 2025 Seahawks".** Correct, but a single season (N16).

No other date or attribution in the curriculum looked wrong on review, and I checked these:
- Super Bowl LIX 40-22
- the 2021 jersey rule
- the 2015 PAT
- the 2005 push rule
- the 2004 illegal-contact emphasis after the Jan 2004 AFC title game
- the 2019 PI-review experiment
- the 2024 hip-drop ban
- 1978 Blount rule and pass-blocking hands
- 1993 free agency
- 1994 cap and two-point conversion
- 1972 hashes
- the 1940 73-0 game
- the 2022 playoff OT change after "13 seconds"
- Romer (2006)
- "2-3 Jet Chip Wasp" on 3rd-and-15 in Super Bowl LIV
- the 10 Hz tracking rate

---

## Revision log (2026-10-06)

All fixes were made in the curriculum source (`planning/curriculum-src/data1.py`, `data2.py`, `gen.py`, `tail.md`), then `CURRICULUM.md`, `chapters.yml`, and the `_quarto.yml` TOC were regenerated. `gen.py` validation passes. It now also checks alias uniqueness, the AUTHORING §4 cap of four animations per chapter, and that every chapter ID cited in objectives, notes, forward references, see-also lines, diagrams, and drills exists. Result: **73 chapters** (was 70), 758 terms plus 127 aliases. **64 of 64 audit fixes and 12 of 12 FACTS corrections were applied; none were skipped.**

**Structural changes**
- **Term aliases.** A term is written `headword | alias | alias`. The term index lists the headword with "also:", and each alias gets its own "see headword" entry. Validation covers names and aliases together.
- **Chapter fields.** Two new fields: `notes` (rendered as "Notes for the writer") and `see` (rendered as "See also (case studies)").
- **Length.** Length now renders as a word target (planning units × 375), so it matches AUTHORING's 3,000–7,000 words.
- **Appendices.** The appendix spec has new card fields, comparison pages, and Appendix G.
- **Renumbering.** Every ID that moved was updated wherever it appears:
  - 02-05 ↔ 02-06 (swapped)
  - 09-03 split into 09-03 and new 09-04
  - 14-01 split into 14-01 and new 14-02
  - 15-01 split into 15-01 and new 15-02
- **Slug changes.**
  - `02-05-a-first-look-at-defense`
  - `02-06-motion-and-shifts`
  - `09-03-contact-rules-and-penalties`
  - `09-04-officiating-replay-and-rules-of-the-ball`
  - `10-01-early-downs-and-field-zones`
  - `11-01-single-wing-to-scoring-drought`
  - `14-01-building-a-roster`
  - `14-02-scheme-and-fantasy`
  - `15-01-watching-live`
  - `15-02-film-study-and-charting`

### MUST
- **M1:** Swapped the two Part 2 chapters. 02-05 is now A First Look at Defense; 02-06 is Motion and Shifts, with prerequisites 02-04, 01-05, 02-05. Updated the downstream prerequisites:
  - 03-01 → 02-05
  - 05-01 → 02-05
  - 04-01 → 02-05
  - 06-01 → 02-05
  - 03-05 → 02-06
  - 06-06 → 02-06

  Also updated forward references, the design principles, the appendix text, and the pilot text.
- **M2:** 01-02 now owns *expected points (EP)*, *EPA*, and *success rate*. It gains the scorecard objective, an EPA-scorecard diagram, and a note. 13-02 keeps the model, stability, and selection effects as the deep treatment, with a note not to redefine the terms.
- **M3:** *Blitz* and *four-man rush* moved to 02-05, with the objective "Define a blitz (5+ rushers) vs a four-man rush". 07-02 now recaps them, keeps the blitz math, and adds blitz families.
- **M4:** *Rub (pick) route* moved from 10-03 to 04-04, with an objective and a forward reference to 09-03 on legality.
- **M5:** *Eligible tackle* moved from 12-07 to 02-02. Added the term *reporting eligible*, an objective on the 2015 reporting rule, and a diagram. 12-07 keeps the Lions usage.
- **M6:** *Flexbone* moved from 11-03 to 02-03 (formation list, plate, and family tree). 11-03 keeps the lineage. 03-04's diagram now cites 02-03.
- **M7 (preferred option):** *Mike identification* moved to 04-02. 01-05 now has a one-line gloss objective, generically relabelled diagrams (box count and A-gap removed), and forward references to 02-05, 03-01, and 04-02.
- **M8:** Added every listed forward reference:
  - 01-03 → 02-01 and 02-05
  - 01-06 → 13-03 and 13-05
  - 02-01 → 13-04, with neutral situations glossed in the diagram
  - 02-04 → 03-05 (crack, after N1) and 04-04 (rubs); *two-way go* is now defined in 02-04
  - 04-03 → 06-01 and 07-02
  - 04-05 → 05-05
  - 09-03 → 10-03
- **M9:** 01-04 gains the staff-map objective, eight staff terms (HC, OC, DC, ST coordinator, play-caller, position coach, QC coach, analytics staff), a staff-map diagram, and play-callers labelled by season. 08-03 deepens the staff roles.
- **M10:** The rules of the ball now live in the new 09-04: catch rule, forward progress, down by contact, fumble through the end zone, lateral, intentional grounding, and tackle box. 04-07's throwaway objective cross-references grounding, and 10-04 lists 09-04 as a prerequisite.
- **M11:** Added the alias syntax and its rendering, as described under Structural changes. Every required alias resolves in the index (Cover 4, Cover 5, creeper, sim pressure, BOB, big-on-big, wide zone, Power O, GT counter, counter trey, dollar, sail, nickel back, mug, man-free, rat, fire zone, fringe, yo-yo, power read, flanker, split end, trips, doubles, 2-read, trap coverage), plus about 100 more. AUTHORING §3 now documents `Term: {def: "...", aliases: [...]}`. `appendices/glossary.qmd` already supported this form, emitting a "See …" entry with its own anchor for each alias, so it needed no change.
- **M12:** Added three comparison pages: Appendix A "Positions and labels", Appendix C "4-3 vs 3-4 vs nickel", and Appendix D's Cover 0-9 coverage family table.
- **M13:** The atlas card fields now include *post-snap tells* and *see also*. See-also absorbs the case-study links.
- **M14:**
  - (a) 01-02 relabels "One Yard Short" as a last-play stop and adds the Super Bowl XLVII alternative, marked verify.
  - (b) Flag #1 is resolved.
  - (c) The 2026 kickoff changes are in 09-02's objectives, its notes, Appendix E, and N15's box.
  - (d) Flags #3 and #10 are resolved. Section 9 is rewritten from FACTS-current.
- **M15:** CURRICULUM §2 now summarises the AUTHORING template and defers to it:
  - book title *Reading the Game*
  - 1-3 predict drills
  - word lengths
  - glossary from front matter, with §6 as the ownership plan
  - "Watch for it" callouts
  - "Watch for it on Sunday" drill label

  AUTHORING.md received small gap-fills only:
  - the "You'll need" box for Level 3+ chapters, plus its callout
  - the case-study body shape
  - the alias YAML form
  - Part 13 shows its code
  - read FACTS-current.md first, and treat 2026 rules as "changed after the 2025 season"
- **M16:** 04-07 is retitled "Quarterback Play: Progressions, the Pocket, and Off-Script Football". Its "shell → key" objective and look-off animation were removed. 08-01 gains the "how the quarterback reads coverage" objective, the term *look-off*, two animations, and a prerequisite on 04-07.
- **M17:** *Draw play* moved to 03-03 (with a diagram); 10-02 references it. *Sack* moved to 01-02.
- **M18:** *Pressure* and *QB hit / hurry* moved to 04-02. 07-01 keeps "why pressure beats sacks".
- **M19:** *Apex* and *overhang defender* are defined once, in 02-05. They were removed from 04-06, 05-04, and 05-05, which now reference 02-05.
- **M20:** *End man on the line of scrimmage* (aliases EMOLOS, EMOL) is defined in 03-04, and the option-principle objective and the drill use it.
- **M21:** *Split zone* was added to 03-02 with an objective and a static diagram. *Wham* was added to 03-03.

### SHOULD
- **S1:** 09-03 became "Contact Rules and Penalties as Strategy", with new terms: hands to the face, block in the back, chop block, defenseless player, use of the helmet, horse-collar, hip-drop, and the 2026 three-strike policy. The new 09-04 "Officiating, Replay, and the Rules of the Ball" (Level 2) carries the seven officials, challenges vs booth review vs replay assist, and the rules of the ball, with a crew plate, a catch-rule flowchart, and a tackle-box plate. *Coach's challenge* and *replay review* moved into 09-04.
- **S2:** 14-01 split in two:
  - **14-01 "Building a Roster":** cap, acquisition, draft, player evaluation by position plus RAS, roster rules, and 25 terms.
  - **14-02 "Scheme and Fantasy":** usage metrics, WOPR, PPR/ADP, coordinator change as a signal, and the scheme-shift drill.

  The Purdy example is reframed as the 2022-24 window.
- **S3:** 15-01 split in two:
  - **15-01 "Watching Live":** checklist, tells catalogue, annotated drive, predictions.
  - **15-02 "Film Study":** All-22 protocol, charting, Brier score and calibration, further learning.
- **S4:** Added an 11-03 objective on college vs NFL rules and the full table in Appendix E, including the 2026 college changes, which are marked verify.
- **S5:** 04-03 gains the WR-vs-press objective and five terms: release, stem, stacking, contested catch, double move. Double move is now defined before 06-02 uses it.
- **S6:** 04-02 gains the stunt pass-off objective and terms (kick slide, punch, anchor, pass-off, scat and empty protection), plus a pass-off animation.
- **S7:** Built a tells catalogue in two stages. 01-06 starts it (objective, terms *tell* (moved from 08-02), *stance*, *heavy hand*, and a starter card). 15-01 carries the full catalogue objective and plate.
- **S8:** Added "checklist so far" cards to 02-06, 04-08, 06-06, and 07-03 (objective, diagram, and note each). 15-01's master card completes them.
- **S9:** 13-02 gains the broadcast-metrics objective and terms: passer rating, QBR, ANY/A, DVOA, PFF grade, run stop win rate, explosive play rate.
- **S10:** Added Appendix G "Metrics and Data Atlas" (about 18 metric cards plus a data-availability table). The appendix count is now 7.
- **S11:** 10-04 gains the out-of-bounds clock-rule objective and term, plus the intentional safety, free kick after a safety, and fair-catch kick.
- **S12:** 10-03 gains the objective "two-point plays from the 2" and a matching diagram.
- **S13:**
  - 09-01 gains a punt-return objective and terms: return wall, punt block, punt safe, rugby, pooch, muff, first touching, kick-catch interference.
  - 09-02 gains return blocking, the hands team, free kick, and restraining line.
  - 09-02's prerequisite changed from 07-02 to 03-01.
- **S14:** 06-01 now covers "Cover 0-9" with a dialect objective, the terms *Cover 8* and *Cover 9*, a dialect strip, and a COVER_9 data note.
- **S15:** 02-06 adds glide, trade, short (rip/liz), and rocket motion (terms, objective, plate).
- **S16:** 05-04 gains the tackling and pursuit objective, the terms *pursuit angle* and *leverage tackling*, and a diagram. The title now says "Tackling".
- **S17:**
  - 11-01 gains Steve Owen's umbrella defense, Red Hickey's 1960 shotgun, and the AFL with the merger.
  - 11-02 gains Arnsparger's "53" and the disputed zone-blitz origin.
  - 05-03 re-attributes the 3-4 origins and marks them disputed.
  - 07-03 presents LeBeau vs Arnsparger as disputed.
- **S18:** 11-05 gains the positional-evolution objective and a position-evolution map.
- **S19:** Added *flare* and the RB swing-vs-screen contrast to 04-05. Following the "consider moving" suggestion, the WR quick screens (*now/smoke*, *bubble*) moved to 04-03 as "quick game's cousins". 04-05 keeps the RB, OL, and TE screens.
- **S20:** 04-04 adds *angle (Texas) route* and *scissors*. *Choice route* is now an alias of 04-01's *option route*, and it was removed from 04-08.
- **S21:** Each signature diagram now has one home; other chapters link to it.

  | Diagram | Home | Change elsewhere |
  |---|---|---|
  | One formation, four plays | 08-02 | removed from 12-03 |
  | Jet Chip Wasp | 12-04 | 08-01 links |
  | Super Bowl XLIX | 12-02 | 08-01 links |
  | Tush push | 10-03 | 12-06 shows only the Eagles-vs-league delta |
  | Safety rotation | 13-05 builds it | 06-06 shows the result; removed from 12-08 |
  | Mesh/Y-cross | 04-04 | removed from 04-08 and 11-03 |
  | Super Bowl XXV/XXXVI/LIII plans | 12-02 | 08-03 links |

  08-01's repeat animations became static recap plates.
- **S22:** 04-08 is narrowed to naming and installing. It lost the coaching-tree network diagram, the 2025-staff objective, and the Air Raid diagram. *Coaching tree* moved to 12-01, and Appendix E keeps the trees.
- **S23:** 06-05 and 06-06 film-room examples changed to Staley's 2020 Rams, Evero, Flores, and college quarters. Fangio and Macdonald are reserved for 12-08.
- **S24:** 10-01 is renamed "Early Downs and Field Zones: How Situation Shapes the Call", with slug `early-downs-and-field-zones`.
- **S25:** The reading-order note now says 09-01 can be read any time after Part 1 and 09-02 any time after 03-01. The Part 9 blurb says the same.
- **S26:** The prediction log is stated once: baseline in 01-02, formal log from 01-06, scored in 15-02. This appears in the design principles, 01-02's drill, 01-06, and the Part 1 and Part 15 blurbs.
- **S27:** Added 13-02 as pilot 4. The pilot section explains which gaps it covers. The case-study shape and rule currency are still not covered by any pilot, so the section recommends outline smoke tests of 12-03 and 09-02 before mass production.

### NICE
- **N1:** 03-01 keeps eight core blocks. The other four now appear as "new block" boxes in the chapter that first needs each one:
  - *cut* → 03-02
  - *log* → 03-03
  - *crack* and *seal* → 03-05
- **N2:** 03-01 now owns *3-technique*, *4i*, and *5-technique*. 05-01 deepens them.
- **N3:** Appendix D's dialect table adds Cover 2 invert, Cover 3 "Mable" and rip-liz naming, 2-read vs Palms, and the Cover 7/8/9 variants.
- **N4:** 05-03 adds the *Eagle front* and *G front* as dialect notes, with a diagram.
- **N5:** Added *wham* (03-03), *bash*, *insert* and *arc* (03-02), and *QB sweep* (03-04).
- **N6:** 07-01 adds *rush plan*, *speed-to-power*, *cross-chop*, *ghost*, and *mush rush*.
- **N7:** 07-02 adds the blitz-family labels: *nickel (cat) blitz*, *safety blitz*, *edge pressure*, *bear pressure*. Includes a plate.
- **N8:** 09-01 adds a weather data box (dome vs outdoor, cold vs warm). Its objective now names wind, temperature, altitude, and dome.
- **N9:** 10-04 adds sidebar plates for the intentional safety and the fair-catch kick.
- **N10:** 01-03 now notes the 2023 jersey change, and its Aaron Donald example is labelled "retired after 2023".
- **N11:** 11-01 is retitled "From the Single Wing to the 1970s Scoring Drought" (slug changed). The term *dead-ball era* was dropped.
- **N12:** 13-02 adds turnover randomness (objective, term, and a fumble-recovery chart).
- **N13:** Every Level 3+ chapter now gets a "You'll need" box. This is stated in the design principles, CURRICULUM §2, and AUTHORING §2/§3.
- **N14:** Part 3-7 chapters gain "See also (case studies)" lines, except 06-03 and 06-04, which have no natural case study.
- **N15:** Appendix E gains a "Rule changes since the 2025 season" box.
- **N16:** 12-03 and 12-08 gain recent-staff-moves boxes. Flag #7 was updated: Kubiak's Seattle tenure is labelled as the 2025 season only, and the 2026 tree map shows him with the Raiders.

### FACTS-current corrections
- **C1:** 12-07 now has the full Lions chain: Morton fired, Campbell calling plays mid-2025, Petzing as 2026 OC, Sheppard remaining DC. 14-02 uses it as a test case.
- **C2:** 12-03's tree objective now gives separate 2025 and 2026 maps (Kubiak Raiders HC, McDaniel Chargers OC, Mike LaFleur Cardinals HC, Fleury Seattle OC). 04-08's tree was removed (S22), and 03-02 labels Kubiak as a single season.
- **C3:** 12-05 is written as a closed 2019-2025 era (title, objective, note), with the 2026 Harbaugh, Monken, and Minter changes as an epilogue.
- **C4:** 12-04 has an objective on the OC line (Bieniemy, then Nagy 2023-2025, then Bieniemy in 2026). The Super Bowl wording is corrected to "won LIV, LVII, LVIII; lost LV, LIX".
- **C5:** Coverage-data caveats were added to:
  - the design principles
  - 06-01, 06-02, 06-05, and 06-06
  - 13-01 and 13-04
  - Appendix G
- **C6:** 11-05's two-high series now starts in 2018 and marks the source break.
- **C7:** 02-06 carries the FTN `is_motion` definition note and the motion series with their sources.
- **C8:** 09-02 and Appendix E are current to 2026.
- **C9:** 09-03, 10-03, and 12-06 note that no ban was proposed in 2026 and that the tush push is legal. The charts use `is_qb_sneak`.
- **C10:** 12-06 and 12-08 note that Fangio is still DC and that Mannion is the 2026 OC (the fifth new OC in five years).
- **C11:** Section 9, flag #1, is resolved.
- **C12:** 04-06, 11-03, and flag #10 state that college is still at 3 yards. The audit (2025) and FACTS-current (2015) disagree on the year the 1-yard proposal was tabled. That conflict is flagged for verification rather than guessed.

Other fact-check items from Section F were also folded in:
- 04-01's numbering is now "popularized by the Gillman-Coryell lineage".
- 04-02's Bengals-Chiefs game is specified as the 2022-season AFC Championship, marked confirm.
- 02-02 now distinguishes the 2014 season from the January 2015 game.
- 12-06 asks writers to confirm the Super Bowl LIX blitz count.
- Trend numbers with sources were added to 02-01, 02-03, 02-05, 02-06, 06-05, and 11-05.
