import os
from typing import *


class RssUrls:
    def __init__(self):
        self.nyt = "https://rss.nytimes.com/services/xml/rss/nyt/World.xml"
        self.cnbc = "https://www.cnbc.com/id/15837362/device/rss/rss.html"
        self.huff = "https://www.huffpost.com/section/front-page/feed"
        self.fox = "http://feeds.foxnews.com/foxnews/world"
        self.bbc = "http://feeds.bbci.co.uk/news/world/rss.xml"
        self.aljaz = "https://www.aljazeera.com/xml/rss/all.xml"

    def to_list(self):
        keys = self.__dict__.keys()
        return [self.__dict__[key] for key in keys]

    def to_dict(self):
        return self.__dict__


class Table:
    def __init__(self, name: str, columns: List[str], unique_cols: List[str], update_cols: List[str]):
        self.name = name
        self.columns = columns
        self.unique_cols = unique_cols
        self.update_cols = update_cols


class Tables:
    def __init__(self):
        self.article_list = Table(
            name="articles",
            columns=["site", "hyperlink", "date_listed"],
            unique_cols=["hyperlink"],
            update_cols=["date_listed"]
        )
        self.categories = Table(
            name="categories",
            columns=["category_id", "label"],
            unique_cols=["category_id"],
            update_cols=["label"]
        )
        self.topics = Table(
            name="topics",
            columns=["topic_id", "wikilink", "wikidata_id", "lastseen"],
            unique_cols=["topic_id"],
            update_cols=["wikilink", "wikidata_id", "lastseen"]
        )
        self.article_categories = Table(
            name="article_categories",
            columns=["article_id", "category_id", "score"],
            unique_cols=["article_id", "category_id"],
            update_cols=["score"]
        )
        self.article_topics = Table(
            name="article_topics",
            columns=["article_id", "topic_id", "score"],
            unique_cols=["article_id", "topic_id"],
            update_cols=["score"]
        )


class DatabaseConfig:
    def __init__(self):
        self.host = os.environ.get("HOST")
        self.port = int(os.environ.get("PORT"))
        self.database = os.environ.get("DATABASE")
        self.tables = Tables()
        self.user = os.environ.get("POSTGRES_USER")
        self.password = os.environ.get("POSTGRES_PASSWORD")


class ContentAnalyzer:
    def __init__(self):
        self.endpoint = os.environ.get("LAMBDA_ENDPOINT")
        self.api_key = os.environ.get("API_KEY")


class Config:
    def __init__(self):
        self.rss_urls = RssUrls()
        self.database = DatabaseConfig()
        self.newsanalyzer = ContentAnalyzer()
