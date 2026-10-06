# Fact-check: 01-06 How to Watch a Broadcast Like You Mean It

Checked 2026-10-06 against FACTS-current.md, nflverse data (recomputed in the `rtg` container with the chapter's own joins) and web sources.
Both `<!-- VERIFY -->` comments are resolved and removed. The chapter builds (`build_pdfs.py 01-06-how-to-watch-a-broadcast`: OK).

| Claim | Verdict | Source | Change |
|---|---|---|---|
| Skycam invented by Garrett Brown (Steadicam inventor) | VERIFIED | Sports Broadcasting HOF bio; Wikipedia "Skycam" | None |
| Skycam's first use: 1984 NFL preseason, 49ers at Chargers in San Diego, on CBS | VERIFIED | Wikipedia; contemporary *Inc.* (Jan 1985) account of the Aug 18, 1984 CBS telecast with Summerall's on-air intro | VERIFY removed; *Inc.* added to fn `skycam`; text says "August 1984". (Note: the SBHOF page wrongly dates the XFL to 1996.) |
| Skycam "gathered dust" because directors weren't sure what to do with it | SOFTENED | Wikipedia: slow progress due to computer/servo limits and cost (~$30k per event in 2001) | Reason changed to cost and the technology of the day |
| Became regular in NFL broadcasts after the XFL (2001) | VERIFIED | Wikipedia (XFL "X-Cam" 2001; ESPN NFL preseason 2001, SNF from 2002) | Footnote extended; "football" → "NFL" broadcasts |
| Yellow first-down line first aired Sept 27, 1998, ESPN, Bengals–Ravens; one network paid for it | VERIFIED | *Sports Illustrated*, Jul 18 2013 (ESPN held exclusivity through that season's playoffs) | None |
| Prime Vision launched with Amazon TNF in 2022; higher in-play camera; routes drawn | VERIFIED (camera wording CORRECTED) | *The Ringer*, Dec 14 2023 ("a wide angle is used, and every player is visible at all times"; route trees) | "switches to a higher camera" → "uses a higher, wider camera ... so every player stays in view" |
| Defensive Alerts added 2023, from pre-snap movement, marks likely rushers | VERIFIED | *Philadelphia Inquirer*, Sep 13 2023 | None |
| Later added coverage identification from tracking | VERIFIED | Amazon feature list; *Sportico* 2024 (man/zone in real time from live tracking data) | Sportico 2024 added to fn `alerts`; "(man or zone, called in real time)" added |
| NFL sold coaches film (All-22 + High End Zone) to fans via Game Rewind from 2012 | VERIFIED | Buffalo Bills / NFL.com, Jul 30 2012 | None |
| NFL+ Premium includes All-22 for every game back to 2022 (still true in 2026?) | CORRECTED (precision) | NFL.com 2024 NFL Pro launch article ("dating back to the 2022 season"); Disney+ explainer Dec 12 2025 and 2026 price guides list All-22 in Premium | VERIFY removed; text now says Premium still offers it for 2026, and the 2022 archive start is dated to the 2024 description; footnote adds the 2025 source and "packages change often" |
| NGS: RFID chips in shoulder pads, stadium receivers, 10 times a second | VERIFIED | operations.nfl.com NGS page (2–3 tags in shoulder pads; 20–30 UWB receivers; 10 Hz); ESPN (Seifert) Dec 11 2014 (17 stadiums in 2014) | None |
| Separation measured when the ball arrives; "three yards is open, one yard is tight" | CORRECTED | nflverse NGS dictionary (at catch or incompletion); own calc, 2025 REG qualifiers: mean 3.0 yd, range 1.9–4.6 | Now "typical regular receiver averages about three yards; a yard or less is tight"; new fn `sep` |
| Speed, completion probability, expected rushing yards descriptions | VERIFIED (general NGS definitions) | NGS / nflverse dictionaries | None |
| Median time to throw ≈ 2.5 s | VERIFIED | Own calc, 2025 participation `time_to_throw`, median 2.5 s (19,378 rows) | None |
| Third-and-4–6: 91% pass (1,652); third-and-1: 23% pass (853) | VERIFIED | Own calc: 90.6% / 1,652; 23.3% / 853 | None |
| Trailing by 1–8 in last two minutes of Q4: 87% pass (692 snaps) | CORRECTED | Own calc: 86.6% on 680 snaps in Q4; 692 included overtime | Footnote now "680 snaps; overtime excluded" |
| Third-and-1 under center 16% pass (525) | VERIFIED | Own calc: 16.4% / 525 | None |
| QB alignment pass rates: shotgun 78.5% (20,104), under center 31.1% (11,035), pistol 29.3% (1,618) | VERIFIED | Own calc, exact match | None |
| Rams under-center share 59% and UC pass rate 40%, both league highs; Washington 15% lowest | VERIFIED | Own calc: LA 59.1% / 40.1%; WAS 15.2% | None |
| Play-action on 82% of UC dropbacks, 10% of shotgun dropbacks | VERIFIED | Own calc: 81.7% / 9.6% | None |
| First-and-10 50% (12,809); 2nd-and-4–6 52% (2,623); 2nd-and-5–7 shotgun 76% (1,547) | VERIFIED | Own calc, exact match | None |
| Ladder: 32,813 snaps; always-pass ≈60%, D&D 62%, scorebug ≈68%, + alignment ≈75% | VERIFIED | Own calc: 60.1 / 62.4 / 67.8 / 75.1% | None |
| "Score and clock add more than the down does" | VERIFIED | Own calc: down+dist adds 2.2 pts over always-pass; score/clock add 5.5 more | None |
| Matthew Stafford 2025 MVP; McVay's Rams | VERIFIED | FACTS-current §2; NFL.com Honors list | None |
| Ball at opp 34 → field goal "about 52 yards" | CORRECTED | Standard conversion: LOS + 17 = 51 | Now "about 51 yards" with the arithmetic |
| "Most people start in the low 60s" | SOFTENED | No source for a population figure | Reworded as an expectation tied to what the scorebug alone is worth |
| Kirwan, *Take Your Eye Off the Ball* (2010; 2nd ed. 2015), former NFL coach and scout | VERIFIED | Wikipedia (Jets defensive assistant, Bucs/Cardinals scout); Triumph 2015 "2.0" edition | None |
| Jaworski/Cosell/Plaut, *The Games That Changed the Game* (2010), seven games | VERIFIED | Penguin Random House; Publishers Weekly | None |
| Chris B. Brown, *The Art of Smart Football* (2015) | VERIFIED | Publisher listing | None |
| Football-technical: stances, heavy hand tell, shotgun ~5 yd, pistol QB ~4 yd with back 6–7 yd, split/safety-depth tells, coaches film = sideline + end zone | VERIFIED (standard coaching usage; consistent with Kirwan and earlier chapters) | Kirwan 2010; Bills/NFL.com 2012 | None |

Counts: VERIFIED 23, CORRECTED 5 (camera wording, NFL+ precision, separation, late-game snap count, FG distance), SOFTENED 2, REMOVED 0.
