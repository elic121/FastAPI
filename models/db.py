from pymongo import MongoClient
from pymongo.collection import Collection
from pymongo.database import Database

class MongoDB:
    def __init__(self, host: str = "localhost", port: int = 27017, db_name: str = "admin", collection_name: str = "fastAPI") -> None:
        self.client = MongoClient(host=host, port=port)
        self.db: Database = self.client[db_name]
        self.collection: Collection = self.db[collection_name]

    def check_collection_existence(self) -> None:
        if self.collection_name not in self.db.list_collection_names():
            raise Exception(f"Collection '{self.collection_name}' not found in database '{self.db.name}'")

    def insert_document(self, document: dict) -> None:
        result = self.collection.insert_one(document)
        print(f"Document inserted with id: {result.inserted_id}")

    def find_documents(self, filter: dict = None, projection: dict = None) -> list:
        documents = self.collection.find(filter, projection)
        return list(documents)

    def update_document(self, filter: dict, update: dict) -> None:
        result = self.collection.update_one(filter, {"$set": update})
        print(f"Modified {result.modified_count} document")

    def delete_document(self, filter: dict) -> None:
        result = self.collection.delete_one(filter)
        print(f"Deleted {result.deleted_count} document")

if __name__ == "__main__":
    db = MongoDB()
