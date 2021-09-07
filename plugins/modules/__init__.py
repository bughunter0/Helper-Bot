# Made with python3
# (C) @FayasNoushad
# Copyright permission under MIT License
# All rights reserved by FayasNoushad
# License -> https://github.com/TelegramHelpBot/Helper-Bot/blob/main/LICENSE

from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


# "text" for adding text in module buttons.
# "help_text" for more information about module.
# "help_buttons" for extra buttons

MODULES = {
    "attach": {
        "text": "Attach",
        "help_text": "**Attach**\n\n- Just send a html or markdown message\n\n- Reply /attach with link for attaching",
        "help_buttons": []
    },
    "country": {
        "text": "Country Info",
        "help_text": "**Country Information**\n\nSend /country with country name for information of that country.\n\nLike :- `/country India`",
        "help_buttons": []
    },
    "covid": {
        "text": "Covid 19 Info",
        "help_text": "**Covid 19 Information**\n\n`For getting covid information of a country`\n\nSend /covid with country name like `/covid India`",
        "help_buttons": []
    },
    "info": {
        "text": "Information",
        "help_text": "**Information**\n\n`For getting user or chat information.`\n\nSend /info with user id\n\nForward a message from chat and reply /info",
        "help_buttons": []
    },
    "json": {
        "text": "Response Json",
        "help_text": "**Response Json**\n\n`For getting json response`\n\nSend /json command with reply a message.",
        "help_buttons": []
    }
}


@Client.on_message(filters.command(["modules"]), group=1)
async def modules_help(bot, update, cb=False):
    if cb and update.data.startswith("module+"):
        await modules_cb(bot, update)
        return
    text = "**Modules**"
    buttons = []
    for module in MODULES:
        button = InlineKeyboardButton(
            text=MODULES[module]["text"],
            callback_data="module+"+module
        )
        if len(buttons) == 0 or len(buttons[-1]) >= 2:
            buttons.append([button])
        else:
            buttons[-1].append(button)
    reply_markup = InlineKeyboardMarkup(buttons)
    if cb:
        await update.message.edit_text(
            text=text,
            reply_markup=reply_markup,
            disable_web_page_preview=True
        )
    else:
        await update.reply_text(
            text=text,
            reply_markup=reply_markup,
            disable_web_page_preview=True,
            quote=True
        )


@Client.on_message(filters.command(["module"]), group=1)
async def module_help(bot, update):
    try:
        module = update.text.split(" ", 1)[1].lower()
        await update.reply_text(
            text=MODULES[module]["help_text"],
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton(text="🔙 Back", callback_data="modules")]]
            ),
            quote=True
        )
    except Exception as error:
        print(error)


async def modules_cb(bot, update):
    module = update.data.split("+")[1]
    await update.message.edit_text(
        text=MODULES[module]["help_text"],
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton(text="🔙 Back", callback_data="modules")]]
        )
    )
