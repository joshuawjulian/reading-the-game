# Curriculum data, Parts 7-15
from data1 import part, ch

# ---------------------------------------------------------------- PART 7
part("07", "Pressure: Rush, Blitz, and Simulated Pressure", "3-4",
     "How defenses attack the quarterback: winning one-on-one, adding rushers, and the modern art of making four "
     "rushers look like six.")

ch("07-01", "pass-rush", "The Pass Rush: Moves, Stunts, and Why Pressure Beats Sacks", 3, 12,
   ["Explain get-off, the rush arc, and the main moves (speed, bull, long arm, swim, rip, spin, counters).",
    "Diagram stunts/games: T-E, E-T, loop, twist.",
    "Explain rush lanes and contain vs mobile QBs.",
    "Explain why pressure is more stable than sacks and how QBs drive sack rate.",
    "Use pass-rush win rate and time-to-pressure metrics."],
   ["get-off", "speed rush", "bull rush", "long arm", "swim move", "rip move", "spin move", "stunt (game)",
    "T-E stunt", "E-T stunt", "rush lane", "pressure", "sack", "QB hit / hurry", "pass rush win rate (PRWR)"],
   ["04-02", "05-01"],
   ["S: Rush-move sequence frames (6 mini panels)", "A: T-E stunt vs slide protection (frame strip)",
    "S: Rush lanes vs a mobile QB", "C: Sack rate vs pressure rate, team-season scatter"],
   ["Lawrence Taylor", "Reggie White", "Aaron Donald", "T.J. Watt", "Myles Garrett", "Micah Parsons"],
   "Count the seconds: stopwatch from snap to first pressure; note whether the ball was already out.")

ch("07-02", "blitz-and-man-pressure", "Blitzing: Numbers, Overloads, A-Gap Mugs, and Cover 0", 3, 13,
   ["Define a blitz (5+ rushers) versus a four-man rush.",
    "Do blitz math: rushers vs protectors, who is free, where the hot throw goes.",
    "Diagram man pressures: Cover 1 blitz, Cover 0, overloads.",
    "Explain double A-gap mugs and why they break protection rules.",
    "Analyse blitz rate vs EPA allowed (high variance, situational value)."],
   ["blitz", "four-man rush", "five-man pressure", "overload blitz", "double A-gap mug", "Cover 0 blitz",
    "Cover 1 blitz", "unblocked rusher"],
   ["07-01", "06-02"],
   ["A: Overload blitz vs half-slide, RB picks wrong man (frame strip)",
    "S: Double A-gap mug: three post-snap variants from one look", "S: Cover 0 blitz vs empty -> hot throw",
    "C: Blitz rate vs EPA/dropback allowed by team"],
   ["Buddy Ryan", "Rex Ryan", "Steve Spagnuolo (2007 Giants, Chiefs Cover 0)", "Brian Flores (Dolphins, Vikings 2024)"],
   "Count the rushers: four or more? If more, predict a quick throw and to which side.")

ch("07-03", "zone-blitz-and-simulated-pressure", "Zone Blitzes, Fire Zones, and Simulated Pressure", 4, 14,
   ["Explain the zone-blitz idea: rush an unexpected defender, drop a lineman, play three-deep three-under.",
    "Diagram fire-zone variants and their hot-zone holes.",
    "Define simulated pressure (creeper): four rushers from unexpected places, seven in coverage.",
    "Explain how sim pressure wins one-on-ones by defeating protection rules without sacrificing coverage.",
    "Narrate the protection-vs-pressure chess: Mike ID, slide direction, hot throws."],
   ["zone blitz", "fire zone (3-under 3-deep)", "simulated pressure (creeper)", "dropper (DL in coverage)",
    "pressure look"],
   ["07-02", "06-03"],
   ["A: Fire zone vs 2x2: DE drops to the hook (frame strip)", "A: Creeper from nickel (frame strip)",
    "S: Protection bust: slide toward the threat, rush from the other side",
    "S: 1990s Steelers zone-blitz plate"],
   ["Dick LeBeau (Bengals origin, 'Blitzburgh' Steelers)", "Dom Capers", "Mike Macdonald Ravens/Seahawks",
    "Brian Flores 2024 Vikings", "Spagnuolo"],
   "Who dropped? After the snap find the lineman who dropped into coverage, and who replaced him as a rusher.",
   fwd=["12-08 (Macdonald)"])

# ---------------------------------------------------------------- PART 8
part("08", "The Chess Match", "4-5",
     "Offense and defense together: which concepts beat which coverages, how plays are sequenced to set each other up, "
     "how a week of game-planning works, and how adjustments and tempo play out on Sunday.")

