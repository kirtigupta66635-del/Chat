from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

# 🔥 ROOT imports (important)
from config import BOT_TOKEN, START_EMOJI
from Aditya.game import start_game, check_answer
from Aditya.database import global_top_users, top_groups
from Aditya.chat_ai import remember, reply


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        f"{START_EMOJI} Welcome!\n/play to start game"
    )


async def play(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        start_game(update.effective_chat.id)
    )


async def leaderboard(update: Update, context: ContextTypes.DEFAULT_TYPE):
    scores = global_top_users()
    if not scores:
        await update.message.reply_text("No scores yet!")
        return

    msg = "🏆 Top 10 Players:\n\n"
    for i, d in enumerate(scores, 1):
        msg += f"{i}. {d['user_id']} → {d['total_score']}\n"

    await update.message.reply_text(msg)


async def grouptop(update: Update, context: ContextTypes.DEFAULT_TYPE):
    groups = top_groups()
    if not groups:
        await update.message.reply_text("No group data!")
        return

    msg = "🏆 Top 10 Groups:\n\n"
    for i, d in enumerate(groups, 1):
        msg += f"{i}. {d['chat_id']} → {d['total_score']}\n"

    await update.message.reply_text(msg)


async def message_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message or not update.message.text:
        return

    text = update.message.text
    chat_id = update.effective_chat.id
    user_id = update.effective_user.id

    # 🎮 Game check
    res = check_answer(text, user_id, chat_id)
    if isinstance(res, str):
        await update.message.reply_text(res)
        return

    # 💬 Chat mode
    remember(user_id, text)
    await update.message.reply_text(reply(user_id, text))


def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("play", play))
    app.add_handler(CommandHandler("top", leaderboard))
    app.add_handler(CommandHandler("grouptop", grouptop))
    app.add_handler(
        MessageHandler(filters.TEXT & ~filters.COMMAND, message_handler)
    )

    app.run_polling()


if __name__ == "__main__":
    main()
