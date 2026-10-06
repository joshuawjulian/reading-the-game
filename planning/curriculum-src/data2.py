# Curriculum data, Parts 7-15 (term syntax: see data1.py)
from data1 import part, ch

# ---------------------------------------------------------------- PART 7
part("07", "Pressure: Rush, Blitz, and Simulated Pressure", "3-4",
     "How defenses attack the quarterback: winning one-on-one, adding rushers, and the modern art of making four "
     "rushers look like six.")

ch("07-01", "pass-rush", "The Pass Rush: Moves, Stunts, and Why Pressure Beats Sacks", 3, 13,
   ["Explain get-off, the rush arc, the main moves (speed, bull, long arm, swim, rip, spin, counters), and the rush plan "
    "(setting up moves, speed-to-power, cross-chop, ghost).",
    "Diagram stunts/games: T-E, E-T, loop, twist.",
    "Explain rush lanes, contain, and the mush rush vs mobile QBs.",
    "Explain why pressure (04-02) is more stable than sacks and how QBs drive sack rate.",
    "Use pass-rush win rate and time-to-pressure metrics."],
   ["get-off", "speed rush", "bull rush", "long arm", "swim move", "rip move", "spin move", "speed-to-power", "cross-chop",
    "ghost (rush move)", "rush plan", "stunt | pass-rush game", "T-E stunt", "E-T stunt", "rush lane", "mush rush",
    "pass rush win rate | PRWR"],
   ["04-02", "05-01"],
   ["S: Rush-move sequence frames (6 mini panels)", "A: T-E stunt vs slide protection (frame strip)",
    "S: Rush lanes and the mush rush vs a mobile QB", "C: Sack rate vs pressure rate, team-season scatter"],
   ["Lawrence Taylor", "Reggie White", "Aaron Donald", "T.J. Watt",
    "Myles Garrett (2025 single-season record, 23.0 sacks; FACTS-current §2)", "Micah Parsons"],
   "Count the seconds: stopwatch from snap to first pressure; note whether the ball was already out.",
   see=["12-06"])

ch("07-02", "blitz-and-man-pressure", "Blitzing: Numbers, Overloads, A-Gap Mugs, and Cover 0", 3, 13,
   ["Recap the blitz (02-05) and do blitz math: rushers vs protectors, who is free, where the hot throw goes.",
    "Diagram man pressures: Cover 1 blitz, Cover 0, overloads.",
    "Name blitz families: nickel (cat), safety, edge, and bear pressure.",
    "Explain double A-gap mugs and why they break protection rules.",
    "Analyse blitz rate vs EPA allowed (high variance, situational value)."],
   ["five-man pressure", "overload blitz", "nickel blitz | cat blitz", "safety blitz", "edge pressure", "bear pressure",
    "double A-gap mug | A-gap mug | mug", "Cover 0 blitz", "Cover 1 blitz", "unblocked rusher"],
   ["07-01", "06-02"],
   ["A: Overload blitz vs half-slide, RB picks wrong man (frame strip)",
    "S: Double A-gap mug: three post-snap variants from one look", "S: Cover 0 blitz vs empty -> hot throw",
    "S: Blitz-family plate: cat, safety, edge, bear",
    "C: Blitz rate vs EPA/dropback allowed by team (FTN n_blitzers, 2022+)"],
   ["Buddy Ryan", "Rex Ryan", "Steve Spagnuolo (2007 Giants, Chiefs Cover 0)", "Brian Flores (Dolphins; Vikings DC 2023-)"],
   "Count the rushers: four or more? If more, predict a quick throw and to which side.",
   see=["12-04"])

ch("07-03", "zone-blitz-and-simulated-pressure", "Zone Blitzes, Fire Zones, and Simulated Pressure", 4, 14,
   ["Explain the zone-blitz idea: rush an unexpected defender, drop a lineman, play three-deep three-under.",
    "Diagram fire-zone variants and their hot-zone holes.",
    "Define simulated pressure (creeper): four rushers from unexpected places, seven in coverage.",
    "Explain how sim pressure wins one-on-ones by defeating protection rules without sacrificing coverage.",
    "Narrate the protection-vs-pressure contest: Mike ID, slide direction, hot throws.",
    "Checklist so far (Parts 1-7): add pressure tells (mugs, walked-up safeties, who could drop) to the card."],
   ["zone blitz", "fire zone | 3-under 3-deep pressure", "simulated pressure | sim pressure | creeper",
    "dropper (DL in coverage)", "pressure look"],
   ["07-02", "06-03"],
   ["A: Fire zone vs 2x2: DE drops to the hook (frame strip)", "A: Creeper from nickel (frame strip)",
    "S: Protection bust: slide toward the threat, rush from the other side",
    "S: 1990s Steelers zone-blitz plate", "S: Checklist-so-far card (Parts 1-7)"],
   ["The zone blitz's origin, presented as disputed: Dick LeBeau (Bengals roots, 'Blitzburgh' Steelers) vs Bill Arnsparger's 1980s Dolphins zone pressures",
    "Dom Capers", "Mike Macdonald (Ravens DC 2022-23, Seahawks HC 2024-)", "Brian Flores' Vikings", "Spagnuolo"],
   "Who dropped? After the snap find the lineman who dropped into coverage, and who replaced him as a rusher.",
   fwd=["12-08 (Macdonald)"],
   notes=["Part-end card (audit S8): close with the 'checklist so far' card, now covering Parts 1-7."],
   see=["12-08"])

# ---------------------------------------------------------------- PART 8
part("08", "The Chess Match", "4-5",
     "Offense and defense together: how the quarterback reads coverage, which concepts beat which coverages, how plays are "
     "sequenced to set each other up, how a week of game-planning works, and how adjustments and tempo play out on Sunday.")

ch("08-01", "concepts-versus-coverages", "What Beats What: Reading Coverage and Pass Concepts Versus Coverages", 4, 17,
   ["Map the QB's pre- and post-snap coverage read: shell, rotation, key defender, where the ball should go (including look-offs).",
    "Build the concept x coverage matrix (smash vs Cover 2, four verts and flood vs Cover 3, dagger vs quarters, mesh vs man, ...).",
    "Explain why 'beaters' are probabilistic given match rules and disguise.",
    "Explain two-way concepts with a man answer and a zone answer built in.",
    "Show the defense's counters (Cover 3 match vs four verts, Palms vs smash).",
    "Practise identify-then-predict on animated plays."],
   ["look-off", "coverage beater", "two-way concept", "alert | shot alert"],
   ["06-06", "04-04", "06-02", "04-07"],
   ["A: How the QB reads coverage: shell -> rotation -> key -> throw (frame strip)",
    "A: Safety look-off: QB eyes hold the safety, throws opposite (frame strip)",
    "S: Concept x coverage matrix, colour-coded by expected advantage",
    "S: Smash vs Cover 2 (recap of the 06-04 animation)", "A: Flood vs Cover 3 (frame strip)",
    "A: Dagger vs quarters (frame strip)", "S: Mesh vs Cover 1 (recap of the 04-04 animation)",
    "S: Smash vs Palms: the defense wins"],
   ["Famous cases live elsewhere; link, don't redraw: 'Jet Chip Wasp' (12-04) and the Super Bowl XLIX interception (12-02)",
    "Recent concept-vs-coverage examples from 2023-2025 film, chosen at writing time (verify each)"],
   "Predict the open man: once you ID the coverage at the snap, name who will be open before the throw.",
   notes=["Audit M16: the coverage-reading half of the old 04-07 lives here, after Part 6.",
          "Animations capped at four (AUTHORING §4); repeats of earlier animations are static recap plates."],
   see=["12-02", "12-04"])

