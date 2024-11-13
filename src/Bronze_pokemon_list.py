# Databricks notebook source
df = spark.read.json("/Volumes/lab/pokemon/pokemon_raw/pokemons_list")
(df.distinct()
    .coalesce(1)
    .write
    .mode('overwrite')
    .saveAsTable("Bronze_pokemon_list"))

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC SELECT *
# MAGIC FROM bronze_pokemon_list
# MAGIC
