"""The Play: alignments + actions -> a static diagram, BDB-style tracking frames, and animation.

Typical use
-----------
    from gridiron import Play, offense, defense, routes as r
    off = offense("gun_2x2")
    p = Play(off, defense("nickel", "single_high", off), los=35, to_go=10,
             title="Smash vs Cover 3")
    p.route("X", r.hitch(5)); p.route("H", r.corner(10))
    p.dropback(3); p.pass_to("H", t=2.4)
    p.draw()                       # static playbook diagram
    trk = p.to_tracking()          # pandas DataFrame in Big Data Bowl columns
    show_animation(p)              # video in HTML, frame strip in PDF

Frames used by `.route/.run/...` (see players.py):
  frame="side"  : waypoints are (down, out) offsets, out = toward this player's sideline
  frame="field" : waypoints are (down, right) offsets in the offense's frame
  absolute=True : waypoints are (d, w) alignment coordinates, not offsets
"""

from __future__ import annotations

from dataclasses import dataclass, field as dc_field

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Ellipse, FancyArrowPatch, RegularPolygon

from . import style
from .field import Field, MIDDLE, HASH_NEAR, HASH_FAR, FIELD_WIDTH
from .players import Player, personnel

SPEED = {"route": 7.5, "run": 6.5, "motion": 5.0, "block": 2.2, "pull": 5.0,
         "rush": 5.0, "drop": 5.0, "qbdrop": 4.0, "path": 6.0, "man": 1.0}
BALL_SPEED = 18.0  # yd/s, a firm NFL throw averages roughly 15-20 yd/s over its flight
MARKER_R = 0.75    # yards


@dataclass
class Action:
    kind: str
    key: str
    pts: list           # absolute (d, w) points, first = start
    speed: float
    delay: float = 0.0
    target: str | None = None
    label: str | None = None
    t0: float = 0.0     # filled by compile
    t1: float = 0.0


@dataclass
class Zone:
    center: tuple
    size: tuple          # (depth extent, width extent) in yards
    label: str = ""
    color: str = style.DEFENSE


