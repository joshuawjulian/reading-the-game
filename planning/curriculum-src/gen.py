import sys, re, collections
from data1 import PARTS, CH
import data2  # noqa: registers parts 7-15

OUT = sys.argv[1]
ids = [c["id"] for c in CH]
assert len(ids) == len(set(ids)), "dup ids"
order = {cid: i for i, cid in enumerate(ids)}
byid = {c["id"]: c for c in CH}

# ---- validation
errs = []
term_home = {}
for c in CH:
    for p in c["prereq"]:
        if p not in order:
            errs.append(f"{c['id']}: unknown prereq {p}")
        elif order[p] >= order[c["id"]]:
            errs.append(f"{c['id']}: prereq {p} not earlier")
    for t in c["terms"]:
        k = t.lower()
        if k in term_home:
            errs.append(f"dup term '{t}' in {c['id']} and {term_home[k][0]}")
        term_home[k] = (c["id"], t)
    if not (3 <= len(c["obj"]) <= 8):
        errs.append(f"{c['id']}: {len(c['obj'])} objectives")
if errs:
    print("\n".join(errs)); sys.exit(1)

TAG = {"S": "Static", "A": "Animation + PDF frame strip", "C": "Data chart (nflverse)", "T": "Tracking-data plot/animation"}
dcount = collections.Counter(d.split(":")[0] for c in CH for d in c["diagrams"])

def anchor(c):
    return f"ch-{c['id']}"

L = []
w = L.append

w("# Football, Explained: Curriculum")
w("")
w("_Planning document for a Quarto book. Curriculum only; no chapter prose. Prepared October 2026; "
  "content current through the 2025 NFL season._")
w("")
w(f"**Size:** {len(PARTS)} parts, {len(CH)} chapters, 6 reference appendices. "
  f"Estimated length {sum(c['pages'] for c in CH)} printed pages of chapters plus roughly 120-160 pages of atlas and glossary.")
w("")
w(f"**Diagram inventory (chapters only):** {dcount['S']} static, {dcount['A']} animations (each also rendered as a PDF frame strip), "
  f"{dcount['C']} nflverse data charts, {dcount['T']} tracking-data figures.")
w("")
w("## Contents")
w("")
w("1. Design principles")
w("2. The chapter template")
w("3. Part and chapter overview")
w("4. Chapter specifications")
w("5. Reference appendices (the atlas)")
w("6. Master term index (glossary seed)")
w("7. Pilot chapters")
w("8. Diagram library requirements")
w("9. Fact-check flags and open questions")
w("")

# ---- 1 design principles
w("## 1. Design principles")
w("")
for p in [
    "**Every concept answers 'why does this exist?'** Each formation, coverage, and scheme is taught as a solution to a problem, "
    "and the problem it creates for the other side is named. The arms race is the course's narrative spine, not just Part 11.",
    "**Never use a concept before it is taught.** Every chapter lists its prerequisites; the build order below satisfies them. "
    "Where a diagram must show something not yet taught (e.g., a front name in a run-game diagram), it is labelled generically "
    "and the chapter states an explicit forward reference.",
    "**Spiral, then deepen.** A deliberately shallow first look at defense (02-06) lets the offense parts mention defenders. "
    "Technique numbers appear in 03-01 and are deepened in 05-01; disguise is hinted at in 02-05 and fully taught in 06-06.",
    "**Pictures first, words second.** Every chapter has diagrams in one consistent visual language (Section 8). Movement is shown "
    "as animation in HTML and as a numbered frame strip in PDF, so nothing depends on the format.",
    "**Real teams, real plays, real data.** Every scheme is anchored to teams that did it well, with season ranges. Charts use nflverse "
    "data; early chapters show the chart with code folded, and Part 13 teaches the reader to build them.",
    "**Watching is the goal.** Every chapter ends with a 'Watch for this on Sunday' drill. The drills feed one prediction log "
    "started in 01-02 and scored in 15-01, so the reader can measure their own improvement.",
    "**Two ways in: learn and look up.** The narrative path (Parts 1-15) teaches; the atlas appendices (A-F) and glossary give "
    "one-page reference cards with consistent fields, each linking back to the teaching chapter.",
    "**Honest about uncertainty.** Coverage names differ by team; charting data has errors; 'beaters' are probabilistic. The "
    "book says so instead of presenting one dialect as truth.",
    "**Levels are stated.** Level 1 = casual-fan basics; 3 = what a well-informed analyst knows; 5 = coach/film-room level. "
    "Chapters at Level 4-5 open with a short 'you'll need' recap box.",
]:
    w(f"- {p}")
