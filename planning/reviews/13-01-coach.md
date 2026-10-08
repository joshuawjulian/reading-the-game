# 13-01 Working with nflverse Data in Python: coach and film-analyst review

Reviewer role: a veteran NFL coach and film analyst, checking technical football accuracy and completeness.
I read the full qmd and looked at all 34 pages of `pdfs/13-01-nflverse-in-python.pdf` (built 08:12, after the
08:11 qmd), plus the field diagrams re-rendered at 110 dpi. I ran three data checks in `rtg`: the Walker row in
participation, accepted holds on designed runs in 2025, and the 01-06 guesser definition.

**Verdict:** the data teaching is sound, and almost every football statement in the prose holds up. The
weak spots are the **four field diagrams**. They use gridiron defaults that a coach would reject on sight:
an uncovered slot in two diagrams, an unsound 4-3 against 12 personnel, no play-side blocks, and routes on
3rd-and-8 that stop short of the sticks. The frame strip also does not show what its caption says. One drill
answer (holding) needs a data nuance that I confirmed in the data. All of these are cheap to fix.

---

## A. Must fix (wrong or misleading football)

### A1. Fig 11 `fig-row-to-play` (and the Fig 12 frame strip): the nickel is lined up over the tight end and the slot is uncovered
- **What's drawn:** `defense("nickel", "single_high", off)` against `offense("singleback")`. The receivers are
  2x2: Y (inline) and Z to the right, X and H to the left. On a tie, the helper puts the nickel `$` over the
  right-side #2, which is the **inline Y** (w ≈ +5.3, d 5). The SS is also rolled down on that side
  (w +6, d 7). The left slot **H (w −9) has no defender within about 9 yards**, and the C is alone outside on X.
  No NFL nickel aligns this way against 11 personnel. It hands the offense a free bubble or glance. It also
  makes Walker's "left end" run look like a run into a hole the defense left on purpose.
- **Fix:** put `$` on the slot, apexed between the LT and H, and keep the SS down to the TE side as the 8th
  box player:
  `dfn = [p.moved(d=4.5, w=-7.0) if p.key == "NB" else p for p in dfn]`. That alignment is close enough to
  count as "in the box" for an 8-man box, so widen the dashed box to w −7.8…+7.6, or say in the caption that
  the apex player is borderline. This matches the data. Participation says
  `3 CB, 2 DT, 1 FS, 2 ILB, 2 OLB, 1 SS`, 8 in the box: five DBs, with the SS down and the nickel in the box.
- **Wording:** the caption's "three cornerbacks (a nickel defense)" should read "five defensive backs (three
  corners, two safeties): nickel". Nickel is defined by five DBs, not three corners. The data also lists two
  **OLBs** and two DTs, so the "E" labels are really stand-up edge players (a 2-4-5 nickel). Either label them
  `OLB`/`E`, or add "(edge players, labelled E)".

### A2. Fig 11: the run arrow ends on the yellow line, and nobody blocks
- `run("RB", ...)` offsets are relative to the back's start (d −7), so the last point (17, −12) lands at d 10,
  **exactly on the line to gain**. The picture reads as a 10-yard gain. Use about `(24.0, -12.5)` so the arrow
  runs out of the window (window top is 15), which matches "+30 yds to NE 46".
- The back's path bends at the LOS **right through H's spot** (w −9). On a left-end run, H is a blocker: draw
  `block("H", target="NB")` (a crack or arc on the apexed `$` after the A1 fix) and `block("X", target="LCB")`
  (stalk). Otherwise the picture shows a 30-yard run with no one blocked.
- **The FTN RPO tag is missing.** The chapter's own printout shows FTN `is_rpo = True`, but the caption lists
  only "quarterback under center". Add "FTN also tags it a run-pass option". Optionally draw H's pass option as
  a short dashed glance or bubble labelled "RPO option (typical, not charted)". Readers learn here that the
  flags are judgements, and that this play is an under-center RPO, which is unusual and worth noticing.

