import requests
from flask import Flask, request

app = Flask(__name__)

TELEGRAM_API_URL = "https://api.telegram.org/bot7911027827:AAFmPaq8pUdQSjKOASuMAgrTd9001raAtJ4/sendMessage"

@app.route('/webhook', methods=['POST'])
def webhook():
    update = request.get_json()
    
    chat_id = update['message']['chat']['id']
    text = update['message']['text']

    if text == "/start":
        # Send a message with a link to the web app
        web_app_url = "https://rtu-dep-bot-git-main-vlads-projects-7e339f13.vercel.app"  # Replace with your web app URL
        message = f"Welcome! Click here to access the web app: {web_app_url}"
        
        requests.post(TELEGRAM_API_URL, json={"chat_id": chat_id, "text": message})

    return "OK", 200

if __name__ == "__main__":
    app.run(port=5000)