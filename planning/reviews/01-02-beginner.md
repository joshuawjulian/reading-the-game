# 01-02 Downs, Distance, and Field Position: beginner-reader review

Reviewer role: casual NFL watcher who has never played. In curriculum order I had read only 01-01 (field markings,
hashes, field/boundary side, the five scores, the try, field-goal distances, possession, game clock and play clock,
kickoff and the 35-yard touchback). I had not read 01-03 (positions) or 01-04 (what a play is). Source:
`chapters/01-foundations/01-02-downs-distance-and-field-position.qmd` (line numbers below are qmd lines) and
`pdfs/01-02-downs-distance-and-field-position.pdf` (18 pages, rasterized at 60 dpi, every page read). Length:
about 9,100 words in the PDF including footnotes, against a spec target of about 4,000. The prose alone is
probably 6,000+.

Overall: this is a strong chapter. The series-of-downs strip, the third-down "price list", the pass-rate grid and
the field-position ladder all land, and the walk down the Super Bowl LIX drive is the best explanation of EPA I
have seen aimed at a fan. The problems are concentrated in four places: the EPA scorecard figure, one false
generalization about EPA, position vocabulary in the drills, and two numbers that disagree with 01-01.

---

## 0. The biggest problems

1. **The takeaway "a drive's EPA always adds up to the points it actually produced" is false for most drives**
   (l.1272, and l.968–971: "the total always matches what happened"). It is only true for a drive that ends in an
   offensive touchdown (or field goal). A drive that ends in a punt does not sum to 0. It sums to
   (−EP of the opponent's new situation) − (EP at the start), because the chapter's own rule (l.859–860) says that
   when the ball changes hands, "EP after" is the negative of the new offense's EP. A data-minded reader will check
   this on the very next drive and find it doesn't hold. Fix: "For a drive that ends in a score, the EPAs plus the
   starting EP add up to exactly the points scored. For a drive that ends in a punt or turnover, they add up to
   the (negative) value of the field position handed over."
2. **The EPA scorecard (Fig 8, l.877–936) doesn't show the thing it's teaching.** The spec asks for "EP before and
   after each play"; the figure shows only EPA. The definition is "EP after − EP before" (l.851–853), but I can't
   check that on any row, because the EP numbers appear in the text for snap 1 (+1.37) and snap 8 only. Also, in
   the "Where the ball went" column the 2- and 3-yard runs are just dots at 60 dpi, and so is the −1. The caption
   says "orange = backward", but I couldn't find the one orange arrow. Fix: add an "EP before → after" column
   (e.g. "+1.37 → +0.93"), and drop or widen the arrow column (the yard line in the row label already says where
   the ball was).
3. **The drill diagrams use position labels I have never been taught.** Fig 10 (l.1113–1122) and Fig 11
   (l.1150–1166) print Q, T, F, Y, U, X, Z, H, R on offense and E, T, W, M, S, SS, FS, C and **$** on defense. There
   is no key and no legend (circles = offense, squares = defense isn't stated either). "T" appears on both teams
   (tailback and defensive tackle). In Fig 10, "S" sits right next to "SS", and I assumed both were safeties
   (one is presumably the Sam linebacker). In Fig 11, "$" means nothing to me. The captions also use "tight ends",
   "fullback", "quarterback under center", "linebackers", "shotgun", "five defensive backs", "cornerbacks", none
   of which 01-01 taught (01-03 owns them). The drills are answerable from down and distance alone, but the
   pictures make me feel I'm missing something. Fix: one sentence under Fig 10 ("Blue circles are the offense,
   orange squares the defense; the letters are positions, decoded in [The Twenty-Two](01-03-the-twenty-two.qmd).
   You don't need them for this drill.") and a gloss of "$" in Fig 11.
4. **Two numbers contradict 01-01.**
   - Field-goal length: 01-02 says "the kicker stands about seven yards behind the line… (Add 17 to the yard line to
     get a field goal's length)" (l.767–769), and Predict 3 uses 38 + 17 = 55. 01-01 says "add about 18 yards"
     (01-01 l.536, l.670) and draws a ball at the opponent's 35 as a 53-yard kick. I learned "18" a chapter ago,
     so now I don't know which one is right. Pick one convention for the whole book (17 is the common rule of
     thumb).
   - Drives per game: 01-02 says "about 10.1 drives per game" per team (l.1006); 01-01 says possessions are
     "about eleven per team" (01-01 l.797, l.1367). The chapter says a drive is "the same thing as the possession
     from the last chapter" (l.1003–1004), so the numbers should match, or the difference should be explained
     (probably different counting rules: kneel-downs, end-of-half snaps).
5. **Learning objective 5 asks for a number the chapter never gives.** "Say roughly what a first down at your own
   25 … is worth" (l.165–166). The bullets give own 5, own 35, midfield, opp 20 and the 1 (l.797–804), and the
   takeaways repeat those (l.1269–1270). The own 25 is the worked example of how EP is built (l.784–791), yet its
   value is never stated. I had to read it off Fig 7 (about +1.0?). Either add the own 25 to the bullets or change
   the objective to the own 35.

---

## 1. Terms used before they are explained (or never explained)

| Where | Term | Problem |
|---|---|---|
| l.147–148 (hook) | "huddle", "sending a sixth defensive back" | "Defensive back" is undefined, and I don't know a defense normally has four or five, so "sixth" carries no meaning. The hook never pays this off. Gloss it ("a sixth pass defender in place of a bigger run-stopper") or cut it. |
| l.149 | crowd on its feet "because the home team is on defense" | Why does that matter? (Noise disrupts the offense's communication.) One clause. |
| l.377 (Fig 3 caption), l.419 (Fig 4 caption), l.689 | "sacks and scrambles count as passes", "dropbacks" | "Scramble" is never defined. "Dropback" appears in the sack rate ("6.5% of dropbacks") with no gloss. |
| l.419 (Fig 4 caption) | "win probability 20-80%" | Win probability is never defined in 01-01 or here. It also drives Predict-3's closing and footnote 7 (l.1316). Needs a half-sentence gloss ("the chance, from the score and clock, that the offense's team wins") plus a link to 13-03. |
| l.455 | "extra pass rushers or extra defensive backs" | Pass rusher is undefined, and so is defensive back (see above). |
| l.369 | "drops more players into coverage" | "Coverage" is undefined. It's guessable but should be glossed. |
| l.578–579 | "catches the long snap", "signals a fair catch" | Both are undefined. "Fair catch" especially: what is it, and why would anyone choose it? |
| l.764 | "a holding penalty" | Holding is undefined. A gloss is enough ("grabbing a defender"). |
| l.963 | "the Eagles' famous quarterback sneak (the tush push)" | "Quarterback sneak" is undefined. Also used in Answer 1 (l.1135). |
| l.1065 | "a slant", "linebacker" | Both undefined (film room). |
| l.1075 | "cornerback" | Undefined. |
| l.1116, l.1153 | tight end, fullback, under center, shotgun, linebackers, safety, cornerbacks, five defensive backs | See §0.3. |
| l.1189 | "a **draw**, a run disguised as a pass" | Bolded like a defined term, but there is no glossary link, and the curriculum doesn't give this chapter ownership. It needs a link to the owning chapter (03-05?). |
| Fig 2 (l.330) | "3rd 6:42" next to "3rd & 8" | Two "3rd"s side by side, one the quarter and one the down. The caption doesn't point this out. A beginner can easily misread it, and it's a nice teaching moment: "the first '3rd' is the quarter". |

Terms the chapter owns are all defined and bolded at first use. **Exception:** "distance" is bolded (l.183) but
isn't a glossary term. That's fine, but the bold suggests one.

## 2. Leaps (a missing or assumed "why")

- **Fourth-down pricing is promised and never done.** Answer 3 opens with "Price the three options with this
  chapter's tools" (l.1233–1234), then gives inputs (58% conversion, +3.5 EP if made, the opponent at its own 38
  if missed, 70% on 55-yarders) but never multiplies them out. I tried: go ≈ 0.58 × 3.5 − 0.42 × (EP of a
  first-and-10 at the opponent's own 38, which the chapter doesn't give, maybe +1.8) ≈ +1.3. Kick ≈ 0.70 × 3 −
  0.30 × (opponent at its own 45, about +2.2?) ≈ +1.4. Punt ≈ −(opponent at its own ~10, about +0.4?) ≈ −0.4. On
  my rough numbers, **kick and go come out about even**, which isn't what the answer implies. Either show the
  arithmetic with real EP values (strongly preferred: it's the payoff of the whole chapter), or say plainly
  "the full arithmetic is in 13-03". As written, it's a promise left half-kept. (Also, after a made field goal
  the opponent gets a kickoff, which is worth something to them; the "3" isn't really 3.)
- **"On first-and-10, a run needs roughly four or five yards just to break even"** (l.944). This is a key fact
  with no evidence (no chart, no source). A one-line breakeven table for 1st/2nd/3rd down, like the one
  computed for Predict 2, would earn it.
- **No scale for EPA.** Objective 6 asks what "a +2.0 or a −0.5 means". The chapter shows individual plays but
  never tells me what's typical: most plays fall between about −1 and +1, a turnover is about −3 to −5, and a
  good offense averages about +0.1 per play with a success rate in the mid-40s. Every later chart ("EPA per
  play", 03-02 etc.) needs this anchor. Two sentences after l.866.
- **Success rate definition vs. what I'll hear on TV.** The chapter defines success as EPA > 0. Broadcasters and
  Football Outsiders-style sites often use the yardage version (40% / 60% / 100% of the distance), which 13-02
  covers (13-02 l.708). One sentence plus a forward link would stop me from being confused when I hear the other
  definition.
- **Two different touchbacks.** Fig 7 marks "own 35 (touchback)" and l.799 explains the 35 is the kickoff
  touchback. Then Predict 3 says a punt that rolls into the end zone is "a touchback at the 20" (l.1198,
  l.1221, l.1245). Nothing tells me punts and kickoffs have different touchback spots. One clause.
- **"Giving the ball up at the opponent's 30 instead of your own 30 is worth several points"** (l.647–648). I read
  this three times. Does it mean the opponent starting at *its* own 30 versus at *your* 30? The wording makes it
  sound like the punt moves the spot from the opponent's 30 to your 30. Rewrite: "Handing the opponent the ball
  at its own 30 instead of at your 30 is worth several points."
- **"A field goal there captures only some of it"** (l.1022–1023). From first-and-10 at the opponent's 20 (EP
  +4.5), a field goal is worth 3, i.e. a *loss* of 1.5 in EPA terms. "Captures only some of it" suggests the
  field goal still adds value beyond the red-zone first down. Say what EPA says: "settling for 3 there is a −1.5
  outcome."
- **Why the third-down conversion rate is still about 10% at 15+** and how the yards beyond 15 are bucketed
  (l.379 clips at 15). That's fine, but the label "15+" deserves "(all longer distances)".
- **The penalty snap** (l.952–956): "automatic first down" is new. Why does a defensive penalty give one? One
  clause (some defensive fouls carry an automatic first down by rule; 09-04 has the list).
- **Next score "before halftime"** (l.788). Earlier in the same sentence it's "the next score in the game". It
  should say "in the half" both times, or explain why halftime resets.

## 3. Diagrams

- **Fig 1, series of downs (p.2):** decoded easily; the best figure in the chapter. The "line of scrimmage" and
  "line to gain" labels are only in panel 1, which is right. Small point: the field numbers "40/30" are drawn
  big and grey, and for a moment I took "30" for a label of the line to gain (the 35). Fine once I read the
  caption.
- **Fig 2, score bug:** clear. See the "3rd/3rd" note in §1.
- **Fig 3, third-down rate:** clear, and the caption says what to notice.
- **Fig 4, pass grid:** clear. The buckets don't match the text, though: the text defines long as "7 yards or
  more" (l.368), but the grid splits 7–10 "long" from 11+ "very long". Either mention "very long" in the bucket
  list or merge.
- **Fig 5, the spot (p.6):** I understood it from the caption. The "driven back two yards" segment is a tiny kink
  and easy to miss. The run line leaves the window past the "sideline" text with an arrow, so it looks as if the
  runner crossed the sideline label. OK.
- **Fig 6, fourth-down choices (p.7):** readable, but the row label "own 40 to opp 46" is a strange boundary
  next to "opp 45–36" (why 46?). The text describes the go-for-it band as "from around your own 40 to the
  opponent's 36", which spans two rows with very different numbers (59% vs 91%). Say which row the claim is about.
- **Fig 7, field map (p.9):** excellent. The caption tells me what to notice.
- **Fig 8, EPA scorecard (p.11):** see §0.2. The x-axis labels "PHI 30, 50, KC 30, 10, goal" switch from "KC 30" to
  a bare "10". The caption says "Four short runs all gained ground or nearly so", while the callout (l.977) says
  "three short runs all gained ground". Same plays, two counts (the fourth lost a yard). Make them agree.
- **Fig 9, film room (p.13):** decodable, but it shows only two ball spots and one X. I learned nothing from it
  that the text didn't say. Consider adding the down-by-down spots of the XLVII series (7 → 5 → 5 → 5) to show
  "four tries, no touchdown", which is the point being made.
- **Fig 10 (p.14), Fig 11 (p.15):** see §0.3. In Fig 11 the field numbers "30" (top left) and "20" (left and
  right at the line of scrimmage) are partly covered by the C, X and Z markers, so the labels collide. I also
  couldn't tell from the picture that the safeties were beyond the line to gain until I read the caption. Worth
  saying "both safeties are deeper than the line to gain".
- **Fig 12 (p.16):** good. The three options are clear. The posts are drawn as a black bar at the very right
  edge of the window. That's OK, but "END ZONE" isn't labelled, so I wasn't sure what the grey band on the right
  was.

## 4. Drag and repetition

- **Length:** more than twice the spec. The places to cut are below.
- **The drives section repeats 01-01.** The share of drives ending in a punt, touchdown or field goal ("A third
  of all drives end in a punt; roughly four in ten end in points", l.1010–1011) is nearly word for word the
  01-01 census ("A third of possessions end in a punt", 01-01 l.797), and the red-zone 7-vs-3 point is
  re-stated with "the last chapter showed" (l.1019). Keep only the new part: the link between drive outcomes
  and the +1.4 EP at a typical start.
- **Predict 1 and Predict 3 have the same punchline.** Both answers end on "on fourth-and-1-to-3 between the
  opponent's 45 and 36, teams went for it 91% of the time" (l.1143–1145, l.1232–1233). Once I'd read Answer 1,
  Drill 3 was solved. Move Drill 3 elsewhere on the field (e.g., 4th-and-2 at your own 34, where the answer is
  genuinely contested), or make Drill 3 about the EP arithmetic (§2).
- **The history box** (l.297–317): the 1880/81 games and Camp are great. The gridiron-etymology tangent
  (l.308–311, plus footnote) and "by then a medical student" are trivia that slow it down.
- **The chain-clip parenthetical** (l.550–552) breaks the best sentence in that section. Move it to the footnote.
- **The "Why it exists: one currency" box** (l.835–843) largely restates the preceding two paragraphs. It could
  shrink to its last two sentences.
- **Fourth-down choice percentages** appear three times (l.589–590 overall, the chart, and the answers). They're
  fine once.

## 5. Can I do the "You'll be able to…" items? Drills attempted before opening answers

Objectives:

1. Four downs, line to gain, why teams punt: **yes**, clearly.
2. Read the graphic, bucket it, say what each bucket does: **yes**.
3. LOS, the spot, the chain crew now that cameras measure: **yes**. The Hawk-Eye paragraph is clear.
4. Ways the ball changes hands; why a sack hurts more than its yards: **yes**.
5. EP at own 25 / midfield / opp 20: **partly**. Midfield and opp 20 yes; the own 25 is never stated (§0.5).
6. What +2.0 or −0.5 means, and why a gain can be a loss: **mostly**. "A gain can be a loss" is nailed. "What
   +2.0 means" in plain words (e.g., "like moving a midfield first down to the opponent's 20") is never said, and
   there's no sense of scale (§2).

Drills (my answers before opening the callouts):

- **Predict 1 (3rd & 1, opp 45, heavy personnel):** I said "run, because short yardage is the one place running is
  normal, and if they miss they'll go for it on fourth because the chart shows ~91% go-for-it at opp 45–36."
  **Correct** on both. The play-action note in the answer was new to me but made sense. The picture's letters
  played no part (§0.3).
- **Predict 2 (2nd & 15, own 20, safeties deep):** "Pass" was easy (82% on the grid). "What is the defense happy
  to give up?" I could only guess from common sense ("they're far back, so they'll allow short stuff"). Nothing in
  the chapter teaches what deep safeties or off-coverage corners mean. **Half right.** The question tests 02-05/06
  material. Either rephrase it ("the defense is lined up very deep; what is it worried about?") or add a sentence
  about it in the drill prompt.
- **Predict 3 (4th & 2, opp 38):** "Go for it, from Fig 6 and the Predict 1 answer." **Correct**, but only by
  recall of a percentage, not by "pricing" the options as the answer claims I can (§2). When I tried to price
  them, kick and go looked roughly equal on my numbers.

## 6. Knowledge gaps: what I still wonder

- What is a *good* team EPA per play and success rate? (§2)
- How exactly are distances rounded on the graphic? "2nd & 6" when 5½ yards remain? Only "inches" is covered.
- Punt touchback (20) vs kickoff touchback (35): why are they different? (§2)
- What's a fair catch, and why would a returner choose it?
- After a missed field goal, why does the opponent get the ball at the spot of the kick? Stated in Answer 3
  (l.1241–1242) but never explained or linked.
- On a fumble that goes out of bounds, who gets it? (A pointer to 09-04 would do.)
- Does EP know the score or time? l.822–823 says "in its full form, a few more things such as the time left".
  Which things? Is it the same EP for a team down 20 in the fourth quarter? One sentence plus the 13-02 link.
- Why did the go-for-it rate double between 2016 and 2025 if the math was known since the 1970s/2000s? There's
  a line about analytics staffs, but the "why so slow" human story is missing. Maybe a sentence on coaches'
  fear of second-guessing.
- Is "success rate" on a broadcast the same as this one? (§2)
- If a drive's EPA total isn't the points (punt drives), what *is* it? (§0.1)

---

## Revision (2026-10-06)

The chapter was revised against this review and against `01-02-coach.md`. It renders cleanly
(`build_pdfs.py 01-02-downs-distance-and-field-position --html`: OK, 20 pages, no cell errors), and I
looked at every diagram page at 60 dpi, with 130–140 dpi zooms of Figs 5, 7, 8, 9 and 12. Every footnote
is referenced exactly once. New factual claims are sourced in footnotes, or computed inline from nflverse
with the seasons and filters stated.

### Beginner review: finding -> action

| Finding | Action |
|---|---|
| §0.1 "A drive's EPA always adds up to the points" is false for non-scoring drives | Rewrote the paragraph after the scorecard: the column adds up to the drive's final value minus its start, which is the points for a scoring drive and the negative of the handed-over field position for a punt or turnover. Takeaway 6 now says the same. |
| §0.2 Scorecard lacks EP before/after; arrow column unreadable | Replaced the "Where the ball went" column with an "EP before → after" column (e.g. "+1.37 → +0.94"), so EPA = after − before can be checked on every row. Rows have alternating shading. The ✓/✗ column moved clear of the +2.95 label. Snap 1's text now quotes both EP values. |
| §0.3 Position letters, shapes and "$" undecoded in drills | Added a lead-in under "Predict the play" (circles = offense, squares = defense, letters decoded in 01-03, not needed for the drills). Both captions name each letter they use, including "$ = slot cornerback". The tailback is relabelled "R" (it was "T", which clashed with the tackles), following 01-03's tag table. Yard numbers that sat under markers were removed. Fig 11's caption says the safeties sit at the line to gain. |
| §0.4 FG "add 17" vs 01-01's "add 18" | Checked nflverse: in 2016–2025, 90% of FG attempts are exactly LOS + 18 (holder about 8 yards back), and most of the rest are + 19. The chapter now says "add 18, as in the last chapter", with a footnote that notes 17 as the college / high-school rule. Fig 12 and Drill 3 are now a 56-yard kick from 8 yards back. (This corrects the fact-check row "holder 7 yards back so … + 17" with stronger evidence.) |
| §0.4 10.1 drives/game vs 01-01's "about eleven" | The old count dropped drives whose first row had no `posteam`. It now uses 01-01's method (one row per game/team/drive): 10.7 per team, stated as the "about eleven" of 01-01. Drive-outcome shares come from the same set. |
| §0.5 Objective asks for own-25 EP, never given | Added an own-25 bullet (+1.1). Fig 7 now marks the own 25 instead of the own 35, and the own-25 value is in the takeaways. |
| §1 hook: "sixth defensive back", crowd noise | Hook now says the defense swaps a big run-stopper for an extra pass defender, and that noise makes it hard for the offense to hear its signals. "Huddle" is glossed and linked to 01-04. |
| §1 scramble, dropback, win probability, pass rusher, defensive back, coverage | Glossed in place: scramble in the Fig 3 caption; dropback in the sack section; win probability in the Fig 4 caption (13-03 linked in the EP section); pass rusher and defensive back in item 2; "drops more players into coverage" reworded as "drops more players back to defend passes". |
| §1 long snap, fair catch, holding, QB sneak, slant, linebacker, cornerback | Long snapper linked to 01-03. Fair catch defined in one clause and linked to 09-01, with a source. Holding glossed and linked to 09-03. QB sneak glossed at snap 8, with the sneak link in Answer 1 going to 10-03. Slant glossed; linebacker and cornerback linked to 01-03. |
| §1 "draw" bolded without ownership | Unbolded, and linked to 03-03, which owns "draw play". |
| §1 "3rd 6:42" next to "3rd & 8" | The score bug now reads "Q3 6:42", and the caption warns that some networks write "3rd" for the quarter. A possession football was added (the coach asked for it too). |
| §1 "distance" bolded but not a glossary term | Now italic. |
| §2 Fourth-down pricing promised, not done | Drill 3 now asks the reader to price the options, and the answer does the arithmetic with real values: go ≈ 0.58 × 3.9 − 0.42 × 1.8 ≈ +1.5; kick ≈ 0.67 × 3 − 0.33 × 2.4 ≈ +1.2; punt ≈ −0.2 (the empirical average after punts from the opp 35–41). The answer honestly says the kick is close and that the bookkeeping ignores the kickoff after a score and the scoreboard, with a pointer to 13-03. This also fixes §4's "same punchline" problem: Drill 1 recalls the go rate, and Drill 3 explains it. |
| §2 "4–5 yards to break even" unsupported | New table (tbl-breakeven, computed): 1st & 10 → 5 yards, 2nd & 10 → 7, 2nd & 5 → 4, 3rd & 5 → 5 (only the line to gain counts). The text now says "about 5". |
| §2 No scale for EPA | New "What's a big number?" paragraph, all computed for 2025: two plays in three fall between −1 and +1; an interception costs about 4.5 and a lost fumble about 4.9; +2.0 is about midfield → opp 20; the league averaged +0.01 per play with a 44% success rate; best team about +0.16, worst about −0.22. |
| §2 Success-rate definition vs TV | Added one sentence on the 40/60/100 yardage version, linked to 13-02 (which teaches it). |
| §2 Two touchbacks (35 vs 20) | The punt bullet now says a punt touchback is at the 20 and a kickoff touchback at the 35 since 2025, set by separate rules. |
| §2 "Giving the ball up at the opponent's 30…" confusing | Now "Handing the opponent the ball at *its own* 30 instead of at *your* 30 is worth about 2.4 points" (computed from EP). |
| §2 "A field goal captures only some of it" | Now says settling for 3 from first-and-10 at the opp 20 scores about −1.5, a loss. |
| §2 "15+" label | Fig 3 caption: "'15+' is every distance of 15 yards or more". |
| §2 "Automatic first down" unexplained | One clause at snap 5 (some defensive fouls give a new set of downs whatever the yardage), sourced, with a pointer to 09-03. |
| §2 "next score in the game … before halftime" | Both now say the next score in the same half; the glossary entry matches. |
| §3 Fig 1 numbers read as labels | Caption adds "The big grey numbers are the yard lines painted on the field." |
| §3 Fig 4 buckets don't match text | The long bullet names "very long" (past 10). The grid's short column is now split into "1" and "2–3" (the coach's A1). |
| §3 Fig 5 tiny kink, run line past sideline | The kink is the point of the figure (driven back two yards) and the caption names it; left as is. Label fixes are in the coach list below. |
| §3 Fig 6 "own 40 to opp 46" boundary, claim spans two rows | Rebinned to own 1–19 / own 20–39 / own 40–49 / midfield to opp 36 / opp 35–21 / opp 20 to goal. The text now quotes each row it uses (51% own 40–49; 85% midfield to opp 36). |
| §3 Fig 8 "four short runs" vs "three" | The caption now says three short runs gained ground and still scored negative, and a fourth lost a yard. The callout says three, so they agree. |
| §3 Fig 9 shows only two spots | The XLVII panel now shows down boxes 1 (at the 7) and 2–4 (at the 5) with a note, so "four tries, no touchdown" can be seen. The XXXIV panel shows the slant (pass path, catch inside the 5, tackle at the 1). The caption calls both schematic. |
| §3 Fig 11 numbers covered by markers | Yard numbers removed from both drill diagrams. |
| §3 Fig 12 end zone unlabelled | Added "END ZONE" and "goalposts" labels. |
| §4 Length | Cut the gridiron-etymology tangent (now a sentence in the Camp footnote) and "by then a medical student". Moved the chain-clip parenthetical to its footnote. Shrank the one-currency box and the punt box to their core. The drives section no longer re-runs the 01-01 census; it prices it. Also trimmed the sticks, fumble and sack-data paragraphs, the turnover-scorecard ending, the neutral-zone aside and Connections. The prose is still about 700 words longer than before, because nearly every finding asked for something to be added (pricing arithmetic, EPA scale, breakeven table, glosses). See "Declined / partial" below. |
| §4 Predict 1 and 3 same punchline | Drill 3 is now about pricing (see §2). |
| §4 4th-down percentages appear three times | The overall split appears once, the chart once, and the text quotes only the chart rows it needs. |
| §5 Drill 2 tests unseen material | The question is now "the defense has lined up very deep: what is it worried about?", and the answer links 02-05 for the why. |
| §6 Graphic rounding | Added: the graphic shows whole yards, so the number is approximate; the line itself is the target. |
| §6 Fair catch; missed FG spot; fumble out of bounds | Fair catch defined and sourced. Missed FG at the spot of the kick is now stated in the fourth-down options. Fumble out of bounds points to 09-04. |
| §6 Does EP know score/time? | It knows time left in the half, timeouts, home team, roof and era, but not the score (sourced to Baldwin's nflfastR model write-up). The score enters through win probability (13-03). |
| §6 Why so slow to go for it? | Added Romer (2006, *JPE*): the departures from optimal choices are conservative, and his two explanations are asymmetric weighting of failed vs. successful gambles, and reliance on intuition over analysis. Quoted from the paper and footnoted. |

### Coach review: finding -> action

| Finding | Action |
|---|---|
| A1 Third-and-short blends 1 and 3 | Computed: 3rd & 1 = 21% pass, 3rd & 2 = 53%, 3rd & 3 = 75% (2025 neutral). Item 3 is now "Third-and-1 is a run down; third-and-3 is a pass down", with the three numbers. The grid splits "1" and "2–3". Answer 1 says about four in five third-and-1 snaps are runs and play-action is the exception. Added a sentence that call sheets cut third down finer than broadcast buckets (linked to 01-04, which owns "call sheet"). |
| A2 Second-and-short box contradicts data | Recomputed for 2021–2025 neutral: 2nd & 1–2 is 73% run, and its passes go 15+ air yards 17% of the time vs 19% for all other passes. So passes there are *not* more downfield, and the "play-action shots" claim was dropped. The box now debunks the "free shot" idea with those numbers. It uses "shot play" (linked to 04-05) rather than "free play", which 09-03 owns with a different meaning. |
| A3 Forecaster threshold | Third/fourth-down threshold changed to 2+. Recomputed accuracy: 66% (was 65%); "always pass" is 58%. |
| A4 Fourth-down caption and text | Caption: inside the 35, teams kick on 4th-and-4-plus but usually go on 4th-and-short. Text: the punt squeeze is described as starting once you cross midfield; own 40–49 is a near coin flip (51%). |
| A5 EPA sum | Fixed (see beginner §0.1). The XP-as-separate-play detail was left out as too fine for a primer: the model's "touchdown = 7" convention is already stated. |
| A6 Sack qualifier | Glossary and text: only on a pass play (a designed-run loss is a tackle for loss), and being forced out of bounds behind the line counts. Sourced. |
| B Fig 10 SS, LB depth, DL depth, "T" label | SS moved to d 3.8, outside the Y. Sam stacked over the Y at 3.5; Mike and Will at 3.5; DL at 0.7; tailback relabelled R. I kept the 4-3 rather than a 5-3 or 6-2 package, because the caption describes it accurately and 01-03 hasn't taught short-yardage fronts yet. |
| B Fig 11 safeties 17 → 14.5; W apex; number collision | Safeties at 14.5 (at the sticks). W at d 5.5, w −6.2, apexing H; Mike at 4.8. Yard numbers removed. Caption and answer text updated. |
| B Fig 5 label into ball; "40" under yellow line; hash ticks through label | Widened the left side of the window and moved the line labels to the far left, sitting on the lines with a turf-coloured backing, clear of the ball. Yard numbers removed. Added the forward-progress nuance (driven back vs retreating on his own; that's why a sack loses yards). |
| B Fig 8 ✓ collides with +2.95 | Fixed (EPA axis widened; ✓ column at the far right). |
| B Fig 2 quarter vs down; possession indicator | Fixed (see beginner §1). |
| B Fig 1 sideline label; chain crew opposite press box | Declined. The caption already places the crew on the sideline, and adding a label would crowd panel 1. I could not verify the press-box-side rule against the current rulebook, so per the coach's own caveat it was not printed. |
| B Fig 7 "roughly the 35 in" | Now "field-goal range (inside about the 35)". The 35–40 suggestion was not adopted: 35 + 18 = 53 is the realistic edge, and 40 + 18 = 58 would contradict the 67% make rate at 54–58 used in Drill 3. |
| C Ball's nose | Added: what counts is the ball's front tip, not the runner's body. Footnoted with the rule wording (college rulebook text as reproduced by BAFRA, with the NFL's tip-of-the-ball measurement). |
| C Holder, not kicker, at 7 | Now "the holder sets the ball down about eight yards behind the line" (data-backed; see §0.4). |
| C Punt outcomes: let it bounce, downed | Added to the punt bullet (return / fair catch / let it bounce and the kicking team downs it). |
| C Red zone: end line as a defender | Added: "the back of the end zone works like an extra defender, so there is no room left to throw over the top" (paraphrased, not quoted). |
| C 3rd & 11+ dip | Added to item 2: about one snap in 12 is a deliberate run there (computed: 8%). |
| C Success-rate dialect | Added (see beginner §2). |
| C Snap 5 "brought on the punt team" | Now "would have left fourth-and-5 at the Kansas City 42: a punt or a gamble." |
| D XXXIV Wycheck detail | Added, and sourced to Tennessee Titans, "Titans Recall Final Play of Super Bowl XXXIV" (Wycheck's route to influence Jones; Jones, in zone, came off him to the slant). |
| D XLVII zero pressure on 4th-and-goal | Declined. I couldn't find a source that confirms the Ravens brought zero coverage or an all-out blitz on that snap, so the text keeps the sourced "under pressure". |
| D XLVII intentional holding on the safety | Added, and sourced to BaltimoreRavens.com. |

### Declined / partial (summary)

- Length: still above the 4,000-word spec. Prose is about 8,100 words counted raw (markdown lists,
  callouts and headings included), against about 7,400 before. Both reviews mostly asked for additions, and
  the cuts above offset part of them.
- The coach's optional Fig 1 sideline tick, the chain-crew press-box detail and the XLVII zero-pressure
  claim were not added (reasons above).
- The extra point counted as its own play (coach A5) is left implicit.

### Fact-check impact

Every VERIFIED row in `01-02-factcheck.md` still holds. Rows changed:
- "Holder 7 yards back so FG length = yard line + 17": superseded by nflverse (90% of 2016–2025 attempts
  are + 18). Now "add 18", footnoted.
- "Gridiron nickname" (SOFTENED): the sentence moved into the Camp footnote, still giving both
  explanations.
- "1st & 10 run needs four or five yards": now "about 5", backed by the computed breakeven table.
- The third-down "1–3" pass share (46%) is no longer quoted. It was replaced by per-yard values (21/53/75%).
- The second-and-short pass share is now quoted as a 2021–2025 run share (73%), with the air-yards comparison.
- New sources: Romer (2006), Baldwin / Open Source Football (EP features), Wikipedia (Quarterback
  sack; Fair catch; Down), BAFRA rule text (forward point of the ball), Tennessee Titans (XXXIV),
  Baltimore Ravens (XLVII safety).
