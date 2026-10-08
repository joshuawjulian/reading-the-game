# Coach / film-analyst review: 14-01 Building a Roster

Reviewed 2026-10-08. I rebuilt `pdfs/14-01-building-a-roster.pdf` (25 pp., OK), rasterized it, and looked at every figure.
The field diagrams (Figs 10, 11, 12, 17) were checked at 130–250 dpi. I read FACTS-current, the 14-01
factcheck log and 06-01, 13-02 for consistency. The chapter is not edited here.

**Verdict:** the cap, acquisition and draft sections are strong and accurate, and the data figures are clean.
The problems are in the football: one coverage claim contradicts the book's own Seattle film room, two
run diagrams leave a play-side defender unblocked, the Cover 3 picture shows the corner beaten deep, and
one data bug drops right tackles from the positional-value chart. Fix the MUST items before publish.

---

## MUST fix (football is wrong or misleading)

### 1. Press does not mean man, and Seattle was a Cover 3 team (text before Fig 12, plus Fig 12)
- The text says "A team that plays a lot of **man coverage** with its corners in press … Pete Carroll's Seattle
  teams…". Carroll's Legion of Boom was the league's signature **press Cover 3** (zone) defense, built on step-kick
  press-bail technique. The book's own 06-01 film room says so ("Seattle Seahawks 2013: press Cover 3"). As written,
  14-01 contradicts 06-01 and teaches the reader that press = man.
- **Fix:** split the corners by **technique** (press vs off), not by man vs zone. Suggested wording: "A team whose
  corners press, whether in man or in a press-bail Cover 3 like Pete Carroll's Seattle, wants long, physical
  corners…". The off-coverage counterexample should be a **squat / flat corner in Cover 2 (Tampa 2)** or an
  off-man/quarters corner who plays with vision and a quick plant. Ronde Barber (5-10) in Tampa Bay's Tampa 2
  is the canonical "a shorter corner can thrive" example; check his height before printing.
- **Fig 12, right panel:** this is the wrong coverage for the point being made. A Cover 3 deep-third corner is the
  *last* player who can be short and slow, because he carries #1 vertically. In the drawn picture he is also
  **beaten deep**: X's go route ends at d≈16 and the corner at d≈12.5 with X outside him, which is a coverage bust.
  - Option A (preferred): re-title it "Off, Cover 2 flat (cloud) corner". Put CB at d=5, w=-13 (outside
    leverage, eyes inside to #2/QB). Show X releasing vertically, CB sinking to ~8–10 yards and then driving to the flat on a
    shallow throw. Drop the "deep third" zone and draw a flat zone at (d 2–8, w -20 to -11).
  - Option B (keep Cover 3): CB must finish deeper than X. Move the CB end to about (18, -15.2), stop X at 16, or give X
    a 12-yard comeback with the CB driving on it. Then fix the caption: a deep-third corner "breaks on what is
    thrown in front of him **only after the vertical threat is gone**".
  - Caption: in Cover 3 the corner's eyes are on #1 through the QB, not purely on the QB.

### 2. Fig 10 left (outside zone): the play-side Sam is unblocked in the back's aiming point
- The front is a 4-3 Over (3 and 9 to the TE, Sam stacked at w≈6.4). Y reaches the 9, RG reaches the 3, and the RT
  steps outside and then climbs *back inside* to the Mike. Nobody touches the **Sam**, and the RB's track (ending
  w≈7.4) runs straight at him. A line coach would circle this first.
- **Fix (standard wide-zone rules vs Over):** C + RG combo the 3 to the Mike (C steps play-side and climbs to Mike
  once RG has the 3 covered). RT is uncovered, so he works to the Sam: a lateral step, then climb outside, ending
  near (4.0, 6.0). Y reaches the 9. LG cuts off the 1. LT cuts off or works to the Will. The backside 5 is
  left (that's QB boot/keep control; say so in the caption).
- Fig 17 uses the same OZ but gives the Sam to the FB, which is fine. The RT climbing inside to the Mike is acceptable
  there, but then the C is on nobody. Have the C combo the 3 with RG and climb to the **Will**, and say "C and RG
  combo the 3" in the answer text. The answer's "then sometimes climb to a linebacker" is right in spirit (the covered
  man stays and the combo partner overtakes), but it reads better framed as the combo.