ch("08-01", "concepts-versus-coverages", "What Beats What: Pass Concepts Versus Coverages", 4, 16,
   ["Build the concept x coverage matrix (smash vs Cover 2, four verts and flood vs Cover 3, dagger vs quarters, mesh vs man, ...).",
    "Explain why 'beaters' are probabilistic given match rules and disguise.",
    "Explain two-way concepts with a man answer and a zone answer built in.",
    "Show the defense's counters (Cover 3 match vs four verts, Palms vs smash).",
    "Practise identify-then-predict on animated plays."],
   ["coverage beater", "two-way concept", "alert (shot alert)"],
   ["06-06", "04-04", "06-02"],
   ["S: Concept x coverage matrix, colour-coded by expected advantage",
    "A: Smash vs Cover 2 (frame strip)", "A: Flood vs Cover 3 (frame strip)", "A: Dagger vs quarters (frame strip)",
    "A: Mesh vs Cover 1 (frame strip)", "A: Smash vs Palms: the defense wins (frame strip)"],
   ["Chiefs' 3rd-and-15 'Jet Chip Wasp' in Super Bowl LIV", "Malcolm Butler's Super Bowl XLIX interception vs a stack/pick"],
   "Predict the open man: once you ID the coverage at the snap, name who will be open before the throw.")

ch("08-02", "constraint-theory-and-sequencing", "Constraint Theory: How Plays Talk to Each Other", 4, 13,
   ["Explain base plays vs constraint plays and the 'illusion of complexity'.",
    "Explain sequencing: setting up a counter, tendency breakers, play-action off the base run.",
    "Explain self-scouting and formation tells.",
    "Show the defense's version: one pressure look, several coverages.",
    "Find a team's tendencies by formation/personnel in data."],
   ["base play", "constraint play", "illusion of complexity", "sequencing", "tendency", "tendency breaker",
    "self-scout", "tell"],
   ["08-01", "03-05", "04-05"],
   ["S: Constraint tree: wide zone -> boot / naked / keeper / counter",
    "S: One formation, four plays (Shanahan-style plate)",
    "C: Tendency table: formation x personnel -> pass rate for one team"],
   ["Shanahan wide-zone family", "Wing-T series", "Reid's Chiefs", "Ben Johnson's Lions sequencing"],
   "Call the follow-up: after a big run from a look, predict play-action from the same look within the next few snaps.")

ch("08-03", "game-planning-week", "The Game Plan: A Week Inside an NFL Building", 4, 14,
   ["Walk through a game week: film, install, situational practice days.",
    "Explain call sheets organised by situation and the opening script.",
    "Explain matchup hunting and 'take away their best thing'.",
    "Explain how a staff scouts an opposing coordinator and QB.",
    "Describe tendency reports and the analytics staff's role."],
   ["game plan", "opening script", "situational call sheet", "matchup (mismatch)", "tendency report",
    "game-plan package"],
   ["08-02"],
   ["S: Annotated call-sheet mock-up", "S: Game-week calendar",
    "C: Matchup heatmap for a sample game (slot vs nickel, TE vs LB, etc.)",
    "S: 'Take away the best thing': normal alignment vs game-plan alignment"],
   ["Belichick: Giants vs Bills (Super Bowl XXV), Patriots vs Rams (Super Bowls XXXVI and LIII)", "Walsh's scripted 15",
    "Andy Reid's play sheet"],
   "Script detector: watch the first 15 offensive plays; list anything you haven't seen from this team before.",
   fwd=["12-02 (Belichick case study)"])

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
     "red-zone decisions depend on kicking ranges and on the contact/penalty rules.")

ch("09-01", "kicking-and-punting", "Field Goals, Extra Points, and the Punting Game", 2, 12,
   ["Explain FG/PAT mechanics: snap-hold-kick timing, protection, block units.",
    "Compute FG distance from the line of scrimmage and reason about range (kicker, weather, altitude).",
    "Explain the 2015 PAT change and its effect on two-point attempts.",
    "Diagram punt formations (shield/spread), gunners, vices; directional and coffin-corner punting; fair catch and downing.",
    "Explain fakes and why they are rare.",
    "Show FG accuracy by distance across eras."],
   ["field goal range", "snap-hold-kick", "shield (spread) punt", "vice (jammer)", "fair catch", "coffin-corner punt",
    "touchback", "net punting average", "fake punt / fake field goal"],
   ["01-02", "01-03"],
   ["S: FG formation and protection", "A: Shield punt and coverage lanes (frame strip)",
    "C: FG% by distance by era", "C: Punt landing spot heatmap"],
   ["Justin Tucker", "Brandon Aubrey's long-range kicking", "Notable fake punts"],
   "Range finder: on every 4th down, predict go / punt / FG before the offense lines up.")

