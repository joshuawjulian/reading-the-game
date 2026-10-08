# 11-02 coach / film-analyst review: 1978 and the Passing Revolution (1978–1999)

Reviewer role: veteran NFL coach and film analyst. Scope: technical accuracy, diagrams, animation timing, and film-room choices.
I rendered `pdfs/11-02-the-1978-liberation.pdf` (22 pp., current with the .qmd) at 80 dpi, made 160 dpi crops of Figs 4 and 7, and looked at every figure (Figs 1–11).
New number computed for this review: the 2025 no-huddle rate from FTN charting (`load_ftn_charting([2025])`, `is_no_huddle`) is **7.8% of 47,316 charted plays**.

**Verdict:** a strong history chapter. The 1978 rule mechanics are explained correctly: contact inside 5 yards only on a receiver in front of the defender, hands-off past 5 until the throw, and extended arms with open hands. The Coryell digit call matches 04-08 (X–Y–Z order; 8 post, 9 go, 6 dig). The 46 plate matches 05-02 exactly: weak end, 3-0-3 bear, W inside and S outside Y, Mike over the right tackle, SS over the left tackle. The counter trey assignments are right: G kicks out, T wraps, the playside blocks down, C blocks back. The H-back answer in Drill 1 is how Gibbs actually used the position.
None of the problems below is a structural blocker. The ones that matter are one wrong present-day claim, one caption that contradicts its own animation, two diagrams whose geometry undercuts their point, and some missing nuance on the 46 counter.

## Must fix (accuracy)

1. **"Watch for it", last bullet (l. 1360–1362): the huddle has not disappeared, and the season is wrong.**
   In 2025 NFL offenses went no-huddle on only **7.8%** of charted plays (FTN `is_no_huddle`, computed above), so they huddle on almost every play. The fullback is rarer but has not gone either (SF, BAL, MIA, DET still use one).
   Today is Oct 2026, so the reader is watching 2026 games.
   Fix: "Then flip to a game from this season… Note what has faded (the two-back pro set, the 46, the seven-step drop) and what survived (the slant-flat, the counter, the stand-up edge rusher, the zone blitz). The huddle survived too: NFL offenses still huddle on more than nine plays in ten."

2. **Fig 7 (46 counter), panel 4 note (l. 1068): "W and S are chasing from behind" is false in the animation.**
   Y hinges on W and holds him at the line (W never leaves the LOS in panels 3–4). Only S, the unblocked backside 9-technique, chases.
   Fix the note: "T has M. Only FS is left; Y has W, and S chases from the backside." Also fix the caption's last sentence ("the stacked linebackers chasing from the far side") and the body text at l. 997–998.

3. **"Where the era landed" (l. 1271–1272): "Three champions, three lines of descent".**
   The 1998 Vikings weren't champions; they lost the NFC title game. Their offense (Denny Green, Brian Billick) was also Walsh-tree, not Coryell. And Denver's outside zone did not descend from "the run game that the one-back offenses had rebuilt": Alex Gibbs's zone came from a different line (see 03-02).
   Fix: "Two champions and a record-setter, and every line of descent from 1978 is in them: Walsh's timing game married to Alex Gibbs's zone running in Denver, a Walsh-tree offense with a vertical threat in Minnesota, and Coryell's vertical game in St. Louis."

4. **Salary cap (l. 1220–1221): "signing bonuses are spread across the years of a contract so they can't be hidden."**
   Any cap analyst would say it's backwards. Proration is the main tool teams use to *push* cap charges into later years (restructures, void years). It doesn't stop hiding.
   Fix: "signing bonuses count against the cap spread evenly over the contract's years (up to five), which also became the tool teams use to push cap charges into the future." (This ties neatly into the Denver paragraph.)

5. **Drill 2 answer (l. 1441–1442): "…or a run against a defense with only four defensive backs spread across the field".**
   This is the wrong half of the K-Gun logic. Base 3-4 personnel is *built* to stop the run, so against base the K-Gun threw. It ran Thurman Thomas (draws, trap) when the defense had subbed to nickel or dime.
   Fix: "Expect a quick throw to H… Had the defense subbed to nickel before the drive, the call flips: Kelly hands to Thurman Thomas against a lighter box. That is why there was no right package to start in." That also sets up the Belichick answer better.
   In the figure, change the label "no huddle: the defense cannot substitute" (l. 1428) to "no huddle: no time to substitute". A defense *may* substitute; the problem is that the offense won't wait.

