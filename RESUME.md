# RESUME — Reading the Game

## Feedback loop
- Every page: Giscus comment box (GitHub Discussions, category "Announcements", mapped by page path)
  and "Report an issue" / "View source" links. Issue forms in `.github/ISSUE_TEMPLATE/`
  label everything `feedback` plus a type (`fact-check`, `clarity`, `diagram`, `topic-request`).
- Triage: `gh issue list -R joshuawjulian/reading-the-game -l feedback` and
  `gh api graphql` for discussion comments. Fix, then close with a link to the commit.
