export const meta = {
  name: 'write-book-batched',
  description: 'Write chapters two at a time end-to-end: writer -> web fact-check -> beginner + coach reviews -> revise & publish',
  phases: [
    { title: 'Write', detail: 'one writer per chapter, renders and inspects its diagrams' },
    { title: 'Fact-check', detail: 'web-verify every factual claim, fix and footnote' },
    { title: 'Review', detail: 'beginner-reader and coach/diagram reviews in parallel' },
    { title: 'Revise', detail: 'apply reviews, re-render, mark done' },
  ],
}

const ROOT = '/home/julian/dev/nfl-learn'
const COMMON = `You are working on "Reading the Game", a football course (Quarto book) in ${ROOT}. The user has seen the four pilot chapters and LOVES them ("THIS IS EXCELLENT") — match their depth, voice and diagram quality. Exemplars: chapters/01-foundations/01-04-what-a-play-really-is.qmd, chapters/03-the-run-game/03-02-zone-running.qmd, chapters/06-pass-coverage/06-06-disguise-rotation-and-split-field.qmd, chapters/13-analytics-and-data/13-02-expected-points-and-success-rate.qmd (skim at least one relevant exemplar to calibrate style, helper patterns and diagram conventions).
Read FIRST: ${ROOT}/planning/AUTHORING.md (the authoring contract — it wins), ${ROOT}/planning/FACTS-current.md (verified current facts; never contradict it; today is 2026-10-08), and your chapter's full spec in ${ROOT}/planning/CURRICULUM.md (search for the chapter ID). Check the CURRICULUM term index: terms this chapter OWNS get defined + glossary front matter; terms owned elsewhere get linked to the owning chapter's file (paths in planning/chapters.yml; the file may not exist yet — fine). Prerequisite chapters that ALREADY EXIST in chapters/: skim them so terminology, labels and diagram conventions stay consistent and you build on (not repeat) what they taught.
Diagrams: the gridiron library in ${ROOT}/gridiron/ (read module docstrings). Do NOT edit gridiron/ (other agents are using it concurrently) — implement anything missing inside the chapter's code and mention it in notes.
Conventions learned from the pilots: (a) Predict-the-play answers are plain markdown callouts \`::: {.callout-tip title="Answer" collapse="true"}\` (NOT emitted from code cells) — the print filter moves them to the chapter end; (b) reference each footnote exactly once (Typst duplicates reused footnotes); (c) keep every on-field label/annotation at least ~1.5 yards inside the drawn window so the field edge never cuts through text — widen window=/lateral= when needed; (d) no label collisions; (e) at most ~4 animations; frame strips must tell the story in print.
Tooling runs in the docker container "rtg" (repo at /workspaces/course): docker exec -w /workspaces/course rtg python scripts/build_pdfs.py <slug> --html ; rasterize: docker exec -w /workspaces/course rtg pdftoppm -r 60 -png pdfs/<slug>.pdf _pdfbuild/<slug>/page ; Read the PNGs to LOOK. Builds are isolated per slug (many agents render concurrently). Never run a full "quarto render" of the book. Do not git commit or push.
No Big Data Bowl data is downloaded: where a spec wants a BDB tracking figure, use gridiron simulated tracking (Play.to_tracking()), label it "simulated, BDB-format", and show the real-data version in an eval: false cell using gridiron.bdb.prepare(). nflverse data: gridiron.data (pbp(), nfl()), cached in data/cache.`

const CHAPTER_RESULT = {
  type: 'object',
  properties: {
    path: { type: 'string' },
    words: { type: 'number' },
    figures: { type: 'number' },
    animations: { type: 'number' },
    renders: { type: 'boolean' },
    notes: { type: 'string', description: 'issues, gridiron gaps, anything unverified or left to do' },
  },
  required: ['path', 'renders', 'notes'],
}

// retry an agent call that dies on transient API errors (agent() returns null)
async function retry(fn, label) {
  for (let i = 0; i < 3; i++) {
    const r = await fn()
    if (r) return r
    log(`${label}: attempt ${i + 1} returned nothing, retrying`)
  }
  return null
}

const chapters = args.chapters

