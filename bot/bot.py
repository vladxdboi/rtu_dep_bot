from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes

# Function to handle the /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # Define the URL of your web app
    web_app_url = "https://rtu-dep-bot-git-main-vlads-projects-7e339f13.vercel.app/"  # Replace with your actual URL

    # Create a button that links to your web app
    keyboard = [[InlineKeyboardButton("Open Web App", url=web_app_url)]]
    reply_markup = InlineKeyboardMarkup(keyboard)

    # Send a message with the button
    await update.message.reply_text("Welcome! Click the button below to open the web app:", reply_markup=reply_markup)

async def main() -> None:
    # Replace 'YOUR_TOKEN' with your bot's actual token
    application = Application.builder().token("7911027827:AAFmPaq8pUdQSjKOASuMAgrTd9001raAtJ4").build()

    # Handle the /start command
    application.add_handler(CommandHandler("start", start))

    # Start the bot
    await application.initialize()
    await application.start_polling()  # Start polling for updates
    await application.idle()  # Wait until the bot is stopped

if __name__ == '__main__':
    import asyncio
    asyncio.run(main())
