# Author: Fayas (https://github.com/FayasNoushad) (@FayasNoushad)

import requests
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from config import *


API = "https://api.sumanjay.cf/covid/?country="


@Client.on_message(filters.command(["covid", "corona"]), group=1)
async def covid_info(update: Message):
    if len(update.text.split()) <= 1:
        await update.reply_text(
            text="Send command with country name",
            quote=True
        )
        return
    try:
        country = update.text.split(" ", 1)[1]
        country = country.replace(" ", "+")
        r = requests.get(API + country)
        info = r.json()
        country = info['country']
        active = info['active']
        confirmed = info['confirmed']
        deaths = info['deaths']
        info_id = info['id']
        last_update = info['last_update']
        latitude = info['latitude']
        longitude = info['longitude']
        recovered = info['recovered']
        covid_info = f"""--**Covid 19 Information**--

Country : `{country}`
Actived : `{active}`
Confirmed : `{confirmed}`
Deaths : `{deaths}`
ID : `{info_id}`
Last Update : `{last_update}`
Latitude : `{latitude}`
Longitude : `{longitude}`
Recovered : `{recovered}`"""
        await update.reply_text(
            text=covid_info,
            disable_web_page_preview=True,
            quote=True,
            reply_markup=BUTTONS
        )
    except Exception as error:
        await update.reply_text(
            text=error,
            disable_web_page_preview=True,
            quote=True
        )
