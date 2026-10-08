# 12-08 beginner-reader review: "Fangio's Two-High Revolution and Macdonald's Answer"

Reviewer persona: casual NFL watcher, never played. Has read every chapter before 12-08 in
curriculum order (Parts 1–11 and 12-01…12-07), but not Part 13. Read start to finish from
`chapters/12-case-studies/12-08-two-high-to-macdonald.qmd` and the print PDF
(`pdfs/12-08-two-high-to-macdonald.pdf`, 21 pages, rasterised at 100 dpi). Line numbers are
from the .qmd; page numbers from the PDF.

**Overall:** strong and readable. The "five connected decisions" spine (each with a "what it
costs" that the next decision pays) is the best part. The double-lie strip is clear, and the
Super Bowl LX dropback grid is a figure I'd actually use. The weak spots: two print bugs,
a few numbers in the text that the table contradicts, one real conceptual gap (what exactly
makes Macdonald's *front* different from Fangio's tite, which also puts five on the line
and drops one), and a sim-pressure story that contradicts what 07-03 taught me without
saying so.

---

## 0. Print defects (fix first, visible to every reader)

1. **p. 8, Staley bullet: "(296)" renders as an ordered-list marker.** Line 803 starts with
   `` (`{python} int(tv(2020, 'LA', 'pa'))`) ``, so Pandoc reads "(296)" as list item "(296)". The
   bullet breaks in two and "and, by this book's count…" hangs under a numbered item. Rewrap so
   the line doesn't start with the parenthesis.
2. **p. 10, "The rushers" bullet: "2025." renders as an ordered-list number.** Line 877 starts
   with `2025. Seattle has them…`, which Pandoc reads as a list item numbered 2025. Rewrap.
3. Table 1 headers hyphenate badly in print: "Points al-/lowed", "EPA/drop-/back" (p. 14).
   Shorter headers ("Pts allowed", "EPA/db") or a narrower Play-caller column would fix it.
4. Big blank half-pages on pp. 1, 7 and 13. Floats get pushed to the next page. Cosmetic only.

## 1. Terms used before explained, or never explained

Most vocabulary is taught in earlier chapters (hook zone, hole zone, alley player, robber,
curl-flat, dig, hot route, two-way concept, Cover 8, motion at the snap, tempo, cadence are all
in earlier front matter). Except for "robber", though, **the body never links them**. In a
chapter this dense, a link at first use would save a trip to the glossary. Specific problems:

- **"match quarters"** (l. 415, decision 4 heading l. 639): the "match" is never explained
  here. Decision 4 describes only the read-safety rule. What does "match" add to plain
  quarters? One sentence plus a link to pattern matching (06-01/06-05) is needed, because
  "match" is in the title of a decision.
- **"two-high beaters"** (Answer 2, l. 1460): not defined anywhere I've read. Is it the same
  as a "two-way concept"? Give it a gloss or reword it.
- **"targeted coverage"** (l. 652): a new term from a named analyst, given only a half-sentence
  ("instead of rotating safeties into set zones…"). I couldn't picture the alternative it is
  being contrasted with.
- **"passing strength"** (ll. 651, 659): defined in 06-01, but in @fig-tite-quarters both sides
  have two receivers (X+H left, Y+Z right). I had to work out that the passing strength is the
  two-*detached*-receiver side. Say so: "the passing strength (the side with two wide receivers;
  here the left, where the nickel lines up)".
