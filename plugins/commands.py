from pyrogram import Client as FayasNoushad
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

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
