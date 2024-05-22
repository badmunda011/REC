from pyrogram import Client, filters, enums
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, CallbackQuery
from pyrogram import Client, errors
from pyrogram.enums import ChatMemberStatus, ParseMode
from pyrogram.enums import ChatType
import asyncio
import os
import requests
from os import getenv
import traceback
from pyrogram.types import Message
from unidecode import unidecode
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
import random 
import time
import random
import logging
import platform
import psutil
from pyrogram import Client, filters
from pyrogram.types import Message
import asyncio


MAX_MESSAGE_LENGTH = 30
    
@app.on_edited_message(filters.group & ~filters.me)
async def handle_edited_messages(_, edited_message: Message):
    await delete_long_edited_messages(_, edited_message)

async def delete_long_edited_messages(client, edited_message: Message):
    if edited_message.text:
        if len(edited_message.text.split()) > 30:
            await edited_message.delete()
            AMBOT = await edited_message.reply_text(f"{edited_message.from_user.mention} ᴇᴅɪᴛ ᴍᴇꜱꜱᴇɢᴇ ɴᴏᴛ ᴀʟʟᴏᴡᴇᴅ ᴡɪᴛʜ ᴍᴇꜱꜱᴇɢᴇ ʟᴇɴɢᴛʜ 30+!")
            await asyncio.sleep(20)
            await AMBOT.delete()

@app.on_message(filters.group & ~filters.me)
async def handle_messages(_, message: Message):
    await delete_long_messages(_, message)

async def delete_long_messages(client, message: Message):
    if message.text:
        if len(message.text.split()) > MAX_MESSAGE_LENGTH:
            await message.delete()
            AMBOT = await message.reply_text(f"{message.from_user.mention} ʏᴏᴜʀ ᴍᴇꜱꜱᴇɢᴇ ʟᴇɴɢᴛʜ 30+ ᴛʜɪꜱ ɪꜱ ɴᴏᴛ ɴᴏᴛ ᴀʟʟᴏᴡᴇᴅ!")
            await asyncio.sleep(20)
            await AMBOT.delete()


api_id = 26480985 #--Add your Api Id here
api_hash = '56c935fae1c5c86ba5a3af655f8caa9d' #--Enter Api Hash Here

token = '71955940eGa8PZG-vIAx8_Ow' #--Enter Bot Token Here.

app = Client("my_bot", api_id=api_id, api_hash=api_hash, bot_token=token)
AM_PIC = [
    "https://graph.org/file/ed513284c18489abfaf5f.jpg",
    "https://graph.org/file/ed513284c18489abfaf5f.jpg",
    
]
ban_txt = """

➻ ʜᴇʟʟᴏ {} ʙᴀɴᴀʟʟ ʙᴏᴛ.

➻ ᴛʜɪꜱ ɪꜱ ᴍᴀᴅᴇ ꜰᴏʀ ᴍᴀꜱꜱ ɢʀᴏᴜᴘ ᴍᴇᴍʙᴇʀꜱ ʙᴀɴꜱ.

➻ ᴘᴏᴡᴇʀ ꜰᴜʟʟ ʙᴀɴ ꜱʏꜱᴛᴇᴍ

ᴘᴏᴡᴇʀ ʙʏ : @SuperBanSBots
"""
help_txt = """
» ꜰᴜᴄᴋᴀʟʟ ʙᴏᴛ ғᴇᴀᴛᴜʀᴇs.
"""
killall_txt = """
1. ᴀᴅᴅ ʏᴏᴜʀ ʙᴏᴛ ɪɴ ᴡʜɪᴄʜ ɢʀᴏᴜᴘ ᴍᴇᴍʙᴇʀꜱ ᴀʀᴇ ʙᴀɴ.
2. ᴍᴀᴋᴇ ᴀᴅᴍɪɴ ᴡɪᴛʜ ʙᴀɴ ʀɪɢʜᴛ ᴛʜᴇ ʙᴏᴛ.
3. ɴᴏᴡ ꜱᴇɴᴅ ᴍᴇꜱꜱᴇɢᴇ ɪɴ ɢʀᴏᴜᴘ : <code>hii</code>

ɴᴏᴡ ʙᴏᴛ ᴡɪʟʟ ᴡᴏʀᴋɪɴɢ ʙᴀɴ ᴍᴇᴍʙᴇʀꜱ ɪɴ ɢʀᴏᴜᴘ ✅.
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
            InlineKeyboardButton("ꜱᴜᴘᴇʀʙᴀɴ ʟᴏɢꜱ", url=f"https://t.me/SuperBanSBots"),    
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
            InlineKeyboardButton("ꜱᴜᴘᴇʀʙᴀɴ ʟᴏɢꜱ", url=f"https://t.me/SuperBanSBots"),    
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


emojis = ["👍", "👎", "❤️", "🔥", "🥰", "👏", "😁", "🤔", "🤯", "😱", "🤬", "😢", "🎉", "🤩", "🤮", "💩", "🙏", "👌", "🕊", "🤡", "🥱", "🥴", "😍", "🐳", "❤️‍🔥", "🌚", "🌭", "💯", "🤣", "⚡️", "🍌", "🏆", "💔", "🤨", "😐", "🍓", "🍾", "💋", "🖕", "😈", "😴", "😭", "🤓", "👻", "👨‍💻", "👀", "🎃", "🙈", "😇", "😨", "🤝", "✍️", "🤗", "🫡", "🎅", "🎄", "☃️", "💅", "🤪", "🗿", "🆒", "💘", "🙉", "🦄", "😘", "💊", "🙊", "😎", "👾", "🤷‍♂️", "🤷", "🤷‍♀️", "😡"]

app = Client("my_bot", api_id=api_id, api_hash=api_hash, bot_token=token)

@app.on_message()
async def react_to_message(client, message):
    chat_id = message.chat.id
    message_id = message.id
    
    # Choose a random emoji from the list
    random_emoji = random.choice(emojis)
    
    url = f'https://api.telegram.org/bot{token}/setMessageReaction'

    # Parameters for the request
    params = {
        'chat_id': chat_id,
        'message_id': message_id,
        'reaction': [{
            "type": "emoji",
            "emoji": random_emoji
        }]
    }

    response = requests.post(url, json=params)

    if response.status_code == 200:
        print("Reaction set successfully!")
        print("Response content:", response.content)
    else:
        print(f"Failed to set reaction. Status code: {response.status_code}")
        print("Response content:", response.content)
    


app.run()
