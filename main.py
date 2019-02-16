import json 
from requests_oauthlib import OAuth1Session

import keys
from search_word import searchWord
from get_userid import getUserids
from block_user import blockUsers

import datetime

# from keys.py
CK = keys.CONSUMER_KEY
CS = keys.CONSUMER_SECRET
AT = keys.ACCESS_TOKEN
ATS = keys.ACCESS_TOKEN_SECRET

# certify
twitter = OAuth1Session(CK, CS, AT, ATS)


result = searchWord(twitter, "url:neta+ru.com exclude:retweets", 100)

if result != [] : 
    user_ids = getUserids(result)
    blockUsers(twitter, user_ids)

    print("-----------------------------")
    print(datetime.date.today())
    print(user_ids)
else :
    print("-----------------------------")
    print(datetime.date.today())
    print("error")
