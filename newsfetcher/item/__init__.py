import xml.etree.ElementTree as Etree


class Item:
    def __init__(self, title="", description="", url="", raw_xml=""):
        self.title = title
        self.description = description
        self.url = url
        self.raw_xml = raw_xml

    def __repr__(self):
        max_char = 30
        return "<Title (short): {}; URL (short): {}".format(self.title[:max_char], self.url[:max_char])


def get_raw(item):
    raw_string = Etree.tostring(item)
    return raw_string.decode("utf-8")


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
