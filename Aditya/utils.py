import random

USED_WORDS = set()

def zipf_frequency(word: str, lang: str = "en") -> float:
    # Simple frequency placeholder
    return random.uniform(1, 10)

def get_random_word(min_len: int, max_len: int = None) -> str:
    while True:
        length = random.randint(min_len, max_len or min_len + 3)
        word = "".join(random.choice("abcdefghijklmnopqrstuvwxyz") for _ in range(length))
        if zipf_frequency(word) > 2.5 and word.upper() not in USED_WORDS:
            USED_WORDS.add(word.upper())
            return word.upper()

def pick_word_by_level(level: int) -> str:
    if level < 10:
        return get_random_word(3, 5)
    elif level < 20:
        return get_random_word(6, 8)
    else:
        return get_random_word(9, 12)

def mask_word(word: str) -> str:
    return "".join(c if random.random() > 0.6 else "_" for c in word)

def masked_word(level: int) -> tuple[str, str]:
    word = pick_word_by_level(level)
    return mask_word(word), word
