# 09-04 Officiating, Replay, and the Rules of the Ball: coach / film-analyst review

Reviewed: the chapter source plus the rendered PDF `pdfs/09-04-officiating-replay-and-rules-of-the-ball.pdf`
(built 2026-10-08 03:06, the same time as the qmd). I looked at all 15 figures at 110 dpi.

Overall: strong and mostly accurate. The officiating mechanics, catch rule, down/fumble order, backward-pass
test, grounding rule, Hochuli/tuck/Holy Roller history and the announcement grammar are all right in
substance. The problems are (1) one internal factual contradiction (Jesse James), (2) a replay flowchart
whose logic puts things in the wrong order, (3) two diagrams whose key moment doesn't read in print
(grounding frame strip, dropped-screen predict), and (4) several nuances a coach would add. Ranked below.

## A. Must fix (wrong or misleading)

1. **Jesse James location contradiction (catch history bullet, ~line 781).** The body says "James caught a
   pass at the 10, went to a knee, and lunged"; the Film room says "goes to a knee at about the 1". The 10 is
   where the *snap* was (first-and-10 at the NE 10). He caught it inside the 5, went to the ground **untouched**,
   and lunged across. Fix the body bullet to "caught a short pass inside the 5, went to a knee untouched...".
   Add the "untouched" point: it's the reason he wasn't down by contact and could lunge at all, a perfect
   bridge to the down-by-contact section.

