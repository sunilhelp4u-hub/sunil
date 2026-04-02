import pandas as pd

def strategy(df):
    df['EMA9'] = df['close'].ewm(span=9).mean()
    df['EMA21'] = df['close'].ewm(span=21).mean()

    if df['EMA9'].iloc[-1] > df['EMA21'].iloc[-1]:
        return "BUY"
    elif df['EMA9'].iloc[-1] < df['EMA21'].iloc[-1]:
        return "SELL"
    return "HOLD"