ch("08-02", "constraint-theory-and-sequencing", "Constraint Theory: How Plays Talk to Each Other", 4, 13,
   ["Explain base plays vs constraint plays and the 'illusion of complexity'.",
    "Explain sequencing: setting up a counter, tendency breakers, play-action off the base run.",
    "Explain self-scouting and formation tells (tells introduced in 01-06).",
    "Show the defense's version: one pressure look, several coverages.",
    "Find a team's tendencies by formation/personnel in data."],
   ["base play", "constraint play", "illusion of complexity", "sequencing", "tendency", "tendency breaker",
    "self-scout"],
   ["08-01", "03-05", "04-05"],
   ["S: Constraint tree: wide zone -> boot / naked / keeper / counter",
    "S: One formation, four plays (Shanahan-style plate)",
    "C: Tendency table: formation x personnel -> pass rate for one team"],
   ["Shanahan wide-zone family", "Wing-T series", "Reid's Chiefs", "Ben Johnson's Lions sequencing (2022-2024)"],
   "Call the follow-up: after a big run from a look, predict play-action from the same look within the next few snaps.",
   notes=["Signature-diagram home for 'one formation, four plays'; 12-03 links here (audit S21)."])

ch("08-03", "game-planning-week", "The Game Plan: A Week Inside an NFL Building", 4, 14,
   ["Walk through a game week: film, install, situational practice days.",
    "Explain call sheets organised by situation and the opening script.",
    "Explain matchup hunting and 'take away their best thing'.",
    "Explain how a staff scouts an opposing coordinator and QB.",
    "Describe tendency reports and the roles of QC and analytics staff (staff map from 01-04, deepened)."],
   ["game plan", "opening script", "situational call sheet", "matchup | mismatch", "tendency report",
    "game-plan package"],
   ["08-02"],
   ["S: Annotated call-sheet mock-up", "S: Game-week calendar",
    "C: Matchup heatmap for a sample game (slot vs nickel, TE vs LB, etc.)",
    "S: 'Take away the best thing': normal alignment vs game-plan alignment"],
   ["Belichick's Super Bowl plans (XXV, XXXVI, LIII) are drawn in 12-02; link there", "Walsh's scripted 15",
    "Andy Reid's play sheet"],
   "Script detector: watch the first 15 offensive plays; list anything you haven't seen from this team before.",
   fwd=["12-02 (Belichick case study)"],
   see=["12-02"])

ch("08-04", "in-game-adjustments-and-tempo", "In-Game Adjustments, Tempo, and the Sideline Battle", 4, 13,
   ["Explain between-series adjustments (tablets, coaching booth) and halftime adjustments.",
    "Explain tempo and no-huddle: freezing substitutions and simplifying the defense.",
    "Explain defensive answers to tempo (simplified calls, check-with-me).",
    "Describe coordinator-vs-coordinator 'call after the call'.",
    "Test the halftime-adjustment narrative with second-half data."],
   ["tempo", "hurry-up offense", "sugar huddle", "substitution freeze", "halftime adjustment", "coaching booth"],
   ["08-03"],
   ["C: Seconds between snaps by team (tempo distribution)", "S: Substitution-matching rule timeline",
    "S: Before/after adjustment example as frame pairs"],
   ["Bills K-Gun", "Peyton Manning's no-huddle", "Chip Kelly's 2013 Eagles", "Chiefs' second-half motion TDs in Super Bowl LVII"],
   "Adjustment hunter: list what changed after halftime (personnel, motion, coverage, pressure).")

# ---------------------------------------------------------------- PART 9
part("09", "Special Teams and the Rules That Shape Strategy", "2-3",
     "The third phase and the rulebook. Placed before situational football because fourth-down, end-of-half, and "
     "red-zone decisions depend on kicking ranges, on the contact/penalty rules, and on the rules of the ball. "
     "09-01 can be read any time after Part 1 and 09-02 any time after 03-01.")

ch("09-01", "kicking-and-punting", "Field Goals, Extra Points, and the Punting Game", 2, 14,
   ["Explain FG/PAT mechanics: snap-hold-kick timing, protection, block units.",
    "Compute FG distance from the line of scrimmage and reason about range (kicker, wind, temperature, altitude, dome).",
    "Explain the 2015 PAT change and its effect on two-point attempts.",
    "Diagram punt formations (shield/spread), gunners, vices; directional and coffin-corner punting; fair catch and downing.",
    "Explain punt returns and their rules: wall and middle returns, punt rush/block, punt safe, rugby and pooch punts, "
    "muff vs fumble, first touching, kick-catch interference, punts out of bounds.",
    "Explain fakes and why they are rare.",
    "Show FG accuracy by distance across eras."],
   ["field goal range", "snap-hold-kick", "shield punt | spread punt", "vice | jammer", "fair catch", "coffin-corner punt",
    "touchback", "net punting average", "fake punt / fake field goal", "return wall | wall return", "punt block",
    "punt safe", "rugby punt", "pooch punt", "muff", "first touching", "kick-catch interference"],
   ["01-02", "01-03"],
   ["S: FG formation and protection", "A: Shield punt and coverage lanes (frame strip)",
    "S: Punt return wall vs punt safe",
    "C: FG% by distance by era", "C: Weather box: FG% by distance, dome vs outdoor and cold vs warm",
    "C: Punt landing spot heatmap"],
   ["Justin Tucker", "Brandon Aubrey's long-range kicking", "Cam Little's 67-yard FG in 2025 (LIKELY; verify)", "Notable fake punts"],
   "Range finder: on every 4th down, predict go / punt / FG before the offense lines up.")

ch("09-02", "kickoffs-and-returns", "Kickoffs, Returns, and the Dynamic Kickoff", 2, 12,
   ["Explain the traditional kickoff and why the league kept changing it (injury data).",
    "Explain the 2024 dynamic kickoff (setup zone, landing zone) and the 2025 permanent version (touchback to the 35; onside declarable whenever trailing).",
    "Explain the 2026 changes, labelled 'changed after the 2025 season': onside declarable at any time; only 5 receiving players required on the "
    "restraining line (a 'floater' allowed); kickoffs from the 50 that go out of bounds or into the end zone now spot at the 20.",
    "Explain the strategic consequences: return rates (about 22% in 2023 -> about 75% in 2025), squibs, landing-zone choices, touchback math.",
    "Explain onside kicks and the hands team under current rules.",
    "Describe return blocking under the dynamic kickoff: setup-zone blocks and double teams."],
   ["kickoff", "free kick", "dynamic kickoff", "landing zone", "setup zone", "restraining line", "onside kick", "hands team",
    "squib kick", "kick coverage unit", "return unit"],
   ["09-01", "03-01"],
   ["S: Dynamic kickoff alignment plate (2026 rules; 2024/2025 differences annotated)",
    "A: Dynamic kickoff from kick to tackle, with return blocks (frame strip)",
    "S: Old vs new kickoff side by side", "C: Return rate and average starting field position by season, 2019-2025"],
   ["League-wide 2024 vs 2025 return behaviour (nflverse: 32.9% -> 74.6% of regular-season kickoffs returned)",
    "Teams that exploited landing-zone rules"],
   "Field-position ledger: log each kickoff's starting yard line; compute the game average.",
   notes=["Rule-currency chapter: kickoff rules changed in 2024, 2025, and 2026. Write against FACTS-current §3 and label every rule with its season.",
          "Prerequisite changed from 07-02 to 03-01 (audit S13): return blocking needs blocking vocabulary, not blitz knowledge."])

