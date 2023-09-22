import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

class Config:
    TG_API_ID       = os.environ.get('TG_API_ID')
    TG_API_HASH     = os.environ.get('TG_API_HASH')
    TG_BOT_TOKEN    = os.environ.get('TG_BOT_TOKEN')
    TG_BOT_USERNAME = os.environ.get('TG_BOT_USERNAME')
    URL_PAGE        = os.environ.get('URL_PAGE')