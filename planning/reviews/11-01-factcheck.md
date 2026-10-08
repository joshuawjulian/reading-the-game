# Fact-check log: 11-01 From the Single Wing to the 1970s Scoring Drought (1906-1977)

Checked 2026-10-08 against FACTS-current.md, web sources, and a recomputation of the points chart from the cached FiveThirtyEight file (`data/cache/fivethirtyeight_nfl_games.csv`). All 13 `<!-- VERIFY -->` comments are resolved and removed. Two footnotes were added (`[^rosters]`, `[^hirsch]`), and every footnote is still referenced exactly once (31 footnotes). Build `build_pdfs.py 11-01-single-wing-to-scoring-drought`: OK. I re-rasterized the timeline page after editing the 1969 row, and it is clean.

**Totals (table rows; several rows bundle many claims):** 55 VERIFIED, 8 CORRECTED, 5 SOFTENED, 0 REMOVED.

| Claim | Verdict | Source | Change |
|---|---|---|---|
| 1905: 19 deaths; Roosevelt pressed for reform, not a ban | VERIFIED | Wikipedia, History of American football | none |
| Forward pass legalized at the rules committee meeting of April 6, 1906 | VERIFIED | Wikipedia, Forward pass ("final meeting ... on April 6, 1906") | none |
| First legal pass: Robinson (SLU) vs Cobb (Bates) | SOFTENED | Wikipedia, Forward pass now calls the Robinson claim "debunked" and credits Cobb, Sept 22, 1906 | Footnote reworded; the text never names a first passer |
| Early rules: incompletion = turnover in 1906, then a 15-yard penalty from 1907; pass must cross the line 5 yards from center; a pass caught in the end zone = touchback; some versions limited the pass's length | VERIFIED (dates SOFTENED) | Smithsonian; Pigskin Dispatch (Timothy P. Brown) | The text already avoids dating each rule; the footnote now explains why (the 20-yard limit appears in 1906 accounts and again in 1910) |
| 1912: 10-yard end zone, fourth down, 6-point TD, length limit dropped | VERIFIED | Wikipedia, History of American football; Pigskin Dispatch ("changed it from 20 yards to ANY distance") | Sources added to `[^early]` |
| 1913 Notre Dame 35-13 at Army; Dorais and Rockne at Cedar Point | VERIFIED | Wikipedia, Forward pass; 1913 Notre Dame team | none |
| NFL founded 1920 and named in 1922 (timeline) | VERIFIED | Common record | none |
| 1932 indoor playoff and Nagurski's disputed pass; 1933 pass legal from anywhere behind the line, hashes, posts on the goal line | VERIFIED | Wikipedia, 1932 NFL Playoff Game; 1933 NFL season | none |
| "From 1934, an incomplete pass no longer drew a five-yard penalty" | CORRECTED | Wikipedia, Modern history of American football: the 1934 change removed the 5-yard loss for a **second** incompletion in a series of downs | Now "a second incomplete pass in the same set of downs no longer cost five yards"; source added |
| Slimmer ball through the 1920s and '30s | VERIFIED | Wikipedia, Forward pass | none |
| Scoring 8.2 (1932), 23.2 (1948), 19.3 (1970), 18.2 (1974), 20.6 (1975), 19.2 (1976), 17.2 (1977); 17.2 the lowest since 1942 (15.9); 1950s-60s around 21-22 | VERIFIED | Recomputed from the cached CSV with the csv module, independently of pandas: it matches the FALLBACK table exactly, game counts are right (for example 78 NFL games in 1960), and the 1943-76 minimum is 18.0 (1944). Wikipedia, 1977 NFL season | none |
| "In each of its first five seasons AFL teams outscored NFL teams, by between one and three points a game" | CORRECTED | Same recomputation: +2.6 (1960), +2.95 (1961), **+0.8 (1962)**, +1.2 (1963), +1.2 (1964) | Now "by close to three points a game in 1960 and 1961, and by about one point a game in 1962-64" |
| No 1,000-yard receiver in 1977 | VERIFIED | Wikipedia, 1977 NFL season | none |
| Single wing: Warner, Carlisle formation, around 1907; Thorpe at Carlisle; unbalanced line 4 and 2; blocking back called the quarterback; spinner; the name from the wing's shape | VERIFIED | Wikipedia, Single-wing formation; PFHOF, Jim Thorpe | none |
| Ralph Jones (Bears HC 1930-32) credited with the man in motion and wider spacing | VERIFIED | Wikipedia, Ralph Jones ("spaced out the offensive line"; "wide ends and a halfback in motion") | Quote added to `[^tform40]`; the "accounts differ" caveat kept |
| Stanford 1-7-1 in 1939, unbeaten in 1940 with a Rose Bowl win; Luckman a Columbia single-wing tailback | VERIFIED | Wikipedia, 1940 Stanford; PFHOF, Luckman | none |
| 1940 title game: Dec 8, 7-3 loss three weeks earlier, Marshall's "crybabies and quitters", Osmanski's 68 yards on the second play, 11 TDs by 10 players, 8 INTs, Shaughnessy's counters to the linebacker shifts, Baugh's "73-7", the most lopsided result in NFL history | VERIFIED | Wikipedia, 1940 NFL Championship Game | none |
| Steelers the last single-wing team, gave it up after 1952 | VERIFIED | Wikipedia, 1952 Pittsburgh Steelers season | none |
| Shaughnessy's 1949 Rams flanked Elroy Hirsch as a permanent receiver | VERIFIED | Britannica, Elroy Hirsch; Yahoo Sports (flankers predate him) | New footnote `[^hirsch]` |
| Free substitution in college 1941 and the NFL 1943; Crisler's Michigan vs Army in 1945; NFL unlimited substitution permanent in 1950; colleges limited it in 1953 and restored it by the mid-1960s | VERIFIED | Wikipedia, Two-platoon system; PFHOF chronology 1940-59 | The footnote now spells out the NFL's 1946 three-man limit, the 1949 one-year return and the Jan 20, 1950 restoration, replacing "sources disagree" |
| "NFL rosters were 22 to 33 players through the 1930s and '40s" | CORRECTED | Hogs Haven roster history (about 20 in 1930-32; 24-25 in the mid-1930s; 30 in 1938-39; 28 in 1943-44; 33 in 1945-46; 35 then 34 in 1947); PFRA forum (22 in 1933-34) | Now "from about 20 players in the early 1930s to the low and mid-30s in the '40s"; new footnote `[^rosters]` |
| Paul Brown: Massillon; OSU's 1942 title; four AAFC titles; 35-10 in the first NFL game; titles in 1950, 1954 and 1955; Graham's 10 seasons and 10 title games | VERIFIED | Wikipedia, Paul Brown; PFHOF | none |
| Brown: full-time staff, playbook tests, intelligence tests, first to scout with film | VERIFIED | Wikipedia, Paul Brown | none |
| The 40-yard dash adopted at Ohio State in 1941 because a punt cover is about 40 yards | SOFTENED | Wikipedia (punt rationale, OSU 1941); Bengals.com, Mike Brown: "the longest anyone had to run ... I'm not so sure about the punt part" | "by the usual account", plus Mike Brown's version; source added |
| Draw play from a 1946 accident (Graham to Motley) | VERIFIED | Wikipedia, Paul Brown (from Brown's autobiography) | none |
| Motley and Willis signed in 1946 | VERIFIED | Wikipedia, Paul Brown | none |
| Messenger guards; Noll one of them, 1953-59 | VERIFIED | Wikipedia, Chuck Noll | none |
| 1956 radio helmet spotted by the Lions in a preseason game, banned by Bell after a few games; helmet radios legal in 1994 | VERIFIED | PFHOF, "Ratterman's radio helmet" (a Lions assistant spotted the transmitter; banned after three more games; 1994) | none |
| Sept 16, 1950: 35-10, Graham 346 yards and 3 TDs; Neale's basketball jab; the Eagle defense won the 1948 and 1949 titles | VERIFIED | Browns.com "Top moments No. 25"; Wikipedia | none |
| Dec 3, 1950: 13-7 "without completing a single official pass attempt ... Graham's only completion was wiped out by a penalty ... the last time an NFL team won without one" | CORRECTED | Wikipedia, 1950 Browns season: two passes thrown, both called back on penalties, no official attempt, and no team since has gone a game without a pass attempt; Browns.com agrees | Now "without a single official pass attempt (the two passes Graham threw were both called back by penalties). No NFL team since has played a whole game without attempting a pass." |
| Owen: heavyset Oklahoman, coaching the Giants since 1930, titles in 1934 and 1938 | VERIFIED | Wikipedia, Steve Owen (co-coach for the last two games of 1930, sole coach from 1931; born in Cleo Springs, Okla.) | none |
| Owen's "6-1-4" that was "a 4-1-6 in reality"; Landry explained and taught it | VERIFIED | Wikipedia, 4-3 defense (Owen, *My Kind of Football*, p. 183) | none |
| Giants 6-0 (Oct 1, 1950, the Browns' first shutout) and 17-13; Browns 8-3 in the Dec 17 playoff; Cleveland's only two losses | VERIFIED | Wikipedia, 1950 Browns season (Groza FGs and a safety vs a Giants FG) | Footnote source added |
| Bill George stood up in 1954; the HOF says no one can be sure who was first | VERIFIED (presented as disputed) | PFHOF, Bill George | none |
| Landry made the 4-3 the Giants' base defense in 1956 with rookie Huff; the Giants won the title; the league copied it the next season | VERIFIED | Wikipedia, 4-3 defense; PFHOF, Landry | none |
| CBS documentary *The Violent World of Sam Huff* | VERIFIED | Wikipedia, Sam Huff; TV Guide listing (Oct 1960, *The Twentieth Century*, hosted by Cronkite) | The year and series were added to the text |
| Lombardi to Green Bay in 1959, aged 45, never an NFL head coach; Giants offensive coach; five titles 1961-67; *Run to Daylight* (1963) | VERIFIED | Common record; PFHOF | none |
| Flex first used in the mid-1960s (1964-66) | SOFTENED (kept as disputed) | PFHOF says only "the 1960s"; PFRA forum citing *D Magazine*: occasionally in 1964, regularly from 1965 | Footnote expanded; the text and the timeline already give a range |
| Flex built against option blocking and around Lilly's quickness | VERIFIED | Wikipedia, 4-3 defense; SI (Zimmerman) | none |
| Dallas reached two straight title games vs GB and won Super Bowls after the 1971 and 1977 seasons | VERIFIED | Common record | none |
| Ice Bowl about -13°F | VERIFIED | Wikipedia, 1967 NFL Championship Game (-13°F at kickoff; -15°F "game-time" also given) | The footnote now points to the game article (the "Ice Bowl" page is a disambiguation page) |
| "Lombardi called a quarterback sneak ... scored with 16 seconds left" | CORRECTED | Same article: third-and-goal with 16 seconds left; Starr conferred with Lombardi; a Kramer and Bowman double-team on Pugh; scored with 13 seconds remaining | Now "Starr conferred with Lombardi and kept the ball on a quarterback sneak ... (a double-team with center Ken Bowman) ... scored with 13 seconds left" |
| 1966 title game 34-27; the Packers won Super Bowl II | VERIFIED | Wikipedia | none |
| Gillman: cut film clips from newsreels at the family theater; Rams 1955-59; Chargers 1960-69; Al Davis's vertical/horizontal quote; coaching tree; Coryell studied him | VERIFIED | Wikipedia, Sid Gillman | none |
| 1963 AFL title: Jan 5, 1964, 51-10; Lincoln 206 rushing and 123 receiving yards | VERIFIED | Wikipedia, 1963 AFL Championship Game | The exact numbers are now in the text |
| AFL: first meeting August 1959; Hunt rebuffed by the NFL; 8 teams; two-point conversion (NFL 1994); names on jerseys; scoreboard clock; equal ABC sharing; $36M NBC deal from 1965; Namath $427,000 on Jan 2, 1965; merger announced June 8, 1966; AFC = 10 AFL teams + Colts, Browns, Steelers; HBCU recruiting | VERIFIED | Wikipedia, American Football League | none |
| Stram: 1960-74; AFL titles 1962, 1966 and 1969; first to use the I and two tight ends; moving pocket; triple stack; Buchanan and Lanier | VERIFIED | Wikipedia, Hank Stram ("first coach in professional football to use Gatorade ... and run both the I formation" and two tight ends); PFHOF | none |
| "Stram became the first pro coach to wear a microphone during a game" | SOFTENED | Wikipedia: "In the Super Bowl, Stram became the first professional football coach to wear a microphone" (scoped to the Super Bowl) | Now "wore a microphone for NFL Films, usually described as a first for a pro coach" |
| Super Bowl III 16-7; Super Bowl IV 23-7 | VERIFIED | Wikipedia | none |
| Timeline: "1969: AFL wins Super Bowls III and IV" in a figure whose years are seasons | CORRECTED | Super Bowl III closed the 1968 season | Row now says "(1968-69 seasons)"; re-rendered and checked |
| Shotgun: Nov 27, 1960, 30-22 over the Colts; QB seven yards deep; Brodie, Kilmer and Waters; 4-1 start including 49-0 and 35-0; Oct 22, 1961 Bears 31-0; Hickey retired it | VERIFIED | PFHOF, "The Shotgun Formation" | none |
| Bill George "lined up over the center" | SOFTENED | The PFHOF says only that George "moved up to the line of scrimmage" and the Bears penetrated "by attacking the center" | The text now follows the HOF wording; the drill diagram stays labeled illustrative |
| The shotgun returned in Dallas in 1975; most NFL snaps are now from the shotgun; under center was about a third of plays in 2025 | VERIFIED | FACTS-current (shotgun 66.2% in 2025; FTN under-center 33.6% in 2025) | none |
| Four causes of the drought: unlimited chucking until 1974; pass blockers' hands limited until 1978; the head slap legal until 1977; zone defenses | VERIFIED | Wikipedia, 1974, 1977 and 1978 NFL seasons | none |
| Arnsparger's 53 in 1972; the 3-4 as a base defense with the 1974 Patriots and Oilers | VERIFIED | Consistent with 05-03 (Fairbanks 1974; Phillips 1974-75) and 11-02 | none |
| 1972 Dolphins: 17-0; SB VII 14-7; No-Name Defense | VERIFIED | Wikipedia, 1972 Dolphins season | none |
| Csonka and Morris the first teammates to each rush for 1,000 yards | VERIFIED | Wikipedia, 1972 Dolphins season ("the first teammates to each rush for 1,000 yards") | Quote added to the footnote |
| Griese broke his leg in week 5; Morrall, 38, started most of the rest | VERIFIED | Wikipedia (week 5 vs San Diego; Morrall 38); SI 1997 (broken right leg and dislocated ankle) | SI source added |
| 1976 Steelers: 1-4 start, nine straight wins, 28 points allowed, five shutouts; Super Bowls after the 1974 and 1975 seasons | VERIFIED | Wikipedia, 1976 Steelers season | none |
| 1972 hashes moved to 70 ft 9 in (23 yd 1 ft 9 in) from 20 yards (in place since 1945); 18.5 ft apart; 29.75 yards to the wide side | VERIFIED | Wikipedia, 1972 NFL season; 01-01's sources; arithmetic | none |
| O.J. Simpson 2,003 in 1973, the first 2,000-yard season | VERIFIED | PFHOF | none |
| 1974 package: goalposts to the end line; kickoffs from the 35; holding 15 to 10; no cut blocks on wide receivers; one chuck after 3 yards; WFL pressure; "long touchdown drives more achievable" | VERIFIED | Wikipedia, 1974 NFL season | none |
| Missed FG "to the line of scrimmage (or the 20, whichever was farther from the kicker's goal)" | CORRECTED | Wikipedia, 1974 NFL season: the line of scrimmage or the 20, "whichever is farther from" the **defense's** goal line. The old wording reversed it | Now "(or to the 20 if the kick came from inside it)" |
| Why the fixes failed: "could still hit a receiver hard once he crossed 3 yards, and legally hit him once more before that" | CORRECTED | 1974 rule: unrestricted contact within 3 yards, one contact beyond | Now "could still jam a receiver as he left the line and hit him again once he crossed 3 yards" |
| "Isaac Curtis rule" nickname | VERIFIED + expanded | Wikipedia, Bump and run coverage (Miami knocked Curtis down "as often as possible" in a 1973 playoff game; Paul Brown, on the rules committee, lobbied for the rule); Boston Globe (Gasper, 2013) | The text gives the real reason (the 1973 playoff and Brown's lobbying); source added |
| 1977: head slap banned; one contact only | VERIFIED | Wikipedia, 1977 NFL season | none |
| 1978: contact only within 5 yards (the Mel Blount rule); extended arms and open hands | VERIFIED | Wikipedia, 1978 NFL season; 11-02 | none |
| Two-point conversion reached the NFL in 1994 | VERIFIED | Wikipedia, AFL | none |

## Uncertain or left as is

- The 1934 change: sources describe a 1926-34 rule penalizing a second (or later) incompletion in a series, but I could not see the 1934 rulebook itself. The new wording follows Wikipedia's "Modern history of American football".
- Roster limits come from a secondary blog that summarizes the Record & Fact Book, plus newspaper reports on the PFRA forum. The text now uses ranges rather than exact numbers.
- The Csonka and Morris "first teammates" claim rests on Wikipedia, and no contrary pre-1972 AFL or NFL pair turned up.
- The −13°F figure is the kickoff temperature; the same Wikipedia article also gives −15°F at game time, so the text says "about −13°F".
