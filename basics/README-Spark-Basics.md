<link rel='stylesheet' href='../assets/css/main.css'/>

# Spark Basics

## Objective

A quick introduction / refresher to Spark

## What you will learn

- Understand Spark architecture
- How Spark is different from from MapReduce
- Get to know Spark components
- How Spark executes code
- Get Spark running locally
- Run Spark on a cluster

## Knowledge Check

A quick check to gauge the knowledge in this section

**Q1 - What were the problems with Hadoop MapReduce, and how is Spark solving them?**

List your answers in about 3-4 bullets.

**Q2 - Which one of these are *NOT* a Spark component**

- Spark SQL
- Spark YARN
- Spark ML
- Spark GraphX

**Q3 - What is the function of 'cluster manager' in Spark?  Name a few cluster managers used today**

**Q4 - What is a driver , job, stage, task?  How are they related?**

**Q5 - What is the difference between 'transformation' and 'action'**

**Q6 - What do we mean by 'lazy evaluation'?  What are the implications of Lazy evaluation?**

## Essential Reading

### Spark basics

- [Chapter 1. Introduction to Apache Spark: A Unified Analytics Engine](https://learning.oreilly.com/library/view/learning-spark-2nd/9781492050032/ch01.html#introduction_to_apache_spark_a_unified_a)  from book [Learning Spark - 2nd Edition](https://learning.oreilly.com/library/view/learning-spark-2nd/9781492050032/)

### What's new in Spark 3  

- Spark 3 is a big release that added a slew of performance related enhancements.
- [Deep dive into Spark 3](https://databricks.com/session_na20/deep-dive-into-the-new-features-of-apache-spark-3-0)
- **Spark 3 - a 10 year evolution** - a very nice video recap of Spark's evolution and new features in Spark 3.  [Link-1](https://databricks.com/session_na20/wednesday-morning-keynotes) ,   [Link-2](https://youtu.be/OLJKIogf2nU) 

## Extra Reading

### Spark Use Cases

- Databricks has an extensive collection of [customer success stories](https://databricks.com/customers).  Worth a browse
- [BigDataUseCases.info](http://bigdatausecases.info/technologies/spark) has a large collection of Spark usescases  Here are some highlights
    - [Migrating from RDBMS to Spark at DBS Bank](http://bigdatausecases.info/entry/migrating-from-rdbms-data-warehouses-to-apache-spark)
    - [Spark based Data Lake](http://bigdatausecases.info/entry/apache-spark-based-reliable-data-ingestion-in-datalake)
    - [Spark pipelines in production](http://bigdatausecases.info/entry/flowspec-apache-spark-pipelines-in-production)

## Code

[Code repository for book 'Learning Spark 2'](https://github.com/databricks/LearningSparkV2)

## Labs

Labs are in **`01-basics`** folder

### Lab-1 : Running Spark locally

Though Spark is designed to run on clusters, it is highly recommended that you have a local Spark setup.  This allows you to experiment with Spark without needing to connect to a cluster.

[lab-1 instructions](01-basics/lab-1-local-spark-install.md)

You may also read [Chapter 2. Downloading Apache Spark and Getting Started](https://learning.oreilly.com/library/view/learning-spark-2nd/9781492050032/ch02.html)  from book [Learning Spark - 2nd Edition](https://learning.oreilly.com/library/view/learning-spark-2nd/9781492050032/)

### Lab-2: Get access to Spark dev/staging cluster

A typical Spark development goes like this:

<img src="assets/images/workflow.png" style="width:90%;">

Next logical step going from a laptop is to run your code on the dev/staging cluster.

[Lab-2 instructions](01-basics/lab-2-spark-cluster.md)

## Review and Key Takeaways

After completing this chapter:

* You should be able to answer the 'Knowledge Check' questions comfortably (see start of the document)
* Have a working Spark installation on your laptop
* Comfortable with Spark shell
* Comfortable with Spark UI (typically port 4040)
* Have access to the dev cluster
* Can deploy Spark code on dev cluster
