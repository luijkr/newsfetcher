class Item:
    def __init__(self, title, description, url, raw_json="{}"):
        self.title = title
        self.description = description
        self.url = url
        self.raw_json = raw_json

    def __repr__(self):
        max_char = 30
        return "<Title (short): {}; URL (short): {}".format(self.title[:max_char], self.url[:max_char])


def get_nyt_item(item):
    title = item.find("title").text
    description = item.find("description").text
    url = item.find("guid").text
    return Item(title, description, url)


def get_item_info(item, site):
    switcher = {
        "nyt": get_nyt_item(item)
    }
    return switcher.get(site, None)
