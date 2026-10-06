# 01-01 The Game in Fifteen Minutes: beginner-reader review

Reviewer role: a casual NFL watcher who has never played. This is chapter one, so I have read
nothing else. Sources: `chapters/01-foundations/01-01-the-game-in-fifteen-minutes.qmd` (line
numbers below are qmd lines) and `pdfs/01-01-the-game-in-fifteen-minutes.pdf` (19 pages, every
page read at 60 dpi, figure pages again at 110 dpi). Length: about 11,000 words in the PDF
including footnotes, against a spec target of about 4,000. The title says "fifteen minutes";
the chapter is a 45-minute read.

Overall: strong. The in-or-out corner diagram (Fig 2), the three-hash comparison (Fig 3), the
scoring card (Fig 4), the clock flowchart (Fig 9) and the Super Bowl LIX strip (Fig 11) all land,
and the hook's three questions all get answered by the end. The problems: one answer that
contradicts its own logic, position letters I can't read in four diagrams, a few internal
inconsistencies, and a heavy "see chapter 10-04" habit.

---

## 0. The biggest problems (fix these first)

1. **Answer 2's defensive advice runs backwards (l.1306–1310).** "You'll see defensive backs
   play inside their receivers in this situation, taking away the throws over the middle (where
   a tackle keeps the clock running anyway) and daring the offense to complete passes outside."
   The paragraph has just said the defense *wants* the clock running and wants Z tackled in
   bounds. If a middle catch keeps the clock running, that's the throw the defense should
   *allow*. The throw it must take away is the sideline throw. As written, I learn the opposite
   of the chapter's own rule. Fix: "play *outside* their receivers, taking away the sideline and
   conceding catches over the middle, where a tackle keeps the clock running."
2. **A related sentence in the body is garbled (l.1027–1029).** "The trailing team's defense
   will even let a runner gain a few extra yards rather than give up a tackle in bounds that keeps
   the clock moving." A defense makes tackles; it doesn't "give them up". And a trailing team's
   defense would *want* the runner pushed out, not kept in. I think the intended point is the
   leading team's defense conceding yards in bounds (or the trailing defense shoving runners
   out of bounds). Rewrite so it says one of those clearly.
3. **Position letters in four diagrams are never explained.** Fig 3 (X, H, C, Y, Z, R, Q),
   Fig 10 (X, H, C, R, Q on offense; C and W on defense), Fig 13 (FS, SS, C, W, M, E, T, **$**),
   Fig 14 (U, Y, H, F, T, Q, C on offense; E, T, N, S, W, M, C, SS, FS on defense). There is no
   key saying blue circles are the offense and orange squares the defense, and the unlabeled
   blue dots (linemen) are never explained. Worse, **"C" means two things in the same picture**:
   the center (blue circle) and the cornerback (orange square) in Figs 10, 13 and 14, and **"T"**
   is both a tailback and a defensive tackle in Fig 14. Fig 10's caption names "the Will
   linebacker (W)", which means nothing to me. Fix: one sentence at the first player diagram
   (Fig 3): "Blue circles are the offense's 11 players, orange squares the defense; the letters
   are positions, decoded in [The Twenty-Two](01-03-the-twenty-two.qmd). You don't need them
   yet." Say "a linebacker (W)" rather than "the Will linebacker", and gloss "$".
4. **Fig 3's caption describes a formation that isn't there (l.480).** "Look at the lone receiver
   on the left: on a high-school field he is almost standing on the sideline." The diagram is a
   2x2 formation: X *and* H are on the left. Nothing on the left is alone. Either say "the
   outside receiver on the left (X)" or draw a 3x1 formation, which would also match the body's
   claim that offenses "leave one receiver alone to the boundary" (l.460–461).
