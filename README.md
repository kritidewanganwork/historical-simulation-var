# Historical Simulation Value at Risk (VaR)
Implementation of a Historical Simulation Value at Risk (VaR) framework in Python, including Expected Shortfall, portfolio P&amp;L estimation, backtesting analysis, and Basel Traffic Light classification.

## Overview
This project implements an end-to-end Historical Simulation Value at Risk (VaR) framework using Python.  
The model estimates portfolio risk using empirical return distributions and evaluates model performance through backtesting and Basel Traffic Light classification.

## Key Features
- Historical Simulation VaR (99%)
- Expected Shortfall (ES)
- Portfolio-level P&L computation
- VaR backtesting and breach analysis
- Basel Traffic Light regulatory classification
- Risk visualisation (time-series and distribution-based)

## Methodology
1. Load historical market price data
2. Compute log returns
3. Construct a portfolio using predefined weights
4. Generate daily P&L
5. Estimate VaR and ES using rolling historical windows
6. Perform backtesting to identify VaR breaches
7. Classify model performance using the Basel Traffic Light framework

## Project Structure
data/ - market price data
src/ - risk engine modules
notebooks/ - execution and analysis
requirements.txt - dependencies


## How to Run
1. Install dependencies:
pip install -r requirements.txt
2. Open the notebook
notebooks/run_model.ipynb
3. Run cells sequentially to:
- compute VaR & ES
- perform backtesting
- visualize breaches
- generate Basel classification

