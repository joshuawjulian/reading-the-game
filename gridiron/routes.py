"""Route and path shapes.

Each helper returns waypoints as (down, out) OFFSETS from where the player starts:
  down : yards toward the defense's end zone
  out  : yards toward the receiver's nearest SIDELINE (negative = toward the middle)
Because "out" is relative to the receiver's side, the same route works for a
receiver on either side of the formation. Pass `side=+1/-1` to Play.route for
players aligned near the ball (backs, the QB) to say which way "out" is.

Depths are typical NFL landmarks; real depths vary by team and by coverage.
"""

from __future__ import annotations


def go(length=25.0):
    """Straight vertical ("fly", "streak", "9 route")."""
    return [(0, 0), (length, 0)]


def fade(length=22.0):
    """Vertical that drifts toward the sideline to create room for a back-shoulder or over-the-top throw."""
    return [(0, 0), (length * 0.4, 0.6), (length, 2.0)]


def seam(length=24.0):
    """Vertical up the seam (between the hash and numbers), usually from a slot or TE."""
    return [(0, 0), (length, -0.5)]


def hitch(depth=5.0):
    """Push to depth, stop and turn back to the QB."""
    return [(0, 0), (depth + 1, 0), (depth, -0.6)]


def slant(stem=2.0, length=8.0):
    """Short stem, then a sharp diagonal break inside."""
    return [(0, 0), (stem, 0), (stem + length * 0.6, -length * 0.8)]


def quick_out(depth=5.0, width=5.0):
    return [(0, 0), (depth, 0), (depth - 0.3, width)]


def out(depth=10.0, width=6.0):
    """Square break toward the sideline."""
    return [(0, 0), (depth, 0), (depth, width)]


def dig(depth=12.0, width=12.0):
    """Square break inside ("in" route). 12+ yards is usually called a dig."""
    return [(0, 0), (depth, 0), (depth, -width)]


def curl(depth=12.0):
    """Push vertical, then turn back inside toward the QB."""
    return [(0, 0), (depth, 0), (depth - 1.5, -1.2)]


def comeback(depth=15.0):
    """Sell vertical, break back toward the sideline."""
    return [(0, 0), (depth, 0), (depth - 2.5, 2.5)]


def post(stem=12.0):
    """Vertical stem, then break toward the goalposts (middle of the field)."""
    return [(0, 0), (stem, 0), (stem + 14, -8)]


def corner(stem=12.0):
    """Vertical stem, then break toward the back pylon (the "flag" route)."""
    return [(0, 0), (stem, 0), (stem + 11, 8)]


def drag(depth=2.0, width=18.0):
    """Shallow cross underneath the linebackers."""
    return [(0, 0), (depth, -1.5), (depth + 1, -width)]


def cross(depth=14.0, width=22.0):
    """Deep crosser: climbs and works across the field."""
    return [(0, 0), (5, -1), (depth, -width)]


def stick(depth=6.0):
    """Push to ~6 yards and sit/settle (the stick concept's middle route)."""
    return [(0, 0), (depth, 0), (depth, -0.8)]


def flat(depth=1.5, width=8.0):
    """Release to the flat (the area near the sideline, close to the LOS)."""
    return [(0, 0), (depth * 0.6, width * 0.4), (depth, width)]


def arrow(depth=4.0, width=7.0):
    return [(0, 0), (depth, width)]


def wheel(width=7.0, length=24.0):
    """Release to the flat, then turn up the sideline."""
    return [(0, 0), (1, width * 0.6), (4, width), (length, width + 1)]


def swing(width=9.0):
    """Back releases flat and slightly backward to the outside."""
    return [(0, 0), (-1, width * 0.45), (0, width)]


def bubble(width=5.0):
    """Slot receiver bows backward then out: a horizontal screen."""
    return [(0, 0), (-1.5, width * 0.4), (-1.0, width)]


def angle(depth=5.0):
    """Back fakes outside, then breaks back inside (Texas/angle route)."""
    return [(0, 0), (2, 3), (depth, 0.5)]


def path(*pts):
    """Arbitrary custom path: path((3,0),(8,-4)) — offsets from the start, (down, out)."""
    return [(0, 0), *pts]
