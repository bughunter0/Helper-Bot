import requests
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import *

@Client.on_message(filters.command(["covid_info", "corona_info"]) & filters.user(AUTH_USERS) if AUTH_USERS else None)
async def covid_info(bot, update):
    try:
        country = update.text.split(" ", -1)
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
        covid_info = f"""
--**Covid 19 Information**--
Country : `{country}`
Actived : `{active}`
Confirmed : `{confirmed}`
Deaths : `{deaths}`
ID : `{info_id}`
Last Update : `{last_update}`
Latitude : `{latitude}`
Longitude : `{longitude}`
Recovered : `{recovered}`
Made by @FayasNoushad
"""
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