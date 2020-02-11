import time
import json
from datetime import datetime
from typing import *

import requests

from classes import Topic, Category
from config import Config
from database import DatabaseClient


def analyze_url(url: str, conf: Config) -> Tuple[List[Topic], List[Category]]:
    headers = {
        "api-key": conf.newsanalyzer.api_key,
        "url": url
    }
    r = requests.post(conf.newsanalyzer.endpoint, headers=headers)
    response = json.loads(r.text.encode('utf8'))["response"]

    topics = [
        Topic(topic_id=topic.get("label"), wikilink=topic.get("wikiLink"), score=topic.get("score"), wikidata_id=topic.get("wikidataId"))
        for topic in response.get("topics")
    ]
    categories = [
        Category(category_id=category.get("categoryId"), label=category.get("label"), score=category.get("score"))
        for category in response.get("categories")
    ]

    return topics, categories


def get_article_categories(article_id, categories, conf, db):
    category_uids = db.get_category_uids(categories, conf.database.tables.categories)
    zipped = zip(category_uids, categories)
    article_categories = [
        [article_id, z[0], z[1].score]
        for z in zipped
    ]
    return article_categories


def get_article_topics(article_id, conf, db, topics):
    topic_uids = db.get_topic_uids(topics, conf.database.tables.topics)
    zipped = zip(topic_uids, topics)
    article_topics = [
        [article_id, z[0], z[1].score]
        for z in zipped
    ]
    return article_topics


def analyze(conf: Config, db: DatabaseClient, ts: datetime):
    """
    Fetches article list from database, analyzes it using Textrazor, and stores these in separate table.
    :param conf:  Configuration object
    :param db:    Database client
    :param ts:    Datetime timestamp with time zone
    :return:      Nothing, only prints progress or failure
    """
    timestamp = ts.isoformat()
    latest_items = db.get_latest(table=conf.database.tables.article_list, ts=ts)

    for article_id, site, url in latest_items[20:30]:
        print("\nAnalyzing article from site '{}' at URL: {}".format(site, url))

        # analyze article
        topics, categories = analyze_url(url, conf)

        # insert topics
        topics_values = [
            [topic.topic_id, topic.wikilink, topic.wikidata_id, timestamp]
            for topic in topics
        ]
        db.insert_items(topics_values, conf.database.tables.topics)

        # commit topics to database
        db.connection.commit()

        # insert article-topics
        article_topics = get_article_topics(article_id, conf, db, topics)
        db.insert_items(article_topics, conf.database.tables.article_topics)

        # insert article-categories
        article_categories = get_article_categories(article_id, categories, conf, db)
        db.insert_items(article_categories, conf.database.tables.article_categories)

        # commit article to database
        db.connection.commit()

        # pause
        time.sleep(5)
