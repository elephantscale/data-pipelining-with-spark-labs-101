<link rel='stylesheet' href='assets/css/main.css'/>

# Spark DataFrames

## Objective

Dataframes are the preferred way to program Spark.  In this section you will learn about DataFrame APIs

## What You Will Learn

- DataFrame architecture
- Using DataFrame APIs

## Knowledge Check

**What are the features of DataFrame API?**

**What are the some of the data types supported in DataFrame?**

**What are some supported file formats (text, csv ..etc)  that are supported by Dataframe**

**There are two ways to define schema.  How?**

**When inferring schema from datafiles, how can we limit the amount of data being read?**

**What is the connection between 'DataFrame' and 'DataSet'?  What are the similarities and differences?**

**How to convert from RDD/DataFrame/DataSets?**

**What is Catalyst?**

**What are some of the optimizations Catalyst can do?**

## References

### Essential Reading

* [Ch 3 - Apache Spark’s Structured APIs](https://learning.oreilly.com/library/view/learning-spark-2nd/9781492050032/ch03.html)  from book [Learning Spark - 2nd Edition](https://learning.oreilly.com/library/view/learning-spark-2nd/9781492050032/)

### Extra Reading

* [A Tale of Three Apache Spark APIs: RDDs vs DataFrames and Datasets](https://databricks.com/blog/2016/07/14/a-tale-of-three-apache-spark-apis-rdds-dataframes-and-datasets.html) - A good article explaining the evolution of data models in Spark
* [Apache Spark RDD vs DataFrame vs DataSet](https://data-flair.training/blogs/apache-spark-rdd-vs-dataframe-vs-dataset/) - a good tutorial covering various aspects of data models

## Labs

Labs are in **`02-dataframes`** folder

### Lab 1 - Creating a DataFrame programatically

Create a small DataFrame programatically

Lab-1 notebook: `02-dataframes/dataframes-1.ipynb`  ([html version](02-dataframes/dataframes-1.html))

### Lab 2 - Read a Dataframe from file

- Read the CSV file from disk
- Print out the schema
- Perform an aggregate query on a column

Lab-2 notebook: `02-dataframes/dataframes-2.ipynb`  ([html version](02-dataframes/dataframes-2.html))

### Lab 3 - Specify Schema

- We will continue with above lab.
- How ever we will specify the schema while loading data

Lab-3 notebook: `02-dataframes/dataframes-3.ipynb`  ([html version](02-dataframes/dataframes-3.html))

## Review and Key Takeaways

After completing this chapter:

* You should be able to answer the 'Knowledge Check' questions comfortably (see start of the document)
* Be able to create / read DataFrames
* Specify schema for the DataFrame
* Can perform queries on DataFrames
