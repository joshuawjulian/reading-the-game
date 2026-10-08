# 13-03 Win Probability and Decision Analysis: beginner-reader review

Reviewer persona: a casual NFL fan who has never played, is comfortable in Python, and has read every
chapter before this one in curriculum order (including 01-06 broadcast WP bar, 09-01 icing, 10-03 two-point
plays and tush push, 10-04 fourth-down heuristics and two-point chart, 11-04 Belichick 4th-and-2, 13-01,
13-02 EP/EPA/log loss). Read start to finish from `pdfs/13-03-win-probability-and-fourth-down.pdf`
(39 pages, built 2026-10-08 08:37, after the last .qmd edit), with figures checked at 90-200 dpi.

**Overall:** This chapter is strong and it delivers what it promises. The random-walk model is a
real "aha", the Lions decision tree (Fig 7) is the best figure in the chapter, and the two-point
formula really can be worked by hand. The problems are a print-rendering bug in two equations, one
internal contradiction, a confusing double use of "down 8", an ambiguous unit ("pts"), a heatmap the
reader can't fully decode, and a lot of drag: about 8,700 prose words against the 5,500 target, plus
about 830 lines of code. Pages 14-20 are almost all code.

---

## 0. Must-fix (defects, not taste)

1. **Equations render broken in the PDF (p.4 and p.30).** In `WP = \Phi\!\left(...\right)` (qmd l.208)
   and `k \cdot \max\!\left(...` (l.1305), the `\!` negative space makes the big left parenthesis
   overprint the Φ and the "max". In print it reads as "WP = (Φ lead+EP / σ√(t+τ))" and "k · ma(x k/2, p)".
   Drop the `\!` (or use `\Phi\left(`).
2. **The chapter contradicts itself about the NFC Championship decisions.** On p.21 (l.914-916):
   "fourth-and-3 at the 30 ... our model says go by 6.7". On p.29, in the Lions film room (l.1268-1270):
   "the two decisions from the NFC Championship Game ... were, by every model, among the *closest*
   calls he made." 6.7 points is not close, and the chapter's own grading would call it a clear go.
   Change it to "by the published models (ESPN, NGS)", or deal with the gap directly.
3. **"46%" shows up before it is computed.** p.18 (l.801): "into 'do we convert more than 46% of the
   time here?'" comes before the Lions example that produces 46%. On first read I didn't know where the
   number came from. Either say "...more than p* here?" or move the sentence after the table.
4. **"Down 8" means two different things.** In the section title "Two-point decisions: down 14, down 8"
   and in l.1367 ("if you score a touchdown when trailing by 8, you are down 2"), down 8 means trailing
   by 8 *before* scoring. In Fig 12, though, the title is "Down 8 after the touchdown" and the caption
   says "trailing by 8 right after a touchdown (the down-14 situation)". The drill 3 title is "Down 8
   after the TD". I had to reread three times to work out that Fig 12 measures the down-14 decision.
   Rename Fig 12 to "Down 14, then a touchdown: going for two", or something similar.
5. **"pts" is ambiguous throughout.** In this chapter football points and percentage points of WP sit
   in the same sentences. Examples: "Our model says punt, by about 2 points" (p.24, l.1033); code
   outputs "gain +2.9 pts"; the column header "gain from going (pts of %)"; "go wins by 0.9 pts of WP".
   It is never stated once that "a point of win probability = one percentage point". Define the unit
   once, early (WPA section), and use a single label everywhere ("pp" or "points of WP").

## 1. Terms used before they are explained, or never explained

- **Point spread / betting line / "favoured by about three points"** (p.6-7, Fig 4 caption, misconception
  callout). This is the central input of `vegas_wp`, but this chapter never glosses it. 01-06 touches it.
  Add a one-liner ("the betting market's predicted final margin") and a back-link.
- **Icing the kicker** (l.1424) is bolded and defined again as if it were new, but 09-01 taught it
  (09-01 l.747). Link back instead.
- **"random forest", "generalised additive model"** (l.339-341). These are name-dropped in the history
  paragraph. The data-science reader can cope, but they add nothing. Either one clause each saying what
  changed, or cut them.
- **The "1 − wp_model(−lead, ...)" trick.** All of `decide()` depends on "the opponent's WP from its
  side, flipped". The prose never says this. The reader first meets it inside code at l.769-783. Add one
  sentence before the decision function.
