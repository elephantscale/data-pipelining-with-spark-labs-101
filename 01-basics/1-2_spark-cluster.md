<link rel='stylesheet' href='../assets/css/main.css'/>

# Lab 1-2: Accessing Spark Cluster

In this lab, you will gain access to your organization's Spark cluster.

## Step-1: Login to the cluster

Instructions will be made available.

## Step-2: Launch Spark Shell

In the terminal type the following:

```bash
$       spark-shell
```

This will drop you into spark shell as follows

```text
Welcome to
      ____              __
     / __/__  ___ _____/ /__
    _\ \/ _ \/ _ `/ __/  '_/
   /___/ .__/\_,_/_/ /_/\_\   version 2.3.0.cloudera4
      /_/
```

In the spark shell type the following command

```scala

scala> spark.range(1,10).show
```

You will see the output as follows:

```text
| id|
+---+
|  1|
|  2|
|  3|
|  4|
|  5|
|  6|
|  7|
|  8|
|  9|
+---+
```

## Step-3: Run Spark in Cluster mode

Here we will run a very simple Spark program.  We are going to calculate the value of pi (π)

First let's run in local mode:

Note:  You may have to change the jar file locations, in the following command

```bash
$       spark2-submit --master local \
    --class org.apache.spark.examples.SparkPi \
/opt/cloudera/parcels/SPARK2-2.3.0.cloudera4-1.cdh5.13.3.p0.611179/lib/spark2/examples/jars/spark-examples_2.11-2.3.0.cloudera4.jar \
    100   2> /dev/null
```

The output may look like :

```text
Pi is roughly 3.1418967141896714
```

Next run in 'cluster' mode

Note:  You may have to change the jar file locations, in the following command

```bash
$	spark2-submit --master yarn \
    --class org.apache.spark.examples.SparkPi \
/opt/cloudera/parcels/SPARK2-2.3.0.cloudera4-1.cdh5.13.3.p0.611179/lib/spark2/examples/jars/spark-examples_2.11-2.3.0.cloudera4.jar \
    100   2> /dev/null
```

The output will be similar to

```text
Pi is roughly 3.1413255141325513
```
