import yfinance as yf


def get_price(ticker: str) -> float | None:
    try:
        t = yf.Ticker(ticker)
        return t.fast_info["last_price"]
    except Exception as e:
        print(f"YFinance error: {e}")
        return None
