class RssUrls:
    def __init__(self):
        self.nyt = "https://rss.nytimes.com/services/xml/rss/nyt/World.xml"
        self.bbc = "http://feeds.bbci.co.uk/news/world/rss.xml"

    def to_list(self):
        keys = self.__dict__.keys()
        return [self.__dict__[key] for key in keys]


class Tables:
    def __init__(self):
        self.raw = "article_list"
        self.analyzed = ""


class DatabaseConfig:
    def __init__(self):
        self.host = "localhost"
        self.port = "27017"

class Config:
    def __init__(self):
        self.rss_urls = RssUrls()
        self.valid_sites = ["nyt", "bbc"]
        self.
