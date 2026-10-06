# Coach / film-analyst review: 02-02 Formation Rules and the Language of Alignment

Reviewed 2026-10-06 against the chapter source and a fresh build of
`pdfs/02-02-formation-rules-and-vocabulary.pdf` (19 pages, rasterized at 90 dpi). I looked at
every figure (13 figures, no animations).

**Verdict:** a strong, accurate chapter. The rules material (on/off the line, covered receivers,
seven on the line, reporting, the 2015 change) is right, and the Patriots and Lions film rooms
are well chosen and fairly told. There are no football errors in the prose that would mislead a
reader badly. The problems are in the **pictures**: one defense that no NFL staff would line up
(base 4-3 against a 2x2 with an uncovered slot), a "wing" that is drawn as a flexed player in two
figures, an H-back inside the tackle, eligible backs left unringed under an "aqua = eligible"
legend, and the `U` letter used three times without being taught. Also missing are the strength
code words that defenses use in their calls (the spec asks for terminology dialects).

---

## Must fix

### 1. `fig-strength` panel 1: base 4-3 against 11 personnel 2x2 leaves the slot unguarded
The offense is `pro_11()`: X, **H in the left slot (w −9)**, Y in-line, Z. The defense is a 4-3
Over with both corners outside and **nobody within 6 yards of H**: the Will is in the box at
w −3.4. Against 11 personnel with a slot receiver, NFL defenses play nickel most of the time
(02-01 teaches this; FACTS §10: base only 29.7% of 2025 snaps). In base, the Will would have to
walk out over H, which takes him out of the picture the panel is trying to show. A coach will
see this immediately.

**Fix (preferred):** make the offense personnel that brings out a 4-3, so the picture stays
"Sam and SS to the tight end". Use **21 personnel, I-formation**: drop H, add
`P("FB", "FB", -4.4, 0, "F")` with the tailback at `TB_D`, keep X on the line left, Y in-line
right, Z off right. Caption: "The offense is 21 personnel (a fullback, F, and one tight end)".
This also puts an F in the chapter's pictures (see item 4).
**Alternative:** keep 11 personnel and switch to a nickel front (`defense("4-2_nickel"/…)`) with a
nickel back over H at about (d 5, w −9). Then drop "Sam" from the caption, since a nickel
usually has no Sam, and point at the strong safety and the line's strong-side shade instead.

The same issue affects the Drill 2 answer and "Watch for it on Sunday". Both say "the Sam ...
goes left" or ask "which side did the bigger linebacker (the Sam) go to?" against 11 personnel.
Reword as "the front (the defensive line's shade and the linebackers) sets to the tight end".
For the Sunday checklist, add "in nickel there may be no Sam: watch which side the defensive
tackle lines up outside the guard (the 3-technique, see [A First Look at
Defense](02-05-a-first-look-at-defense.qmd)) and which safety walks down".

### 2. The wing is drawn as a flexed player (`fig-te-spots`, `fig-predict-count`)
- `fig-te-spots`: WING is at `(OFF_BALL, WING_W + 1.3)` = w 7.5. The right tackle is at w 3.2,
  so this "wing" is 4.3 yards outside the tackle. When the tight end *is* the wing, the end man
  is the tackle, and a wing sets about a yard outside and a yard behind the tackle's outside foot
  (w ≈ 4.5–5.0, d ≈ −1.3). At 7.5 he looks like the FLEXED player next to him (11.8). The spots
  were clearly pushed apart to avoid overlapping the in-line marker.
  **Fix:** draw the attached spots on the **left** side of the line and the detached ones on the
  right: WING at (−1.4, −4.8) "a yard off the line, just outside the tackle", H-BACK at
  (−2.2, −3.6) (see item 3), IN-LINE stays at (−0.7, 4.8), and FLEXED and SPLIT stay right.
  Widen `lateral` to about (−14, 21.5) and drop the "right half of the formation" wording.
  Another option is to keep the wing on the right at `WING_W` (6.2) with a ghost in-line TE and
  say "a wing outside the in-line tight end". Either way, the wing should be within about 1.5
  yards of the end man.
- `fig-predict-count` (Drill 1): U is at `-WING_W - 0.4` = w −6.6, which is **3.4 yards outside
  the left tackle** (no TE on that side). The caption says "a yard off the line just outside the
  left tackle". **Fix:** `P("U", "TE", OFF_BALL, -4.7)`. The drill's logic is unchanged.
  (In `fig-reporting` and Drill 3, U at 6.5–6.6 is outside an in-line player at 4.8, which is
  correct.)

### 3. `fig-te-spots`: the H-back is inside the tackle
H-BACK is at (−2.7, 2.3), behind the guard–tackle gap (RG 1.6, RT 3.2), and labelled "behind the
tackle". The H-back's offset spot (Joe Gibbs' original, and Shanahan-tree "sniffer"/offset
alignments) is **off the tackle's outside hip**, about 1–2 yards deep and 0.5–1 yard outside the
tackle. From there he can kick out, arc, or lead through the C gap. **Fix:** about (−2.0, ±4.0)
(left side per item 2), label "H-BACK (offset): off the tackle's hip, a yard or two deep".

