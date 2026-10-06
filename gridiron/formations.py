"""Offensive formations and defensive fronts/shells.

Everything is authored with the formation's STRENGTH to the offense's right
(w > 0); pass strength="left" to mirror. Alignments are typical landmarks, not
laws: real teams adjust splits by hash, opponent and play.

Offense:  offense("gun_trips")             -> list[Player]
Defense:  defense("nickel", "two_high", off)  aligns DBs to the offense's receivers
List what exists with OFFENSE.keys(), FRONTS.keys(), SHELLS.
"""

from __future__ import annotations

from .players import Player, ELIGIBLE, BACKS

# --- landmarks (yards from the ball, ball on the middle of the field) -----------
OL_SPLIT = 1.6      # center-to-guard, guard-to-tackle spacing
LINE_D = -0.7       # linemen and receivers "on the ball"
OFF_BALL = -1.5     # receivers "off the ball"
TE_W = 4.8          # inline tight end
WING_W = 6.2        # wing, just outside and behind the TE
WIDE = 15.0         # outside receiver near the numbers
SLOT = 9.0          # slot receiver
UNDER_CENTER = -1.9  # drawn a little off the center for legibility
GUN = -5.0
PISTOL = -3.5
FB_D = -4.5
TB_D = -7.0


def _ol():
    return [
        Player("LT", "LT", "off", LINE_D, -2 * OL_SPLIT, label=""),
        Player("LG", "LG", "off", LINE_D, -OL_SPLIT, label=""),
        Player("C", "C", "off", LINE_D, 0.0, label="C"),
        Player("RG", "RG", "off", LINE_D, OL_SPLIT, label=""),
        Player("RT", "RT", "off", LINE_D, 2 * OL_SPLIT, label=""),
    ]


def _P(key, pos, d, w, label=None):
    return Player(key, pos, "off", d, w, label=label or key)


