import os
from gtts import gTTS, gTTSError
from Itachi import telethn as tbot
from Itachi.events import register


@register(pattern="^/tts (.*)")
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    reply_to_id = event.message.id
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        text = previous_message.message
        lan = input_str
    elif "|" in input_str:
        lan, text = input_str.split("|")
    else:
        await event.reply("Invalid syntax\nFor eg: `/tts en | hello`")
        return
    text = text.strip()
    lan = lan.strip()
    try:
        tts = gTTS(text, tld="com", lang=lan)
        tts.save("k.mp3")
    except AssertionError:
        await event.reply(
            "The text is empty.\n"
            "nothing left to speak after pre-precessing,"
            "tokenizing and cleaning."
        )
        return
    except ValueError:
        await event.reply("language is not supported.")
        return
    except RuntimeError:
        await event.reply("error landing the languages dictionary.")
        return
    except gTTSError:
        await event.reply("error in google to speech api request!")
        return
    with open("k.mp3", "r"):
        await tbot.send_file(
            event.chat_id, "k.mp3", voice_note=True, reply_to=reply_to_id
        )
        os.remove("k.mp3")


__help__ = """

⍟ /tts hi|hello  *:* Text to speech


"""

__mod_name__ = "Text to speech 🗣"
