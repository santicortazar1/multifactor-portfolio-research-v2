"""
Raw research-data validation utilities.

Validation functions detect and report data-quality issues.
They must not perform hidden repairs, imputations, analytical transformations,
portfolio calculations, or macro-regime classification.
"""

import pandas as pd
from dateutil.relativedelta import relativedelta

from src.config import (
    ANALYSIS_CONFIG,
    MACRO_REGIME_SERIES,
    RISK_FREE_SERIES,
)


def validate_raw_macro_data(macro_data: pd.DataFrame) -> None:
    """
    Validate the raw FRED macroeconomic dataset against the acquisition contract.
    """

    expected_columns = {
        RISK_FREE_SERIES,
        MACRO_REGIME_SERIES,
    }

    if macro_data.empty:
        raise ValueError("Raw FRED macro-data dataset is empty.")

    if not isinstance(macro_data.index, pd.DatetimeIndex):
        raise TypeError(
            "Raw FRED macro-data index must be a pandas DatetimeIndex."
        )

    missing_columns = expected_columns.difference(macro_data.columns)

    if missing_columns:
        raise ValueError(
            f"Raw FRED macro-data is missing required series: "
            f"{sorted(missing_columns)}"
        )

    if not macro_data.index.is_monotonic_increasing:
        raise ValueError(
            "Raw FRED macro-data dates are not monotonically increasing."
        )

    if macro_data.index.has_duplicates:
        raise ValueError(
            "Raw FRED macro-data contains duplicate dates."
        )

    expected_start_month = pd.Period(
        ANALYSIS_CONFIG.start_date - relativedelta(months=1),
        freq="M",
    )

    expected_end_month = pd.Period(
        ANALYSIS_CONFIG.end_date,
        freq="M",
    )

    actual_start_month = macro_data.index.min().to_period("M")
    actual_end_month = macro_data.index.max().to_period("M")

    if actual_start_month > expected_start_month:
        raise ValueError(
            f"Raw FRED macro-data begins too late: "
            f"{actual_start_month} > required {expected_start_month}"
        )

    if actual_end_month < expected_end_month:
        raise ValueError(
            f"Raw FRED macro-data ends too early: "
            f"{actual_end_month} < required {expected_end_month}"
        )

    null_counts = macro_data.isna().sum()

    print("Raw FRED structural validation PASS")
    print()
    print("Coverage:")
    print(f"  Required start month: {expected_start_month}")
    print(f"  Actual start month:   {actual_start_month}")
    print(f"  Required end month:   {expected_end_month}")
    print(f"  Actual end month:     {actual_end_month}")
    print()
    print("Missing observations:")
    print(null_counts)