ch("09-02", "kickoffs-and-returns", "Kickoffs, Returns, and the Dynamic Kickoff", 2, 11,
   ["Explain the traditional kickoff and why the league kept changing it (injury data).",
    "Explain the 2024 dynamic kickoff (setup zone, landing zone) and the 2025 adjustments.",
    "Explain the strategic consequences: return rates, squibs, landing-zone choices, touchback math.",
    "Explain onside kicks under current rules.",
    "Describe return schemes at a high level."],
   ["kickoff", "dynamic kickoff", "landing zone", "setup zone", "onside kick", "squib kick", "kick coverage unit",
    "return unit"],
   ["09-01", "07-02"],
   ["S: Dynamic kickoff alignment plate", "A: Dynamic kickoff from kick to tackle (frame strip)",
    "S: Old vs new kickoff side by side", "C: Return rate and average starting field position by season, 2019-2025"],
   ["League-wide 2024 vs 2025 return behaviour", "Teams that exploited landing-zone rules"],
   "Field-position ledger: log each kickoff's starting yard line; compute the game average.")

ch("09-03", "rules-that-shape-strategy", "The Rulebook as Strategy: Contact Rules, Penalties, and Officiating", 3, 15,
   ["Explain the 5-yard contact zone, defensive holding, illegal contact, DPI and OPI, and their scheme consequences (spot foul, throwing deep for DPI).",
    "Explain offensive holding, chop/cut-block legality, and ineligible-downfield enforcement.",
    "Explain QB protection rules (roughing, sliding) and their effect on QB run games.",
    "Explain free plays, challenges, and replay review.",
    "Show penalty rates by type and crew, and how penalties enter EPA.",
    "Summarise live rule debates (tush push, hip-drop tackle)."],
   ["illegal contact", "defensive holding", "offensive holding", "defensive pass interference (DPI)",
    "offensive pass interference (OPI)", "spot foul", "roughing the passer", "unnecessary roughness",
    "free play", "coach's challenge", "replay review", "accept / decline (penalty)", "half the distance"],
   ["06-01", "04-06", "04-02"],
   ["S: The 5-yard contact zone", "S: Pick-play legality within 1 yard",
    "S: DPI enforcement: NFL spot foul vs college 15-yard cap", "C: Penalty rates by type 2015-2025",
    "C: Accepted penalties per game by officiating crew"],
   ["2003 AFC Championship and the 2004 illegal-contact emphasis", "2018 NFC Championship no-call -> 2019 PI review experiment",
    "2024 hip-drop tackle ban", "2025 tush-push vote"],
   "Flag predictor: when a flag flies, guess the foul before the announcement and how it changes the series.",
   fwd=["11-02 / 11-04 (rule changes in historical context)", "Appendix E (rule-change timeline)"])

# ---------------------------------------------------------------- PART 10
part("10", "Situational Football", "3-4",
     "The same plays mean different things on 3rd & 8, at the 4-yard line, or with 1:12 left. This part teaches "
     "situations as the frame for everything before it.")

ch("10-01", "down-distance-and-field-zones", "Down, Distance, and Field Zones", 3, 12,
   ["Explain early-down philosophy (first-down pass rate, the 'establish the run' debate).",
    "Bucket second downs (and why 2nd & short is a shot down).",
    "Define field zones: backed up, coming out, open field, fringe (four-down territory), plus territory.",
    "Explain how play-calling changes by zone.",
    "Read pass rate and EPA by down, distance, and yard line."],
   ["early down", "backed up", "coming out", "open field", "four-down territory (fringe)", "plus territory",
    "on schedule / behind schedule"],
   ["01-02", "08-02"],
   ["S: Field-zone map", "C: Pass-rate heatmap, down x distance", "C: EPA by yard line and down"],
   ["2018 Chiefs and Rams early-down passing", "Lions 2023-24", "Ravens 2019"],
   "Situation tag: before each snap tag the play with its situation bucket; compare your run/pass accuracy by bucket.")

ch("10-02", "third-down", "Third Down: The Money Down", 3, 13,
   ["Bucket third downs (short, medium, long) with league conversion rates.",
    "Explain offensive third-down concepts: sticks routes, man-beaters, long-yardage screens and draws.",
    "Explain defensive third-down packages: sticks defense, sim pressure, Cover 0, rush three/drop eight, spy.",
    "Explain why 'past the sticks' matters and when it doesn't."],
   ["sticks route", "third-down package", "rush three, drop eight", "spy (QB spy)", "draw play"],
   ["10-01", "07-03"],
   ["S: 3rd & 7 concept vs Cover 1", "S: Rush three / drop eight", "S: QB spy",
    "A: 3rd-and-long draw vs dime (frame strip)", "C: Conversion rate by distance and play type"],
   ["Patriots' option routes (Welker, Edelman)", "Spagnuolo third-down pressure", "Flores' third-down Cover 0"],
   "Past the sticks? Predict whether the target will be beyond the line to gain.")

