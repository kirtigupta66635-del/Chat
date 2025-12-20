import time
from Aditya.utils import masked_word
from Aditya.database import add_user_score, add_group_score, increase_game_count
from Aditya.hints import generate_hint

ACTIVE_GAME = {}
MAX_TIME = 60
MIN_TIME = 5
BASE_POINTS = 5

def calculate_time(level):
    time_limit = MAX_TIME
    for l in range(1, level+1):
        time_limit -= 5 if l <=3 else 3
    return max(time_limit, MIN_TIME)

def start_game(chat_id):
    prev = ACTIVE_GAME.get(chat_id)
    level = prev.get("level",0)+1 if prev else 1

    masked, answer = masked_word(level)
    time_limit = calculate_time(level)

    ACTIVE_GAME[chat_id] = {
        "answer": answer,
        "start": time.time(),
        "level": level,
        "time": time_limit,
        "hint_shown": False
    }

    return (
        f"🧩 *Level {level}*\n"
        f"Guess the word:\n`{masked}`\n\n"
        f"⏱ Time: {time_limit}s"
    )

def check_answer(text, user_id, chat_id):
    game = ACTIVE_GAME.get(chat_id)
    if not game:
        return None

    elapsed = time.time() - game["start"]

    # AI hint after half time
    if not game["hint_shown"] and elapsed > game["time"]/2:
        hint = generate_hint(game["answer"], revealed=max(1, len(game["answer"])//3))
        game["hint_shown"] = True
        return f"💡 Hint: `{hint}`"

    if elapsed > game["time"]:
        del ACTIVE_GAME[chat_id]
        return "⏰ Time up!"

    if text.upper().strip() == game["answer"]:
        points = BASE_POINTS + game["level"]
        add_user_score(user_id, points)
        add_group_score(chat_id, points)
        increase_game_count(chat_id)
        del ACTIVE_GAME[chat_id]
        return f"✅ Correct! +{points} points"

    return False
