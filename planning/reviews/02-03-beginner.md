# Beginner review: 02-03 Classic Formations

Reviewer persona: casual NFL watcher, never played. Has read 01-01 to 01-06, 02-01 and 02-02 only.
Read the source qmd start to finish and every page of `pdfs/02-03-classic-formations.pdf` (24 pages; figures
re-rasterized at 130 dpi where 60 dpi was too small to read). Prose is about 8,700 words against a ~4,000-word
target.

**Verdict:** strong chapter. The "read it from the back to the front" idea, the anatomy plate, the
trade-off line ("every player you keep in the backfield is a blocker or a runner you gain, and a receiver you
lose"), the one-page backfield sheet and the 2025 revival data all work for me. The problems are: (a) the
blocker-counting logic contradicts itself between the goal-line section, Drill 2 and Drill 3; (b) the rule for
what counts as a "back" (wing, H-back, slotback, wingback) is never settled, and the Watch-for-it rule breaks
on the chapter's own plates; (c) the Pro set and Wing-T threat diagrams contradict or tangle the text; (d) the
history and film rooms run long.

---

## 1. Terms used before they are explained, or never explained

| Where | Quote | Problem |
|---|---|---|
| Flexbone "Why there?"; reason 3 under "Why the classic formations faded"; Ravens film room; Drill 3 title | "takes them out of the box"; "six defenders in the [box]"; "count the defenders in the box"; "the I against eight in the box" | **Box** belongs to 02-05, which I haven't read. The only gloss is a bare link in reason 3, and that comes *after* the flexbone use. Drill 3 and the Ravens "what to notice" both depend on it. Give a one-line gloss at first use, around the flexbone ("the area near the ball, roughly between the tight ends and within about 5–7 yards of the line"). |
| Goal-line heading and paragraph | "more blockers than defenders have gaps"; "a defender for every gap between and outside those blockers" | **Gap** belongs to 03-01. Never glossed here. The heading doesn't parse on a first read. |
| Family tree (Fig 3) | "Split-T, 1941"; "Wishbone, 1968 (after the veer)" | Neither the **Split-T** nor the **veer** appears anywhere in the text. The veer turns up again in "from the wishbone and veer to the spread option." Two dangling names on the map I was told is "the map for the rest of the chapter." |
| End of the option section | "came back to the NFL from the shotgun, as the zone read" | **Zone read** gets no gloss. A casual fan has heard it, so give one clause ("the QB reads one unblocked defender and either hands off or keeps it"). |
| Wing-T "Why it exists" | "buck sweep series", "a trap up the middle", "Defenders who flow with the first thing they see" | **Trap** and **flow** are undefined. "Buck sweep" is half-explained. |
| Wing-T caption | "on a reverse or counter … roll out away from the flow (the bootleg)" | Reverse, counter and flow are all unglossed. |
| Short-yardage paragraph | "The quarterback sneak, and its push-assisted cousin" | Too coy. Just say "the 'tush push'" and link it. I had to guess. |
| Iso caption (Fig 5) | "a base 4-3 defense" | 01-03 drew this matchup, but the chapter never says what "base" or "4-3" means. The pro-set caption and drill captions rely on it too. One parenthetical would fix it: "(four linemen, three linebackers, four DBs)". `base43()` has that in its docstring, but the reader never sees it. |
| "Why the classic formations faded" | "the NGS formation labels in the participation data" | Body text in data-plumbing jargon. Move it to the footnote. |
| Pro set caption | "slip out into a short pass route to his side (the flat)" | **Flat** is used three more times (table "backs in the flats", 49ers film room). This gloss makes it sound like a route; it's an area ("the short zone near the sideline, within a few yards of the line"). |
| Wing-T plate vs goal-line plate | the letter **W** | W means a wingback (aqua, a back) in the Wing-T, a third tight end (gold) in the goal line, the wide receivers in the flexbone, and the **Will** linebacker on defense. The ring legend even lists W under both "running back" and "tight end". **H** means a halfback (T, pro set, Power I, Wing-T), a slot receiver (singleback plate) and the H-back (Fig 9). **T** means tailback on offense and defensive tackle on defense in the same figures. Too much overloading for a chapter whose whole job is reading letters. |

## 2. Leaps (a missing or assumed "why")

1. **The blocker arithmetic contradicts itself.** This is the biggest problem.
   - Goal line (Fig 12): "9 blockers" vs "11 defenders, all in close". Drill 2's answer says "nine blockers
     against eleven defenders … it wants to win with numbers." To me 9 < 11 means the offense is *losing*
     the numbers.
   - Drill 3's answer: "eight players near the line against the offense's seven blockers … one more defender
     than the offense has blockers. That's the defense's answer."
   - So 8 vs 7 is bad for the offense but 11 vs 9 is good? The missing idea is that the ball carrier and the
     QB don't block, so the question is always "box defenders vs blockers", plus who is too far away to
     matter. That idea has to be stated once, in the body (the goal-line "Why it exists" is the place), with
     the count actually done. The goal-line paragraph promises "arithmetic" but never adds anything up.
2. **The iso: "the one defender nobody else blocked"** (Fig 5 caption). The two safeties and two corners are
   also unblocked. Why don't they count? (They're 10+ yards away or covering receivers. That's the box idea
   again.)
