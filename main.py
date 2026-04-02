from flask import Flask
import threading
import os
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

TOKEN = "8331918470:AAEpnz6rgY-AC3P6NuKyyeGiV06q0282YbQ"

# ===== TELEGRAM =====
def start(update, context):
    update.message.reply_text("🚀 Bot Working!")

def reply(update, context):
    update.message.reply_text("Message received ✅")

def run_bot():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text, reply))

    updater.start_polling()
    updater.idle()

# ===== FLASK =====
app = Flask(__name__)

@app.route("/")
def home():
    return "Bot Running 🚀"

def run_web():
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)

# ===== RUN BOTH =====
threading.Thread(target=run_web).start()
run_bot()
