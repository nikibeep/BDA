from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, IntegerType, StringType

# Create a Spark session
spark = SparkSession.builder.appName("StudentAttendanceJoin").getOrCreate()

# Define the schema for students and attendance data
students_schema = StructType([
    StructField("student_id", IntegerType(), True),
    StructField("student_name", StringType(), True)
])

attendance_schema = StructType([
    StructField("date", IntegerType(), True),
    StructField("student_id", IntegerType(), True),
    StructField("days_attended", IntegerType(), True)
])

# Read the data from HDFS
# Update the paths to local file paths
students = spark.read.csv("file:///home/kali/hadoopjoin/students.txt", schema=students_schema, sep=",")
attendance = spark.read.csv("file:///home/kali/hadoopjoin/days_attended.txt", schema=attendance_schema, sep=",")


# Perform the join operation
joined_data = students.join(attendance, on="student_id", how="inner")

# Show the result
joined_data.show()

# Stop the Spark session
spark.stop()
