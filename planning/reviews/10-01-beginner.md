# 10-01 Early Downs and Field Zones: beginner-reader review

Reviewer persona: casual NFL watcher, never played, has read Parts 1-9 in order (not 13-02 or 13-04).
Read the rendered PDF (pdfs/10-01-early-downs-and-field-zones.pdf, 20 pages, rasterized and zoomed
where needed) start to finish, plus the .qmd source for exact wording.

Overall: the strongest analytical chapter I've read so far. The opening hook, the "establish the run,
four claims" section, and the on-schedule bar chart are excellent. I understood the ideas. The real
problems are a few internal contradictions in the numbers, one promised "why" that never comes, an
ambiguous use of "points", and one diagram (the field-zone map) where lines cut through text.

## Must fix

1. **Third-and-short past midfield: the chapter contradicts itself.** The key passages:
   - Plus-territory section: third-and-2-to-4 is thrown "86%" of the time in the offense's own half and
     "73%" past midfield.
   - Table 1: "3rd & short (1–3), plus territory | 45% | run | 55%", and "3rd & short (1–3), own half |
     56% | pass".
   - Takeaways: "past midfield ... third-and-short turns into a running down."
   - Watch for it: "third-and-short past midfield (expect a run ...)".
   - Predict 3 (third-and-**3** at the opponent's 38): the answer leads with "A run is a live option
     here", but the chapter's own number for exactly this situation is 73% pass.

   As a beginner I got two "short" definitions (1-3 and 2-4) with no reason given for switching. Their
   numbers disagree badly: 56% vs 86% in your own half. The takeaway "turns into a running down" is
   only true for 3rd-and-1, which pulls the 1-3 bucket toward the run. In Predict 3 the data says
   "pass, about 3 to 1", while the prose pushes me toward "run". Fix: pick one bucket, or explain in
   one sentence why the 1-yard column is different (the heatmap shows it is). Reword the takeaway to
   "the run comes back into play". Give the Predict 3 answer a clear headline ("Still more likely a
   pass, about 3 in 4, but a run is far more likely than in your own half...").

2. **"Points" means two different things.** Here "points" means percentage points of conversion,
   in a chapter where "points" normally means EPA/expected points:
   - "every yard is worth three or four points of conversion"
   - "From second-and-5 or longer, a wasted down cost about 24 points on average"

   "Cost about 24 points" reads as 24 *points*. Use "percentage points" every time, as the sentence
   just before it does ("13 percentage points").

3. **The promised "why do most teams still run on second-and-short" never arrives.** "You'll be able
   to" item 3 promises it. The bucket list says "That contradiction gets its own section", but the
   section "Why second-and-short is a shot down" only argues for the shot. The only reasons for running
   are half a caption clause ("runs convert two times in three") and the closing "could take this shot
   more often". I finished the section unable to say why 70% of teams run there. It needs a short
   paragraph: the run converts on the spot two times in three and keeps the chains moving, deep shots
   need max protection and time and risk a sack (the drive-killing negative play from the
   on-schedule section), habit and risk aversion (Romer again), and the defense sometimes plays the
   shot anyway.

4. **Wrong back-reference for success rate.** On schedule section: "The yardage version of success
   rate you met in [13-02], 40% of the yards on first down and 60% on second". A reader in order has
   **not** met 13-02. The 40/60 version is taught in 01-02 (around line 943). Point to 01-02 instead,
   and mention 13-02 only as a forward reference.

5. **Field-zone map (Fig 7): lines run through text.**
   - The dotted "field-goal range begins" line cuts straight through "FOUR-DOWN TERRITORY", "(the
     fringe)" and "fourth down is part of the plan" (reads as "FO|UR-DOWN", "(t|he fringe)",
     "pa|rt of the plan").
   - The 5-yard grey lines cut through the small "get out: no sack, no turnover" and "first first down;
     flip the field" text and through the bracket text "minus territory".

   Give the text a background patch like `say()` does, or move the field-goal line or label. Also:
   - The blue strip from the 50 to the +40 has no label. It is open field, but "OPEN FIELD" is centred
     well inside minus territory, so it looks like a sixth, unnamed zone.
   - The text then says "The plus side isn't one zone; it holds the next two". Per the map it holds
     *three*: the end of the open field, four-down territory and the red zone.

