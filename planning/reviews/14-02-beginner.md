# 14-02 Scheme and Fantasy: beginner-reader review

Reviewer persona: casual NFL watcher, never played, has read Parts 1-13 and 14-01 in order. Read the
rendered PDF (`pdfs/14-02-scheme-and-fantasy.pdf`, 17 pages) start to finish, plus the .qmd for exact
wording. Overall: strong, data-rich and mostly easy to follow. The usage → volume → format → coordinator
arc works, and the coordinator cards (Fig 8) are the best thing in the chapter. The biggest problems are
**fantasy basics the chapter assumes I already know**, **one internal contradiction about whether a
play-caller moves target share**, **an unresolved tension with 14-01's positional value**, and **no
method for forecasting game script** (betting lines). Predict-the-play 1 is spoiled by the body text.

## 1. Terms used before they're explained, or never explained

| Where | Quote | Problem |
|---|---|---|
| Hook (p1) | "the tight end you drafted in the sixth round", "a waiver-wire must, your tight end a bust" | The chapter never explains how a fantasy league works: draft rounds, league size, weekly starting lineup (QB/2 RB/2-3 WR/TE/flex/K/DST), the waiver wire. I've never played fantasy. One short "How a fantasy league works" box near the top would fix this and much of §6. |
| Film room, Barkley (p7) | "his consensus half-PPR average draft position was about the 17th pick" | Uses **half-PPR** and **average draft position** two sections before they're defined (Scoring formats, ADP). Needs a forward gloss and link, or move the ADP sentence. Also "17th pick": is that good or bad? I don't know that it means early second round in a 12-team league. |
| Answer 2 (p16) | "barely rosterable", "a weekly starter" | Fantasy jargon, never defined (depends on the lineup-slot explanation above). |
| RB list (p5) | "A true 'bell cow'" | Quoted slang, explained only by context. Fine, but give the gloss outright ("one back who plays nearly every down"). |
| Target share (p4) | "the true 'alpha' receivers" | Same: slang with no definition. |
| p6, p11 | "between the 20s" | Broadcast slang (the field between the two 20-yard lines), never glossed. |
| Answer 2 | "a third-down throw short of the sticks" | "the sticks" (the line to gain) is never glossed here. 01-02 owns *line to gain*, so link it. |
| Fig 8 axis (p12) | "neutral PROE (points)" | In a fantasy chapter "points" reads as *fantasy points*. Write "percentage points". |
| Detroit card text (p13) | "the Lions trailed by about four points per play on average" | Hard to parse. It sounds like a rate. I think it means "the average score differential across their plays was about −4". |
| Fig 5 caption | "the average of nflverse's pass_oe" | Code column name in a caption. Fine in the code notes, odd in prose. |
| Go deeper (p16), fn 5 | "WOPR, RACR" | RACR is never defined. Either define it in one line or drop it. |
| Fig 8 caption, misconception (p12-13) | "±2 standard errors", "a standard error of about 4 percentage points" | Taught in Part 13, but not in the "You'll need" box. Add a one-line recap ("the typical size of sampling noise"), because the whole card reading depends on it. |
| Answer 2 | "the slot receivers (H and Y on the trips side)" | In the figure Y is the gold-ringed **tight end attached to the line**, not a slot receiver. That contradicts the diagram and the chapter's own colour key. |
| Fig 2 caption | "Y runs up the seam" | Seam isn't linked (04-01 owns it). It's minor because Part 4 taught it. |

Owned terms (route participation, target share, air-yards share, WOPR, YPRR, snap share, red-zone share,
game script, pace, PPR, ADP) are all defined clearly at or near first use. The early mentions in the "You'll
be able to" list and the chain paragraph are fine.

## 2. Leaps: a missing or assumed "why"

1. **Contradiction about target share and the play-caller.** p4: target share "is set mostly by design. A
   play-caller who builds his passing game around one receiver gives that receiver the first read". p8,
   after the volume equation: "A coordinator change can move every term except the last one [target share]
   at a stroke." Then the Detroit card shows Petzing moving the *TE* target share from 17% to 23%, and
   Answer 3 says to raise the forecast if the share goes above 28-30%, "meaning the play-caller is building
   the passing game around him." Which is it? I *think* the intended distinction is: a clear WR1's share
   among his team's receivers travels, but how targets split *by position* (TE/RB/WR) is the play-caller's
   fingerprint. The chapter needs to say that explicitly. As written, the key equation sentence is wrong.
