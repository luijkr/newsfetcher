import argparse
from argparse import Namespace

from analyze import *
from fetch import fetch


def main(mode: str):
    """
    Main program. Either fetches new articles from RSS feeds or analyzes them using Textrazor.
    :param mode:    One of 'fetch' or 'analyze'.
    :return:        Nothing, only prints messages regarding success or failure.
    """
    # time-related
    now = datetime.now()

    # configuration, database connection
    conf = Config()
    db = DatabaseClient(conf.database.host, conf.database.database, conf.database.user,
                        conf.database.password, conf.database.port)

    # fetch / analyze articles
    if mode == "fetch":
        fetch(conf, db, now.isoformat())
    elif mode == "analyze":
        analyze(conf, db, now)
    else:
        raise ValueError("--mode must be one of 'fetch', 'analyze'.")

    # commit any changes to database
    db.connection.commit()


def parse_args() -> Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument('--mode', help="Mode of program. On of 'fetch' or 'analyze'.",
                        required=True, choices=["fetch", "analyze"])
    return parser.parse_args()


if __name__ == '__main__':
    args = parse_args()
    main(mode=args.mode)
