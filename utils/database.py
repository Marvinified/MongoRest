import os
import pymongo

client = pymongo.MongoClient(os.environ["MONGO_URL"])
db = client["mongorest"]

