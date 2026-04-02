from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes, CommandHandler
from flask import Flask
import threading
import os

TOKEN = "8331918470:AAEpnz6rgY-AC3P6NuKyyeGiV06q0282YbQ  # ⚠️ new token use karna

# ===== TELEGRAM =====
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🚀 Trading Bot Active!")

async def reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Message received ✅")

# ===== FLASK =====
app = Flask(__name__)

@app.route("/")
def home():
    return "Bot is Running 🚀"

def run_web():
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)

# ===== BOT =====
def run_bot():
    app_bot = ApplicationBuilder().token(TOKEN).build()
    app_bot.add_handler(CommandHandler("start", start))
    app_bot.add_handler(MessageHandler(filters.TEXT, reply))
    app_bot.run_polling()

# ===== RUN BOTH =====
threading.Thread(target=run_web).start()
run_bot()
