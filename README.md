## Overview
A simple ETL pipeline to fetch real-time charts from the public Last.fm API and storing it into a simple PostgreSQL database.

Repo title taken from the title track of Caroline Polachek's fantastic 2019 album, [Pang](https://www.youtube.com/watch?v=C4b3NR4JqnQ). 

## Configuration
To run, fill in your own data in the `config.cfg` file:

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

After setting up configuration, type the following into the command line:

```
python main.py --country Indonesia
```

Note that the country argument is optional; leave blank to retrieve the global charts.

Required modules: 
* `pylast` -- Python interface for Last.fm
* `psycopg2` -- PostgreSQL database adapter for Python

## Files
* `auth.py` : config variables for initial API request
* `config.cfg` : config files for API request, database 
* `database.py` : handles connecting to Postgres database and executing queries
* `lastfm.py` : handles results returned from Last.fm API request
* `main.py` : start here! submits command line arguments
* `queries.py` : queries for Postgres schema and tables
* `reqs.py` : class to make request to the Last.fm API

## To-do
* host in AWS, create a dashboard
* visualizations!