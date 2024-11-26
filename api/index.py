from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
import requests
import logging
from pathlib import Path

app = FastAPI()

# Set up logging
logging.basicConfig(level=logging.INFO)

# Telegram Bot Token and API URL
TELEGRAM_BOT_TOKEN = "7911027827:AAFmPaq8pUdQSjKOASuMAgrTd9001raAtJ4"  # Use an environment variable in production
TELEGRAM_API_URL = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"

# Path to the external HTML file
HTML_FILE_PATH = Path("static/index.html")  # Adjust this path to match your project's structure

# Home route that displays the landing page
@app.get("/", response_class=HTMLResponse)
async def read_root():
    try:
        # Read the content of the HTML file
        html_content = HTML_FILE_PATH.read_text(encoding="utf-8")
        return HTMLResponse(content=html_content)
    except FileNotFoundError:
        return HTMLResponse(content="<h1>Error: HTML file not found</h1>", status_code=404)

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