class Play:
    def __init__(self, offense: list[Player], defense: list[Player] | None = None, los: float = 35.0,
                 ball_y: float | str = "middle", to_go: float | None = 10, title: str | None = None):
        self.players: dict[str, Player] = {}
        for p in list(offense) + list(defense or []):
            if p.key in self.players:
                raise ValueError(f"duplicate player key {p.key!r}")
            self.players[p.key] = p
        self.los = float(los)
        if isinstance(ball_y, str):
            # "left"/"right" hash from the OFFENSE's point of view (offense left = +y)
            ball_y = {"middle": MIDDLE, "left": HASH_FAR, "right": HASH_NEAR}[ball_y]
        self.ball_y = float(ball_y)
        self.to_go = to_go
        self.title = title
        self.actions: list[Action] = []
        self.zones: list[Zone] = []
        self.notes: list[tuple] = []
        self.reads: list[tuple] = []
        self.highlights: dict[str, str] = {}
        self.ball_events: list[tuple] = []  # ("handoff"|"pass"|"pitch", key, t)
        self._compiled = None

    # ------------------------------------------------------------------ helpers
    def keys(self, side=None):
        return [k for k, p in self.players.items() if side is None or p.side == side]

    @property
    def personnel(self) -> str:
        return personnel(self.players.values())

    def _cur(self, key):
        acts = [a for a in self.actions if a.key == key and a.kind not in ("man",)]
        if acts:
            return acts[-1].pts[-1]
        p = self.players[key]
        return (p.d, p.w)

    def _resolve(self, key, pts, frame, absolute, side=None):
        start = self._cur(key)
        if absolute:
            return [start] + [tuple(map(float, q)) for q in pts]
        if frame == "side":
            sgn = side if side is not None else (1 if start[1] >= -0.5 else -1)
            conv = [(start[0] + dn, start[1] + sgn * o) for dn, o in pts]
        else:
            conv = [(start[0] + dn, start[1] + r) for dn, r in pts]
        if conv and np.allclose(conv[0], start):
            conv = conv[1:]
        return [start] + conv

    def _add(self, kind, key, pts, speed=None, delay=0.0, target=None, label=None):
        if key not in self.players:
            raise KeyError(f"no player {key!r}; have {list(self.players)}")
        self.actions.append(Action(kind, key, pts, speed or SPEED[kind], delay, target, label))
        self._compiled = None
        return self

    # ------------------------------------------------------------------ actions
    def motion(self, key, to=None, pts=None, speed=None, frame="field"):
        """Pre-snap motion. `to`=(d, w) absolute end spot, or `pts` offsets."""
        path = self._resolve(key, [to], frame, True) if to is not None else self._resolve(key, pts, frame, False)
        return self._add("motion", key, path, speed)

    def route(self, key, pts, side=None, speed=None, delay=0.0, frame="side", absolute=False, label=None):
        return self._add("route", key, self._resolve(key, pts, frame, absolute, side), speed, delay, label=label)

    def run(self, key, pts, speed=None, delay=0.0, frame="field", absolute=False, label=None):
        """A ball carrier's (or faking back's) path."""
        return self._add("run", key, self._resolve(key, pts, frame, absolute), speed, delay, label=label)

    def path(self, key, pts, speed=None, delay=0.0, frame="field", absolute=False, label=None):
        """Generic movement (e.g., a QB rolling out, a defender's reaction)."""
        return self._add("path", key, self._resolve(key, pts, frame, absolute), speed, delay, label=label)

    def dropback(self, depth=3.0, key="QB", speed=None):
        """QB drop: depth in yards (3 for a gun 3-step, 5-7 from under center)."""
        return self._add("qbdrop", key, self._resolve(key, [(-depth, 0)], "field", False), speed)

    def block(self, key, target=None, pts=None, speed=None, delay=0.0, frame="field"):
        """Drive/reach/down block on a defender (`target`), or toward a spot via `pts` offsets."""
        if target is not None:
            s = np.array(self._cur(key))
            t = np.array(self._cur(target))
            v = t - s
            n = np.linalg.norm(v)
            end = tuple(s + v * max(0.0, (n - 1.0) / n)) if n > 1.0 else tuple(s)
            path = [tuple(s), end]
        else:
            path = self._resolve(key, pts, frame, False)
        return self._add("block", key, path, speed, delay, target=target)

    def pull(self, key, pts, target=None, speed=None, delay=0.0, frame="field"):
        """Lineman pulls along `pts` (offsets) and blocks at the end (optionally on `target`)."""
        path = self._resolve(key, pts, frame, False)
        return self._add("pull", key, path, speed, delay, target=target)

    def rush(self, key, pts=None, target="QB", speed=None, delay=0.0, frame="field"):
        """Pass rush or blitz path. Default: straight at the QB's launch point."""
        if pts is None:
            qb = self.players.get(target)
            st = self._cur(key)
            # aim at the QB's launch point, converging but not all to one spot
            end = (qb.d - 1.5, qb.w + 0.35 * (st[1] - qb.w)) if qb else (-6.0, 0.0)
            path = self._resolve(key, [end], frame, True)
        else:
            path = self._resolve(key, pts, frame, False)
        return self._add("rush", key, path, speed, delay)

    def drop(self, key, to, zone=None, label=None, speed=None, delay=0.0):
        """Zone defender drops to `to`=(d, w). zone=(depth_extent, width_extent) shades the area."""
        path = self._resolve(key, [to], "field", True)
        self._add("drop", key, path, speed, delay, label=None if zone is not None else label)
        if zone is not None:
            self.zones.append(Zone(tuple(to), tuple(zone), label or ""))
        return self

    def man(self, key, target):
        """Man coverage: defender `key` mirrors receiver `target` (follows motion too)."""
        return self._add("man", key, [self._cur(key)], 0.0, target=target)

    def zone(self, center, size, label="", color=None):
        self.zones.append(Zone(tuple(center), tuple(size), label, color or style.DEFENSE))
        return self

    def handoff(self, to, t=0.9):
        self.ball_events.append(("handoff", to, t))
        self._compiled = None
        return self

    def pitch(self, to, t=1.0):
        self.ball_events.append(("pitch", to, t))
        self._compiled = None
        return self

    def pass_to(self, to, t=2.5):
        self.ball_events.append(("pass", to, t))
        self._compiled = None
        return self

    def read(self, target, key="QB"):
        """Dashed 'eyes' line: who the QB (or a defender) is reading."""
        self.reads.append((key, target))
        return self

    def highlight(self, *keys, color=style.THIRD):
        for k in keys:
            self.highlights[k] = color
        return self

    def note(self, text, at, ha="center"):
        """Annotation at alignment coordinates (d, w)."""
        self.notes.append((text, at, ha))
        return self

    # ------------------------------------------------------------------ timing
    def _compile(self):
        if self._compiled is not None:
            return self._compiled
        kf: dict[str, list] = {}
        for key, p in self.players.items():
            acts = [a for a in self.actions if a.key == key and a.kind != "man"]
            pre = [a for a in acts if a.kind == "motion"]
            post = [a for a in acts if a.kind != "motion"]
            t = -sum(_length(a.pts) / a.speed for a in pre)
            frames = [(t, p.d, p.w)]
            for a in pre + post:
                if a.kind != "motion":
                    t = max(t, 0.0) + a.delay
                    frames.append((t, *a.pts[0]))
                a.t0 = t
                for q0, q1 in zip(a.pts[:-1], a.pts[1:]):
                    t += float(np.hypot(q1[0] - q0[0], q1[1] - q0[1])) / a.speed
                    frames.append((t, *q1))
                a.t1 = t
            kf[key] = np.array(frames, dtype=float)
        # man coverage defenders shadow their receiver with a lag and shrinking cushion
        for a in [a for a in self.actions if a.kind == "man"]:
            tgt = kf[a.target]
            p = self.players[a.key]
            off0 = np.array([p.d, p.w]) - _interp(tgt, tgt[0, 0])
            ts = np.unique(np.concatenate([tgt[:, 0], np.linspace(tgt[0, 0], max(tgt[-1, 0], 0) + 0.4, 40)]))
            pts = []
            for t in ts:
                lag = 0.35 if t > 0 else 0.15
                f = 1.0 if t <= 0 else max(0.2, 1 - t / 1.8)
                pts.append((t, *(_interp(tgt, t - lag) + off0 * f)))
            kf[a.key] = np.array(pts)
        t_end = max(float(f[-1, 0]) for f in kf.values())
        t_start = min(float(f[0, 0]) for f in kf.values())
        self._compiled = (kf, t_start, t_end)
        return self._compiled

    def position(self, key, t):
        kf, _, _ = self._compile()
        return _interp(kf[key], t)

    def ball_position(self, t):
        """Ball (d, w) at time t, following snap / handoff / pitch / pass events."""
        kf, _, _ = self._compile()
        if t <= 0 or "QB" not in self.players:
            return np.array([0.0, 0.0])
        qb = self.players["QB"]
        snap_t = 0.12 if qb.d > -2 else 0.45
        if t < snap_t:
            q = _interp(kf["QB"], snap_t)
            return np.array([0.0, 0.0]) + (q - [0.0, 0.0]) * (t / snap_t)
        holder, t_hold = "QB", snap_t
        for kind, to, te in sorted(self.ball_events, key=lambda e: e[2]):
            if t < te:
                break
            if kind == "handoff":
                holder, t_hold = to, te
                continue
            # pass/pitch: in flight from the holder to the target
            start = _interp(kf[holder], te)
            spd = BALL_SPEED if kind == "pass" else 10.0
            t_arr = te + 0.5
            for _ in range(3):
                t_arr = te + float(np.linalg.norm(_interp(kf[to], t_arr) - start)) / spd
            if t < t_arr:
                end = _interp(kf[to], t_arr)
                return start + (end - start) * (t - te) / (t_arr - te)
            holder, t_hold = to, t_arr
        return _interp(kf[holder], t)

    def pass_target_spot(self):
        """(throw_spot, catch_spot) for the first pass, or None."""
        for kind, to, te in self.ball_events:
            if kind in ("pass", "pitch"):
                kf, _, _ = self._compile()
                start = self.ball_position(te)
                spd = BALL_SPEED if kind == "pass" else 10.0
                t_arr = te + 0.5
                for _ in range(3):
                    t_arr = te + float(np.linalg.norm(_interp(kf[to], t_arr) - start)) / spd
                return start, _interp(kf[to], t_arr)
        return None

    # ------------------------------------------------------------------ export
    def to_abs(self, d, w):
        """Alignment frame -> BDB (x, y)."""
        return self.los + np.asarray(d), self.ball_y - np.asarray(w)

    def to_tracking(self, fps=10, t_after=0.6, game_id=0, play_id=0) -> pd.DataFrame:
        """Simulated tracking data in Big Data Bowl columns (normalized: offense moving +x)."""
        kf, t0, t1 = self._compile()
        t0 = np.floor(min(t0, -0.5) * fps) / fps  # keep the snap (t=0) on the frame grid
        ts = np.round(np.arange(t0, t1 + t_after + 1e-9, 1 / fps), 3)
        rows = []
        events = {0.0: "ball_snap"}
        for kind, to, te in self.ball_events:
            events[round(round(te * fps) / fps, 3)] = {"handoff": "handoff", "pass": "pass_forward",
                                                       "pitch": "lateral"}[kind]
        for i, key in enumerate(self.players):
            p = self.players[key]
            dw = np.array([_interp(kf[key], t) for t in ts])
            rows.append(_track_rows(dw, ts, self, key, p.side, p.pos, p.label, 1000 + i, p.jersey, events))
        bdw = np.array([self.ball_position(t) for t in ts])
        rows.append(_track_rows(bdw, ts, self, "football", "ball", "", "", None, None, events))
        df = pd.concat(rows, ignore_index=True)
        df.insert(0, "playId", play_id)
        df.insert(0, "gameId", game_id)
        return df

    # ------------------------------------------------------------------ drawing
    def extent(self):
        ds = [p.d for p in self.players.values()]
        for a in self.actions:
            ds += [q[0] for q in a.pts]
        for z in self.zones:
            ds += [z.center[0] + z.size[0] / 2]
        return min(ds), max(ds)

    def lateral_extent(self, pad=4.0, min_width=26.0):
        """BDB y-range covering every player, path and zone (+pad), at least min_width wide."""
        ws = [p.w for p in self.players.values()]
        for a in self.actions:
            ws += [q[1] for q in a.pts]
        for z in self.zones:
            ws += [z.center[1] - z.size[1] / 2, z.center[1] + z.size[1] / 2]
        ys = [self.ball_y - w for w in ws]
        lo, hi = min(ys) - pad, max(ys) + pad
        if hi - lo < min_width:
            mid = (hi + lo) / 2
            lo, hi = mid - min_width / 2, mid + min_width / 2
        return max(0.0, lo), min(FIELD_WIDTH, hi)

    def draw(self, ax=None, orient="vertical", window=None, width_in=6.5, title=True,
             show_defense=True, legend=False, lateral="auto"):
        """Static playbook-style diagram. Returns the Field.

        window  : (behind, ahead) yards around the LOS; default fits the play
        lateral : "auto" zooms to the players/paths; "full" shows sideline to sideline;
                  or (w_left, w_right) in alignment yards, e.g. (-12, 12) for the box
        """
        lo, hi = self.extent()
        if window is None:
            window = (min(-8.0, lo - 2.5), max(12.0, hi + 3.0))
        if lateral == "auto":
            lat = self.lateral_extent()
        elif lateral == "full" or lateral is None:
            lat = None
        else:
            lat = tuple(sorted((self.ball_y - lateral[0], self.ball_y - lateral[1])))
        fld = Field(ax=ax, orient=orient, los=self.los, window=window, to_go=self.to_go,
                    width_in=width_in, lateral=lat)
        axp = fld.ax
        ppy = fld.pts_per_yard()
        P = lambda d, w: fld.xy(*self.to_abs(d, w))  # noqa: E731

        for z in self.zones:
            cx, cy = P(*z.center)
            wx, wy = (z.size[1], z.size[0]) if orient == "vertical" else (z.size[0], z.size[1])
            axp.add_patch(Ellipse((cx, cy), wx, wy, facecolor=z.color, alpha=0.13,
                                  edgecolor=z.color, lw=0.8, ls=(0, (3, 2)), zorder=2))
            if z.label:
                axp.text(cx, cy, z.label, ha="center", va="center", fontsize=max(6, ppy * 0.9),
                         color=style.INK_2, style="italic", zorder=3)

        _ = self._compile()
        for a in self.actions:
            p = self.players[a.key]
            if not show_defense and p.side == "def":
                continue
            if a.kind == "man":
                tgt = self.players[a.target]
                (x0, y0), (x1, y1) = P(p.d, p.w), P(tgt.d, tgt.w)
                axp.plot([x0, x1], [y0, y1], color=style.DEFENSE, lw=0.9, ls=(0, (1, 2)), zorder=3)
                continue
            xs, ys = P(np.array([q[0] for q in a.pts]), np.array([q[1] for q in a.pts]))
            _draw_action(axp, a.kind, xs, ys, p.side, ppy)
            if a.label:
                axp.text(xs[-1], ys[-1] + 0.9, a.label, fontsize=max(6, ppy * 0.85), color=style.INK_2,
                         ha="center", va="bottom", zorder=6)

        spots = self.pass_target_spot()
        if spots is not None:
            (x0, y0), (x1, y1) = P(*spots[0]), P(*spots[1])
            axp.add_patch(FancyArrowPatch((x0, y0), (x1, y1), arrowstyle="-|>", mutation_scale=9,
                                          color=style.BALL, lw=1.3, ls=(0, (2, 2)), zorder=4,
                                          connectionstyle="arc3,rad=-0.08"))

        for who, tgt in self.reads:
            a0, b0 = self.players[who], self.players[tgt]
            (x0, y0), (x1, y1) = P(a0.d, a0.w), P(b0.d, b0.w)
            axp.plot([x0, x1], [y0, y1], color=style.THIRD, lw=1.2, ls=(0, (4, 2)), zorder=4)

        for key, p in self.players.items():
            if not show_defense and p.side == "def":
                continue
            x, y = P(p.d, p.w)
            draw_marker(axp, float(x), float(y), p.side, p.label, ppy, ring=self.highlights.get(key))

        for text, (d, w), ha in self.notes:
            x, y = P(d, w)
            axp.text(x, y, text, fontsize=max(7, ppy * 0.95), color=style.INK, ha=ha, va="center",
                     zorder=7, bbox=dict(boxstyle="round,pad=0.25", fc=style.SURFACE, ec=style.BASELINE, lw=0.6))

        if title and self.title:
            axp.set_title(self.title, loc="left", fontsize=11, fontweight="bold", color=style.INK)
        if legend:
            add_legend(axp)
        return fld


