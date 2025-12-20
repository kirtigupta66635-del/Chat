
import os

BOT_TOKEN = os.getenv("BOT_TOKEN", "7789010028:AAEA5dC6R99-nHRR1KPlXCl74KvlTjTx6zo")
OWNER_ID = int(os.getenv("OWNER_ID", "7995588921"))
# OpenAI API Key
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "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")
# 🔴 यही line missing है
MONGO_URL = os.getenv(
    "MONGO_URL",
    "mongodb+srv://h17589479_db_user:W5l1NuSQ2cak8I04@cluster0.tkxlnpf.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
)

DB_NAME = "telegram_game"
SCORE_COLLECTION = "scores"
USER_COLLECTION = "users"
GROUP_COLLECTION = "groups"


START_EMOJI = (
    "🎮🧩🔥✨😄🎉🥳"
    "🕹️🎯🧠⚡"
    "🏆⭐🌟💯"
)
