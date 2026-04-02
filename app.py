from flask import Flask, render_template
import config

app = Flask(__name__)

@app.route("/")
def dashboard():
    return render_template("dashboard.html", status=config.BOT_RUNNING)

app.run(debug=True)
