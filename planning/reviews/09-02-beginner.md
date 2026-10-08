# Beginner review: 09-02 Kickoffs, Returns, and the Dynamic Kickoff

Reviewer role-play: a casual NFL watcher who has never played. I have read Parts 1-8 and 09-01 in curriculum
order. I know the field, EP/EPA from 01-02, the block vocabulary from 03-01 (and seal from 03-05), and
touchback, fair catch, muff, downing and return wall from 09-01. I read `pdfs/09-02-kickoffs-and-returns.pdf`
(18 pages, built 2026-10-08 01:40, after the last .qmd save) start to finish. I looked at every page at
60 dpi and at pp. 7-8 (Figs 4-5) at 110-130 dpi.

**Overall.** This is a strong chapter. The opening puzzle ("why would a coach prefer they *return* it?")
gets a real answer, Fig 1 and Fig 6 are the best data charts so far in Part 9, and the touchback-as-a-price
idea lands. Fig 2 (alignment plate plus its rules table), Fig 3 and Table 1 together let me work out the
drive start for nearly any kick. There are three main problems:

1. **Fig 5, the kick-to-tackle strip and the centrepiece of the "read a return as a run play" objective,
   is the hardest figure to read.** I could not find the seal, the lane or the kick-out in panels 3-4
   without the code.
2. **The "Why it exists" box claims "Nobody gets a running start" as the dynamic kickoff's innovation.**
   The chapter's own 2018 bullet already took the running start away.
3. **The 2025 and 2026 rule changes are listed but not explained.** The chapter never says why the league
   loosened the setup zone, why it allowed an onside kick "at any time", or who would use one when ahead.
   The spec asks for those reasons.

## (1) Terms used before they are explained, or never explained

- **"fair-catch kick"** (p1, "and the rare fair-catch kick"): this links to 10-04 with no gloss, and I have
  no idea what it is. 09-01 taught the fair catch, not a *kick* after one. Half a sentence would fix it:
  "a free kick a team may try after a fair catch, worth 3 points".
- **"setup zone" means two different things.** The 2018 bullet (p2) says "eight of the receiving team's
  players inside a 15-yard 'setup zone' near the ball". Two pages later the setup zone is "the five yards
  between the 35 and the 30". I read them as the same zone until the numbers disagreed. Either rename the
  2018 one or add "(a different zone from the one below)".
- **"downed" vs "kneel"**: "can be returned or downed for a touchback" (p5, Fig 3, Table 1) and "take a
  knee" (p10-11) mean the same thing here. But 09-01 taught "downing" as something the *kicking* team does
  to a punt. Say once: "on a kickoff the returner downs the ball by kneeling with it".
- **"live"** ("A kick that lands in the landing zone is live, and it must be returned"): I can guess, but
  "live" vs dead has not been defined for kicks. Does "live" mean the kicking team can recover it if the
  returner muffs it? The chapter never says.
- **"hang time"** is used on p7 ("his accuracy and hang time") and defined only on p9 ("That is the hang
  time of the kick").
- **"seal"**: "Before you start" (p1) says 03-01 "gave you the blocking words (double team, kick-out,
  seal, hat math)", but the text links seal to 03-05, and the 03-01 spec defers seal. Fix the attribution.
- **"point of attack"** (p8-9, "a double team at the point of attack") is not linked, unlike the other
  03-01 words.
- **"the three strips between the sidelines and the hash marks"** (p4-5, floater rule): "between the
  sidelines and the hash marks" reads as two strips. I had to work out that it means left of the left
  hash, between the hashes, and right of the right hash. Say that.
- **"UB"**: Fig 4 (left) has an unexplained orange square at about the receiving team's 14, below
  "returner at the goal line". Is it a second returner, or an up-back? Neither the caption nor the text
  mentions it.
- **"the offense's left"** (Fig 8 caption): the chapter never calls the kicking team "the offense". The
  helper docstring does, but readers don't see it. Write "the kicker's left".
