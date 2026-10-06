# 05-01 Defensive Line Play: coach / film-analyst review

Reviewer role: veteran NFL coach and film analyst. Scope: football correctness, every diagram (built with
`build_pdfs.py 05-01-dl-techniques-and-gap-control`, rasterized at 80 and 130-150 dpi; all 11 figures and both frame
strips looked at), the strips' timing, missing nuance, film rooms, gridiron use. I did not edit the chapter.
Facts and dates are the fact-checker's job (05-01-factcheck.md); I did not re-litigate them.

**Overall:** a strong chapter, close to pilot quality. The three-jobs framing, "alignment is a job description",
the one-gap/two-gap trade, read-the-head, squeeze vs spill, and the hard/soft edge are all taught the way a D-line
coach teaches them. The film rooms (Sapp in XXXVII, Wilfork, Donald's two snaps in LVI, the 2011 Eagles) are well
chosen and fairly characterized. The problems: **Drill 2's answer contradicts its own diagram**, the **slant/angle
figure can't show the difference it teaches**, the text **overclaims "unblocked" two-gap linebackers** while its own
strip shows the guards climbing to them, the double-team **post/drive terminology is backward**, and several diagram
details (an RT blocking air, a runner running through his own tight end, guard/LB marker overlaps, Drill 3's
"empty" backfield that isn't).

Priority: **P1** = misleading football, fix before publishing; **P2** = a coach would object; **P3** = polish.

---

## P1: must fix

### 1. Drill 2 answer contradicts fig-drill-2 (l. 1293-1305; diagram l. 1270-1290)
The diagram's slant moves each lineman one gap right: the 5 (left C) to the **left B** (`LE` ends w=-2.45), the 1
(left A) to the **right A** (w=0.85), the 3 (right B) to the **right C** (w=4.0), the 9 widens. So the gaps the slant
*empties* are the **right B, the left A and the left C**. The answer says the gaps the back aims at, "the right A and
B, now have defenders arriving in them", and that the cutback goes to "the gaps the slant just emptied, the left A
and B". The right B is empty (the 3 left it) and the left B is now filled (by the 5).
**Fix (answer text):** "The slant ran the same way as the play. Inside zone's blockers are happy about that at first:
each one simply rides the man who slanted into his area (the RG takes the 1 who came into the right A, the RT the 3
who went to the right C). But look at what moved: the 3 left the right B, the gap the back is aiming at, and the 1
left the left A. Replacing them is the linebackers' job. The Sam has to get into the right B the 3 vacated; if he does,
the back bends back to the left A, which belongs to the Mike, and the Will has the backside C the 5 left. **The
defender who has to be right is the linebacker replacing the vacated gap the back is reading, first the Sam (front
B), then the Mike (cutback A).** If either flows with the line instead of filling behind it, the back is through
the line untouched." (Alternative: keep the "Will on the cutback" answer and change the drawing so the 5 slants into
the left B *and* the Will's gap is named as left A; but then the right-B problem remains. The text fix is cleaner.)
Also say in the question "the linebackers have not moved yet" (already in the caption) so the reader knows the
replacement is the point.
Minor: QB under center on inside zone right opens to the play side; `go_to(p, "QB", (-3.4, -0.4))` steps him *left*.
Use `(-3.2, 0.5)`.

### 2. Slant vs angle figure doesn't show the difference it teaches (fig-slant-angle, l. 1040-1075)
Because the linemen are drawn at d=3.2 (`moved(d=2.2)`) and every arrow ends at d=0.85, the slant arrows (e.g. the 3:
1.5 yd lateral, 2.35 yd vertical) are *steeper* than the angle arrow (1.4 lateral, 2.75 vertical). The print reader sees
four 45-degree arrows on the left and one 45-degree arrow on the right; "flat" vs "45 degrees and upfield" is invisible.
**Fix:** draw the slant flat and the angle penetrating. Keep linemen at real depth (drop the `moved(d=2.2)` or use
`d=1.6`), end slant arrows at about the defender's own depth minus 0.5 (`(q.d - 0.5, next_gap_w)`, i.e. nearly
lateral), and end the angle at `(-0.6, 0.95)` (past the line into the A gap). Move the "45°, still upfield" label next
to the 3's arrow, e.g. `say(f, p, 1.6, 3.9, ...)`; at (3.6, 4.4) it sits between the M and the S and reads as a
note about the 9. The LB "replacement" arrows on the left look solid at print size although the caption says dashed;
use a coarser dash `(0, (2, 2))` or lw 1.0.
Text, l. 1083-1090: the definition says a slant is "hard and flat", then the parenthetical says clinics agree "the
first step is a roughly 45-degree step with the back foot", which is the chapter's definition of an *angle*. Say:
"Mechanics vary by staff: many teach the slant with a flat 'directional' step with the near foot, then a cross-over
step that gains a little ground; nearly all warn that a step with no upfield gain lets the blocker push the slanter
along the line." (Keep the source; it supports the 'don't go purely sideways' point.)

### 3. "Unblocked" inside linebackers in the two-gap 3-4 (l. 785-789, fig-gap-accounting label l. 631, Drill 1 answer l. 1255)
"The two inside linebackers ... run to the ball, unblocked, because the big men in front of them are occupying all
five offensive linemen." Against a 0 and two head-up 4s, the **guards are uncovered** and climb to the ILBs, exactly as
the chapter's own fig-two-gap-nose shows (and its caption says). Three linemen cannot occupy five blockers by
alignment; the nose does it by *forcing* a guard to stay and help on him. A coach will say the classic 3-4 ILBs were
big, block-shedding thumpers precisely because guards came up to them.
**Fix (l. 785-789):** "...the two inside linebackers have no gap to *rush to* at the snap. They read the play and fill
wherever the ball goes, and the two-gappers' job is to make that possible: a nose who can't be moved by the center
alone forces a guard to stay and help him, so at most one blocker gets up to the linebackers, and the 4s keep the
tackles from climbing at all. That is the two-gapper's real product: not tackles, but *clean linebackers*."
Label l. 631: "M and W: read, then fill" (not "free to chase"). Caption l. 616: "so both inside linebackers can read and
flow to the ball" instead of "are free to run". Drill 1 answer l. 1254-1256: "...and can run to the ball, as long as the
nose makes a guard stay to help him and the ends keep the tackles on the line."
Consider adding in the two-gap strip caption: "In a real game the offense would usually double the nose with a guard
(the ace combo from 03-01); here the guards climb, to show that the nose alone can hold both A gaps against the center."

### 4. Double-team terminology is backward (l. 936-939 vs caption l. 832)
"fights the pressure of the blocker who is driving him (usually the one head-on)". In the standard **post-drive**
(also "post-lead") double team, the **post** man is the one head-on who stops penetration, and the **drive** (lead) man
hits from the side and does the moving. The coaching point is exactly to fight the *drive* man's side pressure (drop
the hip/shoulder into him, turn the shoulders slightly, don't get turned), while holding the post man. The figure
caption says "fights the pressure of the drive man", which is right; the text then mislabels him.
**Fix:** "He widens his base, sinks his hips and fights the pressure of the blocker coming from the side (coaches
call him the *drive* man; the one in front is the *post*): he drops the hip nearest him and leans into him so the pair
can't turn him." Also l. 947-949, "the double team has moved nobody, because there is nobody left to move" is
confusing. Say: "If he doesn't get through, he has turned his shoulders and left his gap, and the double team walks him
out of it."

