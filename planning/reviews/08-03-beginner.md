# 08-03 Game-Planning Week: beginner reader review

Reviewer persona: casual NFL watcher who has never played, has read 01-01 through 08-02 in order.
Read the .qmd start to finish and looked at all 20 PDF pages (60 dpi, plus 130 dpi for pp. 10-11 and 15-19).
Overall: very strong. The week calendar, the tendency report, the matchup grid and the annotated call sheet are
exactly what this beginner wanted. The voice matches the pilots. The problems are a handful of internal
contradictions between figures (the worst is who covers Y), one wrong count on a diagram, and a few loose ends.

## Must fix (contradictions and errors a careful beginner will catch)

1. **Who covers the tight end in "their usual" Cover 1? The chapter gives two different answers.**
   - Matchup grid note (fig-matchup-grid): "Y vs W: line up 3x1 with Y inside; in their usual Cover 1 **the Will
     has the third receiver**." The grid's best cell is Y vs W (+2.0); Y vs M is only +1.5.
   - fig-take-away, top panel and caption: "The rules hand the tight end (Y) to **the Mike** linebacker (red ring),
     which is the offense's best matchup on the board". Label: "M has Y: our best matchup". In the drawing M
     covers Y and W covers R.
   - Predict 2 has the Will on Y again, and its answer says "exactly the cell circled on the matchup grid".
   I spent several minutes trying to work out whether the Mike and Will swap jobs. Pick one version (the Will on Y
   fits the grid and Predict 2) and redraw the top panel of fig-take-away to match. Also update the
   `game_plan_dime` docstring and the caption ("D replaces the Will").

2. **Predict 3 label "SS down: an eighth defender to that side" is a wrong count.** In the drawing the box holds
   4 linemen + S + M = 6. The Will has walked out over H, so the SS makes **seven**, not eight. 05-05 taught me to
   count the box, so I counted, and the label made me doubt how I count. Fix the label (for example "SS down: a
   seventh in the box, on the TE side"), or explain what "eighth" is counting.

3. **Predict 2 answer vs the call sheet.** The answer says the Y option "is probably the first call in the '3rd &
   3-6, vs man' box." On fig-call-sheet the first vs-MAN call in that box is "Gun Bunch Rt 70 Mesh". The Y option
   ("Gun Empty Fly 62 Y Opt") comes second. Either reorder the sheet or say "second call".

4. **Wrong pointer:** "(5) The package. A box built for this opponent only, which **the next section** explains."
   The next section is The opening script. Packages come two sections later. Write "which the Game-plan packages
   section explains".

5. **"Script reason 3" is contradicted by the chart printed just above it.** "The payoff comes later... If that
   works, the gain shows up in snaps 16 to 60, not 1 to 15." The left panel of fig-script-data shows snaps 16-60
   at about zero EPA too, so the gain does *not* show up there. A demanding reader will ask "so where is it?" Either
   admit that the payoff can't be seen in league-wide averages (one team's gain is another team's loss, and
   defenses adjust too), or soften the claim.

6. **Timeline inconsistencies about Tuesday.**
   - Packages: the Viper package was "drawn up on Tuesday", but the calendar builds the 3rd-down plan on
     Wednesday night. A third-down blitz answer belongs in that plan.
   - Reid film room: "Many of them come from **that Tuesday index card**". The callout itself says the script card
     is written and texted on *Friday*, and the new-play cards come "early in the week". Name the card it means.

## (1) Terms used before they are explained, or never explained

- **"Viper"** (call sheet header 'PACKAGE vs "Viper" pressure'; packages section). The chapter never says this is
  the sample opponent's own name for its blitz, invented for the example. A beginner may think it's a standard
  football term to look up.
- **Call-sheet shorthand that is never decoded:** "2-pt: go if then down 2 or 5", "4th & 1: go from own 35 on",
  "vs 5+:", "Post-Whl", "Go-Whip", "Fly 62". 01-04/04-08 taught the "24" numbering, but nothing taught these. The
  4th-down box is the one I couldn't read at all. Add one sentence under (6) that translates a single line, e.g.
  "go for two if, after this touchdown, we'd still trail by 2 or 5".
- **"radio down"** (calendar, QC Sunday cell). This is jargon. Something like "booth: chart the opponent, relay to
  the sideline" would be clearer.
- **"tendency breaker"** is used three times (line ~650 "plan the tendency breakers", the misconception callout,
  the packages section) but is not in the "You'll need" box and is never linked. 08-02 owns it, so add it to the
  box or link the first use.
