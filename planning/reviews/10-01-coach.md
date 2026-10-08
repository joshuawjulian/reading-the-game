# Coach / film review: 10-01 Early Downs and Field Zones

Reviewed 2026-10-08 against the current `pdfs/10-01-early-downs-and-field-zones.pdf` (newer than the
.qmd). I rasterized every page (80 dpi), looked at diagram pages 9, 10, 13 and 16–18 again at 120–220 dpi, and
re-simulated the shot play in the `rtg` container to check ball, route and safety timing.

**Verdict:** the football is sound and the chapter reads like a real staff's call-sheet logic. The
schedule, second-down buckets, the shot-play logic, the four-down-territory point and the light-box read
in drill 2 are all right. Most of the problems are in the diagrams: one wrong mesh point on the goal line, text collisions on the
zone map, a frame strip that ends before the catch, and a pistol depth that doesn't match its caption.
Field-goal arithmetic (LOS + 18) checks out (Tucker's 66 was from the 48), so no change there.

---

## Must fix

1. **Drill 1 answer: "the usual worst case for a stuffed run is second-and-12 at the 1, not a safety" is
   wrong for the look drawn.** LOS is the own 3 (`LOS1 = 13`). R is at d = −6.5, 3.5 yards deep in the end
   zone. From under center with a 6.5–7-yard back, an inside-zone or duo mesh happens about 4–5 yards
   behind the LOS. That is *in the end zone* or on the goal line, so a 2i or 3-technique who penetrates and
   makes the tackle at the mesh scores a safety. Fixes:
   - Text: "...the quarterback takes the snap in the field of play, and the handoff comes right around the
     goal line, so the call has to hit fast. Backed up this tight, staffs cheat the back up a yard or two
     and use downhill runs (dive, iso, duo, the sneak). They cross off anything with a deep mesh or a long
     lateral path: stretch, toss, counter with pullers."
   - Diagram (optional, to match): move R to d = −5.5 in `fig-predict-backed-up`, and to d = −5.5 in panel B of
     `fig-backed-up`. Panel B's caption ("gets the ball near the goal line moving out") is already
     accurate.

2. **Field-zone map (`fig-field-zones`): lines run through text.**
   - The dotted "field-goal range begins" line at x = 75 runs through "FOUR-DOWN", "(the fringe)" and
     "part of the plan". Move that zone's text block right: `NAME_AT["four-down\nterritory"] = 81.5`, with the
     "(the fringe)" label at x = 81.5 too. Alternatively, give those three texts the light `bbox` the chapter
     already uses in `say()` (fc=SURFACE, alpha 0.92) so the line passes behind them.
   - The faint `Field` yard lines run up through both bracket captions ("minus|territory", "PLUS
     TE|RRITORY", "+4|9") and graze "BACKED UP". Fix: add a bbox (fc=SURFACE, ec="none") to the
     `bracket()` text and to the zone names, or stop the Field's yard lines at `top` by drawing the field
     with `lateral=LAT` and clipping lines to the axes' data range.
   - Nice to have: label the two marker lines' yard lines ("−35" under the triangle, "+35" under the
     dotted line). A reader can't otherwise tell the touchback is at the minus 35.

3. **Shot-play frame strip (`fig-shot`) ends before the catch.** Re-simulated: the ball is released at
   3.1 s and reaches Z at **4.6 s**, at d ≈ 16.5, w ≈ −10. At 4.4 s (frame 4) the ball is still 2.8 yards
   short, so the print story ends mid-flight. Use `times=[0.0, 1.0, 3.1, 4.6]` (snap, fake, release,
   catch). Frame 3's note becomes "the throw: the free safety has carried the post"; frame 4's becomes
   "caught behind the linebackers, in front of the corner".

4. **Deep-over depth doesn't match 04-04.** 04-04 defines yankee's over at "about 18–22 yards". This Z
   flattens and is caught at 16.5. Raise the route: `p.route("Z", [(7.0, -1.0), (17.0, -9.0), (20.0, -24.0)],
   frame="field")`, then re-check the catch time and the LCB's depth (keep LCB at (21, −18) so the corner
   stays deeper than the catch point). Also, X's post stops dead at 23.5 yards from 4.0 s on. Extend it
   to (28, 11) and widen the strip window to `window=(-10, 30)` so X never sits on the top edge (it is
   about 2.5 yards inside it now).

