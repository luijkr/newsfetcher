import json
from config import Config, Tables
from database import DatabaseClient

table = Tables().categories
conf = Config()
db = DatabaseClient(conf.database.host, conf.database.database, conf.database.user,
                    conf.database.password, conf.database.port)


def extract_category(obj):
    """
    Extract all IAB category data.
    :param obj:     dict of nested dicts
    :param n_tiers: number of IAB tiers
    :return:        list of values
    """
    arr = []

    def create_label(r):
        label = ">".join(r[1:])
        return [r[0], label]

    def extract(d):
        if isinstance(d, dict):
            for k, v in d.items():
                arr.append(k)
                extract(v)
        else:
            arr.append(d)

        return create_label(arr)

    return extract(obj)


with open("iab-mapping.json", "r") as json_file:
    data = json.load(json_file)
    categories = [extract_category(obj) for obj in data]

    col_query = ", ".join(table.columns)
    values_query = ", ".join(["%s"] * len(table.columns))
    query = "INSERT INTO {} ({}) VALUES ({});".format(table.name, col_query, values_query)

    db.cursor.executemany(query, categories)
    db.connection.commit()
