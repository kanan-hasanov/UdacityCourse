# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays";
user_table_drop = "DROP TABLE IF EXISTS users";
song_table_drop = "DROP TABLE IF EXISTS songs";
artist_table_drop = "DROP TABLE IF EXISTS artists ";
time_table_drop = "DROP TABLE IF EXISTS time ";

# CREATE TABLES

songplay_table_create = (""" CREATE TABLE songplays (songplay_id serial primary key, start_time TIMESTAMP, user_id INT, level VARCHAR, song_id varchar, artist_id varchar, session_id varchar , location VARCHAR, user_agent VARCHAR);
""")

user_table_create = (""" CREATE TABLE users (user_id INT , first_name VARCHAR, last_name VARCHAR, gender VARCHAR, level VARCHAR);
""")

song_table_create = (""" CREATE TABLE songs  (song_id varchar, title VARCHAR, artist_id varchar, year INT, duration FLOAT);
""")

artist_table_create = (""" CREATE TABLE artists (artist_id VARCHAR, name VARCHAR, location VARCHAR, latitude FLOAT, longitude FLOAT);
""")

time_table_create = (""" CREATE TABLE time (start_time bigint, hour INT, day INT, week INT, month INT, year INT, weekday INT);
""")

# INSERT RECORDS

songplay_table_insert = (""" 
insert into songplays ( start_time , user_id , level , song_id , artist_id , session_id  , location , user_agent)
values (%s, %s, %s, %s, %s, %s, %s, %s)
""")

user_table_insert = ("""
insert into users (user_id, first_name, last_name, gender, level)
values(%s, %s, %s, %s, %s);
""")

song_table_insert = ("""
insert into songs (song_id , title , artist_id , year , duration )
values(%s, %s, %s, %s, %s);
""")

artist_table_insert = ("""
insert into artists (artist_id , name , location , latitude , longitude)
values(%s, %s, %s, %s, %s);
""")


time_table_insert = ("""
insert into time (start_time , hour , day , week , month , year , weekday )
values(%s, %s, %s, %s, %s, %s, %s);
""")

# FIND SONGS

song_select = ("""
SELECT songs.song_id, songs.artist_id FROM songs join artists on songs.artist_id = artists.artist_id WHERE songs.title = (%s) and artists.name = (%s) and songs.duration = (%s) ;
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]