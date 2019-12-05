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
pip install feedparser
pip install requests
pip install pymongo
```

or

```
pip install -r requirements.txt
```

Install and set up MongoDB and permissions
```
wget https://fastdl.mongodb.org/osx/mongodb-macos-x86_64-4.2.1.tgz
tar -zxvf mongodb-macos-x86_64-4.2.1.tgz
mv mongodb-*-4.2.1 mongodb
mkdir -p /data/db
sudo chown -R `id -un` /data/db
```

Fire up MongoDB
```
~/mongodb/bin/mongod
```

If needed, MongoDB shell
```
~/mongodb/bin/mongo
```

Run program
```
python main.py
```
