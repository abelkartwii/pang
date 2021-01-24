import configparser
import pylast
from pathlib import Path

# You'll need your own values for API_KEY and API_SECRET
# Find them here https://www.last.fm/api/account

config = configparser.ConfigParser()
config.read_file(open(f"{Path(__file__).parents[0]}/config.cfg"))

api_key = config['KEYS']['API_KEY']
api_secret = config['KEYS']['API_SECRET']
headers = {api_key : api_key}