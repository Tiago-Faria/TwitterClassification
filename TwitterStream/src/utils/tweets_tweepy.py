import configparser
import tweepy

class TweetReader():

    def __init__(self):
        config = configparser.ConfigParser()
        config.read('TwitterStream/src/config.ini') 

        bearer_token = config['your.keys']['bearer_token']
        api_key = config['your.keys']['api_key']
        api_key_secret = config['your.keys']['api_key_secret']
        access_token = config['your.keys']['access_token']
        access_token_secret = config['your.keys']['access_token_secret']

        self.client = tweepy.Client(bearer_token, api_key, api_key_secret, access_token, access_token_secret)


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
