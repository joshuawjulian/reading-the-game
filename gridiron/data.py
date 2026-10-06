"""nflverse data for the analytics chapters, cached on disk under data/cache/.

    from gridiron.data import nfl, pbp
    plays = pbp([2023, 2024, 2025])          # pandas DataFrame of play-by-play
    ftn = nfl().load_ftn_charting([2025]).to_pandas()

Every chapter shares one filesystem cache (also cached in CI), so a season is
downloaded once. nflreadpy returns polars frames; `pbp()` converts to pandas.
"""

from __future__ import annotations

from functools import lru_cache
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CACHE = ROOT / "data" / "cache"


@lru_cache(maxsize=1)
def nfl():
    """The nflreadpy module, configured for the course's persistent cache."""
    import nflreadpy
    from nflreadpy.config import update_config
    CACHE.mkdir(parents=True, exist_ok=True)
    update_config(cache_mode="filesystem", cache_dir=CACHE, cache_duration=60 * 60 * 24 * 365, verbose=False)
    return nflreadpy


def pbp(seasons, columns=None):
    """Play-by-play as pandas. Pass `columns` to keep memory down for multi-season loads."""
    df = nfl().load_pbp(list(seasons) if not isinstance(seasons, int) else [seasons])
    if columns:
        df = df.select([c for c in columns if c in df.columns])
    return df.to_pandas()
