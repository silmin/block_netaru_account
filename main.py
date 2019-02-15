import json, config
from requests_oauthlib import OAuth1Session

# from config.py
CK = config.CONSUMER_KEY
CS = config.CONSUMER_SECRET
AT = config.ACCESS_TOKEN
ATS = config.ACCESS_TOKEN_SECRET

# certify
twitter = OAuth1Session(CK, CS, AT, ATS)

# getMyTimeline
timeline_url = "https://api.twitter.com/1.1/statuses/user_timeline.json"
params = {'count': 2}
res = twitter.get(timeline_url, params = params)

if res.status_code == 200:
    timelines = json.loads(res.text)
    for line in timelines:
        print(line)
        '''
        print(line['user']['name'])
        print(line['text'])
        print(line['created_at']+'\n')
        '''
else :
    print("Faild: %d" % res.status_code)


# search
search_url = "https://api.twitter.com/1.1/search/tweets.json"

