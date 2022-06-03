from tweepy import Tweet

class TweetHandler:
        
    def print(tweet):
        print(tweet.id)
        print(tweet.data)
        print(' - - - - - - - \n')
    
    def show(tweets):
        tweet_list = [tweets] if (type(tweets)==Tweet) else tweets
        
        for tweet in tweet_list:
            TweetHandler.print(tweet)
    
    def clean_texts(tweets):
        tweet_list = [tweets] if (type(tweets)==Tweet) else tweets
        
        for tweet in tweet_list:
            text = tweet.text
            text = TextHandler.remove_links(text)
            #text = TextHandler.remove_tokens(text)
            #text = TextHandler.remove_ponctuations(text)
            tweet.text = text


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
