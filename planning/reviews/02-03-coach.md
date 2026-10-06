# Coach / film-analyst review: 02-03 Classic Formations

Reviewed 2026-10-06 against the chapter source and `pdfs/02-03-classic-formations.pdf`
(24 pages, rasterized at 80 dpi, with the iso diagram, both frame strips and the family
tree re-rendered at 200–250 dpi). I looked at every figure.

**Verdict:** this is a strong chapter. The plates are legal, consistent and clean, the I/offset
I/Power I/ace material is right, and the data sections hold up. There is **one real
football error** (wishbone pitch and lead roles are reversed), **two diagrams whose
assignments don't do what the captions say** (the iso and the H-back strip), and a list
of smaller nuances. Fix the items under "Must fix" before sign-off.

---

## Must fix

### 1. Wishbone triple option: the halfback roles are reversed (text, "The wishbone")
> "The halfback on the play side is the third, trailing the quarterback as a pitch man ... The
> halfback on the other side becomes a lead blocker."

It's the other way round. In the wishbone triple option the **playside halfback is the lead
blocker** (he arc- or load-blocks the pitch-support defender: the corner, the force safety or
the outside linebacker), and the **backside halfback is the pitch man**: he starts away from
the play and runs across to get pitch relationship (about 4–5 yards outside and 1–2 yards
behind the QB). That lead blocker *for the option* is the wishbone's whole selling point, and
it's why Bellard staggered the halfbacks deeper than the fullback: the backside halfback
needs the depth to get across in time.

**Fix:** "The fullback ... the dive. The quarterback is the second, running along the line.
The third is the halfback from the *other* side, who starts away from the play and sprints
across behind the quarterback as the pitch man; that's why the halfbacks line up deeper than
the fullback. The playside halfback leads around the edge and blocks the defender who would
tackle the pitch man. So every back has a job on every play: dive, lead, pitch." The current
sentence "Every back has a job on every play" then lands properly. (Also check 03-04 and
11-03 when they're written, so they don't inherit the reversal.)

### 2. Iso diagram and frame strip (`fig-iso`, `fig-iso-strip`): the Mike is never blocked
- In `iso_play()` the left guard blocks a **point** `pts=[(3.2, 0.5)]` (relative, so it ends at
  about d 2.5, w −1.1), while the Mike scrapes to absolute (3.4, −1.0). The guard stops short
  and the Mike is left free in the hole. The 1.9 s frame shows the result: the ball carrier is
  sitting **on top of the M** at about LOS+3.5, not "through the hole, past the linebackers"
  as the caption says. The M box also covers the ball carrier there.
- **Fix:** `p.block("LG", target="MIKE", speed=3.4, delay=0.15)` (the backside guard climbs to
  the Mike, the standard iso rule against an Over front with a weakside 1-technique), or keep
  the point and move it to meet the Mike's endpoint (about d 3.2, w −0.8 absolute). Then
  extend the RB path so that at 1.9 s he is clearly at LOS+5 or deeper, past the linebacker
  level, or change the frame times to [0, 0.6, 1.2, 2.2].
- **Strip caption, 0.6 s:** "By 0.6 seconds he [the fullback] is crossing the line." In the
  frame he is still about a yard *behind* the left guard. Either say "is arriving at the line"
  or move the frame to about 0.85 s.
- **Static caption:** "The five linemen and the tight end each block a defender in front of
  them." The left guard doesn't. He climbs to the second level. Say: "Four linemen and the
  tight end block the man in front of them; the left guard climbs to the Mike; the fullback
  leads through the B gap (between the left guard and left tackle) on the Will." Seven
  defenders in the box, seven blockers, the runner reads the last block. That's the arithmetic
  of the iso, and it's worth saying.
- **Static legibility:** the fullback's lead path and the tailback's path start from the same
  column and overlap from the backfield to the hole, so the fullback's T-bar on the Will is
  nearly invisible (it's hidden behind the left tackle and the E box). Offset them: start the
  fullback's path aimed at the B gap from the first step (for example via (−2.0, −1.6) to
  (1.6, −2.8) absolute), and draw the tailback's path one-half yard inside it (his aiming
  point is the inside hip of the guard, and he bends off the fullback's block). The
  `fullback leads, blocks the Will` leader should point at the fullback's T-bar, not at
  empty grass.
