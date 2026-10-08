# Coach / film review: 09-01 Field Goals, Extra Points, and the Punting Game

Reviewer role: NFL special-teams coach and film analyst. I checked the qmd as of 2026-10-08 01:36 against the
PDF built at 01:37. I rasterized all 23 pages at 80 dpi (`_pdfbuild/09-01-kicking-and-punting/coach/`) and looked
at all 16 figures and the table. I also read the factcheck report so I don't repeat it.

**Overall:** this is a strong, coach-literate chapter. It gets right the ideas most writers get wrong: the missed-FG
spot, the NFL-only gunner release rule and its 1974 origin, "step inside, don't give ground", muff vs fumble vs first
touching, KCI without a signal, "Peter", and returners staying out of the 10. It also handles selection bias in
the weather data honestly, and Predict 3 is a well-built rules drill. Formations are legal throughout: 7 on the
line in the FG, tight, spread and shield units.

I found **one diagram that is factually wrong** (the Predict 2 rusher count), **two diagrams with unrealistic punt
distances** (the shield-punt animation and the directional panel), a **mislabelled "older" formation** that is
really the NFL's base punt, a hook that contradicts the chapter's own rules, and a list of nuances a special-teams
coach would insist on. Items are in priority order.

---

## A. Must fix (football is wrong or misleading)

### A1. fig-predict-block: six rushers to the right of the snapper, not five
`blk` puts defenders at w = [-4.4, -1.0, **1.0, 2.6, 4.2, 5.8, 7.4, 9.0**], which is **six** to the punt team's right
and two to its left. The PDF shows the same thing. The caption, the "five on this side" label and the answer
("five of them on one side") all say five.
Fix, either way:
- Keep the picture and change the caption, label and answer to "six to the punt team's right of the snapper".
  Six against RG, RT, RW and PP is a clean overload.
- Or move one rusher across: `[-4.4, -2.6, -1.0, 1.4, 3.0, 4.6, 6.2, 7.8]`, which gives 3 left and 5 right.

### A2. fig-shield-punt (animation): the punt is a 32-yard shank, not a normal punt
`return_team(ret_d=32.0)` and `RET = (32.0, 1.5)` put the catch **32 yards past the line**, and the caption says
"about 46 yards away" from the punter. An NFL punt from your own 30 grosses about 47 yards. Your own figure gives
47.1 for 2025. So the returner should stand **44–46 yards past the line, about 58–60 from the punter**. As drawn,
the coverage looks better than it is: the gunners arrive at about 4.6 s and stand and wait for the ball.
Fix:
- Set `ret_d = 45`, `RET = (45.0, 1.5)`, and stretch the gunners' last waypoint to about d = 44, and the
  vices' and lanes' waypoints with them. Keep KICK_T = 2.0 and CATCH_T = 6.4 (a 4.4-s hang is realistic).
- Change the caption to "the returner (PR) about 45 yards past the line, some 60 yards from the punter". Change
  the panel-1 note the same way.
- Punter path: `sp.path("P", [(-10.5, 0.0), ...], delay=0.9, speed=4.0)` moves him about 3.5 yards forward
  **before** the kick, so in the 2.0-s panel the punter's dot is a couple of yards in front of the ball
  (`punt_ball` has the ball at -12.4). Hold him until KICK_T, or end his pre-kick movement at d ≈ -12.4.

### A3. fig-directional, right panel: the "directional" punt from your own 25 travels only 37 yards
LOS x = 35 (your 25) and the ball lands at x = 72 (their 38). That is a 37-yard gross, well short of a normal
directional kick. Fix: land it at about x = 80–81 (their 29–30), toward the numbers (y ≈ 10.5–12). Move the PR
there, shift the five coverage markers and arrows about 14 yards downfield (x ≈ 66–75), and move the shaded
"little room" box with them.

### A4. fig-punt-formations caption: the spread punt is not an "older" formation
The caption says "Two older punt formations" and calls the shield "modern". The spread with wings about 1 yard
off the tackles' outside hips and a PP 5–7 yards deep is the **NFL's base punt formation today**. The
three-across shield with the line releasing at the snap is the **college** model, and some NFL units borrow it.
Under NFL release rules the NFL "shield" is usually the two wings and the PP forming a triangle in front of the
punter. As written, a reader who watches an NFL punt next Sunday will see the "older" formation.
Fix:
- Caption: "Left, a tight punt, now a backed-up or emergency look. Right, the NFL's base spread punt: gunners
  outside the numbers, five interior linemen, two wings a yard back and the PP about six yards deep."
