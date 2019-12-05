import re
import json
import xml.etree.ElementTree as Etree


def change_id(item):
    item["_id"] = item.pop("id")
    return item


class Item:
    def __init__(self, site, raw_xml, timestamp):
        self.site = site
        self.timestamp = timestamp
        self.raw_xml = raw_xml

    def __repr__(self):
        max_char = 25
        return "<Site: {}; Timestamp fetched: {}, Raw xml: {}...".format(self.site, self.timestamp, self.raw_xml[:max_char])

    def to_json(self):
        return json.dumps(self.__dict__)


def get_raw(item):
    raw_bytes = Etree.tostring(item)
    return raw_bytes.decode("utf-8")


# def get_nyt_item(item, datetime_listed, version, site):
#     title = item.find("title").text
#     description = item.find("description").text
#     url = item.find("guid").text
#     raw_xml = get_raw(item)
#     return Item(site, datetime_listed, version, title, description, url, raw_xml)
#
#
# def get_bbc_item(item, datetime_listed, version, site):
#     title = item.find("title").text
#     description = item.find("description").text
#     url = item.find("guid").text
#     raw_xml = get_raw(item)
#     return Item(site, datetime_listed, version, title, description, url, raw_xml)
#
#
# def get_item_info(item, site, datetime_listed, version):
#     switcher = {
#         "nyt": get_nyt_item(item, datetime_listed, version, site),
#         "bbc": get_bbc_item(item, datetime_listed, version, site)
#     }
#     return switcher.get(site, None)
