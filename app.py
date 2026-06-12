from flask import Flask, request
from telegram import Bot
import os

app = Flask(__name__)

bot = Bot(token=os.getenv("BOT_TOKEN"))
ADMIN_ID = 8811147681

@app.route("/send", methods=["POST"])
def send():
    data = request.json

    user_id = data["user_id"]
    message = data["message"]

    bot.send_message(
        chat_id=ADMIN_ID,
        text=f"📩 پیام جدید از {user_id}:\n\n{message}"
    )

    return {"ok": True}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
