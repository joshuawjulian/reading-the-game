"""One-line-per-stage status of the writing run (same logic as progress.qmd)."""
from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parent.parent
rev = ROOT / "planning" / "reviews"
spec = yaml.safe_load((ROOT / "planning/chapters.yml").read_text())
buckets = {k: [] for k in ["published", "revising", "reviewing", "factcheck", "writing", "queued"]}
for part in spec["parts"]:
    for c in part["chapters"]:
        cid = c[:5]
        path = ROOT / "chapters" / part["dir"] / f"{c}.qmd"
        if (rev / f"{cid}.done").exists():
            st = "published"
        elif (rev / f"{cid}-beginner.md").exists() and (rev / f"{cid}-coach.md").exists():
            st = "revising"
        elif (rev / f"{cid}-factcheck.md").exists():
            st = "reviewing"
        elif path.exists():
            st = "writing"
        else:
            st = "queued"
        buckets[st].append(cid)
for k, v in buckets.items():
    print(f"{k:10s} {len(v):3d}  {' '.join(v) if k != 'queued' and k != 'published' else ''}")
