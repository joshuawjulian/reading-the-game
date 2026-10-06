# Authoring contract — Reading the Game

Every chapter is written, fact-checked and beginner-reviewed against this file.
If this file and a habit disagree, this file wins.

## 1. The reader

- An adult who **watches NFL games casually and has never played**. Their model of
  "a play" is picking one in Madden. They have *heard* nickel, Power I, Cover 2,
  blitz, RPO, but cannot say what they are or **why they exist**.
- Analytically minded (data-science grad student, comfortable in Python). Numbers and
  mechanisms land; hand-waving doesn't.
- Goal: watch a live game and **anticipate**: read personnel and formation pre-snap,
  guess run/pass and the coverage, and understand why a coach chose what he did.
- Will later load **NFL Big Data Bowl tracking data** into the `gridiron` library, so
  diagrams are real coordinates, not clip art.

## 2. Chapter shape (adapt per topic; these principles are invariant)

The reader learns best from: **the question → small steps, each with a "why" →
takeaway written last → try it yourself → connections.**

1. **Front matter**: `title`, `subtitle` (one line), and `description`.
2. **Opening hook (the question)**: a concrete moment on a broadcast that this
   chapter explains ("Third-and-6. The offense sends five receivers out. Why does
   the safety walk down?"). One short paragraph.
3. **"You'll be able to…"**: 3–6 bullets, observable skills, not topics.
4. **Body in small steps**. Each `##` section introduces one idea, shows it (diagram),
   then answers **why it exists**: what problem it solves and what it gives up. Every
   scheme is a trade-off; name the trade.
5. **History where it explains the present**: who invented or popularized it, when,
   and *what problem they faced*. Give the person a sentence of humanity (who they were,
   how they thought). Dates and attributions must be verified (see §6).
6. **Film room**: at least one real team or play example (team, season, and
   ideally the game and situation) that shows the concept done well, with what to notice.
7. **Watch for it on Sunday**: a short pre-snap/post-snap checklist the reader can
   use on the next broadcast.
8. **Predict the play**: 1–3 drills. Show a pre-snap picture (diagram), ask what's
   likely and why, and put the answer in a collapsed callout (`collapse="true"`).
9. **Takeaways**: 3–6 bullets, written last.
10. **Connections**: what this builds on, what it sets up (links to chapters), and
    an "If you want to go deeper" line (books, coaches' clinics, sites).

Length: whatever the concept needs. Most chapters will land at 3,000–7,000 words.
Being short never excuses skipping a "why".

## 3. Voice and clarity

- Plain, confident, conversational; second person is fine. No hype, no clichés
  ("chess match" at most once in the whole book).
- **Define every term at first use** in bold, with a one-line plain-English
  definition, and link it to the glossary: `[**nickel**](../../appendices/glossary.qmd#gl-nickel)`.
  Glossary anchors are `gl-` + kebab-case term.
- **Each chapter owns its glossary entries** in front matter, and the glossary page is
  generated from them. Add every term the chapter *teaches* (not terms it only uses):
  ```yaml
  glossary:
    Nickel: "A defense with five defensive backs, usually replacing a linebacker with a slot cornerback."
    "11 personnel": "One running back and one tight end, so three wide receivers."
  ```
  The anchor is the term, lowercased and kebab-cased: `Nickel` → `#gl-nickel`,
  `11 personnel` → `#gl-11-personnel`. Check the curriculum's term index before
  defining a term; define it only in the chapter that owns it.
- **Never use a term before it's taught.** If unavoidable, give a one-line gloss and
  a forward link ("we'll build this fully in [Coverages](...)").
- Use the **Madden bridge** sparingly but deliberately: a callout titled
  "Madden vs. real life" when a real-football fact contradicts the game-menu mental
  model (who calls the play, how audibles really work, why there isn't a "best play").
- Numbers: give real ranges ("deep safeties usually align 10–14 yards deep"), not fake
  precision. Say when it varies by team.
- Callout vocabulary (use these titles consistently):
  - `callout-note` **"Madden vs. real life"**
  - `callout-tip` **"Watch for it"**
  - `callout-important` **"Why it exists"**
  - `callout-note` **"Film room: <team> <season>"**
  - `callout-caution` **"Common misconception"**
  - `callout-tip` **"Predict the play"** (answer inside a nested collapsed callout)
  - `callout-note` **"Go deeper"** (optional, for advanced side-notes)

## 4. Diagrams with `gridiron`

Every play picture is Python. Read `gridiron/` docstrings. Use this pattern:

```python
#| label: fig-smash-vs-c3
#| fig-cap: "Smash: the corner route attacks over the cornerback, the hitch underneath him."
from gridiron import Play, offense, defense, routes as r, show_animation
off = offense("gun_2x2")
p = Play(off, defense("nickel", "single_high", off), los=35, to_go=10,
         title="Smash vs Cover 3")
p.route("X", r.hitch(5)); p.route("H", r.corner(10))
p.dropback(2.5); p.pass_to("H", t=2.3)
p.drop("FS", (16, 0), zone=(12, 16), label="deep middle")
p.draw(legend=True);
```

- Coordinates: BDB frame (x 0–120 incl. end zones, y 0–53.3, offense moving +x).
  You author in **(d, w)**: d = yards downfield of the LOS, w = yards to the
  offense's right. Routes use (down, out) offsets so they work on either side.
- `offense(name)` / `defense(front, shell, off)` give reasonable starting alignments.
  **Adjust anything that's wrong for your concept** with `player.moved(d=..., w=...)`
  or build `Player(...)` lists by hand. Don't bend the football to fit the helper.
  If a helper is wrong in general, note it in your report (don't edit `gridiron/`
  unless told to).
- `p.draw(lateral=(-14, 14))` zooms on the box for run plays; `lateral="full"` shows the
  whole width. Default `"auto"` fits the players.
- Animations: `show_animation(p, times=[...])` gives a video on the site and a frame
  strip in PDFs. Use for motion, option reads, route timing, and coverage rotation.
  Pick `times` that tell the story (e.g., `[-1.5, 0, 1.0, 2.2]`). At most ~4 per chapter.
- Every figure: `#| label: fig-...` and a `#| fig-cap:` that states what to notice.
- Diagrams teach one thing. Show only the actions that matter; leave other players
  standing. Use `p.highlight(key)` for the player the reader should watch and
  `p.note(text, at=(d, w))` for short on-field labels.
- **Look at every diagram you make** (render it to PNG and open it). Check that
  labels don't collide, paths are visible, and the football is right: alignments,
  depths, who blocks whom, legal formation (7 on the line; only the ends on the line are
  eligible; one player in motion and not moving forward at the snap).
- Diagrams are illustrative and typical, not a specific team's exact playbook,
  unless the caption says so.

## 5. Code in chapters

- Code is folded on the website ("Show the Python") and hidden in the PDFs.
- Keep code readable: a reader should be able to copy a cell and tweak a route.
- Analytics chapters: use `nflreadpy` (nflverse) and cache to `data/cache/`. Prefer
  completed seasons through 2025. State the season(s) and filters used.
- Charts follow `gridiron.style.apply()` (validated palette, recessive grid, one axis,
  legend for 2 or more series).

## 6. Facts and verification

- Every **historical claim, date, attribution, statistic, rule detail and
  team example** must be checkable. Put sources in footnotes (`[^1]`) with a URL or a
  book citation. Prefer primary or authoritative sources: NFL Football Operations and the
  rulebook, Pro Football Reference, nflverse data, team sites, Hall of Fame bios,
  respected books (*Blood, Sweat and Chalk*, *The Art of Smart Football*, *Take Your
  Eye Off the Ball*), and coaches' own clinic talks and interviews.
- If something is commonly repeated but disputed (e.g., who "invented" a scheme),
  say so and present the main claims.
- Current through the **2025 season** (today is October 2026). Flag anything
  that may have changed since.
- Rules: cite the current NFL rule (e.g., kickoff rules changed in 2024 and 2025).
- Never invent a specific game, play, score, quote or stat. If you can't verify it,
  generalize it ("in the 2019 season the 49ers ran outside zone more than any other
  play") or drop it.

## 7. Files and rendering

- Chapter file: `chapters/<NN-part-slug>/<NN-MM-chapter-slug>.qmd`.
- Front matter `title:` is required. No `@sec-` cross-refs; use relative markdown
  links to `.qmd` files (rewritten for PDFs automatically).
- Render-check one chapter (isolated; safe to run in parallel):
  `docker exec -w /workspaces/course rtg python scripts/build_pdfs.py <slug> --html`
  → `pdfs/<slug>.pdf` and `_pdfbuild/<slug>/<slug>.html`. Rasterize pages to look at them:
  `docker exec -w /workspaces/course rtg pdftoppm -r 60 -png pdfs/<slug>.pdf _pdfbuild/<slug>/page`.
- A chapter is not done until its PDF renders with zero errors and you have looked at
  every diagram.
