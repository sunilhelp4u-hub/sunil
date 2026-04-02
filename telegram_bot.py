import requests
from config import *

def send(msg):
    url = f"https://api.telegram.org/bot{8331918470:AAEpnz6rgY-AC3P6NuKyyeGiV06q0282YbQ}/sendMessage"
    requests.post(url, data={"chat_id": CHAT_ID, "text": msg})
