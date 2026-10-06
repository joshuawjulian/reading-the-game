# 01-02 Downs, Distance, and Field Position: coach / film-analyst review

Reviewer role: veteran NFL coach and film analyst. Checked for technical accuracy and completeness.
Read: the full qmd, AUTHORING, FACTS-current, the CURRICULUM spec, and 13-02 (for overlap).
Rasterized `pdfs/01-02-downs-distance-and-field-position.pdf`, which is newer than the qmd, at 150 dpi
and looked at all 12 figures plus the table. Spot-checked the quoted numbers against nflverse pbp
inside the `rtg` container.

**Overall:** strong and accurate. The series-of-downs strip, the EPA scorecard and the two-Super-Bowl
film room are good teaching, and the history, rules and Hawk-Eye material agree with FACTS-current.
The problems are concentrated in three places. First, the **short-yardage claims blend third-and-1
with third-and-3**, and the Predict-1 answer and the "toss-up" bullet rest on that blend. Second, the
**second-and-short "misconception" box contradicts the data**. Third, the **two Predict-the-play
defenses** have alignments a coach would not draw. The remaining items are smaller label and caption
fixes.

---

## A. Must fix (accuracy / misleading)

1. **Third-and-short is not a single bucket. Split out third-and-1.** (Section "What the graphic
   tells you", item 3; Predict 1 answer.)
   - 2025 neutral-situation pass rates, which I recomputed: **3rd & 1 = 21% pass**,
     **3rd & 2 = 53%**, **3rd & 3 = 75%**, **3rd & 4 = 87%**. The 46% for "1–3" is an average of a
     run down and a pass down.
   - Item 3, "Short yardage is a real toss-up", is wrong for 3rd & 1. Third-and-1 is a run down, and
     about 4 in 5 snaps are runs.
   - The Predict-1 answer has the same problem. "That's why the pass share on third-and-short is
     still near half" is used to explain a **third-and-1 from 22 personnel under center**, and that
     snap is the most run-heavy look in football.
   - Fix: add a 3rd & 1 figure to the text (`PASS31`, computed like `PASS`) and change the answer to
     "about four in five third-and-1 snaps are runs; in 22 personnel under center it's higher still.
     Play-action is the surprise, not the norm." Optionally split the grid's first column into
     "1" and "2–3".
   - Coach's dialect note worth one sentence: **NFL call sheets cut third down finer than
     short/medium/long**, typically 3rd & 1–2, 3rd & 3–4 (or 3–6), 3rd & 5–7, 3rd & 8–10 and
     3rd & 11+. The reason is the jump the chart shows between 1 and 3 yards. The three broadcast
     buckets are a simplification, so present them that way.

2. **The second-and-short "Common misconception" box overstates its case and contradicts its own number.**
   - The box says second-and-1 is "one of the best situations in football to throw deep", then
     reports that offenses passed only **30%** of the time.
   - My check: 2nd & 1 is 27% pass and 2nd & 2 is 27% pass. Only about **17%** of second-and-short
     passes went 15+ air yards, and only about 9% went 20+. The claim "many of those were
     play-action shots" is not supported.
   - The coaching idea is real. Coaches call second-and-short a **"free play"** or **shot down**
     because a miss still leaves third-and-short. Reframe the box: "Second-and-short is called a
     'free' down. Offenses still run about three times in four, but it's where the shot play lives:
     when they do throw, it's more often downfield than on other downs." Either verify that last
     clause with an air-yards comparison or drop it. Remove "many of those were play-action shots"
     unless it is backed by FTN `is_play_action` data for 2022–2025.

3. **The Watch-for-it forecaster rule calls third-and-3 a run, and the data says it's 75% pass.**
   - The rule "third-or-fourth-and-4-plus → pass" is built on a weak breakpoint. Third-and-2 is
     already 53% pass.
   - Change the third/fourth-down threshold to **2+** (pass on 3rd/4th & 2 or more; run on & 1) and
     recompute `S["rule_acc"]`. It should rise.
   - Consider the same check on second down. 2nd & 4–6 is 48% pass, so the 7+ threshold is fine.

4. **The fourth-down chart's caption and text contradict the chart.**
   - The caption says "inside the opponent's 35, they kick field goals." In the 4th & 1–3 panel,
     teams **went for it 67% (opp 35–21) and 74% (opp 20–goal)**.
   - Fix the caption: "...inside the opponent's 35 they kick on 4th-and-4-plus, but on 4th-and-short
     they now usually go."
   - Body text: "from around your own 40 to the opponent's 36, a stretch where a punt gains little
     (the ball may bounce into the end zone)" is wrong for own 40 to midfield. A punt from your own
     40 still nets about 40 yards. The touchback squeeze starts on the opponent's side of the 50.
     Reword: "a stretch where a field goal is too long and, once you cross midfield, a punt has less
     and less field to buy."

5. **"A drive's EPA always adds up to the points it actually produced" is true only for scoring
   drives.** (EPA section and Takeaways bullet 6.)
   - For a drive that ends in a punt or a turnover, EP₀ + ΣEPA equals the **negative of what the
     opponent's new possession is worth**, not 0. The extra point is also scored as its own play.
     For 2024_22_KC_PHI the XP has EPA +0.05, and the model counts a TD as 7.
   - Fix: "...for a drive that scores, the starting EP plus the EPAs equals the points; for a drive
     that doesn't, it equals the (negative) value handed to the other team."

6. **Sack definition is missing the coaching qualifier.** (Glossary and the "The sack" section.)
   - A sack happens only on a **called pass play**. A QB tackled behind the line on a designed run,
     a keeper or an option is a tackle for loss, not a sack.
   - A QB **forced out of bounds** behind the line on a dropback also counts as a sack.
   - Add both in one line. Suggested glossary text: "Tackling the quarterback, or forcing him out of
     bounds, behind the line of scrimmage on a pass play before he can throw."

## B. Diagrams

- **Fig. 10, Predict 1 (3rd & 1, 22 personnel vs 4-3).** This is the least realistic picture in the
  chapter.
  - **SS is not "walked down".** He is at about 7 yards, deeper than all three linebackers. The
    caption says he is near the line. Move SS to **d=3.5–4, w≈+6** (outside the Y, at linebacker
    depth) or onto the line as a 9-technique.
  - **Linebackers at about 5 yards are too deep for third-and-1.** Short-yardage LB depth is
    **3–4 yards**, and often 2–3 against 22 personnel. Use d=3.5 for W, M and S.
  - **The DL sits a full yard off the ball,** on the yellow line. In short yardage they crowd the
    ball, so set d≈0.6–0.8.
  - Optional: a coach would often show a heavier front here (a 5-3 or 6-2 short-yardage package,
    with a 3rd linebacker replaced by a DL). If the 4-3 stays, the caption is fine once the SS
    moves.
  - Label clash: the **tailback is labelled "T"** (the gridiron I-form default), the same letter as
    the **defensive tackles**, and Predict 2 labels the back "R". Relabel the tailback "R" so the
    figures agree with each other and the tailback isn't read as a tackle.
- **Fig. 11, Predict 2 (2nd & 15, gun 2x2 vs nickel two-high).**
  - **Safeties at 17 yards** is prevent depth for a first-quarter second-and-15. Real two-high
    depth is **13–15**, at or just beyond the sticks, and the safeties bail at the snap. Use d=14.5
    and change the caption and the answer text ("Two safeties 17 yards deep") to match.
  - **The left slot (H) has no apex defender.** W sits inside the left tackle about 9 yards
    lateral from H, while the nickel ($) is apexed over Y on the other side. In a two-high nickel
    vs 2x2, the W walks out to **apex H, at about d=5.5 and roughly midway between the LT and H**.
    As drawn it looks like a blown alignment, not "soft" coverage.
  - **Yard-number collision:** the "20" numbers sit under the X and Z dots and the "30" numbers
    under both corners. Pass `numbers=False` or move them.
- **Fig. 5, spot.**
  - The "new line of scrimmage" label runs into the **ball ellipse**, which covers the last letters.
    Shift the label left (w≈-8) or above the line.
  - The "40" yard number is half hidden under the yellow line.
  - The hash ticks cut through "old line of scrimmage".
  - Football is correct: forward progress applies, the spot comes in to the hash, and the line to
    gain is unchanged.
  - Nuance for the text: forward progress applies when the **defense** drives the runner back. If he
    retreats on his own (reversing field, a QB scramble), the ball is spotted where he is downed.
    One clause fixes it.
- **Fig. 8, EPA scorecard:** on the Dotson row, "+2.95" collides with the ✓. Widen
  `axe.set_xlim(-1.3, 5.6)` or move the tick column to x=5.5.
- **Fig. 2, score bug:**
  - "3rd 6:42" sits next to "3rd & 8", and a beginner will mix up the quarter with the down. Use
    "Q3 6:42", or put the game in another quarter.
  - Add the possession indicator (the football or arrow by the team with the ball). Every network
    shows one, and the caption leans on "the visiting offense".
- **Fig. 1, series strip:** correct. That covers the hashes, the stick positions, the down box at
  the line of scrimmage, and the reset. Optional: add a "sideline" tick label so a reader knows the
  crew stands off the field.
  - FYI: the official chain crew works the sideline **opposite the press box** (normally the
    visitors' side), and an unofficial auxiliary set runs on the other side. That is worth a
    parenthetical. Verify against the NFL rulebook before printing.
- **Fig. 7, field map:** "field-goal range (roughly the 35 in)" reads oddly. Use "field-goal range
  (inside about the 35)". Consider "35–40 for today's kickers", because the chapter's own Predict 3
  says 70% from 53–57 yards.
- **Fig. 9, goal-line panels:** fine as spot-only panels.
- **Fig. 12, Predict 3:** fine. The kick spot 7 yards back is correct. The punter at about 14.5
  yards is realistic. The posts span 18'6" on the end line.
- Only one animation (the series). The PDF 2×2 strip tells the story.

## C. Coaching nuance to add (short)

- **The "line to gain" and the ball's nose.** All spots and measurements use the **forward point of
  the ball**, not the runner's body. One clause in the spot section helps readers make sense of the
  replays of a ball tip and a knee.
- **Field goal geometry.** "The kicker stands about seven yards behind the line" should be "the
  **holder** places the ball about seven yards behind the line". The kicker starts his approach
  further back.
- **Punt outcomes.** Besides a return or a fair catch, the receiving team often **lets it bounce**,
  and the coverage team downs it. That is how punts "pin" teams, and Predict 3 depends on it.
- **Red zone.** Coaches say "the **end line becomes a defender**". That is the plain reason deep
  shots disappear, and it is worth half a sentence.
- **Third-and-very-long is not 100% pass.** In the grid, 3rd & 11+ (92%) is *below* 3rd & 7–10
  (97%). About 8% are draws and "give-up" runs called to set up the punt or the field goal, or to
  avoid a turnover. One sentence turns an apparent anomaly into a lesson. It also conflicts with
  "above 90% at every longer distance", which is technically true but hides the dip.
- **Success rate dialect.** Add a single forward-pointing sentence saying that coaches and
  broadcasters also use a yardage version (40% / 60% / 100% of the distance, "staying on
  schedule"), and link to 13-02, which already teaches it at line ~707. A reader will meet that
  version on TV before reaching Part 13.
- **Snap 5 of the scorecard.** "Which would have brought on the punt team" overstates it. At the
  KC 42 on 4th & 5, the chapter's own chart shows teams in that zone punt only about half the time
  on 4th & 4+. Say "would have left fourth-and-5 at the KC 42: a punt or a gamble."

## D. Film room: accuracy and suggested additions (verify before adding)

- **Super Bowl LIX drive:** checked against the nflverse descriptions. The sequence, the McDuffie
  unnecessary-roughness penalty, Dotson's 28-yard TD reversed to the 1 (the card says "+27", which
  is consistent with the yard-line math) and the Hurts 1-yard sneak are all correct.
- **Super Bowl XXXIV:** the facts are correct (first-and-goal at the 10, 0:06, slant to Dyson,
  Mike Jones). The film-room detail a coach would add: Jones was first carried by **Frank Wycheck's
  route** to the outside, then came off it, read the slant and tackled Dyson short of the goal
  line. Verify the wording.
- **Super Bowl XLVII:** the facts are correct. Two coach-level details are worth considering:
  1. Baltimore **brought pressure / zero coverage** on the fourth-and-goal snap, which is why
     Kaepernick threw the quick fade to Crabtree.
  2. On Koch's intentional safety, the Ravens' blockers **held on purpose**, because holding in
     your own end zone is just another safety. That ties neatly to the "backed up" text earlier.

  Both are widely reported. Verify (Wikipedia or ESPN, or Harbaugh's postgame quotes) before adding.

## E. Checked and OK

- Camp history (1880–81 block games, 1882 five yards in three downs, 1906 ten yards, 1912 four downs).
- The neutral-zone explanation, the hash rule, the blue and yellow broadcast lines, and the
  "& Goal" / "& inches" explanations.
- Hawk-Eye in 2025 (6 × 8K, about 30 s, officials still spot, chains as backup) matches FACTS-current.
- 2025 touchback at the 35, punt touchback at the 20, and a missed FG spotted at the spot of the kick.
- Sack yardage: 6.5 yards on average in 2025, which matches "six or seven".
- "A run gains four yards less than half the time": 46.6% of 2025 runs gained 4+, so the claim holds.
- The Garrett record of 23 matches FACTS.
- Footnotes are each referenced once.
