# 05-03 Odd and Hybrid Fronts: coach / film-analyst review

Reviewer stance: veteran NFL defensive coach and film analyst. I rebuilt the PDF (`build_pdfs.py 05-03-odd-and-hybrid-fronts --html`, OK) and looked at every page at 110 dpi.

**Verdict:** A strong chapter. The history is handled honestly, the "count hands, not names" idea is right, and the nickel-label data figure is excellent. Inside-zone-vs-tite is mostly right. Several things need fixing before a coach would sign off:

- The **outside-zone-vs-tite mechanism** contradicts the book's own zone rules from 03-02.
- The **shift animation** puts a 250-pound outside linebacker at a 4i.
- The **Drill 3 figure** doesn't show what it asks the reader to see.
- The NFL **3-3-5 definition** contradicts the chapter's own data.

No labels are clipped by the field edge, and I found no hard label collisions.

---

## A. Must fix (technical errors)

### A1. Outside zone vs the tite: the "easy reach" claim is backwards under 03-02's rules
This appears in four places: the Fig 5 right panel and its caption, the rule-of-thumb bullet "To beat the reach…", the Drill 2 answer ("the play-side 4i and the nose are *inside* their blockers, the easiest reaches there are"), and the Fig 5 panel label "4is and 0: inside their blockers, easy to reach".

Apply 03-02's rule ("covered = head-up or shaded to his play side") to outside zone right against the tite:
- **RG is covered by the play-side 4i.** The 4i sits in RG's play-side B gap, wider than a 3-technique. RG has to reach a man who is *outside* him, which is a harder reach than a 3-technique. The figure even draws RG stepping flat to w≈2.8 to reach him.
- **RT is uncovered.** The 4i is on his backside, and the C gap is empty. So the RT either combos the edge with Y or climbs straight to the single linebacker.
- **C is covered by the 0.** This is a head-up reach, helped by an uncovered LG.

The tite's real problems against outside zone are these:
1. The play-side C gap is empty at the snap, so the play-side tackle is a free blocker who can climb to the lone Mike or combo the edge.
2. The 4i and the nose are big two-gap bodies who have to *run laterally* to stay square against a stretch. That is the opposite of what they are built for.
3. Outside the tackle there is only one edge, and the alley player (the SS) comes from 10+ yards.

The defense is not hurt because the reaches are easy. It is hurt because the front puts nobody in the C gap and leaves a tackle unaccounted for.

**Fixes:**
- Fig 5 right: change the RT's step to a combo on RE with Y, then climb toward MIKE (e.g. RT via (0.3,4.6) to (2.6,3.0)). Change Y to "reach E with RT's help". Replace the label "4is and 0: inside their blockers, easy to reach" with "C gap empty: the RT is free to climb". Keep the ring on E and the alley shading.
- Caption and rule of thumb: rewrite the outside-zone half as above. The inside-zone half ("line up on or just inside the blockers") is fine.
- Drill 2 answer, Front A paragraph: same rewrite. "The play-side tackle is uncovered and can climb to the only linebacker; the 4i has to chase sideways; the edge faces Y plus help." Front B's reasoning stands as written.

### A2. Fig 9 (shift animation): a stand-up OLB becomes the 4i
In the animation the right **stand-up edge (OLB)** slides inside to a 4i and puts his hand down. In a real tite, the 4is are 290–320-pound linemen. Nobody puts a 250-pound rush OLB on the tackle's inside shoulder against 11 personnel on a run down. He would be washed out by the RT/RG double the chapter just taught.

The chapter's own Georgia source describes a different shift: the RDT becomes the nose, the RDE slides to 4i, the boundary end stands up and walks out, and the other DT becomes a 4i. Every interior spot stays with a lineman.

**Fix:** start from 4-2-5 personnel with four hands down: L3 (DT), R1 (DT), and two DEs at wide 5s. Then shift:
- R1 → 0
- L3 → 4i (left)
- RE (DE) → 4i (right), hand stays down
- LE (DE) stands up and widens. **This is the spec's "edge changes stance" moment, and the ring belongs on him.**
- MIKE walks up outside Y as the fifth man on the line, as now.

