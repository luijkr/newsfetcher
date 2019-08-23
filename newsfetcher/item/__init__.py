import re
import xml.etree.ElementTree as Etree
from datetime import datetime


class Item:
    def __init__(self, title="", description="", url="", raw_xml=""):
        self.title = title
        self.description = description
        self.url = url
        self.raw_xml = raw_xml
        self.datetime_listed = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")

    def __repr__(self):
        max_char = 25
        return "<Title (short): {}...; URL (short): {}...".format(self.title[:max_char], self.url[:max_char])


def get_raw(item):
    raw_bytes = Etree.tostring(item)
    raw_string = raw_bytes.decode("utf-8")
    return re.sub("\s+", "", raw_string)


def get_nyt_item(item):
    title = item.find("title").text
    description = item.find("description").text
    url = item.find("guid").text
    raw_xml = get_raw(item)
    return Item(title, description, url, raw_xml)


def get_item_info(item, site):
    switcher = {
        "nyt": get_nyt_item(item)
    }
    return switcher.get(site, None)
