# RESUME — Reading the Game

## Status (2026-10-06)
- DONE: scaffold (gridiron lib, Quarto book, per-chapter Typst PDFs, Pages CI, feedback);
  curriculum (73 chapters / 15 parts, planning/CURRICULUM.md, editable source in
  planning/curriculum-src/); gap audit (planning/AUDIT-curriculum.md, all 64 fixes applied);
  verified current facts (planning/FACTS-current.md).
- DONE: pilot chapters 01-04, 03-02, 06-06, 13-02 (19/29/25/42 pp), published. Review logs in planning/reviews/.
  Known: the chapters run long (7.8k-13.8k words vs the 3-7k target); links to unwritten chapters warn until they exist.
- The user approved the pilots ("THIS IS EXCELLENT"): keep the depth, push straight live.
- IN PROGRESS: full run of the remaining 69 chapters as 12 parallel workflows (the 4-CPU machine caps each at
  2 agents), round-robin chunks of 5-6 chapters: wf_7ae27f97-9ee wf_a85db7a7-aa0 wf_fccf346d-cf1 wf_fdb01c56-e56
  wf_b9d86fc3-dc9 wf_c85d98e5-c87 wf_433977a0-9f4 wf_b667d8f5-90f wf_6f4e1be0-c4d wf_691711c4-da9
  wf_3eaf6523-45a wf_8c5785cf-550 (script write-book-*.js). Live publishing: scripts/publish_live.sh (batches of 3 chapters, progress page every 5 min). The revise stage writes planning/reviews/<id>.done; an auto-publish loop commits and
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
