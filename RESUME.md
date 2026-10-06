# RESUME — Reading the Game

## Status (2026-10-06)
- DONE: scaffold (gridiron lib, Quarto book, per-chapter Typst PDFs, Pages CI, feedback);
  curriculum (73 chapters / 15 parts, planning/CURRICULUM.md, editable source in
  planning/curriculum-src/); gap audit (planning/AUDIT-curriculum.md, all 64 fixes applied);
  verified current facts (planning/FACTS-current.md).
- DONE: pilot chapters 01-04, 03-02, 06-06, 13-02 (19/29/25/42 pp), published. Review logs in planning/reviews/.
  Known: the chapters run long (7.8k-13.8k words vs the 3-7k target); links to unwritten chapters warn until they exist.
- The user approved the pilots ("THIS IS EXCELLENT"): keep the depth, push straight live.
- IN PROGRESS: full run of the remaining 69 chapters, IN BOOK ORDER, as 3 parallel workflows (the user asked for a
  few at a time, to read along and spare tokens): wf_a507ef10-81e wf_08614ea2-8ff wf_561a1a0f-08b (round-robin
  thirds of the ordered list; script write-book-*.js). Live publishing: scripts/publish_live.sh (batches of 3 chapters, progress page every 5 min). The revise stage writes planning/reviews/<id>.done; an auto-publish loop commits and
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
1. Resume each chapter workflow with the SAME args and `resumeFromRunId` (finished agent steps replay from cache):
   script `~/.claude/projects/-home-julian-dev-course/<session>/workflows/scripts/write-book-*.js`, run IDs above;
   args = `{chapters: _pdfbuild/fullrun-args.json chapters[k::3]}` for k = 0, 1, 2 (in that run-ID order).
2. `docker start rtg` if needed, then start the publisher (do NOT `pkill -f publish_live.sh` from the same
   command line; it matches itself): `scripts/publish_live.sh >> /tmp/rtg-publish.log 2>&1` in the background.
3. Re-create the 30-min check-in cron (session-only).
