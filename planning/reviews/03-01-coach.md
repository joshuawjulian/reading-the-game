# 03-01 The Language of the Run Game: coach / film-analyst review

Reviewer role: veteran NFL coach and film analyst. Scope: football correctness, every diagram (rasterized
`pdfs/03-01-run-game-language.pdf` at 90 dpi, block plate re-rendered at 200 dpi; all 14 figures looked at), the combo
frame strip, missing nuance, film room, gridiron use. I did not edit the chapter.

**Overall:** strong chapter. The vocabulary is right, the "why it exists / what it costs" framing per block is exactly how a
line coach teaches it, hat math and the QB-as-the-missing-man section are excellent, and the history/film rooms are well
chosen. The problems are concentrated in a handful of diagrams that draw a scheme a coach would not run (a static
covered/uncovered count applied to a zone run, a covered center abandoning his man, a lead play aimed at an unblocked
3-technique) plus a few text claims that are too absolute (the "one question" zone/gap test, the RB's first step, the 4i
rationale, the center "helping a guard" against two 3-techniques).

Priority: **P1** = misleading football, fix before publishing; **P2** = a coach would object; **P3** = polish.

---

## P1: must fix

### 1. Drill 3 answer contradicts the chapter's own zone rule and has the center doing something impossible (l. 1359-1371; fig-drill-3)
The answer counts covered/uncovered statically, then says "the center ... can help the left guard on the other
3-technique and then climb to the Will." A left 3-technique sits on the LG's *outside* shoulder (the left B gap), two gaps
from the center; the center cannot double him. Worse, the chapter told the reader one section earlier (l. 686-689), and
03-02 teaches as Rule 2, that zone teams count "covered" only on the play side. On an inside run right, the left 3 is on
the LG's backside shoulder, so the LG is *uncovered* by the zone rule and the left 3 belongs to the LT's play-side gap.
**Fix (answer text):** keep "5, 3, 3, 9" and the static covered list (LT, LG, RG, Y; uncovered C, RT). Then:
"Count the hats: six blockers (five linemen and the Y) against six defenders. Natural assignments: Y on the 9; RG and RT
double the right 3, and the RT climbs to the Mike; the center, with nobody on him and nothing in his play-side A gap,
climbs straight to the Will; the LG takes the left 3 and the LT the 5 (or, by zone rules, the LG and LT work together on the
left 3 and the backside end is left alone; 03-02)." Rewrite the last paragraph to: "by putting both tackles in 3-techniques
the defense left the center uncovered, so he is the free hat who goes straight to a linebacker."
**Fix (diagram):** the RB is offset to the QB's *right* (`O("RB", "RB", -5.0, 1.5, "R")`) for an inside run *right*. From
the gun, an inside-zone back aligns opposite the play side so the mesh carries him across (as fig-qb-short already does).
Use `w=-1.5`.

### 2. The Kelce paragraph repeats the same error (l. 910-915)
"When a four-man front puts both defensive tackles in 3-techniques ... nobody covers the center, so he is the free hat
who helps a guard and then climbs." Against a 3-technique the double-team partner is the *tackle* (a guard-tackle combo,
"deuce" in many systems); the center combos with a guard when the defender is a 1 or 2i (the "ace" combo, as in the strip).
**Fix:** "When a four-man front puts both defensive tackles in 3-techniques (a common nickel look), nobody covers the
center, so he is the free hat: he climbs straight to a linebacker, or helps a guard when a tackle slants into the A gap.
Against a 1-technique or a 2i, he is the one who doubles with a guard and comes off to the linebacker." The film-room
sentence about Kelce's guards finishing the man he left (l. 1215) is correct and fits that ace combo.

### 3. Hat-math figure: the covered center leaves his 1-technique, and the RT climbs *through* the 3 (fig-hat-math, `hat_blocks`, l. 950-955)
The center is covered by the 1 (shaded on his left shoulder), but he climbs to the Will while the LG folds down on the 1.
That is a real "fold" scheme, but it is exotic for the picture whose only job is "a hat on every hat," and it breaks the
chapter's own rule (covered linemen block their man first). The RT's climb `via=[(-0.2, 3.0)]` to `(3.7, 1.8)` crosses
straight through the 3-technique's box at about (1.0, 2.6).
**Fix:** `go_to(p, "C", (0.35, -0.55), via=[(-0.3, -0.3)])` (C on the 1); `go_to(p, "LG", (3.7, -2.0), via=[(0.3, -1.7)])`
(LG climbs to the Will); for the RT, route him outside the 3 and then inside: `via=[(0.4, 3.3), (2.4, 2.9)]` to
`(3.7, 2.1)`. Same assignments in both panels.

