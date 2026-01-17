import yfinance as yf

tickers = ["AAPL", "MSFT", "MS", "GS", "AMZN", "GOOGL", "META", "TSLA", "JPM"]

data = yf.download(
    tickers,
    start="2020-01-01",
    end="2025-12-31",
    auto_adjust=True
)["Close"]

data.reset_index().to_csv("data/prices.csv", index=False)

print("prices.csv created successfully")