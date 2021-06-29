<link rel='stylesheet' href='../assets/css/main.css'/>

# Spark SQL

## Objective

Spark supports SQL as a query language.  Spark also has one of the sophisticated SQL optimizing engines around.

In this module you will learn about using Spark SQL

## What you will learn

- Understand Spark SQL architecture
- Spark SQL features
- SQL optimization engine
- Writing Spark SQL queries
- Learn the new Adaptive Query Optimizer in Spark 3

## Knowledge Check

**What are the advantages of SQL over Scala or Python API?**

**How do we create a 'table view' of a dataframe for SQL query?**

**What is the scope of created table views?**

## Essential Reading

### Spark SQL

* [Ch 4 - Spark SQL and DataFrames: Introduction to Built-in Data Sources](https://learning.oreilly.com/library/view/learning-spark-2nd/9781492050032/ch04.html)  from book [Learning Spark - 2nd Edition](https://learning.oreilly.com/library/view/learning-spark-2nd/9781492050032/)

## Extra Reading

### Adaptive Query Execution (AQE)

This is a new SQL engine introduced in Spark v3

- [AQE explained](https://www.youtube.com/watch?v=OLJKIogf2nU&feature=youtu.be) - Watch from mark 20:00 minute mark to 23:00 minute mark
- [Adaptive Query Engine](https://databricks.com/blog/2020/05/29/adaptive-query-execution-speeding-up-spark-sql-at-runtime.html)
- [Some sample code on using AQE](https://sparkbyexamples.com/spark/spark-adaptive-query-execution/)

## Labs

### Lab-1 : Spark SQL with small data

* We will start with small dataset.
* Follow this notebook [sql-1-query-small-data.ipynb](sql-1-query-small-data.ipynb)  ( [html version](sql-1-query-small-data.html))

### Lab-2: Load VISA data and query

* In this lab, we will try SQL queries with large amount of data
* You can use pre-generated data or the data you generated in previous lab
* Lab file : [sql-2-query-large-data.py](sql-2-query-large-data.py)

A few things to experiment:

* Load data in both CSV and parquet format.  And measure the query speed.  Do you see a noticeable difference?
* Enable 'adaptive query optimizer (AQE)' and run your queries.  Do you see any noticeable difference?
* Use `explain` command to see what optimizations are applied to Spark SQL queries.

## Review and Key Takeaways

After completing this chapter:

* You should be able to answer the 'Knowledge Check' questions comfortably (see start of the document)
* Load csv and parquet dataframes with schema and register them as tables
* Be able to query data using SQL

