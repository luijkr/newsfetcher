import feedparser
from datetime import datetime
from newsfetcher.config import Config
from newsfetcher.database import DatabaseClient
from newsfetcher.item import get_item

conf = Config()
db = DatabaseClient(conf.database.host, conf.database.port, conf.database.database)
db.set_collection(conf.database.tables.raw)
urls = conf.rss_urls.to_dict()

if __name__ == "__main__":
    for key in urls:
        try:
            print("Checking feed for site '{}', with url '{}'".format(key, urls[key]))
            now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            feed = feedparser.parse(urls[key])
            entries = [get_item(entry, now) for entry in feed.get("entries")]
            db.insert_items(entries)
        except:
            print("FAILED to get and store feed for site '{}', with url '{}'".format(key, urls[key]))
