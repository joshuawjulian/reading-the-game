# Coach / film review: 02-01 Personnel: Who's on the Field Before Anything Else

Reviewer role: NFL coach and film analyst. I checked the qmd as of 2026-10-06 14:28 and the PDF built at 14:28:29. I
rasterized all 19 pages at 90 dpi and cropped the substitution strip, the jumbo plate and the dilemma figure at
170 to 200 dpi (`_pdfbuild/02-01-personnel-groupings/coach/`). I looked at all 13 figures. Two throwaway checks,
`rams.py` and `dl.py`, live in the same folder and reuse the chapter's data method.

**Overall:** the chapter is strong and the core teaching is right. The digit system, "who, not where," the
order of the substitution sequence, the umpire hold and its two-minute exception, the one-play rule, the tempo
counter, the pass-rate data and the film-room picks are all sound and well chosen. The personnel cards are legal
and realistic: seven on the line every time, TEs uncovered, sensible depths.
**One diagram is football-wrong:** in the dilemma figure's run panel, the back runs through the man his tight end
is sealing. I also found three diagram realism fixes, a mischaracterized film-room line, and four nuances a coach
would insist on. Items are in priority order.

---

## A. Must fix (football is wrong)

### A1. fig-dilemma, left panel: the run path contradicts the block
`a.block("Y", target="NB")` with the comment "seals the nickel back inside" is paired with
`a.run("RB", [(3.5, 4.5), (6.4, 7.6), ...])`. The nickel is at w = 5.9. The back crosses the line at w ≈ 4–4.5,
which is **inside** the defender Y is sealing inside, and the back's track then runs through the $'s spot. A seal
block and the runner's track have to agree. Pick one of these two (A is closer to the caption):

- **Option A, outside run (Y reach/seals $ inside, back bounces outside him).**
  RB path `[(-3.5, 2.5), (-0.6, 7.2), (2.5, 8.8), (8.0, 10.2)]`, so he crosses the line at about w = 8, outside the $.
  Add the perimeter block that makes it real: `a.block("Z", target="RCB")` (stalk). Without it, the corner, who is
  the force player, makes the tackle for free.
- **Option B, C-gap run at him (Y drives the $ out, back cuts inside him).**
  Y blocks out: `a.block("Y", pts=[(1.2, 6.6)])`. RT down-blocks the SDE. RB path
  `[(-3.0, 1.8), (0.0, 4.0), (4.0, 4.3), (9.0, 4.8)]`.

With either option, either draw RG/C climbing to the MIKE or add "(the MIKE is accounted for by the line; not shown)"
to the caption. Today an unblocked MIKE sits 3 yards from the cut, and a coach reading the board sees a tackle for
loss. Also fix the label collision: the SDE at w = 4.0 puts its "E" box against the SDT's "T" box at w = 2.35. Move
the SDE to w = 4.4 (a 6i over Y's inside shoulder).

### A2. fig-dilemma, right panel: the seam runs straight at a deep safety
The shell is two-high with the SS at w = 7.5, depth 12.5. Y's seam at w = 8.5 runs straight into the safety's lap.
That is the one place a seam is *not* a linebacker-on-tight-end problem, and the caption's point ("LB on a TE in
space") is lost on anyone who knows the shell. Make it single-high (Cover 1 or 3):
`fix["FS"] = dict(d=13.0, w=0.0)`, `fix["SS"] = dict(d=8.0, w=-9.0)` (rolled down over U). Now the Sam is the only
man carrying Y up the seam. Optionally add "single-high: no safety over the seam" to the caption. If you want to keep
two-high, change Y's route to a 6-yard option/stick (`r.stick(6)`). The underneath matchup is then the point, not
the vertical.

### A3. Film room "the 2025 turn": "the 2025 extremes were *binary* teams" is true of the Rams only
The chapter's own fingerprint chart shows the 2025 Seahawks spread across 11 (42%), 12 (28%), 21 (14%) and 22 (9%).
That is the opposite of binary: they are a variety team built on a fullback. Rewrite "What to notice" so it
contrasts the two:

- **Rams:** binary (59.7% 11, 31.3% 13, 8.9% 12, almost no backs-heavy groupings).
- **Seahawks:** varied. A fullback was on the field on about 19% of their 2025 snaps (my check, `dl.py`/`rams.py`).
  If you name the player (rookie FB Robbie Ouzts), fact-check it first.

Add the number that makes the Rams' point land (course calc, neutral situations 2025):

- **Rams 13 personnel:** 46.5% pass (n = 159), the same as the league's 13 (45.8%), and under center 91% of the time.
- **Rams 11 personnel:** 67% pass (n = 255), against a league 56%.

So the Rams' heavy grouping hid the play, and their light grouping was the tell. That is a better coaching
point than "throwing from both", and it backs up the claim at line 283 that they "turned [13] into a weapon for
both".

---

## B. Diagram realism and readability

### B1. fig-jumbo: the "6th lineman" tag sits under X, not under #68
The note `at=(-3.6, -8.6)` lands closer to X (w = −11) than to #68 (w = −4.8). A beginner reads it as labeling the
receiver. Move it under #68: `at=(-2.6, -4.8)`. If it then crowds the left E, use `(-3.2, -6.0)`.

### B2. fig-jumbo: the Y and U rings overlap
U at `(OFF_BALL, WING_W + 0.3)` is about 1.7 yd from Y, and the gold rings touch. Use `P("U", "TE", -1.6, 7.2)`.
That is still a legal wing, and the rings separate.

### B3. fig-jumbo: jersey #68 collides with the Lions story
The film room right below it says #68 was Decker, the starting LT, and #70 (Skipper) was the jumbo lineman who
reported. Calling the generic jumbo lineman "68", with the announcement quoted as "Number 68 is reporting as
eligible", invites the reader to cross the wires. Use #79 in the figure, the caption and the quoted announcement.

### B4. fig-sub-strip: the defense stands in its alignment while the offense is still huddled
In panels 1–3 the nickel and base defenders are drawn in their set alignment at 1–12 yards while the offense is
9.5 yards back in a huddle. In real life the defense stands loose near the ball, eyes on the sideline signaler,
and aligns only after the huddle breaks. You don't need to redraw it. Add one clause to the caption: "(the defense
is drawn in its alignment for clarity; until the offense breaks the huddle it stands loose, watching its
sideline)". Everything else in the strip checks out: the timing (subs :34–:32, match :31–:26, set :16 before the
:15 radio cut), the umpire hold and release, the opposite benches, legal 12 vs Under-front 4-3 in panel 4 (1-tech
to the strength, 3-tech away, Sam on U) and the readable frame strip.

