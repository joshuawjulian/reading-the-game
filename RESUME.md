# RESUME — Reading the Game

## Status (2026-10-06)
- DONE: scaffold (gridiron lib, Quarto book, per-chapter Typst PDFs, Pages CI, feedback);
  curriculum (73 chapters / 15 parts, planning/CURRICULUM.md, editable source in
  planning/curriculum-src/); gap audit (planning/AUDIT-curriculum.md, all 64 fixes applied);
  verified current facts (planning/FACTS-current.md).
- DONE: pilot chapters 01-04, 03-02, 06-06, 13-02 (19/29/25/42 pp), published. Review logs in planning/reviews/.
  Known: the chapters run long (7.8k-13.8k words vs the 3-7k target); links to unwritten chapters warn until they exist.
- WAITING: the user's verdict on the pilots (tone, depth/length, diagrams).
- NEXT: then the full run of the remaining 69 chapters with the same
  workflow (script saved under the session's workflows/scripts/write-chapters-*.js; it takes
  args {chapters: [{id, path}]}, with paths from planning/chapters.yml), then a final
  whole-book gap audit, the atlas appendices, and the glossary check.

## Feedback loop
- Every page: Giscus comment box (GitHub Discussions, category "Announcements", mapped by page path)
  and "Report an issue" / "View source" links. Issue forms in `.github/ISSUE_TEMPLATE/`
  label everything `feedback` plus a type (`fact-check`, `clarity`, `diagram`, `topic-request`).
- Triage: `gh issue list -R joshuawjulian/reading-the-game -l feedback` and
  `gh api graphql` for discussion comments. Fix, then close with a link to the commit.
