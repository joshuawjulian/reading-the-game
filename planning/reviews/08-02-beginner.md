# Beginner review: 08-02 Constraint Theory: How Plays Talk to Each Other

Reviewer role-play: a casual NFL watcher who has never played and has read Parts 1–7 plus 08-01 in order.
That means outside zone (bang/bend/bounce), counter and kick-out, Wing-T series football, play-action, boot,
naked boot, keeper, the shot play and yankee, RPOs, personnel numbers, under center/shotgun/pistol, mugged
linebackers, hot throws, fire zones, simulated pressure, EPA, win probability and quality control coaches are
all things I already know. I read `pdfs/08-02-constraint-theory-and-sequencing.pdf` (20 pages) start to finish
and looked at every figure at 130 dpi, zooming to 250 dpi on Fig 2.

**Overall:** this is a very good chapter. The opening question ("why didn't they call it on the first snap?")
pays off, the constraint tree (Fig 1) is the best single picture in the chapter, the drive table is a lovely
way to show sequencing, and the data half does more than show tendencies: it asks whether breaking one pays,
and the play-action split is a real "aha". There are three serious problems. **The word "squeeze" means opposite
things in three places, and that breaks Predict 1.** **Two plate panels (Fig 2 B and C) can't be decoded from
the drawing.** **One sentence in the defense section gets blitz logic backwards.** After those, the gaps are
smaller, plus three half-empty PDF pages.

---

## (1) Terms used before they are explained, or never explained

Almost everything is prerequisite vocabulary and it is linked. The real gaps:

- **"flea-flicker"** (Common misconception, p. 2): never taught in Parts 1–7, and there is no gloss. One clause
  would fix it: "(a handoff, then a pitch back to the quarterback, who throws deep)".
- **"zero-sum game", "equilibrium", "mix at random", "equalizes the plays' value at the margin"** (footnote 2):
  this is economist vocabulary in a footnote that the main text leans on ("a well-run offense *should* show
  exactly that gap"). Either gloss "at the margin" in the body ("the value of *one more* call") or keep
  the footnote purely as a citation.
- **"squeeze"** is never defined, and it is used for two opposite behaviours (see Leap 1). This is the
  chapter's most important undefined word.
- **"protected boot"** (p. 6, "the protected boot puts a blocker back on the end"): 04-05 taught this, but
  Fig 1's "Bootleg" box is the same play under another name. Say once: "the bootleg (sometimes called the
  protected boot, because a blocker takes the end)".
- **"right tackle"** in Fig 9's caption ("the Will and the right tackle (purple rings) drop"): by this point
  "tackle" makes me think of the offensive lineman first. Write "the right defensive tackle".
- **"tendency table"** is italicised and explained, but the learning objective and the spec say "by personnel
  and *formation*", while the table uses *quarterback alignment*. The chapter never says why: is formation
  missing from nflverse, or is alignment just a cleaner proxy? I noticed the switch and wondered.

## (2) Leaps: a missing or assumed "why"

1. **"Squeeze" means three different things, and the drill depends on it.** This is the biggest problem.
   - Branch (2), p. 3: the backside end "is coached to **squeeze down the line and chase**", and the naked boot
     beats him.
   - Drive table, snap 6: "Backside end **squeezes hard** to stop the cutback", and the text says that is
     "exactly the man the naked boot on snap 7 is built to beat."
   - Predict 1 (Fig 10 and its answer): the end "stayed home and **squeezed straight down, no longer chasing**",
     and "**That kills the naked boot**."

   As a reader, I learned twice that a squeezing end is what the naked boot punishes. Then the drill tells me
   a squeezing end kills the naked boot. The answer depends on a distinction between "squeeze and chase"
   and "squeeze but stay home" that the chapter never draws: how far does each one go, and where does he end
   up relative to the quarterback's launch point? Define both behaviours with a tiny two-panel sketch, use
   different words ("crash/chase" versus "squeeze/stay home"), and make the table and branch (2) say "crash".

