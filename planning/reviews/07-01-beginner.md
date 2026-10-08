# 07-01 The Pass Rush — beginner reader review

Reviewer persona: a casual NFL watcher who has never played and has read everything before this chapter in
curriculum order, including the prerequisites 04-02 (Pass Protection) and 05-01 (Defensive Line Play), plus 04-07,
05-04 and Part 06. I read it start to finish in the PDF (`pdfs/07-01-pass-rush.pdf`, 23 pp, built one minute after
the last .qmd save, so it is current). I rasterized it at 60 dpi, re-rendered pages 3, 4, 6, 8–11 and 15 at 130 dpi,
and checked the source for figure coordinates.

**Overall:** a strong chapter, close to pilot quality. "A race and a fight" is a great spine. The get-off geometry
lands, and the rush-plan triangle is the best idea in it. The pressure-vs-sacks section (the carry-over dot plot
plus the Browns 2024→2025 arrow) is exactly what an analytically minded reader wants. I could do most of the
"You'll be able to…" items, and I got all three drills right before opening the answers. But all three were too easy
(see §5). The problems that matter:

- (a) **The chapter contradicts itself on speed-to-power.** Fig 3 says it beats a tackle who *leans forward*; the
  text says it beats one whose weight is *going backward*.
- (b) **The mush rush can't be told apart from "lanes kept."** Fig 6-left and Fig 7 show the same thing. Fig 7 also
  draws the ends running *around* untouched tackles, while the text says the mush end bull-rushes his tackle straight
  back.
- (c) **The slide-protection strip (Fig 5) doesn't show what the caption says.** You can't see the slide, the RG
  stands idle while the back gets crushed, and the "dotted lines" are hidden under overlapping markers.
- (d) **No benchmarks for the numbers the reader is told to "use."** What is a good get-off, PRWR or time to
  pressure? The worked example's 2.6 s time to pressure falls into a 2.5–3.5 s zone the chapter never explains.
- (e) **Cross-chop and ghost, a whole subsection, have no picture and no "what it looks like on TV."**
- (f) **Length.** About 9,600 words of prose against a ~5,000 target. The Garrett record is told three times and
  the cost of the mush rush four times.

---

## 1. Terms used before they're explained (or never explained)

| Where | Quote | Problem |
|---|---|---|
| Inside rushers (p. 7); Reggie White (p. 16) | "a **club** or a swim the instant they meet the guard"; "a forearm **club** up under the blocker's arm" | Never defined here or in any earlier chapter (grep: no football use of "club" in Parts 1–6). The "hump" is explained *by* the club, so it lands on nothing. One clause: "a club, a forearm swung into the blocker's shoulder to knock him off line". |
| Fig 2 panel 6, Fig 3 panel 1, Madden callout | "He **oversets** for the arc"; "He oversets: inside opens"; "before the tackle had a reason to **overset**" | Not defined in 04-02 or here. I could guess it, but "overset" vs "sets short" vs "sets too deep" needs one line: the tackle's *normal* set depth, and what "over" means relative to it. |
| Answer 3 | "a spin, an inside swim or an **inside rip**" | The rip was taught only as an *outside* finish ("uppercut through his outside arm… the usual finish of a speed rush"). An inside rip is new. Gloss it or drop it. |
| Fig 3 note, "Counter: back inside (spin, swim, **inside move**)" | | "Inside move" reads as a named move. Is it one? |
| Drills 1–2 diagrams | Center labelled **C**, both cornerbacks labelled **C** | A label collision on the same picture. "How to read the diagrams" never introduces C (corner), W, NB, FS, SS or **w9** either; they come from earlier chapters, but the key should say "the drills use the defensive labels from Part 06". Use "CB" for corners. |
| Mush rush (p. 11) | "That defender is called a **spy**, and Third Down has the full picture" | Phrased as if new, but 05-04 already defined *spy* (with a glossary anchor, `gl-spy`). Link the glossary and say "the spy from Linebackers". |
| Long arm (p. 5) | "A long arm is longer than a blocker's punch" | Why? Both men have two arms. The point (one arm locked out with the shoulder turned reaches farther than a two-handed punch thrown square) is assumed. |
| Cross-chop (p. 5) | "brings his **far arm (the one away from the tackle)**" | For a rusher facing the tackle, both arms face him. I think it means the arm farther from the tackle *laterally* (the outside arm for an outside rush). Say "his outside arm". |
| Ghost vs dip | dip: "dropping the shoulder nearest the tackle so the tackle's hands find nothing"; ghost: "dips his inside shoulder and turns it away, so the punch lands on nothing" | These read as the same move. What does the ghost add (timing? no hands at all?). |
| Fig 10 caption vs Fig 1 text | corner = "the moment his hips get **level** with the tackle's"; Fig 10: "the end's hips **get past** the right tackle… a rush 'win'" | The frame shows him *level*, and the code's rule is "deeper than the tackle". Pick one word. |
| Get-off (p. 3) | "scouts time rushers' first steps at the **Combine**" | Minor: probably known, but a half-clause ("the league's pre-draft testing event") costs nothing. |
| Answer 3 | "a **jump set** or a **45-degree set**" | Taught in 04-02, but not linked here. Add the glossary links. |