ch("09-03", "contact-rules-and-penalties", "Contact Rules and Penalties as Strategy", 3, 13,
   ["Explain the 5-yard contact zone, defensive holding, illegal contact, DPI and OPI, and their scheme consequences "
    "(spot foul, throwing deep for DPI, pick-play legality).",
    "Explain offensive holding, illegal hands to the face, block in the back, chop/cut-block legality, and ineligible-downfield enforcement.",
    "Explain player-safety rules: roughing the passer, the sliding QB, the defenseless player, use of the helmet (2018), "
    "horse-collar and hip-drop (2024) tackles, and the 2026 three-strike suspension policy.",
    "Explain free plays, accept/decline, and half-the-distance enforcement.",
    "Show penalty rates by type and how penalties enter EPA.",
    "Summarise live rule debates (tush push: the 2025 ban failed 22-10, no proposal in 2026; hip-drop enforcement)."],
   ["illegal contact", "defensive holding", "offensive holding", "defensive pass interference | DPI",
    "offensive pass interference | OPI", "spot foul", "illegal hands to the face", "block in the back", "chop block",
    "roughing the passer", "unnecessary roughness", "defenseless player", "use of the helmet (2018 rule)",
    "horse-collar tackle", "hip-drop tackle", "free play", "accept / decline (penalty)", "half the distance"],
   ["06-01", "04-06", "04-02"],
   ["S: The 5-yard contact zone", "S: Pick-play legality within 1 yard",
    "S: DPI enforcement: NFL spot foul vs college 15-yard cap", "C: Penalty rates by type 2015-2025"],
   ["2003-season AFC Championship (Jan 2004) and the 2004 illegal-contact emphasis",
    "2018 NFC Championship no-call -> 2019 PI review experiment", "2024 hip-drop tackle ban",
    "2025 tush-push vote (failed 22-10) and no 2026 proposal"],
   "Flag predictor: when a flag flies, guess the foul before the announcement and how it changes the series.",
   fwd=["10-03 (the tush push)", "09-04 (officials, replay, and the rules of the ball)",
        "11-02 / 11-04 (rule changes in historical context)", "Appendix E (rule-change timeline)"],
   notes=["Split from the old 09-03 (audit S1). The three-strike policy is LIKELY in FACTS-current §6; re-verify before printing."])

ch("09-04", "officiating-replay-and-rules-of-the-ball", "Officiating, Replay, and the Rules of the Ball", 2, 12,
   ["Name the seven on-field officials (referee, umpire, down judge, line judge, side judge, field judge, back judge), where each stands, "
    "and which fouls each watches.",
    "Explain coach's challenges (two, plus a third if either succeeds, since 2024) vs booth review (scoring plays, turnovers, inside two minutes).",
    "Explain replay assist (introduced 2023, verify; expanded 2025 to overturn certain flags) and the 2026 power to consult on ejections "
    "for flagrant acts; there is no full sky judge.",
    "Apply the rules of the ball: the catch rule (rewritten 2018), forward progress, down by contact, fumble vs incomplete pass, "
    "a fumble through the end zone (touchback), lateral vs forward pass.",
    "Apply intentional grounding and the tackle box (why a throwaway must reach the line of scrimmage once the QB is outside the box).",
    "Read a referee's announcement, and know the 2025 virtual first-down measurement."],
   ["referee", "umpire", "down judge", "line judge", "side judge", "field judge", "back judge", "coach's challenge",
    "replay review", "booth review", "replay assist", "catch (completed pass)", "forward progress", "down by contact",
    "fumble through the end zone (touchback)", "backward pass | lateral", "intentional grounding", "tackle box",
    "virtual measurement | Hawk-Eye measurement"],
   ["09-03", "04-07"],
   ["S: Officiating crew positions plate", "S: Catch-rule flowchart (control, feet or body part down, football move)",
    "S: Tackle-box grounding plate", "S: Challenge vs booth review vs replay assist decision chart",
    "C: Accepted penalties per game by officiating crew (load_officials)"],
   ["The 2018 catch-rule rewrite after the Dez Bryant (Jan 2015 playoffs) and Jesse James (Dec 2017) rulings (verify both)",
    "2025 Hawk-Eye virtual first-down measurement", "2026 replay consult on ejections"],
   "Ref's mic: when a flag flies or a ruling is close, name the foul or ruling and the official before the announcement; "
   "on reviews, predict stands, confirmed, or overturned.",
   fwd=["10-04 (spikes and grounding in the two-minute drill)"],
   notes=["New chapter (audits M10 and S1). Pull wording from operations.nfl.com; FACTS-current §6 lists the 2023-2026 changes.",
          "The 2026 'sideline assistant may throw the challenge flag' item is UNVERIFIED: do not cite it."])

# ---------------------------------------------------------------- PART 10
part("10", "Situational Football", "3-4",
     "The same plays mean different things on 3rd & 8, at the 4-yard line, or with 1:12 left. This part teaches "
     "situations as the frame for everything before it.")

ch("10-01", "early-downs-and-field-zones", "Early Downs and Field Zones: How Situation Shapes the Call", 3, 12,
   ["Explain early-down philosophy (first-down pass rate, the 'establish the run' debate).",
    "Bucket second downs (and why 2nd & short is a shot down).",
    "Define field zones: backed up, coming out, open field, fringe (four-down territory), plus territory.",
    "Explain how play-calling changes by zone.",
    "Read pass rate and EPA by down, distance, and yard line."],
   ["early down", "backed up", "coming out", "open field", "four-down territory | fringe", "plus territory",
    "on schedule / behind schedule"],
   ["01-02", "08-02"],
   ["S: Field-zone map", "C: Pass-rate heatmap, down x distance", "C: EPA by yard line and down"],
   ["2018 Chiefs and Rams early-down passing", "Lions 2023-24", "Ravens 2019"],
   "Situation tag: before each snap tag the play with its situation bucket; compare your run/pass accuracy by bucket.")

ch("10-02", "third-down", "Third Down: The Money Down", 3, 13,
   ["Bucket third downs (short, medium, long) with league conversion rates.",
    "Explain offensive third-down concepts: sticks routes, man-beaters, long-yardage screens and draws (03-03).",
    "Explain defensive third-down packages: sticks defense, sim pressure, Cover 0, rush three/drop eight, spy.",
    "Explain why 'past the sticks' matters and when it doesn't."],
   ["sticks route", "third-down package", "rush three, drop eight", "spy | QB spy"],
   ["10-01", "07-03"],
   ["S: 3rd & 7 concept vs Cover 1", "S: Rush three / drop eight", "S: QB spy",
    "A: 3rd-and-long draw vs dime (frame strip)", "C: Conversion rate by distance and play type"],
   ["Patriots' option routes (Welker, Edelman)", "Spagnuolo third-down pressure", "Flores' third-down Cover 0"],
   "Past the sticks? Predict whether the target will be beyond the line to gain.")

