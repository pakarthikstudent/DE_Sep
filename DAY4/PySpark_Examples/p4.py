# start spark session
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("example1").getOrCreate()

data = [("pA",101),("pB",102),("pC",103)]
columns = ["pName","pID"]

df = spark.createDataFrame(data,columns)
df.show()
##
df = spark.read.csv("prod.csv",header=True,inferSchema=True)
df.printSchema()
df.show()
df.show(3)
##
# simple transformation
df.select("productName").show() # fetch specific column
df.filter(df.pcost >3000).show() # filter - rows
df.groupBy("pid").count().show() # group by and aggregate

## Sql Queries
df.createOrReplaceTempView("prod")
result = spark.sql("select * from prod where pcost >3000")
result.show()
