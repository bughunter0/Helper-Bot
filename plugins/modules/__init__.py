# Made with python3
# (C) @FayasNoushad
# Copyright permission under MIT License
# All rights reserved by FayasNoushad
# License -> https://github.com/TelegramHelpBot/Helper-Bot/blob/main/LICENSE

from .modules import country, covid
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
    }
}
