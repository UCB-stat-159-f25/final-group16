import pandas as pd
import numpy as np

from utils import add_gamekey_and_win, add_per_minute_stats

def test_add_gamekey_and_win_basic():
    df = pd.DataFrame({
        "Data": ["2025-01-01", "2025-01-02"],
        "Tm": ["LAL", "BOS"],
        "Opp": ["GSW", "NYK"],
        "Res": ["W", "L"],
    })
    out = add_gamekey_and_win(df)

    assert out.loc[0, "Win"] == 1
    assert out.loc[1, "Win"] == 0
    assert out.loc[0, "GameKey"] == "2025-01-01_LAL_vs_GSW"
    assert "GameKey" in out.columns


def test_add_per_minute_stats_clips_zero_minutes():
    df = pd.DataFrame({
        "MP": [10.0, 0.0],
        "PTS": [20, 5],
        "TRB": [10, 2],
        "AST": [5, 1],
    })
    out = add_per_minute_stats(df)

    assert np.isclose(out.loc[0, "PTS_per_min"], 2.0)  # 20/10
    assert np.isclose(out.loc[1, "PTS_per_min"], 5.0)  # 5/1 because MP clipped to 1