## Should fix

6. **Common misconception, second-and-long: the logic slips.** "Two downs to gain ten yards is a much
   harder problem than three downs." Both cases in the comparison (0-yard gain and 4-yard gain) leave
   two downs. The real contrast is two downs for 10 vs two downs for 6. As written it compares the
   wrong things.

7. **Repetition: third-and-3 at the opponent's 38.** The same point ("a stop isn't a stop; fourth down
   is coming") appears five times:
   - the opening paragraph
   - the plus-territory section
   - the paragraph after it ("On third-and-3 at the opponent's 38, a stop isn't a punt")
   - the Lions film room ("a stop on third-and-3 at the plus 38 isn't a stop yet")
   - the Predict 3 answer

   01-02's Predict 3 already taught it (third-and-short at the opponent's 45, "Coaches call this
   four-down territory"). Cut the stand-alone defense paragraph and the Lions repeat. Ideally change
   Predict 3 to something 01-02 didn't drill, such as the coming-out or field-goal-fringe situation.

8. **Predict 2 is framed as a trick.** The prompt asks "Run or pass?" and the answer is "a pass is
   still a slight favorite (56%)", with the headline "More likely a run than ...". Everything the
   chapter taught (alternation, a light box) pushed me to say "run", and then I was told that's wrong,
   sort of. Either ask "More or less likely to pass than a normal second-and-10, and why?" or lead the
   answer with "Pass, barely (56%), well below the 83% after a no-gain run".

9. **"Game theory" leap.** "in game theory, the right mix of runs and passes shouldn't depend on what
   you called last time". Why? The reason is one clause: if it did, the defense could predict you from
   the last play. Also, the most important finding (the habit makes plays *less effective*) is only in
   footnote 11. Put it in the text, because that is what makes the tendency worth charting. 08-02
   already has a misconception box, "A balanced offense alternates run and pass" (around line 1105).
   Link back to it rather than introducing the idea fresh.

10. **The second-down bucket list is in a strange order.** It runs long, very long, medium, short, but
    the chart (Fig 5) and the heatmap go short to long, and so does the bucket definition. I kept
    looking back and forth. Match the chart order.

11. **The "on schedule" definition disagrees with itself.** It says "about half of what's left on
    second down". The next sentence says the yardage success rate is "60% on second", and calls that
    "the schedule turned into a number". Half or 60%? One line reconciling them would help.

12. **Watch for it tags don't match the zones just taught.**
    - The drill says to tag "the zone", and the examples use "plus territory", which the chapter says
      is *not* a zone.
    - Table 1 has no coming-out, open-field or four-down rows ("rest of the field" instead).

    Align the tag vocabulary with the five zones, or say explicitly that the table merges them.
    Also, "watch the safety's eyes" is not possible on a broadcast angle (01-06 taught this). Say
    "count the deep safeties before the snap" instead.

## Diagrams and captions

- **Fig 6 (second-and-1 shot strip):** frames 1, 3 and 4 tell the story; frame 4 is great.
  - Frame 2 ("the fake: linebackers and the strong safety step up") doesn't show it. The defenders
    move about a yard and the Q/R mesh is a smudge. Add a ring or arrow on the stepping linebackers,
    or exaggerate the step.
  - In frames 3-4 the linebackers have the same depth as each other, so "turn to chase, too late"
    isn't visible. The caption doesn't need it, but the code tries to show it.
  - Frame 2's "Q" glyph is overstruck by its own trail.
