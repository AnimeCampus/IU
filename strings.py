from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup 
from Itachi import BOT_NAME,BOT_USERNAME,app
from Itachi.config import OWNER_ID, SUPPORT_CHAT,UPDATES_CHANNEL


PM_START_TEXT = """
────「 `{}` 」────
Hola[!](https://telegra.ph/file/32223c0ba9a062c36cfb2.jpg) {} ,
My Name Is Itachi Uchiha◎! ㅤ
➖➖➖➖➖➖➖➖➖➖➖➖➖➖
◍ I Am  a Group Management Bot , Built For Weebs.
‣ Uptime: {}
‣ Python: {}
‣ Pyrogram: {}
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
        InlineKeyboardButton(text="Help 🚨", callback_data="help_back"),
        InlineKeyboardButton(text="Support 🆘", url=f"t.me/{SUPPORT_CHAT}")
    ], 
    [
        InlineKeyboardButton(text="Music 🎶", callback_data="music_p"),
        InlineKeyboardButton(text="Ai 🤖", callback_data="ai_help")
    ], 
    [
        InlineKeyboardButton(
            text="☯️ Add Itachi To Group ☯️",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        ),
    ],     
]
GRP_START = [
    [
        InlineKeyboardButton(text="Updates", url=f"t.me/{UPDATES_CHANNEL}"),
        InlineKeyboardButton(text="Support", url=f"t.me/{SUPPORT_CHAT}")
    ], 
    [
       InlineKeyboardButton("System Stats",callback_data="Friday_st")
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
