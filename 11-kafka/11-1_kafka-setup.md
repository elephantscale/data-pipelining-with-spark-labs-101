<link rel='stylesheet' href='../assets/css/main.css'/>

# Setting up Kafka

## Overview

We will install and configure Kafka.

For this lab, we assume a Linux system.

## Duration

20 minutes

## Step-1: Download Kafka

Grab the [latest release of Kafka](https://kafka.apache.org/downloads).  We will use Kafka v2.8

```bash
$   wget https://mirrors.ocf.berkeley.edu/apache/kafka/2.8.0/kafka_2.13-2.8.0.tgz

$   tar xvf kafka_2.13-2.8.0.tgz

# rename for easier access

$   mv  kafka_2.13-2.8.0    kafka

# the 'kafka' directory will be our KAFKA_HOME 
```

## Step-2: Start Zookeeper

Kafka depends on Zookeeper.  Soon this dependency will be removed.

```bash
# be in Kafka directory
$   cd kafka

$   bin/zookeeper-server-start.sh config/zookeeper.properties

```

Leave the zookeeper terminal running, do NOT close it.

## Step-3: Start Kafka Broker service

Open another terminal and start kafka

```bash
$   cd kafka
$   bin/kafka-server-start.sh config/server.properties

```

Leave this terminal open as well (do NOT close)

## Step-4: Verify Processes are running

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

## Takeaways

In this lab, we downloaded and setup Kafka