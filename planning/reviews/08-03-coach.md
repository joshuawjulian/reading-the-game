# Coach / film review: 08-03 The Game Plan: A Week Inside an NFL Building

Reviewer role: NFL coach and film analyst. I checked the qmd and the PDF, both built 2026-10-08 00:12. I rasterized all
20 pages at 80 dpi and the figure pages (3, 5, 8, 9, 10, 11, 13, 16, 18, 19) at 130 dpi
(`_pdfbuild/08-03-game-planning-week/coach/`). I looked at all 11 figures, including the frame strip. I checked the
staff and play-caller claims against FACTS-current §C/§staffs, and they are all consistent.

**Overall:** this is a strong, honest chapter. The week's calendar, how QC work differs from analytics work, the
tendency-report cautions, the script data and the Reid and Walsh material are all right, and a staffer would recognize
them. The problems are concentrated in the **sample-game thread**: the matchup grid, Fig 5 and 6, the call sheet and
Predict 2 contradict each other about who covers Y. There are also **two alignment errors that a coach would flag
immediately**: the "bracket" in Fig 5 leaves the out-break open, and the "wide 9 stops outside zone" claim in Predict 3
is backwards. Finally, one label miscounts the box ("eighth defender"). Items are listed in priority order.

---

## A. Must fix (football is wrong or the chapter contradicts itself)

### A1. Who covers Y in "their usual" Cover 1: the Mike or the Will? The chapter says both
- Fig 3 (matchup grid) says the best pairing is **Y vs W (+2.0)**, with the note "in their usual Cover 1 the **Will**
  has the third receiver". The R-vs-M note says "the **Mike** follows [the back] in man".
- Fig 5 top (`their_usual()`) and its caption do the opposite. The **Mike** has Y ("M has Y: our best matchup", red
  ring), and the Will has the back.
- Predict 2 (Fig 10) and its answer go back to the grid version: M follows R, and W stays on Y, "exactly the cell
  circled on the matchup grid".

**Fix (one change, keeping the grid and Predict 2 as they are):** in `their_usual()`, swap the two linebackers' jobs.
Put `WILL` at `(4.5, 3.4)` with the man line to Y, and `MIKE` at `(4.5, -0.6)` with the man line to RB. Change the
loop to `("WILL","Y"), ("MIKE","RB")`, `p.highlight("WILL", color=RED)`, the label to "W has Y:\nour best
matchup", and the caption to "hand the tight end (Y) to the Will linebacker". `game_plan_dime()` already has M on
the back and a dime replacing "the Will". After the swap the whole thread is consistent.

### A2. Fig 5 bottom / Fig 6: the "bracket" is two inside defenders, so Y's out-break is wide open
D sits at `(2.8, 5.8)` and the SS at `(9.0, 4.4)`. **Both are inside** Y, who is at w = 6.5. A real TE bracket splits
the two breaks between the defenders. Either it is under/over (one defender underneath, the other over the top and
slightly outside) or in/out (one takes the inside break, the other the outside break). In the drawing, any out or
corner by Y beats both defenders, which is exactly the route the "Y Option" in the sample game would run against this
leverage. Frame 3 of the strip works only because Y chooses to break inside.
- **Fix:** make it an in/out bracket that matches the strip. Move D to **outside leverage, `(2.5, 7.3)`**, so he
  takes the out and anything underneath it. Keep the SS inside and over, at `(9.0, 4.6)`, so he takes the in and
  anything deep. In Fig 6, keep Y breaking inside into the SS and change D's path to a trail, `via (4.2, 7.0)` to
  `(5.6, 5.2)`. Caption: "D takes everything outside and short; the SS takes anything inside and deep: Y is
  bracketed whichever way he breaks." Move the "over the top of Y" leader target to match.

### A3. Fig 5 caption, bill (2): "only five defenders are left near the line" is not what the picture shows
In the dime panel, the box holds E, T, T, E, M plus D at 2.8 yards (D is closer to the line than the Mike). That is
six, the same count as the nickel panel. The real run bill is different. (a) A 190-lb defensive back has replaced a
linebacker as a run fitter. (b) The SS was a **robber**, a free run fitter in the middle, and is now tied to Y, so
nobody is left over to fill the alley. The red badge "2" is also floating in the offensive backfield at `(-3.2, 2.8)`,
pointing at nothing.
- **Fix:** rewrite (2) as "the robber is gone: the strong safety who used to fit the run in the middle is now tied to
  Y, and a defensive back has replaced a linebacker, so the run is cheaper than usual". Move badge 2 to the
  vacated middle, about `(6.0, 0.5)`, between M and the SS's old robber spot (and ghost the old SS spot at
  `(9.0, 1.5)` with a dashed outline if you like). The body text ("the defense is lighter against the run") already
  says this correctly.