- **"weak rotation"** (l. 660): which safety goes where? "rotates *away* from the passing
  strength (here, the nickel's side)" reads as if the nickel's side is where it rotates *to*.
  Panel D shows the opposite: the safety on the side *away from* the nickel comes down. Reword:
  "the safety on the side away from the passing strength comes down; the other one goes to the
  middle."
- **"bust" / "busts"** (ll. 721, 930): no gloss. Easy to guess, but it's jargon.
- **"delayed identification"** (l. 592): fine in context, but put it in quotation marks as
  Donatell's phrase.
- **"sim"** (l. 878): an abbreviation used once, before the reader has been told it's short for
  simulated pressure (07-03 may have taught it, but say "a sim (simulated pressure)").
- **"[4-3]"** in the Macdonald quote (l. 885): "when we go to dime, we're really a nickel [4-3]
  team" left me confused. Dime is six DBs, nickel is five, and now 4-3? Add a sentence:
  "Emmanwori is a safety who plays like a linebacker, so a six-DB package behaves like a
  five-DB one."
- **"check"** in "let the back check one of them" (Answer 2, l. 1458): if 04-02 taught this
  it should be linked. I didn't know whether "check" meant block him or call out his name.
- **"throw hot into the A gap"** (l. 1457): throws go to receivers, not gaps. As written it
  confused me. Did you mean "don't throw hot to the receiver running into the area the Mike
  vacated"?
- **"the hole"** (fig-double-lie caption, l. 941; also l. 1260): taught in 06-01 as "hole zone", but in a
  run-heavy book "hole" also means the running lane. Link it here.

## 2. Leaps (a missing or assumed "why")

1. **What is actually different about Macdonald's front?** (biggest gap). Decision 3 (l. 631)
   says Fangio's tite already puts five on the line and drops one ("That is a small disguise in
   itself"). Then the Macdonald front bullet (l. 870) uses "We put five on the line and drop a
   guy" as his distinctive idea. As a reader I asked: isn't that the tite? The chapter also says
   Fangio is "multiple in one dimension, the coverage" (l. 864), which contradicts calling the
   tite drop a disguise. The answer is probably that Fangio drops *the same edge from the same
   spot*, so the offense learns it, while Macdonald varies *who* is on the line and *who* drops.
   Spell it out with a two-column contrast, or a small two-panel figure: same five-man line,
   with a different dropper in each.
2. **Sim-pressure story contradicts 07-03 without reconciling it.** 07-03's Ravens 2023 film
   room says Macdonald "leaned into simulated pressures" and that Alexander ranked Baltimore
   "among the league's heaviest users". 12-08 says Macdonald denies it, and the FTN proxy puts
   the 2025 Seahawks 21st, "the reverse of each coach's reputation" (l. 1236). I read both
   chapters and now don't know what to believe about the 2023 Ravens. (I ran the chapter's own
   proxy for the other seasons: BAL 2023 ranks 13th, SEA 2024 12th, PHI 2024 6th, PHI 2025 2nd.)
   Add a sentence that names 07-03, gives the 2023 Ravens' rank, and explains the gap: 2023
   Ravens vs 2025 Seahawks, eyeball charting vs FTN's `n_blitzers`, and a "pressure look" vs a
   sim.
3. **Why put the Cover 2 half toward the passing strength (Cover 8)?** (l. 650). It's called
   "the mirror image of the usual call", but I'm never told what the swap buys. One line: more
   help over the two receivers? A squatting corner against quick outs?
4. **Decision 4 has no "What it costs".** Decisions 1, 2, 3 and 5 all end with one; 4 doesn't.
   The cost (the read safety can be fooled by a blocking #2; see "Make the read safety wrong"
   at l. 1266) belongs here, so the five-decision pattern holds.
5. **Why is Super Bowl LX mostly Cover 2, not quarters?** (l. 1074). The whole chapter sells
   quarters and Cover 6, and then the showcase game is led by 16 Cover 2 snaps. Why Cover 2
   against Maye and McDaniels? One sentence on the game plan, or on what Cover 2 takes away
   that quarters doesn't (the corners sit in the flats against the quick game?).
6. **"Four rush, from two places the offense didn't expect"** (fig-double-lie caption,
   l. 941): I can find only one unexpected rusher, the Will. What is the second "place"? If it
   means the Mike not rushing from the A gap, that's a non-rush, not a place.
7. **"the Will, a player the protection had to guess about"** (l. 941): why guess? Five
   linemen plus the back is six blockers for six threats, so the Will should be someone's man.
   Explain the guess: the back is assigned to whichever linebacker comes, and the line slides
   toward the Mike.
