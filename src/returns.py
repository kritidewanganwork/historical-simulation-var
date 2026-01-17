import numpy as np
import pandas as pd

def calculate_log_returns(prices: pd.DataFrame, return_type: str = "log") -> pd.DataFrame:
    """
    Calculate log returns from price data.
    """
    returns = np.log(prices / prices.shift(1))

    returns = returns.dropna()

    return returns
