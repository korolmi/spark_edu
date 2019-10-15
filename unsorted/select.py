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

# + {"spe": {"lang": "ru"}, "cell_type": "markdown"}
# # select: выбор колонок
# -

# Эта книжка переехала в соответствующее место в дереве, здесь можно смело "упражняться" - это не "боевой" вариант

# + {"spe": {"lang": "ru"}, "cell_type": "markdown"}
# Метод select() позволяет оставить в датафрейме только нужные его колонки
#
# `select(*cols)`
#
# Projects a set of expressions and returns a new DataFrame.
#
# Parameters
#
# cols – list of column names (string) or expressions (Column). If one of the column names is ‘*’, that column is expanded to include all columns in the current DataFrame.
#
# -

# Выполните следующую ячейку для инициализации Spark и подготовки данных

from startup import figDf, sp

# Изначально наш датафрейм с математическими фигурами выглядит так:

sp.sparkContext.uiWebUrl

figDf.show()

# ## Простые примеры использования

# **Простой пример select**
#
# создадим новый датафрейм с двумя колонками - id и name
#
# В качестве параметров используем строки

figDf.select("id", "name").show()

# **То же самое, но с колонками**
#
# в качестве параметров используем выражения (колонки)

figDf.select(figDf.id, figDf.name).show()

# и можно смешивать - колонки (выражения) и строковые имена колонок

figDf.select(figDf.id, "name").show()

# Если ошибиться с именем колонки, получим такое (exception)

figDf.select("id", "noname").show()

# **select с выражениями**
#
# Колонки - частный случай выражения. 
#
# С числами все просто

figDf.select(figDf.id, figDf.points+1).show()

# Со строками все сложнее - простое выражение не пройдет:

figDf.select(figDf.id, "Name is: " + figDf.name).show()

# Нужно использовать функции (о них - см. здезь)

from pyspark.sql import functions as f
figDf.select(figDf.id, f.concat(f.lit("Name is: "),figDf.name)).show(truncate=False)

# В последнем примере получили "не красивое" имя колонки, исправим это с помощью метода alias (см. здезь)

from pyspark.sql import functions as f
figDf.select(figDf.id, f.concat(f.lit("Name is: "),figDf.name).alias("longname")).show(truncate=False)

# **select для добавления колонок**
#
# select может не только уменьшить, но и увеличить количество колонок, например

from pyspark.sql import functions as f
figDf.select("*", f.concat(f.lit("Name is: "),figDf.name).alias("longname")).show(truncate=False)

# **Изменение порядка колонок в датафрейме**
#
# Колонки в новом датафрейме будут расположены именно в том порядке, как мы указали в параметрах. 
#
# Например, в нашем исходном датафрейме порядок таков: id,name,points,dimensions,description
#
# Мы можем сделать его, например, таким: name,description,id,points,dimensions

figDf.select("name","description","id","points","dimensions").show()

# ## Для чего это бывает нужен select

# Когда бывает нужно выбрать колонки из датафрейма
#
# Случай 1: Основная ситуация - требуется подмножество колонок из (потенциально большого) набора колонок исходного датафрейма. Полная аналогия с частью "select" одноименного SQL оператора 
#
# Случай 2: Требуется изменить порядок колонок датафрейма для, например, объединения (union) с другим датафреймом. 

# ## Попробуйте сами

# Задача 1: Создайте датафрейм с колонками points, description

figDf.select().show()

# Задача 2: Создайте датафрейм, в котором останется описание (description) и разница (новая колонка diff), между количеством точек (points) и размерностью (dimension)

figDf.select().show()

# ## Задачи посложнее

# Здесь нужны комплексные задачи, которые будут подтягиваться из общего репозитория
#
# Перед каждой задачей будет краткое описание требований (что нужно прочитать).

sp.stop()
