import sqlite3
from config import DB_NAME

conn = sqlite3.connect(DB_NAME, check_same_thread=False)
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER,
    chat_id INTEGER,
    score INTEGER DEFAULT 0,
    PRIMARY KEY (user_id, chat_id)
)
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS memory (
    user_id INTEGER PRIMARY KEY,
    text TEXT
)
""")

conn.commit()

def add_score(user_id, chat_id, points):
    cur.execute("""
    INSERT OR IGNORE INTO users (user_id, chat_id, score) VALUES (?, ?, 0)
    """, (user_id, chat_id))
    cur.execute("""
    UPDATE users SET score = score + ? WHERE user_id=? AND chat_id=?
    """, (points, user_id, chat_id))
    conn.commit()

def top_scores(chat_id):
    cur.execute("""
    SELECT user_id, score FROM users WHERE chat_id=?
    ORDER BY score DESC LIMIT 5
    """, (chat_id,))
    return cur.fetchall()
