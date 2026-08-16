"""
Canonical portfolio definitions for the empirical research.

This module contains the eligible ETF universe, frozen portfolio target
weights, and validation rules approved under III.1 of the research protocol.

Portfolio calculations, rebalancing, turnover, and transaction-cost logic do
not belong in this module.
"""

# Section I — Imports

from dataclasses import dataclass


# Section II — Portfolio Types

@dataclass(frozen=True)
class Holding:
    ticker: str
    target_weight: float


@dataclass(frozen=True)
class PortfolioConfig:
    portfolio_id: str
    philosophy: str
    holdings: tuple[Holding, ...]


# Section III — Eligible ETF Universe

ELIGIBLE_ETFS: tuple[str, ...] = (
    "SPY",
    "MTUM",
    "USMV",
    "QUAL",
    "AGG",
)


# Section IV — Portfolio Definitions

PORTFOLIOS: tuple[PortfolioConfig, ...] = (
    PortfolioConfig(
        portfolio_id="market_beta",
        philosophy="Market Beta",
        holdings=(
            Holding("SPY", 0.60),
            Holding("AGG", 0.40),
        ),
    ),
    PortfolioConfig(
        portfolio_id="diversified_multifactor",
        philosophy="Diversified Multifactor",
        holdings=(
            Holding("MTUM", 0.20),
            Holding("USMV", 0.20),
            Holding("QUAL", 0.20),
            Holding("AGG", 0.40),
        ),
    ),
    PortfolioConfig(
        portfolio_id="concentrated_momentum",
        philosophy="Concentrated Factor — Momentum",
        holdings=(
            Holding("MTUM", 0.60),
            Holding("AGG", 0.40),
        ),
    ),
    PortfolioConfig(
        portfolio_id="concentrated_low_volatility",
        philosophy="Concentrated Factor — Low Volatility",
        holdings=(
            Holding("USMV", 0.60),
            Holding("AGG", 0.40),
        ),
    ),
    PortfolioConfig(
        portfolio_id="concentrated_quality",
        philosophy="Concentrated Factor — Quality",
        holdings=(
            Holding("QUAL", 0.60),
            Holding("AGG", 0.40),
        ),
    ),
    PortfolioConfig(
        portfolio_id="core_satellite",
        philosophy="Core–Satellite",
        holdings=(
            Holding("SPY", 0.30),
            Holding("MTUM", 0.10),
            Holding("USMV", 0.10),
            Holding("QUAL", 0.10),
            Holding("AGG", 0.40),
        ),
    ),
)


# Section V — Portfolio Validation

WEIGHT_SUM_TOLERANCE = 1e-12


def validate_portfolios(
    portfolios: tuple[PortfolioConfig, ...] = PORTFOLIOS,
    eligible_etfs: tuple[str, ...] = ELIGIBLE_ETFS,
) -> None:
    """Validate portfolio identities, holdings, and target weights."""

    if not portfolios:
        raise ValueError("At least one portfolio must be configured.")

    if len(eligible_etfs) != len(set(eligible_etfs)):
        raise ValueError("ELIGIBLE_ETFS contains duplicate tickers.")

    portfolio_ids = [portfolio.portfolio_id for portfolio in portfolios]

    if len(portfolio_ids) != len(set(portfolio_ids)):
        raise ValueError("Portfolio IDs must be unique.")

    eligible_set = set(eligible_etfs)

    for portfolio in portfolios:
        if not portfolio.portfolio_id:
            raise ValueError("Every portfolio must have a portfolio_id.")

        if not portfolio.philosophy:
            raise ValueError(
                f"Portfolio {portfolio.portfolio_id!r} has no philosophy label."
            )

        if not portfolio.holdings:
            raise ValueError(
                f"Portfolio {portfolio.portfolio_id!r} has no holdings."
            )

        tickers = [holding.ticker for holding in portfolio.holdings]

        if len(tickers) != len(set(tickers)):
            raise ValueError(
                f"Portfolio {portfolio.portfolio_id!r} contains duplicate tickers."
            )

        unknown_tickers = set(tickers) - eligible_set

        if unknown_tickers:
            raise ValueError(
                f"Portfolio {portfolio.portfolio_id!r} contains unknown tickers: "
                f"{sorted(unknown_tickers)}."
            )

        for holding in portfolio.holdings:
            if holding.target_weight < 0:
                raise ValueError(
                    f"Portfolio {portfolio.portfolio_id!r} contains a negative "
                    f"weight for {holding.ticker}."
                )

        total_weight = sum(
            holding.target_weight for holding in portfolio.holdings
        )

        if abs(total_weight - 1.0) > WEIGHT_SUM_TOLERANCE:
            raise ValueError(
                f"Portfolio {portfolio.portfolio_id!r} weights sum to "
                f"{total_weight:.12f}, not 1.0."
            )


validate_portfolios()