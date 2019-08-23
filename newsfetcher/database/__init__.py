import uuid
from cassandra import ConsistencyLevel
from cassandra.cluster import Cluster, NoHostAvailable
from cassandra.query import SimpleStatement


class DatabaseClient:
    def __init__(self, host, keyspace):
        self.host = host
        self.keyspace = keyspace
        try:
            self.client = Cluster([self.host]).connect(self.keyspace)
        except NoHostAvailable as e:
            print(e)
            self.client = Cluster()

    def get_from_table(self, table):
        query = "SELECT * FROM {}".format(table)
        statement = SimpleStatement(query, consistency_level=ConsistencyLevel.QUORUM)
        return self.client.execute(statement)

    def insert_item(self, item, table):
        article_id = uuid.uuid3(uuid.NAMESPACE_URL, item.url)
        query = "INSERT INTO {} (article_id, datetime_listed, source, title, description, url, raw_xml) VALUES (%s, %s, %s, %s, %s, %s, %s)".format(table)
        statement = SimpleStatement(query, consistency_level=ConsistencyLevel.QUORUM)
        try:
            self.client.execute(statement, (article_id, item.datetime_listed, item.source, item.title, item.description, item.url, item.raw_xml))
        except Exception as e:
            print("Oh no!: {}".format(e))

    def insert_items(self, items, table):
        for item in items:
            self.insert_item(item, table)
        print("Inserted {} items".format(len(items)))