5. **The film room contradicts the touchback rule I just learned.** l.864–866 teaches that a
   touchback puts the receiving team at its own 35. The Chiefs 2021 film room (l.1111–1113) says
   "the Chiefs started at their own 25" after a touchback, with no explanation. A beginner will
   think one of them is a typo. Add "(the touchback spot in 2021; it moved to the 35 in 2025)".
6. **The rule for switching ends contradicts itself.** The body (l.869–870), Fig 8 and its
   caption say teams switch ends "after the first and third quarters". Fig 11's caption
   (l.1141) says "in the real game the teams switched ends every quarter." Both can be true,
   because at halftime the teams usually pick the opposite ends again, but the chapter never says
   who chooses ends for the second half, so as a reader I see a contradiction. Add one sentence
   to **Halftime**: "For the second half, the team that didn't choose at the coin toss picks
   again, which usually puts both teams back at their first-quarter ends, so in practice teams
   change ends every quarter."

---

## 1. Terms used before they're explained (or never explained)

Most of these belong to later chapters, and a casual fan half-knows them. The ones marked
**(fix)** confused me or carry an argument.

| Location | Term | Note |
|---|---|---|
| l.200, l.411, l.415, throughout | **snap** | Owned by 01-04. It's used from the second paragraph on and never glossed. **(fix)**: one gloss at first use ("the snap, the hand-off between the legs that starts every play"). |
| l.411 | **play from scrimmage** | Not glossed. "Line of scrimmage" comes at l.296, but "play from scrimmage" vs. a kick isn't explained. |
| l.424, l.444, l.450 | formation; **strong side** | "teams use some other rule (usually the formation's strong side)". I don't know what a strong side is. **(fix)**: gloss + link to 02-02, or drop the parenthetical. |
| l.453 | "twelfth defender" | Assumes I know there are 11 per side. Never stated in this chapter. One clause would do it. |
| l.457–461 | sweeps, screens, "bunched receivers" | Fine for a fan, except "bunched" (a formation term). |
| l.480 | "same **splits**" | Jargon in a caption. Use "spacing". |
| l.524, l.984, l.1278 | **out route**, **dig**, **quick out** | Fig 10's titles and caption depend on them. The pictures explain them well enough, but say "(a route that breaks toward the sideline)" once. |
| l.705–706 | holding, sack | Fan-known; fine. |
| l.709 | **free kick**, "usually punted" | Glossed in place; OK. |
| l.787 | "kicks off" | Used in Possession before the kickoff is described in The shape of a game (l.858). Order issue only. |
| l.860–862 | **"dynamic" alignment**, **onside kick** | Never explained. The parenthetical kickoff history is noise on page 10 of chapter 1 (see §4). |
| l.894 | the **"first touchdown wins"** rule | Mentioned as something that "went away" before I've been told it existed. The Chiefs film room explains it later (l.1121), so add a forward pointer or move the sentence. |
| l.948 (Fig 9) | "**on the ready**", "**winds it**" | Officials' jargon in the flowchart. The text says "signals it's ready for play" (l.963); the figure should use the same words: "No: on the referee's ready signal" / "and starts the clock". |
| l.937 (Fig 9) | "under 5:00 in the 2nd" | The 2nd *half* or the 2nd *quarter*? I read it as the second quarter on first pass. Write "in the 4th quarter" or "2nd half". |
| l.1038 | "**The chains** move" | Owned by 01-02 and not glossed here. Drop it or gloss it. |
| l.1228, l.1234 | **score bug** | The Watch-for-it box assumes it. Gloss it: "the score box in the corner of the screen". |
| l.1278, l.1318 | **line to gain**, **fourth-and-goal** | Owned by 01-02. The drill captions depend on them. "The yellow line" (l.297) gives me half of it. Gloss "and-goal" in a parenthesis. |
| l.1318 | tight ends, fullback, tailback, "heavy goal-line group", "packed the line" | Owned by 01-03. Fine as flavour, but see §0.3: I can't find the "three tight ends" in Fig 14. |
| l.1201 | **short-yardage**, **tush push** | Linked. OK. |
| Fig 5 y-axis, l.632 | "**expected points** per try" | The caption defines it as success rate × points, but 01-02 uses "expected points" (EP) for something different. Call this "average points per try" so the reader doesn't conflate the two. |

