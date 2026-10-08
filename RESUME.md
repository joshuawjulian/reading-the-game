# RESUME — Reading the Game

## Layout (2026-10-08)
- Everything lives in `~/dev/nfl/reading-the-game` (formerly `~/dev/course` + `~/dev/course-site`);
  sibling NFL project: `~/dev/nfl/fantasy-2026`.
  `site/` is the `gh-pages` worktree (gitignored). Dev container `rtg` mounts this folder at
  `/workspaces/course`.

## Status (2026-10-08)
- DONE: scaffold (gridiron lib, Quarto book, per-chapter Typst PDFs, Pages CI, feedback);
  curriculum (73 chapters / 15 parts, `planning/CURRICULUM.md`, source in `planning/curriculum-src/`);
  gap audit (`planning/AUDIT-curriculum.md`, all fixes applied); verified facts (`planning/FACTS-current.md`).
- DONE + published: Parts 1-9 and 13-02 (48/73). The user approved the pilots ("THIS IS EXCELLENT"):
  keep the depth (chapters run 8-14k words), push straight live.
- TODO: Parts 10-15 (25 chapters), split between `scripts/workflows/dual-A.json`
  and `dual-B.json` (alternating pairs in book order). The user allowed up to 4 agents at once => two workflows.
- AFTER: atlas appendices A-G, whole-book gap audit, link/glossary check.

## How the writing pipeline runs
- `scripts/workflows/write-book-batched.js` takes `{chapters: [{id, path, drafted}]}` and runs
  each chapter writer -> web fact-check -> beginner + coach reviews -> revise, two at a time.
  The revise step writes `planning/reviews/<id>.done`, which publishes the chapter.
- `scripts/publish_live.sh` (background) commits and pushes chapters with a `.done` marker in
  batches of 3 (or after 30 min), re-renders, and deploys `_site/` to `site/`.

## To restart after a session restart (background work dies with the session)
1. `docker start rtg`.
2. Run the workflow once per args file, passing the script inline (or by `scriptPath` from the repo
   root) with `args` = the contents of `dual-A.json` / `dual-B.json`, minus chapters that
   already have a `.done` marker; mark chapters with a finished draft `"drafted": true`.
   Run journals do not survive a restart, so `resumeFromRunId` usually fails; start fresh runs instead.
3. Start the publisher: `scripts/publish_live.sh >> /tmp/rtg-publish.log 2>&1` in the background.
   Never stop it with `pkill -f publish_live.sh` inside a command line that contains that text,
   because it kills itself; use `pgrep -f` to get the PID first, then `kill` it.

## Feedback loop
- Every page: Giscus comment box (GitHub Discussions, category "Announcements", mapped by page path)
  and "Report an issue" / "View source" links. Issue forms in `.github/ISSUE_TEMPLATE/`
  label everything `feedback` plus a type (`fact-check`, `clarity`, `diagram`, `topic-request`).
- Triage: `gh issue list -R joshuawjulian/reading-the-game -l feedback` and
  `gh api graphql` for discussion comments. Fix, then close with a link to the commit.
