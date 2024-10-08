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

# Add the /start command handler
application.add_handler(CommandHandler("start", start))

# Vercel requires this entry point for serverless functions
async def handler(request):
    # Parse the incoming request from Telegram
    update = Update.de_json(request.get_json(force=True), application.bot)
    await application.process_update(update)

# This line is essential for Vercel to recognize the handler
app = handler  # Add this line to define the callable app
