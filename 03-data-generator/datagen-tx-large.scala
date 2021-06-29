/* How to run this script:

To run in Spark local mode - for testing purposes:
    $   $SPARK_HOME/bin/spark-shell --driver-memory 4g  --executor-memory 4g  -i datagen-tx-large.scala

To run at server mode:

    First start spark server:
    $   $SPARK_HOME/sbin/start-all.sh

    And run the generator
    $   $SPARK_HOME/bin/spark-shell  --driver-memory 4g  --executor-memory 4g  \
            --master spark://melbourne:7077   -i datagen-tx-large.scala

If running on a Hadoop cluster
    $   $SPARK_HOME/bin/spark-shell  --driver-memory 4g  --executor-memory 4g  \
            --master yarn   -i datagen-tx-large.scala

*/
// ---- Configuration start ----
val aMillion = 1e6.toInt
val numRows = aMillion * 1
//val numRows = Int.MaxValue
// val numRows = 10
//val numPartitions = numRows/1000000
val numPartitions = 10

// optionally, save
// location can be local dir, or HDFS dir
// val save_location = ""   // empty for no save
val save_location = "../data/transactions"
// val save_location = "hdfs://user/me/data.tx"

val save_format = "csv"
// val save_format = "parquet"
// ---- Configuration end ----

/*
data sizes:

    CSV : 1 million rows = 172 MB
    Parquet : 1 million rows = 95 MB

    CSV : 1 million rows =  1.7 GB
    Parquet : 10 million rows = 886 MB
*/

// Reference : https://stackoverflow.com/questions/55083170/efficient-way-to-generate-large-randomized-data-in-spark

import org.apache.spark.rdd.RDD
import org.apache.spark.{Partition, SparkContext, TaskContext}

import scala.collection.Iterator
import scala.reflect.ClassTag
import java.util.UUID.randomUUID



println("\n\n### numRows=%,d  ,   numPartitions=%,d".format(numRows, numPartitions))

// Each random partition will hold `numValues` items
final class RandomPartition[A: ClassTag](val index: Int, numValues: Int) extends Partition {
  //Set the start and end time
  //As there are no conveince API for adding ms (long) directly using an workaround
  val startDate = "2015-01-01"
  val endDate = "2020-12-31"

  import java.text.SimpleDateFormat
  val op_date_format = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss.SSS")
  val ip_date_format = new java.text.SimpleDateFormat("yyyy-MM-dd")
  val start_time = ip_date_format.parse(startDate).getTime()
  val end_time = ip_date_format.parse(endDate).getTime()

  //one days ms
  val diff_ms = 864000000

  //Get the 6 year days
  //This can be calculated as well for now it is
  val diff_days=365*6+1

  //CC generation
  val MinimumLength = 15
  val MaximumLength = 15
  //Card number generator
  def generate_cc: String = {
    val payload: String = {
      import scala.util.Random

      val length: Int = {
        val min: Int = MinimumLength
        val max: Int = MaximumLength
        min + Random.nextInt((max - min) + 1)
      }

      def randomDigit: Int =
        Random.nextInt(10) // 0 to 9

      (1 to length) // Range.Inclusive
        .map(_ => randomDigit) // IndexedSeq[Int]
        .mkString // String
    }
    "4"+payload.toString
    //"%415d".format(payload.toString)
  }

  //Response code
  val response_codes = Map(
                            "00" -> "approved", 
                            "03" -> "invalid_merchant",
                            "06" -> "error", 
                            "08" -> "Honour with identification",
                            "13" -> "Invalid amount", 
                            "14" -> "Invalid card number",
                            "33" -> "Expired card")

  //There is no direct way for weight base selection, this is an workaround
  def generate_response_code: String = {
    val rand_num = scala.util.Random.nextInt(100) + 1
    var resp_code = "00"

    if (rand_num > 80 && rand_num < 83)
      resp_code = "03"
    else if (rand_num == 83)
      resp_code = "06"
    else if (rand_num > 83 && rand_num < 94)
      resp_code = "08"
    else if (rand_num > 94 && rand_num < 98)
      resp_code = "13"
    else if (rand_num > 98 && rand_num < 100)
      resp_code = "14"
    else if (rand_num == 100)
      resp_code = "33"

    resp_code
  }

  //Create merchant names
  val merchant_name_1 = Seq("Super", "Awesome", "Best", "Sunny", "First", "Summer Winds", "Four Seasons", "Sun Shine", "Star")
  val merchant_name_2 = Seq("Dry cleaners", "Restaurant", "Auto", "Flowers", "Bakery", "Toys", "Nursery", "Hardware", "Liquors", "Donuts")

  //generate merchant names
  def generate_merchant_name(): String = {
      "%s %s".format (
            merchant_name_1(scala.util.Random.nextInt(merchant_name_1.length)),
            merchant_name_2(scala.util.Random.nextInt(merchant_name_2.length)))
  }

  //Streets lookup
  val streets = Seq("Main Street", "Broadway", "Hillview St", "Market St", "Beach Road", "Alameda Avenue")

  //Cities lookup
  val cities = Seq("San Jose", "San Francisco", "Redwood City", "Foster City", "Burlingame", "San Mateo")

  //States lookup
  val states = Seq("AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA",
    "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD",
    "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ",
    "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC",
    "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY")

  val countries = Seq("USA")

  //generate address
  def generate_address: String = {
      "%d %s, %s, %s, %s".format ( 
          scala.util.Random.nextInt(1000) + 1,   // street address
          streets(scala.util.Random.nextInt(streets.length)), 
          cities(scala.util.Random.nextInt(cities.length)), 
          states(scala.util.Random.nextInt(states.length)),
          countries(scala.util.Random.nextInt(countries.length)))
  }

