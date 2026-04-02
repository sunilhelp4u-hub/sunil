from flask import Flask
import threading

app = Flask(__name__)

@app.route("/")
def home():
    return "🚀 Trading Bot is Running!"

def run_web():
    app.run(host="0.0.0.0", port=10000)

# start web server in thread
threading.Thread(target=run_web).start()
