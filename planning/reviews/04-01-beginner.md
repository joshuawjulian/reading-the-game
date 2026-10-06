# Beginner-reader review: 04-01 Passing Game Fundamentals

Reviewer role: casual NFL watcher, never played, has read Parts 1–3 (01-01 to 03-05) only.
Read the .qmd start to finish and every page of `pdfs/04-01-passing-fundamentals.pdf` (21 pages,
rasterized at 100 dpi). Line numbers refer to the .qmd.

**Overall:** strong, and in the same voice as the pilots. The route tree, the drop-timing chart, the
high-low frame strip and the horizontal-stretch diagram all teach. The biggest problems: (a) the
chapter runs to about 9,900 words of prose (target 5,000); (b) several internal contradictions that a
careful reader *will* catch (the horizontal-stretch text and figure disagree; the "4-yard gain on
1st-and-10 is a step backward" line clashes with the success-rate rule from 01-02; "the budget is
2.5 s" sits next to deep routes timed past 2.5 s; the "box score" tip conflates yards per catch with
aDOT); (c) the quarterback is hidden under the ball marker in several frames; (d) zone vocabulary
(deep third, curl-flat, hook defender) appears in captions before the chapter glosses it.

---

## 1. Terms used before they're explained (or never explained)

| Where | Term | Problem |
|---|---|---|
| L567, fig-option-route caption | "hook defender (M)", "curl-flat defender ($)" | First use. Curl-flat is glossed at L1007, hook zone at L1133. A caption is the worst place for a first use. Gloss inline ("the linebacker guarding the short middle", "the defender guarding the short area outside") or rephrase. |
| L765, fig-timing-route caption | "off cornerback playing a **deep third**" | Deep third (owned by 06-01) and Cover 3 aren't explained until L1009. "Off" is used throughout (L423, L1397) and never defined. One clause: "lined up several yards off the receiver" / "responsible for the deepest third of the field on his side". |
| L951 + fig-reads bar labels | **EPA** | First use in the chapter is the progression chart (bar labels "EPA +0.28"). The link and reminder ("the course's measure of how much a play changed expected points", 01-02) come only at L1232. Move the gloss and link to the first use, before the reads chart. |
| fig-reads bar "Scramble drill" | scramble drill | Appears as a category before it's glossed at L1360. The caption says only that these throws "sit outside the progression". Add "(throws after the play broke down and the QB ran around)". |
| L875, fig-progressions caption | "the back as the **outlet**" | Never defined. Is it the same as a checkdown? Say so. |
| L747 | "82% of NFL **dropbacks**" | "Dropback" (noun) is never defined. Does it include play-action and designed rollouts, and plays that end in sacks or scrambles? One parenthetical. |
| L819 | "a rhythm throw comes out on the last step of the drop, with **no hitch**" | Ambiguous: the chapter has two "hitches" (route and step, L646). Write "no hitch step". |
| L717 legend, drop chart | "hitch / **set**" | "Set" is never defined. |
| L815, L1297 | "**jammed** at the line", "Craig was jammed in traffic" | Not defined. "Press" gets a gloss (nose to nose), but "jam" doesn't. (The Craig usage means something else: blocked by bodies.) |
| L1097 | "bail into the three deep zones" | "Bail" is owned by 06-01, used here without a gloss. "Drop" would do. |
| L1512, Answer 3 | "if the defense **rolls its coverage** toward the trips side" | Undefined jargon in an answer. Readers met rotation nowhere yet (06-06 is far ahead). |
| L1512, Answer 3 | "**backside** answer" | Owned by 03-01 (playside/backside), so it's fair, but a link would help. |
| L545 | "a **pump fake**" | Obvious to most, but one clause costs nothing. |
| L1364, L1389 | "Next Gen Stats" | Owned by 13-05. Used as if known; add "(the NFL's player-tracking stats)". |
| L1130 | "four in Cover 3, **five in Cover 2**" | Cover 2 so far is only a name (02-05 lists it). The arithmetic (11 − 4 rushers − 2 deep = 5) is the whole point, so show it. |
| L1084 | "a cornerback who plays the flats in Cover 2" | First real use of Cover 2. The gloss only arrives in the PtP 2 caption (L1439). Gloss here. |

