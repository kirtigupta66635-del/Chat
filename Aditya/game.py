import time
from utils import masked_word
from database import add_score

ACTIVE_GAME = {}

BASE_TIME = 25
MIN_TIME = 8
BASE_POINTS = 10


def start_game(chat_id):
    masked, answer = masked_word()
    level = ACTIVE_GAME.get(chat_id, {}).get("level", 0) + 1

    time_limit = max(BASE_TIME - level * 2, MIN_TIME)

    ACTIVE_GAME[chat_id] = {
        "answer": answer,
        "start": time.time(),
        "level": level,
        "time_limit": time_limit
    }

    return (
        f"🧩 Guess the word:\n\n"
        f"`{masked}`\n\n"
        f"⏱ Time: {time_limit}s | 🔥 Level: {level}"
    )


def check_answer(message, user_id, chat_id):
    game = ACTIVE_GAME.get(chat_id)
    if not game:
        return None

    elapsed = time.time() - game["start"]

    if elapsed > game["time_limit"]:
        del ACTIVE_GAME[chat_id]
        return "⏰ Time up!"

    if message.upper().strip() == game["answer"]:
        points = BASE_POINTS + game["level"] * 2
        add_score(user_id, chat_id, points)
        del ACTIVE_GAME[chat_id]
        return f"✅ Correct! +{points} points"

    return False
