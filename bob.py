from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters

# Function that handles the /start command
async def start(update: Update, context) -> None:
    await update.message.reply_text('Hello! I am your Telegram mini app!')

# Function that handles text messages
async def echo(update: Update, context) -> None:
    await update.message.reply_text(update.message.text)

async def main():
    # Replace 'YOUR_TOKEN' with your bot's actual token
    application = Application.builder().token("7911027827:AAFmPaq8pUdQSjKOASuMAgrTd9001raAtJ4").build()

    # Initialize the application
    await application.initialize()

    # Handle the /start command
    application.add_handler(CommandHandler("start", start))

    # Handle text messages
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    # Start the bot
    await application.start()

    # Keep the bot running until it’s manually stopped
    await application.stop()

if __name__ == '__main__':
    import asyncio
    asyncio.run(main())
