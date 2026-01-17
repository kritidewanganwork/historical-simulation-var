import pandas as pd

def load_data(file_path: str) -> pd.DataFrame:

    df = pd.read_csv(file_path, parse_dates=["Date"])
    df.sort_values("Date", inplace=True)
    df.set_index("Date", inplace=True)

    if df.isnull().sum().sum() > 0:
        raise ValueError("Missing values detected in price data")
    if df.shape[1] < 2:
        raise ValueError("Insufficient instruments for portfolio risk")

    return df