Frame 4 can stay: four rush and the walked-up Mike drops. Update the caption, the "Back to the broadcast" bullet ("sliding an edge inside…") and the text after the figure to match. If you want to keep "2-4-5 personnel", the two *DL* have to make the moves inside, and an OLB can only change stance at the edge.

Also: after the shift the old labels ("T", "E") ride along, so the 4i is labelled "E". Relabel in the strip (via `after=`) or say so in the caption.

### A3. Drill 3 figure doesn't show the cue it asks the reader to read
- The three linemen are drawn **2.6 yd off the ball** (`moved(d=2.6)`) while the edges stand at 1.0, so the DL look like off-ball linebackers behind the edges. A quarter-second after the snap a defensive lineman is at or across the line, not 2 yards back. The hand dots float under the squares.
- The first-step arrows in Snap A and Snap B look almost identical (all nearly straight down). The only visible difference is alignment, which gives the answer away without teaching the first step.

**Fix:** keep the DL at d≈1.0, with steps 0.6–1.0 yd long.
- **Snap A (two-gap):** short arrows that end in a block bar or "punch" mark on the blocker's chest, e.g. 4 → (0.2, ±T("4")) with a small perpendicular bar.
- **Snap B (one-gap):** longer diagonal arrows that cross the LOS *into the gap*, ending past the blocker's shoulder. For example: 3 → (−0.6, −2.4) through the B gap, 1 → (−0.6, 0.8) through the A gap, 5 → (−0.6, 4.0) through the C gap.

Alternatively, put both snaps in the *same* (head-up) alignment and let only the steps differ. That makes it a genuine film-reading drill, since one-gap teams also line up head-up and slant.

### A4. "In the NFL, the 3-3-5 is usually a five-man line in nickel" contradicts Fig 8
The chapter's own data shows that roster-labelled 3-3-5 snaps come mostly from GB, WAS, DET and NYJ, which are four-man-front teams with one edge listed as an OLB. The text below the bullet admits it ("often means neither").

**Fix:** split the term in two.
- **As a roster label**, 3-3-5 mostly means a four-man line with mixed edge labels.
- **As a front call** in NFL coaching language, a nickel tite (three interior DL, two edges, one ILB) is what coaches call a 3-3-5. The Fangio tree, including Staley's Rams and Chargers, calls it **"Penny"**: nickel personnel with a nose.

Add "Penny" as a dialect note. Some other staffs use "penny" for a three-safety dime (see the 02-05 coach review). That clash is exactly the dialect point the chapter is making.

### A5. Fig 7 caption says "Same alignments" when they aren't
The left panel (4-2-5) has a 3 and a 1. The right panel (2-4-5) has two 3s. Either draw both as 3/1, or both as 3/3, or change the caption to "nearly the same alignments". The cleanest fix is to give the 2-4-5 a 3 and a 1 too. Edges at ±5.0 are wide 5s, which is fine.

Also, the two "four on the line" labels sit in the offensive backfield at (−2.8, −5.6) and point at nothing. Move them to the defensive side, e.g. (2.4, −6.6), or use a bracket over the four line defenders.

### A6. "Three or five men on the line (the 3-4 and the old 5-2)"
This appears in the text under Fig 1 and in the **Odd front glossary entry**. A 3-4 Okie has **five on the line** (three DL plus two OLBs at the line; Fig 2 shows it). What it has three of is *down linemen*.

**Fix:** "the classic odd fronts have three down linemen (the 3-4, with two standing edges making five on the line) or five (the old 5-2)".

### A7. Wade Phillips "looked like his father's and played nothing like it". Verify; probably wrong
Wade Phillips has consistently described his attacking, one-gap 3-4 as **his father's Oilers defense**, in contrast to the Parcells/Belichick two-gap 3-4. The chapter's own Bum section (Culp "strong enough to need two blockers") doesn't establish that Bum's was a two-gap scheme.

**Fix:** "ran his father's attacking version of the 3-4, the branch that never adopted the Parcells/Belichick two-gap". Hand this to the fact-checker with a source, e.g. a Phillips interview from his Houston or Denver years. If you can't source it, drop the "nothing like it" contrast.

