# chat_ai.py
import openai
from config import OPENAI_API_KEY  # अपने config.py में API की सेट करें

openai.api_key = OPENAI_API_KEY

async def reply(user_message: str) -> str:
    """
    यूज़र के मैसेज का जवाब देने वाला फंक्शन
    """
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # या gpt-4, अगर आपके पास API है
            messages=[
                {"role": "system", "content": "You are a helpful, friendly, and funny chatbot."},
                {"role": "user", "content": user_message}
            ],
            max_tokens=150,
            temperature=0.8
        )
        answer = response['choices'][0]['message']['content'].strip()
        return answer
    except Exception as e:
        return f"Sorry, I couldn't process your message. Error: {e}"


# Optional: एक सिंपल मेमोरी सिस्टम
memory = {}

def remember(user_id: int, message: str):
    """
    यूज़र की बातों को याद रखने वाला फंक्शन
    """
    if user_id not in memory:
        memory[user_id] = []
    memory[user_id].append(message)
    # मेमोरी को 10 मैसेज तक सीमित करें
    if len(memory[user_id]) > 10:
        memory[user_id].pop(0)
