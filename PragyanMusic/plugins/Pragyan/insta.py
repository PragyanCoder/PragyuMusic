from pyrogram import Client, filters
import requests
from PragyanMusic import app
import config
from config import *

@app.on_message(filters.command("insta"))
async def download_instagram_reel(client, message):
    try:
        if len(message.text.split(" ")) == 1:
            await message.reply_text("Please provide an Instagram link after the command.")
            return
        
        url = message.text.split(" ", 1)[1]
        response = requests.post(f"https://api.qewertyy.dev/downloaders/instagram?url={url}")
        
        if response.status_code == 200:
            data = response.json()
            if "content" in data and len(data["content"]) > 0:
                video_url = data["content"][0]["url"]
                await message.reply_video(video_url)
            else:
                await message.reply_text("No content found in the response.")
        else:
            await message.reply_text(f"Request failed with status code: {response.status_code}")
    except Exception as e:
        await message.reply_text(f"Something went wrong: {e}")