- **Fig 4 (team scatter):** "What every season in the top band shares" — I don't know what the "top
  band" is. Also, only the vertical dashed line is labelled ("league average"); label the horizontal
  one too.
- **Fig 8 (zone calls):** the top-panel "BACKED UP" label touches the left axis edge, and "BACKED UP
  COMING OUT" reads as one run-on label. The caption is long but good.
- **Fig 10 (heatmap):** the white numbers on light-blue cells (2nd down 12-15+: "82 85 83"; 3rd down
  "88") have low contrast. Use dark text there or a darker threshold. The caption tells me what to
  notice, which is great.
- **Correlations** (0.67, 0.03, 0.26) are quoted with no scale reminder. 07-01 glossed it ("0 = no
  carry-over, 1 = perfect"). Add a half-sentence the first time.
- **Predict 2 and 3:** at small print size the nickel's "$" is hard to tell from "S" (Sam). It is fine
  at full resolution, but bump the label size if cheap.
- **Fig 9 (backed up):** clear and effective. The fact that a shotgun snap is "3 yards deep in his own
  end zone" landed immediately.
- **Fig 2 (on schedule bars)** and **Fig 3 (establish the run)** are the best figures in the chapter.

## Terms used before explained, or never explained

- Fig 1 and the "four answers" switch between "pass", "called pass" and "dropback" without saying
  they are the same thing. Fig 1's caption covers it, but "dropbacks" first appears in a legend.
- "flip the field" is used in the zone map before it is glossed in the coming-out bullet. Minor.
- "field goal would be 56 yards" from the opponent's 38, and "a 51-yard field goal" at the plus 33:
  the +17 conversion isn't restated. 09-01 covers it, but a parenthetical would save a flip back.
- "selection effect" is credited to 13-02. 02-05 actually introduced it, so link there.
- "Backed up" is defined here as inside the 10. 08-03's call sheet defines it as "inside our own 5".
  The chapter says boundaries vary, but name the discrepancy, since I've seen both.
- "Between the 25s" (open-field section) conflicts with "your own 25 to the opponent's 40" two
  paragraphs earlier.

## Can I do the "You'll be able to..." items?

1. Why first-and-10 is balanced, and which parts of "establish the run" survive: **yes**, clearly.
2. On or behind schedule after a first-down play: **yes** (the 4-yard rule). "Why that matters more
   than the yardage" is odd phrasing, since the schedule *is* yardage. The chart shows conversion
   rate, so the objective should probably say "why it matters for the rest of the series".
3. Four buckets: **yes**. Why second-and-short is a shot down: **yes**. Why most teams still run on
   it: **no** (see item 3).
4. Name the zones and what changes in each: **mostly**. The plus-territory/open-field overlap and
   "plus territory isn't one zone" confused me.
5. Read the heatmap and EPA chart: **yes**. The "three steps" reading guide for Fig 11 is excellent.

## Predict the play (attempted before opening the answers)

- **P1 (1st & 10 at own 3):** I said run, and ruled out a shotgun dropback and a long-developing pass.
  **Correct**, straight from Fig 9. The "surprise" play-action note was a nice payoff.
- **P2 (2nd & 10 after an incompletion):** I said run (light box plus alternation). The answer says
  pass is still a slight favorite. **Half right**, and it felt like a trick (item 8).
- **P3 (3rd & 3 at opp 38):** I said run, because the chapter primed me. By the chapter's own number
  (73% pass) I was wrong, and the answer's headline dodges this (item 1). The "would it change at your
  own 38?" half: yes, pass, which I could do.

## Knowledge gaps: what I still wonder

- **The defense's call sheet.** The chapter is almost all offense. What does a defense do backed up
  (load the box and pressure, hoping for a safety?), in four-down territory, or on second-and-short
  besides "base, eight in the box"? Even one paragraph or a defensive column in the zone map would help.
- **The coming-out zone:** there is no number in the text (only "by about the 15 to the 20 ... looks
  like everywhere else"). How much better is a team's punting position after one first down?
- **Did the 2018 Chiefs and Rams' early-down passing spread?** The first-down trend line says no.
  If not, why not, given how famous those offenses were? One sentence tying the case study back to
  the flat Fig 1 line would close the loop.
- **Is the "plus 35" field-goal line moving** as kickers get stronger, and so shrinking four-down
  territory? The zone map's dotted line invites the question.
- **Is going for it in four-down territory actually right?** The chapter keeps pointing at 10-04,
  which is fine. But I'd like one sentence on whether the 77% go rate is correct or too aggressive.

## Revision (2026-10-08)

Covers both this review and `10-01-coach.md`. The fact-check is unchanged: no verified claim was
altered, and every new number is a course calculation with an assert guard and a footnote. Rebuilt
with `build_pdfs.py 10-01-early-downs-and-field-zones --html` (OK, zero errors, 21 pages). I
rasterized every diagram page and looked at each one again, at 110-250 dpi.

### Beginner review

| # | Finding | Action |
|---|---|---|
| 1 | Third-and-short contradiction (1-3 vs 2-4; "turns into a running down"; Predict 3 headline) | Plus-territory section now says third-and-1 is a run down everywhere (sneak; 24% pass) and that the yard line's effect shows on 3rd-and-2-to-4 (86% own half vs 73% past midfield). The text says "still a passing down, but the run comes back into play". Tag table rebuilt as 3rd & 1 / 3rd & 2-4 own half / 3rd & 2-4 their half / 3rd & 5+. Takeaway, checklist and the zone-chart intro reworded. Predict 3 headline is now "Still more likely a pass, about three times in four, but a run is far more likely than in your own half". |
| 2 | "Points" ambiguous | "percentage points" everywhere conversion is meant. |
| 3 | Promised "why most teams still run on 2nd-and-short" missing | New subsection "Why most teams still run on second-and-short" gives four reasons. (a) The run moves the chains on the spot 66% of the time, 79% on 2nd-and-1 (new computed numbers). (b) The shot's cost: max protection, two receivers, sack risk. (c) Romer's asymmetry. (d) Two-high answers. The bucket bullet now points to both sections. |
| 4 | Success-rate back-reference to 13-02 | Now points to 01-02. 13-02 is a forward reference only. |
| 5 | Field-zone map: lines through text; unnamed 50-to-+40 strip; "holds the next two" | Every zone name, goal, bracket caption and note sits on a light patch. Four-down text moved to x = 81.5, clear of the dotted field-goal line. "OPEN FIELD" is centred on its full span with a \|-\| extent bar across midfield. "−35" added under the touchback triangle, and "(about +35)" added to the field-goal note (a bottom-row "+35" collided with "+40", so I moved it). The text now says the plus side holds "the last ten yards of the open field and the next two zones". |
| 6 | Misconception logic (two downs vs three) | Now "either way the offense has two downs left, but two downs to gain ten ... than two downs to gain six". |
| 7 | Third-and-3-at-the-38 repeated five times | Cut the stand-alone defense paragraph, the Lions-box repeat and the Predict 3 defense paragraph. The defense's view now appears once, in a new "The defense reads the same map" subsection. **Declined: changing Predict 3's situation.** 01-02's drill is fourth-and-2 at the 38 (the go/kick/punt decision). This drill asks how that option changes the *third*-down call, which is new in this chapter and is what the 86/73 data teaches. |
| 8 | Predict 2 felt like a trick | The question now asks "Is a pass more or less likely here than on a typical second-and-10?" The answer leads "Less likely than usual: still a pass more often than not, but only barely (56%), against 83%..." |
| 9 | Game-theory leap; the key finding was buried in a footnote | Added the clause "if it did, the defense could guess the next play from the last". The Emara et al. finding (the habit made plays less effective) is now in the text, with a link back to 08-02's "alternates" misconception box. |
| 10 | Bucket list order | Reordered short → medium → long → very long, to match the chart. |
| 11 | "Half" vs "60%" | Definition (text and glossary) now says "a little more than half of what's left". One line reconciles it with the 40/60 yardage rule: 4 of 6 after a 4-yard gain leaves 3rd-and-2. |
| 12 | Tags don't match zones; "watch the safety's eyes" | The tag table splits first-and-10 by all five zones (backed up / coming out / open field / four-down territory / red zone). The example tag is now "Third and three, four-down territory". A sentence explains the table's cuts. "Count the deep safeties before the snap" replaces "watch the safety's eyes". |
| Fig 6 | Frame 2 didn't show the step; Q glyph overstruck | Linebackers and SS now step up about 2 yards (stopping short of the DL squares). Frame 2 moved to +0.9 s, when Q and R have separated. A carried ball is now drawn beside its carrier, so it never covers his letter (chapter-local `panel()` change). |
| Fig 4 | "Top band" unclear; horizontal line unlabelled | Both dashed lines are labelled ("league-average pass rate", "league-average EPA"). "Top band" is now "the offenses near the top of the chart, whichever side of the average pass rate they sit on". |
| Fig 8 | Top labels touching / run-on | Two-line zone labels at 5.6 pt, with the y-limit raised. |
| Fig 10 | White text on light-blue cells | White text only at ≥90% (or ≤15%). The 79-88 cells are now dark text. |
| — | Correlations with no scale | First use now says "a correlation runs from 0, no connection at all, to 1, a perfect one", and the scatter text repeats "on that 0-to-1 scale". |
| — | "$" vs "S" at small print size | **Declined.** The book's label convention and the gridiron marker size set it, and it is legible at full resolution. Enlarging only this chapter's drill glyphs would break consistency. |
| Terms | pass / called pass / dropback | One-sentence definition added before Fig 1. |
| Terms | "flip the field" before it's glossed | Glossed in the Fig 7 caption, and the coming-out section now quantifies it. |
| Terms | FG distance +17/18 not restated | Restated in the fringe section ("the yard line plus about 18 ...") and in Predict 3 ("38 plus 18"). |
| Terms | Selection effect credited to 13-02 | Now credited to 02-05, with 13-02 as the forward reference (body and Connections). |
| Terms | Backed up: inside the 10 vs 08-03's "inside our own 5" | The backed-up bullet names the discrepancy and explains the tight sub-zone (minus 1 to about minus 4 or 5). |
| Terms | "Between the 25s" | Now "from your own 25 out to about the opponent's 40". |
| Objective 2 | "matters more than the yardage" | Now "say what that does to its chances for the rest of the series". |
| Gap | The defense's call sheet | New subsection "The defense reads the same map": backed up, open field, four-down territory, the field-goal fringe and second-and-short, from the defense's side. |
| Gap | Coming-out zone had no number | Added: after a punt from the own 10-15, the opponent started at about its own 43. After a punt from the own 25-30, about its own 28. So one first down is worth about 15 yards of field position (nflverse 2021-2025, new footnote). Also added the first-and-10 pass rate in the zone: 47%, against 33% backed up and 49% in the open field. |
| Gap | Did 2018 early-down passing spread? | Added to the KC/LA film room. 2018's neutral first-and-10 pass rate (48%) was the decade's high, and no season since has matched it. What spread was *how* those teams threw, not how often. |
| Gap | Is the field-goal line moving? | Added: 50+ yard tries went from 150 (2016) to 266 (2025), and the make rate from 57% to 69% (nflverse, new footnote). So four-down territory shrinks with a strong-legged kicker. |
| Gap | Is going for it right? | Added one hedged sentence: public models (nfl4th) generally favor going on fourth-and-short in this zone, and 10-04 prices the decision. Cited to nfl4th, the same source 10-04 uses. |

### Coach review

| # | Finding | Action |
|---|---|---|
| 1 | Drill 1: "worst case is 2nd-and-12, not a safety" wrong | Answer rewritten. The handoff comes around the goal line, and penetration at the mesh is a safety. Staffs cheat the back up and call downhill runs (dive, iso, duo, sneak). They cross off a deep mesh or long lateral path (stretch, toss, counter with pullers). R moved to d = −5.5 in Predict 1 and in Fig 9 panel B, with the leader target updated. |
| 2 | Zone map collisions; label −35 / +35 | Done; see beginner item 5. |
| 3 | Shot strip ends before the catch | Times are now [0, 0.9, 3.1, 4.8]: snap, fake, release, catch. Re-simulated after the route change, the ball reaches Z at 4.8 s. Notes rewritten as suggested. |
| 4 | Over depth vs 04-04; X stops on the top edge | Z route raised to (17, −9) → (20, −24). It is caught at about 18.5 yards, in front of the LCB, which now drops to (21, −18). X post extended to (28, 11), and the window is widened to 30, so X stays 3.5 yards inside the edge. |
| 5 | Pistol depth | Q at d = −4.0, R at −7.0. Caption: "about four yards behind the ball". The window is widened to −10, so R stays 3 yards inside the edge. |
| 6 | Name the coverage; Cover 1; 7- vs 8-man protection | "Cover 3" in the caption and in frame note 1. A new paragraph covers the same look as Cover 1 (the over becomes a man-beating crosser, and the QB reads the man). The caption adds "(max protection; some teams release a tight end late as an outlet)". |
| 7 | Personnel follows personnel | Points 2 and 3 merged into one causal chain: heavy offense → base → eight in the box → one high. Also added the 11-personnel case (nickel with a safety walked down). |
| 8 | Throwaway / grounding in the end zone | Added: grounding from the end zone is a safety, and a legal throwaway needs the QB outside the tackle box with the ball reaching the line of scrimmage. That is why backed-up passes are quick or rolled out. Links 09-04. New footnote cites Rule 8-2-1 and Rule 11-5 (operations.nfl.com rulebook). |
| 9 | Punter depth numbers | Backed-up bullet: usual depth 14-15 yards, end line 12 yards back at the 2, so he sets up a step in front of it. A blocked punt there is a safety or a touchdown. This matches 09-01's text. |
| 10 | The opening script | New paragraph in "The situation comes before the play", linking 08-03's glossary entry and its section. It notes that some early-game early downs are pre-planned, which qualifies the first-half run-rate panel. |
| 11 | Shot boxes (sudden change, crossing midfield, coming out) | Listed at the end of the new "still run" subsection, with a link to 08-03's sudden-change box. The plus-territory bullet ties "we got the ball in plus territory after a turnover" to the sudden-change shot. |
| 12 | Rams 2018 personnel sameness | Added and verified with data. The Rams ran 93% of their runs and passes from 11 personnel, the league's most (league 65%). Source: nflverse participation (NGS) 2018, with an assert guard and a new footnote. |
| 13 | "Free play" | Opening parenthetical: booth slang. Strictly, a free play is a snap where the defense jumped offside (links 09-03's glossary entry). |
| 14 | Backed-up sub-zones | Promoted to the body (backed-up bullet), with the minus 1 to about minus 4/5 tight box. This also reconciles 08-03's "inside our own 5". |
| 15 | "Lean run" after an incompletion | Checklist now says "less pass than usual, though still slightly more likely a pass". The Predict 2 headline is reframed. |
| 16 | "Almost certainly throw" at own 38 | Now "probably throw, about six times in seven". |
| Fig 9 A | LE loop brushes H | First waypoint tightened to (−3.5, −1.6). |
| Optional | A concrete Lions look | **Not added.** No verified source is at hand for the Lions' personnel mix, and the box already links 08-02's Lions tendency table. |

Notes: gridiron was not edited. The held-ball offset and the zone-map patches live in the chapter's own
helpers.
