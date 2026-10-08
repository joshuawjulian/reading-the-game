# 12-04 Reid / Chiefs: coach and film-analyst review

Reviewed: `chapters/12-case-studies/12-04-reid-chiefs.qmd` (1,540 lines) and `pdfs/12-04-reid-chiefs.pdf` (24 pp.,
rasterized at 110 and 200 dpi). I looked at all 13 figures.

**Verdict:** the history, the data story and the structure are strong, and the Reid → Childress → Nagy → Mahomes
arc is told correctly. Four diagrams have football errors a coach would catch on sight. They are listed first and
ranked by severity: the RPO conflict defender, the scramble-drill cause and effect, the Cover 0 protection, and Buckner's
timing in Wasp. After those come smaller diagram fixes, then text accuracy and missing nuance.

---

## A. Must fix (football is wrong or misleading)

### A1. Fig 2 `fig-kc-rpo`: the read defender is on the wrong side of the receiver
- `APEX` ($) is at `w=11.5`, **outside** 87 (`w=8.5`) and between 87 and Z. The caption says he is "in the apex
  between the box and the slot" with "87 running a 5-yard hitch outside him". The drawing shows the opposite. As
  drawn, the $ fills by running straight across 87's hitch, so the throw goes into the defender, not into the
  space he left.
- **Fix:** move `APEX` to about `(4.5, 5.8)`, halfway between the RT (3.2) and 87 (8.5), and keep 87 at 8.5 on a
  5–6-yard hitch or stick. Re-aim the fill arrow from there to about `(2.0, 3.8)`. The label "If the apex defender
  comes down…" can stay where it is.
- **Box count:** `WILL` at `(4.5, -6.0)` is only 2.8 yards outside the LT and 4.5 deep. Most coaches would count
  him as the backside cutback player in the run fit, which makes the box six against five. You can either (a) widen
  him to an obvious apex on H, about `(5.0, -6.8)`, and say "walked out over the slot" in the caption, or (b) keep him
  in the box and teach the real RPO lesson: "six in the box against five blockers, so the offense reads the man who
  makes it six." Option (b) is the better football, because it explains why you read anyone at all. If it's
  five-for-five, the reader will ask why the QB is reading.

### A2. Fig 4 `fig-kc-scramble`: the wrong defender explains why 87 is open
- The caption and the panel 4 note say "the hole player (M) came up for the QB: 87 is alone". But 87's man is the
  **SS** (`p.path("SS", …)` inside leverage), and 87 catches the ball near the **sideline** at `w≈16`. The Mike's
  hole is the middle of the field. When the hole player leaves, the **crosser (H)** in the middle comes open, not a
  tight end on the boundary.
- **Fix, option 1:** keep the throw to 87 and change the reason. "His man, the SS, was sitting on the in-cut with
  inside leverage. When 87 broke back outside toward the scramble, the SS had to turn and chase, and the throw beats
  him to the sideline." Move the panel-4 note to say that. Keep a separate short note on M ("comes up for the QB:
  the middle opens for H").
- **Fix, option 2:** throw to H on the crosser into the vacated hole. That teaches the hole-player lesson the
  caption wants.
- At 5.45 s the SS is about 3 yards behind 87. "Alone" overstates it, so say "a step clear."

### A3. Fig 9 `fig-kc-zero`: the protection drawn can't happen the way the caption says
- The caption says "six blockers for six rushers on paper, but the running back is carrying out his fake". In the
  drawing the RB never has a blocking assignment: he fakes left and releases right, and Y releases too. Five OL are
  shown against six rushers. And the five OL ignore the most dangerous down lineman: `LG→SAF` (a safety 4 yards
  deep) and `C→LB` turn to second-level players, while 95, aligned in the A gap right in front of them, walks through.
  No NFL line protects like that.
- **Fix:** draw a believable 6-man plan. One way is a slide right with the C and LG working right and the RB
  responsible for the left A/B gap. Then show the RB carrying out the play-action fake to the wrong side or too late,
  so his man (95) comes free. That matches the caption's "six on paper" and is the usual way play-action loses a
  free rusher against zero. Alternatively, mug `LB` and `SAF` on the line (Spagnuolo mugs; 07-02 teaches the
  double A-gap mug) so it's obvious why the C and LG turned to them.
- Do not claim the 49ers' actual protection call unless a film source states it. Keep "illustrative".
- `DB3` is labelled **"D"**, a letter the "Reading the diagrams" legend never defines. Use "S" or "LB" and make sure
  the two "S" labels are both meant to be safeties.
- Small item: on third-and-4 at the 9, H's and Y's verticals stop at or just short of the goal line. Extend them
  1–3 yards into the end zone so they read as end-zone routes.

