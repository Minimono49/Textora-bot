from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Function to handle the /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! I am Textora, your bot.")

# Main function to set up the bot
def main():
    # Replace 'YOUR_API_TOKEN' with your token from BotFather
    application = Application.builder().token("8154052887:AAFvaZE_i3KgmvOWpXnBZnHfd7roE9sBF8g").build()

    # Add command handler for /start
    application.add_handler(CommandHandler("start", start))

    # Start the bot
    application.run_polling()

if __name__ == "__main__":
    main()