---

## B. Should fix (nuance a coach would insist on)

### B1. "Every interior lineman covered": square this with 03-02 and with the bear front
In the tite section ("There is no uncovered lineman…") and the rule-of-thumb bullet ("make every interior lineman covered"), the claim is true *only for the run going toward a given guard*. By 03-02's play-side rule, on inside zone right the **LG and the RT are uncovered**. That is exactly why Fig 4 shows two doubles. The tite's trick is that both uncovered men are *needed on doubles* because the 0 and the 4i can't be blocked one-on-one. That leaves no spare blocker to climb.

Contrast this with the **bear front** of 05-02, which covers C and both guards *by alignment* (0 plus two 3s). One sentence linking 05-02's bear front would let the reader see the family resemblance (the center covered, the B gaps choked) and the difference (bear 3s sit on the guards; tite 4is sit on the tackles, which leaves C gaps open; see A1).

### B2. "That is the tite's answer to inside zone, power, duo…" overstates power
Against gap schemes, defenders aligned inside the blockers give the offense **easy down-block angles**: the RT down on the 4i, the RG down on the nose. The tite survives power because:
- the 4i *squeezes* the down block (fights pressure and closes the B gap),
- the edge wrong-arms or spills the kick-out/puller,
- the lone ILB fits off the spill.

Say that, or say "inside zone and duo" and leave power to 05-05.

### B3. Fig 4 / tite inside zone: the backside edge is the zone-read key
The unblocked backside E squeezes hard down the line, so by frame 4 he is behind the LT. On a shotgun inside zone that is a QB **pull** read, yet the QB hands off. A coach would flag this immediately: no NFL defense teaches the backside edge to crash flat against a gun team.

**Fix (pick one):**
- (a) Make the edge "squeeze and stay square": end LE around (0.6, −3.6), not (−1.6, −3.0), and add a caption phrase saying he holds the QB.
- (b) Put the QB under center or in the pistol and drop the carry-out fake.

Drill 1's answer already cites the zone read, so (a) is consistent.

Also: the caption and frame 4 say "a gain of about a yard", but the back is drawn at d≈0.1, which is no gain. Move his end point to (1.0, 4.3) and the Mike's to (1.6, 4.4). And the frame times 0.95 and 1.45 print as "+0.9 s" and "+1.4 s"; use 1.0 and 1.5.

### B4. The G front breaks the chapter's own one-glance test
An Okie with the nose at 2i has nobody head-up on the center, so by "Find the center" it reads **even**. Say this in one sentence; it is a good teaching beat. That is exactly what the G tag is for: it changes who is covered. It is also why the chapter warns that odd and even describe alignment, not roster.

### B5. Eagle and mint dialect
- In a lot of 3-4 vocabulary, "Eagle" means a **one-side** reduction: the end to a 3 on the guard (or a 4i) and the OLB down onto the tackle or the C gap. That is the Under-like 3-4 of Fig 3 right, not a both-sides pinch. The chapter's Pewter Report cite supports one reading. Add the second ("or, in other staffs, a one-side pinch with the outside linebacker taking the end's spot") so readers aren't surprised by Eagle on a broadcast. This needs a source; Fact-check.
- "Mint" is a **Saban-tree** word (Alabama, and Georgia through Smart), not Georgia's alone. "The Saban tree, Kirby Smart's Georgia among them, calls it mint" is more accurate.

### B6. Stand-up edge: stance claims
- "Get to full speed sooner, because he is already upright": coaches dispute this. Many elite rushers put a hand down for get-off on obvious passing downs. Soften it to "can align wider and see the tackle's set; plenty of rushers still prefer a hand down for get-off".
- "Many of them put a hand down on obvious running downs": correct for short yardage and goal line (leverage), but the most common hand-down moment is **nickel passing downs**, when the 3-4 OLB becomes a 4-2-5 DE. Add it; it also reinforces the 2-4-5 = 4-2-5 point.

### B7. The 3-4 against spread (missing)
The classic Okie's main modern problem goes unsaid: against 11 personnel the field OLB has to **walk out over the slot**, which leaves a four-man box front with a soft edge. That is *why* 3-4 teams go to 2-4-5 or tite instead of staying in the Okie. One paragraph at the start of the nickel section would connect the Okie to the nickel fronts.

