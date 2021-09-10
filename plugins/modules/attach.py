# Author: Fayas (https://github.com/FayasNoushad) (@FayasNoushad)

from pyrogram import Client, filters
from pyrogram.types import Message


@Client.on_message(filters.command(["attach"]) & filters.reply, group=1)
async def attach(update: Message):
    if len(update.text.split()) <= 1:
        await update.reply_text("Send command with link for attaching")
        return
    link = update.text.split(" ", 1)[1]
    await update.reply_text(
        text=f"[\u2063]({link}){update.reply_to_message.text}",
        reply_markup=update.reply_to_message.reply_markup
    )