- **"eight in the box"** (drill 1 prompt, l.1507). In Fig 13 the SS is about 7-8 yards deep and outside
  the tight end. Using the 02-05 box definition I count 7 (E T N E S + W M). Either move the SS down or
  say "seven in the box plus a rolled-down safety".
- **"coin flip on expected points"** (l.1276-1277) is used for 0.96 vs 0.94 points. "Coin flip"
  suggests 50%. Say "almost exactly equal in expected points".

## 2. Leaps (a missing "why")

1. **Why the fitted σ comes out larger than the raw spread** (p.6, l.251-253): "a model judged by how
   well it predicts wins prefers to be slightly less sure ... (a theme that returns below)". This is
   asserted, never shown, and the "theme" never clearly comes back. Either give one sentence on why
   (log loss punishes confident misses, and the last-minute lumps inflate the tails) or cut it.
2. **Fig 4: why does Atlanta start at about 57% when New England was favoured?** The solid line starts
   above 50% and the spread line well below. The likely reason is that nflverse `wp` gives home field to
   the designated home team even at a neutral site, but the text never says so. This is the chapter's
   own misconception callout ("one of them knows who is favoured") in action, and it goes unremarked.
3. **The break-even map is not monotone, and the text says it is.** "The break-even rate falls as you
   approach the end zone" (l.994). Fig 8 (top) jumps from 29 at the opp 40 to 36 at the opp 35, which is
   exactly where the black punt/FG line sits. The reason (once a field goal is available, the kicking
   option is worth more, so the bar rises) is never stated. A reader who checks the map against the
   text will think one of them is wrong.
4. **The "go zone" at the opp 30-40 isn't visible on the map.** The deepest blue on Fig 8 is at the opp
   5-15, at every distance. The 30-40 band is pale to light blue at 4th-and-4/5. Either show why 30-40 is
   special (the gain value, not just the colour) or soften the bullet.
5. **Grading uses the model in situations the chapter just showed it gets wrong.** The 7:38-left,
   down-3 Lions decision has our model at +6.7 against ESPN's +0.3 (p.21). Then the coach-grading cuts
   off only the last *five* minutes (l.1047, l.1143). Drill 2 (6:30 left, down 4) answers "Go, clearly"
   with the teaching model at +11.6. The reader who just learned "simple models are weakest in the
   fourth quarter" will distrust both. Either justify the 5-minute cutoff with data (e.g. calibration by
   minutes left) or cross-check drill 2 against a published model.
6. **Fig 10's "the two measures line up" is partly mechanical.** WP given up on clear mistakes is
   mostly WP given up by *not going* on clear-go downs, so the correlation is built in. Say so, and say
   what is *not* tautological (e.g. teams that went more didn't pay for it in clear-kick spots).
7. **The size of the 5.0 vs 3.0 WP-per-game numbers is unexplained.** Romer (quoted on p.26) estimated
   about 2 points of win probability a game from going more often. This chapter says 5.0 per game lost
   in 2016. "Somewhat more aggressive than published models" doesn't reconcile a factor of 2.5. One
   sentence comparing the two, or a cross-check against nfl4th, would help. Also: 35% of *all* fourth
   downs are "clear go" in this model. Is that what nfl4th says?
8. **"Often worth taking the 5-yard penalty instead" of burning a timeout** (l.1420-1421). The timeout
   is priced (about 1.7 points); the 5 yards never are. The machinery is right there (`ep1`, `wp_model`).
   Price it in one line or soften the claim.
9. **The conversion model ignores field position.** Drill 2 uses the league-average 4th-and-3 rate (about
   52%) at the 8-yard line. 10-03 taught me the red zone compresses the field. Does conversion drop
   there? The "this team, this play" uncertainty section is the natural place for one sentence on this.
10. **Brill-Yurko-Wyner's result is given no number** (l.1089-1093): "far larger than ... graphics
    imply." A data reader wants an order of magnitude (e.g. a typical interval width on a "+3%" call).
11. **SB LI film room: why not kick right away?** "A field goal would have made it 31-20" (l.497) made me
    ask why they didn't just kick on first down. The point (run three times, burn NE timeouts, *then*
    kick) only arrives obliquely three sentences later. Lead with it.