ch("10-03", "red-zone-goal-line-and-short-yardage", "Red Zone, Goal Line, Two-Point Plays, and Short Yardage (Including the Tush Push)", 3, 15,
   ["Explain the compressed field: why deep zones vanish and man/press increases.",
    "Diagram red-zone concepts: fade, back-shoulder, rubs (04-04), slants, shovel, sprint-out.",
    "Design two-point plays from the 2: concepts and the best-percentage calls (whether to go for two is 10-04).",
    "Diagram goal-line personnel and fronts on both sides.",
    "Explain the QB sneak and tush push mechanics, the 2005 push-the-runner rule change, and the ban debate "
    "(2025 ban failed 22-10; no proposal in 2026; legal for the 2026 season).",
    "Analyse red-zone TD rates and sneak success with data."],
   ["compressed field", "fade", "back-shoulder throw", "shovel pass", "goal-line defense",
    "QB sneak", "tush push", "assisting the runner (push rule)"],
   ["10-02", "09-03", "03-04"],
   ["S: Red-zone field map with compressed zones", "A: Rub concept vs man near the goal line (frame strip)",
    "S: Two-point concepts from the 2", "A: Tush push: formation and push (frame strip)", "S: Goal-line 6-2 and 5-3 defenses",
    "C: QB-sneak/tush-push success rate by team, 2022-2025 (FTN is_qb_sneak)"],
   ["Eagles tush push (Hurts, Kelce, Johnson)", "Bills' Allen sneak", "Brady sneak"],
   "Fade or rub? Inside the 10, predict the pass concept from receiver splits.",
   notes=["Signature-diagram home for the tush push (animation and sneak-success chart); 12-06 shows only the Eagles-vs-league delta (audit S21).",
          "FTN has no tush-push flag: use is_qb_sneak, which covers both sneaks and pushes (FACTS-current §7)."])

ch("10-04", "clock-and-game-management", "The Clock, the Two-Minute Drill, and Fourth Down", 4, 16,
   ["Run a two-minute offense: sideline routes, spikes (legal, unlike grounding), timeouts, the 10-second runoff.",
    "Apply the out-of-bounds clock rule (the clock restarts on the ready signal except in the last 2:00 of the first half and the last 5:00 of the second).",
    "Run a four-minute offense: running inbounds, killing clock, the victory formation.",
    "Make end-of-half decisions (points vs risk, FG range, Hail Mary, prevent), including the rare-but-decisive "
    "intentional safety, free kick after a safety, and fair-catch kick.",
    "Use fourth-down and two-point heuristics; explain the 2018-2025 aggression shift (math in 13-03).",
    "Apply current overtime rules (playoffs since 2022; regular season since 2025: both teams possess, 10-minute period, ties possible) and their strategy."],
   ["two-minute drill", "spike", "10-second runoff", "out-of-bounds clock rule", "four-minute offense",
    "victory formation | kneel-down", "Hail Mary", "prevent defense", "intentional safety", "fair-catch kick",
    "go-for-it decision", "two-point chart", "overtime rules"],
   ["10-03", "09-01", "08-04", "09-04"],
   ["S: Annotated two-minute drive timeline", "S: Clock decision flowchart",
    "S: Sidebar plates: intentional safety and the fair-catch kick",
    "C: Fourth-down go rate by season 2010-2025", "C: Go rate by yards to go x field position"],
   ["Chiefs-Bills '13 seconds' (Jan 2022) and the playoff OT change", "Dan Campbell's Lions",
    "Super Bowl LVIII overtime (first Super Bowl under the 2022 playoff rule)", "Andy Reid clock-management critiques"],
   "Coach the clock: in the last two minutes of each half, predict timeouts, spikes, and kneels before they happen.",
   fwd=["13-03 (win probability and the fourth-down model)"])

# ---------------------------------------------------------------- PART 11
part("11", "History: The Arms Race", "2-3",
     "A chronological retelling of how we got here, told as action and reaction: each offensive innovation, the defensive "
     "answer, and the rule changes that tilted the board. Earlier chapters already contain history sidebars; this part "
     "connects them into one story. Disputed origins are presented as disputed (AUTHORING §6).")

ch("11-01", "single-wing-to-scoring-drought", "From the Single Wing to the 1970s Scoring Drought (1906-1977)", 2, 16,
   ["Trace the forward pass from legalisation (1906) to slow adoption.",
    "Explain the single wing -> T-formation shift (1940 Bears 73-0).",
    "Describe Paul Brown's innovations (playbooks, film study, messenger guards).",
    "Describe the 4-3's ancestry (Steve Owen's umbrella defense, then Landry's 4-3 and Flex), Lombardi's sweep, Gillman's vertical passing.",
    "Explain the AFL (1960-69) as a passing laboratory (Gillman, Stram) and the merger, alongside Red Hickey's 1960 49ers shotgun.",
    "Explain 1970s defensive dominance (the book's label: the 1970s scoring drought) and the rules (1972 hashes, 1974 changes) that failed to fix it."],
   ["single wing", "platoon football", "umbrella defense", "Flex defense", "AFL | American Football League", "chuck rule"],
   ["02-03", "06-04"],
   ["S: Single wing plate", "S: 1940 T-formation", "S: Owen's umbrella defense", "S: Lombardi power sweep", "S: Landry Flex",
    "C: Points per game 1932-1977", "S: Timeline graphic"],
   ["Halas, Shaughnessy & Luckman (1940 Bears)", "Paul Brown's Browns", "Steve Owen's Giants", "Lombardi Packers", "Landry Cowboys",
    "Gillman Chargers", "Hank Stram's Chiefs", "Red Hickey's 1960 49ers", "1970s Steelers", "1972 Dolphins"],
   "Spot the ancestor: find one modern play with single-wing or T-formation DNA (wildcat, direct snap, buck sweep).",
   notes=["'Dead-ball era' is baseball usage; the book says '1970s scoring drought' instead (audit N11)."])

ch("11-02", "the-1978-liberation", "1978 and the Passing Revolution (1978-1999)", 3, 16,
   ["Explain the 1978 rules (Mel Blount rule, pass-blocking hands) and their effect.",
    "Describe Air Coryell, the West Coast offense, Gibbs' one-back and counter trey, run-and-shoot, the K-Gun.",
    "Describe the defensive answers: nickel/dime, Arnsparger's '53' (1972 Dolphins) as a 3-4 root, the 46, Lawrence Taylor and the "
    "blind-side tackle, and the zone blitz (origin disputed: LeBeau vs Arnsparger's 1980s Dolphins).",
    "Explain free agency (1993) and the salary cap (1994).",
    "Explain the 1994 two-point conversion and kickoff changes."],
   ["Mel Blount rule (1978)", "53 defense", "blind-side tackle", "free agency (1993)", "salary cap"],
   ["11-01", "04-08", "07-03", "05-02"],
   ["C: League passing yards per attempt and points per game, 1970-1999 (season-level data)",
    "S: Why the left tackle matters: right-handed QB's blind side", "S: 46 vs one-back counter", "S: Timeline graphic"],
   ["Coryell Chargers", "Walsh 49ers", "Gibbs Washington", "Arnsparger's Dolphins ('53' in 1972, zone pressures in the 1980s)",
    "1985 Bears", "Parcells/Belichick Giants", "Run-and-shoot Oilers/Lions/Falcons", "Bills K-Gun", "Blitzburgh Steelers", "1998 Broncos"],
   "Classic film: watch a 1980s game on NFL Films/YouTube; identify the formations and coverages you now know.")

