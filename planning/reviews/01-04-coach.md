# Coach / film review: 01-04 What a Play Really Is

Reviewer role: NFL coach and film analyst. Checked the qmd as of 2026-10-06 07:16 and the PDF built at 07:16:51.
All 12 figures were re-rendered at 170 dpi (`_pdfbuild/01-04-what-a-play-really-is/coach/fig*.png`, made with a throwaway
`render.py` in that folder) and inspected along with the PDF pages.

**Overall:** the chapter is strong. The chain from call sheet to snap is accurate. The 15-second cut-off and the
one-way radio are right. The staff map is right. Stick vs Cover 3 is the right concept for teaching "read one defender".
There is **one real football error that appears in four figures and in the text (the protection)**, plus a set of
precision and completeness fixes. Items are in priority order.

---

## A. Must fix (football is wrong)

### A1. Slide protection: the line and the back are working the same side (figs 7 right, 8, 9 panel 1; text)
Right now the five linemen all angle **left** ("slide left") and the RB, aligned to the QB's **left**, also blocks
**left** (`block("RB", pts=[(1.0, -3.0)])`). A half-slide protection always pairs the slide with a back checking the
**opposite** side, the "man side". If the slide and the back go the same way, the right-side edge and any right-side
LB blitz go unaccounted for, and the back doubles the area the slide already covers. Any line coach will catch this.

Fix (keep the RB on the left, flip the slide):
- **OL:** C, RG and RT slide **right** (C takes the right A gap, RG the B gap, RT the C gap against the 7-technique SDE).
  LG and LT block man: LG on the WDT (the 1-technique shade), LT on the WDE.
  In code: `for k, dx in [("C", 0.9), ("RG", 0.9), ("RT", 0.6)]`, plus `LG`→`(-1.0, -0.4)` and `LT`→`(-1.0, -0.8)`
  so the man side is shown sitting and blocking its own man.
- **RB:** check the **WILL** (left B/C gap): `block("RB", pts=[(1.2, -2.0)])`. Keep the dotted "else slip out" release
  to the left flat. It is now correct, because the back releases from the man side.
- **Text, "Blockers have conditions too":** change "slide left" to "slide right". Add one clause: "the line slides one
  way and the back checks the other side, so between them every gap is accounted for."
- **Caption, fig-eleven-jobs panel 1:** change "the line slides left and the back takes the left edge" to "the line
  slides right and the back checks the weak-side linebacker before slipping out."
- **Code hygiene:** the block and rush loops are copy-pasted in `stick_base` callers, `stick_full` and `protect` (and
  the drops in `stick_full` and `cover`). Factor them into `protect_60(p)` / `rush4(p)` / `cover3_drops(p)` helpers so
  the fix happens once and the figures can't drift apart.

### A2. "Sit vs zone, turn in vs man" contradicts the text (fig 7 right)
The text says the stick route's man rule is "keep moving away from him" (break away from the defender's leverage). The
label and the single dotted branch, which goes up and **inside**, say "turn in". Against man, a stick or option route
breaks **away from leverage**, in *or* out.
Fix: draw **two** short dotted branches from the top of Y's stem, one to (6.5, +2.5) and one to (6.5, −2.5) in route
offsets, and relabel "sit vs zone; vs man, break away from him".

### A3. Call sheet: "Jumbo Rt 32 Sneak" is incoherent (fig 2)
In hole-numbering systems, "32" means the 3-back (fullback) through the 2-hole. A sneak is the QB, so it is the "1" or
"0" back, or simply "QB Sneak". Change it to **"Jumbo Rt QB Sneak"** (or "Jumbo 10 Wedge").

### A4. Call sheet: "Gun Rt 18 Draw (vs blitz)" (fig 2)
A draw beats soft, rush-heavy looks: dime, two-high, linebackers bailing on 3rd & long. Calling one into a blitz puts
an extra defender in the box. Change the note to "(vs dime / two-high)". If you want a blitz-beater in the box,
add "Gun Trips Rt Bubble Screen (vs pressure)" or "Gun Rt Slot Screen".

---

## B. Should fix (precision and realism)

### B1. The hook's "pointing at a linebacker" is never explained
The opening scene has the QB "pointing at a linebacker and shouting". The chapter only answers the shouting (Omaha,
dummy calls). The point is the **protection ID**: the QB or center declares the "Mike" (the reference linebacker) so
that all five linemen and the back count the defense the same way, and the slide is set from it. You can't teach
"protection" as a play-call chunk without mentioning this. Add 2–3 sentences in the Protection bullet of "Anatomy of a
play call" (or right after A1's text), with a forward link to 04-02. Suggested text: "That's what the pointing at the
line usually is: the quarterback or center naming the 'Mike', the linebacker the protection counts from, so all six
blockers agree on who is whose."

### B2. "He is the only one who can" change the call (Madden callout)
That is true for the *play*, but the center commonly changes the slide and line calls, and receivers make sight
adjustments. Change it to "he is the only one who can change the play (the center can adjust the blocking, and
receivers adjust routes by rule)".

