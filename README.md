# Multifactor Portfolio Research

> A reproducible quantitative finance research project evaluating whether alternative strategic portfolio construction philosophies improve the robustness of a traditional 60/40 portfolio under realistic implementation frictions and changing macro-financial environments.

---

## Overview

Strategic asset allocation remains one of the most influential drivers of long-term portfolio performance. While decades of academic research have documented the existence of systematic factor premia, comparatively less attention has been devoted to evaluating how different portfolio construction philosophies perform once realistic implementation constraints are introduced.

This project develops a transparent and reproducible evaluation framework for comparing strategic portfolio construction philosophies implemented through publicly investable exchange-traded funds (ETFs). Rather than reconstructing historical factor returns or optimizing portfolios in-sample, the framework evaluates practical investment strategies under institutional governance principles, implementation frictions, and varying macro-financial environments.

The project is implemented entirely in Python and is designed to be fully reproducible from data acquisition to publication-quality research outputs.

---

## Research Question

> To what extent do alternative strategic portfolio construction philosophies exhibit greater robustness than a traditional 60/40 allocation across macro-financial environments after accounting for realistic implementation frictions?

---

## Research Contribution

This study integrates four complementary research streams into a unified evaluation framework:

- Strategic Portfolio Construction
- Multifactor Portfolio Implementation
- Implementation-Aware Investing
- Macro-Regime Portfolio Evaluation

Unlike many previous studies, the objective is **not** to identify an optimal portfolio or maximize historical performance.

Instead, the project evaluates whether transparent and investable portfolio construction philosophies remain structurally robust under realistic implementation assumptions.

---

## Research Philosophy

The project follows several guiding principles throughout both the empirical analysis and the software implementation.

- Transparency over complexity
- Reproducibility over customization
- Engineering over optimization
- Robustness over in-sample maximization
- Investability over theoretical perfection

Consequently, the unit of analysis is **the strategic portfolio construction philosophy**, rather than individual securities or isolated factor exposures.

---

## Portfolio Construction Philosophies

The research compares multiple strategic approaches to long-term portfolio construction, including:

- Traditional Market Beta
- Diversified Multifactor
- Concentrated Multifactor
- Core-Satellite

Each philosophy is implemented using transparent, investable ETF allocations governed by predefined strategic allocation rules.

---

## Methodology

The empirical framework evaluates portfolios across three complementary dimensions of robustness.

### Structural Robustness

- Strategic portfolio construction
- Portfolio governance
- Quarterly rebalancing
- Long-term performance

### Conditional Robustness

- Performance across macroeconomic environments
- Regime-based analysis
- Rolling performance evaluation

### Implementation Robustness

- Portfolio turnover
- Transaction costs
- Implementation drag
- Net versus gross performance

---

## Repository Structure

```
multifactor-portfolio-research/

│
├── README.md
├── requirements.txt
├── .gitignore
│
├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
│   ├── 00_research_environment.ipynb
│   ├── 01_data_engineering.ipynb
│   ├── 02_portfolio_implementation.ipynb
│   ├── 03_performance_evaluation.ipynb
│   ├── 04_robustness_assessment.ipynb
│   └── 05_research_outputs.ipynb
│
├── src/
│   ├── config.py
│   ├── data.py
│   ├── portfolios.py
│   ├── metrics.py
│   ├── robustness.py
│   └── visualization.py
│
├── figures/
├── tables/
└── paper/
```

---

## Computational Pipeline

The research pipeline follows five sequential stages.

### Stage I — Research Environment

- Configure reproducible Python environment
- Validate dependencies
- Initialize project configuration

### Stage II — Data Engineering

- Acquire ETF market data
- Acquire macroeconomic data
- Clean, align, and validate datasets

### Stage III — Portfolio Implementation

- Construct strategic portfolio implementations
- Apply quarterly rebalancing
- Compute turnover
- Apply implementation assumptions

### Stage IV — Performance Evaluation

- Evaluate return performance
- Compute risk metrics
- Evaluate macro-regime performance
- Compare gross and net performance

### Stage V — Research Outputs

- Generate publication-quality figures
- Generate summary tables
- Export reproducible research outputs

---

## Technologies

- Python
- Pandas
- NumPy
- Matplotlib
- yfinance
- pandas-datareader
- Jupyter Notebook

---

## Project Scope

This repository contains the complete computational workflow supporting an independent quantitative finance research project, including data engineering, portfolio implementation, performance evaluation, and reproducible research outputs.

---

## Reproducibility

The project emphasizes complete computational reproducibility.

All analyses are performed through sequential Jupyter notebooks with modular Python utilities contained in the `src/` directory. Intermediate datasets, figures, and tables are generated directly from source data using deterministic workflows whenever possible.

---

## Future Development

Potential future extensions include:

- Additional macroeconomic regime specifications
- Alternative implementation cost assumptions
- International equity universes

---

## References

The methodological framework builds upon contributions from the literature on:

- Modern Portfolio Theory
- Capital Asset Pricing
- Multifactor Asset Pricing
- Strategic Asset Allocation
- Portfolio Construction
- Downside Risk
- Implementation Frictions
- Macroeconomic Risk Premia

A complete bibliography will accompany the research manuscript.

---

## License

This repository is released for research and educational purposes.

A formal open-source license will be selected prior to public release.