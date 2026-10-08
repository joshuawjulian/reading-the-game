# 12-03 Shanahan Tree: coach / film-analyst review

Reviewed: `chapters/12-case-studies/12-03-shanahan-wide-zone-tree.qmd` and `pdfs/12-03-shanahan-wide-zone-tree.pdf`
(built 07:10 today; I looked at every figure at 110–220 dpi). I checked it against 03-02 (reach-and-overtake
convention), 04-05 (naked boot / keeper / protected boot), 05-02 (bear / 46) and FACTS-current §0 C2 and §9.

**Verdict:** the chapter is strong and most of the football is right. The wide zone vs bear assignments are sound and
match 03-02's overtake convention, the count of 8 in the box against 7 blockers is correct, and the logic of
leaving the end unblocked and then booting him is taught well. Before publishing, fix these: one contradiction
inside the boot strip (the fullback gives the play away), a frame strip that claims routes it doesn't show,
two overstated technique claims about the bear, a missing 49ers film room (the team the chapter is about),
and gaps in the 2026 tree (Stefanski, Slowik and others).

---

## P1: must fix

### 1. Boot strip (fig-boot-strip): the fullback is a tell, and the caption says "everything says wide zone right"
- In @fig-bear-wide-zone the F **leads play-side** (right) onto the SS. In the boot the F starts slicing **left at
  0.15 s**. Frame 1 already shows him two yards left of the QB, so the first second does *not* look the same,
  even though caption (1) and the text ("Freeze the strip at frame 1 and compare… the same") say it does.
- A coach would make one of two fixes:
  - (a) **Preferred, and it's how the family actually pairs these plays:** the F's slice path belongs to
    **split zone / "slice"**, where the F crosses behind the line to kick out the backside end. Say so: the boot's
    companion run for the *F action* is split zone, and the end sees "slice block coming at me", squeezes, and the F
    runs right past him into the flat. One added sentence plus a link to 03-02's split zone (03-02 owns the term).
  - (b) If you keep wide zone with the F leading as the companion, have the F take 2–3 steps play-side first
    (via ≈ (-4.0, 2.6)), then flatten back to the left flat. That delays his release, which is realistic for a
    "fake lead" and keeps frame 1 honest.
- Either way, drop "line, back, linebackers go right" as proof of sameness, or add "(the F's path is the one
  difference: see …)".

### 2. Boot strip: frames 3–4 claim things the window doesn't show
- Caption (3) says "the Z on a deep over route; X's deep route has carried the left corner away". At 2.0 s the Z is
  still at the top *right* (not on the boot side), and the LCB, X and FS are all above the window (`window=(-8.3, 14.2)`).
  In print the reader sees one deep-ish receiver and no corner.
- Fix: `window=(-8.3, 20.5)` and `lateral=(-17.0, 9.0)`, and move frame 3 to about 2.3 s so the Z has crossed the ball.
  Alternatively, keep the window and change caption (3) to say "the Z's deep over (off the top of the frame)".
- Throw timing: the release is at 2.45 s and the catch is about 3.2 s. That is about 0.8 s of flight for a 15-yard
  throw, slow but acceptable. On a naked, though, the QB should be wider at the throw: today he is at w ≈ −8, only
  about 4 yards outside the LT. Take the boot path out to about (−6.5, −10.5) so he is outside the tackle box,
  near the hash or numbers.

### 3. Boot strip: label collisions
- Frame 1: the ringed **E sits on top of the LT** marker, and the LT label is hidden.
- Frame 2: the **M and SS squares overlap**, and **R overlaps RT**.
- Frame 1: **Y overlaps RT/9** (minor).
- Fixes: route the end's crash *flatter* (see 4). End the SS at (3.4, 7.6) instead of (3.4, 6.6). End the RB's fake at
  (0.6, 4.6) or let him continue upfield to (2.0, 6.5) so he clears RT.

