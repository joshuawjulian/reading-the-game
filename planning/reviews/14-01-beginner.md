# Beginner review: 14-01 Building a Roster

Reviewer role: casual fan, never played, has read 01-01 through 13-05 in order. Read the .qmd start to finish
and looked at every page of `pdfs/14-01-building-a-roster.pdf` (25 pages; key figure pages re-rendered at 130 dpi).
Drills were attempted before opening the answers.

**Overall:** strong, confident chapter. The contract-anatomy figure (Fig 4) is the best explanation of cap
mechanics I've seen, and the price-versus-play pair (Figs 2-3) lands the central idea with data. The problems
are concentrated in the draft-value section, where the chart and the drill table contradict the prose, and in
Predict 1, which can't be solved with the information it gives. The chapter is also long: about 10,200 words of
prose and footnotes (code excluded) against a 6,500 target.

---

## 1. Terms used before they're explained, or never explained

| Where | Term | Problem |
|---|---|---|
| Cap hit paragraph ("in one league year") and the Wilson film room | **league year** | Used from the first cap paragraph on. The reader only learns it "turns over in mid-March" from the Fig 5 caption, two pages later. 11-02 used it but never pinned it down. Gloss it at first use: "the NFL's business year, which starts in mid-March". |
| Fig 4 caption, "Middle: before year 3 the team **restructures**" | **restructure** | The caption defines it in passing, but the body only defines it under "Restructures and void years", after the figure. It's also in "You'll be able to" before any definition. This is minor because the caption works. |
| Fig 8 (evaluation card), "STAND-IN NUMBERS: 10-yd split, short shuttle, 3-cone" | **10-yard split, short shuttle, three-cone** | The card comes before "The combine and pro days", which explains them. A reader hits three unknown drills, then learns them a page later. Either move the card after the combine section or add a one-line pointer. |
| Fig 8, Edge card, "motor in the fourth quarter"; OT card, "hand timing"; WR card, "catch radius", "route craft: tempo" | **motor, hand timing, catch radius** | Scouting jargon that's never glossed. The text after the card glosses anchor, get-off, bend and processing but not these. |
| Fig 8, QB card: "hand size; little else" | **why hand size** | It's the only QB number, and the reader has no idea why it matters (grip, fumbles, weather). One clause would fix it. |
| Tags, "or the quarterback tag if that is higher" | **quarterback tag** | Never explained. Is there a separate QB tag price? The reader just learned that tags are priced by position, so this reads as a new rule. |
| Tags, "the average of the top cap numbers at his position (the top five, measured against the cap over recent years)" | **tag formula** | The parenthetical is opaque, and it differs from the glossary ("average of the top salaries"). Write either "the top five at the position, averaged over the last five years as a share of the cap" or just "roughly the average of the top five salaries". |
| Free agency, "usually after a two-day negotiating window" | **negotiating window / "legal tampering"** | Fans hear "legal tampering" on broadcasts. Name it. |
| Trades, "trades cluster around the new league year (when teams reset their caps)" and "why a team 'eats' money" | **reset their caps, eat money** | Neither is explained. "Reset" suggests the cap goes back to zero, which is wrong. "Eats money" is undefined: does the trading team pay salary, or take dead money? |
| Fig 5 caption, "trades become official"; Rams film room, "In March they made official the trade" | **agreed vs official trade** | Stafford was traded in January. Why does it become "official" in March? The reader needs one sentence: trades agreed after the season can't be processed until the new league year. |
| Draft value, "teams need a common price list… a trade that 'balances on the chart'" plus "board" in the scheme-fit section ("a first-round talent on one board") | **draft board** | It's familiar to many fans, but a one-word gloss costs nothing. |
| Positional value, "**premium positions**" | **premium positions** | Bolded like a defined term but not in the glossary or the term index. Either gloss it or unbold it. |

Terms the chapter correctly hands off: kick-slide, bull rush, head-up, two-gap/one-gap, 3-technique, reach,
down block, pull, press, off coverage and RYOE were all taught earlier and are linked. Good.

## 2. Leaps: a missing or assumed "why"

