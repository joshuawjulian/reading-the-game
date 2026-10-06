# 01-06 How to Watch a Broadcast Like You Mean It: beginner-reader review

Reviewer persona: a casual NFL watcher who has never played and has read only 01-01 to 01-05.
I read the whole chapter in the PDF (pdfs/01-06-how-to-watch-a-broadcast.pdf, 19 pages, rasterized
at 95 and 200 dpi) and checked it against the .qmd. I tried the drills before reading the answers.

Overall: this is strong and useful. The trapezoid "what the camera sees" picture (Fig 1) and the
"bar to beat" ladder (Fig 8) are the two best ideas in Part 1 so far. I now *get* why I never see
the safeties. The problems are one real contradiction with 01-05, one internal contradiction about
how much down and distance is worth, a few practical gaps that will bite me on Sunday, and length
(roughly 6,800 words of prose against a 4,000-word target).

---

## Must fix (top 5)

1. **Drill 2 contradicts 01-05 and mostly repeats it.** 01-05's "Predict the play 2: the safety
   at :07" uses the same picture (two-high, safety walks down late) and concludes "Most
   quarterbacks kill it, and throw": seven in the box against six blockers, so the run is bad.
   01-06's Answer 2 ends: "For your log this should *lower* your confidence in a pass on first
   down, not flip it: a defense that adds a man near the line is often inviting the throw." Using
   what 01-05 taught me, I *raised* my pass confidence. The sentence also argues against itself:
   if the defense is "inviting the throw", why would a pass be *less* likely? Either fix the logic
   (more likely a pass or a check to one, consistent with 01-05) or explain why 01-05's reasoning
   doesn't apply on first-and-10 from the shotgun. Then make the drill do something 01-05's
   didn't, like the broadcast angle: "the walk-down happens off screen; what on your TV picture
   tells you it happened?"
2. **"Single biggest input" vs "barely beats always pass."** In the scorebug list: down and distance
   "is the single biggest input to a run-or-pass guess." Later, under Fig 8: "**down and distance
   alone barely beat 'always pass'**" (60% to 62%) and "the **score and the clock add more than the
   down does**." As written, both can't be true. Reconcile them: down and distance swings the pass
   rate the most *where it is lopsided* (3rd and medium is 91%, 3rd and 1 is 23%), but because
   1st and 10 is the most common snap and is a coin flip, it adds little to *accuracy across all
   snaps*. Say that once, in the scorebug section, so the ladder confirms it instead of
   overturning it.
3. **The best defensive tell can't be seen during the moment the chapter tells me to use.**
   Fig 1 teaches that both safeties are off screen at the snap. The safety-depth section then says
   "Find the safeties before every snap; if they are off the screen, look at the top of the frame
   and wait for the skycam replay." But the replay comes *after* the snap, which is too late for a
   prediction. Say plainly what is possible live (the top edge of the frame; the analyst; the
   occasional wide pre-snap shot; Prime Vision) and that safety depth is mostly a *replay* habit
   for now. Otherwise I'll put "safeties" in my log's clue column with nothing to go on.
4. **"Watch one thing" vs the "Where to look" figure.** The rule in bold is "pick one thing to
   watch, and watch only that until the play is over." Fig 4 then numbers eight things, five of
   them during the live play (backfield, safeties, linemen's first step, safeties' first steps,
   catch point). Which is it? Say explicitly that the pre-snap scan covers several things (1–2),
   that after the snap you pick ONE of (3)/(4), and that (5) is what the camera hands you anyway.
5. **The paper log and the pandas log don't match.** The paper template's columns are
   `# | Qtr clock | Down & dist ("1st & 10") | Ball on | Score | Call | Conf. ("55%") | Main clue
   (free text: "under center, 2 TEs") | Result | ✓/✗`. The code expects `down` (a number), `call`,
   `conf` (0.55), `clue` (one of four categories: situation / alignment / stance / safeties) and
   `result`. Someone typing the paper sheet into a spreadsheet won't end up with a file this code
   runs on. Give the CSV header literally (`snap,qtr,clock,down,togo,yardline,call,conf,clue,result`),
   tell me to code the clue into one of the four buckets, and either add the down-and-distance
   baseline to the code or drop "compare it with what the down and distance alone would have
   earned you" from the objective. The code only compares me with "always pass".

