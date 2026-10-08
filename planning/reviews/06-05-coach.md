# 06-05 Quarters and Match: coach and film review

Reviewer role: veteran NFL coach and film analyst. Scope: technical accuracy, diagrams, nuance, film room.
Source reviewed: `chapters/06-pass-coverage/06-05-quarters-and-match.qmd` and `pdfs/06-05-quarters-and-match.pdf`
(PDF newer than the qmd; all 22 pages rasterized at 120 dpi and every figure inspected).

**Verdict:** strong chapter. The read-safety framing ("quarters safeties play #2, not a zone"), the
MOD/MEG contract and the source-break discussion are what a real staff would teach. Diagrams are
mostly legal and realistic, and no label is clipped by a field edge. Nine items need fixing before
it ships: four technical errors (the TE-side safety alignment, "blocks down", the Palms corner's
alignment and the Palms rule against smash), one dialect inconsistency with 06-01 (Fangio's Cover 8),
one film-room characterization the data contradicts (the Rams and Broncos as "quarters base" teams),
and three nuances a coach would insist on.

---

## A. Technical errors (fix)

### A1. Fangio's "Cover 8" sentence contradicts 06-01 (Cover 6 section, around line 705)
Text: "in Vic Fangio's vocabulary the same idea is called Cover 8." 06-01 (body and the `fangio8` note,
citing Cody Alexander) says Fangio's Cover 8 is the **sister call that puts the Cover 2 half toward
the passing strength (the nickel or slot side)** and quarters away from it. The 3x1 diagram here puts
quarters toward trips and the half on the lone receiver, which is the *opposite* of what Fangio calls 8.
**Fix:** "Dialects differ: in Vic Fangio's system the split-field family is Cover 6 and
[Cover 8](...), and his Cover 8 flips the halves, putting the Cover 2 half toward the passing strength
([Coverage Fundamentals] has the dialect notes)."

### A2. TE-side safety alignment: the text says one thing, Fig 1 shows another (and Fig 1 is right)
Text (bullets after Fig 1, the "That also explains where the safety stands" paragraph, Predict 1
caption): the safety stands "a few yards inside the slot receiver or tight end." In Fig 1 the SS is
at w = 6.5 and Y at w = 4.8, so he is ~1.7 yd **outside** the attached TE, which is how real teams
align him. Against an attached TE the safety stacks over him or a yard or two outside, because the TE
is already inside the box. "A few yards inside #2" only applies to a detached slot.
**Fix:** "a few yards inside a slot receiver; over or just outside an attached tight end."
Apply the same fix to the Predict 1 caption ("a couple of yards inside the slot and the tight end").

### A3. "Y blocks down on the end" (Fig 2 caption, right panel)
The SDE is a 9 technique, **outside** Y (`sde_9=True`). A block on a man outside you is a base, drive
or reach block, not a down block (a down block goes inside). **Fix:** "Y fires out low to base-block
the end outside him." The run-fit strip caption ("fires out low to block the end") is already correct.

### A4. Palms corner alignment: "a little inside #1" (Fig 7, Predict 3, the "How do you spot it"
paragraph, Watch-for-it bullet)
Palms and 2-read corners align **5 to 7 yards off, head-up to slightly outside #1, with their shoulders
and eyes turned in to #2**. The trap is an outside-in drive on #2's out or flat route, so an inside
alignment lengthens his path to the throw and gives away the fade if #2 goes vertical. The drawing
also contradicts the chapter's own advice. Predict 3's answer suggests "a quick slant by X, inside a
corner whose eyes are on H," but the drawn corner stands inside X, so the slant runs straight into him.
The real tells are **depth (a yard or two shallower) and eyes/hips turned inside**, not inside leverage.
**Fix:** in `palms_play()` and `pr3`, set `LCB` to about `(6.3, -15.9)` (head-up to a half-yard outside
X at w ≈ -15.3). In `palms_play()` change the drive `p.path("LCB", [(3.0, -14.6)] ...)` to about
`(3.5, -15.0)` so he comes down outside-in onto the out. Reword "lined up a little inside #1" to
"square or slightly outside #1, but with his eyes turned to the slot" in the Fig 7 caption, the
spotting paragraph, Watch-for-it bullet 1 and the Predict 3 caption and answer.

### A5. Palms against smash contradicts the Palms rule as written
Text: "Against smash … the safety carries [#2's corner route], and the hitch runs into the corner
sitting in front of #1." But the bullets just above say that when #2 is vertical "the corner stays
on #1, and it plays like quarters," and under quarters' MOD a 5-yard hitch means the corner **zones
off** to his deep quarter. Most 2-read/Palms teaching makes the corner **man on #1 whenever #2 does not
break out**, with no MOD release, which is why he can squat the hitch. **Fix:** change the third Palms
bullet to "If #2 goes vertical, the safety carries #2 and the corner plays #1 man to man (in most
versions without the MOD release), so a short route by #1 runs into a corner who is already shallow
and squeezing." Then the smash sentence follows.

