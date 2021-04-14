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

## Lab-1: Generate Sample Data

We will use a Python script to generate some sample data.

- Run this notebook in : **`data-generator/datagen-tx-small-1.ipynb`**  ([html version](datagen-tx-small-1.html))
- Or python script **`datagen-tx-small-1.py`**

```bash
$   python   datagen-tx-small-1.py
```

Also generate rewards data

```bash
$   python datagen-merchant-rewards.py
```