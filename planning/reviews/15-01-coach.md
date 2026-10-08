# 15-01 Watching Live — coach / film-analyst review

Reviewer stance: veteran NFL coach + film analyst. Checked the text against the charted data for
`2025_21_LA_SEA` (pbp + participation + FTN, pulled in the container), and looked at every figure
in `pdfs/15-01-watching-live.pdf` (rasterised at 110–220 dpi under `_pdfbuild/15-01-coach/`).

**Verdict:** this is a strong capstone. The order-of-visibility idea is right, the drive is well
chosen and matches the charting snap for snap (personnel, alignment, backs, motion, no-huddle,
box, rush, coverage label, time to throw, route, air yards and YAC all check out), and every
formation is legal: seven on the line, and no covered tight end or slot. Fix the items below
before publishing. They are ordered by importance.

---

## A. Technical errors (must fix)

1. **Safety width and the NFL hash do not match.** The text in "The tells catalogue" says
   "A two-high safety standing on the hash or outside it has a deep half or deep quarter … A
   two-high safety cheated inside the hash, eight yards or fewer from the middle, *can*". NFL hashes
   are 3.1 yards from the middle of the field (06-01 says so, and the plate draws them there). A
   safety "on the hash" is therefore *pinched*, and a safety 8 yards from the middle is well outside
   the hash. The numbers fit high-school hashes, not NFL ones.
   **Fix:** "A two-high safety at normal width (a few yards outside the hash, roughly 8–10 yards from
   the middle, around the top of the numbers) is a half or quarter player and can't reach the post
   in time. A safety pinched to the hash or inside it (within ~3–5 yards of the middle) can." Make
   the same change to the plate key 10 ("Deep and on or outside the hash") and to table row 10.

2. **The leverage rule for inside leverage is backwards.** Plate key 9, table row 9 and the
   "Leverage points at the help" paragraph all say "inside leverage: help is over the top or
   outside" and "a corner with inside leverage against two-high may have a safety over the top and
   outside." A defender almost never has help *outside*. Inside leverage means one of two things.
   It can mean there is no help inside, so he takes away the quick in-breaker himself and uses the
   sideline as his help (Cover 0, much press-man Cover 1). Or it can mean trail technique with a
   safety over the top (2-Man).
   **Fix:** "Inside leverage: usually man: no help in the middle (Cover 0 / press Cover 1, the
   sideline is his help), or trailing with a safety over the top (2-Man)."

3. **"Why does a screen beat a blitz" describes the wrong kind of screen.** "A screen deliberately
   lets the rushers through to put the ball where they came from" describes a slow RB or
   tailback screen. Snap 6 was a perimeter screen: thrown at 0.7 s, caught 4 yards *behind* the
   line (FTN `SCREEN`, read `DES`). It beats a blitz by numbers and leverage. The Will who blitzed
   is one fewer defender on the perimeter, so three Seattle players to that side (X, Y, H) face two
   Rams defenders (the corner and the nickel), and the ball is out before the rush matters.
   **Fix:** rewrite the paragraph in those terms. Keep "every extra rusher is a defender who isn't
   covering anyone". Drop "lets the rushers through". The fig-snap6 caption's "What to notice" is
   already close to the right idea.

4. **Predict 2 answer: "both mugs drop and four rush" is not a creeper.** If the four down linemen
   rush and both mugged linebackers bail, that is a *bluff* (a mug-and-bail with ordinary coverage
   behind it). A simulated pressure or creeper means a second-level player rushes *and* a lineman
   drops, so the rush is still four but comes from unexpected places.
   **Fix:** "the realistic menu is: both mugs bail and the four linemen rush (a bluff); one mug comes
   while a lineman drops into his spot (a [simulated pressure], the creeper of Zone Blitzes); one
   mug comes and one drops (five rush); or …".

5. **The "almost never rushes six" claim needs a qualifier** (step 8 and Predict 2). Rushing six with
   two safeties still at 12 yards is rare. Six-man pressure itself is a real third-down call
   (Cover 0). The point is that Cover 0 *requires* the safeties to come down, so the safeties give
   it away.
   **Fix (one sentence in Predict 2):** "Six can come only if both safeties drop into man-to-man
   coverage (Cover 0), and they have to walk down to do it. If they're still at 12 when the ball is
   snapped, six isn't coming."

6. **The fig-snap9 strip draws the wrong rusher getting home.** The play-by-play desc ends
   `[91-K.Turner]`, so Kobie Turner, an *interior* lineman, hit Darnold. The figure has the SDE beat
   the RT around the edge. The caption calls "which rusher got home" illustrative, but we know who
   it was.
   **Fix:** let the RT block the SDE normally (`protect`). Have the SDT win through the B gap (e.g.
   `p.rush("SDT", pts=[(-2.0, 0.6), (-4.6, -0.3)], speed=3.6)`) with the RG "beaten"
   (`p.block("RG", pts=[(-1.4, 0.5), (-2.4, 0.4)], speed=1.5)`). Change the caption to "interior
   pressure (charted: Kobie Turner)". This also clears the label collisions in A7.

