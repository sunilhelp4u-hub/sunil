import time
import pandas as pd
from strategy import strategy
from telegram_bot import send
from config import *

while True:
    if not BOT_RUNNING:
        time.sleep(5)
        continue

    df = pd.DataFrame({"close": [100,101,102,103,104,105,106]})
    signal = strategy(df)

    if signal != "HOLD":
        send(f"Signal: {signal}")

    time.sleep(60)
