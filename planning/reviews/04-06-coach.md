# Coach / film review: 04-06 Run-Pass Options

Reviewed 2026-10-06 against `pdfs/04-06-rpos.pdf` (20 pages, built 16:38 from the current qmd), rasterized at
110 dpi (`_pdfbuild/04-06-rpos/coach/p-*.png`); every figure looked at. NFL rule text checked against the extracted
2026 rulebook (8-3-1, 8-5-1, 8-5-4).

**Verdict:** a strong chapter. The core football is right: conflict-defender logic, run-as-default, box-count
arithmetic, the 1-yard vs 3-yard rule (NFL 8-3-1 has no "crosses the line" clause; that is correct), the glance
two-branch strip, and the defensive-answer menu. Fixes below are ordered by importance. Two are real errors (wrong
guard in the glance hat math; a self-contradiction about throws behind the line), one is a borderline drill that
teaches the wrong call, and the rest are diagram realism and missing coach-level nuance.

## A. Errors in the explanations (must fix)

1. **Wrong guard in the glance hat math (l. 719-720).** "...so the right guard, who would normally have had to climb
   to the Will, is free..." In the chapter's own blocking (inside zone right; LG/LT on the 3-technique, C/RG on the
   1-technique), the backside linebacker (Will) belongs to the **backside combo (LG with LT) off the 3-technique**. The
   RG/C combo climbs to the **Mike**. Rewrite: "so the left guard, who would normally come off the 3-technique to
   the Will, can stay on his double team and the backside combo never has to climb." That matches Drill 3's answer
   (the LG climbing to the Will), which is right.

2. **Self-contradiction about throws behind the line (l. 1165-1167, and fig-rpo-data caption "that the NFL's rules
   favor").** The chapter says correctly (l. 901-902) that the NFL rule "applies to any legal forward pass", and 8-3-1
   confirms it. Then the data section says a throw behind the line lets linemen keep blocking "without risk of the
   five-yard flag". In the NFL that's only true for a **backward pass**: 8-3-1 applies to *forward* passes, so a
   bubble thrown even slightly backward is a lateral and nobody can be "ineligible downfield". The price is that a
   drop is a live ball. A now screen thrown forward to a receiver on the line is still governed by 8-3-1. Suggested
   rewrite: "That shape is the clock at work: the bubbles and now screens come out about half a second after the snap,
   before any lineman can drift a yard, and a bubble thrown backward isn't a forward pass at all, so the rule doesn't
   apply (the price is that a drop is a live ball). A throw beyond the line has to leave so fast that it can't be far
   beyond it." In the caption, change "that the NFL's rules favor" to "that NFL timing favors". (Also flag for 04-05:
   its l. 1114-1116 and `[^ineligible2]` say the NFL 1-yard limit applies only to passes that cross the line, which is
   the *college* rule. The 04-06 factcheck already noted this. 04-05 should be fixed to match 04-06, which is right.)

3. **"Three choices on one snap" (l. 859-867) lets the QB throw after he has started running.** Step 2 reads "Now
   running ... throw the bubble or the slant past him." Add: he must still be **behind the line** when he throws (a
   forward pass from beyond the line is illegal), and in practice the third option is almost always a **bubble or
   flare** (a backward or flat throw). A slant thrown a second and a half after the snap, with the line run-blocking,
   is an ineligible-downfield flag in the NFL. Change "throw the bubble or the slant past him" to "throw the bubble
   to the receiver outside him before crossing the line." The NFL reason it's rarer should then name the rule
   directly: on a forward throw that late, the linemen are past a yard.

4. **Drill 3 teaches a borderline call as "no foul" in college.** The figure puts the LG at d = 3.4. The NCAA rule
   counts **any part of the body** more than 3 yards **beyond the neutral zone**, so a player whose center is 3.4
   yards past the line is a foul or a coin flip, and the answer even admits "barely". A drill should be unambiguous.
   Move LG to about **(2.3, -3.0)** and change the drill text and answer to "about two and a half yards past the
   line": clearly illegal in the NFL (more than 1 yard, contact released) and clearly legal in college (less than 3
   yards).

5. **Wrong formation word in the hook (l. 353-354).** "three receivers *bunched* to the right": a bunch is a specific
   tight cluster. This is spread trips with the TE attached (Y on the line, H at about 10, Z at about 16). Use "three
   receivers to the right".

6. **"Mugging the window" (l. 730) is not standard terminology.** "Mug" means linebackers or safeties walked up into
   the A-gaps before the snap. The technique described (one hard step forward, then drop) is usually called a
   **fake fill**, a **bluff**, or "stab-and-drop"; on the edge it's a **slow-play**. Replace "Coaches call this playing
   *slow* or *mugging the window*" with "Coaches call this a *fake fill* or *bluff* (on the edge, a *slow-play*)".

