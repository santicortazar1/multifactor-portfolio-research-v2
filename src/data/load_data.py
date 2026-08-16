"""
Persisted research-data loading utilities.

This module loads raw and processed datasets from project storage.

Loading functions should not perform hidden analytical transformations,
missing-data treatment, portfolio construction, or analytical calculations.
"""

# Section I — Imports

import pandas as pd

from src.config import RAW_MARKET_DATA_FILE


# Section II — Raw Market Data

def load_raw_market_data() -> pd.DataFrame:
    """
    Load the persisted raw Yahoo Finance market-data acquisition.
    """

    if not RAW_MARKET_DATA_FILE.exists():
        raise FileNotFoundError(
            f"Raw market-data file not found: {RAW_MARKET_DATA_FILE}"
        )

    return pd.read_parquet(
        RAW_MARKET_DATA_FILE,
        engine="pyarrow",
    )


save_raw_market_data(market_data)