### 4. "QB short" left panel: a no-read handoff that leaves the backside end free is a strawman (fig-qb-short, l. 1019-1057)
No offense that is *not* reading the end leaves him unblocked: nothing stops him chasing from behind. They block him (LT
cut-off) and accept a free linebacker or the box safety instead. The point of the figure is that the free man is in the box
either way until the QB reads someone, and the cleanest way to show it is to move the LT's block.
**Fix:** left panel: `go_to(p, "LT", (0.4, -3.1), via=[(-0.2, -3.5)])` (LT on the 5); leave the Will unblocked and ring him;
send him over the top to the hole: `go_to(p, "WILL", (2.6, 1.4), "path", speed=4.0)`; label "unblocked: the Will". Right
panel stays as is (LT climbs to the Will *because* the QB reads the 5). Caption: "Left: the quarterback hands off and
watches. Six blockers take six of the seven box defenders; the Will (ringed) is free and runs to the ball. Right: the QB
reads the backside end, so the LT can climb to the Will: every man in the box is now accounted for."

### 5. Point-of-attack figure: an iso into the B gap with the 3-technique standing in it, unblocked (fig-point-of-attack, l. 468-486)
The green X sits on the 3-technique's helmet and no lineman blocks anyone, so the picture says "run the fullback and back
straight into the defensive tackle." A lead play hits the "bubble," where a linebacker is stacked over an uncovered lineman.
**Fix (simplest):** move the point of attack to the right A gap (the 1 is shaded to the *left*, so the right A gap is the
bubble under the Mike): `spot(fld, p, 0.0, 0.8, ...)`, FB `go_to(p, "FB", (3.6, 1.1), via=[(-1.2, 0.9), (1.4, 0.9)])`,
RB `via=[(-3.6, 0.5), (-0.5, 0.9)]` to `(3.0, 1.4)`, and draw the two blocks that make the hole: C back on the 1
(`go_to(p, "C", (0.35, -0.5), via=[(-0.3, -0.25)])`) and RG drive the 3 out (`go_to(p, "RG", (0.4, 2.2))`). Caption
and text: "the right A gap". If you want to keep the B gap, flip the front to a 1 on the right and a 3 on the left.

---

## P2: a coach would object

### 6. Block library plate: three panels draw the path through the wrong player (fig-block-library)
- **3. Reach:** the G's path `via=[(-0.1, 2.85)]` steps laterally almost onto the T's spot, so at print size the block line
  appears to come *from the T*. Draw the reach as the classic bucket/crossover: `go_to(p, "RG", (1.15, 2.95), via=[(0.2, 2.15)])`
  and drop the T from the panel (`w0=-2.4` so only C and G show), or keep the T and give him his own first step outside.
- **6. Pull:** the turn-up leg from `(-1.9, 4.4)` to `(0.9, 5.8)` clips the T's marker. Turn up wider: `(-1.9, 4.9)`, `(0.9, 5.9)`.
  The pull depth of 1.9 yards is also deep; guards pull at the heels of the line, about 1 to 1.5 yards (see also item 9).
- **7. Kick-out and 8. Lead:** both the F's and the R's lines run over the T (kick-out) and the R's path runs through the F's
  marker (lead: R `via=(-4.0, 0.7)` passes 0.6 yd from F at (-4.5, 0)). Start R `via=[(-5.6, 0.9), (-2.4, 2.2)]` in the
  lead panel; in the kick-out panel route F `via=[(-2.0, 3.6)]` and R `via=[(-4.0, 1.6), (-1.4, 3.9)]` so both pass
  *outside* the T's marker into the space he vacated.

### 7. "Does the whole line step the same way, or does somebody pull?" is too absolute (l. 1159-1161, Watch for it l. 1249-1250, Takeaways)
**Duo** (03-03) is a gap/man run with no puller, built to look like inside zone; trap and counter variants, and zone's
pin-and-pull, cross the other way. Add one sentence: "The big exception is *duo*, a gap-family run with no puller that is
built to look like inside zone ([03-03](03-03-gap-and-power-runs.qmd)); for that one, look for double teams aimed straight
at the linebackers rather than a line moving sideways together."

### 8. "The RB's first step points at the play side" (Watch for it, l. 1247-1248)
On **counter** the back's first step is deliberately the wrong way (the counter or "false" step), and on split zone and
some RPO looks the first step is also a mesh step. Add: "except on counter plays, where the back's first step is a
deliberate lie (03-03)." The prediction-log line ("whether this offense's first step tells the truth") then becomes a
real, nice payoff.