- **"A quarterback who has played in the system"** (Tuesday). Which system? It's Wolford with the Rams, but the
  text never says so. Name him in the text.
- **"Paul Brown assistant"**. Paul Brown is never introduced. A two-word gloss would do.
- **Correlation 0.32 / 0.09** is fine (04-05 taught correlation), but a reminder like "(0 = no carry-over, 1 =
  perfect)" would help, as 07-01's chart did.

## (2) Leaps: a missing or assumed "why"

- **The opening vignette's own question goes unanswered in the body:** "if they knew it would work, why not run it
  again on the second snap?" The answer (it was a test; save the look for third down) appears only in the Predict 1
  answer at the end of the chapter. The script section mentions "the opening scene" but stops short. Answer it in
  the "What's on one" paragraph.
- **"Three real practices a week, and only so many of them in pads."** The footnote's number (14 padded practices
  in a season) is the striking fact. Put "about one padded practice every week or so" in the text.
- **Tendency report colors.** "Blue cells are well above the league rate, orange well below." Blue and orange are
  this course's offense and defense colors. I first read blue as "good for the offense". Add half a sentence:
  "(blue/orange = higher/lower, not good/bad)".
- **The table's loudest cell gets no comment:** 3rd & 7+ man coverage 19% vs NFL 33%, the darkest orange in that
  column. The bullet for third-and-long talks only about pressure. So on third-and-long Seattle rushes five and
  plays *zone*. What does the OC call? That is exactly the "so what do I call?" the section promised.
- **Fig 5 bill (2): "only five defenders are left near the line".** I counted six (E T T E, M, and D, all within 3
  yards of the line). It's five only if D, over Y outside the end, doesn't count as a run defender. Say so, and
  move badge (2): it floats in the offensive backfield and points at nothing. Shading the box tackle-to-tackle in
  both panels would make the run bill visible.
- **SumerSports "about 60% of teams were more efficient on scripted plays, not far from the 50% a coin would
  give."** Is 60 vs 50 meaningful or not? A beginner can't judge. One clause on why it's weak evidence (each team's
  15-play sample is noisy) would help.
- **"gaps that size are worth a touchdown or more"**: 0.25-0.33 EPA x ~124 targets is 30-40 points, which is four
  or five touchdowns. "A touchdown or more" undersells it, and anyone who does the arithmetic gets confused. Say
  "several touchdowns".
- **The wind game's last line:** "The best thing to take away that night was the weather's." I couldn't parse it.
  The Patriots didn't take anything away. They built the plan around the weather, so it is an example of
  "plans shaped by non-roster things", not of taking away. Rephrase.
- **Why does the play-caller want the call in with 20 seconds left?** (Reid/Nagy). 01-04 covered the radio cutoff.
  A short reminder clause would help.

## (3) Diagrams

- **fig-game-week:** the logic is excellent, but the cell text is 5.3 pt. Even at print size it is the smallest
  text in the chapter, and at screen zoom it is unreadable. The page before it (p. 2) is half blank because the
  figure got pushed. Consider fewer words per cell or a taller figure.
- **fig-tendency-report:** easy to read. See the color note above.
- **fig-matchup-grid:** clear. The column header "RCB / star CB" next to the note "he stays on the offense's right"
  made me pause, because the course says left/right are always the offense's. It works, but a beginner wonders
  whether RCB means the defense's right. Consider "star CB" alone.
- **fig-take-away:** apart from the M/W contradiction (Must fix 1) and the stray badge 2, the top-vs-bottom story
  reads well. The purple rings on D/SS/FS are clear.
- **fig-take-away-play (frame strip):** panels 1-3 tell the bracket story well. **Panel 4 does not show "X has beaten
  a cornerback"**: the CB sits about 2 yards from X, deeper than him, and the ball is a barely visible dot. I would
  read it as "X is covered". Show clear separation, or say "the corner is still backpedalling as X stops", and
  make the ball bigger or ring X.
- **fig-call-sheet:** great artifact, and the numbered key works. See the decoding notes above.
- **fig-script-data:** clear, and the caption says what to notice. Page 15 above it is about half blank (a layout
  gap).
- **fig-predict-takeaway:** Q, under center, overlaps the C marker (label collision). Fix the "eighth defender"
  label (Must fix 2).
- **fig-predict-script / fig-predict-matchup:** clean, no collisions.

## (4) Drag and repetition

- **Predict 1 restates the opening vignette** (two split tight ends, linebackers walk out) and the "What's on one"
  bullet that discusses it. That tests recall, not transfer. Change the drill: say the defense *substituted* a
  nickel back instead, and ask what the offense learned and what it comes back with.
