# Author: Fayas (https://github.com/FayasNoushad) (@FayasNoushad)

from config import *
from pyrogram import Client, filters
from pyrogram.types import Message
from . import *


@Client.on_message(
    filters.private &
    filters.command(
        [
            "start",
            "help",
            "about"
        ]
    ) &
    filters.user(AUTH_USERS) if PRIVATE else None
)
async def command(bot: Client, update: Message):
    text = update.text
    if len(text.split()) == 1:
        if text == "/start":
            await start(update)
        elif text == "/help":
            await help(update)
        elif text == "/about":
            await about(bot, update)
    elif len(text.split()) > 1:
        text = text.split(" ", 1)[1]
        if text == "help":
            await help(update)
        elif text == "about":
            await about(bot, update)