### 3. Fig 10 right (power): the backside LB is unblocked, and the kick-out label is on the wrong line
- The RG+RT double on the 3 never climbs, so the **Will is unblocked**. On power the double team works the 3 to the
  backside 'backer ("double to Will"), and the puller leads for the play-side LB. Draw RG (or RT) coming off the double to
  the Will at about (4.2, -1.5), and keep the puller on the Mike.
- The label "F kicks out the 9" sits next to **Y's climb line to the Sam**, so the reader will read Y's
  block as the kick-out. The FB's path ends hidden under the Y circle. **Fix:** end the FB at the 9's inside hip
  (≈ d 0.7, w 5.7) with a visible block bar. Move the label below the LOS, e.g. `fsay(f2, p2, -2.0, 8.2, "F kicks\nout the 9")`,
  and add a short "Y up to Sam" label if needed.

### 4. Positional-value chart silently drops right tackles (Fig 1, `MKT_GROUP`)
- OTC codes tackles as `LT` and `RT`. `MKT_GROUP` maps `LT`, `LG`, `RG`, `C` but **not `RT`**, so right tackles
  appear nowhere in Fig 1. That matters for the football argument. The "blind side" premium has eroded:
  rushers now align over the RT as often as the LT, the top RTs (Penei Sewell, Lane Johnson) are paid at LT levels,
  and the tag treats every OL as one position.
- **Fix:** add `"RT": "Right tackle"` (or merge both into `"Offensive tackle"`) and re-check the text tiers
  ("cornerbacks and left tackles at 9 to 11 percent"). Add one sentence in the premium-group paragraph: "the
  blind-side idea is older than the data: right tackles now see as many elite rushers and are paid nearly as
  much." The glossary entry "left tackles" should then read "offensive tackles".

### 5. Edge panel of Fig 13 includes off-ball linebackers
- nflverse combine `pos == "OLB"` (310 players, 2006–2021, mean 241 lb) includes 4-3 Sam/Will **off-ball**
  linebackers. The "stand-up 3-4 OLB" ellipse at 248 lb / 4.62 sits right on that cluster, so the data "confirm"
  the archetype partly with players who never rushed.
- **Fix:** restrict to `DE` + `EDGE`. Or join `DRAFT_PICKS` and keep OLBs whose drafted position/team was
  a 3-4 edge. At minimum, say in the caption that "OLB before 2018 includes off-ball linebackers". (Minor:
  `DL`, 120 rows since 2018, is excluded from the interior-DL panel. Include it or say so.)

---

## SHOULD fix (nuance a coach or cap analyst would insist on)

6. **Body-weight ranges are a little off for 2026.**
   - The "4-3 DE 265–285" range is heavy. Modern hand-down ends run about **255–280** (Garrett ~272, Hutchinson ~260).
   - The "3-technique 285–305" range is too narrow. Donald was 285, but Chris Jones and Jalen Carter are ~310–315, so use **285–315**.
   - Add the modern reality in one sentence: most snaps are in nickel with four-man fronts whatever the "base"
     is, so the live split today is run-down edge vs pass-rush specialist more than 4-3 DE vs 3-4 OLB.
7. **Two-gap 3-4 is now rare; the heavy nose came back through "tite" fronts.** Add after Fig 11: Fangio-tree
   and many 2020s fronts play **4i-0-4i (tite/mint)** with gap-and-a-half rules, which revived the 330-plus-pound nose.
   The **2022–23 Eagles** drafted the two archetypes back to back: Jordan Davis (No. 13, 2022, ~340 lb at the
   combine, nose) and Jalen Carter (No. 9, 2023, ~314 lb, 3-technique). That's a perfect paired example for
   Fig 11. Verify pick numbers and weights before printing.
8. **Fig 11 labels:** both 3-4 OLBs read "B" (the gridiron default). Two identical letters look like a typo to a
   reader. Label them "S"/"J" or "O"/"O" and mention it in the caption. The 4-techs as two-gap ends are fine.
9. **Eagles film room overstates "developed rather than bought".** Kelce (6th) and Mailata (7th) are right, but the
   Eagles also spent premium picks on the line: Lane Johnson (No. 4, 2013), Landon Dickerson (2nd, 2021), Cam
   Jurgens (2nd, 2022). The development engine has a name: **OL coach Jeff Stoutland** (2013–present). Add one
   sentence. The callout title should also follow the contract "Film room: <team> <season>", e.g. "Film room:
   Philadelphia Eagles, 2014–2025".
