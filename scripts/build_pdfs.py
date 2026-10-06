"""Render every chapter to its own printable PDF (Typst), independent of the HTML book.

Each chapter is copied into an isolated build dir (_pdfbuild/<slug>/) and rendered
standalone, so builds never collide with the book render or with each other.
Relative links (to other chapters, the glossary) are rewritten to the live site.

    python scripts/build_pdfs.py                 # all chapters
    python scripts/build_pdfs.py 01-02-downs     # one or more slugs (prefix match ok)
    python scripts/build_pdfs.py --html SLUG     # also a standalone HTML preview (animations)
    python scripts/build_pdfs.py --jobs 4

Output: pdfs/<slug>.pdf  (HTML preview: _pdfbuild/<slug>/<slug>.html)
Environment: RTG_FORMAT=pdf tells gridiron.show_animation to draw frame strips.
"""

from __future__ import annotations

import argparse
import os
import re
import shutil
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SITE = "https://joshuawjulian.github.io/reading-the-game/"
BUILD = ROOT / "_pdfbuild"
OUT = ROOT / "pdfs"

PDF_PROJECT = """\
project:
  type: default
format:
  typst:
    papersize: us-letter
    margin:
      x: 0.6in
      y: 0.6in
    fontsize: 10pt
    columns: 1
    toc: false
    fig-format: svg
    fig-width: 6.5
    keep-typ: false
    filters:
      - print-answers.lua
execute:
  echo: false
  warning: false
"""

HTML_PROJECT = """\
project:
  type: default
format:
  html:
    embed-resources: true
    code-fold: true
    fig-format: svg
    toc: true
execute:
  warning: false
"""

LINK = re.compile(r"\]\((?!https?://|#|mailto:)([^)\s]+?)(\.qmd)?(#[^)\s]*)?\)")


def chapters() -> list[Path]:
    return sorted(p for p in (ROOT / "chapters").rglob("*.qmd") if not p.name.startswith("_"))


def rewrite_links(text: str, src: Path) -> str:
    def sub(m):
        target, ext, frag = m.group(1), m.group(2), m.group(3) or ""
        resolved = (src.parent / (target + (ext or ""))).resolve()
        try:
            rel = resolved.relative_to(ROOT).as_posix()
        except ValueError:
            return m.group(0)
        if rel.endswith(".qmd"):
            rel = rel[:-4] + ".html"
        elif not ext and not Path(rel).suffix:
            return m.group(0)
        return f"]({SITE}{rel}{frag})"
    return LINK.sub(sub, text)


def build(src: Path, html: bool = False) -> tuple[str, bool, str]:
    slug = src.stem
    d = BUILD / slug
    shutil.rmtree(d, ignore_errors=True)
    d.mkdir(parents=True)
    # copy sibling assets (images, data) the chapter may reference
    for extra in src.parent.glob(f"{slug}_assets"):
        shutil.copytree(extra, d / extra.name)
    (d / f"{slug}.qmd").write_text(rewrite_links(src.read_text(), src))
    shutil.copy(ROOT / "filters" / "print-answers.lua", d / "print-answers.lua")
    env = dict(os.environ, RTG_FORMAT="pdf", PYTHONPATH=str(ROOT))
    (d / "_quarto.yml").write_text(PDF_PROJECT)
    r = subprocess.run(["quarto", "render", f"{slug}.qmd", "--to", "typst"], cwd=d, env=env,
                       capture_output=True, text=True)
    ok = r.returncode == 0 and (d / f"{slug}.pdf").exists()
    log = (r.stdout + r.stderr)[-4000:]
    if ok:
        OUT.mkdir(exist_ok=True)
        shutil.copy(d / f"{slug}.pdf", OUT / f"{slug}.pdf")
    if html and ok:
        (d / "_quarto.yml").write_text(HTML_PROJECT)
        env["RTG_FORMAT"] = "html"
        r2 = subprocess.run(["quarto", "render", f"{slug}.qmd", "--to", "html"], cwd=d, env=env,
                            capture_output=True, text=True)
        ok = ok and r2.returncode == 0
        log += (r2.stdout + r2.stderr)[-2000:]
    return slug, ok, log


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("slugs", nargs="*")
    ap.add_argument("--html", action="store_true")
    ap.add_argument("--jobs", type=int, default=2)
    a = ap.parse_args()
    todo = chapters()
    if a.slugs:
        todo = [p for p in todo if any(p.stem.startswith(s) for s in a.slugs)]
    if not todo:
        if a.slugs:
            sys.exit("no matching chapters")
        print("no chapters yet")
        return
    failed = []
    with ThreadPoolExecutor(a.jobs) as ex:
        for slug, ok, log in ex.map(lambda p: build(p, a.html), todo):
            print(f"{'OK  ' if ok else 'FAIL'} {slug}")
            if not ok:
                failed.append(slug)
                print(log)
    if failed:
        sys.exit(f"{len(failed)} failed: {failed}")


if __name__ == "__main__":
    main()