## 2. Leaps: a missing or assumed "why"

1. **How much does the hash really matter in the NFL?** The field-side section argues it matters
   a lot: "the sideline acts like a twelfth defender" (l.453), plus three bullets of
   consequences. Then l.521–525 says "An NFL field is close to symmetrical, so alignment and play
   design depend less on the hash." Both can be true, but the chapter doesn't reconcile them.
   I'm left unsure whether a 6-yard difference matters on Sunday. One sentence would fix it: "Six
   yards matters most for plays that stretch to the edge (sweeps, outs, screens) and barely at
   all for plays between the hashes."
2. **Two-score margins (l.771–774).** "Listen for the margins 3, 7, 8, 14 and 17." I can work
   out 3, 7 and 8 from the box. **14** (two touchdowns) and **17** (three scores) aren't
   explained, and the natural question goes unanswered: why is 16 still a two-score game? Add:
   "14 = two touchdowns to tie; 16 is the most two touchdowns with two-point tries can cover; at
   17 you need three scores."
3. **What happens after a missed field goal?** It's never said. That matters for the 7-vs-3
   argument and for Predict 3: a miss gives the other team the ball (at the spot of the kick, or
   the 20 inside the 20). Answer 3 prices a failed fourth-down try but not a missed kick, which
   is fine at 99%, but I still wonder about the 50-yarders.
4. **Why does deferring help? (l.853–856).** "Can turn into back-to-back possessions if they
   score just before halftime" is the reason given. The real point, that the second-half ball
   is guaranteed and that the end of the second half is when possessions are most valuable,
   is implied, not stated. A clause would land it.
5. **Kneel-down arithmetic (l.1087–1090).** "Drain about two minutes" works only if the
   opponent has no timeouts left. The next sentence covers the trailing team's timeouts, but
   say so explicitly: "about two minutes, if the other team is out of timeouts".
6. **The one-point safety (l.713–715).** It's teased as trivia and never explained. Either give
   the one-line scenario or cut it. A teaser I can't resolve is worse than nothing.
7. **The hook's timing (l.188–191).** "Two minutes left in the first half … 'smart, he stopped
   the clock.'" By the chapter's own rule, out of bounds stops the clock until the snap only
   *after* the two-minute warning. At exactly two minutes, before the warning, the praise isn't
   earned. Make it "a minute and a half left".
8. **"After it scores" (Takeaway 4, l.1367–1368).** "A team only gets the ball back by stopping
   the other one or after it scores." "It" reads as the team getting the ball back. Write "after
   the other team scores".

## 3. Diagrams

- **Fig 1 (full field).** Excellent, and every label reads. Small points: the field/boundary
  tints are faint at print scale, and the beginner may not see that the tint is what the
  caption calls "the tinted bands". A thin outline on each band would help. The caption says
  29.75 yd and Fig 3 says 29.8: pick one.
- **Fig 2 (in or out).** The best figure in the chapter. One thing: case 3's blue circle (the
  player's shoulder) isn't labelled, and blue circles haven't been introduced yet. Add "his
  shoulder" as an on-field label.
