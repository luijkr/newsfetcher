from cassandra import ConsistencyLevel
from cassandra.cluster import Cluster, NoHostAvailable
from cassandra.query import SimpleStatement


class DatabaseClient:
    def __init__(self, host, keyspace, table):
        self.host = host
        self.keyspace = keyspace
        self.table = table
        try:
            self.client = Cluster([self.host]).connect(self.keyspace)
        except NoHostAvailable as e:
            print(e)
            self.client = Cluster()

    # def insert_item(self, item):
    #     query = SimpleStatement(
    #         "INSERT INTO users (id, title, description, url, raw_xml, datetime_listed) VALUES (%s, %s, %s, %s, %s, %s)",
    #         consistency_level=ConsistencyLevel.QUORUM)
    #     try:
    #         self.client.execute(query, (id, item.title, item.description, item.url, item.raw_xml, item.datetime_listed))
    #     except:
    #         print("Oh no!")
    #
    # def insert_items(self, items):
    #     for item in items:
    #         self.insert_item(item)
    #     print("Inserted {} items".format(len(items)))