# ---------------------------------------------------------------------- utils
def _length(pts):
    a = np.asarray(pts, dtype=float)
    return float(np.sum(np.hypot(*np.diff(a, axis=0).T))) if len(a) > 1 else 0.0


def _interp(frames, t):
    """Piecewise-linear position (d, w) at time t from keyframes [[t, d, w], ...]."""
    ts = frames[:, 0]
    if t <= ts[0]:
        return frames[0, 1:].copy()
    if t >= ts[-1]:
        return frames[-1, 1:].copy()
    # side="right" picks the later of duplicate timestamps (a player who waits, then moves)
    i = int(np.searchsorted(ts, t, side="right"))
    t0, t1 = ts[i - 1], ts[i]
    f = 0.0 if t1 == t0 else (t - t0) / (t1 - t0)
    return frames[i - 1, 1:] + f * (frames[i, 1:] - frames[i - 1, 1:])


def _track_rows(dw, ts, play, key, side, pos, label, nfl_id, jersey, events):
    x, y = play.to_abs(dw[:, 0], dw[:, 1])
    dt = np.gradient(ts) if len(ts) > 1 else np.ones_like(ts)
    vx, vy = np.gradient(x) / dt, np.gradient(y) / dt
    s = np.hypot(vx, vy)
    a = np.abs(np.gradient(s) / dt)
    # BDB dir: degrees clockwise from the +y axis (0 = toward +y, 90 = toward +x)
    direc = np.where(s > 0.05, (90 - np.degrees(np.arctan2(vy, vx))) % 360, np.nan)
    ftype = np.where(ts < -1e-9, "BEFORE_SNAP", np.where(np.isclose(ts, 0), "SNAP", "AFTER_SNAP"))
    ev = [events.get(round(float(t), 3), None) for t in ts]
    return pd.DataFrame({
        "nflId": nfl_id, "displayName": key, "frameId": np.arange(1, len(ts) + 1), "frameType": ftype,
        "time": ts, "jerseyNumber": jersey, "club": {"off": "OFF", "def": "DEF", "ball": "football"}[side],
        "playDirection": "right", "x": x, "y": y, "s": s, "a": a, "dis": s * dt, "o": direc, "dir": direc,
        "event": ev, "side": side, "position": pos, "label": label,
    })


