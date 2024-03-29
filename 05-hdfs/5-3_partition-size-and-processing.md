<link rel='stylesheet' href='../assets/css/main.css'/>

# Partition Size vs. Processing

## Overview

We will experiment with how partition size affects processing

## Duration

30 minutes

## Depends On

[Lab 5.2](5-2_generate-data.md) - to generate data with various partition sizes.

## Step-1: Make sure you have generated data

Follow [Lab 5.2](5-2_generate-data.md) to generate data with various partition sizes.

Generate the same amount of data, say 10 million rows, into 10 partitions and 50 partitions.

- 10 million rows as 10 partitions will result each partition size to be 174 MB,    total size = 1.7 GB
- 10 million rows as 50 partitions will result each partition size to be 35 MB,    total size = 1.7 GB

## Step-2: Let's do a simple processing in Spark

### Local Mode

Launch Spark Shell

```bash
$   pyspark --master 'local[*]'  --executor-memory 2g  --driver-memory 2g

```

Load the data and do some processing:

Issue this on Spark-Shell

```python

## First read smaller partition size (about 35 MB each)
# Adjust the path accordingly

# read parquet files
df1 = spark.read.parquet('transactions/large/parquet')

# if reading CSV
df1 = spark.read.csv('transactions/large/csv', header=True)


### measure time
import time

t1 = time.time()
count = df1.count()
t2 = time.time()

print ('count : {:,} rows,  time took : {:,.2f} secs'.format(count,  (t2-t1)))


## Then read larger partition size (about 174 MB each)
# Adjust the path accordingly
df2 = spark.read.parquet('transactions/large2/parquet')

#df2 = spark.read.csv('transactions/large2/csv', header=True)

### measure time
import time

t1 = time.time()
count = df2.count()
t2 = time.time()

print ('count : {:,} rows,  time took : {:,.2f} secs'.format(count,  (t2-t1)))
```

**Look at the Spark UI and note the following**

- How much time did loading the data take?  Was it different for both datasets?
- measure the processing times for the count.  Do you see any noticeable difference?
- How many tasks were used for count on both instances?

### Run on Cluster mode

We are going to run this experiment on the cluster.  

Make sure you have data generated in HDFS.

Start pyspark

```bash
$   pyspark  --master yarn  --executor-memory 2g  --driver-memory 2g
```

Run the same code again

```python

## First read smaller partition size (about 35 MB each)
# Adjust the path accordingly
## read parquet
df1 = spark.read.parquet('transactions/large/parquet')
## or csv
df1 = spark.read.csv('transactions/large/csv', header=True)

### measure time
import time

t1 = time.time()
count = df1.count()
t2 = time.time()

print ('count : {:,} rows,  time took : {:,.2f} secs'.format(count,  (t2-t1)))


## Then read larger partition size (about 174 MB each)
# Adjust the path accordingly
df2 = spark.read.parquet('transactions/large2/parquet')
## or csv
df2 = spark.read.csv('/user/me/data/transactions/b/csv', header=True)

### measure time
import time

t1 = time.time()
count = df2.count()
t2 = time.time()

print ('count : {:,} rows,  time took : {:,.2f} secs'.format(count,  (t2-t1)))

```

**Look at the Spark UI and note the following**

- How much time did loading the data take?  Was it different for both datasets?
- measure the processing times for the count.  Do you see any noticeable difference?
- How many tasks were used for count on both instances?

## Takeaways

So what is the **right** partition size?  Unfortunately there is no formula for it.  

The optimal partition size depends on the following:

- The kind of data you are processing
- And the processing you are doing

We recommend you experiment a little bit various partition sizes and see what works for you.

A good starting point is the **default block size** of HDFS.