# 01-03 The Twenty-Two: beginner-reader review

Reviewer role: a casual NFL watcher who has never played. I have read only 01-01 (field, hashes, scoring, clock,
timeouts, play clock) and 01-02 (downs, line of scrimmage, the spot, the sticks, turnovers, sack, EP/EPA, success
rate, drive, red zone). Sources: `chapters/01-foundations/01-03-the-twenty-two.qmd` (line numbers below are qmd
lines) and `pdfs/01-03-the-twenty-two.pdf` (20 pages, read at 80 and 150 dpi). Body is about 9,400 words without
code or footnotes; the spec target is about 5,000. There are 51 links out to other chapters in the body.

Overall: this is a strong chapter. The "three teams", "bodies match jobs" and "position / alignment / assignment"
threads land, and the combine chart is the best figure in it. The problems are mostly about **labels that mean
two things**, a few **diagrams whose geometry contradicts the prose**, and a handful of **load-bearing words that
are never glossed** (box, formation, motion, "back").

---

## 0. The five biggest problems

1. **The tag key reuses letters, and the "back" rule is never connected to receivers.**
   - The key (l.233–238) gives **T** to both the tailback and the defensive tackle, and **C** to both the center
     and the cornerback. Later figures add **H** for the holder (Fig 6), although H is already the slot receiver,
     **R** for the returner (Fig 7), although R is already the running back, and **S** (Sam) next to **SS**
     (strong safety). Colour and shape tell the two sides apart, but in a dense box (Fig 10) I was reading
     "T" and asking myself which one it was. Use "TB" or "R" for the tailback everywhere, and pick other tags
     for the holder and returner.
   - Fig 3 (l.550) labels **84, the slot wide receiver, as "back: eligible"**. Rule 3 (l.539) says "every player
     in the backfield is eligible", but the chapter has just defined "backs" as the running back and fullback
     (l.365). Nowhere does it say that **any player a yard off the line is legally a "back", whatever his
     position**. That one sentence is the key to the whole section, and to Drill 3, and it's missing.
2. **Fig 5 (the "modern default") contradicts its own story.** The prose (l.849–854) says the defense takes off
   the Sam because he would otherwise have to cover the new slot receiver. In the picture, the ghosted Sam is on
   the **right** (the tight end side) and the slot receiver H and the slot corner $ are on the **left**. So the
   Sam was never going to line up over H. I spent a minute trying to work out whether the slot corner had walked
   across the field. Either put H on the tight end side, or say that the Will (or the whole linebacker group)
   shifts and the slot corner takes the slot wherever it is.
3. **Fig 9 (position / alignment) uses formation labels that break the receiver rules taught on p.5.** There, X
   is "on the line", Z is "a yard off the line" and Y is the tight end "tight to the line". In Fig 9 **Y is
   split off the line like a slot receiver and Z is on the line**. Then the label "snap 2: over the slot" sits
   over **Y**. So is Y a tight end or a slot receiver? (Fig 12, Drill 2, has the same problem: its caption says
   "three receivers to the right", but one of the three is Y, a tight end.) The safety's "~12 yards" label is
   also drawn at about 14 yards.
