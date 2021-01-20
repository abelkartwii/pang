import psycopg2
import configparser
from pathlib import Path 
from queries import *

config = configparser.ConfigParser()
config.read('config.cfg')

class Database:
    def __init__(self):
        self._conn = psycopg2.connect("host = {} dbname = {} user = {} password = {} port = {}".format(*config['DATABASE'].values()))
        self._cur = self._conn.cursor()

    def execute(self, query):
        self._cur.execute(query)

    def setup(self):
        self.execute(create_lastfm_schema)
        self.execute(create_lastfm_table)