8. **Ravens 2023 led the NFL with 60 sacks but rank 18th in pressure rate** (Table 1). A
   number-minded reader will stop here. One sentence: sacks per pressure, or different charting
   sources?
9. **Answer 3: "The offense runs, probably to the side away from the nickel"** (l. 1491): why
   that side? I would have guessed toward the side with more blockers. Give the reason.
10. **Minter is in "the Fangio tree" but "never worked for Fangio"** (l. 814). Then why is he
    in the list? Say outright that the tree is about the *idea* spreading (targeted split-field
    coverage), not about who worked for whom, or move Minter to the Macdonald section.
11. **Madden callout's last sentence** (l. 551): "That is also why a coach like Fangio is
    described as a 'play-caller' even though, before the snap, his defense looks the same"
    makes a point I couldn't follow. Isn't every coordinator a play-caller? Cut it or sharpen it.

## 3. Diagrams and captions

- **@fig-tite-quarters (p. 4):** clear. The box outline and the "six vs. six" label land.
  One snag: the thick orange line at 10 yards isn't in the "Reading the diagrams" key. A
  beginner may read it as a zone boundary. Add "orange line = first-down marker" to the key
  (it appears in every field figure).
- **@fig-one-shell (p. 6):** excellent idea, and it reads well in print. Two asks. (a) Panel C
  needs a visible split: a faint vertical line, or "Cover 2 side | quarters side" labels at
  the bottom. Right now "deep half" and "quarters" float at the top, and the squatting corner's
  short arrow is easy to miss. (b) Panel D's title "away from the $" plus the caption's "away
  from the nickel's side" still left me unsure which safety rotates (see §1, weak rotation).
  Label the SS's arrow "rotates down".
- **@fig-personnel (p. 10):** clear. The caption says what to notice.
- **@fig-double-lie strip (p. 11):** panels 1–3 work. Panel 4 is the payoff panel but it is
  the hardest to read. The Z route line, Y's go route and the brown ball path all converge on
  the ringed SS, and nothing on the panel says "dig" or "robber". Add two print-only labels:
  "dig (Z)" at the catch point and "robber (SS)". Also, panel 3 shows the W already past the
  line at +1.1 s but has no "W rushes" label. The caption puts the Will at "four yards" and
  Drill 2's caption puts him at "three yards" (l. 1435). Pick one.
- **@fig-lx (p. 12):** a great figure, but **Q4 has two "I" marks and the text explains only
  one** (Nwosu's pick-six on a five-man rush, l. 1086). The other is Julian Love's, which
  appears only later as a charting caveat (l. 1227). Mention both in the scoreboard bullet.
  Say what the first Q4 "T" was too, and why Q4 has 26 dropbacks against 8–11 in the other
  quarters (no-huddle catch-up). The hook also says "Seattle almost never sent more than four"
  (l. 407), but the grid shows 3 of 8 Q1 dropbacks with 5+ rushers, and 8 of 53 overall.
  "Rarely" or "on about one dropback in seven" would be honest.
- **Table 1 (p. 14):** pattern 2 claims "the best of them stopped the run anyway", but **the
  table has no run-defense column**, so I can't check the claim. Add EPA per designed run (the
  chapter already computes `run_epa_rk`). Pattern 1 says "The pressure rates are good but not
  extreme", but four of the seven rank 17th–18th, which is the league median, not good.
  Reword it to something like "around the league middle, despite rarely blitzing".
- **@fig-scatter (p. 15):** readable. The caption says the named teams have "pressure rates
  around or above the league's middle", but BAL '23 sits visibly below the dashed median.
  SEA '24 is plotted, but the 2024 Seahawks are never discussed in the text.
- **@fig-staffs (p. 17):** readable, but see §4.
- **Drill figures (pp. 18–19):** clean. In Drill 2 the Mike's green ring touches the T box
  beside him, a near-collision. The caption says Mike is one of "five on the line", but he's
  drawn about 2 yards off it.

## 4. Drag and repetition

