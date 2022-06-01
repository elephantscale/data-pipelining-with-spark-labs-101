<link rel='stylesheet' href='../assets/css/main.css'/>

# Datagen with Various Partition Sizes

## Overview

In this lab, we will generate data sizes with various partition sizes

## Duration

30 - 60 mins

## Step-1: Inspect Data Generator Script

The script is located at : `03-data-geneator/datagen-tx-large.scala`

You can modify the following attributes to generate various size data

- around line number 22, set this generate as many rows as needed  
`val numRows = aMillion * 1`
- around line number 26,  set this to desired number of partitions  
`val numPartitions = 10`  
- around line number 31,  adjust to your save location, usually in HDFS (Adjust for your HDFS settings)  
`val save_location = "/user/me/transactions/a"`

Here are some sample settings to generate 
- 10 million rows
- into 50 partitions

```scala
val numRows = aMillion * 10
val numPartitions = 50
val save_location = "/user/me/transactions/a"
```

## Step-2: Run the Data Generator

### To run in local mode

Edit the data-generator script

```scala
val numRows = aMillion * 100
val numPartitions = 10
val save_location = "data/transactions/a/"
```

Arguments explained:

- Allocating 4 GB memory for Spark driver and Spark executor
- Running in local mode (`--master 'local[*]'`)

```bash
# make sure you are in the labs root dir
$   cd  data-pipelining-with-spark-labs-101

$   spark-shell   --driver-memory 4g \
          --executor-memory 4g   --master 'local[*]' \
          -i 03-data-generator/datagen-tx-large.scala

```

### To Run on cluster

Arguments explained:
- Allocating 4 GB memory for Spark driver and Spark executor
- Connecting to YARN cluster (`--master yarn`)

```bash
# make sure you are in the labs root dir
$   cd  data-pipelining-with-spark-labs-101

$   spark-shell   --driver-memory 4g \
          --executor-memory 4g   --master yarn \
          -i 03-data-generator/datagen-tx-large.scala

```

## Step-3: Inspect generated data

```bash
$   hdfs dfs -ls  transactions/a
```

The files will be in CSV directory.  Note the following:

- How many files are generated (should be equal to number of partitions)
- And each files size (partition size)

## Step-4: Generate data at various sizes

Adjust the settings and rerun the above script to generate data of various sizes


Here are some stats from  sample runs.

sample run 1:

- rows = 1 million
- partitions = 10
- each partition is about 17 MB

Sample run 2:

- Rows = 10 million
- partitions = 10
- each partition is about 173 MB