import random

def generate_hint(word, revealed=1):
    """
    Returns a hint for a word:
    - revealed: number of letters to show
    """
    hint = ["_"] * len(word)
    indices = random.sample(range(len(word)), min(revealed, len(word)))
    for i in indices:
        hint[i] = word[i]
    return "".join(hint)
