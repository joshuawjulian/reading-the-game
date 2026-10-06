# Coach / film review: 01-03 The Twenty-Two

Reviewer role: NFL coach and film analyst. I reviewed the qmd as of 2026-10-06 14:29 and rebuilt the PDF
(`build_pdfs.py 01-03-the-twenty-two --html` returned OK). All 13 figures were rasterized at 110 dpi
(`_pdfbuild/01-03-the-twenty-two/hi-*.png`) and inspected. I also dumped the helper coordinates for
`i_form`, `4-3_over`, `gun_2x2`, `nickel`, `gun_trips`/`dime` and `singleback`.

**Overall:** this is a very good position primer. The position definitions, eligibility rules, jersey history, special-teams
units and combine data are accurate, and the position / alignment / assignment section is exactly the right idea for
this book. The 4-3 Over in fig 1 is a real front: 3-technique to the tight end, 1-technique shade weak, Sam over the tight end,
Will stacked weak. The field-goal and punt units are legal and realistic.

**There is one real football error. It is in the chapter's only animation and in the text around it (the lead run).** There
are also two factual claims that the chapter's own combine chart contradicts, and one drill that a reader cannot answer
from the picture. Everything else is nuance or polish. Items are in priority order.

---

## A. Must fix (the football is wrong or misleading)

### A1. The lead run is blocked wrong: the double-team never climbs, so the Mike is "unblocked" (fig-lead-run and text)
The play is drawn as follows. LG and C double the 1-technique (WDT, w=-0.7) and **stay on him**. The FB takes the Will.
The Mike is left free to fill the hole. The text then teaches this as the design: "Nobody on the line blocks a linebacker
on this play; that's the fullback's job" and "Here it left the Mike."

No coach would draw the iso/lead this way. The whole point of the double-team on the playside 1-technique is that it is a
**combo**: two linemen move the tackle, and then one of them comes off onto the backside linebacker (the Mike). The fullback
"isolates" the one linebacker left over, the playside Will. That is where the name **iso** comes from. If you leave the
linebacker who sits directly over the hole unblocked, you have a busted play, not the design. The drawn result says the
same thing: the Mike tackles the runner for about 2 yards.

The math is also misstated. The offense has 9 blockers (11 minus the QB and the ball carrier) against 11 defenders, so
**two** defenders are always unblocked. In the current drawing, the Mike, the Sam (Y never reaches him) and both
safeties are all free.

**Fix: the textbook "Iso weak vs 4-3 Over", which keeps the same alignments.**
- LT: base-block the WDE (5-technique) out. Keep this.
- LG + C: combo the WDT. **C climbs to the Mike** at about 0.6–0.8 s. For example,
  `p.block("C", pts=[(1.0, -0.2), (3.6, -1.0)])`, and stop the Mike at about (2.8, -1.0) absolute when they meet. LG stays
  on the WDT.
- RG: base the 3-technique (SDT). RT: base the SDE. **Y: block the Sam** (backside). Give Y a path that actually reaches
  the Sam at about (3.5, 5.0); right now `(1.6, 0.6)` relative stops him at the line.
- FB: iso the Will **in the hole, about 1 yard past the LOS, by about 1.1 s**. Use `p.block("FB", pts=[(3.2, -2.4), (6.0, -2.8)], speed=6.5)`.
  Make the Will attack downhill: `p.path("WILL", [(1.6, -2.8)], absolute=True, delay=0.2, speed=4.5)`.
