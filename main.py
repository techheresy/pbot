from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes
import pprint
import time
import os


TOKEN = os.getenv("BOT_TOKEN")
if not TOKEN:
    raise ValueError("no token in environment variables")

BAD_WORDS = ["похуй"]

GIF_ID = "CgACAgQAAxkBAAMEaQM-pDF3x3zUQPw1NVyVjCeA-o8AAk8IAALVfqRRj__RcMvDFnw2BA"

async def check_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message:
        return

    text = update.message.text.lower()
    user = update.message.from_user.first_name

    for word in BAD_WORDS:
        if word in text:
            await update.message.reply_animation(animation=GIF_ID)
            break

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, check_message))

while True:
    try:
        print("bot started")
        app.run_polling()
    except Exception as error:
        print(f"error, restarting: {error}")
        time.sleep(1)