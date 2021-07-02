<img src="../assets/images/spark-yarn-1.png" style="width:90%;">

## Spark and YARN

## Overview

In this lab, we will tweak YARN settings for Spark jobs

## Duration

30 minutes

## Depends on

[Lab 7.1](7-1_yarn-1.md)

## Step-1: Run SQL query in interactive mode

Start pyspark in interactive mode, and run a SQL query

```bash
$   pyspark --master yarn --deploy-mode client
```

And try  this query on spark shell

```python

# Read the transaction data from HDFS
## TODO: Adjust the data path accordingly
df = spark.read.csv('/user/me/transactions/csv')

## Register a temp table
df.createOrReplaceTempView("transactions")

## Run a simple SQL query
spark.sql ('select count(*) from transactions').show()

## Run an aggregate query
## Find the top merchants per amount charged
sql_str = """
select merchant_id, SUM(amount_merchant) as total
from transactions
group by merchant_id
order by  total DESC
"""

spark.sql(sql_str).show()
```

Make sure this query works first.

## Step-2: Optimize the Query

When submitting to YARN, we can tweak some settings.

```bash
$   pyspark --master yarn --deploy-mode client \
            --executor-memory 4g  \
            --num-executors 6
```

Parameters explained:

- `executor memory`: how much memory each JVM executor gets
- `num-executors`: how many executors to launch

Read the [Spark and YARN page](https://spark.apache.org/docs/latest/running-on-yarn.html) for some detailed explanations.

**Action:** Start with the above settings and see if the query runs faster.

## Step-3: Run in YARN mode

- Submit the above query in YARN cluster mode.
- Experiment with various parameters