# Each entry: list of skill players (OL added automatically). Strength = right.
OFFENSE = {
    # 21 personnel: two backs, one TE
    "i_form": [
        _P("QB", "QB", UNDER_CENTER, 0, "Q"), _P("FB", "FB", FB_D, 0, "F"), _P("RB", "RB", TB_D, 0, "T"),
        _P("Y", "TE", LINE_D, TE_W), _P("X", "WR", LINE_D, -WIDE), _P("Z", "WR", OFF_BALL, WIDE),
    ],
    "offset_i": [
        _P("QB", "QB", UNDER_CENTER, 0, "Q"), _P("FB", "FB", FB_D, 1.5, "F"), _P("RB", "RB", TB_D, 0, "T"),
        _P("Y", "TE", LINE_D, TE_W), _P("X", "WR", LINE_D, -WIDE), _P("Z", "WR", OFF_BALL, WIDE),
    ],
    # 22 personnel: two backs, two TEs (heavy run formation)
    "i_form_22": [
        _P("QB", "QB", UNDER_CENTER, 0, "Q"), _P("FB", "FB", FB_D, 0, "F"), _P("RB", "RB", TB_D, 0, "T"),
        _P("Y", "TE", LINE_D, TE_W), _P("U", "TE", LINE_D, -TE_W, "U"), _P("Z", "WR", OFF_BALL, WIDE),
    ],
    # "Power I": a third back offset beside the fullback (31 personnel). Usage varies by era.
    "power_i": [
        _P("QB", "QB", UNDER_CENTER, 0, "Q"), _P("FB", "FB", FB_D, 0, "F"), _P("RB", "RB", TB_D, 0, "T"),
        _P("H", "RB", FB_D, 1.8, "H"),
        _P("Y", "TE", LINE_D, TE_W), _P("X", "WR", LINE_D, -WIDE),
    ],
    # 12 personnel, two TEs inline, both WRs off the ball
    "ace": [
        _P("QB", "QB", UNDER_CENTER, 0, "Q"), _P("RB", "RB", TB_D, 0, "R"),
        _P("Y", "TE", LINE_D, TE_W), _P("U", "TE", LINE_D, -TE_W, "U"),
        _P("X", "WR", OFF_BALL, -WIDE), _P("Z", "WR", OFF_BALL, WIDE),
    ],
    # 11 personnel, under center, 2x2
    "singleback": [
        _P("QB", "QB", UNDER_CENTER, 0, "Q"), _P("RB", "RB", TB_D, 0, "R"),
        _P("Y", "TE", LINE_D, TE_W), _P("Z", "WR", OFF_BALL, WIDE),
        _P("X", "WR", LINE_D, -WIDE), _P("H", "WR", OFF_BALL, -SLOT),
    ],
    "gun_2x2": [
        _P("QB", "QB", GUN, 0, "Q"), _P("RB", "RB", GUN, -1.5, "R"),
        _P("X", "WR", LINE_D, -WIDE), _P("H", "WR", OFF_BALL, -SLOT),
        _P("Y", "TE", OFF_BALL, SLOT), _P("Z", "WR", LINE_D, WIDE),
    ],
    # 11 personnel trips (3x1) with the TE attached to the trips side
    "gun_trips": [
        _P("QB", "QB", GUN, 0, "Q"), _P("RB", "RB", GUN, -1.5, "R"),
        _P("X", "WR", LINE_D, -WIDE),
        _P("Y", "TE", LINE_D, TE_W), _P("H", "WR", OFF_BALL, SLOT + 1), _P("Z", "WR", OFF_BALL, WIDE + 2),
    ],
    # 10/11 personnel, empty backfield 3x2 (here: 11 with the back split out)
    "gun_empty": [
        _P("QB", "QB", GUN, 0, "Q"),
        _P("X", "WR", LINE_D, -WIDE - 1), _P("H", "WR", OFF_BALL, -SLOT),
        _P("Z", "WR", LINE_D, WIDE + 1), _P("Y", "TE", OFF_BALL, SLOT + 1), _P("RB", "RB", OFF_BALL, 5.5, "R"),
    ],
    "pistol": [
        _P("QB", "QB", PISTOL, 0, "Q"), _P("RB", "RB", TB_D, 0, "R"),
        _P("Y", "TE", LINE_D, TE_W), _P("Z", "WR", OFF_BALL, WIDE),
        _P("X", "WR", LINE_D, -WIDE), _P("H", "WR", OFF_BALL, -SLOT),
    ],
    "gun_bunch": [
        _P("QB", "QB", GUN, 0, "Q"), _P("RB", "RB", GUN, -1.5, "R"),
        _P("X", "WR", LINE_D, -WIDE - 1),
        _P("H", "WR", LINE_D, 8.0), _P("Y", "TE", OFF_BALL, 6.6), _P("Z", "WR", OFF_BALL, 9.4),
    ],
    # Wishbone: fullback close behind the QB, two halfbacks deeper and wider (31 personnel)
    "wishbone": [
        _P("QB", "QB", UNDER_CENTER, 0, "Q"), _P("FB", "FB", -3.5, 0, "F"),
        _P("LH", "RB", -5.0, -2.5, "H"), _P("RH", "RB", -5.0, 2.5, "H"),
        _P("Y", "TE", LINE_D, TE_W), _P("X", "WR", LINE_D, -WIDE),
    ],
    # Goal line / jumbo: three TEs and two backs (23 personnel)
    "goal_line": [
        _P("QB", "QB", UNDER_CENTER, 0, "Q"), _P("FB", "FB", FB_D, 0, "F"), _P("RB", "RB", TB_D, 0, "T"),
        _P("Y", "TE", LINE_D, TE_W), _P("U", "TE", LINE_D, -TE_W, "U"), _P("W", "TE", OFF_BALL, WING_W, "W"),
    ],
}


