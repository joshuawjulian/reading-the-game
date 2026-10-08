# 13-04 Tendencies: PROE, Personnel, Motion, and Coverage — coach / film-analyst review

Reviewed: `chapters/13-analytics-and-data/13-04-tendencies-proe-and-charting.qmd` and
`pdfs/13-04-tendencies-proe-and-charting.pdf` (built 2026-10-08 08:21, 38 pages). I looked at every
page, with the field diagrams (Figs 1, 8, 12, 13, 14) at 100-110 dpi. I checked numbers against
nflverse 2025 data in the `rtg` container. The scripts are `_pdfbuild/13-04-coach/chk.py` and `chk2.py`.

**Verdict:** the analytics are strong and honest, and the caveats section is excellent. The
problems are on the football side. One diagram is clearly wrong: in Fig 8 the pass rush goes
straight through an offensive line that never blocks. Three pre-snap pictures leave a slot
receiver with no defender over him. Several tendency readings miss things a defensive staff
would raise right away: pistol is a run look, RPOs, the Rams' shotgun tell, 6-OL "heavy" sets,
and FTN's hash column. None of these needs a rewrite. Each is a local fix.

---

## A. Diagrams: must fix

### A1. Fig 8 (`fig-coverage-rotation`): the four rushers run through an offensive line that never blocks
- **What's wrong:** `rot.rush(k)` with no `pts` sends E, T, T and E straight at the QB's launch
  point, and no OL `block` is drawn. In the +0.5 s frame the four rushers are already a yard behind
  the OL. At +1.2 s they are 3 yards deep in the backfield. At +2.1 s all four sit on top of the QB
  (about 7 yards deep), while five offensive linemen still stand on the LOS. In print this reads as
  a four-man jailbreak sack. It is the opposite of a normal Cover 3 snap, and it pulls the eye away
  from the safeties, which are the point of the figure.
- **Fix:** use the 06-03 and 06-06 `protect()` convention. Set the OL with
  `p.block(k, pts=[(-1.2, 0.0)])` for LT, LG, C, RG and RT, and give the rushers
  `p.rush(k, pts=[(-1.6, 0.0)], speed=2.0)` so they engage and stop. Copy the helper into the
  chapter. Don't import it from 06-06.

### A2. Figs 12, 13 and 14 (and Fig 8 before the snap): one slot receiver has nobody over him
gridiron's `defense("nickel", ...)` puts the nickel ($) over #2 on one side only (see the
`formations.py` comment "nickel/dime over the #2 receivers, more crowded side first"). The other
#2 is left to a Will stacked in the box at w ≈ -2. A QB would see a free throw before the snap:
"uncovered slot, throw hot."
- **Fig 12 (drill 1, singleback 11 vs nickel single-high):** H is the left slot (w ≈ -9, off the
  ball). The $ is on the right at (5, +5.3), just outside the inline Y, and stacked under the SS.
  Nobody is within 6 yards of H. **Fix:** move NB over H: `NB.moved(d=5.5, w=-7.5)`, the apex
  between LT and H. The SS stays down on the Y side at about 7 deep, which keeps the 7-man box
  this run-look drill wants (4 DL + M + W + SS).
- **Fig 14 (drill 3, gun 2x2 vs nickel two-high):** $ is over Y (+9), and H (-9) has nothing
  underneath. **Fix:** walk the Will out to an apex on H, `WILL.moved(d=5.0, w=-6.0)` (06-06 does
  exactly this with `p.moved(d=5.0, w=-6.0)`). That gives a 5-man box plus M, a light box. The
  caption already says the defense is "conceding the short run", and the light box makes that true.
- **Fig 8 before the snap:** the same 2x2 picture has the same hole on H, so apply the same Will
  apex. After the snap he already drops to the left curl-flat, so the rotation is unchanged.
- **Fig 13 (drill 2, Vikings mug):** this one is structural. Six men are on or near the line, two
  safeties sit at 12, and two corners cover X and Z. That leaves only the $ (over Y), so H is
  uncovered. Real two-high mug looks handle this in one of two ways. They play the safeties
  shallower, over the slots (a "cap"), or they come out in dime. **Fix (pick one):** (a) set
  FS/SS at `(9.5, ∓8.0)`, over the slots, so the picture reads "two-high, slots capped". That is
  still a two-high shell, and it is how these pressure looks really present. Or (b) keep the
  picture, and add one sentence to the answer: the uncovered left slot is the offense's built-in
  hot or sight-adjust throw, and it is the first thing a QB checks against six-man pressure.
- **Also in Fig 13:** the front leaves both B gaps empty. The DTs sit at w = ±3.6 (outside shade
  of the tackles, a 5 technique) and the ends at ±7.0 (a very wide 9). The usual double-A-gap mug
  puts 3-techniques beside it, so every gap has a threat. **Fix:** `SDT/WDT: (1.0, ±2.4)`,
  `SDE/WDE: (1.0, ±5.5)`.
