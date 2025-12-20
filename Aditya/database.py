from pymongo import MongoClient
from config import MONGO_URL, DB_NAME, USER_COLLECTION, GROUP_COLLECTION

# MongoDB client
client = MongoClient(MONGO_URL)
db = client[DB_NAME]

users = db[USER_COLLECTION]
groups = db[GROUP_COLLECTION]

# ------------- User Score ----------------
def add_user_score(user_id: int, points: int = 5):
    users.update_one(
        {"user_id": user_id},
        {"$inc": {"total_score": points}},
        upsert=True
    )

def global_top_users(limit: int = 10):
    return list(users.find({}, {"_id": 0}).sort("total_score", -1).limit(limit))

# ------------- Group Score ----------------
def add_group_score(chat_id: int, points: int = 5):
    groups.update_one(
        {"chat_id": chat_id},
        {"$inc": {"total_score": points}},
        upsert=True
    )

def increase_game_count(chat_id: int):
    groups.update_one(
        {"chat_id": chat_id},
        {"$inc": {"games_played": 1}},
        upsert=True
    )

def top_groups(limit: int = 10):
    return list(groups.find({}, {"_id": 0}).sort("total_score", -1).limit(limit))
