# Coach / film review: 07-01 The Pass Rush

Reviewer role: NFL coach and film analyst. I checked the qmd as of 2026-10-07 20:31 against the PDF built at 20:32,
which is newer than the qmd. I rasterized every page at 110 dpi (`_pdfbuild/07-01-pass-rush/coach/hi-*.png`) and
cropped the suspect regions at 200 dpi (`coach/z*.png`). I looked at all 14 figures.

**Overall:** this is a strong, well-built chapter. The race-and-fight framing, get-off geometry, move families, rush-plan
triangle, T-E vs slide ("the stunt chose the matchup") and the pressure-vs-sacks data are all accurate and well taught.
The T-E vs slide frame strip is right on every assignment (slide left, so the RT owns the B gap and the back owns the
right end), and its timing tells the story in print. The fixes below are mostly diagrams that show the wrong mechanism
in one spot, one internal contradiction in the measurement strip, one unrealistic defense in a drill, and nuance a
position coach would add. Items are in priority order.

---

## A. Must fix (the football is wrong or misleading)

### A1. fig-rush-lanes, right panel ("One lane lost"): the escape lane runs through the right tackle
- The red escape path `[(-7.0, 0.6), (-6.2, 2.6), (-3.6, 4.6), (0.6, 5.6)]` passes straight through the RT's set point
  `(-3.4, 4.3)`; you can see the dashed line cross his block bar. It also ends with its arrowhead on the RE's
  *original alignment*, so it looks like the QB runs at the end.
- **The mechanism is wrong.** When an end rushes too far upfield, the tackle **rides him** (runs him past the QB). The
  hole opens because the tackle and the end *both* leave, and the QB climbs and escapes underneath them.
- **Fix:** in the lost panel only, send RT with the end: `to(p, "RT", (-6.6, 5.4), via=[(-3.4, 4.6)])`, and draw a
  `pushed()` or short dark-blue line so the reader sees the tackle riding him. Route the escape outside the
  3-technique's lane and under the RT/RE pair, finishing past the LOS but away from the end's start:
  `[(-7.0, 0.6), (-5.4, 2.4), (-2.6, 3.9), (1.4, 4.4)]`.
- **Label collision:** the "escape lane" label at `(-3.2, 7.4)` sits on top of the RE's rush path, which runs at w≈6.5–6.6
  through that depth. Move it inside, next to the red path, at about `(-4.4, 1.6)` (clear of the 3's lane, which ends
  near w=1.0 at d=-5). Or widen to `lateral=(-11.6, 11.6)` and put it at `(-3.0, 9.6)`.
- Add one clause to the caption: "...the right tackle rides him past, and the space they both left becomes an escape
  lane." For B8 below, also add: "a right-handed QB escapes to his right most readily, which is why this side's contain
  matters most."

### A2. fig-ttp-strip / fig-ttp-chart: the left end also "wins" by the chapter's own rule
- By the chapter's definition (rusher deeper than his blocker, which is what `WIN_T` computes), the LE wins too. With
  the scripted waypoints, LE passes LT's depth at about **2.1 s** and is about 0.6 yd deeper at 2.4 s, all inside the
  2.5-second window. Frame 4 shows it: the left E is drawn below (behind) the LT.
- The chart caption says "the other three never beat theirs", so this is a visible contradiction in the one figure
  meant to teach the definition.
- **Fix:** keep the LE in front of the LT, for example
  `timed(p, "LE", [(0.3, 1.0, -5.4), (0.75, 0.0, -5.8), (1.2, -1.3, -6.0), (1.8, -2.4, -5.6), (2.4, -3.0, -5.1), (2.8, -3.2, -4.8)], "rush")`.
  With LT finishing at `(-3.9, -3.5)` that leaves the end on the tackle's outside half, stalemated. The 1- and 3-technique
  are fine.

### A3. fig-stunts, interior twist: caption and text say "across the center's face", but the drawing doesn't show that
- In the drawing the 3-technique (w=2.35) crashes to `(-0.4, 0.8)`, which is the **right A gap** through the RG's inside
  shoulder. He never crosses the center. The 1-technique (shaded to the left of the center) then loops over the top of
  the center into the right B gap.
- That is a legitimate and common game: the 3 picks the guard and center, and the nose wraps to the B gap. Describe it
  that way.
- **Fix the caption and the body text** to: "the 3-technique crashes inside, through the right guard's inside shoulder into
  the A gap, picking the guard and center; the 1-technique wraps over the top behind him into the B gap he left."
  Alternatively, redraw it so the 3 really does cross the center to the far A gap (end near `(-0.4, -0.9)`) with the 1
  looping to the right B gap. Use one version or the other, not a mix of both.