### A6. The TE-side flat is ownerless in Fig 2 (middle panel) and never addressed
Against 11 personnel with the TE attached, the nickel apexes the slot side, so the TE side has **no
apex/overhang defender**. In Fig 2's middle panel Y runs to the flat (w ≈ 12) and nobody goes there:
the Mike's arrow climbs to the hook at (8.0, 3.5). The caption hand-waves ("the apex defender or a
linebacker takes the flat"). A coach would name him: the Mike (strong hook) **expands to the flat as
the first man out**, or the 9-technique end chips Y and sinks. This is also a real quarters stressor:
the TE flat or arrow is a staple throw against nickel quarters. **Fix:** in `read_panel` "out" branch,
change `p.drop("MIKE", (8.0, 3.5))` to `p.drop("MIKE", (4.5, 10.5), speed=4.5)` and the caption to "the
Mike, first man to the flat on the TE side, runs to it." Add one sentence after Fig 1's linebacker
bullet: "On the tight end's side there is no apex defender, so the strong hook linebacker (here the
Mike) is the first man to the flat if the TE releases outside."

---

## B. Film room (accurately characterized?)

### B1. Rams 2020 and Broncos 2022 were Cover 3-majority teams after the snap, and the boxes don't say so
I re-ran the course's own calculation (nflverse `load_participation` joined to pbp `defteam`, same
filters as the `rams`/`surtain` notes):

| Team | Cover 3 | Cover 1 | Cover 4 | Cover 6 | Q + C6 |
|---|---|---|---|---|---|
| 2020 LA Rams | **41.8%** | 15.0% | 20.6% | 15.5% | 36.1% (matches note) |
| 2022 DEN | **46.8%** | 16.9% | 15.6% | 17.7% | 33.3% (matches note) |

The quarters numbers are right, but the title "quarters and Cover 6 as a base" overstates it. Both
defenses **showed two-high and played Cover 3 more than quarters plus Cover 6 combined**, mostly by
rotating at the snap. That is the Fangio/Staley/Evero signature, and it is exactly what a film viewer
will see. **Fix:** retitle the Rams box "Rams 2020: the two-high shell and its quarters share". Add one
sentence to each box: "Their single most common coverage after the snap was still Cover 3 (41.8% /
46.8%), usually rotated down from a two-high look ([06-06]); quarters and Cover 6 were the next
biggest pieces, at well above the league rate." In "What to notice", tell the reader to expect
rotation on many snaps, so a safety who drops into the middle isn't a contradiction.

### B2. Broncos box: the MEG claim is a suggestion, so frame it that way
"A corner the defense trusts alone lets it play MEG on one side…" is fine as a teaching point, but
there is no cited evidence that Denver played Surtain MEG. Keep it as "what to look for" and soften
"Surtain is on an island by design" to "likely by design". (Also confirm for the fact-checker that
Evero is still Carolina's DC in the 2026 season. FACTS-current §DC table doesn't list Carolina.)

### B3. Michigan State 2013 and the Narduzzi, Iowa and Patterson history: accurate
Saban as Cleveland DC 1991-94, MSU 1995, Dantonio on the secondary, Narduzzi as DC 2007-14,
Dennard's Thorpe, Norm and Phil Parker, Patterson's flat-foot shuffle: all consistent with what I
know, and appropriately hedged ("rivals", "names vary"). The quote "can look like man a lot of the
time" plus "MOD from press" is the right lesson.

---

## C. Nuance a coach would insist on (add)

### C1. Backside safety = cutback, boot and reverse player (run-fit section)
The chapter teaches only the play-side safety's alley fill. Every quarters staff also teaches the
**backside safety's fit**: when his #2 blocks or the run goes away, he fills late inside-out as the
cutback defender and stays alert for boot, naked or reverse. In Fig 5 the FS stays deep because H
released. Add one sentence after "The other safety went with his receiver": "Had H blocked, the free
safety still wouldn't race to the ball. With the run going away from him he is the cutback player,
filling late and inside-out, and the first defender who has to see a bootleg coming back his way."
This also sets up the bootleg section better.

### C2. "Costs the offense nothing" is too strong (run-fit section)
A slot who releases on a run is one fewer perimeter blocker, and the nickel/apex is then unblocked
at the point of attack. Change it to "costs the offense little: one perimeter blocker".

