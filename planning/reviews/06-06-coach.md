# Coach / film review (round 2): 06-06 Disguise, Rotation, and Split-Field Coverage

Reviewer role: NFL coach and film analyst. I checked the qmd as of 2026-10-06 08:29 and the PDF built at 08:30.
All 14 figures were rasterized at 80 and 110 dpi (`_pdfbuild/06-06-coach2/`) and inspected. I also extracted the
two rotation plays and printed every defender's (d, w) at t = 0, 1.0, 1.7, 2.0 and 2.6 s
(`_pdfbuild/06-06-coach2/s/pos.py`) to check the timing. The chapter was not edited.

**Overall:** every round-1 item has been fixed: A1–A5, B1–B6, C1–C8, D and E. The Predict-3 spin is now correct,
with the FS walking down toward the motion, the SS going to the post and the RCB left over grass. The NFL and college
hash numbers are right. "Middle of the field closed or open, then the corners" has replaced deep-defender counting.
Leverage is now taught as the *help* tell. The hole shot is placed correctly. The Cover 2 corners sink and widen,
the bender splits the safeties, the trips sets are detached for poach, and the dialect notes for solo and rat are in.
The chapter is now football-sound. What remains is **two diagram errors where the picture contradicts the text**,
followed by smaller realism and nuance items.

---

## A. Must fix (the picture contradicts the football or the text)

### A1. fig-rotate-to-robber: the Cover 3 corner gets beaten deep by X's go route
`p.drop("LCB", (16.0, -16.0))` at the default speed of 5 yd/s puts the corner at 16 yards by 2.0 s, and he then
**stops**. X runs `r.go(20)` at 7.5 yd/s, reaching 14.3 yards at 2.0 s and **18.8 yards at 2.6 s**. In panel 4
("Cover 3 robber"), X is about 3 yards past and outside a deep-third corner who is standing still. That is a
busted Cover 3 in the figure meant to show Cover 3 working. A deep-third corner keeps his cushion and stays on top
of #1 vertical.

Fix: `p.drop("LCB", (20.5, -16.0), speed=5.5)`. At 2.6 s he sits about 1.5 yards over the top and slightly outside
X, which is a textbook deep-third carry. Leave the RCB as he is: Z breaks in at 12, so sinking to 16 and squeezing
is right. Optional: `p.drop("RCB", (15.0, 15.5))` so he finishes over the dig's stem rather than over empty
grass.

### A2. fig-predict-poach: the answer says "pressed with inside leverage", but the corner is head-up
`trips_defense()` puts the LCB at (1.5, **-15.0**), exactly on X's w. fig-poach overrides it to -13.8, but Predict 2
does not. The answer's whole throw recommendation ("the corner gave up the outside, so back-shoulder or go route
outside") depends on an inside shade the reader can't see.

Fix, in the Predict 2 cell after `dfn = trips_defense(off, fs_w=-4.0)`:
`dfn = [p.moved(d=1.2, w=-14.0) if p.key == "LCB" else p for p in dfn]`, which is a press with a clear 1-yard
inside shade. Add "pressed, shading inside" to the caption's "and at the left corner" so the reader knows what to
look for.

---

## B. Diagram realism (should fix)

### B1. fig-cover6-split: the deep zones leave the deep middle uncovered
The boundary `½` ellipse is centred at w = -10.5 and 14 wide (-17.5 to -3.5). The field-safety `¼` is centred at
w = 6 and 10 wide (1 to 11). In the figure there is a visible empty strip of deep grass straddling the ball. In
Cover 6 the boundary half-field safety owns everything from the boundary to the middle of the field, and the
quarters safety's quarter starts at the middle. Fix:
- `p.zone((17.5, -9.0), (8, 17), "½")`, which covers about -17.5 to -0.5.
- `p.zone((17.0, 5.0), (8, 10), "¼")` for the field safety, covering about 0 to 10.
- `p.zone((17.0, 15.5), (8, 11), "¼")` for the field corner.
- Boundary corner: give him the Cover 2 outside shade and keep him from stepping downhill. Align at
  `"LCB": (5.0, -16.0)` and use `p.drop("LCB", (5.5, -17.0))`. The flat zone stays where it is. (He currently
  starts head-up on X and moves a yard *toward* the line.)
- Optional realism: with the ball on the left hash, the field-side receivers would split wider. Use Z at about
  w = +18 (field numbers) and Y at about +11, and move RCB, SS and NB with them. This also makes the field side
  look like the bigger problem the text describes.

