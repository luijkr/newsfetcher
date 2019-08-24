from newsfetcher import conf, NewsClient
from newsfetcher.database import DatabaseClient

db = DatabaseClient(conf.host, conf.keyspace)
news = NewsClient()
for site in conf.valid_sites:
    items = news.call(site)
    db.insert_items(items, conf.tables.raw)
