<link rel='stylesheet' href='../assets/css/main.css'/>

# Spark and Hive

## Overview

Access Hive tables from Spark

<img src="../assets/images/spark-and-hadoop-1.png" style="width:50%;">

## Duration

20 minutes

## Step-1: Log into the Hadoop Cluster

Follow the instructions provided to log into the hadoop cluster

## Step-2: Access Hive

Use hive shell...

```bash
$   hive
```

And in Hive shell, try the following comamnds to see databases and tables

```sql

hive>  show databases;

-- use default db
hive>  use default;

hive> show tables;

-- switch to another db and list tables

```

## Step-3: Now launch Spark Shell

```bash
$   spark-shell --master yarn
```

When the shell launches, you will see messages that it is connected to Hive.

Specifying a custom port

```bash
    $   spark-shell  --conf spark.ui.port=4060
```

Turn off UI altogether  

```bash
    $   spark-shell  --conf spark.ui.enabled=false
```

Turn off logs

```python
    sc.setLogLevel("WARN")
```

## Step-4: Access Hive Metadata

From within Spark-shell, try these commands

```python

from pprint import pprint

pprint(spark.catalog.listDatabases())

## list tables in 'default' database
pprint(spark.catalog.listTables("default"))

## TODO: Try another db
pprint(spark.catalog.listTables("db1"))

```

## Takeaways

In this lab, you have verified Hive access from Spark