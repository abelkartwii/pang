import configparser
import pylast
import argparse
from pathlib import pathlib
from queries import *
from database import *

config = configparser.ConfigParser()
config.read('config.cfg')

parser = argparse.ArgumentParser(description = 'Last.fm tracker based on song, artist, album, and more.')

api_key = config['KEYS']['API_KEY']
api_secret = config['KEYS']['API_SECRET']

if __name__ == "__main__":
    main()