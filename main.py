import configparser
import pylast
import argparse
from pathlib import Path
from lastfm import LastFM
from queries import *
from database import Database

# reads api_key and api_secret from config
config = configparser.ConfigParser()
config.read_file(open(f"{Path(__file__).parents[0]}/config.cfg"))
API_KEY = config['KEYS']['API_KEY']
API_SECRET = config['KEYS']['API_SECRET']

parser = argparse.ArgumentParser(description = 'Last.fm charts: global and per country.')

def to_string(data):
    # converts values in data to string
    return [str(value) for value in data.values()]

def main():
    # sets up variables
    args = parser.parse_args()
    pang = LastFM(country = args.country, user = args.user)
    db = Database()
    db.setup()

    # queries for the database
    queries = [insert_lastfm_table.format(*to_string(result)) for result in pang.get_results()]
    query_to_execute = "BEGIN; \n" + '\n'.join(queries) + "\nCOMMIT;"
    db.execute(query_to_execute)

if __name__ == "__main__":
    # creates required/optional argument groups
    parser._action_groups.pop()
    required = parser.add_argument_group('required arguments')
    optional = parser.add_argument_group('optional arguments')
    optional.add_argument("-c", "--country", help = "Type the country you wish to retrieve charts from. Leave blank if a global chart is preferred.", nargs = '+')
    # required.add_argument("-a", "--artist", required = True, help = "Type the artist", nargs = '+')
    optional.add_argument("-u", "--user", required = False)
    main()