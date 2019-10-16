# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
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

# * colName: string, name of the new column.
# * col: a Column expression for the new column.
#
# Returns a new DataFrame by adding a column or replacing the existing column that has the same name.
#
# The column expression must be an expression over this DataFrame; attempting to add
# a column from some other dataframe will raise an error.

import os
from pyspark.sql import SparkSession
os.environ["SPARK_HOME"] = "/opt/cloudera/parcels/CDH/lib/spark"
os.environ["PYSPARK_PYTHON"] = "/usr/bin/python3"
os.environ["PYSPARK_DRIVER_PYTHON"] = "python3"
os.environ["HADOOP_CONF_DIR"] = "/etc/hadoop/conf"
os.environ["PYSPARK_SUBMIT_ARGS"] = "pyspark-shell"

sp = SparkSession.builder.master("local").appName("withColumn").enableHiveSupport().getOrCreate()

sp.stop()

geoDf = sp.read.format("csv").option("header","true").load("file:///data/jupyter/spark_edu/gem_figs.txt")
geoDf.show()

# **smoke** добавим колонку - количество граней (неправильное - поправим в задаче)

geoDf.withColumn("edges",geoDf.points-1).show()

# переделаем колонку name - добавим размерность через "_"
#
# используем функции
#
# * lit()
# * concat()
# * cast()

from pyspark.sql import functions as f
geoDf.withColumn("name",f.concat(geoDf.name,f.lit("_"),geoDf.dim.cast("string"))).show()

# добавим колонку - литерал: признак импортирования

geoDf.withColumn("was_imported",f.lit(1)).show()

# попробуем добавить колонку из другого датафрейма - получим ошибку

newDf = geoDf.toDF("c1","c2","c3","c4")
try:
    geoDf.withColumn("dim_dim",newDf.c4).show()
except Exception as e:
    print("error:",str(e))

# примерно то же самое получим, если ошибемся с именем колонки в выражении (smoke test)

try:
    geoDf.withColumn("edges",geoDf.point-1).show()
except Exception as e:
    print("error:",str(e))

# Для чего нужна эта функция
#
# Наиболее частые случаи:
#
# * Добавление вычисляемой колонки: нужно добавить колонку, которую можно вычислить по колонкам исходного датафрейма
# * Добавление константной колонки: добавляем колонку с константой 
#
# Частный случай:
#
#

# Задачи
#
# 1. Добавить колонку "has_square" - определяет, есть ли площадь у фигуры (если количество точек больше 2х). Нужна функция when()
# 2. Добавить колонку "math" с текстовым значением "geometry"). Нужна функция lit()
# 3. Добавить колонку "math_sect" со значением "dim"D (2D,3D,...). Нужны функции concat(), cast(), lit()
# 4. Добавить "правильную" колонку "edges" - для точки и отрезка = -1, для остальных = -0

# Задачи комплексные
#
# 1. 
