# Structured streaming with Spark and Kafka


from pyspark.sql import SparkSession
import sys
from datetime import time

topic = "transactions"

spark = SparkSession \
    .builder \
    .appName("KafkaStructuredStreaming") \
    .getOrCreate()

print('### Spark UI available on port : ' + spark.sparkContext.uiWebUrl.split(':')[2])

sc = spark.sparkContext
sc.setLogLevel("WARN")

# option 1
df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", topic) \
    .option("startingOffsets", "latest").load()

# option 2: specify schema
# df = spark.readStream \
#     .format("kafka") \
#     .option("kafka.bootstrap.servers", "localhost:9092") \
#     .option("subscribe", topic).option("startingOffsets", "latest") \
#     .load().selectExpr("CAST(key AS STRING)", "CAST(value AS STRING)", "CAST(topic AS STRING)",
#                        "CAST(partition AS INTEGER)", "CAST(offset AS LONG)", "CAST(timestamp AS TIMESTAMP)")

df.printSchema()

query = df.writeStream \
    .outputMode("append") \
    .format("console") \
    .queryName("Read from Kafka topic:" + topic) \
    .start()

# simple, wait for ever
query.awaitTermination()

spark.stop()