### 5. One-gap strip: the RT blocks air and the back's track isn't outside zone (fig-one-gap-penetration, l. 650-668)
- `go_to(p, "RT", (-0.3, 4.7))` sends the right tackle outward onto the tight end's spot (at +0.3 s his marker sits on
  top of the Y's, and the 3's diamond covers the RG and RT: a three-way collision in frame 2). With a 3 on the RG and a
  9 outside the Y, the RT is uncovered play side; on outside zone he either combos with the RG on the 3 ("deuce") or
  climbs to the play-side backer. Have him step play side and climb, late like the guard:
  `go_to(p, "RT", (0.2, 3.9), speed=2.2)` then `go_to(p, "RT", (2.2, 3.6), speed=2.6)` (toward the Mike). The 3 then
  beats *two* late blockers, which is the stronger lesson, and the strip stops overlapping.
- The back's path (`via=[(-6.0, 1.0)]` to `(-4.1, 2.3)`) climbs at about 35 degrees off vertical: an inside-zone
  track. The caption says he "wanted to run outside the tight end". Outside zone from 7 yards is flatter: use
  `via=[(-6.6, 1.6)]` to `(-5.2, 4.0)`, and move the 3's second leg and the X to about `(-4.6, 3.5)`. That also makes
  the X "4-5 yards deep", so update note 4 and the caption ("in the back's path, four yards deep").
- Frame 2: delay the 3's arrival on the RG by 0.1 s or move his via to `(0.45, 3.3)` so the diamond sits on the guard's
  outside hip instead of on his body.

