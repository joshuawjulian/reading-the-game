# 01-05 The Pre-Snap Phase: beginner reader review

Reviewer persona: casual NFL watcher who has never played and has read only 01-01 to 01-04.
Read start to finish in the rendered PDF (`pdfs/01-05-the-pre-snap-phase.pdf`, 20 pages, rendered
after the last .qmd edit) and in the source. Line numbers refer to the .qmd.

**Overall:** strong chapter. The voice matches the pilots, the "why" behind the four fouls is
excellent, and the kill-call arithmetic (6 v 6 keep, 7 v 6 kill) is the best moment. The main
problems: (a) one contradiction that sits at the centre of the chapter (stillness vs running start),
(b) one drill whose second half the body never teaches, (c) a vocabulary ladder that is described
in the wrong order, and (d) three diagrams where the thing to notice can't be seen.

## 1. Terms used before they're explained, or never explained

| Where | Term | Problem |
|---|---|---|
| fig-shift caption (l.248), fig-defense-moves caption (l.1024) | "simulated, in Big Data Bowl tracking coordinates" | Big Data Bowl isn't mentioned in 01-01 to 01-04. To me it means nothing. Add a half-sentence gloss or a footnote: "the NFL's public player-tracking dataset; you'll load it in Part 13". |
| l.211, l.444 | **T** formation; "single wing" (l.446) | Rockne's backs "lined up in a T" comes before any explanation of what a T is. Later "T formation" is bolded but still not described, and the single wing never is. One clause each would do it ("three backs in a row behind the quarterback, who takes the snap under center"). |
| l.331 | "backfield player" | 01-03 taught that anyone behind the line is in the backfield, but a fan reads "backfield" as the running backs. The jet-motion receiver and the slot H are "backfield players", and that is exactly the case I'd get wrong. Say it outright: "this includes the Z and slot receivers standing a yard off the line." |
| l.426 | "hard to **jam** at the line" | Not defined. 01-03 used "press". |
| l.913 | "all-out blitz" (Purdy quote) | Comes before the blitz gloss at l.1018. "All-out" is never explained. |
| fig-mike-id caption, l.945 | "down linemen" | Easy to infer, but unglossed. |
| fig-mike-id, right panel tag | "re-ID" | Jargon; say "name a new Mike". |
| l.1081 | "who's the extra blocker?" | "Extra blocker" isn't defined anywhere. |
| l.1087–1092 | "rotate at the snap", "late rotation" | Used in the summary paragraph and table as if known. Never explained, even as a gloss. |
| l.1082 | "Late shifts and **tempo**" | Tempo was glossed in 01-04, but this chapter never discusses it. In the table it reads as new. |
| Answer 1 | "previous spot", "replaying the down", "defense accepts/declines" | The defense's option on an offensive foul is new here. 01-04 only covered the offense's option on a defensive foul. |
| Answer 3 | "live-ball foul", "pass interference" | The body says "the play goes on" and never uses "live-ball". The live/dead terms appear only in the glossary entry and footnote [^rulesnz]. Pass interference is undefined (minor). |
| Glossary entry *Offside* (l.10) | "For the defense it is usually…" | This implies there is an *offensive* offside, but the body never mentions it. I immediately wondered whether a lineman lined up in the neutral zone is offside, a false start or an illegal formation. |

## 2. Leaps: a missing or assumed "why"

1. **Stillness vs running start: the central contradiction (l.218–221 vs l.425–431).** The Set
   section says the 1927 rule exists so the snap gives "a head start of a fraction of a second, *not a
   running start*" and that "the play has to start from a standstill." Two pages later, motion's job
   is "**It gives a player a running start**," and jet motion sprints at the snap. As a reader I
   thought "so the rule failed?" Reconcile it explicitly: the rules allow exactly *one* player, moving
   *sideways or backward*, which is the compromise. That is also the missing reason for each motion
   rule:
   - Why "never toward the line"? Because that is the 1920s running start at the defense.
   - Why only one man? Because more than one is the Notre Dame box.
   - Why not linemen? Not explained at all.

   Right now the three motion rules are stated as bare rules, with no "why", in a chapter whose
   whole method is the "why".