ch("10-03", "red-zone-goal-line-and-short-yardage", "Red Zone, Goal Line, and Short Yardage (Including the Tush Push)", 3, 14,
   ["Explain the compressed field: why deep zones vanish and man/press increases.",
    "Diagram red-zone concepts: fade, back-shoulder, rub/pick, slants, shovel, sprint-out.",
    "Diagram goal-line personnel and fronts on both sides.",
    "Explain the QB sneak and tush push mechanics, the 2005 push-the-runner rule change, and the ban debate.",
    "Analyse red-zone TD rates and sneak success with data."],
   ["compressed field", "fade", "back-shoulder throw", "rub (pick) route", "shovel pass", "goal-line defense",
    "QB sneak", "tush push", "assisting the runner (push rule)"],
   ["10-02", "09-03", "03-04"],
   ["S: Red-zone field map with compressed zones", "A: Rub concept vs man near the goal line (frame strip)",
    "A: Tush push: formation and push (frame strip)", "S: Goal-line 6-2 and 5-3 defenses",
    "C: QB-sneak/tush-push success rate by team, 2021-2025"],
   ["Eagles tush push (Hurts, Kelce, Johnson)", "Bills' Allen sneak", "Brady sneak"],
   "Fade or rub? Inside the 10, predict the pass concept from receiver splits.")

ch("10-04", "clock-and-game-management", "The Clock, the Two-Minute Drill, and Fourth Down", 4, 15,
   ["Run a two-minute offense: sideline routes, spikes, timeouts, the 10-second runoff.",
    "Run a four-minute offense: running inbounds, killing clock, the victory formation.",
    "Make end-of-half decisions (points vs risk, FG range, Hail Mary, prevent).",
    "Use fourth-down and two-point heuristics; explain the 2018-2025 aggression shift (math in 13-03).",
    "Apply current overtime rules (playoff 2022 and regular season 2025) and their strategy."],
   ["two-minute drill", "spike", "10-second runoff", "four-minute offense", "victory formation (kneel-down)",
    "Hail Mary", "prevent defense", "go-for-it decision", "two-point chart", "overtime rules"],
   ["10-03", "09-01", "08-04"],
   ["S: Annotated two-minute drive timeline", "S: Clock decision flowchart",
    "C: Fourth-down go rate by season 2010-2025", "C: Go rate by yards to go x field position"],
   ["Chiefs-Bills '13 seconds' (Jan 2022) and the playoff OT change", "Dan Campbell's Lions",
    "Super Bowl LVIII overtime", "Andy Reid clock-management critiques"],
   "Coach the clock: in the last two minutes of each half, predict timeouts, spikes, and kneels before they happen.",
   fwd=["13-03 (win probability and the fourth-down model)"])

# ---------------------------------------------------------------- PART 11
part("11", "History: The Arms Race", "2-3",
     "A chronological retelling of how we got here, told as action and reaction: each offensive innovation, the defensive "
     "answer, and the rule changes that tilted the board. Earlier chapters already contain history sidebars; this part "
     "connects them into one story.")

ch("11-01", "single-wing-to-dead-ball-era", "From the Single Wing to the Dead-Ball Era (1906-1977)", 2, 15,
   ["Trace the forward pass from legalisation (1906) to slow adoption.",
    "Explain the single wing -> T-formation shift (1940 Bears 73-0).",
    "Describe Paul Brown's innovations (playbooks, film study, messenger guards).",
    "Describe Landry's 4-3 and Flex, Lombardi's sweep, Gillman's vertical passing.",
    "Explain 1970s defensive dominance and the rules (1972 hashes, 1974 changes) that failed to fix it."],
   ["single wing", "platoon football", "Flex defense", "dead-ball era", "chuck rule"],
   ["02-03", "06-04"],
   ["S: Single wing plate", "S: 1940 T-formation", "S: Lombardi power sweep", "S: Landry Flex",
    "C: Points per game 1932-1977", "S: Timeline graphic"],
   ["Halas, Shaughnessy & Luckman (1940 Bears)", "Paul Brown's Browns", "Lombardi Packers", "Landry Cowboys",
    "Gillman Chargers", "1970s Steelers", "1972 Dolphins"],
   "Spot the ancestor: find one modern play with single-wing or T-formation DNA (wildcat, direct snap, buck sweep).")

ch("11-02", "the-1978-liberation", "1978 and the Passing Revolution (1978-1999)", 3, 16,
   ["Explain the 1978 rules (Mel Blount rule, pass-blocking hands) and their effect.",
    "Describe Air Coryell, the West Coast offense, Gibbs' one-back and counter trey, run-and-shoot, the K-Gun.",
    "Describe the defensive answers: nickel/dime, the 46, Lawrence Taylor and the blind-side tackle, the zone blitz.",
    "Explain free agency (1993) and the salary cap (1994).",
    "Explain the 1994 two-point conversion and kickoff changes."],
   ["Mel Blount rule (1978)", "blind-side tackle", "free agency (1993)", "salary cap"],
   ["11-01", "04-08", "07-03", "05-02"],
   ["C: League passing yards per attempt and points per game, 1970-1999 (season-level data)",
    "S: Why the left tackle matters: right-handed QB's blind side", "S: 46 vs one-back counter", "S: Timeline graphic"],
   ["Coryell Chargers", "Walsh 49ers", "Gibbs Washington", "1985 Bears", "Parcells/Belichick Giants",
    "Run-and-shoot Oilers/Lions/Falcons", "Bills K-Gun", "Blitzburgh Steelers", "1998 Broncos"],
   "Classic film: watch a 1980s game on NFL Films/YouTube; identify the formations and coverages you now know.")