### 6. Set-the-edge panel: the runner runs through his own tight end (fig-edge-contain left, l. 976)
The solid "edge set" path `via=[..., (-2.8, 5.6), (-1.5, 5.4)]` to `(2.1, 4.5)` turns up straight through the Y's
marker (Y at w=4.8 is blocking the B). Turn him up in the C gap inside the Y: `via=[(-5.0, 2.4), (-3.0, 4.3),
(-1.6, 4.0)]` to `(2.2, 3.7)`, and keep the dashed "hooked" branch leaving from `(-3.0, 4.3)`. With nobody else on
the line blocking, also give the RT a block on the 3 (`go_to(p, "RT", (0.5, 2.9))`) so the lane he turns into is not
created by a 3-technique standing still.

---

## P2: a coach would object

### 7. Two-gap strip: guards land on top of the linebackers (fig-two-gap-nose frames 3-4, l. 749-750)
Guards end at `(3.0, ±2.0)`, linebackers at `(3.95, ±1.9)`: the LG circle covers the M and the RG covers the W in both
ending frames, so the reader can't see who is who. End the guards at `(2.9, ±2.5)` (on the backers' outside half,
as a climbing guard would aim) and the backers at `(3.9, ±1.6)` (stepping downhill to fill inside). QB depth -3.5 is
neither under center nor gun; use -1.2 (under center, matching the other run figures) or -4.0 (pistol).