- "**since 2007**" appears twice in one sentence (SumerSports).
- The Reid material is split between the call-sheet section and the film room, and the film room ends with the
  meta-note "(Both of those details come from the ESPN piece cited in the call-sheet section.)". That's
  footnote housekeeping showing in the prose. Either move the ESPN Reid details into the film room and cite there
  (and drop the call-sheet use), or cut the note.
- "The bill" motif is used about ten times. It's effective, but tighten a couple (e.g. "the bill came due somewhere
  else" in the fig-take-away-play caption right after the paragraph that just said it).
- The Super Bowl XXV plan is listed at line ~976 and then gets a full film room 70 lines later. That's fine, but
  the first mention could drop XXV.

## (5) Can I do the "You'll be able to..." items?

1. **Walk the week day by day:** yes, comfortably. The calendar plus the "why that order" box nail it.
2. **Read a situational call sheet:** mostly. I understand boxes, ranking, pairing, shots with triggers and the
   script box. I could **not** read the 4th-down/2-pt box or several play names (see above).
3. **Spot the script / say what the data says:** yes. The script detector is concrete and doable. I can state the
   result (no EPA gain, slightly more new looks). Reason 3 left me unconvinced (Must fix 5).
4. **Matchup hunting and taking away the best thing:** yes on the concepts (formation/motion/personnel; the bill).
   The M/W contradiction shook my confidence about which defender a rule hands the TE.
5. **Scouting the play-caller/QB; QC vs analytics; reading a tendency report:** I can list the questions and the
   QC/analytics split, and read the report's numbers. The scouting section is all bullets with no worked example,
   so I could recite it but haven't *seen* it done (see gaps).

**Predict-the-play attempts (before opening answers):**
- **PtP 1:** I said: "A script test. Watch how the defense aligns to a new formation. LBs walked out means a TE on
  a LB in space, so expect a quick throw to a TE, and the booth notes it for later." This **matched** the answer.
  It was too easy because the vignette and body already said it.
- **PtP 2:** I said: "Mike ran with the back, so man coverage. The Will is alone on Y, so throw to Y on an option
  route." **Matched.** It was nearly given away: the red ring (legend: "the matchup a plan is hunting") and the
  label "W still on Y" print the answer in the figure. I also wondered about the SS, who has drifted over the slot.
  Is he helping on Y? The answer doesn't say. Consider removing the red ring and mentioning the SS.
- **PtP 3:** I said: "Play-action off the outside-zone look, a shot behind the SS and linebackers, because there's
  one deep safety and it's second-and-3." **Matched** the lead option. The answer hedges three ways (PA, throw to
  H, run left), so it's hard to be wrong. Say which is the best call and why, then list the others as
  alternatives. The "eighth defender" label confused my box count.

## (6) Knowledge gaps: what I still wonder

- **The defensive week.** All the detail (call sheet, script, installs) is offensive. What does a defensive call
  sheet look like (fronts/coverages/pressures by situation)? Does a DC script his first series? Reason 1 of the
  data section says he does, but the chapter never shows it.
- **Sizes.** How many plays go in per install day? How many calls are on a sheet vs how many get used in a game?
  ("a few hundred calls" on the sheet, but roughly 60-65 snaps are played). Give rough numbers.
- **A worked scouting example.** One real play-caller habit with a source (his go-to 3rd-down concept, or what he
  calls after timeouts) would make the scouting section as concrete as the rest.
- **Scout-team cards.** What do they look like? A tiny mock-up, or one sentence on the card-in-the-huddle routine,
  would help.
- **Week 1.** It's called the hardest game to plan for. So what do staffs actually do then (preseason film, the
  coordinator's old team, the base defense)?
- **Who has the final say:** head coach or coordinator?
- **Broadcast tie-in:** why play-callers cover their mouths with the call sheet (lip-reading). It's a natural
  "Watch for it" detail for this chapter.
- **Limits on scouting:** what's legal (film, public data) vs not (filming signals). One line would address the
  obvious "Spygate?" question.

## Revision (2026-10-08)

Addresses this review and `08-03-coach.md`. The fact-check rows are unchanged. New factual claims have sources (new
footnotes: `[^snaps]`, `[^petzing]`, `[^proe]`, `[^spygate]`, `[^bb]`, `[^reidcards]`, plus a Paul Brown HOF link
in `[^walsh]`). Rebuilt with `build_pdfs.py --html`: OK, 24 pages. I looked at every figure page at 60 dpi, and at
the game week, take-away, frame strip, matchup grid, call sheet and the three Predict figures at 110-150 dpi.