4. **Fig 10 / the lead-run text: "The one defender nobody blocks is the Mike" (caption, l.1189; repeated at
   l.1247–1249) is false by the reader's own count.** The offense has nine blockers (5 OL, F, Y, X, Z) and the
   defense has eleven players, so at least two defenders go unblocked. In the figure the Mike **and both safeties**
   are unblocked. The analytically minded reader will count, and then distrust the paragraph. Say "the one
   unblocked defender *near the hole*", and add that the safeties are too far away to matter until the runner gets
   past the Mike. Fig 10 also contradicts l.770–771, which says the **Will** is "often unblocked at the snap". Here
   the Will is the one who gets blocked. One clause would explain why ("it depends on the play; on this one the
   fullback takes the Will").
5. **Unglossed load-bearing words (details in §1):** **box** (l.808, 1110, Fig 9, Hamilton callout, though only
   "box count" gets a gloss), **formation** (used about 15 times, never glossed), **motion** (l.474: "lets him go
   in motion"), **wing** (l.403, then a *different* meaning in Fig 6), **the flat** (l.412), **shaded / head-up**
   (l.710, Fig 10 caption), **coverage shell** (l.1176), **draw** (Answer 2), **screen pass** (Watch-for-it).

---

## 1. Terms used before they are explained, or never explained

| Term | Where | Problem |
|---|---|---|
| **40 / "a fast 40"** | l.216 "can't run a fast 40" | The 40-yard dash is first explained at l.318. Gloss it at l.216. |
| **blitz / blitzing** | l.377 "block a blitzing linebacker" | Glossed only at l.751. It is owned by 02-05; give it a parenthetical at first use. |
| **hole** vs **gap** | l.379, 384 "finds the hole", "leads into the hole" | "Gap" is glossed at l.687 and "hole" never is. Are they the same thing? Say so once. |
| **personnel group / formation** | l.401 "lets one personnel group become many formations" | Neither is glossed. "Formation" appears all through the chapter (I-formation, "strong side of the formation"). Give it one line ("how the offense arranges its players before the snap") and forward links to 02-01 and 02-02. |
| **wing** | l.403 "a 'wing' just off the tight end's hip" | Never defined. In Fig 6 "wing" means a blocker on the field-goal unit, which is a different thing. |
| **the flat** | l.412 "leak out into the flat" | Never defined. |
| **motion** | l.474 "lets him go in motion before the snap" | Never defined, and the reason X "can't move around" (l.470) depends on a motion rule the chapter doesn't state (only a player off the line may go in motion). 01-05 owns motion, so give a gloss and a forward link. |
| **press** | l.471 "easy for a defender to press at the line" | Glossed only at l.799 ("right in the receiver's face"). |
| **"count from" / Mike ID** | l.296 "which defender the blocking scheme will count from" | This is opaque to me: what does "count from" mean? One concrete sentence would do it ("he points at the linebacker the line will treat as the middle, so each lineman knows who is 'his'"). |
| **green dot** | l.760 "the 'green dot' from What a Play Really Is" | The wording assumes I have already read 01-04. I haven't, because it comes next. Write "(the 'green dot', which [What a Play Really Is] explains)". |
| **box** | l.678 "box count" is glossed only as "how many near the ball"; l.808 "between the outside cornerback and the box"; l.1110 "standing in the box"; Fig 9 "in the box"; l.1166 | "The box" itself is never defined. It is in the figure I'm asked to read. Give one line: "the area between the tackles, up to about 5–7 yards deep". |
| **shaded, head-up** | l.710; Fig 10 caption "the tackle shaded over the center" | Forward-linked to the technique chapters but never glossed. The Fig 10 caption needs the gloss because I have to find that player. |
| **3-4 / outside linebacker** | l.731 "In a three-man line … outside linebackers"; Fig 8 caption "3-4 edge rushers"; l.740 "a 4-3 defensive end" | "4-3" is decodable from the Fig 1 caption. "3-4" is never named as such, and the chapter never says a three-man line has **four** linebackers. So how do Mike/Sam/Will work there? |
| **nickel** (bold, l.856), **11 personnel** (bold, l.858) | | Bold like a definition, but not linked to the owning chapters' glossary entries (02-05, 02-01). That's inconsistent with the rest of the chapter. |
| **coverage shell, "bails"** | l.1176 | Undefined. |
| **draw** | Answer 2 | "a draw or a quarterback run is the offense's natural counter": a new play type, undefined. |
| **screen pass** | Watch for it, l.1265 | Undefined. |
| **personal protector** | Fig 7 only | Fine in a caption. But he isn't in the specialist list, so I wonder whether he is a specialist. |
| **"step up"** (in the pocket) | l.697 | The idea that a QB escapes pressure by stepping forward is assumed. Half a sentence would cover it. |
| **run-pass plays** | l.581 | RPO is not glossed. It is forward-linked, so this is acceptable. |

---

## 2. Leaps (a missing or assumed "why")

1. **Why X is on the line and Z is off (l.469–474).** "being on the line makes him hard to move around" is the
   whole reason given, and it rests on an unstated motion rule. Also, "easy for a defender to press… so he
   needs to be able to beat that": why does being on the line make press easier? A cornerback can press a man
   who is a yard off, can't he?
2. **Why eligibility exists (callout, l.585–594).** The "320-pounder no DB could tackle" argument invites an
   obvious reply: then defenses would play bigger defensive backs. The "nobody guarding the quarterback"
   argument is a choice the offense could make anyway. The real history (the seven-on-the-line rule and mass
   formations, 1906–1910) is never mentioned. Give the actual rule-makers' problem, sourced, or soften the
   claim.
3. **Why the Will is "often unblocked" (l.770)** and then gets blocked in the only play we see (see §0.4).
4. **Answer 1: "the run worry is the strong side."** The obvious next question is "so why doesn't the offense run
   weak side, where the defense is lighter?" That is the most interesting idea in the drill, and it's left
   hanging. One sentence is enough: the offense does, and that's why the Will has to be fast.
5. **Strong side when there is no tight end, or two (l.505, 774).** The whole Sam/Will/strong-safety naming hangs
   on "the tight end's side". In Fig 9 and Drill 2 the tight end is split out or in a trips formation, and in
   nickel there is no Sam at all. Who is the strong safety then? A one-line "if there's no tight end, the
   strength is usually the side with more receivers ([Formation Rules])" would close it.
6. **"Front seven … In a nickel defense it is often six" (l.870–874).** "Defenses fill that seventh spot in
   different ways, and the choice tells you what they fear" is a teaser with no example. Give one: a safety
   walked down means they fear the run.
7. **The quarterback's planned "order of receivers" (l.357)** is mentioned with no forward link. A reader who has
   only seen Madden will want one.
8. **The FG kicker standing off-centre** (Fig 6: K is about 2 yards left of the holder). Why? (Soccer-style
   approach angle.) Five words would do.
9. **Why a dedicated long snapper rather than the center (l.915–921)?** "It sounds trivial and isn't" answers
   *that* it is hard, not why the starting center can't do it (the snap goes 7 or 15 yards to a moving target,
   with no look between the legs: a different skill).

---

## 3. Diagrams: what I couldn't decode, and captions that don't say what to notice

- **Fig 1 (all twenty-two).** Good picture with a good caption. At print size the OL tags "LT LG C RG RT" are
  squashed together and Q overlaps C's circle. The left "30" yard number is hidden under X. The "defensive
  tackles" label floats between M and the tackles, so it could belong to either row.
- **Fig 2 (two-back share).** Clear. I wondered what "two or more backs" means when the QB is in the backfield.
  The caption covers it implicitly ("running backs / fullbacks").
- **Fig 3 (eligibility).** The "end of the line: eligible" label on the left sits **between 11 and 84**, and the
  right one sits between 87 and 13. At a glance I attached the left label to 84. Put each label directly over
  its player. And see §0.1: "back: eligible" under a wide receiver needs the rule that makes it true.
- **Fig 4 (jersey numbers).** Good. Three shades of blue in a 3-bar group are hard to tell apart in print,
  though; maybe label the eras at the end of one row.
- **Fig 5 (11 vs nickel).** Side mismatch (§0.2). The "slot corner ($) a.k.a. nickel back" label box sits on
  top of the $ marker's ring, which is a label collision.
- **Fig 6 (FG unit).** The caption says "linemen beside him and two tight ends at the ends", but the figure doesn't
  distinguish them (all unlabeled blue dots), and no rushers are drawn, so the wings' job ("stop rushers coming
  off the edge") can't be seen. The **H** tag for the holder clashes with H the slot receiver.
- **Fig 7 (punt).** This one works well. The LS leader line cuts through the line of players. The six
  return-team players on the line are unexplained (do they rush, or block?), and R for the returner clashes
  with R the running back.
- **Fig 8 (combine).** The best figure in the chapter. But the text says "Edge rushers sit just above the line"
  and "each extra 20 pounds costs roughly a tenth of a second" (l.1082–1085), and **no line is drawn**. Add the
  fitted line, so that "above the line" and Donald's distance from it are visible.
- **Fig 9 (one safety, three alignments).** Y/Z alignment contradicts p.5 (§0.3). "snap 2: over the slot" crowds
  the right cornerback, and the ghost it labels is over Y, not over a slot receiver. The "~12 yards" label is drawn at
  about 14.
- **Fig 10 (lead run, print strip).** The story can't be followed in print:
  - At +1.2 s and +1.8 s the ball marker covers the tailback, and at +1.8 s the M square covers both. I could
    not find the T (tailback) in either frame.
  - The caption says "F blocks W", but at +1.8 s F is beside M and W stands untouched above him.
  - The LG + C double-team on the shaded tackle can't be seen, because the defensive squares hide the linemen.
  - The frame notes ("unblocked M fills the hole") are placed on the far right of the frame, about 8 yards from
    the action, which is on the left.
  - Suggestion: offset the ball from the carrier, ring the tailback, put each note next to the player it
    describes, and add a fifth "+0.3 s" frame showing the blocks engaging.
- **Fig 11 (Drill 1).** Clear and fair.
- **Fig 12 (Drill 2).** See §5. The depth cues are ambiguous, and "three receivers" includes a tight end.
- **Fig 13 (Drill 3).** **The caption gives the answer away**: "the receivers 11 and 13 are on the line, 84 is a
  yard off it, and the tight end 87 is on the line next to the right tackle." Counting who is on the line *is*
  the drill. Cut the caption to "The quarterback (9) is in the shotgun, the running back (23) beside him," and let
  the picture do the work. (In the figure the one-yard difference is visible, so it can carry the drill.)

---

## 4. Drag and repetition

- **Length: about 9,400 words against a target of 5,000.** The places to cut without losing a "why":
  - the second two-brothers aside (J.J. Watt, l.740–741), which repeats the Kelce point;
  - the Theismann/*Blind Side* backstory (l.322–328), which could be two sentences;
  - the body-type numbers recited per position (l.317, 378, 486, 501, 692, 706, 752, 802) and then shown again
    in Fig 8. Keep either the in-line numbers or the chart callouts, not both. Or trim the in-line numbers to
    one per family.
- **"Last line of defense"** appears three times (l.794–795, 812, 1244).
- **The Madden callout (l.782–790)** largely repeats the paragraph just before it (l.774–777: Sam and Will flip
  with the tight end).
- **51 forward links.** Formation Rules alone is linked 7 times. Several sentences are mostly "(X covers this)".
  After the first link to a chapter, drop the parentheticals.
- **The Connections "Sets up" paragraph** is a wall of eleven links. Use a short list.
- **Footnote weight in print:** the Juszczyk footnote alone is 5 lines and pushes p.4 to half-empty. The run-strip
  section leaves p.15 half-empty too.

---

## 5. Can I do the "You'll be able to…" items? (drills attempted before opening the answers)

**Drill 1: name the linebackers.** My answer: the tight end is on the left, so 1 = Sam, 2 = Mike, 3 = Will,
4 = strong safety. Run worry: the left (more blockers there). **Correct.** The drill is fair and the picture is
clean. The answer should add the obvious follow-up (§2.4).

**Drill 2: count the defenders.** My answer: **four linemen, two linebackers, five defensive backs (nickel), with
the Sam gone.** That was **wrong**: the answer is 4-1-6 (dime). Why I missed it:
- The question asks "which defensive **player** has left", singular, which primed me for one substitution, and
  nickel is the only package the chapter taught.
- The sixth DB is drawn about 7.5 yards deep, just inside the tight end. The chapter taught me that linebackers
  are "four or five yards back" and slot corners are "between the outside cornerback and the box", so a player
  inside, in the middle, read to me as a deep-playing linebacker. Nothing in the chapter says a defensive back can
  line up inside the tackles at that depth, and "dime" first appears in the answer.
- Fix: make the question plural ("which players have left"), widen the extra DB so he is clearly over a
  receiver, or add one sentence to the nickel section ("on obvious passing downs some defenses go further: six
  defensive backs is dime"). The answer's "a draw or a quarterback run" is an undefined term (§1).

**Drill 3: who may catch it?** My answer: on the line are 11, five linemen, 87 and 13. The ends are 11 and 13, so
87 is covered and ineligible, and there's a flag. 84, 23 and the shotgun QB are eligible. **Correct**, but only
because the caption counted the line for me (§3). Without the caption I would still have got it, because the
one-yard step is visible, which is why the caption should go.

**The six objectives:**

| Objective | Can I? | Notes |
|---|---|---|
| Name all eleven offensive positions, run and pass jobs | Mostly | I can't do a TE's or slot's *pass* job beyond "run a route". There are also not "eleven positions": there are about 8 position names across 11 players, so the wording invites confusion. |
| Name defensive positions; tell Mike/Will/Sam apart by the tight end | Yes, for one in-line tight end against a 4-3 | No: with two tight ends, no tight end, or a 3-4 (§2.5, §1). |
| Name the specialists and find them on a kicking play | FG and punt, yes | **The kickoff unit is never shown.** Where do the kicker and returners stand on a kickoff? It's linked to 09-02 only. |
| Eligible receivers, checked with numbers | Yes | It hinges on "anyone a yard off the line is a back" (§0.1), which I had to infer. |
| Explain body types with combine data | Yes | It would be stronger with the fitted line drawn (§3). |
| Position vs alignment vs assignment; why coaches blur them | Yes for defense (Hamilton) | The offensive "blur" examples (Deebo, Juszczyk) are told, not shown. The chapter has no offensive alignment picture where a back lines up wide. |

---

## 6. Knowledge gaps: what I still wonder

1. **What exactly is a "formation"?** And what are the I-formation, shotgun and "under center" beyond the one-line
   glosses? (A one-line definition and a forward link would do.)
2. **Who is the strong side, and who is the Sam, when there are two tight ends or none?**
3. **The 3-4: four linebackers?** What are they called, and where are T.J. Watt and the OLBs on a diagram? A
   small 3-4 inset beside Fig 1, or one sentence, would close it.
4. **Does anyone still play both ways?** The history section ends at Bednarik in 1960. A reader in 2026 will have
   heard of Travis Hunter (a receiver and cornerback drafted in 2025). If FACTS-current can verify his 2025 usage,
   he is the natural modern bookend. If not, say nothing, but expect the question.
5. **How do substitutions actually work between plays?** Can the defense always match the offense's personnel?
   (01-04 covers this. A forward gloss at l.201, "Players come and go between plays as freely as the coaches
   like", would help.)
6. **The kickoff unit**: who is on it, where the kicker stands, and what changed in 2024–2026 at the level of
   positions.
7. **The personal protector**: is he a specialist? Who calls the punt protection?
8. **Can a lineman report eligible and line up as a receiver out wide?** And what happens if a lineman wearing
   70 catches a pass without reporting? (It's partly covered at l.653–656.)
9. **How many defensive backs can I actually count on a broadcast**, when the safeties are often off-screen? The
   Watch-for-it drill "count the DBs on first-and-10" may be impossible on the standard TV angle. Acknowledge
   it, or link 01-06.
10. **On the lead run, if the Mike makes the tackle (Fig 10, +1.8 s), did the play fail?** The text says "the
    play works only if the tailback beats him", while the frames show him not beating him. Say which outcome the
    picture shows and why that is still the design.

---

## Revision (2026-10-06): finding → action

Covers this review and `01-03-coach.md`. Rebuilt with `build_pdfs.py 01-03-the-twenty-two --html` (OK, zero errors);
all 14 figures re-inspected at 110 dpi. Fact-check rows in `01-03-factcheck.md` are untouched; new claims are sourced
(new footnotes: `hunter`, `philly`, `seven`, `snapper`, `kickoff`; `sewell` extended for 2026; `combine` extended with
TE/LB 40 medians). Every footnote is referenced exactly once.

### Beginner review

| Finding | Action |
|---|---|
| §0.1 Tag letters reused (T tailback/tackle, C center/corner, H holder, R returner) | Running back is **R** in every diagram in this chapter (tailback included); cornerback is **CB** (matches 02-05); holder **Ho**; returners **PR**/**KR**. Key now says shape/color separate the sides and notes later chapters' blue-circle T for a tailback. |
| §0.1 "Back" never defined as anyone off the line | New paragraph in the backs section ("any offensive player who isn't on the line… is a back"); rule 3 restated with it; Fig 3 labels 84 and 13 "a yard off the line, so a back: eligible"; glossary def updated. |
| §0.2 Fig 5 Sam ghost on TE side, slot on the other | Prose now explains the Sam leaves *because he's the least coverage-minded*, the other two LBs shift and the slot corner goes to the slot wherever it is; caption says the Sam is ghosted where he'd have lined up over the TE. |
| §0.3 Fig 9 Y/Z contradict p.5; "over the slot" over Y; "~12" drawn at 14 | Fig rebuilt on the Fig 5 offense (Y in-line, Z off, X on, H slot). Snap 2 is now "walked down outside the tight end" (where the Sam stood), snap 3 in a drawn dashed **box**; snap-1 label sits beside the safety at 12 yd. |
| §0.4 "One defender nobody blocks is the Mike" (false: 9 v 11); Will "often unblocked" vs blocked | Lead run rebuilt as a real iso (coach A1): C comes off the combo to the Mike, F isolates the Will, Y blocks the Sam; the two unblocked defenders are the safeties. New "Now count: nine blockers for eleven defenders" paragraph; caption and bullets rewritten. Will bullet now says he's the hardest LB to *reach*, not "unblocked". |
| §0.5/§1 Unglossed: box, formation, motion, wing, flat, shaded/head-up, coverage shell, draw, screen | All glossed at first use and linked to the owning chapter's glossary anchor (box, motion, wing, shade, head-up, shell, draw); formation, flat, screen glossed inline. |
| §1 40 before explained; blitz; hole vs gap; press; "count from"; green dot; 3-4; nickel/11 bold not linked; "step up"; personal protector | 40 glossed at first use; blitz parenthetical at first use; hole = opening, gaps lettered (link 03-01); press explained in the X bullet; Mike ID rewritten concretely; green dot "which What a Play Really Is explains"; 3-4 = three linemen, *four* LBs, OLBs are the edge, ILBs split the Mike's job; nickel/dime/11 personnel/big nickel linked; "step up" explained in DT bullet; PP described in punt caption as a non-specialist. |
| §2.1 Why X on / Z off | X bullet: someone must be the end on the non-TE side; on-line players can't be in motion; no cushion → easiest to jam. Z bullet: staying off keeps the TE at the end and eligible. |
| §2.2 Eligibility "why" unsourced/weak | Callout rewritten around the sourced 1910 seven-on-the-line rule against mass plays (Dartmouth Alumni Magazine, Nov 1910), then the structural logic. 320-pounder argument dropped. |
| §2.4 Answer 1: why not run weak side? | Added: offenses do, which is why the Will must be the fastest. |
| §2.5 Strong side with 0 or 2 TEs | New paragraph: passing strength, field, back; Mike declares it; link to formation strength (02-02). |
| §2.6 Front-seven teaser with no example | Concrete example: safety walked down = fear the run; six in the box with two deep = pass first. |
| §2.7 QB "order of receivers" | Named the progression, linked glossary + 04-01. |
| §2.8 FG kicker off-centre | Caption: approaches at an angle, soccer style. |
| §2.9 Why a dedicated long snapper | LS bullet explains the different skill (head down, spiral 7/15 yd vs a hand-to-hand or 5-yard toss) and adds the sourced rule protecting him (Rule 9-1-3). |
| §3 Fig 1 squashed OL tags, Q on C, "30" under X, floating "defensive tackles" | OL tags moved to a label; QB drawn at 2.2 yd; yard numbers hidden in diagrams where they collide (helper `hide_numbers`); DT label has leader lines to both tackles. |
| §3 Fig 3 end labels between players | Each label directly over its player; window widened so nothing is near the edge. |
| §3 Fig 4 three blues hard to tell apart | Eras labelled directly on the first row; caption says oldest on top. |
| §3 Fig 5 $ label on ring | Label moved above the ring. |
| §3 Fig 6 linemen/TEs indistinct, no rushers | Caption reworded; two edge rushers drawn with rush arrows and wing blocks. |
| §3 Fig 7 LS leader through the line; return men unexplained | Leader rerouted behind the line; caption explains the six on the line; returner tagged PR. |
| §3 Fig 8 no fitted line | Straight-line fit (non-specialists) drawn and labelled "about 0.1 s slower per 20 lb"; text now says Edge sits "a little above" and Donald ~0.3 s above. |
| §3 Fig 10 strip unreadable | Rebuilt play; ball drawn beside its carrier on the clearest side; R ringed in every panel; notes placed next to their players; frames snap/+0.5/+1.1/+2.2 show combo, F meets W, C climbs to M, FS fills. |
| §3 Fig 12 ambiguous depth; "three receivers" includes a TE | TE flexed off the line as #3 (Z on the line to keep seven); every DB visibly over a receiver at ~6 yd; caption says the inside one is the TE. |
| §3 Fig 13 caption gives the answer | Caption cut to "The quarterback (9) is in the shotgun, with the running back (23) beside him." |
| §4 Length / drag | Cut: J.J. Watt aside, Blind Side backstory to two sentences, per-position body numbers (RB, DT, DE, LB, CB kept in words only), repeated "last line of defense", duplicate Sam-flip paragraph, repeated parenthetical links (Formation Rules, A First Look at Defense), Juszczyk footnote. Connections "Sets up" is now a list. **Net length still grew (~9,400 → ~10,700 words)** because this review and the coach review asked for ~35 additions (definitions, whys, kickoff, 3-4, strength rules, eligibility history, 9-v-11 arithmetic). Further cuts would remove requested whys; left for the editor. |
| §4 Madden callout repeats the paragraph | Rewritten to carry new content: some defenses flip one Sam to the strength, others play field/boundary so names change with the formation. |
| §5 Drill 2 singular "player has left"; dime never taught | Question now plural; dime introduced in the nickel section; answer adds the "dime backer" caution and that the remaining LB is usually the best cover LB; draw glossed. |
| §5 Objectives: "eleven positions"; kickoff never shown; offense blur not shown | Objective reworded ("about eight names cover the eleven players"); **new kickoff figure** (dynamic kickoff, FACTS §3) and paragraph; specialists objective now includes the kickoff. Offensive "blur" picture: **declined**: 02-02/02-04/02-06 draw backs aligned wide and motion; adding a 15th figure here would add length the review asked to cut. |
| §6.4 Anyone still play both ways? | Travis Hunter (2nd overall 2025; 326 offensive / 162 defensive snaps before an Oct 31 knee injury), sourced. |
| §6.5 How substitution works | Between plays, never during; link to Personnel for the defense's right to match. |
| §6.8 Lineman reporting/out wide | Already covered by the reporting paragraph; detail stays in 02-02 (declined to expand). |
| §6.9 Counting DBs on TV | Watch-for-it notes safeties are often off-screen, count on the replay, link 01-06. |
| §6.10 Did the lead run fail? | Text now says what the last frame shows: the design working, FS meeting the runner ~5 yd downfield ("blocked to the safety"). |

### Coach review

| Finding | Action |
|---|---|
| A1 Iso blocked wrong | Fixed as specified: LT base, LG+C combo with C climbing to M (~1.0 s), RG/RT base, Y on Sam, FB iso on Will in the hole (~1.0 s), safeties unblocked, FS fills the alley. Text, bullets, caption and strip notes rewritten. |
| A2 Runner passes lead blocker | Mesh at 0.72 s from a 7-yd I-back, RB 5.8 yd/s vs FB 6.5; RB ~3 yd behind F at contact; no overlaps (checked frame by frame). |
| A3 TE "faster than the LB" | Both sentences fixed; footnote gives TE 4.72 / LB 4.66 medians. |
| A4 Predict 2 unanswerable | Option (a) implemented, plus option (b)'s dime-backer caution in the answer. |
| B1 Strength isn't always the TE; dialect names | Strength paragraph; Madden callout reworded (same Sam flips vs field/boundary); Watch-for-it caveat; dialect line (Jack, Mo, Star, Money) and the $ pun. "Dollar" omitted because 02-05 uses it as the quarter-package alias. |
| B2 Receiver letters are a dialect | New paragraph: Y as a slot in some systems, F/H swap, U, X/Z flip; "the letter names a spot, not a person". |
| B3 1-tech vs 3-tech | DT bullet split into the absorber and the 3-technique (linked); Donald "an undersized 3-technique"; glossary def extended. |
| B4 Nobody outside the attached TE in Fig 5 | Strong end moved outside the TE (w=5.6) in `eleven_vs_nickel`; text and caption explain it. **Note for gridiron (not edited):** `defense("nickel", …)` against an attached TE leaves the strong DE inside him; it should probably be a 9 when the TE is attached. |
| B5 "LB who plays as a fifth DB" backwards | Rewritten as suggested. |
| B6 Five DBs isn't always a slot corner | Big nickel added (nickel section, Watch-for-it, Hamilton film room). |
| B7 Small edits | "biggest man on the defense"; Davis "as fast as"; guard pull "opens his hips… along the line, just behind it"; box count is the number counted; long-snapper protection rule (verified: Rule 9-1-3, NFL.com); SS at 10.5 yd in the base picture and Predict 1 (answer mentions the depth cue). |
| B8 Sewell 2026 | Verified (AP via WTOP, May 29, 2026): moved to LT after Decker asked for his release. Misconception box now uses both halves of the story. Warner: no status claim in the chapter, nothing to change. |
| C fig-combine RB/LB labels | Separated. |
| C fig-position-alignment label/ghost ring, Y-as-slot | Figure rebuilt (see beginner §0.3). |
| C yard numbers under X | Hidden in all field diagrams where they could collide. |
| C tag reuse | See beginner §0.1. |
| D Philly Special | Added to eligibility rule 3 and the Predict 3 answer, sourced (Wikipedia; Eagles.com). |
| D Lions–Cowboys 2023 reporting play | **Declined**: belongs to 02-02 and would add an unverified detail here; the "number 70 is reporting" sentence already points there. |