### A4. fig-predict-stunt (drill 1): two linebackers stacked in the box against empty 3x2
- Against empty, no defense keeps the Mike and Will at 4.6 yards inside the tackles. The slot on the two-receiver side
  (A at w=-9.5) has nobody within 7 yards, and the #3 receiver on the trips side (Y at 6.5) is uncovered.
- **Real check:** the linebackers walk out to apex the slots. Move WILL to `(5.0, -6.0)`, between the LT and A, and
  MIKE to `(4.8, 4.6)`, inside Y. Keep NB on H and the corners on X and Z. That leaves the four linemen alone in the box,
  which is normal against empty, and it strengthens the drill's point that only the five linemen can block.
- **Answer 1 text:** "with nobody in the backfield there is no back to absorb a mistake; every blocker is already
  committed to a rusher or a gap" is wrong. Five blockers against four rushers means one spare blocker. Against this
  front (1-technique shaded left, LE outside the LT) the spare is the **LG**, who is uncovered.
- **Rewrite:** "five blockers against four rushers gives the offense one spare man, but against this front the spare is
  the left guard, on the far side. Aim the stunt at the right guard and right tackle, away from him, and those two must
  pass it off alone." This makes the answer better, because it explains *why the right side*.

### A5. "A tackle facing the same rusher sixty times in a game"
- An offense runs about 60–70 snaps and about 35–40 dropbacks, and edge rushers rotate. A tackle sees a given rusher on
  roughly **25–40 pass snaps**. **Fix:** "thirty-odd times".

### A6. fig-mush: the ends are drawn having beaten their tackles
- The ends' paths go outside the RT/LT `(-3.0, ±4.0)` to `(-4.2, ±5.7)` and then turn *in behind* the tackles to
  `(-5.6, ±2.8)`. That is a corner turned, which is a speed-rush win, not a mush.
- In a mush or cage rush, the end stays on the tackle's **outside half**, in front of him, and walks him back to the QB's
  depth. The cage is made of driven-back blockers with rushers on their outside shoulders.
- **Fix:**
  - Push the tackles back: `pushed(fld, p, (-1.4, ±3.6), (-4.6, ±3.4))`.
  - End the ends at `(-4.4, ±4.4)`, still outside and slightly in front of the pushed tackle.
  - Drive the guards back too, for example RG/LG to `(-3.0, ±1.7)` with `pushed()`, and the DTs to `(-2.0, ...)`. Right
    now the DTs end at d=-0.9 with the guards in front of them, which shows no push at all.
  - Redraw the cage polygon through those points.
- **The spy:** the M arrow runs downhill from 4.8 to 2.6 toward the LOS. That reads as a delayed blitz or green dog, not
  a spy. Draw a short **lateral** two-headed arrow at constant depth, for example from `(5.0, -1.5)` to `(5.0, 1.5)`,
  labelled "mirrors the QB".

### A7. fig-rush-plan, right panel: the tackle's punch is drawn in the rusher's colour
- `arm(fld, p, (-1.75, 4.65), (-1.15, 5.15))` is the **tackle's** reaching punch, but `arm()` draws it in `ARM`
  (defense dark orange, with a hand dot). The diagram key says that colour is "the rusher's arm", so it reads as the
  rusher's hand.
- "his punch reaches" floats more than 2 yards away with no leader line.
- **Fix:** draw the stroke in `style.OFFENSE_DARK`, which needs a colour parameter in the chapter's `arm()`. Replace
  `say(...)` with `point_to(fld, p, (-5.0, 6.4), (-1.45, 4.9), "his punch\nreaches", color=style.OFFENSE_DARK)`.

---

## B. Precision and nuance a position coach would insist on

**B1. Silent count.** The phrase "a silent count that gives nothing away" overstates it. A silent count takes away the
hard count, but it often makes the snap *more* predictable: the center looks back, the guard taps him, and the snap
comes on a set beat. Good rushers time it. Suggested wording: "a silent count, which takes away the hard count but can
leave the snap on a rhythm a rusher learns to time."

**B2. Get-off numbers.** "The fastest are around a third of a second": the source's 0.33 s is a **single snap** by
Parsons, not a typical elite average.
- The physics: a lineman whose body starts about a yard behind the ball needs roughly 0.5 s to cross it from a standstill
  at NFL acceleration. 0.33 s is a best-ever rep.