1. **The Fig 6 surplus curve contradicts the text, and the reader will catch it.** The text says, "The two
   curves agree on the order (an earlier pick is always worth more)". The blue curve in Fig 6 (top) drops from
   about 170 at pick 1 to **83 at picks 2-3, then rises to about 100 at picks 5-6**. So by the chapter's own
   curve, pick 3 is worth less than pick 6. The bottom panel shows the same dip in "value". Nothing explains it:
   small samples, QB busts at 2-3, smoothing? This matters most because Predict 2 is built on it (see §5).
2. **Predict 2's table undercuts its own answer.** The table gives surplus of **No. 12 = 3.3%** and **No. 3 =
   3.4%**. By the surplus chart, No. 12 is worth about 97% of No. 3. The answer then says, "Surplus value thinks
   No. 12 and No. 29 are each worth a large fraction of No. 3", which undersells its own numbers, and nowhere does
   it tell the reader that on this curve No. 3 is barely better than No. 12. A data-minded reader will ask: then
   why would anyone ever trade from 12 to 3? Either the curve's top-five behaviour is noise (say so, and say how
   many players stand behind it), or it's the finding (say so loudly).
3. **"When the disagreement doesn't matter"** is promised in "You'll be able to" (line 262) and never
   delivered. The only candidates are "they agree on the order and on the first pick" and the QB exception,
   but neither is framed as "when it doesn't matter". Add the sentence, or drop the clause from the objective.
4. **Why value is measured by the *next* contract.** The rookie produces during years 1-4, but "value" is what
   he's paid in years 5+. The implicit assumption (next-contract pay ≈ quality during the rookie deal) needs one
   sentence. Separately, the text never says why cost uses 2021-2025 contracts while value uses 2011-2020
   classes. The caption states it, but the "why" (recent classes haven't reached second contracts yet; old rookie
   costs are out of date) isn't given.
5. **Why normalize to "an average top-ten pick"?** The Fig 6 y-axis and the text both use it, but the reason
   (pick 1 alone is ten players, mostly QBs) is only in a code comment. Put it in the caption.
6. **The Wilson dead-money split.** The chapter teaches that a pre-June 1 cut puts all remaining proration on this
   year, and a post-June 1 cut splits current year and next. Denver released Wilson in March, yet the dead money
   was split $53M/$32M across 2024 and 2025. The footnote adds that a post-June 1 designation "would have produced"
   $35.4M/$49.6M. That's a third pattern the reader has no rule for. One sentence explaining why Denver's March cut
   still spread into 2025 (the guaranteed 2025 salary and offsets) would stop the reader from thinking they
   misunderstood June 1.
7. **The Eagles film room is self-contradictory without one more sentence.** "They *paid* for it" is immediately
   followed by "much of the talent was developed rather than bought: Kelce a sixth-rounder, Mailata a
   seventh-rounder". Then why is the line's share of spending so high? Presumably because they paid to *keep*
   the linemen they developed (second contracts for Kelce, Johnson, Mailata, Dickerson). Say that, or the
   lesson blurs.