ch("11-03", "the-college-laboratory", "The College Laboratory: Wing-T, Wishbone, Air Raid, Spread Option, and the RPO", 3, 17,
   ["Explain why college innovates (talent gaps, wide hashes, ineligible-downfield leeway, tempo).",
    "Trace wishbone/veer/flexbone, Wing-T, BYU passing, Air Raid, spread option, pistol, RPO.",
    "Trace college defensive answers: 3-3-5, quarters, pattern match, tite fronts, three-safety looks.",
    "Explain when and how each crossed into the NFL.",
    "Compare college and NFL rules (the Appendix E table): hash width, one foot vs two in bounds, ineligible downfield (3 yards vs 1), "
    "DPI spot foul vs 15-yard cap, OPI, the college clock, overtime, targeting, kickoff fair catches and the fair-catch kick, motion, "
    "two-minute timeouts, helmet communication."],
   ["spread offense", "spread option", "3-3-5 stack", "three-high safety defense"],
   ["11-02", "03-04", "04-06", "06-05"],
   ["S: Wishbone triple option", "S: Rich Rodriguez zone read with bubble attached",
    "S: 3-3-5 stack", "S: College vs NFL rules table (rendered from Appendix E)",
    "C: NFL shotgun rate with college-import annotations"],
   ["Texas/Oklahoma wishbone", "Houston veer", "Delaware Wing-T", "BYU (LaVell Edwards)",
    "Kentucky/Texas Tech Air Raid (concepts drawn in 04-04)",
    "Rodriguez and Meyer spread option", "Oregon (Chip Kelly)", "Auburn (Malzahn, Cam Newton)", "Oklahoma (Riley: Mayfield, Murray)",
    "Saban's Alabama and Smart's Georgia defenses"],
   "Saturday vs Sunday: watch one college and one NFL game; list three structural differences.",
   notes=["The flexbone is now defined in 02-03; this chapter keeps the lineage (audit M6).",
          "College ineligible downfield is still 3 yards. A proposal to move it to 1 yard was tabled (the audit dates it 2025; "
          "FACTS-current C12 says 2015); confirm the year before printing.",
          "2026 college changes (OPI 10 yards, a fair-catch kick, two challenges per game, targeting second-half carryover removed) come from "
          "one secondary source; verify against the NCAA rulebook."])

ch("11-04", "dynasties-and-counterpunches", "Dynasties and Counterpunches (2000-2016)", 3, 15,
   ["Explain the Tampa 2 dynasty and its counters (seam TEs, Peyton Manning).",
    "Explain the Patriots' adaptability: EP system, 2007 spread, 2010s two-TE 12 personnel.",
    "Explain the 2004 illegal-contact emphasis and the passing boom that followed.",
    "Explain the 3-4 revival and the hybrid edge.",
    "Explain the 2012 read-option wave and why it receded; Seattle's Cover 3; Chip Kelly's 2013 Eagles.",
    "Describe the early analytics movement."],
   ["move tight end | joker", "hybrid edge", "read-option wave (2012)"],
   ["11-03"],
   ["S: Manning vs Tampa 2 seam", "S: Patriots 12 personnel dilemma: base vs nickel",
    "C: League EPA/dropback 1999-2016", "C: Designed QB run share, 2012 spike"],
   ["Manning Colts", "Patriots", "Steelers 2005/2008", "2007 Giants pass rush", "Brees/Payton Saints", "2013 Seahawks",
    "2015 Broncos defense", "Romer (2006) and Brian Burke's Advanced NFL Stats"],
   "Personnel dilemma: when a team uses 12 personnel with an athletic TE, does the defense stay nickel or go base?")

ch("11-05", "the-modern-era", "The Modern Era: McVay, Mahomes, Two-High, and the Under-Center Comeback (2017-2025)", 3, 17,
   ["Explain the McVay/Shanahan revival: 11 personnel, condensed sets, play-action, motion.",
    "Explain Mahomes/Reid off-script and college-concept passing.",
    "Explain the two-high counterrevolution and the offensive response (light-box runs, under center, heavier personnel).",
    "Explain why positions mutated: slot CB -> nickel as base, big nickel/star, hybrid LB/S, the move TE, the edge as the premium defender, the FB's niche revival.",
    "Explain the normalisation of the QB run game (Lamar, Hurts, Allen).",
    "Explain analytics-driven aggression.",
    "Summarise rule-era changes (helmet rule, dynamic kickoff, OT, hip-drop, tush push) and where the game stands entering 2026 "
    "(Seattle's Super Bowl LX title; the 2026 kickoff and replay changes)."],
   ["two-high counterrevolution", "under-center revival", "light-box run game"],
   ["11-04", "06-06"],
   ["C: Two-high rate (2018-2025; mark the 2022/2023 source break) vs 11-personnel rate vs under-center rate (2016-2025)",
    "S: Arms-race loop diagram (offensive move -> defensive answer -> ...)",
    "S: Position-evolution map (slot CB, star, hybrid LB/S, move TE, edge, FB)",
    "C: Fourth-down go rate by season", "S: Timeline graphic"],
   ["Rams 2017-18", "Chiefs 2018-24", "49ers", "Ravens 2019/2023", "Eagles 2022/2024", "Lions 2023-24", "Bills",
    "Seahawks 2025 (Super Bowl LX: Seahawks 29, Patriots 13; Kubiak's single season as OC)", "Fangio/Staley/Evero", "Macdonald"],
   "Arms-race spotting: in one game, identify one offensive trend and the defensive counter you see against it.",
   notes=["Trend numbers with sources (FACTS-current §10): NGS split-safety 32.9% (2018) -> 42.0% (2025); PFF shift/motion 63.9% (2025); "
          "NGS fewer-than-three-WR sets 41.7% (2025); nflverse 12 personnel 24.4% (2025). Two-high data starts in 2018 (audit C6)."])

# ---------------------------------------------------------------- PART 12
part("12", "Case Studies: Teams That Did It Best", "4-5",
     "Deep dives, each structured the same way: the problem the team faced, the scheme answer, the signature plays "
     "(diagrammed and animated), the data fingerprint, how opponents responded, and what survives today. "
     "Every staff and era is labelled with its seasons; 2026 staff moves are in FACTS-current §9.")

ch("12-01", "walsh-49ers-west-coast", "Case Study: Bill Walsh's 49ers and the West Coast Offense", 4, 14,
   ["Explain the WCO's short horizontal passing as a substitute run game.",
    "Explain timing, YAC, and ball placement as design goals.",
    "Explain scripting and Walsh's practice methods.",
    "Break down 'The Catch' (1981 NFC Championship).",
    "Trace the Walsh coaching tree to modern staffs (2025 and 2026 staffs labelled separately)."],
   ["horizontal passing game", "coaching tree"],
   ["11-02", "04-04"],
   ["A: 'Sprint Right Option' / The Catch recreated (frame strip)", "S: WCO drive and slant-flat from split backs",
    "S: Walsh coaching tree"],
   ["1981-1989 49ers (Montana, Rice, Craig)", "Holmgren Packers", "Andy Reid", "Jon Gruden", "the Shanahan link"],
   "WCO census: count short horizontal throws on early downs for a WCO-descended team.")

ch("12-02", "belichick-patriots-game-plan", "Case Study: Belichick and Game-Plan Football", 4, 15,
   ["Explain game-plan-specific defense and 'take away their best thing'.",
    "Break down the defensive plans in Super Bowls XXV (as Giants DC), XXXVI, and LIII.",
    "Explain the offense's chameleon identity (2007 spread, 2011 12 personnel, 2018 run heavy).",
    "Analyse situational mastery (end of half, fourth down, clock).",
    "Break down Super Bowl XLIX's final play."],
   ["game-plan defense"],
   ["11-04", "08-03"],
   ["S: Giants' Super Bowl XXV plan vs the K-Gun", "S: Patriots' plan vs the 2018 Rams (verify specifics on film)",
    "A: Super Bowl XLIX goal-line interception (frame strip)", "S: Gronkowski 12-personnel dilemma"],
   ["1990 Giants", "2001-2019 Patriots"],
   "Take-away test: before a game, guess the opponent's best thing; afterwards decide whether it was taken away.",
   notes=["Signature-diagram home for the Super Bowl XXV/XXXVI/LIII plans and the XLIX interception; 08-01 and 08-03 link here (audit S21)."])

