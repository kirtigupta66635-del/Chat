
"""
Temporary chat_ai module
Chat disabled – Game testing mode
"""

# ---------------------------
# Dummy memory store
# ---------------------------
_USER_MEMORY = {}


def remember(user_id: int, text: str):
    """
    Placeholder function
    Currently does NOTHING
    """
    return None


def reply(text: str):
    """
    Chat disabled
    Always returns None
    """
    return None


def clear_memory(user_id: int):
    """
    Clear user memory (unused for now)
    """
    _USER_MEMORY.pop(user_id, None)


def get_memory(user_id: int):
    """
    Return empty memory
    """
    return []
