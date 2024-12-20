import pandas as pd

# def calculate_moving_average(data, window_size=20):
#     """Calculate moving averages for the given data."""
#     data[f'MA_{window_size}'] = data['Close'].rolling(window=window_size).mean()
#     return data
def calculate_moving_average(data, window_size=20):
    """Calculate moving averages for the given data."""
    data[f'MA_{window_size}'] = data['Close'].rolling(window=window_size).mean()
    data = data.fillna(value=0)  # NaN 값을 0으로 변환
    return data
