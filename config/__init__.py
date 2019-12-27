class RssUrls:
    def __init__(self):
        self.nyt = "https://rss.nytimes.com/services/xml/rss/nyt/World.xml"
        self.cnbc = "https://www.cnbc.com/id/15837362/device/rss/rss.html"
        self.huff = "https://www.huffpost.com/section/front-page/feed"
        self.fox = "http://feeds.foxnews.com/foxnews/world"
        self.bbc = "http://feeds.bbci.co.uk/news/world/rss.xml"
        self.aljaz = "https://www.aljazeera.com/xml/rss/all.xml"
        self.rt = "https://www.rt.com/rss/news/"

    def to_list(self):
        keys = self.__dict__.keys()
        return [self.__dict__[key] for key in keys]

    def to_dict(self):
        return self.__dict__


class Table:
    def __init__(self, name, columns):
        self.name = name
        self.columns = columns


class Tables:
    def __init__(self):
        self.raw = Table(name="article_list", columns=["article_id", "site", "date_listed", "hyperlink", "title"])
        self.analyzed = Table(name="article_profiles", columns=["article_id", "date_analyzed", "article_profile"])


class DatabaseConfig:
    def __init__(self):
        self.host = "localhost"
        self.database = "newsfetcher"
        self.tables = Tables()
        self.user = "newsfetcher_user"
        self.password = "fetchnews!"


class Config:
    def __init__(self):
        self.rss_urls = RssUrls()
        self.database = DatabaseConfig()