ch("12-03", "shanahan-wide-zone-tree", "Case Study: The Shanahan Tree - Wide Zone, Boots, and the Illusion of Complexity", 4, 16,
   ["Trace wide zone from Alex Gibbs' Broncos to Kyle Shanahan's 49ers.",
    "Explain the 49ers' marriage of wide zone, FB, motion, and YAC passing.",
    "Explain why the system makes QBs efficient (and the debate it creates).",
    "Map the tree with seasons: 2025 (McVay, Matt LaFleur, McDaniel in Miami, Kubiak as Seattle OC, Mike LaFleur as Rams OC, Coen) "
    "vs 2026 (Kubiak Raiders HC, McDaniel Chargers OC, Mike LaFleur Cardinals HC, Brian Fleury Seattle OC).",
    "Show the data fingerprint (under-center rate, PA rate, YAC over expected)."],
   ["YAC over expected | YACOE"],
   ["11-05", "08-02"],
   ["S: Wide zone vs bear look", "A: Keeper/boot off wide zone (frame strip)",
    "S: Recent staff moves box: the tree in 2025 vs 2026",
    "C: 49ers EPA/play rank 2019-2025", "C: YAC over expected by team"],
   ["1990s Broncos", "2016 Falcons", "2017-2025 49ers", "McVay Rams", "McDaniel Dolphins (2022-2025)",
    "Kubiak's 2025 Seahawks (Super Bowl LX champions; one season before he became Raiders HC)"],
   "Same look? Track one team's formation+motion combinations and list the different plays run from each.",
   notes=["'One formation, four plays' lives in 08-02; link it, don't redraw (audit S21).",
          "Recent staff moves box (audit N16, FACTS-current C2): label every map with its season."])

ch("12-04", "reid-chiefs", "Case Study: Andy Reid and the Kansas City Chiefs", 4, 15,
   ["Explain Reid's blend of WCO roots, college spread/RPO, and trick plays.",
    "Explain how Mahomes' off-script ability changes defensive math.",
    "Contrast the Tyreek Hill era with the 2022+ Kelce/quick-game era.",
    "Explain Spagnuolo's pressure defense as the complement.",
    "Trace the offensive coordinators with seasons: Bieniemy (2018-2022), Matt Nagy (2023-2025, now Giants OC), Bieniemy again (2026).",
    "Review the Super Bowl appearances: won LIV, LVII, and LVIII; lost LV and LIX."],
   [],
   ["11-05", "07-02"],
   ["A: 'Jet Chip Wasp' 3rd & 15 in Super Bowl LIV (frame strip)", "S: Kelce option route vs man and vs zone",
    "S: Spagnuolo Cover 0 pressure", "C: Chiefs EPA/play 2018-2025"],
   ["2018-2025 Chiefs"],
   "Off-script counter: count plays that leave structure; note the result vs in-structure plays.",
   notes=["Signature-diagram home for 'Jet Chip Wasp'; 08-01 links here (audit S21)."])

ch("12-05", "ravens-lamar-run-game", "Case Study: The Ravens' Option Run Game with Lamar Jackson (2019-2025)", 4, 14,
   ["Explain Greg Roman's 2019 design: heavy personnel, pistol, option variants, QB power/counter.",
    "Explain why a QB runner changes defensive arithmetic in every run fit.",
    "Explain the Todd Monken changes (2023) and the Derrick Henry pairing (2024-2025).",
    "Analyse defensive answers and playoff struggles honestly with data.",
    "Treat 2019-2025 as a closed era: Harbaugh was fired in Jan 2026 (now Giants HC), Monken is Browns HC, and the 2026 staff is "
    "Jesse Minter (HC), Declan Doyle (OC), Anthony Weaver (DC)."],
   ["pistol option offense"],
   ["11-05", "03-04", "05-05"],
   ["S: Pistol inverted veer", "S: Ravens 2019 13-personnel plate", "A: QB counter (frame strip)",
    "C: Ravens rushing EPA vs league 2018-2025"],
   ["2019 Ravens", "2023-2025 Ravens (Monken OC)"],
   "Count the defenders: on Ravens runs, count box defenders vs blockers (with the QB as a runner).",
   notes=["FACTS-current C3: write as a closed era with a 2026 epilogue."])

ch("12-06", "eagles-trenches-and-tush-push", "Case Study: The Eagles - Trenches, RPOs, and the Tush Push", 4, 14,
   ["Explain the 2017 RPO offense and the Philly Special.",
    "Explain the Sirianni/Hurts run game and OL investment (Jeff Stoutland, who left after the 2025 season), "
    "and the coordinator churn (Sean Mannion in 2026 is the fifth new OC in five years).",
    "Analyse the tush push as a talent edge: the Eagles-vs-league success delta (mechanics are in 10-03).",
    "Explain the 2024 team: Saquon Barkley, Fangio's defense (still DC in 2026), and Super Bowl LIX's four-man pressure.",
    "Connect roster building to scheme."],
   ["Philly Special"],
   ["11-05", "10-03"],
   ["A: Philly Special (frame strip)", "S: 2024 outside zone / duo with Barkley",
    "S: Super Bowl LIX four-man pressure without blitzing",
    "C: Eagles QB-sneak success minus league average, 2022-2025 (the delta only; FTN is_qb_sneak)"],
   ["2017 Eagles", "2022 Eagles", "2024 Eagles"],
   "Trench check: on Eagles third-and-short, guess sneak/tush push vs other; note what the defense does.",
   notes=["The tush-push animation and league chart live in 10-03; don't redraw (audit S21).",
          "Super Bowl LIX: confirm the blitz count from a charting source before stating it."])

ch("12-07", "lions-ben-johnson-and-campbell", "Case Study: The Lions - Ben Johnson's Offense and Dan Campbell's Aggression", 4, 14,
   ["Explain the 2021 rebuild philosophy.",
    "Explain Ben Johnson's offense (2022-2024): under center, motion, jumbo with eligible linemen (reporting eligible, 02-02), trick plays.",
    "Analyse Campbell's fourth-down aggression with data.",
    "Explain the 2025 departures (Johnson to the Bears as HC, Glenn to the Jets as HC) and what followed: OC John Morton was fired after one season, "
    "Campbell took over play-calling midway through 2025, and Drew Petzing is the 2026 OC (third in three years); Kelvin Sheppard remains DC.",
    "Assess what transferred with Johnson to the Bears."],
   [],
   ["11-05", "10-04"],
   ["S: Jumbo eligible-tackle play", "A: Shift + motion sequence (frame strip)",
    "C: Lions fourth-down go rate and EPA vs league"],
   ["2022-2025 Lions", "2025 Bears (Johnson as HC and play-caller)"],
   "Trick detector: in a Lions or Bears game, flag every snap with an unusual alignment or eligible lineman.",
   notes=["FACTS-current C1. The term 'eligible tackle' moved to 02-02 (audit M5)."])