### A4. Predict 3 (Fig 11): a wide-9 end does not take away outside zone. It is the front zone teams like to see
The label says "wide: the tight end can't reach him", and the answer says "the wide end makes outside zone to the
right nearly impossible". An outside-zone coach would push back. Against a wide 9, the tight end does not need to
reach him. He kicks or "fans" him wider, the C and B gaps get bigger, and the back presses the edge and cuts up
inside. That is why Shanahan- and McVay-style zone offenses have historically run well against wide-9 fronts. The
alignments that stop outside zone to the tight end set a **hard, attached edge**. The usual tools are a **7 or 6
technique on the tight end** (inside shade or head-up, which the tight end cannot reach), a **shaded 5 or 4i on the
tackle**, a **force safety** in the alley, and backside linebackers who refuse to overflow.
- **Fix (drawing):** change `SDE` to `technique("7", 1)` (inside shade of Y) or `technique("6", 1)`. Relabel it
  "7-tech on the TE: Y can't reach him". Keep the SS at 7 yards as the force player. Optionally turn the SDT into a 4i
  or 5 shade on the RT to show "the front is shaded toward the tight end". Right now the 3-tech/1-tech is just a
  normal over front, not a game-plan shade.
- **Fix (text):** in the answer, replace "the wide end makes outside zone to the right nearly impossible (the tight
  end can't get outside him)" with "the end is set inside the tight end, so Y can't reach him and the edge is set
  hard".

### A5. Predict 3 label: "SS down: an eighth defender to that side" miscounts
The box holds E, T, T, E, S and M, plus the SS: seven defenders, because the Will has left to cover H. "Eighth" is
wrong both overall and to that side.
- **Fix:** "SS down: a seventh man in the box, on the TE side". The answer already uses "an extra run defender on that
  side", which is correct.

### A6. Predict 2 answer vs the call sheet: "probably the first call in the '3rd & 3-6, vs man' box"
On Fig 7, the first call in that box is "Gun Bunch Rt 70 Mesh". The Y option appears second, as "Gun Empty Fly 62 Y
Opt".
- **Fix:** put the Y option first in the vs-MAN pair, for example `"vs MAN:   Gun Trey Rt Zoom Y Option"` ("Zoom" =
  back motions out, which matches Fig 10), with Mesh second. Or change the answer to "one of the two vs-man calls".

### A7. Predict 2 (Fig 10): the SS's spot contradicts the answer
The answer says "with the Mike outside, nobody is left in the short middle except the Will", and it describes Y
breaking "in or out". But the SS stands at `(8.0, 9.0)`, a lurk player 8 yards deep over the trips side (counting
CB, CB, $, W and M in man, the SS is a free **robber**). The W is at `(3.9, 4.4)`, two yards inside Y. The picture
already tells you the answer: **Y breaks out**, away from the Will's inside leverage. A robber over the trips side
would rally to that throw, though.
- **Fix:** move the SS to a middle robber spot, `(9.5, 1.0)`, and say in the answer: "the Will has inside leverage
  and the robber sits in the middle, so Y's option breaks **out**". This also teaches the reader to read leverage,
  which the answer currently waves at.
- Also add one line: a linebacker widening with a motioning back *suggests* man, but zone teams also "bump" a
  defender out with the motion. The tell is whether he **runs with** the back and whether the rest of the defense
  rotates (link [06-06](../../chapters/06-pass-coverage/06-06-disguise-rotation-and-split-field.qmd)). On third
  down, smart defenses disguise this deliberately.

### A8. The call sheet's "3rd & 3-6 vs ZONE" lists the same concept twice
"Gun Trey Lt 61 **Spot**" and "Gun Trips Rt 63 **Snag**" are the same concept: "spot" is the Air Raid name for snag,
corner-flat-spot. A coordinator would never spend both lines of a paired box on one concept.
- **Fix:** replace the second line with a different zone beater, such as `"Gun Trips Rt 60 Stick"` (stick is on the
  two-minute list too) or "Curl-Flat".

---

## B. Should fix (missing nuance a coach would insist on)

