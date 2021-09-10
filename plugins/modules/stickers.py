from config import *
import os , glob
from os import error
from pyrogram import Client, filters
from pyrogram.types import Message, Sticker, Document

DOWNLOAD_LOCATION = os.environ.get("DOWNLOAD_LOCATION", "./DOWNLOADS/")


@Client.on_message(filters.command(["getsticker"]), group=1)
async def getstickers(bot: message):
       if message.reply_to_message.sticker is False:
        await tx.edit("Not a Sticker File!!")
       else :
          if message.reply_to_message is None: 
               tx =  await tx.edit("Reply to a Sticker File!")       
          else :
               if message.reply_to_message.sticker.is_animated:
                       await message.reply_text("Couldn't download animated stickers")
 
               elif message.reply_to_message.sticker.is_animated is False:        
                   try:
                       tx = await message.reply_text("Downloading...")
                       file_path = DOWNLOAD_LOCATION + f"{message.chat.id}.png"
                       await message.reply_to_message.download(file_path)   
                       await tx.edit("Downloaded")
                       await tx.edit("Uploading...")
                       await message.reply_document(file_path) 
                       os.remove(file_path)
                   except Exception as error:
                       print(error)
               else:
                      await message.reply_text("Something bad occurred!!")


@Client.on_message(filters.command(["findsticker"]), group=1)
async def findstickers(bot: message):
  try:
       if message.reply_to_message: 
          txt = await message.reply_text("Validating Sticker ID")
          stickerid = str(message.reply_to_message.text)
          chat_id = str(message.chat.id)
          await txt.delete()
          await bot.send_sticker(chat_id,f"{stickerid}")
       else:
          await message.reply_text("Please reply to a ID to get its STICKER.")
  except Exception as error:
        txt = await message.reply_text("Not a Valid File ID")

 
    
