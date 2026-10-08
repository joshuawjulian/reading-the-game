# 14-02 Scheme and Fantasy: coach / film-analyst review

Reviewed 2026-10-08 against the current `pdfs/14-02-scheme-and-fantasy.pdf` (built after the last qmd save),
rasterized at 60 and 150 dpi. I looked at every figure: 3 field diagrams (Figs 2, 9, 10) and 7 charts.
Facts were already checked (`14-02-factcheck.md`); this review covers football accuracy, nuance and diagrams.

**Overall:** strong and accurate. The usage chain, the TE "two jobs" idea, the goal-line point and the
coordinator method are all how a staff or a sharp analyst actually thinks. No formation is illegal and no
assignment is wrong. The fixes below are one label collision, two terminology slips, one overclaim, and
some coaching nuance worth adding, mostly in the coordinator section.

## Must fix

1. **Fig 10 (Predict 2): B and Q collide.** The green ring around B overlaps Q's disc (the `gun_trips` back
   sits too tight to the QB). Move B to about `w = -1.8` (keep `d` at the QB's depth, or 0.3 yd deeper) so
   both letters read cleanly. That is still a normal gun offset.
2. **Fig 10 / Answer 2: "trips" and "slot receivers" vs. an attached Y.** In the drawing Y is attached to
   the RT (on the line, in-line). 02-04 already teaches that 3x1 with the TE attached is what many teams call
   **trey**, not trips, and the answer calls "H and Y on the trips side" the "slot receivers", which Y is not.
   Pick one:
   - (preferred, more realistic for third-and-8 trailing by 10) detach Y into the #2 slot, about `d = -1.0,
     w = 8` with H moved to about `w = 11.5` and Z at about `w = 17`. That makes it true trips and makes
     "slot receivers H and Y" correct. Keep 7 on the line by putting Z on the ball (`d = -0.7`), or
     put X off and Z on. Count it before you render: 5 OL + X + one of the right-side receivers.
   - or keep the picture and change the caption to "3x1 with the tight end attached (trey)" and the answer to
     "H in the slot and Y, the attached tight end, are the other likely short targets".
3. **Fig 10: the dime defender's label.** Both extra DBs are labelled `$`. The library and 02-05 label the
   nickel `$` and the sixth DB `D` (`pos="DB"`). Change `D("D2", "NB", ...)` to `D("D2", "DB", 6.0, 5.0, "D")`
   so the picture shows dime the way the book taught it. Also link the first use of **dime** in the answer
   to its glossary/02-05 (the term is owned there).
4. **"a 50% difference produced entirely by the play-caller's taste" (PROE section).** Overclaim. Targets
   per game are all-situation numbers, so Arizona's 36 includes a lot of trailing (game script), and
   Baltimore's 24 is held down by Lamar Jackson's scrambles and designed runs (dropbacks that never become
   targets) as well as by taste. Say "produced mostly by the play-caller's taste, with game script and the
   quarterback's legs doing the rest", or compare neutral-situation targets per game if you want "entirely".

## Should fix (coaching nuance a staff would insist on)

5. **Fig 2's claim versus the chapter's own estimate.** The caption ends "Snap share can't tell these plays
   apart; route participation can." True for charted routes (PFF/FTN), but the on-field-dropback *estimate*
   this chapter uses for every later chart can't tell them apart either: both tight ends are on the field in
   both pictures. Add half a sentence to the caption: "...route participation charted from film can; the
   on-field estimate used in this chapter's charts cannot, which is why it is an upper bound for tight ends."
   It sets up the Go-deeper callout instead of quietly contradicting it.
6. **Fig 2: name the concept.** The left picture is a textbook max-protect play-action shot: 7 blockers
   (5 OL + Y + the back) against a 4-man rush, post by Z and dig by X, the "Yankee"-style post/deep-cross
   family with a drag underneath. One clause in the caption ("a max-protection play-action shot") tells the
   reader *why* Y stays in: the call itself buys the deep routes time. That is the scheme-to-usage link the
   chapter is about: some calls take the TE out of the route count by design.
7. **Target share: how play-callers actually feature a receiver.** "Gives that receiver the first read" is
   only part of it. Progressions are coverage-dependent (the first read against Cover 3 is often not the
   first read against two-high), so staffs feature a player mainly by (a) moving his alignment (slot, the
   boundary, motion) to get him the best leverage and matchup, (b) building "alert"/pre-snap answers to him
   when he gets one-on-one coverage, and (c) **manufacturing touches**: screens, jet/orbit-motion pitches and
   quick throws. Add two sentences; McDaniel's Miami (Hill and Waddle jet/orbit touches, Achane screens) is
   the perfect example and ties to the coordinator section.
8. **RB section: pass protection is the gate to the third-down role.** The single biggest reason a talented
   receiving back (often a rookie) doesn't get passing-down snaps is that the staff doesn't trust him in
   blitz pickup. It is in Answer 2 ("a back it trusts to pick up a blitzer") but belongs in item 3 of the RB
   list, linked to Pass Protection. Also worth one clause: **designed** RB targets (angle/option routes,
   screens: the Shanahan-tree McCaffrey usage) are worth more than check-down targets, and they travel with
   the play-caller.
9. **Coordinator section: the head coach shapes PROE too.** The method says "only the play-caller's
   fingerprint matters much", but run/pass identity is often the head coach's: Jim Harbaugh's run-first,
   ball-control football in LA and Dan Campbell's in Detroit. The Chargers' −10 PROE is credited to McDaniel
   ("both are McDaniel habits"); hedge it as "McDaniel's habit and Harbaugh's identity point the same way".
   Add a line to step 1: "and what does the head coach want the offense to be?"
10. **LA paragraph: McDaniel's target fingerprint is concentration, not spread.** Miami funnelled targets
    to Hill and Waddle (that offense was built around their speed). A spread Chargers target tree after four
    weeks is therefore *against* his fingerprint, which points to roster (no Hill-type receiver) rather than
    scheme. That is the paragraph's real fantasy lesson and it's currently missing; say it, and say which way
    you'd bet (the share consolidates on the receiver he can feature with motion, or it stays spread).
11. **Detroit paragraph: separate Petzing's fingerprint from McBride.** Arizona's ~one-third TE target share
    is partly scheme (Petzing comes from Kevin Stefanski's Browns staff, a multiple-TE, under-center,
    play-action lineage) and partly that Trey McBride was simply their best receiver for three years. One
    sentence makes the inference honest: the scheme part travels to LaPorta; the McBride part doesn't. Also
    note the 2025 "before" dot mixes Morton's and Campbell's play-calling.
12. **Kansas City paragraph: don't fully rule out the coordinator.** A non-play-calling OC in Reid's system
    still builds game plans, the run-game install and the situational packages. The jump to 39% under center
    and 37% play-action fits Walker *and* fits Bieniemy's influence on the run game; say the two can't be
    separated in four games rather than crediting Walker alone ("fits ... more than fits a new coordinator").
13. **Fig 9 (tush push) realism.** Legal and recognisable (7 on the line, QB under center, two pushers at
    his hips, 6-man goal-line front with A-gap tackles), so it's fine as "illustrative". Two tweaks make it
    look like the Eagles' version on film: move F and H up to about `d = -2.9` (tight to the QB's hips; the
    pushers are close enough to get hands on him at the snap) and the back to about `d = -4.6`, directly
    behind them, where he can act as the third pusher. Caption: "ten of its eleven players within about three
    yards of the ball" doesn't match the picture (SS at 3.6 yd, corner 9 yd wide); "nearly the whole defense
    within four yards of the line" is accurate.
14. **Answer 2: mention the draw.** Against dime with five in the box (4 DL + M), the one run a coordinator
    calls on third-and-8 is a draw or delay to B. It doesn't change the answer (still B touching it), but a
    coach would say it, and it is another reason B is the back on the field.

## Minor

15. **Game script paragraph:** "A team ahead late runs the ball" is the **four-minute offense**; link it to
    10-04 (owned there) at first use.
16. **Route participation for WRs:** "a wide receiver almost never stays in to block on a pass play" — true
    for protection, but WRs do lose routes on screens (they block for the screen) and on some RPOs. One clause
    explains why even a WR1 sits at 90-95%, not 100%.
17. **Standard scoring:** "minus two for an interception" — fine as typical; Yahoo uses −1. Optional "(−1 at
    some sites)".
18. **Dead helper:** `pointer()` is defined but never used; delete it.

## Diagram checklist

| Fig | Legal | Alignments / assignments | Labels | Notes |
|---|---|---|---|---|
| 2 two jobs | Yes (7 on: 5 OL + Y + U; X, Z off) | Realistic 4-2-5 two-high vs 12; protection counts correct (7 vs 4 left, 6 vs 4 right) | Clean, inside the window | Items 5, 6 |
| 9 goal line | Yes | Realistic goal-line 6-man front; pusher depth a touch deep | Clean; "goal line" label inside | Item 13 |
| 10 third-and-8 | Yes (X, 5 OL, Y on) | Dime is realistic; Y attached = trey | **B/Q collision**; second `$` should be `D` | Items 1-3, 14 |
| Charts 1, 3-8 | n/a | Read correctly; the coordinator cards' noise bars and diamonds are clear | No clipping or collisions at 150 dpi | — |

No animations (none needed for this chapter's spec). gridiron use is sensible; nothing missing from the
library apart from the gun back offset, which is noted for the library owner: `offense("gun_trips")` puts the
RB close enough to the QB that the highlight ring overlaps him.