5. **Drill 3 pistol depth contradicts the caption.** The caption says "the quarterback four yards behind
   the center", but the code has Q at d = −3.5, which is 2.8 yards behind the center (C is at −0.7). An NFL
   pistol QB is about 4 yards from the ball, with the back about 3 yards behind him. Set Q to d = −4.0 and
   R to d = −7.0, and change the caption to "about four yards behind the ball".

## Should fix (accuracy and nuance a coach would insist on)

6. **Shot play: name the coverage, and say what changes against man.** The read described ("the free
   safety can't cover both") is the Cover 3 read, and the CBs bail to deep thirds in the animation, so
   say "Cover 3" in the caption and in note 1. On second-and-1 many defenses play **Cover 1** (man) out of
   this same eight-man, one-high look. Against that, yankee still works, but the over becomes the
   man-beater, a crosser running away from his defender's leverage. One sentence prevents the reader
   from thinking the read is "always the safety".
   - Consistency: 04-04's yankee plate uses a 7-man protection, with U releasing late as the outlet (3).
     This chapter uses an 8-man max protection with no outlet. Both are real, but add "(max protection;
     some teams release a tight end late as an outlet)" so a reader comparing the two doesn't see a contradiction.

7. **Second-and-short, point 2 ("defenses answer it like one: base personnel...").** In the NFL, defensive
   *personnel* follows the offense's personnel, not the down. A defense is in base on second-and-1
   mainly because the offense came out in 12/21/22. Merge points 2 and 3 into one causal chain: heavy
   offensive personnel draws base personnel, base personnel plus the run tendency puts eight in the box,
   and eight in the box leaves one deep safety. Against 11 personnel on second-and-1, most defenses stay
   in nickel and walk a safety down. That "nickel with a safety down" picture is a shot look of its own.

8. **Backed up: "quarterbacks told to throw the ball away rather than take the loss".** In the end zone
   that instruction has a hard limit. Intentional grounding by a passer in his own end zone is a
   **safety**. A legal throwaway needs the QB outside the tackle box and the ball reaching the line of
   scrimmage. Add one sentence. It is also the real reason backed-up passes are quick or rolled out (the
   rollout gets him out of the tackle box). Cite NFL Rule 8-2-1 and the safety rule 11-5 the fact-check
   already used.

9. **Backed up: the punter.** "The punter can't stand at his usual depth" is right; give the numbers.
   The usual depth is about 14–15 yards. At the own 2 the end line is 12 yards behind the ball, so he
   stands at about 11 with his heels on the end line. That shortens the operation time and makes a
   blocked punt (a safety, or a touchdown for the defense) the special-teams fear in this zone. One clause
   is enough.

10. **The script.** A coach would add a sentence in "The situation comes before the play": most NFL
    play-callers *script* their first 10–15 calls (Bill Walsh popularized it), and many of a team's
    first-quarter first downs come off the script rather than the situation boxes. That also qualifies the "first-half early-down run rate" panel: some of
    that rate is pre-planned rather than reactive, which supports the chapter's point. Link to 08-03
    (game planning) for the details.

11. **Shot boxes the chapter half-mentions.** Call sheets usually have explicit shot triggers beyond
    second-and-short: **sudden change** (the first snap after a takeaway, when the defense on the field
    has just run off and the offense takes a shot), the first first down after **crossing midfield**
    ("plus-territory shot"), and the **coming-out shot** the chapter already mentions. Add one sentence
    listing them, in the second-and-short section or in "Plus territory". The "we got the ball in plus
    territory after a turnover" line in the zone list is the natural place to tie in sudden change.

