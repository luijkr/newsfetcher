def change_id(item):
    item["_id"] = item.pop("id")
    return item
