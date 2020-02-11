import feedparser
from typing import *
from database import DatabaseClient
from config import Config


def fetch_item(item: dict, date_listed: str, site: str) -> List[str]:
    return [site, item.get("link"), date_listed]


def fetch(conf: Config, db: DatabaseClient, ts: str):
    """
    Fetches news articles from various RSS feeds and stores it in database.
    :param conf:  Configuration object
    :param db:    Database client
    :param ts:    String of today
    :return:
    """
    urls = conf.rss_urls.to_dict()
    for site in urls:
        try:
            print("\nChecking feed for site '{}', with url '{}'\n".format(site, urls[site]))
            feed = feedparser.parse(urls[site])
            entries = [fetch_item(entry, ts, site) for entry in feed.get("entries")]
            db.insert_items(entries, conf.database.tables.article_list)
        except:
            print("FAILED to get and store feed for site '{}', with url '{}'".format(site, urls[site]))