### 4. The alphabet never shows F, and uses U without teaching it
- The spec's label map is "X/Y/Z/H/F on a 2x2 and on a 3x1". `fig-label-map` shows X, Y, Z and H
  but **no F**. The text says F is often the fullback in 21 personnel.
  **Fix:** add a third, short panel, "21 personnel, I-formation: F is the fullback": X on the
  line left, Y in-line right, Z off right, F at (−4.4, 0), R at (−7, 0), with F and R ringed.
  If figure height is tight, the 21-personnel panel 1 from item 1 can carry an "F" label instead.
- **U** appears in `fig-reporting`, Drill 1 and Drill 3 ("two tight ends, Y and U") but is not in
  the alphabet section. **Fix:** add a bullet or a sentence to the H/F bullet: "Many NFL
  playbooks call the second tight end **U** (others use H or F for him); the running back is
  usually R, T or B, depending on the system." Also say in one clause that the running back
  usually has a letter of his own, because readers will see "R" in every diagram.

### 5. Eligible backs are unringed under an "aqua = eligible receivers" legend (`fig-label-map`)
`fig-legal-illegal` rings R as eligible, which is correct. Two figures later, `fig-label-map`
says "aqua rings = eligible receivers" but leaves **R unringed in both panels**, and in the 3x1
**the shotgun Q is eligible** too (only the under-center QB is excepted, as the chapter itself
says). A careful reader will conclude the back isn't eligible. **Fix:** ring R in both panels, or
change the caption to "aqua rings = the four receivers named by letter (the back, R, is eligible
too)". Optionally add one line to the shotgun section: "a shotgun quarterback is technically an
eligible receiver, which is what makes trick plays to the quarterback possible."

---

## Should fix (nuance a coach would insist on)

### 6. Strength code words (the dialect the spec asks for)
The chapter only has "Strong right!". Real defensive calls use **paired code words** so the
defense can name two strengths at once. Many staffs use something like **Rip/Liz** (right/left)
for the receiver or passing strength and a second pair such as **Ram/Lou** or **Roger/Lucy** for
the tight-end or front strength. Some call field and boundary instead ("Field! Boundary!"). This
fits the "two strengths at once" callout exactly: the Mike yelling "Ram ... Liz!" is the defense
saying "front right, coverage left". Add 2–3 sentences after panel 2's paragraph, framed as "for
example" (the exact words vary by staff). Offenses have a matching dialect point: in many
West Coast–style playbooks the "Right/Left" in a formation name tells the **Y (tight end)** where
to go, while in spread or Air Raid systems it usually names the **trips/passing side**. One
sentence would do it, with a link to [Offensive Systems and
Languages](../04-the-passing-game/04-08-offensive-systems-and-languages.qmd).

### 7. Passing strength: counting includes the back
"Coaches number those receivers from the outside in" is right. Coaches would add that the count
includes the tight end **and the back**: a back offset to the trips side, or one who releases to
it, becomes #3 or #4. Coverage rules ("#3 vertical", "the back to my side") depend on this. One
clause is enough.

### 8. The hash as a landmark (spec: "the numbers, the hash")
The section uses the hash only to explain the asymmetry. It never uses it as an alignment
landmark, which is how inside receivers align. Add 2–3 sentences:
- Slot receivers usually align by the **hash** or by "splitting the difference" between the
  tackle (or end man) and the outside receiver, not by the numbers.
- Boundary receivers often have a **minimum split**: no closer than about 5–7 yards to the
  sideline, or "top of the numbers", so they keep room for an out or a fade. That's why the
  boundary X "looks tight" (it complements the existing misconception callout).
- Optionally add "plus split / minus split" (wider or tighter than the landmark), the
  vocabulary used in coaching tape.

### 9. "In pass protection he usually takes the side he's on" (Offset backs)
This is too categorical. In many shotgun protections the back is assigned to the side **away**
from the slide, and he often **crosses the quarterback's face** to block (a "scan" or "cross"
check). Teams also set the back by protection (the "man side"), not by run direction. Suggested:
"in pass protection he may block his own side or cross the quarterback's face, depending on the
call". The run half of the sentence (the handoff often goes away from the back's side, with the
back crossing the quarterback) is right; keep it.

### 10. Patriots film room: say what "the count" is
"One of their eligible-numbered players reported to the referee as ineligible **to make up the
count**" doesn't say which count. With four linemen, the offense still needs five
**ineligible** players among its seven on the line (the interior five). In the NFL that means
players wearing 50–79 **or** eligible-numbered players who reported ineligible. Add that
sentence and you also explain the trick: Vereen had to report because his number said eligible.
Also add that he was ineligible twice over: on the line *inside* Edelman, he was a covered
receiver anyway. This ties the film room back to the covered-receiver section and strengthens
the "position plus announcement" lesson. (The fact-checker should confirm the exact rule article
for "five ineligible numbers on the line" before a footnote cites it.)

