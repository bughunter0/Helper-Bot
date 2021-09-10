import ytthumb
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


@Client.on_message(
    filters.command(["ytthumb", "thumbnail"]),
    group=1
)
async def youtube_thumbnail(bot, update):
    reply_markup = InlineKeyboardMarkup(
        [[InlineKeyboardButton('Join Updates Channel', url='https://telegram.me/FayasNoushad')]]
    )
    if len(update.text.split()) == 1 or len(update.text.split()) >= 4:
        await update.reply_text(
            "Send command with youtube video link with quality ( optional )",
            quote=True,
            reply_markup=reply_markup
        )
    else:
        length = len(update.text.split())
        video = update.text.split()[1]
        if length == 2:
            thumbnail = ytthumb.thumbnail(video)
        else:
            quality = update.text.split()[2]
            thumbnail = ytthumb.thumbnail(video, quality)
        try:
            await update.reply_photo(
                thumbnail,
                quote=True,
                reply_markup=reply_markup
            )
        except Exception as error:
            await update.reply_text(
                text=error,
                disable_web_page_preview=True,
                reply_markup=reply_markup,
                quote=True
            )
            
