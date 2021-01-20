## Overview
A simple ETL pipeline to fetch real-time data from the public Last.fm API and storing it into a simple PostgreSQL database.

Repo title taken from the title track of Caroline Polachek's fantastic 2019 album, [Pang](https://www.youtube.com/watch?v=C4b3NR4JqnQ). 

## Configuration
Feel free to fill in your own data in the `config.cfg` file.
```
[KEYS]
API_KEY = <insert your key here>
API_SECRET = <insert your shared secret key here>

[DATABASE]
host = <HOST NAME>
database = <DB NAME>
username = <USER NAME>
password = <PASSWORD>
port = <PORT>
```

Required modules: 
* `pylast` -- Python interface for Last.fm
* `psycopg2` -- PostgreSQL database adapter for Python

## Files
* `auth.py` : configuration variables for initial API request
* `database.py` : handles connecting to Postgres database and executing queries
* `main.py` : start here! submits command line arguments
* `queries.py` : queries for Postgres schema and tables
* `request.py` : class to make request to the Last.fm API

## To-do
* host in AWS, create a dashboard
* visualizations!!