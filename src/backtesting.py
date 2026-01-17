import pandas as pd

def var_backtest(pnl: pd.Series, var: pd.Series) -> pd.DataFrame:
    """
    Perform VaR backtesting by comparing actual P&L with VaR estimates.
    """
    data = pd.concat([pnl,var], axis=1).dropna()
    data.columns = ['P&L', 'VaR']

    data['Breach'] = data['P&L'] < -data['VaR']
    breach_count = data['Breach'].sum()
    total_count = len(data)    
    breach_ratio = breach_count / total_count

    summary = pd.DataFrame({
        "Total Observations": [total_count],
        "Number of Breaches": [breach_count],
        "Breach Ratio": [breach_ratio]
    })

    return summary,data