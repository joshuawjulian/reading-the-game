# Coach / film review: 05-02 Even Fronts

Reviewer role: NFL coach and film analyst. I checked the qmd (17:44) and the PDF built at 17:44:55, which is current.
I rasterized every page at 110 dpi (`_pdfbuild/05-02-even-fronts/coach/hi-*.png`) and looked at all 13 figures, including
both frame strips.

**Overall:** this is a strong, accurate chapter. The Over and Under are correct: alignments, gap ownership, the bubble
and the trade each front makes all match how 4-3 staffs teach them. The 46 plate matches the textbook 46. The bear-iso
strip makes its point in print. The wide-9 section is honest about the cost. There is one real football error (two
figures with 10 players a side). One coaching idea is missing, and any 4-3 coach would add it first: **Over to one
side is the same line as Under to the other.** The rest are precision fixes. Items are in priority order.

---

## A. Must fix (football wrong or misleading)

### A1. fig-46-quick: both teams have 10 players
`quick_vs_46()` builds the offense as 5 OL + Y + QB + RB + X + H, which is 10 players. The defense is BEAR (8) + LCB +
FS, also 10. The caption and the text then talk about "three receivers" and "three defensive backs", but the tracking
data the reader may later inspect has only two of each.
- **Offense:** add `O("Z", "WR", -1.5, 15.0, "Z")`. Z must be **off** the line, because Y is on the line on the right
  and an on-line Z would cover him. That gives 7 on the line (X, five OL, Y), which is legal. Give Z a `r.go(10.5)`
  or a hitch.
- **Defense:** add `D("RCB", "CB", 1.2, 15.0, "CB")` and `p.man("RCB", "Z")`. The 46 now has its three DBs.
- Both new players are outside `lateral=(-16, 4)`, so the strip does not change.
- Optional realism: against three wide receivers the 1985 Bears often subbed a nickel DB. Say in one clause that the
  picture is the 46 *caught* in base, which is exactly the matchup Miami went looking for.

### A2. "When the strength moves" leaves out the standard answer: Over one way is Under the other way
Check the chapter's own helpers. `over_front(+1)` puts the 3 on the RG, the 1 shaded left and a 5 on each tackle.
`under_front(-1)` puts the 3 on the RG (the new weak side), the 1 shaded left (the new strong side) and a 5 on each
tackle. **The defensive line is identical.** When the tight end shifts from right to left, the most common answer is
to leave all four linemen where they are and **check the front to Under**. The Sam bumps across and walks up outside
the new tight end, and the Mike and Will bump one gap. Defensive line coaches hate tackles crossing the ball late. The
text instead calls "re-set only the linebackers" "a front that leans the wrong way for one snap", but that front is a
perfectly sound Under, and that is the reason many teams set their tackles by side or by call and not by the TE.
- **Text, paragraph "Defenses have answers…":** replace the first answer with: "The simplest answer leaves the line
  alone. An Over to the right and an Under to the left put the four linemen in exactly the same spots, so when the
  tight end crosses, the call becomes 'Under', the Sam walks up outside the tight end on his new side, and only the
  linebackers move. Nothing crosses the center."
- **fig-strength-shift:** add a third panel titled "Or: check to Under (the line stays)", or replace the right panel.
  Draw `under_front(-1)` with `te(-1)`, put ghosts on the Sam and Will only, and make the caption point out that the
  four linemen did not move. Keep the 3-and-1 swap panel as the option that is more costly and easier to read.
- **Drill 1 answer:** add one line: "Notice that the line is the same one an Over makes when the tight end is on the
  right. Only the Sam and the linebackers tell you which front it is."
- **Takeaways, "Strength is relative" bullet:** add "…or check Over to Under and move only the linebackers."

### A3. The text says the strong end in a 6 or 7 is "tighter". It is wider (The 4-3 Over, paragraph 1)
"some teams play him tighter, in a 6 or 7 on the tight end": a 5 is the tackle's outside shoulder, a 7 the TE's
inside shoulder and a 6 head-up on the TE, so the 6 and 7 are **wider**. Change to "some teams set him wider, in a 7 or
a 6 on the tight end, so the tight end can't release inside cleanly or block down on the 3-technique." Also add this to
the dialect box: 05-01's gap diagram (`fig` with "One-gap 4-3: seven gaps, seven men") drew the Over with the strong end
in a **9** and the Sam *inside* him owning C. Same front, the end and the Sam swap C and D. Name it so a reader
comparing the two chapters doesn't think one of them is wrong.

