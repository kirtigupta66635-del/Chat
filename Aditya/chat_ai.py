# chat_ai.py
import openai
from config import OPENAI_API_KEY  # अपने config.py में API की सेट करें

openai.api_key = OPENAI_API_KEY

# Optional: यूज़र्स की बातचीत याद रखने के लिए memory dict
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


async def reply(user_id: int, user_message: str) -> str:
    """
    OpenAI GPT से यूज़र का जवाब लेने वाला फंक्शन
    """
    try:
        # याद रखें मैसेज
        remember(user_id, user_message)

        # OpenAI से response generate करना
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # या gpt-4
            messages=[
                {"role": "system", "content": "You are a helpful, friendly, and funny chatbot."},
                {"role": "user", "content": user_message}
            ],
            max_tokens=150,
            temperature=0.8
        )

        answer = response['choices'][0]['message']['content'].strip()
        # याद रखें AI का जवाब भी
        remember(user_id, answer)

        return answer

    except Exception as e:
        return f"Sorry, I couldn't process your message. Error: {e}"