- **Fig 3 (three hashes).** Strong. See §0.3 (no key to the letters or dots) and §0.4 ("lone
  receiver" in a 2x2 formation). The orange "9 yd outside X" and blue "15 yd outside Z"
  colour-coding is never explained. Why is X's red and Z's blue?
- **Fig 4 (scoring card).** Clear. The touchdown ball sits on top of the "10" numeral. The "R"
  in the safety vignette is undecoded (call it "runner" or drop the letter). Both kick arcs are
  the same green, so it takes a moment to match the PAT badge's leader to the right arc.
- **Fig 5 (try value).** Fine, apart from the "expected points" naming (§1).
- **Fig 6 (FG by distance).** Clean.
- **Fig 7 (drive outcomes).** Clean. "Turnover on downs" is unexplained, but it's linked to 01-02
  in the text below.
- **Fig 8 (game shape).** Clear. See §0.6 about switching ends. "kickoff (roles usually flip)"
  needs the coin-toss paragraph to make sense, and that paragraph comes after the figure.
- **Fig 9 (clock flowchart).** The chapter's key teaching figure, and it works, apart from the
  jargon and ambiguity noted in §1 ("on the ready", "winds it", "the 2nd").
- **Fig 10 (two clocks).** It makes the point. But "C" is both center and cornerback (§0.3).
  The brown dotted line (the ball's flight) is the only unexplained line style in the chapter,
  so add "dotted = the pass" to the caption. The "caught at +12" label box partly covers the
  "40" yard number in both panels. "+12" is clear enough.
- **Fig 11 (LIX strip).** Very good. But **the caption says "the green line is DeJean's
  interception return" while all four field-goal lines are also green** (dashed). Make the
  return a distinct colour. The Chiefs' third label sits on the faint yard numerals. Readable,
  but it's the one place the type fights the field.
- **Figs 12–14 (drills).** See §5. Fig 13 has "$" and the C/C clash. In Fig 14 I can't pick out
  the "three tight ends" the caption promises, because U, Y and H aren't decoded.

## 4. Drag and repetition

- **Length.** About 11,000 words against a 4,000 target, in a chapter titled "fifteen
  minutes". The footnotes are a big share of that. Pages 1, 2 and 4 are a third footnote, and
  long URLs make the print pages feel heavy. Good trim candidates:
  - the kickoff-rules parenthetical (l.860–862): cut to "the kickoff rules have changed every
    year since 2024; see 09-02";
  - the two-minute-warning history (l.881–887): good, but could be two sentences;
  - the Possession section (l.796–799) mostly re-reads Fig 7, which is already discussed at
    l.747–755.
- **"See Clock and Game Management" appears 9 times** (l.662, 896, 961, 966, 979, 1032, 1091,
  1311, plus Connections). After the fourth one I felt the chapter was holding things back.
  Keep the link at the out-of-bounds rule and in Connections, and drop the rest or turn them
  into "(chapter 10)".
- **"Eleven" means two different things.** The hook's "eleven" minutes of action (l.199, l.900)
  and the "about eleven" possessions per team (l.797, l.1367) collide. On a skim I conflated
  them. Say "about 11 minutes" in the hook and "10–11 possessions" in the body, or flag the
  coincidence.
- **l.747–748 has a double parenthetical**: "about 11 possessions (turns with the ball, the
  subject of the next section) a game (10.7 in 2025)". It's clunky. Move the definition into
  its own clause.

## 5. Can I do the "You'll be able to…" items? (drills attempted before reading answers)

**Predict 1 (wide side), my attempt:** "Ball on the right hash, so the left is the field
side. Three receivers go there for room to spread out; one receiver alone on the right uses the
sideline. What it gives up: I don't know." **Result:** the first two parts are right. The
caption hands me most of it ("The ball is on the right hash"), so the drill is nearly free. Make
it harder by dropping that sentence from the caption and making me find the hash in the picture.
I couldn't answer the "what does it give up" part from the body: the defense's ability to
slide safeties to the field and isolate the boundary corner is taught only in the answer.
Add one sentence to the Defense bullet (l.462–466).

**Predict 2 (clock), my attempt:** "Under five minutes in the fourth, so stopped until the snap.
At 6:12 it restarts on the referee's signal." **Result:** correct, and the flowchart made it
easy. Good drill. Two problems: the caption never says it was *first* down, but the answer
talks about "second-and-1" (add "First-and-10" to the caption), and the answer's last paragraph
is backwards (§0.1).

**Predict 3 (FG or go), my attempt:** "FG = 1 + 18 = 19 yards, about 98%, so about 3 points.
Going for it: I need the chance of scoring from the 1. The only number the chapter gives is
'red-zone drives end in a TD 57% of the time', so I'd use that: 0.57 × 7 ≈ 4. Go for it."
**Result:** I got the right answer for the wrong reason. The 57% red-zone figure is per
*drive*, not per fourth-down play, and it happens to be close to the 55% in the answer. The
drill asks me to "put a number on each choice" with a number the body never gives. Add one
line near l.759: "from the 1-yard line, an NFL offense scores on a single play a bit more than
half the time".

Objectives:

- Name every marking, in/out: **yes**.
- Field/boundary and why: **yes** for finding it. **Partly** for "why both teams change". The
  NFL-vs-college contrast leaves me unsure how much it matters in the NFL (§2.1).
- Score any play, explain 7 vs 3: **yes**, except for margins 14/17 (§2.2).
- Clock after any play: **mostly yes**. I can't handle a fumble out of bounds, a ball carrier
  who runs out behind the line, or the 10-second runoff, but those are fair to defer.
- Game clock vs play clock: **yes**.
- Shape of a game: **mostly**. The ends-switching contradiction (§0.6), plus overtime coin
  toss and playoff OT timeouts not mentioned.

## 6. What I still wonder (that this chapter should answer)

1. Where does the other team get the ball after a missed field goal? (§2.3)
2. Is there a try after a touchdown with 0:00 on the clock, and after a game-winning touchdown
   in overtime? ("the clock doesn't run during it" hints at the first; the second is unaddressed.)
3. Who picks ends for the second half, and for overtime? Is there a new coin toss for OT?
4. Why is 16 a two-score game but 17 three? (§2.2)
5. How does a team "spend a down moving the ball to the middle" (l.468–469, l.424)? What play
   does that?
6. Why is the field 53⅓ yards wide? It's an odd number; a sentence of history (160 ft) would
   satisfy the curiosity the chapter itself raises.
7. In Fig 10, why do the corner and linebacker run *toward* X but fail to keep him in bounds on
   the out route? (I.e., the defender's job in the out-of-bounds fight; the answer to Predict 2
   tries to cover this but gets it backwards.)
8. What actually is the one-point safety? (§2.6)

---

## Revision (2026-10-06): finding -> action

Covers this review and `01-01-coach.md`. The fact-check is unchanged: no verified claim was
altered except where a finding required it, and every new claim has a source (the 2026 rulebook,
nflverse play-by-play, or a cited article). Rebuilt with `build_pdfs.py --html`: OK, 22 pages,
zero errors. Every figure page was rasterized and checked at 60 dpi, with figure crops at
130–300 dpi.

**Beginner §0 (biggest problems)**
1. Answer 2 backwards: rewritten. Defensive backs line up *outside* receivers and concede the
   middle; the figure now shows the corner outside Z driving on the out. Added the two-minute
   warning as a free stoppage (coach A1).
2. Garbled trailing-defense sentence: replaced with the real concept and two verified examples,
   Super Bowl XLVI (Belichick lets Bradshaw score, 1:04, NYG–NE) and Westbrook kneeling at the
   1 (PHI at DAL, 2007). Both are checked in nflverse pbp, with sources in the new fn `letscore`.
   Super Bowl XXXII was left out because nflverse has no 1997 data to check it against.
3. Undecoded position letters: added a reading key paragraph before the first player diagram
   (circles = offense, squares = defense, letters decoded in 01-03, blank circles = linemen).
   A new `ch1()` helper blanks the center's label, so "C" only means cornerback here, and makes
   every running back "R", so "T" only means defensive tackle. Captions now gloss C, $, FS/SS,
   M/W and E/T/N; "Will linebacker" became "a linebacker (W)".
4. Fig 3 "lone receiver" in a 2x2: caption rewritten. The figure now aligns X by landmark,
   never closer than 7 yd to the sideline (coach A4 option b), and labels "X: N yd from the ball"
   (15/13/11), so the squeezed boundary is visible.
5. Chiefs touchback at the 25: added "(the touchback spot in 2021; it's the 35 now)".
6. Switching ends: the coin-toss paragraph now says who chooses for the second half (Rule 4-2-2).
   The unverifiable "teams switched ends every quarter" in the Fig 11 caption is now "the
   direction changed from quarter to quarter".

**Beginner §1 (terms)**: *snap* glossed at first use and linked to 01-04. *Play from scrimmage*
glossed. "Strong side" replaced with "the side with more receivers (the formation's *strength*)",
linked to 02-02. "Eleven players a side" added. "Bunched" became "most of their receivers";
"splits" became "spacing" (caption rewritten). Out route and dig glossed in the Fig 10 caption;
"quick out" became "a 9-yard out". "Kicks off" glossed in place. The kickoff-rules parenthetical
was cut (§4). "First touchdown wins" now explains itself and points to the Chiefs film room.
Fig 9: "on the ready / winds it" became "on the referee's ready signal, once the ball is
re-spotted", and "under 5:00 in the 2nd" became "in the last 5:00 of Q4". "The chains move" was
dropped. *Score bug* glossed. "And-goal" glossed in the Fig 14 caption. Fig 5's "expected points"
became "average points per try". Left as is: holding, sack, free kick, sweeps and screens
(fan-known or glossed in place).

**Beginner §2 (leaps)**
1. Added one sentence on how much the hash matters: most for edge plays, hardly at all between
   the hashes.
2. Margins: explained 14, 16 and 17, and added 16 to the list to listen for.
3. Missed field goal: the ball goes to the spot of the kick, or the 20 (Rule 11-4-2, fn
   `missedfg`). Added to the Field goal section, the Possession list and the glossary entry.
4. Why defer: the end of a half is when a possession is worth most, so a team can get two turns
   in a row.
5. Kneel arithmetic: added "*if the other team is out of timeouts*" and that each timeout gives
   back about 40 s.
6. One-point safety: added the one-line scenario (Rule 11-3-2(c)).
7. Hook: "Ninety seconds left".
8. Takeaway 4: "after the other team scores".

**Beginner §3 (diagrams)**: Fig 1: outlined bands, 29.8 everywhere. Fig 2: "his shoulder" label.
Fig 3: as in §0.4, with both room arrows now neutral ink (no unexplained red/blue). Fig 4: TD run
moved off the "10" numeral and drawn as a run in progress; ball carrier unlabelled; PAT arc in
its own colour (magenta) to match its badge; badges re-laid so no leader crosses a kick arc.
Fig 8: "kickoff, usually by the team that received first". Fig 10: caption explains the dotted
line, centre unlabelled, field numbers hidden, notes stacked so they don't touch. Fig 11: the
return line is purple, not field-goal green; label boxes made opaque over the numerals.
Figs 12–14: see §5 and the coach items below.

**Beginner §4 (drag)**: cut the kickoff-rules parenthetical, cut the two-minute-warning history
to one sentence, and replaced the Possession recap with two sentences. "See Clock and Game
Management" went from 9 occurrences to 4 (overtime per the spec's forward reference, the
out-of-bounds rule and 10-second runoff as owned-term links, and Connections). The "eleven"
collision is fixed: "11 minutes" in the hook, 10.7 possessions in the body, "10 or 11" in the
takeaway. The double parenthetical is rewritten. Footnotes no longer repeat the rulebook URL:
it is given once, in fn `field`. **Partly declined:** the chapter is still long (about 9,500
prose words, up from about 8,500), because the two reviews asked for about 30 additions: rules,
whys, examples and glosses. I kept the length rather than drop requested content. I also kept
the "fifteen minutes" title, which refers to the hook's 11-minutes-of-action idea, not to
reading time.

