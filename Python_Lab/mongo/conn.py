from pymongo import ReturnDocument
from pymongo import MongoClient

MONGODB_HOST="192.168.88.164"
MONGODB_DB = "test_fastapi"

client = MongoClient(MONGODB_HOST)
db=client(MONGODB_DB)
class MongodbBase(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    """
    base for mongodb base on pymongo
    """

    def __init__(
        self, collection: str, model: Type[ModelType], search_fields=[]
    ) -> None:
        client = MongoClient(settings.MONGODB_URI)
        db = client[settings.MONGODB_DB] #test_api表
        self.collection = db[collection]
        self.counters = db["counters"]
        self.sequenceName = self.__class__.__name__
        self.search_fields = search_fields
        self.model = model
