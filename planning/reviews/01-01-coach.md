# 01-01 The Game in Fifteen Minutes: coach / film-analyst review

Reviewer role: veteran NFL coach and film analyst, checking technical accuracy and completeness.
Read: the full qmd, AUTHORING, FACTS-current §3–4, the CURRICULUM spec, and both earlier 01-01 reviews
(factcheck, beginner), so I don't repeat their items except where the football itself is wrong.
Rasterized `pdfs/01-01-the-game-in-fifteen-minutes.pdf` (19 pp.) at 80 dpi, then re-rendered the figure
pages at 150–170 dpi and looked at all 14 figures. Checked the clock, try and missed-FG rules against
the 2026 rulebook text (Rule 4-3, 4-4, 4-5, 4-6, 4-7, 11-3, 11-4). Recomputed 4th-and-goal TD rates
in the `rtg` container: from the 1, 55% (317 snaps); from the 2, 56% (109). The pooled "55%" in Answer 3
is therefore fine for a ball at the 1.

**Overall:** the rules content is accurate and unusually complete for a Level 1 chapter. The clock
section, the in-or-out corner figure and the 13-seconds film room are what a coach would teach. The
football problems are in the **player diagrams**: the goal-line defense (Fig 14) is not one any staff
would line up in, two scoring-card spots are illegal, the two-minute coverage advice in Answer 2 is
backwards, and Fig 3 implies receivers keep fixed splits regardless of the field. There are also a
few missing rules a coach would insist on (missed-FG spot, choosing the try spot, fumble out of
bounds late, when the two-minute warning actually happens).

---

## A. Must fix (wrong or misleading football)

1. **Answer 2: the late-game coverage advice is backwards (qmd l.1306–1310).** The beginner review
   flagged the logic; here is the coaching version. A defense ahead by 4 with 3:12 left, against an
   offense with no timeouts, plays **outside leverage and keeps everything inside and in front**. The
   corners and the flat/curl defenders sit on the sideline throws (in Cover 2 the corner sinks and
   squeezes the out; in man the corner aligns a yard outside the receiver). They concede the
   middle-of-the-field completion, because the tackle keeps the clock running. Rewrite: "You'll see
   defensive backs line up *outside* their receivers in this situation, taking away the sideline and
   conceding catches over the middle, where a tackle keeps the clock running." Also add a sentence:
   **with 3:12 left the offense still has the two-minute warning to come, a free fourth timeout.**
   Coaches count it as one, and it is the next thing a play-caller thinks about here.

2. **Fig 14 (Predict 3): the goal-line defense isn't a real goal-line defense.** It is the `46` front
   with a `zero` shell (l.1320). That puts **both corners about 6 yards deep in the end zone and
   split wide with no receiver to cover**, the FS 6 yards deep, and the SS about 5. On fourth-and-goal
   at the 1 against 23 personnel (U, Y, wing H, F, T), nobody is deeper than about 4 yards, and the
   corners are not out on air. Draw it by hand with `Player(...)`: a **goal-line 6-2 (or 6-3)**.
   - **Six on the line, every gap filled** from the U to the H wing: a 6-technique over U; A-gap
     tackles in both A gaps (or a 0-tech nose plus two 2i); a 5 or 7 over the right tackle/Y; an end
     outside Y, head-up on the wing H.
   - **Two linebackers at about 2 yards** over the guards (labels M and W).
   - **Three DBs.** One corner (C) about 1 yard off, outside U on the left; one (C or S) about 1 yard
     off, outside the H wing on the right. One safety at about 4 yards in the middle, as the
     "extra" run fitter.
   That is also the picture the caption describes ("the defense has packed the line"). The current
   drawing does not show it. Also give the two defensive tackles a different letter (N/T vs the
   tailback "T"), or relabel the tailback "R" as every other diagram does.

3. **Fig 4 (scoring card): the two-point try is spotted outside the hash marks.** The ball is at
   y = 14 (l.567), about 10 yards outside the near hash. The chapter just taught that every
   scrimmage play starts on or between the hashes, and the try is a scrimmage play. Move it to between
   the hashes (e.g. `MID - 2`). Then shorten the purple arrow or nudge the TD run up so they don't
   collide. The TD run's ball (y = 42) is also outside the hashes. That is acceptable if it shows a
   ball carrier mid-run, but start the line at a hash-legal spot, or say "a run" in the badge, so it
   doesn't read as a snap spot.

4. **Fig 3 (hash comparison): "same splits" teaches something no receiver does.** In the
   high-school panel X is 3 yards from the sideline, and in college 5. Real receivers align by
   **landmarks**, not fixed distances from the ball: "on the numbers," "two outside the numbers," and,
   to the boundary, **never closer than about 6–7 yards to the sideline** (so he has room to run an out
   or a fade). On a college or HS field the boundary X **cuts his split** and the field receivers widen.
   Either:
   (a) keep the fixed splits but add to the caption: "Real receivers would adjust. The boundary X
   would cut his split in to stay about 6–7 yards off the sideline, which squeezes the whole
   formation. Either way, the space on the short side is what changes"; or, better,
   (b) align X to `max(15, ...)` so he sits 7 yards from the sideline in every panel, and annotate
   how much tighter he is to the ball. That is the real consequence of wide hashes: a cramped
   boundary formation.
   Drop the caption line "he is almost standing on the sideline" either way.

