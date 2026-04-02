from flask import Flask, request
from telegram import Bot, Update
import os

TOKEN = "8331918470:AAEpnz6rgY-AC3P6NuKyyeGiV06q0282YbQ"
bot = Bot(token=TOKEN)

app = Flask(__name__)

@app.route("/")
def home():
    return "Bot Running 🚀"

@app.route("/webhook", methods=["POST"])
def webhook():
    update = Update.de_json(request.get_json(force=True), bot)
    
    if update.message:
        text = update.message.text
        chat_id = update.message.chat_id
        
        if text == "/start":
            bot.send_message(chat_id=chat_id, text="🚀 Bot Working!")
        else:
            bot.send_message(chat_id=chat_id, text="Message received ✅")

    return "ok"

# set webhook automatically
@app.before_first_request
def set_webhook():
    bot.set_webhook(url="https://tradingsunil-bot.onrender.com/webhook")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