### A3. Fig 12 `fig-walker-anim` frame strip: the caption claims a moment the frames don't show, and labels collide
- The caption says "the run past the yellow line", but at +2.6 s the back is about 3 yards **short** of it
  (d ≈ 7). After the A2 path fix, use `times=[0.0, 0.8, 1.6, 3.4]` (or whatever puts the last frame beyond
  d = 10).
- **21 of 22 players are statues**, including the QB (no carry-out fake, even though FTN says RPO) and every
  defender. For a film-literate reader, a strip where the Will, the Mike and the corner never move while a
  back runs past them is misleading. At minimum, add pursuit paths for W, M, `$` and the play-side C (W fast
  flow over the top, C coming up to fit) and a QB fake or read path. The caption already says the motion is
  simulated, so typical pursuit is fair.
- Inside the frames the painted yard numbers ("30" and "40") sit under the **C** labels on both sides,
  because `drop_numbers` is applied to Fig 11 but not to the animation. Check whether `show_animation` takes a
  numbers-off option. If not, widen `lateral` so the corners clear the numbers.

### A4. Fig 13 `fig-drill-row` (Drill 1): an unsound 4-3 against 12 personnel
- The 4-3 Over puts the Sam (w +5.6) **and** the SS (w +6, d 7) outside Y. The U side (w −4.8) has the weak
  end in a 5-technique **inside** U and nobody outside U: no D-gap defender, no force player. Against a
  balanced 12-personnel set on 3rd-and-2, that is a free off-tackle run to the U side. Real 4-3 teams
  "split the strength": the Sam goes to one tight end and the SS walks down to the other.
- **Fix:** `SS → d 5.5, w −6.5` (down outside U). Optionally tighten both corners to about 5 yards off, since
  it is 3rd-and-2 against two TEs. The answer doesn't depend on any of this, but the picture is the first
  thing a coach looks at.

### A5. Fig 14 `fig-drill-scramble` (Drill 2): "everyone covered" is not what's drawn, and the routes ignore the sticks
- **Uncovered slot again.** In gun 2x2, the helper puts `$` over Y (right), and the Will stays in the box at
  w −2. **H (w −9) has nobody over him**, while the prompt says "everyone covered". In two-high nickel against
  2x2, the Will walks out to an apex over the other #2: `W → d 5, w −6.5`. If this is meant to be 2-Man (the
  classic two-high man coverage), the Mike takes the back.
- **Routes on 3rd-and-8 stop short of the sticks.** H and Y run mirrored 6-yard inside breaks that converge
  on the Mike, two yards short of the line to gain. X and Z run straight 10-yard stems with arrowheads, which
  read as unfinished routes. No NFL staff draws third-and-8 that way. Suggested routes:
  X and Z `[(0,0),(18,0)]` (go routes that clear out and exit the window); H `[(0,0),(9,0),(9,-3)]` and Y
  `[(0,0),(9,0),(9,-3)]` (sit or option routes just past the sticks, both covered). The picture then shows
  "covered past the sticks, so the QB runs".
- **Coaching nuance to add to the answer:** two-high man (2-Man) is the coverage most exposed to QB scrambles,
  because every underneath defender has his back to the quarterback. That is why defenses facing mobile
  quarterbacks add a spy or rush-contain against it. It is one sentence, and it ties the data drill to the
  football.
- R is set beside Q and does nothing. Give him a protection step (`block("RB", target="WILL")`, or a short
  path to the A-gap) so the 5+1 protection is visible.
- The "scramble: +9" note box touches the QB's arrowhead (note at d 10.8 and the tip at about d 9.5–10).
  Move the note to `at=(12.0, 0.5)` or `(6.0, 11.5)`.

