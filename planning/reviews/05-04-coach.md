# 05-04 Linebackers and the Second Level: coach / film-analyst review

Reviewer stance: veteran NFL linebackers coach and film analyst. I rebuilt the PDF (`build_pdfs.py 05-04-linebackers-and-second-level --html`, OK), rasterized it at 90 dpi (200 dpi for Figs 4 and 5), and looked at every page and every figure.

**Verdict:** a strong, well-organised chapter. The keys → flow → fit → pursuit → tackle → coverage order is how a linebacker coach teaches the position. The play-action-from-the-LB's-side strip and the tackle-depth chart are excellent, and the history is honest. Most of the prose would pass a staff room.

The problems are mostly in the **diagrams**:
- Fig 4 draws the "correct" backside linebacker in exactly the wrong place. That undermines the lesson and Drill 3.
- Fig 6 has the wrong offensive lineman climbing.
- Fig 3 has the puller trailing his own ball carrier.
- The Fill panel sends the Mike into his own 3-technique.

There are also a handful of terminology slips (a pull is "away from the center"; Ray Lewis as an "open" linebacker) and a few nuances a coach would insist on.

No on-field label is clipped by the field edge. The only real collisions are in the Fig 3 frame strip (panels 3–4) and the small OL/DL labels in the Fig 11 strip.

---

## A. Must fix (technical errors)

### A1. Fig 4 (fig-flow), fast-flow panel: the Will is drawn *outside* the cutback lane he is supposed to guard
In the code, `go_to(p, "WILL", (3.4, 2.6), via=[(4.4, 0.0)])` puts the Will at w = +2.6. That is the play-side B gap, past the center, and next to where the Mike started. The dashed "cutback lane" ends at w = +0.3. On the page, the Will's arrow ends to the right of the cutback arrowhead, so he has already been cut back on.

It also wrecks Drill 3. The "mistake" Will there is at (3.6, 3.3), only 0.7 yd from the "correct" Will. A reader comparing Fig 4 and Fig 16 can't see the error the drill is about.

- **Fix:** have the Will shuffle and press over the top to about (4.6, 0.0)–(4.8, −0.3). That is over the center or the backside A gap, a yard deeper than the Mike and clearly *inside/behind* the end of the cutback lane. Move his label so it points at that spot.
- In Drill 3, keep the Will level with the Mike at about w = +3.3 and *also* show the backside A/B gap empty (a faint shaded lane). The contrast then reads at a glance.

### A2. Fig 6 (fig-scrape-read): the wrong lineman climbs to the Will
The dashed blue "the left guard climbs to the spot the Will vacated" starts at the LG (−1.6). But `nickel_front` puts the **3-technique on the left guard** (w = −2.35), so the LG is covered. On inside zone right he has to cut off the 3. The backside blocker who is free to climb to the Will is the **LT**: the read end is left unblocked, so the LT is uncovered. He either climbs directly or combos the 3 with the LG and then climbs.

- **Fix:** start the dashed path at the LT, (0.1, −3.2) → (2.4, −2.9) → (3.9, −2.4). In the caption and Fig 6 text, change "The left guard (dashed blue) climbs" to "The left tackle, uncovered because the end is being read, climbs (dashed blue)". It also teaches something: the scrape has to beat the LT's climb, which is why "rub the end's hip" matters.

### A3. Keys table: "Steps flat along the line, away from the center" is wrong for a pull
A guard pulling to the far side, which is the play in Fig 3 and in the opening scene, steps *toward* and behind the center. A pull is recognised by depth and direction: a short drop or bucket step, hips opening, running flat behind the line either way.

- **Fix:** change the row to: "Opens his hips and steps back and flat behind the line (either direction) | A pull: a gap-scheme run (power, counter, trap) going where he goes | 'Pull, follow': flow with him, inside-out."

