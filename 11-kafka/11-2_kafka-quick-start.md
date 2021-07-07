<link rel='stylesheet' href='../assets/css/main.css'/>

# Kafka Quicklstart

## Overview

We will create some sample topic and send data through Kafka

## Duration

20 minutes

## Depends on

[11.1](11-1_kafka-setup.md)

## Step-1: Make sure Kafka is running

Use `jps` command to verify both Kafka and Zookeeper processes are running

```bash
$   jps
```

Your output may look like this (the numbers (process ids) might be different for you)

- _QuorumPeerMain_ is zookeeper
- _Kafka_ is Kafka broker

```text
31331 QuorumPeerMain
31834 Kafka
33423 Jps
```

## Step-2: Create a test topic

We will create a test topic to test our Kafka install

```bash

# be sure in kafka dir
$   cd kafka

$   bin/kafka-topics.sh --create --topic topic1 --bootstrap-server localhost:9092
```

Verify the _topic1_ is created

```bash
$   cd kafka

$   $ bin/kafka-topics.sh --describe --topic topic1 --bootstrap-server localhost:9092
```

## Step-3: Start Console Consumer

Open a terminal, and start a consumer.  This consumer will listen on _topic1_ and print out the data on terminal

```bash
$   cd kafka

$   bin/kafka-console-consumer.sh --topic topic1  --bootstrap-server localhost:9092
```

Leave this terminal window open (DO NOT close)

## Step-4: Start Console Producer

Let's publish some messages into the topic we just created

Open another terminal, and start the producer.  This program will read user input and send data into topic

```bash
$   bin/kafka-console-producer.sh --topic topic1 --bootstrap-server localhost:9092
```

## Step-5: Send some data

On the **producer** terminal, type some text

```text
one
two
hi
bye
```

And keep an eye on the **consumer** terminal, you should see the same messages printed out on the terminal

## Takeaways

In this lab, we tested our Kafka setup