from Aditya.utils import masked_word
from Aditya.game import start_game, check_answer
from Aditya.database import global_top_users, top_groups
from Aditya.chat_ai import remember, reply

USED_WORDS = set()

def get_random_word(min_len, max_len=None):
    while True:
        length = random.randint(min_len, max_len or min_len + 3)
        word = "".join(random.choice("abcdefghijklmnopqrstuvwxyz") for _ in range(length))
        if zipf_frequency(word, "en") > 2.5 and word.upper() not in USED_WORDS:
            USED_WORDS.add(word.upper())
            return word.upper()

def pick_word_by_level(level):
    if level < 10:
        return get_random_word(3,5)
    elif level < 20:
        return get_random_word(6,8)
    else:
        return get_random_word(9,12)

def mask_word(word):
    masked = ""
    for c in word:
        masked += "_" if random.random() < 0.6 else c
    return masked

def masked_word(level):
    word = pick_word_by_level(level)
    return mask_word(word), word