Diagram legend: "Reading the diagrams" (L270–279) says "a dotted line is an optional path", but
the chapter also uses dotted lines for the QB's footsteps (PtP 1 caption, L1397) and for defenders'
leans (horizontal stretch, L1121). It also says "dashed orange arrows are defenders' drops into
zones", but in the man panel of fig-option-route and in fig-timing-route the defenders' paths are
**solid** orange, and nothing explains the difference.

## 2. Leaps: a missing or assumed "why"

1. **"That is the whole budget: roughly two and a half seconds" (L287–288)** reads as "the line
   holds for 2.5 s". The drop chart then times deep routes to break at 2.6 s, and the real median
   for deep throws is 3.0 s. So how does any deep throw happen? The median *time to throw* is not
   the time the line can hold. Say so in one sentence, and point to Pass Protection for how long
   protection typically lasts.
2. **Route pairs (L449–453):** "if the cornerback stays deep, the comeback is open; if he jumps the
   comeback, the go is." A receiver runs one route per play, decided before the snap. How does a
   pair "answer a defender's choice"? Over a game? Through a double move? Through two receivers?
   The pair logic is asserted, not explained. "The curl and the corner make the same pair inside a
   single stem" is even more opaque, because they break opposite ways at nearly the same depth.
3. **Timing route vs the chapter's own zone rule.** L615 says zone defenders "are watching the
   quarterback rather than the receiver", and L1072 says they "break on the ball when it's thrown".
   The timing-route CB is in a zone (deep third), yet "can only drive on the ball once Z breaks"
   (L765, L809), half a second *after* the throw. Why doesn't he break on the QB's release at
   1.75 s? The reader needs the reason: a deep-third corner must respect the go, keys the receiver,
   and his eyes are on Z rather than the QB. Otherwise the figure seems to contradict the text.
4. **Success rate vs EPA (L1231–1233):** "a completion that gains four yards on first-and-10 is a
   step backward in EPA terms." 01-02 taught that 40% of the yards to go on first down (4 of 10) is a
   *success*. The reader now holds two rules that disagree and gets no reconciliation. Also, the
   chart shows behind-the-line completions average about **6** total yards (−3 air + 9 YAC), not 4.
   Use the chart's number and add one sentence on why EPA and success can disagree on a 4–5-yard gain.
5. **Horizontal stretch text vs figure (L1134–1135 vs L1123–1124):** the text says "If he leans
   toward Y, the back is open; **if he stays home, Y is**." The figure tags say "M leans to R: throw
   to Y". Staying home and leaning to R are not the same. Make the text match the figure.
6. **Half-field reads (L929–930):** "the quarterback can decide before the snap which side gives the
   best matchup". How? What does he look at? One example would do, such as a one-on-one on the
   single-receiver side, or a light side.
7. **"Offenses want to know whether the coverage is man or zone before they choose a read" (L1076).**
   How do they know? Since 02-05 taught one-high/two-high and some pre-snap cues, a one-line callback
   ("the shell and the cornerbacks' alignment give hints; 06-0x / 08-01 build this") would close it.
8. **"The deep out is the hardest throw in the tree, because the ball has to travel the full width"
   (L428).** That's only true from the far hash to the wide side. The ball's hash position (01-01,
   field/boundary side) changes this a lot. Say "to the wide side of the field".
9. **Fig-progressions caption (L875):** "the routes on the left (faded) are only there to occupy
   defenders, **so he can throw from a short drop**". That's a non sequitur: fading routes doesn't
   cause a short drop. The reason is that a half-field read is quick.
10. **"Nearly every play mixes them" (L857)**, meaning progression and defender reads. This is never
    shown. One sentence on how they mix (e.g. "his first read is a defender read on the flat
    defender; if that's taken away he moves to the backside") would make it concrete.
11. **PtP 2 situation:** it's third-and-8 and X runs a 5-yard hitch, while the Madden box (L308) and
    the misconception box (L487) both say routes run past the line to gain. A sharp reader asks why
    the hitch is short of the sticks. Either change the down to 2nd-and-8 or use it in the answer
    ("the hitch wouldn't convert anyway").

## 3. Diagrams: hard to decode, or captions that don't say what to notice

- **The QB is hidden under the ball marker** in fig-timing-route panels 1–2, both high-low rows at
  +0.7 s (and the +1.3/+1.7 panels), and PtP 2. The reader is told to watch the drop and the
  release but can't find "Q". Offset the ball or draw it smaller/behind.
- **Fig-route-tree:** the 0 (hitch) and 4 (curl) arrows lie almost on the shared stem; at print
  size you can't see that they turn back. The cheat-sheet uses "→" two ways: "10-12 →" (keeps
  climbing, per the caption) and "15 → 12" for the comeback (breaks at 15, comes back to 12), which
  the caption doesn't explain.
