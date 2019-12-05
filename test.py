from pymongo import MongoClient
import feedparser
from newsfetcher import conf
from newsfetcher.item import change_id


DatabaseClient(host, port, database)

client = MongoClient('localhost', 27017)
db = client.test_database
collection = db.raw_feeds

urls = conf.rss_urls.__dict__

key = "bbc"
feed = feedparser.parse(urls[key])
entries = [change_id(entry) for entry in feed.get("entries")]

collection.insert_many(entries[:3])

for entry in collection.find({}):
    print(entry)