3. **The Pro set's figure contradicts its text.** The text says "a back who takes a handoff from a split
   alignment is usually running at an angle, sideways first." Fig 4's right panel draws both run arrows going
   *straight ahead*. Either draw the angled path or reword. Also, "the lead blocker … has to cross in front of
   the ball carrier": why is that bad? (Timing? The runner's view?) One clause would do it.
4. **Power I: "the two lead backs take the two linebackers who would otherwise make the tackle."** A 4-3 has
   three linebackers. Which two, and who takes the third? No figure shows the Power I in action. A static
   play like Fig 5 would pay off "two lead blockers."
5. **The H-back motion (Fig 9): "One player moving changed which side was strong."** After the motion there
   is a tight end on each side, which by this chapter's own ace logic is *balanced*, not "strong left."
   Explain what "strong" means after the motion (the extra blocker is now on the left, and Y is alone on the
   right?).
6. **What counts as a "back"?** Watch-for-it says "A tight end standing off the line next to a tackle (an
   H-back) counts as a blocker, not a back, for naming." But the Wing-T's wingback (just outside and behind
   the TE) and the flexbone's A-backs (off the line outside the tackles) *do* count as backs: 31 and 30
   personnel. Fig 9's "H-back" stands in a wing spot, while 02-02 placed the H-back "in the backfield behind
   the tackle". From the couch I can't tell a TE from an RB by body type. Give one explicit rule ("count by
   who they are, from personnel; position alone can't tell you") and note the exceptions.
7. **"Under center with one back: closer to even, still play-action heavy"** (Watch for it). No number in the
   chapter supports this. Every under-center stat is for two backs or all plays. Add the one-back figure.
8. **Drill 3's answer: "look downfield … at the receiver on the side away from the deep safety."** The safety
   is drawn in the middle of the field, so why is one side open? The answer also says the run is "often aimed
   away from the extra defender." Neither idea was taught. Both are 02-05 / 06-xx content showing up in an
   answer key.
9. **Reason 1 for the decline: "a pass gained more on average than a run."** I learned EPA in 01-02 and I want
   the number (EPA per dropback vs per run), not just a link to 13-02.
10. **Personnel codes.** In the table, "T-formation | 32 (or 22)": how do three backs fit 22 personnel? In the
    goal-line text, "23, or 13 with a fullback swapped for a tight end": 13 personnel has one wide receiver,
    which contradicts "no wide receivers at all" in the same sentence and in the glossary. The arithmetic I
    learned in 02-01 says this is wrong. Explain it or fix it.
11. **"I has really only three quick receivers"**, and two pages later the 49ers fullback "slips out into the
    flat." Reconcile this ("on play-action the fullback becomes a fourth receiver precisely because nobody
    expects it").

## 3. Diagrams I couldn't decode, or captions that don't say what to notice

- **Fig 11, Wing-T "What it threatens":** four dashed arrows in one color cross in a knot behind the QB. I
  can't tell which back runs which path. The "dive" arrow is mostly hidden under C/Q, and the "dive" and
  "counter" labels sit far from their arrows. Use one color per back, or split it into small multiples.
- **Fig 9, H-back strip:** at −1.1 s the S and M labels sit on top of each other. At +1.0 s the running back
  R is hidden under the ball, so "the running back following him" can't be seen. An unlabeled blue dot past
  the line near W (the climbing LT) looks like the ball carrier. The H blocking E also overlaps E.
- **Fig 6, iso strip:** the caption says "By 0.6 seconds he is crossing the line," but the 0.6 s frame shows F
  still about a yard behind it. At 1.9 s the tailback's T is under the ball marker and the M/W boxes, so
  "through the hole, past the linebackers" isn't visible. Label the ball carrier, or ring him in every frame.