5. **The trailing-defense sentence (l.1027–1029) is garbled. Replace it with the real concept.** A
   trailing defense *wants* the clock stopped, so in the extreme it will **let the offense score**
   to get the ball back with time left: Mike Holmgren's Packers let Terrell Davis score in Super Bowl
   XXXII, and Bill Belichick's Patriots let Ahmad Bradshaw score in Super Bowl XLVI. The mirror image
   is the leading offense's **ball carrier going down short of the goal line** to keep the clock
   running (Brian Westbrook, Eagles at Dallas, Dec. 2007). Both are memorable and correct, and they
   make the clock logic concrete. (Send these to the fact-checker; I'm confident of all three but
   they need cites.)

## B. Missing rules or nuance a coach would insist on

6. **Missed field goal → ball at the spot of the kick** (Rule 11-4-2; at the 20 if the kick was
   from inside the 20). This belongs in "Field goal" and in the Possession list ("The offense loses
   it"). It is half of the 7-vs-3 and 4th-down math: a missed 53-yarder hands the opponent the ball
   at the 43, not the 35. Fig 7 already has a "Missed field goal" bar (2.6%), which the text never
   explains.

7. **The two-minute warning is not "when the clock passes 2:00".** It comes at the end of the last
   down snapped *before* 2:00 (Rule 3-41, which the chapter's own footnote quotes). If the snap is at
   2:04 and the tackle at 1:57, the warning comes after the play. That's why offenses try to get a
   snap off just before 2:00 and why defenses sometimes slow the substitution. Fix the glossary entry
   and l.879: "after the last play that started before 2:00."

8. **Two exceptions to "every play starts on the hash where the last one ended."** On the **try**, and
   after a **touchback**, the offense may place the ball **anywhere on or between the hashes** (Rule
   11-3-1(a); touchback, Rule 11-6-3). That's why the PAT is usually snapped from the middle or the
   kicker's preferred hash, and why a two-point play is often snapped from a hash on purpose. One
   sentence in "Hash marks" or "The try" covers it. It also fixes the implication in the "Kickers"
   bullet that kickers live with whatever hash they get. On a field goal the offense can't move the
   ball, except by running a play to center it, which some college teams do on third down.

9. **Fumble out of bounds restarts the clock on the ready signal, even late** (Rule 4-3-2-f). This is
   the one out-of-bounds ending the late-half exception doesn't protect, so a team can't fumble forward
   out of bounds to save time. Use it as a footnote on the out-of-bounds bullet or the Fig 9 caption.
   Also: the 10-second runoff (l.977–980) can only be charged against the offense, the team trying to
   save time (Rule 4-5-4 Note 9, 4-7-1). Say "a team trying to save time" → "the offense".

10. **Field/boundary is mostly a college dialect; the NFL leans on strength.** The "Defense" bullet
    (l.462–466) is right about field and boundary corners. A coach would add *who* plays them. In
    systems that flip by the hash (most of college, and the Saban/Belichick tree in the NFL), the
    **boundary corner is the bigger, press-and-tackle player**, because the short side gets the force
    and run-support duty, and the **field corner is the better space cover man**. The safeties split
    the same way: the boundary safety is the down/run player, the field safety the range player. Many
    NFL defenses instead set the call to the **formation's strength** (the TE side or the side with
    more receivers) because the hashes are so narrow. That ties straight into the chapter's
    college-vs-NFL point. When the ball is in the middle (l.450), the usual default is "to the
    passing strength (the side with more receivers)". "Strong side" is ambiguous until 02-02.

11. **Fig 1 is missing a real marking: the direction arrows.** Next to each number except the 50 is a
    white arrow pointing toward the nearer goal line (Rule 1, field-markings item 9). On a broadcast
    it is the fastest way to tell which side of the 50 the ball is on. Since the figure claims "every
    marking labelled," add the arrows (a small triangle beside each number) and a callout. Minor:
    real numbers are painted with their bottoms toward the sideline, so the far row reads upside down
    from above. The text uses "tops of the numbers" as a landmark, so drawing the far row rotated
    180° would make "top" unambiguous.

12. **Possession bullet on punting (l.789–790)** says a team punts "because it doesn't want to risk
    failing to keep the ball deep in its own territory." Teams punt from anywhere outside field-goal
    range. Better: "by punting on fourth down, trading the ball for 40-odd yards of field position
    rather than handing it over at the line of scrimmage."

13. **Chiefs film room: name the squib kick.** "A short kick to make Kansas City return it" is the
    **squib kick**, the term every broadcast used that week. Also add "(the touchback was the 25 in
    2021; it is the 35 now)" (beginner item 5); a coach would add it too, because the 10 yards matter
    to the arithmetic of 13 seconds. On the coverage: Buffalo played soft zone and let Hill (crossing)
    and Kelce (seam) find the middle. With KC holding two timeouts, in bounds didn't matter, so the
    defense's only job was to **take away the 20-yard middle throws**, which is the opposite of the
    usual late-game rule. That is a good contrast with Answer 2 and worth one sentence.

