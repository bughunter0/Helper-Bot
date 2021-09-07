# Author: Fayas (https://github.com/FayasNoushad) (@FayasNoushad)

from pyrogram import Client, filters


@Client.on_message(filters.text & filters.private & filters.reply & filters.regex(r'https?://[^\s]+'))
async def attach(bot, update):
    await update.reply_text(
        text=f"[\u2063]({update.text}){update.reply_to_message.text}",
        reply_markup=update.reply_to_message.reply_markup
    )
