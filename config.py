# Author: Fayas (https://github.com/FayasNoushad) (@FayasNoushad)

import os
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


BOT_TOKEN = os.environ["BOT_TOKEN"]
API_ID = int(os.environ["API_ID"])
API_HASH = os.environ["API_HASH"]
BOT_OWNER = int(os.environ.get("BOT_OWNER", ""))
AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "").split())
PRIVATE = bool(os.environ.get("PRIVATE", False))

START_TEXT = """**Hello {} 😌
I am telegram helper bot.**

>> `I have more features for users`

Made by @FayasNoushad"""

HELP_TEXT = """**Hey, Follow these steps:**

I am an user helper bot. Use the commands below for more.

**Available Commands**

/start - Checking Bot Online
/help - For more help
/about - For more about me
/modules - For more modules

Made by @FayasNoushad"""

ABOUT_TEXT = """**About Me**--

➠ **Bot :** [Developers Bot]({}) 🤖
➠ **Creator :** [Fayas](https://telegram.me/TheFayas)
➠ **Channel :** [Fayas Noushad](https://telegram.me/FayasNoushad)
➠ **Credits :** `Everyone in this journey`
➠ **Source Code :** [Helper-Bot](https://github.com/TelegramHelpBot/Helper-Bot)
➠ **Language :** [Python3](https://python.org)
➠ **Library :** [Pyrogram](https://pyrogram.org)
➠ **Server :** [Heroku](https://heroku.com)"""

START_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('⚙ Help', callback_data='help'),
        InlineKeyboardButton('About 🔰', callback_data='about'),
        InlineKeyboardButton('Close ✖️', callback_data='close')
        ]]
    )

HELP_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Modules', callback_data='modules')
        ],[
        InlineKeyboardButton('🏘 Home', callback_data='home'),
        InlineKeyboardButton('About 🔰', callback_data='about'),
        InlineKeyboardButton('Close ✖️', callback_data='close')
        ]]
    )

ABOUT_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('🏘 Home', callback_data='home'),
        InlineKeyboardButton('Help ⚙', callback_data='help'),
        InlineKeyboardButton('Close ✖️', callback_data='close')
        ]]
    )

BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('⚙ Join Updates Channel ⚙', url='https://telegram.me/FayasNoushad')
        ]]
    )
