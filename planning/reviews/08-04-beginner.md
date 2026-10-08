# 08-04 In-Game Adjustments, Tempo, and the Sideline Battle: beginner-reader review

Reader persona: casual NFL watcher, never played, has read 01-01 through 08-03 in order. Read the
qmd start to finish and looked at all 23 PDF pages (60 dpi, key figures re-rendered at 130-150 dpi).
Line numbers are qmd lines; "p." is the PDF page.

**Overall:** strong, readable chapter. The halftime-data section is the best part: clear question,
three tests, honest conclusion. The weak spots are (a) the spec'd before/after frame pair (Fig 9),
whose pictures don't show what the caption claims; (b) all three Predict-the-play drills are answered
before you reach them (by body text, on-figure labels or titles), and drill 1 is nearly the same as
02-01's Drill 3; (c) a few logic gaps in the score-effects/possessions argument and the SB LVII
"tired defense" line.

---

## 1. Terms used before they're explained, or never explained

| Where | Term | Problem |
|---|---|---|
| Fig 2 caption (l.673), tempo text, halftime section (l.1253), fn tempodata | **win probability 20-80% / above 90%** | Owned by 13-03 (later). No inline gloss and no link here. 01-02 glossed it once in passing, but that was 40+ chapters ago. Add "(each team's estimated chance of winning; 13-03)" on first use. |
| l.1254 | **garbage time** | Owned by 13-01 (later). Not glossed or linked. |
| Fig 11 caption (l.1321) | **"within two standard errors of zero"** | Not usable for this reader. Say it plainly: "small enough that coin-flip luck over 100-300 games produces gaps this big." Also fn halfdata. |
| l.1265, Fig 10 right "r = 0.01 (overall r = 0.40)" | **correlation / r** | The reader gets a number but no scale. Add one clause: "0 means no relationship, 1 means perfect." 02-06 used a correlation once, but never explained the scale. |
| Fig 15 (l.1522) | **"W" as a third tight end; "F"** | "W" is the Will linebacker in this chapter's key (l.503). Here it labels an offensive TE in a huddle. F (fullback) isn't in the key either. Relabel (e.g. "T3" or "Y2") and add F to the key. |
| Every field diagram | **orange line across the field** | It's the first-down marker. The "How to read the diagrams" key (l.500-507) doesn't mention it. In Fig 9 and Fig 14 it sits right where the "sitters" are, so you'd think it marks something about the coverage. |
| Fig 6 left | **dashed drop arrows with no shaded zone** | The key says dashed arrows are "zone drops (with a shaded zone)". The left panel has no shading, the right panel does. |
| l.729, l.961, takeaways | **three-and-out** | Never defined anywhere in the course so far (grep). Most fans know it, but it carries the chapter's main "cost of tempo" argument, so gloss it once. |
| Answer 1 (l.1471) | **"a simple count rule"** | "Count" (box count / leverage count) isn't connected back to where it was taught (05-05?). Link it or say "count the defenders near him". |
| l.496 You'll need | **success rate** | Listed as a prerequisite, but the chapter never uses it. Drop it. |

Terms owned by this chapter (tempo, hurry-up offense, sugar huddle, substitution freeze, halftime
adjustment, coaching booth) are all bolded, defined in the text and present in the glossary front matter. Good.

## 2. Leaps: a missing or assumed "why"

1. **Twelve men, two cases (l.746-749).** "if the offense snaps while a twelfth defender is still on
   the field, that is a five-yard penalty, and if he's still running off at the snap, the play goes on
   and the offense can keep the result or take the yards." What's the difference between "still on
   the field" and "still running off"? The reader can't tell why one stops the play and the other
   doesn't. Explain it in one sentence: 12 set in the formation means the whistle blows before the
   play; a player still leaving means the play runs and the offense gets a free play.
2. **Fatigue numbers vs your own chart (l.710).** "gets maybe 15 seconds to breathe instead of 30 or
   more". Fig 2 says even the fastest 2025 offense averaged ~34 s between running-clock snaps,
   which is ~28 s of rest after a 5-6 s play. The 15-second figure only holds for a true hurry-up. Say
   so, or the reader catches the text contradicting the chart.
