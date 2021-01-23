import configparser
import pylast
import argparse
from pathlib import Path
from lastfm import LastFM
from queries import *
from database import Database

config = configparser.ConfigParser()
config.read_file(open(f"{Path(__file__).parents[0]}/config.cfg"))

parser = argparse.ArgumentParser(description = 'Last.fm tracker based on song, artist, album, and more.')

API_KEY = config['KEYS']['API_KEY']
API_SECRET = config['KEYS']['API_SECRET']

def main():
    args = parser.parse_args()
    pang = LastFM(song = args.song, artist = args.artist, album = args.album)
    db = Database()
    db.setup()

if __name__ == "__main__":
    required = parser.add_argument_group('required arguments')
    optional = parser.add_argument_group('optional arguments')
    required.add_argument("-s", "--song", required = True, help = "Type the song title", nargs = '+')
    required.add_argument("-a", "--artist", required = True, help = "Type the artist", nargs = '+')
    optional.add_argument("-al", "--album", required = False)
    main()