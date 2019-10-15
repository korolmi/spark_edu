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

# # select: choose (select) columns

# + {"spe": {"what": "docstr"}, "cell_type": "markdown"}
# Projects a set of expressions and returns a new DataFrame.
#
# Parameters:
#
# * cols: list of column names (string) or expressions (Column).
#
# If one of the column names is '*', that column is expanded to include all columns in the current DataFrame.
# -

# **Init**: execute next cell to start Spark and get data ready

# %run /home/mk/mk_win/projects/SparkEdu/notebooks/core/startup

# Here is our simple "querter data" dataframe

qtrDf.show()

# ## Simple use cases

# **Simlest select example**
#
# Let us create new dataframe with just two columns - 'no' and 'name'
#
# We use column string names in this example

qtrDf.select("no", "name").show()

# **Simplest select using columns**
#
# We can use column as dataframe attribute

qtrDf.select(qtrDf.no,qtrDf.name).show()

# **Simplest select mixed parameter types**
#
# We can mix string names and attributes in select

qtrDf.select(qtrDf.no, "name").show()

# **What if we make mistake**
#
# We will get exception if we misspell column name

try:
    qtrDf.select("no", "badname").show()
except Exception as e:
    print("Got exception:", str(e))

# **Real expressions in select**
#
# We can use expressions instead on column names, let us make quarter no-s zero based

qtrDf.select(qtrDf.name, qtrDf.no-1).show()

# **Be aware of strings expressions**
#
# String concatenation is not that straightforward:

qtrDf.select(qtrDf.no, "Q"+qtrDf.no).show()

# **String concatenation**
#
# To concatenate strings we have to use functions (see details heeree)

from pyspark.sql import functions as f
qtrDf.select(qtrDf.no, f.concat(f.lit("Q"),qtrDf.no.cast("string"))).show()

# **Fix column name**
#
# In our last example we got weird column name - can fix it with alias (see details heeree)

from pyspark.sql import functions as f
qtrDf.select(qtrDf.no, f.concat(f.lit("Q"),qtrDf.no.cast("string")).alias("qname")).show()

# **Add columns with select**
#
# One can use select not only to reduce columns, but to add new columns

from pyspark.sql import functions as f
qtrDf.select("*", f.concat(f.lit("Q"),qtrDf.no.cast("string")).alias("qname")).show()

# **Change columns order**
#
# With select new dataframe will have columns exactly in the order we specified in select.
#
# For example, our dataframe has columns ordered like that: no, name, short
#
# We can reorder them like that: short, name, no

qtrDf.select("short","name","no").show()

# ## What do we need select for

# Typical use cases for using select():
#
# Case 1: We need to get small column subset of potentially wide dataframe. This is exactly why name "select" was chosen, also this is very similar to SQL select clause 
#
# Case 2: We need to reorder columns prior to e.g. union() transformation (see details heeree) 

# ## Try it yourself

# Task 1: Create dataframe with columns "no" and "short"

qtrDf.select(___).show()

# Task 2: Create dataframe with all columns from qtrDf and new zero-based number column named "zno"

qtrDf.select(___).show()

sp.stop()
