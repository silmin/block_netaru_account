import json
from requests_oauthlib import OAuth1Session

def blockUsers(twitter, user_ids) :
    url = "https://api.twitter.com/1.1/blocks/create.json"

    for user_id in user_ids:
        params = {'screen_name': user_id}
        twitter.post(url, params = params)
