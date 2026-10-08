# Beginner review: 13-05 Tracking Data and the Big Data Bowl

Reviewer persona: a casual fan who has never played and is comfortable in Python. I have read Parts 1-12 and
13-01 to 13-04 in order. I read the chapter source and the rendered PDF
(`pdfs/13-05-tracking-data-and-big-data-bowl.pdf`, 48 pages, built 08:51, newer than the .qmd), rasterised at
60/100/120 dpi.

**Overall:** strong. The opening question pays off, the chapter play runs through the whole chapter, and
orientation vs direction, standardising (Fig 4) and the separation-over-time chart are the best teaching in
Part 13. The two biggest problems: **all three Predict-the-play drills give the answer away in visible code**,
and **two statements contradict earlier chapters** (QB motion, buzz/cloud). After those come about 15 pages of
simulator plumbing that slow the read.

---

## 1. Terms used before they're explained, or never explained

| Where | Quote | Problem |
|---|---|---|
| §The columns, chapter-play paragraph; Fig 2 caption | "H a short **arrow** route to the flat" | "Arrow" is not in the term index and is never glossed. The route chapter taught flat, slant and the rest, but not arrow. Gloss it ("a short angled route to the flat") or say "flat route". |
| Fig 7 caption | "at the top of his **stem**" | Owned by 04-03 but not linked. I had to remember it. |
| §Orientation, para after Fig 3; Project 1 trap | "A corner in **off coverage** backpedals…", "Man corners play with **leverage**" | Neither is linked (off coverage is owned by 06-01). Every other borrowed term in the chapter is linked, so these stand out. |
| "What is public" table; Fig 7 caption | "**cushion**", "as the cushions close" | Owned by 06-01, not linked. |
| Fig 12 caption | "pinches in toward the **hole**" | Hole zone (06-01) is not linked. |
| §Feature 3 | "displacement since the **`line_set`** event" | `line_set` appears only in the event list and is never defined. Whose line, and set when? The shift rule depends on it, and I couldn't tell how a shift (players reset, then set) can show up *after* "line set". |
| §The columns table, `time` row; §Drawing | `time` = "The wall-clock timestamp of the frame" vs `prepare()` "adds `time` in seconds from the snap" | One column name has two meanings. The orientation cell uses `one["time"] * FPS` three paragraphs before the reader is told `prepare()` rewrote it. |
| §Orientation cell (Fig 3) | `one = bdb.prepare(...)  # offense now moves toward +x` | `prepare()` does the standardising before standardising is taught (next section), and the `one`, `LOS`, `BALL_Y`, `d`/`w`, `frame_rel` setup is buried in a figure cell. The chapter admits this later ("The `one` table was built that way in the orientation figure's cell above"). Move the setup into its own visible cell after §Lining plays up, or add one sentence at the orientation cell saying what `prepare()` is about to do. |
| §Step 3 | "the **rotation onset**" | Fine as a chapter-local term, but it's bold and used in a takeaway with no glossary entry. Either add it or drop the bold. |
| §Pocket code | "Andrew's monotone chain", "shoelace formula" | Named, never explained. See §4. |
| Coordinate section (Fig 1) | (missing) | The chapter never says that after standardising **+y is the offense's left and low y its right**. I first learn it in the Drill 3 answer ("drifting toward low y, the offense's right"). Without it I could not decode "FS … dir ≈ 150°" in Fig 3 or the sign in `w = ball_y − y`. Add one line and an arrow label to Fig 1, e.g. "offense's left (+y)" at the top sideline. |

## 2. Leaps: a missing or assumed "why"

