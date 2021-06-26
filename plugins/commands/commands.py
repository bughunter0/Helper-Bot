from pyrogram import Client, filters
from plugins.commands import *

@Client.on_message(
    filters.private &
    filters.command(
        [
            "start",
            "help",
            "about"
        ]
    ) &
    filters.user(AUTH_USERS) if AUTH_USERS else None
)
async def command(bot, update):
    text = update.text
    if text == "/start":
        await start(bot, update)
    else:
        text = text.split(" ", -1) if " " in text else text
        else:
            text = text
        if "help" in text:
            await help(bot, update)
        if "about" in text:
            await about(bot, update)
