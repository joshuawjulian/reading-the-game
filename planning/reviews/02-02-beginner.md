# 02-02 Formation Rules and the Language of Alignment: beginner-reader review

Reviewer role: a casual NFL watcher who has never played. I have read only Part 1 (01-01 to 01-06) and 02-01
(Personnel). From those I already know the field, the hashes, field side and boundary side, the line of scrimmage,
every position (including that X is on the line, Z a yard off, and the slot is H or F), that ends and backs are
eligible and 50–79 are not, shift and motion rules, tells and the prediction log, personnel digits, and jumbo
(including a two-line preview of reporting). Sources: the qmd (line numbers below are qmd lines) and
`pdfs/02-02-formation-rules-and-vocabulary.pdf` (19 pages, read at 60 and 110 dpi).

Body prose is about **8,050 words** without code or footnotes. The spec target is about 4,500.

**Overall:** a strong chapter. The best idea in it is that the rules create the letters: X is on the line because
somebody has to be the end on that side. That idea landed for me. The QB-depth chart is the most useful single
thing I've learned in the course so far. The Patriots story is told cleanly and keeps the season and the calendar
year straight. The problems fall into four groups:

- the one-yard on/off difference is almost invisible in every formation plate;
- the Patriots story skips the rule that makes the trick make sense;
- one data sentence contradicts its own chart;
- several numbers don't line up from paragraph to paragraph.

---

## 0. The five biggest problems

1. **"On the line" vs "a yard off" can't be seen in the plates.** gridiron draws on-the-line players at d = −0.7
   and off-the-ball players at d = −1.5, which is **0.8 yards apart, less than one marker diameter**. That affects:
   - **Fig 2 (p.3):** In panel 1, X (on) and H (off) look like they're at the same depth with a slight wobble. In
     panel 2 ("X stepped back") I had to compare it with panel 1 to see that X had moved at all.
   - **Fig 4 (p.7)** and **Drill 1 (Fig 11, p.17):** same problem.

   The drill only works because the caption tells me "X and Z are wide receivers, each a yard off the line". So
   the caption does the counting for me, and the drill becomes reading, not seeing. This is the chapter's central
   skill. Exaggerate the depth, as Fig 1 already does with its "depths are stretched" note, or draw a faint dashed
   "1 yard back" line across each plate.

2. **The Patriots film room (l.1043–1048) never says what "count" Vereen was making up.** It says: "only four
   offensive linemen, and one of their eligible-numbered players reported to the referee as ineligible **to make up
   the count**." Which count? The chapter has taught "seven on the line". The Patriots had seven on the line
   without any report. Nothing in the chapter says the offense also needs a minimum number of *ineligible* players
   on the line. The NCAA box (l.1024) mentions a five-players-numbered-50–79 rule, but only for college, which
   implies the NFL has no such rule.

   Without that rule, the table on p.15 is a puzzle. Vereen stood on the line *inside* Edelman, so by this
   chapter's own covered-receiver rule he was already ineligible. Why report at all? That's the first thing I
   wondered, and the chapter can't answer it. Add one sentence giving the NFL rule the formation had to satisfy
   (fact-checker to confirm the exact wording). A small diagram of the Patriots alignment would also help: 47 at
   left tackle, Solder at guard, Vereen covered in the slot. It's the most memorable story in the chapter and the
   only one with no picture. I had to rebuild the line in my head from the footnote.

3. **"How often does it happen? More often every year." (l.952) contradicts Fig 10 on the next page.** The dark
   (reported) bars go about 720 → 480 → 570 → 780 → 500 → 730 → 720 → 570 → 770 → 1,450. Reported snaps fell in
   2017, 2020, 2022 and 2023. What rose steadily-ish is the *share* with a report, and that wasn't monotonic either
   (56% → 59% → 55% → 69% → 65%). A data-minded reader catches this immediately, and it makes me distrust the
   numbers around it. Suggested fix: "The share has roughly doubled in a decade, and 2025 was a record."