- **Note for the gridiron maintainer:** the nickel helper should apex the weak #2 (Will to about
  (5, ∓6)) when there are two slots. I have not edited gridiron.

### A3. Fig 1 (`fig-snap-as-data`): two small football fixes
- Z motions from about w = +15 to +8.6, a reduced split, but the right corner (C) stays over Z's
  old spot at w ≈ +15. Real corners travel with the receiver. **Fix:** move RCB inside with the
  motion, to about (7, +10). One way is a defender path drawn as a pre-snap adjustment. Another is
  to place him at his post-motion spot and say so in the caption.
- The 4-3 Sam linebacker is labelled "S", directly below "SS". The legend in the Predict-the-play
  section lists only M and W. **Fix:** add "S, the Sam linebacker" to the caption, or to the legend
  paragraph before the drills.
- (Optional) FTN also carries `n_defense_box`. Saying that the two files can give different box
  counts for this snap would sharpen the "7 or 8?" label.

### A4. Fig 8 (rotation): naming and depths
- What the figure shows is a **buzz** rotation: the safety comes down to the hook/curl and the
  nickel takes the curl-flat. 06-03 teaches sky, buzz and cloud. **Fix:** name it in the caption
  ("a buzz rotation, see [Cover 3 family](../06-pass-coverage/06-03-cover-3-family.qmd)").
- The FS ends at 15.5 yards and the corners at 15. 06-03 says the post safety plays the middle at
  "about 17 to 18 yards deep". **Fix:** use FS `(17.0, 0.0)` for consistency. The corners can stay
  at about 15.
- The RB's "flat" (`r.flat(1.5, 5)` from 5 deep) is still about 3.5 yards behind the LOS at
  +2.1 s, so it is really a swing. **Fix:** call it a swing in the code, or use
  `r.flat(6.0, 5)` so it gets to the flat.
- The four frames (-0.5, 0.5, 1.2, 2.1) tell the story well in print once the rush is fixed. The
  chapter has only one animation, which is within the limit.

### A5. Cosmetic
- Field numbers ("40", "50", "30") sit behind X and Z in Figs 8, 13 and 14. Receivers really do
  align "on the numbers", so this is realistic. Leave it, unless you want to set `lateral=(-20, 20)`
  and nudge the receivers to ±14.
- No labels are clipped and none collide in Fig 1 or the drills. The charts (Figs 2-7, 9-11) are
  clean. The scouting card has no overlaps.

---

## B. Tendency readings a coach would correct

### B1. Pistol is a run alignment, but the text groups it with shotgun
- 2025 data, neutral early downs: league pass rate is **30% from pistol**, 34% from under center
  and 71% from shotgun. Atlanta was in pistol on **43%** of its snaps, and Washington and Miami on
  25%.
- The dashboard bullet lists "Washington, Atlanta, Cincinnati, Philadelphia and Kansas City were in
  the shotgun or pistol ... pass-first offenses". Atlanta's low under-center share is mostly pistol,
  which is a run look (Bijan Robinson's offense). It is not evidence of a pass-first team.
- "Grading the card" gives the baseline as "shotgun means pass, under center means run", and the
  Watch-for-it box says the same. 08-02's own caption gives pistol as "two to three in ten" passes.
- **Fix:** write the baseline as "**under center or pistol** means run, shotgun means pass". In the
  dashboard, either add a Pistol column or define the tell column as "under center or pistol (run
  looks)". Rewrite the bullet so Atlanta is described as a pistol team.

### B2. The Rams' biggest tell is the shotgun, and the card shows it but the text skips it
- The card's own QB panel shows the Rams **passing on 89% of shotgun snaps** (132 snaps; league
  71%). Under center, they passed 46% (league 34%).
- A defensive coordinator would circle this first. Against the 2025 Rams, the under-center tell was
  broken, and the gun look was close to a certain dropback, an even louder tell than usual.
