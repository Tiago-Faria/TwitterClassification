from src.utils import get_home_timeline, get_recent_timeline
from src.handlers import TweetHandler
import configparser
import tweepy
import time



def __main__():
    show_recent_timeline()
    start_receiver_loop()



def start_receiver_loop():
    
    # TODO - get newest_id
    newest_id = 321321
    while (True):
        response = get_recent_timeline(since_id = newest_id)

        if(response.data != None):
            newest_id = response.meta['newest_id']
            tweets = response.data
            TweetHandler.clean_texts(tweets)
            for tweet in reversed(tweets):
                TweetHandler.show(tweet)

        time.sleep(10)

def show_recent_timeline() -> int:
    """_summary_

    Returns:
        int: Id of the newest tweet
    """
    response = get_home_timeline()
    tweets = response.data
    TweetHandler.clean_texts(tweets)
    TweetHandler.show(tweets)



    

if __name__ == '__main__':
    __main__()