### 9. Pull paths drawn 3 yards deep (fig-zone-vs-gap gap panel l. 1130; fig-drill-1 l. 1284)
`via=[(-3.05, -1.1), ...]` puts the puller behind the QB and across the fullback's path; the gap-panel pull then turns up
through the RT's marker. Real guards pull flat, about 1 to 1.5 yards off the ball, and the QB opens out of his way. Use
`via=[(-1.6, -1.1), (-1.6, 2.6), (0.3, 3.4)]` and, if the Q marker is in the way, give the QB his open-and-hand path
(`go_to(p, "QB", (-2.6, -0.8), "path")`).
In the same gap panel, the "fixed hole: the C gap" leader points at the FB's kick-out (on the 5's box). Point it at the
hole itself, between the RT's down block and the kick-out: target `(0.3, 3.25)`.

### 10. Drill 1 vs 03-03: the RG leaves for the Will at once (l. 1281)
03-03's power figure has the RG and RT double the 3 before the RG climbs; here the RG's line goes straight to the Will
across the 1, while all other players show only a first step ("the first half-second"). Show the RG stepping to the 3
with the RT (`go_to(p, "RG", (0.4, 2.0))`) and mention the double in the answer. Keeps the two chapters consistent and
the drill honest to its caption.

### 11. The 4i rationale is muddled (l. 605-607)
"...makes the offense's favorite double team, guard and tackle together, awkward to set up." A 4i is the defender a guard
and tackle *can* double most easily (he sits between them). What the tite front's 4is actually do: squeeze the B gaps, sit
inside the tackle so the tackle cannot reach or cut him off cleanly, and, with a 0 on the center, leave each guard
uncovered with a linebacker over him who is hard to climb to because the 4i can play through either blocker. Suggested
wording: "...in the B gap. It squeezes that gap from the inside, it is hard for the tackle to reach, and because it can play
off either the guard or the tackle, it muddles which of them doubles and which climbs."

### 12. The technique chart caption over-states the width (l. 515)
"crammed into the 15 or so yards between the tight ends": tight end to tight end is about 9 to 10 yards (gridiron draws
±4.8). Say "the 10 or so yards between the tight ends." Related nuance worth one sentence after the table: with real
splits, a 3 and a 4i stand about a foot apart (gridiron puts them 0.25 yd apart). The difference is *whose shoulder* he
is on, which is why the covered/uncovered figure ties each defender to a lineman.

### 13. Combo strip: players vanish, and the strip has no pre-snap frame (fig-combo-animation, l. 898-901)
- With `lateral=(-3.4, 4.4)`, the RT is drawn in frame 1 but disappears in frames 2-3 (he blocks out to w=3.9, filtered by
  the "whole marker" rule), and the right 5-technique he blocks is never drawn. A reader thinks the RT left the play.
  Widen to `lateral=(-4.2, 5.4)` (keep labels 1.5 yd inside).
- The left 3-technique's box is drawn on top of the LG in frames 2-3 (`L3` ends at (0.6, -2.0), LG at (0.3, -2.1)). Offset
  engaged pairs by about a yard: `L3` to `(1.2, -2.0)`.
- Add a snap frame: `times=[0.0, 0.4, 0.85, 1.35]` with "1 shaded on the C; Mike stacked behind; RG uncovered" so the
  reader sees *why* C and RG are the pair. Use `ncols=4`.
