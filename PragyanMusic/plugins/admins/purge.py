from asyncio import sleep
from pyrogram import filters
from pyrogram.enums import ChatType
from pyrogram.errors import MessageDeleteForbidden, RPCError
from pyrogram.types import Message
from PragyanMusic.utils.pragyanmusicban import admin_filter
from PragyanMusic import app


@app.on_message(filters.command("purge") & admin_filter)
async def purge(app: app, msg: Message):
    
    if msg.chat.type != ChatType.SUPERGROUP:
        await msg.reply_text(text="**𝐈 𝐜𝐚𝐧𝐧𝐨𝐭 𝐏𝐮𝐫𝐠𝐞 𝐌𝐞𝐬𝐬𝐚𝐠𝐞𝐬 𝐢𝐧 𝐚 𝐁𝐚𝐬𝐢𝐜 𝐆𝐫𝐨𝐮𝐩 𝐌𝐚𝐤𝐞 𝐈𝐭 𝐚 𝐒𝐮𝐩𝐞𝐫 𝐆𝐫𝐨𝐮𝐩.**")
        return

    if msg.reply_to_message:
        message_ids = list(range(msg.reply_to_message.id, msg.id))

        def divide_chunks(l: list, n: int = 100):
            for i in range(0, len(l), n):
                yield l[i : i + n]

        
        m_list = list(divide_chunks(message_ids))

        try:
            for plist in m_list:
                await app.delete_messages(chat_id=msg.chat.id, message_ids=plist, revoke=True)
                
            await msg.delete()
        except MessageDeleteForbidden:
            await msg.reply_text(text="**𝐈 𝐜𝐚𝐧'𝐭 𝐝𝐞𝐥𝐞𝐭𝐞 𝐚𝐥𝐥 𝐦𝐞𝐬𝐬𝐚𝐠𝐞𝐬..**")
            return
            
        except RPCError as ef:
            await msg.reply_text(text=f"**𝐒𝐨𝐦𝐞 𝐞𝐫𝐫𝐨𝐫 𝐨𝐜𝐜𝐮𝐫𝐫𝐞𝐝,  <code>{ef}</code>")
        count_del_msg = len(message_ids)
        sumit = await msg.reply_text(text=f"𝐏𝐮𝐫𝐠𝐞𝐝  <i>{count_del_msg}</i> 𝐌𝐞𝐬𝐬𝐚𝐠𝐞𝐬")
        await sleep(3)
        await sumit.delete()
        return
    await msg.reply_text("**𝐑𝐞𝐩𝐥𝐲 𝐭𝐨 𝐚 𝐦𝐞𝐬𝐬𝐚𝐠𝐞 𝐭𝐨 𝐬𝐭𝐚𝐫𝐭 𝐩𝐮𝐫𝐠𝐞 !**")
    return





@app.on_message(filters.command("spurge") & admin_filter)
async def spurge(app: app, msg: Message):

    if msg.chat.type != ChatType.SUPERGROUP:
        await msg.reply_text(text="**𝐈 𝐜𝐚𝐧𝐧𝐨𝐭 𝐏𝐮𝐫𝐠𝐞 𝐌𝐞𝐬𝐬𝐚𝐠𝐞𝐬 𝐢𝐧 𝐚 𝐁𝐚𝐬𝐢𝐜 𝐆𝐫𝐨𝐮𝐩 𝐌𝐚𝐤𝐞 𝐈𝐭 𝐚 𝐒𝐮𝐩𝐞𝐫 𝐆𝐫𝐨𝐮𝐩.**")
        return

    if msg.reply_to_message:
        message_ids = list(range(msg.reply_to_message.id, msg.id))

        def divide_chunks(l: list, n: int = 100):
            for i in range(0, len(l), n):
                yield l[i : i + n]

        m_list = list(divide_chunks(message_ids))

        try:
            for plist in m_list:
                await app.delete_messages(chat_id=msg.chat.id, message_ids=plist, revoke=True)
            await msg.delete()
        except MessageDeleteForbidden:
            await msg.reply_text(text="**𝐈 𝐜𝐚𝐧'𝐭 𝐝𝐞𝐥𝐞𝐭𝐞 𝐚𝐥𝐥 𝐦𝐞𝐬𝐬𝐚𝐠𝐞𝐬.**")
            return
            
        except RPCError as ef:
            await msg.reply_text(text=f"**𝐒𝐨𝐦𝐞 𝐞𝐫𝐫𝐨𝐫 𝐨𝐜𝐜𝐮𝐫𝐫𝐞𝐝 <code>{ef}</code>")           
            return        
    await msg.reply_text("**𝐑𝐞𝐩𝐥𝐲 𝐭𝐨 𝐚 𝐦𝐞𝐬𝐬𝐚𝐠𝐞 𝐭𝐨 𝐬𝐭𝐚𝐫𝐭 𝐩𝐮𝐫𝐠𝐞 !**")
    return


@app.on_message(filters.command("del") & admin_filter)
async def del_msg(app: app, msg: Message):
    if msg.chat.type != ChatType.SUPERGROUP:
        await msg.reply_text(text="**𝐈 𝐜𝐚𝐧𝐧𝐨𝐭 𝐏𝐮𝐫𝐠𝐞 𝐌𝐞𝐬𝐬𝐚𝐠𝐞𝐬 𝐢𝐧 𝐚 𝐁𝐚𝐬𝐢𝐜 𝐆𝐫𝐨𝐮𝐩 𝐌𝐚𝐤𝐞 𝐈𝐭 𝐚 𝐒𝐮𝐩𝐞𝐫 𝐆𝐫𝐨𝐮𝐩.**")
        return        
    if msg.reply_to_message:
        await msg.delete()
        await app.delete_messages(chat_id=msg.chat.id, message_ids=msg.reply_to_message.id)
    else:
        await msg.reply_text(text="**𝐖𝐡𝐚𝐭 𝐝𝐨 𝐲𝐨𝐮 𝐰𝐚𝐧𝐭 𝐭𝐨 𝐝𝐞𝐥𝐞𝐭𝐞.**")
        return


