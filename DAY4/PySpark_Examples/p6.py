# start spark session
from pyspark.sql import SparkSession

from pyspark.ml.feature import VectorAssembler
from pyspark.ml.regression import LinearRegression

spark = SparkSession.builder.appName("linear_reg").getOrCreate()

data = [(1,1.0,2.0),(2,2.0,3.0),(3,3.0,4.0)]
df = spark.createDataFrame(data,["label1","feature1","feature2"])

assembler = VectorAssembler(inputCols=["feature1","feature2"],outputCol="features")

train = assembler.transform(df).select("label","features")

lr = LinearRegression(featuresCol="features",labelCol="label")
model = lr.fit(train)
print("Coefficient:",model.coefficients)
print("Intercept:",model.intercept)
