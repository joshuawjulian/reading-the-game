"""Players and the offense-relative frame used to author plays.

Authoring frame (what you type when drawing a play):
  d : yards DOWNFIELD from the line of scrimmage (negative = in the backfield)
  w : yards toward the OFFENSE'S RIGHT from the ball (negative = offense's left)

That frame converts to BDB coordinates with the ball spot (los, ball_y):
  x = los + d        y = ball_y - w
(The offense faces +x, so its right hand points toward -y.)
"""

from __future__ import annotations

from dataclasses import dataclass, replace

OFFENSE_LABELS = {
    "QB": "Q", "RB": "R", "TB": "T", "HB": "H", "FB": "F",
    "WR": "W", "TE": "Y",
    "LT": "LT", "LG": "LG", "C": "C", "RG": "RG", "RT": "RT", "OL": "",
}
DEFENSE_LABELS = {
    "DE": "E", "DT": "T", "NT": "N", "EDGE": "B", "OLB": "B", "ILB": "M",
    "SAM": "S", "MIKE": "M", "WILL": "W", "LB": "L",
    "CB": "C", "NB": "$", "DB": "D", "FS": "FS", "SS": "SS", "S": "S",
}


@dataclass
class Player:
    key: str            # unique id within a play: "X", "LT", "MIKE", "RCB" ...
    pos: str            # position abbreviation (QB, WR, TE, DE, CB ...)
    side: str           # "off" or "def"
    d: float            # alignment depth (yards downfield of LOS; negative = backfield)
    w: float            # alignment width (yards to offense's right of ball)
    label: str | None = None
    jersey: int | None = None

    def __post_init__(self):
        if self.label is None:
            table = OFFENSE_LABELS if self.side == "off" else DEFENSE_LABELS
            self.label = table.get(self.pos, self.key if len(self.key) <= 2 else self.key[:2])

    def moved(self, d=None, w=None, **kw) -> "Player":
        """Copy with a new alignment (or other field changed)."""
        return replace(self, d=self.d if d is None else d, w=self.w if w is None else w, **kw)

    def mirrored(self) -> "Player":
        return replace(self, w=-self.w)


ELIGIBLE = {"WR", "TE", "RB", "FB", "TB", "HB"}
BACKS = {"RB", "FB", "TB", "HB"}


def personnel(players) -> str:
    """NFL personnel shorthand: first digit = backs, second = tight ends ("11", "21" ...)."""
    off = [p for p in players if p.side == "off"]
    rb = sum(p.pos in BACKS for p in off)
    te = sum(p.pos == "TE" for p in off)
    return f"{rb}{te}"
