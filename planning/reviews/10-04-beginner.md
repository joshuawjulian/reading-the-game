# 10-04 The Clock, the Two-Minute Drill, and Fourth Down: beginner-reader review

Reviewer role: casual fan who has never played, has read only Parts 1-9 and 10-01 to 10-03 in curriculum
order. Read the .qmd start to finish. Re-rendered (`build_pdfs.py ... --html`, OK) and looked at all 25 pages
of `pdfs/10-04-clock-and-game-management.pdf` at 60 dpi, plus pages 4, 6, 8, 11, 13, 14, 16, 18, 19 and 21 at
110-150 dpi. I tried the three Predict-the-play drills before opening the answers.

**Overall:** this is a very good chapter. The "clock is a currency / price list" framing is the best idea in it,
and the price-list bar chart, the Super Bowl LVIII drive chart and the fair-catch-kick plate are excellent. I
came away able to price plays, to say "running/stopped" after each snap, and to recite the fourth-down rules
of thumb. The main problems:

1. **The kneel-down chart and its rule of thumb leave out the last ~40 seconds** (the play clock that runs
   down before the fourth down), so using the chapter's own tool I got Drill 2 *wrong*. The chapter's own
   Westbrook example (first down at 2:19, two-minute warning still to come) contradicts the rule of thumb.
2. **The clock flowchart's "trailing defense: behind by more than a score? let them score" box is
   incoherent**, and doesn't match the Super Bowl XLVI example it comes from (the Patriots were *leading*).
3. **The fourth-down section announces an expected-points argument and never does the arithmetic**, even
   though 01-02 gave me EP values. For an analytically minded reader this is the biggest missing "why".
4. **Two logic slips**: "Why the exception?" argues the reverse of what it means; the intentional-safety rule
   ("only works with a lead of three or more") is immediately followed by the Patriots taking one while
   *trailing*, with no reconciliation.
5. **The Reid film room's arithmetic doesn't survive a check** against the drives it describes.

---

## 1. Terms used before they're explained, or never explained

| Where | Quote | Problem |
|---|---|---|
| Two-minute drill history (l. 479) | "the Colts won in the first **sudden-death** overtime in NFL history" | Sudden death is only explained ~800 lines later in Overtime ("the first team to score in overtime won"). 01-01 mentions it, but a one-clause gloss here costs nothing. |
| The spike (l. 491) | "a quarterback **under center** may stop the clock legally" | Most offenses I've seen in this course are in the shotgun. Can a shotgun QB spike? (The footnote's "T-Formation Quarterback" hints no.) One sentence: "that's why you see the QB jog up under center to spike." Otherwise I'll be confused the first time I see it. |
| 10-second runoff (l. 530) | "A defense is never charged a runoff ... in the last 40 seconds a defensive time-saving foul can end the half if the defense has no timeouts left." | Reads as a contradiction: never charged a runoff, yet its foul can end the half? *Who* decides, and how? Needs a concrete sentence (e.g. "the offense may choose to let the clock run out instead of taking the yardage"). |
| Fair-catch kick (l. 1010-1011) | "a place kick (no tee) or a **drop kick**"; "no holder seven yards back" | Drop kick is never glossed (one clause: "dropped and kicked on the bounce"). And "no holder seven yards back" made me think there was *no holder*, but the plate caption says "the holder put the ball down at the 47 itself". Say "the holder kneels at the spot itself, not seven yards back". |
| Safety plate caption | "with the 2026 kickoff alignment", "the landing zone", "coverage lines up on the opponent's 40" | These come from 09-02 (Kickoffs), which is **not in the You'll need box** (only in Connections). Why does a kick from my own 20 have its coverage standing on the opponent's 40? A one-line recap or a You'll-need entry for 09-02. |
| Kneel arithmetic (l. 730) | "a **chip-shot** field goal" | Slang; a parenthesis ("a very short, near-certain kick") is enough. |
| Fourth down (l. 1106) | "the 'Philly Special' touchdown" | I'm told it's a "trick play" only in the next sentence, obliquely. What was it? The footnote knows (TE throws to the QB); give it in a clause in the text. |
| Overtime figure caption | "the kickoff itself counts as the receiving team's chance" | I couldn't decode this. Does it mean if the receiving team fumbles the opening kickoff and the kicking team recovers, the receiving team has "had" its possession? Say so with that example. |
| Overtime flowchart | "B's defense scores a safety: Team B wins" | What about a pick-six or fumble return on A's first possession? Not covered anywhere; the obvious question once you see the safety exception. |
| Two-point chart | "close" (yellow) cases: down 1, 4, 9; up 2, 9 | Never explained. **Down 1 after a touchdown (go for the win or kick for the tie?) is one of the most common late-game TV moments**, and the chart just says "close". At least explain down 1. |