- **The "You'll need" box is ~400 words and 8 bullets** (ll. 426–487) before any new idea.
  Most of it is legitimately needed, but the "Reading the diagrams" key could move to just
  above @fig-tite-quarters, where it's used, and the personnel/EPA bullets could shrink to one
  line each.
- **"The coverage charts measure what was played, not what was shown"** appears four times:
  l. 726, pattern 3 (l. 1135), "What the data can't see" (l. 1183), and the Takeaways. Twice is
  enough: set it up at decision 5, then pay it off in the data section.
- **The opening problem section** (ll. 489–517) retells 11-05 ("eighth man", McVay/Shanahan
  play-action, Mahomes deep). It's short and it frames the chapter, so keep it, but the
  three-point "the fix had to do three things" list is the new value. Trim the retelling to two
  sentences.
- **Fangio bio "forty years in the room" vs "thirty years"**: the heading says forty (l. 519),
  the text says "Vic Fangio spent thirty years working out how" (l. 516) and "three decades as a
  coordinator" (l. 527). Make it consistent, or make the difference obviously deliberate.
- **The tree section lists names without payoffs.** Donatell (l. 807), Barry (l. 811) and Desai
  (l. 812) get careers but no results. Desai's 2023 Eagles, ranked 30th in scoring, are the
  defense Fangio inherited, and that is a perfect example of the thesis that the same system
  gives very different outcomes. Use it, or cut the names that carry no lesson.
- **"Staffs entering 2026"** (ll. 1287–1336) drifts: half the table is offensive coordinators
  and a Raiders head coach, in a defensive case study. The Seattle-OC point (that the run game
  kept the defense fresh) is interesting but isn't argued anywhere else in the chapter. Cut the
  table to the defensive rows plus Seattle's OC, or fold it into one paragraph.

## 5. Can I do the "You'll be able to…" items? Drills attempted before opening the answers

| Item | Verdict |
|---|---|
| Five connected decisions, buys and costs | **Yes**, the best-taught item. Weakened by decision 4 having no cost and by "match" never being explained. |
| Trace the tree and why results varied | **Partly.** I can name the people. The "why" ("outcomes are set by the front four and the safeties") is asserted from two examples (2020 Rams, 2024 Panthers) with no players named for the bad side. Who was Carolina missing in 2024? |
| Explain multiplicity | **Mostly.** I can recite the four dimensions, but I can't tell how Macdonald's front differs from the tite (see §2.1). |
| Break down SB LX play by play | **Partly.** The grid lets me describe the game, but "play by play" oversells it. Only two plays are narrated (Witherspoon's sack and Nwosu's pick-six), and the second interception is unexplained. One or two drawn plays from the game (even simulated, from the charted labels) would deliver this. |
| Compare the philosophies with numbers | **Yes, with caveats.** The table can't support the run-defense claim, and the pressure wording overstates. |
| Predict offensive moves and run a disguise audit | **Yes.** The audit is concrete and doable. It would be better with one worked example row ("Q: two-high, M in A gap → after: one-high, 4 rushed, M dropped → RP"). |

**Drill 1 (six vs. six).** My answer before opening: "Don't run inside zone into the tite. Run
outside to the tight-end side and make the safety tackle in space, or use play-action because
the safety reads Y." The defense is counting on the 4is and nose holding, and on the safeties
tackling. **Matched the answer**, including the play-action trap. I didn't think of adding a
seventh blocker with motion; that was a useful addition.

**Drill 2 (crowded line).** My answer: "Four rush, one of M or W drops. Don't panic-throw hot,
read the safeties after the snap." **Matched.** But the answer's protection advice ("set the
protection to the two linebackers, let the back check one") went past what the chapter taught
me. The double lie said the protection "had to account for six", and I didn't know how that
plays out with six blockers. The "two-high beaters" in the answer are undefined.

**Drill 3 (heavy answer).** My answer: "Offense has 7 blockers vs 6. Defense can stay and give
up yards, drop a safety and become one-high (play-action risk), or fit a safety late." **Matched
all three.** Two snags in the answer: "to the side away from the nickel" has no reason given,
and the last line ("three safeties, one of whom is really a linebacker in a safety's spot")
reads backward. The big nickel is a *safety* who plays *linebacker* (l. 883–885), so it should
be "a safety who can be a linebacker".