1. **Contradicts 02-06 on QB motion.** §Feature 3: "Linemen and the quarterback are excluded; **they can't legally be in motion**." 02-06 taught me that "Z, H, the back and the quarterback are backfield players: any one of them may go in motion." Which is right? Say instead "linemen can't be in motion; the quarterback is excluded because his small movements in the cadence are noise".
2. **Contradicts 06-03 on buzz/cloud.** §Step 4: "a real defense can rotate *and* play two-high (a 'buzz' or 'cloud' rotation changes who has which zone without changing the shell)." 06-03 defined both buzz and cloud as **Cover 3** rotations, which end one-high. As written I'd conclude Cover 3 is two-high. Use a genuinely two-high example (Cover 6 rolling to the field, a quarters check) or explain what is meant.
3. **"Left hash" vs "outside the hashes."** Fig 2 caption: "the free safety spins **from the left hash**". The safeties sit 7.5 yd off the middle, and Fig 1 puts the hashes about 3.1 yd off the middle. The code's own docstring says "two-high safeties 13 deep, **outside the hashes**". I checked this against Fig 1 and it doesn't match. Fix the caption.
4. **Step 3 promises code it doesn't show.** "With rotation onset as a column, the measurement 06-06 sketched becomes **a few lines of pandas**: the share of a defense's two-high looks that rotate, and the median onset". Then no lines appear; there is only a comment in the eval:false cell. Disguise as "two numbers per defense" is a takeaway, so show the groupby (4 lines on `onsets`).
5. **Ambiguous phrasing.** Same paragraph: "A defense with **both high** is the hardest to read". Next to "two-high" this reads like a coverage shell. Say "with both numbers high (it lies often, and late)".
6. **Unrealistic acceleration, unexplained.** The raw-rows table shows the corner with `a` = **12.9** yd/s² at frame 45, and 0.64 while standing still at frame 3. The text warns that "careful analysts smooth the data before taking derivatives" but never connects that warning to these numbers or shows smoothing. A demanding reader asks: is 12.9 real (over 1 g)? Either say it's a simulation artefact of unsmoothed differences, or show a rolling-mean smoothing step.
7. **The text overstates the table.** "look at the last three rows … he is moving at about 3 yards a second". The first of those rows shows `s` = 1.87. Say "speeding up to about 3".
8. **Why ignore `dir` below 0.5 yd/s, when Drill 3's C has s = 0.5 exactly?** The rule in §The columns is "ignore frames with `s` below about half a yard a second", and the drill's answer says to ignore C's `dir`. Under the rule as stated, C is the borderline case. Either pick a frame where C is clearly lower or restate the threshold (the motion section uses 1.0).
9. **Why simulate team depths at all?** §Safety depth, team by team: the dots in Fig 14 are random draws from a two-cluster simulator. The only real information is the right-hand "two-high share" column, so the caption's "The distribution splits into two clusters for every team" is true by construction. I'd rather see a bar or dot chart of the **real** shares, perhaps with one simulated strip as an illustration. As it stands, 7 inches of print show noise around one real number per team.
10. **Fig 5 caption vs picture.** "deep ones keep climbing". In the right panel every line flattens by about frame 12 (the deepest at about 16.5 yd), so nothing keeps climbing. The left panel also starts at 0 and drops to −7 in two frames. Nothing says that this is the shotgun snap travelling back to the quarterback, and I paused there.
11. **The printout "frames before the throw: 57"** is never explained. It holds about 3 s of pre-snap frames plus the time to throw; say so, or drop the print.
12. **The pocket paragraph confuses.** "a defensive tackle driving the center back shrinks the space the quarterback can step into **without changing the hull much**". The center is one of the six hull points, so pushing him back should change the hull. Explain (for example, the center is interior when the tackles are wide), or pick a cleaner example.
13. **Fig 14 is followed directly by "Film room: Seattle 2025".** SEA appears in Fig 14 at 46%, but that is **2022, before Macdonald**. A reader will connect the two. Add a clause such as "(the chart's 2022 Seattle predates Macdonald)".
14. **The 2021-2024 rows of the BDB table are vague.** "Measures of coverage and defensive back performance", "Return and coverage-unit measures", "Tackle-probability and missed-tackle measures". No winner and no named metric are given, unlike 2020, 2025 and 2026. One named idea per row would make the claim "their winning ideas changed how the league measures the game" concrete.

## 3. Diagrams I couldn't decode, or whose captions don't say what to notice

