from tweepy import Tweet
from src.handlers import TextHandler
import os
import csv
class TweetHandler:
        
    def print(tweet):
        print(tweet.id)
        print(tweet.data)
        print(' - - - - - - - \n')
    
    def show(tweets):
        tweet_list = [tweets] if (type(tweets)==Tweet) else tweets
        
        for tweet in tweet_list:
            TweetHandler.print(tweet)
    
    def clean(tweets):
        tweet_list = [tweets] if (type(tweets)==Tweet) else tweets
        
        for tweet in tweet_list:
            text = tweet.text
            text = TextHandler.remove_links(text)
            text = TextHandler.remove_whitespaces(text)
            #text = TextHandler.remove_tokens(text)
            #text = TextHandler.remove_ponctuations(text)
            tweet.text = text
    
    def to_csv(tweets, file_path):
        tweet_list = [tweets] if (type(tweets)==Tweet) else tweets

        columns = ['id', 'text','context_annotations','entities']
        if (not os.path.exists(file_path)):
            with open(file_path, 'w', encoding="utf-8", newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(columns)
        
        with open(file_path, 'a', encoding="utf-8", newline='') as csvfile:
            writer = csv.writer(csvfile)
            for tweet in tweet_list:
                 writer.writerow([tweet.id, str(tweet.text), str(tweet.context_annotations), str(tweet.entities)])
            
        