- **Fig 3, family tree:** the icons are about 3 mm wide in print. The single-wing icon has a dark-blue "QB"
  dot that is really the blocking back, so it looks like a QB under center, which is the opposite of the
  point. The T-formation box is blue ("still seen in the NFL") while the table says "rarely." The arrow from
  Singleback to Shotgun implies the shotgun descends from the one-back set, but the text dates the shotgun to
  1960.
- **Fig 2, T-formation:** the leader for "a back in the middle and one on each side" points at the *left*
  halfback, not the middle.
- **Fig 4, Pro set:** the "flat" arrows end near the line of scrimmage, inside the receivers, so "flat" reads
  as a direction rather than an area. See also leap 3.
- **Drill 1 caption** gives the answer away: "the fullback (F) stands behind the left guard, the tailback (T)
  seven yards deep behind the quarterback." Cut it to the situation plus the letter key.
- **Fig 16, backfield sheet:** the Wing-T's W and the goal line's W stand in the same place. Only the ring
  color separates them, and nothing on a broadcast does. Say so in the caption, which ties to leap 6.
- **Missing:** the Lombardi film room says the power sweep is "the signature play" but only links to a drawing
  in 11-01. A pro-set chapter with no pro-set play drawn misses its best picture.
- **Missing:** everything is drawn from above (All-22 view). The skill I'm promised is naming formations "on
  sight" on a broadcast, where the main camera is high and to the side and depth is foreshortened (01-06
  taught this). One sentence or one inset on how an I vs a pro set looks on the TV angle would help a lot.

## 4. Drag and repetition