- **Fig 1 (coordinates):** good overall. Missing the +y = offense-left label (see §1). The "offense moves toward +x (after standardising)" text sits on the top sideline and yard lines. It is readable, but it's on the field edge.
- **Fig 3 (orientation vs direction):** the arrows are 3.2 yd long and partly hidden under the markers. The FS arrows in particular are tiny at print size, and the dashed green on the FS is hard to see. "Left end" (whose left?) should be "the defensive end on the offense's left". The QB is drawn as the football icon (brown ball over a blue dot), which a first-time reader may not take for the quarterback.
- **Fig 4 (standardising), panel (a):** the **"Z" label collides with the "QB" label** ("Z" sits under the Z dot and "QB" above the QB dot; they touch). In (d) the "X" and "Z" labels sit on the LOS line. Otherwise this is the best figure in the chapter.
- **Fig 6 (frame strip):** the text below it claims "The robber is in place by about one second; the quarterback releases the ball before Z has broken". Neither moment is in the strip (frames are −1.5, 0, +1.5, +3.2), so in print I can't verify the chapter's main timing point. Swap +1.5 for the throw frame (`T_THROW`, about 1.95 s), or add it as a fifth frame. In the +3.2 panel, X and his corner sit on the top edge of the window (convention (c)).
- **Fig 9 (pocket):** the left panel is cramped. The T and E markers overlap the hull outlines, and at the throw I can't tell which outline is which. Draw the three hulls in three different colours or line weights and add a small legend.
- **Fig 10 (motion):** the caption promises "the first half-second after" in the top panel, but the speed lines stop at frame 0 (the code filters `frame_rel <= 0`).
- **Fig 12 (rotation, 60 plays):** the caption says "the thick lines barely move before frame 0". The green and orange medians visibly start bending at about −8 in both panels, because the 8 early rotations pull them. Say "start to bend about 8 frames early, pulled by the 8 early rotations".
- **Fig 16 (routes):** clear. The top-row panels have no x tick labels, so readers can't read the dig and out widths. Also, "other 0 of 95" is 10% of all routes; one more sentence on why stopped curls fall through would help.
- **Fig 17 (Drill 1):** at print size the defenders' trails are 1-2 yd stubs and almost invisible. The caption says "Watch the defenders' trails", but the evidence isn't visible. The corners are labelled **"CB"**, while the key above the drills says "C a cornerback" and every other figure uses "C" (the `nickel_vs_2x2()` relabel causes this).
- **Page 46 layout:** the line "Answer 3 is at the end of the chapter. Try it first." runs into the bottom border of the callout and the page number.

## 4. Drag and repetition