- The front itself is correct and well chosen: a 4-3 Over with the 3-technique to the tight
  end side and the 1-technique to the weak side leaves the weak B gap as the "bubble", with the
  Will over it. That's exactly where you run the iso. Consider saying so in a clause: "the iso
  goes where there's no defensive lineman in front of the linebacker."

### 3. H-back motion strip (`fig-hback-strip`): the run goes straight into the unblocked Sam
- The Sam travels across with H (his final spot is about d 4.0, w −6.2, outside the new
  H-back). At the snap, H blocks the end, the left tackle climbs to the Will, the tailback
  runs at w ≈ −4.2, and **nobody blocks the Sam**, who is now the playside force player
  standing right in the runner's path. The caption says the motion "changed which side had
  the extra blocker", but the picture shows the defense cancelling it and the offense running
  into it anyway.
- **Fix, option A (keep the travel, which is a real rule in some 4-3 systems, "Sam to the
  tight end"):** keep the run to the left, but H arcs or inserts to the Sam
  (`p.block("H", target="SAM")`), the left tackle base-blocks the end (`target="WDE"`), the left
  guard climbs to the Will, and the center or right guard climbs to the Mike. Caption: "the
  defense matched the motion with the Sam; the H-back now blocks *him*, and the left tackle
  takes the end."
- **Fix, option B (cleaner teaching point):** don't move the Sam. Have the Will widen a step
  and the Mike bump half a gap (`fix` moves at −1.1 s), and run left with H on the end. Then
  the caption's claim (one motion created a new strong side and an extra blocker there) is
  what the picture shows. Add one sentence: "Most defenses bump their linebackers rather than
  run the Sam across the formation; some teams' rules send the Sam with the tight end."
- Either way, add the nuance a coach would insist on: **the defensive line didn't flip.** The
  3-technique is still on the right, so after the motion it's on the *weak* side, and the
  offense now runs at the 1-technique side with an extra blocker. That front/strength mismatch
  is the real reason the motion works.
- **Label collision at −1.1 s:** the S box sits on top of the M box while the Sam crosses.
  Send the Sam behind the linebackers (path via d ≈ 5.5, then back up to 4.0) so the boxes
  never overlap.
- `p.highlight("H", ...)`: the gold ring doesn't show in the strip frames. Either drop it from
  the caption's implied legend or accept it. (The caption doesn't mention a ring, so this is
  minor.)

### 4. Family tree: the single-wing icon is an illegal formation
`SINGLE_WING` has five linemen plus one end on the line (six) and the wingback off the line,
so the icon shows **six on the line**. The single wing had seven: an unbalanced line with the
weakside end too. **Fix:** add `P("SE", "TE", LINE_D, -3.2)` (the weak end). Also separate
the tailback and fullback, which overlap at glyph scale: TB about (−5.0, 0.6), FB about
(−4.3, 2.6), BB at (−1.2, 2.6). Leave the blocking back dark blue if you like, but the
caption could say "the dark-blue dot in the single wing is the blocking back; the snap went
to the tailback."

---

## Should fix (nuance and accuracy)

5. **Pro set, "What does it give up?"** "A back who takes a handoff from a split alignment is
   usually running at an angle, sideways first." That overstates it. Split-back dives, traps
   and the split-back veer are among the **fastest-hitting runs in football** (the back is
   about five yards deep and close to the hole). What split backs give up is the *deep*
   tailback: less time to read the blocks, no lead blocker aligned in front of the runner (a
   lead has to come from the other side and cross), and less cutback room. Also, the
   threat diagram draws each back running straight ahead, which contradicts "sideways first."
   Rewrite: "Neither back is deep and directly behind the quarterback, so the runner has less
   time to read blocks, and a lead blocker has to cross from the other side..."

6. **The tailback's aiming points and the I's "downhill" claim are fine.** One addition a coach
   would want: the I's tailback is also the formation's **cutback** threat. From seven yards
   and centered he can press the play side and cut back across the formation; that's why
   zone teams kept the I (see item 7).

7. **"The one-back, two-tight-end look became the home of the modern NFL run game."**
   Overstated. Mike Shanahan's 1990s Broncos, *the* zone-running offense, ran wide zone
   largely from the I and offset I with fullback Howard Griffith; Kyle Shanahan's 49ers do it
   from the I with Juszczyk today. Soften: "...it's why one-back, two-tight-end sets became a
   main home of zone running, alongside the I." (Gibbs/Bugel's one-back zone in Washington is
   the right lineage for the one-back half.)

