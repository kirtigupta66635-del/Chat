# simple behavior model placeholder

def mood(text):
    if "sad" in text.lower():
        return "😢 Don't worry, I'm here"
    if "happy" in text.lower():
        return "😄 That's great!"
    return "🤖 Hmm..."
