# 07-02 Blitzing — coach / film-analyst review

Reviewer stance: veteran NFL defensive coach + film analyst. Checked against the PDF
(`pdfs/07-02-blitz-and-man-pressure.pdf`, rasterized at 80 and 130 dpi; all 11 figures inspected).

**Overall verdict:** strong chapter. The voice, the blitz-math framing, the "the protection chooses
who is free" idea, the overload pair (Figs 3–4) and the data section are excellent and match the pilots.
But there are **rusher-count errors in two diagrams that run into the opening story and the payoff**, a
claim the chapter's own data contradicts, and one protection drawn the way no line coach would teach it.
Fix the MUST items before shipping.

---

## MUST fix (technical errors)

### 1. Fig 6 (mug), variant 2 is six rushers, not five, and Cover 0, not Cover 1. This runs into the opening and "Back to the opening play"
- In the code, `dl_rush(p)` rushes 4 DL, the **Will rushes**, and the **nickel rushes** (red dashed). That makes **6 rushers**.
  The caption ("Five rushers") and the panel note ("5 rush") are wrong.
- Coverage left: CB, CB (off frame), SS on Y, **FS rotates down to H**, and Mike drops to the hole. **Nobody is
  deep.** That is Cover 0 with a hole player ("zero lurk / 0 hole"), not Cover 1.
- The opening ("five rushed, not seven") and "Back to the opening play" ("a five-man pressure with Cover 1
  behind it") both inherit the error. The opening also has "a safety creeping down from 12 yards toward the
  slot", which matches the FS rotating down, so nobody is left deep.
- **Recommended fix (keeps the story and makes it coherent):** call it **six rushers, Cover 0 with the dropping
  mugger as the hole/lurk player**. Redraw variant 2 so that:
  - **R (aligned right) steps up to the Will in the right A gap** (his side), and
  - **C is set on the Mike (left A gap)**, who drops. The center is left blocking air. Show his bar stopping at
    about (-1.5, -0.6), with a tiny "C: his man dropped" label if there is room.
  - **NB comes free off the far (left) edge.** No interior blocker can reach him.
  - Text: "Six rush against six blockers: no free man by arithmetic. But two blockers were tied to two
    muggers, one of them dropped, and the man who came free was a defensive back from outside the box. By
    most protection rules that rusher is the **quarterback's** (he is "hot" off him), which is why the QB
    never looked at him." This is also what makes "left unblocked *on purpose*, by the offense" in the
    opening literally true.
  - Opening: "six rushed, not seven". Back-to-opening: replace "Five rushers against six blockers… with the
    back stepping up to the linebacker in the A gap and the center on the other one" with the sentence above.
    As written, the center is "on" a linebacker who dropped, so it doesn't parse.
  - Alternative if you want to keep "five-man pressure / Cover 1": both muggers drop, the NB comes, and the FS
    stays deep. But then nobody covers H (the NB's man) unless a mugger walks out to him, which spoils the
    story. The six-man version is cleaner.

### 2. Fig 6 variant 1 ("Both go"): the back crosses the QB's face for no reason
- R is aligned to the right of the QB and the Will is in the right A gap. The drawing has **C take the Will
  and R cross the QB's face to the Mike** (left A). No line coach teaches that. In man/BOB protection against a
  double-A mug, **the back takes the A-gapper on his side, and the center takes the other one** (or the center is
  "pointed" away from the back). Predict-the-play 2's own answer says "keep the back in to check the A gap on
  his side", so the chapter contradicts itself.
- Fix: `to(p, "C", (-1.6, -0.6))` onto the Mike, and R steps straight up into the right A gap onto the Will
  (about (-3.0, 0.8), no `via`). Change the label to "R must take a LB head-on in the A gap". The real difficulty
  is a 210-lb back meeting a downhill linebacker in the hole, not a crossing path. Update the caption the same
  way ("the back has to take the other head-on, in the A gap on his side").

### 3. Fig 5 panel 3 (edge pressure): six rushers drawn, note says 5, and two DL in one gap
- Rushers in code: LE, 1-tech, 3-tech (`short_rush`), RE (slant), W (edge), NB (free). That is **6**. The note
  "5 rushers" is wrong.
- With six blockers, the free NB only exists because the protection is a **half-slide left**: C, LG and LT
  have just the LE and the 1-tech (an idle blocker), while RG, RT and R face 3-tech, E, W and NB (4 v 3). So this
  is an edge **overload on the man side**. Say so in the note and the caption: "6 rush; the slide went left,
  so it is 4 v 3 on the man side, and the free man is the widest".
- **Gap integrity:** the 3-technique rushes into the right B gap (ends at about (-0.1, 2.6)) and the RE also
  slants into the B gap (to (-0.6, 2.9)). Two rushers in one gap is unsound against the rush (they collide)
  and against a run or draw. Fix: **slant the 3-tech into the A gap** (end at about (-0.2, 0.9)) as the "tackle
  in, end in" partner, or start him as a 2i. Then the RE's B-gap slant is clean.
- Also soften "the tackle follows him (he has to…)". Against slants, linemen are taught to **pass off**: the
  tackle passes the slanting end to the guard and takes the edge man, which is exactly what a slide does. Edge
  pressure works when the guard is occupied (here by the 3-tech) or the protection is man-side. Add one clause
  saying so.

### 4. "Almost all blitzes travel with man coverage" is contradicted by the chapter's own number
- The rendered text says man coverage on **60%** of blitzes, so 40% of NFL blitzes are zone. Fire zones (five-man,
  three-under/three-deep) are the most common five-man pressure for a large part of the league.
- Fix: "Most blitzes travel with man coverage… defenses played man on 33%… and on 60% when they sent five or
  more. The rest are zone blitzes (07-03)…". Keep the "roughly doubles" line.

### 5. Predict-the-play 3: wrong coverage count and wrong blocker count
- Answer: "Six blockers against seven rushers… **with five defenders in man on four receivers**". If seven rush
  (4 DL + M + FS + W hug), only **four** are left (2 CB, NB, SS) on four receivers (X, Z, H, Y). Fix: "four
  defenders in man on four receivers, nobody deep, nobody spare." (Five on four is the six-rusher case: the
  Will stays on the back.)
- Caption: "six potential blockers, five eligible receivers". **Y is an attached TE**, so the offense has
  **seven** potential blockers (5 OL + Y + R). Fix the caption to "up to seven potential blockers (the line, the
  tight end and the back)", and add one line to the answer: "keep Y in too and it is seven on seven with
  three receivers out, which is max protect against zero, with no margin either way".
