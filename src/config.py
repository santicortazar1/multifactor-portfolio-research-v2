"""
## Centralized project configuration for the Multifactor Portfolio Research repository.

## Purpose

This module provides project-wide constants shared across notebooks and source
modules. Centralizing configuration improves consistency, reproducibility, and
maintainability by avoiding duplicated values throughout the codebase.

## Current Scope

- Project paths
- Project metadata
- Canonical data sources

## Notes

Analytical parameters (e.g., portfolio weights, transaction costs, or
performance metrics) do NOT belong here. They should remain in the modules
that implement the corresponding methodology.
"""

## Section I - Imports

from pathlib import Path


## Section II - Project Paths

PROJECT_ROOT = Path(__file__).resolve().parent.parent

DATA_DIR = PROJECT_ROOT / "data"

RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"

NOTEBOOKS_DIR = PROJECT_ROOT / "notebooks"

OUTPUTS_DIR = PROJECT_ROOT / "outputs"
FIGURES_DIR = OUTPUTS_DIR / "figures"
TABLES_DIR = OUTPUTS_DIR / "tables"
REPORTS_DIR = OUTPUTS_DIR / "reports"

SRC_DIR = PROJECT_ROOT / "src"


## Section III - Supported Data Sources (Draft)

# This section is reserved for canonical project data sources.
# Only repository-wide source identifiers belong here—not analytical parameters.
#
# Possible future additions:
# - Yahoo Finance
# - FRED
# - Kenneth French Data Library