### A4. Fig 5 `fig-kc-wasp`: Buckner arrives two seconds early
- In the +1.8 s panel, 99 is already through the RG, at about d = −8, roughly 3 yards from Mahomes (d ≈ −11). He then
  "chases" 3 yards behind for two more seconds and hits at 3.78 s. A clean DT that close at 1.8 s is a sack, and it
  contradicts the text ("the coverage held for three seconds"; "seven blockers' worth of attention for the first
  second and a half").
- **Fix:** keep `BUCK` engaged with the RG until about 2.6–2.8 s, for example
  `p.rush("BUCK", pts=[(-1.6, 0.2)], speed=1.0)` and then a `p.path(... delay=...)` burst to `(-12.2, -3.4)`. He should
  first appear past the guard in the 3.8 s panel. The other three rushers should look engaged too: they currently
  stop at −1.8 to −2.6 with the OL at −1.6, which reads fine.

---

## B. Wasp: accuracy and teaching gaps (Fig 5 and its text)

1. **"Jet" and "2-3" are never explained.** "Take the call one word at a time" covers only "Chip" and "Wasp", and the
   West Coast section labels the parts as "protection, a word for the back, a route name". Add one short paragraph
   saying that "2-3 Jet" is the protection part of the call, with a source, or say plainly that its exact meaning is
   Kansas City's own and not public. Some accounts give a longer call. Check that the quoted call is complete before
   calling it "the full call".
2. **The alignment is presented as "charted facts" but isn't charted.** The caption says "Hill (10) and Sammy Watkins
   (14) to the same side as Kelce". The participation file gives personnel and formation, not alignment, and
   `[^waspdata]` doesn't support who stood where. Either cite an All-22 breakdown (Nguyen, Keysor, or the NFL Films
   mic'd-up cut) for the trips-left / Kelce in-line look, or move that sentence into the "our illustration" part of
   the caption.
3. **Hill's stem doesn't look like a crosser.** The route goes `(13, -8.8) → (21, -4.0)`: 4.8 yards inside over 8
   yards, which is a skinny post. The text says "a deep crosser's stem toward the middle at 15 to 20 yards". To sell
   the safety, have him reach roughly the hash or the middle of the field (`w ≈ -1…0`) by 18–20 yards, then break
   to `(44.5, -17.6)`. Ward taking the crosser only makes sense if the crosser really threatens the middle.
4. **The Cover 3 corner is drawn too shallow for "the 49ers did almost nothing wrong."** At 3.8 s `LCB` is at about
   16 yards, squatting on Watkins's comeback, while Hill is at about 29 yards heading into his deep third. A
   textbook Cover 3 corner who stays 13 yards under a vertical in his own third has busted the coverage. Either:
   - **Explain it as pattern-match Cover 3**, which is the better lesson: the corner has #1; when #1 stops at 15
     he drives on it, trusting the post safety to own #2 crossing into the middle. Hill's break back outside lands
     exactly in the seam between those two rules. That is *why* Wasp beats a well-played Cover 3, and it's the
     coaching point the section is missing.
   - **Or** deepen `LCB` to 20–24 yards at 3.8 s and let Hill beat him on the angle.

   Either way, soften "almost nothing wrong" to "played their rules".
5. **Panel title "+7.0 s · the stinger":** a reader won't get the wasp pun, and "stinger" is also a football injury
   word. Use "+7.0 s · the catch".
6. **Throw timing:** the text says "the coverage held for three seconds… the play wasn't done yet". The ball came out
   at 3.78 s. That's fine, but say "almost four seconds", since this chapter's own threshold is four.
7. **The text says "Cover 3, with two linebackers and a nickel inside the 49ers' five defensive backs".** That's
   garbled. Rewrite as: "nickel personnel (four linemen, two linebackers, five DBs), four rushers, Cover 3 behind
   them."
8. **Label collisions:**
   - +1.8 s panel: "E", "81" and "26" overprint at the right end of the line, and "SS" touches the 87 marker.
     Offset the RB's chip point or move the note. The cleanest fix is to drop 81's block to `(-1.2, 0.0)`, so Bell
     sets straight back while the RB chips wider.
   - +3.8 s panel: "15" sits about 1.5 yards above the bottom frame. Widen `WIN[2]` to `(-16.5, 31.0)`.

## C. Option route (Fig 7 `fig-kc-option`)

- **The route runs through a defender.** In both panels the RDE (`w=5.4`, on the line) is head-up on 87 (`w=5.4`,
  off the ball), and 87's route arrow passes straight through the "E" box. Either move 87 to `w≈6.5` (a true wing
  outside the end) or set the DE as a 5-tech at `w≈3.8`. That fixes the overlap and stops the reader asking how Kelce
  releases through a rusher.
- **Clipping:** in the zone panel `WILL` starts at `w=-3.0` against `lateral=(-3.5, 19.5)`, so the "W" box is cut
  by the frame. Use `lateral=(-5.5, 19.5)` or move the Will.
- **"M plays him from inside" floats** at 12.5 yards, far from M (4.5 yards). Use `pointer(...)` to M, or put the
  label at about `(8.0, 1.0)`.
