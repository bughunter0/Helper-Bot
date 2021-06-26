from pyrogram import Client, filters
from ..commands import *

@Client.on_message(filters.private & filters.command(["start", "help" "about"]) & filters.user(AUTH_USERS) if AUTH_USERS else None)
async def start_command(bot, update):
    text = update.text
    if text == "/start":
        await start(bot, update)
    else:
        text = text.split(" ", -1)
