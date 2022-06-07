from tweepy import Tweet
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
            text = TextHandler.remove_substr_from_text(text, '\n')
            #text = TextHandler.remove_tokens(text)
            #text = TextHandler.remove_ponctuations(text)
            tweet.text = text
    
    def to_csv(tweets, file_path):
        tweet_list = [tweets] if (type(tweets)==Tweet) else tweets

        columns = ['id', 'text']
        if (not os.path.exists(file_path)):
            with open(file_path, 'w', encoding="utf-8", newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(columns)
        
        with open(file_path, 'a', encoding="utf-8", newline='') as csvfile:
            writer = csv.writer(csvfile)
            for tweet in tweet_list:
                 writer.writerow([tweet.id, str(tweet.text)])
            
        


class TextHandler:
    
    def remove_links(text):
        http_inicio = text.find('https://')
        while(http_inicio != -1):
            http_len = text[http_inicio:].find(' ')
            if(http_len < 0):
                http_len = len(text[http_inicio:])

            text = text[:http_inicio] + '__link__' + text[http_inicio + http_len:]
            http_inicio = text.find('https://')
        return text

    def remove_substr_from_text(text,substr):
        return text.replace(substr,' ')