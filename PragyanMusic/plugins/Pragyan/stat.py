from pyrogram import filters, Client
from PragyanMusic import app
from PragyanMusic.utils.database import add_served_chat

# ------------------------------------------ #

@app.on_message(filters.command(["hi", "hii", "hello", "hui", "good", "gm", "ok", "bye", "welcome", "thanks"] ,prefixes=["/", "!", "%", ",", "", ".", "@", "#"]) & filters.group)
async def bot_check(_, message):
    chat_id = message.chat.id
    await add_served_chat(chat_id)

# ------------------------------------------ #
