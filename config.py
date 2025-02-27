import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = 24648630
API_HASH = "2fb7a8358803a958d6993e73a5da136d"
# Get your token from @BotFather on Telegram.
BOT_TOKEN = "7701373418:AAGeQ9j3DKZhTODbDNaKMzwYCIeW9vuGK-k"
# Add Owner Username without @ 
OWNER_USERNAME = getenv("OWNER_USERNAME","Pragyan")
# Get Your bot username
BOT_USERNAME = getenv("BOT_USERNAME" , "PragyanMusicBot")
# Don't Add style font 
BOT_NAME = getenv("BOT_NAME" , "Pragyan Music")
#get Your Assistant User name
ASSUSERNAME = getenv("ASSUSERNAME" , "PragyanMusicAssistant")
EVALOP = list(map(int, getenv("EVALOP","8025794193").split()))

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = "mongodb+srv://PihuMusic:PihuMusic@cluster0.w3eiu.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
DEEP_API = getenv("DEEP_API","ef488aaf-e253-4cd9-b115-d24ece89a5c7")
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 9999999))

# Chat id of a group for logging bot's activities
LOGGER_ID = "@PRAGYANMUSICLOGS"

# Get this value from  on Telegram by /id
OWNER_ID = int(getenv("OWNER_ID", 8025794193))

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/CoderPragyan/PragyanMusic",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/VrindavanNeeko16007")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/AryavartChats")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "1c21247d714244ddbb09925dac565aed")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "709e1a2969664491b58200860623ef19")


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 5242880000))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes



STRING1 = getenv("STRING_SESSION", "BAF4G7YAMdo5LDDEQxfWoUSdEIeLWAW-zYj6P3UEsGYJ9uB8hTHImUoHt_BHfmYmLF8Gi8FEhXuuzUI7l3COnJAbhjL7bjYE60ACegAUCrujcqILWP89OF-Z_gfYHRDqGMd3esoTjZWLuuYnmzhoWjYmZWvBZTsKboh0pgVc9gArBU7r9fNL-XRbw1EndqueDCqjPw7BbUCBS5tnXpvyDqgEX3xcWPSZ4_LSyX5kCpjCgqmIIPHzcQosxIxPfixemA_OXabOaM4h3eXQhYX8y3kBqby3H4IzhYzRbSTWUh4X0fRJYxKPH0csKK_Qq8ghnSbcSTWk3UvDzqqEsquDk6xh9Y8PmQAAAAGmyq61AA")
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = getenv(
    "START_IMG_URL", "https://graph.org/file/b9463a0c5e01efec0c799-b1de962c295a265ea4.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://graph.org/file/b9463a0c5e01efec0c799-b1de962c295a265ea4.jpg"
)
PLAYLIST_IMG_URL = "https://graph.org/file/b9463a0c5e01efec0c799-b1de962c295a265ea4.jpg"
STATS_IMG_URL = "https://graph.org/file/b9463a0c5e01efec0c799-b1de962c295a265ea4.jpg"
TELEGRAM_AUDIO_URL = "https://graph.org/file/b9463a0c5e01efec0c799-b1de962c295a265ea4.jpg"
TELEGRAM_VIDEO_URL = "https://graph.org/file/b9463a0c5e01efec0c799-b1de962c295a265ea4.jpg"
STREAM_IMG_URL = "https://graph.org/file/b9463a0c5e01efec0c799-b1de962c295a265ea4.jpg"
SOUNCLOUD_IMG_URL = "https://graph.org/file/b9463a0c5e01efec0c799-b1de962c295a265ea4.jpg"
YOUTUBE_IMG_URL = "https://graph.org/file/b9463a0c5e01efec0c799-b1de962c295a265ea4.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://graph.org/file/b9463a0c5e01efec0c799-b1de962c295a265ea4.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://graph.org/file/b9463a0c5e01efec0c799-b1de962c295a265ea4.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://graph.org/file/b9463a0c5e01efec0c799-b1de962c295a265ea4.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