6. **Film room, Epic in Miami (l. 728–731): "both teams were playing the 1970s way… on almost every throw nobody is allowed to [collide]".**
   By January 1982 defenses had played three seasons under the rule, and Miami's coordinator was Bill Arnsparger himself. "Playing the 1970s way" mischaracterizes the film.
   What the viewer *will* see: base 4-DB defenses with a linebacker or safety matched on Winslow wherever he aligned, and the Dolphins changing who covered him.
   Fix: "Then notice the defenses: still mostly in base with four defensive backs, so wherever Winslow lines up a linebacker or a safety has to cover him past five yards, where he can't be touched. That mismatch is the rule change on film."

## Diagram fixes

7. **Fig 4 (West Coast slant-flat): the Will runs *through* the throwing window.**
   W starts at (4.5, −3.0), inside the box over the left guard/tackle, and drops to (3.0, −11.0). His path crosses the slant's catch point (~w −8.5, 5–6 yd) and the brown pass line. In the image the W arrow and the ball path visibly cross. The ball is thrown at t=0.8 s, when W is at about w −6, i.e. *in* the window, not outside it. A coach would say the drawing shows the QB throwing into the Will.
   Fix: align W as the weak apex/curl-flat player, wider and shallower: `D("WILL", "LB", 4.5, -7.0, "W")` (override after `era_43`) dropping to `(3.5, -12.5)`. Keep the slant's break inside him: X route `[(0,0),(1.5,0),(6.0,-5.5)]` ends at w −7.5. Then the window opens inside W as he widens. Use `pass_to("X", t=1.0)` to match the caption's "about a second".
   Also: the caption says "the fullback (F) … block[s]", but F has no block drawn. Add `p.block("FB", pts=[(1.0, 0.8)])` (step up to the B gap).

8. **Fig 5 (the 53): two standing edge players contradict the text's "four rushers or three?".**
   The weak-side "L" stands on the LOS at (1.6, −6.6), outside the left tackle. That makes the picture a generic Okie 3-4 with two ambiguous edge players, and the text says there is one.
   Matheson's 53 was 4-3 personnel with one LB at the strong-side DE spot: the other three linebackers were off the ball.
   Fix: move WLB off the ball to `(4.2, -5.0)`, which gives three off-ball linebackers (Will, plus the two "L"s) and one standing edge player (53), as the text describes. Optionally relabel the three off-ball players W, M, S.
   The "three linemen with hands down" label sits directly above that weak L, and its leader goes to the left E. A reader thinks the L is one of the three. Once the L moves the problem mostly goes away. Better still, bracket the three down linemen or ring them faintly, and move the label to (−3.4, −8.5) behind the line.
   The "or drop" label (10.8, 2.6) is ~4 yd inland from the drop arrow, which ends at (7.6, 9.6). Move it to about (9.6, 8.2) so it sits on its arrow (stay ≥1.5 yd inside the 14.5 window top).

9. **Fig 7 (counter trey vs the 46): the defense is too passive, and that flatters the scheme.**
   Defensive line speeds are 1.0–2.0 yd/s, so the bear front barely moves. Ryan's front slanted and penetrated. Against a pulling guard, the backside 3-technique (ST) is the man who wrecks counter by chasing through the vacated B gap.
   The text already says the center's back-block is "the hardest block on the play". Show it: give ST an inside slant into the RG's vacated gap, `go_to(p, "ST", (0.6, 0.6), kind="rush", speed=3.0)`, and let C meet him there. The point (C must cut him off, or the play dies from behind) is then visible.
   **Add the nuance (l. 1000–1005).** The bear front is hard on gap schemes generally, because every interior lineman is covered and a pulling guard leaves a penetrator. Teams that ran counter at the 46 often pulled the guard with the **H-back** wrapping (GH counter) instead of the tackle, so the backside tackle could down-block the 3-technique. 03-03 already mentions the H-back lead version; link it.
   Add one sentence that the more famous 46-beater was spreading out and throwing quick: the Dolphins' Dec 2, 1985 MNF win, which 05-02 already tells in full (`fig-46-quick`). Link it, so readers don't come away thinking the counter trey was *the* answer.
   **QB action:** Washington's QB carried out a boot fake away from the counter, to hold the unblocked backside end (here S). A coach would add the QB's fake path, e.g. `go_to(p, "QB", (-5.0, 4.0), kind="path", delay=1.1)` after the handoff. Mention it in the text.
   **Moment 3 timing:** at +1.2 s ("pullers arrive") the kick-out guard is still ~2 yd behind the LOS and hasn't reached E, yet the note says "G kicks out E". Move moment 3 to about 1.6 s.
   **Label collisions:** blocks end with markers stacked on top of each other: "E" over the ringed "G" in panel 4, "N" over "G" and "T" over "T" in panel 3. Offset each block end point ~0.8 yd short of the defender's spot so the markers touch rather than overlap (LT, LG, RG and H end points), per convention (d).

