# 15-01 Watching Live — beginner-reader review

Reviewer persona: a casual fan who never played and has read only Parts 1–14 in curriculum order. Read the PDF
(`pdfs/15-01-watching-live.pdf`, 25 pages) start to finish, looked at every figure, and tried the three
Predict-the-play drills before opening the answers. Line numbers point into
`chapters/15-capstone/15-01-watching-live.qmd`.

**Overall:** a strong capstone. The "why this order" framing (each step asked when its answer becomes visible, and
each answer changes what the next clue means) is the best idea in the chapter, and Figure 1 makes it concrete. The
"what each step is worth" chart (Fig 3) changed how I'd spend the twenty seconds. Using a real NFC Championship drive
as a scored log is exactly what a capstone should do. The problems are two internal contradictions about confidence,
one drill whose picture doesn't match its answer, a handful of figure-decoding problems, and length: the PDF runs to
about 12k words including tables, captions and footnotes, against a 5k target.

---

## 1. Terms used before they're explained, or never explained

Almost everything is owned by earlier chapters and named in the text, so very few true gaps. The gaps that remain:

- **Chapter IDs on the master card (Fig 2, p4; qmd ~l.567–600).** The right-hand "where taught" column reads
  "02-01, 02-05, 08-04", "06-01, 06-06", "15-01", etc. The book never shows chapter numbers (sections are unnumbered
  and the prose always uses titles like "Motion and Shifts"), so as a reader I can't map "05-05" to anything. Use
  short titles, or Part numbers only.
- **"Part 10", "Parts 3 and 4", "Part 2" (Step 1, Step 3; l.647, l.705).** Same problem, milder: I remember chapter
  titles, not part numbers. "The situational chapters (Part 10)" would help.
- **"formation strength" (Step 3, l.703–704).** It's in the step's title and on the card, but the chapter never says
  what you *do* with the strength once you've found it. Only the run-direction second layer (l.1120, "to the
  strength") uses it. One sentence on why strength matters here (the defense sets its front and rotation to it; runs
  and the coverage rotation usually go toward it) would do.
- **Marker letters "B" and "D" in Fig 10 (snap 3, p17).** The dime defense shows four "B"s, two "D"s and "$". I
  had to guess that B = outside linebacker or edge and D = the extra defensive backs. No key or caption mention.
- **"looper" (tells table row 6, "a looper needs his weight back").** Stunts were taught in 07-01, but "looper"
  as a noun may not have been. Gloss it ("the lineman who loops around on a stunt").
- **"do-confirm" (footnote 3).** Fine in a footnote, but it's the most interesting idea in that footnote and it's
  buried. Either cut it or put one clause in the body ("you run it from memory, then glance at the card").
- **"H-back" (snap 2, p16).** Used in passing ("most likely a tight end as an H-back"). It probably appeared in
  Part 2 or 3, but a 3-word gloss would cost nothing.
- **"progression" / "read in the progression" (snap 9 and footnote 14).** The term is owned by 04-01, which is
  fine, but the footnote then goes three levels deeper into FTN codes "0", "1", "CHK", "DES", "SD". I don't need
  that to understand the snap (see §4).

## 2. Leaps: a missing or assumed "why"

1. **The chapter contradicts itself on the meaning of a missed 90% call.** "Why a number" point 1 (l.1047):
   *"A 55% call and a 90% call that both miss are different mistakes. The first was honest uncertainty; the second
   was a misread."* Then the misconception box (l.1142): *"'My 90% call missed, so I was wrong.' Not necessarily:
   one in ten 90% calls should miss. You can't judge a single probabilistic call by its outcome."* As a beginner I
   came away unsure which lesson to believe. Fix point 1 so it talks about a pattern: a *pile* of missed 90% calls
   is a misread; a single one isn't.
2. **"Rarely above 90" is undercut by the chapter's own data.** The rule (l.1068) says to cap at 90, and the
   takeaway repeats "rarely go past 90". But the step 1 table shows 3rd-and-7-to-10 is a pass **94%** of the time,
   and Fig 6 shows the model's 90–100% band is **right 94%** of the time on 20% of all snaps. So capping at 90 makes
   me *under*confident on a fifth of snaps, which the next chapter's Brier score will penalise. The real argument
   is "stay away from 99 because the tendency breakers exist", which justifies a cap of about 95, not 90. Either
   explain why 90 is still right (log ranges are coarse, human readers are overconfident on average, so a cap
   protects them) or allow 90–95 for the most lopsided spots. As written it reads like a rule the data argues against.
