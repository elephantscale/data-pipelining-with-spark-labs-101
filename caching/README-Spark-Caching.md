<link rel='stylesheet' href='../assets/css/main.css'/>

# Spark Caching

## Objective

Spark can cache data in memory and disk.  This is a very powerful feature.  In this module we will learn about Spark caching and how to use it effectively

## What you will learn

- Spark caching mechanics
- How to effectively use caching

## Knowledge Check

**When is it appropriate to cache data in Spark?**

**When caching is NOT appropriate?**

**What are some of the caching options Spark supports?**

**Is caching a lazy or eager operation?**

**How can we check the data is cached?**

## Essential Reading

* Read **Caching and Persistence of Data** in [Chapter 7. Optimizing and Tuning Spark Applications](https://learning.oreilly.com/library/view/learning-spark-2nd/9781492050032/ch07.html) from book [Learning Spark - 2nd Edition](https://learning.oreilly.com/library/view/learning-spark-2nd/9781492050032/) - this covers the basics of Spark caching
* [Comparing different cache mediums and their performances](https://towardsdatascience.com/apache-spark-caching-603154173c48)

## Extra Reading

* [Best practices in Spark caching](https://towardsdatascience.com/best-practices-for-caching-in-spark-sql-b22fb0f02d34)
* [Good explanation and sample code for caching](https://sparkbyexamples.com/spark/spark-difference-between-cache-and-persist/)

## Labs

### Lab-1: Understand Caching mechanics

- In this lab, we will measure caching performance
- And inspect the Spark UI for caching details

### Lab-2: Query execution with caching

- In this lab, we will optimize query run speed by caching data

## Review and Key Takeaways

After completing this chapter

* You should be able to answer the 'Knowledge Check' questions comfortably (see start of the document)
* Comfortable with Spark caching
