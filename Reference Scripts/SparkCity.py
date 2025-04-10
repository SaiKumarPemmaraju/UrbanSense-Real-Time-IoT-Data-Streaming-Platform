import time
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, TimestampType, DoubleType, IntegerType
from pyspark.sql.functions import from_json, col
from pyspark.sql.dataframe import DataFrame

from config import configuration


def read_kafka_topic(spark, topic, schema):
    return (
        spark.readStream
            .format('kafka')
            .option('kafka.bootstrap.servers', 'broker:29092')
            .option('subscribe', topic)
            .option('startingOffsets', 'earliest')
            .load()
            .selectExpr("CAST(value AS STRING)")
            .select(from_json(col("value"), schema).alias("data"))
            .select("data.*")
            .withWatermark("timestamp", "2 minutes")
    )


def streamWriter(input: DataFrame, checkpointFolder, output):
    return (
        input.writeStream
            .format('parquet')
            .option('checkpointLocation', checkpointFolder)
            .option('path', output)
            .outputMode('append')
            .start()
    )


def main():
    spark = SparkSession.builder.appName("SmartCityStreaming") \
        .config("spark.jars.packages",
                "org.apache.spark:spark-sql-kafka-0-10_2.13:3.5.5,"
                "org.apache.hadoop:hadoop-aws:3.3.1,"
                "com.amazonaws:aws-java-sdk:1.11.469") \
        .config("spark.hadoop.fs.s3a.impl", "org.apache.hadoop.fs.s3a.S3AFileSystem") \
        .config("spark.hadoop.fs.s3a.access.key", configuration.get('AWS_ACCESS_KEY')) \
        .config("spark.hadoop.fs.s3a.secret.key", configuration.get('AWS_SECRET_KEY')) \
        .config('spark.hadoop.fs.s3a.aws.credential.provider', 'org.apache.hadoop.fs.s3a.SimpleAWSCredentialsProvider') \
        .getOrCreate()

    spark.sparkContext.setLogLevel("WARN")

    # Add timestamp to make checkpoint folders unique per run
    timestamp = str(int(time.time()))

    # Schemas
    vehicleSchema = StructType([
        StructField("id", StringType(), True),
        StructField("deviceId", StringType(), True),
        StructField("timestamp", TimestampType(), True),
        StructField("location", StringType(), True),
        StructField("speed", DoubleType(), True),
        StructField("direction", StringType(), True),
        StructField("make", StringType(), True),
        StructField("model", StringType(), True),
        StructField("year", IntegerType(), True),
        StructField("fuelType", StringType(), True)
    ])

    gpsSchema = StructType([
        StructField("id", StringType(), True),
        StructField("deviceId", StringType(), True),
        StructField("timestamp", TimestampType(), True),
        StructField("speed", DoubleType(), True),
        StructField("direction", StringType(), True),
        StructField("vehicleType", StringType(), True)
    ])

    trafficSchema = StructType([
        StructField("id", StringType(), True),
        StructField("deviceId", StringType(), True),
        StructField("cameraId", StringType(), True),
        StructField("location", StringType(), True),
        StructField("timestamp", TimestampType(), True),
        StructField("snapshot", StringType(), True)
    ])

    weatherSchema = StructType([
        StructField("id", StringType(), True),
        StructField("deviceId", StringType(), True),
        StructField("location", StringType(), True),
        StructField("timestamp", TimestampType(), True),
        StructField("temperature", DoubleType(), True),
        StructField("weatherCondition", StringType(), True),
        StructField("precipitation", DoubleType(), True),
        StructField("windSpeed", DoubleType(), True),
        StructField("humidity", IntegerType(), True),
        StructField("airQualityIndex", DoubleType(), True)
    ])

    emergencySchema = StructType([
        StructField("id", StringType(), True),
        StructField("deviceId", StringType(), True),
        StructField("incidentId", StringType(), True),
        StructField("type", StringType(), True),
        StructField("timestamp", TimestampType(), True),
        StructField("location", StringType(), True),
        StructField("status", StringType(), True),
        StructField("description", StringType(), True)
    ])

    # Reading from Kafka
    vehicleDF = read_kafka_topic(spark, topic='vehicle_data', schema=vehicleSchema).alias('vehicle')
    gpsDF = read_kafka_topic(spark, topic='gps_data', schema=gpsSchema).alias('gps')
    trafficDF = read_kafka_topic(spark, topic='traffic_data', schema=trafficSchema).alias('traffic')
    weatherDF = read_kafka_topic(spark, topic='weather_data', schema=weatherSchema).alias('weather')
    emergencyDF = read_kafka_topic(spark, topic='emergency_data', schema=emergencySchema).alias('emergency')

    # Writing to S3 with unique checkpoint directories
    query1 = streamWriter(
        vehicleDF,
        checkpointFolder=f's3a://spark-streaming-bucket01/checkpoints/vehicle_data_{timestamp}',
        output='s3a://spark-streaming-bucket01/data/vehicle_data'
    )

    query2 = streamWriter(
        gpsDF,
        checkpointFolder=f's3a://spark-streaming-bucket01/checkpoints/gps_data_{timestamp}',
        output='s3a://spark-streaming-bucket01/data/gps_data'
    )

    query3 = streamWriter(
        trafficDF,
        checkpointFolder=f's3a://spark-streaming-bucket01/checkpoints/traffic_data_{timestamp}',
        output='s3a://spark-streaming-bucket01/data/traffic_data'
    )

    query4 = streamWriter(
        weatherDF,
        checkpointFolder=f's3a://spark-streaming-bucket01/checkpoints/weather_data_{timestamp}',
        output='s3a://spark-streaming-bucket01/data/weather_data'
    )

    query5 = streamWriter(
        emergencyDF,
        checkpointFolder=f's3a://spark-streaming-bucket01/checkpoints/emergency_data_{timestamp}',
        output='s3a://spark-streaming-bucket01/data/emergency_data'
    )

    query5.awaitTermination()


if __name__ == "__main__":
    main()
