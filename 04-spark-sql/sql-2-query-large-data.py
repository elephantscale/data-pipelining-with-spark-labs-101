## Run it as 
##  $SPARK_HOME/bin/spark-submit  --master 'local[*]' --driver-class-path ../logging/  sql-2-query-large-data.py
## 
## To prevent out-of-memory errors, provide more memory...
##      $SPARK_HOME/bin/spark-submit  --master 'local[*]' --driver-class-path ../logging/  --driver-memory 2G --executor-memory 4G sql-2-query-large-data.py
##

from pyspark.sql import SparkSession
from pyspark.sql.types import ArrayType, IntegerType, LongType, StringType, FloatType, TimestampType, StructType, StructField
import time

spark = SparkSession.builder.appName("sql-2").getOrCreate()
spark.sparkContext.setLogLevel("ERROR")
print('### Spark UI available on port : ' + spark.sparkContext.uiWebUrl.split(':')[2])

## two options to load:
## 1 - loading CSV files, specify schema
my_schema = StructType([
                       StructField("id", StringType(), True),
                       StructField("timestamp", StringType(), True),
                       StructField("mti", StringType(), True),
                       StructField("card_number", StringType(), True),
                       StructField("amount_customer", FloatType(), True),
                       StructField("merchant_type", StringType(), True),
                       StructField("merchant_id", StringType(), True),
                       StructField("merchant_address", StringType(), True),
                       StructField("ref_id", StringType(), True),
                       StructField("amount_merchant", FloatType(), True),
                       StructField("response_code", StringType(), True),
                      ])
df = spark.read.csv('../data/transactions/csv/', header=True, schema=my_schema)

## 2 - loading parquet 
# df = spark.read.parquet('../data/transactions/parquet/')

df.show()
df.printSchema()

# create a temp table
df.createOrReplaceTempView("transactions")

## count
t1 = time.perf_counter()
result = spark.sql('select count(*) as count from transactions')
count = result.first()['count']
t2 = time.perf_counter()
print ('count : {:,} rows,  time took : {:,.2f} ms'.format(count,  (t2-t1)*1000))

## find the top-10 credit cards that spend most money!

sql = """
select card_number, SUM(amount_customer) as total
from transactions
group by card_number
order by total DESC
"""

t1 = time.perf_counter()
spark.sql(sql).show()
t2 = time.perf_counter()
print ('top spending credit cards,  time took : {:,.2f} ms'.format((t2-t1)*1000))


print("Press Enter to continue...")
scanner = spark.sparkContext._gateway.jvm.java.util.Scanner
sys_in = getattr(spark.sparkContext._gateway.jvm.java.lang.System, 'in')
result = scanner(sys_in).nextLine()

spark.stop()  # close the session
