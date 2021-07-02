<link rel='stylesheet' href='../assets/css/main.css'/>

# Querying Hive Tables from Spark

## Overview

We will run some queries on Hive tables

## Duration

30-40 minutes

## Depends on

[Lab 6.1](6-1_hive-spark.md)

## Step-1: Setup Hive Table

You may already have transaction data setup on Hive.  Instructor will provide access details.

If not you can setup your own Hive table by following the instructions.

We will use the data we generated earlier in [lab 5.2 - generating data in HDFS](../05-hdfs/5-2_generate-data.md)

```bash
$   hive
```

```sql

-- create your own db
hive> 
    set hive.cli.print.current.db=true;

    -- TODO: change the db name 
     create database MY_NAME_db; 

    -- TODO: switch to your db
    use MY_NAME_db;

    -- TODO: Create the following transaction table
    -- TODO: update the data location to match your HDFS location

    CREATE EXTERNAL TABLE transactions (
            id STRING,
            `timestamp` TIMESTAMP,
            mti STRING,
            card_number STRING,
            amount_customer DECIMAL (10,2),
            merchant_type STRING,
            merchant_id STRING,
            merchant_address STRING,
            ref_id STRING,
            amount_merchant  DECIMAL (10,2),
            response_code STRING
            )
        ROW FORMAT DELIMITED
        FIELDS TERMINATED BY ','
        stored as textfile
        LOCATION '/user/me/transactions/csv'  ;

```

Verify we have data in Hive tables

```sql
hive>
    select * from transactions limit 10;
```

## Step-2: Query Hive Table from Spark

Launch Spark shell 

```bash
$   pyspark
```

Verify table acceess from pyspark

```python
from pprint import pprint

# TODO: change the dbname
pprint(spark.catalog.listTables("MY_NAME_DB"))
# you should see the transaction table

## Let's do a query

spark.sql('select * from MY_NAME_DB.transactions').show()
```

## Step-3: Query 1: Find top spending card numbers

Do an aggregte query on the data.


```python

sql_query = """
select card_number, SUM(amount_customer)
from MY_NAME_DB.transactions
group by ???
order by ???
"""

top_spenders = spark.sql(sql_query)

print (top_spenders.count())

top_spenders.show(10)
```

## Step-4: Query on YARN

Run the query on YARN cluster.

Start pyspart as below and execute the same query.

```bash
$   pyspark --master yarn
```

Observe the query running metrics from Spark UI and YARN UI

### Step-5: Bonus Lab

Come up with a few more queries on the data.