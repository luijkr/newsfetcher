# News fetcher

Client to fetch news from different news sources and analyze them using the TextRazor API.

Resources
- RSS feeds
    - [New York Times world news](https://rss.nytimes.com/services/xml/rss/nyt/World.xml)
- The official documentation [TextRazor](https://www.textrazor.com/docs/python)

### Prerequisites

Create virtual environment

```
python3 -m venv venv
source venv/bin/activate
```

Install dependencies

```
pip install feedparser, requests, pymongo
pip freeze > requirements.txt
```

or

```
pip install -r requirements.txt
```

Install and set up MongoDB and permissions
```
tar -zxvf mongodb-*4.2.1.tgz
mv mongodb-*-4.2.1 mongodb
mkdir -p /data/db
sudo chown -R `id -un` /data/db
```

Fire up MongoDB
```
~/mongodb/bin/mongod
~/mongodb/bin/mongo
```

Create database with tables
```
use newsfetcher
db.createCollection("raw_feeds")
db.createCollection("article_??")
```