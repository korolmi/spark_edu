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

# # Верхнеуровневая структура курса

# Попробуем набросать - что будет в курсе и понять, что надо делать



# **Вопросы к удеми**
#
# 1. насколько важно и полезно иметь в курсе в углу "говорящую морду"
# 2. как лучше бить на лекции (видео)
#     * в курсе по скале лекции были совсем небольшие и их было много
#     * в курсе по спарку лекций было не много, но они были длинные

# Название
#
# Spark for data engineering: learn core Spark by practice

# Краткое содержание
#
# * Кратко про спарк и про дата инженерию
#   * лекция
# * Основные сущности и отношения между ними
#   * лекция
# * Главные принципы
#   * датафреймы, строки и колонки
#       * лекция
#       * отсылка к референсу по датафреймам (общему) и колонкам
#       * практика: создадим дарафрейм (игрушечный)
#   * трансформации и действия
#       * лекция
#       * практика: посмотрим, когда что-то заработает
#   * параллелизм, план запросов и оптимизация (???)
#       * лекция
#       * отсылка к курсу
#       * практика - посмотрим план запросов
#   * ввод вывод
#       * лекция
#       * здесь должно быть все, чтобы можно было загрузить файл/таблицу и выгрузить файл/таблицу (с отсылкой к курсу)
#       * практика - загрузим
# * Познакомимся с API
#   * основные трансформации
#       * лекция (проход по теме) - на основе этой лекции родится какая-то сводка над референсом (основные трансформации)
#       * практика по основным трансформациям
#       * лекция - как бы я решал задачи
#       * задачи (несколько штук)
#   * агрегации и группировка
#       * лекция (проход по теме) - то же
#       * практика
#       * задачи
#       * отсылка к более углубленному курсу
#   * сортировка
#       * лекция
#       * практика
#       * задачи
#   * джойны и юнионы
#       * лекция
#       * практика
#       * задачи
# * Заключение
#   * лекция
#   
# Итого даже беглым взглядом получается
#
# * 11 лекций
# * 8 практик
# * (сосчитать) 20 задач
# * сколько-то юпитеров
# * 3 набора данных

# Отличия лекций от практик
#
# Лекция - это рассказ (голос). Подложка - PDF (подумать, как его делать - скорее всего, оперофисом)
#
# Тут все просто
#
# * слайд
# * под слайд записывается голос
# * накладываем одно на другое
# * клеим одно за другим
#
# Практика - это проход по книжке и выполнение действий в книжке. Наверное, надо научиться показывать (открывать) следующие узлы в книжке по ходу рассказа (чтобы не отвлекать слушателя). Можно для этого попробовать использовать фолдируемый контент, хотя - все равно монтировать (не писать же все подряд большим куском). Тогда в процессе монтажа и заниматься открыванием/закрыванием 
#
# * монтировать будем запись экрана (голос и видео)
# * перед началом очередной части переносим нужный кусок в видимую часть
# * отрабатываем эту часть (скролируя по ходу действия)
# * останавливаем запись

# Пример практики: джойны
#
# Часть 1: Посмотрим на данные
#
# * маркдаун с описанием одного датасета
# * ячейка с датасетом и show()
# * выполняем (оно скроллирует)
# * то же с другим датасетом
# * выполняем
# * подытоживаем - обращаем внимание на разницы в данных
#
# Часть 2: иннер джойн
#
# * (перенесли md, код в открытую часть)
# * md с кратким напоминанием того, что такое иннер джойн
# * ячейка с кодом джойна
# * выполняем, комментирууем
# * ячейка с другим кодом (если есть)
# * выполняем, комментируем
# * отсылка к референсу
#
# И так далее
#
# Тут вот непонятка: каждая часть может быть отдельной лекцией (технически - она будет отдельным видео). Как лучше?
#

# **Связь практики и раздаваемых книжек**
#
# Я буду раздавать книжки, по которым буду проходить практические занятия. И в то же время эти книжки проговаривать в формате лекции. Как это лучше совместить?
#
# С точки зрения обучения лучше сначала пройтись по верхам (обозреть сверху, например, джойны). А потом попрактиковаться. Но можно и наоборот 
#
# * поговорили про иннер джойн
# * практика (попробовали на данных)
#
# Наверное, так лучше:
#
# * курс у них навеки остается, они могут его "мотать" как им будет удобно
#
# **Вообще надо отказаться от слайдов**
#
# Пусть все будет в книжках. Механизм открытия книжек наладить да и все.
#
# Да, это возможно - см. https://dzone.com/articles/creating-presentations-with-jupyter-notebook
#
# получается вполне сносно, главное, что все остается в юпитерах - не нужны другие инструменты. Захочется, конечно, какую-то подложку сделать (чтобы не на белом фоне), но это научимся постепенно.

# Бесплатный курс 
#
# * Что такого хорошего в спарке
# * Из чего он состоит
# * Где его можно технически запускать
# * Где и как его можно взять (кратко) - подробно в другом курсе
#
# Подготовительный курс
#
# * Что есть спарк - отсылка на другой бесплатный курс
# * Настройка юпитера и юпитекста
# * Установка спарка и связь с юпитером
# * Как можно связать с Хадупом 
# * Где можно взять хадуп
#

# **Куда копать дальше**
#
# (в плане обучения - дальнейших курсов)
#
# План запросов: отдельная большая тема для вдумчивых (но можно попробовать сделать ее простой). Просто о том, как читать план запросов.
#
# Параллелизм и оптимизация: партиции, управление параллелизмом, оптимизация. Сослаться на предыдущий курс, поговорить про визуальный интерфейс, что там есть что и как пользоваться
#
# Агрегация и оконные функции: есть что поделать
#
# Ввод вывод: про оптимизацию, кратко форматы файлов и т.п.
#
# Спарк, юпитер, айрфлоу и ливи: подумать... Может быть, это сделать прямо вторым???
#
# RDD: отдельный разговор (надо только понять, что именно там можно найти интересного)
#
# Стриминг и ML - непонятно...