3. **Snap 6: why does the model disagree with the base rate it just quoted?** The text (l.1439–1444) says that
   from the shotgun in 11 personnel on 2nd-and-1, offenses threw **57%** of the time, and then *"the full model, with
   the motion and the six-man box added, makes it a coin flip the other way: run, 55%."* But the chapter has just
   spent a section showing that motion and the box add almost nothing (0.3 points). And in Fig 8, row 6, the model
   is already below 50% (about 45%) at the formation step, *before* motion and box. So the stated cause is wrong
   or misleading, and I'm left wondering why a model that sees "shotgun, 11, 2nd-and-1" says 45% when the raw rate
   for exactly that look is 57%. One sentence is needed: the model adds clues up one at a time and misses some
   combinations, so on this snap the raw base rate was the better guide. That is itself a useful lesson.
4. **Snap 6, "this is the snap where step 8 earns its place" (l.1499).** *"If you'd seen a linebacker creeping
   toward the line and counted only one safety deep…"* But in Fig 11 the Will is not shown creeping at all: both
   pre-snap frames show him at normal depth. Either draw the tell the text says I could have seen, or say plainly
   that in the reconstruction we don't know whether there was one.
5. **Second-layer run calls are promised but never shown.** Layered predictions (l.~1118–1121) offer "on a
   likely run: the direction… or the scheme family (zone, if the line steps together; gap, if a guard is set to
   pull)". (a) Whether the line steps together is visible only *at* the snap, not before it, so it isn't a pre-snap
   tell. What is the pre-snap clue for gap/pull? It isn't in the tells catalogue. (b) None of the four drive runs
   gets a direction call, and no drill asks for one. The "if pass" column even fills in coverage calls on run snaps.
   Add a run-direction call to at least one run snap (snap 1 or 4: "back offset left, so right side, 60%").
6. **Why does man coverage jump in the red zone and on short yardage?** Snaps 8 and 9 rely on "the base rate leaned
   man (70%)" in the red zone, against a 31% man rate overall. The chapter never says *why* (a compressed field
   leaves less deep space to zone off, and short yardage favours tight coverage). A clause would make the second
   layer feel like reasoning rather than a lookup.
7. **"Add it up" conclusion (l.1585).** *"…steps 4, 6 and 8 … are worth more than the base rate, so look harder
   there before you trust it."* "Worth more than the base rate" is vague and unmeasured; the drive has two coverage
   misses, which isn't evidence for that particular claim. Reword it as advice ("in the red zone, don't trust the
   base rate for coverage; that's where the motion response and the shell earn their seconds").
8. **"The Rams' under-center passing in 2025 is the textbook bait" (misconception box, l.1033).** This is stated as
   fact with no number, while everything around it is quantified. Add their under-center pass rate or play-action rate.
9. **The camera problem is named but not solved.** The first section says *"the camera won't show you all of it"*,
   and the replay case gets a fallback ("call it from the situation, write 'sit'"). But the most common live
   problem is a tight broadcast shot where the safeties and corners are off screen, so steps 6–7 can't be done
   at all. What do I write in the `shell` column then? Should I lower my second-layer confidence? I'd like one
   short paragraph.

## 3. Diagrams I couldn't decode, or captions that don't say what to notice

- **Fig 4, the tells plate (p8).** The best-looking plate, but: (a) there are no yard numbers or depth ticks, so I
  can't check "the Mike has crept to three yards" or "the right safety is shallower" without measuring between the
  5-yard lines. A small depth scale on the side would help. (b) Badges 4 (receiver split) and 6 (lineman width)
  don't point at anything visibly unusual. The caption lists the exaggerated alignments for 7, 9 and 10 but not for
  4 or 6. Is Z the reduced split? Is the left end in a wide technique? Say so. (c) Badge 1 floats behind the
  right side of the line without pointing at a particular lineman.
