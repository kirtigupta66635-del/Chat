from utils import masked_word
from database import add_score

ACTIVE_GAME = {}

def start_game(chat_id):
    masked, answer = masked_word()
    ACTIVE_GAME[chat_id] = answer
    return f"🧩 Guess the word:\n\n`{masked}`"

def check_answer(message, user_id, chat_id):
    if chat_id not in ACTIVE_GAME:
        return None
    if message.upper() == ACTIVE_GAME[chat_id]:
        add_score(user_id, chat_id, 10)
        del ACTIVE_GAME[chat_id]
        return True
    return False
