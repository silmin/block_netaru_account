import json, config
from requests_oauthlib import OAuth1Session

import get_timeline
import search

# from config.py
CK = config.CONSUMER_KEY
CS = config.CONSUMER_SECRET
AT = config.ACCESS_TOKEN
ATS = config.ACCESS_TOKEN_SECRET

# certify
twitter = OAuth1Session(CK, CS, AT, ATS)

getMyTimeline();

# search
search_url = "https://api.twitter.com/1.1/search/tweets.json"
