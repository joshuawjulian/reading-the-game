# RESUME — Reading the Game

## Status (2026-10-06)
- DONE: scaffold (gridiron lib, Quarto book, per-chapter Typst PDFs, Pages CI, feedback);
  curriculum (73 chapters / 15 parts, planning/CURRICULUM.md, editable source in
  planning/curriculum-src/); gap audit (planning/AUDIT-curriculum.md, all 64 fixes applied);
  verified current facts (planning/FACTS-current.md).
- IN PROGRESS: pilot chapters 01-04, 03-02, 06-06, 13-02 via the write-chapters workflow
  (writer -> web fact-check -> beginner + coach reviews -> revise). Review logs: planning/reviews/.
- NEXT: user reviews the pilots; then the full run of the remaining 69 chapters with the same
  workflow (script saved under the session's workflows/scripts/write-chapters-*.js; it takes
  args {chapters: [{id, path}]}, with paths from planning/chapters.yml), then a final
  whole-book gap audit, the atlas appendices, and the glossary check.

## Feedback loop
- Every page: Giscus comment box (GitHub Discussions, category "Announcements", mapped by page path)
  and "Report an issue" / "View source" links. Issue forms in `.github/ISSUE_TEMPLATE/`
  label everything `feedback` plus a type (`fact-check`, `clarity`, `diagram`, `topic-request`).
- Triage: `gh issue list -R joshuawjulian/reading-the-game -l feedback` and
  `gh api graphql` for discussion comments. Fix, then close with a link to the commit.