The drills were fair and the body prepared me for them. They're slightly *too* easy for a level-5
case study: all three are about box counts and "rush four". None asks me to tell Fangio from
Macdonald from a picture. A fourth drill, "Two pre-snap pictures from two defenses: which is
the Fangio defense and which is the Macdonald defense, and what would you watch for at the
snap?", would test the chapter's actual thesis.

## 6. Knowledge gaps: what I still wonder

1. **How do eleven players run "one picture, many plays" without busting?** How does the call
   get in, who adjusts to motion, and how much is called vs. checked at the line? The chapter
   says the cost is "complexity… when communication fails, the busts are spectacular" but
   shows none. One known bust from a Macdonald or Fangio defense would make the cost real.
2. **What changed between Seattle 2024 and 2025?** SEA '24 is plotted, the NYT "tweaks" piece
   is cited, and Love's Week 14 return lines up with the jump to 54.8% split-safety, but the
   chapter never tells the year-one-to-year-two story. That's the most natural "how he built
   it" thread for a case study.
3. **Why did Denver's Fangio defenses only rank 14th–18th?** Which pieces were missing? This
   would strengthen the "players decide outcomes" thesis.
4. **What does Fangio's tite do against 12 personnel?** Drill 3 switches to a four-man line with
   two linebackers, with no word on whether that's what Fangio would actually play or why the
   tite isn't used.
5. **What does a defensive coordinator do when the head coach calls the defense?** (Durde
   under Macdonald.)
6. **How are Fangio and Macdonald each doing *now* (October 2026)?** The chapter is dated "as
   of the start of the 2026 season". A one-line hedge would cover it.
7. **What's a "good" pre-snap lie rate?** The audit gives Evero's Carolina at ~50% rotation.
   What would I expect from Seattle, given ~93% two-high shown (65/70) vs 52% two-high played?
   The chapter has the two numbers to make a back-of-envelope estimate and doesn't.
8. **EPA scale in the Super Bowl bullet:** "−0.67 EPA per dropback" has no anchor. Point to the
   league median in Table 1 (+0.05) so I know −0.67 is catastrophic.

## Top fixes, in priority order

1. Fix the two list-marker print bugs (ll. 803, 877).
2. Sharpen Fangio-front vs Macdonald-front (§2.1), and reconcile the sim-pressure story with
   07-03 (§2.2).
3. Explain both Super Bowl LX interceptions and fix "almost never sent more than four"; add an
   EPA anchor.
4. Add a run-defense column to Table 1 and fix the "pressure rates are good" wording.
5. Add a "What it costs" to decision 4, a sentence on "match", and the "why" for Cover 8 and
   for Cover 2 in the Super Bowl.
6. Add "dig"/"robber" labels to double-lie panel 4, mark the split in fig-one-shell panel C,
   and add the first-down line to the diagram key.
7. Trim the repetition ("played, not shown" ×4), the staff table, and the name-only tree bullets.
8. Consider a fourth drill: tell Fangio from Macdonald from the pre-snap picture.

---

## Revision (2026-10-08)

Covers both this review and `12-08-coach.md`. The fact-check results are unchanged; every new claim is
either a course calculation done inline in the chapter's data cell or footnoted. Rebuilt with
`build_pdfs.py 12-08-two-high-to-macdonald --html` (OK, 25 pp.), and every figure page was re-checked at 110–150 dpi.

### Beginner review

