import configparser
import pylast
from pathlib import Path

# You'll need your own values for API_KEY and API_SECRET
# Find them here https://www.last.fm/api/account

config = configparser.ConfigParser()
config.read_file(open(f"{Path(__file__).parents[0]}/config.cfg"))

API_KEY = config['KEYS']['API_KEY']
API_SECRET = config['KEYS']['API_SECRET']
headers = {'Authorization': API_KEY}

'''
try:
    API_KEY = os.environ[""]
    API_SECRET = os.environ[""]
except KeyError:
    API_KEY = "your_key"
    API_SECRET = "your_secret"
'''
# API_URL = 'http://ws.audioscrobbler.com/2.0