- X / Z on the corners: keep.
- That leaves **the two safeties as the unblocked defenders**, which is what a well-blocked inside run looks like ("blocked
  to the safety"). Have the FS fill the alley and meet the tailback about 5 yards downfield.

**Text changes:**
- Offensive-line bullet: "each lineman blocks the man in front of him, and the two who double-team the nose tackle finish
  with one of them climbing to the Mike."
- Linebackers bullet: "The Will takes on the fullback; the Mike is picked up by the center coming off the double-team."
- Safeties bullet: "the two players nobody blocks: the free safety fills the alley and is the man the tailback must beat."
- Paragraph "Notice that the play is a contest over one defender…": rewrite it around the 9-vs-11 arithmetic. The offense
  can block at most nine of the eleven, so it chooses which two to leave alone. The usual choice is the two farthest from
  the hole, here the safeties. The play works if the tailback beats the first safety. Option football ([03-04]) is the
  trick of reading one of those defenders instead of blocking him. This also sets up box count in 02-05 better than the
  current text does.
- Caption: replace "The one defender nobody blocks is the Mike linebacker, who fills the hole and meets the tailback" with
  "The center comes off the double-team onto the Mike; the two defenders nobody blocks are the safeties, and the free
  safety is the man the tailback has to beat."
- Strip notes: 1.2 s → "F meets W in the hole; C climbs to M". 1.8 s → "unblocked FS fills the alley".

### A2. The lead-run frames are timed wrong: the runner passes his lead blocker, and "F blocks W" never happens (fig-lead-run)
In the +1.2 s and +1.8 s panels the tailback (with the ball) is **ahead of** the fullback. At 1.8 s the F, the ball carrier
and the M are piled into one unreadable clump about 2 yards past the line. The W is still standing about 4 yards deep and
untouched, while the label says "F blocks W". On a lead play the fullback must reach the linebacker first and the
tailback stays on his hip ("press the hole, read the block").

The A1 path changes fix this: FB at 6.5 yd/s, Will attacking downhill. Also move the mesh slightly later (handoff at about
0.7–0.8 s from a 7-yard I-back). Then check that at 1.2 s the FB is engaged with the W at about +1 yd and the RB is about
2 yards behind him, and that at 1.8 s the RB is clear of the clump.

### A3. "The tight end is faster than the linebacker" is contradicted by the chapter's own combine chart
- Tight-end section: "run a 40 in about 4.7 seconds … much faster than the linebacker who might cover him".
- "Why bodies match jobs": "the same tight end covered by a 240-pound linebacker is a mismatch in the other direction
  (the tight end is faster)".

The nflverse combine medians for 2010–2026 are TE 4.72, LB 4.62, ILB 4.76, OLB 4.68. In fig-combine the LB dot sits
**above** (faster than) the TE dot. On average the linebacker is as fast as the tight end or faster.

The real mismatch is skill and size, not speed. The tight end is a trained route runner with receiver hands, his catch
radius is 3 inches taller, and the linebacker is coming from a run fit and has to react. Elite receiving tight ends
(Kelce, Kittle) are the exception who are also faster.

**Fix:**
1. Tight-end section: "…run a 40 in about 4.7 seconds, slower than a receiver but about as fast as the linebackers who
   usually cover him, and he's the better route runner and pass-catcher."
2. Mismatch sentence: "…a mismatch in the other direction (the tight end runs routes and catches like a receiver; the
   linebacker is a run defender trying to cover)."

### A4. Predict the play 2 can't be answered from the picture: the dime back looks like a second linebacker (fig-predict-count)
The sixth DB is moved to `(d=7.5, w=5.8)`. That puts him inside the box, over the attached tight end / right-tackle area,
2.5 yards behind the Mike, which is exactly where a linebacker stands. A reader counting "by where they stand" will
reasonably say 2 linebackers and 5 DBs, and the answer will mark them wrong. (A coach would call that player a "dime
backer". That is a real thing, but it is exactly why it can't be identified by alignment alone.)

**Fix, either one:**
- (a) Make the drill answerable. Flex the tight end into a detached #3 slot (e.g. `Y` at `d=-1.0, w=7.0`; then make
  `Z`/`H` on/off so 7 stay on the line) and put the dime DB **over #3 at about 6 yards** (`d=6.0, w=7.5`), with the NB over
  #2 and the CB over #1. Every DB is then visibly lined up on a receiver.
- (b) Keep the picture but change the answer to acknowledge the ambiguity: "the sixth DB at 7–8 yards over the tight end
  looks like a linebacker; teams call him the dime backer. You'd tell from his size and number on TV, a 200-pounder
  wearing 2x–4x." That's a good lesson too, but then the prompt shouldn't promise "identify them by where they stand".

Also in that answer: "two linebackers have left, almost certainly the Sam and one of the others" is fine. You could add
that the remaining linebacker is usually the best cover linebacker, often the Will or the Mike.

---

## B. Should fix (precision, nuance a coach would insist on)

### B1. Strength isn't always the tight end. Say so once (Mike/Will/Sam section, Madden callout, Watch-for-it)
"The letters come from where they line up *relative to the offense's tight end*" is the classic rule and right for a first
pass. But a coach would add one sentence. Many defenses set their strength **to the field** (the wide side of the
field), **to the passing strength** (the side with more receivers), or to the back. Against a two-by-two formation with no
tight end, the Mike **declares** the strength with a call. The same goes for the strong safety.

Add a terminology-dialect line as well. In 3-4 systems the Sam is often a stand-up edge rusher, the weak-side edge is the
**Jack**/**Rush**/**Predator**, and the second inside linebacker is the **Mo** or **Buck**. Slot defenders are also called
**Star** or **Nickel**, and the dime back is the **Money** or **Dollar**. The chapter already uses `$` for the slot corner,
so one sentence explaining the money/dollar puns would land.

The Madden callout currently says "Many defenses go further and swap names by alignment instead of by player: whoever ends up
on the strength is the Sam this play." Make that sentence more precise: "Some defenses keep the same player at Sam and flip him to
the strength; others play field and boundary instead, so a player stays on the wide side or the short side and his name
changes with the formation."

