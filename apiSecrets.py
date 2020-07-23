from os import environ

API_KEY = environ.get("MEMESAVER_TWT_API_KEY")
API_SECRET = environ.get("MEMESAVER_TWT_API_SECRET")
ACCESS_TOKEN = environ.get("MEMESAVER_TWT_ACC_TKN")
ACCESS_SECRET = environ.get("MEMESAVER_TWT_ACC_SECRET")

client_id = environ.get("MEMESAVER_GDRIVE_CLIENT_ID")
client_secret = environ.get("MEMESAVER_GDRIVE_CLIENT_SECRET")