- Panel title: "Spread punt (the NFL base)".
- Text: in "The NFL's standard is the spread family …" and the shield paragraph, say outright that the
  three-man shield grew up in college, where everyone may release at the snap. NFL teams mostly line up in spread,
  and the wings and PP act as the "shield". This also reconciles the curriculum's alias (shield | spread) with a
  figure that currently shows them as two different things.
- Optional: retitle fig-shield-punt "a college-style shield, run under NFL release rules", or rebuild it from
  `spread_punt()`, since the animation explicitly applies the NFL rule.

### A5. Opening hook: the returner waves for a fair catch and then lets the ball drop
"The returner stands under it, waves one arm over his head, and lets it fall." Under the rules the chapter teaches,
an uncaught ball after a fair-catch signal is live and can be downed or muffed. A returner who signals almost
always catches. This also makes the "what was that wave?" payoff muddled.
Fix: "…waves one arm over his head, catches it at the 9, and nobody lays a finger on him."

### A6. fig-fg-operation, panel 3 label contradicts the caption
The panel label says "ball down, kicker plants". The caption says the kicker "is on his second step", and the
strip shows K still about 1.5 yards behind and to the left of the ball. Change the label to "ball down,\nkicker
on 2nd step". The plant comes at about 1.2 s.

### A7. Muff/first-touching "free play" may be overstated (verify)
Rule 3 of the kicked ball says "if things go wrong his team still gets the ball at the spot of first touching". The
rule's own footnote says the option is "disregarded if … there is a change of possession". Here is a case to
check against Rule 9-2-2: K first-touches, R picks the ball up (possesses), R fumbles, K recovers. Does R keep
the option? If not, narrow the sentence to "a returner can pick it up and try to run, and if he is tackled behind
the spot, his team takes the spot". Factcheck should rule on it.

## B. Diagram polish

- **fig-fg-protection:** the purple highlight ring on the outermost rusher (L5) sits on the end of the "overload:
  six on one side (the limit)" label. Move the label to about (d 4.2, w -9.8), or put it on two shorter lines
  further left.
- **fig-return-vs-safe, Return wall panel:** the text says "vices ride G", but the four vices never move, so
  they stand at the line while the gunners run 28 yards. Give each vice a path that parallels its gunner (outside
  vice on the gunner's outside hip, inside vice inside). Without paths the right gunner's arrow also slices through
  the wall-forming arrows and reads as if he ran through the wall. With the vices escorting him outside, that
  reads as intended.
- **fig-return-vs-safe, Punt safe panel:** LB2 has no assignment, and the punter (a back, so eligible) is not
  covered, so "every eligible covered" isn't quite true. Add `ps.man("LB2", "P")`, or label LB2 "spy: punter /
  run". Coaches call this player the "rat" or "spy" in punt safe.
- **fig-punt-heatmap:** the bottom row label "their 51+" means the kick finished on the *punting* team's side of
  midfield. Relabel it "beyond midfield (51+)" or "own side of 50".
- **fig-directional left:** the "1 coffin corner" label sits on the painted "10" on the right. Nudge it to y ≈ 6
  or x ≈ 95.
- **fig-predict-muff:** the punt arc starts at the 26 and is labelled "punt from midfield". That is fine as a stub,
  but add "(flight shortened)" or start the arc at the window edge so it doesn't read as a 17-yard punt.
- **Consistency with 01-03:** 01-03 puts the holder "~7 yards back". This chapter says 8 in the fig-fg-geometry
  caption and "7 or 8" in the text. Suggest "about 7 to 8 yards (scorers count 8, which is where 'add 18' comes
  from)". The 87% at exactly +18 mostly reflects the **scoring convention**, not a measured spot. Say so in a
  clause after the [^fg18] sentence.
- Spot checks that are right and need no change: holder on the kicker's right for a right-footed kicker, kicker
  about 2.5 back and 2 over, laces out, wings a yard behind and outside the ends, and the defenders beside the
  snapper outside his pads. Wind arrow direction in Predict 1 is correct.

## C. Missing nuance a coach would insist on

1. **Icing the kicker.** It is the one kicking-game tactic every viewer sees, and it isn't mentioned. A timeout
   called just before the snap. Teams may not call back-to-back timeouts in the same dead-ball period, so you
   can't "double-ice". Kickers often get a free practice swing when the whistle comes late. Add two sentences in
   "The operation". (Factcheck the rule cite: the 2012 consecutive-timeouts rule.)
2. **The "Fire!" call.** On a bad snap or a bobbled hold, the holder yells a code word ("Fire!" in most
   systems). The ends and wings release as receivers, and the holder scrambles to throw or run. It belongs next
   to the "slow operation" paragraph and sets up the fakes section.
