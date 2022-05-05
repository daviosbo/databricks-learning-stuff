# Databricks notebook source
dbutils.fs.ls("/mnt/da01/bronzeroot01/vet_data")

# COMMAND ----------

df = spark.read.csv("/mnt/da01/bronzeroot01/vet_data/TVA_USI_1617_INTELLIFY_FINAL.csv", header=True)
display(df)

# COMMAND ----------

df.columns

# COMMAND ----------

dbutils.fs.ls("/mnt/da01/bronzeroot01/a_and_t_data/")
