import yfinance as yf

def fetch_stock_data(ticker, start_date, end_date):
    """Fetch historical stock data for a given ticker."""
    stock = yf.Ticker(ticker)
    data = stock.history(start=start_date, end=end_date)
    return data
