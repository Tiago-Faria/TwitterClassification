import tweepy
from src.config import TwitterAccess
from src.handlers import TweetHandler
import time

class TweepyConnector:
    
    def get_client():
        client = tweepy.Client(TwitterAccess.bearer_token,
                               TwitterAccess.api_key,
                               TwitterAccess.api_key_secret, 
                               TwitterAccess.access_token, 
                               TwitterAccess.access_token_secret)
        return client
    
    # SE TIVER OUTROS STREAMERS MANTER A FUNÇÃO
    # TODO
    def get_streaming_conjunto1_params():
        return (TwitterAccess.bearer_token)


class TweetReader():
    
    def __init__(self):
        self.client = TweepyConnector.get_client()

    def get_home_timeline(self) -> tweepy.Response:
        """Get tweets from the timeline associated with the api_key

        Returns:
            tweepy.Response: tweepy object containing the tweets and some meta data
        """
        response = self.client.get_home_timeline(max_results = 20)
        self.newest_id = response.meta['newest_id']
        return response


    def get_recent_timeline(self, since_id) -> tweepy.Response:
        """_summary_

        Args:
            since_id (_type_): Id do último twitte lido

        Returns:
            tweepy.Response: tweepy object containing the tweets and some meta data
        """
        print("getting recent timeline")
        response = self.client.get_home_timeline(since_id = since_id)
        self.newest_id = response.meta['newest_id']
        return response

    def get_newest_id(self) -> int:
        """ gets the newest received tweet id 

        Returns:
            int: newest received tweet id
        """
        return self.newest_id




class TweetStreamer(tweepy.StreamingClient):
    
    def __init__(self, file_path, saving_time=20, verbose=True):
        super().__init__(TwitterAccess.bearer_token)
        self.file_path = file_path
        self.verbose = verbose
        
        self.tweets = []
        self.last_save = time.time()
        self.saving_time = saving_time
        self.languages = ['en']
    
    def set_languages(self, languages):
        self.languages = languages
        
    def on_tweet(self, tweet):
        if(tweet.lang not in self.languages):
            return
        TweetHandler.clean(tweet)
        self.tweets.append(tweet)
        
        time_now = time.time() 
        if(time.time() - self.last_save >= self.saving_time):
            self.save_tweets(timestamp = time_now)
    
    def on_closed(self, response):
        self.save_tweets()

    def start(self, threaded=True):
        if (self.verbose):
            print(f'Starting saving tweets every {self.saving_time} seconds!\n')
        super().sample(tweet_fields = ['lang','context_annotations','entities'], threaded = threaded)
    

    def stop(self):
        super().disconnect()
    
    def save_tweets(self, timestamp=None):
        if (self.verbose):
            print(f'Saving {len(self.tweets)} tweets...')
            
        TweetHandler.to_csv(self.tweets, self.file_path)
        self.tweets = []
        if timestamp is not None:
            self.last_save = timestamp