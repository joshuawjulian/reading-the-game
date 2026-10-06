# Coach / film review: 04-02 Pass Protection

Reviewed 2026-10-06 against the built PDF (`pdfs/04-02-pass-protection.pdf`, newer than the qmd). I looked at
all 18 figures at 110 dpi (`_pdfbuild/04-02-pass-protection/coach/hi*.png`). I did not edit the chapter.

**Verdict.** The chapter is technically sound and well pitched. Counting, inside-out, the cup, the slide/man/half-slide
assignments, check-release, Mike ID as a reference point, hot vs sight, and switch vs stay are all explained the way
an NFL line coach would teach them. The slide and half-slide gap ownership in Figs 2–3 is correct gap by gap. Two
must-fix errors remain: Predict-the-play 3 hands the star rusher to the tight end and back instead of the tackle,
and Fig 12's caption says something its own frames contradict. After those come diagram fixes (one convention
break, overlaps, unrealistic spacing) and some coaching nuance a position coach would add.

## Must fix

1. **Predict 3 answer: the star rusher goes to the tackle, and the help is extra.** The answer says "expect the
   line to slide left, so that the interior and left side are handled by linemen, while the tight end and back deal
   with 99." Read as written, it gives 99 to a TE and an RB. No staff does that against the defense's best rusher.
   The correct answer is a **half-slide left**: C, LG and LT slide left; on the man side the **RG takes the
   3-technique and the RT takes 99 man to man**; Y chips 99 on his release and the back (offset right) checks
   his linebacker, then chips 99 and releases. If the offense wants a full-time double, it is RT + Y on 99 (a
   seven-man look). Rewrite the first paragraph to say this, and add one line: "you never leave a star alone
   with a back; help means *in addition to* the tackle." The same idea belongs in the slide section, where
   "Good offenses slide *toward* the biggest threat in the middle and send help to the end they left behind" is
   muddled. Better: "Offenses either slide toward the most dangerous inside rusher or the overload, or slide
   away from a star edge rusher so their tackle is on him man to man, and then send a chip."

2. **Fig 12 (pocket hull) caption contradicts its frames.** The caption says "By two seconds the ends have been
   pushed past the quarterback's depth." In frame 3 (+2 s) both Es are at about 4.6 yd deep, level with the
   tackles, and the QB is at 7.4. They only reach his depth at about 3 s. Fix the caption and the frame-3 note to
   "by two seconds the ends are being run up the arc, level with the tackles", or move the E waypoints at 2.0 s to
   about (-6.8, ±4.6).
   - **Coaching error in the same simulation:** the line has five blockers against a four-man rush, yet the
     uncovered **C drifts right** (w 0.1 → 0.5) while the 1-technique bull-rushes the LG from -1.3 to -4.7 yd.
     The spare man has to help, which is the chapter's own "looks for work" rule. Fix: script the C to check
     the middle, then post onto the 1-technique's near hip, e.g. `C: (1.0,-1.8,-0.4) (2.0,-2.5,-0.8) (3.0,-3.3,-0.7)`.
     Keep the shrinking pocket by having the push stall later, or by having the RE beat the RT late. If you
     keep the bull rush, say in the caption that the C should have helped. As drawn it teaches a bust as
     normal. Also note that the QB "steps up" into the side where the LG is being driven back, which works
     against the text's "step-up only works if the interior held." Have him climb toward the right B gap
     (w ≈ +0.8) instead.

## Diagram fixes (by figure)

- **Fig 1 (cup).** The "3-technique: about 9 yd straight up the middle" label sits at w = -0.6, directly above the
  **1**, not the 3. Use `point_to` aimed at the 3 (w 2.35), or move the label to w ≈ 2.0 and narrow the edge label so
  the two don't touch.
- **Fig 4 (Mike bust).** The red dotted C→52 line runs straight through the **1** marker. Bend it (route via
  (0.5, -1.6)) or move 52 to w = -3.4 and start the line from the C's left shoulder.
