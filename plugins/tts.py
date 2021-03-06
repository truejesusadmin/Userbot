from pyrogram import Client, filters
from .utils.utils import modules_help

from gtts import gTTS
from io import BytesIO


@Client.on_message(filters.command('tts', ['.']) & filters.me)
def tts(client, message):
    lang = message.command[1]
    text =  ' '.join(message.command[2:])
    message.edit('<code>Speech synthesis...</code>')
    tts = gTTS(text, lang=lang)
    voice = BytesIO()
    tts.write_to_fp(voice)
    voice.name = 'voice.ogg'
    message.delete()
    client.send_audio(message.chat.id, voice)


modules_help.update({'tts': '''<b>Help for |Covid|\nUsage:</b>
<code>.tts [lang] [text]</code>
<b>[Say text]</b>''', 'tts module': '<b>• Tts</b>:<code> tts</code>\n'})
