from Itachi import app
import requests
from pyrogram import *

@app.on_message(filters.command("ask"))
async def gpt(_,message):
    rep = await message.reply_text("💭")
    if len(message.text) < 1:
        return await rep.edit_text("**Give me a query too...**")
    text = message.text.split(maxsplit=1)[1]
    resp = requests.get("https://alphacoder-api.vercel.app/chatgpt" , params={"query":text})
    if resp.status_code == 200:
        return await rep.edit_text(resp.json())
    else:
        return await rep.edit_text("**Currently API is Down!**")


__help__ = """
**ChatGPT openai model**

**Commands**

♠ `/ask <query>` - retrieves text from chatgpt.

"""
__mod_name__ = "chatGPT"
    

  
