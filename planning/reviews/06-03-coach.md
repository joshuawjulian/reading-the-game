# 06-03 Cover 3: Sky, Buzz, Cloud, and Seattle's Match Version: coach / film-analyst review

Reviewer role: veteran NFL coach and film analyst. Scope: football correctness, every diagram (rasterized
`pdfs/06-03-cover-3-family.pdf` at 80 and 150 dpi; all 13 figures, both frame strips and both charts looked at), strip
timing, missing nuance, film room, gridiron use. I did not edit the chapter.

**Overall:** a strong, well-taught chapter. The core football is right: 3 deep/4 under, corners' and post safety's rules,
the curl-flat vs seam-flat distinction (the best part of the chapter), force/alley ownership by rotation, the eight-man
front logic, the four classic holes, and the Mable/MEG trips check. The Seattle personnel facts are right, and so are the
corner sides (Sherman on the defense's left). The problems are a few diagrams and answer texts that contradict the
chapter's own tells (the sky/buzz pre-snap safety spot, the cloud safety width), a check-down labelled "in the flat"
that isn't, an unrealistic nickel/LB assignment in the buzz picture, and a "count three deep" heuristic that misfires on
Tampa 2.

Priority: **P1** = misleading football, fix before publishing; **P2** = a coach would object; **P3** = polish.

---

## P1: must fix

### 1. Drill 2 answer: the free safety's width is not a tell as drawn (l. 1335-1352; also fig-cloud l. 784-785)
The answer says the FS is "only about 5 yards from the middle of the field, narrower than a Cover 2 safety (who would be
outside the hash)." NFL hashes are 3.1 yards from the middle (the chapter's own `HASH_W`), so a safety 5 yards from the
middle is **already about 2 yards outside the hash**. That's a normal NFL two-high width, so the stated tell isn't there.
**Fix (diagram):** in `pp2`, set `"FS": (13.0, -2.0)` (inside the left hash, shaded toward the ball) and keep the SS wide at
`(12.0, 11.0)`. Do the same in `CLOUD_PRE`: `"FS": (13.5, -2.5)`. This also moves the FS ghost off the "hook (W)" box edge.
**Fix (text, answer 2):** "The free safety's alignment helps: he's inside the hash, almost over the ball, while the
strong safety is wide over the squatting corner. Two Cover 2 safeties would be balanced, each on or outside his hash. A
safety cheated toward the middle is already halfway to the deep middle third." Update fig-predict-cloud's caption to
match ("about 2 yards left of the ball, inside the hash").

### 2. Sky figure contradicts the chapter's own sky/buzz tell (fig-cover3-sky l. 405 vs l. 1231-1233 and l. 1260-1261)
"Recognising Cover 3" teaches: *a down safety outside the slot or tight end suggests sky; one inside over the slot with a
nickel outside suggests buzz.* But in fig-cover3-sky the sky SS starts at `(11.5, 5.0)`, which is **inside** the flexed TE
(Y at w=9), over the guard-tackle and inside the hook box. That's almost the buzz SS's spot `(11.0, 3.0)`. A reader who
compares the two figures finds no difference in the safety. The ghost also collides with the "hook" zone label on the
right.
**Fix:** `two_state(spread(), C3_PRE | {"SS": (9.5, 9.8)}, C3_POST, ...)`: the sky safety at 9 to 10 yards over or just
outside Y, the classic "cheated" sky spot that the text describes. The path to the curl-flat `(9.5, 12.5)` becomes
mostly outward. That is what sky is supposed to look like, and it clears the label.

### 3. Match strip: the check-down is not "in the flat" (fig-verts-match l. 943, 1020, 1029, 1036-1042)
The RB's route ends at `(3.6, 3.4)`, a yard or so past the line just outside the right tackle. That's a short
check-down, not the flat (the flat starts around the numbers, w≈12+). The caption says "checks down to the back (R) in
the flat, where the Mike (M) ... rallies." A coach would also point out that the chapter's own "What it gives up" says the
flat is exactly where match is weak when both seam-flat players carry. So a real flat route *should* be open-ish, not
tackled by the Mike for 4 yards.
**Fix (minimum):** change the caption and panel tag to "checks down to the back just past the line, outside the tackle,
where the Mike, who matched him, rallies." **Better (teaches the cost):** send the back to the flat
(`[(-4.6, 2.6), (-2.0, 7.5), (1.5, 13.0)]`, `pass_to("RB", t=2.6)`) and change the Mike keyframes to rally out
(`(1.6, 7.0, 5.0), (2.6, 5.0, 9.5), (3.4, 3.0, 12.0)`). Then rewrite to "the back catches it in the flat that the carries
emptied; the Mike, matched to him, has to run him down from the hook. Gain of 5 or 6, the price of carrying both
seams."