- **Fig-option-route:** the man panel has solid orange paths with no legend entry. The $ path
  crosses Y's route, so the panel is busy. In the zone panel, Y's "sit and turn to face the QB"
  shows only as a straight arrow; the turn isn't visible.
- **Fig-drop-timing:** the quick row shows a "hitch / set" segment before the ball comes out, while
  the text says the ball leaves "as his third step lands" (L643) and a rhythm throw has no hitch
  (L819). The left panel's y-ticks (3/6/9 yd) don't line up with the depths the text uses
  (5/7/9). Tick at the drop depths instead.
- **Fig-progressions:** the panels are only 2.75 in tall, so the receiver letters are unreadable in
  print. With no defenders drawn, "both reading the same cornerback" can't be seen. The "deeper
  drop" for full-field (4.0 vs 2.5) is barely visible. Either enlarge the figure or drop the
  claims the reader can't check.
- **Fig-high-low strip:** the "low" tag sits about 4 yards *behind* the line of scrimmage, not on
  the flat route. Put it beside Y's route at about 2–3 yards.
- **Fig-horizontal-stretch:** the dotted "lean" arrows from M are tiny, and the text mismatch is
  covered in §2.5. Otherwise the best diagram in the chapter: you can count four defenders and five
  receivers.
- **PtP 1:** route A (hitch) is a 1-yard tick, nearly invisible. The QB marker stays at the line
  while the dotted drop is drawn behind it, which is fine but could be stated.
- **PtP 2:** the X and CB markers overlap.
- **PtP 3:** the question asks "which defender is in conflict" but the defense is omitted and no
  coverage is stated. I had to assume Cover 3, which the answer does too. Say "assume Cover 3" in
  the prompt or caption.
- **Fig-depth-value:** good. But the text claims "carry the highest interception rate" (L1237),
  and the chart doesn't show interceptions. Either show it or source it.

## 4. Drag and repetition

- **Length: about 9,900 words of prose against a 5,000-word target.** That's the main drag. Cut
  candidates:
  - "Who numbered the routes" (L467–483): three coaching tenures with year ranges, plus the
    numbering caveats, which the misconception box half-repeats.
  - "Brady/Mahomes" film room (L1344–1366): seven percentages in one paragraph plus the Super Bowl
    LV aside.
  - "The clock in real games" (L823–835): it previews the reads chart, which then makes the same
    point again (L977–983).
  - "Two more names are worth having now" (drag/crosser, L548–553): deferred concepts named early.
- **"By the time he looks open it's too late" is said four times:** in the Madden box (L310–312),
  the "Why it exists" box (L737–740), timing routes (L813–816), and the anticipation-throw gloss
  (L820). Keep two.
- **"Make a defender choose, throw where he didn't go"** is restated in the tree-pairs paragraph,
  the conflict-defender intro, the high-low section, the horizontal stretch and its Why-it-exists
  box. It reinforces, but the conflict-defender paragraph (L987–998) could lose a sentence.
- **"Reading the diagrams" (L270–279)** is a 10-line paragraph before any content. The reader of
  01-04 already knows most of it. Trim it to what's new (route colours, the ruler, \$) and link the
  rest.

## 5. Can I do the "You'll be able to…" items?

