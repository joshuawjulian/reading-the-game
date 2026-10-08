# Coach / film review: 10-02 Third Down: The Money Down

Reviewed 2026-10-08. I rebuilt the PDF (`build_pdfs.py 10-02-third-down`, OK), rasterized it at 110 and 200 dpi, and looked
at all 11 figures. Overall the chapter is strong. The bucket logic, the sticks-route rationale, the trade-off framing and
the data are good, and the film rooms are well chosen and accurately characterised. There is one real diagram error: the
option route in Fig 2 breaks **short** of the sticks. That needs fixing because the whole section rests on it. The rest are
alignment and realism fixes, plus a few things a coach would insist the chapter mention.

## Must fix

### 1. Fig 2 (`fig-sticks-vs-cover1`): H's "option route at 8 yards" breaks at 6.5, short of a 7-yard line to gain
gridiron route offsets are measured from the player's **alignment**, not from the LOS. H is aligned at d = -1.5, so
`r.out(8, 5)` breaks at **6.5 yards**. In the render the out cut sits right on, or just under, the orange line. The caption,
the label ("breaks out at 8 yards, one past the line"), the body text and the hook all say 8.
- Fix: `p.route("H", r.out(9.5, 5))`, which puts the break at 8.0 past the LOS. Check that the ball's end point still lands
  at the cut. Re-render and confirm the cut sits clearly above the orange line.
- The same check applies everywhere else. Spy figure: H and Y run `r.out(8, 4)` from -1.5, so they break at 6.5 on
  third-and-6. Make it `r.out(9.0, 4)` (7.5 past the LOS) so the picture matches "a yard or two past". Rush-three figure:
  the H/Y digs at `dig(14, 7)` break at 12.5, which is fine. Draw figure: the receivers' depths are fine.

### 2. Fig 7 (`fig-rush-three`): label covers the FS, two identical digs collide, and the checkdown is mislabelled
- **Collision:** the "five underneath at 11–13 yards…" box (text at (17.2, -7.2)) sits on top of the **FS** marker (only the
  "S" shows). Move it to roughly (18.5, -13) with the leader to (12.6, -6.0), or put it on the right side at (17.5, 12).
- **Route design:** H and Y both run `dig(14, 7)` at the same 12.5-yard depth from opposite sides, so they meet in the
  middle, in the Mike's zone. No staff draws two digs at the same depth into each other. Use a real third-and-long
  concept:
  - Dagger: Y seam (`r.seam(18)`) and H dig at 13.
  - Levels: H dig at 12.5 and Y dig at 16.
  - Or keep one dig and turn Y into a sit at 13.
  The teaching point still holds: every window has a defender in it.
- **Checkdown:** the back's `r.flat(1.0, 5)` from d = -5 ends 4 yards **behind** the LOS, which is 16 yards short of a
  third-and-12, not "10 yards short" (label and caption). Either change the text to "open, ~15 yards short", or give the
  back a check-release that settles 2–3 yards past the LOS (for example `[(0,0),(3,2.5),(7.5,4)]`) so that "about 10 short"
  is true.
- Realism (optional): deep thirds at 22–25 yards are very deep, even with a three-man rush. Use 18–22 (CBs to about 19,
  FS to about 21) and change the label to match.
- Protection (optional): at present C and both guards all step to the nose, which is a triple team. Draw C plus LG doubling
  the nose and RG "looking for work" (a small step toward the RDE). That matches "two linemen spare".