| Finding (beginner = B, coach = C) | Action |
|---|---|
| B-Must 1 / C-A1: Mike or Will on Y | `their_usual()` swapped: the Will has Y (red ring, "W has Y: our best matchup") and the Mike has the back. Caption, docstring and lead-in sentence updated. Grid, Fig 5, Predict 2 and the call sheet now agree. |
| B-Must 2 / C-A5: "eighth defender" | Label is now "SS down: a seventh man in the box, TE side". |
| B-Must 3 / C-A6: Y option not first in the vs-MAN box | Reordered the sheet: "Gun Trey Rt Zoom Y Opt" is first and Mesh second. "Zoom" (back motions out) matches Predict 2, and the answer says "first call". |
| B-Must 4: wrong section pointer | Now "which the Game-plan packages section below explains". |
| B-Must 5: script reason 3 contradicted by the chart | Rewritten as "the payoff comes later, and averages can't see it". The defense learns from the same snaps, and one side's edge is the other's loss, so league averages can't show it. |
| B-Must 6: Tuesday timeline | The Viper package is now flagged in the QC blitz report, drawn up Wednesday night in the third-down plan and installed Thursday. The Reid film room now says "those early-week index cards". |
| "Viper" undefined | Explained under (5): it's the sample opponent's own name for its blitz, invented for the example. Sheet header changed to 'vs their "Viper" blitz'. |
| Call-sheet shorthand | Under (6) the 4th-down/2-pt box is decoded line by line, including why down 2/5 and up 1/5. A paragraph decodes "Gun Trey Rt Zoom Y Opt", Post-Whl, Go-Whip, Fly and "vs 5+". The 2-pt line now reads "2-pt after TD if: dn 2/5, up 1/5" (C-B5). |
| "radio down" | Calendar cell is now "booth: chart them, tell the sideline". |
| "tendency breaker" unlinked | Added to the You'll need box with a gloss. The first body use is linked. |
| "a quarterback who has played in the system" | Wolford is named in the text ("John Wolford, then a Rams quarterback"). |
| Paul Brown | Glossed as the founding coach of the Browns and the Bengals, sourced to his HOF page. |
| Correlation scale | Added "(0 would mean no carry-over at all ..., 1 a perfect repeat)". |
| Vignette question unanswered in the body | New paragraph in "What's on one" answers it: the first play was a test, and the look is worth more saved for third down. It also covers the box count and the RPO (C-B3). |
| Padded practices | Text now says "only about one practice a week in pads: fourteen ... in the whole regular season". |
| Blue/orange meaning | Caption says the colors mean higher/lower, not good/bad. |
| 3rd & 7+ man cell gets no comment | The third-and-long bullet now covers it with inline values (19% vs 30%). Pressure plus zone means fire zone (linked to 07-03), so the call is a quick zone beater, a screen, or a deeper beater only with full protection. Ties to the sheet's "vs 5+" line. Added an assert. |
| Fig 5 bill (2) count / floating badge (C-A3) | Bill (2) is rewritten as "the robber is gone ... a DB has replaced a linebacker". Badge 2 moved to the vacated middle, and the old SS spot is ghosted with a dashed outline. I did not add box shading, because the ghost plus the text tell it with less clutter. |
| SumerSports 60 vs 50 | Explained: 15-play team samples are noisy, so 60% is "a hint, not a finding". The duplicate "since 2007" is fixed. |
| "a touchdown or more" | Now "add up to 30 or 40 points, several touchdowns". |
| Wind game last line | Now: "Nothing was taken away that night; the whole plan was built around the weather". |
| Why 20 seconds | Added a reminder that the radio cuts off at 15 seconds (link to 01-04). |
| fig-game-week tiny text | Cell text goes from 5.3 to 6.3 pt with fewer words, and the figure is taller. The lane label no longer collides with the Monday cells. Coordinators' Friday adds special teams, and Saturday adds the game-management meeting (C-B7). |
| Matchup grid "RCB / star CB" | Column headers are now "CB / 2nd corner" and "CB / star corner". |
| Strip panel 4 (and C-B4) | Timing is realistic: X speed 7, throw at 2.35 s. Frame 4 is at 3.8 s with the ball arriving and X ringed red. The corner is about 4 yards deeper and inside, playing the post. The caption and note say why no middle help opens the comeback. The window is widened (-9 to 19.5 deep, 21.5 to the left) so FS, Q and X are not clipped. Tracking runs past the last route (`t_after=1.6`) so the ball lands. |
| Predict 3 Q/C overlap | QB moved to d = -2.3. |
| Predict 1 restates the vignette | Redesigned as "the second time". The defense substituted a nickel for the Sam and brought the SS down. The question asks what the offense learned and what it calls now. The answer covers the personnel conflict (run at the nickel), the size mismatch near the goal line, and tempo to trap the personnel. |
| Predict 2 gives the answer away | Removed the red ring and the "W still on Y" label. The remaining label is an observation ("M runs out with R"). The SS is moved to a middle robber spot (C-A7). The answer now teaches leverage (Y breaks out) and names the robber. |
| Predict 3 hedges | The answer leads with one best call (PA shot off the outside-zone look) and ties it to the sheet's SHOTS "when SS walks down" trigger (C-minor). The other options are listed as alternatives. |
| ESPN meta-note in the film room | Cut. A separate footnote `[^reidcards]` cites Henne/Childress, so each footnote is still referenced once. |
| "bill" motif | Trimmed in the strip caption and the pass-rusher paragraph. |
| XXV mentioned twice | The first mention is now "the Buffalo plan in the film room below". |
| Defensive week / DC script (gap, C-B6) | New paragraph: the defensive sheet is filed by situation x offensive personnel/formation, with an example box. DCs plan an opening series too. |
| Sizes | New: about 60 offensive plays a game in 2025 (inline course calculation, `[^snaps]`) against a sheet of a few hundred calls, and why. **Declined:** plays per install day, because I found no reliable source. |
| Worked scouting example | New worked example from data: Petzing's Arizona early-down PROE went from -7 (29th) in 2023 to +8 (1st) in 2025. The lesson: season averages follow the roster, and what travels lives on film. Inline values, assert, and footnotes `[^petzing]` and `[^proe]`. |
| Scout cards | One sentence on the poster-board card held up in the scout huddle. |
| Week 1 | Says what staffs do: the coordinator's old film, last year's tape, a simpler plan, and more weight on the script. |
| Final say | New paragraph: coordinators build and call their sides, and the head coach signs off and owns team decisions. |
| Lip-reading | Added to the Watch-for-it callout ("And on the sideline"). |
| Limits on scouting | One paragraph on Spygate (2007 penalties), sourced (`[^spygate]`). |
| C-A2 bracket leaves the out open | Changed to an in/out bracket. D is at (2.5, 7.3) outside Y, and the SS at (9.0, 4.6) is inside and over. In the strip D trails, and the caption and labels match. |
| C-A4 wide-9 stops outside zone | SDE is now a 7-technique ("7-tech on the TE: Y can't reach him"). The answer explains why a wide-9 would make outside zone easier (link 05-02). I kept the 3-technique tackle and said the Sam and the 3 load that side. A 5-technique would sit 0.2 yd from the 7-tech marker. |
| C-A7 the tell | Added a caution that zone teams also "bump" with motion, with a link to 06-06. |
| C-A8 Spot and Snag twice | The second line is now "Gun Trips Rt 60 Stick". |
| C-B1 sim pressure; post-snap coverage | Sim-pressure caveat added to the 2nd-and-long bullet (link 07-03). The coding caution now notes that coverage is post-snap and disguise isn't in the table. |
| C-B2 safety on the TE | Added to the Formation bullet, with a link to robber. |
| C-B5 missing boxes | Added BACKED UP, 4-MINUTE and SUDDEN CHANGE / after timeout boxes (the sheet now has 6 rows). (2) adds splits by personnel/formation and hash. |
| C-B8 field position | Added to "What a script is not" (backed-up alternatives). |
| C-B9 third downs in the first 15 | Added a downs 1-2-only check in the text (+0.002 vs +0.008, inline, with an assert). The main figure is unchanged, so the fact-checked numbers still stand. |
| C-B10 Baltimore | Now stated explicitly as a "who calls it" scouting question. |
| C-minor Belichick's Browns years | Now "as the Giants' defensive coordinator and then as head coach of the Browns and the Patriots", sourced to the PFR coach page. **Declined:** the "two down linemen" detail, because it is unverified. |
| C-minor "Ace" near Predict 3 | The answer names the SHOTS box by its trigger and avoids the play name. |
| C-minor kill call | Linked in (3), with a pointer to 01-05. |
| C-minor victory Monday | **Declined:** optional color, and the review also asked to cut drag. |
| Layout gaps (p. 2, p. 10, script-data page) | **Declined / not fixable here:** these are Typst float placement. The figures are too tall to fit the remaining space and get pushed to the next page. |
