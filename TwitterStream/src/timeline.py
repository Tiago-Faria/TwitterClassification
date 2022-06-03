from src.utils import get_home_timeline, get_recent_timeline
import configparser
import tweepy
import time



def print_tweet(tweet):
    print(tweet.id)
    print(tweet.text)
    print(' --- ')

def print_all(tweets):
    for tweet in reversed(tweets):
        print_tweet(tweet)

def remove_links_from_text(text):
    http_inicio = text.find('https://')
    while(http_inicio != -1):
        http_len = text[http_inicio:].find(' ')
        if(http_len < 0):
            http_len = len(text[http_inicio:])

        text = text[:http_inicio] + '__link__' + text[http_inicio + http_len:]
        http_inicio = text.find('https://')
    return text

def process_tweets(tweets):
    for tweet in tweets:
        tweet.text = remove_links_from_text(tweet.text)
    return tweets

def start_receiver_loop(newest_id):
    while (True):
        response = get_recent_timeline(since_id = newest_id)

        if(response.data != None):
            newest_id = response.meta['newest_id']
            tweets = process_tweets(response.data)
            for tweet in reversed(tweets):
                print_tweet(tweet)

        time.sleep(10)

def show_recent_timeline() -> int:
    """_summary_

    Returns:
        int: Id of the newest tweet
    """
    response = get_home_timeline()
    newest_id = response.meta['newest_id']
    tweets = process_tweets(response.data)
    print_all(tweets)
    return newest_id


def __main__():
    newest_id = show_recent_timeline()
    start_receiver_loop(newest_id)

    

if __name__ == '__main__':
    __main__()