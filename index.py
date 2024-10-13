from fastapi import FastAPI, Request
import requests
import os

app = FastAPI()

TOKEN = os.getenv("7911027827:AAFmPaq8pUdQSjKOASuMAgrTd9001raAtJ4")

@app.post("/webhook")
async def webhook(request: Request):
    update = await request.json()
    
    # Log the incoming update for debugging
    print(update)  # This will print the update to Vercel logs
    
    if 'message' in update and 'text' in update['message']:
        chat_id = update['message']['chat']['id']
        text = update['message']['text']

        if text == '/start':
            send_message(chat_id, "Welcome! How can I assist you today?")
        else:
            send_message(chat_id, "You typed: " + text)  # Echo any other message

    return {"status": "ok"}

def send_message(chat_id, text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": text,
        "parse_mode": "HTML"  # Optional: Use HTML formatting
    }
    response = requests.post(url, json=payload)
    
    # Log the response for debugging
    print(response.json())  # Check if the message was sent successfully

