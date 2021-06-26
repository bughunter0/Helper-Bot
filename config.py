import os

class Config(object):
    BOT_TOKEN = os.environ["BOT_TOKEN"]
    API_ID = int(os.environ["API_ID"])
    API_HASH = os.environ["API_HASH"]