### 11. `fig-on-off`: Y is covered but this goes unexplained
In the close-up, X is on the line outside Y, so **Y is covered**. The figure is correct to leave Y
unringed, but the caption lists Y among the players on the line without saying why the tight
end isn't ringed, one section before covered receivers are taught. **Fix:** add to the caption:
"(Y has no ring: X is on the line outside him, so Y is covered; more on that in a moment.)" Or
move X off the line and drop his ring. The figure's job is on/off, and that keeps it to one
idea.

### 12. `fig-reporting`: make the bite visible and tidy the defense
- Panel 3: the E's crash path `(-1.2, 2.6)` is hidden under the #70 ring, so "E bites on the
  fake" points at nothing. Lengthen it to about `(-1.8, 3.6)` and make the E visibly end up
  inside #70. Optionally highlight the E.
- The lone corner (LCB) at (2.0, −10.0) stands over empty grass. With no receivers on that side,
  a goal-line corner squeezes to about 2–3 yards outside the end man: move him to about
  (2.5, −8.0). (He then becomes the man who should cover #70's release, which makes the throw
  more honest: the E's bite plus the corner's run fit leave #70 alone.)
- Panel 1, minor: the NFL referee stands about 10–12 yards deep, usually on the quarterback's
  throwing-arm side. At (−5.4, −5.4) he looks like a back. The window stops at −8.8, so either
  widen `window` to about −11 and place him at (−10, 5), or leave him and accept the license.

### 13. Drill 1 answer: name the third "fix"
Add one line: "Z stepping up also makes seven, but then Z covers Y, who becomes ineligible:
legal, and the wrong fix if you want your tight end in the route." This reinforces panel 3 of
`fig-legal-illegal` and costs one sentence.

### 14. Drill 3 answer: the play-action partner
"A fake to the right and a throw off it" is fine. A coach would name the classic answer to this
look: **the boot** back to the left, away from the fake, with the reduced Z often running the
long crosser toward the bootleg side and X the backside comeback or post. Both men's splits
make this possible. One sentence and a link to [Play-Action, Boots and
Screens](../04-the-passing-game/04-05-play-action-boots-screens.qmd).

---

## Diagram polish (no football errors)

- `fig-legal-illegal`: the line-count digits "2" and "6" sit on the hash tick column and are
  hard to read. Raise `dy` in `count_line` to about 2.8, or draw with `box=True`. In panel 3,
  the label "Y: on the line but not at the end" starts on the hash ticks, which cut its left
  edge. Move it to w ≈ 8.0.
- `fig-label-map` 3x1: the label "Y in-line (#3)" overlaps the hash ticks. Shift it to
  w ≈ TE_W + 0.8.
- `fig-te-spots`: FLEXED at w 11.8 is a full slot alignment (8.6 yards outside the tackle). A
  flexed tight end more often sits 3–6 yards outside the tackle. Something like (−1.5, 9.5)
  separates him better from SPLIT WIDE and is more typical.
- `fig-split-ladder`: "FIELD SIDE (wide)" is drawn across the shaded numbers lane. Nudge it to
  w ≈ 22.5 or give it a backing box.
- Everything else is clean: no labels clipped by the field edge, alignments legal in every
  panel I checked (seven on the line, ends correct, a maximum of four backs).

---

## Checked and correct (no change)

- On/off the line (helmet through the snapper's beltline; backs a yard deep; the strip in
  between is illegal); covered-receiver logic; why X is on and Z is off; "weird is legal".
- Panel 2/3 logic of `fig-legal-illegal` and the Drill 1 count.
- Strength by TE, receivers and field; NFL vs college hash arithmetic (29.75 vs 23.6 yards;
  ~6 vs ~13 yards difference).
- X/Z history (Hirsch flanker), the Air Raid Y-as-slot dialect, H/F team-to-team variation.
- QB depths (under center, pistol ~4 with the back about 7, gun ~5), what each gives up, the
  shotgun and pistol history; data claims (69/34/28%; 81% PA from under center; 97% gun on
  3rd-and-7+).
- Splits ladder and the tells (reduced: crack or outside-breaker; wide: inside route or iso);
  "judge a split by landmarks".
- Reporting mechanics, alignment still decides eligibility, NCAA strictness, A-11.
- Patriots (Vereen on the line in the slot, Hoomanawanui at the left tackle spot, the 2015
  inside-the-core rule) and Lions (Sewell, Skipper, the St. Brown 70-yarder; "watch the
  safeties" is excellent coaching advice).
- Drill 2's "make the defense's definitions disagree" answer, apart from the Sam wording in
  item 1.
