<link rel='stylesheet' href='../assets/css/main.css'/>

# Spark SQL Labs

## Lab-4.1 : Spark SQL with small data

* We will start with small dataset.
* Follow this notebook [sql-1-query-small-data.ipynb](sql-1-query-small-data.ipynb)  ( [html version](sql-1-query-small-data.html))

## Lab-4.2: Load data and query

* In this lab, we will try SQL queries with large amount of data
* You can use pre-generated data or the data you generated in previous lab
* Lab file : [sql-2-query-large-data.py](sql-2-query-large-data.py)

A few things to experiment:

* Load data in both CSV and parquet format.  And measure the query speed.  Do you see a noticeable difference?
* Enable 'adaptive query optimizer (AQE)' and run your queries.  Do you see any noticeable difference?
* Use `explain` command to see what optimizations are applied to Spark SQL queries.
