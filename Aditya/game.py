import random
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

# ================= WORD BANK (LEVEL WISE) =================

WORD_LEVELS = {
    1: ["CAT", "DOG", "SUN", "BAT", "BALL", "CAR", "BUS", "HAT"],
    2: ["APPLE", "BANANA", "MONKEY", "TIGER", "ELEPHANT", "PENCIL"],
    3: ["COMPUTER", "KEYBOARD", "INTERNET", "PYTHON", "TELEGRAM"],
    4: ["ASTRONOMY", "MICROSCOPE", "PHILOSOPHY", "PSYCHOLOGY"],
    5: ["METAMORPHOSIS", "ELECTROMAGNETISM", "HIPPOPOTOMONSTROSES"]
}

# ================= GAME STATE =================

CURRENT_WORD = {}        # chat_id -> word
USED_WORDS = {}          # chat_id -> set(words)
USER_SCORE = {}          # user_id -> score

# ================= FUN TEXT =================

FUN_CORRECT = [
    "🔥 BOOM!",
    "😎 OP PLAYER!",
    "🎯 PERFECT!",
    "🧠 BRAIN ON!",
    "💥 LEGEND MOVE!"
]

FUN_SKIP = [
    "😂 Skip bhi talent hai!",
    "🙈 Chalo next!",
    "😜 Easy wala do!",
]

# ================= HELPERS =================

def get_level(score: int) -> int:
    if score < 5:
        return 1
    elif score < 10:
        return 2
    elif score < 20:
        return 3
    elif score < 35:
        return 4
    else:
        return 5


def get_new_word(chat_id: int, level: int):
    USED_WORDS.setdefault(chat_id, set())
    pool = list(set(WORD_LEVELS[level]) - USED_WORDS[chat_id])

    if not pool:  # level words finished
        USED_WORDS[chat_id].clear()
        pool = WORD_LEVELS[level][:]

    word = random.choice(pool)
    USED_WORDS[chat_id].add(word)
    CURRENT_WORD[chat_id] = word
    return word


def keyboard():
    return InlineKeyboardMarkup(
        [[InlineKeyboardButton("⏭ SKIP", callback_data="skip_word")]]
    )

# ================= START GAME =================

def start_game(chat_id: int):
    word = get_new_word(chat_id, 1)
    return (
        f"🎮 WORD GAME STARTED\n\n"
        f"👉 **{word}**\n\n"
        f"✍️ Just type the word!",
        keyboard()
    )

# ================= CHECK ANSWER =================

def check_answer(text: str, user_id: int, chat_id: int):
    if chat_id not in CURRENT_WORD:
        return None

    # 🔥 CASE INSENSITIVE MATCH
    if text.strip().upper() != CURRENT_WORD[chat_id]:
        return None

    USER_SCORE[user_id] = USER_SCORE.get(user_id, 0) + 1
    score = USER_SCORE[user_id]
    level = get_level(score)

    new_word = get_new_word(chat_id, level)

    return (
        f"{random.choice(FUN_CORRECT)}\n\n"
        f"🏆 +1 POINT\n"
        f"⭐ SCORE: <b>{score}</b>\n"
        f"🧩 LEVEL: <b>{level}</b>\n\n"
        f"👉 NEXT WORD:\n"
        f"<b>{new_word}</b>",
        keyboard()
    )

# ================= SKIP =================

def skip_word(chat_id: int):
    score = 0
    for s in USER_SCORE.values():
        score = max(score, s)

    level = get_level(score)
    word = get_new_word(chat_id, level)

    return (
        f"{random.choice(FUN_SKIP)}\n\n"
        f"👉 NEW WORD:\n"
        f"<b>{word}</b>",
        keyboard()
    )