ch("11-03", "the-college-laboratory", "The College Laboratory: Wing-T, Wishbone, Air Raid, Spread Option, and the RPO", 3, 16,
   ["Explain why college innovates (talent gaps, wide hashes, ineligible-downfield leeway, tempo).",
    "Trace wishbone/veer/flexbone, Wing-T, BYU passing, Air Raid, spread option, pistol, RPO.",
    "Trace college defensive answers: 3-3-5, quarters, pattern match, tite fronts, three-safety looks.",
    "Explain when and how each crossed into the NFL."],
   ["flexbone", "spread offense", "spread option", "3-3-5 stack", "three-high safety defense"],
   ["11-02", "03-04", "04-06", "06-05"],
   ["S: Wishbone triple option", "S: Air Raid four verts", "S: Rich Rodriguez zone read with bubble attached",
    "S: 3-3-5 stack", "C: NFL shotgun rate with college-import annotations"],
   ["Texas/Oklahoma wishbone", "Houston veer", "Delaware Wing-T", "BYU (LaVell Edwards)", "Kentucky/Texas Tech Air Raid",
    "Rodriguez and Meyer spread option", "Oregon (Chip Kelly)", "Auburn (Malzahn, Cam Newton)", "Oklahoma (Riley: Mayfield, Murray)",
    "Saban's Alabama and Smart's Georgia defenses"],
   "Saturday vs Sunday: watch one college and one NFL game; list three structural differences.")

ch("11-04", "dynasties-and-counterpunches", "Dynasties and Counterpunches (2000-2016)", 3, 15,
   ["Explain the Tampa 2 dynasty and its counters (seam TEs, Peyton Manning).",
    "Explain the Patriots' adaptability: EP system, 2007 spread, 2010s two-TE 12 personnel.",
    "Explain the 2004 illegal-contact emphasis and the passing boom that followed.",
    "Explain the 3-4 revival and the hybrid edge.",
    "Explain the 2012 read-option wave and why it receded; Seattle's Cover 3; Chip Kelly's 2013 Eagles.",
    "Describe the early analytics movement."],
   ["move tight end (joker)", "hybrid edge", "read-option wave (2012)"],
   ["11-03"],
   ["S: Manning vs Tampa 2 seam", "S: Patriots 12 personnel dilemma: base vs nickel",
    "C: League EPA/dropback 1999-2016", "C: Designed QB run share, 2012 spike"],
   ["Manning Colts", "Patriots", "Steelers 2005/2008", "2007 Giants pass rush", "Brees/Payton Saints", "2013 Seahawks",
    "2015 Broncos defense", "Romer (2006) and Brian Burke's Advanced NFL Stats"],
   "Personnel dilemma: when a team uses 12 personnel with an athletic TE, does the defense stay nickel or go base?")

ch("11-05", "the-modern-era", "The Modern Era: McVay, Mahomes, Two-High, and the Under-Center Comeback (2017-2025)", 3, 16,
   ["Explain the McVay/Shanahan revival: 11 personnel, condensed sets, play-action, motion.",
    "Explain Mahomes/Reid off-script and college-concept passing.",
    "Explain the two-high counterrevolution and the offensive response (light-box runs, under center, heavier personnel).",
    "Explain the normalisation of the QB run game (Lamar, Hurts, Allen).",
    "Explain analytics-driven aggression.",
    "Summarise rule-era changes (helmet rule, dynamic kickoff, OT, hip-drop, tush push) and where the game stands entering 2026."],
   ["two-high counterrevolution", "under-center revival", "light-box run game"],
   ["11-04", "06-06"],
   ["C: Two-high rate vs 11-personnel rate vs under-center rate, 2016-2025",
    "S: Arms-race loop diagram (offensive move -> defensive answer -> ...)",
    "C: Fourth-down go rate by season", "S: Timeline graphic"],
   ["Rams 2017-18", "Chiefs 2018-24", "49ers", "Ravens 2019/2023", "Eagles 2022/2024", "Lions 2023-24", "Bills",
    "Seahawks 2025", "Fangio/Staley/Evero", "Macdonald"],
   "Arms-race spotting: in one game, identify one offensive trend and the defensive counter you see against it.")

# ---------------------------------------------------------------- PART 12
part("12", "Case Studies: Teams That Did It Best", "4-5",
     "Deep dives, each structured the same way: the problem the team faced, the scheme answer, the signature plays "
     "(diagrammed and animated), the data fingerprint, how opponents responded, and what survives today.")

