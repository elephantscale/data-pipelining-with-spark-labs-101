<link rel='stylesheet' href='../assets/css/main.css'/>

# Accessing HDFS Data from Spark

## Overview

A quick test to accessing HDFS files from Spark

## Duration

15 minutes

## Step-1 : Gain Access to Hadoop Cluster

Plese follow the guidelines provided to you by the instructor, to gain access to Hadoop cluster

### Get the labs

```bash
$   git clone https://github.com/elephantscale/data-pipelining-with-spark-labs-101
```

## Step-2 : Copying files into HDFS

You will have a home directory in HDFS under `/user` directory.  So if your name is `root` your home directory in HDFS will be `/user/root`

Let's create this directory, if it doesn't exist

Note : Replace user name `root` with your own username :-)

```bash
$       hdfs  dfs -ls -p   /user/
# if you see /user/root directory, you can skip the next step
$       hdfs  dfs -mkdir -p   /user/root/
$       hdfs  dfs -ls   /user/root/
```

Next create a directory for transaction data

```bash
$       hdfs  dfs -mkdir -p  transactions/sample

# if the above command fails, specify the full path
$       hdfs  dfs mkdir -p  /user/root/transactions/sample
```

Copy some sample data into HDFS.  We have some data in `data/transactions` directory

```bash
# make sure you are in the project dir

$       cd  data-pipelining-with-spark-labs-101
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
- if that doesn't work, specify full path :   `/user/root/transactions/sample`  (change username `root` to yours, of course)
- If that doesn't work, specify full HDFS URL as follows.
    - URL will start with `hdfs://`  (just like `http://`)
    - It will include fully qualified hostname of Hadoop namenode
    - And then will have full path of files or directories
    - `hdfs://nn1.company.com/user/root/transactions/sample/`
    - You will need to adjust the URL according to your cluster settings

```python
# specify relative path
df = spark.read.csv('transactions/sample/', header=True)

# if the above doesn't work, specify full path
df = spark.read.csv('/user/root/transactions/sample/', header=True)

# or 
df = spark.read.csv('hdfs:///user/root/transactions/sample/', header=True)

df.count()
df.show()
```

If you are successfuly able to load the file, you are set.

## Takeaways

In this lab, we verified your access to HDFS