- **Fig 5, stance figures (p9).** The idea is good, but B ("tackle, outside foot back → pass set?") is drawn
  almost upright and walking, not as a stance. It reads as "a man standing up", not "a man in a stance with his
  weight back". A and C are nearly identical, which is fine, but then B and D (both "upright") also look the same,
  so the diagram seems to teach "upright = pass" for both positions, which the table then calls a weak tell for
  tight ends. The "line ►" marker for the A/B pair sits between B and C, so it's ambiguous which pair it belongs to.
- **Fig 8, confidence trace (p15).** I can't tell the three small dots apart. The legend lumps them together
  ("+ personnel, formation, motion/tempo"), so I can't verify the caption's claim that "the biggest moves come at
  the formation step". Give each step its own marker, or label the formation dot on one row.
- **Fig 9, nine thumbnails (p16).** The players have no letters at print size, so the captions underneath do all
  the work. That's acceptable as an overview, but "two backs" vs "one back" (the key formation fact on snaps 1, 2
  and 4) is hard to see. Consider bigger panels (two rows of 4 and 5, or 3 × 3 at full width with letters).
- **Fig 10, snap 3 (p17).** The caption says Kupp runs a "quick out on the left". In the frames, H's route first
  breaks *inside* (frame 2 shows the line heading toward the middle), then he is caught further *outside* than
  he started. I couldn't read it as an out. In frame 2 the ball icon also covers the QB, and nothing shows the
  "QB looks right first" that the caption tells me to notice (no gaze line).
- **Fig 11, snap 6 (p18).** The caption's "what to notice" is good. See §2.4: the pre-snap frames don't show the
  pressure tell the text says I could have seen.
- **Fig 15, Predict 3 (p24): picture and answer disagree.** The caption says the strongside linebacker "has had to
  walk out over the slot receiver on the right". In the picture that slot is **Y, the tight end**, and Answer 3
  confirms it ("with the tight end split out as a slot"). A linebacker on a tight end is the *normal* base-defense
  matchup, not the mismatch the freeze creates. Meanwhile the true slot receiver, **H on the left, has no defender
  over him at all** (W and M stay in the box). So the drill's premise ("the linebacker is covering a slot receiver
  in space") doesn't match its own figure. Fix: put H (a receiver) in the right slot with the Sam over him and Y
  attached or on the left, or rewrite the premise around the uncovered left slot.
- **Layout: pages 14 and 15 are about half blank** (Fig 7 and Fig 8 each float alone with empty space below). This
  is a print-layout issue, not a reading one, but it makes the drive section feel padded.

## 4. Drag and repetition

- **Length.** About 12.3k words in the PDF against a ~5k target. The biggest cuts that wouldn't cost any teaching:
  - **Footnote 14** (FTN `read_thrown` codes and the data-dictionary discrepancy, about 120 words): data-plumbing
    detail. Keep "a read in his progression, not a checkdown" in the body; move the code archaeology to 15-02 or cut it.
  - **Footnote 13** (a list of every nflverse column name) and the column list in **footnote 7**: a beginner skims
    them; one sentence of provenance is enough.
  - **Footnote 12** (Kubiak to the Raiders, Fleury, Darnold and Kupp signing dates and contract): trivia for this
    chapter.
  - **"Film room" box**: the "sources" paragraph repeats what Fig 7's caption and footnote 13 already say.
  - **Snap-by-snap prose plus Fig 7 plus Fig 8 plus Fig 9** say the drive four times. Each adds something, but the
    prose for snaps 1, 2 and 4 mostly re-reads Fig 7. Snaps 3, 5, 6, 7 and 8 are where the teaching is.
- **"Base rate"** appears 17 times. Fine as a concept, but the step 1 section, the "how do you choose the number"
  section and the layered-predictions section each re-explain "start from the base rate".
- **The two-minute and four-minute material** appears in "You'll need", in step 1, in the stoppage habit #3 and on
  the card. Step 1 plus the card is enough.
- **The tells catalogue appears twice** (the plate key and the full table) with near-identical "usually means" text.
  The table adds "why it leaks" and "how far to trust it", which are the valuable columns. Trim the plate key to
  2–4 words per tell so the two don't read as duplicates.

## 5. Can I do each "You'll be able to…" item?

