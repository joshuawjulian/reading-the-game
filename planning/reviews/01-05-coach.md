# Coach / film review: 01-05 The Pre-Snap Phase

Reviewer role: NFL coach and film analyst. Checked the qmd as of 2026-10-06 14:29 and the PDF built at 14:30.
I rasterized all 20 pages at 70 and 150 dpi into `_pdfbuild/01-05-coach/` and cropped and inspected every figure
(`c-fig1/2/6/8.png`, `top-11/12/14/16/17/18.png`).

**Overall:** this is a strong chapter. The rules are accurate: the one-second set, shift vs motion, motion parallel or
away, a lineman's hand down, offside as a live-ball foul vs encroachment and NZI as dead-ball fouls, defensive
disconcerting signals, and the illegal-shift false start inside two minutes. The free-play logic, including the
interception case, is exactly right. The film rooms (Rodgers, the Eagles' home silent count, Manning, Purdy) are well
chosen and fairly characterized. Two pieces of **football logic are wrong**. One is the Mike-ID figure: the defense's
"late move" does not break the protection as drawn. The other is a factual slip in the shift text: the formation is
not a mirror image. Several diagrams also need cleanup for realism and collisions. The list below is in priority order.

---

## A. Must fix (football is wrong or misleading)

### A1. Mike-ID figure, right panel: the Mike walking into the A-gap doesn't break the declared protection (fig-mike-id)
Panel 1 assigns **C → MIKE** (the five linemen block the four down linemen plus the Mike, and the back takes the Will).
In panel 2 the Mike walks into the right A-gap. That is now the **center's own gap**, so the protection is *better*
off and nothing needs re-declaring. Any line coach will spot this. The caption ("protection was set against the old
picture, so the QB must re-declare") and the text ("changes the arithmetic") describe a problem the picture doesn't
show.

Fix: make the late move create a threat the declared protection can't handle. Pick one:
- **(preferred) Add a seventh potential rusher.** After the ID, the nickel (`NB`/"$") walks down to the edge at about
  (d 1.5, w 7.5), outside the RT, and/or the SS rolls down. Now 7 can rush against 6 protectors (5 OL + RB). Caption: "now
  seven can rush against six blockers. The QB re-IDs (slides the protection toward the new threat and gives the back
  the other side) or knows he must throw 'hot' to the receiver the free man left."
- **Double A-gap mug.** The Mike *and* the Will both walk into the two A-gaps. The center can block only one, and the
  back has to step up to the other, so the edge is short. This sets up 07-02's "A-gap mugs" forward reference
  directly.

In either case, change the text paragraph after the figure from "a linebacker walking up into the A-gap changes the
arithmetic" to the real reason: the defense adds a rusher, or moves the man the protection counts from, *after* the
call.

### A2. Mike-ID figure, left panel: the pass-pro assignments are drawn as run blocks
`p.block(...)` draws solid lines that drive forward. The C's line runs 5 yards upfield to a linebacker who hasn't
rushed, and the RB's line passes *through* the LG/C to reach the Will. In pass protection, linemen set backward. The
C has the Mike **only if he rushes**; otherwise he helps on the nearest DT. The back has the Will **if he comes**;
otherwise he releases ("check-release").

Fix: replace the block lines with responsibility markers. Use thin dashed "if he comes" leaders from each blocker to
his man, or small tags ("C: M if he rushes", "R: W, else release"). If you keep `block()`, give the OL short
**backward** set paths (`pts=[(-1.2, dw)]`, as fig-defense-moves already does) and draw the assignment with a dotted
leader instead.

### A3. Shift text: the result is not a "mirror image" (fig-shift and text)
Before the shift the formation is 2x2: X (on the line) and H (off) to the left, Y (attached) and Z (off) to the right.
H never moves. After the shift it is **3x1**, with X, H and Y to the left and Z alone. So "The formation that results
is the mirror image of the one the defense first lined up against" is false.

Fix, either way:
- Text: "The tight end and the strength move to the left, and the formation becomes three receivers to the left (trips)
  with the tight end attached." Or
- Make it a true mirror: also shift **H** from (−1.5, −10) to (−1.5, +10) as a fourth mover, so the result is 2x2 with
  the TE on the left. The trips version is the better teaching picture, because it also changes the passing strength.
  I would keep the picture and fix the sentence.

### A4. Kill-call drill 2: the safety rotates down to the **backside** of the run (fig-predict-kill + answer)
The huddle call is "a run to the **left**", but the SS walks down on the **right**, over Y. Coaches count the box
**by halves, toward the play side**. A safety rotating down to the backside of a run left is the cutback/backside
player, and many run-game coordinators would *keep* that run, because the extra man is on the wrong side. As written,
"most quarterbacks kill it" will draw objections from coaches.

Fix: either make the huddle call "a run to the **right**" (toward Y and the walking safety) or walk the **FS** down on
the left, inside H, at about (6.5, −5). Add one sentence to the answer: "Quarterbacks count the box toward the side
the run is going; a seventh defender on the backside matters less."

---

## B. Diagram realism and readability

### B1. fig-shift: X and Z's moves are invisible, and the reason they move isn't taught
X steps off and Z steps up by under one yard (about 9 px in print), with no trail or label. In print the reader sees only Y
moving, and the strip label claims "Y, X and Z move together".
- In the −2.6 s and −1.4 s panels, add small tags or ghost outlines: "X steps off", "Z steps up".
- In the text, say **why**. Once Y attaches on the left, X on the line would "cover" him and make him ineligible, and
  the right side would have no end man on the line. Stepping X off and Z on keeps seven on the line with Y eligible.
  This is the most coach-like detail in the whole shift, and it previews 02-02.
- Name it: coaches call this a **TE trade** ("Y trade").
- Y's path behind the line at d = −1.9 nearly touches the under-center QB in the −2.6 s frame. Drop that leg to
  d ≈ −3.0.
- Optional realism note in the text: many defenses don't run the Sam and SS across the field against a trade. They
  **flip/swap labels**, so the linebacker already on the new strong side becomes the Sam. That matches the
  "Mike is a label" idea later in the chapter. One sentence would do: "some defenses travel, some just swap names."

### B2. fig-legal-motion: the dots show the start, but the caption says "the moment of the snap"
Every mover is drawn at his **starting** spot, with an arrow to where he's heading. Change the caption to "each dot is
where the player started; the dashed arrow is where he is moving at the snap." The **"one at a time"** panel looks
identical to the **"two men moving"** flag panel apart from the 1/2 numbers. Draw H **at his stopped spot**
(−1.5, −5.6), with a ghost outline at the start and a small "stopped" tag, so the difference is visible.

### B3. fig-kill-call: run blocks are illegible; pass side throws into the rolled-down safety; the RB has no job
- **Left panel:** the six run-block stubs are 1.2-yard lines buried under the DL squares, and the T/E rings on the
  right overlap. The RB arrow runs through the left A-gap on top of them. Draw each blocker to a named defender (for
  example, LT→E, LG→T, C→W, RG→T, RT→E, Y→M, or whatever your run is) with `block(target=...)`, or drop the block
  lines and shade the run's aiming point. Nudge the right DT to w ≈ +1.8 so its ring stops overlapping the end's.
- **Right panel:** slant/flat goes to the right, exactly where the SS just rolled down. Against a safety rotating
  down, the coached throw is **away** from the rotation. Either have the QB's side be the left (hitch/out), adding a
  tag "throw away from the rotated safety", or move the walk-down to the left.
- The H quick-out (3 × 4.5) ends right on X's hitch landmark. Space it: X hitch at 5–6, H speed-out at 2–3 yards
  breaking to about w −17.
- The RB stands still. In the kill-to-pass he should **pass-protect** (`p.block("RB", pts=[(1.0, -1.5)])`). Then add
  the clause "with seven in the box, the ball comes out before a seventh rusher can arrive." That is *why*
  quick game is the standard kill.

### B4. fig-defense-moves (+1.1 s panel): the four rushers have run *through* the offensive line
At +1.1 s the E/T/T/E squares are drawn **behind** the OL circles (d ≈ −2), overlapping them, so it looks as if all
four rushers beat their blocks in one second. Stop the rush at the blockers' faces: for example `rush(..., speed=1.5)`,
or rush paths that end at d ≈ −0.8, about half a yard in front of each set lineman. Also:
- At the snap frame, the M box overlaps the T boxes in the A-gap. Put M at d ≈ 1.6 so he sits just above.
- The left CB box at +1.1 s sits on the painted "40". Use `drop_numbers` or shift the window slightly.

### B5. fig-predict-free: defense is a base 4-3 with soft corners on fourth-and-1
On fourth-and-1, a defense is in a short-yardage front with 8–9 in the box and pressed or tight corners, not base
4-3 with corners at 7 yards and the SS at 7. Bring the SS to about d 4, play the CBs at about 3 yards off, and add
"short-yardage defense" to the caption. That also makes the answer's point stronger: a deep shot against a crowded
box is exactly the shot a defense never gives you otherwise.

### B6. Minor collisions
- fig-neutral-zone, false-start panel: the "neutral zone (drawn ~2x)" label touches the left E box. Move it to
  about (3.3, −6.2) or lower.
- fig-predict-kill: the "$" square sits against the painted "30". Drop the numbers or shift NB to w −9.
- fig-predict-shift: the right T square and E square straddle a hash tick ("T -E"). Cosmetic only.

---

## C. Text: accuracy and missing nuance a coach would insist on

1. **"No coach can talk to any player" (Fifteen seconds).** Only the **radio** goes dead at :15. Hand signals and
   signboards from the sideline stay legal right up to the snap, and defenses get late checks in exactly that way.
   Change it to "no coach can talk to any player *by radio*; signals from the sideline are still legal, but the
   decisions are now mostly the players'."
2. **"Offensive linemen block better than you'd expect when they're outweighed" (Cadence).** NFL offensive linemen
   usually **outweigh** the men across from them (OL around 310–320 lb, edge rushers around 250–270). Rephrase:
   "…it's a big reason pass rushers who time the snap well, and get off the ball on the center's first twitch, are so
   valuable."
3. **"Linemen who have put a hand on the ground are now locked in place" (Set).** The absolute rule covers
   **interior** linemen (tackle to tackle). A TE in a three-point stance may not move abruptly, but he isn't under
   the same "any movement" rule. Say "interior linemen", as the foul section already does.
4. **Audible list order.** The intro says "four terms, from most freedom to least", but the list runs general →
   check → kill → check-with-me, and calls check-with-me the one that "goes furthest". Change the intro to "from least
   freedom to most" (after the general term), or reorder.
5. **"The kill call… is usually a choice between a run and a pass."** Change "usually" to "often". In the NFL, kills
   are just as often **run-to-run** (flip the run to the light side, which some teams call "opposite" or "flip") or
   **pass-to-pass** (a man-beater paired with a zone-beater). One sentence would fix it.
6. **Terminology dialects.** The spec asks for them, and the chapter only says "every team uses its own words". Add a
   short line or small table. Kill (Shanahan/McVay trees and many others); **"Can"** (the Holmgren and Gruden West
   Coast term for "run the other one"); **"Alert"** (a tag that says "if you get this look, take this shot");
   **check-with-me** (Manning's Colts). For protection direction, many teams use L- and R-words such as "Lucky/Ringo"
   or "Liz/Rip". Defenses check too ("trips check", "Mable" and similar).
7. **Silent count description mixes two systems.** If the center is "looking back between his legs" (shotgun), he
   sees the QB's foot lift himself, and no guard tap is needed. The **guard tap** is used when the center keeps his
   eyes up on the defense (to make the line calls) and the guard, who can see the QB, relays the cue. Describe them as
   two common versions. Say the line keys the **ball/center's head**, and note the snap comes a set number of beats
   after the head comes up.
8. **Kill call costs.** Add a line on the protection side. When a run is killed to a pass, the TE who was a run
   blocker becomes a route runner, so the count of blockers changes too (see B3).
9. **Motion as a man/zone tell.** It's well hedged. Add the one modern trick coaches would name: in man coverage many
   defenses now **"bump"** (the defenders slide over and exchange receivers, with nobody running across the
   formation), so "nobody followed" no longer reliably means zone. The forward link to 02-06 can carry the rest.
10. **The free play needs a fast center.** Free plays from a defender jumping don't happen by accident. Centers and
    QBs are coached to **snap the ball the instant a defender jumps**, before he can get back. Rodgers' twelve-men
    free plays were mostly **tempo** (snapping while the defense was mid-substitution), not cadence. Worth one sentence
    in the film room, because the chapter currently ties them all to the hard count.
11. **Eagles film room tie-in (optional).** FACTS-current §4 records that after the 2025 tush-push vote failed, the
    league **tightened officiating guidance on false starts and alignment** for that play. That is a good one-line
    coda for this chapter. The tush push lives entirely on the snap-count head start, and the league chose to police
    the pre-snap part.
12. **fig-fouls-by-situation caption.** Third down is also when crowds are loudest. Part of the third-down rise in
    false starts is noise, not hard counts. Add "and crowds are loudest" to "when the snap count matters most".
13. **Packers data sentence.** "less often than the median team" is followed by "0.61 for the league as a whole".
    Use one comparison (the league average) consistently.
14. **Predict 1 caption.** "Second quarter, game clock running" makes the reader wonder about the inside-two-minutes
    exception the answer then raises. Write "8:30 left in the second quarter" so the base answer is unambiguous.
15. **Rules elsewhere (optional "Go deeper").** The Canadian game allows backfield players to be in motion **toward**
    the line at the snap. One sentence would make the NFL's "never toward it" rule feel like a choice rather than a
    law of nature.

---

## D. What's right and should not change
- The one-second-set history (Rockne box, the 1927 committee) is accurate and is exactly the right "why".
- The rule statements in the four-fouls section, and the free-play answer (accept on an interception, 5 > 1 for the
  first down, NZI kills the free shot), are correct.
- The illegal-shift answer is correct: it's a live-ball foul, the defense chooses, and inside two minutes it becomes
  a false start with a runoff.
- The fig-defense-moves concept (two-high → SS buzz + Mike mug → 4-man rush with FS rotating to the middle, a
  Cover 3 bail) is a real, common simulated-pressure picture. Only the rush depth (B4) is wrong.
- Two animations, both with frame strips that tell the story in print. Timing is sensible (offense set ≥ 2 s before
  the snap; defense finishing at −0.9 s).
- The film rooms are accurately characterized and well sourced.
