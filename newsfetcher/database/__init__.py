import mysql.connector


class DatabaseClient:
    def __init__(self, host, database, user, password):
        self.host = host
        self.connection = mysql.connector.connect(user=user, password=password, host=host, database=database)
        self.cursor = self.connection.cursor()

    def test_connection(self):
        return self.connection.is_connected()

    def insert_item(self, item, table):
        col_query = ", ".join(table.columns)
        col_holders = ", ".join(["%s"] * len(table.columns))
        values = (item["id"], item["site"], item["date_listed"], item["link"], item["title"])
        sql_query = "INSERT INTO {} ({}) VALUES ({})".format(table.name, col_query, col_holders)
        self.cursor.execute(sql_query, values)

    def insert_items(self, items, table):
        n_total = len(items)
        items_entered = 0
        for item in items:
            try:
                self.insert_item(item, table)
                items_entered += 1
            except:
                pass

        self.connection.commit()
        print("Inserted {} out of {} items in collection.\n".format(items_entered, n_total))