### 3. Fig 4 (`fig-draw-vs-dime`, frame strip): the center never blocks the Mike, so the back appears to run past an unblocked linebacker
The center climbs to (3.8, 0.0) at 2.2 s and stops. The Mike comes down to (5.4, 0.9) at 2.9 s. The back runs through
that spot at 2.7–3.3 s. In the +3.3 s panel the **M sits underneath (behind) the ball carrier with the C below him, with no
contact**. A reader will see either "the Mike whiffed" or "nobody blocked him", which contradicts the caption ("the center
releases to block him").
- Fix: script the C to meet the Mike, e.g. `timed(p, "C", [(0.8, -0.2, 0.2), (2.2, 4.6, 0.4), (3.3, 5.2, 0.6)])`, and stop
  the Mike on him: `timed(p, "MIKE", [(0.9, 10.0, 0.4), (1.6, 10.0, 0.4), (2.3, 5.6, 0.5), (3.3, 5.6, 0.5)])`. Bend the RB
  path a yard to the right of that block (w ≈ 1.8–2.4 from 2.4 s on). The back should visibly cut off the center's block.
- Guards vs DTs: at 1.6 s the guards are at w = ∓3.0/3.2 while the DTs are at ∓2.8/3.4, so they are level or even outside
  their men, with the DTs between the guards and the LOS. On a draw the guards set, then ride the 3-technique and 1-technique
  **out and upfield**, staying on their inside shoulders to wall off the lane. Put each guard about 0.8–1.0 yard **inside**
  his DT (LG ≈ (-2.0, -2.0), RG ≈ (-2.0, 2.4) at 1.6 s). Also, the 1-technique (LDT at w = -0.7) drifting outward on his
  own is not realistic. Show the LG turning him out.
- Clarity: in the +3.3 s panel the dashed defender trails (FS and $ especially) form a large crossed triangle that reads as
  noise. Consider passing only the trails of M, FS, SS, $ and D in the last panel, or shortening the trail start to t = 1.6 so
  only the rally to the ball shows.

### 4. Predict-the-play 3 answer: "the middle at 6 to 8 yards" is the spy's lane
The spy is aligned at 5.5 yards directly in front of the QB, with his eyes on the QB. That means he sees the throw too. A
shallow cross or inside-breaking option at 6–8 yards runs right across his face, and spies rob that throw all the time. A
coach would answer:
- **Behind the spy and in front of the FS**: a dig or over route at 10–14 yards. Against Cover 1 with no robber, that hole
  is the vacated space.
- **Away from leverage outside**: an out or option-out against the inside-leveraged $ or SS.
- **Make the spy choose**: the back on an angle or option route right at him.

Rewrite the "Where to throw" paragraph along those lines. Keep the "make the spy choose" sentence.

### 5. Predict-the-play 1 answer: the sneak is not the run that "doesn't need a hat on every one"
Against a **double A-gap mug**, the QB sneak runs straight into the two extra defenders standing in the sneak's gaps. This
is one of the worst looks for it, and mugs are partly there to take it away. Replace that sentence with something like:
"A run is live only if the offense can account for the mugged linebackers. Against this look, the quick throw is the better
bet, and the sneak becomes a better call once a mugged linebacker shows he's dropping."

## Should fix (accuracy and nuance)

6. **Chiefs film room, last sentence of para 1** ("the all-out blitz with no deep safety, kept for the down when a quick
   throw short of the line doesn't hurt"). This contradicts the Cover 0 section, where Cover 0 is a **short-yardage** call
   (9% at 3rd & 1–3 vs 2% at 11+), and on short yardage a quick throw *does* hurt. Reword: "kept for third down, when a hot
   throw that doesn't get there ends the drive."
7. **"Medium (4–6) … blitzes to force the ball out"**: the chapter's own Fig 5 shows the blitz rate is *lowest* at 4–6 (about
   27%, vs about 30% at 1–3 and 38% at 7–10). Say "plays tight man, mixes in pressure, and leans on mugs and disguise" rather
   than implying it blitzes most there.
8. **Cover 0 timing**: "the ball has to come out in about a second" / "has a second or so" is too fast. An unblocked A-gap
   rusher reaches a shotgun QB in roughly 1.5–2 seconds. Coaches say "the ball's out under two". Use "well under two seconds".
9. **Option-route leverage in Fig 2**: inside leverage on #2 with a robber is legitimate. But with a robber or rat in the
   middle, the *more common* Cover 1 rule is for the slot defender to play **outside** leverage and funnel inside to the help.
   The text already covers the alternative. Add one clause so a reader doesn't think inside leverage is the default:
   "Many defenses would play the nickel outside here and trust the robber; this one is taking away the quick slant." Also
   mention the third branch of the option rule that coaches always teach: **against soft, head-up or zone, sit it down**
   (the Welker film room uses it, but the main explanation does not).
10. **Fig 6 (sticks defense) depths**: on third-and-12 the FS is aligned at **19 yards** pre-snap (`deep_d - 3`) and the CBs
    bail to 22. A free safety at 19 at the snap is unrealistic. Use FS at 15–16 (bail to 20–21) and CB landmarks of about
    18–19. On the left panel, the $'s drop arrow runs into the left CB marker; start the $ at w = -10.5 or end his drop at
    w = -11.

## Missing nuance a coach would insist on

11. **Protection is half of third-down offense, and the hook raises it without explaining it.** The QB who "points at a
    safety and shouts" is setting the **Mike / protection ID**. Add a short paragraph (or a "Go deeper" box) in the
    package or pressure section covering:
    - Third-down protections slide toward the pressure threat.
    - Six-man protection (the back staying in) answers five-man pressure. The cost is one fewer route.
    - "Hot" vs "sight-adjust" answers when the defense brings more rushers than the protection has blockers.
    - Simulated pressures are designed to beat the protection's *counting rules* ("who's the fifth?"), not just to show
      a blitz.

    This also gives the James White film room its other half: picking up blitzers.
12. **Two-man (Cover 2 man) and brackets are missing from the defensive families.** 2-Man means man underneath with trail
    technique and two deep safeties over the top. It is the classic third-and-medium/long man call against option-route
    offenses and is exactly what Belichick-era and modern defenses played on the money down. Bracketing or doubling the
    offense's best third-down receiver ("take away the guy") is the other half of the matchup point in the man-beaters list.
    Add a short paragraph after "Sticks defense", or fold it into the "Calls" paragraph.
13. **Four-man rush games (stunts and twists) on third down.** The most common third-down "pressure" is not a blitz at all.
    It is a four-man rush with a T-E or E-T twist, often from the NASCAR / four-DE front the chapter already introduces.
    Add one or two sentences in the pass-rushers paragraph.
14. **Empty formations**: offenses go five-wide on third down to spread the box, force the defense to declare man or zone,
    and get a linebacker on a receiver. Add one bullet under the man-beaters ("Matchups" fits) and to "Watch for it".
15. **Rush lanes against mobile QBs**: in the spy section, name the rush technique coaches use with a spy (**mush / cage
    rush**: rushers stay square and in their lanes rather than winning upfield). Also add the reason man coverage needs a spy
    more than zone does: **man defenders have their backs to the quarterback**, so nobody sees him take off, while zone
    defenders face him. That is the single most important "why" for the spy and it is not stated.
16. Terminology dialects: in the Cover 1 discussion, note that the middle-of-the-field low player is a **robber**, **rat**
    or **hole** player depending on the staff. The spy section's "green dog" also goes by **hug** or **add-on** rusher.

## Minor diagram notes

- Predict 3 (`fig-predict-spy`): the line to gain at 5 yards runs through the "5 yd" ruler label and through the W marker.
  Move the Will to d = 4.0 (still "over the back"). The ruler collision is cosmetic; skip the 5-yard ruler tick when
  `to_go == 5`.
- Predict 1 (`fig-predict-zero`): the M/W markers sit on the orange line. That is acceptable at third-and-2, but mugged
  linebackers are usually at 1–2 yards, so d ≈ 1.8 would read more like a mug. The caption says the nickel is "pressed on
  H", but he is about 3 yards off H (H at -1.5, $ at +1.5). Move him to d = 0.8 or change the caption to "tight on H".
- Fig 8 (spy): fine. Contain rush, B-gap escape and the spy's closing angle all read correctly, and the labels are clear of
  the edges.
- Fig 1, Fig 3 and Fig 5 (charts): clean, with no collisions. The Fig 5 end labels are legible.
- Frame strip (Fig 4): four panels tell the story in print, and the timing (0 / 0.8 / 1.7 / 3.3 s) is right for a draw
  (handoff at 0.9 s). Only the blocking issue above needs work.

## Film-room check (coach's view)

All the film rooms are well chosen and fairly characterised:
- Welker/Edelman option routes.
- James White as the third-down back.
- Flores's 2021 Cover 0 and the Nov 11, 2021 Ravens game.
- Spagnuolo's situational pressure.
- Chenal in 2024 and Sheppard's 2025 spy plan against Lamar.

The factcheck already confirmed the numbers. The only change I'd make is to the White box: add "pass protection" as the
first job, since that is why a third-down back plays (see item 11).
