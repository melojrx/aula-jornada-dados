# Databricks notebook source
import requests 
import datetime
import json

url = 'https://pokeapi.co/api/v2/pokemon?limit=2000'

response = requests.get(url)
data = response.json()
data_save = data['results']

now = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
path = f"/Volumes/lab/pokemon/pokemon_raw/pokemons_list/{now}.json "


with open(path, 'w') as open_file:
  json.dump(data_save, open_file)


# COMMAND ----------

dbutils.fs.ls("/Volumes/lab/pokemon/pokemon_raw/pokemons_list")
