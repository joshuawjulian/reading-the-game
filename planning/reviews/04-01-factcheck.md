# Fact-check log: 04-01 Passing Game Fundamentals

Checked 2026-10-06 against FACTS-current.md, web sources and recomputed nflverse data (in the `rtg`
container). All 5 `<!-- VERIFY -->` comments resolved and removed. Build
`build_pdfs.py 04-01-passing-fundamentals --html`: OK (21 pages; film room, footnotes and Go deeper
pages checked by eye).

| Claim | Verdict | Source | Change |
|---|---|---|---|
| Coryell coached San Diego State 1961–1972 and the Chargers 1978–1986 | VERIFIED (and completed) | PFHOF Coryell bio (SDSU 1961–72, Cardinals 1973–77, Chargers 1978–86) | Added the St. Louis Cardinals years to the text so the career is not misleadingly truncated |
| Route numbering "usually traced to" Coryell; three receivers' routes in a three-digit call | VERIFIED as attribution (no documented first use) | ESPN Dallas, Watkins, Jul 2, 2010 (Garrett: "three-digit system of digitizing the routes"); Air Coryell (Wikipedia); widely repeated in SI and coaching sites | Chapter's hedged wording kept; footnote now says the credit rests on coaching tradition, adds the ESPN source; VERIFY removed |
| Gillman coached the Chargers in the 1960s; principle "defend the entire field"; Coryell built on it | VERIFIED | PFHOF Gillman bio (Chargers HC/GM 1960–69); Air Coryell (Wikipedia) | Footnote describes the HOF bios (URLs checked, both live) |
| Chargers led NFL in passing yards 1978–1983 and 1985 | VERIFIED | Air Coryell (Wikipedia): "an NFL record six consecutive years from 1978 to 1983 and again in 1985" | none |
| Route tree 1 flat … 9 go; NFP article June 30, 2011 by Matt Bowen | VERIFIED | NFP article (fetched) | none |
| Patriots built option routes for Welker and Edelman | VERIFIED (source CORRECTED) | Farrar, SI, Jul 12, 2016 ("Edelman has replaced Wes Welker as the best option route runner in the NFL") | The cited Grantland piece (Brown, Jan 25, 2013) names Welker once but never mentions option routes or Edelman; SI added as the supporting source, Grantland kept only for the system |
| 3/5/7-step drops end about 5/7/9 yards; shotgun 1/3/5 equivalents | VERIFIED | Palazzolo, PFF, Jun 7, 2014 | New footnote `[^drops]` |
| Shotgun share of 2025 dropbacks (inline, ~82%); nflverse `shotgun` includes pistol | VERIFIED | Recomputed: 2025 FTN `qb_location == 'P'` → pbp `shotgun == 1` on 1,700 of 1,704 plays | none |
| Median 2025 time to throw ~2.5 s; 10–14 yd median 2.7, deep 3.0 (inline) | VERIFIED | Inline-computed; participation dictionary; FACTS-current §7 (NGS→FTN break, noted in `[^ttt]`) | none |
| Walsh a Bengals assistant (1968–75); Carter mobile, accurate, weak arm; led NFL in completion % in 1971 | VERIFIED | West Coast offense (Wikipedia); PFR 1971 leaders (Carter 62.2%, 138/222) | PFR source added to `[^walsh]`; VERIFY removed |
| Walsh 49ers HC from 1979, three Super Bowls (XVI, XIX, XXIII) | VERIFIED | Bill Walsh (Wikipedia) | none |
| FTN `read_thrown` codes: "1" = first read, "2" = later, "0" = no read (contradicting nflverse dictionary) | VERIFIED (against the data) | Dictionary text (fetched raw) says "0" = first read and that 2022 first reads are NA. Release files: "1" has 9,303 / 9,268 / 9,749 / 9,788 pass attempts in 2022–2025 (same in 2022, so not NA there); "0" is 2–3% of attempts, 52–74% throwaways, 3–8% completed, and from 2023 is the value on every run play (2022 runs are NA) | Footnote `[^ftn]` now gives this evidence; chapter's reading stands. The dictionary appears wrong; worth flagging upstream |
| Progression chart prose: >half to first read, quickest, most valuable; each later look ~0.5 s; checkdown ~0 EPA | VERIFIED | Recomputed 2022–2025: first 53.5%, 2.3 s, +0.28; later 2.9 s, +0.15; CHK 2.9 s, −0.04, 80% comp | none |
| Air yards / YAC definitions | VERIFIED | nflverse pbp dictionary | none |
| 2025 aDOT ~7.8, YAC ~47% of receiving yards (inline) | VERIFIED | Inline-computed | none |
| Behind-LOS throws: ~4 in 5 completed, ~9 YAC, negative EPA | VERIFIED | Recomputed 2021–25: 78.8%, 9.0 YAC, −0.18 | none |
| 5–9 yd throws completed ~2 in 3, highest success rate | VERIFIED | 67.7%, success 58.8% (highest) | none |
| 20+ yd throws: under half completed, highest INT rate, "worth about as much as a 15-yard throw" | CORRECTED | 20+ yds: 36% comp, 6.2% INT, EPA +0.36; 10–14 +0.33, 15–19 +0.43 | Now "about as much as a throw of 10–19 yards" |
| Steady 3–6 YAC for any throw past the line | VERIFIED | 0–4: 4.8 … 30+: 6.4 | none |
| Brady 2022 "the league's model of a rhythm passer"; Mahomes long tail (inline %s) | VERIFIED | Recomputed: Brady lowest mean time to throw of 29 passers with 300+ attempts (2.45 s); Mahomes 2.89 | Added the ranking to `[^bm]` |
| 2022 = Brady's last season, Mahomes's second MVP season | VERIFIED | common record (MVP 2018, 2022; Brady retired Feb 2023) | none |
| SB XXIII: Jan 22, 1989, Miami; Bengals led 16–13; "a little over three minutes left"; own 8; 92 yds, 11 plays; TD to Taylor with 34 s; 20–16; Walsh's last game | VERIFIED | Super Bowl XXIII (Wikipedia: 3:10 after kickoff, penalty to the 8) | Footnote rebuilt; the unchecked PFHOF "92-Yard Walk" citation replaced |
| Snap "about 40 seconds" left | CORRECTED (made exact) | FootballScoop (Walsh diagramming the play: "with 39 seconds remaining") | Now "with 39 seconds left" |
| Play call "20 Halfback Curl, X-Up," designed for Craig; "Craig and Jerry Rice were both covered" | CORRECTED | Inquirer, Jan 25, 2008 (designed for Craig; Taylor: Rice "was just to run motion to clear out the back side"); SI/press accounts: Craig jammed in traffic | Now: Rice in motion to clear out the other side, Craig jammed, Montana moved on to Taylor. Taylor's "three options" account kept in the footnote |
| SB LV: Feb 7, 2021, TB 31–9; both KC starting tackles out; Mahomes 497 yds traveled, most in NGS era (since 2016) | VERIFIED | NFL.com, Nick Shook (quote checked) | none |
| *Finding the Winning Edge* (Walsh, Billick, Peterson, 1997) as an account of the passing game | SOFTENED | Publisher listings; Pigskin Books (out of print, rare); the book is mainly about running a program | Description now "long manual on building and coaching a team, including his offensive philosophy and passing game (out of print and hard to find)" |
| *Blood, Sweat and Chalk* (Layden, 2010) covers "Coryell's numbers and Walsh's timing" | SOFTENED | CSMonitor review / publisher blurb (Air Coryell and West Coast among ~20 schemes) | Description generalized to the chapters it is known to have |
| Brown, *The Essential Smart Football* (2012), *The Art of Smart Football* (2015); Bowen a former NFL DB, later ESPN | VERIFIED | publisher listings; ESPN bio | none |
| Football-technical claims (route definitions, option-route rules, high-low/horizontal stretch, Cover 3 curl-flat to ~12 yds, smash vs Cover 2, flood/sail) | VERIFIED (standard teaching) | Bowen NFP 2011; consistent with 01-04, 06-06 and coaching literature | none |

Counts: VERIFIED 22 · CORRECTED 4 (20+ yd value comparison, snap time, SB XXIII play description, Patriots source) · SOFTENED 2 (two Go-deeper book descriptions) · REMOVED 0 (the unverified PFHOF "92-Yard Walk" citation was replaced, not the claim).

Still uncertain / for the editor:
- The nflverse FTN dictionary contradicts its own data on `read_thrown`; the chapter follows the data. If nflverse fixes the files (not the dictionary) the chart labels would need to change.
- "Seven-step drop rarer now than in the 1970s and 80s" is an uncontroversial characterization left unsourced.