## 3. Diagrams and captions

- **Fig 8 (recommendation map), the hardest figure.** (a) No colourbar, so "blue = go by how much?" can
  only be learned from the caption's ±6. (b) The number in each cell is the break-even rate, but the
  thing to compare it with (P(convert) for that row) isn't on the figure, so the reader has to flip back
  to Fig 6. Add a narrow right-hand column with P(convert) per row, or print the gain in the cell and
  break-even only in selected cells. (c) The 5.6-pt numbers are tiny in print. (d) The caption calls it
  a "black step line", but in both panels it is a straight vertical line. (e) The caption should tell me
  what to notice: the jump at the punt/FG line, and the near-flatness of break-even down each column.
- **Fig 7 (decision tree)** is excellent. One nit: the caption says "the markers show where each branch
  leaves the ball", but only the LOS and the FG spot have markers. "convert ... SF 23" and "fail ...
  their 28" are free-floating text, and the fail label sits at the bottom edge, away from the ball.
- **SB LI WPA table (p.11).** The pick-six row reads "Q2 2:36 NE: Brady pass short left intended for
  80-D.Amendola ..." and the truncation removes "INTERCEPTED", so I couldn't match it to "Alford's
  pick-six" in the text. There is no score column, so "at 0-0 and 14-0" can't be checked. The row "Q2
  15:00 Brady deep to Edelman, +10.1" (a 27-yard completion at 0-0) is the third-largest swing of the
  first half and goes undiscussed. The header "NE WPA (pts of %)" wraps into a stray "%)" line.
- **Fig 4 (SB LI).** Good. The two "8:31" labels (Q3 TD, Q4 strip-sack) look like a typo even though they
  are correct; add "(the same clock time, one quarter later)". The caption could say the strip-sack moved
  WP only from about 99% to about 96%, which is the point of the "decayed slowly" paragraph.
- **Fig 1 caption vs text.** The caption says "a constant 1.85 points per square-root minute" and the
  text says the median is 1.83. Pick one number.
- **Fig 9 title "Coaches moved toward the model, about halfway".** Going from 19% to 41% on clear-go
  downs is not halfway to 100%. Use "...from one in five to two in five".
- **Drill figs 13 and 15: the yellow line runs through defender labels.** In Fig 13 the line to gain sits
  exactly on the defensive front and the pressed corners (C, E, T, N, E, S boxes all bisected). In Fig 15
  the goal line runs through C, $, C. This breaks the no-collision rule. Nudge the defenders, or draw the
  line under the markers.
- **The drill pictures carry no decision-relevant information.** None of the three answers uses anything
  in the diagram (drill 1 even says "the eight-man box doesn't change the answer much"). A pre-snap
  picture should matter. Ideas: drill 1, ask *which* play to call against this box; drill 2, show a goal-line
  look and ask whether the league-average conversion rate is fair here.

## 4. Drag and repetition

- **Length:** about 8,700 prose words (including captions) against the 5,500 target, plus about 830 code
  lines. In print, pp.14-20 are about 80% code. Pure presentation code is the drag, not the modelling:
  `tbox`/`tarrow` and the 70-line Fig 7 cell, the heatmap text loops, the `LABEL` offset dict for Fig 10,
  `md_table`, and `short_desc` regexes. Fold or hide the plotting cells. Keep `wp_model`, `decide`, the
  ingredients, the grading and the two-point functions visible.
- **Repeated three times:** the fourth-down rules of thumb (map bullets l.989-1000, Watch for it
  l.1464-1467, Takeaways l.1645-1647). The down-14 logic (section, Fig 11 caption, answer 3, near-verbatim).
  The "teaching model, treat with caution" disclaimer.
- **The WP model history paragraph** (l.338-344) is a citation list with little payoff for the reader.
  Compress to two sentences.
- The "Two honest caveats" paragraph and the overtime caveat in the Data section say the same thing
  about the 2025 OT rule.

## 5. Can I do the "You'll be able to..." items?

