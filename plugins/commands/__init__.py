# Author: Fayas (https://github.com/FayasNoushad) (@FayasNoushad)

from config import *
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


async def start(update, cb=False):
    text=START_TEXT.format(update.from_user.mention)
    if cb:
        await update.message.edit_text(text=text, disable_web_page_preview=True, reply_markup=START_BUTTONS)
    else:
        await update.reply_text(text=text, disable_web_page_preview=True, quote=True, reply_markup=START_BUTTONS)


async def help(update, cb=False):
    if cb:
        await update.message.edit_text(text=HELP_TEXT, disable_web_page_preview=True, reply_markup=HELP_BUTTONS)
    else:
        await update.reply_text(text=HELP_TEXT, disable_web_page_preview=True, quote=True, reply_markup=HELP_BUTTONS)


async def about(bot, update, cb=False):
    text = ABOUT_TEXT.format((await bot.get_me()).username)
    if cb:
        await update.message.edit_text(text=text, disable_web_page_preview=True, reply_markup=ABOUT_BUTTONS)
    else:
        await update.reply_text(text=text, disable_web_page_preview=True, quote=True, reply_markup=ABOUT_BUTTONS)
