import pandas as pd
import numpy as np

def historical_simulation_risk(pnl: pd.Series, window: int = 250, confidence_level: float = 0.95) -> pd.DataFrame:
    """
    Calculate Historical Simulation Value at Risk (VaR) and Expected Shortfall (ES).
    """
    var_list = []
    es_list = []

    for i in range(window, len(pnl)):
        hist = pnl.iloc[i-window:i]
        sorted_pnl = np.sort(hist.values)
        var_index = int((1 - confidence_level) * window)
        var_value = sorted_pnl[var_index]
        es_value = sorted_pnl[:var_index+1].mean()
        var_list.append(-var_value)  # Convention: VaR is reported as a positive number
        es_list.append(-es_value)    # Convention: ES is reported as a positive number
    
    index = pnl.index[window:]
    # var = (pnl.shift(1).rolling(window).apply(lambda x: np.percentile(x, (1 - confidence_level) * 100), raw=True))

    return pd.DataFrame({'VaR': var_list, 'ES': es_list}, index=index)