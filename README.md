# Reading the Game

A course that takes a casual football fan to a high-level understanding of the game:
formations, personnel, the run and pass games, fronts, coverages, pressure, situational
football, special teams, history, team case studies, and analytics.

**Read it:** https://joshuawjulian.github.io/reading-the-game/ (every chapter also has a printable PDF)

Play diagrams are drawn with **`gridiron`**, a small Python library in this repo that works
in NFL Big Data Bowl tracking coordinates, so the same code animates real BDB plays.

```python
from gridiron import Play, offense, defense, routes as r, show_animation
off = offense("gun_2x2")
p = Play(off, defense("nickel", "single_high", off), title="Smash vs Cover 3")
p.route("X", r.hitch(5)); p.route("H", r.corner(10)); p.pass_to("H", t=2.3)
p.draw()                 # static diagram
p.to_tracking()          # BDB-shaped DataFrame
show_animation(p)        # video (HTML) / frame strip (PDF)
```

Build locally in the dev container (`.devcontainer/`): `python scripts/build_pdfs.py`
for per-chapter PDFs, `quarto render` for the site. Status and roadmap: `RESUME.md`.
