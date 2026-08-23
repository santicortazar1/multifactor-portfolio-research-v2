"""
Centralized project configuration for the Multifactor Portfolio Research
repository.

This module is the single source of truth for repository-wide infrastructure,
canonical data-source identifiers, and global analysis parameters approved in
the research protocol.

Domain-specific configuration belongs in its corresponding source module.
For example, portfolio definitions and portfolio-specific validation belong in
src/portfolio/portfolio_definitions.py.

Analytical formulas and portfolio-simulation logic do not belong here.
Methodological parameters must not be duplicated or silently overridden in
notebooks or downstream modules.
"""

# Section I — Imports

from dataclasses import dataclass
from datetime import date
from pathlib import Path
from typing import Literal


# Section II — Project Paths

PROJECT_ROOT = Path(__file__).resolve().parent.parent

DATA_DIR = PROJECT_ROOT / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"

RAW_MARKET_DATA_FILE = RAW_DATA_DIR / "yahoo_market_data.parquet"
RAW_MACRO_DATA_FILE = RAW_DATA_DIR / "fred_macro_data.parquet"

NOTEBOOKS_DIR = PROJECT_ROOT / "notebooks"

OUTPUTS_DIR = PROJECT_ROOT / "outputs"
FIGURES_DIR = OUTPUTS_DIR / "figures"
TABLES_DIR = OUTPUTS_DIR / "tables"
REPORTS_DIR = OUTPUTS_DIR / "reports"

SRC_DIR = PROJECT_ROOT / "src"


# Section III — Canonical Data Sources

MARKET_DATA_PROVIDER = "Yahoo Finance"
MARKET_DATA_FREQUENCY = "monthly"
MARKET_PRICE_REQUIREMENT = "adjusted_total_return"
MONTHLY_OBSERVATION_RULE = "last_available_trading_observation"

FRED_PROVIDER = "Federal Reserve Economic Data"
RISK_FREE_SERIES = "DGS3MO"
MACRO_REGIME_SERIES = "T10Y3M"
FRED_MONTHLY_OBSERVATION_RULE = "last_available_observation"


# Section IV — Type Definitions

@dataclass(frozen=True)
class AnalysisConfig:
    start_date: date
    end_date: date
    base_frequency: Literal["monthly"]


# Section V — Analysis Configuration

ANALYSIS_CONFIG = AnalysisConfig(
    start_date=date(2013, 7, 1),
    end_date=date(2024, 12, 31),
    base_frequency="monthly",
)


# Section VI — Configuration Validation

def validate_analysis_config(config: AnalysisConfig) -> None:
    """Validate the frozen analysis-period configuration."""

    if config.start_date >= config.end_date:
        raise ValueError(
            "Analysis start_date must be earlier than end_date."
        )

    if config.base_frequency != "monthly":
        raise ValueError(
            "The frozen empirical specification requires monthly frequency."
        )


def validate_configuration() -> None:
    """Run all project-level configuration checks."""

    validate_analysis_config(ANALYSIS_CONFIG)


validate_configuration()