- **Fix:** add one sentence to "Walk the card" ("...and the flip side: when Stafford was in the gun
  on an early down, it was a dropback about nine times in ten"). Add a clause to the Drill 1 answer
  too. Guard the number with an assert.

### B3. PROE measures the play that was run, not the play that was called
The chapter repeatedly calls PROE "the play-caller's choice". Several common mechanisms break that
equivalence, and a coach would insist on a short caveat. The natural home is the "Common
misconception" box after the Eagles, or the caveats list.
- **RPOs:** FTN `is_rpo` covers **7.6%** of 2025 neutral early-down snaps league-wide, and 23% of
  them end as dropbacks. The QB's read after the snap decides whether the snap counts as a run or a
  pass. Kansas City (18% of neutral early downs), the Giants (16%), Tennessee (15%), Cincinnati
  (13.5%) and the Jets (13%) were the heaviest users.
- **Checks at the line:** run/pass "kill" calls and check-with-me. Stafford and McVay are the
  textbook case, so even the opening's "the Rams threw when they didn't have to" is partly the
  quarterback's choice, not the coordinator's.
- **Screens** count as dropbacks, even though they work as an extension of the run game (Pittsburgh
  ran screens on 18% of neutral early-down dropbacks). **Scrambles** count as passes, which the
  chapter already notes. **Designed QB runs** count as runs.

### B4. "Cincinnati and Kansas City used play-action least ... don't need the fake" is incomplete
Both are top-five RPO offenses (KC 18%, CIN 13.5%). Their run action comes as run/pass options
rather than as play-action. **Fix:** "...used play-action least, and both were among the heaviest
RPO users: their run-pass conflict comes from options, not fakes."

### B5. "Heavy" misses six-offensive-linemen sets
`personnel_code` counts backs and tight ends only, so a 6-OL jumbo set with one TE codes as "11"
or "12". In 2025, **6.2%** of neutral early-down snaps had six or more OL. The leaders were
Pittsburgh (120 snaps), Houston (95) and Arizona (87).
- **Fix:** count OL as C+G+T from the 2023-on strings, or the "OL" token in the older strings. Add
  `ol >= 6` to the heavy flag, and name 6-OL in the dashboard caption. This matters most for the
  heavy-personnel bullet and its NGS "fewer than three WRs" comparison.

### B6. "What the card can't say" understates the FTN file
The text says the public files don't record "the hash". FTN has `starting_hash` (L/M/R, filled on
essentially every 2025 snap). It also has `n_offense_backfield` (an empty, 1-back or 2-back proxy),
`is_qb_out_of_pocket` (boots and movement passes), `is_rpo` and `is_screen_pass`.
- **Fix:** take the hash out of the "can't" list and add a sentence saying it's available. Better
  still, add a hash split to the card's offense panel, or at least to the "try it yourself" line.
  Field/boundary tendencies are a staple of every pro tendency report. Receiver splits, bunch/nub,
  route concepts and run scheme really are missing, so keep those in the "can't" list.

### B7. Drill 3 answer: "a team that needs two scores and wants to use clock between them"
That reasoning runs backwards. A trailing team wants to *save* clock. The sound reasons for running
here are different. At 6:10 with timeouts there is time for two possessions. A two-high shell with
a light box gives away 4-5 free yards. And a run avoids a sack or turnover on first down. **Fix:**
"a team down 10 with 6:10 and its timeouts still has time for two drives, and a two-high defense
is handing it a light box and four free yards."

### B8. Cover 9 is used but never defined or linked
Cover 9 appears in the coverage table, Fig 9 and the card legend. The term is owned elsewhere, and
`gl-cover-9` exists (06-03 links it). **Fix:**
- Link [Cover 9](../../appendices/glossary.qmd#gl-cover-9) at its first use, in the prose before
  the coverage table.
- In the Fig 9 caption, say that FTN's COVER_9 is usually a single-high match variant, which is why
  it is shaded blue. Note that 06-06 counts it in neither the one-high nor the two-high group. This
  chapter's `TWO_HIGH` already excludes it, so the numbers agree with 06-06.

---

## C. Checked and correct, or acceptable (no change)
- Fig 1: 12 personnel ace with 7 on the line (X, OL, Y; U attached) is legal. 4-3 over is right vs
  two tight ends: 3-technique and Sam to the Y side, the SS at 7 yards outside Y as the box
  question. The ball is on the left hash, and the hash spacing is right.
- Figs 12-14: offensive alignments are legal (X and Z or Y on the line as appropriate, slots off the
  ball). Depths are realistic: corners 7 off, single-high FS about 13, two-high safeties about 12,
  linebackers 4.5-5. The singleback RB is at about 7.
- Drill 3's run path (offset back, crossing the QB's face to the right A/B gap, ending on the Mike
  at about 4 yards) matches "handoff for 4 yards".
- Fig 12 caption, "run about two times in three": the league pass rate in 11 personnel under center
  on 2025 neutral early downs is **33%**. The Rams were at 54% (151 snaps), consistent with the
  answer text.
- "Almost everyone runs on third-and-1": neutral third-and-1 has a 23% pass rate (2023-25). "Almost
  everyone throws on third-and-8": 97%. Both are fine. "Inside two minutes of the first half
  everyone throws" is really about 80%. Consider "four snaps in five".
- The `n_blitzers` vs `number_of_pass_rushers` distinction (a sim pressure has a blitzer but four
  rushers) is exactly right. The Vikings film room ("blitz usually travels with man, Flores broke
  that link") is well chosen, characterized accurately, and consistent with 06-06.
- "Defenses play more man on third-and-medium" (26% to 49%) is correct and well explained.
- Rotation logic (two-high shell, FS to the post, SS down, corners bail) is sound football apart
  from the A1 and A4 items.
- The Eagles 2024 film room (Barkley plus a new play-caller in Kellen Moore, PROE down about 13
  points) and the Petzing example are both well chosen for "PROE belongs to the play-caller".