### A4. Fig 3 (fig-key-pull, frame strip): the puller trails the back, and the Mike reads a guard who is not "in front of him"
- **Timing.** At +1.0 s the pulling LG and the tailback are on the same spot (circles overlap). At +1.4 s the guard is *behind* the X where the back is tackled. On power the puller leads the back through the hole by 1–2 yards. As drawn, a coach sees a play with no puller at all.
  - **Fix:** raise the LG's speed to about 5.5–6.0 yd/s and/or delay the RB's track 0.1–0.15 s, so that at +1.0 s the guard is at the hole's mouth about 1.5 yd ahead of the back.
  - Then end the play with the Mike meeting the **puller at or behind the line** and the back stopped behind it (a squeeze/wrong-arm fit). Alternatively, have the Mike beat the puller by a step to the back's near hip.
  - Either way, update panel 4's note ("beats the puller to the hole") and the caption to match.
- **Collisions.** Panels 3–4 pile the "3", "5", M ring, X, T and Y markers on top of each other. Once the timing is fixed, nudge the end-point of the SE or DT a half-yard so the X and the M ring are readable.
- **Key.** The Mike is aligned at w = +0.8 (strong A gap). His "guard in front of him" is the **RG**, but the eyes line goes to the **LG**. That is a legitimate read, but it is a different read from the one the text teaches ("the guard in front of him").
  - **Fix (pick one):**
    - (a) Say so: "Many teams have the inside linebackers read *both* guards ('guard-to-guard' or a 'triangle' read: near guard, far guard, near back). Here the far guard's pull is the key." Draw the Mike's eyes to both guards.
    - (b) Make the Will the hero, since he is over the LG.
  - Option (a) also covers the dialect point in B2.

### A5. Fill panel of Fig 5 (fig-fit-actions): the Mike fills into his own 3-technique
The iso is aimed at w ≈ 2.2–2.4 (the right B gap), and the Mike's arrow ends at (1.75, 2.35), which is on top of the 3-technique's square. No offensive blocks are drawn, so the picture shows the Mike, the fullback and the tailback all converging on a spot the defensive tackle is standing on. Iso is aimed at a **bubble**: the uncovered guard and the linebacker over him.

- **Fix:** keep the Over front and the Mike's default w = +0.8. Run iso at the strong A gap, which is open in the Over because the 1 is shaded weak:
  - FB → (0.6, 0.9)
  - RB → (−1.2, 0.9) via (−4.6, 0.4)
  - Mike → (1.6, 0.9)
- Alternatively, keep the B gap and draw the RG base-blocking the 3 inside and the RT on the 5, so the hole exists.

### A6. Scrape panel of Fig 5: the Mike overshoots into the Sam's gap, and the end's squeeze is invisible
- The caption says the Mike scrapes "to the gap outside the end." The end is a 5-technique at w = 4.0, inside the TE at 4.8, so that gap is the **C gap** (about w 4.0–4.8). The Mike ends at (2.3, 5.9), which is outside the tight end and directly in front of the Sam: the D gap.
  - **Fix:** end the Mike at about (2.0, 4.4).
  - Optionally move the Sam to (1.8, 6.6) with a short arrow so the reader sees he keeps the D gap/force. That way the panel shows the gap exchange rather than two players fitting the same gap.
- The SE's squeeze is 0.8 yd and is drawn as a speck (the "3 •5" dot).
  - **Fix:** move the SE to (0.6, 2.9) so the squeeze arrow is visible, and add a tiny label "end squeezes".

### A7. Film room, Ravens 2000: Lewis is not "the open linebacker"
The chapter defines *open* as standing over an **uncovered** guard who can climb to you. The point of the paragraph is the opposite. Siragusa and Adams covered or occupied the guards so that *nobody* could climb to Lewis.

- **Fix:** "This is the **protected** (or 'clean') linebacker at his best: two big tackles who keep both guards off him, and a linebacker fast enough to his keys to make that pay." Optionally add a line saying this is the 46/'Bear' idea of covering both guards, built into a 4-3.

### A8. Drill 1 answer: the Mike is the *backside* linebacker, not the one the wrapping tackle is looking for
In the figure the Mike is at w = +0.2 (over the center) and the Will at −2.2, which is the play side of a counter going left. On GT counter, the guard kicks out the end man and the tackle wraps for the **play-side linebacker, here the Will**. The backside Mike is the one the down-blockers (LG or C) climb to, or he is left unblocked.

