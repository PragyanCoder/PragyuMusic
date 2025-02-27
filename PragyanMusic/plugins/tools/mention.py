import asyncio
from pyrogram.enums import ChatType
from PragyanMusic import app
from pyrogram import filters
from PragyanMusic.utils.pragyanmusicban import admin_filter

SPAM_CHATS = []

@app.on_message(filters.command(["mention", "all"]) | (filters.regex(r"@all(.*)") & filters.group & admin_filter))
async def tag_all_users(_, message):
    replied = message.reply_to_message  
    text = message.text.split(" ", 1)[1] if len(message.text.split(" ", 1)) > 1 else ""
    
    if replied:
        SPAM_CHATS.append(message.chat.id)      
        usernum = 0
        usertxt = ""
        async for m in app.get_chat_members(message.chat.id): 
            if message.chat.id not in SPAM_CHATS:
                break       
            usernum += 1
            usertxt += f"\n⊚ [{m.user.first_name}](tg://user?id={m.user.id})\n"
            if usernum == 5:
                await replied.reply_text(f'{text}\n{usertxt}')
                await asyncio.sleep(2)
                usernum = 0
                usertxt = ""
        try:
            SPAM_CHATS.remove(message.chat.id)
        except Exception:
            pass
    else:
        SPAM_CHATS.append(message.chat.id)
        usernum = 0
        usertxt = ""
        async for m in app.get_chat_members(message.chat.id):       
            if message.chat.id not in SPAM_CHATS:
                break 
            usernum += 1
            usertxt += f"\n⊚ [{m.user.first_name}](tg://user?id={m.user.id})\n"
            if usernum == 5:
                await app.send_message(message.chat.id, f'{text}\n{usertxt}')
                await asyncio.sleep(2)
                usernum = 0
                usertxt = ""                          
        try:
            SPAM_CHATS.remove(message.chat.id)
        except Exception:
            pass        
           
@app.on_message(filters.command("tagoff") & ~filters.private)
async def cancelcmd(_, message):
    chat_id = message.chat.id
    if chat_id in SPAM_CHATS:
        try:
            SPAM_CHATS.remove(chat_id)
        except Exception:
            pass   
        return await message.reply_text("**ᴛᴀɢ ᴀʟʟ sᴜᴄᴄᴇssғᴜʟʟʏ sᴛᴏᴘᴘᴇᴅ!**")     
                                     
    else:
        await message.reply_text("**ɴᴏ ᴘʀᴏᴄᴇss ᴏɴɢᴏɪɴɢ!**")  
        return

@app.on_message(filters.command("sticker") & filters.reply & filters.photo)
async def convert_to_sticker(_, message):
    photo = message.reply_to_message.photo
    if not photo:
        return await message.reply_text("**Please reply to an image to convert it into a sticker.**")
    
    file_path = await message.reply_to_message.download()
    sticker = await app.send_sticker(message.chat.id, file_path)
    await message.reply_text("**Sticker created successfully!**")

@app.on_message(filters.command("kang") & filters.reply & filters.sticker)
async def kang_sticker(_, message):
    sticker = message.reply_to_message.sticker
    if not sticker:
        return await message.reply_text("**Please reply to a sticker to kang it.**")
    
    await app.send_sticker(message.chat.id, sticker.file_id)
    await message.reply_text("**Sticker kanged successfully!**")
