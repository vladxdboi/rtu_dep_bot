from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
import requests
import logging

app = FastAPI()

# Set up logging
logging.basicConfig(level=logging.INFO)

# Telegram Bot Token and API URL
TELEGRAM_BOT_TOKEN = "7911027827:AAFmPaq8pUdQSjKOASuMAgrTd9001raAtJ4"  # Use an environment variable in production
TELEGRAM_API_URL = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"

# Home route that displays a greeting landing page
@app.get("/", response_class=HTMLResponse)
async def read_root():
    return """
    <html>
        <head>
            <title>Welcome to My Web App</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    text-align: center;
                    padding: 50px;
                }
                h1 {
                    color: #4CAF50;
                }
                button {
                    padding: 10px 20px;
                    font-size: 16px;
                    cursor: pointer;
                    background-color: #4CAF50;
                    color: white;
                    border: none;
                    border-radius: 5px;
                }
                button:hover {
                    background-color: #45a049;
                }
            </style>
        </head>
        <body>
            <h1>Welcome to My Web App!</h1>
            <p>Click the button below to get started:</p>
            <button onclick="window.location.href='https://t.me/rtu_dep_bot/Bobing'">Go to Web App</button>
        </body>
    </html>
    """

# Webhook route for Telegram bot
@app.post("/webhook")
async def telegram_webhook(request: Request):
    update = await request.json()
    logging.info(f"Received update: {update}")  # Log incoming updates

    # Check if the necessary keys exist in the update
    if 'message' in update and 'chat' in update['message'] and 'text' in update['message']:
        chat_id = update['message']['chat']['id']
        text = update['message']['text']

        if text == "/start":
            # Send a welcome message with a link to the web app
            web_app_url = "https://t.me/rtu_dep_bot/Bobing"  # Replace with your web app URL
            message = f"Welcome! Click here to access the web app: {web_app_url}"
            response = requests.post(TELEGRAM_API_URL, json={"chat_id": chat_id, "text": message})

            # Log response status from Telegram API
            if response.status_code != 200:
                logging.error(f"Failed to send message: {response.text}")

    return {"status": "ok"}