7. **The Shanahan-tree generalization is contradicted by the chart (l. 1153-1155).** In fig-rpo-data's 2025 panel,
   GB (LaFleur, Shanahan/McVay tree) is about 5th, well above the league rate. SF and LA are the bottom two. Say "the
   49ers and Rams, who run mostly from under center with wide-zone blocking, barely use them, while the Packers, from
   the same coaching tree, are among the leaders: RPO use is a play-caller's choice." Also soften "must come out of a
   shotgun mesh": pistol and under-center RPOs exist; they are just less common.

## B. Diagram fixes (which player, where)

**fig-three-plays (p. 2), RPO panel.** H's quick inside route ends at (3.8, -7.8), right under the nickel at (4.8,
-6.4), and the nickel doesn't move, so it reads as a throw into the defender. Add the red "defender's choice" arrow
used elsewhere: `branch(f, p, [(4.6, -6.3), (2.4, -4.6)], color=RED)` (the $ stepping down to fit), and add "react"
to the legend. Optional: in the option panel, the "keep" path runs straight at the $; that's fine (scrape exchange),
no change.

**fig-bubble-count (p. 4).** Football is right. Only nit: in the left panel the walked-in $ at w = 6.4 sits on the
shaded box edge (box drawn to w = 6.3). Widen the box to w = 6.8 so he is clearly inside the count the label claims.

**fig-glance-rpo strip (p. 5).**
- Linemen block **differently in the two rows**. Throw row: the RG "holds the combo: no climbing". Give row: the RG
  climbs to the Mike from t = 0.4 s, before the 0.75 s handoff. Linemen can't see the mesh, so on a real RPO the
  five block identically on both branches. Make the give row's RG hold the combo until after 0.75 s (delay ≥ 0.8),
  or keep both rows the same through frame 2. The caption sentence "In both rows no lineman is more than a yard past
  the line when the decision is made" then becomes the teaching point.
- The code comment "LCB bails to his deep third" is wrong for a two-high shell. With a two-high shell, the backside
  corner plays quarters or squats. A comment only, but the CB's bail to 13 deep is fine as "quarters, carrying #1."
- Caption: "Simulated in Big Data Bowl coordinates" should be "simulated, BDB-format" (house label).
- Timing is good: throw at 0.85 s, catch at about 11 yards by 1.9 s is realistic NFL glance timing.

**fig-slant-rpo (p. 7).**
- The "walls the slant: hand off" arrow goes deep and outside (from (5.9, -10.3) to (7.4, -12.0)). Walling the slant
  is **lateral, at depth or slightly under**: make it about (5.4, -10.0) to (5.6, -12.4) so it doesn't read as a
  bail.
- The prose (l. 772-775) gives the reason the safety is there as "because the offense's formation put three receivers
  on the other side". Three receivers pull defenders *toward* them. The real reason is a **weak rotation**: the
  defense rotates the weak safety down (Cover 3 "weak"/Cover 1 robber look) to stay plus-one against the run to the
  single-receiver side, accepting a 3-on-3 to trips with the FS over the top. Say that.

**fig-stick-pop (p. 8).**
- The stick text (l. 791-793) says "and another to the flat", but the diagram has no flat route (Y run-blocks, Z
  runs a clear-out). Add one clause: "as an RPO the flat is usually dropped: the run is the flat's job, and #1
  clears."
- Pop pass: the $ at (5.0, 7.4) is only about 4 yards from Y's catch point and stands still. Give him a path widening
  with H's vertical, e.g. `go_to(p, "NB", (6.5, 10.0), "path")`, so the window behind the Mike is honest.

**fig-ineligible (p. 9).**
- NFL panel: the LT is at d = 1.5 and his man (5) at 3.2, a 1.7-yard gap, so he isn't "still blocking", and the
  caption says "two yards". Put **LT at (2.0, -3.9) and BE at (2.8, -3.9)**. Likewise, the interior linemen at d = 0.3
  face DTs at 1.9 and look unengaged. Put the BT, PT and PE at about d = 1.1 so the "holding first blocks" claim is
  visible.
- College panel: the LG and RG have released past the 3 and the 1, and **nobody blocks either DT** (the C at 0.25 is
  between them). That's a free tackler on the run and isn't how a college RPO is blocked. Keep the combo partners on
  the DTs: **LT on the 3 at about (0.9, -2.4), C on the 1 at about (0.9, 0.4)**. Leave the backside 5 unblocked (or
  read), and RT on the 7. Then the guards' release reads as "combo, then climb within 3 yards."
- Marker collisions: the LG circle overlaps the W box and the RG circle overlaps the M box (college panel). Pull both
  guards to d ≈ 2.3 (also safer under the any-part-of-the-body rule) or push the LBs to d ≈ 5.3.

**fig-rpo-answer (p. 14).** Good, and the right answer to show. One realism note: the FS comes from (13, -0.5) into
the backside B-gap by (3.4, -1.4) at the snap. Fine, but the overhang SS "widens at the snap" to (5.8, -11.0), which
is more a bail than a wall. Make it about (5.4, -11.0). Label "SS walls the slant" is clear of the field edge, so no
clipping issue.

