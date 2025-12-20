import random
from Aditya.utils import zipf_frequency  # अगर तुम्हारे utils में है
from Aditya.database import add_score  # अगर जरूरी हो तो

# ------------------------------
# Used words tracker
# ------------------------------
USED_WORDS = set()

# ------------------------------
# Generate random word
# ------------------------------
def get_random_word(min_len: int, max_len: int = None) -> str:
    """
    Random English word generate करता है जो frequency > 2.5 और
    पहले इस्तेमाल नहीं हुआ हो।
    """
    while True:
        length = random.randint(min_len, max_len or min_len + 3)
        word = "".join(random.choice("abcdefghijklmnopqrstuvwxyz") for _ in range(length))
        # Frequency check
        if zipf_frequency(word, "en") > 2.5 and word.upper() not in USED_WORDS:
            USED_WORDS.add(word.upper())
            return word.upper()

# ------------------------------
# Pick word according to level
# ------------------------------
def pick_word_by_level(level: int) -> str:
    if level < 10:
        return get_random_word(3, 5)
    elif level < 20:
        return get_random_word(6, 8)
    else:
        return get_random_word(9, 12)

# ------------------------------
# Mask the word
# ------------------------------
def mask_word(word: str) -> str:
    """
    Word को mask करता है, random letters hide करता है
    """
    return "".join(c if random.random() > 0.6 else "_" for c in word)

# ------------------------------
# Main function to get masked word
# ------------------------------
def masked_word(level: int) -> tuple[str, str]:
    """
    Level के हिसाब से word pick और mask करके return करता है
    Returns:
        masked_word (str), original_word (str)
    """
    word = pick_word_by_level(level)
    return mask_word(word), word