| Item | Verdict |
|---|---|
| Explain WP, fit a simple one, differ from nflverse/betting line | **Yes.** The random walk plus the score table make this clear. |
| Read a WP chart, compute WPA, use leverage | **Yes** for WPA and leverage. Reading the SB chart was hampered by the unexplained 57% starting point. |
| Build a fourth-down tree, compute break-even | **Yes.** From Fig 7 by hand: (93.7−90.6)/(97.3−90.6) = 46%. Matches. |
| Work down-14 by hand; say when going early is right | **Mostly.** I computed 46.5% vs 58.9% from the formula with k = .944, p = .478. "When early is right" is answered only under "two TDs, nothing else, 4th quarter". Nothing on down 14 in Q2-Q3. |
| Critique calibration, failure modes, uncertainty | **Partly.** Calibration and bootstrap: yes. Model uncertainty: only qualitative (no Brill number, no nfl4th cross-check). |
| Measure coaches' changes | **Yes**, via the code. |

**Predict-the-play, attempted before opening answers:**

1. *4th-and-1, own 34, Q1 tie.* My call: **go**. Break-even of about 48% (read off Fig 8 at the own 35);
   P(convert) about 67% (Fig 6). Behaviour guess: about 10% in 2016, about 50% in 2025.
   **Answer:** go, 48%, 67%, 4% then 61%. Call correct. The behaviour sub-question can't be answered
   from the chapter body (no own-territory go-rate data appears before the answer). It's a guess, not a
   prediction.
2. *4th-and-3 at opp 8, down 4, 6:30.* My call: **go**. Break-even of about 25% (the trailing case is only
   described, "the blue spreads", not mapped, so I extrapolated). Tied Q1: still go, about 25% (top map,
   opp 10/5).
   **Answer:** 22% and 25%, go by 11.6 vs 4.4. Correct. My unease: the model the chapter just called
   weakest in the fourth quarter says "Go, clearly" with no cross-check.
3. *Down 14 → 22-14, 9:00 left.* My call: **go for two**, about half of teams do. **Answer:** correct, but
   it is a direct re-read of Figs 11 and 12. No new reasoning is required.

Net: the drills are passable but easy. Two of three repeat a figure, and the pictures are decorative.

## 6. What I still wonder (knowledge gaps this chapter should close)

- **The two-point chart from 10-04, through WP.** Up 5 after a TD (go to 7?), down 2, down 10, down 9.
  The chapter does down 14 only. The "down 8" half of the spec is reduced to "no decision".
- **How the 2025 OT rule changes the down-14 math.** The chapter says a tie is possible and both teams
  possess, but doesn't plug a non-50% OT value into the formula (the `ot=` argument is right there).
- **Timeouts: the decisions themselves.** When should a defense trailing late use its timeouts? When
  should a team let the opponent score? When should it kneel? The section prices a timeout as a
  regression coefficient and then mostly talks about icing. There is no figure, and the "pricing the
  clock" promise is thin.
- **How to adjust P(convert) for *this* team in practice.** The chapter says "that's the coach's job".
  A data reader wants a method (team short-yardage rates with shrinkage, tush-push conversion rates for
  PHI or BUF, kicker-specific FG curves).
- **What did nfl4th actually say** about the drills and the Lions/Belichick decisions? An `eval: false`
  cell calling nfl4th, or quoted numbers, would anchor "our model is more aggressive".
- **How broadcast WP bars differ** (ESPN, NGS, Amazon). How can I tell on Sunday whether the bar knows
  the spread?
- **Why 4th-down conversion barely depends on field position**, if it doesn't (goal-to-go,
  compressed red zone).

---

## Revision (2026-10-08)

