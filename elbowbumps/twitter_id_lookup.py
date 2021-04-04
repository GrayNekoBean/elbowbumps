import requests
import os
import json
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


def auth():
    return os.getenv("BEARER_TOKEN")

def create_url_id(username):
    return "https://api.twitter.com/2/users/by/username/{}".format(username)


def get_params():
    return {"tweet.fields": "context_annotations"}


def create_headers(bearer_token):
    headers = {"Authorization": "Bearer {}".format(bearer_token)}
    return headers


def twitterID(user):
    bearer_token = auth()
    headers = create_headers(bearer_token)
    url_id = create_url_id(user)
    response = requests.request("GET", url_id, headers=headers, params={})
    #print(response.status_code)
    data = response.json()
    #print("Request returned an error: {} {}".format(response.status_code, response.text))
    if "errors" in data:
        return False
    else:
        data = response.json()
        return data["data"]["id"]




