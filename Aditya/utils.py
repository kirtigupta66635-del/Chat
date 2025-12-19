import random

WORDS = {
    "animal": ["CAT", "LION", "TIGER", "DOG"],
    "human": ["KING", "QUEEN", "DOCTOR"],
    "history": ["ROME", "INDIA"]
}

def masked_word():
    category = random.choice(list(WORDS.keys()))
    word = random.choice(WORDS[category])
    idx = random.randint(1, len(word)-2)
    masked = word[:idx] + "_" + word[idx+1:]
    return masked, word
