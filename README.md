## Overview

A simple ETL pipeline to fetch real-time data from the public Last.fm API and storing it into a simple PostgreSQL database.

## Configuration
Feel free to fill in your own data in the `auth.py` file.
```
[KEYS]
API_KEY = <insert your key here>
SHARED_SECRET = <insert your shared key here>

[DATABASE]
host = <HOST NAME>
database = <DB NAME>
username = <USER NAME>
password = <PASSWORD>
port = <PORT>
```

## Files
* `auth.py` : configuration variables
* `queries.py` : queries for Postgres schema and tables
* `request.py` : class to make request to the Last.fm API