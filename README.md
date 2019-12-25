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
pip install ...
```

or

```
pip install -r requirements.txt
```

For install and set up MariaDB and permissions, see
```
https://pimylifeup.com/raspberry-pi-mysql/
```

Set up database.
```
CREATE DATABASE newsfetcher;
USE newsfetcher;
```

Create table for raw article list.
```
CREATE TABLE article_list (
    
)
```

Run program
```
bash run.sh
```
