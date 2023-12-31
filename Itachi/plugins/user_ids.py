from Itachi import app
from Itachi.modules.pyro.decorators import control_user
import random
from pyrogram import filters , Client

ITACHI_PIC = "https://telegra.ph/file/64eab10c10b0242004b86.jpg"

@Client.on_message(filters.command("id") & filters.group)
@control_user()
async def _iSd(client, message):
    chat = message.chat
    your_id = message.from_user.id
    mention_user = message.from_user.mention
    message_id = message.id
    reply = message.reply_to_message

    text = f"**♣ [Message ID]({message.link})** › `{message_id}`\n"
    text += f"**♣ [{mention_user}](tg://user?id={your_id})** › `{your_id}`\n"

    if not message.command:
        message.command = message.text.split()
        
    if not message.command:
        message.command = message.text.split()

    if len(message.command) == 2:
        try:
            split = message.text.split(None, 1)[1].strip()
            user_id = (await client.get_users(split)).id
            user_mention = (await client.get_users(split)).mention 
            text += f"**• [{user_mention}](tg://user?id={user_id})** » `{user_id}`\n"

        except Exception:
            return await message.reply_text("**User Not Found!**")

    text += f"**• [Chat ID](https://t.me/{chat.username})** › `{chat.id}`\n\n"

    if not getattr(reply, "empty", True) and not message.forward_from_chat and not reply.sender_chat:
        text += (
            f"**• [Replied Message ID]({reply.link})** › `{message.reply_to_message.id}`\n"
        )
        text += f"**• [Replied User ID](tg://user?id={reply.from_user.id})** › `{reply.from_user.id}`\n\n"

    if reply and reply.forward_from_chat:
        text += f"**• Forwarded Channel {reply.forward_from_chat.title}\nID :** `{reply.forward_from_chat.id}`\n\n"        
    
    if reply and reply.sender_chat:
        text += f"**• Chat ID :** `{reply.sender_chat.id}`"
        
    await message.reply_photo(
       photo = ITACHI_PIC,
       caption=text)
      
@Client.on_message(filters.command("id") & filters.private)
@control_user()
async def _id(client, message):
    chat = message.chat
    your_id = message.from_user.id
    mention_user = message.from_user.mention
    message_id = message.id
    reply = message.reply_to_message

    text = f"**♣ [Message ID]({message.link})** › `{message_id}`\n"
    text += f"**♣ [{mention_user}](tg://user?id={your_id})** › `{your_id}`\n"

    if not message.command:
        message.command = message.text.split()
        
    if not message.command:
        message.command = message.text.split()

    if len(message.command) == 2:
        try:
            split = message.text.split(None, 1)[1].strip()
            user_id = (await client.get_users(split)).id
            user_mention = (await client.get_users(split)).mention 
            text += f"**• [{user_mention}](tg://user?id={user_id})** » `{user_id}`\n"

        except Exception:
            return await message.reply_text("**User Not Found!**")

    text += f"**• [Chat ID](https://t.me/{chat.username})** › `{chat.id}`\n\n"

    if not getattr(reply, "empty", True) and not message.forward_from_chat and not reply.sender_chat:
        text += (
            f"**• [Replied Message ID]({reply.link})** › `{message.reply_to_message.id}`\n"
        )
        text += f"**• [Replied User ID](tg://user?id={reply.from_user.id})** › `{reply.from_user.id}`\n\n"

    if reply and reply.forward_from_chat:
        text += f"**• Forwarded Channel {reply.forward_from_chat.title}\nID :** `{reply.forward_from_chat.id}`\n\n"        
    
    if reply and reply.sender_chat:
        text += f"**• Chat ID :** `{reply.sender_chat.id}`"
        
    await message.reply_photo(
       photo = ITACHI_PIC,
       caption=text)
      
