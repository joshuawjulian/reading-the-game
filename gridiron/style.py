"""Colors and typography shared by every diagram and chart in the course.

Palette follows the course's validated categorical order: offense = slot 1 (blue),
defense = slot 2 (orange). Text always wears ink colors, never a series color.
"""

import matplotlib as mpl

OFFENSE = "#2a78d6"
OFFENSE_DARK = "#1c5cab"
DEFENSE = "#eb6834"
DEFENSE_DARK = "#b84a1f"
DEFENSE_TINT = "#fde3d7"
OFFENSE_TINT = "#d6e6f9"
THIRD = "#1baf7a"  # aqua: a third actor when needed (e.g., highlighted reads)
LINE_TO_GAIN = "#eda100"

SURFACE = "#fcfcfb"
TURF = "#f3f6ef"  # faint green-gray field surface; prints cleanly
INK = "#0b0b0b"
INK_2 = "#52514e"
MUTED = "#898781"
GRID = "#e1e0d9"
BASELINE = "#c3c2b7"
BALL = "#7a4a21"

# Categorical order for analytics charts (never cycle; fold extras into "Other").
SERIES = ["#2a78d6", "#eb6834", "#1baf7a", "#eda100", "#e87ba4", "#008300", "#4a3aa7", "#e34948"]
SEQUENTIAL_BLUE = ["#cde2fb", "#9ec5f4", "#6da7ec", "#3987e5", "#256abf", "#184f95", "#0d366b"]
DIVERGING = ("#2a78d6", "#f0efec", "#e34948")

FONT = ["DejaVu Sans", "Liberation Sans", "Arial", "sans-serif"]


def apply():
    """Course-wide matplotlib defaults for analytics charts (recessive grid, thin marks)."""
    mpl.rcParams.update({
        "figure.facecolor": SURFACE,
        "axes.facecolor": SURFACE,
        "axes.edgecolor": BASELINE,
        "axes.labelcolor": INK_2,
        "axes.titlecolor": INK,
        "axes.titleweight": "bold",
        "axes.titlelocation": "left",
        "axes.spines.top": False,
        "axes.spines.right": False,
        "axes.grid": True,
        "grid.color": GRID,
        "grid.linewidth": 0.6,
        "xtick.color": MUTED,
        "ytick.color": MUTED,
        "lines.linewidth": 2,
        "axes.prop_cycle": mpl.cycler(color=SERIES),
        "font.family": FONT,
        "legend.frameon": False,
        "savefig.bbox": "tight",
        "figure.dpi": 110,
    })