def draw_marker(ax, x, y, side, label, ppy, ring=None, r=MARKER_R):
    """One player marker. Offense = filled circle; defense = outlined square (shape AND color differ)."""
    arts = []
    if side == "off":
        patch = Circle((x, y), r, facecolor=style.OFFENSE, edgecolor="white", lw=0.8, zorder=8)
        tcolor = "white"
    elif side == "def":
        patch = RegularPolygon((x, y), 4, radius=r * 1.25, orientation=np.pi / 4,
                               facecolor=style.DEFENSE_TINT, edgecolor=style.DEFENSE, lw=1.3, zorder=8)
        tcolor = style.INK
    else:  # football
        patch = Ellipse((x, y), 0.7, 0.45, facecolor=style.BALL, edgecolor="white", lw=0.5, zorder=9)
        ax.add_patch(patch)
        return [patch]
    ax.add_patch(patch)
    arts.append(patch)
    if ring:
        rp = Circle((x, y), r * 1.55, facecolor="none", edgecolor=ring, lw=2.0, zorder=7)
        ax.add_patch(rp)
        arts.append(rp)
    if label:
        fs = max(4.0, min(9.0, ppy * (1.05 if len(str(label)) <= 1 else 0.8)))
        arts.append(ax.text(x, y, str(label), ha="center", va="center", fontsize=fs, color=tcolor,
                            fontweight="bold", zorder=10))
    return arts


