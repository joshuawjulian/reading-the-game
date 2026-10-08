# 12-05 The Ravens' Option Run Game with Lamar Jackson (2019-2025): beginner-reader review

Reviewer role: a casual fan who has never played and has read only the chapters before this one in curriculum
order (Parts 1-11 and 12-01 to 12-04), including the prerequisites 03-04, 05-05 and 11-05. I read the .qmd start
to finish and looked at all 22 pages of `pdfs/12-05-ravens-lamar-run-game.pdf` (built 06:52, after the last .qmd
edit) at 60 dpi, plus pages 4, 6, 7, 8 and 19 at 130 dpi. I tried the three Predict-the-play drills before opening
the answers.

**Overall:** a strong case study. The "one front, two quarterbacks" plate (Fig 1) is the best single picture of
"count the quarterback" in the book, and the reader should not miss it. The three-era reading of the fingerprint
chart and the honest playoff section are what this reader came for. The 13-personnel "surprise" (Baltimore threw on
67% of its three-tight-end snaps) is a real "aha". The main problems, most important first:

1. **The playoff section contradicts its own numbers.** It says "the run game was rarely the reason", but two
   paragraphs earlier it reports designed-run EPA falling from **+0.08 to -0.02** in the playoffs. Its main
   evidence that deficits pushed the Ravens off the run is a fall in designed-run share from **46% to 41%**, and a
   data-minded reader will see that as small. The text also names the losses by **calendar year** ("the Chargers in
   2019 and the Titans in 2020"), while Fig 8 labels the games by **season**. On the chart, "2020 TEN" is a **win**.
2. **Fig 6 and the text give different 2022 pistol shares.** The bottom-left panel plots 2022 at about **33%** (NGS);
   the Monken bullet says "Pistol snaps fell from **26%** of plays in 2022" (FTN). The panel's big drop sits exactly on
   the "NGS | FTN" source line, so I could not tell whether the "pistol nearly disappeared" story is real or partly
   caused by the change of data source.
3. **The chapter never says why the Ravens left the pistol, the formation it sold so hard.** The pistol is sold for
   its "downhill back" and "no tell". Then for Henry, the most downhill back in the league, the Ravens moved **under
   center**, and the chapter's own data shows Henry did *better* from the pistol (7.8 yds, +0.21 EPA, n=92) than from
   under center. The text never explains this.
4. **In Drill 2, the picture and the answer disagree.** The answer says "every other box defender is blocked", but in
   the drill figure the Will and the Mike are untouched. Going by the picture, I answered "the Mike scraping over the
   top" and was marked wrong.
5. **The QB counter frame strip doesn't show the story it narrates.** The fake step and the linebackers "stepping
   with them" are under a yard of movement and can't be seen in panel 2, and in panels 3-4 the LG and R labels are
   buried under defender boxes.
6. **"Faced boxes about as heavy as anyone's"** is supported by 22% vs 21% for the league (eight or more in the box),
   which is league average. The hook ("crowds eight men... selling out") leads me to expect much more.

---

## 1. Terms used before they're explained, or never explained

| Where | Quote | Problem |
|---|---|---|
| 2018 section (l. 488-491) and "The rebuild worked" (l. 592) | "-0.02 EPA per play, slightly worse than an average snap"; "+0.11 EPA per play" | EPA is used twice before its gloss in the data section (l. 924-925). The You'll-need box mentions it, but a reader coming from search hits the number cold. Move the one-clause gloss to l. 489. |
| QB counter caption (Fig 4) | "the tight end **wraps** up through the hole" | In 03-03, *wrap* is a glossary alias for **log block** (`#gl-wrap` points to log block). Here it means "pulls around and leads up through the hole", which is a different action. Either say "leads up through the hole" or link it and say which sense is meant. Same problem at l. 731: "kick out or log". |
| Inverted-veer text (l. 731) | "the man the power play would normally kick out or **log**" | Fine for a reader who remembers 03-03, but there's no link. One link to `#gl-log-block` is enough. |
| Data section (l. 969) | "'successful'" | Success rate isn't re-glossed. Five words would do it: "(gained enough yards to stay on schedule)". It's owned by 01-02. |
| Answer 1 (l. 1108) | "the **big-nickel** and 'safety as linebacker' packages" | Not linked (owned by 02-05). It's the modern descendant of the seven-DB idea, so a link and a half-sentence gloss would pay off. |
| Fig 3 caption | "a base 4-3 with the **strong safety** walked down" | The drawn SS stands on the offense's *left*. That's the single-tight-end side, because Y and the H wing are both on the right. 02-05 taught me the strong safety goes to the strength. Either move him or say why he's on the weak side. |
| Fig 6 caption | "Next Gen Stats formation labels through 2022, FTN charting from 2023" | Every chapter mentions the source break, but here it *matters* (see item 2). Say what it does to the pistol line. |
| Fig 3, left panel | The brown dashed line from the backfield to the seam, and the thin dotted orange line from M to Y | Neither is in the "How to read the diagrams" key (l. 461-471). The brown line starts next to **R**, so it reads as the running back's route. It's actually the ball's flight from the quarterback's play-action spot. Add "dashed brown = the ball in the air" and "dotted orange = man coverage" to the key, or start the ball line visibly at Q. |
| Ring colours | "orange marks the defender to watch, purple a blocker to follow, and green follows the ball" | 10-02, which I just read, used **green = player to watch, purple = spy**. That's fine within this chapter, but it tripped me up for a moment. Consider aligning it, or at least don't use purple for a blocker in a chapter that also discusses spies. |

## 2. Leaps: a missing or assumed "why"

1. **Why under center for Henry, and not the pistol?** (l. 1311-1320.) The pistol section says the pistol's back is
   "seven yards deep and straight behind the ball, runs at the line with momentum, like a back in the I-formation".
   Then the Henry section says under center "lets him get the ball deep in the backfield, running forward". Both
   alignments are described the same way. What does under center give that the pistol doesn't? Possible answers:
   the quarterback's back turned to the defense on play-action, a deeper handoff point for wide zone, a QB who isn't a
   runner any more. And why give up the read game when Henry's pistol carries were the best ones? This is the
   biggest unanswered "why" in the chapter.
2. **"The run game was rarely the reason" (l. 1232) vs "designed runs went from +0.08 per play to -0.02" (l. 1218-1219).**
   The second number says the run game got clearly worse in the playoffs. The chapter needs to reconcile the two.
   For example: was the run EPA drop concentrated in the two games it names as "stuffed" (2018 LAC, 2019 TEN)? If the
   other games' runs were fine, show that, maybe as a per-game run-EPA dot in Fig 8.
3. **"Deficits pushed the Ravens out of their offense" rests on 46% → 41% designed runs** (l. 1228-1229, and again in
   Drill 3's answer). Five points is a small drop next to trailing-by-8+ going from 10% to 37%. I wanted the obvious
   check: what was the designed-run share *when not trailing* in the playoffs? If it was ~46%, the deficit
   explanation stands. If it was lower, the staff was abandoning the run on its own. Without that split the "trap"
   in Drill 3 is asserted rather than shown.
4. **"Playoff opponents are better... but the drop is bigger than either explains on its own"** (l. 1220-1221). This
   is a claim with no number. How big would we expect the drop to be against playoff-quality defenses? Compare the
   Ravens' regular-season EPA against playoff teams, or drop the sentence.
5. **Answer 3, Cover 0 (l. 1135-1149).** The section opens "If the box can't be made heavy enough to stop the run...
   send everyone", but Cover 0 then only attacks *dropbacks*. Does an all-out blitz also stop the run, or does it give
   up the run to win on passing downs? The Miami game is the example, but there's no result (score) and no
   mechanism; all of that lives in 10-02. One sentence on what the blitz did to the *run* plays that night would
   close the loop. "The quarterback is the man best equipped to punish it by running" also needs its why: in zero,
   every defender either rushes or has his back turned in man coverage, so nobody is left to tackle a scrambling
   quarterback.
6. **Answer 4, the spy (l. 1151-1158)**, is three sentences and a pointer. "The Lions did it in 2025 with a plan their
   coordinator credited not to the spy but to making every defender look the same" makes me ask "so did the spy
   work or not?", and the chapter doesn't say. Either give one result line per game or fold this into Answer 3.
7. **"The threat was doing the work the carries used to do... whether Jackson ran six times or four"** (l. 1281-1282).
   This is plausible but asserted. The chapter has the tools to test it (box counts, or Henry/RB run EPA vs Jackson's
   carries per game). Even one number would turn it from opinion into evidence.
8. **Why did heavy personnel jump to 86% in 2022?** (Fig 6 top right; l. 1041-1043.) It went from 53% in 2019 to
   86%, more than twice the league. Was that receiver injuries, or Roman doubling down? A phrase is enough.
9. **"A pattern repeated across six seasons, four lead running backs and three coordinators"** (l. 1244). Three
   coordinators? Only Roman and Monken are named. Mornhinweg (2018) appears only in a footnote URL. Also, l. 968 says
   "five different leading running backs" and l. 1244 says "four lead running backs". The spans differ, but I noticed
   and stopped to wonder which was right. Name them once (Ingram, Dobbins, Edwards, ..., Henry).
10. **Hook vs data.** The hook ("crowds eight men... selling out to stop the run") and the misconception callout
    ("faced boxes about as heavy as anyone's") suggest defenses loaded up against Baltimore far more than others did.
    The rendered numbers say **22% vs 21%**, which is ordinary. What defenses *did* do differently was base personnel
    (40% vs 27%). Reword it ("about as often as anyone else did") and say the interesting thing: defenses got bigger,
    not more numerous.
11. **13 personnel (l. 816):** "the answer defenses chose against these snaps about 77% of the time" is 77% of
    **57 snaps**. The footnote warns about this, but the body doesn't, and the reader builds a whole sideline decision
    on it.

## 3. Diagrams I couldn't decode, or captions that don't say what to notice

- **Fig 1 (one front, two QBs).** Excellent. One snag: in the *right* panel the green "keep" branch is drawn outside
  the 9 while the caption says the 9 "stays home", so I first read it as "Jackson keeps here". The caption says it's a
  branch, but a two-word label on the green arrow ("keep if he chases") would make it obvious. In the left panel the
  back's path goes nearly straight up and the X is at the 1, so I don't actually see a *cutback* being chased.
- **Fig 2 (pistol inverted veer).** The LG's pull path runs underneath the row of offensive markers and disappears.
  The "LG pulls for the Mike" label points at LG's starting spot, so I can't see the guard leading the quarterback
  through the hole, which is the whole point of the keep. The RG's climb to the *backside* Will also crosses the
  pull. Draw the pull a yard deeper (behind the line, under the QB) so it's visible.
- **Fig 3, left panel:** see §1 (brown ball line looks like R's route; the dotted man-coverage line isn't in the key).
  The FS arrow drifts right toward Y. Good, but the caption says "only the free safety behind him" without saying
  the FS is *late*, which is what makes the throw work.
- **Fig 4 (QB counter frame strip).**
  - Panel 2's note says "QB and back step left; the LBs step with them", but the QB moves less than a yard and the
    W and M barely move. In print the fake isn't visible, and the fake is the play's first reason (l. 883-886). Make
    the counter step and the linebackers' false step 1.5-2 yards so they show.
  - Panel 3: the "LG" label is hidden under the play-side 9's box (the kick-out contact). Panel 4: "R" is hidden under
    the backside 9's box, the one block the text says to count ("the back blocks the backside 9"). Offset the
    markers or ring R.
  - The caption says the Mike "first stepped the wrong way". His trail in panel 3 points *toward* the play.
- **Fig 8 (playoffs).** The x-labels are seasons ("2019 TEN") but the text uses calendar years ("Titans in 2020").
  There are *two* Titans games, and the one labelled 2020 is a win. Use the label form "2019 TEN (Jan 2020)", or
  write the text in seasons. "Three in four of the six losses" (l. 1227) is ambiguous: does it mean three or more
  turnovers in four of the six losses? Say it that way.
- **Drill 1 figure.** The prompt says "the defense walks a safety down", but every box defender is labelled 9, 5, 1,
  3, 5, 9, W, M, and no safety is visible in the box. Which one is the safety? Either label one box defender SS or
  drop the phrase. (The 8-in-the-box count still works.)
- **Drill 2 figure.** The squeezed 9 is drawn on top of the 5 and touching Y (marker collision), and his "short
  arrow" is mostly hidden by his ring. The LG pull is drawn as a line ending in a **block bar** behind RG, and the key
  says a bar means a block, so it reads as "LG blocks RG". Use the pull arrow style. Also see §5 on W and M.
- **Fig 7 (seven DBs).** Clear, nicely labelled. The caption is excellent.

## 4. Drag and repetition

- **The 2019 record line** ("3,296 rushing yards... 1,206... unanimous MVP") is the fourth time I've read it (02-01,
  03-04, 05-05, 10-01). It's fine here because this is its home, but the 02-01/10-01 film rooms are "earlier chapters
  have shown...", and the pistol film room (l. 904-918) spends its first paragraph listing them. Cut that paragraph
  to one sentence.
- **Numbers that disagree with 05-05.** 05-05 told me Jackson had **120** designed runs at **7.1** yds in 2019. This
  chapter says **113** at **7.4**. The sneak exclusion probably explains it, but a reader who remembers will think
  one of them is wrong. Add a footnote clause ("05-05's count includes short-yardage sneaks").
- **"The cost is the quarterback between the tackles"** is said three times (Why it exists; inverted veer "What does
  it cost?"; QB counter "the cost is the one the chapter keeps coming back to"). The third one admits it. Fine, but
  the first two could merge.
- The Answers to Drill 3 and the playoffs section repeat the 46%→41% argument almost word for word.
- Otherwise the pace is good. ~12,400 rendered words (including footnotes) for a ~5,000-word spec is long, but the
  body rarely drags.

## 5. Can I do the "You'll be able to..." items? Drills attempted before opening the answers

| Objective | Verdict |
|---|---|
| Explain the four pieces of Roman's 2019 design and what each solved | **Yes.** The numbered list (l. 523-569) is crisp, and each piece is tied to the Chargers game. |
| Count a Ravens run the way opponents had to, and say where the extra man must come from | **Yes.** Fig 1 nails it, and Drill 1 confirmed it. |
| Recognize the signature plays from the formation and the first step of the line | **Partly.** I can tell the power read from the QB counter by the pullers (the Watch-for-it bullet is good). From the *formation* alone I can't, because every play is pistol 12. And the QB counter's tell (QB and back step the wrong way) isn't visible in the strip. |
| Read the data fingerprint and say what changed under Monken and with Henry | **Mostly.** The three-era reading is clear. I can't fully trust the pistol panel across the NGS/FTN line (item 2), and I can't say *why* the Henry offense went under center. |
| Describe the defenses' answers and judge "can't win in the playoffs" with numbers | **Partly.** I can name the four answers, but only 1 and 2 are explained. 3 and 4 are pointers to 10-02. On the playoffs, the chapter's numbers (run EPA +0.08 → -0.02) undercut its own verdict, and I could argue either side. |

**Drill 1 (eight in the box).** My answer: 7 blockers (5 OL + U + Y); box 8 (six on the line, W, M); with Jackson
reading one end it's even, a hat on every hat. The extra man is the free safety. Invited play: "a read, probably
the inverted veer, since Fig 2 is this exact front; or play-action behind the safety." **Correct on the count and the
FS.** On the play I got half credit: the answer says "most of all a play-action pass at the deep middle", citing the
13-personnel seam (Fig 3, which has a third TE on the wing). The chapter spent two figures running the ball
successfully against this exact eight-man front, and says Baltimore faced 8+ boxes at a league-average rate and still
led the league. So "the play this picture is *begging* for is a pass" reads like the chapter changing its mind. Give
me a number (Ravens play-action EPA vs 8+ boxes) or soften it to "both, and that's the point". Also the "walked-down
safety" isn't in the picture (see §3).

**Drill 2 (read the 9).** My answer: **give**, since the 9 squeezed and took the keep away. For who tackles, I said
"the corner or the free safety, *or the Mike/Will scraping over the top*, because in the picture nobody is blocking
them." **Give is correct.** On the tackle, the answer says "Nobody in the box: every other box defender is blocked".
In the drill figure, W and M have no blocks on them: the RG's climb bar stops near the 3, and the LG pull hasn't
arrived. Either draw the RG's path to the Will and the LG's pull to the Mike, as in Fig 2, or soften the answer.
Otherwise a careful reader gets marked wrong for reading the picture.

**Drill 3 (down fourteen).** My answer: box 6 (5, 1, 3, 9, W, M; the NB is outside it) vs 6 blockers (5 OL + Y) plus
Jackson's read, so the offense is plus-one and the box says run. Down 14 in the third quarter is two scores with a
quarter and a half left, so stay with the run and call a zone read. **Correct.** But I came in from 10-01, which says
early-down passing is usually more efficient and the 2019 Ravens are the "exception every pass-more chart has to
answer". The answer leans on "the Ravens were the most efficient running team" and never compares the Ravens' *run*
EPA to their *own pass* EPA. That one comparison is what makes "keep running when behind" right or wrong for this team.

## 6. Knowledge gaps: what I still wonder

1. **Why did the pistol go away?** Was it Monken's preference, Jackson's development as a pocket passer, defenses
   solving the pistol reads, or Henry? The chapter's own Henry-from-pistol number argues against dropping it.
2. **Run vs pass EPA for the Ravens themselves, season by season.** Was their run better than their pass in 2019?
   In 2023? That's the number behind every "should they have kept running" question in the chapter.
3. **Did defenses actually play the Ravens differently over time?** Box counts and base-personnel share against
   Baltimore by season (2019 → 2025) would show the "how opponents responded" section in data rather than in
   anecdotes. Answer 1's claim that "big-nickel and safety-as-linebacker packages" spread through 2025 has no number.
4. **The 2020 Buffalo playoff loss.** Jackson left with a concussion in that game, which bears directly on the
   "honest" playoff accounting, and it isn't mentioned (only the dot on Fig 8).
5. **What did the Ravens' passing game look like in the Roman years?** "The passing game punishes the bigger, slower
   players" is said several times, but the only passing evidence is the 13-personnel seam figure. One number (play-
   action rate or EPA, 2019 vs league) would support the "Why it exists" box's second sentence.
6. **Injury cost.** The "trade is the quarterback's body". Did Jackson's designed-run volume relate to his December
   injuries in 2021 and 2022? The chapter raises the cost and then never measures it.
7. **The 2026 epilogue** says "what Doyle builds is a 2026 story". Fine for a closed era, but given today is October
   2026, one hedged clause on whether the 2026 Ravens look pistol, gun or under-center so far would satisfy the
   curiosity the chapter builds. Or say explicitly that the book doesn't cover 2026 results.

## Smaller notes

- l. 420-421: "Mark Ingram directly behind *him*, three yards deeper" agrees with the 4-yard / 7-yard pistol.
- l. 1101-1103 ("Jackson, eight games into his career as a starter"): he had started seven regular-season games
  (l. 492, "six of his seven starts"), so the playoff game was his eighth start. That's consistent but reads as
  "eight games into", so the reader has to do the arithmetic.
- Fig 5: the "13th" label for 2021 sits below the point and among the gray dots, so it's slightly hard to find. OK.
- Watch-for-it box is excellent and usable as written.

---

## Revision (2026-10-08)

Rebuilt `pdfs/12-05-ravens-lamar-run-game.pdf` (25 pages) and HTML with zero errors; every diagram page re-checked at
130 dpi. Fact-check results kept; every new claim is sourced (13 new footnotes, each referenced once; 48 total).

**Beginner review**

| Finding | Action |
|---|---|
| Top 1: playoff section contradicts its own run-EPA numbers; 46%→41% looks small; calendar vs season labels | Section rewritten. New per-game run-EPA diamonds on Fig 8 show the run lost value in the first four losses (LAC Jan '19, TEN Jan '20, BUF Jan '21, Huntley game) and gained it in the last two losses and all three wins; without the Jan 2019 and Jan 2020 games playoff runs averaged +0.06. "Rarely the reason" replaced by "failed early in the era, and not at the end". Added the by-score split: within one score the Ravens called designed runs on 47% of playoff snaps vs 45% in the regular season, so the overall fall comes from time spent trailing; added the two worst-deficit games' run shares (23%, 18%). Fig 8 x-labels are now opponent + game month ("TEN / Jan / '20"), and the text names every game by date, with a note on the season/calendar offset. "Three in four" now reads "three or more turnovers in 4 of the 6 losses". |
| Top 2 / Fig 6: pistol 2022 NGS 33% vs FTN 26% | FTN's own 2022 point added as a hollow diamond with a dashed like-for-like segment to 2023; caption explains the source break and that the drop survives it; Monken text gives "7%, down from 26% in 2022 counted the same way". |
| Top 3 / Leap 1 / Gap 1: why under center for Henry? | New sub-argument in the Henry section: what differs at the mesh (no QB in the back's track, shoulders square on zone/duo), play-action with the QB's back to the defense, Jackson now a passer first; Henry's under-center history (ESPN: most yards with QB under center 2019–23, 5,795) and Lewan's comment + Henry's reply. Also says what it gave up (the read), and warns that the pistol change-up's 92-carry number is flattered by selection. |
| Top 4 / Drill 2: picture vs answer (W and M unblocked) | Drill 2 figure now draws the RG's full climb to the Will and the LG's full pull to the Mike (pull style, not a stray bar); answer says each box defender has a blocker *assigned* and credits the Mike-over-the-top possibility as the reason a give isn't sure. |
| Top 5 / Fig 4: fake invisible; LG and R buried; Mike's trail wrong | Fake step 1.4 yd (QB) and 1.9 yd (RB); LB false steps ~1.9 yd at 3 yd/s, visible as faint trails in panel 2; Mike now steps left then comes back. Hole widened (Y's down block inside, kick-out outside, 9 fights outside) so LG, Y, U and Q never stack; R and the backside 9 offset. Panels retimed to 0 / 0.6 / 1.9 / 2.7 s so panel 4 shows U on the Mike with Jackson a step behind and outside. Panel-2 note no longer truncated. |
| Top 6 / Leap 10: "boxes about as heavy as anyone's" | Misconception callout rewritten: same 8+ box rate in 2019 (22% v 21%), but defenses got *bigger* (base 40% v 26%, held 36–40% v 23–26% through 2022); heavier boxes came later (30% and 33% in 2021–22 v ~23%), and the runs still ranked 13th and 2nd. |
| §1 EPA used before its gloss | Gloss + glossary link moved to the first use in the 2018 section; duplicate gloss in the data section removed. |
| §1 "wraps" / "log" | Caption and strip now say the tight end "turns up through the hole / leads up the hole"; "log" linked to `#gl-log-block` with a parenthetical definition. |
| §1 success rate | Linked to `#gl-success-rate` and glossed with 01-02's definition (positive EPA). |
| §1 big nickel | Linked to `#gl-big-nickel` with a half-sentence gloss and a pointer to 02-05; the unsourced "many defenses used against the Ravens through 2025" claim replaced by the data-backed point that opponents mostly got bigger. |
| §1 Fig 3 strong safety on the weak side | Kept the alignment and explained it in the caption: the Sam already covers the wing, so the SS balances the box on the other side. |
| §1 Fig 3 brown and dotted lines not in the key | "How to read the diagrams" now defines the dotted brown ball line and dotted orange man-coverage line; the QB's play-action set-up spot moved so the ball visibly leaves Q, not R; caption names both lines. |
| §1 ring colours vs 10-02 | Declined: colours are consistent within the chapter and the legend states them; the chapter has no spy diagram for purple to be confused with, and changing them would ripple through six figures. |
| Leap 2/3 | See Top 1. |
| Leap 4: "bigger than either explains" had no number | Added the league baseline (a typical playoff offense, 2018–24, was ~0.06 EPA/play worse in January; Baltimore fell 0.10) and Baltimore's regular-season EPA against playoff teams (+0.083 v +0.089 overall). |
| Leap 5: Cover 0 vs the run; why the QB punishes zero | Answer 3 now explains why zero is a gamble against a runner (nobody faces the QB), names rush lanes and the hug/green-dog rule (linked to 07-02), and gives the Miami result (22–10) and what happened to the runs that night (designed runs −0.14 EPA; Jackson 5 designed carries for 21 yds). |
| Leap 6: did the spy work? | Answer 4 gives a result line per game: KC 2024 won 27–20 but the runs were good (+0.26, Jackson 16 for 122); DET 2025 won 38–30 and the runs were held (−0.40, Jackson 7 for 35). |
| Leap 7: "the threat was doing the work" asserted | Softened to "likeliest reason ... some of the work" and backed with a number: non-QB designed runs +0.002 EPA in 2023, 5th, v league −0.08 (9th in 2022). |
| Leap 8: why 86% heavy in 2022 | Brown traded on draft night (April 2022) and Bateman's season-ending Lisfranc surgery (Nov 2022), sourced; personnel mix (22: 33%, 21: 25%, 12: 23%) checked and given in the footnote. |
| Leap 9: three coordinators / four vs five backs | Mornhinweg named in the 2018 section and the Roman paragraph; the five 2019–25 lead backs named in the data section; the four playoff-season lead backs and three coordinators named in the playoffs section. |
| Leap 11: 77% of 57 snaps | Body now says "about 77% of Baltimore's 57 such snaps ... a small sample, read every 13-personnel number here as a tendency". |
| Fig 1 green branch / cutback not visible | Right panel: green "keep, if he chases" label on the branch; caption says the green branch is what happens *if* he chases. Left panel: back's path now cuts back across the line (drawn above the markers), 9 chases to the X behind it, "cuts back" label. Also added the coach's "(or the backside linebacker)" note. |
| Fig 2 pull hidden; RG climb crosses it | Pull drawn ~1.5 yd deeper behind the line and the keep branch trails it; leader points at the visible pull path; RG climb no longer crosses. |
| Fig 3 FS "late" | Caption says the FS has to hold the middle against the fake and arrives late. |
| Fig 8 labels | See Top 1. |
| Drill 1 "walks a safety down" but no safety shown | Play-side edge defender relabelled SS (walked down outside Y), box shade widened to include him; answer counts him. |
| Drill 1 "begging for a pass" | Softened to "both, and that's the point": the box is even and the Ravens ran well against 8-man boxes, and it is also the look play-action is built for. (No 2019 play-action flag exists in nflverse, so no PA number.) |
| Drill 2 squeezed 9 collides with the 5/Y; arrow hidden; LG bar | 9 moved to (1.6, 5.6); squeeze arrow starts from his original side and ends outside the ring; LG drawn with a full pull. |
| Drill 3: compare the Ravens' run EPA to their own pass EPA | Answer now does it: 2019 dropbacks (+0.32) beat runs (+0.11), so it isn't automatic; what tips this snap is the light box (BAL runs +0.09 v 6-or-fewer, league −0.02) and the deficit (trailing 8+: runs +0.11, dropbacks +0.06, with a caveat about selection). |
| Drag: pistol film room's list of earlier chapters | Cut to one clause; the film room now names a specific game (SF at BAL, Dec 1 2019: 71% pistol, Jackson 16 designed runs for 101, 4th-and-1 conversion, Tucker 49-yd FG). |
| Drag: 120 @ 7.1 (05-05) vs 113 @ 7.4 | Footnote `[^lj]` explains 05-05 keeps the short-yardage sneaks. |
| Drag: "the cost" said three times | QB-counter version cut to one sentence pointing back to the "Why it exists" box. |
| Drag: Drill 3 answer repeats the playoff 46→41 argument | Answer now points to the figure and spends its space on the new run-v-pass comparison. |
| Gap 2: run v pass EPA by season | 2019 dropback EPA (+0.32, 1st) added after the rebuild paragraph, and used in Drill 3; 2024 dropback rank (1st) in the Henry section. |
| Gap 3: did defenses play Baltimore differently over time? | Base and 8+ box shares by season in the misconception callout and `[^box]` (2019–22 NGS; FTN-era box counts flagged as not comparable). |
| Gap 4: Buffalo Jan 2021 | Named in the playoffs section: 3–3 at half, down 10–3, end-zone INT returned 101 yds by Taron Johnson, Jackson's concussion two plays later, Huntley finished; sourced (AP, CBS) and checked against pbp. |
| Gap 5: passing in the Roman years | See Gap 2. |
| Gap 6: injury cost | Added: neither season-ending December injury came on a designed run (2021 ankle on a completed pass at CLE; 2022 knee on a sack v DEN, from pbp); Stanley's lost 2021 noted. |
| Gap 7: 2026 | Epilogue now says explicitly that the book stops at the 2025 season and turns the pistol/gun/under-center question into a viewing task. |
| Smaller: "eight games into his career" | Now "making only his eighth NFL start". |
| Smaller: Fig 5 "13th" label | Moved to the right of the 2021 point with a white backing. |

**Coach review**

| Finding | Action |
|---|---|
| A1 "gained EPA season after season" false for 2021 | "in every season but 2021". |
| A2 QB counter: RG reaching across C | Swapped per the review: C blocks back on the backside-shaded 1, the uncovered RG climbs to the Will; code comments updated, caption names the RG's climb. |
| A3 "pulling the tackle leaves the backside end free" | Rewritten: pulling the tackle leaves a second backside hole to fill; pulling the TE keeps the tackle home on the 5 and puts the better athlete on the second-puller job; the back takes the backside 9 as on any counter. |
| A4 Drill 3 "six underneath" | "two deep and five underneath (nickel, both linebackers, both corners, with four rushing)". |
| A5 calendar vs season | See beginner Top 1. |
| A6 Buffalo Jan 2021 omitted; "three in four"; Huntley game | See beginner Gap 4 and Top 1; Huntley game flagged in Fig 8 and the text. |
| B7 mesh behind the QB; "across his face" | Back routed through the QB's play-side hip in Fig 2 and Drill 2; caption and Drill 2 stem say "comes around his right hip". |
| B8 counter panels 3 and 4 | See beginner Top 5. |
| B9 seven-DB figure in 11 personnel | Redrawn in pistol 12 (U added, H dropped, both WRs off the line, NB as an overhang outside U); box label and text now "6 v 7 blockers + a read"; caption says why heavy sets are the point. |
| B10 Drill 1 safety | See beginner Drill 1. |
| B11 Fig 5 "13th" | Moved to the right. |
| B12 lone WR "split wide" | "off the line as a flanker"; diagram key states that omitted receivers stand off the line. |
| B13 (optional) Fig 1 backside LB | Added to the caption. |
| C14 LB keys and the counter | New paragraph: backfield-key LBs beaten by the counter step; guard-key LBs read the pullers correctly but are beaten by the half-second of mesh hesitation. Also softened "every linebacker follows a pulling guard" in the IV section. |
| C15 everyday answers | New subsection "The everyday answers": scrape/gap exchange (linked), mesh charge, make him pay, late safety rotation (linked to 12-08). |
| C16 Cover 0 hug/green-dog and rush lanes | See beginner Leap 5. |
| C17 who blocks the alley on the give | Fig 2 caption and IV text: play-side WR blocks the corner; the back's problem is the alley player (linked). |
| C18 the people up front | 2019 Pro Bowl line and FB (Stanley, Yanda, Ricard; Brown Jr. alternate), sourced to BaltimoreRavens.com; Stanley's 2021 loss added to the dip paragraph, sourced (CBS). |
| C19 Watch-for-it cues | "usually" for zone/zone read with the gap-run caveat; counter read/counter bash cue (back follows the pullers) added. |
| C20 box definition | "about 5–7 yards of the line". |
| C21 "under-center teams" contradiction | Reworded as a change-up for shotgun- or under-center-based offenses, as the Henry-era Ravens used it. |
| D film room with no game | Pistol film room now SF at BAL, December 1, 2019 (pbp-verified details). |
| D positive Henry film room | Added: PIT at BAL, January 11, 2025 (28–14, Henry 26 for 186, 64% designed runs, never trailed). |
| E 86% heavy sanity check | Checked against the 2022 personnel mix; real, and explained (see beginner Leap 8). |
| E FTN 2022 pistol marker | Added (see beginner Top 2). |

**Notes for the next pass:** the rendered prose grew to about 12,200 words (the spec says ~5,000; the beginner judged
the earlier ~12,400 including footnotes as not dragging). 10-02's spy film room says the Lions won "in Baltimore" in
Week 3 2025; nflverse confirms the game was in Baltimore (`2025_03_DET_BAL`, 38–30), so the two chapters agree.
`branch()` gained a `zorder` argument (chapter-local helper, not gridiron).