- **Run the checklist in about 20 s, and know the short version:** Mostly yes. Figure 1 and the card make the
  order memorable, and I can recite 1-3-6-9 for tempo. But nothing in the chapter makes me *practise* it under
  time pressure. All the drills are static pictures. A suggestion: "pause a broadcast at the moment the offense
  sets; give yourself 10 seconds; write steps 1–9" as a warm-up before the live run.
- **Use the full tells catalogue, "saying for each … how often it lies":** Partly. I can say what each tell means
  and why it leaks. But "how often it lies" is quantified for only one tell (#3, shotgun 79% pass) plus the empty
  backfield (95%). The rest get "Medium" or "Weak". Either soften the objective or add a number wherever the data
  allows it (back offset vs run direction is surely measurable from FTN plus pbp `run_location`).
- **Say what each step is worth:** Yes. Clear, memorable, and the "expensive steps on the cheap question" line sticks.
- **Layered predictions with stated confidence:** Yes for pass-side second layers (coverage family, rush count).
  No for run-side (direction or scheme): never demonstrated or drilled (§2.5).
- **Follow a complete playoff drive:** Yes, and it's the most satisfying part of the chapter.

**Predict-the-play attempts (made before opening the answers):**

1. *First down, 21 personnel in an I-formation, eight in the box, single-high.* **My call:** run, 70%; if pass,
   play-action deep behind the linebackers. **The answer:** run, about 70%, play-action shot. **Matched.** The
   chapter (snap 7 and the misconception box) set this up well. Fair drill.
2. *Third-and-6, double A-gap mugs, two deep safeties, corners off.* **My call:** pass, about 90%. Using step 8's
   "count the deep players" rule: 4 deep leaves 7, and six rushing would leave one underneath, so not six. I said
   four rush, 55%, with a mug dropping, and the ball out quickly to the hot side. **The answer:** four rush, 60%,
   ball out in under 2.5 s near the sticks. **Matched.** But "the side a dropping linebacker has the farthest to
   run to" is never resolved to a side for *this* picture. Tell me which side (or why you can't know).
3. *Second-and-2, tempo, base defense frozen, Sam out over the right slot.* **My call:** pass, 60%, attacking the
   linebacker in coverage. **The answer:** the same. **Matched**, but only by trusting the caption. Looking at the
   picture, the Sam is over the tight end and the left slot receiver is unguarded (§3). A careful reader who looks
   at the figure will get confused or reach a different answer ("throw to H on the left").

All three drills ask about pass situations. None asks for a run-direction call or a fourth-down or clock call,
though the chapter claims both.

## 6. Knowledge gaps: what I still wonder

- What do I log for steps 5–7 when the broadcast never shows the safeties or the full box? (The most common live case.)
- How do I find a team's PROE or tendency card on game day? Step 1 says "look it up before the game", and Tendencies
  has a scouting report, but which numbers should I carry to the couch?
- Could the step 1 base-rate landmarks (the 7-row table) go on the master card? They're the anchor for every call,
  and they're not on the card I'm told to keep.
- The stoppage habit says "fourth down is its own prediction: go, kick or punt", but the final log has no column for
  it, and no confidence guidance. How do I log and score it?
- How do I score my *second-layer* coverage calls live, when I can't see the coverage on a broadcast replay? The
  drive used FTN labels; at home I won't have them until later. Does 15-02's All-22 pass handle this? Say so in one line.
- Why watch one offense for the live run, and not both teams? Is the defense half of the checklist easier or harder
  to do for the team without the ball?
- The halftime pandas snippet reads `nfc_title_q3.csv`, which I don't have. Can the CSV be offered for download, or
  shown as a 9-row table I could type in?

---

## Revision (2026-10-08): finding -> action

Covers this review and `15-01-coach.md`. The fact-check log still holds. New claims are sourced (footnotes `hash`, `jsn`, `mcdaniels`, `overconf`) or computed in the chapter's data cell from nflverse/FTN 2025. Render: `build_pdfs.py 15-01-watching-live --html` OK, 28 pages. I looked at every figure page at 100 dpi. Each footnote is referenced exactly once.

### Beginner review

| Finding | Action |
|---|---|
| §1 Chapter IDs on the master card | The "where taught" column now uses short names ("Broadcast · Clock · Tendencies", "Box math", …), and the caption says it names the part of the course. Wrap narrowed so text no longer collides with the column. |
| §1 "Part 10", "Parts 3 and 4", "Part 2" | Replaced with chapter titles and links (Third Down, The Clock, Personnel Groupings, Formation Rules and Vocabulary; "the coverage chapters", "the pressure chapters"). |
| §1 Formation strength: what to do with it | New paragraph in step 3: the defense sets its front and rotation to strength, and runs and route combinations go there. It also covers the dialect point (coach C13). |
| §1 B/D markers in Fig 10 | Snap 3's edges are now labelled E and the dime backs $ and D. The caption keys every letter. |
| §1 "looper" | Glossed in table row 6. |
| §1 "do-confirm" buried | Moved into the body as one clause; footnote shortened. |
| §1 "H-back" | Glossed at first use in snap 2. Fig 9's caption also explains F. |
| §1 "progression" footnote archaeology | `[^read]` cut to one sentence. The code/dictionary detail was dropped (15-02 can check on All-22). |
| §2.1 Contradiction about a missed 90% call | "Why a number" point 1 now talks about a *pile* of misses vs a single miss. It now agrees with the misconception box. |
| §2.2 Cap at 90 vs a 94%-right top band | Kept 90 but explained why with numbers computed in the chapter. On a call that is right 94% of the time, the Brier score is 0.056 honest, 0.057 at 90 and 0.058 at 99. Under-claiming costs almost nothing; over-claiming costs more, and people are usually overconfident (Lichtenstein, Fischhoff & Phillips 1982). Added "raise the ceiling to 95 once 15-02 shows you've earned it". |
| §2.3 Snap 6 model vs base rate | Rewritten. The model adds clues one at a time with no interactions: 44% at the formation step against the raw 57% for gun-11 on 2nd-and-1–2. The exact look (one back, motion, six in the box) is 49% on 57 snaps. Lesson: trust the exact-look base rate over a sum of clues. The false "motion and box flipped it" causal claim is gone. |
| §2.4 "Step 8 earns its place" with no tell drawn | The text now says the charting can't show whether the Will showed his blitz, so the figure draws no tell. The conditional advice is kept. |
| §2.5 Run-side second layer never shown | Added the pre-snap gap tell (guard's weight, depth, heel) to tell 1 and a paragraph. Zone is now flagged as an at-the-snap read; card line 10 updated. Added a measured note: runs from a hash split almost evenly between field and boundary. Snap 4 now makes a direction call and says plainly why this drive can't score it. Predict 1 now asks for and answers a run direction ("left, away from the walked-down safety, 55%"). Back offset against run direction can't be measured: no public charting records the offset. That is now stated in the chapter. |
| §2.6 Why man coverage rises in the red zone | Clause added with the 2025 numbers (28% outside the red zone, 46% inside) and the reason (a short field leaves zone defenders little deep space). |
| §2.7 Vague "worth more than the base rate" | Reworded as advice: in the red zone, don't trust the coverage base rate; that's where the motion response and shell earn their seconds. |
| §2.8 Rams "textbook bait" unquantified | Computed in-chapter. The Rams lined up under center on 59% of snaps (league 34%) and passed on 40% of those (league 31%). 81% of those passes were play-action. |
| §2.9 Camera won't show the secondary | New paragraph under "When the offense goes fast, or the camera won't show you": write `?` for shell, make the second layer from the base rate at ≤60%, then fill the shell in from the replay. Log table updated. |
| §3 Fig 4 tells plate | Added a depth scale (LOS, 5, 10, 15 yd). Z's reduced split is now visible: a ghost circle on the numbers with an arrow in to 9 yards. The left end is aligned clearly wide. Badge 1 sits behind the right tackle. The right safety is pinched to the hash. The caption names every exaggeration. |
| §3 Fig 5 stance figures | Redrawn. Each player has his own LOS line, and the tackle and tight-end pairs are split and titled. B is a crouched two-point pass set (caption: many tackles stand up on obvious passing downs). D stands a marked yard off the line. Labels are spaced apart. |
| §3 Fig 8 three small dots indistinguishable | One marker per step (circle, square, triangle for formation, diamond, filled circle) with a five-entry legend. The caption names the formation-step moves, which match the data. |
| §3 Fig 9 thumbnails: one back vs two | Backfield players are now drawn dark and lettered (Q/R/F) at a readable size, and the gun R no longer overlaps Q. The ball is spotted on the charted hash, and titles name it. Red-zone panels use compressed depths (coach B10). |
| §3 Fig 10 route not readable as an out; ball covers QB; no "looks right" | H now runs a 5-yard out flat to the sideline. Removed the "settle" leg (coach B9). The ball icon is hidden until the throw. A green dashed "eyes" line goes from the QB to Z until the release. New times: 0, 1.5, 2.8 (the release), 4.6. |
| §3 Fig 11 pre-snap tell not shown | See §2.4. The figure was also reworked (coach A3, B7, B8). |
| §3 Fig 15 Predict 3 picture contradicts premise | The offense is now gun trips right with Y attached and H in the slot, and the Sam is walked out over H. The answer is rewritten: six in the box against six blockers is a fair fight for a run, hence only 60%. |
| §3 Half-blank pages 14–15 | Reordered: the drive board now comes before the confidence trace, and pages 15–18 are full. Some short pages remain where a large figure can't fit (Typst doesn't float figures). |
| §4 Length | Partly done. Cuts: footnotes 7, 12, 13, 14; the film-room sources paragraph; snaps 1, 5 and 8; the split-tell paragraph; the "compare with the last draft" paragraph; the Madden box, the checklist box, "You'll need", between-snaps and the BDB box; the plate key cut to one line per tell. The two reviews also asked for about 25 additions. Net prose (excluding code and captions) went from about 10.0k to about 11.1k words of body text. **Declined** cutting to the 5k target: the capstone carries the whole checklist, the catalogue and a scored drive, and AUTHORING §2 says length follows the concept. |
| §4 "Base rate" re-explained | Step 1's why, "How do you choose the number" and the second-layer paragraph now point back to step 1 instead of re-explaining. |
| §4 Two-minute/four-minute repeated | Shortened in "You'll need"; removed from stoppage habit 3. Step 1 and the card keep it. |
| §4 Plate key duplicates the table | Plate key cut to one short line per tell. The table keeps "why it leaks" and "how far to trust it". |
| §5 No timed practice | Added a "First, a warm-up" drill to Watch for it: pause at the set, ten seconds, steps 1–9 aloud, five snaps. |
| §5 "How often it lies" quantified for only two tells | The objective is softened to "where public data can measure it". The chapter says why (offset, splits and stances aren't charted). |
| §5 Predict 2: which side? | The answer now says you can't know before the snap, because it depends on which mug drops. That is why the QB's answer is a post-snap read. |
| §5 No run-direction or fourth-down drill | Predict 1 now includes a run-direction call. Fourth down is logged as a second-layer call (stoppage habit 3, log table, card line 13). A separate fourth-down drill was **declined** because 10-04 owns it. |
| §6 Which numbers to carry to the couch | Step 1: copy PROE, under-center pass rate and play-action rate from 13-04's scouting card. |
| §6 Base-rate landmarks on the card | Card line 1 now carries 1st-and-10 ≈50%, 3rd-and-7–10 ≈94%, empty ≈95%, computed. |
| §6 Scoring coverage calls you couldn't see | One line: they are checked on the All-22 in Film Study. |
| §6 Why one offense | Added to Watch for it: one play-caller's habits make the between-snaps tally meaningful; switch teams next time. |
| §6 CSV not available | The chapter now prints the nine CSV lines before the pandas cell so the reader can type or copy them. |

### Coach review

| Finding | Action |
|---|---|
| A1 Safety width vs NFL hash | Fixed in the paragraph, table row 10, plate key 10 and the plate itself. Normal width is 8–10 yd from the middle; pinched is to the hash or within 3–5 yd; NFL hashes are about 3 yd off the middle. |
| A2 Inside leverage backwards | Fixed in the paragraph, table row 9 and plate key 9. Inside leverage is usually man: Cover 0 or press Cover 1 (the sideline is his help), or trail technique with a safety over the top (2-Man). Linked to the glossary. |
| A3 Screen-beats-blitz described the wrong screen | Rewritten in terms of numbers and leverage on a perimeter screen. "Lets the rushers through" dropped. The caption now says the screen side has three Seattle players against two defenders. |
| A4 "Both mugs drop" is not a creeper | The menu is corrected: bluff (both bail, four linemen rush), simulated pressure (one comes, a lineman drops), five-man (one comes, one drops). |
| A5 "Never rushes six" qualifier | Cover 0 sentence added to step 8 and Predict 2. |
| A6 Wrong rusher in snap 9 | The RT now protects normally. The SDT wins through the B gap past a beaten RG, and the RB helps to the other side. Caption: "interior pressure (charted: Kobie Turner)". |
| B7 Collisions in strips | Snap 6: the Will is at the line at 0.7 s, then goes wide, away from Q and R. X stays engaged with the corner. The Mike makes the tackle, and the FS and corner finish clear of H. Snap 9: the nickel's first path is pushed outside, and the RB and safety paths no longer cluster. Checked at 100 dpi. |
| B8 Strips skip the release | New times: snap 3 [0, 1.5, 2.85, 4.6], snap 6 [−1.6, 0, 0.75, 3.0], snap 9 [0, 1.6, 2.45, 4.6]. Each third panel is titled at the release. |
| B9 A quick out doesn't settle | Settle leg removed. The 12-08 Cover 9 (weak-rotation Cover 3) link is added next to the 06-01 link. |
| B10 Board: hash and red-zone depths | The ball is on the FTN hash. FTN's L/R is offense-relative: from FTN's "L" hash most screens go right, and screens go to the wide side 63% of the time (footnote `hash`). Red-zone safeties are at 9.5 and corners at 5.5. The drive log shows the hash, and the snap text uses it (snap 3 and the snap 6 screen went to the field; snap 9's quarters side is to the field). |
| B11 Stance labels, two-point | See beginner §3 Fig 5. |
| C12 Field/boundary on the checklist | Added to step 1 (with the screen-to-field number), card line 1 and the board/log. |
| C13 Strength is a dialect | Added to step 3, linked to 02-02; card line 3 updated. |
| C14 Defense matching a player | Verified in participation (snaps 1, 7 and 8: Kupp and Bobo, base; every Smith-Njigba snap drew nickel or dime). Added to step 2 and snap 2, sourced in `[^jsn]` (OPOY from FACTS-current). "Notice the defense's bets" updated. |
| C15 "Two nose tackles" | Now "five linemen and edge rushers, two of them listed on the roster as nose tackles". |
| C16 Defenses fake the motion response | One paragraph in step 4, framed through 02-06's exchange and "indicator lies" (a lean, not a read). I didn't name specific defenses: I couldn't source that particular teams do it. |
| C17 QB/center pointing as a pressure tell | Added to step 8 ("the offense reacting") and card line 8. |
| C18 Pulling-guard and depth tells | Added to table row 1, plate key 1, a new paragraph and card line 3. The "legal up to the center's waist" rule detail was **not** added because I couldn't source the rule text in-session; the tell is described without it. |
| C19 Model doesn't know it's Seattle | Snap 1 now says "offenses throw from this look too". Snap 7 adds Seattle's 2025 pass rate from 12 personnel under center on first down: 42% on 139 snaps, against 34% for the league. The coach said "far more under-center play-action than the league", but the data shows Seattle's overall under-center pass rate (32%) and play-action share (25%) are near the league, so the chapter uses the 12-personnel first-down number and says "several points". |
| C20 Two-high stat is post-snap | Reworded. NGS 42% is after the snap; before the snap, McDaniels' "65 of 70 look the same" (sourced; also in 12-08). The gap is the disguise. |
| C21 Snap 8 designed throw | Clause added. The throw was aimed 1 yard behind the line (computed from `air_yards`), FTN charts it as a designed throw, and it's a perimeter extension of the run game. |
| D wording | "Two defenders will be unblocked"; LB depth 4½–5½ yd; the snap 5 sixth-man wording. The clock-figure note was already covered by "timings vary". |

gridiron: no library edits. Chapter-local changes: `snapshot()` now draws the QB's `read` line until the throw and hides the ball icon while the QB holds it.
