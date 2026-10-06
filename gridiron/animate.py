"""Render tracking data (simulated from a Play, or real Big Data Bowl frames).

Input contract — a DataFrame with at least:
    frameId, x, y, side ("off" | "def" | "ball"), label
plus optional: time (s, 0 = snap), nflId/displayName (player identity), event.
`gridiron.bdb.prepare()` turns raw BDB files into this shape.

    animate(trk)              -> matplotlib FuncAnimation
    frame_strip(trk, times)   -> Figure of small multiples (print/PDF friendly)
    show_animation(play_or_trk) -> video in HTML builds, frame strip in PDF builds
"""

from __future__ import annotations

import os
import shutil

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import animation

from . import style
from .field import Field, FIELD_WIDTH
from .play import Play, draw_marker

ID_COLS = ("nflId", "displayName")


def _ensure(trk) -> pd.DataFrame:
    if isinstance(trk, Play):
        return trk.to_tracking()
    return trk


def _ident(df):
    """Stable per-player identity column."""
    if "nflId" in df and df["nflId"].notna().any():
        return df["nflId"].fillna(-1).astype(int).astype(str) + "|" + df["displayName"].astype(str)
    return df["displayName"].astype(str)


def _window(df, los, pad=4.0):
    lo = float(df["x"].min()) - los - pad
    hi = float(df["x"].max()) - los + pad
    return (min(lo, -8.0), max(hi, 10.0))


def _los(df):
    snap = df[df.get("frameType", pd.Series("", index=df.index)) == "SNAP"] if "frameType" in df else df.iloc[0:0]
    base = snap if len(snap) else df[df["frameId"] == df["frameId"].min()]
    ball = base[base["side"] == "ball"]
    return float(ball["x"].iloc[0]) if len(ball) else float(base["x"].mean())


def _frame_time(df):
    if "time" in df:
        return df.groupby("frameId")["time"].first()
    snap = df.loc[df.get("frameType", "") == "SNAP", "frameId"]
    f0 = int(snap.iloc[0]) if len(snap) else int(df["frameId"].min())
    fr = df["frameId"].drop_duplicates().sort_values()
    return pd.Series((fr - f0) / 10.0, index=fr.values)


def draw_frame(fld: Field, frame: pd.DataFrame, trails: pd.DataFrame | None = None, ppy=None):
    """Draw one frame onto an existing Field; returns artists."""
    ppy = ppy or fld.pts_per_yard()
    arts = []
    if trails is not None:
        for (_, side), g in trails.groupby(["_id", "side"]):
            if side == "ball":
                continue
            px, py = fld.xy(g["x"].values, g["y"].values)
            col = style.OFFENSE if side == "off" else style.DEFENSE
            arts += fld.ax.plot(px, py, color=col, lw=1.0, alpha=0.45, zorder=3)
    for _, r in frame.iterrows():
        px, py = fld.xy(r["x"], r["y"])
        arts += draw_marker(fld.ax, float(px), float(py), r["side"], r.get("label", ""), ppy)
    return arts


def animate(trk, orient="vertical", width_in=6.0, fps=10, trails=True, title=None, window=None):
    """FuncAnimation of a tracking DataFrame (or a Play)."""
    df = _ensure(trk).copy()
    df["_id"] = _ident(df)
    los = _los(df)
    window = window or _window(df, los)
    lat = (max(0.0, float(df["y"].min()) - 5), min(FIELD_WIDTH, float(df["y"].max()) + 5))
    fld = Field(orient=orient, los=los, window=window, width_in=width_in, to_go=None, lateral=lat)
    ppy = fld.pts_per_yard()
    times = _frame_time(df)
    frames = sorted(df["frameId"].unique())
    clock = fld.ax.text(0.01, 0.99, "", transform=fld.ax.transAxes, ha="left", va="top",
                        fontsize=9, color=style.INK, zorder=20,
                        bbox=dict(boxstyle="round,pad=0.25", fc=style.SURFACE, ec=style.BASELINE, lw=0.6))
    if title:
        fld.ax.set_title(title, loc="left", fontsize=11, fontweight="bold", color=style.INK)
    state = {"arts": []}

    def update(fid):
        for a in state["arts"]:
            a.remove()
        cur = df[df["frameId"] == fid]
        tr = df[df["frameId"] <= fid] if trails else None
        state["arts"] = draw_frame(fld, cur, tr, ppy)
        t = float(times.get(fid, 0.0))
        ev = cur["event"].dropna().iloc[0] if "event" in cur and cur["event"].notna().any() else ""
        clock.set_text(f"{'snap' if abs(t) < 1e-6 else f'{t:+.1f}s'}" + (f"  {ev}" if ev else ""))
        return state["arts"] + [clock]

    anim = animation.FuncAnimation(fld.fig, update, frames=frames, interval=1000 / fps, blit=False)
    return anim