8. **The waivers rule after the deadline.** "And, after the trade deadline, any player": why? The reason (so a
   contender can't sign a veteran a rival just cut, outside the trade rules) is the interesting part. The
   Beckham example is exactly this rule in action (released Nov 8, after the Nov 2 deadline), but the chapter
   doesn't connect them. It reads as if Beckham went through waivers by chance.
9. **Compensatory picks: why the league awards them, and how a team "games" them.** The text says a team can
   "avoid signing others' in order to collect picks", but never says that signing a UFA *cancels* one you lost
   in the formula. That cancellation is the whole mechanism behind the Ravens strategy.
10. **"Spread the cap cost over years when the cap will (usually) be higher."** Why is that good? Because a fixed
    dollar charge is a smaller *share* of a bigger cap. Spell it out. It's also why Purdy's back-loaded hits
    look less scary.
11. **The scheme-fit archetypes rest on hand-drawn regions, and the chapter's own data shrinks the effect.** Fig
    13's ellipses are "drawn by hand", and the 49ers film room reports the purest wide-zone team's linemen
    average 311 lb against a league average of 314. So is the 295-315 vs 315-340 split in Figs 10 and 13 real?
    The chapter half-concedes this ("rough tendencies"). A data-minded reader wants either a team-level check
    (wide-zone teams' drafted OL weight vs gap teams') or a clearer statement that the difference is about
    movement on film, not pounds. As written, Fig 13 shows the regions as if they were findings.
12. **Takeaways: "frees a fifth or more of the cap".** Never computed in the text. It's derivable from Fig 1
    (top-10 QB 22.4% minus a rookie's 0.4%), but say so where Purdy's window is discussed.
13. **"Picks gained value through the first round"** (Massey-Thaler) is counter-intuitive and gets no "why". The
    mechanism is that cost falls faster than expected production. The modern Fig 6 doesn't reproduce it either
    (blue falls after pick 6), so the reader is left holding two contradictory claims.
14. **The Purdy window is three years on a four-year contract.** The film room says "four-year rookie contract",
    and Fig 7 shades only 2022-2024. The answer is in the draft section ("cannot sign an extension until after
    their third regular season"), so link it: the window closes after year 3 *because* that's the first moment an
    extension is allowed, and a team extends its star QB at the first chance.

## 3. Diagrams I couldn't decode, or captions that don't say what to notice

- **Fig 6 (draft value), top panel:** see §2.1. The dip at picks 2-3 is the most visible feature after pick 1,
  and neither the caption nor the text mentions it. The orange "54" label at pick 16 sits on the orange line,
  and the "5" at pick 100 sits on the x-axis.
- **Fig 4, bottom panel:** the caption says the March cut "saves only $5 million of cap", but the panel doesn't
  show the year-3 cap hit the cut is being compared to (35). The reader has to scroll up to panel 1. A ghost
  outline of the as-signed year-3 bar (35) next to the red 30 would make "saves 5" visible.
- **Fig 9 (RAS), right panel:** the caption says "within a draft-round group the bars change only modestly",
  and the text says "a high score adds a little, not a lot". But rounds 1-2 go **50 → 65 → 61 → 71**, a
  21-point rise from the bottom to the top quarter. That isn't "modest" to anyone reading the bars. Either soften
  the claim, say it's noisy (n=29 in the bottom-quarter early group), or show uncertainty. As drawn, the figure
  argues *for* RAS more than the text admits. The figure also never shows the actual 0-10 score, only quarters,
  so "a 9 is elite" never connects to anything on the page.
- **Fig 10 (power panel):** the caption says "the right guard and tackle double-team the 3-technique", but RG and
  RT are unlabeled in that panel and the double team isn't visually distinct from the other blocks. Label RG
  and RT, or draw the double team as a bracket. The puller's path through the backfield is busy, but it reads.
- **Fig 12 (off zone):** the dashed green line from Q to the corner isn't explained in the caption. Is it the
  QB's eyes or the corner's? The caption says the *corner* watches the QB. Also, the receiver's go route ends
  well past the corner's arrow, so a beginner may read the picture as "the off corner gets beaten deep", the
  opposite of the Cover 3 rule taught in 06-03. Keep the corner's arrow level with or above the receiver's.
- **Fig 15 (roster):** the red arrow from "Signed through the season" to "Injured reserve" isn't explained in
  the caption. The "elevation" label sits on the 53-man box's top border. (This is cosmetic; the two don't collide
  as text.)
- **Fig 13 (archetypes):** the OL caption says wide-zone teams shop on "the left, low shuttle times", but the
  shuttle axis is inverted, so low times are at the *top*. Say "upper left (fast shuttle)". The Edge panel
  includes combine "OLB", which pulls in off-ball 4-3 outside linebackers. A reader can't tell, but it inflates
  the "stand-up" cloud.
- **Fig 3:** works. The caption tells you exactly what to notice. Best figure-caption pair in the chapter, along
  with Fig 4.
- **Fig 2:** works, but the ten tiny panels at print size are hard to read (6-7 pt). It's acceptable because the
  message is "all flat".

## 4. Drag and repetition

- **Length.** About 10,200 words against a 6,500 target. It's not padded sentence by sentence, but some sections
  could go: the full tag escalator (120%/144%), the minority-coach comp-pick rule, the exclusive-rights FA bullet,
  practice-squad veteran counts, and the Seattle 32-inch-arms aside are all fact-sheet detail with no "why"
  attached.
- **Purdy is told five times.** In the hook, the Fig 3 labels, the rookie-contract window, the film room (with a
  full cap figure), Predict 2's answer, and the emergency-QB rule. Each use is fair, but together they make the
  chapter feel like a Purdy feature, and the emergency-QB story needs no Purdy tie-in.
- **Predict 2 spoils itself.** It reuses *exactly* the Lance trade the reader read in the film room two pages
  earlier ("exactly what the 49ers sent Miami"), so the reader already knows the outcome (Lance bust, Purdy
  starter). Use an anonymized or different real trade-up (for example, the 2021 Bears 20→11 for Fields, or a
  trade-down), so the drill tests reasoning rather than recall.
- **"Price is not value"** is restated in the positional value section, the three-reason list, the QB paragraph,
  the misconception callout and the takeaways. Two statements would do.
- **The 04-07 overlap is a missed connection, not repetition.** 04-07's Purdy film room is the "system
  quarterback" debate. One clause here ("whether Purdy or Shanahan earned those numbers, 04-07, the cap didn't
  care") would tie the threads together.

## 5. Can I do each "You'll be able to…" item?

| Objective | Verdict |
|---|---|
| Rank positions by value using contract **and play-by-play** data | **Partly.** I can rank by *market price* (Fig 1). Play-by-play evidence exists only for QB (Fig 3). For edge vs RB vs LB, the "why" is argument, not data. Either soften the objective or add one play-level measure for a second position (for example, pressure rate vs edge spending, or RYOE spread vs WR). |
| Read a contract: cap hits, guarantees, dead money, restructure, void years | **Yes.** Fig 4 is excellent. I could reproduce the 35 → 19 restructure math. |
| Explain acquisition routes and their cost | **Yes**, at a definitional level, with the gaps in §2.8-9. |
| Price a pick two ways and explain why they disagree **and when it doesn't matter** | **Two of three.** I can price both ways (Predict 2), but the chapter never tells me when the disagreement doesn't matter, and the No. 3 vs No. 12 near-tie confused me. |
| What scouts grade; what the combine and RAS can and can't tell you; scheme fit | **Yes**, though Fig 9 made me think RAS matters more than the text says. |
| Follow roster moves: 53, 48, elevations, IR, emergency QB | **Yes.** It's clear. |

### Drills (attempted before opening the answers)

**Predict 1 (March squeeze).** My answer was: cut the RB (saves 12, at a low-value position), plus cut the LB
(saves 8, low value, age 30) to clear 14 with room to spare. The "obvious move to avoid" I named was **cutting
the QB**, the biggest single saving (18).
*Answer key:* cut the RB and restructure the QB; avoid cutting the LT.
*Problems:*
(a) The figure gives no base salaries, so I couldn't consider a restructure quantitatively. The answer invents
"$25 million of next year's base salary". Either add a base-salary column, or state the QB's base in the prompt.
(b) "Which obvious move does it avoid?" is ambiguous. With a "saves 18" label at the top of the chart, the QB is
the obvious tempting cut, not the LT. Either name the LT in the question ("Someone suggests cutting the left
tackle…") or have the answer address the QB too.
(c) The answer says the RB cut "alone nearly solves the problem" and calls the S/LB cuts moves "if the team needs
more room". But it *does* need more room (12 < 14). The answer should explicitly compare restructure + RB against
RB + LB, and name the cost of the restructure: it adds future dead money to a QB already carrying $34M.
**Partly got it.** The drill is solvable in spirit but underspecified.

**Predict 2 (trade-up).** Johnson: 2,572 vs 2,200, so the 49ers overpaid by about 17%. Surplus: 9.5% vs 3.4%, so
they paid about 2.8 times what they got. The QB exception makes it right. **Got it fully**, but only because I'd
just read the outcome in the film room (§4). And I was distracted by No. 12 = 3.3% vs No. 3 = 3.4% (§2.2).

**Predict 3 (which guard).** Prospect B, the quick, lighter guard, for an outside-zone team. **Got it in under
10 seconds.** The caption says "outside zone" and the diagram is a near-copy of Fig 10's left panel, so it's a
recall check, not a prediction. To make it harder, don't name the run in the caption (make the reader identify
outside zone from the first steps), or give Prospect B a real cost the team must weigh, such as a pass-pro grade.

## 6. What I still wonder (gaps this chapter should answer)

1. **How do I actually read an Over the Cap team page?** The cap check sends me there, but doesn't tell me which
   columns map to "cap hit", "dead money if released" and "cap savings" (OTC labels them "Cap Number", "Dead
   Cap", "Cap Savings", with pre- and post-June 1 views). One screenshot-style mock row would make the Sunday
   checklist doable.
2. **Cap space and carryover.** Can a team roll unused cap into next year? (Yes, carryover.) It's crucial to why
   some teams "bank" space, and it's never mentioned.
3. **The salary floor / minimum spending.** Is there a minimum? Could a team spend 50% of the cap and pocket the
   rest?
4. **PUP and NFI lists, and "designated to return".** Broadcasts mention them, and the roster section stops at IR.
5. **Why do players accept restructures and void years?** Answered briefly (cash sooner, guaranteed), but is
   there any downside for the player? And why does the league allow void years at all?
6. **Rookie QB timing:** does a team gain anything by extending early versus waiting a year on the fifth-year
   option? The chapter shows Purdy's window closing, but not the choice of *when* to close it.
7. **Is there a real test of scheme fit in the data?** (See §2.11.) Do wide-zone teams draft measurably lighter
   or quicker linemen?
8. **Positional value beyond QB, with data:** does pressure rate track edge spending? Does pass-block win rate
   track OL spending? Even a short "we checked one more position" would back up the ranking.
9. **The Fig 6 dip at picks 2-5:** is it real (QB busts at 2-3?) or noise?

## Priority fixes (for the author)

1. Fix or explain the Fig 6 surplus dip, and reconcile the "earlier pick is always worth more" claim and the
   Predict 2 answer wording with the 3.3% vs 3.4% table.
2. Make Predict 1 solvable: add base salaries or state the QB's base; disambiguate the "obvious move"; compare
   restructure + RB with RB + LB.
3. Replace Predict 2's Lance trade with a trade the reader hasn't just read about. Make Predict 3 harder.
4. Fig 9: bring the caption and text in line with the 50 → 71 bars, or show uncertainty.
5. Deliver "when the disagreement doesn't matter", or cut it from the objectives.
6. Gloss league year, quarterback tag, reset caps / eat money, and official trades. Move Fig 8 after the
   combine drills or point forward.
7. Add the one-sentence whys: the Eagles' second contracts, the waivers-after-deadline reason (tie it to
   Beckham), comp-pick cancellation, Wilson's split, next contract as the value measure.
8. Trim toward the target length (tag escalators, the minority-coach rule, practice-squad veteran counts).

---

## Revision (2026-10-08)

Addresses this review and `14-01-coach.md`. Re-rendered with `build_pdfs.py 14-01-building-a-roster --html` (OK, 0 errors, 26 pp.). Every figure page was rasterized and checked; Figs 4, 6, 9, 10, 11, 12 and 17 were checked again at 110–130 dpi after the fixes. Footnotes: each is referenced exactly once (script check).

### Beginner review

| Finding | Action |
|---|---|
| §1 league year | Glossed at first use ("the NFL's business year, which starts in mid-March") in "The cap is hard". |
| §1 restructure before definition | Kept as is. The Fig 4 caption defines it, and the body defines it in the next paragraph. |
| §1 Fig 8 drills before the combine section | Caption now says the drills are explained in the next section. |
| §1 motor, hand timing, catch radius; why hand size | Glossed in the paragraph after Fig 8. The QB card now reads "hand size (grip in cold, wet weather)". |
| §1 quarterback tag / tag formula | Tag escalator sentence cut (drag), so "quarterback tag" is gone. Formula is now "roughly the average of the five largest cap numbers at his position", in both the body and the glossary. |
| §1 legal tampering | Named in the UFA bullet. |
| §1 reset caps / eat money / official trades | Rewritten. "Ate money" = took a dead-money charge so the other team would take the player. Trades cluster in March because a trade agreed after the season can't be processed until the new league year. The Fig 5 caption says the same. |
| §1 draft board | Glossed in the draft-chart section. |
| §1 premium positions bolded | Unbolded (plain words). |
| §2.1 / §2.2 / §6.9 Fig 6 dip and "earlier is always worth more" | Claim removed. Text, caption and an on-chart note now say the 2–3 dip is 20 players (6 QBs, 7 paid less on their next deal than as rookies), i.e. noise. The finding is that surplus is roughly flat from pick 2 to the mid-teens. Predict 2 was replaced (below), so the 3.3% vs 3.4% table is gone. |
| §2.3 "when the disagreement doesn't matter" | Delivered as a paragraph: at No. 1, and for a QB the team is truly sure of. Everywhere else (multi-pick and future-first trades) it decides who won. |
| §2.4 why the next contract; why two cohorts | Two sentences added. The next contract is the market's summary after 32 teams watched four years. Value comes from the 2011–20 classes (later ones haven't reached a second deal yet); cost comes from 2021–25 contracts (today's prices). |
| §2.5 why normalize to the top ten | Now in the Fig 6 caption. |
| §2.6 Wilson split | Film room rewritten. The release carried a post-June 1 designation, and Denver chose to put the larger $53M part on 2024. "Why March": $37M of future salary would have become fully guaranteed on day 5 of the league year (PFT). **Fact-check note:** the factcheck log removed the post-June 1 claim, but its own source (AP via KOAA) says "He was given a post-June 1 designation". The text now follows AP. The plain post-June 1 split ($35.4M/$49.6M) is in the footnote as reported. |
| §2.7 Eagles contradiction | Added. The high spending is the price of *keeping* what they developed: second contracts for Kelce, Johnson, Mailata and Dickerson (OTC via nflverse). |
| §2.8 waivers after the deadline | Reason added (so a contender can't use a rival's release to dodge the deadline), tied to Beckham in the Rams film room. |
| §2.9 comp-pick cancellation | Added. Signings cancel losses, roughly by size, and released players count on neither side (NFL.com, new `[^compnet]`). |
| §2.10 why spreading the cap cost helps | Added: a fixed charge is a smaller share of a bigger cap. |
| §2.11 / §6.7 scheme-fit archetypes are hand-drawn | Text now says the regions are a picture of the idea, not a finding. Added a team-level check (computed in code): OL drafted 2017–25 by Shanahan-tree offenses (SF, LAR, GB 2019+, MIA 2022+) average 311 lb and a 4.67 s shuttle (n=40), against 314 lb and 4.73 s for everyone else. The archetype is real but faint. |
| §2.12 "a fifth of the cap" | Derived in the Purdy film room: a top-10 QB is about 22% of the cap (Fig 1) against Purdy's under 0.5%. |
| §2.13 Massey–Thaler "gained value" | Why added (cost fell faster than expected production). Reconciled with the modern curve: the wage scale removed that effect. |
| §2.14 three-year window | Window paragraph explains it closes after year 3, because that is the first extension date. Purdy, a 7th-rounder, had no fifth-year option (also coach #10). |
| §3 Fig 6 labels | Orange labels moved below-left of the line; "5" at pick 100 moved off the axis. |
| §3 Fig 4 bottom | Dashed ghost bar for the as-signed year-3 hit (35) plus the note "if kept 35 / cut 30 dead / saves only 5". Caption updated. |
| §3 Fig 9 "modest" vs 50→71 | Added 95% intervals and score ranges per quarter on the axis. Caption and text now give the 71% vs 50% numbers, the n (62 vs 26) and the ±19-point uncertainty. The reading: athleticism helps a little after the draft order, but the size is uncertain. |
| §3 Fig 10 RG/RT unlabeled, double team | RG and RT labeled in both panels. The double team and the RG coming off to the Will are drawn. Kick-out label moved off Y's line (see coach #2–3). |
| §3 Fig 12 dashed line; corner beaten deep | Panel replaced with a Cover 2 squat corner (coach #1). Caption says "the dashed line is his eyes, on the quarterback", and a "safety takes him deep" label covers the go route. |
| §3 Fig 15 red arrow; elevation label on border | Caption explains both arrows. Elevation label moved above the practice-squad box. |
| §3 Fig 13 "left, low shuttle"; OLB in edge | Caption now says "upper left: the shuttle axis is flipped". The edge panel keeps DE/EDGE plus only combine OLBs with 10+ NFL sacks. |
| §3 Fig 2 small panels | Kept. The message is "all flat", as the review says. |
| §4 length | Cut the tag escalator, the minority-coach comp rule, the exclusive-rights bullet, the practice-squad veteran count, the Seattle 32-inch detail (footnote kept), the Snead T-shirt aside, the waiver-priority aside, the fantasy paragraph (its 14-02 link moved to the new Graham paragraph), the Madden "read this chapter" line and the duplicate draft caveat. Predict 1's answer was tightened. **Partly declined:** the two reviews asked for about 30 additions (whys, nuance, new examples). After the cuts the chapter is about the same length as before (≈10,500 prose words), not 6,500. Cutting further would remove the whys the reviews asked for. |
| §4 Purdy five times | Removed from the emergency-QB story (now "San Francisco lost its starter… then its backup"). Predict 2 no longer uses the Lance/Purdy trade. |
| §4 Predict 2 spoils itself | Replaced with the 2021 Bears–Giants trade-up (No. 20 + No. 164 + 2022 1st + 2022 4th for No. 11; nflverse `load_trades()`). Future picks are priced as mid-round at draft time. The answer adds the hidden risk: the 2022 first became No. 7 (Chicago won 6 games), which makes the real cost about 2.0× No. 11 on the Johnson chart. Fields was later traded for a conditional 6th. |
| §4 "price is not value" restated | Left in the spending section, the QB paragraph and the takeaways. The misconception callout makes a different point (price vs whether a position matters). |
| §4 04-07 connection | Added in the Purdy film room ("the cap didn't care"). |
| §5 objective 1 (play-by-play beyond QB) | Objective softened: rank by contract data; use play-by-play for the QB price-vs-play contrast. A second position's play-level measure was declined for length. |
| §5 Predict 1 underspecified | The caption gives the QB's base ($40M) and proration ($12M, 3 years left; dead money now 36). The question names both tempting cuts (QB and LT). The answer compares RB+LB ($20M, the cheap answer) with RB plus a QB restructure ($20M, at a future cost), names that cost, and adds the top-51 and June-2 timing points. |
| §5 Predict 3 too easy | The caption no longer names the run; the reader must identify outside zone from the first steps. Prospect cards add pass-pro grades. The question also asks what choosing B costs and how the team covers it, and the answer addresses that. |
| §6.1 reading an OTC page | The Watch-for-it callout now maps OTC's "Cap Number" and "Dead Money & Cap Savings" (Cut pre-/post-June 1) columns (checked on the live OTC team page). |
| §6.2 carryover | Added with the top-51 rule (CBA Art. 13 via OTC, new `[^cbacap]`). |
| §6.3 salary floor | Declined. No source in hand for the current minimum-spend rule, and it isn't needed for the chapter's argument. |
| §6.4 PUP / NFI | Declined for length. It belongs with roster rules, not the chapter's core. |
| §6.5 why players accept restructures; why void years are allowed | Added one clause each (dead money = job security; void years move charges without erasing them). |
| §6.6 extend early vs option | Partly covered (why teams extend at the first chance). The full timing trade-off was declined for length. |
| §6.8 positional value beyond QB with data | Declined (see §5). Added the data point that 4 of the 10 richest tackle deals are right tackles. |

### Coach review

| Finding | Action |
|---|---|
| MUST 1 press ≠ man; Seattle was press Cover 3; Fig 12 | Corner section rewritten: the split is by technique, not man vs zone. Seattle is now "the league's signature press Cover 3" (links 06-01). The off example is the Cover 2 squat corner and Ronde Barber, 5-10 (Pro Football HOF, new `[^barber]`; links 06-04 `#gl-squat-corner`, `#gl-tampa-2`). Fig 12 right is coach Option A: CB six yards off with outside leverage, sinks, drives on the flat throw, flat zone drawn, safety over the top. |
| MUST 2 Fig 10 OZ: Sam unblocked | Redrawn per the coach's rules: C+RG combo the 3 (C climbs to the Mike), RT to the Sam, Y reaches the 9, LG cuts off the 1, LT climbs to the Will, backside 5 left (said in the caption). Fig 17: C combos the 3 and climbs to the Will, RT to the Mike, FB on the Sam, and the answer text describes the combo. |
| MUST 3 Fig 10 power: Will unblocked; kick-out label | RG comes off the double to the Will. The FB ends at the 9's inside hip with a block bar. The "F kicks out the 9" pointer sits below the LOS; a "Y up to the Sam" label was added. |
| MUST 4 RT dropped from Fig 1 | `MKT_GROUP` maps LT and RT to "Offensive tackle" (9.9%). The text is updated: "offensive tackles" in the tier sentence and the glossary, plus a blind-side sentence backed by data (4 of the 10 richest tackle deals are RTs). |
| MUST 5 OLB in the Fig 13 edge panel | Edge = DE + EDGE + OLBs with 10+ NFL sacks (nflverse draft data). The caption says so and also says why the "DL" label is excluded from the interior panel. |
| 6 weight ranges | 4-3 DE 255–280. 3-technique 285–315 (caption and archetype ellipse). Added the nickel reality: base personnel on only 29.7% of 2025 snaps (NGS via NFL.com, `[^base]`). |
| 7 tite fronts; Davis/Carter | Paragraph added after Fig 11, linking 05-03's tite front. Davis No. 13 2022 (341 lb) and Carter No. 9 2023 (314 lb) verified in nflverse draft and combine data (`[^phidl]`). |
| 8 duplicate "B" labels | 3-4 OLBs labeled "E" (stand-up edge, as in 05-03), explained in the caption. Library note: gridiron's default OLB label "B" still duplicates. Not edited here. |
| 9 Eagles overstatement; Stoutland; title | Lane Johnson No. 4 (2013), Dickerson and Jurgens (2nd round) added, all verified in nflverse. Stoutland added, **with a correction to the review**: he left in February 2026, so the text says "2013 through the 2025 season" (NFL.com, `[^phiol]`). Callout titles are now "Film room: Philadelphia Eagles, 2014–2025", "San Francisco 49ers, 2017–2025" and "Denver Broncos, 2024". |
| 10 Purdy / no fifth-year option | Added. The proven-performance escalator was declined (optional, unverified). |
| 11 tag by CBA position bucket; Jimmy Graham | Graham 2014 paragraph added (about $7.0M TE vs $12.3M WR tag; the arbitrator ruled him a TE; NFL.com and SI, `[^graham]`). It also carries the 14-02 forward link. |
| 12 top-51, June 2, carryover | All three added in the June 1 section (CBA Art. 13 §6, `[^cbacap]`). The Drill 1 answer uses top-51 and June 2. |
| 13 Wilson $37M vesting | Added ("Why March"; PFT). The benching backdrop was not added (not needed). |
| 14 comp formula: expired vs released | Added (`[^compnet]`). |
| 15 scouting card | IDL proxy adds arm length. CB traits add hip turn and run-support tackling. OT feet = "pass sets (kick-slide, jump sets)". |
| 16 takeaways order | Reordered to match Fig 1 (edge, WR, then IDL, CB, OT). The Watch-for-it list was updated the same way. |
| 17 "roughly 24 jobs" | Now "about 25". |
| Nit: Miller date | Now "At the trade deadline" (footnote keeps nflverse's Nov. 2). |

New facts and their sources: Wilson post-June 1 and $37M vesting (AP/KOAA; PFT); top-51, June 2, carryover (CBA Art. 13); Graham grievance (NFL.com, SI); comp-pick netting (NFL.com); Barber 5-10 (Pro Football HOF); Davis/Carter, Johnson/Dickerson/Jurgens, Bears–Giants trade, Fields trade (nflverse); Stoutland tenure (NFL.com); base-defense share (FACTS-current §10, NFL.com); OTC column names (live OTC team page). Fact-check items left intact apart from the Wilson correction above; removed items (minority-coach rule, tag escalators, Snead T-shirt, waiver-priority aside) were cut, not changed.