- **Fig 6 (chip).** Y is a "wing" 3.2 yd outside the LT (w -6.4) with the end *inside* him (w -5.3). That is
  unrealistically wide for a wing, and it shows the uncommon outside-in chip. Use the standard look: **Y as a wing
  at (-1.2, -4.8)** (about 1.5 yd outside and 1 yd behind the LT), **LE in a wide 9 at (1.0, -6.3)**. Y chips him
  inside-out as the end starts his arc, then releases up the seam or flat. The back's chip on the right is correct as drawn.
- **Fig 7 (max protect).** The **offensive-line labels were blanked** (`q.moved(label="")`). That breaks the chapter's
  "LT, LG, C, RG, RT" convention and leaves five anonymous dots. Restore them. The caption also says "seven-step drop"
  but `p.dropback(6.4)` from under center ends about 7.4 yd deep, which is a five-step depth. Use `dropback(8.5)`
  (about 9.5 yd) or say "five-step". Optional realism: X post plus Z deep crosser at about 18 yd is the classic
  max-protect shot (Yankee). Raise Z's break from 12 to about 16–18 yd and name it, or call it a "post–dig" and
  leave it.
- **Fig 8 (hot throw).** The RE's rush arrow ends on top of the **R** marker: R is at w 5.0, only 1.8 yd outside
  the RT, which is a wing rather than a 3x2 slot. Re-space the empty 3x2 (`empty_3x2`) as **R (-1.4, 6.5), Y
  (-1.4, 10.0), Z (-0.7, 14.0)** and move the Will to about w 6.3. That also fixes Fig 16, which reuses the helper.
  Optional: the OL labels are crowded by block bars, so shorten the LG/RG block vectors.
- **Fig 9 (tackle sets), jump-set panel.** The RT finishes at d = +0.1, *past* the line of scrimmage, and the E's
  rush arrow is hidden under the block bar, so the panel shows no rusher action. Use RT end (-0.3, 4.5) and
  E path via (0.6, 5.9) to (0.2, 5.1) so a short orange arrow shows the meeting point at the line.
- **Figs 10 and 11 (T-E stunt).** In frame 4 (+1.4 s) and the "switch" panel the **E and 3 squares overlap**, and the
  end of the story ("RG has E, RT has 3") is hard to read in print. Spread the finish: DT final (-1.7, 4.0), RT final
  (-2.8, 4.1), RE final (-1.1, 2.0), RG final (-2.3, 1.9). The stay panel also reads better with one more 0.2 s.
- **Fig 13.** The dashed "frames shown above" lines at 1.0 and 3.0 s sit on gridlines and can't be seen. Draw them
  in `style.SERIES[6]` or another distinct ink.
- **Fig 16 (Predict 1).** The DTs are labelled **T**, but the chapter's legend says defensive tackles are labelled by
  technique. Both are on the guards' outside shoulders (w ±2.4), so label them **3**. The W and M rings crowd the
  T/3 markers; nudge the LBs to w ±0.75 at d 1.4. R spacing as in Fig 8.
- **Fig 5 (RB pickup), minor.** The back meets the Will about 2.5 yd behind the line, while the text says "meeting
  him at the line of scrimmage." Either move the 1.0 s contact to about (-1.8, -2.6), or say "in the hole, a yard
  or two behind the line." Both are realistic.

## Accuracy and nuance a coach would insist on

1. **Predict 1 answer misses the coverage count.** With seven rushers, 11 - 7 = 4 defenders are left to cover five
   receivers, so someone is uncovered before the snap. As drawn, nobody is over R. This is the first thing a QB
   coach asks ("count the coverage, not just the rush"). Add it. Also say *which* end the line takes: set the
   protection toward the nickel or overload side (LT on LE). The free rushers are then the NB and the RE, the QB
   is hot to **both** sides (H on the left, R/Y on the right), and the hot answer depends on who actually comes.
2. **Pick where the free rusher comes from.** Inside-out decides *how many*. Coaches also decide *where*: they
   would rather leave the free man where the QB can see him (front side) than on his blind side. One sentence in
   "Protection is counting" or the hot-route section.
