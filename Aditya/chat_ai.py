# import openai
from config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

async def reply(user_id: int, user_message: str) -> str:
    try:
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful, friendly, and funny chatbot."},
                {"role": "user", "content": user_message}
            ],
            temperature=0.8,
            max_tokens=150
        )
        answer = response.choices[0].message.content
        return answer
    except Exception as e:
        return f"Sorry, I couldn't process your message. Error: {e}"