### 4. Boot strip: the backside end's crash path is unrealistic
- `BE` goes to (−3.4, +1.6) through (−1.8, −0.4). That is 3.4 yards into the backfield and **right of the center**,
  exactly at the fake mesh point, so he would run into the quarterback. A crashing end flattens down the line
  1–2 yards deep, chasing the back's heels, and the QB passes *behind* him at 4–5 yards deep. That depth
  difference is the whole picture of a naked boot.
- Fix: via (0.0, −3.0), (−1.0, −0.8), end around (−1.6, +1.2), then turn back at (−3.0, −2.5). The caption's "chases
  the back down the line" then matches what the reader sees.

### 5. "Crossing behind the linebackers": in the strip the Y crosses *at* linebacker depth
- Frames 2–3: the Y is at 5–7 yards, level with the W and M (who fill only to 3–3.6 yards, then drop back to 5.6–6).
- Real Shanahan boots run the Y on a **deeper cross, about 8–12 yards** ("over" level). There is also a separate
  shallow "drag" tag at 5–6 yards. To keep the three-level story (flat 2, cross ~10, deep over ~18):
  - Take the Y through (5.5, 3.0), (8.5, −1.0), (9.5, −7.0), and end at (10.5, −14).
  - Bring the M and W downhill to about 2.5 yards on the fake (`MIKE` → (2.6, 5.4), `WILL` → (2.8, 1.8)) before
    they turn back.
  - Update the text "crossing at about 7 yards" in the caption to "about 10".

### 6. The Shanahan franchise has no film room of its own
- The film rooms are ATL 2016, MIA 2023 and LAR 2018/2025. The spec lists **2017–2025 49ers** and **Kubiak's 2025
  Seahawks** as team examples, and neither gets a film room. Add both:
  - **Film room: San Francisco 49ers 2019**, NFC Championship vs Green Bay (Jan 19, 2020). Garoppolo threw 8
    passes (6 completions); the 49ers ran 42 times for 285 yards, and Mostert had 220 yards and 4 TDs
    (already footnoted in `[^backs]`, which must then be referenced only once). This is the purest wide-zone
    game of the era. What to notice: the same outside-zone track to both sides; the F/Juszczyk leading; the
    backside end left alone; how few dropbacks were needed. Verify the 42/285 team totals with PFR before using them.
  - **Film room: Seattle Seahawks 2025**, Super Bowl LX. Kenneth Walker III had 27 carries, 135 yards and the MVP
    (FACTS-current §2, VERIFIED). What to notice: Kubiak's under-center wide zone (the 2024→2025 jump is already
    in @fig-fingerprint), and boots and keepers off it against a Patriots front built to stop it. This ties the
    fingerprint to film and to the 2025/2026 tree section.

### 7. 2026 tree: notable omissions (FACTS-current §9)
- **Kevin Stefanski**: Gary Kubiak's branch. He was Vikings OC in 2019 with Gary Kubiak as assistant head coach /
  offensive adviser, and Browns head coach from 2020 to 2025 running Kubiak's outside zone and boots.
  **2026: Falcons head coach** (FACTS §9). Add a MOVES row (2025 Browns HC → 2026 Falcons HC). Leave "calls plays"
  unmarked unless confirmed; he gave up Cleveland's play-calling during 2025, which needs verifying.
- **Bobby Slowik**: 49ers staff 2017–22 and Texans OC 2023–24. **2026: Dolphins OC under Jeff Hafley** (FACTS §9).
  This makes the caption's "the family lost a head coach in Miami" true but incomplete: Miami's *offense* stays in
  the family. Add a row (verify his 2025 job first).
- **Nick Caley** (Texans OC, from the Rams) is in the footnote for the 2025 fingerprint but missing from 2026.
  The Texans' OC is unchanged in 2026 (FACTS §9), so add Houston to the 2026 list.
- The "Watch for it" 2026 team list is missing **Falcons (Stefanski), Dolphins (Slowik), Texans (Caley) and
  Chargers (McDaniel as OC)**.

---

## P2: technical accuracy (wording fixes)

