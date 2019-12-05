import uuid
from pymongo import MongoClient

class DatabaseClient:
    def __init__(self, host, port, database, collection):
        self.host = host
        self.port = port
        self.client = MongoClient(self.host, port)
        self.db = self.client[database]

    def get_table(self, table):
        return self.client.execute(statement)

    def item_exists(self, article_id, table):
        query = "SELECT article_id FROM {} where article_id={}".format(table, article_id)
        statement = SimpleStatement(query, consistency_level=ConsistencyLevel.QUORUM)
        res = self.client.execute(statement)
        return len(list(res)) > 0

    def insert_item(self, item, table):
        article_id = uuid.uuid3(uuid.NAMESPACE_URL, item.url)
        query = "INSERT INTO {} (article_id, datetime_listed, source, title, description, url, raw_xml) VALUES (%s, %s, %s, %s, %s, %s, %s)".format(table)
        statement = SimpleStatement(query, consistency_level=ConsistencyLevel.QUORUM)
        if not self.item_exists(article_id, table):
            try:
                self.client.execute(statement, (article_id, item.datetime_listed, item.source, item.title, item.description, item.url, item.raw_xml))
            except Exception as e:
                print("Oh no!: {}".format(e))
        else:
            print("article already exists")

    def insert_items(self, items, table):
        print("Trying to insert {} items".format(len(items)))
        for item in items:
            self.insert_item(item, table)