**fig-drill-2 (p. 17).** "Frozen at the mesh" but every marker is drawn at its pre-snap spot with motion arrows; R is
still 1.6 yards from Q. Either move R to the mesh spot ((-4.8, -0.5)) and SS to its 0.6 s spot, or reword the
caption: "drawn at the snap; arrows show where each player has gone by 0.6 s."

**fig-drill-3 (p. 18).** Besides the LG depth (A4): RT is at (1.8, 4.0) and his 7-technique at (3.9, 4.2), so there's
2 yards of air between them. Make the PE about (2.6, 4.2). The "LG: 3 yards past" leader crosses the throw arrow and
the 5. Put the label at about (-2.6, -6.0) or on the right side.

**Labels and edges:** no on-field label is clipped by the window edge in any figure, and there are no text-on-text
collisions apart from the marker overlaps above. Footnotes are each referenced once.

## C. Nuance a coach would insist on (add; short)

1. **The defense's best tell is the uncovered lineman (How defenses answer).** This is the most important missing
   answer, and it ties straight to the 1-yard rule. NFL linebackers on RPO teams are taught to **key the uncovered
   guard**. If he climbs hard to the second level, it's a true run, because he can't legally do that on a pass. If he
   sits at the line, catch-blocks, or "hat-on-hat" blocks without climbing, it's an RPO: the linebacker plays his pass
   job. Add as a bullet: "Read the line, not the back." It also explains why offenses answer with true runs that climb.

2. **On-field tells for Watch for it.**
   - **Where the QB's eyes go.** On a zone read his eyes are on a defensive *lineman* at the line. On a post-snap RPO
     they are at the *second level* or out over a slot.
   - **The backside receiver.** On a pure run he jogs or stalk-blocks; on an RPO he runs a full-speed slant or glance.
   - **The line.** Linemen who stay on the line rather than climbing.

3. **Terminology dialects (one short "Go deeper" or a sentence).**
   - Pre-snap RPOs are also called **alerts**, **tags** or "check-with-me" plays.
   - The glance is also a **bang-8**, **bend** or skinny post.
   - Quick screens are now, smoke and bubble (04-03 has these).
   - Technique numbers vary: the chapter's "7 on the TE's inside shoulder" is the Bryant/Bear numbering, and many
     staffs call that alignment a **6i**. Worth half a sentence in "How to read the diagrams".

4. **Other RPO runs.** The chapter only pairs RPOs with inside zone. Mention that **duo, split zone and counter or
   power** carry RPO tags too (gap schemes with pullers are rarer because pullers drift), so readers aren't surprised
   on Sunday.

5. **8-3-1 Item 1(b).** After breaking contact more than a yard downfield, a lineman may **stay put, move laterally or
   back off** until the throw. This is legal and taught ("freeze"). One clause in the exception bullet.

6. **"The NFL's favorite version" (l. 652).** Unsupported as a superlative. Use "one of the NFL's most common
   versions". Bubble, now, slant and stick RPOs are at least as common.

7. **Table nit.** The option row "Who chooses: The read key's first step" conflicts with the RPO row ("the
   quarterback"). Use "The quarterback, from the read key's first step, after the snap."

## D. Film room and history

- **Eagles 2017 and Chiefs film rooms** are accurately characterized and well chosen. No invented plays, which is
  right.
  - **Optional (verify first):** the 2017 Eagles leaned heavily on Zach Ertz in the RPO game (the pop/seam and stick
    family). Naming him under "what to notice" would make the TE section concrete.
- **Spec gap:** the spec lists **Oregon / Auburn / Baylor** roots; only Baylor appears. Add one sentence each:
  - **Chip Kelly's Oregon**: packaged zone-read plays.
  - **Gus Malzahn's Auburn** (2010, Cam Newton): the inside-zone read with the **pop pass** to an H-back is the
    canonical college pop.
- **Missing direct link: Chip Kelly's 2013 Eagles with Foles.** It is the obvious bridge. The `[^foles]` ESPN source
  is literally titled "Eagles pull from Chip Kelly playbook to awaken 2013 Nick Foles". One sentence in the 2017 film
  room ("the coaches went back to the packaged plays Foles had run under Chip Kelly in 2013") uses a source already
  cited.
- **Hurts 2022:** fine. "A give, a keep and a throw" is accurate for that offense.

## E. gridiron use

Sensible. The chapter builds its own hand-placed `trips()` and `nickel()` (clean, legal: `check_legal` asserts 7 on
the line with X and Y as the ends) and its own frame-strip/video helpers. One animation, so it is within budget. The
frame strip tells the story in print. No library changes needed. The BDB eval-false cell is correct in shape
(`pff_runPassOption`, `pass_forward`).
