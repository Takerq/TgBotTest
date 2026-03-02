# from telegram import Update
# from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
# from config import API_TOKEN
# bot = ApplicationBuilder().token(API_TOKEN).build()
# @bot.message_handler(commands=['start'])
# def welcome(message):
#     bot.send_message(message.chat.id, "Welcome to the bot!")

# bot.run_polling()

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

BOT_TOKEN = "8632396495:AAHf5AjI-rIBcxHtLvy5IlgRv3tSEtn1pgU"

# This will store user IDs
users = []

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id

    # Add user if not already saved
    if user_id not in users:
        users.append(user_id)
        print("New user added:", user_id)

    await update.message.reply_text("Welcome!")

app = ApplicationBuilder().token(BOT_TOKEN).build()

app.add_handler(CommandHandler("start", start))

print("Bot started...")
app.run_polling()