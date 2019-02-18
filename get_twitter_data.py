import tweepy
import json


def oauth():
    """
    Return Tweeter access data.
    """
    return {"consumer_key": "0PlKlKMbNYWL9UeVuC6DPxX4B",
            "consumer_secret": "dpvpCGjA9udpjsPkCVfdxZhmAOLMXFeZcZEVLbH3usRiv8fHfN",
            "token_key": "963011359737774080-mYiiiIGOarKbuYGVdVTJBPcYC39RkqC",
            "token_secret": "f8031GVQo6dJXX35RRVbDlGxMcitrAt7uyAUVgKuO1E0R"}


def log_in(data):
    """
    Log in into your Tweeter API account and return api object.
    """
    auth = tweepy.OAuthHandler(data['consumer_key'], data['consumer_secret'])
    auth.set_access_token(data['token_key'], data['token_secret'])
    api = tweepy.API(auth)
    return api


def get_api_json(api):
    """
    Return JSON data by the Tweeter API object.
    """
    data = api.me()
    json_dict = json.loads(json.dumps(data._json))
    return json_dict


def get_value(key_str, json):
    """
    (str, dict) -> str
    Return an str value of the json dict file by its key represented as a str.
    key in a form 'key1 key2 ... keyN'
    """
    data = json
    keys = key_str.split()
    for key in keys:
        try:
            data = data[key]
        except KeyError:
            break
        if not isinstance(data, dict):
            return str(data)
    return str()
