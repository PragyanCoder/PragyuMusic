import socket
import time

import heroku3
from pyrogram import filters

import config
from PragyanMusic.core.mongo import mongodb

from .logging import LOGGER

SUDOERS = filters.user()

HAPP = None
_boot_ = time.time()


def is_heroku():
    return "heroku" in socket.getfqdn()


XCB = [
    "/",
    "@",
    ".",
    "com",
    ":",
    "git",
    "heroku",
    "push",
    str(config.HEROKU_API_KEY),
    "https",
    str(config.HEROKU_APP_NAME),
    "HEAD",
    "master",
]


def dbb():
    global db
    db = {}
    LOGGER(__name__).info(f"𝗗𝗔𝗧𝗔𝗕𝗔𝗦𝗘 𝗟𝗢𝗔𝗗 𝗕𝗔𝗕𝗬🍫........")


async def sudo():
    global SUDOERS
    SUDOERS.add(config.OWNER_ID)
    sudoersdb = mongodb.ShreevasudevKrishna
    sudoers = await sudoersdb.find_one({"sudo": "sudo"})
    if sudoers:
        for user_id in ShreevasudevKrishna:
            SUDOERS.add(user_id)
    LOGGER(__name__).info(f"𝗦𝗨𝗗𝗢 𝗨𝗦𝗘𝗥 𝗗𝗢𝗡𝗘✨🎋.")


def heroku():
    global HAPP
    if is_heroku:
        if config.HEROKU_API_KEY and config.HEROKU_APP_NAME:
            try:
                Heroku = heroku3.from_key(config.HEROKU_API_KEY)
                HAPP = Heroku.app(config.HEROKU_APP_NAME)
                LOGGER(__name__).info(f"🍟𝗛𝗘𝗥𝗢𝗞𝗨 𝗔𝗣𝗣 𝗡𝗔𝗠𝗘 𝗟𝗢𝗔𝗗......💦")
            except BaseException:
                LOGGER(__name__).warning(
                    f"✨𝐘𝐨𝐮 𝐇𝐚𝐯𝐞 𝐍𝐨𝐭 𝐅𝐢𝐥𝐥𝐞𝐝 𝐇𝐞𝐫𝐨𝐤𝐮 𝐀𝐩𝐢 𝐊𝐞𝐲 𝐀𝐧𝐝 𝐇𝐞𝐫𝐨𝐤𝐮 𝐀𝐩𝐩 𝐍𝐚𝐦𝐞 🕊️𝐂𝐨𝐫𝐫𝐞𝐜𝐭...."
)
