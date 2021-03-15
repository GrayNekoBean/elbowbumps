import requests
import os
import json
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import os

def auth():
    return os.getenv("BEARER_TOKEN")



def create_url_tweets(user_id):
    return "https://api.twitter.com/2/users/{}/tweets".format(user_id)


def get_params():
    return {"tweet.fields": "context_annotations", "max_results" : 100}


def get_new_page_params(tweets_data):
    parameters = {"tweet.fields": "context_annotations"}
    if ('next_token' in tweets_data["meta"]):
        parameters["pagination_token"] = tweets_data["meta"]["next_token"]
    return parameters


def create_headers(bearer_token):
    headers = {"Authorization": "Bearer {}".format(bearer_token)}
    return headers


def connect_to_endpoint(url, headers, params={}):
    response = requests.request("GET", url, headers=headers, params=params)
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(
            "Request returned an error: {} {}".format(
                response.status_code, response.text
            )
        )

    return response.json()

def getTweets(user, category):
    bearer_token = auth()
    headers = create_headers(bearer_token)
    params = get_params()
    url_tweets = create_url_tweets(int(user))
    tweets_data = connect_to_endpoint(url_tweets, headers, params)
    if ('next_token' in tweets_data["meta"]):
        params = get_new_page_params(tweets_data)
        new_data = connect_to_endpoint(url_tweets, headers, params)
        for x in new_data["data"]:
            tweets_data["data"].append(x)
            tweets_data["meta"]["result_count"] = tweets_data["meta"]["result_count"] + 1

        while('next_token' in new_data["meta"]):
            params = get_new_page_params(new_data)
            new_data = connect_to_endpoint(url_tweets, headers, params)
            if "data" in new_data:
                for x in new_data["data"]:
                    tweets_data["data"].append(x)
                    tweets_data["meta"]["result_count"] = tweets_data["meta"]["result_count"] + 1
            else:
                break

    #print(json.dumps(tweets_data, indent=4, sort_keys=True))
    return categoryScore(tweets_data["data"])


def categoryScore(data):
     #so far does it for the category sport
    analyzer = SentimentIntensityAnalyzer()
    total = 0
    total_sen = 0
    sports_ids = [11, 12, 26, 27, 28, 39, 40, 60, 68, 138, 137, 92]
    for i in range(len(data)):
        if "context_annotations" in data[i]:
            for value in data[i]["context_annotations"]:
                if int(value["domain"]["id"]) in sports_ids:
                    sentence = data[i]["text"]
                    vs = analyzer.polarity_scores(sentence)
                    print("{:-<65} {}".format(sentence, str(vs)))
                    if vs["compound"] > 0.0: 
                        total = total + vs["compound"] 
                        total_sen +=1
                    break
    print("This is the number of tweets we thought had a sport" + str(total_sen))
    if total_sen == 0:
        return 0
    else:
        return total / total_sen
