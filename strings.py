from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup 
from Itachi import BOT_NAME,BOT_USERNAME,app
from Itachi.config import OWNER_ID, SUPPORT_CHAT,UPDATES_CHANNEL


PM_START_TEXT = """
────「 `{}` 」────
Hola[!](https://telegra.ph/file/32223c0ba9a062c36cfb2.jpg) {} ,
My Name Is Itachi Uchiha◎! ㅤ
➖➖➖➖➖➖➖➖➖➖➖➖➖➖
◍ I Am  a Group Management Bot , Built For Weebs.
➖➖➖➖➖➖➖➖➖➖➖➖➖➖
◍ I Am Specialized In Managing Groups Of Anime Communities⚝!
"""

SUPPORT_SEND_MSG = """
**Itachi Uchiha !**
**Python Version:** `{}`
**Pyrogram Version:** `{}`
**UpTime:** `{}`
"""

LOG_MSG = "Itachi Uchiha Started ✨"

HELP_STRINGS = f"""
Hey there! My name is Itachi Uchiha.

Main commands available:

• Click on the button bellow to get description about specifics pcommand.
• If You Face Any Problems Please Report It To Our Support Group.
• /help <Module Name>: PM's you info about that module.
• Click on below buttons to access commands of {BOT_NAME}.
"""

START_BUTTONS = [
    [
        InlineKeyboardButton(text="𝙃𝙚𝙡𝙥 𝘼𝙣𝙙 𝘾𝙤𝙢𝙢𝙖𝙣𝙙𝙨 🚨", callback_data="help_back")
    ],
    [      
        InlineKeyboardButton(text="𝙐𝙥𝙙𝙖𝙩𝙚 𝘾𝙝𝙖𝙣𝙣𝙚𝙡 🆘", url=f"t.me/{UPDATES_CHANNEL}"),
        InlineKeyboardButton(text="𝙎𝙪𝙥𝙥𝙤𝙧𝙩 𝙂𝙧𝙤𝙪𝙥 🆘", url=f"t.me/{SUPPORT_CHAT}")
    ], 
    [
        InlineKeyboardButton(text="𝙊𝙪𝙧 𝙉𝙚𝙩𝙬𝙤𝙧𝙩 🎶", url=f"https://t.me/Emperors_Network"),
        InlineKeyboardButton(text="𝘼𝙞 🤖", callback_data="ai_help")
    ], 
    [
        InlineKeyboardButton(
            text="☯️ 𝘼𝙙𝙙 𝙄𝙩𝙖𝙘𝙝𝙞 𝙏𝙤 𝙈𝙖𝙣𝙖𝙜𝙚 𝙔𝙤𝙪𝙧 𝙂𝙧𝙤𝙪𝙥 ☯️",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        ),
    ],     
]
GRP_START = [
    [
        InlineKeyboardButton(text="𝙐𝙥𝙙𝙖𝙩𝙚𝙨", url=f"t.me/{UPDATES_CHANNEL}"),
        InlineKeyboardButton(text="𝙎𝙪𝙥𝙥𝙤𝙧𝙩", url=f"t.me/{SUPPORT_CHAT}")
    ], 
    [
       InlineKeyboardButton("𝙎𝙮𝙨𝙩𝙚𝙢 𝙎𝙩𝙖𝙩𝙨",callback_data="Friday_st")
    ],
]
BACK_BTN = [[InlineKeyboardButton("🔙",callback_data="friday_back")]]
MUSIC_BTN = [
    [
        InlineKeyboardButton(text="Admin Commands 🐥", callback_data="admin_music"),
        InlineKeyboardButton(text="Play Commands 🍼", callback_data="play_music")
    ], 
    [
       InlineKeyboardButton("Back 🔙",callback_data="friday_back")
    ],
]
MUSIC_BACK =  [[InlineKeyboardButton("🔙",callback_data="m_back")]]