10. **Purdy window nuance.** Purdy was a 7th-rounder, so there was **no fifth-year option**. The window was always
    going to close once he became extension-eligible after year 3, which is why it lasted three seasons and not
    four or five. Optionally add that rounds 3–7 picks get the **proven performance escalator**, which would
    have raised his 2025 salary anyway.
11. **The franchise tag uses CBA position buckets, which is where scheme meets money.** All OL share one tag price
    (tagging a guard costs tackle money), and DE vs LB tags are argued over for 3-4 edge players. The best
    example is **Jimmy Graham, 2014**: tagged as a TE, he filed a grievance to be paid the WR tag because he lined up
    in the slot or wide on most snaps, and **lost** before the July deadline. That's a great one-paragraph
    illustration of "role vs position" that also sets up 14-02. Verify the dates.
12. **Cap mechanics a cap analyst would add** (one or two sentences each):
    - **Top-51 rule:** from the new league year until the season, only a team's 51 largest cap hits count. "$14M
      over" in Drill 1 is a top-51 number, and cutting a player saves his hit minus the replacement 52nd man.
    - **Post-June 1 savings arrive on June 2.** A post-June 1 designation in March leaves the full cap hit on the
      books until June 2, so it **does not help clear space before free agency**. Drill 1's answer should say this
      (it's why "release before June 1" is the right column).
    - **Unused cap space carries over** to the next year. One clause explains why some teams "bank" room.
13. **Wilson timing (Denver film room).** The real reason for the March 2024 date was that **$37M of his 2025 salary
    vested as guaranteed on the fifth day of the 2024 league year**. That was also the backdrop to the late-2023
    benching. One sentence makes "dead money as sunk cost" concrete. Check the figure; it was widely reported.
14. **Compensatory-pick formula:** only players whose contracts **expired** count, and players who were **released**
    don't. That is why comp-chasing teams sign cut veterans freely. Add half a sentence.
15. **Scouting card tweaks (Fig 8):**
    - Interior DL stand-ins should include **arm length** (the two-gap trait the text stresses).
    - Corner film traits should include **hip transition / opening the hips**, the classic CB grade, and
      **run support / tackling**, which matters for Cover 2 and Cover 3 corners.
    - Tackle feet: "kick-slide" is one dialect. Many lines now use vertical, 45 and jump sets, so say "pass sets
      (kick-slide, jump sets)".
16. **Takeaways vs Fig 1 ordering:** the takeaway lists "edge rushers, left tackles, receivers and corners". The
    chart shows edge, WR, IDL, CB, LT. Reorder it and include interior pass rushers to match the chart and glossary.
17. **"roughly 24 different jobs":** 22 starters plus K, P and LS is 25, before returners. Say "about 25".

## Nits / checked and fine
- The contract anatomy (Fig 4) arithmetic is right: 15/30/35, restructure 35→19, +4 in years 4–5, $8M of void
  acceleration, March cut 30 dead / saves 5, post-June 1 split 10/20. The calendar (Fig 5) dates are sensible.
- The Rams 2021 trades, the Lance and Purdy details, the 49ers OL picks, the Trent Williams trade, the roster rules
  (48 with 8 OL, PS 16+1 with 6 vets, 2 elevations a game and 3 per player, IR 4 games and 8 returns, emergency 3rd QB) are consistent
  with FACTS-current and the factcheck log. The Miller trade is announced Nov 1, 2021 in many reports, with the deadline Nov 2;
  the text's "On November 2, at the trade deadline" is borderline, so re-check it or say "at the trade deadline".
- Fig 12 (left): press alignment one yard off, square on X, is fine. The `p.read("QB", key="CB")` sight line correctly
  draws the CB's eyes to the QB.
- Fig 17 drill: Prospect A/B measurables are realistic for a guard (4.45 shuttle at 305 lb is genuinely excellent),
  and the answer is the right football answer.
- The Fig 3 claim "four of five reached a conference title game, three a Super Bowl" checks out (KC 2018 AFCCG; BAL 2019
  lost in the divisional round; PHI 2022, SF 2023, NE 2025 reached the SB).
- No labels are clipped by the field edge in Figs 10–12 and 17. The only collision is the "F kicks out the 9" label/line confusion (item 3).
- Library note: the gridiron default OLB label "B" (players.py) produces duplicate letters in 3-4 pictures. Flag
  it for the library owner; don't edit it here.
