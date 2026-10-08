# Fact-check: 10-02 Third Down: The Money Down

Checked 2026-10-08 against FACTS-current.md, nflverse (every computed value re-run in the `rtg` container) and web sources.
All 4 `<!-- VERIFY -->` comments are resolved and removed. The chapter builds (`build_pdfs.py 10-02-third-down --html`: OK).

**Main correction (data bug):** the conversion flag was `third_down_converted | touchdown`, so a third-down
turnover returned for a touchdown by the *defense* counted as a conversion (e.g. Xavien Howard's 49-yard fumble-return
TD in 2021_10_BAL_MIA). The flag now requires `td_team == posteam` (`td_team` added to the columns). Effects: every
conversion rate drops by about 0.1–0.4 points; Baltimore's third downs vs Miami go from 3 of 14 to **2 of 14**, which matches
Eisenberg's "two of 14"; 2025 worst third-down offense changes from TEN to MIN; KC 2024 third-down-allowed rank 26 → 24.
All prose claims that depend on order (highest season 2020, "1–2 past" best group, the "at it" dip, run/pass level at 3rd & 3, blitz peak at 7–10) still hold.

| Claim | Verdict | Source | Change |
|---|---|---|---|
| Third-down conversion definition (counts any TD) | CORRECTED | nflverse `td_team`; game 2021_10_BAL_MIA play 24286 (Howard fumble-return TD) | Code fixed; fn `conv` now says "a touchdown by the offense; a turnover returned for a TD is a failure" |
| EPA swing ~3 points; third downs ~21% of runs/passes | VERIFIED | Recomputed (+1.77 / −1.26, swing 3.0; 20.6%) | None |
| League conversion 39–42% each season 2016–2025; highest 2020 | VERIFIED | Recomputed (38.6%–42.1%; 2020 max) | None |
| Runs beat dropbacks at 3rd & 1–2; level at 3rd & 3; dropbacks far better from 4 on; pass shares 91%/94% | VERIFIED | Recomputed (run 72.5/60.9/51.6 vs drop 58.8/54.9/49.9) | None |
| Bucket rates 60/44/31/15%; "the long kinds are the common kinds" (46% need 7+) | SOFTENED | Recomputed: 46% is under half | Now "the long kinds are common" |
| Past-the-sticks chart: 10+ short completed 77%, converted 9%; 1–2 past best (63%); dip at the line | VERIFIED (numbers) / SOFTENED (cause) | Recomputed; completion also falls to 52% "at it", so the defender explanation is plausible but not proven | Text: dip is "very likely, at least in part" the sticks-sitting defender, "with completions falling off too" |
| Short-of-sticks completions convert 80%/69% at 3rd & 1/2 vs 36%/11% at 7–10/11+; past-share 78/68/52/29% | VERIFIED | Recomputed | None |
| Man coverage 58%/58%/26% by bucket; dime 11/42/45% vs 8% early; blitz peaks 38% at 7–10, 17% at 11+ vs 25% early; Cover 0 9%→2%; rush-3 most common at 11+ | VERIFIED | Recomputed (FTN participation 2023–25) | None |
| 07-03 has a third-down blitz man/zone chart; 07-02 breaks down Spagnuolo's SB LVIII zeros; 08-03 installs third down on Thursday; 03-03 credits Paul Brown's Browns with the draw | VERIFIED | Cross-chapter grep (07-03 §"Third down: when to blitz…", 07-02 film room, 08-03 week figure, 03-03 l.1220) | None |
| Spagnuolo 2007 Giants "Four Aces" package of four pass rushers (SI, Vrentas 2016) | VERIFIED | SI, Dec 27 2016 (names no players) | VERIFY removed; text keeps no names; fn links 11-04, which has the 2007 ends |
| By 2011 the four-DE third-and-long package was "NASCAR" | VERIFIED | Bleacher Report 2012; Tuck quote via Jayski (Feb 7 2012); consistent with 11-04 factcheck | Tuck quote added to fn `nascar` |
| James White NE's most-targeted third-down receiver 2018 and 2019; 26% share | VERIFIED | Recomputed (2018: 30 vs 22; 2019: 41 vs 32) | None |
| Spagnuolo KC DC since 2019, still 2026 | VERIFIED | FACTS-current (2026 staffs) | None |
| KC 2024 blitz 32% early (league median 23%), 42% on 3rd (2nd); 2025 32%/37%; 2025 Cover 0 on 3rd 11.2%, most in NFL | VERIFIED | Recomputed | None |
| 2024 Chiefs 15–2; third-down rate allowed 43% (now 24th-best) | VERIFIED | PFR 2024 Chiefs; recomputed | Rank auto-updated by fix |
| Flores "fifteen seasons on Belichick's staff" | CORRECTED | Wikipedia: scouting 2004–07, coaching 2008–18 | Now "fifteen seasons in Belichick's New England organisation (four in scouting, then eleven on the coaching staff)"; fn `mia` updated |
| Flores Dolphins HC 2019–21; Vikings DC since 2023, still 2026 | VERIFIED | Wikipedia; FACTS-current | None |
| MIA 2020 Cover 0 16.8% level with NE 16.8% at top; 2021 28.5% most, >4x median (6.6%) | VERIFIED | Recomputed (NGS labels) | None |
| Thursday Nov 11 2021, 2–7 Dolphins beat 6–2 Ravens 22–10 in Miami | VERIFIED | PFR box score 202111110mia; BaltimoreRavens.com game page | VERIFY removed; sources added to fn `eisenberg` |
| Blitz on 52% of 48 dropbacks, Cover 0 on 17; Baltimore third downs | CORRECTED (via data fix) | Recomputed; Eisenberg: "two of 14" | Now 2 of 14 (was 3); fn notes agreement |
| Eisenberg quotes ("heavy diet of blitzes and a Cover Zero scheme"; "overwhelmed by relentless blitzes") | VERIFIED | BaltimoreRavens.com, Nov 12 2021 | None |
| 2023 Vikings heaviest blitzers; most rush-3 on 3rd & 7+ (30%) | VERIFIED | Recomputed (MIN 50% blitz, 1st) | None |
| 2025 rush-3 leaders LAC (18.8%) and DET (18.4%); Minter LAC DC 2024–25, Ravens HC 2026; Sheppard DET DC | VERIFIED | Recomputed; FACTS-current | None |
| Rush-3/4/5+ conversion 21/24/31% and sack rates on 3rd & 7+ | VERIFIED | Recomputed | None |
| Chiefs–Ravens, Sept 5 2024; KC 27–20, decided on final snap; Jackson 16–122 | VERIFIED | Recomputed; search results (Jackson 122 rush yds, 27–20) | None |
| Chenal "lined up on the defensive line 18 times", "pure spy role", rushing off the edge (Arrowhead Pride) | SOFTENED | Arrowhead Pride 403 (unreadable); A to Z Sports (Goldman, Sept 9 2024): five box spots, two DL spots, slot overhang, spied Jackson in key moments, pressures off the edge. No source found for "18" | "18" and AP wording removed; text now "moved all over the front … used him to spy Jackson in key moments"; fn rewritten on A to Z Sports, AP kept as a link only |
| Lions 38–30 at Ravens, MNF Sept 22 2025; Jackson sacked 7 times, 7 runs for 35 yds | VERIFIED | CBS Baltimore / NBC (38–30, 7 sacks); recomputed | None |
| Sheppard "publicly sceptical of spies" | VERIFIED (reworded) | SI (Maakaron, Sept 25 2025): he "had previously voiced displeasure with using a spy" | VERIFY removed; text "had earlier said publicly that he didn't like using a spy"; fn adds his reply quote |
| Sheppard quotes (folder built three years; "making everything look the same … who's the spy, who's in coverage") | VERIFIED | SI, Sept 25 2025 | None |
| Team faces ~200–230 third downs a season | VERIFIED | Recomputed 2021–25: IQR 206–227 (runs/passes) | None |
| Early-down success predicts next-year 3rd-down rate "about as well" as 3rd-down rate | CORRECTED (precision) | Recomputed: 0.33 vs 0.39 | "nearly as well" (text and takeaway) |
| Defensive carry-over r ≈ 0.2; 288 pairs; 2025 best/worst offense | VERIFIED | Recomputed (0.20; SF 50.7%, MIN 32.3%) | Values auto-update |
| Welker most-targeted 4 of 4 seasons 2009–12; 28% share; 48% vs league 39%; median throw at the sticks | VERIFIED | Recomputed | None |
| Edelman 2013/2016/2019 "his seasons as the lead option receiver" | CORRECTED (criterion) | Recomputed (he was not NE's top 3rd-down target in 2019); PFR: those are his three 16-game seasons | Now "the three seasons in which he played all 16 games"; PFR link in fn |
| Edelman missed 2017 with torn ACL; 2007–08 receiver names missing ~4 in 10 | VERIFIED | Wikipedia; recomputed (38%) | None |
| Chris B. Brown, *The Art of Smart Football* covers "option routes, the Patriots' passing game and constraint plays" | CORRECTED | Constraint theory is in *The Essential Smart Football* (2012); no TOC found confirming the other topics | Go-deeper now lists both books with general description |
| Ted Nguyen "at *The Athletic*" | SOFTENED | Current employer not verified for 2026 | Outlet dropped |
| Rules: ball spotted at forward progress; Cover 0/blitz definitions; NFL week install order | VERIFIED | NFL rulebook (forward progress, Rule 3/7); glossary and 08-03 | None |

Counts: VERIFIED 27, CORRECTED 7, SOFTENED 4, REMOVED 0 (the "18 snaps" figure was removed inside a SOFTENED row).

Uncertain: Arrowhead Pride article could not be read (403), so its exact wording is unconfirmed; it remains only as a link.