3. **"Two forces you can see in @fig-coach-halves" (l.1344).** You can't see either force in Fig 11.
   Score effects need the lead-bin data, and Fig 11 doesn't show possessions at all. Then the number
   given is tiny: leading teams "were outscored by about **0.3 points**" in the second half (p.17).
   A 0.3-point effect can't explain Andy Reid's ~1.8-point drop. As written, the argument undercuts
   itself. Either show the bins, or explain how 0.3 per game becomes more for teams that lead often
   and by a lot.
4. **The possessions argument is at the wrong level (l.1352).** Possessions explain one game, like SB
   LVII. Over 100-300 games per coach, who receives the second-half kickoff should roughly even out,
   so it can't explain a coach's dot in Fig 11. Say which claim it supports. Also explain why
   "one team gets the ball first in the second half" matters (the coin-toss deferral). Nothing so far
   has taught that.
5. **SB LVII "a defense that had played a lot of snaps" (l.1420).** Which defense? Philadelphia's
   defense played only 20 first-half snaps. It was **Kansas City's** defense that was on the field
   for 44. As written it reads as if the Eagles' defense was tired, which the chapter's own Fig 12
   contradicts. Clarify or cut.
6. **SB LVII halftime length.** The chapter teaches "13 minutes" (l.607). Its main halftime example
   was a Super Bowl, where the halftime runs about twice as long (the footnote mentions this). The
   reader wonders whether the extra time mattered. One sentence would settle it.
7. **Fig 8 step 5, "one fewer defender near the box: run" (l.1111).** Why is there one fewer? The
   steps move a safety over X (step 4). Nothing explains where a box defender went. Say who left the
   box and why.
8. **Fig 3, lane 2 logic (p.7).** The snap marker says "snap can come here" at :32, then a long
   segment from :26 to :10 says "defense subbing now risks 12 on the field". If the snap already
   came at :32, what is that later segment? It reads as "the snap came, then the defense subbed".
   Fix: shade the whole lane after "set" as "snap can come any moment from here; a defense that
   subs risks 12 men", or show the snap at :32 as the end of the lane.
9. **Kelly, "And the league adjusted" (l.962-967).** No Kelly-specific evidence. "The tools they use are
   the next section", but the next section is generic. One concrete example of what defenses did
   against Kelly's Eagles (e.g. a simplified front, or how they played the bubble/RPO) would pay off
   the setup.
10. **Fig 6 left (p.11).** The caption explains the nickel, LDE, FS and SS. It doesn't say the Will
    drops (the solid-to-dashed arrow near W/M) or what the corners do. A beginner can't tell which of
    the two "A-gap threats" actually rushed. Also, "the quarterback's pre-snap read is wrong" assumes
    the 06-06 idea. Add "so he expects X and gets Y".
11. **"Under tempo" time budget.** Fig 6 says disguise needs "twenty seconds to set the picture".
    The text never says how long a defense actually has against a sugar huddle or a no-huddle snap.
    Fig 3 lets you infer ~8 s. Say it in the text: "maybe eight seconds instead of twenty".
12. **"Nothing about the call was wrong" (Fig 7 caption).** We never learn what the call was, so the
    reader can't judge that. Name it ("a quarters call with the nickel over H").

## 3. Diagrams I couldn't decode, or captions that don't say what to notice

- **Fig 9, before/after frame pairs (p.14). The biggest problem in the chapter.** At "First half:
  +1.6 s" the nickel ($) is about a yard and a half from H, upfield of him, and there's no visible
  "traffic". H labelled "open" doesn't look open. At "Second half: +1.6 s" the $ stands ~6 yards from
  any receiver on the left, and **both** crossers are converging on the SS. The panel doesn't
  show "each crosser runs straight into a waiting defender". If anything, the second-half picture
  looks *more* open than the first. The crossers have only just passed each other at 1.6 s. Use a
  later second frame (~2.1-2.4 s, when each crosser reaches the far sitter), or annotate the handoff
  ("$ takes Y, SS takes H"). Also, the first-half chasers need to visibly trail their men by a step.
