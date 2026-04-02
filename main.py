from flask import Flask, request
import requests
import os

TOKEN = os.getenv("8331918470:AAEpnz6rgY-AC3P6NuKyyeGiV06q0282YbQ")
URL = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

app = Flask(__name__)

@app.route("/")
def home():
    return "Bot Running 🚀"

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.get_json()

    if "message" in data:
        chat_id = data["message"]["chat"]["id"]
        text = data["message"].get("text", "")

        if text == "/start":
            msg = "🚀 Bot Working!"
        else:
            msg = "Message received ✅"

        requests.post(URL, json={
            "chat_id": chat_id,
            "text": msg
        })

    return "ok"

@app.before_first_request
def set_webhook():
    webhook_url = "https://tradingsunil-bot.onrender.com/webhook"
    requests.get(f"https://api.telegram.org/bot{TOKEN}/setWebhook?url={webhook_url}")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