| Finding | Action |
|---|---|
| §0.1 "(296)" list marker (Staley) | Reflowed. A new instance found in the rewritten Minter bullet ("301." at a line start) also fixed; every line starting with an inline value was audited |
| §0.2 "2025." list marker | Reflowed ("November 2025." no longer starts a line) |
| §0.3 Table headers hyphenate | Headers now "Pts", "EPA/db", "Run EPA", "Caller"; abbreviations explained in the caption |
| §0.4 Blank half-pages | **Declined (cosmetic):** they come from Typst float placement of large figures; fixing them would mean hand-placing floats per page, and the layout changes whenever text changes |
| §1 Terms not linked | Linked at first body use: four-man rush, alley player, pattern matching, passing strength (06-01), cloud, MOFO/MOFC, creeper, two-way concept, hole zone, tempo, RPO, hot route, check-release, curl-flat, dig, green dot, 2-4-5 |
| "match quarters" never explained | New paragraph in decision 4 on what "match" (pattern matching) adds |
| "two-high beaters" | Removed; reworded as "the throws that beat two-high" / "a route combination that beats two-high", with a two-way concept link |
| "targeted coverage" | Now contrasted explicitly with fixed-zone rotation ("decides, call by call, which side gets the Cover 2 help") |
| "passing strength" | Defined in place: "the side with more wide receivers: in Figure 1 the left, where the nickel lines up" |
| "weak rotation" ambiguous | Reworded: "the safety on the side away from the passing strength comes down, and the other one runs to the middle"; panel D retitled, given a "rotates down" leader, and its caption explains which safety |
| "bust" | Glossed at first use (decision 5) |
| "delayed identification" | Now in quotation marks as Donatell's phrase |
| "sim" | Glossed: "a sim (simulated pressure)" |
| "[4-3]" quote | Decoded after the quote: Emmanwori plays like a linebacker, so a six-DB package behaves like a five-DB one |
| "check" (Drill 2) | Replaced with a linked check-release and a plain description |
| "throw hot into the A gap" | Now "don't throw hot to the short middle the Mike appears to vacate" |
| "the hole" | Glossed and linked (hole zone) in "How offenses responded"; the double-lie caption says "the hole, the short middle at about 10 yards" |
| §2.1 Fangio front vs Macdonald front | Decision 3 now says the tite drop is "small but readable: the same five players in the same spots"; the front bullet in Multiplicity spells out the contrast (Macdonald changes *who* is on the line); new 4-panel **fig-fronts** (Fangio 2-4-5 nickel, Fangio tite with the TE-side edge dropping, Macdonald mugged Mike, Macdonald safety on the line); "multiple in one dimension" → "multiple mainly in one dimension"; new takeaway line |
| §2.2 Sim story contradicts 07-03 | New paragraph in "What the data can't see": the 2023 Ravens rank 13th on the same proxy (computed inline); 07-03's ranking was PFF charting through Week 6 of 2023 (via Alexander); much of the reputation is pressure *looks*. Pointer added in the rushers bullet. 07-03's own footnote already notes the proxy gap |
| §2.3 Why Cover 8 | Decision 4: the flip puts the cloud corner and half-field safety on the two-receiver side (quick outs and hitches) and keeps the quarters read on the TE/run-strength side |
| §2.4 Decision 4 lacks a cost | Added "What it costs": the read rule can be used against him (play-action, RPOs), and the run help arrives late. "How offenses responded" now points back to it |
| §2.5 Why Cover 2 in SB LX | Computed: 10 of the 16 Cover 2 snaps were in the fourth quarter against the hurry-up with a lead; the bullet explains what Cover 2 buys there |
| §2.6 "two places" | Caption rewritten per the coach: "one of them (W) a player the protection had to guess about, and two of the six it counted (M, E) are in coverage" |
| §2.7 Why the Will was a guess | "Count the lies" now walks through the protection: the line takes the five on it, the back has the Will, nobody knows whether he's coming, so the back stays in and four receivers face seven |
| §2.8 60 sacks vs 18th pressure | Ravens film room: pressure ranked 18th, but Baltimore converted pressures to sacks at the 2nd-highest rate (computed inline) |
| §2.9 Drill 3 "away from the nickel" | Reason given (the nickel is a seventh defender close enough to fit on his side) |
| §2.10 Minter in the tree | Tree reframed as "who took the *idea*"; Minter introduced as "the branch that shows the idea traveling without the man" |
| §2.11 Madden callout last sentence | Cut |
| §3 Key lacks the first-down line | Key now explains the blue line of scrimmage and the yellow-orange first-down line, plus S (third safety) and the purple ring |
| §3 fig-one-shell C/D | Panel C has a dashed split line and "Cover 2 side / quarters side" labels; panel D has a "rotates down" leader and a clearer title |
| §3 Double-lie panel 4 / panel 3 | Print-only labels "dig (Z)", "robber (SS)" (panel 4) and "W rushes" (panel 3), with leaders aimed at each player's computed position; the Will is "about three and a half yards" in both the double lie and Drill 2 |
| §3 fig-lx: two I's, first T, 28 vs 7–10 dropbacks, "almost never sent more than four" | Scoreboard bullet names all four Q4 marks (Hollins TD vs Cover 6, Love INT, Nwosu pick-six, Stevenson TD) and explains the long Q4 row (no-huddle share computed); hook now "more than four rushers on only 8 of 53 dropbacks" (inline) |
| §3 EPA anchor | Scoreboard bullet compares −0.67 with the 2025 median defense (+0.05) |
| §3 Table: no run-defense column; "pressure rates are good" | Run EPA column added; pattern 1 now gives the computed rank range (4th–18th) and says "top of the league to its middle"; pattern 2 cites the Run EPA column (6 of 7 in the top ten, computed) |
| §3 Scatter caption | Says BAL '23 sits below the median and why; SEA '24 is now discussed (year-one-to-year-two paragraph) |
| §3 Drill 2 ring touches T; Mike "on the line" | Mike moved to 2 yards off the ball (mugged); Drill 2 rings only the Will; caption says "walked up into the left A gap about two yards off the ball" |
| §4 "You'll need" box ~400 words | Diagram key moved to just above Figure 1; tracking-figure aside, personnel and EPA bullets shortened |
| §4 "played, not shown" ×4 | Now twice: set up in decision 5, paid off in pattern 3 |
| §4 Opening problem retells 11-05 | Retelling cut to two sentences; the three-point list kept |
| §4 Forty vs thirty years | Heading "four decades in the room" (1979–2026); text "most of a long career" and "more than twenty years as a coordinator" (1995–2018 minus the Ravens assistant years) |
| §4 Tree names without payoffs | Every name now carries a result (computed points-allowed ranks): Staley's Chargers, Donatell's 2022 Vikings, Barry's Packers, Desai's 2021 Bears and 2023 Eagles (30th, the defense Fangio inherited) |
| §4 Staff table drifts | Cut to defensive rows plus Seattle's OC; Raiders and Eagles-OC rows and Patriots DC removed; Kubiak's move mentioned in the caption |
| §5 Who was Carolina missing in 2024? | Derrick Brown (Week 1 knee) and Shaq Thompson (Week 4 Achilles), sourced (CBS Sports, WBTV/AP); Carolina 32nd in pressure and run EPA; rebound to 15th in 2025 with Brown back (participation confirms his 2025 snaps) |
| §5 "Play by play" oversells | Objective and section heading now "dropback by dropback". **Declined:** drawing actual SB LX plays, because no tracking data exists for the game and drawing specific plays from charted labels alone would invent alignments |
| §5 Audit worked example | Added a worked row |
| §5 Fourth drill | Added Drill 4, "whose defense is it?" (two pre-snap pictures, Fangio 2-4-5 vs Macdonald mug + third safety), with an answer |
| §6.1 How the call gets in / busts | "Why it exists" callout now covers the green-dot radio, adjusting to motion, and a concrete description of a bust. **Declined:** a named real bust, because none was verified |
| §6.2 SEA 2024 → 2025 | New paragraph: big-nickel share 6% → 56% (computed), ranks 11th → 1st in points, Love's Week 14 return (NGS) |
| §6.3 Why Denver ranked 14th–18th | Added Denver's computed pressure ranks (31st, 25th, 19th): the four-man rush rarely got home |
| §6.4 Tite vs 12 personnel | Drill 3 answer now includes "Match the personnel: sub to base (a third linebacker, or Fangio's 3-4 tite)" |
| §6.5 What a DC does under a play-calling HC | **Declined:** 07-03 (which cites a Yakima Herald profile of Durde) owns that detail, and nothing here was verified beyond it |
| §6.6 How are they doing now | One-line hedge in "Staffs entering 2026" (numbers stop at the end of 2025; the 2026 season is under way) |
| §6.7 Good lie rate | Back-of-envelope added: ~90% shown two-high vs 52% played → rotated out on at least ~38% of dropbacks (inline), labelled as an estimate |
| §6.8 EPA anchor | Done (see §3) |