| Objective | Verdict |
|---|---|
| Name every route on a replay, with number | **On a diagram, yes** (PtP 3 went perfectly). **On a replay, not yet.** I've never seen one route on real footage or an end-zone/broadcast angle, and the tree is drawn for an outside receiver while slot routes "may be numbered separately". |
| Count a drop and say depth/timing | **In principle.** But I don't know how to count from the shotgun: does catching the snap count as a step? Is the 1-step "a catch, a step and a throw"? I also don't know what a 5-step drop looks like on the standard broadcast angle (behind the QB, high). One sentence on what to watch (his back foot, the plant, the forward hitch step) would help. |
| Progression vs defender read; half vs full field | **Can define, can't spot.** The Watch-for-it test ("if he looks one way and throws the other, he moved through his progression") would also fire on a defender read where he looks at the flat defender. How do I tell them apart on TV? |
| Find the conflict defender in a stretch | **Yes.** The high-low and horizontal-stretch figures plus PtP 2 and 3 made this land. |
| Read air yards, YAC, aDOT | **Yes for definitions and the chart.** But the Watch-for-it box-score tip (L1387–1388), "a receiver with lots of yards on few catches has a high aDOT", is wrong by the chapter's own logic: high yards per catch can come from YAC, and an RB catching screens could have huge yards/catch and an aDOT near 0. Box scores don't print aDOT. Rewrite it ("lots of yards per catch *could* be deep targets or YAC; Next Gen / PFR advanced stats separate the two"). |

**Predict-the-play drills (attempted before opening answers):**

1. **Count the steps:** I answered **B, out at 12, ball out about 1.8–1.9 s**. Correct. But the
   off-corner cue pulled me toward A: L423–424 taught "when a cornerback lines up 7 or 8 yards off…
   a 5-yard hitch is open almost by definition", and the drill puts the CB 8 off. The answer does
   address it, but it should name the tension head-on: "the off corner *invites* the hitch, but a
   five-step drop is too slow for it, so the hitch would be a different call (three steps)." As
   built, the drill tests recall of the pairing table more than reasoning.
2. **The cornerback who stopped:** I answered the **corner route to H, now, over the CB and before
   the safety**. Correct. A good drill. The QB hidden under the ball made me hunt for him.
3. **Name the routes:** I answered **Z go (9), H out (5), Y flat (1), X slant (2)**, with the
   conflict defender being the short-outside defender, high-low on out/flat. Correct, but only after
   assuming Cover 3 myself. I was unsure whether Y's route, which climbs to about 4.5 yards near the
   sideline, is a "flat" (tree table says 0–3) or a quick out. "Rolls its coverage" in the answer
   was unknown to me.

## 6. Knowledge gaps: what I still wonder

- How long does a line actually hold? Is there a "sack clock" number (median time to sack,
  pressure)? The chapter says 2.5 s is the "budget", but that's time to throw.