Everything else I checked was taught earlier or glossed in place: kick slide, vertical set, punch, anchor, pocket,
launch point, set point, slide/man/half-slide, chip, pass-off, A/B/C gap, technique numbers, wide-9, contain, edge
rusher, two-point stance, 3-4, H-back, blind side, FTN/NGS, EPA, hard/quick/silent count, penetrator/looper,
clean-up and coverage sacks, hump.

## 2. Leaps (a missing or assumed "why")

1. **Speed-to-power contradicts itself.** Fig 3 panel 3 is titled "He leans: power opens", and the caption says "he
   leans into his punch, reaching for the rusher". The triangle paragraph says "Power threatens the tackle who reaches
   or leans". But the speed-to-power paragraph, the hook and Answer 3 say it works by "hitting him while his weight is
   still going backward", and the bull rush beats a set "too deep and fast, with his weight already going backward".
   So does power punish a tackle leaning *forward* or one retreating *too fast*? If both, say so. As written, the
   triangle doesn't close either: the tackle's "deep and fast" set is listed as the opening for the inside counter
   *and* for power. Answer 3 then gives both as answers to the same picture. **Fix:** make Fig 3 panel 3 the
   fast-retreat case (weight going back, can't anchor), or explain that a reaching tackle and a bailing tackle are two
   different openings for power.
2. **Mush rush vs ordinary lane discipline.** The rush-lane definition already says the ends "must not run past the
   quarterback's depth" and the interior "pushes the pocket". The mush rush is defined as "the four rushers stay in
   their lanes, the ends stop level with the quarterback". That is the same sentence. The lanes paragraph even
   describes the mush end ("the end who stops at the quarterback's depth is not running the full, fast arc"). The real
   difference only appears in prose on p. 11: the mush end *doesn't try to turn the corner at all* and uses power. Put
   that in the definition and in the figure.
3. **When T-E and when E-T?** The chapter explains each but never says when a defense would pick one over the other.
   Drill 1 then asks "which one". I picked T-E only because it was called "the most common". One paragraph is needed:
   which matchup each one hunts, and where the best rusher should be (the text says "build stunts so their best player
   is the looper", which is a start).
4. **Fig 5: why does the line slide left, and why does the RG do nothing?** 04-02 taught "offenses slide toward the
   most dangerous inside threat". Here the line slides *away* from the 3-technique, and the reader isn't told why. In
   frames 4–6 the right guard owns an empty A gap and stands idle a yard from the back who is getting run over. Why
   doesn't he help? (One sentence: the slide's rules don't let him leave his gap, or he does help in real life.) Also
   say plainly that this is the reverse of 04-02's stunt figure, where the RT *took* the crashing 3-technique: it's
   man/switch there and slide here. Otherwise the two pictures look contradictory.
5. **How does the defense know which way the slide goes?** "Defenses aim stunts away from the slide" assumes the
   defense knows before the snap. From film tendencies? The back's alignment? The center's call? Answer 1 hints at it
   ("defenses study how a team protects in empty"). It belongs in the body.
6. **Inside rushers: "the center is often free to help."** Why is he free? It's the 5-on-4 arithmetic from the
   chapter's own opening (one blocker is spare, and it's usually the center), but the chapter doesn't connect it. That
   connection is also the "why" behind double teams on interior rushers.
7. **The 2.5–3.5 s hole.** The stopwatch rule is "under about 2.5 s is a rush win; past 3.5 s the coverage or the
   QB owns most of it" (p. 14 and the Watch-for-it box). The chapter's own measured example puts time to pressure at
   **2.6 s**, outside the PRWR window (Fig 11), even though the rush was "won" at 1.4 s. So what is a pressure at 2.6?
   Say what the middle band means, or retime the simulation so it lands inside 2.5 s.
8. **"Why pressure beats sacks": the section proves *stability*, not *value*.** It shows convincingly that pressure
   is the better *measure*. The hook, though, claims a no-stat pressure is "one of his best plays of the day". How
   much does a pressure *without* a sack actually cost the offense (EPA per dropback, completion rate, pressured vs
   clean)? 04-02 has a related chart (EPA by time to throw). One number here would close the loop the hook opens.
9. **"How much of a sack belongs to the quarterback"** (objective 5) is answered qualitatively: the QB's conversion
   repeats (+0.33) and the defense's doesn't (0.00). The bullet promises "how much". Either give a share (a variance
   split, or "the gap between the best and worst QB conversion rates is X vs Y") or reword the bullet.
10. **"Repeats far better" with six season pairs.** In Fig 9, pressure rate averages +0.31 and sack rate +0.13. But
    the individual pairs overlap a lot (sack rate's dots run from −0.18 to +0.27, pressure rate's from +0.10 to
    +0.55), and n = 32 per pair gives an SE of roughly ±0.17. An analytic reader will ask whether that's significant.
    Soften to "repeats better" or add a sentence on noise.
11. **The Browns' 41.1% pressure rate** is far to the right of every other team-season in Fig 8. Is that real, or
    charting variation in FTN? A data-minded reader will wonder. One clause on charting noise would help.
12. **Get-off: no scale.** "The fastest are around a third of a second." Then the simulated rushers come in at
    0.5–0.8 s. Is 0.8 bad? What's league average? Without a range I can't "use" the number (objective 6). The same
    goes for PRWR: what's a good edge win rate on ESPN's board?

## 3. Diagrams I couldn't decode, or captions that don't say what to notice

- **Fig 1 (get-off).** The two faint squares nearly touch, so at print size they read as one smear. "0.2 s slower:
  still in front of him" points at a square that is beside the end of the tackle's bar, not obviously "in front". The
  tackle at 1.2 s exists only as a bar. A faint tackle marker at the bar, plus more separation (or a 0.3 s gap), would
  make "level vs in front" visible.
- **Fig 2 (six moves).** *Bull rush* and *long arm* are almost the same picture; the only difference is a short thick
  stroke and the dashed escape path. The swim and rip "curl" arrows can't be read as arm actions at this size. This is
  acceptable for paths, but the caption should say "the arrows show *where* he goes; the arm work is in the notes".
- **Cross-chop and ghost have no figure at all.** That's a whole subsection about hands. A two-panel close-up (the
  tackle's two hands as short bars, the rusher's chop knocking them down, the dip turning away) would make them
  watchable.
