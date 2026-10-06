# RESUME — Reading the Game

## Status (2026-10-06)
- DONE: scaffold (gridiron lib, Quarto book, per-chapter Typst PDFs, Pages CI, feedback);
  curriculum (73 chapters / 15 parts, planning/CURRICULUM.md, editable source in
  planning/curriculum-src/); gap audit (planning/AUDIT-curriculum.md, all 64 fixes applied);
  verified current facts (planning/FACTS-current.md).
- DONE: pilot chapters 01-04, 03-02, 06-06, 13-02 (19/29/25/42 pp), published. Review logs in planning/reviews/.
  Known: the chapters run long (7.8k-13.8k words vs the 3-7k target); links to unwritten chapters warn until they exist.
- The user approved the pilots ("THIS IS EXCELLENT"): keep the depth, push straight live.
- RESUMED 17:30 (user: "after they finish only one workflow at a time till reset"):
  4 short runs, one Part 5/6 pair each: wf_1af1b897-6dc (05-02, 06-01), wf_6c5445e6-827 (05-03, 06-02),
  wf_a73773c7-835 (05-04, 06-03), wf_abffd2f3-5a9 (05-05, 06-04).
  THEN launch ONE workflow: scripts/workflows/write-book-batched.js with args = scripts/workflows/single-rest.json
  (the remaining 37 chapters in book order, 2 at a time). Keep it to one workflow until the user's token limit resets.
- WAS IN PROGRESS: remaining 69 chapters via scripts/workflows/write-book-batched.js: 4 workflows, each taking its
  chapters TWO AT A TIME all the way to published (book order; chapters with "drafted": true skip the writer).
  Runs: wf_c480f37f-1d6 wf_ac33f498-efd wf_696ecbf2-3a5 wf_a370e8fb-ddc, args in scripts/workflows/batched{0..3}.json. Live publishing: scripts/publish_live.sh (batches of 3 chapters, progress page every 5 min). The revise stage writes planning/reviews/<id>.done; an auto-publish loop commits and
  pushes chapters that have a .done marker every 20 minutes. To RESUME after an interruption, rerun the
  workflow with resumeFromRunId, or run it fresh with only the chapters that lack a .done marker.
- AFTER: atlas appendices A-G, whole-book gap audit, link/glossary check.
- OLD: then the full run of the remaining 69 chapters with the same
  workflow (script saved under the session's workflows/scripts/write-chapters-*.js; it takes
  args {chapters: [{id, path}]}, with paths from planning/chapters.yml), then a final
  whole-book gap audit, the atlas appendices, and the glossary check.

## Feedback loop
- Every page: Giscus comment box (GitHub Discussions, category "Announcements", mapped by page path)
  and "Report an issue" / "View source" links. Issue forms in `.github/ISSUE_TEMPLATE/`
  label everything `feedback` plus a type (`fact-check`, `clarity`, `diagram`, `topic-request`).
- Triage: `gh issue list -R joshuawjulian/reading-the-game -l feedback` and
  `gh api graphql` for discussion comments. Fix, then close with a link to the commit.

## If the Claude session restarts (everything background dies with it)
1. Resume each workflow: Workflow({scriptPath: scripts/workflows/write-book-batched.js, resumeFromRunId: <run>,
   args: <contents of scripts/workflows/batched{k}.json>}) for k = 0..3 in the run-ID order above. (Finished agent
   steps replay from cache.)
2. `docker start rtg` if needed, then start the publisher (do NOT `pkill -f publish_live.sh` from the same
   command line; it matches itself): `scripts/publish_live.sh >> /tmp/rtg-publish.log 2>&1` in the background.
3. Re-create the 30-min check-in cron (session-only).
