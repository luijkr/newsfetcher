from newsfetcher import conf, NewsClient
news = NewsClient()

for site in conf.valid_sites:
    print("Fetching articles for: {}".format(site))
    news_response = news.call(site)
    filename = "{}/{}_{}".format(conf.data_dir, news_response.site, news_response.timestamp)
    with open(filename, "w") as file:
        for item in news_response.items:
            file.write(item.raw_xml + "\n")
