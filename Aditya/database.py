from pymongo import MongoClient
from config import MONGO_URL

# Mongo client connect
client = MongoClient(MONGO_URL)

# Database & Collection
db = client["telegram_game"]
scores_col = db["scores"]

def add_score(user_id: int, chat_id: int, points: int = 10):
    """
    Add or update user score in MongoDB
    """
    scores_col.update_one(
        {
            "chat_id": chat_id,
            "user_id": user_id
        },
        {
            "$inc": {"score": points}
        },
        upsert=True
    )


def top_scores(chat_id: int, limit: int = 5):
    """
    Get top users of a chat from MongoDB
    """
    cursor = scores_col.find(
        {"chat_id": chat_id},
        {"_id": 0, "user_id": 1, "score": 1}
    ).sort("score", -1).limit(limit)

    return [(doc["user_id"], doc["score"]) for doc in cursor]
