from flask import Flask, request
import requests
import os

TOKEN = os.getenv("8331918470:AAEpnz6rgY-AC3P6NuKyyeGiV06q0282YbQ")

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

        requests.post(
            f"https://api.telegram.org/bot{TOKEN}/sendMessage",
            json={"chat_id": chat_id, "text": msg}
        )

    return "ok"

@app.route("/setwebhook")
def set_webhook():
    url = "https://tradingsunil-bot.onrender.com/webhook"
    return requests.get(
        f"https://api.telegram.org/bot{TOKEN}/setWebhook?url={url}"
    ).text

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