def offense(name: str, strength: str = "right") -> list[Player]:
    """Return the 11 offensive players for a named formation."""
    if name not in OFFENSE:
        raise KeyError(f"unknown formation {name!r}; have {sorted(OFFENSE)}")
    players = _ol() + [p.moved() for p in OFFENSE[name]]
    if strength == "left":
        players = [p.mirrored() for p in players]
    assert len(players) == 11, name
    return players


# --- defense -----------------------------------------------------------------
DL_D = 1.0     # defensive linemen depth
LB_D = 4.5     # off-ball linebacker depth


def technique(t: str, sgn: int = 1) -> float:
    """Width for a defensive lineman's technique number, on side sgn (+1 = offense's right).

    The common (Bear Bryant-derived) numbering: even = head-up on a lineman,
    odd = shaded to the outside. 0 nose on center, 1 shade on center, 2 head-up
    guard, 2i inside shade guard, 3 outside shade guard, 4i inside shade tackle,
    4 head-up tackle, 5 outside shade tackle, 7 inside shade TE, 6 head-up TE,
    9 outside shade TE. Systems differ; see the fronts chapter.
    """
    g, t_ = OL_SPLIT, 2 * OL_SPLIT
    table = {"0": 0.0, "1": 0.7, "2i": g - 0.6, "2": g, "3": g + 0.75, "4i": t_ - 0.6, "4": t_,
             "5": t_ + 0.8, "7": TE_W - 0.6, "6": TE_W, "9": TE_W + 0.9, "wide9": TE_W + 2.3}
    return sgn * table[t]


def _D(key, pos, d, w, label=None):
    return Player(key, pos, "def", d, w, label=label)


def _front(name, s):
    """Front players. s = +1 if offense strength is to its right."""
    if name == "4-3_over":
        return [
            _D("SDE", "DE", DL_D, technique("7", s)), _D("SDT", "DT", DL_D, technique("3", s)),
            _D("WDT", "DT", DL_D, technique("1", -s)), _D("WDE", "DE", DL_D, technique("5", -s)),
            _D("SAM", "SAM", LB_D - 0.5, s * 5.6), _D("MIKE", "MIKE", LB_D, s * 0.8),
            _D("WILL", "WILL", LB_D, -s * 3.0),
        ]
    if name == "4-3_under":
        return [
            _D("SAM", "SAM", DL_D, technique("9", s)), _D("SDE", "DE", DL_D, technique("5", s)),
            _D("NT", "NT", DL_D, technique("1", s)), _D("WDT", "DT", DL_D, technique("3", -s)),
            _D("WDE", "DE", DL_D, technique("5", -s) - s * 1.0),
            _D("MIKE", "MIKE", LB_D, s * 1.2), _D("WILL", "WILL", LB_D, -s * 2.6),
        ]
    if name == "3-4":
        return [
            _D("SDE", "DE", DL_D, technique("4i", s)), _D("NT", "NT", DL_D, technique("0")),
            _D("WDE", "DE", DL_D, technique("4i", -s)),
            _D("SOLB", "OLB", DL_D, technique("9", s)), _D("WOLB", "OLB", DL_D, technique("wide9", -s) * 0.75),
            _D("MIKE", "ILB", LB_D, s * 2.0, "M"), _D("WILL", "ILB", LB_D, -s * 2.0, "W"),
        ]
    if name == "nickel":   # 4-2-5
        return [
            _D("SDE", "DE", DL_D, technique("7", s)), _D("SDT", "DT", DL_D, technique("3", s)),
            _D("WDT", "DT", DL_D, technique("1", -s)), _D("WDE", "DE", DL_D, technique("5", -s) - s * 1.0),
            _D("MIKE", "MIKE", LB_D, s * 1.8), _D("WILL", "WILL", LB_D, -s * 2.0),
        ]
    if name == "dime":     # 4-1-6
        return [
            _D("SDE", "DE", DL_D, technique("5", s) + s * 1.0), _D("SDT", "DT", DL_D, technique("3", s)),
            _D("WDT", "DT", DL_D, technique("3", -s)), _D("WDE", "DE", DL_D, technique("5", -s) - s * 1.0),
            _D("MIKE", "MIKE", LB_D + 0.5, 0.0),
        ]
    if name == "46":
        # "Bear": both guards and the center covered; SS walked down as an extra box player.
        return [
            _D("WDE", "DE", DL_D, technique("5", -s) - s * 1.2), _D("WDT", "DT", DL_D, technique("3", -s)),
            _D("NT", "NT", DL_D, 0.0), _D("SDT", "DT", DL_D, technique("3", s)),
            _D("SAM", "SAM", DL_D, technique("9", s)), _D("WILL", "WILL", DL_D, technique("9", s) + s * 1.8),
            _D("MIKE", "MIKE", LB_D, s * 2.0), _D("SS", "SS", LB_D + 0.5, -s * 3.5),
        ]
    raise KeyError(f"unknown front {name!r}; have {FRONTS}")