## C. Diagram details (alignment, routes, labels)

14. **Fig 13 (Predict 2): Z runs through his corner and the defense is static.** The right corner
    (C) is head-up on Z at 7 yards, and Z's stem passes straight through his square. Given A1, align
    this corner **a yard outside Z at about 6 yards** and give him a short path driving on the out, so
    the catch happens in front of him at the sideline. That matches the situation and the corrected
    answer. Also:
    - **A 9-yard out is not a "quick out"** (that's 5–6 yards, on three steps). Call it "a 9-yard out"
      in the caption.
    - **The nickel shell leaves the left slot H uncovered** while W sits in the box. Against 2x2 a
      nickel defense walks the W (or the SS, in a single-high look) out to an apex over H. Move W to
      about (4.5, H.w + 1.5).
    - Label nit: the "Q4 3:12" box sits over the FS's deep-left area. It doesn't touch anything now,
      but keep it there if FS moves.

15. **Fig 10 (two clocks): the ball arrives at the sideline, not at the catch point.** In the out panel
    the dashed ball path ends at X's final spot after the run-after-catch, on the sideline, while the
    caption says "caught at +12." Throw to the catch point: shorten `t`, or pass to the end of the
    route, not the run. Then X's dark RAC arrow carries him out of bounds. Also:
    - A 12-yard out is a **deep (or "speed") out**. Fine, but the title could say "Deep out to the
      sideline" for accuracy.
    - The two "C"s (center and corner) share a panel. Use the book's 01-03 table (corner = C) and
      leave the center unlabeled here, as Fig 3 effectively does.
    - The "40" field number at the top of each panel sits under the note box and is half hidden.
      Hide it, as Fig 3 does, or move the note.

16. **Fig 12 (Predict 1): "three receivers to its left" includes an attached TE.** In `gun_trips`, Y
    is in-line at 4.8 yards, so this is 3x1 with the tight end attached ("trips TE"), not three
    wideouts. Either change the caption to "two receivers and the tight end to its left," or detach Y
    (`d = OFF_BALL`, w ≈ 7) so it reads as true trips. The answer's "room to spread out" logic fits
    detached trips better. Alignment check: Z is 12.7 yards and X 8.6 yards from their sidelines.
    Both are realistic, and the line is legal (seven on the line: Y, five OL, X).

17. **Fig 2 (in or out):** correct as drawn. Optional nuance for case 4: the ball must cross the plane
    *inside or over* the pylon. A ball that crosses the goal line extended outside the pylon is out
    of bounds, not a touchdown. One clause in the key would head off the most common replay argument.

18. **Fig 4 (scoring card):** the FG geometry (LOS at the opponent's 35, hold at the 43, 53 yards) and
    the PAT (snap at the 15, hold at the 23, 33 yards) are right. Apart from item 3, the safety
    vignette works, but the ball carrier's "R" goes unexplained. An unlabeled circle reads fine.

19. **Figs 1, 5–9 and 11** are accurate, with no clipping or collisions. The game-shape, clock and
    drive-outcome figures say nothing a coach would argue with. On Fig 9, the "under 5:00 in the 2nd"
    wording should say "2nd half" (beginner item).

## D. Smaller accuracy and wording points

20. **Hook (l.188):** "Two minutes left in the first half": make it "Ninety seconds left." At exactly
    2:00 the warning is pending. The out-of-bounds stop only lasts until the snap after the warning,
    so the scene should be clearly after it.
21. **"The boundary corner can play more aggressively, because the sideline guards half of his
    space"**: "half" overstates it. Use "because the sideline takes away his outside."
22. **Safety (l.708–711):** "often around midfield" is optimistic. A safety free kick from the 20
    usually gives the scoring team the ball around its own 40, or a bit better with a return. Say
    "usually near its own 40."
23. **Timeouts job 3 (l.1058–1059):** icing is correct (one per kick; the second is
    unsportsmanlike and ignored). A coach would add that the **offense** also uses "job 2" timeouts
    to get out of a bad play against an unexpected front. That's already implied; fine.
24. **Kneel-down arithmetic (l.1087–1090):** three kneels drain about 2:00 **only if the defense has
    no timeouts**. Each defensive timeout gives back about 40 seconds. The next sentence implies this;
    make it explicit ("…if the other team is out of timeouts").
25. **LIX film room:** accurate. Optional: one line on *why* the Chiefs' drives stalled (Philadelphia
    pressured Mahomes all night rushing only four, per FACTS). The "stalled" framing invites the
    question, and it is a nice teaser for the pass-rush chapters.

## Verdict

Fix A1–A5 (the Answer 2 coverage logic, the goal-line defense, the illegal try spot, the Fig 3 split
caveat, the garbled trailing-defense sentence) and add B6–B8 (missed-FG spot, two-minute warning
timing, choosing the spot on tries and touchbacks). Everything else is polish. No gridiron changes are
needed; the Fig 14 defense should be built with explicit `Player(...)` objects in the chapter.
