from pymongo import MongoClient
from config import MONGO_URI, DB_NAME, USER_COLLECTION, GROUP_COLLECTION

client = MongoClient(MONGO_URI)
db = client[DB_NAME]

users = db[USER_COLLECTION]
groups = db[GROUP_COLLECTION]

# ------------- User Score ----------------
def add_user_score(user_id, points):
    users.update_one(
        {"user_id": user_id},
        {"$inc": {"total_score": points}},
        upsert=True
    )

def global_top_users(limit=10):
    return list(users.find({}, {"_id":0}).sort("total_score",-1).limit(limit))

# ------------- Group Score ----------------
def add_group_score(chat_id, points):
    groups.update_one(
        {"chat_id": chat_id},
        {"$inc": {"total_score": points}},
        upsert=True
    )

def increase_game_count(chat_id):
    groups.update_one(
        {"chat_id": chat_id},
        {"$inc": {"games_played": 1}},
        upsert=True
    )

def top_groups(limit=10):
    return list(groups.find({}, {"_id":0}).sort("total_score",-1).limit(limit))
