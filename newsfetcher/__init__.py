import requests
import xml.etree.ElementTree as Etree
from datetime import datetime
from newsfetcher.item import Item, get_raw
from newsfetcher.config import Config

conf = Config()


class NewsResponse:
    def __init__(self, site, timestamp, items):
        self.site = site
        self.timestamp = timestamp
        self.items = items


class NewsClient(object):
    def call(self, site):
        if site not in conf.valid_sites:
            raise ValueError("Client: 'site' must be one of %r." % ", ".join(conf.valid_sites))

        url = conf.rss_urls.__getattribute__(site)
        now = datetime.utcnow()
        timestamp = now.strftime("%Y%m%d_%H%M%S")
        response = requests.get(url)
        if response.ok:
            content = response.content
            tree = Etree.ElementTree(Etree.fromstring(content))
            return NewsResponse(site, timestamp, [Item(site, get_raw(item), timestamp) for item in tree.find("channel").findall("item")])
        else:
            return None
