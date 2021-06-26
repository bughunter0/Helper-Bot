from pyrogram import Client, filters
from ..commands import *

@Client.on_message(filters.private & filters.command(["start"]) & filters.user(AUTH_USERS) if AUTH_USERS else None)
async def start_command(bot, update):
