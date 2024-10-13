from fastapi import FastAPI, File, UploadFile, Request
from fastapi.responses import HTMLResponse
import requests
import logging

app = FastAPI()

# Set up logging
logging.basicConfig(level=logging.INFO)

# Telegram Bot Token and API URL
TELEGRAM_BOT_TOKEN = "7911027827:AAFmPaq8pUdQSjKOASuMAgrTd9001raAtJ4"  # Use an environment variable in production
TELEGRAM_API_URL = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"

# Home route that displays a simple HTML form for file upload
@app.get("/", response_class=HTMLResponse)
async def read_root():
    return """
    <html>
        <body>
            <h1>Upload a File</h1>
            <form action="/uploadfile/" method="post" enctype="multipart/form-data">
                <input name="file" type="file" />
                <input type="submit" value="Upload" />
            </form>
        </body>
    </html>
    """

# Route to handle file upload
@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile = File(...)):
    contents = await file.read()
    return {"filename": file.filename, "file_size": len(contents)}

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
            web_app_url = "https://rtu-dep-bot-git-main-vlads-projects-7e339f13.vercel.app"
            message = f"Welcome! Click here to access the web app: {web_app_url}"
            response = requests.post(TELEGRAM_API_URL, json={"chat_id": chat_id, "text": message})

            # Log response status from Telegram API
            if response.status_code != 200:
                logging.error(f"Failed to send message: {response.text}")

    return {"status": "ok"}
