import configparser
import tweepy

config = configparser.ConfigParser()
print(config.read('src/config.ini'))

api_key = config['your.keys']['api_key']
api_key_secret = config['your.keys']['api_key_secret']
access_token = config['your.keys']['access_token']
access_token_secret = config['your.keys']['access_token_secret']

auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

def get_timeline():
    return api.home_timeline()