2. **Predict 1 has a second correct-looking answer that the drill doesn't rule out.** Fig 1 maps "linebackers
   flow hard" to the **bootleg** (branch 1), with a blocker on the end, not to the counter. In Fig 10 the
   linebackers fly right and the end stays home. By the tree's own logic, the protected bootleg, which blocks
   the end that killed the naked boot, is a natural answer. The answer only discusses "counter versus naked
   boot" and never says why the protected bootleg is worse here than the counter. Add a sentence. Possibly:
   an end who stays home and squeezes is easy for a puller to kick out on a run, but sits right on the
   bootleg's launch point.

3. **"The blitz that punishes an offense for getting too comfortable with quick throws"** (p. 15, defense
   section): this is backwards for someone who read 07-02. Quick throws are the offense's *answer* to the
   blitz. The defense's constraint against quick throws is the *drop* into the hot window, which the next
   sentence and Predict 3 say correctly. I think it should read "the blitz that punishes an offense for holding
   the ball / getting comfortable in the pocket; the drop that punishes a quarterback who expects a blitz and
   throws hot."

4. **The "three hundred pictures" arithmetic contradicts the sentence before it** (p. 8). "A defense doesn't
   line up against a play; it lines up against a *formation*." Then: "a dozen core plays from eight formations
   with three motions is nearly three hundred pictures for the defense." If the defense lines up against
   formations, it sees 8 × 3 = 24 pictures. The ×12 is what the defense has to *prepare for* behind each
   picture, not what it sees. Reword it: "24 pictures to align to, each of which could hide any of a dozen
   plays".

5. **The dose model's key step is stated, not shown** (Fig 3 and the paragraph after it). "Calling it one more
   time would gain the difference between the two plays on that snap, but ... costs a little on *every* snap.
   At the peak those two effects cancel." This is the hardest idea in the chapter and gets two sentences. A
   one-line worked example with the toy numbers would make it click. At 13%, one more percentage point of
   constraint calls gains about 0.15 EPA on that 1% of snaps (+0.0015 per snap). It also costs about 0.03 on
   the constraint snaps already being called and adds about 0.003 to the base snaps, which together nearly
   cancel. Also, **every value of the "offense's average" line is negative** (the peak is about −0.02 EPA per
   snap), so the "best mix" loses points on every snap. That is distracting even with "illustrative" on the
   axis. Shift the toy curves up so that the best mix is positive.