ch("12-01", "walsh-49ers-west-coast", "Case Study: Bill Walsh's 49ers and the West Coast Offense", 4, 14,
   ["Explain the WCO's short horizontal passing as a substitute run game.",
    "Explain timing, YAC, and ball placement as design goals.",
    "Explain scripting and Walsh's practice methods.",
    "Break down 'The Catch' (1981 NFC Championship).",
    "Trace the Walsh tree to modern staffs."],
   ["horizontal passing game"],
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
   "Take-away test: before a game, guess the opponent's best thing; afterwards decide whether it was taken away.")

ch("12-03", "shanahan-wide-zone-tree", "Case Study: The Shanahan Tree - Wide Zone, Boots, and the Illusion of Complexity", 4, 16,
   ["Trace wide zone from Alex Gibbs' Broncos to Kyle Shanahan's 49ers.",
    "Explain the 49ers' marriage of wide zone, FB, motion, and YAC passing.",
    "Explain why the system makes QBs efficient (and the debate it creates).",
    "Map the tree: McVay, LaFleur, McDaniel, Kubiak, Coen and others.",
    "Show the data fingerprint (under-center rate, PA rate, YAC over expected)."],
   ["YAC over expected (YACOE)"],
   ["11-05", "08-02"],
   ["S: Wide zone vs bear look", "A: Keeper/boot off wide zone (frame strip)", "S: One look, four plays",
    "C: 49ers EPA/play rank 2019-2025", "C: YAC over expected by team"],
   ["1990s Broncos", "2016 Falcons", "2017-2025 49ers", "McVay Rams", "McDaniel Dolphins", "Kubiak 2025 Seahawks"],
   "Same look? Track one team's formation+motion combinations and list the different plays run from each.")

ch("12-04", "reid-chiefs", "Case Study: Andy Reid and the Kansas City Chiefs", 4, 15,
   ["Explain Reid's blend of WCO roots, college spread/RPO, and trick plays.",
    "Explain how Mahomes' off-script ability changes defensive math.",
    "Contrast the Tyreek Hill era with the 2022+ Kelce/quick-game era.",
    "Explain Spagnuolo's pressure defense as the complement.",
    "Review the Super Bowl run (LIV, LV, LVII, LVIII, LIX)."],
   [],
   ["11-05", "07-02"],
   ["A: 'Jet Chip Wasp' 3rd & 15 in Super Bowl LIV (frame strip)", "S: Kelce option route vs man and vs zone",
    "S: Spagnuolo Cover 0 pressure", "C: Chiefs EPA/play 2018-2025"],
   ["2018-2025 Chiefs"],
   "Off-script counter: count plays that leave structure; note the result vs in-structure plays.")

ch("12-05", "ravens-lamar-run-game", "Case Study: The Ravens' Option Run Game with Lamar Jackson", 4, 14,
   ["Explain Greg Roman's 2019 design: heavy personnel, pistol, option variants, QB power/counter.",
    "Explain why a QB runner changes defensive arithmetic in every run fit.",
    "Explain the Todd Monken changes (2023) and the Derrick Henry pairing (2024).",
    "Analyse defensive answers and playoff struggles honestly with data."],
   ["pistol option offense"],
   ["11-05", "03-04", "05-05"],
   ["S: Pistol inverted veer", "S: Ravens 2019 13-personnel plate", "A: QB counter (frame strip)",
    "C: Ravens rushing EPA vs league 2018-2025"],
   ["2019 Ravens", "2023-2024 Ravens"],
   "Count the defenders: on Ravens runs, count box defenders vs blockers (with the QB as a runner).")

ch("12-06", "eagles-trenches-and-tush-push", "Case Study: The Eagles - Trenches, RPOs, and the Tush Push", 4, 14,
   ["Explain the 2017 RPO offense and the Philly Special.",
    "Explain the Sirianni/Hurts run game and OL investment (Jeff Stoutland).",
    "Analyse the tush push as a scheme and as a talent edge.",
    "Explain the 2024 team: Saquon Barkley and Fangio's defense, and Super Bowl LIX's four-man pressure.",
    "Connect roster building to scheme."],
   ["Philly Special"],
   ["11-05", "10-03"],
   ["A: Philly Special (frame strip)", "S: Tush push, revisited from 10-03", "S: 2024 outside zone / duo with Barkley",
    "S: Super Bowl LIX four-man pressure without blitzing", "C: Eagles QB sneak conversion rate vs league"],
   ["2017 Eagles", "2022 Eagles", "2024 Eagles"],
   "Trench check: on Eagles third-and-short, guess sneak/tush push vs other; note what the defense does.")

ch("12-07", "lions-ben-johnson-and-campbell", "Case Study: The Lions - Ben Johnson's Offense and Dan Campbell's Aggression", 4, 14,
   ["Explain the 2021 rebuild philosophy.",
    "Explain Ben Johnson's offense (2022-2024): under center, motion, jumbo with eligible linemen, trick plays.",
    "Analyse Campbell's fourth-down aggression with data.",
    "Explain the 2024 team and the 2025 coordinator departures (Johnson to Chicago, Glenn to the Jets).",
    "Assess what transferred with Johnson to the Bears."],
   ["eligible tackle (tackle-eligible)"],
   ["11-05", "10-04"],
   ["S: Jumbo eligible-tackle play", "A: Shift + motion sequence (frame strip)",
    "C: Lions fourth-down go rate and EPA vs league"],
   ["2022-2025 Lions", "2025 Bears"],
   "Trick detector: in a Lions or Bears game, flag every snap with an unusual alignment or eligible lineman.")