- **Fig 3 panel 3** contradicts the text (see Leap 1).
- **Fig 4 (stunts).** The "2" badge sits at the *top* of each loop, so it reads as man 2's starting point. The loops
  run 2–3 yards back into the defense's side; the caption admits it, but I came away thinking loopers step backward.
  The blockers just set straight back, so the "point" (two blockers ending up on the wrong man) isn't shown. In T-T,
  the caption says the 3-technique "crashes across the center's face", but the arrow stops at the C–RG seam.
- **Fig 5 (T-E vs slide).** (i) **I couldn't see the slide.** The linemen barely move left between frames 1 and 3.
  (ii) The RG stands idle in frames 4–6 (Leap 4). (iii) **The caption's "dotted lines in the last frame" are
  invisible:** E sits on top of RT and the 3 on top of R, so the links have zero length. Pull the frame-6 positions
  apart or put the links in frame 5. (iv) Note 6 says "back driven into the QB", but R is still about 3 yards from Q.
  (v) The QB drifts left, and nothing explains it.
- **Fig 6 (lanes).** In *both* panels the ends sail around tackles who never touch them, so the "good" picture looks
  like two beaten tackles. The caption should say the lanes are drawn without the blocks.
- **Fig 7 (mush).** The ends are drawn running *around* the tackles to the QB's depth, the same path as Fig 6-left.
  But the text says a mush end "may bull-rush or long-arm his tackle straight back… without ever trying to beat him
  around the corner". Draw that instead: an end pushing the tackle (dashed, as in Fig 2) from outside in. The
  interior "push the pocket" arrows are tiny stubs; make them visible. The spy's arrow points *toward the line*,
  which reads as rushing, not mirroring.
