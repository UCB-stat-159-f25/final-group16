import pandas as pd
import numpy as np

def add_gamekey_and_win(df: pd.DataFrame) -> pd.DataFrame:
    """
    Add:
      - Win: 1 if Res == 'W', else 0
      - GameKey: YYYY-MM-DD_<Tm>_vs_<Opp>

    Requires: Data, Tm, Opp, Res
    """
    required = {"Data", "Tm", "Opp", "Res"}
    missing = required - set(df.columns)
    if missing:
        raise KeyError(f"Missing required columns: {sorted(missing)}")

    out = df.copy()
    out["Data"] = pd.to_datetime(out["Data"], errors="coerce")
    out["Win"] = (out["Res"] == "W").astype(int)
    out["GameKey"] = out["Data"].dt.strftime("%Y-%m-%d") + "_" + out["Tm"] + "_vs_" + out["Opp"]
    return out


def add_per_minute_stats(df: pd.DataFrame, cols=("PTS", "TRB", "AST"), mp_col="MP") -> pd.DataFrame:
    """
    Add per-minute columns:
      STAT_per_min = STAT / max(MP, 1)

    Requires: MP plus each stat in cols
    """
    if mp_col not in df.columns:
        raise KeyError(f"Missing minutes column: {mp_col}")

    missing_stats = [c for c in cols if c not in df.columns]
    if missing_stats:
        raise KeyError(f"Missing stat columns: {missing_stats}")

    out = df.copy()
    mp_safe = out[mp_col].clip(lower=1)

    for c in cols:
        out[f"{c}_per_min"] = out[c] / mp_safe

    return out
