# ETL process for Sparkify songplay logs.

Intention of this project is to create Fact and Dimension tables from Sparkify logs data.

Tables:
`users`
`songs`
`artists`
`songplays`
`time`

# # Data: Each log is a JSON file.

ETL Process: The code consumes all provided json files and loads data from created tables.

Step 1: Launch Terminal
Step 2: 
    Run:
        `python create_tables.py` :This will drop/create empty tables in Sparkify database.
        `python etl.py` :This will populate created tables with data.

Project File Structure:
`sql_queries.py` - SQL scripts that is being used during run time to Drop/Create tables, Select/Insert data to the tables;
`create_tables.py` - Script that recreates database sparkifydb and Drops/Creates tables;
`etl.py` - Script that orchestrates ETL process etl.ipynb - The python notebook to test