# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.4'
#       jupytext_version: 1.2.4
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# # Создадим данные для обучения

# +
import os
from pyspark.sql import SparkSession
from pyspark.sql.types import ArrayType, StructField, StructType, StringType, IntegerType

os.environ["SPARK_HOME"] = "/home/mk/mk_win/projects/SparkEdu/lib/python3.5/site-packages/pyspark"
os.environ["PYSPARK_PYTHON"] = "/usr/bin/python3"
os.environ["PYSPARK_DRIVER_PYTHON"] = "python3"
os.environ["PYSPARK_SUBMIT_ARGS"] = "pyspark-shell"
# -

sp = SparkSession.builder.master("local").appName("data").getOrCreate()

sp.stop()

# +
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

# Convert list to RDD
rdd = sp.sparkContext.parallelize(data)

# Create data frame
df = sp.createDataFrame(rdd,schema)
df.show()