### B3. Defensive calls carry built-in checks
The paragraph "Defensive calls are built the same way…" should add one sentence: a defensive call usually comes with
automatic **checks** by formation (for example "vs trips, check to X"), and the Mike sets the front's strength call
while the safeties make the coverage check. That is the defense's equivalent of the audible, and it is half of the
"pre-snap contest" section. Without it the defense reads as static until the snap.

### B4. Personnel order: the offense moves first
"Both coaches call blind" is right, but the *asymmetry* is the important part. The offense picks its personnel
first. The defense sees it and matches. The rules then protect the defense's chance to match when the offense
substitutes, which is why the umpire stands over the ball. Make that explicit in one sentence in "Both coaches call
blind". The current text says the offensive play-caller knows "which players the defense has on the field", which is
often not yet true when he first picks personnel. It also sets up Predict 3.

### B5. Huddle depth (text, "The huddle")
"A tight circle a few yards behind the ball" is wrong for the NFL. A standard huddle is roughly **7–10 yards** behind
the ball, and that distance is what separates it from the sugar huddle ("a few yards from the ball") later in the
chapter. Change it to "about seven to ten yards behind the ball".

### B6. "The more players a word affects, the earlier it comes" (Anatomy)
"Zip" (one player) comes before "60" (six players), so the rule as stated is broken by the chapter's own example.
The real logic is the **order of events**: line up (formation), move (motion), block (protection), run routes
(concept), then exceptions (tags). Reword it that way. The "left tackle cares about 60, not X Dig" sentence can stay.

### B7. Dialect notes the chapter is missing (Verbiage section, 1–2 sentences)
- **Trips vs Trey:** this formation uses the inline TE as the third receiver. Many playbooks (Gruden/West Coast
  lineage) call that **"Trey Right"** and keep "Trips" for three detached receivers. Mention it in the Formation
  bullet. It is exactly the kind of dialect difference the chapter is teaching.
- **Motion words:** "Zip" for a short Z motion toward the ball is common in Shanahan/McVay-family verbiage. Other
  systems say "Z-in", "Zoom" (often the F) or "Rip/Liz" variants. One line saying motion words vary by system.
- **Protections:** number series (60/70s) belong to West Coast lineages. E-P and others use words ("Ringo/Lucky"
  slide calls, "Scat", "Jet").
- Name the **third family**, Air Coryell digit route-tree calls ("896 F-Post"), in one clause before the forward
  link to 04-08, so the reader doesn't think there are only two traditions.

### B8. Stick: say what Z's go is *for*
Panel 2 says "four receivers run their part of the concept" but never explains the outside vertical. The Z go is the
**clear-out**: it carries the Cover 3 corner deep. That is *why* the nickel is the only man left for both H and Y and
the two-on-one exists. Add one sentence to "The quarterback reads one defender": "Z's vertical is there to run the
cornerback off, so the slot defender is alone with two receivers." Also: stick depth is usually 5–6 yards and is often
set relative to the sticks on third down ("a yard past the line to gain"). The 3rd-and-4 setup is a good place for
half a sentence on that.

