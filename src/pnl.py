import pandas as pd

def calculate_pnl(portfolio_returns: pd.Series, portfolio_value: float) -> pd.Series:
    """
    Convert portfolio returns into monetary profit and loss (P&L).
    
    """
    pnl = portfolio_returns * portfolio_value

    return pnl