### C3. Cover 6: what "most often calls for it" (Cover 6 section)
"Here it is against the formation that most often calls for it, a 3x1 trips set." In NFL usage Cover 6
is **most often a field/boundary call against 2x2 with the ball on a hash** (06-06's version). Against
3x1 most staffs first reach for their trips checks (poach, solo, MEG/"Mable"), and Cover 6 against
trips appears in both directions, with the half toward or away from trips. **Fix:** "Here it is against
a 3x1 trips set, one of the formations that calls for it, with the split made by formation."

### C4. Cover 6 FS width (Fig 6 and Predict 2)
The half-field FS at w = -10 / -10.5 with the ball in the middle is about 7 yd outside the hash,
roughly halfway to the numbers. That is wide for a deep-half player who also owns the backside post
and dig window. Typical: hash to 2-3 yd outside it, 12-14 deep, cheating outward only with the ball on
the far hash. **Fix:** `FS: (12.5, -7.0)` in Fig 6 and `(13.0, -7.0)` in Predict 2, and update the
captions to "12 to 13 yards deep, just outside the hash". The asymmetry tell still reads clearly.

### C5. Four verticals: name the one-on-ones (four-verts paragraph)
"Four verticals is the one call this defense was built for" (Predict 1 answer) is fair, but add the
coach's caveat. Every deep defender is now **man-to-man with nobody in the middle**, so a great outside
receiver against a MOD corner (fade, back-shoulder) and the back checking down against three
underneath defenders are the offense's answers. One sentence after Fig 3.

### C6. MEG panel (Fig 4 right): the corner's start is unrealistic
An off corner at 7.5 yd playing MEG doesn't get *in front of* a 2-yard slant, as the arrow to
`(4.5, -10.8)` implies; he trails it. Either start the MEG corner in press (`LCB` at about `(1.0, -15.9)`
for that panel only, matching Saban's "MEG from press") and keep the drive, or keep him off and draw
him trailing the slant from behind (`(5.5, -12.5)` then `(8.0, -8.0)`). The caption's "MEG needs a
corner the defense trusts" already says why.

---

## D. Diagram checklist (formation legality, labels, timing)

- **Fig 1 (Cover 4 vs 2x2):** legal (7 on the line: X, 5 OL, Y; H and Z off). Depths and leverage
  realistic; labels clear, none clipped. Only the A2 text mismatch.
- **Fig 2 (three answers):** legal and clear; fix A3 (caption) and A6 (Mike to the flat). In the
  run panel, the RB's track toward w = 6.5 runs outside Y, who is blocking the 9 technique: say "Y
  reaches the end" if you keep the outside track, or aim the back at the B/C gap.
- **Fig 3 (four verts):** correct match; see C5.
- **Fig 4 (MOD/MEG):** MOD panel correct (the 2-yard slant passed to $, the corner sinks under H's
  corner route, the FS carries). See C6 for MEG.
- **Fig 5 (run-fit strip):** 6 v 6 count correct, inside-zone blocking sensible (C to Will, RT to
  Mike, Y on the 9), timing reads well across 0 / 0.5 / 1.3 / 2.1 s. The "alley" note doesn't collide.
  Add C1 to the text.
- **Fig 6 (Cover 6 vs 3x1):** legal; see A1, C3 and C4. Minor: the "M: if #3 goes vertical, carry him"
  box straddles the dashed split line. Nudge it to `(8.9, 3.6)`.
- **Fig 7 (Palms strip):** story reads well in print (ball out about 1.05 s, arriving at the corner
  at 2.0 s; the FS clearly over X by +2.0 s). Fix A4 alignment.
- **Fig 8 (trend):** numbers match FACTS §10 (32.9 / 37.8 / 40.4 / 42.0; 2025 C4 17.2, C2 13.9, C6
  9.2) and the source break is marked. Cosmetic: in the bottom panel the "Cover 6 (nflverse)" and "NGS
  2025 (published)" legend entries sit on the dashed break line. Use `ncol=1` at `loc="upper left"` or
  move the legend to `loc="lower left"`.
- **Fig 9 (boot flood):** legal (X and Z off the ball; U and Y are eligible ends; 7 on the line).
  Front, run fake, boot path and three levels are all correct. Optional: the unblocked backside
  end on a naked boot is the play's real risk, worth a half-clause ("the backside end is left
  unblocked, so the fake has to hold him too"). The "S" (Sam) label isn't in the "Reading the
  diagrams" key: add "S the Sam linebacker (in a 4-3)".
- **Fig 10 (RB wheel):** concept correct and a real quarters beater (dig by #1 plus an inside route
  by #2 pulls both deep defenders inside, then the flat-to-wheel). Minor realism: the RB is offset to
  the **left** of the QB and has to cross behind him to wheel right. Align him to the QB's right
  (`RB.moved(w=+3.2)` or use a right-offset gun) so the release is natural. X is out of the window
  and H sits about 1.4 yd from the left edge; widen to `lateral=(-14, 26)` or accept.
- **Predict 1-3:** pictures legal and readable; first-down lines correct (2nd-and-8 from the 40,
  3rd-and-6, 2nd-and-4 from the 30). Predict 3 needs A4.
- **Animations:** two (run fit, Palms), well under the cap of four, and both strips tell the story in print.
- **Clipping/collisions:** none found apart from the two minor overlaps noted (Fig 6 Mike label on the
  split line, Fig 8 legend on the break line).

## E. Notes that need no change
MOD/MEG definitions and the Soran quotes; "four over two"; the Madden callout; the "trigger is a read,
not a call" contrast with 06-06; the nine-man-front framing; the play-action EPA footnote (honest that
play-action helps against every coverage); the wheel's "changes category" explanation; Watch-for-it
three-look sequence. Footnotes appear once each.
