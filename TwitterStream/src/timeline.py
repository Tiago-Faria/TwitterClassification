#from utils import get_home_timeline, get_recent_timeline
import configparser
import tweepy
import time

config = configparser.ConfigParser()
config.read('TwitterStream/src/config.ini') 

bearer_token = config['your.keys']['bearer_token']
api_key = config['your.keys']['api_key']
api_key_secret = config['your.keys']['api_key_secret']
access_token = config['your.keys']['access_token']
access_token_secret = config['your.keys']['access_token_secret']

client = tweepy.Client(bearer_token, api_key, api_key_secret, access_token, access_token_secret)

def get_home_timeline() -> tweepy.Response:
    """Get tweets from the timeline associated with the api_key

    Returns:
        tweepy.Response: tweepy object containing the tweets and some meta data
    """
    print("getting all timeline")
    return client.get_home_timeline(max_results = 20)

def get_recent_timeline(since_id) -> tweepy.Response:
    """_summary_

    Args:
        since_id (_type_): Id do último twitte lido

    Returns:
        tweepy.Response: tweepy object containing the tweets and some meta data
    """
    print("getting recent timeline")
    return client.get_home_timeline(since_id = since_id)


def print_tweets(response):
    for twitte in response.data:
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