import os
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()

dburl = os.getenv("URL")

print(dburl)
if not dburl:
    raise ValueError("no tienes url mongo")

#connect to db
client = MongoClient(dburl) 
db = client.get_database("speeches")
collection = db.xmas
#mongoimport --db speeches --collection xmas --jsonArray speeches_2014_2020

