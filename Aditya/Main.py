import sys
import os

# root directory add
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters
)

from config import BOT_TOKEN, START_EMOJI
from game import start_game, check_answer
from Model import mood   # ✅ FIXED (case-sensitive)

# ---------------- TEMP SAFE FUNCTIONS ----------------
# जब तक database.py और chat_ai.py नहीं बनते

def top_scores(chat_id):
    return []

def remember(user_id, text):
    pass

def reply(user_id, text):
    return "🙂 I heard you."
# -----------------------------------------------------


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        f"{START_EMOJI} Welcome!\n/play to start game"
    )

async def play(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = start_game(update.effective_chat.id)
    await update.message.reply_text(text)

async def leaderboard(update: Update, context: ContextTypes.DEFAULT_TYPE):
    scores = top_scores(update.effective_chat.id)
    msg = "🏆 Top 5 Players:\n"
    for uid, score in scores:
        msg += f"{uid} → {score}\n"
    await update.message.reply_text(msg)

async def message_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    chat = update.effective_chat

    res = check_answer(update.message.text, user.id, chat.id)
    if res:
        await update.message.reply_text("✅ Correct! +10 points")
        return

    remember(user.id, update.message.text)
    await context.bot.send_message(
    chat_id=update.effective_chat.id,
    text=text
)


app = ApplicationBuilder().token(BOT_TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("play", play))
app.add_handler(CommandHandler("top", leaderboard))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, message_handler))

app.run_polling()
