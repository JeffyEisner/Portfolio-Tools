def volume_filter(df, min_avg_volume=1000000) -> bool:
    """
    Check if average volume is above the specified threshold.
    """
    avg_volume = df["volume"].tail(20).mean()
    return avg_volume >= min_avg_volume


def momentum_filter(df, lookback=20) -> bool:
    """
    Check if the stock has positive momentum over the specified lookback period.
    """
    # Check if we have enough data
    if len(df) < lookback:
        print(f"Not enough data for momentum filter: {len(df)} rows, need {lookback}")
        return False

    recent_return = (df["close"].iloc[-1] / df["close"].iloc[-lookback] - 1) * 100
    return recent_return > 0


def volatility_filter(df, max_volatility=0.05) -> bool:
    """
    Check's if a stock is too volatile

    Returns:
        True if the stock's volatility is below the specified threshold
        False otherwise.
    """
    returns = df["close"].pct_change()
    volatility = returns.tail(20).std()
    return volatility < max_volatility


def rsi_filter(df, period=14, max_rsi=70) -> bool:
    """
    Checks if RSI inidicates that a stock is overbought
    """
    delta = df["close"].diff()
    gain = delta.where(delta > 0, 0)
    loss = -delta.where(delta < 0, 0)
    avg_gain = gain.rolling(window=period).mean()
    avg_loss = loss.rolling(window=period).mean()
    rs = avg_gain / avg_loss
    rsi = 100 - (100 / (1 + rs))
    return rsi.iloc[-1] < max_rsi


def trend_filter(df, window=200) -> bool:
    """
    Confirm stock is above long-term trend
    """
    sma = df["close"].rolling(window=window).mean()
    return df["close"].iloc[-1] > sma.iloc[-1]


def sma_crossover_filter(df, short_window=50, long_window=200) -> bool:
    """
    Calculate and validate if the short average exceeds teh long
    """
    # Calculate moving averages
    df["SMA_short"] = df["close"].rolling(window=short_window).mean()
    df["SMA_long"] = df["close"].rolling(window=long_window).mean()

    # Return Signals
    return df["SMA_short"].iloc[-1] > df["SMA_long"].iloc[-1]


def calculate_recent_performance(df, days=30):
    """
    Calculate percentage gain over last N days
    """
    # NOTE: Move to a calculations directory
    return ((df["close"].iloc[-1] / df["close"].iloc[-days]) - 1) * 100
