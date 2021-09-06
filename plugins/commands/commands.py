# Author: Fayas (https://github.com/FayasNoushad) (@FayasNoushad)

from pyrogram import Client, filters
from plugins.commands import *


@Client.on_message(
    filters.private &
    filters.command &
    filters.user(AUTH_USERS) if PRIVATE else None
)
async def command(bot, update):
    text = update.text
    if len(text.split()) == <= 1:
        if text == "/start":
            await start(bot, update)
        elif text == "/help":
            await help(bot, update)
        elif text == "/about":
            await about(bot, update)
        else:
            await modules(bot, update)
    elif len(text.split()) > 1:
        text = text.split(" ", 1)[1]
        if text == "help":
            await help(bot, update)
        elif text == "about":
            await about(bot, update)
        else:
            await modules(bot, update)
