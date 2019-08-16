class RssUrls:
    def __init__(self):
        self.nyt = "https://rss.nytimes.com/services/xml/rss/nyt/World.xml"


class Config:
    def __init__(self):
        self.rss_urls = RssUrls()
        self.valid_sites = ["nyt"]
