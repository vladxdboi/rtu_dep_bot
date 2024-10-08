import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes

# Create the application instance globally
application = Application.builder().token(os.getenv("7911027827:AAFmPaq8pUdQSjKOASuMAgrTd9001raAtJ4")).build()

# Function to handle the /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # Define the URL of your web app
    web_app_url = "https://rtu-dep-bot-git-main-vlads-projects-7e339f13.vercel.app"  # Replace with your actual URL

    # Create a button that links to your web app
    keyboard = [[InlineKeyboardButton("Open Web App", url=web_app_url)]]
    reply_markup = InlineKeyboardMarkup(keyboard)

    # Send a message with the button
    await update.message.reply_text("Welcome! Click the button below to open the web app:", reply_markup=reply_markup)

application.add_handler(CommandHandler("start", start))

# Vercel requires this entry point for serverless functions
async def handler(request):
    # Parse the incoming request from Telegram
    json_data = await request.json()  # Get JSON data from the request
    update = Update.de_json(json_data, application.bot)  # Convert it to a Telegram Update object
    await application.process_update(update)  # Process the update

# This line is essential for Vercel to recognize the handler
app = handler  # Define the callable app