6. **Why is a constraint play "usually a worse play" when the defense hasn't cheated?** The callout says so,
   but the receiver-run and play-action data the chapter cites show these plays winning *on average*. The dose
   model reconciles the two, but only later. One forward pointer in the "Why it exists" callout ("you'll see
   below why their averages still look better") would stop me from thinking the chapter contradicts 03-05 and
   04-05.

7. **Fig 7: how can "guess the team's overall lean" be *worse* than a coin flip?** LA 2024 (about 42%),
   TB 2025 (about 43%) and CAR 2025 (about 46%) have grey dots below 50. The text explains the Packers' *blue*
   dot being below their grey one, but never says why a team's own overall lean, taken from its other games,
   can be right less than half the time. (I assume the team was close to 50/50 and the side of 50 flipped from
   game to game.) One sentence would do.

8. **The Lions film room's Decker anecdote doesn't connect to sequencing.** "He also used personnel itself as
   a weapon ... a two-point pass to a tackle ... wiped out." Why does this belong in a sequencing film room? Is
   it a tendency breaker, since the jumbo package usually means run? If so, say it. As written, it reads as a
   fun fact.

9. **Detroit and the 21-personnel base look.** The whole chapter teaches 21 personnel, offset I, as the
   Shanahan base look. Then the Lions, the chapter's star example, show "too few" and "none" in every
   21-personnel cell of Fig 6. A sentence saying the modern descendants hide the same idea in 11/12 personnel,
   under center, would stop me wondering whether the Lions really fit the family.

10. **Predict 2's last paragraph gives me information I can't use.** "If the free safety is backing up at the
    snap ... the defense guessed the shot. Then the right answer for the offense was the run after all." The
    play-caller has to call the play before the snap. Either frame it as an *audible* cue the quarterback could
    check on, or as a lesson for the next snap.

11. **"Linebackers bite on a good fake whether or not the run has been working"** (sequencing shape 2) slightly
    undercuts "play-action after the big run". The "timing" explanation (the coaches have just told the
    defense to come up) is good, but it is pure assertion. Is there any evidence that play-action EPA rises
    right after a big run? If the course has none, say "coaches believe".

## (3) Diagrams: could I decode them? Do the captions say what to notice?

- **Fig 1 (constraint tree): excellent.** The numbered badges tying defenders to boxes work. One nit: badge
  ① sits between M and S under the linebackers, and at print size it is not obvious that ① means *both*
  linebackers. Badge ③ (backside linebacker) sits next to W, so ① and ③ both point at the linebacker group.
  A one-word label at ① ("both LBs") would help.

- **Fig 2 (the signature plate): A and D work; B and C don't.**
  - **B, naked boot:** I couldn't tell which line belongs to whom. There are four long blue paths. The
    quarterback's roll, the crossing routes and a line running from the right side of the backfield to the
    lower left all look alike, and **no throw is drawn**. The quarterback has a green ring, but his path isn't
    the thick ball-carrier arrow. **The red-ringed end hasn't moved** from his alignment, although the caption
    says he "chased the fake". The "end chases the fake" leader points at a tiny arrow hidden behind the
    linemen. Draw the end's chase clearly (he should end up inside, near where the back's fake went). Make Q's
    roll the thick arrow, and add the throw.
  - **C, counter:** the right guard's pull, the defining feature, is drawn along the quarterback's marker and is
    almost invisible. The fullback's arrowhead points *backwards* (down-field toward the backfield), and I
    can't see a kick-out block on the end. The caption says "the right guard pulls back to kick out the end",
    but I would never have found that in the drawing. Route the pull path a yard deeper than Q, add the
    kick-out bar on E, and label "RG pulls".
  - D: decodable. The post, the deep crosser, the throw over the free safety and his arrow coming down all
    read cleanly.
  - The caption explains every panel but doesn't say **where to look** to see that the first half-second is
    the same. The text does ("cover the bottom three panels..."), but in print a reader looks at the figure
    first. Maybe add: "Compare the five linemen's first steps and R's first step across the panels: they
    match, except for the right guard in C."

- **Fig 3 (dose model):** readable, but the blue "base play rises" line is nearly flat, the dashed "average"
  line is nearly flat from 5% to 20%, so its peak is hard to see, and the bracket at the best mix is small.
  The negative y-values are a problem (see Leap 5).

- **Fig 4 (one play, four outfits):** clear. But the "short bars" (the line's first steps), which the caption
  asks me to compare, are tiny ticks at print size. The caption says "to the defense it is four formations
  to prepare for", but no defense is drawn, so that half of the idea is told, not shown. In the shotgun panel,
  R and Q touch.

- **Fig 5 (counter strip):** frames 2–4 tell the story well: RG and F crossing, the end kicked out, R through
  on the vacated side. But **frame 1 contradicts its own note**. At +0.5 s the RG has *already left the line*
  and stands behind the quarterback, and R hasn't visibly stepped right. The note says "R steps right; the
  line steps right". The whole point of the counter is that the first half-second looks like outside zone,
  and frame 1 shows the pull before it shows the fake. Add a frame at about +0.2 s that shows every lineman,
  RG included, stepping right with R's jab step. Or delay the pull in the simulation.

- **Fig 6 (tendency table):** clear and well captioned. The note "grey cells had fewer than 15 snaps" is
  helpful. Detroit's under-center 39% and 40% are called "close to a coin flip", which is generous next to the
  league's 32–36%. "Much closer to even" (the caption's wording) is fairer, so use it in the text too.

