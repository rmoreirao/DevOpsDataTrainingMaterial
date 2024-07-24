# addcol.py

# The file represents a library function that might be installed on an Azure Databricks cluster. 
# This simple function adds a new column, populated by a literal, to an Apache Spark DataFrame.

import pyspark.sql.functions as F

def with_status(df):
  return df.withColumn("status", F.lit("checked"))