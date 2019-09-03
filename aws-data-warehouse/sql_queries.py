import configparser


# CONFIG
config = configparser.ConfigParser()
config.read('dwh.cfg')
iam_role = config['IAM_ROLE']['ARN']
log_data = config['S3']['LOG_DATA']
log_jsonpath = config['S3']['LOG_JSONPATH']
song_data = config['S3']['SONG_DATA']

# DROP TABLES

staging_events_table_drop = "drop table if exists staging_events"
staging_songs_table_drop = "drop table if exists staging_songs"
songplay_table_drop = "drop table if exists songplays"
user_table_drop = "drop table if exists users"
song_table_drop = "drop table if exists songs"
artist_table_drop = "drop table if exists artists"
time_table_drop = "drop table if exists time"

# CREATE TABLES

staging_events_table_create= ("""
create table if not exists staging_events (
    artist varchar,
    auth varchar,
    first_name varchar,
    gender varchar,
    item_in_session int,
    last_name varchar,
    length float,
    level varchar,
    location varchar,
    method varchar,
    page varchar,
    registration float,
    session_id int,
    song varchar,
    status int,
    ts bigint,
    user_agent varchar,
    user_id int);
""")

staging_songs_table_create = ("""
create table if not exists staging_songs (
    num_songs int,
    artist_id varchar,
    artist_latitude float,
    artist_longitude float,
    artist_location varchar,
    artist_name varchar,
    song_id varchar,
    title varchar,
    duration float,
    year int);
""")

songplay_table_create = ("""
create table if not exists songplays (
    songplay_id int identity(0,1) primary key, 
    start_time timestamp not null, 
    user_id int not null, 
    level varchar, 
    song_id varchar, 
    artist_id varchar, 
    session_id int, 
    location varchar, 
    user_agent varchar);
""")

user_table_create = ("""
create table if not exists users (
    user_id int primary key, 
    first_name varchar, 
    last_name varchar, 
    gender char, 
    level varchar);
""")

song_table_create = ("""
create table if not exists songs (
    song_id varchar primary key, 
    title varchar not null, 
    artist_id varchar not null,
    year int, 
    duration float not null);
""")

artist_table_create = ("""
create table if not exists artists (
    artist_id varchar primary key, 
    name varchar not null, 
    location varchar, 
    latitude float, 
    longitude float);
""")

time_table_create = ("""
create table if not exists time (
    start_time timestamp primary key, 
    hour int not null, 
    day int not null, 
    week int not null,
    month int not null, 
    year int not null, 
    weekday int not null);
""")

# STAGING TABLES

staging_events_copy = ("""
copy staging_events
from {}
iam_role {}
region 'us-west-2'
json {};
""").format(log_data, iam_role, log_jsonpath)

staging_songs_copy = ("""
copy staging_songs
from {}
iam_role {}
region 'us-west-2'
json 'auto';
""").format(song_data, iam_role)

# FINAL TABLES

songplay_table_insert = ("""
insert into songplays (start_time, user_id, level, 
    artist_id, song_id, session_id, location, user_agent)
select dateadd(ms,se.ts,timestamp 'epoch'), se.user_id, se.level,
    ss.song_id, ss.artist_id, se.session_id, se.location, se.user_agent
from staging_events se
join staging_songs ss 
    on se.artist = ss.artist_name
    and se.song = ss.title
    and se.length = ss.duration
where se.page = 'NextSong';
""")

user_table_insert = ("""
insert into users
select distinct user_id, first_name, last_name, gender, level
from staging_events
where page = 'NextSong';
""")

song_table_insert = ("""
insert into songs
select song_id, title, artist_id, year, duration
from staging_songs;
""")

artist_table_insert = ("""
insert into artists
select distinct artist_id, artist_name, artist_location,
    artist_latitude, artist_longitude
from staging_songs;
""")

time_table_insert = ("""
insert into time
select distinct dateadd(ms,ts,timestamp 'epoch') as start_time,
    extract(hour from start_time), extract(day from start_time),
    extract(week from start_time), extract(month from start_time),
    extract(year from start_time), extract(dayofweek from start_time)
from staging_events
where page = 'NextSong';
""")

# QUERY LISTS

create_table_queries = [staging_events_table_create, staging_songs_table_create, songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [staging_events_table_drop, staging_songs_table_drop, songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]
copy_table_queries = [staging_events_copy, staging_songs_copy]
insert_table_queries = [songplay_table_insert, user_table_insert, song_table_insert, artist_table_insert, time_table_insert]