- The chapter's own simulation gives 0.5–0.8 s, which is closer to typical.
- Suggested wording: "the quickest single snaps are around a third of a second; most edge rushers average well over
  half a second." Have factcheck verify the average if you quote one.

**B3. Long-arm aiming point.** "Inside arm into the blocker's outside shoulder area": coaches teach the strike to the
**outside half of the chest, the near breastplate**. On the shoulder, the blocker can turn and shed the arm. Change
"shoulder area" to "the outside half of his chest".

**B4. Missing hand moves.**
- The text uses "a **club** or a swim" for interior rushers without defining club.
- The two most common power hand moves are missing: the **club** (a forearm or open-hand blow to the blocker's
  shoulder or elbow to knock his punch aside, usually set up for a rip or swim) and the **push-pull** (also called the
  snatch or jerk: grab the blocker, pull him forward past you as he leans, and go).
- Push-pull is the interior rusher's signature move, and Donald's game was full of it. Add two sentences, with an
  inline gloss and no glossary entries (they are not owned terms), in "Moves are counters to hands" or "Inside rushers".
- Reggie White's "hump" then reads as a club-and-lift variant.

**B5. Two coaching principles the chapter never names.**
- **Rush half a man:** attack one half of the blocker, never his whole chest. That is why every move starts on a
  shoulder.
- **The landmark:** edge rushers aim at the QB's launch point, not at the blocker. That point is about 7–8 yards deep
  from shotgun (5 yards plus a two-step drop) and 7–9 under center.
- Both fit naturally in "The arc and the corner". The diagrams already put Q at about -7, so they are consistent.

**B6. Stunt dialects and technique.**
- **Dialects:** in many rooms "stunt" means pre-snap or at-snap line movement (slants and angles) used against the run
  too, while "game" or "twist" means a pass-rush exchange. The current sentence says they all mean the same thing in
  most rooms; soften it to "overlap, and many staffs use 'stunt' for run-down line movement and 'game' for pass-rush
  twists".
- **Role names:** the penetrator is also called the crasher, driver or picker, and the looper the wrapper. Code names
  vary (Tex, Ex/Ed, Tom, Pirate).
- **Technique, missing:** the penetrator's aiming point is the near hip or inside number of the *far* blocker (the OT on
  a T-E). He has to collide with both blockers, a legal **pick**, so they cannot switch cleanly. If he just runs around
  the tackle, the stunt fails.
- **T-E paragraph wording:** "crashes outward into the offensive tackle" should become "drives into the offensive
  tackle's inside half to pick him, then takes over contain."

**B7. End vs edge dialect.** The chapter calls every edge rusher an "end" and labels him E. Three of the chapter's six
named rushers were 3-4 outside linebackers: LT, Watt, and Parsons (in Dallas). Add one sentence in "How to read the
diagrams" or "The arc": "**edge rusher** covers both: a 4-3 defensive end with his hand down, or a 3-4 outside linebacker
standing up; E in the diagrams means either."