### Coach review

| Finding | Action |
|---|---|
| 1. 2018 Bears nickel had two ILBs | Verified in data: both Trevathan and Smith were on the field for 80% of Chicago's 2018 nickel snaps, Baun and Dean for 84% of Philadelphia's 2024 snaps (computed inline from participation + rosters). Film room rewritten; decision 2 gains a paragraph on the 2-4-5 everyday nickel; Figure 1 caption relabelled truthfully (five-man nickel tite = Fangio's base front, Staley's everyday nickel, sourced to MatchQuarters via 05-03); 2-4-5 drawn in fig-fronts panel A |
| 2. "The box stayed light" contradicts 4 of 13 | Bullet retitled "The run never mattered"; 9 of 13 runs met 7+ in the box (computed) |
| 3. Drill 3 misses "let the reads do it" | Answer rewritten: "Let the reads do it" (8 fitters after the snap) first, then match personnel (base 29.7%), safety down pre-snap, rotate at the snap |
| 4. Double-lie seam wide open | Edge now walls Y (drop to (10, 8.6)); FS shades to (17.5, 3.0); Y stops at 16.5; caption says the edge carries Y until the FS takes him; SS moved slightly inside so the rings don't touch |
| 5. Quarters safeties drawn bailing | Figure 1 and fig-one-shell B/C: safeties now take a short 2.5-yard read step, with the deep quarters shaded separately; caption explains the flat-footed read; "safeties read #2" tag in panel B |
| 6. "No free blockers" overstated | Reworded: the guards are uncovered on paper but kept busy helping on the nose and 4is |
| 7. Cover 6 / Cover 8 stated two ways | One statement in decision 4 (Cover 6 = half away from passing strength, Cover 8 = toward); the box defers to it; dialect note added. **For the 06-01 owner:** its Cover 8 glossary line ("what most teams call Cover 6") is consistent but loose; the coach suggests noting Fangio's two names |
| 8. Strength dialect in panel D | Clause added to the fig-one-shell caption |
| 9. Drill 2 hot-throw wording; attack the dropper | Reworded, and "Attack the dropper" added as its own step |
| 10. Double-lie smaller items | Caption reworded; the Will stops at (−2.6, 2.4) and the back at (−3.3, 2.5) so the pickup is visible; Mike at 2 yards off the ball (double lie, Drill 2, Drill 4, fig-fronts); corners at 8.5 so they clear the first-down line |
| 11. "Dime" not necessarily three safeties | Checked: every Seattle 2025 dime snap had 3+ safeties; caption now gives big nickel (>half) and dime (~1 in 6) separately and the league's three-safety share (~a quarter) |
| Nice: creeper | Decision 3 clause with link |
| Nice: corners 7–9 off, outside leverage | In the Figure 1 caption |
| Nice: MOFO/MOFC | Decision 5, linked |
| Nice: audit timing | Column 1 now charted at the snap, with the pre-snap spin explained |
| Nice: Drill 1 motion caveat + 05-03 link | Added |
| Nice: Drill 3 nickel walk-down | **Declined:** the revised answer doesn't count the nickel as a fitter, so the apex alignment stands |
| Nice: big nickel tie-in | Double-lie caption: "The nickel ($) could just as well be Seattle's third safety" |
| Rendering bug ("2025.") | Fixed (see §0.2) |

**Not changed:** `gridiron/` (all new drawing is inside the chapter). The chapter grew from ~9,200 to ~11,400
prose words, mostly from the new figure, Drill 4, and the reconciliations the reviews asked for.