- **Fig 10/11 (measured rush).** Frame 2 says "all four across the line", but the 1 and the 3 still sit on it. In
  Fig 11, every rusher's distance to the QB *rises* for the first half-second, and the caption doesn't say why (the QB
  is dropping back). The get-off dots for the 1, the 3 and the left end overlap.
- **Drill 3's figure gives the answer away.** A big "?" in the inside gap plus the caption "kicked back hard and
  wide… to take the corner away" is Fig 3 panel 1 again.

## 4. Drag and repetition

- **Length:** about 9,600 words of prose (code excluded) against a ~5,000 target. Candidates to cut or compress:
  - the "Where the moves came from" history (Taylor/Gibbs is retold from 04-02, and Watt/Garrett again);
  - Answer 2, which restates the mush section almost line by line;
  - the long "How to read the diagrams" legend, which could be split so each symbol is introduced with its first
    figure.
- **Garrett's 23.0 and unanimous DPOY** appear in the measuring section, the history section and the Film room.
  "The Browns pressured more in 2024; 2025 was the year the pressures turned into sacks" is told twice (data section,
  Film room).
- **The mush rush's price** ("the quarterback gets longer to throw; the coverage has to hold longer") appears in the
  Fig 7 caption, the cost paragraph, the misconception callout and Answer 2. "Which is why such quarterbacks are so
  hard to defend" appears nearly verbatim twice.
- **"Pass Protection" is linked 14 times.** After the first few, the "as Pass Protection showed" tags become noise.
- **The spin's risk** is explained twice (spin paragraph and Fig 2 note), and the "conversation across a game" line
  twice (Madden callout, Answer 3). Both are minor.

## 5. Can I do the "You'll be able to…" items? (drills attempted before opening answers)

| Objective | Verdict |
|---|---|
| Name moves as I see them, and the mistake each punishes | **Partly.** Speed, bull and spin, yes. On a broadcast I can't tell a long arm from a bull rush or a swim from a rip, and the chapter gives no "on TV it looks like…" cue. The speed-to-power contradiction muddles "which mistake". |
| Explain the rush plan; spot the counter | **Yes**, the strongest section. |
| Recognise a stunt and say what it did to the protection | **Recognise, yes. What it did, only partly:** I can't tell slide from man protection from the couch, and the chapter doesn't say how. |
| Rush lanes, contain, why mush and what it costs | **Mostly**, but I couldn't explain how a mush rush differs from a normal disciplined rush (Leap 2). |
| Why pressure is steadier than sacks; QB's share | **Yes for the first** (excellent). **"How much" for the QB: no number given.** |
| Use PRWR, get-off, time to pressure, and their limits | **Limits: yes. Use: no.** There is no scale for a good get-off, PRWR or time to pressure, and the 2.5–3.5 s band is undefined. |

**Drill 1 (3rd-and-11, empty).** My answer: yes, stunt; long yardage gives the looper time, as the chapter said.
T-E on the right with the ringed 3 and E, aimed at the RG–RT seam. Risks: a quick throw beats it, and contain
shifts. **Right**, but my "T-E, not E-T" was a guess based on "most common". The answer's main caution (if the
slide goes that way the stunt dies) can't be read from the picture, which is fine, but say so.
**Drill 2 (running QB, wide-9).** Mush rush; the wide-9 has the hardest job; the price is time. **Right, and easy:**
the purple ring on the wide-9 answers "who has the hardest job" before I think. I also wondered about the inline TE
(Y) beside the RT and the back (R): will they chip the wide-9, or stay in to block and change the math? The answer
ignores both.
**Drill 3 (the counter).** Inside counter, or speed-to-power. Offense: the guard helps, the tackle varies his set,
chips, quick game. **Right, instantly.** It's a recognition test of Fig 3 panel 1 with the answer drawn in.
Suggestion: show a *different* tackle mistake (say a tackle who sets short and square after being beaten inside) and
make the reader pick the move.

## 6. What I still wonder (the chapter should answer at least some)

1. **Holding.** When a rusher wins, doesn't the tackle often just hold him? How often is holding called, how does it
   show up in pressure and PRWR, and is a "win that drew a hold" counted?
2. **Batted passes and the throwing lane.** When the ball is coming out quickly, what does a rusher do instead (get
   his hands up)? Interior rushers batting passes is a visible pass-rush outcome the chapter never mentions.