Revised against this review and `13-03-coach.md`; fact-check rows left intact. New factual claims are sourced (new
footnotes `lionsdrop`, `doubleice`; `brill` extended with the v6 section-4 numbers) or computed in shown code
(nflverse pbp, FTN `is_qb_sneak`, 2009 pbp for the Colts' timeouts).

### This review

| Finding | Action |
|---|---|
| 0.1 `\!` breaks Φ( and max( in print | Removed both `\!`; both equations checked in the PDF (pp. 4, 28). |
| 0.2 "by every model, among the closest calls" contradicts +6.7 | Film room now: close by the published models (ESPN, NGS); this chapter's model, weakest in Q4, called the second a clear go (now +7.3 after the red-zone change). |
| 0.3 "46%" before it is computed | Now "more than $p^{*}$ of the time". |
| 0.4 "Down 8" used two ways | Section "down 14 and down 8"; "Down 8 before you score" paragraph; Fig 12 retitled "Down 14, then a touchdown…" with a caption that says "cut their deficit to 8"; drill 3 title "Down 14, then a TD". |
| 0.5 "pts" ambiguous | Defined the **WP point** once (WPA section); every output, header, caption and sentence now says "WP points"; bare "points" means the scoreboard. |
| 1 Point spread never glossed | Glossed at first use ("the betting market's forecast of the final margin") with a link to 01-06. |
| 1 Icing re-defined | Now a link back to 09-01, not a bold definition. |
| 1 Random forest / GAM name-drops | History paragraph cut to two sentences, no method names in the text (still in the footnote). |
| 1 The `1 − wp_model(−lead, …)` trick | One paragraph before `decide()` explains it. |
| 1 "Eight in the box" didn't match Fig 13 | SS moved to d=5 on the TE's outside shoulder, FS to 9.5; caption says so. |
| 1 "Coin flip on expected points" | Now "almost exactly equal in expected points". |
| 2.1 Why fitted σ > raw spread | Two reasons given (late-game lumps; log loss's asymmetry, with a worked 2% vs 20% number). "Theme that returns" cut. |
| 2.2 Why ATL starts at 57% | New paragraph after Fig 4: nflverse `wp` gives home field to the designated home team at a neutral site; the spread line starts at 39%. Ties to the misconception callout. |
| 2.3 Break-even map not monotone | Bullet rewritten: the bump at the punt/FG line explained (a field goal is a better consolation, so the bar rises 31%→34%); flat down each column. Caption tells the reader to notice both. |
| 2.4 "Go zone" at opp 30-40 not visible | With the new red-zone term the deepest blue at long yardage *is* at the opp 40; bullet re-anchored there with computed gains (4th-and-4 +3.2, 4th-and-7 +1.5). |
| 2.5 Grading uses the model where it was shown wrong | New log-loss-by-minutes table (2025): ours within ~1.5% of nflverse in every band, so the failure is in *comparisons*, not averages; cutoff called a judgement; grading re-run with a 10-minute cutoff and a 2-point threshold (robustness table). Drill 2 answer now leans on the size of the gain (≈9 WP pts, beyond Brill et al.'s 4-point "almost always clear" mark). |
| 2.6 Fig 10 slope partly mechanical | Said so (99% of WP lost comes from not going); the non-tautological finding added: no team lost more than ~0.09 WP pts/game by going when it should have kicked. |
| 2.7 5.0 vs Romer's ~2 | New paragraph: different yardsticks (Romer EP, early-game; ours WP, three quarters), our model more aggressive (36% clear go), levels are an upper bound, trend robust (table). nfl4th's own clear-go share **not** checked (no R in the container); stated as a limit in the notes. |
| 2.8 5-yard penalty never priced | Priced: 4th-and-1 at own 40 → 4th-and-6 costs ≈4.7 WP points; advice now down-dependent. |
| 2.9 Conversion ignores field position | `p_conv(togo, yl)` gains a fitted inside-the-10 term (−8 to −9 points); paragraph + dashed curve in Fig 6; map caption notes it; drill 2 asks about it. |
| 2.10 Brill et al. given no number | Added: −4 to +5 interval on a +1.1 call; confident on 48% of 2018-22 fourth downs; 1-in-5 under 1 point; >4 points almost always clear; coaches 91% / 49%. |
| 2.11 SB LI: why not kick at once | Film room now leads with the plan (run three times, burn NE's three timeouts, ATL had one, then kick). |
| 3 Fig 8 hard to decode | Colourbar added; P(conv) column at right; impossible cells greyed; cell numbers 5.6→6.6 pt; caption says "vertical line" and what to notice. |
| 3 Fig 7 markers | Diamond at the conversion spot, leader lines from both labels to their spots; fail label moved next to the ball; goalposts drawn; FG miss branch now uses the holder spot (SF 36) consistently in code and text. |
| 3 SB LI WPA table | Event tags ([INTERCEPTION, TD], [FUMBLE], [2-PT GOOD]); NE-ATL score column; header no longer wraps; the +10.1 Q2 15:00 row discussed as a quarter-change artefact. |
| 3 Fig 4 | "(8:31, Q4: same clock, one quarter later)"; caption gives 99%→96% for the strip-sack; leader lines no longer cross their own labels. |
| 3 Fig 1 1.85 vs 1.83 | Line now drawn at the computed median (1.83); caption and text agree. |
| 3 Fig 9 "about halfway" | Retitled "one in five to two in five". |
| 3 Yellow line through defender labels (Figs 13, 15) | Drill helper draws the line to gain by hand with gaps around any player on it (gridiron untouched). |
| 3 Drill pictures carry no information | Drill 1 asks which play attacks this front (answer: sneak/tush push in the A-gaps, 82% vs 66%; PHI 83%, BUF 91%; play-action vs one deep safety). Drill 2 asks whether the league rate is fair from the 8 (no: the picture's compressed field; 46% vs 55%). Drill 3 adds an underdog/overtime twist (go first still wins, 56% vs 46%, gap narrows). |
| 4 Length / code in print | Plotting code moved to folded, web-only helper cells (13-01 pattern); print shows only data and model code. Rules of thumb cut from the Watch-for-it list and Takeaways; down-14 caption shortened; history paragraph cut; OT caveat removed from the data section; 99% paragraph merged into its callout; bots history tightened. **Partly declined:** prose grew to ≈10k words (incl. captions) because most findings asked for added explanation; the print length stays 39 pp. with far less code. |
| 6 Two-point chart rows, OT rule, down 14 early | One paragraph points to 10-04's rows (down 2/5/10; up 1/5/12/15) and the same tree; `ot=` used with a computed 40% case; one sentence on down 14 in Q2-Q3. |
| 6 Timeout decisions themselves | Timeout value now split by situation (trailing 1-3: +1.2 per own timeout; leading: +0.1) and the penalty trade priced; when-to-spend / let-them-score / kneel pointed to 10-04's flowchart. **Declined** a new timeout figure (length). |
| 6 nfl4th numbers, broadcast bars | nfl4th not run (R package; no R in the container): **declined**, noted. Watch-for-it now tells the reader how to tell whether a broadcast bar knows the spread (its kickoff value). |

### Coach review (`13-03-coach.md`)

| Finding | Action |
|---|---|
| 1 Lions contradiction; Reynolds | Fixed as above; Reynolds "couldn't hold onto Goff's pass" sourced to AP (Dubow, Jan 28 2024), used as the decision-vs-execution point. |
| 2 Drill 2 "must" | Reworded: end zone only 10 yards deep, so nobody needs to play deeper. |
| 3 Red-zone conversion | Fitted red-zone term in `p_conv`; 44% vs 53% (3rd/4th-and-3) quoted from pbp. |
| 4 FG geometry | `miss_spot = yl + 8`; prose "about 8 yards back to the holder (an extra point from the 15 is a 33-yard kick)". |
| 5 Timeout advice | Down-dependent advice with the priced 4th-and-1 example; "a third-quarter timeout costs some of that, not all". |
| 6 Four-down territory | Added to Watch for it; third-down selection paragraph softened (selection runs both ways). |
| 7 Sneak numbers | FTN `is_qb_sneak` 2023-25 in drill 1's answer; A-gap point made. |
| 8 `no_play` bias | One sentence in the grading method (about 1 in 18 fourth-down rows). |
| 9 Icing contamination; double-ice | Sample restricted to kicks that tie or take the lead (116 iced vs 297); the 37 "ahead" kicks reported; second-timeout rule sourced (ESPN, Seifert 2015, Rule 4-5). Rule wording is as explained in 2015; worth a check against the 2026 rulebook. |
| 10 Timeout regression mixes situations | Split by trailing 1-3 / 4-8 / tied / leading, with each margin as its own dummy. Note: the split shows the pooled +1.7 *overstated* every subgroup (pooled linear margin was confounded), not understated the trailing team. |
| 11 WPA table | Tags + score column; jumpy-quarter note. |
| 12 Trips terminology | Caption: "3x1 with the tight end attached on the trips side (often called trey)". |
| Fig 13 | SS d=5 outside the TE, FS d=9.5. Kept "base 4-3 stays on the field" in prompt and caption. |
| Fig 15 | W walked to the apex over H (d=3); $ over the Y slot; corners press at the 1. |
| Fig 7 goalposts | Drawn. |
| Smaller | Colts had one timeout and NE none (2009 pbp, shown in code); DET "level with Buffalo"; ATL one timeout / NE three in SB LI; impossible map cells masked. |