- **The flexbone film room** (Johnson's I-AA titles, Navy 0–10, the Orange Bowl, Niumatalolo, Reynolds's
  record, Newberry, Cronic's "Millennial Wing-T") is the longest film room, for a formation the chapter says
  "You won't see … in the NFL." The paragraph about the three-way invention dispute adds more. Cut by about
  half.
- **Stats repeated:** the 27% / 73% neutral figure for two backs under center appears three times (I gives up,
  Drill 1, Drill 3), and the goal-line three-in-four / four-in-five figures appear twice (body, Drill 2). Drill
  2's answer is close to a paraphrase of the paragraph three pages earlier, so it tests short-term memory, not
  reading.
- **"Downhill"** is introduced as new ("what coaches call running *downhill*"), but 02-02 already taught it.
  Link it instead.
- "A formation your grandfather would recognize" appears twice (hook and Ravens film room). The callback is
  fine, but it's noticeable.
- The I-formation history paragraph (Nugent, Hollister, Zuppke in the footnote, McKay, Coryell, Garrett,
  Simpson) is fine. With T, pro set, I, wishbone, flexbone, Wing-T, Gibbs and Lombardi together, the chapter
  is about 50% history by feel. At roughly 8,700 words against a 4,000 target, trim the history.

## 5. Can I do each "You'll be able to…"? Drills attempted before opening the answers

- **Name the formations on sight:** yes from top-down plates, thanks to the backfield sheet. Not confident on
  a TV angle (see §3), or when a TE stands off the line (see leap 6).
- **Say what each was invented to do and what it gives up:** mostly yes. The flexbone's cost is never stated
  (what does it give up versus the wishbone, inside power?). The ace has no stated cost of its own.
- **Match formation to personnel:** yes, with the table, apart from the 22-for-T and 13-for-goal-line puzzles.
- **Explain the decline, and where it survives:** yes. The data section is the chapter's strongest part.
  "21 personnel" as one of three "places" is a category mix (the other two are situations), but I understood it.
- **Use the backfield as a pre-snap clue:** yes.

**Drill 1 (my answer before opening):** offset I, offset weak (FB left, TE right), 21 personnel; lean run,
probably toward the fullback, left. **Result:** correct. But the answer then says "smart offenses vary it so
the clue means little," so the "which way" part can't be graded. Give a league rate for runs toward the offset
FB, or drop "which way" from the question. The caption also gave away the formation.

**Drill 2 (mine):** run, likely a lead or sneak; if a pass, play-action to a tight end, probably the wing.
**Result:** correct, but only because the body said the same thing a few pages earlier. I was confused by
"nine blockers against eleven … win with numbers" (leap 1).

**Drill 3 (mine):** safety came down because two backs under center says run; the offense might run anyway or
use play-action over the top. **Result:** I got the gist. I did not get "aim the run away from the extra
defender" or "the receiver on the side away from the deep safety," because neither was taught (leap 8).
"Eight vs seven" contradicted my takeaway from Drill 2.

## 6. What I still wonder (the chapter should answer)

1. How do I count blockers vs defenders properly, and who "doesn't count"? (Leaps 1–2. One paragraph here,
   with a forward link to 02-05.)
2. On TV, how do I tell an I from a pro set, or a wing from an on-line tight end, from the sideline camera?
3. When a tight end lines up in the backfield as a fullback (the misconception box mentions "an offset I with a
   tight end at fullback"), is it 12 personnel in an I? What do I call it out loud? The chapter teaches that
   personnel and formation can disagree but never walks through one example.
4. What is the one-back, under-center pass rate in 2025? (Leap 7.)
5. Do NFL teams actually run toward an offset fullback more than half the time? (Drill 1.)
6. Why did the shotgun become *less* popular in 2024–25 if it is "a better place to pass from"? The revival
   paragraph gives the defense-got-lighter reason. A sentence on what changed on *offense* (wide zone and
   play-action efficiency, QBs like Stafford comfortable under center) would close the loop with reason 4,
   college QBs.
7. The team scatter shows the Ravens in the top-right quadrant (x≈35%, y≈28%), but the text's list of top-right
   teams ("the 49ers, Seahawks, Bills and Patriots") leaves them out. Did I misread, or should they be named?
8. What's the pistol's relationship to these formations? The pistol shows up in the FTN chart (29% pass rate,
   51% play-action, both closer to under center than to the shotgun), but the chapter sends it to "the next
   chapter's world." The data says otherwise and deserves one sentence.

## Small fixes

- Hook: "stand a 300-pound fullback and a 247-pound running back, seven yards deep" reads as if both are
  seven yards deep.
- Misconception box: "a singleback with the back in the pistol." The pistol is a QB depth, so "with the QB in
  the pistol"?

---

## Revision (2026-10-06): finding -> action

Covers this review and `02-03-coach.md`. Fact-check entries are untouched; every new factual claim is footnoted
(`[^splitt]`, `[^veer]`, `[^epa]`, `[^ucepa]`, expanded `[^neutral]` and `[^bellard]`) and every new number is
asserted in the chapter code. Build: `build_pdfs.py 02-03-classic-formations --html` OK, 28 pages, every diagram
page re-rasterized and inspected (60 dpi, strips and goal line re-checked at 110–140 dpi).

### Beginner review

**§1 Terms**
- Box -> glossed at first use, now the iso section (link to 02-05), with the full count explained there; flexbone re-glosses briefly.
- Gap -> glossed in the goal-line "Why it exists" (link to 03-01); the goal-line heading was rewritten ("shrink the field, pick the spot").
- Split-T and veer -> new paragraph under the family tree (Faurot's 1941 wide line splits and QB pitch read; Yeoman's mid-1960s Houston triple option, which Bellard drew on), with sources.
- Zone read -> one-clause gloss plus link to 03-04.
- Trap, flow, buck sweep -> each glossed in the Wing-T "Why it exists"; trap links 03-03, buck sweep/waggle 03-05.
- Wing-T caption's reverse/counter/flow -> caption replaced (see §3); counter described in its panel.
- Tush push -> named outright, linked to 10-03, noted as still legal in 2026 (FACTS §5).
- "Base 4-3" -> spelled out (four linemen, three linebackers, four DBs) in the text before the iso, linked to 02-05.
- NGS jargon -> moved to the footnote; body says "the formation labels in the public data".
- Flat -> defined as an area in the pro-set caption, and drawn as a shaded area with the release arrows ending in it.
- Letter overloading -> tailback is now R everywhere (T now only ever means a defensive tackle); flexbone receivers are X and Z; the goal-line wing TE is H (the H-back letter), so W is only the Wing-T wingback and the Will; ring legend no longer lists letters; new "letters in this chapter's diagrams" key after the anatomy plate explains the two deliberate double-duty letters and that the ring settles it.

**§2 Leaps**
1. Blocker arithmetic -> stated once, with the count done, in the I-formation section (blockers = everyone but QB and ball carrier; box defenders only; "hat on a hat" vs one extra defender). Iso 7 v 7, Power I 8 v 8, Drill 3 8 v 7, goal line 11 v 9 (the defense always wins the count there, so the offense shrinks the gaps and picks one spot). Drill 2's "win with numbers" removed. New takeaway "Count, every time".
2. "The one defender nobody blocked" -> removed; text explains why corners and deep safeties don't count in the first second.
3. Pro set figure vs text -> text rewritten per coach (split-back runs hit fast; the cost is the deep tailback and a lead blocker who must cross, which costs a beat and needs timing); arrows now go straight at the near holes, matching the text.
4. Power I "two linebackers" -> new static figure `fig-power-i` (8 blockers v 8 in the box, SS walked down; F on the Sam, H on the safety, Y turns the end, RT down, RG/LG climb) and a count paragraph.
5. H-back "strong left" -> strip redrawn (coach option B) and text now says the formation is balanced after the motion but the defense is still set right; the line didn't flip, so the offense runs at the 1-technique side with an extra blocker.
6. What counts as a back -> new rule in the opening section: name the formation by where players stand, the personnel by who they are; exceptions (wingback, A-backs, H-back) explained; Watch-for-it bullet rewritten; H-back now starts at 02-02's H-back spot (behind the tackle).
7. One-back under-center rate -> computed: 38% passes, 78% play-action (neutral, 2022–25); in the I section, footnote and Watch-for-it.
8. Drill 3 "side away from the safety" / "away from the extra defender" -> answer rewritten: the run away from the walked-down safety makes him chase; coverage language per coach (single-high, Cover 1 one-on-one or Cover 3 window behind the LBs), linked to 06-02/06-03.
9. EPA numbers -> added: dropbacks +0.04 vs designed runs −0.05 EPA/play in 2025; +0.03 vs −0.07 over 2006–2025; dropbacks ahead every season (asserted).
10. Personnel codes -> T is 32 only; goal line is 23 / 14 / jumbo (text, table, glossary).
11. "Three quick receivers" vs fullback in the flat -> reconciled in the I's costs bullet (play-action makes the fullback a fourth receiver because nobody is watching him).

**§3 Diagrams**
- Wing-T knot -> replaced by a 2x2 small-multiple "buck series": same backfield action, one bold ball carrier per panel, fakes gray, pulling guards dark blue.
- H-back strip -> custom box-zoomed strip with gold/aqua rings and per-frame notes; no S/M overlap; R ringed so he's visible; frame 2 moved to −0.6 s so H is clear of Q.
- Iso strip -> custom zoomed strip, F and R ringed every frame, frames at 0 / 0.85 / 1.35 / 2.2 s; captions now match ("arrives at the line"; R through and past the LBs at 2.2 s).
- Family tree -> icons ~25% larger; single wing now legal (seven on the line) with TB/FB separated and the dark-blue blocking back explained in the caption; T box now gray (matches "rarely"); split-T icon widens the line, not the backs; dashed "direct snap returns" edge from the single wing to the shotgun, so the shotgun no longer appears to descend only from the singleback.
- T-formation leader -> "a back in the middle" now points at F; labels moved inside the 1.5-yard margin.
- Pro set flats -> see §1.
- Drill 1 caption -> no longer gives away the formation.
- Backfield sheet -> caption says the Wing-T W and goal-line H stand in the same spot and only personnel separates them.
- Missing pro-set play -> declined to redraw: Lombardi's sweep is already drawn block by block in 03-03 (which exists); the film room now links there instead of the unwritten 11-01. The chapter now has three drawn plays (iso, Power I, H-back motion) plus the Wing-T series.
- Missing TV angle -> new section "What the backfield looks like on TV" with `fig-tv-view`, a perspective sketch from the sideline camera: an I reads as a row, split backs as a stack.

**§4 Drag**
- Flexbone film room cut by more than half (Orange Bowl, Niumatalolo, Reynolds, Army streak, Navy coordinators dropped); invention dispute down to one sentence.
- Repeated stats -> 27%/73% stated once (I section); Drill 1 and Drill 3 no longer repeat them; the goal-line figures appear once (body); Drill 2 now tests the count instead of paraphrasing the body.
- "Downhill" -> linked to 02-02 instead of re-taught.
- "Grandfather" -> second use removed.
- History trimmed: I-formation, Wing-T dates, Lombardi, Gibbs, Ravens film room tightened.
- Length: declined to cut to 4,000. Net prose grew (to roughly 10,500 words including callouts and drills) because the two reviews asked for substantial additions (count logic, back-counting rule, letters key, TV view, terminology dialects, EPA, one-back and pistol data, revival's offensive side). Every addition answers a specific finding; the cuts above removed the drag the review named.

**§5 Drills**
- Drill 1 -> "which way" now asks which side the fullback is set up to lead to (gradeable); answer explains that public data can't say how often teams run toward the offset (FTN records backfield count, not offset side) and points to tracking data in 13-05.
- Drill 2 -> new question: count blockers and box defenders; answer works the 11 v 9 logic.
- Drill 3 -> "Do the count" added; answer uses the 8 v 7 count and the corrected coverage language.
- "21 personnel" as a category mix -> kept (it's the curriculum's own objective wording) but the survive section now says "two situations and one kind of team".

**§6 What I still wonder**
1. Counting -> see leap 1. 2. TV angle -> new section. 3. TE at fullback -> rule plus worked phrase ("an I with 12 personnel"). 4. One-back UC pass rate -> 38% (neutral). 5. Runs toward offset FB -> honest "not in public data" answer. 6. Why the gun fell -> revival now gives the offensive side: under-center dropbacks +0.14 vs shotgun +0.03 EPA (2024–25, selection caveat stated) and QBs comfortable under center. 7. Ravens in top right -> named ("just over the under-center line"; 2025: 34.9% UC, 28.7% two-back). 8. Pistol -> new paragraph: 29% pass, 51% play-action in 2025, a cousin of the under-center sets.

**Small fixes** -> hook reworded ("a 300-pound fullback and, seven yards deep, a 247-pound running back"); misconception box says "the quarterback in the pistol".

### Coach review

1. Wishbone roles reversed -> fixed: backside halfback is the pitch man (hence the deeper alignment), playside halfback leads on the pitch-support defender; sourced in `[^bellard]` (Wikipedia quote).
2. Iso -> LG now blocks the Mike (target, after the Mike's path); FB path aimed at the B gap from his first step; RB path offset inside the FB; leader points at the FB's block; caption rewritten ("four linemen and Y block the man in front; LG climbs to the Mike"; the bubble clause; 7 v 7); strip frames moved so 0.85 s says "arrives at the line" and 2.2 s shows R past the LBs.
3. H-back strip -> option B (Sam stays; Will widens, Mike bumps), run left with H on the end, LT to the Will, LG to the Mike, C on the 1-technique; "the line didn't flip" nuance and the Sam-travels alternative in text; label collision gone.
4. Single-wing icon -> weak end added (seven on the line); TB/FB separated; caption explains the dark-blue blocking back.
5. Pro set "sideways first" -> rewritten as suggested; diagram consistent.
6. Cutback -> added to the I's "Time to see" (link 03-02).
7. "Home of the modern run game" -> "a main home of zone running, alongside the I".
8. Dialects -> Strong I / Weak I added as glossary aliases of Offset I and in text; I Pro / I Twins / I Slot paragraph; "Heavy" replaced with "Deuce"; Near/Far/Split mentioned.
9. 23 -> 14 fix in text, table and glossary.
10. Goal-line plate -> DL at d 0.5, LBs ~2.0, DBs within 4.6; goal-line splits 1.25 via a local `line5(split)`, TEs at ±3.9, wing at 5.2; nine gaps numbered on the figure.
11. Drill 3 coverage language -> rewritten as suggested.
12. 49ers "What to notice" -> "watch where the fullback's path ends" (slice-and-leak to the flat), and Juszczyk leads on "a linebacker or the edge defender".
13. "A step or two" -> "a few strides".
14. Wing-T -> "same backfield action"; waggle named and defined; down blocks and pulling guards described and drawn.
15. Family tree -> split-T icon widens the line; dashed single-wing-to-shotgun edge.
16. Shotgun drop -> "takes a shorter drop and never has to turn his back".
17. Hook -> fixed.
18. Wishbone halfbacks -> widened to ±3.1 (behind the tackles).
19. H-back naming rule -> folded into the new back-counting rule and Watch-for-it ("a tight end directly behind the quarterback still makes it an I").

### Notes for other agents
- gridiron was not edited. The chapter defines its own box-zoomed `strip`/`video`/`panel` (ported from 03-01) because `gridiron.frame_strip` fits all 22 players and has no rings, and a local `tv_project` perspective helper for the sideline-camera sketch.
- `defense("4-3_over", ..., off)` puts the right cornerback over the tight end (w 4.8) when there is no receiver on that side (Power I); the chapter moves him by hand.
