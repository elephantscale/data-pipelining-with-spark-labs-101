<link rel='stylesheet' href='../assets/css/main.css'/>

# Effective Data Formats

## Objective

In this module, we will examine various data formats and their query effectiveness

## What you will learn

- Learn about popular data formats
- Query effectiveness of variuos data formats

## Knowledge Check

**What are the data formats (csv, json ..etc) do you use?**

**What are text data formats and binary data formats?**

**What are the differences between row format and columnar format?**

**What are the advantages of columnar format?**

**Currently what is the most popular data format to use Spark?**

## Essential Reading

* [Ch 4 - Spark SQL and DataFrames: Introduction to Built-in Data Sources](https://learning.oreilly.com/library/view/learning-spark-2nd/9781492050032/ch04.html)  from book [Learning Spark - 2nd Edition](https://learning.oreilly.com/library/view/learning-spark-2nd/9781492050032/) - covers reading, writing parquet files
* [Spark Data Sources page](https://spark.apache.org/docs/latest/sql-data-sources.html) has a good overview of supported dataformats: [Parquet](https://spark.apache.org/docs/latest/sql-data-sources-parquet.html), [ORC](https://spark.apache.org/docs/latest/sql-data-sources-orc.html), [JSON](https://spark.apache.org/docs/latest/sql-data-sources-json.html) and [Avro](https://spark.apache.org/docs/latest/sql-data-sources-avro.html)
* [Columnar Stores — When/How/Why?](https://towardsdatascience.com/columnar-stores-when-how-why-2d6759914319) - a good comparision of diferent data formats
* [Spark Convert JSON to Avro, CSV & Parquet](https://sparkbyexamples.com/spark/spark-convert-json-to-avro-csv-parquet/) - has examples of how to convert data from one format to another

## Extra Reading

* [Chapter 12. Avro](https://learning.oreilly.com/library/view/hadoop-the-definitive/9781491901687/ch12.html)  of the book [Hadoop: The Definitive Guide, 4th Edition](https://learning.oreilly.com/library/view/hadoop-the-definitive) by Tom White
* [Chapter 13. Parquet](https://learning.oreilly.com/library/view/hadoop-the-definitive/9781491901687/ch13.html)  of the book [Hadoop: The Definitive Guide, 4th Edition](https://learning.oreilly.com/library/view/hadoop-the-definitive) by Tom White

## Labs

### Lab-1: Data conversion

- In this lab, we will convert data from csv/json format into parquet
- Instructions (TODO)

### Lab-2: Benchmarking data formats

- In this lab, we will measure query performance of various data formats
- Instructions (TODO

## Review and Key Takeaways

After completing this chapter:

* You should be able to answer the 'Knowledge Check' questions comfortably (see start of the document)
* Handle data format conversions
* Choose the best data formats for your application