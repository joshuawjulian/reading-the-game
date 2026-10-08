# 08-04 In-Game Adjustments, Tempo, and the Sideline Battle: coach / film-analyst review

Reviewer role: veteran NFL coach and film analyst. Scope: football correctness, every diagram (rasterized
`pdfs/08-04-in-game-adjustments-and-tempo.pdf` at 80 dpi; figs 6, 7 and 9 also at 160-200 dpi; all 15 figures looked
at), the tempo frame strip, the before/after frame pairs, missing nuance, film rooms, gridiron use. I also dumped the
simulated positions for `mesh()` to check the frame pairs against what the caption claims. I did not edit the chapter.

**Overall:** a strong, honest chapter. The between-series loop, the "re-rank, don't install" framing, the clean split
between no-huddle, tempo and hurry-up, the substitution-freeze explanation, the history (Wyche, K-Gun, Manning, Kelly), the
call-after-the-call ladder and the halftime data test are all right and pitched well. The 2x2 call ladder (trips rotation,
then X-iso, then bracket, then 3-on-3, then disguise, then motion to identify) is how a staff actually sequences against a
rotating defense. The problems sit in three diagrams (the halftime frame pairs don't show what the caption says; the
disguised-pressure panel has a mugged linebacker in an occupied gap and an empty blitz-side flat; the sugar-huddle drill
has a label clash and a huddle that isn't close), one muddled rule sentence (twelve men), and a few things a coach would
add: DL rotation as the real fatigue mechanism, injuries as the biggest in-game adjustment, the headset side of the equity
rule, and tempo used to beat a replay challenge.

Priority: **P1** = misleading football, fix before publishing; **P2** = a coach would object; **P3** = polish.

---

## P1: must fix

### 1. fig-before-after (halftime frame pairs) doesn't show the adjustment working (`mesh()`, ~l. 1166-1214)
I dumped the positions. In the second half at +1.6 s: H is at (2.0, 3.1), but the SS "sitter" is at (4.0, 4.6), two yards
*behind* H and outside him, with H running away from him. Y is at (5.1, 0.3) and the nickel is at (4.8, -4.0), four yards
away. Neither crosser has reached his sitter. H is still the obvious throw: uncovered in front of the SS. So "each crosser runs
straight into a waiting defender ... nowhere to go" is not what the frame shows. A coach will see an open shallow.
**Fix (pick one):**
- Move the sitters to where the crossers arrive at about +1.6: `go_to(p, "NB", (5.0, -1.5), "path", speed=2.4)` and
  `go_to(p, "SS", (3.0, 2.4), "path", speed=2.4)`. Each defender is then on his crosser's track, a yard in front of him.
  Change "sit at about five yards" in the text and caption to "sit at four to five yards".
- Or keep the sitters and put the second frame at about 2.2 s, after checking that each crosser is on top of his sitter.
Also fix the crosser depths so the play is actually mesh. H flattens at 1-2 yards (a drag). Real mesh crossers run at 5-6
yards, about one yard apart, with the mesh point over the ball. Use `go_to(p, "H", (4.5, 10.5), "route", via=[(4.0, -5.5)])`
and Y at 5.5-6.0. The sitters' depth then matches "sit at five yards" as written.

### 2. fig-before-after, first half: man trails zig-zag, and the Mike blitzes into the RDT (same function)
`p.man()` gives jittery trails. The nickel goes 5.5 → 4.2 → 5.0 → 3.8 deep. The SS goes 6.0 → 4.7 → 5.9 → 7.1 → 6.6 and
loops back. In print the trails look like busted coverage, not "a step behind through the traffic." Replace `p.man` for NB
and SS with explicit trail paths, one yard behind and on the near hip of each crosser, e.g.
`go_to(p, "NB", (3.0, 1.5), "path", via=[(4.6, -6.0), (3.4, -2.5)], speed=4.6)` (and the mirror for SS on Y).
Separately, the Mike's blitz ends at (0.6, 0.9) and the RDT's rush ends at (-0.4, 0.8). They finish on top of each other in
both +1.6 frames (the "M" box sits on the "T"). Send the Mike through the right B gap, `go_to(p, "MIKE", (0.4, 2.4), ...)`, or
slant the RDT into the left A gap so the Mike has the right A gap.

### 3. The twelve-men sentence is muddled (l. ~347-350)
"if the offense snaps while a twelfth defender is still on the field, that is a five-yard penalty, and if he's still
running off at the snap, the play goes on and the offense can keep the result or take the yards." That describes the same
foul twice, as if it were two. **Fix:** "If the defense has twelve on the field at the snap, even one player jogging off,
it's a five-yard foul. And because it's a live-ball foul, the play runs: the offense keeps the result or takes the five
yards. That 'free play' is why quarterbacks rush the snap when they see a defender running for the sideline." (Fact-check:
whether the NFL also has a dead-ball version for a defense with 12 in formation before the snap. If so, add one clause.
Don't guess.)

---

## P2: a coach would object

### 4. fig-tempo-defense, left panel (disguised pressure): mugged LB in an occupied gap; blitz-side flat left empty
- The Mike mugs at (2.2, +0.9), but the RDT is a shade at w=+0.8, already in that A gap. You can't walk a linebacker into a
  gap a defensive tackle occupies. Double-A-gap mugs come with the tackles in 3-techniques (or a three-down front). In this
  panel, move the RDT to a 3 (`w=2.4`, outside the RG). The W and M boxes also nearly touch and the M ring overlaps the T.
  Mug them at w = ±1.0 after moving the RDT.
- Coverage behind the five-man pressure: the dropping LDE goes straight up at w=-4.6, the Will crosses to (6.5, +2.8) and
  the SS comes down to (8, 6.5). That leaves the blitz side's curl/flat (H's side, where the nickel left) empty. The H quick
  out is wide open, which is the first hot a fire zone is built to take away. Standard 3-under: the dropper replaces the
  blitzer. **Fix:** `p.drop("LDE", (6.5, -8.5))` (seam-curl-flat to the nickel's side), `p.drop("WILL", (7.0, -0.5))` (hole),
  and keep the SS on the right curl/flat.
- The corners have no actions, so they stand at 7 yards in a three-deep pressure. Add `p.drop("LCB", (15.0, -12.5))` and
  `p.drop("RCB", (15.0, 12.5))` (deep thirds). Otherwise the reader can't see it's 3-deep, 3-under behind five.
- Right panel (quarters) is fine. One caption nuance: quarters still pattern-matches after the snap, so "tells the QB the
  truth" is about the shell, not the coverage. Say "shows the shell it will play".

### 5. fig-predict-sugar: "W" label clash; the huddle isn't close (l. ~1520-1530)
- The third tight end is labelled "W", which is also the Will linebacker in the same picture and in the key. Use "V" (or
  any letter not in the key), and add F (fullback) and the new letter to the "How to read the diagrams" key. F isn't there now.
- The huddle is centred 7 yards back with radius 3 (it spans 4-10 yards). The label says "4-5 yards back", and the point of
  the drill is that it's *close*. Use centre `-4.0`, radius about 2.0 (lateral 2.3). The label and caption then hold up, and
  the circle isn't a 7-yard pro huddle.

### 6. Fatigue point misses the real mechanism: DL rotation (l. ~310-313)
Coaches don't mainly fear one tired tackle. They fear losing the rotation. NFL defensive lines rotate constantly (most DL
play well under 80% of snaps), and tempo with no offensive substitution stops the defense subbing fresh linemen in. Add a
sentence: "Defensive lines rotate every few plays to stay fresh; tempo freezes the rotation, so the same four men keep
rushing." This also links fatigue to the freeze, which the chapter treats separately.

