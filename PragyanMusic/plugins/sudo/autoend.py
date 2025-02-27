from pyrogram import filters
from pyrogram.types import Message

from PragyanMusic import app
from PragyanMusic.misc import SUDOERS
from PragyanMusic.utils.database import autoend_off, autoend_on


@app.on_message(filters.command("autoend") & SUDOERS)
async def auto_end_stream(_, message: Message):
    usage = "<b>ᴇxᴀᴍᴘʟᴇ :</b>\n\n/autoend [𝐄𝐧𝐚𝐛𝐥𝐞 | 𝐃𝐢𝐬𝐚𝐛𝐥𝐞]"
    if len(message.command) != 2:
        return await message.reply_text(usage)
    state = message.text.split(None, 1)[1].strip().lower()
    if state == "enable":
        await autoend_on()
        await message.reply_text(
            "» 𝐀𝐮𝐭𝐨 𝐞𝐧𝐝 𝐬𝐭𝐫𝐞𝐚𝐦 𝐞𝐧𝐚𝐛𝐥𝐞𝐝.\n\n𝐀𝐬𝐬𝐢𝐬𝐭𝐚𝐧𝐭 𝐰𝐢𝐥𝐥 𝐚𝐮𝐭𝐨𝐦𝐚𝐭𝐢𝐜𝐚𝐥𝐥𝐲 𝐥𝐞𝐚𝐯𝐞 𝐭𝐡𝐞 𝐯𝐢𝐝𝐞𝐨𝐜𝐡𝐚𝐭 𝐚𝐟𝐭𝐞𝐫 𝐟𝐞𝐰 𝐦𝐢𝐧𝐬 𝐰𝐡𝐞𝐧 𝐧𝐨 𝐨𝐧𝐞 𝐢𝐬 𝐥𝐢𝐬𝐭𝐞𝐧𝐢𝐧𝐠.."
        )
    elif state == "disable":
        await autoend_off()
        await message.reply_text("» 𝐀𝐮𝐭𝐨 𝐞𝐧𝐝 𝐬𝐭𝐫𝐞𝐚𝐦 𝐝𝐢𝐬𝐚𝐛𝐥𝐞𝐝.")
    else:
        await message.reply_text(usage)