ch("12-08", "two-high-to-macdonald", "Case Study: Fangio's Two-High Revolution and Macdonald's Answer", 5, 16,
   ["Explain Fangio's principles: two-high, light box, four-man rush, tite front, match quarters/Cover 6.",
    "Trace the spread (Staley, Evero and others) and Fangio's 2024 Eagles.",
    "Explain Macdonald's multiplicity: disguise, sim pressure, and front variety (2023 Ravens, 2024-25 Seahawks).",
    "Compare philosophies with data (pressure rate, disguise rate, EPA allowed).",
    "Predict what offenses do next."],
   ["multiplicity (defensive)"],
   ["11-05", "06-06", "07-03"],
   ["S: Fangio tite + quarters vs 11 personnel", "A: Macdonald sim pressure from a two-high look (frame strip)",
    "T: Safety rotation measured from tracking", "C: Two-high rate vs pressure rate by team"],
   ["2018 Bears", "2020 Rams", "2024 Eagles", "2023 Ravens", "2024-2025 Seahawks"],
   "Disguise audit: chart pre-snap shell vs post-snap coverage for one defense; compute its lie rate.")

# ---------------------------------------------------------------- PART 13
part("13", "Analytics and Data", "3-5",
     "The reader's home turf. Earlier chapters show nflverse charts with code folded; this part teaches the reader to "
     "build them and then goes further, ending with tracking data and the Big Data Bowl. 13-01 can be read early "
     "(right after Part 2) by readers who want to run code alongside the course.")

ch("13-01", "nflverse-in-python", "Working with nflverse Data in Python", 3, 14,
   ["Install and use nflreadpy (polars) and convert to pandas where needed.",
    "Load play-by-play, schedules, rosters, participation, and FTN charting data.",
    "Understand the pbp row structure (play_type, down, ydstogo, yardline_100, epa, wp, ...).",
    "Filter to 'real' plays (rush/pass, no-play penalties, garbage time).",
    "Join participation data for personnel and formation.",
    "Reproduce a chart from an earlier chapter end-to-end."],
   ["play-by-play (pbp)", "nflverse", "nflreadpy", "participation data", "FTN charting data", "yardline_100",
    "garbage-time filter"],
   ["01-02", "02-01"],
   ["S: pbp schema diagram", "C: Reproduce 02-01's personnel usage chart",
    "S: Data flow: nflverse -> course diagram library"],
   ["League pass rate by down, reproduced"],
   "Sunday notebook: after each week, load the new pbp and score your prediction log against it.")

ch("13-02", "expected-points-and-success-rate", "Expected Points, EPA, and Success Rate", 4, 16,
   ["Explain the expected-points model (down, distance, yard line).",
    "Compute EPA per play and success rate; explain why EPA beats yards.",
    "Compare run and pass EPA honestly (selection effects).",
    "Use CPOE and RYOE for player evaluation.",
    "Handle stability, noise, sample size, and opponent adjustment."],
   ["expected points (EP)", "EPA (expected points added)", "success rate", "RYOE (rush yards over expected)",
    "year-over-year stability", "opponent adjustment"],
   ["13-01"],
   ["C: EP curve by yard line for each down", "C: EPA distribution, run vs pass", "C: Team offense vs defense EPA scatter",
    "S: One play's EPA, worked by hand"],
   ["2024 and 2025 team rankings"],
   "EPA in your head: estimate EP before and after a play; check with the model.")

ch("13-03", "win-probability-and-fourth-down", "Win Probability and Decision Analysis: Fourth Downs, Two-Pointers, Timeouts", 4, 15,
   ["Explain win-probability models and WPA; leverage.",
    "Build a fourth-down decision framework (conversion probability x WP outcomes vs punt/FG).",
    "Analyse two-point decisions (down 8, down 14).",
    "Critique model uncertainty and calibration.",
    "Measure coaches' changing behaviour."],
   ["win probability (WP)", "WPA (win probability added)", "leverage (game situation)", "fourth-down model (bot)",
    "break-even conversion rate"],
   ["13-02", "10-04"],
   ["C: WP chart for Super Bowl LI (28-3)", "C: Fourth-down recommendation heatmap", "S: Decision tree for one fourth down",
    "C: Team aggressiveness vs model recommendation"],
   ["Ben Baldwin's fourth-down model", "NYT 4th Down Bot", "Lions under Campbell"],
   "Be the bot: make every fourth-down call live; compare with the model afterwards.")

