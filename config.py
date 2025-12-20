
import os

BOT_TOKEN = os.getenv("BOT_TOKEN", "7789010028:AAEA5dC6R99-nHRR1KPlXCl74KvlTjTx6zo")

# MongoDB Atlas URI
MONGO_URI = os.getenv(
    "MONGO_URI",
    "mongodb+srv://h17589479_db_user:W5l1NuSQ2cak8I04@cluster0.tkxlnpf.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
)

DB_NAME = "telegram_game"
SCORE_COLLECTION = "scores"

START_EMOJI = "🎮"