8. **Terminology dialects a coach would insist on (offset I and pro set):**
   - Offset I is also called **Strong I / Weak I** (very common in NFL playbooks and in
     *Madden*); split backs are **Near / Far / Split** in many systems (near back to the
     strong side or the call side). Add one sentence and the aliases (glossary aliases for
     "Offset I": "Strong I", "Weak I").
   - Classic formation names are usually **backfield + receiver set**: "I Pro" (one tight end,
     receivers on both sides), "I Twins" (both receivers to the split-end side), "I Slot",
     "Pro Set Flex" and so on. A reader hears "I-formation twins" on broadcasts. One short
     paragraph (or a row under the anatomy figure) would close this gap and set up 02-04.
   - Misconception box: "One team's 'ace' is another's 'Tiger' or 'Heavy'." "Heavy" usually
     means 13 personnel or extra linemen, not balanced 12. Use **"Deuce"** or "Tiger" (both
     real names for one-back, two-tight-end looks) instead.

9. **Goal line, personnel line:** "In personnel terms that's 23, or 13 with a fullback swapped
   for a tight end." Swapping the fullback for a tight end turns 23 into **14** (one back, four
   tight ends), not 13; 13 would put a receiver on the field, which contradicts "no wide
   receivers." Fix: "23, or 14 with a tight end at fullback, or a jumbo grouping with a sixth
   lineman." Same fix in the table ("23 (or 14, or jumbo)").

10. **Goal-line diagram (`fig-goal-line`, `fig-predict-gl`): depths and splits.**
    - The defensive linemen are at d = 1.0 and the linebackers at 3.2 (two-plus yards into the
      end zone). Goal-line defensive linemen get as close to the ball as the neutral zone
      allows, low, in four-point stances (about d 0.4–0.5), and the linebackers sit at
      about 1.5–2 yards, on or just behind the goal line. Move the DL to d = 0.5 and the
      LBs to d = 1.8–2.2. Keep the safeties at 3.5–4.5.
    - The text says goal-line splits "shrink to a foot or two," but the plate uses the normal
      `OL_SPLIT` = 1.6 (about a 3-foot split). Draw the goal-line plate with a tighter line
      (spacing about 1.25) and the tight ends at about 3.9 and −3.9, with the wing at about
      5.2. Do it inside the chapter (a local `line5(split=...)`), not in gridiron.
    - The defensive line is all gap-aligned except the nose. That's realistic for a gap-8 /
      5-3 goal-line front; good.

11. **Predict 3 answer: coverage language.** "With ... only one safety deep in the middle, a
    well-sold fake can leave the outside receivers one-on-one with cornerbacks and nobody
    behind them on one side of the field ... look downfield at the receiver on the side away
    from the deep safety." With the free safety centered, "the side away from the deep safety"
    has no meaning. And with corners at seven yards and one high safety, the likeliest
    coverages are Cover 3 (corners bail to deep thirds) or Cover 1 (man, safety help in the
    middle). Rewrite: "Single-high means each cornerback is alone on his side. Against man
    (Cover 1) that's a one-on-one outside; against Cover 3, the fake pulls the linebackers up
    and opens the window behind them for a deep crossing route or a dig. Either way the run
    fake is what moves the eight defenders." Keep the forward link to the coverage chapters.

12. **49ers film room, "What to notice."** "If he heads for a linebacker, it's a run; if he
    heads for the flat ... the defense is about to be fooled." On Shanahan's play-action the
    fullback's first steps are designed to look *the same* as on the run. The tell comes a
    beat later: on the bootleg he crosses the formation as if to block the backside end
    (the "slice" path), and then **doesn't block anyone** and leaks into the flat. Rewrite:
    "watch where the fullback's path ends. If he hits someone, it's a run; if he crosses the
    formation, brushes past the end and keeps going to the flat, it's the bootleg." Also, in
    the Shanahan run game Juszczyk leads as often on the **edge/force defender** (on wide
    zone) as on a linebacker. Say "leads on a linebacker or the edge defender."

13. **T-formation paragraph:** "With three backs, all a step or two from the line." They're
    four to five yards deep (the figure says 4½). Say "all a few strides from the line."

14. **Wing-T:**
    - The figure caption says "Every play starts with the same *motion*." In this book
      "motion" means pre-snap movement (01-05, 02-06). Say "the same backfield action."
    - Name the bootleg the way Wing-T coaches do: the **waggle** (the bootleg with a guard
      pulling to the boot side to protect the QB). Add it to the buck-series sentence: "...a
      trap up the middle (the buck trap) or a quarterback bootleg the other way (the
      waggle)." This also pays off the NFL "keeper/boot" link.
    - Mention that the Wing-T line blocks down and pulls rather than base-blocking. Down
      blocks plus pulling guards are the series' signature, and the reader will see the same
      thing in 03-03.

