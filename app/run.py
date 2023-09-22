import threading
import logging
logging.basicConfig(level = logging.INFO)

from flask import Flask
from flask_autoindex import AutoIndex
from pyrogram import Client, idle

from config import Config
from bot_interface import PyrogramTelegramBotInterface

BROWSE_ROOT = 'files'
ARGS        = ('0.0.0.0', 5000)

app = Flask(__name__)
app.config.from_object(Config)
AutoIndex(app, browse_root = BROWSE_ROOT)

bot = PyrogramTelegramBotInterface(
    pyro_bot_client = Client(
        name        = app.config['TG_BOT_USERNAME'],
        api_id      = app.config['TG_API_ID'],
        api_hash    = app.config['TG_API_HASH'],
        bot_token   = app.config['TG_BOT_TOKEN'],
        in_memory   = True
    ), logger = app.logger, config = app.config
)
bot.start()


threading.Thread(
    target      = app.run,
    args        = ARGS,
    daemon      = True
).start()

idle()
