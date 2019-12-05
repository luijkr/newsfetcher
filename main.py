import feedparser
from newsfetcher.config import Config
from newsfetcher.database import DatabaseClient
from newsfetcher.item import change_id

conf = Config()
db = DatabaseClient(conf.database.host, conf.database.port, conf.database.database)
db.set_collection(conf.database.tables.raw)
urls = conf.rss_urls.to_dict()

if __name__ == "__main__":
    for key in urls:
        try:
            print("Checking feed for site '{}', with url '{}'".format(key, urls[key]))
            feed = feedparser.parse(urls[key])
            entries = [change_id(entry) for entry in feed.get("entries")]
            db.insert_items(entries)
        except:
            print("FAILED to get and store feed for site '{}', with url '{}'".format(key, urls[key]))
