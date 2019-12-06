class RssUrls:
    def __init__(self):
        self.nyt = "https://rss.nytimes.com/services/xml/rss/nyt/World.xml"
        self.bbc = "http://feeds.bbci.co.uk/news/world/rss.xml"
        self.aljazeera = "https://www.aljazeera.com/xml/rss/all.xml"

    def to_list(self):
        keys = self.__dict__.keys()
        return [self.__dict__[key] for key in keys]

    def to_dict(self):
        return self.__dict__


class Tables:
    def __init__(self):
        self.raw = "article_list"
        self.analyzed = "article_profiles"


class DatabaseConfig:
    def __init__(self):
        self.host = "localhost"
        self.port = 27017
        self.database = "newsfetcher"
        self.tables = Tables()


class Config:
    def __init__(self):
        self.rss_urls = RssUrls()
        self.database = DatabaseConfig()