3. **The long snapper's protection.** He is a **defenseless player** on FG, try and punt snaps (no forcible
   contact to his head or neck while his head is down). That, plus the no-one-over-the-snapper rule, explains why
   block units can't simply bulldoze him. (College has a stronger 1-second snapper-protection rule.)
4. **Roughing exceptions.** There is no foul if the rusher touches the kick, or if he is blocked into the punter.
   This is why a "whiff" near the ball usually gets no flag, and viewers ask about it every week. Add one clause to
   the punt-block paragraph.
5. **Backed-up punting.** Inside the own 5 the end line caps the punter's depth. He can't stand 14–15 yards
   back, so he aligns at the end line (about 11–12 yards from a LOS at the 2), and the operation gets tighter.
   Late in a game, the punt team sometimes takes an **intentional safety** instead. One paragraph in the
   tight-punt text, linked to 10-04.
6. **Scrimmage-kick numbering exception.** On punt and FG formations, players with eligible numbers may line up
   at interior line spots and are ineligible there without reporting. An ineligible-numbered player at end must
   report to be eligible, as Gilliam did. This is why punt units are full of linebackers and safeties at "line"
   spots, and it explains the Seahawks fake. One sentence in the fakes section.
7. **Terminology dialects: vise vs jammer.** In most coaching vernacular a **vise** (usually spelled "vise", like
   the tool) is the *two-man* bracket on a gunner. A single defender on a gunner is a **jammer** or "single
   jam". The glossary treats them as exact synonyms, and Predict 2's "one vice per gunner" is really "single
   jams". Suggest: keep the curriculum alias, but add a half-sentence: "Strictly, coaches call the two-man bracket
   the vise and a lone blocker a jammer; the BDB/PFF data spell it 'vises'."
8. **Protection scheme in the spread punt.** Name it in one line: most NFL units use a zone/slide protection
   with the PP "IDing" the most dangerous rusher, or a big-on-big man count. That makes the Predict 2 answer
   ("slides the protection") land.
9. **Show-block, drop-return.** The Predict 2 answer should add that return teams sometimes show this exact
   overload and then peel into a return. Eight on the line is a strong tell, not a guarantee.
10. **Kicker footwork/hash.** The NFL's narrow hashes make the hash much less important than in college, but
    kickers still have a preferred hash (many right-footers like the left hash, where their natural draw starts
    outside). That is why you still see third-down runs to "spot the ball". Optional.

## D. Film room

- **Tucker, Aubrey, Little:** accurately characterized and well chosen. Little's setting note (indoors) and the
  2025 K-ball tie-in are exactly the right "what to notice".
- **Seahawks fake FG (Jan 18 2015):** good. Add the numbering detail from C6 (he wore 79 and reported).
  Optionally add that Ryan rolled **left**, away from the rush.
- **The spec asks for "notable fake punts", and the only fake-punt example is the Colts' failure.** Add one
  well-executed fake punt that matches fig-fake (a direct snap to the up-back or PP). One candidate to verify in
  nflverse: **Chiefs at Bills, AFC Divisional, Jan 21 2024**, a direct-snap fake punt to
  **Damar Hamlin** for a first down in the third quarter. The `(Punt formation)` filter in the chapter's code will
  confirm or reject it in seconds. For the Colts play, name the snapper (WR Griff Whalen over the ball, safety Colt
  Anderson behind him) so readers can find it.

## E. Data / gridiron

- The two strips use gridiron simulated tracking, labelled "simulated tracking in Big Data Bowl format". Good.
  **There is no `eval: false` real-data cell**, though the book convention asks for one next to simulated BDB
  figures. This topic has a perfect source: the **2022 Big Data Bowl was special teams** (2018–2020 punts,
  kickoffs and FGs). Its PFF scouting file has `snapTime`, `operationTime`, `hangTime`, `kickDirectionIntended`
  and `kickDirectionActual`, plus `gunners`, `vises`, `puntRushers` and `specialTeamsSafeties` by jersey. Add a
  short `eval: false` cell after fig-shield-punt using `gridiron.bdb.prepare()`. Point it at a 2022-BDB punt and
  mention that `operationTime` and `hangTime` let a reader check this chapter's 2.0-s and 4.5-s numbers on real
  plays.
- `with_ball()` (replacing gridiron's QB-centric ball with a kick flight) is a sensible in-chapter workaround.
  Note it for the gridiron maintainer: a `kick` ball model (snap → hold/catch → flight to a landing point) would
  serve 09-01 and 09-02.
- Four strips/animations at most: this chapter has two. Fine.
