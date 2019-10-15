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

# # Как инсталлировать
#
# Эта инструкция будет уточняться, возможно появятся варианты.

# Как минимальным образом установить Spark (я делал в virtualenv):
#
# 1. Должна быть предустановлена java
# 1. Сам Spark у меня был установлен вместе со scala (видимо)
# 2. pip install pyspark
# 3. pip install jupyter ipyparallel
# 4. jupyter notebook
#
# Далее в ноутбуке
#
# import os
# from pyspark.sql import SparkSession
#
# os.environ["SPARK_HOME"] = "<путь куда был установлен pyspark - /home/mk/mk_win/projects/SparkEdu/lib/python3.5/site-packages/pyspark>"
# os.environ["PYSPARK_PYTHON"] = "/usr/bin/python3"
# os.environ["PYSPARK_DRIVER_PYTHON"] = "python3"
# os.environ["PYSPARK_SUBMIT_ARGS"] = "pyspark-shell"
#
# Чтобы стартануть сессию делаем
#
# sp = SparkSession.builder.master("local").appName("имя_приложения").getOrCreate()
#
# После этого сессию можно видеть здесь:
#
# http://192.168.1.68:4040
#
# Чтобы остановить сессию делаем
#
# sp.stop()
#
# После этого сессия пропадает...