- **Fix:** replace "looking for the playside linebacker, which is you, or the Will" with "looking for the play-side linebacker, the Will. You are the backside linebacker. Your guard has just pulled, so you follow him over the top, flat and inside-out, while the center or left guard tries to climb to you, and you fill the hole the tackle leads through."
- Optional nuance: on GT counter, Y would normally **hinge** (step back and wall off) the backside 5, because the pulling RT leaves him unblocked. Add a short Y hinge step in the drill figure, or one clause in the answer.

### A9. Pursuit caption: "he never catches him" is false
I re-ran the chapter's own pure-pursuit integration. The chasing linebacker (7.5 yd/s against 7.0) is 1.75 yd behind after 1.9 s. He catches the back after about **4.4 s, roughly 28 yards downfield**.

- **Fix:** caption: "he doesn't catch him until about 28 yards downfield." Text: "never gets closer than about two yards" → "is still nearly two yards behind after two seconds, and doesn't catch him for another twenty-odd yards." That number is a better teaching point anyway.

---

## B. Should fix (nuance a coach would insist on)

### B1. Block destruction and the read step are missing
The chapter says a linebacker "wins by getting to the spot first, or by slipping the block," and leaves spill/box to 05-05. A linebacker coach would not sign off without a short paragraph on two things.

- **The read step.** The first step is a short (about 6-inch) downhill "read step" or "pop step", not a lunge. It lets him go forward or back once his keys declare. "False step" (a step the wrong way) is the cardinal sin the chapter already alludes to.
- **Taking on a climbing lineman:**
  - Shock with the hands, keep the **gap-side arm free**, and get off the block toward your gap.
  - Never run around a block, which opens the gap behind you, unless the call is to spill.
  - The two named takes-on are *box* and *spill/wrong-arm*, which 05-05 builds.

This fits naturally after the four fit verbs (before the Madden callout). It also makes the "Watch for it" item "first step forward or back?" more accurate: the first step is the read step, and the *second* step tells you what he saw.