- **Fig 7 (look predictability):** good chart. The caption says "The 50% line is a coin flip", but **no 50%
  line is visually distinguished** from the other gridlines. Darken or label it. Also see Leap 7.

- **Fig 8 (breaker value):** the best data figure in the chapter. The printed play-action shares make the
  point by themselves. One nit: in the right panel, the "look said run, no run fake" bar has a huge whisker
  (about 0.0 to 0.12), so "about the same from either look" rests on a very uncertain bar. The caption could
  say that.

- **Fig 9 (one pressure look, three answers):** **the red rings break the chapter's own legend.** "How to read
  the diagrams" says "A **red ring** marks the defender a play is built to punish", but here the red rings mark
  the *defense's* threats ($, SS, W, M). Worse, $ and SS are ringed as if they are part of the pressure, and
  then they rush in **none** of the three answers. So why ring them? Either show one answer in which one of
  them rushes, or ring only the mugged linebackers. Use a different colour for "threat". The same legend clash
  happens in Fig 12 (W and M in red rings). The title "six at the line" plus two more defenders walked up made
  me count eight possible rushers against six blockers, and the text never addresses that.

- **Figs 10–12 (drills):** clean. In Fig 10 the caption says "the faint dashed arrows show what the defense did",
  but the end, whose behaviour is the key to the drill, has **no** arrow. Only a leader label says "end stays
  home, squeezes down". Draw his short squeeze path so I can compare it with the chase in Fig 2B.

## (4) Drag and repetition

- **"Find the defender who's cheating and you've found the play"** appears four times: after Fig 1, in Watch for
  it, in the Takeaways and in the Predict 1 answer. That's fine as a refrain, but the first two are nearly word
  for word.
