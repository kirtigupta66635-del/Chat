
from database import cur, conn

def remember(user_id, text):
    cur.execute("INSERT OR REPLACE INTO memory (user_id, text) VALUES (?,?)", (user_id, text))
    conn.commit()

def reply(user_id, text):
    cur.execute("SELECT text FROM memory WHERE user_id=?", (user_id,))
    old = cur.fetchone()
    if old:
        return f"😄 You said earlier: {old[0]}"
    return "🙂 Tell me more..."
