# Postgres Data Modeling Project: Schema for Song Play Analysis

## Introduction
Sparkify's analytics team is interested in analyzing what songs users are listening to. The relational database tables will allow the analytics team to optimize queries for song play analysis. 

This ETL pipeline extracts JSON logs of user activity and JSON metadata of the songs library and loads into the star schema database.

## Schema
Star schema was chosen for its simplicity. Benefits of star schema design include simpler queries for analysis, faster aggregation and query performance. The schema includes the following tables:

### Fact Table
* `songplays` - records in log data associated with song plays

### Dimension Tables
* `users` - users in the app
* `songs` - songs in music database
* `artists` - artists in music database
* `time` - timestamps of records in `songplays` broken down into specific units

## ETL Pipeline
1. `create_tables.py` - reset tables; need to run prior to running `etl.py`
2. `etl.py` - main ELT script; these two scripts run in sequence completes the ETL process
3. `sql_queries.py` - contains queries for above scripts
4. Jupyter notebooks are for testing and development of ETL scripts.