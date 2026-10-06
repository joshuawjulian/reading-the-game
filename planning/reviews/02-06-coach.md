# Coach / film-analyst review: 02-06 Motion and Shifts as Weapons

Reviewed 2026-10-06 against the current qmd and `pdfs/02-06-motion-and-shifts.pdf` (22 pages, rasterized at 80 and 130 dpi; every figure looked at). Overall: this is a strong chapter. The vocabulary, the travel/bump/spin framework, the "indicator lies" section and the at-the-snap trade-offs are all how a staff would teach it. The fixes below are about football accuracy in three diagrams, two answer keys that overlook defenders, a heading-numbering slip, and some nuance a coach would want added. Ordered by priority.

## A. Must fix (wrong or misleading)

1. **Section numbering does not match the "five jobs" list.** The list has five jobs. The headings are "Job 1", "Job 2", "Job 3: leverage and the running start" (which covers jobs 3 and 4), then "Job 4: stressing the defense's communication", whose first sentence says "The fifth job…". Rename the headings to **"Jobs 3 and 4: leverage and the running start"** and **"Job 5: stressing the defense's communication"**.

2. **fig-jet-vs-man, panel 3 title and caption are wrong at the snap.** At t=0 the ringed corner is at about w=+3.9 and Z at w=+2.6, so both are still on the *right* of the ball. Panel 3 says "Snap: he has crossed the formation", and the caption says "At the snap the corner is on the wrong side of the formation". Fix one of these:
   - Change the panel 3 label to "3 · Snap: he is chasing across, behind Z", and the caption sentence to "At the snap the corner is in the middle of the formation, trailing a receiver who is already at full speed." (Note that he is deeper and *trailing*, not "inside": at the snap he is outside Z in the direction of travel.)
   - Or move the panel 3 time to about 0.3 s.

3. **Jet figures (fig-jet-vs-man and fig-jet-vs-zone): the "lead" running back ends up behind the ball carrier.** In panel 4 of both strips, R is about 1.5–2 yards *behind* Z, so he leads nobody. That is because `jet_offense` starts the RB at (-5, -1.6) at 6 yd/s while Z crosses in front of him at 8.5 yd/s. Pick one fix:
   - (preferred, and what most NFL jet sweeps look like) have the RB **fake inside zone the other way**: `p.run("RB", [(0.3, 1.5), (1.5, 3.0)], speed=5.5)`. Leave him unhighlighted. This also matches the "The jet as a fake" pairing taught two sections later.
   - Or have him **arc** flat and early as a true lead: line him up at w=-1.6 and path him at speed ≥7.5 on `[(-0.3,-4.0),(0.8,-8.0),(2.0,-11.0)]`, so he is in front of Z by about 1.0 s.
   Remove the `# leads for the sweep` comment either way.