3. **Who calls the stunts?** The coordinator in the signal, the line coach, or the linemen themselves at the line
   ("games" checked on the fly)?
4. **Beating doubles and chips.** The best rusher gets slid to, chipped and doubled (the Film room says count it). So
   how does a defense free him, beyond Parsons-style alignment? And how does he beat a chip?
5. **Rush vs run.** A wide-9 speed rusher on an obvious passing down is a run-defense liability on a draw. How do
   rushers avoid getting "run past" by a draw or a screen? (A single line with a link to 04-05 would do.)
6. **Left vs right.** Do the best rushers line up over the right tackle (the QB's blind side for a right-hander)? Do
   modern rushers flip sides by matchup?
7. **Stance and width.** Two-point vs three-point stance for an edge rusher, and what a wider alignment buys and costs
   in get-off and arc length. The chapter uses the wide-9 in Drill 2 but never explains its rush trade here.
8. **The finish.** Strip-sacks (going for the ball instead of the man), and how roughing-the-passer rules shape how a
   rusher is allowed to land on the quarterback.
9. **Rotation.** Why defensive linemen rotate in and out, and whether fatigue shows up in late-game pressure rates.

---

## Revision (2026-10-07)

Revised against this review and `07-01-coach.md`. The fact-check entries are unchanged; every new claim is sourced
(new footnotes `[^epa]`, `[^qbfault]`, `[^gsack]`, `[^schwartz]`, `[^mac]`; `[^prwr]` extended). Each footnote is
referenced once. The build (`build_pdfs.py 07-01-pass-rush --html`) runs with zero errors, 26 pp. I re-read every
figure at 100 dpi.

### Beginner review

| Finding | Action |
|---|---|
| (a) Speed-to-power contradiction | Power now consistently punishes a tackle whose **weight is going backward**. Fig 4 panel 3 is redrawn as "He bails: power opens": the tackle retreats straight back fast, the rusher turns into his outside half, and the tackle is driven back, labelled "weight going back: no anchor". The triangle paragraph now says depth can be gained only two ways: widening (opens inside) or bailing (opens power). Bull-rush text and note: "a high set or one already bailing". "Reaches/leans" is gone everywhere. |
| (b) Mush rush = lanes kept | The mush definition (prose and glossary) now holds the real difference: ends **give up the corner** and drive their tackles straight back from the outside shoulder ("cage rush"). The section opens by contrasting it with ordinary lane discipline. Fig 8 is redrawn per coach A6 (see below). The Fig 7 caption says the arrows show lanes, not the hand fight. |
| (c) Fig 6 (T-E vs slide) | The slide is now visible (every lineman steps left in frames 1–3). The caption gives the reason for the slide (toward the 1-technique in the left A gap, as 04-02 teaches). The RG now helps the center on the 1, and the caption explains why (slide rules point his eyes to the slide side). Final-frame pairs are pulled about 2 yd apart, so the dotted links show. Note 6 and the caption now say "driven back toward the QB, who slides away", which explains the QB's drift. The text contrasts it with 04-02's man/switch figure. |
| (d) No benchmarks | Get-off: best-ever single snaps are about 0.33 s, about 0.5 s is the physical floor from a standstill, the sim runs 0.5–0.8 s. PRWR: when ESPN introduced it, about 22% for the average edge, early leaders 40–47% (Burke 2018). Time to pressure: the 2.5–3.5 s band is defined as shared credit (prose and Watch box). The sim is retimed so time to pressure is 2.4 s, inside the window. |
| (e) Cross-chop / ghost have no figure | New **fig-hands** (two close-up panels; the tackle's punch drawn in dark blue). Added "on a replay it looks like…" cues for both. Also added a "Telling them apart on the broadcast" paragraph for all six moves. |
| (f) Length | Cut the repeats you named: Garrett's 23.0 and DPOY now appear once each (the Film room no longer repeats them), "pressured more in 2024" once, the mush-rush price twice (it was four times), Answer 2 rewritten rather than restated, the long legend split (marks are introduced with their first figure), Pass Protection links 14 → 6, the history compressed (Taylor/Gibbs no longer retold), the Why-it-exists and Madden boxes tightened. **Partly declined:** net prose is still about 11,000 words. The findings in both reviews add real content (hand moves, T-E vs E-T, slide clues, pressure EPA, the QB share, benchmarks), and I didn't want to buy brevity by dropping a "why". |
| Terms: club | Defined inline with push-pull in "Moves are counters to hands" (coach B4). White's hump is now "a club-and-lift". |
| Terms: overset | Defined in "The arc and the corner". |
| Terms: inside rip / "inside move" | Both gone (the old Answer 3 is replaced; the Fig 4 note now reads "spin or swim"). |
| Drill labels (C vs C) | Corners are now "CB"; the legend says the drills use Part 06 labels. |
| Spy | Linked to `gl-spy` as "the spy you met in Linebackers" (05-04). |
| Why a long arm reaches farther | Explained: two-handed square punch with bent elbows vs one locked arm with the shoulder turned in. |
| Cross-chop "far arm" | Now "outside arm" (prose and glossary). |
| Ghost vs dip | Distinguished: the dip lowers the shoulder under hands already reaching; the ghost is timed to the punch, with no hand contact (prose and glossary). |
| Corner "level" vs "past" | The corner is where the hips draw level. The measurement rule is "past the tackle" (half a yard deeper), and Fig 11 shows him visibly past. |
| Combine | Glossed. |
| Jump set / 45-degree set | Linked (`gl-jump-set`; 45-degree goes to 04-02, which has no glossary entry). |
| Leap 3: T-E vs E-T | New "Which one, when?" paragraph: make the best rusher the looper, and aim the looper at the weaker blocker. Answer 1 now gives the reason for T-E. |
| Leap 5: how the defense knows the slide | New paragraph: film tendencies by formation and back alignment, the center's Mike point, late shifts. |
| Leap 6: why the center is free | Tied to the 5-on-4 arithmetic. |
| Leap 7: the 2.5–3.5 s hole | Defined, and the sim is retimed (2.4 s). |
| Leap 8: value of a non-sack pressure | New paragraph, nflverse 2023–25: clean dropback +0.23 EPA, pressured non-sack −0.07, sack −1.77; completion rate 70% clean vs 47% pressured, with a selection caveat. |
| Leap 9: "how much" for the QB | Added the spread among 35 QBs with 200+ pressured dropbacks (13% Bo Nix to 30% Will Levis; middle half 18–23%) and FTN's `is_qb_fault_sack` (about 34% of sacks charged to the QB). |
| Leap 10: "far better" with six pairs | Softened to "repeats better" and added a noise note (±0.17 per pair; the gap is about two standard errors). |
| Leap 11: Browns 41.1% | Added a charting-variation clause. |
| Leap 12: get-off / PRWR scale | See (d). |
| Fig 1 | The gap is now 0.3 s (about 2.2 yd apart), with a faint tackle marker at his set point. The slow rusher's label reads "still upfield of him". |
| Fig 2 | The caption says arrows show where he goes and the arm work is in the notes. The long arm now shows the push from arm's length, with the arm from the rusher's end spot to the driven-back tackle (coach B14), so it differs from the chest-to-chest bull rush. |
| Fig 4 (stunts) | Badges now sit above each rusher's start. DL are drawn at depth 1.6 (the book default is 1.0), and loops are tight hooks. Blockers now show the mistake each stunt hunts (guard follows the 3, tackle chases the end, etc.). The T-T now matches the text (coach A3). |
| Fig 6/7 (lanes, mush) | See coach A1 and A6. The spy arrow is now lateral, two-headed and at constant depth. |
| Fig 10/11 | Frame 2 is a beat later, so all four have visibly crossed. The LE stays in front of his tackle (coach A2). The caption explains why distances first rise. Get-off dots no longer overlap. |
| Drill 3 gives the answer away | Replaced with a different picture: a tackle who sets short and square after being spun inside twice. There is no shading or "?"; the answer is the speed rush. The new answer covers the covered guard (coach B12). |
| Drill 2: purple ring gives it away; Y and R ignored | The ring is removed. The answer now covers the back's likely chip on the LE side, the TE's chip, and the end tightening his alignment (coach B13). |
| Drill 1: slide can't be read | The answer says so explicitly. |
| Repetition (spin risk, "conversation across a game") | The spin risk is stated once. The Madden box is tightened, and Answer 3 keeps the "conversation" line. |
| Wonder 1: holding | One clause in "The arc and the corner" (a tackle's last resort, 10 yards if seen). I added no stats, because I found no sourced number. |
| Wonder 2: batted passes | Added to "Inside rushers". |
| Wonder 3: who calls stunts | Added (the coordinator's call, plus line games checked at the line). |
| Wonder 4: beating doubles and chips | The Donald paragraph covers hands vs doubles, the PRWR double-team rule is added, and the Film room bullet covers how to beat a chip. |
| Wonder 5: rush vs run | One clause on the wide-9's soft spot against draws and screens. |
| Wonder 6: left vs right | Added to the LT paragraph: defenses like a great rusher on the blind side, but many flip sides by matchup. |
| Wonder 7: stance and width | New paragraph on the alignment-width trade. |
| Wonders 8–9 (strip-sacks and roughing; rotation) | **Declined:** both are out of scope here. Roughing belongs to 09-03, and rotation would need sourced fatigue data. |

### Coach review

| Finding | Action |
|---|---|
| A1 lanes: escape through the RT | In the lost panel the RT now rides the end past ("tackle rides him past"). The escape lane runs under the RT/RE pair, past the LOS between the 3 and the E. Labels moved clear, and the window is widened to ±11.6. Caption clauses added, including the right-handed-QB contain priority (B8, also in prose). |
| A2 LE also "wins" | LE waypoints changed per the suggestion, so he stays in front of the LT. The chart caption is now true. |
| A3 T-T description | Used your first version: the 3 goes through the RG's inside shoulder into the A gap, picking the guard and center, and the 1 wraps to the B gap. Caption, prose and drawing agree. |
| A4 Drill 1 LBs and answer | W at (5.0, −6.0) and M at (4.8, 4.6). The answer is rewritten around the spare LG and why the right side. |
| A5 sixty times | Now "thirty-odd times". |
| A6 mush ends beat their tackles | Redrawn: tackles and guards walked back (dashed), ends finish on the tackles' outside shoulders, the cage is drawn through those points, and the spy arrow is lateral. |
| A7 punch in rusher colour | `arm()` gains a `color` parameter. The new bail panel draws no punch; fig-hands draws the tackle's punch in OFFENSE_DARK. |
| B1 silent count | Reworded as suggested. |
| B2 get-off numbers | "Quickest single snaps are around a third of a second", plus the half-second physics floor. I gave no league average, since I found no source for one. |
| B3 long-arm aim | "The outside half of his chest, the near breastplate." |
| B4 club, push-pull | Added. |
| B5 rush half a man; landmark | Both added to "The arc and the corner". |
| B6 dialects, role names, pick technique, T-E wording | All added. The glossary T-E definition is updated. |
| B7 end vs edge | The legend now defines E as an edge rusher (4-3 DE or 3-4 OLB), linked to `gl-edge-rusher`. |
| B8 contain priority | Added (prose and Fig 7 caption). |
| B9 SB sim pressure | Checked rather than assumed. In SB LX FTN charted a blitzer on only 4 of Seattle's 46 four-man rushes, and Macdonald said in Nov 2025 that Seattle does "not run a lot of simulated pressures" (SI, footnoted). The text gives both, with the 07-03 link. The unsourced "most damaging pressures came early" is now an instruction. |
| B10 Garrett film room | Names the play from nflverse: Week 18 at CIN, 4th quarter, 5:16 left, sacking Joe Burrow. Adds Schwartz (Browns DC 2023–2025; Browns.com and AP), alignment and side bullets, and a game-script/wide-front context sentence in the data section. |
| B11 PRWR claim | Softened as suggested. Limits gain the "bull rush that never sheds" point. The double-team treatment is verified (ESPN's 2019 update: beating one of two blockers is no longer a win) and stated. |
| B12 Drill 3 RG | The new drill has a 3-technique on the RG, so the answer says he cannot help. The RG is set, not frozen. |
| B13 Drill 2 | Tighten-alignment line and back/TE chips added. |
| B14 long-arm panel mixed moments | Fixed (see Fig 2 above). |
| B15 stunt depth cheat | DL drawn at depth 1.6 (they were at 1.6 before too; the "2.6" in the review misread `moved(d=)`, which is absolute). The caption now says "about half a yard deeper than the book's other diagrams", and the loops are tight hooks. |
| B16 scatter label collision | Browns 2025 label moved up (`xytext=(9, 6)`, `va="bottom"`) and `shrinkB` raised. |
| B17 Watch-for-it protection bullet | Added ("Where is the help?"). |

**For other agents and gridiron (nothing in gridiron/ was edited):** the chapter's local `arm()` helper now takes
`color=`. `Player.moved(d=...)` sets an *absolute* depth; worth a docstring line, because the coach misread it.