- Picture: M and FS at 4.2 yds are at linebacker depth, not "walked up". Move them to about 2.0 yds (d=2.0) or say
  "creeping over the guards".

### 6. Fig 1 legend conflict: the Will's hug is drawn as a dashed orange line, which the legend defines as "dropping into coverage"
- Either draw the hug as a **solid orange arrow with alpha about 0.5** (a conditional rush), or add to "How to read the
  diagrams": "a faded or dashed orange arrow is a conditional rush (only if his man blocks)". The caption's
  "(dashed)" alone fights the legend.

---

## SHOULD fix (diagram realism / misleading details)

7. **Fig 2 (Cover 0 v empty): the unblocked end's path loops outside.** `dashed(...)` goes (1.0, 5.4) → (-1.6, **6.5**)
   → (-4.6, 5.0) → (-6.4, 1.2). An unblocked rusher takes the shortest path to the launch point; Y has released.
   Use (1.0, 5.4) → (-2.8, 4.0) → (-5.8, 1.0). That also makes "~2 s" honest. A free edge rusher from a wide 5
   gets home in about 1.6–1.9 s, so say "under two seconds" in the caption, the point_to label and the text.
8. **Fig 2: the H out is too shallow for third-and-4.** The break at 4.5 yds drifts back to 4.2, which puts the catch on
   the sticks while going out of bounds. Coaches run it at "sticks + 1 or 2": `p.route("H", [(0,0),(6.0,0),(5.8,4.0)])`.
9. **Fig 2 caption/label: "line blocks inside-out, man on man".** The RT is blocking the 3-tech and the RG the Will, so
   this is a **gap/slide inside-out** protection, not man. Drop "man on man".
10. **Fig 2 cushions:** NB, SS and FS sit at 5.0 yds in Cover 0 on third-and-4. That concedes the sticks. Many zero teams play
   tighter (2–3 yds, inside leverage) or press. Either tighten them to d=3.0, or add the nuance in the text:
   "zero press" (deny everything, live with the fade) vs "off zero" (cushion against the fade, rally to the short
   throw), both common.