- Where does the ball sit (hash), and how does that change which side the QB attacks and how hard
  the outs and comebacks are? (Field vs boundary was taught in 01-01 but isn't used here.)
- How does the play call tell each receiver his route? The chapter says a three-digit call exists
  (L474) but never shows one, e.g. "a 2-jet-**596**: X runs a 5, Y a 9, Z a 6". One example would
  make the digit system click now instead of four chapters later.
- When a timing route is broken (receiver jammed), what *exactly* happens? Does the QB move to
  read 2 on his hitch step? This is where progressions and timing meet, and it's left implicit.
- What do receivers do against man coverage to get open? Release and stem are deferred to 04-03,
  but separation is "the moment that matters", and nothing says how big a typical NFL window is
  (yards, or tenths of a second).
- Why do outside receivers' routes and slot receivers' routes differ? (The text says "inside
  receivers have routes of their own" but not why: space, leverage, who covers them.)
- Back-shoulder throws and fades come up constantly on broadcasts. The fade gets one clause; the
  back-shoulder throw isn't mentioned.
- The ball's flight time: the chart assumes a throw "a beat before" the break, but how long is the
  ball in the air on a 12-yard out vs a 40-yard go? (The code uses 18–22 yd/s. One sentence would
  make the timing arithmetic complete.)
- Interception risk by depth: the text asserts it, and I'd like the number.

## Priority fixes (for the author)

1. Fix the horizontal-stretch text/figure contradiction (L1134–1135).
2. Reconcile the "4-yard gain on 1st-and-10 is a step backward" line with success rate, and use the
   chart's ~6-yard figure (L1231–1233).
3. Separate "median time to throw" from "how long the line holds" (L287–288).
4. Explain why the deep-third CB in the timing route doesn't break on the throw (L806–811).
5. Un-hide the QB from the ball marker in the strips and PtP 2. Move the "low" tag onto the flat.
6. Gloss deep third, curl-flat, hook defender, EPA and scramble drill at first use (captions L567,
   L765, fig-reads).
7. Fix the box-score aDOT tip (L1387–1388), state the coverage in PtP 3, and gloss "rolls its
   coverage".
8. Cut toward the target length: the history tenures, the "clock in real games" preview, the
   repeated "too late when he looks open", and the Brady/Mahomes stat pile.

---

## Revision (2026-10-06): finding -> action

Covers this beginner review and `04-01-coach.md`. Fact-check claims were left as verified; new
numbers are computed inline from nflverse and footnoted (`[^first10]`), and the one new historical
detail (the "896" digit order) is sourced in `[^coryell]`. Rebuilt with
`build_pdfs.py 04-01-passing-fundamentals --html` (OK, no errors, 22 pages); every figure page was
re-rasterized and checked by eye.

### Beginner review

| Finding | Action |
|---|---|
| §1 hook defender / curl-flat first used in a caption | fig-option-route caption now glosses them in plain words ("the Mike, who guards the short middle", "the nickel, who guards the short area outside"). |
| §1 "off cornerback playing a deep third" | Timing caption says "lines up 7 to 8 yards off Z ... guard the deepest third of the field on his side (a deep third)"; the high-low intro links [deep third] (06-01). |
| §1 EPA first used in the reads chart | One-line EPA gloss + link moved to the paragraph before fig-reads. |
| §1 scramble drill in the reads chart | Caption glosses it ("made after the play broke down and the quarterback ran around"). |
| §1 "outlet" never defined | Progression paragraph: "the checkdown ... to a back or tight end (the *outlet*)"; caption uses "outlet" for the flat release. |
| §1 "dropback" undefined | Defined in parentheses at the start of the drop section (includes play-action, sacks, scrambles). |
| §1 "no hitch" ambiguous | Now "no hitch step" everywhere (text and drop chart). |
| §1 "set" in the drop-chart legend | Legend now "hitch step"; caption explains it. |
| §1 "jammed" undefined | Defined in the release bullet; the Craig usage became "held up in traffic". |
| §1 "bail" | Replaced with "drop". |
| §1 "rolls its coverage" / backside | Answer 3 now says "shifts extra defenders toward the three receivers"; "backside" links to 03-01. |
| §1 pump fake | One-clause gloss. |
| §1 Next Gen Stats | Linked to 13-05 with "(the NFL's player-tracking numbers)". |
| §1 Cover 2 arithmetic and first use | Horizontal-stretch text shows 11 − 4 − 3 = 4 and 11 − 4 − 2 = 5; Cover 2 is glossed where smash is first mentioned. |
| Legend: dotted/dashed/solid lines | "Reading the diagrams" rewritten (and trimmed to what is new): dashed orange = zone drop, solid orange = running with a receiver or driving on the ball, dotted with arrowhead = a choice, thin dotted behind the QB = footsteps, grey = on the play but not the point. |
| §2.1 2.5 s "budget" vs line holding | New sentences: the median is how long QBs *choose* to hold the ball, not how long the line holds; deep throws routinely leave after 3 s; link to Pass Protection. |
| §2.2 route pairs unexplained | Pairs paragraph rewritten: one route per play, but routes are built to look alike (slant/sluggo, hitch/hitch-and-go, post/post-corner); pairs work across a game, inside a double move, and across two receivers. The curl/corner line is gone. |
| §2.3 why the deep-third CB doesn't break on the throw | New paragraph: deep defenders key the receiver who can beat them deep, not the QB; underneath defenders watch the QB. Option-route text now says "underneath defenders". |
| §2.4 4-yard gain vs success rate; chart says ~6 yards | Rewritten with computed numbers: a completed behind-the-line throw gains ~6 yards; on 1st-and-10 a 4-yard gain averages −0.16 EPA and 5 yards breaks even, which is stricter than 01-02's yardage rule; the incompletions finish the job. Footnote `[^first10]`. |
| §2.5 horizontal-stretch text vs figure | Text now "if he leans toward the back, Y is"; figure geometry fixed (coach A2). |
| §2.6 how the half-field side is chosen pre-snap | Added: a receiver alone against an off cornerback, or the side with fewer defenders than receivers. |
| §2.7 how offenses learn man vs zone | Callback to 02-05 (the shell) plus cornerback alignment/eyes, with links to 06-01 and 08-01. |
| §2.8 deep out "hardest throw" | Replaced by a field/boundary paragraph: deep out from the far hash to the wide side (~30 yards, checked geometrically) is the arm test; outs and comebacks usually go to the boundary. |
| §2.9 caption non sequitur | Caption rewritten: short drop because a half-field read is quick; the faded routes just occupy defenders. |
| §2.10 "nearly every play mixes them" unshown | New paragraph with a concrete mix (defender read on one side, then progression), plus the hot/sight-adjust check that comes first. |
| §2.11 PtP 2 third-and-8 with a 5-yard hitch | Changed to second-and-8; the answer notes a 5-yard hitch is a fine result on 2nd-and-8. |
| §3 QB hidden under the ball | The chapter's snapshot helper now draws a held ball beside the QB (on the emptier side) until it is thrown. Fixes the timing strip, both high-low rows and PtP 2. |
| §3 route tree: hitch/curl invisible; "→" used two ways | Hitch and curl turn back visibly (1.5–2.3 yd); cheat sheet now says "15, back to 12", "10-12 / out, climbs", "10-14 / in, climbs"; caption updated. |
| §3 option route: solid orange paths, busy man panel, turn invisible | Solid vs dashed explained in the legend and caption; nickel now trails on the inside hip (coach A6); Y breaks at 6 yd; zone-panel Y hooks back visibly and the tag says "turns to face Q"; window raised so the CB/Z arrows aren't cut. |
| §3 drop chart: quick-row hitch, y-ticks | Quick row has no hitch segment and the ball leaves as the drop ends; left panel ticks at 5/7/9 yd. |
| §3 progressions too small, claims uncheckable | Taller figure, narrower field slice, labelled players enlarged ~35%; the ringed cornerback is drawn in the half-field panel so "read off the cornerback" is visible; drop depth tagged ("3-step drop" / "5-step drop"). |
| §3 high-low "low" tag behind the LOS | Moved beside the end of the flat route. |
| §3 horizontal stretch lean arrows tiny | Thicker dotted leans with larger heads, re-aimed (coach A2). |
| §3 PtP 1 hitch nearly invisible; QB marker vs drop | Hitch drawn to 6 yd and back 1.4 yd; caption says the marker is where he starts and the dotted line is the drop. |
| §3 PtP 2 X and CB overlap | CB now outside X with clear space (coach A1). |
| §3 PtP 3 coverage not stated; Y's route ambiguous | Caption and question say "assume Cover 3"; Y's flat now finishes at ~2 yd; H's out breaks at 12. |
| §3 depth chart: INT claim not shown | Interception rate printed inside each completion bar; text quotes 20+ yd INT rate vs shorter (computed inline). |
| §4 length (~9,900 words) | Cut: "The clock in real games" subsection (two sentences kept under the drop chart), the drag/crosser paragraph, the Coryell tenures, the Super Bowl LV aside and `[^sb55]`, three of the Brady/Mahomes percentages, two of the four "too late when he looks open" lines, a conflict-defender sentence, the long diagram legend, and line edits throughout (about 1,400 words of old prose). The review and coach asked for about a dozen additions (budget vs line, field/boundary, dialects, digit-call example, break types, hot routes, MOFO/MOFC, CB eyes, EPA reconciliation, read mixing, TV tells), which added roughly 1,000. Net prose is ~8,550 (raw count incl. link tokens) against ~8,930 before. **Partly declined:** reaching 5,000 would mean dropping requested nuance or one of the spec'd figures; the contract allows "whatever the concept needs", and every section now carries a why. |
| §4 "too late" said four times | Kept in the Madden box and the drop "Why it exists"; removed from the timing-route section and the anticipation gloss. |
| §4 conflict-defender paragraph | Merged and shortened. |
| §5 replay recognition | Watch-for-it now says which replay angle to use; the field/boundary paragraph and splits bullet say what to expect where. |
| §5 counting from the shotgun / on TV | "Catching the snap is not a step"; what to watch on the high broadcast angle (steps back, plant, hop forward). |
| §5 progression vs defender read on TV | New "Then his head" bullet: head stays on one side vs snaps across receivers with feet resetting. |
| §5 box-score aDOT tip wrong | Rewritten: high yards per catch could be depth or YAC; PFR / Next Gen pages list aDOT and YAC separately. |
| PtP 1 off-corner tension | Answer now names it: the cushion invites the hitch, but a five-step drop is too slow for it; the hitch would be a three-step call. |
| §6 gaps: line hold, hash, digit call, broken timing, slot vs outside, back-shoulder, ball flight, INT number | Addressed: line hold (budget paragraph), hash (field/boundary paragraph), "896" example (X post, Y go, Z dig; sourced), broken timing (hitch step = eyes to read 2), slot vs outside (off-tree intro), back-shoulder throw (go bullet, link 10-03), ball flight (~29 yd at 22 yd/s, >1 s, stated as the simulation's speed), INT rate (inline). **Not added:** a typical NFL separation window in yards (no source checked; separation is owned by 13-05). |

### Coach review

| Finding | Action |
|---|---|
| A1 PtP 2 corner lands on the safety; CB leverage wrong | H's corner now `r.path((11.5, 0), (20, 11))`: breaks at 10, lands ~18 deep at w ≈ −20, far from the FS. LCB starts at (5.0, −17.5) and squats to (3.4, −18.6), outside X. Caption: "just outside X and in front of the hitch". Answer depth updated to ~18 yards. |
| A2 horizontal stretch: Mike not stretched | R now check-releases and sits at (5.5, −2.5), between W and M; leans re-aimed to (7.4, −1.0) and (7.4, 4.5); the "hash" comment dropped; R moved off Q. |
| A3 timing route timing | QB drop at 3.8 yd/s finishes ~1.45 s, hitch step to 1.85 s, `pass_to` at 1.85; Z (aligned on the numbers, w = 14) breaks at 12 yards at ~1.95 s; CB backs to 15.5 deep, drives only after the break and finishes at (14.2, 19.0), visibly a step behind and inside. Panels 0.9 / 1.85 / 2.45 / catch (catch time computed). Prose: "12 yards", "a tenth of a second later". Optional out-flat point added in one sentence. |
| A4 progressions order | Full field: 1 X post, 2 H dig, 3 Y curl, 4 R checkdown; Z's go is grey with no number. Half field: R released outside the tackle to the flat (~2 yd, w ≈ 11); caption says the smash pair is read high to low off the cornerback (corner 1, hitch 2). Larger panels, back at w = ±2.5. |
| A5 wheel not a wheel | Wheel turns up at w ≈ 19.5 (outside the numbers); Z moved to w = 15 and clears inside on a grey skinny post; text and caption say the wheel needs the sideline cleared. |
| A6 option man panel: defender undercuts | Nickel now trails on the inside hip (`[(5.6, 8.0), (6.4, 11.0)]`, delay 0.25). |
| A7 high-low "low" label | Moved next to the end of the flat route. |
| A8 route tree Z on the line | Relabelled X. |
| B1 landmarks, field vs boundary | New paragraph after the tree bullets (boundary outs/comebacks, wide-side deep out, 5–6 yd sideline rule, depths from the LOS, links to the numbers and reduced split in 02-02). |
| B2 hot routes / sight adjust | Slant bullet names the hot route; the Reads intro adds hot route and sight adjust as the check before any progression (links to 04-02). |
| B3 kinds of break | Added to "The break": speed vs sink-and-plant, and the 12-yard out breaking slightly back; cheat sheet says "~square". |
| B4 terminology dialects | Short paragraph after the history. **Declined:** the Coryell deep-to-short vs Walsh short-to-deep read-order note; it is a generalization I could not source quickly, and 04-08 owns system comparisons. |
| B5 Answer 1 dated seven-step claim | Now "today it is usually a later read off this drop or a shot off play-action". |
| B6 route pairs | Replaced with slant/sluggo, hitch/hitch-and-go, post/post-corner. |
| B7 slant "the quickest" | "One of the quickest". |
| B8 option-route third case and MOFO/MOFC | Both added in two sentences, MOFO/MOFC glossed and linked to 06-01. |
| B9 film rooms | Kept as verified. Brady/Mahomes trimmed for length (beginner §4); the SB LV aside was cut, so `[^sb55]` is gone. |

### Notes for the editor

- Helpers written inside the chapter (gridiron was not edited): the snapshot helper draws a held ball
  beside the QB; `faded_route()` draws grey "not the point" routes; the progressions figure enlarges
  labelled markers after drawing. `gridiron.animate` still draws the ball on top of the QB in the web
  videos; a `ball_offset_when_held` option in gridiron would fix both formats.
- The FTN `read_thrown` dictionary caveat from the fact-check still stands.
