<link rel='stylesheet' href='../assets/css/main.css'/>

# Data Generator

## Objective

Generate data to be used in our Spark labs

## Data Types

We have the following data types

### Transaction Data

This is **large** data (100s of millions of rows)

|    | id                                   | timestamp               |   mti |      card_number |   amount_customer |   merchant_type |   merchant_id | merchant_address                                           | ref_id                               |   amount_merchant |   response_code |
|---:|:-------------------------------------|:------------------------|------:|-----------------:|------------------:|----------------:|--------------:|:-----------------------------------------------------------|:-------------------------------------|------------------:|----------------:|
|  0 | c0538d79-c866-4417-be4d-672dc04d4628 | 2017-09-16 18:36:59.557 |  0100 | 4463221065841858 |              6.65 |            1760 |             0 | Awesome Bakery, 136 Hillview St, San Jose, WA, USA         |                                      |            nan    |             nan |
|  1 | 3d759627-cf66-43ae-a4b2-4232268489df | 2017-09-16 18:37:01.800 |  0110 | 4463221065841858 |              6.65 |            1760 |             0 | Awesome Bakery, 136 Hillview St, San Jose, WA, USA         | c0538d79-c866-4417-be4d-672dc04d4628 |              6.45 |              33 |
|  2 | 8a97a4e4-fa1c-4169-8d0b-5d200e00569d | 2020-03-31 07:06:28.451 |  0100 | 4225767294992126 |             77.98 |            3567 |             0 | Four Seasons Hardware, 330 Market St, Burlingame, NV, USA  |                                      |            nan    |             nan |

### Rewards Points Data

This is **small** data (few 100 rows)

|   merchant_id |   reward_points |
|--------------:|----------------:|
|             1 |              11 |
|             2 |               6 |
|             3 |              12 |
|             4 |              10 |
|             5 |              14 |

## Data Locations

We have the data files already generated for you.  Check here.

* Transaction data : TODO
* Rewards data : TODO

You can also generate data by following the instructions below.

## Lab-1: Generate Rewards Data

This is fairly small data (few hundred rows).  

```bash
    $   python  datagen-merchant-rewards.py
```

This will save data in file `reward-points.csv`

## Lab-2: Generate Sample Transaction Data

We will use a Python script to generate some sample data.

- Run this notebook in : **`data-generator/datagen-tx-small-1.ipynb`**  ([html version](datagen-tx-small-1.html))
- Or python script **`datagen-tx-small-1.py`**
- The helper functions are in  **`data-generator/datagen_helper.py`**

```bash
$   python   datagen-tx-small-1.py
```

Also generate rewards data

```bash
$   python datagen-merchant-rewards.py
```

## Lab 3: Generate Large Amount of Transacation Data Using Spark

In this lab, we will use built in Spark dataframe API to generate large amount of data.

This script is written in Scala : **`datagen-tx-large.scala`**

Inspect the configuration settings in the above file:

* `val numRows = aMillion * 1`  : default is one million rows
* `val numPartitions = 10`  : generate data in 10 partitions
* `val save_location = "datagen.tx"` : where to save data (default : local)
* `val save_format = "csv"` : save format (default csv)

First test on local mode:

```bash
    $   spark-shell --driver-memory 4g  --executor-memory 4g  -i datagen-tx-large.scala
```

To run on Hadoop cluster,

```bash
    $   spark-shell --driver-memory 4g  --executor-memory 4g  --master yarn -i datagen-tx-large.scala
```

## Lab-4: Reading back generated data to verify

* Inspect the file **`load-data.py`**
* Around line-10, make any changes needed
* Run the script as follows

```bash
    $   $SPARK_HOME/bin/spark-submit  --master local[*] --driver-class-path ../logging/  load-data.py
```