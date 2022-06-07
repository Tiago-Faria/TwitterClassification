import tweepy
from src.config import TwitterAccess


class TweepyConnector:
    
    def get_client():
        client = tweepy.Client(TwitterAccess.bearer_token,
                               TwitterAccess.api_key,
                               TwitterAccess.api_key_secret, 
                               TwitterAccess.access_token, 
                               TwitterAccess.access_token_secret)
        return client
    
    def get_streaming_client():
        streamer = tweepy.StreamingClient(TwitterAccess.bearer_token)
        return streamer


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




class TweetStreamer:
    
    def __init__(self):
        self.streamer = TweepyConnector.get_streaming_client()