- **Fig 7, tempo frame strip (p.12).** Panels 1-3 tell the story well: the $ is moving and inside
  H. Panel 4 doesn't. No throw line is drawn, the ball is a speck near the line of scrimmage, and the
  receiver trails all look alike. The reader can't see "throw on rhythm" or that H caught it. Draw
  the throw (the key promises "a dashed brown arrow a throw") and ring or label H.
- **Fig 6 left.** It's busy: dashed rings, a purple ring and six arrows all in the middle. At print
  size the M rush arrow and the W drop are hard to separate. Consider labelling "rushes" and "drops"
  on the two A-gap threats.
- **Fig 11 (p.17).** Dot size isn't explained. Presumably it's games coached; say so. The caption is
  long (six sentences) and the "two standard errors" clause will lose this reader (see §1).
- **Fig 15 (p.21).** The huddle reads well. Apart from the W label clash, the "base defense still
  on; short-yardage group on the sideline" note floats over the FS/deep area, far from anything it
  refers to.
- **Fig 13 (Predict 1).** The labels "U: nobody within 6 yards" / "Y: nobody within 6 yards" give the
  answer away (see §5).
- Good: Fig 1 (adjustment loop and halftime bar), Fig 2 (tempo by team; the "within 30 s" column is a
  nice touch), Fig 4 (freeze), Fig 5 (history), Fig 10 left (regression; the diagonal makes it
  obvious), Fig 12 (SB LVII).
