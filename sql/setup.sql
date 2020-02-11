--Locally: run script from within container
--docker run --name my-postgres -e POSTGRES_USER=myuser -e POSTGRES_PASSWORD=mypassword -d -p 5432:5432 postgres
--docker exec -it my-postgres psql -U myuser

CREATE DATABASE newsfetcher;
\c newsfetcher;

--article list
CREATE TABLE articles(
    uid serial PRIMARY KEY,
    site text NOT NULL,
    hyperlink text NOT NULL,
    date_listed timestamp with time zone NOT NULL,
    UNIQUE (hyperlink)
);

--categories
CREATE TABLE categories(
    uid serial PRIMARY KEY,
    category_id text NOT NULL,
    label text NOT NULL,
    UNIQUE (category_id)
);

--topics
CREATE TABLE topics(
    uid serial PRIMARY KEY,
    topic_id text NOT NULL,
    wikilink text,
    wikidata_id text,
    lastseen timestamp with time zone NOT NULL,
    UNIQUE (topic_id)
);

--article_categories
CREATE TABLE article_categories(
    article_id integer,
    category_id integer,
    score double precision,
    UNIQUE (article_id, category_id),
    CONSTRAINT article_categories_article_id_fkey FOREIGN KEY (article_id) REFERENCES articles (uid),
    CONSTRAINT article_categories_category_id_fkey FOREIGN KEY (category_id) REFERENCES categories (uid)
);

--article_topics
CREATE TABLE article_topics(
    article_id integer,
    topic_id integer,
    score double precision,
    UNIQUE (article_id, topic_id),
    CONSTRAINT article_topics_article_id_fkey FOREIGN KEY (article_id) REFERENCES articles (uid),
    CONSTRAINT article_topics_topic_id_fkey FOREIGN KEY (topic_id) REFERENCES topics (uid)
);