2. **Positional value is set up and never paid off.** The "You'll need" box reminds me that in 14-01
   "running backs and tight ends sit near the bottom of the real-football market", and says "this chapter
   borrows all three ideas". It never comes back to that. My obvious question: *why are running backs among
   the most expensive fantasy players when NFL teams treat them as cheap?* The answer (fantasy scores
   touches and touchdowns, and replacement level/scarcity by lineup slot) is the fantasy version of
   positional value, and it's exactly what makes ADP a cross-position market. Without it, "ADP as a market
   price" stays abstract.
3. **Fig 1 overstates the usage vs. efficiency gap.** The text says "the efficiency numbers sit lower:
   yards per target is down near 0.45". On the chart, receiving yards per game (0.62) and catch rate (0.59)
   sit almost level with target share and WOPR (0.64). Only YPT and touchdowns are clearly lower. With n = 78
   the noise is roughly ±0.08, so 0.64 vs 0.62 is no difference at all. Yards per game is also volume times
   efficiency, so calling it "efficiency" is questionable. An analytical reader will push back. Say
   "touchdowns and per-target efficiency are the unstable ones", and note the sample only includes players
   who kept a 50-target role both years (survivors).
4. **Why WOPR, if it's no stickier than target share?** Fig 1 gives WOPR 0.64 and target share 0.64.
   The text says WOPR's weights "come from fitting the two shares to receivers' fantasy production" (no
   source for that claim). So what does WOPR add, predicting *points* rather than *itself*? One sentence would
   answer it.
5. **The neutral filter vs. score effects (Detroit, p13).** "trailing pulls even neutral-situation calls
   toward the pass". I was taught in 13-04 that the neutral filter exists to remove the score. Explain the
   gap: win probability of 20-80% still includes being down a touchdown, and xpass already adjusts for score,
   so why is there residual pull?
6. **Barkley's price compares apples to oranges.** p11: "Barkley in 2024, taken around the 17th pick and
   finishing first in standard scoring, was a bargain." The 17th *overall* pick is compared with *first
   among RBs*. What was his positional ADP (RB-what)? The "5th running back taken who finishes 5th" example
   right before it uses positional ranks, so stay consistent.
7. **"ADP ... overreacts to last season's box scores"** (p10). That claim is asserted without one example.
   A touchdown-fluke player drafted too high the next year would tie ADP back to Fig 1.
8. **Game-script misconception (p9)** reads muddled. It opens "Over a season, mostly yes" and then
   introduces "soft coverage to protect a lead" (prevent defense, never named or linked). The useful point
   (taste vs. fate) is in the last sentence. Lead with it.
9. **Fig 6 oddity.** The 4th-quarter line *drops* from about 86% at −18 to about 74% at −21. Why do teams
   down three scores throw less? Garbage-time backups? Giving up? The caption should say, or cap the chart
   at −18.
10. **Puka Nacua in Fig 3.** The text says he and Smith-Njigba "sit alone at the top", but Nacua's dot sits
    right on the median-participation line (about 79%), visually in the "efficient part-timer" half. Why was
    a star WR1 on the field for only about 79% of dropbacks? Missed games, or an artefact of the estimate?
    Explain it or he undermines the quadrant reading.
11. **Answer 1 vs. the definition of red-zone share.** By the glossary definition (carries + targets inside
    the 20), a QB sneak *lowers* the RB's red-zone share. The answer says instead that it makes the RB's
    red-zone share "overstate his touchdown chances". Both can be true, but say it in that order: it takes
    the shortest carries off him, so his remaining red-zone chances are longer and convert less.

## 3. Diagrams and captions

- **Fig 2 (one snap, two jobs):** clear and the best teaching diagram here. Minor: in the left panel the
  "U: snap and a route" label sits low-left, closer to X than to U. A short pointer to U would help. The
  footer "On the field: 11 · eligible: 5" is a nice touch.
- **Fig 3 (route participation vs YPRR):** decodable. Parker Washington is labelled but never mentioned.
  Either use him or drop the label. Nacua: see leap 10. The bottom-left quadrant is unnamed. It's fine,
  but I wondered what it means (part-time and unproductive: the waiver fodder).
- **Fig 4 (goal line):** the Seattle panel shows chances but not touchdowns, while the Philadelphia panel
  shows touchdowns. Adding a "rushing TDs" pair (Walker 5, Charbonnet 12) to the Seattle panel would let
  the picture make the point the text makes.