### B5. "T E" box collisions on the front in drills 2 and 3 and the dilemma panels
The SDE at w ≈ 4.0 abuts the SDT box and Y's ring. Nudge the SDE to w = 4.4 in `fix`, as in A1.

### B6. Drill 2 answer: give the defense its third option
The answer says the defense must either leave the Sam on Z or send a linebacker 15 yards out with F. A coach
would add the common answer: the **strong safety walks down over Z** (rolls to single-high) and the Sam stays in
the box. That keeps the box but leaves one deep safety, which is exactly what the offense's play-action is built
for. Add one sentence: "Or the safety comes down over Z and the defense plays with one deep safety, which is the
look the offense's play-action wants." This keeps the answer honest: every defensive answer costs something.

---

## C. Missing nuance a coach would insist on

### C1. Defenses substitute by *situation* as well as by personnel
The body teaches matching only by offensive personnel. In practice the defensive call sheet has packages by
**down and distance**: third-and-long dime, a short-yardage or goal-line package, two-minute. These come on at
the whistle, whatever the offense sends. Drill 3's last paragraph assumes this ("substituting into nickel on third
down") but the body never teaches it. Add 2–3 sentences in "What defenses actually do", for example: "Defenses
also substitute by situation: many have a third-and-long package and a short-yardage package that come on at the
whistle whatever the offense sends, and the offense's personnel then decides only the fine-tuning." The hook
benefits too. On third-and-1 against 22, a real defense brings its short-yardage group (a big DT on, a corner or
safety off), not just one linebacker for one corner. Consider "a cornerback and a safety jog off; a linebacker
and a 320-pound tackle run on."

### C2. How the defense actually reads the personnel: the personnel caller
The hook mentions "someone near the defensive bench shouting a single word". Name him. Every NFL defensive staff
has a coach (often a quality-control assistant) whose job is to ID the offense's grouping as the players come on
and call the package. The defense then signals it in or uses the green-dot radio. That is why the offense's
substitution and the defense's answer are nearly simultaneous on film, rather than strictly sequential as the
strip shows. It also explains offensive counter-tactics: sending personnel late, and **hybrid players who make the
caller's job hard** (next item).

### C3. "Who, not where" needs the hard case: hybrid players
The chapter covers TEs split wide and a FB lined up wide. It misses the case defenses actually lose sleep over:
**the player whose body type is ambiguous**. Deebo Samuel was a WR used as a RB, which on paper is 11 but on the
field plays like 21. Taysom Hill was a QB/TE. Patrick Ricard was a DL/FB, already named in the Ravens box. Offenses
use them precisely so the defense's personnel caller can't match. One short paragraph under "Personnel is who,
not where" would do it. Have the fact-checker verify any player-season attributions.
Data tie-in (`dl.py`): in 2019 about 420 offensive personnel strings contain a second QB or a defensive position,
for example "2 QB, 1 RB, 1 TE, 2 WR" and "1 RB, 1 TE, 2 WR, 1 LB". The chapter's `pers` code labels these "11"
even though only two WRs are on the field. That is about 1% of plays, so the charts don't change. But the
"Go deeper: where the numbers come from" box should say that hybrids are counted by roster position. Ideally the
code should send `rb + te + wr != 5` plays to "other".