12. **Rams 2018 film room: the missing coaching detail is personnel sameness.** McVay's 2018 Rams lined
    up in 11 personnel on the large majority of snaps (roughly 90%; verify with FTN/PFF or nflverse
    participation data). So the defense got no personnel tell, and the run and the play-action came from
    identical personnel *and* formations. That is how "runs that look exactly like their passes" actually
    gets done, and it is the specific lesson 13-04 builds on. Add one sentence (have the fact-checker
    attach the number).

13. **"Free play" (opening paragraph).** The analyst calls second-and-1 "a free play". Broadcasters say
    that, but on the field "free play" means a snap on which the defense has jumped offside, so the offense loses
    nothing whatever happens. A short parenthetical ("announcers say 'free play'; strictly, coaches save
    that for a snap where the defense jumped offside") would keep a reader from mixing the two up when the booth says it
    after a neutral-zone flag.

14. **Field zones: backed-up sub-zones.** Many staffs split the deepest zone again: a "tight" or
    "minus 1 to minus 3" box where even under-center play-action is restricted and the sneak and
    quick-hitting runs dominate, and minus 4 to minus 10. The chapter's footnote already quotes Hauser's
    "avoid punting from the −1 to −4". Promote that to the body as one sentence. It explains why drill 1
    (at the −3) is more extreme than the "backed up" averages.

15. **Drill 2 answer and the watch-for-it checklist say "lean run" after an incompletion.** The data says
    a pass is still 56%, as the answer itself says. In the checklist, write "(less pass than usual; still
    a coin flip)" so a reader scoring himself doesn't learn to guess run on second-and-10.

16. **Drill 3 answer: "the offense would almost certainly throw".** At the own 38 the data gives about
    six in seven (86%). Say "probably throw, about six times in seven", in keeping with the book's
    real-ranges rule.

## Diagram-by-diagram notes (beyond the fixes above)

- **fig-shot:** legal formation (7 on the line: 5 OL + Y + U; X and Z off). The 4-3 with the SS walked down
  on the U side and the Sam over Y is a credible eight-man front against 12 personnel. The 8-man
  protection count is right (5 OL + 2 TE + R). The QB's play-action set depth (about 8 yards) and a 3.1 s release are
  realistic for a 7-step play-action shot. The rings work. The LB "step up then chase" timing reads well.
- **fig-field-zones:** zone boundaries match the text and glossary. Kickoff touchback at the −35 matches
  FACTS-current (the 35 is unchanged in 2026). The "open field" band crossing midfield to the +40 is
  consistent with the text. Collisions as in item 2.
- **fig-backed-up:** legal in both panels (A: X and Z on the line, H and Y off; B: U and Y on the line,
  X and Z off). Panel A: the LE's loop path brushes the H marker. Tighten the first waypoint to
  (−3.5, −1.6) so the rusher arcs around the tackle instead of through the slot. The OL pass-set dashes
  read as "blocks backward". Fine.
- **fig-predict-backed-up:** a believable 4-3 over against 12 personnel with the SS rolled down outside Y
  (eight near the line, one deep). All labels are 2.5 or more yards inside the window. See item 1 for the
  back's depth.
- **fig-predict-2nd-10:** a correct two-high nickel against 11 personnel, with a six-man box against six blockers. The
  read-option/RPO "+1" logic in the answer is right. Labels are clean.
- **fig-predict-3rd-3:** item 5 (pistol depth). The rest is fine. The single-high nickel with $ and SS
  at 4.5–6 yards gives exactly the "6 in the box plus two fillers" picture the caption describes.
- **Charts (figs 1–5, 8, 10, 11, table 1):** no label collisions or clipping. The data figures support
  the text as written.

## Film-room selection

The examples are well chosen and accurately characterized: 2018 KC and LA (pass-leaning efficiency), 2019 BAL
(efficient running; the TEN playoff loss is the right coda), and 2023–24 DET (balance plus fourth-down
aggression). The only gap is item 12 (Rams personnel sameness). Optional: name one concrete Lions
look (heavy 12/13 personnel under center, with runs and play-action from it) so "ran and faked from the
same looks" has a picture.
