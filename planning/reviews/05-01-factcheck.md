# Fact-check: 05-01 Defensive Line Play: Techniques, One-Gap and Two-Gap

Checked 2026-10-06 against FACTS-current.md, the nflverse combine file (re-read in the `rtg` container) and web sources.
Pro Football Reference returns HTTP 403 to automated fetches, so the PFR spot-checks were done against Wikipedia,
team sites and the Hall of Fame instead. All 8 `<!-- VERIFY -->` comments are resolved and removed. The chapter builds
(`build_pdfs.py 05-01-dl-techniques-and-gap-control`: OK, 20 pages). Footnotes: 17 definitions, each referenced once.

| Claim | Verdict | Source | Change |
|---|---|---|---|
| Combine sizes: Wilfork 6-1/323, Donald 6-1/285, J.J. Watt 6-5/290, T.J. Watt 6-4/252, Babin 6-3/260, J. Davis 6-6/341, D. Lawrence 6-4/342; combine file covers 2000 onward | VERIFIED | nflverse `load_combine()` re-read in container (min season 2000) | None |
| "the Giants' Dexter Lawrence" (present tense) | CORRECTED | NBC Connecticut, Apr 19 2026 (traded to CIN for the No. 10 pick) | Now "a Giant until an April 2026 trade sent him to Cincinnati"; source added to fn `combine` |
| Jordan Davis is an Eagle | VERIFIED | CBS Philadelphia / NFP (fifth-year option, 2026 extension) | None |
| Sapp and Donald "listed between 285 and 300" | CORRECTED | Wikipedia: Sapp 6-2, 303 (PFR 300); Donald 6-1, 280 | Now "roughly 280 to 300 pounds"; new fn `dtsize` |
| J.J. Watt led NFL in sacks 2012 (20.5) and 2015 (17.5); DPOY 2012, 2014, 2015 | VERIFIED | Wikipedia "J. J. Watt" (PFR blocked) | Second source added to fn `jjwatt` |
| Watt played the 5 (left end) in Phillips's 3-4 | VERIFIED | Texans 2011 DL preview: "starting left end, a five-technique between the right tackle and tight end" | Quote added to fn `jjwatt` |
| Washburn: Titans DL 1999–2010, Eagles 2011–2012; both quotes | VERIFIED | Wikipedia; philadelphiaeagles.com Feb 9 2011 (both quotes verbatim) | None |
| Washburn "a Southern line coach" | REMOVED | No source for the characterization | Dropped "Southern" |
| 2011 Eagles tied for league lead with 50 sacks; Babin 18, third in NFL | VERIFIED | philadelphiaeagles.com, Jan 17 2012 | None |
| Babin played for Washburn in Tennessee (2010) | VERIFIED | Philadelphia Inquirer, Dec 17 2011 | None |
| Schwartz: TEN DC 2001–08, PHI DC 2016–20 (SB LII), CLE DC 2023–25, resigned Feb 2026 | VERIFIED | Wikipedia "Jim Schwartz" (resigned Feb 6 2026) | None |
| Schwartz's Cleveland front was a wide-9 | SOFTENED | ClevelandBrowns.com, Jan 18 2023 (describes the "Wide 9" technique for Garrett) | Added that it was billed as wide-9 but alignment varied with down, distance and personnel; source added to fn `schwartz` |
| Garrett DPOY 2023 and 2025; 23.0 sacks record in 2025 | VERIFIED | FACTS-current §2; NFL.com | None |
| Greene 1974 "stunt 4-3": tilted at 45°, Perles or Greene's idea, Carson/Noll approval, "first used in the playoffs" | SOFTENED / CORRECTED | Steelers.com (Labriola, Nov 26 2014): over the center at a 45° stance, a practice-field experiment, used 23 of 60 snaps vs NE in late Nov; Simpson 49 yd in the 32–14 playoff win. PFHOF credits Greene; Wikipedia "George Perles" credits Perles | Origin now presented as disputed (PFHOF: Greene; others: Perles); "first used in playoffs" corrected to first heavy use vs NE in late November; unsourced Carson/Noll approval detail removed; fn `greene` rewritten |
| Sapp: Bucs 1995–2003, DPOY 1999, 96.5 sacks, HOF 2013 | VERIFIED | PFHOF; Wikipedia | None |
| Dungy HC 1996–2001; Kiffin DC 1996–2008 | VERIFIED | Buccaneers Ring of Honor (Kiffin) | Source added to fn `sb37`; film room now says Kiffin still ran the defense in Gruden's first season (Dungy was gone by SB XXXVII) |
| SB XXXVII: Jan 26 2003, TB 48–21 OAK, five Gannon INTs, Gannon league MVP | VERIFIED | Wikipedia (Super Bowl-record five INTs, three returned for TDs); KCBD/AP | Added "Super Bowl-record" and "three returned for touchdowns" |
| Wilfork: No. 21 pick 2004, NE 2004–14, HOU 2015–16, five Pro Bowls, 1st-team All-Pro 2012, SB XXXIX and XLIX | VERIFIED | Wikipedia; Patriots.com | Fn clarifies Pro Bowl years are seasons (2007, 2009–12) |
| Wilfork's role as a 2004 rookie | CORRECTED (precision) | Wikipedia (shared nose with Keith Traylor, started SB XXXIX); Patriots.com May 3 2005 (Traylor released) | Text now says he shared the job with Traylor as a rookie and it was his alone from 2005 |
| Patriots 2004–2010 a two-gap 3-4 | VERIFIED | Chris B. Brown, Grantland, Feb 6 2012 ("two-gapping war daddy"; Belichick "traditionally a 3-4 coach") | Source added to fn `wilfork` |
| Wilfork moved between nose and end in 2010–11; NE to a 4-3 in 2011 | VERIFIED | Wikipedia (moved to DE from Week 4 of 2010; 4-3 in 2011) | Wording tightened |
| Phillips's Texans preview: linemen "shoot into a single gap," linebackers take the read gap | CORRECTED | Texans.com Sep 7 2011: neither phrase appears; it says "his one-gap scheme" and Kollar's "not like a two-gap type defense where you need that 350-pound nose man..." | Fabricated quote replaced with the real quotes; fn `phillips34` rewritten |
| Phillips (son of Bum) ran a one-gap 3-4 for decades | VERIFIED (general) | Texans.com 2011; widely documented | None |
| PFF: 0-technique controls center, draws double team; two-gap noses "north of 330" | VERIFIED | PFF, Sam Monson, Jun 3 2015 | None |
| Slant mechanics: 45° first step with back foot, a flat slant gets pushed along | VERIFIED | Viqtory Sports | None |
| Friends University clinic quote on slants | VERIFIED | Gridiron Strategies (Welch and Shaw), verbatim | None |
| SB LVI: Feb 13 2022, SoFi, 23–20; Kupp TD left 1:25; Donald and Gaines stop Perine on 3rd-and-1; Donald wraps Burrow on 4th-and-1 | VERIFIED | Wikipedia "Super Bowl LVI" | None |
| Reggie White: PHI 1985–92, GB 1993–98, CAR 2000; 198 sacks, record at retirement, passed by Bruce Smith; HOF 2006 | VERIFIED | Wikipedia; PFHOF | Fn wording made explicit |
| White's 3 sacks in SB XXXI "a record at the time" | CORRECTED (precision) | Guinness World Records: 3 is still the record, shared with Dockett (XLIII), Ealy (50), Jarrett (LI); SB LX had no 3-sack player (Murphy 2) | Now "a Super Bowl record that has since been tied but never broken"; source in fn `white` |
| SB XXXI: Jan 26 1997, GB 35–21 NE | VERIFIED | Wikipedia | None |
| BDB 2025 = 2022 season weeks 1–9; plays.csv has `isDropback`; players.csv has `position` | VERIFIED | GitHub BDB-2025 code (several repos read `isDropback`); unravelsports BDB loader reads `position` from players.csv | None |
| eval:false cell reads `position` from the tracking frames | CORRECTED (code) | BDB 2025 tracking files carry no position column | Cell now merges `position` from players.csv into tracking before `bdb.prepare(..., label="position")`; prose says position comes from the players file |
| 2011 Eagles run-defense figure (optional VERIFY) | REMOVED | Not added; no figure was in the text | Comment deleted |

**Counts:** VERIFIED 24 · CORRECTED 8 · SOFTENED 2 (Schwartz wide-9; Greene stunt 4-3 origin, also partly corrected) · REMOVED 2.