2. **The shift's X/Z swap (l.240–244, fig-shift).** "X steps back off the line, and Z steps onto it."
   *Why?* 01-03 set this up perfectly: if Y moves beside the left tackle and X stays on the line
   outside him, Y is "covered" and ineligible. And with Z off the line on the right, the offense has
   only six on the line. So the swap keeps seven on the line and Y eligible. That's a great
   payoff of 01-03, and it's missing. Without it the X/Z steps look like decoration.
3. **Why do defenses set the front to the strength? (l.298–302)** "Defenses set their front toward the
   offense's strength" with no reason. One clause is enough: the tight end is an extra blocker, so
   that side needs more defenders.
4. **Hard counts look like a losing trade (fig-fouls-by-situation, l.551–552, caption).** The data say
   "in every situation the offense commits more pre-snap fouls than it draws". The obvious beginner
   question is "then why does anyone hard count?" It goes unanswered. The chart also doesn't isolate
   hard counts: third-and-short false starts may come from noise, nerves or pass-rush anticipation,
   not from the team's own hard count. Either soften "That trade shows up clearly in the data" or add
   the reason it's still worth it (free plays are big; one 30-yard TD outweighs several 5-yard flags;
   the hard count also *slows* the defensive line's get-off even when nobody jumps). Also, the "4th &
   3+" bar is lowest of all, and I wondered why. Say that it's mostly punts and field goals.
5. **"The silent count works" (l.640–642)** is an over-reach from false-start counts alone. The
   chapter's own stated cost (l.603–605: linemen can time it, so they get off faster) isn't something
   false-start data can see. Say "it costs no extra false starts" and keep the get-off cost explicit.
6. **The kill-call box arithmetic (l.858–868).** Two gaps:
   - Why aren't X, H and Z counted as blockers? 01-03 told me receivers block on runs. One clause would
     fix it: "they're too far away to reach box defenders."
   - Show the *pass* side of the arithmetic too. Left panel: 5 defenders outside the box against 4
     receivers. Right: 4 against 4. "Should have room" currently rests on faith.

   Also, "roughly between the tight ends" (l.858): the picture has one tight end.
7. **Naming the Mike, right panel (fig-mike-id, l.987–990).** In the left panel the centre already has
   M. In the right panel M walks into the A-gap, and he is still in front of the centre. So *what
   broke?* The text says it "changes the arithmetic" but the picture shows the same assignment. A
   beginner needs the concrete failure, e.g. the Will walks up too and now there are six rushers for
   the five linemen plus a back who was assigned elsewhere, or M's new spot puts him on the guard's
   side of the slide. As drawn, the panel undercuts its own point.
8. **Offside vs NZI boundary (l.732–743).** "Free path to the quarterback" and "a nearby offensive
   player" are the deciding facts, but neither is explained. How near is "nearby"? Does lining up
   over the tackle in the neutral zone automatically count? Drill 3's answer depends on this ("If the
   end had kept going *past* the tackle…").
9. **Which pre-snap fouls stop the play?** The body gives this for the four neutral-zone fouls only.
   For illegal shift and illegal motion it says just "five yards" (l.238, l.338). That they are
   live-ball fouls, with the defense choosing, appears only in Answer 1 (see §5).
