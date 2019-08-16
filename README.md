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
pip install -r requirements.txt
```

Run interactively

```
from newsfetcher import Client

my_client = Client()
my_client.call()
```
