import requests
import os
import json
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# To set your environment variables in your terminal run the following line:
# export 'BEARER_TOKEN'='<your_bearer_token>'


def auth():
    return os.environ.get("BEARER_TOKEN")

def create_url_id(username):
    return "https://api.twitter.com/2/users/by/username/{}".format(username)


def get_params():
    return {"tweet.fields": "context_annotations"}


def create_headers(bearer_token):
    headers = {"Authorization": "Bearer {}".format(bearer_token)}
    return headers


def twitterID(user):
    bearer_token = 'AAAAAAAAAAAAAAAAAAAAAGdUMwEAAAAAoATpgUpvx1d9mrcHPuHkkYLDJTo%3DABfbwqrBlaWD6pwE1lMgBzWjiZHZZZQ3QUrW4yq2439j7Od0hE'
    headers = create_headers(bearer_token)
    url_id = create_url_id(user)
    response = requests.request("GET", url_id, headers=headers, params={})
    print(response.status_code)
    data = response.json()
    if "errors" in data:
        #return "Request returned an error: {} {}".format(response.status_code, response.text)
        return False
    else:
        data = response.json()
        return data["data"]["id"]




