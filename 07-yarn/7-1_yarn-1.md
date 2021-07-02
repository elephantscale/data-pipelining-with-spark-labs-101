<link rel='stylesheet' href='../assets/css/main.css'/>

# Spark and YARN

## Overview

Running Spark jobs over YARN

## Duration

15 minutes

## Step-1: Understanding Spark and YARN

<img src="../assets/images/spark-architecture-1.png" style="width:60%;">

When Spark is configured properly on Hadoop cluster, it will automatically connect to YARN to submit jobs.

## Step-2: Testing YARN Connectivity

Launch Spark in yarn mode

```bash
$   pyspark --master yarn
```

Inspect the logs.  You will see something along the lines like these.

```text
...connected to resource manager ...
```

## Step-3: YARN Client Mode

lient mode let's you interact with YARN using Spark Shell.

Used for interactive development and debugging

<img src="../assets/images/spark-yarn-1.png" style="width:90%;">

```bash
$   pyspark --master yarn  --deploy-mode client
```

Try this on Spark-shell

```python

df = spark.range(1,10000)

df.count()
```

## Step-4: YARN Cluster Mode

Cluster mode is non-interactive.  Used for submiting jobs in production.

Note the difference where 'driver' is running.

<img src="../assets/images/spark-yarn-2.png" style="width:90%;">

Create a python file `sample.py` as follows

```python

from pyspark.sql import SparkSession

spark = SparkSession.builder.
        appName("mysparkapp").getOrCreate()

df = spark.range(1,10000)

df.count()

spark.stop()
```

Submit this program as follows:

```bash
$   spark-submit --master yarn --deploy-mode cluster \
            sample.py
```