  //generate merchant address with merchant name and address
  def generate_merchant_address: String = {
    "%s, %s".format (generate_merchant_name , generate_address)
  }
    
  def generate_merchant_id: String = {
      val a = scala.util.Random.nextInt(150)
      if (a <= 100)
          return a.toString;
      else
          return 0.toString;
  }

  //Generate tuples based on below formulae
  def generateTuples: ((String, String, String, String, String, String, String, String, String, String, String), (String, String, String, String, String, String, String, String, String, String, String)) = {

    val id = randomUUID().toString
    val merchant_type = "%04d".format(scala.util.Random.nextInt(9999) + 1)
    val amount_customer = (scala.util.Random.nextInt(10000) + 100.0) / 10
    val amount_merchant = amount_customer * .97
    val cc_num = generate_cc
    val merchant_id = generate_merchant_id

    //We need to get the random number here... probaly we can do something here
    //since there is no random for long, we would do for days and the and int which would for a day
    val rand_days = scala.util.Random.nextInt(diff_days)
    val rand_req_ms = scala.util.Random.nextInt(diff_ms)
    val res_time = rand_req_ms + 300 + scala.util.Random.nextInt(30000)

    import java.util.Calendar
    val cal_req = Calendar.getInstance
    cal_req.setTimeInMillis(start_time)
    cal_req.add(Calendar.DATE,rand_days)
    cal_req.add(Calendar.MILLISECOND,rand_req_ms)

    //We might need to create here
    val cal_res = Calendar.getInstance
    cal_res.setTimeInMillis(start_time)
    cal_res.add(Calendar.DATE,rand_days)
    cal_res.add(Calendar.MILLISECOND,res_time);

    //Convert into dates
    val merchant_add = generate_merchant_address
    val response_code = generate_response_code

    //Generate a random 2 decimal float here
    val req = Tuple11 (id,
                      op_date_format.format(cal_req.getTime), 
                      "0100", 
                      cc_num, 
                      "%.2f".format(amount_customer), 
                      merchant_type, 
                      merchant_id,
                      merchant_add, 
                      "",
                      "", 
                      "")
    val res = Tuple11(randomUUID().toString,
                     op_date_format.format(cal_res.getTime), 
                     "0110", 
                     cc_num, 
                     "%.2f".format(amount_customer), 
                     merchant_type, 
                     merchant_id,
                     merchant_add, 
                     id,
                     "%.2f".format(amount_merchant), 
                     response_code)

    (req, res)
  }


  def values: Iterator[A] = Iterator.fill(numValues)(generateTuples).asInstanceOf[Iterator[A]]
}


// The RDD will parallelize the workload across `numSlices`
final class RandomRDD[A: ClassTag](@transient private val sc: SparkContext, numSlices: Int, numValues: Int) extends RDD[A](sc, deps = Seq.empty) {

  // Based on the item and executor count, determine how many values are
  // computed in each executor. Distribute the rest evenly (if any).
  private val valuesPerSlice = numValues / numSlices
  private val slicesWithExtraItem = numValues % numSlices

  // Just ask the partition for the data
  override def compute(split: Partition, context: TaskContext): Iterator[A] =
    split.asInstanceOf[RandomPartition[A]].values.toIterator

  // Generate the partitions so that the load is as evenly spread as possible
  // e.g. 10 partition and 22 items -> 2 slices with 3 items and 8 slices with 2
  override protected def getPartitions: Array[Partition] =
    ((0 until slicesWithExtraItem).view.map(new RandomPartition[A](_, valuesPerSlice + 1)) ++
      (slicesWithExtraItem until numSlices).view.map(new RandomPartition[A](_, valuesPerSlice))).toArray

}

var t1 = System.nanoTime()
// supplying numRows / 2, because each iteration generates 2 rows : request and response
val rdd1 = new RandomRDD[((String,String, String, String, String, String, String, String, String, String, String), (String, String,String,String, String, String, String, String, String, String, String))](spark.sparkContext, numPartitions, numRows/2)
var t2 = System.nanoTime()

import spark.implicits._
val df = rdd1.toDF().withColumn("id", monotonically_increasing_id + 123).selectExpr("id", "stack(2,`_1`,`_2`)")
  .withColumnRenamed("col0", "data") // default name of this column is col0
  .drop("id").selectExpr("data._1 as id", "data._2 as timestamp", "data._3 as mti", "data._4 as card_number", "data._5 as amount_customer", "data._6 as merchant_type", "data._7 as merchant_id", "data._8 as merchant_address","data._9 as ref_id", "data._10 as amount_merchant", "data._11 as response_code")
var t3 = System.nanoTime()
println("### Created data frame in %,.2f ms".format((t3 - t1) / 1e6))

// t1 = System.nanoTime()
// val count = df.count()  // force going through df
// t2 = System.nanoTime()
// println("### Counted %,d rows in %,.2f ms".format(count, (t2 - t1) / 1e6))

df.show(20, truncate=false)

if (!save_location.isEmpty) {
    val save_location2 = save_location + "/" + save_format
    t1 = System.nanoTime()
    if (save_format == "parquet")
        df.write.mode("overwrite").parquet(save_location2)
    else
        df.write.mode("overwrite").option("header",true).option("sep", ",").csv(save_location2)
    t2 = System.nanoTime()
    println("### Saved  to '%s' in %,.2f ms".format(save_location2, (t2 - t1) / 1e6))
}

// keep alive so we can check out the Spark UI
println("### Hit enter to terminate the program...:")
val line = Console.readLine
System.exit(0)



