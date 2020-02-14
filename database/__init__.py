import pg8000
from typing import *
from datetime import datetime
from classes import Topic, Category
from config import Table


def create_insert_query(table: Table) -> str:
    col_query = ", ".join(table.columns)
    values_query = ", ".join(["%s"] * len(table.columns))
    conflict_query = ", ".join(table.unique_cols)
    update_query = ", ".join([
        "{}=excluded.{}".format(col, col)
        for col in table.update_cols
    ])
    return (
        "INSERT INTO {} ({}) VALUES ({}) "
        "ON CONFLICT ({}) DO UPDATE SET {};"
    ).format(table.name, col_query, values_query, conflict_query, update_query)


class DatabaseClient:
    def __init__(self, host: str, database: str, user: str, password: str, port: str):
        self.host = host
        self.connection = pg8000.connect(user=user, password=password, host=host, port=port, database=database)
        self.cursor = self.connection.cursor()

    def insert_items(self, items: List[List], table: Table):
        query = create_insert_query(table)
        self.cursor.executemany(query, items)

    def get_latest(self) -> List[any]:
        query = "SELECT uid, site, hyperlink FROM articles t1 " \
                "LEFT JOIN article_topics t2 ON t1.uid = t2.article_id " \
                "WHERE t2.article_id IS NULL " \
                "ORDER BY date_listed DESC; "
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def get_topic_uids(self, topics: List[Topic], table: Table):
        query = "SELECT uid FROM {} WHERE topic_id=%s;".format(table.name)
        return [self.get_topic_uid(topic, query) for topic in topics]

    def get_topic_uid(self, topic: Topic, query: str):
        self.cursor.execute(query, (topic.topic_id, ))
        return self.cursor.fetchone()[0]

    def get_category_uids(self, categories: List[Category], table: Table):
        query = "SELECT uid FROM {} WHERE category_id=%s;".format(table.name)
        return [self.get_category_uid(category, query) for category in categories]

    def get_category_uid(self, category: Category, query: str):
        self.cursor.execute(query, (category.category_id, ))
        return self.cursor.fetchone()[0]