- **About 15 of the 48 pages are simulator plumbing:** `as_bdb_rows` (about 60 lines), `write_week`, `nickel_vs_2x2`, `_seg`, `sim_dropback`, `sim_coverage`, `jitter`, and the matplotlib for every figure. The ideas I'm meant to learn (`standardise`, `align`, `separation`, `safety_tracks`, `rotation_onset`, `stickiness`, `route_features`/`classify`) are short and sit among them. Fold the simulator and plotting cells (`code-fold: true` per cell, "Show the simulator") and keep the feature functions open. In print, a reader skims past several pages of `ax.text(...)` per figure.
- **Hand-written convex hull (Andrew's monotone chain plus the shoelace formula):** about 20 lines of computational geometry the reader doesn't need. 04-02 already has `convex_hull`, and `scipy.spatial.ConvexHull(pts).volume` gives the area in one line. Use that, and keep the football point.
- Disguise as "how often it lies, and how late" is stated in Step 3, again in Project 3, and in the Takeaways. Step 3 and the Takeaways are enough.
- Fig 11 (one play) and Fig 12 (60 plays) are both justified ("one play is an anecdote"). Fine.

## 5. Can I do each "You'll be able to…" item?

| Objective | Can I? |
|---|---|
| Read a tracking file: what one row is; x, y, s, a, dis, o, dir; where (0, 0) is | **Yes.** The columns table and Fig 1 are clear. The one gap is which sideline +y is for the offense. |
| Flip plays left to right; line plays up on the snap or the throw | **Yes.** `standardise()` and `align()` are short and explained, and Fig 4(b) vs (c) makes the mirror trap stick. |
| Draw and animate any play with gridiron | **Mostly.** `show_animation(prepare(...))` is clear, but I never see a real-data frame. Every real-data cell is eval:false, so I'm trusting that it works. |
| Compute separation, pocket area, motion at the snap and safety rotation, and say what each misses | **Yes.** The "what it misses" paragraphs are the chapter's strongest habit. |
| Sketch three projects | **Yes** for man/zone and routes. Project 3 (disguise) points to 06-06 for the result and code, so I can describe it but not run it from this chapter. |
| Recognise BDB themes and what the winners had in common | **Yes** for themes and the five habits. Winners for 2021-2024 are missing (§2.14). |

**Predict the play, attempted before opening the answers:**

- **Drill 1 (motion, nobody follows).** My answer: zone, because H crossed and no defender went with him. Two safeties at 13 at the snap still leave Cover 2, 4 or 6, or a late rotation to Cover 3, open. That **matched** the answer. **But the drill is spoiled by visible code.** The cell above the picture is `def zone_motion_play():` with the comment `# bumps toward the motion, two or three yards`, so the function name *is* the answer. And at print size the trails I was told to watch are barely visible, so I answered from the code and from H's long trail, not from the defenders.
- **Drill 2 (read the chart).** My answer: one-high shown (A deep in the middle at about 13, B down at about 8 and 6 off the middle) and two-high played (both 15-18 deep, about 10 wide). It starts about 8 frames before the snap, so the QB could see it, and `rotation_onset()` returns `None` because neither ends within 2.5 yd of the middle. That **matched** the answer, and it is the best drill: it tests whether you understood the rule's conditions. **Also spoiled:** the visible cell is `sim_dropback("spin2", rng_d, tau=-0.8)`, which gives away both the kind ("spin" to two-high) and the timing (0.8 s early) before I look at the chart.
- **Drill 3 (read the rows).** My answer: A backpedals (o ≈ 272, dir ≈ 100); B runs a route (s 7.5, o ≈ dir ≈ 150); C stands still (s 0.5), so ignore his dir. That **matched**. **Spoiled again:** `mystery = {"LCB": "A", "H": "B", "RB": "C"}` is printed in the cell, so the identities in the answer ("the left corner", "H", "the running back") are given away. C's s = 0.5 sits exactly on the stated 0.5 threshold (§2.8).

**Fix for all three:** hide the drill figure code (`#| echo: false`, or fold it with a neutral name such as `drill_play_1()` and no comments), and rename `mystery` to something neutral.

## 6. Knowledge gaps: what I still wonder

1. **Getting the data.** What exactly do I type? (`kaggle competitions download -c nfl-big-data-bowl-2025` after `pip install kaggle` and an API token.) How big is it (several GB unzipped), and will a week fit in pandas memory? The Step 4 code loops week by week "to keep memory sane" but never says how big a week is.
2. **Smoothing.** The chapter tells me careful analysts smooth before derivatives but never shows how (rolling mean? Savitzky-Golay?), or whether the BDB's own `s` and `a` are already smoothed. Given the 12.9 yd/s² row, I want this.
3. **Known quirks in the real files.** The chapter promises the simulated files have the "same quirks", but lists only direction, wobble and 53.3. Are there others I should know about (orientation offsets in some releases, missing ball rows, plays with no snap event)?
4. **What a real frame looks like.** One figure or screenshot of a published real play (even an NGS graphic) would show me how much messier reality is than the clean simulated lines.
5. **How the broadcast ring is made live.** The hook asks how far to trust "separation 3.1". I now know it's nearest-defender-at-arrival, but is the live number the same computation, and how fast is it available?
6. **Defining "throw" in the 2026 files.** If the input/output files split at the throw, how do I find the throw frame there? It isn't an event in that layout, is it?
7. **Can tracking see the ball in flight?** "The ball can carry a chip too", but then is the in-air ball path in the BDB files real or interpolated?

## Priority fixes

1. Hide or neutralise the drill code so it doesn't give answers away (all three drills).
2. Fix the QB-motion statement (contradicts 02-06) and the buzz/cloud two-high claim (contradicts 06-03).
3. Fix "from the left hash" in the Fig 2 caption.
4. State that +y is the offense's left in the coordinate section and on Fig 1.
5. Put the throw frame in the Fig 6 strip; widen the window so X and his corner aren't on the edge.
6. Fold the simulator and plotting code; replace the hand-written hull with scipy.
7. Show the Step 3 "few lines of pandas"; fix "both high", the Fig 12 "barely move", the Fig 5 "keep climbing" and the Fig 10 "half-second after" captions.
8. Fix the Fig 4(a) Z/QB label collision, the "CB" labels in Drill 1 and the page-46 callout overflow.

---

## Revision (2026-10-08): finding -> action

Re-rendered with `build_pdfs.py 13-05 --html`: OK, 40 pages (was 48), zero errors. Every figure page was rasterised and checked (pp. 4, 6, 9-11, 14, 19 and 36 at 100-150 dpi). Fact-check claims are unchanged. New claims are sourced: 2021-2024 winners in a new `[^bdb-winners]`, Seattle's 54.8% / 46% in `[^twohigh]`, and route label sets in `[^route-labels]` (my tabulation from nflverse).

### This review (beginner)

| Finding | Action |
|---|---|
| §1 "arrow" never glossed | Glossed in Fig 2 caption ("an angled route to the flat"). |
| §1 stem, off coverage, cushion, leverage not linked | Linked to `gl-stem`, `gl-off-coverage`, `gl-cushion` (now with a one-line gloss in the "What is public" table) and `gl-leverage-inside-outside` (also glossed). |
| §1 "hole" unlinked (Fig 12) | Caption now says "toward the middle". |
| §1 `line_set` undefined; shift after line set? | Defined in Feature 3: the frame the *offensive line* is set. Skill players may still shift or motion after it, hence `shiftSinceLineset`. The motion table gains a `shifted` column. |
| §1 `time` has two meanings | The column table now gives both. The `one` setup moved into its own visible cell (`prepare-one`), with a paragraph on `prepare()`'s three jobs, before the first figure that uses it. |
| §1 `prepare()` standardises before standardising is taught | Same paragraph: it says what `prepare()` does and that the next two sections build it by hand. |
| §1 "rotation onset" bolded with no glossary entry | Bold dropped (chapter-local term, italic). |
| §1 Andrew's chain / shoelace | Hull moved to a folded helper. Text points to `scipy.spatial.ConvexHull(...).volume`; the container has no SciPy, so the helper stays. |
| §1 +y = offense's left never stated | New second "fact" bullet. Fig 1 labels both sidelines ("high y = the offense's LEFT", "low y = the offense's RIGHT"). Angle bullet adds 0/90/180/270 in offense terms. |
| §2.1 QB motion contradicts 02-06 | Rewritten with the rule: one player, off the line, not toward the line. Linemen can't move; the QB almost never does. Added an `assert`-style data-quality check (2+ movers = shift not set, flag, or glitch). |
| §2.2 buzz/cloud two-high claim | Replaced by quarters rolling to Cover 6, plus invert Cover 2 as a trap (deepest-defender rule follows the wrong men). Buzz and cloud are named as Cover 3 rotations (link 06-03) that the rule does catch. |
| §2.3 "from the left hash" | Chapter-play safeties moved to w = ±6. Caption: "from just outside the left hash". Fig 11 caption: "about 6 yards off the middle". |
| §2.4 "few lines of pandas" not shown | New `disguise-profile` cell: groupby with rotate_share and median_onset (`per_play` keeps non-rotations as NaN). |
| §2.5 "both high" | Now "scores high on both (it rotates often, and its median onset sits at or after the snap)". |
| §2.6 a = 12.9 unexplained | New paragraph: the simulator starts players instantly, and differencing amplifies noise. New `smoothing` cell compares raw vs 5-frame-smoothed speed and acceleration on the standing corner. Savitzky-Golay is mentioned. |
| §2.7 "about 3 yd/s" overstated | Inline-computed values (now about 2.2, dir ≈ 273, o ≈ 92). |
| §2.8 0.5 threshold vs Drill 3 C | One threshold, 1 yd/s, everywhere. C is now 0.1 yd/s (the RB is set, not drifting). |
| §2.9 simulated team depths are noise | Replaced by a real dot chart of each team's two-high share (Fig 15), plus a new simulated depth × width figure (Fig 14) that teaches why the shell needs width. |
| §2.10 Fig 5 "keep climbing"; initial dip | Caption explains the dip (shotgun snap plus drop; annotated on the chart) and says each line climbs until the catch, then levels. |
| §2.11 "frames before the throw: 57" | Explained inline (pre-snap seconds plus snap-to-throw, computed). |
| §2.12 pocket/center paragraph | Rewritten: the hull measures enclosed area, not where it is. A center driven back becomes interior, so the area barely changes. |
| §2.13 2022 SEA vs Macdonald | Clause added after the team chart (Macdonald coached Seattle from 2024; per 12-08). |
| §2.14 vague 2021-2024 rows | Each row now names the winning idea (2021 man/zone and defender grading; 2022 returner optimal path; 2023 "Between the Lines" pocket pressure; 2024 "Uncovering Missed Tackle Opportunities"), sourced in `[^bdb-winners]`. Habit 2 and takeaways reference them. |
| §3 Fig 1 label on field edge | Direction arrow moved inside the field (boxed). Sideline labels added; compass enlarged. |
| §3 Fig 3 small arrows, "left end", QB icon | Arrows 5 yd and thicker, with a legend. Ball not drawn, so Q shows. "End on the offense's left". The end's label moved off his path. |
| §3 Fig 4 Z/QB collision; (d) labels on LOS | Labels now sit behind each dot, away from the ball arrow. (d) labels are boxed above the markers, with a taller window so FS clears the edge. |
| §3 Fig 6 throw frame missing; X on edge | Strip is now −1.5 / snap / throw / catch, with titled panels. A custom fixed-window strip (`strip()`, folded) gives ≥2 yd margins and larger markers. |
| §3 Fig 9 hull outlines indistinct | Three colours and line styles plus a legend; wider window. |
| §3 Fig 10 "half-second after" not shown | Speed lines now run to +5 frames; caption explains the post-snap climb. |
| §3 Fig 12 "barely move" | Caption: the 8 early rotations pull the medians into a gentle bend about 8 frames early. |
| §3 Fig 16 no x ticks on top row; "other" | Tick labels on every panel. New paragraph on the "other" group and the threshold trade-off (inline count). |
| §3 Fig 17 trails invisible; "CB" labels | Drill strip uses thick (2.8 pt) opaque defender trails and a tighter window. `nickel_vs_2x2` labels corners "C". |
| §3 page-46 overflow | Gone in the new layout (checked p. 36). |
| §4 ~15 pages of plumbing | Simulator (`as_bdb_rows`, `write_week`, `nickel_vs_2x2`, `_seg`, `sim_dropback`, `sim_coverage`, `jitter`), the hull and all plotting moved into folded web-only cells ("Show the simulator" / "Show the plotting code"), left out of print. Feature functions stay visible. New paragraph in "The data this chapter uses" explains this. |
| §4 disguise repeated 3× | Removed from Project 3; kept in Step 3 and Takeaways. |
| §5 drills spoiled by code | All drill cells are `echo: false` with neutral names (`drill_play_1`, `pick3`). Drill 2's answer values are inline expressions, not a code cell. Drill 3 letters only A/B/C. |
| §6.1 getting the data, size | New "Go deeper: getting the real files" callout (accept rules, Kaggle CLI + token, unzip; week sizes by arithmetic; load a week at a time with `usecols`). |
| §6.2 smoothing | See §2.6. |
| §6.3 known quirks | Listed in the same callout (missing snap event, short pre-snap recordings, ball rows without `nflId`, 2026 split). |
| §6.4 a real frame | A paragraph after the real-data cell says what real plays look like. **Declined** showing a real frame: no BDB data is downloaded, and NGS graphics can't be reproduced here. |
| §6.5 live broadcast ring | **Declined**: no verifiable source on the live computation. |
| §6.6 throw frame in 2026 files | Answered: the throw is the seam, so the last `input_` frame is frame 0. |
| §6.7 ball in flight real or interpolated | **Declined**: could not verify. The chapter keeps only the sourced "chip in the ball". |

### Coach review

| Finding | Action |
|---|---|
| A1 man matchups | Nickel aligned over H at (5.5, −8.3) with `man("NB","H")`. Will over Y at (5, 6) with `man("WILL","Y")`. Same change in `sim_coverage` (man branch realigns). Text, Fig 2/6/7/10 captions and the motion panel ("nickel") updated. |
| A2 two-high depth cutoff | New section "The shell at the snap, by depth and width". `shell_at()` = the two deepest are 8+ yd, on opposite sides of the ball, each ≥3 yd off the middle; one-high = deepest within 3 yd of the middle. The prose is now "usually 10 to 14, quarters often 8 to 10". Watch-for-it and Project 3 use the width rule. I used 8 yd, not 9, so quarters safeties at 8-9 count. |
| A3 coverage played ≠ shell shown | Lead-in, caption and follow-up paragraph say "coverages played (charted after the snap) as a stand-in", and that late rotators would show more two-high at the snap. The gap is Project 3. Footnote notes 2022 labels have no Cover 9/invert codes (checked `value_counts`). |
| A4 buzz | See beginner §2.2. Used quarters→Cover 6 and invert Cover 2 rather than cloud, because 06-03 defines cloud as a Cover 3 rotation. |
| A5 comeback and timing | `r.comeback(14)` (+ a 1.5 yd/s settle back toward the sideline), route speed 6.4 (top of stem ≈2.2 s), `dropback(3.0)`, throw 2.1 s. One wording everywhere: "releases as Z reaches the top of his stem, before the break". Ball flight is ≈1.4 s because gridiron's ball speed is fixed at 18 yd/s (library note). |
| B1 strip timing and collisions | See beginner §3 Fig 6. Nickel no longer on Y. The corner on Z's hip at the catch is called out in the caption. |
| B2 RB on LT | `block("RB", pts=[(0.4, 0.5)])`: up and inside the LG. No marker overlap. |
| B3 off-man cushion | Corners steered by hand with a new `timed_path()` helper (backpedal, turn and run; RCB plants and drives). Z: about 2.0 yd at the throw, 4.3 mid-flight, 1.6 at the catch. A at 0.7 s: cushion ≈4 yd. |
| B4 safety width | ±6 in the chapter play. `sim_dropback` unchanged (5.5-8.5) to keep 06-06's seed and figure identical; its docstring already says "outside the hashes". |
| B5 robber depth | Chapter-play robber at 10 yd. `rotation_onset` threshold raised to 12. Text says robber depth runs 8 to 12 by call (06-06's 10-12 is linked). |
| B6 QB posture; shoulders vs eyes | Fig 3 caption adds the right-handed-QB note. The orientation paragraph is rewritten with the coach's wording (`o` is the chest, not the eyes). The DB facing rule now keeps o toward the QB during any slow backpedal. |
| B7 motion legality | See beginner §2.1. |
| B8 route side relative to ball; label set | `route_features()` and Fig 17 use the ball's y at the snap, with a prose explanation of the hash case. Label vocabularies come from nflverse (2022 NGS: 12 names; 2025 FTN: QUICK OUT, IN/DIG, …), sourced. The BDB `routeRan` set isn't verified, so the reader is told to tabulate it. |
| B9 Drill 2 Cover 2 | Answer: "Cover 2 (or 2-Man)", with why it's not quarters. |
| B10 Seattle film room | Kept the title and added Seattle's own numbers from the cited NFL.com article (54.8% two-high from Week 14 through SB LX, the highest of any playoff team; 46% without Julian Love), plus a Seattle-specific thing to watch. |
| B11 minor | "C" labels; sim comment fixed ("Cover 1 with a rat and a robber; RB blocks"); "most lines start high"; "high on both"; TE "flexed off the line into the right slot"; Z/QB label nudge (see Fig 4). |
| B12 separation nuance | New paragraph (play-caller manufactures separation; alignment, press and the top corner lower it), echoed in the Higgins film room and the takeaways. |

**Library notes (gridiron not edited):** `Play.man()` closes any cushion to 20% within about 1.4 s regardless of route depth, so off-man corners need hand-timed paths (worked around with `timed_path()` in the chapter). `show_animation()` doesn't pass `lateral_pad`/window through to `frame_strip()`, so a chapter-side `strip()` helper fixes the windows. `BALL_SPEED` = 18 yd/s makes long sideline throws float about 0.2 s longer than real.
