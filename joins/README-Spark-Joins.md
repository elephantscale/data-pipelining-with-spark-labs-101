<link rel='stylesheet' href='../assets/css/main.css'/>

# Spark Joins

## Objective

Joins can be expensive, specially on large scale.  Here we will take a closer look at mechanics of join in Spark

## What you will learn

- Joins in Spark
- How to effectively do joins in Spark

## Knowledge Check

**Why are joins expensive?**

**What are some issues of joining a very large table (100 of millions of rows) with a tiny table (say few 100 rows)?**

**What is a 'broadcast hash join'?  How does it work?  And what problem does it solve?**

**How does 'Sort Merge Join' work in Spark?**

**How can 'Sort Merge Join' be sped up?**

## Essential Reading

* Read **A Family of Spark Joins** in [Chapter 7. Optimizing and Tuning Spark Applications](https://learning.oreilly.com/library/view/learning-spark-2nd/9781492050032/ch07.html) from book [Learning Spark - 2nd Edition](https://learning.oreilly.com/library/view/learning-spark-2nd/9781492050032/) - this covers the basics of Spark caching
* [The art of joining in Spark](https://towardsdatascience.com/the-art-of-joining-in-spark-dcbd33d693c)
* [About Joins in Spark 3.0](https://towardsdatascience.com/about-joins-in-spark-3-0-1e0ea083ea86)
* [Spark Performance Tuning Guide](https://spark.apache.org/docs/latest/sql-performance-tuning.html#join-strategy-hints-for-sql-queries) a good overview of configuration parameters for optimizing

## Extra Reading

* [Optimizing Spark Joins](https://databricks.com/session/optimizing-apache-spark-sql-joins)

## Labs

### Lab-1: Doing a straight join

- In this lab, we will do a simple, straight forward join of two datasets
- Notebook (TODO)

### Lab-2: Doing a broadcast join

- Instructions (TODO)

### Lab-3: Speeding up 'Sort Merge Join'

- Instructions (TODO)

### Lab-4: Optimizing Joins

- We will combine all techniques to speed up joins