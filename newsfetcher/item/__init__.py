def get_item(item, date_listed, site):
    return {"id": item.get("id"), "site": site, "date_listed": date_listed, "link": item.get("link"), "title": item.get("title")}
