import configparser
import tweepy

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
    return client.get_home_timeline()


def get_recent_timeline(since_id) -> tweepy.Response:
    """_summary_

    Args:
        since_id (_type_): Id do último twitte lido

    Returns:
        tweepy.Response: tweepy object containing the tweets and some meta data
    """
    return client.get_home_timeline(since_id = since_id)