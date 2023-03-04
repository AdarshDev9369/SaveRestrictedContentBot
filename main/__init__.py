#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = config("4069594", default=None, cast=int)
API_HASH = config("3badefa1852d129109faa0d4d69ed251", default=None)
BOT_TOKEN = config("6171876157:AAGCuo8jSiKq-k3lVhDtnEOFr14vcxnvvKM", default=None)
SESSION = config("BQC-S5ZZ7HMwPCdkDUTK3nmzqqCuB72UojoaFxwInmkqCaLH_jg68g1Q5pm5bsTd8sYEA8Mt6z_VgBirBsIp1Dy5ARhRoBleZeKhXZ2e9liCn8jMBf0NPouNyneWiXnvb7aDD1SHLJJmbPZX9awuE0PsZzojQNgIqKj4FS95VWfecnkHh6Or6UTBvPyN03YY_Y-JvotsGSl6H50pXpakFFHxfADaKQqDWIlTdXTpLfICIMqWdTuTI8VW2ERMfFPY3PJRt4dSfXFbbUEFQXYgLlZt58ZqWOLsVr-LWNLNAmxZNGAJ5Mf_3_n6v0gUUTGBfIhOQdznZ8EYFs8oKaqjjCSPOiphEAA", default=None)
FORCESUB = config("ADARSH_TELEGRAM_BOTS", default=None)
AUTH = config("975855888", default=None, cast=int)

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client(
    session_name=SESSION, 
    api_hash=API_HASH, 
    api_id=API_ID)

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
