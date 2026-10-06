"""Load real NFL Big Data Bowl tracking data into gridiron's drawing contract.

Kaggle's BDB files change shape a little each year. What has been stable since
2023: tracking CSVs keyed by (gameId, playId, nflId, frameId) with x, y, s, a,
dis, o, dir, playDirection, and a team column ("club" in recent years, "team"
earlier), plus a plays.csv with possessionTeam. The 2026 edition split frames
into input/output files around the throw. `prepare()` normalizes what it can;
check the year's data dictionary and adapt `COLUMN_ALIASES` if needed.

    trk = bdb.load_tracking("data/bdb/tracking_week_1.csv")
    plays = pd.read_csv("data/bdb/plays.csv")
    one = bdb.prepare(trk, plays, game_id=2022091100, play_id=55)
    show_animation(one)
"""

from __future__ import annotations

import glob

import pandas as pd

from .field import FIELD_LENGTH, FIELD_WIDTH

COLUMN_ALIASES = {"team": "club", "event": "event", "jersey_number": "jerseyNumber",
                  "nfl_id": "nflId", "game_id": "gameId", "play_id": "playId", "frame_id": "frameId",
                  "play_direction": "playDirection", "player_position": "position",
                  "player_name": "displayName"}


def load_tracking(pattern: str) -> pd.DataFrame:
    """Read one or many tracking CSVs (glob pattern allowed)."""
    files = sorted(glob.glob(pattern))
    if not files:
        raise FileNotFoundError(pattern)
    df = pd.concat((pd.read_csv(f) for f in files), ignore_index=True)
    return df.rename(columns={k: v for k, v in COLUMN_ALIASES.items() if k in df.columns})


def normalize_direction(df: pd.DataFrame) -> pd.DataFrame:
    """Flip plays moving left so the offense always moves toward +x (gridiron's convention)."""
    df = df.copy()
    left = df["playDirection"].astype(str).str.lower() == "left"
    df.loc[left, "x"] = FIELD_LENGTH - df.loc[left, "x"]
    df.loc[left, "y"] = FIELD_WIDTH - df.loc[left, "y"]
    for col in ("o", "dir"):
        if col in df:
            df.loc[left, col] = (df.loc[left, col] + 180) % 360
    df["playDirection"] = "right"
    return df


def prepare(trk: pd.DataFrame, plays: pd.DataFrame | None, game_id, play_id,
            label: str = "jersey") -> pd.DataFrame:
    """One play's frames with gridiron columns: side ('off'/'def'/'ball') and label."""
    df = trk[(trk["gameId"] == game_id) & (trk["playId"] == play_id)].copy()
    if df.empty:
        raise ValueError(f"no frames for game {game_id} play {play_id}")
    df = normalize_direction(df)
    is_ball = df["displayName"].astype(str).str.lower().eq("football") | df["nflId"].isna()
    if "player_side" in df:  # 2026-style files label sides directly
        side = df["player_side"].str.lower().map({"offense": "off", "defense": "def"})
    else:
        if plays is None:
            raise ValueError("pass plays.csv (needs possessionTeam) to tell offense from defense")
        poss = plays.loc[(plays["gameId"] == game_id) & (plays["playId"] == play_id), "possessionTeam"].iloc[0]
        side = df["club"].eq(poss).map({True: "off", False: "def"})
    df["side"] = side.where(~is_ball, "ball")
    if label == "jersey" and "jerseyNumber" in df:
        df["label"] = df["jerseyNumber"].fillna("").map(lambda v: "" if v == "" else str(int(v)))
    elif "position" in df:
        df["label"] = df["position"].fillna("")
    else:
        df["label"] = ""
    df["frameId"] = df["frameId"].astype(int)
    if "time" in df:
        df = df.rename(columns={"time": "clock"})
    snap = df.loc[df.get("event", pd.Series(dtype=str)).isin(["ball_snap", "snap_direct"]), "frameId"]
    if "frameType" in df and (df["frameType"] == "SNAP").any():
        snap = df.loc[df["frameType"] == "SNAP", "frameId"]
    f0 = int(snap.min()) if len(snap) else int(df["frameId"].min())
    df["time"] = (df["frameId"] - f0) / 10.0
    if "frameType" not in df:
        df["frameType"] = df["time"].map(lambda t: "SNAP" if t == 0 else ("BEFORE_SNAP" if t < 0 else "AFTER_SNAP"))
    return df.sort_values(["frameId", "side"]).reset_index(drop=True)
