def get_item(item, timestamp):
    return {"_id": item.get("id"), "timestamp": timestamp, "link": item.get("link"), "title": item.get("title")}
