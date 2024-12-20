import matplotlib.pyplot as plt

def plot_stock_data(data, ticker):
    """Plot stock closing prices and moving averages."""
    plt.figure(figsize=(12, 6))
    plt.plot(data.index, data['Close'], label='Close Price')
    for col in data.columns:
        if 'MA_' in col:
            plt.plot(data.index, data[col], label=col)
    plt.title(f"{ticker} Stock Data")
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.legend()
    plt.grid()
    plt.show()