---

## B. Diagram fixes

7. **Label and marker collisions in the frame strips** (print versions):
   - **fig-snap6, frame 4 (+3.2 s):** the blitzing **W sits on top of Q** at the bottom. At the
     catch point, the **CB square, FS square, ball and H's ring overlap**. Fix: stop the WILL's rush
     short (e.g. `p.rush("WILL", pts=[(-3.5, 0.6)], speed=5.0)`), or use a frame at ~2.6 s. Also
     end the LCB and FS 1–2 yards apart and short of H. The charted tackler was Omar Speights, an
     *inside linebacker*, so it is more accurate to let the MIKE make the tackle and keep the
     corner and safety a step away.
   - **fig-snap6, frame 4:** X has drifted 6 yards away from the corner he was supposed to
     block. On a perimeter screen the corner is X's block. Keep X engaged (`p.block("X",
     target="LCB")` already exists, so the LCB's late `drop` is probably pulling the corner out of the
     block; end the LCB's path at the block point).
   - **fig-snap9, frame 2 (+1.6 s):** the nickel's **$ square sits on H's ring**. That makes the
     "nickel bites" caption hard to see, because he looks *on* Kupp, not outside him. Push the
     nickel's first path farther outside (e.g. `(5.0, 10.2)`).
   - **fig-snap9, frames 3–4:** the **E square sits on R** next to the QB, and **E/T/R cluster** in
     frame 4. Fixed by A6 (an interior rusher, with the RB blocking to the other side).

8. **The strips skip the key moment, the throw.** Every reconstruction is about *when the ball came
   out*, but no panel shows the release:
   - fig-snap3: use `[0.0, 1.5, 2.8, 4.6]` and title the third panel "2.8 s · right side covered;
     ball to the checkdown".
   - fig-snap6: use `[-1.6, 0.0, 0.7, 3.0]`. A "0.7 s · ball out; the Will is still at the line"
     panel *proves* the caption's claim, which the current 1.3 s frame doesn't, because the Will is
     already in the backfield there.
   - fig-snap9: use `[0.0, 1.6, 2.4, 4.6]` and title the third panel "2.4 s · ball out as the
     pressure arrives". "Darnold threw on time under pressure" is the point of the snap.

9. **fig-snap3: a "quick out" doesn't "settle".** The charted route is `QUICK OUT`, read `CHK`, thrown
   at 2.8 s. The figure has H run the out, stall at 0.42 speed, and then turn up. A coach would draw
   either a 5–6 yard speed out the QB comes back to after the right side (Z curl, Y dig) is covered,
   or say "a quick out thrown late, as the outlet". Remove the "settles" leg or slow the whole route.
   Also, both corners bailing to 17 yards while the left safety rotates down is a fair picture of a
   weak-rotation three-deep coverage. It matches 12-08's "Cover 9 = Fangio weak-rotation Cover 3", so
   cite 12-08 next to the 06-01 link.

10. **fig-drive-board (the 3×3 board):**
    - **The ball is always on the middle, but FTN records the hash.** `starting_hash` for snaps 1–9
      is L, R, R, L, M, R, L, L, L. Put the ball there (`Play(..., ball_y=...)`; check whether FTN's
      L/R is from the offense's view). This pays off in the text, because it explains three plays.
      Snap 6's screen went left to the *field* from the right hash. Snap 3's checkdown went left to
      the field. Snap 9's Cover 6 has its quarters side to the field (right, Kupp's side) and its
      Cover 2 / cloud side to the boundary, which is exactly how Cover 6 is usually set.
    - **The red-zone panels use open-field depths.** In snaps 8–9, the safeties at 12.5–13 are
      standing *on the goal line*, and the corners are 7 off. Compress them for the red zone: safeties
      at 9–10, corners at 5–6. Snap 9 should match fig-snap9's own pre-snap picture (FS 10, SS 9.5).
      At the moment the two figures disagree.

11. **fig-stance-pairs:** the A and B labels nearly touch ("…run block?  B tackle…"). Move B's label
    right by ~1 unit or wrap it to three lines. Separately, pose B looks like a standing man. That
    works as a "two-point stance", which is the *most* visible tackle pass tell on TV, so say so in
    the caption: "many tackles go to a two-point stance on obvious passing downs".

The other figures check out. fig-clock-budget, the master card, fig-checklist-worth, the tells plate
(apart from key 9/10 wording), fig-drive-log, fig-drive-trace, and Predict 1–3 are all legal and
realistic. In Predict 1–3 the 4-3 Over has the 3-tech and the 6/7 technique to the TE and the
SS rolled down to make 8 in the box, the mugs are in the A gaps, and the SAM is walked out over the
slot. Labels sit clear of the field edges.

---

## C. Missing nuance a coach would insist on

12. **Field and boundary (the hash) is missing from the checklist.** For coaches it's the first
    thing after down and distance. Defenses set strength, rotations and blitzes by field and
    boundary. Offenses set formations into the field and run perimeter screens and sweeps to it.
    Add "hash: field side / boundary side" to step 1 (or step 3) on the card and in the step text.
    Show it on the drive board (B10).

13. **"Strength" is a dialect.** The task asks about terminology across systems, and step 3 says
    "formation strength" as if it were one thing. Defenses declare strength in different ways: to the
    tight end, to the side with more receivers (passing strength), or to the field. The defense's
    choice decides which way the rotation and the front set. Add one sentence and link 02-02's
    definition.

14. **Personnel matching is about *who*, not only *how many* (snap 2).** The text calls the Rams'
    nickel on snap 2 "the defense betting on a pass". The charting suggests a better reading. Snap 1
    (12 personnel, WRs Kupp and Bobo) drew **base**. Snap 2 was the same 12 personnel, but with Kupp and
    **Smith-Njigba** (the 2025 OPOY), and drew **nickel**. Snaps 7–8 (12 personnel with Bobo again)
    drew base, and every snap with Smith-Njigba on the field drew nickel or dime. That pattern looks
    like the defense matching a *player*. It's a great step 2 lesson: "Count the digits, then notice
    *which* receivers are on; defenses sub for players." Reword snap 2 and add a clause to step 2.

15. **Snap 4's "two nose tackles"** comes from participation's roster position labels (`2 NT`), not
    from where they lined up. Say "five big bodies up front (two of them listed as nose tackles)", or
    drop it.

16. **Defenses now fake their motion response** (step 4). The man/zone indicator still works, but
    two-high and match teams (the Fangio tree and Macdonald, the defenses in this very drive's
    lineage) deliberately bump in man and travel in zone. Add one sentence. "Motion response" belongs
    with leverage and the shell as a *lean*, not a read.

17. **The quarterback and center at the line are a pressure tell missing from step 8.** The center
    or QB pointing out the Mike ("54's the Mike"), a slide check, a "kill" call or a look to the
    sideline all tell you the offense *sees* pressure and has reset the protection. They are the
    easiest pressure tells to see live on the broadcast. Add one line to step 8 and to the card's line 8.

18. **Pulling-guard and depth tells are missing from tell 1.** Linemen's tells that coaches actually
    read are: a guard with lighter weight, a slight depth cheat, or his heel turned toward the
    pull side (the gap-scheme tell that the "layered predictions" section relies on), and the OL
    backing off the ball (legal up to the center's waist) on passing downs. Add both to row 1.

19. **The drive model doesn't know it's Seattle.** On snap 1, "only a lean, because Seattle throws from
    this look too" is not what the model said, because it is league-wide. Say "because offenses throw
    from this look too". Then put this in the snap 7–8 paragraph: Kubiak's offense ran far more
    under-center play-action than the league. A reader who did the step 1 PROE homework (13-04
    scouting card) would have started snaps 7–8 lower than the model did. That reinforces the
    chapter's own between-snaps advice.

20. **The two-high statistic measures something other than what the text uses it for** (step 6).
    "NGS measured two-high coverage on 42.0% of dropbacks … Two-high before the snap, then, is no
    longer a tell by itself." NGS's figure is *post-snap* split-safety coverage. The stronger
    argument for "two-high pre-snap isn't a tell" is the *gap* between the pre-snap shell
    (two-high on most snaps) and the post-snap coverage (two-high on 42%). That gap is the disguise.
    Reword it, or give a pre-snap MOFC/MOFO rate if one is sourced.

21. **Snap 8 deserves one more clause.** The throw went −1 air yards in 0.6 s with read `DES`, against
    a five-man pressure. That was a designed, at-or-behind-the-line throw: a perimeter extension of the
    run game, not a dropback "tendency-breaker" in the play-action sense. Say "a designed quick
    throw behind the line, the run game's perimeter extension". The miss stands either way.

---

## D. Smaller wording

- Step 5: "six against eight means someone will be unblocked" → "two defenders will be unblocked".
- Step 7 linebacker depths are fine for the NFL. For consistency with 05-05, consider "4½–5½ yards".
- Fig-clock-budget: "huddle: the call comes in by helmet radio" from :30 to :21 is roughly right. In
  practice the call is usually in by :25 and huddle teams break around :18–:20. That fits the caption's
  "timings vary".
- Snap 5: "a defense that brings a sixth man gets a free rusher" → "…the quarterback has to beat
  the sixth man with a hot throw; nobody can block him."

## gridiron notes (no library edits needed)

- The chapter uses only public gridiron API plus local helpers (`snapshot`/`strip`), and that's fine.
  For B10, `Play(..., ball_y=...)` takes care of the hash.