### 7. Injuries are the biggest in-game adjustment, and they're missing (halftime list, l. ~218-227; loop text)
Every line coach will say this first. When the left tackle or the nickel goes down, the plan changes: chips and slide
protection toward the backup, a different package for the backup corner, plays scratched because the replacement hasn't
repped them. Add a bullet: "**Replanning around injuries.** The most common forced adjustment: a backup tackle gets help
from a tight end or back; a backup corner gets safety help or is hidden in a package."

### 8. Equity rule covers headsets as well as tablets (l. ~136-137)
The equity rule is best known for headsets: if one team's coach-to-player radio fails, the officials shut off the other
side's. Add "and the coach-to-player headsets" (same `[^equity]` source, which covers it; fact-check the wording).

### 9. Kelly film room overstates "one personnel group" (l. ~932-936)
Kelly's Eagles lived in 11 but used a lot of 12 (Celek and Ertz, and James Casey in 2013-14). The tempo point holds because
the 12 group could also play spread, which is exactly the freeze idea. Say "with one or two personnel groups (often 12 that
could spread out like 11)". Have fact-check confirm the 12-personnel share before quoting a number.

### 10. Score-effects bullet leans on a tiny, partly tautological number (l. ~1346-1352)
"Teams leading by 1-13 at the half were outscored by about 0.3 points in the second half, and teams trailing by 1-13
outscored their opponents by the mirror amount." The mirror is automatic (every leader has a trailer). And 0.3 points is
too small to "push every good team's second-half margin down." The effect is real but shows up mostly with big leads. Quote
the 14+ bin (`LEAD_BINS.iloc[4]`), or say "small at modest leads, larger with big ones" and drop "the mirror amount."