w("")

# ---- 2 template
w("## 2. The chapter template")
w("")
w("Every teaching chapter (8-20 printed pages) uses the same skeleton so readers know where to look:")
w("")
for i, s in enumerate([
    "**Cold open:** one real play described in two paragraphs, with the question it raises.",
    "**What you'll learn / You'll need:** objectives and prerequisite links (the 'you'll need' box carries a two-line recap of each prerequisite).",
    "**The problem:** why the concept exists (whose problem does it solve).",
    "**The concept:** diagrams first, then rules, then variations.",
    "**How the other side answers:** the counter, and the counter to the counter.",
    "**History sidebar:** where it came from (college origins where relevant) and which rule changes mattered.",
    "**Who does it best:** team/era examples with seasons.",
    "**By the numbers:** one or two nflverse charts (code folded; reproducible in Part 13).",
    "**Predict the play:** 3-5 frozen pre-snap pictures; the reader predicts, then the answer shows the animation/frame strip.",
    "**Watch for this on Sunday:** the drill, plus what to record in the prediction log.",
    "**Key terms:** each term linked to the glossary.",
], 1):
    w(f"{i}. {s}")
w("")
w("Case-study chapters (Part 12) use: the problem -> the scheme answer -> signature plays -> data fingerprint -> how opponents responded -> what survives.")
w("")

# ---- 3 overview
w("## 3. Part and chapter overview")
w("")
w("| Part | Title | Levels | Chapters | Est. pages |")
w("|---|---|---|---|---|")
for p in PARTS:
    cs = [c for c in CH if c["id"].startswith(p["id"] + "-")]
    w(f"| {p['id']} | {p['title']} | {p['levels']} | {len(cs)} | {sum(c['pages'] for c in cs)} |")
w(f"| | **Total** | | **{len(CH)}** | **{sum(c['pages'] for c in CH)}** |")
w("")
w("Full chapter list:")
w("")
w("| ID | Slug (filename) | Title | Level | Pages | Prerequisites |")
w("|---|---|---|---|---|---|")
for c in CH:
    w(f"| {c['id']} | `{c['id']}-{c['slug']}.qmd` | {c['title']} | {c['level']} | {c['pages']} | {', '.join(c['prereq']) or 'none'} |")
w("")
w("**Reading-order note:** the order above satisfies every prerequisite. Two sanctioned shortcuts: 13-01 (nflverse in Python) can be "
  "read any time after Part 2; Part 11 (history) can be read any time after Part 7 by readers who prefer the story first, "
  "skipping the few references to situational and special-teams material.")
w("")

# ---- 4 chapters
w("## 4. Chapter specifications")
w("")
w("Diagram tags: **[S]** static; **[A]** animation, also rendered as a numbered frame strip in PDF; **[C]** nflverse data chart; "
  "**[T]** tracking-data figure (Big Data Bowl / NGS).")
w("")
for p in PARTS:
    w(f"### Part {p['id']}: {p['title']}")
    w("")
    w(f"_Levels {p['levels']}._ {p['blurb']}")
    w("")
    for c in [c for c in CH if c["id"].startswith(p["id"] + "-")]:
        w(f"#### {c['id']} {c['title']}")
        w("")
        w(f"- **Slug:** `{c['id']}-{c['slug']}` | **Level:** {c['level']} | **Est. length:** {c['pages']} pp")
        w(f"- **Prerequisites:** {', '.join(c['prereq']) or 'none'}")
        if c["fwd"]:
            w(f"- **Forward references (flag in text):** {'; '.join(c['fwd'])}")
        w("- **Learning objectives:**")
        for o in c["obj"]:
            w(f"  - {o}")
        w(f"- **Key terms introduced:** {'; '.join(c['terms']) if c['terms'] else 'none new (consolidation chapter; uses terms from prerequisites)'}")
        w("- **Diagrams:**")
        for d in c["diagrams"]:
            tag, txt = d.split(":", 1)
            w(f"  - [{tag}] {txt.strip()}")
        w(f"- **Team / era examples:** {'; '.join(c['examples'])}")
        w(f"- **Watch for this on Sunday:** {c['drill']}")
        w("")

