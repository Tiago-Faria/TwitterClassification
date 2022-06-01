import configparser
import tweepy
from tweepy.asynchronous import AsyncClient
import asyncio

config = configparser.ConfigParser()
print(config.read('src/config.ini'))

bearer_token = config['your.keys']['bearer_token']
api_key = config['your.keys']['api_key']
api_key_secret = config['your.keys']['api_key_secret']
access_token = config['your.keys']['access_token']
access_token_secret = config['your.keys']['access_token_secret']

auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
client = tweepy.Client(bearer_token, api_key, api_key_secret, access_token, access_token_secret)

def get_home_timeline():
    print(client.get_home_timeline(max_results=20))