### 8. The 3-technique's "one-on-one" is overstated (l. 488-493)
"if the tackle comes inside to double him, the tackle has abandoned whoever was outside him." The guard-tackle
**deuce** combo on a 3 is the most common double team in football; when nobody is on the tackle (no 5) he is *free*
to help, then climb. The 3 is one-on-one mainly in pass protection (the center slides away, the tackle has the edge)
and when the defense puts a 5 or a 4i on the tackle. **Fix:** "...he is the interior lineman most likely to get a
single blocker on passing downs, and against the run the offense has to choose: double him with the tackle (and give
up that blocker's climb to a linebacker) or block him one-on-one. Either answer suits the defense." Then the text
before "The cost is the mirror image" stays true.

### 9. Down-block technique (l. 896-900, fig-block-reactions panel 1)
- "drops his outside shoulder into the blocker and pushes back outward" is fine, but the "fight across the blocker's
  head" line needs its caveat: crossing a down-blocker's face takes the defender into the hole only if he wins; most
  staffs teach "fight pressure, keep your gap, never go behind the block". Say "a few defenses let a dominant player
  fight across the blocker's face; if he doesn't win, he has given up the inside".
- Panel 1 shows the 3 with no response arrow (his path, `(2.2, 3.05)` from d=2.6, is a 0.4-yard move hidden under the
  block bar) and the 3 and 5 squares nearly touch. Give the 3 a short orange push toward the tackle
  (`go_to(p, "D3", (2.0, 3.4), "path")`), and move the 5 to `T("5") + 0.5`. Also note the guard is standing still in
  panel 1; on power he would usually be part of the down block (double the 3 with the tackle). Either show the G
  stepping to the 3 or say "the guard is omitted".
- Panel 2 (reach): the RT and LT are dropped, so the runner's path appears to cut up through an empty space where the
  tackle should be, and the arrow tip touches the right edge (w0+SPAN = 6.3). Keep the RT (show him stepping to the
  next defender) and end the runner at `(-1.0, 5.6)` with the "has to keep running sideways" idea drawn flatter:
  `via=[(-4.6, 2.4), (-3.4, 4.6)]`.

### 10. Contain needs the modern caveat (l. 1013-1016)
The classic backside-end rule (trail at the depth of the ball: "boot, counter, reverse") is right, but a coach will
add that against zone-read teams many calls tell the backside end to **squeeze/crash** the zone and give contain to a
linebacker or safety who scrapes outside: the *scrape exchange*. One sentence plus a link to 05-05 (or 03-05 for the
read): "Not every call keeps the end outside: against read-option teams the end is often told to crash and a scraping
linebacker takes the quarterback, a swap built to confuse the read."

### 11. One-gap mechanics and stance are missing
The chapter says a one-gapper "attacks his gap" but never says *how*, which is the most-taught fundamental in D-line
rooms. Add three sentences in "One-gap": stance (shaded alignment, the hand and foot on the gap side back so the
first step goes into the gap), the key (move on the ball or the blocker's first movement, as the strip says), and
"hat and hands" (helmet into the gap you own, hands on the blocker's near breastplate, pad level under his). That gives
the reader something to *see* at the snap, which the "Watch for it" box then asks for.

### 12. The head-up 4 (and the 2i) are missing from the technique map, though the chapter uses them
fig-gap-accounting, fig-two-gap-nose and Drill 1 all use **head-up 4s** as the two-gap ends, but the map and "The 4i
and the 5" section never mention the 4 (only 4i and 5). Add "4" to `TECHS` (head row, x = -2*SP) with the 4i/5
silhouette's leader, and one sentence: "The classic two-gap 3-4 end is a head-up 4, controlling the tackle and owning
the B and C gaps; the one-gap version plays a 5 or a 4i." A note on the 2i (the guard's inside shoulder, a common
"shade" for 3-4 ends and under-front tackles) would complete it; 03-01 already defined it.

### 13. 4i rationale (l. 511-514)
"The tackle can't easily reach him (he is already inside the tackle's body)" mixes up who reaches whom. Be specific:
"On a zone run toward him, the guard has to reach a man who is already outside him; on a run away, the tackle has to
cut off a man who is already inside him. And because he can play off either blocker, he muddles which of them should
take him and which should climb." (Matches the fixed 03-01 wording.)

### 14. Drill 3: the backfield is not empty (l. 1310, l. 1318)
The question says "an empty-looking backfield", but the drawing has an R right beside the Q (`(-5.0, -1.5)`; the two
markers touch). Either drop the R (true empty, five receivers) and change the text to "empty backfield", or keep him
and say "one back beside the quarterback, who may stay in to block". If he stays, move him to `w=-2.0`. Add one line to
the answer: offenses often also use a **spy** or "mush rush" (rushers stay level with the QB) against a runner; it
reinforces "flatten the rush".

---

## P3: polish

15. **Wide-9 alignment** (l. 527-529, fig-wide-nine caption): "often a good two yards beyond him" / "two and a half
    yards outside the tight end" is at the wide end; Washburn-style ends were commonly 1 to 2 yards outside the TE's
    outside shoulder. Say "one to two-plus yards outside him, varying by down and distance".
16. **The "if nobody blocks you" rule** (l. 916-919): add the other likely explanation for an unblocked end: he is the
    *read* man on an option (link 03-04/03-05). "Trap or read" is the coach's phrase.
17. **Cut blocks** (l. 958-962): backside defenders against zone face cut blocks; one clause ("and he plays the cut with
    his hands, keeping his feet free") is the nuance a line coach would add.
18. **Go deeper table** (l. 1415-1416): `.reset_index()` prints a 0/1 index column in the PDF. Return the frame without
    it (e.g. `depth_table(...)` with the defender name as the index, or `.style.hide(axis="index")`).
    For the eval: false BDB cell: filtering on `position in ["DT","NT"]` misses 3-4 ends who play 4i/3 and DEs
    who slide inside on sub downs, and an unblocked defender (read, trap, influence) shows up as a "penetrator" too.
    One sentence of caveat in the text keeps the analytics honest.
19. **Edge/contain labels near the window edge:** "QB boots away from the fake" (d=-8.0 in a window starting at -8.6)
    and "a quarterback who likes to run" (d=-7.4) sit within ~1 yard of the bottom edge; nothing is clipped, but widen
    the window to -9.6 per the 1.5-yard convention.
20. **Front labels:** fig-gap-accounting and the slant figure's 4-3 (3 to the tight end, 1 away, 9 outside the Y, Sam
    off the ball in the C gap) is a 4-3 Over with a wide strong end, which is fine, but say "a 4-3 Over" once in a
    caption so 05-02 can refer back to it.
21. **Two-gap strip frame 2** (+0.45 s): the guards are drawn level with the nose at the line, so frame 2 looks like a
    three-man wall on the nose. A climbing guard is a step upfield and outside by then; ending their first leg at
    `(0.6, ±2.0)` reads better.
22. **Animation count/timing:** two animations (well under the cap). The one-gap strip's +0.3/+0.65/+1.15 and the
    two-gap's snap/+0.45/+1.25 split tell the story in print; no change beyond the fixes above.

## Checked and fine

- Technique numbering, gap letters and the map's positions (5 and 4i bracketing the LT, 1 and 0 on the center, 3,
  9 outside the Y, wide-9) match 03-01 and gridiron's `technique()`.
- Two-gap "read the blocker's head / play across the face" rule: correctly stated.
- Squeeze/box vs spill/wrong-arm on the down-block "man left alone": correct and correctly deferred to 05-05.
- Reach: outside arm free, don't run around the block; double team: don't get moved, keep both, make a pile.
- Hard vs soft edge, force defender deferred to 05-05; pass-rush contain "not past the QB's depth".
- Slant costs (bet on direction, zone absorbs it, LBs must move with it) and the loop/stunt hand-off to 07-01.
- Film rooms: Sapp as the Tampa 3-technique; Wilfork's two-gap nose with the Traylor/2010-11 caveats; Donald's two
  snaps in LVI; the 2011 Eagles as the full-time wide-9. All accurately characterized. (Optional: the 2011 Eagles'
  run defense struggled early that season, which would make the "trade" concrete if the fact-checker can source it.)
- Common misconception box (3-4 is not always two-gap; Phillips): exactly the right nuance.
