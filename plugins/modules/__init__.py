# Made with python3
# (C) @FayasNoushad
# Copyright permission under MIT License
# All rights reserved by FayasNoushad
# License -> https://github.com/TelegramHelpBot/Helper-Bot/blob/main/LICENSE

from plugins.modules import country, covid, info, json
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


MODULES = {
    "country": {
        "text": "Country Info",
        "help_text": country.TEXT,
        "help_buttons": country.BUTTONS
    },
    "covid": {
        "text": "Covid 19 Info",
        "help_text": covid.TEXT,
        "help_buttons": covid.BUTTONS
    },
    "info": {
        "text": "Information",
        "help_text": info.TEXT,
        "help_buttons": info.BUTTONS
    },
    "json": {
        "text": "Json",
        "help_text": json.TEXT,
        "help_buttons": json.BUTTONS
    }
}


async def modules_help(bot, update, cb=False):
    buttons = []
    for module in MODULES:
        buttons.append(
            InlineKeyboardButton(
                text=MODULES[module]["text"],
                callback_data="module"+module
            )
        )
