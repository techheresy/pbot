from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes
import time
import os
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s - %(message)s",
)

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
            logging.info(f"user {user} sent bad word {word}")
            await update.message.reply_animation(animation=GIF_ID)
            break

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, check_message))


while True:
    try:
        logging.info("bot started")
        app.run_polling()
    except Exception as error:
        logging.exception("error, restarting")
        time.sleep(1)