### 8. The "hardest block in football" and "hardest alignment" claims contradict each other and overstate
- The text says the center's reach on a head-up 0 is "the hardest block in football", then calls the 3-techniques
  "the hardest alignment of all to reach". In zone teaching a head-up nose is *easier* to reach than a play-side
  shade (1/2i), and the play-side 3 on a guard is the reach line coaches fear most. The bear's real damage is that
  **nobody is free to help or climb**, not that any single reach is the hardest.
- Rewrite as: "the center must reach the nose with no help, because his play-side neighbor is covered too", and
  drop the superlative. Same change in the fig-bear-wide-zone caption ("has the hardest block in the play" →
  "has to reach the nose with no help").

### 9. Cutback logic for the nose is backwards
- Current text: "because he has stepped play-side, he also clogs the cutback lane". A nose who steps play-side is
  *out of* the backside A gap, so he has moved away from the cutback, not into it.
- Correct version: a head-up 0 can play **either A gap**. He can fight across the center's reach into the front-side
  lane (bang), or let the center's momentum carry past him and fall into the backside A gap, the cutback lane
  (bend). Meanwhile the LG is busy cutting off the backside 3 alone, so nobody can help. Link "bang/bend" to 03-02
  (`#gl-bang-bend-bounce`).

### 10. Gibbs chronology
- The text has Gibbs's zone as the answer to Capers's 1992–94 zone blitzes, but the chapter's own footnote has him
  coaching Denver's line from 1984 to 1987. Gibbs had been building the zone scheme since the 1980s against slanting
  and stunting fronts (including Buddy Ryan's 46). The zone blitz made it more valuable, but didn't create it.
- One clause fixes it: "Gibbs, who had been refining zone since his first Denver stint in the 1980s, …".

### 11. Gibbs and the backside cut block are missing
- Any coach discussing the Gibbs Broncos mentions the **backside cut block**: backside linemen put pursuing
  defenders on the ground. It is central to how the scheme stopped backside pursuit, and the source of its
  "dirty" reputation and later rule pressure. 03-02 owns *cut block*, and the curriculum forward-references
  09-03 for chop/cut legality.
- Add one sentence in "Denver, 1995" with links to 03-02 `#gl-cut-block` and 09-03.

### 12. "What the offense does about it" vs the bear: add the run-game answers
- The three bullets (bring the F, choose who's unblocked, boot him) are right but incomplete. Add a fourth:
  **change the run.** Vs the bear, Shanahan teams also run **split zone** (the F kicks out the end, so every
  defender has a blocker), **crack toss** (the Z cracks the rolled-down SS, the F and pullers lead outside the
  3s instead of reaching them), and **duo/counter** from the same look (already mentioned in "How defenses
  answered", point 1). One bullet with links to 03-02/03-03 is enough.

### 13. Motion: two modern nuances
- "If a defender runs across with the motion man, the coverage is probably man" is a fair first rule, but 2020s
  defenses *bump* linebackers in zone and *pass off* motion in man ("lock and replace"). That is exactly why
  McDaniel's Dolphins moved to motion **at the snap**: the read stopped being clean. Add a clause.
- Missing job: **motion that changes the strength after the front has set** (for example, a Z across or a TE trade
  that leaves the 3-technique on the new weak side and forces a late re-fit). This is a staple of the 49ers'
  run game and fits naturally as a 4th bullet.

### 14. The boot read
- "Reads them high to low" is fine, but on a *naked* the first read is the unblocked end. If he's on the QB, the
  ball goes to the flat immediately (04-05's right panel teaches exactly this). Add half a sentence in "The read
  is simple…" so the two chapters agree.

### 15. Madden callout is too absolute
- "The same call on the first snap of the game… is a much worse play." Defensive habits are scouted on film all
  week, and Shanahan-family scripts regularly open with play-action or boots when film shows the end crashes.
- Soften to: the boot is aimed at a habit, which can be learned from the week's film or from the first quarter.
  Called blind, against an end who isn't chasing, it's a worse play.

### 16. Rams 2025 film room: "count how often Stafford throws before the fake has finished"
- As written, this is not a real coaching cue: the fake has to finish before the throw. Replace with "how quickly
  his eyes come back downfield after the fake and the ball comes out on the first hitch", or "how often the
  under-center play-action is a one-read throw".

### 17. Drill 2 answer: give the other textbook pairing
- With jet motion right to left, "wide zone toward the motion" is defensible. But the McVay/Shanahan staple is
  just as often **wide zone *away* from the jet** ("fly/jet fake, zone away"): the fake holds the backside edge
  and drags the W/NB toward the motion, which thins the play side. Note that the jet man in full flight behind
  the QB can't *block* the edge on a zone run the same way; he only threatens.
- Accept either in the answer, and explain what each one does to the defenders. The six-against-six box count
  is the right primary reasoning; keep it.

### 18. Drill 3 answer: name the cutback
- Add: with the end sitting, the back's **bend/cutback** lane is the one that opens, because the man who used to
  close it from behind is now waiting for the QB. The other option is split zone / "slice", where the F kicks out
  the end so the run is fully blocked. Both are tidier than "one fewer defender".

### 19. Atlanta 2016 film room: add the fullback and the play the critics cite
- Patrick DiMarco was the **2016 Pro Bowl fullback** for that offense. It's the fullback ingredient in its
  pre-49ers form; verify before adding.
- The "play-calling with a lead" criticism has one canonical clip: Super Bowl LI, 4th quarter, about 3:56 left,
  Atlanta up 28–20 at the NE 23. A sack on 2nd-and-11 and then a holding penalty pushed them out of field-goal
  range. One bullet; verify the down, distance and spot against the PFR play-by-play.

---

## P3: diagram polish

- **fig-bear-wide-zone:** the assignments are correct and consistent with 03-02: RT hands on the 3 and RG
  overtakes; C solo on the 0; LG cuts off the backside 3; LT climbs to W; Y reaches the 9; F leads on the SS;
  Z stalks; X runs off. The count is right and nothing is clipped. Two small issues:
  - The F's lead path and the R's thick path run almost on top of each other from the F to the aiming point. Bend
    the F through (−2.4, 4.6) so the two lines separate.
  - The R's path starts by passing through the F marker. This is fine for a static picture, but it reads as a
    collision; starting the R at a slightly wider offset (0.4 yd) would clear it.
  - The bear's weak end is labelled **E** here and **5w** in 05-02's bear plate. Consider "5" for consistency, or
    keep "E" and say "E (a wide 5)" in the how-to-read paragraph.
- **fig-predict-1 / fig-predict-3:** legal (7 on the line: Y-LT-LG-C-RG-RT-X), and the alignments are realistic.
  The Drill 3 label sits clear of the E ring. No issues.
- **fig-predict-2:** legal and the box count is clean (9-3-1-5 + M + W = 6; the NB is outside the box). The
  2-high safeties at ±6.5 are a little narrow; ±8 is more typical with the ball in the middle. Optional.
- **fig-same-qb:** the Goff row's two labels ("+0.12 (2,374)" and "+0.13 (2,997)") crowd each other and the dots,
  because the values nearly coincide. Put one label above the line (`xytext=(0, 7)`) when |in − out| < 0.03.
- **fig-fingerprint, fig-yacoe, fig-epa-rank, fig-staff-moves:** clean, with no collisions. The staff figure needs the
  rows from item 7.

## Things that are right and should stay
- The covered/uncovered pairing and the overtake direction match 03-02 exactly.
- The 8-in-the-box vs 7-blockers arithmetic, and "the offense chooses who goes free".
- "What if the end doesn't chase? → protected boot with the F", consistent with 04-05.
- The two YACOE models (nflverse ignores where the defenders are; NGS uses tracking) and why their agreement matters.
- Labelling the 2025 and 2026 staffs separately, as FACTS C2 requires.
