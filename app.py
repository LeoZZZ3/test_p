import os
from flask import Flask
import datetime

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return "Salut", 200, {"Content-Type": "text/plain"}

@app.route("/actual_hours", methods=["GET"])
def actual_hours():
    current_hour = datetime.datetime.now().time().strftime("%H:%M:%S")
    return {"current_hour": current_hour}, 200, {"Content-Type": "application/json"}

@app.route("/actual_day", methods=["GET"])
def actual_day():
    current_day = datetime.datetime.now().strftime("%Y-%m-%d")
    return {"current_day": current_day}, 200, {"Content-Type": "application/json"}

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5001))
    app.run(host="0.0.0.0", port=port)