3. **Back: dual reads and the order of jobs.** In many half-slide and BOB rules the back has two linebackers to
   check, inside-out ("Mike to Will", a "dual read"), not one. When a chip is tagged, the order is **check,
   then chip, then release** ("block-chip-release"): blitz first, chip only an outside rush (if the end
   goes inside, don't chase him), then the route. Add to the check-release and chip sections, and to the chip
   glossary.
4. **The language of the count.** Many staffs number the box from the Mike ("0, 1, 2 ...") and name slide
   directions with code words ("Lucy/Ringo", "Lion/Ram"). The QB usually owns the final Mike point and the center
   the line call. One sentence in the Mike section, plus a mention in the existing "50s/60s/90s" dialect
   parenthetical, would cover the dialect question readers will meet on film or podcasts.
5. **Empty protection.** "They usually block man-to-man on the four defensive linemen plus the Mike": many NFL
   teams run empty as a five-man slide or half-slide with a "QB hot" rule, so change to "often". The same applies
   to the table row.
6. **Punch timing nuance.** Modern NFL tackles often use **delayed or independent hands** (a "catch" and a late punch,
   one hand at a time) against rushers who swipe and chop. As written, "punch too early and he swats the hands"
   implies one textbook two-hand punch. One sentence fixes it.
7. **Watch-for-it bullet:** "a back offset to one side usually means that side's edge rusher is getting a chip".
   An offset back more often shows his **check side** (usually away from the slide) or a run tell. Change to "often
   means that side is his to check, and maybe chip."
8. **Stunt paragraph wording:** "defenses that love to stunt see a lot of slide protection" puts the choice on the
   wrong side. Use "offenses facing stunt-heavy fronts lean on slide." Consider one coaching cue for the switch:
   the tackle **squeezes the penetrator** (flattens down to him) and the guard pushes him off and turns his eyes
   to the looper ("hip to hip"). Note that E-T games attack the guard–center seam, where slide is strongest.
9. **History link:** the "blind side" link goes to 11-02 (the 1978 rules chapter). It belongs with the
   Taylor/left-tackle story. Point it to the history chapter on Taylor/LT if one exists, or unlink it.
10. **Film room, Bengals at Buffalo (flag for the fact-checker):** "Jackson Carman, making his first NFL start at
    left tackle." Carman started several games at **right guard** as a 2021 rookie. Make sure the wording reads as
    "his first start at left tackle", not his first NFL start. The fact-check log records "Carman's first NFL start",
    which I believe is wrong. PLAUSIBLE, verify.

## Checked and correct (no change)

- Slide-right gap ownership (LT: left B, LG: left A, C: right A, RG: right B, RT: right C), the back on the end left behind,
  and LB blitzes landing in the C's or LT's gap: correct. BOB (4 DL + Mike, back on the Will): correct.
- Half-slide right with the back to the left (man side), the C helping when his gap is empty, and check-release: correct,
  and consistent with the "60" in 01-04 (`protect_60`).
- Mike-ID bust mechanics (five rushers against six blockers, still a free man): correct and well chosen.
- Hot vs sight adjust and the Madden distinction: correct. The Cover-1 pressure in Fig 8 adds up to 11, and the
  NB's roughly 2 s path to the QB is realistic.
- Max protect (8 v 5, 2 receivers v 6 in coverage) arithmetic, and play-action pairing.
- Kick slide, vertical / 45 / jump trade-offs, inside counter vs vertical set, anchor vs bull rush, holding per Rule 12-1-2/3:
  correct.
- Metrics: the pressure, hit and sack definitions, the FTN-only window, the TTT/sack-rate scatter, and the Bears arrow are all
  sound and well read.
- Film rooms: Patriots/Brady Mike calls (spec), the Bengals rebuild into the AFC Championship Game (Jones's third-down sack
  on the last possession), and Stoutland/Eagles are well chosen and accurately characterized, apart from the Carman wording.
- Animation count (2 animations + 1 strip) is within limits, and the strips tell the story in print apart from the
  Fig 10 final-frame overlap above.
