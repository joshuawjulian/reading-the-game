# 15-02 Film Study: coach / film-analyst review

Reviewer role: veteran NFL coach and film analyst. Scope: technical football accuracy, diagrams, film-room
characterisation, missing coaching nuance. I rendered `pdfs/15-02-film-study-and-charting.pdf` (newer than the .qmd)
and looked at every figure (pages 4, 8, 9, 11, 14, 17, 18, 21, 23, 24, 25).

Verdict: the protocol, the charting sheet and codebook, the game board and the scoring section are sound and well
judged. The problems are in the **strip-sack reconstruction (Figs 2 and 3)**, where the picture contradicts the
chapter's own "because" line, and in the **two Predict-the-play diagrams**, where one alignment and one blocking
description would draw an objection from any coach. Ranked most important first.

---

## A. Must fix

### A1. Strip-sack (Fig 2/3): the drawn back stands next to the sack man, so the film says "back's fault", not "coverage sack"
- **What the picture shows:** at +2.7 s and +3.3 s the RB (R) is directly beside Hall (ringed B), inside him, blocking
  nobody. `p.block("RB", pts=[(-0.3, -3.0)])` just slides him 3 yards left and parks him. Meanwhile the LT kick-slides
  only to 2.4 yd depth and stops, while Hall runs 5+ yards deep past him. Any coach freezing panel 3 would write
  *"sack because the back didn't chip/pick up the edge and the LT quit on his set"*. That is the opposite of the
  chapter's "because" line (*"Sack because of the coverage ... rush won late"*), and Pass 1's own caption ("4 rush vs 5
  + the back") invites the question of what the extra blocker did.
- **Fix (chapter code only):**
  - LT: a proper vertical set that rides Hall wide: `p.block("LT", pts=[(-1.8, -1.0), (-3.6, -1.6), (-5.2, -1.8)], speed=1.6)`,
    so the LT stays on Hall's inside hip to ~5 yd depth (he is beaten late, not standing still).
  - Hall: an arc run *past* the launch point, then back under as the QB climbs (the classic late coverage sack):
    `pts=[(-3.0, -1.6), (-6.8, -2.2), (-7.4, -0.8), (-6.4, 0.0)]` (end on the QB after he hitches to ~6 yd).
  - RB: give him real work. Either (a) he checks the A-gap / helps the centre on the DT (end at `(-0.6, -0.8)`
    *touching* T), with T's rush ending there, or (b) he chips Hall at ~0.8 s then releases to a checkdown in the
    left flat (making it 5 out and making the M's "low hole" role visible). (a) keeps the "six blockers" story.
  - With six blockers vs four rushers someone should visibly double: have C and LG both end on the DT (T), and RG/RT
    on E/OLB, so the panel reads "three stalemated, one double, edge beaten late".
- Then the "because" line holds. Also add one sentence to Pass 1: *"with two spare blockers, ask where they went: a
  free centre and a back who helped nobody are part of the sack too."*

### A2. Strip-sack: man defenders are drawn ON TOP of their receivers, hiding H and Y (label collision)
- `p.man()` in gridiron shrinks the cushion to 20% by ~1.4 s with a 0.35 s lag, so `$` sits on H, `D` sits on Y, CB on
  X (panels 2 to 4 of Fig 2 and Fig 3 panels 3 and 4). Y is not readable at +1.5 s, the very panel the caption names
  ("every receiver has a defender on his inside hip").
- **Fix:** replace `p.man(...)` for LCB/NB/DM/RCB with explicit `p.path()` trail paths that keep a constant offset of
  **~1 yd behind and ~1 yd inside** each receiver (trail technique = inside hip, underneath), e.g. compute the
  receiver's route points and offset them by `(-1.0, +1.0 * inside_sign)`. That also *teaches* trail technique, which
  the text leans on. (Gridiron note for maintainers: `man()` collapses the cushion to near zero; a `cushion=` / `hip=`
  option would help every coverage chapter.)

### A3. Strip-sack: two different defenders both labelled "B"
- Hall (`OLB`) and the right-side OLB both draw as "B"; the caption says "Derick Hall (B, ringed)". Relabel the right
  OLB `label="E"` (edge) or give Hall a distinct label (e.g. his number, "58"). The ring alone is too weak at print
  size.

### A4. Predict 2 (power, Fig 10): the answer misdescribes who blocks whom against the drawn front, and ignores the 8th man
- Drawn front (4-3 Over): backside E 5-tech, 1-tech shaded to the LG side, **3-tech outside the RG**, strong E at
  ~6-tech inside the TE, Sam stacked off the ball outside the TE at ~4 yd, SS walked down at 6 yd outside him.
- The answer says "the center, right guard, right tackle and tight end all block *down*". Against this front:
  C **blocks back** on the 1-tech (correct in spirit), but the RG has nobody to his inside: the 3-tech is *outside*
  him, so it is a **RG/RT double-team ("deuce") on the 3-tech climbing to the Will/Mike**; TE down on the 6-tech E.
- "The fullback ... kicks out the defender on the end of the line on the right": there is no defender on the line
  outside the TE in the picture. The kick-out target is the **Sam** (first defender outside the TE's down block).
  Either move Sam to a 9-tech on the line (`d=1.0, w≈+6.4`) so "end man on the line" is literally true, or reword to
  "the first defender outside the tight end".
- **The 8-man box arithmetic is missing.** Power has 7 blockers (5 OL with LT hinging, TE, FB) plus the puller wrapping
  for a linebacker; against 8 in the box the backside E is unblocked *by design* **and the walked-down SS is the
  unaccounted-for +1** (he's the free hitter on the play side). Coaches would say this is exactly why a run vs 8 is
  either checked to play-action/RPO or accepted with the back "making the safety miss", or why Z cracks the SS. The
  question literally asks "which defender will nobody block?", so the answer should name both: the backside end (by
  design) and the safety (by arithmetic). This also sharpens the "because" line ("if the SS makes the tackle at 2 yards,
  the call lost to the 8-man box").

---

## B. Should fix

### B1. Predict 1 (Fig 9): the field safety is drawn at the Cover 2 half-field landmark, which argues against him being the post player
- Ball on the left hash: the field's middle is at w≈+3; the field safety is at 13 yd, w=+12.5, i.e. the classic
  hash-to-numbers half-field spot. To become the single-high safety he must run ~9.5 yd laterally while gaining depth,
  which NFL teams do disguise, but a coach would flag that width as the strongest *two-high* tell on the screen.
- Either (preferred) move him to ~14 yd at w≈+8 (just outside the far hash, "wide" relative to the pinched safety but
  in range of the post), or keep it and say in the answer that his width is why it's only 60-65% and why his first step
  is the thing to watch.
- Add the tell the picture already contains: **nobody is apexed over the boundary slot (H)**. The pinched 9-yard
  safety is the only defender who can get to H's area, another sign he's the one coming down (buzz to the hook/curl
  over #2). It's a better confirming tell than the corners.
- Wording: "off and outside leverage is how corners line up to bail into deep thirds **with help inside**" — "help
  inside" is man-coverage language and outside-leverage off corners also occur in Cover 1. Say instead: *"off,
  outside leverage, eyes inside: the alignment of a corner who will bail to a deep third and keep everything in front
  and outside"*, and note the 7-yd cushion is the zone-ish part of the clue.
- Also worth one clause: a pinched safety at 8-9 yd is equally the **robber/rat** in Cover 1 ("rotate down into the
  hole"), which the answer covers only implicitly under "Cover 1 is possible too".

### B2. Strip-sack routes: Y's "up and into the flat" is a ~8-yd out-cut that converges on H's out
- `r.path((5,0),(8,2.5))` sends Y to 8 yd, angling outside toward H's out at 8 yd, 5 yd away on the same side. Two
  routes at one level into the same window isn't how a third-and-6 man-beater is drawn, and "flat" is a 0-5 yd route.
- Fix: give Y a real flat (`r.flat(2, 6)`-style, 2-3 yd deep) or a **stick/option at 6 off the wing**, so the left side
  is a high-low (H out at the sticks, Y flat underneath) and the right side's Z dig is the backside: that's a coherent
  third-and-6 concept vs 2-Man (outs and option routes against trail defenders).

### B3. Strip-sack: X's split and the field safety's width
- Ball on the right hash puts the field to the **left**. X is at w≈-14.6, 15 yd from the left sideline, i.e. a
  reduced split inside the numbers, with a go route. Fine if intentional, but the text doesn't use it. Prefer X on the
  numbers (w≈-18 to -19) and widen `lateral=(-24, 21)` (keep labels ≥1.5 yd inside).
- FS's deep-half landmark (19, -10) is too narrow for the field half (field half spans w≈-3 to -30). Move to
  (19, -14) so he's genuinely "above" X at +2.7 s; at present X (d≈20) is level with him, which undercuts "a safety above
  every route" in later panels.

### B4. Strip-sack: the Mike's role vs a mobile QB
- The text says M "sits in the short middle ... taking away the crossing route". True, but the coaching rule in 2-Man
  when the back blocks is usually **hug / green-dog** (add to the rush) or **spy / robot the low hole**; since FTN
  charted four rushers he didn't hug. Against Drake Maye the coach's reading is *spy/rat*: the biggest weakness of 2-Man
  is the **QB scramble** (every underneath defender's back is to the QB). Add one sentence to Pass 3 and one to the
  misconception callout: *"in a four-man rush against a mobile quarterback, rush-lane integrity (who has contain) is
  part of the coverage"*. It also makes the "QB hitched up and still didn't run" observation meaningful.

### B5. Motion response nuance (Step 0)
- "His defender went with him ... saying man" is the right textbook read, but Macdonald's Seattle is a match/bump team:
  many motion responses are **bumps / "lock-and-pass" swaps** even in zone, and match coverages travel in zone too. Add a
  clause: *"a travel is a man vote, not a verdict; a bump (defenders sliding over) says zone or match"* and point to
  02-06.
- Motion path: the TE's across-motion trail runs at d=-1.5, straight through the OL markers. Use a path at d≈-3 then
  settle into the wing at (-1.0, -5.6) (`p.motion` with intermediate points, or `p.path` with negative delay if the
  helper allows).

### B6. Pass 1 text: line tells need two coaching caveats
- **RPOs and play-action**: on RPOs the line run-blocks while the QB throws (NFL OL may be only 1 yard downfield), so
  "forward = run" will mislabel RPOs; the tell is the QB/ball, not the line. Add after "look at how far they go":
  *"on an RPO the line run-blocks even when the ball is thrown; linemen in the NFL may go only a yard past the line on
  a pass, so watch for them stopping."* Also the coaching classic: **high hats = pass, low hats = run**.
- **Duo vs zone**: "every lineman steps the same direction = zone" misfiles **duo** (no puller, double-teams driving
  straight ahead). Since DUO is in the codebook, add: *"if they drive straight ahead in double-teams with no puller and
  no lateral step, it's duo."* Also: on inside zone the **backside end** is often left for the QB's read or a
  sift/insert block, so "the defender left alone" isn't only a gap-scheme thing.

### B7. Pass 3 text: safety first-step heuristic
- "A safety who backpedals straight is playing his half or his quarter." Half-field (Cover 2) safeties pedal and
  widen; **quarters safeties usually shuffle flat-footed reading #2 and can come *forward* on run action**. Suggest:
  *"a safety who pedals and widens is playing a half; one who sits flat-footed reading the slot is playing a quarter
  (and will come downhill on a run); one who runs to the middle is becoming the single high."*

---

## C. Nice to have

- **Codebook `rot`**: B/F/L mixes direction with timing. Make it direction (B, F) plus a late flag (e.g. `B*`), or a
  separate `late` column, so "late rotation to the boundary" is codable.
- **Codebook `concept`**: add TRAP, TOSS/PIN-PULL, ZR (zone read)/QB run to the run list; designed QB runs vs
  scrambles are a common charting mistake (scrambles are dropbacks; the sheet already treats them so, say it).
- **Codebook `box`**: state the depth explicitly and that it's counted at the snap (post-motion). "About five yards"
  is fine but FTN/NGS-style definitions run a bit deeper (~7-8 yd); one clause avoids readers' box counts disagreeing
  with the participation file for definitional reasons.
- **Explosives**: "run 10+, pass 20+" is one common definition; many staffs use 12+/16+ or 15+/20+. Add "(staffs vary)".
- **Pass 2**: "a quick drop from the shotgun, a five- or seven-step drop from under center" — say shotgun drops are
  three or five steps (the gun equivalents of five and seven).
- **Full-speed look first**: most coaches watch a snap once at full speed before breaking it down (to see the
  play as a whole and the result). The short version mentions real speed; add it to Step 0 ("after the freeze, one
  look at game speed") — it also explains why Pass 3 can say "by now you know where the ball went".
- **Predict 2**: the LG is drawn ~1.45 yd deeper (exaggerated, as the caption says). Add "(in reality a few inches; he
  must still be on the line)" so readers don't think a lineman can be a yard off the ball.
- **The "because" list**: a sixth candidate coaches use constantly is **the defense's call** (a pressure or coverage
  that beat the protection/concept by design, e.g. a sim pressure that wins the count). Right now "the call" only
  means the offensive play-caller.
- **Special teams**: one line noting coaches chart special teams too (out of scope here) would be honest.

## D. Checked and fine
- Protocol order (line → QB → coverage → skill), the angle table (end zone for line/QB, All-22 for coverage/routes),
  2.5 s / 3.5 s pass-pro rules of thumb with the "judge against the drop" caveat.
- Fig 1 protocol card: clean, nothing clipped.
- Fig 4 chart sheet: columns and codes consistent with the codebook; the sk −10 / dir "–" handling is sensible.
- Fig 5 game board: drive results match the text ("first nine drives ... eight punts, ninth the strip-sack"; Seattle
  4 FGs in its first 7 drives = 12–0 after three, consistent with FACTS §1).
- Coaches/coordinators named for Super Bowl LX match FACTS-current (Macdonald, Kubiak OC, Durde DC; McDaniels NE OC).
- 2-Man description (trail technique underneath, two deep halves, outside-breaking/option routes as the beater) is
  correct.
- Predict 1 answer's "shallower, narrower safety is the rotator" heuristic and "watch the field safety's first step"
  are good coaching; the 60-65% confidence is right.
- Fig 9/10 labels and scorebugs sit inside the window; no field-edge clipping. Figs 6-8, 11 have no collisions
  (Fig 8's "down-and-distance rule"/"always pass" labels nearly touch but read fine).
- Frame-strip timing (0, 1.5, 2.7, 3.3 s) tells the story in print once A1/A2 are fixed.
