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

# + {"slideshow": {"slide_type": "notes"}, "cell_type": "markdown"}
# # Лекционные части курса

# + {"slideshow": {"slide_type": "slide"}, "cell_type": "markdown"}
# # Data engineering and Spark

# + {"slideshow": {"slide_type": "slide"}, "cell_type": "markdown"}
# ## What is Data Engineering
#
# * треугольник потребностей
# * другими словами - дата сайентист и облегчение его труда
# * основные задачи
# * вход и выход - таблицы

# + {"slideshow": {"slide_type": "slide"}, "cell_type": "markdown"}
# ## Spark and Hadoop
#
# * кластер уже есть - в нем хранятся данные
# * Spark кроме всего другого предоставляет преобразования данных (таблица - таблица)
# * парадигма hadoop - доставить вычисления к данным
# * spark доставляет вычисления к данным

# + {"slideshow": {"slide_type": "slide"}, "cell_type": "markdown"}
# ## How it works
#
# * картинка про драйвер и екзекьюторы
# * про питон и java
# * передача данных между узлами и на драйвер
# * про эффективность даже питона 11

# + {"slideshow": {"slide_type": "slide"}, "cell_type": "markdown"}
# # Main abstraction in Spark

# + {"slideshow": {"slide_type": "slide"}, "cell_type": "markdown"}
# Картинка с rdd dataset dataframe
#
# * обясняем кратко картинку
# * что-то надо сказать про параллелизм и партиции

# + {"slideshow": {"slide_type": "slide"}, "cell_type": "markdown"}
# ## RDD
#
# * key - value
# * пример для случая реляционных таблиц
# * отдельный курс
# * достуна во всех API 

# + {"slideshow": {"slide_type": "slide"}, "cell_type": "markdown"}
# ## Dataset
#
# * строка таблицы (одинаковая структура)
# * статическая типизация - набор строк одного и того же типа (как правило - структура)
# * доступна в Java/Scala API

# + {"slideshow": {"slide_type": "slide"}, "cell_type": "markdown"}
# ## Dataframe
#
# * основная наша абстракция
# * можно сказать, что это датасет, в котором строки имеют универсальный тип "Row"
# * позволяет Sparky работать со своими типами данных
# * доступна во всех API
# * структура данных этого курса

# + {"slideshow": {"slide_type": "notes"}, "cell_type": "markdown"}
# * Основные сущности и отношения между ними
# * Главные принципы
#   * датафреймы, строки и колонки
#   * трансформации и действия
#   * параллелизм, план запросов и оптимизация (???)
#   * ввод вывод
# * Познакомимся с API
#   * основные трансформации
#       * лекция (проход по теме) - на основе этой лекции родится какая-то сводка над референсом (основные трансформации)
#       * лекция - как бы я решал задачи
#   * агрегации и группировка
#   * сортировка
#   * джойны и юнионы
# * Заключение
#   * лекция