4. **fig-numbers (Job 2): Z "zooms" to a wing spot that is inside the shaded box, so the "left: 3 v 2" and "box 5 v 6" arithmetic does not hold.**
   - **Problem 1: where Z sets.** Z sets at w=-5.8, about 2.6 yards outside the LT. That is a wing/flex spot. The shaded box runs to ±6.0, so Z is *inside* it. A coach would count him as a seventh box blocker, not as a third receiver "outside the box", and the Will would simply walk to an apex. Set Z at **(-1.5, -7.5)** (a real #3 in trips) and widen H to -10.5 and X to -16 so the spacing reads as trips.
   - **Problem 2: the box shading.** Draw the box as 02-05 defines it: about 2 yards outside the LT to 2 yards outside the attached Y, so roughly w=-5.2 to +6.8, not ±6.0. Then "left: 3 v 2" and "a linebacker? (box 5 v 6)" are both literally true.
   - The motion-family **Zoom** panel has the same issue: Z sets at (-1.8, -4.8), 1.6 yd outside the LT, which reads as a wing, not "now 3x1". Set him at about w=-7.

5. **Predict 2 answer misses the force defender.** The answer says the jet-side edge has "nobody setting it except a corner who is seven yards off and blocked by X". The diagram has a **nickel back at (5.5, -10)** (the force/apex player on that side), with H in the slot at -9, and a two-high **FS at 13 yards over that side** (the alley player). Rewrite: "H blocks the nickel, who is the force player, X stalks the corner, and the only unblocked defender on that side is the safety 13 yards deep, too far away to set the edge before Z gets there." Also, the end "squeezing inside" is drawn as a **pre-snap** dashed move, but the caption describes a post-snap action. Make the caption say "the end on Z's side pinches his alignment inside as Z starts", which is a legitimate pre-snap tell. Alternatively drop the arrow and describe it as "he has been crashing all half."

6. **Rip/Liz conflict with 02-02.** 02-02 (line 544) teaches "Rip" and "Liz" as the *passing-strength call* (Saban's right/left), and in Part 6 they will reappear as Cover 3 "Rip/Liz Match". This chapter now calls short motion "rip/liz motion" with no warning. Keep the curriculum alias, but add one sentence in the Short-motion bullet: "Don't confuse it with the Rip/Liz *strength call* from [Formation Rules](02-02-…qmd): the same words are a direction tag in some offensive playbooks and the defense's strength call in others." Make the matching glossary tweak: "…Some offensive playbooks call it rip (right) and liz (left), the same words many defenses use for the strength call."

7. **Running-start physics: one claim is not supported by the model.** The text says "A head start is worth more to a receiver with a high top speed, because he gains more ground during the acceleration…". In the chapter's own model the lead is `v0·τ·(1−e^(−t/τ))`, which is **independent of VMAX**: the lead depends on motion speed (v0) and on how long acceleration lasts (τ). Rewrite: "A head start is worth most to receivers who run their motion fast and still have a long acceleration phase ahead of them, and very fast receivers tend to do both." Also add one clause that the head start points in the **direction of the motion**. A jet man's speed helps a sweep or a flat route. For a vertical route, the receiver has to turn upfield (which is exactly what the "cheat motion" was about).

8. **Rams film room: reacting to the motion does not choose the play.** "If they jump toward him, the next jet is likely to be a fake with the run going the other way; if they stay home, the jet man himself gets the ball." The play was called in the huddle, and at-the-snap motion leaves no time to check. Rewrite as a film-watching cue: "If they jump toward him, the run the other way should hit; if they stay home, expect the Rams to give it to the jet man on a later snap." Also soften "a jet motion before an outside zone run one play, a jet sweep the next and a play-action pass the play after that". It reads like a specific sequence. Use "over a game, the same jet look comes before an outside-zone run, a jet sweep and a play-action pass."

## B. Should fix (missing nuance a coach would insist on)

9. **At-the-snap motion trades away the pre-snap check.** The "Why it exists" box says the QB can use a kill call or check to swap the play "for one that suits the answer he just got". That works only when the motion **finishes early**. With motion at the snap, the answer arrives too late to change the play and feeds only the QB's **post-snap** read (which side, which receiver). Add this to the costs list under "Motion at the snap": "The quarterback gives up the chance to check the play after seeing the reaction; the information arrives in time for his read, not his call." This is the central trade-off of the modern style. Pair it with a sentence in Job 1: "Motion that sets early buys a check; motion at the snap buys a head start."

10. **The run-game job is missing: motion to add a blocker or create an angle.** All five jobs are framed around coverage and leverage. A run-game coach would add, as a short paragraph in Job 2 or in the leverage section: motion that puts an **extra blocker in the box** or gives a **better blocking angle**.
    - A WR or FB motions in to become a lead, insert or "slice" blocker. The 49ers move Juszczyk and their receivers into the box. The Rams' short motion into a condensed split sets up a **crack** on the force defender on outside zone.
    - Motion also changes the **gap count**: the motion man adds a gap the defense must fit.
    Glide/crack is mentioned in passing, but the *job* is missing. One sentence plus a forward link to 03-02 and 03-05 is enough.

11. **How the motion is started and timed.** The Madden box and Job 5 say the snap comes "at precisely that moment" and that the motion man "starts on the right word". Add the mechanics a broadcast viewer can actually see:
    - The QB starts the motion with a **leg lift, heel tap or clap**.
    - The center snaps on a **silent count** timed to the motion man's landmark.
    - This is why a defense that knows the timing can "time the snap" (which ties into the Solak paragraph).

12. **Direction of the spin.** The glossary and text fix the spin as "the safety on the side the motion is heading to comes down". That is the most common version (rotate to the motion). But defenses also rotate **away**: the backside safety comes down as a robber or "buzz" player while the motion-side safety stays high, which protects the thinned side. Add "usually" plus "some defenses rotate the other way; see 06-06" so the reader isn't misled in Part 6.

13. **Defensive dialect.** The chapter carefully covers offensive dialect but says nothing on the defensive side. Add one sentence, since the reader will hear these on All-22 breakdowns:
    - Travel is often called **"lock"**.
    - The hand-off exchange is called **"push/pull"**, **"banjo"** or **"switch"**.
    - The safety rotation is called **"rock/roll"**, **"buzz"** or **"sky"**, depending on the staff.

14. **The jet "flip" is a forward pass.** Add one clause where the jet is defined: the little forward shovel to the jet man is legally a **forward pass**, so a drop is an incomplete pass rather than a fumble. That is why it is sometimes called a "pop pass", and why some teams hand it off or pitch it slightly backward instead.

15. **Trades and the one-second set.** "All of that has to flip in the two or three seconds before the snap…" A trade is a shift, so the offense must hold a full second after it, and the defense is always guaranteed that beat. Defenses answer by **declaring strength late** (they don't set the front until the shift is done). Offenses answer by **following the trade with a motion**, which is the "shift, freeze, motion" sequence 01-05 taught. One sentence.

16. **Dolphins film room: internal inconsistency, and a counter that is probably backwards.**
    - The cheat-motion paragraph says the Dolphins' receivers motioned **outward** toward the sideline. The film room says Hill or Waddle "glides or jogs a few yards, often toward the formation". Reconcile: "a few yards, sometimes in toward the formation, sometimes out toward the sideline (the 'cheat' version)".
    - "Against Miami, many [corners] played off the line, because pressing a receiver who is in motion is almost impossible." The widely discussed 2023 counter was the opposite. The teams that slowed Miami (e.g., the Chiefs in Frankfurt and in the wild-card game, and the Ravens) got **hands on Hill and Waddle when they could**, aligning tight before the motion started, stayed two-high and **didn't chase** the motion. Either drop the sentence or replace it with that counter, and have the fact-checker source it before it ships.

17. **Empty test (Predict 3).** The caption says the Mike stops "near the numbers". The RB actually sets at w≈+12.3, between Y (9) and Z (15), which is about 5 yards inside the numbers. Either change the text to "out between the slot and the wide receiver" or move the RB set point to w≈+17 with Z widened. Also add one sentence to the answer: many man teams **exchange** against this (they bump the nickel or the safety onto the back and push the Mike onto the slot), so a *box defender* leaving is the tell, not specifically the Mike.

## C. Diagram polish (labels, collisions, readability)

- **Motion family plate:**
  - In the **Jet** panel, the post-snap arrow ends on top of H (-2.4, -9). End it at about (-2.0, -6.5) and angle it upfield so H isn't overprinted.
  - In the **Trade** panel, the X ghost and the new X overlap almost completely at -15 (on the line vs. 0.8 yd off). Either drop X's ghost and add "X steps off" as a tiny note by him, or exaggerate the step-off to d=-2.0.
  - In the **Shift to bunch** panel, Y's ghost at (-1.5, 9.0) sits underneath the finished bunch. Fine, but the triangle reads crowded. Consider point Z at 9.0 on the line, with Y at (-1.9, 7.4) and H at (-1.9, 10.6).
- **fig-jet-vs-zone:**
  - In panels 3 and 4, the W and M ghosts overlap the live W/M markers (and each other). With ghosts on four players, drop the linebacker ghosts: the bump is only 1–2 yards, and the trail lines already show it.
  - Panel 2 at t=-1.1 is titled "linebackers bump over", but the LBs have barely moved at that frame because their window is (-1.7, -0.4). Either retitle it "Nobody follows Z" or move the frame to about -0.6.
- **fig-return-motion:**
  - In panel 3, the Y marker sits on top of the M marker. In panel 4, FS and Y touch at the goal line. Nudge Y's route (e.g., `r.path((3.0,-2.5),(6.0,-5.5))`) or the FS start (w=-1.4).
  - The caption says the throw beats the corner "to the pylon", but the catch is at about the 3-yard line, w≈+17, well inside the pylon. Say "toward the corner of the end zone" or "in the flat".
  - The defense is labelled "Cover 0, six rushers", but FS (5.6 deep) neither rushes nor covers anyone. In real Cover 0 he would be man on the RB, and when the RB stays in to block he either adds to the rush ("green dog") or sits. Add `p.rush("FS", speed=2.0, delay=0.4)` or note "FS has the back" in the caption.
- **fig-team-motion:** the "league 2022 / 37.6%" and "league 2025 / 55.1%" labels are drawn straight through by their own dashed lines. Offset the text (ha="left", x+0.6) or give it a SURFACE bbox.
- **Predict 1:** the label "snap as H arrives" sits under Z/Y with no leader. It is fine, but a short leader to H's arrowhead would help. All labels are inside the window; no clipping anywhere in the chapter.
- No label in any diagram is clipped by the field edge.
- Formations are legal throughout: seven on the line every time, motion men always off the ball, and the trade and bunch end states legal. Good.

## D. Checked and fine

- **Definitions** of jet (in front of the gun QB, snap just before he reaches him), fly (Wing-T wingback behind an under-center QB), orbit, rocket (including the flexbone A-back version), return, glide and zoom are correct and appropriately hedged as dialect.
- **The trade explanation** is exactly right: why X steps off and Z steps on, and the 7-on-the-line logic.
- **Travel vs. exchange vs. pattern-match follow, and fake spins**, are the right three counters, at the right depth for a Part 2 chapter.
- **The Cover 1 robber read** in Predict 1 is correct and well caveated (the robber jumps the crosser).
- **Rules:** NFL / NCAA / CFL table, the Toney–Moore wrong-formation anecdote, and the 2024 Rule 7-4-2 Item 2 language with the "clarification" framing.
- **The running-start model** numbers check out (+3.2 yd at 1 s).
- **The motion-numbers section** ("never on one axis") is excellent and should stay as is.
- **The Big Data Bowl eval cell** matches the `gridiron.bdb.prepare(trk, plays, game_id, play_id)` signature. Minor: it loads only week 1 tracking but picks the first motion play from all nine weeks. Filter `flags` to week 1 (merge `week` from plays.csv) so the snippet runs as written.
