from pyspark.sql import SparkSession
from pyspark.ml.classification import LogisticRegression
from pyspark.ml.feature import VectorAssembler
from pyspark.ml import Pipeline

spark = SparkSession.builder.appName("MLibExample").getOrCreate()

data = [(0.0,1.0,3.0,0.0),
        (1.0,2.0,1.0,1.0),
        (0.0,2.0,2.0,0.0),
        (1.0,3.0,3.0,1.0), ]

columns = ["feature1","feature2","feature3","label"]

df = spark.createDataFrame(data,columns)
assembler = VectorAssembler(inputCols=["feature1","feature2","feature3"],outputCol="features")

## model
lr = LogisticRegression(featuresCol="features",labelCol="label")
pipeline = Pipeline(stages=[assembler,lr])

model = pipeline.fit(df) # Train

predictions = model.transform(df)
predictions.select("features","label","predictions","probability").show()