10. **Fig 3 (Coryell 896 vs Cover 2), minor.**
    The corners start at 6.5 yd and "drop" *forward* to 5.0, which looks like a blitz. Cover 2 corners show at 5 yd and squat or sink. Fix: align LCB/RCB at (5.0, ±14.0) and drop them to (6.5, ±15.0), sinking toward the flat/hole.
    Coaching nuance for the body text: in Cover 2 the Mike is taught to carry or wall the #2 vertical (Y's seam). "Splits the safeties" works because the Mike can't run with Winslow after 5 yards, and that is the chapter's whole point. Say so in one clause; it also previews the Tampa 2 answer in Drill 3.

11. **Drill 3 (Fig 11) vs its answer.**
    The strong end (SE, `T("5")+0.2`) is drawn essentially on Y's nose, but the answer says "nobody touched Y at the line." Either move SE inside to a true 5-technique (`T("5") - 0.4`) or change the answer to "if Y gets a clean release…".

12. **Fig 1 (Blount rule), cosmetic.** "hit 1" (2.6, 9.0) sits beside the Sam rather than at the X on Y's release, and in the right panel "hit" is likewise 4 yd away from its X. Move both to about (1.2, 3.4), just inside the contact.

13. **Notation consistency (Drill 2).** "H" is the H-back in Figs 7 and 9 and the slot receiver in Fig 10. The caption explains it, but say "(H, here the slot receiver)" in the drill text, since the chapter just spent a section defining H-back.

## Missing nuance a coach would add (short, optional)

- **The Blount rule (l. 407–411).** Today's illegal-contact restriction applies only while the passer is in the pocket with the ball. Once he leaves the pocket, downfield contact is no longer restricted to 5 yards. One clause, with a link to 09-03, saves a reader from calling a phantom foul on scramble drills.
- **The West Coast section (l. 773–789).** The quick slant is a fine entry point, but Walsh's signature was the **five-step timing drop with high-low progressions and backs as primary receivers** (the halfback option, "Spider 2 Y Banana"). Add one sentence so readers don't equate the WCO with the three-step game, which every offense had. Optional trivia: the label "West Coast offense" came from a reporter's misattribution; Walsh said it originally described Coryell and Gillman's San Diego offense. (Fact-checker: verify before using.)
- **SB XXV film room (l. 1127–1129).** Belichick's plan is usually described as playing with **only two down linemen** much of the game (two DL, four LB, five or six DBs) and as hitting Buffalo's receivers on every legal opportunity. Naming the two-man front makes "extra defensive backs" concrete and is something viewers can spot on film. (Fact-checker: verify against the SB XXV page or Halberstam.)
- **Free agency (l. 1207–1209).** "Younger players are restricted" compresses two categories: players with three accrued seasons are restricted free agents, and fewer than three are exclusive-rights free agents. Also, the 1993 system first required five accrued seasons for unrestricted free agency (fact-checker: confirm).
- **SB XXII film room.** Denver was in Joe Collier's 3-4, which is why a counter that kicks out an edge player and wraps a tackle onto a linebacker gashed it. One clause would connect this film room to the previous section.

## Checked and correct (no change)

- The 1977/1978/1979 rule descriptions, the head slap, the side judge's purpose, and the "Ty Law" 2004 re-emphasis.
- The blind-side geometry in Fig 6: a right-handed QB opens right on the drop and turns his back to the left. The wedges are oriented correctly. The LT and the rusher are ringed and none of the labels are clipped.
- The 46 alignment in Fig 7 matches 05-02's plate. Counter assignments (G kick-out, T wrap to M, LT/LG down, H on the box safety, C back, Y hinge, backside 9-tech unblocked) are as Washington drew them.
- Drill 1 (H-back to the blind side to chip and release, travelling in motion if 56 flips) is exactly right, and so is the Tampa 2 follow-up in Drill 3.
- The chart and the timeline: labels are clear, nothing is clipped, the numbers match the fact-check.
- The animation count (1) and the frame strip both tell the story in print. Fix the panel 4 note (item 2) and the moment 3 timing (item 9).
