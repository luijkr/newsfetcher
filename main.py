import time
import argparse
import feedparser

from datetime import date
from config import Config
from database import DatabaseClient
from newsfetcher.item import fetch_item
from textrazorclient import TextrazorClient


def time_to_string(obj):
    """ Converts datetime.date object to string
        :param obj: datetime.date object
        :return:    string format of datetime.date
    """
    return obj.strftime("%Y-%m-%d")


def fetch(conf, db, today):
    """ Fetches news articles from various RSS feeds and stores it in database.
        :param conf:    Configuration object
        :param db:      Database client
        :param today:   String of today
        :return:        Nothing, only prints progress or failure
    """
    urls = conf.rss_urls.to_dict()
    for key in urls:
        try:
            print("\nChecking feed for site '{}', with url '{}'\n".format(key, urls[key]))
            feed = feedparser.parse(urls[key])
            entries = [fetch_item(entry, today, key) for entry in feed.get("entries")]
            db.insert_fetched_items(entries, conf.database.tables.raw)
        except:
            print("FAILED to get and store feed for site '{}', with url '{}'".format(key, urls[key]))


def analyze(conf, db, day):
    """ Fetches article list from database, analyzes it using Textrazor, and stores these in separate table.
        :param conf:  Configuration object
        :param db:    Database client
        :param day:   String of today
        :return:      Nothing, only prints progress or failure
    """
    client = TextrazorClient()
    latest_items = db.get_latest_fetched(table=conf.database.tables.raw, day=day)
    max_tries = 2
    for article_id, url in latest_items:
        print("\nAnalyzing article id '{}'".format(article_id))
        for _ in range(max_tries):
            try:
                results = client.analyze(url)
                item = {
                    "article_id": article_id,
                    "date_analyzed": day,
                    "article_profile": results.to_json()
                }
                db.insert_analyzed_item(item, conf.database.tables.analyzed)
                print("\nInserted article id '{}'".format(article_id))
                time.sleep(10.0)
            except Exception as e:
                print(
                    "FAILED to get and/or store anaylzed article identifier '{}'\nWaiting 1 minute before retrying.".format(
                        article_id))
                time.sleep(60.0)
            else:
                break
    db.connection.commit()


def main(mode):
    """ Main program. Either fetches new articles from RSS feeds or analyzes them using Textrazor.
        :param mode:    One of 'fetch' or 'analyze'.
        :return:        Nothing, only prints messages regarding success or failure.
    """
    # time-related
    now = date.today()
    today = time_to_string(now)

    # configuration, database connection
    conf = Config()
    db = DatabaseClient(conf.database.host, conf.database.database, conf.database.user, conf.database.password)
    if mode == "fetch":
        fetch(conf, db, today)
    else:
        analyze(conf, db, today)


if __name__ == '__main__':
    # parse command-line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('--mode', help="Mode of program. On of 'fetch' or 'analyze'.", required=True, choices=["fetch", "analyze"])
    args = parser.parse_args()

    # run main
    main(mode=args.mode)
