# start spark session
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("example1").getOrCreate()

data = [("pA",101),("pB",102),("pC",103)]
columns = ["pName","pID"]

df = spark.createDataFrame(data,columns)
df.show()
