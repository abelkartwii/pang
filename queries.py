create_lastfm_schema = """CREATE SCHEMA IF NOT EXISTS lastfm;"""

create_lastfm_table = """

    DROP TABLE IF EXISTS lastfm.data;

    CREATE TABLE IF NOT EXISTS lastfm.data (
    track VARCHAR(255),
    duration INT,
    playcount INT PRIMARY KEY,
    listeners INT,
    trackurl VARCHAR,
    artistname VARCHAR,
    artistmbid VARCHAR,
    artisturl VARCHAR
);
"""

insert_lastfm_table = """INSERT INTO lastfm.data (track, "duration", "playcount", "listeners", "trackurl", "artistname", "artistmbid", "artisturl")
                        VALUES ('{}', {}, {}, {}, '{}', '{}', '{}', '{}');
                        """