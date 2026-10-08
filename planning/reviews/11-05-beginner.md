# Beginner-reader review: 11-05 The Modern Era

Reviewer persona: casual NFL watcher who has never played and has read Parts 1-10 and 11-01 to 11-04 in
order. I read the qmd start to finish and the PDF (`pdfs/11-05-the-modern-era.pdf`, 27 pages, rasterized at
60 and 110 dpi). Line numbers refer to `chapters/11-history/11-05-the-modern-era.qmd`.

**Overall:** this is a strong chapter. The arms-race framing works, the box arithmetic ("six against six,
now seven against six") is the clearest idea in it, and the 2018 vs 2025 play-action pair (figs 2 and 6)
is the right teaching device. The biggest problems are that **two of the data charts undercut the story the
text tells about them** (under-center and QB-rushing trends), **one drill's premise contradicts a rule
taught in 02-01**, some diagram details that don't match the captions, and **length**: about 10,400 body
words against a 6,500 target.

---

## 1. Terms used before they're explained, or never explained

Nearly every term is owned by an earlier chapter and linked, which is good. The real problems are terms
whose meaning changes inside this chapter:

- **"Light box" has two definitions.** "You'll need" (l.221-222): "A light box has no more of them than the
  offense has blockers." The glossary entry (l.7), the trend chart and the stats (l.620-623) use "six or
  fewer". Against 12 personnel (seven blockers), a 7-man box is light by the first definition and heavy by
  the second. Because fig 5 and drill 3 hinge on 7 against 6, pick one definition. Use "six or fewer" for
  the data and say so once.
- **"Two-high" measures different things in different places.** The narrative and the Sunday checklist
  are about the *pre-snap shell* ("Count the deep safeties: one or two?", l.1355). The trend line and the
  stats are *post-snap coverage labels*, and footnote `[^trendcalc]` admits that by that measure Fangio's
  2024 Eagles were 27th and the 2023 Ravens 22nd. The misconception callout (l.740-742) touches this in a
  parenthesis, but a reader hits "Fangio's light-box Eagles" (timeline) and "two-high defenses ... allowed
  the fewest points" before learning that those teams were *below average* on the chart's measure. Put this
  in the body next to fig 4: "this line counts coverages after the snap, not the shells you see before it".
- **"Ninth run defender" vs "eight in the box"** (drill 1). The caption (l.1378) says the SS crept down and
  "eight defenders are in the box". The answer (l.1400) says "he is now a ninth run defender". The figure
  also shows an **S** (Sam linebacker) beside the SS, while the caption says "The two linebackers are at
  4.5 yards". I count W, M, S and SS, which is three linebackers plus a safety. Which is it?
- **"Mesh"** (l.1116) is glossed inline as the handoff point, but the glossary's `mesh` (04-04) is the
  crossing-route passing concept. Add "(the mesh point, not the mesh concept)" or reword.
- **"Outside leverage"** (fig-pa-two-high caption) and **"fit"** (used as a verb throughout) are owned
  earlier, so these are acceptable. "6-1 front" (l.456) gets an inline gloss but no picture. Fine.
- **Internal jargon leaks into footnotes:** "rated LIKELY" (`[^seahawks25]`), "course fact sheet §0 (C2)",
  "course fact sheet §7/§9/§10". A reader doesn't know what the "course fact sheet" is. Replace it with the
  underlying sources or drop it.

## 2. Leaps (a missing or assumed "why")

1. **The under-center chart undercuts "revival".** Fig 4's right panel shows non-shotgun snaps at about
   35% (2016), 40% (2017) and 36% (2018), falling to 28% in 2023 and back to 34% in 2025. So in 2025 the
   league was under center *less* than in 2016-2018. The opening says "Nearly every piece of that 2017
   picture had flipped by 2025" (l.185), and the takeaways present under center as the new answer. A
   numerate reader will see that the "revival" is a recovery from a 2019-2023 dip back to the 2016-2018
   level, and that the dip bottoms out in **2023, exactly at the data-source break** (NGS to FTN). The text
   needs to say what really happened. Did teams leave under center in 2019-2022 and come back? Is the 2023
   low partly a charting artifact? Is the "revival" about *which* teams and *which* downs, not the
   league-wide level? Right now the chart quietly contradicts the chapter title.
2. **The QB-rushing chart undercuts "spike and fall".** Fig 8: 2013 is 12.8%, 2014-16 about 11%, 2017
   12.6%, 2018 13%, and **2019 (Jackson's record year) 12.8%, lower than 2018**. The 2012 wave didn't "fade
   in two seasons" (l.1088). The share stayed well above the pre-2012 7-8%. The real second step is 2020
   (14%) and 2024 (16.5%), not "the Lamar Jackson era". The annotation "Jackson's 1,206 yards (2019)" points
   at a bar no taller than 2013's. Either recast this as a staircase (2012 step, 2020 step) or change the
   claim. The blue bars from 2018 on are also never explained in the caption.
3. **The light-box runs are shown before 2017 too.** Fig 4: in 2016 about 38% of runs faced six or fewer,
   the same as 2018 (37%). The opening's 2017 picture of "one deep safety and eight players crowded near the
   line" (l.184-185) and the claim that "the boxes empty" from 2018 both need the 2016-17 points explained,
   or the trend starts at a dip (2017, 30%) and looks cherry-picked.
4. **"Two-high climbs steadily from 2018"** (fig 4 caption) is not what the drawn line does: 41.2 (2023),
   38.6 (2024), 43.3 (2025). Say "climbs, with a 2024 dip", or explain the dip (Eagles-style rotation?).
5. **"The 20-yard pass ... got rarer"** (l.623-625) is backed by 10.0% vs 11.3% deep attempts against
   two-high vs single-high in 2025. That is a one-point difference between coverages in one season, not a
   decline over time. The "bargain" paragraph's punchline needs a stronger number, such as explosive-play
   rate or EPA per dropback against two-high vs single-high, or a time series.
6. **A safety reading a receiver "doesn't care what the back is doing"** (l.558-559), yet fig 6 is built on
   a quarters safety who *is* fooled by the run fake. The caption half-explains this ("reading the tight end
   in front of him"), but the reader needs the bridge stated in the body: a quarters safety reads the #2
   receiver, and when #2 (the TE) blocks, his rule tells him to fit the run. Heavy, under-center
   personnel turns the receiver he reads into a blocker. That sentence is the whole mechanism of the
   under-center revival, and it is missing.
7. **The loop diagram (fig 10) says "each arrow is the answer it provoked"**, but the arrow from McVay
   (offense) to Mahomes (offense) is not an answer. Mahomes wasn't a response to McVay, so the loop breaks
   its own offense/defense alternation. The dashed arrow from Macdonald back to "Single-high, eighth man in
   the box" also suggests the answer to 2025 is a return to 2013. The text says the open question is
   "what beats that?" and proposes spreading out heavy personnel. Either point the dashed arrow at the
   centre "2026: ?" or label it.
8. **Mahomes section: what was actually "borrowed from college"?** l.487-494 lists RPO, shovel option, jet
   motion and "Air Raid concepts" but never shows one. This is the only big era section with no diagram,
   and "Jet Chip Wasp" (film room) is described in words only. I can't picture it. A single frame of
   Wasp, or a 2-panel Air Raid concept vs a single-high defense, would fix the gap.
9. **Rules table:** the text says kickoffs changed five times, "(2018, 2023, 2024, 2025 and 2026)"
   (l.1238), but **the table has no 2023 row**. The 2017 OT row says "the first possession matters more"
   without saying why. The 2022/2025 OT changes "reward offenses that can score touchdowns" (l.1242-1243)
   also needs one clause of why.
10. **Drill 3's premise breaks a rule taught in 02-01.** The caption says the offense used three receivers
    on the previous play and now, "without huddling", is in 12 personnel while the defense is "unable to
    substitute". 02-01 taught (glossary "Substitution matching") that **when the offense substitutes, the
    defense must get a chance to respond**. A reader who learned that will stop here. Fix the setup: the
    same eleven stayed on the field and the second TE had been split out as a receiver, or the offense was
    already in 12 and lined up 2x2 on the previous play.

## 3. Diagrams I couldn't decode, or captions that don't say what to notice

- **Fig 2 (play-action vs Cover 3, p.5):** in panels 3 and 4 the unblocked **E is drawn about 1-1.5 yards
  directly in front of the quarterback**, and the ball's dashed path starts through him, while the caption
  says the QB is "clear of the unblocked end". In print it looks like a sack about to happen. In panel 2 the
  green Z ring overlaps the SS square. **Y has no gold ring**, though the reading key says gold rings mark
  tight ends. The same is true in fig 3.
- **Fig 3 (light-box inside zone, p.9):** the caption says "the linemen double-team the two defensive
  tackles and climb to the linebackers", but linemen paths aren't drawn, so nothing visibly climbs. In
  panels 3 and 4, **W and M stand unblocked 1-2 yards from the runner's path**, which makes "every box
  defender has a man" unconvincing. The "5-6 yards" label in panel 4 overlaps the W/runner area. The figure
  also duplicates 05-05's light-box figure ("Two-high and the light box"). Consider citing that one and
  spending the space on something new.
- **Fig 4 (trend lines, p.10):** the y-axis says "share of plays (%)", but two-high is a share of
  dropbacks and light box a share of designed runs. Everything else is covered in §2 (1-4).
- **Fig 6 (play-action vs two-high, p.13):** **the two top panel titles collide**: "Snap · 12 personnel
  under center, two-high" runs into "+0.9 s · the strong safety fits the 'run'". Otherwise this is the
  best diagram in the chapter.
- **Fig 7 (positions map, p.14):** the caption says the move TE is "split into the slot", but Y is drawn as
  a wing about a yard outside the right tackle. The EDGE callout points to one E though both are ringed.
- **Fig 9 (fourth downs, p.18):** the orange label "4th and 1-2, between the 30s" sits at about 15%, right
  on top of the green "every fourth down" label and about 10 points below the orange line. I first read it
  as labelling the green line. Move it next to its line.
- **Fig 1 (timeline):** the half-year offsets (2018.74, 2019.26, 2022.74, 2024.74) make items float between
  rows, so I couldn't tell whether "Lamar Jackson, unanimous MVP" was 2018 or 2019, or "Ben Johnson's
  Lions" 2022 or 2023. The "Offense" column also mixes Super Bowl results and coaching moves with
  offensive *moves*. Fine for a timeline, but the caption calls them "offensive moves".
- **Drill 3 figure (p.25):** the "7 blockers" label sits far left under X, away from the two TEs who make
  the seventh blocker, and **gives away half the answer**. The dashed box ends between Y and U, so the
  seventh blocker (U) is outside the box being counted. Either widen the box or say why U counts.
- **Print layout:** pages 8, 12 and 17 are about half blank because the following figure won't fit.
  Worth a `fig-pos`/size tweak.

## 4. Drag and repetition

- **Length:** about 10,400 body words (plus about 3,000 footnote words) against a 6,500 target. The chapter
  reads long in the middle (two-high through positions).
- **The same numbers repeated.** NGS 32.9% → 42.0% appears in the glossary, fig 4 caption, the bullets
  (l.716-720), the takeaways and the opening. Seattle's 53% under center appears in the opening, l.824 and
  the film room. 27% → 34% under center appears at l.8, l.727 and l.821-825. Keep each once in the body.
- **Overlap with earlier chapters:** NGS two-high numbers, the Staley 2020 Rams film room and the Evero tree
  are already in 06-06. The light-box inside-zone picture and box-count EPA are already in 05-05. Here they
  could be one-line callbacks with links.
- **Three "Common misconception" callouts and seven film rooms.** The Lions NFCCG film room (l.1196-1212)
  is long and re-litigates the 2009 Belichick decision from 11-04. Its "what to notice" could be half
  the length.
- The "Rules underneath" closing paragraph and "Where the game stands" both list the 2026 rule changes
  (l.1235 and l.1281-1283).

## 5. Can I do the "You'll be able to…" items? Drills attempted before opening answers

| Objective | Verdict |
|---|---|
| McVay/Shanahan 2017 and why it beat single-high | **Yes.** Fig 2 plus the "Why it exists" box make it concrete. |
| Mahomes/Reid additions | **Partly.** I can say "off-script plus college ideas", but I can't describe one college-borrowed concept. Nothing is drawn. |
| Two-high counterrevolution, its trend line, its cost; the offensive answer by counting | **Yes for counting** (figs 5-6 are excellent). **Shaky for "read its trend line"**, because the chart's measure (post-snap) differs from what I'm told to watch (pre-snap shell) and the line dips in 2024. |
| Positions that changed and which move each answered | **Yes**, from the map plus the prose. |
| Why the QB run stuck; why coaches went for it, with numbers | **Fourth down: yes**, a clear chart and four reasons. **QB run: I can recite the reasons, but the chart contradicts the "faded after 2012" premise** (see §2.2). |
| Rule changes and where the game stands entering 2026 | **Yes**, though the table is missing the 2023 kickoff row. |

**Drill 1 (creeping safety, 2019).** My answer before opening: play-action boot away from the run with a
crosser behind the linebackers, because three good runs taught the SS and the LBs to step up. **Correct.**
I was confused by the count: the caption says eight in the box but I see W, M, **S** and SS. Then the
answer says "ninth run defender". The answer also points to "the play-action figure earlier", which was 11
personnel with H in the flat, not the fullback. That's minor.

**Drill 2 (second-and-6 vs two-high, 2022).** Before opening: six in the box, six blockers, two safeties
at 12-13, so run, and the defense accepts it to protect the deep ball. **Correct.** Easy, perhaps too easy,
because it repeats fig 3 almost exactly. A harder version would ask "what if the TE is detached?" or add a
rotation tell.

**Drill 3 (heavy, no huddle, 2025).** Before opening: (a) stay and give up the run, (b) rotate the SS down
and risk play-action behind him, (c) slant or pressure. I guessed the offense wants (b). **Correct**, but
partly because the "7 blockers" label told me the count and fig 6 had just shown (b). The premise also
made me stop and wonder why the defense couldn't substitute (§2.10).

## 6. What I still wonder (knowledge gaps this chapter should answer)

1. **Did offenses really leave under center from 2019 to 2023, or is that dip partly the data source?**
   And why is 2025 (34%) a "revival" if 2016-18 was 35-40%?
2. **What shell did the 2024 Eagles and 2023 Ravens actually *show* before the snap?** Is there a public
   pre-snap two-high stat? Without one I can't connect the Sunday checklist to the chart.
3. **What did offenses do *through the air* against two-high** before going heavy? Was the Chiefs'
   "patience" (underneath throws, Kelce) the general answer? Is there a stat (e.g. aDOT falling
   2019-2022)?
4. **What does Macdonald's "pressure from two-high looks" look like on TV?** The loop's last defensive box
   is the least explained. One sentence on what to watch for (a linebacker in the A gap who drops, a
   safety who blitzes) would help, or a link to the exact figure in 07-03.
5. **We're five weeks into 2026 (today is 2026-10-08).** The chapter speaks only of "entering 2026" and
   "what the 2026 season will tell you". A "how to check early-2026 trends yourself" pointer (the code
   cells already compute everything by season) would make the chapter feel current rather than dated.
6. **How do defenses play the running QB?** "Spy" appears once, in the checklist (l.1364). What did
   defenses do against Jackson and Allen, and did it work?
7. **Why did 11 personnel barely move (60-64%) for eight years** if the whole era was a fight about
   personnel? The fight seems to have happened in alignment and shells, not personnel, until 2025. Say so
   explicitly, because it reframes the McVay section.

---

### Priority fixes (in order)

1. Reconcile fig 4's under-center line and fig 8's QB-share bars with the text's claims (§2.1-2.3).
2. Fix drill 3's substitution premise. Fix drill 1's eight/ninth count and the stray S linebacker.
3. Add the "quarters safety reads #2; a blocking TE turns his read into a run fit" sentence (§2.6).
4. Fig 6 title collision; fig 2 end-on-QB; fig 9 label placement; fig 3 linemen/LBs; drill 3 box and label.
5. Pick one light-box definition. Say that the two-high line is post-snap coverage, not the shell.
6. Add the 2023 kickoff row. Remove "rated LIKELY" and "course fact sheet §…" from the footnotes.
7. Trim about 2,500 words, mostly repeated numbers, the overlap with 05-05 and 06-06, and the long NFCCG
   film room.

---

## Revision (2026-10-08): finding -> action

Covers this review and `11-05-coach.md`. Fact-check log left intact; every new claim is footnoted (new notes:
`[^mcvayradio]`, `[^adot]`, `[^explosive]`, `[^barkley]`, `[^motion]`, `[^star]`, `[^ftn2026]`; rewritten:
`[^trendcalc]`, `[^qbshare]`, `[^eagles24]`, `[^lightbox]`, `[^seahawks25]`, `[^staffs26]`, `[^rules]`). 42 footnotes,
each referenced once. New numbers are this book's nflverse calculations (scripts in `_pdfbuild/1105-rev/`).
Render: `build_pdfs.py 11-05-the-modern-era --html` OK, 27 pages (was 27); every figure page looked at.

### Beginner review

| Finding | Action |
|---|---|
| §1 Light box has two definitions | "You'll need" now says the glossary's definition (no more than the blockers) equals "six or fewer" against the usual one-back offense, and that every number uses that cut. Glossary entry for light-box run game says the same. |
| §1 Two-high: pre-snap shell vs post-snap labels | Glossary entry, fig 4 caption and the first trend bullet now say the line is the coverage played after the snap, that no free public series records the shell (link to 06-06's "Measuring the lie"), and "on Sunday you count the shell; this line is the coverage". New film room "Eagles 2024: a two-high defense that charts as single-high" explains why Fangio's Eagles (27th) and the 2023 Ravens (22nd) sit below average. Timeline no longer says "light-box Eagles". |
| §1 Drill 1 eighth vs ninth, stray S | Answer now says "eighth". Caption: a 4-3; Mike and Will at 4.5 yards, Sam outside the tight end. SS moved to (5.8, 7.6), inside the newly drawn dashed box, with an "8 in the box" label. |
| §1 "Mesh" vs mesh concept | Ravens film room now says "mesh point, the moment the ball sits in the back's belly and Jackson decides". |
| §1 "rated LIKELY", "course fact sheet §" in notes | All removed; replaced with the underlying sources (Wikipedia season pages, PFR, nflverse dictionaries, Pro Football Rumors tracker, KSAT/AP, CBS). |
| §2.1 Under-center chart contradicts "revival" | Recomputed: 35.8 (2016), 40.7 (2017), slide to 27.8 (2023), 33.8 (2025); teams at 45%+: 12 (2017), 0 (2023), 6 (2025). Text, glossary and takeaways now say: a six-season slide, then a reversal back to the 2018 level, led by a handful of teams. The `shotgun` flag comes from the play description, so it doesn't cross the participation source break, and FTN's own flag shows the same 2022-to-2023 drop, so the low is real. Opening no longer says "nearly every piece flipped". |
| §2.2 QB chart contradicts "spike and fall" | Recast as a staircase: about 8% (2006-11), about 12% from 2012 (held after the designed read-option faded), about 14% from 2020 (16.5% in 2024). Chart redrawn with three plateaus, mean lines and "first step / second step" marks; Jackson arrow removed; caption explains the colours. Section renamed "The quarterback runs, in two steps", and the question is now "why a second step, and why it held". |
| §2.3 Light boxes already common in 2016 | Bullet now says so (38% in 2016, mostly vs three receivers), names 2017 as the decade's heaviest boxes (mean 7.0), flat 2018-22, then past half in 2024-25 (all FTN seasons). Opening reworded ("walked the other down toward the line"). |
| §2.4 "Two-high climbs steadily" with a 2024 dip | Caption and bullet say "with a 2024 dip that Next Gen Stats' own series doesn't show". |
| §2.5 Weak 10.0 vs 11.3 deep-attempt evidence | Replaced with 20+-yard gains per dropback by post-snap shell, every season 2018-2025 (two-high lower in every season; gap grew from about an eighth to about a quarter fewer). League aDOT trend (8.3 to 7.8) added to the Mahomes section for the "patience" point. |
| §2.6 Missing "#2 read" bridge | Two-high point 1 now states the quarters safety's rule (reads #2; comes down only if #2 blocks); "Why under center" reason 3 and fig 6's caption use it explicitly. |
| §2.7 Loop: McVay to Mahomes arrow; dashed arrow back to 2013 | Loop redrawn with five nodes (McVay/Shanahan and Mahomes/Reid merged into one offensive node), strict offense/defense alternation, dashed arrow ends at "2026: ?". Caption year range fixed (2013-2025). Redundant move/answer table after it cut. |
| §2.8 Mahomes section has no diagram | Added a static Jet Chip Wasp diagram (fig 3, horizontal, inside the film room) reconstructed from the published facts and 12-04's version, with a link to the case study's frame-by-frame. "Jet" explained as an unexplained protection word, per 04-08. |
| §2.9 Rules table missing 2023; OT whys | Added the 2023 fair-catch row (CBS Sports source) and a 2023 timeline entry; 2017 row explains why ("a long first-possession drive leaves the other team less time"); OT paragraph explains that a first-possession TD no longer ends the game. |
| §2.10 Drill 3 substitution premise | Rewritten per coach: same 12 personnel spread on the previous play (U split out), now compressed at tempo; nobody substituted, so the defense can't. Title now "heavy personnel at tempo". |
| §3 Fig 2 end in the QB's face; Z ring on SS; no Y ring | End now squeezes then chases late (still a few yards away at the throw); caption says "chasing but still a few yards away". Y has a gold ring. Z's release and the SS's step were moved so the rings no longer overlap; press corner starts deeper and bails. |
| §3 Fig 3 (light-box run): linemen, unblocked LBs, label, duplicate of 05-05 | Removed. The bargain now links 05-05's fig-light-box and spends the space on numbers (cost and what it buys). Animations: 2 (were 3). |
| §3 Fig 4 y-axis | Axis "share (%), see caption"; caption gives each line's denominator; direct labels say "% of dropbacks" and "% of designed runs". |
| §3 Fig 6 title collision | Titles shortened ("Snap · 12 under center vs two-high"), strip widened; no collision. |
| §3 Fig 7 move TE as wing; EDGE pointer | Y moved to a clear slot spot (w = 9.5, off the line); label reads "EDGE (both E's)". Mike/Will swapped (coach 16). |
| §3 Fig 9 label on wrong line | Direct labels replaced by a legend clear of the lines; Romer/Belichick notes moved down. |
| §3 Fig 1 half-year offsets; "offensive moves" | Every box now sits on its season's row (items merged); caption and intro say "moves and the results they won". |
| §3 Drill 3 "7 blockers" label gives away the answer; box ends at U | Label removed (the drill now asks you to count); box widened to include the wing. |
| §3 Half-blank print pages | Typst figure placement set to auto for the body (as in 12-01), reset before the drills; no half-blank pages remain. |
| §4 Length and repetition | Cut: repeated NGS two-high numbers (now once, in the bullet), repeated Seattle 53% (once, in "Why under center"), the duplicate 2026-rules paragraph (now in the table row), the NFCCG film room (halved), the "aggression spread" paragraph, the analysts bullet (unsourced), the move/answer table, the light-box animation, and trims throughout (three forces, Why it exists, Rams 2018, Mahomes, two-high history, options and reasons lists, misconceptions, positions, QB reasons, Seahawks film room, drill answers, takeaways). **Partly declined:** the net body is roughly level with the old draft, not 2,500 words shorter, because both reviews asked for additions (Wasp diagram, motion, tite front, #2 rule, defenses vs the running QB, a two-high film room, the shell-vs-coverage explanation, 2026 pointer, drill 3 option, drill 2 harder version). Those were judged worth more than the remaining cuts. |
| §4 Overlap with 05-05 / 06-06 | Light-box figure removed (05-05 link); the Staley 2020 Rams film room was not added (it is in 06-06); the new two-high film room uses the Eagles' post-snap rank, which neither chapter has, and links 05-05 for the front. |
| §5 Drill 2 too easy | Added a "harder version" (the tight end splits out 6 yards: five blockers against six). |
| §6.1 Under-center dip real? | Answered in the bullet (FTN's own flag shows the drop). |
| §6.2 Public pre-snap two-high stat? | Answered: none free and league-wide; link to 06-06. |
| §6.3 What offenses did through the air | aDOT trend added (shorter throws, same deep-shot share). |
| §6.4 What Macdonald's pressure looks like on TV | One-sentence description in the Seahawks film room plus a link to 07-03's two-high simulated-pressure figure. |
| §6.5 Five weeks into 2026 | New "Go deeper: check the 2026 season yourself" callout: FTN charting updates weekly; participation arrives after the season; an `eval: false` snippet for 2026 under-center share. |
| §6.6 How defenses play the running QB | New paragraph: spy, lane-discipline rush, safety down (each with its cost), link to 05-05. |
| §6.7 Why 11 personnel barely moved | Stated in the third trend bullet: the fight was over alignment, motion and the safeties until 2025. |

### Coach review

| # | Action |
|---|---|
| 1 | Drill 3 premise and answer wording fixed as suggested. |
| 2 | Eighth, not ninth; SS and Sam moved; caption fixed; the seam throw on a boot is now "a different call off the same fake, without the boot"; boot read stated high to low (X, Z, F). |
| 3 | Both strips rebuilt so QB and back meet at the mesh (about 0.8 s, QB about 4.6 yards deep) before the boot or drop; the 0.8 s panel shows them together. |
| 4 | Z's post now stems to 12 yards before breaking; throw at 2.6 s; SS fits at about 6.5 yards. Catch-depth titles computed from the play. |
| 5 | Title collision fixed. |
| 6 | End lags (squeeze, then chase with delay); caption rewritten. |
| 7 | Misconception now says the safety becomes an alley defender when #2 blocks. |
| 8 | Tite front added to two-high point 2 with glossary link to 05-03 (corrected placement: two 4i's on the *tackles'* inside shoulders, per 05-03's glossary; the review said guards). |
| 9 | Rams 2018 film room: covered interior linemen, no double teams; Bears 2018 "not yet two-high"; Staley (Bears OLB coach 2017-18) carries the idea to the Rams. The stronger claim that Fangio built his Denver system from that night was not sourced, so it is not made. |
| 10 | Two-high section now has a film room (Eagles 2024, shell vs coverage). The 2020 Rams version was declined because 06-06 already has it. |
| 11 | New "Motion: making the shell decide early" subsection: PFF 43.0% (2018) to 63.9% (2025), ESPN motion at the snap about 4% (2017) to 22% (2023), 2023 Dolphins 59%; sources from 02-06, kept as separate series. |
| 12 | McVay radio habit added with Goff's 2017 quote (Rams.com via 04-08); jet motion named specifically. |
| 13 | RPO/QB "plus one" clause added to the box arithmetic. |
| 14 | Star dialect stated (sourced to The Ringer on Ramsey as "Star"); Chancellor reworded. The Saban "Money" detail was not added because there is no source for it in the book. |
| 15 | Ravens personnel reworded (Andrews, Hurst, Boyle; Ricard). **Declined:** naming a signature concept, since 12-05 owns the detail and nothing here is sourced. |
| 16 | Mike and Will swapped; hybrid ring stays on W. |
| 17 | High-low on the $ added; "nobody left in the hole" note moved off the FS (now beside the catch). |
| 18 | "Shift the front" option added to answer 3. |
| 19 | 2023 kickoff row added. The roughing-the-passer swap was not made (that rule isn't in FACTS-current or the fact-check). |
| 20 | Label removed (see beginner §3). |
| 21 | Corners now drawn pressed in fig 2; text says "press corners". Fig 5 (two snaps) left at its static off alignment, which matters only for counting. |
| 22 | Loop caption range fixed. |
| 23 | QB caption recast (staircase, 2020 step). |
| 24 | "Jet" explained as an unexplained protection word. |
| 25 | Moot: the light-box animation was removed. |

### Not changed in gridiron
Nothing was edited in `gridiron/`. The chapter's own helpers (`snapshot`, `strip`, `pointer`, `say`, `box_outline`) handle the frame strips and labels, as before.