def _draw_action(ax, kind, xs, ys, side, ppy):
    col = style.OFFENSE if side == "off" else style.DEFENSE
    dark = style.OFFENSE_DARK if side == "off" else style.DEFENSE_DARK
    spec = {
        "route": dict(color=col, lw=1.8, ls="-", end="arrow"),
        "run": dict(color=dark, lw=2.6, ls="-", end="arrow"),
        "path": dict(color=col, lw=1.6, ls="-", end="arrow"),
        "motion": dict(color=col, lw=1.4, ls=(0, (3, 2)), end="arrow"),
        "block": dict(color=dark, lw=1.8, ls="-", end="tee"),
        "pull": dict(color=dark, lw=1.8, ls="-", end="tee"),
        "qbdrop": dict(color=col, lw=1.0, ls=(0, (1, 1.5)), end=None),
        "rush": dict(color=col, lw=1.8, ls="-", end="arrow"),
        "drop": dict(color=col, lw=1.3, ls=(0, (3, 2)), end="arrow"),
    }[kind]
    if len(xs) < 2:
        return
    ax.plot(xs[:-1] if spec["end"] == "arrow" else xs, ys[:-1] if spec["end"] == "arrow" else ys,
            color=spec["color"], lw=spec["lw"], ls=spec["ls"], solid_capstyle="round", zorder=4)
    if spec["end"] == "arrow":
        ax.add_patch(FancyArrowPatch((xs[-2], ys[-2]), (xs[-1], ys[-1]), arrowstyle="-|>",
                                     mutation_scale=8 + spec["lw"] * 2, color=spec["color"], lw=spec["lw"],
                                     ls=spec["ls"] if kind != "motion" else "-",
                                     shrinkA=0, shrinkB=0, zorder=4))
    elif spec["end"] == "tee":
        v = np.array([xs[-1] - xs[-2], ys[-1] - ys[-2]])
        n = np.linalg.norm(v)
        if n > 0:
            perp = np.array([-v[1], v[0]]) / n * 0.75
            ax.plot([xs[-1] - perp[0], xs[-1] + perp[0]], [ys[-1] - perp[1], ys[-1] + perp[1]],
                    color=spec["color"], lw=spec["lw"] + 0.6, solid_capstyle="butt", zorder=4)


def add_legend(ax):
    from matplotlib.lines import Line2D
    h = [
        Line2D([], [], marker="o", ls="", markerfacecolor=style.OFFENSE, markeredgecolor="white", ms=9, label="Offense"),
        Line2D([], [], marker="D", ls="", markerfacecolor=style.DEFENSE_TINT, markeredgecolor=style.DEFENSE, ms=8,
               label="Defense"),
        Line2D([], [], color=style.OFFENSE, lw=1.8, label="Route"),
        Line2D([], [], color=style.OFFENSE_DARK, lw=2.6, label="Ball carrier"),
        Line2D([], [], color=style.OFFENSE, lw=1.4, ls=(0, (3, 2)), label="Pre-snap motion"),
        Line2D([], [], color=style.DEFENSE, lw=1.3, ls=(0, (3, 2)), label="Zone drop"),
        Line2D([], [], color=style.BALL, lw=1.3, ls=(0, (2, 2)), label="Pass"),
    ]
    ax.legend(handles=h, loc="upper center", bbox_to_anchor=(0.5, -0.01), ncol=4, fontsize=7.5, frameon=False)
