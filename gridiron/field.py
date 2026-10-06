"""The field, in NFL Big Data Bowl (BDB) coordinates.

BDB convention (used everywhere in this library):
  x : 0 -> 120 yards along the long axis. 0-10 is one end zone, 110-120 the other,
      so the goal lines are x=10 and x=110 and "the 50" is x=60.
  y : 0 -> 53.3 yards across the field (sideline to sideline).
All plays are normalized so the offense moves toward +x ("left to right").
Facing +x, the offense's RIGHT hand points toward -y.

Diagrams are usually shown "vertical" (offense moving up the page), the way a
coach's playbook draws them. That view is a pure rotation of the BDB frame:
    plot_x = 53.3 - y      plot_y = x
so real tracking data and hand-drawn plays share one drawing path.
"""

from __future__ import annotations

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

from . import style

FIELD_LENGTH = 120.0
FIELD_WIDTH = 160 / 3  # 53.33 yd (BDB files round to 53.3)
# NFL hash marks are 70'9" from each sideline.
HASH_NEAR = 70.75 / 3   # 23.58 yd
HASH_FAR = FIELD_WIDTH - HASH_NEAR  # 29.75 yd
MIDDLE = FIELD_WIDTH / 2
# Field numbers: the tops sit ~12 yd in from the sideline; we label at 12.
NUMBERS_IN = 12.0


def yardline_to_x(yardline: float, own: bool = True) -> float:
    """Convert a broadcast yard line ("own 25") to BDB x for an offense moving +x."""
    return 10 + yardline if own else 110 - yardline


class Field:
    """A drawn field window.

    orient  : "vertical" (offense moving up) or "horizontal" (BDB native, moving right)
    los     : line of scrimmage, BDB x
    window  : (behind, ahead) yards shown relative to the LOS, e.g. (-12, 25).
              None shows the whole 120 yards.
    to_go   : yards to the line to gain (draws the yellow line); None to hide
    """

    def __init__(self, ax=None, orient="vertical", los=35.0, window=(-12, 25),
                 to_go=None, width_in=6.5, numbers=True, hashes=True, lateral=None):
        self.orient = orient
        self.los = los
        self.window = window
        self.to_go = to_go
        # lateral = (y_lo, y_hi) in BDB y to zoom across the field; None = sideline to sideline
        self.y0, self.y1 = lateral if lateral is not None else (0.0, FIELD_WIDTH)
        if window is None:
            self.x0, self.x1 = 0.0, FIELD_LENGTH
        else:
            self.x0 = max(0.0, los + window[0])
            self.x1 = min(FIELD_LENGTH, los + window[1])
        if ax is None:
            depth = self.x1 - self.x0
            across = self.y1 - self.y0
            if orient == "vertical":
                h = width_in * depth / across
                fig, ax = plt.subplots(figsize=(width_in, h))
            else:
                h = width_in * across / depth
                fig, ax = plt.subplots(figsize=(width_in, h))
        self.ax = ax
        self.fig = ax.figure
        self._draw(numbers, hashes)

    # -- coordinate transform -------------------------------------------------
    def xy(self, x, y):
        """BDB (x, y) -> plot coordinates for this orientation."""
        x = np.asarray(x, dtype=float)
        y = np.asarray(y, dtype=float)
        if self.orient == "vertical":
            return FIELD_WIDTH - y, x
        return x, y

    def pts_per_yard(self) -> float:
        """Points per yard on the rendered figure; used to size labels to markers."""
        self.fig.canvas.draw_idle()
        bbox = self.ax.get_window_extent()
        span = (self.y1 - self.y0) if self.orient == "vertical" else (self.x1 - self.x0)
        return bbox.width / span * 72 / self.fig.dpi

    # -- drawing --------------------------------------------------------------
    def _line(self, xs, ys, **kw):
        px, py = self.xy(xs, ys)
        self.ax.plot(px, py, **kw)

    def _draw(self, numbers, hashes):
        ax = self.ax
        ax.set_aspect("equal")
        ax.axis("off")
        # turf
        (ax_, ay_), (bx_, by_) = self.xy(self.x0, 0), self.xy(self.x1, FIELD_WIDTH)
        lo_x, hi_x = sorted([float(ax_), float(bx_)])
        lo_y, hi_y = sorted([float(ay_), float(by_)])
        ax.add_patch(Rectangle((lo_x, lo_y), hi_x - lo_x, hi_y - lo_y,
                               facecolor=style.TURF, edgecolor=style.BASELINE, lw=1, zorder=0))
        # end zones
        for ez0 in (0.0, 110.0):
            a, b = max(ez0, self.x0), min(ez0 + 10, self.x1)
            if a < b:
                (p0x, p0y), (p1x, p1y) = self.xy(a, 0), self.xy(b, FIELD_WIDTH)
                rx, ry = min(p0x, p1x), min(p0y, p1y)
                ax.add_patch(Rectangle((rx, ry), abs(p1x - p0x), abs(p1y - p0y),
                                       facecolor=style.GRID, edgecolor="none", alpha=0.6, zorder=0))
        # yard lines every 5, labels every 10
        for x in np.arange(10, 111, 5):
            if self.x0 <= x <= self.x1:
                lw = 1.1 if x in (10, 110) else (0.8 if x % 10 == 0 else 0.5)
                self._line([x, x], [0, FIELD_WIDTH], color=style.BASELINE, lw=lw, zorder=1)
        if hashes:
            for x in np.arange(11, 110, 1):
                if self.x0 <= x <= self.x1 and x % 5:
                    for yh in (HASH_NEAR, HASH_FAR):
                        self._line([x, x], [yh - 0.35, yh + 0.35], color=style.BASELINE, lw=0.5, zorder=1)
                    for ys in (0.2, FIELD_WIDTH - 0.2):
                        self._line([x, x], [ys - 0.3, ys + 0.3], color=style.BASELINE, lw=0.5, zorder=1)
        if numbers:
            for x in np.arange(20, 101, 10):
                if self.x0 + 1 <= x <= self.x1 - 1:
                    yl = int(x - 10 if x <= 60 else 110 - x)
                    for yn in (NUMBERS_IN, FIELD_WIDTH - NUMBERS_IN):
                        px, py = self.xy(x, yn)
                        rot = -90 if self.orient == "vertical" else 0
                        if self.orient == "vertical" and yn > MIDDLE:
                            rot = 90
                        ax.text(px, py, f"{yl}", color=style.MUTED, alpha=0.55, fontsize=9,
                                ha="center", va="center", rotation=rot, zorder=1,
                                fontweight="bold")
        # line of scrimmage and line to gain
        if self.window is not None and self.x0 <= self.los <= self.x1:
            self._line([self.los, self.los], [0, FIELD_WIDTH], color=style.OFFENSE_DARK,
                       lw=1.4, alpha=0.75, zorder=2)
        if self.to_go is not None:
            ltg = self.los + self.to_go
            if self.x0 <= ltg <= self.x1:
                self._line([ltg, ltg], [0, FIELD_WIDTH], color=style.LINE_TO_GAIN, lw=2.2, zorder=2)
        px0, py0 = self.xy(self.x0, self.y0)
        px1, py1 = self.xy(self.x1, self.y1)
        ax.set_xlim(min(px0, px1) - 0.5, max(px0, px1) + 0.5)
        ax.set_ylim(min(py0, py1) - 0.5, max(py0, py1) + 0.5)
        self.fig.patch.set_facecolor(style.SURFACE)
