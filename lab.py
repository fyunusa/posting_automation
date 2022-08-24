import datetime   # This will be needed later
import os
from pymongo import MongoClient

# Load config from a .env file:
MONGODB_URI = os.environ['MONGODB_URI']
# Connect to your MongoDB cluster:
client = MongoClient(MONGODB_URI)
# List all the databases in the cluster:
for db_info in client.list_database_names():
   print(db_info)