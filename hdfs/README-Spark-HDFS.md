<link rel='stylesheet' href='../assets/css/main.css'/>

# Spark and HDFS

## Objective

HDFS is a highly popular distributed file system.  In this section we will look into Spark and HDFS integration

## What you will learn

* Understand HDFS architecture
* Understand partitions and distributed storage

## Knowledge Check

**What is the default partition size in HDFS?**

**What are the problems caused by small files in HDFS?**

**How do small files affect processing times in Spark?**

**How can we detect small files in HDFS?**

**How can we mere small files into large files?**

## Essential Reading

### Hadoop and HDFS

* [Chapter 1. Meet Hadoop](https://learning.oreilly.com/library/view/hadoop-the-definitive/9781491901687/ch01.html)  of the book [Hadoop: The Definitive Guide, 4th Edition](https://learning.oreilly.com/library/view/hadoop-the-definitive) by Tom White - Gives a nice background and history on Hadoop
* [Chapter 3. The Hadoop Distributed Filesystem](https://learning.oreilly.com/library/view/hadoop-the-definitive/9781491901687/ch03.html)  of the book [Hadoop: The Definitive Guide, 4th Edition](https://learning.oreilly.com/library/view/hadoop-the-definitive) by Tom White - A good introduction to HDFS design and architecture

### Small File Problem

* [Small file problem](https://medium.com/arabamlabs/small-files-in-hadoop-88708e2f6a46)
* [Small Files](https://blog.cloudera.com/small-files-big-foils-addressing-the-associated-metadata-and-application-challenges/)  - discusses file sizes and its impact on processing
* [Dealing with small file problem in Hadoop](https://www.quora.com/What-is-the-small-file-problem-in-Hadoop)
* [Spark and blocksize](https://www.quora.com/Why-is-it-recommended-to-use-256-MB-block-size-on-Spark-projects-Does-it-matter-if-you-use-smaller-or-larger-block-size-if-your-spark-jobs-computationally-intensive)

### Spark and HDFS

HDFS chops files into partitions and these partitions are distributed across the cluster

<img src="../assets/images/distributed_file_blocks.png" style="width:90%;">

Spark works well with HDFS.  Spark can understand file layout and prioritize local data.

<img src="../assets/images/spark_and_hdfs.png" style="width:90%;">

Spark will spin up a task per partition to process data.  This way, we get parallelism

<img src="../assets/images/distributed_processing.png" style="width:90%;">

## Labs

### Lab-1: Accessing HDFS files from Spark

This is a quick lab we will access data on HDFS from Spark

Lab instructions (TODO)

### Lab-2: Generating data

* In this lab, you will use a **data generator script** to create some sample data.
* We can configure partition size for the generated data
* We will generate various partition sizes (small to large)
* Lab instructions (TODO)

### Lab-3: Partition size vs processing times

* In this lab, we will run Spark jobs on data of various partition sizes and compare the results
* Lab instructions (TODO)

### Lab-4: Merging small files into large files

* In this lab, we will explore how to detect small files and merge them into large files
* Lab instructions (TODO)

## Review and Key Takeaways

After completing this chapter

* You should be able to answer the 'Knowledge Check' questions comfortably (see start of the document)
* Deal with small files and work with them effectively using Spark
