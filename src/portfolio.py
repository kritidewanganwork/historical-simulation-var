import pandas as pd

def compute_portfolio_returns(returns: pd.DataFrame, weights: dict) -> pd.Series:
    """
    Compute the portfolio value over time given return data and asset weights.
    """
    # Ensure weights sum to 1
    if not abs(weights.sum() - 1.0) < 1e-6:
        raise ValueError("Weights must sum to 1")

    returns = returns[weights.index]

    returns = returns @ weights

    return returns