# ---- 5 appendices
w("## 5. Reference appendices (the atlas)")
w("")
w("The atlas is built from the same diagram source as the chapters (one plate definition, rendered in both places). "
  "Every atlas card has the same fields: **name and aliases | diagram | what it is (2-3 sentences) | why it exists | "
  "strong against / weak against | pre-snap tells | teams known for it | taught in (chapter link)**. "
  "Cards are one per half-page in PDF, searchable in HTML.")
w("")
appx = [
    ("A", "offense-atlas", "Offensive Atlas: Personnel and Formations",
     "All personnel groupings (02-01); classic and spread formations (02-03, 02-04); backfield alignments; motion family (02-05); specialty looks. ~45 cards."),
    ("B", "concept-atlas", "Concept Atlas: Runs, Passes, Screens, RPOs",
     "Run concepts (zone, gap, option, perimeter; 03-02 to 03-05); route tree; quick, dropback, play-action, screen, RPO concepts (04-03 to 04-06); "
     "red-zone and short-yardage concepts (10-03). ~60 cards."),
    ("C", "defense-atlas", "Defensive Atlas: Packages, Techniques, and Fronts",
     "Packages (02-06); technique chart (03-01/05-01); even, odd, hybrid, nickel, goal-line fronts (05-02, 05-03, 10-03); run-fit cheat sheet (05-05). ~30 cards."),
    ("D", "coverage-pressure-atlas", "Coverage and Pressure Atlas",
     "Cover 0, 1 (robber/rat), 2, Tampa 2, 2-Man, 3 (sky/buzz/cloud/match), 4, 6, Palms, 7/split-field, poach (Part 6); "
     "fire zones, sim pressures, overloads, mugs (Part 7); plus the concept x coverage matrix (08-01) and a 'coverage dialects' table "
     "mapping different teams' names for the same call. ~40 cards."),
    ("E", "rules-timeline-trees", "Rules, Timeline, and Coaching Trees",
     "Penalty quick-reference table (yardage, auto first down, enforcement spot); kickoff/punt/OT rule summaries (current as of 2025 season); "
     "rule-change timeline 1906-2025 with each change's strategic effect; Super Bowl results with a one-line scheme note each; coaching-tree diagrams."),
    ("F", "glossary", "Glossary",
     "Alphabetical; every term from Section 6 with a one-sentence definition, aliases/dialect variants (e.g., 'Cover 5 = 2-Man'), "
     "and a link to the defining chapter. Generated from a single YAML terms file so chapter key-term boxes and the glossary never drift."),
]
w("| Appendix | Slug | Title | Contents |")
w("|---|---|---|---|")
for a in appx:
    w(f"| {a[0]} | `appendix-{a[0].lower()}-{a[1]}.qmd` | {a[2]} | {a[3]} |")
w("")
w("Front matter (unnumbered `index.qmd`): how to use the book, the level system, the diagram notation key, and how to set up the Python environment.")
w("")

# ---- 6 term index
w("## 6. Master term index (glossary seed)")
w("")
w(f"{len(term_home)} terms, each defined in exactly one chapter (validated by the generator: no term is defined twice). "
  "Later chapters may deepen a term; the glossary links to the defining chapter.")
w("")
def sortkey(t):
    s = t.lower()
    s = re.sub(r"^[^a-z0-9]+", "", s)
    return s
groups = collections.OrderedDict()
for k, (cid, t) in sorted(term_home.items(), key=lambda kv: sortkey(kv[1][1])):
    first = sortkey(t)[0].upper()
    if first.isdigit():
        first = "0-9"
    groups.setdefault(first, []).append((t, cid))
for g, items in groups.items():
    w(f"**{g}**")
    w("")
    for t, cid in items:
        w(f"- {t} -> {cid}")
    w("")

# ---- 7 pilots (static text appended)
with open("tail.md") as f:
    tail = f.read()
tail = tail.replace("{{NS}}", str(dcount['S'])).replace("{{NA}}", str(dcount['A'])) \
           .replace("{{NC}}", str(dcount['C'])).replace("{{NT}}", str(dcount['T']))
L.append(tail)

open(OUT, "w").write("\n".join(L))
print("chapters", len(CH), "terms", len(term_home), "pages", sum(c['pages'] for c in CH), dict(dcount))
lv = collections.Counter(c["level"] for c in CH); print("levels", sorted(lv.items()))
