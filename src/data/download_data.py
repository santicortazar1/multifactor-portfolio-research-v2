"""
Yahoo Finance market-data acquisition for the empirical research.

This module retrieves raw daily market observations for the canonical ETF
universe defined in src/portfolio/portfolio_definitions.py.

The acquisition window includes one calendar month before the configured
analysis start date so that the first potentially valid monthly return can be
constructed downstream.

Monthly transformation, return calculation, missing-data treatment, portfolio
construction, and analytical calculations do not belong in this module.
"""

# Section I — Imports

from datetime import date, timedelta

import pandas as pd
import yfinance as yf

from src.config import ANALYSIS_CONFIG, RAW_MARKET_DATA_FILE
from src.portfolio.portfolio_definitions import ELIGIBLE_ETFS


# Section II — Acquisition-Window Helpers

def get_market_data_start_date() -> date:
    """
    Return the beginning of the calendar month preceding the analysis start.

    The additional month supplies the prior month-end observation required
    to calculate the first potentially valid monthly return.
    """

    analysis_month_start = ANALYSIS_CONFIG.start_date.replace(day=1)
    previous_month_end = analysis_month_start - timedelta(days=1)

    return previous_month_end.replace(day=1)


def get_market_data_end_date() -> date:
    """
    Return the exclusive Yahoo Finance end date.

    yfinance treats the end parameter as exclusive, so one day is added to
    the configured inclusive analysis end date.
    """

    return ANALYSIS_CONFIG.end_date + timedelta(days=1)


# Section III — Market Data Acquisition

def download_market_data(
    tickers: tuple[str, ...] = ELIGIBLE_ETFS,
) -> pd.DataFrame:
    """
    Download raw daily Yahoo Finance observations for the canonical ETF universe.

    Prices are requested with automatic OHLC adjustment enabled so that the
    returned price representation reflects Yahoo Finance adjustments.

    Source-level NaN rows are preserved for downstream validation.

    No monthly transformation, return calculation, imputation, automatic
    repair, or portfolio-level calculation is performed here.
    """

    if not tickers:
        raise ValueError("At least one ticker must be supplied.")

    data = yf.download(
        tickers=list(tickers),
        start=get_market_data_start_date(),
        end=get_market_data_end_date(),
        interval="1d",
        auto_adjust=True,
        actions=True,
        repair=False,
        keepna=True,
        progress=False,
        threads=False,
        group_by="ticker",
        multi_level_index=True,
    )

    if data is None or data.empty:
        raise RuntimeError(
            "Yahoo Finance returned no market data."
        )

    return data


# Section IV — Raw Market-Data Persistence

def save_raw_market_data(
    data: pd.DataFrame,
) -> None:
    """
    Persist raw Yahoo Finance market data without analytical transformation.

    The persisted representation must preserve the acquisition structure,
    source-level missing values, dates, ticker identities, and corporate-action
    fields required for downstream validation and processing.
    """

    if data is None or data.empty:
        raise ValueError(
            "Cannot persist empty market data."
        )

    RAW_MARKET_DATA_FILE.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    data.to_parquet(
        RAW_MARKET_DATA_FILE,
        engine="pyarrow",
        index=True,
    )