# Author: Fayas (https://github.com/FayasNoushad) (@FayasNoushad)

from config import *
from pyrogram import Client
from pyrogram.types import CallbackQuery
from .commands import *
from .modules import modules_cb


@Client.on_callback_query(
    filters.user(AUTH_USERS) if PRIVATE else None
)
async def cb_handler(bot: Client, update: CallbackQuery):
    if update.data == "home":
        await start(update, cb=True)
    elif update.data == "help":
        await help(update, cb=True)
    elif update.data == "about":
        await about(bot, update, cb=True)
    elif update.data == "close":
        await update.message.delete()
    elif update.data.startswith("module+"):
        await modules_cb(update)
    elif update.data.startswith("modules"):
        await modules_cb(update, cb=True)