**Beginner §5 (drills)**: Predict 1: the hash is no longer given away in the caption ("Find the
hash marks first"), and the body's Defense bullet now teaches sliding the safeties and isolating
the boundary corner. Predict 2: the caption says "First-and-10". Predict 3: the body now gives
the one-snap rate from the 1 or 2 (`goal_td`, 55%, fn `goalline` moved to the body), so the drill
can be solved from the chapter.

**Beginner §6 (wonders)**: 1 done. 2: the try is played after time expires and skipped in
sudden-death OT (Rule 4-8-2(c)). 3: second-half choice added, and OT starts with a new coin
toss (Rule 16-1-2). 4 done. 5: "centering the ball" explained. 6: 53⅓ yd dates to the 1881
convention (fn `width`, Pigskin Dispatch, one secondary source). 7: leverage sentence added
after Fig 10. 8 done.

**Coach A (must fix)**
- A1: done (see §0.1).
- A2: Fig 14 hand-built goal-line 6-2: six linemen (6-tech on U, 3-tech, two A-gap N, inside
  shade of Y, head-up on the wing), M and W at 2.3 yd, corners 1.2 yd off outside U and H, one
  safety at 4 yd. Tailback relabelled R.
- A3: the two-point try is now on a hash and the PAT is snapped from the middle; the caption says
  tries start between the hashes, where the offense chooses.
- A4: option (b), done.
- A5: done with XLVI and Westbrook (see §0.2).

**Coach B**
- B6: done.
- B7: the two-minute warning now comes "after the last play that started with more than 2:00",
  with the 2:04/1:57 example, in the glossary, the text and a takeaway.
- B8: added the try and touchback "anywhere between the hashes" rule (fn `spot`, Rules
  11-3-1(a) and 11-6-3). The Kickers bullet now says a field goal is snapped wherever the last
  play ended.
- B9: fumble out of bounds restarts on the ready signal (4-3-2-f), and "an offense that does"
  now carries the runoff ("a defense is never charged a runoff", 4-5-4 Note 9). Both are in fn
  `clockrules`.
- B10: the Defense bullet now covers casting (bigger press corner and run-support safety into the
  boundary), the safety slide, and "mostly a college habit; many NFL defenses set calls by
  strength".
- B11: Fig 1 now has direction arrows beside each number except the 50, and the far row is
  rotated 180°. Text and fn `field` cite Rule 1, item 9.
- B12: punt bullet rewritten.
- B13: touchback note and *squib kick* (linked to 09-02) added, plus the contrast that with KC
  holding timeouts, in-bounds didn't matter, only yards. **Partly declined:** the claim that
  Buffalo "played soft zone" is not in pbp, so I wrote only what pbp shows (Kelce's 25-yarder
  "short middle").

**Coach C/D**
- C14: the corner is now outside Z (16.5) at 6 yd, driving on the out. W is at an apex over H.
  "9-yard out" in the caption.
- C15: the pass is now thrown to the catch point (new `time_pass()` helper). The title says "Deep
  out to the sideline". The centre is unlabelled and the numbers are hidden.
- C16: Y is detached and Z is on the line, so this is true trips with 7 on the line.
- C17: the pylon clause is added to key 4.
- C18: "R" is removed.
- C19: wording fixed.
- D20: done.
- D21: changed to "takes away his outside".
- D22: changed to "usually near its own 40", backed by a new nflverse calc (median first snap
  after a safety, 2016–2025: own 37). It is computed inline as `safety_start`.
- D23: no change needed.
- D24: done.
- D25: added one line on the four-man rush (FACTS §1), with the source in fn `lix`.

**Gridiron:** not edited. The chapter-local helpers are `ch1()` (labels), `time_pass()` (throw to
the catch point, using `Play.position`/`ball_position` and `gridiron.play.BALL_SPEED`) and
`hide_numbers()`.
