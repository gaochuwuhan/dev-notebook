from pymongo import ReturnDocument
from pymongo import MongoClient

MONGODB_HOST="127.0.0.1"
MONGODB_DB = "test_fastapi"

client = MongoClient(MONGODB_HOST)
db=client(MONGODB_DB)