15. **Family tree, minor:**
    - **Split-T:** what "split" referred to was Don Faurot's **wide line splits** (and the
      quarterback riding down the line). The icon widens the *backs* (±3.6) instead.
      Widen the line spacing in the icon (OL at about ±1.0 per man at glyph scale) and keep
      the backs where the T has them.
    - **Shotgun's parent:** the edge into "Shotgun and spread" comes only from singleback.
      Red Hickey's 1960 shotgun was explicitly a direct-snap, single-wing/short-punt idea.
      Add a dashed edge from the single wing to the shotgun. The tree then tells the truth
      that the shotgun is the single wing's return.

16. **"The shotgun is a better place to pass from ... doesn't have to ... take a three- or
    five-step drop."** Shotgun QBs still take drops (a one- or three-step from the gun
    times like a three- or five-step from under center). Say "takes a shorter drop and never
    has to turn his back."

17. **Opening hook:** "a 300-pound fullback and a 247-pound running back, seven yards deep."
    This reads as if both are seven yards deep. Say "...a 300-pound fullback, and behind him,
    seven yards deep, a 247-pound running back."

18. **Wishbone plate depth/width (small):** the halfbacks at ±2.5 are between the guard and
    tackle. Bellard's halfbacks lined up about behind the **tackles** (±3.0–3.2 here) and a
    good yard deeper than the fullback (FB about 3.5–4, HBs about 5–5.3). The depths are
    right; widen the halfbacks to ±3.1. That also makes the upside-down Y read better.

19. **Watch-for-it bullet:** "A tight end standing off the line next to a tackle (an
    H-back) counts as a blocker, not a back, for naming." Reasonable, but it contradicts the
    Wing-T, where the off-the-line wingback counts as a back, and NFL broadcasts that call a
    tight end at fullback an "I". Add: "...unless he's directly behind the quarterback; then
    it's still an I."

---

## Checked and correct (no change needed)

- **Every plate is legal:** seven on the line, covered receivers ineligible (the chapter's
  `check_legal` asserts it), and the flanker is off the line so Y is the end. The pro set,
  I, offset I, Power I, singleback, ace, wishbone, flexbone and Wing-T alignments,
  depths and letters are realistic. The flexbone's slotbacks are about a yard and a half off
  and outside the tackles, and the B-back is about 4.5 deep. The Wing-T halfback is behind
  the weak tackle and the wingback a yard outside and behind Y.
- **Personnel counts** in the plates, captions and table are right (T 32, wishbone 31,
  flexbone 30, Wing-T 31/21, Power I 31).
- **The I's three virtues** (running start, time to read, lead blocker) and costs (slow to the
  edge, backs late into routes, tendency) are exactly what a coach would teach.
- **Offset strong/weak** and the "tilt is a tendency, so smart offenses break it" point are
  right. Drill 1's answer is sound.
- **Power I:** two lead backs on two linebackers, with the TE on the Sam. Correct.
- **Lombardi film room:** Red formation (wide split backs), both guards pulling, the fullback
  on the end, "run to daylight". Right. "What to notice" is well judged.
- **Gibbs film room:** the Taylor/H-back origin, the counter trey (backside guard and tackle
  pulling against the backfield's first step), the Hogs. Right and well characterized.
- **Flexbone film room:** the motion slotback becomes the pitch man ("which way the option is
  headed"), the other slot often blocks. Correct (and it's the *flexbone* version of the
  roles that item 1 gets backwards for the wishbone).
- **Goal-line arithmetic and Drill 2** (play-action to the wing or backside tight end, watch
  the safeties) are good coaching.
- **Data figures** (shotgun trend, QB location, under-center usage, team scatter) are labeled
  clearly. The labels don't collide; the "Eagles/Chiefs" pair is tight but legible.
- **Label/edge rule:** no on-field label is clipped by the drawn window in any figure. The
  Wing-T "bootleg" tag is about 1.3 yd from the bottom edge, close to the 1.5-yard rule but
  not clipped. The only collisions are the strip frames noted in items 2 and 3.
- **Animation count:** two strips (iso, H-back), well under the cap. Both tell their story
  in print once items 2 and 3 are fixed.