## 2. Leaps: a missing or assumed "why"

1. **Kneel arithmetic ignores the fourth-down play clock** (fig-kneel-math, l. 718-722). The chart says three
   kneels drain 2:03 / 1:24 / 0:45 / 0:45 and the rule of thumb says "with no defensive timeouts, a first down
   with about two minutes or less ... ends the game". But after the third kneel the offense doesn't have to
   snap again until the play clock expires, so the true thresholds are ~40 s higher (~2:43 / ~2:04 / ~1:25).
   Drill 2's answer *uses* that extra 40 s ("16 seconds left and a 40-second play clock, so the game clock
   reaches zero") but the chart never shows it. The chapter's own Westbrook example confirms the gap: first
   down at 2:19 with the two-minute warning still to come (which the chapter says works like a timeout, so the
   chart says ~1:24) and the Eagles still knelt it out (kneels at 2:00, 1:15, 0:30). Fix: add the fourth
   play-clock segment to every bar (or a "game over if ≤ this" marker), and restate the rule of thumb.
   Also say what happens if time *is* left at fourth down: kneel and hand over the ball? take a delay of game?
2. **"Why the exception?"** (l. 398): "Because without it the end of every close game would be a parade of
   five-yard sideline throws, each stopping the clock for free." The *exception* (late in a half) is what lets
   out of bounds stop the clock; the *general rule* (restart on the ready signal) is what prevents the parade.
   As written the reasoning runs backwards. Reword as "Why the general rule? ... Why the exception? ...".
3. **"So does the first snap after a change of possession, at any time."** (l. 404) I had to re-read three
   times to work out what "so does" refers to. Spell it out.
4. **Spike "costs 1 second"** (l. 495) vs the price list's "Completion in bounds, then a spike: 16 s". Both are
   right (the spike play itself vs snap-to-snap) but the chapter never says so, and then: "That second cost is
   the real one" — "second" here means "the second-listed cost (the down)", right after "1 second". I read it
   as "that one-second cost". Say "the down is the real cost".
