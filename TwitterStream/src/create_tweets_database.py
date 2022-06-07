from src.utils import TweetStreamer
from src.handlers import TweetHandler
import configparser
import tweepy
import time


def __main__():
    create_database(max_read_time = 122)


def create_database(max_read_time:int):
    """_summary_

    Args:
        max_read_time (int): maximum time to read tweets
    """

    tweet_streamer = TweetStreamer("TwitterStream/data/base_test.csv")
    tweet_streamer.start()

    time.sleep(max_read_time)
    tweet_streamer.stop()


if __name__ == '__main__':
    __main__()