"""
Persisted research-data loading utilities.

This module loads raw and processed datasets from project storage.

Loading functions should not perform hidden analytical transformations,
missing-data treatment, portfolio construction, or analytical calculations.
"""

# Section I — Imports

import pandas as pd

from src.config import (
    RAW_MACRO_DATA_FILE,
    RAW_MARKET_DATA_FILE,
)


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


# Section III — Raw Macroeconomic Data

def load_raw_macro_data() -> pd.DataFrame:
    """
    Load the persisted raw FRED macroeconomic-data acquisition.
    """

    if not RAW_MACRO_DATA_FILE.exists():
        raise FileNotFoundError(
            f"Raw macro-data file not found: {RAW_MACRO_DATA_FILE}"
        )

    return pd.read_parquet(
        RAW_MACRO_DATA_FILE,
        engine="pyarrow",
    )