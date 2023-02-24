import os
import requests

from flask import Flask, request

app = Flask(__name__)

@app.route("/callback", methods=["POST"])
def callback():
    # Get the request content
    request_json = request.get_json()

    # Get the reply token
    reply_token = request_json["events"][0]["replyToken"]

    # Send a reply message
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer <your_channel_access_token>"
    }
    data = {
        "replyToken": reply_token,
        "messages": [
            {
                "type": "text",
                "text": "Hello, world!"
            }
        ]
    }
    requests.post("https://api.line.me/v2/bot/message/reply", headers=headers, json=data)

    return "OK"

if __name__ == "__main__":
    app.run(port=os.environ.get("PORT", 5000))