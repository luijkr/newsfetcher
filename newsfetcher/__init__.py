from newsfetcher.item import Item, get_item_info
from newsfetcher.config import Config

import requests
import xml.etree.ElementTree as Etree


class Client:
    def __init__(self, site):
        conf = Config()
        if site not in conf.valid_sites:
            raise ValueError("Client: 'site' must be one of %r." % ", ".join(conf.valid_sites))

        self.site = site
        self.url = conf.rss_urls.__getattribute__(site)

    def call(self):
        response = requests.get(self.url)
        if response.ok:
            content = response.content
            tree = Etree.ElementTree(Etree.fromstring(content))
            items = tree.find("channel").findall("item")
            return [get_item_info(item, self.site) for item in items]
        else:
            return [Item()]
