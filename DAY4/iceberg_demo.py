from pyspark.sql import SparkSession

# Start Spark with Iceberg extension
spark = (
    SparkSession.builder
    .appName("IcebergDemo")
    .config("spark.sql.extensions", "org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions")
    .config("spark.sql.catalog.local", "org.apache.iceberg.spark.SparkCatalog")
    .config("spark.sql.catalog.local.type", "hadoop")  # Using local FS
    .config("spark.sql.catalog.local.warehouse", "warehouse")  # Metadata + data files stored here
    .getOrCreate()
)

# Create table
spark.sql("""
    CREATE TABLE local.db.sample_iceberg (
        id BIGINT,
        data STRING
    )
    USING iceberg
""")

# Insert some rows
spark.sql("INSERT INTO local.db.sample_iceberg VALUES (1, 'hello'), (2, 'iceberg'), (3, 'table format')")

# Query table
print("Current Data:")
spark.sql("SELECT * FROM local.db.sample_iceberg").show()

# Check snapshots (time travel metadata)
print("Snapshots:")
spark.sql("SELECT * FROM local.db.sample_iceberg.snapshots").show()

spark.stop()