**B8. Contain priority.** A right-handed QB escapes to his right (the offense's right) most readily, because he can throw
on the run that way. Defenses therefore guard that contain hardest. The figure already "loses" the RE's lane, so this is
a one-sentence add to the text and the caption.

**B9. Super Bowl film room: "pressure with four" vs simulated pressure.**
- "Got to the quarterback without blitzing" is true by rusher count. But Macdonald's Seattle defense (2025) is known for
  four-man **simulated pressures**: a lineman drops, and a linebacker or DB rushes in his place. That is a different
  mechanism from four linemen winning one-on-one, and it is exactly 07-03's subject.
- Add one sentence: "Seattle's four were often not its four linemen; [Zone Blitzes and Simulated Pressure](07-03-zone-blitz-and-simulated-pressure.qmd)
  shows how." If you can, compute the split from FTN's `n_blitzers` (a four-man rush with `n_blitzers > 0` is a sim).
- "Most of the damaging pressures in both games came early enough that no receiver had finished his route" is
  unsourced, and the chapter has no data for it (FTN has no pressure time). Soften it to an instruction ("time the
  pressures yourself and see how many arrive before the routes finish"), or drop it.

**B10. Garrett film room is generic.**
- "Pick any Browns passing down from 2025" falls short of the contract's "ideally the game and situation". Name the
  record sack: Week 18 against Cincinnati, and (verify) the quarterback and the quarter.
- Add his alignment. He played a lot of wide-9 in Jim Schwartz's attacking front (Browns DC 2023–2025; label the
  seasons) and moved sides.
- In the data section, "the sacks just arrived in one year rather than the other" is defensible statistically (defense
  pressure-to-sack carry-over is +0.00). Still, add context: a wide, upfield front produces many hurries that arrive at
  the throw, and game script (the 2024 Browns trailed often) shapes which dropbacks a defense faces. One sentence is
  enough. Keep the conclusion.

**B11. "Back to the replay": the PRWR claim.** A speed-to-power that walks the tackle back without ever shedding him is
the kind of rep a "did he beat his block" measure can miss. Change "would very likely count it as a win" to "might well
count it as a win, though a bull rush that never sheds is the kind of rep a beat-the-block measure can miss". Factcheck:
confirm how ESPN's PRWR treats double teams. If doubles get special credit, say so in the limits paragraph, because that
is precisely the inside rusher's problem.

**B12. Predict 3 (the counter).**
- The answer says the right guard can slide out to help. That is true only if he is **uncovered**; with a 3-technique on
  him he cannot. Add "if nobody is lined up on him".
- In fig-predict-counter the RG is still frozen in his stance at 0.8 s after the snap. Set him: `to(p, "RG", (-1.5, 1.8))`.

**B13. Predict 2 (running QB).**
- A DC worried about this quarterback would often *tighten* the end to a 5 or 6 rather than leave him in a wide-9. Add:
  "expect him to tighten his alignment, or, if he stays wide, to rush through the tackle's outside half rather than
  around him."
- The back on the QB's left is a likely chipper or check-release on the LE side. That helps explain why the right
  (wide-9) side is the pressure point.

**B14. fig-rush-moves, long arm panel.** The arm is drawn at the moment of contact (E at d=-0.8), but the tackle's ghost
is already driven to d=-3.7, so two moments are mixed in one panel. Either draw a rusher ghost at about `(-2.9, 4.2)`
with the arm from it to the tackle ghost, or shorten the push to about `(-2.4, 3.6)`.

**B15. fig-stunts depth cheat (optional).** The DL are drawn at d=2.6, which is 2.6 yards off the ball. The caption
discloses it, but the pilots kept real depth. Playbooks draw this with DL at real depth (d≈1.0) and the looper's path as
a tight hook just behind the penetrator's start. That would be truer and still readable if you reduce `DL_DEEP` to about
0.6 and keep the loops wide.

**B16. fig-pressure-vs-sacks label collision.** The arrowhead overprints the "5" of "Browns 2025 / 53 sacks". Use
`xytext=(10, 8)` with `va="bottom"` for that label, or raise `shrinkB` to about 9.

**B17. Watch for it, before the snap.** Add one bullet: "**Which way is the protection set?** Find the back. In a
half-slide he is usually on the man side, and a tight end or back aligned near the best rusher means a chip. Stunts and
the best rusher's moves are aimed away from the help." This ties the checklist back to 04-02 and to fig-te-vs-slide.

---

## C. Checked and correct (no change)
- **Get-off geometry (fig-get-off):** realistic arc, set point and labels, all at least 1.5 yd inside the window.
- **Move families and what each beats:** speed beats a slow or short set, bull beats a high, light or deep set, swim and
  spin beat an overset, rip finishes the corner. The cross-chop and ghost descriptions are accurate.
- **Spin mechanics:** plant the outside foot, back to the blocker. The risk is described correctly.
- **T-E vs slide-left frame strip:** every assignment is right (C/LG/LT slide, RT owns the B gap, RB owns the right end).
  The stunt picks up the B-gap looper and lands a DT on the back. The note that the same T-E into the slide side "dies" is
  correct.
- **Rush lanes, left panel:** the contain line at QB depth and the interior push lanes are right.
- **Data framing:** pressure carries over better than sacks, defense conversion does not carry over, QB conversion does.
  The source break is handled correctly.
- **History:** Deacon Jones's head slap (banned 1977), the 1978 blocking change, LT's 1986 MVP, White's 198 sacks and
  Smith's 200, Freeney (HOF 2024), Donald (13th pick in 2014, DPOY 2017/18/20, 20.5 sacks in 2018), the Watt/Garrett
  records, and the Parsons trade (Aug 28, 2025) all match FACTS and the cited sources.
- **Drill 2 formation:** legal (7 on the line, Y attached, Z off). The wide-9 at w=7.1 is 2.3 yd outside the TE,
  consistent with 05-01's definition.
- **Animation count:** one video plus one static strip, well within the limit. Frame captions tell the story in print.
