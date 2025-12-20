MEMORY = {}

def remember(user_id, message):
    if user_id not in MEMORY:
        MEMORY[user_id] = []
    MEMORY[user_id].append(message)

def reply(user_id, message):
    prev = MEMORY.get(user_id, [])
    response = f"🤖 You said: {message}"
    if prev:
        response += f"\nLast thing you said: {prev[-1]}"
    return response