### B9. Fig 7 and fig 8: the right corner ignores the Zip motion
After Z zips from w≈17 to w≈13, the RCB is still at w≈17, four yards outside his man with no reaction. In Cover 3 he
would bump in with the motion to about 1–1.5 yards outside leverage. Fix: in `stick_base` when `motion=True`, set the
RCB to `moved(d=7.0, w=14.5)` (the Cover 3 corner also plays 7–8 yards off, deeper than the helper's 6.5), or add a
`p.path("RCB", [(7.0, 14.5)], ...)` pre-snap adjustment in the animation. The same `moved(d=7.0)` applies to the LCB.

### B10. Throw timing in fig 8 (animation)
`pass_to("Y", t=1.15)`: Y has run only about 5 yards at 0.9 s and is still climbing when the ball comes out. From the
gun, a stick throw usually leaves on the QB's hitch at **~1.5–1.8 s**, as Y settles at 6. A 12–13 yard throw then takes
~0.6–0.7 s, not "just under a second". Fix: `p.pass_to("Y", t=1.6)` (and in `qb_read`). Change `TIMES` to
`[-1.2, 0.0, 1.1, 2.1]` so the third panel still shows the NB's choice and the fourth shows the ball arriving. Update
the caption to "the ball is out about a second and a half after the snap and arrives well under a second later". The
four-man rush stalling 1.6 yards past the LOS is fine as a picture of engaged blocks.

### B11. Predict 2: the hot-throw rule is the natural follow-up
The parenthetical about two defenders and the progression is good. Add the other common outcome: if the defense
**blitzes** more than six can block (the SS and NB both come), the ball comes out "hot" to the area the blitzer
vacated. Stick is a hot-friendly concept for exactly that reason. One sentence, linking 04-02.

### B12. Staff: missing titles a reader will see on broadcasts
Add one sentence: many staffs also have a **passing-game coordinator**, a **run-game coordinator** and an
**assistant head coach** (Kingsbury's 2026 Rams title is an in-chapter example), and these are usually the people in
the booth. Also mention sideline **tablets** in the position-coach paragraph: they are the tool for "fix something
before the next series", since coaches show the player stills of the last series. Have the fact-checker confirm when
in-game *video* on sideline tablets was allowed before printing a year; if it can't be verified, leave the year out.

---

## C. Nice to have

- **Who calls plays:** "The most common arrangement is that the OC calls the offense". In recent seasons something
  close to half the league's head coaches have called their own offense (2026 list in FACTS §9: Shanahan, McVay,
  Reid, LaFleur, O'Connell, Johnson, plus others). Either get a verified count or soften to "very common… on offense,
  nearly as common for head coaches to keep the call". Optional example for a defensive HC caller besides Glenn:
  Mike Macdonald (Seahawks), but only if verified.
- **Lions film room:** as written it is a narrative, not film. Make it observable by adding a small before/after
  table from nflverse pbp for 2025 (early-down pass rate, neutral no-huddle rate, 4th-down go rate, seconds per
  play) split at the week Campbell took over. Get the week verified first. Those are the "fingerprints" the callout
  already tells readers to look for.
- **Omaha:** add that it was widely reported as a live-cadence signal (that the snap was coming on the next sound),
  which the course can source, so the "joke is the lesson" point has the real use beside it.
- **Wristbands:** add that defenses use them too (green dot, safeties, sometimes everyone) for call numbers. That
  makes the "wristband offenses" point two-sided.
- **Radio equity rule:** if one team's coach-to-player system fails, the league disables the other team's too.
  Verify it and add one line to the "radio" paragraph.
- **Delay of game glossary:** it can also be called on the defense (for example, delaying the ready-for-play). Add
  "usually on the offense" or leave as is.
- **Call sheet realism:** the caption could say real sheets carry 100+ calls with sections like "shots", "screens",
  "backed up", "4-minute" and "2-pt". The figure is fine as a simplification.
- **Run-play "rules":** the "rules not paths" section is all pass. One sentence with a run rule would generalise it,
  for example zone blocking's "covered or uncovered: if a man is in my play-side gap I block him, if not I climb to
  the linebacker", with a link to 03-02.

---

## D. Diagram-by-diagram verdicts

| Fig | Verdict | Notes |
|---|---|---|
| 1 staff map | OK | Accurate. Optional: add the passing/run-game coordinator titles (B12). |
| 2 call sheet | Fix | A3 (32 Sneak), A4 (draw vs blitz). Otherwise realistic in style. |
| 3 anatomy | OK | Text reword B6, dialect B7. |
| 4 play clock | OK | The timings are plausible (calls in by ~:28, huddle break ~:19, snap ~:05). The defense "sees subs" before radioing, which is right. |
| 5 comm flow | OK | Correct: one-way radio, booth → caller by headset. |
| 6 no-huddle chart | OK | Not football-diagram content. The sugar-huddle caveat is correct. |
| 7 Madden vs coach | Fix | A1 (slide and back same side), A2 (man branch), B9 (RCB not adjusting to Zip). Formation legal: 7 on the LOS (5 OL + X + Y), H and Z off the ball, motion lateral. Cover 3 shell, 4-2-5 over front to the TE, and DL techniques (7/3/1/wide 5) are sensible. |
| 8 stick frame strip | Fix | A1, B9, B10 (throw at 1.6 s). Drops are textbook Cover 3: 3 deep, 4 under, NB curl/flat widening with the arrow. |
| 9 eleven jobs | Fix | Panel 1: A1 plus the caption. Panels 2–4 are correct. |
| 10 predict clock | OK | |
| 11 predict read | OK | The NB sitting inside, so the ball goes to H in the flat, is the right answer. Mirror A1's protection change here if any blocks are added. |
| 12 twelve men | OK | Legal 2x2 (7 on the line). The two-high nickel is sensible. The answer's live-ball vs dead-ball distinction is correct. Optional: put the "L" at d≈5, w≈−12 so he doesn't read as the slot defender over H. |

## E. Code and gridiron notes (for the library owner, not chapter edits)
- `frame_strip` draws the ball too small to read in print. The chapter overlays its own ball and flight line. Worth
  fixing in `animate.py`.
- `defense()` doesn't react to motion: corners and the nickel keep their pre-motion alignment (B9). A
  `follow_motion=True` option, or a documented `p.path()` adjustment pattern, would help every motion chapter.
- `formations.offense("gun_trips")` puts an inline TE as #3. Consider a docstring note that many systems call this
  "Trey" (B7).
- The Cover 3 corner depth of 6.5 in `defense()` is on the shallow side for Cover 3 (7–8 is typical) and fine for
  two-high or quarters.
