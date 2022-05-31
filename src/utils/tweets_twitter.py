import os
import json
import requests
import configparser


config = configparser.ConfigParser()
config.read('src/config.ini')

def auth():
    if ('your.keys' not in config.keys() or
        'bearer_token' not in config['your.keys'].keys()
    ):
        raise Exception('The environment variable TOKEN must be defined!')
    return config['your.keys']['bearer_token']


def create_query(keyword, max_results = 10):
    
    search_url = "https://api.twitter.com/2/tweets/search/recent" #Change to the endpoint you want to collect data from

    bearer_token = auth()
    headers = {"Authorization": "Bearer {}".format(bearer_token)}
    
    #change params based on the endpoint you are using
    query_params = {'query': keyword,
                    'max_results': max_results,
                    #'start_time': start_date,
                    #'end_time': end_date,
                    #'expansions': 'author_id,in_reply_to_user_id,geo.place_id',
                    #'tweet.fields': 'id,text,author_id,in_reply_to_user_id,geo,conversation_id,created_at,lang,public_metrics,referenced_tweets,reply_settings,source',
                    #'user.fields': 'id,name,username,created_at,description,public_metrics,verified',
                    #'place.fields': 'full_name,id,country,country_code,geo,name,place_type',
                    #'next_token': {}
                    }    
    
    return (search_url, headers, query_params)


def connect_to_endpoint(url, headers, params):
    response = requests.request("GET", url, headers = headers, params = params)
    print("Endpoint Response Code: " + str(response.status_code))
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    return response.json()


def get_tweets_related_to(keyword:str, max_results:int = 20) -> dict:

    url, headers, params = create_query(keyword, max_results)
    json_response = connect_to_endpoint(url, headers, params)

    return json.dumps(json_response, indent=4, sort_keys=True)