- **The solid blue line at the kicking team's 35** in Figs 4, 8, 10 and 11 is gridiron's line-of-scrimmage
  marker, and it is never explained. A kickoff has no line of scrimmage, so I wondered whether it was a
  third restraining line.
- **"competition committee"** (p3) has no gloss. This is minor, since 09-01 also used it bare.
- **"bounce kick"** (p9) is introduced and never used again. Cut it or use it.
- **The EPA signs**: "a kickoff that was returned was worth, on average, +0.19 expected points to the
  receiving team, and a touchback +0.47" (p10). +0.19 compared with what? 01-02 taught EPA on a play from
  scrimmage. It never covered what the "before" value of a kickoff is. One clause would do: "measured
  against the value of the moment before the kick".

## (2) Leaps: a missing or assumed "why"

1. **"Nobody gets a running start" is presented as new.** The "Why it exists" box (p6) says: "The dynamic
   kickoff attacks ... **distance** and **speed**. Nobody gets a running start". The 2018 bullet (p2)
   already said "No running start (the coverage had to stand still, within a yard of the ball, until the
   kick)". The onside section (p12) repeats "the rule changes since 2018 had already taken away the running
   start". So what *did* 2024 add on speed? The answer is in the text but buried: the coverage starts 25
   yards downfield, five yards from the blockers. Rewrite the box around that.
2. **The kick-from-the-50 loophole existed in 2024, not just 2025.** Table 1, 2024 column: "the 30 / the
   25". Out of bounds (the 25) already beat a touchback (the 30) in 2024. The text says "In 2025 a team in
   that spot was better off kicking the ball out of bounds", so I ask why nobody did it in 2024. Either
   say it was there in 2024 too, or explain why it only came to light in 2025.
3. **Why is a ball that rolls into the end zone downed at the 20, not the 35?** The 20 is the key reward in
   Drill 1 and in the menu ("the best result a kicker can hope for"), but there is no "why". Presumably the
   league wanted to reward a kick that was returnable, and stop teams punishing a kicker whose kick landed
   in the landing zone. One sentence.
4. **The 2025 and 2026 setup-zone loosening (7+2, then 6+3, then 5+4) has no reason given.** What does a
   fourth floater let the return do? More double teams? Protection against squibs? This is a spec
   objective ("Explain the 2026 changes"), and the chapter only lists the numbers.
5. **Onside "at any time" (2026) has no purpose given.** The misconception box says it "only removes the
   requirement to be losing", which leaves me asking why the league bothered and who would use it. A tied
   team late? A team ahead by 1? A coach trying a gamble to open a half? Give one plausible scenario and the
   league's stated reason, if there is one.
6. **Troy Vincent's "under 5%" doesn't match the chapter's numbers.** p12 says recovery was 6% in 2024 and
   10% in 2025, then "a recovery rate under 5% might push the owners to 'revisit' the play". Neither season
   was under 5%, so what is he reacting to? Was the 2025 rate under 5% as of October 2025? Reconcile this,
   or explain it.
7. **"Three points a game, split between the two teams"** (p13). Both teams receive kickoffs, so a
   league-wide shift helps both equally and changes nobody's win chances. The paragraph then switches to
   team-vs-team gaps ("best kicking unit ... two yards below the league average") without saying that this
   is the part that matters. "Over a season that gap is worth more than a few field goals" also comes with
   no arithmetic. Show it: about 0.06 EP per yard × 5 yards × about 70 kickoffs ≈ 20 points.
8. **The EP per 5 yards changes from one page to the next.** 35 vs 30 is "about 0.2 points" (p10), but
   30 vs 25 is "about 0.3" (p13). It is fine if the curve flattens, but say so. Otherwise it reads as a
   contradiction.
