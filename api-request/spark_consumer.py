from pyspark.sql import SparkSession
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, TimestampType
from pyspark.sql.functions import from_json, col

spark = SparkSession.builder.appName("UserStreamApp").getOrCreate()
spark.sparkContext.setLogLevel("ERROR")

schema = StructType(
    [
    StructField("name", StringType(), True),
    StructField("gender", StringType(), True),
    StructField("email", StringType(), True),
    StructField("phone", StringType(), True),
    StructField("address", StringType(), True),
    StructField("picture", StringType(), True),
    StructField("username", StringType(), True),
    StructField("registered_date", TimestampType(), True)
    ]
)
time
# Đọc stream từ Kafka
df = (
    spark.readStream
        .format("kafka")
        .option("kafka.bootstrap.servers", "kafka:9092")
        .option("subscribe", "user_topic")
        .option("startingOffsets", "earliest")
        .load()
)
kafka_df = df.selectExpr("CAST(key AS STRING)", "CAST(value AS STRING)")
json_df = kafka_df.select(from_json(col("value"), schema).alias("data")).select("data.*")


query = (
    json_df.writeStream
        .outputMode("append")
        .format("console")
        .option("truncate", False)
        .trigger(availableNow= True)
        .start()
)

query.awaitTermination()