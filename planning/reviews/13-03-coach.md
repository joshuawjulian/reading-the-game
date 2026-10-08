# Coach / film-analyst review: 13-03 Win Probability and Decision Analysis

Reviewed 2026-10-08 against the current `pdfs/13-03-win-probability-and-fourth-down.pdf` (39 pp., built
08:37, newer than the .qmd). I rasterized it at 60 and 90 dpi and looked at every figure: random walk,
WP curves, calibration, SB LI chart and WPA table, leverage heatmap, ingredients, decision tree with the field strip,
recommendation maps, follow-rate trend, team scatter, down-14 and down-8 charts, and the three drill
diagrams. I also ran pbp queries in `rtg` to check the points below.

**Verdict:** The analytics are strong and the decision-tree teaching is right. The football is mostly
right, but several places need a coach's nuance, and one claim is contradicted by the chapter's own numbers. Two of the three
drill diagrams have alignment problems a defensive coach would catch at once. No label is clipped by the field
edge, and there are no collisions.

## Must fix (accuracy)

1. **Lions film room contradicts its own table (l.1268-1270).** "The two decisions from the NFC
   Championship Game ... were, by every model, among the *closest* calls he made." The chapter's
   model gives the 4th-and-3 at the SF 30 (down 27-24, 7:38) a **+6.7-point** gain, a "clear go" by
   the chapter's own 1-point rule (table, p.18). Only ESPN (0.3) and NGS (2.5) called it close. Fix:
   "by the published models (ESPN, Next Gen Stats), both were close calls; this chapter's simpler
   model, which is weakest in the fourth quarter, called the second one a clear go." Add a coach's
   point here too: the 4th-and-2 failed on an incompletion to Josh Reynolds (pbp: "incomplete short
   left to 8-J.Reynolds"). It is widely remembered as a drop, but **have the fact-checker verify that
   before printing "drop"**. That makes it the cleanest example in the book of grading the decision
   separately from the execution.

2. **Drill 2 text: "everyone within about 8 yards of the line, as it must be this close to the end
   zone" (l.1552).** That is false. From the 8, the end line is 18 yards away, and defenders may align
   anywhere up to it. Keeping everyone tight is a *choice* (the field is compressed, so there is no deep
   space worth guarding). Reword: "the defense is in nickel with its safeties on the goal line. The end
   zone is only 10 yards deep, so nobody needs to play deeper."

3. **Conversion model ignores field position, and near the goal line that matters (drill 2, map, "Watch
   for it").** pbp 2016-2025, 3rd and 4th downs: **3-to-go converts 44% inside the 10 against 52-54%
   between the 20s** (2-to-go: 50% against 57-60%; 4-to-go: 41% against 48-50%). The compressed field
   takes away pass windows, and every defender can play the sticks. Drill 2 says "the roughly 50%
   that teams convert on fourth-and-3". From the 8 it is closer to 44%. The answer doesn't flip
   (break-even 22%), but a coach would insist on it. Fix: add one sentence in "The ingredients", and either
   add `yardline_100` (or an inside-10 dummy) to `fit_logit`, or at least say the red-zone cells of
   @fig-fourth-map overstate p(convert) by about 6-8 points. nfl4th's go-for-it model includes
   field position.

4. **Field-goal geometry is off by a yard in the code (l.779 vs l.777 and the tree labels).** `dist =
   yl + 18` puts the holder 8 yards back, which is correct: the NFL PAT from the 15 is a 33-yard kick.
   But `miss_spot = yl + 7` and `miss_wp` use the 35, while the tree's text box says "SF ball at its 36".
   Make both `yl + 8`. Also change the prose "the 7 or 8 yards back to the holder" (l.696) to "about 8
   yards back to the holder (an extra point snapped from the 15 is a 33-yard kick)".

5. **Timeout advice can hurt on fourth down (l.1419-1421).** "It is often worth taking the 5-yard
   penalty instead." On 4th-and-1 that penalty turns a go (break-even about 48%, p 67%) into 4th-and-6
   (p about 41%) and flips the decision. Qualify it: "on first or second down, or when you are going to
   kick anyway. On a fourth-and-short you plan to go for, the timeout is usually cheaper." Also,
   1.7 points is the value of a timeout *in the last 1:00-2:30*. Say "a timeout burned in the third
   quarter costs some of that later", not "about a point".

## Should fix (missing nuance a coach would insist on)

6. **"Four-down territory" is decided before third down.** This is the most important coaching reality
   the chapter leaves out. Staffs decide going into the series whether the drive is four-down
   territory, and that changes the *third-down call*: run on 3rd-and-4 to set up 4th-and-1, or take a
   shot on 3rd-and-2 because 4th down is a free play. It belongs in two places:
   (a) "Watch for it": "on third down, ask: is this four-down territory? Watch the call." (b) The
   third-vs-fourth selection paragraph (l.689-693). "Third downs have no such selection" is too
   strong. Third-and-long has its own selection: give-up draws and screens to set up the punt, which drag
   the 10+ rate down, as your 3rd-down orange diamond at 20% shows. Third downs in four-down
   territory are also called differently. Soften it to "much less selection, and errors in both
   directions", and keep the conclusion.

7. **The quarterback sneak deserves its own number.** Drill 1's answer says "with a sneak or a tush push
   available, more". Give the size: league QB sneaks on 3rd/4th-and-1 convert far above 67% (compute
   `qb_scramble==0 & rusher==passer`, or use FTN `is_qb_sneak` for 2023-2025), and the Eagles' and Bills'
   rates are higher still. That is why the box count barely matters on 4th-and-1. Also: "it makes the run a
   little harder and the play-action pass a little easier" (l.1544-1546) is true for a downhill run, but the
   sneak is nearly immune to an 8-man box because the extra defenders are outside the A-gaps. Say so.

8. **Hard counts and penalty-negated attempts bias the go rate (`grade`, l.1151).** Plays that end as
   `no_play` (false start or delay on a 4th-and-1 the team lined up to go for, then a punt on 4th-and-6) are
   graded as a *punt on 4th-and-6*. "Line up, hard count, then call timeout or take the delay and punt" is a
   standard tactic, so the coaches' true go intent is slightly understated. One sentence in the
   method paragraph is enough.

9. **Icing sample is contaminated by clock timeouts (`icing`, l.1430).** A defensive timeout right
   before a late field goal is often clock management, not icing. pbp: of 161 "iced" kicks, **37 came
   with the kicking team already ahead** (a trailing defense stopping the clock to save time for its own
   possession). Restrict to kicks that tie or take the lead (`score_differential` between -3 and 0). That is the
   classic icing situation: 116 kicks. Also mention that a team can't call back-to-back timeouts in
   the same dead-ball period to "double-ice" (it's a 15-yard foul). **Verify the exact rule wording
   with the fact-checker before printing.**

10. **Timeout regression mixes opposite situations (`timeouts`).** A timeout is worth a lot to a team
    that needs the clock stopped (trailing) and little to one that wants it running (leading). Fit the
    regression separately for offense trailing and offense leading, or add `timeouts × sign(lead)`
    interactions. The averaged +1.7 and -1.1 understate the trailing team's value, which is the
    situation the text then describes ("trailing by a field goal at its own 25").

11. **SB LI WPA table hides the key words.** `short_desc` cuts the text at 60 characters, so "Q2 2:36 NE: Brady pass short
    left intended for 80-D.Amendola ..." doesn't show INTERCEPTED or TOUCHDOWN. The reader can't tell it
    is Alford's pick-six that the next paragraph names. Append a tag for INTERCEPTED, FUMBLES, sacked or
    TOUCHDOWN (or cut at 75 characters after removing the receiver's number). Also, the +10.1 for a 27-yard first
    completion of Q2 at 0-0 is bigger than any sensible model should give. One clause would help:
    "nflverse's WP is jumpy at the quarter change; read single early swings loosely."

12. **Drill 2 / drill 3 terminology.** The drill 2 caption says "3x1 shotgun trips", but Y is
    *attached* inline next to the RT (H slot, Z wide). Most staffs call that "Trey" (or "trips closed" or
    "TE trips"). Either detach Y (`moved(w=+6)` so it sits between RT and H, off the ball) or change the
    caption to "3x1 with the tight end attached (trey)".

## Diagram fixes (specific players)

**Fig 13, drill 1 (4th-and-1, own 34, I-form vs 4-3 Under):** The front is legitimate (weak 5, weak 3-tech,
strong-shade nose, strong 5, Sam on the TE at 9). Corners pressed. Good. But:
- **SS is not "in the box".** He sits about 7 yards deep and about 3 yards outside Y. For a short-yardage
  eighth man, use `SS.moved` to **d≈5, w≈Y.w+1.5** (outside shoulder of the TE, ready to fit the C gap
  or D gap).
- **FS too deep for 4th-and-1.** He is at about 13 yards. Cheat him to **d≈9-10** over the ball.
- Optional: W and M at 4 yards are fine. In real short yardage many teams sub to goal-line
  personnel (5-3 or 6-2), so the caption could say "base 4-3 stays on the field" to make it a deliberate choice.

**Fig 14, drill 2 (4th-and-3 at the 8):** Alignments are reasonable. Safeties on the goal line, corners at 3-4,
$ over H at 5, both LBs at 4-5. Only the Y-attached terminology (item 12) and the "must" wording (item 2) need fixing.
X at w=-17.5 is about 2.5 yards inside the lateral window, so the label is OK.

**Fig 15, drill 3 (2-point try, 2x2 vs nickel):** **The left slot (H, w≈-8.4) is uncovered.** The
nickel ($) went to the Y side, and the W stays inside at w≈-2, 3 yards deep in the end zone. No defense
leaves a slot unaccounted for on a two-point play. Fix: walk the **W out to an apex over H (d≈3,
w≈-6)**, or put $ over H and roll the SS down over Y. The safeties at about 5 yards into the end zone are fine.
Keep the M in the box over the back side of R.

**Fig 7, field strip:** correct. Ball at the SF 28, the yellow line at the 26, the hold spot at the 36, and the
hashes at the right width. If you like, draw the goalposts on the end line so the dashed kick arc lands on
something.

## Smaller notes

- l.1033-1041 (Belichick 2009): good use of drive data. It is worth adding that Indianapolis had **one
  timeout** in Burke's analysis. Check it, and include it only if verified, because the timeout is exactly
  the input the random walk lacks.
- Leverage heatmap: "Up or down 17, even the first quarter is quieter than average": the cell values (0.4-0.5)
  support it. Fine.
- @fig-fourth-map has impossible cells: 4th-and-6 to 10 at the opp 5, and so on (yards to go cannot exceed
  the yards to the goal). Mask cells where `togo > yl` (blank or grey), or a sharp reader will ask about
  "4th & 10 at the 5".
- Team scatter: DET and BUF are both 0.016 WP lost per game. "Ranked 1 of 32" is a near-tie. Say
  "fewest, level with Buffalo".
- SB LI film room: confirmed in pbp that NE had **all three timeouts** at 4:40 (it used #1 at 3:50) and
  ATL had one. So "three runs would have forced New England to burn its timeouts" is right. Consider
  adding "and Atlanta had only one timeout of its own" for completeness.
- Two-point section: the spec's "down 8" is handled as "no decision". That is fine, but add one line pointing to the
  10-04 two-point chart rows a coach actually uses after a touchdown: up 5 (go to 7), up 12 (go to 14), down 2 (go to tie),
  down 10 (kick to 9?) and down 15 (go: same logic as down 14). It would round out "two-point decisions".

## gridiron use

Sensible. Pre-snap pictures only, through `Play(...).draw()`, with `moved()` adjustments, `Field` for the strip, and no
animations (none are needed here). No gridiron changes are needed. The issues above are alignments chosen in
the chapter, not helper bugs. One observation for the library owner: `defense("nickel", "two_high", gun_2x2)`
puts $ over the *Y* slot and leaves the W inside. Other chapters using 2x2 vs nickel should check that a
defender is walked out over the second slot.
