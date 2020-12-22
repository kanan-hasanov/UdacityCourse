# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays";
user_table_drop     = "DROP TABLE IF EXISTS users";
song_table_drop     = "DROP TABLE IF EXISTS songs";
artist_table_drop   = "DROP TABLE IF EXISTS artists";
time_table_drop     = "DROP TABLE IF EXISTS time ";

# CREATE TABLES

songplay_table_create = (
""" CREATE TABLE songplays (songplay_id serial PRIMARY KEY,
                                                start_time TIMESTAMP NOT NULL,
                                                user_id INT NOT NULL,
                                                LEVEL VARCHAR,
                                                song_id VARCHAR,
                                                artist_id VARCHAR,
                                                session_id VARCHAR NOT NULL ,
                                                LOCATION VARCHAR,
                                                user_agent VARCHAR); """)

user_table_create = (
""" CREATE TABLE USERS (user_id INT PRIMARY KEY ,
                                        first_name VARCHAR NOT NULL,
                                        last_name VARCHAR NOT NULL,
                                        gender VARCHAR,
                                        LEVEL VARCHAR NOT NULL); """)

song_table_create = (
""" CREATE TABLE songs (song_id VARCHAR PRIMARY KEY,
                                        title VARCHAR NOT NULL,
                                        artist_id VARCHAR NOT NULL,
                                        YEAR INT NOT NULL,
                                        duration FLOAT NOT NULL); """)

artist_table_create = (
""" CREATE TABLE artists (artist_id VARCHAR PRIMARY KEY,
                                            NAME VARCHAR NOT NULL,
                                            LOCATION VARCHAR,
                                            latitude FLOAT,
                                            longitude FLOAT); """)

time_table_create = (
""" CREATE TABLE time (start_time bigint NOT NULL PRIMARY KEY,
                                        HOUR INT NOT NULL,
                                        DAY INT NOT NULL,
                                        week INT NOT NULL,
                                        MONTH INT NOT NULL,
                                        YEAR INT NOT NULL,
                                        weekday INT NOT NULL); """)

# INSERT RECORDS

songplay_table_insert = (
""" INSERT INTO songplays ( start_time ,
                        user_id ,
                        LEVEL ,
                        song_id ,
                        artist_id ,
                        session_id ,
                        LOCATION ,
                        user_agent)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s); """)

user_table_insert = (
""" INSERT INTO users ( user_id,
                    first_name,
                    last_name,
                    gender,
                    LEVEL)
VALUES(%s, %s, %s, %s, %s)
ON CONFLICT (user_id)
DO UPDATE
SET level = EXCLUDED.level


; """)

song_table_insert = ("""
INSERT INTO songs (song_id ,
                    title ,
                    artist_id ,
                    YEAR ,
                    duration )
VALUES(%s, %s, %s, %s, %s)
ON CONFLICT (song_id)
DO NOTHING; """)

artist_table_insert = (
""" INSERT INTO artists (artist_id ,
                    NAME ,
                    LOCATION ,
                    latitude ,
                    longitude)
VALUES(%s, %s, %s, %s, %s)
ON CONFLICT (artist_id)
DO NOTHING; """)


time_table_insert = (
""" INSERT INTO time (start_time ,
                    HOUR ,
                    DAY ,
                    week ,
                    MONTH ,
                    YEAR ,
                    weekday)
VALUES(%s, %s, %s, %s, %s, %s, %s)
ON CONFLICT (start_time)
DO NOTHING; """)

# FIND SONGS

song_select = (
""" SELECT
    songs.song_id,
    songs.artist_id
FROM
    songs
INNER JOIN artists 
    ON songs.artist_id = artists.artist_id
WHERE
        songs.title = (%s)
    AND artists.name = (%s)
    AND songs.duration = (%s) ; """)

# QUERY LISTS

create_table_queries    = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries      = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]