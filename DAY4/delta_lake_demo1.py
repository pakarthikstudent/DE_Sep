#  (pyspark-env) student@paka:~$ pip install delta-spark
# ------------------------------ =========================
from pyspark.sql import SparkSession
from delta import configure_spark_with_delta_pip

# 1. Create SparkSession with Delta Lake
builder = (
    SparkSession.builder.appName("DeltaLakeExample")
    .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension")
    .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog")
)

spark = configure_spark_with_delta_pip(builder).getOrCreate()

# 2. Create sample DataFrame
data = [
    (1, "Alice", 25),
    (2, "Bob", 30),
    (3, "Charlie", 35),
]
columns = ["id", "name", "age"]

df = spark.createDataFrame(data, columns)

# 3. Write DataFrame to Delta table (local folder)
df.write.format("delta").mode("overwrite").save("delta-table")

# 4. Read Delta table
df_read = spark.read.format("delta").load("delta-table")
print("Initial Data:")
df_read.show()

# 5. Update data (add a new row)
new_data = [(4, "David", 40)]
df_new = spark.createDataFrame(new_data, columns)
df_new.write.format("delta").mode("append").save("delta-table")

# 6. Read updated table
print("After Insert:")
spark.read.format("delta").load("delta-table").show()

# 7. Time Travel Example (read old version)
print("Reading Version 0 (before insert):")
old_df = spark.read.format("delta").option("versionAsOf", 0).load("delta-table")
old_df.show()
