# Made with python3
# (C) @FayasNoushad
# Copyright permission under MIT License
# All rights reserved by FayasNoushad
# License -> https://github.com/TelegramHelpBot/Helper-Bot/blob/main/LICENSE

from . import country, covid, info, json
from .country import country
from .covid import covid_info
from .info import information
from .json import response_json
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


MODULES = {
    "country": {
        "text": "Country Info",
        "help_text": """**Country Information**

Send /country with country name for information of that country.

Like :- `/country India`""",
        "help_buttons": []
    },
    "covid": {
        "text": "Covid 19 Info",
        "help_text": """**Covid 19 Information**

`For getting covid information of a country`

Send /covid with country name like `/covid India`""",
        "help_buttons": []
    },
    "info": {
        "text": "Information",
        "help_text": """**Information**

`For getting user or chat information.`

Send /info with user id
Forward a message from chat and reply /info""",
        "help_buttons": []
    },
    "json": {
        "text": "Json",
        "help_text": """**Json**

`For getting json response`

Send /json command with reply a message.""",
        "help_buttons": []
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


async def modules_commands(bot, update):
    command = update.text
    if command.startswith("/country"):
        await country(bot, update)
    elif command.startswith("/covid"):
        await covid_info(bot, update)
    elif command.startswith("/info"):
        await information(bot, update)
    elif command.startswith("/json"):
        await response_json(bot, update)
