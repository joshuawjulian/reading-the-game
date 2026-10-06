# Beginner review (round 2): 06-06 Disguise, Rotation, and Split-Field Coverage

Reviewer persona: casual NFL watcher, never played, thinks a play is a Madden card. Has read
01-01 through 06-05 plus 02-06 in curriculum order. Those chapters are not written yet (only
01-04, 03-02 and 13-02 exist), so "what I know" means their curriculum objectives plus this
chapter's "You'll need" box. I read the .qmd start to finish and the rendered PDF
(`pdfs/06-06-disguise-rotation-and-split-field.pdf`, 23 pages, built 08:30 today from the 08:29
.qmd, so it is current). I looked at every page at 60 dpi and every diagram page at 130 dpi.
Page numbers below are PDF pages.

**Overall.** This round fixes most of what the last review flagged: leverage and the zones are now
in the recap box, drill answers move to the end in print, the rotation direction is taught, and
the Cover 6 corner tell is in place. What still trips a beginner, in order of damage:

1. **"Distance from the ball's line"** (Fig 4's y-axis, and in the text). I read "line" as the
   line of scrimmage, so the tracking figure looked like nonsense until I worked it out from the code.
2. **The diagrams hide the landmarks the text keeps naming.** `no_numbers()` deletes the yard-line
   numbers, nothing says the faint horizontal lines are 5 yards apart, and the hashes are never put
   in yards. So I can't check "on the numbers", "outside the hash" or "13 yards deep" against any
   picture.
3. **Drill 2's answer describes a corner the picture doesn't show.** The answer says "pressed with
   inside leverage", but the drawn CB is head-up on X (both at w = −15). Drill 3 is spoiled in the
   body text.
4. **Two figures look like evidence but are simulated** (Fig 4's 22-of-30 late rotations, and
   Fig 9 entirely). The prose reads them like findings, but they only replay the parameters the
   author typed in.
5. **No real play shows the chapter's core move,** a two-high shell rotating to a robber or
   Cover 3. Both film rooms are general descriptions, and the Vikings one is mostly about
   pressure disguise.

---

## 1. Terms used before they're explained, or never explained

| Where (PDF page) | Term | Problem |
|---|---|---|
| Fig 4 y-axis, Fig 4 caption, p.10 text ("distance from the ball's line") | **ball's line** | Means lateral distance from a line running downfield through the ball. A beginner reads "line" as the line of scrimmage, and the top panel is labelled "Depth beyond the line", which is the LOS. Two different "lines" sit on one figure. Use "distance from the middle (yd)" or "sideways distance from the ball". |
| p.5 "the other one is the likely **post safety**"; p.18 Watch for it "one safety in the **post**"; checklist line 10; drill 2/3 answers | **post** (as in post safety) | The You'll-need box defines *post* only as a route ("breaks deep toward the middle"). "In the post" meaning "the deep-middle spot" is never defined. Same word, two meanings. |
| Fig 2 panel title "+1.0 s · FS spins, SS **drops**"; Fig 4 label "dropped down" | **drop / spin** | The box teaches "zone drop" as a retreat to a landmark, and "spins down" (02-06) as a safety *coming down*. Here "spins" means going *up* to the middle and "drops" means *coming down*. Other movement verbs pile up with no table: creep, walk down, stem, spin, rotate, bail, sink, rob, poach, cheat. |
| Every diagram; p.6 "the Will and the nickel take the curl-flat zones"; p.11 "the Mike takes the hook" | **Will, Mike, W, M, E, T; X, Y, Z, H, R, Q** | The "Reading the diagrams" note explains C, CB and $ only. Will and Mike aren't in the recap box. X/Y/Z/H are used everywhere ("Z's dig", "Y bends") and never recapped: which one is the tight end? |
| p.4 "on the numbers"; p.5 "on or just outside the hash marks… splitting the hash and the numbers" | **hash marks, the numbers** (as positions in yards) | The chapter gives "numbers ≈ 15 yards from the middle" once. The NFL hash's distance from the middle (about 3 yards) never appears; the hash footnote is about sidelines. Since Fig 1 removes the numbers, I can't place "a few yards outside the hashes" vs "splitting the hash and the numbers". |
| p.3 rules paragraph | **neutral zone** | Used with no gloss. |
| p.2 box ("press… corners and bail technique"), p.18 Watch for it ("trailing their man for 2-Man") | **trail** | 06-01 term, not in the recap box, now used in the key post-snap call. |
| p.12 "a bracket on one receiver" | **bracket** | 06-02 term, not recapped. |
| p.4 Fig 1 pointer "outside shade"; caption "shading slightly outside" | **shade** | Never tied to "leverage"; I had to guess they mean the same thing. |
| p.9 one-high-to-two-high box: "deep shots against **single coverage**" | single coverage | Undefined (one-on-one). |
| p.14 stubbie: "a linebacker **walls off** #3" | walls off | Undefined. What does a linebacker *do* to wall off? |
| p.14 "as decoded in **the Throw Deep breakdown cited above**" | Throw Deep | In print, "cited above" means footnote 4. Nothing in the body says what Throw Deep is. Name it: "Cameron Soran's guide to Saban's coverages". |
| p.8 Fig 3 label "open: **MOF**" | MOF | The box gives MOFC and MOFO, never bare "MOF". Write "middle open". |
| p.12 history, p.18 Rams | **Fangio** ("Fangio's tree") | Used three times as if I know him; 06-05 was told *not* to use Fangio for film room, so I may never have met him. Give one clause: "Vic Fangio, the defensive coordinator most associated with the two-high wave". |
| p.15 "pre-snap shifts or motion on 63.9% of **plays**"; p.12 "32.9% of **dropbacks**" | dropback | Never defined. I can guess "pass plays", but the stats depend on it. |
| p.17 Fig 10 caption "labels **BLOWN and COMBO** excluded" | coverage labels | Meaningless to me. Either say "plays charted as a blown or mixed coverage" or drop it. |

## 2. Leaps (a "why" that's missing or assumed)

- **p.4 physics: "A safety who will be a robber 10 or 11 yards deep can line up at 13, but he'd
  rather line up at 11."** Why would he rather? The trade-off isn't stated: at 11 his trip is
  shorter, but 11 is a tell, which the next figure is about. This is the hinge of the whole
  "circle" idea and it's left implicit.
- **p.5 Safety width bullet versus the physics paragraph.** Physics says a safety 7.5 yards from
  the middle can reach the deep middle. The width bullet says "a safety on or just outside the
  hash marks can reach the deep middle. One splitting the hash and the numbers is probably staying
  on his half." Where is 7.5 yards: "just outside the hash" or "splitting"? Without yardage for the
  hash, the two rules don't connect, and the Fig 1 caption's "two yards narrower than usual" is
  unreadable.
- **p.4 Fig 1 caption: "Compared with the textbook picture."** The textbook picture is never
  shown. A ghost layer or a side-by-side "normal two-high" panel would let me *see* "three yards
  shallower, pinched in". As drawn, I'm told the tells rather than shown them.
- **p.7 "Offenses facing two-high tend to run the ball (the box is lighter)."** Why is the box
  lighter? The step "both safeties deep means only 6 or 7 near the line" is assumed. Same with
  "eighth defender against the run" on p.3: eighth counting from what base?
- **p.12–13 trips arithmetic.** "On the trips side… the corner, the safety, the nickel and perhaps
  a linebacker… On the backside it has a corner and a safety against one receiver." Where is the
  Will? Every trips figure (6, 7, 8, 12) has a W on the backside. Counting the dots, I got three
  backside defenders against one receiver, not two, and the "ugly count" argument fell apart until
  I decided the Will must be a run defender. Say what the backside linebacker does.
- **p.13 "Quarters rules… Nobody's rule mentions #3."** Why can't the nickel or the Mike just take
  him? The answer arrives two subsections later (solo: a linebacker can't run with him). Put one
  sentence here: "the underneath defenders can't carry a fast receiver 20 yards deep".
- **p.14 stubbie: "the safety takes #3 deep while staying over the top of #2."** How can one man
  do both? He sits between them and takes whichever goes deep? Not explained, and Fig 8 doesn't
  show #3's or #2's route.
- **p.14 solo naming paragraph.** The chapter defines solo the *opposite* way from "much of the
  pro and big-college quarters vocabulary you will meet online", then puts "down (solo)" on the
  Sunday checklist while saying NFL defenses rarely use it. As a beginner I'll google "solo
  coverage", get the other meaning, and be lost. Either lead with the common usage or explain why
  this book's version is worth a checklist line.
- **p.8 Fig 3 / box definition of the flat.** The box defines the flat as "0–6 yards". In Fig 3 the
  Cover 2 corners "widen into the flats" but finish at about 8.5 yards deep, past the line to gain.
  The picture and the definition disagree, and I don't know which to trust.
- **p.10 tracking text: "within about ten frames (one second) the safeties are in completely
  different places… that half-second to a second is precisely the window a quarterback can
  exploit."** How does a QB exploit it? He's still calling signals. The text should connect it:
  he can change the protection or the play, as p.2 said.
- **p.16 Fig 9 / "Measuring the lie".** The defenses' disguise rates and late shares are typed in
  (`DEFS = {...}`), so the chart just draws the inputs back out. The prose ("The chart makes the
  chapter's argument in numbers") presents it as a result. An analytically minded reader will feel
  cheated. Say plainly that it is a *demonstration of the measurement* on made-up defenses, and
  what the real number would need. Same for Fig 4's "On most rotated plays (22 of 30) nothing
  moves until the snap". That is a design choice in line 746 of the code, not a finding, but the
  caption reads like one.
- **p.17 Vikings film room.** It argues disguise "pays" because the Vikings are high on both
  two-high and Cover 0. Then it admits the chart "shows the menu, not the disguise". The two
  "what to notice" items (six on the line becoming a four-man rush; a blitz look over Cover 6) are
  pressure disguise, Part 7's subject. Nothing in the film room is a safety rotation, which is
  this chapter's main topic.
- **p.6 Fig 2 vs its own caption.** The panel titles say "Snap · nothing has moved", but in the
  code (and visibly in the frames) both safeties creep about 0.8 yards between −1.4 s and the
  snap. That is the very "timing tell" p.5 just taught. Either remove the creep or caption it
  ("a small creep that doesn't change the picture").

## 3. Diagrams I couldn't decode, or whose caption didn't tell me what to notice

- **All field diagrams:** there's no depth or width scale. The faint horizontal lines are (I
  assume) 5-yard lines, but nothing says so. The yard numbers are removed. The orange
  line-to-gain sits at a different depth in every figure (7, 9, 10 yards), so I tried to use it as
  a ruler and got different answers. Add "faint lines every 5 yards" to the "Reading the
  diagrams" note, and consider leaving short tick labels (5, 10, 15) on one sideline.
- **Green rings** (highlights) are never explained. I guessed "the players to watch".
- **Frame-strip legend (Figs 2, 3):** "Defender before the snap (the disguise)" is drawn as a
  solid white square and "Defender now" as a near-white tinted square. In print they look
  identical. On the field the ghosts are *dashed*, but the legend shows them solid. Make the
  legend match (dashed outline) and darken the "now" fill.
- **Fig 2 panel 4:** the "robber" label box sits directly above the **M** (Mike), not the SS. My
  first read was "the Mike is the robber". Move it next to the SS. Also, X has run off the top of
  the panel. Fine, but the ball arrow ends beside the M too, which makes it worse.
- **Fig 3:** the corners' "widen into the flats" is about 1.5 yards of movement, nearly invisible
  next to their ghost markers. The caption tells me to notice it; the picture can't show it.
  The "½" labels at the top edge are cut against the frame.
- **Fig 4:** besides "ball's line", the two panels' bottom curves need a plain sentence: "bottom
  panel: 0 = right over the middle of the field". The green "dropped down" median in the bottom
  panel also moves inward (7 → 4.7 yards). That's the robber pinching in, and nobody tells me.
- **Fig 5 (Cover 6):** the field corner (CB) marker is drawn on top of the "curl-flat" label, so
  the label is partly hidden, and the "hook" label is cut by the dashed divider. The divider
  runs through the ball on the left hash, so the "halves" are visibly unequal. That's correct,
  but the caption should say so, or I think it's a drawing error. The ¼ bubbles sit at 17 yards
  while the field corner's arrow stops at 13.
- **Fig 6 (poach) and Drill 2:** "detached trips (Y flexed off the line)" is not visible. Y sits
  about 1 yard wider and a step deeper than the in-line Y of Figs 7–8. Side by side, I couldn't
  tell attached from detached, and the distinction carries the whole solo-vs-poach argument.
  Exaggerate the split (Y 3+ yards outside the tackle) and label it "detached".
- **Figs 7 and 8 (solo, stubbie):** no #1/#2/#3 labels, unlike Fig 6. The captions talk in
  numbers ("locks on #1… #2… walls off #3"), so I had to flip back to work out that #3 = Y. In
  Fig 8 no routes are drawn, so "staying over the top of #2" is uncheckable.
- **Fig 9:** why do honest defenses A and B not score 100 at the snap? (Some late plays, I
  think.) What does a "bar" mean when the hollow dot is to the *right* of the filled one? (It
  can't be here, but the axis allows it.) The caption is long but never says these rates are
  invented inputs.
- **Fig 10 (Vikings):** one unlabeled grey dot (≈2.9 % Cover 0, 50.5 % two-high) is almost as
  high as the Vikings on two-high. Who is it? "Narrowly" undersells how close it is.
- **Fig 13 (Drill 3):** the FS arrow goes straight down, but the caption says he "walks down
  **and out** toward him". The nickel's arrow is a 1-pixel stub. Z's motion path ends at the
  ball, but the caption says the ball is snapped "as Z passes the quarterback", so he never
  reaches the end of his arrow. Fine, but confusing.
- **Fig 14 (checklist card):** readable and useful. Line 9 ("Run or pass: the offensive linemen's
  first step") sits *after* the rotation call under "At the snap". Shouldn't I see run/pass
  before judging a rotation, given that the rotating safety may be a run fitter?

## 4. Drag and repetition

- **Late rotation is defined three times** (flavour 3 on p.3, the "Timing" tell on p.5, and its
  own section on p.9), and the third adds only the "race" sentence. Fold the Timing tell into a
  forward pointer.
- **"The shell is a hypothesis"** appears in the Madden box, the misconception box, the "read it
  after the snap" paragraph, the checklist intro, two drill answers ("confirms it on his first
  step") and the takeaways. Twice would be enough.
- **Cover 6 is defined four times** (recap box, split-field section, Vikings film room, Watch for
  it).
- **The motion paragraph (p.15) is overloaded:** the motion indicator again (already in the recap
  box), the PFF stat, three defensive answers, and motion at the snap. That is about 180 words in
  one paragraph. Split it.
- **The history section (p.12)** is a list of names (Saban, Belichick, Dantonio, Narduzzi,
  Patterson, Iowa, Staley, Evero) with no "sentence of humanity" and no problem-solution beat
  beyond "wide hashes, option offenses". For a beginner it reads as a footnote moved into the
  body.
- **"Cover 7 and the numbers problem"** is a dead end: no picture and no tell, and the
  conclusion is "ask whose playbook". It is fine as a two-line aside but costs a heading.
- **Length:** the PDF runs 23 pages. The physics section (p.4) and "Measuring the lie" (pp.15–16)
  are where I slowed down most and got least.

## 5. Could I do the "You'll be able to…" items? (drills tried before reading answers)

**Drill 1 (leaning safety).** My answer: "SS is shallower and narrower, so he's coming down; FS
goes to the middle; corners are off and facing the QB, so it's zone, Cover 3; beware the right
side." **Correct**, including the side. But the caption does most of the work ("look closely…
SS has crept to 10… two yards narrower… turned toward the quarterback"). Every cue is named, so
this tests reading the caption, not reading the picture. I could not have produced the
"opportunities" half of the answer (stress the left curl-flat defender, seam between the deep
middle and the deep third). Nothing in the chapter teaches me which throws beat Cover 3 robber.
Try making the caption only state the situation and let me find the tells.

**Drill 2 (safety who isn't home).** My answer: "Left safety is pinched in, so he's not home:
poach. Throw to X." **Correct.** Again the caption points straight at the tells ("look at the left
safety's width… and at the left corner") and gives away the throw ("its best receiver, X, alone
on the left"). I looked at the left corner as told and saw him **directly over X, not inside**.
The answer then says "pressed with inside leverage, taking away the inside… the corner gave up the
outside". The drawing has LCB at w = −15.0 and X at w = −15.0, head-up. So the part of the answer
that teaches the throw (fade outside) depends on a detail the picture doesn't show. Move the CB
about 1 yard inside X.

**Drill 3 (spin with motion).** I got the first half (nobody followed, so zone; FS down and SS to
the middle, so one-high, Cover 3). I got the "catch" only because p.15 already told me: "**Fake
spins:** a safety spins down with the motion on purpose and re-rotates at the snap (Predict the
play 3 below)." That's a spoiler pointing at the drill. Also, the caption says the ball is snapped
as Z passes the QB, which is the *counter* to the catch. So my first instinct was "there is no
catch: motion at the snap stops the re-rotation", and that's half-right by the answer's own logic.
The question is muddy.

Objectives:

| Objective | Could I? | Notes |
|---|---|---|
| Say what disguise is and its price | Yes | The costs list (p.3) is clear and memorable. |
| Spot the tells; say before the snap which way a shell rotates | Partly | On a diagram with the caption's help, yes. On TV I can't judge "two yards narrower" without knowing where the hash is in yards (see §1). |
| Call the two big rotations as they happen | Only on replay | The chapter itself says the live camera rarely shows the safeties at the snap. "As they happen" overpromises; say "on the replay". |
| Recognise split-field / Cover 6 by its two halves; poach, solo, stubbie | Yes for Cover 6 (the one-squat, one-bail corner tell is great). Poach yes. Solo and stubbie only on the diagrams; I couldn't tell attached from detached trips, which decides which is likely. |
| Explain how offenses fight disguise; why late rotation forces post-snap reading | Yes | This section is the clearest in the chapter. |
| Read a tracking chart of safeties; add shell → rotation → leverage | Read the chart: only after decoding "ball's line". Checklist: yes. |

## 6. What I still wonder after finishing

1. **What does this look like in a real game I can find?** Give one specific play (team, season,
   game, quarter, down) where a two-high shell rotated to a robber or Cover 3, so I can pull up
   the replay. Both film rooms are general descriptions.
2. **How often does an NFL defense actually rotate?** The chapter says there's no public number,
   but the Evero/Carolina footnote has one (397 static vs 375 rotated, nearly 1:1). Put it in the
   Watch-for-it box as a benchmark for my own "disguise rate", so I know whether my log of 3 out
   of 10 is low or high.
3. **Can a corner be the post safety?** The code comment mentions "corners rotate to the post in
   cloud or invert calls", but the text never does. If that happens, my "watch the two safeties"
   rule fails.
4. **Rotating into man:** Fig 1 says the rotation lands in Cover 1 robber, but every animated
   example rotates into zone. What do the corners do differently at the snap when the rotation is
   into man?
5. **After the QB sees the rotation mid-drop, what does he throw?** I learn that dagger dies
   against the robber, but not the answer that beats it (the throw the robber vacated). One
   sentence and a pointer to 08-01 would close the loop.
6. **Who makes the trips check, and how fast?** When motion creates trips at the last second
   (p.15), who shouts the check, and what happens if half the defense doesn't hear it? Is that the
   "bust" from p.3?
7. **How do I see this from the couch?** The live broadcast angle hides the safeties. Is there any
   live cue at all (e.g. the safeties visible in the pre-snap wide shot, or the analyst's
   telestrator), or is this purely a replay skill? The Watch-for-it box should say which
   broadcast shot to use for Call 1.
8. **Is the simulated tracking realistic?** I'd like one sentence on whether real safeties' paths
   look like Fig 4 (e.g. "real data is noisier; medians look similar"). Otherwise I can't tell
   whether the figure teaches football or teaches the simulator.
9. **Bunch and empty:** trips gets checks; what about 3x2 empty or a bunch set? Does the same
   #3 problem apply?

---

## Revision (2026-10-06, round 2 → round 3)

Revised `chapters/06-pass-coverage/06-06-disguise-rotation-and-split-field.qmd` against this review and
`06-06-coach.md`. Rebuilt with `build_pdfs.py 06-06-disguise-rotation-and-split-field --html` (OK, zero
errors, 25 pages), rasterized at 60 dpi, and looked at every page; all 14 figures were also rendered at
110 dpi (`_pdfbuild/06-06-rev/preview.py`) and inspected. Fact-check results are kept; the new claims are
sourced (listed at the end).

### Beginner review

**Overall top five**
1. "Distance from the ball's line" → Fig 4 bottom axis is now "Sideways from the middle (yd)"; the caption
   explains both panels ("0 = straight down the middle"); the text and code comments say "sideways from
   the middle / the ball".
2. Hidden landmarks → new `ruler()` helper (drawn on the Field's ax) puts depth labels (5 yd, 10, 15…) on
   the left edge of every field diagram and frame strip, and "hash" and "numbers" labels along the bottom
   of fig-tells and the Drill 1 and 2 figures. The "You'll need" box now gives the hash (about 3 yd from the
   middle) and the numbers (start 12 yd in from the sideline, about 13–15 yd from the middle; new source),
   and the diagram key says the faint lines are 5 yards apart from the line of scrimmage and that the
   orange line-to-gain is not a ruler.
3. Drill 2 corner head-up → `trips_defense()` now presses the LCB a yard inside X (w = −14). Caption asks
   the reader to look at where the corner stands; the answer says "pressed a yard inside X". Drill 3
   spoiler removed (see §5).
4. Simulated figures read as findings → Fig 4 caption says "not real plays" and "we told the simulation
   to start 22 of the 30 rotations at the snap"; the text opens "Read it as a picture of the idea, not as
   evidence". Fig 9: the text says the defenses are made up and the chart "can only give back what we put
   in"; the caption says the same.
5. No real rotation example → added **Film room: Panthers under Ejiro Evero** (rotation, not pressure):
   Alexander's 397 static vs 375 rotated count and Jaycee Horn's "It was just on the snap; everything
   happened," with a what-to-notice. *Not done:* a specific game/quarter/down rotation play. I searched
   (MatchQuarters, PFF Galina 2021, Arrowhead Pride) and found no accessible source that names a play
   with its pre-snap shell; the one candidate (a Chiefs–Chargers rotation) could not be verified
   (Arrowhead Pride 403). Per AUTHORING §6 nothing was invented.

**§1 Terms**
| Term | Action |
|---|---|
| ball's line | Replaced everywhere (axis, caption, text, code comments). |
| post (safety) | Defined in the box: "the deep-middle spot is called the post… the post safety… one safety in the post means MOFC". |
| drop / spin and other verbs | New verb table after the rotation definition (rotate/spin, come down, bail, sink, creep/walk down/cheat, rob, poach). Fig 2 panel title now "FS to the post, SS comes down"; Fig 4 label "came down". |
| Will, Mike, letters | New "Who's who" bullet (Mike, Will, X, Z, Y = tight end, H) with glossary links; diagram key lists Q, R, C, E, T, M, W, $, CB, FS, SS. |
| hash marks, numbers | See top-five 2. Safety-width bullet now in yards ("within about 8 yards… 9 to 11 yards out"). |
| neutral zone | Glossed in place. |
| trail | Defined in the box (trail technique, linked to 06-01's glossary entry). |
| bracket | Defined in the box (linked to 06-02). |
| shade | fig-tells caption: "shading slightly outside (outside leverage)". |
| single coverage | "single (one-on-one) coverage". |
| walls off | Defined in the trips paragraph ("stays in his path and keeps him from running free across the middle"). |
| Throw Deep | Now "Cameron Soran's guide to Saban's coverages, cited above". |
| MOF | Fig 3 label now "middle open". |
| Fangio | One clause at first body use: "Vic Fangio, the defensive coordinator most associated with the NFL's two-high wave". |
| dropback | Defined in the "Who's who" bullet. |
| BLOWN/COMBO | Fig 10 caption: "plays the charters marked as a blown coverage or a mix of coverages are left out". |

**§2 Leaps**
- Why line up at 11 rather than 13 → physics section now states the trade: 13 keeps the picture but costs
  time; 11 makes the job easy but is a tell; "the closer to the real job, the easier the job and the
  louder the tell".
- Width rule vs physics → both now in yards and consistent (7.5 yd out = "a few yards outside the hash";
  "on the numbers" ≈ 14 yd out ≈ 14 yd from the landmark).
- "Textbook picture" never shown → fig-tells now draws the textbook two-high spots as grey dashed outlines
  with a legend; the caption measures the cheats against them.
- Why the box is lighter / "eighth defender" → explained with counts (six or seven near the line; a safety
  makes it seven or eight) in the costs list and the two-high-to-one-high box.
- Trips arithmetic / backside Will → the trips paragraph now counts only players who can run 20 yards
  downfield and says the Will's jobs are the run and a short zone.
- Why can't the nickel or Mike take #3 → same paragraph: the underneath defender walls #3 but "can't carry a
  fast receiver 20 yards deep" (merged with coach C1).
- Stubbie safety doing two jobs → text explains he aligns deeper than and between #2 and #3; Fig 8 now draws
  #3's seam and #2's short out so the reader sees him carry #3.
- Solo naming → paragraph now leads with the common online meaning (= this book's poach), then says why the
  book keeps the linebacker version under "solo"; checklist line 11 reads "down as a run defender (solo,
  mostly vs tight-end trips)".
- Flat 0–6 vs Cover 2 corners at 8.5 → Fig 3 caption explains they "play the flat from on top, at about 8
  yards rather than the flat's usual 0 to 6", because the outs break at 8.
- How a QB exploits an early rotation → text now says he can change the protection, check to another
  play, or pick the side his progression starts on.
- Fig 9 / Fig 4 presented as results → see top-five 4. "The chart makes the chapter's argument in numbers"
  is gone.
- Vikings film room is pressure disguise → kept (the coach said "no change", and it carries the "menu"
  argument), trimmed, and the new Panthers film room supplies the safety rotation.
- Fig 2 "nothing has moved" but safeties creep → creep removed from both rotation plays (a tiny Mike
  shuffle supplies the pre-snap frames); captions say "no defensive back moves".

**§3 Diagrams**
- Scale on all field diagrams → `ruler()` (see top-five 2). Diagram key explains the lines and orange line.
- Green rings → explained in the key ("the players to watch").
- Strip legend → ghosts are now hollow (no fill) with dashed outlines, and the legend uses matching dashed
  and filled patches ("Dashed outline: where he stood… / Solid, filled: where he is now").
- Fig 2 panel 4 → "robber" label moved beside the SS; window deepened so X stays in frame; ball arrow ends
  at the SS. Coach A1 corner fix applied (see below).
- Fig 3 → corners now widen three yards (to ±19) so the move is visible against their outlines; "½" labels
  moved down off the frame edge.
- Fig 4 → axis, caption, robber pinch-in (about 7 → under 5 yd) explained.
- Fig 5 (Cover 6) → coach B1 zones applied (no deep-middle gap); "curl-flat" and "hook" labels no longer
  covered (hook moved off the divider; field receivers and corner widened); caption explains the unequal
  halves (24 vs 30 yd); corner drops now reach their ¼ bubbles; corners highlighted since they are the tell.
- Fig 6 / Drill 2 detached trips → Y now about 4 yd outside the tackle (coach B3), labelled "Y detached";
  poach FS and Mike landmarks moved with him.
- Figs 7 and 8 numbering → #1/#2/#3 labels added (Fig 7 also "Y in-line"); Fig 8 routes drawn.
- Fig 9 → caption says the inputs are invented, gives A/B's disguise rates (why they aren't at 100) and
  says a filled dot can't fall left of the hollow one here.
- Fig 10 → the grey dot is labelled "Bills"; text and caption give 51.4% vs 50.5%. While checking, found
  the Vikings and Ravens tied on Cover 0 (5.771% vs 5.770%): text now says "behind only Kansas City and
  level with Baltimore"; exact counts in fn `labels`.
- Fig 13 (Drill 3) → caption no longer says "and out" (coach B4); the 1-yd nickel stub removed; the
  snap-timing sentence removed from the caption (see §5).
- Fig 14 → run/pass (8) now comes before rotation (9), with "(a rotating safety may be a run fitter)".

**§4 Drag**
- Late rotation defined three times → the Timing tell is now two sentences and a pointer; the section keeps
  the definition.
- "Shell is a hypothesis" → kept in the Madden box and takeaways; cut from the misconception box, checklist
  intro ("first guess") and drill answers 1 and 3.
- Cover 6 defined four times → Vikings box now just "split-field Cover 6"; recap box and split-field
  section keep theirs (prerequisite recap and the topic itself).
- Motion paragraph → split into a paragraph, a three-item list of defensive answers and the motion-at-the-
  snap counter.
- History section → rewritten around the problem (run defense vs deep ball against spread/option on wide
  hashes) and its answer, with a sourced sentence of humanity: Gary Patterson's "Don't go till you know"
  clinic quote (Grantland 2015).
- Cover 7 heading → demoted to a short paragraph without a heading.
- Length → physics and "Measuring the lie" both tightened. The chapter still runs ~11,200 words of prose
  (25 PDF pages), well over the 6,000 target, because most review items asked for additions. *Open.*

**§5 Drills**
- Drill 1 caption gave away the tells → caption now only states the situation and points to the ruler and
  hashes; the measurements moved into the answer. The "opportunities" half is now taught in the body
  ("What beats the robber" paragraph and Cover 3 seams).
- Drill 2 → corner inside X (above); caption no longer says "its best receiver"; the answer conditions the
  throw on X being the best receiver.
- Drill 3 → "(Predict the play 3 below)" pointer removed; the snap-timing line removed from the caption;
  question reframed as "what could the defense still do at the snap, and how would the offense take that
  away?", so motion at the snap is now the expected answer rather than a contradiction.
- Objective "as they happen" → now "on the replay (and, with practice, live from the wide shot)".

**§6 Still wonder**
1. Real play → see top-five 5 (Panthers film room; no verified single play).
2. Benchmark → Watch-for-it "Log the lie" cites the Panthers' ~half rotation rate.
3. Corner as post safety → corner-disguise bullet adds the *invert* and "watch the two deepest defenders,
   whoever they are".
4. Rotating into man → new paragraph after Fig 2: same safety movement, corners stay on receivers (press or
   trail) instead of bailing.
5. What the QB throws vs the robber → new "What beats the robber" paragraph plus a pointer to 08-01.
6. Who makes the trips check → "a safety or the Mike shouts and signals… a defender who doesn't hear it plays
   the old call", tied to the bust.
7. Couch view → Watch-for-it now says which shots show the safeties and that Call 1 is often a replay skill.
8. Is the simulation realistic → new paragraph: real lines are noisier; not validated against real tracking.
9. Bunch and empty → one paragraph: empty 3x2 has the same trips question; bunch is handled with banjo
   calls (06-02).

### Coach review

| Finding | Action |
|---|---|
| A1 Cover 3 corner beaten by X's go | Applied: `drop("LCB", (20.5, -16.0), speed=5.5)` and optional `drop("RCB", (15.0, 15.5))`. Checked positions: at 2.6 s LCB (20.5, −16.0), X (18.8, −15.0). |
| A2 Drill 2 corner head-up | Applied once in `trips_defense()` (LCB w = −14.0, per E); poach keeps its off-corner override. Caption and answer updated. |
| B1 Cover 6 deep-middle gap | Applied all zone sizes, boundary corner (5.0, −16.0) → (5.5, −17.0), and the optional field-side widening (Z at +18, Y at +11, defenders moved with them). |
| B2 fig-tells nickel on TE | Applied: nickel over H (1.5, −8.2), Will over Y (4.5, 7.0); pointer moved; caption names H and Y. |
| B3 detached trips spacing | Applied: Y (d −1.5, w 7.0); poach FS lands (17, 3), Mike (7, 5). |
| B4 "walks down and out" | Applied: caption "walks down to about 9 yards on the side Z is heading to". |
| C1 "Nobody's rule mentions #3" | Applied (reworded around #2 and #3 both vertical; #3 walled by the hook/apex player). |
| C2 invert | Applied in the corner-disguise bullet. |
| C3 "ready to bail" | Applied: "ready to backpedal or turn and run to a deep third". |
| C4 1.3–1.5 s landmark benchmark | **Not applied:** no source found; the coach said to skip it without one. |
| D film rooms | No change requested; Vikings trimmed, Cover 0 tie corrected (see Fig 10 above). |
| E code | `drop()` parking checked by printing positions (A1). No gridiron edits. |

### New sourced claims
- NFL yard-line numbers: bottom edge 12 yd from the sideline (Wikipedia, "American football field", citing
  the NFL field rules), added to fn `hashes`.
- Patterson "Don't go till you know" and the flat-foot-shuffle quote: Grantland (Brown, Sept 1 2015), new fn
  `patterson`.
- Panthers 397/375 and Jaycee Horn quote: MatchQuarters (Alexander, Apr 20 2026), new fn `panthers` (notes
  the article doesn't name the season).
- Bills 50.5% two-high; Vikings/Ravens Cover 0 tie: course calculation, added to fn `labels`.
- Duplicate footnote references (`saban7` used twice) split into `saban7` + new `cover7` so the PDF no longer
  prints the same note twice; the second Vikings CBS reference was dropped for the same reason.

### Library notes (gridiron not edited)
- `Field` draws the painted numbers centred 12 yd from the sideline; by rule the *bottom edge* is at 12 yd,
  so the centre is nearer 13. Harmless here (numbers are removed), but worth fixing in `field.py`.
- No depth ruler or landmark labels in `Field`; this chapter's `ruler()` does it on the ax. A `Field(ruler=True)`
  option would help every chapter.
- A play with no pre-snap motion has no negative-time frames, so the chapter adds an invisible 0.2-yd Mike
  shuffle to get "before the snap" panels. A `Play(presnap=1.5)` option would be cleaner.