const STAGES = [
  (c) => c.drafted ? Promise.resolve({ path: c.path, renders: true, notes: 'existing complete draft (writer already finished); check its <!-- VERIFY --> comments' }) : retry(() => agent(`${COMMON}

YOUR TASK: write chapter ${c.id} as ${ROOT}/${c.path} (create the directory if needed), per its CURRICULUM spec and AUTHORING.md: every objective covered, every owned term defined and in glossary front matter, every planned diagram/animation/chart built with gridiron, film-room examples, Watch-for-it, Predict-the-play drills with collapsed answers, takeaways, connections. The reader: a casual fan who has never played; every idea gets its "why". Be generous — long-form course, not summary.
Facts: draw on FACTS-current.md and solid knowledge; footnote sources for history, dates, stats, rules. Mark anything uncertain with <!-- VERIFY: ... --> for the fact-checker.
Render (build_pdfs.py <slug> --html), fix all errors, rasterize, LOOK at every diagram page; fix collisions, clipped labels, wrong alignments, illegal formations. Iterate until right. Return the structured result.`,
    { label: `write:${c.id}`, phase: 'Write', schema: CHAPTER_RESULT, effort: 'high' }), `write:${c.id}`),

  (w, c) => retry(() => agent(`${COMMON}

YOUR TASK: FACT-CHECK chapter ${c.id} at ${ROOT}/${c.path}. Writer's notes: ${JSON.stringify((w && w.notes) || '')}.
Load web tools first: ToolSearch "select:WebSearch,WebFetch". Extract EVERY checkable claim: dates, names, attributions, stats, rules and rule-change years, games/plays/scores, team-season examples, staff roles, quotes, and football-technical claims (alignments, rule mechanics). Verify against authoritative sources (NFL rulebook / operations.nfl.com, Pro Football Reference, Hall of Fame, nflverse docs, reputable books/analysts, coaching clinics).
Verdict per claim: VERIFIED (footnote source), CORRECTED (fix + source), SOFTENED (genuinely disputed — present as disputed), REMOVED (unverifiable specific — generalize or cut). Resolve and delete every <!-- VERIFY --> comment. Edit surgically; keep the style.
Log a table claim | verdict | source | change to ${ROOT}/planning/reviews/${c.id}-factcheck.md. Re-render (build_pdfs.py <slug>) to confirm it builds. Return the structured result (notes = counts by verdict + anything uncertain).`,
    { label: `factcheck:${c.id}`, phase: 'Fact-check', schema: CHAPTER_RESULT }), `factcheck:${c.id}`),

  async (f, c) => {
    await parallel([
      () => retry(() => agent(`${COMMON}

YOUR TASK: BEGINNER READER review of chapter ${c.id} (${ROOT}/${c.path}; rasterize pdfs/<slug>.pdf and look at the pages). Role-play the target reader: watches NFL casually, never played; has read ONLY the chapters before this one in curriculum order (see CURRICULUM.md for what those taught). Read start to finish.
Report with exact quotes/locations: (1) terms used before explained, or never explained; (2) leaps — a missing or assumed "why"; (3) diagrams you couldn't decode, or captions that don't say what to notice; (4) drag/repetition; (5) can you actually do each "You'll be able to…" item — attempt the Predict-the-play drills BEFORE opening answers and report; (6) knowledge gaps: what you still wonder that this chapter should answer. Be specific and demanding.
Write to ${ROOT}/planning/reviews/${c.id}-beginner.md; return a concise version. Do NOT edit the chapter.`,
        { label: `beginner:${c.id}`, phase: 'Review' }), `beginner:${c.id}`),
      () => retry(() => agent(`${COMMON}

YOUR TASK: veteran NFL COACH + film analyst review of chapter ${c.id} (${ROOT}/${c.path}) for TECHNICAL accuracy and completeness. Rasterize pdfs/<slug>.pdf and LOOK at every diagram.
Check: correctness of every explanation (how it really works, assignments, landmarks, technique, terminology dialects across systems); every diagram (legal formation, realistic alignments/depths/splits, correct assignments, routes/blocks as real teams draw them, sensible defenders, nothing misleading; labels not clipped by the field edge or colliding); animation/frame-strip timing; missing nuance a coach would insist on; film-room examples well chosen and accurately characterized; sensible gridiron use.
Write to ${ROOT}/planning/reviews/${c.id}-coach.md with concrete fixes (which player, which alignment/route). Return a concise version. Do NOT edit the chapter.`,
        { label: `coach:${c.id}`, phase: 'Review' }), `coach:${c.id}`),
    ])
    return retry(() => agent(`${COMMON}

YOUR TASK: REVISE chapter ${c.id} (${ROOT}/${c.path}) using ${ROOT}/planning/reviews/${c.id}-beginner.md and ${ROOT}/planning/reviews/${c.id}-coach.md (read both fully). Keep the fact-check intact (${ROOT}/planning/reviews/${c.id}-factcheck.md); source any new factual claim.
Address every finding: explain what the beginner couldn't follow, add missing whys, fix every flagged diagram, add missing nuance, cut drag. If you decline a finding, say why. Render (build_pdfs.py <slug> --html), rasterize, LOOK at every diagram page again. Zero render errors required.
Append a "Revision" section (finding -> action) to ${ROOT}/planning/reviews/${c.id}-beginner.md.
FINALLY, only if the chapter renders cleanly, write the file ${ROOT}/planning/reviews/${c.id}.done containing "ok" (this publishes it). Return the structured result.`,
      { label: `revise:${c.id}`, phase: 'Revise', schema: CHAPTER_RESULT, effort: 'high' }), `revise:${c.id}`)
  },
]

// Two chapters at a time, each all the way to published, so chapters land steadily in book order.
const results = []
for (let i = 0; i < chapters.length; i += 2) {
  const batch = chapters.slice(i, i + 2)
  results.push(...(await pipeline(batch, ...STAGES)))
  log(`batch done: ${batch.map(b => b.id).join(', ')}`)
}

const done = results.filter(Boolean).length
log(`${done}/${chapters.length} chapters completed`)
return results.map((r, i) => ({ id: chapters[i].id, renders: r ? r.renders : null, notes: r ? r.notes.slice(0, 400) : 'FAILED' }))
