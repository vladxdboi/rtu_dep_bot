from fastapi import FastAPI, Request
import requests
import os

app = FastAPI()

# Replace this with your actual bot token
TOKEN = os.getenv("7911027827:AAFmPaq8pUdQSjKOASuMAgrTd9001raAtJ4")

@app.post("/webhook")
async def webhook(request: Request):
    update = await request.json()
    
    # Check if the update contains a message with the /start command
    if 'message' in update and 'text' in update['message']:
        chat_id = update['message']['chat']['id']
        text = update['message']['text']

        if text == '/start':
            send_message(chat_id, "Welcome! How can I assist you today?")

    return {"status": "ok"}

def send_message(chat_id, text):
    url = f"https://api.telegram.org/bot{7911027827:AAFmPaq8pUdQSjKOASuMAgrTd9001raAtJ4}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": text,
        "parse_mode": "HTML"  # Optional: Use HTML formatting
    }
    requests.post(url, json=payload)