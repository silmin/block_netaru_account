import json, config
from requests_oauthlib import OAuth1Session

from get_timeline import getTimeline
from search_word import searchWord

# from config.py
CK = config.CONSUMER_KEY
CS = config.CONSUMER_SECRET
AT = config.ACCESS_TOKEN
ATS = config.ACCESS_TOKEN_SECRET

# certify
twitter = OAuth1Session(CK, CS, AT, ATS)

getTimeline(twitter, 1)

flg, result = searchWord(twitter, "url:neta+ru.com", 5)


