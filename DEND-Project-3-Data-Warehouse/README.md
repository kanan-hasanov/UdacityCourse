## Overview
A music streaming startup, Sparkify, has grown their user base and song database and want to move their processes and data onto the cloud to let its analytics team to continue finding insights in what songs their users are listening to.
The data resides in S3, in a directory of JSON logs on user activity on the app, as well as a directory with JSON metadata on the songs in their app.

### Objectives of the project:

Building SQL scripts and Python ETL pipeline that extracts the data from S3, stages it in Redshift, and transforms data into a set of dimensional tables.
Star schema is chosen in order to simplify queries, because less joins are needed to answer the same questions.

### The structure of the project:

`create_tables.py` creates the Sparkify star schema in Redshift

`etl.py` defines the ETL pipeline, extracts data from S3, loads into staging tables on Redshift, inserts into analytics tables on Redshift

`sql_queries.py` defines SQL queries that are used on Redshift to run drop/create/copy/insert commands

`dwh.cfg` configuration file that needs to be modified by a user looks like below:


`[CLUSTER]

HOST=<>

DB_NAME=<>

DB_USER=<>

DB_PASSWORD=<>


DB_PORT=<>

[IAM_ROLE]

ARN=<>

[S3]

LOG_DATA='s3://udacity-dend/log_data'

LOG_JSONPATH='s3://udacity-dend/log_json_path.json'

SONG_DATA='s3://udacity-dend/song_data'

`

## Database Schema
fact table:
`songplay` 

dimension tables:
`users`
`songs`
`artists`
`time`

## Execute the ETL on an existing cluster from the command line:

python create_tables.py
python etl.py


Query Example:
-- top 10 rows from tables songplay and songs

select top  10* from songs s join songplay sp on s.song_id = sp.song_id join users u on u.user_id = sp.user_id ;