4. **The QB-depth numbers don't line up from paragraph to paragraph.**
   - l.667 says the shotgun is on "about two in three" plays in the 2020s.
   - Fig 7 (p.10) says shotgun was **52%** of plays.
   - l.775 says under center was "about a third of all plays in 2025".
   - Fig 7 says under center was **39%**.

   These are different populations (all plays vs neutral 1st/2nd down; one season vs three). The only explanation
   is footnote 8, which I read only after I'd decided something was wrong. Put the reconciliation in the body,
   for example: "On early downs in close games, which is where formation choice is most informative, the shotgun
   drops to about half."

   Also, **pistol's 28% pass rate is lower than under center's 34%.** That's the most surprising number on the
   page, and the chapter doesn't comment on it. Why is the pistol the run-heaviest alignment? Who uses it? Is
   this mostly the Ravens? This is also the payoff of the opening hook ("why four yards instead of five changes
   what the offense is likely to do"), and the chapter never calls back to it. The hook's other two details get
   explicit callbacks (l.262, l.379). The pistol one should too.

5. **Labels used but never defined in this chapter.**
   - **U**: used as a tight-end letter in Fig 9, Drill 1 and Drill 3. The alphabet section is titled "X, Y, Z, H
     and F" and the subtitle says "five letters". 02-01 showed U only in captions ("Y/U = tight ends"). Add a
     line: "U (or another letter) for a second tight end."
   - **H-back**: in the Wing glossary entry and at l.572 ("a tight end or an H-back"). Only Fig 5's caption
     explains it, two paragraphs later. It isn't owned anywhere in the term index, so this chapter should define
     it in the text.
   - **C**: means both center and cornerback in Fig 3 panel 1 (p.5) and in all four panels of Fig 9 (p.13).
     01-03's beginner review flagged the same collision. In Fig 9 there's a "C" on each side of the ball within
     five yards of each other.

---

## 1. Terms used before they're explained, or never explained

| Where | Term | Problem |
|---|---|---|
| Fig 1 label (p.2) | "the offense's line (the back tip of the ball)" | First time I learn that the offense's line of scrimmage is the back of the ball, not the ball. It's said only in a figure label, and it matters for "a yard behind the line". Say it once in the bullet at l.204. |
| l.200–201 | "a plane through the center's waist" | I pictured a horizontal plane (a height). It's a vertical plane parallel to the line. Fig 1 helps, but one word ("an imaginary vertical wall through the center's waist") would avoid it. |
| l.541 | "jam him at the snap" | 01-03 used "press". Fine in context, but "press" and "jam" should be tied together once. |
| l.476–477 | "over", "under", "rotate to strength" | Offered as examples of defensive calls but not glossed. Add a half-line ("'over' and 'under' are fronts shifted toward or away from the strength, built in [Even Fronts]"). |
| Fig 3 caption | "a typical 4-3 defense", "the strong safety (SS) **rolls** to that side" | "4-3" was previewed in 02-01. "Rolls" is new jargon. |
| l.498, l.832, l.844 | "the X ran a dig", "slants, digs, posts", "an out, a corner route" | Routes aren't taught until Part 4. The inside/outside grouping in l.832 is enough to follow the sentence, but "dig" in the section's opening quote means nothing to me. Use a route a casual fan knows ("the X ran a slant"), or gloss it. |
| l.848, l.853, l.1110 | "a cornerback all alone on an island", "isolation" | Jargon. "Isolation" also collides with "iso", a run play owned by 03-03. |
| l.548 | "the Air Raid" | Undefined. Either drop it or add "(a pass-first college system, see 04-08)". |
| l.583 / Fig 5 | "a lead blocker or a fullback-like player" | "Lead blocker" isn't defined. |
| l.771 | "can sneak" | QB sneak isn't defined (the meaning is guessable). |
| l.686 | "pistol option plays" | Has a forward link. OK. |
| l.707, Fig 7 | "charting data", "FTN charting" | I don't know who FTN is or what "charting" means (people watching film and tagging plays?). One clause would do it. |
| Answer 2 (p.19) | "the strong-side defensive line" | Never defined. |
| Answer 2 (p.19) | "a special check against three-receiver sets" | Vague. Name it or forward-link it ("a 'trips check'"). |
| l.1068 / fn 17 | the 2015 rule's penalty | The body never says what the foul is. "Illegal substitution" appears only in the footnote. |
| l.886 | "tackle-eligible" vs "eligible tackle" | Fine, but say which one broadcasters actually say. |

## 2. Leaps (a missing or assumed "why")

1. **Why is the slot receiver off the line?** The X-on/Z-off logic (l.354–361) is great, but it explains only
   the outside receivers. Fig 4 labels H "slot, off the line" with no reason. The reason follows directly from
   this chapter: if H stood on the line inside X, X would cover him. Say so. It also gives the reader a general
   rule: *on each side, only the outermost player on the line is eligible, so anyone inside the end who wants
   to catch passes has to be a yard off.*

2. **Can a covered or ineligible player still run downfield on a pass?** The "Why it exists: covering on
   purpose" box (l.369) says "If the defense doesn't notice he can't run a route, it will waste a defender
   covering him." That implies he doesn't run a route. If he does release, is that a foul? The ineligible-downfield
   rule is linked only in Connections (04-06). One sentence would do: "an ineligible player can't go more than
   a yard downfield before a pass is thrown, so a covered tight end is a blocker on a pass play."

3. **Is the shotgun quarterback eligible?** l.188 makes the under-center QB the one exception, so a shotgun QB is
   a back and therefore eligible? I immediately thought of the Philly Special. This is a perfect one-line
   payoff of the rule, and it's missing.

4. **Does a detached tight end still set the strength?** Fig 3 panel 3 has Y in the slot and calls it
   "balanced, no attached tight end", so the strength goes to the field. That implies a flexed or split tight
   end loses his strength-setting power. That's a real rule, but it's only implied by a figure. Say it in the
   tight-end-strength paragraph, and tie it to Fig 5 ("the farther he stands from the tackle, the more he says
   receiver"; does he also stop saying "strong side"?).

5. **For passing strength, do the backs count?** l.459 says "eligible receivers lined up away from the ball". In
   Fig 4's 3x1, the in-line Y counts as #3. Does the running back beside the QB count? Probably not. Say so.

6. **"Some defenses set the front toward the running back's side, or away from it" (l.492).** This is left
   dangling. Why would they? Either give the reason in a clause or cut the sentence.

7. **Why did reporting go from 40% to 80%?** Fig 10 shows the trend but the text gives no explanation. The
   follow-up question: if reporting costs nothing and adds a threat, why doesn't *every* jumbo lineman report?
   Is there a cost? The Lions box suggests one: a report tells the defense to expect a run. There may also be a
   rules cost: fn 10 says the status persists until a stoppage. Neither point is made in the body.

8. **How does the defense actually hear the announcement?** l.876 mentions the stadium mic and "signalling to
   the defense". What's the signal? Does the referee point at the player? On TV, how do I tell which lineman
   reported? The Watch-for-it bullet says "listen for 'reporting as eligible'", so I need to know what I'll hear
   and see.

9. **Opening hook (l.158–159): "two of them are about the rules."** Which two? Only the receiver's question is
   about a rule. Strength is a defensive convention and QB depth is a choice. I reread the paragraph looking for
   the second one.

10. **Does the defense have any alignment rules?** After a whole chapter of offensive constraints, it's the
    obvious question. One sentence would answer it ("none of this applies to the defense, which can line up
    anywhere on its side of the neutral zone").

## 3. Diagrams: what I couldn't decode, and captions that don't say what to notice

- **Fig 1 (p.2):** Clear and effective. It's the one plate where on and off are visible. The caption says "the
  receiver far out on the right (X)", but the X in the plate isn't drawn far out; it's at the right edge of a
  close-up. That's fine, but "the receiver" alone would read better.
- **Fig 2 (p.3):** The counting numbers are good. As covered in §0.1, X's step back in panel 2 is nearly
  invisible. In panel 3 the red ring on Y is clear.
- **Fig 3 (p.5):**
  - Panel 1 is good once you find S and SS. The C/C collision is described in §0.5.
  - Panel 2 labels "where the front sets" and "where the coverage leans" but shows **no defense**, so the claim
    is asserted, not shown. Either add ghosted defenders, or change the labels to "front usually sets here" and
    "coverage usually leans here".
  - Panel 3 is drawn at full-field scale, so the markers are about half the size of panels 1–2 on the same page.
    It reads, but the jump in scale is jarring.
- **Fig 4 (p.7):** Good. The bottom panel's #1/#2/#3 labels are what I needed. On/off depth again (§0.1).
- **Fig 5 (p.8):**
  - The caption says the H-back is "behind the tackle", but he's drawn behind the guard–tackle gap, nearer the
    guard (w = 2.3; guard at 1.6, tackle at 3.2).
  - **WING and FLEXED look the same.** With no in-line tight end drawn, the "wing" sits about 4 yards outside the
    tackle, a yard off the line. The flexed tight end is also a yard off, just about 4 yards farther out. I
    couldn't tell what makes one a wing and the other flexed. A ghosted in-line player, or pulling the wing in
    tight to the tackle, would fix it.
- **Fig 6 (p.9):** Clear.
- **Fig 7 (p.10):** Clear. The pistol bar is the aqua used for "eligible" everywhere else, which is a trivial
  clash. The caption should tell me what to notice (for example "under center and pistol are run-first; shotgun
  is pass-first; under-center passes are almost all fakes").
- **Fig 8 (p.11):** Good. This one taught me something I didn't know. The hdim arrows run straight through the
  shotgun Q, which is a bit cramped but readable.
- **Fig 9 (p.13):**
  - Panel 3 is the busiest plate in the chapter. E's path, the ball's dashed path and 70's route all cross within
    a yard of 70, and the "E bites on the fake" label isn't attached to any visible arrow. I couldn't tell which
    way E moved.
  - In panel 1 the label "goal line" sits inside the grey end zone, not on the orange line. Since orange means
    "line to gain" in every earlier chapter, say "the orange line here is also the goal line".
  - The C collision (§0.5).
- **Fig 10 (p.14):** Clear, but the text contradicts it (§0.3).
- **Drill 1 (p.17):** U is drawn about 3.4 yards outside the left tackle, so he looks like a slot or flexed tight
  end, not the "wing just outside the left tackle" the caption describes.
- **Drill 3 (p.18):** The numbers bands are a great touch. The caption gives away the key read ("Z ... well inside
  the numbers"). The picture alone shows it, so trust the picture and let the reader find it.

## 4. Drag and repetition

- **Length:** about 8,050 words against a 4,500 target. It rarely *feels* padded, but several things are said
  three or four times:
  - **The QB-depth tell** appears in the body (l.763–776), the mid-chapter "Watch for it" (l.778–782), the Sunday
    checklist (l.1107), Answer 3, and the Takeaways. The mid-chapter "Watch for it" is nearly word for word the
    Sunday bullet. Cut it.
  - **The legality test** appears in the section opener (recapping 01-03), the misconception box (l.337–339), and
    Takeaways. The misconception box's closing "legality test is short" list is good. The opener's recap could
    be two lines shorter.
  - **The covered-receiver logic** appears in the Fig 2 caption, at l.326–330, at l.345–348, and in the
    "covering on purpose" box. Fig 2's caption could stop at what to notice and leave the explanation to the
    text.
  - **Fig 4's caption** restates the four bullets that follow it.
- **The "Go deeper: college and high school" box (l.1023–1034)** is interesting, but the A-11 story is a long
  tangent from a chapter that's already long. It's a candidate to trim. The one sentence I'd keep is "college
  linemen can't report eligible at all".
- **The Lions box** spends its first paragraph pointing back to 02-01. It could start at "Detroit's reported
  linemen did catch passes."

## 5. Can I actually do each "You'll be able to…" item?

I attempted all three drills before opening the answers.

- **Drill 1 (count it):** I said: six on the line (5 OL + Y), so illegal. Fix: X steps up, which makes X the
  left end and Y the right end. Eligible after the fix: X, Y, U, Z, R; the QB isn't. **Matched the answer.** I
  missed the alternative fix (U steps up), which is fine. But I got the count only from the caption's words.
  From the picture I couldn't see that X and Z were off the line (§0.1).
- **Drill 2 (strength):**
  - My answer: TE left, receivers right, field left (ball on the right hash). Front to the left, coverage leaning
    right. Why: it makes the rules disagree. **Matched.**
  - The "why the offense likes it" part was an educated guess from the "one word, eleven players" box. I didn't
    reach the answer's specific point that the trips are in the *boundary*, so the coverage has to choose between
    following the receivers and protecting the field.
- **Drill 3 (read the alignment):**
  - My answer: under center, which leans run. Both tight ends are right and the field is right, so a run right.
    Z's reduced split suggests a crack block or an out-breaking route. If it's a pass, play-action. **Matched.**
  - I didn't think of X as the backside threat. That's fine; it's a Part 4 idea.

Objectives:

1. **Check legality: mostly yes.** On paper I can do it. On TV I don't know how to judge a yard of depth from the
   standard broadcast angle (§6).
2. **Strong side three ways, and front vs coverage: yes.** Seeing *which way the defense set its front* on Sunday
   is harder. The checklist says to find the Sam and the safety who walks down, but I don't know how to pick out
   the Sam on TV. A pointer to 02-05 would help.
3. **Labels and old names: yes,** except U and H-back (§0.5).
4. **QB depth as a clue: yes.** This is the most immediately usable skill in the chapter.
5. **Splits vs numbers and hash: yes,** and the "boundary receiver looks tight" misconception was an aha moment.
6. **Reporting, the Patriots, the 2015 rule: partly.** I can explain reporting and the 2015 rule. I can't fully
   explain *why the Patriots' trick needed Vereen to report ineligible* (§0.2).

## 6. Knowledge gaps: what I still wonder

- How do I judge on vs off the line from the TV angle? Is there a visual tell, like stance, hands on knees,
  or the receiver being level with the tight end's helmet? Or do I need the end-zone or All-22 view (01-06)?
- What NFL rule did the Patriots' formation satisfy, and why did Vereen have to report if he was covered anyway?
- Why is the pistol so run-heavy, and which teams live in it today?
- Is a shotgun QB an eligible receiver? (The Philly Special.)
- Can a covered tight end go downfield on a pass play?
- Why don't jumbo linemen *always* report? What does reporting cost?
- Why did the share of reports double over the decade?
- Does a flexed or detached tight end still set the strength?
- Do backs count toward passing strength or the #1/#2/#3 numbering?
- What do "over" and "under" look like? (A forward link is enough.)
- What about the QB alignments the chapter doesn't name: empty backfield, or a direct snap to a running back
  (Wildcat)? One sentence and a forward link would close the set.
- Does the defense have any alignment rules at all?

---

## Revision (2026-10-06)

Revised against this review and `02-02-coach.md`. Rebuilt with `build_pdfs.py 02-02-formation-rules-and-vocabulary --html`
(OK, zero errors, 22 pages) and every figure page re-inspected. Fact-check log left intact; every new factual claim
has a footnote (new: `[^defalign]`, `[^downfield]`, `[^strengthcalls]`, `[^qbelig]`, `[^phillyspecial]`,
`[^pistolteams]`, `[^patscount]`), most of them quoting the 2026 NFL rulebook text directly.

### Beginner review

| Finding | Action |
|---|---|
| §0.1 on/off depth invisible in plates | All formation plates now draw off-the-line players at d = −2.7 (new `OFF_D`) with a dashed "a yard back (depth stretched)" guide (`depth_guide()`); captions say depths are stretched. X's step back in Fig 2 panel 2 and the Drill 1 count are now visible, not just stated. Added a "can you see it from your couch?" paragraph (helmet vs nearest lineman; end-zone replay; the count does the work). |
| §0.2 Patriots "count" unexplained; why Vereen reported | The reporting section now states the rule (Rule 7-5-1(b): all five players between the ends must be ineligible; Rule 5-3-1: an eligible-numbered player in such a spot must report), with Belichick's own summary. Film room says Vereen was "ineligible twice over" (covered and reported). New figure `fig-patriots` draws the seven on the line (47 at tackle, 77 Solder at guard, 34 Vereen covered, 11 Edelman) with the five-man bracket; it replaces the table. |
| §0.3 "More often every year" contradicts Fig 10 | Rewritten: the share "didn't climb every year (it dipped in several), but it roughly doubled over the decade", 2025 the highest. |
| §0.4 QB numbers don't reconcile; pistol 28% unexplained; hook callback | Body paragraph reconciles all-plays (~2 in 3 shotgun) vs the chart's neutral early downs (~half). New pistol paragraph: run-first by design; ~6% of plays; Atlanta ~⅓ of plays in 2024 and 2025, Miami 29% in 2024, Baltimore only ~7% (computed and asserted in the chapter's code). Explicit callback to the opening scene in the pistol section. |
| §0.5 U, H-back, C/C collision | Added a bullet defining U (second tight end) and R/T/B (the back). H-back defined in the spot-names list (backfield, off the tackle's hip; Gibbs; link to 03-01). Not added to the glossary: no chapter owns it in the term index. All cornerbacks now labelled CB. |
| §1 terms | Offense's line / back tip of the ball now in the bullet text (with the neutral zone, per Rule 3-18); "imaginary vertical wall"; press tied to jam (linked); over/under glossed with link to 05-02; "rolls" replaced; "dig" replaced with slant, inside routes glossed with a Part 4 link; island/isolation replaced with "one-on-one with the cornerback"; Air Raid glossed; lead blocker glossed inside the H-back definition; sneak glossed; FTN charting explained; Answer 2 rewritten (front sets to the TE; "trips check" named and glossed); 2015 rule's penalty (illegal substitution, 5 yards) now in the body; "you'll hear both" for tackle-eligible. |
| §2.1 why the slot is off the line | New paragraph: on each side only the outermost man on the line can catch a pass, so slot, wing and backs are off the ball. |
| §2.2 can a covered player go downfield | Added to "covering on purpose": not more than a yard past the line before the throw (Rule 8-3-1). |
| §2.3 shotgun QB eligible | New paragraph with Rule 3-42 / 8-1-6 and the Philly Special (Super Bowl LII, Feb 2018, 2017 season). Fig 4 caption notes it. |
| §2.4 detached TE and strength | Stated in the tight-end-strength paragraph and tied back after Fig 5. |
| §2.5 backs and the #1/#2/#3 count | Added: the count includes the TE and a back once he aligns or releases to that side; a back directly behind the QB isn't counted until he picks a side. |
| §2.6 running-back-side sentence dangling | Cut. |
| §2.7 why reporting rose; why not 100% | New paragraph: the data can't say what coaches thought; the rulebook shows the costs (announcement time; must keep reporting and stay eligible until a stoppage) and the message (a report says "run"). |
| §2.8 how the defense hears it | Step 2 rewritten: rule wording ("will inform the defensive team"), the turn-and-announce plus wireless mic in practice, the ball can't be snapped until the referee is back in position, and the TV giveaway. |
| §2.9 "two of them are about the rules" | Hook rewritten: rulebook / defense's language / offense's plan. |
| §2.10 defense alignment rules | New paragraph: anywhere on its side of the neutral zone, sourced (`[^defalign]`). |
| §3 Fig 1 | Caption says "the receiver (X)" and explains why Y has no ring. |
| §3 Fig 3 | Panel 1 rebuilt (see coach #1); all three panels now at one scale (full width); panel 2 labels now "the front usually sets here" / "the coverage usually leans here". |
| §3 Fig 5 | Redrawn: wing on the left, ~1.4 yd outside the tackle; H-back off the tackle's hip; flexed moved in to w 9.2; in-line, flexed and split on the right. Wing and flexed no longer look alike. |
| §3 Fig 7 | Pistol bar recoloured neutral grey; caption now says what to notice. |
| §3 Fig 8 | Quarterback moved under center so the dimension arrows no longer cross him; FIELD SIDE label moved off the numbers lane and boxed. |
| §3 Fig 9 | Panel 3: E starts wider and visibly crashes inside #70; W chases the fake; both ringed; one "E and W chase the run fake" label; 70's release goes straight up past them. Panel 1 label "goal line = the orange line". CB labels. |
| §3 Drill 1 / Drill 3 | U moved to just outside the left tackle. Drill 3 caption no longer gives away Z's split. |
| §4 drag | Cut the mid-chapter QB "Watch for it" box; opener recap shortened to one paragraph; Fig 2 caption trimmed to what to notice; college/A-11 box cut to five sentences; Lions box's opening paragraph cut to a clause. Declined: the 4,500-word target. The chapter is longer (about 9,900 words by a raw count including callouts and captions) because most findings asked for missing whys; the repetition the review flagged is gone. |
| §5 objectives 1, 2, 6 | Addressed by §0.1 (visible depth), the Sunday-checklist nickel note with links to 05-01 and 02-05 (how to spot the front without a Sam), and §0.2. |
| §6 knowledge gaps | All answered in the text (TV angle, Patriots rule, pistol users, shotgun QB, covered TE downfield, reporting costs, why reports rose (honestly: unknown from data), detached TE, backs in the count, over/under link, empty and Wildcat in one sentence with a link to 02-04, defense alignment). |

### Coach review

| Finding | Action |
|---|---|
| 1. Base 4-3 vs 11-personnel slot | Panel 1 offense is now 21 personnel, I-formation (F and R), against the 4-3 Over; caption updated. Drill 2 answer now says "nickel ... the front (the defensive line's shade and the linebackers) sets to the tight end". Sunday checklist adds the nickel/no-Sam note (3-technique, link 05-01; package link 02-05). |
| 2. Wing drawn as flexed | Fig 5 wing at (−2.7, −4.6), 1.4 yd outside the tackle; Drill 1 U at w −4.7. |
| 3. H-back inside the tackle | Now at (−4.4, 4.2), off the tackle's hip; label "off the tackle's hip". |
| 4. No F; U untaught | Third panel in Fig 4 (21 personnel I-formation, F = fullback); U and R/T/B bullet. |
| 5. Eligible backs unringed | R ringed in all Fig 4 panels (and F); caption notes the shotgun QB is technically eligible; shotgun-eligibility paragraph added. |
| 6. Strength code words | Added Rip/Liz (Saban), Roscoe/Louie, "Rita Sky!", framed as examples; offensive dialect sentence (Right = TE side in many pro-style books vs trips side in many spread books) with link to 04-08. |
| 7. Back counts in numbering | Added (see beginner §2.5). |
| 8. Hash landmark, minimum split, plus/minus | New paragraph. Hedged: the slot "splits the difference" and uses the far hash on the wide side (the NFL hash is only ~3 yd from a centred ball, so "align on the hash" as stated would be wrong for the NFL); minimum split ~6 yd / top of the numbers; plus/minus split. |
| 9. Back's pass-protection side | Reworded: "may block his own side or cross the quarterback's face, depending on the protection call" (link 04-02). |
| 10. What "the count" is | Done (beginner §0.2); rule article confirmed from the 2026 rulebook text: 7-5-1(b) and 5-3-1. Note: the NFL has no "five numbered 50–79" quota as such; the requirement is that the five between the ends be ineligible, with eligible numbers reporting. |
| 11. Fig 1 Y covered | Caption explains Y's missing ring. |
| 12. Fig 9 bite, corner, referee | Done: E crash visible; LCB at (2.7, −8.5), ~3.7 yd outside #70 and clear of the E; referee ~10 yd deep on the QB's right (window widened to −12.4). |
| 13. Drill 1 third fix | Added (Z steps up: legal, but covers Y). |
| 14. Drill 3 play-action partner | Answer now names the bootleg away from the fake, Z's crosser and X's comeback/post, with a link to 04-05. |
| Polish: count digits on hash ticks | `count_line` raised to dy 2.9 with a light circular backing. |
| Polish: Fig 2 panel 3 label on hash ticks | Moved to w 8.0 and separated vertically from the Z label. |
| Polish: Fig 4 "Y in-line (#3)" | Shifted to TE_W + 0.6 with backing. |
| Polish: flexed too wide | w 9.2 (4.4 yd outside the tackle at OFF_D depth). |
| Polish: FIELD SIDE label on numbers lane | Moved to w 23.4 with a backing box. |

### Print-layout note

Quarto's Typst callouts are unbreakable, and footnotes referenced inside a callout that gets pushed to the next
page are stranded on the earlier page (this produced two near-blank pages in the first rebuild). The Patriots
figure therefore sits just after the film-room callout, and the film rooms' source footnotes are referenced
once each in a sources sentence under "## Film room" instead of inside the callouts.