### B2. Name the key-read dialects
The text gives one read (near guard + near back) plus a good note on 3-4 vs 4-3. Add one sentence naming what the reader will hear:
- the "guard read" / "high hat–low hat" read
- the **triangle read** (near guard, far guard or near tackle, near back)
- the **flow** or "backfield" read (Tampa-2 style 4-3 teams, Kiffin's linebackers)
- for the apex player, the near tackle or TE through to the #2 receiver

This also resolves A4's "far guard" issue.

### B3. The keys table needs two more rows
- **Down block** (the guard blocks inside, away from the linebacker): gap scheme to the linebacker's side. The tackle or a puller is coming, so squeeze and find the puller/kick-out.
- **High hat, back stays in, nobody releases:** a draw or screen alert. As written, "high hat = pass, get to your drop" teaches the linebacker to run away from the draw. That is exactly how draws work, and 04-05 covers screens.

### B4. Cross-chapter terminology conflict on "stack"
05-02 (line ~499) says the Over front's Mike "**stacks** over the strong A gap… (the stack alignment)", and links to this chapter. By this chapter's definition (directly behind a defensive lineman), that Mike is not stacked. The strong A gap in the Over is empty, so he is in a **10** over open grass. This chapter's Fig 1 middle panel even calls the Over's Will "open".

- **Fix:** in 05-02, change "stacks over the strong A gap" to "lines up over the strong A gap (a '10' alignment)". Flag this for the 05-02 owner; it is outside this chapter's file.
- In 05-04, soften "Most four-man fronts stack one linebacker at a time, typically behind the 3-technique" to: "Four-man fronts usually stack at most one linebacker (in many Under fronts, the Will behind the 3-technique, a '30') and play the others open or over a shaded lineman."

### B5. Apex/walk-out run job: "fill back inside" is the wrong verb for most calls
A walked-out apex linebacker is normally the **force or alley player** to his side. He fits *outside-in*, squeezing the D gap or alley and keeping the ball inside. He does not refill the box from outside.

- **Fix (Fig 2 label and caption):** change "run: fill back inside" to "run: come downhill outside-in (force/alley)", and say the call decides whether he squeezes or spills (forward link to 05-05).
- Also, "With only four defensive backs, the defense *has to* walk both outside linebackers out" overstates it. Alternatives are rotating a safety down (single-high, Sam over the detached Y, Will in the box) or checking to nickel. Change "has to" to "one answer is to", and add a clause naming the alternatives. Otherwise the reader thinks base vs 2x2 always means a five-man box.

### B6. Cover 3 hook/curl: mention the seam carry
In Cover 3 the biggest job of the inside hook/curl ("seam/hook") defender is to **carry #2's vertical (the seam)** to about 10–12 yards so that four verticals don't beat three deep defenders. Walling the inside route comes second.

- **Fix:** add one sentence to the "wall, sink, eyes" sequence: "…and if the slot runs straight up the seam, he carries him until a deep defender takes over." In Fig 9, the "wall the inside route" label sits under the $ and reads as the nickel's job. Move it next to the Will's drop, about (6.5, −4.6).

### B7. Front strength vs coverage strength (green dot)
Fig 13 uses a formation where the TE and the trips are on the same side, so "Strength right!" is easy. What makes the green dot's job hard, and is the thing a coach would mention, is that many defenses set the **front** to the tight end (or the back) and the **coverage** to the receiver strength. Against 3x1 with the TE on the single-receiver side, those are opposite, and he has to call both.

- **Fix:** add one sentence under "He sets the strength". Optionally put a footnote in the figure: "if the TE were on the left, the front would set left and the coverage right."

### B8. Rat vs robber (dialect)
The term index aliases robber = rat, so keep that, but add a half-sentence on how coaches use the words:
- many staffs say **rat** for a low hole defender (about 5–8 yards, crossers), usually a linebacker or a lurking lineman;
- they say **robber** for a deeper one (about 10–12 yards, digs and in-cuts), usually a safety.

Also, the Fig 10 caption says "8 to 12 yards" while the text says "8 to 15". Pick one, and keep the hole-zone depth consistent with 06-01.

### B9. Tackle-depth data (Fig 8): many off-ball 4-3 outside linebackers are in the "edge" group
I checked nflverse 2023 rosters. `depth_chart_position == "OLB"` includes off-ball 4-3 linebackers such as **Jeremiah Owusu-Koramoah (CLE)** and **Germaine Pratt (CIN)**, alongside 3-4 rushers (Watt, Parsons, Zaven Collins). So "Off-ball linebacker" is undercounted, and "Outside linebacker / edge" mixes two different jobs.

The "about a quarter on runs of 3 to 9 yards" claim is still directionally right, but it is a floor. **Fix (pick one):**
- Rename the series "ILB/MLB-listed linebackers" and "OLB-listed (mostly edge rushers, some 4-3 outside linebackers)", and say the LB share is a lower bound.
- Reclassify OLBs by weight (for example, under 245 lb = off-ball) from `load_combine`/rosters, and say so in the footnote.

Flag this to the fact-check/data reviewer too.

### B10. Drill 3 answer overclaims
"The cutback runs you see go for 20 yards are almost always one linebacker being too fast." The backside **end** (who has to squeeze or chase so the back can't bend it back) and the backside **safety's** fit are equally often the culprits.

- **Fix:** "…are usually a backside player out of place: a linebacker who ran too fast, an end who got reached or cut, or a safety who flowed too early." Also add to the answer that the Will's job is shared with the backside end.

### B11. Hook vs figure consistency, and the invented "Smith"
- The opening says the Mike "arrives in the hole at the same moment as the back and a pulling guard". The figure, the text and "Back to the huddle" say he gets there **first**. Make the hook say "a step before the pulling guard".
- The broadcast quote names "Smith". With Roquan Smith featured in the film room, a reader will assume this is a real Ravens play and a real quote (AUTHORING §6: never invent a specific play or quote). **Fix:** use "the Mike" in the quote, or make it explicitly generic ("Watch the guard. He pulls, and the Mike is gone…").
- The hook also describes a counter step by the back ("two steps to his left"), while Fig 3 is I-formation power with no counter step. Either acknowledge it ("the picture leaves out the back's counter step") or drop the "two steps left" from the hook. "Back to the huddle" already explains it as a counter step, so the cleanest fix is to add that clause to the Fig 3 caption.

### B12. Film room, 49ers 2023: the "safety-sized linebacker in a much bigger body" is self-contradictory
Warner is about 6-3 and 230+ lb. **Fix:** "the coverage linebacker at its best, in a full-sized body: what teams hoped the safety-sized linebacker would be." The wide-9 and seam-carry details are good. Note in passing that his seam carry is the Cover 3 match "Mike runs the seam" rule (ties to B6).

---

## C. Minor and polish

1. "A linebacker weighs 230 to 245 pounds" → "about 225 to 245". The chapter's own Combine average since 2019 is 233.
2. Depth: "about four to five yards" → "about four to six". NFL off-ball linebackers against shotgun often sit at 5–6.
3. "the eleven or so square yards of grass": tackle to tackle and LOS to linebacker depth is closer to 30 square yards. Say "the few square yards between the tackles", or drop the number.
4. Fig 5 Plug panel: the green "B" tag and "the 3 slants inside" both sit in the offensive backfield, 2–4 yards from the action. Put the B tag just above the LOS between the G and T (about d = 0.3, w = 2.4, nudging the Mike's arrow if needed). Put the label beside the slant arrow, at about (2.4, −0.2), or above the 1/3 pair.
5. Fig 5 Run-through panel: the Will's path runs straight down the LG's left edge and visually grazes his marker. Start the Will at w = −2.5 and angle him to (−2.2, −2.7) so he is clearly in the B gap between G and T.
6. Fig 11 strip: in frames 2, 3, 5 and 6 the OL labels (LT/LG/C/RG/RT) are hidden under the DL squares. Use `line("short")` in `pa_play`, as the other figures do, or set the DL's end-points 0.3 yd shallower.
7. Fig 12 right panel: the 2019 point is joined by a line to 2022 across the excluded 2020–21 classes. Plot 2019 as a lone marker, or break the line, so it doesn't imply data that was dropped.
8. "Linebackers are the most common blitzers in football": with nickel/dime and DB-heavy pressures this is arguable. Say "the most common *extra* rushers from the second level" or "traditionally the most common blitzers".
9. The play-action "situations" sentence: "on the offense's side of midfield" is an odd marker for play-action. Use "first down and second-and-short, and in the shot zones near midfield".
10. Spy bullet: worth noting that teams now often spy with a safety or the nickel, the same speed logic as the Sam section.

---

## What is right and should stay
- Keys before flow before fit, "the linemen tell the truth sooner than the ball does", "if your keys disagree, believe the linemen", and the counter/play-action-as-key-lies framing. This is exactly how it is coached.
- Fig 11 (play-action, back key vs guard key) is the best figure in the chapter. The rule hook (ineligible downfield) as the tell is a real coaching point.
- The scrape-exchange timing/path/leverage breakdown, "rub the end's hip", and the arc answer.
- Pursuit geometry (after the A9 wording fix), inside-out plus the leverage player, and the hawk-tackle points (near shoulder/near thigh, head behind, eyes through the thighs, wrap and roll).
- The green dot's five jobs, including disguising the protection's Mike point, and the move of the dot to DBs.
- Film-room picks match the spec and are characterised correctly, apart from A7 and B12. Kuechly's two NFC pick-sixes, Roquan's trade date and contract, and the Ravens 2000 records are all as I know them (fact-check reviewer to confirm Wagner's 10 SB tackles and Warner's 2024 first-team).
- Animation count (2) is within budget. The Fig 11 frame strip tells its story in print. Fig 3's will, once A4 is fixed.
