import configparser


config = configparser.ConfigParser()
config.read('TwitterStream/src/config.ini') 


class TwitterAccess:
    bearer_token = config['your.keys']['bearer_token']
    api_key = config['your.keys']['api_key']
    api_key_secret = config['your.keys']['api_key_secret']
    access_token = config['your.keys']['access_token']
    access_token_secret = config['your.keys']['access_token_secret']