---

## (1) Terms used before they are explained, or never explained

- **shotgun**: used in Table 2 ("shotgun with no back"), in the stance section ("shotgun-heavy
  offenses") and in Fig 5 ("79% of snaps from the shotgun") before it is defined in "The running
  back: depth and offset" ("The quarterback stands about five yards behind the center (the
  shotgun)"). 01-02/01-03 used the word but never defined it. Define it at first use, or move
  the gloss up.
- **"heavy formation"** (Table 2, Run row) is never defined and clashes with **heavy hand**, which
  is taught a page later. A beginner will think they are related. Say "a formation with extra
  tight ends or a fullback".
- **"shotgun with no back"** (Table 2) and **"shotgun, no back"** (log row 4) mean an empty
  backfield, which isn't explained.
- **slant / dig** (Answer 3: "a route that breaks inside (a slant or a dig across the middle)"):
  not defined; they are owned by 04-01. Add a gloss and a link, or say "a quick route cutting
  inside".
- **"receivers around the stadium record where each one is"** (Next Gen Stats bullet). In a
  football book "receivers" means wide receivers. Say "antennas" or "sensors" instead.
- **pressure** (completion probability: "this receiver separation and this pressure"): not
  defined here or earlier as a term. Gloss it in a few words.
- **man-to-man coverage** (Answer 2): 01-03 glossed man and zone briefly, so this is fine, but the
  Answer adds it as a third possibility with no reason. Why would a walked-down safety mean man
  coverage? It's a leap (see (2)).
- **FTN charting** (Fig 5, Fig 6 and Fig 8 captions): what is FTN? The text's "charting services
  record it on every snap" helps; name FTN in that sentence once.
- **XFL** (skycam history): give it a two-word gloss ("a spring league").
- **pocket** (Table 1, "The pocket"): owned by 04-02. Probably familiar from TV, but give it a
  word of gloss.
- **"the box"**: glossed again here, which is fine. But Answer 2 says "an extra defender **next
  to** the box" while the body says "in the box". Pick one.
- **crack block**: glossed inline, which is good, but it isn't linked to its owner, 03-05.
- **calibration**: explained in plain words, which is good. It could link to 15-02, its owner.
- **Short / medium / long buckets**: here "long (7 or more)". 01-02 used 7–10 long and 11+ very
  long. Keep 01-02's buckets or say "7 or more (01-02 split this into long and very long)".
- **Marker letters**: in Drill 1, **T** is the tailback (blue) and also both defensive tackles
  (orange), and **S** (Sam) sits right next to **SS**. The tailback's T especially tripped me.
  The caption explains it, but consider R for the tailback, as in every other figure.

## (2) Leaps: a "why" that's missing or assumed

- **"A back offset to the quarterback's right usually runs to the left"** (body and Fig 5 B):
  why? It's deferred to Zone Running, but one sentence would land: the back takes the handoff
  moving across in front of the QB, so his path already points to the other side.
- **Defensive linemen "sitting back on his heels may be about to drop into coverage"**: a
  defensive lineman dropping into coverage? Nothing so far has told me linemen ever cover. Gloss
  it ("some defenses drop a lineman to fool the protection; see 07-02") or cut it.
- **Table 2, Pass row: "Where [the safeties] go in the first second tells you the coverage"**:
  tells me *what*? I don't know any coverages yet. Give the one beginner-level read: both stay
  deep, or one drops toward the middle and one comes down. Otherwise I'll watch the safeties and
  learn nothing.
- **Table 2, Run row: "One guard"**: which guard, and why a guard rather than a tackle or the
  center? One clause would do (the guards pull and lead most runs, and are the easiest linemen to
  pick out).
- **Table 2 has overlapping rows.** "Run (short yardage…)" says watch a guard; the next row,
  "Short yardage / goal line", says watch the line of scrimmage. Which one on third-and-1?
- **Answer 1: "about 80–85%"**: the base rate from under center on third-and-1 is already 84%
  (footnote), and then three more clues all point to run. Why doesn't my confidence go *above*
  the base rate? The real answer (the clues overlap, since heavy personnel, under center and a
  deep tailback travel together, so they aren't independent) is a valuable lesson. Say it.
- **Answer 3 dismisses two of the three meanings of a reduced split.** The body says a reduced
  split means a crack block, a crossing route, or an outside-breaking route. The answer picks
  "a route that breaks inside" without saying why the other two are less likely. (Crack: the run
  would go away from him, because the back is offset left. Outside-breaking: possible.)
  Show that reasoning.
- **Answer 3 ignores the two-high safeties**, although the drill caption lists them as a clue and
  the safety section says two-high means "fewer defenders near the line to stop a run". Does that
  push me toward run? Say whether it matters here and why.
- **"Inside the opponent's 20 … the field shrinks"**: why? (The end zone caps how deep receivers
  can go.) One clause.
- **The play clock on the scorebug** (":18") is shown but isn't one of the five things. Then
  Drill 2 says "with about eight seconds on the play clock". Tell me why the play clock matters
  (late walk-downs; no-huddle teams) or say it's deliberately left out.
- **The chapter's simulated play doesn't match its opening.** The hook is a safety biting on a
  *play fake*. Figs 2 and 4 are a shotgun deep shot with no fake, yet the Fig 2 caption says "the
  safety who was supposed to be there". I went looking for the fake in the frames. Either add a
  fake or say "a different deep shot".
- **Hook vs scorebug**: the hook is "Third-and-6, early in the fourth quarter". The scorebug
  example is third-and-6 with 2:41 left, which is late, not early. If they are meant to be the
  same moment, make them agree.
- **Safety depth ranges drift**: "usually 10 to 15 yards off the ball" (Fig 1 text), "12 to 15
  yards" (safety section), 13 yards in the diagrams. Use one range.

## (3) Diagrams: what I couldn't decode, or captions that don't say what to notice

- **Fig 1 (TV frame)**: excellent. It's the chapter's best picture. Two snags: (a) the label
  "◄ camera: high on this sideline" sits in the bottom-left corner, and I first read it as
  "the camera is behind the offense". Put a camera glyph on the left edge, level with the line
  of scrimmage. (b) "$" for the slot defender: 01-03 introduced it, but a one-word reminder in
  the caption ("$ = slot cornerback") would help.
- **Fig 2 (camera follows)**: the story reads in print. In panel 4, "The catch: 3 of 22 on
  screen", the football icon covers Z, so I count a ball, C and SS, and the receiver who caught it
  is invisible. Same in panel 2: the QB marker is hidden under the ball. Offset the ball icon or
  draw it smaller on top.
- **Fig 4 (where to look)**:
  - Panel 2: the QB is hidden under the ball icon again.
  - Panel 3: the catch-point oval (5) runs into the top edge of the window, and its badge sits
    almost on the frame. Widen the window by about 2 yards.
  - Panel 4: badge **7** sits between the X oval (8) and the FS oval, so I couldn't tell which
    oval it belongs to. The SS oval has no number at all.
  - Panel 2's caption says "(3) the linemen's first step (back = pass, forward = run)", but at
    this scale the step is invisible. Fine for "where", but don't imply I can see it here.
  - See must-fix 4 on the conflict with "watch one thing".
- **Fig 5 (tells card)**:
  - A. Stance: there's no line of scrimmage or "forward →" label, so the arrows are
    ambiguous. The two-point figure is a man standing fully upright (offensive linemen in a
    two-point stance are crouched, hands on thighs). The light-hand and heavy-hand figures mostly
    differ in head height; the weight difference the caption describes isn't visible. Add a
    weight arrow or shading over the hand vs the heels.
  - B: fine. The panel title says "depth and offset", but only the shotgun shows an offset.
  - C: three Z markers on one line read as three receivers. Say "the same receiver, three
    possible spots".
  - D: the axis numbers 5/10/15 have no unit ("yards off the ball").
  - There is a large empty band between rows A/B and C/D.
- **Fig 3 (scorebug)**: clear. The possession football touches the "H" of HOME. "AWY" reads
  like a typo; real bugs use team codes.
- **Fig 6 (alignment by team)**: clear, and the Washington/Rams labels are good.
- **Fig 7 (paper log)**: clear. See must-fix 5 on the CSV mismatch.
- **Fig 8 (ladder)**: very good. The caption's "Each rule was learned from the 2024 season …"
  is a sentence a stats-minded reader will love.
- **Drill 1 figure**: the "heavy hands all along the line" arrow lands on the U/LT gap rather
  than on the line as a whole. See also the T/T and S/SS label clashes in (1).
- **Drill 2 figure**: clear. The ghost SS is small and faint at print size, so enlarge it a touch.
- **Pandas output in print** includes `Name: hit, dtype: float64` clutter. Format the groupby
  output (for example `.to_string()` or one rounded table) so a beginner isn't reading pandas
  internals.

## (4) Drag and repetition

- **Length**: about 6,800 words of prose and callouts against a 4,000-word target. It doesn't feel
  padded paragraph by paragraph, but it adds up. Candidates to cut:
  - The yellow-line anecdote ("after one network agreed to pay for it") doesn't serve the
    lesson; the skycam history alone makes the "too early" point.
  - The "Madden vs. real life" callout and the "Common misconception" callout under All-22 make
    nearly the same point back to back. Keep one.
  - The "Go deeper: why the confidence column?" callout and the paragraph after it both explain
    that later chapters add columns or scoring. Merge them.
- **The alignment numbers are repeated about six times**, in alternating frames: Fig 5 caption
  (79% / about 30% pass), panel B (79/29/31% pass), bullets ("threw on 79%", "ran on about 70% of
  pistol snaps", "about 69% runs"), Fig 6 caption, the misconception ("seven in ten"), and the
  Takeaways. Switching between pass % and run % makes me do arithmetic. Use pass % throughout
  and state the numbers once in full.
- **"Clue, not a guarantee"** appears in the glossary, an objective, the tells intro, the Fig 5
  caption ("a lean, not a law"), the misconception and the Takeaways. Twice in the body is enough.
- **Drill 2** repeats 01-05's drill 2 (see must-fix 1).

## (5) Can I do each "You'll be able to…"? Drills attempted before opening the answers

| Objective | Verdict |
|---|---|
| Say what the TV camera hides and which angle gives it back | **Yes.** Fig 1 plus Table 1 nail it. |
| Read the scorebug in five seconds and form a lean | **Yes**, though "single biggest input" vs the ladder left me unsure how much weight down and distance gets (must-fix 2). |
| Pick one thing per snap and per replay | **Mostly.** Table 2 works, but overlapping rows, "which guard?", and Fig 4's eight things muddy it. |
| Read the win-probability bar and NGS numbers | **Yes.** Clear and well glossed. The calibration misconception is great. |
| Spot four tells | **Partly.** Backfield: yes. Splits: yes, as "where to look". Stance: only on close-ups, and the figure doesn't show the weight. Safety depth: **not live** (must-fix 3). |
| Keep and score a prediction log, compare with down and distance alone | **Paper: yes. Pandas: not from my own paper sheet** (must-fix 5). The code doesn't compute the down-and-distance comparison. |

**Drill 1 (third-and-1, I-formation, heavy hands):** my answer was run, 85%, watching the line of
scrimmage or a guard. This matches the answer. I hesitated over which "one thing" to pick
because Table 2 gives two rows for short yardage. I wondered why 85% and not higher (see (2)).

**Drill 2 (safety walks down late):** my answer was two-high to one-high with one more defender
near the line, so a likely run blitz or a check by the QB. Using 01-05's kill call I *raised*
pass, to about 65%. On TV I'd see it only if he walked into the top of the frame. I got "what
changed" and "how would you know" right. My lean **contradicted the answer's "lower your
confidence in a pass"**, and I think the answer is the one at fault (must-fix 1).

**Drill 3 (second-and-6, gun trips, back offset left, X reduced, two-high):** my answer was pass
at 75% because of the shotgun. Offset left means a run would go right, toward trips. For X's
reduced split I couldn't choose between crack block, crossing route and outside-breaking route.
I wondered whether two-high should pull me toward run. The answer agreed on pass at 75%, but it
chose "inside-breaking" without showing why, and it never addressed the two-high clue (see (2)).

## (6) What I still wonder (the chapter should answer some of these)

- **The pause often isn't on my screen.** The broadcast is frequently still showing a replay,
  a sideline shot or a graphic until a second or two before the snap, and against a no-huddle
  team there's almost no pause. What do I do then? Log from the situation alone? Mark it
  "didn't see the formation"? This will happen on Sunday, probably several times a quarter.
- **Logistics.** When do I write the line? Between the snap and the next huddle I'm watching the
  replays the chapter told me to use. Should I pause the DVR? Use abbreviations? (The paper
  template has ten columns, which is a lot to write in 30 seconds.)
- **Edge cases when logging.** Scrambles and sacks count as passes, good. But what about RPOs,
  QB designed runs, screens, and trick plays? A one-line rule would help (for example "log what
  the QB did with the ball; scrambles are passes").
- **Which team do I log?** "One team" for a half. Does it matter which, home or away, or the one
  I know better?
- **How visible is a heavy hand on real TV?** How often does the broadcast actually show a line
  close-up before the snap? If it's rare, say "use this one on replays and the end-zone angle"
  and don't make it a live clue.
- **Which side is the main camera on in a given game, and does it matter for which receiver I
  can see?** Is the near-side receiver sometimes in frame? (Fig 1 hides both.)
- **What does the skycam replay actually look like?** A one-line description of the frame (the
  camera behind and above the QB, safeties at the top of the picture) would help me recognise it
  when it comes on.
- **Is there a way to see the All-22 free?** The chapter mentions team sites and film-breakdown
  writers. One concrete example of where to find a clip would turn "there exists" into "go here".

---

## Revision (2026-10-06)

Both reviews (this one and `01-06-coach.md`) were addressed in one pass. The fact-check is intact:
no verified claim was changed except where a review required it, and every new number or rule is
footnoted (new footnotes: `wp`, `idp`, `pa`, `gun110`; `short` extended with the sneak share).
New numbers are course calculations from nflverse + FTN (2025 REG, runs and dropbacks), or reuse
13-02's fact-checked play-action sources. Rendered with `build_pdfs.py --html` (OK, 20 pages);
every figure re-inspected at 80–170 dpi.

### Beginner review

| Finding | Action |
|---|---|
| MF1 Drill 2 contradicts 01-05 and repeats it | Rewritten as a broadcast drill: "the safety who walks into the picture". The figure now shades the TV footprint, so both safeties start off screen and the SS walks into the top edge. The answer covers what you'd see on TV (a defender arriving at the top edge, the box count going from six to seven, linebackers shifting, the QB changing the call, the analyst) and nudges the lean *toward* pass, consistent with 01-05: 72% shotgun 1st-and-10 base (new fn `gun110`), the low play clock and the possibility of a bluff. The unexplained man-coverage leap is gone. |
| MF2 "Single biggest input" vs "barely beats always pass" | Scorebug item 1 now says D&D decides the lopsided downs, but first-and-10 is a coin flip, so it adds little across a game, and points to the ladder. The ladder text says "as the scorebug section warned". Takeaway updated. |
| MF3 Safety tell isn't visible live | New paragraph in the safety-depth section on what you *can* do live (top edge of frame, count the box, the analyst, wide shots, Prime Vision); otherwise it's a replay habit for now. Takeaway says so. |
| MF4 "Watch one thing" vs Fig 4's eight numbers | Rule restated in two halves: scan several things before the snap, then watch ONE from the snap. Fig 4 panel titles are now "scan 1 and 2", "pick 3 OR 4", "the camera shows 5", "replays: one per replay". The caption says the line's step is too small to see at this scale. |
| MF5 Paper log ≠ pandas log | The paper sheet's columns are now the CSV header, given literally (`snap,qtr,clock,down,togo,ball_on,score,call,conf,clue,note,result`). The clue is one of four words (sit/align/stance/safety), with a free-text `note`, and the essential columns are shaded. The code now computes the down-and-distance-only guesser (the 2024 majority rule behind the ladder's second bar), so the objective is met. |
| shotgun used before defined | Defined, with under center, in a short paragraph before the tells card (linked to 02-02). The table rows no longer use the word. |
| "heavy formation" | Now "a formation with extra tight ends or a fullback". |
| "shotgun with no back" / "shotgun, no back" | Now "no running back in the backfield" / "empty backfield" (log row 4). |
| slant / dig | Glossed in plain words in Answer 3; dig linked to 04-01. |
| "receivers around the stadium" | Now "sensors mounted around the stadium". |
| pressure | Glossed: "how close the pass rushers were to the passer when he threw". |
| man-to-man in Answer 2 | Removed (Answer 2 rewritten). |
| FTN unexplained | Named and described once in "How strong is each clue?". |
| XFL | "a short-lived spring league". |
| pocket | Glossed in Table 1 and linked to 04-02. |
| "next to" vs "in" the box | Answer 2 now says "in the box" throughout. |
| crack block not linked | Linked to 03-05. |
| calibration | Linked to 15-02. |
| D&D buckets differ from 01-02 | Note added: 01-02 split long into long and very long; one bucket is enough here. |
| T/T and S/SS marker clash in Drill 1 | Tailback relabelled R. The SS moved slightly away from the Sam, and the caption explains S = Sam and SS = strong safety. (The defensive T for tackle is the library-wide convention; it no longer clashes once the tailback is R.) |
| Why does an offset-right back run left? | One sentence added: he takes the handoff moving across in front of the QB, so his path already points the other way. |
| DL "drop into coverage" unexplained | Now in a bullet: a DL sitting back may loop on a stunt (07-01) or drop to confuse the blockers (07-03). |
| Table 2 Pass row: "tells you the coverage" (what?) | Gives the beginner read: both stay deep, or one heads to the deep middle and one comes down. Part 6 names the coverages. |
| "One guard": which, and why? | Explained: the guards are easy to find beside the center, and on many runs they pull to lead (pull glossed, linked to 03-01). |
| Overlapping Run / Short-yardage rows | Short yardage removed from the Run row. The short-yardage row now says it wins over "Run" on third-and-1. |
| Answer 1: why not above the base rate? | New paragraph: the clues aren't independent (they travel together and are already in the 84%), and on short yardage everyone is heavy. |
| Answer 3 dismisses two meanings of a reduced split | Now walks through all three. Crack is unlikely because the run would go away from him; underneath dig/crosser or out-breaking corner are the fits; a slant is the least likely. |
| Answer 3 ignores the two-high clue | New item 3: two-high is six-on-six near the line and pulls you back a notch, which is why the answer is 70–75%, not 80%. The question now lists five clues. |
| Red zone "field shrinks": why? | The back of the end zone caps how deep receivers can run. |
| Play clock shown but unexplained | New paragraph after the five items: late movement happens in the last 8–10 seconds; a quick no-huddle snap denies the defense time. |
| Simulated play doesn't match the hook (no fake) | The analyst's line is now "the safety jumped the short route". The simulated play is rebuilt so the SS bites on Y's curl and Z runs into the space he left (see coach A5/12). The Rams film-room callback to "bit on the play fake" is removed. |
| Hook "early in the fourth" vs 2:41 scorebug | They are the same moment now: third-and-6 at the opponent's 34, 2:41, down three. The simulated play's line of scrimmage moved to the opponent's 34, the scorebug caption says "the moment from the opening", and the scorebug example closes the loop ("the offense took the deep shot instead… a lean is a probability"). |
| Safety depth ranges drift | Uses 10 to 15 yards everywhere, matching 01-03's glossary. Diagrams draw 13, inside that range. |
| Fig 1 camera label misread | Replaced by a camera icon at the left edge, level with the LOS, labelled "main camera (high on this side)". The caption names the icon and adds "$ = slot cornerback". |
| Fig 2 ball covers Z and QB | The chapter now draws the ball smaller and nudges it aside when a player holds it (`draw_frame_ball_aside`). Panel 4's count is computed, not hard-coded. |
| Fig 4: QB hidden; oval 5 at the top edge; badge 7 ambiguous; SS oval unnumbered; invisible step | Ball offset. Window widened to 42 yd. Both safety ovals carry a 7, each with its badge on its own side. Badge 8 sits outside X. The caption says the step is too small to see. Figure is taller (6.9 in). |
| Fig 5A: no LOS/forward; upright two-point; weight not shown | Dashed line of scrimmage with "line forward ►". The two-point figure is redrawn as a crouch (knees bent, hands on thighs). A red dot and arrow mark where the weight rests (even / back foot / hand). |
| Fig 5B title/offset | Retitled "Where the back lines up". Depths corrected (see coach 14) and a 5/7-yard ruler added. |
| Fig 5C three Z's | Caption and in-panel note: "one receiver, three possible spots". Labels corrected (see coach 4). |
| Fig 5D no unit | "yards off the ball" label added. |
| Fig 5 empty band | Figure height cut from 6.0 to 4.75 in. |
| Fig 3 football touches HOME; "AWY" | Ball and text separated. The field position reads "BALL ON AWAY 34". |
| Drill 1 arrow lands on a gap | A bracket now spans the five linemen, and the arrow points to the bracket. |
| Drill 2 ghost too small | Ghosts are 1.5× marker size, filled, with labels. The FS ghost and arrow were added (coach 2). |
| Pandas output clutter | The by-clue table prints with `.to_string()` and named columns. The by-down `Series` print was dropped. |
| Length (~6,800 words) | Cut: the yellow-line anecdote (and its footnote), the All-22 misconception callout (folded into the Madden callout), and the paragraph after the confidence callout (merged into it). Alignment numbers are now pass % everywhere and stated once in prose. "Clue, not a guarantee" was cut from the Fig 5 caption. Net length still grew (~8,500 words of prose and tables by a crude count) because both reviews asked for many new whys (live safeties, logging rules, high hat/low hat, the clue-independence lesson, modern stance details). AUTHORING §2 sets length by what the concept needs; the curriculum's 4,000 is a planning estimate. |
| Alignment numbers repeated six ways | Pass % only. The full numbers appear once in the backfield prose (fn `qbloc`) and once in panel B. The Fig 5 and Fig 6 captions no longer restate them, and the misconception uses 31%. |
| (6) Pause not on screen / no-huddle | New "two warnings" paragraph: call it from the scorebug and log the clue as "sit". |
| (6) Logistics | New rules list: call before the snap and write during the replays; abbreviate; pause if you can; otherwise fill only the shaded columns. |
| (6) Edge cases when logging | "Log what the QB did with the ball": dropbacks (sack, scramble, throwaway, screen) are P; an RPO is whatever he did; a handoff or designed run (sneaks included) is R; skip kneels, spikes and penalties. |
| (6) Which team? | "Pick one team for the half, ideally the offense you know better; don't switch." |
| (6) How visible is a heavy hand on TV? | New paragraph: line close-ups are occasional, so it's a replay clue first (end zone) and a live clue when you get the shot. |
| (6) Which side is the camera; near-side receiver? | New sentences after Fig 1: the near receiver is hidden too (the narrow end of the trapezoid). The side varies by stadium, usually the press box. |
| (6) What does the skycam replay look like? | One-line description added to the angles list. |
| (6) Free All-22 source? | **Declined.** Free sources (team sites, social accounts, writers' clips) change constantly and none is stable or verifiable enough to cite. The text keeps the general pointer, and 15-02 owns the study routine. |

### Coach review

| Finding | Action |
|---|---|
| A1 Answer 2 points the wrong way | Fixed (toward pass, a little; bluff and clock caveats). Same as beginner MF1. |
| A2 Drill 2: no one in the middle | The FS now slides to (14, −1.5), with a ghost and a dashed arrow. Caption and answer say so. |
| A3 Drill 3 LCB covering nobody | LCB moved to (d 6.5, w −8.8), slight outside leverage. **FS cheat not added**: it would be a sixth clue in a drill already teaching clue-weighing; noted for 06-06. |
| A4 Reduced-split meaning | The splits bullets, panel C labels and Answer 3 now follow the coaching convention and 02-02: reduced = crack, underneath dig/crosser, or out-breaker; wide = deep, inside-breaker, quick throw or clear-out, with out-breakers cramped. "Reduced split" links `#gl-reduced-split`. |
| A5 X wide open deep in the shot play | Rebuilt as a coherent Cover 2. Corners sink underneath, and the FS drops to (24.5, −12), on top of X. The SS bites on Y's curl, then chases Z, who catches it with the SS a step late. |
| A6 Play-action/RPO caveat on "line forward = run" | The table's No-idea row teaches high hat / low hat and "fire out but stop at the line → play-action" (fn `idp`, the one-yard ineligible-downfield rule, linked to 04-06 which owns it). A paragraph covers RPOs and screens. The Fig 4 caption is softened. |
| A7 WP "not a judgment about these teams" | Now "mostly about the situation; many models also start from the pregame betting line". Sourced to the nflverse dictionary (`wp` vs `vegas_wp`, verified in the data and the dictionary CSV). |
| A8 Play-action causal framing; LBs not safeties | The film room now says PA attacks the linebackers' eyes: watch their first step, then the safety. The "after a good run" tendency is kept with the Baldwin/Hermsmeyer counterpoint (fn `pa`, the same sources fact-checked in 13-02). |
| B9 Short yardage kills the stance tell; QB sneak | Answer 1 says heavy hands add nothing on short yardage, and the stance section says the tell goes quiet there. Sneak share: 31% of 2025 under-center third-and-1 snaps (`is_qb_sneak`, fn `short`). The tush push is linked to 10-03. |
| B10 Stance modern reality | Rewritten: interior linemen mostly three-point; shotgun tackles often two-point; many edge rushers stand up. New bullets on the tackle's stagger (kick slide, 04-02), a guard tipping a pull (03-01), a team that puts hands down only for runs, and the DL in reverse (stunt, 07-01; drop, 07-03). |
| B11 Two-minute warning | Added to the clock item (linked to 01-01, its owner) and to the worked example. The optional fourth-down note is included with a 13-03 link. |
| B12 Hook vs simulation | Done (see the beginner table). |
| B13 WILL not apexed | `base_play()` puts the WILL at (5.0, −5.5). He drops to (8, −6). The on-screen count stays 16 (re-checked in Fig 1). |
| B14 Card B depths | Shotgun QB/RB at −5.0, pistol QB −4.0 / RB −7.0, under-center RB −7.0. Labels moved down, ylim (−15, 3.5), and a depth ruler added. |
| B15 Two-point figure | Redrawn as a crouch. |
| B16 Drill 3 caption: TE attached | "trips to the right, the tight end attached to the line (Y, H and Z)". |
| B17 Spikes; log row 4 | Spikes are skipped in the log rules and the Sunday drill. Row 4 is "empty backfield, 90%". Course calc for 2025: 95% pass on 2,269 empty snaps; the sheet shows a confidence, not the rate, so no footnote was needed. |
| C18 Fig 4 window and badge 8 | `WIN = (-9.5, 42)`. Badge 8 moved off the numeral to the inside of X. |
| C19 Fig 1 camera label | Replaced by the icon and a label inside the grey (see the beginner table). |
| C20 Fig 3 ball over HOME | Fixed. |
| C21 Fig 10 label near the top edge | `window=(-8.5, 19.5)`. The label is 2.5 yd inside. |
| C22 Fig 4 size | `figsize=(6.5, 6.9)`. |

Library note (no edits to `gridiron/`): `draw_frame` draws the football (1.1 × 0.7 yd, z 11) on
top of the ball carrier's marker, hiding the QB and the receiver in frame strips. This chapter
works around it with a local `draw_frame_ball_aside`. A library option to offset or shrink the
ball when it is held would help other chapters.