### B8. Two-gap ILBs are not truly "gap-free" against two backs
Against 21 personnel (the Fig 2 offense) the fullback is an extra blocker. On an iso or lead, one ILB has to take on the FB in the hole, and the other fills off the nose. "Gap-free" holds against one-back sets. Add a clause in the Fig 3 text, or point to 05-04/05-05.

### B9. 2018 Bears as "the classic example" of the tite/light-box bargain
The 2018 Bears' base was Fangio's 3-4 (Hicks and Goldman inside). They did play tite, but they also played a lot of single-high with Eddie Jackson. The two-high light-box identity is more clearly Staley's 2020 Rams and Fangio's Denver and Philadelphia teams.

**Fix:** "the 2018 Bears' 3-4, often in the tite" rather than "the classic example" of the two-high bargain. Alternatively, lead with the 2020 Rams, which the chapter already sources at 78% light box.

### B10. Small accuracy items
- "The nose … is the heaviest man on the field." Offensive linemen often outweigh him. Change to "usually the heaviest man on the defense".
- 3-4 DE weights "290-to-310": Seymour (~317) and similar players argue for "290 to 320".
- Fig 1 even panel: the end is at 9 with the Sam stacked over Y. Check that this matches how 05-02 draws the Over (05-02 uses a 5 end in its Over/Under figures). Keep the two chapters consistent.

---

## C. Diagram-by-diagram check (looked at every page)

| Fig | Football | Layout |
|---|---|---|
| 1 even/odd | OK (see B10 on matching 05-02's Over) | clean |
| 2 Okie plate | Legal, realistic (ILBs ~4.5 deep over the guards; 9 on Y; open-side E wide) | clean, leaders good |
| 3 two ways | Gap math correct. One-gap = Under with Mike strong B and Will weak A: correct | the **edge arrows in the right panel are nearly invisible** (end points too close); lengthen to ~0.6 yd past the LOS |
| 4 tite vs IZ (strip) | Doubles are correct by zone rules (C+LG on 0, RG+RT on the play-side 4i, LT cutoff, Y on E). Issues in B3 | readable; SS enters frame 4 |
| 5 front vs zone | **A1** (outside zone panel) | labels OK; "alley" sits ~1.5 yd inside the edge, fine |
| 6 4-2-5 vs 2x2 | Good: wide 5s, $ in apex, SS rotated down, 6 vs 5 box | clean |
| 7 4-2-5 vs 2-4-5 | **A5** | stray "four on the line" labels |
| 8 labels data | Good, and it drives A4 | fine |
| 9 shift (strip) | **A2**; frame timing is fine (−2.6, −0.6, snap, +1.1) | relabel after the shift |
| 10 dialect | Fine; add B4/B5 text | clean |
| 11 Drill 1 | Fine | clean |
| 12 Drill 2 | Fronts fine; the answer needs A1 | clean |
| 13 Drill 3 | **A3** | DL drawn off the ball behind the edges |

Animations: two (Fig 4, Fig 9), within the limit, and both strips tell the story in print. Answers use the markdown callout convention correctly, and each footnote is referenced once.

## D. Film room
- **Texans 2011–12:** good choice, accurately described. Watt did align all over (5, 3, 4i), so "lines up on a tackle's outside shoulder" should read "often".
- **SB50 Broncos:** accurate (Miller 2.5 sacks, 2 FF, Jackson TD). Worth adding that Denver lived in nickel and dime that night, so viewers will see the 2-4-5, which ties to that section.
- **Eagles 2024:** good. The SB LIX "four-man rushes" is accurate (no blitzes). Note that on passing downs Fangio's Eagles were mostly 2-4-5 with Carter and Williams inside, so the reader looks for the tite on early downs against 12/21.
- **Georgia 2021:** good, but the shift description comes from a 2025 Substack about Georgia's current scheme. Say "Georgia's defense under Smart (the 2021 unit included)" or find a 2021-specific source. Use "mint (the Saban-tree name)" per B5.