### 4. "Count three deep" also catches Tampa 2 (l. 1240-1243, 1263-1264; curriculum's Watch-for-it line)
Tampa 2 shows **three** deep defenders one second after the snap: two half-field safeties plus the Mike running the
middle. A reader following "three means the Cover 3 family" will call Cover 3. Add the discriminator in both places:
"Check *who* the three are. In Cover 3 two of them are the corners, deep and wide. If the corners are sitting in the flats
and the middle man is a linebacker running down the seam-to-seam middle, it's Tampa 2
([Cover 2 and Tampa 2](06-04-cover-2-and-tampa-2.qmd))." While there, "one means Cover 1 or a robber" is fine. Note too that
Cover 1 *robber* (Cover 1 with a robber) is still Cover 1.

---

## P2: a coach would object

### 5. Buzz figure: the nickel and Will are on the wrong receivers (fig-buzz l. 742-745)
The figure has the **nickel apexed over the flexed tight end (Y)** and the **Will linebacker walked out over a WR slot (H)**
as a curl-flat defender. NFL 4-2-5 teams do the opposite: the nickel (a DB) takes the wide-receiver slot, and a
linebacker or safety takes the tight end. A linebacker as the curl-flat player over a slot WR is the matchup offenses hunt.
**Fix (keeps the right-side buzz and all the BUZZ_POST spots):** swap H and Y for this figure only, so the TE is the left
slot and the WR the right slot:
`off_b = [q.moved(w=-q.w) if q.key in ("H", "Y") else q for q in spread()]` (or build it by hand: `O("Y","TE",-1.5,-9.0)`,
`O("H","WR",-1.5,9.0)`). Now the nickel is over the WR slot (H) on the buzz side and takes the curl-flat. The Will widening
to the TE side's curl-flat is the natural LB-on-TE assignment, and the SS buzzes to the right hook-curl. Rewrite the
caption accordingly ("the nickel over the right slot (H), the Will over the tight end (Y) on the left").
Also make the buzz visible. The SS moves only from `(11.0, 3.0)` to `(9.5, 6.2)`, about 3.5 yards, so the ring sits
almost where the ghost is. Start him at `(12.5, 5.0)` (12 to 13 deep, over the inside shoulder of #2) so the downhill
"buzz" path reads at a glance. That also matches tell #2 (buzz: safety inside, over the slot, nickel outside).

### 6. The match rules contradict the Seattle description; say that both versions exist (table l. 1008-1013, fig-verts-match, l. 1105-1108)
The table and match strip have **both** seam-flat defenders carry both #2s with the FS "free" over the top. The Seattle
section (and its cited source, Matty Brown) says the **down safety carries one seam and the post safety leans 60-40 to the
other**. Both are real and common. But the reader gets them back to back with no reconciliation and will think one is
wrong. Add one sentence after the table: "Staffs split on the far seam. Some carry both #2s (as drawn here). Many, like
Seattle, carry only the seam on the rotation side and give the other one to the post safety, who leans to it. That keeps
the weak-side curl-flat defender home for the flat and the curl." Change the FS row to "the #2 away from the rotation (in
many versions), or both #2s; the quarterback".

### 7. "Mostly by playing one coverage" is too absolute for Seattle (l. 1080-1082, 1110, takeaways)
Seattle's identity was single-high: **Cover 3 and its man twin Cover 1 (man-free)** from the same press, one-high look.
Cover 1 was especially common on third down and in the red zone, and in Super Bowl XLVIII. That pairing is *why* the
press-bail corners mattered: the quarterback couldn't tell a bail from man before the snap. Fix: "mostly by playing one
pre-snap picture, a single high safety and pressed corners, and two coverages behind it, Cover 3 and its man twin
Cover 1." Add the same point to item 3 ("press and bail looks like press man until the corner turns").

### 8. Cloud corner "jams Z" from 5 yards off (fig-cloud caption l. 783, label l. 795, text l. 808-810)
A corner 5 yards off can re-route but can't jam. Pick one. (a) Align him in press at 1 to 2 yards (`"RCB": (1.5, 16.4)`),
which is how many teams play a "hard" cloud. Then "jam #1 and sit in the flat" is right, and the pre-snap tell becomes "a
pressed corner with a safety stacked deep over him." Or (b) keep 5 yards and say "re-route #1, then sit in the flat."
Make drill 2's caption agree with whichever you choose.

### 9. Spot-drop four-verts timing (fig-verts-spot l. 939, 966-974)
The ball is thrown at 1.75 s, when H is only about 12 yards downfield (panel 3), and arrives at 3.5 s: **1.75 s in the
air** for about 33 yards of travel. NFL seam throws against Cover 3 from the gun usually come out around 2.2 to 2.5 s,
with the receiver at 15 to 18 yards and just past the curl-flat defender, and land about 1.0 to 1.2 s later. As drawn, the
QB is throwing to a receiver who hasn't cleared the underneath zone yet, which undercuts the "every defender did his job"
point. **Fix:** `p.pass_to("H", t=2.35)` and stretch the FS lean so he is still right of the ball at the throw (e.g.
`(2.3, 19.6, 3.6)` before he breaks back). Then `SPOT_T = [0.0, 1.0, 2.35, T_CATCH]` and retitle "+2.4 s · the throw".
The catch should land about 3.4 to 3.6 s, around 25 yards.

