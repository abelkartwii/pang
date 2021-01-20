import os
import time
import configparser
import pylast

# You'll need your own values for API_KEY and API_SECRET
# Find them here https://www.last.fm/api/account

try:
    API_KEY = ""
    API_SECRET = ""
except KeyError:
    API_KEY = "your_key"
    API_SECRET = "your_secret"

API_URL = 'http://ws.audioscrobbler.com/2.0/'
