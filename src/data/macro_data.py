"""
FRED macroeconomic data acquisition and raw persistence utilities.

This module owns retrieval and persistence of raw FRED observations.
It must not perform downstream monthly transformation, regime classification,
risk-free conversion, portfolio merging, or analytical calculations.
"""

from dateutil.relativedelta import relativedelta
import pandas as pd
from pandas_datareader import data as web

from src.config import (
    ANALYSIS_CONFIG,
    MACRO_REGIME_SERIES,
    RAW_MACRO_DATA_FILE,
    RAW_MARKET_DATA_FILE,
    RISK_FREE_SERIES,
)


def get_fred_acquisition_window():
    """
    Derive the raw FRED acquisition window from the frozen analysis period.

    One calendar month of pre-sample history is required so that the
    prior month-end T10Y3M state can later classify the first analytical
    return month.
    """

    start_date = ANALYSIS_CONFIG.start_date - relativedelta(months=1)
    end_date = ANALYSIS_CONFIG.end_date

    return start_date, end_date


def download_macro_data() -> pd.DataFrame:
    """
    Download raw DGS3MO and T10Y3M observations from FRED.
    """

    start_date, end_date = get_fred_acquisition_window()

    series = [
        RISK_FREE_SERIES,
        MACRO_REGIME_SERIES,
    ]

    macro_data = web.DataReader(
        series,
        "fred",
        start_date,
        end_date,
    )

    if macro_data.empty:
        raise ValueError("FRED macro-data download returned an empty dataset.")

    missing_series = [
        series_id for series_id in series
        if series_id not in macro_data.columns
    ]

    if missing_series:
        raise ValueError(
            f"FRED response is missing required series: {missing_series}"
        )

    return macro_data


def save_raw_macro_data(macro_data: pd.DataFrame) -> None:
    """
    Persist raw FRED observations without analytical transformation.
    """

    RAW_MACRO_DATA_FILE.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    macro_data.to_parquet(
        RAW_MACRO_DATA_FILE,
        engine="pyarrow",
    )