ch("12-08", "two-high-to-macdonald", "Case Study: Fangio's Two-High Revolution and Macdonald's Answer", 5, 16,
   ["Explain Fangio's principles: two-high, light box, four-man rush, tite front, match quarters/Cover 6.",
    "Trace the spread (Staley, Evero and others) and Fangio's 2024 Eagles (still Eagles DC in 2026).",
    "Explain Macdonald's multiplicity: disguise, sim pressure, and front variety (2023 Ravens, 2024-25 Seahawks).",
    "Break down Seattle's Super Bowl LX defense (Seahawks 29, Patriots 13; six sacks of Drake Maye).",
    "Compare philosophies with data (pressure rate, disguise rate, EPA allowed).",
    "Predict what offenses do next."],
   ["multiplicity (defensive)"],
   ["11-05", "06-06", "07-03"],
   ["S: Fangio tite + quarters vs 11 personnel", "A: Macdonald sim pressure from a two-high look (frame strip)",
    "S: Recent staff moves box (2025 vs 2026)",
    "C: Two-high rate vs pressure rate by team"],
   ["2018 Bears", "2020 Rams", "2024 Eagles", "2023 Ravens", "2024-2025 Seahawks"],
   "Disguise audit: chart pre-snap shell vs post-snap coverage for one defense; compute its lie rate.",
   notes=["The safety-rotation tracking figure lives in 13-05 (shown in 06-06); link it (audit S21).",
          "Recent staff moves box (audit N16): Seattle's 2026 OC is Brian Fleury after Kubiak left; Aden Durde remains DC (FACTS-current §9)."])

# ---------------------------------------------------------------- PART 13
part("13", "Analytics and Data", "3-5",
     "The reader's home turf. Earlier chapters show nflverse charts with code folded; this part shows the code and teaches the reader to "
     "build them, then goes further, ending with tracking data and the Big Data Bowl. 13-01 can be read early "
     "(right after Part 2) by readers who want to run code alongside the course.")

ch("13-01", "nflverse-in-python", "Working with nflverse Data in Python", 3, 14,
   ["Install and use nflreadpy (polars; nfl_data_py is archived) and convert to pandas where needed.",
    "Load play-by-play, schedules, rosters, participation, and FTN charting data.",
    "Understand the pbp row structure (play_type, down, ydstogo, yardline_100, epa, wp, ...).",
    "Filter to 'real' plays (rush/pass, no-play penalties, garbage time).",
    "Join participation data for personnel and formation, handling the 2022 -> 2023 NGS-to-FTN source break.",
    "Reproduce a chart from an earlier chapter end-to-end."],
   ["play-by-play | pbp", "nflverse", "nflreadpy", "participation data", "FTN charting data", "source break", "yardline_100",
    "garbage-time filter"],
   ["01-02", "02-01"],
   ["S: pbp schema diagram", "S: Data-availability timeline (pbp 1999+, participation 2016+, coverage labels 2018-2025, FTN 2022+)",
    "C: Reproduce 02-01's personnel usage chart",
    "S: Data flow: nflverse -> course diagram library"],
   ["League pass rate by down, reproduced"],
   "Sunday notebook: after each week, load the new pbp and score your prediction log against it.",
   notes=["FACTS-current §7: participation is NGS for 2016-2022 and FTN for 2023-2025; the current season arrives only after it ends (~Feb 2027 for 2026). "
          "offense_formation values shrink to SHOTGUN / UNDER CENTER / PISTOL from 2023; personnel strings change format; ngs_air_yards is NA from 2024 "
          "(use pbp air_yards). FTN charting is updated weekly in season."])

ch("13-02", "expected-points-and-success-rate", "Expected Points, EPA, and Success Rate: The Model, the Noise, and the Broadcast Metrics", 4, 17,
   ["Explain the expected-points model (down, distance, yard line) behind the 01-02 primer.",
    "Compute EPA per play and success rate from pbp; explain why EPA beats yards.",
    "Compare run and pass EPA honestly (selection effects).",
    "Use CPOE and RYOE for player evaluation.",
    "Handle stability, noise, sample size, opponent adjustment, and turnover randomness (fumble-recovery luck, interception variance).",
    "Place the broadcast metrics (passer rating, QBR, ANY/A, DVOA, PFF grades, ESPN win rates, explosive play rate) relative to EPA: "
    "what each measures, open vs proprietary, when to distrust it."],
   ["RYOE | rush yards over expected", "year-over-year stability", "opponent adjustment", "turnover luck (fumble-recovery rate)",
    "passer rating", "QBR | Total QBR", "ANY/A | adjusted net yards per attempt", "DVOA", "PFF grade",
    "run stop win rate | RSWR", "explosive play rate"],
   ["13-01"],
   ["C: EP curve by yard line for each down", "C: EPA distribution, run vs pass", "C: Team offense vs defense EPA scatter",
    "S: One play's EPA, worked by hand", "C: Fumble-recovery rate by team, year to year (a coin flip)",
    "S: Metric map: broadcast metrics placed by what they measure and open vs proprietary"],
   ["2024 and 2025 team rankings"],
   "EPA in your head: estimate EP before and after a play; check with the model.",
   notes=["Pilot chapter (code shown; validates the 01-02 EPA primer). The terms EP, EPA, and success rate are owned by 01-02 (audit M2); "
          "this chapter is the deep treatment and must not redefine them.",
          "Each broadcast metric also gets a card in Appendix G."])

ch("13-03", "win-probability-and-fourth-down", "Win Probability and Decision Analysis: Fourth Downs, Two-Pointers, Timeouts", 4, 15,
   ["Explain win-probability models and WPA; leverage.",
    "Build a fourth-down decision framework (conversion probability x WP outcomes vs punt/FG).",
    "Analyse two-point decisions (down 8, down 14).",
    "Critique model uncertainty and calibration.",
    "Measure coaches' changing behaviour."],
   ["win probability | WP", "WPA | win probability added", "leverage (game situation)", "fourth-down model (bot)",
    "break-even conversion rate"],
   ["13-02", "10-04"],
   ["C: WP chart for Super Bowl LI (28-3)", "C: Fourth-down recommendation heatmap", "S: Decision tree for one fourth down",
    "C: Team aggressiveness vs model recommendation"],
   ["Ben Baldwin's fourth-down model", "NYT 4th Down Bot", "Lions under Campbell"],
   "Be the bot: make every fourth-down call live; compare with the model afterwards.")

ch("13-04", "tendencies-proe-and-charting", "Tendencies: PROE, Personnel, Motion, and Coverage from Charting Data", 4, 15,
   ["Explain expected pass rate (xpass) and PROE; compute by team, season, and situation.",
    "Measure personnel, formation, motion, and play-action tendencies.",
    "Measure coverage tendencies where charting data exists (coverage labels 2018-2025 only; NGS -> FTN source break between 2022 and 2023).",
    "Build a one-page data scouting report.",
    "State the caveats of charting data (definitions such as FTN is_motion, coverage, errors, label changes across the source break)."],
   ["xpass | expected pass rate", "PROE | pass rate over expected", "neutral situation", "coverage charting"],
   ["13-02", "08-02"],
   ["C: Team PROE vs EPA scatter", "C: Team tendency dashboard (personnel x pass rate x PA x motion)",
    "C: Coverage mix by team (2025 labels; source caveat on the chart)", "S: Scouting-report template"],
   ["2024-2025 team tendencies"],
   "Opponent card: produce a one-page tendency card before a game and grade it live.",
   notes=["FACTS-current §7: man/zone shares jump across 2022 -> 2025 (coding artefact); COVER_9, COMBO and BLOWN exist only from 2023; "
          "current-season participation is unavailable until after the season. Motion: FTN is_motion = 'before or at the snap'."])

