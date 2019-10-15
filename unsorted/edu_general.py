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

# # Про обучение SPARKу

# **Это немного устарело**
#
# общие мысли из самолета...
#
# здесь немного мыслей про то, как могут быть устроены учебные материалы, курсы и т.п.

# Кого учим - тех, кто слышал что-то про спарк и хочет узнать поподробнее
#
# Как учим - немного теории и много практики, даем возможность все попробовать в ноутбуках (главным образом)
#
# Фишка - ноутбуки, мелкая нарезка и практика
#
# Какие будут курсы
#
# * классические: последовательное изложение, мелкая нарезка (работа с источниками, датафреймы, датасеты, rdd, возможно еще мельче)
# * тематические: задачи обработки данных (из дата инженерии)
# * сборные (как идея): собираемые в кросс-темы (непонятно)
#
# Все это будет сопровождаться референсом (тоже мелко нарезанным и с понятными урлами), из референса должны быть ссылки на "поучиться/попрактиковаться".

# Пример курса в мелкой нарезке
#
# select()
#
# это где-то внутри части про датафреймы. Особо рассказывать про эту функцию нечего, рассказ про другое. В рассказе ссылки на референс, который является html-м (возможно, прямо книжка в неком застывшем виде - как книга про спарк).
#
# урл something/dataframe/select
#
# данные уже загружены (два датафрейма - фигуры и страны)
#
# * чуть объясняем, что такое select
# * примеры (одна колонка, несколько, переименование и т.п.)
# * типовые применения (придумать, нагуглить, добавлять)
# * навигация (горизонтальная - что еще подобного есть, вертикальная - что выше, есть ли более детальные ниже)
# * задачки (в том числе про эту функцию, задачки будут более комплексными)
#
# В книжке есть ссылка/текст про то, что можно все это попробовать - надо придумать, как сделать это интересным (попробовать). Наверное, интерес в том, что у тебя на локальном (своем) компьютере появляется возможность все понажимать - оно все твое.

# Что надо делать - с чего начать
#
# * придумать первый курс, ибо он продается
# * понять, какое обеспечение ему нужно
# * сделать минимум
# * сделать бесплатный курс про подготовку к основному (юпитекст, спарк, контрольный пример)
# * зарегиться на удеми как учитель
# * посмотреть, где еще есть возможность оставить ссылки (на курсы)
# * надо научиться пользоваться линкед ином
#

# Какой первый курс
#
# * бесплатно можно рассказать - что такое спарк и зачем он нужен (только вот где рассказать). Рассказать можно в бесплатном курсе
# * бесплатный курс (или даже два)
#
#   * подготовка к курсу (юпитер, юпитекст, спарк)
#   * что такое спарк, точнее - чем он интересен и выделяется 
#
# Что может быть интересно
#
# * про спарк уже много всего сделано, нужно выделиться
# * выделиться можно ноутбуками, но до этого еще нужно добраться (понять, что книжки в моем курсе это клево)
# * бесплатным курсом (подготовкой) можно заинтересовать
#
# варианты
#
# * спарк в задачах дата инженерии (пока непонятно, что это...)
# * чтение планов исполнения - отдельный и не очень связанный, но интересный (пока сам не умею)
# * датафреймы: эффективное использование (банально, надо посмотреть, что другие пишут)
# * спарк мелкими кусочками (bite sized) - посмотреть, кстати, на датакамп - может быть, там что-то такое сделать?
#
# вот с последнего можно и начать... сделать цену поменьше, объяснить в бесплатном курсе про общий подход. Еще нужно добавить про подход "от наиболее нужного к наименее нужному".
#
# можно попробовать свой опыт постепенно описывать (реальные примеры преобразований), но только надо быть уверенным, что делаешь хорошо, иначе засмеют

# а если не курс продавать? продать можно сами книжки
#
# * про датафреймы
# * про рдд
# * про датасеты (нужны они кому-нибудь?)
# * про работу со стораджами
#
# в видео (ютуб) рассказать, как этим пользоваться (по сути это тот же подготовительный бесплатный курс)
#
# чем курс отличается от книжки?
#
# в курсе есть генеральная линия - начал, прошел до конца = чему-то научился (кстати, надо это не забывать...)
#
# книжка должна быть
#
# * хорошим референсом
# * возможностью просто попрактиковаться
# * надо подумать над мыслью создания настраиваемого под пользователя референса (настраиваем набор функций и объем предоставляемой информации)
#

# как можно сгруппировать нарезку
#
# * манипуляции с датафреймами (обзор в стиле книжки - что можно делать: добавлять строки и столбцы, убирать строки и столбцы, изменять строки и столбцы), просто перечень функций, которые это позволяют делать
# * агрегация
# * упорядочение и оконные функции
# * джойны и юнионы
#
# ориентируемся на дата инженерные функции - то есть на преобразование данных, делание датафреймов из других датафреймов