- R and Q overlap in frame 2 (handoff at 0.6). Moving the QB's path to `(-2.6, -0.6)` (opening away) separates them.
- The unblocked Will arrives in the hole in frame 3. Say so in the caption ("the Will is the free hat in this
  seven-man box; see the next section"): it turns a loose end into a bridge to hat math.

### 14. Missing vocabulary a line coach would insist on (glossary aliases or one-line glosses)
- **Base block** as an alias of drive block. NFL coaches and broadcasters say "base" more than "drive."
- **Scoop** for the backside zone cut-off (often a two-man guard-tackle scoop). The reader will hear it on broadcasts and in 03-02.
- Combo names by pair: **ace** (C-G), **deuce** (G-T), **trey/tray** (T-TE), dialects vary. One sentence in the combo paragraph.
- **Bubble**: an uncovered lineman with a linebacker stacked over him, where lead and iso plays aim. It pairs with item 5.
- **End man on the line of scrimmage (EMLOS)**: the kick-out paragraph says "the end man"; gloss it and forward-link to
  03-04, which owns the term.
- **Mike ID**: the center's pre-snap call that sets the count for every blocker ("54 is the Mike"). The chapter opens on
  the center telling four linemen who blocks whom; one gloss plus a forward link to 04-02 (which owns it) completes that thought.
- **Hinge** appears in code comments and 03-03 but never in this text; fine to leave to 03-03.

### 15. Madden callout is out of date (l. 457-462)
Current Madden run menus are largely named by scheme ("Inside Zone," "Outside Zone," "Power O," "Counter," "Duo"), and I
can't confirm "a lane lights up." Reframe the contrast around the *pre-drawn path*: "Madden's play art draws the back's path
to one spot, and the game rewards hitting it. In real zone runs the hole on half the plays is decided after the snap..."
Drop "a lane lights up" unless verified.

---

## P3: polish

16. **Label margins (rule c).** Drill 3: "inside run to the right" sits at d=7.1 in a window ending at 7.0 (it renders
    outside the field, against the title); widen to `window=(-6.6, 8.6)` or put the arrow at d=6.0 with the text below
    it. Hat math: "the two free men are 12+ yards away" at d=14.2 in a 15.0 window; use 13.4 or widen. fig-qb-short: "Q hands
    off, watches"/"Q reads the end" at d=-6.9 in a -7.8 window; use -6.2. Point-of-attack: "PLAY SIDE/BACKSIDE" at 6.3 in a 7.5 window (1.2).
17. **fig-point-of-attack** leader from "point of attack" to the X crosses between RT and Y markers; anchor the text at `(-2.8, 7.4)`.
18. **fig-hat-math:** X, Z and both corners are off-picture at ±15. Add a small edge note on each side, "X and CB ->" /
    "<- Z and CB", inside the window (w = ±9), so the reader can see the receivers that "take defenders away."
    The caption's "the two defenders nobody blocks are the safeties" should be "nobody blocks *or covers*" (the corners
    and nickel are occupied by receivers).
19. **"Line coaches say the double team 'creates the movement and the climb creates the hole'"** (l. 907): reads as a
    quote with no source. Drop the quotation marks or paraphrase.
20. **"older than the gap letters"** (l. 413): unsourced priority claim; soften to "a separate system".
21. **Ravens 2019 "read-option-heavy"** (l. 1071): Roman's offense was as much gap/QB-run (power read, QB power, counter)
    as zone read. "an option-heavy offense built around Lamar Jackson" is safer.
22. **Drill 2:** the first-down line at d=1.0 runs right through the defensive linemen's boxes. Either nudge the DL to
    d=1.2 for this figure or set `to_go=2` (and say second-and-2). Also worth a clause in the answer: on 2nd-and-1 most
    defenses would *not* sit in two-high base; that's why it is such a good look to run into.
23. **Fig 6 (covered)**: with the tite edge moved 0.5 wide, the "LT covered twice over" is true but looks odd; the caption
    could say why: "the 5 and the 4i bracket the left tackle."
24. **Film room, Eagles 2022:** AUTHORING asks for a game where possible. Two good, checkable choices (verify before
    using): the 2022 Divisional round vs the Giants (Jan 21, 2023; a big rushing day) or the NFC Championship vs the
    49ers (Jan 29, 2023; four rushing TDs). Either gives the reader a specific broadcast to pull up for "watch Kelce."
25. **Hook:** the analyst's play has the *tackle* climbing to the Mike off a guard-tackle double; 03-03's power figure has
    the *guard* climb. Both happen, but match 03-03 ("the guard climbs to the backside linebacker") or drop the climber
    name, so the reader doesn't meet two versions.

---

## What is right (keep)
- Gap letters, D gap only with a TE, gaps move with the players (excellent misconception box), splits widen gaps.
- Technique numbering, TE dialects (6/7 swap, 8 with two TEs, wide 9), shade = gap responsibility, two-gap preview, Phillips origin.
- Covered/uncovered plus the play-side refinement for zone (just make Drill 3 obey it).
- Each block's "why / cost"; the angle-block callout; play side vs strong side.
- Hat math, two-high vs one-high, "the scheme only chooses *which* defender is free," the 10-v-11 handoff argument and the
  Harbaugh/Holtz quote, the pass threat as a hat, QB run = RB becomes a blocker.
- Super Bowl XVII 70 Chip is a perfect hat-math film room; the Gibbs counter trey / H-back history is accurate and well used.
- The box-count data box and its selection-bias explanation are exactly right.
- One animation, BDB eval:false cell present and labelled; gridiron used sensibly (technique(), to_tracking()).

## gridiron notes (not edited)
- `technique("3")` = 2.35 and `technique("4i")` = 2.6: correct in spirit (a foot apart), but at print size the two are
  indistinguishable; chapters that contrast them need tie lines or labels, as 03-01 does.
- The chapter's `panel()` filters out any player whose marker is not wholly inside the window, which makes engaged players
  vanish between frames (item 13). A "clip but keep" option in a shared helper would avoid this book-wide.
