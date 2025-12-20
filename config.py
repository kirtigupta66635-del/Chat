
import os

BOT_TOKEN = os.getenv("BOT_TOKEN", "7789010028:AAEA5dC6R99-nHRR1KPlXCl74KvlTjTx6zo")
OWNER_ID = int(os.getenv("OWNER_ID", "7995588921"))
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