- **Fig 5 (share vs PROE):** clear. The caption says what to notice. Good.
- **Fig 6 (game script):** clear, except for the −21 dip (leap 9).
- **Fig 7 (formats):** readable with the legend. It floats under the "ADP" heading in print, away from the
  PPR text that discusses it. Four of the ten players (Henry, Charbonnet, Jefferson, Higgins) are never
  discussed. Jefferson 30 → 21 especially makes me wonder what happened to him. Charbonnet 20 → 24 is a
  missed callback to the Seattle goal-line story: he's a touchdown-dependent back who falls in PPR.
- **Fig 8 (coordinator cards):** dense but decodable thanks to the "read across a card" caption. Two
  things the text skips: Detroit's **under-center** dot moved *away* from Petzing's diamond (about 46% vs
  about 27%) and is never mentioned. The narrative only cites moves toward the fingerprint, and I'd like the
  counter-example acknowledged. The KC TE-share row shows no grey dot (it's hidden behind the blue). Say so
  or offset it.
- **Fig 9 (Predict 1):** clear. The "goal line" label is squeezed between the gold line and the C box but
  readable.
- **Fig 10 (Predict 2):** clear. B's ring touches Q. Separate them a little.
- **Print layout:** p6 is half blank, p14 (Predict 1 alone) is two-thirds blank, and p17 is almost
  entirely blank. Typst float placement is worth a look.

## 4. Drag and repetition

- The Barkley/Hurts inside-the-2 numbers (18 vs 6 chances, 11 vs 2 TDs) appear **three times**: the Fig 4
  caption, the film room and Answer 1. Keep them in the film room and point back to it.
- "Four games is a small sample" appears five times (method step 5, the Fig 8 caption, the LAC paragraph,
  the Detroit paragraph, the misconception callout). The callout is the right home. Trim the others.
- The "You'll need" box is long (four dense bullets, about 180 words). It's acceptable for Level 3, but the
  participation/FTN detail ("2016-2025; the current season arrives only after it ends") belongs in the
  code note.
- The opening hook (the 52-snap tight end, the 14-snap backup who scored twice) is **never resolved**. A
  two-sentence callback in the TE or goal-line section ("your tight end was a blocker, so check his route
  participation; the backup has the inside-the-5 job, so check whether it's his role") would close the loop
  satisfyingly.

## 5. Can I do the "You'll be able to…" items? (drills attempted before opening answers)

- **Predict 1 (first-and-goal at the 1):** I said "QB sneak / tush push; it takes the TD away from the
  RB." **Correct, but no work required.** The film room two pages earlier told me exactly this with the same
  stats. Either make it a different team or situation (e.g. a back who *is* the goal-line back, so the
  reader has to read the personnel), or ask a harder question (what does this do to the *QB's* fantasy value?).
- **Predict 2 (third-and-8, down 10):** I said "pass; B is the passing-down back, PPR-valuable, A is a
  game-script/early-down back." **Correct.** The caption carries most of it (it tells me A had 18 carries
  and 1 catch). "Who on the offense is likely to touch the ball" was too open: I answered "B or a slot
  receiver" and the answer accepted roughly that. The H/Y "slot receivers" error confused me (see §1).
- **Predict 3 (receiver changes teams):** I said 0.25 × 27 ≈ 6.75, so about 7. **Correct, trivially.** The
  prompt hands me targets per game, so the plays, PROE and pace numbers are decoration, and I never used the
  volume equation the chapter built. A better drill would give plays, PROE (or pass rate) and target rate
  and make me compute targets.
- **Skill 1 (receiver usage, which stats carry over):** yes, with the Fig 1 caveat above.
- **Skill 2 (RB role, TE in 12 personnel, goal-line role):** RB yes. TE only partly: the TE section has no
  data example of a TE's route participation (e.g. McBride's or LaPorta's), only the target-share figure.
  I can state the rule but have never seen a real number.
- **Skill 3 (forecast volume from PROE, pace, game script):** PROE yes, pace roughly. **Game script no:**
  the chapter tells me game script matters but never how to *forecast* it before a game or season. The
  standard tool is betting lines (point spread, implied team total, season win totals), and it isn't
  mentioned.
- **Skill 4 (formats and ADP):** formats yes. ADP only as a metaphor: I couldn't use positional vs.
  overall ADP or say what "value" at a pick means across positions (leap 2, 6).
- **Skill 5 (coordinator change):** yes. The 5-step method and the cards are excellent. But the worked
  examples never name the *loser* on any team (the Watch-for-it asks me to "name the player who gains most
  and the one who loses most"). LAC: which receiver is hurt? DET: does St. Brown or Williams lose share to
  LaPorta? Model it once.

## 6. Knowledge gaps: what I still wonder

1. How does a fantasy league actually work: roster slots, flex, weekly lineups, waivers? Why does a TE go in
   the sixth round?
2. Why are RBs expensive in fantasy and cheap in the NFL (replacement level, scarcity)? This is the bridge
   from 14-01.
3. **Quarterbacks.** The chapter never discusses fantasy QB usage. Hurts' tush-push touchdowns are framed
   only as a loss for Barkley, but they're a huge *gain* for the fantasy QB: rushing QBs and goal-line
   sneaks. Even one paragraph would help.
4. How do I forecast game script? Point spreads and implied totals.
5. **Vacated targets:** when a receiver leaves, where do his targets go? (Detroit shows this for carries
   with Montgomery. Is there a target version?)
6. How many weeks before a *player's* target share or route participation is trustworthy in-season? The
   chapter gives this for team PROE (SE of about 4 points after 4 games) but not for player shares.
7. Does a quarterback change (not a coordinator) move receiver value the same way?
8. Where can I get real snap counts and route data for free? `load_snap_counts()` is used in code but not
   pointed to in prose. Routes are paid (PFF/FTN), which is said.
9. Half-PPR is explained in words but never shown. Where do players land in Fig 7 under half-PPR? Is it
   simply halfway?

## Priority fixes

1. Resolve the target-share contradiction (p8 equation sentence vs. p4, the Detroit card and Answer 3).
2. Add a short "How fantasy works" box (lineup slots, draft rounds, waivers, ADP overall vs positional) and
   a paragraph on why fantasy RBs are pricey when NFL RBs are cheap.
3. Add how to forecast game script (betting lines).
4. Rework Predict 1 (spoiled) and Predict 3 (one multiplication). Fix "H and Y ... slot receivers".
5. Soften the Fig 1 usage-vs-efficiency claim, and explain why WOPR adds anything.
6. Forward-gloss half-PPR and ADP in the Barkley film room. Make "neutral PROE (points)" read "percentage
   points".
7. Cut the repeated Barkley inside-the-2 stats and "four games is small" lines. Call back to the hook.

## Revision (2026-10-08)

Covers this review and `14-02-coach.md`. Fact-check claims are unchanged; every new number is a course
calculation (footnoted with filters) or a new sourced footnote. Rebuilt with `build_pdfs.py --html` (OK, zero
errors), 21 pages, every figure re-inspected at 60 and 120-130 dpi.

### Beginner review

| Finding | Action |
|---|---|
| §1 no fantasy basics (draft, lineup, waivers, rosterable, weekly starter) | New callout "How a fantasy league works" after the You'll-need box: snake draft, ESPN default lineup (sourced, 4for4), flex, waiver wire (linked to 14-01's NFL waivers), RB1/WR2 shorthand, rosterable, weekly starter |
| §1 half-PPR / ADP used before definition; "17th pick" meaningless | Film room glosses ADP and half-PPR with a link forward; adds "middle of the second round ... sixth running back off the board" (RB6 from the same FanDuel source, footnote updated) |
| §1 bell cow, alpha, between the 20s | Each glossed inline |
| §1 "the sticks" | Answer now says "just past the line to gain", linked to 01-02's glossary |
| §1 "neutral PROE (points)" | Axis now "percentage points"; caption says so too |
| §1 Detroit "trailed by about four points per play" | Rewritten ("trailed on an average snap by about four points") and the interpretation corrected (see leap 5) |
| §1 `pass_oe` in a caption | Replaced with "the neutral-situation version from Tendencies" |
| §1 RACR undefined | Defined in Go deeper (receiving yards per air yard) |
| §1 standard error not recapped | One-line recap added to You'll need |
| §1 "H and Y ... slot receivers" vs attached Y | Diagram changed to true trips: Y detached into the slot; answer now "H and the detached tight end Y" |
| §1 seam not linked | Linked in the text under Fig 2 |
| Leap 1 target-share contradiction | New "two layers" paragraph in Target share (a number one's share travels; the position split is the play-caller's fingerprint); the equation sentence rewritten; Predict 2 (the old 3) now exercises exactly this |
| Leap 2 positional value never paid off | New ADP material: overall vs positional ADP, why fantasy RBs are dear and NFL RBs cheap, value over replacement (Joe Bryant/VBD, sourced), and a new chart of 2025 PPR points above the worst starter by position (`fig-replacement`) |
| Leap 3 Fig 1 overstates usage vs efficiency | Yards per game recoloured grey as "volume × efficiency"; text now says per-chance stats (YPT, TD) are the unstable ones, explains catch rate's role component, gives the ±0.08 noise and the survivor caveat in caption and text |
| Leap 4 why WOPR | Unsourced "weights fitted" claim removed. New paragraph with a course test: 2024 WOPR and 2024 target share predict 2025 PPR points per game equally (0.58 vs 0.57); WOPR's value is describing the shape of a role. Footnoted |
| Leap 5 neutral filter vs score | Checked the data: in neutral situations Detroit was roughly level (−0.4), and team neutral PROE barely tracks score (r = 0.13). The old claim was wrong; text now says it isn't the score, xpass already includes it, and the jump is ~1.5 standard errors toward Petzing's +6 |
| Leap 6 Barkley apples to oranges | Now RB6 ADP vs RB1 standard / RB2 PPR, positional throughout |
| Leap 7 "ADP overreacts" unsupported | Assertion removed; reframed as an inference from the stability chart ("if prices are set by people reading box scores, they will tend to price last season's touchdowns ...") |
| Leap 8 muddled game-script misconception | Rewritten to lead with taste vs fate; prevent defense named and linked to 10-04 |
| Leap 9 Fig 6 dip at −21 | Explained in the caption from the data (down 20+ late, win probability < 2% on 97% of snaps: teams stop chasing); end ticks relabelled "21+ behind/ahead" |
| Leap 10 Nacua on the median line | Explained with data: Rams in 13 personnel on 21% of dropbacks, Nacua on for 42% of those (85% in 11 personnel), plus one game left early and one missed. Footnoted |
| Leap 11 Answer 1 vs red-zone share | Order fixed in the film room: sneaks take the shortest carries off the back, so his remaining red-zone chances convert less |
| Fig 2 U label far from U | Replaced with a labelled arrow pointing at U (this also uses the formerly dead `pointer()` helper) |
| Fig 3 Parker Washington unused; bottom-left quadrant unnamed | Label dropped; quadrant labelled "Part-time, low output" and described in the caption |
| Fig 4 Seattle panel lacks TDs | Legend now reads "Kenneth Walker III: 5 rush TD / Zach Charbonnet: 12 rush TD" (computed); figure shortened so it no longer strands half a page |
| Fig 7 floats away; four players undiscussed | Half-PPR rank added as a tick (answers gap 9); new paragraphs on Henry, Charbonnet (goal-line callback), Jefferson (141 targets, 2 TD) and Higgins (11 TD); now sits in the PPR text |
| Fig 8 Detroit under-center counter-example; KC grey dot hidden | Detroit paragraph now cites under center 48% → 46% vs Arizona's 28% as the piece that didn't move; 2025 dots drawn larger so an unchanged value shows as a grey ring (caption explains) |
| Fig 10 B touches Q | B moved to w = −2.1 (see coach 1) |
| Print layout blanks | Fig 4 shortened, Predict 2 window tightened, drill order swapped (text-only drill second) so callouts fill pages; 22 → 21 pages. Typst callouts don't break across pages, so a few short pages remain |
| Drag: Barkley inside-2 numbers three times | Kept in the film room only; Fig 4 caption points to it; the old Answer 1 is gone |
| Drag: "four games is small" ×5 | Kept in the misconception callout; method step 5 points there; caption, LAC and DET repeats removed |
| Drag: long You'll-need box | Trimmed; participation-season detail moved out |
| Drag: hook never resolved | Two callbacks: the backup (after the Seattle paragraph: check who is in inside the 5) and the 52-snap tight end (TE section: count routes) |
| §5 Predict 1 spoiled | Replaced: first-and-goal at the 2 from 22 personnel with the lead back subbed out for backup G. The reader must read the substitution; the answer ties to Seattle, the hook's backup, and when the QB sneak would take over |
| §5 Predict 2 too open | Kept, with the true-trips diagram, dime labels, a draw mention and a cleaner "who touches it" answer |
| §5 Predict 3 trivial | Rebuilt around the volume equation (plays × pass rate × target rate × share) plus a position-split twist (new play-caller feeds TEs 30%) that tests the two-layer target share idea |
| §5 TE skill: no real route-participation number | TE section now gives McBride 94%, LaPorta 92%, Higbee/Parkinson 56-59% (estimate, upper bound) |
| §5 game script: no forecasting method | New point spread / total / implied team total paragraphs (glossary entries added), with 2025 data: 7+ favorites led by ~4 per snap, ran 26 times vs 23 for big underdogs, but both dropped back ~35 times; so the spread is mostly an RB and TD signal |
| §5 never names a loser | LAC: McConkey 21% → 15%; DET: Williams 19% → 16% and St. Brown 31% → 29% (inside the noise); method step 4 says to name one |
| Gap 3 quarterbacks | New paragraph after the film room: Hurts 2024, 14 rushing TDs, QB8 in standard despite 2,903 passing yards ("a running back's tax and a quarterback's dividend") |
| Gap 5 vacated targets | Added to method step 3 |
| Gap 6 when are player shares trustworthy | Misconception callout: 2025 target share Weeks 1-4 vs rest r = 0.67, typical miss 5 points |
| Gap 7 QB change | One sentence in method step 3 |
| Gap 8 free snap counts | `load_snap_counts()` named in the snap-share paragraph and Go deeper; betting lines' nflverse columns named too |

### Coach review

| Finding | Action |
|---|---|
| 1 Fig 10 B/Q collision | B at w = −2.1, d = −5.2 |
| 2 trey vs trips | Took the preferred option: Y detached at (−1.5, 8), H at 11.5, Z on the ball at 17; 7 on the line (5 OL + X + Z) |
| 3 dime label | Sixth DB is now `D("D2", "DB", ..., "D")`; caption explains $ and D; dime linked to 02-05's glossary in the answer |
| 4 "entirely by taste" | Now "mostly by the play-caller's taste, with game script and the quarterback's legs doing the rest" |
| 5 Fig 2 vs the on-field estimate | Caption adds that the on-field estimate can't separate the two pictures either, so it is an upper bound for tight ends |
| 6 name the concept | Caption and text: max-protection play-action shot; max protect linked; "some calls take the TE out of the route count by design" |
| 7 how play-callers feature a receiver | Alignment, alerts, manufactured touches (jet/orbit linked); progressions are coverage-dependent; McDaniel's Miami (Hill 30-31%, Waddle 19-21% in 2022-23, course calculation) |
| 8 RB pass protection gate; designed targets | Added to RB item 3 with a Pass Protection link and the Shanahan-tree McCaffrey example |
| 9 head coach shapes PROE | Method step 1 now asks what the head coach wants (Jim Harbaugh, Campbell); LAC PROE credited to both |
| 10 McDaniel's fingerprint is concentration | LA paragraph rewritten: the spread tree runs against his fingerprint, points to roster; bet stated (consolidation, but on whom is unknown) and the loser named |
| 11 Petzing vs McBride | Petzing's Stefanski lineage added (Browns TE coach 2020-21, QB coach 2022; Browns.com sources); scheme vs McBride split stated; LaPorta's 19% in his nine 2025 games shows much of the TE rise is health; the mixed 2025 play-callers noted |
| 12 KC: don't rule out Bieniemy | Paragraph now says a non-calling OC builds the game plan and run install, and four games can't separate him from Walker |
| 13 Fig 9 tush-push realism | Moot: Predict 1 replaced (see beginner §5). The new goal-line drawing is legal (7 on: 5 OL + Y + U; X off) and its caption says "nearly all of it within four yards", which matches |
| 14 Answer 2: the draw | Added (draw to B against five in the box), linked to 03-03 |
| 15 four-minute offense link | Linked at first use in Game script |
| 16 WR route participation not 100% | Clause added: screens, some RPOs, rest snaps |
| 17 Yahoo −1 | "(some sites take off only one for an interception)" |
| 18 dead `pointer()` | Kept and used (Fig 2's U arrow) instead of deleted |

Declined or partial: none declined. The target length (~4,500 words) is exceeded (body now about 10,700 words
before footnotes, from about 7,500) because both reviews asked for substantial additions (fantasy primer,
replacement level, betting lines, QB value, drills); drag items were cut where flagged. New glossary entries
not in the term index: point spread, implied team total, value over replacement (no other chapter defines them);
the index should list them under 14-02.