9. **How does anyone know where the ball first hit?** The returner's whole decision "hinges on ... where
   the ball first hit the ground", and the chapter admits "the broadcast rarely explains" it. How does the
   returner know, mid-play? Does an official signal it? What happens if they disagree? And how do *I* tell
   from the couch? Is there a flag, a bean bag or a signal to watch for?
10. **Why the onside alignment is different** ("the kicking team lines up beside the ball ... much like
    the old kickoff"): the chapter gives no reason. I'd guess it is because otherwise the kicking team
    could not reach a 10-yard kick. Say it.
11. **The unblocked man's speed problem.** The safety pitch is that contact comes after a few yards. But
    the unblocked cover man and the kicker run 20-plus yards at full speed into the returner (Fig 5,
    panel 4). Is that collision measured? Is it why the kicker is "a safety with a kicking leg"?
12. **Hat math.** "Nine blockers in the setup zone, plus the second returner if it uses two: **ten**
    blockers at most" implies fewer with one returner. But with one returner, ten players stand in the
    setup zone, which is still ten. Say "always ten blockers". The glossary's "at least nine" leaves this
    open.
13. **"they are the ones the return cannot afford to block"** (p9) reads backwards at first. You mean
    "they are the ones the return has no blocker left for".
14. **The squib sentence**: "the receiving team often has a blocker in the setup zone or the second
    returner field it". This reads as the receiving *team's* choice. You mean the kicking team aims it so
    that a blocker has to field it.
15. **Drill 2 depends on clock rules the chapter never states.** Does a touchback take any time off? When
    does the clock start on a kickoff (at the catch? at the landing)? The answer asserts "the clock runs
    during the return" and defers to 10-04. I could only half-solve the drill (see 5).
16. **"Before 2024" in Fig 4 and the 2010 data point.** Fig 1's bottom panel shows 26.0 in 2010, but the
    text says "when the touchback was at the 20, drives after kickoffs started around the 22". I had to
    work out that 2010 was kicked from the 30. Add a half-clause.

## (3) Diagrams

- **Fig 5 (kick-to-tackle strip, p8) is the weakest figure and the one that matters most.**
  - Panels 1-2: the caption says "only the kicker and the two returners move", but the kicker is outside
    the window in both panels. I never see him move or where he is waiting.
  - Panels 3-4: a mass of pale trail lines, with about 20 unlabeled markers in a 2-yard band. I could not
    tell which orange square was the "seal" or which blue circle it was on. The "seal" label sits under
    a pair at the left-centre. The pale green double-team ellipse is nearly invisible at print size.
  - Panel 3: "lane" is written above a gap that does not look like a gap. The returner is 15 yards upfield
    with no arrow showing where he is heading, so the lane is not tied to his path.
  - Panel 3: "unblocked" is jammed against the left edge, over a half-hidden "40".
  - Panel 4: "the unblocked cover man and the kicker" sits several yards left of and below the two players
    it names. "kick-out" is at the far right, and I could not see which pair it marked.
  - The zoom shifts both depth and width between rows 1 and 2, and I lost track of left and right.
  - Fixes: label the key actors in panels 3-4 (S for the sealed man, D for the double team, KR2, C1, K).
    Draw the returner's remaining path as an arrow in panel 3. Darken the double-team outline. Put leader
    lines from the labels to the players. Fade or drop the trails for players who are already engaged.
- **Fig 4 (old vs new, p7)** is good overall, and the arrows tell the story.
  - The unexplained "UB" square (see 1).
  - Right panel: "contact here" sits at about the 27, above the shaded band, not in it.
  - The solid blue line at the kicker's 35 in both panels is unexplained.
- **Fig 3 (outcomes map, p5)**:
  - The out-of-bounds kick is drawn as a long diagonal ending in an X near the receiving team's 12 at the
    sideline. Its label, "out of bounds: ball at the 40", sits at the far left. Seeing the X near the 12
    and reading "the 40", I briefly thought the ball comes back to where it went out. Put the label next to
    the X: "out of bounds anywhere: ball at the 40".
  - Kicks start at the left edge with no tee drawn. That is fine, since the caption says so.
- **Fig 8 (onside, p12)**:
  - Every receiving player is labeled "H", but the caption says "The hands team's front line (H)".
  - "the offense's left" (see 1).
  - "must go 10 yards before the kicking team may touch it" sits at the bottom-left, over the yard number,
    away from the dotted 10-yard line it explains.
  - It isn't clear whether the hop's X (1 yard past the H front row) is the target or a typical landing.
- **Figs 10 and 11 (Drills 2-3)** are the same alignment plate with a different text box. They add nothing
  the drill text doesn't give.
  - The bold situation box overlaps the "40" number and the top blue dot (a collision).
  - Drill 3's figure shows only the deep-kick option, the one the reader should reject. Show the onside
    alignment next to it, or cut both figures to save a page. Pp. 15-16 are half empty.
- **Fig 6 (touchback math, p10)** is excellent. One gap: the "end zone" bucket mixes kicks that landed in
  the end zone with kicks that rolled in. The text says the difference is everything, so either split
  them or say in the caption which this bucket is.
- **Figs 1, 2 and 7** are clear and well captioned, and the Fig 2 table is a great idea. In Fig 1, the
  stepped labels with "→" are decodable but take a second look.

## (4) Drag and repetition

- **The Bears Week-1 double team appears three times**: the hat-math paragraph (p9, "exactly what coaches
  began doing in 2024"), the "Why it exists" box ("became the fashion within weeks of the 2024 opener") and
  its own Film room (p14). Keep the Film room and cut the other two to a phrase.
- **The kneel/run rule appears six times**: Fig 3 caption, Table 1, the returner section, Watch for it,
  Drill 1 answer and Takeaways. The repetition helps a little, but Fig 3's caption and the bullet list under
  "The returner's decision" say the same thing in almost the same words.
- **"Five yards apart" / "five yards from the blockers"** appears about eight times.
- **Film room: Seattle 2025** has a "What happened" that is two numbers and a Super Bowl field-goal record
  unrelated to kickoffs, and a "What to notice" that is the ledger homework again. It is the weakest box.
  Either give a concrete Seattle kick to watch, or merge it into the Fig 7 discussion.
- **The four `[^ringer]`/`[^ringer2]`/`[^grupe]`/`[^bears]` footnotes** cite the same Ringer article with
  overlapping text. The reader pays four footnotes for one source.

## (5) Can I do each "You'll be able to..." item?

| Objective | Verdict |
|---|---|
| Name every part on the broadcast; say where the next drive starts under 2024/25/26 | **Mostly yes.** Fig 2, Fig 3 and Table 1 work. I can't handle edge cases: a kick that lands in the landing zone and *then* goes out of bounds; a kick that lands in the end zone and bounces back into the field; a returner who catches at the 3 and retreats into the end zone (safety? touchback?); a muffed kickoff recovered by the kicking team. |
| Why the league kept changing it, from the injury data | **Yes.** The 5× concussion rate, 71 concussions in 2015-17 and −43% in 2024 are clear. The running-start confusion (2.1) muddies which change did what. |
| Touchback math: end zone / landing zone / squib; kneel or run | **Yes.** This is the chapter's best section. |
| Read a return as a run play: double team, seal, unblocked men | **Partly.** I understand it in words (hat math, 10 vs 11, pick who goes unblocked). I could not find these things in Fig 5 (see 3), so I doubt I'd find them on TV. |
| Onside kicks and the hands team under current rules; why surprise onsides are gone | **Yes**, apart from the "why any time?" gap (2.5). |
| Keep a field-position ledger and compare with league average | **Yes.** The checklist is concrete. |

**Predict-the-play, attempted before opening the answers:**

- **Drill 1 (kneel or run).** My answer: run it out, because it landed at the 4 so a knee only gets the 20.
  If it lands in the end zone on the fly, kneel for the 35. **Correct.** This was easy, which is right
  for the first drill.
- **Drill 2 (0:22, up 13-10).** My answer: no touchback (it gives them the 35 with all 22 seconds); kick
  deep into the landing zone or squib; never short or out of bounds. **Mostly right.** I missed the
  clock half of the answer, that the return itself burns 5-6 seconds while a touchback burns none. The
  chapter never told me when the clock starts on a kickoff, so I could not have reasoned it. The answer
  also says "two quick completions and it is in field-goal range" and "one timeout ... barely enough time
  for two plays". I accepted both on faith.
- **Drill 3 (down 8, 1:01, no timeouts).** My answer: declare the onside kick, because if you kick deep
  they run the clock out; expect the hands team; the chance is about 1 in 10. **Correct.** "Takes a knee
  three times" assumes I know kneeling keeps the clock running and that 40-second play clocks add up. That
  is fine from 01-01, but worth a clause. I wanted the answer to say what happens next if you recover: you
  still need a TD plus 2 in about 55 seconds with no timeouts, so the true win chance is far below 10%.
  That is the honest "why bother" number.

## (6) What I still wonder (the chapter should answer)

1. How do officials rule, and how do I tell from the couch, whether the ball landed in the end zone or
   rolled in? Is there a signal?
2. What happens on a muffed kickoff in the landing zone? Can the kicking team recover it, since the ball
   is "live"? 09-01 taught muff vs fumble for punts, and one sentence would carry it over.
3. Can the returner fair-catch a dynamic kickoff anywhere (the end zone? the landing zone?)? The chapter
   says only "no fair catches" where it lands.
4. What does a free kick after a safety look like under the dynamic rules? Kicked from the 20, so where do
   the coverage and the setup zone stand? The footnote says "same setup", but the coverage cannot stand on
   the receiving 40 if the kick is from the 20.
5. What is the penalty for an onside kick that was not declared?
6. Who actually plays on these units in 2025-26? Starters or backups? The chapter says "mostly backups",
   but it names no returner of the dynamic-kickoff era. Who are the dangerous returners teams squib away
   from?
7. How many kickoff-return touchdowns are there now, compared with before? The 2024 figure of seven is
   buried in a footnote.
8. Directional kicking: do kickers aim at one side (a "corner" kick, like the coffin corner in 09-01) to
   shrink the field for the return, and how close to the sideline do they dare go given out of bounds =
   the 40?
9. Why do the 2025 and 2026 alignment changes keep giving the return team more freedom? Is the league
   trying to push the return rate higher still?
10. Overtime kickoffs: are they the same rules?

---

## Revision (2026-10-08)

Revised against this review and `09-02-coach.md`; fact-check items kept. New rule claims are sourced to the 2026
rulebook text (Rule 6, 4-3-1, 10-2-1, 11-4-3, 11-5-1, 16-1); new data claims are course calculations in the
chapter's own cells. Renders cleanly (22 pp.); every figure page re-rasterized and inspected (60 and 100-220 dpi).

### Beginner findings

| Finding | Action |
|---|---|
| (1) "fair-catch kick" unglossed | Glossed inline: a field-goal try from the spot of a fair catch, worth three (Rule 11-4-3); glossary entry updated. |
| (1) "setup zone" means two things | The 2018 bullet now says "a 15-yard zone near the ball (the rules called it a setup zone too, but it is not today's setup zone)". |
| (1) "downed" vs "kneel" | New paragraph: on a kickoff the returner downs the ball by kneeling in the end zone; contrasted with 09-01's punt "downing". |
| (1) "live" undefined | Defined at first use: still in play, nobody's until possessed; the kicking team may recover once it lands in the landing zone (6-1-4); a ball left to rest is dead. Glossary "Landing zone" updated; "must be returned" softened to "field it" everywhere (text, table, Fig 3). |
| (1) "hang time" used before defined | Defined at the start of the kick-to-tackle section, before any use, together with the fact that it buys the coverage nothing. |
| (1) seal attributed to 03-01 | "Before you start" now credits 03-01 with double team, kick-out, lead block, point of attack, hat math, and 03-05 with the seal (also in Connections). |
| (1) "point of attack" unlinked | Linked to 03-01 and glossed at use ("the spot the return is aimed at"). |
| (1) "three strips" unclear | Spelled out: left of the left hash, between the hashes, right of the right hash. |
| (1) "UB" unexplained | Tagged "up back" in Fig 4 and named in the caption. |
| (1) "the offense's left" | Fig 8 caption now "the kicker's left". |
| (1) solid blue line at the 35 | Removed from every field (in-chapter `fix_field()` drops gridiron's LOS marker; a kickoff has none). |
| (1) "competition committee" | Glossed at first use. |
| (1) "bounce kick" used once | Now the alias of squib kick (glossary alias, used in the menu); the squib section explains today's version. |
| (1) EPA sign baseline | Added "measured, as EPA always is, against the value of the moment just before the kick". |
| (2.1) "Nobody gets a running start" presented as new | "Why it exists" rewritten around *distance*: 2018 took the running start; 2024 moved the coverage's starting line 25 yards downfield, five from the blockers. Takeaway reworded the same way. |
| (2.2) kick-from-50 loophole in 2024 | Text now reads across the row: the loophole existed in 2024 (25 vs 30) and 2025 doubled it to ten yards, when Dallas tried it. |
| (2.3) why the roll-in is the 20 | New bullet pair explaining the two touchback spots: the roll-in kick did what the rules ask, so the receiving team can't escape with the generous spot; otherwise kickers would stop aiming at the goal line. Also fixed the backwards "so that kneeling is not free" (coach A6). |
| (2.4) why loosen the setup zone | Added the league's stated aim ("improve safety and make returns more competitive", CBS, Mar 31 2026) and the mechanism: floaters can pick their man at the catch, so more of them means more choosers and more ways to build a double team. |
| (2.5) why onside "at any time" | New paragraph: no published reason found beyond the rule text; the option matters for tied teams, especially to open overtime, where a recovered kickoff uses up the receiving team's guaranteed possession (Rule 16-1-5(c)). |
| (2.6) Vincent's "under 5%" | Quoted exactly ("when you start getting a less than 5% recovery rate") and reconciled with a course calculation: 1 of 21 (4.8%) through Week 7 of 2025, when he spoke; Weeks 8-18 were kinder. |
| (2.7) "three points a game, split" | Rewritten: the league-wide shift helps both teams equally; what matters is the team-vs-team gap, now with arithmetic computed in the chapter (about 87 kickoffs × yards × points/yard: best unit ≈ +14, worst ≈ -16, ≈ 30 points apart). Watch-for-it per-game figure corrected to "more than half a point" with its arithmetic. |
| (2.8) EP per 5 yards changes | One fitted slope (≈0.07 points a yard, 20-40) is used throughout; a footnote explains why single raw 5-yard steps read 0.2 or 0.3. |
| (2.9) how anyone knows where it landed | Added: the returner is under it; in 2026 four officials stand on the goal line on kickoffs (Football Zebras, Sept 2026); from the couch, watch the bounce on replay and the returner's choice. Did not claim a signal or beanbag (none found in rulebook or mechanics sources). |
| (2.10) why the onside alignment differs | Explained: the target is ten yards from the tee and every kicking player must be behind the ball (6-1-6(d)), so players 25 yards downfield would be past it. |
| (2.11) unblocked man's speed | Added a paragraph: the two unblocked men still run 20-plus yards, so the play is not collision-free; the injury numbers cover the play as a whole; kicker prepared for contact (Tucker, ESPN 2024). |
| (2.12) hat math "at most ten" | Now "always ten blockers: everyone except the catcher", with both ways to get there. |
| (2.13) "cannot afford to block" reads backwards | Rewritten (with coach C3): the backside men are the ones the return chose not to block; coverage teaches them to pursue flat and stay behind the ball (lane integrity). |
| (2.14) squib sentence | Rewritten (with coach A5): the kicking team aims away from the dangerous returner; a ball touching a setup-zone player is now dead at the 40. |
| (2.15) Drill 2 clock rules | Clock rule stated in the returner section (4-3-1: clock starts when the ball is legally touched in the field of play; touchback takes no time) and used in the Drill 2 answer; "two quick completions" made concrete (15-20-yard sideline throws plus a timeout). |
| (2.16) 2010 data point | Fig 1 caption and text note 2010 was the last season kicked from the 30. |
| (3) Fig 5 strip | Rebuilt: kicker visible in panels 1-2 (window extended; tag "may not cross midfield yet"); zoom area drawn as a dashed box in panel 2 to anchor left/right; trails only for the five movers; key actors lettered on markers (S, D, D, KR, K) and named beside markers (R1, R2, R3); labels with leader lines to the players they name; returner's remaining path drawn as a dashed arrow through the lane; double-team outline darker and drawn over markers; every label ≥1.5 yd inside the window. |
| (3) Fig 4 | Up back tagged; LOS line removed; "contact here" now points into the shaded band with an arrow in both panels (no longer over the "20"). Left-panel arrows re-timed (coach). |
| (3) Fig 3 | OOB label sits next to the X: "out of bounds anywhere: ball at the 40"; "penalty" changed to "dead". |
| (3) Fig 8 | Only the hands team's front row is lettered H; "kicker's left"; the 10-yard label sits beside the dotted line with a pointer; the X is labelled "the hop comes down here". Alignment made legal (coach A4). |
| (3) Figs 10-11 add nothing / box collisions | Drill 2 now shows the kicker's four options A-D as kick paths, and the question asks which to choose; situation box moved clear of players and numbers. Drill 3 is now two panels: deep-kick vs declared-onside alignments. |
| (3) Fig 6 end-zone bucket mixes kinds | Caption says the bucket pools end-zone landings and roll-ins (play-by-play doesn't say which); the text's 9% figure says the same. |
| (4) Bears double team three times | Cut from the hat-math paragraph and the "Why it exists" box; kept in its Film room. |
| (4) kneel/run rule repeated | Fig 3 caption trimmed to the spots; the touchback-spot bullets carry the rule once. |
| (4) "five yards apart" repetition | Trimmed several instances (Why it exists, Fig 4 caption, panel notes). |
| (4) Seattle Film room weak | Box removed; Seattle's numbers folded into the Fig 7 discussion (the unrelated Super Bowl FG record dropped). |
| (4) four footnotes for one Ringer article | Now two: `[^ringer]` (full cite, Grupe) and `[^bears]` (short, pointing back). |
| (5) edge cases | New "Go deeper" box: landing zone then out of bounds; muff in the landing zone; catch-and-retreat safety (momentum exception); safety kick setup; overtime. |
| (5) Drill 3 "why bother" | Answer now says recovery is only step one: a TD plus two in under a minute with no timeouts, so the win chance is far below the recovery rate; kneel/clock clause added. |
| (6.1) landed vs rolled in, signal | See 2.9. |
| (6.2) muffed kickoff | Answered in text (live ball) and the edge-case box. |
| (6.3) fair catch on a dynamic kickoff | Answered: legal on a ball caught in the air (10-2-1), but it only ends the play at the spot, inside the 20, so nobody does. |
| (6.4) safety kick | Answered in the edge-case box (kicker at his 20, teammates still on the receiving 40; OOB/short = 30 yards from the kick). |
| (6.5) undeclared onside | Partly: the text now covers the reverse (declared then kicked deep = 15 yards, 6-1-6(k)); an undeclared short kick is simply a kick short of the landing zone (ball at the 40), which the outcomes map already shows. |
| (6.6) who plays / returners | Added the personnel shift (bigger blockers, tight ends, linebackers, defensive linemen; ESPN 2024, Steelers Depot) and the 2025 top returner average (~30 yards, Ray Davis; course calculation). Declined a list of named "dangerous returners": names age fast and the ledger is the skill. |
| (6.7) return TDs now vs then | Added from nflverse: 6 (2025), 7 (2024), 25 (2010). |
| (6.8) directional kicking | Added to menu item 2: the sideline as a twelfth defender, limited by out of bounds = the 40. |
| (6.9) why keep loosening | See 2.4. |
| (6.10) overtime | Edge-case box (same rules) and the onside-in-overtime paragraph. |

### Coach findings

| Finding | Action |
|---|---|
| A1 hang time gives no head start | Fixed everywhere: hang-time definition says it buys the coverage nothing; old-vs-new point 2; menu item 2; "why still kick to the end zone"; Madden box; Watch for it ("Did it bounce first? How deep was it caught?"); Saints film room. Added the causal paragraph after Fig 6 (fixed coverage start vs returner distance). |
| A2 double-team rule missing | Added (6-2-1(c)-(d)): only setup-zone players may double-team; wedges still banned. The sim's story stated legally (B4 + F3 double; KR2 takes F3's man). "Why it exists" reworded (restricted, now practical). "Combo" replaced by drive double team / "deuce". Bears film room notes the setup-zone requirement. |
| A3 illegal front line | Default front line now (-21, -10, 0, 10, 21); applies to Figs 2, 4, 5 and the drills. Gridiron numbers drawn 12 yd off the sideline are moved in-chapter to 8 yd so "outside the numbers" reads correctly (library untouched; flagged in notes). |
| A4 illegal onside alignment | Fixed to (-23.5, -20.5, -14, -9, -4, 4, 9, 14, 20.5, 23.5); kick-side arrows run past the 10 and converge on the X, C4 trails as scoop; hands front row at about 13 yards. Text adds the 6-1-6(k) penalty and the lean/holder rule. |
| A5 squib with old tactics | Glossary, menu and squib paragraph rewritten: first touch must be the ground inside the 20; aimed away from the dangerous returner; "first hits the ground short of the 20". Live for both teams; "field it or risk the coverage recovering it". |
| A6 smaller fixes | Touchback-high wording fixed; "penalty" → "dead" (Fig 3, caption, menu item 4); ten-in-setup-zone = six on the 35 tell added to text and Watch for it; EZ pooling stated. |
| B Fig 4 | Coverage arrows end at R(30), blockers at R(27); "contact here" moved; up back tagged. |
| B Fig 5 | (a) legal line; (b) tackle moved past the lane to about the 37 by the kicker, L5 a beat late, caption/tag updated; (c) R3/KR2 kick-out labelled; (d) blockers take a drop step and engage around their 33-34. |
| B Figs 10-11 | Box moved; see beginner (3). |
| C1 L5-R5 numbering | Coverage relabelled L5..L1, R1..R5 in the plate and text; return calls named by direction (Madden box). |
| C2 kicker is the returner's man | New hat-math bullet. |
| C3 backside pursuit | Rewritten (lane integrity). |
| C4 penalties | Added to "ceiling is low": holding/blocks in the back (10 yards), early movement 5 yards with possible re-kick (6-1-3, 6-3-1), and the 2026 four-across goal-line mechanics. |
| C5 personnel shift | Added (sourced). |
| C6 directional kicking | Added to menu item 2. |
| D Saints / Bears wording | Fixed (A1, A2). |
| E private gridiron calls | Left as is; docstring notes the fragility; flagged in notes. |
