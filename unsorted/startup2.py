# -*- coding: utf-8 -*-
import os
from pyspark.sql import SparkSession
from pyspark.sql.types import ArrayType, StructField, StructType, StringType, IntegerType

os.environ["SPARK_HOME"] = "/home/mk/mk_win/projects/SparkEdu/lib/python3.5/site-packages/pyspark"
os.environ["PYSPARK_PYTHON"] = "/usr/bin/python3"
os.environ["PYSPARK_DRIVER_PYTHON"] = "python3"
os.environ["PYSPARK_SUBMIT_ARGS"] = "pyspark-shell"

# Spark session
sp = SparkSession.builder.master("local").appName("general").getOrCreate()

# quarters data
data = [
    ( 1, 'first quarter', 'QI' ),
    ( 2, 'second quarter', 'QII' ),
    ( 3, 'third quarter', 'QIII' ),
    ( 4, 'fourth quarter', 'QIV' ),
]
schema = StructType([
    StructField('no', IntegerType(), True),
    StructField('name', StringType(), True),
    StructField('short', StringType(), True)
])
rdd = sp.sparkContext.parallelize(data)
qtrDf = sp.createDataFrame(rdd,schema)

#  figures data
data = [
    ('PNT', 'point', 1, 1, "точка"),
    ('LNS', 'line segment', 2, 2, "отрезок"),
    ('TRI', 'triangle', 3, 2, "треугольник"),
    ('QDR', 'quadrangle', 4, 2, "четырехугольник"),
    ('QDT', 'quadrant', 4, 2, "квадрат"),
]
schema = StructType([
    StructField('id', StringType(), True),
    StructField('name', StringType(), True),
    StructField('points', IntegerType(), True),
    StructField('dimensions', IntegerType(), True),    
    StructField('description', StringType(), True)
])
rdd = sp.sparkContext.parallelize(data)
figDf = sp.createDataFrame(rdd,schema)

message = """
Spark was successfully initialized.
Spart context is available via:   sp
Quarter data df:                  qtrDf

(...to stop Spark execute sp.stop()...)"""

print(message)

