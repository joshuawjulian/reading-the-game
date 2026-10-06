# Fact-check: 04-04 Dropback Concepts

Checked 2026-10-06 against FACTS-current.md, nflverse (recomputed independently in the `rtg` container, script `_pdfbuild/0404-fc/chk.py`) and web sources.
All 9 `<!-- VERIFY -->` comments are resolved and removed. The chapter builds (`build_pdfs.py 04-04-dropback-concepts --html`: OK; 32 pages).
Each footnote is still referenced exactly once (14 footnotes; `fourverts`, `mesh` and `yankee` are new).

| Claim | Verdict | Source | Change |
|---|---|---|---|
| 2025 median time to throw: 2.3 s (0–9 air yds), 2.8 s (10–19), 3.1 s (20+); 2.2 s behind LOS | VERIFIED | Own recalculation (pbp + participation `time_to_throw`, 99.7% coverage) | None |
| EPA/att +0.10 vs +0.39 (and +0.44 deep); completion 72% vs 54% (37%); INT 1.6% vs 3.2% (5.0%) | VERIFIED (numbers) / CORRECTED (wording) | Own recalculation | Text said "less than ten yards", but the numbers are the 0–9 band (including throws behind the line gives +0.02 EPA, 73%, 1.4%). Now "zero to nine yards" |
| Heatmap: 53,346 attempts 2023–25; 10–14 middle +0.52 (n 2,023), 15–19 middle +0.60 (n 1,167); outside +0.26 and +0.39–0.40 | VERIFIED | Own recalculation | None |
| Caption: intermediate middle "the most valuable area on the field per attempt" | SOFTENED | Own recalculation: 30+ middle +0.58 and 20–29 middle +0.51 are about as high as 10–14 middle (+0.52) | Now "is, with the deep middle, the most valuable area" |
| Levels: inside receiver runs the short in, outside receiver the dig | CORRECTED | Chris B. Brown, "One-Trick Pony," Grantland, Jan 25 2013 (Colts "Dig"/"Levels": inside receiver square-in/dig, outside receiver five-yard in); footballnationusa "levels concept" (#1 runs 5-yd "fin", #2 the dig) | Text now gives the common version (outside short in, inside dig); levels plate redrawn (H dig at 12, X in at ~4), caption, labels and progression numbers moved; checked rendered |
| Peyton Manning's Colts made levels a signature call | VERIFIED (made specific) | Brown, "One-Trick Pony" (called "Dig" in Indy; "ten times a game in various forms") | Text adds the Colts' name for it and Brown's count; footnote `colts` rewritten with the real essay and URL |
| Four verticals lineage (BYU, Coryell, run-and-shoot; Air Raid core call) | SOFTENED | Wikipedia "Air Coryell" (built on Gillman), "Run and shoot offense"; Sherman, The Ringer, Aug 14 2018 (four verts the Air Raid's "signature play") | Now "has no single inventor; its roots are usually traced to Gillman and Coryell, Edwards's BYU and Mouse Davis"; "at least to the 1970s and 1980s" dropped; new fn `fourverts` |
| Chiefs' four-verticals variants with a Kelce seam that bends or holds by safety look | REMOVED (specific) | No accessible source tying a Kelce seam-read to the Chiefs (Arrowhead Pride film reviews 403) | Seam-read now described generically (sourced to Brown's Colts "Read-Seam"); Chiefs kept only as an example of speed outside (Hill). KC film room "Watch Kelce's seam bend" now "Watch the seam routes for a conversion" |
| Yankee: post + deep over off play-action; signature Rams/McVay shot; Shanahan-tree usage | VERIFIED (detail added) | Nick Wagoner, ESPN, Oct 19 2018 (Rams from 11 personnel with jet motion, 49ers from 12) | Adds the Rams' 11-personnel/jet version and the 49ers; new fn `yankee`; "almost always" play-action now "usually"; Rams film room "yankee chief among them" now "yankee among them" |
| Mumme "a high school and small college coach" | CORRECTED | Wikipedia "Hal Mumme" (UTEP OC 1982–85) | Now "a former high school coach and college assistant" |
| Leach "a former law student" who never played college football | CORRECTED (precision) | Leach earned a JD from Pepperdine; played rugby, not football, at BYU (Saturday Down South profile; Wikipedia) | Now "a law-school graduate" |
| Iowa Wesleyan c. 1989, Valdosta State, Kentucky 1997; Couch #1 pick 1999 | VERIFIED | Wikipedia "Hal Mumme" (IWU 1989–91, VSU 1992–96, UK 1997–2000); PFR 1999 draft | Footnote dates made explicit |
| Leach HC stops: Texas Tech 2000–09, Washington State 2012–19, Mississippi State 2020–22 | VERIFIED | Wikipedia "Air raid offense" | None |
| Mesh came to the Air Raid from BYU | VERIFIED | Leach quoted by The Scouting Academy ("which BYU under LaVell Edwards ran for two decades") | Text quotes it; new fn `mesh` |
| Mesh Air Raid progression: corner, crossers, back | VERIFIED | Erick Streelman, Win With The Pass, 2017 ("The Progression is Corner, Mesh, Swing") | Cited in fn `mesh` |
| Air Raid "lived on a dozen" plays | SOFTENED | Gwynne (small menu); no exact count | "a dozen or so" |
| Mesh "in every NFL playbook"; concepts "in every NFL playbook" | SOFTENED | Generalization | "nearly every" / "almost every" |
| OPI: from snap until ball touched; downfield blocking = OPI; contact within one yard of LOS isn't PI; 10 yards from previous spot, no loss of down | VERIFIED (wording tightened) | NFL Rule 8, Section 5 (as checked in 02-04 fact-check); Wikipedia "Pass interference" (NFL OPI 10 yards from previous spot) | "contact within a yard … is allowed" now "isn't pass interference" (text and rub/pick figure caption: it can still be holding); footnote rewritten to quote the rule |
| Erhardt and Perkins together on Fairbanks's Patriots staff in the 1970s | VERIFIED | Wikipedia "Ray Perkins" (NE WR coach 1974–77), "Ron Erhardt" (NE 1973–81); Brown, "Speak My Language," Grantland | Footnote gives the 1974–77 overlap and the 1982 move to the Giants; cites Brown's essay |
| McDaniels NE OC "for most of Brady's tenure (2006–2008 and 2012–2021)" | CORRECTED (precision) | Wikipedia "Josh McDaniels"; FACTS-current (NE OC 2025–26) | Footnote now "2006–08 and 2012–21, covering 11 of Brady's 20 seasons, and returned in 2025" |
| Harrell 5,705 yds (2007); Crabtree 134-1,962-22 (2007); Biletnikoff 2007 and 2008 | VERIFIED | Wikipedia "Michael Crabtree", "Graham Harrell" | "freshman" now "redshirt freshman"; footnote cites them |
| Kingsbury played QB for Leach at Texas Tech 1999–2002 | CORRECTED | Wikipedia "Kliff Kingsbury" (redshirt 1998, played 1999–2002; Dykes coached him in 1999, Leach from 2000) | Footnote: Tech QB 1999–2002, last three seasons under Leach |
| PFR coach slug KingKl0; Cardinals HC 2019–22 | VERIFIED | PFR (KingKl0 coach pages indexed); Wikipedia | None |
| Rams 2018: McVay's 2nd season, 13–3, lost SB LIII 13–3 to NE; Goff 4,688 yds, 32 TD | VERIFIED | PFR; own recalculation (4,688 / 32) | None |
| Rams 2018 deep throws: 11.3% (18th), +0.77 EPA (3rd); league 12.0%, +0.37 | VERIFIED | Own recalculation | None |
| Chiefs 2018: Mahomes 5,097 yds, 50 TD, MVP; KC 15.1% deep (5th), +0.75 EPA (4th) | VERIFIED | Own recalculation; PFR | None |
| Connections: curl-flat, triangle and timed dropback game "were born" with Walsh's 49ers | SOFTENED | Walsh developed the system in Cincinnati before San Francisco | Now "the offense that made [them] famous" |
| BDB 2025 = 2022 season weeks 1–9, routes charted, Kaggle login | VERIFIED | FACTS-current; 02-04 fact-check | None |
| Books: Brown 2012/2015; Gwynne, Scribner 2016; Walsh/Billick/Peterson 1998 | VERIFIED | Publisher listings | None |
| Football-technical (Cover 2/3/Quarters rules, smash/flood/dagger/scissors/post-wheel reads, angle route, tags, conversions) | VERIFIED (general) | Consistent with Brown's essays and the coverage chapters | None |

Uncertain / notes
- "Speak My Language" (Grantland) is cited without a date: the fetched page gave the same date as "One-Trick Pony", which looked unreliable.
- The Chiefs' 2018 four-verticals usage is plausible (Arrowhead Pride film reviews mention it per search snippets), but the pages returned 403, so the specific Kelce claim was removed rather than sourced.
- The levels plate was edited (route swap); the drive, shallow-cross and other plates were not changed.
