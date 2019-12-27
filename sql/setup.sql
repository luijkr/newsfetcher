CREATE USER 'newsfetcher_user'@'localhost' IDENTIFIED BY 'fetchnews!';
GRANT ALL PRIVILEGES ON *.* TO 'newsfetcher_user'@'localhost';

CREATE DATABASE newsfetcher;
USE newsfetcher;

CREATE TABLE article_list(
    article_id VARCHAR(500) NOT NULL,
    site VARCHAR(20) NOT NULL,
    date_listed DATE NOT NULL,
    hyperlink VARCHAR(800) NOT NULL,
    title TEXT NOT NULL,
    PRIMARY KEY (article_id)
);

CREATE TABLE article_profiles(
    profile_id INT auto_increment,
    article_id VARCHAR(500) NOT NULL,
    date_analyzed DATE NOT NULL,
    article_profile LONGTEXT NOT NULL,
    PRIMARY KEY (profile_id),
    FOREIGN KEY (article_id) REFERENCES article_list(article_id)
);
