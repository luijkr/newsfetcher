from newsfetcher import conf, NewsClient
from newsfetcher.database import DatabaseClient

db = DatabaseClient(conf.host, conf.keyspace)
nyt_news = NewsClient("nyt")
bbc_news = NewsClient("bbc")
nyt_items = nyt_news.call()
bbc_items = bbc_news.call()
db.insert_items(bbc_items, conf.tables.raw)
