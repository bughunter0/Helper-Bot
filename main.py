import os
import pyrogram
from pyrogram import Client, filters

FayasNoushad = Client(
    "Developers-Bot",
    bot_token = os.environ["BOT_TOKEN"],
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"]
)

FayasNoushad.run()