### 11. Sugar huddle history: link it to Wyche (l. ~455-463, 474-484)
The text describes Wyche's "shortened huddles very close to the line" but doesn't connect them to the sugar huddle defined
a section earlier. Wyche's Bengals are commonly credited with the "sugar huddle" (fact-check). One clause in the 1988
paragraph, "the quick huddle near the line that became known as the sugar huddle", ties the history to the term. As
written, the reader thinks the sugar huddle is a Ben Johnson invention.

---

## P3: polish and nuance a coach would add

12. **Tempo vs. replay.** A common in-game use of tempo: snap before the opponent can challenge a close catch or spot.
    Scoring plays and turnovers are reviewed automatically; most other plays need a coach's challenge. One sentence under
    "Why go fast?" (fact-check which plays are auto-reviewed in 2026).
13. **The officials are the speed limit.** After a long gain the umpire has to spot the ball and get clear before the snap.
    That's the real floor on tempo, and it's why the hook's "set eight seconds after the tackle" still means a snap at
    12-15 s. One clause in the freeze section helps the reader see why a 15-second play clock isn't the floor.
14. **"Look to the sideline" tempo.** The info no-huddle has a named pattern: sprint to the line, let the defense show its
    call, then everyone looks to the sideline for the real call. Naming it next to Washington's 78% no-huddle and 39 s
    median would explain that number.
15. **fig-tempo-snap (strip), the RCB and SS are statues.** In panel 4, Z has run past the RCB, who never moves, and the SS
    is static too. Give the RCB a backpedal, `go_to(p, "RCB", (9.0, 12.5), "path", delay=0.2, speed=3.0)`, and the SS a
    shuffle. The story (the nickel inside H) still reads well. Timing [-2.0, -0.8, 0, 1.2] is good. The ball in panel 4 is in
    flight (checked), not a bug.
16. **SB LVII film room.** Add a possessions point: Kansas City received the second-half kickoff and scored a TD on it (the
    chapter's own "possessions" force; fact-check who received). Also worth a clause: Philadelphia, the league leader in
    sacks that season, had none all game. KC's protection plan is the "adjustment" that held in both halves. That supports the
    chapter's thesis that the plan, not the locker room, won it.
17. **fig-predict-freeze:** the "U/Y: nobody within 6 yards" label boxes sit on the yellow line-to-gain. Drop them to
    d=8.0, or the line can stay hidden (`to_go=None`), since this drill doesn't need it.
18. **Predict 1 answer:** "quick hitch, out or seam" to a TE with a safety at 11 yards directly over him. The seam isn't
    the count-rule throw. Say "a quick hitch, stick or out (or an RPO tagging the TE)". The RPO is the modern default here.
19. **Predict 2 answer:** fine. Optionally add the RB "rail/wheel" as a sitter-beater. The pivot is the best answer, though.
20. **Booth paragraph:** "which coordinator sits upstairs varies" is right. Many DCs call from the booth while most
    offensive play-callers are on the sideline. Saying which is more common would sharpen the broadcast tip.

## Checked and correct
Matching rule mechanics and the 2:00 exemption; the 15-second radio cut-off; 13-minute halftime; the injured player sits
one down; the 2025 slow-walk/simulated-substitution guidance; the Wyche 1988 story (Nash, Levy, 21-10); K-Gun (McKeller,
Kelly calling plays, Marchibroda, 13-3/428 points, 51-3, four Super Bowls); Super Bowl XXV 40:33; the 606-point 2013 Broncos;
the 2012 Patriots plays; Kelly's tenure and exit; SB LVII facts (24-14 half, the ankle, four second-half scores, two
fourth-quarter Corn Dog TDs, the 65-yard Toney return). The fig-freeze formations are legal (seven on the line in both
panels) and the box counts in the text match the drawings. The call ladder is football-correct. No label is clipped by
the field edge in any figure.