ch("13-05", "tracking-data-and-big-data-bowl", "Tracking Data and the Big Data Bowl", 5, 18,
   ["Understand NGS tracking (10 Hz; x, y, s, a, o, dir) and the coordinate system.",
    "Standardise play direction and align frames to the snap and the throw.",
    "Plot and animate tracking frames with the course's diagram library.",
    "Derive features: separation, pocket area, safety rotation (the book's safety-rotation figure is built here), motion detection.",
    "Sketch projects: man/zone classification, route classification, disguise measurement.",
    "Survey Big Data Bowl themes and winning approaches."],
   ["tracking data", "Next Gen Stats | NGS", "frame (tracking)", "orientation vs direction", "standardised play direction",
    "separation", "Big Data Bowl"],
   ["13-04", "06-06"],
   ["S: Tracking coordinate system", "T: One real play animated from BDB data with the course library (frame strip)",
    "T: Safety rotation around the snap, built step by step (the figure 06-06 shows and 12-08 links)",
    "T: Separation over time for each receiver", "T: Safety depth at the snap, team distribution"],
   ["Big Data Bowl themes 2019-2026 (2025: pre-snap behaviour; 2026: player movement while the ball is in the air; "
    "2027 not announced as of Oct 2026, so check before printing)"],
   "First tracking chart: choose a play you watched live and plot it with the library.",
   notes=["FACTS-current §8: BDB 2025 columns are camelCase (2022 season, Weeks 1-9); BDB 2026 columns are snake_case "
          "(released files are 2023 Weeks 1-18 despite press text). Field is x 0-120, y 0-53.3 in both."])

# ---------------------------------------------------------------- PART 14
part("14", "The Business of Scheme: Roster, Cap, Draft, and Fantasy", "3",
     "How X's and O's turn into money and fantasy points: first how a roster is built and paid for, then how scheme "
     "shows up in fantasy usage.")

ch("14-01", "building-a-roster", "Building a Roster: Positional Value, the Cap, Free Agency, and the Draft", 3, 17,
   ["Explain positional value with data (QB, edge, LT, WR, CB vs RB, LB, S).",
    "Explain cap mechanics: cap hit, signing-bonus proration, guarantees, dead money, void years.",
    "Explain player acquisition: UFA/RFA, franchise and transition tags, compensatory picks, trades and the trade deadline, waivers.",
    "Explain the draft: rookie wage scale and fifth-year option, draft value charts (Jimmy Johnson chart vs surplus-value curves, Massey-Thaler), "
    "the combine and pro days.",
    "Explain player evaluation by position (QB processing, arm, accuracy; OL length, anchor, feet; edge bend and get-off; CB press/mirror and long speed) "
    "and RAS as a data proxy with limits.",
    "Explain scheme fit in the draft (wide-zone OL vs gap OL, two-gap nose vs 3-tech, press vs off corners).",
    "Explain roster rules: the 53, game-day actives, practice squad and elevations, IR, the emergency third QB."],
   ["cap hit", "signing-bonus proration", "guaranteed money", "dead money", "void years", "franchise tag", "transition tag",
    "unrestricted free agent | UFA", "restricted free agent | RFA", "compensatory pick", "trade deadline", "waivers",
    "rookie wage scale", "rookie-contract window", "fifth-year option", "draft value chart", "surplus value",
    "NFL Scouting Combine | combine", "pro day", "RAS | Relative Athletic Score", "positional value", "scheme fit",
    "practice squad elevation", "injured reserve | IR", "emergency third quarterback"],
   ["13-02", "08-03"],
   ["C: Positional cap share vs wins", "C: Draft pick value curve: Jimmy Johnson chart vs surplus value",
    "S: Evaluation card: what scouts grade at each position",
    "S: Scheme-fit archetype chart (body type by scheme and position)"],
   ["2021 Rams trade-heavy build", "Eagles OL investment", "49ers' mid-round wide-zone linemen",
    "Brock Purdy's 2022-24 surplus-value window (he signed a five-year extension in May 2025)",
    "Massey & Thaler, 'The Loser's Curse'"],
   "Cap check: for one team, find its biggest cap hits and dead money; predict which contract it restructures or cuts next.",
   fwd=["14-02 (fantasy)"],
   notes=["Split from the old 14-01 (audit S2). Roster facts (48 actives, emergency third QB) are in FACTS-current §6."])

ch("14-02", "scheme-and-fantasy", "Scheme and Fantasy: Reading Usage, Not Box Scores", 3, 12,
   ["Translate scheme into receiver usage: route participation, target share, air-yards share and WOPR, YPRR.",
    "Read RB usage (snap share, red-zone share, routes) and the TE's role in 12 personnel.",
    "Use PROE, pace, and game script to forecast volume.",
    "Explain scoring formats (PPR, half-PPR, standard) and ADP as a market price.",
    "Predict how a coordinator change shifts fantasy value."],
   ["route participation", "target share", "air-yards share", "WOPR | weighted opportunity rating", "YPRR | yards per route run",
    "snap share", "red-zone share", "game script", "pace (plays per game)", "PPR | point per reception", "ADP | average draft position"],
   ["14-01", "13-04"],
   ["C: Target share vs team PROE", "C: Route participation vs YPRR (2025)", "S: Coordinator-change before/after usage card"],
   ["Saquon Barkley in 2024",
    "2026 coordinator changes as test cases: Lions (Drew Petzing, the third OC in three years), Mike McDaniel as Chargers OC, Eric Bieniemy back as Chiefs OC"],
   "Scheme-shift draft: for one team with a new coordinator, predict which fantasy assets rise and fall.")

# ---------------------------------------------------------------- PART 15
part("15", "Capstone: Watching Like a Coach", "5",
     "Integrates every per-chapter drill into one live protocol, then into film study, and scores the reader's prediction log "
     "from the 01-02 baseline and the formal log begun in 01-06.")

ch("15-01", "watching-live", "Watching Live: The Master Checklist and Anticipation", 5, 13,
   ["Run the master pre-snap checklist in ~20 seconds: situation -> personnel -> formation/strength -> motion response -> box -> shell -> "
    "leverage -> pressure tells -> prediction.",
    "Use the full tells catalogue: stance (heavy vs light hand, OL weight back on a pass set), RB depth/offset, pistol vs gun, receiver splits "
    "(a reduced split suggests a crack or an inside-breaking route), TE stance, LB depth, DB depth and leverage, safety width.",
    "Break down a complete annotated drive.",
    "Make in-game predictions with a stated confidence, ready for scoring in 15-02."],
   ["master pre-snap checklist", "stated confidence"],
   ["08-04", "10-04", "13-04"],
   ["S: Master checklist one-page card (the Part 2/4/6/7 cards, completed)", "S: Tells catalogue plate",
    "A: Full drive (8-12 plays) annotated, frame strips"],
   ["A recent playoff drive chosen for variety (verify at writing time)"],
   "Live run: for one half, run the checklist on every snap and log a prediction with a confidence (50-90%).",
   fwd=["15-02 (scoring your predictions)"],
   notes=["Split from the old 15-01 (audit S3)."])

ch("15-02", "film-study-and-charting", "Film Study: All-22, Charting a Game, and Scoring Yourself", 5, 13,
   ["Get and watch All-22 with a four-pass film protocol (OL, QB, coverage, skill players).",
    "Chart a full game with a template.",
    "Score the season's prediction log with Brier score and calibration plots in Python.",
    "Know where to keep learning (coaching clinics, analytics community, BDB)."],
   ["film-study protocol", "game charting | charting", "Brier score", "calibration"],
   ["15-01", "13-04"],
   ["S: Four-pass film protocol card", "S: Charting sheet template", "C: Calibration plot of the reader's prediction log"],
   ["One full game charted end to end (choose a recent game; verify at writing time)"],
   "Chart a full game: every snap, all checklist fields, prediction, outcome; then score it.")