### B2. fig-tells: in a Cover 1 picture, the nickel is on the tight end and the Will is on a slot receiver
In `gun_2x2`, Y is the **TE** (flexed slot right) and H is a **WR**. The chapter's base alignment apexes the Will
over H and puts the nickel on Y. For zone figures that hardly matters. In fig-tells, though, the caption calls a
**man** coverage (Cover 1 robber), which would leave a linebacker on a slot receiver and the nickel on the tight
end, the opposite of how NFL nickel defenses match up. Fix, in fig-tells only: put the nickel over H,
`"NB": (1.5, -8.2)`, and the Will apexed over Y, `"WILL": (4.5, 7.0)`, then move the "nickel tight on the slot"
pointer to `text_at=(6.8, -15.5), to=(1.5, -8.2)`. Alternatively, keep the figure and add half a sentence to the
caption: "(the slot to the right is the tight end)".

### B3. Detached trips spacing (fig-poach, fig-predict-poach)
`trips(detached=True)` sets Y at w = 6.0. That is about 1 yard outside where the in-line TE stood, so it reads as a
wing or tight flex, not a third slot. H is at 10 and Z at 17. A real detached-trips split is about 6.5–7.5 / 11–12 /
17–18. Change it to `p.moved(d=-1.5, w=7.0)` for Y. If you do, move the poach FS's landing point to
`(17.0, 3.0)` and the Mike's drop to `(7.0, 5.0)` to stay over the #3 seam. Low priority, but a coach notices.

### B4. fig-predict-motion: "walks down and out toward him"
Z finishes at w ≈ -3 (passing the QB), and the FS walks to (9, -8), which is *outside* Z's position at the snap,
toward where Z is heading. That is correct football: he is taking the flat that Z's motion threatens. "Out toward
him" still reads oddly. Caption: "...walks down toward the side Z is heading to, landing over the flat..."

---

## C. Text precision

1. **Trips section, "Nobody's rule mentions #3."** This is overstated. Most quarters systems give #3 to someone:
   the apex or hook player walls him, and the trips-side safety's rule is "#2, then #3 if #2 goes out". The real
   problem is **#2 and #3 both vertical**, where the safety can carry only one. Reword: "Quarters rules are built
   for two receivers per side. The safety reads #2, and if #2 and #3 both run vertical he can carry only one of
   them, while two defenders on the backside guard one man."
2. **Corner disguise: add the invert.** "Corners can disguise too" mentions press-bail and cloud. The other common
   two-high disguise is the **invert** (corner and safety trading jobs, the safety rolling to the flat and the
   corner bailing to the deep half). The tracking code comment already mentions it. Add half a sentence:
   "...or trade jobs with the safety (an *invert*: the safety comes down to the flat and the corner bails to the
   deep half), as Palms does on one side."
3. **"Seven or eight yards off and ready to bail."** Coaches usually say *bail* for press-bail. From 7–8 yards off,
   a deep-third corner backpedals or shuffles at the snap. Use "ready to backpedal or turn and run to a deep third".
   Optional, but it avoids blurring the term 06-01 owns.
4. **Optional nuance (late rotation):** give the reader a coaching benchmark. The post safety wants to be at his
   landmark by the time the QB hits the top of a 5-step drop, roughly 1.3–1.5 s from the gun. That ties the
   physics section to the QB's clock. Skip it if there is no source.

---

## D. Film room

- **Vikings 2023–2025:** good now, with a "what to notice" and the "narrowly" in the caption. No change.
- **Rams 2020:** accurate. The front and alley-fit point is in. No change.
- **Evero:** the text now says "rotation from a two-high shell", which matches the source. Good.

---

## E. Code

- gridiron is used sensibly throughout. The two-time-state helpers (ghosts, strip, pointer, divider) are drawn on
  the Field's ax, as they should be. No gridiron changes are needed.
- The A1 bug comes from a gridiron behaviour worth remembering: `drop()` **parks** the defender at the end point.
  Whenever a receiver keeps running (go, seam), the drop landmark has to be deep enough to stay on top of him at the
  last time shown. A quick check is to print `p.position(k, t)` for the last panel time, as I did in
  `_pdfbuild/06-06-coach2/s/pos.py`.
- `trips_defense()`'s LCB default of w = -15.0 (head-up) is the root of A2. If you'd rather fix it once, set it to
  -14.0 there and drop the per-figure override in fig-poach. That also gives solo and stubbie an inside-shaded
  corner, which is fine for both.