ch("13-04", "tendencies-proe-and-charting", "Tendencies: PROE, Personnel, Motion, and Coverage from Charting Data", 4, 15,
   ["Explain expected pass rate (xpass) and PROE; compute by team, season, and situation.",
    "Measure personnel, formation, motion, and play-action tendencies.",
    "Measure coverage tendencies where charting data exists.",
    "Build a one-page data scouting report.",
    "State the caveats of charting data (definitions, coverage, errors)."],
   ["xpass (expected pass rate)", "PROE (pass rate over expected)", "neutral situation", "coverage charting"],
   ["13-02", "08-02"],
   ["C: Team PROE vs EPA scatter", "C: Team tendency dashboard (personnel x pass rate x PA x motion)",
    "C: Coverage mix by team", "S: Scouting-report template"],
   ["2024-2025 team tendencies"],
   "Opponent card: produce a one-page tendency card before a game and grade it live.")

ch("13-05", "tracking-data-and-big-data-bowl", "Tracking Data and the Big Data Bowl", 5, 18,
   ["Understand NGS tracking (10 Hz; x, y, s, a, o, dir) and the coordinate system.",
    "Standardise play direction and align frames to the snap and the throw.",
    "Plot and animate tracking frames with the course's diagram library.",
    "Derive features: separation, pocket area, safety rotation, motion detection.",
    "Sketch projects: man/zone classification, route classification, disguise measurement.",
    "Survey Big Data Bowl themes and winning approaches."],
   ["tracking data", "Next Gen Stats (NGS)", "frame (tracking)", "orientation vs direction", "standardised play direction",
    "separation", "Big Data Bowl"],
   ["13-04", "06-06"],
   ["S: Tracking coordinate system", "T: One real play animated from BDB data with the course library (frame strip)",
    "T: Separation over time for each receiver", "T: Safety depth at the snap, team distribution"],
   ["Big Data Bowl themes 2019-2026"],
   "First tracking chart: choose a play you watched live and plot it with the library.")

# ---------------------------------------------------------------- PART 14
part("14", "The Business of Scheme: Roster, Cap, Draft, and Fantasy", "3",
     "How X's and O's turn into money and fantasy points.")

ch("14-01", "scheme-roster-and-fantasy", "Scheme, Roster, and Fantasy: How X's and O's Shape Money and Points", 3, 18,
   ["Explain positional value with data (QB, edge, LT, WR, CB vs RB, LB, S).",
    "Explain cap mechanics: cap hit, dead money, rookie-contract window, fifth-year option, franchise tag, void years.",
    "Explain scheme fit in the draft (wide-zone OL vs gap OL, two-gap nose vs 3-tech, press vs off corners).",
    "Explain roster construction: 53, game-day actives, practice squad.",
    "Translate scheme into fantasy: route participation, target share, YPRR, RB usage, TE in 12 personnel, PROE and pace.",
    "Predict how a coordinator change shifts fantasy value."],
   ["cap hit", "dead money", "rookie-contract window", "fifth-year option", "franchise tag", "void years",
    "positional value", "scheme fit", "route participation", "target share", "YPRR (yards per route run)",
    "snap share", "game script"],
   ["13-02", "08-03"],
   ["C: Positional cap share vs wins", "C: Draft pick value curve", "C: Target share vs team PROE",
    "S: Scheme-fit archetype chart (body type by scheme and position)"],
   ["2021 Rams trade-heavy build", "Eagles OL investment", "49ers' mid-round wide-zone linemen",
    "Brock Purdy's rookie contract", "Saquon Barkley in 2024"],
   "Scheme-shift draft: for one team with a new coordinator, predict which fantasy assets rise and fall.")

# ---------------------------------------------------------------- PART 15
part("15", "Capstone: Watching Like a Coach", "5",
     "Integrates every per-chapter drill into one protocol and scores the reader's prediction log from Chapter 01-02 onward.")

ch("15-01", "watching-like-a-coach", "Watching Like a Coach: The Master Checklist, All-22, and Charting a Game", 5, 18,
   ["Run the master pre-snap checklist in ~20 seconds: situation -> personnel -> formation/strength -> motion response -> box -> shell -> leverage -> pressure tells -> prediction.",
    "Get and watch All-22 with a four-pass film protocol (OL, QB, coverage, skill players).",
    "Chart a full game with a template.",
    "Break down a complete annotated drive.",
    "Score the season's prediction log with Brier score and calibration plots in Python.",
    "Know where to keep learning (coaching clinics, analytics community, BDB)."],
   ["film-study protocol", "charting (game charting)", "Brier score", "calibration"],
   ["08-04", "10-04", "13-04"],
   ["S: Master checklist one-page card", "A: Full drive (8-12 plays) annotated, frame strips",
    "C: Calibration plot of the reader's prediction log", "S: Charting sheet template"],
   ["A recent playoff drive chosen for variety (verify at writing time)"],
   "Chart a full game: every snap, all checklist fields, prediction, outcome; then score it.")
