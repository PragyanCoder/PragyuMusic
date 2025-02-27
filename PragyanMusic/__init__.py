from PragyanMusic.core.bot import PragyanMusic
from PragyanMusic.core.dir import dirr
from PragyanMusic.core.git import git
from PragyanMusic.core.userbot import Userbot
from PragyanMusic.misc import dbb, heroku

from SafoneAPI import SafoneAPI
from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = PragyanMusic()
api = SafoneAPI()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
