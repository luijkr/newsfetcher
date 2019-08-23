class RssUrls:
    def __init__(self):
        self.nyt = "https://rss.nytimes.com/services/xml/rss/nyt/World.xml"


class Tables:
    def __init__(self):
        self.raw = "article_list"
        self.analyzed = ""

class Config:
    def __init__(self):
        self.rss_urls = RssUrls()
        self.valid_sites = ["nyt"]
        self.host = "127.0.0.1"
        self.keyspace = "test01"
        self.tables = Tables()
