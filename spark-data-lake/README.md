# Data Lake with Spark

## Introduction
Sparkify's analytics team is interested in analyzing what songs users are listening to. This ETL pipeline extracts JSON logs of user activity and JSON metadata of the songs library from S3 bucket and process them using Spark and loads into another S3 bucket as fact and dimensional tables.

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

### Files
1. `etl.py` - ETL script
2. `dl.cfg` - config file for AWS credentials

### To run ETL Pipeline
1. Run main ETL script:
> `python etl.py`
