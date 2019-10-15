# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.2'
#       jupytext_version: 1.2.4
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# %% [markdown]
# # drop: удаление колонок

# %% [markdown]
# Метод drop() позволяет удалить из в датафрейма ненужные его колонки
#
# `drop(*cols)`
#
# Returns a new DataFrame that drops the specified column.
# This is a no-op if schema doesn't contain the given column name(s).
#
# Parameters
#
# cols: a string name of the column to drop or Column to drop, or a list of string name of the columns to drop.

# %% [markdown]
# Выполните следующую ячейку для инициализации Spark и подготовки данных

# %%
from startup import figDf, sp

# %% [markdown]
# Изначально наш датафрейм с математическими фигурами выглядит так:

# %%
sp.sparkContext.uiWebUrl

# %%
figDf.show()

# %% [markdown]
# ## Простые примеры использования

# %% [markdown]
# **Простой пример drop**
#
# создадим новый датафрейм, удалив колонки - id и name
#
# В качестве параметров используем строки

# %%
figDf.drop("id", "name").show()

# %% [markdown]
# **То же самое, но с колонками**
#
# казалось бы - какая разница (строки или колонки), но... нельзя. При использовании колонок можно указать только одну колонку (в отличие от того же select())

# %%
figDf.drop(figDf.id, figDf.name).show()

# %%
figDf.drop(figDf.id).show()

# %% [markdown]
# Зато если ошибиться с именем колонки, то не произойдет ничего страшного - удалится то, где не ошиблись.

# %%
figDf.drop("id", "noname").show()

# %% [markdown]
# ## Для чего это бывает нужен drop

# %% [markdown]
# Когда бывает нужно удалять колонки из датафрейма
#
# Случай 1: Основная ситуация - требуется удалить небольшое подмножество колонок из набора колонок исходного датафрейма. Колонки можно удалять и select-ом, вопрос - что проще: перечислить колонки, которые остались, или перечислить колонки, которые нужно удалить.
#
# Случай 2: Также часто бывает нужно удалить "лишние" колонки после объединения (join) двух датафреймов.

# %% [markdown]
# ## Попробуйте сами

# %% [markdown]
# Задача 1: Удалите из датафрейма колонки points, description

# %%
figDf.drop(___).show()

# %% [markdown]
# ## Задачи посложнее

# %% [markdown]
# Здесь нужны комплексные задачи, которые будут подтягиваться из общего репозитория
#
# Перед каждой задачей будет краткое описание требований (что нужно прочитать).

# %%
sp.stop()