2. **fig-replay-doors flowchart order is wrong.** As drawn, "Scoring play/turnover/try or inside 2:00?" is
   asked first, so a holding call at 1:30 routes to "BOOTH REVIEW"; and replay assist is reachable only for
   plays that are *not* reviewable rulings, the opposite of reality (assist mostly works on reviewable,
   objective facts: catch, down, spot, in/out). Restructure:
   - Q1 "Is it a reviewable ruling (catch, down, in/out, spot at line to gain/goal line, recovery, forward/
     backward pass...)?" No -> "Call stands (holding, PI...)" *unless* it's a flag on the replay-assist list
     (side lane).
   - Q2 (yes) "Score, try, turnover, or inside 2:00 / OT?" -> BOOTH; else -> COACH'S CHALLENGE (needs a
     timeout).
   - Draw REPLAY ASSIST as a vertical side band spanning both outcomes ("can fix objective facts on any
     play; can wipe out a listed flag"), and CONSULT (2026) as a separate side note for ejections.
   Also add "team must have a timeout" to the challenge box.

3. **Booth-review list: "every ruling that the offense came up short on fourth down" (Booth review section,
   glossary "Booth review", footnote [^challenges]).** I don't recognise a failed fourth-down spot as an
   automatic booth trigger in Rule 15, and coaches routinely challenge fourth-down spots outside two minutes.
   Fact-checker must confirm against the 2026 Rule 15-1 text; if it can't be confirmed, delete from all three
   places.

4. **"Because these are turnovers when ruled fumbles, the booth reviews every one of them" (Pass or fumble).**
   Only true when the field rules a fumble *recovered by the defense*. A strip-sack the offense recovers is not a
   turnover; a play ruled **incomplete** on the field is not a turnover either, so outside 2:00 the defensive
   head coach has to challenge it (or replay assist steps in on the possession fact). That is exactly the
   "coach grabs his flag on a strip-sack ruled incomplete" moment fans see. Rewrite: "When the field rules a
   fumble the defense recovered, the booth reviews it automatically. When the field rules incomplete, the
   defense's coach usually has to throw the flag."

5. **fig-grounding-anim: the story doesn't read in print.** At +2.1 s ("outside: exception on") the QB disc
   sits on the box edge, ball just outside; at +2.9 s ("back inside") he is still on the edge (w ~ 4), and only
   barely inside at +4.3 s. A reader can't see out-then-in. Fix in the chapter code: extend the escape to
   w = 8 (`sp.path("QB", [(-2.0, 0.0), (-2.8, 8.5), (-1.0, 1.5)], ...)`) and pick frame times where he is
   clearly outside (~2.4 s, w >= 6.5) and clearly inside (~3.1 s, w <= 2.5); throw after that (T_THROW ~3.4).
   Optionally draw a small ball marker in flight in panel 4 (the ball is invisible there; only the landing X
   shows).

6. **fig-predict-screen: H looks like a backfield alignment, and the nickel's path misses the ball.**
   H is drawn standing 6 yards deep at w = -7 with no route trail, which reads as an odd pre-snap alignment.
   Draw H at his slot alignment (about d = -1, w = -8.5) and give him a bubble path bowing back to the catch
   point (-6.2, -7). The $ path goes (3.5,-8.5) -> (-6.8,-8.2), two yards wide of the ball's X at (-7.3,-6.0);
   route him through the X: `ps.path("NB", [(-7.0, -6.3), (-11.5, -5.0)], absolute=True)`. Also R and Q discs
   touch/overlap at the release line: move R to w = -1.8 or w = +1.8 clear of Q.

## B. Should fix (diagram realism and collisions)

7. **fig-predict-pylon offense is not a real goal-line picture.** Only four linemen (no LT), QB at -2.8
   (neither under center at ~-1 nor shotgun at -5; pistol is ~-4). Add the LT at w = -3.2, put the QB under center
   (d = -1.0) or in the gun (d = -5.0) with the RB beside/behind accordingly, and add a TE. The punch: the
   safety comes from the inside (w = 9 -> 13) and punches a ball carried in the runner's *outside* arm, which is
   physically awkward; either have the cornerback (outside) make the punch or caption it "as he extends the
   ball toward the pylon" (which also matches the answer's moral). The C square sits on the fumble X/ball path;
   nudge C to (3.6, 16.0).

8. **fig-crew-moves (frame strip).** (a) Panel +2.6 s: WILL "W" and nickel "$" labels overlap at about
   d = 8, w = -4; offset the NB drop. (b) The caption says the ball goes "to the receiver on the right sideline", but
   Z catches it on the numbers (w ~ 18, eight yards from the sideline); say "down the right side" or push the fade to
   w ~ 22. (c) "Only from there can they judge whether the pass was thrown from behind it": soften. In NFL
   mechanics the wings also read their receivers through the first 5-7 yards, and the line judge usually keeps
   the beyond-the-line responsibility while the down judge releases earlier. "Both wings frozen on the line
   for 2.6 s" overstates it. Suggest having the DJ start drifting at ~1.2 s and the LJ hold.

9. **fig-tackle-box.** QB B has no rusher near him, yet grounding needs "imminent loss of yardage". Add a
   defender closing on B (for example D at (-6.0, 9.5)) so throw 4 is honestly grounding. Also add a line: the box is
   set by where the **tackles** lined up; a tight end (Y here at w = 8) does not widen it. Readers will ask.

10. **fig-lateral.** H and R are drawn at their catch points with no paths, so H looks like he's aligned 5 yards
    deep beside the QB. Draw H from the slot with a bubble path to (-5.4, -7.5), and R from his gun alignment with a
    pitch-relationship path, as in point 6.

11. **fig-measure, left panel.** The blue "line of scrimmage" sits 3 yards behind the ball. That is the previous
    snap's line, not the line of scrimmage now. Relabel it "where the last play started" or drop it. The ball is
    nearly invisible at that scale; draw it 2-3 times bigger (it's a schematic) or add a leader line from "the ball".

12. **fig-predict-sideline.** The FJ disc sits about 4 yards out of bounds. On a sideline catch a deep wing does work
    from the sideline, but 1-2 yards off is more typical: move him to w ~ 25. Fine otherwise; the toe-tap dots and
    labels are clear of the edges.

13. **fig-fumble-oob.** In every panel the fumble X sits on top of the defender square "D"; offset D by about 1 yard
    so the X reads. Otherwise correct (forward out -> spot of fumble; into EZ and out -> touchback; backward out ->
    out-of-bounds spot).

14. **fig-crew.** Correct and clean: referee on the right (a right-hander's throwing arm), SJ on the DJ's side,
    FJ on the LJ's side, BJ deepest, wings off the field on the line. No change, except optionally
    showing the chain crew on the DJ's sideline, since the text keys the DJ to it.

## C. Nuances a coach would insist on (add a sentence each)

15. **Down by contact: touched while on the ground.** A runner who slips untouched isn't down, *but if a
    defender touches him while he's on the ground, he is down*. Defenders are coached to "touch him down". Add to
    the paragraph and to the bottom row of fig-down-fumble ("NOT DOWN unless touched while on the ground").
    Same idea as the glossary "Down by contact" entry; amend it too.

16. **Predict 2 answer: the first review question is the plane.** Before "did the knee go down first", the booth
    asks whether the ball **broke the plane (or touched the pylon) in his possession before the punch**; if so,
    it's a touchdown. Also note that a loose ball that hits the pylon is out of bounds in the end zone -> touchback.

17. **10-second runoff.** A replay reversal (or an offensive foul such as intentional grounding) that stops a clock that would otherwise have been running, inside the final minute of a half, brings a
    10-second runoff. It is directly relevant to the hook and to Predict 1 (here: no runoff, because the receiver went out
    of bounds and the time is over 1:00). One sentence plus a forward link to 10-04.

18. **Forward progress and the clock.** A runner whose progress is stopped in bounds and who is then driven out
    of bounds: the clock keeps running, because the play ended where progress stopped, in bounds (late in a
    half the officials stop it briefly to re-spot the ball and then restart it on the ready). Good tie to 10-04; one sentence in the forward-progress paragraph.

19. **Illegal forward pass: the whole body.** The LJ "beyond the line" call: a pass is illegal only if the
    passer's **entire body** is beyond the line at release. It's the call fans see on scrambling QBs. One clause in the
    backward/forward section.

20. **Illegal challenge flag on an automatic review.** Since 2013 (after the Jim Schwartz Thanksgiving 2012 play)
    a coach who throws a flag on a play the booth reviews automatically is charged a timeout (or 15 yards), but
    the play is still reviewed. Pre-2013 it made the play unreviewable. It's a great "why" story for the
    challenge rules, and the Predict 1 answer already half-states it.

21. **Crews in the playoffs.** "Each referee leads the same crew for a season" holds for the regular season
    only. Playoff crews are assembled from top-graded individuals, and the league reshuffles crew members
    between seasons. One clause; it also helps explain why year-to-year crew correlations are weak.

22. **Crew-correlation wording.** The year-to-year correlation range runs up to 0.76 in one pair of seasons, which sits
    oddly with "the ranking doesn't hold". Say "usually weak (median 0.28), occasionally strong".

23. **Umpire positioning history (footnote [^umpire] and body).** I recall the 2010 rule also returned the umpire
    to the defensive side in the last **two minutes of the first half** (not only the last five of the game), and
    the "since 2023 on the defensive side for FG/PAT" claim rests on Wikipedia alone. Fact-checker should confirm
    both or hedge ("in the closing minutes of each half").

24. **Replay-assist chronology vs FACTS-current §6.** FACTS verifies only the 2025 flag list and the 2026
    consult wording. The chapter's "since 2021" start and the "2024 powers over roughing, grounding, hits out of
    bounds" rest on one ESPN and one CBS link, and the spec itself said "introduced 2023, verify". Not a coaching
    error, but flag it to fact-check, because it appears in the description, the glossary, the body, the takeaways
    and footnote [^assist].

## D. Film-room examples

- **Dez Bryant (2014 DIV) and Jesse James (2017):** well chosen and correctly characterised (Bryant was a
  Green Bay challenge at 4:42; James was a booth review under two minutes). Fix the James location (A1).
- **Seferian-Jenkins (2017 Wk 6):** correct and the best real example of the touchback rule. Optionally add
  that the controversy was whether he *re-gained* control before going out of bounds in the end zone; that's what
  made it infamous.
- **Hochuli 2008:** accurate. The film-room line "his arm never comes forward with the ball" is slightly strong:
  the ball slipped as his arm *began* forward. Say "the ball leaves his hand before his arm is really moving
  forward" so readers don't go looking for a stationary arm.
- **2025 cameras:** fine as a generic watch-for-it.
- Optional addition: a recent grounding-from-outside-the-pocket throwaway or a 2025 replay-assist flag wipe
  (for example a face-mask flag picked up), so replay assist has one concrete film example. Currently it has none.

## E. Gridiron use

Sensible. Hand-built Players for the teaching plates, simulated tracking (labelled "simulated tracking in
Big Data Bowl format") for both frame strips, at most two animations. Custom helpers (official discs, tackle box,
scene/frame-strip engine) live in the chapter, not in gridiron/. Nothing needs to move into the library, but a
reusable `official()` marker and `tackle_box()` would serve 10-04 and Appendix E: note for the library owner.
