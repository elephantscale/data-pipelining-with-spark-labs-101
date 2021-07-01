<link rel='stylesheet' href='../assets/css/main.css'/>

# Merging Small files into Larger Ones

## Overview

Merge smaller files into larger ones.

## Duration

20 minutes

## Depends on

Lab 5.2 and 5.3

## Step-1: Generate Data with variuos partition sizes

Follow lab [5.3](5-3_partition-size-and-processing.md) to generate data with various partition sizes

## Step-2: Load small partition data

```bash
$   pyspark
```

```python

# load small partition data

df1 = spark.read.csv('/user/me/transactions/a/csv')

# See how many partitions we have
df1.rdd.getNumPartitions()

# repartition into 5 partitions
df2 = df1.repartition(5)

# save the new data
df2.write.mode('overwrite').csv('/user/me/transactions/a2/')

```

Now let's inspect the generated data

```bash
$   hdfs dfs -ls /user/me/transactions/a/csv

$   hdfs dfs -ls /user/me/transactions/a2/csv
```

Do you notice the partition size difference?