- **The Lions under center** is discussed three times: in the text after Fig 6, again in the text after Fig 7,
  and in the Lions film room ("in Figure 6 the Lions' under-center looks were close to coin flips, and in
  Figure 7 they were among the three hardest..."). The film room should add something new, such as a real
  sequence from a Lions game, instead of recapping the two figures.
- **Print layout:** pages 4, 11 and 15 are roughly half blank, because a large figure got pushed to the next
  page. In a 20-page chapter that's noticeable drag. Shrinking Fig 2 / Fig 6 / Fig 9 slightly, or moving a
  paragraph, would close the gaps.
- "That's constraint theory and the illusion of complexity again, showing up in the averages: the fake works
  because it matches the look, and the look works because it carries both." This is a nice line, but it closes
  a paragraph that has already made the point. It could be cut to the first clause.

## (5) Can I do each "You'll be able to…" item?

| Objective | Verdict |
|---|---|
| Tell base from constraint, name the punished defender, explain why the constraint play's average looks better | **Yes / mostly.** Fig 1 makes the first two easy. I can repeat the dose argument, but I couldn't explain it to a friend without the worked numbers asked for in Leap 5. |
| Recognize the illusion of complexity from both ends | **Yes.** Figs 2 and 4 plus the Rams film room do it. |
| Spot sequencing | **Mostly.** Counter after flow and play-action after the big run: yes. Telling "naked boot time" from "counter time" by watching the backside end: no, because of the squeeze contradiction. |
| Explain what a self-scout looks for and does | **Yes.** The question list plus break / hide / bait is crisp, and the Eagles film room is a great counter-example. |
| Read the defense's version | **Partly.** I get one look carrying three answers, but the red-ring legend clash, the $/SS mystery and the backwards blitz sentence left me unsure which defenders actually matter in the look. |
| Build a team's tendency table in nflverse and say how much the look gave away | **Not from the PDF.** The `tendency_table` call is in a folded, `eval: false` code cell that doesn't appear in print, and it depends on helpers defined in another hidden cell. On the web I could run it. The objective also says "formation", but the table uses alignment. |

**Predict-the-play attempts.** Honesty note: the source dump I read included the answer text, so these are not
perfectly blind. I've written what the figure and chapter alone would have led me to, and graded against that.

- **Predict 1:** from Fig 10 and the tree, I'd have said **bootleg (protected)**. The linebackers are flying
  right, which is branch 1, and with the end staying home a *naked* boot is out, so the quarterback needs a
  blocker for the end. My second choice would have been the counter. The official answer is the counter, and
  "naked boot" is the only wrong answer it addresses. That's two problems: the protected bootleg is never ruled
  out (Leap 2), and the squeeze language contradicts the drive table (Leap 1). **I'd have got it "wrong" for
  reasons the chapter itself taught me.**
- **Predict 2:** I'd have said **play-action shot, a post to hold the free safety plus a crosser behind the
  linebackers**. That matches the answer's spirit. The answer opens with "Run is still the single most likely
  call", which felt like a gotcha after a question set up for play-action. The hedge is correct but should be
  the second sentence, not the headline. The final paragraph's pre-snap free-safety cue can't be used by the
  play-caller (Leap 10).
- **Predict 3:** I'd have said **not six: a drop into H's window, probably the Will, with a simulated pressure
  or fire zone**. That matches. It's arguably too easy, because the immediately preceding section is about
  exactly this. It works as a check, but it isn't a stretch.

## (6) Knowledge gaps: what I still wonder

- **How does a defender tell "same look" plays apart, in practice?** The plate section says defenses coach "read
  the guard" and "if nobody blocks you, think boot". What does an NFL linebacker actually read first, and how
  long does he have? Half a second? A sentence with a rough time budget would make "waiting and reacting are
  both wrong" concrete.
- **How fast do defenses adjust within a game?** The drive table has the defense learning between snaps 3 and 4.
  Is that realistic, and who tells the end to change: the coordinator between series, or the player himself?
  This might be a forward link to 08-04.
- **How many base plays does a real offense have?** "A small number" and "a handful": is that 3? 10? Same
  question for constraints per base play. A rough number would anchor the whole tree idea.
- **Does play-action really pay more right after a big run?** The chapter says the timing is the point. It has
  the data to check play-action EPA on the snap after a 10+ yard run from the same look. I'd love that figure,
  even if the answer is "no detectable difference".
- **What does a tendency breaker look like on defense in real life?** An example (a team and a game) of a defense
  breaking its own tendency would balance the offensive film rooms. Right now the defense section has no film
  room.
- **Is unpredictability actually correlated with scoring?** The "predictable is not bad" caution is good, but now
  I want the scatter: Fig 7's blue dot against offensive EPA per play. If that belongs in 13-04, add a forward
  link that says so.
- **How does the RPO fit the Fig 7 measure?** An RPO-heavy team's "run or pass" is decided after the snap, and
  nflverse codes the outcome. Does that make RPO teams look more or less predictable? A one-line caveat in the
  method would help.

---

## Revision (2026-10-07): finding -> action

Inputs: this review, `08-02-coach.md`, and `08-02-factcheck.md`. The fact-check's corrections are all still in place. Every
footnote is still referenced exactly once. New factual claims are sourced: Engstrand (AP, new `[^jets]`), plus course
calculations guarded by asserts (`[^afterrun]`, jumbo counts in `[^neutral]`, the predictability vs. EPA correlation).
Build: `build_pdfs.py 08-02-constraint-theory-and-sequencing --html` OK, 23 pages, and every figure page was checked.

### Beginner review

| Finding | Action |
|---|---|
| (1) "flea-flicker" not glossed | Glossed in the Common misconception callout. |
| (1) Footnote 2 economist vocabulary | Footnote rewritten in plain words ("choose at random each snap, neither can learn"). The body now glosses "at the margin" as "the value of *one more* call". |
| (1)/(2.1) "squeeze" used for opposite behaviours | Two words, defined once. **Squeeze** = boot-counter-reverse: a yard down the line, shoulders square, eyes on Q, stays at the edge. **Crash** = turns and chases flat down the line. Branch (2) is rewritten (with the coach's A7 fix). A new two-panel figure, `fig-end-two-ways` ("He squeezes: the naked boot dies" / "He crashes: the naked boot wins"), shows where the end ends up relative to Q's launch point. Drive table snap 6, its prose, Watch for it, the Predict 1 caption and the answer now all say "crash" for the cheat and "squeeze" for the disciplined play. |
| (1) "protected boot" vs "Bootleg" box | Branch (1) says the bootleg is what 04-05 called the protected boot. The Fig 1 box reads "behind a blocker (the protected boot)". |
| (1) "right tackle" in Fig 9 caption | Now "right defensive tackle". |
| (1)/(5) Tendency table: formation vs. QB alignment | New paragraph: QB alignment is the only formation information in nflverse. It lists what a real report charts (formation codes, offset, motion, hash and field zone), so the table is a *floor*. The objective and the description now say "personnel by quarterback alignment". |
| (2.2) Predict 1: protected bootleg not ruled out | The answer now gives the bootleg partial credit as a reasonable second choice and explains why it is worse here: the BCR end waits on the launch point, the lone blocker meets a defender who expects him, and the crossers don't get time. It also explains why the counter still wins even though a BCR end is a counter defender (coach B1). |
| (2.3) Backwards blitz sentence | Rewritten: the blitz punishes holding the ball (long PA shots, slow dropbacks, a protection that always slides one way). The drop punishes a QB who expects a blitz and throws hot. |
| (2.4) "Three hundred pictures" arithmetic | Now: 24 pictures to align to, each hiding any of a dozen plays, so about 300 *combinations* to prepare for. |
| (2.5) Dose model step stated, not shown; negative curves | Added a three-bullet worked example (gain +0.0015, cost -0.0039, side benefit +0.0026 per snap; net about zero). All numbers are computed inline from the model. Curves are shifted so the best mix is positive (about +0.08). Added a dot at the peak, a leader label and a thicker bracket. |
| (2.6) "Usually a worse play" vs. winning averages | The Why-it-exists callout now has a forward pointer to "Why not just run the constraint play more?". |
| (2.7) Grey dots below 50% | One sentence explains that a team close to 50/50 overall can guess wrong in a game where it leaned the other way. |
| (2.8) Decker anecdote disconnected | The Lions film room is rebuilt around the jumbo package as a tendency breaker. It now has new data: league ~28% pass from 6-OL looks in 2022–24, Detroit 33% on 99 snaps, 82% of those passes play-action. The Decker two-point try is framed as the extreme run-look pass. |
| (2.9) Lions and 21 personnel | Sentence added after the tendency table: the modern tree hides the same idea in 11/12 personnel under center. |
| (2.10) Predict 2's pre-snap safety cue unusable | Reframed as an audible cue (safety drifting back before the snap: check to the run) plus a lesson for the next snap from that look. |
| (2.11) "Linebackers bite anyway" vs. timing | The timing story is now attributed to coaches ("coaches describe..."). The claim is then tested with new data: first-and-10 PA right after a 10+ yd run averaged +0.21 EPA vs. +0.11 otherwise, higher in 3 of 4 seasons, n=581, under 2 SE, so it is read as consistent with the story, not as proof (`[^afterrun]`, asserts). |
| (3) Fig 1 badge (1) | Badge moved between W and M, with a "both LBs" label. The RB track is also fixed (coach B2). |
| (3) Fig 2B undecodable | The end is drawn where his chase took him, with a dashed outline where he started. Q's roll is the thick ball-carrier arrow. The throw to Y is drawn. X runs a clear-out go (coach A4) with an "X clears the corner" label. F starts on his arc before slicing to the flat (coach B4). |
| (3) Fig 2C pull invisible, FB arrow backwards, no kick-out | The RG has a purple ring, a "RG pulls, kicks out E" label and a pull path behind Q to a kick-out bar on E. The RB cuts inside the kick (coach A1). The FB leads onto the Will (coach A2). The LBs are drawn at their flowed spots with outlines where they started. |
| (3) Fig 2 caption: where to look | The caption opens with "Where to look: compare the five linemen's first steps and R's first step... except the right guard in C". It also explains why the counter's line steps right: play-side linemen block down (coach B8). |
| (3) Fig 3 readability | See (2.5). |
| (3) Fig 4 tiny bars; defense told, not shown; R and Q touching | Longer line steps. Under each panel, an italic note says what the *defense* must change ("base 4-3, eight in the box", "nickel, a slot corner on H", ...). The shotgun RB was moved off Q. Z's motion now clears the mesh (coach B3). |
| (3) Fig 5 frame 1 contradicts its note | The RG now takes the zone step before pulling. Frame 1 is at +0.3 s, where every lineman, RG included, steps right. The RB's track is inside the kick (coach A1), and the FB is delayed and on a deeper lane so he doesn't sit on the RG. The caption says "the end on the left (the backside end of the zone fake)" (coach B5). |
| (3) Fig 6 "close to a coin flip" | Text now says "much closer to even". |
| (3) Fig 7 50% line | Darker line with a "coin flip" label, and the caption updated. |
| (3) Fig 8 wide whisker | The caption says the no-fake run-look bar rests on few snaps, so "about the same" is loose for that bar. |
| (3) Fig 9 red-ring legend clash; $/SS never rush; 8 vs 6 | New "dashed brown ring = blitz threat" convention, added to the "How to read the diagrams" legend (which now also explains purple and green). $ and SS are actually walked up (coach B6). In the fire zone the nickel now blitzes off the edge. The title is "eight could rush, one deep". A new paragraph counts 8 threats vs. 6 blockers and gives the standard answer (center and back on the mugs, QB hot off the 7th; coach B11). The Cover 0 FS comes down to take the back (coach B7). Fig 12 uses the same dashed threat rings. |
| (3) Fig 10 end has no arrow | Short dark squeeze arrow drawn over the line. The leader now reads "end squeezes a yard, eyes on Q (no chase)". The Mike ghost no longer touches the S. |
| (4) Refrain repeated near-verbatim | The Watch for it bullet is reworded ("Pick out the cheater... the next constraint play will be aimed at him"). |
| (4) Lions recap in the film room | The recap was removed and replaced with the jumbo data (see 2.8). |
| (4) Half-blank PDF pages | Explanatory paragraphs moved ahead of Fig 3 (plate) and Fig 10. The plate and Fig 10 are slightly smaller. The pages before both figures are now full. The remaining white space is on the Predict pages, which are one drill per page by design. |
| (4) "That's constraint theory... carries both" | Cut to the first clause. |
| (5) Tendency table objective not doable from the PDF | Added a plain-language "recipe" paragraph that appears in print (load, join participation + FTN, filter neutral, pivot mean and counts). The code itself stays folded or hidden, per AUTHORING §5. |
| (5) Predict 2 headline felt like a gotcha | The answer now leads with "This is the snap for a play-action shot"; the run hedge comes second. |
| (5) Predict 3 too easy | **Declined** to make it harder. It is a deliberate check on the section just read, and it is now less trivial because the $ and SS are real threats, so the answer has to name where the extra rusher comes from. |
| (6) How long a defender has to read | Sentence added: the read happens in his first step or two, well under a second. This is kept qualitative because I found no source for a precise number. |
| (6) How fast defenses adjust in-game | Sentence after the drive table (between series, coach in the booth or on the tablet) and a link to 08-04. |
| (6) How many base plays | A qualitative answer: a few base runs and passes, each with a small family. **Declined** to give a specific count: it varies by staff and I found no source for a typical number. |
| (6) PA after a big run | Done with data (see 2.11). |
| (6) Defensive tendency-breaker film room | **Declined**: I could not verify a specific defensive example (team, game, snap) in this pass, and AUTHORING §6 forbids inventing one. The Flores/06-06 pointer remains. |
| (6) Unpredictability vs. scoring | Computed: across 128 team-seasons, look predictability vs. EPA/play correlation is about -0.03 (asserted). Added to the "predictable is not bad" caution, with a link to 13-04. |
| (6) RPOs and the measure | Caveat added to `[^neutral]`: RPOs are coded by outcome. |

### Coach review

| Finding | Action |
|---|---|
| A1 Back outside his kick-out | Plate C and the strip: RB track inside the kick (coach's coordinates, lightly adjusted); RG kick at -4.4/-4.6. |
| A2 FB blocks air; LT purposeless | Plate C: the FB leads onto the Will's flowed spot. LT and LG block down (one step right), C blocks back, and the back side hinges. |
| A3 Unblocked WDE in the PA shot | Plate D: the LT takes one zone step and hinges back onto the end (option 1). The caption says so. The throw now goes between W and M (catch point about (18, -2.5)). |
| A4 X and Z finish together | X runs a go to clear the corner. Z's over is at 11–12 yards under it; Y intermediate, F flat. |
| A5 Backwards blitz sentence | Fixed (see beginner 2.3). |
| A6 Drive doesn't add up | Table replaced with the coach's consistent version, plus a note that snaps 2 and 5 (6 yards each) came from other looks. |
| A7 Backside end's coaching contradicts 03-05/04-05 | Branch (2) now teaches squeeze-and-check boot-counter-reverse as the coaching, with crashing as the cheat. It links 03-05. |
| B1 Kick-out vs. log | The Predict 1 caption and answer are rewritten. The kick-out is the default; the log is the case where the end crosses the guard's face and the back bends outside. The BCR end as counter defender is addressed. |
| B2 RB arrow ends on the Sam | "Press then bounce" in Fig 1, 2A and 4. |
| B3 Z in the mesh at the snap | Motion now ends behind and past the mesh, at (-3.6, -3.0). |
| B4 FB's first step gives the naked away | F takes his arc step before slicing back. The caption says so. |
| B5 "Backside end" in the Fig 5 caption | Fixed. |
| B6 NB and SS not walked up | `mug_look`: NB (3.0, -6.6), SS (4.0, 6.6). |
| B7 13-yard FS manning the back | FS path comes down, and the caption says "comes down late to take the back". |
| B8 Why the counter's line steps right | Caption clause added. |
| B9 Formation is more than QB alignment | Paragraph added: the table is a floor (see beginner (1)). |
| B10 Sixth-lineman snaps folded into 11/12 | Line added to `[^neutral]` (3% league, 28 of 418 Detroit snaps in 2024, verified in the container). Jumbo snaps are counted separately in the Lions film room. |
| B11 Protection language | "IDs the Mike, center and back on the mugs, QB hot off the 7th" in the Fig 10 prose and the Predict 3 answer. |
| C1 Credit Gibbs | Named, with a link to 03-02. |
| C2 Wing-T guard key | Sentence added. I deliberately avoided claiming the waggle uses the *same-direction* guard pull: per 03-05's glossary the guards pull the other way on the waggle. |
| C3 Terminology dialects | Paragraph added (complementary plays, answers, if-then calls, play-pass off, "keeps them honest"). I left out "keepers" to avoid a clash with the QB keeper term the chapter uses. |
| C4 Eagles within-run variety | Paragraph added to the Eagles film room. |
| C5 Engstrand | Verified (AP, Feb 1 2025: Jets OC, formerly Lions passing-game coordinator). Added with `[^jets]`, which also notes Reich as the 2026 OC per FACTS. |
| C6 "No cut, no block: think boot" | Made explicit in "Look closely". The block is attributed to the backside tackle or tight end, consistent with 04-05's U cut-off. |
| D collisions | 2D throw clears W. 2B arrowheads separated. RB no longer on the S. The Fig 10 Mike ghost ends at (3.0, 4.2). Strip frame 2: RG and F on separate lanes. |
| D gridiron notes | Not edited (shared library). New chapter-local helpers: `was_here`/`shifted` (draw a defender at his moved spot with a dashed outline where he started) and `threat` (dashed blitz-threat ring). These belong in the library (see the agent notes). |
