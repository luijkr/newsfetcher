import feedparser
from datetime import datetime
from newsfetcher.config import Config
from newsfetcher.database import DatabaseClient
from newsfetcher.item import get_item


def main():
    conf = Config()
    db = DatabaseClient(conf.database.host, conf.database.port, conf.database.database)
    db.set_collection(conf.database.tables.raw)
    urls = conf.rss_urls.to_dict()

    for key in urls:
        now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        try:
            print("\nChecking feed for site '{}', with url '{}'\n".format(key, urls[key]))
            feed = feedparser.parse(urls[key])
            entries = [get_item(entry, now) for entry in feed.get("entries")]
            db.insert_items(entries)
        except:
            print("FAILED to get and store feed for site '{}', with url '{}'".format(key, urls[key]))


if __name__ == '__main__':
    main()
