def handler(event, context):
    from newsfetcher import conf, NewsClient
    from newsfetcher.database import DatabaseClient

    db = DatabaseClient(conf.host, conf.keyspace)
    news = NewsClient()
    for site in conf.valid_sites:
        print("Fetching articles for: {}".format(site))
        items = news.call(site)
        for item in items[:3]:
            print(item) # db.insert_items(items, conf.tables.raw)