- **Print "Go deeper" box (p.15):** "The code below sketches that". In the PDF there is no code below
  (the eval: false cell isn't shown). Reword for print, or say "in the online version".

## 4. Drag / repetition

- **The freeze is taught a fifth time, and the reader already did this drill.** 02-01 explained
  substitution matching, the umpire hold, "not substituting is a weapon", and had a predict drill
  (Drill 3: 12 personnel vs base, TEs split off the ball, no huddle, "a pass, probably to a tight
  end"). 08-04 then covers the rule in prose (l.734-751), in Fig 3, in the "Why it exists: the matching rule"
  callout (which restates 02-01's "offense chooses first" callout), in Fig 4, and in **Predict 1, which
  is essentially 02-01's Drill 3 again**. Cut the rule restatement to two sentences plus "you met
  this in 02-01". Make Predict 1 something new: a defense that pre-empts by subbing at the whistle,
  a like-for-like swap that triggers the umpire hold, or a timeout decision.
- **"No new plays" is made three times.** The chef analogy (l.515), the "Madden vs. real life" callout
  (l.596-602) and the halftime paragraph (l.628-630) make the same point. Keep one or two.
- **History section.** The Wyche anecdote (l.873-883) is fun but long for a point ("the league once
  nearly banned the no-huddle"). The Manning/Patriots paragraph (l.901-908) is a run of records
  (606 points, 1,191 plays) that don't connect to the chapter's argument.
- **Print layout.** Large blank half-pages on p.4, 6, 15, 16, 17, 18, 20 (figures pushed to the next
  page). It isn't the prose, but it makes the PDF feel padded.

## 5. Can I do the "You'll be able to..." items? Drills attempted before opening the answers

- **Describe what a staff can change between series and at halftime:** yes. Fig 1 and the
  bullet list make this concrete.
- **Tell tempo, hurry-up and no-huddle apart; explain the matching rule and the freeze:** yes. The
  three-bullet distinction (l.656-659) and the Washington example (no huddle, still slow) are
  excellent. The 12-men nuance is still hazy (§2.1).
- **Explain the sugar huddle and spot it:** mostly. I'd look for a huddle 4-5 yards back and a fast
  snap. I'm not sure I'd tell it apart from a team that just huddles a bit closer than usual. Say how
  fast "fast" is (Fig 3 implies a snap with about :30 left).
- **Name the defense's answers and what each costs:** partly. The objective asks for costs. The cost
  of simplified calls is clear (no disguise). The cost of rule-based checks gets one clause
  ("players must be smart"). The cost of versatile personnel isn't given at all: what does a hybrid
  safety-linebacker give up? Size against the run? Coverage skill? Also missing is the pre-emptive
  answer 02-01 taught: sub at the whistle, before the offense gets set.
- **Follow a call-after-the-call sequence:** on paper, yes (Fig 8). On TV, I doubt it. Fig 8 is
  seven text boxes with no field picture, and the one field example (Fig 9) doesn't read (§3).
- **Judge a halftime-adjustment claim:** yes, for regression to the mean, and this section is the
  highlight. Score effects and possessions are shakier (§2.3-2.4).

**Drill attempts (before opening the answers):**

- **Predict 1:** "Snap right now and throw to a tight end. The labels say nobody is within 6 yards
  of U or Y, and the linebackers stayed inside." Matches the answer, but too easily: the figure's
  labels give it away, and I did this exact drill in 02-01. I didn't come up with the second
  paragraph's "if the linebackers widen, run" branch. That part is good teaching, and the drill
  should *ask* for it ("what if S and W walk out?").
- **Predict 2:** "A route that breaks back against the sitting defenders (a pivot/whip), or a crosser
  that climbs behind them." Matches the answer, but only because the paragraph right after Fig 9
  (l.1215-1219) spells it out ("pivot or whip route ... That is the next call after the call, and
  you'll get to make it in the drills"). Without that paragraph I would probably have said "throw
  deep over them" or "run mesh again, deeper". Move that paragraph after the drill, or cut it to
  "the adjustment gave something away; you'll find it in the drills".
- **Predict 3:** "Sugar huddle; snap fast before the short-yardage package arrives; a QB sneak or
  an inside run." Matches. But the title ("the quick huddle on fourth down") plus the body text
  ("especially useful for ... a fourth-and-short", l.859) make this recall, not prediction. Better:
  leave the situation ambiguous, or ask what the defense should do (timeout or not) and what each
  choice costs.

## 6. Knowledge gaps: what I still wonder

1. **Does tempo actually work?** The chapter measures how fast teams go, but never whether fast snaps
   gain more. Compare EPA or success rate for no-huddle vs huddle snaps, or for snaps within 30 s
   vs the rest (with the obvious caveat about selection). This is the question a beginner asks
   first, and the data is already loaded.
2. **If tempo works, why did it disappear?** Fig 2 shows one fast team in 2025. Why did the league
   go slow after Kelly: fatigue for its own defense, motion-heavy offenses that need the clock,
   radio/wristbands? A paragraph would close the loop between the history and Fig 2.
3. **Do defenses get caught with 12 men, or burn timeouts, more often against tempo?** Some evidence
   that the freeze bites would help.
4. How does the defense know the offense *didn't* substitute? Who watches the offensive sideline,
   and how fast?
5. The booth-to-sideline radio: the chapter says the 15-second cut-off applies to the coach-to-player
   radio. Does the defense's green-dot radio get cut at the same time? Is that why tempo hurts the
   defense's call more than the offense's?
6. Who receives the second-half kickoff, and does deferring matter for the "possessions" argument?
7. Do offenses or defenses make the bigger halftime changes? The data treats offense EPA. Does a
   defensive split look any different?
8. In SB LVII, what did *Philadelphia* change, or fail to change, in the second half?

---

## Revision (2026-10-08): finding -> action

Covers both this review and `08-04-coach.md` (C# = coach item number). Fact-check claims were left intact;
removed claims (606 points, 1,191 plays, 50 rushes) were cut for drag, not accuracy. Every new factual claim is
sourced (new notes: `[^dlsnaps]`, `[^replay]`, `[^tmm]`, `[^tempowork]`, `[^pffmotion]`, `[^defer]`) or is a course
calculation guarded by an assert. Renders clean (26 pages); every diagram page re-rasterized and looked at.

**§1 Terms**
- Win probability 20-80% / 90%: glossed inline and linked (glossary + 13-03) at first use in the halftime section; the tempo
  footnote already explains the filter.
- Garbage time: glossed and linked to `gl-garbage-time-filter` (13-01).
- "Within two standard errors": cut from the Fig 12 caption; the text now explains it in plain words ("wobbles by about a
  point either way from luck alone") and counts the coaches inside the band.
- Correlation / r: one-clause scale added ("0 means ... nothing, 1 means everything").
- "W" as third TE / F: relabelled V; F and V added to the diagram key (also C5).
- Orange line: key now names the blue line (scrimmage) and orange line (line to gain).
- Dashed drops without shading (Fig 6 left): every drop in that panel now has a shaded zone; key says "usually".
- Three-and-out: glossed at first use.
- "Count rule" (old Answer 1): Answer 1 replaced (see §4), so the phrase is gone.
- Success rate unused: kept in "You'll need" because the new "Does tempo work?" section now uses it.

**§2 Leaps**
1. Twelve men: rewritten as two clear cases (12 in formation with the snap imminent = dead ball, five yards; a 12th still
   leaving at the snap = live-ball foul, "free play"), matching the fact-check's Rule 5-1-1 reading (also C3). Added data
   that the threat is real: ~25 defensive too-many-men fouls a season, ~4x as common on no-huddle snaps (2016-2025).
2. Fatigue vs chart: rewritten. Normal pace = 30+ s of rest (even NO's 34 s average is ~28 s rest); only a true hurry-up
   (20-25 s snap to snap) cuts it to 15-20 s. Added the DL-rotation mechanism with 2025 snap-count data (C6).
3. "Two forces you can see": replaced. New computation shows score effects are small in points (halftime leaders give back
   ~0.7 pts vs what their quality predicts; at most ~0.2 pts on any coach's dot), so the section now says the coach dots
   are mostly chance, score effects are real but small (new Fig 13 shows the bins against a quality prediction), and
   possessions explain single games. The old 0.3-point "mirror" sentence is gone (also C10).
4. Possessions at the wrong level: now explicitly "for single games", with the deferral explained and linked to 01-01
   (source reused from 01-01); "evens out over 100+ games, so not a coach's dot".
5. SB LVII "tired defense": fixed. Text now says the Eagles' defense couldn't get a stop and that KC's defense was the one
   on the field for 44 first-half plays.
6. SB halftime length: one clause added (a Super Bowl halftime gives a staff far more than 13 minutes); the conclusion
   (re-ranking, not new plays) still holds.
7. Fig 9 step 5: box and caption now say why the box is light (three defenders spread over trips, a safety committed to X).
8. Fig 3 lane 2: redrawn. "Earliest snap" marker when the offense is set, then one shaded band to the end of the clock:
   "from here on the snap can come at any moment / a defense that swaps players now risks 12 men". Caption rewritten.
9. Kelly "and the league adjusted": **partly declined.** I found no verifiable Kelly-specific account of a defensive
   counter, so I did not invent one. The sentence now says "the offense itself faded" and makes the concrete, checkable
   point (by year three every opponent had a season of film on the same few plays), then hands off to the general tools.
10. Fig 6 left: football fixed (C4) and caption rewritten to say what each player does, including "the QB expects a
    two-high, six-man picture and gets a one-high, five-man play". Labels "M rushes" / "W drops" added on the threats.
11. Time budget: stated in text ("maybe eight seconds instead of twenty") in the freeze and defense sections.
12. "Nothing about the call was wrong": caption now names the call (two-high nickel, quarters, nickel over H).

**§3 Diagrams**
- Fig 10 frame pairs (also C1, C2): rebuilt. Real mesh depths (H ~5 yd, Y a yard deeper, crossing over the ball); man
  chasers on explicit trail paths a step or two behind (no zig-zag); Mike through the right B gap (no longer on the RDT);
  second frame moved to +2.3 s; second-half sitters placed on each crosser's track at 5-6 yd, with "$ takes Y" /
  "SS takes H" leaders; first-half throw drawn to the open H. Text/caption say "five to six yards".
- Fig 7 strip: the throw is now drawn (dashed brown arrow, brown ring on the target) via a new chapter helper in `panel()`;
  last frame moved to +1.4 s so the ball arrives; RCB backpedals and SS/FS shuffle (C15).
- Fig 6 busy left panel: labels added; tackles moved so the M/W boxes no longer touch the T.
- Fig 12 dot size: caption says bigger dots = more games; caption shortened.
- Fig 15/17 (sugar huddle): huddle now centred ~5 yd back and tight; defense note moved next to the base defenders.
- Fig 13 (old predict-freeze) label giveaways: drill replaced (below).
- Print "code below": reworded to "the online version includes a short code sketch".

**§4 Drag**
- Freeze taught five times: matching-rule prose cut to two sentences plus "you met this in 02-01"; the "Why it exists"
  callout now only adds what 02-01 didn't (the freeze as the bargain in reverse, the 2025 procedures). Predict 1 replaced
  with a new drill: a one-for-one substitution during a hurry-up (any substitution opens the umpire hold, so the offense
  ends up 11 vs nickel), contrasted with Fig 4.
- "No new plays" three times: the halftime restatement cut to one sentence; chef analogy and Madden callout kept.
- History: Wyche anecdote trimmed; the 606-point / 1,191-play records cut (and their notes).
- Blank half-pages: tall figures shortened (Figs 2, 4, 5, 11, 12); a few float gaps remain where Typst pushes a figure.

**§5 Drills**
- Predict 1: new (see above); the answer also covers "what if the defense doesn't sub".
- Predict 2: the paragraph after Fig 10 no longer gives the answer (it now says only that the fix gave something away).
  Answer adds the RB wheel/rail (C19).
- Predict 3: retitled neutrally ("no waiting"); body text no longer says "fourth-and-short"; the question now also asks
  the reader to play defensive coordinator (timeout or not, and the cost of each), answered in the callout.
- Objectives: sugar huddle "how fast" now stated (snap with 25-30 s left vs ~5); costs given for every defensive answer
  (substitute first, rule-based checks, versatile personnel); pre-emptive subbing added from 02-01.

**§6 Knowledge gaps**
1. Does tempo work? New section and Fig 8: fast snaps +0.053 vs +0.011 EPA raw; same down & distance edge ~+0.03 EPA and
   +1.7 pts success rate, with the selection caveat.
2. Why did it fade? Same section: league share of fast/no-huddle snaps by season (peak 2014-15), with three reasons, the
   motion one sourced (PFF 37.6% -> 63.9%).
3. 12-men evidence: added (see §2.1).
4. Who watches the offensive sideline: one clause (the personnel caller, linking back to 02-01).
5. Green-dot radio: stated that it cuts at 15 s like the QB's (per 01-04).
6. Deferral: answered (§2.4).
7. Offense vs defense halftime changes: already answered by the offense/defense persistence numbers; left as is.
8. What did Philadelphia change: added (PHI offense was *better* after halftime, 28 plays, EPA +0.10 -> +0.22; the defense
   got no stops; PHI's league-leading 70 sacks and zero in the game, C16).

**Coach items not covered above**
- C7 injuries: new halftime-list bullet ("Re-planning around injuries").
- C8 equity rule headsets: added, with the footnote extended (same NFL Ops source; 01-04 cites it for the radios).
- C9 Kelly "one personnel group": softened to "a small number of formations and personnel groups". **Declined** to quote a
  12-personnel share: nflverse participation data starts in 2016, so I couldn't verify a number.
- C11 sugar huddle / Wyche: linked descriptively ("what today would be called a sugar huddle") rather than claiming Wyche
  coined the term, which I could not verify.
- C12 tempo vs replay: new fifth "why go fast" item, sourced (`[^replay]`), linked to 09-04.
- C13 officials as the speed limit: added with data (only 1 in 20 no-huddle snaps within 21 s of the last; ~15 s tackle to
  snap).
- C14 "look to the sideline": named next to Washington's number.
- C16 SB LVII possessions: KC received the second-half kickoff and scored (nflverse kickoff rows); 0 sacks noted.
- C17, C18: the drill they refer to was replaced.
- C20 which coordinator sits upstairs: **declined.** I found no reliable league-wide count, so the text stays "varies by team".