### A4. fig-attack-bubble: each panel leaves an inside linebacker unblocked
The blocks are "simplified", but each one leaves a box linebacker free and blocks a defender a real zone play would
leave alone. A coach will see it right away.
- **Left (Over, inside zone weak):** RG on the 3, RT on the strong 5, Y on the Sam, so the **Mike is free** in the
  strong A gap, which is the backside cutback lane of a weak zone play. Real rule: LT on the weak 5, LG/C combo on the
  1 to the **Will**, **RG/RT combo the 3 to the Mike**, Y cuts off the strong 5, and the **Sam, backside and 5 yards
  wide, is the unblocked man**. Code: `go_to(p, "RG", (0.3, 2.3))` plus `go_to(p, "RT", (0.3, 2.9))` (both onto the 3),
  then add a dashed RT climb to the Mike (like the LG's green dash, but in blue or grey so the green stays "the
  bubble"). Change Y to `(0.3, 4.6)` (cut off the 5), and leave the SAM untouched.
- **Right (Under, inside zone strong):** LG on the 3 and LT on the weak end, so the **Will is free**. Real rule: Y on
  the Sam, RT on the 5, C/RG combo on the nose to the Mike (already drawn), **LG/LT combo the 3 to the Will**, and the
  **backside end (the Leo) is unblocked**. He is the man a gun team reads, and an under-center team lets him chase.
  Code: `go_to(p, "LT", (0.3, -2.6))`, then a short climb toward the Will.
- **Caption:** add "receivers not shown". Change "Blocks are simplified" to "the backside end is left unblocked, as
  zone plays usually do".

## B. Should fix (precision a coach would insist on)

### B1. Wide-9 data table: the 2011 Eagles had a rookie coordinator
The table credits 2011 to "Washburn". He was the line coach. The **defensive coordinator was Juan Castillo**, a
career offensive-line coach in his first year running a defense, and the linebackers that year were weak (a
rookie Casey Matthews at middle linebacker early on). That is the chapter's own thesis ("judge a wide-9 by its
linebackers"), so say it: change the Coach column to "Castillo (DC) / Washburn (DL)" or add a note column. Add one
sentence in the text: "the 2011 linebackers were the weak link, in a season with a first-time coordinator." Have the
fact-checker source Castillo and Matthews.

### B2. Drill 3 answer: who blocks whom is muddled
"he can let him run past and turn inside to block the Sam, or climb to the Mike while the tackle takes the 3". The 3
is on the **RG**, not the RT. Against two wide-9s with a 3 on the RG, **both the RT and the Y are uncovered**. The clean
answer: RG blocks the 3, RT climbs to the Mike (or Will), **Y blocks the Sam**, and the wide end is left alone. He
either rushes himself out of the play or is read by the QB. Rewrite those two sentences. Then add the point the drill
is set up for: **the zone read and RPOs are the modern way to punish a wide-9**, because the end is the easiest
defender on the field to leave unblocked and read. Link 03-0x (zone read) / 04-06 (RPOs). Also say that the lane
between the 3 and the right end spans **two** gaps (C and D), which is why one Sam can't own it alone and a safety fit
is part of the plan.

### B3. fig-wide-nine-front: what the weak-side lane is
The "5.3 yd" lane on the left is not a single "off-tackle" lane. It spans the uncovered left guard (the bubble) **and**
the weak C gap. Rewrite the caption: "On the weak side the lane runs from the 1-technique all the way to the end: two
gaps, with the Will responsible for the B and a safety or the end's squeeze for the C." The text's "three to five
yards" can stay.

### B4. Drill 2 answer: the defense has a third option
The answer says the offense "wins either way". A base defense against trips usually has a third answer: **rotate a
safety down**. The SS buzzes down over the slot or into the box, the Sam stays, and the shell goes to one-high
(Cover 3 or Cover 1). The chapter teaches exactly this in the nickel section (Seattle's down safety). Add a third
bullet: "**Rotate**: the safety over the trips buzzes down and the defense plays one-high. The box and the slot are
both covered, but now one safety guards the deep middle against three vertical threats, so the offense's answer is
four verticals or a seam." Then: "Every answer costs something, and that is why defenses substitute." Also in the
figure code: add `O("X", "WR", -0.7, -16.0, "X")` and `D("LCB", "CB", 6.5, -16.0, "CB")`. Both are outside the drawn
window, so nothing changes visually, but each side then has 11 players (each currently has 10).

### B5. "No pullers" / "No double teams" overstate the bear
Against a bear, an offense *can* pull or double if a **tackle** blocks down on the guard's 3-technique. The tackles
are the bear's uncovered (or loosely covered) linemen. The bear makes that block long and hard and frees the tackle's
outside man, but it does not make it impossible. Soften "the bear leaves none" to: "the only way to free a guard is a
long down-block by the tackle on a 3-technique, which is hard to make and frees whoever the tackle was supposed to
block." This is also where the offense's run answer comes from. Add one sentence to "Why it disappeared": offenses
ran *outside* the bear (tosses, stretch plays, and runs to the open side away from the stacked tight-end side), as well
as passing over it.

### B6. Nickel figure (fig-under-vs-11): the safeties are inconsistent
- **Left panel:** the 8th man (SS) is down on the **weak** side `(5.3, -4.4)`, but the right panel and the text have
  the strong safety doing "the Sam's old job on the tight end". Against an I-formation, the rotated safety in a 4-3
  Under / Cover 3 (Seattle's model) normally comes down on the strong or field side. Move him to about `(6.5, 8.0)`,
  outside and behind the Sam, and widen the box shading to match. If you want a weak-side 8th man, say so in the
  caption ("some teams roll the extra man weak, to the side the fullback can lead to").
- **Text vs picture:** the text says "The four linemen are the same players in the same spots", while the right panel
  moves the weak end out (`w=-6.4`) and the caption says "the weak end widens". Change the text to "the same players,
  and the three inside men in the same spots; only the open-side end loosens." Label him "w5" (or "7") so the
  technique label matches where he stands.
- **Captions:** add "corners and outside receivers not shown" to both panels. Each side currently has 9 players drawn.

### B7. Film room: Eagles, Super Bowl LII is the wrong game to show run defense
The callout asks the reader to watch the 2017 wide-9 stop the run. But New England barely ran in that game, which
was a 505-yard Brady passing game, and I recall the Patriots averaging about 5 yards a carry on ~22 rushes. The
signature play described (Graham's strip-sack) came with Graham **lined up inside, not from a wide-9**. Either:
(a) keep LII but retitle the "what to notice" around the pass rush and Graham kicking inside on a passing down (a
real and useful wide-9-team habit: on passing downs ends slide inside to rush over guards), or (b) pick a 2017
regular-season or playoff game where opponents ran into the front and failed. Have the fact-checker pull opponent
rush yards per carry by game from nflverse for PHI 2017 and choose the lowest high-volume game (verify LII's numbers
too).

### B8. Film room: Lovie Smith's Bears, "every time"
"He should be on the guard away from the tight end, every time." Smith's Bears set the under tackle by call and by
formation, and they played Over looks too. Change to "on most early downs". Also "Brian Urlacher, behind the nose":
in an under-shaded line the Mike sits over the uncovered **strong guard**, protected by the shade nose. Rewrite as
"over the strong guard, with the nose's shade keeping that guard busy. Watch how often he reaches the ball
untouched."

### B9. Film room, Super Bowl XX: not every snap is a 46
"Before each early-down snap… Eight is the 46" reads as if Chicago lined up in the 46 on every play. By 1985 it was a
package within a 4-3 defense, and New England trailed early and threw most of the game. Change to "On the snaps where
you count eight within five yards, you are looking at the 46." Expect more pass rush than run fits on this tape.

## C. Diagram polish (collisions and clarity)

- **fig-strength-shift, right panel:** the ghost "W" touches the new "M" marker (ghost W at w=-2.0 and new Mike at
  w=-0.8, same depth). The caption also says "the Mike slides over a gap", but no Mike ghost or arrow is drawn. Either
  add `ghost(f, p, 4.5, 0.8, "M")` and move the Will ghost 0.3 yd deeper, or drop the Mike clause from the caption.
  (If A2 adds the "check to Under" panel, this panel is the place to show only the costly option.)
- **fig-bear-iso, frame 4 (t=1.55):** the SS ring, the R marker, the tackle X and the F crowd together, and the "3"
  on the RG is half hidden. Use t≈1.4 (meeting just before contact), or move `spot` to `(1.75, 0.55)` and use
  `ring_r=0.75`. The story reads correctly in print. This is only clutter.
- **fig-drill-1:** only eight offensive players are drawn and the caption doesn't say why. Add "(receivers outside the
  picture)". Drawing the right end as a plain "5" while the caption calls him "a wide end" is fine, but a label like
  "w5" would let the picture teach the loose 5 itself.
- **fig-attack-bubble / fig-over-under:** say "receivers not shown" in the captions (fig-over-under already does this
  for the backs).
- **fig-broadcast:** it works. One honest caveat for the text: in an Under, the strong 1-technique sits almost on the
  "empty" guard's inside shoulder, so from the sideline the visible hole runs from the nose to the 5 (across the RG
  *and* the RT). Tell the reader to look for "the widest space between two down linemen" and not for a man-sized gap
  exactly across from the guard.
- All labels sit inside the field windows. I found no clipped text anywhere.

## D. Nice-to-have nuance

1. **"Bubble" has two meanings.** The run-defense bubble collides with the *bubble screen* (04-03) and the *bubble
   RPO* (04-06). Add a half-sentence: "not the bubble screen; same word, different thing."
2. **Fronts come with coverages.** One sentence linking the fronts to the coverages usually played behind them: the
   Over with Tampa 2/Cover 2 (Kiffin, Dungy, Lovie) and the Under with Cover 3 (Carroll), with links to Part 6. This
   explains why the film-room teams look so different behind the same four linemen.
3. **Strength-call dialects.** "Strong right! Over!" is fine. Many NFL staffs use word codes for direction (Lion/Larry,
   Rip/Liz and so on). One clause in the dialect box would help readers who hear them on mic'd-up clips.
4. **The bear today.** The chapter says the bear is now "mostly near the goal line". Since about 2019 it has also come
   back as a **nickel bear / mug look** against outside-zone teams (see the PFF piece already cited in [^bearname]).
   One sentence with a forward link to 05-03 / 12-08 would connect it to the Macdonald case study. Leave the team
   attribution to the fact-checker.
5. **Wide-9 also invites the draw and the screen.** Ends rushing upfield on every snap are what the draw and the RB
   screen are built for. Mention this with the off-tackle lane cost.

## E. Verified as correct (no change)
- Over and Under alignments, gap tables (5-W-1-M-3-5-S / 5-3-W-1-M-5-S), the uncovered guard and bubble for each,
  and the "why lean" reasoning, including the under tackle name and the 3-4 look of the Under.
- 46 alignment: weak end 1–2 yd outside the LT, double 3s and a 0, both OLBs on the TE (inside and outside), Mike over
  the strong tackle, SS at 4–4.5 yd over the weak tackle, press man and one deep safety. The 46 is named for Plank's
  jersey number. The legal formation in fig-46-plate (7 on the line, Z off).
- Bear-iso logic: 7 blockers vs 8, FB on the Mike, RT on the inside OLB, Y on the outside OLB, the SS is the unblocked
  +1. Frame-strip timing (handoff at 0.6 s, fill at about 1.5 s) is realistic.
- Quick-out timing in fig-46-quick (three-step, ball out at 1.3 s) is realistic. The inside leverage of the box
  safety on H is exactly how the 46 got beaten.
- The "set for one full second" shift rule, and the strength rules with no TE (field, back, receivers).
- Two animations in total, within the limit of four. Both strips tell the story in print.
