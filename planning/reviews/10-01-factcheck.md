# Fact-check: 10-01 Early Downs and Field Zones

Checked 2026-10-08 against FACTS-current.md, nflverse play-by-play (queried in the rtg container), and the sources linked below. All 5 `<!-- VERIFY -->` markers were resolved and deleted. The chapter rebuilds cleanly (`build_pdfs.py 10-01-early-downs-and-field-zones --html`: OK).

**Totals:** 30 VERIFIED · 5 CORRECTED · 1 SOFTENED · 0 REMOVED

| Claim | Verdict | Source | Change |
|---|---|---|---|
| About three snaps in four are first or second downs | VERIFIED | nflverse 2025: 1st 43.5%, 2nd 33.1% of scrimmage plays | none |
| Neutral 1st-and-10 pass rate 44–48% 1999–2025; dropbacks out-earn runs every year (27 seasons) | VERIFIED | Chapter computation (asserts), nflverse | none |
| Romer, JPE 114(2) 2006: 340–365; 1998–2000 seasons; conservatism; asymmetric weighting of failed vs. successful gambles | VERIFIED | Romer PDF (text extracted: "1998, 1999, and 2000 seasons"; "value decreases in the chances of winning from failed gambles and increases from successful gambles asymmetrically") | none |
| "Twenty years ago" (2006) | VERIFIED | Date arithmetic | none |
| Yardage success rate 40%/60% | VERIFIED | Standard definition (13-02) | none |
| Play-action does not need a successful run game | VERIFIED | Cross-reference to 04-05 (fact-checked there) | none |
| Winning correlates with total runs, not first-half early-down run rate | VERIFIED | Chapter computation (asserts) | none |
| 2018 Chiefs 12–4, led NFL with 565 points; Mahomes's first season as starter | VERIFIED | PFR 2018 standings; nflverse schedules | none |
| 2018 Rams 13–3, 527 points (2nd); McVay's second season | VERIFIED | PFR; McVay hired Jan 2017 | none |
| Rams 54, Chiefs 51, Mon Nov 19 2018, LA Coliseum | VERIFIED | NFL.com game recap; nflverse `2018_11_KC_LA` | none |
| Moved from Mexico City on Nov 13 (six days before kickoff) because of the Azteca field condition | VERIFIED | NFL.com announcement (Nov 13 2018); CBS Sports; AP | footnote now cites NFL.com + CBS instead of Wikipedia; VERIFY removed; reason stated precisely (re-sodded surface failed NFL playability standards) |
| Mahomes 478 yds, 6 TD, 3 INT; Goff 413 yds, 4 TD | VERIFIED | nflverse play-by-play (passing yards 478 / 413) | none |
| Three defensive TDs: Ebukam fumble return + INT return, Allen Bailey fumble return | VERIFIED | nflverse play-by-play (writer); NFL.com recap | none |
| Both offenses threw on about seven of ten first downs that night | VERIFIED | nflverse `pass` flag incl. scrambles/sacks/penalty plays: KC 70%, LA 71% | none |
| Ravens 2019 14–2, led NFL with 531 points | VERIFIED | PFR; nflverse | none |
| Ravens 3,296 rushing yards broke 1978 Patriots' 3,165 (most in NFL history) | VERIFIED | NFL.com "Ravens break single-season team rushing record" (Dec 2019); NBC Sports Boston; nflverse 2020–2025 shows no team above it since (max 3,184, BAL 2024). Note: the 1948 AAFC 49ers ran for more, so "NFL history" is the right qualifier | footnote cites NFL.com; notes record still stands after 2025; nflverse 3,287 discrepancy explained; VERIFY removed |
| Jackson 1,206 rushing yards broke Vick's QB record 1,039 (2006) | VERIFIED | CBS Sports MVP story; Wikipedia 2019 Ravens season | none |
| Jackson second unanimous MVP after Brady (2010) | VERIFIED | CBS Sports; Ravens.com ("all 50 first-place votes") | footnote cites CBS instead of Wikipedia; 50 votes added |
| Divisional round Jan 11 2020, Titans 28–12 | VERIFIED | nflverse schedules | none |
| Ravens threw on about three of four early downs in that game (77%) | VERIFIED | nflverse `pass` flag, early downs: 77.1% (70 snaps) | none |
| Lions 2023 12–5, lost NFC Championship 34–31 at SF (Jan 28 2024) | VERIFIED | PFR; nflverse schedules | none |
| Lions 2024 15–2, NFC No. 1 seed, led NFL with 564 points; lost divisional round to WAS 45–31 (Jan 18 2025) | VERIFIED | PFR; nflverse schedules | none |
| Ben Johnson DET OC 2022–2024, Bears HC 2025 | VERIFIED | FACTS-current §staffs | none |
| Emara et al. 2017, JBEE 69: 125–132 | CORRECTED | Haverford scholarship repository; IDEAS/RePEc (MPRA 67862) | first author's name corrected from "Nadeem" to **Noha** Emara; URL added; sample (2000–2012) added |
| Emara et al. finding: callers alternate more than an unpredictable caller would, "and defenses gain from it" | CORRECTED | Abstract: negative serial correlation "negatively affects play efficacy" | now "the habit makes plays less effective" (the paper measures play efficacy, not defensive gains directly) |
| Zone names (backed up, coming out, open field, fringe, plus/minus) are call-sheet usage, not rulebook terms; boundaries vary | SOFTENED | Coach and Coordinator clinic (backed up, minus yard lines); SI 2017 indoor play-calling ("coming off"); Wikipedia "Dead zone" (four-down territory / no man's land, kicker-range dependent) | no single published call sheet uses every name; footnote now cites these sources and notes the "coming off" variant; VERIFY removed |
| Holding / sack in own end zone is a safety | VERIFIED | NFL Rule 11-5 (safety) | none |
| Punt into end zone is a touchback at the 20 | VERIFIED | NFL rulebook | none |
| Since 2025, a kickoff landing in the end zone comes out to the 35 (unchanged for 2026) | VERIFIED | FACTS-current §3; NFL.com (already cited) | none |
| "So most drives now start in the open field" | CORRECTED | nflverse: first scrimmage snap of each drive at own 25+: 66% in 2025, 70% in 2024 | the "now" implied the 2025 rule caused it; it was already true in 2024. Text now says "about two drives in three now start at the offense's own 25 or better" with a new footnote `[^starts]` |
| 3rd-and-3 at opp 38 → 56-yard FG; plus 33 → 51, after a 7-yard sack → 58 | VERIFIED | LOS + 17/18 arithmetic | none |
| 4th-down go rates (2025), third-down pass-rate switch at midfield, Lions 4th-down attempts | VERIFIED | Chapter computation (asserts) | none |
| Shotgun from own 3: QB about 3 yards deep in the end zone | VERIFIED | Shotgun depth 5–7 yards | none |
| Pat Kirwan, *Take Your Eye Off the Ball* "(2nd ed., 2015)", "a former NFL coach" | CORRECTED | Triumph Books listing (ISBN 9781629371696, Oct 2015, with David Seigerman); Wikipedia (Jets defensive assistant, Bucs/Cardinals scout, Jets director of player administration) | now *Take Your Eye Off the Ball 2.0* with Seigerman; described as former NFL assistant coach, scout and front-office executive |
| Brian Burke essays (no specific title) | CORRECTED | Burke, "Game Theory and Run/Pass Balance," Advanced NFL Stats, June 2008 (archive URL; cited by Cornell INFO 2040 blog) | Go-deeper item now names the essay with URL; `[^establish]` reference adjusted to "the Brian Burke essay"; VERIFY removed |
| QB sneak the best short-yardage play | VERIFIED | Widely supported (10-03; nflverse sneak conversion rates) | none |

Uncertain / notes:
- The Burke archive page could not be fetched directly (only cited via secondary sources); the URL pattern is the standard archive.advancedfootballanalytics.com one.
- Pro-Football-Reference returned 403 to the fetcher; team records and points were cross-checked against nflverse schedules and news reports instead.