### C4. Terminology dialects: the digits are the lingua franca, not what's in every playbook
The task brief asks about dialects, and the chapter is silent on them. Inside many playbooks, groupings carry
**word names** that vary by team. Commonly cited examples include "Regular" (21), "Ace" (12), "Pony" (two RBs),
"Heavy" and "Jumbo". The digits are what scouting reports, broadcasts and the data share. College also counts the
same way but leans on 10/20 groupings. Add a two-sentence "Go deeper" or a parenthesis after the digit rule. Note:
the fact-check removed the earlier "Regular" claim for lack of a source. This needs a citable source (Kirwan's
*Take Your Eye Off the Ball* or a Smart Football piece are the likely candidates) or must stay generic ("many teams
give each grouping a word name in the playbook").

### C5. Any offensive substitution triggers the hold, even like-for-like
Worth one clause in "The rules that protect the match": swapping a tired receiver for another receiver still
triggers the umpire hold. Personnel doesn't change, but the defense still gets its window. That's why up-tempo
offenses avoid even like-for-like swaps (rotating receivers only on stoppages), which strengthens the tempo point
that follows.

---

## D. Smaller accuracy and wording fixes

- **Lions film room, "penalty, no conversion":** the illegal-touching foul did not end the try. Detroit had to
  retry from farther back and failed. My recollection is that a Dallas offside gave another try that also
  failed. Have the fact-checker confirm the sequence. Suggested: "the conversion was wiped out, Detroit retried
  from farther back and failed, and the Cowboys won 20–19."
- **Jumbo data paragraph:** "Many scouts and coaching staffs would instead call the extra lineman a tight end and
  the grouping '13'" is asserted without a source. Soften it to: "Some charting services and staffs count an extra
  lineman standing at tight end as a tight end (making this '13'); others note it as '12 jumbo' or '6 OL'."
- **Jumbo text:** add half a sentence noting that the sixth lineman doesn't always stand at the end. Teams also
  put him *inside* in an unbalanced "tackle-over" look, where he is covered and can't report usefully (02-04 owns
  unbalanced lines; link it).
- **Receiver letters paragraph:** "X is the receiver on the line on one side" is contradicted by the 12 and 22 cards
  right above, where X is off the line because both TEs are inline. Change it to "**usually** on the line" and add
  "with two in-line tight ends, both receivers stand off the line so the tight ends stay uncovered." That is a
  nice free lesson that sets up 02-02.
- **fig-clue-clock (optional):** add a row "Defense's personnel answer (:34–:25)". The reader is told to watch the
  defense's substitution, and the chart has no bar for it.
- **10 personnel "why rare":** fine as written. Consider adding the stronger NFL reason: defenses can answer four
  WRs with dime, while an offense with an elite TE gets a matchup the defense can't sub against.

## E. Checked and correct (no change)
- The two-digit rule and the 5 − RB − TE math. All eight cards are legal (seven on the line, ends correct, TEs
  uncovered, X/Z on and off the line used consistently with 02-02). The depths are realistic: QB 1.9 under center,
  5 in the gun, 3.5 in the pistol; FB 4.5; TB 7.
- Umpire position (offensive backfield since 2010), the hold-the-ball rule and its last-two-minutes exception, the
  one-play rule with warning then 15 yards, 12 men = 5 yards, no protection when the offense doesn't substitute.
- The jumbo goal-line defense is a realistic gap-control 5-3 (B-gap tackles, nose, ends outside the end men, three
  LBs, three DBs) and the 2-yard-line geometry is right.
- Drill 1 (13 personnel with a TE split as X) is legal and realistic. The answer's base/45% figures match the data.
- Drill 3 is a realistic tempo trap. Trips with two flexed TEs against a stuck base 4-3 on third-and-7 is exactly
  how it is used.
- The film-room choices fit the spec and are accurately characterized: McVay 2017–19 11, the 49ers and Juszczyk 21,
  the 2019 Ravens' inverted tendencies (an excellent pick), and the Eagles' 2024 12 as a known tendency they beat
  anyway. Staffs and roles are labeled by season and agree with FACTS-current (Kubiak "2025 OC").
- Animation budget: one animation (the substitution strip), and the PDF strip tells the story.
- Footnotes are each referenced once. No on-field label is clipped by the field edge.
