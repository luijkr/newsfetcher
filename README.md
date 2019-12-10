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
brew tap mongodb/brew
brew install mongodb-community@4.2
```

Run program
```
bash run.sh
```
