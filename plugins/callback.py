# Author: Fayas (https://github.com/FayasNoushad) (@FayasNoushad)

from pyrogram import Client
from .commands import *


@Client.on_callback_query(
    filters.user(AUTH_USERS) if PRIVATE else None
)
async def cb_handler(bot, update):
    if update.data == "home":
        await start(bot, update, cb=True)
    elif update.data == "help":
        await help(bot, update, cb=True)
    elif update.data == "about":
        await about(bot, update, cb=True)
    elif update.data == "close":
        await update.message.delete()
    elif "help+" in update.data:
        cb_data = update.data.split("+", -1)
