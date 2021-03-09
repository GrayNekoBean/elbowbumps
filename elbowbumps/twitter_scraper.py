import requests
import os
import json
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# To set your environment variables in your terminal run the following line:
# export 'BEARER_TOKEN'='<your_bearer_token>'


def auth():
    return os.environ.get("BEARER_TOKEN")



def create_url_tweets(user_id):
    return "https://api.twitter.com/2/users/{}/tweets".format(user_id)


def get_params():
    return {"tweet.fields": "context_annotations"}


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

    return categoryScore(tweets_data["data"])


def categoryScore(data):
     #so far does it for the category sport
    analyzer = SentimentIntensityAnalyzer()
    total = 0
    total_sen = 0
    for i in range(len(data)):
        if "context_annotations" in data[i]:
            for value in data[i]["context_annotations"]:
                print(value)
                if value["domain"]["name"] == "Sport":
                    print("You've got a sport")
                    sentence = data[i]["text"]
                    vs = analyzer.polarity_scores(sentence)
                    print("{:-<65} {}".format(sentence, str(vs)))
                    if vs["compound"] != 0:
                        total = total + vs["compound"]
                        total_sen +=1
    return total / total_sen