5. **Intentional safety: lead vs trailing** (l. 992-1001). "The arithmetic only works with a lead of three or
   more ... and when the clock is nearly gone." The very next example is the Patriots taking a safety while
   *trailing* 24-23 with 2:51 left. The text calls it "the boldest" but never says it's a *different* logic
   (needs timeouts + a defensive stop, trading 2 points for field position on the next possession). One
   sentence would fix it. Also: with a lead of exactly 3, the safety makes it 1 and a field goal then *loses*
   — say why "three" is still the threshold (only when there's no time for a drive).
6. **Fourth down: "Put values on each outcome and the 'go' option usually wins"** (l. 1070). The chapter
   never puts the values. 01-02 gave me an EP ladder; one small worked example (EP of 1st-and-10 at the
   opponent's 34 × 58% + EP of the opponent's ball at its 36 × 42% vs punt EP vs 74% × 3 minus miss) would
   turn a claim into a mechanism. As written I have to take it on faith, which this book otherwise never asks.
7. **Heuristics vs what teams do.** The rule "the opponent's 30 to 40 ... even fourth-and-4 or 5 is usually a
   go there" (l. 1166-1168), but the heatmap two pages earlier shows 2023-2025 teams going only 32% / 29% on
   4th-and-4/5 at the opponent's 30-39. Similarly "fourth-and-2 or 3: go from about midfield in" vs 26% on
   4th-and-3 inside the 9. Say explicitly: these are the *models'* recommendations; teams are still more
   conservative, and here's the gap. Otherwise the reader sees a contradiction.
8. **Why did the go rate dip in 2022-2023?** The caption notes it; the text doesn't explain it. I want a
   sentence (even "nobody knows; possibly X").
9. **LVIII, San Francisco's field goal** (l. 633-636): "A touchdown there would have forced Kansas City to
   score a touchdown." On fourth-and-5 the choice wasn't field goal vs touchdown, it was field goal vs going
   for it (and how much clock to burn first). "That is the end-of-half trade-off this chapter returns to
   later" — it never does, explicitly. Should the 49ers have gone? What would the heuristics say?
10. **Flowchart, trailing-defense box** (fig-clock-flow, l. 1435): "late, still behind by more than a score?
    let them score, get the ball back." If I'm behind by more than a score, letting them score puts me
    further behind; that can't be the tactic. The real case (XLVI, l. 728) is a defense that is *leading or
    tied* and facing a near-certain go-ahead field goal at the gun. The caption repeats the same wording.
    Also l. 731: "Both are the four-minute offense seen from either side" — in XLVI the team with the ball
    (Giants) was *trailing*, so it's not a four-minute offense. This paragraph needs rethinking.
11. **Reid film room arithmetic** (l. 1375-1378): "the difference between huddling (40-odd seconds a play) and
    hurrying (about 20) over 13 or 16 plays is four or five minutes." But the 2015 drive was 16 plays in 5:16
    (≈20 s/snap on average) and the 2004 drive took 3:52 in total, so a 4-5 minute saving is impossible for
    it. A reader who checks finds the critique doesn't add up. Show the real breakdown (how many
    running-clock snaps, their median gap vs the ~21 s hurry price, and the unused timeouts' value).
12. **Hail Mary at 0:04 with a ~6 s play**: the chapter never says the half doesn't end until the play ends
    (and that a defensive foul gives an untimed down). That's exactly what makes the Hail Mary and the
    end-zone pass-interference drama work.
13. **Drill 1 answer**: "a catch in bounds at, say, the 18 would leave the offense needing to spike with the
    clock still running and perhaps ten seconds left, which is fine" — but by the price list a hurried real
    play costs ~21 s from the previous snap (snap at ~0:15), plus ~16 s for the spike after an in-bounds catch;
    that runs out. Either fix the numbers or drop "which is fine". And it calls running a real play "a gamble"
    and then "fine" in the same sentence.

## 3. Diagrams I couldn't decode, or captions that don't say what to notice

- **fig-kneel-math**: decodable and nice, but see Leap 1 — the bars omit the decisive final play-clock run;
  rows 2 and 3 both say "0:45 drained", and the caption's "each timeout takes about 40 seconds off" is then
  false for the third timeout. Caption says "orange tick"; the legend says "defense timeout" in a red-brown.
- **fig-safety-plate**: yard numbers are removed, so I can't verify "opponent's drive starts around your 46"
  or "returned to the opponent's own 34" by eye; I have to trust the labels. Add a few yard-line numbers
  (at least the 20s and 50). Label says "own 34", caption says "own 35". In panel A the punt arc and the
  return arrow end at the same point, so it looks like the ball goes forward and then back to where it
  landed; I couldn't tell the kick distance from the return.
- **fig-victory**: the offense's deep man is labelled **S**, and the defense also has an **S** (linebacker)
  and **SS**. In a formation where the caption says "S, often a safety or a receiver", this is a genuine
  confusion. Use a different letter (e.g. "D" for deep, or "K"-style "B").
- **fig-hail-mary** (frame strip): in the "+6.3 s: the ball arrives" panel Y is hidden under the ball and
  X/H/Z/FS/SS labels overlap, so the caption's "one man (Y) goes up for it, the others in front and behind"
  can't be seen. Also the defense uses **L** for linebackers here while the victory/drill pictures use W/M/S
  and the two-minute menu uses M/$ — label sets change from figure to figure.
- **fig-clock-flow**: at print size the subtitle text in the boxes is ~5 pt; readable only when zoomed. The
  "trailing defense" box is wrong (Leap 10). The left column's "No → Take your time" is good.
- **fig-two-point-chart**: the annotations under the tiles are sparse and the "close" tiles have none; the
  up-15 "GO" isn't in the caption's list ("up 1, 5 and 12"), nor in Takeaways or Watch-for-it.
- **fig-lviii-drive, fig-clock-prices, fig-oob-window, fig-fck-plate, fig-go-rate, fig-go-heatmap,
  fig-ot-flow, fig-two-minute-menu, fig-prevent**: all decoded fine; captions say what to notice. The
  heatmap is particularly good.

## 4. Drag and repetition

- "A catch in the middle costs about 20 seconds" appears in the hook, the menu bullets, the menu caption,
  the price-list text and the four-minute section. Three would do.
- Super Bowl XXXVI's final drive is told twice (two-minute history, l. 481; end-of-half, l. 807-813) with two
  footnotes; merge into the second, richer telling.
- "Judge the decision, not the result" is made in the Common-misconception box and again at length in the
  Lions film room. Keep the film room, shorten the box.
- Several captions restate the paragraph next to them nearly verbatim (two-minute menu, safety plate, kneel
  chart). Fine for print-skimmers, but they make pages 3-13 feel long.
- Title mismatch: "Film room: Chiefs 2015 season" contains the 2004 Eagles case too.

## 5. Can I do each "You'll be able to…" item?

| Objective | Result |
|---|---|
| Price any play in game-clock seconds; say whether the clock runs (incl. out-of-bounds exceptions) | **Yes.** The price list and the OOB window chart are the strongest teaching in the chapter. |
| Run a two-minute drill in my head (throws, spike vs timeout, runoff) | **Mostly.** Spike vs timeout logic is clear. The defensive-foul half of the runoff rule I can't apply (§1). |
| Kneel-down arithmetic, recognise four-minute offense and victory formation | **Partly — got Drill 2 wrong** using the chapter's own chart (Leap 1). |
| End-of-half calls: points vs shot, Hail Mary vs FG, intentional safety, fair-catch kick | **Partly.** The three questions are qualitative; I couldn't make a first-half "kneel or go" call with numbers. I can spot the two rare plays. |
| Fourth-down and two-point heuristics; explain the post-2017 rise | **Yes for the heuristics** (but they disagree with the heatmap, Leap 7); **no for "close" two-point cases**, including down 1. |
| Apply current OT rules and predict how teams play them | **Yes** for the rules; the receive-vs-kick discussion is honest. Can't handle a defensive TD on the first possession. |

**Predict-the-play attempts (before opening answers):**

- **Drill 1 (spike or snap, 0:31, no timeouts, first-and-10 at the 26):** I said spike now (price list: ~16 s
  from the last snap, so stops ~0:20 on second down), then one sideline throw or throwaway, then kick with
  the clock stopped. **Matched the answer.** But I wondered why not spike and kick on second down right away
  (44 yards is inside the kicker's range); the answer never weighs that against the risk of one more snap.
- **Drill 2 (1:40, leading, first-and-10, defense one timeout, after the 2MW):** Using the chart: one timeout
  → three kneels drain 1:24 < 1:40, so I answered **"No — they'll face a fourth down with ~16 s left; the
  defense should use its timeout immediately."** The answer says **yes**, because the 16 s run off during the
  fourth-down play clock. **Wrong, because the chapter's tool omits that step** (Leap 1). The answer's second
  paragraph ("one timeout is worth only about 40 seconds") also isn't what the chart taught me.
- **Drill 3 (fourth-and-2 at the opponent's 36, 2Q, tied):** I said go: 58% conversion, the 30-40 "go zone",
  a 54-yarder near the kicker's 55 long, and the offense left 11 personnel on the field. **Matched**,
  including the personnel clue. Good drill.

## 6. Knowledge gaps: what I still wonder

- What happens at fourth down in the kneel-out when time *is* left: kneel and give it back, take a delay of
  game, or run a real play? (Directly needed for Drill 2.)
- Can a half end on a defensive penalty? The untimed down; why Hail Marys draw pass interference flags.
- Down 1 after a touchdown late: go for the win or kick to tie? Down 4? (The "close" cells.)
- How does a team kick a field goal with the clock running and no timeouts (the "fire drill" FG)? The chapter
  says the unit "realistically can't" run on, but it happens; how fast is it?
- Why the go rate dipped in 2022-2023; and why teams still go only ~30% in spots the heuristics call a "go".
- The clock rules around the two-minute warning: if a play starts at 2:03, does the clock stop at 2:00 even
  mid-play? (01-01 covered it; a recap line in the kneel section would help, since the chart counts it as a
  timeout.)
- Should the 49ers have gone for it on fourth-and-5 at 1:57 in LVIII, or burned more clock first?
- What does a regular-season tie do in the standings? (Half a win and half a loss; one clause in Overtime.)
- What about a pick-six or fumble return on the first overtime possession?
- Is there a clock difference in the first half vs second half beyond the OOB rule (e.g. timeouts reset at
  halftime, so the first half's last two minutes play looser)? The end-of-half section touches this; a
  sentence on "teams are more aggressive with first-half timeouts because they don't carry over" would land.

---

## Revision (2026-10-08): finding → action

Covers both this review and `10-04-coach.md`. The fact-check's verified wording was kept; every new claim
has a footnote (2026 rulebook text, nflverse pbp, or a named source). Re-rendered with zero errors (29 pages)
and looked at every diagram page at 60 dpi plus close-ups at 100–130 dpi.

### Beginner: headline problems

| Finding | Action |
|---|---|
| 1. Kneel chart / rule of thumb omit the fourth-down play clock (Drill 2 got wrong) | fig-kneel-math redrawn: each bar now ends with a hatched "4th-down play clock (≈40 s)" segment and is labelled "game over from ≤ 2:43 / 2:04 / 1:25" and "≤ 0:45; else a 4th-down snap" for 3 timeouts. Caption rewritten (the third timeout is worth more than 40 s). Rule of thumb restated in coaching form (after the 2:00 warning: 0–1 timeouts → over; 2 → ≤1:25; 3 → ≤0:45), and "warning still to come: count it as a timeout from 2:00". Westbrook example now worked through on the chart. New paragraph on fourth down with time left (the "burn the clock" snap). Flowchart, Watch-for-it and Takeaways updated to match. Drill 2 answer now cites the one-timeout row. |
| 2. Flowchart "trailing defense … let them score" is incoherent | Box rewritten as "MEANWHILE, THE DEFENSE": trailing → timeouts; ahead or tied facing a sure go-ahead FG at the gun → let them score. Caption fixed. XLVI paragraph rewritten as its own explanation (Patriots *leading* 17–15; Giants would bleed the clock for a chip shot) and no longer called "the four-minute offense from either side". |
| 3. Fourth down announces an EP argument but never does the arithmetic | Added a computed EP table (nflverse EP of first-and-10, 2021–25): go +1.3, FG +0.6, punt −0.2 for 4th-and-2 at the opp 36, with the "why" (failure costs only ~1.6 points of field position vs a punt). Drill 3's answer now points to it. |
| 4a. "Why the exception?" argues backwards | Rewritten as "Why the general rule? … Why the exception? …". |
| 4b. Intentional safety "only with a lead of 3+" then the Patriots take one trailing | Split into two named versions: the clock-killer (lead ≥3, no time left; explains why exactly 3 needs *no* time, since a FG would then lose) and the field-position safety (Patriots 2003: needs timeouts and a stop). |
| 5. Reid film-room arithmetic doesn't survive a check | Replaced "four or five minutes" with a pbp calculation in the chapter code: in-bounds, clock-running snaps (7 Eagles, median 33 s; 8 Chiefs, median 29 s) vs ~21 s hurry price ≈ 60 s each, plus unused timeouts → about 1:30 and 1:46. Callout retitled "Eagles 2004 and Chiefs 2015 — Andy Reid's slow drives". |

### Beginner §1: terms

| Finding | Action |
|---|---|
| Sudden death used early | One-clause gloss in the 1958 sentence. |
| Spike "under center" vs shotgun | Body now says within one yard of the snapper (Rule 3-42, footnoted), a shotgun spike is grounding, and the QB stepping under center is the tell. Drill 1's picture now shows it. |
| Defensive runoff "never charged … can end the half" | Rewritten with the 4-7-3 mechanism: in the last 40 s, a defense with no timeouts that fouls to stop the clock gives the offense the choice to end the half. Footnote quotes the rule. |
| Drop kick / "no holder seven yards back" | Glossed "dropped and kicked on the bounce"; "the holder kneels at the spot itself, not seven yards behind a line". |
| Safety plate uses 09-02 terms not in You'll need | Added a 09-02 entry to the You'll need box; caption explains the 40-yard-line coverage. |
| "chip-shot" | Glossed in the XLVI paragraph. |
| Philly Special unexplained | Clause added: TE throws a TD to QB Nick Foles on 4th-and-goal from the 1. |
| OT "kickoff counts as the receiving team's chance" | Caption now gives the example (kicking team recovers the kickoff → A has had its possession), per Rule 16-1-5(c). |
| OT pick-six / fumble return | Flowchart box now "B's defense scores (a safety or a return TD): Team B wins"; text paragraph on both edge cases (and the 2026 any-time onside kick as a curiosity). |
| Two-point "close" cells unexplained, esp. down 1 | Every close tile now has a note; new paragraph explains down 1 (win now vs coin-flip OT and what tilts it), down 4, and up 2/9/10. |

### Beginner §2: leaps

| # | Action |
|---|---|
| 1 | See headline 1. |
| 2 | See headline 4a. |
| 3 | "So does the first snap after a change of possession" replaced by an explicit sentence. |
| 4 | Spike paragraph separates the ~1 s spike play from the 16 s snap-to-snap price; "The down is the real cost." |
| 5 | See headline 4b. |
| 6 | See headline 3. |
| 7 | Heuristics now introduced as "what the models recommend, not what teams do"; the go-zone bullet states teams go only ~30% on 4th-and-4/5 there (verified: 30% of 138, 2023–25). Takeaway says "in the models, if not yet on every sideline". |
| 8 | Added a paragraph on the 2022–23 dip: no proven answer; 50+ yard FG attempts jumped (182 in 2021 → 224 in 2022 → 279 in 2024, computed in the chapter), so some go-for-its became long kicks. Framed as "probably part of it". |
| 9 | LVIII "Notice also" rewritten: the 4th-and-5 kick was defensible; the criticised call was the 3rd-and-5 incompletion at 2:00 (pbp) that saved KC a timeout or ~40 s. |
| 10 | See headline 2. |
| 11 | See headline 5. |
| 12 | New paragraph: a half never ends while the ball is live (4-8-1); an accepted defensive foul gives an untimed down, an offensive one doesn't (4-8-2). Ties to Hail Mary PI and prevent technique. |
| 13 | Drill 1 answer rewritten with consistent prices (real play snapped ~0:15, catch in bounds ~0:10, spike would need ~16 s → game over); "gamble … fine" contradiction removed; adds the kick-now (44 yd, ~84%) vs one-shot (34 yd, ~97%) choice the reviewer asked about, with the no-sack condition. |

### Beginner §3: diagrams

| Figure | Action |
|---|---|
| fig-kneel-math | See headline 1; legend moved under the bars; "orange tick" now matches the legend. |
| fig-safety-plate | Yard-line numbers added along the bottom of both panels; label and caption both say "own 34"; punt arc and return now end at different points (return drawn diagonally to the marked start), with "punt" and "return" labels; punt protection added (coach B). |
| fig-victory | Deep man relabelled **D** (no clash with the defense's S/SS). |
| fig-hail-mary | Close-ups rebuilt: receivers finish in a diamond (Y jumper, H front tipper, Z back tipper, X and R sides) with labelled leaders, the ball drawn (with a flight trace) so Y is never hidden; underneath defenders now W/M/D (no more "L"). |
| fig-clock-flow | Defense box fixed (headline 2); kneel box rewritten; "Tight" gains "or call a sideline throw". Sub-text kept at 6 pt (boxes have no room to grow without a redesign) — **partly declined**; it is legible at 100 dpi. |
| fig-two-point-chart | Notes now under every go and close tile, staggered so neighbours never touch; up 15 added to caption, Watch-for-it and Takeaways. |

### Beginner §4: drag

- "About 20 seconds" removed from the menu bullet and the menu caption (kept in the hook, price list and on-field label).
- Super Bowl XXXVI now told once, in End of the half (richer version incl. the first-down spike and the final spike), footnotes merged.
- Fourth-down "Common misconception" box cut to two sentences, pointing to the Lions film room.
- Caption restating text: trimmed where touched; others kept for print skimmers (declined as low value).
- Film-room title fixed (see headline 5).

### Beginner §6 knowledge gaps

All answered in text: fourth down with time left (burn play); half-ending on defensive fouls; down 1/down 4; running-clock FG ("fire"/"Mayday", ~17 s per Dave Toub, sourced); the 2022–23 dip and the model-vs-team gap; two-minute warning timing (Rule 3-41, snap at 2:05 → full stoppage); should SF have gone (LVIII paragraph); ties = half win/half loss (NFL.com); OT return TD; first-half timeouts vanishing at halftime.

### Coach review

| Finding | Action |
|---|---|
| A1 kneel threshold | Fixed (beginner headline 1), thresholds 2:43/2:04/1:25/0:45 as the coach gave, plus the burn play. |
| A2 Predict-1 arithmetic | Fixed: real-play path now "game over"; ball-out-fast / no-sack coaching point added. |
| A3 "can't run on with a running clock" | Replaced: emergency running-clock FG exists, ~17 s at best (Toub, Chiefs On SI, 2025; Butker's 59-yarder snapped at 0:03 after a 0:17 snap, verified in pbp). |
| A4 runoff contradiction | Fixed with Rule 4-7-3 wording. |
| A5 "+12" label; down 9; up 10 | +12 now "→ up 14: two TDs only tie". Up 10 changed to "close" with note. **Down 9 kept "close" (declined "kick")**: with one more TD each, kick (down 8 → TD+2) and go (48% → down 7 → TD+XP) both tie ≈45% of the time, so the arithmetic is even; the note says "→ 7 or 8: both one score". The fact-check also flags close cells as judgement calls. |
| A6 "second cost" pun | Fixed. |
| B menu: flat route | RB now runs a real flat, past the line to w≈−12.5. Caption names the three-level flood. Z comeback kept; caption now describes the corners as eight yards off (soft), which the comeback attacks. |
| B LVIII: vertical nudges; SF timeout | Nudges are now horizontal (time) only, so every dot sits on its true yard line; key row 9 and text note two 49ers DBs hurt and the injury-timeout rule. |
| B victory | QB drawn at the library's under-center depth (1.9 yd, drawn slightly off the center for legibility, as the gridiron convention does) with backs at −3.3, ±1.5, i.e. on his hips. Base defense kept, captioned as the "given up" look. |
| B Hail Mary | Diamond roles, DBs at/above the jump point, a goalie, underneath players at the front; throw at 4.3 s (caption: "a little over four seconds"); own-40 parenthetical replaced by hook-and-lateral / "river" plays from deep in your own half. |
| B prevent | Outside underneath players moved to w≈±18.5 at 11 yd as "sideline sinks" with labels; go routes extended to 29 yd; caption says "shaded zones". The checkdown already ends ~3.5 yd deep (the route waypoints are offsets from a back 5 yd deep), so "about 4 yards" was right; caption unchanged on that point. |
| B safety plate | Punt protection added (line, wings, PP, punter); label and caption give the shorter punter depth and the bad-snap/muff risk; punter-out label moved beside his path. Holding: verified that Rule 12-3-3 now penalises multiple fouls to manipulate the clock (15 yards, clock reset to the snap); text says so, with the Ravens' XLVII holding as history. |
| B fair-catch plate | Bold box moved clear of the defensive line and the end-line label; window widened to (−25, 57) and the left label wrapped so nothing touches the edge; defense-may-not-cross rule added (Rule 3-19 offside definition / 11-4-3). |
| B go-rate/heatmap caveat | Added (model vs teams, ~30%). |
| B two-point label spacing | Fixed (staggered notes, tighter limits). |
| B OT flow | Return-TD branch added; onside curiosity sentence added. |
| B clock flow | Kneel numbers updated; sideline-throw option added. |
| B Predict-1 | QB under center, receivers 1–3 yd short of their spots, label "gun team, QB now under center: the spike tell". |
| B Predict-2 | Offense now in i_form_22 (heavy, not victory formation), defense crowded within ~5 yd; timeout label removed (score bug says it). |
| B Predict-3 | Defense now single-high with pressed corners and the SS walked down (7 within ~6 yd); the answer uses the shell as the defense's own read. |
| C1 first downs don't stop the clock | Added, with the 2023 NCAA change (NCAA.com). |
| C2 two-minute warning as a free timeout | Added (Rule 3-41). |
| C3 half can't end on a defensive foul | Added (Rule 4-8). |
| C4 injury inside 2:00 | Added (Rule 4-5-4, 4-7-3), tied to LVIII. |
| C5 spike needs QB under center | Added (Rule 3-42). |
| C6 radio cut-off at 15 s | Added to the two-plays bullet (Rule 5-3-3), linking 01-04's helmet radio. |
| C7 four-minute technique | Added (backs go down in bounds; QB slides or takes the sack), as the mirror of "no sacks". |
| C8 dialects | Added a short paragraph (dime/quarter packages, "clock", "fire"/"Mayday", four-minute drill). Team-specific Hail Mary names ("Rocket", "Big Ben") **declined**: could not source them. |
| D film rooms | LVIII 3rd-and-5 at 2:00 added; KC OT timeout at 6:05 added; XXXVI first-down "textbook" spike added; Westbrook used as the worked kneel example; Reid recomputed from pbp; Lions kicks given as 46 and 48 yards. |
