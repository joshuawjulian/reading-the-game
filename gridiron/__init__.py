"""gridiron — football play diagrams and animations in Big Data Bowl coordinates.

    from gridiron import Play, offense, defense, routes as r, show_animation
"""

from . import style, routes, bdb
from .field import Field, FIELD_LENGTH, FIELD_WIDTH, HASH_NEAR, HASH_FAR, yardline_to_x
from .players import Player, personnel
from .formations import offense, defense, technique, OFFENSE, FRONTS, SHELLS
from .play import Play, draw_marker, add_legend
from .animate import animate, frame_strip, show_animation, draw_frame

__all__ = [
    "style", "routes", "bdb", "Field", "FIELD_LENGTH", "FIELD_WIDTH", "HASH_NEAR", "HASH_FAR",
    "yardline_to_x", "Player", "personnel", "offense", "defense", "technique", "OFFENSE", "FRONTS",
    "SHELLS", "Play", "draw_marker", "add_legend", "animate", "frame_strip", "show_animation", "draw_frame",
]
