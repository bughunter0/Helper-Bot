from pyrogram import Client as FayasNoushad
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

START_TEXT = """
**Hello {} 😌
I am telegram developers bot.**

>> `I have more features for developers`

Made by @FayasNoushad
"""

HELP_TEXT = """
**Hey, Follow these steps:**

I am a developer helper bot. Use the commands below for more.

**Available Commands**

/start - Checking Bot Online
/help - For more help
/about - For more about me

>> **Please join my [updates channel](https://telegram.me/FayasNoushad) for more bots and updates and Please contact [Fayas](https://telegram.me/TheFayas) for reporting, bugs, requests, and suggestions.**

Made by @FayasNoushad
"""

ABOUT_TEXT = """
➠ **Bot :** ``Developers Bot` 🤖
➠ **Creator :** [Fayas](https://telegram.me/TheFayas)
➠ **Channel :** [Fayas Noushad](https://telegram.me/FayasNoushad)
➠ **Credits :** `Everyone in this journey`
➠ **Language :** [Python3](https://python.org)
➠ **Library :** [Pyrogram](https://pyrogram.org)
➠ **Server :** [Heroku](https://heroku.com)
"""

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

@FayasNoushad.on_message(filters.private & filters.command(["start"]))
async def start(bot, update):
    await update.reply_text(
        text=START_TEXT.format(update.from_user.mention),
        disable_web_page_preview=True,
	reply_markup=START_BUTTONS
    )

@FayasNoushad.on_message(filters.private & filters.command(["help"]))
async def help(bot, update):
    await update.reply_text(
        text=HELP_TEXT,
      	disable_web_page_preview=True,
	reply_markup=HELP_BUTTONS
    )

@FayasNoushad.on_message(filters.private & filters.command(["about"]))
async def about(bot, update):
    await update.reply_text(
        text=ABOUT_TEXT,
        disable_web_page_preview=True,
	reply_markup=ABOUT_BUTTONS
    )
