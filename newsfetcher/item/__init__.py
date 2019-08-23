import re
import xml.etree.ElementTree as Etree


class Item:
    def __init__(self, source, datetime_listed, version, title="", description="", url="", raw_xml="", analyzed=False):
        self.source = source
        self.title = title
        self.description = description
        self.url = url
        self.raw_xml = raw_xml
        self.datetime_listed = datetime_listed
        self.analyzed = analyzed
        self.version = version

    def __repr__(self):
        max_char = 25
        return "<Title (short): {}...; URL (short): {}...".format(self.title[:max_char], self.url[:max_char])


def get_raw(item):
    raw_bytes = Etree.tostring(item)
    raw_string = raw_bytes.decode("utf-8")
    return re.sub("\s+", "", raw_string)


def get_nyt_item(item, datetime_listed, version, site):
    title = item.find("title").text
    description = item.find("description").text
    url = item.find("guid").text
    raw_xml = get_raw(item)
    return Item(site, datetime_listed, version, title, description, url, raw_xml)


def get_bbc_item(item, datetime_listed, version, site):
    title = item.find("title").text
    description = item.find("description").text
    url = item.find("guid").text
    raw_xml = get_raw(item)
    return Item(site, datetime_listed, version, title, description, url, raw_xml)


def get_item_info(item, site, datetime_listed, version):
    switcher = {
        "nyt": get_nyt_item(item, datetime_listed, version, site),
        "bbc": get_bbc_item(item, datetime_listed, version, site)
    }
    return switcher.get(site, None)
