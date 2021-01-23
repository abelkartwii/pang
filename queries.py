create_lastfm_schema = """CREATE SCHEMA IF NOT EXISTS lastfm;"""

create_lastfm_table = """
CREATE TABLE IF NOT EXISTS lastfm.data (
    id INTEGER PRIMARY KEY,
    mbid VARCHAR(255),
    name TEXT NOT NULL UNIQUE,
    play_count INTEGER NOT NULL,
    rank INTEGER NOT NULL
    url VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS
"""

insert_lastfm_table = """
INSERT INTO lastfm.data
VALUES ()

"""