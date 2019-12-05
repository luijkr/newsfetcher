from pymongo import MongoClient


class DatabaseClient:
    def __init__(self, host, port, database):
        self.host = host
        self.port = port
        self.client = MongoClient(self.host, port)
        self.database = self.client[database]

    def set_collection(self, collection):
        self.collection = self.database[collection]

    def item_exists(self, item):
        return self.collection.count_documents({"_id": item._id}) > 0

    def insert_items(self, items):
        # private function to insert article into self.collection
        items = [item for item in items if not self.item_exists(item)]
        n_items = len(items)
        if n_items > 0:
            self.collection.insert_many(items)
            print("Inserted {} items in collection.\n".format(n_items))
        else:
            print("All items already in database.\n")
