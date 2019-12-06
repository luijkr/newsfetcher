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
        n_total = len(items)
        items_filtered = [item for item in items if not self.item_exists(item)]
        n_filtered = len(items_filtered)
        if n_filtered > 0:
            self.collection.insert_many(items_filtered)
            print("Inserted {} out of {} items in collection.\n".format(n_filtered, n_total))
        else:
            print("All {} items already in database.\n".format(n_total))
