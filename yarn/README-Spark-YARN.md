<link rel='stylesheet' href='../assets/css/main.css'/>

# Spark and YARN

## Objective

YARN is the cluster manager for Hadoop.  In order to run Spark jobs on a Hadoop cluster it needs to interact with YARN

## What you will learn

* Understand YARN
* Spark and YARN

## Knowledge Check

**What are the components of YARN cluster?**

**How do you submit a Spark job to YARN?**

**What is the different between 'client mode' and 'cluster mode'?**

**How do we submit Spark applications in client mode and cluster mode?**

**What are some of settings that affect Spark jobs with YARN?**

## Essential Reading

### YARN

* [Chapter 4. YARN](https://learning.oreilly.com/library/view/hadoop-the-definitive/9781491901687/ch04.html)  of the book [Hadoop: The Definitive Guide, 4th Edition](https://learning.oreilly.com/library/view/hadoop-the-definitive) by Tom White - a good overview of YARN

### Spark and YARN

#### Spark and YARN interaction

<img src="assets/images/spark-architecture-1.png" style="width:90%;">

#### YARN Client mode

Used for interactive development and debugging

<img src="assets/images/spark-yarn-1.png" style="width:90%;">

#### YARN cluster mode

Non interactive runs (production).  Note the difference where 'driver' is running.

<img src="assets/images/spark-yarn-2.png" style="width:90%;">

#### References

* [Running Spark on YARN](http://spark.apache.org/docs/latest/running-on-yarn.html) from Spark documentation gives a good overview of Spark and YARN and describes various configurations
* [Examples of Spark-submit command](https://sparkbyexamples.com/spark/spark-submit-command/) by Spark By Examples has good practical examples of commands

## Extra Reading

* [Chapter 7. Optimizing and Tuning Spark Applications](https://learning.oreilly.com/library/view/learning-spark-2nd/9781492050032/ch07.html)   from book [Learning Spark - 2nd Edition](https://learning.oreilly.com/library/view/learning-spark-2nd/9781492050032/) has good optimization techniques.  Specially read the section on **static versus dynamic resource allocation**

## Labs

### Lab-1: Submiting a Spark job to YARN

- This lab will test Spark and YARN connectivity
- Follow these lab instructions (TODO)

### Lab-2: Tune Spark job with YARN

- In this lab, you will submit a Spark job
- And tune memory settings to optimize runtime

## Review and Key Takeaways

After completing this chapter

* You should be able to answer the 'Knowledge Check' questions comfortably (see start of the document)
* Comfortable with Spark and YARN
