# Author: Fayas (https://github.com/FayasNoushad) (@FayasNoushad)

import os
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


BOT_TOKEN = os.environ["BOT_TOKEN"]
API_ID = int(os.environ["API_ID"])
API_HASH = os.environ["API_HASH"]
AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "").split())
PRIVATE = os.environ.get("PRIVATE", "")

COVID_API = "https://api.sumanjay.cf/covid/?country="

START_TEXT = """**Hello {} 😌
I am telegram developers bot.**

>> `I have more features for developers`

Made by @FayasNoushad"""

HELP_TEXT = """**Hey, Follow these steps:**

I am a developer helper bot. Use the commands below for more.

**Available Commands**

/start - Checking Bot Online
/help - For more help
/about - For more about me

Made by @FayasNoushad"""

ABOUT_TEXT = """**About Me**--

➠ **Bot :** [Developers Bot]({}) 🤖
➠ **Creator :** [Fayas](https://telegram.me/TheFayas)
➠ **Channel :** [Fayas Noushad](https://telegram.me/FayasNoushad)
➠ **Credits :** `Everyone in this journey`
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
