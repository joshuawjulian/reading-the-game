# 02-01 Personnel: beginner-reader review

Reviewer role: a casual NFL watcher who has never played. I have read only Part 1: 01-01 (field, clock, play clock),
01-02 (downs, LOS, EPA, success rate, red zone, baseline guessing), 01-03 (every position, X/Z/slot, Mike/Will/Sam,
nickel back `$`, eligible receivers, 50–79 and reporting, the 11-vs-nickel picture), 01-04 (forty seconds,
personnel goes in first, radio cut-off at :15, no-huddle and the umpire substitution rule), 01-05 (set/motion, fouls,
counting the box) and 01-06 (broadcast, All-22, stance tells, under center/gun pass rates, prediction log).
Source: `chapters/02-personnel-and-formations/02-01-personnel-groupings.qmd` (line numbers are qmd lines) and
`pdfs/02-01-personnel-groupings.pdf` (19 pages, read at 60 and 130 dpi).
Length: about 7,500 words of prose before footnotes. The spec target is about 4,000.

Overall: this is a strong chapter. The two-digit rule, the "who, not where" idea, the substitution strip and the
two-tight-end dilemma all landed, and I could do every drill. The problems are the jumbo arithmetic, a few promises
the chapter makes but doesn't keep, a contradiction with 01-04, several small diagram faults, and length and
repetition.

---

## 0. The five biggest problems

1. **Jumbo breaks the formula I was just taught, and nobody says so.** l.203 says "Wide receivers = 5 − backs −
   tight ends", and the Takeaways repeat it. Then Fig. 3 (jumbo) shows six linemen, 2 TE, 1 RB and **1** WR, and
   l.399–401 says the data calls this "12". By the formula, 12 means **two** receivers. I stopped and recounted
   twice. One sentence is needed: "with a sixth lineman the formula is 4 − backs − tight ends: jumbo takes one of the
   five skill spots." The answer to "is it 12 or 13?" (l.400–401) should be pinned to that rule.