### A6. Fig 15 `fig-drill-holding` (Drill 3): an off-tackle run with no play-side blocks, and the arrow runs through the end
- The back's path crosses the LOS at about w 3.7, **straight through the 7-technique E's label** (d 1,
  w 4.2). It then runs past the Sam and the SS, who are 1.5–2 yards away and unblocked. The only block drawn
  is the backside LT on the WDE. Draw a scheme. Inside zone or duo to the right is the simplest consistent
  one: `Y + RT` double the 7-technique E up to the Sam, `RG + C` double the 3-technique up to the Mike, and
  `LG` and `LT` cut off the backside 1-technique and 5-technique. That last assignment is exactly where
  backside-tackle holds come from, so the drill's story improves. Aim the back at the RT's outside hip, so
  the path bends off the double team instead of through a defender.
- The LT's orange highlight ring cuts through the WDE's "E" box (the WDE is at w ≈ −4.0, d 1). Shrink the ring
  or nudge the WDE to w −4.4. A 5-technique is drawn a little wide anyway.

### A7. Drill 3 answer: not every accepted hold on a run is a `no_play`
I checked this in the data. In the 2025 regular season there were **238** accepted offensive holds on designed
runs (`rush == 1`):
**176** are `play_type == "no_play"` and **62 (26%)** are `play_type == "run"`. The 62 are holds **beyond the
line of scrimmage**, such as a receiver or a climbing lineman at the second level. These are enforced from
the spot of the foul, so the run counts up to that spot. Example: "(14:36) 7-B.Irving right end to ATL 42 for
11 yards … PENALTY on TB-62-G.Barton, Offensive Holding, 10 yards, enforced at TB 49."

The drill's specific case is right. A hold by the left tackle at the line is enforced from the previous spot,
giving 1st-and-20 at the 15, and the play is a `no_play`. But the answer and the `N_HOLD` sentence read as if
every hold on a run is a `no_play`. Add one sentence: "A hold downfield (by a receiver, say) is different: the
run counts up to the spot of the foul, the row stays `play_type == "run"` with `penalty == 1`, and your filter
keeps it, about a quarter of holds on runs in 2025." That is a real filter trap, and the chapter is about
filter traps.

---

## B. Should fix (nuance a coach or analyst would insist on)

1. **`pass` records what happened after the snap, not the call, on RPOs** (lines 602–604, 633–636 and the
   Drill 2 answer). The chapter says the flags "tell you what the offense *intended*" and that `pass == 1` is
   "what the offense called". On an RPO, the call is a run-pass option, and `pass`/`rush` record the QB's
   post-snap decision. Walker's run, which FTN tags RPO, is the chapter's own example. Add one sentence:
   "Exception: on an RPO the flags record what the quarterback chose after the snap; FTN's `is_rpo` is the
   only place the call shows up." Screens and play-action are also "passes" under the flag. That is right for
   play-calling, but say so.
2. **"First-and-10 is where play-callers most want to be unpredictable, and they are"** (Film room,
   lines 1194–1200). The league's 44–49% is an average across teams, personnel and formations. Per snap,
   first-and-10 is quite predictable once you see the formation. 01-06 showed QB alignment alone adds about
   7 points of guessing accuracy, and 12 or 21 personnel under center is heavily run. Reword: "The scorebug
   alone tells you almost nothing on first-and-10; the formation tells you a lot, which is why Part 2
   exists." Otherwise the chapter contradicts 01-06 and the book's thesis.
3. **The third-down decline mixes distance with play-calling** (lines 1204–1208). "More third-and-short runs"
   could mean more third-and-shorts (better early downs, or the tush push setting up 3rd-and-1) or more runs
   on 3rd-and-short. These are different stories. Either show third-down pass rate inside the chapter's own
   distance buckets for 2015–2019 against 2025, or reword to "partly because the mix of third-down distances
   changed and partly …". It is a natural extension exercise for this chapter.
4. **Personnel strings are roster positions, not roles** (Rule 2, line 979, and the parser). "Both suppliers
   could count backs and tight ends, so personnel survives" is true for the count, but a coach will point out
   three limits. (a) A sixth offensive lineman reporting as eligible ("jumbo") is silently dropped by
   `count(..., {"TE"})`, so a 6-OL short-yardage set is filed as 11 or 12 personnel. (b) A FB-listed player
   (e.g. Patrick Ricard, Ravens) versus a TE used as a fullback depends on the roster label. (c) Personnel is
   not alignment: 12 personnel with the TE split wide plays like 11. Add a short "personnel is who, not where"
   caveat. Optionally add an `ol > 5` flag to the parser (FTN strings carry `C/G/T` counts; NGS 2016–2022
   lists linemen only when there are more than 5, as the chapter already says).