FRONTS = ["4-3_over", "4-3_under", "3-4", "nickel", "dime", "46"]
SHELLS = ["two_high", "single_high", "zero"]


def _receivers(off):
    """Non-backfield eligible receivers, split by side, ordered outside-in."""
    rec = [p for p in off if p.pos in ELIGIBLE and not (p.pos in BACKS and abs(p.w) < 3)]
    right = sorted([p for p in rec if p.w > 0], key=lambda p: -p.w)
    left = sorted([p for p in rec if p.w < 0], key=lambda p: p.w)
    return left, right


def defense(front: str, shell: str = "two_high", off: list[Player] | None = None,
            press: bool = False, strength: str | None = None) -> list[Player]:
    """Build 11 defenders: a front plus DBs aligned to the offense's receivers.

    shell: "two_high" (two deep safeties ~12 yds), "single_high" (one deep middle
    safety, the other in the box), "zero" (no deep safety: everyone down).
    """
    off = off or []
    if strength is None:
        te = [p for p in off if p.pos == "TE"]
        sw = sum(p.w for p in te) if te else sum(p.w for p in off if p.pos in ELIGIBLE)
        strength = "left" if sw < 0 else "right"
    s = 1 if strength == "right" else -1
    players = _front(front, s)
    n_db = 11 - len(players)
    left, right = _receivers(off)
    cb_d = 1.0 if press else 6.5
    out: list[Player] = []

    def over(rec_list, sgn, default_w):
        if rec_list:
            return rec_list[0].w + 0.0
        return sgn * default_w

    # corners on the widest receiver each side (offense's left = LCB)
    out.append(_D("LCB", "CB", cb_d, over(left, -1, 12.0)))
    out.append(_D("RCB", "CB", cb_d, over(right, 1, 12.0)))
    n_nick = max(0, n_db - 4) if n_db >= 5 else 0
    # nickel/dime over the #2 receivers, more crowded side first
    sides = sorted([(right, 1), (left, -1)], key=lambda t: -len(t[0]))
    for i in range(n_nick):
        lst, sgn = sides[i % 2]
        w = lst[1].w if len(lst) > 1 else sgn * 7.0
        key, pos = ("NB", "NB") if i == 0 else ("DB", "DB")
        out.append(_D(key, pos, 5.0, w + sgn * 0.5))
    n_safe = n_db - 2 - n_nick
    has_ss = any(p.key == "SS" for p in players)
    if n_safe >= 2:
        if shell == "two_high":
            out += [_D("FS", "FS", 12.0, -s * 9.0), _D("SS", "SS", 12.0, s * 9.0)]
        elif shell == "single_high":
            out += [_D("FS", "FS", 13.0, 0.0), _D("SS", "SS", 7.0, s * 6.0)]
        else:  # zero
            out += [_D("FS", "FS", 6.0, -s * 4.0), _D("SS", "SS", 6.0, s * 5.0)]
    elif n_safe == 1:
        key = "FS" if has_ss else "SS"
        out.append(_D(key, key, 13.0 if shell != "zero" else 6.0, 0.0))
    return players + out
