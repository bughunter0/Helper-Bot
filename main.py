import os
import pyrogram
from pyrogram import Client, filters

plugins = dict(root="plugins")

FayasNoushad = Client(
    "Developers-Bot",
    bot_token = Config.BOT_TOKEN,
    api_id = Config.API_ID,
    api_hash = Config.API_HASH,
    plugins = plugins
)

FayasNoushad.run()
