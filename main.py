import feedparser
from datetime import date
from newsfetcher.config import Config
from newsfetcher.database import DatabaseClient
from newsfetcher.item import get_item


def main():
    conf = Config()
    db = DatabaseClient(conf.database.host, conf.database.database, conf.database.user, conf.database.password)
    urls = conf.rss_urls.to_dict()

    for key in urls:
        today = date.today().strftime("%Y-%m-%d")
        try:
            print("\nChecking feed for site '{}', with url '{}'\n".format(key, urls[key]))
            feed = feedparser.parse(urls[key])
            entries = [get_item(entry, today, key) for entry in feed.get("entries")]
            db.insert_items(entries, conf.database.tables.raw)
        except:
            print("FAILED to get and store feed for site '{}', with url '{}'".format(key, urls[key]))


if __name__ == '__main__':
    main()
