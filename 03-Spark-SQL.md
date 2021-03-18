<link rel='stylesheet' href='assets/css/main.css'/>

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

## References

### Essential Reading

#### Spark SQL

* [Ch 4 - Spark SQL and DataFrames: Introduction to Built-in Data Sources](https://learning.oreilly.com/library/view/learning-spark-2nd/9781492050032/ch04.html)  from book [Learning Spark - 2nd Edition](https://learning.oreilly.com/library/view/learning-spark-2nd/9781492050032/)

### Extra Reading

#### Adaptive Query Execution (AQE)

This is a new SQL engine introduced in Spark v3

- [AQE explained](https://www.youtube.com/watch?v=OLJKIogf2nU&feature=youtu.be) - Watch from mark 20:00 minute mark to 23:00 minute mark
- [Adaptive Query Engine](https://databricks.com/blog/2020/05/29/adaptive-query-execution-speeding-up-spark-sql-at-runtime.html)
- [Some sample code on using AQE](https://sparkbyexamples.com/spark/spark-adaptive-query-execution/)

## Labs

### Lab-1 : Loading flights data and querying via SQL

- In this lab, we will load flights data and query with SQL
- Follow this notebook (TODO)

### Lab-2: Load VISA data and query

- Follow this notebook (TODO)

## Review and Key Takeaways

After completing this chapter:

* You should be able to answer the 'Knowledge Check' questions comfortably (see start of the document)
* Load csv and parquet dataframes with schema and register them as tables
* Be able to query data using SQL

