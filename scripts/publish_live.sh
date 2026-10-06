#!/bin/bash
# Live publishing during the writing run (no CI round-trip, no Claude tokens).
#  - every 60 s: once 3 more chapters have finished (planning/reviews/<id>.done), or 30 min have
#    passed with at least one, commit + push their source,
#    re-render the site locally (freeze: auto => only the new chapter executes) and push the built
#    site to the gh-pages branch (worktree at ../course-site), which GitHub Pages serves.
#  - every 5 min otherwise: refresh the Progress page if any review file changed.
# Needs the dev container "rtg" running.  Usage: scripts/publish_live.sh
cd "$(dirname "$0")/.." || exit 1
SITE=../course-site
TRAILER=$'\n\nCo-Authored-By: Claude Opus 5.5 (1M context) <noreply@anthropic.com>\nClaude-Session: https://claude.ai/code/session_017tWEYignuoHaT3tqHoSVdL'
last_done=""; last_rev=""; last_progress=0; last_publish=0; BATCH=3

deploy() {
  rsync -a --delete --exclude .git --exclude pr-preview --exclude .nojekyll _site/ "$SITE"/
  touch "$SITE/.nojekyll"
  (cd "$SITE" && git add -A && git commit -qm "$1" && git push -q origin gh-pages) && echo "$(date +%H:%M) deployed: $1"
}

while true; do
  done_now=$(ls planning/reviews/*.done 2>/dev/null | sort | tr '\n' ' ')
  rev_now=$(ls -l --time-style=+%s planning/reviews/ 2>/dev/null | md5sum)
  new=$(comm -13 <(echo "$last_done" | tr ' ' '\n' | sort) <(echo "$done_now" | tr ' ' '\n' | sort) | grep -c .)
  age=$(( $(date +%s) - last_publish ))
  if [ "$new" -ge "$BATCH" ] || { [ "$new" -ge 1 ] && [ "$age" -ge 1800 ]; } || [ -z "$last_done" ]; then
    n=$(ls planning/reviews/*.done | wc -l)
    docker exec -w /workspaces/course rtg python scripts/gen_toc.py >/dev/null
    for m in planning/reviews/*.done; do
      id=$(basename "$m" .done)
      git add -- chapters/*/"$id"-*.qmd "$m" planning/reviews/"$id"-*.md 2>/dev/null
    done
    if docker exec -w /workspaces/course rtg quarto render --to html >/tmp/rtg-render.log 2>&1; then
      git add _quarto.yml _freeze 2>/dev/null
      git commit -qm "Publish: $n/73 chapters done$TRAILER" && git push -q
      deploy "$n/73 chapters"
    else
      echo "$(date +%H:%M) RENDER FAILED (see /tmp/rtg-render.log); will retry"; sleep 120; continue
    fi
    last_done="$done_now"; last_rev="$rev_now"; last_progress=$(date +%s); last_publish=$(date +%s)
  elif [ "$rev_now" != "$last_rev" ] && [ $(( $(date +%s) - last_progress )) -ge 300 ]; then
    if docker exec -w /workspaces/course rtg quarto render progress.qmd --to html >/tmp/rtg-progress.log 2>&1; then
      deploy "progress update"
    fi
    last_rev="$rev_now"; last_progress=$(date +%s)
  fi
  sleep 60
done
