# Author: Fayas (https://github.com/FayasNoushad) (@FayasNoushad)

from pyrogram import Client, filters
from io import BytesIO
from config import *


@Client.on_message(filters.command(["json", "response"]), group=1)
async def response_json(update):
    json = update.reply_to_message
    with BytesIO(str.encode(str(json))) as json_file:
        json_file.name = "json.text"
        await json.reply_document(
            document=json_file,
            reply_markup=BUTTONS,
            quote=True
        )
        try:
            os.remove(json_file)
        except:
            pass
