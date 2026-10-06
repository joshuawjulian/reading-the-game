"""Write planning/chapters.yml (book TOC source) from the curriculum data files."""
import re, sys
from pathlib import Path
import yaml

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))
import data1, data2  # noqa: E402

parts = data1.PARTS  # data2 registers into data1
chs = data1.CH
out = []
for p in parts:
    short = re.sub(r"[^a-z0-9]+", "-", p["title"].split(":")[0].lower()).strip("-")
    mine = [c for c in chs if c["id"].split("-")[0] == p["id"]]
    out.append({"title": f"Part {int(p['id'])}: {p['title'].split(':')[0]}",
                "dir": f"{p['id']}-{short}",
                "chapters": [f"{c['id']}-{c['slug']}" for c in mine]})
(HERE.parent / "chapters.yml").write_text(yaml.safe_dump({"parts": out}, sort_keys=False, width=120))
print(sum(len(p["chapters"]) for p in out), "chapters")