10. **"Whoever moves last has the advantage, which is why offenses snap with the play clock at :02
    after a late motion" (l.1089–1090).** That's a new claim in the summary. It is unsourced, and it is
    in tension with l.436–439, which treats a late snap as a cost ("the defense gets more time to
    sort itself out").
11. **"Most teams sit in between, with kill calls on most plays and a few checks" (l.922).** Stated as
    fact without a source. Hedge it or cite it.
12. **"It's why offensive linemen block better than you'd expect when they're outweighed" (l.529).**
    Asserted, not shown.

## 3. Diagrams I couldn't decode, or captions that don't say what to notice

- **fig-shift (frame strip, p.3).** The X and Z moves ("X steps off the line, Z steps onto it") are
  invisible. At this scale a 1-yard depth change can't be seen, and X and Z look identical in every
  frame. Either label them in the -2.6 s frame ("X off", "Z on") or skip that part of the shift. The
  defensive trails in the -1.4 s frame form a tangle of long orange lines across the formation, and
  the Sam (S) sits on top of the left E/T at -1.4 s. It is hard to see "the defense flipped". A
  one-word tag at the snap frame ("S now on the left") would make the story readable in print.
- **fig-legal-motion (p.4).**
  - The "two men moving at the snap" (FLAG) panel and the "one at a time" (LEGAL) panel are **visually
    identical** apart from tiny "1" and "2" digits. Both show H and Y with arrows in the same places.
    The one panel that should teach the difference can't. Show H's arrow ending with a stop bar, or
    H drawn at his *finished* spot.
  - The caption says "each panel shows the moment of the snap", but the players are drawn at their
    *starting* spots with arrows. Which is it?
  - The "a man on the line in motion" FLAG panel ("X is on the line: only a back may move")
    contradicts the bullet at l.331–332, which says a receiver on the line *can* slide along it if he
    stops before the snap. The panel should say "X still moving at the snap".
  - X (on the line) and Z (off it) look the same depth, so I can't see why X is flagged and Z wouldn't
    be.
- **fig-presnap-fouls (p.6).** The PFF motion-share annotations ("~38% of plays", "~64%") point with
  leader lines at dots on the *foul-rate* line. It reads as if 0.1 on the y-axis is 38%. Put the
  motion share in a separate text box or a secondary panel. The first two series aren't needed to
  make this section's point.
- **fig-neutral-zone (p.9).** Good figure. One problem: the "neutral zone (drawn ~2x)" leader line runs
  through the left E box, so it looks like it labels the defender. Also, the Offside panel and the NZI
  panel show the end in the same spot. The only visual difference is the tackle, and the timing
  ("at the snap" vs "before") isn't shown. That's acceptable, but the caption could say "the pictures
  are identical; what differs is *when* and *whether a blocker reacted*".
- **fig-kill-call (p.11).**
  - In the right panel the walked-down SS sits *on the edge* of the shaded box, half outside it, yet
    he is ringed as one of the 7. The one defender the count hinges on should be clearly inside.
  - The "safety walks down" label covers the "4" of the "40" yard number (only "0" shows) and nearly
    touches the "7 in the box" tag.
  - The routes in the right panel aren't explained, so "throws quickly to receivers with fewer
    defenders around them" isn't visible.
- **fig-mike-id (p.12).** In the left panel the R→W and C→M block lines both run straight upfield
  through the line, so they read as runs or routes, not blocks. See also leap 7.
- **fig-defense-moves (p.14).**
  - In the snap frame M overlaps the left T box ("T M T" stacked): a label collision.
  - In the +1.1 s frame the QB has disappeared into a ball marker, and it isn't clear that M "dropped".
    Tag M in that frame ("M drops").
  - The caption doesn't say what the offense is doing (routes drawn but unexplained).
- **fig-predict-free (p.18).**
  - The ringed E box touches the Y circle.
  - The caption says "Before anyone can block, the quarterback launches a deep throw", yet the figure
    shows R blocking and a full dropback.
- **Print layout:** pages 2 and 13 are half blank (a figure pushed to the next page), and pages 16–17
  each hold one drill on a mostly empty page. That makes the print version feel padded.

## 4. Drag and repetition

- **The free play is explained four times.** 01-04 already taught it, with the same link. Here it is
  presented as new ("That choice has a name… Fans and broadcasters call this a free play", l.753–758),
  then explained again in the Rodgers film room, then again in Answer 3. Acknowledge 01-04 ("the
  *free play* you met in 01-04") and cut one retelling.
- **Drill 2 is given away by the body.** The kill-call cost paragraph (l.879–881) already says "A
  safety can walk down at :07 on the play clock, wait for the quarterback to kill the run, then back up
  at the snap". It's the same scenario, down to the same :07. The drill tests recall, not application.
  Change the drill (for example a 7-man box with *two* safeties high and a nickel back walking in,
  or a third look the kill call didn't plan for).
- **Rodgers film room, second paragraph (l.774–781).** The Packers drew *fewer* accepted jumps. The
  section offers two readings, then a caveat that may cancel the stat, then "Either way". I came away
  with nothing reliable. Cut it to one sentence, or drop the statistic.
- **Forward links pile up.** 02-06 is linked 6 times and 02-05 6 times, mostly with "you'll see in /
  full guide is in". The "Why motion exists" section alone has four forward pointers in three
  paragraphs. Keep one per section.
- **Three foul charts in a row** (fig 3–5) is a lot for a Level 2 chapter. Fig 3's message (motion fouls
  stayed rare) fits in one sentence, and its chart confuses (see §3).
- **The hook is never resolved.** The opening ends with "the right tackle flinches and a yellow flag
  flies" after a defender stood "nose to nose with the center". After reading the fouls section I
  wanted the payoff: whose flag was it? (A false start on the tackle, or an NZI if a defender
  triggered the flinch?) Return to the hook in the takeaways or near the fouls figure. It's the
  perfect mini-drill.
- **Film room Eagles (l.653–655):** "The one year the pattern clearly broke was 2020." In the chart,
  2021 is the *clearer* break (home ~0.75 vs road ~1.1, while 2020 is nearly tied). The caption itself
  says "one of the two exceptions was 2020". Fix the text.

## 5. Can I actually do the "You'll be able to…" items?

| Objective | Result |
|---|---|
| Shift vs motion; spot illegal ones | **Mostly.** I can do the rules, but would misjudge a slot receiver ("is H a backfield player?"), and the legal-motion figure left me unsure whether a receiver on the line may slide (bullet: yes if he stops; figure: "only a back may move"). |
| Cadence / hard / silent counts; tell the four fouls apart | **Yes for definitions.** Offside vs NZI stays fuzzy ("nearby", "free path"). I can't say what happens if the *offense* is in the neutral zone. |
| Tell audible / check / kill call / check-with-me apart; guess when the QB is changing the play | **Partly.** l.788 says the four terms run "from most freedom to least", but the list runs audible (umbrella), check (least), kill call, check-with-me ("goes furthest"), which is least-to-most after an umbrella term. That confused me. Whether a kill call is a kind of check is never settled, and the Madden box then says real audibles "are kill calls and checks". Guessing *when* the QB is changing the play: the chapter gives almost no observable tells beyond "he's shouting", and dummy calls make shouting unreliable. Name 2–3 visible cues (linemen re-setting or changing stance, the back switching sides, receivers looking back at the QB, the QB turning and calling to both sides, a re-set of the play clock wait). |
| Why the QB/center points at a linebacker | **Yes.** |
| Recognise defensive pre-snap moves and that they may be a bluff | **Yes, conceptually.** Telling a real blitz from a bluff gets a single sentence (weight on toes vs flat-footed). That's enough for Level 2. |
| List what each side is trying to learn | **Yes** (the table is good). The defense's side in the table includes "what's the protection, who's the extra blocker", which the body never explains. |

### Predict the play (attempted before opening answers)

1. **Quick snap after a shift.** My answer: "Illegal shift, 5 yards. The whistle blows, the play is
   dead and the six yards don't count." **Half wrong.** The answer says the play is live and the
   defense chooses whether to accept. Nothing in the body tells me illegal shifts are live-ball fouls,
   or that the *defense* has an accept/decline option. The only accept/decline teaching (here and in
   01-04) is the offense's option on defensive fouls. The second question ("what happens to the
   six-yard gain?") isn't answerable from the chapter. Add one sentence in the Shift or Motion section,
   or a small "which pre-snap fouls stop the play" table with all six fouls. Answer 1's two-minute
   false-start/10-second runoff aside is new information that comes far too late (fine as a bonus,
   but flag it as one).
2. **The safety at :07.** My answer: "Kill it, because 7 v 6 leaves one free defender. The risk is
   that he's bluffing and backs out." **Correct**, but only because the body spelled out the same
   scenario (see §4). The "risk either way" half of the question also wants the risk of *keeping* the
   run. The answer only states it implicitly.
3. **Fourth-and-1 heave.** My answer: "Free play. Offside is a live-ball foul, so if it fails take 5
   yards = first down." **Correct and easy** after three earlier tellings. The "what would change the
   answer" coda is the best part of the answer.

## 6. Knowledge gaps: what I still wonder

- **The opening scene:** whose flag was it?
- **Can the offense be offside?** What happens if a lineman lines up in the neutral zone or a receiver
  lines up with his foot over the line? (The glossary hints at it.)
- **Why the asymmetry?** Why can eleven defenders move freely while the offense gets one? (Implied by
  "the offense knows the snap", but never said in one sentence.)
- **The defense's own audibles.** How does the defense communicate *its* checks? Who calls them (the
  green-dot Mike from 01-04/01-03?), with what signals, and what happens when motion forces a late
  coverage change? The defense's version of "Changing the play at the line" gets one clause (l.794).
  A short paragraph would balance the chapter.
- **Motion after a shift.** Can a player go in motion right after a shift without a second reset? (Yes,
  once the 1-second set is complete, but this is never stated, and it's the most common sequence on
  TV.)
- **The shotgun snap.** In the shotgun, who triggers the snap: the QB's clap or foot lift to the center
  (who is looking between his legs), or to the guard? The silent-count paragraph mixes both.
- **The play clock at the line.** How long does a typical huddling offense actually have at the line?
  How does the QB see the play clock (it was "play clock :07" in drill 2)? And who decides when to
  snap: the QB or a fixed count?
- **How refs judge an "obvious attempt"** by the QB to draw the defense offside (head bob, clap rhythm).
- **Free plays per season.** How common are free plays now, league-wide? The only number is Rodgers'
  12 TDs from 2008–2017.
- **Can a tight end in a three-point stance go in motion?** (He's on the line, so no, unless he
  shifts off first.) This is the question I'd have on Sunday after seeing a TE motion across.

## Priority fixes (if only five)

1. Reconcile "standstill / not a running start" with "motion gives a running start", and give the
   "why" for each motion rule (§2.1).
2. Teach that illegal shift and illegal motion are live-ball with the defense's option, or change
   Drill 1's second question (§5).
3. Fix the "most freedom to least" ordering and settle the check / kill call / audible hierarchy (§5).
4. Make fig-legal-motion's "two at once" vs "one at a time" panels visually different, and fix the
   on-the-line panel's wording (§3).
5. Explain the X/Z swap in the shift via 01-03's covered-receiver rule, and make it visible in the
   strip (§2.2, §3).

## Revision (2026-10-06)

Revised against this review and `01-05-coach.md`. Fact-check items kept as verified; new claims are sourced
(2026 rulebook text for every new rule detail; nflverse recalculation for new numbers; FACTS-current §5 for the
tush-push coda). Rebuilt with `build_pdfs.py 01-05-the-pre-snap-phase --html` (OK, 21 pages) and every diagram page
was rasterized and inspected.

### Beginner findings

| Finding | Action |
|---|---|
| §1 "Big Data Bowl" unexplained | First animation caption now glosses it ("the NFL's public player-tracking dataset, which you'll load yourself in Part 13"); both strips labelled "simulated tracking in Big Data Bowl format". |
| §1 T formation / single wing | T glossed at first use (QB behind center, three backs side by side) and linked to the 02-03 glossary entry; single wing glossed (direct snap to a deep back) and linked to 11-01; Wikipedia source added to fn `tform`. |
| §1 "backfield player" | Motion rules now say outright that "backfield" means anyone a yard off the line, including the slot and the Z, and that a TE in his stance on the line can slide but must stop. |
| §1 "jam" | Replaced with **press**, glossed and linked to 06-01. |
| §1 "all-out blitz" before the gloss | Blitz glossed at its first use in the Purdy paragraph (links to 02-05 glossary). |
| §1 "down linemen" / "re-ID" | "Down linemen" glossed in the Mike text; "re-ID" replaced by "name a new Mike". |
| §1 "extra blocker" | Table row rewritten ("Who is blocking whom, and is the back staying in?"); the Mike figure and text show the back's "W if he comes, else release" job. |
| §1 "rotate at the snap", "late rotation" | **Rotate** explained in "A safety walks down" before the summary uses it. |
| §1 "tempo" in the table | Table cell changed to "A late shift or motion, then a quick snap"; tempo now appears only in Connections with its link. |
| §1 previous spot / replay / defense accepts | New live-ball paragraph and Table 1 (which fouls stop the play) teach accept/decline, the previous spot, the replayed down, and that the *defense* chooses on the offense's live-ball fouls; accept/decline linked to 09-03. |
| §1 "live-ball foul", pass interference | "Live-ball foul" defined in the body; pass interference glossed in Answer 3. |
| §1 Offside glossary implies offensive offside | Body now covers offensive offside (rule 7-4-5/7-4-1; 21 accepted calls in 2025, fn `offoff`); glossary entry rewritten. |
| §2.1 stillness vs running start | Set section now ends by flagging "one carefully fenced exception"; the Motion section opens by reconciling it and gives a *Why* for each rule (one man = no Notre Dame box; never toward the line = no running start at the defense; backfield only = linemen inches from opponents, and the seven on the line fixed for eligibility). Footnote notes these are the book's reading of the history, not rulebook text. |
| §2.2 X/Z swap | New paragraph explains it via 01-03's covered-receiver rule (Y would be covered; only six on the line); named a **tight end trade** (linked to 02-06 glossary). |
| §2.3 why front to the strength | One clause added: the TE is an extra blocker, so the defense puts one more man there. |
| §2.4 why hard count at all; 4th & 3+ bar | Text softened ("the data can't tell a team's own hard count from crowd noise or plain nerves") and a new paragraph gives three reasons (flags not worth the same; 4th-down hard count nearly free because a punt was coming; chart counts all false starts). Caption now says 4th & 3+ is ~85% punts/FGs (recomputed: 85.4%). |
| §2.5 "the silent count works" | Now "costs no extra false starts on average", with the get-off cost and lost hard count stated as invisible to penalty data. |
| §2.6 kill-call arithmetic | Receivers' exclusion explained; pass-side arithmetic added (5 outside the box v 4 receivers, then 4 v 4 with one deep safety); "between the tight ends" replaced by the 02-05 box definition. |
| §2.7 Mike figure shows nothing broken | Right panel redrawn per coach A1 (preferred fix): the nickel walks down after the call, 7 can rush v 6 blockers; text and caption give the concrete failure and both answers (name a new Mike / throw hot). |
| §2.8 offside vs NZI boundary | "Nearby" (2½ positions; split receiver on that side; over-the-center case) and "free path" (level with or past a lineman, unimpeded path) defined from rule 7-4-4; lining up in the neutral zone over the tackle isn't automatically a foul. |
| §2.9 which fouls stop the play | Table 1 lists all six fouls; shift section flags that an illegal shift doesn't stop the play. |
| §2.10 "snap at :02" claim | Removed; summary now says offenses like to snap soon after their final motion, consistent with 01-04 and with the motion trade-off paragraph. |
| §2.11 "Most teams sit in between" | Replaced with an unfalsifiable-safe framing (the league sits along that spectrum; it shifts when QB or play-caller changes). |
| §2.12 OL "outweighed" claim | Removed (coach C2: NFL OL usually outweigh DL); replaced with the pass-rusher get-off point. |
| §3 fig-shift | X and Z tagged in the −1.4 s panel ("X stepped back off the line", "Z stepped up onto the line"); Y tagged mid-cross; snap panel tags "S and SS have crossed to the left"; Sam's loop raised so he no longer sits on the E/T; Y's path dropped behind the QB. |
| §3 fig-legal-motion | Redrawn at the moment of the snap: solid dot = where he is at the snap, dashed outline = start, arrow = still moving, bar = stopped. "Two at once" (two arrows) and "one at a time" (H with a stop bar, Y with an arrow, numbered 1/2) now look different; the on-the-line panel says "X lined up on the line: he had to stop first" plus an "X: on the line" pointer. |
| §3 fig-presnap-fouls | Replaced by fig-motion-fouls: two panels (PFF motion share; illegal shift/motion per team-game with false starts in grey for scale). No more PFF labels pointing at foul-rate dots. The FS and defensive-jump trends moved to text and fn `fouldata`. |
| §3 fig-neutral-zone | Neutral-zone label moved clear of the E; caption now says offside and NZI look alike in a still, and the difference is timing and whether a blocker reacted. |
| §3 fig-kill-call | Rotated safety placed well inside the box; numbers dropped (no "40" collision); named run blocks; routes explained in the caption (throw away from the rotation, back protects, TE becomes a receiver). |
| §3 fig-mike-id block lines | Replaced by dotted responsibility leaders (back's leader routed through the B-gap, not through the guard); caption says they are responsibilities, not paths. |
| §3 fig-defense-moves | M placed higher so it doesn't stack on the T boxes; rushers stop in front of the setting linemen; "M drops into coverage" and "QB, with the ball" tags in the +1.1 s panel; numbers dropped; caption describes the offense's routes and the back's block. |
| §3 fig-predict-free | Ringed E moved wider (no contact with Y); caption no longer says "before anyone can block". |
| §3 print layout | Drill figures resized so Drills 1 and 2 share a page (21 pages, was 20 with less content). Some half-pages remain where Typst keeps a figure with its caption; not fixable without fighting the layout engine. |
| §4 free play explained four times | Body now says "the free play you met in What a Play Really Is"; retellings cut to one in the body, one in the film room (now about tempo and the code word), and the drill. |
| §4 Drill 2 given away | Replaced: the nickel walks in on the *backside* of a run to the right with two safeties still deep. Tests applying the new "count toward the play side" idea; answer covers the risk of keeping and of killing, and the open slot. |
| §4 Rodgers second paragraph | Cut (with fn `gbdata`); one line on the free play as a plan remains. |
| §4 forward links | 02-06 down from 6 to 4, 02-05 to 1 chapter link (others now glossary anchors); "Why motion exists" has one forward pointer. |
| §4 three foul charts | The first is now about motion (see above); the cadence section keeps its two charts. |
| §4 hook never resolved | Intro promises the answer; "Back to the opening scene" paragraph after Table 1 resolves it (NZI if the tackle reacted to the linebacker, who counts as nearby over the center; false start if nobody moved). |
| §4 Eagles 2020 vs 2021 | Text and caption now name both exceptions (2020 and 2021). |
| §5 objective 3 / audible ordering | Intro now says audible is the umbrella and the other three run from least to most freedom; the kill-call bullet says how it differs from a check. New paragraph lists visible cues that the play is changing (QB calls to both sides, receivers look back, back switches sides, linemen reset, late snap); Watch-for-it bullet updated. |
| §5 Drill 1 second question | Answerable from the body now (live-ball foul, defense chooses, previous spot, replayed down); the two-minute rule is marked as a bonus. |
| §5 Drill 2 "risk of keeping" | Answer states the risk of keeping explicitly. |
| §6 offensive offside, asymmetry, defense's audibles, motion after a shift, shotgun snap trigger, who decides when to snap, NZI "obvious attempt", TE in a stance | All answered in the body: offensive offside bullet; "Why the double standard?" paragraph; defense-communication paragraph (green dot until :15, then players' checks and sideline signals); motion-after-shift sentence (rule 7-4-7); silent count rewritten as two versions plus the shotgun cue; QB decides when the cadence starts; TE on the line may slide but must stop. |
| §6 free plays per season | New number: 229 defensive-offside flags on scrimmage downs in 2025, 85 declined (fn `freeplays`, own calculation). |
| §6 play clock visibility; how refs judge an "obvious attempt" | **Declined**: no source in hand beyond the rule text already quoted; not needed for the objectives. |

### Coach findings (`01-05-coach.md`)

| Finding | Action |
|---|---|
| A1 Mike figure doesn't break the protection | Fixed with the preferred option (nickel walks down: 7 v 6). The double A-gap mug is mentioned in text as the other way to do it (07-02 link). |
| A2 pass-pro drawn as run blocks | Dotted responsibility leaders; C "M if he rushes"; back "W if he comes, else release". |
| A3 "mirror image" wrong | Text now says 2x2 becomes three receivers left (TE attached) and Z alone; strip label at the snap says the same. |
| A4 drill 2 safety on the backside | Kill-call figure now rotates the safety down on the run side (left); drill 2 rebuilt around a backside nickel, and the body teaches counting toward the play side. |
| B1 fig-shift | Tags, Y path at d ≈ −3.3, named "tight end trade", "some defenses travel, some swap names" sentence added. |
| B2 fig-legal-motion | Redrawn as above. |
| B3 fig-kill-call | Named run blocks to defenders; right DT moved to w 1.9; throw goes away from the rotated safety (to the TE in the flat); H speed-out at 2.5 yds; back pass-protects; "ball comes out before the extra man matters" in caption. |
| B4 fig-defense-moves | Rush stops in front of the set linemen; M higher; numbers dropped. |
| B5 fig-predict-free | Short-yardage defense: SS down in the box, corners at 3 yds, "short-yardage defense" in caption; answer notes the deep shot is the one this defense never allows. |
| B6 minor collisions | NZ label moved; numbers dropped in drill 2 (and drill 1). **Declined**: the "T –E straddling a hash tick" in drill 1 (cosmetic, and moving the ball off the middle shifts every alignment). |
| C1 "no coach can talk" | Now "by radio"; sideline signals still possible; new fn `radio` quotes rule 5-3-3. |
| C2 OL outweighed | Rewritten. |
| C3 hand on the ground | "Interior linemen (tackle to tackle)". |
| C4 audible order | Fixed. |
| C5 kill "usually" run/pass | Now "often"; run-to-run (flip to the light side) and pass-to-pass (man-beater/zone-beater) named; fn `kill` notes the definition is any two plays. |
| C6 terminology dialects | **Partly declined**: could not verify team-specific words ("Can" for Holmgren/Gruden, Lucky/Ringo, Liz/Rip) in a citable source in this pass, so the text keeps "or the team's own word" and fn `kill` cites a source for color-word audibles. Worth adding with a source in 04-08 (systems and languages). |
| C7 silent count mixes systems | Rewritten as two versions (center sees the cue / guard taps), line keys the ball and the center's head, snap a set count after. |
| C8 kill call changes the blocker count | Added (TE becomes a receiver; back stays in) in text and caption. |
| C9 bump | Added with the 02-06 glossary link. |
| C10 free play needs a fast snap; twelve-men free plays are tempo | Both added (body and Rodgers film room). |
| C11 tush-push coda | Added to the Eagles film room with fn `tushpush` (FACTS-current §5 sources). |
| C12 crowds loudest on third down | Added to the fouls-by-situation caption. |
| C13 Packers median vs league | Moot: that paragraph is cut. |
| C14 drill 1 clock | "8:30 left in the second quarter". |
| C15 Canadian rules | One sentence pointing to 02-06's comparison (no specific CFL claim, since 02-06's CFL source is still marked VERIFY). |

Length note: the chapter grew from about 7,950 to about 10,000 words of prose. Almost all of the growth is the
missing "whys" and rule details both reviews asked for (Table 1, the hook payoff, NZI definitions, why-hard-count,
audible cues, defensive communication); drag was cut where flagged (Rodgers stat paragraph, repeated free-play
explanation, forward-link pile-ups, the confusing motion annotations).
