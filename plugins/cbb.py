from pyrogram import Client
from config import *

@Client.on_callback_query(filters.user(AUTH_USERS) if AUTH_USERS else None)
async def cb_handler(bot, update):
    if update.data == "home":
        await update.message.edit_text(
            text=START_BUTTONS.format(update.from_user.mention),
            reply_markup=START_BUTTONS,
            disable_web_page_preview=True
        )
    elif update.data == "help":
        await update.message.edit_text(
            text=HELP_TEXT,
            reply_markup=HELP_BUTTONS,
            disable_web_page_preview=True
        )
    elif update.data == "about":
        await update.message.edit_text(
            text=ABOUT_TEXT,
            reply_markup=ABOUT_BUTTONS,
            disable_web_page_preview=True
        )
    else:
        await update.message.delete()
