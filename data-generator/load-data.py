## Run it as 
##  $SPARK_HOME/bin/spark-submit  --master local[*] --driver-class-path ../logging/  load-data.py

from pyspark.sql import SparkSession
import time

spark = SparkSession.builder.appName("data-gen-test").getOrCreate()
print('### Spark UI available on port : ' + spark.sparkContext.uiWebUrl.split(':')[2])

## Load the generated files and test
df = spark.read.csv('data/transactions.csv/*', header=True, inferSchema=False)
t1 = time.perf_counter()
count = df.count()
t2 = time.perf_counter()

print ('count : {:,}'.format(count))
df.printSchema()
df.show(10, truncate=False)


print("Press Enter to continue...")
scanner = spark.sparkContext._gateway.jvm.java.util.Scanner
sys_in = getattr(spark.sparkContext._gateway.jvm.java.lang.System, 'in')
result = scanner(sys_in).nextLine()

spark.stop()  # close the session
