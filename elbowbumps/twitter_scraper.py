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
    #print(response.status_code)
    if response.status_code != 200:
        raise Exception(
            "Request returned an error: {} {}".format(
                response.status_code, response.text
            )
        )

    return response.json()

def getTweets(user):
    MAX_TWEETS = 250
    bearer_token = auth()
    headers = create_headers(bearer_token)
    params = get_params()
    url_tweets = create_url_tweets(int(user))
    tweets_data = connect_to_endpoint(url_tweets, headers, params)

    if "meta" in tweets_data:
        if ('next_token' in tweets_data["meta"]):
            params = get_new_page_params(tweets_data)
            new_data = connect_to_endpoint(url_tweets, headers, params)
            for x in new_data["data"]:
                tweets_data["data"].append(x)
                tweets_data["meta"]["result_count"] = tweets_data["meta"]["result_count"] + 1
            while('next_token' in new_data["meta"] and tweets_data["meta"]["result_count"] < MAX_TWEETS):
                params = get_new_page_params(new_data)
                new_data = connect_to_endpoint(url_tweets, headers, params)
                if "data" in new_data:
                    for x in new_data["data"]:
                        tweets_data["data"].append(x)
                        tweets_data["meta"]["result_count"] = tweets_data["meta"]["result_count"] + 1
                else:
                    break
        #print(json.dumps(tweets_data, indent=4, sort_keys=True))
        if 'data' in tweets_data:
            return categoryScore(tweets_data["data"])
        else: 
            return 0
    else:
        return 0

def categoryScore(data):
    categories = {"sports": 
                    {"ids": [11, 12, 26, 27, 28, 39, 40, 60, 68, 138, 137, 92],
                    "total_sen": 0,
                    "score": 0,
                    "genre_id": [11],
                    "genre_scores" : {}},
                "films/tv": 
                    {"ids": [4, 117, 86, 87, 55, 56],
                    "total_sen": 0,
                    "score": 0,
                    "genre_id": [87,3],
                    "genre_scores" : {}},
                "music": 
                    {"ids": [54, 89, 132, 89, 90, 84],
                    "total_sen": 0,
                    "score": 0,
                    "genre_id": [84],
                    "genre_scores": {}},
                "video_games": 
                    {"ids": [71, 78, 79, 136, 137, 138, 115, 116],
                    "total_sen": 0,
                    "score": 0,
                    "genre_id": [71],
                    "genre_scores": {}}
            }
    scores = {}
  
    for i in range(len(data)):
        if "context_annotations" in data[i]:
            for value in data[i]["context_annotations"]:
                for cat in categories.values():      
                    if int(value["domain"]["id"]) in cat["ids"]:
                        score = sentimentScore(data[i]["text"])
                        cat["score"] = cat["score"] + score
                        cat["total_sen"] += 1
                        if (int(value["domain"]["id"]) in cat["genre_id"]) and ("entity" in value):
                            genre = value["entity"]["name"]
                            if genre in cat["genre_scores"]:
                                cat["genre_scores"][genre]["score"] += score
                                cat["genre_scores"][genre]["total_sen"] += 1
                            else:
                                cat["genre_scores"][genre] = {
                                    "score": score,
                                    "total_sen": 1
                                } 
                        break

                
    for name, cat in categories.items():
        if cat["total_sen"] != 0:
            scores[name] = cat["score"] / cat["total_sen"]
            for genre_name, genre in cat["genre_scores"].items():
                scores[genre_name] = genre["score"] / genre["total_sen"]
            #print(name + " : " + str(total))
    return scores

def sentimentScore(sentence):
    analyzer = SentimentIntensityAnalyzer()
    vs = analyzer.polarity_scores(sentence)
    #print("{:-<65} {}".format(sentence, str(vs)))
    return vs["compound"]