- **The "curl" zone label** is crossed by H's vertical. Nudge the label to about `w=14`.
- **Missing nuance:**
  - The option route is itself West Coast. Walsh's and Holmgren's "Y-option" is the ancestor, the Patriots made it
    famous, and Kelce inherited it. One sentence here ties the Kelce era back to the chapter's thesis (West Coast
    bones) instead of calling it just "the oldest idea in the passing game."
  - Name the real menu. Against man: in, out, or a whip/return off leverage. Against zone: sit, *or keep running
    away from the zone defender's leverage into open grass*. Against two-high: some versions convert to a seam when
    the middle of the field is open.
  - Note that Kelce often ran it deeper than 6 yards (8–10) off five-step timing.
  - Note that Mahomes–Kelce scramble chemistry (Kelce drifting into the QB's vision) is the bridge between this
    section and the scramble-drill section.

## D. Drills

- **Drill 1 (Fig 11):** Kelce's motion path ends angling *toward* the line of scrimmage (last point `(0.0, 11.4)` from
  a dip to d≈−2.7). A man in motion may not be moving forward at the snap, and a reader who has learned that rule in
  02-06 will flag it. End the motion flat (`d` unchanged on the last leg), or show him set. In the answer, add the
  coach's caveat: *travel = man, bump = zone*, but some match-zone teams travel a linebacker with tight-end motion, so
  confirm with the corners' and the nickel's leverage.
- **Drill 2 (Fig 12):** the football is fine (6 vs 5, two safeties at 11 deep owning Y/R in zero). In the answer,
  replace "set the protection to the mug" with what an empty QB actually does: slide the five so the free rusher comes
  from the side he can see, and throw hot away from him. With five blockers and six threats, someone is always free.
- **Drill 3 (Fig 13), answer error:** "Only six defenders are in the box against five linemen and a running back, so
  an inside run has a blocker for nearly every defender." The running back is the ball carrier, not a blocker. It's
  six defenders against five blockers, so the defense is +1 even in a two-high shell. That is exactly why two-high
  worked against the run and why the Chiefs answered with **RPOs that read the sixth man** (tie it back to Fig 2) and
  with screens. Rewrite that sentence.
  - Also, safeties "about 17 yards deep" is extreme. 14–16 is a more typical deep two-high against a speed team.
    Say "15–17" or move them to 15.

## E. Text accuracy and smaller points

- **Super Bowl ledger, LIV row:** "Jet Chip Wasp on third-and-15 started three touchdown drives". Wasp was one play on
  one drive. Write: "Jet Chip Wasp on third-and-15 kept alive the first of three late touchdown drives."
- **Spagnuolo paragraph:** "the Chiefs hired Steve Spagnuolo, a man he knew well". "He" has no antecedent. Write
  "a coach Reid knew well".
- **"Seven blockers' worth of attention" for 1.5 s:** fine, but say who is out. With 6 blocking plus a chip, only
  Hill, Watkins and Kelce run routes before the back leaks. That is the price of "Chip" and worth naming as the trade.
- **Spagnuolo is not only Cover 0.** A coach would want one sentence on the rest of his toolbox:
  - simulated pressures and creepers, which chapter 07-03 teaches;
  - disguising zero from two-high, which is exactly the Drill 2 picture;
  - Chris Jones as the interior rusher who makes six-man pressures work;
  - the 2023 defense's press-man corners (McDuffie, Sneed).

  As written, a reader could think zero is the whole system.
- **Super Bowl XLII:** "whose four-man rush beat the unbeaten Patriots" is fair shorthand, but the Giants also
  blitzed in that game. "Whose pass rush" is safer.
- **College graft:** the most visible college import besides RPOs is Reid's shovel-pass and shovel-option package
  (Meyer's Florida). It's worth a clause, and it's the play casual viewers actually remember. Optional.
- **Reid "learned his football in Green Bay in the early 1990s":** he had coached college line since 1983. Make it
  "learned his NFL football".

## F. gridiron use

- The custom `snapshot()` per-panel windows are justified: the camera follows a 57-yard ball. Fine.
- `no_numbers()` finds yard numbers by `alpha == 0.55`. That's fragile if gridiron's styling changes. Note this for
  the library owners; no chapter change needed.
- There are 2 `show_animation` calls (scramble, Wasp), well under the limit, and both print strips tell the story
  once A2 and A4 are fixed.
- The BDB `eval: false` cell is present. The Wasp is labelled a reconstruction, which is correct: it isn't simulated
  BDB of a real tracked play.

## G. Checked and fine

- **Fig 1 (staff timeline):** correct per FACTS C4 (Nagy 2023–25, Bieniemy 2026, Spagnuolo DC).
- **Fig 3 (late throws), Fig 6 (eras), Fig 8 (Cover 0 rates), Fig 10 (EPA):** clean, labelled, and the captions match
  the code.
- **Drill 2 formation:** legal, with seven on the line.
- **Fig 2 and Fig 4 formations:** legal.
- **Fig 5 formation:** legal (87, 5 OL, 81 on the line).
- **Fig 9 formation:** legal.
- **Super Bowl results and MVPs:** match FACTS.
- **2025 season (6–11, Mahomes ACL on Dec 14):** consistent with the footnote.