11. **Fig 4: the throw lane runs straight through the Will/back collision** (the brown dashed line passes over W's ring
   and R's block bar). Flatten Y's slant so the ball goes through the B/C gap window: end Y at about (5.0, 5.2)
   with via (1.8, 8.6), and keep `pass_to t=1.1`.
12. **Fig 5 panel 1 (cat blitz): the right slot Y has no defender.** M and W stand idle, the SS rotates to H and the FS
   goes to the middle. Draw `p.man("WILL", "Y")` (or have the Will walk out over him) and `p.man("MIKE", "RB")`.
   A linebacker on a slot is the real cost of a nickel blitz from 2x2 and deserves a phrase in the note ("…and a
   linebacker ends up on the slot").
13. **Fig 5 panels 2 and 4: the hug rule is ignored.** In panel 4, `p.man("WILL", "RB")` is drawn, and R stays in to block the
   Mike, so by the chapter's own rule the Will hugs and it is 7 v 6. Either note "(7 with the hug)" or make
   the Will a hole/robber player and drop the man line. Panel 2: draw NB→H and W→RB man lines and make the same
   note, or the plate looks like defenders standing around.
14. **Fig 5 panel 4 (bear):** R, aligned right, must cross the formation to the Mike's left C gap. That is fine, and it is
   the point (the back's long trip), but say it in the note ("the back has the sixth, and a long way to go").
15. **Fig 6 panel 3 ("Both drop"): "C and R block nobody".** In most protections the back **check-releases** when his
   man drops, and the center helps. Change the label to "C helps; R checks, then releases". The check-release
   outlet is the offense's real answer to "both drop" and links back to 04-02.
16. **Predict-play 2 answer:** "plan to throw to the side the free rusher would come from if both linebackers
   come". If both come, it is 6 v 6 and nobody is free by arithmetic. The free man appears only if a seventh (the
   NB) comes, and then the hot is **H, the nickel's man**. Reword: "…and know his hot: if the nickel comes too,
   H is open as soon as he turns."
17. **Predict-play 2 caption:** "a safety down over the right slot at eight yards". Eight yards is not "down". Say
   "a safety at eight yards over the right slot" or move him to d=5.

## Label collisions (print)
- Fig 6 panel 2: the "M drops / to the middle" label sits on the FS's dashed rotation line. Move it to about (7.0, 1.2).
- Fig 5 panel 1: the "SS takes H" label sits on the SS's dashed path. Move it to about (8.0, -10.6) or (7.6, -3.6).
- Fig 3 strip, frame 5: the SS square overlaps R's purple ring. Frame 6: the E square covers the "RT" label. Both are acceptable in
  motion. For print, consider ending the SS at (-2.6, 6.9) so the pair separates.
- Fig 7: the "MIN 2023" label touches the dashed fit line. Use xytext (-7, -14).
- No field-edge clipping found in any figure.

## Missing nuance a coach would insist on (add a sentence or two each)
- **"A DB from outside the box is the quarterback's."** Most protections count the box, and a nickel, corner or
  safety blitzing from outside it is the QB's to beat (hot / sight adjust). This one rule makes the cat blitz, the
  opening play and "unblocked on purpose" fully coherent. Put it in Blitz math or the nickel paragraph.
- **The peel rule.** Man-pressure rushers whose assignment includes the back must **peel** with him if he releases
  (swing, wheel, angle). The RB swing/wheel against a blitzing LB is a classic blitz-beater. One sentence in
  the Cover 1 section next to the hug rule.
- **Terminology dialects box.** Hug = "green dog" / "add-on" (06-02 uses "green-dog"). "Dog" = linebacker blitz,
  "fire/plug" in some systems. **"Cat" is the corner blitz in many playbooks** ("cat/cougar"), while the nickel
  is "nick", "star" or "cat" depending on the staff. Keep the spec's "nickel (cat)" alias, but add "in other
  systems 'cat' means the corner".
- **Rush-lane integrity and contain.** Six- and seven-man pressures still assign contain and stay gap-sound against the run
  and the draw. Mention it in the Cover 0 "what it gives up" or the edge paragraph, especially against a mobile QB.
- **Blitzer technique in one line.** Time the cadence (creep, don't sprint early), get skinny through the gap, aim
  at the QB's launch point. Against the back: a two-way go, so the back wants to meet him in the hole and not wait.
- **Mug: dummy calls.** Centers and QBs use fake points and "check-with-me" Mike calls precisely because the
  defense reads the point. A half-sentence after "the center's point is visible".

## Checked and correct
- Blitz math table; half-slide definition (matches 04-02's glossary); overload count by side (Figs 3–4);
  inside-out rule and "the protection chooses who is free"; Cover 0 inside leverage and the out/fade answers;
  bear front mechanics; safety-blitz timing; edge-pressure weakness (step-up, draw, screen); mug-breaks-the-rules
  section (Mike ID, center, guards, back's eyes); offense-answers table; data narrative (style, not strength;
  stickiness; variance); history (Ettinger/Drulis/Wilson, Ryan/46/Plank, Johnson's tree, Spagnuolo 2007, Rex,
  Zimmer/Guenther with the hedge, Flores). Film rooms are well chosen: SB LVIII late-game zeros show the variance
  cleanly, and the Vikings three-game "dial" is excellent teaching. (Leave the specific play facts to the
  factcheck pass.)
- Only one animation (the overload strip). Frame timing is plausible: Will walks up in about 1.5 s pre-snap and arrives at
  1.45 s, and the strip tells the story in print.