2. **The hook is never paid off.** l.157–158: "someone near the defensive bench is shouting a single word." What
   word? Who is shouting it? Is there a defensive coach whose job is to call the personnel? I never find out. The
   hook also has the offense swap **two** players (two WR off, a TE and a FB on, l.155–156) while the defense swaps
   **one** (a CB off, a LB on). That contradicts the one-for-one rule at l.451–452 ("Add a receiver, add a defensive
   back. Add a tight end, add a linebacker"). The 2025 chart agrees with the hook, not the rule: against 22, defenses
   still played four DBs 76% of the time. Why do defenses almost never drop below four DBs? (Presumably two corners
   and two safeties are a floor for deep coverage.) Without that "why", the matching rule I was taught predicts the
   wrong thing on the chapter's own opening play.
3. **It contradicts 01-04 on where the umpire stands.** 01-04 l.817 says the umpire is "the official who stands
   among the defenders". 02-01 l.614–615 says he "normally stands in the offensive backfield behind the running
   back", and Fig. 4 draws him there. 02-01 is right (footnote: since 2010), so 01-04 needs fixing. Until it is, a
   reader who has read both chapters gets two answers.
4. **The chapter makes promises the data on the page doesn't show.**
   - The section title is "the rise, and the turn, of 11" (l.925), but the chart starts in 2016 and the 11 line is
     flat. The rise happens off-chart ("had happened earlier, over the 2000s", l.961). Either add a pre-2016 data
     point or anchor (even one NGS or Sharp figure in the text), or retitle.
   - "Why personnel is the first clue" (l.743) then "11 leans slightly pass, 12 is a coin flip" (l.1132) leaves me
     asking: **how much does personnel add to what down and distance already told me?** 01-02/01-06 gave me a
     situation-only baseline. A single number would settle it, for example: "the down/distance guess alone gets X%;
     add personnel and you get Y%." As written, I can't tell if personnel is worth my attention on 11/12 snaps,
     which are 83% of plays.
   - "22 and jumbo are strong run" (l.1132): 22 is 36% pass, so 64/36. Calling that "strong" while 11's 56/44 is a
     "nudge" is fair in relative terms, but the Watch-for-it bullet should give the numbers so I calibrate my log.
5. **Too long, and it repeats Part 1.** About 7,500 words against a 4,000 target. The substitution-rule material
   (umpire over the ball, twelve men, five yards, no-huddle freezes the defense) was already taught in 01-04
   l.816–826. Here it appears **five more times**: l.623–639, l.1137–1138 (Watch for it), Drill 3 setup, Drill 3
   answer l.1246–1250 and the Takeaways. "A linebacker can't cover a slot receiver" was the climax of 01-03
   l.849–854 and comes back at l.610–612 and l.736–737. The NGS→FTN source caveat appears four times (Fig. 9
   caption, Go deeper box, `[^ngs2]`, `[^data]`). Saying "you met this rule in What a Play Really Is; here is why it
   matters for personnel" would cut a page and read as building on Part 1, not restarting.

---

## 1. Terms used before they are explained, or never explained

| Where | Quote | Problem |
|---|---|---|
| l.746 | "situation → personnel → formation → motion → **the defense's box and shell** → prediction" | "Shell" is never defined. 01-05 l.1013 explicitly deferred shells to Part 2, and 02-05 comes later. The clue-clock figure says "box and safeties". Use that wording here, or add a gloss: "shell = how many safeties are deep". |
| l.974–975 | "two-deep safety looks (the two-high shells **introduced in** A First Look at Defense)" | Past tense for a chapter I haven't read yet. Write "which [A First Look at Defense] introduces" and add a one-line gloss. |
| l.846–847 | "That's the story of the **'big nickel'** and the **hybrid defender**" | Neither term is glossed. One clause each would do, e.g. "a third safety instead of a slot corner". |
| l.1254 | "Now both tight ends are **flexed** out with Z" | "Flexed" is never defined. Write "split out" or "standing off the line, away from the tackle". |
| l.276 | "the old **'pro set,'** the standard NFL look of an earlier era" | Named but never shown or described, and no link. Add a link to 02-03 and a six-word picture ("two backs side by side behind the QB"). |
| l.254–255 | "**H** or **F** a **'move'** player" | "Move" in quotes is vague. Say "a player the offense moves around: slot, wing or backfield". |
| l.706 cap., l.931 cap. | "**FTN**-charted", "NGS → FTN" | FTN is never explained (it's a charting company). Five words would do it. |
| l.214 | "a '4-2-5' defense" vs l.438 "'4-3'" | I can work out 4-2-5, but not why base is "4-3" (no DB digit) while nickel is "4-2-5". One sentence on the naming convention would help, or defer it explicitly to 02-05. |
| l.1150 / Fig. 11 | QB drawn at 3.5 yards: neither under center nor shotgun | The chapter's check ("if you counted three tight ends and the quarterback is five yards deep… count again", l.905–907) leaves me unsure how to treat a QB at this depth. Either put him under center or name the alignment (pistol, which 01-06 showed). |

Terms done well: personnel grouping, heavy, jumbo, substitution matching, neutral situations ("not late, not
lopsided" is excellent), light box, seam, play-action, wing, empty backfield.

---

## 2. Leaps (a missing or assumed "why")

1. **One-for-one matching vs. the data** (see §0.2). Why is four DBs the floor? Why does 11→22 cost the defense
   only one swap?
2. **Rams 2025, l.1114–1116**: "if the defense **guessed** nickel and the three tight ends came on, it was small
   against a very big offense." The whole chapter says the defense doesn't guess: it sees the substitution and
   gets time to answer. So how was this a hard decision? Was it tempo (no subs, so no window)? Did the 13-personnel
   tight ends play like receivers? This is the chapter's most current example, and its mechanism contradicts the
   rule I just learned.
3. **The run in Fig. 7 (left), l.795 and l.836–838**: the text says the offense can "run **straight at him**" (the
   nickel back). The arrow, though, bounces outside the nickel, and the code comment says "bounce outside the seal".
   Which is it: run through the small man, or let the TE pin him inside and run around him? A beginner reads the
   arrow literally.
4. **Drill 1 answer, l.1172–1174**: "#81 is a tight end lined up like a receiver, so the defense has to cover him
   with someone. **If it's a linebacker**, that's a mismatch." In base the defense still has two corners for #81 and
   #11, so a linebacker isn't forced onto him. The real trade (a corner covering a 250-lb TE who may block him on a
   run, or a defender pulled out of the box) is never stated. The reasoning feels hand-waved compared with Drill 2's
   clean box count.
5. **McVay film room, l.1044–1046**: "the defense… sits in nickel all day." Why is a defense stuck in nickel good
   for the Rams? I can infer "lighter box, so run at it" from the dilemma figure, but the film room should say it.
   As written, McVay's edge is only "the defense learns nothing", and the run payoff is missing.
6. **l.1072 Juszczyk**: "a linebacker **or a safety** following a fullback". Why would a safety follow him and not
   a corner? Drill 2 puts a corner on him. Make the two consistent.
7. **l.1166 "personnel counts who the players are"**: so how does the data label a Deebo Samuel or a Taysom Hill?
   The chapter explains the jumbo labeling problem (l.398–402) but not the more common one: hybrid players counted
   by roster position. This matters for my log as soon as I watch the 49ers.
8. **l.888–890**: "If you predicted 'pass' every time you saw 11 and 'run' every time you saw 12, you'd be right a
   bit more than half the time." Compared with what? Always guessing "pass" in neutral situations gets 52%
   (Fig. 8). Give that comparison in one sentence.

---

## 3. Diagrams: what I couldn't decode, and captions that don't say what to notice

- **Fig. 3 (jumbo)**: the **"6th lineman" label sits under X**, about four yards left of and below #68 (l.384,
  `at=(-3.6, -8.6)`). In print it reads as labeling X, the receiver. Move it next to #68, e.g. behind him at w ≈ −5.
  The gold rings on Y and U also overlap.
- **Fig. 4 (substitution strip)**:
  - The ring colors change meaning from Figs 1–3: gray now means "leaving" (H and `$`), orange means "defensive
    sub", and gold still means TE, while Y, a tight end, now has no ring. The caption explains the pieces, but the
    convention I had just learned ("count the rings") stops working here. Add a line such as "rings here mark the
    four players who change".
  - In panel 1, U (gold) and S (orange) are already drawn at the sideline edges, and nothing tells me they are
    substitutes waiting on the sideline. My first count gave 12 offensive players.
  - The 10-man huddle in panels 1–3 is illegible at print size, and I couldn't find H in it. That's fine if the
    caption says "H is in the huddle".
  - **M and W swap sides** between panels 3 and 4, and S goes to the **left**. The code comment says the strength
    is set to U's side, but with tight ends on both sides I don't know why left. Either keep M and W in place or add
    a clause to the caption.
  - The umpire glyph is a tiny striped disc that looks like a "0" at 60 dpi. Label it "U" or "ump" once, in panel 2.
- **Fig. 5 (defense's answer) and Fig. 10 (fingerprints)**: the white vertical gridlines are drawn **over** the
  bars and cut through the value labels ("80%" for 13, "10%" and "76%" for 22, "33" for the Eagles, "42" for the
  49ers and Seahawks). Draw the grid below the bars.
- **Fig. 8 (pass rate)**: the dashed league line runs straight through the "49%" label on the 12 bar.
- **Fig. 9 (trend)**: the end labels for 21, 13 and "all other" are black, and those three lines converge in
  2024–25. I couldn't tell which line ended at 7.0% and which at 5.1% without the code. Color each label to match
  its line.
- **Fig. 7 (dilemma)**: both notes ("TE blocks the nickel", "LB on a TE in space") float at the top center, away
  from the players they describe. Put them beside the `$`/Y and S/Y pairs. The caption is good.
- **Fig. 12 (Drill 2)**: the right-end "E" box touches Y's gold ring (minor).
- **Fig. 6 (clue clock)**: clear and useful. The caption says what to notice. Good.
- **Figs 1–2 (card deck)**: excellent. The ring-counting convention is the best teaching device in the chapter.
- **Print layout**: large blank areas (a third to a half of the page) on pp. 4, 5, 6, 8, 13, 14 and 17, because
  figures and callouts don't fit and get pushed to the next page. That's roughly three wasted pages, and it
  breaks the reading flow in the jumbo and substitution sections.

---

## 4. Drag and repetition

- The substitution rule and no-huddle material repeat 01-04 (see §0.5). Cut l.623–639 to a recap plus the new
  details: the one-play rule and why the defense can't move first.
- The 11-vs-nickel slot logic repeats 01-03.
- The NGS→FTN caveat appears four times. Keep it in the Go deeper box and one footnote.
- McVay is introduced twice (l.964–966 "see the film room below", then the film room itself).
- The film-room intro says "Five teams, five ways" (l.998), but there are six teams (Rams 2018, 49ers, Ravens,
  Eagles, Rams 2025, Seahawks), plus the Lions earlier.
- "Personnel is who, not where" is said in the section, Drill 1, Drill 2 and the Takeaways. That much
  reinforcement is acceptable, but Drill 2's answer could drop its first paragraph.
- The film rooms are good individually, but five in a row (pp. 13–15) feels long. The 2025 Rams/Seahawks box is the
  freshest, so keep it. The Eagles box could shrink to its "What to notice".

---

## 5. Can I do each "You'll be able to…"? (drills attempted before reading answers)

| Objective | Verdict |
|---|---|
| Decode any two-digit label and recognize jumbo | **Yes** for the eight. **Shaky** on jumbo: the formula fails there (§0.1). |
| Count personnel between plays by watching who runs on and off | **Partly.** I know *what* to count, but not *how* to tell a TE from a WR on TV. The chapter says jersey numbers no longer work and leaves me with "body type… broadcast graphics… homework" (l.337–338). Which broadcast graphics? 01-06 taught stance tells, and a line like "TEs usually set in a three-point stance next to the tackle; WRs stand up, out wide" would connect the two chapters. |
| Explain why personnel is the first clue | **Yes.** The clue clock and the "three jobs" section are clear. |
| Explain the substitution rules and how offenses use or deny them | **Yes.** It was already learned in 01-04; the one-play bluff rule is new and good. |
| Read the 2016–2025 trends | **Yes** for the 2025 turn. **No** for the "rise", which isn't on the chart. |
| Turn personnel into a first run/pass guess with real numbers | **Yes**, but I can't say how much better than the down/distance baseline it is (§0.4). |

**Drill 1** (my answer before opening): 13 personnel (26; 87, 81, 88; 11), expect base, leans run (about 45% pass),
though #81 split wide hints at a pass. **Matches.** The drill is too easy because it hands me the roster
positions. The hard real-world skill is telling a TE from a WR, and the drill skips it. Also, the answer says
nickel against 13 was "about **14%**" (l.1169), but Fig. 5 shows **13%**.

**Drill 2** (my answer): still 21. The offense has the edge: S, a linebacker, is out over Z and a corner is on F,
leaving six in the box against six blockers. So it's a quick throw to Z or a run. **Matches**, and I could do it
because 01-05 taught box counting. This is the best drill.

**Drill 3** (my answer): the defense couldn't substitute because there was no change and no umpire window, so it's
stuck in base. Third-and-7 means a pass, aimed at a linebacker covering a TE. **Matches**, but the setup text and
the section just before it give the answer away, so there is little to predict. A better version would show the
picture and ask "what's wrong for the defense?" without the "Now the offense doesn't substitute" spoiler, and let me
spot that the personnel is unchanged.

---

## 6. Knowledge gaps: what I still wonder

1. Who on the defensive sideline identifies the personnel, and what is the "single word" they shout (base, nickel,
   or a code name)? How fast does it happen?
2. Practical TE vs WR vs FB identification on a broadcast (§5). Do any broadcasts show the personnel on screen?
   (Prime Vision? NFL+?)
3. Why four DBs is the defense's floor, and why defenses rarely swap more than one player at a time.
4. How hybrid players (a WR who plays RB, a TE who is really a big receiver) distort both the label and my count.
5. How much personnel adds over down and distance, including on **3rd down**, which "neutral" excludes. What does
   22 personnel on 3rd-and-1 look like, the hook's own situation? The chapter opens there and never returns to it
   with a number.
6. Is there any limit on how many players can substitute at once? (I assume not, but the Madden note invites the
   question.)
7. The 2025 Rams mechanism (§2.2): if the defense always sees the subs, what made 11-or-13 hard for it?
8. Why 12 personnel rose specifically in 2025. Was there a trigger (a coaching tree, a rule, the kickoff or other
   changes), or just the arms race? One sentence of "nobody knows for sure; the leading explanations are…" would do.

---

## Quick-fix list (in priority order)

1. Add the jumbo arithmetic sentence (§0.1).
2. Pay off the hook: the shouted word, and the one-for-one vs. four-DB floor (§0.2, §2.1).
3. Fix the umpire contradiction in 01-04 l.817 (§0.3).
4. Gloss or replace "shell", "flexed", "big nickel/hybrid", "pro set", "FTN" (§1).
5. Fix the Rams 2025 "guessed" mechanism and the Fig. 7 "straight at him" vs arrow mismatch (§2.2–2.3).
6. Fig. 3 label position; Figs 5 and 10 gridline z-order; Fig. 8 line through "49%"; Fig. 9 colored end labels;
   Fig. 4 note on the subs waiting at the sideline (§3).
7. Drill 1 answer: change "14%" to "13%". Film-room intro: change "five teams" to six.
8. Trim the repeated substitution and source-caveat material to move toward the 4,000-word target, and reduce the
   blank half-pages in print (§4, §3).

---

## Revision (2026-10-06)

Chapter rebuilt with `build_pdfs.py 02-01-personnel-groupings --html`: OK, zero cell errors or stderr, 20 pages (was 19). Every
diagram page was rasterized and looked at, with 150-dpi crops of the substitution strip, jumbo, dilemma, pass-rate and trend
figures. New data claims were recomputed in the `rtg` container with the chapter's own method. New outside claims have
footnotes: `words`, `hybrid`, `floor`, `caller`, `emman`, `fo`, `why`. Every footnote is referenced exactly once.

### Beginner review

| Finding | Action |
|---|---|
| §0.1 Jumbo breaks 5 − RB − TE | Added the rule "with a sixth lineman, receivers = 4 − backs − tight ends." It is flagged early ("jumbo bends the arithmetic"), the jumbo caption sums to 11, the "12 or 13?" paragraph is pinned to the rule, and the rule is in the Takeaways and Watch-for-it. |
| §0.2 Hook not paid off: the shouted word; 2 swaps vs 1 | New "four-DB floor" paragraph: matching is a direction, not one-for-one, and it explains why the hook's defense swapped only one player (data: four DBs on 76% of plays against 22; three or fewer on 14%, mostly short yardage or goal line; `[^floor]`). New "Who makes the call?" paragraph: the word is the package name, a staff member IDs the personnel and the package is relayed (sourced: Steelers.com 2026 on Patrick Graham; ESPN 2015 on the Bills' card system). The hook now promises both answers. |
| §0.3 Umpire contradiction with 01-04 | Fixed 01-04 l.817 to "the official who normally lines up in the offensive backfield". This is a one-phrase edit; 01-04's footnote already cites the 2010 move. |
| §0.4a "Rise of 11" not on the chart | Added a sourced pre-2016 anchor: Football Outsiders 11 personnel at 40.4% (2011), 45.7% (2012), 51.2% (2013) via CBS Sports, 2014 (`[^fo]`). The text says it is a different provider and not on the same axis. Section retitled "Personnel by season: the rise of 11, and the 2025 turn". |
| §0.4b How much does personnel add over down/distance? | New subsection, "How much does personnel add?", with code and asserts. A majority-call guesser by down × distance is right 60% of the time on neutral 2023–25 plays. Adding personnel still gives 60%; adding shotgun gives 66%. On all downs personnel takes it from 63% to 67%. The text says honestly where personnel's value lies: the heavy groupings, short yardage, formation prediction and matchups. |
| §0.4c "Strong run" needs numbers | Watch-for-it now gives 11 56%, 12 49%, 13 45%, 22 36%, jumbo 30%. The heavy-groupings paragraph says "stronger clues". |
| §0.5 Too long / repeats Part 1 | The substitution-rule section is now a recap that links 01-04, plus three new details (like-for-like triggers the hold, not substituting as a weapon, the bluff limit). Cut: the 01-03 slot-logic repeat (now a link), the "Notice three things" umpire repeat, the no-huddle Watch-for-it bullet, two of the four NGS→FTN caveats (the Fig. 9 caption now points to the Go deeper box), the McVay double intro, the Drill 2 "who not where" paragraph, Drill 3's closing rule restatement, and parts of the Madden, heavy-personnel, Why-it-exists, Lions, Ravens and Eagles boxes. **Partly declined:** the chapter is about 8,500 words (prose, drills and callouts, excluding code and footnotes), not 4,000. The coach review asked for five new nuances (personnel caller, situational packages, hybrids, dialects, like-for-like), and this review asked for several new "whys" (four-DB floor, baseline comparison, Rams mechanism, TE identification). Adding all of that while hitting 4,000 would mean dropping film rooms the spec requires. |
| §1 "shell" | Replaced with "box and safeties" (to match the clue clock). |
| §1 "introduced in" 02-05 (past tense) | Now "which A First Look at Defense introduces as two-high", with a gloss (two safeties deep). |
| §1 big nickel / hybrid defender | Glossed: "a nickel whose fifth DB is a bigger safety rather than a small slot corner", linked to 02-05. Example: Seahawks rookie safety Emmanwori (`[^emman]`). |
| §1 "flexed" | Removed. Drill 3 now says "stand off the line, split out beside Z". |
| §1 "pro set" | Linked to 02-03 with "(two backs side by side behind the quarterback)". |
| §1 "move" player | Now "a player the offense moves around, who can be a slot receiver, a second TE or a fullback". |
| §1 FTN | Fig. 5 caption: "charted by FTN, a football-data company". |
| §1 4-3 vs 4-2-5 naming | One sentence in the misconception box: older names leave off the DB count because four was assumed. Linked to 02-05. |
| §1 Fig. 11 QB at 3.5 yd | Named as the pistol (linked to 02-02) in the drill text and caption. |
| §2.1 One-for-one vs data | See §0.2 (four-DB floor). |
| §2.2 Rams 2025 "guessed" | Rewritten. Defenses did match (base on about 73% of Rams 13 snaps), but matching bought little: the Rams threw 47% of neutral 13 snaps (league 13: 46%), almost all from under center (shotgun 9%). The tell was 11: 67% pass vs the league's 57%. Numbers are in `[^rams25]`. |
| §2.3 Fig. 7 "straight at him" vs arrow | Text now says the TE walls the nickel off and the back runs around him. The figure follows the coach's option A (below). |
| §2.4 Drill 1 answer hand-waved | Rewritten: a base corner probably goes with #81. On a run that corner is 195 lb, blocked by a 250-lb TE, and he is the force player; sending a LB or S instead costs a box defender. |
| §2.5 McVay: why nickel helps the Rams | Added: defenses had five or more DBs on 94% of 2018 Rams plays (course calculation in `[^mcvay]`), so the run game faced a lighter front, and the grouping told the defense nothing. |
| §2.6 Juszczyk "LB or safety" vs Drill 2 | Now "a cornerback (leaving a LB on a receiver) or a linebacker (emptying the box)". Points to Drill 2. |
| §2.7 Hybrid players and labels | New paragraph under "who, not where": Deebo Samuel (2021: 59 carries, 365 yards, 8 TD); Taysom Hill listed as QB in 2023/2025 and TE in 2024 in the FTN positions; Ricard. Sources: `[^hybrid]`, nflverse. The Go deeper box explains that the data counts roster position, not role. |
| §2.8 "Right a bit more than half" | Now "about 54% … barely better than the 53% from saying pass every time" (on 11/12 plays). |
| §3 Fig. 3 label under X | "6th lineman" moved directly behind #79. U moved to a legal wing (−1.6, 7.2) so the gold rings no longer touch. The jersey changed to #79 (coach B3). |
| §3 Fig. 4 ring meaning | The caption says rings here mark only the four players who change, with the colors spelled out. |
| §3 Fig. 4 subs at sideline | Panel 1 note: "U and S wait on their sidelines". The caption says the same. |
| §3 Fig. 4 H in the huddle | Panel 1 note "(H too)", and the caption says "H is in the huddle". |
| §3 Fig. 4 M/W swap | Nickel linebackers re-spotted so M and W stay put. The caption explains that S goes left onto U, the TE who just arrived. |
| §3 Fig. 4 umpire glyph | Glyph enlarged and labeled "ump" in every panel. |
| §3 Figs 5 and 10 gridlines over bars | `ax.set_axisbelow(True)` on Figs 5, 8 and 10. |
| §3 Fig. 8 line through "49%" | Value labels now sit inside the bar ends (white). The league line is drawn behind the bars. |
| §3 Fig. 9 black end labels | Each end label is in its line's color and bold. |
| §3 Fig. 7 notes far from players | The notes are now beside the pairs: "Y seals the $ inside" above the $, and "S must run with Y" beside the seam. |
| §3 Fig. 12 E box touches Y ring | The SDE is nudged to a 6i at 1.4 yd depth; the box is now clear of the ring. |
| §3 Print blank half-pages | Fig. 5 shortened (3.0 → 2.6 in) and Fig. 9 shortened (3.6 → 3.1 in), and text was trimmed. The blanks on the old pp. 4, 8, 13 and 14 are gone. Some remain where a long callout or a drill box can't break (Typst keeps callouts whole). |
| §4 "Five teams" | Now "Six teams, six ways". |
| §4 Eagles box long | Cut to a "What to notice" with the numbers. |
| §5 Telling a TE from a WR on TV | The jersey misconception box now gives size, stance (three-point, linked to 01-06) and homework. The same cue is in Watch-for-it. **Drill 1 now tests this skill:** the roster gives only heights and weights plus who has a hand down, not positions. |
| §5 Drill 1 "14%" | Now 13%, matching Fig. 5 (13.4%). |
| §5 Drill 3 gives the answer away | Setup no longer says "doesn't substitute". It says "fourteen seconds later the ball is snapped from this picture". Title is now "third-and-7". The question is "count both teams' personnel; what's wrong for the defense…". Caption trimmed. |
| §6.1 Who calls personnel | See §0.2. |
| §6.2 Broadcast personnel graphics | Not added. I could not verify which broadcasts show personnel on screen, so the text says only that the analyst often names the grouping. |
| §6.3 Four-DB floor | See §0.2. |
| §6.4 Hybrids | See §2.7. |
| §6.5 3rd down / the hook's situation | Added: on 3rd/4th-and-1 (2023–25), 22 personnel passed about 15% of the time (jumbo about 15%), against about 32% from 11. Asserted in code. |
| §6.6 Limit on simultaneous subs | **Declined.** I couldn't verify the exact NFL rule wording, so I state no cap. The hook shows two players swapping at once. |
| §6.7 Rams mechanism | See §2.2. |
| §6.8 Why 12 rose in 2025 | Added "no rule change or single coach set it off". Then the explanation analysts give, with NGS (Reber) quotes: defenses were pressuring and covering better, and heavy personnel forces base (`[^why]`). |

### Coach review

| Finding | Action |
|---|---|
| A1 Dilemma run path vs block | Option A. Y seals the $ inside; the RT reaches a 6i SDE at w = 4.4; Z stalks the RCB (force); the RG climbs to the MIKE. The RB path (absolute) bounces outside the sealed $. The caption says the backside is left to backside blockers. (Note: the original path offsets were relative to the RB, so it already crossed at w ≈ 7.6. The real faults were the missing Z and MIKE blocks and the text.) |
| A2 Seam into a two-high safety | Right panel is now single-high: FS at (13, 0), SS rolled down to (7.5, −9). The caption says "no safety over the seam". |
| A3 "Binary" true only of the Rams | Box split into Rams (binary, 13 hid the play, 11 was the tell: 46.5% / 67.1%) and Seahawks (variety across 11/12/21/22, a FB on 18.9% of snaps, usually Robbie Ouzts per FTN positions). Ouzts is named from the nflverse/FTN data, not from a rookie claim. |
| B1–B3 Jumbo label, rings, #68 | All three done (#79). |
| B4 Defense aligned while the offense huddles | Caption clause added. |
| B5 E/T box collisions | SDE at w = 4.4 in the dilemma (both panels) and in Drill 2 (plus depth 1.4 there). |
| B6 Drill 2 third option | Added: the safety walks down over Z, leaving single-high, which is the look the play-action wants. |
| C1 Situational substitution | Added a paragraph (third-and-long dime, short-yardage/goal-line packages at the whistle). Drill 3's answer now points back to it. |
| C2 Personnel caller | Added "Who makes the call?" (sourced). |
| C3 Hybrids + data labels | Paragraph added, and the Go deeper box explains roster-position counting (a "2 QB … 2 WR" string is labeled 11; about 1% of plays). **Declined:** routing `rb+te+wr != 5` to "other". It would also strip every jumbo play from its grouping and break agreement with the FACTS-current personnel table, which uses the same RB+TE method. Stated in the box. |
| C4 Dialects | Added: words vary by team, digits are the shared language. Sourced to a Texans.com explainer ("20 Pony", "20 Rabbit"). No unsourced "Regular" or "Ace". |
| C5 Like-for-like triggers the hold | Added as the first bullet of "The rules that protect the match". Football Zebras 2025 ("any time the offense substitutes") is already in `[^subs]`. |
| D Lions retry sequence | Corrected per AP: the second try was intercepted but erased by a Dallas offside; the third was incomplete. Footnote updated. |
| D "Many scouts…" | Softened to "some charters and staffs … others write '12 jumbo' or '6 OL'". |
| D Sixth lineman inside | Half sentence added, linking unbalanced line to 02-04. |
| D X "usually" on the line | Done. Also added the free lesson: with two in-line TEs both receivers step back. |
| D Clue-clock defense row | Added "Defense's personnel answer" (:33 → snap). |
| D 10 personnel reason | Added: the defense answers four WRs with dime, and no substitute matches a great TE. |
