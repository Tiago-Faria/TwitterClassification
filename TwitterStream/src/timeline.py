from src.utils import get_home_timeline, get_recent_timeline
import configparser
import tweepy
import time

def print_tweets(response):
    for twitte in reversed(response.data):
        print(twitte.id)
        print(twitte.text)
        print(' --- ')


def __main__():
    response = get_home_timeline()
    newest_id = response.meta['newest_id']
    print_tweets(response)

    while (True):
        response = get_recent_timeline(since_id = newest_id)

        if(response.data != None):
            newest_id = response.meta['newest_id']
            print_tweets(response)

        time.sleep(10)

if __name__ == '__main__':
    __main__()