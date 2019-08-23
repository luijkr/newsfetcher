import requests
import xml.etree.ElementTree as Etree
from datetime import datetime
from newsfetcher.item import Item, get_item_info
from newsfetcher.config import Config

conf = Config()


class NewsClient(object):
    def call(self, site):
        if site not in conf.valid_sites:
            raise ValueError("Client: 'site' must be one of %r." % ", ".join(conf.valid_sites))

        url = conf.rss_urls.__getattribute__(site)
        now = datetime.utcnow()
        datetime_listed = now.strftime("%Y-%m-%d %H:%M:%S")
        version = now.strftime("%Y-%m-%d")
        response = requests.get(url)
        if response.ok:
            content = response.content
            tree = Etree.ElementTree(Etree.fromstring(content))
            items = tree.find("channel").findall("item")
            return [get_item_info(item, site, datetime_listed, version) for item in items]
        else:
            return [Item("", "", "")]