def frame_strip(trk, times=(0.0, 1.0, 2.0, 3.0), ncols=None, width_in=6.5, title=None, lateral_pad=4.0):
    """Small multiples of the play at chosen seconds after the snap (negative = pre-snap).

    The PDF stand-in for an animation: each panel shows positions at that moment
    plus faint trails of where everyone has been.
    """
    df = _ensure(trk).copy()
    df["_id"] = _ident(df)
    los = _los(df)
    tmap = _frame_time(df)
    # size the panels to where players are during the shown moments, not the whole play
    shown = df[df["frameId"].map(tmap) <= max(times) + 0.25]
    window = _window(shown, los, pad=3.0)
    n = len(times)
    ncols = ncols or (2 if n == 4 else min(n, 3))
    nrows = int(np.ceil(n / ncols))
    # crop sideline-to-sideline to where the players are, to keep markers legible
    ylo = max(0.0, float(shown["y"].min()) - lateral_pad)
    yhi = min(FIELD_WIDTH, float(shown["y"].max()) + lateral_pad)
    span_w = yhi - ylo
    span_d = window[1] - window[0]
    panel_w = width_in / ncols
    fig, axes = plt.subplots(nrows, ncols, figsize=(width_in, nrows * panel_w * span_d / span_w + 0.3 * nrows),
                             squeeze=False)
    for ax in axes.flat[n:]:
        ax.axis("off")
    for ax, t in zip(axes.flat, times):
        fid = int((tmap - t).abs().idxmin())
        fld = Field(ax=ax, orient="vertical", los=los, window=window, numbers=False, lateral=(ylo, yhi))
        draw_frame(fld, df[df["frameId"] == fid], df[df["frameId"] <= fid], fld.pts_per_yard())
        lab = "snap" if abs(t) < 1e-6 else f"{t:+.1f}s"
        ax.set_title(lab, fontsize=9, color=style.INK_2, loc="center")
    if title:
        fig.suptitle(title, x=0.01, ha="left", fontsize=11, fontweight="bold", color=style.INK)
    fig.tight_layout()
    return fig


def _pdf_build() -> bool:
    return os.environ.get("RTG_FORMAT", "").lower() in ("pdf", "typst", "print")


def show_animation(trk, times=None, title=None, **kw):
    """In HTML builds: an embedded, scrubbable video. In PDF builds: a frame strip.

    Use as the last line of a Quarto code cell. Pass `times` to choose the PDF panels.
    """
    from IPython.display import HTML, display
    df = _ensure(trk)
    if times is None:
        t = df["time"] if "time" in df else pd.Series([0, 3])
        t_end = float(t.max())
        t_start = float(t.min())
        times = [round(x, 1) for x in np.linspace(max(t_start, -2.0) if t_start < -0.2 else 0.0, t_end, 4)]
    if _pdf_build():
        fig = frame_strip(df, times=times, title=title)
        plt.show()
        return None
    anim = animate(df, title=title, **kw)
    if shutil.which("ffmpeg"):
        html = anim.to_html5_video(embed_limit=40)
        html = html.replace("<video ", '<video style="max-width:100%;height:auto" ')
    else:
        html = anim.to_jshtml(default_mode="once")
    plt.close(anim._fig)
    display(HTML(html))
    return None