### B1. Seattle 2025 = Macdonald = simulated pressure. The tendency read "content to rush four and cover" needs that caveat
The numbers are right: few 5+ rushers on second-and-long and third-and-medium. But Macdonald's signature is the
**four-man pressure that doesn't look like four**: linebackers or defensive backs rush, and a lineman drops. So "the
extra rusher usually isn't coming" is true, while "routes that take a beat longer" can still face a free rusher from
an unexpected spot. The public data's `number_of_pass_rushers` cannot tell a sim from a plain four-man rush.
- **Fix:** add one sentence to the second-and-long / third-and-medium bullet: "But four rushers isn't the same as a
  plain four-man rush: Macdonald's defense is built on simulated pressure (linebackers or defensive backs rushing while
  a lineman drops), which this column can't see. So the protection plan still has to identify the fourth rusher, and the
  hot throw still has to be ready." Link the term to
  [07-03](../07-pressure/07-03-zone-blitz-and-simulated-pressure.qmd).
- Similarly for "two-deep shell 64%": FTN codes the **post-snap** coverage. The disguise tendency a staff would
  actually chart (how often a two-high *look* rotates to one-high at the snap) is not in this table. One clause in the
  Coding caution covers it.

### B2. Formation rule in "Matchup hunting": modern defenses often put a safety on a detached TE
"In a typical Cover 1 … the linebackers take the backs and tight ends." That was the old rule. Against a receiving
tight end aligned as #3, many NFL defenses now match a **safety** (or a big nickel) on him and give the linebacker the
back. That is why 3x1 with Y as #3 is a *question* rather than a guaranteed linebacker. Add: "good defenses answer with
a safety on the tight end, and then the offense has learned who the robber is (or isn't) this week." This makes the
dime plan in Fig 5 feel like the natural escalation it is.

### B3. Predict 1 (Fig 9): the light box is half the answer
With the Sam and Will walked out, the box holds five (E, T, T, E, M) against five linemen, with the SS at 8.5 yards.
The classic payoff of spreading out 12 personnel against base is **"they walked the linebackers out, so run it"**: a
numbers-advantaged run, or an RPO that throws to the tight end if the overhang widens late and runs if he doesn't.
The answer mentions running only for the case where the defense subs a nickel.
- **Fix:** add one sentence: "And count the box: walking two linebackers out leaves five defenders against five
  linemen, so the same formation is also a good run look. Many offenses carry a run-pass option from it that reads the
  walked-out linebacker."

### B4. Fig 6 timing and window
- `p.pass_to("X", t=1.75)` on a 14-yard comeback with a 2.5-yard gun drop is about half a second early. Real comeback
  timing from the gun is about 2.3–2.6 s, thrown as X breaks down. Use X `speed=7.0` and `pass_to("X", t=2.35)`, and
  move frame 4 to about 3.0 s. It still tells the story, and Y's inside break (frame 3) then happens *before* the
  throw, which is the right order for "QB sees the bracket close, then goes backside".
- Pick the bill route that matches the logic of "no deep help". With the FS gone, the corner on X has to protect the
  **post/inside**, so the comeback opens because he is playing inside leverage and a big cushion. Add that one clause to
  note 4 or the caption ("with no safety in the middle, the corner has to play the post, and the comeback opens
  underneath him"). Otherwise a coach asks why removing *middle* help beat an *outside* route.
- Frame window: the FS square touches the top edge in frames 2–4 (FS ends at d = 16.5 with window top 17.5), and $/H
  are nearly there in frame 4. Use `window=(-7.5, 19.5)`.

### B5. The call sheet is missing boxes every sheet has
For realism, add (or swap TWO-MINUTE into a narrower box to make room for) **"BACKED UP  -1 to -5"** (coming out)
and **"4-MINUTE"** (protect the lead). The body text names the four-minute offense on Friday but the sheet doesn't
carry it. Also worth one sentence in "(2) Ranked lists": real boxes are usually split further **by personnel or
formation and by hash** (left-hash and right-hash calls), which is why sheets are so dense. The 2-pt line "go if then
down 2 or 5" is ambiguous. Use "after TD, go for 2 if: down 2, down 5, up 1, up 5" or similar. It is illustrative,
but the wording should read cleanly.

### B6. Defensive call sheet: one paragraph
The chapter's sheet is offensive, and the text implies all sheets are filed by situation. Defensive sheets are filed
by **situation × offensive personnel/formation** (e.g., "3rd & 4-6 vs 11 personnel 3x1: Cover 1 robber / sim
'Viper' / Cover 2 man"). Add two sentences after the Shanahan paragraph so the reader knows the other sideline's sheet
looks different.

### B7. Special teams and game management are invisible in the week
A coach would note that the third phase gets its own plan: return and punt-rush schemes, and fakes the special-teams
coordinator found on film. Usually there is also a head coach's **game-management meeting** on Friday or Saturday
(timeouts, challenges, end-of-half, and the analytics card). Add "special teams" to the Coordinators row of Fig 1
(e.g., Fri: "2-minute plan; special-teams review; finish the call sheet"), and put one sentence in the Friday or
Saturday paragraph. The analytics row already hints at it ("decision card to the head coach").

### B8. Scripts are often conditional by field position
"Third downs, red-zone snaps and penalties all interrupt it." Add "and field position": many scripts carry
"backed-up" alternatives, because a scripted shot or a reverse is not what you call from your own 2. Walsh's scripts
had this. One clause is enough.

### B9. Script data: third downs are in the "first 15"
The scripts that the text describes are first and second down only, but `NEU` includes every down. For a fairer
test of "do scripted plays gain more", restrict both groups to downs 1–2. The answer will very likely stay "no", and
the footnote can say so. At minimum, add a sentence acknowledging it.

### B10. Who calls Baltimore's defense?
For the 2026 Ravens the chapter tells readers to watch both Weaver's Miami tape and Minter's Chargers tape. That is
correct, and it is the "who actually calls it" problem from the bullet just above. Say so explicitly ("with a
defensive head coach and a defensive coordinator who both called defenses elsewhere, who calls Baltimore's is itself
a scouting question until the film shows it"). This turns a list into a lesson.

---

## C. Minor / wording

- Film room XXV: Belichick's first head-coaching job was Cleveland (1991–95), so "first as the Giants' coordinator
  and then as the Patriots' head coach" skips it. Add "(and the Browns')" or say "as a coordinator and a head coach".
  If you want the vivid, verifiable detail: the Giants often played with only two down linemen and six DBs in that
  game. Verify it before adding.
- The Chiefs film room's last line says "Many of them come from that **Tuesday** index card", but the script card is
  written **Friday**. The new-play cards are the early-week ones. Say "from those early-week index cards".
- Call sheet: "Ace" means one-back **12** personnel in many Gibbs-tree languages, and "Trey" usually means an
  *attached* TE with two receivers to that side. The caption already says the names are invented, so this is fine,
  but avoid "Ace" in the text near the Predict 3 picture (11 personnel under center) so a knowledgeable reader isn't
  tripped up.
- Predict 3 answer: tie it to the sheet's **SHOTS "when SS walks down"** box ("Ace Rt Fake 24 X Post"), since this
  picture is exactly that trigger. It is a nicer payoff than the shot-down box alone.
- Paired calls (3): the "gives the quarterback both and lets him choose at the line" mechanism has a name, the
  **kill call** (or check-with-me), which 01-05 owns. Link it as
  `[kill call](../../appendices/glossary.qmd#gl-kill-call)` in the text, with a pointer to
  `../01-foundations/01-05-the-pre-snap-phase.qmd`.
- Players' Monday: after a win, many staffs give a "victory Monday". This is optional color.

## Diagram checklist (all looked at)

| Fig | Legal / realistic | Labels | Notes |
|---|---|---|---|
| 1 game week | n/a | clean | add special teams (B7) |
| 2 tendency report | n/a | clean | add sim/disguise caveat in text (B1) |
| 3 matchup grid | n/a | clean | consistent once A1 is done |
| 4 TE EPA | n/a | clean | fine |
| 5 take-away | 7 on line, legal; dime count OK | clean, but badge 2 floats in the backfield | A1, A2, A3 |
| 6 strip | OK | FS touches the top edge | A2, B4 |
| 7 call sheet | n/a | clean | A6, A8, B5 |
| 8 script data | n/a | clean | B9 |
| 9 Predict 1 | legal (X, Z on the line; TEs off) | clean | B3 |
| 10 Predict 2 | legal; motion lateral | clean | A7 |
| 11 Predict 3 | legal (Y attached, X on the line, Z/H off) | clean | A4, A5 |

No labels are clipped by the field edge in the static diagrams, and none collide. Footnotes are each referenced once.