5. **The FTN pistol spike is a within-supplier artefact** (cross-check table: pistol 3.9% in 2023, **9.3%** in
   2024, 4.9% in 2025; the same bump is visible in Fig 7). Pistol usage did not more than double and then
   halve. This is a good second lesson for "every column is somebody's judgement": a series can break with
   no change of supplier. Mention it in the paragraph after the cross-check table.
6. **The pbp `shotgun` flag "has no source break", but it is not uniform** (line 1014). It is typed by each
   game's home stat crew, so there are about 30 recorders and the convention can differ by stadium (as the
   Walker play shows). Say "no change of supplier" rather than implying a single consistent recorder.
7. **Drill 1 answer, "the *next* row".** In the second quarter, the next row after a 3-yard run can be a
   timeout, the two-minute warning or an end-of-quarter row with no down. Say "the next row with a down", or
   use `lead()` within `drive`. That is the same "a row is not always a play" lesson from earlier in the
   chapter.
8. **Garbage-time paragraph** (lines 684–688). "Drops eight players into coverage" is fine as prevent, but the
   bigger football point is that the *trailing* team's defense also changes. Leading teams face soft
   two-deep shells and prevent, which inflates their run success. That is a second reason the filter matters
   for **efficiency**, not just for play-calling rates. One clause would cover it.

---

## C. Checked and correct (no change)

- `yardline_100` explanation, the Fig 3 geometry (SEA 24 → 76 → x 34; NE 46 → 46 → x 64; ruler direction) and
  the red-zone `<= 20` rule.
- Scramble = `play_type "run"` with `pass == 1`; sack = `play_type "pass"`; two-point tries have no down;
  kneels and spikes have their own types.
- Holding enforcement in Drill 3: a foul by the offense behind or at the LOS on a run that ends beyond the
  line is enforced from the previous spot (NFL; NCAA differs), so 1st-and-20 at the 15 is right.
- The formation-label break (NGS describes the backfield; FTN describes the QB's spot; empty folded into
  shotgun), the personnel format change, COVER_9/COMBO/BLOWN, `ngs_air_yards` NA from 2024, and the man-share
  artefact all match FACTS-current §7.
- Drill 1 and 2 data answers; the 01-06 down-and-distance guesser definition matches 01-06 exactly; "ace" =
  12 personnel, two TEs, one back; 4-3 Over has the 3-technique to the TE side (correct).
- Fig 13 and Fig 15 formations are legal (7 on the line; in singleback Z is off the ball, so Y is the
  eligible end; in ace X and Z are off and both TEs are on).
- The 2004 illegal-contact emphasis reference and the fourth-down distance argument (backed by an assert).
- Animation count: 1 (within the limit of about 4).

## D. Notes for the gridiron maintainer (do not edit gridiron/ from this chapter)

- `defense()` nickel placement: with a 2x2 set that includes an **inline TE** (`singleback`, `pistol`) or a
  slot TE (`gun_2x2`), the tie-break sends the NB to the right-side #2 (the TE). The other slot is left
  uncovered, and with `single_high` the SS also rotates to the same side. Suggested rule: the NB goes over
  the slot **WR** (not the TE) and the rotated safety goes to the TE side. For `two_high` against 2x2, walk
  the Will out to apex the uncovered #2.
- `4-3_over` against a balanced 12-personnel set (`ace`): nothing outside the weak-side TE. Suggest the SS
  roll down to the weak-side TE when `off` has two inline TEs.
- `show_animation` has no way to suppress the painted yard numbers (cf. the chapter's `drop_numbers`
  helper), so labels collide in frame strips.
