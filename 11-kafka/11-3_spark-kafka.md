<link rel='stylesheet' href='../assets/css/main.css'/>

# Spark + Kafka

## Overview

Using Spark to process data in Kafka

## Duration

40 minutes

## Depends on

[11.1](11-1_kafka-setup.md)  and [11.2](11-2_kafka-quick-start.md)

## Step-1: Create a topic

Create a topic (`transactions`), that will be used for Spark streaming

```bash
$   cd kafka

$    bin/kafka-topics.sh --create --topic transactions --bootstrap-server localhost:9092  --partitions 2
```

## Step-2: Inspect Spark Streaming code

Spark streaming with Kafka has evolved quite a bit over the years.  We will look at the latest API, **structured streaming**.

See [Spark structured streaming guide](https://spark.apache.org/docs/latest/structured-streaming-programming-guide.html) for more information

Inspect the file : `spark_streaming_1.py` for sample code.  Make any changes necessary.

## Step-3: Run the streaming app

Open a terminal and run it as follows

```bash
$   spark-submit  --master local[2] \
    --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.0.1 \
    spark_streaming_1.py
```

## Step-4: Inject some data into topic

In another terminal, start a Kafka producer:

```bash
$   cd kafka

$   bin/kafka-console-producer.sh --topic transactions --bootstrap-server localhost:9092
```

Paste some data, into the terminal.  Here is some sample:

```text
1,2,3
a,b,c
```

**Action**  
Observe how quickly the new data is being processed.

## Takeaways

We have connected Spark and Kafka to process data in real time.
