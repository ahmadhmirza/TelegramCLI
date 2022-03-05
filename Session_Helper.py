from datetime import datetime
from telethon import TelegramClient

"""
Holds methods to help with client/session lifecycle operations
"""

async def logout(client):
    await client.log_out()
    print("Logged out successfully.")


def create_session(api_id, api_hash):
    client = TelegramClient('anon', api_id, api_hash)
    print(f"Session created at {datetime.now()}")
    return client
