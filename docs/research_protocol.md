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