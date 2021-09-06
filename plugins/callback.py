# Author: Fayas (https://github.com/FayasNoushad) (@FayasNoushad)

from pyrogram import Client
from .commands import *
from .modules import modules


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
    elif "module+" in update.data:
        await modules(bot, update, cb=True)
