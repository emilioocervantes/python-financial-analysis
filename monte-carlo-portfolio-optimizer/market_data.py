import yfinance as yf
import pandas as pd


def download_prices(tickers, start_date):
    data = yf.download(
        tickers,
        start=start_date,
        auto_adjust=True,
        progress=False,
    )

    prices = data["Close"]

    return prices
