CREATE USER 'newsfetcher_user'@'localhost' IDENTIFIED BY 'fetchnews!';
GRANT ALL PRIVILEGES ON *.* TO 'newsfetcher_user'@'localhost';

CREATE DATABASE newsfetcher;
USE newsfetcher;

CREATE TABLE article_list(
    id VARCHAR(500) NOT NULL PRIMARY KEY,
    site VARCHAR(20) NOT NULL,
    date_listed DATE NOT NULL,
    hyperlink VARCHAR(800) NOT NULL,
    title TEXT NOT NULL
);

CREATE TABLE article_profiles(
    id VARCHAR(500) NOT NULL PRIMARY KEY,
    site VARCHAR(20) NOT NULL,
    date_analyzed DATE NOT NULL,
    hyperlink VARCHAR(800) NOT NULL
);