### 10. Two-high run defense is undersold (l. 604-606)
"Two-high coverages ... usually play seven against seven, or bring a safety down late." Quarters exists largely *because*
its safeties fit the run from 8 to 10 yards as alley players, reading the #2/tight end. Fix: "Two-high coverages keep both
safeties 10 to 14 yards deep. They can still fit the run (quarters safeties are taught to fill the alley), but they
arrive a beat later from depth. Cover 3 puts the eighth man there from the start."

### 11. Film room (Seattle 2013) needs one checkable snap (l. 1117-1132)
"Find any wide shot" is a viewing guide, not a film example. Anchor it on one play the chapter's own source breaks down.
Matty Brown's SI piece (footnote `[^match]`) analyses Chancellor in Super Bowl XLVIII. Use his first-half interception of
Manning, or a snap the piece diagrams, with quarter and situation, and describe the rotation on *that* snap. **Verify the
specific snap against the article before writing it**; don't reconstruct it from memory.

---

## P3: polish

12. **fig-curl-vs-seam-flat, left panel:** the "breaks to the flat on the throw" arrow points at an empty flat. Add a faint
    RB or #2 flat route (alpha 0.4), or end the caption sentence with "(not drawn)". In the right panel the CB has no ghost
    or drop while the left one does; make them consistent.
13. **"Wall" wording (l. 553-554):** from a 5-yard apex the defender usually meets #2 at 5 to 7 yards, so the wall is
    mostly *leverage* (body in the inside path, forcing him to run around) with contact only inside 5 yards. Say "gets in
    his path (any contact must come within 5 yards)" rather than "pushes him a step outward".
14. **Terminology dialects (add 2 to 3 sentences to the Madden box or a Go-deeper):** "cloud" and "sky" are also the names
    for the corner-flat and safety-flat sides of split-field coverages (the "cloud side" of Cover 6), which 06-06 and drill 2
    both lean on. Many staffs also have a **weak rotation** (rotate away from strength, to the boundary, or to the back).
    Saban-tree teams declare the rotation with "Rip/Liz" (already in a footnote; worth one line in the text). The
    rotation rule "rotate to motion" is why **motion** is the offense's way to find the rotation. Add to Watch for it:
    "When a receiver motions across, watch the safeties: if they rotate with him, it's a single-high rotation."
15. **BDB Go-deeper (l. 1286):** name the real PFF labels so the reader can find the variants this chapter teaches.
    The 2025 BDB `pff_passCoverage` includes `Cover-3`, `Cover-3 Seam` (curl-flat players carry the seams, the match
    idea), `Cover-3 Cloud Left/Right` and `Cover-3 Double Cloud`. Verify the exact strings against the data dictionary.
16. **fig-cloud:** the SS ghost `(12.5, 11.0)` butts against the end of the "hook-curl (M)" label. Nudge the ghost to
    `(12.5, 11.8)` or the label to `label_d=11.6`.
17. **Drill 3 (fig-predict-flood):** football is right. Optional realism: the play-side hook defender (Mike) usually
    expands toward the curl when #2 goes outside and #3 goes to the flat ("hook to curl"). Moving his drop to
    `(9.5, 7.5)` shows that he still can't reach the flat, which strengthens the answer.
18. **fig-eight-man-front:** the line-to-gain stripe at 10 yards runs just under "8 defenders in the box" and the two
    "deep ⅓" labels. Pass `to_go=None` (it's not a down-and-distance picture) to declutter.
19. **Facts to route to the fact-checker (not in FACTS-current):** Bradley as 2025 49ers assistant head coach and as
    Titans DC in 2026 (l. 1144-1145, `[^tree]`). The FACTS table lists Saleh as Titans HC but not his DC.

## What's right and should stay
- Curl-flat vs seam-flat ("a place" vs "a receiver") and the order "seam first, flat second, curl last".
- Force/alley ownership: sky = safety is force, buzz = safety is alley and the outside defender is force, cloud = corner
  is force.
- Corner technique (7 to 9 off, outside leverage, stay deeper than the deepest in the third, concede the hitch), post
  safety depth, thirds geometry (seams at ±8.9, between hash and numbers).
- Flood and curl-flat stretch explanations; play-action as the eight-man front's punishment.
- Mable / MEG trips check and the backside-corner tell.
- Seattle personnel (Thomas 14th pick 2010, Chancellor rd 5 2010, Sherman rd 5 2011, Maxwell rd 6 2011, Browner from
  Calgary 2011), Bradley/Quinn/Saleh timelines, 2012 to 2015 points-allowed streak, XLVIII 43-8.
- Formation legality in every figure (7 on the line; X/Z off the ball in the 12-personnel and I-form pictures), 4-3 over
  front alignment, and two animations (within the limit) whose strips tell the story in print.
