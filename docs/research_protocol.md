# Research Protocol

> **Status:** Draft v0.1
>
> This document translates the research design into a computational protocol for the
> Multifactor Portfolio Research repository. It is intentionally concise and may
> evolve as the methodology is refined.

---

## 1. Research Identity

### Research Question

> How robust are strategic multifactor portfolio construction philosophies across
> macroeconomic environments after accounting for implementation policies?

### Core Research Idea

The study evaluates **strategic portfolio construction philosophies**, rather than
individual factors or isolated ETFs.

The central premise is that investment outcomes depend not only on factor exposure,
but also on how exposures are combined, implemented, and evaluated across changing
economic environments.

---

## 2. Conceptual Research Framework

The empirical framework evaluates portfolio robustness across three dimensions:

1. **Structural Robustness**
   - Portfolio construction philosophy
   - Strategic allocation
   - Portfolio governance
   - Rebalancing

2. **Conditional Robustness**
   - Performance across macroeconomic environments
   - Yield-curve-based regime classification
   - Risk and risk-adjusted performance

3. **Implementation Robustness**
   - Turnover
   - Transaction costs
   - Gross vs. net performance
   - Practical implementation assumptions

### Conceptual Flow

```text
Strategic Portfolio Construction Philosophy
                    │
                    ▼
          Transparent ETF Implementation
                    │
                    ▼
          Implementation Considerations
                    │
          ┌─────────┴─────────┐
          ▼                   ▼
   Unconditional          Conditional
    Performance            Performance
          │                   │
          └─────────┬─────────┘
                    ▼
          Robustness Evaluation

(UPDATE)

Investment Portfolio Extended Research — Research Protocol

Phase status

Phase II — Research Infrastructure: CLOSED

Phase III — Empirical Implementation: IN PROGRESS

III.1 — Empirical Specification: FROZEN

III.1 → III.2 gate: PASSED

This specification is the single methodological authority for empirical implementation. Code may expose frozen values through configuration, but must not silently reinterpret them. Any later amendment requires a documented methodological reason, an explicit protocol version change, and rerunning affected outputs.

III.1 — Frozen empirical specification

III.1.2A — Portfolio implementations

The unit of analysis is the portfolio-construction philosophy. All implementations are transparent, rule-based, specified ex ante, and maintain a strategic 60% equity / 40% fixed-income allocation. AGG is the fixed-income sleeve in every portfolio.

Philosophy

Empirical implementation

Market Beta

60% SPY / 40% AGG

Diversified Multifactor

20% MTUM / 20% USMV / 20% QUAL / 40% AGG

Concentrated Factor — Momentum

60% MTUM / 40% AGG

Concentrated Factor — Low Volatility

60% USMV / 40% AGG

Concentrated Factor — Quality

60% QUAL / 40% AGG

Core–Satellite

30% SPY / 10% MTUM / 10% USMV / 10% QUAL / 40% AGG

The investable universe is fixed to SPY, MTUM, USMV, QUAL, and AGG. Historical optimization, tactical factor timing, macro-triggered allocation, and ex-post weight selection are prohibited.

III.1.2B — Return and data conventions

Frequency: monthly.

Intended coverage: July 2013 through December 2024.

Price convention: last available trading observation in each calendar month.

Asset return: adjusted market-price total return,

$$R_{i,t}=\frac{P^{adj}{i,t}}{P^{adj}{i,t-1}}-1.$$

Adjusted prices must capture distributions and splits. Dividends are not added again.

ETF operating expenses are embedded in observed ETF returns and are not deducted again.

Transaction costs are modeled separately at portfolio level.

Taxes, integer-share constraints, residual cash caused by indivisibility, and synthetic pre-inception backfills are excluded.

Fractional weights are allowed.

The first valid return for a portfolio is the first month in which every required asset has a valid return.

Frozen missing-data rule

Validate the expected month-end observation and retry or corroborate the source when an observation is missing or anomalous.

Do not forward-fill prices, replace a missing return with zero, interpolate, or renormalize portfolio weights around a missing asset.

If a required asset return remains unavailable after investigation, that portfolio-month is missing.

Any cross-portfolio comparison uses the intersection of valid portfolio-months for the portfolios being compared. Portfolio-specific descriptive outputs may retain their own valid sample, but must disclose start date and observation count.

Unresolved systematic source gaps or a materially shortened comparison sample are data-engineering blockers requiring documented review; code must not invent an imputation rule.

III.1.2C — Rebalancing mechanics

Baseline rebalancing is quarterly at the last available trading observation of March, June, September, and December. Each portfolio is initialized at target weights. The initial establishment is excluded from recurring turnover.

For month $t$, gross portfolio return uses weights entering the month:

$$R^{gross}{p,t}=\sum_i w^{post}{i,t-1}R_{i,t}.$$

After month-$t$ asset returns, pre-rebalance weights are:

$$w^{pre}{i,t}=\frac{w^{post}{i,t-1}(1+R_{i,t})}{\sum_j w^{post}{j,t-1}(1+R{j,t})}.$$

At an active scheduled rebalance:

realize month-$t$ asset returns;

calculate gross portfolio return and drifted pre-rebalance weights;

calculate required trades, one-way turnover, and transaction cost;

restore strategic target weights; and

enter month $t+1$ at target weights.

In non-rebalance months, $w^{post}{i,t}=w^{pre}{i,t}$. At a rebalance, $w^{post}{i,t}=w^{target}{i}$. No terminal rebalance is performed solely to close the simulation.

Robustness schedules are frozen as follows:

Monthly: rebalance after every month-end return observation.

Quarterly baseline: rebalance after March, June, September, and December month-end return observations.

Annual: rebalance after the December month-end return observation.

Monthly rebalancing does not make turnover mechanically zero. The portfolio starts each month at target, drifts with that month's asset returns, and is then restored at month-end.

III.1.2D — Turnover and transaction costs

The turnover rule is frequency-agnostic. Turnover is generated at dates defined by the active rebalance schedule; quarterly is the baseline schedule.

One-way turnover at rebalance $t$ is:

$$TO_t=\frac{1}{2}\sum_i\left|w^{target}i-w^{pre}{i,t}\right|.$$

$TO_t=0$ on non-rebalance dates. Initial establishment and a terminal closing trade are excluded. Calendar-year turnover is the sum of observed one-way turnover within that year.

Transaction cost as a fraction of pre-trade portfolio wealth is:

$$TC_t=TO_t\times c,$$

where $c$ is 0.0005 for the 5 bps baseline, 0.0002 for the 2 bps low-cost scenario, and 0.0010 for the 10 bps high-cost scenario.

Costs are applied at the end of the same month in which the rebalance occurs, after that month's gross return and before the next holding period:

$$1+R^{net}{p,t}=(1+R^{gross}{p,t})(1-TC_t).$$

Gross and net wealth paths are therefore:

$$V^{gross}t=V^{gross}{t-1}(1+R^{gross}_{p,t}),$$

$$V^{net}t=V^{net}{t-1}(1+R^{gross}_{p,t})(1-TC_t).$$

Transaction costs reduce net portfolio wealth but do not alter normalized drifted weights: proportional portfolio-level cost is a scalar applied to total wealth, and post-rebalance weights are reset to target. This prevents costs from being deducted twice or from creating a separate weight path. ETF expenses remain embedded and are not deducted separately.

III.1.2E — Performance metrics

All metrics use monthly observations. Unless explicitly labeled gross, net performance is the principal implementation-aware result. Full-sample metrics are calculated separately for gross and net series, including path-dependent maximum drawdown.

Cumulative return: $\prod_{t=1}^{T}(1+R_t)-1$.

CAGR: $(V_T/V_0)^{12/T}-1$.

Annualized arithmetic return: $12,\bar{R}_m$.

Annualized volatility: $s(R_m)\sqrt{12}$, using monthly sample standard deviation.

Maximum drawdown: minimum of $V_t/\max_{s\le t}V_s-1$ on the relevant gross or net wealth path.

Sharpe ratio: monthly mean excess return divided by monthly sample standard deviation of excess returns, multiplied by $\sqrt{12}$.

Sortino ratio: monthly mean excess return divided by monthly downside deviation, multiplied by $\sqrt{12}$.

The risk-free proxy is FRED DGS3MO. Use the last available daily observation of each calendar month. Convert annualized decimal yield $y_t$ to a monthly equivalent:

$$R_{f,t}=(1+y_t)^{1/12}-1.$$

Monthly excess return is $X_t=R_{p,t}-R_{f,t}$.

Frozen Sortino convention

The minimum acceptable return is the contemporaneous monthly risk-free return. Equivalently, downside deviation is computed on monthly excess returns relative to zero:

$$DD_m=\sqrt{\frac{1}{T}\sum_{t=1}^{T}\min(X_t,0)^2}.$$

The denominator uses all observations in the evaluation window, not only negative-excess months. If downside deviation is zero, the Sortino ratio is undefined and must be reported as missing rather than infinite.

Rolling analysis uses a 36-month window, requires 36 valid monthly observations, and applies the same metric definitions as the full-sample analysis. CAGR remains a full-sample/path metric; rolling return reporting uses the explicitly defined rolling metrics rather than silently redefining CAGR.

III.1.2F — Macroeconomic-regime classification

Use FRED T10Y3M, reported in percentage points. For each month, take the last available daily observation as the month-end information state:

$$Regime_t=\begin{cases}Inverted,&T10Y3M_t<0\Normal,&T10Y3M_t\ge 0.\end{cases}$$

The state observed at month-end $t$ classifies portfolio return at $t+1$. The first portfolio return without a prior month-end regime is unclassified for regime analysis. Missing regime states are not forward-filled unless a separately documented source-validation rule is approved. Regimes are used only for conditional ex-post evaluation and never influence portfolio construction or rebalancing.

DGS3MO is aligned contemporaneously to return month $t$ for ex-post risk-adjusted evaluation; T10Y3M is lagged one month for regime classification. These distinct timing rules are intentional.

III.1.2G — Robustness specification

The baseline is quarterly rebalancing with 5 bps cost per unit of one-way turnover.

Primary robustness test: transaction costs at 2, 5, and 10 bps, holding the quarterly schedule and all other assumptions fixed.

Secondary robustness test: monthly, quarterly, and annual rebalancing, using the 5 bps cost assumption and holding all other assumptions fixed.

Core analysis, not a robustness test: gross versus net performance.

Held fixed: portfolio definitions, ETF universe, target weights, DGS3MO proxy, 36-month rolling window, and baseline T10Y3M regime rule.

No additional parameter search is permitted solely in response to observed results. Any extension requires an independently documented methodological, data-quality, literature, or external-review rationale.

Robustness is judged by directional stability of principal relative advantages versus the Market Beta benchmark across the baseline, cost scenarios, rebalancing schedules, and macroeconomic environments—not by peak performance under one specification.

III.1 final consistency audit

Resolved blockers

Turnover language generalized from quarterly-only to the active rebalance schedule.

Sortino MAR and downside-deviation denominator fixed.

Annualized arithmetic return fixed as 12 times mean monthly return.

Missing-data handling and comparison-sample alignment made deterministic.

Monthly and annual rebalance calendars fixed.

Gross/net weight mechanics and transaction-cost timing fixed.

Monthly-rebalance drift behavior made explicit.

Maximum drawdown explicitly calculated on separate gross and net wealth paths.

Audit conclusion

No remaining contradiction among A–G.

No unresolved implementation parameter that code is authorized to guess.

No look-ahead path in portfolio returns, rebalancing, risk-free evaluation, or regime assignment.

No transaction-cost or ETF-expense double counting.

Market, risk-free, regime, and rebalance observations share explicit month-end alignment rules.

The specification remains consistent with the research backbone: strategic rule-based 60/40 implementations; structural, conditional, and implementation robustness; quarterly baseline rebalancing; investable ETF histories; reproducibility; and implementation-aware gross/net analysis.

III.1 acceptance criteria — SATISFIED

Portfolio universe, implementations, and target weights are explicit.

Return field requirement, frequency, coverage, and missing-data rules are explicit.

Rebalancing sequence, calendars, drift, initialization, and terminal treatment are explicit.

Turnover formula, cost rates, timing, and gross/net compounding are explicit.

Every required performance metric has a deterministic definition.

Risk-free source, conversion, alignment, and Sortino MAR are explicit.

Macro source, threshold, lag, and non-use in construction are explicit.

Robustness dimensions and fixed parameters are bounded ex ante.

Independent implementations following this protocol should reconcile, subject only to validated source-data differences.

Decision: III.1 Empirical Specification is FROZEN. The III.1 → III.2 gate is PASSED. Coding and data acquisition remain out of scope until III.2 is approved.

III.2 — Configuration Layer

First concrete task

Define the configuration contract and populate one canonical baseline configuration before data acquisition or portfolio-engine code is written. The contract should expose only methodological choices that must be read by downstream modules, while formulas and invariants remain implementation logic.

Required configuration groups:

analysis period and monthly frequency;

ETF universe and portfolio target-weight mappings;

baseline and robustness rebalance schedules;

baseline and robustness transaction-cost rates;

market-data adjusted-total-return requirement;

FRED series identifiers and monthly aggregation conventions;

macro threshold and one-month assignment lag;

metric annualization factor, rolling window, Sortino MAR convention, and minimum observations;

missing-data policy identifiers; and

output labels for baseline and robustness scenarios.

Acceptance criteria for the first III.2 task

A single canonical configuration object/file represents every frozen parameter above; no value is duplicated across notebooks or modules.

Portfolio weights are numeric, non-negative, use only eligible tickers, and sum to 1 within a strict tolerance.

Baseline is unambiguous: quarterly schedule and 5 bps cost.

Robustness scenarios are exactly 2/5/10 bps and monthly/quarterly/annual, without an accidental Cartesian parameter search unless explicitly requested by the protocol.

Annual rebalancing resolves to December and quarterly to March/June/September/December.

FRED identifiers are exactly DGS3MO and T10Y3M; the regime lag is exactly one month.

Rolling window is 36 months and annualization factor is 12.

Configuration validation fails loudly for unknown tickers, invalid weights, unsupported frequencies, negative costs, missing required keys, or protocol-inconsistent values.

A human-readable configuration summary can be emitted for audit logs.

No market data is downloaded and no portfolio returns are calculated as part of this task.

