<link rel='stylesheet' href='../assets/css/main.css'/>

# Accessing HDFS Data from Spark

## Overview

A quick test to accessing HDFS files from Spark

## Duration

15 minutes

## Step-1 : Gain Access to Hadoop Cluster

Plese follow the guidelines provided to you by the instructor, to gain access to Hadoop cluster

## Step-2 : Copying files into HDFS

You will have a home directory in HDFS under `/user` directory.  So if your name is `mrmeow` your home directory in HDFS will be `/user/mrmeow`

Let's create this directory, if it doesn't exist

Note : Replace user name `mrmeow` with your own username :-)

```bash
$       hdfs  dfs mkdir -p   /user/mrmeow/
```

Next create a directory for transaction data

```bash
$       hdfs  dfs mkdir -p  transactions/sample

# if the above command fails, specify the full path
$       hdfs  dfs mkdir -p  /user/mrmeow/transactions/sample
```

Copy some sample data into HDFS.  We have some data in `data/transactions` directory

```bash
# make sure you are in the project dir

$       hdfs   dfs -put  data/transactions/transactions-sample.csv    transactions/sample/

# verify the file is copied successfully
$       hdfs   dfs -ls    transactions/sample/
# you should see files
```

## Step-3: Access HDFS Data from Spark

Start Spark shell

```bash
$       pyspark
```

And load the file as follows in Spark shell.  To access HDFS files, we may need to specify full path

- start with simple path `transactions/sample/`
- if that doesn't work, specify full path :   `/user/mrmeow/transactions/sample`  (change username `mrmeow` to yours, of course)
- If that doesn't work, specify full HDFS URL as follows.
    - URL will start with `hdfs://`  (just like `http://`)
    - It will include fully qualified hostname of Hadoop namenode
    - And then will have full path of files or directories
    - `hdfs://nn1.company.com/user/mrmeow/transactions/sample/`
    - You will need to adjust the URL according to your cluster settings

```python
df = spark.read.csv('/user/mrmeow/transactions/sample/')
df.count()
df.show()
```

If you are successfuly able to load the file, you are set.

## Takeaways

In this lab, we verified your access to HDFS