Watch-for-it bullet "Find the tight end … predict which side the Sam and strong safety line up on" → add "(most teams;
some set to the wide side of the field instead, and spotting which one is a scouting clue)".

### B2. Receiver letters are a dialect. Say so in one sentence (X, Z and the slot)
"(often called H, or F, depending on the team)" undersells it. One sentence would prevent confusion later in the book.
In the Air Raid the slots are **Y** and **H** (Y is a receiver, not a tight end). In West Coast systems **F** is the
fullback and the slot is often **H**. Many teams use **U** for a second tight end. Shanahan- and McVay-style offenses flip
X and Z by formation, so **the letter names a spot, not a person**. That last point also reinforces the chapter's
position-vs-alignment theme.

### B3. The two defensive tackles have different jobs: name the 1-technique and the 3-technique (defensive line)
The DT bullet says their first job is to occupy blockers, "often two at once". That is the nose/1-technique's job. In a
four-man front the other tackle is the **3-technique**, lined up on the guard's outside shoulder. He is the one-gap
penetrator and the interior pass rusher, and he is the most valuable DT in a 4-3. Aaron Donald was a 3-technique, which
is why "small for the position" worked. Fig 1 already shows exactly this split (SDT at w=2.35 is the 3-technique, WDT at
-0.7 is the 1-technique shade).

Add one line with a gloss and a forward link to 03-01/05-01: "In a four-man line the two tackles split the work: one
(the '1-technique', shaded on the center) absorbs double-teams; the other (the '3-technique', on a guard's outside
shoulder) shoots a gap and rushes the passer." Then in the Donald paragraph say "an undersized 3-technique".

### B4. In fig 5 nobody covers the edge outside the tight end after the Sam leaves (fig-eleven-vs-nickel)
After the Sam is removed, the SDE sits at w=4.2, on the inside shade of the attached Y (w=4.8). Nobody is outside the
tight end, the LBs are at -2.0 and +1.8, and both safeties are at 12 yards. A coach would see an unfit D gap: a toss or
outside zone to the tight-end side walks in. Real 4-2-5 fronts against an attached tight end do one of three things:
- align the strong end **outside** the tight end (6- or 9-technique), or
- bump the backers to the strength, or
- roll a safety down.

**Fix:** move the SDE to the tight end's outside shoulder: `q.moved(w=5.5)` for `SDE` in `eleven_vs_nickel`. As an
alternative, slide the Mike to w≈2.8 and the Will to w≈-0.8. This also makes the text's point ("in nickel, the safety or
the slot corner … becomes the seventh man") visible instead of leaving a hole. The same `nickel` default sits under
fig-position-alignment, but there the tight end is flexed, so it's fine.

Note for `gridiron`: `defense("nickel", …)` against an **attached** tight end leaves the strong DE in a 7-technique with
no one outside. That should probably be a 9 when the tight end is attached.

### B5. "Most defenses list a 'linebacker' who plays almost every down as a fifth defensive back" is the wrong way round
The common real cases are the reverse. A **safety** plays linebacker in sub-packages (big nickel, the dime backer or
"money"), and a roster "linebacker" is really an edge rusher (Watt). Rewrite: "Many defenses play a safety at
linebacker on passing downs, list their best edge rusher as a 'linebacker', or use a 'safety' who plays almost every down
near the line…"

### B6. Five defensive backs doesn't always mean a slot cornerback (nickel section, Watch-for-it)
"Count the defensive backs on first-and-10. Four means a base defense; five means a slot cornerback is on the field."
Several defenses now use a third **safety** as the fifth DB ("big nickel"). Kyle Hamilton in the Ravens' film room is
exactly this player. Change to "five means nickel: usually a slot corner, sometimes a third safety (the 'big nickel')".
Then the Hamilton film room ties back to it.

### B7. Small accuracy edits
- Nose tackle: "he's usually the biggest man on **the team**" → "**on the defense**". Offensive linemen are as heavy or
  heavier (the chart puts OL at 313 and DT at 308). The glossary already says "defense".
- Jordan Davis "ran the 40 in 4.78 seconds, faster than the typical quarterback" → "**as fast as** the typical
  quarterback". 4.78 vs a 4.80 median is a 0.02 s difference, inside timing noise.
- Guard pull: "steps back off the line at the snap and runs sideways behind it" → "opens his hips at the snap and runs
  along the line, just behind it". A pull is a lateral open or drop step, not a step back.
- "A coordinator's most basic decision is how many to put near the ball … a balance called **box count**". Box count is
  the number you count, not the decision. Use: "…and how many to keep back; the number near the ball is called the
  **box count**, which A First Look at Defense teaches."
