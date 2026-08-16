# src/portfolio/implementation_config.py

"""
Canonical implementation-policy configuration for the empirical research.

This module contains the frozen rebalancing, turnover, and transaction-cost
parameters approved under III.1 of the research protocol.

Portfolio calculations, weight drift, rebalance execution, turnover formulas,
transaction-cost formulas, and gross/net return calculations do not belong
in this module.
"""

# Section I — Imports

from dataclasses import dataclass
from typing import Literal


# Section II — Type Definitions

RebalancingFrequency = Literal["monthly", "quarterly", "annual"]
TurnoverConvention = Literal["one_way"]


@dataclass(frozen=True)
class RebalancingConfig:
    baseline_frequency: RebalancingFrequency
    supported_frequencies: tuple[RebalancingFrequency, ...]
    monthly_rebalance_months: tuple[int, ...]
    quarterly_rebalance_months: tuple[int, ...]
    annual_rebalance_months: tuple[int, ...]


@dataclass(frozen=True)
class TransactionCostConfig:
    baseline_bps: int
    cost_scenarios_bps: tuple[int, ...]


@dataclass(frozen=True)
class TurnoverConfig:
    convention: TurnoverConvention
    include_initial_establishment: bool
    include_terminal_liquidation: bool


# Section III — Rebalancing Configuration

REBALANCING_CONFIG = RebalancingConfig(
    baseline_frequency="quarterly",
    supported_frequencies=(
        "monthly",
        "quarterly",
        "annual",
    ),
    monthly_rebalance_months=tuple(range(1, 13)),
    quarterly_rebalance_months=(3, 6, 9, 12),
    annual_rebalance_months=(12,),
)


# Section IV — Transaction-Cost Configuration

TRANSACTION_COST_CONFIG = TransactionCostConfig(
    baseline_bps=5,
    cost_scenarios_bps=(2, 5, 10),
)


# Section V — Turnover Configuration

TURNOVER_CONFIG = TurnoverConfig(
    convention="one_way",
    include_initial_establishment=False,
    include_terminal_liquidation=False,
)


# Section VI — Configuration Validation

def validate_rebalancing_config(config: RebalancingConfig) -> None:
    """Validate the frozen rebalancing-policy configuration."""

    if config.baseline_frequency != "quarterly":
        raise ValueError(
            "The frozen empirical specification requires quarterly "
            "baseline rebalancing."
        )

    if config.supported_frequencies != (
        "monthly",
        "quarterly",
        "annual",
    ):
        raise ValueError(
            "Supported rebalancing frequencies must be monthly, quarterly, "
            "and annual."
        )

    if config.monthly_rebalance_months != tuple(range(1, 13)):
        raise ValueError(
            "Monthly rebalancing must include every calendar month."
        )

    if config.quarterly_rebalance_months != (3, 6, 9, 12):
        raise ValueError(
            "Quarterly rebalancing must occur after March, June, September, "
            "and December."
        )

    if config.annual_rebalance_months != (12,):
        raise ValueError(
            "Annual rebalancing must occur after December."
        )


def validate_transaction_cost_config(
    config: TransactionCostConfig,
) -> None:
    """Validate the frozen transaction-cost configuration."""

    if config.baseline_bps != 5:
        raise ValueError(
            "The frozen baseline transaction cost is 5 bps."
        )

    if config.cost_scenarios_bps != (2, 5, 10):
        raise ValueError(
            "Transaction-cost scenarios must be exactly 2, 5, and 10 bps."
        )

    if any(cost < 0 for cost in config.cost_scenarios_bps):
        raise ValueError(
            "Transaction-cost assumptions cannot be negative."
        )


def validate_turnover_config(config: TurnoverConfig) -> None:
    """Validate the frozen turnover-policy configuration."""

    if config.convention != "one_way":
        raise ValueError(
            "The frozen turnover convention is one-way turnover."
        )

    if config.include_initial_establishment:
        raise ValueError(
            "Initial portfolio establishment must be excluded from turnover."
        )

    if config.include_terminal_liquidation:
        raise ValueError(
            "Terminal liquidation must be excluded from turnover."
        )


def validate_implementation_configuration() -> None:
    """Run all implementation-policy configuration checks."""

    validate_rebalancing_config(REBALANCING_CONFIG)
    validate_transaction_cost_config(TRANSACTION_COST_CONFIG)
    validate_turnover_config(TURNOVER_CONFIG)


validate_implementation_configuration()