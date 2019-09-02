# AWS Data Warehousing Project: ETL from S3 Buckets to Redshift Cluster

## Introduction
Sparkify's analytics team is interested in analyzing what songs users are listening to. The Redshift database tables will allow the analytics team to optimize queries for song play analysis. This ETL pipeline extracts JSON logs of user activity and JSON metadata of the songs library from S3 buckets and loads into the star schema database in Redshift.

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
1. `create_tables.py` - reset tables and create them if ran for the first time; need to run prior to running `etl.py`
2. `etl.py` - ETL script; these two scripts run in sequence completes the ETL process
3. `sql_queries.py` - contains queries for above scripts
4. `dwh.cfg` - config file for Redshift cluster, IAM role for cluster to read S3, location of data files in S3

### AWS Configuration
1. Create IAM role that allows Redshift cluster to read from S3 [link](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-service.html)
2. Create Redshift cluster in us-west-2 region [link](https://docs.aws.amazon.com/redshift/latest/gsg/rs-gsg-launch-sample-cluster.html)
3. Fill details in `dwh.cfg` file

### How to run ETL Pipeline
1. Run script to create/reset tables:
> `python create_tables.py`<br/>
2. Run main ETL script:
> `python etl.py`