- Long snapper: "and then block a defender charging at him". It's worth one clause that the rules protect him: on
  kicking plays a defender within a yard of the line may not line up head-up on the snapper (he must be outside the
  snapper's shoulder pads). **Verify the current NFL wording (Rule 9-1 / 12-2) before adding.**
- Fig 1 / Predict 1: the text says the strong safety is "often a bit closer to the line", but both safeties sit at
  exactly 12 yards. Optional: set the SS at `d=10.5` in `i_form_vs_43` so the diagram shows the cue the text teaches.
  That also gives Predict 1's "which is the strong safety" question a second clue besides the side.

### B8. Facts to re-check for 2026 (not errors as written, but the context may have moved)
- **Penei Sewell**: the misconception box rests on "the best tackle in football can play on the right". Check whether
  Detroit moved him to left tackle for 2026 after Taylor Decker's departure. If so, add "(he moved to left tackle in
  2026)". The point still holds for 2021–2025. I am not certain of this; it needs verifying.
- **Fred Warner**: the chapter only calls him "the modern ideal", which is fine. If 2025 status is mentioned anywhere,
  check his October 2025 ankle injury.

---

## C. Diagram polish (layout and legibility)

- **fig-combine, bottom panel:** the "RB" and "LB" labels abut and read as one phrase, "RB LB". Change `OFF_B["LB"]` to
  `(-9, -0.13)` or `OFF_B["RB"]` to `(14, 0.05)`.
- **fig-position-alignment:** the "snap 3: in the box" label (at d=2.5, w=5.6) touches the dashed ghost ring at
  (4.2, 4.6). Move it to `(2.4, 6.6)`. Also, the "slot" on that side is the flexed tight end Y (gun_2x2's Y is at w≈9.6 off
  the line), while the previous figure taught "slot = H". Either relabel to "snap 2: over the flexed tight end in the
  slot" or adjust the caption wording.
- **fig-eligible and fig-predict-eligible:** the X / #11 marker at w=-15 sits on the painted yard numbers (the "40" and
  "20" peek out behind the ring). This is cosmetic. Pass `numbers=False` or move X to w=-16.
- **Tag reuse:** "H" is the slot receiver and also the FG holder; "T" is the tailback and also the defensive tackle. The
  colors separate them, but for a first-chapter reader use `"Ho"` for the holder.
- **fig-lead-run:** after A1/A2, re-check the 1.8 s panel. F, RB and M must not overlap, and the "F blocks W" note must
  be true in the frame.
- Everything else checked clean: no labels clipped by the field edge, and the brackets and leaders read correctly in figs
  1, 3, 5, 6, 7, 11, 12 and 13. One animation (the budget is 4), and the strip tells the story in print once the blocking
  is fixed.

---

## D. Film-room suggestions (optional, high value)

- **QB eligibility in the shotgun:** the "Philly Special", Super Bowl LII (Feb 4, 2018, Eagles vs Patriots). Nick Foles
  was not under center, the snap went directly to Corey Clement, and Trey Burton threw to Foles for a touchdown. It is
  the perfect one-line example for rule 3 ("a quarterback in the shotgun is just another back"). Verify the alignment details
  (Foles had stepped up beside the line as if changing the call).
- **Reporting eligible:** the Lions–Cowboys two-point attempt (Dec 30, 2023), where the officials ruled that the tackle who
  caught it had not reported. This is the most famous recent example of the 50–79 rule. It belongs to 02-02, so give at
  most a one-line pointer in the jersey section ("number 70 is reporting as eligible").
- The Juszczyk, Kelce brothers, Watt brothers and Hamilton examples are well chosen and accurately described. The Juszczyk
  "what to notice" (find #44; lead or leak to the flat; who goes with him when he splits out) is exactly how a film
  analyst would cue it.

---

## Verified as correct (no change)
- Eligibility rules (7 on the line, ends and backs, the T-formation QB exception, 50–79 reporting, ineligible downfield
  limit of 1 yard) and the Predict 3 answer (13 covers 87; the shotgun QB is eligible; illegal touching).
- Fig 1 4-3 Over: SDT 3-technique to the strength, WDT 1-technique weak shade, WDE wide 5, Sam outside the tight end at
  4 yards, Mike 10/20, Will 50, corners at 7, safeties at 12 in a two-high shell. The iso weak B-gap is the natural hole
  against this front.
- FG unit: 7 on the line plus 2 wings, holder at about 7 yards, kicker about 2.5 yards back and offset. Punt unit: spread
  punt with 5 interior plus 2 gunners on the line, wings off the line, PP at about 6 yards, punter at about 15. The 6-man
  box, 4 vices and returner are legal and realistic.
- Jersey ranges by era. X on the line and Z off. Strong side named by the tight end (as a first approximation; see B1).
- Fig 2's data and its Shanahan-tree framing.
